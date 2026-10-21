# diagnose cwm rank32 ablation v2

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_cwm-rank32-ablation-v2_20260515T135518_result.json`
- **Structured JSON:** [`49cf031597e5d877bff9.json`](../../sessions/49/49cf031597e5d877bff9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。诊断总结：

| 项目 | 结果 |
|------|------|
| 结论 | **成功完成** (EXIT_CODE=0) |
| 最后 step | 1434/1434 (100%) |
| 训练时间 | ~83 min |
| Checkpoints | `best/`, `checkpoint-1434/`, `checkpoint-478/` |
| Accuracy | 87.0% (+35.2pp vs baseline) |
| MVP-B | **PASS** |
| cuda:0 | 空闲 (0MiB, 0% util) |
| Registry | status=ANALYZING, conclusion=success |

训练脚本内置了评估流程，已自动跑完测试集评估，结果保存在 `eval_cwm_rank32_results.json`。

---
