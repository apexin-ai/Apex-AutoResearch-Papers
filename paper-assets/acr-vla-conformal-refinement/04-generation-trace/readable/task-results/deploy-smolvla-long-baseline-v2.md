# deploy smolvla long baseline v2

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_smolvla-long-baseline-v2_20260522T182731_result.json`
- **Structured JSON:** [`18716c5ed988b285dd4e.json`](../../sessions/18/18716c5ed988b285dd4e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**这3个eval已经全部跑完了，不是幽灵条目。** Registry 和服务器 log 都确认了结果：

| Seed | pc_success | n_episodes | eval_time |
|------|-----------|------------|-----------|
| 42 | 49.5% | 200 | ~1226s |
| 43 | 53.5% | 200 | ~1269s |
| 44 | 49.5% | 200 | ~1194s |

**Mean ± Std = 50.83 ± 1.89%**

Registry 中 conclusion 标记为 `failed`，可能是因为 baseline 表现不佳的语义标注（非运行失败）。输出目录在 `/root/outputs/eval/smolvla_long_seed{42,43,44}/`，含完整 video。

不需要重新部署。是否需要将 registry 条目的 conclusion 改为 `success`（eval 本身成功完成），或者有其他需要处理的？

---
