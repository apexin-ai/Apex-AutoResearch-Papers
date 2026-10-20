# analysis prolog sta s44 premise count

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_prolog-sta-s44-premise-count_20260514T184205_result.json`
- **Structured JSON:** [`745ffbc22b733c9c2f7a.json`](../../sessions/74/745ffbc22b733c9c2f7a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Analysis complete. Key findings:

**s44 ISR=0.885 is 100% artifact.** The model collapsed entirely to single-clause H7 programs:
- 78/100 samples: 1 clause matching the query exactly → ISR=1.0 (tautological)
- 22/100 samples: 1 fact + 1 NL comment → ISR=0.5
- **Zero samples have n_clauses ≥ 3** — premise-count controlled ISR cannot even be computed

**All 3 Prolog STA seeds are negative** with distinct failure modes:

| Seed | PR | ISR | ISR (n_cl≥3) | Failure Mode |
|------|-----|------|-------------|-------------|
| s42 exec | 86% | 0.043 | 0.051 | Verbose dumps, n_nec≈0 |
| s43 STA | 36% | 0.113 | 0.149 | Always n_necessary=1 |
| s44 STA | 97% | 0.885 | **N/A (0 samples)** | Total H7 collapse |

Compared to FOL D051 (where n_prem≥3 ISR ratio was 1.06×, i.e. no real advantage), Prolog s44 is even more extreme — the model didn't just benefit from low-premise inflation, it **exclusively generated** 1-2 clause programs. Goodhart collapse is more thorough in Prolog than FOL.

Report registered as `art_20260514_dd1269`.

---
