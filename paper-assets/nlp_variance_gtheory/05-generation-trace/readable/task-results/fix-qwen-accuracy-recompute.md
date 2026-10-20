# fix qwen accuracy recompute

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_qwen_accuracy_recompute_20260521T074236_result.json`
- **Structured JSON:** [`54870a1c115090288726.json`](../../sessions/54/54870a1c115090288726.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**exp001_qwen overall accuracy（259,200 条）：0.7252**

| precision | correct | total | accuracy |
|-----------|---------|-------|----------|
| bfloat16 | 72,749 | 100,200 | 0.7260 |
| float16 | 57,769 | 79,600 | 0.7257 |
| float32 | 57,446 | 79,400 | 0.7235 |

三种 precision 差异极小（< 0.3pp），float32 略低。共 1,227 个 unique condition_id，3 档 temperature（0.0 / 0.3 / 0.7）。

---
