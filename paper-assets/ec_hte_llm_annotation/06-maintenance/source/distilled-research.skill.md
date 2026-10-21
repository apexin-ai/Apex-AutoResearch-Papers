---
name: LLM Annotation Debiasing for Causal Inference — Research Patterns
description: 从25篇论文蒸馏的研究共识：方法族谱、baseline/metric/dataset惯例、实验设计模式、竞品定位、研究空白
type: research
domain: ec_hte_llm_annotation
source_papers: 25
distill_date: 2026-05-21
---

## 方法族谱

**PPI 家族**（6/25）是主流。PPI（Science'23）→ CrossPPI 去 data splitting（PNAS'24）→ ActiveInf 省>80%标注（ICML'24）→ PPCI 条件推断（arXiv'26）→ PDI 多群体推断（arXiv'26）。PPI ≡ survey sampling 差分估计量（Mozer'26）。**6/25，高。**

**DSL**（2/25）用 doubly-robust pseudo-outcome + IPW。sRMSE 比 PPI 低15-30%但对共线性敏感（Audinet, EMNLP'25）。**2/25，高。**

**测量误差校正**（6/25）提供理论基础。ForestIV 用 RF tree 去相关性做 IV（Bu'23）；经典框架（Fuller'87, Carroll'06）；非经典误差（Hu'08）。**6/25，高。**

## Baseline / Metric / Dataset 共识

**标准 baseline 组合：**(1) Classical labeled-only (2) Naive LLM imputation (3) PPI (4) DSL。至少需 classical + 一种 debiased 方法。**支持度5/8精读，高。**

**核心 metric：**95% CI 覆盖率（6/25）是有效性金标准；CI 宽度（3/25）衡量效率；sRMSE/bias（2/25）做有限样本比较。**支持度6/25，高。**

**数据集模式：**需3+领域。常用：US Census、政治调查、CSS benchmarks（sentiment/hate/ideology）。实际 LLM 标注（非合成噪声）日益成为要求。**支持度5/8精读，高。**

## 实验设计模式

**主 x 轴：**标注样本量 n——所有 PPI/DSL 论文都以此为变量。**6/8精读，高。**

**辅助变量：**无标签总量 N、LLM/模型类型、surrogate 质量。**4/8，高。**

**最低标注量：**~200 个 expert 标注即可有效去偏（sRMSE<0.2）。**2/8，中。**

**LLM 选择：**测 3+ LLM，覆盖 API（GPT-4/Claude）和开源（Llama）。含非LLM baseline（如 BERT+LR）加分。**3/8，中。**

## 竞品定位

**直接竞品：**PPCI（Sui'26）将 PPI 扩展到条件推断——最接近我们的 HTE 目标，但缺少测量误差框架且不处理 treatment effect。

**我们填补的空白：**
1. 无论文同时做 PPI/DSL 去偏 + HTE 估计（PPI 做边际参数；HTE 假设 clean labels）
2. 标注质量模型（Dawid-Skene/MACE）与 PPI/DSL 框架脱节——桥接可改善误差建模
3. 面向 HTE（非均值）的标注预算分配策略未被探索
4. LLM 标注偏差已被证实（Ashwin'25：系数反转），但未在因果推断场景中系统校正

## 共同局限（跨论文）

- 仅渐近保证，有限样本表现因场景而异（5/8）
- 假设 expert 标注 = ground truth（3/8）
- 限于分类/二元结果（3/8）
- 需要合理准确的 ML 预测器（3/8）
