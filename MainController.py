import DBModel
import datetime
import time
import Classes.CurrentBrew
import Classes.Step
import Classes.CurrentStatus
import Classes.Setting
db = DBModel.DBModel()

def main():
    #Main Loop
    while True:
        currentBrew = Classes.CurrentBrew.CurrentBrew(db.GetCurrentBrew())
        if currentBrew.HasBrew:
            currentStep = Classes.Step.Step(db.GetStep(currentBrew.StepId))
            currentStatus = Classes.CurrentStatus.CurrentStatus(db.GetCurrentStatus())
        
        time.sleep(1)

def getTemp():
    pass

def switchPump():
    pass

def switchHeater():
    pass


if __name__ == '__main__':
    main()