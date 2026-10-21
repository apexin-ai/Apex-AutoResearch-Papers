# research ppl downstream disconnect

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_ppl-downstream-disconnect_20260516T020025_result.json`
- **Structured JSON:** [`b685b45e077e3eca7c78.json`](../../sessions/b6/b685b45e077e3eca7c78.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已完成，保存在 `artifacts/literature_ppl_downstream_disconnect.md`，memory.md 已更新。核心发现：

**PPL-downstream disconnect 是已知但未充分研究的现象，我们的工作构成文献空白。**

关键文献支撑：
- **Khanal & Capone (2024)**: 直接证明 SparseGPT/Wanda 50% sparsity 保持 PPL 但下游退化，提出 JS Divergence 替代
- **Xu et al. (2024, EMNLP Findings)**: PPL 在 45-60% sparsity 下无法捕捉能力退化，"normalized PPL shows poor alignment with human-aligned evaluation"
- **Kodathala & Vunnam (2026)**: 最极端案例——N:M pruning 25-30% sparsity 下 factual QA 崩溃 97% 但 PPL 不变
- **Siam et al. (2026)**: 定义 Type 2 degeneration trap（推理断裂→重复循环），与我们的 GSM8K 退化完全吻合

**文献空白**: 没有论文在 contextual sparsity predictor + KL distillation 设置下系统研究过此现象。我们的 PPL 1.96x 但 GSM8K -98% 是目前文献中最极端的 activation sparsity disconnect 案例。

**30% vs 50% 转折点**: TEAL 原文报告 25% safe / 40% minimal / 50% degradation；多篇论文报告 50-60% "sparsity wall"。我们的 30% 数据如果下游保持良好，可以 claim phase transition。

---
