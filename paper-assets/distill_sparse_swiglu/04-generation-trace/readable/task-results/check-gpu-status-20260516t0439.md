# check gpu status 20260516T0439

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_gpu_status_20260516T0439_20260516T043949_result.json`
- **Structured JSON:** [`3ead4b147d6a07635c95.json`](../../sessions/3e/3ead4b147d6a07635c95.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 双卡状态报告

### GPU 占用

| GPU | PID | 显存 | 利用率 | 进程 |
|-----|-----|------|--------|------|
| cuda:0 | 203707 | 66986 MiB / 97887 MiB | 100% | `benchmark_eval.py --exp_id d030_kl50_uniform` (50% sparsity, uniform allocation) |
| cuda:1 | 205598 | 90714 MiB / 97887 MiB | 100% | `train.py --loss_type bce --output_dir checkpoints/bce_isocompute_v3_s42` |

### D030 进度

- **已完成**: wikitext2, arc_challenge, winogrande (3/5 tasks)
- **进行中**: MMLU — `loglikelihood requests: 6% (3713/58702)`, ~44 it/s，预计还需约 21 分钟
- **待跑**: gsm8k
- PID 203702 (shell wrapper) → 实际 python PID 203707，12:30 启动，运行正常

### BCE v3

已启动，PID 205598 在 cuda:1 上跑 `train.py`（bce_isocompute_v3_s42, 2700 steps, batch_size=4, wandb offline），12:38 启动，已运行约 2 分钟。

### cuda:1 无流氓进程

没有 benchmark_eval 自动 spawn 的问题，`ps aux` 中除 BCE v3 外无其他 benchmark/train 进程。

**结论**: 双卡均被占满。cuda:0 跑 D030 评测（约完成 60%，MMLU 阶段），cuda:1 已被 BCE v3 训练占用，不可用。

---
