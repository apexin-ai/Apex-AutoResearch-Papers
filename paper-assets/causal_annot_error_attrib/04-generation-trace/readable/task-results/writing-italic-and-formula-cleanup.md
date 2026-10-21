# writing italic and formula cleanup

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_writing_italic_and_formula_cleanup_20260524T063512_result.json`
- **Structured JSON:** [`44488db775f3796a7507.json`](../../sessions/44/44488db775f3796a7507.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

编译成功。0 errors, 0 undefined references, 36 pages（正文 8 页 + 附录）。

---

## 汇报

### 1. 斜体修复清单

| 文件:行号 | 修改 | 原因 |
|---|---|---|
| `appendix_proofs.tex:978` | `\emph{confounding topology}` → `confounding topology` | "confounding topology" 在全文已出现数十次（method.tex、experiments.tex、附录多处），不是首次定义，属于重复强调 |

其余所有 `\emph{}` 和 `\textit{}` 均为合法用途：
- 证明步骤标题（Step 1:, Derivation., Sign analysis. 等）— 标准数学写作
- 首次定义术语（starred-node, protective, immune, conditional indirect effect, component-wise diagonal dominance 等）
- 命题标签（(a), (b), (c)）
- 数学强调（all, constant, causes 等）— 强调普遍性/反直觉结果
- 枚举配置标签（Diagonal-dominant, Moderate noise 等）
- 关键结果强调（structure, vanishes, worsen 等）— 对比/反直觉语境

### 2. 公式重复清理清单

**无重复公式。** 附录中的方程使用与正文不同的数学形式：
- `eq:plim_conf`（附录）用 FWL 标量形式 vs `eq:confounding`（正文）用矩阵形式
- `eq:med_bias`（附录）用 Cov/Var 形式 vs `eq:mediation`（正文）用 λ(C) 参数化形式
- 附录在需要引用正文公式时正确使用了 `\ref{eq:xxx}`（如 line 445: "Substituting back into~\eqref{eq:mediation}"）

### 3. 编译结果

- 0 errors
- 0 undefined references
- 36 pages（正文 8 页以内）

---
