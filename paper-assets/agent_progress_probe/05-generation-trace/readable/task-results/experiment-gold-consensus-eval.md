# experiment gold consensus eval

**Are Stagnation Signals Structural? A Systematic Empirical Study of Progress Detection in LLM Agents via Weak Supervision LLM-based agents deployed on software001** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_experiment_gold-consensus-eval_20260515T110043_result.json`
- **Structured JSON:** [`973c88222d568d2033c9.json`](../../sessions/97/973c88222d568d2033c9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 601-window 共识 gold set 评估完成

### 1. 数据匹配统计

| 指标 | 值 |
|------|-----|
| Gold 总数 | 601 (progress 418 / stagnation 183) |
| 结构模型匹配 (GB/RF/MV) | 584 |
| TWV Labels | 402 |
| TWV/GRU Probe | 386 |
| 未匹配 | 17 |

### 2. Per-model Macro-F1

| Model | N | Macro-F1 |
|-------|---|----------|
| TWV Labels | 402 | 0.7392 |
| TWV Probe | 386 | 0.7370 |
| **Structural GB** | 584 | **0.7237** |
| GRU Probe | 386 | 0.7028 |
| Structural RF | 584 | 0.6973 |
| MV Labels | 584 | 0.6818 |

### 3. Bootstrap 结果 (10,000 iter, seed=42)

| Test | Delta | 95% CI | p-value | Sig? |
|------|-------|--------|---------|------|
| GB vs MV | +0.042 | [+0.021, +0.065] | 0.0000 | **YES** |
| GB vs GRU Probe | +0.050 | [+0.012, +0.088] | 0.0048 | **YES** |
| RF vs GB | -0.026 | [-0.043, -0.010] | 0.0007 | **YES** (GB > RF) |
| TWV Probe vs GB | -0.016 | [-0.045, +0.013] | 0.1403 | NO |
| TWV Probe vs GRU | +0.034 | [-0.002, +0.070] | 0.0321 | Borderline |

### 4. Eval vs Bootstrap 一致性

一致。GB 在 full-coverage 模型中最优，显著优于 MV/RF/GRU Probe。TWV Probe vs GB 无显著差异。

### 5. 对比表：N=195 → N=601

| Model | Old (N=195) | New (N=601) | Δ |
|-------|-------------|-------------|-------|
| GB | 0.764 | 0.724 | -0.041 |
| RF | 0.752 | 0.697 | -0.054 |
| MV | 0.718 | 0.682 | -0.037 |
| GRU Probe | 0.735 | 0.703 | -0.032 |
| TWV Probe | 0.768 | 0.737 | -0.031 |

### 关键变化

1. **所有模型下降 3-5 pp**（更大 gold set 更难，含更多 OH 边缘案例），TWV Labels 例外（+2.1pp）
2. **GB 现在显著优于 RF**（p<0.001），N=195 时两者无差异
3. **GB vs GRU Probe 现在显著**（p=0.005），N=195 时 p=0.070
4. **TWV Probe vs GB 仍然无显著差异**（delta -1.6pp，p=0.14），两个评估一致

---
