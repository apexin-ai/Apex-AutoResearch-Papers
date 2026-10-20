# monitor all gpu status check

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_all-gpu-status-check_20260515T181824_result.json`
- **Structured JSON:** [`1eb759a5a3b3a3ee9952.json`](../../sessions/1e/1eb759a5a3b3a3ee9952.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## GPU 状态汇总 (2026-05-16 02:18 UTC)

| GPU | VRAM | GPU% | 任务 | PID | 状态 | 进度 | 关键指标 |
|-----|------|------|------|-----|------|------|----------|
| **cuda:0** | 18.5/32.6 GB | 99% | val-sweep-seq8192-v2 (CLS eval) | 402135 | **运行中** | ckpt-2000, 3600/9335 samples (38.6%) | running_acc=**87.2%** |
| **cuda:1** | 27.3/32.6 GB | 90% | cls-8b-s42-resume 训练 | 295794 | **即将完成** | step 6600/6633 (99.5%), epoch 2.99 | loss=0.137, eval_loss=0.477 |
| **cuda:2** | 21.0/32.6 GB | 97% | cwm-8b-v5 resume 训练 | 400280 | **运行中** | 307/9335 samples (3.3%), 从 ckpt-5200 恢复 | ~7-8 it/s |
| **cuda:3** | 22.5/32.6 GB | 85% | cwm8b-ckpt400-test-eval | 381618 | **运行中** | 2240/9784 samples (22.9%) | running_acc=**64.3%**, ~8 samples/57s |

### 各任务详情

**cuda:0 — val-sweep-seq8192-v2**: 当前正在评估 checkpoint-2000（从 ps 看到的 checkpoint_dir）。3600/9335 val samples，速率 ~5.4 samples/sec，本 checkpoint 还需 ~18 min。之后还有大量 checkpoint 待 sweep（可用 ckpt: 800–6400，间隔 200）。

**cuda:1 — cls-8b-s42-resume 训练**: 几乎跑完。6600/6633 steps，epoch 2.99。最新 loss=0.137，最近一次 eval_loss=0.477 (epoch 2.89)。最新 checkpoint: **checkpoint-6400** (01:48 保存)。剩余 33 steps ≈ **~4 min** 完成。

**cuda:2 — cwm-8b-v5 resume**: 从 checkpoint-5200 恢复，刚启动 ~27 min (01:51 启动)。307/9335 samples，tqdm ETA ~18 min 完当前 epoch pass。剩余步数 ~1400+ steps (至 6633)，按当前速率估算总 ETA **~2 小时**。

**cuda:3 — cwm8b-ckpt400-test-eval**: 2240/9784 test samples (22.9%)，acc=64.3%。速率 ~8 samples/57sec。剩余 7544 samples，ETA **~15 小时**。

---
