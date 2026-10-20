# audit trace 1 7b rsft s42

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_trace-1_7b-rsft-s42_20260524T053119_result.json`
- **Structured JSON:** [`c6e9706219d43f9ea66c.json`](../../sessions/c6/c6e9706219d43f9ea66c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据收集完毕。以下是完整结果。

---

## 所有 1.7B RSFT s42 Eval 结果

| 文件路径 | ign_f1 | f1 | evi_f1 | max_new_tokens | checkpoint | split | 修改时间 |
|----------|--------|-----|--------|----------------|------------|-------|----------|
| `eval_results/d102_1_7b_k1_s42/` | **51.22** | 52.90 | 82.43 | 1024 | `rsft_output_qwen3_1_7b_k1/checkpoint-567` (k=1 CED) | dev | May 18 18:14 |
| `eval_results/plan_006_qwen3_1_7b_rsft_eval_r2/` | **50.50** | 52.19 | 83.09 | 1024 | `rsft_output_qwen3_1_7b/checkpoint-1698` (k=3 CED) | dev | May 17 19:16 |
| `eval_results/test_eval_1_7b_rsft_s42/` | 29.33 | 29.33 | 23.20 | 2048 | `rsft_output_qwen3_1_7b_k1` | test | May 21 |
| `eval_results/test_eval_1_7b_rsft_s42_no_evi/` | 23.90 | 23.90 | — | 2048 | `rsft_output_qwen3_1_7b_k1` | test (no-evi) | May 22 |

对照 seeds（s43/s44，均为 k=1 CED dev eval）：
- s43 (`rsft_1_7b_s43_r2_eval`): ign_f1 = **51.09**
- s44 (`rsft_1_7b_s44_r2_eval`): ign_f1 = **51.25**

---

## 结论

**Registry 50.50** = `plan_006_qwen3_1_7b_rsft_eval_r2`
- checkpoint: `rsft_output_qwen3_1_7b/checkpoint-1698`（**旧 k=3 CED**，9042 训练样本）
- 精确值: ign_f1 = 0.504952

**Paper 51.23** = `d102_1_7b_k1_s42`
- checkpoint: `rsft_output_qwen3_1_7b_k1/checkpoint-567`（**新 k=1 CED**，3021 训练样本）
- 精确值: ign_f1 = 0.512172 → **51.22**（paper 写成 51.23 有 0.01pp 四舍五入偏差）

**根因：两个 eval 使用了不同的 RSFT checkpoint。** D102 是方法论修正后的 k=1 CED 版本（与论文声明和 4B canonical 一致），plan_006 是修正前的 k=3 CED。Registry 未更新为 d102 的值。

第一版 audit (`final_audit_w2_tables.md:61`) 已验证 paper 用 d102 值计算 3-seed mean = (51.22 + 51.09 + 51.25)/3 = 51.19±0.09 ✅。

---
