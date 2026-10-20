# train sft standard 25 retry4

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_train_sft_standard_25_retry4_20260516T062038_result.json`
- **Structured JSON:** [`5b9717512cc92f8840a1.json`](../../sessions/5b/5b9717512cc92f8840a1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**sft_standard_25 训练已完成，无需第四次重试。**

总结：
- 之前提交的重试实际成功完成了 2 epochs（1870 steps，35分30秒）
- `model.safetensors` 完好：11.58 GB，339 keys，5.79B params
- `optimizer.pt` 保存时有 RuntimeError，但 optimizer 仅用于 resume training，不影响推理/评估
- GPU 1 已释放（0 MiB）
- 最终 checkpoint 路径：`/root/autodl-tmp/recovery_aware_struct_prune/sft_standard_25/checkpoint-1870/`

---
