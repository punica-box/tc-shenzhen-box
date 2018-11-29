#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from boa.builtins import concat, sha256, state, ToScriptHash
from boa.interop.System.Runtime import CheckWitness, Serialize, Deserialize, GetTime, Notify
from boa.interop.System.Storage import GetContext, Put, Get
from boa.interop.Ontology.Native import Invoke


OPERATIONS = [
    'grant_copyright',      # 授权
    'check_copyright',      # 检查授权
    'create_copyright',     # 创建版权
    'transfer_copyright',   # 交易版权
    'buy_copyright',        # 购买版权
]

OWNER_KEY_PREFIX = 'copyright_owner_'
GRANTS_KEY_PREFIX = 'copyright_grants_'

ctx = GetContext()


def Main(operation, args):
    if operation == 'grant_copyright':
        return grant_copyright(args[0], args[1], args[2])
    elif operation == 'check_copyright':
        return check_copyright(args[0], args[1])
    elif operation == 'create_copyright':
        return create_copyright(args[0], args[1])
    elif operation == 'transfer_copyright':
        return transfer_copyright(args[0], args[1])
    elif operation == 'buy_copyright':
        return buy_copyright(args[0], args[1])
    else:
        return False


def create_copyright(address, copyright):
    copyright = sha256(copyright)
    if not CheckWitness(address):
        return False

    if check_owner_exists(copyright):
        return False

    Notify(['create', copyright, address])

    return set_owner(copyright, address)


def check_copyright(copyright, address):
    copyright = sha256(copyright)
    owner = get_owner(copyright)
    if owner == address:
        return True

    grants = get_grants(copyright)
    if not grants:
        return False

    for grant, expired in grants:
        if grant == address:
            return expired is None or expired > GetTime()

    return False


def grant_copyright(copyright, address, expired):
    copyright = sha256(copyright)
    if not check_owner(copyright):
        return False

    Notify(['grant', copyright, address])

    return put_grants(copyright, address, expired)


def transfer_copyright(copyright, address):
    copyright = sha256(copyright)
    if not check_owner(copyright):
        return False

    Notify(['transfer', copyright, address])

    return set_owner(copyright, address)


def buy_copyright(copyright, address):
    copyright = sha256(copyright)
    if check_owner(copyright):
        return False
    owner_adr = get_owner(copyright)

    Notify(['buy', copyright, address])

    param = state(address, owner_adr, 10)
    OntContract = ToScriptHash("AFmseVrdL9f9oyCzZefL9tG6UbvhUMqNMV")

    res = Invoke(0, OntContract, "transfer", [param])
    if res != b'\x01':
        raise Exception("transfer ont error.")
    Notify("transferONT succeed")
    return put_grants(copyright, address, 120)


def get_owner(copyright):
    key = get_key(OWNER_KEY_PREFIX, copyright)
    return Get(ctx, key)


def set_owner(copyright, address):
    key = get_key(OWNER_KEY_PREFIX, copyright)
    return Put(ctx, key, address)


def check_owner(copyright):
    owner = get_owner(copyright)
    return owner and CheckWitness(owner)


def check_owner_exists(copyright):
    owner = get_owner(copyright)
    return not not owner


def get_grants(copyright):
    key = get_key(GRANTS_KEY_PREFIX, copyright)
    grants = Get(ctx, key)
    if not grants:
        return False

    return [Deserialize(x) for x in grants]


def put_grants(copyright, address, expired):
    key = get_key(GRANTS_KEY_PREFIX, copyright)

    grants = get_grants(copyright)
    if not grants:
        grants = []

    grants.append([address, GetTime() + expired if expired != 0 else None])
    serialized = [Serialize(x) for x in grants]
    return Put(ctx, key, serialized)


def get_key(prefix, copyright):
    return concat(prefix, copyright)
