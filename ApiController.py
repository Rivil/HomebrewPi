from flask import  Flask, jsonify, request

import ApiControllers.ApiCSettings
import ApiControllers.ApiCStatus
import ApiControllers.ApiCRecipes
import ApiControllers.ApiCSteps
import ApiControllers.ApiCBrew
import ApiControllers.ApiCHistory

app = Flask(__name__)

#region "Settings"
@app.route('/homebrew/api/v1.0/settings/<string:settingName>', methods=['GET'])
def getSetting(settingName):
    return ApiControllers.ApiCSettings.getSetting(settingName)

@app.route("/homebrew/api/v1.0/settings", methods=['GET'])
def getSettings():
    return ApiControllers.ApiCSettings.getSettings()

@app.route("/homebrew/api/v1.0/settings", methods=['POST'])
def setSettings():
    return ApiControllers.ApiCSettings.setSetting(request.json.get('SettingName', ""), request.json.get('SettingValue', ""))

@app.route("/homebrew/api/v1.0/setting/<string:settingName>", methods=['DELETE'])
def deleteSetting(settingName):
    return ApiControllers.ApiCSettings.deleteSetting(settingName)
#endregion

#region "Recipes"
@app.route("/homebrew/api/v1.0/recipes", methods=['POST'])
def addRecipe():
    return ApiControllers.ApiCRecipes.AddReciepe(request.json.get('RecipeName', ""))

@app.route("/homebrew/api/v1.0/recipes/<int:recipeId>", methods=['DELETE'])
def deleteRecipe(recipeId):
    return ApiControllers.ApiCRecipes.DeleteRecipe(recipeId)

@app.route("/homebrew/api/v1.0/recipes/<int:recipeId>", methods=['PUT'])
def updateRecipe(recipeId):
    return ApiControllers.ApiCRecipes.UpdateRecipe(recipeId, request.json.get('RecipeName', ""))

@app.route("/homebrew/api/v1.0/recipes", methods=['GET'])
def getRecipes():
    return ApiControllers.ApiCRecipes.GetRecipes()

@app.route("/homebrew/api/v1.0/recipe/<int:recipeId>", methods=['GET'])
def getRecipe(recipeId):
    return ApiControllers.ApiCRecipes.GetRecipe(recipeId)
#endregion

#region "Steps"
@app.route("/homebrew/api/v1.0/steps", methods=['POST'])
def addStep():
    return ApiControllers.ApiCSteps.AddStep(request.json.get('RecipeId', ""), request.json.get('StepName', ""), request.json.get('TempSet', ""), request.json.get('TimeSet', ""), request.json.get('IsOnTimer', ""), request.json.get('PumpOn', ""), request.json.get('HeaterOn', ""))

@app.route("/homebrew/api/v1.0/steps/<int:stepId>", methods=['DELETE'])
def deleteStep(stepId):
    return ApiControllers.ApiCSteps.DeleteStep(stepId)

@app.route("/homebrew/api/v1.0/steps/<int:stepId>", methods=['PUT'])
def updateStep(stepId):
    return ApiControllers.ApiCSteps.UpdateStep(stepId, request.json.get('StepName', ""), request.json.get('TempSet', ""), request.json.get('TimeSet', ""), request.json.get('IsOnTimer', ""), request.json.get('PumpOn', ""), request.json.get('HeaterOn', ""))

@app.route("/homebrew/api/v1.0/steps/<int:recipeId>", methods=['GET'])
def getSteps(recipeId):
    return ApiControllers.ApiCSteps.GetSteps(recipeId)

@app.route("/homebrew/api/v1.0/step/<int:stepId>", methods=['GET'])
def getStep(stepId):
    return ApiControllers.ApiCSteps.GetStep(stepId)
#endregion

#region "Brew"
@app.route("/homebrew/api/v1.0/brew/<int:recipeId>", methods=['GET'])
def setBrew(recipeId):
    return ApiControllers.ApiCBrew.SetBrew(recipeId)

@app.route("/homebrew/api/v1.0/brew/nextStep")
def nextStep():
    return ApiControllers.ApiCBrew.NextStep()

@app.route("/homebrew/api/v1.0/brew/clear")
def clearCurrentBrew():
    return ApiControllers.ApiCBrew.ClearCurrentBrew()

@app.route("/homebrew/api/v1.0/brew")
def getCurrentBrew():
    return ApiControllers.ApiCBrew.GetCurrentBrew()
#endregion

#region "History"
@app.route("/homebrew/api/v1.0/history", methods=['GET'])
def getHistories():
    return ApiControllers.ApiCHistory.GetHistories()

@app.route("/homebrew/api/v1.0/history/<int:historyId>", methods=['GET'])
def getHistory(historyId):
    return ApiControllers.ApiCHistory.GetHistory(historyId)

@app.route("/homebrew/api/v1.0/logs/<int:historyId>", methods=['GET'])
def getLogs(historyId):
    return ApiControllers.ApiCHistory.GetLogs(historyId)
#endregion

#region "Current Status"
@app.route('/homebrew/api/v1.0/currentStatus', methods=['GET'])
def getCurrentStatus():
    return ApiControllers.ApiCStatus.getStatus()

@app.route('/homebrew/api/v1.0/forcePumpOff/<string:isOff>', methods=['GET'])
def forcePumpOff(isOff):
    return ApiControllers.ApiCStatus.ForcePumpOff(isOff)

@app.route('/homebrew/api/v1.0/forceHeaterOff/<string:isOff>', methods=['GET'])
def forceHeaterOff(isOff):
    return ApiControllers.ApiCStatus.ForceHeaterOff(isOff)
#endregion



if __name__ == '__main__':
    app.run(debug=True)