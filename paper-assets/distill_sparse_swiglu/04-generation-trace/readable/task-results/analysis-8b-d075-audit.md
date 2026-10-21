# analysis 8b d075 audit

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_8b_d075_audit_20260519T210305_result.json`
- **Structured JSON:** [`01a4e3e4136499826f06.json`](../../sessions/01/01a4e3e4136499826f06.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Now I have all the data needed. Here's the complete audit:

## LLaMA-8B Eval 实验 D075 状态审计

D075 修复时间：**2026-05-19 13:50 UTC**。所有 LLaMA-8B eval 均在此之前完成。

### Table 2 核心实验

| exp_id | 方法 | Tasks | created_at | sparsity_mode | D075状态 | 论文可用? |
|--------|------|-------|-----------|--------------|---------|----------|
| **bench_dense** | Dense baseline | 5-task | 05-16 | `--dense` | N/A | Yes |
| **bench_kl30_uniform** | KL 30% uniform s42 | 5-task | 05-16 | `teal_global` | **Pre-D075** | 需验证 |
| **bench_kl30_global** | KL 30% global s42 | 5-task | 05-16 | `teal_global` | **Pre-D075** | 需验证 |
| **bench_teal30** | TEAL vanilla 30% | 5-task | 05-16 | `teal_vanilla` | N/A | Yes |
| **bench_teal50** | TEAL vanilla 50% | 5-task | 05-16 | `teal_vanilla` | N/A | Yes |
| **bench_teal70** | TEAL vanilla 70% | PPL only | 05-17 | TEAL vanilla (sourced) | N/A | Yes |
| **bench_kl50_global** | KL 50% global s42 | 5-task | 05-16 | `teal_global` | **Pre-D075** | 需验证 |
| **bench_kl50_uniform** | KL 50% uniform s42 | 5-task | 05-16 | `teal_global` | **Pre-D075** | 需验证 |
| **bench_kl40_global** | KL 40% global s42 | 5-task | 05-16 | `teal_global` | **Pre-D075** | 需验证 |
| **bench_kl70_global** | KL 70% global s42 | PPL only | 05-17 | `teal_global_masks` | **Pre-D075** | 需验证 |

### Table 2 多 seed 实验

| exp_id | 方法 | Tasks | created_at | sparsity_mode | D075状态 | 论文可用? |
|--------|------|-------|-----------|--------------|---------|----------|
| **kl30_s123_uniform_v3** | KL 30% uniform s123 | 5-task | 05-18 | `teal_global` | **Pre-D075** | 需验证 |
| **kl30_s456_uniform_v3** | KL 30% uniform s456 | 5-task | 05-18 | `teal_global` | **Pre-D075** | 需验证 |
| **kl30_s123_global_v3** | KL 30% global s123 | 5-task | 05-18 | `teal_global` | **Pre-D075** | 需验证 |
| **kl30_s456_global_v3** | KL 30% global s456 | 5-task | 05-18 | `teal_global` | **Pre-D075** | 需验证 |
| **kl30_8b_s123_eval** | KL 30% s123 | 5-task | 05-18 | `teal_global`(推测) | **Pre-D075** | 需验证 |
| **kl30_8b_s456_eval** | KL 30% s456 | 5-task | 05-18 | `teal_global`(推测) | **Pre-D075** | 需验证 |
| **bench_kl50_uniform_s123** | KL 50% uniform s123 | 5-task | 05-16 | `teal_global` | **Pre-D075** | 需验证 |
| **bench_kl50_uniform_s456** | KL 50% uniform s456 | 5-task | 05-16 | `teal_global` | **Pre-D075** | 需验证 |

### BCE iso-compute 实验

| exp_id | 方法 | Tasks | created_at | sparsity_mode | D075状态 | 论文可用? |
|--------|------|-------|-----------|--------------|---------|----------|
| **eval_bce_v3_s42** | BCE v3 50% s42 | evaluate.py+bench | 05-16 | `teal_global` | **Pre-D075** | 需验证 |
| **bce_isocompute_v3_s42_eval** | BCE v3 50% s42 | 5-task | 05-18 | `teal_global` | **Pre-D075** | 需验证 |
| **bce_isocompute_v3_s123_eval** | BCE v3 50% s123 | 5-task | 05-17 | `teal_global` | **Pre-D075** | 需验证 |
| **bce_isocompute_v3_s456_eval** | BCE v3 50% s456 | 5-task | 05-17 | `teal_global` | **Pre-D075** | 需验证 |
| **bce_30pct_s42_eval** | BCE 30% s42 | 5-task | 05-18 | `teal_global`(global_topk) | **Pre-D075** | 需验证 |
| **bce_50pct_teal_global_unified** | BCE 50% global s42 | 5-task | 05-19 01:07 | `teal_global` | **Pre-D075** | 需验证 |
| **bce_isocompute_hellaswag_piqa_v2** | BCE 30% uniform s42 | HS+PIQA | 05-19 01:08 | `teal_global` | **Pre-D075** | 需验证 |

### HellaSwag/PIQA 补充实验

| exp_id | 方法 | Tasks | created_at | sparsity_mode | D075状态 | 论文可用? |
|--------|------|-------|-----------|--------------|---------|----------|
| **downstream_dense_baseline** | Dense | HS+PIQA+BoolQ | 05-17 | `--dense`(无checkpoint) | N/A | Yes |
| **downstream_extended_kl30_s42** | KL 30% global s42 | HS+PIQA+BoolQ | 05-17 | `teal_global` | **Pre-D075** | 需验证 |
| **downstream_teal30_baseline** | TEAL 30% | HS+PIQA+BoolQ | 05-17 | `teal_vanilla` | N/A | Yes |
| **kl30_uniform_hellaswag_piqa** | KL 30% uniform s42 | HS+PIQA | 05-18 | `teal_global` | **Pre-D075** | 需验证 |
| **kl50_global_hellaswag_piqa** | KL 50% global s42 | HS+PIQA | 05-18 | `teal_global` | **Pre-D075** | 需验证 |

### Sparsity regime curve 实验

| exp_id | 方法 | Tasks | created_at | sparsity_mode | D075状态 | 论文可用? |
|--------|------|-------|-----------|--------------|---------|----------|
| **kl_sparsity25_s42_eval_teal** | KL 23% global | 5-task | 05-18 | `teal_global` | **Pre-D075** | 需验证 |
| **kl_sparsity35_s42_eval_teal** | KL 33.6% global | 5-task | 05-18 | `teal_global` | **Pre-D075** | 需验证 |
| **kl_sparsity45_s42_eval_teal** | KL 44.9% global | 5-task | 05-18 | `teal_global` | **Pre-D075** | 需验证 |

### 其他 KL eval

| exp_id | 方法 | Tasks | created_at | sparsity_mode | D075状态 | 论文可用? |
|--------|------|-------|-----------|--------------|---------|----------|
| **eval_kl30_teal_30pct** | KL 30% s42 | evaluate.py PPL | 05-16 | evaluate.py(非benchmark_eval) | **Pre-D075** | 需验证(evaluate.py同一bug) |
| **d030_kl40_uniform** | KL 40% uniform | bench+train | 05-16 | `per_token` | 可能不受影响 | 需确认code path |
| **kl30_s42_global_mmlu_recheck** | KL 30% global s42 | MMLU only | 05-18 | `teal_global` | **Pre-D075** | 需验证 |

---

### 总结

| 类别 | 数量 | D075状态 |
|------|------|---------|
| Dense / TEAL vanilla (不受影响) | **6** | N/A, 论文可用 |
| KL + teal_global (受影响) | **~27** | 全部 Pre-D075 |
| BCE + teal_global (受影响) | **7** | 全部 Pre-D075 |
| per_token mode (待确认) | **1** (d030_kl40_uniform) | 可能不受影响 |

**结论**：所有使用 `--sparsity_mode teal_global` 的 LLaMA-8B eval 实验均为 **Pre-D075**（最晚的也在 2026-05-19 03:15 完成，远早于 D075 的 13:50 UTC 修复时间）。需要判断 D075 bug 是否在 8B 模型上实际触发（条件：predictor active ratio < keep ratio），如果触发则这些实验需要 post-D075 重跑。

---
