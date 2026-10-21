# audit appendix discoverability

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_appendix_discoverability_20260524T050201_result.json`
- **Structured JSON:** [`42d8c8ef3106e75d0209.json`](../../sessions/42/42d8c8ef3106e75d0209.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Results are clear. Here's the audit:

---

## == Appendix Sections ==

| Status | Section | Label | Referenced from |
|--------|---------|-------|-----------------|
| ✅ | Training Configuration | `sec:appendix-hyper` | experiments.tex, method.tex |
| ✅ | Loss Formulation Search | `sec:appendix-loss` | method.tex (×2) |
| ✅ | Instruction Retention Details | `sec:appendix-ir` | discussion.tex |
| ✅ | Long-Conversation AR Evaluation | `sec:appendix-n5` | experiments.tex (×2) |
| ✅ | Statistical Test Details | `sec:appendix-stats` | experiments.tex |
| ✅ | Llama-3.1-8B Complete Results | `sec:appendix-llama` | analysis.tex |
| ❌ | **Additional Visualizations** | `sec:appendix-viz` | 正文无引用 |
| ❌ | **Per-Layer Gate Profile** | `sec:appendix-gate-profile` | 正文无引用 |
| ❌ | **Scheduled Sampling Implementation** | `sec:appendix-ss` | 正文无引用 |
| ❌ | **Computational Cost Analysis** | `sec:appendix-cost` | 正文无引用 |
| ❌ | **Qualitative Steering Examples** | `sec:appendix-examples` | 正文无引用 |
| ❌ | **Gradient Conflict Analysis** | `sec:appendix-gradient` | 正文无引用 |
| ❌ | **Training Data Characteristics** | `sec:appendix-data` | 正文无引用 |
| ❌ | **Exposure Bias Scaling** | `sec:appendix-eb-scaling` | 正文无引用 |
| ❌ | **Per-Turn AR GAR Dynamics** | `sec:appendix-ar-gar-dynamics` | 正文无引用 |
| ❌ | **Use of AI Assistants** | `sec:appendix-ai` | 正文无引用 |
| ✅ | Full Attention Steering Results | `sec:appendix-steering` | experiments.tex |

## == Appendix Tables ==

| Status | Table | Label | Referenced from |
|--------|-------|-------|-----------------|
| ❌ | **Training hyperparameters** | `tab:hyperparams` | 正文无 `\ref` (仅通过 section 引用间接可达) |
| ❌ | **Loss formulation iterations** | `tab:loss-iterations` | 正文无引用 |
| ❌ | **Instruction retention by category** | `tab:ir-results` | 正文无引用 |
| ❌ | **AR GAR on N=5 ten-turn** | `tab:n5-ar` | 正文无引用 |
| ❌ | **Consolidated statistical tests** | `tab:stat-tests` | 正文无引用 |
| ❌ | **Llama complete results** | `tab:llama-full` | 正文无引用 |
| ❌ | **Per-layer gate values** | `tab:gate-profile` | 正文无引用 |
| ❌ | **Computational cost** | `tab:cost` | 正文无引用 |
| ❌ | **Qualitative steering examples** | `tab:examples` | 正文无引用 |
| ❌ | **Training/eval data stats** | `tab:data-stats` | 正文无引用 |
| ❌ | **Full steering results** | `tab:steering-full` | 正文无引用 |

## == Appendix Figures ==

| Status | Figure | Label | Referenced from |
|--------|--------|-------|-----------------|
| ❌ | **Gate profile heatmap** | `fig:gate-heatmap` | 正文无引用 |
| ❌ | **Cross-model gate comparison** | `fig:gate-crossmodel` | 正文无引用 |
| ❌ | **Per-turn AR GAR decay** | `fig:ar-gar-perturn` | 正文无引用 |
| ❌ | **Gate value distributions** | `fig:gate-distribution` | 正文无引用 |
| ❌ | **Training loss curves** | `fig:training-loss` | 正文无引用 |
| ❌ | **Gradient conflict heatmap** | `fig:gradient-heatmap` | 正文无引用 |
| ❌ | **Exposure bias scaling** | `fig:eb-scaling` | 正文无引用 |
| ❌ | **Per-turn AR GAR curves** | `fig:kl_ar_gar_curves` | 正文无引用 |
| ❌ | **Mid-turn AR GAR bar** | `fig:kl_ar_gar_bar` | 正文无引用 |

---

## 总结

- **Sections**: 7/17 有正文引用，**10 个无引用**
- **Tables**: 0/11 有正文直接 `\ref` 引用（所有 table 都只在 appendix 内部被引用）
- **Figures**: 0/9 有正文引用

注意：appendix 内部的 tables/figures 被它们所属的 appendix section 间接覆盖（如 `tab:hyperparams` 在 `sec:appendix-hyper` 中，而该 section 被正文引用）。但严格来说，reviewer 检查可发现性时，**10 个 section** 完全没有正文 pointer，读者无法从正文知道这些附录内容的存在。特别需要关注的高价值未引用 section：

1. **`sec:appendix-cost`** — 计算成本分析，reviewer 常问
2. **`sec:appendix-gradient`** — 梯度冲突分析，支撑 PCGrad 讨论
3. **`sec:appendix-ss`** — 调度采样实现细节
4. **`sec:appendix-data`** — 数据特征，可复现性相关
5. **`sec:appendix-eb-scaling`** — 曝光偏差缩放分析
6. **`sec:appendix-examples`** — 定性示例
7. **`sec:appendix-ai`** — AI 使用声明（部分会议要求）

---
