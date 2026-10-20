# analyze docred full s1 fallback

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_docred_full_s1_fallback_20260514T083432_result.json`
- **Structured JSON:** [`6f0aa49681e9ecfd04ae.json`](../../sessions/6f/6f0aa49681e9ecfd04ae.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已写入 `artifacts/docred_full_s1_dr_root_cause_analysis.md`。

---

**核心发现：**

1. **根因是约束紧度差异，不是 semantic 层失效**。DocRED avg tightness=0.842 vs SciERC=0.333 — DocRED 每个 relation 中位数仅允许 5/36 对 type pairs，SciERC 中位数 23/36。

2. **Semantic 层确实有效**：DR 从 grammar-only 的 26.17% 降到 10.19%（-61%，-15.98pp），几乎所有 relation 都有改善。

3. **剩余 10.19% 集中在高 tightness relations**：
   - tightness ≥ 0.95 (1-2 pairs): 聚合 DR = 30.6%
   - tightness 0.90-0.94 (3-4 pairs): 聚合 DR = 19.3%  
   - tightness < 0.70 (11+ pairs): 聚合 DR = 0.7%

4. **Fallback 日志不可用**（counter 代码在 full_s1 之后加入），但从 violation 模式可推断：高 tightness relations 下 semantic∩grammar=∅ 概率最大，是 fallback 高发区。

5. **SciERC DR 低的原因**：约束本身就松，Used-for 允许 35/36 对，最紧的 Compare 也有 17/36 对，LLM 几乎不可能违规。

---
