# ssh 14b 32b progress check

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_14b-32b-progress-check_20260519T234338_result.json`
- **Structured JSON:** [`e35b069b03b7e77999e9.json`](../../sessions/e3/e35b069b03b7e77999e9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 训练进度汇总

### 14B (autodl-5090-c, PID 56773) — RUNNING

| 指标 | 值 |
|------|-----|
| 进度 | **21,809 / 41,180 (53.0%)** |
| Epoch | 2.65 / 5.0 |
| Loss | 0.0273 (step 21800) |
| 速度 | ~2.15 s/it |
| 剩余 | 19,371 steps × 2.15s ≈ **11h 34m** |
| 更新 ETA | **~2026-05-20 19:20 UTC** |
| GPU | GPU0 95% (25.9G), GPU1 96% (25.8G), GPU2 74% (18.2G), GPU3 89% (18.0G) |

### 32B (autodl-5090, PID 804438) — RUNNING

| 指标 | 值 |
|------|-----|
| 进度 | **15,346 / 41,180 (37.3%)** |
| Epoch | 1.86 / 5.0 |
| Loss | 0.0528 (step 15300) |
| 速度 | ~2.50 s/it |
| 剩余 | 25,834 steps × 2.50s ≈ **17h 56m** |
| 更新 ETA | **~2026-05-21 01:40 UTC** |
| GPU | GPU0-3 均 93-100%, 各 ~30.5G/32.6G |

### 与上次对比

- **14B**: 48.8% → 53.0%，速度稳定，ETA 从 05-20 14:00 推迟到 05-20 19:20 UTC（偏慢约 5h，可能之前估算过于乐观或 checkpoint 保存导致减速）
- **32B**: 34.5% → 37.3%，刚保存了 checkpoint-15000（删除了旧的 checkpoint-12000），ETA 从 05-20 23:40 推迟到 05-21 01:40 UTC（推迟约 2h）
- 两个实验 loss 均在正常下降，GPU 利用率健康

---
