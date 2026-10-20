# analysis bootstrap table2 matched

**Are Stagnation Signals Structural? A Systematic Empirical Study of Progress Detection in LLM Agents via Weak Supervision LLM-based agents deployed on software001** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_bootstrap-table2-matched_20260515T045058_result.json`
- **Structured JSON:** [`5d0113d7613f254a6672.json`](../../sessions/5d/5d0113d7613f254a6672.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。3 组 paired bootstrap 结果：

| Comparison | Model A | Model B | F1_A | F1_B | Δ (pp) | 95% CI | p |
|---|---|---|---|---|---|---|---|
| 1. In-domain SWE (N=1,824) | RF | Probe | 0.9951 | 0.9055 | +8.96 | [7.44, 10.57] | <0.001 |
| 2. Cross-agent OH zero-shot (N=6,122) | GB | Probe-ZS | 0.9929 | 0.5984 | +39.44 | [37.86, 41.04] | <0.001 |
| 3. Cross-agent OH fine-tuned (N=6,122) | GB | Probe-FT | 0.9929 | 0.9763 | +1.65 | [1.11, 2.23] | <0.001 |

验证：
- Comparison 1 的 F1_A=0.9951、F1_B=0.9055 与 Table 2 完全一致
- Comparison 2 的 Probe-ZS=0.5984 与 Table 2 的 0.598 一致；GB 在 conf≥2 test split 上为 0.9929（Table 2 报告的 0.9674 是在 all 150,652 OH windows 上的值，scope 不同已注明）
- Comparison 3 的 Probe-FT=0.9763 与 Table 2 的 0.976 一致
- 所有 3 组差异均显著（p<0.001）

---
