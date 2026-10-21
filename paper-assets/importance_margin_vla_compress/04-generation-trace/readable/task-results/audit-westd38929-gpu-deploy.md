# audit westd38929 gpu deploy

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_westd38929-gpu-deploy_20260524T041306_result.json`
- **Structured JSON:** [`3c63f8984b13fafe8ebb.json`](../../sessions/3c/3c63f8984b13fafe8ebb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

GPU 2 实验已注册为 RUNNING。

## 当前 GPU 状态汇总

| GPU | 实验 | PID | 状态 |
|-----|------|-----|------|
| 0 | eval_xvla_random_k085_long_seed42 | 316570 | 运行中（不动） |
| 1 | eval_xvla_l2norm_k07_spatial_seed42_v2 | 367301 | 运行中（不动） |
| 2 | eval_xvla_l2norm_k05_long_seed42_v3 | 447347 | **刚部署**，已开始评估（Ep 1 SUCCESS） |
| 3 | — | — | **空闲** |

## GPU 3 说明

**不需要重新部署 eval_xvla_l2norm_k03_goal_seed42_v4**。v3 和 v4 都已成功完成（EXIT_CODE=0），结果完全一致：
- **Overall SR: 37.6% (188/500)**，95% Wilson CI: [33.5%, 41.9%]
- 最强 task: Task 4 (98%), Task 1 (94%), Task 8 (80%)
- 最弱 task: Task 5 (0%), Task 9 (0%), Task 6 (2%)

v3 之前 registry 标记为 failed 是误判（"process dead 5× with no sentinel/W&B — auto-resolved as failed"），实际日志显示正常完成。GPU 3 现在空闲，可以安排其他实验。

---
