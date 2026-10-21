# diag exp 001 eval 3B d100 v2 para aligned

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_exp_001_eval_3B_d100_v2_para_aligned_20260515T005025_result.json`
- **Structured JSON:** [`f3ba143bd04855285f7f.json`](../../sessions/f3/f3ba143bd04855285f7f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**判定：SUCCESS** — 4 个 benchmark 全部完成，registry 已更新为 DONE，cron 不存在无需清除。

**Metrics（v2 para_aligned vs 前版 v1 para_aligned）：**

| Benchmark | v2 | v1 | Δ |
|---|---|---|---|
| mmlu | 0.659 | 0.676 | -0.017 |
| gsm8k | 0.583 | 0.614 | -0.031 |
| arc_challenge | 0.809 | 0.828 | -0.019 |
| humaneval | 0.115 | — | — |

v2 各指标相比 v1 均有小幅下降（1.7~3.1 个百分点）。

---
