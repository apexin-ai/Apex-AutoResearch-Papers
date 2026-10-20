# monitor v5 full status

**collapse aware mixing** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_v5_full_status_20260512T182725_result.json`
- **Structured JSON:** [`21a5ccb4674f8c90eea8.json`](../../sessions/21/21a5ccb4674f8c90eea8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## mvp_pilot_v5 训练状态报告

### 1. 进程状态: 存活

| 项目 | 值 |
|------|-----|
| PID | 32492 (父进程所属 session leader: 32154) |
| 状态 | R (running), 104 线程, 活跃运行中 |
| 命令 | `python3 pilot_pipeline.py --learning_rate 0.000002 --num_generations 3 ...` |
| 启动时间 | 2026-05-12 23:52 |
| 已运行 | ~2.5 小时 |
| GPU 占用 | 9304 MiB / 97887 MiB, 10% 利用率, 40°C |

### 2. 各代状态

| 代 | 训练 | 评估 | 合成数据 |
|----|------|------|----------|
| **G0** | **完成** (1373/1373 steps, 00:48 结束) | **进行中** (无输出文件，已耗时 ~1h42m) | 未开始 |
| **G1** | 未开始 | 未开始 | 未开始 |
| **G2** | 未开始 | 未开始 | 未开始 |

### 3. G0 训练详情

- **Loss 轨迹**: 2.641 (step 50) → 2.523 (step 550) → 2.517 (step 850) → 2.541 (step 1350) — 稳定收敛
- **Learning rate**: cosine decay, peak ~2e-6
- **Grad norm**: 稳定在 1.0-1.1（健康）
- **训练时长**: ~56 分钟
- **磁盘占用**: 59 GB (含所有 checkpoint)

### 4. Checkpoint 完整列表

```
G0/training/checkpoint-152   (00:02)
G0/training/checkpoint-304   (00:08)
G0/training/checkpoint-456   (00:13)
G0/training/checkpoint-608   (00:19)
G0/training/checkpoint-760   (00:25)
G0/training/checkpoint-912   (00:30)
G0/training/checkpoint-1064  (00:36)
G0/training/checkpoint-1216  (00:41)
G0/training/checkpoint-1368  (00:47)
G0/training/checkpoint-1373  (00:48)  ← 最终 step
G0/final_model/              (00:48)  ← 2GB safetensors + tokenizer
```

### 5. 评估阶段分析

pipeline 在 G0 评估阶段：需评估 11 个 checkpoint（10 + final_model），每个需要：
- 加载模型
- 生成 500K tokens（自回归生成，慢）
- 计算 spectral effective rank（50K samples）
- 计算 perplexity、KL、entropy 等

metrics 文件在**所有 checkpoint 评估完成后**才写入磁盘，所以目前无输出文件是正常的。GPU 10% 利用率符合自回归 token 生成的特征（memory-bandwidth bound）。

### 6. pilot_v4 vs v5

- **v4** (默认 lr=1e-5): 训练发散，loss 飙升到 106-116，grad_norm 90-106，在 step 775 被 Terminated
- **v5** (lr=2e-6): 训练稳定，loss 2.5-2.6，grad_norm 1.0-1.1，成功完成
- eval_ppl.log: v4 的 checkpoint-760 诊断，CE=114.8, PPL=inf — 确认 v4 已发散

### 7. analyze_g0.py holdout 修复

修复已到位。`load_holdout_data()` (line 70-80):
- `holdout_path` 非 None → `load_dataset(holdout_path, split="test")`
- `holdout_path` 为 None → 回退到 HuggingFace `wikitext-103-raw-v1`
- 支持缓存路径 `_packed_cache`
- `--holdout-path` 默认 None

### 8. 预估剩余时间

| 阶段 | 预估时长 | 状态 |
|------|----------|------|
| G0 评估 (11 ckpt × ~20min) | ~3.5h 总计, 还剩 ~2h | 进行中 |
| G0 合成数据生成 (90M tokens) | ~30-60min | 等待 |
| G1 训练 | ~56min | 等待 |
| G1 评估 | ~3.5h | 等待 |
| G1 合成数据生成 | ~30-60min | 等待 |
| G2 训练 | ~56min | 等待 |
| G2 评估 | ~3.5h | 等待 |
| **总计剩余** | **~12-15 小时** | |

---
