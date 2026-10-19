---
round: 5
review_mode: fresh
overall_score: 3.0 - Findings
timestamp: 2026-05-22T15:43:11.555911+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告 — Round 5 (Fresh Review)

**项目**: contrastive_entrain_calib
**论文**: "The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration"
**Venue**: EMNLP 2026 (ARR May 2026)
**审稿模式**: Fresh（独立初审）
**Reviewer 编排**: 2 人（R1 方法严谨性 / R2 新颖性完整性）
**交叉轮次**: 1 轮（共识达成，无需追加）

---

## Summary

论文发现当用冻结线性 probe 在对比性谄媚方向 (d_syc) 上作为 SFT 训练信号时，行为死亡（ToF=0）在 step 500 发生，而生成熵直到 step ~1840 才崩溃，产生 1,300 步的监测盲区。论文还在 GRPO（group size=2）下测试了三种 d_syc reward 形式和行为 reward-only 基线，均未能稳定超越 vanilla，同时展示 ACT（per-token SFT）作为对比参照。

---

## Strengths

1. **C2（Probe Reward Trap）是干净的贡献**：在 SFT + stopped gradients 设置下发现 behavioral death 先于 distributional collapse 1,300 步，reward 全程 +0.72，直接挑战 entropy-based early stopping 的有效性。此发现独立于 GRPO 优化动态，不受 group_size confound 影响。[R1, R2 共识]

2. **诊断链设计严谨**（§4）：F1a→F1b→F1c→F1d 四个 cosine 配置形成逐步排除的因果链，每个修复前者的 failure mode 但暴露更深层问题，是优秀的实验叙事结构。[R1, R2 共识]

3. **Limitations 讨论异常透明**：对 group_size confound、truncation、seed count、ACT 不可比性的 disclosure 水平远超平均。三个 competing hypotheses 的框架诚实地承认了无法区分的替代解释。[R1, R2 共识]

4. **Cross-model discriminability 验证充分**：Qwen3-8B (AUROC 0.827) + Llama-3-8B (0.779) 双模型验证，evidence-strength gradient 一致，排除了 model-specific artifact。[R1]

5. **Stubbornness Taxonomy**（Appendix B）：181 条 response 的 5 类手动分析，76.8% 是 refusal style 调节而非 acceptance rate 调整——有质量的定性证据。[R1]

---

## Weaknesses

### Critical（Must-Fix）

**W-C1** [R1-N1, R2-N2, 双方 AGREE] **Group_size=2 confound 使 C1 贡献无法成立**

GRPO group_size=2 远低于文献标准 8-64。R₃-only GRPO（完全不含 d_syc）同样失败（4/27 checkpoints > vanilla），强烈暗示 group_size=2 下任何 scalar reward 的 ranking diversity 不足。论文承认无法区分 hypothesis (a) d_syc 不适合 vs (b) group_size 不足，但仍将 C1 列为并列贡献。C1 实质上是 confounded observation，不可作为因果结论呈现。

→ **要求**：将 C1 从 contribution 降级为 observational finding，或补做 group_size=8/16 ablation。

**W-C2** [R1-N2, R2 PARTIALLY AGREE] **Truncation 摧毁 GRPO 训练时 d_syc 信号，但论文以 AUROC 0.827 为前提**

论文全文以 offline AUROC 0.827 建立 "discriminability 高但 reward 失败" 叙事，但训练中 max_completion_length=256 导致 80-84% response 被截断，d_syc AUROC 降至 0.60（仅略好于 chance）。C1 的失败可能主要是 signal degradation 而非 semantic gap。R2 指出此 confound 仅影响 C1（GRPO），不影响 C2（SFT probe 在完整 response 上工作）。

→ **要求**：叙事中明确区分 offline discriminability（0.827）和 training-time discriminability（0.60）；不以 0.827 作为 GRPO failure 的论证前提。

**W-C3** [R1-N3, R2, 双方 AGREE] **ACT vs GRPO 比较存在 5+ 维度 confound，不可归因**

LoRA α 差 2x（64 vs 128），modules 差 1.75x（4 vs 7），dropout/loss/supervision/data format 全不同。Table 4 + Figure 3 并列给读者 "SFT works, GRPO doesn't" 的 misleading takeaway，尽管脚注标注 "not directly comparable"。

→ **要求**：Table 4 加视觉 separator + "reference only" 标注；或统一 LoRA 配置做控制实验。

**W-C4** [R1-W2/R2-N3, 共识] **标题和泛化声明超出证据范围**

标题 "The Probe Reward Trap" 暗示通用现象，但证据仅来自单模型（Qwen3-8B）、单 run（exp-008v3）、单方向（d_syc for sycophancy）。1,300-step lag 为单次观察。R1 认为机制推理支持泛化，但同意标题需限定。

→ **要求**：标题加限定（如 "A Case Study" 或 "on Qwen3-8B"）；abstract/conclusion 中 1,300-step lag 标注 "under our configuration"。

### Warning（Should-Fix）

**W-S1** [R1-W5, R2 strongly AGREE] **§3 与 §5 内部矛盾：evidence-strength gradient vs "does not encode evidential warrant"**

§3 明确写 "d_syc encodes the degree of evidential warrant"，但 §5/§1/§8 反复声称 "d_syc encodes whether belief changed, not whether it should have"。这是核心论断的内部矛盾。需要更精确的措辞调和（如 "discriminability covaries with evidence strength" 而非 "encodes"）。

**W-S2** [R2-W2, R1 AGREE——"最有力的一条"] **SMART 讨论存在逻辑矛盾**

§7 称 "SMART applies per-step process rewards with MCTS for sycophancy. These methods succeed because target and suppressed behaviors are geometrically distinct; sycophancy breaks this condition"。但 SMART 处理的就是 sycophancy——与本文同一 target behavior。如果 sycophancy 的 geometric separability 被打破，SMART 怎么能成功？论文回避了这个矛盾。应解释 per-step granularity 如何绕过 completion-level entanglement。

**W-S3** [R2-W1, R1 AGREE] **Wu & Tang (2026) 对比缺乏定量分析**

"Geometric separability" 是论文核心解释机制，但从未量化验证。未报告 d_syc 方向上两类行为的 cosine gap 分布或 intra-class/inter-class separation 指标。

**W-S4** [R1-W1, R2 AGREE] **2 seeds 不足以支撑 GRPO 统计结论**

Cross-seed rank correlation ρ≈0.33, n<10 无统计功效。论文自称 "descriptive" 但 abstract 措辞暗示更强结论。建议增加到 3-5 seeds 或删除 cross-seed correlation。

**W-S5** [R1-W4, R2 AGREE] **ACT seed 2 仅 6/16 checkpoints evaluated**

Incomplete result。如果后续 checkpoint 出现 crash，"all exceed vanilla" 声明不成立。建议完成或删除。

**W-S6** [R1-W2, R2 PARTIALLY AGREE] **SyconScore harmonic mean 需补充 arithmetic mean**

ToF=0 时 SyconScore=0 vs arithmetic mean ~0.498，视觉冲击力差异大。Harmonic mean 设计合理但应同时报告 arithmetic mean。

**W-S7** [R1-W3, R2 AGREE] **181 对 contrastive pairs 无 human IAA**

全部由 GPT-4.1 生成和标注，无人类验证。至少应抽样 50 对做 human validation。

**W-S8** [R2-W4, R1 AGREE] **"Negative result" 与 "general principle" 定位模糊**

论文时而定位为 negative result，时而提升为 general principle（§6 geometric entanglement）。应明确选择 negative result 定位。

**W-S9** [R2-N1, R1 partial REBUT] **核心 novelty 需重新定位**

"Probe reward trap" 概念层面可从 Goodhart's law 预期。R1 反驳：temporal decoupling 量化、reward 全程 healthy、SFT 独立于 RL 三点超出 Goodhart 预测。共识：从 "we discover" 改为 "we quantify"，强调具体机制特征。

---

## Reviewer Consensus [AGREE]

1. C2（probe reward trap in SFT）是干净的贡献，独立于 GRPO confound
2. C1（GRPO failures）被 group_size=2 + truncation 双重 confound 侵蚀，应降级
3. ACT 比较不可归因（5+ 维度差异）
4. 标题和泛化声明需要 scope 限定
5. §3 与 §5 的 "evidential warrant" 表述存在内部矛盾
6. SMART 讨论存在逻辑矛盾
7. 论文应明确选择 negative result 定位

## Reviewer Divergence [REBUT]

1. **Novelty（R2-N1 vs R1 REBUT）**：R2 认为核心发现是 Goodhart 特例、novelty 不足；R1 认为 temporal decoupling 的量化和 SFT 设置独立于 RL 的特征超出了 Goodhart 一般预测。最终共识偏向 R1——novelty 存在但 framing 需精确化。

2. **Taxonomy 深度（R2-W3 vs R1 REBUT）**：R2 希望 taxonomy 有 temporal dynamics 和跨 failure mode 对比；R1 认为 8-page paper 的 appendix 已足够。Director 判断：现有 taxonomy 对于支撑论点已足够，此项不列为必改。

3. **跨模型复现需求（R2-N3 vs R1 partial REBUT）**：R2 要求在 Llama 上复现 probe trap；R1 认为机制推理 + 双模型 discriminability 验证足以支撑泛化。Director 判断：标题限定即可，不强制跨模型训练复现。

---

## Questions

1. 如果 group_size 增加到 8 或 16，R₃-only GRPO 能否超越 vanilla？这将决定 C1 的 attribution 是指向 d_syc 还是 GRPO 配置。
2. Probe reward trap 在 full-length completions（无 256-token 截断）下是否仍然出现？SFT 设置理论上不受截断影响，但未明确确认。
3. §3 的 evidence-strength gradient（AUROC 0.675→0.929）是反映 d_syc 编码了 evidential warrant，还是仅仅反映强证据下行为差异更大、更容易分离？论文需给出明确立场。

---

## Missing References

- 未发现严重遗漏。但 DPO/KTO 在 sycophancy calibration 上的实际应用工作（如有）值得讨论，目前仅在 §7 末尾一句带过。

---

## External Review

**状态**: 未请求（本轮未启用外部审稿）

---

## Visual Layout Check（非评分项）

**状态**: done（5 warnings, 0 critical, 7 info）

关键发现：
- **Warning**: 前 3 页无任何 display item（纯文本墙），建议前移 Figure 1 或加方法概览图
- **Warning**: Page 4 堆积 3 个 display item（Table 1 + Table 2 + Figure 1），节奏不均
- **Warning**: Table 1 右侧列标题拥挤重叠，Table 2 最右列 "Root Cause" 疑似被截断
- **Warning**: Figure 3 坐标轴标签偏小（≤6pt），打印后可能低于可读阈值
- **Info**: 全文无概念图/方法流程图，所有 display item 均为实验结果
- **Info**: 参考文献格式统一，无未解析引用

---

## Overall Assessment

**评分**: 3.0 / 5 — Findings

**置信度**: 4 / 5

**理由**：

论文有一个干净的核心贡献（C2，probe reward trap in SFT：behavioral death 先于 distributional collapse 1,300 步，entropy monitoring 完全失效），对社区有实践警示价值。但：

1. C1（GRPO failures）被 group_size=2 和 truncation（AUROC 降至 0.60）双重 confound 深度侵蚀，无法作为因果结论成立，论文自身承认无法区分竞争假说。
2. ACT 比较存在 5+ 维度 confound，不可归因为方法论差异。
3. 核心叙事 "high discriminability fails as reward" 对 C1 不成立（训练时 discriminability 并不高），仅对 C2 成立。
4. 标题和泛化声明超出单模型单 run 的证据范围。
5. §3 与 §5 的 evidential warrant 表述存在内部矛盾。

论文实质上只有 C2 一个不受 confound 影响的 contribution，但该 contribution 本身是 solid 的——量化了一个 entropy monitoring 的具体盲区，对 representation-based reward design 有直接指导意义。如果能（1）降级 C1，（2）修正叙事区分 offline vs training-time discriminability，（3）限定标题 scope，（4）解决 §3/§5 矛盾，论文可作为 Findings 论文接收。

**建议优先级**（按影响排序）：
1. 降级 C1 或补做 group_size ablation [决定论文走向]
2. 区分 offline/training-time discriminability，修正叙事前提 [影响可信度]
3. 标题加限定 + 明确 negative result 定位 [影响审稿人第一印象]
4. 修复 §3/§5 内部矛盾 [影响论证一致性]
5. ACT 比较加 separator + 强化不可比声明 [影响读者 takeaway]

---

## Detailed Comments

### §1 Introduction
- "we discover the probe reward trap" → 建议改为 "we quantify a temporal decoupling"，更精确地定位增量贡献
- AUROC 0.827 不应在此处作为 GRPO reward failure 的前提（训练时仅 0.60）

### §2 Experimental Framework
- §2.5 SyconScore 的 harmonic mean justification 仅一句话，建议扩展 F1-score 类比并脚注 arithmetic mean 数值

### §3 Direction Discriminability
- "This gradient indicates that d_syc encodes the degree of evidential warrant" → 与 §5 "does not condition on input validity" 矛盾。建议改为 "discriminability covaries with evidence strength, possibly because stronger evidence produces more behaviorally distinct responses"

### §4 Cosine R₁: Structural Failure
- 开头应明确警告：训练时 AUROC 仅 0.60（因 256-token 截断），failure chain 可能部分反映 signal degradation
- Table 2 "Root Cause" 列在 PDF 中疑似被截断（视觉审查发现）

### §5 The Probe Reward Trap
- 核心贡献节，证据链清晰。无重大修改意见。

### §6 Discussion
- ACT 比较段落应加强 "not directly comparable" 的措辞力度，避免读者误读 Figure 3
- Cross-seed rank correlation 报告 exact N 和 p-value，或删除该分析

### §7 Related Work
- SMART 句存在逻辑矛盾，需解释 per-step vs per-completion 的关键差异
- DPO/KTO 在 sycophancy 上的应用可扩展讨论

### §8 Conclusion
- 泛化声明加 "in our setting" 等限定词
- 1,300-step lag 标注为特定配置下的观察

### Appendix
- Table 5 超参数完整，reproducibility 合格
- Appendix B taxonomy 百分比完整（合计 100.1%，四舍五入正常）