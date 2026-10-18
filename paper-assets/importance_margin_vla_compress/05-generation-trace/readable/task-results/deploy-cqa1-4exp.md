# deploy cqa1 4exp

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_cqa1_4exp_20260526T034119_result.json`
- **Structured JSON:** [`62550268284f1dcf4cc7.json`](../../sessions/62/62550268284f1dcf4cc7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

4 个 Python 进程全部在运行：

| GPU | 实验 | PID | RSS | 状态 |
|-----|------|-----|-----|------|
| 0 | π0.5 Random k=0.75 | 3728 | ~6.9GB (CPU加载中) | Rl |
| 1 | π0.5 Attention k=0.75 | 3874 | ~13.6GB (CPU加载中) | Rl |
| 2 | OpenVLA Attn k=0.9 Goal seed43 | 4049 | ~3.0GB, GPU 14.9GB | Rl |
| 3 | OpenVLA Random k=0.5 Object | 4365 | ~3.4GB, GPU 14.9GB | Rl |

4 个实验全部部署成功。π0.5 的两个实验正在把模型从磁盘加载到 CPU 内存（两个同时读同一份模型文件，有 I/O 竞争所以慢一些），加载完毕后会搬到 GPU 显存开始 eval。OpenVLA 的两个已经在 GPU 上运行评测。

---
