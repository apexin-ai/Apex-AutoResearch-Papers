# exp conditional pi 002

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_conditional_pi_002_20260522T021207_result.json`
- **Structured JSON:** [`bffa513eb41276c44d00.json`](../../sessions/bf/bffa513eb41276c44d00.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。总结：

**conditional_pi_002 实验已完成**，Registry 已更新为 DONE (negative)，3 个 artifact 已注册。

**关键验证结论**：Perplexity tail family 在 conditional PI 下**不是** top family。

| Family | Avg PI | Avg Rank |
|--------|--------|----------|
| **surprisal** | 0.0890 | 7.3 |
| perplexity | 0.0388 | 7.5 |
| lexical | 0.0043 | 9.7 |

- **Top feature**: var_surprisal (rank 1.4, PI=0.260, bootstrap CI width=0.44)
- **Runner-up**: p90_ppl (rank 1.7, PI=0.238, bootstrap CI width=0.22)
- Surprisal family胜出是因为 var_surprisal 单特征极强（PI=0.260），而 perplexity family 虽然 p90_ppl/p75_ppl 个体排名高，但被 skewness_ppl (rank 13.3) 和 kurtosis_ppl (rank 14.2) 拉低了家族均值
- 两个 top 特征的 bootstrap 排名极度稳定（CI width < 0.5），结论可靠

---
