# research cats feasibility

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_cats_feasibility_20260517T115314_result.json`
- **Structured JSON:** [`cca878932f0b882c0a30.json`](../../sessions/cc/cca878932f0b882c0a30.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## CATS Baseline 可行性报告

**代码可用性**: 有。https://github.com/ScalingIntelligence/CATS (MIT License, COLM 2024)

**核心机制**: 对 SwiGLU 的 gate branch 输出 (`SiLU(x @ W_gate)`) 做对称阈值截断——绝对值低于阈值 t 的激活置零。阈值通过 ~500 样本校准确定（按 percentile 计算，per-layer）。支持任意 sparsity level（50%/70%/90% 均有评估）。

**兼容性问题**:
- 锁定 `transformers==4.36.2`，直接 import 内部类（`MistralMLP` 等），与新版不兼容
- 有自定义 CUDA kernel（`flash_gemv`），但核心机制不依赖它
- 已有 LLaMA-2-7B 实现，但无 LLaMA-3.1-8B

**复现难度: 低（4-8 小时）**。核心 `SparseSiLU` 仅 ~10 行代码，重新实现比适配其 codebase 更快：
1. 校准数据过模型，收集各层 `|SiLU(gate)|` 直方图
2. 按目标 sparsity 计算 percentile 阈值
3. 推理时低于阈值的 gate activation 置零

**与我们的实验设置完全兼容**: CATS 就是在 SwiGLU gate activation 上做 sparsity，可直接集成到 `benchmark_eval.py` 评估，无需特殊推理代码。

**推荐: 值得加入。** 方法简单、复现容易、与我们的 setting 高度对齐（同样利用 SwiGLU gate 的天然稀疏性），是 training-free baseline 的理想对照。

---
