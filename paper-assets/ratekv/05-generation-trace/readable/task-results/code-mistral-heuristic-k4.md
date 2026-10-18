# code mistral heuristic k4

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_mistral_heuristic_k4_20260514T115500_result.json`
- **Structured JSON:** [`cdfc7271914c667fa56c.json`](../../sessions/cd/cdfc7271914c667fa56c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。结果汇总：

## Mistral-7B-v0.3 Heuristic Baselines (k=4) — 结果

| Method | PPL | Budget |
|---|---|---|
| Baseline bf16 | 7.0351 | 1.0 |
| Uniform 4-bit | **7.1314** | 0.25 |
| MCKP (k=4) | 7.1648 | 0.248 |
| L0-random seed_0 | 7.1882 | 0.2559 |
| L0-random seed_1 | 7.1995 | 0.2559 |
| L0-random seed_2 | 7.1723 | 0.2559 |
| L0-random seed_3 | 7.3577 | 0.2559 |
| L0-random seed_4 | 7.2875 | 0.2559 |
| **L0-random mean** | **7.2411 ± 0.0707** | **0.2559** |
| **Naive positional** | **7.2105** | **0.2559** |

### 对照确认
- baseline = 7.0351 ✓, uniform = 7.1314 ✓, MCKP(k=4) = 7.1648 ✓

### 关键发现

1. **k=16→k=4 大幅改善**：L0-random 从 7.56 降至 7.24（Δ -0.32），naive 从 7.48 降至 7.21（Δ -0.27）。验证了 reviewer 关于 k=16 compounding 的 concern。

2. **Budget 不匹配**：heuristic budget=0.2559 vs MCKP budget=0.248（heuristic 多 3% 内存）。因为 k=4 时 L0@8-bit 的 "额外" 预算无法被 2-bit 节省完全抵消。MCKP k=4 不保护 L0（全部 4-bit + 4 个 2-bit），这也是 conservative comparison——heuristic 有更多预算却仍不如 MCKP。

3. **Mistral 仍是 genuine negative**：uniform 4-bit（7.131）优于所有 selective allocation 方案。低异质性下任何非均匀分配都是损失。

4. **Random ≈ MCKP**：最佳 L0-random (seed_2=7.172) 仅比 MCKP 差 0.008，中位数差 0.035。head sensitivity 非常均匀，random selection 几乎与 profile-guided optimization 一样好——强化 "heterogeneity determines benefit" 的 claim。

---
