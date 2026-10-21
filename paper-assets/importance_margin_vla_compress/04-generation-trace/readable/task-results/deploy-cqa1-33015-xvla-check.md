# deploy cqa1 33015 xvla check

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_cqa1-33015-xvla-check_20260523T184829_result.json`
- **Structured JSON:** [`c48e05df3dc41b3fb9a0.json`](../../sessions/c4/c48e05df3dc41b3fb9a0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验已成功启动，Python 进程正在运行。

## 部署报告

| 项目 | 状态 |
|------|------|
| **X-VLA 模型** | 存在 (`/root/autodl-tmp/X-VLA-Libero/`, 3.3GB) |
| **GPU 数量** | 2 块（非任务预期的 4 块），每块 ~96GB |

### GPU 占用情况

| GPU | 状态 | 实验 |
|-----|------|------|
| GPU 0 | **已部署** | `eval_xvla_l2norm_k03_long_seed42` (PID 366055, tmux session 同名) |
| GPU 1 | **被占用** | `eval_openvla_baseline_long_seed42`（之前的实验，未中断） |

### 未部署的实验（无空闲 GPU）

- `eval_xvla_random_k03_goal_seed42` (原定 GPU 1)
- `eval_xvla_random_k03_spatial_seed42` (原定 GPU 2 — 不存在)
- `eval_xvla_random_k03_long_seed42` (原定 GPU 3 — 不存在)

GPU 1 上的 openvla 实验完成后可部署剩余实验。

---
