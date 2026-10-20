# research paper results prep

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_paper-results-prep_20260514T083314_result.json`
- **Structured JSON:** [`b0c25e2a5af6c7f3daa9.json`](../../sessions/b0/b0c25e2a5af6c7f3daa9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已写入 `artifacts/paper_draft/results_tables.md`，包含 6 张表格：

1. **Table 1** — Model×Dosage eval 矩阵（12 格，6 格有数据，4 格确认 legacy format）
2. **Table 2** — d000 跨 seed 一致性（MC benchmarks CV<5%，generation benchmarks 高方差）
3. **Table 3** — MVP 4PL+γ base recovery（PASS，γ_rel_bias=6.8%）
4. **Table 4** — MVP confounding robustness（PASS，θ-exposure corr=0.38 下仍可分离）
5. **Table 5** — EXP-004 sweep（43/120 runs，AUC×N_models 矩阵）
6. **Table 6** — SFT 训练汇总

主要发现：
- **实际可用于论文分析的 eval 结果为零** — 所有 0.5B eval 确认 legacy mc_format，1.5B/3B format 未标注，contaminated dosage (d005/d100) 只有 0.5B legacy 数据
- **3B GSM8K 异常低**（0.117/0.176 vs 1.5B 的 0.637），需要排查
- **Simulation 结果可直接用于论文**（MVP + EXP-004 前 43 runs 均可）
- Gap analysis 列出了填满矩阵需要的实验清单

---
