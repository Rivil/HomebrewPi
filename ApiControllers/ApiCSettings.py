from flask import jsonify
import Classes.Setting
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
        s = Classes.Setting.Setting(row)
        jsonRow = {}
        jsonRow['Setting']={
            'Id': s.Id,
            'SettingName': s.SettingName,
            'Value': s.Value
            }
        returnValue.append(jsonRow)
    return jsonify(returnValue)

def setSetting(settingName, settingValue):
    db.SetSetting(settingName,settingValue)
    return jsonify({'result': 'OK'}),200

def deleteSetting(settingName):
    db.DeleteSetting(settingName)
    return jsonify({'result': 'OK'}),200
