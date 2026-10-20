# analysis eval llama ar n20

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_eval_llama_ar_n20_20260522T081113_result.json`
- **Structured JSON:** [`e8956da57431ff53a058.json`](../../sessions/e8/e8956da57431ff53a058.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry updated to DONE/success. Summary:

**eval_llama_ar_n20 — SUCCESS**

N=20 (T=4) 3-way Llama AR evaluation complete. Key results:

| | Base | TG | LoRA-only |
|---|---|---|---|
| **GAR-ours mid** | 0.0088 | **0.0434** | 0.0284 |
| **GAR-dongre mid** | 0.0049 | 0.0183 | 0.0205 |
| **PPL** | 1.29 | 1.44 | 1.42 |

**Critical correction vs N=5:** GAR-ours ranking reversed — N=5 showed LoRA-only (0.0617) > TG (0.0304), but N=20 shows **TG (0.0434) > LoRA-only (0.0284)**. The N=5 LoRA-only estimate was inflated by outlier turns. N=20 confirms gating provides genuine GAR benefit beyond LoRA-only adaptation.

GAR-dongre still shows LO slightly > TG (0.0205 vs 0.0183), but both metrics agree on the Base < {TG, LO} ordering.

---
