from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbhomework


## HTML 화면 보여주기
@app.route('/')
def homework():
    return render_template('index.html')


# 주문하기(POST) API
@app.route('/order', methods=['POST'])
def save_order():
    name = request.form['name']
    ea = request.form['ea']
    addr = request.form['addr']
    phone = request.form['phone']
    client = MongoClient('localhost', 27017)
    db = client.dbsparta
    cl = db.shopping
    cl.insert({'name': name, 'ea': ea, 'addr': addr, 'phone': phone})
    return jsonify({'result': 'success'})


# 주문 목록보기(Read) API
@app.route('/order', methods=['GET'])
def view_orders():
    # 여길 채워나가세요!
    client = MongoClient('localhost', 27017)
    db = client.dbsparta
    cl = db.shopping
    orders = cl.find({},{'_id': False})
    orders = list(orders)
    return jsonify({'result': 'success', 'orders': orders})


if __name__ == '__main__':
    app.run(debug=True)
