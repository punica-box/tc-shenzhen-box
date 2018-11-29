import time
import pandas as pd
import numpy as np
import networkx as nx
import itertools
import requests

from django.db import IntegrityError

URL = "https://explorer.ont.io/api/v1/explorer/transactionlist/20/{}"
TURL =  "https://explorer.ont.io/api/v1/explorer/transaction/{}"

from threading import Thread
from ontofraud.models import Wallet, Transaction


def sync_transactions_via_api(page):
    response = requests.get(URL.format(page))
    if response.status_code == 200:
        for txn in response.json()['Result']['TxnList']:
            t_response = requests.get(TURL.format(txn['TxnHash']))
            if t_response.status_code == 200:
                try:
                    transfer_list = t_response.json()['Result']['Detail']['TransferList']
                    for transfer in transfer_list:
                        if transfer['Description'] != 'gasconsume':
                                from_address, _ = Wallet.objects.get_or_create(hashid=transfer['FromAddress'])
                                to_address, _ = Wallet.objects.get_or_create(hashid=transfer['ToAddress'])
                                Transaction.objects.create(amount=transfer['Amount'],
                                                           from_address=from_address,
                                                           to_address=to_address,
                                                           hashid=txn['TxnHash'],
                                                           description=transfer['Description'])
                except (KeyError, IntegrityError):
                    print(txn)
            else:
                print('Txn Response: {}'.format(t_response.status_code))

    else:
        print('Response: {}'.format(response.status_code))


def sync_with_offset(i):
    for j in range(1000):
        sync_transactions_via_api(i + j * 10)


def run_sync():
    for i in range(10000, 20100, 10):
        try:
            if i % 100:
                print("PAGE: ", i)
            sync_transactions_via_api(i)
        except Exception as ex:
            print(ex)
            time.sleep(5)


def get_csv():
    f = open('f.csv', 'w')
    for t in Transaction.objects.all():
        f.write("{},{},{}\n".format(t.from_address.hashid, t.to_address.hashid, t.amount))
    f.close()


def validate_wallet(source, targets, data):
    colnames = ['source', 'target', 'coins']
    data = pd.DataFrame.from_records(data, columns=colnames)
    G = nx.from_pandas_edgelist(data)
    G.remove_nodes_from(list(nx.isolates(G)))

    sources = [source]  # For example, sources = [0,1,4]
    max_shortest_path = None
    for (s, t) in itertools.product(sources, targets):
        if s == t: continue  # Ignore  src can not be equal to dst
        shortest_paths = list(nx.all_shortest_paths(G, s, t))
        path_len = len(shortest_paths[0])
        if path_len <= 3:
            max_shortest_path = list(shortest_paths)  # Copy shortest_paths list

    if max_shortest_path is not None and len(max_shortest_path) >= 0:
        return 'fraud'
    return 'ok'
