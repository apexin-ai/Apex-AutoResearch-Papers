# fix dstudy formula critical

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_dstudy_formula_critical_20260521T043738_result.json`
- **Structured JSON:** [`8a40965e7e1bef52424d.json`](../../sessions/8a/8a40965e7e1bef52424d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

`gstudy_full.py` 运行正常，assertion 通过，D-study G 值单调递增。

## 汇报

### 1. 错误代码位置和修复
- **错误文件**: `temperature_stratified_analysis.json` 中的 `practical.d_study_correct` 和 `practical.min_items_G80`
- **原始生成脚本已不存在**，用 `scripts/fix_dstudy_formula.py` 修复
- **公式修正**: `ni / n_actual` → `n_actual / ni`

### 2. 修复前后 D-study G 值对比

| n_items | 修复前 (错) | 修复后 (对) |
|---------|-----------|-----------|
| 25      | 0.9394    | 0.1949    |
| 50      | 0.8857    | 0.3262    |
| 100     | 0.7948    | 0.4919    |
| 200     | 0.6595    | 0.6595    |
| 500     | 0.4365    | 0.8288    |
| 1000    | 0.2792    | 0.9064    |

- **min_items_G80**: 10 → **414**

### 3. gstudy_full.py
**不受影响**。该脚本已使用正确公式 `n_items_actual / ni`，`llama_single_model_gstudy.json` 的 D-study 值单调递增（25→0.164, 500→0.797）。已添加 monotonicity assertion。

### 4. 全量 Sanity Check
所有 7 个 JSON 文件检查通过，无非单调 D-study 值：
- `binary_data_limitation.json`: clean
- `bootstrap_vs_jackknife.json`: clean
- `cross_model_gstudy.json`: clean
- `fixed_vs_random_sensitivity.json`: clean
- `irt_vs_gtheory.json`: clean
- `llama_single_model_gstudy.json`: D-study OK ✓
- `temperature_stratified_analysis.json`: D-study OK ✓ (修复后)

### 5. 修复后完整 JSON
已在上方输出完整的 `temperature_stratified_analysis.json` 内容，D-study 部分现在正确地从 0.1949（25 items）单调递增到 0.9064（1000 items）。

---
