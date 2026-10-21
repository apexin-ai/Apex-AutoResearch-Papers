# ops metrics extract and deploy

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_metrics_extract_and_deploy_20260522T023715_result.json`
- **Structured JSON:** [`5f963fa816693dc58c81.json`](../../sessions/5f/5f963fa816693dc58c81.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

任务 3 已成功启动。OpenVLA L2norm k=0.5 Object eval 正在运行，正在执行 Task 1/10，vision tokens 从 256 裁剪到 128。

---

## 总结

### 任务 1：4 个实验 registry 已更新为 DONE
| 实验 | SR | 状态 |
|------|-----|------|
| `eval_pi05_random_k085_spatial_seed42` | 58.4% | DONE |
| `eval_pi05_random_k0925_object_seed43` | 30.0% | DONE |
| `eval_pi05_random_k09_spatial_seed42` | 54.6% | DONE |
| `eval_pi05_l2norm_k09_spatial_seed42` | 95.0% | DONE |

### 任务 2：westd-41074 两个实验仍在运行
- `eval_pi05_random_k095_spatial_seed42_v2` (PID 943105): 运行中，T2 完成 92%
- `eval_pi05_random_k0925_spatial_seed42` (PID 942389): 运行中，T0 进行中 100%
- 预计各需 ~90 分钟完成

### 任务 3：OpenVLA eval 已部署
- `eval_openvla_l2norm_k05_object_seed42_v5` 在 westd-38929 GPU 3 运行中 (PID 311157)
- 修复了 huggingface-hub 版本兼容问题（安装 0.36.2 到 openvla_deps）
- 已确认模型加载成功，开始评估 Task 1/10

---
