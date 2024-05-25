from flask import request, jsonify, render_template, url_for
from app import app 
from .models import fetch_all_tools, fetch_tools_by_code, insert_tools, delete_tools, update_tools, get_all_users, fetch_users_by_id

import random

# from transbank.error.transbank_error import TransbankError
# from transbank.webpay.webpay_plus.transaction import Transaction
# from flask_mysqldb import MySQL

# conexion = MySQL(app)

@app.route('/users', methods=['GET'])
def get_users():
    users = get_all_users()
    return jsonify(users)

@app.route('/users', methods=['GET'])
def get_users_by_id():
    users = fetch_users_by_id()
    return jsonify(users)

@app.route('/tools', methods=['GET'])
def get_tools():
    tools = fetch_all_tools()
    return jsonify(tools)


@app.route('/tools/<code>', methods=['GET'])
def get_tool(code):
    tool = fetch_tools_by_code(code)
    return jsonify(tool)


@app.route('/tool', methods=['POST'])
def create_tools():
    tools_data = request.get_json()
    insert_tools(tools_data)
    return jsonify({'message': 'Herramienta creada exitosamente'}), 200


@app.route('/tools/<id>', methods=['DELETE'])
def delete_tool_route(id):
    try:
        eliminada = delete_tools(id)

        if eliminada:
            return jsonify({'message': 'Herramienta eliminada correctamente'}), 200
        else:
            return jsonify({'message': 'Herramienta no encontrada'}), 404
    except Exception:
        return jsonify({'Error': 'Error del servidor'}), 500
    

@app.route('/tools/<id>', methods=['PUT'])
def update_tool_route(id):
    try:
        tools_data = request.json
        update = update_tools(id, tools_data)

        if update:
            return jsonify({'message': 'Herramienta actualizada correctamente'}), 200
        else:
            return jsonify({'message': 'Herramienta no encontrada'}), 404
    except Exception:
        return jsonify({'Error': 'Error del servidor'}), 500
    

@app.route('/Cliente')
def cliente():
    return render_template('Cliente.html')

@app.route('/Carrito')
def carrito():
    return render_template('carrito.html')

@app.route('/Inicio')
def inicio():
    return render_template('inicio.html')

@app.route('/Login')
def login():
    return render_template('login.html')

@app.route('/Equipos_medicion')
def equipos_medicion():
    return render_template('equipos-medicion.html')

@app.route('/Equipos_seguridad')
def equipos_seguridad():
    return render_template('equipos-seguridad.html')

@app.route('/Fijaciones_adhesivos')
def fijaciones_adhesivos():
    return render_template('fijaciones-adhesivos.html')

@app.route('/Herramientas_manuales')
def herramientas_manuales():
    return render_template('herramientas-manuales.html')

@app.route('/Materiales_basicos')
def materiales_basicos():
    return render_template('materiales-basicos.html')

@app.route('/Tornillos_anclajes')
def tornillos_anclajes():
    return render_template('tornillos-anclajes.html')


    


# @app.route("create", methods=["GET"])
# def webpay_plus_create():
#     print("Webpay Plus Transaction.create")
#     buy_order = str(random.randrange(1000000, 99999999))
#     session_id = str(random.randrange(1000000, 99999999))
#     amount = random.randrange(10000, 1000000)
#     return_url = request.url_root + 'webpay-plus/commit'

#     create_request = {
#         "buy_order": buy_order,
#         "session_id": session_id,
#         "amount": amount,
#         "return_url": return_url
#     }

#     response = (Transaction()).create(buy_order, session_id, amount, return_url)

#     print(response)

#     return render_template('webpay/plus/create.html', request=create_request, response=response)


# @app.route("commit", methods=["GET"])
# def webpay_plus_commit():
#     token = request.args.get("token_ws")
#     print("commit for token_ws: {}".format(token))

#     response = (Transaction()).commit(token=token)
#     print("response: {}".format(response))

#     return render_template('webpay/plus/commit.html', token=token, response=response)

# @app.route("commit", methods=["POST"])
# def webpay_plus_commit_error():
#     token = request.form.get("token_ws")
#     print("commit error for token_ws: {}".format(token))

#     #response = Transaction.commit(token=token)
#     #print("response: {}".format(response))
#     response = {
#         "error": "Transacción con errores"
#     }

#     return render_template('webpay/plus/commit.html', token=token, response=response)    


# @app.route("refund", methods=["POST"])
# def webpay_plus_refund():
#     token = request.form.get("token_ws")
#     amount = request.form.get("amount")
#     print("refund for token_ws: {} by amount: {}".format(token, amount))

#     try:
#         response = (Transaction()).refund(token, amount)
#         print("response: {}".format(response))

#         return render_template("webpay/plus/refund.html", token=token, amount=amount, response=response)
#     except TransbankError as e:
#         print(e.message)


# @app.route("refund-form", methods=["GET"])
# def webpay_plus_refund_form():
#     return render_template("webpay/plus/refund-form.html")


# @app.route('status-form', methods=['GET'])
# def show_create():
#     return render_template('webpay/plus/status-form.html')


# @app.route('status', methods=['POST'])
# def status():
#     token_ws = request.form.get('token_ws')
#     tx = Transaction()
#     resp = tx.status(token_ws)
#     return render_template('tbk_status.html', response=resp, token=token_ws, req=request.form)

def error_page(error):
    return "PÁGINA NO ENCONTRADA..."
app.register_error_handler(404, error_page)


