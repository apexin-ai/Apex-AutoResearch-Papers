# ops eval misfire audit and submit

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_eval-misfire-audit-and-submit_20260515T031836_result.json`
- **Structured JSON:** [`fb8c48890ad0198d9c4b.json`](../../sessions/fb/fb8c48890ad0198d9c4b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Both GPUs loaded (6791 MiB each). All tasks complete.

---

### Part A: exp_001_eval_15B_d100_s123_aligned → **SUCCESS** (cron 误判确认)
| Benchmark | Accuracy |
|-----------|----------|
| mmlu | 0.5956 |
| gsm8k | 0.6444 |
| arc_challenge | 0.7816 |
| humaneval (pass@1) | 0.2805 |

Registry → DONE, conclusion=success, metrics recorded.

### Part B: exp_001_eval_05B_d005_s123_para_aligned → **SUCCESS** (cron 误判确认)
| Benchmark | Accuracy |
|-----------|----------|
| mmlu | 0.3166 |
| gsm8k | 0.2939 |
| arc_challenge | 0.2912 |
| humaneval (pass@1) | 0.0 |

Registry → DONE, conclusion=success, metrics recorded.

### Part C: 两个 3B eval 已提交
- **cuda:1**: exp_001_eval_3B_d000_v2_s123_aligned — RUNNING, 6791 MiB loaded
- **cuda:2**: exp_001_eval_3B_d000_v2_s123_para_aligned — RUNNING, 6791 MiB loaded
- Cron 监控已设置 (每 8 分钟, job ID: 2bf66d61)

---
