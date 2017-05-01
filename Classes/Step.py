class Step:
    Id = 0
    RecipeId = 0
    StepName = ""
    TempSet = 0
    TimeSet = 0
    IsOnTimer = 0
    PumpOn = 0
    HeaterOn = 0
    IsDeleted = 0
    def __init__(self, row):
        if row is not None:
            Id = row[0]
            RecipeId = row[1]
            StepName = row[2]
            TempSet = row[3]
            TimeSet = row[4]
            IsOnTimer = row[5]
            PumpOn = row[6]
            HeaterOn = row[7]
            IsDeleted = row[8]