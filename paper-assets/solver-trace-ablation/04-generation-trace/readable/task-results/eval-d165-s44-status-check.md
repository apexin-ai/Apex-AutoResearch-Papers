# eval d165 s44 status check

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_d165-s44-status-check_20260521T142100_result.json`
- **Structured JSON:** [`a43e88e0106613725cfc.json`](../../sessions/a4/a43e88e0106613725cfc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## d165-llama-exec-s44 状态报告

**进程状态**: Running (PID 887114)
- 启动时间: 2026-05-21 22:09（约 12 分钟前，从 step 1 重新开始的新 run）
- 当前进度: **step 76/500** (15%)
- 平均 step 时间: ~10s/step
- **预计剩余: ~70 分钟**（约 23:30 完成）

**GPU**: GPU 0, 36.6G / 97.9G VRAM, 60% util — 正常

**磁盘风险**: `/root/autodl-tmp` 97% 满（9.3G 可用）
- 当前 checkpoint-50 占 6.1G
- save_total_limit=1，每次 checkpoint 轮转需写入 ~6.1G 再删旧的
- 峰值时可用空间会降至 ~3.2G — 勉强够用但很紧

**配置确认**: 
- 数据: `data/train_500_seed42.jsonl` ✓ (C001)
- CUDA_VISIBLE_DEVICES=0 ✓ (C002)
- save_total_limit=1 ✓ (C003)
- seed=44, 500 steps, execution_only

**最后 5 步 reward**:
| step | reward | prove_rate | ISR |
|------|--------|------------|-----|
| 72 | 0.250 | 0.250 | 0.092 |
| 73 | 0.125 | 0.125 | 0.062 |
| 74 | 0.125 | 0.125 | 0.018 |
| 75 | 0.125 | 0.125 | 0.083 |
| 76 | 0.000 | 0.000 | 0.000 |

训练仍在早期阶段，prove_rate 还较低（step 76 时 s42/s43 也类似）。需要等 ~70 分钟完成后再 eval。是否需要我设定定时检查？

---
