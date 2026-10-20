# ops grpo stage2 progress

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_grpo-stage2-progress_20260515T031037_result.json`
- **Structured JSON:** [`05d89472deb5b586d2db.json`](../../sessions/05/05d89472deb5b586d2db.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## GRPO Stage 2 进度报告（2026-05-15 ~03:12 UTC）

### 进程状态

| 实验 | PID | 运行时间 | 状态 |
|------|-----|---------|------|
| grpo_stage2_rasp_20 | 263888 | 1h59m | Ss+ (存活) |
| grpo_stage2_standard_20 | 263966 | 1h59m | Ss+ (存活) |

### GPU 状态

| GPU | 利用率 | 显存 | 功耗 |
|-----|--------|------|------|
| cuda:0 (rasp) | 100% | 52.0 / 97.9 GB | 596W |
| cuda:1 (standard) | 100% | 52.0 / 97.9 GB | 604W |

### 训练进度

| 实验 | 当前 step | 总 step | Step 1 耗时 | 预估 ETA |
|------|----------|---------|------------|----------|
| rasp_20 | **1/500** | 500 | 1h50m55s | ~38.5 天 (922h) |
| standard_20 | **1/500** | 500 | 1h52m04s | ~38.8 天 (932h) |

### 关键指标

**暂无。** wandb 只记录了 profiling 数据（generate、compute_loss 等），训练指标（reward、loss、grad_norm、clip_ratio）尚未出现。Step 1 刚完成，Step 2 正在 generation 阶段（已进行约 7 分钟）。

### Checkpoint

两个实验目录下均无 checkpoint，只有空的 `completions/` 目录。

### 健康判断

- **进程正常**：两个实验均存活，GPU 满载运行
- **严重问题：速度极慢**。每 step ~1h51m，500 steps 需要 **~38 天**。瓶颈在 `transformers.generate`（单 GPU 上对剪枝后的非均匀 MLP 模型做多轮 completion 生成）。按这个速度基本不可行，需要考虑：
  - 减少 `num_generations`（每 prompt 的 completion 数）
  - 减少总 step 数
  - 减小 `max_new_tokens`
  - 启用 vLLM 后端加速生成
- **无异常信号**：没有零梯度/NaN/OOM 等问题，但因为只完成了 1 step，还不足以判断 reward desert

---
