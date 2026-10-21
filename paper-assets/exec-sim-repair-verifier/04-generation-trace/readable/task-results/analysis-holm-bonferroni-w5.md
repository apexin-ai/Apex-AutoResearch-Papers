# analysis holm bonferroni w5

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_holm-bonferroni-w5_20260519T092929_result.json`
- **Structured JSON:** [`aeac671f3252e7416583.json`](../../sessions/ae/aeac671f3252e7416583.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果：

**3/6 comparisons survive Holm-Bonferroni correction (α=0.05):**

| Rank | Comparison | Raw p | ×k | Adj p | Sig? |
|------|-----------|-------|-----|-------|------|
| 1 | Repo: CLS vs CWM | 0.003 | 6 | **0.018** | YES |
| 2 | Func: CLS vs CWM (TOST) | 0.007 | 5 | **0.035** | YES |
| 3 | Func: CLS vs TRAJ (TOST) | 0.0087 | 4 | **0.035** | YES |
| 4 | Repo: CWM vs TRAJ | 0.039 | 3 | 0.117 | no |
| 5 | Func: CWM vs TRAJ (TOST)* | 0.044 | 2 | 0.117 | no |
| 6 | Repo: CLS vs TRAJ | 0.385 | 1 | 0.385 | no |

\* Approximate (SE borrowed from CLS-TRAJ).

核心 CLS 优势的两个 claim (CLS vs CWM at both levels, CLS-TRAJ equivalence at function-level) 都 survive 校正。Repo-level 的 CWM vs TRAJ 和 CLS vs TRAJ 不再显著，论文中需要相应弱化措辞。

脚本和 JSON 已保存到 `artifacts/`。

---
