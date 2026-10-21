# audit westd27271 refresh 20260522T2

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_westd27271_refresh_20260522T2_20260522T203146_result.json`
- **Structured JSON:** [`d9a1753d58d96ab26a04.json`](../../sessions/d9/d9a1753d58d96ab26a04.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 审计报告：westd-27271

### GPU 状态
| GPU | 显存 | 利用率 | 任务 |
|-----|------|--------|------|
| cuda:0 | 4.9/98 GB | 1% | X-VLA Random k=0.9 Goal — **Task 5/10** (push plate, 0% 预期) |
| cuda:1 | 4.4/98 GB | 0% | X-VLA Random k=0.9 Spatial — **Task 6/10** (cookie box, 全 SUCCESS) |

两卡均忙。tmux 链式命令：k=0.95（已完成）→ k=0.9（正在跑）→ k=0.7（自动排队）。

### 预计完成时间
- k=0.9 Goal：~25 min 剩余 → k=0.7 Goal 自动启动 (~60 min)
- k=0.9 Spatial：~20 min 剩余 → k=0.7 Spatial 自动启动 (~60 min)
- **全部完成预计 ~85 min**

### 已收割 X-VLA 结果汇总

**L2norm（从 eval_xvla_pruning_libero.py，同一 eval 管线）：**
| k | Goal | Spatial |
|---|------|---------|
| 1.0 (baseline) | **98.4%** | **93.0%** |
| 0.9 | 70.2% | 78.8% |
| 0.7 | 53.4% | 72.0% |

**Random：**
| k | Goal | Spatial |
|---|------|---------|
| 0.95 | 54.0% | 70.2% |
| 0.9 | RUNNING | RUNNING |
| 0.7 | QUEUED | QUEUED |

**Random k=0.9 中间结果（截至 Task 5-6/10）：**
- Goal 已完成任务：T0=100%, T1=88%, T2=96%, T3=6%, T4=96%, T5=进行中(0%)
- Spatial 已完成任务：T0=100%, T1=64%, T2=100%, T3=100%, T4=82%, T5=6%, T6=进行中(100%)

### Registry 更新
- `eval_xvla_random_k09_goal_seed42` → RUNNING
- `eval_xvla_random_k09_spatial_seed42` → RUNNING
- `eval_xvla_random_k07_goal_seed42` → QUEUED
- `eval_xvla_random_k07_spatial_seed42` → QUEUED
- 所有已完成的 L2norm 和 Random k=0.95 已在 registry 中

### 部署
**无可用 GPU**，两卡链式任务将自动完成 Random k=0.9→k=0.7 的 Goal 和 Spatial。无需人工干预。

### 关键发现
X-VLA 对 random pruning 极其敏感：仅移除 2.5/50 tokens (k=0.95) 即导致 Goal 从 98.4%→54.0%，Spatial 从 93.0%→70.2%。这与 π0.5（256+ tokens，Random k=0.95 ≈ 97.6%）形成鲜明对比，证实了 fewer-tokens-higher-sensitivity 假说。

---
