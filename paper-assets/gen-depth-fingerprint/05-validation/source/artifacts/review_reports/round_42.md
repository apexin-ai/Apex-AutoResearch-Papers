---
round: 42
review_mode: fresh
overall_score: 3.5 - Borderline Conference
timestamp: 2026-05-22T05:22:28.505079+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# Round 42 审稿报告 — Depth Fingerprinting

**论文**: Depth Fingerprinting: Classifying Recursive Generation Depth in Base-Model LLM Text
**Venue**: EMNLP 2026 via ACL Rolling Review (ARR Long Paper)
**截止日期**: 2026-05-25
**审稿模式**: Fresh（重新审稿）
**Reviewer 编排**: 2 名 Reviewer（R1: 方法严谨性+实验有效性; R2: 新颖性+完整性+表述质量）
**交叉回应**: 完成（R1→R2, R2→R1），1 轮即收敛

---

## Summary

本文提出 depth fingerprinting 任务——将 AI 文本检测从二元（human vs. machine）扩展为序数深度分类（gen-0 / gen-1 / gen-2+）。核心分析框架 Differential Depth Response (DDR) 将递归生成引起的分布偏移分解为 location 分量（entropy mean、TTR、hapax ratio 随深度单调漂移）和 shape 分量（entropy max/min、tail decay 保持近稳态）。基于 7 个手工特征的 XGBoost 分类器在 8 个 base-model 生成器（5 families, 0.6B–8B）的 LOGO 评估中达到 leak-free binary F1=0.694、3-class F1=0.762；QLoRA 端到端分类器达 3-class F1=0.905。附录 23 页涵盖 15+ 项消融分析。

---

## Strengths

**S1. 任务定义新颖且有意义。** 将 binary detection 推广到 ordinal depth classification 是自然但未被充分探索的方向。DDR 的 location/shape 分解概念简洁、直觉强，提供了理解递归生成动态的有用框架。[R1+R2 共识]

**S2. 统计方法论远超同类检测论文。** 综合使用 TOST 等价检验、Bootstrap CI + Bonferroni 校正、Granger 因果、PCA、排列重要性、Cohen's d 效应量。在 AI 文本检测领域罕见的严谨程度。[R1 主评]

**S3. 消融实验极为全面。** 23 页附录覆盖：LOFO、cross-group ablation、length confound、temperature sensitivity、prompt type、random perturbation、cross-domain、instruction-tuned models、cross-generator transfer、decoding strategy、9-generator scale validation、DDR partition validation 等。覆盖面之广在 empirical study 中少见。[R1+R2 共识]

**S4. 诚实的局限性报告。** 论文坦承 instruction-tuned models 下 depth signal 显著弱化、base-model-only scope、English-centric setup。3-class F1 的 gen-0 inflation 被明确讨论并给出 leak-free binary metric。[R1 主评]

**S5. Cross-reference 消融有效。** Appendix s (Table 26) 展示三个不同 family 参考模型的 LOGO F1 spread < 0.013，DDR partition invariant，证明 depth signal 不依赖特定参考模型家族。[R1+R2 共识]

**S6. Concurrent work 结构化对比。** Table 45 将本文与 Mohamed et al. (2025) 和 Geng et al. (2026) 按 chain type、feature space、analysis goal 等维度对比，清晰界定了独特贡献。[R2 主评]

---

## Weaknesses

### Must-Fix（影响接收决定）

**MF-1 [Critical, 共识] DDR novelty 主要为 empirical observation，方法论贡献有限。**
DDR 核心是一个 empirical finding（不同特征以不同速率随深度变化）+ 标准分类 pipeline（7 feature + XGBoost）。Section 5 的理论推导（nucleus sampling → self-typicality → entropy compression）仅为定性叙述，缺乏 formal derivation。论文贡献在于 task definition + analytical insight，但不应 overclaim 为 methodological innovation。R1 补充：ARR 明确允许 diverse paper types，empirical-analytical 论文贡献在于 insight 而非 algorithm——但这将论文推向 Findings 而非 Conference。
- **位置**: Section 1 (contributions), Section 4.2, Section 5
- **Issue ID**: R42-N1

**MF-2 [Critical, 共识] Instruction-tuned models 下 DDR 结构性失效 + scope 前置不足。**
Appendix k 显示 instruction-tuned OLMo-2-1B 的 binary F1→0.487（近随机），DDR silhouette 0.37→0.07，部分特征 ρ 极性反转。这不仅是 performance degradation，而是 DDR 框架在 instruction-tuned setting 下的结构性失效。Footnote 1 的 scope limitation 太不显眼——Introduction 前两段 general motivation（"data curation and collapse prevention"）给读者通用框架印象。
- 建议: (1) Intro 更前置 scope limitation; (2) 讨论 *why* instruction tuning 破坏 signal（RLHF KL-regularization? SFT distribution matching? format constraints?），给出 testable hypothesis; (3) 明确 base-model 场景的具体实用价值（synthetic data pipeline, pretraining corpus auditing）
- **位置**: Footnote 1, Appendix k (Table 17-19), Introduction, Limitations
- **Issue ID**: R42-N2

**MF-3 [Critical, 共识] Claim scope 与 F1=0.694 performance 不匹配。**
Abstract "establishing the analytical framework as the primary contribution" 与正文多处实用化措辞矛盾（"enabling data curation and collapse prevention"、"depth estimation without per-generator calibration"）。F1=0.694 不足以实际 deploy。
- 建议: (1) 明确界定 analytical framework vs practical tool 的 claim boundary; (2) Discussion 坦率讨论 F1=0.694 实用局限; (3) 正面论证 DDR 的独立分析价值（即使分类性能有限，DDR decomposition 对理解递归生成动态仍有贡献）
- **位置**: Abstract, Section 1, Section 5, Section 6
- **Issue ID**: R42-N3

### Should-Fix（影响评分但不一票否决）

**SF-1 [Major→Minor, R1 提出 major / R2 rebut→minor] "What is preserved" 叙事 overselling。**
Table 28 的 |ρ| 值（entropy_min=0.02, entropy_max=0.04, tail_decay=0.03）仅说明"弱相关"，"preserved" 暗示 mechanistic protection 无证据支持。Appendix v 的六重验证（k-means + threshold sweep + TOST + Granger + PCA + per-generator replication）部分弥补了论证。
- 建议: 将 "what is preserved" 降调为 "what remains approximately invariant" 或 "what drifts slowly"
- **位置**: Abstract, Section 1 para 2, Section 4.2, Section 5 para 1
- **Issue ID**: R42-W1

**SF-2 [Major, 共识] XGBoost-to-QLoRA gap ~11.6pp 未充分分析。**
7-feature XGBoost 3-class F1=0.789 vs QLoRA F1=0.905。论文仅称 "raw token embeddings contain depth signal beyond summary statistics"，未分析 QLoRA 额外捕获了什么。对 analytical framework 论文，~12pp 未解释信号是显著遗漏。R2 补充：gap 本身也是 positive signal——可 frame 为 "DDR features are interpretable proxies for a richer signal space"。
- 建议: probing/attribution analysis，或明确作为 future work + 承认 framework 覆盖局限
- **位置**: Appendix e (Table 7), Section 4.1
- **Issue ID**: R42-W2

**SF-3 [Major, 共识] Scale ≤8B 泛化性未充分论证。**
所有生成器 0.6B–8B，未测试 13B/70B+。Appendix z.5 仅加入同尺度 Gemma-2-2B。larger models 的 output distribution 更平滑、vocabulary coverage 更广，DDR 可能呈不同模式。
- 建议: Discussion 中明确讨论 (a) 为什么受限于 ≤8B; (b) larger models 的 testable predictions
- **位置**: Section 3.2, Appendix z.5, Limitations
- **Issue ID**: R42-W3

**SF-4 [Major, 共识] Downstream TOST n=3 统计功效极低。**
n=3 seeds 的 TOST 几乎无统计力证明效应不存在。等价结论可能仅因 underpowered 成立。整个 downstream experiment 规模不足以支撑 corpus curation 叙事。
- 建议: 增加 seeds 至 n≥10，或 Bayesian equivalence，或更保守表述（"no evidence of meaningful difference given limited power"）
- **位置**: Appendix m
- **Issue ID**: R42-W4

### Minor Issues

**MI-1 [Minor, 分歧→minor] DDR partition thresholds 主文引用 Appendix v 证据不足。**
R1 认为 7-point k-means 统计力有限（major）；R2 rebut 认为六重验证已充分，核心问题仅是主文引用不足（minor/presentation）。最终判定为 presentation issue。
- 建议: §4.2 更明确总结 Appendix v 的验证结果
- **Issue ID**: R42-W5

**MI-2 [Minor, 共识] "Ordinal classification" framing 与 3-class 实际分辨率存在 gap。**
5-class F1 降至 ~0.50，gen-3/gen-4 几乎不可区分。实际分辨率仅 3 级。
- 建议: 明确 practical resolution 限于 3 classes，调整 framing 为 "coarse ordinal"
- **Issue ID**: R42-W6

**MI-3 [Minor, R2 提出 / R1 partial rebut] Entropy 术语指代 NLL 存在混淆。**
已有 explicit disclaimer (Section 3.3)，但 entropy_max/entropy_min 命名不标准。
- 建议: 改用 NLL 或 surprisal 更准确，但非必须修改
- **位置**: Section 3.3, Table 1

---

## Reviewer Consensus

两位 Reviewer 在以下关键问题上达成完全一致 [AGREE]：

1. DDR novelty 主要是 empirical observation，非 methodological innovation
2. Instruction-tuned models 下 DDR 结构性失效，限制实际影响力
3. Claim scope 与 F1=0.694 不匹配，proof-of-concept 定位摇摆
4. XGBoost-QLoRA gap ~12pp 未充分解释
5. Scale ≤8B 泛化性未充分论证
6. Downstream TOST n=3 underpowered
7. 3-class 分辨率 vs "ordinal" framing 存在 gap
8. "What is preserved" 叙事需降调

---

## Reviewer Divergence

**唯一分歧**: DDR partition thresholds justification 的严重性评估
- R1: [Major] — 7-point k-means 统计力有限，阈值来自外部惯例
- R2: [REBUT→Minor] — Appendix v 六重验证（k-means + threshold sweep + TOST + Granger + PCA + permutation importance）已充分，核心问题仅是主文引用不足

**Director 判定**: 采纳 R2 的降级意见。证据存在且充分，问题在于 presentation 而非 substance。标记为 Minor/Presentation issue。

---

## Questions for Authors

1. **QLoRA 额外信号来源** [R1+R2]: 11.6pp gap 是否意味着 DDR 7-feature 有 systematic blind spot？能否通过 probing/attention analysis 定位 QLoRA 额外利用了什么（sequential patterns? stylistic features? sub-word signals?）？
2. **Instruction-tuned 失效机制** [R1+R2]: 是 RLHF 的 KL-regularization 平滑了 depth-specific NLL patterns，还是 instruction following 的 format constraints 覆盖了 depth signal？是否测试过 SFT-only models（无 RLHF）以隔离因素？
3. **Ordinal regression** [R1, R2 同意]: 为什么不使用 ordinal-specific methods（CORAL, CORN）？confusion matrix 显示错误集中在相邻深度——ordinal regression 可能利用这一结构。
4. **更大参考模型** [R1+R2]: 三个参考模型均 ≤1B，3B 或 7B 级参考模型是否改变 DDR pattern 或提升 depth discrimination？
5. **DDR vs model collapse** [R2, R1 rebut]: Section 5 的区分已 adequate，但能否提供更 formal 的区分框架？

---

## Missing References

以下为建议性引用，不影响评分：
- Varshney et al. (2020) "Limits of Detecting Text Generated by Large-Scale Language Models" — 检测信息论下界与 depth fingerprinting 理论极限相关
- Ippolito et al. (2020) "Automatic Detection of Generated Text is Easiest when Humans are Fooled" — 检测难度与生成质量关系
- Shi et al. (2024) 与本文的方法论关联讨论可加强（同为 reference-model NLL approach）

---

## External Review (Stanford Agentic Reviewer)

**状态**: 未请求（项目配置未启用外部审稿）

---

## Visual Layout Check（非评分项）

**状态**: 超时（Agent 在 300s 后 timeout）
视觉审查 Agent 启动但在规定时间内未完成。未产出可用 findings。用户可选择在后续轮次手动重新触发。

---

## Overall Assessment

### 维度评分（两位 Reviewer 加权综合）

| 维度 | R1 | R2 | 综合 | 理由 |
|------|----|----|------|------|
| **Soundness** | 3.5/5 | 3.5/5 | **3.5/5** | 统计方法论扎实，LOGO + Bootstrap + TOST 规范。扣分: TOST downstream n=3 underpowered; DDR 缺 formal theory; claim scope 过宽 |
| **Excitement** | 3/5 | 3/5 | **3/5** | DDR 框架新颖，task definition 有价值。但 base-model-only + instruction-tuned 失效 + F1=0.694 中等性能共同限制了兴奋度 |
| **Reproducibility** | 4/5 | 4/5 | **4/5** | 特征定义清晰，评估协议详尽，超参数完整。代码承诺公开。扣分: 部分种子/split 信息不完整 |
| **Confidence** | 4/5 | 4/5 | **4/5** | 两位 Reviewer 均仔细审阅 35 页全文（正文 + 23 节附录），领域熟悉 |

### Overall: **3.5 — Borderline Conference**

**一句话总结**: 一篇方法论严谨、消融全面的 empirical-analytical 论文，DDR 框架提供了有价值的分析视角，但 novelty 主要为 empirical observation、base-model-only scope 限制实际影响力、F1=0.694 的 proof-of-concept 定位与部分实用化措辞不匹配，使其处于 Conference/Findings 边界。

**推向 Conference (4.0) 的因素**:
- Task definition genuinely novel（binary → ordinal depth classification）
- DDR decomposition clean 且可验证，有独立 analytical 价值
- 实验方法论远高于同类检测论文平均水准
- 附录消融完整度罕见（23 页, 15+ 项分析）
- Concurrent work 结构化对比和诚实的局限性报告

**推向 Findings (3.0) 的因素**:
- Core method（7 feature + XGBoost）完全标准，novelty 在 insight 而非 algorithm
- Base-model-only scope 在 instruction-tuned LLM 主导时代应用场景狭窄
- Instruction-tuned models 下 DDR 结构性失效（非仅 performance 下降）
- XGBoost-QLoRA gap ~12pp 暗示 interpretable framework 只覆盖部分信号
- "What is preserved" 叙事 overselling
- Scale ≤8B 泛化性未充分论证

### Rebuttal 关键路径

如果作者在 rebuttal 中能：
1. **收窄 claim scope**: 明确 analytical framework 定位，降低实用化措辞
2. **降调 "preservation" 叙事**: 改为 "approximate invariance"
3. **解释 QLoRA gap**: 至少定性讨论 gap 来源，承认 framework 覆盖局限
4. **讨论 instruction-tuned 失效机制**: 给出 testable hypothesis（RLHF smoothing vs format constraints）
5. **补充 scale 讨论**: 明确 ≤8B 约束理由和 larger models 预测

则评分可上调至 **4.0 (Conference)**。当前状态下，**3.5 (Borderline Conference)** 更准确——如果 AC 更看重方法论创新和分析深度，可接收为 Conference；如果更看重 practical impact 和 novelty，则 Findings 更合适。

---

## Detailed Comments（逐节）

### Abstract
- 信息密度高，核心数字和 DDR 概念均包含
- "Differential depth response" 首次出现缺简要解释，对不熟悉读者造成障碍
- "what converges" vs "what is preserved" 对比缺足够上下文
- Base-model scope 在 title 中有但 abstract 正文中不够显眼

### Section 1 (Introduction)
- 叙事弧线 compelling：recycled content → binary detection 局限 → depth as missing dimension → DDR → contributions
- Footnote 1 的 base-model scope 太不显眼，应提升为正文 paragraph
- Contribution 3 "Scope characterization" 表述模糊，"identifying key challenges in instruction-tuned models" 在主文无相应讨论

### Section 2 (Related Work)
- §2.1-2.4 分类合理，覆盖充分
- §2.2 对 concurrent work 的定位清晰（non-paraphrastic continuation vs back-translation）
- §2.4 与 Shi et al. (2024) 的连接有趣但讨论不足

### Section 3 (Method)
- §3.1 任务形式化清晰
- §3.2 chain construction 合理；prompt 选择 ("Continue the following text:") 已在 Appendix c 充分消融（三种 prompt, cross-prompt LOGO F1=0.753）
- §3.3 特征设计逻辑清楚，Table 1 简洁有效
- §3.4 LOGO + XGBoost 评估方案标准且合适

### Section 4 (Results)
- §4.1: Seed sharing confound 讨论诚实（leak-free binary F1=0.694, independent-seed F1=0.680）
- §4.2: DDR formal definition 紧凑，Figure 2 可视化有效。但 Appendix v 的多重验证在主文引用不足
- §4.3: Baseline comparison (Table 3) 公平，同一 LOGO 框架下比较。Figure 3 有效展示 7-feature ensemble 优势

### Section 5 (Discussion)
- DDR 理论解释 plausible 但缺 formal 支撑
- "DDR is mechanistically distinct from model collapse" claim 需更强证据（当前仅定性描述）
- Downstream framing（corpus curation）缺主文实证支撑

### Section 6 (Conclusion)
- 简洁得当，主要 claims 准确概括
- "extending this signal to instruction-tuned models...remains the key open challenge" 恰当但过于泛泛

### Limitations
- 覆盖合理（base-model scope, English-centric, ≤8B, fixed decoding）
- 可加强 TOST 统计功效局限讨论
- 可更具体讨论 instruction-tuned 失效原因

### Ethics Statement
- 充分讨论 dual-use risk 和 deployment 建议

### 格式合规性
- ✅ 匿名: "Anonymous ACL submission"
- ✅ 页数: 正文 8 页 (pp.1-8)，Limitations 从 p.9 开始（不计入页数）
- ✅ References: pp.9-12，格式规范
- ✅ Limitations section: 存在且位置正确
- ✅ ACL style template