# ops disk check

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_disk-check_20260515T005122_result.json`
- **Structured JSON:** [`20cc04d0cce99aea26dc.json`](../../sessions/20/20cc04d0cce99aea26dc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 磁盘使用报告

### 分区概况

| 分区 | 总容量 | 已用 | 可用 | 使用率 |
|------|--------|------|------|--------|
| `/root/autodl-tmp/` (数据盘) | 250G | 82G | 169G | **33%** |
| `/` (根分区) | 30G | 9.1G | 21G | 31% |

### outputs 目录明细 (总计 ~61G)

| 目录 | 大小 | 状态 | 可删? |
|------|------|------|-------|
| `exp1_isr_b03_s44_r2/` | **31G** | 训练完成，已有 eval 结果 | **可删** |
| `exp1_random_b03_s44/` | **15G** | 训练完成，有 checkpoint-100 (15G) | **可删** |
| `exp1_random_b03_s44_r2/` | **15G** | **正在运行 (PID 51297)** | **不碰** |
| `exp1_isr_b03_s43_eval/` | 228K | eval 结果 | 保留 |
| `exp1_isr_b03_s44_r2_eval/` | 168K | eval 结果 | 保留 |
| `exp1_random_b03_s43_eval/` | 0 | 空目录 | 无所谓 |

### 可释放空间

- `exp1_isr_b03_s44_r2/` — 31G — 训练完成且 eval 已出结果，模型权重可删
- `exp1_random_b03_s44/` — 15G — 训练完成，checkpoint 可删

**共可释放约 46G**，释放后数据盘使用率从 33% 降至约 14%。

当前磁盘压力不大，但如果后续还要跑多个实验，建议清理这两个目录。需要我执行删除吗？

---
