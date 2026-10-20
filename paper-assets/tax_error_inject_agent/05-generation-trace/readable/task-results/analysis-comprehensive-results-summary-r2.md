# analysis comprehensive results summary r2

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_comprehensive-results-summary-r2_20260515T002203_result.json`
- **Structured JSON:** [`cffb651c1d4369a7cbe0.json`](../../sessions/cf/cffb651c1d4369a7cbe0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已生成并注册 artifact `art_20260515_b5a5a7`。

汇总覆盖 7 个维度：
1. **多种子 Clean Eval** — Vanilla 65.3%±3.3, TaxEI 56.7%±8.6, Random 60.7%±7.6 (2 seeds)
2. **Recovery Eval** — TaxEI 59.6% vs Vanilla 61.7%, 含 per-operator breakdown
3. **Dose-Response** — 10% injection -3.6pp, 25% injection -16.4pp
4. **训练 Metrics** — final loss, token accuracy, duration 全表
5. **统计检验** — McNemar p-values 均不显著 (p=0.375~1.0)
6. **实验时间线** — 从轨迹收集到 ablation 的全流程
7. **6 条核心 Negative Results** — 直接可用于论文 conclusion

唯一缺口：`v4-random-seed123-eval` 仍在 RUNNING，完成后需更新 Random 的 3-seed 统计。

---
