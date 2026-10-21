# ops gpu patrol deploy urgent

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gpu-patrol-deploy-urgent_20260518T102010_result.json`
- **Structured JSON:** [`548092e441c4e8ca336a.json`](../../sessions/54/548092e441c4e8ca336a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

部署完成。汇总报告：

### 服务器状态

| 服务器 | GPU | 内存占用 | 状态 |
|--------|-----|---------|------|
| **bjb2-28827** | 0 | 2839 MiB | BUSY |
| | 1 | 2875 MiB | BUSY |
| | 2 | 2411 MiB | BUSY |
| | 3 | 2875 MiB | BUSY |
| | 4 | 3306 MiB | BUSY |
| | 5 | 2410 MiB | BUSY |
| **bjb1-32546** | 0 | 2876 MiB | BUSY |
| | 1 | 2411 MiB | BUSY |
| | 2 | 1942 MiB | BUSY |
| | 3 | 2411 MiB | BUSY |
| | 4 | 1943 MiB | BUSY |
| | 5 | 2876 MiB | BUSY |
| **bjb1-18228** | 0 | 3341 MiB | BUSY |
| | 1 | 1941 MiB | BUSY |
| | 2 | 2410 MiB | BUSY |
| | 3 | 1 MiB | **IDLE → 已部署** |
| **bjb2-40593** | 0 | 1869 MiB | BUSY (random_selection seed42) |

**总计：17 GPU 中 16 BUSY，1 IDLE（已部署）**

### RUNNING 实验确认

| 实验 | PID | 服务器/GPU | 启动时间 | 状态 |
|------|-----|-----------|---------|------|
| eval-obs-only-object-norm02-k5-seed43 | 527474 | bjb2-28827/GPU2 | 12:37 | ✅ ALIVE |
| eval-perdof-object-norm01-seed42-r2 | 497642 | bjb2-28827/GPU3 | 07:52 | ✅ ALIVE |
| eval-obs-only-object-norm01-seed42-r2 | 497445 | bjb2-28827/GPU1 | 07:52 | ✅ ALIVE |

### 已完成实验
无。所有实验仍在运行。

### 新部署

| 实验 | 服务器/GPU | 优先级 |
|------|-----------|--------|
| **eval-perdof-object-default-seed43** | bjb1-18228/GPU3 | P1 — perdof uncapped collapse seed43 确认 |

### 剩余队列

| 优先级 | 实验 | 备注 |
|--------|------|------|
| P2 | eval-perdof-object-default-seed45 | 等待空闲 GPU |
| P3 | eval-random-selection-object-seed44 | **已在 bjb2-28827 运行中**（tmux session 10:25 启动） |
| P4 | eval-obs-only-object-norm02-k5-seed44 | 等待空闲 GPU |

### 额外发现
- **bjb2-40593** 上 random_selection seed42 以 nohup 方式运行（非 tmux），已跑 ~22h，当前进度：chocolate_pudding 任务，SR 20% (2/10)
- **bjb1-32546** 满载 6 个实验（norm005 和 norm01 系列）
- **bjb1-18228** 另外 3 个 GPU 跑 obs_only norm01/norm02/norm03 seed48 系列

---
