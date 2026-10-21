# code fix few nerd loader

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fix-few-nerd-loader_20260514T173444_result.json`
- **Structured JSON:** [`0516bebd4a9ae48c638d.json`](../../sessions/05/0516bebd4a9ae48c638d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

验证通过。

**结果：**
- Test samples: 37,648（符合预期）
- 第一个样本正确提取了 4 个细粒度实体：`building-other`, `building-hotel`, `location-GPE`, `organization-showorganization`
- 前 100 个样本覆盖 46 个细粒度类型（如 `person-actor`, `location-GPE` 等）

**修改内容：**
1. `load_few_nerd()` 优先从本地 parquet 加载，parquet 不存在时 fallback 到 HF Hub
2. `ner_tags` → `fine_ner_tags`（9 粗粒度 → 66 细粒度）
3. `_tokens_to_spans()` 重写：Few-NERD 标注无 B-/I- 前缀，改为按连续同类 tag_id 分组提取 span
4. `data_dir` 参数化，默认 `/root/schema-dag-extraction/data/parquet/`

---
