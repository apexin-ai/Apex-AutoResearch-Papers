# Wang et al. 竞品分析报告

## 论文基本信息

- **标题**: A Systematic Analysis of Hybrid Linear Attention
- **arXiv**: 2507.06457 (2025-07-08)
- **作者**: Dustin Wang, Rui-Jie Zhu, Steven Abreu, Yong Shan, Taylor Kergan, Yuqi Pan, Yuhong Chou, Zheng Li, Ge Zhang, Wenhao Huang, Jason Eshraghian
- **机构**: UC Santa Cruz, ByteDance, University of Groningen, CASIA, PolyU, M-A-P
- **规模**: 72 个模型 (36×340M/20B tokens + 36×1.3B/100B tokens)，训练数据 FineWeb-Edu
- **开源**: HuggingFace 集合 m-a-p/hybrid-linear-attention-research

---

## 问题 a: 是否已报告完整 architecture × ratio × benchmark 交叉数据？

**没有。** 他们的报告方式是聚合的：

| 表格 | 内容 | 粒度 |
|------|------|------|
| Table 2 (340M) | 每架构最优 ratio + 6 个 LM benchmark 的分数 | arch × benchmark（仅最优 ratio） |
| Table 3 (1.3B) | 同上 | arch × benchmark（仅最优 ratio） |
| Table 4 | LM 聚合分数 | arch × ratio（平均分，无逐 benchmark 拆分） |
| Table 5 | Recall 聚合分数 | arch × ratio（RULER 平均分） |
| Table 6 | RULER 子任务拆分 | 仅 select models |

**关键缺失**：不存在 "GatedDeltaNet 在 6:1 ratio 下 LAMBADA 得分" 这样的完整交叉表格。LM 性能只在 "最优 ratio" 下拆分到各 benchmark，其余 ratio 只报告聚合平均值。

**他们的结论**：
- LM 性能跨 ratio 基本稳定（~0.55-0.57 平均），ratio 选择对 LM 影响不大
- Recall 性能随 full attention 比例增加而显著改善，尤其 3:1 以下
- 推荐 HGRN-2 或 GatedDeltaNet，ratio 3:1 到 6:1

---

## 问题 b: 是否发现 architecture-dependent hybridization effects？

**是的，这是他们的核心发现之一。** 具体：

1. **GatedDeltaNet**: standalone 最强（340M），但 hybridized 后优势缩小甚至消失
2. **HGRN-2**: standalone 不突出，但在 6:1 hybrid 下超越所有架构（含 Transformer），成为最佳选择
3. **RetNet**: fixed decay 导致 recall 能力极差，hybridization 帮助有限
4. **GLA**: 中等表现，3:1 时 recall 改善明显但 LM 性能无优势

他们明确指出 "standalone scores are unreliable predictors of hybrid performance"，并分析了 selective gating 和 hierarchical recurrence 作为有利于 hybridization 的机制。

**但他们的分析维度是 "哪个架构 hybrid 后最好"，不是 "不同架构在不同任务类型上的退化模式是否不同"。**

---

## 问题 c: 论文 focus

他们的论文是一篇 **系统性 benchmark 研究**，focus 是：

1. **主要目标**: 为从业者提供 hybrid linear attention 的架构选择指南
2. **核心问题**: 哪种 linear attention + 什么比例的 full attention = 最佳性价比
3. **分析框架**: 按 "generation"（vector state → fixed decay → data-dependent gate → delta rule）分类，解释机制差异
4. **不涉及**: 训练方法创新、fine-tuning、task-specific 退化分析、composition depth 理论

本质上是 "practitioner's guide to hybrid architecture selection"。

---

## 问题 d: 训练设置

| 项目 | 详情 |
|------|------|
| 数据 | FineWeb-Edu |
| 模型规模 | 340M (20B tokens) + 1.3B (100B tokens) |
| 架构数 | 6 核心 + DeltaNet（实际 7 个架构） |
| 比例 | pure, 24:1, 12:1, 6:1, 3:1 |
| 总模型数 | 72 |
| 变量控制 | 同数据、同 tokenizer、同训练框架 (fla + flame)、同超参（推测） |
| Benchmark | LM: ARC-c/e, HellaSwag, LAMBADA, OBQA, PIQA; Recall: RULER |
| 不含 | **MMLU, WinoGrande, BLiMP** |

---

## 我们数据的新颖性判断

### 与 Wang et al. 的重叠

| 维度 | Wang et al. | 我们 | 重叠度 |
|------|-------------|------|--------|
| 模型来源 | 同一批 m-a-p 模型 | 同一批 | 完全重叠 |
| 架构 | 7 个（含 HGRN, Hawk, GLA） | 3 个（GDN, RetNet, HGRN2） | 子集 |
| 比例 | pure, 24:1, 12:1, 6:1, 3:1 | 同 | 完全重叠 |
| LM Benchmark | ARC-c/e, HellaSwag, LAMBADA, OBQA, PIQA | LAMBADA, HellaSwag, ARC, **MMLU, WinoGrande, BLiMP** | 部分重叠 |
| 分析角度 | 架构选型指南（哪个最好） | **composition depth × architecture 交互效应** | 不重叠 |

### 新颖性评估

**数据层面**：中等新颖性
- Wang et al. 不含 MMLU/WinoGrande/BLiMP，我们有
- Wang et al. 不报告完整 arch × ratio × benchmark 交叉数据（只报聚合），如果我们报告完整交叉表，有增量
- 但原始 benchmark 跑分本身附加价值有限，因为任何人都可以复现

**分析层面**：高新颖性（核心差异化）
- Wang et al. 的问题是 "which hybrid is best"（横向比较）
- 我们的问题是 "why do different architectures degrade differently across task types"（机制解释）
- composition depth 假设、task-agnostic 假设、functional segregation 假设的三假设对比框架完全不在 Wang et al. 的讨论范围内
- 他们观察到 "architecture-dependent hybridization effects" 但没有用 task complexity/composition depth 维度去解释这些差异

### 结论

**Wang et al. 提供了我们需要的基础设施（模型 + 初步 benchmark），但没有回答我们要问的问题。** 我们的增量价值不在于 "跑更多 benchmark"，而在于：

1. **理论框架**: 用 composition depth 理论解释 architecture-ratio-task 三维交互
2. **新 benchmark 维度**: MMLU/WinoGrande/BLiMP 提供更宽的 task complexity 光谱
3. **分析深度**: 完整交叉数据 + 统计检验（Spearman ρ, permutation test），而非 "best ratio" 推荐

**风险**: 如果我们的 composition depth 假设最终不成立（H_agnostic 胜出），那论文价值会大幅缩水，因为纯 benchmark 数据与 Wang et al. 高度重叠。
