# paper compile check

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_compile_check_20260514T121430_result.json`
- **Structured JSON:** [`a91bf3b156b17f2ebc8a.json`](../../sessions/a9/a91bf3b156b17f2ebc8a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

ACL 模板文件齐全。以下是完整检查报告。

---

## 论文编译 & Figure 完整性检查报告

### 1. Figure 文件完整性 ✅

`docs/paper/figures/` 下 3 个 PDF 文件，全部存在：
| 文件 | 状态 |
|------|------|
| `fig1_head_delta_heatmap.pdf` | ✅ |
| `fig2_compounding_curve.pdf` | ✅ |
| `fig3_allocation_comparison.pdf` | ✅ |

### 2. LaTeX 引用完整性 ✅

**Figure 引用**：3 个 `\includegraphics` 全部指向存在的文件，3 个 `\label{fig:*}` 均有对应 `\ref{fig:*}`。

**Table 引用**：6 个 table label（`main_results`, `budget_sweep`, `heuristic`, `downstream`, `solver_equiv`, `heterogeneity`）全部有对应 `\ref`。

**Section 引用**：所有 `\S\ref{sec:*}` 引用（`profiling`, `heterogeneity`, `profiling_resolution`, `method`, `compounding`, `experiments`, `solver_equiv`, `kv_separation`）均有对应 `\label`。

**Bibliography 引用**：19 个 `\cite` key 全部在 `references.bib` 中有对应条目。ACL 模板文件（`acl.sty`, `acl_natbib.bst`）存在。

### 3. 论文结构 ✅

| 文件 | 行数 | 章节 |
|------|------|------|
| main.tex | 31 | 入口文件 |
| abstract.tex | 7 | Abstract |
| introduction.tex | 50 | Introduction |
| related_work.tex | 17 | Related Work |
| method.tex | 118 | Method |
| experiments.tex | 177 | Experiments |
| analysis.tex | 110 | Analysis |
| conclusion.tex | 19 | Conclusion |
| **Total** | **529** | |

`main.tex` 的 `\input` 顺序：abstract → introduction → related_work → method → experiments → analysis → conclusion。结构完整。

### 4. 数字精度一致性

**PPL 值**：主要结果统一为小数点后 2 位（9.81, 15.45, 11.23, 8.45, 7.16 等）。✅

**发现 1 个问题**：

- **Tab 2 (budget_sweep) 算术误差**：Uniform 15.45 − Constrained 11.23 = **4.22**，但表中写的是 **4.21**。需修正。(`experiments.tex:92`)

**发现 1 个精度不一致**：

- Layer 1 oracle gap 在两处精度不同：`analysis.tex:93` 写 "0.018"，`method.tex:118` 写 "0.0183"。建议统一为 0.018 或 0.0183。

### 5. 其他观察

- `\bibliographystyle` 未显式声明——`acl.sty` 内部处理，编译应无问题。
- 论文总行数 529 行（不含 bib），对 ARR 8 页正文限制来说篇幅合理。

### 总结

**需修复**：1 项（budget_sweep 表 Δ 值 4.21 → 4.22）
**建议统一**：1 项（oracle gap 精度 0.018 vs 0.0183）
**其余检查项全部通过。**

---
