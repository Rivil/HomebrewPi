import datetime

class BrewHistory:
    Id = 0
    RecipeId = 0
    Date = datetime.datetime.now()
    def __init__(self, row):
        if row is not None:
            Id = row[0]
            RecipeId = row[1]
            Date = datetime.datetime.fromtimestamp(row[2])