import os

### params
result = False

### configs
contractName = "NameContract"
contractVarName = "contract1"


# end config


### codes
checkCodeStatus1 = [False]*2
print(checkCodeStatus1)
with open('./migrations/2_contract_name.js', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    for line in lines:
        line.replace(" ", "").replace("\t","").strip()
        print(line, len(line))
        
        if "artifacts.require" in line and contractName in line and contractVarName in line:
            print("ok")
            checkCodeStatus1[0] = True
        
        if checkCodeStatus1[0] and "deployer.deploy("+contractVarName+")" in line:
            print("ok2")
            checkCodeStatus1[1] = True
            break
        
    f.close()

    if checkCodeStatus1[-1]:
        result = True

if result == True:
    exit(0)

print("check code fail:", checkCodeStatus1)
exit(1)