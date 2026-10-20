# analysis qwen imp registry update

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_qwen-imp-registry-update_20260514T075546_result.json`
- **Structured JSON:** [`a7c3a3733011e56955d3.json`](../../sessions/a7/a7c3a3733011e56955d3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

4 个实验 registry 全部更新完毕，status=DONE, conclusion=success, failure_reason 已清除。

## Qwen2.5-7B Importance Masking 结果对比

| Metric | s=0.15 | s=0.20 | s=0.25 | s=0.30 |
|--------|--------|--------|--------|--------|
| **Verdict** | PASS | PASS | PASS | PASS |
| **Median II (high)** | 0.001 | -0.000 | 0.003 | 0.010 |
| **Median II (mid)** | -0.011 | 0.002 | 0.114 | 0.688 |
| **Median II (low)** | 0.039 | 0.235 | 1.271 | 2.953 |
| **PPL both (high)** | 1.31 | 1.37 | 1.54 | 1.86 |
| **PPL both (mid)** | 2.20 | 3.43 | 5.36 | 9.48 |
| **PPL both (low)** | 5.44 | 9.20 | 16.96 | 35.32 |
| **Low/High PPL ratio** | 4.2x | 6.7x | 11.0x | 19.0x |
| **Low/High II ratio** | ~45x | ~2000x | ~371x | ~295x |

趋势清晰：随 sparsity 增加，low phase 的 II 和 PPL 均爆炸式增长，high phase 几乎不受影响。Qwen2.5-7B 完全复现了 DeepSeek 的 phase-dependent interaction pattern。

---
