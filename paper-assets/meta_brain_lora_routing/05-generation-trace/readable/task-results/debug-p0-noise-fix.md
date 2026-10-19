# debug p0 noise fix

**Meta-Brain: Perturbation-Diagnostic Routing of LoRA Experts for Parameter-E cient VLA Robustness** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_debug_p0_noise_fix_20260516T212831_result.json`
- **Structured JSON:** [`ac7c0b337f899d472ca9.json`](../../sessions/ac/ac7c0b337f899d472ca9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

3 determinism verification runs are now executing on cuda:0. I'll check back in ~3 minutes to see if the first run has completed.

**Fix applied so far:**
1. Added `torch.backends.cudnn.deterministic = True` and `torch.backends.cudnn.benchmark = False` at module level (lines 39-40)
2. Added `torch.manual_seed(seed)` and `torch.cuda.manual_seed_all(seed)` in `run_episode` (lines 205-206), right after the existing `random.seed(seed)` / `np.random.seed(seed)` calls

This ensures `sample_noise` (which uses `torch.normal()`) produces identical noise for the same episode seed across runs.

---
