# code update analysis two layer

**trace distill repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_update_analysis_two_layer_20260515T145906_result.json`
- **Structured JSON:** [`4df801eec758cc7a3118.json`](../../sessions/4d/4df801eec758cc7a3118.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部验证通过。总结：

**已完成：**
- `analyze_phase3_v2.py` 更新至 812 行，新增 `--two-layer`、`--retest-csv-path`、`--output-two-layer-json` 三个参数
- **Layer 1**：显示 diff_apply 成功率（原始 14/32 = 44%），无 retest 数据时自动降级为仅展示原始数据 + 逐实例状态表
- **Layer 2**：oracle-clean + diff_apply=True 筛选后，仅 httpie_2 的 line_filtered 有 1 条有效记录；其他条件因该实例 diff_apply=False 被过滤掉，head-to-head 和统计检验均为空（符合预期——数据量不足）
- JSON 已输出到 `pipeline_output/phase3_v2_two_layer_analysis.json`
- PID 131777 未受影响

---
