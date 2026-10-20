# ssh token length check

**prov grounded uie** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_token-length-check_20260512T133159_result.json`
- **Structured JSON:** [`7ea40511cdd4e23362cd.json`](../../sessions/7e/7ea40511cdd4e23362cd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果：

1. **tmux**: 已安装，版本 **3.2a**，路径 `/usr/bin/tmux`
2. **DocRED token 长度分布**:

| 统计量 | 值 |
|--------|------|
| mean | 1648 |
| p50 | 1443 |
| p90 | 2725 |
| p95 | 3299 |
| p99 | 4909 |
| max | 10140 |

p95 在 3299，p99 到 4909，max 达到 10140。训练时 `max_seq_length` 设 4096 可覆盖 ~97% 样本，设 8192 则几乎全覆盖（仅极少数超长样本被截断）。

---
