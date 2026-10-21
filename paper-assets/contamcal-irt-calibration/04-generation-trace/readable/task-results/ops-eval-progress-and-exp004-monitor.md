# ops eval progress and exp004 monitor

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_eval_progress_and_exp004_monitor_20260514T043902_result.json`
- **Structured JSON:** [`93b14a516c96208bf8f0.json`](../../sessions/93/93b14a516c96208bf8f0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## GPU 状态

| GPU | Util | VRAM |
|-----|------|------|
| 0 | 8% | 10.1/24.6 GB |
| 1 | 56% | 12.6/24.6 GB |
| 2 | 54% | 7.3/24.6 GB |
| 3 | **0%** | **空闲** |
| 4 | 6% | 18.5/24.6 GB |
| 5 | 16% | 10.4/24.6 GB |

## Eval 实验进度

| 实验 | 当前 benchmark | 进度 | 预计剩余 |
|------|---------------|------|---------|
| eval_3B_d000_s42 | GSM8K | 1239/1319 (94%) | ~35 min |
| eval_15B_d000_s123 | HumanEval | 157/164 (96%) | ~3 min |
| eval_05B_d005 | GSM8K | 1178/1319 (89%) | ~42 min |
| eval_05B_d000_s42_v5 | GSM8K | 744/1319 (56%) | ~2h47m |
| eval_05B_d100_v5 | GSM8K | 749/1319 (57%) | ~2h48m |

**eval_15B_d000_s123** 即将完成（HumanEval 96%），还没有 eval_results.json 产出。

## SFT 训练进度

| 实验 | 进度 | epoch | loss | 预计剩余 |
|------|------|-------|------|---------|
| sft_d100_15B_v2 | 2826/4159 (68%) | 0.67 | 1.27 | ~3h46m |
| sft_d005_15B | 703/3177 (22%) | 0.13 | 1.21 | ~6h42m |

## exp-004 重排监控状态

- **监控进程 (PID 362586)**: 存活，已运行 4m31s
- **Sweep 主进程 (PID 340553)**: 存活，已运行 1h16m，仍在跑 `run_sweep.py subset`
- **监控日志**: "Current seeds saved: 6. Waiting for seed 6 to complete..." — 正在等 auc0.55_n100 的 seed 6 完成
- **重启尚未触发** — sweep_restart.log 不存在，说明监控还在等当前 seed 跑完才会 kill + 重启

**Sweep 结果统计**:

| 条件 | 完成 seeds | 状态 |
|------|-----------|------|
| auc0.55_n20 | 10/10 | ✅ 完成 |
| auc0.55_n50 | 10/10 | ✅ 完成 |
| auc0.55_n100 | 6/10 | ⏳ seed 6 运行中 |
| **auc0.80_n50** | **1/10** | ⏳ 仅 seed 0，等重排后优先跑 |

**结论**: AUC=0.80 目前只完成了 1 个 seed。监控进程在等 auc0.55_n100 当前 seed 结束后才重排，重排生效后 AUC=0.80 会被提前。暂无已完成的 eval 需要 update_registry。

---
