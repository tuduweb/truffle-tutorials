/***** 引入合约开始 *****/
const contract = artifacts.require("SimpleContract");
/***** 引入合约结束 *****/

module.exports = function(deployer) {
    /***** 部署合约程序开始 *****/
    deployer.deploy(contract);
    /***** 部署合约程序结束 *****/
};