from flask import jsonify
import datetime
import DBModel
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
    row = db.GetCurrentBrew()
    if row is not None:
        returnValue = {
            'RecipeId': row[0],
            'StepId': row[1],
            'StartDate': datetime.datetime.fromtimestamp(row[2]),
            'StepStart': datetime.datetime.fromtimestamp(row[3]),
            'HistoryId': row[4]
            }
        return jsonify(returnValue)
    else:
        return jsonify({'result': 'No current brew'}), 404