# ops comprehensive status check

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_comprehensive-status-check_20260514T065702_result.json`
- **Structured JSON:** [`f9236e61d21527aa87a2.json`](../../sessions/f9/f9236e61d21527aa87a2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 实验状态汇报

### GPU 状态
| GPU | 利用率 | 显存 | 状态 |
|-----|--------|------|------|
| 0 | 99% | 46.5/97.9 GB | 忙 |
| 1 | 99% | 46.5/97.9 GB | 忙 |
| 2 | 99% | 46.5/97.9 GB | 忙 |
| 3 | 68% | 46.5/97.9 GB | 忙 |

**无空闲 GPU。**

---

### 1. adaptive_seed42/123/456 — 全部 DONE ✓

| 实验 | train_loss | steps | runtime | 完成时间 (CST) | checkpoint |
|------|-----------|-------|---------|---------------|------------|
| adaptive_seed42 | **9.2665** | 6103 | 3h 38m 35s | 14:25:09 | `output/models/adaptive_seed42/final` |
| adaptive_seed123 | **9.2665** | 6103 | 3h 39m 57s | 14:26:34 | `output/models/adaptive_seed123/final` |
| adaptive_seed456 | **9.2354** | 6103 | 3h 38m 50s | 14:25:27 | `output/models/adaptive_seed456/final` |

三个 seed 的 loss 非常一致（seed456 略低）。每个还有 checkpoint-6000 和 checkpoint-6103。EXIT_CODE=0。

---

### 2. grid_b_seed42_batch (cuda:0) — RUNNING

串行 6 个 b 值，当前进度：

| b 值 | 状态 | train_loss | 时间 |
|------|------|-----------|------|
| 0.5 | **DONE** | 9.5979 | 07:50→11:27 (3h 37m) |
| 1.0 | **RUNNING** 97% (5928/6103) | — | 11:27→ ~ETA 6min |
| 1.5 | 等待中 | — | — |
| 2.0 | 等待中 | — | — |
| 3.0 | 等待中 | — | — |
| 5.0 | 等待中 | — | — |

b=1.0 即将完成（~6min）。之后还剩 4 个 b 值，每个 ~3.5h，串行共需 **~14h**。

---

### 3. grid_b round 1 seed123 (cuda:1/2/3) — RUNNING

均刚启动不久（~提交后 3-4 分钟的进度）：

| 实验 | GPU | 进度 | 当前 loss | ETA |
|------|-----|------|----------|-----|
| grid_b0_5_seed123 | cuda:1 | 107/6103 (2%) | 10.13 (step 100) | ~3.5h |
| grid_b1_0_seed123 | cuda:2 | 105/6103 (2%) | 10.77 (step 100) | ~3.5h |
| grid_b1_5_seed123 | cuda:3 | 105/6103 (2%) | 11.07 (step 100) | ~3.5h |

三个并行跑，预计 **~3.5h 后完成**（约 CST 18:30）。

---
