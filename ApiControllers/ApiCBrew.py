from flask import jsonify
import datetime
import DBModel
import Classes.CurrentBrew
db = DBModel.DBModel()


def SetBrew(recipeId):
    db.SetBrew(recipeId)
    return jsonify({'result': 'OK'}),200

def NextStep():
    db.NextStep()
    return jsonify({'result': 'OK'}),200

def ClearCurrentBrew():
    db.ClearCurrentBrew()
    return jsonify({'result': 'OK'}),200

def GetCurrentBrew():
    brew = Classes.CurrentBrew.CurrentBrew(db.GetCurrentBrew())
    if brew.HasBrew:
        returnValue = {
            'RecipeId': brew.RecipeId,
            'StepId': brew.StepId,
            'StartDate': brew.StartDate,
            'StepStart': brew.StepStart,
            'HistoryId': brew.HistoryId
            }
        return jsonify(returnValue)
    else:
        return jsonify({'result': 'No current brew'}), 404