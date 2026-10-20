---
round: 1
overall_score: weak reject
timestamp: 2026-05-15T07:24:13.017243+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告 — Round 1

**论文**: "When Does Error Injection Help LLM Agents? Boundary Conditions from a Failed Transfer to Embodied Planning"
**目标 Venue**: Insights from Negative Results in NLP @ EMNLP 2026
**审稿模式**: 2 Reviewer 圆桌，1 轮独立审稿 + 交叉回应，1 轮收敛
**收敛状态**: 关键问题高度共识，无需 Round 2

---

## Summary

本文测试 taxonomy-guided error injection（TaxEI）从 tool-use（PALADIN）向 embodied planning（ALFWorld）的迁移。在 Qwen3-8B 上对比 Vanilla/TaxEI/Random 三条件（3 seeds），发现 TaxEI 无改善（−8.6pp, p=0.054）。论文提出三个 boundary conditions：variance gradient、dose-response threshold、per-operator local/global split。论文定位为 negative result paper，目标 venue 为 EMNLP 2026 Negative Results Workshop。

---

## Strengths

1. **选题精准，venue 匹配度高**：跨域迁移测试是自然的下一步，负面结果避免社区重复尝试。[R1, R2 共识]
2. **实验透明诚实**：Limitations 坦承几乎所有统计弱点，Version Discrepancy（Appendix D）透明披露，v3→v4 数据问题不隐瞒。[R1, R2 共识]
3. **超越简单报告失败**：dose-response、per-operator 分析和 structural comparison（Table 3）生成可检验假说。[R1]
4. **整体实验框架合理**：三条件 + 多 seed + dose-response 消融 + recovery eval 的设计逻辑完整。[R1]
5. **写作清晰流畅**：叙事有条理，实验细节充分（超参完整：LoRA rank 16, α=32, lr 1e-4, 3 epochs, bf16）。[R2]

---

## Weaknesses

### Must-Fix（影响接收决定）

**[MF-1] Recovery-pairing confound 使核心 "迁移失败" 结论不可靠** [R1-N3, R2-N2 | 双方最强共识]
- PALADIN = taxonomy tagging + recovery pairing + retrieval augmentation（~30pp 增益来自 retrieval）。TaxEI 仅复现了 taxonomy tagging。
- "迁移失败"无法区分：(a) error injection 在 embodied planning 本身无效 vs (b) 缺少 recovery pairing 导致失败。
- §5.2 承认了这点，但 Title/Abstract/Introduction/Conclusion 的 framing 暗示 (a)。
- **必须修改**：framing 明确限定为 "unpaired error injection" 的迁移测试；将 confound 从 Discussion 提升至 Introduction；两个竞争假说（task structure vs recovery pairing）并列为等权重解释。

**[MF-2] Variance gradient 作为 boundary condition 无统计支撑** [R1-N2 | R2 强烈同意]
- 三组 SD=3.3/7.0/8.6pp，每组仅 n=3。所有检验均 NS（Levene's p=0.085, F-test p=0.252, bootstrap P=69%）。
- n=3 估 SD 的 95% CI 极宽（SD=3.3 → CI≈[1.9, 12.6]；SD=8.6 → CI≈[4.9, 33.0]），大幅重叠。
- 将统计上完全不支持的 pattern 列为论文第一个 boundary condition，违反 soundness 标准。
- **必须修改**：从 boundary conditions 列表中移除或降级为"方向性观察"，不在 Abstract 中以 claim 形式出现。

**[MF-3] 数据量混淆与统计功效不足并存** [R1-N1 | R2 同意]
- 主表（Table 1）：TaxEI/Random 9,029 vs Vanilla 4,358（2.1×），有数据量混淆。
- 控制数据量的 dose-response 消融（Table 2）更公平，但仅用 seed=42（TaxEI 表现最好的 seed），可能系统性高估。
- 三个 boundary conditions 的证据基础全部建立在 underpowered 设计上。
- **必须修改**：(1) 将 Table 1 明确定位为"保守估计——TaxEI 即使多出 2.1× 数据仍更差"，把混淆转化为论证优势；(2) dose-response 补充 seeds 或明确标记为 preliminary；(3) 降低 claim 强度。

**[MF-4] 主体文本超 4 页限制** [R2-N1, R1-W4 | 双方同意]
- PDF 确认 Conclusion 结束于 page 5 上半部，主体约 4.3–4.5 页。
- Insights workshop 短文 ≤ 4 pages excluding references，硬性格式违规。
- **必须修改**：大幅精简 Related Work（当前约 0.8 页），或将部分 Discussion 移至 Appendix。

**[MF-5] PALADIN +57pp 归因不准确** [R2-N3, R1-W3 | 双方同意，R2 坚持 must-fix 级别]
- Abstract 第一句将 +57pp 归因于 error injection，但这是 PALADIN 完整系统增益（含 retrieval ~30pp）。
- 误导读者高估 error injection alone 的效果，扭曲论文出发点。
- **必须修改**：首次提及时拆分增益来源，区分 taxonomy injection 和 retrieval augmentation 的贡献。

### Should-Fix

**[SF-1] Per-operator local/global split 粒度过粗** [R1-W1 | R2 同意]
- N=11-12 per operator，单 seed，±1 task ≈ ±8-9pp。C4 的 +9.1pp 实际仅 +1 task。
- "Binary split" 措辞过强，可能是随机波动。
- 应报告 exact task count（如 "7/11 vs 6/11"），降级为 hypothesis-generating observation。

**[SF-2] Training-evaluation paradox 缺替代假说** [R1-W2 | R2 部分反驳]
- 论文归因于 memorization，但 distribution shift 是更简单的竞争解释。
- R2 指出 10% 的非线性行为部分支持 memorization，但共识是应讨论两种解释。
- 在 §4.2 中增加 distribution shift 作为 competing explanation。

**[SF-3] Boundary conditions 新颖性有限** [R2-W1 | R1 部分反驳]
- Variance gradient："加噪声增加不稳定性"可预期，无新颖性。[共识]
- Dose-response threshold：R1 指出与 Rolnick 2017（vision 对 massive noise robust）的对比有新意。[分歧]
- Local/global split：接近 error locality 的定义性属性，但实证量化有增量贡献。[部分共识]
- 建议 frame 为"经验验证"而非"新发现"。

**[SF-4] AgentDebug 重叠讨论不足** [R2-W2 | R1 同意]
- AgentDebug 在 ALFWorld 提出 5 维 error taxonomy 且发现 error cascading 是主要瓶颈，与 §3.5 C1 cascading 直接重叠。
- §6 仅一句话提及，需详细对比两套 taxonomy 和 cascading 发现。

**[SF-5] 单 seed 消融可靠性不足** [R2-W3 | R1 同意]
- Dose-response（Table 2）和 per-operator（Figure 2）均仅 seed=42。
- 主实验 TaxEI 的 seed 间方差极大（s0=46.8% vs s42/s123=61.7%），单 seed 结论可靠性存疑。

**[SF-6] Related Work 缺 ALFWorld training-time 方法对比** [R2-W4 | R1 同意]
- §6 "ALFWorld methods" 段列出的几乎全是 inference-time 方法，缺 training-time 对比。

**[SF-7] Title/claim scope vs 实际实验** [R2-W5 | R1 部分反驳]
- "Embodied Planning" 但仅测 ALFWorld（text-based interface）。
- R1 指出 ALFWorld 原论文标题即含 "Embodied"，用词符合文献惯例。但 text-based 接口使 errors 相对 discrete（如 "Nothing happens"），反而削弱论文 "errors 不够 discrete" 的论证。
- 建议在 Limitations 中讨论 text-based vs vision-based 区别。

**[SF-8] 缺少其他数据增强方法对比** [R1-W5 | R2 同意]
- 无法区分 "error injection 没帮助" 和 "任何 off-distribution augmentation 在小数据 SFT 下都 harmful"。
- 应在 Discussion 中承认此限制。

---

## Reviewer Consensus [AGREE]

以下问题双方完全一致：
1. Recovery-pairing confound 是论文最根本的 framing 问题
2. Variance gradient 不应作为 boundary condition（统计完全不支持）
3. 主体文本超页数限制，需压缩
4. PALADIN +57pp 数字需准确归因
5. Per-operator 分析应报告 exact task count
6. AgentDebug 需更深入讨论
7. Abstract "no improvement" → "no statistically significant improvement"
8. 0% error detection rate 值得更突出讨论

## Reviewer Divergence [分歧]

1. **+57pp 和页数超限的严重性**：R2 列 must-fix，R1 初始列 should-fix（交叉后 AGREE）。**裁定：must-fix**——workshop 页数限制是硬约束，+57pp 影响 framing 基础。
2. **Training-evaluation paradox 解释**：R1 偏 distribution shift，R2 偏 memorization（10% 非线性为证据）。**裁定**：两种解释可共存，论文应并列讨论。
3. **Dose-response threshold 新颖性**：R2 认为已知，R1 认为与 Rolnick 2017 的 vision 对比有新意。**裁定**：R1 论证更具说服力——不同 domain 的对比确有增量贡献，但应明确标记为经验验证。
4. **Title "Embodied Planning"**：R2 认为 scope 过宽，R1 认为符合文献惯例。**裁定**：Title 可保留，但需在 Limitations 讨论 text-based vs vision-based 区别。

---

## Questions（需作者澄清）

1. §5.2 估计 PALADIN retrieval 贡献约 30pp，此数字来源？论文未引用 PALADIN 消融实验。
2. 如果 error injection without recovery pairing 在 tool-use 上也不 work，boundary conditions 框架是否成立？
3. Dose-response 消融为何选择 seed=42 而非 3-seed？是资源限制还是设计选择？
4. 0% error detection rate 是否意味着 taxonomy labels 完全未被模型学到？这对 TaxEI 的机制假说有何影响？

---

## Missing References

1. **AgentDebug** (Zhu et al., 2025) 需更深入讨论——5 维 error taxonomy + error cascading 发现直接相关
2. ALFWorld 上的 training-time 数据增强方法（如有）
3. Embodied AI 中的 adversarial training / error injection 工作
4. Negative results 方法论文献中的 methodological precedents

---

## External Review (Stanford Agentic Reviewer)

外部审稿未启用（项目配置中 `external_review.paperreview_ai.enabled` 未设置）。

---

## Overall Assessment

**评分: Weak Reject (偏向 Borderline)**
**置信度: High (4/5)**

**核心判断**：论文选题有价值、实验透明诚实，适合 Negative Results Workshop。但存在一个根本性 framing 缺陷（recovery-pairing confound 使 "迁移失败" 归因不可靠）和多个统计功效问题（variance gradient 无支撑、单 seed 消融、per-operator N 过小）。三个 boundary conditions 中，仅 dose-response threshold 有一定新颖性和可靠性。

**修改后可接收的条件**：
1. 修正 framing：限定为 "unpaired error injection" 的迁移测试，两个竞争假说并列
2. 降级 variance gradient 为方向性观察，从 boundary conditions 主列表移除
3. 降低所有 claim 强度，与证据水平匹配
4. 压缩至 ≤ 4 页
5. 准确归因 PALADIN +57pp

修改难度中等，不涉及补充实验（虽然补充 seeds 会显著加强论文）。预计 1 轮修改后可达 borderline accept。

**Reviewer 评分汇总**：
- Reviewer 1: Overall 3/5, Soundness 2.5/5, Excitement 3/5
- Reviewer 2: Overall 2.5/5, Soundness 2.5/5, Excitement 3/5
- **综合**: Weak Reject (2.75/5)

---

## Detailed Comments

### §1 Introduction
- 第一句 +57pp 需拆分归因（MF-5）
- "variance gradient" 作为第一个 boundary condition 前置需降级（MF-2）

### §2 Method
- Error taxonomy 设计合理，但 local/global 分类需更强理论依据
- "Error-recovery pairs are not explicitly paired"——这是与 PALADIN 的关键差异，应在此处（而非仅 §5.2）强调

### §3 Experiments
- Table 1: 添加脚注明确 2.1× 数据量差异的论证逻辑（MF-3）
- Table 2: 标注 "single seed, preliminary"（SF-5）
- §3.1: "no improvement" → "no statistically significant improvement"
- §3.4: 0% detection rate 值得独立段落讨论
- §3.5: 报告 exact task count，如 "C4: 7/11 (TaxEI) vs 6/11 (Vanilla)"（SF-1）
- Figure 2: 增加 "Exploratory, single seed" 标注醒目度

### §4 Discussion（原 §5）
- §5.1: 结构假说应与 recovery-pairing 假说并列
- §5.2: Recovery-pairing confound 应提升至 Introduction
- §5.3: 增加 text-based vs vision-based ALFWorld 的讨论（SF-7）

### §6 Related Work
- AgentDebug: 扩展讨论，对比两套 taxonomy（SF-4）
- ALFWorld: 补充 training-time 方法（SF-6）
- 此 section 是压缩页数的主要候选

### Appendix
- Table 3 (structural comparison) 有用，可保留
- Training dynamics 和 per-task analysis 支撑主文 claims