# diagnose 8b rsft k1 metrics

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_8b-rsft-k1-metrics_20260522T224050_result.json`
- **Structured JSON:** [`3818a93ae67cac5a0e51.json`](../../sessions/38/3818a93ae67cac5a0e51.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Test eval 没有 metrics.json，但日志已包含所有信息。结果如下：

---

## seed 42 (d102_8b_k1_s42) — Dev
路径: `/root/autodl-tmp/eval_results/d102_8b_k1_s42/metrics.json`
model_path: `/root/autodl-tmp/rsft_output_qwen3_8b_k1`

| 指标 | 值 |
|------|-----|
| ign_f1 | 0.5376 |
| f1 | 0.5549 |
| evi_f1 | 0.8136 |
| evi_f1_joint | 0.4401 |
| edcr | 0.6231 |
| precision | 0.5529 |
| recall | 0.5569 |
| ign_precision | 0.5275 |
| ign_recall | 0.5482 |
| field_compliance_rate | 0.7492 |
| n_truncated | 242 |

## seed 43 (d102_8b_k1_s43) — Dev
路径: `/root/autodl-tmp/eval_results/d102_8b_k1_s43/metrics.json`
model_path: `/root/autodl-tmp/rsft_output_qwen3_8b_k1_s43`

| 指标 | 值 |
|------|-----|
| ign_f1 | 0.5471 |
| f1 | 0.5651 |
| evi_f1 | 0.8180 |
| evi_f1_joint | 0.4544 |
| edcr | 0.6094 |
| precision | 0.5640 |
| recall | 0.5663 |
| ign_precision | 0.5385 |
| ign_recall | 0.5560 |
| field_compliance_rate | 0.7533 |
| n_truncated | 231 |

## seed 44 (rsft_8b_k1_s44_eval) — Dev
路径: `/root/autodl-tmp/eval_results/rsft_8b_k1_s44_eval/metrics.json`
model_path: `/root/autodl-tmp/rsft_output_qwen3_8b_k1_s44`

| 指标 | 值 |
|------|-----|
| ign_f1 | 0.5451 |
| f1 | 0.5620 |
| evi_f1 | 0.8145 |
| evi_f1_joint | 0.4472 |
| edcr | 0.6233 |
| precision | 0.5607 |
| recall | 0.5632 |
| ign_precision | 0.5360 |
| ign_recall | 0.5545 |
| field_compliance_rate | 0.7614 |
| n_truncated | 230 |

## 3-seed 汇总

| 指标 | s42 | s43 | s44 | mean | std |
|------|-----|-----|-----|------|-----|
| ign_f1 | 0.5376 | 0.5471 | 0.5451 | 0.5433 | 0.0050 |
| f1 | 0.5549 | 0.5651 | 0.5620 | 0.5607 | 0.0052 |
| evi_f1_joint | 0.4401 | 0.4544 | 0.4472 | 0.4472 | 0.0072 |
| edcr | 0.6231 | 0.6094 | 0.6233 | 0.6186 | 0.0080 |

## test_eval_8b_rsft_s42 模型确认
日志路径: `~/runs/faith-evidence-ie/test_eval_8b_rsft_s42.log`
adapter: `/root/autodl-tmp/rsft_output_qwen3_8b_k1`
base: `/root/autodl-tmp/models/Qwen/Qwen3-8B`
sft_adapter: `/root/autodl-tmp/sft_output_qwen3_8b_bf16`
**结论: k=1 模型（正确），不是 k=3**

Test 结果: F1=0.3353, Evi-F1(DREEAM)=0.2526, EDCR=0.7993

## test_eval_8b_rsft_s42_no_evi 模型确认
日志路径: `~/runs/faith-evidence-ie/test_eval_8b_rsft_s42_no_evi.log`
adapter: `/root/autodl-tmp/rsft_output_qwen3_8b_k1`（同一模型）
**结论: k=1 模型（正确）**

Test 结果: F1=0.3319, Evi-F1(DREEAM)=0.0707, EDCR=0.7424

---
