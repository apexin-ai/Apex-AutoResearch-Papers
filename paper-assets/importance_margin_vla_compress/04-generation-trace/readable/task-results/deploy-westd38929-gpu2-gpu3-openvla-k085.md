# deploy westd38929 gpu2 gpu3 openvla k085

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_westd38929_gpu2_gpu3_openvla_k085_20260524T205856_result.json`
- **Structured JSON:** [`e6428fb5e033c29382e2.json`](../../sessions/e6/e6428fb5e033c29382e2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

```
Kill: PID 756339 [killed] — L2norm k=0.3 seed43 冗余
GPU2: eval_openvla_attn_k085_goal_seed42, PID=860471, registry=RUNNING
GPU3: eval_openvla_attn_k085_spatial_seed42, PID=861122, registry=RUNNING
```

westd-38929 四卡全满：GPU0/1 跑 k=0.9/k=0.85 Object，GPU2/3 跑 k=0.85 Goal/Spatial。

---
