## 3-1-truffle调试合约的方法









### 相关知识

#### 概述

Truffle 集成了一个调试器，以便我们可以调试合约进行的交易。 此调试器类似于传统开发环境中使用的命令行调试程序。

调试区块链上的交易与调试传统应用程序（例如，用C++或Javascript编写的应用程序）不同。 在区块链上调试交易时，没有实时运行代码; 相反，我们将逐步执行该交易的历史执行，并将该执行映射到其关联的代码上。 这为调试提供了许多自由，因此我们可以随时调试任何交易，只要我们拥有交易与之交互的合约的代码和工件(artifacts)即可。 可以将这些代码和工件（artifacts）类似于传统调试器所需的调试符号。

要调试交易，需要以下几个条件：

- Truffle 4.0 及以上；
- 所要调试区块链上的交易哈希值；
- 交易对应的合约源代码和工件(artifacts)。

注意：只要存在于链上交易，我们都可以调试它， 即使交易发生异常或者gas耗尽，也没关系。

警告：针对在启用优化的情况下编译的合约，在调试交易时可能无法可靠地工作。

#### 在测试中调试

Truffle v5.1及更高版本，提供了`truffle test --debug`，和相关的`debug()`全局函数，允许我们中断测试以调试特定的操作。

无需像下面描述的需要捕获交易哈希`transaction hash`，我们只需要使用`debug()`包裹需要调试的任何合约操作，比如：

```javascript
it("should succeed", async function() {
  // wrap what you want to debug with `debug()`:
  await debug( myContract.myFunction(accounts[1], { from: accounts[0] }) );
  //           ^^^^^^^^^^^^^^^^^^ wrap contract operation ^^^^^^^^^^^^^^
});
```

接着，执行`truffle test --debug`，truffle将会编译我们的源码，并正常的运行我们的测试，直到执行到相关的操作（即`debug()`包裹的部分）。此时，truffle将中断正常的测试流程并启动调试器，并允许我们进行设置断点、检查Solidity变量等操作。

#### 调试只读`call`

从Javascript内部运行调试器，允许的外的功能，超出了`truffle debug <txHash>`提供的功能。

除了可以调试交易`transactions`外，在测试中调试还允许我们调试只读调用(`read-only call`)。

```javascript
it("should get latest result", async function() {
  // wrap what you want to debug with `debug()`:
  const result = await debug( myContract.getResult("latest") );
  //                          ^^^^^ read-only function ^^^^^
});
```

#### 相关命令(`Command`)

要使用调试器以收集交易信息，你需要执行以下操作：

```bash
$ truffle debug <transaction hash>
```

比如需要使用一个开始于 `0x8e5dadfb921dd...` 的交易，你需要执行以下操作：

```bash
$ truffle debug 0x8e5dadfb921ddddfa8f53af1f9bd8beeac6838d52d7e0c2fe5085b42a4f3ca76
```

这将会启动下面描述的调试界面。



如果你只是想启动调试器，使调试器准备就绪，以便后续调试交易，你也可以简单的运行：

```bash
$ truffle debug
```

无论你通过什么方式启动调试器，一旦调试器运行，你就不仅限于只能调试你启动时的交易，你可以通过下面描述的方法，卸载当前交易，并加载新的交易。



你可以通过使用`--network`选项，指定你想要调试的网络，如下所示：

```bash
$ truffle debug [<transaction hash>] --network <network>
```

如果你想要调试你的solidity测试合约，你可以使用`--compile-test`选项，如下所示：

```bash
$ truffle debug [<transaction hash>] --compile-tests
```

#### 调试器界面

<img src="/Users/bin/Library/Application Support/typora-user-images/截屏2021-12-21 下午12.08.08.png" alt="截屏2021-12-21 下午12.08.08" style="zoom:50%;" />

启动调试器后，打开的交互界面和其他类型应用程序调试器差不多。 在它启动时，将看到以下内容：

- 在此交易过程中处理或创建的地址列表。
- 调试器所支持的调试命令列表。
- 以及交易的初始入口点，包括合约源文件和代码预览。

`enter` 回车键设置为执行最后输入的命令。 当调试器启动时，在执行期间 `enter` 键被设置为步进到源代码的下一个逻辑元素（即，由以太坊虚拟机确定的下一个表达式或语句）。 此时，我们可以按 `enter` 单步执行交易，或者输入一个可用命令来更详细地分析交易。 下面是命令列表详述。

##### (o) 跳过（step over）

此命令跳过当前行（即当前在Solidity源文件中语句或表达式的位置）， 如果我们不想在当前行上进入函数调用或合约创建，或者我们想快速跳转到源文件中的特定点，请使用此命令。

##### (i) 进入（step into）

此命令进入当前所在的函数调用或合约创建。 使用此命令跳转到该函数内，并快速开始调试其中存在的代码。

##### (u) 跳出（step out）

此命令退出当前运行的函数。 如果这是交易的入口点，使用此命令会快速返回到调用函数，或结束交易的执行。

##### (n) 下一步（step next）

此命令将执行源代码中的下一个逻辑语句或表达式。 例如，在虚拟机可以评估完整表达式之前，需要首先评估子表达式。 如果要分析虚拟机评估的每个逻辑项，请使用此命令。

##### (;) 单步指令（step instruction）

此命令允许我们逐步执行虚拟机评估的每个单独指令。 如果要了解 Solidity 源代码创建的低级字节码，这个命令非常有用。 使用此命令时，调试器还将在评估指令时打印出堆栈数据。（如果使用`p`指令打开了额外的数据显示，那么这些数据也将会显示出来。）

你可以将此命令与数字参数一起使用，以达到多次步进的效果。

##### (p) 打印指令（print instruction）

此命令打印当前指令和堆栈数据，但不会跳到下一条指令。 当我们使用上面调试命令导航到一个交易语句时，希望查看当前指令和堆栈数据时，就可以使用此命令。

如果想要查看内存、存储或调用数据时，此命令还可以打印堆栈意外的位置。

只需要键入`p memory`以显示内存和其他信息；键入`p storage`以显示存储信息；`p calldata`显示函数参数`calldata`。

这些指令也可以缩写，例如内存：`p mem`。它们也可以组合使用，比如，显示内存存储：`p mem sto`。

你也可以`+`将这些额外的位置添加到默认显示中：比如，`p +mem`将会在你输出`p`或者`;`时始终显示内存，而使用`p -mem`将关闭此功能。你也可以使用`p -sta`关闭存储显示，或者使用`p sta`强制显示。这些选项也可以像前段提到的那样组合使用。

这些指令也可以打印一组围绕当前指令的指令。默认情况下，它会额外打印当前指令之前的三条指令，和当前指令后面的三条指令。你可以使用`+`和`-`来配置需要打印的指令数量，例如，使用`p +<instructions-ahead> -<instruction-back>`将会打印前`instructions-ahead`条指令和后`instructions-back`条指令。这些配置的数量将会保存以用于后续的打印输出。

##### (l)打印额外的上下文源码 print additional source context

此指令可以打印当前源代码行的上下文。默认情况下，它将会打印当前源码行前的5行和后3行。我们可以通过使用`+`和`-`来配置要打印的源代码行数。例如`l +<lines-ahead> -<lines-back>`，其效果同上*打印指令*所述。

##### (g)打开生成的源代码

使用solidity 0.7.2或更高版本时，你可以使用此选项允许调试器进入solidity生成的内部汇编例程。你可以随时使用`;`指令，但此选项允许其它调试器命令（`n`，`i`，`o`，`u`）也进入这些例程。

##### (G) turn off generated sources

此指令撤销`g`指令，使调试器返回其生成源的默认行为。

请注意，当生成源关闭时，你仍然可以使用`;`进入它们。命令`;`如果一个断点被放置，继续`c`仍然会在这些断点上停止。此外，一旦进入这样的例程，其他调试指令（`n`，`i`，`o`，`u`）仍会在其中正常推进，它们将不会立即退出。

##### (h) print this help

打印可用调试命令列表。

##### (q) 退出

退出调试器。

##### (r) 重置（reset）

将调试器重置为交易的开头。

##### (b) 设置断点（set a breakpoint）

此命令允许我们为任何源文件中的任何行设置断点（请参阅下面的[添加和移除断点示例](https://learnblockchain.cn/docs/truffle/getting-started/debugging-your-contracts.html#adding-and-removing-breakpoints) ）。 命令后面可以接一个行号、或相对（当前）行号、 或者可以简单地在当前所在行添加断点。

你不需要加载交易来设置断点，但在这种情况下，必须指定要将其设置的源文件。

##### (B) 移除断点（大写的B）

此命令允许我们删除任何现有断点，方法和添加断点一样（请参阅下面的[添加和移除断点示例](https://learnblockchain.cn/docs/truffle/getting-started/debugging-your-contracts.html#adding-and-removing-breakpoints) ）。 键入 `B all` 删除所有断点。

##### (c) 跳到下一个断点

此命令将代码继续执行，直到到达下一个断点或执行到最后一行。

##### (+) 添加一个监视表达式

使用 `+:<expression>` 添加一个监视表达式， 这样在每次执行的时候，都可以看到监视表达式的值。

比如我们要调试 `addNote(string memory note)` 函数, 就可以使用 `+:note`:

```
debug(development:0xd2acb9c3...)> +:note
```

来查看note的内容。

##### (-) 移除监视表达式

使用 `-:<expression>` 删除监视表达式

##### (?) 列出所有的监视表达式及断点

此命令将显示所有当前监视表达式的列表及断点。

##### (v) 显示变量

此命令将显示当前变量及其值，但不会执行下一条指令。如果你希望使用上述逻辑查看交易后，查看当前的变量及其值的时候，可以使用这个选项。

这个指令也可以从变量显示中移除变量和变量值。如果你想移除solidity内置变量、全局常量、合约变量或局部变量时，你可以键入`v -builtins`来从显示中移除solidity内置变量及其它信息，使用`v -global`，`v -contract`，`v -local`。这些指令也可以简写，比如`v -bui`，`v -glo`，`v -con`，和`v -loc`，你也可以组合使用它们，比如`v -bui -glo`。

##### (T) 卸载交易

此命令卸载当前交易，以便可以加载新交易。

##### (t) 加载交易

此命令加载新交易（给定 交易哈希）。 请注意，如果您已经加载了交易，则必须首先显式卸载它，然后才能加载新交易。

#### 添加和移除断点

以下是一些添加和移除断点的例子。注意，添加断点（小写字母`b`）和移除断点（大写字母`B`）之间的区别。如果你想你想在调试器将要跳过的位置添加断点，这个断点将会自动向下移动到调试器能停止的下一个调试点位置，但这不适用于移除断点操作。

使用`?`命令可以列出当前的断点。

```bash
MagicSquare.sol:

11:   event Generated(uint n);
12:
13:   function generateMagicSquare(uint n)
      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

debug(develop:0x91c817a1...)> b 23
Breakpoint added at line 23.

debug(develop:0x91c817a1...)> B 23
Breakpoint removed at line 23.

debug(develop:0x91c817a1...)> b SquareLib:5
Breakpoint added at line 5 in SquareLib.sol.

debug(develop:0x91c817a1...)> b +10
Breakpoint added at line 23.

debug(develop:0x91c817a1...)> b
Breakpoint added at this point in line 13.

debug(develop:0x91c817a1...)> B all
Removed all breakpoints.

```

