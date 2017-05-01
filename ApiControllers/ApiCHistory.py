from flask import jsonify
import DBModel
import Classes.BrewHistory
import Classes.BrewHistoryLog
db = DBModel.DBModel()

def GetHistories():
    rows = db.GetHistories()
    returnValue = []
    for row in rows:
        history = Classes.BrewHistory.BrewHistory(row)
        jsonRow = {}
        jsonRow['History']={
            'Id': history.Id,
            'RecipeId': history.RecipeId,
            'Date': history.Date
            }
        returnValue.append(jsonRow)
    return jsonify(returnValue)
    

def GetHistory(historyId):
    history = Classes.BrewHistory.BrewHistory(db.GetHistory(historyId))
    returnValue = {
        'Id': history.Id,
        'RecipeId': history.RecipeId,
        'Date': history.Date
        }
    return jsonify(returnValue)

def GetLogs(historyId):
    rows = db.GetLogs(historyId)
    returnValue = []
    for row in rows:
        log = Classes.BrewHistoryLog.BrewHistoryLog(row)
        jsonRow = {}
        jsonRow['Log']={
            'BrewHistoryId': log.BrewHistoryId,
            'DateTime': log.DateTime,
            'StepId': log.StepId,
            'TempRead': log.TempRead,
            'PumpOn': log.PumpOn,
            'HeaterOn': log.HeaterOn
            }
        returnValue.append(jsonRow)
    return jsonify(returnValue)