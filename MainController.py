import DBModel
import datetime
import time
import Classes.CurrentBrew
import Classes.Step
import Classes.CurrentStatus
import Classes.Setting
import Max31865Controller
import math
import RPi.GPIO as GPIO

db = DBModel.DBModel()

max = Max31865Controller.max31865(db.GetSetting("csPin"), db.GetSetting("misoPin"), db.GetSetting("mosiPin"), db.GetSetting("clkPin"), db.GetSetting("BoardNumerationType"))
usePWM = db.GetSetting("UsePWM")
lastTemp = 0
setTempReached = False

if db.GetSetting("BoardNumerationType") == "BOARD":
    GPIO.setmode(GPIO.BOARD)
else :
    GPIO.setmode(GPIO.BCM)
if usePWM:
    pwmPin = GPIO.PWM(db.GetSetting("HeaterOnPin"),50)
else:
    GPIO.setup(db.GetSetting("HeaterOnPin"), GPIO.OUT)

GPIO.setup(db.GetSetting("PumpOnPin"), GPIO.OUT)

def main():
    #Main Loop
    GPIO.setup(db.GetSetting("FanControlPin"), GPIO.OUT)
    GPIO.output(db.GetSetting("FanControlPin"), GPIO.HIGH)
    if usePWM:
        pwmPin.start(0)
    while True:
        currentBrew = Classes.CurrentBrew.CurrentBrew(db.GetCurrentBrew())
        if currentBrew.HasBrew:
            getTemp()
            currentStep = Classes.Step.Step(db.GetStep(currentBrew.StepId))
            currentStatus = Classes.CurrentStatus.CurrentStatus(db.GetCurrentStatus())
            currentStatus.ForcePumpOff
            currentStep.PumpOn
            switchHeater(currentStatus, lastTemp, currentStep)
            lastTemp = currentStatus.CurrentTemp
        time.sleep(1)
    
    if usePWM:
        pwmPin.stop()
    GPIO.output(db.GetSetting("FanControlPin"), GPIO.LOW)
    GPIO.cleanup()

def getTemp():
    db.UpdateCurrentTemp(max.readTemp)

def switchHeater(currentStatus, lastTemp, currentStep):
    if currentStatus.ForceHeaterOff and currentStatus.IsHeaterOn:
        if usePWM:
            SetPWM(0)
        else:
            SetHeater(False)
        return
    if not currentStep.HeaterOn and currentStatus.IsHeaterOn:
        if usePWM:
            SetPWM(0)
        else:
            SetHeater(False)
        return
    if currentStatus.UsePWM:
        tempDelta = currentStep.TempSet - currentStatus.CurrentTemp
        if tempDelta > 10:
            setTempReached = False
            SetPWM(100)
            return
        if tempDelta <= 10 and tempDelta > 5:
            SetPWM(50)
        if tempDelta <=5 and tempDelta > 1:
            SetPWM(30)
        if tempDelta <= 1:
            if currentStatus.PWMSetting > 5 and setTempReached == False:
                setTempReached = True
                SetPWM(5)
            else:
                if math.ceil(currentStatus.CurrentTemp) > math.ceil(lastTemp):
                    pwm = currentStatus.PWMSetting - 1
                    SetPWM(pwm)
                if math.ceil(currentStatus.CurrentTemp) < math.ceil(lastTemp):
                    pwm = currentStatus.PWMSetting + 1
                    SetPWM(pwm)
    else:
        tempDelta = currentStep.TempSet - currentStatus.CurrentTemp
        if tempDelta > 1:
            SetHeater(True)
        else:
            SetHeater(False)

def switchPump(currentStatus, currentStep):
    if currentStatus.ForcePumpOff and currentStatus.IsPumpOn:
        SetPump(False)
        return
    if not currentStep.PumpOn and currentStatus.IsPumpOn:
        SetPump(False)
        return
    if currentStatus.PumpIn and not currentStatus.IsPumpOn:
        SetPump(True)
        return 

def SetPWM(dutyCycle):
    currentStatus = Classes.CurrentStatus.CurrentStatus(db.GetCurrentStatus())
    if currentStatus.PWMSetting != dutyCycle:
        pwmPin.ChangeDutyCycle(dutyCycle)
        if dutyCycle == 0:
            db.UpdateHeater(False)
        else:
            db.UpdateHeater(True)
        db.UpdatePWMSetting(dutyCycle)

def SetHeater(IsOn):
    heaterPin = db.GetSetting("HeaterOnPin")
    db.UpdateHeater(IsOn)
    if IsOn:
        GPIO.output(heaterPin, GPIO.HIGH)
    else:
        GPIO.output(heaterPin, GPIO.LOW)

def SetPump(IsOn):
    pumpPin = db.GetSetting("PumpOnPin")
    db.UpdatePump(IsOn)
    if IsOn:
        GPIO.output(pumpPin, GPIO.HIGH)
    else:
        GPIO.output(pumpPin, GPIO.LOW)

if __name__ == '__main__':
    main()