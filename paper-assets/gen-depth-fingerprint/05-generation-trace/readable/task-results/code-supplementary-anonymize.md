# code supplementary anonymize

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_supplementary-anonymize_20260517T211543_result.json`
- **Structured JSON:** [`89dd6ef67e13fca7e8ae.json`](../../sessions/89/89dd6ef67e13fca7e8ae.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Done. Here's a summary:

**Anonymization**: All 26 `.py` files and README are clean. No `/root/`, `/home/ubuntu/`, wandb, autodl, API keys, or author info found in the zip.

**New scripts added** (6 files from server, anonymized):
| File | Anonymization fix |
|------|------------------|
| `prepare_downstream_data.py` | Default paths changed to `../data/`; removed duplicate buggy `save_jsonl` |
| `finetune_downstream.py` | Removed `/root/autodl-tmp/...` from docstring usage example |
| `bootstrap_downstream_ci.py` | `BASE` path changed from `/root/autodl-tmp/...` to `experiments/downstream` |
| `end_to_end_classifier.py` | Removed internal experiment name from output dir; generalized output path |
| `cross_temp_transfer.py` | Already clean (uses `__file__`-relative paths); adjusted DATA_DIR to `../data` |
| `distributional_tests.py` | `DATA_PATH` and `OUT_PATH` changed from `/root/gen-depth-fingerprint/...` to relative |
| `scripts/tost_equivalence.py` | Output path changed from `/root/gen-depth-fingerprint/...` to `results/` |

**README updated**: Added data format docs, full script reference with appendix mappings, downstream utility section, requirements section.

**Package**: `supplementary.zip` = **76 KB**, 32 files (26 `.py` + 1 `.md` + 1 `.txt` + 4 dirs).

---
