# ops gpu process check

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gpu_process_check_20260517T124730_result.json`
- **Structured JSON:** [`bc1959aae4f9edacca61.json`](../../sessions/bc/bc1959aae4f9edacca61.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果汇总：

**GPU 进程状态：**
- **PID 705918 (Binoculars/Fast-DetectGPT pilot)** — **已死**。cuda:0 完全空闲 (0MiB, 0% util)。ps aux 也无此进程。项目目录中未找到任何 binoculars/fast-detect 相关文件（脚本和结果均无）。
- **PID 695547 (prompted_gen_gpt2xl_001)** — **运行中**。cuda:1, 15676MiB, 63% util。启动命令：`python scripts/prompted_generation_eval.py --gpu 1`

**MLP Baseline 结果：**

| Variant | Mean Acc | Delta vs RF (0.782) |
|---------|----------|---------------------|
| MLP-128-128 | 0.7866 | +0.0046 |
| MLP-64-128-64 | 0.7895 | +0.0075 |
| **MLP-Poly-Top5** | **0.7906** | **+0.0086** |

结论：最好的 MLP 也只比 RF 高不到 1pp，feature bottleneck confirmed。

结果已保存至服务器 `artifacts/gpu_check_20260517.md`。

---
