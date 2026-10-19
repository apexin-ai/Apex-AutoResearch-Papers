# monitor exp 002 step1

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_exp_002_step1_20260513T205927_result.json`
- **Structured JSON:** [`d11499fe72ef61826c60.json`](../../sessions/d1/d11499fe72ef61826c60.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**exp_002 已崩溃。** Step 1 在 rollout generation 阶段报错退出（EXIT_CODE=1）。

### 错误原因

```
ValueError: The decoder prompt (length 32768) plus the number of requested output tokens (at least 1) 
is longer than the maximum model length of 32768.
```

某条 trajectory 的 prompt 在多轮交互中累积到了 32768 tokens，恰好等于 `max_model_len`，导致 vLLM 无法生成任何 output token。

### 初始验证结果（崩溃前完成的）

| 指标 | 值 |
|------|-----|
| success | 0.0% |
| invalid_action | 73.75% |
| reward/mean | -3.6875 |
| action_is_valid | 15.1% |
| action_is_effective | 26.25% |
| response_length | 9378 tokens |

### GPU 状态（进程已死）

| GPU | 利用率 | 显存 | 温度 |
|-----|--------|------|------|
| cuda:0 | 0% | 0 MiB / 97887 MiB | 28°C |
| cuda:1 | 100%* | 0 MiB / 97887 MiB | 35°C |

*GPU 1 显示 100% 利用率但 0 显存，是进程崩溃后 GPU 计数器未清零。

### 修复方向

需要防止 prompt 超长。几个选项：
1. **增大 `max_model_len`**（如 33792 或 36864），给 output 留余量——但会增加显存占用
2. **限制交互轮数或截断 prompt**，在 prompt 接近上限时提前终止 episode
3. **减小 `max_tokens`（generation）** 并在 rollout 前检查 prompt_len + max_tokens ≤ max_model_len

选项 2 最稳健——即使增大 max_model_len，长 episode 仍可能再次触顶。需要查看配置中是否有 `max_turns` 或 prompt truncation 相关参数。要我去查配置并修复吗？

---
