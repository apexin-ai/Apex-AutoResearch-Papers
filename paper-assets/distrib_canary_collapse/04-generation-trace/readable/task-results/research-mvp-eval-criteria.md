# research mvp eval criteria

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_mvp-eval-criteria_20260514T082626_result.json`
- **Structured JSON:** [`e07c312d9d8b0ebefd61.json`](../../sessions/e0/e07c312d9d8b0ebefd61.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已完成：

- **文件**: `artifacts/mvp_evaluation_criteria.md`
- **manifest.yaml**: 已注册为 `art_20260514_8c1d3e` (type: report)

文档覆盖全部 6 项要求：
1. **显著性阈值** — permutation test (B=10000), p<0.10 + |r|≥0.60 双重门槛，含小样本效力讨论
2. **3/3 一致性** — 严格负 lag 规则，lag=0 不算 lead，附具体示例表
3. **非单调指标** — Gen 4–9 OLS 斜率法，含三种结果（一致下降/一致上升/混合）的处理路径
4. **MAUVE 地板效应** — Gen 0 < 0.10 且 CV < 0.50 则降级为补充指标，perplexity + distinct-n 替代
5. **分级判定** — STRONG PASS / PASS / CONDITIONAL PASS / FAIL 四级，2/3 一致明确判 NO LEAD
6. **决策总表** — 6 步检查流程 + 各判定对应的后续行动

---
