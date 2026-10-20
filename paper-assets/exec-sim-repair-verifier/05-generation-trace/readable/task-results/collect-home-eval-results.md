# collect home eval results

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_collect_home-eval-results_20260515T073925_result.json`
- **Structured JSON:** [`0d93e9db91d44118dd14.json`](../../sessions/0d/0d93e9db91d44118dd14.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**ckpt4600 (val) — 已完成，registry 已更新：**

| Metric | Value |
|--------|-------|
| accuracy | 90.07% |
| f1_macro | 85.04% |
| f1_fail | 76.37% (P=89.65%, R=66.52%) |
| f1_pass | 93.71% (P=90.16%, R=97.56%) |
| majority_baseline | 75.88% |
| gap_vs_majority | +14.19pp |
| unparseable | 0 |
| total_samples | 9,335 |

对比 hypothesis 里的 ckpt-4400 val (89.96%)：ckpt-4600 val accuracy **90.07%**，轻微提升 +0.11pp。val-best 从 ckpt-4400 移到 ckpt-4600。

**ckpt4400 (test) — 仍在运行 (39%)，已设置 4.5 分钟后轮询。**

---
