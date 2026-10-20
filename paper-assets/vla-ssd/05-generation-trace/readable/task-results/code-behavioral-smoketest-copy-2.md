# code behavioral smoketest

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_behavioral_smoketest_20260519T034635_result.json`
- **Structured JSON:** [`9efc43129e4dcf189353.json`](../../sessions/9e/9efc43129e4dcf189353.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Job submitted and registry updated. Summary:

**Environment fixes applied:**
- `NUMBA_DISABLE_JIT=1` — fixes robosuite numba/mujoco type mismatch (`can't unbox array from PyObject`)
- `LD_LIBRARY_PATH` includes mujoco package dir — fixes `libmujoco.so.3.1.6` not found
- `transformers` downgraded 5.8.1 → 4.40.2 — OpenVLA needs `AutoModelForVision2Seq` (removed in 5.x)
- `numpy` upgraded 1.24.0 → 2.0.2 — fixes torch/numpy type mismatch in `torchvision.to_tensor()`
- Installed `future`, `matplotlib`, `timm`, `accelerate` (missing deps)

**Script:** `/root/vla-ssd/scripts/behavioral_smoketest.py`
- 1 task (task_id=0: "open the middle drawer of the cabinet") × 3 episodes × baseline
- If baseline SR > 0, automatically runs ablated condition (L1 top-24 heads)
- Ablation hook rewritten for transformers 4.40.2 (patches `LlamaAttention.forward` directly, not `eager_attention_forward`)

**Running in:** tmux session `behavioral_smoketest` on cuda:1
**Log:** `/root/autodl-tmp/vla-ssd/results/behavioral_smoketest.log`
**Results:** `/root/autodl-tmp/vla-ssd/results/behavioral_smoketest.json`

Estimated runtime: ~15-20min (model inference ~0.5s/step × 400 max steps × 3 episodes). Registry: `behavioral_smoketest` status=RUNNING.

---
