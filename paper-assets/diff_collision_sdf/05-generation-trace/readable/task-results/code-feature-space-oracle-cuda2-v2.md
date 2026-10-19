# code feature space oracle cuda2 v2

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_feature_space_oracle_cuda2_v2_20260522T201817_result.json`
- **Structured JSON:** [`abffdde3b1faee1a678e.json`](../../sessions/ab/abffdde3b1faee1a678e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Process alive (PIDs 181486, 181492, 186100). The torch.compile first-run compilation is in progress — this is normal and can take several minutes before the first episode log appears.

**Summary:**

- **11/11 patches applied** to `eval_safelibero.py` — added `query_gt_sdf_differentiable`, `_refine_action_feature_oracle`, `--feature_oracle` CLI flag, chunk_timestep tracking, feature oracle branch/setup, and output config
- **Syntax verified** (`py_compile` passed)
- **Launched on GPU 2** (8586 MiB in use) in tmux session `oracle_feature`
- **Registered** as `oracle_true_gt_feature_v11` (status: RUNNING)
- Feature oracle initialization confirmed in log: suffix_out hook registered, norm stats loaded (mean/std correct), GT SDF loaded (4084 points)
- Currently in `torch.compile` phase — first episode results will appear after compilation completes

---
