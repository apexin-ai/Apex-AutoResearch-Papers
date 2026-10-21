# code eval anova batch prep

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_eval-anova-batch-prep_20260527T041435_result.json`
- **Structured JSON:** [`f569e898e89f69651f35.json`](../../sessions/f5/f569e898e89f69651f35.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Both paths work. The script handles balanced/unbalanced designs correctly.

**Deliverables:**

1. **Eval batch commands** → `artifacts/_project/data/eval_batch_commands.md`
   - 8 complete nohup eval commands ready to copy-paste via `ssh_execute`
   - Maps user names (e.g. `s1c_r2`) to actual checkpoint IDs (e.g. `full_occ_ln_v2_s1c`)
   - Includes monitoring and result collection commands

2. **`run_v2_anova.py`** → `artifacts/_project/data/run_v2_anova.py`
   - 2x2 ANOVA (Type III SS) via statsmodels
   - Partial eta-squared, Cohen's d, simple effects
   - Bootstrap 95% CI (10000 resamples) for cell means and contrasts
   - Comparison vs Vanilla baseline
   - Supports `--json data.json` or built-in defaults
   - Dry-run verified with current data (N=9, min cell n=1) and synthetic full data (N=16)

Key checkpoint ID mapping (user name → actual):
- `full_occ_ln_v2_s1c_r2` → `full_occ_ln_v2_s1c`
- `full_occ_ln_v2_s2_r2` → `full_occ_ln_v2_s2`
- `detach_ln_v2_s0c_r2` → `detach_ln_v2_s0c`
- `detach_ln_v2_s1_35` → `detach_ln_v2_s1`

---
