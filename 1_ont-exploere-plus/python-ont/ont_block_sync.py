import binascii

from ontology.ont_sdk import OntologySdk
from ontology.wallet.wallet_manager import WalletManager
import requests
import time
import pymongo
from ontology.common.address import Address
from ontology.utils import util


class OntBlockSync:

    def __init__(self):
        rpc_address = 'http://polaris1.ont.io:20336'
        self.rest_address = 'http://polaris3.ont.io:20334'

        self.sdk = OntologySdk()
        self.sdk.rpc.set_address(rpc_address)
        base58_address = "AKErtiRYq83f4f54WhiDHxs2piqG1QoNE4"
        address_balance = self.sdk.rpc.get_balance(base58_address)
        self.ont_balance = address_balance['ont']
        self.ong_balance = address_balance['ong']

        myclient = pymongo.MongoClient("mongodb://localhost:27017/")
        mydb = myclient["ont"]
        self.smt_block = mydb["smt_block"]
        self.oep_token = mydb["oep_token"]

    def query_symbol(self):
        asset = self.sdk.native_vm().asset()
        token_symbol_ont = asset.query_symbol('ont')
        token_symbol_ong = asset.query_symbol('ong')

        print(token_symbol_ont, token_symbol_ong)

    def print_balance(self):
        return {"ont": self.ont_balance, "ong": self.ong_balance}

    def get_oep4_name(self):
        oep4 = self.sdk.neo_vm().oep4()
        contract_address = '9d70f2d7fd2a2318c611ae8feb4f7bf067ba680e'
        oep4.set_contract_address(contract_address)

        oep4_name = oep4.get_name()
        oep4_symbol = oep4.get_symbol()
        oep4_total_supply = oep4.get_total_supply()
        balance = oep4.balance_of('AKErtiRYq83f4f54WhiDHxs2piqG1QoNE4')
        balance2 = oep4.balance_of('AecaeSEBkt5GcBCxwz1F41TvdjX3dnKBkJ')

        print(oep4_name, oep4_symbol, oep4_total_supply, balance, balance2)
        return oep4_name

    def create_account(self):
        wm = WalletManager()
        label = 'leec'
        password = '123'
        acct = wm.create_account(label, password)
        print(acct)

    def get_leatest_block(self):
        res = requests.get(self.rest_address + '/api/v1/block/height')
        snapshot = res.json()
        print(snapshot['Result'])  # 当前高度

    def get_smartcode_by_height(self, height):

        res = requests.get(self.rest_address + '/api/v1/smartcode/event/transactions/' + height)
        snapshot = res.json()
        print(snapshot)

    def get_smartcode_by_hash(self, hash):
        res = requests.get(self.rest_address + '/api/v1/smartcode/event/txhash/' + hash)
        snapshot = res.json()
        print(snapshot['Result'])

    # 通过 python sdk
    def get_curr_block_height(self):
        current_block_height = self.sdk.rpc.get_block_count()
        print(current_block_height)

    def get_curr_block(self):
        current_block_hash = self.sdk.rpc.get_current_block_hash()
        print(current_block_hash)

    def get_block_by_height(self, height):
        block = self.sdk.rpc.get_block_by_height(height)
        print(block)

    def get_block_by_hash(self, hash):
        block = self.sdk.rpc.get_block_by_hash(hash)
        print(block)

    def get_sm_evt_by_hash(self, hash):

        event = self.sdk.rpc.get_smart_contract_event_by_tx_hash(hash)
        print(event)

    def get_sm_evt_by_height(self, height):

        event = self.sdk.rpc.get_smart_contract_event_by_height(height)
        print(event)

    # 开始同步区块

    def save_block_to_db(self, sync_block_height):
        print('开始后同步区块 height:', sync_block_height)

        current_block = self.sdk.rpc.get_block_by_height(sync_block_height)
        curr_timestamp = current_block['Header']['Timestamp']
        print('当前区块的 timestamp', curr_timestamp)  # 当前区块的 timestamp

        curr_smc_evt = self.sdk.rpc.get_smart_contract_event_by_height(sync_block_height)

        if curr_smc_evt == None:  # 如果当前区块没有smart contract交易数据
            # print('curr smc evt none ')

            insert_data_one = {
                'block_height': sync_block_height,
                'timestamp': curr_timestamp
            }

            insert_res = self.smt_block.insert_one(insert_data_one)
            # print(insert_res)

            print('height:', sync_block_height, ' 同步完成，该区块没有智能合约交易')
            return False

        if len(curr_smc_evt) > 0:  # 如果当前区块有smart contract交易数据

            insert_data = []
            for transation in curr_smc_evt:
                # print(transation['Notify'])
                for n in transation['Notify']:
                    contractAddress = n['ContractAddress']
                    states = n['States']
                    # print(contractAddress, states)

                    insert_data.append({
                        'block_height': sync_block_height,
                        'timestamp': curr_timestamp,
                        'contractAddress': contractAddress,
                        'states': states
                    })

            # print(insert_data)
            insert_res = self.smt_block.insert_many(insert_data)
            # print(insert_res)
            print('height:', sync_block_height, ' 同步完成，该区块存在智能合约交易', len(insert_data), ' tx')

    def sync_block_loop(self):
        start_block_height = 431300  # 设置从哪个区块高度开始同步

        current_block_height = self.sdk.rpc.get_block_count() - 1

        # current_block_height = 431183
        # print(current_block_height)

        # 查询当前数据库中的区块高度
        sort_block_res_count = self.smt_block.find().count()
        if (sort_block_res_count == 0):
            print('数据库中没有数据')

            least_db_block_height = start_block_height
        else:
            sort_block_res = self.smt_block.find().sort('block_height', -1)
            # print(sort_block_res)

            least_db_block_height = sort_block_res[0]['block_height']

            print('数据库中的block height max:', least_db_block_height)

        # return False

        # 比较数据库中存在数据的最高高度 与 当前高度对比
        print('当前高度：', current_block_height)
        print('数据库中存在数据的最高高度：', least_db_block_height)

        if (current_block_height <= least_db_block_height):
            return False

        sync_block_height = least_db_block_height  # 当前同步区块

        while (sync_block_height < current_block_height - 1):  # if 当前要同步的区块height <  当前主网的区块高度

            sync_block_height = sync_block_height + 1

            time.sleep(1)  # 1s 同步一笔

            print('-' * 50)

            if self.save_block_to_db(sync_block_height) == False:
                continue

        print('全部数据同步完成')

        print('*' * 50)

    # 永久循环 同步db
    def sync_block_loop_forever(self):
        while True:
            self.sync_block_loop()
            time.sleep(3)  # wait 3s

    # 列出认证的oep4 token list
    def list_oep4_token(self):

        res = []
        for t in self.oep_token.find():
            res.append({
                "smc_addr": t['contractAddress'],
                "name": t['name'],
                "symbol": t['symbol']
            })

        return res

    # 查询 oep4 token detail
    def query_oep4_detail(self, contractAddress):
        oep4 = self.sdk.neo_vm().oep4()
        oep4.set_contract_address(contractAddress)

        print(oep4.get_symbol())
        print(oep4.get_total_supply())

        decimal = oep4.get_decimal()

        total_supply = oep4.get_total_supply() / (10 ** decimal)

        return {
            "smc_addr": contractAddress,
            "name": oep4.get_name(),
            "symbol": oep4.get_symbol(),
            "total_supply": total_supply,
            "decimal": decimal
        }

    # 查询 oep4 数据
    def query_oep4_token_transfer(self, contractAddress):

        sm_res = self.smt_block.find({'contractAddress': contractAddress})

        res = []

        oep4 = self.sdk.neo_vm().oep4()
        oep4.set_contract_address(contractAddress)
        decimal = oep4.get_decimal()

        for sm in sm_res:
            print(sm)

            if len(sm['states']) != 4:
                continue

            if self.hex_to_str(sm['states'][0]) == 'transfer':
                # 需要进行转换
                timestamp = sm['timestamp']
                from_addr = sm['states'][1]
                to_addr = sm['states'][2]
                trans_amount = sm['states'][3]
                trans_amount = bytearray(binascii.a2b_hex(trans_amount))
                trans_amount.reverse()
                trans_amount = binascii.b2a_hex(trans_amount)
                trans_amount = int(trans_amount, 16) / (10 ** decimal)

                from_addr = Address(binascii.a2b_hex(from_addr)).b58encode()
                to_addr = Address(binascii.a2b_hex(to_addr)).b58encode()
                print(from_addr, to_addr, trans_amount, timestamp)

                res.append({
                    "from_addr": from_addr,
                    "to_addr": to_addr,
                    "trans_amount": trans_amount,
                    "timestamp": timestamp
                })

        return res

    # 将 hex 转成 string
    def hex_to_str(self, hex):
        return bytes.fromhex(hex).decode('utf-8')


if __name__ == '__main__':

    ont_sync = OntBlockSync()
    ont_sync.sync_block_loop_forever()
