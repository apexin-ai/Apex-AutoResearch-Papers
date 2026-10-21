---
round: 11
review_mode: fresh
overall_score: 3.0 — Findings
timestamp: 2026-05-23T10:24:43.197966+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告 — Round 13 (Fresh Review)

**论文**: *Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families*
**Venue**: EMNLP 2026 (ARR Long Paper)
**审稿模式**: Fresh（重新审稿，无先轮记忆）
**Reviewer 编排**: 2 人（R1: 方法严谨性+实验设计；R2: 新颖性+完整性+写作质量）

---

## Summary

本文提出 ContamCal 框架，结合多信号污染暴露映射（RRF 融合 3 类检测信号）与污染增强 IRT 模型（2PL+γ），对六个 ≤14.7B 模型（来自五个独立家族）在五个 SFT 注入剂量水平下的 benchmark 污染效应进行受控实验。核心发现：污染效应是家族特异的——Immune（Phi-4, LLaMA-3.1）、Benefit（Gemma-2, Falcon3, borderline OLMo-2）、Collapse 和 V-recovery（均仅 Qwen2.5）——而非均匀膨胀。DiD 分析未检测到 item-specific memorization（MDES 1.2-2.0pp）。

---

## Strengths

**S1. 受控 SFT 注入实验设计的系统性** [CONSENSUS]
5 家族 × 5 剂量 × 统一 LoRA 配置 × 多种子复现 × 跨 benchmark 迁移测试，是迄今对 LLM 污染进行的最系统的受控实验之一。75 种 model-dosage 配置的覆盖面在领域内具有突出价值。

**S2. Immune 和 Benefit 模式的跨家族复现** [CONSENSUS]
Immune（Phi-4 + 独立验证 LLaMA-3.1）和 Benefit（Gemma-2 CI 排除零, Falcon3 方向一致）在独立家族中复现。"Not all models are inflated" 的核心论点有数据支撑。

**S3. 跨 benchmark 迁移分析** [CONSENSUS]
MMLU 污染对 GSM8K 的迁移效应揭示了污染通过全局能力调制（而非 item memorization）影响模型，是论文的独到发现。

**S4. 诚实报告负面结果** [CONSENSUS]
ContamCal MAE > Raw MAE、DiD null result、AICc 模型比较、OLMo-2 CI 跨零等均如实报告。Collapse/V-recovery 被标注为"await independent replication"。这种透明度在该领域少见。

**S5. 附录极其详尽** [CONSENSUS]
13 页附录覆盖 identifiability simulation、prior sensitivity、signal ablation、DIF parameterization comparison、domain decomposition、parametric DR model comparison、volume control 等，为可复现性提供了强支持。

---

## Weaknesses

### Must-Fix（影响接收决定）

**MF1. ContamCal 校准 MAE 劣于 Raw Accuracy** [CONSENSUS Critical — R1-N1 = R2-N1]

Table 3 (p.8): ContamCal MAE=0.009, B0-Raw MAE=0.006 (MMLU); ARC 更差（Appendix Z: 0.020 vs 0.007）。以"Calibration"命名的框架在校准任务上不如"什么都不做"基线。论文辩护"value lies in domain-level diagnosis"，但此辩护本身有问题：(a) 方法名与实际价值不匹配；(b) 如果 observed dosages 下效应小到 raw accuracy 已足够，框架附加价值存疑；(c) domain-level 诊断不一定需要完整 IRT 框架。

R1 补充：IRT 确实提供了 raw accuracy 无法提供的 credible intervals 和 item-level modeling，但在 γ 不可靠识别（见 MF3）的情况下，这些增量价值的可信度被削弱。

→ 必须重新定位核心贡献：实证 profiling 发现优先于框架校准精度。

**MF2. S2 (Min-K%++) 在 RRF 中主动损害剂量-响应信号** [CONSENSUS Critical — R1-N2, R2-AGREE]

Appendix E Table 7: 移除 S2 后 MMLU ρ_dose 从 0.049 跳至 0.471（~10× 改善）。S2 不是"无信息"而是主动压制模型级别的剂量信号。论文以"provides unique item-level information (ρ ≈ 0.773)"辩护，但 item-level 相关性不能为 model-level 损害正名。

R2 补充：如果 S2 对所有 items 给出相似分数模式（与真实污染无关），这意味着系统性偏差。关键缺失实验：移除 S2 后完整 pipeline 的 ContamCal MAE 是否改善？如果改善到优于 Raw=0.006，将根本改变论文结论。

→ 必须提供不含 S2 的 pipeline 作为主分析或参考基线。

**MF3. γ 后验对先验高度敏感，J=16 下可识别性不足** [CONSENSUS Critical — R1-N3, R2-AGREE]

Appendix M: 先验 N(0,0.5)→N(0,2) 时 γ 后验均值从 0.34 变为 0.89（2.6×）。95% CI 在所有先验下包含零。论文自承"J=16 provides insufficient data to override the prior"（Appendix M），但此关键 caveat 仅在附录第 16 页——正文将 γ 估计当作数据驱动结果使用。

R2 指出闭环：γ 不可靠 → 2PL+γ 校准不可靠 → MAE 劣于 Raw（MF1）。如果 γ 主要由先验驱动，"contamination-augmented" IRT 的增量贡献实质为零。

→ 正文必须讨论先验敏感性；明确 γ 绝对值不可靠，仅方向性结论可信。

**MF4. ARC PPP=0.003 严重模型失拟下的结果仍用于主分析** [CONSENSUS Critical — R1-N4, R2-AGREE]

Appendix Z 承认 ARC PPP≈0.003，"structural misfit"。但 §5.2 cross-benchmark transfer 分析和 Table 4 仍包含 ARC IRT 结果。在已知模型失拟的 benchmark 上报告该模型的结果会误导读者。

→ ARC IRT 结果应移至附录；主分析 ARC 结论应仅基于 raw accuracy。

**MF5. 四模式分类法 overclaiming 为通用 taxonomy** [CONSENSUS Critical — R2-N2, R1-AGREE+补充]

Collapse/V-recovery 仅在 Qwen2.5（同一家族的两个规模变体）中观察到。Abstract 和 Algorithm 1 将其与 Immune/Benefit 并列为已确立的通用分类。R1 进一步补充：即使 Benefit 的统计基础也不牢固——AICc 显示 Gemma-2/OLMo-2 与 constant 不可区分，OLMo-2 CI 跨零。严格来说，唯一统计 robust 的分类是 Immune（Phi-4）。

→ 必须重构为"2 个已确认模式 + 2 个待确认的 Qwen2.5 特有观察"。

**MF6. AUGMENT 模式 volume confound 未充分控制** [CONSENSUS Critical — R2-N3 = R1-W3 升级]

d100 训练量 +33%（66.5k vs 50.0k）。仅 Falcon3 做了 volume control，显示 45% 归因于数据量。这意味着 Benefit 效应的近一半可能来自额外训练而非污染内容。关键缺失：Collapse 家族（Qwen-14B，-25pp）的 volume control——catastrophic forgetting from extra training volume 是未排除的替代解释。

R1 建议：至少对一个非 Benefit 家族重复 volume control，或将分类标签从"contamination response"改为"SFT injection response (contamination + volume)"。

→ 至少在一个非 Benefit 家族做 volume control；或在全文中使用"SFT injection effect"替代"contamination effect"。

### Should-Fix（影响评分但不一票否决）

**SF1. e_ij 作为点估计输入 IRT，缺失 uncertainty propagation** [CONSENSUS — R1-W1, R2-AGREE]
RRF 融合产生点估计 e_ij，作为 IRT 固定协变量使用。暴露测量误差被忽略 → γ CI 被低估。在 J=16 下尤为严重。可能部分解释 γ 不稳定性（MF3）。

**SF2. n=3 seeds 下 BCa CI 支撑力不足** [CONSENSUS — R1-W2, R2-AGREE]
n=3 BCa bootstrap resample 空间极小。OLMo-2 CI 跨零但被归类为 borderline Benefit。AICc 显示 Gemma-2/OLMo-2 与 constant 不可区分。正文应明确区分统计显著分类和仅基于 3 seeds 的探索性分类。

**SF3. Algorithm 1 是描述性启发式，不应定位为方法贡献** [CONSENSUS — R2-W1 = R1-W4]
τ=2pp 等阈值是描述性的，非统计检验。Appendix U 的 sensitivity sweep 缓解了 robustness 但不改变其本质。应定位为"实验结果的组织框架"而非方法贡献。Algorithm 1 的 Benefit 分支有 dead code（Lines 91-94 两分支都返回 BENEFIT）。

**SF4. Abstract 数字密度过高** [CONSENSUS — R2-W2, R1-AGREE]
~250 词中 20+ 个具体数字，核心信息被淹没。应精简至 3-4 个关键数字。

**SF5. Title 暗示广泛适用性与实验覆盖不匹配** [CONSENSUS — R2-W4, R1-AGREE]
"Not All Models Are Inflated" + "Across Model Families" 暗示普遍结论，实验仅 6 模型 ≤14.7B，全部 SFT injection，全部开源。建议在 Abstract 首句即明确 scope。

**SF6. "contamination vs. additional training" 概念张力** [CONSENSUS — R2-W6, R1-AGREE]
SFT injection 同时引入 content exposure + extra volume + LoRA updates。Table 1 标签隐含将全部效应归因于 contamination，但 volume control 数据表明 45% 来自数据量。需在 Discussion 专段讨论。

**SF7. DiD MDES 1.2-2.0pp 实际意义未充分讨论** [CONSENSUS — R1-W5, R2-AGREE]
null result 成立前提是 <1.2pp 的效应不具实际意义。但在高 stakes 评估中 1pp 可能有实质影响。需讨论 MDES 在不同应用场景下的意义边界。

### Minor

**m1.** Figure 1 y 轴范围不一致，可能视觉上夸大变化幅度。[R1]
**m2.** Figure 1 caption ~60 词，过于密集。[R2]
**m3.** Figure 2/3 heatmap cell 字号过小，打印时可能难辨认。[Visual check]
**m4.** 300 items 子采样代表性验证未检查 exposure variance bias。[R1]
**m5.** Table 1 "Stab." 列定义不清。[R1, R2]
**m6.** ρ=0.3 saturation ratio 来源未明。[R1]
**m7.** Limitations 中"70B+ models may exhibit qualitatively different dynamics"无文献支撑。[R1]
**m8.** Split-R̂ 术语对 NLP 读者应加解释。[R2]
**m9.** Deng et al. 引用可能需从 arXiv 更新为 NAACL 2024。[R2]

---

## Reviewer Consensus

| 问题 | R1 | R2 | 结果 |
|------|----|----|------|
| ContamCal MAE > Raw | N1 (Critical) | N1 (Critical) | **CONSENSUS Critical** |
| S2 主动损害 RRF | N2 (Critical) | AGREE | **CONSENSUS Critical** |
| γ 先验敏感性 | N3 (Critical) | AGREE | **CONSENSUS Critical** |
| ARC PPP 失拟 | N4 (Critical) | AGREE | **CONSENSUS Critical** |
| 四模式 taxonomy overclaiming | AGREE+补充 | N2 (Critical) | **CONSENSUS Critical** |
| Volume confound | W3→升级 | N3 (Critical) | **CONSENSUS Critical** |
| e_ij uncertainty propagation | W1 (Warning) | AGREE | **CONSENSUS Warning** |
| n=3 seeds 不足 | W2 (Warning) | AGREE | **CONSENSUS Warning** |
| Algorithm 1 启发式 | W4 (Warning) | W1 (Warning) | **CONSENSUS Warning** |
| Abstract 数字密度 | AGREE | W2 (Warning) | **CONSENSUS Warning** |
| Title scope | AGREE | W4 (Warning) | **CONSENSUS Warning** |
| contamination vs training | AGREE | W6 (Warning) | **CONSENSUS Warning** |
| DiD MDES significance | W5 (Warning) | AGREE | **CONSENSUS Warning** |
| γ bracket placement (ΔELPD≈0) | W6 (Warning) | REBUT | **RESOLVED** (R2 正确：选择合理) |

---

## Reviewer Divergence

**D1. 2PL+γ 方法新颖性** [RESOLVED — 无需进一步讨论]
- R2 (W3): 2PL+γ 是标准 explanatory IRT/DIF 实例，不构成方法新颖性。
- R1 (REBUT): 应用层面仍有创新——连续 RRF exposure（非传统二元 DIF）、per-benchmark fitting、嵌入 causal framework。但同意需更清晰的定位声明。
- **综合判断**：应在正文中明确承认模型本身是标准 DIF，贡献在于应用框架和实证发现。

**D2. Bayesian-frequentist 混用** [RESOLVED — 降级为 minor]
- R2 (W5): 三种推断框架混用未交代。
- R1 (REBUT): NLP 领域惯例，无逻辑矛盾。
- **综合判断**：在首次出现处标注 CI 类型（credible vs confidence）即可。

---

## Questions to Authors

1. **[最关键]** 移除 S2 后完整 pipeline 的 ContamCal MAE 是否优于 Raw=0.006？如果是，当前论文结论需根本性调整。
2. 是否存在某个 contamination 剂量阈值，使得 ContamCal 开始优于 Raw？如果不存在，ContamCal 作为校准工具的使用场景是什么？
3. Table 1 中的 dose-response 分类在不同 γ 先验下是否改变？
4. Qwen-14B 的 Collapse（-25pp at d100）是否可能主要由 +33% 训练数据量导致的 catastrophic forgetting？
5. 无 ground-truth labels 时，如何验证 Stage 1 信号 AUC ≥ 0.55 的要求是否满足？

---

## Missing References

R2 系统审查了被要求检查的 6 项工作，均已引用。50+ 参考文献覆盖全面。两个 minor 改进点：
- Deng et al. 可能需从 arXiv 更新为 NAACL 2024 正式出版信息
- Schaeffer et al. (2026) 在 §2 Related Work 中的讨论可更深入（特别是其 statistical power 讨论与本文 n=3 seeds 限制高度相关）

---

## External Review (Stanford Agentic Reviewer)

外部审稿：未请求。项目配置中未启用外部审稿。

---

## Visual Layout Check（非评分项）

视觉审查已完成（4 warnings, 20 infos, 0 critical）：

**Warnings:**
- Pages 3-5 连续 3 页无 figure/table（Method 部分），视觉单调。建议将 Appendix Figure 4（ContamCal 三阶段 pipeline 概念图）提升至正文 Method 部分
- Figure 4（pipeline 架构图）被放在 Appendix 而非正文——这是全文唯一的方法概览图，浪费了正文中的视觉锚定作用
- Figure 2（baseline vulnerability heatmap）尺寸偏小，cell 内数字打印时可能难辨认
- Figure 3（cross-benchmark transfer heatmap）同样偏小，cell 字号约正文 50-60%

**通过项：**
- 正文 8 页，Limitations 在 p.8 底部，EMNLP 2026 合规 ✓
- Figure 1 在 p.2 顶部，Title-Abstract-Figure 1 叙事对齐 ✓
- 所有表格使用 booktabs 风格，专业规范 ✓
- Figure/Table 均在首次引用附近，无 float 漂移 ✓
- 匿名性通过（"Anonymous ACL submission"）✓
- 无 LaTeX 错误残留、无异常空白 ✓

---

## Overall Assessment

**Overall Score: 3.0 / 5 — Findings**

| 维度 | R1 | R2 | 综合 |
|------|----|----|------|
| Soundness | 2.5 | 3.0 | **2.75** |
| Excitement | 3.5 | 3.0 | **3.25** |
| Reproducibility | 4.0 | 4.0 | **4.0** |
| Overall | 3.0 | 3.0 | **3.0** |
| Confidence | 4.0 | 4.0 | **4.0** |

**置信度**: 4/5（两位 Reviewer 均仔细通读全文和 13 页附录，验证了具体数字和 claims）

**核心判断**：

论文的实验设计（受控 SFT 注入 × 5 家族 × 5 剂量）是该领域的重要贡献，"not all models are inflated" 的核心发现有价值且有数据支撑。然而六个 Must-Fix 问题共同构成了方法论层面的严重隐患：

1. **校准劣势**（MF1）+ **γ 不可识别**（MF3）+ **S2 有害**（MF2）形成闭环：核心方法在技术上不能交付其 promise
2. **Taxonomy overclaiming**（MF5）+ **volume confound**（MF6）削弱了实证贡献的可信度
3. **ARC 失拟**（MF4）影响 cross-benchmark 论证的可靠性

论文的核心价值在于实证发现（家族特异性 dose-response）而非方法框架（ContamCal）。如果重新定位为以实证发现为主的论文——降低 ContamCal 的 claim 强度、重构 taxonomy 为 2+2、扩展 volume control、修正 RRF pipeline——有潜力达到 Conference (3.5-4.0) 档位。当前状态适合 Findings (3.0)。

---

## Detailed Comments（逐节）

### Abstract
- 20+ 数字过密，核心 insight 被淹没。精简至 3-4 个关键数字。
- BCa CI、paired Cohen's d 等统计细节不适合 Abstract。
- "ContamCal, our diagnostic framework" — 如果重定位为诊断而非校准，名称本身就有误导性。

### §1 Introduction
- Contribution 1 声称"cross-seed and cross-benchmark validation"但 OLMo-2 CI 跨零、AICc 不可区分。
- Contribution 2 "enables domain-level contamination diagnosis with credible intervals" — 但 γ 在 J=16 下不可靠识别。
- "Our methodological contribution lies not in the IRT specification" (p.5 末) — 此声明正确但应更早出现（在 Abstract/Contribution 中）。

### §2 Related Work
- Han et al. (2026) 差异化在方法层面充分，缺乏实证发现交叉比较。
- Schaeffer et al. (2026) 讨论不足——其 pretraining-stage 结果可与本文 SFT-stage 结果直接对比。

### §3 Method
- §3.1: S2 AUC≈0.48-0.51 近随机但保留在 pipeline 中——需要更强的正当性论证或移除。
- §3.2: γ 先验敏感性应在此处讨论而非仅在 Appendix M。
- §3.2: ΔELPD≈0 说明 γ bracket 选择是约定性的——应明确表述。
- §3.4: Algorithm 1 应标注为 descriptive classification scheme。Dead code（Lines 91-94）应清理。

### §4 Experimental Setup
- §4.1: AUGMENT mode 的 volume confound 需要更显著的讨论。
- LoRA r=16 统一配置导致 trainable parameter % 差异 4.7×（已在 Limitations 讨论，可接受）。

### §5 Results
- §5.1 Table 1: "Repl." 列中 Collapse/V-recovery 的 △ 标记与文本中"observed profiles"定位不一致——应统一。
- §5.3: OLMo-2 "borderline" 的处理合理，但 Abstract 和 Contribution 1 中未反映。
- §5.5 Table 3: ContamCal MAE=0.009 > Raw=0.006 是论文最大的方法论挑战。"Calibration Quality" 标题与内容矛盾。
- §5.6: Min-K%++ 方向反转的分析是论文的亮点之一。
- §5.7: Social Sciences γ_d 的 prior sensitivity 分析（Table 11）很有价值，但主分析 γ 的同级分析仅在附录。

### §6 Discussion
- "65-70% baseline range" 仍出现，但被 LLaMA-3.1 直接反驳——应降格或删除。
- "contamination vs additional training" 段落存在但讨论不足。
- Volume control 的 45% volume / 55% content 分解应该更显著地出现在 Discussion 中。

### Limitations
- 覆盖了模型规模、SFT vs pretraining、种子敏感性、LoRA 统一配置、AUGMENT volume。长度适当。
- 缺失：300 item 子采样的 exposure variance bias、MDES 实际意义边界。