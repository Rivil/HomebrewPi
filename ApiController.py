from flask import  Flask, jsonify, request

import ApiCSettings
import ApiCStatus
import ApiCRecipes
import ApiCSteps
import ApiCBrew
import ApiCHistory

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

@app.route("/homebrew/api/v1.0/setting/<string:settingName>", methods=['DELETE'])
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

@app.route("/homebrew/api/v1.0/recipe/<int:recipeId>", methods=['GET'])
def getRecipe(recipeId):
    return ApiCRecipes.GetRecipe(recipeId)
#endregion

#region "Steps"
@app.route("/homebrew/api/v1.0/steps", methods=['POST'])
def addStep():
    return ApiCSteps.AddStep(request.json.get('RecipeId', ""), request.json.get('StepName', ""), request.json.get('TempSet', ""), request.json.get('TimeSet', ""), request.json.get('IsOnTimer', ""), request.json.get('PumpOn', ""), request.json.get('HeaterOn', ""))

@app.route("/homebrew/api/v1.0/steps/<int:stepId>", methods=['DELETE'])
def deleteStep(stepId):
    return ApiCSteps.DeleteStep(stepId)

@app.route("/homebrew/api/v1.0/steps/<int:stepId>", methods=['PUT'])
def updateStep(stepId):
    return ApiCSteps.UpdateStep(stepId, request.json.get('StepName', ""), request.json.get('TempSet', ""), request.json.get('TimeSet', ""), request.json.get('IsOnTimer', ""), request.json.get('PumpOn', ""), request.json.get('HeaterOn', ""))

@app.route("/homebrew/api/v1.0/steps/<int:recipeId>", methods=['GET'])
def getSteps(recipeId):
    return ApiCSteps.GetSteps(recipeId)

@app.route("/homebrew/api/v1.0/step/<int:stepId>", methods=['GET'])
def getStep(stepId):
    return ApiCSteps.GetStep(stepId)
#endregion

#region "Brew"
@app.route("/homebrew/api/v1.0/brew/<int:recipeId>", methods=['GET'])
def setBrew(recipeId):
    return ApiCBrew.SetBrew(recipeId)

@app.route("/homebrew/api/v1.0/brew/nextStep")
def nextStep():
    return ApiCBrew.NextStep()

@app.route("/homebrew/api/v1.0/brew/clear")
def clearCurrentBrew():
    return ApiCBrew.ClearCurrentBrew()

@app.route("/homebrew/api/v1.0/brew")
def getCurrentBrew():
    return ApiCBrew.GetCurrentBrew()
#endregion

#region "History"
@app.route("/homebrew/api/v1.0/history", methods=['GET'])
def getHistories():
    return ApiCHistory.GetHistories()

@app.route("/homebrew/api/v1.0/history/<int:historyId>", methods=['GET'])
def getHistory(historyId):
    return ApiCHistory.GetHistory(historyId)

@app.route("/homebrew/api/v1.0/logs/<int:historyId>", methods=['GET'])
def getLogs(historyId):
    return ApiCHistory.GetLogs(historyId)
#endregion

#region "Current Status"
@app.route('/homebrew/api/v1.0/currentStatus', methods=['GET'])
def getCurrentStatus():
    return ApiCStatus.getStatus()

@app.route('/homebrew/api/v1.0/forcePumpOff/<bool:isOff>', methods=['GET'])
def forcePumpOff(isOff):
    return ApiCStatus.ForcePumpOff(isOff)

@app.route('/homebrew/api/v1.0/forceHeaterOff/<bool:isOff>', methods=['GET'])
def forceHeaterOff(isOff):
    return ApiCStatus.ForceHeaterOff(isOff)
#endregion



if __name__ == '__main__':
    app.run(debug=True)