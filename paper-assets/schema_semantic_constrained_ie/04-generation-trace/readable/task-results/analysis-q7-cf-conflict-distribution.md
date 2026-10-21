# analysis q7 cf conflict distribution

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_q7_cf_conflict_distribution_20260515T085725_result.json`
- **Structured JSON:** [`4b9c9a0d2ef479ea322c.json`](../../sessions/4b/4b9c9a0d2ef479ea322c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已写入 `artifacts/rebuttal/q7_cf_distribution_report.md`。

**关键发现**:

- **SciERC full_s1 (Qwen v2) 共 245 个 CF**，全部为 2-type 冲突，完整分布 15 个 pair：
  - Top-1: Generic ↔ OtherScientificTerm = **85 (34.7%)**，**不是任务中说的 60**
  - "60" 对应的是 **full_s2** (179 CF 中 60 个 Generic↔OtherScientificTerm)，user 可能混淆了 s1/s2
  - 涉及 Generic 的冲突合计 155 (63.3%)

- **跨模型/数据集**:
  - SciERC full_s1 (Llama): 162 CF，Top-1 同样是 Generic↔OtherScientificTerm (53, 32.7%)
  - DocRED full_s1 (Qwen): 2670 CF，Top-1 MISC↔ORG (701, 26.3%)
  - DocRED full_s1 (Llama): 3824 CF，Top-1 NUM↔TIME (671, 17.5%)
  - 所有 unconstrained baseline 都 ≤10 CF — **CF violation 是 constrained decoding 的产物**

- **语义解释**: SciERC 中 Generic 是 anaphoric 占位类型，DocRED 中 MISC 是 catch-all。两者都吸收低置信度 mention，导致 per-slot 决策跨 slot 漂移。报告内含直接可投到 rebuttal 的回复模板。

---
