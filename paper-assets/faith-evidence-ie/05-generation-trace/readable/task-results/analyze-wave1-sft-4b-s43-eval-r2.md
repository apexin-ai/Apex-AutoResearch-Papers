# analyze wave1 sft 4b s43 eval r2

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_wave1_sft_4b_s43_eval_r2_20260518T213345_result.json`
- **Structured JSON:** [`9444656f8d9c8341f9eb.json`](../../sessions/94/9444656f8d9c8341f9eb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry updated, status = DONE (success).

## wave1_sft_4b_s43_eval_r2 结果摘要

| 指标 | s43 值 | s42 canonical | 差异 |
|------|--------|---------------|------|
| **ign_f1** | **0.4365** | 0.3974 | **+3.91 pp** |
| rel_f1 | 0.4429 | 0.4049 | +3.80 pp |
| evi_f1_joint | 0.3462 | — | — |
| evi_f1_tp | 0.8021 | — | — |
| edcr | 0.6827 | — | — |
| format_compliance | 100% | — | — |
| n_truncated | 318/985 | — | — |
| n_predictions | 17,055 | — | — |
| inference_time | 7,158s | — | — |

**Conclusion: success.** s43 的 ign_f1=0.4365 比 s42 canonical 高 +3.91 pp，是目前 4B SFT 三个 seed 中最好的结果。截断率 32.3% 偏高但未影响格式合规率（100%）。与更大模型相比仍有差距（1.7B s42: 0.4786, 8B s42: 0.5051）。

---
