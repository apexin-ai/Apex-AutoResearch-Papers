# ops westd status check loop19

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_westd-status-check-loop19_20260516T010605_result.json`
- **Structured JSON:** [`d9118e0222727776f531.json`](../../sessions/d9/d9118e0222727776f531.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 服务器状态汇报

### GPU 状态

| GPU | 显存占用 | 利用率 | 任务 |
|-----|---------|--------|------|
| 0 | 17.6/32.6 GB (54%) | 77% | CLS 8B eval (ckpt-1000, test mutation) |
| 1 | 17.6/32.6 GB (54%) | 99% | CLS 8B eval (ckpt-1000, resume test mutation) |
| 2 | 29.3/32.6 GB (90%) | 88% | **CWM 8B 训练** (从 ckpt-6100 继续) |
| 3 | 21.1/32.6 GB (65%) | 89% | CWM 8B ckpt-400 test eval |

**4 块 GPU 全满载。**

---

### 1. CWM 8B v5 训练 (GPU 2, PID 442200) — 新进程，非原 PID 400279

- 从 checkpoint-6100 恢复训练，总步数 6633
- 当前进度: **6195/6633 (93%)**, ~12s/step
- 剩余 ~438 步 → **ETA ~1.5h (约 10:36)**
- 已保存 checkpoints: 400, 5800, 5900, 6000, 6100 (save_total_limit=5)

### 2. CWM 8B ckpt-400 test eval (GPU 3, PID 443221) — 新进程，非原 PID 381618

- 进度: **5440/9784 (55.6%)**, 增量恢复了 5287 条旧结果
- 新评估样本: 153 条, running_acc = **59.5%**
- 速率 ~8 样本/min (batch=8, max_new_tokens=1024 生成慢)
- 剩余 4344 样本 → **ETA ~8-9h (约 17:00-18:00)**

### 3. CLS 8B ckpt-1000 test mutation eval × 2 (GPU 0 & 1)

两个并行 CLS eval，同一 checkpoint 不同输出目录:

| 任务 | GPU | 进度 | Running Acc | ETA |
|------|-----|------|-------------|-----|
| cls8b_s42_**ckpt1000**_test_mutation | 0 | 5630/9784 (58%) | **82.8%** | ~10 min |
| cls8b_s42_**resume**_ckpt1000_test_mutation | 1 | 5870/9784 (60%) | **83.0%** | ~9 min |

CLS eval 很快（max_new_tokens=8），两个都约 10 分钟内完成。

### 4. 其他

- 无额外 python/train/eval 进程
- 后台有 auto_backup_checkpoints.sh 在运行
- tmux 查不了（read_only 限制），但 ps 显示有一个 `eval_cwm_seed123` 的 tmux session（已结束的旧任务壳）

---
