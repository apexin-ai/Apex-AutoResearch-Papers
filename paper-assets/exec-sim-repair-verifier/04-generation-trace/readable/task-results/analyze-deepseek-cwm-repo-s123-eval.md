# analyze deepseek cwm repo s123 eval

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_deepseek-cwm-repo-s123-eval_20260519T043404_result.json`
- **Structured JSON:** [`d10fd33a0931708990ad.json`](../../sessions/d1/d10fd33a0931708990ad.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry updated. Summary:

**deepseek-cwm-repo-s123 eval results (checkpoint-8844, epoch 2, seq4096)**

| Metric | Value |
|---|---|
| **Accuracy** | 61.9% |
| **Majority baseline** | 72.96% |
| **Gap vs majority** | -11.06 pp |
| **F1 macro** | 51.5 |
| **F1 pass / fail** | 73.96 / 29.04 |
| **Recall pass / fail** | 74.15 / 28.84 |
| **Unparseable rate** | 65.53% (6411/9784) |
| **Total samples** | 9784 (complete) |
| **Correct** | 6056 |
| **Truncated** | 0 |

**结果文件**: `/root/autodl-tmp/eval_results/deepseek_cwm_repo_s123_test/eval_deepseek_cwm_repo_s123.json`

结果低于 majority baseline 11 pp，unparseable rate 高达 65.5%，与 s42 seed 的 CWM repo-level 表现一致（同样高 unparseable）。训练在 step 10045/13266 被 kill（EXIT_CODE=129），但 epoch 2 eval 在此之前已完整完成。

---
