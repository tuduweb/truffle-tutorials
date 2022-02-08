# must run in root directory

# must reset the ganache status or change the contract name

logFile="./migrate.out"
rm $logFile > /dev/null


python3 ./checkFiles.py > $logFile
if [ $? != 0 ] ; then
    cat $logFile
    exit
fi

python3 ./checkCode.py > $logFile
if [ $? != 0 ] ; then
    cat $logFile
    exit
fi

truffle migrate > $logFile
isOk=$?
echo $isOk
if [ $isOk == 0 ] ; then
    echo "success"
else
    # exec python grap errors
    ##echo $isOk
    cat $logFile
fi