# fix audit d1 d6 all

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_audit_d1_d6_all_20260523T195857_result.json`
- **Structured JSON:** [`3b13ad93fe270b88807f.json`](../../sessions/3b/3b13ad93fe270b88807f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All 5 issues fixed. Summary:

| Issue | File | Change |
|-------|------|--------|
| **D1** | `experiments.tex:42` | Caption rewritten: "TF evaluation, N=45, 7-8% decay" → "AR generation, N=5, 77-81% decay" |
| **D1** (spillover) | `analysis.tex:31` | Inline reference fixed: removed wrong "7-8% decay" TF claim, correctly attributes 77-87% decay to AR figure |
| **D2** | `analysis.tex:12` | Fig 3b caption: added "($N$=5 pilot)" |
| **D3** | `appendix.tex:299` | Table: 7.2h/+20% → 8.0h/+33% |
| **D3** | `appendix.tex:313` | Text: "~20% overhead" → "~33% overhead" |
| **D4** | `appendix.tex:279` | SS ratio: "0 to 0.5" → "0 to 0.3" |
| **D6** | `abstract.tex:2` | "27× on Llama" → "27× (median) on Llama" |
| **D6** | `analysis.tex:41` | "27× on Llama" → "27× (median) on Llama" |

---
