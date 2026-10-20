# diag baseline llm judge final

**Are Stagnation Signals Structural? A Systematic Empirical Study of Progress Detection in LLM Agents via Weak Supervision LLM-based agents deployed on software001** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_baseline-llm-judge-final_20260514T140715_result.json`
- **Structured JSON:** [`aa96ef9f8c99217946dd.json`](../../sessions/aa/aa96ef9f8c99217946dd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**baseline-llm-judge → DONE (success)**

最终结果：

| Metric | LLM Judge (zero-shot) | GRU Probe | Delta |
|--------|----------------------|-----------|-------|
| macro_f1 | 0.6625 | 0.9055 | **-24.3pp** |
| accuracy | 0.6721 | — | — |
| f1_stagnation | 0.6055 | — | — |
| f1_progress | 0.7195 | — | — |
| parse_failures | 0 | — | — |
| API cost | $11.66 | <$0.01 | — |
| Total tokens | 3,063,440 | — | — |

1824/1824 完成，0 parse failures，0 API fails。Claude Sonnet 4.6 zero-shot judge 大幅落后于 GRU probe（-24.3pp macro_f1），且成本高出 3 个数量级。Registry 已更新为 DONE/success。

---
