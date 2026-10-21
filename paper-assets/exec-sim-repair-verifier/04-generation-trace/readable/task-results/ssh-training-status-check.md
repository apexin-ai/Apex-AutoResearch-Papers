# ssh training status check

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_training-status-check_20260520T102139_result.json`
- **Structured JSON:** [`0150341c1d179b1cbf59.json`](../../sessions/01/0150341c1d179b1cbf59.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 训练进度汇总 (2026-05-20 18:22 UTC)

### GPU 状态

| GPU | Util | VRAM | Temp |
|-----|------|------|------|
| 0 | 98% | 21.3/32.6 GB | 74°C |
| 1 | 99% | 20.3/32.6 GB | 76°C |
| 2 | 90% | 20.0/32.6 GB | 71°C |
| 3 | 93% | 31.3/32.6 GB | 76°C |

### 训练任务

| GPU | 任务 | Step | 进度 | sec/step | 已运行 | 剩余 | 预计完成 (UTC) | Checkpoint |
|-----|------|------|------|----------|--------|------|---------------|------------|
| 0 | Qwen3-8B CWM s123 (v4) | 1365/6633 | **20.6%** | 12.1 | 8h46m | ~17.7h | **May 21 ~12:00** | ckpt-1300 (18:09) |
| 3 | Qwen3-8B CWM s456 (v3) | ~1400/6633 (eval中) | **21.1%** | 11.7 | 8h45m | ~17.0h | **May 21 ~11:20** | ckpt-1300 (18:01) |
| 2 | DeepSeek CWM s123-v2 | 2025/12627 | **16.0%** | 8.0 | 4h30m | ~23.6h | **May 21 ~18:00** | 无 (尚未保存) |
| 1 | DeepSeek CWM s456-v2 | 528/12627 | **4.2%** | 7.9 | 1h18m | ~26.6h | **May 21 ~21:00** | 无 (尚未保存) |

### 关键信息

- **任务变化**: 与上次检查不同 — Qwen 改用 `train_repo_cwm.py` (Qwen3-8B, 非 Qwen2.5)，DeepSeek v2 改用 `train_unified.py` + `swebench_full/swebench_train.jsonl` (70748 样本，12627 steps)
- **GPU 3 VRAM 接近满载** (31.3/32.6 GB, 96%)，需关注 OOM 风险
- **DeepSeek s123-v2 checkpoints 为空**：2025 步没有保存任何 checkpoint，确认一下是否配置了 save_steps
- **Qwen 两个训练** 已保存 5 个 checkpoint（300, 1000-1300），save_total_limit=5，符合预期
- **所有进程正常运行，无 OOM、无报错**
- Qwen s456 刚完成 step 1400 的 eval，eval_loss=0.359

### 预计全部完成: May 21 ~21:00 UTC (DeepSeek s456-v2 最慢)

---
