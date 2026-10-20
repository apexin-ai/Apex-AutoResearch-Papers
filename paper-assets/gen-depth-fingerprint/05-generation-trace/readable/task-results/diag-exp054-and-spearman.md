# diag exp054 and spearman

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_exp054-and-spearman_20260518T114600_result.json`
- **Structured JSON:** [`85750a61c32cebe7e32d.json`](../../sessions/85/85750a61c32cebe7e32d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All data collected. Here's the complete report.

---

## 问题 1: exp_054 Instruct Llama 评估详情

### 1. 完整结果（`exp054_instruct_llama_eval.json`）

| 模型 | 样本数 | Binary F1 | 95% CI | 3-class F1 | 95% CI |
|------|--------|-----------|--------|------------|--------|
| Llama-3.2-3B-Instruct | 4974 | 0.8381 | [0.8281, 0.8472] | 0.5437 | [0.5299, 0.5581] |
| Llama-3.2-3B-Base | 4680 | 0.8488 | [0.8389, 0.8590] | 0.7424 | [0.7279, 0.7553] |
| **Delta** | | **−0.0107** | | **−0.1987** | |

### 2. 评估类型：**Within-model 5-fold Stratified CV**，不是 LOGO

脚本 `eval_exp054_instruct_llama.py` 第 29-35 行明确使用 `StratifiedKFold(n_splits=5)`，训练和测试都在同一模型数据上。

### 3. 分类方案：两种

- **Binary**: gen-1 vs gen-2+（排除 gen-0）
- **3-class**: gen-0 / gen-1 / gen-2+

### 4. 训练数据来源

- Instruct: `data/features_llama-3.2-3b-instruct.csv`（单独的 instruct 特征文件）
- Base: 从 `data/features_8gen.csv` 中提取 `model_name == "llama-3.2-3b"` 的子集
- 两者各自独立做 within-model CV，**不混合训练**

### 5. 关键判断：0.838 与论文 claim 不矛盾

**Within-model CV 的 binary F1 高不代表信号没被削弱。** 真正揭示问题的证据：

| 指标 | Instruct | Base | 含义 |
|------|----------|------|------|
| entropy_mean ρ | **+0.2299** | **−0.6270** | 方向完全翻转 |
| entropy_std ρ | +0.2623 | −0.1597 | 方向翻转 |
| ttr ρ | −0.1411 | −0.6856 | 强度大幅衰减 |
| hapax_ratio ρ | −0.1157 | −0.6975 | 强度大幅衰减 |
| 3-class F1 | 0.5437 | 0.7424 | **下降 20pp** |
| Direction reversals | | | **3/7 特征方向翻转** |

Within-model CV binary F1 相近（0.838 vs 0.849）只说明分类器能拟合每个模型内部的某些模式，但：
- Spearman 方向翻转说明特征与深度的关系在 instruct 模型上本质不同
- 3-class F1 大幅下降说明细粒度深度判别力丧失
- **LOGO 评估才是检验信号泛化性的正确实验**（`temp_curve_binary_logo.json` 中有 LOGO 数据，但那个实验是 cross-generator 的，不直接包含 instruct 模型）

**结论**：0.838 是 within-model CV，不是 LOGO，与 "instruction tuning weakens the signal" 完全不矛盾。

---

## 问题 2: Qwen t=0.9 Spearman ρ 来源

### 搜索结果

所有 `results/*.json` 中均无 Qwen t=0.9 的预计算 Spearman 值。`temp_curve_binary_logo.json` 只有 binary F1，无 Spearman。

### 实际计算验证

从 `data/features_qwen3-1.7b-t09.csv`（4558 条记录）直接计算：

| 特征 | Qwen3-1.7B t=0.9 ρ | Pythia-2.8B t=0.9 ρ |
|------|---------------------|---------------------|
| **entropy_mean** | **−0.3739** | **−0.2947** |
| entropy_std | −0.0443 | +0.1098 |
| entropy_min | −0.2119 | −0.2056 |
| entropy_max | +0.0888 | −0.0683 |
| tail_decay | −0.0862 | +0.1373 |
| ttr | −0.5141 | −0.3700 |
| hapax_ratio | −0.5352 | −0.4034 |

**论文 appendix_classifier.tex 第 53 行声称 Qwen3-1.7B t=0.9 entropy_mean ρ = −0.37 → 实际值 −0.3739，四舍五入正确 ✓**

Pythia-2.8B t=0.9 entropy_mean ρ = −0.2947 → 论文写 −0.30，四舍五入正确 ✓

### 数据来源

该值没有被保存到任何 results JSON 中，是从原始特征 CSV 直接计算得到的。建议将 t=0.9 的 Spearman 结果也持久化到一个 results 文件中以保持可追溯性。

---
