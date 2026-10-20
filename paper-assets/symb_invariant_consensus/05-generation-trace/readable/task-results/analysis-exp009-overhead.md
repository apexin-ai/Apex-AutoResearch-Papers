# analysis exp009 overhead

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp009-overhead_20260517T113105_result.json`
- **Structured JSON:** [`6b6cecfb45a7ee76486f.json`](../../sessions/6b/6b6cecfb45a7ee76486f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

CSV 已写入 `/root/symb_invariant_consensus/results/exp009_overhead/overhead_breakdown.csv`。

```
============================================================
OVERHEAD ANALYSIS (n=804 problems):
Mean total wall time: 61.6s/question
  - Trace generation:       31.6s (51.3%)
  - Constraint extraction:  29.0s (47.0%)
  - Deduplication:          1.0s (1.6%)
  - MaxSAT solving:         0.003s (0.00%)
SICA overhead vs SC: +30.0s/question (+48.7%)
  (SC equivalent = trace generation only: 31.6s)
============================================================

PROOFWRITER (n=600):
  Total: 65.6s | Trace: 32.0s (48.7%) | Extract: 32.5s (49.6%)
  SICA overhead: +33.6s (+51.3%)

FOLIO (n=204):
  Total: 49.8s | Trace: 30.6s (61.4%) | Extract: 18.5s (37.2%)
  SICA overhead: +19.2s (+38.6%)

Overhead % percentiles:
  P50: 48.9%  |  P90: 57.6%  |  P99: 63.7%
```

关键发现：
- SICA 的 overhead 几乎全部来自 **constraint extraction**（LLM 二次调用），占总时间 47%
- MaxSAT 求解和去重可忽略不计（合计 <2%）
- 相比纯 SC，SICA 平均每题多花 30s（+48.7%），即总时间约翻倍
- ProofWriter 的 overhead 比 FOLIO 更重（51.3% vs 38.6%），因为 ProofWriter 约束提取文本更长

---
