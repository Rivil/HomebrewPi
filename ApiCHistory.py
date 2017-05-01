from flask import jsonify
import datetime
import DBModel
db = DBModel.DBModel()

def GetHistories():
    rows = db.GetHistories()
    returnValue = []
    for row in rows:
        jsonRow = {}
        jsonRow['History']={
            'Id': row[0],
            'RecipeId': row[1],
            'Date': datetime.datetime.fromtimestamp(row[2])
            }
        returnValue.append(jsonRow)
    return jsonify(returnValue)
    

def GetHistory(historyId):
    row = db.GetHistory(historyId)
    returnValue = {
        'Id': row[0],
        'RecipeId': row[1],
        'Date': datetime.datetime.fromtimestamp(row[2])
        }
    return jsonify(returnValue)

def GetLogs(historyId):
    rows = db.GetLogs(historyId)
    returnValue = []
    for row in rows:
        jsonRow = {}
        jsonRow['Log']={
            'BrewHistoryId': row[0],
            'DateTime': datetime.datetime.fromtimestamp(row[1]),
            'StepId': row[2],
            'TempRead': row[3],
            'PumpOn': bool(row[4]),
            'HeaterOn': bool(row[5])
            }
        returnValue.append(jsonRow)
    return jsonify(returnValue)