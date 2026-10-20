# code gpu probe 35694

**What Can IRT Person-Fit Statistics Reveal About SFT-Stage Benchmark Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_gpu-probe-35694_20260521T131031_result.json`
- **Structured JSON:** [`5acc291da51247144591.json`](../../sessions/5a/5acc291da51247144591.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇总

### GPU 状态（4× RTX PRO 6000 Blackwell, 各 96GB）

| GPU | VRAM | Util | 占用进程 |
|-----|------|------|---------|
| 0 | 20.4/95.6 GB (21%) | 97% | `train.py --condition clean_s8` (Llama) |
| 1 | 28.1/95.6 GB (29%) | 79% | `train.py --condition clean_s9` (Llama) |
| 2 | 10.7/95.6 GB (11%) | 81% | `train_grpo.py --gpu 2` (Post-RL) |
| 3 | 25.4/95.6 GB (27%) | 96% | `train.py --condition clean_s10` (Llama) |

**所有 4 卡满载，无空闲 GPU。**

### 旧 PID 状态
97791, 98622, 96745, 99214, 99807 — **全部已死。**

### 运行中任务

| 任务 | GPU | 进度 | 预计剩余 |
|------|-----|------|---------|
| GRPO v3 (post_rl_contam) | 2 | 466/3000 (15%) | ~1h50m |
| Llama clean_s8 | 0 | 377/939 (40%), epoch ~1.0 | ~10min |
| Llama clean_s9 | 1 | 376/939 (40%), epoch ~1.0 | ~10min |
| Llama clean_s10 | 3 | 377/939 (40%), epoch ~1.0 | ~10min |

Llama s8/s9/s10 快接近 epoch 1 结束，还有 3 个 epoch 要跑（总 939 steps = 3 epochs），约 10+20=30min 左右全部完成。

### 已完成任务

**Qwen (ctrl_contam_pilot)** — 全部完成 ✓
- clean_s1~s10 results 全部存在
- clean_s10 checkpoint: 3 个 checkpoint (313/626/939) ✓
- contam_15, contam_50 results ✓

**Llama (ctrl_contam_llama)** — s1~s7 完成，s8/s9/s10 训练中
- clean_s1(=clean), s2, s3, s4, s5, s6, s7 results ✓
- s8/s9/s10 checkpoints 目录已创建但尚无完整 checkpoint
- contam_15, contam_50 results ✓

**MIA SFT eval (post_rl_contam)** — 完成 ✓
- `mia_base_results.json` (4.0MB) ✓
- `mia_sft_results.json` (4.0MB) ✓
- `comparison_mia_lz.json` ✓

### 磁盘
- `/` : 1.4G / 30G (5%) — 充裕
- `/root/autodl-tmp` : 84G / 250G (34%) — 充裕

---
