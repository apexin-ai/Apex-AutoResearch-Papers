# ssh grpo fix and test

**prov grounded uie** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_grpo-fix-and-test_20260512T222414_result.json`
- **Structured JSON:** [`76ceb2abf82713821b79.json`](../../sessions/76/76ceb2abf82713821b79.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

sft_eval_v4 (PID 40391) 正常运行，已跑 55 分钟。

---

## 完整报告

### 1. 代码修改摘要

**config.py** — 删除 9 行：
- 移除 `use_vllm` (default=True)
- 移除 `vllm_mode` (default="colocate")
- 移除 `vllm_gpu_memory_utilization` (default=0.5)
- 移除 `vllm_enable_sleep_mode` (default=True)
- 移除相关注释行
- `bf16=True` 和 `gradient_checkpointing=True` 已正确，未改动

**train_grpo.py** — 删除 5 行：
- 从 `GRPOConfig(...)` 中移除 `use_vllm`, `vllm_mode`, `vllm_gpu_memory_utilization`, `vllm_enable_sleep_mode` 四个参数及注释
- `bf16`, `torch_dtype: torch.bfloat16`, `gradient_checkpointing` 已正确，未改动

### 2. Config 验证结果
```
bf16=True ✓
gradient_checkpointing=True ✓
has use_vllm: False ✓
max_completion_length=2048 ✓
```

### 3. 测试结果

**max_completion_length=2048** — OOM
- backward pass 时 OOM，需额外 2.32 GiB，GPU 只剩 1.33 GiB
- 峰值显存 ~85 GiB / 95 GiB

**max_completion_length=1024** — 成功完成 2 步
```
train_runtime: 88.48s
train_loss: 0.0
step_time: ~44s/step
```

### 4. 三个目标确认

| 目标 | 结果 |
|------|------|
| 无 OOM | ✓（1024 可跑通） |
| mean_length > 128 | ✓（mean_length=1024） |
| reward > 0 | ✗（reward=0.0） |

### 5. Reward 各 component

**全部为零。** `rewards/reward_fn/mean=0.0`, `rewards/reward_fn/std=0.0`。无法分拆 component——reward function 对所有生成返回 0。

根本原因：`completions/clipped_ratio=1.0`——所有 10 个 completion 全部被截断在 1024 token，没有一个自然结束（`mean_terminated_length=0`）。模型输出被截断后可能不构成合法格式，reward function 判定为 0。

### 6. OOM 明细

| max_completion_length | GPU 峰值显存 | 结果 |
|-----------------------|-------------|------|
| 2048 | ~85 GiB | OOM（backward需2.32G, 余1.33G） |
| 1024 | ~34 GiB | 成功（~60 GiB 余量） |

### 7. sft_eval_v4 状态
PID 40391，运行 55 分钟，状态 S（正常），GPU 0 显存 29.6 GiB，未受影响。

### 后续问题
reward 全零是核心问题。可能原因：
1. 所有生成被截断，不含完整结构化输出 → format reward = 0
2. 需要检查 reward function 对截断输出的处理逻辑
3. 可能需要增大 max_completion_length（但 2048 会 OOM），或优化模型让它生成更短的输出

---
