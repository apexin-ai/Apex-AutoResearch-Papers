# code eval script fix d008

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_eval-script-fix-d008_20260513T000154_result.json`
- **Structured JSON:** [`0a2e586c519619cab35d.json`](../../sessions/0a/0a2e586c519619cab35d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All 3 files are byte-for-byte identical between both servers:

| File | MD5 | Lines | Bytes |
|------|-----|-------|-------|
| `eval_repo_cls.py` | `5748c837cd2a8a2d83ab4d90b50f622f` | 307 | 11551 |
| `eval_repo_cwm.py` | `4fc9808182f003ac2d7a5e23bcbf7e57` | 339 | 13163 |
| `paired_bootstrap_repo.py` | `d9073b9399fe471c5abfaece2a438227` | 229 | 9052 |

All 3 fixes complete:
- **Fix #1**: `max_seq_length` default changed from 4096 to 2048 in both `eval_repo_cls.py` and `eval_repo_cwm.py`
- **Fix #2**: Truncation tracking breakdown added to `eval_repo_cwm.py` summary JSON (`truncated_count`, `truncated_pct`, `truncated_accuracy`, `non_truncated_accuracy`)
- **Fix #3**: All 3 scripts synced to seetacloud-westd-4x5090 — MD5 hashes match, syntax verified

---
