# analysis test eval llama rsft s42 with evi v3

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_test_eval_llama_rsft_s42_with_evi_v3_20260523T115003_result.json`
- **Structured JSON:** [`b236d68ea07c572d7962.json`](../../sessions/b2/b236d68ea07c572d7962.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry updated, artifact registered. Summary:

**v3 成功修复了 field compliance 问题**（176/500 → 499/500），产出干净结果。

**关键结论：**
- **ign_f1 = 0.3554**，与 s43 (0.3488) 跨 seed 一致（+0.66pp）
- **修正后 LLaMA 8B evidence tax = −2.20pp**（evidence helps），方向与旧值 −2.65pp 一致，幅度减小 0.45pp（旧值因 field compliance 低导致 with-evi F1 偏低，tax 被夸大）
- 两个 seed 方向一致：s42 = −2.20pp, s43 = −1.17pp
- LLaMA 8B 与 Phi 8B / 1.7B 同向（evidence helps），仅 4B 反向（evidence hurts）

---
