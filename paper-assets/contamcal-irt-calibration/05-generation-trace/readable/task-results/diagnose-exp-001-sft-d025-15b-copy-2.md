# diagnose exp 001 sft d025 15B

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_exp_001_sft_d025_15B_20260514T174132_result.json`
- **Structured JSON:** [`ecb2c66e98ef12af29f0.json`](../../sessions/ec/ecb2c66e98ef12af29f0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结论：**训练已成功完成，需要转 DONE**

**状态**: SUCCESS — 进程正常退出，非异常消失。

**证据**:
- 日志最后一行为训练汇总：`train_runtime=11610.6s`（~3.23h），`epoch=1.0`，`train_loss=1.2715`
- `lora_adapter/` 目录完整：`adapter_model.safetensors`（70.5MB）、`adapter_config.json`、tokenizer 文件、`checkpoint-3384`（最终 step）
- 完成时间：2026-05-15 01:32（启动于 14:19，耗时约 11.2h — 含 checkpoint 保存等开销）
- learning_rate 已衰减至 ~1.19e-9（cosine schedule 末尾），epoch 精确到 1.0

**训练指标**:
- 最终 train_loss: 1.2715
- mean_token_accuracy: 0.7192
- entropy: 1.2623
- 3384/3384 steps 全部完成

**Cron 误报原因**: 进程正常完成退出，tmux session 已无活跃进程，没有写 sentinel 文件也没连 W&B，所以 reconcile 检测为 "gone"。这是 success，不是 failure。

---
