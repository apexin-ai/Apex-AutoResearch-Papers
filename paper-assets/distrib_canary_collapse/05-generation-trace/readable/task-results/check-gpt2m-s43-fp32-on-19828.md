# check gpt2m s43 fp32 on 19828

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_gpt2m_s43_fp32_on_19828_20260520T093108_result.json`
- **Structured JSON:** [`aa47d0bf8b5910852ec8.json`](../../sessions/aa/aa47d0bf8b5910852ec8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

**服务器**: westd-19828  
**路径**: `/root/autodl-tmp/distrib_canary_collapse/results/gen_wiki_gpt2m_a100_s43/analysis/5method_summary.txt`

**关键数值**:
- **PermG (FDR)**: 6/8
- **K≥3 (robust pairs)**: 6/8
- DiffXCorr: 6/8, TY Granger: 4/8, Threshold Onset: 0/8

**D102 canonical 确认**: JSON 中 `threshold_criterion: "true_3sigma_d105"` 且使用 5 方法 (naive_xcorr, diff_xcorr, threshold_onset, perm_granger, ty_granger)，`n_perm: 5000`, `fdr_alpha: 0.05`——符合 D105+D111 canonical pipeline 配置。

注意目录命名是 `gen_wiki_gpt2m_a100_s43`（无 `_fp32` 后缀），不在 `generalize/` 子目录下，而是直接在 `results/` 下。

---
