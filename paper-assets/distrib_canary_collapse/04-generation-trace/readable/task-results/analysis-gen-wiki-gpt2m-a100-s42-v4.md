# analysis gen wiki gpt2m a100 s42 v4

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_gen_wiki_gpt2m_a100_s42_v4_20260518T113124_result.json`
- **Structured JSON:** [`db88fff33a3f32b78e1e.json`](../../sessions/db/db88fff33a3f32b78e1e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成，实验已标记 DONE(success)。

## 结果摘要

**Table 7 GPT-2m 行**:

| Naive | Diff | Thresh | PG_fwd | PG_rev | TY | K>=4 |
|-------|------|--------|--------|--------|-----|------|
| 8/8 | 8/8 | 8/8 | 6/8 | 3/8 | 5/8 | **6/8** |

**与 Baseline (Pythia-410M) 几乎一致**：Naive/Diff/Thresh/PG_fwd/PG_rev/K>=4 完全相同，TY 从 4/8 提升到 5/8。

**Drift 亮点**：
- token_entropy: -86.6% (严重坍缩)
- perplexity: +50527.6% (32.6 → 16520.5，所有条件中最极端)
- distinct_1/2/3: -12% ~ -14%

**结论**: GPT-2m 确认 canary-downstream 因果信号跨架构泛化成立，K>=4=6/8 与其他条件 (5/8-6/8) 一致。报告已注册 (`art_20260518_bd30d8`)，registry 已更新为 DONE。

---
