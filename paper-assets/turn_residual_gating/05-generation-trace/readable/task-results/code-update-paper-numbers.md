# code update paper numbers

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_update_paper_numbers_20260522T180818_result.json`
- **Structured JSON:** [`490ba3c3e50265678d29.json`](../../sessions/49/490ba3c3e50265678d29.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

No more MISSes. All 33 replacements matched across 4 files.

Script created at `scripts/update_paper_numbers.py`:
- **14 rule categories** covering abstract, intro, experiments, and discussion
- Supports `--summary` (aggregated JSON) and `--results-dir` (per-seed eval JSONs)
- `--dry-run` (default) prints what would change; `--apply` writes to .tex files
- Handles: AR GAR range, gap range, TF spread, SS improvement/gap compression, TG multi-seed stats, Table 1 AR values (regex), N=5→N=50, and `(single seed)` annotations
- Rules that produce no change (old == new) are automatically skipped

---
