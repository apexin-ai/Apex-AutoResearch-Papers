# deploy westd27271 gpu1 openvla

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy-westd27271-gpu1-openvla_20260524T010056_result.json`
- **Structured JSON:** [`8156b7c598407ada796e.json`](../../sessions/81/8156b7c598407ada796e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

部署完成。

**已部署**: `eval_openvla_random_k05_goal_seed42` on westd-27271 GPU 1 (PID 500676)
- 模式: Random pruning, k=0.5, libero_goal, seed 42
- 模型: openvla-7b-finetuned-libero-goal (256→128 vision tokens)
- 日志: `/root/runs/importance_margin_vla_compress/eval_openvla_random_k05_goal_seed42.log`
- 已进入 Task 1/10 评估，运行正常
- GPU 0 实验 (PID 486402, L2norm k=0.5 Goal) 未受影响

Registry 已更新为 RUNNING。参考 L2norm k=0.5 Goal v3 的结果（~5h 完成 10 tasks），预计本实验也需约 5 小时。

---
