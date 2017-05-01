from flask import  jsonify
import DBModel
db = DBModel.DBModel()

def GetCurrentStatus():
    row = db.GetCurrentStatus()
    returnValue = {
        'CurrentTemp': row[0],
        'IsPumpOn': row[1],
        'IsHeaterOn': row[2],
        'ForcePumpOff': row[3],
        'ForceHeaterOff': row[4]
        }
    return jsonify(returnValue)

def ForcePumpOff(isOff):
    db.ForcePumpOff(isOff)
    return jsonify({'result': 'OK'}),200

def ForceHeaterOff(isOff):
    db.ForceHeaterOff(isOff)
    return jsonify({'result': 'OK'}),200