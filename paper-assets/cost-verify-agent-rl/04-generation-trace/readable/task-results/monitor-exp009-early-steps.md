# monitor exp009 early steps

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_exp009_early_steps_20260514T033941_result.json`
- **Structured JSON:** [`cb938bb35c64d805d48a.json`](../../sessions/cb/cb938bb35c64d805d48a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**训练进程已退出。** PID 194788 不存在。

日志显示启动即失败，错误原因：

```
AssertionError: response mask is currently only supported for qwen and llama-3 models
```

配置中启用了 `enable_response_mask`，但模型路径不包含 "qwen" 或 "llama-3"，触发了 `train.py:137` 的断言检查。

训练从未开始，没有任何 step 输出。需要修复配置后重新启动。

---
