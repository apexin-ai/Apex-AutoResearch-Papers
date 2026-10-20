# paper writing

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_writing_20260521T200146_result.json`
- **Structured JSON:** [`8006f04cb56eedc0f041.json`](../../sessions/80/8006f04cb56eedc0f041.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

文件已写入 `projects/nlp_variance_gtheory/docs/paper/sections/experiments.tex`。

结构概览：
- **§4.1 Single-Model Baseline** — 6-facet G-study，item_id=61.1%，G=0.918
- **§4.2 Cross-Model Variance** — Table 2: item_id 降至 42.1%，model×item=33.6%，含 D-study 验证（predicted 0.816 vs actual 0.820）
- **§4.3 Format-Conditional Variance Structure** — Table 3: MC vs free-form 二分结构，Figure 1 引用，含 PLACEHOLDER 注释
- **§4.4 Precision Separability** — BF16≈FP16 (Δ=0.23pp)，排除 FP32 后 precision=0.0006%
- **§4.5 Design-Dependent Reproducibility Budgets** — Table 4: 72 vs 631 items (8.8×)，IRT 对比，Figure 3 引用
- **§4.6 Robustness Checks** — 6 项检验压缩在一段内（~150 words）
- **§4.7 PLACEHOLDER** 注释留给 8-model × 5-benchmark 扩展

合规检查：无 em-dash，无 -ing 句尾，无连续过渡词，所有 `\cite` key 均在 references.bib 中（已移除不存在的 `hendrycks2021mmlu`），booktabs 表格，caption 在 tabular 上方，图片路径用无扩展名文件名。

---
