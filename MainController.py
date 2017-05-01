import DBModel

db = DBModel.DBModel()

db.SetSetting("Test", "Test1")
row = db.GetSetting("Test")
print(row)