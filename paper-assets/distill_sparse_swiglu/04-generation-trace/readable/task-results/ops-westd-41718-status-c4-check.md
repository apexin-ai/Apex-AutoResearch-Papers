# ops westd 41718 status c4 check

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_westd-41718-status-c4-check_20260518T040845_result.json`
- **Structured JSON:** [`56f3a1e9f842669eb9b7.json`](../../sessions/56/56f3a1e9f842669eb9b7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## westd-41718 状态汇报

| 项目 | 状态 |
|------|------|
| **GPU** | 2× RTX PRO 6000 Blackwell (96GB each), **全空闲**, 0% utilization, 0MiB VRAM 占用 |
| **残留进程** | 无 GPU 进程 |
| **磁盘** | `/` 27G 可用 (12% used); `/dev/sda2` 764G 可用 (9% used); `/autodl-pub` 5.3T 可用 |
| **C4 数据** | 已下载, 路径 `/root/autodl-tmp/.hf_cache/hub/datasets--allenai--c4/`, 419MB, 包含 `en/` validation (8 shards) 和 `en.noblocklist/` |
| **Python/CUDA** | miniconda3 Python 3.12 可用 (`/root/miniconda3/bin/python`), PyTorch CUDA 正常 (2 devices detected) |
| **项目代码** | `/root/distill_sparse_swiglu/` 完整 (src/, scripts/, checkpoints/, results/, wandb/ 等) |

**注意**: 服务器重启后 `python` 未加入 PATH (conda 未 activate)。新实验启动命令需用 `source /root/miniconda3/bin/activate && ...` 或完整路径。

**结论: 可以立即派新实验。**

---
