# analysis exp016 r1024 extract missing

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp016_r1024_extract_missing_20260514T232845_result.json`
- **Structured JSON:** [`d74ee5e9e0d2ed05b87c.json`](../../sessions/d7/d74ee5e9e0d2ed05b87c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已经有完整数据了。结论如下：

## 完整 Selection F1 表格 (exp_016_rerun_1024)

| Method | NER F1 | RE F1 |
|--------|--------|-------|
| greedy | 0.6439 | 0.4042 |
| random_avg | 0.6077 | 0.3544 |
| sj_best | 0.6450 | 0.3855 |
| voting_conf_best | 0.6337 | 0.3592 |
| logprob_best | 0.6501 | 0.3948 |
| ensemble_best | 0.6450 | 0.3855 |
| oracle | 0.7758 | 0.5850 |

### 缺失值说明

**`em_best` (exact_match_best) 和 `fk_best` (fleiss_kappa_best) 不存在于 exp_016_rerun_1024 的输出中。** 该实验只计算了 7 种 selection method 的 F1，没有单独为 exact_match 和 fleiss_kappa 信号做 best-of-N selection。

这两个信号只在 logistic ensemble 的 AUROC 分析中出现（作为特征），但没有作为独立的 selection criterion 输出 best-of-N F1 值。

### Random baseline 确认

- NER random_avg = 0.6077 ✓
- RE random_avg = 0.3544 ✓

如需补充 em_best 和 fk_best，需要修改实验脚本，用 exact_match / fleiss_kappa 分数作为 selection criterion 重新跑 best-of-N selection。

---
