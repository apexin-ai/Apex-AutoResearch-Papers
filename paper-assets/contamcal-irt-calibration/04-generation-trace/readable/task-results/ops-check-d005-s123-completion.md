# ops check d005 s123 completion

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-d005-s123-completion_20260518T172423_result.json`
- **Structured JSON:** [`964fad6fca78a58b2163.json`](../../sessions/96/964fad6fca78a58b2163.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇总

**训练：成功完成。**

- 日志最后一行：`2026-05-19 01:21:29 [INFO] Training complete.`
- 进度：3177/3177 steps (100%), epoch=1
- **Final metrics**：train_loss=**0.9304**, mean_token_accuracy=**0.7568**, entropy=1.042
- 最后一个 logging step (step 3170)：loss=0.8921, mean_token_accuracy=0.7837
- 训练时长：6497s (~1h48m)

**Checkpoint：完整。**

| 文件 | 大小 |
|---|---|
| adapter_model.safetensors | 154 MB |
| adapter_config.json | 1.1 KB |
| tokenizer.json | 10.9 MB |
| tokenizer_config.json | 696 B |
| training_args.bin | 5.8 KB |
| checkpoint-3177/ | 子目录存在 |

**cuda:3：不空闲。** PID 45613 占用 62156 MiB（非原始 PID 36943，说明原训练已结束，当前是新进程）。四块 GPU 全部在跑任务。

---
