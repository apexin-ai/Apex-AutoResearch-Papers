---
round: 13
review_mode: fresh
overall_score: 3.0 (Findings)
timestamp: 2026-05-20T06:13:49.863527+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告 — Round 14 (Fresh Review)

**论文**: Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs
**Venue**: EMNLP 2026 (ARR May 2026)
**Reviewers**: R1 (方法严谨性+实验), R2 (新颖性+完整性)
**轮次**: Round 14, 1 轮交叉分享后收敛

---

## Summary

本文研究用 KL 散度替代 BCE 训练 SwiGLU LLM 的上下文稀疏预测器。在 LLaMA-3.1-8B 上，KL predictor 在 30% sparsity 下将 TEAL 的 perplexity 降低 19%（10.82→8.81），发现与 magnitude mask 偏离 46-68% 的 mask pattern。Target-swap ablation (C1) 证明 mask 质量而非梯度耦合本身驱动推理阶段质量。但 PPL 改善未一致转化为下游增益（MMLU 反而低于 TEAL 5.2pp），方法新颖性有限（KL+Gumbel 框架已被 MaskLLM 使用），且无实际推理加速。

---

## Strengths

1. **C1 target-swap ablation 设计精巧**（R1-S1, R2 Summary）：3-seed 跨 30%/50% 系统性解耦 mask 质量与梯度耦合，实验设计超越常规消融，是论文最强贡献。
2. **系统性消融覆盖全面**（R1-S2）：KL/JSD/RKL divergence direction、Gumbel/STE relaxation、penalty controller、bottleneck dim、temperature、training steps——每个设计选择都有对应消融。
3. **二维 taxonomy 有概念贡献**（R1-S3）：Correction Granularity × Training Signal Coupling 的分类框架清晰定位了 Per-token × Coupled 的空缺，有助于后续工作定位。
4. **诚实透明的局限性讨论**（R1-S4）：明确承认无加速、14B GSM8K −20pp、PPL ≠ 下游能力，Limitations section 质量高于平均水平。
5. **SNR 反直觉洞见**（R1-S5）：KL 梯度更嘈杂（2.3× lower SNR）但产生更好的 mask，说明 target alignment > gradient quality。
6. **可复现性高**（R2 Reproducibility 4/5）：超参数完整、单 GPU 训练、3-seed 核心结果。

---

## Weaknesses

### Must-Fix（全体共识）

**W1. [CRITICAL] PPL 改善未一致转化为下游增益，叙事以 PPL 为中心** [R1-N1 + R2-W1, FULL CONSENSUS]
- Table 2 at 30%: KL uniform MMLU=40.7 vs TEAL=45.86 (−5.2pp); 14B: MMLU −8pp (global), GSM8K −20pp (uniform)
- KL 在 ARC (+4.4pp), WG (+3.9pp), HellaSwag (+7.8pp), PIQA (+2.2pp) 上优于 TEAL——存在 task-type 差异
- Abstract "moderate downstream degradation" 低估了 MMLU 的系统性退化
- 论文需要按 task type（knowledge-intensive vs commonsense）区分叙事，而非笼统称 "moderate"
- 根本问题：为何 mass-covering KL 在 PPL 上更好但牺牲 MMLU？这可能是 forward KL 的固有 tradeoff，但论文未分析机制

**W2. [CRITICAL] MSE baseline 训练配置不透明，"coupling alignment" 实验基础被削弱** [R1-N2, R2 cross-response AGREE]
- MSE at 50% yields PPL 229.26（catastrophic），但训练配置未报告：是否使用 Gumbel-Sigmoid？稀疏度如何控制？超参数是否独立调优？
- 如果 MSE 训练不公平（如缺乏 proper sparsity control），则 "per-layer coupling fails" 的结论不可靠
- "Coupling alignment" 作为论文核心贡献之一，其实验基础需要透明化
- R1 建议 per-layer KL baseline 作为更纯粹的 intermediate coupling 对比——这比 MSE 更 controlled（同 divergence family, 不同 coupling level）

### Should-Fix

**W3. [DIVERGENCE] 与 MaskLLM 新颖性区分** [R2-W3 Must-Fix, R1 REBUT]
- R2：MaskLLM (NeurIPS 2024) 已使用 frozen weights + learnable masks + KL + Gumbel，核心思想已发表
- R1 反驳：三个维度的区分已在 §2 充分讨论（sparsity type / mask generation / allocation mechanism）。Activation sparsity 需要 predictor generalization to unseen inputs，这与 MaskLLM 的直接参数优化根本不同
- **Director 判断**：§2 的区分合理但不够突出。论文应在 Introduction 或 §2 开头明确总结"什么不能从 weight sparsity 直接迁移"——particularly 为何 predictor-based dynamic masking + global allocation 使 coupling 的意义不同于 MaskLLM 的固定 N:M 组内优化

**W4. 跨架构/跨规模 claim 证据不足** [R1-N4 + R2-W2, FULL CONSENSUS]
- Mistral-7B: 单 seed, 无 std
- Qwen-14B: 单 seed (global), 3-seed (uniform) 但 GSM8K σ=5.2pp
- Introduction "cross-architecture evaluation confirms the pattern" 与 Abstract "Preliminary single-seed evaluation" 不一致
- 不应作为核心贡献列出

**W5. "Coupling alignment" 缺乏形式化定义** [R2-W5, R1 部分 AGREE]
- 本质定义接近 "use the right objective" 的同义反复
- 实验证据非平凡（MSE fail + SNR paradox + C1 transfer），但缺乏可检验预测
- 需要操作性定义或至少讨论边界条件

**W6. Conclusion 仅 3 句 + \vspace{-18pt}** [R1-Minor + R2-W6, FULL CONSENSUS]
- 空间操纵是 format red flag，审稿人会注意到
- Long paper 的 Conclusion 应包含核心发现总结 + 局限性精华 + future work

**W7. BCE+Gumbel (32.22) 比标准 BCE (27.97) 更差，缺乏解释** [R1-W1, R2 部分 AGREE]
- C1 ablation 部分化解了 Gumbel×KL 交互的担忧（mask 可转移到 plain BCE）
- 但 Gumbel 为何对 BCE 有害仍需解释——可能是 sparsity gap (38.3% vs 50%) 或 Gumbel noise 与 per-neuron BCE 的冲突

**W8. 30% 实际稀疏度偏差，headline "19%" 在 matched sparsity 下约 14.5%** [R1-N3, R2 REBUT]
- Appendix C 已分析（matched-sparsity TEAL PPL=10.30, 差异 0.67 可忽略）
- 但正文 headline 应注明 matched-sparsity 改善

### Minor

**W9.** 训练数据仅 ~8M tokens，C4 OOD gap (1.74× vs 1.46×) 显著，但 Limitations 已透明报告 [R2-W7]
**W10.** 无实际推理加速，6.4% overhead [R2-W4]——已在 §1 + Appendix A 明确说明，定位合理
**W11.** Missing references: ActTail (2026, arXiv:2603.12272) 需验证; 另 2 篇需验证真实性 [R2]

---

## Reviewer Consensus

| 问题 | R1 | R2 | 状态 |
|------|----|----|------|
| PPL-downstream 脱节 | N1 Must-Fix | W1 Must-Fix | ✅ AGREE |
| MSE baseline 公平性 | N2 Must-Fix | Cross-response AGREE | ✅ AGREE |
| 跨架构 claim 过强 | N4 Should-Fix | W2 Must-Fix | ✅ AGREE (severity differs) |
| Conclusion 过短 | Minor | W6 Should-Fix | ✅ AGREE |
| 无实际加速 | — | W4 Should-Fix | ✅ AGREE (定位合理) |

## Reviewer Divergence

| 问题 | R1 | R2 |
|------|----|----|
| MaskLLM 新颖性 | REBUT (§2 三维度区分充分) | W3 Must-Fix (核心思想已发表) |

---

## Questions（需作者澄清）

1. MSE 的具体训练配置？使用 Gumbel-Sigmoid 还是 STE？稀疏度控制方式？超参数调优程度？
2. KL 为何在 MMLU 上系统性低于 TEAL？mass-covering 是否以牺牲 knowledge-intensive 路径为代价保持 output 广度？是否有 per-layer analysis 支持？
3. BCE+Gumbel+Penalty 是否成功控制到目标 50% 稀疏度？如果实际稀疏度偏离，Table 4 的比较可能不公平。
4. 是否考虑过 per-layer KL（intermediate coupling + same divergence family）作为更 controlled 的 MSE 替代？
5. C1 ablation at 50% 能否补充 3-seed 以匹配 30% 的统计强度？

---

## Missing References

1. **ActTail (2026, arXiv:2603.12272)** — 需验证。如讨论 global activation sparsity allocation，与 §4.6 直接相关。
2. **"A Sparsity Predicting Approach via Activation Pattern Clustering" (2025)** — 需验证真实性。
3. **"Universal Properties of Activation Sparsity in Modern LLMs" (2025)** — 需验证真实性。

---

## External Review (Stanford Agentic Reviewer)

**状态：pending**（已于 2026-05-20T05:57 发送请求，8 小时后自动提醒）。本报告不等待外部审稿结果。如后续返回，将单独转发。

---

## Visual Layout Check（非评分项）

**状态：done** (耗时 ~3 分钟)

| Severity | Finding |
|----------|---------|
| **CRITICAL** | Page 14 (Appendix): Figure 3 包含占位符文本 "[Placeholder: layernorm_dynamics.pdf] Awaiting sync from remote server"，未替换为实际图表。审稿人打开 appendix 会立即看到未完成稿件。 |
| WARNING | Pages 1-4 连续纯文本（含公式但无 figure/table），审稿人前 4 页无视觉锚点 |
| WARNING | Figure 1 (Method overview) 在 p3 引用但 p5 才出现，float 漂移 2 页 |
| WARNING | Figure 1 与 Table 1 挤在 p5 顶部，Figure 1 尺寸偏小 |
| WARNING | Page 17 最后一页有约 1/3 空白，内容利用率 <50% |
| info | Display items 集中在 pages 5-8 (0.88/页)，前半部分完全空白 |
| info | Table 2-4 格式一致，booktabs 风格，排版规范 |
| info | Figure 2 (sparsity sweep) 清晰可读 |

**紧急处理**：占位符 Figure 必须在提交前替换或删除。

---

## Overall Assessment

**评分：3.0 (Findings)**
**置信度：4/5**

### 理由

**支持 Findings (3.0) 而非 Conference (3.5+) 的因素：**
1. PPL-downstream 脱节是根本性叙事问题——论文的核心 claim "KL discovers better masks" 需要限定为 "better for PPL"，而 MMLU（最重要的知识基准）上 TEAL 一致性地优于 KL
2. 方法新颖性有限：KL+Gumbel for mask training 的核心框架已在 MaskLLM (NeurIPS 2024) 发表；本文的增量是 activation sparsity + predictor-based + global allocation 的特定组合下的实证研究
3. MSE baseline 的训练公平性未被验证——"coupling alignment" 作为核心贡献之一，其实验基础不够 robust
4. 无实际推理加速（+6.4% overhead），作为 activation sparsity 工作缺乏实际部署价值

**支持不低于 Findings (3.0) 的因素：**
1. C1 target-swap ablation 是高质量的实验设计，提供了 "mask quality vs gradient coupling" 的精巧解耦
2. 系统性消融覆盖（10+ 变量）远超平均论文
3. 二维 taxonomy 有概念贡献
4. SNR 反直觉洞见（noisier gradient → better masks）有启发性
5. 实验执行质量高、可复现性好
6. Limitations 讨论诚实透明

**R1 (3.5) vs R2 (3.0) 分歧调和：**
核心分歧在 MaskLLM 新颖性。R1 认为三维度区分充分（问题设置根本不同），R2 认为核心思想已发表（增量不足）。Director 判断：§2 的区分在技术上合理，但论文未充分阐述"为什么这些差异使得 activation sparsity 场景下的实证研究有独立价值"。当前版本偏向 Findings。

**提升至 3.5 的条件：**
- 解决 W1：按 task type 重构叙事，提供 MMLU 退化的机制分析
- 解决 W2：报告 MSE 完整配置 + 可选 per-layer KL baseline
- 加强 MaskLLM 区分：总结"什么不能从 weight sparsity 迁移"

---

## Detailed Comments

### Abstract
- "moderate downstream degradation" 不准确——MMLU 低于 TEAL 5.2pp，应明确说明
- "renders post-hoc compensation redundant" 合理
- "46-68% divergence (depending on sparsity level)" 准确

### Introduction
- "cross-architecture evaluation confirms the pattern" 与 Abstract "Preliminary single-seed" 矛盾，需对齐
- Contribution list 第 4 点 (allocation analysis) 的 "non-monotonic allocation preference" 是有趣发现但证据仅来自单模型
- 明确 "empirical study" 定位是正确的做法

### Method (§3)
- KL 公式推导正确，Gumbel-Sigmoid relaxation 标准
- 梯度分析 (§3.6) 逻辑自洽——"coupled gradient as search mechanism" 的叙事与 C1 结果一致
- Adaptive penalty controller 设计合理，Appendix C 的收敛分析完整
- Taxonomy (Table 1)：MSE 归入 "Intermediate" 合理但需要实验公平性支撑

### Experiments (§4)
- Table 2 数值内部一致，正文引用与表格匹配
- C1 ablation (Table 3)：3-seed at 30% 强，50% 仅 s42——统计强度不对等
- Table 4 消融覆盖充分
- §4.6 Sparsity Scaling: Figure 2 + Table 5 呈现清晰
- Cross-architecture (§4.6 末尾)：Mistral 单 seed + Qwen 退化严重，不应与主实验等量齐观

### Related Work (§2)
- 覆盖全面（47 citations），MaskLLM 三维度区分在技术上准确
- 缺少 ActTail (2026) 等可能相关的最新工作（待验证）

### Conclusion
- 仅 3 行 + vspace{-18pt}，需要扩展。至少应包含：核心发现（1-2句）、practical implication（消除 compensation network）、key limitation（PPL ≠ downstream）、future work（per-layer KL、N:M sparsity、scaling to 70B）

### Limitations
- 质量高于平均水平，诚实讨论了 PPL-downstream disconnect、GSM8K reversal、OOD gap、scale limitations

### Format
- **CRITICAL**: Appendix 占位符 figure 必须处理
- Figure 1 漂移 2 页需修复
- 正文 8 页限制内（含 Limitations + Ethics 不计页数）