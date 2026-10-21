# diagnose bjb1 18228 norm seed65 fill

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_bjb1-18228-norm-seed65-fill_20260521T025446_result.json`
- **Structured JSON:** [`d6b809c651a464915eab.json`](../../sessions/d6/d6b809c651a464915eab.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部信息已收集。cuda:1 已被占用。

---

## 汇总报告

### 任务 1: seed65 诊断 — Cron False Positive ✅

实验正常完成，被 cron 误判。
- **Overall SR = 14.0% (14/100)**
- 输出 JSON 存在: `eval_obs_only_object_norm005_seed65.json` (1490 bytes)
- Registry 已更新: conclusion=success, metrics 已写入

### 任务 2: seed66 系列 — 全部正常运行中 ✅

三个进程都存活，运行约 1h25m，当前在 task 4/10 (bbq_sauce)，约 35-40% 进度：

| 实验 | PID | GPU | 当前任务进度 |
|------|-----|-----|-------------|
| norm003-seed66 | 642428 | cuda:0 | bbq_sauce 15/20 |
| norm005-seed66 | 642506 | cuda:2 | bbq_sauce 20/20 完成 |
| norm01-seed66 | 642775 | cuda:3 | bbq_sauce 20/20 完成 |

### 任务 3: 填补 cuda:1 — 无需操作

**cuda:1 已被占用。** PID 666593 正在运行 `eval-obs-only-object-norm01-seed67`（已跑 14 分钟）。这是 seed65 完成后被其他 Worker 填入的。

另外 `eval-obs-only-object-norm005-seed67` 已经在 bjb1-32546:cuda:2 上运行，不可重复提交。

**bjb1-18228 当前 4 个 GPU 全部占满，无空闲 GPU 可填。**

---
