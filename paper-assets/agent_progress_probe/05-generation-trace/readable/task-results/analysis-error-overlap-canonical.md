# analysis error overlap canonical

**Are Stagnation Signals Structural? A Systematic Empirical Study of Progress Detection in LLM Agents via Weak Supervision LLM-based agents deployed on software001** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_error-overlap-canonical_20260515T014801_result.json`
- **Structured JSON:** [`0674c7a6ba914f57819c.json`](../../sessions/06/0674c7a6ba914f57819c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Now I have the full picture. Let me compile the results and provide the report.

## Results

### Step 1: Root Cause — Initial Hypothesis is WRONG

The hypothesis that "Worker C evaluated structural on all-windows (conf=1)" is **incorrect**. Both scripts explicitly filter `confidence >= 2`. Verified:
- Worker C's `oh_crossagent_error_analysis_fixed.py` → `w.get("confidence", 0) >= 2`
- Worker A/B's `oh_crossagent_error_analysis.py` → same filter
- Both evaluate on 43,366–43,376 conf≥2 windows

**Actual root cause**: The v2 result (57 structural errors) is **not reproducible**. My canonical run using the exact same code logic, hyperparameters (GB: 200 trees, lr=0.05, max_depth=5, seed=42), data paths, and feature extraction produces 1,421 structural errors — aligning with Worker C's 1,342 (the small difference explained by Worker C's different hyperparameters: 100 trees, lr=0.1).

The v2 JSON was likely generated under conditions that no longer exist on disk. The most probable explanation: the script was edited after the v2 run (either by the same or a different Worker), and the v2 result came from a script version that is no longer recoverable.

### Step 2: Authoritative Numbers (Canonical Verification)

| Metric | v2 claim | Canonical run | Verdict |
|--------|----------|---------------|---------|
| n_windows (conf≥2) | 43,366 | 43,366 | **Confirmed** |
| Probe errors | 8,643 | 8,643 | **Confirmed** |
| Probe CM | TN=1661, FP=6955, FN=1688, TP=33062 | identical | **Confirmed** |
| Probe macro_f1 | 0.581 | 0.581 | **Confirmed** |
| Struct GB errors | 57 | **1,421** | **NOT confirmed** |
| Struct GB CM | FP=32, FN=25 | **FP=442, FN=979** | **NOT confirmed** |
| Struct GB macro_f1 | 0.998 | **0.950** | **NOT confirmed** |
| Both wrong | 31 | **364** | **NOT confirmed** |
| Overlap rate | 0.36% | **4.21%** | **NOT confirmed** |

**Paper impact**: Two claims need revision:
- `analysis.tex:56` — "only 0.4% of probe errors overlap" → should be **~4.2%**
- `appendix.tex:85,89` — "structural GB (0.998 on conf≥2)" → should be **~0.950**

The experiments table value (cross-agent 0.9674) comes from `cross_agent_structural_results.json`, a separately validated evaluation, and is not affected.

### Step 3: Script and Dry-Run Output

**Script**: `/root/autodl-tmp/agent_progress_probe/src/analysis/error_overlap_canonical.py`

**Dry-run output** (from `/tmp/canonical_run.log`):
```
=== Loading probe checkpoint ===
Checkpoint: epoch=9, embed_dim=1024, hidden=256, layers=2

=== Loading OH embeddings ===
Total embeddings: 143057
conf>=2: 43366 windows (stag=8616, prog=34750)

=== Probe inference ===
Probe: macro_f1=0.5810, errors=8643
  CM: TN=1661, FP=6955, FN=1688, TP=33062

=== Structural GB ===
SWE non-abstain: 54809
SWE features: (54809, 30)
Training GB on SWE data (n_estimators=200, lr=0.05)...
OH conf>=2 for structural: 43376
Struct GB: macro_f1=0.9498, errors=1421
  CM: TN=8184, FP=442, FN=979, TP=33771

=== Error overlap ===
Common windows: 43366 / probe=43366, struct=43376
Probe errors:  8643
Struct errors: 1421
Both wrong:    364
Probe-only:    8279
Struct-only:   1057
Overlap rate:  364/8643 = 0.0421 (4.21%)

Saved to results/error_overlap_canonical.json
```

**Output JSON**: `results/error_overlap_canonical.json`

---
