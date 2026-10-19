# ops fix starcoder s42 epoch 0515

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_fix-starcoder-s42-epoch-0515_20260515T140526_result.json`
- **Structured JSON:** [`8e73e49a580a4a965cc9.json`](../../sessions/8e/8e73e49a580a4a965cc9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个文件的 diff 确认修改正确，只改了预期的行：

**`run_m2_full_starcoder_resume.sh`** (3 处变更):
- 注释: D026 → D050
- `embedding_distance:42:3` → `embedding_distance:42:2`
- `dataflow_aware:42:3` → `dataflow_aware:42:2`
- `--early-stopping-patience 2` 已存在，无需额外添加

**`run_m2_s42_supplement.sh`** (3 处变更):
- 注释: D026 → D050
- `NUM_EPOCHS=3` → `NUM_EPOCHS=2`
- 新增 `--early-stopping-patience 2`

两个备份文件已保存为 `.bak.d050`。当前 StarCoder chain (PID 519791) 在 random_s44，脚本修改已就绪，chain 到达 embedding_distance_s42 时将使用新配置（2 epochs + patience=2）。

---
