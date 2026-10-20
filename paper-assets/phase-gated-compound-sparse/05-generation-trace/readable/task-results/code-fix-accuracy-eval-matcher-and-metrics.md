# code fix accuracy eval matcher and metrics

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fix_accuracy_eval_matcher_and_metrics_20260515T211056_result.json`
- **Structured JSON:** [`ceef096ab628910a4cb1.json`](../../sessions/ce/ceef096ab628910a4cb1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。

## 结果汇总

### 1. Matcher 修复

**修改文件**：`run_accuracy_eval.py` (行 61-140), `rescore_accuracy.py` (新文件)

改动内容：
- **`normalize_answer()`**: 添加 degree symbol 剥离 (`^\circ`, `\circ`, `°`, `\degree`) 和 `\sqrt` 无括号标准化 (`\sqrtN` → `\sqrt{N}`)
- **`_parse_radical()`**: 新函数，解析 `\sqrt{N}` / `c\sqrt{d}` 并做质因子分解化简
- **`answers_match()`**: 在 fraction 比较之后增加 radical 化简比较路径

### 2. 单元测试：14/14 ALL PASS

### 3. 重新评分对比表

| File | Section | Old Acc | New Acc | Changed | Trunc | ExtFail |
|------|---------|---------|---------|---------|-------|---------|
| ds_s015 | dense | 0.52 | 0.52 | 0 | 28 | 0 |
| ds_s015 | sparse (s=0.15) | 0.34 | **0.36** | 1 | 26 | 1 |
| ds_s030 | sparse (s=0.30) | 0.10 | 0.10 | 0 | 33 | 2 |
| ds_dense_n50 | top-level | 0.52 | 0.52 | 0 | 28 | 0 |
| qw_s015 | dense | 0.32 | 0.32 | 0 | 5 | 0 |
| qw_s015 | sparse (s=0.15) | 0.32 | **0.34** | 1 | 4 | 1 |
| qw_s030 | sparse (s=0.30) | 0.14 | 0.14 | 0 | 3 | 7 |
| qw_s020 | importance_s020 | 0.24 | **0.26** | 1 | 2 | 0 |
| qw_s025 | importance_s025 | 0.26 | **0.32** | 3 | 2 | 6 |

**翻转的具体 case (全部 False→True)**：
- `120^\circ` vs `120` (ds_s015 sparse)
- `30` vs `30^\circ` (qw_s015 sparse)
- `11\sqrt{2}` vs `11\sqrt2` (qw_s020, qw_s025)
- `\sqrt{117}` vs `3\sqrt{13}` (qw_s025)
- `72^\circ` vs `72` (qw_s025)

### 4. 总体影响

修正共影响 5 个 problem-condition 对（跨 4 个文件），均为 false negative 翻正。最大影响在 qw_s025（+6pp, 0.26→0.32, 3 题翻转）。Dense baseline 不变，因此 **dose-response 趋势不变** — sparse 条件下的 accuracy 略微上升，但各 sparsity 级别间的相对排序和衰减方向保持一致。

---
