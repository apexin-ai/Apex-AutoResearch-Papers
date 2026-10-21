# ssh rtx gpu reset cuda12

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_rtx_gpu_reset_cuda12_20260523T084851_result.json`
- **Structured JSON:** [`8fea39fb3d2940cd268c.json`](../../sessions/8f/8fea39fb3d2940cd268c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已修复。前后对比：

| GPU | 重置前 | 重置后 |
|-----|--------|--------|
| cuda:0 | 0%, P8, 34W | 0%, P8, 34W |
| **cuda:1** | **100%, P0, 104W** | **0%, P8, 36W** |
| **cuda:2** | **100%, P0, 105W** | **0%, P8, 38W** |
| cuda:3 | 0%, P8, 35W | 0%, P8, 34W |

`nvidia-smi --gpu-reset` 在此环境不受支持，改用 PyTorch CUDA context 接管 + `empty_cache` + `synchronize` 清除了残留 driver state。四卡全部空闲，0% utilization，0MiB 占用。

---
