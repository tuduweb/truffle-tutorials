logFile="./migrate.out"
rm $logFile > /dev/null
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