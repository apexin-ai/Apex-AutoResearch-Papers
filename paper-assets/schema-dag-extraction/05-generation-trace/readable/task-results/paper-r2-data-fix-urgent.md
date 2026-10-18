# paper r2 data fix URGENT

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_r2_data_fix_URGENT_20260522T084608_result.json`
- **Structured JSON:** [`995fa5006ce2d847229b.json`](../../sessions/99/995fa5006ce2d847229b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Body text ends on page 8 (with Limitations starting on page 9). The 8-page limit is respected.

---

**修改报告：**

| 文件 | 行号 | 修改前 | 修改后 |
|------|------|--------|--------|
| `abstract.tex` | 4 | `BCS explains ~22% ... ($R^2 \approx 0.22$, ecological level)` | `BCS independently explains ~27% ... (semipartial $R^2 = 0.273$ after controlling for degree centrality; VIF=1.18)` |
| `introduction.tex` | 24 | `explaining ~22% of batch-level variance (ecological level)` | `independently explaining ~27% of batch-level variance (semipartial $R^2 = 0.273$; ecological level)` |
| `results.tex` | 50 | `BCS explains ~22% of cross-batch RE accuracy variance` | `BCS independently explains ~27% ... (semipartial $R^2 = 0.273$, $n = 204$, after controlling for degree centrality)` |
| `results.tex` | 55 | `relative to FewRel (0.218)` | `relative to FewRel's pooled semipartial $R^2 = 0.273$` |
| `results.tex` | 64 | `BCS explains 22% ... ($R^2 = 0.218$, $p < 0.001$)` | `$r = -0.22$, $R^2 \approx 0.05$, $p = 0.027$ ... ~5% in restricted-range; pooled semipartial $R^2 = 0.273$ as primary` |
| `results.tex` | 64 | `pairwise $r^2 \approx 1.5\%$ to batch-level $R^2 \approx 22\%$` | `pairwise $r^2 \approx 1.5\%$ to pooled semipartial $R^2 \approx 27.3\%$` |
| `main.tex` | 595 | `observed batch-level $R^2 = 0.218$` | `observed pooled semipartial $R^2 = 0.273$` |
| `main.tex` | 597 | `observed batch-level $R^2 \approx 22\%$` | `substantial batch-level $R^2$` |
| `main.tex` | 599 | `matching the observed value of 0.218` | `consistent with the pooled semipartial $R^2 = 0.273$ (which falls within the simulation CI)` |
| `main.tex` | 602 | `observed $R^2 = 0.218$` ... `matches the observed value` | `pooled semipartial $R^2 = 0.273$` ... `produces batch-level $R^2$ consistent with the pooled observation` |
| `main.tex` | 605 | `still matching the observed value` ... `observed batch $R^2 = 0.218$` | removed "still matching" phrase; `pooled semipartial $R^2 = 0.273$` |
| `main.tex` | 608 | `$R^2 = 0.218\text{--}0.578$` | `FewRel semipartial $R^2 = 0.273$, DocRED pooled $R^2 = 0.578$` |

**未修改（不同指标）：**
- `main.tex:590` — SCS Spearman ρ = 0.218（SCS-confusion 相关性，非 R²）
- `main.tex:630` — SCS baselines 表中 Spearman ρ = 0.218（同上）

**Author response template** — 已确认无 R²=0.218 引用，已使用正确的 semipartial R²=0.273。

**编译结果：** 26 pages, 0 errors, 0 undefined references, body ≤ 8 pages (Limitations 从 page 9 开始)。

---
