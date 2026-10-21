# analysis mf3 unify n166 direction

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_mf3-unify-n166-direction_20260525T000714_result.json`
- **Structured JSON:** [`fdb04abd6d6ddc192248.json`](../../sessions/fd/fdb04abd6d6ddc192248.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

non_unanimous_problems = 166，确认修复成功。新旧对比：

| 指标 | 旧值 (n=148) | 新值 (n=166) | 变化 |
|------|-------------|-------------|------|
| non_unanimous_problems | 148 | **166** | +18 |
| total_minority_unique_constraints | 2169 | **2603** | +434 |
| minority_exclusive_count | 1596 | **1912** | +316 |
| **minority_exclusive_pct** | **73.58%** | **73.5%** | -0.08pp |
| shared_count | 573 | **691** | +118 |
| shared_pct | 26.42% | **26.5%** | +0.08pp |
| per_problem_exclusive_ratio mean | 0.687 | **0.6688** | -0.018 |
| per_problem_exclusive_ratio std | 0.2357 | **0.2496** | +0.014 |
| per_problem_exclusive_ratio median | 0.7222 | **0.7222** | 不变 |
| variable_overlap_ratio mean | 0.6621 | **0.6611** | -0.001 |
| variable_overlap_ratio n | 146 | **161** | +15 |

**修改内容**：`scripts/minority_constraint_direction.py` 第64-73行。原逻辑在 `normalize_answer` 返回 `None` 时丢弃 trace；新逻辑保留原始答案字符串，这些自由文本 trace 的答案必然 ≠ majority（majority 总是 True/False/Unknown），自动归入 minority 组参与 constraint 方向性分析。

**关键发现**：minority-exclusive ratio 几乎不变（73.58% → 73.5%），说明这 18 个新增问题中的自由文本 trace 与其他 minority trace 表现一致，验证了 Director 的判断——纳入它们不会扭曲分析结论。

---
