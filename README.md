# NLP_module_demo
`python3.0+`  
NLP中各个技术点的模块化，这样就能在需要的时候快速组装
## 中文分句
## LSTM超参数调节
[连接](https://zhuanlan.zhihu.com/p/55671493)
- 小心过拟合，神经网络基本在“记忆”训练数据时，就会发生过拟合。过拟合意味着你在训练数据上有很好的表现，在其他数据集上基本无用。
- 正则化有好处：方法包括 l1、 l2和dropout等。
- 要有一个单独的测试集，不要在这个测试集上训练网络。
- 网络越大，功能就越强，但也更容易过拟合。 不要试图从10000个示例中学习一百万个参数，参数>样例=麻烦。
- 数据越多越好，因为它有助于防止过度拟合。
- 训练要经过多个epoch(算法遍历训练数据集)。
- 每个epoch之后，评估测试集表现，以了解何时停止(要提前停止)。
- 学习速率是最重要的超参数。
- 总体而言，堆叠层会有帮助。
- 对于LSTM，可以使用softsign(而不是softmax)函数替代双曲正切函数，它更快，更不容易饱和( 梯度大概为0 )。
- 更新器：RMSProp、AdaGrad或Nesterovs通常是不错的选择。AdaGrad也会降低学习率，这有时会有所帮助。
- 记住，要将数据标准化、MSE损失函数+恒等激活函数用于回归、Xavier权重初始化。
