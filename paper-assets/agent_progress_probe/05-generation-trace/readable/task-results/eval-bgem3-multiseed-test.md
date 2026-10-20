# eval bgem3 multiseed test

**Are Stagnation Signals Structural? A Systematic Empirical Study of Progress Detection in LLM Agents via Weak Supervision LLM-based agents deployed on software001** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_bgem3-multiseed-test_20260514T221221_result.json`
- **Structured JSON:** [`7eaabfde12c90b4f7b11.json`](../../sessions/7e/7eaabfde12c90b4f7b11.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。汇总结果：

| Seed | test_macro_f1 | test_f1_stag | test_f1_prog | test_size |
|------|-------------|------------|------------|-----------|
| 42   | **0.9413**  | 0.9147     | 0.9679     | 1824      |
| 123  | **0.8474**  | 0.8173     | 0.8775     | 2216      |
| 456  | **0.9364**  | 0.9183     | 0.9545     | 2343      |

**Mean ± Std (3 seeds)**:
- macro_f1: **0.9084 ± 0.0529**
- f1_stag: 0.8835 ± 0.0573
- f1_prog: 0.9333 ± 0.0488

**Seed 123 确认为 outlier**：test macro_f1 比 seed 42 低 9.4pp（val 阶段仅低 3-4pp，test 上差距扩大）。所有 std 远超 0.01 阈值。

**根因**：三个 seed 不仅 init 不同，train/val/test 划分也不同（test 集大小分别为 1824/2216/2343），方差同时包含了 split variance 和 init variance。如果论文需要稳定的 mean±std，建议固定 split 只变 seed，或增加 seed 数量。Registry 和 artifact 均已更新。

---
