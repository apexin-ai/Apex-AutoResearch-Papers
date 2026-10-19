# ops trim starcoder supplement to bm25 only

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_trim-starcoder-supplement-to-bm25-only_20260515T175406_result.json`
- **Structured JSON:** [`d4d2e38c4d44a672d983.json`](../../sessions/d4/d4d2e38c4d44a672d983.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

修改完成。

### 结果

**1. Diff（修改前 → 修改后）：**
删除了第 262-269 行（StarCoder 段的 `run_training` 调用 + 空行）：
```diff
262,269d261
<     run_training \
<         "StarCoder" \
<         "/root/autodl-tmp/models/bigcode/starcoder2-3b/bigcode/starcoder2-3b" \
<         "/root/autodl-tmp/structfuse/full_m2_starcoder_data" \
<         "/root/autodl-tmp/structfuse/checkpoints/m2_full_starcoder" \
<         "/root/runs/m2_full_starcoder" \
<         "m2_full_sc2"
<
```

**2. bash -n：** `SYNTAX OK`

**3. StarCoder 段现在只有：** `run_bm25_training` → bm25_s42 / bm25_s43 / bm25_s44

**4. Qwen 段完整未动：** `run_training`（embed_s42 + dataflow_s42）+ `run_bm25_training`（s43 + s44）

备份文件：`run_m2_s42_supplement.sh.bak.pre_trim`

---
