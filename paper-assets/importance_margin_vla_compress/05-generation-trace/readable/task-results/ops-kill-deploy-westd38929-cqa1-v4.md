# ops kill deploy westd38929 cqa1 v4

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_kill_deploy_westd38929_cqa1_v4_20260522T080627_result.json`
- **Structured JSON:** [`cece05b70059e3063c73.json`](../../sessions/ce/cece05b70059e3063c73.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有 eval 实验部署验证完成。汇总报告：

---

## westd-38929

| GPU | 实验 | PID | 状态 |
|-----|------|-----|------|
| 0 | l2norm k0.5 spatial seed43 | 708992 | RUNNING (旧) |
| 1 | random k0.3 spatial seed43 | 709233 | RUNNING (旧) |
| 2 | l2norm k0.3 spatial seed43 | 709369 | RUNNING (旧) |
| 3 | **random k0.9 object seed43** | 766525 | **RUNNING** ✓ (n_keep=230/256) |

- PID 709985 kill 成功，但实际占 GPU 的 python 子进程是 709608（bash wrapper vs python child），已二次 force kill
- 注意：用户给的 PID 都是 bash wrapper，实际 GPU 进程 PID 整体偏移了一位

## cqa1-33015

| GPU | 实验 | PID | 状态 |
|-----|------|-----|------|
| 0 | (旧) l2norm k0.5 + random k0.5 spatial | 209336/209728 | RUNNING, 占 20.5GB |
| 1 | **l2norm k0.95 object seed43** | 212714 | **RUNNING** ✓ (n_keep=243/256) |
| 2 | **random k0.925 object seed43** | 213453 | **RUNNING** ✓ (n_keep=236/256) |
| 3 | **l2norm k0.9 object seed43** | 216142 | **加载中** ⏳ (CPU→GPU transfer) |

- cqa1 GPU 0 **不是空的**（有 2 个旧 spatial 实验），l2norm k0.9 原计划部署 GPU 0 → OOM，改部署到 GPU 3
- l2norm k0.9 的 python 进程 33GB RSS 正在 CPU 加载模型，预计很快 transfer 到 GPU 3

## Spatial Heatmap 可视化（P1）

**未执行**，原因：
1. cqa1 GPU 3 被 l2norm k0.9 占用（因 GPU 0 OOM 挪过来的）
2. `scripts/visualize_token_importance.py` 是硬编码脚本（固定 v8 checkpoint，无 `--suite`/`--seed`/`--output` argparse），不支持用户给的 CLI 参数
3. 建议等某个 eval 完成后空出 GPU，同时改造脚本支持 CLI 参数再跑

---
