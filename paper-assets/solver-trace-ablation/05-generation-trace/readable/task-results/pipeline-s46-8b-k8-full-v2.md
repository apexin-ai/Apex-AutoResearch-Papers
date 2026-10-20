# pipeline s46 8b k8 full v2

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_pipeline_s46-8b-k8-full-v2_20260522T034053_result.json`
- **Structured JSON:** [`61a3bfe31e0ff0e63c81.json`](../../sessions/61/61a3bfe31e0ff0e63c81.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**全流水线完成。** 8B K=8 s42 训练已确认运行中。

---

## 汇报

### 1. s46 结果
| 指标 | 值 |
|------|-----|
| Prove Rate | 15% (15/100) |
| Mean ISR | 0.084 |
| Proved-only ISR | 0.560 |
| TS (H7) | 1 (6.7%) |
| CE (H1) | 1 (6.7%) |
| PG (H8) | 0 |
| Genuine | 13/15 (86.7%) |
| Conclusion | **negative** — seed-dependent non-convergence confirmed |

### 2. 8B K=8 dry-run
- **成功**，2 步无 OOM
- K=8 保留
- VRAM 峰值：~54 GB / 98 GB（充裕）
- Step time：~15s/step

### 3. 8B s42 训练启动确认
- PID: 969681（python 进程）
- tmux session: `d154-8b-exec-s42-k8`
- GPU: cuda:0, 54046 MiB 占用
- 已在 step 4/500，ETA ~2h
- Registry: `d154-8b-exec-s42-k8` (RUNNING)

---
