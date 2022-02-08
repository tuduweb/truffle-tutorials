const Web3 = require('web3')
const fs = require('fs')
const solc = require('solc')

async function start() {

    let web3 = new Web3(new Web3.providers.HttpProvider("http://127.0.0.1:8545"))
    // let rootAccountAddr = "0x"
    // let abi = ""
    // let contractAddress = "0x"
    
    // let NoteContract = new web3.eth.Contract(abi, contractAddress)
    
    let accounts = await web3.eth.getAccounts()
    console.log(accounts)

    const supperAccount = accounts[0]
 
    console.log(supperAccount)

    // directly load contract object from .json files, 从已有部署的合约中捣鼓数据..
    let sourceJson = fs.readFileSync('./build/contracts/MetaCoin.json', 'utf-8')
    let contract = JSON.parse(sourceJson)

    console.log(contract.abi)

    let contractAddress = '0x79E0D5F41485Bc70d3a6ed9925e6608A02EAFf55'
    let nameContract = new web3.eth.Contract(contract.abi, contractAddress)

    // await instance.getBalance(accounts[0])
    // check your MetaCoin
    console.log(await nameContract.methods.getBalance(accounts[1]).call())// calling a method

    // let sourceCode = fs.readFileSync('./contracts/NameContract.sol')
    // console.log(sourceCode.toString())

    // //编译合约
    // let compiledCode = solc.compile(sourceCode.toString())
    // //获取合约abi
    // let abiDefinition = JSON.parse(compiledCode.contracts[':NameContract'].interface)
    // //获取合约字节码
    // let byteCode = '0x' + compiledCode.contracts['NameContract'].bytecode

    // //new一个合约对象
    // var nameContract = new web3.eth.Contract(abiDefinition)

    // console.log(byteCode)


    //const output = solc.compile(sourceCode.toString(), 1)

    // var bytecode;
    // var abi;
    // for (var contractName in output.contracts) {
    //     // code and ABI that are needed by web3
    //     bytecode = output.contracts[contractName].bytecode
    //     abi = JSON.parse(output.contracts[contractName].interface)
    //     //console.log(contractName + ': ' + output.contracts[contractName].bytecode)
    //     //console.log(contractName + '; json.parse:' + JSON.parse(output.contracts[contractName].interface))
    //     //console.log('json.stringify:' + JSON.stringify(abi, undefined, 2));
    //     //可以把abi打印出来，看看智能合约的编译和本来的是不是相同
    // }

    //console.log(output.contracts)


    
}

start()