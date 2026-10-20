# analysis d102 t25 a050 v3

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_d102_t25_a050_v3_20260522T071226_result.json`
- **Structured JSON:** [`faad63df9460b831cb4c.json`](../../sessions/fa/faad63df9460b831cb4c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

D102 分析完成。

**结果：PermG FDR = 6/8 forward, 0/8 reverse**

| Method | Forward | Reverse |
|--------|---------|---------|
| PermG FDR | 6/8 | 0/8 |
| Diff xcorr FDR | 6/8 | 6/8 |
| Threshold onset | 6/8 | — |
| TY Granger | 6/8 | — |
| Robust (≥3/5) | 6/8 | — |

6/8 ceiling 在 T=25 保持一致，与 T=10/15/20 的 α=0.50 结果完全匹配。失败的 2 对均为 mauve downstream（0/5 和 2/5），符合已知 pattern。

**关键路径：**
- 结果目录：`/root/autodl-tmp/distrib_canary_collapse/results/phase_diagram/t25_a050_s42_fp32`
- 最终 checkpoint：`.../t25_a050_s42_fp32/gen_25/checkpoint`
- 分析 JSON：`.../t25_a050_s42_fp32/analysis/5method_leadlag.json`
- 本地 JSON：`artifacts/phase_diagram_t25_a050_s42_fp32_v3/data/d102_t25_a050_s42_fp32_v3.json`
- 本地报告：`artifacts/phase_diagram_t25_a050_s42_fp32_v3/report/D102_t25_a050_s42_fp32_v3_analysis.md`

---
