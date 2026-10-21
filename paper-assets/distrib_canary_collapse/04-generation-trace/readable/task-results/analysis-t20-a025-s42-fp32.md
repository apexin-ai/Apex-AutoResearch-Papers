# analysis t20 a025 s42 fp32

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_t20_a025_s42_fp32_20260521T050105_result.json`
- **Structured JSON:** [`12884d21c74622fae342.json`](../../sessions/12/12884d21c74622fae342.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 更新完毕，实验状态 → DONE。

---

## t20_a025_s42_fp32 分析摘要

### 训练状态
20 generations 全部完成，EXIT_CODE=0，gen_0 至 gen_20 目录完整。

### 完整 Metrics

| 指标 | 值 |
|---|---|
| **PermG FDR forward** | **3/8** |
| PermG FDR reverse | 0/8 |
| DiffXCorr FDR forward | 1/8 |
| DiffXCorr FDR reverse | 1/8 |
| Threshold onset forward | 4/8 |
| TY forward | 0/8 |
| **Robust pairs K≥3** | **1/8** |
| Robust pairs K≥4 | 0/8 |

### PermG FDR Detail (forward)

| Pair | F-stat | p_raw | p_FDR | Sig |
|---|---|---|---|---|
| token_entropy→distinct_1 | 232.69 | 0.0042 | 0.031 | **Yes** |
| token_entropy→distinct_2 | 200.82 | 0.016 | 0.043 | **Yes** |
| token_entropy→distinct_3 | 65.63 | 0.030 | 0.049 | **Yes** |
| token_entropy→mauve | 1.66 | 0.344 | 0.536 | No |
| ece→distinct_{1,2,3} | 0.4–1.5 | 0.35–0.50 | 0.536 | No |
| ece→mauve | 0.49 | 0.536 | 0.536 | No |

方向性完美：3 fwd / 0 rev。所有 3 个显著对均为 **token_entropy→distinct_X**，ECE canary 完全失灵。

### Drift (gen0→gen20)

| Metric | Gen0 | Gen20 | Drift % |
|---|---|---|---|
| token_entropy | 3.234 | 3.129 | **-3.3%** |
| distinct_1 | 0.098 | 0.058 | **-40.4%** |
| distinct_2 | 0.514 | 0.212 | **-58.7%** |
| distinct_3 | 0.813 | 0.301 | **-62.9%** |
| ece | 0.011 | 0.020 | **+84.9%** |
| perplexity | 26.95 | 21.93 | **-18.6%** |
| mauve | 0.031 | 0.020 | **-34.3%** |

### 与 Baseline 和其他 T=20 实验对比

| 实验 | PermG | K≥3 | K≥4 |
|---|---|---|---|
| **T=11 α=0.25** (3 seeds 一致) | **0/8** | 0 | 0 |
| **T=20 α=0.25** (本实验) | **3/8** | 1 | 0 |
| T=20 α=0.45 | 5/8 | 3 | 1 |
| T=20 α=0.50 | 6/8 | 6 | 2 |
| T=20 α=1.0 | 6/8 | 6 | 6 |

### 预测对比
- **Predicted** (T=10 sigmoid, α=0.25 deep below α_c≈0.475): **0/8**
- **Observed**: **3/8**
- **Verdict**: **FAIL** — point prediction 失败
- **blind_zone_conclusion**: **power_breakthrough**

### 论文意义

T=20 α=0.25 **打破了 T=11 blind zone**（0/8→3/8），确认 blind zone 是统计功效问题而非根本检测极限。T=20 dose-response 曲线 (α: 0.25→0.45→0.50→1.0 = PermG: 3→5→6→6) 平滑单调递增，证实 phase boundary α_c(T) 随 T 增大而左移。

关键细节：信号仍然脆弱（K≥3 仅 1/8），且**仅 token_entropy canary 有效**（ECE 完全无信号）——低 α 下两种 canary 的灵敏度出现分化，这为论文提供了一个额外发现：canary 选择在 near-blind-zone 区间具有决定性作用。

---
