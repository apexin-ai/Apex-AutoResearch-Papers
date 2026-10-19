# ops fix r8 training

**Meta-Brain: Perturbation-Diagnostic Routing of LoRA Experts for Parameter-E cient VLA Robustness** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_fix_r8_training_20260517T014625_result.json`
- **Structured JSON:** [`8371e8fe1f75c51b7bbc.json`](../../sessions/83/8371e8fe1f75c51b7bbc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。总结：

**v3_lora_universal_r8 状态：正常运行中**

- PID 792529 存活，cuda:0 占用 12662MiB，GPU 利用率 99%
- tmux session `v3_lora_universal_r8` 存在
- 当前进度：step=100/10000，loss 从 2.0314 降至 1.0687
- 配置：lora_rank=8, alpha=16, lr=2e-4, batch_size=16
- 训练参数：1,843,200 trainable / 3.5B total (0.05%)
- 每 50 步约 51s，预计总训练时间约 170 分钟

**已执行修复：**
- Registry 状态：PREPARING → QUEUED → RUNNING（含完整 spec）
- 已注册 cron 监控（120s 轮询）

---
