# experiment dir i3 sica qwen3 14b

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_experiment_dir-i3-sica-qwen3-14b_20260520T172642_result.json`
- **Structured JSON:** [`080c24094a57a20f0e52.json`](../../sessions/08/080c24094a57a20f0e52.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果写入 `/root/symb_invariant_consensus/results/dir_i3_sica_qwen3_14b/results.json`。

## Dir-I3 结果：SICA vs SC on Qwen3-14B (FOLIO, n=204, k=12)

| 方法 | Correct | Accuracy |
|------|---------|----------|
| SICA | 177/204 | **86.76%** |
| SC   | 176/204 | **86.27%** |
| Δ(SICA−SC) | +1 | **+0.49 pp** |

**McNemar exact test**: p=1.0, **不显著**

**Discordant pairs** (仅 3 题不一致):
- SICA✓ SC✗: `folio_19`, `folio_20`
- SICA✗ SC✓: `folio_156`
- 175 题两者都对，26 题两者都错

SICA 在 Qwen3-14B 上略优于 SC (+0.49pp)，但差异在统计上不显著（仅 3 个 discordant pairs，太少无法检出差异）。

---
