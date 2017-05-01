from flask import jsonify
import Classes.Step
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
        s = Classes.Step.Step(row)
        jsonRow = {}
        jsonRow['Step']={
            'Id': s.Id,
            'RecipeId': s.RecipeId,
            'StepName': s.StepName,
            'TempSet': s.TempSet,
            'TimeSet': s.TimeSet,
            'IsOnTimer': s.IsOnTimer,
            'PumpOn': s.PumpOn,
            'HeaterOn': s.HeaterOn,
            'IsDeleted': s.IsDeleted
            }
        returnValue.append(jsonRow)
    return jsonify(returnValue)
    
def GetStep(stepId):
    s = Classes.Step.Step(db.GetStep(stepId))
    returnValue = {
        'Id': s.Id,
        'RecipeId': s.RecipeId,
        'StepName': s.StepName,
        'TempSet': s.TempSet,
        'TimeSet': s.TimeSet,
        'IsOnTimer': s.IsOnTimer,
        'PumpOn': s.PumpOn,
        'HeaterOn': s.HeaterOn,
        'IsDeleted': s.IsDeleted
        }
    return jsonify(returnValue)