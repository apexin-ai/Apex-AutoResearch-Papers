---
round: 15
overall_score: 3.0
timestamp: 2026-05-18T08:34:12.416176+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# Round 16 合并审稿报告（Fresh Review）

**论文**: Depth Fingerprinting: Detecting Recursive Generation Depth in Base LLM Text Chains
**Venue**: EMNLP 2026 (ARR May 2026 cycle)
**Reviewer 编排**: 2 人（R1: 方法严谨性+实验验证, R2: 新颖性/完整性+写作质量/格式）
**流程**: Round 1 独立审稿 → 交叉分享（逐条 AGREE/REBUT）→ 收敛（1 轮达成共识）

---

## Summary

本文提出 generation depth classification 任务，将文本分类为 gen-0（人类）/ gen-1（首次 LLM 生成）/ gen-2+（递归生成），超越二分类 AI 文本检测。作者在 8 个 base model（5 个模型家族，0.6B-8B）上发现 differential depth response (DDR)：central-tendency 特征随深度单调漂移，shape 特征保持相对稳定。7 特征 XGBoost 集成在 8-generator LOGO 评估下达到 leak-free binary F1=0.694，cross-model chains 达到 0.764（5-generator 子集）。方法仅适用于 base model，instruction tuning 下信号严重退化。

---

## Strengths

**S1** [AGREE R1+R2] **任务定义具有原创性**。Generation depth classification（gen-0/gen-1/gen-2+）是对 binary AI-text detection 的有意义扩展，与 data provenance 和 model collapse 文献有明确连接点。

**S2** [AGREE R1+R2] **DDR 分析有洞察力**。Drifting vs stationary 特征分解提供了理解递归生成动力学的结构化框架，超越了 model collapse 文献中的聚合漂移观察。

**S3** [AGREE R1+R2] **实验设计严谨**。LOGO/LOFO 评估协议、seed demeaning、disjoint-seed 控制、length-matched subsampling 等 confound 控制体现了细致的方法论。Bootstrap CI、McNemar test、Bonferroni correction 使用规范。

**S4** [AGREE R1+R2] **附录全面**。18 个附录覆盖消融、敏感性、跨域、误差分析等，增强了结果可信度。

**S5** [AGREE R1+R2] **诚实报告局限性**。论文透明地报告了 instruction tuning 退化、scale effect、temperature sensitivity 和下游 null result。

**S6** [AGREE R1+R2] **写作质量良好**。AI 写作痕迹极少，叙事主线清晰，ACL 格式完全合规。

---

## Weaknesses

### Must-Fix（影响接收决定）

**MF1** [AGREE R1+R2] **DDR "comparatively stable" 措辞跨章节不一致 + 缺少 effect size**
- **Tracker**: R7-W2（reopened R16）
- Abstract/Introduction 使用 "location shift... whose shape remains comparatively stable" 作为核心理论支柱，但 §4.2 报告 Levene test 拒绝所有 feature 的等方差假设（p < 10⁻¹⁰），并将结论框定为 "practical characterization rather than strict invariance"。Abstract/Intro 呈现定性二分，§4.2 呈现定量连续体——构成内部不一致。
- 论文报告了 CV shift（<3% vs >15%）和方差比（0.98-1.12 vs 1.90-2.20），但缺少 Cohen's d 或 Glass's delta 等标准 effect size 指标。
- §5 从 softmax + fixed sampling → shape preservation 的推理链缺乏形式化或半形式化论证。
- **行动**: (a) 统一全文措辞为 "shape features drift at a substantially lower rate"（must-fix）; (b) 补充 Cohen's d（should-fix）; (c) 考虑 Ansari-Bradley test 分离 location/scale（nice-to-have）。

**MF2** [AGREE R1+R2] **Base-model-only 限制与 Introduction motivation 矛盾**
- **Tracker**: R7-W5（reopened R16）
- Title 已包含 "Base LLM"（R15 修复），但 Introduction §1 仍以 "7-17% of recent scientific papers and peer reviews contain substantial LLM-modified content" 开篇。这是 instruct-model 场景的证据，用于 motivate 一个仅在 base model 上有效的方法。
- Limitations 诚实承认 instruction tuning 退化（OLMo-Instruct LOGO F1=0.338 vs 0.763 base），但 Introduction 的 framing 创造了方法可检测真实世界 LLM 文本的预期。
- **行动**: Intro §1 重新排序——以递归生成动力学问题开场，"7-17%" 统计数据降级为背景证据而非核心 motivation。更早声明 base-model scope。

**MF3** [AGREE R1+R2] **Scale 声明限于 0.6B-8B，"scale effect" 结论过强**
- **Tracker**: R13-SF7（wont_fix due to compute, R16 再次标记）
- Binary F1 从 0.718-0.724（1-2.8B）退化至 0.633（Mistral-7B）。Discussion 和 Conclusion 语言暗示 DDR 为通用现象，但证据严格限于 0.6B-8B。
- 如果退化趋势外推至 70B+，方法可能降至 chance level。这不仅是 "长期可行性" 问题，而是 "当前可行性" 问题——最广泛使用的 LLM 远大于 8B。
- **行动**: 所有 scale-related 声明严格限定为 "within the 0.6B-8B range"。此条因计算约束无法通过新实验解决，但措辞必须调整。

### Should-Fix（影响评分）

**SF1** [R1: critical, R2: should-fix → 共识 should-fix] **KS test 无法验证 location/shape 分解**
- **Tracker**: R16-N1（new）
- KS test 对分布的任何差异敏感，无法区分 location/scale/shape 贡献。论文组合使用 Spearman + Levene + CV shift + KS，多检验组合提供合理证据。但 KS test 的局限性应显式说明。
- **行动**: 添加 KS test 为 omnibus test 的说明；考虑 Wilcoxon + Ansari-Bradley 补充（not blocking）。

**SF2** [AGREE R1+R2] **下游 QLoRA 实验为 negative result，削弱 practical utility 叙事**
- **Tracker**: R10-N3（resolved R15, R16 residual concern）
- Appendix L 结论 "data quantity dominates depth composition" 表明 depth-aware curation 无优势。实验规模小（3 seeds, 1 model, 5 variants）。
- 论文已将其移至 Appendix 并在 §4.3 诚实报告，但 Discussion 仍涉及 practical utility。
- **行动**: 确保 Discussion 中 practical utility 叙事与 null result 一致。

**SF3** [AGREE R1+R2] **与 concurrent work 区分不够充分**
- **Tracker**: R16-N2（new）
- Mohamed et al. (2025, "Broken Telephone", ACL 2025) 已验证存在且高度相关。论文 §2.2 用 ~2 段笼统区分，缺少逐条对比（task/chain type/method/findings）。
- R2 提到的 "Geng et al. (2026), Markovian Generation Chains" 需要验证存在性——R1 对此持保留态度。
- **行动**: 扩展 §2.2 concurrent work 比较；验证所有 cited concurrent papers 的真实性。

**SF4** [AGREE R1+R2] **Independent-seed 实验缺少 bootstrap CI**
- **Tracker**: R16-W1（new）
- F1 差异 0.005（0.694→0.689），无 CI 则 "consistent with cross-generator transfer" 为无依据断言。

**SF5** [R1: should-fix, R2: REBUT → 部分共识] **Baseline 比较维度不对称**
- **Tracker**: R14-W4（in_progress）
- R1: 7 features vs 4 features 给 tree-based model 更多分裂点。R2: 同一 XGBoost 框架确保公平的 feature informativeness 对比。
- **共识**: 框架本身公平，但 matched-dimensionality 消融（best 4 of 7）和简单阈值 baseline（如 entropy_mean threshold）会加强论证。

**SF6** [AGREE R1+R2] **gen-0 3-class F1 叙事残留**
- **Tracker**: R16-W2（new）
- Binary F1 为 primary metric（正确），但 3-class F1 仍出现在 Table 1 列标题和 §4.1 开头，缺少一致的 "inflated by gen-0 seed sharing" 说明。

**SF7** [AGREE R1+R2] **Table 1 vs Table 2 评估协议不同**
- **Tracker**: R16-W3（new）
- Table 1: 8-gen LOGO per-generator macro average。Table 2: pooled evaluation。不同 generator 子集。跨表对比困难。

**SF8** [AGREE R1, R2 nuance] **Wikipedia-only 主实验 + 小规模 cross-domain**
- 主实验: 1000 Wikipedia seeds。Cross-domain (Appendix): 3 domains × 200 seeds × 3 generators。
- Claim "signal not an artifact of Wikipedia" 需更大规模验证，或限定为 "preliminary evidence within formal English text"。

**SF9** [AGREE R1+R2] **Reference model 同家族潜在偏差**
- **Tracker**: R11-W1（reopened R16）
- Pythia-410M 与 Pythia generators 共享家族和预训练数据。Pythia generators 达到最高 binary F1 (0.718-0.724)。Cross-ref spread 0.013 部分缓解，但 same-family confound vs scale effect 未干净分离。

### Minor

- **M1**: §2.2 model collapse framing 应在段首区分 training-loop vs inference-chain drift（R16-M2）
- **M2**: Figure 1 DDR 分组阈值 |ρ|=0.10 未标注虚线（R16-M2）
- **M3**: 5 个 orphan bib 条目（briesch_self_consuming, dolma, fineweb, jovanovic_watermark_stealing, mcgovern_fingerprints）+ 5 个 title/author mismatch（R16-M1）
- **M4**: method.tex "which" 从句密度偏高（~10 处）（R16-M2）
- **M5**: Figure 1(b) 需增加 hatching 以适配黑白打印（R16-M2）
- **M6**: Appendices A-T 可合并精简低密度部分（R16-M2）

---

## Reviewer Consensus

| 问题 | R1 | R2 | 共识 |
|------|----|----|------|
| DDR 措辞不一致 (MF1) | Must-Fix (N1) | Agree with nuance | **Must-Fix**（措辞）; Should-Fix（额外检验） |
| Base-model-only vs motivation (MF2) | Agree | Must-Fix (N1) | **Must-Fix** |
| Scale ≤8B 声明过强 (MF3) | Must-Fix (N3) | Agree (W4) | **Must-Fix**（措辞限定） |
| 方法新颖性 | Rebut（Findings 足够） | Must-Fix (N2) | **Findings-appropriate**（非 Main） |
| Concurrent work (SF3) | Agree | Must-Fix (N3) | **Should-Fix** |
| KS test (SF1) | Must-Fix (N2) | Should-Fix | **Should-Fix** |
| 下游 negative (SF2) | Should-Fix | Should-Fix | **Should-Fix** |
| Baseline 公平性 (SF5) | Should-Fix | Rebut | **部分共识** |
| Paraphrase detection 文献 | Rebut | Should-Fix | **不要求** |
| Overall score | 3.0 Findings | 3.0 Findings | **3.0 Findings** |

## Reviewer Divergence

1. **方法新颖性 severity** [R1: REBUT → Findings ok, R2: Must-Fix N2]
   - R1: 核心贡献在任务定义+现象发现，非方法。Findings track 不要求方法新颖性。
   - R2: 7 handcrafted features + XGBoost 无算法创新，不足以 Main Conference。
   - **Resolution**: 双方均认为 Findings-appropriate。非实质分歧。

2. **KS test severity** [R1: Must-Fix N2, R2: Should-Fix]
   - R1: KS 单独无法验证 DDR 分解。
   - R2: 论文组合使用多检验，非仅依赖 KS。
   - **Resolution**: 降级至 Should-Fix。

3. **Baseline 公平性** [R1: Should-Fix, R2: REBUT]
   - R1: Feature 维度不对称（7 vs 4）。
   - R2: 同框架控制了 feature informativeness 比较。
   - **Resolution**: 框架公平；matched-dimensionality 消融为加分项。

4. **Paraphrase detection 文献** [R1: REBUT, R2: Should-Fix]
   - R1: 概念距离远（单文本分类 vs 文本对相似度）。
   - R2: 递归 continuation 功能上类似 paraphrasing。
   - **Resolution**: 不要求独立子节；如有 distributional-feature-based paraphrase work 可选择性引用。

---

## Questions for Authors

1. 能否提供 shape features vs drifting features 在不同 depth class 之间的 Cohen's d 或 Glass's delta，以量化 "comparatively stable" 的程度？
2. 如果将论文 motivation 严格限定为 base-model pretraining data curation，Introduction 如何重写？
3. Disjoint-seed 实验中 binary F1 差异（0.694→0.689）的 95% bootstrap CI 是多少？
4. 除 QLoRA fine-tuning 外，是否尝试过其他下游任务（如 summarization quality, factuality）来验证 depth information 的实际价值？
5. 如何看待 scale degradation 对实际部署的影响？最广泛使用的 API 模型远大于 8B。
6. 能否验证 "Geng et al. (2026), Markovian Generation Chains" 的存在及完整引用信息？

---

## Missing References

- **需补充**: Guo et al. (2023) "How Close is ChatGPT to Human Experts?"（人类与 LLM 文本统计特性对比）
- **需补充**: Ordinal classification 方法论文献（Frank & Hall 2001）应在正文 Related Work 中引用，不仅限于 Appendix
- **需验证**: "Geng et al. (2026), Markovian Generation Chains" — 存在性需确认
- **可选**: Data attribution/provenance 文献以加强 motivation（如重新框定）

---

## External Review (Stanford Agentic Reviewer)

外部审稿未配置（`external_review.paperreview_ai.enabled` 未设置），本轮无外部审稿结果。

---

## Overall Assessment

**Score: 3.0 / 5 (Findings)**
**Confidence: 4/5**

### 评分理由

论文通过新颖的任务定义（generation depth classification）和 DDR 实证发现（drifting vs stationary 特征分解）做出了真正的科学贡献。实验设计严谨，confound 控制细致（LOGO, seed demeaning, disjoint seeds, length matching），写作质量良好。

三个结构性限制阻止 Main Conference 接收：
1. **Scope-motivation 不匹配**: 真实世界动机（检测 LLM 文本污染）需要 instruct model 支持，但方法仅在 base model 有效。这将实际影响大幅缩窄。
2. **Scale 限制**: 证据仅覆盖 0.6B-8B，且上端已显退化趋势。对 70B+ 模型的外推无依据。
3. **方法简洁性**: 7 handcrafted features + XGBoost 技术新颖性接近零。贡献是 empirical/analytical 而非 methodological。

论文适合 **EMNLP 2026 Findings**：任务定义和 DDR 表征是有价值的科学贡献，实验证据充分（修复上述 Must-Fix 后），局限性报告诚实。解决 MF1（措辞一致性）和 MF2（motivation reframing）后达到 Findings 接收标准。MF3（scale 声明限定）因计算约束只能通过措辞调整而非新实验解决。

---

## Detailed Comments

### Abstract
- "whose shape remains comparatively stable" 需与 §4.2 更审慎的处理对齐（MF1）
- Binary F1=0.694 作为 headline 正确
- "base (pretrained) models" 标注到位

### Introduction
- §1 开头段仍以 instruct-model 证据（"7-17% papers"）驱动 motivation（MF2）
- DDR 新颖性声明已区分已知漂移 vs 新颖结构化分解，但可更精确
- Contribution 列表适当（task + DDR，无性能优势声明）

### Related Work
- §2.2 Concurrent work 比较需扩展——逐条对比 Broken Telephone 和已验证的 concurrent work（SF3）
- §2.2 开头应前置 training-loop vs inference-chain 区分（M1）
- Ordinal classification 引用应进入正文（当前仅在 Appendix）

### Method
- Feature extraction 描述清晰；"entropy as shorthand for NLL" 澄清得当
- TTR-hapax r=0.97 相关性已承认，effective dimensionality ~5 诚实
- LOGO 协议是方法论优势
- Pythia-410M 同家族偏差应显式讨论（SF9）

### Results
- Table 1 gen-0 leakage caveat 存在但可更显著（SF6）
- Table 1 vs Table 2 协议差异需更清楚说明（SF7）
- Independent-seed 控制需 CI（SF4）
- Temperature sensitivity 和 prompt-type sensitivity 段落是有价值的补充

### Discussion
- DDR vs model collapse 区分充分但可加强
- Instruction tuning 反转发现（entropy_mean ρ flip）有趣且报告得当
- Scale degradation 趋势需显式限定为 0.6B-8B（MF3）
- "insufficient for automated filtering but sufficient for corpus-level flagging" 定位恰当

### Limitations
- 全面诚实，覆盖所有主要局限
- 可更显式声明 "此方法不适用于 instruction-tuned models，而后者生产了绝大多数真实世界 LLM 文本"

### Format/Compliance
- ACL template [review] ✓, Anonymous ✓, Line numbers ✓
- 页数限制合规
- Limitations section 位置正确（references 前）
- Ethics statement 包含 license, compute, software 信息
- 5 个 orphan bib 条目 + 5 个 title/author mismatch 待修复（M3）

---

## Issue Tracker 同步

本轮更新 `review_issues.yaml`（Round 16）：
- **Reopened**: R7-W2（DDR 措辞）, R7-W5（base-model-only motivation）, R11-W1（reference model bias）
- **New**: R16-N1（KS test limitation）, R16-N2（concurrent work）, R16-W1（disjoint seed CI）, R16-W2（3-class F1 caveat）, R16-W3（Table 1/2 protocol）, R16-M1（bib cleanup）, R16-M2（minor writing/figure）
- **Updated mention**: R10-N3（downstream null, kept resolved）, R13-SF7（scale, kept wont_fix）, R14-W4（baseline fairness, kept in_progress）
- **Open issues total**: 10