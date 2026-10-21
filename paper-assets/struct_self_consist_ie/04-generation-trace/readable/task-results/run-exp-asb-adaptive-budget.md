# run exp asb adaptive budget

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_run_exp_asb_adaptive_budget_20260520T175146_result.json`
- **Structured JSON:** [`d1b909c9eb80250432ba.json`](../../sessions/d1/d1b909c9eb80250432ba.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## ASB 实验完成 — 结果汇总

| 指标 | FewNERD (32565) | SciERC (529) | CoNLL (2756) |
|---|---|---|---|
| max_n | 8 | 8 | 16 |
| Greedy (N=1) F1 | 0.7478 | 0.6453 | 0.9070 |
| Uniform N=8 F1 | 0.7277 | 0.6382 | 0.9021 |
| **Adaptive F1** | **0.7440** | **0.6528** | **0.9046** |
| Oracle F1 | 0.7616 | 0.6658 | 0.9078 |
| **Δ(adaptive-uniform)** | **+0.0163** | **+0.0146** | **+0.0025** |
| Best predictor | MLP (0.5993) | RF (0.4843) | MLP (0.5071) |
| Mean optimal N | 4.40 | 4.29 | 3.94 |

**关键发现：**
- Adaptive allocation 在所有 3 个数据集上都优于 uniform N=8，且使用相同总预算
- 大多数实例最优 N≈4（远低于预算 8），说明很多实例不需要那么多 samples
- FewNERD 上 greedy F1(0.7478) > uniform N=8 F1(0.7277)，说明 majority vote 在简单实例上反而有害
- Top features: **degeneracy rate** 和 **agreement**（N=2 subsamples），说明极少量 samples 就能判断实例难度
- Oracle 上界 vs adaptive 有 gap（特别是 FewNERD +1.75），predictor 仍有改进空间

---
