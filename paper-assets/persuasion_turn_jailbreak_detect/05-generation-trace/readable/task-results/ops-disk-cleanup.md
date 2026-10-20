# ops disk cleanup

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_disk-cleanup_20260517T163118_result.json`
- **Structured JSON:** [`743edf5aae71a3f538ee.json`](../../sessions/74/743edf5aae71a3f538ee.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
=== Disk Cleanup Report ===
Before: 26 GB used / 30 GB total (86% usage)
After:  24 GB used / 30 GB total (79% usage)
Freed:  ~2.1 GB

Deleted items:
- checkpoints/treatment_dryrun/:  1.4 GB
- checkpoints/pilot_deberta/:     710 MB
- checkpoints/pilot_gru/:         23 MB
- checkpoints/baseline_gru/:      12 MB
- data/embeddings/baseline_*.pt:  11.2 MB
- data/pilot/:                    6 MB
- data/generated/benign_v4b*.jsonl: 874 KB
- data/mock*.jsonl:               95 KB

Preserved (verified):
- crescendo_all.jsonl: OK (250 lines)
- crescendo_part1.jsonl: OK (2.9M)
- crescendo_part2.jsonl: OK (2.8M)
- benign_v4c_full_gpu0.jsonl: 115 lines (idle)
- benign_v4c_full_gpu2.jsonl: 115 lines (idle)
- src/, scripts/, taxonomy/: untouched

⚠️ Note: Generation processes are NOT running — no python processes found. The v4c files appear idle (last modified ~00:31).
```

---
