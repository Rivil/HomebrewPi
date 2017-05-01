from flask import  jsonify
import DBModel
db = DBModel.DBModel()

def getStatus():
    row = db.GetCurrentStatus()
    returnValue = {
        'CurrentTemp': row[0],
        'IsPumpOn': bool(row[1]),
        'IsHeaterOn': bool(row[2])
        }
    return jsonify({'CurrentStatus': returnValue})