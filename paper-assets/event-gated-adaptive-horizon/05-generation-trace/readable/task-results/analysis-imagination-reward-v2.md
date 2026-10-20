# analysis imagination reward v2

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_imagination_reward_v2_20260515T135127_result.json`
- **Structured JSON:** [`8a81c59014ec0416ff49.json`](../../sessions/8a/8a81c59014ec0416ff49.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇总结果：

---

### 结果总结

**Table 1: Trained Actor (N=100, 95% Bootstrap CI)**

| Model | dt=1 | dt=2 | Ratio |
|-------|------|------|-------|
| 008d | 0.363 [0.309, 0.421] | 1.052 [0.950, 1.157] | **2.90x** |
| 008f | 0.254 [0.163, 0.358] | 0.249 [0.156, 0.352] | 0.98x |

**Table 2: Random Policy (N=100, 95% Bootstrap CI)**

| Model | dt=1 | dt=2 | Ratio |
|-------|------|------|-------|
| 008d | 0.193 [0.161, 0.230] | 0.324 [0.280, 0.374] | **1.68x** |
| 008f | 0.095 [0.058, 0.138] | 0.106 [0.065, 0.153] | 1.11x |

**Decomposition (008d)**

| Component | Contribution |
|-----------|-------------|
| Dynamics bias (dt=2 embedding alone) | **1.68x** (~36%) |
| Actor exploitation (co-adaptation) | **64.2%** of total inflation |
| Total CIVO | **2.90x** |

008f sanity check 通过：无 dt embedding 时两种 policy 下 dt 值均无效果。

**文件产出**:
- 脚本: `analysis/imagination_reward_analysis_v2.py`
- JSON: `analysis/imagination_reward_results_v2.json`
- 报告已更新: `artifacts/imagination_reward_analysis.md`

---
