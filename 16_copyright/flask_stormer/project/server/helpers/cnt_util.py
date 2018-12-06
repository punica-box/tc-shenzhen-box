from flask import current_app as app


def create_copyright_to_contract(ont_id_acct: Account, copyright: str) -> str:
    create_copyright_func = app.config['ABI_INFO'].get_function('create_copyright')
    ont_id_acct_bytes = ont_id_acct.get_address().to_array()
    create_copyright_func.set_params_value((ont_id_acct_bytes, copyright))
    gas_limit = app.config['GAS_LIMIT']
    gas_price = app.config['GAS_PRICE']
    contract_address_bytearray = app.config['CONTRACT_ADDRESS_BYTEARRAY']
    tx_hash = app.config['ONTOLOGY'].neo_vm().send_transaction(contract_address_bytearray,
                                                               ont_id_acct, ont_id_acct,
                                                               gas_limit, gas_price,
                                                               create_copyright_func, False)
    return tx_hash
