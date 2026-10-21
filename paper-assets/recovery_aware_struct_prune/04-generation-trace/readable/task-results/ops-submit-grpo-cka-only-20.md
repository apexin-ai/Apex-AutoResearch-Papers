# ops submit grpo cka only 20

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_submit_grpo_cka_only_20_20260517T145107_result.json`
- **Structured JSON:** [`61649213be931300388f.json`](../../sessions/61/61649213be931300388f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

任务已完成。报告如下：

---

**grpo_cka_only_20 提交成功**

| 项目 | 详情 |
|------|------|
| **tmux session PID** | 725227 |
| **python 进程 PID** | 725232 |
| **GPU** | cuda:0 (CUDA_VISIBLE_DEVICES=0) |
| **状态** | 模型加载中（CPU→GPU 传输阶段），进程正常运行 |
| **超时** | 168h |

**nvidia-smi 当前状态：**
- **cuda:0**: 3MiB / 97887MiB — grpo_cka_only_20 正在加载模型（预计分钟级别完成加载后占用 ~20-30GB）
- **cuda:1**: 73165MiB / 97887MiB, 99% util — grpo_random_20 (PID 719684) 正常训练中

两个实验进程均正常。cuda:0 的显存将在模型加载完成并 `.to(cuda)` 后分配。

---
