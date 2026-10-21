# check gradient plot script

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_gradient-plot-script_20260527T034215_result.json`
- **Structured JSON:** [`c62b4a4ab25cfde49252.json`](../../sessions/c6/c62b4a4ab25cfde49252.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结论

**`plot_gradient_analysis_v2.py` 已就绪，无需修改。**

关键确认：
- 脚本自动 glob `*_gradient_stats.json`，不限条件数量，5 条件直接支持
- `CONDITION_STYLES` 已预定义全部 5 个 v2 条件的颜色/标记/线型
- 与 `run_gradient_analysis_v2.py` 的输出格式（`{condition_name}_gradient_stats.json` + JSON 内 `"condition"` 字段）完全匹配
- 4-panel 布局自动处理 Vanilla/Detach 无 OCC 梯度的情况

唯一注意：运行 `run_gradient_analysis_v2.py` 时 `--condition_name` 必须用**空格**（如 `"Vanilla v2"`），不能用下划线，否则出图样式会退化为灰色默认。

报告已写入 `artifacts/_project/intermediate/gradient_plot_readiness.md`。

---
