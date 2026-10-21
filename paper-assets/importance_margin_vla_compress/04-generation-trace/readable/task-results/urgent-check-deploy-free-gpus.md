# urgent check deploy free gpus

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_urgent_check-deploy-free-gpus_20260524T023203_result.json`
- **Structured JSON:** [`d394c0fa5e8b5dd5a49b.json`](../../sessions/d3/d394c0fa5e8b5dd5a49b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 状态机限制，无法完成后两个的 RUNNING 转换。实验本身已正常运行，cron 监控会自动跟踪。

## 部署总结

| 实验 | 服务器 | GPU | PID | tmux session | 状态 |
|------|--------|-----|-----|-------------|------|
| eval_xvla_l2norm_k03_goal_seed42_v3 | westd-38929 | 2 | 16447 | eval_xvla_l2norm_k03_goal_seed42_v3 | RUNNING, 模型已加载, Task 0 进行中 |
| eval_xvla_l2norm_k07_goal_seed42_v2 | westd-38929 | 3 | 16590 | eval_xvla_l2norm_k07_goal_seed42_v2 | RUNNING, 已评估 Ep 1 SUCCESS |
| eval_pi05_l2norm_k085_spatial_seed42 | cqa1-33015 | 3 | 723020 | eval_pi05_l2norm_k085_spatial_seed42 | RUNNING, 模型加载中 |

**收割的结果：**
- π0.5 L2norm k=0.85 Goal seed42: **SR=88.2%**
- π0.5 L2norm k=0.85 Goal seed43: **SR=87.0%**

---
