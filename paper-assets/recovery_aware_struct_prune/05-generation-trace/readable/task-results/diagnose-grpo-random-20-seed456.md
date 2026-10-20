# diagnose grpo random 20 seed456

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_grpo_random_20_seed456_20260522T162635_result.json`
- **Structured JSON:** [`d6513166930935908072.json`](../../sessions/d6/d6513166930935908072.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

训练已成功启动，模型加载正常。

**汇报：**

1. **磁盘清理**：删除了损坏的 `grpo_random_20_seed456` 目录（12GB，checkpoint-100 内含部分写入的模型权重），释放 12GB
2. **当前可用空间**：33GB（250G 总量，218G 已用，88%）
3. **训练已重提交**：PID 225466，westb-23072:cuda:0，模型已加载并开始训练
4. **预估完成时间**：~3 小时后（约 UTC+8 03:30 左右）

注意：上次运行时 checkpoint-100 实际保存了完整的 12GB model.safetensors，说明训练 100 步完成且 checkpoint 保存成功，仅最终 save_pretrained 因磁盘满失败。这次多了 12GB 余量，保存不会再有问题。

---
