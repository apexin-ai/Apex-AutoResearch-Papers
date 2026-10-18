# deploy smolvla westd38929 gpu3 v3

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_smolvla-westd38929-gpu3-v3_20260521T172023_result.json`
- **Structured JSON:** [`9ba0e361383b573ee37d.json`](../../sessions/9b/9ba0e361383b573ee37d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。

**1. OpenVLA L2norm k=0.3 seed43 SR = 25.0% (125/500)**
- seed42 也是 25.0%，两个种子完全一致，确认 k=0.3 下 L2norm 表现稳定

**2. SmolVLA L2norm k=0.95 seed43 — PID 425135, RUNNING**
- 已在 GPU3 上启动，日志显示正在评估 Task 0（前 4 个 episode 全 FAIL，与 seed42 的 0% SR 预期一致）
- Registry: `eval_smolvla_official_l2norm_k095_object_seed43` → RUNNING

---
