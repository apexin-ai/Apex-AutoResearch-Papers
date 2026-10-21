# code qwen v3 full eval

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_qwen_v3_full_eval_20260518T102559_result.json`
- **Structured JSON:** [`6c8d8b80361ba983cc98.json`](../../sessions/6c/6c8d8b80361ba983cc98.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All data collected. Here's the full summary:

---

## Violation Report — Qwen v3 Constrained

| Violation | Count | Rate |
|---|---|---|
| ET (Entity Type) | 0 | 0.0% |
| EV (Event Vocab) | 0 | 0.0% |
| RoV (Role Vocab) | 0 | 0.0% |
| AC (Arg Constraint) | 109 | 2.1% |
| CF (Cross-Field) | 593 | 21.1% |
| **Go/No-go (RoV+AC)** | — | **2.05%** |

## Parse Failures

- **40/246 docs** (16.3%) failed to parse
- All 40 are **output truncation** — raw_output ranges 25.8k–34.8k chars, valid JSON that gets cut off at the token limit
- No structural/format errors; the model generates correct JSON but the documents are too long for the max token budget

## F1 Comparison

| Config | Entity F1 | Trigger F1 | Argument F1 |
|---|---|---|---|
| **Unconstrained** | 0.0000 | 0.1184 | 0.0009 |
| **Constrained v3** | 0.1409 | 0.1339 | 0.0168 |
| **v3 + Post-hoc** | 0.1409 | 0.1339 | 0.0170 |
| **v3 + CF Voting** | 0.1352 | 0.1339 | 0.0168 |

## Post-hoc Filtering

| | Constrained v3 | Unconstrained |
|---|---|---|
| Events before→after | 2835→2835 | 3013→2291 |
| Args before→after | 5330→5221 | 5467→23 |
| Removed | 109 (AC only) | 4834 (722 EV + 4094 RoV + 18 AC) |

Unconstrained post-hoc is devastating — 99.6% of arguments removed because the model uses out-of-vocabulary role names.

## CF Majority Voting

- CF violations: 593 → 499 (fix rate 15.9%, 110 corrections)
- 563 corrections blocked by AC constraints
- Top corrections: PER→FAC (20), PER→GPE (10), ORG→GPE (7)
- Entity F1 slightly **decreased** (0.1409→0.1352) — the voting re-types some entities incorrectly
- Argument F1 unchanged (0.0168)

## Key Takeaways

1. Constrained v3 massively outperforms unconstrained (Arg F1 0.0168 vs 0.0009) — schema constraints work
2. Post-hoc on v3 is near-no-op (only 109 AC removals, +0.0002 Arg F1) — constraints already did the job at generation time
3. CF voting hurts entity F1 — AC constraints block most corrections, and the unblocked ones are often wrong
4. 16.3% parse failure rate from truncation is the main bottleneck — those 40 long docs contribute zero to F1

---
