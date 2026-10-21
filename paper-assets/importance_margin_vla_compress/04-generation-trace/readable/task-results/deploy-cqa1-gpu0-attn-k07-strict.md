# deploy cqa1 gpu0 attn k07 strict

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_cqa1_gpu0_attn_k07_strict_20260527T123544_result.json`
- **Structured JSON:** [`1495be7a01f7f66c2070.json`](../../sessions/14/1495be7a01f7f66c2070.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

GPU0 is **not free** — it's running π0.5 Attn k=0.75 Long (PID 300492, elapsed 4m44s). All 4 GPUs are occupied.

This is a cascade dependency: k=0.7 needs to wait until one GPU frees up. The k=0.75 job just started ~5 minutes ago and will run ~3h on Long suite.

**Current cqa1 status:**
- GPU0: π0.5 Attn k=0.75 Long (just started)
- GPU1-3: other jobs running

Cannot deploy k=0.7 now. Options:
1. **Wait** for GPU0's k=0.75 job to finish (~3h), then deploy k=0.7
2. **Deploy on another server** if a GPU is available (westd-27271, westd-38929, westd-41074)

Want me to check the other servers for a free GPU, or queue this for after k=0.75 finishes on cqa1?

---
