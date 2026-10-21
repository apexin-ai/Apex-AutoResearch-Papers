# audit deploy westd27271 attn k05

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_deploy_westd27271_attn_k05_20260526T155524_result.json`
- **Structured JSON:** [`18a8b882334361cd3dc3.json`](../../sessions/18/18a8b882334361cd3dc3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

验证通过。新进程 PID 397225 在 GPU 1 上占用 16169 MiB，log 显示 attention pruning 已激活（256→128 tokens）。

```
DEPLOYED: yes
EXP_TYPE: attn_k05_long
SERVER: westd-27271
GPU: cuda:1
PID: 397225
VERIFY: GPU memory occupied (16169 MiB) + log producing output (Attn Pruning 256->128 active, Task 1/10 running)

NOTE: attn_k05_goal 已完成（SR=0.4420, 221/500），无需再跑
```

---
