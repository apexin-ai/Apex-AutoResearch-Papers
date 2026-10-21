# fix qwen shard3 restart

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_qwen_shard3_restart_20260521T061206_result.json`
- **Structured JSON:** [`02efb24a39036936bf2b.json`](../../sessions/02/02efb24a39036936bf2b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

恢复成功。汇报：

### 恢复状态

| 项目 | 状态 |
|------|------|
| **GPU 3 恢复前** | 0% util, 0 MiB — 确认空闲 |
| **shard_3 已完成** | 26000 行 → **offset = 130** conditions（共 324 conditions） |
| **恢复 PID** | **101900**（实际 python 进程） |
| **GPU 3 恢复后** | **56% util, 87955 MiB** — 模型已加载，正在推理 |

### GPU 0-2 进度

| Shard | 行数 | 已完成 conditions | 总 conditions |
|-------|------|-------------------|---------------|
| shard_0 (GPU 0) | 46200 | 231 | — |
| shard_1 (GPU 1) | 45000 | 225 | — |
| shard_2 (GPU 2) | 45400 | 227 | — |

日志显示 shard_3 恢复后已开始处理（Condition 551, 489 等），推理速度 ~19K toks/s input, ~618 toks/s output，运行正常。

完成后需要将 `shard_3.jsonl`（26000 行）和 `shard_3_resume.jsonl` 合并为完整结果。

---
