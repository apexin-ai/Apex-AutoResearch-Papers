# ssh diagnose deepseek cwm s123 eval

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_diagnose-deepseek-cwm-s123-eval_20260520T045524_result.json`
- **Structured JSON:** [`f8b257a1f513f94b56c3.json`](../../sessions/f8/f8b257a1f513f94b56c3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Cron 已不存在（可能之前已清除），无影响。

## 结果汇总

**deepseek-cwm-repo-s123-eval** — DONE (success)

| 指标 | 值 |
|------|-----|
| Accuracy | **86.05%** |
| F1 macro | 80.93 |
| F1 pass / fail | 90.81 / 71.05 |
| Unparseable | 0 (0%) |
| Majority baseline | 72.96% |
| Gap vs majority | +13.09pp |
| Instances | 9784 / 9784 |

**注意**：s123 accuracy (86.05%) 与 s42 (61.49%) 差距达 24.56pp，远超正常 seed 方差。需要排查 s42 eval 是否有 bug（truncation、数据泄漏、checkpoint 选择等），或者确认两次 eval 使用的数据/代码版本是否一致。

---
