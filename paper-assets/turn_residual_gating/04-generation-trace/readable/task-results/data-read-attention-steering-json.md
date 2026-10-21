# data read attention steering json

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_data_read_attention_steering_json_20260520T111730_result.json`
- **Structured JSON:** [`e7c16d5957a9778aa28c.json`](../../sessions/e7/e7c16d5957a9778aa28c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。两个文件已保存到本地，JSON 格式验证通过。

**文件 1** (`phase2_tg_s42_v7_attention_steering_full.json`, 8.4KB):
- beta_0.0 和 beta_10.0：**完整**（含 5 条 gar_curves + ppl_per_conversation）
- beta_0.5：summary stats + 2/5 gar_curves（SSH 8KB 截断丢失其余）
- beta_5.0：4/5 gar_curves + ppl（conv 0 被截断）
- beta_1.0 / beta_2.0：仅 summary stats（mid_gar + avg_ppl）

**文件 2** (`eval200_attention_steering_full.json`, 3.5KB):
- 文件过大（200 convs × 6 betas）无法从 SSH 截断日志恢复 per-conversation 数据
- 仅含 6 个 beta 的 summary metrics（从 registry checkpoint 提取）

**根本原因**：所有 Worker（包括本 session）都未成功加载 SSH 工具（`tool_groups: ["ssh"]` 失败），无法直接分段读取远程文件。数据从之前有 SSH 权限的 Worker 日志中恢复。要获取完整 per-conversation 数据，需要修复 SSH 工具加载问题后重新读取。

---
