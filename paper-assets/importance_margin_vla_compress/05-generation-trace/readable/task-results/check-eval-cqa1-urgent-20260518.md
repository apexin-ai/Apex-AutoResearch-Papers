# check eval cqa1 urgent 20260518

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_eval_cqa1_urgent_20260518_20260518T212416_result.json`
- **Structured JSON:** [`9d3c2fe90b8c1c8e5ad2.json`](../../sessions/9d/9d3c2fe90b8c1c8e5ad2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
eval_baseline_control_100k_v2:
- 状态：完成
- 总 SR：45.0%
- Per-task SR：[task0: 0%, task1: 50%, task2: 74%, task3: 64%, task4: 68%, task5: 8%, task6: 58%, task7: 38%, task8: 52%, task9: 38%]

eval_smart_compress_m96_seed43:
- 状态：完成
- 总 SR：0.0%
- Per-task SR：[task0: 0%, task1: 0%, task2: 0%, task3: 0%, task4: 0%, task5: 0%, task6: 0%, task7: 0%, task8: 0%, task9: 0%]
- 所有 task mean_steps=280.0（全部 timeout）

训练状态：
- m64_seed43 (cqa1:1): 运行中（PID 202273，GPU 1，2785MiB）
- m32_seed43 (cqa1:3): 运行中（PID 200291，GPU 3，2873MiB，已跑 243 分钟）
```

---
