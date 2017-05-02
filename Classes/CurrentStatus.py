class CurrentStatus:
    CurrentTemp = 0
    IsPumpOn = False
    IsHeaterOn = False
    ForcePumpOff = False
    ForceHeaterOff = False
    PWMSetting = 0
    def __init__(self, row):
        if row is not None:
            CurrentTemp = row[0]
            IsPumpOn = bool(row[1])
            IsHeaterOn = bool(row[2])
            ForcePumpOff = bool(row[3])
            ForceHeaterOff = bool(row[4])
            PWMSetting = bool(row[5])