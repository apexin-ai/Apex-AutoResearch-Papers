# code exp 013 constraint cache

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp-013-constraint-cache_20260516T080137_result.json`
- **Structured JSON:** [`d81d94b2c9a11d53c5af.json`](../../sessions/d8/d81d94b2c9a11d53c5af.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

**情况 B**：exp-001 不保存原始约束（pipeline 未返回 `raw_constraints`）。

### 已完成修改

**1. `sica/pipeline.py`** — 在 `run_single()` 返回值中添加 `raw_constraints` 序列化：
```python
"raw_constraints": [
    {
        "expression": uc.expression,
        "z3_formula_str": str(uc.z3_formula),
        "weight": uc.weight,
        "source_traces": uc.source_traces,
    }
    for uc in unique_constraints
],
```

**2. `scripts/constraint_ablation.py`** — 支持从 results 文件内联 `raw_constraints` 自动构建 cache（无需单独 `--constraint-cache` 文件）：
```python
if not cache:
    inline_cache = {}
    for p in problems:
        rc = p.get("raw_constraints", [])
        if rc:
            inline_cache[str(p["problem_idx"])] = rc
    if inline_cache:
        cache = inline_cache
```

### 验证结果
- Pipeline dry-run：返回 3 个约束，格式 `{expression, z3_formula_str, weight, source_traces}` ✓
- constraint_ablation.py `--help` 正常 ✓
- 不改变现有逻辑，只增加输出 ✓

### exp-001 状态
- 正在运行（158/804 完成），使用 `--save-intermediates`
- **但**：运行中进程已加载旧 pipeline.py，`raw_constraints` 将全部为空
- exp-001 数据无法回溯提取约束（per_trace 只存了 metadata，trace 文本未保存）

### 后续使用
从 exp-002 起，只要加 `--save-intermediates`，constraint_ablation.py 即可直接用精确模式：
```bash
python scripts/constraint_ablation.py --data-dir results/exp002_results.json
# 自动从 inline raw_constraints 构建 cache，跑 exact mode
```

---
