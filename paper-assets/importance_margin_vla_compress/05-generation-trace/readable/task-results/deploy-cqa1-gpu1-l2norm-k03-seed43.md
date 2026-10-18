# deploy cqa1 gpu1 l2norm k03 seed43

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_cqa1-gpu1-l2norm-k03-seed43_20260521T220718_result.json`
- **Structured JSON:** [`9ca5f833ee4381273623.json`](../../sessions/9c/9ca5f833ee4381273623.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇总

1. **Killed** GPU1 原进程 (PID 720036, eval_pi05_l2norm_k05_object_seed43 重复实验)
2. **eval_pi05_l2norm_k03_object_seed43 已有结果**，无需重跑：
   - **SR = 55.4%** (seed42 的 k=0.3 是 51.0%)
   - V-shape 跨 seed 可复现：k=0.3 (55.4%) > k=0.5 (33.6%)，与 seed42 趋势一致
3. **GPU1 当前空闲** (4 MiB)，可部署其他实验

---
