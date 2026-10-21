# deploy eval openvla attn k07 object seed42 v3

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_eval_openvla_attn_k07_object_seed42_v3_20260526T135917_result.json`
- **Structured JSON:** [`79d875a55dac0b07f64f.json`](../../sessions/79/79d875a55dac0b07f64f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**v2 还活着且在进步。** 日志刚更新（21:57:54），当前在 Task 7 Ep 40/50 — 已经跑过了之前 v1/v2 崩溃的位置。

cuda:2 被 v2 (PID 542010) 占满，无法部署 v3。两个选项：

1. **等 v2 跑完** — 它已过了之前的崩溃点，可能会完整跑完 10 个 Task，这样就不需要 v3 了
2. **杀 v2 部署 v3** — 但 v2 已有 6 个完整 Task 结果 + Task 7 进行中，杀掉会浪费

建议等 v2 跑完。要杀掉部署 v3 还是等？

---
