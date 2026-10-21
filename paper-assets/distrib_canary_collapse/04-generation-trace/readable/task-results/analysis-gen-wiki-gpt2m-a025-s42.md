# analysis gen wiki gpt2m a025 s42

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_gen_wiki_gpt2m_a025_s42_20260516T082739_result.json`
- **Structured JSON:** [`ffdc3d74d161c181d3b4.json`](../../sessions/ff/ffdc3d74d161c181d3b4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。核心结论：

**SUCCESS — 跨架构验证支持 Claim 2 (regime-dependent validity)**

关键发现：

| | GPT-2 small α=0.25 | GPT-2 medium α=0.25 |
|---|---|---|
| PPL | 26.95→22.32 (-17%) | 32.63→18.12 (-45%), gen 1 后稳定 |
| Distinct-1 | -40.3% | -23.5% |
| Distinct-2 | -57.1% | -31.6% |
| Token entropy | -4.1% | -32.8% |
| ECE | +79.7% | +427.3% |
| 定性 regime | Low collapse | Low collapse |

- **6/7 指标方向一致**，唯一 mismatch 是 effective rank（架构差异导致基线和方向不同）
- GPT-2m α=0.25 vs α=1.0 对比：α=1.0 PPL 爆炸至 14,617、entropy 崩至 0.48，α=0.25 完全无 runaway 迹象——同架构内 regime 边界清晰
- **架构效应**：GPT-2m 在 diversity (distinct-n) 上更鲁棒（-24~32% vs -40~60%），但在分布度量 (entropy/ECE) 上更敏感——大模型有更多表征冗余保持词汇多样性

**Regime 分类：Low collapse**

报告已保存至 `artifacts/gen_wiki_gpt2m_a025_s42/report/analysis_gen_wiki_gpt2m_a025_s42.md`

---
