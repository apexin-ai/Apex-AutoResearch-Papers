# debug extract d005 metrics verify gpus

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_debug_extract_d005_metrics_verify_gpus_20260515T163706_result.json`
- **Structured JSON:** [`d05882e6734e9cd03c24.json`](../../sessions/d0/d05882e6734e9cd03c24.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部 registry 更新成功。

## 任务 1 完成 — 1.5B d005 s123 Eval Metrics

| Benchmark | Score | Correct/Total |
|-----------|-------|---------------|
| MMLU | 58.69% | 8241/14042 |
| GSM8K | 64.82% | 855/1319 |
| ARC-Challenge | 75.68% | 887/1172 |
| HumanEval | 25.00% | 41/164 |

两个 registry 条目 (`exp_001_eval_15B_d005_s123_v2`, `exp_001_eval_15B_d005_s123`) 的 metrics 和 checkpoint_path 均已更新。

## 任务 2 — GPU 状态

| GPU | Memory Used | Utilization | PID | Process | Elapsed | Status |
|-----|------------|-------------|-----|---------|---------|--------|
| 0 | 17961/24564 MiB | 33% | 594494 | train_sft.py (3B d100 a32 s123) | 3h18m | **运行中** |
| 1 | 13325/24564 MiB | 37% | 593745 | train_sft.py (3B d100 a32 s42) | 7h11m | **运行中**（非空闲） |
| 2 | 8985/24564 MiB | 66% | 580698 | evaluate.py (3B d005 s123 aligned) | 1h31m | 运行中 |
| 3 | 8985/24564 MiB | 71% | 576735 | evaluate.py (3B d025 s123 aligned) | 1h46m | 运行中 |
| 4 | 9667/24564 MiB | 57% | 590509 | compute_signals.py (3B d000 s42) | 23m39s | **exp_002_signals_3B_v2 还在跑** |
| 5 | 17641/24564 MiB | 31% | 589763 | train_sft.py (3B d025 v3 s42) | 25m12s | **exp_001_sft_d025_3B_v3 还在跑** |

**注意**: GPU 1 不空闲 — PID 593745 占 13.3GB 在跑 3B d100 a32 s42 的 SFT 训练，已运行 7h11m。所有 6 张卡均被占用。

---
