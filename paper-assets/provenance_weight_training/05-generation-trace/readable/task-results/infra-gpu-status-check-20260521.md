# infra gpu status check 20260521

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_gpu_status_check_20260521_20260520T091419_result.json`
- **Structured JSON:** [`ab5ecfa68fbd4d7f47e3.json`](../../sessions/ab/ab5ecfa68fbd4d7f47e3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## westd-41312 状态汇总

### GPU 利用率

| GPU | 型号 | 利用率 | 显存占用 | 任务 |
|-----|------|--------|----------|------|
| cuda:0 | RTX PRO 6000 Blackwell (96GB) | **100%** | 61.7 / 95.6 GB | uniform_1_7b_seed42_v5 训练 |
| cuda:1 | RTX PRO 6000 Blackwell (96GB) | **88%** | 61.7 / 95.6 GB | adaptive_1_7b_seed42_v5 训练 |
| cuda:2 | RTX PRO 6000 Blackwell (96GB) | **0%** | 1.8 / 95.6 GB | lm-eval: contamination_60_adaptive_seed456 downstream eval（运行 1h14m） |
| cuda:3 | RTX PRO 6000 Blackwell (96GB) | **0%** | 0 / 95.6 GB | **空闲** |

### 1.7B v5 训练进度

| 实验 | PID | 当前 Step | 总 Step | 进度 | 速度 | 预计剩余 | 运行时间 |
|------|-----|-----------|---------|------|------|----------|----------|
| uniform_1_7b_seed42_v5 | 453123 | **449** / 6103 | 7.4% | 2.87 s/it | ~4h30m | 21h53m |
| adaptive_1_7b_seed42_v5 | 453200 | **427** / 6103 | 7.0% | 3.03 s/it | ~4h47m | 21h52m |

两个进程均存活，运行约 21-22 小时。

### cuda:2 进程

PID 457400 — `lm_eval` 在跑 contamination_60_**adaptive**_seed456 的 downstream 评测（arc_easy, arc_challenge, hellaswag, piqa, winogrande），已运行 1h14m。显存占用低（1.8GB），GPU 利用率 0%（可能在加载数据或等待 I/O）。

### contamination_60_uniform_seed456 checkpoint

**存在**，路径 `/root/autodl-tmp/provenance_weight_training/output/models/contamination_60_uniform_seed456/`，包含：
- `config.json`（May 18）
- `eval_results.json`（May 18）
- `final/` 目录（May 18）
- `step_metrics.jsonl`（~5MB）

### 磁盘

| 挂载点 | 总容量 | 已用 | 可用 | 使用率 |
|--------|--------|------|------|--------|
| /root/autodl-tmp | 250 GB | 75 GB | **176 GB** | 30% |

磁盘充裕。

---
