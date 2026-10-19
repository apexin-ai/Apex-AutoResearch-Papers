# diagnose seed300 id eval diag result

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_seed300_id_eval_diag_result_20260522T191708_result.json`
- **Structured JSON:** [`b0b31aac585c4d55b913.json`](../../sessions/b0/b0b31aac585c4d55b913.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**结果：eval 成功完成，但表现极差。**

| 指标 | 值 |
|------|-----|
| **ID pass@1** | **0.0**（32 episodes 全部失败） |
| success | 0.0 |
| raw_reward | 0.0 |
| action_is_valid | 0.925625 |
| action_is_effective | 1.0 |
| response_length | 6224.25 |
| val-core/unknown/reward/mean@32 | 0.0 |

**enable_response_mask runtime 值**：config 中设为 `True`，grep 输出中同时出现了 `'enable_response_mask': False`（某个 config section 的默认值）和 `'enable_response_mask': True`（实际生效值）。最终生效的是 **True**。

**唯一错误**：wandb teardown 时的 `BrokenPipeError`，不影响 eval 结果。

**结论**：seed300 step5 checkpoint 在 ID eval（AlfworldSG, 32 episodes）上 pass@1 = 0.0，模型完全无法完成任务。

---
