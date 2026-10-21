# deploy eval openvla random k05 object seed42

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_eval_openvla_random_k05_object_seed42_20260526T154442_result.json`
- **Structured JSON:** [`bad0b53b486b8b197995.json`](../../sessions/ba/bad0b53b486b8b197995.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

This experiment already has a completed result. The registry shows a previous successful run: **Random k=0.5 Object SR=35.8%** with full per-task breakdown:

| Task | SR |
|------|-----|
| alphabet_soup | 56% |
| bbq_sauce | 58% |
| butter | 0% |
| chocolate_pudding | 30% |
| cream_cheese | 2% |
| ketchup | 60% |
| milk | 12% |
| orange_juice | 74% |
| salad_dressing | 40% |
| tomato_sauce | 26% |

The registry status is DONE/failed only because a retry attempt failed (server unreachable), but the original run completed successfully with SR=35.8%.

**Summary:**

```
ATTN_K05_OBJ_STATUS: running (Task 4/10, Ep 30/50, ~36% done, ETA ~4h)
RANDOM_K05_OBJ: already completed — SR=35.8% (179/500)
DEPLOYED: no (not needed — data already exists)
SERVER: westd-41074
GPU1: occupied by Attn k=0.5 Object (PID 652888)
GPU2: free
EXP_ID: eval_openvla_random_k05_object_seed42
```

Random Object cliff curve is now complete: k=0.9=62.8%, k=0.7=44.4%, **k=0.5=35.8%**. No re-deployment needed unless you want to verify the result. Want me to fix the registry status back to DONE/success instead?

---
