# audit appendix tables

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_appendix_tables_20260529T052825_result.json`
- **Structured JSON:** [`976f3e5e1042adb0353b.json`](../../sessions/97/976f3e5e1042adb0353b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

The audit is complete. The report is at `artifacts/audit_appendix.md` — 29/29 tables audited, ~580 numerical values checked, 6 issues documented:

| ID | Severity | Issue |
|----|----------|-------|
| P1 | Medium | `fig_multi_layer_attn` plot script has L31=19 trained heads; table/text/server all say 18 |
| P2 | Medium | `tab:2x2_r2_summary` Δ_train(L15–L25 avg) not reproducible from per-layer data |
| P3 | Medium | TraceVLA Reference late-layer std reported as 0.068, computed as 0.170 |
| P4 | Low | Appendix prose says "L32: 0.551" — should be L31: 0.557; std range also off |
| P5 | Low | `tab:seed_sensitivity` R² std=0.002 vs 0.001 from displayed values |
| P6 | Info | Unnamed counterfactual Goal table (L271) missing `\label` |

None of these affect the paper's main conclusions. P1 is the most actionable — a single hardcoded value in the plot script.

---
