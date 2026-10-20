# code fix h6 phantom number

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fix_h6_phantom_number_20260525T203733_result.json`
- **Structured JSON:** [`014b4c7a782034e5c287.json`](../../sessions/01/014b4c7a782034e5c287.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。修改了两个文件：

1. **`docs/paper/method.tex`** — 删除了 "OBD achieves lower MAE than multiclass LightGBM (0.984 vs 1.016)" 比较句，改为直接陈述 OBD 相对 ordinal logistic regression 的 AUC 优势
2. **`artifacts/_project/paper/method.tex`** — 删除了整段 "multiclass LightGBM" 对比（含所有幻影 MAE 数字），保留 ordinal logistic regression 的有效比较

其他位置的 0.984 均为 AUC 置信区间值，与此幻影 MAE 无关。报告已写入 `artifacts/h6_fix_phantom_number.md`。

---
