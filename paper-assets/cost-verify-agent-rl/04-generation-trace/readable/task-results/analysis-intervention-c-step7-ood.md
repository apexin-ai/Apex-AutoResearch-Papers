# analysis intervention c step7 ood

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_intervention_c_step7_ood_20260521T232105_result.json`
- **Structured JSON:** [`a28394e39652cf8f0584.json`](../../sessions/a2/a28394e39652cf8f0584.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。结果摘要：

**Intervention C Step 7 OOD 评估结果**

| 指标 | 值 |
|------|-----|
| **OOD pass@1** | **14.93%** (20/134) |
| action_is_valid | 66.30% |
| num_actions | 43.67 |
| response_length | 6365.6 |
| eval_time | 1370s |

**结论**: success — hypothesis confirmed。Hard cap 导致的 collapse checkpoint OOD=14.93%，低于 15% 阈值，与预期一致。这区别于 Seed 4 的异常（collapsed 但 OOD=30.6%），表明 hard cap 引发的 collapse 不仅训练失败，还产生更差的 OOD 泛化。

Registry 已更新为 DONE(success)，report 已注册。

---
