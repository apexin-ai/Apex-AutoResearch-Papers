# diagnose 8b sft clean eval v2 exit

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_8b_sft_clean_eval_v2_exit_20260519T112254_result.json`
- **Structured JSON:** [`5ff63041fbaf59b7ebe4.json`](../../sessions/5f/5ff63041fbaf59b7ebe4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。

**8b_sft_clean_eval_v2 结果：成功（EXIT_CODE=0，32 episodes）**

| Metric | Value |
|---|---|
| **success_rate** | **71.875%** |
| pass@1 | 71.875% |
| num_actions | 23.44 |
| action_is_valid | 95.95% |
| action_is_effective | 100% |
| response_length | 1731 |
| reward_mean@32 | 7.1875 |
| reward_std@32 | 4.496 |

Registry 已更新为 DONE/success，cron 已删除。

对比参考：之前 OOD 134 tasks 的 80.6% vs 现在 in-dist 32 tasks full-context 的 71.875%，in-dist 反而低约 9pp。

---
