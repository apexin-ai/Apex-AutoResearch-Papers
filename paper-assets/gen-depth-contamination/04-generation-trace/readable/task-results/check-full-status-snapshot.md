# check full status snapshot

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_full_status_snapshot_20260516T183356_result.json`
- **Structured JSON:** [`830f43671eede67e333b.json`](../../sessions/83/830f43671eede67e333b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态快照 (2026-05-16)

### 1. GPU 状态

| GPU | 显存占用 | 利用率 | 状态 |
|-----|---------|--------|------|
| 0 | 0 / 24564 MiB | 0% | **空闲** |
| 1 | 0 / 24564 MiB | 0% | **空闲** |
| 2 | 3771 / 24564 MiB | 89% | PID 67287 (exp-025) |
| 3 | 0 / 24564 MiB | 0% | **空闲** |

### 2. exp-025 (pythia-1.4b × arxiv): RUNNING

- **PID**: 67287, 已运行 32min38s
- **当前进度**: Step 3 Depth Chain — **depth 4, batch 71/275 (26%)**
- **已完成**: depth 0 (seed, skipped) → depth 1 ✓ → depth 2 ✓ → depth 3 ✓
- **待完成**: depth 4 剩余 74% → depth 5 全部 → Step 4 特征提取 → Step 5 评分
- **速度**: ~2.14s/batch
- **预估剩余**: depth 4 剩余 ~7min + depth 5 ~10min + 特征/评分 ~5min ≈ **~22min**
- **结果目录**: 空（pipeline 完成后一次性写出）

参数: `pythia-1.4b` + `Qwen2.5-1.5B` scorer, continuation mode, top_p=0.95, T=1.0, 2200 samples, max_depth=5

### 3. exp-022 (cross_scorer): 不存在

结果目录 `results/exp_022_cross_scorer/` 不存在。该实验未在此服务器上运行过，或结果已被清理。

### 4. 可用 GPU

**GPU 0, 1, 3 空闲**，可立即分配新任务。

---
