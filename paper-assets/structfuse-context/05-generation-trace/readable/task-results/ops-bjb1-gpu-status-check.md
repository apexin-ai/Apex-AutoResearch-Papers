# ops bjb1 gpu status check

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_bjb1-gpu-status-check_20260513T061611_result.json`
- **Structured JSON:** [`97c8f39581bbbf0168e5.json`](../../sessions/97/97c8f39581bbbf0168e5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 训练状态汇总

### 两个实验均 **运行中**，双卡满载

| 实验 | GPU | 模型 | PID | 运行时间 | 显存占用 | GPU利用率 |
|------|-----|------|-----|---------|---------|----------|
| **m2_embed_verify** (Qwen2.5-Coder-3B) | GPU 1 | Qwen2.5-Coder-3B | 23729 | 50min | 49,872 MiB / 97,887 MiB | 100% |
| **plan_013_starcoder** (StarCoder2-3B) | GPU 0 | StarCoder2-3B | 23810 | 50min | 24,298 MiB / 97,887 MiB | 100% |

### 训练进度

**数据量**: 3,282 条训练样本

**plan_013_starcoder** (batch_size=4):
- Epoch 1, Step 500 / ~820 (61%)，即将触发 eval (eval_steps=500)
- Loss 趋势正常：0.59 → 0.52 → 0.05 → 0.17（波动但整体下降）
- 尚无 checkpoint 保存（save_steps=1000）

**m2_embed_verify** (batch_size=8):
- Epoch 1 已启动，日志仅显示模型加载完成，尚无 step 输出
- 推测刚刚进入训练循环（日志每 50 步输出一次，~410 steps/epoch，目前可能还在前 50 步内）
- 注意：日志只有 6 行，但进程已运行 50 分钟 — 可能日志缓冲未刷新，或实际训练速度较慢（batch_size=8 + num_negatives=7 + max_seq_length=2048 在 Qwen 3B 上显存压力较大）

### 估算剩余时间

- StarCoder2: 2 epochs × ~820 steps = ~1640 total steps，已完成 500 步（30%），按 50 min 跑 500 步推算，剩余约 ~1.9 小时
- Qwen: 2 epochs × ~410 steps = ~820 total steps，刚开始，按显存占用推算速度会更慢，预计 2-3 小时

### 注意事项

- W&B 设置为 **offline** 模式，指标只存本地
- 两个输出目录均为空（尚未到 save_steps=1000 的 checkpoint 保存点）
- m2_embed_verify 日志异常少（50 分钟只有 6 行），建议后续关注是否存在 I/O 阻塞或日志未 flush 的问题

---
