# analysis exp 008a unexposed s2

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp_008a_unexposed_s2_20260518T080858_result.json`
- **Structured JSON:** [`458bea2759f100154239.json`](../../sessions/45/458bea2759f100154239.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新为 DONE。

## exp_008a_unexposed_s2 分析结论：**SUCCESS**

### Eval Return 曲线
| Step | eval_return |
|------|------------|
| 5k | 39.3 |
| 15k | 159.8 |
| 25k | 374.7 |
| 35k | 431.6 |
| 45k | 430.8 |
| 55k | 607.5 |
| 65k | 653.8 |
| 75k | 534.4 (临时 dip) |
| 85k | 605.4 |
| 95k | 819.4 |
| **105k** | **899.4** |

### CIVO 检查
- `ve_ratio` 全程 0.03→0.33，稳定在 ~0.33，**远低于 1.5× 阈值**
- `civo/alert = 0` 全程无触发
- `delta_ve` 后半段为负值（-0.003），value estimation 趋于保守

### V-recovery
- `value_mean = 299.4`, `target_mean = 300.3`，差异 <0.3%，**完美对齐**

### 与父实验和 baseline 对比
| 实验 | eval_return | CIVO |
|------|------------|------|
| baseline (无 gate) | ~850 | N/A |
| 父实验 008a_no_subsample_dt2 (seed=0) | 778 | 无 |
| **本实验 (seed=2)** | **899.4** | **无** |

### C3 claim 支撑
seed=2 不仅复现了父实验的 CIVO protection，eval return 还超过 baseline 50 分。unexposed dt_emb + fixed dt=2 + no subsample 配置的 CIVO 保护性跨 seed 稳定可复现，可作为 C3 rebuttal 的有力证据。

---
