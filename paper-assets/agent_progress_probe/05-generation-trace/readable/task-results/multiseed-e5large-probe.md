# multiseed e5large probe

**Are Stagnation Signals Structural? A Systematic Empirical Study of Progress Detection in LLM Agents via Weak Supervision LLM-based agents deployed on software001** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_multiseed_e5large-probe_20260514T215551_result.json`
- **Structured JSON:** [`69ec1cfa1b35c7e3b60e.json`](../../sessions/69/69ec1cfa1b35c7e3b60e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个 seed 都训练和评估完成。汇总结果：

## E5-large Probe 3-Seed 结果

| Seed | best_epoch | macro_f1 | f1_stagnation | f1_progress |
|------|-----------|----------|---------------|-------------|
| 42   | -         | 0.9363   | 0.9067        | 0.9660      |
| 123  | 7         | 0.9433   | 0.9268        | 0.9598      |
| 456  | 6         | 0.9418   | 0.9242        | 0.9593      |

### Mean ± Std

| Metric | Mean | Std |
|--------|------|-----|
| macro_f1 | 0.9405 | ±0.0037 |
| f1_stagnation | 0.9192 | ±0.0109 |
| f1_progress | 0.9617 | ±0.0038 |

---
