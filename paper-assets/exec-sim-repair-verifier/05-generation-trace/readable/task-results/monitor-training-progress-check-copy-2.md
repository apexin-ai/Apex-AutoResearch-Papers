# monitor training progress check

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_training-progress-check_20260515T020900_result.json`
- **Structured JSON:** [`1e839422505935c6a46a.json`](../../sessions/1e/1e839422505935c6a46a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇总如下：

## 训练进度汇总

| 实验 | GPU | Step | 进度 | 速度 | 最新 Eval Loss | 预计剩余 |
|------|-----|------|------|------|---------------|---------|
| **seed123-conda-v3** | cuda:3 | 5415/6633 | 82% | ~8.5s/step | 0.349 (step 5400) | **~3h** |
| **cwm-8b-conda-v2** | cuda:2 | 2900/6633 | 44% | ~12s/step | 0.448 (step 2900) | ~13h |
| **cls-8b-s42-resume** | cuda:1 | 1864/6633 | 28% | ~8s/step | 0.276 (step 1800) | ~10.5h |

## GPU 状态

| GPU | 利用率 | 显存 | 任务 |
|-----|--------|------|------|
| cuda:0 | 78% | 19.2/32 GB | eval_repo_cls.py (checkpoint-1200, val split) |
| cuda:1 | 60% | 27.3/32 GB | s42-resume 训练 |
| cuda:2 | 97% | 30.7/32 GB | cwm-8b 训练（当前在 eval 中） |
| cuda:3 | 99% | 30.9/32 GB | seed123 训练 |

## 关键信息

- **seed123 距完成还剩 ~1218 步 / ~3 小时**，刚完成 step 5400 的 checkpoint 保存和 eval
- **cwm-8b** 日志名是 `repo-level-cwm-8b-conda-v2.log`（不是 v4，v3/v4 启动失败）
- **s42-resume** checkpoints 已保存: 800, 1000, 1200, 1400, 1600, 1800
- **cuda:0** 上额外跑着 s42-resume ckpt-1200 的 val eval（PID 316307）

---
