# code classify errors fix v3

**error diag dpo recovery** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_classify_errors_fix_v3_20260512T175013_result.json`
- **Structured JSON:** [`362c2504ea4b2139ed31.json`](../../sessions/36/362c2504ea4b2139ed31.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部验证通过。

---

### 修改差异说明

**6 处修改**：

1. `run_dual_analysis()` 签名加 `is_dry_run: bool = False` 参数
2. 在 Version A/B 计算后、print 前，插入 **Version C** 逻辑：按 `task_type` 分组，每组内按 `error_type` 做 Kruskal-Wallis（组内 error_type < 2 或某类样本 < 3 → insufficient）
3. print 输出末尾追加 Version C 表格 + summary + confound interpretation
4. `p1_analysis.json` 追加 `tautological_warning` 和 `version_c` 字段
5. dry-run 路径：`analysis_recs` 加 `task_type` 字段，调用传 `is_dry_run=True`
6. full classification 路径：同上，传 `is_dry_run=False`

### dry-run 输出

```
⚠️  WARNING: rule-based classification — stats are tautological, for pipeline testing only

=== P1 Correction Span Analysis ===

Version A (Full, N=38):
  action:           N=0
  verification:     N=5, mean=6.00, median=6.0, std=0.00
  planning:         N=33, mean=12.39, median=9.0, std=6.72
  Kruskal-Wallis: H=12.9835, p=0.000314

Version B (Deduplicated, N=38):
  action:           N=0
  verification:     N=5, mean=6.00, median=6.0, std=0.00
  planning:         N=33, mean=12.39, median=9.0, std=6.72
  Kruskal-Wallis: H=12.9835, p=0.000314

Version C (Task-type stratified):
  pick_and_place:                N=3,  error_types=1, H=N/A, p=N/A [INSUFFICIENT]
  pick_clean_then_place:         N=11, error_types=2, H=N/A, p=N/A [INSUFFICIENT]
  pick_cool_then_place:          N=7,  error_types=2, H=N/A, p=N/A [INSUFFICIENT]
  pick_heat_then_place:          N=11, error_types=2, H=6.1395, p=0.013219 [SIGNIFICANT]
  pick_two_obj:                  N=6,  error_types=1, H=N/A, p=N/A [INSUFFICIENT]
  Summary: 1/5 groups significant, 4 groups insufficient
```

### p1_analysis.json

- `"tautological_warning": true` (dry-run 模式)
- `version_a` / `version_b`：与之前一致
- `version_c.groups`：5 个 task_type，pick_heat_then_place 显著 (p=0.013)，其余 4 组 insufficient
- `version_c.summary`：`{"significant": 1, "not_significant": 0, "insufficient": 4, "total": 5}`
- `version_c.confound_warning`: `false`（因为有 1 组 C 显著，不触发 confound 警告）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "significant": 1,
    "not_significant": 0,
    "insufficient": 4,
    "total": 5
  }
}
```

</details>

---
