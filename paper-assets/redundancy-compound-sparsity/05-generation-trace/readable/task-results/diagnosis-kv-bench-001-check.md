# diagnosis kv bench 001 check

**When Does KV Redundancy Predict MLP Sparsity? Architecture Dependence of Cross-Axis Signals in Reasoning Inference** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnosis_kv-bench-001-check_20260512T022421_result.json`
- **Structured JSON:** [`b547cfc78910232ad260.json`](../../sessions/b5/b547cfc78910232ad260.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## kv-bench-001 实验结果：**失败**

**现象**：
- 进程静默退出，tmux session 已消失，无残留进程
- 日志仅4行，无 error/traceback，无完成标记
- 结果 JSON 未生成

**日志内容**（完整）：
| # | tokens | PPL | evictions |
|---|--------|-----|-----------|
| 1 | 99 | 3.06 | 0 (baseline) |
| 2 | 99 | 3.17 | 49 |
| 3 | 99 | 3.12 | 49 |
| 4 | 99 | 3.14 | 49 |

只跑了4条记录就停了，远未覆盖全部 policy × budget 组合。

**已完成**：
- Registry 更新：conclusion=failed, status=DONE, notes 记录失败原因
- Cron `kv-bench-001` 已删除

需要排查 `run_kv_benchmark.py` 的静默退出原因后重跑。

---
