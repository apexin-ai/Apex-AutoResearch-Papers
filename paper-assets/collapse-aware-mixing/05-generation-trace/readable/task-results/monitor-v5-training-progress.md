# monitor v5 training progress

**collapse aware mixing** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_v5_training_progress_20260512T182741_result.json`
- **Structured JSON:** [`a57731406fdc8f0e702e.json`](../../sessions/a5/a57731406fdc8f0e702e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## mvp_pilot_v5 训练状态报告

### 进程状态
**ALIVE** — PID 32154，已运行 2h36m

### 当前阶段
**G0 checkpoint 评估中** — 正在评估 checkpoint 8/11 (checkpoint-1216)

Pipeline 进度：
| 阶段 | 状态 | 耗时 |
|------|------|------|
| 数据准备 | ✅ 完成 | 4 min (57052 sequences, 90M tokens) |
| G0 训练 (1373 steps) | ✅ 完成 | 51 min |
| G0 checkpoint 评估 (11个) | 🔄 进行中 (7/11 完成) | ~94 min elapsed |
| G1 训练 | ⏳ 未开始 | — |
| G2 训练 | ⏳ 未开始 | — |

### G0 训练指标
- **train_loss = 2.5459** — 正常范围，无异常
- 末尾 loss 趋势：2.5317 → 2.5311 → 2.5417（稳定收敛）
- grad_norm = 1.0~1.0625（正常，无梯度爆炸）
- 速度：1.99 s/step，14.3 samples/sec
- **10 个 checkpoint** 已保存（每 152 步一个）+ final_model (1.9GB)

### 已完成的评估指标（checkpoint 7/11 示例）
- eff_rank = 662.2
- ppl = 12.57
- entropy_var = 2.8272
- unigram_H = 6.989
- coverage = 0.4749
- 每个 checkpoint 评估耗时 ~808s（~13.5 min）

### GPU 状态
- 利用率：12%（评估/生成阶段，正常偏低）
- 显存：9.3 GB / 97.9 GB

### 异常信号
- ❌ 无 NaN / OOM / Error
- ⚠️ 大量 `right-padding` 警告（不影响训练，但刷屏严重，建议后续抑制）

### 预估剩余时间
评估瓶颈严重 — 每个 checkpoint 评估 ~13.5 min，每代 11 个 checkpoint：

| 剩余工作 | 预估耗时 |
|----------|---------|
| G0 评估剩余 4 个 checkpoint | ~54 min |
| G1 训练 | ~51 min |
| G1 评估 11 checkpoints | ~150 min |
| G2 训练 | ~51 min |
| G2 评估 11 checkpoints | ~150 min |
| **总计** | **~7.6 hours** |

**远超预期的 1-2 GPU-hours。** 瓶颈在 checkpoint 评估（每代 ~2.5h），而非训练本身（每代 ~51min）。3 代评估总计将耗费约 7.5h，训练只占 2.5h。

---
