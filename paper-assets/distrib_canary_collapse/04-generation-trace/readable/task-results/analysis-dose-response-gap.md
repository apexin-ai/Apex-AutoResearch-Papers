# analysis dose response gap

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_dose-response-gap_20260519T071655_result.json`
- **Structured JSON:** [`e94622c3ca3d65bf4d6d.json`](../../sessions/e9/e94622c3ca3d65bf4d6d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。

## 汇总

### 报告已注册
`art_20260519_4b0a1a` → `artifacts/_project/report/report_dose_response_gaps.md`

### Dose-Response Map fp32 状态
- **✅ fp32 完成**: α=0.05, 0.60, 1.00（3/8 点）
- **部分 fp32**: α=0.10（s43 done, s42 RUNNING）
- **RUNNING**: α=0.50（3 seeds fp32, ~10:30 UTC 完成）
- **fp16 缺口**: α=0.00（3 seeds）、α=0.25（3 seeds）、α=0.75（低优先）

### experiment_plan.yaml 6 条过期指针已修复
| Plan ID | 修复 |
|---------|------|
| plan_001 (α=0.25 s42) | `alpha_sweep_a025_s42_v3` → `null`（待 fp32 重跑）|
| plan_001b (α=0.00 s42) | `alpha_sweep_a000_s42` → `null`（待 fp32 重跑）|
| plan_001c (α=0.50 s42) | `alpha_sweep_a050_s42` → `alpha_sweep_a050_s42_fp32`（RUNNING）|
| plan_001d (α=0.75 s42) | `alpha_sweep_a075_s42` → `null`（低优先）|
| plan_010 (GPT-2m) | `gen_wiki_gpt2m_a100_s42_v3` → `gen_wiki_gpt2m_a100_s42_v4`（success）|
| plan_030 (OPT-1.3B s43) | `gen_opt13b_a100_s43_bf16` → `null`（killed，需重排）|

### 下一步
α=0.00 + α=0.25 共 6 seeds fp32 重跑，最早 ~10:30 UTC（a050 完成释放 GPU 后）启动，~15:30 UTC 完成。完成后 map 达 7/8 fp32 覆盖。

---
