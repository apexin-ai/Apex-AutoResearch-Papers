# diagnose bs16 adaptive tau07 seed123 r2

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_bs16_adaptive_tau07_seed123_r2_20260521T232300_result.json`
- **Structured JSON:** [`c3db576732750e17a1c5.json`](../../sessions/c3/c3db576732750e17a1c5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**诊断结果：误报（false alarm）— 训练已正常完成。**

- **进程状态**：PID 645294 已退出，原因是训练跑完了，不是崩溃
- **训练进度**：6103/6103 步 (100%)，耗时 ~4h20m，train_loss=2.534
- **模型保存**：`/root/autodl-tmp/provenance_weight_training/output/models/bs16_adaptive_tau07_seed123/final/`（model.safetensors 1.1GB）
- **Checkpoints**：checkpoint-5500, checkpoint-6000, checkpoint-6103 均完整
- **GPU cuda:0**：仅占用 8.3GB（已释放训练显存），可用于新任务
- **Registry**：已更新为 DONE/success

Cron 监控报警是因为进程正常退出后没有 sentinel 文件，属于 false alarm。

---
