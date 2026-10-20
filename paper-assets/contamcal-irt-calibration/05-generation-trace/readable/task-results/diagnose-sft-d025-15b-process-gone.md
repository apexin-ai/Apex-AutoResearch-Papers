# diagnose sft d025 15B process gone

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_sft_d025_15B_process_gone_20260514T174402_result.json`
- **Structured JSON:** [`f737e8dcd7ee6d103b6d.json`](../../sessions/f7/f737e8dcd7ee6d103b6d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 调查结论

**进程消失原因：训练已正常完成，非异常退出。**

关键证据：
- 训练日志最后一行是完整的汇总统计：`train_runtime: 11610.65s`（~3.2h），`epoch: 1.0`，`train_loss: 1.2715`
- learning_rate 已降至 ~1.19e-09（cosine schedule 终点）
- 完成全部 3384/3384 steps
- `lora_adapter/` 目录包含完整的 adapter 产出：
  - `adapter_model.safetensors`（~70MB）
  - `checkpoint-3384/`（最终 checkpoint）
  - tokenizer 文件齐全
- GPU 0 已释放（0MiB，0% util），符合训练完成后的预期状态
- 完成时间：May 15 01:32 UTC

**不需要重启。** 下一步是对该 adapter 跑评估。

---
