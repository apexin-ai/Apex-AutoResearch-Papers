# verify attn k05 goal and w41074 gpu2

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_verify_attn_k05_goal_and_w41074_gpu2_20260526T160706_result.json`
- **Structured JSON:** [`e3a2cd299ca5cc10dc36.json`](../../sessions/e3/e3a2cd299ca5cc10dc36.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果已验证。

```
ATTN_K05_GOAL_VERIFY:
  VALID: yes
  SR: 44.2% (221/500)
  TOTAL_EPISODES: 500
  MODE: attention_prune, k_ratio=0.5, suite=libero_goal
  SEED: 42
  RESULT_FILE: /root/autodl-tmp/importance_margin_vla_compress/eval_results/openvla_attention_prune_k05_goal_seed42.json
  TIMESTAMP: 2026-05-24 19:11:55
  ELAPSED: 264.5 min
  PER_TASK:
    open the middle drawer of the cabinet:        14% (7/50)
    put the bowl on the stove:                    56% (28/50)
    put the wine bottle on top of the cabinet:    70% (35/50)
    open the top drawer and put the bowl inside:  10% (5/50)
    put the bowl on top of the cabinet:           62% (31/50)
    push the plate to the front of the stove:     66% (33/50)
    put the cream cheese in the bowl:             38% (19/50)
    turn on the stove:                            80% (40/50)
    put the bowl on the plate:                    32% (16/50)
    put the wine bottle on the rack:              14% (7/50)

WESTD-41074:
  GPU0: BUSY (15980/97887 MiB, 71%, PID 682346)
  GPU1: BUSY (15980/97887 MiB, 63%, PID 652888)
  GPU2: IDLE (1/97887 MiB, 0%, no process)
  GPU3: BUSY (15984/97887 MiB, 71%, PID 642262)
```

---
