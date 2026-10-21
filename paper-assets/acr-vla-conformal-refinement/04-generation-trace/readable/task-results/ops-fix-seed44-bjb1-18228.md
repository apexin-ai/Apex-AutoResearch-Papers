# ops fix seed44 bjb1 18228

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_fix-seed44-bjb1-18228_20260516T045605_result.json`
- **Structured JSON:** [`ab6d4a0e35c7a3dc2276.json`](../../sessions/ab/ab6d4a0e35c7a3dc2276.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

r3 条目已清理为 DONE/killed。汇总如下：

## bjb1-18228 GPU 状态

| GPU | Python PID | 实验 | 进度 | 状态 |
|-----|-----------|------|------|------|
| cuda:0 | 390936 | crm_perdof seed**42** (eval_object_perdof_default_norm_r2) | 运行中 | 非 seed44 相关 |
| cuda:1 | 452987 | **eval-perdof-object-seed44** | 刚启动，模型/环境已加载，0/10 tasks | 正常 |
| cuda:2 | 428411 | **eval-obs-only-object-norm02-seed44-r2** | 2/10 tasks 完成，第3个进行中 | 正常 |
| cuda:3 | 428122 | **eval-argmin-object-seed44-r2** | 2/10 tasks 完成 | 正常 |

## seed=44 实验结论

**没有 GPU 冲突。** r3 的两个进程（PID 430985/431189）已经死了，无 /proc，无 exit file。实际占用 GPU 的都是 r2 进程，且都在正常推进。

**有效实验对应关系：**
- `eval-argmin-object-seed44-r2` → 包装 PID=428117, Python PID=428122, cuda:3（Cron 追踪正确）
- `eval-obs-only-object-norm02-seed44-r2` → 包装 PID=428406, Python PID=428411, cuda:2（Cron 追踪正确）
- `eval-perdof-object-seed44` → 包装 PID=452982, Python PID=452987, cuda:1（新提交，刚开始跑）

**已清理：** r3 的两个 registry 条目已从 PREPARING 转为 DONE/killed，不会再干扰。

**cuda:1 并非空闲** — eval-perdof-object-seed44 刚被提交上去，正在跑（不是你提到的 seed43 已完成的那个）。

---
