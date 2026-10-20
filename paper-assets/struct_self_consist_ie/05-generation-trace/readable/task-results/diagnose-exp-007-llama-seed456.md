# diagnose exp 007 llama seed456

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_exp_007_llama_seed456_20260514T151826_result.json`
- **Structured JSON:** [`e448c167df5d17f130fd.json`](../../sessions/e4/e448c167df5d17f130fd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。

**结论：negative**（实验正常运行完毕，但结果不支持假设）

**关键指标：**

| | NER | RE |
|---|---|---|
| Greedy F1 | 0.6597 | 0.4334 |
| Oracle F1 | 0.7575 | 0.5789 |
| ρ(SJ,F1) | +0.3663 | +0.2870 |
| Structural > Surface | YES (+0.055) | NO (-0.014) |

**失败原因：**
- RE 的 ρ_sj=0.287 未达阈值 0.40
- >30% 样本 F1=0（RE 高达 41.8%），建议 T=0.7 重跑
- NER 子任务结构一致性信号成立，但 RE 子任务不成立，joint 模式判定为 FAIL

**已完成操作：**
- Registry: status=DONE, conclusion=negative, metrics 已记录
- Cron 已清除

---
