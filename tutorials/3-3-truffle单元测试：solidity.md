## 3-3-truffle单元测试：solidity





### 相关知识

Solidity测试合约作为`.sol`文件与JavaScript测试一起存在于`./test`目录下。运行`truffle test`时，它们将被不同的测试套件分离测试。

这些合约保留了在JavaScript测试时的所有优点：

* 每个测试套件的“干净”环境
* 直接访问我们部署的合约
* 导入任何合约依赖项

除这些特定之外，Truffle的Solidity测试框架在构建时，还考虑了以下的问题：

* Solidity测试不应该从任何合约拓展（如：测试合约）。这使我们的测试尽可能的少，并且我们可以完全控制我们编写的合约的。
* Solidity测试不应该受制于任何断言库。Truffle为我们提供了一个默认的断言库，但我们可以随时更改此库以满足我们的要求。
* 我们能够在任何以太坊客户端运行我们的Solidity测试。

#### 测试结构

##### 断言

Solidity的断言功能，像`Assert.equal()`由`truffle/Assert.sol`库提供。这是默认的断言库，但是我们也可以包含自己的断言库，只要该库通过触发正确的断言事件，并与Truffle的测试运行器松散地继承。我们可以在`Assert.sol`中，找到所有可以使用的断言函数。

##### 部署地址

我们已经部署的合约（例如作为迁移的一部分的部署合约）的地址可以通过`truffle/DeployedAddresses.sol`库获得。这是由Truffle提供的，它在每个套件运行之前重新编译和重新链接，以便为我们的测试提供Truffle的“干净”环境。该库以以下形式为所有的已部署合约提供功能：

```solidity
DeployedAddresses.<contract name>();
```

这将会返回一个地址，我们可以通过这个地址访问合约。



continue：

http://trufflesuite.com/docs/truffle/testing/writing-tests-in-solidity.html