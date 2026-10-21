---
round: 16
review_mode: fresh
overall_score: 3.0
timestamp: 2026-05-22T16:24:53.909340+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告 — Round 16 (fresh)

**论文**: DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection
**Venue**: EMNLP 2026 (ARR May 2026)
**截止日期**: 2026-05-25
**审稿模式**: 重新审稿 (fresh)
**Reviewer 编排**: 2 人（R1: 方法严谨性+实验设计; R2: 新颖性+完整性+相关工作+写作+格式）

---

## Summary

本文对 encoder adaptation 在多轮越狱检测中的跨攻击泛化能力进行了系统性控制研究。通过 13 种 encoder 配置（7 个 Stage-1 变体 × DeBERTa-v3/RoBERTa 等多架构），在合成多轮对话数据上分解了跨攻击泛化的驱动因素。核心发现：(1) 分类监督式 DAPT 将 OOD 检测从 vanilla 的 F1=0.26–0.31 恢复到 0.97–1.0；(2) Scrambled labels 与语义正确标签表现相当（TOST confirmed, d<0.1 on template attacks），表明分类目标结构本身（而非标签语义）驱动判别性压缩；(3) 结构复杂攻击（ActorAttack）存在复杂度依赖的泛化边界（d=0.44）。论文提出 DisPeD 两阶段 frozen pipeline（Stage 1 turn-level encoder adaptation + Stage 2 BiGRU conversation-level classification），推理速度 24.3× 优于 LLM-as-judge。

---

## Strengths

**S1. 范本级受控实验设计。** 7 个 Stage-1 变体共享完全相同的 Stage-2 BiGRU pipeline（Table 1），每个变体仅改变预训练目标，冻结 Stage-1 后下游完全一致。这是本领域罕见的真正控制变量的消融研究，使因果归因比大多数 ML 安全论文更可信。[R1 S1, R2 S1, 共识]

**S2. 统计方法论远超同领域水准。** TOST 等价检验（3/5/10-seed 分层）、BCa bootstrap 95% CI（10,000 resamples）、permutation test（10,000 permutations）、cross-seed 独立性验证、cross-hardware 复现（RTX PRO 6000, 5 seeds）——在 NLP 安全论文中极为罕见。[R1 S2]

**S3. Scrambled labels 发现有真正新意。** 任何（domain-relevant 的）确定性标签分区都能产生与语义正确标签相当的判别性压缩（Fisher ≥ 2.6），这非平凡地连接到 Zhang et al. (2021) 的分类修改表征理论框架。[R1 S3, R2 S2, 共识]

**S4. 附录质量极高（17 页，A–Z.1）。** 覆盖 error analysis、perturbation robustness、cross-architecture、embedding visualization、cross-LLM、dataset scale、TOST sensitivity、frozen probing、layer-wise analysis、efficiency、data efficiency 等。几乎每个潜在审稿问题都有对应实验。[R1 S5, R2 S3, 共识]

**S5. Negative results 的诚实报告。** 论文坦诚报告 temporal modeling 不重要（mean pooling ≈ BiGRU）、ToxicChat 上 evidence hierarchy 反转、Topic 监督有害、mixed-LLM 中 MLM 崩溃等 negative/unexpected findings。[R2 S5]

**S6. 实用性强。** 24.3× 推理加速（DeBERTa+BiGRU 13.1ms vs Qwen3-8B 318.5ms），868MB GPU 显存，使部署在消费级硬件上切实可行。[R1 S4, R2 S4]

---

## Weaknesses

### Must-Fix（影响接收决定）

**MF1. [critical] Turn count 分布零重叠构成潜在分类捷径** [R1 N1, R2 交叉 AGREE]

良性对话 12–20 turns，越狱对话 3–10 turns，分布完全无重叠。论文提供了三个缓解论据（truncation FPR=0%、K=1 检测 F1=0.673、vanilla 有同等长度信息但失败），但均不充分：

- K=1 F1=0.673 显著低于 full-length F1≈0.97+，说明长度信息在贡献检测性能
- Adversarial padding（Appendix U, Table 31 Part C）显示将 ActorAttack 对话 padding 到 15+ turns 后检测暴跌 57pp，直接支撑长度作为 contributing factor
- Truncation 只验证了一个方向（短良性→仍判良性），未验证反方向（长越狱→仍判越狱）
- Vanilla 反驳有说服力（长度不 sufficient）但不排除 DAPT 后模型同时学到内容+长度特征

此 issue 自 Round 9 持续至今（R9-W1），Appendix U 有控制实验但仍不足以排除 confound。

**所需修改**：构建 turn count 重叠的数据集（如 benign 和 jailbreak 均 5–15 turns）验证检测性能；或训练 turn-count-only baseline 量化长度信号上限。

---

**MF2. [critical] "Any deterministic partition suffices" 声称与 Topic 变体失败直接矛盾** [R1 N2, R2 交叉 AGREE]

这是论文三个核心 contribution 之一（Section 1, Contribution 2）。仅测试了 3 个有效 partition（9-class, binary, scrambled），但 **Topic 变体**（5-class topic classification，同样是 domain data 上的确定性 partition）在 full-length 上 DD OOD F1=0.541±0.207（Table 3），直接反例了 "any partition"。

Abstract 声称 "any deterministic label partition triggers discriminative compression"，但 Discussion (Section 5) 承认需要 "domain-relevant label partitioning"——内部自相矛盾。

如果 claim 修正为 "domain-relevant partition on domain data helps"，novelty 大幅缩水——本质上是 Gururangan et al. (2020) DAPT 结论的特例应用。Scrambled ≈ 9-class 的发现仍有新意（说明语义正确性不必要），但 "any partition" 的 universal claim 不成立。

**所需修改**：(1) 修正 Abstract/Intro 为 "any domain-relevant classification objective"，明确 Topic 失败；(2) 增加更多 partition 实验（如 10 个不同随机二分类 partition）；(3) 讨论为什么 Topic 失败——是 label space 太小、task alignment 不足、还是域相关性缺失。

---

**MF3. [critical] 全合成单源数据严重限制结论可推广性** [R1 N3, R2 N2, 共识]

训练数据（500 conversations）、OOD 评估数据、策略标注——全部由 Qwen3-8B 生成/标注。两个关键实证证据质疑结论的泛化性：

1. **Cross-LLM 训练中 MLM 崩溃**（Table 14）：混入 Llama 3.1-8B 后 MLM 变体崩溃到 vanilla 水平（F1≈0.28），说明 evidence hierarchy 中 "domain exposure 是最关键因素" 可能仅在同源数据下成立。
2. **ToxicChat 上 evidence hierarchy 完全反转**（Table 5）：JB-MLM leads（0.837±0.013）而 9-class 更低（0.596±0.087）。虽然 ToxicChat 是单轮数据（任务不同），但 hierarchy 反转至少说明发现是 condition-specific 的。

唯一的人类数据验证（ToxicChat）是单轮数据，无法验证核心的多轮检测 claim。论文声称的 "cross-attack generalization" 实质是 "cross-synthetic-attack generalization within single-LLM data"。

此 issue 自 Round 13 持续至今（R13-N1）。

**所需修改**：(1) Abstract/Conclusion 中将 claim scope 限定为 "on synthetic persuasion-based multi-turn jailbreaks"；(2) 增加至少一个非 Qwen3-8B 来源的多轮 OOD 评估；(3) 更显著地讨论 ToxicChat hierarchy 反转的含义及其对核心结论的限制。

---

### Should-Fix（影响评分但不一票否决）

**SF1. "Disentangled" 术语误用** [R2 N1 critical → R1 交叉 AGREE 但建议降级; Director 判定 should-fix]

"Disentangled" 在 ML 中指学习独立变化因子的表征（β-VAE, InfoGAN, DCI framework），本文的两阶段 frozen pipeline 是 decomposed/decoupled architecture，无关。Footnote 1 的免责声明反而暴露了术语选择的不当。

**所需修改**：将 "Disentangled" 替换为 "Decomposed" 或 "Decoupled"（如 DecomPeD/DecoPeD）。

---

**SF2. Temporal modeling negative finding 讨论不足** [R2 W2, R1 交叉 AGREE, R1 称自己审查中遗漏的重要发现]

Mean pooling ≈ BiGRU（F1 gap ≤ 1pp, Appendix T Table 29）+ turn-order shuffling negligible（|Δ| < 1pp, Section 4.3）意味着模型未学到有意义的时序动态。"Multi-turn jailbreak detection" 实质是 "aggregated turn-level anomaly detection"。这对论文的叙事有重大影响，但主文仅一句话带过。

**所需修改**：Discussion 增加一段讨论——如果 turn order 不重要，multi-turn detection 的本质是什么？这是一个更弱但更诚实的 claim。

---

**SF3. Benign-side 分析不足以支撑实用性声称** [R2 N3 critical → R1 交叉 AGREE 但建议降级; Director 判定 should-fix]

WildChat FPR=68.1%（Table 19）远超可部署阈值。Diversification pilot（Appendix P, 150 WildChat conversations, n=49 评估）被标注为 preliminary 但 Conclusion 声称 "FPR 65–68% → 0–1.5% via 10–25 conversations" 未加充分限定。WildChat 评估是 IID（Table 20 明确标注）。

核心贡献是 representation learning 的受控分析，非 deployment-ready 系统。但 Conclusion 的措辞暗示了实用价值。

**所需修改**：Conclusion 中明确标注 benign-side 结果为 preliminary/pilot，注明 IID 评估条件。

---

**SF4. 单一 encoder 架构限制发现普适性** [R1 W4, R2 W1, 共识]

深度分析仅在 DeBERTa-v3-base 上。Table 4 的 cross-architecture 对比混淆了架构和规模差异（DeBERTa-v3-base 184M vs. RoBERTa-large 355M）。未测试 decoder-based encoder 或更现代的架构。Appendix Q 有 BERT-base proxy 间接验证。

**所需修改**：至少补充同规模对比（RoBERTa-base vs DeBERTa-v3-base），或在 Limitations 中讨论对 decoder-based 模型的预期适用性。

---

**SF5. Discriminative compression 因果故事不完整** [R1 W5, R2 交叉 AGREE; 与 R15-SF1 关联]

论文展示 DAPT → SVD compression → OOD detection 的相关性（Appendix S, Tables 27–28），但未建立因果关系。IID-only SVD 对照（cosine sim=0.974）部分缓解了 R15 的数据泄漏问题，但仍缺少 compression-controlled 实验（如通过正则化控制 compression 程度验证对 OOD 的影响）。

**所需修改**：弱化因果语言（"enables" → "is associated with"），或增加 compression-controlled 实验。

---

**SF6. 策略标注质量对核心声称的支撑力不足** [R1 W2, R2 M1, 共识]

κ=0.78, n=50，9 个类别平均每类仅 ~5.5 个验证样本。如果 9-class taxonomy 是核心实验变量，其标注质量需要更强的验证。

**所需修改**：增加标注验证样本量至 n=200+，或引入第二个 human annotator。

---

**SF7. 数据划分描述不够清晰** [R1 W6, R2 交叉 AGREE]

Section 4.1 中 250+250=500, split 350/74/76 的数学关系和 IID/OOD 边界首次阅读时易混淆。

**所需修改**：Section 4.1 开头明确列出 IID 训练集和 OOD 评估集的完整组成。

---

## Reviewer Consensus

| 问题 | R1 | R2 | 状态 |
|------|-----|-----|------|
| Turn count confound | N1 critical | 交叉 AGREE | **共识 critical** |
| "Any partition" overclaim | N2 critical | 交叉 AGREE | **共识 critical** |
| 合成单源数据局限性 | N3 critical | N2 critical | **共识 critical** |
| "Disentangled" 术语 | 交叉 AGREE (降级 should-fix) | N1 critical | **共识 should-fix** |
| Temporal modeling 讨论不足 | 交叉 AGREE (遗漏) | W2 | **共识 should-fix** |
| Benign-side 分析不足 | 交叉 AGREE (降级 should-fix) | N3 critical | **共识 should-fix** |
| 单一 encoder 架构 | W4 | W1 | **共识 should-fix** |
| Discriminative compression 因果 | W5 | 交叉 AGREE | **共识 should-fix** |
| 策略标注质量 | W2 | M1 | **共识 should-fix** |

## Reviewer Divergence

| 问题 | R1 | R2 | Director 判定 |
|------|-----|-----|---------------|
| Two-axis framework 新颖性 | REBUT: 不同 failure mode 需不同解法，非 trivial | W3: FPR/FNR 权衡重新包装 | R1 更有说服力——attack-side (representation quality) 和 benign-side (distribution shift) 确实需要不同解法，但同意 "framework" 措辞过重，建议改为 "decomposition" |
| 效率对比公平性 | W3: 参数量差 43 倍，不对等 | REBUT: 部署场景下参数量差异是决策因素 | R2 更有说服力——效率对比定位为 deployment cost analysis 是合理的，但论文应明确这一定位 |
| 3-seed 统计检验力 | REBUT: 论文实际用 3/5/10-seed 分层 | M2: 3-seed 有限 | R1 正确——R2 遗漏了 Appendix L 的 5/10-seed 分析 |
| Overall 评分 | 3.5 Borderline Conference | 3.0 Findings | 见下 |

---

## Questions

1. **Turn count 重叠数据集上 9-class DAPT 是否仍保持 F1≥0.97？** 这是排除长度 confound 的最直接实验。[R1 Q1, R2 交叉 AGREE]

2. **Scrambled variant 是否测试了多个不同随机排列？** 如果仅一个排列，存在 "幸运排列" 风险。至少需要 5–10 个不同排列的结果分布。[R1 Q2, R2 交叉 AGREE]

3. **如何先验地定义 "domain-relevant partition"？** 如果定义是 "产生有效 compression 的 partition"，则变成循环论证。[R1 Q3, R2 交叉 AGREE]

4. **Cross-LLM 中 MLM 崩溃对 evidence hierarchy 的 generality 意味什么？** 如果 "domain exposure 是最关键因素" 仅在同源数据下成立，整个 evidence hierarchy 的 scope 需重新界定。[R1 Q4, R2 交叉 AGREE]

5. **E2E fine-tuning 在 AA 上 +5.8pp——frozen pipeline 的设计选择是否牺牲了实际性能？** R2 部分 REBUT: Appendix N 数据显示两者在大多数条件下相当，+5.8pp 来自特定条件。[R1 Q6]

---

## Missing References

以下引用由 Reviewer 提出，**需核实真实性后再决定是否要求补充**（R1 对 R2 部分引用的真实性存疑）：

**R2 提出：**
1. Yang et al. (2025), "Multi-Turn Jailbreaks Are Simpler Than They Seem" — 如真实存在，直接挑战本文关于多轮检测必要性的前提假设，**必须讨论**
2. Souly et al. (2024), "A StrongREJECT for Empty Jailbreaks" (NeurIPS 2024) — jailbreak 评估方法论
3. "State-Dependent Safety Failures in Multi-Turn Language Model Interaction" (2026)
4. "Mass-Scale Analysis of In-the-Wild Conversations Reveals Complexity Bounds on LLM Jailbreaking" (2025)

**R1 提出：**
5. Li et al. (2024), "Inference-time intervention" — probe-based safety 方法，与 discriminative subspace probe 有概念联系
6. Ke et al. (2023) — continual pretraining 机制分析
7. JailbreakBench 多轮扩展

---

## External Review (Stanford Agentic Reviewer)

外部审稿：未启用。

---

## Visual Layout Check（非评分项）

**状态**: done（耗时 ~3.5 分钟）

**Findings** (0 critical, 0 warning, 8 info):
- Page 1: 首页无视觉锚点（纯文本），Figure 1 在 p.2 顶部出现。对 method-driven 论文可接受。
- Page 4: 唯一纯文本页（Section 3.3 + 4 开头），内容为方法说明，可接受。
- Page 5: Figure 2 柱状图颜色方案区分度足够，建议确认色盲友好；Table 2 格式规范。
- Page 14: Tables 8-9 数据密集字号偏小，作为 appendix 可接受。
- Page 15: Figure 3 热力图轴标签字号较小，建议确认打印辨识度。
- Page 16: 单页含 Figure 4 + Figure 5 + Tables，密度高但无溢出。
- Page 22: Figure 6 line chart 颜色区分清晰。

**格式合规性**：
- 正文页数 ≤ 8: ✅ (Section 7 Limitations 从 page 9 开始)
- 匿名性: ✅ (Anonymous ACL submission，未发现泄露)
- ACL review 模板: ✅ (双栏格式正确，行号可见)
- Limitations: ✅ (Section 7, 覆盖 3 点)
- Ethics Statement: ✅ (p.9)
- Responsible NLP Checklist: N/A (按规则在 OpenReview form 中)

---

## Overall Assessment

**评分: 3.0 (Findings)**
**置信度: 4/5** (两位 Reviewer 均仔细通读全文含 17 页附录)

**评分理由**:

R1 给 3.5 (Borderline Conference)，R2 给 3.0 (Findings)。Director 判定 **3.0 (Findings)**，理由如下：

**支持 Findings 的因素**：
- 实验设计方法论确实是 NLP 安全领域的范本（controlled ablation + rigorous statistics），这一方法论贡献本身有价值
- Scrambled labels 发现有真正新意，值得发表
- 17 页附录的 thoroughness 在同类论文中罕见

**阻碍 Conference 的三个核心 blocker**：

1. **Turn count confound 未被排除**（MF1）：benign 12–20 turns vs jailbreak 3–10 turns 的零重叠是一个严重的方法论缺陷。Adversarial padding 后 AA 暴跌 57pp 直接表明长度是重要的 contributing factor。此 issue 自 Round 9 持续至今，未被充分解决。

2. **核心 claim 的逻辑缺陷**（MF2）：Abstract 中 "any deterministic label partition" 与 Discussion 中 "domain-relevant partitioning is necessary" 的自相矛盾，加上 Topic 变体作为直接反例，使 Contribution 2 的 novelty 大幅缩水。修正后 claim 本质是 "domain-relevant DAPT 比 MLM 好"，这更接近 Gururangan et al. (2020) 的增量应用。

3. **结论的外部效度严重不足**（MF3）：全合成单源数据 + ToxicChat 上 evidence hierarchy 反转 + cross-LLM 中 MLM 崩溃，共同指向核心发现可能特定于 synthetic Qwen3-8B data。论文声称的 "cross-attack generalization" 的 scope 远超证据支撑范围。此 issue 自 Round 13 持续至今。

**提升到 Conference 的路径**：
- MF1: 提供 turn count 重叠数据集的验证结果
- MF2: 修正 "any partition" claim + 增加多个随机 partition 实验
- MF3: 限定 claim scope + 增加非 Qwen3-8B 多轮评估
- 若以上三项均完成，评分可提升至 3.5 (Borderline Conference)

---

## Detailed Comments

### Abstract
- "any deterministic label partition" 需修正为 "any domain-relevant classification objective"（MF2）
- 应在研究问题后立即限定 scope: "on synthetic persuasion-based multi-turn data"（MF3）

### Section 1 (Introduction)
- Contribution 2 的表述需与 Discussion 中的限定条件一致（MF2）
- DisPeD 命名建议更改（SF1）

### Section 3 (Method)
- Table 1 中 Topic 变体的失败应在方法描述时预告（MF2）
- Stage-2 frozen BiGRU 的设计选择可补充 E2E 对比的引用（Appendix N）

### Section 4 (Experiments)
- Section 4.1 数据划分描述需更清晰（SF7）
- Section 4.3 "Temporal modeling" 段落：mean pooling ≈ BiGRU 的 implication 需更多讨论（SF2）
- Turn count confound 需在主文中正面讨论而非仅放 Appendix（MF1）

### Section 5 (Discussion)
- "condition-specific advantage" 段落需扩展，更显著讨论 ToxicChat hierarchy 反转的含义（MF3）
- Discriminative compression 的因果语言需弱化（SF5）
- 增加 temporal modeling 无关紧要的 implication 讨论（SF2）

### Section 6 (Conclusion)
- "FPR 65–68% → 0–1.5%" 需标注 preliminary/pilot + IID 条件（SF3）
- Claim scope 全面限定（MF3）

### Section 7 (Limitations)
- 当前 3 点覆盖合理但可补充 turn count confound（MF1）和 "any partition" 限定（MF2）

---

## 跨轮次 Issue 追踪摘要

本轮与历史 issue 的关联：
- **R9-W1** (长度混淆, Round 9→16): 从 warning 升级为 critical，仍未充分解决
- **R9-W2** (ToxicChat hierarchy 反转, Round 9→16): 持续 critical
- **R13-N1** (合成单源数据, Round 13→16): 持续 critical
- **R13-N2** (WildChat FPR, Round 13→16): 有改善（3-seed + OASST2）但仍不足
- **R13-W2** (DisPeD 命名, Round 13→16): 持续 should-fix

新发现：
- **R16-N1**: "Any partition" claim 与 Topic 反例的逻辑矛盾（新 critical）
- **R16-W1**: Temporal modeling negative finding 讨论不足（新 should-fix）

完整 issue tracker 已更新至 `artifacts/review_issues.yaml`。