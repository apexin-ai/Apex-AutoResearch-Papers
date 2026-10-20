---
round: 0
overall_score: weak reject
timestamp: 2026-05-16T17:15:50.305194+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---


# 审稿报告 — ContamCal: Post-Hoc Calibration of Benchmark Scores under Training Data Contamination via Contamination-Augmented Item Response Theory

**项目**: contamcal-irt-calibration
**Venue**: EMNLP 2026 ARR May 25
**轮次**: Round 1
**日期**: 2026-05-16
**Reviewer 编排**: 2 名（R1: 方法严谨性/实验设计；R2: 新颖性/Related Work/完整性）

---

## Summary

论文提出 ContamCal，一个基于 contamination-augmented 4PL IRT 的框架，旨在对受污染 LLM benchmark 分数进行事后校准。核心技术是在标准 IRT 模型中加入 per-benchmark 污染效应参数 γ_k，通过 Stage 1 多信号检测融合估计逐项暴露分数，Stage 2 Bayesian IRT 推断校准分数。论文最终从校准工具转向诊断框架定位，报告了多个负面结果及诊断发现。

---

## Strengths

**S1. Min-K++ 方向逆转发现具有独立价值** [R1, R2 共识]
Cohen's d = -1.55 到 -1.98 的效应量极大，且跨 Qwen 和 Llama 家族复制。对 contamination detection 社区有直接实践意义——大量研究假设 Min-K++ score 越高 = 越可能污染，方向逆转直接挑战这一假设。两位 Reviewer 均认为这可能是论文最有价值的贡献。

**S2. 诚实报告负面结果的科学态度** [R1]
论文坦率承认校准失败，将 ContamCal 从校准工具重新定位为诊断框架。Section 4.3 的 "Honest downgrade" 和 Section 5.5 的 Limitations 展示了值得赞赏的学术诚实。

**S3. Calibration gating criterion 是有用的方法论贡献** [R1, R2 共识]
三条件门控（γ CI 排除零、PPP 合理范围、校准 MAE < raw MAE）简单可操作。"知道何时不该校准"对后续研究者有实际价值。

**S4. 控制 SFT 实验设计严谨** [R1]
多剂量级别（d000-d100）、3 seeds、QC 过滤、position bias 监控，展示了对实验混淆变量的深思熟虑。

**S5. 问题定位合理** [R2]
从 contamination detection 推进到 calibration/correction 是文献中的自然缺口。将教育测量 item compromise 文献迁移到 LLM benchmark contamination 是有意义的跨领域类比。

---

## Weaknesses（重点）

### Critical（影响接收决定）

**C1. 跨尺度核心主张缺失 1.5B/3B 实验数据** [R1-N1, R2 AGREE]
论文声称覆盖四个尺度（0.5B/1.5B/3B/7B），但 Table 1 仅展示 0.5B，Table 2 仅展示 7B。"污染效应随尺度单调衰减"是论文核心叙事，但单调性至少需要三个数据点。缺少中间尺度让核心主张变成不可证伪的两点连线。R2 补充：中间尺度可能恰好处于 IRT information function 最高效区域，遗漏了最有信息量的观测。

**C2. 跨家族验证统计力严重不足** [R1-N2, R2 AGREE]
Llama-3.2-3B 仅 3 个剂量级别（N=3），所有 γ CI 包含零，所有 Kendall τ 非显著（p > 0.55）。论文从中推导 "provably infeasible" 结论。R2 指出：N=3 时 γ posterior 几乎完全由 prior 主导，CI 包含零仅表明数据对 prior 无更新——这是经典的 absence of evidence ≠ evidence of absence 错误。论文需要 post-hoc power analysis 并将结论标注为 inconclusive。

**C3. 三重不可能性结论过度泛化** [R1-N3, R2 AGREE with stronger arguments]
"三重不可能性"（开放权重、N≥50、容量混淆）绑定在 IRT + membership inference 这一特定方法组合上，但论文声称为领域层面的结构性限制。R2 从 related work 视角提供更强论据：
- DCR (Li et al., EMNLP 2025) 的存在直接构成反例——它在不需要 IRT、不需要开放权重的条件下实现了某种程度的 decontaminated calibration
- 能力-污染混淆是 causal identification 问题，文献中有 IV/RDD/DiD 等方法可能打破 confounding，论文未讨论
- DIF 文献 (Holland & Wainer 1993) 对 "item compromise 效应何时可估计" 有严格理论分析（anchor item 策略等），论文未对比

### Warning（影响评分但不一票否决）

**W1. 与 DCR 差异化不足** [R2-W1, R1 AGREE]
DCR 与 ContamCal problem framing 高度重叠。论文仅用一句话处理 DCR。R1 识别出三个方法论差异（UQ/逐项检测/IRT框架），但论文缺少 head-to-head 实证对比。论文标题以 "calibration" 立题放大了与 DCR 的对比压力。

**W2. 叙事 pivot 缺乏说服力** [R2-W3, R1 AGREE]
Introduction 以 "post-hoc calibration" 立题，后承认校准失败转向 "diagnostic framework"。R1 指出如果以诊断/不可能性立题（如 "On the Identifiability Limits of Contamination Calibration"），叙事会更自然。当前 "先承诺校准→承认失败→声称失败就是贡献" 的结构有事后合理化之嫌。

**W3. 核心 IRT 建模技术增量有限** [R2-W5, R1 PARTIALLY AGREE]
向 4PL IRT 加 γ_k·ε_{ij} 协变量是 Explanatory IRT (De Boeck & Wilson 2004) 的标准操作。两位 Reviewer 达成共识：论文价值在实证发现（Min-K++ 逆转、identifiability boundary、gating criterion）而非建模创新。但这意味着实验证据链必须完整——回到 C1。

**W4. Fisher Information 模拟缺乏可验证性** [R1-W2, R2 AGREE]
N≥50 identifiability boundary 和 CI width ∝ N^{-0.48} scaling law 仅文字描述，无图表。建议增加 N × AUC 热力图或 information matrix 可视化。

**W5. 观测实验推理过度** [R1-W3, R2 AGREE with qualification]
Exp 4（RL/Instruct）和 Exp 5（72B）无地面真值。γ 估计反映的是 "与 Min-K++ signal 相关的性能变异"，不等同于真实污染效应。R2 认为严重性略低——观测实验有 ecological validity 价值，标注 associational 即可。

**W6. SFT ≠ 真实污染 gap 可能被低估** [R1-W4, R2 AGREE]
SFT 是集中式高强度注入；真实污染是 pretraining 中的分布式 incidental exposure。核心发现（小模型灾难性遗忘、position bias 放大）可能是 SFT artifact。R2 补充：SFT 可能产生 format-specific overfitting 在自然污染中未必出现。

**W7. Table 2 标题 misleading** [R1-W1, R2 AGREE]
标题 "across model scales" 实际只展示 7B。

---

## Reviewer Consensus [AGREE]

所有关键问题均达成共识：

| Issue | R1 | R2 | 共识 |
|-------|----|----|------|
| C1 缺失 1.5B/3B 数据 | 首次提出 | AGREE + 补充 | ✅ 核心证据链断裂 |
| C2 跨家族 N=3 不足 | 首次提出 | AGREE + 补充 | ✅ absence ≠ evidence |
| C3 不可能性过度泛化 | 首次提出 | AGREE + 更强论据 | ✅ DCR 构成反例 |
| W1 DCR 差异化 | AGREE | 首次提出 | ✅ 需 head-to-head |
| W2 叙事 pivot | AGREE | 首次提出 | ✅ 考虑改标题 |
| W3 技术增量 | PARTIALLY AGREE | 首次提出 | ✅ 价值在实证非建模 |
| Min-K++ 逆转有独立价值 | 首次提出 | AGREE | ✅ 论文最强贡献 |

---

## Reviewer Divergence [REBUT]

**仅一处分歧，已解决**：

| Issue | R2 立场 | R1 回应 | 解决 |
|-------|---------|---------|------|
| eckerly2017 引用可验证性 | OpenAlex 未收录，怀疑真实性 | REBUT: 确认为 University of Iowa PhD thesis，ProQuest 可获取 | ✅ 数据库收录问题，非虚假引用 |

**评分差异**：
- R1: 3/6 (Borderline Reject)；Novelty 4/6
- R2: 2/5 修正后 (Resubmit next cycle)；Novelty 建议 3/6-3.5/6
- R2 认为 R1 的 Novelty 4/6 偏高，主要因 DCR 重叠和技术增量有限。R1 在交叉回应中承认 DCR 区分不足。

---

## Questions（需要作者澄清）

1. 1.5B/3B 的完整剂量-效应数据是否存在？如果存在，为什么没有在论文中展示？
2. 论文引用的 DCR 是 Oren et al. (2024, ICLR) 还是 Li et al. (2025, EMNLP)？如果存在 DCR 2025 版本，是否已做对比？
3. Section 4.6 "Triple impossibility" 的三条约束中，哪些在非 IRT 框架下仍然成立？作者是否有理论论证？
4. Min-K++ 逆转的因果机制是什么？是 benchmark format 依赖（MC vs. generative）、模型容量交互、还是 SFT-specific artifact？
5. 72B 加入后 coverage 从 0.35 降到 0.32 的反直觉现象的解释？

---

## Missing References

1. **Li et al. (2025), "Decontaminated Calibration and Ranking for Benchmark Evaluation", EMNLP 2025** — 与 ContamCal 目标最接近的现有工作，论文中可能引用了旧版本(2024)但未讨论 2025 版本 [R2]
2. **Causal inference 文献**（IV, RDD, DiD）用于处理能力-污染 confounding [R2]
3. **DIF 可辨识性理论**（Holland & Wainer 1993 中的 anchor item 策略条件）——论文引用了 DIF 但未讨论可辨识性条件 [R2]

---

## External Review (Stanford Agentic Reviewer)

**状态**: 未请求。本轮未配置外部审稿。

---

## Overall Assessment

**Overall Score: Weak Reject (Borderline Reject)**
**置信度: High (4/5)**

论文提出了一个方向正确的研究问题（从 contamination detection 推进到 calibration），并通过系统实验发现了有价值的诊断结果（Min-K++ 方向逆转、scale paradox、gating criterion）。诚实报告负面结果的科学态度值得赞赏。

然而，论文存在三个 critical 级别问题：(1) 核心跨尺度主张缺失 1.5B/3B 关键数据，证据链断裂；(2) 跨家族验证统计力严重不足（N=3），从非显著结果推导强结论；(3) 三重不可能性结论将方法特异限制过度泛化为领域层面限制，且被 DCR 的存在直接挑战。

此外，与 DCR 的差异化不足（W1）、从 calibration 到 diagnostic 的叙事 pivot 缺乏说服力（W2）、以及核心建模技术增量有限（W3）进一步削弱了论文的竞争力。

**修改潜力**：如果作者 (1) 补充 1.5B/3B 完整数据修复证据链，(2) 将不可能性结论严格限定为 IRT-specific，(3) 重新定位标题和 Introduction framing，(4) 增加与 DCR 的正式对比，论文有潜力上升至 Weak Accept。核心诊断发现——特别是 Min-K++ 逆转（跨家族复制，大效应量）和 calibration gating criterion——具有独立学术价值。

**⚠️ 流程注意**：本轮审稿中发现磁盘上的 main.pdf 为过期编译版本（Abstract=TODO、实验章节未渲染），导致 R2 初始评分 1/5。提交前必须确保 PDF 完整编译。R2 在了解完整论文内容后修正评分为 2/5。本报告综合评估基于论文的完整内容（R1 审阅版本）。

---

## Detailed Comments（逐节）

### Introduction
- 以 "post-hoc calibration" 立题但最终转向诊断框架，叙事结构需重新考虑 [R1-N3, R2-W3 共识]
- 建议：要么改标题以诊断/限制性立题，要么加强 calibration 成功案例呈现

### Related Work
- related_work.tex 内容完整且质量良好，涵盖检测/缓解/IRT/教育测量四个维度
- 与 DCR 的区分仅一句话，严重不足 [R2-W1, R1 AGREE]
- 缺少 causal inference 方法和 DIF 可辨识性理论的讨论 [R2]

### Method
- 4PL+γ 建模本身合理但技术增量有限（Explanatory IRT 标准操作）[R2-W5, R1 PARTIALLY AGREE]
- Fisher Information analysis 缺乏图表可视化 [R1-W2, R2 AGREE]
- 4PL 参数可辨识性（γ 与 c/d 之间的混淆）未讨论 [R1 minor]

### Experiments (Section 4)
- 控制 SFT 协议严谨（多剂量/多种子/QC）[R1 S4]
- 核心缺陷：1.5B/3B 数据缺失 [C1]
- 跨家族 N=3 严重不足 [C2]
- 观测实验需标注 associational [W5]

### Discussion/Conclusion
- "三重不可能性"需限定 scope [C3]
- SFT vs 真实污染 gap 讨论需深化 [W6]
- Coverage 反直觉现象（72B 加入后下降）需解释 [R1 minor]
