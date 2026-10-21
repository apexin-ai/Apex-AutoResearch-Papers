---
round: 12
review_mode: fresh
overall_score: 3.0
timestamp: 2026-05-25T21:47:55.704070+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# Round 13 审稿报告

**Venue**: EMNLP 2026 (via ARR) | **模式**: Fresh review | **Reviewer**: R1 (方法严谨性) + R2 (新颖性/完整性) | **交叉回应**: 已完成，已收敛

---

## Summary

本文提出 ContamCal，一个结合多信号污染检测与污染增强 IRT（Item Response Theory）的诊断框架，用于研究 benchmark 污染在不同模型家族间的剂量-响应模式。通过对 5 个开源家族的 6 个模型（7B–14.7B）进行 5 个剂量水平的受控 SFT 注入实验，论文识别出 4 种剂量-响应模式（Immune、Benefit、Collapse、V-Recovery），其中前两种在独立家族间可复现，后两种仅在 Qwen2.5 中观察到。论文还报告了跨 benchmark 传递效应、DiD 无 item 级记忆化结果、以及 volume 控制实验显示 45% 的 Benefit 效应来自数据量而非污染内容。

---

## Strengths

**S1. 重要且及时的研究问题。** 此前研究将污染效应视为均匀膨胀，本文首次在生产级规模（7B–14B）对多个独立模型家族进行受控剂量-响应分析，填补了文献中的实质性空白。

**S2. 跨家族受控实验设计。** 5 个家族（Phi-4、LLaMA-3.1、Gemma-2、OLMo-2、Falcon3）+ Qwen2.5（两个规模），覆盖了不同架构和训练流程，是目前最全面的受控污染实验。

**S3. 多信号暴露映射。** RRF 融合 4 个污染检测信号为连续 per-item 暴露分数，解决了二元污染标签的局限性，工程贡献合理。

**S4. 负面结果的诚实报告。** 论文坦诚报告了 ContamCal MAE 劣于 raw accuracy、DiD 未检测到 item 级记忆化、以及 volume 控制显示 45% 来自数据量。这种透明度值得肯定。

**S5. 广泛的鲁棒性分析。** 附录包含 prior sensitivity、DGP simulation、profile stability、parametric DR 比较、identifiability 分析、KS 检验等，展示了对方法论假设的严谨审视。

**S6. 实际意义。** "并非所有模型都被污染膨胀"的发现对 benchmark leaderboard 解读有直接影响。

---

## Weaknesses

### Must-Fix（6 项）

**W1. Volume confound 控制不足——威胁核心叙事 [R6-W1 + R11-W2, CONSENSUS Critical]**

SFT 注入协议同时引入 (i) 污染内容、(ii) 额外训练数据量、(iii) LoRA 参数更新。Falcon3-7B 的 volume 控制实验揭示 45% 的 Benefit 来自数据量。但此控制仅覆盖 6 个模型中的 1 个。Collapse 模式（Qwen2.5-14B, −25pp at d100）完全没有 volume 控制——来自额外训练的灾难性遗忘是未被反驳的替代解释。这意味着 "dose-response" 的 x 轴不是纯粹的污染内容轴，而是污染 + 数据量 + LoRA 的混合轴，削弱了论文关于模型家族展现不同"污染"响应的核心主张。

**交叉回应共识**：这是本轮两位 Reviewer 最强的共识点。R1 从方法角度（单一家族控制不足）、R2 从概念角度（"Benefit" 归类为污染响应在概念上可能有误）分别指向同一问题，合并后构成论文最需要回应的挑战。

**W2. RRF pipeline 完整性——S2 信号主动有害 [R2-W1, CONSENSUS Critical]**

移除 S2（AUC ≈ 0.48–0.51，接近随机）后，ρ_dose 从 0.049 提升到 0.471（~10× 改善）。尽管有此证据，主分析仍保留 S2。item 级 ρ ≈ 0.773 的辩护不能抵消 model 级的伤害。论文至少应报告去除 S2 后的完整 pipeline 结果，验证下游 γ 估计和剂量-响应 profile 是否被扭曲。

**W3. ContamCal 劣于 raw accuracy baseline [R10-N1, CONSENSUS Critical]**

MMLU MAE = 0.009 vs raw accuracy MAE = 0.006; ARC MAE = 0.020 vs 0.007。名为 "ContamCal"（校准）的框架产出了比 "什么都不做" 更差的校准结果。"价值在于诊断"的辩护本身成问题：如果观察到的剂量产生的效应小到 raw accuracy 已能捕捉群体模式，框架的实际效用存疑。IRT 提供的 credible intervals 和 item 级建模虽是 raw accuracy 不具备的，但 γ 在 J=16 下的不可靠性（W5）削弱了这些增量收益。

**W4. 剂量-响应分类体系证据不足 [R8-N3, CONSENSUS Critical]**

4 个分类来自 5 个家族。Collapse 和 V-Recovery 各仅在 1 个家族（均为 Qwen2.5 不同规模）中观察到——同一家族的不同规模不构成独立复现。更严峻的是，即使在 "已复现" 的模式中，Benefit 的统计基础也很薄弱：AICc 分析显示 Gemma-2 和 OLMo-2 的剂量-响应曲线与常数在统计上不可区分。仅 Immune（Phi-4）在跨 seed 下统计稳健。分类体系必须重构为 2 confirmed + 2 preliminary。

**W5. Domain-level γ 在 J=16 下不可靠 [R4-N1, CONSENSUS Critical]**

γ 后验均值在不同先验下偏移 2.6×（0.34 → 0.89），表明数据（每域 J=16 items）不足以压制先验。论文在 Appendix M 中承认了这一点但未在正文中讨论。Abstract 中 "enables within-family domain-level contamination diagnosis with credible intervals" 的声明在当前证据下不成立。域级分析（Social Sciences 负面、STEM 正面）应被显式标记为先验敏感且探索性的。

**W6. ARC IRT 结果结构性无效 [R3-N3, CONSENSUS Critical]**

ARC 后验预测 p 值（PPP）= 0.003，表明 2PL+γ 模型对 ARC 数据存在严重结构性失配。尽管如此，ARC IRT 结果仍出现在正文 §5.2（跨 benchmark 传递分析）中。使用来自明显不拟合模型的 IRT 估计值具有误导性。正文中的 ARC 结论应完全基于 raw accuracy，IRT 结果移至附录并附适当警告。

### Should-Fix（8 项）

**W7. Abstract/Title 范围超出证据 [R11-N1, CONSENSUS Should-Fix]**

"Not All Models Are Inflated" 和 "Across Model Families" 暗示广泛适用性，但研究仅覆盖 ≤14.7B 的 6 个开源模型在 SFT 下的表现。Abstract 首句 "has never been measured across model families" 过度声明——Schaeffer et al. (2025) 在更小规模进行了受控预训练注入，Bordt et al. (2025) 扩展到 1.6B。如果显式限定为 "SFT-stage injection at 7B–14B scale across five independent open-source families"，claim 可以成立。

**W8. n=3 seeds 统计不充分 [R8-N1, CONSENSUS Should-Fix]**

BCa bootstrap with n=3 seeds 的 resample 空间极小。OLMo-2 的 CI 跨越零。AICc 显示 Gemma-2 和 OLMo-2 与常数不可区分。仅 Immune (Phi-4) 在跨 seed 下统计稳健。跨 seed 稳定性声明应大幅弱化。

**W9. Stage 1→2 不确定性传播缺失 [R12-M2, CONSENSUS Should-Fix]**

RRF 暴露分数 (e_ij) 作为固定协变量进入 IRT 模型。Stage 1 的暴露测量误差导致 Stage 2 的 γ credible interval 被低估。在 J=16 下尤为严重，可能部分解释 γ 不稳定性（W5）。最低要求：在 Limitations 中承认并讨论对 γ CI 解释的影响。

**W10. Han et al. (2026) 和 Schaeffer et al. (2025) 区分不足 [R8-N4 + R2-W8]**

与 Han et al. 的方法论区分（group-level binary DIF vs. continuous exposure covariate）在方法层面足够，但缺少经验对比。Schaeffer et al. 在 §2 的讨论不充分——他们的统计功效分析与本文的 n=3 seed 局限高度相关，应予讨论。

**W11. Algorithm 1 是描述性启发式，非方法贡献 [R8-W3, CONSENSUS Should-Fix]**

Algorithm 1 的阈值（τ=2pp, σ=5, ρ=0.3）缺乏理论基础。Appendix U 的 sensitivity sweep 有帮助但不改变其本质。应显式定位为"实验结果的组织框架"而非与 IRT 模型并列的方法论贡献。

**W12. Abstract 数字密度过高 [R4-W6, CONSENSUS Should-Fix]**

Abstract 在 ~193 词中包含 20+ 个数字。核心洞见（模型对污染的响应不同，并非都被膨胀）被定量细节淹没。减少到 8–10 个关键数字，以概念发现引领。

**W13. Bayesian/频率主义术语混用 [R8-W1, DIVERGENT→RESOLVED]**

论文同时使用 "credible intervals"（Bayesian IRT）和 "confidence intervals"（bootstrap）以及 "significant"。在首次出现时标注 CI 类型：credible interval（来自 Bayesian IRT）vs. confidence interval（来自 bootstrap）。

**W14. SFT 生态效度警告不足 [R2-W6, Should-Fix]**

SFT 注入同时引入内容暴露、额外训练信号和 LoRA 更新。现实中的污染发生在预训练阶段。Limitations 应明确讨论 SFT 特异性发现能否推广到预训练污染。

### Minor（5 项）

**M1.** Algorithm 1 dead code：Lines 91–94 两个分支（saturating/sustained gain）均返回 BENEFIT。删除冗余或添加子标签。

**M2.** Table 1 'Stab.' 列未在 caption 或脚注中定义。

**M3.** ρ=0.3 saturation ratio 在 Algorithm 1 中使用但未引用来源。

**M4.** Figure 1 图例文字 ~6–7pt，低剂量区域多条线重叠，打印尺寸下难以辨识。

**M5.** Table 2 MAE 精度不一致（混合 3 位和 4 位小数）。

---

## Reviewer Consensus

以下问题两位 Reviewer 达成完全共识：

1. **Volume confound 是论文最关键的弱点**（W1）。R1 从方法/实验角度（单一家族控制）、R2 从概念角度（"污染剂量-响应"概念在 45% 为数据量时的有效性）独立识别，合并后挑战核心叙事。

2. **ContamCal 劣于 baseline 是根本性问题**（W3）。两者一致认为"诊断价值"辩护在 γ 不可靠的情况下不充分。

3. **分类体系需重构为 2+2**（W4）。Collapse/V-Recovery 应显式标为 Qwen2.5 特异的初步观察。

4. **Domain-level γ claims 必须降级**（W5）。R1 从统计理论（J=16 < J≥50 minimum）、R2 从经验证据（仅 Qwen2.5 显示显著域异质性）共同得出 Abstract claim 不成立。

5. **ARC IRT 结果应退出正文**（W6）。PPP=0.003 使 IRT 估计不可靠。

6. **RRF S2 信号必须处理**（W2）。移除后 10× 改善不可忽视。

7. **Abstract 需限定范围**（W7）。两者一致认为需要 SFT-stage 限定。

---

## Reviewer Divergence

**技术新颖性定位 [R3-N7]：**

- **Reviewer 2** 认为 2PL+γ 是标准 explanatory IRT/DIF 方法论，贡献主要是应用框架而非方法创新。各组件（Min-K%++、RRF、explanatory IRT、threshold classification）均为标准方法。
- **Reviewer 1** 部分反驳：training-free contamination signals → RRF fusion → continuous per-item exposure → IRT covariate structure → credible intervals 的完整技术路径此前不存在。γ 的参数化选择（outside vs inside a_i bracket）是有理论含义的非 trivial 设计决策。将方法论贡献降级为 "merely application" 低估了应用层面的创新。
- **共识落点**：论文需要更清晰的定位声明，显式承认 2PL+γ 是标准 explanatory IRT，同时阐明将其应用于 LLM 污染检测（连续暴露协变量）的具体创新之处。当前表述模糊了这一区分。

---

## Questions for Authors

**Q1.** Volume 控制何时能推广到至少一个非 Benefit 家族（如 Collapse 模式的 Qwen2.5-14B）？没有这个控制，剂量-响应分类混淆了污染与数据量效应。

**Q2.** 移除 S2 后 γ 估计和剂量-响应 profile 如何变化？10× ρ_dose 改善暗示下游有实质影响。

**Q3.** Full fine-tuning 是否会产生不同的剂量-响应模式？LoRA 的低秩约束（r=16）可能抑制记忆化效应，使 Benefit 模式可能是 LoRA 特有的 artifact。

**Q4.** 鉴于 γ 在 J=16 下对先验的 2.6× 敏感性，读者应如何解读具体 γ 值（如 Social Sciences γ_d=−0.63）？符号是否稳健即使数值不稳定？

**Q5.** 跨 benchmark 传递有多少是 SFT 引入的指令跟随能力提升，而非真正的污染传播？GSM8K 的 volume 控制显示 53% volume 贡献，支持此替代解释。

**Q6.** 如果框架的价值是诊断而非校准，是否应重命名？当前名称创造了论文无法满足的期望。

---

## Missing References

- **Hill (1910)** — dose-response 是论文标题概念和核心框架。奠基性文献仅出现在 Appendix AB，必须在正文（§1 或 §3）中引用。
- **Deng et al. (2024)** — 引用为 arXiv 但可能已发表于 NAACL 2024，需验证并更新引用元数据。

---

## External Review (Stanford Agentic Reviewer)

**状态：未请求。** 本轮未派发外部审稿。

---

## Visual Layout Check（非评分项）

**状态：已完成**（耗时 ~4 分钟）。

10 项发现，均为 info 级别（0 critical, 0 warning）：

- **Figure 1 (p.1)**：图例文字 ~6–7pt，低剂量区多条曲线重叠。建议加大 marker 差异。
- **Table 1 (p.2)**：8+ 列，紧凑但未溢出。booktabs 格式正确。
- **Table 2 (p.5)**：MAE 精度不一致（3 vs 4 位小数）。
- **Section 5 heading (p.6)**：出现在左栏底部 ~1/4 处，勉强可接受。
- **Page 7**：密度很高（Table 4 + Figure 5 + 5 个 subsection），不影响可读性。
- **Figure 6 (p.8)**：Per-domain CI 图清晰。Limitations ~1 段，EMNLP 合规。
- **Figure 2 (p.3)**：全文最佳 display item——pipeline 架构图，三阶段颜色区分明确。
- **Appendix (p.13, p.17)**：多面板子图 axis label ~6pt，附录可接受。
- **Algorithm 1 (p.18)**：排版规范。

**未检测到格式违规。** 8 页正文确认，EMNLP 2026 合规。

---

## Overall Assessment

**Score: 3.0 (Findings)**

**Confidence: 4/5 (High)**

本文探讨了一个重要问题——不同模型家族如何响应 benchmark 污染——并在生产级规模进行了精心设计的受控实验。核心经验发现（污染不均匀膨胀分数、剂量-响应模式因家族而异）对社区有真正的信息价值。

但论文面临三个相互关联的问题，阻碍了主会议推荐：

1. **方法论框架（ContamCal）未兑现承诺。** 校准性能劣于 raw accuracy，域级估计对先验敏感且在 J=16 下不可靠，核心信号组件之一（S2）主动损害 pipeline 性能。IRT 诊断是论文声称的方法论贡献，但当前状态下其可靠性不如它声称要改进的 baseline。

2. **剂量-响应叙事被混淆。** 45% 的 Benefit 来自数据量，Collapse 可能由额外训练的灾难性遗忘解释，且仅一个家族有 volume 控制。论文无法自信地将剂量-响应模式归因于污染特异性效应。核心主张可能从"模型对*污染*的响应不同"变为"模型对*内容重叠不同的额外 SFT 训练*的响应不同"。

3. **分类体系从不充分的证据过度泛化。** 四个类别来自五个家族，其中两个类别各基于一个家族（均为 Qwen2.5），两个 "已复现" 类别的统计支持从稳健（Immune/Phi-4）到边界（Benefit/OLMo-2）到统计不可区分（Benefit/Gemma-2 on AICc）。

这些问题单独看是实质性的，合并后相互强化：volume confound (1) 削弱 taxonomy (3)，而 IRT 框架的不可靠性 (2) 削弱了本可帮助解纠缠混淆因素的域级诊断。鉴于真正的经验贡献，Findings 级别发表是合适的，但主会议接收需要解决 volume 控制缺口、pipeline 完整性和框架重新定位。

---

## Detailed Comments

### Abstract
- 首句需显式限定范围："across *five open-source* model families *at 7B–14B scale under SFT injection*"
- "enables within-family domain-level contamination diagnosis with credible intervals" 在 J=16 下不成立，替换为限定性语言或删除
- 20+ 数字减至 8–10，以概念发现引领
- 字数 ~193，在 EMNLP 2026 的 200 词限制内

### Section 1 (Introduction)
- 引入 dose-response 概念时引用 Hill (1910)
- 将 claims 限定至 SFT injection at 7B–14B

### Section 2 (Related Work)
- 扩展 Schaeffer et al. (2025) 讨论——其统计功效分析直接相关于 n=3 seed 局限
- Han et al. (2026) 方法层面区分足够；考虑增加 1–2 句经验对比范围

### Section 3 (Method)
- §3.2：增加一句说明 ΔELPD ≈ 0（γ outside vs inside a_i），选择基于解释便利性
- §3.3：承认 e_ij 点估计限制及对 γ CI 宽度的影响
- §3.4：显式声明 Algorithm 1 是描述性启发式，非方法贡献

### Section 4 (Experimental Setup)
- 报告 volume 控制设计理由和局限（仅测试 Falcon3）

### Section 5 (Results)
- §5.1：重构为 2 confirmed (Immune, Benefit) + 2 preliminary (Collapse, V-Recovery)，增加 AICc 证据
- §5.2：ARC 跨 benchmark 结论必须基于 raw accuracy 而非 IRT，增加显式声明
- §5.5：从 "Calibration Quality" 改写为 "Diagnostic Utility"，以域级 γ_d 对比引领，将聚合 MAE 定位为非目标指标
- 域级 γ 讨论处：在正文（非仅附录）中增加 prior sensitivity 警告

### Section 6 (Discussion)
- 增加段落讨论 triple confound (content/volume/LoRA)
- 更显著地呈现 Falcon3 45%/55% 分解
- 删除或限定 "65–70% baseline vulnerability band"（基于 2 个 Qwen 模型，被 LLaMA 反例推翻）

### Limitations
- 承认：(a) 单一家族 volume 控制，(b) SFT 特异性发现可能不推广到预训练污染，(c) 暴露测量不确定性未传播到 γ CI

### 格式
- 首次出现时标注 CI 类型："credible interval (from Bayesian IRT)" vs "confidence interval (from bootstrap)"
- Table 1：定义 'Stab.' 列
- Algorithm 1：删除 dead branching (lines 91–94)
- Figure 1：增大图例字号，区分 markers