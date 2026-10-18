# deploy westd41074 goal l2norm k05

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_westd41074_goal_l2norm_k05_20260522T154559_result.json`
- **Structured JSON:** [`a9aefc02d0b7c058ff40.json`](../../sessions/a9/a9aefc02d0b7c058ff40.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

GPU 还没上，但进程在跑（PID 723360，16.8GB RAM，CPU 345%），说明 π0.5 正在 CPU 加载阶段，`.to(cuda:1)` 还没执行。这是正常的——π0.5 模型很大，CPU 加载要几分钟。

部署完成：
- **实验**: `eval_pi05_l2norm_k05_goal_seed42`
- **服务器**: westd-41074, cuda:1
- **进程**: PID 723360，已启动，CPU 加载模型中
- **Registry**: RUNNING
- **日志**: `/root/autodl-tmp/importance_margin_vla_compress/logs/eval_pi05_l2norm_k05_goal_seed42.log`
- **其他 GPU 未动**: cuda:0 (3 MiB), cuda:2 (10.7GB, 43%), cuda:3 (27.5GB, 0%) 均维持原状

模型上 GPU 后 cuda:1 内存会升到 ~20-30GB。

---
