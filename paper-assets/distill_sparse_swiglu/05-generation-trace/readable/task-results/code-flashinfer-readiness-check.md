# code flashinfer readiness check

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_flashinfer_readiness_check_20260519T155945_result.json`
- **Structured JSON:** [`aa5df6f70f79cef14d1d.json`](../../sessions/aa/aa5df6f70f79cef14d1d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部信息收集完毕。汇总如下：

---

## FlashInfer Inference Benchmark 就绪状态报告

### flashinfer 包：**未安装**
- `import flashinfer` → `ModuleNotFoundError`
- miniconda3 下无 flashinfer 相关文件
- 服务器上无任何代码 import flashinfer

### 现有 benchmark 代码：**有，但是 mask-and-multiply（无真正加速）**
两个脚本：
- `src/benchmark_latency.py` — 较完整，支持多 batch size、多 sparsity level、predictor overhead 测量、JSON 输出
- `src/latency_benchmark.py` — 较早版本，固定 batch=1

**已有运行结果** (`results/benchmark_latency.json`, 2026-05-19)：
| 条件 | batch=1 tok/s | batch=8 tok/s | vs Dense |
|------|--------------|--------------|----------|
| Dense | 17,309 | 15,637 | 1.00x |
| KL Sparse 30% | 16,089 | 14,697 | **0.93x (慢 7%)** |
| KL Sparse 50% | 16,057 | 14,757 | **0.93x (慢 7%)** |

这正是 W3 质疑的核心：mask-and-multiply 没有 FLOP 节省，predictor 还加了 overhead（bs=1: 3.26ms, bs=8: 14.4ms），所以比 dense 更慢。

### 模型和 checkpoint：**就绪**
- LLaMA-3.1-8B: `/root/autodl-tmp/models/llama-3.1-8b` ✓
- KL 30% predictor: `checkpoints/kl_sparsity30_s42_v3/predictor_kl_normalized.pt` ✓
- KL 50% predictor: `checkpoints/mvp_kl_norm_v2_s42/predictor_kl_normalized.pt` ✓

### 环境
- GPU: 2x NVIDIA RTX PRO 6000 Blackwell (96GB each)
- PyTorch: 2.8.0+cu128
- CUDA: 12.8

### 本地 flashinfer 仓库
- `/home/ubuntu/.../projects/distill_sparse_swiglu/flashinfer/` 有完整 flashinfer 源码 clone（含 benchmarks、CUDA kernels）
- 但尚未 push 到服务器，也未安装为 Python 包

### 缺什么

1. **flashinfer Python 包安装**（`pip install flashinfer` 或从源码编译，需匹配 cu128 + torch 2.8）
2. **sparse kernel benchmark 脚本**——现有脚本只做 mask-and-multiply。需要新脚本利用 flashinfer 的 sparse matmul/structured sparsity kernel 实现真正的 FLOP 节省，然后测 wall-clock speedup
3. **sparse FFN forward pass 实现**——用 flashinfer API 将 predictor mask 转换为实际跳过 down_proj 计算的 sparse execution path

### 预估搭建时间
- flashinfer 安装（预编译 wheel if available for cu128）：5-15 min
- 从源码编译（如无匹配 wheel）：20-40 min
- sparse kernel benchmark 脚本编写 + 调试：1-2 hours
- 端到端测试 + 数据收集：30 min

---
