import DBModel
import datetime
import time
import Classes.CurrentBrew
import Classes.Step
import Classes.CurrentStatus
import Classes.Setting
import Max31865Controller
import math
db = DBModel.DBModel()

max = Max31865Controller.max31865(db.GetSetting("csPin"), db.GetSetting("misoPin"), db.GetSetting("mosiPin"), db.GetSetting("clkPin"), db.GetSetting("BoardNumerationType"))
usePWM = db.GetSetting("UsePWM")
lastTemp = 0
setTempReached = False

def main():
    #Main Loop
    while True:
        currentBrew = Classes.CurrentBrew.CurrentBrew(db.GetCurrentBrew())
        if currentBrew.HasBrew:
            getTemp()
            currentStep = Classes.Step.Step(db.GetStep(currentBrew.StepId))
            currentStatus = Classes.CurrentStatus.CurrentStatus(db.GetCurrentStatus())
            
            currentStatus.IsHeaterOn
            currentStep.TempSet
            switchHeater(currentStatus, lastTemp, currentStep)
            

            lastTemp = currentStatus.CurrentTemp
        time.sleep(1)

def getTemp():
    db.UpdateCurrentTemp(max.readTemp)

def switchHeater(currentStatus, lastTemp, currentStep):
    if currentStatus.ForceHeaterOff and currentStatus.IsHeaterOn:
            pass #TURN OFF THE HEATER
            return
    if not currentStep.HeaterOn and currentStatus.IsHeaterOn:
        pass #TURN OFF THE HEATER
        return
    if currentStatus.UsePWM:
        tempDelta = currentStep.TempSet - currentStatus.CurrentTemp
        if tempDelta > 10:
            setTempReached = False
            pass #set PWM 100
        if tempDelta <= 10 and tempDelta > 5:
            pass #set pwm 50
        if tempDelta <=5 and tempDelta > 1:
            pass #set pwm 30    
        if tempDelta <= 1:
            if currentStatus.PWMSetting > 5 and setTempReached == False:
                setTempReached = True
                pass #set pwm 5
            else:
                if math.ceil(currentStatus.CurrentTemp) > math.ceil(lastTemp):
                    pwm = currentStatus.PWMSetting - 1
                    db.UpdatePWMSetting(pwm)
                    pass #set PWM to pwm
                if math.ceil(currentStatus.CurrentTemp) < math.ceil(lastTemp):
                    pwm = currentStatus.PWMSetting + 1
                    db.UpdatePWMSetting(pwm)
                    pass #set PWM to pwm
    else:
        tempDelta = currentStep.TempSet - currentStatus.CurrentTemp
        if tempDelta > 1:
            pass #set Heater On
        else:
            pass #set Heater Off

def switchPump():
    pass


if __name__ == '__main__':
    main()