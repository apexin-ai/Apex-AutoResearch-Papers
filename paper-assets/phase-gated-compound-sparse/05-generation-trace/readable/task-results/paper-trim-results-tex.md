# paper trim results tex

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_trim_results_tex_20260514T114501_result.json`
- **Structured JSON:** [`462b9305aac9cc7fdb74.json`](../../sessions/46/462b9305aac9cc7fdb74.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

验证完毕，所有编辑正确。

**行数变化**: 200 → 155 行 (−45 行 LaTeX 源码)

**移出内容清单**:
| 元素 | 移至 |
|------|------|
| §5.5 模型架构细节、phase segmentation 说明 | `app:cross-model-details` |
| §5.5 per-problem concordance (ρ=−0.11) | `app:cross-model-details` |
| §5.5 random eviction control (3/4 FAIL) | `app:cross-model-details` |
| §5.5 onset lag 讨论 | `app:cross-model-details` |
| Figure 5 (fig5_crossmodel.pdf) | `app:cross-model-details` |
| §5.6 permutation test 方法段 | `app:stat-validation-details` |
| Table 4 (permutation test 表) | `app:stat-validation-details` |
| Figure 4 (fig4_bootstrap.pdf, forest plot) | `app:stat-validation-details` |
| §5.6 CI 增长分析 | `app:stat-validation-details` |
| §5.6 QW onset threshold + variance 讨论 | `app:stat-validation-details` |

**估计页数节省**: ~2.5–3 页（2 个 figure + 1 个 table + 大量 prose 移出，双栏格式下）

**Table 3 Qwen s020**: 已是 0.23，无需修改。

**label/ref 完整性**: 主体中 `\ref{app:cross-model-details}` 和 `\ref{app:stat-validation-details}` 指向 appendix 中对应 `\label`；移出的 `fig:cross-model`、`fig:permtest-forest`、`tab:permutation` 的 label 均在 appendix 中，主体不再直接引用这些浮动体。

---
