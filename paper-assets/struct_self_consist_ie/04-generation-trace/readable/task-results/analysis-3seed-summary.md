# analysis 3seed summary

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_3seed_summary_20260514T185130_result.json`
- **Structured JSON:** [`526452073427cf38483a.json`](../../sessions/52/526452073427cf38483a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。汇总报告已写入 `artifacts/3seed_ner_summary.md` 并注册，registry 已更新。

核心结论：

| 指标 | 最强信号 | 最 seed-robust |
|------|---------|---------------|
| Full ρ | voting_conf (0.422) | EM (CV=3.5%) |
| Conditional ρ | EM (0.408) | EM (CV=1.5%) |
| Full AUROC | EM (0.780) | logprob (SD=0.010) |

- **Structural > Surface 3/3 seeds 全部成立**，SJ−FK Δ≈0.15 稳定
- **SJ ρ 变异系数 6.0%**（Mean=0.412±0.025）——ROADMAP 基于 2-seed 报的 "Δ<0.004" 偏乐观，seed456 降至 0.384 拉大了方差
- **FK 最不稳定**（CV=12.2%），**EM 最稳定**（CV=3.5% full / 1.5% conditional）

---
