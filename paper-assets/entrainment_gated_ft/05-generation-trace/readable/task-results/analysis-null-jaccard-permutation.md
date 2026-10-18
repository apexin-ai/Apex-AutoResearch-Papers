# analysis null jaccard permutation

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_null-jaccard-permutation_20260520T011902_result.json`
- **Structured JSON:** [`2cf5d612bd16bddd7244.json`](../../sessions/2c/2cf5d612bd16bddd7244.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果：

**所有 6 对 Jaccard（3 对 × helped/hurt）均显著高于 null baseline（p < 0.0001, z = 5.91–8.61）。**

| Category | Pair | J_obs | J_null | z | p |
|----------|------|-------|--------|---|---|
| **Helped** | GDN vs HGRN2 | .100 | .051 | 7.11 | <.0001 |
| | GDN vs RetNet | .092 | .045 | 6.75 | <.0001 |
| | HGRN2 vs RetNet | .108 | .049 | 8.61 | <.0001 |
| **Hurt** | GDN vs HGRN2 | .088 | .049 | 5.91 | <.0001 |
| | GDN vs RetNet | .103 | .056 | 6.85 | <.0001 |
| | HGRN2 vs RetNet | .087 | .045 | 6.05 | <.0001 |

Null baseline J̄ ≈ 0.048 (helped) / 0.050 (hurt)，观测值约为 null 的 **2 倍**。粗估验证也吻合（462×426 / 5153×~880 ≈ 0.043）。

结论：overlap 虽然绝对值低（~10%），但显著高于随机预期，确认了跨架构存在系统性共享的 helped/hurt 样本。结果已保存至 `artifacts/null_jaccard_results.json` 和服务器 `/root/entrainment_gated_ft/null_jaccard_results.json`。

---
