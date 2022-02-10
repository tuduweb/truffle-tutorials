### 步骤：`truffle debug`功能的运用

检查用户对`truffle debug`的运用情况。

#### 思路方法

1. 查验日志

#### 记录

日志内容

```
debug(development:0x5898e273...)>

MetaCoin.sol:

22:                 balances[msg.sender] -= amount;
23:                 balances[receiver] += amount;
24:                 emit Transfer(msg.sender, receiver, amount);
                                              ^^^^^^^^

:amount
  10

:balances
  Map(2) {
   0x60Fb076c0b7e3B4a46a458eE67Ed2C772667e17C => 9990,
   0x895aeACbbCf55beb4eF225Acd9B1289eeBaDFb48 => 10
 }
```