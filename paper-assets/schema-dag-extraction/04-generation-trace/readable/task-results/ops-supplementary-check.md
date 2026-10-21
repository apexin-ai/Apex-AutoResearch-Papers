# ops supplementary check

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_supplementary_check_20260518T115144_result.json`
- **Structured JSON:** [`28999915e16788845a09.json`](../../sessions/28/28999915e16788845a09.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

检查完毕。

---

## Supplementary Materials 状态报告

### 1. Appendix 内容（共 21 个 section，全部嵌入 `main.tex`）

appendix 通过 `\appendix` 命令（line 67）直接写在 `main.tex` 中，另有 `prompt_appendix.tex` 通过 `\input` 引入。

| # | Section | Label |
|---|---------|-------|
| A | Additional Figures (cross-model tables, error taxonomy) | `sec:appendix_figures` |
| B | SDGD Full Protocol and Results | `sec:appendix_sdgd` |
| B.1 | Practical Routing Strategies on RE | `sec:appendix_routing` |
| C | Factorial Analysis and Separability Test | `sec:appendix_factorial` |
| D | Within-Pool CI Details | `sec:appendix_within_pool` |
| E | Controlling for Centrality Confounds (MAVEN) | `sec:appendix_residualized_bcs` |
| F | Batch Composition Results | `sec:appendix_batch_composition` |
| G | Prompt Templates (via `prompt_appendix.tex`) | `sec:appendix_prompts` |
| H | Prompt Version Sensitivity Analysis | `sec:appendix_prompt_sensitivity` |
| H.1 | Cross-Prompt-Variant BCS Correlation | `sec:appendix_prompt_variants` |
| I | BCS Aggregation Sensitivity | `sec:appendix_bcs_sensitivity` |
| J | BCS-Controlled Detailed Results | `app:bcs-controlled-table` |
| K | Within-Pool Analysis Methodology | `app:within-pool-method` |
| L | SCS Embedding Ablation | `app:scs-ablation` |
| M | Pair-to-Batch Aggregation Simulation | `app:aggregation-sim` |
| N | BCS Independence from Type Composition | `app:bcs-composition` |
| O | SCS vs Simple Baselines | `app:scs-baselines` |
| P | Split-Origin Covariate Analysis | `app:split-origin` |
| Q | Cross-Seed Variance Decomposition | `app:variance-decomposition` |
| R | Cross-Domain Connections | `app:cross-domain` |
| S | Cross-Model Validation: LLaMA-3.1-70B | `sec:appendix_cross_model_70b` |
| T | Cross-Model Validation: Gemini 2.5 Flash | `sec:appendix_cross_model_gemini` |
| U | Few-Shot Prompting and Confusability | `sec:appendix_fewshot_bcs` |

### 2. 悬空引用检查

**无悬空引用。** 所有正文中的 `\ref{app:*}` / `\ref{sec:appendix_*}` 均有对应 `\label` 定义。LaTeX 编译日志中无 undefined reference 或 undefined citation 警告。

### 3. `supplementary.tex` 状态

是一个 stub 独立文档，内容仅一句："All supplementary material is included in the appendix of the main paper." 如果 ARR 要求上传单独的 supplementary PDF，这个文件可以直接编译提交。

### 4. Checklist (`checklist.tex`)

已完整填写 A1-A4, B1-B6, C1-C4, D1-D5 (N/A), E1。符合 ARR Responsible NLP Research Checklist 要求。

### 5. 是否建议提交额外 supplementary zip

- `src/` 有 ~50 个实验脚本，`data/` 有 4 个数据集的预处理文件
- Checklist C4 写明 "Code and scripts will be released upon acceptance"
- **建议**：不需要在 review 阶段提交代码 zip。ARR 政策允许但不强制 supplementary materials，且 reviewer 不保证阅读。当前 appendix 内容已经非常充分（21 个 section），所有关键实验细节和 robustness check 都已包含在 PDF 中。

### 6. 潜在问题

- `main.tex` 中有 3 处 `'h' float specifier changed to 'ht'` 警告（无害，LaTeX 自动回退）
- Appendix 全部嵌入 main.tex 单文件（约 618 行），较长但 ARR 不限制 appendix 页数

---
