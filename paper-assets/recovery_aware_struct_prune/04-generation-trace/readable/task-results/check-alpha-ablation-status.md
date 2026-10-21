# check alpha ablation status

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_alpha_ablation_status_20260516T205940_result.json`
- **Structured JSON:** [`310101229379e6398f0f.json`](../../sessions/31/310101229379e6398f0f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Alpha Ablation Phase B Status

### 1. SFT Checkpoint Status

| α | SFT | Eval | Accuracy |
|---|-----|------|----------|
| 0.0 | ✅ done (03:56) | ✅ done (04:07) | **70.0%** |
| 0.3 | ✅ done (04:39) | ✅ done (04:49) | **73.0%** |
| 0.5 | 🔄 training on cuda:3 | pending | — |
| 0.7 | pending | pending | — |
| 1.0 | pending | pending | — |
| 2.0 | ✅ done (05:00) | 🔄 running on cuda:0 | — |

### 2. Currently Running

- **cuda:0**: Evaluating α=2.0 (pid 46908, started 05:00). After this → SFT α=1.0 → eval α=1.0
- **cuda:3**: Training α=0.5 SFT — **step 624/1870 (33%)**, ~1.05 it/s, ~20 min remaining. After this → eval 0.5 → SFT 0.7 → eval 0.7 (then redundantly redoes 1.0, 2.0)

### 3. Eval Results So Far

- **α=0.0**: 70.0% (140/200), stderr=0.032
- **α=0.3**: 73.0% (146/200), stderr=0.031

α=0.3 recovers **3 percentage points** more than standard pruning (α=0.0). Good early signal.

### 4. cuda:2 Status

**Not idle** — 2 processes running (pids 33921, 34032) using ~34 GB total.

### 5. Estimated Completion

- **cuda:0 finishes all its work** (eval 2.0 + SFT/eval 1.0): ~05:50 UTC
- **cuda:3 finishes unique work** (SFT/eval 0.5 + SFT/eval 0.7): ~06:10 UTC
- **All 6 alphas with eval results**: ~**06:10 UTC** (~1 hour from now)

Note: cuda:3's loop will redundantly redo α=1.0 and α=2.0 after finishing α=0.7, running until ~07:30. Those are wasted cycles since cuda:0 will have already completed them. Could kill the loop after α=0.7 to free cuda:3.

---
