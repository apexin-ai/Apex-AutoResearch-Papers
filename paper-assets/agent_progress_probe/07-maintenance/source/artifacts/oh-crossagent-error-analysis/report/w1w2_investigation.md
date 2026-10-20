# W1 & W2 Investigation Report

Date: 2026-05-15

## W1: Probe ZS macro_f1 = 0.581 vs 0.5984

### Findings

Both values are **correct** — they differ because of evaluation scope, not model or data mismatch.

| Metric source | Value | Checkpoint | Data | Scope |
|---------------|-------|-----------|------|-------|
| oh_crossagent_error_analysis.py | 0.5810 | checkpoints_full/best_model.pt (probe-002, epoch=9) | embeddings_fixed.pt conf>=2 | ALL 43,366 windows |
| fewshot_results_fixed/fewshot_results.json | 0.5984 | checkpoints_full/best_model.pt (probe-002, epoch=9) | embeddings_fixed_conf2.pt | test split only (6,122 windows) |

### Root cause

The fewshot script splits 43,366 windows into train/val/test by instance (trajectory). The zero-shot result (0.5984) is evaluated on the **test split** (6,122 windows), not the full dataset. The error analysis script evaluates on **all** 43,366 windows (0.5810).

Both use the same model (probe-002) and same data (fixed labels, conf>=2). The 0.03 difference is sampling variance across the instance-level split.

### Conclusion

- For the **paper** (Table 2, cross-agent transfer): 0.5984 is correct (test-split evaluation, consistent with how SWE results are reported).
- For the **error analysis** (all-window error examination): 0.581 is correct (needs full coverage to characterize errors).
- No registry update needed.

---

## W2: Error overlap coverage 28.4% → 100%

### Bug

In `oh_crossagent_error_analysis.py`, line ~258:

```python
c2_windows = [non_abstain_windows[i] for i in conf2_mask]
```

`conf2_mask` contains indices into the embedding tensor (0..43,365). `non_abstain_windows` is loaded from `windows_labeled.jsonl` (154,743 entries). Using embedding indices to index into JSONL data produces wrong windows — different ordering between embeddings and JSONL.

The same misalignment propagated to the error overlap section (lines 620-640), where `probe_keys` were built from the wrong `c2_windows`, yielding only 12,328 / 43,366 = 28.4% key overlap.

### Fix

In `oh_crossagent_error_analysis_fixed.py`:

1. **Window matching**: Build a lookup `{(trajectory_id, tuple(step_indices)): window}` from all JSONL windows. Match each embedding entry by its `(traj_id, step_indices)` key stored in the embedding file.
   - Result: 43,366 / 43,366 = **100% match** (0 unmatched).

2. **Overlap key matching**: Use `(trajectory_id, tuple(step_indices))` keys for both probe and structural predictions instead of positional indexing.
   - Result: 43,366 common windows (100% coverage).

### Fixed error overlap results

| Metric | Old (buggy) | Fixed |
|--------|-------------|-------|
| Common windows | 12,328 | 43,366 |
| Coverage | 28.4% | **100.0%** |
| Probe errors | — | 8,643 |
| Structural errors | — | 1,342 |
| Both error | — | 358 |
| Probe-only errors | — | 8,285 |
| Struct-only errors | — | 984 |
| Overlap rate (of probe errors) | — | **4.14%** |
| Overlap rate (of struct errors) | — | **26.68%** |

### Interpretation

The two methods make largely **complementary** errors:
- Only 4.1% of probe errors overlap with structural errors — the probe's failures (mostly FP: predicting stagnation as progress) are in regions where structural features classify correctly.
- 26.7% of structural errors overlap with probe errors — about a quarter of structural failures also fool the probe.
- The probe has 6.4x more errors than the structural GB (8,643 vs 1,342) in zero-shot cross-agent transfer, confirming that representation-based transfer degrades significantly without fine-tuning on the target agent.

### Full results

Saved to: `results/oh_crossagent_error_analysis_fixed.json` on server bjb2-23165.
