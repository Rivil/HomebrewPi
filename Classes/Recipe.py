import datetime

class Recipe:
    Id = 0
    DateCreated = datetime.datetime.now()
    Name = ""
    IsDeleted = False
    def __init__(self, row):
        if row is not None:
            Id = row[0]
            DateCreated = datetime.datetime.fromtimestamp(row[1])
            Name = row[2]
            IsDeleted = bool(row[3])