# code fix t1t5 scripts

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fix_t1t5_scripts_20260515T121718_result.json`
- **Structured JSON:** [`82bc17d5febf89623fa3.json`](../../sessions/82/82bc17d5febf89623fa3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

3 files fixed. Summary:

### 修改的文件

| 文件 | 行号 |
|------|------|
| `run_qwen14b_hires_profiling.py` | L156-158 |
| `run_pythia14b_hires_profiling.py` | L238-240 |
| `run_opt67b_hires_profiling.py` | L238-240 |

### 修改前后

**修改前**（错误 — 第1名 raw delta / 第5名 raw delta）：
```python
top1_d = sorted_by_d2[0][2]
top5_d = sorted_by_d2[4][2] if len(sorted_by_d2) > 4 else sorted_by_d2[-1][2]
t1_t5 = top1_d / top5_d if top5_d > 0 else float("inf")
```

**修改后**（正确 — canonical concentration ratio，与 `compute_shape_metrics.py` L43 一致）：
```python
top1_conc = sorted_by_d2[0][2] / total_sum if total_sum > 0 else 0
top5_conc = top5_sum / total_sum if total_sum > 0 else 0
t1_t5 = top1_conc / top5_conc if top5_conc > 0 else float("inf")
```

`top5_conc` 使用已有变量 `top5_sum`（top 5% heads 的 delta 总和），与 canonical 定义 `s[0] / top5_sum` 数学等价。

### 其他脚本
- `run_yi15_hires_profiling.py` — 不计算 t1_t5，无需修复。

---
