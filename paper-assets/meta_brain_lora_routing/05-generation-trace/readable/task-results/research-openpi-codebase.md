# research openpi codebase

**Meta-Brain: Perturbation-Diagnostic Routing of LoRA Experts for Parameter-E cient VLA Robustness** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_openpi-codebase_20260515T103420_result.json`
- **Structured JSON:** [`8a7b0d46ae5984f46081.json`](../../sessions/8a/8a7b0d46ae5984f46081.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

调研完成。报告已写入 `artifacts/openpi_research_report.md`，摘要已更新到 `memory.md`。

## 核心发现

**架构**: π₀ 基于 PaliGemma (SigLIP + Gemma 2B) + Action Expert (Gemma 300M)，总计 ~3.3B 参数。Transformer 深度 **18 层**（不是 32），这意味着原计划的 layers {4,8,12,16,20,24,28,32} 中后四个不存在，需调整为 {2,4,6,8,10,12,14,16}。

**LIBERO 集成**: OpenPI 有完整的一等 LIBERO 支持，包括评测脚本、数据转换、Docker 配置。LIBERO-Plus 扰动评测通过直接替换 LIBERO 库即可使用。

**LoRA 支持**: JAX 原生支持（rank=16, attn+ffn）；PyTorch 官方不支持，但 Issue #842 有完整社区实现（单 4090 可训练，LIBERO 96.95%）。

**激活提取**: PyTorch 版可通过标准 `register_forward_hook` 在 `model.paligemma_with_expert.paligemma.language_model.layers[i]` 注册 hook。

**主要风险**:
1. 🔴 层数仅 18，需重新设计采样策略
2. 🟡 PyTorch LoRA 需要用未合并的社区 PR
3. 🟡 完整激活存储量大（1.7TB），建议只存 action tokens (48GB) 或池化表征 (0.95GB)

---
