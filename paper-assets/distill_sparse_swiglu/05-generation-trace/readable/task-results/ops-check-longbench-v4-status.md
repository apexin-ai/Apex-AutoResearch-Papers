# ops check longbench v4 status

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-longbench-v4-status_20260516T134320_result.json`
- **Structured JSON:** [`2268d2271b5ee533177f.json`](../../sessions/22/2268d2271b5ee533177f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

**longbench_dense_v4 已失败，进程未在运行。**

| 项目 | 状态 |
|------|------|
| tmux session | 不存在（no server running） |
| 进程 PID | 无 longbench 相关进程 |
| 退出码 | EXIT_CODE=1 |

**失败原因：CUDA OOM**

日志显示在 `LlamaMLP.forward` 中触发 `torch.OutOfMemoryError`：
- 尝试分配 13.98 GiB，但 GPU 0 仅剩 13.48 GiB 可用
- PyTorch 已占用 62.87 GiB allocated + 17.98 GiB reserved（共 ~81 GiB / 95 GiB）
- 在 `generate_until` 的第 0/800 个请求时就崩了（刚开始推理即 OOM）
- 建议日志中提到可尝试 `PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True` 减少碎片

---
