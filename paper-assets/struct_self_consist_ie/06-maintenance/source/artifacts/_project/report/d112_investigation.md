# MF3 调查：Random vs Single 3.5pp 差距根因分析

## 结论

**Single (0.645) 实际上是 T=0 greedy decode 的 macro F1，而非论文标注的 "one T=1.0 draw"。**
3.5pp 差距是 greedy (T=0) vs stochastic sampling (T=1.0) 的预期差异，不是统计异常。

## 1. 精确定义追踪

### Paper Table 2 三个 baseline

| Paper 标签 | F1 | 代码变量 | 实际含义 |
|---|---|---|---|
| Greedy (T=0)† | 0.663 | `ner_greedy_f1` (report.json) | Micro F1, T=0 argmax, 551 instances |
| Single‡ | 0.645 ± 0.001 | `greedy_f1` (table2_selection_f1.py) | Macro F1, T=0 argmax, 529 instances (non-empty gold) |
| Random | 0.610 ± 0.003 | `random_f1` (table2_selection_f1.py) | Macro F1, mean of N=8 T=1.0 samples, 529 instances |

### 代码证据

table2_selection_f1.py:131-132:
```python
greedy = inst.get("greedy", samples[0])  # T=0 decode
g_f1 = per_instance_f1(greedy, gold, subtask=SUBTASK)
```

sampling.py (greedy 字段来源):
```python
raw_greedy = sampler.sample(prompts, n_samples=1, temperature=0.0, ...)
```

Paper caption: "$^\ddagger$Single: one T=1.0 draw" — 这与代码不符。

## 2. 数学解释

- 如果 Single 正确实现为 T=1.0 单次采样：E[Single] = E[Random] ≈ 0.610
- 当前代码：Single = F1(T=0 greedy) = 0.645，Random = E[F1(T=1.0 sample)] = 0.610
- 3.5pp 差距 = T=0 argmax vs T=1.0 stochastic 的解码策略差异

## 3. 对论文叙事的影响

正确 baseline 应为 Random (0.610)。信号 vs Random: LP +3.7pp, SJ/FK +3.6pp, EM +2.7pp, VC +1.3pp。信号能改善 random selection，但未能超过 T=0 greedy。