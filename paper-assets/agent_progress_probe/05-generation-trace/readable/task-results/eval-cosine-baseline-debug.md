# eval cosine baseline debug

**Are Stagnation Signals Structural? A Systematic Empirical Study of Progress Detection in LLM Agents via Weak Supervision LLM-based agents deployed on software001** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_cosine_baseline_debug_20260514T083817_result.json`
- **Structured JSON:** [`0a98eedf4e29f35319b2.json`](../../sessions/0a/0a98eedf4e29f35319b2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 排查结果

### 结论：Bug，不是 negative result

**原因**：`CosineSimilarityBaseline.fit()` 中 threshold 搜索只考虑了一个方向 (`score >= t → progress`)，但数据中的实际关系是 **stagnation 的 cosine similarity 更高**（符合假设：stagnation 时 agent 重复操作，相邻 embedding 更相似）。

### 关键数据

| | Progress | Stagnation |
|---|---|---|
| mean cosine | 0.6133 | **0.6923** |
| median | 0.6138 | **0.7168** |

- t-test: t=-14.56, p≈0, Cohen's d=0.70 (medium effect)
- 两组分布有显著差异，cosine similarity **是有效特征**，只是代码用反了

### 修复前后对比

| | macro-F1 | F1(stag) | F1(prog) |
|---|---|---|---|
| 修复前 | 0.3129 | 0.1347 | 0.4911 |
| **修复后** | **0.5606** | 0.5059 | 0.6153 |
| Random | 0.4955 | — | — |

### 修复内容

`baselines.py` 的 `CosineSimilarityBaseline`：新增 `self.invert` 字段，`fit()` 中同时搜索正/反两个方向，取 macro-F1 更高的。本地 artifacts 和服务器文件均已更新。

---
