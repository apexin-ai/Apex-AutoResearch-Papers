# check eval batch status

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_eval_batch_status_20260514T102915_result.json`
- **Structured JSON:** [`6d12a58a936b1b79b8c1.json`](../../sessions/6d/6d12a58a936b1b79b8c1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## GPU 状态

| GPU | 显存占用 | 利用率 | 实际 PID | 任务 |
|-----|---------|--------|---------|------|
| 0 | 2769/24564 MiB | 100% | 349021 | `compute_signals.py` 0.5B d005 (刚启动 ~2min) |
| 1 | 5857/24564 MiB | 49% | 336765 | `evaluate.py` 1.5B d000 aligned (运行 1h12m) |
| 2 | 3695/24564 MiB | 32% | 332221 | `evaluate.py` 0.5B d000 aligned (运行 1h51m) |
| 3 | 13341/24564 MiB | 31% | 319555 | `train_sft.py` 3B d100 (运行 3h34m) |
| 4 | 21827/24564 MiB | 52% | 335351 | `train_sft.py` 3B d005 (运行 1h19m) |
| 5 | 8985/24564 MiB | 68% | 342940 | `evaluate.py` 3B d000 aligned (运行 38min) |

## 实验状态

| 实验 | GPU | PID | 存活 | 进度 | 结果文件 |
|------|-----|-----|------|------|---------|
| **exp_001_eval_15B_aligned_batch** | cuda:1 | 336765 | ✅ 运行中 1h12m | 正在跑 d000 aligned，d005/d100 尚未开始 | `*_aligned/` 目录为空（进行中） |
| **exp_001_eval_05B_aligned_batch** | cuda:2 | 332221 | ✅ 运行中 1h51m | 正在跑 d000 aligned，d005/d100 尚未开始 | `*_aligned/` 目录为空（进行中） |
| **exp_002_signals_05B** | cuda:0 | 349021 | ✅ 运行中 ~2min | 正在跑 d005 signals (embedding/minkpp/selfcritique) | d000 已有 3 个 signal 文件 |
| **SFT 3B d100** | cuda:3 | 319555 | ✅ 运行中 3h34m | — | — |
| **SFT 3B d005** | cuda:4 | 335351 | ✅ 运行中 1h19m | — | — |
| **Eval 3B d000 aligned** | cuda:5 | 342940 | ✅ 运行中 38min | — | `*_aligned/` 目录为空（进行中） |

注意：原始 PID 346325/335346/342935 是父 shell 进程（0% CPU, ~3MB RSS），实际 GPU 工作进程是上表中的 PID。

**缺失项**：`Qwen2.5-1.5B_d005_s42` 的普通 eval 结果不存在（其他配置的普通 eval 都已完成）。1.5B aligned batch 跑完 d000 后如果要跑 d005 aligned，需要确认 d005 的 checkpoint 是否存在。

---
