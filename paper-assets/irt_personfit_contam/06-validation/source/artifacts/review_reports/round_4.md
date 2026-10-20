---
round: 4
review_mode: fresh
overall_score: 3.0
timestamp: 2026-05-22T07:59:06.483542+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告：What Can Binary Response Patterns Reveal About Benchmark Contamination? An IRT Person-Fit Characterization

**Venue**: EMNLP 2026 via ACL Rolling Review (Long Paper)
**Reviewers**: R1（方法严谨性, 3.5 Borderline Conference）、R2（新颖性/完整性, 3.0 Findings）
**Overall Assessment**: **3.0 (Findings)**
**Confidence**: 4/5

---

## Summary

本文首次将心理测量学中的 IRT person-fit 统计量（ℓ_z*）系统性应用于 LLM 基准污染检测。核心思路：被污染的 LLM 类似于拥有题目预知的考生，会在难题上产生异常正确的作答模式。作者提出 Δℓ_z*（差分设计）消除 IRT 模型误设的影响，在 3 个 7-8B 模型族（Qwen2.5-7B、Llama-3.1-8B、Mistral-7B；n=10 clean seeds，Mistral n=6）× 2 个基准（MMLU 14,042 items、ARC-C 295 items）× 3-4 个污染水平（15%/25%/50%）上进行了控制实验（每个污染条件单次 QLoRA 运行）。报告三个行为边界：(1) 模型特异的 θ-shift absorption；(2) detection-diagnosis tradeoff；(3) 能力依赖的非单调剂量-效应。附带 N=1 的 post-RL preliminary observation。

---

## Strengths

1. **新颖的跨学科桥接**：首次将教育测量学 person-fit 理论系统性引入 NLP 污染检测。"污染 LLM ≈ 作弊考生" 的类比自然且有启发性，开辟了 psychometrics × NLP 的新方向。[R1 AGREE, R2 AGREE]

2. **Δℓ_z* 差分设计的优雅性**：绝对 ℓ_z* 在 LLM 上完全失效（57/60 cells flagged as aberrant），差分设计通过消除共享模型误设巧妙解决了这一核心障碍。Appendix F 的 local dependence 模拟进一步验证了该设计在现实依赖结构下的鲁棒性（d_ratio ≥ 0.93 for σ_τ ≤ 0.5）。[R1 AGREE, R2 AGREE]

3. **θ-shift absorption 机制分析**：对 "为什么高能力模型检测信号更弱" 的机制解释清晰有说服力。Table 2 的 free-θ vs fixed-θ 对比（Qwen 50%: 7.6× amplification）提供了强支撑。ARC-C 的 ceiling effect 反转（高基线反而增强信号）是非教科书式的经验发现。[R1 AGREE, R2 partial AGREE]

4. **诚实定位**：论文明确定位为 "characterization"（行为边界刻画）而非 "tool"（现成工具），坦承简单统计量在纯检测任务上表现更优（Table 3: accuracy z-score |d|=68.7 vs ℓ_z* |d|=1.90）。这种学术诚实在该领域少见。[R1 AGREE, R2 AGREE]

5. **详尽的鲁棒性分析**：8 个 Appendix 涵盖 simulation validation、4PL vs 3PL ablation、seed sensitivity、cross-family consistency、item-level AUROC、local dependence robustness、parameter perturbation、BCa comparison、MML-EM refit。方法论严谨态度明显。[R1 AGREE, R2 AGREE]

6. **Appendix H 的 MML-EM 对比**：证明 classical MML-EM 估计无法替代 PSN-IRT（r_a=0.127），为 "为什么需要外部 item bank" 提供了定量支撑，是重要的方法论贡献。[R2 特别肯定]

---

## Weaknesses

### Must-Fix（影响接收决定）

**[W-MF1] 每个污染条件仅单次运行，Cohen's d 统计解释受限** [R1-N1, R2 AGREE]

论文的 Cohen's d 本质上是单一污染观测值相对于 clean 分布的 one-sample z-score，而非两组分布间的标准化均差。每个污染水平（15%/25%/50%）仅训练了 1 个 QLoRA 模型，所有方差估计均来自 clean seeds。QLoRA 微调具有随机性（初始化、数据顺序、gradient noise），不同 seed 可能产生不同的 ℓ_z* 值。当前设计无法：(a) 估计污染效果的方差；(b) 判断观测到的 ℓ_z* shift 是否具有代表性。Table 1 的全部 effect sizes、inverted-U 的具体幅度（Qwen 4.3× peak-to-trough）、cross-model 比较均可能因单一运行的随机性而不稳定。

*两位 Reviewer 一致认为这是最核心的实验设计缺陷。*

**[W-MF2] 缺少与现有污染检测方法的实证对比** [R2-N2, R1 AGREE]

Table 3 仅在自身框架内对比了 ℓ_z*、HT、accuracy z-score，完全没有与已有的专用污染检测方法（ConStat、MIA-based methods）进行头对头比较。作者拥有完整 model access（QLoRA 训练），可运行 Min-K% Prob 等 MIA 方法。Discussion 中 "different information requirements" 的辩护不充分——不同信息需求恰恰是应该对比的原因，读者需要知道 "只用 binary patterns + item bank" 相比 "用 logits" 损失了多少检测能力。R1 补充：论文定位为 "characterization, not tool"，但如果不与外部方法对比，characterization 的实际价值难以评估。

**[W-MF3] 实验矩阵事后扩展构成假设确认风险** [R1-N3, R2 AGREE with severity nuance]

§3.3 明确承认："Following initial observation of non-monotonic dose-response for Qwen, we added a 25% contamination condition." 这是 hypothesis-confirming data collection。Inverted-U 是论文三大核心贡献之一，但确认该发现的数据点（25%）是在看到初始结果后才添加的。虽然后续扩展到 Llama 提供了部分独立复制，但 Mistral 未测 25%。论文的透明披露是加分项，但 inverted-U 的 claim 强度与证据的独立性不匹配。R2 认为可降级为 "observation requiring prospective confirmation"。

### Should-Fix（影响评分但不一票否决）

**[W-SF1] Title/framing scope mismatch** [R2-N3, R1 AGREE but downgrade]

标题 "Binary Response Patterns" 掩盖了对 PSN-IRT 外部 item bank 的核心依赖（Appendix H 证明不用 PSN-IRT 时 r_a=0.127）。"Benchmark Contamination" 远宽于 SFT-stage QLoRA 实验范围。Abstract 提到 PSN-IRT 依赖但嵌在长句中不够突出。R1 认为这在 NLP 论文中常见，改标题加 "SFT-Stage" 限定 + Abstract 突出 item bank 依赖即可。

**[W-SF2] Post-RL 观察（N=1）占据过大篇幅** [R1-W4, R2-W2, 双方 AGREE]

N=1（Qwen only, GRPO, 15% MMLU）的 post-RL 观察获得了 Discussion 完整段落 + Figure 4（~0.5页），且在 Abstract 中被提及。在 8 页空间限制下，这一比重过高。两位 Reviewer 一致建议移至 Appendix。

**[W-SF3] 无低污染水平（<15%）的实证实验** [R1-W1, R2 AGREE]

经验实验最低污染水平为 15%，模拟（Appendix A）显示 5% 时 MMLU power 仅 47.6%。实际场景中低污染更常见，当前最低测试阈值过高。

**[W-SF4] ARC-C 仅限 Qwen，跨基准泛化证据不足** [R1-W2, R2 AGREE]

ARC-C（295 items）仅在 Qwen 上测试。"across three model families" claim 的跨基准支撑仅来自 MMLU。

**[W-SF5] Fixed-θ 反直觉现象缺乏解释 + 无实用决策指导** [R1-W3 + R2-W4, 双方 AGREE]

Table 2 显示 Qwen 15% 时 fixed-θ 反而比 free-θ 更差（ratio=0.7×），与 "fixed-θ recovers signal" 的核心叙事矛盾。§4.2 末段给出定性指导但缺少操作化定义和 decision rule。

**[W-SF6] 实验规模/多样性不足** [R2-W1, R1 AGREE]

全部 7-8B 规模，无 1-3B/13B+/MoE 架构。仅 QLoRA SFT，无 full fine-tuning/continued pretraining。Generalization claims 超出实验覆盖。

**[W-SF7] QLoRA 训练细节不足** [R1-W5, R2 partial AGREE]

§3.3 仅报告 rank=16, α=32，缺 LR、epoch、batch size、数据混合方式等关键超参数。建议在 Appendix 补充完整 hyperparameter table。

**[W-SF8] Mistral n=6 的 bootstrap CI 可靠性** [R1-W6, R2 AGREE]

n=6 的 bootstrap CI 在统计理论上可靠性有限。BCa（Appendix G）提供了 sensitivity check，但自身在 n=6 也未必可靠。

---

## Reviewer Consensus [AGREE]

两位 Reviewer 在以下关键问题上达成完全共识：

1. **单次污染运行是最核心的实验设计缺陷**（W-MF1）——需要至少为关键条件补充多 seed 污染实验
2. **缺少与外部方法的实证对比削弱了论文的价值定位**（W-MF2）——至少应与 1-2 种代表性方法做 baseline 比较
3. **Post-RL N=1 应精简**（W-SF2）——移至 Appendix
4. **Framing 应收窄以匹配实验范围**（W-SF1）——标题加 SFT-stage，Abstract 突出 PSN-IRT 依赖
5. **实验矩阵的事后扩展降低了 inverted-U 的证据强度**（W-MF3）——应降级 claim 或补充独立验证

---

## Reviewer Divergence [REBUT]

**[R5-D1] Novelty 评估**

- **R2 立场（3.0 Findings）**：三个核心 findings 大部分可从 IRT 理论直接预测——θ-shift ceiling effect 是 well-known 的 IRT 性质，detection-diagnosis tradeoff 是 power vs. richness 的经典权衡，inverted-U 是 Finding 1 的直接推论。经验贡献主要在定量校准层面（"useful calibration, not new insight"）。

- **R1 立场（3.5 Borderline Conference）**：承认理论方向可预测，但强调：(a) 定量结果和边界条件是新的——ARC-C ceiling effect 反转非教科书推论，57/60 vs 4/60 flagged cells 是新经验发现；(b) LLM 严重违反 IRT 假设，理论预测是否在 LLM 上成立需要经验回答；(c) "useful calibration" 对 characterization paper 可构成充分贡献，**前提是实验设计足够严格**（R1-N1/N3 的缺陷削弱了这一前提）。

- **Director 判断**：分歧未解决，但两位 Reviewer 均同意当前实验设计不够严格，这使得 calibration 的可信度本身也受损。实验设计缺陷的修复（多 seed 运行、外部方法对比）可能间接缓解 novelty 争议——如果 calibration 数据更可靠，其独立贡献更容易被接受。

---

## Questions to Authors

1. 如果为 Qwen 15%/50% 各训练 3-5 个不同 seed 的污染模型，预期 ℓ_z* 的 seed-level 方差有多大？是否有任何 pilot 数据估计污染效果的可重复性？

2. ConStat 需要 reference benchmark 分数——你们已有 ARC-C 和 MMLU 两个 benchmark，这似乎满足了 ConStat 的最低信息需求。为什么选择不做对比？

3. Table 2 中 Qwen 15% 的 fixed-θ 比 free-θ 更差（ratio=0.7×），能否提供定量解释？Snijders correction 在此处的具体影响是什么？

4. PSN-IRT 校准样本（13,000+ 模型）中，估计有多大比例可能存在基准污染？Appendix F.2 的 ±10% 随机噪声能否模拟系统性污染偏差？

5. 是否考虑过在 held-out 模型族（如 Phi-3、Gemma）上前瞻性验证 inverted-U？

---

## Missing References

- **污染检测 survey**：虽然论文已引用 Chang et al. (2024) survey，但 R2 建议补充更近期的专题 survey（如 Dong et al. 2024 "Does Data Contamination Detection Work (Well) for LLMs?"，对检测方法假设做了系统评估，与本文的 characterization 目标直接相关）。R1 认为当前覆盖已属充分。Director 倾向于：至少补充 Dong et al. (2024)，因其对检测假设的评估与本文高度互补。

- **IRT person-fit 功效分析**：Sinharay & Johnson (2017) 等 person-fit 功效分析文献可为 benchmark size boundary 提供理论支撑。

---

## External Review (Stanford Agentic Reviewer)

未请求。

---

## Visual Layout Check（非评分项）

视觉审查已完成（8 项 info 级发现，无 critical/warning）：

- **Page 1**：首页纯文本无视觉锚点，Figure 1 在第 2 页（前 3 页阈值内可接受，但若能提升至第 1 页底部可增强第一印象）
- **Pages 3-4**：连续 2 页无 display item（Method 段），仅有公式。建议添加 pipeline/framework 概念图
- **Page 6**：Figure 2 heatmap cell 内数字字号偏小（~6-7pt），打印时可能难以辨认
- **Page 6**：Figure 2 单色蓝梯度，色盲安全 ✓
- **Page 7**：Figure 3 marker shape 可进一步区分以增强灰度打印可读性
- **Page 5**：Table 1 未对最大 Cohen's d 加粗，可提升 scannability
- **Page 8**：Figure 4 双轴设计增加认知负担，caption 解释充分
- **Page 14**：末页内容约 60-65%，作为附录末页可接受

---

## Overall Assessment

**评分：3.0 (Findings)**

本文在 NLP-psychometrics 交叉领域做出了有意义的探索。Δℓ_z* 差分设计优雅地解决了绝对 person-fit 阈值在 LLM 上失效的核心问题，θ-shift absorption 的机制分析有洞察力，detection-diagnosis tradeoff 对实践有指导意义。8 个 Appendix 展现了扎实的方法论功底，论文定位诚实。

然而，三个 Must-Fix 问题制约了评分：

1. **每个污染条件仅单次运行**——这是实验设计层面的根本缺陷，使得所有定量结论（effect sizes、inverted-U 幅度、cross-model 比较）的统计基础不牢靠。多 seed 污染实验是修复路径。

2. **缺少与现有方法的实证对比**——一篇声称 characterize contamination detection 的论文，不与任何专用检测方法做头对头比较，使读者无法评估 IRT person-fit 的实际价值。至少应与 ConStat 和一种 MIA 方法做 baseline 对比。

3. **实验矩阵事后扩展**——inverted-U 的确认性证据源于事后添加的 25% 条件，且仅在部分模型上验证。论文的透明度是加分项，但 claim 强度需与证据独立性匹配。

Novelty 存在分歧（R1: 3.5, R2: 3.0）。R1 认为经验校准对 characterization paper 有独立价值，R2 认为 findings 大部分可从 IRT 理论预测。Director 认为：当实验设计本身不够严格时，calibration 数据的可信度也受损，novelty 争议因此难以在当前版本中解决。

**修复路径**：(1) 为关键条件补充 3-5 个 contaminated seeds；(2) 与 ConStat + 1 种 MIA 方法做 baseline 对比；(3) 将 inverted-U 降级为 exploratory observation。如果上述修改完成，论文有望达到 3.5（Borderline Conference），结合 framing 调整和 post-RL 精简可能达到 4.0（Conference）。当前版本推荐 Findings。

---

## Detailed Comments

### Abstract (p.1)
- Abstract 对实验设计的描述实际上是透明的（明确区分 "clean seeds" 和 "single QLoRA run"），这是方法论诚实的体现
- 但 "only binary response patterns" 的 minimal-information framing 需突出对 PSN-IRT 4PL item bank 的核心依赖
- Post-RL preliminary observation 可从 enumerated findings 中移除

### Introduction (pp.1-2)
- Figure 1 的 "clean vs contaminated" 类比有效且直观
- "Rather than proposing ℓ_z* as a ready-to-deploy detection tool" 的诚实定位值得肯定
- SFT-stage 限定（"we focus on SFT-stage contamination"）存在但不够突出

### Related Work (pp.2-3)
- 五类方法的覆盖系统全面
- Person-fit 文献覆盖充分（Karabatsos 2003、Embretson & Reise 2000、Sinharay 2017）
- 建议补充 Dong et al. (2024) 对检测方法假设的系统评估

### Method (pp.3-4)
- Δℓ_z* DiD 设计（Eq. 2）是论文最核心的方法论贡献
- §3.2 "DiD" 命名不够精确——标准 DiD 需时间维度，建议改为 "matched-difference design"
- §3.3 对 25% 条件事后添加的透明披露是加分项，但应进一步讨论对统计推断的影响
- 缺少完整的 QLoRA hyperparameter table

### Results (pp.5-7)
- Table 1 的 effect sizes 全部 CI 排除零，基本检测 claim 有支撑
- §4.2 θ-shift absorption 分析清晰，Table 2 的 free/fixed 对比有说服力
- §4.3 detection-diagnosis tradeoff（Table 3）的 57/60 vs 4/60 对比是强经验发现
- §4.4 inverted-U 的证据受事后扩展和单次运行限制

### Discussion (pp.7-8)
- "Characterization over tool" 段落定位准确
- ConStat 对比仅用一句 "complicated by different information requirements" 带过，不充分
- Post-RL 段落 + Figure 4 的空间分配需重新考虑

### Limitations (p.9)
- 简洁且涵盖主要限制，符合 EMNLP 要求
- 应补充对 "单次污染运行" 和 "无 <15% 低污染实验" 的显式讨论
- LD 模拟假设局限性（testlet+Gaussian 可能不代表 LLM 依赖结构）已包含，是加分项

### Appendix (pp.10-14)
- 8 个 Appendix 构成完整的鲁棒性分析体系
- Appendix H（MML-EM 对比）是重要方法论贡献，建议在主文 §3.1 简短提及
- Appendix G（BCa 对比）确认 percentile CI 保守，增强了主文结论的可信度