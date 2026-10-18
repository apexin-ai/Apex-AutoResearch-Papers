# ops audit westd38929 smolvla v3

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_audit_westd38929_smolvla_v3_20260522T150558_result.json`
- **Structured JSON:** [`21a83efb5d6513d2078d.json`](../../sessions/21/21a83efb5d6513d2078d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇报

### 结论：GPU 不是空闲的，4 个实验全部正常运行中

低 GPU 利用率（0-1%）是因为 LIBERO 模拟在 episode 执行阶段是 CPU 密集型的（CPU 占用 160-189%），GPU 只在推理时短暂使用。内存 2-2.8 GB 是模型常驻显存。**无需重部署。**

### Tmux Session 状态

| Session | GPU | 当前任务 | 进度 | 状态 |
|---------|-----|---------|------|------|
| smolvla_object | 0 | random_prune k=0.95 Object | ep 45/50 | 运行中（链中第2个，l2_norm 已完成） |
| smolvla_spatial | 1 | l2_norm k=0.95 Spatial | ep 34/50 | 运行中（链中第2个，baseline 已完成） |
| smolvla_goal | 3 | l2_norm k=0.95 Goal | ep 20/50 | 运行中（链中第2个，baseline 已完成） |
| smolvla_long | 2 | baseline Long | ep 15/50 | 运行中（链中第1个） |

### 已完成实验 SR

| 实验 | SR | 详情 |
|------|-----|------|
| **Spatial baseline** | **44.6%** (223/500) | CI [40.3%, 49.0%] |
| **Goal baseline** | **60.8%** (304/500) | CI [56.5%, 65.0%] |
| **Object l2_norm k=0.95** | **0.2%** (1/500) | 灾难性崩溃，假设被否定 |

### IndexError bug
**未出现。** 所有命令已使用 `--num_episodes 50`（50/task × 10 tasks = 500 total），修复已生效。

### 注意
- Object baseline (seed=42, official checkpoint) 不在当前批次中。之前只有 `smolvla_baseline_object_seed43.json`（seed 43）。如果需要 seed=42 的 Object baseline，需要单独安排。
- Object 的 l2_norm k=0.95 结果（SR=0.2%）说明 SmolVLA 对 expert 剪枝极其敏感——即使只移除 5% 也完全崩溃。

---
