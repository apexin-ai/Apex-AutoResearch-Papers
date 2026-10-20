# code d134 analysis isr star patch

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_d134-analysis-isr-star-patch_20260518T233104_result.json`
- **Structured JSON:** [`c0be21b87b8f1a1344f0.json`](../../sessions/c0/c0be21b87b8f1a1344f0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部通过。

## 报告

### 修改内容

| 位置 | 改动 |
|------|------|
| `discover_runs` (L152-159) | 加载 `eval_results.json`，提取 `summary.proved_only_mean_isr` |
| `compute_row` (L184) | 返回值增加 `ISR_star` 字段 |
| `mannwhitney_isr_star` (L269-285) | 新增函数：ISR* Mann-Whitney U 检验 |
| `condition_stats` (L370-372) | 增加 ISR* mean/std 计算 |
| `print_per_seed_table` (L414-420) | 表格增加 ISR* 列 |
| `print_condition_stats` (L435-436) | 输出增加 ISR* 行 |
| `print_tests` (L439, L477-482) | 增加第 6 项 ISR* MW 输出 |
| `generate_markdown` (L490, L560-566) | Table A1 增加 ISR* 列 + 第 5 项 ISR* MW |
| `main` (L623, L625, L627) | 调用 `mannwhitney_isr_star` 并传递 |

### ISR* 字段名
`summary.proved_only_mean_isr`

### Per-seed ISR* 值

| Condition | Seed | ISR* |
|-----------|------|------|
| ISR | 47 | 0.5670 |
| ISR | 48 | 0.7462 |
| ISR | 49 | 0.5339 |
| ISR | 50 | 0.7274 |
| ISR | 51 | 0.7134 |
| RANDOM | 47 | 0.0963 |
| RANDOM | 48 | 0.0625 |
| RANDOM | 49 | 0.1143 |

### ISR* 条件统计
- ISR mean: 0.6576 +/- 0.0992
- RANDOM mean: 0.0910 +/- 0.0263

### ISR* Mann-Whitney U 结果
- U = 15.0, p = 0.0179, rank-biserial r = 1.000
- 完全分离（所有 ISR seed 的 ISR* 都高于所有 Random seed）

### 原有功能验证
Fisher (p=0.0179), H7 MW (U=15.0, p=0.0179), Permutation (p=0.7845), BF10 (21.00) 均正常输出，无回归。

---
