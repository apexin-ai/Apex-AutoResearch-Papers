# check preparing experiments

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_preparing-experiments_20260529T041441_result.json`
- **Structured JSON:** [`f830cbe32e6f9a3ceecd.json`](../../sessions/f8/f830cbe32e6f9a3ceecd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果已写入 `artifacts/preparing_check_result.md`。

**结论：6 个实验全部 DEAD，无一进入训练。**

根因统一：两台服务器 nvidia-smi 只暴露 GPU 0（各 ~96GB），但实验分配的 cuda:1/2/3 不可见，`torch.cuda.set_device()` 立即抛 `RuntimeError: No CUDA GPUs are available`，所有进程在 11:40 UTC 启动后秒崩。

需要排查的关键问题：
- 两台服务器为什么只有 1 张 GPU 可见？（`nvidia-smi -L` 能否列出更多？是 cgroup 限制还是 `CUDA_VISIBLE_DEVICES` 被设了？）
- 修复 GPU 可见性后需要重新提交全部 6 个实验

---
