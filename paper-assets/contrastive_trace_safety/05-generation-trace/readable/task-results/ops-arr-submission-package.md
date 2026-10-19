# ops arr submission package

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_arr_submission_package_20260520T043855_result.json`
- **Structured JSON:** [`3c59837bb2c49375fc56.json`](../../sessions/3c/3c59837bb2c49375fc56.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Submission package is complete. Summary:

**`artifacts/submission_package/`** — 34 files:

| Component | Contents |
|---|---|
| **code/src/** | 17 anonymized Python files (core library: config, data loader, hidden state extraction, probes, evaluation, baselines, experiments) |
| **code/scripts/** | 10 experiment scripts (layer sweep, ensemble, residualization, random projection, threshold sensitivity, etc.) |
| **code/reproduce/** | 3 shell scripts: `reproduce_table2.sh` (HS vs text), `reproduce_table3.sh` (layer selection), `reproduce_table4.sh` (ensemble) |
| **code/requirements.txt** | 9 dependencies (torch, transformers, datasets, scikit-learn, etc.) |
| **code/README.md** | Setup guide, directory structure, reproduction instructions |
| **DATA_STATEMENT.md** | License/usage info for HarmThoughts, AdvBench, all 4 models, and text encoders |
| **openreview_metadata.json** | Title, abstract, keywords, ethical considerations, formatting spec |

**Anonymization verified:**
- No `/root/autodl-tmp/` paths (replaced with `DATA_DIR`/`MODEL_DIR` env vars)
- No API keys, tokens, passwords, emails, or author names
- No `.git/`, `__pycache__/`, or `.pyc` files
- No wandb project/entity references
- HF mirror URLs commented out

---
