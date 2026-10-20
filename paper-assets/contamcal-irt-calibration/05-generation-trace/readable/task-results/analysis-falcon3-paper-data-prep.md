# analysis falcon3 paper data prep

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_falcon3-paper-data-prep_20260522T131429_result.json`
- **Structured JSON:** [`5e35b8161f770a90608b.json`](../../sessions/5e/5e35b8161f770a90608b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已注册 `art_20260522_2e1572`。产出包含：

1. **Table 1 更新行** — Falcon3 MMLU/ARC 完整 5-dosage 数据，Δ(d100)=+4.19pp/+4.01pp，Pattern=Benefit
2. **三家 Benefit 对比表** — Falcon3 vs OLMo-2 vs Gemma-2 逐 dosage MMLU+ARC 数据，含 shape/consistency 对比。Falcon3 MMLU benefit magnitude 最大(+4.19pp)
3. **SFT tax** — 8.63pp，Rank 3/7，已引用 `sft_tax_analysis.md` 现有数据
4. **Cross-benchmark consistency** — MMLU×ARC agreement 从 5/6 (83%) 升到 **6/7 (86%)**，Falcon3 双 Benefit 一致
5. **Taxonomy 更新** — Benefit×3 成为最多类别(43%)；baseline gradient 三个 Benefit 家族全部 <62%，强化 vulnerability gradient

---
