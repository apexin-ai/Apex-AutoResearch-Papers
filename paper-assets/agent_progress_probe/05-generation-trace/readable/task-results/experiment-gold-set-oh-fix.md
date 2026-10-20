# experiment gold set oh fix

**Are Stagnation Signals Structural? A Systematic Empirical Study of Progress Detection in LLM Agents via Weak Supervision LLM-based agents deployed on software001** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_experiment_gold-set-oh-fix_20260515T073532_result.json`
- **Structured JSON:** [`5ea425bac418988b98a8.json`](../../sessions/5e/5ea425bac418988b98a8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All done. Three deliverables written locally and registered:

| Deliverable | Path | Artifact ID |
|---|---|---|
| `oh_fix_report.md` | `artifacts/gold_set/oh_fix_report.md` | `art_20260515_a4fd2d` |
| `eval_results_full.json` | `artifacts/gold_set/eval_results_full.json` | `art_20260515_228dfd` |
| `eval_report_full.md` | `artifacts/gold_set/eval_report_full.md` | `art_20260515_498f01` |

**Summary of what was done on the server (bjb2-23165):**

1. **Merged** 154,743 OH windows into `data/windows_labeled.jsonl` (now 214,239 total)
2. **Patched** `evaluate_gold_set.py` with `--oh_trajectories` arg and source-aware trajectory routing
3. **Re-ran evaluation** — matched **195/199** (was 132), 4 unmatched are conf=0 abstains
4. **Ran stratified analysis** by source, confidence, and source x confidence

**Key numbers for the paper:**
- MV-Gold agreement: **74.9%** (n=195)
- conf>=2 agreement: **82.5%** (n=80), macro-F1=0.816
- SWE-agent conf=3: **100%** agreement (n=8)
- Best model: TWV Probe macro-F1=**0.768** (n=132, SWE-only)
- Structural GB macro-F1=**0.760** on full n=195

---
