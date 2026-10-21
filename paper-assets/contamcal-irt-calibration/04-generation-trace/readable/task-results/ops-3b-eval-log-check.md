# ops 3B eval log check

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_3B-eval-log-check_20260515T141518_result.json`
- **Structured JSON:** [`6070aa4132dc25192bb6.json`](../../sessions/60/6070aa4132dc25192bb6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 进度报告

### exp_001_eval_3B_d000_s123_aligned (cuda:3, PID 551219)
| Benchmark | 状态 | 结果 |
|-----------|------|------|
| MMLU | done | 0.6332 (8892/14042) |
| GSM8K | done | 0.1812 (239/1319) |
| ARC_Challenge | done | 0.8328 (976/1172) |
| HumanEval | **running** | 55% (90/164), ~9min 剩余 |

### exp_001_eval_3B_d005_s42_aligned (cuda:5, PID 551290)
| Benchmark | 状态 | 结果 |
|-----------|------|------|
| MMLU | done | 0.6345 (8909/14042) |
| GSM8K | done | 0.2077 (274/1319) |
| ARC_Challenge | done | 0.8294 (972/1172) |
| HumanEval | **running** | 26% (43/164), ~15min 剩余 |

两个实验都在最后一个 benchmark (HumanEval)，预计 **~15 分钟内全部完成**。

注意：这两个实验没有 tmux session（可能是 nohup 启动的），日志在 `/tmp/` 下。log_path 已补录到 registry 顶层字段。

---
