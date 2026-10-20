# multiseed bgem3 probe

**Are Stagnation Signals Structural? A Systematic Empirical Study of Progress Detection in LLM Agents via Weak Supervision LLM-based agents deployed on software001** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_multiseed_bgem3-probe_20260514T215558_result.json`
- **Structured JSON:** [`a6133be593ae1529ed9f.json`](../../sessions/a6/a6133be593ae1529ed9f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇总 BGE-m3 Probe 3-seed 结果：

| Seed | test_macro_f1 | test_f1_stag | test_f1_prog | best_epoch | test_windows |
|------|--------------|-------------|-------------|------------|-------------|
| 42   | 0.9413       | 0.9147      | 0.9679      | -          | -           |
| 123  | 0.8474       | 0.8173      | 0.8775      | 2          | 2216        |
| 456  | 0.9364       | 0.9183      | 0.9545      | 5          | 2343        |

**3-seed Mean±Std:**
| Metric | Mean±Std |
|--------|----------|
| macro_f1 | 0.9084 ± 0.0529 |
| f1_stagnation | 0.8834 ± 0.0573 |
| f1_progress | 0.9333 ± 0.0488 |

Seed 123 明显低于其他两个 seed（macro_f1 低 ~9 个百分点），方差较大。这可能是 `split_by_instance` 基于不同 seed 给出了差异较大的 test 集划分——seed 123 的 test set（2216 windows）也比 seed 456（2343）少。

---
