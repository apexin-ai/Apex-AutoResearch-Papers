# ops llama rsft r3 bf16

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_llama_rsft_r3_bf16_20260517T032639_result.json`
- **Structured JSON:** [`4fbee1c64500b66142b7.json`](../../sessions/4f/4fbee1c64500b66142b7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。总结：

- **死进程已 kill**，cuda:2 显存已释放
- **r3 训练已启动**：PID 408764，cuda:2 占用 28.9GB，正常训练中
- **配置**：bf16 + gradient_checkpointing（硬编码）+ bs=1 + grad_accum=8，effective bs=8
- **预计时长**：~2.8 小时（3312 steps × ~3s/step）
- **Registry**：plan_016_llama_rsft_train_r3 → RUNNING

修正了一个问题：`--rsft_data_path` 需要指向文件 `rsft_train.jsonl` 而非目录。

---
