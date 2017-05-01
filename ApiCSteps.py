from flask import jsonify
import datetime
import DBModel
db = DBModel.DBModel()

def AddStep(recipeId, name, tempSet, timeSet, isOnTimer, pumpOn, heaterOn):
    return jsonify({"StepId": db.AddStep(recipeId,name,tempSet,timeSet,isOnTimer,pumpOn,heaterOn)})
    
def DeleteStep(stepId):
    db.DeleteStep(stepId)
    return jsonify({'result': 'OK'}),200
    
def UpdateStep(stepId, name, tempSet, timeSet, isOnTimer, pumpOn, heaterOn):
    db.UpdateStep(stepId, name, tempSet,timeSet,isOnTimer,pumpOn,heaterOn)
    return jsonify({'result': 'OK'}),200
    
def GetSteps(recipeId):
    rows = db.GetSteps(recipeId)
    returnValue = []
    for row in rows:
        jsonRow = {}
        jsonRow['Step']={
            'Id': row[0],
            'RecipeId': row[1],
            'StepName': row[2],
            'TempSet': row[3],
            'TimeSet': row[4],
            'IsOnTimer': bool(row[5]),
            'PumpOn': bool(row[6]),
            'HeaterOn': bool(row[7]),
            'IsDeleted': bool(row[8])
            }
        returnValue.append(jsonRow)
    return jsonify(returnValue)
    
def GetStep(stepId):
    row = db.GetStep(stepId)
    returnValue = {
        'Id': row[0],
        'RecipeId': row[1],
        'StepName': row[2],
        'TempSet': row[3],
        'TimeSet': row[4],
        'IsOnTimer': bool(row[5]),
        'PumpOn': bool(row[6]),
        'HeaterOn': bool(row[7]),
        'IsDeleted': bool(row[8])
        }
    return jsonify(returnValue)