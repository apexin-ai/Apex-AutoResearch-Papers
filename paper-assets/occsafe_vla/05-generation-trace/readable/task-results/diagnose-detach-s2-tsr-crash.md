# diagnose detach s2 tsr crash

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_detach_s2_tsr_crash_20260522T220637_result.json`
- **Structured JSON:** [`1018b8706be5e57e69fd.json`](../../sessions/10/1018b8706be5e57e69fd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 排查结果

### 1. 训练过程
- **无 NaN / OOM / CUDA 错误** — 日志干净
- **无 loss 数据** — `WANDB_MODE=disabled`，tqdm 也没打印 loss
- 50005 步全部完成，EXIT_CODE=0
- 训练速度始终稳定 ~1.08 it/s，与 s0 一致
- Checkpoint 正常保存于 10000/20000/30000/40000/50000 步
- 模型配置与 s0 完全一致（trainable params: 279,977,608）

### 2. Checkpoint
- 大小 15 GB，结构完整（4 safetensors shards + action_head 302MB + occ_head 2.4MB + proprio_projector 67MB + LoRA adapter 484MB）
- s0/s1 checkpoint 不在本服务器，无法直接对比大小

### 3. 逐任务 TSR 对比

| Task | s0 | s1 | s2 |
|------|-----|-----|-----|
| 0 | 0.98 | 1.00 | **0.70** |
| 1 | 0.96 | 0.96 | **0.72** |
| 2 | 1.00 | 1.00 | **0.92** |
| 3 | 1.00 | 1.00 | **0.90** |
| 4 | 0.90 | 0.80 | **0.30** |
| 5 | 0.34 | 0.36 | **0.16** |
| 6 | 1.00 | 0.98 | **0.66** |
| 7 | 0.98 | 0.94 | **0.66** |
| 8 | 0.98 | 0.94 | **0.74** |
| 9 | 1.00 | 1.00 | **0.48** |
| **Avg** | **0.914** | **0.898** | **0.624** |

CAR 几乎一致：s0=0.746, s2=0.748（碰撞数 127 vs 126）。

### 4. 结论

**不是正常的 seed variance，很可能有隐性训练异常。** 理由：

1. **全部 10 个任务一致性下降**——seed variance 会有升有降，不会 10/10 全跌
2. 跌幅极大：task 4 从 0.90→0.30，task 9 从 1.00→0.48
3. CAR 几乎不变 → occ_head 学习正常，问题出在 action prediction
4. **无法确认 loss 是否正常**——WANDB 禁用且 tqdm 未打印 loss，无法排除 silent gradient explosion/spike

**建议**：用 `WANDB_MODE=online` 重跑 s2（seed=2），捕获 loss 曲线以定位问题。如果 loss 曲线正常但 TSR 仍低，则确认是 bad seed；如果出现 loss spike，则说明训练不稳定。

---
