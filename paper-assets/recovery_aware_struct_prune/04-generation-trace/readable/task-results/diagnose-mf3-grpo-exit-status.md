# diagnose mf3 grpo exit status

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_mf3_grpo_exit_status_20260522T095328_result.json`
- **Structured JSON:** [`dfdc4951d40908b13465.json`](../../sessions/df/dfdc4951d40908b13465.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
结论: SUCCESS
证据: 日志 "100%|██████████| 100/100 [1:38:31<00:00, 59.12s/it]" + "GRPO v4 recovery training complete."
最终 step: 100/100
model.safetensors: 存在 size=11.5GB
GPU 1 当前: 占用 (16547 MiB, 99%) — GSM8K 评估进程 PID 179898 正在运行
```

补充：GRPO 训练于 17:40:59 完成保存，之后自动触发了 GSM8K 评估（PID 179898，评估 1319 samples），目前仍在跑。GPU 0 被另一个 GRPO 任务 `grpo_rasp_alpha3p0_20`（PID 170676）占用。

---
