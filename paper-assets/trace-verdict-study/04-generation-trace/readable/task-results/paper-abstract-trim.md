# paper abstract trim

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_abstract_trim_20260519T154034_result.json`
- **Structured JSON:** [`fff2f810a7780458072e.json`](../../sessions/ff/fff2f810a7780458072e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

验证统计：

**词数**：~154（在 150-200 范围内）

**具体数字**：3 个
1. ≥99.33% — exception_only 跨模型表现
2. 18 percentage points — full_trace gap
3. 50 training steps — 收敛速度

**Narrative arc**：
1. Exception events suffice → "≥99.33% accuracy on three of four models"
2. More info hurts → "complete traces plateau roughly 18 pp lower"
3. Mechanism (training dynamics) → "converges within 50 steps" vs "oscillates throughout training"
4. Mechanism (density) → "information overload and gradient dilution from low-density tokens"

**已删除**：55.5%、150 tokens、500 tokens、76%/24%、96.58%、82-88%、82-89%、100% recall、10×

**无 AI 风格词汇**，主动语态为主。

---
