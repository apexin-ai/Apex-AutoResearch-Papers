# status check all running

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_status_check-all-running_20260515T033550_result.json`
- **Structured JSON:** [`c6750913fb5626151e50.json`](../../sessions/c6/c6750913fb5626151e50.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 实验状态汇总

### Plan-014 (Qwen3-8B, cuda:0)

| 指标 | 值 |
|------|-----|
| PID 134817 | **存活**，已运行 3h17m |
| 进度 | **802/996 seeds (80.5%)** |
| 速度 | ~15s/seed |
| 剩余 | ~194 seeds → **预计 ~48 min 完成** |
| 输出文件 | `generations_shard0.jsonl` — 416 行, 475KB（缓冲写入，未全部 flush） |
| .recovered 文件 | **不存在**，只有 `.bak_416` 备份 |
| GPU 0 | 79% 利用率, 16.5/32.6 GB VRAM |

注意：日志中大量 "Skipping seed X at depth Y: empty output" 警告，很多 seed 在某些 depth 产出为空被跳过。

---

### Plan-005 子实验 (Pythia-2.8B, cuda:1/2/3)

三个进程都刚启动约 **7.5 分钟**（不是 2 小时前），均存活：

| 实验 | PID | 进度 | 速度 | 输出行数 | 预计完成 |
|------|-----|------|------|---------|---------|
| cont (continuation) | 164658 | ~55/995 (5.5%) | ~9s/seed | 289 行 | **~2h20m** |
| elab (elaboration) | 164737 | ~50/995 (5%) | ~9.5s/seed | 275 行 | **~2h30m** |
| rewrite (inspired_rewriting) | 164881 | ~51/995 (5.1%) | ~9.3s/seed | 275 行 | **~2h25m** |

GPU 利用率：GPU 1/2/3 均 ~66-67%, 各占 6.2/32.6 GB VRAM。

---

### GPU 总览

| GPU | 利用率 | 显存 | 任务 |
|-----|--------|------|------|
| 0 | 79% | 16.5/32.6 GB | plan-014 (Qwen3-8B) |
| 1 | 66% | 6.2/32.6 GB | plan-005-cont |
| 2 | 66% | 6.2/32.6 GB | plan-005-elab |
| 3 | 67% | 6.2/32.6 GB | plan-005-rewrite |

4 块 GPU 全部在用。Plan-014 约 48 分钟后完成，plan-005 三组约 2.5 小时后完成。

---
