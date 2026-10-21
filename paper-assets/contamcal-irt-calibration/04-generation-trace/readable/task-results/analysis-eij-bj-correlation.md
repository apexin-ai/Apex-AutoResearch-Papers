# analysis eij bj correlation

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_eij-bj-correlation_20260522T231724_result.json`
- **Structured JSON:** [`51f2777ab2e509319d62.json`](../../sessions/51/51f2777ab2e509319d62.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已生成至 `artifacts/eij_bj_correlation.md`。

核心结论：**τ_j（per-item RRF exposure）与 b_j（item difficulty）的相关性可忽略不计**——所有 benchmark 的 Pearson |r| < 0.13，R² < 1.4%。γ 的 identifiability 不受影响，原因：
1. exposure 和 difficulty 在数据空间近乎正交
2. γ 的识别来自 dosage 跨 respondent 的变化（0→5→25→100），在 dosage=0 时 γ 项消失，b 从 clean respondent 识别，即使 τ-b 有相关也不影响

---
