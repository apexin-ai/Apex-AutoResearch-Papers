# research exp 009 wang differentiation

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_exp_009_wang_differentiation_20260519T131120_result.json`
- **Structured JSON:** [`be68b2fa995a3ec487d5.json`](../../sessions/be/be68b2fa995a3ec487d5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已完成。文件写入 `/root/entrainment_gated_ft/analysis/wang_et_al_differentiation.md`（178行）。

与之前版本的关键修正：

1. **新增论文元数据**：标题、作者、日期、arXiv ID
2. **修正数值错误**："4/6 benchmarks significant" → 实际只有 LAMBADA 显著（p=0.008），ARC-Easy/MMLU 仅 suggestive（p=0.117）
3. **修正 340M 数据**：std reduction 从错误的 38% 修正为 56%（0.025→0.011 at attn=4），并标注 rebound 至 0.015
4. **修正 task-specificity 数值**：用 CSV 实际计算值替代之前的估算值（HellaSwag ρ=+0.3, ARC-C ρ=+0.6 — 这些是正相关，即无收敛甚至发散）
5. **新增 Wang et al. 原始表格数据**：Tables 2-4 的关键数值，作为 differentiation 的证据基础
6. **新增 verbatim extractions**：补充了 perplexity plateau、diminishing returns、practical recommendations 等此前遗漏的关键引文

核心结论不变：四个 differentiation 维度均为 **fully novel**，Wang et al. 提供基础设施（72 models），我们提供分析框架（equalizer effect + paradox）。

---
