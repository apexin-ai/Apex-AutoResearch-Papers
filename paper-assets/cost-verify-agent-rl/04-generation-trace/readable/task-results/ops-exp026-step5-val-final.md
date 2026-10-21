# ops exp026 step5 val final

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_exp026_step5_val_final_20260515T142632_result.json`
- **Structured JSON:** [`ad3f809f6baf53df0b2a.json`](../../sessions/ad/ad3f809f6baf53df0b2a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

进程已确认全部终止。汇总：

```
STEP5_VAL_RESULT: NOT_AVAILABLE (val generation 已启动但未完成即被 kill)
KILL_STATUS: killed (781795 force_killed, 778562 terminated, 均已验证死亡)
CHECKPOINT: NONE (exp026/ 目录为空，save_freq=25 未触发)
FINAL_METRICS_SUMMARY:
┌──────┬───────┬─────────┬───────────────────┬─────────────────────┬────────┐
│ Step │ Phase │ Success │ action_is_valid   │ action_is_effective │ pass@16│
├──────┼───────┼─────────┼───────────────────┼─────────────────────┼────────┤
│  0   │ val   │  6.25%  │ 63.13%            │ 87.88%              │  -     │
│  1   │ train │ 21.88%  │ -                 │ -                   │  -     │
│  2   │ train │ 32.81%  │ 73.13%            │ 93.44%              │  -     │
│  3   │ train │ 17.19%  │ 71.88%            │ 93.75%              │  -     │
│  4   │ train │  0.00%  │ 71.69%            │ 93.66%              │  0.00% │
│  5   │ val   │   -     │   -               │   -                 │  -     │
└──────┴───────┴─────────┴───────────────────┴─────────────────────┴────────┘
```

关键观察：action_is_valid/effective 在 step 2-4 保持稳定（~72%/~94%），但 success 从 32.81% 崩至 0%——模型学会了生成"看起来合理"的 action 但完全丧失了完成任务的能力。GPU 已释放。

---
