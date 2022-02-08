const contract1 = artifacts.require("NameContract");

module.exports = function (deployer) {
  deployer.deploy(contract1);
};
