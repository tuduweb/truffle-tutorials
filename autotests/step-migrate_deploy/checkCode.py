import os

### params
result = False

### init param
_currentFilePath = os.path.split(os.path.realpath(__file__))[0]
_fileToHomeworkPath = '../../homework/'

### configs
contractName = "SimpleContract"
# contractVarName = "contract1"
### end config

### codes
checkCodeStatus1 = [False]*2

with open('./3_deploy_contracts.js', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    for line in lines:
        line = line.replace(" ", "").replace("\t","").strip()
       
        if "artifacts.require" in line and contractName in line:
            print(line, "ok")
            checkCodeStatus1[0] = True
        
        if checkCodeStatus1[0] and "deployer.deploy" in line:
            print(line, "ok2")
            checkCodeStatus1[1] = True
            break
        
    f.close()

    if checkCodeStatus1[-1]:
        result = True

if result == True:
    exit(0)

print("check code fail:", checkCodeStatus1)
exit(1)