---
round: 6
review_mode: fresh
overall_score: weak reject
timestamp: 2026-05-23T06:01:04.550275+00:00
reviewer_ids: [1, 2, 3]
cross_response_reviewer_ids: [1, 2, 3]
force_resubmit: False
---


# Round 6 审稿报告：Why Token Pruning Crashes Some Robot Policies but Not Others

**Venue**: CoRL 2026 | **Deadline**: 2026-05-29 | **审稿模式**: Fresh (重新审稿)

---

## Summary

论文研究 vision token pruning 在不同 VLA 架构上的表现差异，提出 connector architecture 是 pruning robustness 的主要关联因素。核心发现：(1) pixel-shuffle connector (SmolVLA) 在仅移除 5% token 即崩溃至 0% SR，经双 checkpoint 验证；(2) token-entangling connectors 展现 task-complexity amplified collapse（X-VLA 在 Object 仅损失 1.4pp 但 Goal 损失 27.8pp）；(3) CV of L2 norms 作为 diagnostic 与 pruning tolerance 相关；(4) VTR (cross-attention re-encoding) 在 SmolVLA 上从 0% 恢复至 ~60% SR。实验覆盖 6 个 VLA 架构（450M-7B），4 个 LIBERO task suite，2 种 pruning 策略。

---

## Strengths

**S1** [3/3 共识] **Pixel-shuffle 崩溃机制发现扎实且有价值。** SmolVLA 在 k=0.95（仅移除 6/128 tokens）即从 59.2% 崩溃至 0.0% SR，经 LoRA fine-tuned 和官方 checkpoint 双重验证，7 种 pruning 配置（ACIS/random/L2 × zero-mask/true removal/ToMe）均为 0%。这是从 pixel-shuffle 架构定义可演绎推导但首次被系统实证的结果，对 practitioners 有直接预警价值。(Section 4.3, Table 3/Appendix D)

**S2** [3/3 共识] **实验设计系统性在 VLA pruning 文献中范围最广。** 6 个架构 × 3 种 connector family × 2 种 pruning 策略 × 6 个 retention ratio，附录详尽（27 页，含 per-task breakdown、multi-seed validation、hypergeometric model、attention entropy analysis）。Wilson 95% CI + 500 episodes/condition 是合理的统计实践。

**S3** [3/3 共识] **写作清晰，结构合理。** Figure 1 teaser 有效传达 two-axis framework，Table 1 model properties 设计精简，Introduction 的 problem→gap→approach→contributions 流程逻辑严密。

**S4** [2/3 共识] **Limitations 态度诚实。** 论文承认 simulation-only、causal isolation 不可能、CV data points 有限等核心局限（虽然主文过短，扩展讨论在 Appendix A）。

**S5** **VTR 从 0% 恢复至 ~60% SR 是有价值的 proof-of-concept。** 在所有 hard pruning 方法均失败的条件下，22M 参数的 re-encoding 模块在 75% 压缩下恢复功能性能。MLP adapter 达到 comparable 性能 (p=0.15) 的发现本身也有价值——说明 re-encoding 而非特定架构是关键。

---

## Weaknesses (Must-Fix)

**W-MF1** [3/3 全员共识] **CV diagnostic 证据严重不足——N=3-4 闭环模型无法建立可靠诊断工具。**
- 论文声称 CV "enables connector-appropriate compression strategy selection without downstream evaluation" (Introduction C2, Section 3.3)
- 实际闭环验证仅 4 个模型；method sensitivity 有效数据点仅 3 个（SmolVLA 全 0% 无法参与 method gap 比较）
- Spearman rank correlation N=4 时最小可能 p≈0.083，**原则上无法达到 0.05 显著性**
- 论文未报告任何正式相关性检验
- **R1 量化**：4 个单调排列概率 ≤ 1/24 ≈ 4.2%，统计边缘
- **严重性**：C2 是论文核心 contribution 之一，evidence base 不足直接削弱论文价值

**W-MF2** [3/3 全员共识] **Table 2（核心结果表）数据大量缺失，削弱 cross-architecture, cross-suite analysis 的 claim。**
- π₀.5 Goal: k=0.9 Random 和 k=0.7 L2 缺失
- X-VLA Long: k=0.9/0.7/0.5 大部分缺失
- X-VLA Spatial/Goal: 部分缺失
- **OpenVLA 仅评估 Object 一个 suite**——论文中唯一的 high-CV independent-connector 模型在 task-complexity axis 上完全无验证
- Abstract 声称 "Evaluation spans six VLA architectures... and four LIBERO task suites"，与实际数据矩阵填充率不足 70% 形成叙事落差
- **严重性分歧**：R2/R3 列为 Must-Fix，R1 列为 Should-Fix（认为 SmolVLA 0% 是 finding 不是缺失）。Review Director 裁定 Must-Fix——对 empirical study 而言数据完整性是底线

**W-MF3** [2/3 共识 + 1/3 间接支持] **因果叙事超出证据范围——"primary determinant" 在无 matched-backbone 控制下不可支撑。**
- Conclusion: "connector coupling is the primary determinant of pruning robustness"
- 6 个模型同时在 backbone (Qwen2/PaliGemma/Llama-2)、参数量 (450M-7B, 16×)、vision encoder (SigLIP variants/DINOv2)、token 数量 (50-768, 15×) 上不同
- Appendix N 承认 "preventing clean isolation of the connector effect from backbone differences"
- **Conclusion 与 Limitations 直接矛盾**（R3 叙事一致性检查确认）
- Title "Vision Connectors and VLA Token Compressibility" 隐含因果方向

**W-MF4** [2/3 共识] **缺少 attention-based pruning baseline——论文引用但不测试的标准方法。**
- Attention-based scoring 是 VLA/VLM token pruning 最自然的竞争方法（FastV、VLA-Cache 采用）
- Related Work 引用了 FastV 和 VLA-Cache，但实验不使用 attention-based scoring——叙事缺口
- 如果 attention-based 在 entangling connectors 上也失败，会大幅加强论文核心 narrative
- L2 norm 在 OpenVLA 上与 random 差距 <3pp (Appendix E.10)，说明 L2 并非总是有效的 importance score
- Gradient-based importance 也完全缺失

**W-MF5** [2/3 共识] **Generative AI 使用披露完全缺失——CoRL 2026 合规硬要求。**
- CoRL 2026 Author Instructions 明确要求披露 AI 工具使用
- 论文全文无任何相关声明
- 可能触发 desk rejection 或 AC 质疑

**W-MF6** [3/3 全员共识] **VTR 与 Smart Compress 命名不一致——核心贡献术语混乱。**
- 主文 Section 3.4/4.5 使用 "Vision Token Re-encoder (VTR)"
- Appendix E/F/G/H 大量使用 "Smart Compress"/"Smart Compressor"
- 两个名字无任何词汇重叠，读者无法确定是否为同一组件
- 损害核心贡献（C3）的可信度和可理解性

---

## Weaknesses (Should-Fix)

**W-SF1** [3/3 全员共识] **VTR 贡献被 MLP adapter 控制实验严重削弱。**
- MLP adapter 63.4±2.6% vs VTR 60.1±1.3% (p=0.15)，MLP 点估计更高
- Introduction C3 以 VTR 为主角，但证据表明 cross-attention 非关键——任何 learned re-encoding 都能恢复 pixel-shuffle collapse
- VTR ≈ Q-Former/BLIP-2 applied to VLA token compression，architecture novelty 有限
- 建议：将 C3 reframe 为 "learned re-encoding recovers pixel-shuffle VLAs"

**W-SF2** [3/3 全员共识] **LaTeX 渲染错误 `$\pi_0.5$` 全文 50+ 处。**
- 正确写法 `$\pi_{0.5}$`，当前仅 "0" 下标，".5" 以正文字体显示
- 反映稿件准备粗糙度

**W-SF3** [2/3 共识] **Limitations section 过于简短——3 句话（~60 词），格式为 \\paragraph。**
- CoRL 要求 "describe limiting assumptions, failure modes, and other limitations"
- 遗漏关键局限：单一 benchmark (LIBERO only)、N=3 CV evidence base、pruning 方法范围有限（仅 L2+random）、VTR 单模型验证、主实验多为单 seed
- Appendix A 有 extended discussion 但 reviewer 不要求读附录

**W-SF4** [2/3 共识] **仅 LIBERO simulation 评估，无 real-robot 验证或 sim-to-real 讨论。**
- CoRL CFP: "prioritize real-robot experiments or provide convincing evidence that simulation experiments are transferable to real robots"
- Compressor-VLA (concurrent work) 已含 real-robot 验证
- Conclusion 仅将 real-robot 列为 future work，无 transferability 论证

**W-SF5** [2/3 共识] **Post-connector pruning 选择缺乏系统 justification。**
- 未讨论 pre-connector pruning 可能性
- Concurrent work (VLA-Cache, EfficientVLA) 在 KV-cache 或 pre-connector 操作
- Pre-connector pruning 对 pixel-shuffle 可能不 catastrophic，论文核心发现可能限于 post-connector 这一特定设定

**W-SF6** [2/3 共识] **跨条件使用不同 seed，Table 2 未标注。**
- OpenVLA L2=seed42, random=seed7
- Same-seed 控制仅在 Appendix 提供
- Table 2 caption 无 seed 信息

**W-SF7** [2/3 共识] **论文 identity 分裂——empirical study / diagnostic tool / method 三者各自不够深入。**
- C1 empirical study 数据缺失 (Table 2)
- C2 diagnostic tool N=3 不可靠
- C3 method 被 MLP adapter 平替
- "三个 shallow contribution 拼凑" 结构削弱整体力量

**W-SF8** **No code/data release plan.** 对 empirical 论文的 reproducibility 有影响。建议添加 "Code and data will be released upon acceptance" 声明。

---

## Reviewer Consensus

以下问题经交叉分享后达成共识：

| 问题 | R1 | R2 | R3 | 共识 |
|------|-----|-----|-----|------|
| CV diagnostic N=3-4 不足 | Must-Fix (N1) | Must-Fix (N1) | AGREE | ★★★ |
| Table 2 数据缺失 | Should-Fix (W4) | Must-Fix (N3) | Must-Fix (N3) | ★★★ |
| VTR 被 MLP adapter 削弱 | Should-Fix (W1) | Should-Fix (W1) | AGREE | ★★★ |
| VTR/Smart Compress 命名 | AGREE | AGREE | Must-Fix (N2) | ★★★ |
| π₀.₅ LaTeX 错误 | AGREE | Minor (M4) | Should-Fix (W1) | ★★★ |
| 因果叙事过强 | Must-Fix (N2) | indirect | AGREE | ★★☆ |
| Simulation-only | — | Should-Fix (W4) | AGREE | ★★☆ |
| Attention-based baseline 缺失 | Must-Fix (N3) | AGREE | nuance | ★★☆ |
| Limitations 过短 | implied | AGREE | Should-Fix (W2) | ★★☆ |
| AI disclosure 缺失 | AGREE | AGREE | Must-Fix (N1) | ★★☆ |

## Reviewer Divergence

| 分歧点 | 立场 | 裁定 |
|--------|------|------|
| Table 2 严重性 | R1: Should-Fix (SmolVLA 0% 是 finding); R2/R3: Must-Fix | **Must-Fix**——empirical study 数据完整性是底线 |
| "Don't Run with Scissors" 差异化 | R1: REBUT (不同 domain); R2: Should-Fix | 记录为 info——建议加 1-2 句对比但非关键 |
| Abstract 信息密度 | R3: Should-Fix (17 个数字); R2: partial REBUT (数字是卖点) | 折中——保留 4-5 个关键数字 |
| Figure 3 可读性 | R3: Should-Fix; R1: REBUT (尚可) | 记录为 info |
| VTR 训练 batch size | R1: Should-Fix (不公平); R2: partial REBUT (比较对象是 0% 不是 baseline) | Should-Fix——VTR 内部消融公平，但与 baseline 比较需 caveat |
| CV vs 替代 metric | R1: Should-Fix (未比较); R2: REBUT (N=3 比较无意义) | 取决于是否增加模型数量 |

---

## Questions

1. **[R1-Q1, R2-Q1]** π₀.5 在 k=0.9 Random 下 Object SR 仅 12.0%，但 k=0.7 反弹至 77.2%。这是否为单 seed 随机波动？multi-seed 复现了吗？
2. **[R2-Q2, 3/3 共识]** MLP adapter 达到 63.4% vs VTR 60.1% (p=0.15)。作者如何看待这一结果？C3 的 value proposition 是什么？
3. **[R2-Q3]** CV diagnostic 的 practical workflow 是什么？decision threshold 如何确定？3 个数据点如何建立可操作的指导？
4. **[R2-Q4]** 是否在 SmolVLA 上比较过 GLUESTICK (Don't Run with Scissors 的 training-free recovery) 和 VTR？
5. **[R1-Q5]** 同一 LLM backbone 搭配不同 connector，CV-pruning tolerance 关系是否成立？
6. **[R1-Q3]** SmolVLA k=0.99（仅移除 1 token）是否仍崩溃？是否测试了更精细的崩溃阈值？
7. **[R1-Q5b]** Pruning 后保持原始 position ID（不 re-index）结果是否变化？

---

## Missing References

以下引用已被 Reviewer 确认覆盖（16 个指定检查的 concurrent work 全部已引用）。建议补充：
- A Survey on Efficient Vision-Language-Action Models (2025, arXiv:2510.24795)
- ATP-LLaVA (Adaptive Token Pruning for Large Vision Language Models)

---

## External Review

**状态**：未请求（项目未配置外部审稿）

---

## Visual Layout Check（非评分项）

**状态**：已完成（2 warning, 8 info, 0 critical）

**Warnings:**
1. **Page 2**: Figure 1 子面板内 axis label 和 legend 字号偏小（估计 ~6-7pt），接近可读性下限。打印后可能低于 8pt 最低建议。
2. **Pages 23-25**: 附录连续 3 页纯文本无 figure/table/equation，缺乏视觉锚点。

**Info items:**
- Page 6: 正文唯一纯文本整页（四模型逐一结果），建议考虑 inline summary table
- Page 27: 末页内容约 50%，下半部空白
- Page 7: Table 2 格式正确（最优加粗），但无次优下划线或方向标记
- Page 16: Figure 5 axis label 字号偏小
- Page 5: Figure 2 legend 含 CV 值，字号略小
- Pages 12-15: 附录 per-task breakdown 4 页连续表格，caption 清晰自包含
- Page 4: Table 1 booktabs 风格专业
- Page 8: Figure 3 bar chart 简洁有效

---

## Overall Assessment

**评分：Weak Reject (5/10)**
**置信度：4/5（High）**
**Reviewer 评分：R1=5/10, R2=5/10, R3=6/10**

论文发现了一个有价值的现象（pixel-shuffle connector 在 5% pruning 即 catastrophic collapse，经双 checkpoint 验证），实验设计的系统性在 VLA pruning 文献中范围最广，写作清晰。但存在以下结构性问题阻碍接收：

1. **核心 contribution (CV diagnostic) 的统计基础不足**：N=3-4 闭环模型，Spearman N=4 原则上无法达到显著性。论文将 "preliminary observation" 包装为 "diagnostic tool"，claim 强度与 evidence 不匹配。
2. **数据完整性不足**：核心结果表 (Table 2) 约 20% 条目缺失，OpenVLA 仅评估一个 suite，与 "cross-architecture, cross-suite analysis" 的 claim 矛盾。
3. **因果推断超出证据范围**：6 个模型在 connector 外的多个维度同时不同，无 matched-backbone 控制实验。
4. **Pruning baseline 不完整**：仅用 L2 norm + random，未测试 attention-based scoring。
5. **论文 identity 分裂**：empirical study / diagnostic / method 三者各自不够深入。

**修改路径建议**（Review Director 裁定，非建议作者）：
- **最小修改（deadline 前可行）**：AI disclosure、命名统一、LaTeX 修复、Limitations 扩展、因果语言降级、CV claim 降级、Abstract 精简——这些纯文字修改可在 6 天内完成
- **实质性修改（可能需要更多时间）**：Table 2 补全（需要 GPU 资源和实验时间）、attention-based baseline（需要新实验）、更多 VLA 架构验证 CV diagnostic
- **理想但可能超出 deadline**：real-robot validation、matched-backbone control experiment

---

## Detailed Comments

### Section-by-Section

**Abstract** (abstract.tex): 信息密度过高（17 个数字），建议精简至 4-5 个核心数字。"six VLA architectures" 应明确 "four in closed-loop, two via offline metrics"。

**Introduction** (introduction.tex): 论证逻辑清晰。C2 的 claim "enabling connector-appropriate compression strategy selection without downstream evaluation" 过强，应降级。C3 应 reframe 为 learned re-encoding 而非 VTR 本身。

**Related Work** (related_work.tex): 覆盖范围合理（~46 citations），但对 "Don't Run with Scissors" 的差异化讨论不足（仅在 VLA-specific methods 列表中一笔带过）。建议增加 1-2 句显式对比。VTR 与 Q-Former/BLIP-2 的关系未讨论。

**Method** (method.tex): Section 3.2 pruning protocol 清晰但缺少 post-connector 选择的 justification。Section 3.3 CV 引入缺少与替代 metric (entropy/kurtosis/Gini) 的对比讨论或排除理由。Section 3.4 VTR 描述清晰。

**Experiments** (experiments.tex): Table 2 数据缺失是核心问题。Section 4.2 的 four-model analysis 详尽但纯文本占据整页，建议提炼 inline summary。Section 4.4 CV sensitivity analysis 仅 3 个有效数据点，"correlates" 措辞过强。Section 4.5 VTR recovery 的 MLP adapter 结果应在 Introduction C3 中反映。Limitations 段落需大幅扩展。

**Conclusion** (conclusion.tex): "primary determinant" 需改为 "primary correlate" 或 "strongest observed factor"。Future work 方向合理但缺少 sim-to-real transferability 讨论。

**Appendix** (appendix.tex): 详尽且有价值。命名不一致 (Smart Compress vs VTR) 需全局修复。Pages 23-25 连续纯文本缺乏视觉锚点。Appendix G 脚注中的 batch size 差异信息应提升至主文。
