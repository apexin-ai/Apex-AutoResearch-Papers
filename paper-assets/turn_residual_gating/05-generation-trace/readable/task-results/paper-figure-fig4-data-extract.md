# paper figure fig4 data extract

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_figure_fig4_data_extract_20260519T213806_result.json`
- **Structured JSON:** [`c51bd6e4cebbb4d02adf.json`](../../sessions/c5/c51bd6e4cebbb4d02adf.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

SSH 不可用（本地无对应密钥，MCP SSH 工具也不在可用列表中），无法从服务器提取 per-turn 原始数据。

本地能获取的信息仅有 4 模型的 summary metrics（mean, T1, T10, decay），per-turn 10 值数组只存在于服务器 `/root/turn_residual_gating/runs/analysis/attention_heatmap/heatmap_*.json` 中。

两个选择：
1. **你手动提供 SSH 密钥或 per-turn 数据** — 我来完成脚本修改
2. **我先用 summary metrics 做能做的改动**（改标题 "identical" → "near-identical"，替换 base_data 为 attention heatmap Base 的 T1/T10，但 TG/UG/LoRA 仍保留指数拟合，因为无法获取真实中间点）

你倾向哪个？

---
