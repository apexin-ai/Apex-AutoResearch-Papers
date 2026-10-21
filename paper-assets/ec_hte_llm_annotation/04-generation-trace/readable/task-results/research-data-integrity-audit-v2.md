# research data integrity audit v2

**When Debiasing Hurts: An Exact Bias Identity for LLM-Annotated Treatment Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_data-integrity-audit-v2_20260523T195958_result.json`
- **Structured JSON:** [`88e9e3f26c66913e3337.json`](../../sessions/88/88e9e3f26c66913e3337.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

审计完成。报告已保存到 `artifacts/data_integrity_audit_v2.md`。

**核对结果**: 59 项中 54 项一致, 5 项存在问题:

1. **Table 1 Strat. MLE Coverage**: 数据 0.9450, 论文写 0.95 (边界舍入)
2. **R²=0.994 (K=2 synthetic)**: 数据 0.993, 论文写 0.994 (微小向上舍入)
3. **R²=0.974 (K=4 synthetic)**: 数据 0.965, 差 0.009 — 可能与 real-CM R²=0.975 混淆, 需核实
4. **"10 of 11 ≥ 0.93"**: 实为 9 of 11 (gpt-4o-mini×TweetEval R²=0.929 < 0.93)
5. **AUC=1.0 (Δτ>0 subgroups)**: 方向一致但无法从 CSV 精确复现

另外, appendix 中 "seven LLMs" 与主文 "eight" 及 Table 21 (9 models) 存在内部不一致。

---
