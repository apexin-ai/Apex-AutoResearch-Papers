# code plan 014 perturbation extended

**Policy Ambiguity Is Nocuous: Clause-Level Causal Effects on Customer-Service Agent Safety** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_plan_014_perturbation_extended_20260521T105804_result.json`
- **Structured JSON:** [`6bcca8445e0bb1b9f256.json`](../../sessions/6b/6bcca8445e0bb1b9f256.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Plan 014 完成。结果：

| 指标 | plan_010 (n=120) | plan_014 (n=300) |
|------|-----------------|-----------------|
| Δ_perturb | 3.33pp | **-0.67pp** |
| 95% CI | [-5.0, 13.33] | **[-8.0, 6.67]** |
| CI width | 18.33pp | **14.67pp** |
| McNemar p | — | **1.00** |
| Verdict | PASS | **PASS** |

CI 宽度从 18.33pp 收窄到 14.67pp（减少 3.66pp），Δ_perturb 接近零（-0.67pp），McNemar p=1.0 表明 perturbed 与 original 条件间无显著差异。这强化了 C1 因果推断：主研究观察到的 34pp ambiguity delta 不可归因于表面措辞变化。

输出文件：
- `perturbation_extended/results.json` — 完整统计结果
- `perturbation_extended/clauses_perturbation_extended.json` — 150 pairs
- `perturbation_extended/episodes.jsonl` — 300 episodes
- `perturbation_extended/judgments/judgments.jsonl` — 300 judgments

---
