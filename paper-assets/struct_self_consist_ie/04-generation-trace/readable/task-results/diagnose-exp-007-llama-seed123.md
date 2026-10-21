# diagnose exp 007 llama seed123

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_exp_007_llama_seed123_20260514T151905_result.json`
- **Structured JSON:** [`1a7b7eb6baa98c8c66a1.json`](../../sessions/1a/1a7b7eb6baa98c8c66a1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。

**结论：negative（FAIL）** — 进程正常完成，无报错，但科学指标未达标。

关键结果：

| 指标 | NER | RE |
|------|-----|-----|
| Greedy F1 | 0.6605 | 0.4330 |
| Oracle F1 | 0.7703 | 0.5719 |
| ρ(SJ,F1) | +0.3371 | +0.2680 |
| Structural > Surface | YES (+0.1228) | NO (-0.0165) |

失败原因：
- RE ρ_sj=0.268 远低于 ≥0.40 阈值
- RE 41% samples F1=0（>30% 上限）
- RE 子任务结构一致性未优于表面一致性

NER 子任务表现尚可（structural > surface 成立），但 joint mode 要求 RE 也达标。报告建议降温到 T=0.7 重试。

已完成：registry → DONE/negative + metrics 已写入，cron 已清除。

---
