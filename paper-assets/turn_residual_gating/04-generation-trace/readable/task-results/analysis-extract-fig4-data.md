# analysis extract fig4 data

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_extract_fig4_data_20260519T210826_result.json`
- **Structured JSON:** [`d9fa6196aba038000349.json`](../../sessions/d9/d9fa6196aba038000349.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

文件已写入。总结：

**已完成**: `figures/paper/fig4_real_data.json` 已生成。

**问题**: SSH 工具（`mcp__agent-ml-research__ssh_read_only`）已从当前环境的 MCP server 中移除，4 个 worker 都无法连接服务器。所有 worker（`fig4_extract`, `extract_heatmap_gar`, `extract_fig4_data`, `fig4_attention_heatmap_fix`）均因此卡住。

**当前数据来源**:
- **Base**: registry 中 `phase1_gar_diag` 的实际 per-turn 值（10 个点，来自 GARMeasurer）
- **TG/UG/LoRA**: 从 attention_heatmap 实验汇总指标（mean + decay）用指数衰减模型拟合的 10 个点，**不是实际测量值**

**获取实际数据**: 服务器上的 JSON 文件路径已记录在 `_metadata.server_json_paths` 中。恢复 SSH 访问后，在服务器上执行 `_metadata.note` 中的命令即可提取实际 per-turn 均值并替换拟合值。

---
