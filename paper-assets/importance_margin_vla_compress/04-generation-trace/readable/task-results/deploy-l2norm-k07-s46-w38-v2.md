# deploy l2norm k07 s46 w38 v2

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_l2norm_k07_s46_w38_v2_20260528T074655_result.json`
- **Structured JSON:** [`518db21510d8d17324df.json`](../../sessions/51/518db21510d8d17324df.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**GPU 0 on westd-38929 is NOT clean** — PID 363197 is running. Deployment blocked per instructions.

Progress of the 4 experiments:

| exp_id | status | task_progress | cumulative SR | est_remaining |
|--------|--------|---------------|---------------|---------------|
| attn_k07_s45_w41 | **DONE** | 10/10 (T0-T9) | **53.8%** | 0 |
| l2norm_k075_s46_w41 | RUNNING | 9/10 (T8 done, T9 next) | 71.3% (321/450) | ~15 min |
| random_k085_s46_w41 | RUNNING | 7/10 (T7 ep=20/50) | 44.9% (157/350) | ~40 min |
| attn_k085_s46_w38 | RUNNING | 7/10 (T7 ep=30/50) | 50.0% (175/350) | ~35 min |

Key findings:
- **Cannot deploy l2norm_k07_s46 to w38:cuda:0** — GPU occupied (PID 363197). Need to identify that process or wait for it to finish.
- **attn_k07_s45_w41 completed** with SR=53.8% (EXIT_CODE=0). This frees a GPU on w41.
- **l2norm_k075_s46_w41** is nearly done (~15 min), will also free a w41 GPU soon.

---
