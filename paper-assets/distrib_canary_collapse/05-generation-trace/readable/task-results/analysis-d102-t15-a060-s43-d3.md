# analysis d102 t15 a060 s43 d3

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_d102-t15-a060-s43-d3_20260523T200904_result.json`
- **Structured JSON:** [`91cbac0d33b6709849d8.json`](../../sessions/91/91cbac0d33b6709849d8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。

**D102 结果总结 (scale_14b_t15_a060_s43_fp32, downstream=distinct_3)**:

| Pair | Votes | Methods |
|------|-------|---------|
| token_entropy → distinct_3 | **4/5** | diff, threshold, perm, ty |
| ece → distinct_3 | **4/5** | naive, diff, threshold, perm |

- **Robust pairs: 2/2 (100%)**
- 所有 5 种方法中 4 种对两个 pair 都检测到 forward，仅 TY 在 ece→d3 未达显著（p=0.22）
- Entropy drop-then-recover (2.97→1.80→2.10) 不影响 lead-lag 检出——DiffXCorr (r=0.94) 和 TY 均对非平稳性鲁棒
- distinct_3 单调下降 0.817→0.566 (-31%)，信号清晰
- MAUVE 确认无信号（range 0.005），验证 Reviewer #155 的判断

**产出**:
- 远程 JSON: `results/analysis/D102_14b_t15_a060_s43_fp32_d3.json`
- 本地 JSON: `artifacts/D102_14b_t15_a060_s43_fp32_d3.json`
- 分析报告: `artifacts/_project/d102_t15_a060_s43_d3_result_20260523.md`
- Registry metrics 已更新

---
