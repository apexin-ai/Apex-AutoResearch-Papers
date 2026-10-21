# analysis exp 064 completion check

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp-064-completion-check_20260519T181317_result.json`
- **Structured JSON:** [`d667efbf59dc98cdd41c.json`](../../sessions/d6/d667efbf59dc98cdd41c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Cron 已不存在（可能在之前的 session 中创建，当前 session 无残留）。

**诊断结果：exp-064 成功完成。**

| 指标 | 值 |
|---|---|
| SC accuracy | 83.8% (171/204) |
| SICA accuracy | 83.8% (171/204) |
| Delta (SICA - SC) | 0.0% |
| Extraction rate | 38.2% |
| Contradiction rate | 1.7% |
| Wall time | 355.6 min |
| n_samples | 204/204 |

Registry 已更新：status=DONE, conclusion=success, metrics/checkpoint_path/log_path 均已设置。Cron 在当前 session 中不存在，无需清除。

注意：如任务说明所述，此实验用 legacy 代码，SC 数据可用但 SICA/delta 不入 Table 1（sica_not_comparable）。delta=0 本身也说明 SICA 未对 SC 产生增益，与 extraction_rate 仅 38.2% 一致——约束提取率过低导致 SICA 几乎退化为 SC。

---
