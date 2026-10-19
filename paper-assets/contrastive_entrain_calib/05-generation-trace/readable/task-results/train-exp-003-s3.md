# train exp 003 s3

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_train_exp-003-s3_20260525T124402_result.json`
- **Structured JSON:** [`d3e6aa62e483db31f2dc.json`](../../sessions/d3/d3e6aa62e483db31f2dc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

训练成功启动，第一步已完成。R3 NLI 模型从本地缓存加载成功。

**训练启动报告：**

| 项目 | 值 |
|------|-----|
| exp_id | exp-003-s3 |
| 服务器 | westd-29046, cuda:1 |
| PID | 31710 |
| tmux session | `exp-003-s3` |
| 训练脚本 | `training/run_exp003_s3_r3only.py` (seed=44) |
| 输出目录 | `/root/autodl-tmp/checkpoints/exp003_r3only_seed3/` |
| 日志 | `/root/runs/contrastive_entrain_calib/exp-003-s3.log` |
| 速度 | ~26s/step |
| 预计运行时间 | 8000 steps × 26s ≈ **58 小时 (~2.4 天)** |
| Registry | RUNNING |

**修复记录：** 首次启动因 HuggingFace 网络不可达卡住（R3 model 下载），设置 `HF_HUB_OFFLINE=1` + `TRANSFORMERS_OFFLINE=1` 后从本地缓存加载成功。

---
