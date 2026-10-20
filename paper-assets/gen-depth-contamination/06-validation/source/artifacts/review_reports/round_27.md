---
round: 27
review_mode: fresh
overall_score: 3.5
timestamp: 2026-05-23T01:50:19.252343+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# Round 27 审稿报告 — Generational Depth Estimation of Recursive Synthetic Text

**Venue**: EMNLP 2026 (ARR May 2026)
**Reviewers**: R1 (方法严谨性+实验设计+统计有效性), R2 (新颖性+相关工作+写作呈现)
**交叉回应**: 已完成（R1↔R2 全部逐条 AGREE/REBUT）

---

## Summary

本文提出 generational depth estimation 任务，通过 15 个统计特征和 OBD-LightGBM 分类器测量递归合成文本的最大可判别深度 K*_empirical。在 10 个模型配置（6 架构族，1B-8B）、3 个领域、4 种解码策略上实验，发现 web text K*_empirical ≤ 2，arXiv K*_empirical = 3。跨模型迁移保留 80-92% 准确率，特征排序跨 scorer 稳定（ρ > 0.90）。K*-guided filtering 一致性验证显示 binary filtering 最有效地最小化下游任务退化。

---

## Strengths

**S1** [共识] **问题定义新颖且有意义**：在 binary detection 和 model collapse 之间定义了"生成深度辨别边界"这一新维度。K*_empirical 操作性定义（Eq. 1）清晰可执行，可直接指导数据管道决策。

**S2** [共识] **实验覆盖系统全面**：10 个模型配置 × 6 深度级别 × 5,000 样本/级别，配合 3 域、4 种解码策略消融。三路 ANOVA 将 Generator/Scorer/Depth-Pair 效应分解，方法论成熟。

**S3** [共识] **统计实践规范**：Bootstrap 95% CI（1,000 resamples）+ 10,000-iteration permutation test + Bonferroni correction for 10 comparisons + seed robustness 验证，在 NLP 实证研究中属上乘水平。

**S4** [共识] **跨模型迁移有说服力**：Continuation-mode 80-92% accuracy retention，0v1 cross-model AUC > 0.96，scorer-invariant feature rankings（ρ > 0.90），支持 K*_empirical 反映递归生成的内在统计属性而非模型特异性伪影。

**S5** [R1] **阈值敏感性和鲁棒性分析**：Figure 3 提供 θ ∈ [0.55, 0.70] 的连续 sensitivity surface，seed robustness 分析（Table 26）有效缓解阈值选择和随机性担忧。

---

## Weaknesses

### Must-Fix（影响接收决定）

**MF-1** [critical, 共识] **普适性声明超出实验覆盖范围**

- Qwen 占 10 配置中的 4 个，且全部为 K\*=2。非 Qwen 的 6 个配置中仅 Pythia-1.4B（边界值 AUC=0.593）和 LLaMA-3.1-8B 达到 K\*=2，其余 4 个（Pythia-6.9B, OLMo-1B, Mistral-7B, Gemma-2-2B）均为 K\*=1
- Abstract/Conclusion 的 "regardless of model family or scale" 在 1B-8B 范围且 Qwen-heavy 的情况下属 overclaiming
- 仅 Qwen-Instruct 一个指令微调模型，缺少 RLHF/DPO 覆盖
- **处理建议**：弱化为 "across six families at 1B-8B scale"；Limitations 讨论家族分布不均影响

**MF-2** [critical, 共识] **K\*≤2 导致的贡献悖论**

- K\*≤2 使 depth estimation 框架在实践中退化为 binary classification
- Section 5 filtering 实验印证 binary-ours 即可最小化 MMLU 退化（-0.77pp vs -1.53pp no-filter）
- arXiv K\*=3 作为 depth estimation 有增量价值的正面证据仅基于两模型（Qwen-1.5B, Pythia-1.4B）一域（arXiv abstracts），n=2,200，说服力有限
- R1 注意到标题已包含 "Measuring the Discrimination Boundary"，核心贡献本就是测量边界值
- **处理建议**：Introduction 更早明确 K\*=2 本身就是核心发现（而非深度估计的通用能力）；扩展 arXiv K\*=3 的模型/域覆盖

### Should-Fix — Reviewer 分歧项

**SF-1** [R1: Must-Fix, R2: Should-Fix] **DPI→AUC 推理链的逻辑缺口**

- (a) AUC 非互信息单调函数，论文仅半句承认 "are not formally equivalent"
- (b) Table 19 greedy decoding 下 AUC 在高深度出现非单调上升（Pythia-1.4B greedy 4v5 AUC=1.0 > 3v4=0.522），论文归因于 repetition collapse 但仅在脚注
- (c) K\*_theory 定义依赖 AUC 单调性假设，如不成立则 "lower bound" 解释动摇
- R1 立场：理论框架的脊柱，动摇 K\*_theory 和 lower bound 解释
- R2 立场：K\*_empirical 操作性定义不依赖理论推导，DPI 是 motivation 而非 derivation
- **处理建议**：DPI 从 derivation 降级为 motivating intuition；限定 "lower bound" 解释的适用条件（排除 greedy 退化情形）；正文显式讨论 Table 19 非单调性

**SF-2** [R2: Must-Fix, R1: Should-Fix] **相关工作缺失递归生成理论文献**

- 未引用递归 LLM 生成的 Markov chain 收敛理论（收敛速率、不动点行为）
- 未引用 detection erosion 文献（检测性能随生成代数衰减）
- R2 立场：缺失影响新颖性判断
- R1 立场：方法论和实验设计不依赖这些文献，属完整性问题
- **处理建议**：Related Work 补充两类文献引用，明确本文实证测量与理论预测的互补性

### Should-Fix — 共识项

**SF-3** [warning, 共识] **θ=0.60 的 Cohen's h 映射数学错误**：脚注 1 声称 h ≈ 0.20（小效应），实际 d = √2·Φ⁻¹(0.60) ≈ 0.358（小到中效应）。Figure 3 sensitivity 已提供更有力的阈值论证，但数学错误应修正。

**SF-4** [warning, 共识] **Abstract 信息过载**：~200 词内压缩 K\* 定义、10 配置、3 域、4 解码策略、Bonferroni、arXiv 特例、filtering 等。建议聚焦 K\*≤2 核心发现和 cross-model transfer 两个 take-home messages，方法细节留给正文。

**SF-5** [warning, 共识] **"model-free" 措辞与 scorer 依赖的张力**：15 维中 8 个 surprisal 特征依赖外部 scorer 模型。Table 22 cross-scoring 下部分配置 K\* 变化（Qwen-cont: K\*=2→1）。建议改为 "generator-agnostic"。

**SF-6** [warning, 共识] **self-BLEU 在 GroupKFold 中潜在数据泄漏**：self-BLEU 的 100 参考样本是否跨 fold 未说明。Section 3.2 提及 fold 内计算但不够明确。非 top-3 特征，影响可能有限，但方法论应澄清。

**SF-7** [warning, R1 提出, R2 部分 REBUT] **Filtering 实验在现实污染率下效果量极小**：附录 B.8 已有 dose-response（10% 污染下 Δ=0.1pp，不显著），但正文仅展示 100% 设置。建议正文引用 dose-response 结果，定位进一步弱化为 "consistency check under extreme contamination"。

**SF-8** [warning, 共识] **K\*_empirical 下界紧致性未量化**：Neural probe（frozen encoder）2v3 AUC=0.6159 仅略高于 θ，暗示 K\*_theory 可能接近 K\*_empirical，但单一 probe 不充分。建议讨论 tightness 或承认为开放问题。

**SF-9** [warning, 共识] **One-wash laundering 新颖性边界模糊**：与 model collapse 文献中 first-iteration dominant degradation 的区分不清。建议明确区分质量退化（分布坍缩）vs 可辨别性消失（统计指纹被抹平），讨论二者是否独立现象。

**SF-10** [warning, R2 提出, R1 部分 REBUT] **Binary detector 对比框架部分不公平**：6-class accuracy 对 binary detector 不公平，但 pairwise AUC（K\*_binary ≤ 1）是公平评估。建议弱化 6-class accuracy 讨论，突出 pairwise AUC 作为主要对比指标。

### Minor

- **m1** Top-3 特征（surp_d1_std, surp_std, surp_d2_std）正文缺直觉解释
- **m2** Figure 2 caption 未自解释 "pairwise AUC" 含义
- **m3** 统计检验策略（Bootstrap/permutation/Bonferroni）散布多处，缺统一说明
- **m4** Table 4 arXiv K\*=3 仅两模型验证
- **m5** Conclusion 与 Abstract 核心句逐字重复
- **m6** Figure 3 x 轴范围 θ∈[0.53,0.70] 选择未解释
- **m7** Eq.1 记法模糊（量化变量 ℓ' 与外层 ℓ 混淆）
- **m8** OBD vs multiclass 差异仅 0.032，未报告统计检验
- **m9** Table 1 Config 命名（Qwen-rw/Qwen-cont/Qwen-base）易混淆
- **m10** Appendix 表编号跳跃，正文引用需大量翻页

---

## Reviewer Consensus

以下关键问题双方达成共识 [AGREE]：
1. 问题新颖有价值，K\*_empirical 定义清晰
2. "regardless of model family or scale" 属 overclaiming（Qwen-heavy, 1B-8B），需弱化
3. K\*≤2 贡献悖论需正面处理（重新定位贡献）
4. arXiv K\*=3 证据薄弱（仅两模型一域）
5. Abstract 信息过载
6. "model-free" 应改为 "generator-agnostic"
7. θ=0.60 Cohen's h 数学错误需修正
8. 跨模型迁移和统计实践是论文最强的方面

## Reviewer Divergence

| 问题 | R1 | R2 | 备注 |
|------|----|----|------|
| DPI→AUC 缺口 | Must-Fix | Should-Fix | R1: 理论框架脊柱; R2: DPI 是 motivation 非 derivation |
| 相关工作缺失 | Should-Fix | Must-Fix | R1: 不影响方法论; R2: 影响新颖性判断 |
| Binary detector 对比 | pairwise AUC 部分救回 | 6-class 不公平 | 共识弱化 6-class，突出 pairwise AUC |

---

## Questions

1. **[R1 Q2, R2 AGREE, 高优先级]** 去掉 Qwen 4 个配置后，K\*=2 仅剩 2/6（Pythia-1.4B 边界值 + LLaMA-8B）。这是否仍支撑 "K\*=2 is the norm" 的结论？
2. **[R1 Q1]** Table 19 greedy decoding AUC 非单调上升（Pythia 4v5=1.0 > 3v4=0.522）如何在 DPI 框架下解释？
3. **[R1 Q3, R2 AGREE]** Fine-tuned encoder（而非 frozen hidden states）是否会显著提升 2v3 AUC，改变 K\*_empirical 估计？
4. **[R1 Q4, R2 AGREE]** Rewrite mode 始终给出更高 K\*。K\* 更多反映 generation strategy 还是 model intrinsic property？
5. **[R2 Q1]** 70B+ 模型（如 Llama-3-70B）K\* 会降到 1 还是保持 2？
6. **[R2 Q2]** arXiv K\*=3 是因为学术文本结构化程度（section headings, citation patterns）还是种子文本低熵？
7. **[R2 Q3]** Multi-model pipeline（GPT-4→Claude→Llama）下 K\* 是否变化？

---

## Missing References

**共识应补充：**
- Ghostbuster (Verma et al., 2024): perplexity-based detection，与 surprisal 特征方法论联系
- GPTZero (Liang et al., 2023): 广泛使用的检测器，Related Work baseline
- RAID benchmark (Dugan et al., 2024): AI text detection benchmark，与跨模型泛化声明相关
- 递归生成 Markov chain 收敛理论文献（收敛速率、不动点行为）
- Detection erosion / performance degradation 文献

**R1 提出 R2 反驳：**
- Kirchenbauer et al., 2023 (watermarking, ICML): R2 认为方法论正交（proactive vs passive），非必要引用

---

## External Review

外部审稿：未请求（项目未配置 paperreview.ai）。

---

## Visual Layout Check（非评分项）

视觉审查已完成。0 critical / 2 warning / 13 info。

**Warnings：**
1. **第 7-8 页视觉节奏中断**：Discussion 全文 + Conclusion 开头连续两页纯文本，无图表穿插。建议加总结性表格或 summary figure。
2. **附录末页空白过多**：第 18 页仅顶部 ~25% 有 Table 28，~75% 空白。建议重排或合并。

**正面发现：**
- 主文 8 页含 4 figure + ~5 table = 9 display items，密度合适
- 第 3-6 页 text-figure-table 交替良好
- 所有图表专业（booktabs 风格），Figure 2/3/4 清晰可读
- 未发现 margin 溢出、未解析引用或公式渲染错误
- 格式合规：8 页正文 + Limitations/Ethics 不超页，匿名化正确

---

## Overall Assessment

**评分：3.5 / 5（Borderline Conference）**
**置信度：4 / 5**

| 维度 | R1 | R2 | 综合 |
|------|----|----|------|
| Soundness | 3.5 | 4.0 | 3.75 |
| Excitement | 3.0 | 3.0 | 3.0 |
| Reproducibility | 4.0 | 4.0 | 4.0 |
| Overall | 3.5 | 3.5 | 3.5 |

**核心判断**：论文定义了一个新颖且有意义的研究问题，实验系统全面，统计实践规范，跨模型迁移令人信服。但两个核心顾虑限制了评分：(1) 普适性声明显著超出 Qwen-heavy + 1B-8B 实验覆盖范围；(2) K\*≤2 的核心发现使 depth estimation 框架的增量价值受限于测量工具本身而非实用工具。DPI→AUC 理论缺口（R1 Must-Fix / R2 Should-Fix）是唯一未解决的 Reviewer 分歧。

**接收条件**：如果 rebuttal 能 (a) 弱化 "regardless of" 普适性声明至实验支撑范围，(b) 诚实重新定位贡献为 "measuring the boundary" 而非 "depth estimation tool"，(c) 处理 DPI→AUC 缺口（降级为 motivation 或提供形式化修补），两位 Reviewer 均表示愿意考虑提升至 4.0（Conference）。

**降分风险**：R2 在交叉回应后指出，若 Qwen 代表性问题和贡献悖论未有效回应，3.0（Findings）可能更合适。

---

## Detailed Comments

### Section 1 (Introduction)
- 贡献 (a) 定位从 "depth estimation tool" 调整为 "measurement of the discrimination boundary"
- "regardless of model family or scale" 弱化为实验支撑范围
- 更早声明 K\*=2 本身是核心发现

### Section 2 (Related Work)
- 补充 Markov chain 收敛理论和 detection erosion 文献
- 补充 Ghostbuster、GPTZero、RAID benchmark
- 与已有理论预测对比本文实证测量的互补性

### Section 3 (Method)
- DPI 从 derivation 降级为 motivating intuition
- θ=0.60 脚注 Cohen's h 数学修正（h≈0.20→实际≈0.36）
- Eq.1 量化变量记法改进
- self-BLEU CV 计算粒度澄清（fold 内 vs 全局）
- "model-free" → "generator-agnostic"

### Section 4 (Experiments)
- Table 2 脚注或正文讨论 Qwen 过度代表的影响
- Section 4.6 弱化 6-class accuracy，突出 pairwise AUC 作为主要对比指标
- Section 4.4 讨论 lower bound tightness
- 正文显式讨论 Table 19 greedy 非单调性

### Section 5 (Filtering)
- 正文引用 dose-response 结果（附录 B.8: 10% 下 Δ=0.1pp 不显著）
- 明确定位为 "consistency check under extreme contamination"

### Section 6 (Discussion)
- One-wash laundering 与 model collapse first-iteration degradation 的区分
- 讨论 K\* 是 mode-dependent 还是 model-intrinsic
- 考虑加总结性表格改善第 7-8 页视觉节奏

### Section 7 (Conclusion)
- 避免与 Abstract 核心句逐字重复
- 弱化 "regardless of scale" 为 "at 1B-8B scale"