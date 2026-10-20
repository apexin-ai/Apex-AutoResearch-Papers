---
round: 14
review_mode: fresh
overall_score: 3.0
timestamp: 2026-05-22T08:12:58.857727+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告 — Round 14 (Fresh)

**论文**: DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection
**目标 Venue**: EMNLP 2026 (ARR Long Paper)
**截止日期**: 2026-05-25
**审稿模式**: 圆桌 2 人 × 1 轮 + 交叉分享
- Reviewer 1: 方法严谨性 + 实验设计 → 3.5 (Borderline Conference)
- Reviewer 2: 新颖性 + 完整性 + 写作质量 → 3.0 (Findings)

---

## Summary

论文通过 7 个 Stage-1 编码器适配变体和冻结 BiGRU Stage-2 分类器的受控消融，系统性地分解多轮越狱检测中的跨攻击泛化机制。核心发现：(1) 领域暴露 (DAPT) 是主要泛化机制（弥合 ~60pp OOD gap），(2) 分类监督增加稳定性（variance 降低 4-20×）但不改变检测上限，(3) 标签粒度和时序顺序无关紧要，(4) 标签正确性仅在结构复杂攻击上有中等效应 (d=0.44)。论文提出"攻击侧 + 良性侧"双轴泛化框架，在 4 个攻击族、3 个编码器架构上验证。

---

## Strengths

**S1. 消融设计的严谨性** [R1-S1, R2-S1, 共识]
7 个 Stage-1 变体各自精确隔离单一因素（Table 1），冻结 Stage-2 确保下游条件一致。这是该领域少见的真正受控实验。Scrambled labels 实验尤其精巧——保留分类结构同时破坏语义，直接检验标签正确性。

**S2. 统计分析远超平均水平** [R1-S2, R2-S3, 共识]
Bootstrap CIs、配对置换检验、TOST 等价性检验（扩展至 10 seeds）、Cohen's d、McNemar 检验、CKA 分析、Fisher ratio、participation ratio——统计工具箱的丰富程度在 NLP 论文中罕见。明确标注 population vs. Bessel-corrected std 的差异。

**S3. 异常坦诚的局限性披露** [R1-S3, R2-S2, 共识]
WildChat FPR 68.1%、ToxicChat 证据层级反转、cross-LLM 90% FPR、RoBERTa-large DAPT regression——多数论文会隐藏这些结果。这种透明度值得赞赏。

**S4. 约束性负面结果的独立价值** [R1-S5, R2-S2, 共识]
时序顺序无关 (Δ<1pp)、标签粒度无关 (binary ≈ 9-class)、mean pooling ≈ BiGRU——这些"无效"发现对该领域有指导意义。

**S5. 跨架构验证** [R1-S4]
DeBERTa-v3-base, RoBERTa-base, RoBERTa-large 三个编码器 + BERT-base proxy，证明 DAPT 效果不依赖特定架构。RoBERTa-large 反转的诚实报告进一步增强可信度。

**S6. 可复现性** [R1 4.5/5, R2 4/5]
23 页附录含 30+ 表格，超参数完整，Stage-1/Stage-2 方差分离实验，承诺代码和数据开源。

---

## Weaknesses

### Must-Fix（影响接收决定）

**N1** [critical, R1-N1 + R2-W1, 共识] **ToxicChat 证据层级反转动摇核心 claim 的外部有效性**

在唯一的人类数据验证中，JB-MLM (0.837±0.013) 大幅领先 9-class (0.596±0.087)，24pp 差距且 CIs 不重叠 (p<0.001)。这与合成数据上的证据层级完全相反。更值得注意的是，classification-supervised 变体在 ToxicChat 上的 variance (std=0.056-0.087) 远高于 MLM (std=0.013)——与合成数据上"classification supervision reduces variance 4-20×"的发现也完全相反。

论文解释"ToxicChat 是单轮数据，分类头无优势"，但未解释为什么 9-class 反而**劣于** MLM 24pp 且 variance 更高。核心矛盾：合成数据上建立的 evidence hierarchy 可能只是合成数据分布的 artifact。目前不存在人类生成的多轮越狱数据集来验证多轮场景下的 hierarchy 是否仍然成立。

**要求**: (1) Abstract/Conclusion 明确限定 claim 适用范围为"合成多轮数据"；(2) ToxicChat 反转提升为 Discussion 核心议题（当前仅 Section 4.5 一段）；(3) 补充 ToxicChat 错误分析（FP vs FN 分解）；(4) 提供机制解释——为什么分类监督在合成多轮上减少 variance 但在真实单轮上增加 variance？

**N2** [critical, R1-N2 + R2-N3, 共识] **良性 IID 混淆使 OOD F1 系统性偏高；FPR=68.1% 下 "deployment recipe" 不令人信服**

所有 OOD 评估中良性样本均来自训练分布（IID）。论文在 Table 3 caption 标注"upper bounds"，但主文叙事大量使用"near-perfect OOD detection"、"recovers to 0.97–1.0"。当良性分布 shift 时（WildChat），FPR 高达 68.1%——每 3 条良性对话中 2 条被误判为越狱。且 9-class FPR (68.1%) > vanilla (48.1%)，DAPT 恶化了 benign-side。

10-shot benign adaptation 修复 (Table P) 验证极弱：n=49 评估集、IID 评估、仅 seed 42。ROC AUC=0.700±0.054，论文自己承认"no post-hoc calibration can overcome this"。工业部署 FPR 阈值通常 1-5%，FPR=0% (n=49, 95% CI upper 6.1%) 在 CI 层面仍不满足 5% 阈值。

**要求**: (1) Abstract 加入 benign-side limitation 限定；(2) 主文 OOD F1 表格标注"attack-side only"；(3) WildChat FPR 详情从附录移至主文 Discussion；(4) C3 "deployment recipe" 降格为 "preliminary evidence"；(5) 10-shot 修复补充多种子验证。

**N3** [critical, R2-N1 + R2-N2, R1 交叉 AGREE] **核心新颖性不足：DAPT 应用 + scrambled label 增量贡献定位不清**

核心发现"continued pretraining closes ~60pp OOD gap"本质是 Gururangan et al. (2020) DAPT 的标准效果在 jailbreak 领域的复现。"attack-side 需要 domain adaptation"在任何 domain shift 场景下都成立，"benign-side shift 导致 false positive"是 domain adaptation 经典问题。J-DAPT (arXiv:2509.23281) 已将 DAPT 用于 jailbreak 检测，论文未引用。

Scrambled label 结果 (scrambled F1=0.994 ≈ 9-class F1=0.994 on DD) 与 Zhang et al. (2021) / Maennel et al. (2020) 的已知发现高度一致。论文引用了这些工作但未明确讨论增量贡献。R1 指出：论文的消融设计本身有方法论价值（7 变体解耦 5 个因素），但 Introduction 中 C1/C3 仍过多强调效果而非方法论。

**要求**: (1) Related Work 补充 J-DAPT 引用和对比；(2) Introduction 贡献重心从"DAPT 有效"转向"受控消融分解的方法论价值"；(3) 用 1-2 段显式定位 scrambled label vs Zhang et al./Maennel et al. 的增量贡献（如 ActorAttack d=0.44 的 complexity-dependent 效应）。

**N4** [critical, R1-N3, R2 交叉 AGREE] **数据规模扩大后性能反常下降——威胁结果稳健性**

Table 14: 训练集 350→1000 对话后，9-class DD OOD 从 0.994→0.889 (-10.5pp)，AA 从 0.972→0.913 (-5.9pp)。MLM 完全崩溃至 vanilla 水平 (DD=0.338, AA=0.351)。IID 存在 71% train/test overlap。

如果方法对训练语料组成如此敏感，350 样本上的 near-perfect 结果可能是偶然的"甜点"而非稳健表现。论文未解释性能下降原因——是新数据引入了不同的 topic distribution？还是 DAPT 对数据量存在非单调关系？

**要求**: (1) 解释 350→1000 性能下降的原因；(2) 控制实验：1000 样本中随机抽取 350 个检验是否恢复原始性能；(3) 主文 Discussion 讨论这一发现。

### Should-Fix（影响评分但不一票否决）

**W1** [warning, R1-W1, R2 AGREE] **BCa Bootstrap 跨 seed 池化违反独立性假设**
3 seed × 118 样本池化进行 bootstrap 存在双重独立性违反，系统性低估 CI 宽度。论文标注 "exploratory" 但仍在主文中使用池化 CI 作为关键证据。建议降级为补充证据，改用 seed-level F1 range 作为主要参考。

**W2** [warning, R1-W2, R2 部分 AGREE] **3-seed 标准差统计效力不足**
n=3 的 variance 估计变异性极大。MLM DD std=0.115 几乎完全由 seed 456 (F1=0.751) 驱动。论文对 scrambled vs 9-class 扩展至 10 seeds（Appendix I），但其他关键对比（如 MLM vs 9-class on AA）仍依赖 3 seeds。

**W3** [warning, R1-W3, R2 部分 REBUT] **Scrambled labels 实验的精确解读**
scrambled labels 保留分类结构和确定性标签分配——测试的是"标签-策略映射正确性"而非"标签信息"是否重要。正确解读："任意确定性分配即可"。ActorAttack 上 TOST 未确认等价 (p=0.183, d=0.44)。Conclusion 中"scrambled labels within 3.9pp"的措辞可能给读者留下"可忽略"的印象，但 AA 上存在 moderate effect。

**W4** [warning, R1-W4, R2 AGREE] **LLM-as-judge 基线可能因 prompt 设计偏弱**
GPT-5.5 零样本 30-47% 不可解析；prompt 模板未提供；未尝试 prompt 优化。当这些数字用于 Introduction motivation 时，weak baselines inflate perceived contribution。应提供 prompt 模板、尝试至少一种 prompt 优化策略、降低对 LLM-as-judge 劣势的 motivation 依赖。

**W5** [warning, R1-W5, R2 AGREE] **Mixed-LLM MLM 崩溃解释不充分**
Mixed-LLM 中 MLM 崩溃至 vanilla 水平 (DD=0.289) 缺乏机制解释。可能是 MLM 学到"区分 Qwen vs Llama 风格"而非"区分越狱 vs 良性"——与 cross-LLM error decomposition (Table H.2: Llama benign FPR 88-90%) 一致。需要表征分析或控制实验（500 Qwen-only MLM vs 250+250 mixed MLM）。

**W6** [warning, R2-W5, R1 AGREE] **Abstract 信息密度过高**
~200 词内包含 13 种配置、60pp gap、多个 F1/FPR/CI 数字，核心研究问题在 Abstract 中缺失。首读可理解性差。建议在 Abstract 开头明确研究问题，减少数值密度。

**W7** [warning, R2-W6, R1 AGREE] **Benign-side 仅 WildChat 单一数据源**
C1 two-axis decomposition 的 benign 轴仅在 WildChat (GPT-3.5 用户) 上验证。至少需要第二个 benign OOD 数据源。

**W8** [warning, R2-W3, R1 AGREE] **DisPeD 命名与发现不一致**
"Disentangled Pattern Detection"暗示 pattern 分解是检测机制，但论文发现标签语义对检测不重要，detection 通过 domain-adapted [CLS] embeddings 运作。命名给读者错误预期。

**W9** [warning, R2-W4, R1 部分 REBUT] **Related Work 遗漏**
J-DAPT (arXiv:2509.23281) 是直接前驱工作，必须引用。TrajGuard (2604.07727)、SAE jailbreak mitigators (2602.12418)、tensor decomposition detection (2602.11495)、Alon et al. (2023) perplexity detection、Phute et al. (2023) LLM Self Defense——需审慎评估相关性后决定。R1 指出 arXiv 预印本数量爆发式增长，不可能穷尽引用，但 J-DAPT 不可忽略。

**W10** [warning, visual check] **Figure 2 缺失 ActorAttack**
ActorAttack 是论文中最有区分力的评估集（TF-IDF 崩溃、证据层级差异最明显），但 Figure 2 仅展示 Crescendo/DD/FITD。构成视觉偏差。

---

## Reviewer Consensus [AGREE]

1. **ToxicChat 反转是 critical 级问题** — R1 标 N1 critical, R2 初审标 W1 should-fix 后在交叉回应中同意升级为 Must-Fix。共识：直接质疑 evidence hierarchy 的外部有效性。
2. **良性 IID 混淆 + FPR=68.1%** — R1 N2 + R2 N3，完全一致。C3 deployment recipe 应降格。
3. **新颖性需要更好的定位** — R2 N1 + R2 N2，R1 交叉 AGREE（但给消融设计更多 credit）。
4. **数据规模反常下降** — R1 N3 首提，R2 交叉 AGREE。Table 14 是未解释的重要发现。
5. **消融设计质量高、统计分析远超平均** — 两位 Reviewer 在优势评估上完全一致。
6. **诚实报告负面结果值得赞赏** — 共识。

## Reviewer Divergence [REBUT]

1. **实验规模评估** — R2 标 W2（较笼统的批评）；R1 REBUT 指出论文已有 TOST 10-seed、per-seed tables、data efficiency 等缓解措施。R2 的批评不完全公平，但 R1 同意多数非 scrambled 对比仍依赖 3 seeds。**结论：论文统计处理在 NLP 中属上游水平，但关键对比应扩展至 5-10 seeds。**

2. **Scrambled labels 解读** — R1 W3 指出正确解读是"任意确定性分配即可"；R2 部分 REBUT 认为这是精确化补充而非否定。**结论：两者可兼容——scrambled 实验验证了分类结构（而非标签语义）驱动 discriminative compression，Appendix S representation geometry 提供了支持证据。**

3. **E2E gap 是否 "modest"** — R1 指出 AA +5.8pp 意味着错误率减少 95%；R2 REBUT 认为 5.8pp 在 n=118 上对应约 5 个样本，在 seed variance 范围内。**结论：措辞应更中立。**

4. **Overall score** — R1: 3.5, R2: 3.0。主要分歧在新颖性权重。R1 对消融方法论给予较高 credit；R2 认为 DAPT 在安全领域的增量贡献 + 高 FPR 将论文锚定在 Findings。

---

## Questions

1. **Table 14 性能下降**: 为什么 350→1000 训练集导致 OOD 性能下降？是否尝试在 1000 样本中随机抽取 350 个来检验稳健性？
2. **ToxicChat 反转机制**: 是否有证据表明分类监督在合成数据上过拟合合成分布结构（如 Qwen3-8B 特有的句法/词汇模式）？
3. **WildChat 10-shot 多种子**: Table P 仅用 seed 42。是否有 3-seed 10-shot benign adaptation 结果？
4. **ActorAttack padding collapse**: AA padded F1=0.383 (Δ=-57.9pp) 暴露了 BiGRU 时序聚合在 attention dilution 下的脆弱性。鉴于真实对话中良性 turn 和攻击 turn 会交错出现，这一脆弱性是否比论文讨论的更根本？
5. **DeepContext 直接对比**: BERT-base proxy 是间接对比，是否尝试过直接复现 DeepContext？

---

## Missing References

**必须补充**:
- J-DAPT (arXiv:2509.23281) — DAPT 用于 jailbreak 检测的直接前驱工作

**建议评估后补充**:
- TrajGuard (arXiv:2604.07727)
- SAE jailbreak mitigators (arXiv:2602.12418)
- Tensor decomposition detection (arXiv:2602.11495)
- Alon et al. (2023) "Detecting Language Model Attacks with Perplexity"
- Phute et al. (2023) "LLM Self Defense"

---

## External Review

**外部审稿**: 未配置，无外部审稿结果。

---

## Visual Layout Check（非评分项）

视觉审查已完成。3 warnings, 7 info:

**Warnings**:
- **Page 8-9 溢出**: Section 6 (Conclusion) 在 page 8 右栏底部开始，约 10 行溢出到 page 9。Conclusion 属于主文，必须收入 8 页内。需压缩 Discussion 或 Results。
- **Page 8 过度压缩**: Section 4.7 Perturbation Analysis、4.8 Strategy Trajectory、Section 5 Discussion、Section 6 Conclusion 全部挤在一页，文字密度远高于其他页面。
- **Page 16**: Figure 4 (CKA) 和 Figure 5 (UMAP) 子图较小，打印尺寸下可读性存疑。

**Info**: 首页无视觉锚点（纯文字）；Figure 1 架构图清晰但内部文字略小；Figure 2 x 轴标签字号偏小；Table 2 混合单/多种子统计口径；附录表格数据密集但可接受。

---

## Overall Assessment

**评分: 3.0 (Findings)**
**置信度: 4/5**

**理由**:

论文的消融设计质量高（7 变体精确隔离单因素）、统计分析远超 NLP 平均水平、局限性披露异常坦诚——这些是真正的优点，表明作者在实验方法论上有深厚功底。

但核心 claim 的可信度受到多重限制：(1) 唯一人类数据验证 (ToxicChat) 上 evidence hierarchy 完全反转，直接质疑合成数据发现的外部有效性；(2) OOD F1 是 benign-IID 条件下的 upper bound，真实场景 FPR=68.1% 使系统几乎不可部署；(3) 数据规模扩大后性能反常下降 (-10.5pp on DD) 威胁结果的稳健性；(4) "DAPT closes OOD gap"本质上是已知效应的领域复现，增量新颖性有限。

论文的消融分解框架和负面结果集合对社区有参考价值，适合 Findings track。升级至主会议需要：(a) 人类多轮数据验证证据层级不反转，(b) 部署场景 FPR 降至可接受水平并有充分验证，(c) 更清晰地定位 vs prior DAPT/random-label 文献的增量贡献。

---

## Detailed Comments

### Abstract
- 信息密度过高（~200 词，13 种配置，多数值）。核心研究问题 ("what representation properties enable cross-attack generalization?") 应出现在 abstract 开头。
- "as few as 10 target-domain benign conversations eliminate false positives" 在 FPR=68.1% 和 n=49 IID 验证的背景下过于强烈。

### Introduction
- C1/C3 贡献措辞偏重"效果"而非"方法论分解"。建议将受控消融设计和约束性发现作为贡献核心。
- GPT-5.5 "30-47% unparseable" 作为 motivation 可能因 prompt 设计偏弱而 inflate perceived contribution。

### Related Work
- 遗漏 J-DAPT (arXiv:2509.23281)——直接前驱工作。
- Scrambled label 相关的 Zhang et al. (2021) / Maennel et al. (2020) 仅在 Section 5 括号中引用，未讨论增量贡献。

### Method
- 7 变体设计精巧、描述清晰（Table 1 信息密集且高效）。
- Scrambled labels 实验应更精确地表述：测试的是"标签-策略映射正确性"而非"标签信息"。

### Experiments
- Table 3 和其他 OOD 表格：应在每个 caption 中重复 "OOD F1 reflects attack-side only; benign is IID"。
- Figure 2 应包含 ActorAttack。
- "evidence hierarchy" 术语应限定为 "evidence hierarchy on synthetic multi-turn data"，因在 ToxicChat 上反转。
- Section 4.5 ToxicChat 讨论过于简略——24pp 反转和 variance 反转需要更深入分析。
- Section 4.5 Mixed-LLM MLM 崩溃缺乏机制解释。
- E2E gap (AA +5.8pp) 的 "modest" 措辞不够中立——错误率从 6.1% → 0.3%。

### Discussion
- "Discriminative compression" 机制解释有 representation geometry 支持 (Appendix S)，但应更谨慎——这是观察性关联而非因果证据。
- WildChat FPR 详情应从附录移至主文 Discussion。
- RoBERTa-large vanilla AA=1.000 的含义（"大模型不需要 DAPT"）应在 Discussion/Conclusion 中更显著地讨论，因为它直接限定论文贡献的适用范围。

### Conclusion
- "this yields a deployment recipe requiring no target-domain attack data" 在 FPR=68.1% 下过于强烈。
- Scrambled ≈ 9-class 的 AA 非等价 (d=0.44) 应更突出。
- 疑似溢出 page 8——Conclusion 必须完整收入 8 页主文。

### Limitations
- 覆盖充分且简洁，符合 EMNLP 2026 要求。
- 10-shot benign adaptation 单种子限制应在此处强调。

### Appendix
- 极其详尽（30+ 表格），可复现性优秀。
- Table 14 (dataset scale validation) 的性能下降应在主文 Discussion 中讨论而非仅在附录中呈现。
- LLM-as-judge prompt 模板应提供。

### 格式
- ⚠️ 主文 Conclusion 疑似溢出至 page 9（视觉审查发现），需压缩。
- 参考文献 arXiv/published 混合，应统一为最新 published 版本。
- Ethics Statement 中 "withholding prompts" 与开源承诺的范围应更精确。