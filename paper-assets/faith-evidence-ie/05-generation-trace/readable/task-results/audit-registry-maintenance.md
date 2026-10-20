# audit registry maintenance

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_registry-maintenance_20260524T053309_result.json`
- **Structured JSON:** [`6bb78bfc56ba6b16185e.json`](../../sessions/6b/6bb78bfc56ba6b16185e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部 registry 更新完成。汇总结果：

---

## 汇总

### 1. d102 k=1 eval 注册

| exp_id | ign_f1 | rel_f1 | evi_f1 | edcr | 操作 |
|--------|--------|--------|--------|------|------|
| d102_1_7b_rsft_k1_s42 | 0.5122 | 0.5290 | 0.8243 | 0.6224 | 补录 eval metrics ✓ |
| d102_8b_rsft_k1_s42 | 0.5376 | 0.5549 | 0.8136 | 0.6231 | 补录 eval metrics ✓ |
| d102_8b_rsft_k1_s43 | 0.5471 | 0.5651 | 0.8180 | 0.6094 | 已有，无需更新 |
| d102_llama_rsft_k1_s42 | 0.5714 | 0.5839 | 0.8238 | 0.5799 | 补录 eval metrics ✓ |
| seed_llama_rsft_k1_s43_eval | 0.5662 | 0.5780 | 0.8287 | 0.5783 | 补录 eval metrics ✓ |

### 2. plan_006 SUPERSEDED 标记

| exp_id | 旧 ign_f1 (k=3) | 替代 entry |
|--------|-----------------|------------|
| plan_006_qwen3_1_7b_rsft_eval_r2 | 0.505 | d102_1_7b_rsft_k1_s42 |
| plan_006_llama_rsft_r3_eval | 0.5563 | d102_llama_rsft_k1_s42 |
| plan_006_qwen3_8b_rsft_eval | 0.5433 | d102_8b_rsft_k1_s42 |
| plan_006_qwen3_1_7b_rsft_seed43_eval | 0.5024 | d102 k=1 series |
| plan_006_llama_rsft_seed43_eval_r2 | 0.5619 | seed_llama_rsft_k1_s43_eval |

conclusion 字段不支持 "superseded"（仅 failed/killed/negative/success），已通过 notes 前缀 `[SUPERSEDED]` 标记。

### 3. DPO 3ep Rel-F1

- 源文件：`/root/autodl-tmp/eval_results/dpo_rebuilt_3ep_eval/metrics.json`
- **rel_f1 = 0.3145**（f1 字段），ign_f1 = 0.3076
- Registry 已有 `rel_f1: 0.3145`，与论文 31.45% 完全一致，无需补录

### 4. 8B RSFT Evi-F1

| seed | 来源 | evi_f1 |
|------|------|--------|
| s42 | d102_8b_k1_s42 | 0.8136 |
| s43 | d102_8b_k1_s43 | 0.8180 |
| s44 | rsft_8b_k1_s44_eval | 0.8145 |
| **3-seed mean** | | **0.8154 (81.54%)** |

**论文值 81.54% 完全匹配 d102 k=1 三种子均值。** 旧 registry 的 81.16% 来自 plan_006 k=3 值（plan_006_qwen3_8b_rsft_eval evi_f1=0.8052 等），已被 d102 k=1 取代。差异来源：k=3 → k=1 方法修正。

---
