# ops gpu utilization check

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gpu_utilization_check_20260516T083228_result.json`
- **Structured JSON:** [`054a0d3c52765357238d.json`](../../sessions/05/054a0d3c52765357238d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## GPU 利用率

| GPU | util% | mem used/total | 任务 | 状态 |
|-----|-------|---------------|------|------|
| 0 | 48% | 3.6G/24G | 1.5B d005_s123 signals (mmlu s4) | 11/~14 chunks done (~79%) |
| 1 | 55% | 6.7G/24G | 3B d100_a32_s42 signals (mmlu s4) | 4/~14 chunks + 当前 76% (~34%) |
| 2 | 57% | 6.9G/24G | 3B d005_a32_s42 signals (mmlu) | 7/~14 chunks + 当前 75% (~55%) |
| 3 | 65% | 8.6G/24G | 3B-Instruct eval (aligned mc-format) | 运行中 |
| 4 | 58% | 6.7G/24G | 3B d000_a32_s42 signals (mmlu s4) | 6/~14 chunks + 当前 75% (~48%) |
| 5 | 29% | 4.8G/24G | 0.5B d025_s123 signals + 0.5B-Instruct exp008 | 双进程共享 |

## cuda:3 详情

PID 731930 — `evaluate.py --model-path Qwen2.5-3B-Instruct --mc-format aligned --benchmarks mmlu gsm8k arc_challenge humaneval`。3B-Instruct 模型已加载（8.6G VRAM），eval 正在运行（99.4% CPU），不是在下载模型。

## cuda:5 详情

**两个进程共享 GPU 5**：
- PID 701549 (2774 MiB) — `exp008/compute_signals_on_model.py` 0.5B-Instruct signals，从 12:56 运行至今
- PID 727941 (2034 MiB) — `compute_signals.py` 0.5B d025_s123 signals (mmlu)，从 15:42 运行至今

0.5B d025_s123: 4 chunk files 已完成，当前 chunk [4000:5000] 约 76%。

## 3B signals 进度 (mmlu s4)

| 模型 | GPU | chunks done | 当前 chunk | 估计总进度 |
|------|-----|-------------|------------|-----------|
| 3B d005_a32_s42 | 2 | 7 (0-7000) | [7000:8000] 75% | ~55% |
| 3B d000_a32_s42 | 4 | 6 (0-6000) | [6000:7000] 75% | ~48% |
| 3B d100_a32_s42 | 1 | 4 (0-4000) | [4000:5000] 76% | ~34% |

## 其他

- **1.5B d005_s123** (GPU 0): 11 chunks done (0-11000)，进度最快 ~79%
- **CmdStan** (PID 734231, CPU): exp006 mmlu_domain_gamma IRT 拟合正在运行
- 6 张卡全部活跃，无空闲 GPU

---
