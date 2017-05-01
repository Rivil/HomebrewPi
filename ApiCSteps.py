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
    
def GetSteps(self, recipeId):
    conn = sqlite3.connect(self.DBName)
    c = conn.cursor()
    step = (recipeId,)
    c.execute("SELECT * FROM 'RecipeSteps' WHERE RecipeId = ?", step)
    rows = c.fetchall()
    conn.close()
    return rows

def GetStep(self, stepId):
    conn = sqlite3.connect(self.DBName)
    c = conn.cursor()
    step = (stepId, )
    c.execute("SELECT * FROM 'RecipeSteps' WHERE Id = ?", step)
    row = c.fetchone()
    conn.close()
    return row