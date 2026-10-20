# diagnose carr fullft k4 probe 02

**Does Reward Curation Kill Diversity? Systematic Evidence of Surprising Resilience in Iterative Self-Training** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_carr_fullft_k4_probe_02_20260516T165859_result.json`
- **Structured JSON:** [`6ce2347ef16eb77238bc.json`](../../sessions/6c/6ce2347ef16eb77238bc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

PID 514305 已退出（确认 probe_02 已崩溃），PID 514162 仍在运行。

---

## 诊断报告：carr_fullft_k4_probe_02 CUDA OOM

### OOM 精确阶段

**生成阶段（Generation Phase）**，第一个 batch 就崩了。

调用链：`run_quick_probe_fullft.py:69` → `pipeline.py:71` → `generate.py:35` → `generate.py:60 model.generate()` → Qwen3 MLP forward

仅生成了 16/2000 个 prompt 就 OOM。

### 根本原因：GPU 显存被另一个进程占用

**PID 514162 (`python3 run_quick_probe_fullft.py`)** 已经在物理 GPU 1 上运行，占用 ~21 GiB 显存。当 probe_02（PID 514305，CUDA_VISIBLE_DEVICES=1）启动时，GPU 1 只剩 ~10 GiB 可用。

OOM 时的显存分布：

| 占用方 | 显存 |
|--------|------|
| PID 514162（另一个 fullft 实验） | 20.99 GiB |
| PID 514305（probe_02 本身） | ~10.23 GiB（PyTorch 8.46 + reserved 1.19 + non-PyTorch） |
| 可用 | 129.75 MiB |
| GPU 1 总容量 | 31.36 GiB |

**不是 probe_02 自身配置过大，而是 GPU 1 被两个进程同时使用。**

### PID 514162 的身份

`python3 run_quick_probe_fullft.py` — 一个更早启动的 fullft 实验，当前仍在运行（29854 MiB on GPU 1）。同时 GPU 0 上还有 PID 507603 (`python3 run_quick_probe_k8.py`，25036 MiB)。

### 附带问题

`generate.py:10` 仍使用 `torch_dtype=torch.float16` 而非 bf16。虽然不是这次 OOM 的直接原因，但与 "已修复为 bf16" 的说法不符。

### 当前 GPU 状态

| GPU | 进程 | 显存占用 | GPU利用率 |
|-----|------|---------|----------|
| GPU 0 | PID 507603 (run_quick_probe_k8.py) | 25036 MiB / 32607 MiB | 86% |
| GPU 1 | PID 514162 (run_quick_probe_fullft.py) | 29863 MiB / 32607 MiB | 90% |

两块 GPU 都被占满，无法再启动新实验。

### 修复建议

1. **立即方案**：等 PID 514162 完成（或 kill 掉），再单独在 GPU 1 上跑 probe_02。Qwen3-0.6B full-FT + gen_batch_size=16 × K=4 在 32 GiB 独占 GPU 上应该可以跑通。

2. **如果独占 GPU 仍 OOM**，按优先级降低显存：
   - `gen_batch_size`: 16 → 8（生成阶段 num_return_sequences=K 使得实际并发序列为 batch×K=64，减半到 32）
   - 在 `generate.py` 的 `_generate_batch` 中加 `torch.cuda.empty_cache()` 每个 batch 后清理
   - 设置 `PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True` 减少碎片

3. **修复 float16 → bf16**：`generate.py:10` 的 `torch_dtype=torch.float16` 改为 `torch.bfloat16`，与训练阶段一致。

4. **长期方案**：加互斥机制，避免多个实验同时占用同一 GPU。或在启动前检查 `nvidia-smi` 确认目标 GPU 空闲。

---
