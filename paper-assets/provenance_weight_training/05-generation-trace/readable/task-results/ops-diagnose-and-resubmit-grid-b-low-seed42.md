# ops diagnose and resubmit grid b low seed42

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_diagnose_and_resubmit_grid_b_low_seed42_20260515T055626_result.json`
- **Structured JSON:** [`051602f9c163ebad83ac.json`](../../sessions/05/051602f9c163ebad83ac.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。汇总如下：

---

## grid_b_low_seed42 — 场景 A：进程存活

| 项目 | 值 |
|------|-----|
| PID | 163662 (GPU 1, 74998MiB) |
| tmux | `grid_b_low_seed42` 存活 |
| 当前 b 值 | 0.1 (3个中的第1个) |
| 训练进度 | step 2500/6103 (41%) |
| 训练耗时 | 4:25:13 已用, ~2:07 剩余 (仅 b=0.1) |
| 已有 checkpoint | checkpoint-1500, checkpoint-2000 |
| b=0.2, b=0.3 | 尚未开始 |
| 脚本 | 含 `--eval_data_path data/human/eval_holdout.jsonl --eval_steps 500` ✓ |

**已执行操作：**
- Registry 恢复 RUNNING (DONE→PREPARING→QUEUED→RUNNING)
- failure_reason 清空
- tmux pipe-pane 日志捕获恢复到 `~/runs/provenance_weight_training/grid_b_low_seed42.log`
- 进程未被 kill

**ETA 估算：** b=0.1 剩余 ~2h + b=0.2 ~6.5h + b=0.3 ~6.5h ≈ **~15h**（每个 b 值的 eval 每 500 步约 44 min 开销）。预计 ~05:00 UTC May 16 完成。

**未处理：** cron 监控未重新注册（submit_training_job 会启动新进程，不适用于已存活进程）。需要手动设置 cron 或等完成后由 hook 处理。

---

## seed456 实验进度

| 实验 | GPU | PID | 训练步数 | 进度 | 当前状态 | ETA (wall clock) |
|------|-----|-----|---------|------|---------|-----------------|
| grid_b2_0_seed456 | 0 | 152488 | 3500/6103 | 57% | 训练中 | ~1.5h + eval 开销 |
| grid_b5_0_seed456 | 2 | 158300 | 2500/6103 | 41% | 正在跑 eval (6232/8477) | ~7h (含 eval) |
| grid_b3_0_seed456 | 3 | 158216 | 2500/6103 | 41% | 正在跑 eval (6369/8477) | ~7h (含 eval) |

3 个 seed456 实验均存活正常，PID 与预期匹配（子进程偏移几个 ID）。grid_b2_0 进度最快，预计今天 ~15:30 UTC 完成；另两个预计 ~21:00 UTC。

---
