# code exp 001b qwq 32b

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp_001b_qwq_32b_20260516T215746_result.json`
- **Structured JSON:** [`5ed3ee4a6241288b363e.json`](../../sessions/5e/5ed3ee4a6241288b363e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All 5 phases of exp_001b are complete. Here's the summary:

## Results

**Phase 1 - Extraction**: 95 QwQ-32B traces extracted (4,852 steps, 64 layers, hidden_dim=5120). 3.18 GB total. Zero errors.

**Phase 2 - Layer Sweep**: Best layers are **early (0-6)**, not middle layers like R1-8B (layer 14). Best: layer 1 with acc=0.737, crossing_rate=47.4%, lead_mean=16.3 steps.

**Phase 3 - Temporal LR**: Window=10 achieves best lead_mean=21.9 steps, crossing_rate=42.1%.

**Phase 4 - GRU 3-seed**: Acc=0.713 +/- 0.005, crossing_rate=63.2% +/- 12.9%, lead_mean=12.4 +/- 0.75.

**Phase 5 - Bootstrap**: HS probe pre-CP FPR (0.164) significantly lower than text baseline (0.312), p=0.001.

## Key Finding vs R1-8B

QwQ-32B has **lower accuracy** (~73% vs 81%) but **dramatically better lead times** (16-22 steps vs ~0 for R1-8B) and higher crossing rates. The signal concentrates in very early layers (0-6) rather than middle layers, suggesting a different encoding strategy for safety-relevant representations. The bootstrap test confirms HS probes provide significantly earlier detection than text baselines.

---
