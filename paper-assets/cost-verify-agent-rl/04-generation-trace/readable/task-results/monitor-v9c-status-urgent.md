# monitor v9c status urgent

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_v9c_status_urgent_20260519T230842_result.json`
- **Structured JSON:** [`f66d0a2bbdb26c8bfa4c.json`](../../sessions/f6/f66d0a2bbdb26c8bfa4c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## v9c 状态：已崩溃

| 项目 | 值 |
|------|-----|
| 进程 | **DEAD**，`EXIT_CODE=1` |
| 崩溃位置 | Step 3/30（step 2 完成后，step 3 rollout 阶段崩溃） |
| 运行时长 | ~59 分钟（2 个 step） |
| GPU | 4 卡全部释放（0 MiB / 0%） |

### Step 2 指标（最后完成的 step）

| 指标 | 值 |
|------|-----|
| success | **0.6406** |
| entropy | 0.0746 |
| ppo_kl | -0.400 |
| grad_norm | 2.017 |
| pg_loss | 0.040 |
| response_length/max | 16043 |
| pass@8 | 1.0 |

### 崩溃原因

**vLLM prompt 长度溢出：**

```
ValueError: The decoder prompt (length 16384) plus the number of requested output tokens 
(at least 1) is longer than the maximum model length of 16384.
```

配置中 `max_prompt_length: 16384` 与 vLLM 的 `max_model_len: 16384` 相同。当某条 prompt 在多轮交互中增长到恰好 16384 tokens 时，无剩余空间生成 output，触发硬错误。

**修复方向：** 将 `max_prompt_length` 降低（如 15360 或 16000），为 generation 留出 headroom；或增大 vLLM 的 `max_model_len`。

---
