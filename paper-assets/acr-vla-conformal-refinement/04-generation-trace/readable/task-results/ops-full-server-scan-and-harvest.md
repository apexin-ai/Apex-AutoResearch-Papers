# ops full server scan and harvest

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_full-server-scan-and-harvest_20260516T111045_result.json`
- **Structured JSON:** [`09d150b89a71f198a3b3.json`](../../sessions/09/09d150b89a71f198a3b3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 全服务器状态扫描报告

### bjb1-18228 (4 GPU 活跃, 0 空闲)
| 实验 | GPU | 进度 | 启动时间 |
|------|-----|------|---------|
| **eval-obs-only-object-norm02-seed44-r2 (P0)** | cuda:2 | **7/10 tasks** (butter 完成) | 09:32 |
| **eval-argmin-object-seed44-r2 (P0)** | cuda:3 | **6/10 tasks** (在 butter) | 09:32 |
| eval-perdof-object-seed44 | cuda:1 | 4/10 tasks | 12:57 |
| eval-obs-only-object-norm01-seed45 | cuda:0 | 0/10 (task1 进行中) | 17:03 |

**P0 预计 ~2-4h 完成。**

### bjb1-32546 (6 GPU 活跃, 0 空闲)
| 实验 | GPU | 进度 |
|------|-----|------|
| eval-scalar-object-seed44-r2 | cuda:0 | 2/10 |
| eval-vla-mean-object-seed44 | cuda:1 | 4/10 |
| eval-obs-only-object-norm03-seed44 | cuda:2 | 3/10 |
| eval-obs-only-object-norm02-seed45 | cuda:3 | 2/10 |
| eval-obs-only-object-norm01-seed44 | cuda:4 | 3/10 |
| eval-obs-only-object-default-seed44 | cuda:5 | 2/10 |

### bjb2-28827 (6 GPU 活跃, 0 空闲)
| 实验 | GPU | 进度 | 问题 |
|------|-----|------|------|
| eval-scalar-object-seed45 | cuda:0 | 0/10 (task1 rollout 15/20) | **20 rollouts!** |
| eval-perdof-object-norm02-seed45 | cuda:1 | 0/10 (task1 rollout 15/20) | **20 rollouts!** |
| obs-only-norm03-seed45 | cuda:2 | 0/10 (刚启动) | **未注册 registry** |
| obs-only-default-seed45 | cuda:3 | 0/10 (刚启动) | **未注册 registry** |
| eval-vla-only-object-seed45 | cuda:4 | ~6/10 (on butter) | **20 rollouts!** |
| eval-argmin-object-seed45 | cuda:5 | 2/10 | 正常 10 rollouts |

### bjb2-40593 (1 GPU 活跃, 5 空闲)
| 实验 | GPU | 进度 |
|------|-----|------|
| eval-perdof-object-default-seed44 | cuda:0 | 1/10 |
| **空闲** | cuda:1-5 | - |

---

### 关键发现

1. **P0 未完成** — obs-only-norm02-seed44-r2 完成 7/10, argmin-seed44-r2 完成 6/10, 预计 2-4h 后可回收

2. **无已完成未回收的 RUNNING 实验** — 全部 15 个 RUNNING registry 条目的进程都在运行

3. **bjb2-28827 有 3 个实验用了 20 rollouts**（scalar-seed45, perdof-norm02-seed45, vla-only-seed45）— 缺少 `--n_rollouts 10` 参数，使用了默认值 20，会花 2x 时间并且和其他实验的 100 rollouts 不可比

4. **bjb2-28827 有 2 个实验未注册 registry**（obs-only-norm03-seed45 cuda:2, obs-only-default-seed45 cuda:3）

5. **bjb2-40593 有 5 个空闲 GPU** (cuda:1-5)

### 3-seed Fisher test 状态
| seed | obs-only-norm02 | argmin |
|------|----------------|--------|
| 42 | 22% ✅ | 12% ✅ |
| 43 | 16% ✅ | 17% ✅ |
| 44 | **7/10 运行中** | **6/10 运行中** |

→ **还不能做 3-seed Fisher test，等 seed44 对完成（~2-4h）。**

---
