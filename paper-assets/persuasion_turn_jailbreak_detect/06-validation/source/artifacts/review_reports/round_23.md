---
round: 23
review_mode: fresh
overall_score: 3.0 (Findings)
timestamp: 2026-05-24T13:45:19.890373+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# Round 23 审稿报告

## Summary

本文对 DeBERTa-v3 在多轮越狱检测任务上的 7 种领域自适应预训练（DAPT）策略进行了系统性消融研究，建立了从 vanilla continued pretraining 到 9-class persuasion strategy classification 的性能梯度（"evidence hierarchy"），并发现 scrambled labels 在 template attacks 上与正确标签等效。论文还报告了 ToxicChat 人类数据上 hierarchy 反转、RoBERTa-large 规模下 DAPT 反效果等 boundary conditions。实验设计全面（7 variants × 2 evaluation axes × 3 seeds × 2 encoders），但核心叙事在真实数据场景中受到严重削弱。

## Strengths

**S1: 系统性消融设计。** 7 种 DAPT 变体构成完整的因子分解光谱（vanilla → Wiki-MLM → JB-MLM → topic → binary → scrambled → 9-class），每个步骤隔离一个实验因素。这种设计在安全检测领域罕见。

**S2: 两轴评估框架。** 将泛化能力分解为 attack-side OOD（跨攻击家族）和 benign-side OOD（跨 benign 分布）两个正交维度，结构清晰，便于定位失败模式。

**S3: Boundary conditions 的诚实报告。** ToxicChat 反转、RoBERTa-large DAPT 反效果、ActorAttack 上 scrambled ≠ 9-class 等 negative/boundary results 均在论文中呈现，没有选择性报告。

**S4: Scrambled label 等价性发现。** 在 template attacks（DangerousDialogues, FITD）上 scrambled labels 与正确 9-class labels 的 TOST 等价检验通过（p<0.05, |d|≤0.14），这一发现对理解 DAPT 机制有启示——classification objective 的结构性角色比标签语义更重要（在适用范围内）。

**S5: 实验基础设施质量。** 10-seed TOST、BCa bootstrap CI、CKA/SVD 表征分析、多粒度长度控制实验等统计和分析手段丰富，方法论意识强。

**S6: 实用部署价值。** 与 LLM-as-judge 相比 24-43× 推理加速，few-shot benign adaptation 仅需 10-25 条对话即可将 WildChat FPR 从 68% 降至 0-1.5%，具备实际部署潜力。

## Weaknesses

### Must-Fix

**MF1 [共识]: ToxicChat hierarchy 反转严重削弱核心叙事。**
ToxicChat 是论文唯一的人类数据评估（Table 5, Section 4.6），MLM 以 F1=0.837 大幅超越 classification F1=0.596。论文核心叙事 "classification-based DAPT is the most robust variant" 在人类数据上质的反转。论文在 Section 5 和 Conclusion 各用一句话带过，处理深度与问题严重性不匹配。综合 WildChat 68.1% FPR（Section 4.8），论文的核心 hierarchy 在**所有真实数据场景**中均失效或严重退化：
- 合成 OOD 数据：hierarchy 成立
- ToxicChat（人类数据，单轮）：hierarchy 反转
- WildChat（人类数据，多轮 benign）：68.1% FPR

需要增加对 ToxicChat 反转的深入分析（至少 1-2 段），并在 Conclusion 中给出条件性结论而非一句话概括。[R1-N3 ↔ R2-N2, 两位 AGREE]

**MF2 [共识]: Abstract 中 "label semantics" claim 范围未限定。**
Abstract 称 "indicating the classification objective's structural role—not label semantics—drives generalization"，但 TOST 在 ActorAttack 上失败（p=0.183, d=0.44, Appendix L Table 16）。"Generalization" 未限定为 template attacks，读者可能误解为适用于所有攻击类型。Section 4.3 正文有正确限定，但 Abstract 缺失。需修改为 "drives generalization **on template attacks**" 或 "**for structurally consistent attack families**"。[R1-N2 ↔ R2 cross AGREE]

**MF3 [共识，严重程度有分歧]: 核心 evidence hierarchy 增量新颖性定位过高。**
Classification DAPT 优于 vanilla/MLM 在 Gururangan et al. (2020) 的 DAPT 框架下是 largely predictable——该文已系统证明 task-adaptive pretraining 在多个 NLP 任务上优于 vanilla continued pretraining。论文将此结果标记为三大 "unexpected findings" 之一（Section 1, page 2），novelty framing 有拔高之嫌。论文的真正贡献在于因子分解的定量化（domain exposure vs classification supervision 的贡献量级、boundary conditions、scrambled equivalence），而非 hierarchy 排序本身。建议将 finding (i) 重新定位为 "quantifying the magnitude and conditions" 而非 "unexpected"。[R2-N1 critical + R1 cross AGREE but prefers major. Director 判定: Must-Fix for framing]

### Should-Fix

**SF1 [分歧裁定]: 对话长度混淆——现有控制充分但缺直接 baseline。**
Benign 12-20 turns vs jailbreak 3-10 turns 的长度差异是潜在混淆因素。论文已提供截断验证（Appendix V, Table 32 Part A: 截断后 FPR=0.000）、length-matched 子集（N=155, ΔF1=-2.5pp）、length stratification（Appendix U, Table 31: 无系统性退化）。R2 认为这些控制已充分排除长度 shortcut；R1 认为 turn-count-only baseline F1 是更直接的反驳。**Director 裁定: Should-Fix**——现有控制合理但非决定性，一个简单的 turn-count classifier 可一步封堵此质疑。[R1-N1 Must-Fix vs R2 Should-Fix]

**SF2 [分歧裁定]: WildChat 68.1% FPR——合成数据训练的根本局限。**
R1 将此视为跨域泛化失败；R2 指出论文的 "cross-attack generalization" 始终限定在攻击家族维度而非域泛化。R2 的论证在技术上正确——abstract 已标注 few-shot adaptation，没有声称 zero-shot 跨域泛化。**Director 裁定: Should-Fix**——68.1% FPR 不构成 soundness 问题，但暴露了合成 benign 训练数据的系统性偏差，应在 Discussion 中更明确讨论。需第二个人类多轮数据源（如 ShareGPT 或 LMSYS-Chat）的验证。[R1-N3 Must-Fix vs R2 Minor]

**SF3 [共识]: TOST δ=5pp 缺乏 practical significance 论证。**
在 F1>0.95 的区间，5pp 差异意味着 miss rate 的数倍变化——如果 5pp 在部署场景下有实际意义，用它做等价阈值则自相矛盾。应补充 domain-specific practical significance 论证或 δ=3pp sensitivity analysis。[R1-W1 + R2 AGREE]

**SF4 [共识]: Topic 变体 5 vs 9 类别数量混淆。**
Topic variant 用 5-class 分类而 9-class variant 用 9 categories（Table 1）。Topic 的失败可能因为 5 classes 不足以产生足够的 discriminative compression，而非因为 topic labels 与 jailbreak detection 无关。一个 9→5 class merging 控制实验成本低且能直接回答这个问题。[R1-W3 + R2 AGREE]

**SF5 [共识]: RoBERTa-large DAPT "有害" 机制未解释。**
Section 4.4 和 Section 5 解释了为什么大模型不需要 DAPT（vanilla capacity 足够），但 9-class DAPT 在 AA 上 F1 从 1.000→0.946 表明 DAPT 是 actively harmful，不仅仅是 unnecessary。可能的机制（over-specialization、catastrophic forgetting）未被区分。CKA 分析（Appendix S, Figure 6）可能提供线索但未被讨论。[R1-W4 + R2-W4 AGREE]

**SF6 [共识]: 1000 样本性能反常下降未解释。**
Appendix I (Table 9/10) 报告 1000 样本时的性能下降，论文归因于 distributional heterogeneity，但无实验验证。应报告 1000 样本的 training loss 曲线、data composition 分析或 seed 一致性验证。[R1-W5 + R2 AGREE]

**SF7 [共识]: "Evidence hierarchy" 术语缺乏正式定义。**
从 Section 1 (page 1-2) 开始频繁使用但首次出现时无明确定义。读者需从上下文推断含义。R1 进一步指出该术语暗示超出经验排序的理论地位，建议改为 "performance ranking"。应在首次使用处加入操作性定义。[R2-W1 + R1 AGREE]

**SF8 [共识]: Conclusion "reusable template" claim 超出实证范围。**
Section 6 声称 "This ablation framework provides a template for diagnosing when domain adaptation succeeds and fails in this safety-critical detection setting"，但实证基础仅限于单一任务、单一数据源、单一 encoder 家族。应限定为 "template for future controlled studies of domain adaptation in safety-critical NLP tasks"。[R2-W3 + R1 AGREE]

**SF9 [共识]: BiGRU vs mean pooling 讨论不足。**
Appendix T (Table 30) 显示 frozen probing 下 BiGRU 和 mean pooling 差异在 CI 范围内，E2E fine-tuning 下均收敛到 F1=1.000。这暗示 temporal order 在充分表征质量下非必需，与论文将 BiGRU 作为 Stage 2 核心组件的设计选择相关。应在正文明确说明 BiGRU 可被 mean pooling 替代且不影响检测性能。[R1-W3 + R2-W4 AGREE]

**SF10 [共识]: 策略标注质量验证不足。**
50 样本验证 9 个类别，部分类别仅 2-5 个验证样本，κ=0.78 在此粒度下可靠性不足。Scrambled 实验缓解了对主要检测结论的影响，但 Appendix Y 策略预测准确率（90.1%）受标注质量直接限制。建议增加验证样本至≥100 并报告 per-class κ。[R1-W4 + R2 AGREE]

### Minor

**M1: Abstract 句法模糊。** "this hierarchy reverses" 后的修饰对象不清晰，需要重写以消除歧义。[R2, 跨轮持续存在]

**M2: Scrambled ≈ 9-class 发现的叙事定位。** 该发现可能是论文最具洞察力的结果，但当前论文将其作为 hierarchy 排序的补充讨论，而非核心贡献。建议在 Section 5 增加段落讨论 classification objective structure vs label semantics 的机制意涵。[R1-W2 ↔ R2-W2]

## Reviewer Consensus

以下关键问题两位 Reviewer 完全一致：
1. ToxicChat hierarchy 反转是论文最大的 narrative concern（MF1）
2. Abstract "label semantics" claim 需限定到 template attacks（MF2）
3. Scrambled ≈ 9-class 在 ActorAttack 上不成立（d=0.44, TOST p=0.183）
4. "Reusable template" overclaim 需限定范围（SF8）
5. RoBERTa-large DAPT 反转缺乏机制解释（SF5）
6. BiGRU 可被 mean pooling 替代（SF9）
7. Overall 3.0 (Findings) 评分

## Reviewer Divergence

**分歧 1: 长度混淆严重程度** — R1 列为 Must-Fix（turn-count shortcut 可能性未排除）；R2 列为 Should-Fix（Appendix U/V 的截断、length-matched、stratification 实验已充分控制）。Director 裁定 Should-Fix：现有控制合理，但 turn-count-only baseline 可一步封堵。

**分歧 2: WildChat 68.1% FPR 严重程度** — R1 列为 Must-Fix（跨域泛化声明严重削弱）；R2 列为 Minor wording（论文从未声称跨域泛化，attack-side 和 benign-side 是正交轴）。Director 裁定 Should-Fix：R2 技术上正确但 68.1% FPR 暴露合成数据训练的系统性偏差，需更充分讨论。

**分歧 3 (minor): Scrambled "counter-intuitive" framing** — R2 认为在 discriminative compression 框架下可预期；R1 认为对 NLP 社区多数读者仍具 counter-intuitive 成分（random labels 在标准 NLP 文献中被视为 noise injection 而非有效训练信号）。Director 判断 R1 更准确——scrambled ≈ 9-class 确有 counter-intuitive 价值，但 ActorAttack 例外需在正文突出。

## Questions

**Q1:** 作者能否提供一个 turn-count-only classifier 的 F1 作为 sanity check？这是一个零成本实验，可以彻底排除长度 shortcut 质疑。

**Q2:** ToxicChat 反转的根因是 single-turn 特性还是 distributional properties？作者能否将 ToxicChat 数据用多轮格式包装（padding with neutral turns）测试 classification DAPT 是否恢复？

**Q3:** RoBERTa-large 上 9-class DAPT 导致 AA F1 从 1.000 降至 0.946 的机制是什么？CKA 分析（Figure 6）能否提供线索？

**Q4:** 1000 样本性能下降是否在 3 个 seeds 中一致出现？训练 loss 曲线是否显示过拟合迹象？

**Q5:** 如果将 9-class 策略标签合并为 5 个类别，性能是否下降至 topic variant 水平？这可以区分类别数量和标签相关性的各自贡献。

## Missing References

- **Galinkin & Sablotny (2024)**. "Improved LLM Jailbreak Detection via Pretrained Embeddings." arXiv:2412.01547. 最直接相关的已发表工作——同样使用预训练 encoder embeddings 进行越狱检测。两位 Reviewer 共识应补充。[R22 遗留]
- **Perez and Wang (2022)** red teaming 工作。R1 建议补充，R2 指出论文可能已引用 Perez et al. (2022)，需确认是否为同一工作。

## External Review (Stanford Agentic Reviewer)

未请求。

## Visual Layout Check（非评分项）

视觉审查已完成（3 warnings, 9 info items）。

**Warnings:**
1. **[Page 9] Conclusion 溢出**: Section 6 (Conclusion) 正文溢出约 3-4 行到第 9 页顶部，之后才是 Limitations。EMNLP 2026 正文限 8 页（Limitations 不计入）。**注意**: Round 20 曾将类似报告标记为 FALSE POSITIVE（"Sections 1-6 在 p1-p8"），本轮视觉审查重新检测到溢出——可能是后续修改导致的回归。建议作者确认 Section 6 最后一行是否在第 8 页内，若确实溢出需压缩 Discussion/Conclusion。
2. **[Pages 3-5] 纯文本区间过长**: Related Work (p3) + Experiments Setup (p5) 均为纯文本，中间仅 p4 右栏有 Table 1，连续 3 页缺乏视觉锚点。建议将 Figure 2 或某关键表格前移。
3. **[Page 15] Figure 5 heatmap 标注过小**: 三个 heatmap 并排，cell 内数值在 150dpi 下偏小，打印可能难辨。

**Info 亮点**: Figure 1 架构图位置好（p2 顶部）、全文表格 booktabs 风格统一、未发现 LaTeX 渲染错误或未解析引用。正文 display item 密度 1.1/页，符合实证论文标准。

## Overall Assessment

**评分: 3.0 (Findings)**
**置信度: 4/5 (High)**

本文是一项全面、系统的消融研究，实验设计质量高，分析工具丰富。但以下因素阻碍其达到 Conference (4.0) 水平：

1. **核心叙事在真实数据上失效**: ToxicChat hierarchy 反转 + WildChat 68.1% FPR 表明论文的 "evidence hierarchy" 仅在合成数据生态系统内成立。这不是 soundness 缺陷（论文报告了这些结果），但严重限制了结论的实际影响力。
2. **方法新颖性有限**: 论文本质上是将已知的 DAPT 范式（Gururangan et al., 2020）应用于新领域，方法层面无创新。其贡献在于 empirical findings（scrambled equivalence、boundary conditions），但这些发现中的核心一条（classification > MLM ranking）可从先行工作预期。
3. **Claims 多处超出实证范围**: "reusable template"（单一任务）、"label semantics don't matter"（仅 template attacks）、"unexpected"（可预期）等表述需要系统性收窄。

**为何不低于 3.0**: 实验执行质量高，因子分解设计在安全检测领域有参考价值，scrambled label equivalence 和 boundary conditions 的发现对社区有实用启示。论文作为 Findings paper 的贡献足够。

**为何不高于 3.0**: 核心叙事的真实数据泛化失败是结构性问题而非措辞问题——即使完美修改 framing，论文的主要 take-away 仍然是 "DAPT hierarchy exists but only in synthetic settings"，这限制了 impact。方法新颖性不足以支撑 Conference 推荐。

## Detailed Comments

### Abstract
- "indicating the classification objective's structural role—not label semantics—drives generalization" 需限定为 template attacks（MF2）
- "this hierarchy reverses" 句法模糊，修饰对象不清（M1）
- 三大 "unexpected findings" 中的 finding (i) 应降格为 "quantifying the magnitude"（MF3）

### Section 1 (Introduction)
- "Evidence hierarchy" 首次使用处需操作性定义（SF7）
- 三大贡献的 novelty framing 需调整——contribution #1 从 "unexpected" 改为 "systematic quantification"（MF3）

### Section 3 (Method)
- BiGRU 选择理由需补充说明——正文应明确 mean pooling 可替代（SF9）

### Section 4.3 (Evidence Hierarchy)
- 正文有 ActorAttack d=0.44 的限定，但 abstract 缺失——需保持一致（MF2）
- Topic 5-class vs 9-class 类别数量混淆需讨论或补充控制实验（SF4）

### Section 4.4 (Scale Effects)
- "DAPT unnecessary at 355M" 需区分 "unnecessary" vs "harmful"，讨论 CKA 线索（SF5）

### Section 4.6 (ToxicChat)
- 需从 1 句话扩展为 1-2 段深入分析，隔离 single-turn vs distributional 因素（MF1）

### Section 4.7 (Data Scale)
- 1000 样本下降需补充 seed 一致性和 training loss 证据（SF6）

### Section 5 (Discussion)
- 增加 scrambled equivalence 的机制讨论段落（M2）
- WildChat FPR 作为合成数据训练局限的讨论需更充分（SF2）

### Section 6 (Conclusion)
- "reusable template" 限定范围（SF8）
- ToxicChat 反转的条件性结论需加深（MF1）
- 检查是否溢出到 page 9（Visual Check Warning #1）

### Appendix
- TOST δ=5pp 补充 practical significance 论证（SF3）
- 策略标注验证样本量增加至≥100，报告 per-class κ（SF10）
- 确认 Galinkin & Sablotny (2024) 和 Perez and Wang (2022) 引用状态