import os
import re

### params
result = False

### configs
contractName = "NameContract"
contractVarName = "contract1"

pathToLogFile = '../../demo/debug.out'


# end config


### codes
checkCodeStatus1 = [False]*2
print(checkCodeStatus1)

# check file exist

def PickData(line):
    datas = re.findall(r"(0x.+?)=>.+33m([0-9]+)", line)
    print(datas)

with open(pathToLogFile, 'r', encoding='utf-8') as f:
    lines = f.readlines()
    
    for idx, line in enumerate(lines):

        if "Map(1)" in line:
            print(lines[idx + 1])
            # PickData(lines[idx + 1])
            # print(lines[idx + 1][8:-24])
            # print(lines[idx + 1][60:-6])
            
            data = re.sub('\x1b.*?m', '', lines[idx + 1])
            datas = re.findall(r"(0x.+?) => ([0-9]+)", data)
            print(datas[0])


        if "Map(2)" in line:
            print(lines[idx + 1])
            print(lines[idx + 2])
            PickData(lines[idx + 1])
            PickData(lines[idx + 2])


    #print(lines)
    f.close()