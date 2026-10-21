# ops westb sft fix

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_westb_sft_fix_20260520T094800_result.json`
- **Structured JSON:** [`87ee355dc439bc14bee7.json`](../../sessions/87/87ee355dc439bc14bee7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

任务完成。总结：

**诊断结果**：
- `sft_recovery.py` 的 `--gpu 0` 参数在 import torch 前覆写 `CUDA_VISIBLE_DEVICES=0`，导致框架注入的 `CUDA_VISIBLE_DEVICES=1` 被覆盖，两个 SFT 都落到物理 GPU 0
- 单卡 SFT 约 50GB，无需 gradient_checkpointing

**当前状态**：
- **CKA-only v2**: 已完成 (DONE)，train_loss=0.3481，模型已保存
- **Standard v2**: 已重新提交，在 GPU 0 上正常训练中（CKA-only 已释放），step ~14/935，预计 ~18:08 UTC 完成

**后续**: 未来使用 submit_training_job 时，命令中不要传 `--gpu` 参数，让框架的 CUDA_VISIBLE_DEVICES 生效；或修改 `sft_recovery.py` 第 22 行在环境变量已存在时跳过覆写。

---
