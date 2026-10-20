# check frontier sc progress

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_frontier_sc_progress_20260521T065741_result.json`
- **Structured JSON:** [`b029be600daf37620555.json`](../../sessions/b0/b029be600daf37620555.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Frontier SC 实验进度汇总

| 实验 | 服务器 | 进程 | 进度 | 速率 | 预计完成 |
|------|--------|------|------|------|---------|
| **GPT-5.5** | 5090-c | **已完成** | **200/200** ✅ | ~31s/inst | 已完成 (6126s) |
| **Claude Sonnet 4** | 5090 | PID 6302 alive | **132/200** (66%) | ~17s/inst | ~15:18 CST (~19min) |
| **DeepSeek Chat** | 5090-c | alive | **23/200** (11.5%) | ~21s/inst | ~16:00 CST (~1h) |
| **Gemini 2.5 Pro** | 5090-c | alive | **11/200** (5.5%) | ~43s/inst | ~17:14 CST (~2h15m) |

### GPT-5.5 最终结果
- greedy_f1 = **0.6382**, mv_f1 = **0.6521** (Δ=+1.4%), oracle_f1 = **0.7203**
- degeneracy_rate = **50%** (100/200)
- Agreement rho = 0.3551, FK rho = 0.3515, SJ rho = 0.3461
- Parse fails: 161 (10.1% of 1600 API calls)
- F1_sc_hurts: 5.5%, F2_sc_helps: 3.0%

### 5090-c GPU 状态
全部 4 块 RTX 5090 空闲（0MiB），**cuda:1 已释放**。这些是纯 API 实验，不占 GPU。

---
