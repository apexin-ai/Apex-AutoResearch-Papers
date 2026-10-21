---
round: 4
review_mode: fresh
overall_score: 3.0 (Findings)
timestamp: 2026-05-20T05:39:43.512978+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告 — Round 4 (Fresh Review)

**论文**: *What Makes Multi-Turn Jailbreaks Detectable? Domain Exposure Bridges the Cross-Attack Gap*
**Venue**: EMNLP 2026 (ARR May cycle)
**Reviewer 编排**: 2 名 Reviewer（R1: 方法严谨性+实验设计; R2: 新颖性+完整性+Related Work）
**审稿轮次**: Round 1 独立审稿 → 交叉分享 → 收敛（1 轮收敛，无需 Round 2）

---

## Summary

论文提出 DisPeD，一个两阶段多轮越狱检测 pipeline（Stage 1: 编码器领域适应，Stage 2: 冻结编码器 + BiGRU 时序分类），通过 7 个 Stage-1 变体的 controlled ablation 分解跨攻击泛化的驱动因素。在 4 个攻击家族、3 个编码器规模、2 种训练组合上进行系统实验。核心发现：(1) 分类 DAPT 在合成 OOD 上是最稳健变体；(2) MLM 单独可关闭约 60pp OOD 差距但在 mixed-LLM 条件下崩溃；(3) scrambled labels ≈ correct labels（标签正确性不影响检测）；(4) 编码器容量与 DAPT 必要性呈负相关。

---

## Strengths

**S1. 系统化的消融框架（R1+R2 共识）。** 7 个 Stage-1 变体系统隔离单一因素，frozen-encoder 策略确保公平比较。这种 "先拆解再组装" 的方法论为理解跨攻击泛化提供了清晰的分解视角。在 NLP 安全领域，这种程度的 controlled ablation 较为罕见。

**S2. 有价值的负面结果（R1+R2 共识）。** Scrambled labels ≈ correct labels（McNemar p>0.13, TOST p<0.01）揭示了 classification supervision 的核心机制在于表征空间压缩而非 label semantics。Mean pooling ≈ BiGRU 表明检测依赖逐 turn 表征而非序列顺序。这些负面结果对社区理解 supervised fine-tuning 机制有启发意义。

**S3. 多维度分析工具箱（R1+R2 共识）。** CKA 相似性分析、TOST 等价检验、BCa bootstrap CI、paired permutation test、对抗扰动实验、策略轨迹分析、t-SNE 可视化——多角度交叉验证增强了核心发现的说服力。

**S4. 实用导向的轻量级架构（R1）。** 184M 参数 DeBERTa-v3 + BiGRU 在 OOD 上超越 GPT-5.5 级 LLM-as-judge（Appendix A），总计 <4 GPU-hours，部署和复现成本极低。

**S5. 写作质量与 Limitations 诚实度（R1+R2 共识）。** 叙事线索清晰，实验逻辑串联合理。Limitations section 覆盖了数据多样性、标注质量、OOD 策略预测、FITD 区分能力、单轮局限、计算成本等，相当诚实。补充材料完整（LLM baseline、全 prefix 结果、扰动详细结果、CKA/t-SNE 可视化、跨 LLM 验证、数据规模验证、可复现性细节）。

---

## Weaknesses

### Must-Fix（影响接收决定）

**N1. [critical] 核心 claim "classification-based DAPT is universally robust" 与人类数据严重矛盾。**
- 位置：Abstract, Section 4.5 (Table 5), Conclusion
- 问题：ToxicChat 人类数据上 JB-MLM (F1=0.897±0.013) >> 9-class (F1=0.596±0.087)，排序逆转幅度达 30pp。论文在 Section 4.5 提及排序差异但立即转向 positive framing（"domain exposure transfers to human-written attacks"），未直接面对这一逆转对 "universally robust" claim 的冲击。在论文的唯一人类数据验证中，分类监督反而损害了迁移能力。
- **R1+R2 共识**：两位 Reviewer 均将此视为论文最严重的问题。R2 补充：classification supervision 可能对合成数据特定模式过拟合。
- 建议：(1) 将 "universally robust" 修改为 "robust within synthetic multi-turn OOD evaluation"；(2) 对 ToxicChat 排序逆转进行深入分析；(3) 如需维持 "universal" claim，必须提供多轮人类数据验证。

**N2. [critical] Mixed-LLM 条件下分类 DAPT 绝对性能过低。**
- 位置：Appendix I (Table 13), Section 5
- 问题：9-class 在 DD OOD 上仅 F1=0.422±0.045，接近二分类随机水平。"最强变体"在实践中不可用。论文将此结果放在 Appendix 而非主文，暗示作者意识到不利。
- **R1+R2 共识**：两位 Reviewer 均认为论文未充分区分 "最优相对排序" 与 "实际可部署性能"。
- 建议：(1) 明确承认绝对性能不足；(2) 提供 FP/FN error decomposition；(3) 讨论达到可用性能所需的数据规模。

**N3. [critical] 完全依赖合成数据，缺少多轮人类数据验证。**
- 位置：Section 4.1, 4.5, 7 (Limitations)
- 问题：所有训练和 OOD 评估数据均由 Qwen3-8B 生成。检测器可能学习 Qwen3-8B 特有语言风格而非 jailbreak 本质特征。ToxicChat 验证存在 modality mismatch（single-turn vs. multi-turn）。论文自己承认 "the multi-turn evidence hierarchy requires multi-turn human data to validate"。Cross-LLM 实验（Table 11-12）暴露了跨 LLM 泛化的脆弱性（Llama benign 文本上 FP rate 高达 88-90%）。
- **R1+R2 共识**：这是论文最大的外部效度缺陷。
- 建议：至少增加一个多轮人类数据评估集（如 MHJ 数据集），或在 Abstract/Conclusion 中显著降低 claim 普适性。

### Should-Fix（影响评分但不一票否决）

**W1. 缺少与现有多轮越狱防御方法的直接实验对比。**
- 位置：Section 4, Table 2
- 问题：引用了 DeepContext、BIID、G-Guard、SafeDream 但无实验对比。唯一 baseline 是 TF-IDF LR 和 LLM-as-judge（极弱 baseline）。
- **R2 Must-Fix, R1 AGREE 但认为对 ablation 论文可适度降低要求。** 综合判断为 Should-Fix。
- 建议：至少补充 1 个可复现方法作为参照点。

**W2. Title claim 在 mixed-LLM 条件下被部分否定。**
- 如 "domain exposure" 指 MLM，则 mixed-LLM 中崩溃（Table 13）直接否定标题。如指广义领域接触（含分类 DAPT），则 F1=0.422 使这座 "bridge" 几乎坍塌。标题过于笼统。

**W3. "Capacity-dependent pattern" 基于 3 个跨架构编码器，统计支撑不足。**
- DeBERTa-v3-base (184M) vs. RoBERTa-base (125M) vs. RoBERTa-large (355M) 同时改变架构和规模。3 个数据点不足以建立 "pattern"。
- **R1+R2 共识**：建议降级为 observation 或补充同架构 scaling。

**W4. 消融中 binary jailbreak intent head 始终存在。**
- 所有分类变体均含 binary head，无法完全区分策略分类 vs. 越狱信号的贡献。
- **R2 partial rebut**：Binary vs. 9-class 数据部分回答此问题（两者 F1 几乎无差异），但缺少 "strategy-only（无 binary head）" 变体。

**W5. TOST 等价检验 δ=5pp 缺乏安全领域论证。**
- 在安全关键应用中 5pp 差距可能意味着每 20 个 jailbreak 中多漏检 1 个。需要 sensitivity analysis（δ=2pp, 3pp）。

**W6. 3-seed 评估在高方差条件下可靠性不足。**
- ToxicChat 9-class std=0.087（95% CI ≈ [0.449, 0.743]，区间极宽），Mixed-LLM MLM std=0.466。关键条件需 5-10 seeds。

**W7. DD 作为 OOD 基准有效性存疑。**
- TF-IDF 在 DD 上 F1=0.961，说明 DD 包含 trivially detectable 的词汇特征。"Cross-attack generalization" claim 实质上主要依赖 ActorAttack 一个评估集。

**W8. 编码器规模局限于小模型（≤355M）。**
- 现有 safety classifiers（Llama Guard 3, WildGuard）使用 7B+。论文未讨论 findings 在 LLM-scale 是否成立。

**W9. 参考文献格式问题。**
- han2024wildguard 首作者应为 Choi，chao2023pair 年份应为 2025，he2023debertav3 年份应为 2021，anthropic2025constitutional 作者应为 Sharma 等。

### Minor

**M1.** DisPeD 缩写未展开全称。
**M2.** Stage 1 多任务损失权重（α=0.3）选择标准不明确（所有配置 IID F1 均为 1.0）。
**M3.** MLM-only IID 结果基于单 seed，可比性降低。
**M4.** Figure 2 应加 95% CI band。
**M5.** Topic 变体在某些指标上优于 9-class 的异常表现未充分解释。

---

## Reviewer Consensus

以下关键问题两位 Reviewer 达成共识（标注 [AGREE]）：

1. **[AGREE] ToxicChat 排序逆转是核心问题**：MLM >> 9-class 在人类数据上直接推翻 "universally robust" claim。两位均视为 critical。
2. **[AGREE] Mixed-LLM 绝对性能不足**：F1=0.422 不可部署，需区分相对排序与绝对性能。
3. **[AGREE] 合成数据依赖**：所有多轮结论建立在 Qwen3-8B 数据上，缺少多轮人类验证。
4. **[AGREE] Capacity-dependent pattern 架构混淆**：3 个跨架构编码器不足以建立 "pattern"。
5. **[AGREE] TOST δ=5pp 需论证**：安全领域需更严格的等价标准。
6. **[AGREE] DD 基准有效性存疑**：TF-IDF 近乎完美，说明 DD 词汇可分性过高。
7. **[AGREE] 3-seed 高方差条件可靠性不足**：关键条件需更多 seed。

---

## Reviewer Divergence

1. **缺少 SOTA 对比**：R2 视为 Must-Fix（W1），R1 同意缺陷但认为对 ablation 论文可适度降低要求。→ 综合为 Should-Fix。
2. **Binary head 混淆变量**（W4）：R1 视为 Should-Fix，R2 partial rebut 认为 Binary vs 9-class 部分回答了问题。两位均同意 "strategy-only" 变体是理想的补充但非必须。
3. **Related Work 遗漏**：R2 列出 7 项工作（X-Boundary, Active Honeypot, J-DAPT, Jailbreaking Leaves a Trace, RCS, MultiBreak, M2S），R1 rebut 因缺少具体 citation 无法确认全部相关性。→ 需逐一核实后判断。
4. **9-class taxonomy 价值**：R1 质疑 OOD 策略预测仅 30.7% 精度下的价值，R2 partial rebut 认为 taxonomy 作为表征塑造工具有独立价值（scrambled ≈ correct 支持此论点），但不应宣传为可解释预测工具。
5. **评分差异**：R1 给 3.0 (Findings)，R2 给 2.5 (Borderline Findings)。差距主要来自对 novelty 的不同要求——R2 认为 DAPT for safety 是已有技术直接应用，novelty limited。

---

## Questions（需要作者澄清）

Q1. ToxicChat 上 9-class F1=0.596 vs MLM F1=0.897——如何调和此结果与 "classification-based DAPT is the only universally robust variant" 的声称？分类标签是否在合成数据上引入了不迁移到真实数据的 spurious features？

Q2. 所有分类变体均含 binary jailbreak intent head。是否做过仅保留 strategy head（去掉 jailbreak head）的实验？如果没有，如何排除 jailbreak head 是真正的关键信号？

Q3. Mixed-LLM DD OOD F1=0.422 的根本原因是什么？是 DD 的风格特异性、混合训练的分布冲突、还是数据量不足？

Q4. TOST δ=5pp 如何确定？在实际部署中 5pp F1 差异对应多少漏检/误报？

Q5. 9-class taxonomy 的 OOD 策略预测精度仅 30.7%（κ=0.126），如果可解释性不能泛化，taxonomy 的实际价值定位是什么？

Q6. Scrambled vs correct labels 的 representation CKA 相似度如何？如果 CKA 显著不同但 F1 类似，是否说明不同表征路径达到类似检测效果？

---

## Missing References

R2 指出以下可能遗漏的工作（R1 无法逐一确认，需核实后补充）：
- X-Boundary (EMNLP 2025 Findings): representation-level multi-turn jailbreak defense
- Active Honeypot Guardrail System (2025): proactive intent detection
- J-DAPT (2025): domain adaptation for jailbreak detection
- Jailbreaking Leaves a Trace (2026): internal representation analysis
- RCS (ACL 2026): representation-level jailbreak detection
- MultiBreak (2026): multi-turn jailbreak benchmark
- M2S (2025): multi-turn to single-turn reduction

注：R1 指出论文 Related Work 已覆盖多轮攻击（6 个家族）、多轮防御（8 个系统）、计算说服力（6 个框架）和迁移学习（4 个方向），覆盖面合理。但如上述工作确为已发表的直接相关工作，应补充引用。

---

## External Review (Stanford Agentic Reviewer)

外部审稿：未配置。项目配置中未启用 `external_review.paperreview_ai`。

---

## Visual Layout Check（非评分项）

视觉审查已完成（0 critical, 1 warning, 5 info）：

- **[warning]** 页 1-2 连续纯文本无 display item（Abstract + Introduction + Related Work），审稿人前 2 页看不到视觉锚点。建议将 Figure 1（架构图）前移或在页 1 加 teaser figure。
- **[info]** Figure 1 内部文字字号偏小（约正文 60-65%）。
- **[info]** Figure 2 颜色方案未确认色盲安全性。
- **[info]** 页 8 包含 4 个 section（Perturbation Analysis, Strategy Trajectory, Discussion, Conclusion），节奏偏快，Discussion/Conclusion 篇幅较短。
- **[info]** Figure 3（Appendix）轴标签字号较小，密集排列。
- **[info]** Figure 4+5（Appendix）4 个 subplot 挤在同一页。

---

## Overall Assessment

### 综合评分

| 维度 | R1 | R2 | 综合 |
|------|----|----|------|
| Soundness | 3/5 | 3/5 | **3/5** |
| Excitement | 3/5 | 2.5/5 | **2.5/5** |
| Reproducibility | 4/5 | 4/5 | **4/5** |
| Overall | 3.0 | 2.5 | **3.0 (Findings)** |
| Confidence | 4/5 | 4/5 | **4/5** |

### 综合判断：**3.0 (Findings)**

论文通过 controlled ablation 提供了有价值的 empirical insights，特别是 (1) scrambled labels ≈ correct labels 这一负面结果对理解 classification supervision 机制有独立贡献，(2) domain exposure 作为跨攻击泛化主要机制的实证分离，(3) 多维度分析工具箱（CKA, TOST, perturbation, trajectory）交叉验证增强了说服力。消融框架设计严谨，写作质量良好，可复现性信息充分。

但三个核心问题限制了论文的 impact：
1. **Claim overclaiming**：核心 claim "universally robust" 在人类数据上被直接推翻（ToxicChat: MLM >> 9-class, 30pp gap），在 mixed-LLM 条件下绝对性能不可用（F1=0.422）。
2. **External validity gap**：所有多轮结论建立在单一 LLM 合成数据上，缺少多轮人类数据验证。
3. **Missing baselines**：缺少与 DeepContext 等现有方法的直接对比，读者无法判断实际竞争力。

### 提分路径

修复以下任一组合可提升至 **3.5 (Borderline Conference)**：
- **路径 A**（claim 修正）：修改 "universally robust" 为 "robust within synthetic OOD" + 深入分析 ToxicChat 排序逆转 + 修改标题加边界条件
- **路径 B**（数据补充）：增加多轮人类数据验证（如 MHJ）+ 补充 1-2 个 SOTA baseline

同时修复 A+B 可冲击 **4.0 (Conference)**。

---

## Detailed Comments

### Abstract
- "classification-based domain adaptation is the only universally robust variant" 需限定为 synthetic OOD
- "condition-dependent" 的表述不够明确——合成 vs 人类数据的条件依赖是论文最重要的 nuance
- 数值密度适中（~5 个 headline numbers），比前期版本改善

### Introduction (Section 1)
- 第四段结果预览仍偏长（~200 words, 15+ 数值），建议压缩
- 三个 contribution 表述准确但 Contribution 2 ("capacity-dependent pattern") 基于 3 个编码器过于自信
- Vanilla baseline 与 DeepContext 的关系措辞需统一（Section 4.1 说 "corresponds to DeepContext architecture"，但未做直接对比）

### Related Work (Section 2)
- 覆盖面合理（4 个维度），但可能遗漏近期 2025-2026 工作（待核实）
- 最后一段 "Our ablation fills this gap" 的过渡自然

### Method (Section 3)
- 消融设计总体严谨
- Table 1 清晰展示 7 个变体
- Figure 1 架构图存在但文字偏小
- DisPeD 全称缺失
- Binary head 在所有分类变体中始终存在是一个未被显式讨论的设计选择

### Experiments (Section 4)
- Section 4.2 (Cross-Attack): 核心表格清晰，TF-IDF baseline 有效建立 lexical vs beyond-lexical 对比
- Section 4.3 (Decomposition): evidence hierarchy 是论文最有价值的贡献，但 DD 的 lexical separability 削弱了部分结论的力度
- Section 4.4 (Cross-Encoder): 3 个编码器的 capacity pattern 有趣但 under-powered
- Section 4.5 (Human Data): 最关键的一节——排序逆转被讨论但未充分对待其对核心 claim 的影响
- Section 4.6 (Perturbation): 结果有价值但正文占比可再压缩
- Section 4.7 (Strategy): OOD 策略预测精度低（κ=0.126）限制了可解释性 claim

### Discussion (Section 5)
- Topic shortcut confound 讨论有价值
- Single-LLM confound 讨论诚实但未到位——mixed-LLM 结果在 Appendix 而非主文
- Encoder capacity confound 需更明确的 caveat

### Conclusion (Section 6)
- 过短（约 1/4 栏），建议扩充

### Limitations (Section 7)
- 覆盖全面且诚实
- 缺一个重要讨论：ToxicChat 排序逆转对核心 claim 的影响

### Appendix
- 完整且有组织
- Mixed-LLM 结果（Appendix I）放在附录而非主文，降低了论文的透明度

### 格式合规
- 页数：8 页正文 ✓
- Limitations section：存在且充实 ✓
- Responsible NLP Research Checklist：存在且完整 ✓
- 匿名性：Anonymous ACL submission ✓
- 引用格式：需修正若干 bib 条目（首作者、年份等）
