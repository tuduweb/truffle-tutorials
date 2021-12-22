## 3-2-truffle单元测试





### 相关知识

#### 单元测试

##### 概述

在计算机编程中，单元测试（英语：Unit Testing）又称为模块测试，是针对程序模块（软件设计的最小单位）来进行正确性检验的测试工作。程序单元是应用的最小可测试部件。在过程化编程中，一个单元就是单个程序、函数、过程等；对于面向对象编程，最小单元就是方法，包括基类（超类）、抽象类、或者派生类（子类）中的方法。

通常来说，程序设计师每修改一次程序就会进行最少一次单元测试，在编写程序的过程中前后很可能要进行多次单元测试，以证实程序达到软件规格书要求的工作目标，称有程序错误；虽然单元测试不是必须的，但这可以给我们的程序提升一定的健壮性。

每个理想的测试案例独立于其它案例；为测试时隔离模块，经常使用stubs、mock或fake等测试马甲程序。单元测试通常由软件开发人员编写，用于确保他们所写的代码符合软件需求和遵循开发目标。它的实施方式可以是非常手动的，或者是做成构建自动化的一部分。

##### 收益

单元测试的目标是隔离程序部件并证明这些单个部件是正确的。一个单元测试提供了代码片断需要满足的严密的书面规约。

因此，单元测试带来了一些益处。 单元测试可以在软件开发过程的早期发现设计问题。

单元测试WIKI：https://zh.wikipedia.org/wiki/%E5%8D%95%E5%85%83%E6%B5%8B%E8%AF%95

#### Truffle单元测试

##### 测试框架

Truffle中标配自动化测试框架，让测试合约变得十分轻松。这个框架允许我们以两种不同的方式，编写简单且可管理的测试：

1. 在Javascript和TypeScript中：允许我们从外部方式执行我们的合约，就像我们的应用程序一样。
2. 在Solidity中，允许我们在更高一级的层面，裸机场景中执行我们的合约。

这两种风格的测试方式都有其优点和缺点。我们将在后续章节中对其进行介绍。

##### 测试用例目录

在Truffle中，所有的单元测试文件应该被放置在工程的`./test`目录下。Truffle将只会执行以下文件拓展的测试文件：`.js`，`.ts`，`.es`，`.es6`，`.jsx`和`.sol`。其它后缀的文件将被忽略。

##### 测试合约命令

运行目录下所有的测试，你只需要执行：

```bash
$ truffle test
```

或者，你也可以指定要执行指定的测试文件，例如：

```bash
$ truffle test ./path/to/test/file.js
```

这时候，就执行了`./path/to/test/file.js`相对路径下的测试文件。

##### “干净的”测试环境

Truffle在运行测试文件的时候，提供了一个干净的环境。在针对在`Ganache`或者`Truffle Develop`环境下运行测试时，Truffle将使用高级快照功能，确保测试文件不会相互共享状态。当在`go-ethereum`等其它以太坊客户端运行时，Truffle将在每个测试文件开始时重新部署我们的所有迁移，以确保我们又一组新的合约进行测试。

##### 速度和可靠性探究

使用`Gananche`和`Truffle Develop`在运行自动化测试时比其它客户端要快得多。此外，它们包含特殊特性，Truffle利用这些特性将测试运行时间加快近90%。作为一般的工作流程，官方推荐在正常开发和测试阶段使用`Gananche`和`Truffle Develop`，然后在准备部署到实时或生产网络时针对`go-ethereum`或其它官方以太坊客户端时，运行一次测试。

##### 堆栈跟踪

我们可以使用`truffle test --stacktrace`选项，获取失败交易的Solidity堆栈跟踪（情况）。如果在测试阶段恢复并导致测试失败，这将在测试期间，生成在Truffle合约下部署和进行交易的堆栈跟踪信息。

> This will produce stack traces for transactions and deployments made via Truffle Contract during your tests should one of them revert and thereby causes your test to fail. 

这个选项仍处在试验阶段（2021-12-21），当前不支持调用`call`和`gas`估算的堆栈跟踪，此外，当这个选项打开时，Truffle合约的`PromiEvent`功能可能无法工作。

还有`truffle test --stacktrace-extra`选项。这个选项将打开堆栈跟踪，并将在Solidity的调试模式下额外编译合约以获取额外的恢复消息。这种模式仅在Solidity0.6.3中引入，因此它对早期版本的Solidity没有影响。使用调试模式可能会导致较大的合约出现问题。

#### 用JavaScript编写测试

Truffle使用Mocha测试框架，和使用Chai断言工具进行断言。为我们提供了一个可靠的框架来编写JavaScript测试。接下来，让我们深入了解一下Truffle是如何构建在Mocha之上的，让测试合约变得轻松。

##### 使用`contract()`代替`describe()`

在结构上，我们的测试应该与Mocha中的测试基本保持不变：测试文件应存在于`./test`目录下，它们应该以`.js`拓展名结尾，并且它们应该包含Mocha中将识别为自动化测试的代码，即符合Mocha的测试句法规范。

两者不同的是，在Truffle中使用`contract()`函数，该函数与Mocha测试中的`describe()`完全相同，只是它启用了Truffle的“干净”测试环境功能。它的工作方式如下简述：

* 在运行每个`contract()`函数之前，我们的合约将重新部署到正在运行的以太坊客户端上，以便这个测试以干净的合约状态运行。
* `contract()`函数提供了一个由我们的以太坊客户端提供的账户列表，我们可以用它来编写测试。

由于Truffle测试在底层使用了Mocha，我们仍可以使用`describe()`来运行正常的Mocha测试，只是在这种情况下Truffle的“干净”环境功能将不被应用。

##### 在测试中使用合约抽象

合约抽象是通过JavaScript实现合约交互的基础。由于在Truffle中，无法检测我们在测试中需要和哪些合约进行交互，因此我们要明确需要测哪些合约。我们可以通过使用`artifacts.require()`方法来完成此操作，这个方法由Truffle提供，允许我们为特定的Solidity合约请求可用的合约抽象。正如在下面的例子中所见，我们可以使用此合约抽象来确保我们的合约正常工作。

##### 使用`artifacts.require()`

在你的测试中使用`artifacts.require()`的方式和在迁移中使用它的方式相同，我们只需要传递合约的名称。

##### 使用web3

在每一个测试文件中，`web3`实例都是可用的，配置到了合适的`provider`上。

我们只需要调用`web3.eth.getBalance`使用即可。

#### 例子

##### 使用`.then`方法

我们以MetaCoin Truffle Box中提供的测试示例举例，注意`contract()`函数的使用，其用于指定可用以太坊账户的`account`数组，以及我们使用`artifacts.require()`直接与我们的合约交互。

示例文件：`./test/metacoin.js`

```javascript
const MetaCoin = artifacts.require("MetaCoin");

contract("MetaCoin", accounts => {
  it("should put 10000 MetaCoin in the first account", () =>
    MetaCoin.deployed()
      .then(instance => instance.getBalance.call(accounts[0]))
      .then(balance => {
        assert.equal(
          balance.valueOf(),
          10000,
          "10000 wasn't in the first account"
        );
      }));

  it("should call a function that depends on a linked library", () => {
    let meta;
    let metaCoinBalance;
    let metaCoinEthBalance;

    return MetaCoin.deployed()
      .then(instance => {
        meta = instance;
        return meta.getBalance.call(accounts[0]);
      })
      .then(outCoinBalance => {
        metaCoinBalance = outCoinBalance.toNumber();
        return meta.getBalanceInEth.call(accounts[0]);
      })
      .then(outCoinBalanceEth => {
        metaCoinEthBalance = outCoinBalanceEth.toNumber();
      })
      .then(() => {
        assert.equal(
          metaCoinEthBalance,
          2 * metaCoinBalance,
          "Library function returned unexpected function, linkage may be broken"
        );
      });
  });

  it("should send coin correctly", () => {
    let meta;

    // Get initial balances of first and second account.
    const account_one = accounts[0];
    const account_two = accounts[1];

    let account_one_starting_balance;
    let account_two_starting_balance;
    let account_one_ending_balance;
    let account_two_ending_balance;

    const amount = 10;

    return MetaCoin.deployed()
      .then(instance => {
        meta = instance;
        return meta.getBalance.call(account_one);
      })
      .then(balance => {
        account_one_starting_balance = balance.toNumber();
        return meta.getBalance.call(account_two);
      })
      .then(balance => {
        account_two_starting_balance = balance.toNumber();
        return meta.sendCoin(account_two, amount, { from: account_one });
      })
      .then(() => meta.getBalance.call(account_one))
      .then(balance => {
        account_one_ending_balance = balance.toNumber();
        return meta.getBalance.call(account_two);
      })
      .then(balance => {
        account_two_ending_balance = balance.toNumber();

        assert.equal(
          account_one_ending_balance,
          account_one_starting_balance - amount,
          "Amount wasn't correctly taken from the sender"
        );
        assert.equal(
          account_two_ending_balance,
          account_two_starting_balance + amount,
          "Amount wasn't correctly sent to the receiver"
        );
      });
  });
});
```

运行这个测试，将会产生如下输出：

```
  Contract: MetaCoin
    ✓ should put 10000 MetaCoin in the first account (85ms)
    ✓ should call a function that depends on a linked library (145ms)
    ✓ should send coin correctly (352ms)


  8 passing (8s)
```

##### 使用`async`/`await`

不同于使用`.then`方法，你也可以使用`async`/`await`语法。示例如下：

```javascript
const MetaCoin = artifacts.require("MetaCoin");

contract("2nd MetaCoin test", async accounts => {
  it("should put 10000 MetaCoin in the first account", async () => {
    const instance = await MetaCoin.deployed();
    const balance = await instance.getBalance.call(accounts[0]);
    assert.equal(balance.valueOf(), 10000);
  });

  it("should call a function that depends on a linked library", async () => {
    const meta = await MetaCoin.deployed();
    const outCoinBalance = await meta.getBalance.call(accounts[0]);
    const metaCoinBalance = outCoinBalance.toNumber();
    const outCoinBalanceEth = await meta.getBalanceInEth.call(accounts[0]);
    const metaCoinEthBalance = outCoinBalanceEth.toNumber();
    assert.equal(metaCoinEthBalance, 2 * metaCoinBalance);
  });

  it("should send coin correctly", async () => {
    // Get initial balances of first and second account.
    const account_one = accounts[0];
    const account_two = accounts[1];

    const amount = 10;

    const instance = await MetaCoin.deployed();
    const meta = instance;

    const balance = await meta.getBalance.call(account_one);
    const account_one_starting_balance = balance.toNumber();

    balance = await meta.getBalance.call(account_two);
    const account_two_starting_balance = balance.toNumber();
    await meta.sendCoin(account_two, amount, { from: account_one });

    balance = await meta.getBalance.call(account_one);
    const account_one_ending_balance = balance.toNumber();

    balance = await meta.getBalance.call(account_two);
    const account_two_ending_balance = balance.toNumber();

    assert.equal(
      account_one_ending_balance,
      account_one_starting_balance - amount,
      "Amount wasn't correctly taken from the sender"
    );
    assert.equal(
      account_two_ending_balance,
      account_two_starting_balance + amount,
      "Amount wasn't correctly sent to the receiver"
    );
  });
});
```

这个测试和使用`.then`方法功能相同，只是实现方式不同，故输出类似。

#### 指定测试

你可以指定特定文件运行测试，如下所示：

```bash
truffle test ./test/metacoin.js
```

#### 