# analyze eval openvla attn k085 long seed42 v5

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_eval_openvla_attn_k085_long_seed42_v5_20260526T231340_result.json`
- **Structured JSON:** [`1adfa9cad8cae9e3fc1f.json`](../../sessions/1a/1adfa9cad8cae9e3fc1f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个实验均已完成，registry 已更新为 DONE。

---

### 实验 1: eval_openvla_attn_k085_long_seed42_v5

**Overall SR: 45.8%** (229/500) — 确认了之前 k=0.85=45.8% 的数据点，非 noise。

Per-task SR (%): 60, 58, 56, 34, 38, 66, 34, 66, 24, 22

**Long suite Attention cliff curve 更新**:
| k | SR | tokens kept |
|---|---|---|
| 0.90 | 44.0% | 230 |
| **0.85** | **45.8%** | **217** |
| 0.70 | 24.0% | 179 |
| 0.50 | running | 128 |

k=0.85 和 k=0.9 之间差异极小（+1.8pp），说明 Attention pruning 在 Long suite 上 k=0.85~0.9 区间处于平台期，cliff 在 k=0.7 以下。

---

### 实验 2: eval_openvla_l2norm_k075_goal_seed42_v2

**Overall SR: 70.2%** (351/500)

Per-task SR (%): 54, 80, 86, 22, 88, 70, 68, 98, 82, 54

**Goal suite L2norm cliff curve 更新**:
| k | SR | tokens kept |
|---|---|---|
| 0.90 | 74.8% | 230 |
| 0.85 | 75.4% | 217 |
| **0.75** | **70.2%** | **192** |
| 0.70 | 68.4% | 179 |
| 0.50 | 43.4% | 128 |

k=0.75 填补了 k=0.85→k=0.7 的斜率：75.4% → 70.2% → 68.4%，下降是渐进的（~2.5pp per 0.05 step），没有 cliff。L2norm 在 Goal suite 上退化非常 graceful，真正的 cliff 在 k=0.5 附近（68.4% → 43.4%）。

---
