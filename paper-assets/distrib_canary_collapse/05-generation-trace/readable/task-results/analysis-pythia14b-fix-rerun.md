# analysis pythia14b fix rerun

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_pythia14b_fix_rerun_20260518T001149_result.json`
- **Structured JSON:** [`203dead0b654832d68c4.json`](../../sessions/20/203dead0b654832d68c4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

确认 C4 (n_perm=1000, max_lag=1) 和 OPT-1.3B (n_perm=1000, max_lag=1) 也有同样的参数错误。

## 修正结果汇报

### 修改内容
三个参数已修正到 `pythia14b_8pair_analysis.py`：
- DOWNSTREAM: `mauve` → `perplexity`（Wiki 的 perplexity drift +3340%，mauve 仅 -15%）
- N_PERM: 1000 → 5000
- xcorr max_lag: 3 → 5（naive_pearson 和 diff_xcorr 的 default param，Granger max_lag=1 不变）

### 修正后结果

| 方法 | Sig/8 |
|---|---|
| naive_xcorr | **4/8** |
| diff_xcorr_fdr | **6/8** |
| threshold_onset | **8/8** |
| permg_fwd_fdr | **2/8** |
| permg_rev_fdr | **0/8** |
| ty_granger | **0/8** |
| consensus_ge4 (K≥4/5) | **1/8** |

### 关键问题：PG_fwd raw=5/8 但 FDR 后=2/8

PG_fwd **raw p<0.05** 的 pairs 有 5 个：
- ece→distinct_1 (p=0.0042), ece→distinct_2 (p=0.0086), ece→distinct_3 (p=0.0216)
- token_entropy→distinct_1 (p=0.0274), token_entropy→distinct_2 (p=0.0346)

但当前脚本把 **40 个 p-values**（8 pairs × 5 methods）池化做 BH FDR，导致 borderline p-values (0.02-0.05) 被校正掉。如果 Table 7 的 PG_fwd=5/8 是 raw p<0.05，那数字吻合。

FDR scope（pooled vs per-method）是数字不匹配的根因。即使 per-method FDR（仅 8 个 PG_fwd p-values 一起校正），也只有 2/8 通过。

### 其他实验参数风险

**C4** 和 **OPT-1.3B** 的已有分析同样存在：
- n_perm=1000（应为 5000）
- xcorr max_lag 未独立于 Granger max_lag 设置

C4 的 DOWNSTREAM 用 mauve 是合理的（C4 的 mauve drift 大），但 n_perm 和 xcorr max_lag 需要修正后重跑。

---
