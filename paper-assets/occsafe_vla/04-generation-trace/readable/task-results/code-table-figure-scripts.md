# code table figure scripts

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_table-figure-scripts_20260526T200543_result.json`
- **Structured JSON:** [`6cabba0c9aaa3e58db72.json`](../../sessions/6c/6cabba0c9aaa3e58db72.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个脚本均已验证通过：

**`generate_table1.py`** — LaTeX 和 Markdown 格式均正常，空 cell 显示 "—"，best 值加粗，Δ 计算正确。

**`generate_factorial_figures.py`** — 两张图均已生成：
- **Bar Chart**: 暖/冷色系区分 gradient_flow ON/OFF，Vanilla 虚线参考线，error bar 正常
- **Interaction Plot**: 只有 BN 列有数据点（LN 尚无数据），等 v2 LN 数据就绪后会自动补全两条线

v2 数据齐全后，更新 JSON 文件用 `--data-json` 即可一键重新生成 Table 1 和 Figure。

---
