from flask import jsonify, request
from db import cnx

class Medicion():
    global cur
    cur = cnx.cursor()

    def list():
        lista = []
        cur.execute("SELECT * FROM mediciones")
        rows = cur.fetchall()
        columns = [i[0] for i in cur.description]
        for row in rows:
            registro = zip(columns, row)
            json = dict(registro)
            lista.append(json)
        return jsonify(lista)
        cnx.close


    def create(body):
        data = (body['fecha'],body['origen'],body['valor'],body['codigoSensor'],body['observacion'], body['imagen'])
        sql = "INSERT INTO mediciones(fecha, origen, valor, codigoSensor, observacion, imagen) VALUES(%s, %s, %s, %s, %s, %s)"
        cur.execute(sql,data)
        cnx.commit()
        return {'estado': "insertado"}, 200