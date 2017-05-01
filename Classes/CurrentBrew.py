import datetime

class CurrentBrew:
    HasBrew = False
    RecipeId = 0
    StepId = 0
    StartDate = datetime.datetime.now()
    StepStart = datetime.datetime.now()
    HistoryId = 0
    def __init__(self, row):
        if row is not None:
            RecipeId = row[0]
            StepId = row[1]
            StartDate = datetime.datetime.fromtimestamp(row[2])
            StepStart = datetime.datetime.fromtimestamp(row[3])
            HistoryId = row[4]
            HasBrew = True
        else:
            HasBrew = False