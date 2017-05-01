from flask import jsonify
import Classes.Recipe
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
        rec = Classes.Recipe.Recipe(row)
        jsonRow = {}
        jsonRow['Recipe']={
            'Id': rec.Id,
            'DateCreated': rec.DateCreated,
            'Name': rec.Name,
            'IsDeleted': rec.IsDeleted
            }
        returnValue.append(jsonRow)
    return jsonify(returnValue)

def GetRecipe(recipeId):
    rec = Classes.Recipe.Recipe(db.GetRecipe(recipeId))
    returnValue = {
        'Id': rec.Id,
        'DateCreated': rec.DateCreated,
        'Name': rec.Name,
        'IsDeleted': rec.IsDeleted
        }
    return jsonify(returnValue)