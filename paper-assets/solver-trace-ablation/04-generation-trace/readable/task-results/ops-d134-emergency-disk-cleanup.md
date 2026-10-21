# ops d134 emergency disk cleanup

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_d134-emergency-disk-cleanup_20260518T180001_result.json`
- **Structured JSON:** [`374ae96efff3580dd60c.json`](../../sessions/37/374ae96efff3580dd60c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

清理完成。结果汇总：

| 指标 | 清理前 | 清理后 |
|------|--------|--------|
| 已用 | 250G (100%) | 193G (77%) |
| 可用 | 800K | **58G** |

**释放空间：~57G**

- s48 checkpoint-50 (15G) + checkpoint-100 (13G) = 28G 已删
- s47 Random 模型权重 (~13G) 已删
- s47 ISR 模型权重 (~16G) 已删

**s49 状态**：PID 124789 存活，运行正常（已运行 229 秒）。

**剩余空间充足**：58G 可用，s49-s51 每个 seed 峰值 ~15G（save_total_limit=1 只保留最新 checkpoint），足够跑完剩余 3 个 seed。

---
