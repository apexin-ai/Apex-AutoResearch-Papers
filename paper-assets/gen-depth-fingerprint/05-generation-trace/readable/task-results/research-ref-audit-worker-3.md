# research ref audit worker 3

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_ref-audit-worker-3_20260526T103739_result.json`
- **Structured JSON:** [`5a729199946ee5052289.json`](../../sessions/5a/5a729199946ee5052289.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Audit complete. Report written to `ref_audit_worker3.md`.

**4 issues found across 74 entries:**

**Serious (2):**
1. **`human_texts_outliers`** — Title and authors in bib don't match arXiv:2510.08602. The actual paper is by Cong Zeng et al. with title "Detecting LLM-generated Texts via Out-of-distribution Detection", not by Li Yafu et al. with "Rethinking..." subtitle. Either the arXiv ID or the metadata is wrong.
2. **`diveye`** — Venue is TMLR 2026, not ICLR 2026. The ICLR 2026 submission was withdrawn; GitHub repo confirms `[TMLR '26]`.

**Moderate (2):**
3. **`xu_spectrum_detection`** — Published at EMNLP 2024, but bib still lists it as arXiv preprint.
4. **`beyond_final_actor`** — ACL 2026 venue couldn't be independently confirmed yet.

All 74 entries verified as real papers. No hallucinated references. No cite-context mismatches found.

---
