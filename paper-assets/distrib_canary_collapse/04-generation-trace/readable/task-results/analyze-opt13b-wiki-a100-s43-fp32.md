# analyze opt13b wiki a100 s43 fp32

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_opt13b_wiki_a100_s43_fp32_20260520T001430_result.json`
- **Structured JSON:** [`57a2c8235b7704adbf7d.json`](../../sessions/57/57a2c8235b7704adbf7d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。

## 结果汇总

| 指标 | s43 | s42 (对照) |
|------|-----|-----------|
| PermG fwd (BH FDR) | **6/8** | 6/8 |
| K≥3 (3σ) | **6/8** | 6/8 |
| K≥4 (3σ) | **4/8** | 2/8 |
| D111 direction | **8/8 PASS** | — |

**结论：success。** 跨 seed 复现完全一致——相同 6 对 (entropy/ECE × d1/d2/d3) 显著，相同 2 对 (mauve) 不显著。K≥4 比 s42 更强（4/8 vs 2/8），因 s43 中 ECE pairs 的 TY d_max=0 提供了更多自由度。方向检查全部通过（canary leads downstream，PermG fwd p << rev p）。

Registry 已更新为 DONE/success，报告和分析 JSON 已保存。

---
