# diagnose 8h long running

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_8h_long_running_20260526T135542_result.json`
- **Structured JSON:** [`21990f9431a9f4788ecf.json`](../../sessions/21/21990f9431a9f4788ecf.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
EXP: eval_openvla_attn_k07_object_seed42_v2
SERVER: westd-41074 cuda:2
PID: DEAD
GPU_UTIL: 68% (but PID gone — GPU used by other process)
PROGRESS: Task 7/10, Ep 30/50 — crashed mid-evaluation
VERDICT: dead
SR_SO_FAR: 40.0% (6 tasks: .380/.120/.660/.300/.620/.320)

EXP: eval_openvla_random_k085_long_seed42_v3
SERVER: westd-41074 cuda:0
PID: alive (uptime 09:14:44, CPU 930%)
GPU_UTIL: 79%
PROGRESS: Task 10/10, Ep 30/50 — last task, 60% done
VERDICT: normal_running
SR_SO_FAR: 48.7% (9 tasks: .660/.560/.660/.340/.220/.780/.200/.660/.300)
EST_REMAINING: ~22 min (20 eps left @ 0.9 eps/min)

EXP: eval_openvla_random_k05_long_seed42_v2
SERVER: westd-38929 cuda:1
PID: alive (uptime 08:52:58, CPU 849%)
GPU_UTIL: 69%
PROGRESS: Task 9/10, Ep 40/50 — then 1 more task
VERDICT: normal_running
SR_SO_FAR: 21.5% (8 tasks: .300/.260/.220/.020/.060/.440/.260/.160)
EST_REMAINING: ~75 min (10 eps Task 9 + 50 eps Task 10 @ 0.8 eps/min)
```

```
SUMMARY:
- Normal: eval_openvla_random_k085_long_seed42_v3 (~22min left), eval_openvla_random_k05_long_seed42_v2 (~75min left)
- Dead (need rerun): eval_openvla_attn_k07_object_seed42_v2 (crashed at Task 7/10 Ep 30/50, PID gone)
```

---
