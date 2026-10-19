# ssh m1 reextract launch

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_m1_reextract_launch_20260513T193609_result.json`
- **Structured JSON:** [`3091d9a8b66e1e04795e.json`](../../sessions/30/3091d9a8b66e1e04795e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

启动成功，4 个 worker 已在并行处理。汇总：

| 项目 | 结果 |
|------|------|
| prepare_m1_rerun.py | 删除 28,276 个 error JSON，生成 metadata |
| tmux session | `m1_reextract` |
| 主进程 PID | 97358 (`batch_extract.py`) |
| 日志路径 | `/root/runs/structfuse-context/m1_rerun.log` |
| 状态 | 运行中，4 workers，82 个 repo 组，已开始创建 CodeQL DB 并提取 |

注意：有一条 CodeQL query warning（`call_graph.ql` 对 feedparser 返回 non-zero），这是个别 repo 的查询失败，脚本会继续处理其他实例。

额外操作：因服务器上缺少 codeql，安装了 CodeQL CLI 2.25.4 到 `/opt/codeql`（脚本已有对应 PATH 设置）。预估 4 workers 约 60h 完成全部 28,276 个实例。

---
