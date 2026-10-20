# analysis encoder ablation results

**Are Stagnation Signals Structural? A Systematic Empirical Study of Progress Detection in LLM Agents via Weak Supervision LLM-based agents deployed on software001** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_encoder-ablation-results_20260514T135021_result.json`
- **Structured JSON:** [`a2183517a4c4f46768c7.json`](../../sessions/a2/a2183517a4c4f46768c7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。两个实验均已标记 DONE(success)。

**Test 结果汇总 (n=1824)**

| Encoder | test macro_f1 | test acc | f1_stag | f1_prog | val macro_f1 | best_epoch | vs probe_001 |
|---|---|---|---|---|---|---|---|
| e5-large | 0.9363 | 0.9501 | 0.9067 | 0.9660 | 0.9596 | 4 | +3.1pp |
| **bge-m3** | **0.9413** | **0.9534** | **0.9147** | **0.9679** | 0.9579 | 5 | **+3.6pp** |
| probe_001 (SFR/Qwen3) | 0.905 | - | - | - | - | - | baseline |

bge-m3 在 test 上全面优于 e5-large，两者均显著超过 probe_001 baseline。两个 encoder 的 val-test gap 约 2pp，正常范围。

---
