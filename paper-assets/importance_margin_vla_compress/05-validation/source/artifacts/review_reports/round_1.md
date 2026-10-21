---
round: 1
overall_score: weak reject
timestamp: 2026-05-18T11:41:55.818098+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告 — Round 1

**论文**: "Why Token Pruning Crashes Some Robot Policies but Not Others: The Role of Vision Connectors in VLA Token Compressibility"
**目标 Venue**: CoRL 2026 (Deadline: 2026-05-29)
**Reviewer 编排**: Reviewer 1（方法严谨性 + 实验设计），Reviewer 2（新颖性 + 完整性 + 格式合规）
**审稿轮次**: Round 1（独立初审 + 交叉分享，1 轮收敛）

---

## Summary

论文首次系统性地在闭环控制中跨架构评估 VLA vision token pruning。核心发现是 SmolVLA（pixel-shuffle connector）在所有 6 种 pruning 配置下从 44.8% SR 崩溃至 0%（cliff-edge），而 OpenVLA（MLP projector）从 74.0% 渐进降至 37.4%（graceful degradation）。论文提出 attention entropy ratio 作为可压缩性诊断指标，并通过 cross-attention re-encoding（Smart Compress）将 SmolVLA SR 从 44.8% 提升至 ~60%。

---

## Strengths

**S1** [共识] Cliff-edge 发现本身有实际价值。6 种 pruning 配置（3 轴：scoring/ratio/mechanism）在 3 个 LIBERO suite 上全部收敛至 0% SR，ablation 设计系统，有效排除了多个替代假设。这对 VLA 推理加速社区有重要警示意义。

**S2** [共识] 统计处理严谨。所有结果报告 Wilson score 95% CI，每个条件 500 episodes，significance test 使用得当。

**S3** [共识] Smart Compress 的 M=128 passthrough control 是 well-designed 的实验设计，有效分离了 re-encoding effect 和 compression effect。

**S4** [共识] 写作质量高。主线逻辑清晰（问题→发现→解释→解决），AI 写作痕迹极少，Limitations section 诚实地面对了主要局限。

**S5** [共识] 研究问题直接面向 CoRL 核心受众，VLA 推理效率是当前热点。

---

## Weaknesses

### Must-Fix（影响接收决定）

**W-MF1** [critical, R1+R2 共识] **Scale confound 严重削弱核心因果 claim**

SmolVLA (0.5B, pixel-shuffle) vs OpenVLA (7B, MLP projector) 同时改变了 connector 类型和模型规模（14× 参数差异）。论文的三条间接论据均有漏洞：
- k=0.9 论据：0.5B 模型 baseline 仅 44.8%（capacity-marginal），对扰动敏感可能与 connector 无关
- Entropy ratio 论据：7B 有 32 层 vs 16 层，更深网络本身更容易发展 selective attention
- Mechanistic 论据：相关性证据而非因果证据

论文标题、abstract、全部四条 contribution 均以 connector-level 因果解释为前提。如果 scale 是主要因素，叙事基础不成立。

**需要**：(1) 弱化因果语言（"determined by" → "associated with"）；(2) 在更多 pixel-shuffle VLA 或同一模型不同 connector 上验证；(3) 在 abstract 中明确提及 scale confound。

**W-MF2** [critical, R1 主导, R2 支持] **SmolVLA baseline 远低于官方值（44.8% vs 87.3%），cliff-edge 普适性存疑**

性能几乎腰斩，模型处于功能边缘状态。在该 operating regime 下观察到的 cliff-edge 可能是 undertrained/underfitting 模型特有的脆弱性，而非 pixel-shuffle connector 的固有属性。论文声称"the relevant comparison is the relative change"，但 well-trained 模型的 attention pattern 和 token dependence structure 可能截然不同。此问题与 W-MF1（scale confound）叠加，进一步削弱 connector-level 归因。

**需要**：(1) 在接近官方 87.3% 的 baseline 上验证 cliff-edge；(2) 至少讨论 undertrained model 的 cliff-edge 可能不代表 well-trained model 的行为。

**W-MF3** [critical, R2 主导, R1 支持] **Smart Compress 的 15pp gain 存在 capacity/training confound**

M=128 passthrough (59.8%) 比 baseline (44.8%) 高 15pp，论文归因于 "cross-attention re-encoding"。但这也可能来自：(a) 额外 22.2M 参数（5% 容量增加），(b) 额外 100K 步 end-to-end 训练，(c) 两者组合。对于一个 capacity-marginal 模型（baseline 44.8%），5% 参数增加 + retraining 本身可能带来显著提升。

**缺失的关键 ablation**：(a) baseline + 100K more training（无 compressor）；(b) 同参数量的 MLP adapter control；(c) 只训练 compressor 冻结 LLM。

**需要**：至少增加 "baseline + 100K more training" 控制实验。

**W-MF4** [critical, R1 主导] **Attention entropy ratio 作为 "compressibility predictor" 仅有 2 个数据点**

从 2 个数据点（SmolVLA=0.98, OpenVLA=0.64）无法建立任何预测关系。这 2 个数据点还受 scale confound 污染（entropy 差异可能来自模型深度而非 connector）。Abstract 和 Introduction 中的表述（"diagnostic"/"predictor"）比 Section 4.2 末尾的 hedging 更为强烈。

**需要**：(1) 降级为 "observation"/"hypothesis"；(2) 在更多架构上测量 entropy ratio（即使只做前向推理）；(3) 在 abstract/contribution 中明确限定。

**W-MF5** [critical, R2 主导] **CogACT 在 Related Work 中被提及两次但缺少 bib 条目**

CogACT 被用作论据支持 "MLP projector VLAs exhibit graded degradation"，但未引用。更重要的是：如果 CogACT 使用 pixel-shuffle 类 connector 但仍能被 EfficientVLA 成功 prune，将直接反驳论文核心论点。

**需要**：补充 CogACT 引用，明确说明其 connector 类型，核实与论文假说的一致性。

### Should-Fix（影响评分但不一票否决）

**W-SF1** [warning, R2] 缺少重要相关工作引用。24 篇对 CoRL 偏少（通常 30-50 篇）。遗漏 Octo（使用类 Perceiver cross-attention tokenizer，与 Smart Compress 直接相关）、Open X-Embodiment、RT-1、HPT。

**W-SF2** [warning, R2] Smart Compress 方法新颖性有限。Cross-attention pooling 与 Q-Former (BLIP-2) 和 Perceiver Resampler (Flamingo) 架构几乎相同。论文需要明确定位 contribution 在 empirical finding 而非 architectural novelty。

**W-SF3** [warning, R1+R2 共识] M=96 outlier (52.6%) 未被合理解释。CI [48.2, 56.9] 与 M=32/64 的 CI [57.3, 65.8] 不重叠，这是统计显著的差异。仅有单 seed 无法区分 training noise 和 systematic effect。"approximately flat" claim 可能不成立。

**W-SF4** [warning, R1] "Cost-free deployment benefit" 措辞 overstated。需 22.2M 参数 + 100K 步训练 + 仅 6% latency gain（164ms → 155ms）。应改为 "performance-neutral compression"。

**W-SF5** [warning, R1] 单 seed (seed=42) 实验设计削弱统计 claim。CoRL 仿真实验通常要求至少 3 个 seed。

**W-SF6** [warning, R1] Offline metric disconnect (Contribution 4) 缺少具体数据。111.5% relative action error 仅文字提及，无 table/figure 支撑。作为正式 contribution 需要数据展示。

**W-SF7** [warning, R1] Cliff-edge 在 k=0.95/0.99 未被测试。k=0.9 移除 13 tokens = 10% 视觉覆盖，更极端保留率的实验将显著增强说服力。

**W-SF8** [warning, R2] "First systematic closed-loop evaluation" claim 过于宽泛。VLA-IAP 已有 closed-loop SR 报告。应限定为 "first cross-architecture evaluation"。

**W-SF9** [warning, R2] 仅 LIBERO 仿真评估，无 real robot 验证。CoRL 偏好 real robot evaluation。

---

## Reviewer Consensus

以下问题两位 Reviewer 达成共识（[AGREE]）：
- Scale confound 是核心问题，严重削弱因果归因 [R1-N1, R2-N1]
- Smart Compress gain 需要更好的 disentangle [R1-W1, R2-N2]
- M=96 outlier 需要解释或多 seed 验证 [R1-W2, R2-W4]
- Low baseline 影响 cliff-edge 的普适性 [R1-N2, R2-W2]
- 论文写作质量高，AI 痕迹极少 [R1 Clarity 3/4, R2 Clarity 4/5]
- Cliff-edge 发现本身有价值，ablation 设计系统 [R1-S1, R2-S1]
- 对 CoRL 高度 relevant [R1 4/4, R2 4/5]

## Reviewer Divergence

以下问题存在 severity 分歧（非内容分歧）：
- **Smart Compress confound severity**：R1 列为 Should-Fix (W1)，R2 列为 Must-Fix (N2)。Director 判定：**升级为 Must-Fix**。理由：对于 capacity-marginal 模型（baseline 44.8%），5% 参数增加 + retraining 的混淆效应不可忽视，缺少控制实验使 Contribution 3 的归因不可靠。
- **Baseline 偏低的独立影响**：R1 列为 Must-Fix (N2)，R2 列为 Should-Fix (W2)。Director 判定：**维持 Must-Fix**。理由：与 scale confound 叠加后，cliff-edge 可能是 undertrained + small-scale model 的产物这一替代假说很难排除。
- **Entropy ratio 2-datapoint 问题**：R1 列为 Must-Fix (N3)，R2 在 Originality 中提及但未单独升级。Director 判定：**维持 Must-Fix**。理由：作为 Contribution 2 列出的 "predictor"/"diagnostic" 仅基于 2 个受 confound 污染的数据点，overclaiming 明确。

---

## Questions（需要作者澄清）

**Q1**: 是否可能在接近官方 87.3% baseline 下验证 cliff-edge？即使只测试 k=0.9 一个点。

**Q2**: 是否尝试过 baseline + 100K more training（不加 compressor）作为 Smart Compress 的 control？

**Q3**: M=96 的 52.6% 是否在不同 seed 下复现？

**Q4**: 111.5% relative action error 的具体测量条件？为什么没有以 table/figure 展示？

**Q5**: 是否考虑过测试 k=0.95 或 k=0.98？

**Q6**: CogACT 的 vision connector 类型是什么？EfficientVLA 在 CogACT 上的 pruning 行为是否与论文假说一致？

---

## Missing References

- **Octo** (Ghosh et al., 2024): 使用类 Perceiver cross-attention tokenizer，与 Smart Compress 直接相关
- **Open X-Embodiment** (RT-X, 2024): VLA 训练的重要数据源
- **RT-1** (Brohan et al., 2023): VLA 重要前驱工作
- **CogACT** (Li et al., 2024): 正文中被提及但无引用
- **HPT** (Wang et al., 2024): 另一种 VLA 架构
- 另有 7 条 bib 条目的 first author 与实际不匹配（zitkovich2023rt2, hsu2025vlacache, wang2026vlaiap, liu2023libero, yang2025efficientvla, liu2025vlapruner, yang2024qwen2）

---

## External Review (Stanford Agentic Reviewer)

**状态：pending（未返回）**。已于 2026-05-18T11:31 UTC 发送请求，8 小时后自动提醒。内部审稿不阻塞。

---

## Format Issues

- **[Must-Fix]** figures/ 目录为空，5 张图无法编译
- **[Must-Fix]** 无行号（review 版需要）
- **[Should-Fix]** corl_2026.cls 是 12 行 placeholder，非官方模板（可能导致 desk reject）
- **[Minor]** `\textendash` 使用不规范，应统一用 `--`
- **[Minor]** 7 条 bib 条目 author mismatch

---

## Overall Assessment

**评分：Weak Reject**
**置信度：High（两位 Reviewer 在核心问题上达成共识）**

论文的核心发现（cliff-edge phenomenon）有实际价值，ablation 设计系统，写作清晰。但存在 5 个 Must-Fix 问题：

1. **Scale confound 未解决**：0.5B vs 7B 的对比无法区分 connector 与 capacity 的影响，核心因果 claim 的证据链不完整
2. **Baseline 远低于官方值**：44.8% vs 87.3%，cliff-edge 可能是 undertrained model 的产物
3. **Smart Compress gain confound**：15pp 提升可能来自额外参数/训练而非 re-encoding 机制，缺少控制实验
4. **Entropy ratio overclaiming**：2 个受 confound 污染的数据点被包装为 "predictor"/"diagnostic"
5. **CogACT 引用缺失**：可能影响核心论点的一致性

这些问题的共同根源是：论文的实证发现（cliff-edge、graded degradation、Smart Compress 有效）是可靠的，但从实证到因果归因（connector determines compressibility）的推理跳跃不够严谨，缺少关键控制实验。

如果作者能在 revision 中：(a) 在更强 baseline 上验证 cliff-edge，(b) 增加 "baseline + more training" 控制实验，(c) 弱化因果语言，(d) 降级 entropy ratio 为 observation——论文有潜力升级为 borderline accept。

---

## Detailed Comments（逐节意见）

**Abstract**: 数字密度偏高（9 个数字），更像 Results 摘要而非故事。建议减少到 4-5 个关键数字。

**Introduction**: 叙事线完整，但 Contribution 4 (offline metric disconnect) 前文铺垫不足。建议在第三段（existing evaluations）中更充分地铺垫 offline vs closed-loop 的区别。

**Related Work**: (1) CogACT 缺引用；(2) "To our knowledge" claim 应移到 Introduction；(3) 需补充 Octo、RT-1、Open X-Embodiment。

**Background**: 清晰完整，SmolVLA 和 OpenVLA 的架构对比有效。

**Experimental Setup**: 设计严谨；但 Smart Compress jointly optimize compressor + LLM backbone 缺少对应的 ablation（冻结 LLM 的 control）。

**Results**: Table 1 中 ACIS k=0.5 只有 300 episodes（vs 其他 500），原因未说明。OpenVLA 和 SmolVLA 的 k 值集合不完全对齐（k=0.3 仅 OpenVLA 有）。

**Analysis**: Section 4.2 entropy 测量中 OpenVLA 仅 250 frames（vs SmolVLA 2400），应讨论可靠性。Section 4.3 重复了 Results 中已说明的 Smart Compress 结果。

**Discussion**: Section 5.1 诚实面对 scale confound，但 Section 5.4 (Design Implications) 给出了基于 connector 的 design recommendation，与 5.1 承认的 confound 存在逻辑矛盾。Section 5.2 offline metric disconnect 缺少具体数据。Section 5.3 cost-benefit analysis 措辞 overstated。

**Conclusion**: 沿用了 Abstract/Intro 的因果语言，应在 revision 中一并弱化。

**Appendix**: Table 7 caption 说 "per-task differences up to 48 percentage points"，但表中数据最大差异约 30pp（需核实是否包含未展示的 M=16/M=96 数据）。

---

*审稿报告由 Review Director 基于 Reviewer 1（方法严谨性 + 实验设计）和 Reviewer 2（新颖性 + 完整性 + 格式合规）的独立审稿及交叉回应汇总生成。*