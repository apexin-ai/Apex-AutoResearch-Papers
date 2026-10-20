# ssh westb status check

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_westb_status_check_20260520T215155_result.json`
- **Structured JSON:** [`471d869f4b9b0cece7a8.json`](../../sessions/47/471d869f4b9b0cece7a8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**westb-23072 状态报告：**

| 项目 | 状态 |
|------|------|
| **数据盘** | 227G/250G (91%)，剩余 24G — 与预期一致 |
| **GPU 0** | 空闲，0% 利用率，0/95.6GB 显存 |
| **GPU 1** | 空闲，0% 利用率，0/95.6GB 显存 |

**残留进程：**
- `tmux eval_unstructured_20` (PID 680597, May17 启动) — 看起来是之前的 GSM8K 评估 session，bash 已退出但 tmux session 还在
- `http.server 8765` (PID 985445, May15 启动) — 数据盘上的文件服务

无活跃的 Python 训练/推理进程在跑，两张 GPU 完全空闲可用。

---
