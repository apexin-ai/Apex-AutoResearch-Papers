# infra gpu status and seed123

**The Embedding Alignment Gap: Why Diversity-Based Data Selection Accelerates Model Collapse in Iterative Self-Training** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_gpu_status_and_seed123_20260513T092420_result.json`
- **Structured JSON:** [`015d7cf4fc4258f4b04b.json`](../../sessions/01/015d7cf4fc4258f4b04b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**结果汇总：**

### seed123 实验状态
**正在运行。** PID 180459（wrapper）和 180473（python3）均存活。
- 当前进度：**Generation 3/7**，正在执行 Training student（step 3/5）
- Gen 2 结果：PPL=52.21, RankMe=298.54, k-NN=0.988
- 使用 GPU 0，占用 21678MiB

### GPU 状态

| GPU | 显存占用 | 进程 | 状态 |
|-----|---------|------|------|
| GPU 0 | 70859 / 97887 MiB | PID 180473 (seed123) 21678MiB | **~49181MiB ghost memory**，但无法 reset——seed123 正在使用 GPU 0 |
| GPU 1 | 0 / 97887 MiB | 无 | **完全空闲，可用** |

### GPU 0 ghost memory
无法执行 `nvidia-smi --gpu-reset -i 0`，因为 seed123 正在 GPU 0 上运行。ghost memory 需要等 seed123 完成后再清理（或 kill 进程后 reset，但不建议）。

### 结论
- seed123 正常运行中，Gen 3/7，无需干预
- GPU 1 空闲，可用于启动其他任务
- GPU 0 ghost memory 暂时无法处理，等 seed123 跑完后再 reset

---
