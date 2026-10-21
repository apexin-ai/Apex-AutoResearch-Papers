# audit ref verify B

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_ref-verify-B_20260526T103552_result.json`
- **Structured JSON:** [`4012a719f856e8e1f5f0.json`](../../sessions/40/4012a719f856e8e1f5f0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Report written to `artifacts/ref_audit_worker_B.md`.

**Results**: 91 entries audited, 68 passed, 23 have issues.

**P0 (9 serious issues across 10 entries):**
- `hsu2024improved` — fabricated authors (arXiv 2412.01547 is by Galinkin & Sablotny)
- `li2025m2s` — wrong authors AND title (arXiv 2503.04856 is by Ha et al.)
- `ren2024actorattack` — venue is ACL 2025, not ICLR 2025
- `jiang2024redqueen` — wrong title, wrong venue (ACL 2025 Findings), wrong year (2025)
- `mehrotra2024tap` — wrong subtitle ("Automatically" not "with the Pruning of Candidate Outputs")
- `robey2024smoothllm` — venue is TMLR, not ICML 2024
- `shen2025antidote` / `shen2024jailbreakantidote` — duplicate entries (same arXiv 2410.02298)
- `wang2026trajguard` — wrong title and wrong first author
- `marchiori2025jdapt` — wrong title

**P1 (9 entries):** missing venues (`chao2024jailbreakbench`, `yousefpour2025repbend`, `wu2025safeint`), under-specified citation (`metallamaguard3_2024`), title mismatches (`gguard2025`, `lu2025xboundary`), wrong journal name (`mann1988rst`), premature venue (`song2026multibreak`), non-standard source (`deceptivedelight2024`).

**18 uncited entries** should be removed or re-evaluated.

---
