# ops check sft predictions and edcr

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check_sft_predictions_and_edcr_20260517T184013_result.json`
- **Structured JSON:** [`0947f078163462151fd7.json`](../../sessions/09/0947f078163462151fd7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇报

### 1. 1.7B SFT dev — **Y，数据存在**
路径: `/root/autodl-tmp/eval_results/qwen3_1_7b_sft_eval/metrics.json`

| 指标 | 值 |
|---|---|
| evi_f1 (TP-only) | 83.16 |
| evi_f1_joint (DREEAM) | 39.58 |
| EDCR | 67.04 |
| RE F1 | 49.45 |
| RE ign_F1 | 47.86 |

### 2. 8B SFT dev — **Y，数据存在**
路径: `/root/autodl-tmp/eval_results/qwen3_8b_sft_eval/metrics.json`

| 指标 | 值 |
|---|---|
| evi_f1 (TP-only) | 81.88 |
| evi_f1_joint (DREEAM) | 41.39 |
| EDCR | 65.10 |
| RE F1 | 52.62 |
| RE ign_F1 | 50.51 |

### 3. 1.7B RSFT (seed 42) dev — **Y，数据存在**
路径: `/root/autodl-tmp/eval_results/plan_006_qwen3_1_7b_rsft_eval_r2/metrics.json`

| 指标 | 值 |
|---|---|
| evi_f1 (TP-only) | 83.09 |
| evi_f1_joint (DREEAM) | 42.23 |
| EDCR | 62.97 |
| RE F1 | 52.19 |
| RE ign_F1 | 50.50 |

注: Registry 查询 `plan_006_qwen3_1_7b_rsft_eval_r2` 返回 0 条结果（可能 exp_id 不完全匹配），但磁盘上数据完整。

### 4. 额外：No-evidence SFT baseline
也已存在，但 evidence 指标均为 0（`no_evidence=true`，符合预期）：
- 1.7B no-evidence (v3): RE F1 = 41.03
- 8B no-evidence (v2): RE F1 = 52.83

**结论：Table 3 所需的 3 项数据全部已存在，无需重跑。**

---
