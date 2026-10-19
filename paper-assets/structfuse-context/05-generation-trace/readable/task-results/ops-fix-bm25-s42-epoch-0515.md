# ops fix bm25 s42 epoch 0515

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_fix-bm25-s42-epoch-0515_20260515T130542_result.json`
- **Structured JSON:** [`a3ac5215d0a5ca772286.json`](../../sessions/a3/a3ac5215d0a5ca772286.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

修改确认完成。Diff 结果：

**run_m2_full_qwen.sh** (3 处改动)：
- L110: 注释 `3 epochs` → `2 epochs, D050 unified regime`
- L143: `--num-epochs 3` → `--num-epochs 2`
- L154: 新增 `--early-stopping-patience 2`

**run_m2_full_starcoder_resume.sh** (1 处改动)：
- L42: `"bm25:42:3"` → `"bm25:42:2"`（early-stopping-patience 已有，无需加）

其他训练段未受影响。

**注意**：starcoder_resume.sh 中 `embedding_distance:42:3` 和 `dataflow_aware:42:3` 仍为 3 epochs（D026 旧策略）。如果 D050 要求所有 s42 统一 2 epochs，这两项也需要改。

---
