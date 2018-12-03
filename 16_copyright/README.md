     _  _         _        _   _               _____ ___ 
    | || |__ _ __| |____ _| |_| |_  ___ _ _   |_   _/ __|
    | __ / _` / _| / / _` |  _| ' \/ _ \ ' \    | || (__ 
    |_||_\__,_\__|_\_\__,_|\__|_||_\___/_||_|   |_| \___|
       ___  ___ ______    ______                __          
      |_  |/ _ <  ( _ )  / __/ /  ___ ___  ___ / /  ___ ___ 
     / __// // / / _  | _\ \/ _ \/ -_) _ \/_ // _ \/ -_) _ \
    /____/\___/_/\___/ /___/_//_/\__/_//_//__/_//_/\__/_//_/
                                                            

### 1. 预选课题：

Special Task:
Ontology Challenge by Ontology

Task:
1.Try to build an application for real-world scenarios using modules provided byOntology – digital identity and/or data exchange (DDXF).
2.Try to enhance Ontology modules (OWallet, DID, OEPs,  ) by adding new features/functions/GUIs or create new ones for whatever cases that you assume to be valuable.
3.Try to enhance Ontology blockchain explorer with rich functions designed for dAppsoverview and detailed view, also with highly customizable interface which is adaptable for real world business (both public and private chains).

Suggestions:
1.Easy to play games integrated with ONT ID and digital asset management.
2.Decentralize a sophisticated reputation rating algorithm on Ontology andintegrated with certain modules.
3.User friendly dApp statistical analysis framework with graphics and customizable
4.Open API for integrating OEP-4, OEP-5 and OEP-8 assets into to a wallet with orwithout ONT compatibility.
5.Optimization for Ontology development toolkit SmartX, Punica (more available on GitHub) etc.
6.Transfer dApps from Ethereum, EOS or any other blockchain platform.
7.Or any ideas that you think are valuable for Ontology technology and ecosystem.

Prizes:
First Prize: 10,000 USD in ONT
Second Prize: 5,000 USD in ONT
Third Prize: 3,000 USD in ONT

Special Prizes:
The Best Creative Prize: 1,000 USD in ONT
The Best User Experience Prize: 1,000 USD in ONT

### 2. 说明

1. 资源：

    - ontology 开发文档: [onto dev doc](https://ontio.github.io/documentation/tutorial_for_developer_zh.html).
    - Python sdk api: [sdkapi](https://apidoc.ont.io/pythonsdk/#introduction).
      Ontology python: [ontopy](https://github.com/ontio/ontology-python-sdk).
    - ontology cli guide： [cli_guide](https://ontio.github.io/documentation/cli_user_guide_zh.html).
    - dapp: [dapp](https://www.dapp.com/search).
    - 其他[^foot1]
    - vul-sea「45.76.243.92」

    - ontology去中心化数据交易框架DDXF
      [DDXF](https://ontio.github.io/documentation/DDXF_zh.html).
    - Ontology TypeScript SDK 开发者手册:
      [Ontology TypeScript SDK](https://ontio.github.io/documentation/ontology_ts_sdk_zh.html).

### 3. Schedule
Day1: 

- 开始时间为**11月17号上午9:00**.
- 9:00-11:00， Sign in&Team up, Introduction of Principles.
- 11:00-11:30，找好座位能把自己的设备弄好就不错了...
- 11:30-13:00，午餐及休息时间.
- **13:00-18:00** 几乎仅有的全部开发时间，确保能完成的点跑通，传达产品功能点即可.
- 18:00--19:00，休息时间，按需再整理下代码.

Day2:

- 9:30-11:30   Free developing.
- 11:30-13:00，午餐及休息时间.
- 13:30-15:00，Demo/Presentation time for teams 3mins for each team.
- 15:00-16:00，Review and reward.

### 4. TODO
- 产品想法
  - ~~「人类简史」~~
  - ~~「结婚登记」~~
  - ？
  - [x] **版权系统 版权的签发/转让/授权/验证**
  
### 5. FUC

```commands
  ./ontology --rest --testmode --gasprice 0 --gaslimit 10                     # start on test mode
  ./ontology account list                                                     # account list
  ./ontology asset balance <address|index|label>                              # account balance
  ./ontology asset transfer --from= --to= --amount= --asset=ont               # balance transfer

  # contract deploy & invoke
  ./ontology contract deploy --code hello.avm --name 'Hello' --version '1.0' --author 'ester' --email 'tester@test.com' --desc 'helloWorld' --account 1 --gaslimit 1000
  ./ontology contract invoke --address 362cb5608b3eca61d4846591ebb49688900fedd0 --params string:Hello,[string:tester] --gaslimit 200000
```

### 6. 课题计划

#### 课题核心

使用区块链的不可否认性，利用智能合约，解决版权的授权/验证问题。

#### 概念

- 版权物。版权物即版权标的物品，在此合约内，以唯一哈希值的形式存在。
- 权限。版权物的权限分为两种，使用权和所有权。所有权可以签发使用权，所有权可以进行转让，使用权不可转让。
- 验证。验证用户U对版权物C的权限，及所有权或使用权或无权限。

#### 功能点

- 版权签发
用户U1可以对自己的版权创作物C1进行签发，声明所有权。

- 版权转让
在用户U2付出等价物后，可以向用户U1购买版权C1，此时，所有权从U1转让至U2。

- 版权授权
版权C1的所有者U1可以对其他人如U3进行使用授权，授权后，U1对C1的所有权不变，U2获得C1的使用权。

- 版权收回
在到期后，U3拥有的C1使用权会自动取消。

~~另外在U1和U3同意的前提下，可以协商取消U3对C1的使用权~~

- 版权验证
验证用户U1是否有对版权C1的所有权。

验证用户U2是否有对版权C1的所有权。

验证用户U3是否有队版权C1的使用权。

#### 问题

1. 数据存储
Q: 授权信息应该如何在链上存储？
A: 链上提供 Storage，可以直接调用 GET PUT 接口

2. 签发验证
Q: 是否有可用的公私钥对进行签发和验证？ 
A: 有 Storage，可以不用公私钥机制

#### 用到的技术点

  - ontology
  - smart contract
  - ONT ID
  - 链上 Storage

### 7. 接口设计

#### 数据上链

给出 ontid 和版权物，系统记录所有权

输入：

- ~~所有者私钥~~  ontid
- 版权物哈希

输出：

- 结果：成功与否

写入链：
copyright_owner_hash  --> ontid

异常：

- 哈希值重复，拒绝签发


#### 查询是否被授权
输入：

- 版权hash
- 使用者 ontid

输出：
- 成功与否

#### 版权授权

约束：

- 只有版权拥有者才可以调用

输入：

- 版权hash
- 被授权ontid
- 所有权ontid
- 到期时间

输出：

- true, false

写入链：
copyright_grants_hash  --> [[被授权ontid, expiredtime],... ]

#### 版权转移

约束：

- 只有版权拥有者才可以调用

输入：

- 版权hash
- 被转移ontid
- 所有权ontid

输出：

- true, false

写入链：
key_owner_hash  --> ontid[写入新被转移人的ontid]


#### 购买版权

输入：

- 版权hash
- 购买者ontid

输出：

- true, false

写入链：
key_qulified_hash  --> [[购买者ontid, expiredtime],... ]


#### ~~版权取消~~

取消原因：这个接口是需要双方授权的，需要确认如何调用

约束：
- 只有版权拥有者才可以调用

输入：

- 版权hash
- 协商被取消的ontid

输出：

- true, false

写入链：
copyright_grants_hash  --> [[删除掉协商取消的ontid],... ]

### 8. Presentation

[slide](https://docs.google.com/presentation/d/1ZM7N84HiS3qsapCFAm_uwCYW5QNOqBzktO9VCuHf4rA)

---
[^foot1]: [What is Gas?](https://kb.myetherwallet.com/gas/what-is-gas-ethereum.html)
