# ops check sft unpruned and alpha

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-sft-unpruned-and-alpha_20260516T001645_result.json`
- **Structured JSON:** [`52f260830351aadcb26f.json`](../../sessions/52/52f260830351aadcb26f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry updated. Here's the summary:

## Part A: sft_unpruned_baseline (westd cuda:1)
**Status: DONE** ✓

| Metric | Value |
|--------|-------|
| Final loss | 0.3321 |
| Final token_accuracy | 0.909 |
| Avg train loss | 0.4253 |
| Total steps | 1870/1870 (2 epochs) |
| Runtime | 31m48s (1908s) |
| Checkpoint | 14.2GB @ `/root/autodl-tmp/recovery_aware_struct_prune/sft_unpruned_baseline/` |

**N=100 eval launched** → PID 71116 on westd cuda:1 (running, ~15-20min to complete)

## Part B: α sweep + v9 (westb cuda:0)
**α sweep: DONE** ✓ — All 5 alphas complete (cal=512, sparsity=20%, N=100 greedy):

| α | Accuracy | EOS rate | Avg length |
|---|----------|----------|------------|
| 0.0 | **27%** | 0.80 | 1192 |
| 0.25 | **23%** | 0.63 | 1834 |
| 0.5 | **22%** | 0.81 | 1141 |
| 1.0 | **31%** | 0.92 | 733 |
| 2.0 | **36%** | 0.59 | 2130 |

Pattern: non-monotonic, α=2.0 best (36%), α=0.5 worst (22%). Higher α → stronger CKA penalty → better reasoning retention at this sparsity. α=1.0 has best EOS discipline (0.92).

**GRPO RASP v9: RUNNING** — Auto-launcher triggered successfully at 08:04 UTC.
- PID 566666, wandb run `mrikafz3` (`grpo_stage2_rasp_20_v9`)
- Config: 30 steps, lr=1e-6, dapo loss, temp=0.4
- Progress: step 1/30 (~7min/step → ETA ~3.5h from launch, ~11:30 UTC)

---
