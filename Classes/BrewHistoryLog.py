import datetime

class BrewHistoryLog:
    BrewHistoryId = 0
    DateTime = datetime.datetime.now()
    StepId = 0
    TempRead = 0
    PumpOn = False
    HeaterOn = False
    def __init__(self, row):
        if row is not None:
            BrewHistoryId = row[0]
            DateTime = datetime.datetime.fromtimestamp(row[1])
            StepId = row[2]
            TempRead = row[3]
            PumpOn = bool(row[4])
            HeaterOn = bool(row[5])