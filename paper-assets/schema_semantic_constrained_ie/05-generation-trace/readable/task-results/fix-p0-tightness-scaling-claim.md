# fix p0 tightness scaling claim

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_p0_tightness_scaling_claim_20260514T210017_result.json`
- **Structured JSON:** [`92a8d926ae013be85b0c.json`](../../sessions/92/92a8d926ae013be85b0c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两处修改完成：

1. **section5_docred_draft.tex L220-222** — 替换了旧的 single-factor tightness scaling claim，改为 tightness × RV 交互叙事：RV 高的 Qwen 因 grammar 层强制匹配导致 latent DR 浮出，残余 DR 10.21%；RV 低的 Llama 达到 2.55%（DR↓90.2%）。保留了 L223-227 的 grammar R-F1 vs full S1 观察（无矛盾）。

2. **section5_crossmodel_draft.tex L102-108** — `[TIGHTNESS-NARRATIVE-TBD]` 替换为 3 句 tightness × RV 交互解释，引用 §5 tightness 段落，附 exp_id 注释追溯。

---
