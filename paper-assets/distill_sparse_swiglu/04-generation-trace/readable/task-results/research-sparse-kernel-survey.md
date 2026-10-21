# research sparse kernel survey

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_sparse-kernel-survey_20260519T025318_result.json`
- **Structured JSON:** [`d76134cd5a6e76186451.json`](../../sessions/d7/d76134cd5a6e76186451.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

调研完成，综合四路结果。以下是完整评估。

---

## Sparse Inference Kernel 方案评估

### 场景约束
- Unstructured activation sparsity, 30-50%, per-token dynamic mask
- SwiGLU FFN (非 ReLU)
- 模型: LLaMA-3.1-8B / Mistral-7B / Qwen-2.5-14B
- GPU: RTX PRO 6000 Blackwell
- DDL: 6 天

---

### 方案总览

| 方案 | 可行性 | 实现难度 | 预期 Speedup | 硬件兼容 | 时间估计 | GitHub |
|------|--------|---------|-------------|---------|---------|--------|
| **TEAL (Triton GEMV)** | **直接可用** | 低 (有现成 kernel) | 1.5x@40%, 1.8x@50% | Triton 通用 | **2-3 天** | [FasterDecoding/TEAL](https://github.com/FasterDecoding/TEAL) |
| R-Sparse | 可用 | 中 | 1.43x@50% | CUDA/Triton | 3-4 天 | [VITA-Group/R-Sparse](https://github.com/VITA-Group/R-Sparse) |
| ProSparse CUDA | 部分 (针对 ReLU) | 中 | 2-2.4x/step | CUDA | 4-5 天 | [Raincleared-Song/sparse_gpu_operator](https://github.com/Raincleared-Song/sparse_gpu_operator) |
| TwELL (SakanaAI) | 可用 | 中-高 | 1.2x (batch) | H100 优化 | 4-5 天 | [SakanaAI/sparser-faster-llms](https://github.com/SakanaAI/sparser-faster-llms) |
| CATS CUDA | 可用 | 中 | 1.15x | CUDA | 3-4 天 | [ScalingIntelligence/CATS](https://github.com/ScalingIntelligence/CATS) |
| Deja Vu (Triton) | 可用 | 中 | 2x (大模型) | Triton | 3-4 天 | [FMInference/DejaVu](https://github.com/FMInference/DejaVu) |
| PyTorch 2:4 | **不可用** | — | — | — | — | — |
| cuSPARSE | 不推荐 | 高 | 动态 mask 转换开销抵消收益 | — | — | — |
| DeepSparse | **已废弃** | — | — | — | — | — |
| PowerInfer | 不独立可用 | 高 (GPU-CPU 混合架构) | 大但不可移植 | — | — | — |

---

### 排除项说明

1. **PyTorch 2:4 semi-structured**: 仅支持静态 2:4 weight sparsity，不支持 unstructured dynamic activation sparsity
2. **cuSPARSE**: 每 token 需做 dense→sparse 格式转换，overhead 抵消 sparsity 收益
3. **cuBLAS**: 无 sparse GEMM，需走 cuSPARSELt（仅 2:4）
4. **DeepSparse**: Neural Magic 2025-06 停止维护，CPU-only
5. **PowerInfer**: 架构绑定（GPU-CPU hybrid + llama.cpp），kernel 不可独立提取

---

### 推荐方案：TEAL Triton Kernel

**理由：**
1. 我们的论文已经在用 "TEAL-style inference" 框架（predictor → mask → sparse FFN）
2. TEAL 的 Triton sparse GEMV kernel 直接支持 unstructured activation sparsity + dynamic per-token mask
3. ICLR 2025 Spotlight，代码质量高，有完整 benchmark
4. Triton kernel 跨 GPU 架构兼容（Blackwell 支持 Triton）
5. 实现路径最短：clone kernel → 接入我们的 predictor mask → benchmark

**关键文件：**
- `kernels/sparse_gemv.py` — Triton sparse GEMV kernel
- 支持 deterministic 和 atomic-add 两种变体
- FP16 精度（Triton BF16 atomic_add 有限制）

**预期数据：**
- 40% sparsity → ~1.5x wall-clock speedup
- 50% sparsity → ~1.8x wall-clock speedup
- 单 batch decoding 场景最优

---

### 实现步骤（6 天计划）

**Day 1-2: 集成 TEAL kernel**
1. Clone TEAL repo，提取 `kernels/sparse_gemv.py`
2. 适配我们的 predictor output（binary mask）→ TEAL sparse format
3. 替换 SwiGLU FFN forward 中的 dense matmul 为 sparse GEMV
4. 单层验证：sparse FFN output 与 dense FFN output 对齐（numerical check）

**Day 3-4: Benchmark**
5. Wall-clock latency benchmark：dense vs sparse，逐层 + 端到端
6. 扫 sparsity level: 30%, 40%, 50%
7. 扫模型: LLaMA-3.1-8B, Mistral-7B, Qwen-2.5-14B
8. 记录 throughput (tokens/s) 和 per-layer latency breakdown

**Day 5: 论文数据整合**
9. 制作 speedup table/figure
10. 写 experiments section 的 efficiency 段落

**Day 6: Buffer + 备选**
11. 如果 TEAL kernel 在 Blackwell 上有兼容问题，fallback 到手写简化版 Triton kernel（gather-based sparse matmul，~200 行）
12. 或参考 Deja Vu 的 `gather_gemv.py` 作为替代

---

### 备选方案优先级

如果 TEAL 遇阻：
1. **Deja Vu Triton kernel** (`gather_gemv.py`) — 同样是 Triton，gather-based sparse GEMV
2. **自写 Triton kernel** — 基于 scatter/gather pattern，核心逻辑 ~200 行
3. **R-Sparse** — ICLR 2025，有 CUDA kernel，但适配成本更高

### 论文可引用的 speedup 参考值

即使我们自己的 kernel 实测数据还没出，论文中可以引用同类工作的数据作为 "activation sparsity speedup 是 well-established" 的论据：
- TEAL: 1.53-1.8x (ICLR 2025)
- R-Sparse: 1.43x (ICLR 2025)
- ProSparse: 2-4.5x (COLING 2025, ReLU models)
- TwELL: 1.2x batch / 1.2x e2e (ICML 2026)

---
