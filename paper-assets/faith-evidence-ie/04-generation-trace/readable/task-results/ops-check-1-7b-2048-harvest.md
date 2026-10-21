# ops check 1 7b 2048 harvest

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check_1_7b_2048_harvest_20260519T192518_result.json`
- **Structured JSON:** [`7b8e548d2d823043ebcc.json`](../../sessions/7b/7b8e548d2d823043ebcc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

The 2048 eval is **still running** — at batch 216/247 (87%). The log is at a different path, and no metrics.json yet because it hasn't finished.

**Progress**: 216/247 batches (87.4%)
- Speed: ~80-85s/batch (2x slower than 1024 version, expected)
- Remaining: 31 batches × ~83s ≈ **43 minutes**
- Last logged batch timestamp: 4:36:47 elapsed

The process PID 702837 is the parent shell; the actual Python child is doing the GPU work on cuda:3.

## Summary

| Item | Value |
|------|-------|
| **Status** | Running, 87% complete |
| **ETA** | ~43 min from last log entry |
| **Log** | `/root/autodl-tmp/eval_outputs/eval_1_7b_rsft_no_evidence_2048.log` |
| **Output dir** | `/root/autodl-tmp/eval_outputs/eval_1_7b_rsft_no_evidence_2048/` |
| **Note** | Registry entry for `plan019_1_7b_rsft_no_evidence_eval_2048` does not exist yet — needs to be created when harvesting results |

---
