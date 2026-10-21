# exp-019 Analysis: LLaMA-8B StrategyQA 200 (D031 Powered Test)

**Date**: 2026-05-17
**Status**: NEGATIVE — 未达统计显著性，维持 Capability Trap analysis paper 方向

## 核心指标

| Metric | Value |
|--------|-------|
| SICA accuracy | 74.00% (148/200) |
| SC accuracy | 72.00% (144/200) |
| Delta | +2.00pp |
| McNemar p-value (exact) | 0.424 |
| McNemar p-value (chi2) | 0.285 |
| Bootstrap p-value (two-sided) | 0.345 |
| Bootstrap 95% CI | [-1.50pp, +5.50pp] |

## Contingency Table (Discordant Pairs)

|  | SC correct | SC wrong |
|--|-----------|----------|
| **SICA correct** | 139 | 9 |
| **SICA wrong** | 5 | 47 |

- Total discordant pairs: **14** (out of 200)
- SICA wins: 9, SC wins: 5
- Discordant rate: 7.0% — 绝大多数问题两种方法结果一致

## 与 exp-011 对比

| | exp-011 | exp-019 |
|--|---------|---------|
| n | 60 | 200 |
| Delta | +6.67pp | +2.00pp |
| p-value | 0.22 | 0.42 |
| 显著性 | 不显著 | 不显著 |

效应量从 +6.67pp 缩小到 +2.00pp。扩大样本量后效应非但没有被 confirm，反而缩水了 70%。exp-011 的 +6.67pp 可能是小样本波动。

## SICA Wins 分析 (n=9)

| Problem | GT | SICA | SC | SC Votes | 模式 |
|---------|-----|------|-----|----------|------|
| strategyqa_028 | Yes | Yes | No | 6:6 | 平票 |
| strategyqa_043 | No | No | Yes | 3:3 | 平票 |
| strategyqa_070 | Yes | Yes | No | 3:6 | SC 少数派正确 |
| strategyqa_101 | No | No | Yes | 3:3 | 平票 |
| strategyqa_123 | No | No | Yes | 3:3 | 平票 |
| strategyqa_127 | No | No | Yes | 7:5 | SC 多数派错误 |
| strategyqa_152 | No | No | Yes | 3:3 | 平票 |
| strategyqa_170 | No | No | Yes | 6:5 | SC 多数派错误 |
| strategyqa_199 | No | No | Yes | 6:6 | 平票 |

**关键发现**: 9 个 SICA wins 中 6 个是 SC 平票（3:3 或 6:6），SICA 本质上只是个 tiebreaker，不是系统性改进。

## SC Wins 分析 (n=5)

| Problem | GT | SICA | SC | SC Votes |
|---------|-----|------|-----|----------|
| strategyqa_046 | Yes | No | Yes | 3:3 |
| strategyqa_114 | Yes | No | Yes | 3:3 |
| strategyqa_125 | Yes | No | Yes | 3:3 |
| strategyqa_145 | No | Yes | No | 4:8 |
| strategyqa_194 | No | Yes | No | 7:5 |

SC wins 中 3 个也是平票 — constraint filtering 在这些 case 里选错了方向。

## Constraint Extraction Stats

| Metric | Value |
|--------|-------|
| Traces without constraints | 478/2400 (19.9%) |
| Total constraints extracted | 3,976 |
| Avg unique constraints/problem | 6.2 |

## SC Vote Distribution

| Category | Count | Ratio |
|----------|-------|-------|
| Unanimous SC (只有一个答案) | 109 | 54.5% |
| Close SC (minority >= 4/12) | 24 | 12.0% |

54.5% 的问题 SC 投票一致 — 这些 case 中 SICA 没有改变余地。

## 运行信息

- Model: LLaMA-3.1-8B-Instruct (vLLM)
- Dataset: StrategyQA, n=200, K=12, T=0.7
- Wall time: 50.4 min
- W&B: 未记录
- 结果文件: `/root/symb_invariant_consensus/results/exp019_strategyqa_200/exp019_results.json`
- 日志: `~/runs/symb_invariant_consensus/exp-019-llama8b-strategyqa-200.log`

## D031 决策判定

- **p = 0.424 >> 0.10** → 维持 Capability Trap analysis paper 方向
- 效应量 +2.00pp（CI 跨零）不支持 SICA 在弱模型上有显著增益的 claim
- SICA 在 LLaMA-8B 上的作用仅限于 tiebreaking，且 tiebreak 方向不一定正确
- 结合 exp-011 (+6.67pp shrunk to +2.00pp)，弱模型上的 SICA 增益是 noise 而非 signal
