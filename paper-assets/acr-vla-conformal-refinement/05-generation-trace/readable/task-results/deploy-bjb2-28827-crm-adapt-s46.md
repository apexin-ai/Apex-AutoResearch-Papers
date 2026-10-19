# deploy bjb2 28827 crm adapt s46

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_bjb2-28827-crm-adapt-s46_20260524T071104_result.json`
- **Structured JSON:** [`17b962ea122cb37637ef.json`](../../sessions/17/17b962ea122cb37637ef.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇总：

**GPU 0 — CRM eval**: 已在运行。tmux session `eval-supp-crm-norm005-spatial-s46` 已存在，PID 121241 在 GPU 0 上 (6287 MiB)。无需再操作。

**GPU 1 — Adaptive eval**: 无法启动。GPU 1 被一个 nohup 的 OpenVLA object eval 占用（`openvla_eval.py --benchmark object --mode vla_only --seed 42`，PID 114990, 19121 MiB），目前才在 task 1/10 rollout 5/20，预计还要跑几个小时。

Registry 中 `eval-supp-adapt-tau025-spatial-s46` 已标记 RUNNING 但实际没有 tmux session。

需要你决定：
1. **等** GPU 1 上的 object eval 跑完后再启动 adaptive eval
2. **kill** 掉 object eval（PID 114990）腾出 GPU 1 立即部署

---
