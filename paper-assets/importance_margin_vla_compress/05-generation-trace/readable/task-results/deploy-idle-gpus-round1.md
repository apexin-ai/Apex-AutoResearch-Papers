# deploy idle gpus round1

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_idle-gpus-round1_20260527T232412_result.json`
- **Structured JSON:** [`def6d19840509b499c21.json`](../../sessions/de/def6d19840509b499c21.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

3 个实验全部部署成功，进程已确认在运行：

| # | 实验 | 服务器 | GPU | PID | 状态 |
|---|------|--------|-----|-----|------|
| 1 | Attn k=0.7 seed44 | cqa1-33015 | cuda:3 | **834234** | 运行中，模型加载中 |
| 2 | L2norm k=0.85 seed44 v2 | westd-38929 | cuda:2 | **783927** | 运行中，模型加载中 |
| 3 | Attn k=0.5 seed44 v2 | westd-38929 | cuda:3 | **784004** | 运行中，模型加载中 |

GPU 显存尚未完全分配（模型还在编译/加载阶段），所有进程 CPU 利用率高，符合预期。tmux session 名称与 exp_id 一致，日志输出到指定 log_path。

---
