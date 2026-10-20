# infra westd status check loop20

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_westd-status-check-loop20_20260516T010855_result.json`
- **Structured JSON:** [`0d25f0e396fee59a8b41.json`](../../sessions/0d/0d25f0e396fee59a8b41.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 实验状态汇总

### 进程状态

| 实验 | PID | 状态 | GPU | 进度 |
|------|-----|------|-----|------|
| **CWM 8B ckpt400 test eval v3** | 443221 | **ALIVE** | cuda:3 | 5472/9784 (55.9%) |
| **CLS 8B s42-resume ckpt1000 test mutation** | 444130 | **ALIVE** | cuda:1 | 7210/9784 (73.7%) |
| **CLS 8B s42 ckpt1000 test mutation** | 444502 | **ALIVE** | cuda:0 (CUDA_VISIBLE_DEVICES=0) | 6950/9784 (71.0%) |
| **CWM 8B training (resume from ckpt-6100)** | 442200 | **ALIVE** | cuda:2 | 已保存到 ckpt-6100，正在继续训练 |

### GPU 利用率

| GPU | 显存占用 | 利用率 | 任务 |
|-----|---------|--------|------|
| cuda:0 | 17.6/32.6 GB (54%) | 78% | cls8b_s42_ckpt1000_test_mutation |
| cuda:1 | 17.6/32.6 GB (54%) | 99% | cls8b_s42_resume_ckpt1000_test_mutation |
| cuda:2 | 29.3/32.6 GB (90%) | 99% | CWM 8B training (resume ckpt-6100) |
| cuda:3 | 21.1/32.6 GB (65%) | 88% | CWM 8B ckpt400 test eval |

**所有 4 张 GPU 都在使用中，无空闲 GPU。**

### 关键指标

- **CWM 8B eval**: running_acc=61.1% (新处理 185 samples)，每 batch 约 57 秒，预计剩余 ~4.7 小时完成
- **CLS 8B resume mutation eval**: running_acc=83.1%，速度 ~10 samples/1.4s，预计 ~36 分钟完成
- **CLS 8B s42 mutation eval**: running_acc=83.2%，预计 ~40 分钟完成
- **CWM 8B training**: checkpoints 5800→5900→6000→6100 每隔约 40 分钟保存，save_total_limit=5

### Tmux Sessions

- `ckpt_backup` (May 14)
- `cwm8b-ckpt400-test-eval-v3` (May 16 08:46)

无错误或异常，所有进程正常运行。

---
