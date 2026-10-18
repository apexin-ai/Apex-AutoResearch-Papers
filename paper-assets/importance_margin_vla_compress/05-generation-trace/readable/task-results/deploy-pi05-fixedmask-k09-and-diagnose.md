# deploy pi05 fixedmask k09 and diagnose

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_pi05-fixedmask-k09-and-diagnose_20260521T195603_result.json`
- **Structured JSON:** [`cf2e1f0d27000ddcec4c.json`](../../sessions/cf/cf2e1f0d27000ddcec4c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

模型正在加载中，GPU1 尚未分配显存（正常启动行为）。

**总结：**

**Part 1 — seed43 诊断完成：**
- PID 531274 已退出，eval 正常完成
- **Overall SR = 9.6%** (48/500)，与 seed42 的 12% 一致，确认 random k=0.9 的性能退化可复现
- Registry `eval_pi05_random_k09_object_seed43` → DONE (success)，metrics 已记录

**Part 2 — fixed-mask 已部署：**
- PID 625841 在 westd-41074 GPU1 启动，模型加载中
- Registry `eval_pi05_random_k09_fixedmask_object_seed42` → RUNNING
- 预计运行 ~2h，结果将判别 temporal consistency 假说：
  - fixed-mask 恢复 ~90%+ → per-call stochastic mask 是根因
  - fixed-mask 仍 ~10% → random 90% subset 本身信息不够

---
