# analysis deepseek training progress

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_deepseek-training-progress_20260517T084409_result.json`
- **Structured JSON:** [`71d2a7c16070c3c9ce3b.json`](../../sessions/71/71d2a7c16070c3c9ce3b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All data collected. Here's the summary:

---

## 训练进度汇总 (2026-05-17 16:44 CST)

所有 4 个进程均在正常运行，使用 `train_unified.py`（之前 `train_repo_cls.log` / `train_repo_cwm.log` 中的 crash 是旧脚本 `train_repo_verifier.py` 的残留日志，与当前训练无关）。

### 进程信息

| Exp | GPU | PID | Process Start |
|-----|-----|-----|---------------|
| deepseek-cls-repo-v4 | cuda:0 | 548885 | May 17 02:41 |
| deepseek-cwm-repo | cuda:1 | 479953 | May 16 16:04 |
| deepseek-cls-repo-s123 | cuda:2 | 542514 | May 17 01:27 |
| deepseek-cwm-repo-s123 | cuda:3 | 542906 | May 17 01:30 |

### 训练进度

| Exp | GPU | GPU Util | Last Ckpt | Total Steps | Ckpt Progress | Est. Current Step | Est. Progress | Speed | ETA |
|-----|-----|----------|-----------|-------------|---------------|-------------------|---------------|-------|-----|
| deepseek-cls-repo-v4 | cuda:0 | 96% | 2211 (ep1) | 6633 | 33.3% | ~4400 | ~66% | ~5.4 steps/min | ~7.2h |
| deepseek-cwm-repo | cuda:1 | 99% | 8844 (ep2) | 13266 | 66.7% | ~10400 | ~78% | ~7.3 steps/min | ~6.8h |
| deepseek-cls-repo-s123 | cuda:2 | 98% | 4422 (ep2) | 6633 | 66.7% | ~4700 | ~71% | ~5.4 steps/min | ~6.2h |
| deepseek-cwm-repo-s123 | cuda:3 | 100% | 4422 (ep1) | 13266 | 33.3% | ~6400 | ~48% | ~7.2 steps/min | ~16.7h |

### 要点

- **Speed** 从 checkpoint 时间间隔推算（cls ~11s/step, cwm ~8.2s/step）
- **ETA** 包含剩余 epoch-end eval 时间（cls eval ~19min, cwm eval ~24min each）
- Checkpoint 只在 epoch 结束时保存（save_steps=500 但 eval + save 实际发生在 epoch boundary）
- **cwm-repo-s123 最慢**，只完成了 1/3，预计还需 ~17h
- **cls-repo-s123 最快完成**，预计 ~6.2h 后结束（约今晚 23:00 CST）
- 4 张 RTX 5090 GPU 利用率均在 96-100%，VRAM 使用 17.6-19.7 GiB / 32.6 GiB

---
