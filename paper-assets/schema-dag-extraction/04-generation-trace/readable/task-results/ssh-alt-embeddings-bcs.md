# ssh alt embeddings bcs

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_alt-embeddings-bcs_20260514T194037_result.json`
- **Structured JSON:** [`c7d9843aee81ea428fcc.json`](../../sessions/c7/c7d9843aee81ea428fcc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇报如下：

---

## 结果

**模型**: `intfloat/e5-large-v2`（1024 维，CPU 推理）

### 三套 BCS 分布对比

#### Per-type BCS（每个 type 的最大混淆相似度，DAG 构建直接用这个）

| Method | Min | Max | Mean | Std | Range |
|---|---|---|---|---|---|
| Qwen3 mean-pool | 0.8413 | 0.9732 | 0.9139 | **0.0264** | **0.1319** |
| E5 name+definition | 0.8790 | 0.9346 | 0.9087 | 0.0147 | 0.0556 |
| E5 name-only | 0.8984 | 0.9669 | 0.9315 | 0.0155 | 0.0685 |

#### Pairwise cosine similarity（全部 2145 对）

| Method | Min | Max | Mean | Std | Range |
|---|---|---|---|---|---|
| Qwen3 mean-pool | 0.4422 | 0.9732 | 0.8077 | **0.0599** | **0.5309** |
| E5 name+definition | 0.7863 | 0.9346 | 0.8394 | 0.0254 | 0.1483 |
| E5 name-only | 0.7976 | 0.9669 | 0.8617 | 0.0287 | 0.1693 |

### 关键发现

**Qwen3 mean-pool 的区分度实际上最好**——无论是 pairwise std（0.0599 vs 0.0254/0.0287）还是 per-type BCS 的 range（0.1319 vs 0.0556/0.0685），Qwen3 都远优于 E5。E5 作为 sentence embedding 模型反而把所有 type 压到了更窄的 0.79-0.97 区间。

之前说的 "BCS 挤在 0.88-0.92" 对应的是 per-type BCS（0.84-0.97），实际 spread 不算窄。E5 的 per-type BCS 更窄（0.88-0.93 / 0.90-0.97）。

### 产出文件

- Heatmaps: `/root/schema-dag-extraction/data/heatmap_e5_a_name_def.pdf`, `heatmap_e5_b_name_only.pdf`
- Embeddings: `/root/schema-dag-extraction/data/type_embeddings_e5.pt`

### 建议

**Exp 2 继续用 Qwen3 mean-pool embeddings**。E5 sentence embeddings 并未提升区分度，反而降低了。Qwen3 的 5120 维表示在这个 domain-specific 任务上天然有更好的分辨力。

---
