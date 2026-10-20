# ops registry cleanup stale

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_registry-cleanup-stale_20260522T193257_result.json`
- **Structured JSON:** [`82d58aec2de9bc11531b.json`](../../sessions/82/82d58aec2de9bc11531b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

103/103 全部完成。汇报：

## Registry 清理完成

**总计标记：103 个实验**（notes 添加 `[ARCHIVED] superseded by ...`）

### 按前缀分组

| 前缀 | 标记数 | 说明 |
|------|--------|------|
| mvp2_* | 35 | 统一标注 "superseded by final pipeline (plan017/plan019 series)" |
| plan_0* / plan0* | 38 | 各自指向成功的 r2/r3/r4/r5 或后续 plan 版本 |
| d1xx_* | 7 | 指向 _fix / _bf16 / _r3 等修正版本 |
| eval_* | 10 | 指向 _r2 或正确版本 |
| llama_sft_* | 4 | 指向 _r3 版本 |
| wave1_* | 2 | 指向 _r2 版本 |
| rsft_ced_* | 5 | 指向 _r3 / _r4 版本 |
| retrain_/reeval_/test_eval_/rsft_s44_* | 2 | 指向 _v2 或对应成功版本 |

### 跳过的实验（6 个，无明确替代者）

1. `eval_plan_012_dpo_1ep_fixed` — DPO 方向整体放弃（结论 negative）
2. `eval_plan_012_dpo_ced_ckpt400` — 同上
3. `lead2_rsft_grpo_ced` — 训练失败，checkpoint eval 独立成功
4. `lead2_rsft_grpo_ced_r2` — 同上
5. `plan019_1_7b_rsft_no_evidence_eval` — 结论是 negative（evidence 有帮助），非技术失败
6. `seed_comparison_prep` — 一次性分析任务

---
