# research literature scan ddl

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_literature-scan-ddl_20260516T051027_result.json`
- **Structured JSON:** [`dad7950ed0fdb60b8d5b.json`](../../sessions/da/dad7950ed0fdb60b8d5b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

文献扫描完成。报告已写入 `artifacts/literature_scan_20260516.md`。

**核心结论：**
- **无直接 novelty 威胁** — 没有论文做了 dual-constraint adaptive b* on (1-q)^b
- **6 篇建议必须引用**，最重要的是：
  1. **Subramanyam et al. 2025** (Scaling Laws Revisited) — 用 ESS 动机建模 corpus-level 数据质量 Q，需在 Related Work 中与我们的 per-batch α_eff(b) 做区分
  2. **Amin et al. 2025** (NeurIPS) — 理论证明 minimal curation 即可避免 collapse，支撑我们的 "lightweight detector sufficiency" claim
  3. **Kang et al. 2025** (EMNLP) — synthetic data mixing 大规模实证，强化问题动机
  4. **Kazdan et al. 2025** (ICML) — synthetic data 三种 workflow 分析
  5. **Martino et al. 2025** — ESS 与 Rényi 熵关系，强化 ESS 约束理论基础
  6. **Grangier et al. 2025** (ICLR) — CRISP clustered IS for pretraining

**3 个间接威胁**均有清晰 differentiation（corpus-level vs per-batch, loss-based vs provenance-based, existence proof vs constructive formula）。

---
