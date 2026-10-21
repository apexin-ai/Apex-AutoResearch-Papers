# ssh unify ci coverage numbers

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_unify-ci-coverage-numbers_20260524T091921_result.json`
- **Structured JSON:** [`c0113498586c0ff41eba.json`](../../sessions/c0/c0113498586c0ff41eba.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

`coverage.*71` 匹配的是已修改行中 `$0.771$`（Kendall tau 值），不是旧 CI 数字。`coverage.*68` 无匹配。无遗漏。

## 汇报

| # | 文件 | 行 | 旧文本 | 新文本 |
|---|------|----|--------|--------|
| 1 | `appendix.tex` | L188 | `from 50 Monte Carlo seeds. Empirical CI coverage is 71\%...moderate posterior overconfidence` | `from 200 Monte Carlo seeds. Empirical $c_n$ CI coverage is ${\sim}$65--66\% across $N=8$ and $N=20$...structural posterior overconfidence that does not improve with sample size` |
| 2 | `appendix.tex` | L326 | `empirical coverage ${\sim}$71\%` | `$\theta$ coverage ${\sim}$90\%, $c_n$ coverage ${\sim}$65--66\%` |
| 3 | `experiments.tex` | L52 | `synthetic CI coverage 71\%` | `$c_n$ CI coverage ${\sim}$65--66\%, though $\theta$ achieves ${\sim}$90\%` |
| 4 | `limitations.tex` | L3 | `71\% at $N=50$, 68\% at $N=8$...a structural issue from` | `${\sim}$65--66\% across $N=8$ and $N=20$, 200 seeds...arising from` |

编译结果：0 个语法错误（6 个缺图警告为已有问题，与本次无关）。无遗漏旧数字。所有 4 处现与 Appendix Q (exp-017) 数据一致。

---
