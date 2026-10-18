# eval smolvla baseline spatial

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_smolvla_baseline_spatial_20260519T111128_result.json`
- **Structured JSON:** [`d256f558e65b5905d844.json`](../../sessions/d2/d256f558e65b5905d844.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已完成：

- **Eval 已启动**: `eval_smolvla_baseline_spatial` 在 cqa1-33015 cuda:0 上运行
  - 脚本: `eval_success_rate_libero.py --mode baseline --suite libero_spatial`
  - Checkpoint: `checkpoints/libero_baseline/latest/checkpoint.pt` (SmolVLA LoRA fine-tuned, 无压缩)
  - 参数: 50 episodes/task, seed=42, 10 tasks = 500 total episodes
  - tmux session: `eval_smolvla_baseline_spatial`
- **Registry**: `eval_smolvla_baseline_spatial` → RUNNING
- **Cron 监控**: 每 12 分钟检查一次进度（job 01841a32）
- 日志已确认 eval 正常进行中（Task 0 已开始，Ep 3 成功）

预计运行约 1.5-2 小时（参考之前 spatial eval ~6800s）。

---
