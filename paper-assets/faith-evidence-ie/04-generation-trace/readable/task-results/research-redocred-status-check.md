# research redocred status check

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_redocred_status_check_20260518T024828_result.json`
- **Structured JSON:** [`04373c58591d15935484.json`](../../sessions/04/04373c58591d15935484.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All data collected. Here's the summary:

---

## Plan_007 Re-DocRED Cross-Dataset 实验状态汇总

### 1. Re-DocRED 数据就绪度

| 文件 | 大小 | 文档数 | 过滤后三元组 |
|------|------|--------|-------------|
| train_annotated.json | 13.5 MB | 3,053 | 47,260 |
| dev.json | 2.2 MB | 500 | 7,473 |
| test.json | 2.2 MB | 500 | 7,547 |

数据完备，eval 使用 dev split (493 docs evaluated)。

### 2. SFT Eval (plan_007_redocred_4b_sft_eval_r2) — Registry: success

| Metric | Value |
|--------|-------|
| **Ign-F1** | **0.3659** |
| F1 | 0.3706 |
| Precision | 0.4316 |
| Recall | 0.3247 |
| Evi-F1 | 0.8170 |
| EDCR | 0.6674 |
| Format compliance | 99.6% |
| Truncated | 139/493 |

模型：Qwen3-4B + SFT adapter (DocRED 训练)，直接 zero-shot 迁移到 Re-DocRED。

### 3. RSFT Eval r2 (plan_007_redocred_rsft_eval_r2) — Registry: negative ⚠️ **实际是 BUG**

| Metric | Value |
|--------|-------|
| F1 | **0.0025** |
| Ign-F1 | 0.0026 |
| field_compliance | **0%** |
| evidence_format_rate | 0% |

**原因**：model_path=Qwen3-4B + sft_adapter=rsft_checkpoint，缺少 SFT 中间层。模型输出格式完全错误（field_compliance=0），19/7431 triplets 偶然命中。这不是真实的 negative 结果，是加载 bug。

### 4. RSFT Eval r4 (服务器有结果，未注册到 registry)

| Metric | Value | vs SFT | Delta |
|--------|-------|--------|-------|
| **Ign-F1** | **0.4145** | 0.3659 | **+4.86pp** |
| F1 | 0.4234 | 0.3706 | +5.28pp |
| Precision | 0.4962 | 0.4316 | +6.46pp |
| Recall | 0.3691 | 0.3247 | +4.44pp |
| Evi-F1 | 0.8182 | 0.8170 | +0.12pp |
| EDCR | 0.6210 | 0.6674 | -4.64pp |
| Format compliance | 100% | 99.6% | — |
| Truncated | 90/493 | 139/493 | fewer |

**正确的 3-param loading**：base_model=Qwen3-4B, sft_adapter=sft_output, model_path=rsft_output_ced_s43/checkpoint-510。

**RSFT 在 Re-DocRED 上显著优于 SFT (+4.86pp Ign-F1)**。

### 5. 结论

**plan_007 目标已达成**，但 registry 状态不一致：

- ✅ Cross-dataset transfer 验证完成：SFT 和 RSFT 均能 zero-shot 迁移到 Re-DocRED
- ✅ RSFT > SFT 在 Re-DocRED 上成立（Ign-F1: 0.4145 vs 0.3659, +4.86pp）
- ⚠️ Registry 中 r2 的 "negative" 结论是错误的（加载 bug 导致）
- ⚠️ r4 的正确结果未注册到 registry
- ⚠️ experiment_plan.yaml 中 plan_007 status 仍为 "planned"

**需要的修复操作**：
1. 将 r4 结果注册到 registry（作为 plan_007_redocred_rsft_eval_r5 或更新 r4）
2. 更新 r2 的 conclusion 为 "invalid"（加上 bug 说明）
3. 将 experiment_plan.yaml 中 plan_007 status 更新为 "done"

**不需要重做实验**——数据已齐全，SFT 和 RSFT 在 Re-DocRED 的对比结论明确。

---
