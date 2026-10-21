---
round: 5
overall_score: borderline
timestamp: 2026-05-16T19:49:41.960395+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# Round 6 审稿报告 — recursive_gen_depth_est

**Paper**: "How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints"
**Venue**: EMNLP 2026 Main Conference (ARR May cycle)
**Deadline**: 2026-05-25
**Reviewers**: 2 (R1: 方法严谨性+实验有效性; R2: 新颖性+Related Work+写作)

---

## Summary

本文将递归生成深度估计形式化为 ordinal classification 任务，提出 19 维统计指纹特征（以 perplexity tail statistics 为主导），在 3×3 model-strategy atlas (180K samples) 上实现 70-85% 四类准确率。引入 Effective Discriminable Depth (EDD) 指标量化可区分深度边界。经过 5 轮修订，论文在实验系统性、Limitations 诚实度、d0 inflation 透明化等方面有显著改善，但在 novelty framing、文献遗漏和若干写作问题上仍有不足。

---

## Strengths

1. **任务定义清晰有价值**：recursive depth estimation as ordinal classification 是该领域自然但此前未被提出的 framing，EDD 指标设计合理（连续性公式、threshold sensitivity 分析）。

2. **实验系统性优秀**：3×3 atlas + 7 轴 generalization + 多种 ablation + domain bias 自纠正 + base-vs-instruct control 远超 typical EMNLP 论文的 thoroughness。

3. **诚实的 Limitations**：覆盖 7+ 个明确局限（reference model dependency、domain FPR、adversarial robustness、BOS-seeded ecological validity、cross-strategy constraint），展现严谨学术态度。

4. **Cross-boundary chain + reverse control**：双向异构链实验 (84.75%/85.75%) 巧妙地 address architecture confound，是实验设计亮点。

5. **Feature validity 多角度验证**：VIF 分析 + 三种 importance measure concordance (Kendall W=0.90) + forward selection + top-k ablation (top-5 = 97.6%) 提供了 robust 的特征有效性证据。

6. **Temperature robustness 的机制洞察**：τ=1.1 collapse + 训练 loss 分析揭示 "memorization as prerequisite for depth signal" 的有意义发现。

---

## Weaknesses

### Must-Fix (2 项)

**MF1** [引用诚信] `alemohammad2024_mad` bib 条目作者错误
- "Romero, Oscar" 应为 "Leong, Oscar"，"Ramanarayanan, Sriram" 应为 "Rangamani, Akshay"
- 来源：arXiv:2307.01850 确认
- 影响：引用诚信问题，camera-ready 审查必发现
- **共识**：两位 Reviewer 一致确认 Must-Fix

**MF2** [文献遗漏] Related Work 缺失 Schaeffer et al. (2025) "Model Collapse Does Not Mean What You Think"
- 该文直接质疑 model collapse 的普遍性前提——本文以 collapse detection 为应用动机，不讨论 counterargument 构成对 literature 的选择性呈现
- 需要在 Discussion 加 1-2 句：即使 collapse 非必然，depth estimation 作为 provenance signal 仍有独立价值
- **共识**：两位 Reviewer 一致确认 Must-Fix

### Should-Fix (7 项)

**SF1** [实验] LoRA rank sensitivity ablation 缺失（遗留自 Round 1，6 轮未回应）
- r=16 是唯一测试值。若 r=4 时 signal 显著减弱则 depth signal 可能部分来自 LoRA capacity artifact
- 建议：至少在一个 cell 上测试 r∈{4, 64} 并报告 accuracy 变化
- **共识**：两位 Reviewer 一致

**SF2** [framing] Novelty vs Dohmatob (2024) 区分不够 explicit
- Related Work 建立了任务层面区分 ("inverse problem")，但 perplexity tail 使用的具体贡献区分缺失
- 需要 2-3 句 bridge: "Dohmatob et al. predict theoretically that tails erode; our contribution is demonstrating this prediction can be operationalized as a sufficient and dominant signal for ordinal depth classification"
- **共识**：两位 Reviewer 一致

**SF3** [写作] Abstract 信息密度过高 (20+ 数字 + "§4.4" 内部引用)
- 核心 message 被稀释，读者无法一次抓住 main result
- 建议精简至 5-8 个关键数字，删除 section 引用
- **共识**：两位 Reviewer 一致

**SF4** [framing] "universal/universality" 残留
- generalization.tex line 110: "further confirm signal universality" 无范围限定
- 建议替换为 "signal consistency across all tested configurations"
- **共识**：两位 Reviewer 一致

**SF5** [实验] Single-generator non-independence 未讨论
- 每个 depth 仅一个 LoRA instance，5-Fold CV 所有 folds 来自同一 generator
- 建议 Limitations 加 1-2 句承认此局限性
- **共识**：两位 Reviewer 一致

**SF6** [方法] EDD 未定义为 operational measure
- EDD 被呈现为 data 固有属性，实为 classifier+features 联合性质
- Table 3 (spread <0.4pp) 间接支持但未 explicitly connected
- 建议 §3.4 Definition 1 后加 caveat
- **共识**：R1 Should-Fix，R2 minor → 综合为 Should-Fix (low end)

**SF7** [写作] Discussion 正文 curation 提及未标注 inconclusive
- Contribution list 已删除 curation，Appendix 标注 inconclusive
- 但 Discussion.tex 仍以应用方向口吻提及，需加 "(preliminary; pilot results inconclusive)"
- **共识**：两位 Reviewer 一致

### Minor (5 项)

- R1-W1 残余：§4.2 个体 feature 排名声明需加 VIF caveat（"the stable signal unit is the feature group"）
- R6-N1：Contribution bullet 3 过度压缩 (7 axes + 6 数字)，建议拆分或概括
- R6-N2：Introduction "universal and scale-variant" 用词矛盾，建议 "consistent in direction but scale-dependent in magnitude"
- R5-W4 部分：Ordinal Classification 段落缺 Frank & Hall (2001) 和 Rennie & Srebro (2005) 经典引用
- Table 12 commentary typo："d1 (2.9%), d2 (0.9%), d1 (3.1%)" 第二个 d1 应为 d3

---

## Reviewer Consensus

以下问题两位 Reviewer 完全一致 [AGREE]：
- alemohammad 作者错误 Must-Fix
- Schaeffer et al. 遗漏 Must-Fix
- LoRA rank ablation Should-Fix（6 轮未回应）
- Single-generator non-independence Should-Fix
- Abstract 信息密度 Should-Fix
- "universal" 残留 Should-Fix
- Novelty vs Dohmatob bridge Should-Fix
- Discussion curation qualifier Should-Fix
- d0 inflation RESOLVED
- Reference model dependency RESOLVED via Limitations
- Strategy detection prerequisite RESOLVED
- Cross-scale "preliminary" RESOLVED（已存在于 abstract）
- §5.1 标题 RESOLVED（已为 "Classifier Comparison and Surface-Text Ablation"）
- FPR 数据报告准确（R1 初始误读已被 R2 纠正并核实）

## Reviewer Divergence

| 问题 | R1 | R2 | Director 裁定 |
|------|----|----|--------------|
| 方法论需 formal theory | 不必要 (EMNLP empirical track) | 限制 excitement | 不 blocking，记录于 R4-W3 |
| "consistent across families" p-value 不均 | 需确认 exact claim context | 建议 "directionally consistent" | Minor，abstract 已有 "graded statistical support" |
| EDD classifier-dep severity | Should-Fix | Minor | Should-Fix (low end) |

---

## Questions for Authors

1. LoRA rank sensitivity：是否有技术障碍阻止补充 r∈{4, 64} 消融？这是连续 6 轮未回应的 highest-priority open experiment。
2. Schaeffer et al. (2025) 的论点（accumulative training 不导致 collapse）对本文方法在 realistic web-scale 设置中的适用性有何影响？
3. 是否考虑过从 Dohmatob (2024) 尾部缩放律 formally derive EDD 的理论下界？

---

## Missing References

1. **Schaeffer, R., Balestriero, R., & LeCun, Y. (2025).** "Model Collapse Does Not Mean What You Think." [Must-Fix]
2. **Frank, E. & Hall, M. (2001).** "A Simple Approach to Ordinal Classification." [Should-Fix]
3. **Rennie, J. & Srebro, N. (2005).** "Loss Functions for Preference Levels: Regression with Discrete Ordered Labels." [Should-Fix]

---

## External Review (Stanford Agentic Reviewer)

外部审稿：pending（已请求，截至报告提交时未返回）

---

## Overall Assessment

**Score**: Borderline (weak accept for Findings, borderline reject for Main Conference)

**置信度**: High (6 轮审稿积累，两位 Reviewer 高度收敛)

**详细评分**：
- Soundness: 3.5/5 — 方法论合理、实验 solid，但 LoRA rank 和 single-generator 未验证
- Novelty: 3/5 — 新任务定义有价值，但 core method (perplexity tail → RF) 在知晓 Dohmatob (2024) 后 conceptually straightforward
- Excitement: 3/5 — 系统性好但 practical deployment 受限于 strategy-dependence 和 FPR
- Reproducibility: 4.5/5 — 完整超参报告 + code release promised
- Presentation: 3/5 — Abstract 过载、novelty framing 不清晰、文献有遗漏

**推荐**：
- **EMNLP Findings**: Accept（任务定义新颖 + 系统性实验 + 诚实 Limitations）
- **EMNLP Main Conference**: Borderline reject（novelty framing 不清晰、理论深度有限、practical gaps）

**升级路径**（若要争取 Main Conference）：
1. 补 LoRA rank ablation（消除 capacity artifact 疑虑）
2. Introduction 加 explicit novelty bridge vs Dohmatob
3. 引用并讨论 Schaeffer et al. counterargument
4. 精简 Abstract

---

## 变化追踪（Round 5 → Round 6）

| 类别 | Round 5 | Round 6 | 变化 |
|------|---------|---------|------|
| Critical open | 3 | 0 | 全部降级或解决 |
| Must-Fix | — | 2 (引用错误+文献遗漏) | 新发现 |
| Should-Fix | 8 | 7 | 5 resolved, 4 new/continued |
| Minor | 3 | 5 | +2 new |
| Overall | 3.0/5 | 3.0/5 | 稳定 |

论文经 6 轮审稿已趋于稳定。核心技术贡献 solid for Findings，但 Main Conference 需要更清晰的 novelty differentiation 和若干 targeted fixes。