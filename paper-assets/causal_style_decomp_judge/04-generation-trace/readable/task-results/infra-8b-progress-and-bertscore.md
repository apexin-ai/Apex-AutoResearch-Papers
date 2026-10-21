# infra 8b progress and bertscore

**The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_8b_progress_and_bertscore_20260520T120645_result.json`
- **Structured JSON:** [`f4f33b3abbbe83e77d46.json`](../../sessions/f4/f4f33b3abbbe83e77d46.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**8B NOT READY — 下载仍在进行中**

| 项目 | 状态 |
|------|------|
| **Qwen3-8B** | 1/5 shards 完成 (model-00005, 1.2G)，4 shards 在 `._____temp/` 中 (2.9G + 2.5G + 3.2G + 2.8G = 11.4G)，总计 ~12.6G。PID 12091 运行中 (2h07m) |
| **Qwen3-32B** | 31G 已下载，PID 12163 运行中 (2h07m) |
| **磁盘** | `/root/autodl-tmp/` 47G/250G used (19%)，空间充足 |
| **BERTScore** | `microsoft/deberta-xlarge-mnli` 后台下载已启动，**PID: 21528** |

ModelScope 下载模式：先写入 `._____temp/`，全部完成后移到正式目录。当前 shards 00001-00004 仍在 temp 中等待校验/移动，进程仍活跃。

---
