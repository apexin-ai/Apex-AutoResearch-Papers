# code activation collection v3

**Meta-Brain: Perturbation-Diagnostic Routing of LoRA Experts for Parameter-E cient VLA Robustness** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_activation_collection_v3_20260516T223034_result.json`
- **Structured JSON:** [`2301d3fbcbaa240824e8.json`](../../sessions/23/2301d3fbcbaa240824e8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

After warmup, throughput jumped to ~20 samples/sec. ETA ~55 minutes, 0 errors. Collection is running successfully.

**Summary:**

1. **Script was already mostly correct** — previous Worker had already fixed:
   - `suppress_errors = False`
   - Layer path: `paligemma_with_expert.paligemma.model.language_model.layers.6`
   - Uses `policy.infer(obs_dict)` pattern with `OpenPIMetaBrainPolicy`

2. **Fix applied**: Changed `policy_wrapper.policy.infer(obs_dict)` → `policy_wrapper.infer(obs_dict)` for full consistency with eval pipeline.

3. **Dry run passed**: 5/5 samples, activation shape (2048,), all 2048 elements non-zero, 0 errors.

4. **Full collection running**: PID 274941, processing 66984 frames on cuda:2, ~20 samples/sec steady state, ETA ~55 min. Output: `/root/autodl-tmp/activations_v3/activations.pt`

---
