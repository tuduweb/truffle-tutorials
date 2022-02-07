import os

checkDir = '../truffle-test1/build'
## check build files
checkFiles = {
    "contracts" : ['Migrations.json']
}

if not os.path.isdir(checkDir + ''):
    print(checkDir + ' is not exist! exit')
    exit(-1)

items = os.listdir(checkDir + '')
print(items)

print("*"*10)

res = True

for d in checkFiles:
    if res == False: break
    #if d == "./": continue

    _path = os.path.join(checkDir, d)
    print(d, " isDir = ", os.path.exists(_path))
    if os.path.exists(_path) == False: res = False ; continue
    hasFiles = os.listdir(_path)
    needFiles = checkFiles[d]
    print(hasFiles)
    print(needFiles)

    _sub = set(needFiles) - set(hasFiles)
    # if checkFile not exist, _sub include it
    res = res and (len(_sub) == 0)

print(res)

if not res:
    exit(-1)

exit(0)

# 在bash中使用 echo $? 输出返回值