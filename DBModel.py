import sqlite3
import time

class DBModel(object):

    def __init__(self):
        self.DBName = "Homebrew.db"
        conn = sqlite3.connect(self.DBName)
        c = conn.cursor()
        c.execute("CREATE TABLE if not exists 'Recipes' ('Id' INTEGER PRIMARY KEY AUTOINCREMENT, 'DateCreated' INTEGER, 'Name' TEXT, 'IsDeleted' INTEGER)")
        c.execute("CREATE TABLE if not exists 'RecipeSteps' ('Id' INTEGER PRIMARY KEY AUTOINCREMENT, 'RecipeId' INTEGER, 'StepName' TEXT, 'TempSet' REAL, 'TimeSet' INTEGER, 'IsOnTimer' INTEGER, 'PumpOn' INTEGER, 'HeaterOn' INTEGER, 'IsDeleted' INTEGER)")
        c.execute("CREATE TABLE if not exists 'Settings' ('Id' INTEGER PRIMARY KEY AUTOINCREMENT, 'SettingName' TEXT, 'Value' TEXT)")
        c.execute("CREATE TABLE if not exists 'CurrentBrew' ('RecipeId' INTEGER, 'StepId' INTEGER, 'StartDate' INTEGER, 'StepStart' INTEGER, 'HistoryId' INTEGER)")
        c.execute("CREATE TABLE if not exists 'BrewHistory' ('Id' INTEGER PRIMARY KEY AUTOINCREMENT, 'RecipeId' INTEGER, 'Date' INTEGER)")
        c.execute("CREATE TABLE if not exists 'BrewHistoryLog' ('BrewHistoryId' INTEGER, 'DateTime' INTEGER, 'StepId' INTEGER, 'TempRead' REAL, 'PumpOn' INTEGER, 'HeaterOn' INTEGER)")
        c.execute("CREATE TABLE if not exists 'CurrentStatus' ('CurrentTemp' REAL, 'IsPumpOn' INTEGER, 'IsHeaterOn' INTEGER, 'ForcePumpOff' INTEGER, 'ForceHeaterOff' INTEGER)")
        c.execute("SELECT Count(*) FROM CurrentStatus")
        row = c.fetchone()
        if row[0] == 0:
            c.execute("INSERT INTO CurrentStatus (CurrentTemp, IsPumpOn, IsHeaterOn, ForcePumpOff, ForceHeaterOff) VALUES (0,0,0,0,0)")
        conn.commit()
        conn.close()

    def GetSettings(self):
        conn = sqlite3.connect(self.DBName)
        c = conn.cursor()
        c.execute("SELECT * FROM 'Settings'")
        rows = c.fetchall()
        conn.close()
        return rows

    def GetSetting(self, settingName):
        conn = sqlite3.connect(self.DBName)
        c = conn.cursor()
        t = (settingName,)
        c.execute("SELECT Value FROM 'Settings' WHERE SettingName = ?", t)
        row = c.fetchone()
        conn.close()
        return row[0]

    def SetSetting(self, settingName, settingValue):
        conn = sqlite3.connect(self.DBName)
        c = conn.cursor()
        setting = (settingName, )
        c.execute("SELECT EXISTS(SELECT 1 FROM 'Settings' WHERE SettingName = ?)", setting)
        row = c.fetchone()
        if row[0]:
            setting = (settingValue, settingName)
            c.execute("UPDATE 'Settings' SET Value = ? WHERE SettingName = ?", setting)
        else:
            setting = (settingName, settingValue)
            c.execute("INSERT INTO 'Settings' (SettingName, Value) VALUES (?, ?)", setting)
        conn.commit()
        conn.close()

    def DeleteSetting(self, settingName):
        conn = sqlite3.connect(self.DBName)
        c = conn.cursor()
        setting = (settingName,)
        c.execute("DELETE FROM 'Settings' WHERE SettingName = ?", setting)
        conn.commit()
        conn.close()

    def AddReciepe(self, recipeName):
        conn = sqlite3.connect(self.DBName)
        c = conn.cursor()
        name = (recipeName, int(time.time()))
        c.execute("INSERT INTO 'Recipes' (Name, IsDeleted, DateCreated) VALUES (?, 0, ?)", name)
        conn.commit()
        c.execute("SELECT last_insert_rowid()")
        row = c.fetchone()
        conn.close()
        return row[0]

    def DeleteRecipe(self, recipe):
        conn = sqlite3.connect(self.DBName)
        c = conn.cursor()
        recipeId = (recipe, )
        c.execute("UPDATE 'Recipes' SET IsDeleted = 1 WHERE Id = ?", recipeId)
        conn.commit()
        conn.close()

    def UpdateRecipe(self, recipeId, name):
        conn = sqlite3.connect(self.DBName)
        c = conn.cursor()
        recipeUpdate = (name, recipeId)
        c.execute("UPDATE Recipes SET Name = ? WHERE Id = ?", recipeUpdate)
        conn.commit()
        conn.close()

    def GetRecipes(self):
        conn = sqlite3.connect(self.DBName)
        c = conn.cursor()
        c.execute("SELECT * FROM 'Recipes'")
        rows = c.fetchall()
        conn.close()
        return rows

    def GetRecipe(self, recipeId):
        conn = sqlite3.connect(self.DBName)
        c = conn.cursor()
        recipe = (recipeId,)
        c.execute("SELECT * FROM Recipes WHERE Id = ?", recipe)
        row = c.fetchone()
        conn.close()
        return row
    
    def AddStep(self, recipeId, name, tempSet, timeSet, isOnTimer, pumpOn, heaterOn):
        conn = sqlite3.connect(self.DBName)
        c = conn.cursor()
        step = (recipeId, name, tempSet, timeSet, isOnTimer, pumpOn, heaterOn)
        c.execute("INSERT INTO 'RecipeSteps' (RecipeId, StepName, TempSet, TimeSet, IsOnTimer, PumpOn, HeaterOn, IsDeleted) VALUES (?,?,?,?,?,?,?,0)", step)
        conn.commit()
        c.execute("SELECT last_insert_rowid()")
        row = c.fetchone()
        conn.close()
        return row[0]

    def DeleteStep(self, stepId):
        conn = sqlite3.connect(self.DBName)
        c = conn.cursor()
        step = (stepId,)
        c.execute("UPDATE 'RecipeSteps' SET IsDeleted = 1 WHERE Id = ?", step)
        conn.commit()
        conn.close()

    def UpdateStep(self, stepId, name, tempSet, timeSet, isOnTimer, pumpOn, heaterOn):
        conn = sqlite3.connect(self.DBName)
        c = conn.cursor()
        step = (name, tempSet, timeSet, isOnTimer, pumpOn, heaterOn, stepId)
        c.execute("UPDATE 'RecipeSteps' SET StepName = ?, TempSet = ?, TimeSet = ?, IsOnTimer = ?, PumpOn = ?, HeaterOn = ? WHERE Id = ?", step)
        conn.commit()
        conn.close()

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
        
    def SetBrew(self, recipeId):
        conn = sqlite3.connect(self.DBName)
        c = conn.cursor()
        c.execute("DELETE FROM CurrentBrew")
        conn.commit()
        recipe = (recipeId, )
        c.execute("SELECT Id FROM 'RecipeSteps' WHERE RecipeId = ? AND IsDeleted = 0 ORDER BY Id ASC", recipe)
        row = c.fetchone()

        history = (recipeId, int(time.time()))
        c.execute("INSERT INTO 'BrewHistory' (RecipeId, Date) VALUES (?, ?)", history)
        conn.commit()
        c.execute("SELECT last_insert_rowid()")
        rowh = c.fetchone()

        recipe = (recipeId,row[0],int(time.time()), int(time.time()), rowh[0])
        c.execute("INSERT INTO 'CurrentBrew' (RecipeId, StepId, StartDate, StepStart, HistoryId) VALUES (?, ?, ?, ?, ?)", recipe)
        conn.commit()
        conn.close()
    
    def NextStep(self):
        conn = sqlite3.connect(self.DBName)
        c = conn.cursor()
        c.execute("SELECT RecipeId, StepId FROM 'CurrentBrew'")
        row = c.fetchone()
        recipe = (row[0], row[1])
        c.execute("SELECT Id FROM 'RecipeSteps' WHERE RecipeId = ? AND Id > ? AND IsDeleted = 0 ORDER BY Id ASC", recipe)
        row = c.fetchone()
        recipe = (row[0], int(time.time()))
        c.execute("UPDATE 'CurrentBrew' SET StepId = ?, StepStart = ?", recipe)
        conn.commit()
        conn.close()

    def ClearCurrentBrew(self):
        conn = sqlite3.connect(self.DBName)
        c = conn.cursor()
        c.execute("DELETE FROM 'CurrentBrew'")
        conn.commit()
        conn.close()

    def GetCurrentBrew(self):
        conn = sqlite3.connect(self.DBName)
        c = conn.cursor()
        c.execute("SELECT * FROM 'CurrentBrew'")
        row = c.fetchone()
        conn.close()
        return row

    def AddHistory(self, recipeId):
        conn = sqlite3.connect(self.DBName)
        c = conn.cursor()
        history = (recipeId, int(time.time()))
        c.execute("INSERT INTO 'BrewHistory' (RecipeId, Date) VALUES (?, ?)", history)
        conn.commit()
        c.execute("SELECT last_insert_rowid()")
        row = c.fetchone()
        conn.close()
        return row[0]

    def AddHistoryLog(self):
        conn = sqlite3.connect(self.DBName)
        c = conn.cursor()
        c.execute("SELECT HistoryId, StepId")
        cBrewRow = c.fetchone()
        c.execute("SELECT CurrentTemp, IsPumpOn, IsHeaterOn FROM CurrentStatus")
        cStatusRow = c.fetchone()
        log = (cBrewRow[0], int(time.time()), cBrewRow[1], cStatusRow[0], cStatusRow[1], cStatusRow[2])
        c.execute("INSERT INTO 'BrewHistoryLog' (BrewHistoryId, DateTime, StepId, TempRead, PumpOn, HeaterOn) VALUES (?, ?, ?, ?, ?, ?)")
        conn.commit()
        conn.close()
        
    def GetHistories(self):
        conn = sqlite3.connect(self.DBName)
        c = conn.cursor()
        c.execute("SELECT * FROM 'BrewHistory'")
        rows = c.fetchall()
        conn.close()
        return rows

    def GetHistory(self, historyId):
        conn = sqlite3.connect(self.DBName)
        c = conn.cursor()
        history = (historyId, )
        c.execute("SELECT * FROM 'BrewHistory' WHERE Id = ?", history)
        row = c.fetchone()
        conn.close()
        return row

    def GetLogs(self, historyId):
        conn = sqlite3.connect(self.DBName)
        c = conn.cursor()
        log = (historyId, )
        c.execute("SELECT * FROM 'BrewHistoryLog' WHERE BrewHistoryId = ?", log)
        rows = c.fetchall()
        conn.close()
        return row
        
    def GetCurrentStatus(self):
        conn = sqlite3.connect(self.DBName)
        c = conn.cursor()
        c.execute("SELECT * FROM CurrentStatus")
        row = c.fetchone()
        conn.close()
        return row

    def UpdateCurrentTemp(self, temp):
        conn = sqlite3.connect(self.DBName)
        c = conn.cursor()
        t = (temp,)
        c.execute("UPDATE CurrentStatus SET CurrentTemp = ?", t)
        conn.commit()
        conn.close()

    def UpdatePump(self, pumpOn):
        conn = sqlite3.connect(self.DBName)
        c = conn.cursor()
        t = (pumpOn,)
        c.execute("UPDATE CurrentStatus SET IsPumpOn = ?", t)
        conn.commit()
        conn.close()
    def UpdateHeater(self, heaterOn):
        conn = sqlite3.connect(self.DBName)
        c = conn.cursor()
        t = (heaterOn,)
        c.execute("UPDATE CurrentStatus SET IsHeaterOn = ?", t)
        conn.commit()
        conn.close()

    def ForcePumpOff(self, isOff):
        conn = sqlite3.connect(self.DBName)
        c = conn.cursor()
        off = (isOff, )
        c.execute("UPDATE CurrentStatus SET ForcePumpOff = ?", off)
        conn.commit()
        conn.close()

    def ForceHeaterOff(self, isOff):
        conn = sqlite3.connect(self.DBName)
        c = conn.cursor()
        off = (isOff, )
        c.execute("UPDATE CurrentStatus SET ForceHeaterOff = ?", off)
        conn.commit()
        conn.close()
