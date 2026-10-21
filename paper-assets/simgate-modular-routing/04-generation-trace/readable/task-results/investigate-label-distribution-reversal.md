# investigate label distribution reversal

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_investigate_label-distribution-reversal_20260514T065722_result.json`
- **Structured JSON:** [`b27f22d1f7a2a80f7bbd.json`](../../sessions/b2/b27f22d1f7a2a80f7bbd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部数据已收集完毕，以下是完整分析。

---

## 分析报告：plan-002 vs plan-004 标签分布反转

### 1. 两个 pipeline 的标签生成逻辑对比

| | plan-002 (`router_sft_train.py`) | plan-004 (`implicit_router_sft.py`) |
|---|---|---|
| **数据源** | `results/plan_c/*/labeled_steps.jsonl` (11 task types, 2040 steps) | `results/plan_c_test_labels/implicit_sft.jsonl` (4 task types, 1814 records) |
| **上游标注脚本** | 未知（但产出无 "no-preference" 记录） | `death_aware_labeling.py` → `sft_triples.jsonl` → `format_implicit_data.py` → `implicit_sft.jsonl` |
| **"no-preference" 处理** | `data_loader.py:60` — RAW_LABEL_MAP 无映射 → **丢弃** | 旧版 format_implicit_data.py **映射为 "internal"** |
| **模型类型** | 分类头 (SequenceClassification) | 因果LM，通过 `[SIMULATE]` 前缀隐式路由 |

### 2. 翻转根因：三重差异叠加

**差异 A — 数据集完全不同：**
- `plan_c/`：11 个 task，2040 steps，**无 "no-preference" 记录**
- `plan_c_test_labels/sft_triples.jsonl`：4 个 task（`death_aware_labeling.py` 产出），1814 steps，其中 **"no-preference" 占 1064 条（58.7%）**

**差异 B — "no-preference" 处理方式截然相反（核心原因）：**

`sft_triples.jsonl` 的原始标签分布：
```
det-preferred:      600  (33.1%)
internal-preferred: 150  ( 8.3%)
no-preference:     1064  (58.7%)   ← 占大头
```

- plan-002 的 `data_loader.py` 丢弃 "no-preference" → 只剩 750 条 → internal=150 (20%), det=600 (80%)
- plan-004 的旧版 `format_implicit_data.py` 把 "no-preference" 全部映射为 "internal" → 1814 条 → **internal=1214 (66.9%), det=600 (33.1%)**

1064 条 "no-preference" 涌入 "internal" 类别，直接翻转了分布。

**差异 C — plan_c/ 本身标签就不同：**

plan-002 实际用的 `plan_c/` 数据更极端（11 task 全量，0 条 no-preference）：
```
internal-preferred: 210  (10.3%)
det-preferred:     1830  (89.7%)
```

### 3. 代码证据

**旧版 format_implicit_data.py 的痕迹：** 当前 `conversion_summary.json` 的字段（`input_path`、无 `skipped`）与当前代码不匹配。当前代码输出 `output_path` + `skipped`，但文件中是 `input_path` 且无 `skipped`。这证实 implicit_sft.jsonl 由**旧版脚本**生成，该版本将 "no-preference" 映射为 "internal"。

**`death_aware_labeling.py:44-46` 的隐性偏置：** 对 "no-preference" episode，使用 `always_internal` trajectory 提取 step actions：
```python
else:
    source_key = "always_internal"  # no-preference 默认用 internal 轨迹
```
所以 "no-preference" 记录不仅标签被设为 internal，连训练文本（action）都来自 internal trajectory。

### 4. 是否是 bug？

**是。** plan-004 的数据生成有两个问题：

1. **旧版 `format_implicit_data.py` 将 "no-preference" 映射为 "internal" 是语义错误。** "no-preference" 意味着两种模态效果相当（双方都死亡或分数持平），不应偏向任一类别。当前版本已修复（正确丢弃），但 implicit_sft.jsonl 未重新生成。

2. **数据源不一致。** plan-002 用 11 task 的 plan_c/，plan-004 用 4 task 的 plan_c_test_labels/，不具可比性。

### 5. 修复方案

- **立即修复**：用**当前版本**的 `format_implicit_data.py` 重新生成 `implicit_sft.jsonl`，会正确丢弃 "no-preference"，产出 750 条 (internal=150, det=600)，分布与 plan-002 方向一致
- **数据量不足问题**：750 条偏少。考虑改用 `plan_c/`（11 task, 2040 steps）作为输入替代 `plan_c_test_labels/`
- **对齐数据源**：让两个 plan 用同一份标注数据，否则 ablation 对比无意义

---
