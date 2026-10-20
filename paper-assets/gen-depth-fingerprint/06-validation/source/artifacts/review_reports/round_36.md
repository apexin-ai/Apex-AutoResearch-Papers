---
round: 36
review_mode: fresh
overall_score: 3.0 (Findings)
timestamp: 2026-05-21T04:01:20.443482+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# Round 36 审稿报告 — Depth Fingerprinting: Detecting Recursive Generation Depth in LLM Text Chains

**Venue**: EMNLP 2026 (ARR) | **Deadline**: 2026-05-25 | **审稿模式**: Fresh (初审)
**Reviewer 编排**: R1 (方法严谨性) + R2 (新颖性/完整性) | **轮次**: 1 轮 + 交叉回应

---

## Summary

论文提出 "depth fingerprinting"：将 AI 文本检测从二分类扩展到序数深度估计（gen-0/gen-1/gen-2+），核心发现为 differential depth response (DDR)——在 8 个 base-model generator（5 个架构家族, 0.6B-8B）的递归生成链中，NLL 位置统计量单调漂移而分布形状特征保持稳定。基于 DDR 的 7 特征 ensemble 在 leave-one-generator-out 评估下达到 binary F1=0.694；端到端 QLoRA 分类器达到 0.905。

---

## Strengths

1. **新颖的问题定义** [R1+R2 共识]：从 binary detection 到 ordinal depth classification 是自然且有意义的延伸，在 data provenance 和 model collapse 预防中有清晰的应用场景。
2. **DDR 分解有洞察力** [R1+R2 共识]：location/shape 分离——drifting features 单调漂移而 shape features 近似不变——是一个有趣的实证发现，为理解 LLM 递归生成的分布演化提供了新视角。
3. **实验覆盖面极广且预判到位** [R1+R2 共识]：17+ 项补充实验（TOST、LOFO、cross-domain、temperature、prompt type、instruction tuning、QLoRA、Granger causality、transfer、perturbation robustness 等），24 页附录系统性回答了大部分可预见质疑。
4. **泄露控制设计严谨** [R1]：三重机制——leak-free binary F1、seed-level demeaning (F1=0.701)、independent-seed control (F1=0.680)——差距仅 1.4pp，令人信服。
5. **诚实的 proof-of-concept 定位** [R2]：论文没有过度宣传分类性能，明确承认 ~30% 错分率和范围限制。
6. **与 baseline 的公平对比** [R1+R2 共识]：Table 2 使用相同 XGBoost pipeline 和 LOGO 协议，方法论公平。
7. **引用规范** [R2]：66 条引用，0 orphan，0 phantom，覆盖 2019-2026 文献。

---

## Weaknesses

### Must-Fix（影响接收决定）

**N1** [Critical | R1+R2+Visual Check 三方共识] **主文页数超过 EMNLP 8 页限制**
- Discussion 跨 page 8-9（约 1.3 页），Conclusion 在 page 9 约 20%，主文合计约 8.5-8.7 页。
- EMNLP 2026 严格限制主文 8 页（Limitations/Ethics 不计入）。格式违规可导致 desk reject。
- **修复方向**：压缩 Discussion 至 ~0.8 页（model collapse 区分、14B 初步结果、温度重复论述可移至附录）。

**N2** [Critical | R2 提出, R1 部分同意] **DDR 核心新颖性的 nucleus sampling confound**
- DDR 的 shape stability（entropy_max, tail_decay 稳定）可能是 nucleus sampling 在固定 p=0.9 下截断的 by-design 结果。Discussion (p.8) 原文 "top-p truncation selects from a fixed probability mass fraction...preserving the functional form" 恰恰暗示这是采样机制的数学性质。
- 论文**仅在 nucleus sampling 框架内**变化温度，未测试 greedy decoding、pure top-k、beam search。如果 shape stability 在非 nucleus sampling 下不成立，DDR 框架的泛化性和新颖性将显著缩水——变成 "nucleus sampling 的已知属性 + 已知的 diversity loss"。
- **R1 交叉回应中的关键判断**："问题不仅是温度范围窄，而是整个 decoding paradigm 的覆盖缺失"，建议升级为 must-fix 级补充实验。
- **R2 的核心论点**：drifting features（entropy_mean↓, TTR↓, hapax↓）本质上是 model collapse 文献中已记录的 diversity loss / entropy erosion；论文声称的新颖性在于 "what is preserved"，但如果 preservation 是采样机制的固有属性，增量贡献有限。
- **R1 的部分反驳**：location/shape 分离作为 decomposition 在 model collapse 文献中未被报告，且正是有 stable reference 才使 cross-generator depth detection 成为可能——DDR ≠ diversity loss 的简单重述。
- **分歧状态**：R1 认为 location/shape 分离有独立贡献但同意需要实验验证；R2 认为增量性更强。两人均同意 nucleus sampling confound 需要至少 greedy + top-k 验证实验。
- **修复方向**：(1) 补充 greedy/top-k 下 shape stability 验证；(2) 或明确承认 nucleus-sampling-specific 并精准界定增量贡献。

**N3** [Critical→Major, R1 提出, R2 降级] **k=2 聚类在 n=7 特征点上统计效力不足**
- DDR 分区依赖 k-means 在 7 个数据点上的聚类（silhouette=0.660），本质上是描述性的而非推断性的。排列检验 p=0.030 仅边际显著。
- **缓解证据**（R2 指出，R1 同意其存在但认为不充分）：generator-split validation 两组独立产生完全相同分区；holdout split 中 zone assignment 完全一致；跨 ε 稳定性在 [0.10, 0.75] 内核心分区不变。
- **严重性分歧**：R1 维持 critical（描述性非推断性），R2 降级为 major（三重验证已相当充分）。
- **综合判断**：降为 **Major**——现有 validation 支撑 descriptive claim，但 inferential rigor 有提升空间。
- **修复方向**：补充 gap statistic 或 prediction strength；考虑 sample-level bootstrap 验证聚类稳定性。

**N4** [Critical→Major, R1 提出, R2 同意] **TOST 中 tail_decay 仅 4/8 generator 通过——"near-stationary" 名不副实**
- tail_decay 在 ε=0.20 下仅 4/8 generator 通过 TOST；非通过 generators |d|=0.15-0.22。Granger causality p=0.375，permutation importance rank 7/7（最低）——均指向 "noisy/inconsistent" 而非 "near-stationary"。
- R1 和 R2 均同意应重分类。DDR 三分区（3/1/3）中 near-stationary 组有 1/3 不稳定，削弱框架清晰度。
- **修复方向**：主文将 tail_decay 重分类为 "weakly stationary"；补充移除 tail_decay 后的分类和分区 sensitivity analysis；Figure 2 中用不同标记区分。

**N5** [Critical→Major, R1 提出, R2 部分反驳] **ε=0.20 等价阈值缺乏问题特定正当性**
- Cohen's d=0.20 是行为科学通用惯例，未论证在生成深度检测中的合理性。
- **R2 反驳要点**：Table 30 证明核心分区在 ε∈[0.10, 0.75] 内完全不变——"分区结果是阈值函数" 仅适用于 entropy_std 的归属，不适用于核心 drifting/stationary 分区。
- **综合判断**：降为 **Major**——核心分区对 ε 高度稳定，但补充 task-specific justification 会增强论证。
- **修复方向**：从分类 F1 角度反推 SESOI（操作上可忽略的最小效应）；或绘制 equivalence frontier 图。

### Should-Fix（影响评分但不一票否决）

**W1** [Major | R1+R2 共识] **Base-model-only 范围限制实际适用性**
- Appendix K 显示 instruction-tuned models 3-class F1 降至 0.575/0.544（降幅 17-21pp），DDR silhouette 从 0.660 降至 0.372。2025-2026 年绝大多数部署 LLM 都是 instruction-tuned。
- Abstract/Introduction 措辞 ("When LLM outputs re-enter generation pipelines") 暗示广泛适用性，与 base-model-only 范围存在张力。
- **修复方向**：Discussion 增加专门段落讨论 instruct 退化机制；Introduction 第一段明确 scope。

**W2** [Major | R2 提出, R1 同意] **Downstream null result 在主文中讨论不充分**
- Appendix M 的 TOST 明确显示 depth-aware curation ≈ random subsampling。这直接关系到 Introduction 中 "data provenance matters" 的动机。Discussion 仅用一句话带过。
- **修复方向**：Discussion 增加专门段落讨论 null result 含义、为什么 depth signal 不能转化下游收益、在什么条件下可能有差异；重新定位价值为 provenance/audit 而非 curation。

**W3** [Major | R1 提出, R2 同意] **QLoRA +11.6pp 基线比较跨子集不一致**
- +11.6pp 基于 6-gen subset (XGBoost baseline=0.789)，而主文 Table 1 的 8-gen LOGO binary F1=0.694。两个基线相差 9.5pp。Discussion 引用 "QLoRA recovers 0.905" 时未标注是 6-gen 结果，读者容易误读。
- **修复方向**：所有 QLoRA 引用标注 "(6-gen subset)"；补报 8-gen LOGO 下 QLoRA 结果。

**W4** [Major | R1 提出, R2 同意] **Bootstrap CI 未捕获 generator-level 方差**
- 8-gen LOGO macro F1=0.762，95% CI 宽度仅 4.8pp。但 per-generator binary F1 range 达 9.1pp (0.633-0.724)。Pythia 系列系统性高于其他 family，可能反映 Pythia-410M 参考模型的 same-family 优势。
- **修复方向**：补充 across-generator SD/IQR 与 bootstrap CI 并列报告；讨论 same-family reference bias。

**W5** [Minor-Major | R1+R2+Visual Check 共识] **前 4 页无任何图表，信息密度不均**
- 作为 empirical paper，前 4 整页纯文字，首个视觉元素 (Table 1) 在 page 5，Figure 1 在 page 6。Related Work 1.5+ 页无结构化对比。
- **修复方向**：将 Figure 1 (strip plot) 前移至 Introduction 末尾或 Method 开头；Related Work 加入 method comparison table。

**W6** [Minor | R1 提出, R2 部分同意] **五种 effect-size measures 的 "complementarity" 过度宣称**
- Cohen's d 和 Glass's Δ 在组间方差接近时高度相关；KS 在 location shift 主导时也与 Cohen's d 强相关。"五重验证" 可能过度膨胀置信度。
- **修复方向**：改为 "convergence across parametric and non-parametric measures"；补充 inter-measure 相关矩阵。

**W7** [Minor | R1+R2 共识] **Reference model (Pythia-410M) same-family confound 主文讨论不足**
- 8 个 generator 中 2 个来自 Pythia family，reference model 同家族。Appendix S 验证了 cross-family reference 信号保持（spread 0.013），但主文仅一笔带过。
- **修复方向**：§3.3 或 §5 补充 reference model bias 讨论；分 generator 报告 cross-reference 影响。

---

## Reviewer Consensus [AGREE]

1. **页数超限** (~8.5 页) 需立即修复——desk reject 风险
2. **tail_decay 应重分类**——4/8 TOST 通过率不支持 "near-stationary" 标签
3. **Base-model-only 限制**需在主文更显著讨论
4. **QLoRA +11.6pp 跨子集不一致**需标注子集信息
5. **Bootstrap CI + generator-level variance** 需补充报告
6. **Downstream null result** 需在 Discussion 获得更充分讨论
7. **前 4 页无图表**需改善信息密度分布
8. **Proof-of-concept 定位总体良好**，论文在大多数位置保持一致
9. **引用质量良好**（66 条, 0 orphan, 0 missing），建议补充 Tulchinskii et al. (2024)

## Reviewer Divergence [REBUT]

1. **DDR 新颖性** [核心分歧]
   - R1 (3.5): location/shape 分离是新贡献，在 model collapse 文献中未见——DDR ≠ diversity loss 的简单重述；即使需更强验证，decomposition 本身有独立价值
   - R2 (3.0): drifting features 本质是已知的 diversity loss，shape stability 可能是 nucleus sampling 的 trivial 推论，增量贡献有限
   - **两人共识**：无论如何，nucleus sampling confound 需要实验验证（greedy/top-k）

2. **k=2 聚类严重性**
   - R1: critical（描述性非推断性，p=0.030 仅边际显著）
   - R2: major（generator-split/holdout/ε-stability 三重验证已相当充分）

3. **ε=0.20 循环论证严重性**
   - R1: critical（缺乏 domain-specific justification）
   - R2: major（Table 30 证明核心分区对 ε 高度稳定，"循环论证" 判断过重）

4. **3-class 粒度的价值**
   - R1: 科学价值独立于即时应用，证明 depth 可检测本身就是贡献
   - R2: 缺乏量化 use case，增量价值论证不足

---

## Questions

1. Shape stability 是否在 greedy decoding / pure top-k 下同样成立？如果仅在 nucleus sampling 下成立，如何论证这不是 sampling truncation 的 trivial 推论？[R1+R2]
2. Downstream null result (Appendix M) 表明 depth-aware curation ≈ random subsampling。在什么条件下预期 depth signal 能转化为实际 downstream benefit？[R2]
3. 增加更多特征（n-gram diversity, 句法复杂度, discourse coherence）后 DDR 的 drifting/stationary 二分是否仍成立？当前 7 特征中 5 个基于 token-level NLL，特征空间局限性是否预设了分区结果？[R1]
4. Instruction-tuned 下 silhouette 降至 0.372——DDR 框架的 drifting/stationary 分离前提是否在 instruction-tuned 模型下不再成立？这是否意味着论文的理论贡献局限于 base models？[R1+R2]
5. 使用 2.8B/7B 参考模型是否会改变 DDR 分区本身（不仅是分类 F1）？Appendix S 未报告此项。[R1]
6. 是否尝试过从分类 F1 角度反推 ε（操作上可忽略的最小效应）？[R1]
7. 是否尝试过在 instruction-tuned chain 上重新训练分类器（而非 base-trained 分类器直接迁移）？[R2]

---

## Missing References

以下由两位 Reviewer 独立建议：
1. **Tulchinskii et al. (2024)** "Intrinsic Dimension Estimation for Robust Detection of AI-Generated Texts" (ICLR 2024) — R1+R2 共同建议，使用几何/拓扑特征检测 AI 文本，与本文 distributional statistics 方法互补
2. **RADAR (Hu et al., 2023)** — R2 建议，adversarial training-based detector
3. 代码域检测先前工作 — R1 建议，论文在 Appendix J 测试了 Code 域但未引用相关文献

---

## External Review (Stanford Agentic Reviewer)

**状态**: 已跳过（用户未提交）

---

## Visual Layout Check（非评分项）

**状态**: 完成 | 4 warnings, 14 info

**关键发现**：
- **[Warning]** Pages 1-4 连续纯文本，无任何 display item。审稿人需翻到 page 5 才看到第一个视觉锚点 (Table 1)。建议将 Figure 1 (strip plot) 前移至 page 2-3。
- **[Warning]** 第一个 display item 出现在 page 5，Figure 1 在 page 6——审稿人在前 2 分钟内无法建立核心发现的视觉认知。
- **[Warning]** Discussion 跨 page 8-9，约 1.5 页连续纯文本。结合前面 pages 1-4 的纯文本段，全文 "文本墙" 比例偏高。
- **[Warning]** 主文延伸至 page 9 约 2/3 处，约 8.7 页，可能超页。
- **[Info]** Table 1/2 格式规范（booktabs, 加粗最优结果）。Figure 2+3+Table 2 在 page 7 密度适当。Figure 7 (base vs instruct DDR) 颜色清晰。Figure 1 strip plot 中 8 色在黑白/色弱条件下可能难以区分，建议添加 marker shape。Appendix 中 page 15 (Figure 4) 底部约 1/4 空白、page 25 (Figure 8) 子面板字号偏小（约正文 60%）。

---

## Overall Assessment

**综合评分: 3.0 (Findings)**
**置信度: 4/5**

| 维度 | R1 | R2 | 综合 |
|------|-----|-----|------|
| Soundness | 3/5 | 3.5/5 | 3/5 |
| Excitement | 3.5/5 | 2.5/5 | 3/5 |
| Reproducibility | 4/5 | 4/5 | 4/5 |
| Overall | 3.5 | 3.0 | 3.0 |

**评分理由**：

论文在实验执行和统计方法上高于平均水准，DDR 的 location/shape 分解角度有一定新意，问题定义从 binary 到 ordinal 是有意义的延伸。但以下因素将评分压至 Findings 水平：

1. **格式违规** (N1): 主文约 8.5-8.7 页，超过 8 页限制，存在 desk reject 风险。这是可修复的但当前状态下是硬伤。
2. **核心新颖性存疑** (N2): shape stability 可能是 nucleus sampling 的 by-design 属性——论文未提供非 nucleus sampling 的验证实验，而 Discussion 原文恰恰暗示了这一机制解释。如果这一质疑成立，DDR 的 "novel observation" 将缩水为 "nucleus sampling + 已知 diversity loss"。R1 认为 location/shape 分离本身有独立贡献 (3.5)，R2 认为增量性更强 (3.0)——这是评分差异的核心来源。
3. **统计框架的方法论短板** (N3-N5): k=2 聚类在 n=7 上虽有辅助验证但统计效力先天不足；tail_decay "near-stationary" 标签不准确（4/8 TOST）；ε=0.20 缺乏 domain-specific justification。这些单独看是可修复的 major 问题，但累积起来削弱了 DDR 分析框架的 methodological rigor。
4. **实际影响力受限**: base-model-only scope + downstream null result + 3-class 粒度限制了论文的应用前景。

**如果以下条件满足，评分可提升至 3.5 (Borderline Conference)**：
- 修复页数超限
- 补充 greedy/top-k 下 shape stability 验证（或令人信服地论证为何 nucleus-sampling-specific 仍有独立贡献）
- 修正 tail_decay 分类标签
- Discussion 充分讨论 instruct 退化和 downstream null result

---

## Detailed Comments

### Section 1 (Introduction)
- 开头 "When LLM outputs re-enter generation pipelines" 暗示广泛适用性，但论文仅覆盖 base model continuation chains。建议第一段明确 scope。
- Contribution 列表从 3 条缩减到 2 条 + 一个 "additionally provide"——结构清晰但 "additionally" 部分读起来像第三个贡献。
- R2-Q5: 为什么选 continuation chain 而非 paraphrase chain？R1 引用 Appendix Z.6 Table 41 解释了方法论原因（语义自由度更高），但主文未讨论此设计选择。

### Section 2 (Related Work)
- §2.2 最后一段对 Broken Telephone / Markovian Chains 的区分较好，但 R2 认为仍可加入结构化对比表以增强说服力。
- 缺 Tulchinskii et al. (2024) [R1+R2 共识]。

### Section 3 (Method)
- §3.3 "entropy as shorthand for NLL" 声明存在但可考虑更精确的措辞（R2 minor）。
- §3.4 "LOGO family-level" 行定义需澄清——是 per-generator 还是 per-family leave-one-out（R1 minor）。
- Reference model 选择的潜在偏差应在此处或 §5 明确讨论。

### Section 4 (Results)
- §4.1: bootstrap CI [0.758, 0.766] 宽度仅 0.8pp，而 per-generator spread 9.1pp。需补充 generator-level variance。
- §4.2: "five complementary effect-size measures" → 建议改为 "convergence across parametric and non-parametric measures"。
- §4.2: tail_decay 的 4/8 TOST 在主文已有三句覆盖 (L89-91)，但 "near-stationary" 标签仍过于宽泛。
- §4.3: Table 2 显示 4-det+surface (0.708) > 7-feature (0.705)——论文诚实报告，DDR 贡献定位为 decomposition 而非 classification performance。

### Section 5 (Discussion)
- 篇幅过长（~1.3 页），是页数超限的主要原因。
- 14B preliminary results 可移至附录。
- Model collapse 区分的讨论虽重要但可精简。
- Downstream null result 仅一句话——需扩展。
- QLoRA "0.905" 引用未标注 6-gen subset。

### Section 6 (Conclusion)
- "preliminary 14B evidence confirms the partition" 用词偏强——14B 是 preliminary 且仅 1 个模型。
- 可适当压缩。

### R1 事实纠正
R1-W5 声称 "缺 t=1.0"，但 Table 10 (Appendix H) 明确测试了 t∈{0.5, 0.7, 1.0}。R2 在交叉回应中纠正了此事实错误。温度覆盖度限制在于仅 4/8 generator 参与温度实验，而非缺少特定温度点。