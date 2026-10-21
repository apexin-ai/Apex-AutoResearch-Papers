# analysis oracle improvable fraction

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_oracle_improvable_fraction_20260515T050344_result.json`
- **Structured JSON:** [`b8ff385966203ca6bf07.json`](../../sessions/b8/b8ff385966203ca6bf07.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。结果：

| Config | Total | Improv | Degrad | Tied | Imp% | Headroom | Degrad |
|---|---|---|---|---|---|---|---|
| qwen_scierc_ner | 529 | 222 | 2 | 305 | 0.4197 | 0.3186 | 0.4773 |
| qwen_scierc_re | 397 | 164 | 9 | 224 | 0.4131 | 0.4530 | 0.2803 |
| llama_scierc_ner | 529 | 208 | 2 | 319 | 0.3932 | 0.3368 | 0.1114 |
| qwen_conll_ner | 2756 | 251 | 5 | 2500 | 0.0911 | 0.4482 | 0.2419 |
| llama_conll_ner | 2756 | 110 | 0 | 2646 | 0.0399 | 0.4608 | 0.0000 |

SciERC 上约 39-42% 的 instance 有至少一个 sample 优于 greedy，headroom 约 0.32-0.45 F1。CoNLL 上 improvable 比例显著低（4-9%），因为 greedy 本身已经很强，但 improvable instance 的 headroom 仍有 0.45 左右。degradable instance 极少（0-9 个），说明 sampling 几乎不会全部劣于 greedy。

已保存到 `output/review_round2/oracle_improvable_fraction.json`。

---
