# code 14b table and figure scripts

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_14b-table-and-figure-scripts_20260523T052047_result.json`
- **Structured JSON:** [`029155f72c568805f153.json`](../../sessions/02/029155f72c568805f153.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个脚本都通过验证，`CONFIRMED_14B` 的 `True`/`False` 两条路径均正常。

产出：
- **`artifacts/update_14b_table.py`** — 顶部填入 s123/s456 accuracy 后运行，输出 mean±std、TOST p-value、LaTeX 行。当前仅有 s42 数据时自动跳过 TOST。3-seed 完整时会提示需新增 s456 列。
- **`artifacts/plot_figure2_v3.py`** — 顶部修改 `cls_acc_14b`/`cwm_acc_14b` 和 `CONFIRMED_14B`。确认后自动切换为实线+实心 marker，移除 exploratory 标注，gap 使用实际数值。

---
