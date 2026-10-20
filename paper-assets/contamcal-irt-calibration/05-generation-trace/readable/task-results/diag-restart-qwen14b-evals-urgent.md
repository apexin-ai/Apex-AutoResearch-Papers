# diag restart qwen14b evals urgent

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_restart-qwen14b-evals-urgent_20260521T032813_result.json`
- **Structured JSON:** [`f16dd27a5c80b1983ab9.json`](../../sessions/f1/f16dd27a5c80b1983ab9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部 4 GPU 满载运行。

## 结果汇总

### 原来的 3 个 eval：全部已成功完成（不是崩溃）

| Job | Accuracy | 状态 |
|-----|----------|------|
| d100 MMLU s0 | 43.85% (6157/14042) | `.done` ✓ |
| d100 ARC s0 | 81.06% (950/1172) | `.done` ✓ |
| partial ARC s0 (d000/d005/d025/d100) | 全部完成 | `.done` ✓ |

GPU 空闲原因是任务跑完了，不是崩溃。

### 新启动的 3 个 MMLU s0 eval

| GPU | Dosage | tmux session | 速度 | 预估完成 |
|-----|--------|-------------|------|----------|
| cuda:0 | d000 | `eval_mmlu_d000_s0` | ~17 it/s | ~11:46 |
| cuda:2 | d005 | `eval_mmlu_d005_s0` | ~17 it/s | ~11:46 |
| cuda:3 | d025 | `eval_mmlu_d025_s0` | ~12 it/s | ~11:52 |

### 当前 GPU 状态

| GPU | VRAM | Util | 任务 |
|-----|------|------|------|
| cuda:0 | 32.7 GB | 95% | MMLU d000 s0 eval |
| cuda:1 | 42.9 GB | 53% | d050 retrain (65%, ~1h45m) |
| cuda:2 | 32.7 GB | 96% | MMLU d005 s0 eval |
| cuda:3 | 32.7 GB | 95% | MMLU d025 s0 eval |

### 仍缺的 Qwen-14B eval

- **MMLU s0 d050**: 等 d050 retrain 完成后再跑
- **ARC s0 d050**: 同上
- **MMLU s42**: 全部 5 个 dosage 都未做（ARC s42 已完成）
- **GSM8K s0**: 全部未做（cqa1 在跑 GSM8K？）

---
