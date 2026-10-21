# analysis exp fewnerd pretrained n16 s42 v2

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp_fewnerd_pretrained_n16_s42_v2_20260523T002055_result.json`
- **Structured JSON:** [`c3b63c7ae764cada5953.json`](../../sessions/c3/c3b63c7ae764cada5953.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新为 DONE/success。

**exp_fewnerd_pretrained_n16_s42_v2 最终结果（gold-nonempty, n=32,565）：**

| 指标 | N=8 s42 | N=16 s42 |
|---|---|---|
| greedy_f1 | 0.5384 | 0.5373 |
| mv_strict_f1 | 0.5788 | 0.5779 |
| mv_delta_strict | +4.03pp | **+4.06pp** |
| oracle_f1 | 0.6508 | **0.6786** (+2.78pp) |
| degeneracy | 12.2% | **7.6%** |
| alpha_crit_eff_strict | — | 0.4398 |
| mv_capture_rate | — | 28.8% |

**结论**: N=16 符合 N-scaling 预期——greedy/MV delta 稳定（seed 间差异 <0.1pp），oracle headroom 显著扩大（+2.78pp），退化率下降近一半（12.2%→7.6%）。MV 仍然能捕获 28.8% 的 oracle headroom，与 N=8 一致。实验 success。

---
