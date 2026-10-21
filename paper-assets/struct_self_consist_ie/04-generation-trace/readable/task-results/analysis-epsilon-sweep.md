# analysis epsilon sweep

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_epsilon_sweep_20260515T161811_result.json`
- **Structured JSON:** [`09c29e216fc794db8da8.json`](../../sessions/09/09c29e216fc794db8da8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

## 完整结果

### Selection F1 (%) — ε sweep 全表

**Qwen2.5-7B / SciERC** (n=529, N=16, 3 seeds)

| Signal | ε=0 | ε=0.01 | ε=0.02 | ε=0.05 | ε=0.1 | ε=0.2 | Range |
|--------|-----|--------|--------|--------|-------|-------|-------|
| SJ | 64.36 | 64.34 | 64.31 | 64.08 | 63.57 | 63.44 | 0.92pp |
| FK | 64.57 | 64.51 | 64.37 | 64.31 | 63.70 | 63.54 | 1.03pp |
| VC | 61.19 | 61.24 | 61.43 | 62.28 | 63.03 | 63.52 | 2.33pp |
| EM | 63.50 | 63.50 | 63.50 | 63.50 | 63.50 | 63.50 | 0.00pp |
| LP | 64.88 | 64.50 | 64.35 | 63.17 | 61.85 | 61.22 | 3.65pp |
| *Greedy* | *64.41* | | | | | | |

**Qwen2.5-7B / CoNLL2003** (n=2756, N=16, 1 seed)

| Signal | ε=0 | ε=0.01 | ε=0.02 | ε=0.05 | ε=0.1 | ε=0.2 | Range |
|--------|-----|--------|--------|--------|-------|-------|-------|
| SJ | 90.43 | 90.38 | 90.23 | 90.16 | 90.00 | 89.44 | 0.99pp |
| FK | 90.33 | 90.28 | 90.26 | 90.19 | 90.13 | 89.73 | 0.60pp |
| VC | 89.69 | 89.70 | 89.76 | 90.38 | 90.41 | 89.88 | 0.72pp |
| EM | 90.17 | 90.17 | 90.17 | 90.17 | 90.17 | 90.17 | 0.00pp |
| LP | 89.78 | 89.68 | 89.47 | 88.68 | 87.37 | 86.78 | 3.00pp |
| *Greedy* | *90.70* | | | | | | |

**LLaMA-3.1-8B / SciERC** (n=529, N=8, 3 seeds)

| Signal | ε=0 | ε=0.01 | ε=0.02 | ε=0.05 | ε=0.1 | ε=0.2 | Range |
|--------|-----|--------|--------|--------|-------|-------|-------|
| SJ | 64.36 | 64.38 | 64.28 | 63.99 | 63.39 | 62.94 | 1.45pp |
| FK | 64.43 | 64.46 | 64.38 | 64.43 | 64.13 | 63.52 | 0.93pp |
| VC | 63.78 | 63.80 | 63.80 | 63.85 | 64.31 | 63.98 | 0.53pp |
| EM | 63.66 | 63.66 | 63.66 | 63.66 | 63.66 | 63.66 | 0.00pp |
| LP | 64.55 | 64.06 | 63.99 | 63.07 | 62.51 | 61.97 | 2.58pp |
| *Greedy* | *64.58* | | | | | | |

**LLaMA-3.1-8B / CoNLL2003** (n=2756, N=16, 3 seeds)

| Signal | ε=0 | ε=0.01 | ε=0.02 | ε=0.05 | ε=0.1 | ε=0.2 | Range |
|--------|-----|--------|--------|--------|-------|-------|-------|
| SJ | 92.62 | 92.59 | 92.60 | 92.59 | 92.56 | 92.44 | 0.18pp |
| FK | 92.63 | 92.63 | 92.63 | 92.62 | 92.58 | 92.48 | 0.15pp |
| VC | 92.68 | 92.68 | 92.70 | 92.75 | 92.67 | 92.57 | 0.18pp |
| EM | 92.63 | 92.63 | 92.63 | 92.63 | 92.63 | 92.63 | 0.00pp |
| LP | 92.51 | 92.51 | 92.51 | 92.47 | 92.36 | 92.20 | 0.31pp |
| *Greedy* | *92.40* | | | | | | |

### Plateau 分析结论

**一致性信号 (SJ, FK, VC, EM)：**
- |F1(ε=0) − F1(ε=0.05)| 最大仅 1.09pp（VC on Qwen SciERC），均值 0.21pp
- 局部区间 [0.02, 0.1] 内最大变化 1.59pp，均值 0.37pp
- EM 完全不受 ε 影响（整数计分，ε<1 不改变选择）
- CoNLL 全部 range < 1pp

**LP 信号：**
- 更敏感（最大 range 3.65pp），因为 mean_logprob 是精细连续信号
- 这是 LP 的固有特性，恰好凸显了离散一致性信号对 ε 的鲁棒性优势

**ε-free 论证：**
Spearman ρ（信号分数 vs per-instance F1）是完全不依赖阈值的连续度量，论文已有报告。ε sweep 确认一致性信号在 ε∈[0, 0.2] 范围内 selection F1 基本不变，ε=0.05 仅为便利参数，不影响任何结论。

**Sanity check 通过：** ε=0 的 selection F1 与 `multiseed_selection_f1.json` 已有值完全一致。

**产出文件（服务器 `output/analysis_epsilon_sweep/`）：**
- `epsilon_sweep_results.csv` — 120 行完整结果
- `epsilon_sweep_summary.json` — 含逐信号 plateau 判定和结论

---
