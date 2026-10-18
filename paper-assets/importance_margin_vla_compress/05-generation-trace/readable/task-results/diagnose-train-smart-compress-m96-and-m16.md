# diagnose train smart compress m96 and m16

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_train_smart_compress_m96_and_m16_20260518T041651_result.json`
- **Structured JSON:** [`15dfbd14388c25605bee.json`](../../sessions/15/15dfbd14388c25605bee.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个实验都**正常完成了训练**，没有失败。监控系统误判。

**关键证据：**
- M96: 日志最后一行 `2026-05-18 11:53:18 [INFO] Training complete.`，跑完 99999/100000 steps，final checkpoint 已保存
- M16: 日志最后一行 `2026-05-18 12:04:21 [INFO] Training complete.`，跑完 99999/100000 steps，final checkpoint 已保存

两个实验都用的 `WANDB_MODE=offline`，所以 cron 监控检测不到 W&B heartbeat，进程结束后被误判为 "dead with no sentinel/W&B"。

```
M96: {"root_cause":"未失败，训练正常完成100k steps。监控误报：W&B offline模式无heartbeat，进程正常退出后被误判为dead","error_type":"infrastructure","fix_steps":["无需修复，训练已完成","将实验状态从failed更新为completed","同步W&B离线数据: wandb sync /root/autodl-tmp/importance_margin_vla_compress/wandb/offline-run-20260518_044901-ckfwhayl"],"can_auto_fix":true,"training_progress":"100k/100k steps完成，最终loss=0.055，eval_loss=0.064","has_checkpoint":true}
M16: {"root_cause":"未失败，训练正常完成100k steps。监控误报：进程正常退出后被误判为异常","error_type":"infrastructure","fix_steps":["无需修复，训练已完成","将实验状态从running更新为completed","同步W&B离线数据: wandb sync /root/autodl-tmp/importance_margin_vla_compress/wandb/offline-run-20260518_050757-9b422m4q"],"can_auto_fix":true,"training_progress":"100k/100k steps完成，最终loss=0.058，eval_loss=0.069","has_checkpoint":true}
```

---
