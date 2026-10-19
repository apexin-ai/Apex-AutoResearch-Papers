# data m2 starcoder build and train

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_data_m2_starcoder_build_and_train_20260513T162034_result.json`
- **Structured JSON:** [`90ca78a180838f873bfe.json`](../../sessions/90/90ca78a180838f873bfe.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

任务已提交到 bjb1-42106 cuda:1，tmux session `m2_full_starcoder`。

**执行摘要**：

**Phase 1 (数据构建)** - 正在运行：
- Random/dataflow 数据直接从 Qwen 复制（不依赖编码器）
- 仅用 StarCoder2-3B 重算 embedding negatives，seeds 42/43/44
- 输出: `/root/autodl-tmp/structfuse/full_m2_starcoder_data/`
- 含自动验证：检查 9 train + 9 val 文件行数是否与 Qwen 一致

**Phase 2 (训练)** - 数据验证通过后自动启动：
- 9 runs: 3 strategies (random, embedding_distance, dataflow_aware) × 3 seeds (42, 43, 44)
- StarCoder 参数: batch_size=4, num_negatives=5, epochs=2, lr=2e-5
- 双 checkpoint: `best/` (val_loss) + `best_by_recall_at_1/` (R@1)
- Checkpoint: `/root/autodl-tmp/structfuse/checkpoints/m2_full_starcoder/{strategy}_s{seed}/`
- Log: `/root/runs/m2_full_starcoder/{strategy}_s{seed}.log`

**注意**：实际 seeds 是 42/43/44（与 Qwen 数据匹配），非 42/123/456。`train.py` 已内置双 checkpoint 支持，无需修改。

---
