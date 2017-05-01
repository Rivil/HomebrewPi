from flask import  Flask, jsonify, request

import ApiCSettings
import ApiCStatus
import ApiCRecipes

app = Flask(__name__)

#region "Settings"
@app.route('/homebrew/api/v1.0/settings/<string:settingName>', methods=['GET'])
def getSetting(settingName):
    return ApiCSettings.getSetting(settingName)

@app.route("/homebrew/api/v1.0/settings", methods=['GET'])
def getSettings():
    return ApiCSettings.getSettings()

@app.route("/homebrew/api/v1.0/settings", methods=['POST'])
def setSettings():
    return ApiCSettings.setSetting(request.json.get('SettingName', ""), request.json.get('SettingValue', ""))

@app.route("/homebrew/api/v1.0/settings/<string:settingName>", methods=['DELETE'])
def deleteSetting(settingName):
    return ApiCSettings.deleteSetting(settingName)
#endregion

#region "Recipes"
@app.route("/homebrew/api/v1.0/recipes", methods=['POST'])
def addRecipe():
    return ApiCRecipes.AddReciepe(request.json.get('RecipeName', ""))

@app.route("/homebrew/api/v1.0/recipes/<int:recipeId>", methods=['DELETE'])
def deleteRecipe(recipeId):
    return ApiCRecipes.DeleteRecipe(recipeId)

@app.route("/homebrew/api/v1.0/recipes/<int:recipeId>", methods=['PUT'])
def updateRecipe(recipeId):
    return ApiCRecipes.UpdateRecipe(recipeId, request.json.get('RecipeName', ""))

@app.route("/homebrew/api/v1.0/recipes", methods=['GET'])
def getRecipes():
    return ApiCRecipes.GetRecipes()

@app.route("/homebrew/api/v1.0/recipes/<int:recipeId>", methods=['GET'])
def getRecipe(recipeId):
    return ApiCRecipes.GetRecipe(recipeId)
#endregion




@app.route('/homebrew/api/v1.0/currentStatus', methods=['GET'])
def getCurrentStatus():
    return ApiCStatus.getStatus()




if __name__ == '__main__':
    app.run(debug=True)