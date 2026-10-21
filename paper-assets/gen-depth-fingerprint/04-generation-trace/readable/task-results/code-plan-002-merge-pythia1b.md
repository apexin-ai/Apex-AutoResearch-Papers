# code plan 002 merge pythia1b

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_plan-002-merge-pythia1b_20260514T210736_result.json`
- **Structured JSON:** [`0a4137d6a22febc46540.json`](../../sessions/0a/0a4137d6a22febc46540.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇报结果：

## 1. 合并数据

合并文件 `data/pythia-1b/generations.jsonl` **已存在**（可能由 `merge_shards.py` 生成），无需重复操作。

- shard0: 2286 行 + shard1: 2269 行 = **4555 行** ✓

## 2. 数据质量

| 指标 | 值 |
|------|-----|
| 总记录数 | **4555** |
| Unique seeds | **995** |
| 空文本 | **0** |
| 字段 | `id, depth, text, seed_id, token_count, model` |

**Depth 分布：**

| depth | records | seeds |
|-------|---------|-------|
| 0 | 995 | 995 |
| 1 | 993 | 993 |
| 2 | 912 | 912 |
| 3 | 851 | 851 |
| 4 | 804 | 804 |

高 depth 的 seed 衰减（995→804）说明部分 seed 在深层生成失败，这是正常的 chain 衰减现象。depth 0 覆盖全部 995 个 seed，质量无问题。

## 3. 评估脚本就绪状态

| 脚本 | 功能 | 状态 |
|------|------|------|
| `extract_features_multi.py` | 多生成器特征提取（Pythia-410M 参考模型 entropy + 表面特征），输出 `features_all.csv` | **就绪**，已包含 pythia-1b 的数据发现逻辑，支持 `--model-name pythia-1b` 增量提取 |
| `cross_generator_eval.py` | Leave-one-generator-out CV，XGBoost 3-class 分类（gen-0/gen-1/gen-2+） | **就绪**，Pythia-1B 已在 `PYTHIA_FAMILY` 列表中 |
| `classify_multi.py` | 完整评估：leave-one-generator-out + leave-one-family-out + pooled 5-fold CV | **就绪**，`MODEL_FAMILIES` 已含 `pythia-1b: pythia` |

Pipeline 流程：`extract_features_multi.py --model-name pythia-1b` → 追加到 `features_all.csv` → `classify_multi.py` / `cross_generator_eval.py` 运行评估。三个脚本均已适配 Pythia-1B，可以直接使用。

---
