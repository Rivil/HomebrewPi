from flask import  jsonify
import DBModel
import Classes.CurrentStatus
db = DBModel.DBModel()

def GetCurrentStatus():
    s = Classes.CurrentStatus.CurrentStatus(db.GetCurrentStatus())
    returnValue = {
        'CurrentTemp': s.CurrentTemp,
        'IsPumpOn': s.IsPumpOn,
        'IsHeaterOn': s.IsHeaterOn,
        'ForcePumpOff': s.ForcePumpOff,
        'ForceHeaterOff': s.ForceHeaterOff, 
        'PWMSetting': s.PWMSetting
        }
    return jsonify(returnValue)

def ForcePumpOff(isOff):
    db.ForcePumpOff(isOff)
    return jsonify({'result': 'OK'}),200

def ForceHeaterOff(isOff):
    db.ForceHeaterOff(isOff)
    return jsonify({'result': 'OK'}),200