# analysis fig overview and vc rho

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_fig_overview_and_vc_rho_20260518T233414_result.json`
- **Structured JSON:** [`2a760b7bc76698caa000.json`](../../sessions/2a/2a760b7bc76698caa000.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

### Check 1: fig_overview

**不存在。** 项目中没有任何 `fig_overview` 文件或相关引用：
- `docs/paper/figures/` 只有 `fig_selection_gap` 和 `fig_degeneracy_lp_scatter`
- 所有 tex 文件中无 "overview" 引用
- 全项目搜索无匹配

**结论：fig_overview 不存在，无数据依赖，不受影响。**

---

### Check 2: FewNERD VC ρ_global

来源确认：`fewnerd_multiseed_unified_v2.json`（unified 管道产出）

| Seed | VC ρ_global |
|------|------------|
| seed42 | **0.3858** |
| seed123 | 0.3633 |
| seed456 | 0.3943 |
| 3-seed mean | 0.3811 |
| seed789 (独立文件，未入 unified_v2) | 0.2673 |

- **ρ=0.39 对应 seed42 的 0.3858（四舍五入）**，来自 unified 管道，已确认
- VC 基于 entity-level 投票一致性，不依赖 F1 函数，**不受 F1 迁移影响**
- 注：cross_seed_summary 中未包含 VC ρ 的聚合值，只有 LP 相关指标

---
