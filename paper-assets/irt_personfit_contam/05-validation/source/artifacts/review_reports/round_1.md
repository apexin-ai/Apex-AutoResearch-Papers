---
round: 1
review_mode: fresh
overall_score: 3.0 Findings
timestamp: 2026-05-21T18:25:11.561462+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告：IRT Person-Fit for LLM Benchmark Contamination Detection

**项目**: irt_personfit_contam
**目标 Venue**: EMNLP 2026 (ARR Long Paper)
**审稿轮次**: Round 2 (fresh)
**审稿日期**: 2026-05-21
**Reviewer 编排**: 2 人（R1: 方法严谨性+实验设计, R2: 新颖性+完整性+写作格式）

---

## Summary

本文首次系统地将 IRT person-fit 统计量（ℓz*）应用于 LLM benchmark contamination 检测，操作在 minimal-information point（仅需二值 response pattern + 外部校准的 4PL 参数）。通过在三个 7-8B 模型家族（Qwen, Llama, Mistral; n=10 seeds）上的受控实验（QLoRA SFT, 15%/50% 污染）和 MMLU + ARC-Challenge 两个 benchmark，论文识别了四个边界条件：(1) free-θ 下的 inverted-U dose-response，(2) 模型特异性 θ-shift dynamics，(3) detection-diagnosis tradeoff，(4) post-RL residual pattern (N=1)。

---

## Strengths

**S1. 跨学科新颖性** [R1, R2 共识]
将教育测量学中有 40 年积累的 person-fit 统计量迁移到 LLM contamination 检测，这一视角是 genuinely novel 的。基于"响应模式异常"而非"信息泄露痕迹"，与现有 MIA/n-gram/probing 方法在理论层面有根本性区别。

**S2. Δℓz* 差分设计务实合理** [R1, R2 共识]
认识到 LLM 系统性违反 IRT 假设（57/60 cells flagged even absent contamination），提出差分设计消除共享 misfit，是方法论上合理的处理。

**S3. 受控实验设计规范** [R1, R2 共识]
n=10 seeds × 3 model families × 2 benchmarks × 3 conditions，bootstrap 95% CI（10,000 resamples）提供了统计推断基础。Table 1 所有 CI 不包含零。Cohen's d 作为 effect-size 指标选择恰当。

**S4. θ-shift 机制分析有理论深度** [R1]
揭示 baseline accuracy 与检测灵敏度的负相关（MMLU 上 Mistral 52.4% → |d|=3.50 > Qwen 67.8% → |d|=1.90），以及 ARC-C 上因天花板效应导致的 sign flip，提供了可解释的机制理解。

**S5. 坦诚的自我定位** [R1, R2 共识]
以"characterization"而非"detection method"自居，Discussion 和 Limitations 坦诚讨论了主要局限。Detection-diagnosis tradeoff 的诚实报告（accuracy |d|=42-68 vs ℓz* |d|=0.58-1.90）值得肯定。

---

## Weaknesses

### Must-Fix（影响接收决定）

**MF-1. [Critical] IRT 假设违反分析不充分，Δℓz* 有效性缺乏理论保证** [R1-N1, R2 AGREE]

Section 3.2 承认 LLM 系统性违反 IRT 局部独立性和单维性假设。Δℓz* 差分设计仅在 clean/contaminated conditions 下 misfit 为加性且等量时有效。但论文未分析关键问题：**污染是否改变了 item 间依赖结构？** 如果 memorized items 的答对独立于 θ（纯靠记忆），contaminated condition 下的 misfit 结构与 clean condition 不同，Δℓz* 不再是有效差分估计量。Appendix A 模拟验证（R²=0.957）假设 IRT 模型成立，构成循环论证。57/60 clean cells 被 flag 说明 IRT misfit 极严重，Δℓz* 承担极大校正负担但其理论保证缺失。

**MF-2. [Critical] 生态效度不足——QLoRA SFT ≠ pretraining 污染** [R2-N1, R1 AGREE]

QLoRA (rank=16, α=32) 仅修改低秩 adapter，权重变化受限于低秩子空间，与 pretraining contamination（全参数分布式梯度更新）本质不同。Fine-tuning 污染接近"item preknowledge"（教育测试中的作弊），pretraining 污染更接近"over-exposure"（重复暴露的隐式学习），两种机制可能产生不同的 aberrance pattern。所有四个 findings 的外推有效性存疑，核心贡献范围被 SFT-specific 所限制。

**MF-3. [Critical] Post-RL finding (N=1) 统计效力严重不足，Abstract overclaim** [R1-N3, R2-N2 共识]

Section 4.5 的 post-RL 发现仅基于 N=1（Qwen, 15% MMLU, GRPO）。Figure 4 无误差条或置信区间。一个 N=1 观察被提升到与 n=10 seeds 验证的其他发现同等地位——Abstract 将其列为四大 findings 之一且未标注 preliminary，与正文末尾 "We report this as a preliminary characterization" 的 hedging 不一致。单一实验点无法建立任何 "pattern"。R1 建议如不增加实验应从 Abstract 移除。

**MF-4. [Critical] PSN-IRT 参数依赖缺乏敏感性分析** [R1-N4, R2 AGREE]

整个框架的 4PL 参数来自 PSN-IRT，这是 single point of failure。论文未提供：(a) 参数精度/标准误信息；(b) 参数扰动下 ℓz* 的敏感性分析（如 5-10% 噪声）；(c) 与其他估计方法的交叉验证。4PL upper asymptote d 参数本身估计不稳定。如果 leaderboard 校准样本包含已污染模型（很可能），PSN-IRT 参数可能已有偏差。

**MF-5. [Critical] Inverted-U 削弱 minimal-information 实用性主张** [R1-N2, R2 AGREE]

free-θ 下 Qwen |d| 从 15% 的 6.58 降到 50% 的 1.90——污染越严重检测越弱。fixed-θ anchoring 解决此问题但需要 clean baseline，与 Abstract "operating at the minimal-information point: binary response patterns" 的定位相矛盾。方法的宣传定位与实际信息需求之间存在显著落差。

---

### Should-Fix（影响评分但不一票否决）

**SF-1. 仅两个污染水平不足以支撑 inverted-U 曲线** [R1-W2, R2 AGREE]
三个数据点（0%, 15%, 50%）无法区分 inverted-U 和 monotonic decrease。缺少 5%, 10%, 25% 等中间点来确认峰值位置和曲线形状。

**SF-2. Item-level detection 接近随机，与 fingerprint claim 矛盾** [R1-W3, R2-W2 共识]
Table 8: ℓz* itemwise AUROC=0.53 ≈ random。但 Section 5 声称 "ℓz* can yield per-item memorization fingerprints"，claim 与 evidence 矛盾。

**SF-3. Detection-diagnosis tradeoff 论证不足** [R1-W4, R2 AGREE]
accuracy |d| 比 ℓz* 大 20-70 倍，但论文未提供具体 use case 展示诊断信息如何改变实际决策。

**SF-4. 57/60 vs 4/60 比较具有误导性** [R1-W5, R2 AGREE]
57/60 flagging 反映 IRT misfit 普遍性而非检测能力优势。将 raw ℓz* 的 95% FPR 作为优势呈现，与 Δℓz* 设计动机（正是因为 raw ℓz* 无法区分 contamination 和 general misfit）自相矛盾。

**SF-5. 模型覆盖范围过窄** [R2-W1, R1 AGREE]
仅 3 个 7-8B 模型。θ-shift dynamics 的 negative correlation 基于 3 个数据点不足以建立系统性关系。缺少更大规模（13B/70B）和不同架构（MoE）验证。

**SF-6. Mistral n=6 与 n=10 声称不一致** [R1-Q2, R2 AGREE]
Table 1 footnote 标注 Mistral n=6，但 Section 3.3 声称 "n=10 clean seeds per family"。应在正文解释原因。

**SF-7. 缺少代码/数据可用性声明** [R1]
ARR 建议提供 reproducibility statement。PSN-IRT 参数可获取性和 bootstrap CI 实现细节（bias-corrected? percentile?）未说明。

**SF-8. Orphan bibliography + 遗漏关键引用** [R1, R2]
bib 有 28 条 orphan entries。Tendeiro & Meijer (2014) 和 St-Onge et al. (2011) 在 bib 中但未 cite，均与核心 findings 直接相关。总引用 31 篇处于顶会下限。

---

## Reviewer Consensus

以下问题两位 Reviewer 完全一致（均 [AGREE]）：

1. **MF-1**: IRT 假设违反 + Δℓz* 有效性是方法论根基问题
2. **MF-2**: QLoRA SFT 的生态效度限制所有 findings 的外推范围
3. **MF-3**: Post-RL N=1 被 overclaim，应降级或补充实验
4. **MF-4**: PSN-IRT 参数依赖是 single point of failure
5. **MF-5**: Inverted-U 与 minimal-information 定位矛盾
6. **SF-1 至 SF-8**: 所有 Should-Fix 均达成共识

---

## Reviewer Divergence

**分歧 1: Findings 新颖性定级**
- R2 认为 3/4 findings 可从 IRT 理论直接预测（inverted-U = 天花板效应, θ-shift = 经典议题, tradeoff = power vs specificity），novelty 被高估 → **Critical**
- R1 反驳（[REBUT]）：empirical characterization in new domain 有独立价值。θ-shift absorption 机制 + benchmark size 交互是 new empirical finding，4PL vs 3PL +27pp power gain 超越理论预测 → **Should-Fix**（加强对 prior literature 的引用即可）
- **Review Director 判断**：降为 Should-Fix。论文标题已使用 "characterization" 定位，findings 的量化结果（|d| 幅度、benchmark size 依赖、4PL advantage）确实超越了理论层面的定性预测。但写作确实应更好 acknowledge prior IRT person-fit literature（特别是 St-Onge et al. 2011, Meijer & Sijtsma 2001 关于 ability-person fit interaction 的讨论）。

**分歧 2: 是否需要与 ConStat/MIA/CoDec 实证对比**
- R1 要求至少与 ConStat 进行实证对比（两者都基于 benchmark performance）→ **Warning**
- R2 反驳（[REBUT]）：characterization paper 不应被要求性能竞赛，但应讨论互补关系
- **Review Director 判断**：采纳 R2 立场。Characterization paper 的评价标准不同于 detection method paper。但 Discussion 确实应讨论与 ConStat 的互补性。

---

## Questions for Authors

1. Appendix A 模拟是否假设 IRT 模型正确拟合？引入 local dependence（testlet 结构）后 ℓz* 的 Type I error rate 和检验力如何变化？
2. Mistral 实际使用了多少 seeds？为什么与 Qwen/Llama 不同？
3. PSN-IRT 校准数据是否包含已知被污染的模型？Section 3.1 的 "rₐ=0.127" 来自何种实验条件？
4. Fixed-θ 的 cross-benchmark ability estimation 在实际部署中如何实现？如果多个 benchmark 同时被污染呢？
5. Table 8 item-level AUROC=0.53 与 Section 5 "per-item memorization fingerprints" 如何调和？
6. Post-RL 后 ℓz* gap 是否只是残留 accuracy difference（0.5-1%）被 IRT 放大的结果，而非独立的 response-pattern information？

---

## Missing References

1. **Tendeiro & Meijer (2014)** — 非参数 person-fit 假设违反下的替代方案（已在 bib 未 cite）
2. **St-Onge et al. (2011)** — aberrance rate 对 person-fit accuracy 的影响（已在 bib 未 cite）
3. **Magis et al. (2012)** — person-fit 在 model misfit 下的 robustness 分析
4. **Sinharay (2016)** — person-fit 在假设违反下的行为
5. **Li et al. (2024)** — Data Contamination Quiz (TACL)

---

## External Review (Stanford Agentic Reviewer)

**状态**: 未配置（项目未启用 external_review.paperreview_ai）

---

## Visual Layout Check（非评分项）

**状态**: 已完成

| 严重度 | 页码 | 发现 |
|--------|------|------|
| Critical | p12 | Appendix 最后一页仅 Table 8（4行×2列小表）占约 15% 面积，~85% 为空白。建议合并至 p11。 |
| Warning | p4 | Table 1 主结果表未对最优值加粗标注；Table 2 (p6)、Table 3 (p7) 同样缺少加粗。 |
| Warning | p8 | 正文最后页为纯文本（Discussion+Limitations+Conclusion+Refs 开头），无 display item。 |
| Info | p2 | Figure 1 子图坐标轴标签和 legend 字号偏小（约正文 60%），建议放大至 70%+。 |
| Info | p5 | Figure 2 热力图 cell 内数字字号较小，建议增大或简化 CI 显示。 |
| Info | p11 | Tables 4-7 密集堆叠，表间距略紧。 |
| Info | p1 | 首页无视觉锚点（ACL 模板限制，非硬伤）。 |

---

## Overall Assessment

**评分: 3.0 — Findings**（可被 Findings 接收）

**置信度: 4/5**

**评分理由**:

跨学科概念桥接（person-fit → contamination）genuinely novel，受控实验设计规范（n=10, 3 families, bootstrap CI），诚实的自我定位（characterization rather than tool）。这些优势使论文达到 Findings 可接收水平。

但五个 critical 问题限制了其达到 main conference 水平（4.0）：

1. **方法论根基不稳**（MF-1）: Δℓz* 有效性依赖 IRT 假设，但 LLM 系统性违反这些假设，且论文未分析污染对 item 依赖结构的影响。
2. **生态效度受限**（MF-2）: QLoRA SFT 产生的 aberrance pattern 可能与 pretraining contamination 本质不同，所有 findings 的适用范围被限定为 SFT-based contamination。
3. **核心 claim overclaim**（MF-3）: Post-RL finding 是最具新颖性的贡献，但 N=1 的证据不足以支撑 Abstract 级别的 claim。
4. **外部依赖未验证**（MF-4）: PSN-IRT 参数是 single point of failure，缺乏敏感性分析。
5. **实用性定位矛盾**（MF-5）: free-θ 的 inverted-U 问题削弱了 minimal-information 的卖点。

**升级路径**（达到 4.0 所需）:
- 对 Δℓz* 在 IRT 假设违反下的行为进行理论分析或模拟验证
- Post-RL 实验扩展至至少 2 个额外模型或 RL 方法
- PSN-IRT 参数扰动敏感性分析
- 增加中间污染水平（25%）以验证 dose-response 曲线形状
- 调整 Abstract/Introduction claim 强度以匹配证据层级

---

## Detailed Comments

### Section 1 (Introduction)
- 逻辑链清晰（问题→现有方法不足→psychometric analogy→本文方法→findings），但第四个 bullet（post-RL）未标注 N=1/preliminary
- Figure 1 的 clean/contaminated response pattern 示意图有效传达核心 insight
- "operating at the minimal-information point" 的 claim 需与 fixed-θ 的额外信息需求协调

### Section 2 (Related Work)
- 覆盖三个维度（contamination detection, IRT for LLM, person-fit in psychometrics）结构清晰
- 引用 31 篇处于顶会下限，bib 中有 28 条 orphan entries 需清理
- 应引用 Tendeiro & Meijer (2014)（与 tradeoff 相关）、St-Onge et al. (2011)（与 inverted-U 相关）

### Section 3 (Method)
- 4PL 模型公式和 ℓz* 定义清晰
- Δℓz* 差分设计的动机论证有力（57/60 flagging），但有效性条件（加性等量 misfit）未充分论证
- Section 3.3: "n=10 clean seeds per family" 与 Mistral 实际 n=6 不一致
- 缺少 data preprocessing 细节（如何从 benchmark 采样 15%/50%？分层还是随机？）

### Section 4 (Results)
- Section 4.2 (Inverted-U): 应引用 St-Onge et al. (2011) 讨论 aberrance rate 对 person-fit 的影响；"inverted-U" 表述应加限定（仅 2 个非零数据点）
- Section 4.3 (θ-shift): 仅 3 个模型的 negative correlation 不足以建立系统性关系；ARC-C 反转现象的 ceiling effect 解释 interesting 但同样仅 1 个数据点
- Section 4.4 (Tradeoff): Table 3 的 accuracy |d|=42-68 需解释为什么如此大（cross-seed variance 极小导致 denominator 很小）
- Section 4.5 (Post-RL): N=1 无统计推断基础；Figure 4 需误差条；应排除 ℓz* gap 只是残留微小 accuracy difference 被放大的替代解释

### Section 5 (Discussion)
- "per-item memorization fingerprints" 与 Table 8 AUROC=0.53 矛盾
- 57/60 vs 4/60 比较需重新表述——这是 IRT misfit 普遍性的证据，不是检测能力优势
- 应讨论与 ConStat 的互补关系

### Limitations
- 覆盖了模型规模、污染机制、post-RL N=1 三个主要限制
- **缺失**: IRT 假设违反（应是最重要的 limitation）、PSN-IRT 参数依赖
- 篇幅适当（3 句话，符合 EMNLP 规范）

### 格式合规
- ✅ 正文 8 页内
- ✅ ACL review 模板，双盲匿名
- ✅ Limitations 章节存在
- ⚠️ Mistral n=6 标注不一致
- ⚠️ 无 reproducibility statement
