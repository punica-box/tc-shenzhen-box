import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["ont"]
mycol = mydb["oep_token"]

mylist = [
    {"contractAddress": "9d70f2d7fd2a2318c611ae8feb4f7bf067ba680e", "name": "HACK111" , "symbol":"HA"},
    {"contractAddress": "9482aee6844b6607562da739effb7a9819b3938c", "name": "HACKATHON2018SZ" , "symbol":"HACK"},
]

x = mycol.insert_many(mylist)

# 输出插入的所有文档对应的 _id 值
print(x.inserted_ids)