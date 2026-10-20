# ops d025 v3 status check

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_d025_v3_status_check_20260515T202252_result.json`
- **Structured JSON:** [`a50e1806c296caa61660.json`](../../sessions/a5/a50e1806c296caa61660.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**SUCCESS**

**判断依据：**
- `train_v2.log` 显示训练正常完成 1 个 epoch（epoch=1.0），learning rate 衰减至 ~3e-10
- 最终指标：`train_loss=1.1501`, `mean_token_accuracy=0.7342`, `train_runtime=14499s`（~4h）
- 无 error/traceback/OOM

**Checkpoint：**
- 路径：`/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d025_s42/lora_adapter/`
- `adapter_model.safetensors` 存在，114 MB，完整
- 含 tokenizer、adapter_config、training_args，以及中间 checkpoint-3384

**cuda:5 当前状态：** 0 MiB / 0% — 完全空闲。

---
