# ssh migrate 5090b data

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_migrate_5090b_data_20260521T101948_result.json`
- **Structured JSON:** [`5116f5800ae53a993b02.json`](../../sessions/51/5116f5800ae53a993b02.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

5090 上没有 SSH config，且无法解析 `autodl-5090-b` 主机名。

**问题**：`autodl-5090-b` 不在 MCP 可用服务器列表中，从 5090 也无法 SSH 连接到它。可能原因：
- AutoDL 实例重启后端口/地址变了
- 该实例未配置在当前环境的 `resources.yaml` 中

**需要你提供**：
1. 5090-b 的实际 SSH 连接信息（IP + 端口），或
2. 将 5090-b 添加到 `resources.yaml` 后重试

如果 5090-b 是 AutoDL 实例，请去控制台查看当前的 SSH 地址和端口。

---
