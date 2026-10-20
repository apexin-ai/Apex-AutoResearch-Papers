# research paper experiments prep

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_paper-experiments-prep_20260516T012513_result.json`
- **Structured JSON:** [`e7fe7ed5b1d8c0fb26da.json`](../../sessions/e7/e7fe7ed5b1d8c0fb26da.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已写入 `artifacts/paper_tables_data.md` 并注册为 artifact (`art_20260516_0bfbd6`)。

核心发现：
- **Table 1**: Adaptive (17.651±0.007) 与 Grid-b=0.5 (17.646±0.007) 性能相当，但 Adaptive 无需调 b；ESS-only (17.723) 甚至不如 Uniform (17.694)
- **Table 2**: PPL 随 b 单调递增，b=0.5 最优；seed456 b≥2 因 checkpoint resume 异常，论文仅报 2 seeds
- **Table 3**: τ=0.8 最优 (17.653)，两端 (0.5, 0.95) 均退化
- **Table 4**: n_min=3 最优 (17.644)，n_min=1 方差过大导致不稳定，n_min=4 退化为 uniform

---
