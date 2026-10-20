# ops investigate process gone

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_investigate-process-gone_20260516T024446_result.json`
- **Structured JSON:** [`223cd9858c2afcf1da68.json`](../../sessions/22/223cd9858c2afcf1da68.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All data collected. Here's the report:

---

## 实验 1: exp_002_signals_3B_d025_v3_s42 (cuda:5)

**状态: STILL RUNNING**

报告的 PID 663047 已退出，但其子进程链仍在运行：
- PID 663052 (bash wrapper `run_signals_3B_d025_v3_s42.sh`)
- PID 663067 (python `compute_signals.py --signal s4 --benchmark mmlu`), 运行 2h28m

日志显示 mmlu s4 self-critique 进度 96% (6775/7021)，预计约 10 分钟内完成。

**已完成的 signal 文件：**
| 文件 | 大小 |
|------|------|
| signal_s1_embedding_mmlu.json | 7.8MB |
| signal_s1_embedding_gsm8k.json | 734KB |
| signal_s1_embedding_arc_challenge.json | 664KB |
| signal_s2_minkpp_mmlu.json | 2.9MB |
| signal_s2_minkpp_gsm8k.json | 272KB |
| signal_s2_minkpp_arc_challenge.json | 250KB |

**待完成：** s4_selfcritique (mmlu 进行中 ~96%，gsm8k/arc_challenge 未开始)。无 .done sentinel。

---

## 实验 2: exp_001_eval_3B_d025_v3_s42_batch (cuda:3)

**状态: PARTIAL SUCCESS**

日志文件不存在（`*d025_v3*batch*` 无匹配），可能以不同命名方式启动。

**aligned eval: SUCCESS**
- `.done` sentinel 存在，完成时间 10:33
- 产出文件：eval_results.json (1.96MB), correctness_matrix.json (105KB), item_responses.json (2.2MB)
- 指标：
  - **MMLU: 0.6242**
  - **GSM8K: 0.6823**
  - **ARC-Challenge: 0.8225**

**para_aligned eval: NOT COMPLETED**
- 目录已创建但为空，无任何结果文件
- cuda:3 已释放（0 MiB），进程已退出
- 可能是 batch 脚本在 aligned 完成后、para_aligned 启动前退出

---

## GPU 状态总表

| GPU | 显存占用 | 利用率 | 状态 | 运行任务 |
|-----|---------|--------|------|---------|
| cuda:0 | 9017/24564 MiB | 65% | **BUSY** | PID 642757: eval d100_a32_s123 para_aligned |
| cuda:1 | 8985/24564 MiB | 70% | **BUSY** | PID 676497: eval d000_s42 a32 aligned |
| cuda:2 | 8985/24564 MiB | 63% | **BUSY** | PID 679190: eval d005_s42 a32 aligned |
| cuda:3 | 0/24564 MiB | 0% | **IDLE** | — |
| cuda:4 | 6931/24564 MiB | 59% | **BUSY** | PID 668217: signals d025_s123 s4 mmlu |
| cuda:5 | 7805/24564 MiB | 61% | **BUSY** | PID 663067: signals d025_v3_s42 s4 mmlu |

**cuda:3 空闲可用。** para_aligned eval 需要重新提交。

---
