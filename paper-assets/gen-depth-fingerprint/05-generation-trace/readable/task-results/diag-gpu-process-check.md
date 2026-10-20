# diag gpu process check

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_gpu-process-check_20260514T205445_result.json`
- **Structured JSON:** [`63850ddc5d1592ca54d5.json`](../../sessions/63/63850ddc5d1592ca54d5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结果

### 汇总表

| GPU | 进程PID | 实验 | 运行时长 | 状态 | 备注 |
|-----|---------|------|----------|------|------|
| 0 | 111538 | plan-002-qwen3-1_7b-s0 | 02:11 | ALIVE | 第1组 Qwen3，348/497 seeds (70%) |
| 0 | 112184 | plan-002-qwen17b-s0 | 01:50 | ALIVE | **第2组 Qwen3，仅 9/498 seeds** |
| 1 | 111651 | plan-002-qwen3-1_7b-s1 | 02:09 | ALIVE | 第1组 Qwen3，333/498 seeds (67%) |
| 1 | 112269 | plan-002-qwen17b-s1 | 01:48 | ALIVE | **第2组 Qwen3，仅 ~12 seeds** |
| 2 | 108247 | plan-002-olmo2-s0 | 45:25 | ALIVE | 正常，1669 lines |
| 3 | 108457 | plan-002-olmo2-s1 | 45:23 | ALIVE | 正常，1564 lines |

### Qwen3 重复提交 — 确认冲突

**两组都活着**，全部 4 个 python 进程均在运行。两组跑完全相同的任务（相同模型、相同数据、相同 shard），共享 GPU 0 和 GPU 1。

- **第1组** (qwen3-1_7b, 04:52:58 提交)：已跑 ~70%，进展正常
- **第2组** (qwen17b, 04:53:19 提交)：仅跑了 ~2%，进展极慢（因与第1组争抢 GPU 显存/算力）

两组各占 ~3968MiB，GPU 0/1 各被占 7950MiB，利用率 86%。输出都写入同一目录 `data/qwen3-1.7b/`，**存在文件写冲突风险**。

### OLMo-2 状态

正常运行，已 45 分钟。数据正在增长（shard0: 1669 lines / 1.9MB, shard1: 1564 lines / 1.7MB）。

### 已生成数据

| 模型 | shard0 lines | shard1 lines | 总行数 | 状态 |
|------|-------------|-------------|--------|------|
| pythia-1b | 2286 | 2269 | 4555 | **已完成** (文件停止于 04:47-04:48) |
| olmo-2-1b | 1669 | 1564 | 3233 | 进行中 |
| qwen3-1.7b | 52 | 41 | 93 | 进行中（两组冲突写入同一文件） |

### 建议操作

第2组 `plan-002-qwen17b-*` 应该被 kill 掉——它是重复提交，进展极慢，且与第1组争抢 GPU 并可能导致输出文件损坏。第1组已完成 70%，让它跑完即可。

---
