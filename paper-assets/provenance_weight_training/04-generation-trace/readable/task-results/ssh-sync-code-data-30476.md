# ssh sync code data 30476

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_sync_code_data_30476_20260517T101945_result.json`
- **Structured JSON:** [`a29427ff5c38bbf5431b.json`](../../sessions/a2/a29427ff5c38bbf5431b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All checks pass. Here's the summary:

## Sync Report: westd-41312 → westd-30476

| Item | Status | Details |
|------|--------|---------|
| **Code sync** | SUCCESS | 7 .py, 25 .sh, training/ (18 files), scripts/ (51 files), + analysis/, detector/, evaluation/, etc. |
| **Data sync** | SUCCESS | 13 jsonl files, 11GB total. `scored_data.jsonl`: 371,499 lines. `mixed_data_60.jsonl` re-synced after truncation (896M, 371,499 lines). |
| **Model sync** | SUCCESS | Qwen3-0.6B (1.5G), Llama-3.2-3B (6.8G), ModernBERT-base |
| **Dry-run** | SUCCESS | `pretrain_weighted.py --help` parses OK |
| **Output dir** | `/root/autodl-tmp/provenance_weight_training/output/` | Symlinked from project dir. 241GB available on `/dev/md0`. |
| **GPUs** | 4x NVIDIA RTX PRO 6000 Blackwell (98GB VRAM each) | |

**Additional setup done:**
- Moved data to `/root/autodl-tmp` (250GB disk) to avoid filling the 30GB overlay; created symlinks matching 41312's layout
- Set up SSH key auth from 30476 → 41312 for future transfers

**No blockers.**

---
