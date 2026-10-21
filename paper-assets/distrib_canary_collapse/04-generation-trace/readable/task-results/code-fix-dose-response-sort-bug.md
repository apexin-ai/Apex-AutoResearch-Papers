# code fix dose response sort bug

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fix-dose-response-sort-bug_20260515T045013_result.json`
- **Structured JSON:** [`34a4031d59fcc025302c.json`](../../sessions/34/34a4031d59fcc025302c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

验证通过。现在输出对比表。

**gen_last_idx 修复确认：**

| α | 旧 gen_last_idx | 新 gen_last_idx | 旧 n_gens | 新 n_gens |
|---|---|---|---|---|
| 0.00 | 9 | **10** | 11 | 11 |
| 0.25 | 9 | **10** | 11 | 11 |
| 0.50 | 7 | **8** | 8 | **9** |
| 1.00 | 9 | **10** | 11 | 11 |

**distinct_1 drift 对比（旧 vs 新）：**

| α | 旧 drift | 新 drift | 差异 |
|---|---|---|---|
| 0.00 | -13.81% | **-13.78%** | +0.03pp |
| 0.25 | -39.90% | **-40.34%** | -0.44pp |
| 0.50 | -34.90% | **-36.16%** | -1.26pp |
| 1.00 | -28.14% | **-28.34%** | -0.20pp |

**总结：**
1. **根因**：`extract_drift.py` 硬编码了 `gen_last` 值，不是排序 bug。gen_10 的数据完全被忽略。
2. **新脚本** `gen_dose_response.py` 动态发现所有 gen 目录，用数值排序，已覆盖旧 CSV。
3. **`analyze_alpha_sweep.py`、`analyze_extended.py`、`pooled_panel_analysis.py`** 排查完毕，排序逻辑均正确（用整数排序），无需修复。
4. α=0.50 多了 gen_8（旧脚本写死 gen_last=7），drift 幅度系统性增大，符合预期——真正的末代比上一代退化更严重。

---
