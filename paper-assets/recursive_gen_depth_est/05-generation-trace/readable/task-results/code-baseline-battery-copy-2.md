# code baseline battery

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_baseline_battery_20260514T185551_result.json`
- **Structured JSON:** [`4a78e19a3e369d337edc.json`](../../sessions/4a/4a78e19a3e369d337edc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All dry-runs passed. Summary:

| Baseline | Status | Key output |
|----------|--------|------------|
| 1. DivEye OVR | Pass | Acc=0.672, d0_vs_d1 AUC=0.974 |
| 2a. PPL Ridge | Pass | Acc=0.421 |
| 2b. PPL Ordinal | Pass | Acc=0.698, macro-AUC=0.89 |
| 3. CORAL DeBERTa | Pass | "Dry run complete (2 steps). Pipeline OK." |
| 4. CE DeBERTa | Pass | "Dry run complete (2 steps). Pipeline OK." |
| 5. Zero-shot LLM | Pass | Import OK (no API key needed) |

All 6 scripts written locally and synced to server at `/root/autodl-tmp/recursive_gen_depth_est/scripts/`. The `.float()` fix was applied for baselines 3-4 to handle fp16 model weights on CPU. DeBERTa model weights also downloaded to `/root/autodl-tmp/models/deberta-v3-base/`.

---
