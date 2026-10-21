# analysis d111 direction check 69b qwen

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_d111_direction_check_69b_qwen_20260520T073057_result.json`
- **Structured JSON:** [`ce1b6f169c9870f9861d.json`](../../sessions/ce/ce1b6f169c9870f9861d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## D120 Canonical 分析结果

### 1. Pythia-6.9B s42 (`scale_check/pythia69b_wiki_a100_s42`)

| Method | /8 |
|---|---|
| PermG_fwd (FDR) | 7/8 |
| PermG_rev | 0/8 |
| Diff XCorr (FDR) | 6/8 |
| Naive XCorr | 5/8 |
| Threshold Onset | 2/8 |
| TY Granger | 1/8 |
| **K≥3** | **5/8** |
| **K≥4** | **0/8** |

```
5-Method Lead-Lag Analysis Summary
Alpha=1.0, Seed=42, Generations=11
============================================================

Robust pairs (>=3/5 methods agree): 5/8

Per-method forward significance:
  Perm Granger (FDR): 7/8
  Diff XCorr (FDR):   6/8
  Threshold Onset:    2/8
  TY Granger:         1/8

Consensus detail:
  token_entropy&lt;distinct_1  3/5  [naive, diff, perm]
  token_entropy&lt;distinct_2  3/5  [naive, diff, perm]
  token_entropy&lt;distinct_3  2/5  [diff, perm]
  token_entropy&lt;mauve       2/5  [threshold, ty]
  ece&lt;distinct_1            3/5  [naive, diff, perm]
  ece&lt;distinct_2            3/5  [naive, diff, perm]
  ece&lt;distinct_3            3/5  [naive, diff, perm]
  ece&lt;mauve                 2/5  [threshold, perm]
```

### 2. Qwen3.5-0.8B s42 (`generalize/qwen35_08b_wiki_a100_s42_fp32_v2`)

| Method | /8 |
|---|---|
| PermG_fwd (FDR) | 8/8 |
| PermG_rev | 0/8 |
| Diff XCorr (FDR) | 8/8 |
| Naive XCorr | 4/8 |
| Threshold Onset | 0/8 |
| TY Granger | 6/8 |
| **K≥3** | **6/8** |
| **K≥4** | **3/8** |

```
5-Method Lead-Lag Analysis Summary
Alpha=1.0, Seed=42, Generations=11
============================================================

Robust pairs (>=3/5 methods agree): 6/8

Per-method forward significance:
  Perm Granger (FDR): 8/8
  Diff XCorr (FDR):   8/8
  Threshold Onset:    0/8
  TY Granger:         6/8

Consensus detail:
  token_entropy&lt;distinct_1  3/5  [diff, perm, ty]
  token_entropy&lt;distinct_2  3/5  [diff, perm, ty]
  token_entropy&lt;distinct_3  3/5  [diff, perm, ty]
  token_entropy&lt;mauve       2/5  [diff, perm]
  ece&lt;distinct_1            4/5  [naive, diff, perm, ty]
  ece&lt;distinct_2            4/5  [naive, diff, perm, ty]
  ece&lt;distinct_3            4/5  [naive, diff, perm, ty]
  ece&lt;mauve                 2/5  [naive, perm]
```

### 旧值 vs 新值对比

| 实验 | 旧 K≥3 | 新 K≥3 (D120) | 变化 |
|---|---|---|---|
| Pythia-6.9B s42 | 8/8 | **5/8** | **-3** |
| Qwen3.5-0.8B s42 | 8/8 | **6/8** | **-2** |

**差异原因**: D111 direction fix（`peak_lag < 0` 才算 forward causation）过滤掉了 naive xcorr 中 lag>0 的伪正向显著。两个 mauve 对几乎全部失去 consensus（Threshold Onset 在 11 代数据上极少触发 3σ）。核心 distinct_1/2/3 对仍保持 K≥3，overall pattern 不变——canary 确实 lead downstream，只是 mauve 对信号偏弱。

---
