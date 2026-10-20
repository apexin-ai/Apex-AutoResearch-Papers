# ssh fix h5 tab s3c

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_fix_h5_tab_s3c_20260525T203719_result.json`
- **Structured JSON:** [`16c3079076f9ecfa73a2.json`](../../sessions/16/16c3079076f9ecfa73a2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Fix applied. Summary:

**Tab s3c OBD per-depth recall** changed from `96, 39, 14, 19, 22` (sum=190, 38.0%) to `94, 44, 17, 15, 23` (sum=193, **38.6%**).

**Reproduction**: 6-class multiclass LightGBM (pipeline hyperparams: n_est=300, md=8, nl=63) trained on full 30K data, OOF predictions on first 100 doc_ids per depth (depths 0-4), N=500. Gives exactly 193/500 = 38.6%.

**LaTeX**: `appendix.tex:205` updated. Bold pattern unchanged. GPT-5.5 and Claude rows remain untouched (already self-consistent).

**Report**: `artifacts/h5_fix_recall_values.md`

**Note**: The caption claims "gap originates from depth-0" but with corrected values, Depth 1 contributes more (+25) than Depth 0 (+17) to OBD's advantage over LLMs. This is a minor wording issue, not a numerical error.

---
