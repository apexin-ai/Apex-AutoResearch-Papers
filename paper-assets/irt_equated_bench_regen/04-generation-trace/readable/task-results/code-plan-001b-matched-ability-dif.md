# code plan 001b matched ability dif

**Temporal Score Incomparability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_plan_001b_matched_ability_dif_20260520T211545_result.json`
- **Structured JSON:** [`e9dfc1281e7cc1a94e3c.json`](../../sessions/e9/e9dfc1281e7cc1a94e3c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果：FAILURE

Matched-ability DIF 未能隔离出污染信号。核心数据：

| 方法 | C% | FPR | Enrichment |
|------|-----|------|-----------|
| plan_001 raw temporal | 31.3% | ~0.31 | 0.96 |
| plan_001b ≥2 quintiles | 47.5% | 0.48 | 0.98 |
| plan_001b CMH pooled | 33.3% | 0.33 | 1.00 |
| plan_001b ≥3 quintiles | 25.4% | 0.26 | 0.96 |

**所有方法的 enrichment 都在 0.94–1.04 之间，与随机无异。** 控制能力后 DIF 信号不但没有聚焦到污染 items 上，C% 反而从 31.3% 升到 47.5%（因为 quintile 内样本量更小，统计波动更大导致更多 false flags）。

关键诊断：
- 5 个 quintile 的 per-quintile enrichment 全在 0.94–1.04，没有任何一个 quintile 显示出差异化信号
- 6365/12508 items 在至少一个 quintile 中有 NaN delta（样本量不足导致分层失败），但 CMH 补回了这些 items，enrichment 仍为 1.00
- Q2/Q3 的 C% 最高（34–42%），对应的是 2023/2024 模型比例最不均衡的 quintile（Q2: 406 vs 106），说明组间 N 不平衡放大了 type-I error

**结论：MH-DIF（含 ability matching）对 Li et al. proxy labels 没有区分力。** 污染 items 和 clean items 被等比例地 flag 为 DIF。这说明 temporal cohort 间的 item-level 响应差异主要由能力差异和随机噪声驱动，而非 item-specific contamination。

产出文件已保存到 `artifacts/plan_001b/`。

---
