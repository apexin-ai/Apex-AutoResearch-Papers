# verify number consistency

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_verify_number-consistency_20260514T143205_result.json`
- **Structured JSON:** [`2f098e6b4deb70ccb8b3.json`](../../sessions/2f/2f098e6b4deb70ccb8b3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

审计完成。**66 项定量 claim 全部核对，0 FAIL，1 NOTE**。

结果：
- **所有核心数字一致**：Δ_full=+29.60, Δ_nd=+2.84, DAF=90.41%, r=0.9698, p=8.12e-07, 245 episodes, 11 tasks, death rates, label distribution — 全部与 plan-012-full registry 匹配
- **Table 1 全部匹配**：5 策略的 scores、95% CIs、death rates 均与 bootstrap_95ci.json 和 plan-003-baseline-245eps 一致
- **Router 训练数字匹配**：GA=8 (65.4%/51.5%) 对应 plan-004-ablation-b，GA=1 (74.5%/79%/53.3%/26.7%) 对应 plan-004-v5
- **MATH pilot 全部匹配**：50 题、80% vs 72%、label 分布 1/5/44
- **唯一 NOTE**：4-seed balanced accuracy ±0.8% 略不精确（sample σ=0.884，population σ=0.766），属展示问题非错误
- **非数字问题**：Δ_nd vs Δ_no_death 下标符号在各节不统一，建议统一

报告已保存至 `artifacts/_project/report/paper_number_audit.md`。

---
