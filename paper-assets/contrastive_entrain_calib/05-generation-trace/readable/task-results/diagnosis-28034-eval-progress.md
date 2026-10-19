# diagnosis 28034 eval progress

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnosis_28034-eval-progress_20260521T073540_result.json`
- **Structured JSON:** [`f3bb32a215cc750219e9.json`](../../sessions/f3/f3bb32a215cc750219e9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Eval 状态汇总

| Exp ID | PID | 状态 | 进度 | 预计剩余 |
|--------|-----|------|------|---------|
| exp003-ckpt5000-v2 | 497834 | **RUNNING** | 40/362 (11%) | ~72 min |
| exp003-ckpt6000 | 498446 | **RUNNING** | 40/362 (11%) | ~72 min |
| exp003-ckpt6500 | 498584 | **RUNNING** | 40/362 (11%) | ~72 min |
| exp003-ckpt7000-v2 | 500589 | **RUNNING** | 0/362 (刚开始推理) | ~85 min |

**速率**: ~20 samples / 5 min（前三个 checkpoint 一致）。

**ckpt7000-v2 注意**: GPU 3 显存占用 29781/32607 MiB（91%），日志有 accelerate 内存不足警告（`no modules could be assigned to device 0 due to insufficient memory`），但进程已通过模型加载阶段并开始 eval。需关注是否会 OOM。

## GPU 快照

| GPU | 利用率 | 显存 |
|-----|--------|------|
| 0 (ckpt5000-v2) | 35% | 16884 / 32607 MiB |
| 1 (ckpt6000) | 38% | 16864 / 32607 MiB |
| 2 (ckpt6500) | 36% | 16864 / 32607 MiB |
| 3 (ckpt7000-v2) | 36% | 29781 / 32607 MiB |

## 已有结果（results 目录）

ckpt1000, 2000, 3000, 4000, 4500, 5500 已完成，当前跑的 4 个 checkpoint 尚无结果文件产出。

---
