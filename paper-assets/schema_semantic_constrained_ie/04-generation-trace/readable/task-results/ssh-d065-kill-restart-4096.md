# ssh d065 kill restart 4096

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_d065_kill_restart_4096_20260520T013419_result.json`
- **Structured JSON:** [`17cacfa018c904e4aa09.json`](../../sessions/17/17cacfa018c904e4aa09.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部就绪。汇报：

### 执行结果

**1. Kill 确认** — 2048 进程 676441、682762、676436 已终止，无残留

**2. 文件清理** — 所有 d064 greedy 文件已删除（含 Llama w5 和 Qwen 输出+日志）

**3. 新进程 PID**
| 任务 | PID | GPU |
|------|-----|-----|
| Llama greedy UNC 4096 | 697390 | GPU0 |
| Llama greedy CON 4096 | 698081 | GPU1 |
| Cascade (等 Llama 完后启 Qwen) | 698469 | — |

**4. GPU 利用率**
- GPU0: 90%, 18275 MiB
- GPU1: 86%, 18275 MiB

**5. 输出文件**
- `d065_llama_docred_greedy_unc_4096.jsonl` (114KB, 正在写入)
- `d065_llama_docred_greedy_con_4096.jsonl` (31KB, 正在写入)
- Qwen 两个文件将由 cascade 自动启动后生成：
  - `d065_qwen_docred_greedy_unc_4096.jsonl`
  - `d065_qwen_docred_greedy_con_4096.jsonl`

**注意**：首次启动 CON 时 `nohup python` 找不到命令，已改用 `/root/miniconda3/bin/python` 完整路径重启成功。Cascade 脚本也已更新为完整路径。

---
