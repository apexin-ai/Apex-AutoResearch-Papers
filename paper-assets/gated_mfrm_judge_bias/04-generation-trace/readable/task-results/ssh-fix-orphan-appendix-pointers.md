# ssh fix orphan appendix pointers

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_fix_orphan_appendix_pointers_20260524T052228_result.json`
- **Structured JSON:** [`25d6111e41c4d9c4ca8e.json`](../../sessions/25/25d6111e41c4d9c4ca8e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

None of the overfull warnings are at our edited lines — all pre-existing (in appendix tables at lines 367+).

**验证通过。三个 ref 插入位置：**

| Ref | 文件 | 行号 | 上下文 |
|-----|------|------|--------|
| `app:murphy_topel` | `method.tex` | 103 | "...Murphy-Topel variance correction \citep{murphy1985} to inflate the Stage~3 posterior variance by the estimated Stage~2 sampling variability **(Appendix~\ref{app:murphy_topel})**." |
| `app:cn_recovery` | `experiments.tex` | 52 | "Contamination susceptibility $\hat{c}_n$ exhibits a gradient by model age, directionally consistent with known training data exposure **(Appendix~\ref{app:cn_recovery})**." |
| `app:ci_coverage` | `limitations.tex` | 3 | "$c_n$ credible intervals should be treated as lower bounds on uncertainty **(Appendix~\ref{app:ci_coverage})**, with SBC-based recalibration..." |

- 0 undefined references
- 0 new overfull hbox（9 个全是 pre-existing）
- 编译成功，17 页 PDF

---
