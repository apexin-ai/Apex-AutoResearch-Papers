# knowledge paper framing fix

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_knowledge_paper_framing_fix_20260517T010520_result.json`
- **Structured JSON:** [`89a4a1703c2863239fef.json`](../../sessions/89/89a4a1703c2863239fef.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。修正内容：

1. **4B evidence tax**: 所有 -7.0pp → -7.5pp（Core Insight、Story Arc、Claim 5、Evidence Tax Scaling 表）
2. **MVP Evidence Summary 表**：SFT baseline Ign-F1 40.36→39.86，no-evidence Δ +7.00pp→+7.50pp，所有 RSFT/DPO/GRPO 的 Δ vs SFT 列同步重算（基于新 baseline 39.86）
3. **移除矛盾的内联计算**：Claim 5 中 "(D076 统一协议：no-evi 47.36 vs with-evi 40.36)" 删除（与 -7.5pp 矛盾）
4. **最后更新日期**：2026-05-16 → 2026-05-17

已确认：p=0.44 全文一致，"non-monotonic" 已在使用（无 V-shape 残留），1.7B = +6.2pp 正确。

---
