"""
Author - GopalaSutharsan
First Commit - 07/09/2021
Latest Change - 18/10/2021

Starts the opcua server in local ip endpoint
New node is created in the server
A new variable is created with name space and identifiers
Each variable will be simulating a random value and will set value to the variable
"""
import json
import random
from random import randint


def read_config():
    filePath = './config.json'
    with open(filePath) as f:
        json_string = json.load(f)
        f.close()
    return json_string

def mainfunction(cyclestart_status,downntimereasoncode,downtimestatus, emgstopstatus, idealcycletime,jobid,machineid, operatorid, poweronstatus, productionstart, qualitycode,shiftid):
    try:
        config = read_config()
        cyclestart_status_var = config["CycleStart"]
        downntimereasoncode_var = config["DownTimeReasonCode"]
        downtimestatus_var = config["DownTimeStatus"]
        emgstopstatus_var = config["EmergencyStop"]
        idealcycletime_var = config["IdealCycleTime"]
        jobid_var = config["JobID"]
        machineid_var = config["MachineID"]
        operatorid_var = config["OperatorID"]
        poweronstatus_var = config["PowerOnStatus"]
        productionstart_var = config["ProductionStart"]
        qualitycode_var = config["QualityCode"]
        shiftid_var = config["ShiftID"]

        cyclestart_status.set_value(cyclestart_status_var)
        downntimereasoncode.set_value(downntimereasoncode_var)
        downtimestatus.set_value(downtimestatus_var)
        emgstopstatus.set_value(emgstopstatus_var)
        idealcycletime.set_value(idealcycletime_var)
        jobid.set_value(jobid_var)
        machineid.set_value(machineid_var)
        operatorid.set_value(operatorid_var)
        poweronstatus.set_value(poweronstatus_var)
        productionstart.set_value(productionstart_var)
        qualitycode.set_value(qualitycode_var)
        shiftid.set_value(shiftid_var)

        print("CycleStart: {},\nDownTime Reason Code: {},\nDownTime Status: {},\nEmergency Stop: {}, \nIdeal Cycle Time: {}, \nJob ID :{}, \nMachine ID:{}, \nOperator ID:{}, \nPowerOn Status: {}, \nProduction Start: {}, \nQuality Code: {}, \nShift ID: {} \n".format(cyclestart_status_var, downntimereasoncode_var, downtimestatus_var, emgstopstatus_var, idealcycletime_var,
              jobid_var, machineid_var, operatorid_var, poweronstatus_var, productionstart_var, qualitycode_var,shiftid_var))
        
    except Exception as ex:
        print("Error", ex)
