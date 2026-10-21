# code plan 020 circularity ablation

**Temporal Score Incomparability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_plan_020_circularity_ablation_20260521T031201_result.json`
- **Structured JSON:** [`dc76463eccb208fab25e.json`](../../sessions/dc/dc76463eccb208fab25e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。核心结果：

**DIF removal 是所有非随机策略中扰动最小的**，直接反驳了 tautology 质疑：

| 策略 | ρ (2024) | z vs random |
|------|----------|-------------|
| DIF-C removal | 0.9970 | −9.5 |
| High discrimination | 0.9957 | −15.8 |
| High accuracy gap | 0.9657 | −156.5 |
| High variance | 0.9761 | −107.9 |
| Random baseline | 0.9990 | 0.0 |

关键发现：
- DIF-C 与 accuracy gap 的 item overlap 为 62.6%，但 DIF removal 的扰动比 accuracy gap 小 **16×**（z = −9.5 vs −157）
- MH 方法条件于 ability level，选出的 items 虽与 raw accuracy gap 相关（r = 0.61），但对 ranking 的影响远小于 naive gap selection
- DIF 与 discrimination/variance 的 overlap 分别只有 22%/43%，DIF 捕获的不是 general item quality

产出文件：
- `artifacts/plan_020/circularity_ablation_report.md`
- `artifacts/plan_020/circularity_ablation_results.csv`
- `artifacts/plan_020/strategy_overlap.csv`
- `artifacts/plan_020/metric_correlations.csv`

---
