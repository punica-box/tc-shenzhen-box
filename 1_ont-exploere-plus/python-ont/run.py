from eve import Eve
from OntTest import OntTest
import json

app = Eve()

@app.route("/x")
def hello():
    return "Hello World!"


@app.route("/ont")
def world():
    ontt = OntTest()
    return str(ontt.print_balance())


@app.route('/oep4token/<string:address>')
def query_oep4_token_transfer(address):
    ontt = OntTest()
    return  json.dumps(ontt.query_oep4_token_transfer(address))



@app.route('/oep4token/list')
def list_oep4_token():
    ontt = OntTest()
    return  json.dumps(ontt.list_oep4_token())

@app.route('/oep4token/detail/<string:address>')
def query_oep4_detail(address):
    ontt = OntTest()
    return  json.dumps(ontt.query_oep4_detail(address))


if __name__ == '__main__':
    app.run(debug=True)