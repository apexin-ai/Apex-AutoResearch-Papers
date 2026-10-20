# code fix embedding v2

**afford invar** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fix-embedding-v2_20260519T180135_result.json`
- **Structured JSON:** [`1f1031199e50804b520f.json`](../../sessions/1f/1f1031199e50804b520f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。结果总结：

### 1. Text Encoder 类型
**SigLIP text encoder** (`google/siglip-base-patch16-256`) — OpenVLA 权重中只有 SigLIP vision encoder，text encoder 需独立加载。使用 base 变体（110M params），与 OpenVLA 使用的 SigLIP 架构一致。

### 2. 修改的文件
- **`diversity_metrics.py`**: 用 `SiglipTextModel` + `AutoTokenizer` 替换了旧的 Llama token embedding 方式（`_load_openvla_embed_weight` 已移除）。批量编码 + pooler_output + L2 归一化。
- **`tier_classifier.py`**: `classify_tier` 简化为仅基于 `embed_sim`（去除 BLEU 条件）。阈值：>0.95 Tier-1, >0.80 Tier-2, ≤0.80 Tier-3。

### 3. Dummy 测试结果

**openvla_embed_sim vs minilm_embed_sim 数值对比：**

| Paraphrase | openvla_sim | minilm_sim |
|---|---|---|
| grab the red cup off the table | 0.906 | 0.928 |
| lift the crimson mug from the desk surface | 0.664 | 0.503 |
| retrieve the red drinking vessel from the tabletop | 0.834 | 0.605 |
| pull out the upper drawer of the cabinet | 0.903 | 0.859 |
| slide open the highest drawer in the storage unit | 0.780 | 0.657 |

SigLIP embedding 对同义句更敏感（更能区分浅层改写 vs 深层改写）。

### 4. Tier 分布
- **Tier-1 (trivial)**: 0 (0%) — 无 sim > 0.95 的改写
- **Tier-2 (moderate)**: 3 (60%) — sim 在 0.80~0.95 之间
- **Tier-3 (deep)**: 2 (40%) — sim ≤ 0.80

分布合理：dummy 数据中大多是有实质性词汇替换的改写，没有极浅层的改写（如仅改变语序），所以无 Tier-1；含同义词替换（crimson/mug）的深度改写正确归入 Tier-3。

---
