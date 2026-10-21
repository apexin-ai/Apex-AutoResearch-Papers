# analysis phase2 cross alpha fdr rerun

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_phase2_cross_alpha_fdr_rerun_20260515T105507_result.json`
- **Structured JSON:** [`df583680cfc24478512f.json`](../../sessions/df/df583680cfc24478512f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已保存。核心结果：

**Granger**: 10/32 raw-sig → **1/32 FDR-sig**（仅 ECE→d1 at α=1.0 p_fdr=0.019 存活）。D024 的 "canary regime switch" 叙述在 FDR 下不成立。

**Method × α sig rates delta (raw → FDR)**:
- Toda-Yamamoto 受影响最大：α=0.25 从 25%→0%，α=0.50 从 38%→12%（与 C001 约束一致——TY df 太低）
- diff_xcorr 在 α=0.00 和 α=1.00 分别下降 19% 和 13%
- naive_pearson 和 threshold_onset 不受影响

**Consensus robust pairs 不变**：0/16 → 1/16 → 0/16 → 6/16 的 α 递进模式在 FDR 下保持，因为 consensus 要求 ≥4/5 methods 一致，本身就是隐式多重检验保护。

报告位于：`artifacts/analysis/cross_alpha_fdr_4point.md`

---
