# code fix alpha sweep f2 guard

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fix-alpha-sweep-f2-guard_20260515T012837_result.json`
- **Structured JSON:** [`e910db5d4b60b9d25957.json`](../../sessions/e9/e910db5d4b60b9d25957.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

修复完成，验证通过。

### 修改内容

`analyze_alpha_sweep.py` 中 3 处修改：

1. **`_f2_label()` (line 347)** — 添加 `df_resid` 参数，当 `df_resid < 20` 时返回 `"df_too_low"`
2. **`toda_yamamoto()` (line 293)** — 传入 `df_resid=df_resid`，并在 `df_resid < 20` 时添加 `f2_note` 字段
3. **`perm_granger()` (line 315-329)** — 使用 `permutation_granger_test` 已修复的 `f2_size` 字段替代重算，传递 `df_resid` 和 `f2_note`

### 验证结果

summary.txt 确认 TY 在 α=0.25 下的 f² 标签已从 `"large"` 改为 `"df_too_low"`：

```
α=0.25 token_entropy → distinct_1  toda_yamamoto  f²=21.9383 (df_too_low)
α=0.25 token_entropy → distinct_2  toda_yamamoto  f²=10.4321 (df_too_low)
α=0.25 token_entropy → distinct_3  toda_yamamoto  f²=2.3739  (df_too_low)
```

JSON 输出中所有 TY 和 PG 的 f² 条目均带有 `"effect_size_label": "df_too_low"` 和 `"f2_note": "df_resid=4 < 20, standard benchmarks not applicable"`。

---
