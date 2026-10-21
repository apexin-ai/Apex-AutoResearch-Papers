# writing w2 domain bias paper update

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_writing_w2-domain-bias-paper-update_20260516T013302_result.json`
- **Structured JSON:** [`1b895e39a95d4222ac19.json`](../../sessions/1b/1b895e39a95d4222ac19.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

No dedicated LOGO table. The paper already has the correct v2 numbers:

**Verified matches:**
- `section_appendix.tex:97` — LOGO mean 72.1%, range 59.5–81.6%, CV 72.0% ✓
- `section_appendix.tex:102` — Depth pred 72.0%, seed-group 10.2% ✓  
- `section_appendix.tex:103` — Ratio 7.1× ✓
- `conclusion.tex:15` — LOGO 72.1%, CV 72.0%, seed-group 10.2% ✓

**No stale numbers found:** No "8pp drop" or "22.9% min" anywhere in the .tex files.

The paper text already reflects the v2 corrected LOGO results. The numbers match exactly:
- Mean LOGO = 72.1%, Mean CV = 72.0%, mean drop = -0.08pp (reported as "within noise")
- Range 59.5–81.6% matches per-cell min/max from v2 table
- Sub-C: 72.0% depth vs 10.2% seed-group (chance level)

No edits needed — the paper was already updated to v2 results.

---
