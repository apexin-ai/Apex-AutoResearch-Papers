# code fix reviewer critical

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fix-reviewer-critical_20260514T163331_result.json`
- **Structured JSON:** [`f9965cd1eca104b4e470.json`](../../sessions/f9/f9965cd1eca104b4e470.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部修改验证完毕。汇总如下：

---

### Fix 1 — BCS 定义：mean → max
- **compute_bcs.py:55-62** — `compute_bcs()` 改为取 max pairwise cosine similarity（原先 `total/count` 取均值，现在遍历所有 pair 取最大值）
- **select_type_batches.py:45-51** — `select_low_bcs()` greedy 准则从 `avg_sim` 改为 `max_sim`（选使最大相似度最小的候选）
- **select_type_batches.py:82-88** — `select_high_bcs()` 同上，改为 `max_sim`（选使最大相似度最大的候选）

### Fix 2 — Random samples 10 → 25
- **run_experiment.py:120** — exp2 的 `select_random_batches(count, 10, ...)` → `(count, 25, ...)`

### Fix 3 — Exp1 加 solo baseline (count=1)
- **run_experiment.py:105-113** — count 列表加入 `1`，变为 `[1, 2, 6, 12, 22, 44, 66]`
- **run_experiment.py:108-111** — count=1 时为每个 active type 单独生成一个 batch（`[{"types": [t], "bcs": 0.0}]`），不走 random sampling

### Fix 4 — 分析改用 ΔF1
- **evaluate.py:126-129,138** — `evaluate_all()` 增加 `per_type_f1` 字段（per-type exact F1 breakdown）
- **analyze_results.py:78→solo_f1参数** — `analyze_exp2()` 新增 `solo_f1` 参数
- **analyze_results.py:85-96** — 每个 batch 计算 `delta_f1 = mean(solo_F1[t] - batch_F1[t])`
- **analyze_results.py:100-110** — 当 solo baseline 覆盖所有 entry 时 `use_delta=True`，用 ΔF1 做 Pearson r、t-test、Cohen's d
- **analyze_results.py:main()** — 从 exp1 count=1 结果提取 per-type solo F1，传给 `analyze_exp2`
- 图表 Y 轴自动切换为 "ΔF1 (solo − batch)"

### Fix 5 — JSON schema 动态 enum
- **run_extraction.py:16-28** — 静态 `JSON_SCHEMA` 替换为 `build_json_schema(batch_types)` 函数，type 字段加 `"enum": sorted(batch_types)`
- **run_extraction.py:111-116** — `GuidedDecodingParams` 和 `SamplingParams` 移入 per-batch 循环内，每个 batch 动态生成 schema

---
