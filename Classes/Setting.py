class Setting:
    Id = 0
    SettingName = ""
    Value = ""
    def __init__(self, row):
        if row is not None:
            Id = row[0]
            SettingName = row[1]
            Value = rpw[2]