# fix e7 persist results

**Are Stagnation Signals Structural? A Systematic Empirical Study of Progress Detection in LLM Agents via Weak Supervision LLM-based agents deployed on software001** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_e7-persist-results_20260515T143058_result.json`
- **Structured JSON:** [`56d4963e61cfc5323ed9.json`](../../sessions/56/56d4963e61cfc5323ed9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已完成。`artifacts/gold_set/e7_probe_oh_gold.json` 已保存并注册。

核心数据：
- **OH gold 覆盖**: 158/169 有 embeddings (93.5%)
- **OH gold 标签分布**: 5 stagnation / 164 progress (97% progress)
- **GRU Probe OH-only**: macro-F1=0.475, f1_stag=0.093
- **TWV Probe OH-only**: macro-F1=0.477, f1_stag=0.000
- **GRU Probe SWE-only**: macro-F1=0.787 (供 E4 scope-matching 参考)
- **TWV Probe SWE-only**: macro-F1=0.854 (供 E4 scope-matching 参考)

SWE-only probe 结果也已包含在文件中，可直接用于 E4 scope-matching 对比。

---
