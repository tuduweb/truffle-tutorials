## 2-2-truffle创建项目

（注：unbox下载项目受到访问Github的连通性决定，需要测试）





https://learnblockchain.cn/docs/truffle/quickstart.html

### 相关知识

#### 创建项目

Truffle 大多数命令都是在 Truffle 项目目录下运行的。 所以第一步是创建一个 Truffle 项目。 可以创建一个空项目模板，不过对于刚接触Truffle的同学，推荐使用Truffle Boxes，它提供了示例应用代码和项目模板。 我们将使用MetaCoin box作为案例，它创建一个可以在帐户之间转移的Token（代币）。

为新建的项目创建新目录：

```shell
mkdir MetaCoin
cd MetaCoin
```

通过`unbox`下载`MetaCoin`项目：

```shell
truffle unbox metacoin
```

（注：unbox下载项目受到访问Github的连通性决定，需要测试）



为新建的项目创建新目录：

```shell
mkdir project
cd project
```

创建没有合约的空工程：

```shell
truffle init
```

在操作完成后，目录下有以下的项目结构：

* `contracts/`Solidity合约目录
* `migrations/`部署脚本文件
* `test/`测试脚本目录
* `truffle-config.js`Truffle工程配置文件