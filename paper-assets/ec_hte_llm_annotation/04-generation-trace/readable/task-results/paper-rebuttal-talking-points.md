# paper rebuttal talking points

**When Debiasing Hurts: An Exact Bias Identity for LLM-Annotated Treatment Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_rebuttal-talking-points_20260524T055908_result.json`
- **Structured JSON:** [`99da1ed9cc8e61e85fde.json`](../../sessions/99/99da1ed9cc8e61e85fde.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

文档已生成并注册。`artifacts/rebuttal_talking_points.md` 包含：

**Must-Address (4 题)**:
1. **方法论新颖性** — 标准技术 + novel setting identification + diagnostic + systematic validation
2. **AUC 三级** — 1.0/0.86/0.63 反映不同评估条件，非 cherry-picking；低 AUC 源于 Δτ≈0 子群
3. **Semi-synthetic vs real data** — 诚实报告，real LLM Δπ不足 + 高FNR；warning paper 定位
4. **(A1) 违反** — outcome-dependent graceful (−2pp)，treatment-dependent breakeven γ_T≈0.10

**Should-Address (4 题)**:
5. **Operating window** — 量化条件本身是贡献；条件满足时 7.4×；diagnostic 在窗口外仍有用
6. **HB vs MLE** — 87.5% configs wins；优势集中在小 n_expert 场景
7. **K scalability** — K=8 coverage 仍 95.6%，RMSE 退化是 bias-variance tradeoff
8. **Debiasing 术语** — 脚注 1 已消歧，measurement error 文献先例

**Pre-emptive (8 题)**: Cross-LLM consistency, stance detection, PPCI composition, bootstrap SE, subgroup selection, 计算成本, 7.4× 基准选择, hyperprior 敏感性。所有数字标注了 registry exp-XXX 或论文 §X.X 来源。

---
