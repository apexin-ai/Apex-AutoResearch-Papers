# code fix v9d config and submit

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fix_v9d_config_and_submit_20260519T231124_result.json`
- **Structured JSON:** [`a96077a602d88942cdc1.json`](../../sessions/a9/a96077a602d88942cdc1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

本地无此 config 副本，仅服务器端有。

## 产出总结

### 1. Diff

```diff
# Line 88: agent_proxy.max_prompt_length
-  max_prompt_length: 16384
+  max_prompt_length: 15360
```

其余字段不变：
- `max_model_len: 16384`（L68，不变）
- `response_length: 1024`（L65，不变）
- `ppo_max_token_len_per_gpu: 16384`（actor 侧 token budget，不变）

**修复逻辑**：`15360 + 1024 = 16384 = max_model_len`，prompt 截断后保证至少 1024 token 的生成空间。

### 2. Checkpoint 恢复

**无可恢复 checkpoint。** v9c 在 step 3/30 崩溃，`save_freq: 999` 意味着训练期间不保存中间 checkpoint。westd-47453 上 `/root/autodl-tmp/checkpoints/` 下无任何 v9 相关目录。v9d 需从头开始。

### 3. 修改后关键参数确认

| 参数 | 值 | 位置 |
|------|-----|------|
| `max_prompt_length` | **15360** (已修改) | L88, agent_proxy |
| `max_model_len` | 16384 | L68, rollout |
| `response_length` | 1024 | L65, rollout |
| `resume_mode` | "disable" | trainer（从头训练） |

---
