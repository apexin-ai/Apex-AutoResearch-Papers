---
round: 1
review_mode: fresh
overall_score: 3.0 — Findings
timestamp: 2026-05-23T06:41:15.267815+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告 — Round 1

**论文**: Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Fix
**目标 Venue**: EMNLP 2026 via ARR
**截止日期**: 2026-05-25
**审稿日期**: 2026-05-23
**Reviewer 编排**: R1（方法严谨性）+ R2（新颖性/完整性）
**交叉轮次**: 1 轮交叉分享，关键问题全部收敛

---

## Summary

本文诊断了多轮 agent RL 中 step-independent windowing 的两个失败机制：policy information loss (M1，截断上下文造成恒定性能天花板) 和 advantage sign misattribution (M2，梯度方向错误造成累积退化)。通过 2×2 factorial 实验分离两个机制的贡献，并展示 episode-level GRPO（GRPO 的原始设计）可解决两者。11-seed 系统评估表明 73% 的 seed 避免崩溃，但仅 27% 实现 OOD 泛化。跨尺度 (8B) 和跨环境 (ScienceWorld) 验证提供了初步 generality 证据。

---

## Strengths

**S1. 精准的问题诊断与结构化分析框架 [R1-S1, R2-S1, 共识]。** 将 step-independent training 崩溃分解为 M1 (constant ceiling) 和 M2 (cumulative divergence) 两个可分离机制，对社区理解此类 failure mode 有明确价值。这种诊断性贡献在同期工作中独特。

**S2. 干净的 factorial 实验设计 [R1-S2, R2-S1, 共识]。** A→B 消除 M2（collapse → bounded learning），B→D 消除 M1（bounded → generalization），辅以 dense reward、γ sweep、REINFORCE++ 等控制实验系统排除替代假说。

**S3. 坦诚的负面结果报告 [R1-S3, R2-S2, 共识]。** 11-seed 评估的 27% 泛化率透明报告，"necessary but not sufficient" 的 claim 定位准确。

**S4. 多层次实证验证 [R1-S4, 共识]。** Credit agreement rate (52.07% ≈ random)、advantage sign 与 episode outcome 高相关 (r>0.99) vs local quality 低相关 (r=0.068)、γ=1.0 同样崩溃——系统排除了 discounting 假说。

**S5. 跨尺度/跨环境验证方向正确 [R2-S3, 部分共识]。** 1.7B→8B 和 ALFWorld→ScienceWorld 的验证思路正确，但均为 single seed（见 W4）。

---

## Weaknesses

### Must-Fix (Critical)

**W1. "Locally correct actions" 缺乏形式定义 [R1-C1, R2 AGREE]。**
整个理论框架建立在 "locally correct actions" 上，但全文未给出形式定义。Proposition 2 的 "80.9% incorrect sign" 含义完全取决于 "correct" 的定义。Section 4.4 的 credit agreement rate 度量的操作化方式（如何度量 "local action quality"）也未描述。两位 Reviewer 共识：需要形式定义，但非循环论证（R2 的修正判断——核心论点 "sign 由 episode outcome 决定" 不依赖 local quality 的精确定义）。

**W2. 理论 (binary reward) 与实验 (binary + invalid action penalty) 不一致 [R1-C2, R2 AGREE]。**
Propositions 1-2 严格依赖 binary reward (R ∈ {0, r+})，但实验使用了 invalid action penalty = 0.1。Appendix Remark 仅定性声称 "qualitative conclusion is preserved"，无定量分析。R2 补充：Proposition 2 预测 19.1% correct sign rate，实测 52.07%，discrepancy 可能正是 non-binary reward 导致，但论文未讨论。

**W3. 10/20 引用使用 "Anonymous" 作者——ARR 格式违规 [R2-W1, R1 AGREE]。**
irc2026, grpolambda2025, oar2026, ragen2_2026, grpocollapse2025, gradientcoupling2025, turnppo2026, gagpo2026, mtgrpo2025, sweetrl2025——这些均为已公开 arXiv 预印本，有可查的真实作者信息。ACL ARR 仅要求匿名化自己的在审稿件，不应匿名化他人已公开工作。50% 引用缺少真实作者是严重合规问题，可能触发 desk-rejection checklist。

### Should-Fix (Major)

**W4. 8B 和 ScienceWorld claims 基于 single seed [R1-M3, R2-W4, 共识]。**
论文在 1.7B 上用 11 seeds 发现 27% collapse、36% stagnant、27% generalize，但 8B 和 ScienceWorld 均为 single seed。"Both mechanisms operate across environments, confirming..." 的 confirmatory language 与实际 statistical power 不匹配。应降级为 "preliminary evidence"。

**W5. h-sweep cliff claim 基于 single seed [R1-M2, R2 AGREE]。**
Figure 1(b) 的 h=10→h=20 "credit assignment cliff" 基于 seed 1 的单次结果。结合 Table 2 的高 seed variability（同条件下 8.21%–30.60%），无法排除 seed-specific 噪声。

**W6. 核心贡献新颖性有限 [R2-W2, R1 部分 REBUT]。**
Fix 是回归 GRPO 原始设计（论文自己承认 "This is GRPO's original design"）。同期 5+ 独立工作（IRC, MC-GRPO, GRPO-λ, OAR, RAGEN-2）收敛到类似诊断。R1 反驳：M1/M2 factorial 分离框架有独立价值，但同意在 Findings 定位下合适，不足以支撑 main conference。**分歧记录**：R2 认为 critical（Excitement 2.5），R1 认为 major（Excitement 3.5）。

**W7. 引用数量不足：仅 20 篇 [R2-W3, R1 AGREE]。**
EMNLP long paper 通常 40-60 篇引用。缺失类别：RL 基础（PPO、reward shaping classics）、LLM agent 训练/评估（AgentTuning, Reflexion, ReAct）、credit assignment 相关（COMA, PRM, Math-Shepherd）。R1 对 agent benchmark 类引用的优先级低于 R2。

**W8. Cell C 缺失使 factorial 不完整 [R1-M1, R2 AGREE]。**
Cell C (full observation + step-level advantage) 被论述为 "degenerate"，但概念上可实现（每步看全 history，advantage 仍 per-window）。缺失意味着 M2 无法在无 M1 条件下独立验证。

**W9. 15 步训练可能不利于 baseline 方法 [R1-M5, R2 部分 AGREE]。**
REINFORCE++ 停留在 SFT baseline (12.5%) 可能因训练不足而非方法无效。R2 补充：Cell A 的崩溃不受此影响（主动退化），concern 主要针对 REINFORCE++ 等替代方法。

**W10. Conclusion 对 "80.9%" claim 省略 qualifier [R1-M4, R2 AGREE on wording]。**
Abstract 写 "for locally correct actions" 但 Conclusion 省略为 "~80.9% of gradient updates carry incorrect sign"——扩大了 claim 范围。R2 修正：在 binary reward 假设下 80.9% 是精确值而非 upper bound，但 qualifier 省略确实是 overclaim。

**W11. 理论分析深度有限 [R2-W5, R1 部分 AGREE]。**
P(correct|update) = p/[1-(1-p)^K] 是简单条件概率。缺乏从 "80.9% wrong sign" 到 "training will diverge" 的形式化连接。R1 建议：简化设定下的发散证明可显著增强理论贡献。

### Nice-to-Fix (Minor)

**W12.** Table 1 对不同 cell 使用不同报告标准（best seed / best checkpoint / mean）[R1-m1, R2 AGREE]
**W13.** Eq. 3 近似条件不明确 [R1-m2, R2 AGREE]
**W14.** Section 4.4 "local action quality" 操作化定义未描述 [R1-m3, R2 AGREE]
**W15.** Appendix A.3 "Why Defaults" 部分 Factor 3 措辞偏 editorial，"design accident" 建议改为 "inherited default" [R1-m4, R2 部分 REBUT]
**W16.** RAGEN 版本/commit hash 未报告 [R1-m5, R2 AGREE]
**W17.** "fundamental" 一词过度使用（5+ 次）[R2-W6, R1 AGREE]
**W18.** Dense reward 实验细节不足（Appendix 仅两句话）[R2-W7, R1 AGREE]
**W19.** Figure 1(a) 图例字号偏小、多线区分度有限 [R2-W8, R1 AGREE]

---

## Reviewer Consensus

以下问题两位 Reviewer 一致同意（`[AGREE]`）：
1. "locally correct actions" 需要形式定义（但非循环论证）
2. Binary reward 理论与 non-binary 实验存在 gap
3. Anonymous 引用是严重格式违规
4. 8B/ScienceWorld/h-sweep 的 single-seed claims 统计 power 不足
5. 引用总量不足
6. Table 1 报告标准应统一
7. RAGEN 版本需报告
8. COMA、PRM、PPO 等为高优先级缺失引用

## Reviewer Divergence

| 议题 | R1 | R2 | 说明 |
|------|----|----|------|
| **新颖性严重性** | Major（Findings 可接受） | Critical（影响 Excitement） | R1 认为 M1/M2 factorial 分离有独立值；R2 更重视 fix 非新方法+同期工作多 |
| **Excitement** | 3.5/5 | 2.5/5 | 0.5 分差——R1 偏重诊断价值，R2 偏重方法创新 |
| **Soundness** | 3/5 | 3.5/5 | R2 认为 factorial 方法论扎实抵消了理论缺陷 |
| **R1-M4 (80.9% 性质)** | Upper bound | 精确值（under assumptions） | R2 修正：在 binary reward 假设下是精确计算 |
| **Cell B 下降原因** | M1 下 overfitting（不需要第三机制） | 可能暗示第三机制 | R1 反驳成立——overfitting 解释与 evidence 一致 |

---

## Questions（需要作者澄清）

**Q1.** Section 4.4 中 "local action quality" 具体如何度量？操作化定义是什么？

**Q2.** 是否在 pure binary reward（无 invalid action penalty）下验证了 credit agreement rate？如果有，结果与 52.07% 差异多大？19.1% vs 52.07% 的 discrepancy 如何解释？

**Q3.** seed1 使用 "RAGEN built-in eval; checkpoint unavailable for re-evaluation"——与其他 seed 的 eval protocol 是否完全一致？

**Q4.** Episode-level training 在 1.7B 上的实际 GPU 内存使用和训练时间 vs step-independent？

**Q5.** 11-seed 中是否分析了 generalized vs stagnant seeds 的初始化特征差异？

**Q6.** 是否有与 Turn-PPO 或 GAGPO 的直接实验对比？

---

## Missing References

**高优先级**（与论文主题直接相关，两位 Reviewer 共识）：
- PPO (Schulman et al., 2017) — 论文多处提及但未引用原始文献
- COMA (Foerster et al., 2018) — 论文 Appendix A.4 画了多智能体类比但未引用
- Process Reward Models / Let's Verify Step by Step (Lightman et al., 2023)
- Math-Shepherd (Wang et al., 2023)
- ReAct (Yao et al., 2023)

**中优先级**（领域 background）：
- TRPO (Schulman et al., 2015)
- Hindsight Experience Replay (Andrychowicz et al., 2017)
- Reward shaping theory (Ng et al., 1999)
- QMIX (Rashid et al., 2018)

**可选**（R1/R2 优先级有分歧）：
- AgentTuning, Reflexion, WebShop, AgentBench, FireAct
- RC-GRPO (arXiv:2602.03025)
- TSR (arXiv:2602.11767)

---

## External Review (Stanford Agentic Reviewer)

外部审稿：未配置。

---

## Visual Layout Check（非评分项）

状态：**done**（2026-05-23T06:24 → 06:27，耗时约 3 分钟）

| 严重性 | 位置 | 发现 |
|--------|------|------|
| **critical** | page 12 | 仅 ~10 行文字后整页空白（>80%），LaTeX float 问题——Figure 4 被推到 page 13 留下空页。需调整 float placement。 |
| warning | page 1-3 | 前 3 页无任何 display item（figure/table），审稿人前 4 页只见纯文本+数学推导。建议将 Figure 1 或概念图提前到 page 1-2。 |
| warning | page 5 | 单页承载 1 figure + 2 tables，视觉密度过高，与前 3 页纯文本形成强反差。考虑平衡分布。 |
| warning | page 13 | Figure 4 位于页面下半部，上方 ~40% 空白。与 page 12 合计附录末尾 2 页空间利用率极低。 |
| info | page 5 | Figure 1 legend 字号偏小（约正文 60%），多条目密集排列。 |
| info | page 7 | Figure 3(a) 部分 bar 上数值标注字号较小，打印阅读可能吃力。 |
| info | page 4 | 论文第一个 display item（Table 1）出现在 page 4，对实证论文偏晚。 |

---

## Overall Assessment

**Overall: 3.0 — Findings**

| 维度 | R1 | R2 | 综合 |
|------|----|----|------|
| Soundness | 3/5 | 3.5/5 | 3/5 |
| Excitement | 3.5/5 | 2.5/5 | 3/5 |
| Reproducibility | 3/5 | 3.5/5 | 3/5 |
| Confidence | 4/5 | 4/5 | 4/5 |

**评分理由**：

论文精准识别了 step-independent agent RL 中一个重要且广泛存在的 failure mode，M1/M2 dual mechanism 分离框架和 factorial 实验设计是扎实的诊断性贡献。坦诚的 11-seed 负面结果报告增强了可信度。

但存在以下限制：(1) 理论核心概念 "locally correct actions" 缺乏形式定义，理论与实验的 reward structure 不一致（binary vs binary+penalty），削弱了理论-实验闭环；(2) 关键 generality claims（8B、ScienceWorld、h-sweep cliff）均基于 single seed，与论文自身展示的高 seed 方差矛盾；(3) 核心 fix 是回归 GRPO 原始设计，方法新颖性有限；(4) 50% 引用使用 Anonymous 作者，存在 ARR 合规风险。

在 Findings 定位下，诊断性贡献（M1/M2 分离 + factorial 验证 + seed variability 分析）达到接收门槛。升级到 Conference 需要：形式化 "locally correct" 定义、补充 multi-seed 8B 验证、修复引用格式、增加引用覆盖。

---

## Detailed Comments

### Abstract
- "fundamental credit assignment pathology" 措辞过重，建议改为 "structural"
- "80.9% of gradient updates for locally correct actions carry incorrect sign" — qualifier 正确，但需在全文保持一致（Conclusion 省略了 qualifier）
- "consistent with an empirically measured 52% credit agreement rate" — 理论预测 19.1% vs 实测 52%，两者关系未解释

### Section 1 (Introduction)
- Contribution 3 "necessary but not sufficient" 定位准确，但意味着 73% 的情况下方案不达目标，实际影响力存疑
- 第一段对同期工作的定位（"share a common, unscrutinized implementation pattern"）需加入更多具体引用

### Section 2 (Method)
- POMDP 形式化标准，无问题
- M1/M2 分离是论文最有价值的概念贡献
- Eq. 3 的 ≈ 号缺乏成立条件说明
- Cell C "degenerate" 论述混淆了实现方式与概念区分

### Section 3 (Theoretical Analysis)
- Proposition 2 推导在 binary reward 假设下数学正确
- 缺少 p 随训练动态变化时的分析（正反馈循环仅在 Discussion 定性提及）
- "sign errors cause active divergence" 缺乏梯度动态系统的形式化分析

### Section 4 (Experiments)
- Table 1 报告标准不一致（best seed / best checkpoint / mean）
- Section 4.4 sign verification 是亮点实验，但 "local action quality" 操作化未描述
- Section 4.5 的 11-seed 分析有价值，"collapsed" 定义（>50% decline for ≥3 steps）可做 sensitivity analysis
- Table 3 (8B) 使用不同解码温度（SFT: τ=0, RL: τ=0.4），引入额外变量
- Section 4.7 ScienceWorld 仅展示 Cell A 崩溃，未报告 episode-level 的正面结果

### Section 5 (Related Work)
- 结构合理但覆盖面不足（20 篇引用）
- "but all share a common assumption: trajectory decomposition into fixed windows is benign" 过强——GiGPO/GAGPO 明确在 windowing 框架内改进 credit assignment

### Section 6 (Discussion)
- M1-M2 interaction（正反馈循环）是有洞察力的观察，建议在理论部分形式化
- Practitioner guidance 基于仅两个环境，generalizability 注明

### Section 7 (Conclusion)
- "~80.9% of gradient updates carry incorrect sign" 缺少 "for locally correct actions" qualifier

### Limitations
- 位置正确（conclusion 后 references 前），仅一个 section，符合 EMNLP 规定
- 覆盖面适当
- 建议补充：理论分析仅适用于 binary reward 的局限性

### Appendix
- A.3 (Why Defaults) 有独立价值但 Factor 3 措辞可更中性
- A.4 (Classical Connection) 缺少 COMA/QMIX 引用
- Page 12 有严重排版空白问题（LaTeX float）
