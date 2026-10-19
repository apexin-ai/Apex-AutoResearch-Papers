# ops full status check all 4

**action cond info bottleneck** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_full-status-check-all-4_20260516T035158_result.json`
- **Structured JSON:** [`22ed5f92dba3a5ef5a93.json`](../../sessions/22/22ed5f92dba3a5ef5a93.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## GPU 内存
| GPU | 已用 | 总量 | 占比 | 进程 |
|-----|------|------|------|------|
| GPU 0 | 21573 MiB | 97887 MiB | 22% | PID 675231 (baseline_plus eval, 5331M) + PID 682233 (seed1 train, 16214M) |
| GPU 1 | 22845 MiB | 97887 MiB | 23% | PID 733616 (baseline_std eval, 6601M) + PID 755664 (seed2 train, 16216M) |

OOM 风险: 无（双卡均 <25%）

## ACIB 训练

### seed1 (acib_v5_div_reg)
- **Step: 7400/20000 (37%)**
- task_loss: 0.0754, ib_loss: 0.1595, div_loss: -0.4434
- scorer_std: **0.443** (>0.05? ✅), scorer_mean: 0.551
- Speed: 0.9 steps/s → ETA: **2026-05-16 ~15:45 UTC**（剩余 ~3.9h）
- β: 0.0100（warmup 已完成）
- 状态: **正常** — loss 平稳下降，scorer_std 稳定在 0.43-0.45 未 collapse

### seed2 (acib_v5_div_reg_seed2)
- **⚠️ 日志问题**: log 文件仅包含旧进程输出（step 100-700 → Terminated EXIT_CODE=129）。新进程 PID 755664 存活 19 分钟但 stdout 未写入 `acib_v5_div_reg_seed2.log`（wrapper PID 750952 已死）
- lambda_ent config 确认: **0.0** ✅（config.json + 命令行 `--lambda_ent 0` 双重确认）
- Output 目录仅有 config.json，无 checkpoint（预期：19 min ≈ ~700 steps，首次保存在 step 5000）
- 估算当前 step: ~700-800/20000（~4%），基于 0.6-0.7 steps/s 初始速度
- Speed 估算: 0.6-0.7 steps/s → ETA: **2026-05-16 ~19:30 UTC**（剩余 ~7.6h）
- 状态: **进程存活但无法监控** — GPU 内存正常（16216M），但缺少日志输出

## Baseline Eval

### baseline_plus libero_10
- PID 675231 存活，已运行 2h28m
- 视频进度: task 0 ✅ (10 videos), task 1 ✅ (10 videos), task 2 进行中 (4 videos)
- main.log: `Stepping through eval batches: 8% | 4/50, running_success_rate=75.0%`（当前 task 2, episode 4/50）
- Rollouts 完成: **~104/500** (20.8%) — 2 tasks × 50 + 4 episodes
- 预计完成时间: **2026-05-16 ~21:15 UTC**（剩余 ~9.4h）

### baseline_std libero_10
- PID 733616 存活，已运行 48m
- 视频进度: 仅 task 0 (10 videos)，其余尚未开始
- main.log: 显示前一个进程 (PID 708166) 被 Killed，当前是重启后的新进程
- Rollouts 完成: **~34/500** (6.8%) — task 0 进行中
- 预计完成时间: **2026-05-16 ~22:45 UTC**（剩余 ~10.9h）

## 磁盘
| 分区 | 已用 | 可用 | 占比 |
|------|------|------|------|
| 根分区 (/) | 18G | 13G | **58%** |
| 数据盘 (/root/autodl-tmp) | 57G | 194G | 23% |

---

**需要关注的问题**:
1. **seed2 日志丢失**: PID 755664 在跑但没有日志输出。wrapper 750952 已死，新进程的 stdout 未重定向到 log 文件。进程本身看起来正常（GPU 内存占用正确），但无法追踪训练指标。如需监控需要重新挂载日志。
2. **PID 471056、750952 已死**: 这两个旧 wrapper 进程不再存活，但其子进程（或新启动的进程）仍在运行。

---
