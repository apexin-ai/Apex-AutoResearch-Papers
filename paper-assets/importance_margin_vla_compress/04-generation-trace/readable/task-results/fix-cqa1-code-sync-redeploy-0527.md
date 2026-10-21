# fix cqa1 code sync redeploy 0527

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_cqa1_code_sync_redeploy_0527_20260527T012958_result.json`
- **Structured JSON:** [`492cb71773057329af2c.json`](../../sessions/49/492cb71773057329af2c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All 3 experiments running successfully:

| GPU | exp_id | Mode | Status |
|-----|--------|------|--------|
| 0 | `eval_openvla_random_k095_goal_seed42` | Random k=0.95 | Running, 256→243 tokens |
| 1 | `eval_openvla_attn_k095_goal_seed42` | Attn k=0.95 | Loading model from openvla-libero-goal |
| 3 | `eval_openvla_attn_k05_goal_seed42_v3` | Attn k=0.5 | Running, 256→128 tokens |

All 5 steps complete:
1. Killed 3 invalid processes (834190, 832020, 876797) + stale 895742
2. Synced correct eval script (OpenVLAForActionPrediction + transformers 4.40.1) to cqa1
3. Verified: 425 lines, correct imports, openvla_deps, fixed SUITE_MODEL_MAP for libero_goal
4. Deployed 3 experiments on GPU 0/1/3
5. Verified all running with correct pruning hooks active

---
