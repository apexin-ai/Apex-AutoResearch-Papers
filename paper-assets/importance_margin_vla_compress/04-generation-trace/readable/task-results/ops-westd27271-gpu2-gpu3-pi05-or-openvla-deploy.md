# ops westd27271 gpu2 gpu3 pi05 or openvla deploy

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_westd27271-gpu2-gpu3-pi05-or-openvla-deploy_20260521T122624_result.json`
- **Structured JSON:** [`17460c72769eaf678f20.json`](../../sessions/17/17460c72769eaf678f20.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**问题：服务器只有 2 张 GPU（GPU 0 和 GPU 1），没有 GPU 2/3。**

当前占用情况：
- GPU 0: python 进程 (PID 193983), 16GB/98GB
- GPU 1: python 进程 (PID 921279), 42GB/98GB

两张卡都已被占用。无法在 GPU2/GPU3 上部署——这台机器没有这两张卡。

需要你决定：
1. **等现有任务结束** — 等 GPU 0 或 GPU 1 空出来再部署
2. **换服务器** — 在有空闲 GPU 的其他服务器上跑
3. **强制终止现有进程** — 杀掉当前进程腾出 GPU（需确认这些进程是否还需要）

---
