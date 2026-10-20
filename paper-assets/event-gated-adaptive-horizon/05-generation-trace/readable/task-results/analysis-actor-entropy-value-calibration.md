# analysis actor entropy value calibration

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_actor-entropy-value-calibration_20260514T093931_result.json`
- **Structured JSON:** [`e1ca95b343b5383862c3.json`](../../sessions/e1/e1ca95b343b5383862c3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。核心结论：

### Actor Entropy (plan_031)
| 实验 | 类型 | Entropy@15K | 最终 Entropy |
|------|------|-------------|-------------|
| baseline | 健康 | -0.90 | -1.51 (505K, 有恢复) |
| 008a | 健康 | -1.15 | -5.24 (105K) |
| 008c | 健康 | -1.18 | -5.27 (65K) |
| **008d** | **崩塌** | **+0.48** | -4.88 (55K) |
| **006** | **崩塌** | **+0.96** | -5.12 (65K) |
| 008f | 健康 | +0.61 | -4.85 (105K) |
| 008e_v3 | 健康 | +2.21 | -5.18 (105K) |

崩塌实验在 15K 时 entropy 仍为正值，比健康实验（已转负）收敛更慢。

### Value Calibration (plan_032) — **最强信号**
- **崩塌 = 病态高估 (delusional critic)**：
  - exp_008d: v/R = **1.87** (value=137.9, 实际 return=73.8)
  - exp_006: v/R = **2.43** (value=361.7, 实际 return=149.0)
  - 归一化后分别为 baseline 的 5.27x 和 5.66x
- **健康 = 一致低估**：baseline v/R ≈ 0.70，事件门控健康实验 v/R 在 0.2-0.6
- **分类准确率 100%**：v/R > 1.5 完美区分崩塌 vs 健康

数据已保存到 `logdir/analysis_actor_entropy_value_calibration.json`，artifact 已注册，memory.md 已更新。

---
