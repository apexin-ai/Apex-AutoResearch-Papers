# ops post restart4 status 28034

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_post-restart4-status-28034_20260519T135144_result.json`
- **Structured JSON:** [`479be0a8cb5464586b8c.json`](../../sessions/47/479be0a8cb5464586b8c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## westd-28034 任务状态汇总

### GPU 状态
| GPU | 利用率 | 显存 | 任务 |
|-----|--------|------|------|
| 0 | 13% | 17660/32607 MiB | exp-004 eval |
| 1 | 100% | 31432/32607 MiB | exp-008v3 training |
| 2 | 0% | 30670/32607 MiB | exp-008v3 training (DeepSpeed rank 1) |
| 3 | 0% | 16508/32607 MiB | exp-016 re-eval |

---

### 1. exp-004 eval (GPU 0) — 运行中
- **PID**: 136205，进程存活
- **当前**: checkpoint-500, **140/362** pairs (~39%)
- **启动**: 21:35 UTC
- **每 checkpoint 约 60 min**，还有 checkpoint-2000 和 checkpoint-8000 待跑
- **结果目录**: `eval/results/` 不存在，结果尚未保存（每个 checkpoint 完成后才写）
- **ETA**: 约 3 小时完成全部 3 个 checkpoint

### 2. exp-016 ActAdd re-eval (GPU 3) — 运行中
- **5 个 alpha**: [0.0, 0.5, 1.0, 2.0, 5.0]，每个约 60 min
- **已完成**: alpha=0.0, 0.5, 1.0（3/5）
- **当前**: alpha=2.0, **80/362** (~22%), 开始于 21:33 UTC
- **待跑**: alpha=5.0
- **结果目录**: `results/exp016_unified_reeval/` 空——脚本在全部 alpha 跑完后才统一保存
- **ETA**: alpha=2.0 剩余~45min + alpha=5.0 ~60min ≈ **~105 min**（约 23:35 UTC）

### 3. exp-008v3 training (GPU 1+2) — 运行中
- **PID**: 103925 (deepspeed), tmux session `exp-008v3` 存活
- **进度**: step **1277/8000** (16%)
- **速度**: ~21s/step
- **启动**: 14:40 UTC（已跑 ~7h10m）
- **Rewards (最近)**:
  - combined_mean 在 0.34–0.66 区间波动
  - r1_mean: 0.0–0.5, r2_mean: 持续 0.0, r3_mean: 0.32–0.84
- **ETA**: 剩余 6723 steps × 21s ≈ **~39 小时**（约 5月21日 13:00 UTC）

---

**总结**: 3 个任务全部在服务重启后存活。exp-016 最快完成（~1.5h），exp-004 约 3h，exp-008v3 约 39h。r2_mean 持续为 0 值得关注。

---
