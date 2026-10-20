# code consensus framework formalization

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_consensus_framework_formalization_20260515T083742_result.json`
- **Structured JSON:** [`ce0d2b7032fc9ef2204e.json`](../../sessions/ce/ce0d2b7032fc9ef2204e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

D027 三个子任务全部完成。

**Sub-task 1 — Consensus Classification (≥4/5 methods, ≥3/4 seeds)**: 6 robust / 10 non-robust
- token_entropy→distinct_{1,2,3}: 5/5 unanimous
- ece→distinct_{1,2,3}: 4-5/5（TY 在 d2/d3 上是唯一 dissenter）
- canary→perplexity 方向全部 non-robust
- self_bleu、effective_rank 作为 canary 不可靠

**Sub-task 2 — Sensitivity Analysis**: token_entropy→distinct 在 9/9 配置下 100% stable；ece→distinct_2/d3 在 7/9 下 robust（borderline 如预期）；self_bleu 全系 0%

**Sub-task 3 — FPR/FNR**:

| Method | FPR | FNR |
|--------|-----|-----|
| naive | **100%** | 0% |
| differenced | 0% | 0% |
| threshold | 11.1% | 0% |
| TY | 0% | **20.8%** |
| perm_granger | 11.1% | 0% |
| **consensus** | **0%** | **0%** |

TY 的 FNR (20.8%) 低于预估的 50-94%，因为 TY 在 4 个最强 robust pair 上实际通过了（FN 集中在 ece→d2/d3 的 5 个 seed 观测）。核心叙事成立：naive 全面 FP，TY 是唯一有 FNR 的方法，consensus 取得平衡。

**产出**: 4 个文件已写入 `artifacts/analysis/consensus_framework/`，服务器端结果在 `results/mvp/analysis/consensus/`。

---
