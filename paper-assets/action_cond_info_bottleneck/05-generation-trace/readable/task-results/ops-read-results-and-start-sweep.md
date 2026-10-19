# ops read results and start sweep

**action cond info bottleneck** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_read-results-and-start-sweep_20260517T003516_result.json`
- **Structured JSON:** [`697fa947bea5f2f43878.json`](../../sessions/69/697fa947bea5f2f43878.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态报告

### 1. Eval 结果（3/4 suites 完成，libero_10 仍在跑）

| Suite | Seed1 (v7_contrastive) | Seed2 (v7_seed2) | Baseline | Δ Seed1 | Δ Seed2 |
|-------|----------------------:|------------------:|---------:|--------:|--------:|
| libero_spatial | 58.4% | 51.4% | 66.0% | -7.6pp | -14.6pp |
| libero_object | 58.6% | 49.4% | 67.8% | -9.2pp | -18.4pp |
| libero_goal | 72.8% | 63.0% | 76.4% | -3.6pp | -13.4pp |
| libero_10 | ⏳ running | ⏳ running | 54.2% | — | — |
| **AVG (3 suites)** | **63.3%** | **54.6%** | **70.1%** | **-6.8pp** | **-15.5pp** |

### 2. GPU 状态：**未空闲**

两个 eval 进程仍在运行（状态 `Rl+`，已运行 ~7h）：
- GPU 0: PID 104743 (seed1 eval, 6331 MiB)
- GPU 1: PID 111920 (seed2 eval, 6678 MiB)

正在跑最后一个 suite `libero_10`（500 episodes），估计还需 1-2h。

### 3. Alpha sweep：**无法启动**

根据约束 C003，两个 GPU 都有活跃 eval 进程，禁止在其上启动新任务。需等 libero_10 完成后再启动。

### 初步观察

结果全面低于 baseline，seed2 尤其严重（-15.5pp avg）。v7_contrastive 的 ACIB 机制目前在 inference 阶段反而降低了性能。这使得 alpha sweep（特别是 alpha=0.0 pass-through）更加关键，可以诊断是否是 conditioning 本身引入的退化。

---
