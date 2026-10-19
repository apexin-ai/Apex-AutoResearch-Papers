# fix experiments v1 round2

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_experiments-v1-round2_20260514T230518_result.json`
- **Structured JSON:** [`c9ab1a2ebfff2620cccb.json`](../../sessions/c9/c9ab1a2ebfff2620cccb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

修改完成，共 7 处改动：

**Warning 1 — Table 6 repo count**
- Total 行 repos 从 **123 → 87**，标签改为 "Total (tiered)"
- 新增说明句："The tier classification covers 87 of 123 repositories with extraction output; the remaining 36 repositories produced only failed extraction records and contribute no training instances to the per-tier breakdown."

**Warning 2 — 策略数量不一致**
- §4.1 Baselines 重写：明确 core experiment = 3 strategies × 3 seeds × 2 encoders = 18 runs，BM25 retrieval baseline 和 BM25-mined negatives 作为 "reported separately from the core matrix" 的补充
- §4.2 Hardware："full experiment matrix" → "core experiment matrix"，新增 "BM25-mined negative runs are conducted separately and reported as a supplementary comparison."

**Warning 3 — §4.2 projection head / pooling 同步**
- "linear projection head mapping the last hidden state" → "mean pooling over non-padding positions of the last hidden layer, followed by L2 normalization. A two-layer MLP projection head (Linear→GELU→Linear) maps the pooled representation to a 256-dimensional embedding."

**Info 1 — structural instance count**
- §4.1: 15,160 → **15,133**（与 registry codeql_success 一致，34.3% coverage rate 不变）

**Info 2 — §4.3 措辞**
- "subsequently confirmed at full scale" → "with patterns expected to be confirmed at full scale (pending M2 full results)"

**Info 3 — 无需操作**（Qwen s44 eval@1000=0.5638 已在 registry）

Artifact 已注册：`art_20260514_eccca0`。

---
