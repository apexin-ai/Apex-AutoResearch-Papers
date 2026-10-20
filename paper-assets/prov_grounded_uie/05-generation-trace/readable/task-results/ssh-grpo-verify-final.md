# ssh grpo verify final

**prov grounded uie** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_grpo-verify-final_20260512T225904_result.json`
- **Structured JSON:** [`77a60fb80343ffbf6b4e.json`](../../sessions/77/77a60fb80343ffbf6b4e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

GRPO 验证完成，3 步训练成功。

---

## GRPO 最终验证报告

### 1. cuda:1 状态
- 清理了 PID 58729（旧采样参数调试进程），cuda:1 已空闲
- cuda:0 PID 40397（sft_eval_v4）未受影响

### 2. 配置验证
| 参数 | 值 | 状态 |
|------|-----|------|
| top_k | 20 | ✓ |
| top_p | 0.95 | ✓ |
| temperature | 0.7 | ✓ |
| bf16 | True | ✓ |
| gradient_checkpointing | True | ✓ |
| max_completion_length | 2048 (config默认) | ✓ |

### 3. 训练运行结果（3 steps, ~3分9秒）

```
train_runtime: 189.29s
train_loss: -0.1361
step_time: ~62.3s/step
```

### 4. 五项验证目标

| # | 指标 | 值 | 目标 | 结果 |
|---|------|-----|------|------|
| 1 | completions/mean_length | **743.8** | < 1024 | **PASS** — 自然终止，非截断 |
| 2 | reward | **0.4804** | > 0 | **PASS** |
| 3 | completions/clipped_ratio | **0.333** | < 1.0 | **PASS** — 仅 1/3 被截断 |
| 4 | OOM | 无 | 无 OOM | **PASS** — 76GB VRAM，正常完成 |
| 5 | train_loss | **-0.1361** | ≠ 0 | **PASS** — 有学习信号 |

### 5. Reward 详情

| 指标 | 值 |
|------|-----|
| rewards/reward_fn/mean | 0.4804 |
| rewards/reward_fn/std | 0.0265 |
| frac_reward_zero_std | 0.333 |
| kl | 2.11e-05 |
| entropy | 0.0225 |
| clip_ratio (low/high/region) | 全为 0.0 |

自然终止的 completions 平均长度 402.5 tokens（terminated_length），远低于 1024 上限。

### 6. 结论

**GRPO 训练 ready for 正式跑。** 采样参数修复（top_k=20, top_p=0.95）后，completions 正常自然终止，reward 稳定为正，无 OOM，loss 有梯度信号。唯一注意：`per_device_train_batch_size` 需设为 `num_generations` 的倍数（本次用 batch_size=2, num_generations=2）。

---
