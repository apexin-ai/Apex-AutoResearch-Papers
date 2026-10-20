# maintenance fix milestone checker

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_maintenance_fix-milestone-checker_20260520T100349_result.json`
- **Structured JSON:** [`5f536300bf2ac32d97df.json`](../../sessions/5f/5f536300bf2ac32d97df.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇总：

| 项目 | 结果 |
|------|------|
| 旧 milestone_checker | 已不存在（无需杀） |
| 新等待脚本 PID | **11648**，运行中 |
| 正确模型路径 | `/root/autodl-tmp/models/meta-llama/Meta-Llama-3.1-8B/` (PATH_A ✓, Instruct 不存在) |
| 当前 shard3 大小 | **989 MB**（~1.04GB / 需 >4GB 触发 Milestone A） |

脚本每 2 分钟检查一次 shard3，达到 4GB+ 后写 `/tmp/milestone_a.flag`，然后转入 Milestone B 检测（14B adapter + generations + Qwen3 shards）。

---
