# ssh check old processes

**The Embedding Alignment Gap: Why Diversity-Based Data Selection Accelerates Model Collapse in Iterative Self-Training** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_check-old-processes_20260512T122738_result.json`
- **Structured JSON:** [`4f11ce6ba49419a1e7e3.json`](../../sessions/4f/4f11ce6ba49419a1e7e3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇报：

- **旧进程（7215, 7294）**：早已退出，无需清理。
- **v2 实验进程（10214, 10291）**：也已不存在，**未在运行**。
- **GPU 状态**：
  - GPU 0 (RTX PRO 6000 Blackwell, 96GB)：无计算进程，但有 49175MiB 显存被占用（可能是残留显存未释放），GPU 利用率 0%
  - GPU 1 (RTX PRO 6000 Blackwell, 96GB)：完全空闲，0MiB 占用

**结论**：所有实验进程（旧的和 v2）都已退出。GPU 0 有约 48GB 残留显存占用但无对应进程，可能需要 `nvidia-smi --gpu-reset` 或等待自动释放。两张卡当前空闲，可以启动新实验。

---
