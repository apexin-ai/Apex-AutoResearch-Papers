# ops deploy westd38929 gpu3

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_deploy_westd38929_gpu3_20260526T085051_result.json`
- **Structured JSON:** [`0f7f5eb8b5403a34a39d.json`](../../sessions/0f/0f7f5eb8b5403a34a39d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

部署完成。

**实际情况与任务描述的差异：**
- GPU3 并非空闲（PID 288325 正在跑 attn k=0.85 object），**GPU2 才是空闲的**
- PID 252246（l2norm k=0.7 object）已结束

**已部署（优先级 1）：**
- **实验**: `eval_openvla_attn_k085_goal_seed42_v3`
- **内容**: OpenVLA Attention k=0.85 Goal — 论文 cliff curve 关键中间点
- **服务器**: westd-38929 **GPU2**（非 GPU3）
- **PID**: 412621
- **模型**: `/root/autodl-tmp/models/openvla-7b-finetuned-libero-goal`
- **状态**: RUNNING，已开始 Task 1/10，vision tokens 256→217

westd-38929 现在 4 GPU 全部在用。

---
