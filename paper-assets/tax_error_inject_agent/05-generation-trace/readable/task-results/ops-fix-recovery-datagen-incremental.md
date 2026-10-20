# ops fix recovery datagen incremental

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_fix-recovery-datagen-incremental_20260515T184129_result.json`
- **Structured JSON:** [`ab8025ec92ec2dafdfd1.json`](../../sessions/ab/ab8025ec92ec2dafdfd1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇报

### 当前脚本输出机制

**一次性写入，无任何安全网。** `results = []` 在内存中累积所有结果，仅在 760 条全部处理完后写入 `data/recovery_paired/recovery_paired.jsonl`。无 signal handler、无 atexit、无 checkpoint。crash = 丢失全部已处理数据。

### 安全 checkpoint 方案

当前进程 **无法安全地从外部 dump 内存数据**。没有 signal handler 可以触发，通过 `/proc/PID/fd` 也读不到内存中的 list。唯一安全的做法是让当前进程跑完（预计还需 ~3-4h），然后用 v2 替换。

### v2 patch 改动摘要

已保存到 `artifacts/gen_recovery_paired_v2.py`，核心改动：

| 改动 | 说明 |
|------|------|
| **增量写入** | 每处理完 1 条立即 append 到 jsonl + `fsync`，不再攒到最后 |
| **断点续传** | 启动时读取已有输出文件，提取已完成的 `inject_id` 集合，跳过已处理条目 |
| **SIGUSR1 handler** | `kill -USR1 &lt;PID>` 打印进度快照（processed/total/rate/ETA），不中断进程 |
| **`--flush-every N`** | 控制 fsync 频率，默认 1（每条都刷），可调大减少 IO |
| **try/finally** | 即使异常退出也保证 flush + close |

所有业务逻辑（prompt 构建、API 调用、parse_response）保持不变，仅改了 main() 的 IO 流程。

### 建议

当前进程让它跑完。跑完后用 v2 替换，后续重跑如果中断可自动续传。

---
