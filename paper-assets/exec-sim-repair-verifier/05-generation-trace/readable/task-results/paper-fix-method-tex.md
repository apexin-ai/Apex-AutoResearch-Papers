# paper fix method tex

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_fix-method-tex_20260512T205807_result.json`
- **Structured JSON:** [`ffb0fc7a92b0af2f99fc.json`](../../sessions/ff/ffb0fc7a92b0af2f99fc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部引用均指向 `meta2025cwm`，该 key 在 `docs/paper/references.bib` 中存在（line 10）。

---

**修改摘要（`docs/paper/method.tex`）：**

| 修复项 | 位置 | 改动 |
|--------|------|------|
| 编译阻塞 | L31 | `\citep{ding2024cwm}` → `\citep{meta2025cwm}` |
| $c_p$ 定义 | L24 | 补充 "represented as a unified git diff in our experiments" |
| Exact match footnote | L38 | 添加 footnote 说明 exact match 是 CWM accuracy 的 conservative lower bound |
| TRAJ 输入表示 | L57 | 补充 "all tests $T = \{t_1, \ldots, t_n\}$ are concatenated into a single input sequence" |

注意：`paper/method.tex`（另一版本）不含 `\citep{ding2024cwm}`，已使用正确的 `\citet{meta2025cwm}`，且无 $c_p$ 符号（使用 `\texttt{code\_context}(p)` 写法），未做修改。

---
