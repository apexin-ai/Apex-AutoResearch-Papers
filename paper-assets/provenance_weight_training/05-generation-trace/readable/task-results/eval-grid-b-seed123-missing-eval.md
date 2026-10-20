# eval grid b seed123 missing eval

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_grid_b_seed123_missing_eval_20260514T143340_result.json`
- **Structured JSON:** [`4cf727793c572a6268e9.json`](../../sessions/4c/4cf727793c572a6268e9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。两个实验的 eval 已补跑，registry 已更新。

**结果汇总（seed123 系列）：**

| b 值 | eval_ppl_holdout | eval_loss | tokens |
|------|------------------|-----------|--------|
| 0.5 | 17.638 | - | ~4,077k |
| 1.0 | 17.674 | - | ~4,077k |
| 1.5 | 17.701 | - | ~4,077k |
| **2.0** | **17.725** | **2.875** | **4,077,068** |
| **3.0** | **17.760** | **2.877** | **4,077,068** |

趋势一致：b 越大 PPL 越高，b=0.5 最优。

---
