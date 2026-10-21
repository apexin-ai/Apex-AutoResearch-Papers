# code mistral hspiqa check and 41718 gpu1

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_mistral_hspiqa_check_and_41718_gpu1_20260519T144203_result.json`
- **Structured JSON:** [`62a132ba7c01f9b88634.json`](../../sessions/62/62a132ba7c01f9b88634.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇报完毕。

---

## 1. Mistral KL 30% HS/PIQA 结果：已完整

结果文件在服务器重启前已生成（`2026-05-19 13:12:13`）。

| Task | Metric | Dense | KL 30% (uniform) | Δ |
|------|--------|-------|-------------------|---|
| HellaSwag | acc_norm | 0.8320 | 0.6892 | -14.28pp |
| PIQA | acc | 0.8003 | 0.7443 | -5.60pp |
| PIQA | acc_norm | 0.8188 | 0.7519 | -6.69pp |

另有 `mistral_kl30_downstream` 也完整：ARC-C acc_norm=0.5017, WinoGrande acc=0.6914, MMLU acc=0.4404, GSM8K em=0.1114。

## 2. FlashInfer Benchmark 准备情况

**现状**：
- **flashinfer 未安装**（westd-41718 上 miniconda3 中没有 flashinfer 包；westd-41718 上也没有 flashinfer 源码目录）
- 本地 repo 有完整的 flashinfer git clone（`flashinfer/`），但未 sync 到服务器
- **已有 benchmark 脚本**：
  - `src/benchmark_speedup.py` — 支持 zero-masking + gather-scatter，不含 flashinfer 内核
  - `src/latency_benchmark.py` — dense vs predictor-only vs predictor+compensation
- **已有 benchmark 结果**（westd-34887）：zero-masking 方式 speedup = 0.93x（即比 dense 还慢 7%），因为 matmul 仍是 full-size，无实际 FLOP 节省

**需要准备的工作**：
1. flashinfer 安装（需编译或找预编译 wheel，匹配 CUDA 12.8 + PyTorch 2.8）
2. 将本地 `flashinfer/` 目录 sync 到 westd-41718
3. 写/改 benchmark 脚本支持 flashinfer 的 sparse MLP kernel（如果 flashinfer 有 structured sparse matmul 的话）
4. 明确 benchmark 目标：是要展示真正的稀疏 kernel 加速，还是仅测 flashinfer attention 加速？

**等你确认方案后再在 westd-41718 cuda:1 上执行。**

---
