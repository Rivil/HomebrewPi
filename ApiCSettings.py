from flask import jsonify
import DBModel
db = DBModel.DBModel()

def getSetting(settingName):
    row = db.GetSetting(settingName)
    returnValue = {
        'SettingName': settingName,
        'Value': row
        }
    return jsonify(returnValue)

def getSettings():
    rows = db.GetSettings()
    returnValue = []
    for row in rows:
        jsonRow = {}
        jsonRow['Setting']={
            'Id': str(row[0]),
            'SettingName': row[1],
            'Value': row[2]
            }
        returnValue.append(jsonRow)
    return jsonify(returnValue)

def setSetting(settingName, settingValue):
    db.SetSetting(settingName,settingValue)
    return jsonify({'result': 'OK'}),200

def deleteSetting(settingName):
    db.DeleteSetting(settingName)
    return jsonify({'result': 'OK'}),200
