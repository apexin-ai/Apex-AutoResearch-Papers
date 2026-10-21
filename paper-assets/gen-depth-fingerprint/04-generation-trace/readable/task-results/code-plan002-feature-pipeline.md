# code plan002 feature pipeline

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_plan002-feature-pipeline_20260514T205746_result.json`
- **Structured JSON:** [`70d58120e37cca2124fd.json`](../../sessions/70/70d58120e37cca2124fd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Dry-run 通过。Pipeline 端到端验证成功。

---

## 产出总结

### 1. 现有 Pipeline 架构

```
generate_chain.py  →  merge_shards.py  →  extract_features.py (单模型)
                                       →  extract_features_multi.py (多模型, plan-002 ready)
                                       →  classify_and_eval.py (单模型, 3-class)
                                       →  ablation_analysis.py (消融+趋势+PPL)
```

### 2. plan-002 所需变更清单

| 组件 | 状态 | 需要做什么 |
|---|---|---|
| `generate_chain.py` | 已支持多模型 | 无需改动 |
| `merge_shards.py` | 已支持 `--model-name` | 无需改动 |
| `extract_features_multi.py` | 已存在，支持增量 | 无需改动 |
| `classify_multi.py` | **新建** | ✅ 已完成 |

### 3. 已完成代码

**`classify_multi.py`** — 三种评估模式：
- **Leave-one-generator-out**: 每轮 hold out 1 个生成器，4 个训练
- **Leave-one-family-out**: hold out 整个模型族（pythia/olmo/qwen）
- **Pooled stratified 5-fold CV**: 混合全部数据的 baseline
- 输出 generalization gap（pooled vs leave-out 的 F1 差距）
- 结果保存为 JSON + CSV

### 4. 数据生成后的执行顺序

```bash
# 1. 各模型 merge shards
python merge_shards.py --model-name olmo-2-1b --num-shards 2
python merge_shards.py --model-name qwen3-1.7b --num-shards 2
python merge_shards.py --model-name qwen3-0.6b --num-shards 2

# 2. 多模型特征提取
python extract_features_multi.py --device cuda:0

# 3. 多模型分类评估
python classify_multi.py --input data/features_all.csv
```

**注意**：qwen3-0.6b 数据尚未开始生成，olmo-2-1b 和 qwen3-1.7b 仍在生成中。当前 pythia-1b 已就绪（4555 条），可以先对 pythia-2.8b + pythia-1b 两个模型跑完整 pipeline 做早期验证。

---
