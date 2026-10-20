# fix cuda3 duplicate eval

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_cuda3_duplicate_eval_20260520T214229_result.json`
- **Structured JSON:** [`9a7d019c92533297ae08.json`](../../sessions/9a/9a7d019c92533297ae08.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

当前状态汇总：

## 清理完成

| 操作 | 状态 |
|------|------|
| Kill 重复进程 531852 → 537137 | ✅ 已终止 |
| 保留进程 530955 → 535166 | ✅ 运行中（Wiki eval） |
| cuda:0/1/2 | ✅ 未触碰 |

## adaptive_1_7b_seed456 Eval 结果

| 指标 | 值 | 状态 |
|------|------|------|
| Holdout PPL | **13.267** | ✅ 完成 |
| OWT PPL | **13.292** | ✅ 完成 |
| Wikipedia PPL | — | ⏳ 进行中（PID 535166，已跑 ~16 min） |
| Downstream 5-task | — | ⏳ 待 Wiki 完成后由 530955 脚本继续执行 |

Wiki eval 和 downstream 任务由保留的 `/tmp/run_eval_seed456.sh`（530955）自动串行执行，无需手动干预。需要我轮询等结果出来吗？

---
