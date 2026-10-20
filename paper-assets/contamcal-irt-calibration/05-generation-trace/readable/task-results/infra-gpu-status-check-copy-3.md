# infra gpu status check

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_gpu-status-check_20260521T032624_result.json`
- **Structured JSON:** [`0dd1b806b1771533c8b3.json`](../../sessions/0d/0dd1b806b1771533c8b3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## westd-29999
| GPU | 显存占用 | 利用率 | 状态 |
|-----|---------|--------|------|
| GPU 0 | 0 / 97887 MiB | 0% | **IDLE** |
| GPU 1 | 42911 / 97887 MiB | 64% | **PID 455006** — `train_sft.py` Qwen2.5-14B d050 s0 (运行 3h15m) |
| GPU 2 | 0 / 97887 MiB | 0% | **IDLE** |
| GPU 3 | 0 / 97887 MiB | 0% | **IDLE** |

- PID 464485 (eval_gemma2_d100_mmlu_s0): **DEAD**
- PID 464631 (eval_gemma2_d100_arc_s0): **DEAD**
- PID 455006 (retrain_qwen14b_d050_s0): **ALIVE** — 3h15m, alpha=32, cuda:1
- tmux sessions: `qwen14b_d050_retrain`

## cqa1-21977
| GPU | 显存占用 | 利用率 | 状态 |
|-----|---------|--------|------|
| GPU 0 | 17125 / 24564 MiB | 85% | **PID 435752** — `evaluate.py` Qwen2.5-7B d025 s0, gsm8k (运行 13m) |

- tmux sessions: `eval_gsm8k_7b`
- active python: 仅上述 eval 进程

## 结论
- Registry 中 6 个 RUNNING 实验，实际只有 **2 个**在跑：westd GPU 1 的 14B d050 训练 + cqa1 GPU 0 的 7B d025 eval
- 3 个 Qwen-14B eval（无 pid）确认是**未提交的占位条目**，westd GPU 3 完全空闲
- 2 个 Gemma2 eval（PID 464485/464631）已**结束**，GPU 0/2 空闲

---
