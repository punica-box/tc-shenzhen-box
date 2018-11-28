
# coding: utf-8

# # <center><font color='#333333'>TechCrunch Shen Zhen Hackathon</font></center>
# ## <center><font color='#808080'>Ontology Challenge</font></center>
# ### <center><font color='#3b5998'>Created by cyda - Yeung Wong & Carrie Lo</font></center>

# --------------------------------------------------------------------------------------
# ![logo](https://4.bp.blogspot.com/-LAXjdvVCYCU/WxeQFKQ-1wI/AAAAAAAAACs/o8IJ1eLLAEwQYv2Az7EqQi9jODTqRx7wACK4BGAYYCw/s1000/tight%2Bbanner_with_description.png)

# --------------------------------------------------------------------------------------
# Please acknowledge <b>team cyda - Yeung Wong and Carrie Lo</b> when using the code
# 
# <b><font color='#3b5998'>If you find this script is helpful, please feel free to endorse us through Linkedin!</font></b>
# 
# <b>Linkedin:</b>
# 
# Yeung Wong - https://www.linkedin.com/in/yeungwong/
# 
# Carrie Lo - https://www.linkedin.com/in/carrielsc/

# In[ ]:


import face_recognition
import cv2
video_capture = cv2.VideoCapture(0)
valid_image = face_recognition.load_image_file("valid.jpg")
valid_face_encoding = face_recognition.face_encodings(valid_image)[0]
known_face_encodings = [valid_face_encoding]
known_face_names = ["Valid"]
face_locations = []
face_encodings = []
face_names = []
process_this_frame = True
while True:
    ret, frame = video_capture.read()
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    rgb_small_frame = small_frame[:, :, ::-1]
    if process_this_frame:
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)
        face_names = []
        for face_encoding in face_encodings:
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
            name = "Unknown"
            if True in matches:
                first_match_index = matches.index(True)
                name = known_face_names[first_match_index]
            face_names.append(name)
    process_this_frame = not process_this_frame
    for (top, right, bottom, left), name in zip(face_locations, face_names):
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)
    cv2.imshow('Video', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
video_capture.release()
cv2.destroyAllWindows()
import os
import binascii
from ontology.smart_contract.neo_contract.abi.abi_info import AbiInfo
from ontology.ont_sdk import OntologySdk
from ontology.wallet.wallet_manager import WalletManager
from ontology.account.account import Account
dict_abi = {"contractHash":"8bc0f46814f436cfb2ffe7bf95ad61e6db0db213","abi":{"functions":[{"name":"Main","parameters":[{"name":"operation","type":""},{"name":"args","type":""}],"returntype":""},{"name":"Save_Manufacture_Data","parameters":[{"name":"manufacture_date","type":""},{"name":"manufacture_time","type":""},{"name":"manufacture_origin","type":""},{"name":"manufacture_company","type":""},{"name":"manufacture_people","type":""},{"name":"manufacture_medicine_name","type":""},{"name":"manufacture_expiry_date","type":""},{"name":"manufacture_ingredient1","type":""},{"name":"manufacture_amount1","type":""},{"name":"manufacture_ingredient2","type":""},{"name":"manufacture_amount2","type":""},{"name":"manufacture_ingredient3","type":""},{"name":"manufacture_amount3","type":""},{"name":"manufacture_ingredient4","type":""},{"name":"manufacture_amount4","type":""},{"name":"manufacture_ingredient5","type":""},{"name":"manufacture_amount5","type":""},{"name":"manufacture_ingredient6","type":""},{"name":"manufacture_amount6","type":""},{"name":"manufacture_ingredient7","type":""},{"name":"manufacture_amount7","type":""},{"name":"manufacture_ingredient8","type":""},{"name":"manufacture_amount8","type":""}],"returntype":""},{"name":"Get_Manufacture_Data","parameters":[{"name":"","type":""}],"returntype":""},{"name":"Save_Storage_Data","parameters":[{"name":"storage_location","type":""},{"name":"storage_condition","type":""},{"name":"storage_temperature","type":""},{"name":"storage_humidity","type":""},{"name":"storage_warehouse","type":""},{"name":"storage_start_date","type":""},{"name":"storage_end_date","type":""}],"returntype":""},{"name":"Get_Storage_Data","parameters":[{"name":"","type":""}],"returntype":""},{"name":"Save_Logistics_Data","parameters":[{"name":"logistics_ship_company","type":""},{"name":"logistics_ship_model","type":""},{"name":"logistics_ship_date","type":""},{"name":"logistics_arrive_date","type":""},{"name":"logistics_origin","type":""},{"name":"logistics_destination","type":""}],"returntype":""},{"name":"Get_Logistics_Data","parameters":[{"name":"","type":""}],"returntype":""},{"name":"Save_Distribution_Data","parameters":[{"name":"distribution_date","type":""},{"name":"distribution_time","type":""},{"name":"distribution_company","type":""},{"name":"distribution_people","type":""},{"name":"distribution_buyer","type":""},{"name":"distribution_amount","type":""}],"returntype":""},{"name":"Get_Distribution_Data","parameters":[{"name":"","type":""}],"returntype":""}]}}
abi_info = AbiInfo(dict_abi['contractHash'], dict_abi.get('entrypoint',''), dict_abi['abi']['functions'], dict_abi.get('events',''))
manufacture_date = '3 Aug 2017'
manufacture_time = '11:03 A.M.'
manufacture_origin = 'India'
manufacture_company = 'Getwell Oncology'
manufacture_people = 'Machon Christ'
manufacture_medicine_name = 'Gefitinib Tablets IP'
manufacture_expiry_date = '20 Nov 2025'
manufacture_ingredient1 = 'Gardasil'
manufacture_amount1 = '0.225mg'
manufacture_ingredient2 = 'Thiomersal'
manufacture_amount2 = '0.103mg'
manufacture_ingredient3 = 'Human Serum Albumin'
manufacture_amount3 = '0.097mg'
manufacture_ingredient4 = 'Recombinant human serum albumin'
manufacture_amount4 = '0.093mg'
manufacture_ingredient5 = 'Gelatine'
manufacture_amount5 = '0.076mg'
manufacture_ingredient6 = 'Monosodium glutamate'
manufacture_amount6 = '0.054mg'
manufacture_ingredient7 = 'Ovalbumin'
manufacture_amount7 = '0.023mg'
manufacture_ingredient8 = 'Sorbitol and other stabilisers'
manufacture_amount8 = '0.009mg'
storage_location = 'Caloni District, India'
storage_condition = 'Good'
storage_temperature = '23 degree celsius'
storage_humidity = '65%'
storage_warehouse = 'Onergy Max. Ltd.'
storage_start_date = '4 Aug 2017'
storage_end_date = '17 Oct 2017'
logistics_ship_company = 'Seagull Shipping Ltd.'
logistics_ship_model = 'KX438'
logistics_ship_date = '17 Oct 2017'
logistics_arrive_date = '28 Dec 2017'
logistics_origin = 'Varoni Harbor, India'
logistics_destination = 'Shen Zhen Harbor, China'
distribution_date = '18 Nov 2018'
distribution_time = '14:23 P.M.'
distribution_company = 'Tai Sin Medicine Ltd.'
distribution_people = 'Chan Tai Fung'
distribution_buyer = 'Mr. Piglet'
distribution_amount = 'RMB $5400.00'
save_manufacture_func = abi_info.get_function('Save_Manufacture_Data')
save_manufacture_func.set_params_value((manufacture_date,manufacture_time,manufacture_origin,manufacture_company,manufacture_people,manufacture_medicine_name,manufacture_expiry_date,manufacture_ingredient1,manufacture_amount1,manufacture_ingredient2,manufacture_amount2,manufacture_ingredient3,manufacture_amount3,manufacture_ingredient4,manufacture_amount4,manufacture_ingredient5,manufacture_amount5,manufacture_ingredient6,manufacture_amount6,manufacture_ingredient7,manufacture_amount7,manufacture_ingredient8,manufacture_amount8))
save_storage_func = abi_info.get_function('Save_Storage_Data')
save_storage_func.set_params_value((storage_location,storage_condition,storage_temperature,storage_humidity,storage_warehouse,storage_start_date,storage_end_date))
save_logistics_func = abi_info.get_function('Save_Logistics_Data')
save_logistics_func.set_params_value((logistics_ship_company,logistics_ship_model,logistics_ship_date,logistics_arrive_date,logistics_origin,logistics_destination))
save_distribution_func = abi_info.get_function('Save_Distribution_Data')
save_distribution_func.set_params_value((distribution_date,distribution_time,distribution_company,distribution_people,distribution_buyer,distribution_amount))
acct = Account('f7bfe8f8ed0cf33a2321bbbdd0c621ef2826d22d16d087a950a2a8f57a128239')
rpc_address = 'http://polaris3.ont.io:20336'
sdk = OntologySdk()
sdk.rpc.set_address(rpc_address)
contract_address_hex = b'8bc0f46814f436cfb2ffe7bf95ad61e6db0db213'
contract_address_bytearray=bytearray(binascii.a2b_hex(contract_address_hex))
contract_address_bytearray.reverse()
gas_limit=20000000
gas_price=500
manufacture_tx_hash = sdk.neo_vm().send_transaction(contract_address_bytearray,acct,acct,gas_limit,gas_price,save_manufacture_func,False)
print(manufacture_tx_hash)
sdk.rpc.get_smart_contract_event_by_tx_hash(manufacture_tx_hash)
storage_tx_hash = sdk.neo_vm().send_transaction(contract_address_bytearray,acct,acct,gas_limit,gas_price,save_storage_func,False)
print(storage_tx_hash)
sdk.rpc.get_smart_contract_event_by_tx_hash(storage_tx_hash)
logistics_tx_hash = sdk.neo_vm().send_transaction(contract_address_bytearray,acct,acct,gas_limit,gas_price,save_logistics_func,False)
print(logistics_tx_hash)
sdk.rpc.get_smart_contract_event_by_tx_hash(logistics_tx_hash)
distribution_tx_hash = sdk.neo_vm().send_transaction(contract_address_bytearray,acct,acct,gas_limit,gas_price,save_distribution_func,False)
print(distribution_tx_hash)
sdk.rpc.get_smart_contract_event_by_tx_hash(distribution_tx_hash)

