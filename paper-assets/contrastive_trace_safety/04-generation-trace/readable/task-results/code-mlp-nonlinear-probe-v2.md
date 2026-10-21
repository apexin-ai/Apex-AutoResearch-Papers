# code mlp nonlinear probe v2

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_mlp_nonlinear_probe_v2_20260517T123523_result.json`
- **Structured JSON:** [`10654c8c7d67557aef59.json`](../../sessions/10/10654c8c7d67557aef59.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。结果汇总：

## MLP vs LR 对比

| Model | W | MLP bal_acc | MLP prec | MLP fpr | MLP cov | LR bal_acc | delta |
|-------|---|------------|----------|---------|---------|------------|-------|
| **r1_8b** | 1 | 0.806 | 0.646 | 0.137 | 0.767 | **0.817** | -0.011 |
| | 5 | **0.843** | 0.595 | 0.201 | 0.884 | - | - |
| | 10 | **0.846** | 0.592 | 0.206 | 0.884 | - | - |
| **r1_32b** | 3 | **0.713** | 0.585 | 0.245 | 0.800 | - | - |
| | 10 | 0.688 | 0.524 | 0.332 | 0.750 | **0.737** | -0.049 |
| **qwq_32b** | 5 | 0.604 | 0.339 | 0.692 | 0.842 | **0.761** | -0.157 |
| | 10 | **0.698** | 0.432 | 0.428 | 0.842 | - | - |
| **ot_7b** | 1 | 0.730 | 0.456 | 0.165 | 0.766 | - | - |
| | 3 | **0.747** | 0.343 | 0.362 | 0.872 | 0.688 | **+0.059** |

**关键发现：**

1. **r1_8b**: MLP W=1 略低于 LR (0.806 vs 0.817)，但 MLP W=5/10 达到 0.843-0.846，coverage 提升到 0.884
2. **r1_32b**: MLP 全面低于 LR baseline (best MLP=0.713 at W=3 vs LR W=10=0.737)
3. **qwq_32b**: MLP 显著低于 LR (best MLP=0.698 at W=10 vs LR W=5=0.761)，FPR 很高
4. **ot_7b**: MLP W=3 超过 LR baseline (+5.9%: 0.747 vs 0.688)

总体来看，MLP 非线性探针在 3/4 模型上**未超过 LR**（在同等 W 下），仅 ot_7b 有明显提升。这表明 hidden states 中的 safety-relevant 信号在大多数模型上是线性可分的，非线性并未带来一致性收益。小数据集（r1_32b=100, qwq_32b=95 traces）可能导致 MLP 过拟合。

结果已保存到 `/root/autodl-tmp/contrastive_trace_safety/artifacts/exp_r3_mlp_probe/results.json`。

---
