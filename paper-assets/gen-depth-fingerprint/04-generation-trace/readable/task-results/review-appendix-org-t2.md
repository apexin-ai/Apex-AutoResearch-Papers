# review appendix org t2

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_review_appendix-org-t2_20260519T232849_result.json`
- **Structured JSON:** [`c1ba04343036db5b6e22.json`](../../sessions/c1/c1ba04343036db5b6e22.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Appendix 组织检查报告

### 1. 引用顺序一致性

**正文首次引用顺序**（introduction → method → results → discussion → limitations）：

| # | Label | 首次出现位置 | Appendix 位置 |
|---|-------|-------------|--------------|
| 1 | app:downstream | introduction:22 | **#13** |
| 2 | app:dataset-stats | method:33 | #1 |
| 3 | app:classifier | method:89 | #8 |
| 4 | app:length | method:102 | #2 |
| 5 | app:confusion | results:10 | #7 |
| 6 | app:transfer | results:15 | **#25** |
| 7 | app:domain | results:18 | #10 |
| 8 | app:qlora | results:19 | #5 |
| 9 | app:instruct | results:19 | #11 |
| 10 | app:seed-control | results:25 | **#20** |
| 11 | app:ddr-validation | results:55 | **#22** |
| 12 | app:feature-distributions | results:69 | #15 |
| 13 | app:tost | results:81 | **#21** |
| 14 | app:ablation-table | results:85 | #17 |
| 15 | app:lofo | results:89 | **#6** |
| 16 | app:cross-ref | results:92 | #19 |
| 17 | app:sampling-sensitivity | results:96 | (inside #8) |
| 18 | app:prompt-type | results:96 | **#3** |
| 19 | app:convergence | results:99 | (inside #26) |
| 20 | app:ddr-temp-stability | results:99 | (inside #26) |
| 21 | app:error-analysis | discussion:8 | #12 |
| 22 | app:cross-temp | discussion:9 | #16 |
| 23 | app:finer-depth | discussion:15 | **#4** |

**主要不一致**（粗体标记）：
- **app:downstream**：正文第 1 个引用（introduction），但排在 appendix 第 13 位
- **app:transfer**：正文第 6 个引用，但排在 appendix 第 25 位（倒数第二）
- **app:prompt-type**：正文第 18 个引用，但排在 appendix 第 3 位（过于靠前）
- **app:finer-depth**：正文最后一个引用（discussion），但排在 appendix 第 4 位（过于靠前）
- **app:lofo**：正文第 15 个引用，但排在 appendix 第 6 位
- **app:seed-control / app:tost / app:ddr-validation**：正文第 10-13 位引用，但排在 appendix 第 20-22 位

**从未被正文引用的 appendix**（5 个）：
- app:human-edit（#9）
- app:cross-model-detail（#14）
- sec:appendix-feature-correlation（#18）
- app:gen-subsets-section（#23）
- app:qualitative（#24）

---

### 2. 开场句质量

| Appendix | 开场句 | 评价 |
|----------|--------|------|
| dataset-stats | "Table X reports per-generator sample counts after filtering..." | OK — 说了报告什么，但缺少"为什么需要这个表" |
| length | "Surface diversity features mechanically depend on text length..." | **OK** — 清晰说明动机 |
| prompt-type | "We evaluate depth fingerprinting under three prompt types..." | **OK** |
| finer-depth | "We evaluate finer-grained 5-class depth classification..." | **OK** |
| qlora | "To assess whether depth signal extends beyond handcrafted features..." | **OK** |
| lofo | "We complement the permutation importance analysis..." | **OK** |
| confusion-matrix | "Table X reports the aggregated confusion matrix from..." | OK — 直接说明内容 |
| classifier | "To verify that the depth signal resides in the features rather than the classifier..." | **OK** |
| human-edit | "We assess robustness to post-generation text modification..." | **OK** |
| domain | "We evaluate whether depth signal generalizes beyond Wikipedia..." | **OK** |
| instruct | "Table X summarizes depth classification under instruction tuning..." | 需改进 — 缺少目的说明 |
| error-analysis | "We analyze the distribution and characteristics of binary classification errors..." | **OK** |
| downstream | "Can depth-aware data curation improve downstream LM quality?" | **OK** |
| **cross-model-detail** | `\begin{table}` | **需改进 — 无开场句，直接跳入表格** |
| feature-distributions | "Figure X shows the per-feature depth trend..." | 需改进 — 缺少为什么展示这个图 |
| cross-temp | "Figure X shows cross-temperature transfer results..." | 需改进 — 缺少目的说明 |
| **ablation** | `\begin{table}` | **需改进 — 无开场句，直接跳入表格** |
| feature-correlation | `\section` + `\begin{table}` | **需改进 — 无开场句** |
| seed-control | "To test for topic-level leakage from shared seeds..." | **OK** |
| tost | "To confirm that the near-stationary classification is not a pooling artifact..." | **OK** |
| ddr-validation | "To assess whether the 3/1/3 DDR partition emerges from the data..." | **OK** |
| generator-subsets | "Table X summarizes the generator subsets used across experiments." | OK |
| qualitative-examples | "Table X presents an example generation chain..." | OK |
| transfer | "To isolate the depth signal from generator identity..." | **OK** |
| temperature-stability | "To assess whether the DDR three-way partition generalizes beyond the default temperature..." | **OK** |
| **convergence** | `\begin{figure}` | **需改进 — 无开场句，直接跳入图** |

**需改进的**（4 个无开场句）：`appendix_cross_model_detail.tex`、`appendix_ablation.tex`、`appendix_feature_correlation.tex`、`appendix_convergence.tex`

---

### 3. 交叉引用完整性

所有 `\ref{}` 均有对应 `\label{}` 定义，**无 broken 引用**。

验证范围：appendix 文件中共 64 个交叉引用（5 个 `app:`、37 个 `tab:`、9 个 `fig:`、13 个 `sec:`），全部匹配。

---
