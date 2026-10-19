# research sparsity threshold literature

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_sparsity_threshold_literature_20260516T051258_result.json`
- **Structured JSON:** [`c94a69e018a323fd0f0f.json`](../../sessions/c9/c94a69e018a323fd0f0f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已写入 `artifacts/literature_sparsity_threshold.md`。

核心发现：

1. **Ma et al. (npj AI, 2026)** 直接提出了 "Phase Transition Point" 概念——structured pruning 在 30-45% 崩溃，unstructured 在 55-65%。你们的 50% 断崖恰好落在此区间。

2. **PPL-downstream disconnect 已被多篇论文确认**（Týr-the-Pruner, GISP 等），机制是 layer-wise reconstruction 保 PPL 但不保 multi-step reasoning。

3. **但 activation sparsity prediction 的 PTP 尚未被系统研究**——现有 PTP 文献聚焦 weight pruning/quantization，DejaVu/CATS 等 activation sparsity 工作未深入分析断崖行为。

**Framing 建议**：贡献不是"threshold 存在"（已知），而是 contextual sparsity prediction 中 predictor 误差在高 sparsity 下非线性放大导致的 phase transition，以及 "30% 可用 allocation 修复 vs 50% 不可逆" 这个具体边界的实证发现。这与 Ma et al. 互补但不重叠。

---
