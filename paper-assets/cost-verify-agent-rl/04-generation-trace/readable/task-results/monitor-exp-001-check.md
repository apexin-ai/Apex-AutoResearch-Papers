# monitor exp 001 check

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_exp_001_check_20260513T191117_result.json`
- **Structured JSON:** [`327ca6495cf0764533ef.json`](../../sessions/32/327ca6495cf0764533ef.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

report.md 是自动生成的，无法手动写入。直接汇报结果：

---

## exp_001 状态: FAILED

| 项目 | 结果 |
|------|------|
| **进度** | step 6/50（第 7 步崩溃） |
| **GPU 利用率** | 0%（双卡空闲，无 GPU 进程） |
| **PID 87845** | 已终止 |
| **退出码** | 1 |

**错误**:
```
ValueError: The decoder prompt (length 4096) plus the number of requested output tokens
(at least 1) is longer than the maximum model length of 4096.
```

**原因**: 多轮 rollout 累积的 prompt 在 step 7 达到 4096 tokens 上限（等于 `max_model_len`），vLLM 拒绝生成因为没有剩余空间给输出 token。

**修复方向**: 增大 `max_model_len`（如 8192），或在 rollout 时截断/压缩历史 prompt 使其不超过 `max_model_len - max_new_tokens`。

---
