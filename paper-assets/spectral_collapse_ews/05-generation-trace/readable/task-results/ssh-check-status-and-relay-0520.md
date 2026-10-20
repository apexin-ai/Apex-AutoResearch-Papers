# ssh check status and relay 0520

**Spectral Early Warning Signals for Model Collapse and Their Prevention–Detectability Tradeoff** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_check-status-and-relay-0520_20260520T011350_result.json`
- **Structured JSON:** [`0d8e46a7fd9ecbc3b5b8.json`](../../sessions/0d/0d8e46a7fd9ecbc3b5b8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## exp_011 状态: RUNNING (但 10gen 数据已齐)
- PID: 319889 → 319899 (python), 已运行 8h57m
- 命令: `run_phase1.py --condition fixed_mix --seed 42 --generations 10 --start_gen 6 --real_ratio 0.2 --gpu 0`
- `results.json` 已包含 gen 0-9 全部 10 代数据（最后修改 08:50）
- 进程仍在运行，可能在做 evaluation 或生成 summary

| gen | log_det (SLV) | Δ_t | PPL | eff_rank | distinct_4 |
|-----|--------------|-----|-----|----------|------------|
| 0 | 2366.68 | — | 9.55 | 417.5 | 0.741 |
| 1 | 2367.46 | +0.78 | 10.28 | 476.7 | 0.674 |
| 2 | 2358.31 | -9.15 | 10.74 | 481.6 | 0.498 |
| 3 | 2362.52 | +4.22 | 11.14 | 486.5 | 0.467 |
| 4 | 2379.19 | +16.67 | 11.51 | 490.3 | 0.451 |
| 5 | 2398.93 | +19.74 | 11.83 | 492.7 | 0.438 |
| 6 | 2429.83 | +30.90 | 12.19 | 496.4 | 0.463 |
| 7 | 2436.35 | +6.52 | 12.54 | 496.2 | 0.488 |
| 8 | 2454.30 | +17.96 | 12.96 | 501.5 | 0.501 |
| 9 | 2463.14 | +8.84 | 13.39 | 504.9 | 0.508 |

总 SLV 变化 gen0→9: +96.46 (+4.1%)。Δ_t 全程较小（max +30.9），控制器在 r=0.2 下始终静默（与论文 §4.5 Type II 结论一致）。

---

## exp_010 状态: RUNNING (gen 7/10 完成)
- PID: 283142 → 283147 (python), 已运行 19h22m
- 命令: `run_phase1.py --condition pure_collapse --seed 43 --generations 10 --gpu 0` (CUDA_VISIBLE_DEVICES=1)
- 当前应在 gen 8

| gen | log_det (SLV) | Δ_t | PPL | eff_rank | distinct_4 |
|-----|--------------|-----|-----|----------|------------|
| 0 | 2366.68 | — | 9.55 | 417.5 | 0.741 |
| 1 | 2462.62 | +95.94 | 11.37 | 490.8 | 0.600 |
| 2 | 2466.63 | +4.01 | 13.57 | 496.2 | 0.505 |
| 3 | 2438.38 | -28.25 | 16.22 | 494.0 | 0.478 |
| 4 | 2404.60 | -33.78 | 19.94 | 489.2 | 0.415 |
| 5 | 2365.13 | -39.46 | 24.60 | 480.1 | 0.417 |
| 6 | 2325.01 | -40.13 | 30.06 | 471.9 | 0.408 |
| 7 | 2291.55 | -33.46 | 37.44 | 464.2 | 0.391 |

pure_collapse 典型走势：SLV gen1 暴涨后持续下降（gen2→7 累计 -175），PPL 爆炸式增长（9.55→37.44），eff_rank 持续衰减。

---

## r=0.3 seed43 脚本: EXISTS
- 路径: `/root/spectral_collapse_ews/scripts/launch_mixed_r0.3_seed43.sh`
- 创建时间: May 20 09:10
- 内容: `run_phase1.py --condition fixed_mix --seed 43 --generations 10 --real_ratio 0.3 --gpu 0`
- 注意：脚本中 `--gpu 0` 是 PyTorch device 参数，实际 GPU 由 `CUDA_VISIBLE_DEVICES=${GPU_ID}` 控制（默认 GPU_ID=0 即 cuda:0）

## r=0.3 seed43 进程: NOT_RUNNING
无匹配进程，无结果文件，无日志。

## GPU 状态
- cuda:0: 70% util, 65909/97887 MiB (67.3%) — exp_011 占用
- cuda:1: 62% util, 25017/97887 MiB (25.6%) — exp_010 占用

---

**关键发现**: exp_011 的 10gen 数据已完整写入 results JSON，但 python 进程仍在运行（可能在做 eval/summary），cuda:0 仍被占用。r=0.3 seed43 **未启动**。一旦 exp_011 进程退出释放 cuda:0，应立即启动 `bash launch_mixed_r0.3_seed43.sh 0` 接力。是否需要我监控 exp_011 进程并在结束后自动启动？

---
