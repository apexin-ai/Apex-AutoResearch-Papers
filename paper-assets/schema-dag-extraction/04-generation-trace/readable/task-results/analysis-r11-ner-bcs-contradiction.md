# analysis r11 ner bcs contradiction

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_r11-ner-bcs-contradiction_20260517T095903_result.json`
- **Structured JSON:** [`b61c03f98629daa3e3df.json`](../../sessions/b6/b61c03f98629daa3e3df.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。以下是完整汇报：

---

## 调查结论：NER BCS-F1 r=+0.50/+0.58 vs Q1 null

### 1. +0.50/+0.58 的确切来源

| 属性 | 值 |
|------|------|
| 文件 | `artifacts/eval_exp2.json` + `scripts/d037/d037_ner_v2_bcs_analysis_results.json` |
| v1 r=0.50 | D005 决策记录（原始数据已被 v2 覆盖），n=27, count_12 |
| v2 r=0.58 | `eval_exp2.json` 直接验证, n=27 (25 random + 2 extreme), count_12 |
| BCS 定义 | **MAX pairwise cosine similarity（旧定义）** |
| BCS range | [0.892, 0.973] (MAX) / [0.779, 0.833] (MEAN 重算) |
| Batch seed | seed 42+12=54（`run_experiment.py` 的 `seed + count` 逻辑） |
| Sim matrix | `artifacts/sim_matrix.pt`（66×66, Qwen3 embeddings） |

### 2. Q1 null 的确切来源

| 属性 | 值 |
|------|------|
| 文件 | `artifacts/d051_fewnerd_n25_s{42,123,456}/eval_results.json` |
| 结果 | `artifacts/paper/ner_partial_correlation_results.json`: r=0.0037, p=0.937 |
| n_batches | 75 (25 per seed × 3 seeds, count_12 only) / 450 (all counts) |
| BCS 定义 | **MEAN pairwise cosine similarity（新定义）** |
| BCS range | [0.763, 0.848] |
| Seeds | 42, 123, 456 |
| Sim matrix | 同一个 `artifacts/sim_matrix.pt` |

### 3. d051 count_12 per-seed BCS-F1 相关系数

| Seed | n | r(BCS, F1) | p | r(BCS, freq) |
|------|---|-----------|---|-------------|
| s42 | 25 | +0.189 | 0.365 | +0.219 |
| s123 | 25 | +0.021 | 0.921 | +0.132 |
| s456 | 25 | -0.165 | 0.432 | +0.217 |
| **Pooled** | **75** | **+0.003** | **0.982** | **+0.173 (NS)** |

### 4. 矛盾根因

**主因：eval_exp2 的 batch composition 恰好产生了 BCS-frequency 的虚假关联**

| 对比维度 | eval_exp2 (27 batches) | d051 (75 batches) |
|----------|----------------------|------------------|
| r(BCS, freq) | **0.53** (强关联!) | 0.17 (NS) |
| r(F1, freq) | 0.59 | 0.59 |
| r(BCS, F1) raw | 0.50-0.58 | 0.003 |
| Partial r(BCS, F1 \| freq) | **0.28 (p=0.16, NS)** | -0.12 (p=0.29, NS) |

**因果链**：eval_exp2 的特定 25 个 random batches（seed=54）**恰好**产生了 BCS↔type_frequency 的相关（r=0.53）。由于 type frequency 是 F1 的真实预测因子（高频类型模型识别更好），这制造了虚假路径：BCS → freq → F1。

控制 frequency 后，**两组数据的 partial r 都不显著**。eval_exp2 的 r=+0.50/+0.58 完全是 **confound-driven spurious correlation**。

**次因**：
- BCS 定义差异（MAX vs MEAN）不是主因 — BCS_MEAN 重算后 eval_exp2 仍 r=0.50
- 零 batch 重叠（不同 seed）
- 小样本 n=27 放大了随机偏差

### 5. 建议

1. **不应在论文中报告 r=+0.50/+0.58** — 这是受 type frequency confound 污染的虚假结果
2. **使用 d051 的结论**（r≈0.00, NS）作为 NER batch-level BCS-F1 的最终结果
3. 如果论文 §4.5 已写入这些数字，需要替换为 d051 结果，并可简要说明 frequency confound 的存在（作为 methodological insight）
4. 关键教训：25-27 个 random batches 不足以产生可靠的相关性估计 — 特别是在高维 type space 中容易出现 spurious confounds

---
