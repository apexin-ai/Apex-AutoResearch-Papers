# monitor check progress

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_check-progress_20260514T145420_result.json`
- **Structured JSON:** [`b873312fd53b912cc757.json`](../../sessions/b8/b873312fd53b912cc757.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 实验进度汇总

### rep44 (PID 30672, cuda:0)
| 项目 | 状态 |
|------|------|
| 进程 | **ALIVE**, 运行 1h19m |
| 当前进度 | **Gen 3/10**, 训练中 step **2246/5000** (45%) |
| 已完成 gen | gen_0 (21:50), gen_1 (22:10), gen_2 (22:35) — 共 3 个 |
| 最新 loss | 0.4297 @ step 2200 |

### rep45 (PID 31425, cuda:1)
| 项目 | 状态 |
|------|------|
| 进程 | **ALIVE**, 运行 1h12m |
| 当前进度 | **Gen 3/10**, 数据生成阶段（尚未开始训练） |
| 已完成 gen | gen_0 (21:57), gen_1 (22:17), gen_2 (22:41) — 共 3 个 |
| 最新 loss | gen_2 完成时 train_loss=0.6236 |

### GPU 利用率
| GPU | 利用率 | 显存 |
|-----|--------|------|
| cuda:0 (rep44) | 85% | 12.5 / 95.6 GB |
| cuda:1 (rep45) | 50% | 14.1 / 95.6 GB |

rep45 GPU 利用率较低因为当前在做推理生成而非训练。

### 剩余时间估算
从目录时间戳看，每个 gen 耗时 20-25 分钟（逐渐增长）。按 ~25 min/gen 稳态估算：
- **rep44**: 还剩 ~6.5 gen → **~2.7h**
- **rep45**: 还剩 ~7 gen → **~2.9h**

对照 rep42/43 的 5.8h 基准，当前两个实验均已运行约 1.3h，预计总耗时 4-5h，**剩余约 3-3.5h**。

---
