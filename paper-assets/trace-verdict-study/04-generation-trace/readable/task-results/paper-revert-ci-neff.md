# paper revert ci neff

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_revert_ci_neff_20260515T200208_result.json`
- **Structured JSON:** [`fb1799978b14d5258c3f.json`](../../sessions/fb/fb1799978b14d5258c3f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

编译成功，12 页，无错误。

### 修改报告

| 文件 | 行 | 旧值 | 新值 |
|------|-----|------|------|
| experiments.tex | L30 (Table 1 caption) | `[98.81, 99.91]$^*$` | `[99.58, 100.00]` |
| experiments.tex | L30 (Table 1 caption) | `$^*$CI computed with $N_\text{eff}{=}607$...` | 删除 |
| experiments.tex | L58 (Table 2 body) | `[98.81, 99.91]$^*$` | `[99.58, 100.00]` |
| experiments.tex | L66 (Table 2 caption) | `$^*$CI computed with $N_\text{eff}{=}607$...` | 删除 |
| method.tex | L20 | `For conditions with high input duplication (exception\_only), we report confidence intervals based on $N_\text{eff} = 607$...` | `The \texttt{exception\_only} test set contains 48.99\% duplicate inputs due to representation compactness; all confidence intervals treat samples as independent Bernoulli trials.` |

编译结果：成功，main.pdf 12 页，308511 bytes。

---
