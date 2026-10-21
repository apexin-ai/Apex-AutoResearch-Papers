# analysis deep error prep

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_deep_error_prep_20260518T140405_result.json`
- **Structured JSON:** [`2cd59637e689624978c1.json`](../../sessions/2c/2cd59637e689624978c1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据收集完毕。以下是完整的 survey 和分析框架。

---

## 1. 可用 Eval 预测数据清单

### 有 predictions.json（可做 error analysis）— 27 个目录

**核心多尺度对比组（dev split, 985 docs, 含 gold_triples）：**

| 条件 | Qwen3-1.7B | Qwen3-8B | Llama-3.1-8B |
|------|-----------|----------|-------------|
| **SFT** | `qwen3_1_7b_sft_eval` (F1=.495) | `qwen3_8b_sft_eval` (F1=.526) | `llama_3_1_8b_sft_eval` (F1=.551) |
| **No-Evidence** | `qwen3_1_7b_no_evidence_eval_v3` (F1=.410) | `qwen3_8b_no_evidence_eval_v2` (F1=.528) | `llama_3_1_8b_no_evidence_eval` (F1=.562) |
| **RSFT** | `plan_006_qwen3_1_7b_rsft_eval_r2` (F1=.522) | `plan_006_qwen3_8b_rsft_eval` (F1=.561) | `plan_006_llama_rsft_r3_eval` (F1=.567) |
| **d102 (k=1)** | `d102_1_7b_k1_s42` (F1=.529) | `d102_8b_k1_s42` (F1=.555) | `d102_llama_k1_s42` (F1=.584) |

**补充 seed / 其他：**
- `d102_8b_k1_s43`, `plan_006_llama_rsft_seed43_eval_r2`, `plan_006_qwen3_1_7b_rsft_seed43_eval`
- `rsft_s43_dev_eval_preds` (Qwen3-4B RSFT 旧版)
- `plan_014_no_evidence_eval_d076` (4B no-evidence)
- test split: `plan_006_*_test` × 3, `plan_002_test_rsft_s43/s44`, `test_rsft_ced_s44`（无 gold metrics，需提交 CodaLab）
- Re-DocRED: `plan_007_redocred_*` × 3

### 只有 metrics.json（无 predictions，不可做详细 error analysis）— 30 个目录
包括旧的 4B 实验（rsft_r1/r2a/r2b/s42-45, rsft_flat_nli_*, sft_baseline_*, GRPO/DPO 系列）

---

## 2. 现有分析代码

| 文件 | 功能 |
|------|------|
| `eval/evaluator.py` | F1, Ign-F1, Evi-F1, EDCR 计算 |
| `scripts/edcr_diagnostic.py` (346 行) | 跨方法 EDCR 诊断，按 relation type 分解，含 Spearman 相关性分析 |
| `eval/cross_method_table.py` | 跨方法对比表 |
| `eval/post_hoc_retrieval.py` | BM25 post-hoc evidence retrieval baseline |

已有产出：`edcr_diagnostic_table.md`（13 方法对比）、`edcr_per_relation_analysis.md`（93 个 relation）、`qualitative_case_study.json`（SFT vs RSFT case study）

**不存在** error_analysis 专用脚本。

---

## 3. 分析框架建议

### A. False Positive 分类（预测了但 gold 没有）

| 类别 | 定义 | 检测方式 |
|------|------|---------|
| **幻觉关系 (Hallucinated Relation)** | 预测的 (h,t) 对在 gold 中无任何关系 | pred (h,t) pair 不存在于 gold |
| **关系混淆 (Relation Confusion)** | (h,t) 对在 gold 中有关系，但预测了错误的 relation type | pred (h,t) ∈ gold 但 relation 不匹配 |
| **实体混淆 (Entity Confusion)** | 预测的 head/tail 实体与 gold 接近但不完全匹配（别名、部分匹配） | fuzzy match pred 的 h/t 与 gold 实体 |
| **重复预测 (Duplicate)** | 同一三元组被预测多次 | 去重后计数 |

### B. False Negative 分类（gold 有但没预测）

| 类别 | 定义 | 检测方式 |
|------|------|---------|
| **跨句关系遗漏 (Cross-sentence Miss)** | gold evidence 跨 ≥2 句，模型未预测 | gold evidence span > 1 sentence |
| **稀有关系遗漏 (Rare Relation Miss)** | gold relation 在训练集中频率低（bottom 25%） | 按 relation frequency 分组 |
| **截断丢失 (Truncation Loss)** | 模型输出被截断（`truncated=True`），导致后面的 triple 丢失 | `truncated` 字段 + 位置分析 |
| **实体不识别 (Entity Miss)** | gold triple 的 h 或 t 完全没出现在任何预测中 | entity coverage 统计 |

### C. Evidence Error 分类（triple 匹配但 evidence 错误）

| 类别 | 定义 |
|------|------|
| **证据过泛 (Over-citation)** | pred evidence ⊃ gold evidence（引用了多余句子）|
| **证据偏移 (Evidence Shift)** | pred evidence ∩ gold evidence = ∅（完全引错句子）|
| **证据不全 (Under-citation)** | pred evidence ⊂ gold evidence（漏了部分 gold 句子）|

### D. 对比维度

1. **SFT → RSFT error pattern 变化**：相同模型、相同尺度，RSFT 修正了哪类 FP/FN
2. **尺度对比**：1.7B vs 8B 的 error 分布差异（小模型是否更容易幻觉？）
3. **架构对比**：Qwen3 vs Llama-3.1（同为 8B 时 error pattern 差异）
4. **d102 vs RSFT**：不同 rejection sampling 策略的 error 差异
5. **Per-relation breakdown**：哪些 relation type 最受益于 RSFT

---

## 4. 推荐分析优先级

**P0（论文核心分析贡献）：**
1. 3 个尺度 × {SFT, RSFT} 的 FP/FN 分类对比（6 个 dev 预测文件）
2. Evidence error 分类 × {SFT, RSFT}（EDCR 改善的来源）
3. Per-relation RSFT gain breakdown（已有 edcr_per_relation_analysis 可扩展）

**P1（增强说服力）：**
4. Truncation 影响量化（1.7B 截断率 vs 8B）
5. Cross-sentence vs single-sentence relation 的 F1 差异
6. d102 vs RSFT error pattern 对比

**P2（可选深入）：**
7. Qualitative case study 扩展（已有 3 case，需要更多对比类别）
8. No-evidence baseline 的 FP 分析（验证 evidence 训练是否引入特定 error）

**数据充足度**：P0 和 P1 所有分析都可用现有 dev predictions.json 完成，无需重新推理。需要写一个统一的 `error_analysis.py` 脚本，输入多个 predictions.json，输出分类统计 + LaTeX 表格。

---
