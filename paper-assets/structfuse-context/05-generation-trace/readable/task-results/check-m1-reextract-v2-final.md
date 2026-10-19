# check m1 reextract v2 final

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_m1-reextract-v2-final_20260515T015229_result.json`
- **Structured JSON:** [`19ce839db97548fddd2a.json`](../../sessions/19/19ce839db97548fddd2a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## M1 reextract v2 状态 (09:53 CST)

**进程：存活** — 4 个 worker 仍在运行（codeql 进程活跃）

**总进度：24,624 / 28,276 = 87.1%**（上次 09:10 为 86.0%，43 分钟处理了 303 个）

**活跃 repo 进度：**

| Repo | 总量 | 约已完成 | 状态 |
|------|------|---------|------|
| sqlfluff | 1,272 | ~1,270 | 基本完成 |
| conan | 972 | ~770 | 处理 PR 尾部（pr_15829） |
| pydicom | 1,315 | ~640 | 进行中 |
| MONAI | 524 | ~225 | 进行中 |
| getmoto/moto | 536 | 刚开始 | 09:47 刚启动，CodeQL query failed 1 次 |

**错误：** 19 个 WARNING（含 getmoto 的 CodeQL query 失败），0 个 ERROR

**all.jsonl：** 44,173 行（含历史数据，大于 instance 总数属正常——每个 instance 可能产生多行）

**速率：** ~7 instances/min

**剩余：** ~3,652 instances → **预计完成时间 17:00-19:00 CST**，比之前 ETA 推迟约 2 小时（getmoto 是新增大 repo，且 pydicom/MONAI 还有较多剩余）。

---
