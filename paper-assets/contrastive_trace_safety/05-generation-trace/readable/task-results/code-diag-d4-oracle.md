# code diag d4 oracle

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_diag_d4_oracle_20260516T193009_result.json`
- **Structured JSON:** [`24b494f54ff49561649b.json`](../../sessions/24/24b494f54ff49561649b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Done. `diag_d4_oracle_upper_bound` registered as DONE/success.

## 结果

**结论：任务可解，hidden-state 方法有大量空间。**

| K (连续无 safety 步数) | 检测率 | 可提前检测比例 | 平均 lead time (提前检测的 traces) |
|---|---|---|---|
| 1 | 100% | 83.7% | 35.6 steps |
| 3 | 100% | 76.7% | 34.8 steps |
| 5 | 100% | 76.7% | 31.0 steps |
| 8 | 95.3% | 65.1% | 28.8 steps |

关键发现：
- 用 K=5 oracle，**76.7% 的 traces 在 commitment 前就能被检测**，平均提前 31 步
- pre-commitment 区间内最长无 safety streak 平均 14.6 步（中位数 13 步）
- 这意味着 safety labels 在 commitment 前很早就开始消失，hidden-state probe 的理论天花板远高于 5 步 lead time

---
