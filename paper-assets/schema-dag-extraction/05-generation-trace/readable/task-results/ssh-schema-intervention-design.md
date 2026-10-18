# ssh schema intervention design

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_schema_intervention_design_20260517T145722_result.json`
- **Structured JSON:** [`5c746214cdbb3ac9883a.json`](../../sessions/5c/5c746214cdbb3ac9883a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

## 分析报告

### Phase 1: Top-20 高 SCS Pairs

| Rank | Type A | Type B | SCS |
|------|--------|--------|-----|
| 1 | participant | participant of | 0.9706 |
| 2 | contains administrative territorial entity | located in the administrative territorial entity | 0.9179 |
| 3 | country | country of origin | 0.9051 |
| 4 | member of | part of | 0.9002 |
| 5 | followed by | follows | 0.8969 |
| 6 | follows | part of | 0.8920 |
| 7 | has part | part of | 0.8806 |
| 8 | instance of | member of | 0.8657 |
| 9 | father | mother | 0.8565 |
| 10 | instance of | part of | 0.8476 |
| 11 | follows | member of | 0.8467 |
| 12 | child | mother | 0.8405 |
| 13 | participating team | position played on team | 0.8371 |
| 14 | child | father | 0.8361 |
| 15 | follows | has part | 0.8361 |
| 16 | country | country of citizenship | 0.8292 |
| 17 | followed by | part of | 0.8280 |
| 18 | follows | instance of | 0.8263 |
| 19 | part of | said to be the same as | 0.8262 |
| 20 | follows | said to be the same as | 0.8253 |

- 218 pairs with SCS > 0.7, 1067 pairs > 0.6, mean = 0.5572

### Phase 2-3: 优化后 Renaming 方案（经过两轮迭代，MiniLM 验证）

对 10 个 unique type 实施 renaming，影响 14 个高 SCS pairs：

| # | Type A | Type B (原) | 原 SCS | 重命名 B | 新 SCS | Δ |
|---|--------|------------|--------|---------|--------|---|
| 1 | participant | participant of | 0.9706 | **event involvement** | 0.7200 | -0.2506 |
| 2 | contains admin... | located in admin... | 0.9179 | **situated within governing region** | 0.7878 | -0.1302 |
| 3 | country | country of origin | 0.9051 | **homeland provenance** | 0.6367 | -0.2684 |
| 4 | member of | part of | 0.9002 | **integral segment of** | 0.6375 | -0.2627 |
| 5 | followed by | follows | 0.8969 | **prior entry** | 0.6860 | -0.2108 |
| 6 | has part | part of | 0.8806 | **integral segment of** | 0.5813 | -0.2994 |
| 7 | instance of | member of | 0.8657 | **affiliated with** | 0.6603 | -0.2054 |
| 8 | father | mother | 0.8565 | **female progenitor** | 0.6165 | -0.2400 |
| 9 | child | mother | 0.8405 | **female progenitor** | 0.6347 | -0.2059 |
| 10 | participating team | position played on team | 0.8371 | **athletic role on roster** | 0.6913 | -0.1458 |
| 11 | country | country of citizenship | 0.8292 | **citizenship allegiance** | 0.6125 | -0.2167 |
| 12 | military branch | military rank | 0.8226 | **service rank designation** | 0.6264 | -0.1963 |
| 13 | child | father | 0.8361 | **paternal figure** | 0.6840 | -0.1522 |
| 14 | competition class | winner | 0.8147 | **contest victor** | 0.7728 | -0.0419 |

**平均 SCS 降幅: -0.2019** (0.8695 → 0.6677), **14/14 pairs 均降低**

Cross-check 显示多数 renamed type 是 CLEAN（与其他 80 type 均无 >0.7 的 SCS），仅 "event involvement" 与 "participant" 仍有 0.72 的残余相似度。

### Phase 4: 实验数据状态

- **batch_groups.json**: `artifacts/exp_v2_re_n25/batch_groups.json` 存在，25 low-BCS (mean=0.3624) + 25 high-BCS (mean=0.7982) batches, 每 batch 8 types
- **vLLM/GPU**: RTX PRO 6000 Blackwell (98GB) 空闲，**vLLM 未运行**，需要手动启动 Qwen3-32B-FP8
- **Qwen3-32B-FP8 权重**: 在 `/root/autodl-tmp/.hf_cache/qwen3-32b-fp8/`

### 建议实验脚本结构

```python
# pseudo: run_renaming_intervention.py

# 1. Load batch_groups.json (25 low + 25 high BCS batches)
# 2. For each batch:
#    a. CONTROL: run RE with original type names → accuracy_original
#    b. TREATMENT: apply renaming map to schema → run RE → accuracy_renamed
#    c. Record per-batch: (bcs_group, original_acc, renamed_acc, delta_acc)
# 3. Analysis:
#    - Paired t-test: renamed vs original within high-BCS group
#    - Interaction: does renaming help more in high-BCS than low-BCS?
#    - Per-type: which renamed types improved most?

RENAME_MAP = {
    "participant of": "event involvement",
    "located in the administrative territorial entity": "situated within governing region",
    "country of origin": "homeland provenance",
    "part of": "integral segment of",
    "follows": "prior entry",
    "member of": "affiliated with",
    "mother": "female progenitor",
    "position played on team": "athletic role on roster",
    "country of citizenship": "citizenship allegiance",
    "military rank": "service rank designation",
    "father": "paternal figure",
    "winner": "contest victor",
}
```

结果保存在 `artifacts/scs_renaming_intervention.json`。需要启动 vLLM 才能跑实际的 extraction 实验。

---
