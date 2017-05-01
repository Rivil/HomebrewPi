from flask import jsonify
import datetime
import DBModel
db = DBModel.DBModel()

def AddReciepe(recipeName):
    return jsonify({"RecipeId": db.AddReciepe(recipeName)}), 200

def DeleteRecipe(recipeId):
    db.DeleteRecipe(recipeId)
    return jsonify({'result': 'OK'}),200

def UpdateRecipe(recipeId, name):
    db.UpdateRecipe(recipeId, name)
    return jsonify({'result': 'OK'}),200

def GetRecipes():
    rows = db.GetRecipes()
    returnValue = []
    for row in rows:
        jsonRow = {}
        jsonRow['Recipe']={
            'Id': row[0],
            'DateCreated': datetime.datetime.fromtimestamp(row[1]),
            'Name': row[2],
            'IsDeleted': row[3]
            }
        returnValue.append(jsonRow)
    return jsonify(returnValue)

def GetRecipe(recipeId):
    row = db.GetRecipe(recipeId)
    returnValue = {
        'Id': row[0],
        'DateCreated': datetime.datetime.fromtimestamp(row[1]),
        'Name': row[2],
        'IsDeleted': row[3]
        }
    return jsonify(returnValue)