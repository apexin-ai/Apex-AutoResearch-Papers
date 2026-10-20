# fix batchsize16 restart

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_batchsize16_restart_20260517T004334_result.json`
- **Structured JSON:** [`d6174eac0100e00ee430.json`](../../sessions/d6/d6174eac0100e00ee430.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结论与处理

**根因**：实验从未实际运行。之前的 Worker 在旧服务器 `westd-41312`（已失效）上声称启动，但：
- 脚本名错误（注册为 `run_batchsize16_nmin8_seed42.sh`，实际为 `run_batchsize16.sh`）
- 旧服务器不再可达
- 无任何日志、输出或进程痕迹

**当前状态**：服务器 westd-47453 全部 4 个 GPU 被占用（4 个训练实验进行中），无法立即启动。

**已执行操作**：
1. 确认脚本 `/root/provenance_weight_training/scripts/run_batchsize16.sh` 存在且参数正确（batch_size=16, n_min=8, tau=0.8, seed=42, scored_data.jsonl, Qwen3-0.6B, WANDB_MODE=disabled）
2. 部署队列启动器（PID 375555），每 30 秒轮询 4 个训练 PID，第一个结束时自动在对应 GPU 启动 batchsize16_nmin8_seed42
3. 更新 registry spec 和 notes

**预计时间线**：GPU 3（bs8_auto_nmin_seed42, 13% 完成）将在约 4 小时后（~12:40 CST）最先释放，届时实验自动启动。

**无法满足的要求**：任务要求"启动后验证 nvidia-smi 显存占用 > 10GB 并等 15 秒二次确认"——由于 GPU 资源不可用，实验尚未实际启动，此验证步骤需在实验启动后单独执行。

---
