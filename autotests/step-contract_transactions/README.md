### 步骤：检查`transactions`的运用

主要是检查钱包余额，查看待转移账户中的余额。

#### 思路方法

1. 检查文件是否存在
2. 检查特定代码段是否存在：文字匹配方法
3. 执行程序

#### 记录

```bash
truffle console
```

带输出记录的方式：

```bash
tee out.txt | truffle console
```

```bash
migrate

let instance = await MetaCoin.deployed()

instance.address
```