# check rho03 status and eval

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_rho03_status_and_eval_20260522T235651_result.json`
- **Structured JSON:** [`2b337c6bef40d00e55ad.json`](../../sessions/2b/2b337c6bef40d00e55ad.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部 12 个 eval 完成。汇总如下：

## ρ=0.3 Perplexity 评估结果

| 实验 | holdout_ppl | owt_ppl | wiki_ppl |
|------|-------------|---------|----------|
| rho03_adaptive_seed42 | 17.422 | 18.123 | 15.172 |
| rho03_adaptive_seed123 | 17.435 | 18.148 | 15.165 |
| rho03_uniform_seed42 | 17.422 | 18.113 | 15.204 |
| rho03_uniform_seed123 | 17.433 | 18.126 | 15.204 |

**观察**：
- Adaptive vs Uniform 在 holdout 和 OWT 上几乎无差异（差异 < 0.02 PPL）
- Wiki 上 adaptive 略优于 uniform（15.17 vs 15.20，差异 ~0.03）
- 两个 seed 之间的方差很小，结果稳定

---
