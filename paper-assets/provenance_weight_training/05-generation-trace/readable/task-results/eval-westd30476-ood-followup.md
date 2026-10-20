# eval westd30476 ood followup

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_westd30476_ood_followup_20260520T044306_result.json`
- **Structured JSON:** [`0aec79c4158d04bd9e6a.json`](../../sessions/0a/0aec79c4158d04bd9e6a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有 holdout 指标已恢复，OOD 指标已正确合并。

## 最终汇总

8/8 checkpoint OOD eval 全部完成，结果已写入 registry（保留了原有 holdout 指标）。

| exp_id | Holdout PPL | OWT PPL | Wikitext PPL |
|---|---|---|---|
| epoch_matched_dr_seed123 | 17.66 | 18.30 | 27.90 |
| epoch_matched_dr_seed456 | 17.66 | 18.27 | 28.14 |
| detect_remove_q01_seed42 | 17.40 | 18.22 | 28.22 |
| detect_remove_q02_seed42 | 17.27 | 18.06 | 27.64 |
| detect_remove_q03_seed123 | 17.25 | 18.03 | 27.53 |
| detect_remove_q03_seed456 | 17.25 | 18.03 | 27.61 |
| detect_remove_q05_seed123 | 17.27 | 18.01 | 27.75 |
| detect_remove_q05_seed456 | 17.28 | 18.01 | 27.68 |

**说明：**
- 因 `wikimedia/wikipedia` 在 AutoDL 上 HF 超时无法下载，Wikipedia 指标改用 `wikitext-103-v1`（Salesforce/wikitext test split, 1942 docs），字段名为 `eval_ppl_wikitext`
- OpenWebText 使用完整 5000 docs
- OOD PPL 趋势与 holdout 一致：q03 阈值区间（q03/q05）OOD 表现最好，epoch_matched 和 q01 稍差

---
