# restart grpo fast config

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_restart_grpo_fast_config_20260514T173835_result.json`
- **Structured JSON:** [`52abdb37d9ff8e38297a.json`](../../sessions/52/52abdb37d9ff8e38297a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个训练都在正常运行：

| 实验 | GPU | 显存 | Step 速度 | Total Steps | 预计时间 |
|------|-----|------|-----------|-------------|----------|
| `grpo_rasp_20_fast` | cuda:0 | 55161 MiB, 97% | ~25s/step | 500 | ~3.5h |
| `grpo_standard_20_fast` | cuda:1 | 55077 MiB, 96% | ~25s/step | 500 | ~3.5h |

**确认：**
- 训练数据 2000 samples ✓
- Total steps = 500（2000 / batch_size=2 / grad_accum=8 × 1 epoch × num_generations 调整 → 500）
- Step 时间 ~25s（远优于之前的 173s，满足 <50s 目标）✓
- RewardDesertCallback patience=50 ✓
- GSM8K 用了本地缓存（网络不通但不影响）✓

从 173s/step × 5604 steps ≈ 270h 降到 25s/step × 500 steps ≈ 3.5h，加速 ~77x。

---
