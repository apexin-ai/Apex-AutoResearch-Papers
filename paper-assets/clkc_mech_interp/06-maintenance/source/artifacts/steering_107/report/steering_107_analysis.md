# steering_107 实验结果分析

## 实验配置
- **模型**: Llama-3.1-8B-Instruct
- **Steering 层**: Layer 28 (probe peak layer)
- **探针精度**: 77.57%
- **测试样本**: 136 条知识冲突数据
- **Alpha 范围**: [-20, -10, -5, -2, -1, +1, +2, +5, +10, +20]
- **对照**: 随机正交方向（同幅度干预）

## Baseline 分布
| 类别 | 数量 | 占比 |
|------|------|------|
| contextual | 41 | 30.1% |
| both | 35 | 25.7% |
| parametric | 32 | 23.5% |
| neither | 28 | 20.6% |

## 核心结果表

| alpha | steering flips | control flips | steering rate | control rate | p→c | c→p | Fisher p |
|-------|---------------|---------------|---------------|--------------|-----|-----|----------|
| -20 | 20/136 | 23/136 | 14.7% | 16.9% | 0 | 2 | 0.740 |
| -10 | 14/136 | 13/136 | 10.3% | 9.6% | 0 | 1 | 1.000 |
| -5 | 6/136 | 5/136 | 4.4% | 3.7% | 1 | 0 | 1.000 |
| -2 | 5/136 | 4/136 | 3.7% | 2.9% | 1 | 0 | 1.000 |
| -1 | 6/136 | 4/136 | 4.4% | 2.9% | 2 | 0 | 0.749 |
| +1 | 1/136 | 1/136 | 0.7% | 0.7% | 0 | 0 | 1.000 |
| +2 | 3/136 | 2/136 | 2.2% | 1.5% | 0 | 0 | 1.000 |
| +5 | 5/136 | 6/136 | 3.7% | 4.4% | 0 | 0 | 1.000 |
| +10 | 10/136 | 9/136 | 7.4% | 6.6% | 0 | 0 | 1.000 |
| +20 | 17/136 | 24/136 | 12.5% | 17.6% | 1 | 0 | 0.309 |

## 结论：NEGATIVE（假设证伪）

### 关键发现

1. **Steering flip rate 未达到 ≥15% 阈值**。最高为 α=-20 的 14.7%，勉强接近但未达标。

2. **Steering 与随机对照无统计差异**。所有 alpha 的 Fisher exact p > 0.3，无一显著。大 |alpha| 时随机方向甚至产生更多 flips（α=20: random 17.6% > steering 12.5%）。

3. **方向性 flips (p→c, c→p) 极少**。全部 alpha 总计 p→c=6, c→p=3，说明观测到的 flips 几乎都是进出 both/neither 类别的噪声，而非 parametric↔contextual 的定向转换。

4. **Flip 率随 |alpha| 单调递增，且 steering/random 对称**。这表明 flips 由扰动幅度驱动，与方向无关——是通用的 representation 破坏效应。

### 解读

线性探针权重方向在判别意义上确实编码了冲突信号（精度 77.6%），但**不具有因果意义**。沿此方向干预不能定向控制模型的冲突解决行为。这说明：

- 探针捕获的是**相关性（correlational signal）**，而非因果机制的直接编码
- 知识冲突解决可能涉及**分布式、非线性计算**，不可简化为残差流中的单一线性子空间
- 或者因果方向存在，但不等于判别方向（probe weight ≠ causal direction）

## 对论文 story 的影响

- **D006 探针结果（77.6%精度）作为描述性/相关性发现仍然成立**，可以在论文中报告
- **不能声称因果性**——steering 实验是一个 clean negative，必须如实报告
- 这个 negative result 本身有价值：correlation ≠ causation 的实证案例，表明线性探针的高精度不等于 mechanistic understanding
- 如果写进论文，可以作为 "the gap between probing and intervention" 的讨论点

## 建议下一步

1. **DAS/Distributed Alignment Search**: 尝试非线性或多层干预方向，而非单层线性方向
2. **Activation patching**: 用 causal tracing 方法（如 path patching）定位真正的因果节点，而非假设探针方向即因果方向
3. **多层联合 steering**: 探针 peak 在 layer 28，但因果机制可能跨层分布，尝试多层联合干预
4. **重新审视 probe**: 用非线性探针（MLP probe）对比，看因果方向是否在非线性子空间中