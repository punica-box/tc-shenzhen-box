# Ontofraud

Hackathon related files: 
- wallet.txt contains Ontology-wallet
- TCSZ-2018(1).key - contains presentation 
- URL: https://ontofraud.herokuapp.com
- Admin URL: https://ontofraud.herokuapp.com/admin/
- Admin Credentials: admin / qr1af2zv3

# Introduction
The Ontofraud team (Emil Balashov, Ruslan Dautov and Vlad Sergeev) has built the web-service to check and prevent fraudulent transactions based on Ontology blockchain technology. The web service provides the tool to make the transactions as Trusted, OK, New, Suspicious and Fraudulent. Although, the main functionality is deep search algorithm which analyzes a graph of transactions based on Pandas and Networkx. 

# Getting started
Run project:

In order to run project you should go through this steps:

- init python virtual environment
- install needed packages `pip install -r requirements.txt`
- install PostgreSQL and create a DB `onto`, it should be avialble by URL: `postgres://localhost:5432/onto'`
- run `./manage.py migrate`
- run `./manage.py collectstatic`

- Then run the server `./manage.py runserver`
