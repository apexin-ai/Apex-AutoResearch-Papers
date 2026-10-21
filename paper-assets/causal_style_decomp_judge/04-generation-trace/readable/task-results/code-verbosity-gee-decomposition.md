# code verbosity gee decomposition

**The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_verbosity_gee_decomposition_20260521T050306_result.json`
- **Structured JSON:** [`c7926df17d42ee518c3c.json`](../../sessions/c7/c7926df17d42ee518c3c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果：

| Effect | OR | 95% CI | p |
|--------|-----|--------|---|
| **Verbose style** | **13.10** | [5.62, 30.55] | 2.60e-09 *** |
| **Originality** | **0.49** | [0.21, 1.14] | 0.096 ns |

符合预期：verbose OR = 13.10（极显著），originality OR = 0.49（不显著，p = 0.096）。Verbosity bias 完全由 style effect 驱动，originality 无显著贡献。

脚本已保存在 `csd_pipeline/verbosity_gee.py`。

---
