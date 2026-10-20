# infra fix sft launch

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_fix-sft-launch_20260514T061451_result.json`
- **Structured JSON:** [`bcc40b0e6d0bb1113b1d.json`](../../sessions/bc/bcc40b0e6d0bb1113b1d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

训练正常运行中：

- **进度**: 5/144 steps（~3.5%），~8.4s/step
- **4 卡 GPU 均在使用**: 7.5-13.8 GB / 32 GB
- **预计训练时长**: ~20 分钟/epoch，3 epoch 约 1 小时
- lr_scheduler 警告无害，可忽略

代码无需修改——TRL 1.1.0 的 SFTConfig 支持 `max_length` 和 `dataset_text_field`，原代码已正确使用。之前的崩溃可能是残留进程或环境问题导致，清理后重新提交即恢复正常。

---
