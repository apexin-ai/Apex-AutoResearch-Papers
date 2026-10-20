# ssh check traj collect final

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_check-traj-collect-final_20260514T121957_result.json`
- **Structured JSON:** [`e0b5d3e9fbc97cb91b38.json`](../../sessions/e0/e0b5d3e9fbc97cb91b38.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果汇总

| 项目 | 值 |
|------|-----|
| **最终成功轨迹** | 400 / 500（未达目标） |
| **退出原因** | `/tmp` 磁盘满（`No space left on device`） |
| **成功率** | 69.6%（575 次尝试中 400 成功） |
| **运行时间** | 5.51 小时 |
| **API 费用** | $34.72 |
| **Registry** | → DONE, conclusion=negative |
| **Cron** | ✓ 已删除 |

磁盘满从 traj_0534 左右开始，之后约 40 次尝试全部因无法复制 `libdownward.so` 到 `/tmp` 而失败。要补齐剩余 100 条轨迹，需先清理 `/tmp` 或将临时文件重定向到数据盘。

---
