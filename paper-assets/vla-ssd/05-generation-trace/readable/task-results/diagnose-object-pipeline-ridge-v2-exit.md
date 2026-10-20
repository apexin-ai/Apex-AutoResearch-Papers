# diagnose object pipeline ridge v2 exit

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_object_pipeline_ridge_v2_exit_20260521T085047_result.json`
- **Structured JSON:** [`944512d0aa71d44c38cc.json`](../../sessions/94/944512d0aa71d44c38cc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Cron 已不存在（可能在之前的 session 中清除或过期）。

---

## 诊断结果：`object_pipeline_ridge_v2` — 部分完成（trained only）

**状态**: Pipeline 全 6 phase 成功完成，耗时 96.3 min。但**只跑了 trained model**（`openvla-7b-finetuned-libero-object`），无 untrained 对照。按 C001 约束，不下结论，只记数字。

**输出文件** (5个，位于 `/root/autodl-tmp/vla-ssd/results/libero_object/`):
- `action_r2_probing.json`, `l1_attention_profile.json`, `cross_instruction_classification.json`, `rsa_analysis.json`, `counterfactual_combined.json`

### Trained Model 关键 Metrics

**Action R² Probing (Ridge)**

| Position | Peak R² | Peak Layer | Last Layer (L31) |
|----------|---------|------------|------------------|
| img_mean | 0.8071 | L12 | 0.7931 |
| last_pre | 0.7871 | L13 | 0.6663 |

img_mean R² 全层稳定 ~0.80；last_pre 在中间层达峰后尾部下降至 0.67。

**L1 Attention Profile**
- **24/32 instruction-dominant**, 0 image-dominant, 8 mixed
- Top heads: h0 (0.880), h22 (0.828), h10 (0.745), h25 (0.740), h14 (0.721)

**Cross-instruction Classification**
- **所有层 = 1.000 accuracy**（ceiling effect，10 个不同 object name 太容易区分）

**RSA**
- Best: L28_last_preaction = **0.622** (CI: 0.589–0.651)
- last_pre RSA 从 L0 (0.493) 上升至 L28 (0.622)

**Counterfactual (trained)**

| Condition | Cohen's d | Cross-task mean d | Token div |
|-----------|-----------|-------------------|-----------|
| empty | **1.212** | 1.223 | 1.000 |
| wrong | **1.188** | 1.193 | 0.999 |
| shuffled | **1.122** | 1.125 | 1.000 |
| paraphrased | **0.896** | 0.898 | 0.963 |

### 与 Goal 实验初步数值对比（不做因果归因，仅记录差异）

| Metric | Goal (trained, from counterfactual_instruction) | Object (trained) |
|--------|------------------------------------------------|-------------------|
| Counterfactual: empty d | 0.968 | **1.212** |
| Counterfactual: wrong d | 0.844 | **1.188** |
| Counterfactual: shuffled d | 0.625 | **1.122** |
| Counterfactual: paraphrased d | 0.697 | **0.896** |
| L1 instruction-dominant heads | — | 24/32 |

Object suite 全部 counterfactual condition 的 Cohen's d 均高于 Goal suite（注意 Goal 数据来自 untrained base model `counterfactual_instruction` 实验，非 finetuned model，因此不可直接对比——需要 Object untrained 数据才能做 paired comparison）。

### Registry 更新
- `status=DONE`, `conclusion=negative`（缺 untrained 对照，C001 约束）
- Metrics 和 notes 已写入

### 下一步
需要跑 **untrained base model**（`openvla-7b`）在 LIBERO Object 上的相同 pipeline，才能完成 3×4 矩阵中 Object cell 的 trained vs untrained 对比。

---
