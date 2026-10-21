# ssh check pythia410m status 20260517

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_check_pythia410m_status_20260517_20260517T112505_result.json`
- **Structured JSON:** [`1f5e0bccdfa9de70fdad.json`](../../sessions/1f/1f5e0bccdfa9de70fdad.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果报告

### 1. Pythia-410M (`pythia410m_wiki_a100_s42`) — **完成 ✓**

10 代全部完成 (gen_0 ~ gen_10)。进程仍在运行但输出已写完。

**Drift（gen_0 → gen_9）：**
| 指标 | gen_0 | gen_9 | drift |
|------|-------|-------|-------|
| distinct_1 | 0.098 | 0.072 | **-26.7%** |
| distinct_2 | 0.518 | 0.350 | **-32.5%** |
| token_entropy | 3.234 | 1.239 | **-61.7%** |
| ECE | 0.011 | 0.417 | **+3758.9%** |
| perplexity | 26.9 | 935.0 | **+3369.4%** |

**5-Method 分析（16 pairs = 4 canary × 4 downstream, sig_rate = 58/80）：**

| Method | Sig / 16 |
|--------|----------|
| Naive Pearson | **15/16** |
| Differenced XCorr | **16/16** |
| Threshold Onset | **10/16** |
| Toda-Yamamoto | **7/16** |
| Permutation Granger | **10/16** |

弱点集中在 `effective_rank` 作为 canary（TY 和 Threshold Onset 大面积 not_significant）和 `self_bleu->distinct_{1,2}`（TY、Permutation Granger、Threshold Onset 均 not_significant）。`token_entropy` 和 `ece` 作为 canary 表现最强。

### 2. OPT-1.3B (`opt1b_wiki_a100_s42`) — **进行中**

当前进度：**gen_8/10**，PID 249384 存活，预计还需约 50 分钟完成（按每代 ~24min 估算）。

---
