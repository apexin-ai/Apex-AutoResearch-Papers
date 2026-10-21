# ops deploy argmin and audit 40593

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_deploy-argmin-and-audit-40593_20260519T114219_result.json`
- **Structured JSON:** [`809443acb94f62fb5500.json`](../../sessions/80/809443acb94f62fb5500.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 更新完成。汇总全部信息。

---

## 汇报

### 1. bjb1-32546 argmin K=5 部署状态

**实际部署**：seed42/43/45 在 GPUs 0/2/5（非 Director 要求的 seed42/43/44）

| Seed | Server | GPU | 状态 | 进度 |
|------|--------|-----|------|------|
| 42 | bjb1-32546 | 0 | RUNNING | task 1/10, 刚启动 ~30min |
| 42 | bjb2-28827 | 4 | RUNNING | task 10/10 (orange_juice), 接近完成 (**重复**) |
| 43 | bjb1-32546 | 2 | RUNNING | task 1/10, 刚启动 ~30min |
| 44 | **bjb2-28827** | 1 | RUNNING | task 4/10 (bbq_sauce) |
| 45 | bjb1-32546 | 5 | RUNNING | task 1/10, 刚启动 ~30min |

- seed44 部署在 bjb2-28827 而非 bjb1-32546，且**未注册到 registry**
- seed42 有重复部署（bjb1-32546 + bjb2-28827）
- bjb1-32546 GPU 3 空闲

### 2. bjb2-40593 三个实验状态

| 实验 | 状态 | 结果 |
|------|------|------|
| eval-scalar-object-seed45-r2 | **DONE** (negative) | overall 7% — 与 scalar 历史一致 (mean ~8.5%) |
| eval-random-selection-object-seed46-r2 | RUNNING | task 4/10, 仍在跑 |
| eval-obs-only-spatial-norm02-seed43 | RUNNING | 顺序执行 seed43→44→45，seed43 接近尾声 |

scalar_seed45_r2 已更新 registry → DONE (negative), metrics 已录入。

### 3. 完整 GPU 分配表

```
Server: bjb1-32546 (6 GPUs)
GPU 0: eval-argmin-object-k5-seed42 (reconvla K=5)  | 26% | 5651/24564 MiB
GPU 1: eval-spatial-obs-only-norm02-seed45 (CRM obs_only Spatial ε=0.2) | 19% | 2007/24564 MiB
GPU 2: eval-argmin-object-k5-seed43 (reconvla K=5)  | 21% | 5651/24564 MiB
GPU 3: *** IDLE ***                                   |  0% |    2/24564 MiB
GPU 4: eval-perdof-norm005-seed45 + eval-obs-only-default-seed48 (共享!) | 99% | 4818/24564 MiB
GPU 5: eval-argmin-object-k5-seed45 (reconvla K=5)  | 24% | 5651/24564 MiB

Server: bjb2-40593 (1 GPU)
GPU 0: eval-random-selection-seed46-r2 + eval-spatial-obs-only-norm02-seq (共享) | 98% | 7286/24564 MiB
       (eval-scalar-seed45-r2 已完成)

Server: bjb1-18228 (4 GPUs)
GPU 0: eval-obs-only-object-norm005-seed48    | 23% | 3804/24564 MiB
GPU 1: *** IDLE *** (旧 session norm003-seed43 已死) |  0% |    1/24564 MiB
GPU 2: eval-perdof-object-norm005-seed47      | 23% | 3804/24564 MiB
GPU 3: eval-perdof-object-norm003-seed47      | 23% | 3804/24564 MiB

Server: bjb2-28827 (6 GPUs)
GPU 0: eval-random-seed46-t16                 | 15% | 1942/24564 MiB
GPU 1: eval-argmin-object-k5-seed44 (reconvla K=5)  | 17% | 4233/24564 MiB
GPU 2: eval-perdof-norm03-seed43              | 99% | 4777/24564 MiB
GPU 3: eval-spatial-obs-only-norm02-seed44    | 18% | 2006/24564 MiB
GPU 4: eval-argmin-object-k5-seed42 (重复) + eval-obs-only-norm003-seed44 | 18% | 1906/24564 MiB
GPU 5: eval-perdof-norm005-seed45             | 18% | 1942/24564 MiB
```

### 4. 空闲 GPU

**2 个空闲 GPU**：
- bjb1-32546 GPU 3
- bjb1-18228 GPU 1

### 需要决策

1. **seed44 不在 bjb1-32546**，而在 bjb2-28827 GPU 1 已经跑到 task 4/10。是否需要在 bjb1-32546 GPU 3 再部署一份？
2. **seed42 重复运行**：bjb2-28827 的 seed42 接近完成（task 10/10），bjb1-32546 的刚开始。完成后是否要 kill 其中一份？
3. bjb1-18228 GPU 1 的旧 tmux session `eval-obs-only-object-norm003-seed43` 已死，需要清理或重部署。

---
