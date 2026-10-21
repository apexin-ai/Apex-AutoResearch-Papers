---
round: 20
review_mode: fresh
overall_score: 3.0 — Findings
timestamp: 2026-05-19T00:42:59.653562+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# Round 20 (Fresh) 审稿报告 — gen-depth-fingerprint

**论文**: Depth Profiling: Classifying Recursive Generation Depth in Base LLM Text Chains
**Venue**: EMNLP 2026 via ARR (deadline 2026-05-25)
**审稿模式**: Fresh (重新审稿)
**Reviewer 编排**: R1 (方法严谨性+实验设计) + R2 (新颖性+完整性+写作)
**交叉回应**: 已完成，1 轮收敛

---

## Summary

本文提出 generation depth classification，将 LLM 文本按递归生成步数分为 gen-0/gen-1/gen-2+ 三类（仅限 base pretrained models）。核心发现是 Differential Depth Response (DDR)：7 个手工特征按深度响应分为 drifting (|ρ|>0.60)、intermediate、near-stationary (|ρ|<0.10) 三组。使用 XGBoost 在 8-generator LOGO 评估下 binary F1=0.694 (95% CI [.688,.700])。附录覆盖 LOFO、温度敏感性、跨域、QLoRA、下游效用等大量消融实验。

---

## Strengths

1. **问题定义有价值**: 将 LLM 文本检测从 binary 推进到 ordinal depth classification，问题自然且尚未被充分探索。DDR 三分将特征按行为模式分组的思路有概念吸引力。[R1-S1, R2 在交叉回应中未反驳]

2. **评估协议严谨**: LOGO 排除 generator-level 泄漏；独立种子实验确认 seed sharing 对 binary task 影响可忽略 (Δ=1.4pp)；LOFO 评估确认跨 family 迁移。[R1-S2, R2-优势1]

3. **消融实验覆盖全面**: LOFO、特征子集、分类器对比、扰动鲁棒性、跨域、QLoRA 端到端、下游效用、温度敏感性等多维度消融，显著超越同类 empirical 论文。[R1-S3, R2-优势5]

4. **统计方法规范**: Bootstrap CI、Cohen's d、TOST equivalence、Bonferroni correction、KS tests 等全套统计检验。[R2-优势2]

5. **诚实的范围界定**: Limitations 涵盖 base-model scope、instruct 退化、温度敏感性、scale gap、语言限制，Discussion 明确标注 DDR 为 "parameter-dependent phenomenon"。[R1-S4, R2-优势3]

6. **写作质量良好**: 无 AI 写作痕迹（无 em-dash、无 Furthermore/Moreover 堆砌），段落合理，专有名词有定义。[R2-优势4]

---

## Weaknesses (按严重性排序)

### Must-Fix [consensus] — 两位 Reviewer 均 AGREE

**MF1** [critical] **DDR 三分阈值为 post-hoc 选择，缺乏先验依据**
- |ρ|>0.60 / |ρ|<0.10 之间 6 倍间距恰好分 3/1/3，强烈暗示阈值根据数据事后选定。±0.10 sensitivity analysis 仅证局部稳定性，存在循环论证风险。DDR 分组实际依赖 ρ、d、Levene、CV shift 四个统计量的 "convergence"，但 convergence 未形式化定义。Scatter plot 视觉 gap ≠ 统计显著分组。
- **历史**: R18 首次标记，R19/R20 持续标记。论文已做 sensitivity analysis + TOST + scatter plot + 降级为 "empirical descriptive framework"，但阈值先验依据仍缺。
- **建议**: (a) holdout generator 子集上选阈值，另一子集验证；(b) 引用 Cohen 标准并论证偏离理由；(c) 或 data-driven clustering on (|ρ|, d) space 并报告最优 k。

**MF2** [critical] **特征冗余严重削弱 DDR 结构叙事**
- TTR/hapax r=0.97 几乎完全冗余，drifting 组独立信号仅约 2 个。entropy_min LOFO ΔF1=+0.01pp 零贡献但被保留。DDR 实际为 ~2 drifting signals / 1 intermediate / ~2 near-stationary + 1 borderline (tail_decay)，而非论文呈现的 clean 3/1/3。
- **建议**: (a) DDR 叙事改用 effective signal count (~2/1/~2)；(b) entropy_min 标为 redundant backup；(c) 报告合并 TTR+hapax 后的 DDR 和分类性能。

**MF3** [critical] **tail_decay TOST 仅 4/8 generator 通过，near-stationary 标签不稳健**
- tail_decay |d| 范围 0.07-0.22，半数 generator 展现统计显著深度效应。Pooled d=0.08 掩盖 generator-level 异质性 (Simpson's paradox 风险)。即使 tail_decay 重归类，entropy_min(8/8)+entropy_max(6/8) 保留两个较稳健 near-stationary 成员，DDR 不完全瓦解但退化为 messy 分组。
- **建议**: tail_decay 重分类为 borderline/conditional near-stationary；或在 DDR 叙事中 explicit 标注 4/8 限制。

**MF4** [critical] **Introduction 动机与 downstream negative result 自我矛盾**
- Introduction 以 data provenance / training pipeline 为核心动机，但 Appendix L 显示 random subsampling (ppl=2.367) 优于 depth-aware curation (2.387)。Discussion 第 8 页才重定位为 "diagnostic not prescriptive"——关键定位出现太晚。
- **历史**: R17 首次标记，R18-R20 持续标记。论文已多次调整但 Introduction framing 仍以 provenance/pipeline 为主。
- **建议**: (a) Introduction 重构为 "scientific understanding of recursive generation dynamics"；(b) downstream null result 在 Introduction 预告；(c) 正面 framing: "depth affects surface statistics but not functional quality"。

### Must-Fix [divergent] — R2 标记但 R1 反驳

**MF5** [critical, 分歧] **方法论零新颖性**
- R2 判定 7 标准特征 + XGBoost 无方法论贡献，DDR 本质为 effect-size 分析。R1 反驳：问题定义 (depth classification) 和经验发现 (DDR) 本身有价值，ACL/EMNLP 接收 empirical 论文。
- **Director 评估**: R1 的反驳有道理——问题定义是非平凡贡献。但 R2 的担忧也有实质性：如果核心 empirical finding 的统计基础 (MF1-MF3) 存在问题，且无方法论创新兜底，论文的接收风险较高。

**MF6** [warning→分歧] **Base-model-only scope 实用性**
- R2: instruct F1=0.338, 30% 错分率不可部署。R1 反驳: 标题已含 "Base LLM"，论文定位 empirical characterization 不需部署标准。
- **Director 评估**: R1 反驳合理——empirical study 不必满足部署标准。但 Abstract 应更早标注 scope。降级为 warning。

**MF7** [warning, 分歧] **相对并行工作增量不足**
- R2: Broken Telephone + Markovian Chains 已得出 ~3 类上限。R1 反驳: non-paraphrastic chains 测试不同生成过程，DDR 提供独有可解释性；R2 关于作者重叠的指控违反 blind review 规范。R1 同意 head-to-head 对比会加强论文。
- **Director 评估**: R1 对 blind review 违规的指出正确。增量论述需加强但非 must-fix。降级为 warning。

### Should-Fix [consensus]

**SF1** [warning] 温度限定未在 Abstract 充分标注 — Abstract 应前置 "under standard decoding (t≤0.7)"
**SF2** [warning] Generator subset 不一致 (5/6/8-gen) — §3.4 已有说明但不够显著，需 mini-table 汇总
**SF3** [warning] 下游 TOST n=3 统计功效不足 — Cohen's d 被 inflate 至 86.0/119.7，结论应降级为 preliminary observation
**SF4** [warning] 跨域温度 confound — cross-domain 用 t=1.0 vs 主实验 t=0.7，需显著声明
**SF5** [warning] TOST ε=0.20 缺乏领域论证 — 需 SESOI 分析或 NLP 领域先例
**SF6** [warning] DDR location/shape 解释缺乏理论基础 — 需形式化分析或标注为 empirical interpretation
**SF7** [warning] Related Work 对 multi-class detection 讨论不足 — Beyond Binary (Cheng et al. 2025) 等应详细对比
**SF8** [warning] Table 1 vs Table 2 指标差异 (macro vs pooled) 需在正文解释
**SF9** [warning] Appendix N/U 未在正文被 \ref 引用
**SF10** [warning] Limitations L15 仍含 unsupported paraphrastic 数字 (0.671/0.749)

---

## Reviewer Consensus

### [AGREE] 双方共识的关键问题：
1. DDR 阈值 post-hoc 无先验依据 (MF1)
2. 特征冗余使 DDR 实际为 ~2/1/~2 (MF2)
3. tail_decay near-stationary 标签不稳健 (MF3)
4. Introduction 动机与 downstream 矛盾 (MF4)
5. DDR location/shape 缺理论基础 (SF6)
6. 温度限定不充分 (SF1)
7. 下游 TOST 统计功效不足 (SF3)
8. 跨域温度 confound (SF4)
9. TOST ε=0.20 无领域论证 (SF5)
10. Generator subset 说明不够显著 (SF2)
11. Multi-class related work 覆盖不足 (SF7)

### [REBUT] 分歧及 Director 裁决：
1. **方法论新颖性** (MF5): R2 判定零新颖性，R1 反驳问题定义有价值。→ Director 评估：问题定义是非平凡贡献，但需 MF1-MF3 修复后才能有效支撑 empirical 论文的接收。
2. **Base-model scope** (MF6): R2 判定实用性不足，R1 反驳 empirical study 不需部署标准。→ Director 降级为 warning，要求 Abstract 前置 scope。
3. **并行工作增量** (MF7): R2 判定增量不足，R1 反驳差异非仅 scope 且指出 blind review 违规。→ Director 降级为 warning，建议 head-to-head 对比。
4. **3-class F1 bias** (R2-W1): R2 认为反复出现，R1 反驳处理充分。→ Director 裁定论文处理基本充分（binary F1 为 primary metric），不列为独立问题。
5. **附录庞大** (R2-W5): R2 认为过度，R1 逐一核查多数有引用。→ Director 裁定仅需补充 Appendix N/U 的引用 (SF9)。
6. **Lakens 引用** (R1-MR): R1 称缺少，R2 反驳论文已引用。→ R2 正确，论文已在 Appendix T/L 引用 `\cite{lakens_equivalence}`。

---

## Questions to Authors

1. DDR 阈值 |ρ|=0.60 / |ρ|=0.10 是在特征计算前预设还是观察数据后选定？如果有先验依据，请提供引用。
2. 如果移除 entropy_min 并将 TTR/hapax 合并为一个复合特征，DDR 框架和分类性能是否有实质变化？
3. Appendix L 下游实验如果增加到 n≥10 seeds，作者是否预期 null result 结论会改变？
4. Binary F1=0.694 (30% 错分率) 在什么具体应用场景下是 actionable 的？能否给出 corpus-level flagging 的具体 use case 和所需 precision/recall 阈值？
5. DDR 在 instruct models 上是否存在？Table 12 显示 6/7 特征方向反转，是否意味着 instruct tuning 下 DDR 不成立？如果 DDR 非递归生成固有属性，其理论意义如何？

---

## Missing References

1. **Cheng et al. (WWW 2025)** "Beyond Binary: Towards Fine-Grained LLM-Generated Text Detection via Role Recognition and Involvement Measurement" — 已引用但讨论过于简略，作为最直接的 beyond-binary 前作应详细对比
2. **"Two Birds with One Stone" (2025)** — multi-task detection + attribution 框架，应讨论与 depth classification 的关系
3. **"Beyond the Final Actor" (2026)** — fine-grained detection，应讨论

引用核查：67 条 bib entries 无虚构引用。7 条 OpenAlex "not_found" 和 5 条 "mismatch" 经人工判断均为 API 索引问题（DetectGPT, Pythia, XGBoost 等），非引用造假。

---

## External Review (Stanford Agentic Reviewer)

项目未配置外部审稿 (`external_review.paperreview_ai.enabled` 未设置)。未触发外部审稿流程。

---

## Overall Assessment

**R1 评分**: 3.0 (Findings) — Soundness 3.0, Excitement 2.5, Reproducibility 4.0, Confidence 4/5
**R2 评分**: 2.5 (Borderline Findings) — Soundness 3.0, Excitement 1.5, Confidence 4/5

**综合评分**: **3.0 (Findings)**

**评分依据**:

论文在问题定义 (depth classification)、实验设计严谨性 (LOGO/LOFO/seed control/length confound 等多层验证)、统计规范性和诚实的范围界定方面表现优秀，这些是其达到 Findings 门槛的基础。

但存在 4 个共识 Must-Fix 问题：DDR 框架的阈值缺乏先验依据 (MF1)、特征冗余使 DDR 结构从 clean 3/1/3 退化为 ~2/1/~2 (MF2)、tail_decay near-stationary 标签在半数 generator 上不成立 (MF3)、Introduction 动机与 downstream 矛盾 (MF4)。这些问题的核心在于：**DDR 是论文唯一的 intellectual contribution，但其统计基础存在多处需要修补的问题**。

关于 R1 (3.0) 与 R2 (2.5) 的分差：R1 侧重方法论严谨性，认为 DDR 统计问题可修复、问题定义有独立价值；R2 同时考虑 novelty/impact，认为即使统计问题全修复，方法论零创新 + downstream 为负 + instruct 不可用的组合仍不足。Director 裁定：问题定义构成非平凡贡献，实验工程扎实，在 MF1-MF4 修复后可达到 Findings 水平。但若 DDR 统计基础无法修补（如 holdout 验证失败），则论文降级至 Borderline Findings。

**投稿建议**: 当前版本可作为 Findings 候选提交，但需优先处理 MF1 (阈值验证) 和 MF4 (动机重构)。MF2 和 MF3 可通过 DDR 叙事调整解决，无需新实验。SF1-SF10 均为写作层面修改。

---

## Detailed Comments

### Abstract (abstract.tex)
- "base (pretrained) models" 在第 7 行才出现，应前移至第 2-3 行
- "under standard decoding (t≤0.7)" 限定已存在，位置适当

### Introduction (introduction.tex)
- 动机以 data provenance/training pipeline 为主 (L7: "re-enters training pipelines at scale")，但 downstream 实验否定该承诺。需重构为 scientific understanding
- Contribution 列表仅 2 条，且均为 empirical，对 Findings 级别论文来说偏少

### Method (method.tex)
- §3.3 已加 "selected a priori" 声明和 r=0.97 acknowledgment (L65-69)，这是 R19 修改的成果
- §3.4 已有 3-tier subset 说明 (L75)，但需更显著化

### Results (results.tex)
- Table 1 vs Table 2 指标差异 (macro vs pooled) 仅在 Table 2 caption 解释，需在正文段落说明
- §4.2 prompt-type sensitivity 中 "near-paraphrastic settings approach detection floor" 的 qualitative 描述适当

### Discussion (discussion.tex)
- DDR 已降级为 "empirical descriptive framework" 和 "parameter-dependent phenomenon"，这些是 R18-R19 修改成果
- Location/shape 解释 (L1-6) 作为 post-hoc interpretation 可接受，但不应作为 novelty claim

### Limitations (limitations.tex)
- L15 仍含 paraphrastic F1=0.671/0.749，需与 results.tex 同步更新
- 整体覆盖全面

### Appendices
- Appendix L (downstream): n=3 seeds 的 TOST 结论应降级
- Appendix T (TOST): ε=0.20 需领域论证
- Appendix N/U: 需在正文添加 \ref 引用

### 格式合规
- 正文 8 页 ✅
- ACL [review] 模板 ✅
- 匿名化完整 ✅
- Limitations section ✅
- 行号 ✅
- Ethics Statement ✅