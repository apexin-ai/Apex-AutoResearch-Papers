# exp review p0a gen0 leakage

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_review-p0a-gen0-leakage_20260515T134008_result.json`
- **Structured JSON:** [`b072d49bb0fcc9fd1544.json`](../../sessions/b0/b072d49bb0fcc9fd1544.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

P0-A 完成。结果汇总（Binary LOGO: gen-1 vs gen-2+, gen-0 excluded, 21557 samples, 6 generators）：

| Method | F1 | 95% CI | Std | Range |
|--------|-----|--------|-----|-------|
| **7_feature** | 0.7233 | [0.7174, 0.7292] | 0.0511 | 0.1533 |
| **4_baseline_surface** | 0.7239 | [0.7179, 0.7303] | 0.0490 | 0.1399 |
| avg_logprob | 0.7124 | [0.7060, 0.7189] | 0.0441 | 0.1384 |
| 4_baseline | 0.7118 | [0.7052, 0.7182] | 0.0436 | 0.1289 |
| ld_score | 0.7009 | [0.6942, 0.7073] | 0.0454 | 0.1440 |
| fastdetectgpt | 0.6155 | [0.6086, 0.6222] | 0.0562 | 0.1804 |
| binoculars | 0.5240 | [0.5167, 0.5306] | 0.0220 | 0.0621 |

排除 gen-0 后，7-feature depth ensemble（0.723）和 4-baseline+surface（0.724）表现基本持平，都显著高于单 baseline detector。Binoculars 在 binary 任务上接近随机（0.524）。结果保存在 `results/review_p0a_binary_logo.json`，registry 已更新为 DONE。

---
