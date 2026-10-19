# diagnose analyzing exps bjb1 32546

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_analyzing-exps-bjb1-32546_20260522T162149_result.json`
- **Structured JSON:** [`ca648f11fbd931b8344f.json`](../../sessions/ca/ca648f11fbd931b8344f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个实验均已成功完成，registry 已更新为 DONE。

| 实验 | Success Rate | 详情 |
|------|-------------|------|
| eval-pi05-vla-only-goal-seed43-r4 | **98.0%** (196/200) | 10 tasks, 20 rollouts each, EXIT_CODE=0 |
| eval-pi05-vla-only-goal-seed44-r4 | **97.5%** (195/200) | 10 tasks, 20 rollouts each, EXIT_CODE=0 |

Cron 报 "no sentinel, no W&B" 是因为这些 eval 脚本没有写 sentinel 文件也没有上传 W&B，但实际都正常跑完了。两个 seed 的结果符合预期（~98%）。

---
