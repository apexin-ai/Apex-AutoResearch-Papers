# analysis test eval 4b rsft s44 with evi

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_test_eval_4b_rsft_s44_with_evi_20260523T104602_result.json`
- **Structured JSON:** [`8cf0bbfaafe8caf5565e.json`](../../sessions/8c/8cf0bbfaafe8caf5565e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新为 DONE/success。

**汇总：**

s44 with-evi: **ign_f1=0.2525**, evi_f1_tp=0.6155, edcr=0.8324

3-seed with-evidence 对比：

| seed | ign_f1 | evi_f1_tp | edcr |
|------|--------|-----------|------|
| s42 | 0.2501 | 0.6237 | 0.8288 |
| s43 | 0.2503 | 0.6127 | 0.8425 |
| s44 | 0.2525 | 0.6155 | 0.8324 |
| **mean** | **0.2516** | **0.6173** | **0.8346** |
| std | 0.0014 | 0.0057 | 0.0069 |

s44 ign_f1 略高于 s42/s43（+0.22-0.24pp），三 seed 方差很小（std=0.0014），结果稳定。对应 no-evi s42=0.2652, s43=0.2702，待 s44 no-evi 完成后可计算 3-seed mean evidence tax。

---
