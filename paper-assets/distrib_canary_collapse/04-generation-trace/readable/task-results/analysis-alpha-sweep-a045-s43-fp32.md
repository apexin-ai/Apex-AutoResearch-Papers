# analysis alpha sweep a045 s43 fp32

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_alpha_sweep_a045_s43_fp32_20260520T100117_result.json`
- **Structured JSON:** [`f254f25b4c988d50597e.json`](../../sessions/f2/f254f25b4c988d50597e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。

## 结论: **SUCCESS** — α=0.45 blind zone 跨 seed 稳健

| 指标 | s42 | s43 |
|------|-----|-----|
| PermG_fwd | 0/8 | **0/8** |
| PermG_rev | 0/8 | 0/8 |
| K≥3 | 3/8 | 2/8 |
| K≥4 | 0/8 | 0/8 |
| entropy drift | -18.73% | -19.61% |
| ppl drift | +12.19% | +12.37% |

两个 seed 在 α=0.45 均 PermG=0/8，退化幅度也高度一致（entropy ~-19%, ppl ~+12%）。onset boundary [0.45, 0.50] 现已有 2-seed 支撑。

注意：个体方法 seed 敏感性很高（naive_xcorr 从 7/8 降到 1/8，ty_granger 从 1/8 升到 7/8），但 PermG（FDR 校正 + 置换检验）在两个 seed 上完全一致，进一步验证了 PermG 作为主要指标的稳健性。

---
