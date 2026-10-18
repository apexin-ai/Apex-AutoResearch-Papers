# verify westd41074 gpu01 deploy

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_verify_westd41074_gpu01_deploy_20260527T085733_result.json`
- **Structured JSON:** [`3f023c89334cc445c392.json`](../../sessions/3f/3f023c89334cc445c392.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部 4 个 GPU 验证通过，实验正常运行。

| GPU | PID | 实验 | 显存占用 | GPU-Util | 状态 |
|-----|-----|------|----------|----------|------|
| **0** | 340187→340196 | random k=0.9 | 5,313 MiB | 5% | 模型加载中（已加载 state dict，处理 vision embedding） |
| **1** | 340421→340432 | random k=0.5 | 2,032 MiB | 74% | 模型加载中（gradient checkpointing 已启用） |
| **2** | 262128→262137 | random k=0.95 | 10,507 MiB | 33% | 运行中 ✓ |
| **3** | 262464→262473 | l2norm k=0.95 | 10,796 MiB | 23% | 运行中 ✓ |

注意：GPU1 上还有一个额外进程 PID 335321 占用 16,169 MiB（可能是之前的实验残留）。GPU0/1 的两个新实验刚启动约 2 分钟，正在加载模型，尚未进入 eval 阶段，属于正常状态。

---
