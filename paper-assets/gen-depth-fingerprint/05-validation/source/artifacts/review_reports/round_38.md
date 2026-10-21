---
round: 38
review_mode: fresh
overall_score: 3.0 (Findings)
timestamp: 2026-05-21T05:13:27.639830+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告 — Round 38 (Fresh Review)

**论文**: Depth Fingerprinting: Detecting Recursive Generation Depth in LLM Text Chains
**目标 venue**: EMNLP 2026 (via ARR, Long Paper)
**审稿人**: Reviewer 1 (方法严谨性/实验设计) + Reviewer 2 (新颖性/完整性/写作)
**审稿轮次**: 1 轮独立审稿 + 1 轮交叉回应，已收敛

---

## Summary

本文提出 differential depth response (DDR)——递归 LLM 生成链中 NLL location 特征随深度单调漂移而 shape 特征保持近平稳的非对称现象。基于此观察构建 7-feature XGBoost ensemble，在 8 个 base-model generators / 5 families 上实现 LOGO binary F1=0.694 (gen-1 vs gen-2+)。实验方法论严谨（TOST 等价性检验、bootstrap CI、LOGO 交叉验证、21 页消融附录），但核心限制在于 base-model-only scope（instruct 模型上 DDR 反转）、相对于 model collapse 文献的增量新颖性定位不清晰、以及 "formalize" 等 framing 措辞与实际贡献不匹配。

---

## Strengths

1. **DDR 分解具有分析洞察力**：location drift vs shape stability 的正交分解提供了可测试假设，解释了为何无需 per-generator calibration 即可跨生成器检测深度 (§4.2, Figure 1-2)
2. **统计方法论在 NLP 实证论文中属上等水平**：TOST 等价性检验验证 near-stationary（非仅依赖 "不显著"）、Cohen's d + Cliff's delta 多指标收敛、bootstrap CI、LOGO + LOFO 双层评估
3. **评估框架系统性覆盖关键 confounds**：length-matching (App B)、prompt generalization (App C)、temperature sensitivity (App H)、random/LLM perturbation robustness (App I)、cross-domain (App J)、seed complexity (App T)
4. **Baseline 对比公平**：Table 3 在相同 LOGO 框架下重评 4 个 detection methods，7-feature ensemble 与 4-det ensemble 性能相当 (0.705 vs 0.706)，诚实呈现
5. **深度分类是文献中的新颖任务**：超越 binary human-vs-machine detection 至 ordinal depth estimation，与 data provenance 直接相关
6. **可复现性强**：特征提取、模型配置、计算预算描述详尽；承诺开源；reference model 公开
7. **引用覆盖全面**：67 条引用经验证无虚假，覆盖 AI text detection / model collapse / iterative generation / authorship attribution 等方向

---

## Weaknesses

### Must-Fix (影响接收决定)

**[W-Critical-1] Base-model-only scope 严重削弱泛化价值 [共识: R1+R2]**
- Appendix K: instruct 模型 DDR pattern 部分反转（entropy mean ρ 极性反转），silhouette 0.660→0.372
- 仅 2 个 ≤1B instruct 模型，证据基础过于薄弱，未区分 SFT vs RLHF 影响
- Abstract/Conclusion framing 过于宽泛（"When LLM outputs re-enter generation pipelines..."），可能误导读者认为 claims 适用于所有 LLM
- 实际场景中绝大多数 LLM 生成内容来自 instruction-tuned/chat models
- **建议**: Abstract/Conclusion 明确限定 base-model scope；Appendix K 核心发现提升到 Discussion；分析 instruct DDR 反转原因

**[W-Critical-2] DDR "formalize" 名不副实——缺数学定义 [共识: R1+R2, severity 分歧]**
- Abstract 说 "we formalize this asymmetry as DDR"，但全文无数学定义或理论推导
- DDR 实际是用 Cohen's d 阈值 (|d|>0.6 / |d|<0.11) 的经验分类
- location vs shape 命名缺理论依据——entropy_std 是 scale 参数而非 shape 参数
- §5 "autoregressive compression" 解释是非形式化直觉
- R1 标 critical（核心贡献声称），R2 标 major（writing fix 即可）
- **建议**: "formalize" → "characterize"；或给出 DDR 数学定义和统计判别准则

**[W-Critical-3] 新颖性相对 model collapse 文献定位模糊 [共识: R1 AGREE with nuance]**
- DDR 核心观察（递归生成导致 distributional compression）在 Shumailov et al. (2024) / Geng et al. (2026) 已有广泛讨论
- §5 试图区分 DDR 与 model collapse（推理时 vs 训练时），但这是 setting 区别而非 mechanism 区别
- 最有说服力的贡献是 location/shape 分解 + cross-generator generalization without calibration，但 Introduction 不够突出
- **建议**: Introduction 坦诚定位为"已知 distributional compression 现象在 detection task 上的精细分解和应用"

### Should-Fix

**[W-Major-1] 深度分辨率实际仅 3 类，标题存在 overclaim 风险 [分歧: R1 critical / R2 minor]**
- 实际分辨率: gen-0 / gen-1 / gen-2+。Appendix D 5-class F1≈0.50，gen-2/3/4 几乎无法区分
- R2 反驳: 副标题 "Classifying Recursive Generation Depth" 准确；正文已限定；3-class 本身有意义
- **建议**: Abstract 加一句明确 3-class 分辨率（不需改标题）

**[W-Major-2] Continuation-chain 与真实递归生成场景差距未讨论 [共识]**
- 固定 prompt "Continue the following text:" 构建深度链
- 3 种 prompt 类型 (continuation/elaboration/inspired) 均属 open-ended continuation 变体
- 未覆盖: instruction-following chains、multi-turn 对话、混合模型链、反复润色等真实场景
- **建议**: Discussion 明确讨论场景差异

**[W-Major-3] Cohen's d 阈值缺乏 sensitivity analysis [共识]**
- |d|>0.6 (drifting) 和 |d|<0.11 (near-stationary) 无理论依据
- Appendix U 仅覆盖 near-stationary 边界 (ε∈{0.15,0.20,0.25})，未覆盖 drifting 边界
- **建议**: 补充完整 threshold sweep

**[W-Major-4] 7 特征选择缺乏系统化论证 [部分共识]**
- 未报告初始候选集合及筛选过程
- 未考虑 NLL skewness/kurtosis/分位数差等替代特征
- entropy_min LOFO drop≈0.01pp，R2 解释其保留是为完整表征 DDR partition 而非分类性能
- **建议**: §3.3 报告候选特征集和排除理由

**[W-Major-5] 关键负面结果过度依赖附录 [部分共识: R1 部分 REBUT]**
- Instruct DDR 反转 (App K)、cross-domain F1 drops to 0.62-0.65 (App J) — 应提升到正文
- R1 REBUT: length confounding 和 downstream 放附录合理
- **建议**: 至少将 instruct 结果和 cross-domain 结果的关键数字移入 Discussion

### Minor Issues

**[W-Minor-1]** Figure 1 出现在第 6 页，前 3 页连续纯文本无任何 display item（视觉审查+两位 Reviewer 共识）
**[W-Minor-2]** 术语一致性: DDR 同时指 pattern 和 partition；"generation depth" vs "recursive generation depth" 交替
**[W-Minor-3]** Table 3 numbering: Table 3 出现在 Table 2 之前（可能是 float 位置问题）
**[W-Minor-4]** Granger 因果分析仅 5 个时间点，统计效力存疑，应降格为 supplementary evidence

---

## Reviewer Consensus [AGREE]

1. **Base-model-only 是最大结构性限制**：instruct DDR 反转、证据基础薄弱、framing 过于宽泛 — 两位 Reviewer 的最高优先共识
2. **"formalize" 应改为 "characterize"**：DDR 是经验观察而非数学框架
3. **Cohen's d threshold sensitivity 缺失**：drifting 边界未验证
4. **新颖性定位应更坦诚**：DDR 是已知现象的精细分解和检测应用
5. **实验覆盖的全面性是论文强项**：21 页附录系统性排除混淆因素

## Reviewer Divergence [分歧]

1. **标题 overclaim (R1-N2)**: R1 标 critical（3-class ≠ fingerprinting），R2 REBUT 为 minor（副标题准确，正文已限定）→ 记录分歧，建议 Abstract 补充分辨率限定即可
2. **Reference model 同族偏差 (R1-W6)**: R1 标 warning，R2 REBUT（Appendix S + Table 37 off-diagonal 0.810 已充分控制）→ R2 证据更有说服力，降为 minor
3. **"formalize" severity**: R1 标 critical（核心贡献声称），R2 标 major（writing fix）→ 采纳 R2 判断: major（修改措辞即可，不需重做实验）

---

## Questions (需作者澄清)

1. DDR 在 top-k / greedy / beam search 下是否成立？如果 shape stability 仅限 nucleus sampling，DDR 的普适性如何论证？
2. Instruct DDR 反转是否意味着 base 和 instruct 需要完全不同的 DDR partition？统一框架价值何在？
3. Per-generator CI 宽度达 0.213（如 Gemma-2-2B [0.521, 0.734]），是否反映样本量不足？
4. 是否尝试过更长的链（depth 10-20）？如果 autoregressive compression 趋于 attractor，shape features 是否最终也会 drift——使 DDR 成为 finite-depth 现象？
5. 与 Geng et al. (2026) 有无在相同数据/evaluation protocol 下的 detection accuracy 直接对比？

---

## Missing References

- **Pillutla et al. (2021)** — MAUVE: 生成文本分布偏移度量，可为 DDR location drift 提供理论支撑
- **Briesch et al. (2023)** — "LLMs Suffer From Their Own Output": 直接研究 LLM iterative generation 退化
- **Diaz & Karampatziakis (2019)** — "Soft Labels for Ordinal Regression": depth task 具有 ordinal 性质
- **Tulchinskii et al. (2024)** — "Intrinsic Dimension Estimation" (ICLR 2024): 几何/拓扑特征检测 AI 文本

---

## External Review (Stanford Agentic Reviewer)

外部审稿：未配置，跳过。

---

## Visual Layout Check (非评分项)

状态: **done** (耗时 ~4 分钟)

**Warnings (5)**:
1. Pages 1-3: 连续 3 页纯文本无任何 display item，审稿人前 2 分钟内无视觉锚点
2. Figure 1（核心结果图）出现在第 6 页，距正文开头太远——建议前移至 page 2-3
3. Table 3 出现在 Table 2 之前（float 位置导致编号乱序）
4. Page 7 单页包含 3 个 display items（Figure 2 + 表 + Figure 3），与 pages 1-3 极端反差
5. Page 33 末页 Table 42 仅占顶部 1/3，下方 60% 大面积空白

**Info (10)**: Figure 1 strip plot 清晰美观、表格 booktabs 规范、附录视觉节奏良好。Figure 13 热力图建议改用色盲友好色板。

---

## Overall Assessment

**Overall Score: 3.0 (Findings)**

| 维度 | R1 | R2 | 综合 |
|------|----|----|------|
| Soundness | 3.5/5 | 3/5 | 3.25/5 |
| Excitement | 3.0/5 | 3/5 | 3.0/5 |
| Confidence | 4/5 | 4/5 | 4/5 |
| Overall | 3.0 | 3.5 | **3.0** |

**评分理由**:

论文在实验方法论上表现出色——LOGO 交叉验证、TOST 等价性检验、系统性消融实验等在 NLP 实证论文中属于上等水平。DDR 分解（location drift vs shape stability）是一个有洞察力的经验发现，depth classification 作为超越 binary detection 的新任务具有学术价值。

然而，三个结构性问题阻止了 Conference-level 接收:

1. **Base-model-only 的致命限制**: 实际场景中 LLM 生成内容几乎全来自 instruct 模型，而论文证据显示 DDR 在 instruct 上反转——这不是可通过修改措辞解决的 framing 问题，而是方法适用性的根本限制
2. **增量新颖性**: DDR 的核心观察（递归生成压缩分布）在 model collapse 文献中已有讨论；论文贡献在于精细分解和检测应用，但 Introduction 将其包装为全新发现
3. **Framing 与实际能力不匹配**: "formalize"（实为经验分类）、"depth fingerprinting"（实为 3-class）、"surpassing baselines"（实与 4-det ensemble 持平）——多处措辞超出实验证据

综合评估: 论文适合 Findings track 接收。如能 (a) 坦诚重新定位 contribution（characterize not formalize, empirical analysis not detection method），(b) 将 instruct/cross-domain 负面结果移入正文，(c) 补充 threshold sensitivity，有望升至 3.5 Borderline Conference。

---

## Detailed Comments

### §1 Introduction
- "formalize" → "characterize" 或 "identify and quantify"
- 应更坦诚定位: DDR 是已知 distributional compression 在 depth detection 的精细分解
- 缺少 overview figure 导致前 3 页纯文本

### §3 Method
- §3.3 应报告初始候选特征集和筛选理由
- Reference model (Pythia-410M) 与 Pythia generators 同族的 caveat 应在此提及

### §4 Results
- Table 2 macro F1=0.762 vs Table 3 pooled F1=0.774 的切换需在正文明确解释
- Cohen's d threshold sensitivity: 建议在正文引用附录中的 threshold sweep（如补充）
- Figure 1 应前移至 Method 或 Results 开头

### §5 Discussion
- 需增加 instruct DDR 反转的关键数字（silhouette 下降、ρ 反转）
- 需讨论 continuation-chain vs 真实递归生成场景的差异
- 需讨论 downstream null result 的含义
- 与 model collapse 的区分应承认 shared mechanism 而非仅强调 setting 差异

### Abstract
- 加一句明确 3-class 分辨率
- "formalize" → "characterize"
- Binary F1 定义加 "(gen-1 vs gen-2+, excluding shared gen-0 seeds)"
- 最后一句 scope limitation 位置太靠后，容易被忽略