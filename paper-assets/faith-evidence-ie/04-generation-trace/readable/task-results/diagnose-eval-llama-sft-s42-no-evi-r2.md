# diagnose eval llama sft s42 no evi r2

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_eval-llama-sft-s42-no-evi-r2_20260520T143838_result.json`
- **Structured JSON:** [`845e8e21b38e36563796.json`](../../sessions/84/845e8e21b38e36563796.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新为 DONE/success。

**诊断结果：实验成功完成，进程正常退出 (EXIT_CODE=0)。**

| 指标 | 值 |
|------|-----|
| Ign-F1 | **0.5219** |
| F1 | 0.5311 |
| Format OK | 88.7% |
| Truncated | 219/985 |

**Evidence Tax (LLaMA SFT s42)**：with-evidence ign_f1=0.5384 → no-evidence ign_f1=0.5219，差值 **0.0165 (3.1% relative drop)**。cuda:3 现已空闲。

---
