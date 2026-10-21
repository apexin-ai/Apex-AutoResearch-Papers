---
round: 33
review_mode: fresh
overall_score: 3.0 — Findings
timestamp: 2026-05-20T15:45:46.154766+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告 — Round 32 (Fresh Review)

**论文**: "Depth Fingerprinting: Detecting Recursive Generation Depth in LLM Text Chains"
**Venue**: EMNLP 2026 via ACL Rolling Review (Long Paper)
**Reviewer 编排**: 2 名 Reviewer（R1: 方法严谨性+实验设计, R2: 新颖性+完整性+写作质量）
**交叉回应**: 完成（R1→R2, R2→R1）

---

## Summary

论文提出 depth fingerprinting——将文本按递归 LLM 生成深度分类为 gen-0/gen-1/gen-2+。核心分析发现 Differential Depth Response (DDR)：在 8 个 base model 生成器（5 个家族，0.6B–8B）上，NLL 分布的位置特征（entropy mean、TTR、hapax ratio）随深度单调漂移（Cohen's d=0.76–1.17），而形状特征（entropy max、tail decay）保持稳定（d&lt;0.10）。7-feature XGBoost ensemble 在 LOGO CV 下 binary F1=0.694，cross-model chains 0.830。QLoRA end-to-end 达 F1=0.905。实验仅限 base model；instruct model 上信号严重退化。附录极为详尽（21 页，25+ 子节）。

---

## Strengths

**S1. 任务定义新颖且有意义** [R1+R2 共识]
将 binary human/machine detection 扩展为 ordinal depth classification 是一个自然但未被充分探索的方向，与 model collapse、数据溯源问题紧密关联。

**S2. DDR 的二元分解（drifting vs. non-drifting）有扎实实证支持** [R1+R2 共识]
k=2 clustering（silhouette=0.632）、5 种 effect-size 指标交叉验证、holdout generator split（Δ|ρ|≤0.05）、bootstrap TOST（100% rejection for near-stationary features）——证据链在二元分解层面收敛。这是论文最有价值的发现。

**S3. 评估协议严谨** [R1+R2 共识]
LOGO CV 是跨生成器泛化的正确选择；binary F1 排除 gen-0 消除 seed-sharing 泄漏；independent-seed control（F1=0.680 vs 0.694）进一步确认信号来源。

**S4. 自我批判程度罕见** [R1+R2 共识]
Abstract 明确标注 "base (pretrained) LLMs"、"preliminary equivalence testing"、"depth signal degrades under instruction tuning"。Limitations 坦诚列举温度敏感性、instruct 退化、scale 限制。

**S5. 附录实验覆盖度令人印象深刻** [R1+R2 共识]
25+ 子节涵盖 LOFO、TOST、bootstrap、Granger causality、cross-temp、cross-domain、instruct、downstream、error analysis 等——几乎穷尽了所有合理的 robustness check。

---

## Weaknesses

### Critical（必须解决才可考虑接收）

**W1. 仅限 Base Model 的实验设计严重限制论文的现实意义** [R1+R2 共识, Critical]
- 全部 8 个生成器均为 base (pretrained) model。现实中 LLM 文本绝大多数来自 instruction-tuned/RLHF 模型。
- Appendix K 明确显示：instruct 模型上 3-class F1 下降 3.7–19.9pp，binary F1 降至 0.487（cross-generator LOGO）。
- 标题 "Detecting Recursive Generation Depth in LLM Text Chains" 暗示通用性，但实验仅支持 base-model chains。
- **处理建议**：(1) 至少加入 2-3 个主流 instruct 模型纳入主实验；(2) 或在标题/abstract 中明确限定 scope，将 Appendix K 结果提升到主文 Discussion。

**W2. DDR 发现的增量新颖性不够清晰** [R2 主导, R1 部分同意, Critical]
- DDR 核心（中心趋势漂移 + 形状稳定）可能是已知 diversity loss / mode-seeking behavior 的重新表述。
- LLM 多样性递减（entropy mean↓、TTR↓）已被广泛记录（Guo et al., 2024; Padmakumar &amp; He, 2024）。
- Geng et al. (2026) 已展示 attractor dynamics 将可区分深度约束在 ~3 类——与本文结论高度重叠。
- **处理建议**：设计实验直接对比 DDR 与简单 diversity-decline 假说；证明 shape stability 是 non-trivial 新发现。

**W3. 3/1/3 Partition 是 post-hoc 叙事构建，超出数据支持范围** [R1, Critical]
- k-means 结果不支持 3/1/3：k=2（silhouette=0.632, clean split）vs k=3（silhouette=0.499, 更差）——k=3 将 entropy_min 而非 entropy_std 分出独立 cluster。
- 获得 3/1/3 需要 "domain-informed refinement"，非 data-driven。
- **处理建议**：以 2-way split 为核心发现，3/1/3 降级为 secondary refinement 并明确标注。

**W4. Entropy min 的分类存在根本性矛盾** [R1, Critical]
- Pooled |ρ|=0.40（远离 near-stationary 的 |ρ|&lt;0.10）；Cohen's d=0.016 vs Cliff's δ=0.354（矛盾结论）。
- k=3 clustering 将 entropy_min 分出独立 cluster 而非归入 near-stationary。
- **处理建议**：将 entropy_min 标记为 "boundary feature"，或采用 3/2/2 partition。

**W5. Tail_decay 的 near-stationary 归类仅 50% generator 通过 TOST** [R1, Critical]
- Per-generator TOST (ε=0.20): 仅 4/8 通过；OLMo d=0.22 超过阈值。
- Bootstrap pooled 100% rejection 因大样本 power 过高，不可替代 per-generator 结论。
- **处理建议**：在主文明确 tail_decay 的 borderline 状态；报告 per-generator TOST 通过率。

### Major（影响评分但不一票否决）

**W6. Binary F1=0.694 的实用性需更诚实的定位** [R1+R2 共识]
- ~30% 错分率，depth-2 error rate 高达 48.42%。标题 "Detecting" 暗示可部署系统。
- **处理建议**：明确定位为 proof-of-concept；讨论不同场景下 F1=0.694 的 sufficiency。

**W7. Downstream Utility 实际为 null result，framing 含糊** [R1+R2 共识]
- Depth-aware curation (PPL=2.387) 不优于 random subsampling (PPL=2.367)——方向相反。
- n=3 seeds；Abstract 说 "no downstream training quality degradation"——技术正确但实际含义是 depth fingerprinting 对数据清洗无用。
- R2 观点：即使扩大规模，小 effect size 只会更精确确认 "没有差异"。
- **处理建议**：降低 downstream 作为 contribution 的权重；Abstract 改为更精确的表述。

**W8. QLoRA +11.6pp gap 反衬 7-feature 方法局限性** [R1+R2 共识]
- QLoRA F1=0.905 vs 7-feature 0.789；instruct 上 QLoRA 0.888–0.907 vs XGBoost 0.575–0.732。
- Contribution 3 仍以 classifier 为卖点。
- **处理建议**：更显式地将 7-feature 定位为分析工具而非竞争性检测方法。

**W9. Baseline 比较存在结构性不公平** [R1]
- 7-feature vs single-score baselines 不是公平比较；4-det.+surface binary F1=0.708 **优于** 7-feature 的 0.705。
- DDR-inspired features 在分类性能上无优势。
- **处理建议**：在 Table 2 中明确指出 4-detector ensemble 优于 7-feature；将比较 focus 转向分析解释力。

**W10. Cross-model chain F1=0.830 可能被 generator heterogeneity confound** [R1+R2 共识]
- Depth-1 由 generator A、depth-2 由 generator B——depth effect 与 generator identity 共变。仅 5 generator 子集。
- **处理建议**：标注为 "upper bound under favorable conditions"。

**W11. 遗漏直接相关的重要工作** [R1+R2]
- Wang et al. (ACL 2025) "Unveiling Attractor Cycles in LLMs" — 与 DDR convergence 直接相关
- Sun et al. (2026) "When AI Settles Down: Late-Stage Stability" — 与 shape stability 有对话关系
- Guo et al. (ICLR 2024) 迭代生成链分布收敛
- Li et al. (2024) 递归生成分布演化理论分析
- Zhang et al. (2024) MMD-based detection（可作 baseline）
- Weng et al. (2025) source attribution / provenance tracking
- self_refine (Madaan et al., 2023) orphan bib entry 仍存在

**W12. TOST Power Analysis 缺失** [R1]
- Per-generator n≈3,500–4,500，大样本下 TOST 几乎总检测到 equivalence。
- 未报告在 ε=0.20 下区分 d=0.10 vs d=0.20 的 power。

### Minor

**W13.** 术语混淆：全篇用 "entropy" 指代 NLL，与 Shannon entropy 概念不同 [R2]
**W14.** 附录 25 页是主文 3 倍，Appendix K (instruct)、Appendix E (QLoRA) 等关键结果应在主文讨论 [R2]
**W15.** 3-class F1=0.762 因 gen-0 共享（recall 99.4%）而 misleading，Abstract 仍提到此数字 [R1+R2]
**W16.** 单一解码策略（nucleus, τ=0.7, p=0.9），未验证 greedy/top-k 下 DDR [R1+R2]
**W17.** 7 个特征选取缺乏系统性论证（R1: major → R2 降级为 warning） [R1+R2 分歧]
**W18.** self_refine orphan bib entry [R1+R2]
**W19.** Figure 2 黑白打印不可辨别 [R2]
**W20.** LOFO 用 6-generator 子集而非 8-generator LOGO，数值不可比 [R1]
**W21.** entropy_max 在 LOFO 中贡献最大（-1.50pp）但为 near-stationary feature——暗示非线性交互，值得讨论 [R1]

---

## Reviewer Consensus [AGREE]

1. Base-model-only 是核心瓶颈，标题/abstract 需限定 scope 或扩展实验
2. Binary F1=0.694 不足以支撑 "detecting" 的标题承诺，需明确 proof-of-concept 定位
3. Downstream utility 为 null result，framing 需更透明
4. Cross-model F1=0.830 可能被 generator heterogeneity confound
5. QLoRA gap 证明 7-feature 是 lossy compression，定位需更显式
6. 附录实验覆盖度令人印象深刻，统计方法总体严谨
7. 任务定义新颖且有意义
8. DDR 二元分解（drifting vs non-drifting）有扎实实证支持

## Reviewer Divergence [REBUT]

1. **DDR 新颖性角度**：R2 认为 DDR 可能是 diversity loss 的重新表述（更根本性质疑）；R1 认为 2-way split 本身有价值但 3/1/3 是 post-hoc over-fitting（关注 granularity 而非 existence）。两种批评互补而非矛盾。
2. **特征选择 severity**：R1 列为 must-fix（需从更大候选池系统筛选）；R2 rebut 降为 warning（reference/surface 分组有理论动机，LOFO 提供事后验证）。采纳 R2 判断，归入 minor。
3. **Figure 1 strip plot**：R1 认为过于拥挤；R2 认为信息密度可接受。
4. **Downstream 改进方向**：R1 建议扩大规模（100K+）；R2 rebut 认为 effect size 才是核心问题，扩大规模只会更精确确认"没有差异"。采纳 R2 判断。

---

## Questions（需作者澄清）

Q1. 如果将 DDR partition 简化为 2-way（drifting vs. non-drifting），classification performance 如何变化？
Q2. Entropy_max 在 LOFO 中贡献最大（-1.50pp）但为 near-stationary feature——它如何通过 depth 不相关的信号帮助分类？
Q3. Per-generator TOST 中 tail_decay 仅 4/8 通过。将 tail_decay 重分类为 intermediate 后（partition → 3/2/2），主要结论是否仍成立？
Q4. Cross-model chain 实验中能否控制 generator heterogeneity confound？
Q5. Downstream experiment 显示 depth-aware 不优于 random——depth fingerprinting 的用途是否仅限于分析性？
Q6. 7-feature 在 instruct data 上 LOGO F1=0.487（near chance），QLoRA 恢复到 0.89——7 个 summary statistics 是否从根本上无法捕获 instruct depth signal？
Q7. 如何回应 "DDR 只是 mode-seeking behavior / diversity loss 的重新表述" 这一批评？

---

## Missing References

1. Wang, Z. et al. (ACL 2025). "Unveiling Attractor Cycles in Large Language Models: A Dynamical Systems View of Successive Paraphrasing."
2. Sun, K. et al. (2026). "When AI Settles Down: Late-Stage Stability as a Signature of AI-Generated Text Detection." arXiv:2601.04833.
3. Guo et al. (ICLR 2024). "On the Stability of Iterative Retraining of Generative Models on their own Data."
4. Li et al. (2024). "Self-Consuming Generative Models with Curated Data Provably Optimize Human Preferences."
5. Zhang et al. (2024). "Detecting Machine-Generated Texts by Multi-Population Aware Optimization for Maximum Mean Discrepancy."
6. Weng et al. (2025). "Source-Aware Training Enables Knowledge Attribution in Language Models."
7. Orphan bib entry: `self_refine` (Madaan et al., 2023) — 存在于 .bib 但未被引用，应删除。

---

## External Review (Stanford Agentic Reviewer)

外部审稿：**已跳过**（用户未提交）。

---

## Visual Layout Check（非评分项）

视觉审查已完成（2 critical, 6 warning, 18 info）。主要发现：

- **[Critical] Page 24 严重空白**：>75% 页面空白，仅有 "UMAP Embedding" 小节标题 + 11 行文字，Figure 8 被推到 page 25。LaTeX float 排列失败，需修复 float placement。
- **[Critical] Page 24 空白重复确认**：全文最严重的排版问题。
- **[Warning] Page 1-3 连续纯文本**：前 3 页无任何 display item（Abstract → Introduction → Related Work → Method）。建议在 page 1-2 加入 overview figure 锚定论文 idea。
- **[Warning] Page 8-9 纯文本**：Discussion + Conclusion + Limitations + Ethics 无 display item 支撑。
- **[Warning] Page 23 底部 ~1/3 空白**；**Page 25 三个 figures 过于密集**（与 page 24 空白形成对比）。
- **[Info]** Figure/Table 格式整体良好：booktabs 风格统一、最优值加粗、颜色可区分、无 LaTeX 错误残留。主正文 5 个 display items（密度偏低但可接受）；附录约 30 个 display items。

---

## Overall Assessment

**Overall Score: 3.0 — Findings**

| 维度 | R1 | R2 | 综合 |
|------|-----|-----|------|
| Soundness | 3.5 | 3.5 | 3.5 |
| Excitement | 3.0 | 2.5 | 2.5 |
| Reproducibility | 4.0 | 4.0 | 4.0 |
| Confidence | 4/5 | 4/5 | 4/5 |

**核心判断**：

论文提出了一个有意义的新任务（depth fingerprinting），DDR 的二元分解（drifting vs. non-drifting features）是一个 clean 且跨生成器一致的实证发现，附录实验覆盖度令人印象深刻，自我批判程度罕见。

但三个核心瓶颈使其不适合 main conference 接收：

1. **Scope 限制**（W1）：仅在 base model 上验证，instruction-tuned 模型上信号严重退化（F1 降至 0.487），而后者是实际应用的主流。标题/abstract 的通用表述与实验范围不匹配。

2. **新颖性 + 方法论严谨性**（W2-W5）：DDR 与已知 diversity loss / mode-seeking behavior 的理论区分不够清晰。3/1/3 partition 超出数据支持范围（k-means 仅支持 2-way split, k=3 silhouette 更差）。Entropy min 分类矛盾、tail_decay TOST 仅 50% 通过——DDR partition 的 granularity 和一致性存疑。

3. **实用性不足**（W6-W10）：Binary F1=0.694 的分类性能中等；downstream utility 为 null result；QLoRA 的 +11.6pp 优势反衬 7-feature 局限；4-detector ensemble 在 binary F1 上实际优于 7-feature（0.708 vs 0.705）。

**升级路径**：如果作者能够 (1) 将 instruct model 结果提升到主文或明确限定 scope；(2) 以 2-way split 为核心、诚实处理 entropy_min 和 tail_decay 的 borderline 状态；(3) 设计实验证明 shape stability 非 trivial；(4) 将分类性能明确定位为 proof-of-concept——论文可提升至 3.5–4.0（Borderline Conference 至 Conference）。

当前状态适合 **Findings** 接收。