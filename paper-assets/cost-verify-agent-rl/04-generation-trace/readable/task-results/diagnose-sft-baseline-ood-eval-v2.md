# diagnose sft baseline ood eval v2

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_sft_baseline_ood_eval_v2_20260521T135709_result.json`
- **Structured JSON:** [`afd66e1039a297f425dc.json`](../../sessions/af/afd66e1039a297f425dc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。

**判定：成功完成**（W&B "crashed" 仅因 wandb teardown BrokenPipeError，eval 本身正常完成全部 134 episodes）

**结果：OOD success rate = 5.97%** (8/134)

| 指标 | 值 |
|------|-----|
| OOD success_rate | 5.97% |
| action_is_valid | 69.58% |
| action_is_effective | 99.40% |
| avg num_actions | 47.16 |
| reward_mean@134 | 0.597 |
| generation time | 1549.6s |

Registry 已更新为 DONE/success + metrics。Cron 已不存在（此前已清理或未创建）。GPU 3 已释放。

---
