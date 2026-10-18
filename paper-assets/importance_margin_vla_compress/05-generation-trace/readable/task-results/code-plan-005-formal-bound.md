# code plan 005 formal bound

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_plan_005_formal_bound_20260516T142434_result.json`
- **Structured JSON:** [`0909622a8ec5bf38d909.json`](../../sessions/09/0909622a8ec5bf38d909.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Job is running — loading SmolVLA model from HuggingFace cache. 

**Summary:**

1. **Script written**: `eval_formal_bound.py` — complete formal bound verification implementing:
   - Lipschitz constant estimation (spectral norm product + empirical via perturbation)
   - Top-k stability measurement across 5 ε levels (0.005, 0.01, 0.02, 0.05, 0.1)
   - Perturbation applied directly to visual tokens (ACIS input), not raw images
   - Theoretical bound comparison: P(Δ_k > 2·L·ε) as stability lower bound
   - Margin distribution statistics + tightness ratio reporting
   - JSON output for plotting

2. **Script location**: 
   - Local: `/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/eval_formal_bound.py`
   - Server: `/root/autodl-tmp/importance_margin_vla_compress/eval_formal_bound.py`

3. **Job submitted**: `plan_005_formal_bound` on westd-27271 cuda:0, using checkpoint `checkpoints/imm_anchor_v8b_twostage/final/checkpoint.pt` with config `configs/imm_anchor_v8b_twostage.yaml`. Currently loading model.

---
