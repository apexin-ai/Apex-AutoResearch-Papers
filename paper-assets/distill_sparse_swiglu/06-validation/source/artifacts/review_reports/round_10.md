---
round: 10
review_mode: fresh
overall_score: 3.0 Findings
timestamp: 2026-05-19T06:44:59.164109+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告 — Round 11 (Fresh Review)

**论文**: Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs
**Venue**: EMNLP 2026 via ARR May 2026 cycle
**Reviewers**: R1 (方法严谨性+实验有效性), R2 (新颖性+写作+格式)
**流程**: Round 1 独立审稿 → 交叉分享 + 逐条回应 → 收敛汇总

---

## Summary

本文提出用 forward KL divergence + Gumbel-Sigmoid 松弛训练轻量 sparsity predictor（75.9M params, <1% of base），替代传统 BCE 目标，用于 SwiGLU LLM 的 activation sparsity 预测。核心发现：KL 训练发现的 mask 与 magnitude-based mask 偏离 68%（per-layer Jaccard 32%），causal ablation (C1) 表明 mask target 质量是 KL 质量优势的主要来源。方法在 LLaMA-3.1-8B 30% sparsity 下 PPL 改善 18%（vs TEAL），消除了 67.2M 参数的 compensation network，并在 Mistral-7B 上泛化（5/6 downstream tasks 胜出）。但 50% sparsity 下 downstream 全面崩溃、14B Qwen 上 MMLU 反转 -8.1pp、无 wall-clock speedup、C1 因果推断存在逻辑缺陷。

---

## Strengths

1. **有洞察力的核心发现**：KL mask 与 magnitude mask 68% 偏离不是显而易见的结果，对 sparsity prediction 文献有分析价值。U-shaped per-layer divergence pattern 提供了可操作的信号。[R1, R2 consensus]

2. **设计精良的 C1 causal ablation**：用 BCE 在 KL-derived targets 训练来分离 target quality 和 training objective，50% 下 max Δ=0.59pp (2-seed)，30% 下 max Δ=1.70pp (3-seed)。实验设计有 genuine intellectual merit。[R1, R2 consensus]

3. **系统化的实验覆盖**：3 架构（LLaMA-8B, Mistral-7B, Qwen-14B），6 个 sparsity 级别（25%-70%），两种 allocation 策略，消融涵盖 divergence 方向/relaxation/compensation/hyperparameter，3-seed 评估覆盖核心实验。[R2]

4. **诚实的 claim 边界**：明确声明 "Our contribution is empirical"，诚实报告 50% downstream collapse、14B 反转、无 speedup、C4 OOD gap 等负面结果。在同类论文中属上游。[R1, R2 consensus]

5. **训练效率高**：单 GPU 45 分钟，1000 步收敛，predictor <1% base model 参数，工程实用性好。[R1]

6. **写作干净无 AI 痕迹**：em-dash 0 处、en-dash 0 处、黑名单词 0 处、过度过渡词 0 处。格式完全合规（ACL [review]、行号、匿名化、Limitations 位置、双栏）。[R2 验证]

7. **引用完整**：46 条引用全部通过交叉验证，无虚构引用，Related Work 6 段覆盖所有主要方向，与 MaskLLM 的三点区分具体且有说服力。[R1, R2 consensus]

---

## Weaknesses

### Must-Fix（影响接收决定）

**N1 [critical, consensus] C1 因果消融推断逻辑有缺陷**
- **因果链断裂**：C1 训练 BCE 在 KL-derived masks 上，匹配 KL 质量。论文推断"target quality, not gradient coupling, drives quality"。但 KL gradient coupling 是 *发现* 这些 superior masks 的必要条件。C1 证明的是 mask transferability（已知好 masks 可迁移到更简单的训练），而非 gradient coupling 在训练阶段不重要。论文的 framing 混淆了 mask discovery 阶段和 inference 阶段。
- **Soft-vs-Hard confound 反常未解释**：BCE + Gumbel-Sigmoid = PPL 38.02，比 vanilla BCE (27.97) 更差。§4.5 给出的解释（"penalty interferes with per-neuron optimization without global coordination"）缺乏实验验证。如果 Gumbel 在 BCE 下有害，KL 的优势可能部分来自 KL loss 与 Gumbel 的特殊协同，而非纯粹的 target quality。
- **建议**：(a) 修正 framing 为 "mask transferability" 而非 "gradient coupling unimportant"，明确区分 training-stage 和 inference-stage 的 coupling 角色；(b) 补充实验：去掉 penalty 只保留 Gumbel 的 BCE 作为控制；(c) 50% C1 增加至 3-seed。

**N2 [critical, consensus] 14B Qwen MMLU 反转未被充分分析**
- Qwen-2.5-14B 上 KL PPL 优于 TEAL (7.62 vs 8.73) 但 MMLU 严重反转 (63.7% vs 71.8%, -8.1pp)。BCE 在 14B 上 MMLU=71.67% 接近 TEAL，说明 KL mask patterns 在大模型上可能系统性损害知识检索任务。
- Contribution #3 声称分析了 "scale-dependent effects at 14B"，但 §4.6 仅用一句话处理 ("warrants further investigation")。这不是可推迟到 future work 的问题——如果方法在最有价值的方向（更大模型）上 downstream 退化，实际可推广性存在根本质疑。
- Abstract "advantages hold on most tasks across architectures" 与数据矛盾。
- **建议**：(a) 分析 14B per-layer mask divergence 与 8B 对比；(b) 检查 14B layer retention 分布；(c) 提供至少一个假说并用已有数据验证/排除；(d) 修正 Abstract 和 Introduction 中的 cross-architecture claims。

**N3 [critical, consensus] 49% PPL headline 来自 downstream 全面崩溃的 regime，framing 有误导性**
- 49% PPL 改善 (11.79 vs 23.31) 来自 50% sparsity，但此 regime 下 MMLU≈28%（近随机）、GSM8K<2.2%。论文自身在 Limitations 承认 "PPL is poor proxy for reasoning ability"。将 49% 放在 Abstract 和 Introduction 最显眼位置，而 30% 的 18% PPL 改善放在次要位置，产生内部矛盾。
- 实际可用操作点是 30%（downstream 保持 86-92% retention），但这个 regime 的改善幅度远不如 headline 宣传的 49%。
- **建议**：以 30% sparsity 为 Abstract/Introduction 的主叙事支撑点，50% 降为分析补充。保留最多 2-3 个关键数字（mask 68% 偏离、30% PPL 18% 改善、compensation 冗余），删除其余。

### Should-Fix（影响评分但不一票否决）

**W1 [warning, consensus] Abstract 数据堆砌**
- ~170 词中 15+ 个数字，读起来像 results 缩写而非独立叙事。审稿人 30 秒内难以判断核心价值。
- R2 评为 Must-Fix，R1 评为 Should-Fix（presentation 非 soundness）。Director 判定为 Should-Fix：实质修复方向是削减 claim 数量（4→2-3），数字自然减少。

**W2 [warning, consensus after correction] 50% KL 3-seed 数据未上浮至主表**
- Table 2 中 50% KL 仅显示 seed 42 (PPL 11.79)，完整 3-seed 数据 (PPL 11.92±0.07, CV<1%) 在 Appendix E。30% BCE baseline 为单 seed。
- R1 初始评为 critical 但描述不准确（30% KL 实际全部 3-seed），R2 用证据纠正。Director 判定 Should-Fix：50% 3-seed 应上浮至主表，30% BCE 应补充 multi-seed。

**W3 [warning, consensus] 无 wall-clock speedup**
- Pipeline 增加 6.4% overhead（126.78 vs 119.11 ms/forward）。论文诚实承认 sparse kernel 不在 scope 内，但作为 sparsity prediction 论文无加速演示是显著弱点。

**W4 [warning, consensus] PPL 局限性未充分反映在实验叙事中**
- Limitations 承认 PPL 是 poor proxy，但 §4.2 main results 叙事仍以 PPL 驱动。与 N3 overlapping。

**W5 [warning, consensus] HellaSwag 和 PIQA 在 Abstract 引用但不在主表**
- Abstract 引用 86.0%/92.5% retention，但 Table 2 仅含 ARC-c、WG、MMLU、GSM8K。如果指标重要到出现在 Abstract，应在主表中。

**W6 [warning, consensus] Table 3 C1 ablation 30% KL 行缺 ARC-c/WG/GSM8K**
- Max Δ=1.70pp claim 基于 MMLU 单一 metric，其他 downstream 可能有更大偏差。C1 作为核心 claim 支撑，比较应完整。

### Minor Issues

**M1** [info] 符号不一致：§3.1 $\mathbf{x}^{(\ell)}$ ("hidden state after attention") vs §3.2 $\mathbf{h}$ ("pre-FFN hidden state")，指代同一量但符号切换。
**M2** [info] KL (Kullback-Leibler)、TEAL、SPON 在首次使用时未展开定义。
**M3** [info] 68% mask divergence 无 bootstrap confidence interval（64 samples, 131K tokens 的均值无 CI）。
**M4** [info] SPON 2.4% PPL 改善 (12.08→11.79) 为单 seed，可能在噪声范围内（3-seed std≈0.07）。论文已 frame 为 "optional, marginal"。
**M5** [info] Table 2 caption 5 行，信息密度过高。
**M6** [info] Penalty controller terminology 不统一（"Adaptive Penalty Sparsity Controller" vs "adaptive penalty controller" vs footnote "resembles augmented Lagrangian"）。
**M7** [info] §3.6 gradient analysis 中 SNR 5.14× 是经验度量，论文定位为 "suggestive" 是恰当的（R1 初始质疑 overclaiming，R2 rebut 指出论文未声称理论证明）。

---

## Reviewer Consensus [AGREE]

以下问题两位 Reviewer 在交叉回应中达成明确共识：

1. **C1 因果推断逻辑有缺陷** [R1-N2, R2-W1→upgraded]：C1 证明 mask transferability，不等于 gradient coupling 在训练阶段不重要。Framing 需修正。
2. **14B MMLU 反转分析不足** [R1-N3, R2-N3]：BCE 14B MMLU=71.67% 接近 TEAL=71.83%，说明 magnitude masks 在大模型上对知识任务更优。需要 mechanism 分析。
3. **49% PPL headline 有误导性** [R2-N2, R1 cross-AGREE]：50% regime downstream 崩溃但 PPL 大幅改善，作为 headline 有内部矛盾。
4. **方法新颖性适合 Findings** [R1, R2 consensus]：KL+Gumbel+MLP predictor 是已有组件的自然组合，无技术 surprise，但 empirical findings 有价值。两位 Reviewer 均评 3.0 (Findings)。
5. **无 wall-clock speedup 是显著弱点** [R1-W2, R2-W2]。
6. **实验诚实度在同类论文中属上游** [R1, R2 consensus]：负面结果均被报告。
7. **写作质量高，格式完全合规** [R2 验证，R1 agree]。

---

## Reviewer Divergence [REBUT]

以下问题两位 Reviewer 存在分歧，经交叉回应后部分解决：

1. **Single-seed 严重性** [R1: Must-Fix → R2 rebut with evidence → Director: Should-Fix]
   - R1 声称 "绝大多数结果 seed 42"，R2 逐条反驳：30% KL 全部 8 个 metric-method 组合均为 3-seed，TEAL 是 deterministic 无需 multi-seed。实际 gap 仅在 50% 主表呈现和 30% BCE baseline。Director 采纳 R2 的纠正，降级为 Should-Fix。

2. **Abstract 数据堆砌严重性** [R2: Must-Fix vs R1: Should-Fix]
   - R2 认为 15+ 数字的 Abstract 无法通过 "30 秒可读性测试"；R1 认为这是 presentation 问题不应与 soundness 并列。Director 采纳 R1 的分级逻辑，判定 Should-Fix。

3. **Three regime 分析** [R1: overfitting 4 points → R2 rebut: 6 points in Appendix]
   - R1 未阅读 Appendix Table 7（6 个 sparsity 级别完整数据），R2 纠正后 R1 未坚持。Director 判定：regime 分析有 6 点数据支撑，不构成独立 weakness。

4. **Compensation 验证范围** [R1: 仅 50% → R2 rebut: 事实错误]
   - §4.5 明确报告 30% 和 50% 两个 sparsity level 的 compensation 冗余结果。R1 遗漏。Director 判定：不构成 weakness。

5. **Taxonomy 质量** [R2: 人为构建感 vs R1: 有价值的 positioning]
   - R1 论证 taxonomy 维度合理且帮助读者理解方法差异。Director 判定：不构成 weakness，但 MSE "intermediate coupling" 定义可更清晰。

6. **Soundness 评分** [R1: 3.0 vs R2: 3.5]
   - R1 因 C1 confound + seed 问题评 3.0；R2 因 C1 设计精良 + 30% 3-seed 完整评 3.5。Director 综合判定 Soundness 3.0（C1 逻辑缺陷是实质问题，不被 seed 覆盖率缓解）。

7. **Excitement 评分** [R1: 3.0 vs R2: 2.5]
   - R1 认为 mask divergence 发现有真正洞察价值（3.0）；R2 认为无 speedup + 窄 window + 已知组件组合限制实际影响（2.5）。Director 综合判定 Excitement 2.5（mask divergence 有分析价值但 practical impact 有限）。

---

## Questions for Authors

1. **C1 反事实控制**：如果用随机初始化预测器（而非 KL-trained）导出 oracle mask 训练 BCE，质量如何？这才是测试 "target quality vs gradient coupling" 的完整控制。[R1-Q1, R2 cross-AGREE]

2. **BCE+Gumbel 恶化机制**：为何 soft relaxation 使 BCE 从 27.97 恶化到 38.02？是 Gumbel noise 与 BCE binary target 冲突，还是 penalty controller 与 per-neuron 独立梯度冲突？去掉 penalty 只保留 Gumbel 的 BCE 表现如何？[R1-Q2, R2 cross-AGREE]

3. **14B MMLU 反转根因**：BCE 在 14B MMLU=71.67% 接近 TEAL=71.83%，而 KL=63.7%。是否 KL 的 coupled gradient 在大模型上发现了牺牲知识检索的 mask patterns？14B per-layer mask divergence 数据能否澄清？[R1-Q3, R2-Q1, consensus]

4. **Table 3 缺失数据**：30% KL 行缺 ARC-c/WG/GSM8K。如果这些 task 的 Δ 超过 1.70pp 或方向反转，会影响 C1 的结论。这些数据是否可用？[R2-Q2, R1 cross-AGREE]

5. **Mask divergence 训练动态**：68% 偏离是训练终点测量。early checkpoint 的 Jaccard 数据能帮助理解 KL mask 何时、如何偏离 magnitude。[R2-Q3, R1 cross-AGREE]

6. **Penalty controller 30% 公平性**：实际 sparsity 28.5% vs target 30%（偏差 5%）。TEAL 在 28.5% 下的 PPL 数据可作为 sanity check。[R2-Q5, R1 cross-AGREE]

---

## Missing References

**共识遗漏**：
- **OWL (Yin et al., 2024)**：研究 non-uniform layerwise sparsity allocation，与 §4.6 global vs uniform allocation 分析直接相关。[R1 cross-AGREE]

**可选补充**（不影响评分）：
- Sheared LLaMA (Xia et al., 2023)：structured pruning + distillation，与 MiniTron 方向相同。

**排除项**：
- LLM.int8() (Dettmers et al., 2022)：量化论文，不在 activation sparsity scope 内。[R2 cross-REBUT]
- FLAP (An et al., ICML 2024)：structured weight pruning，与本文问题空间不同。[R1 cross-REBUT]

---

## External Review (Stanford Agentic Reviewer)

外部审稿：未配置（项目未启用 `external_review.paperreview_ai`）。

---

## Overall Assessment

**Overall Score: 3.0 (Findings)**

**Soundness: 3.0/5** — 方法设计合理，C1 ablation 方向正确但因果推断逻辑有缺陷（mask transferability ≠ gradient coupling unimportant），soft-vs-hard confound 反常结果未充分解释。14B cross-architecture claim 与数据矛盾。30% 核心实验统计效力充分（3-seed），50% 主表呈现不完整。

**Excitement: 2.5/5** — Mask divergence 发现有分析价值，三 regime allocation 分析对后续工作有参考意义。但方法是已知组件的自然组合（KL + Gumbel + MLP predictor），无技术 surprise；无 wall-clock speedup；practical window 仅 30%（实际加速更窄）；14B downstream 反转限制可推广性。实践者从论文学到的 actionable insight 有限——"用 KL 替代 BCE" 是一个 recipe 而非 principle。

**Reproducibility: 3.5/5** — 超参数完整报告（d_b=128, τ schedule, lr, wd, batch, seq_len），GPU 型号和训练时间精确到分钟，3-seed 覆盖核心实验。但 evaluation protocol 细节（few-shot 设置、exact prompt templates）未完全明确，代码未开源。

**Confidence: 4/5** — 两位 Reviewer 均熟悉 LLM activation sparsity、knowledge distillation 和 efficient inference 文献，仔细核实了核心实验数据和 claim 对应关系。

### 判断理由

**为什么是 Findings (3.0) 而非 Borderline Conference (3.5)**：
1. 方法新颖性不足以支撑 Main：每个组件均为已有技术，组合合理但缺乏技术 surprise。两位 Reviewer 一致认为 Findings-appropriate。
2. C1 因果推断——论文最核心的 claim——存在逻辑缺陷和未解释的反常结果。
3. 14B downstream 反转是 scaling concern，不是可推迟到 future work 的问题。
4. 无 wall-clock speedup，practical operating window 仅 30%。

**为什么不低于 Findings (2.5)**：
1. C1 causal ablation 实验设计有 genuine intellectual merit。
2. 实验系统性和诚实度在同类论文中属上游。
3. Mask divergence 发现和 allocation regime 分析对后续工作有参考价值。
4. 写作质量高，格式完全合规，无 AI 痕迹。
5. 引用完整无遗漏。

### Rebuttal 优先级

1. **最高优先级**：修正 C1 framing（区分 mask discovery 和 inference-stage quality）+ 补充 BCE+Gumbel 无 penalty 控制实验
2. **高优先级**：14B MMLU 反转 mechanism 分析（per-layer divergence 对比 + layer retention 对比）
3. **高优先级**：Abstract/Introduction 重构——30% 为主叙事，50% 降级；削减至 2-3 个核心 claim
4. **中优先级**：50% KL 3-seed 上浮至主表；Table 3 补全 30% KL downstream 数据
5. **低优先级**：符号统一、缩写展开、caption 精简

---

## Detailed Comments (per section)

### Abstract
- 15+ 数字在 170 词中，信息过载。删减至 3 个关键数字。[W1]
- BCE/PPL 未展开（标准缩写可接受，但 KL/TEAL/SPON 应展开）。[M2]
- "advantages hold on most tasks across architectures" 与 Qwen MMLU 反转矛盾。[N2]
- 49% headline 来自 downstream 崩溃的 regime。[N3]

### Introduction
- 五段结构基本完整。从 SwiGLU sparsity → BCE 局限 → KL 提出 → C1 发现 → 贡献列表，逻辑流畅。
- P2→P3 过渡略突兀：缺少 "Therefore, we propose..." 桥接。[R2]
- Contribution #3 "allocation-to-downstream interactions at 7-14B" 在前文无铺垫。[R2]
- 49% headline 在 L14 位置过于突出。[N3]

### Related Work
- 6 段组织清晰，positioning 准确。
- MaskLLM 三点区分（sparsity type / mask generation / allocation）具体且有说服力。[R1, R2 consensus]
- D2DMoE 的 "intermediate coupling" 描述可更精确（不仅是 MSE supervision）。[R2]
- Griffin 引用感觉勉强（RG-LRU gating 与 SwiGLU 关系间接）。[R2]
- 缺少 OWL (Yin et al., 2024) 的引用。[consensus]

### Method (§3)
- 数学叙述清晰，Eq.1-6 内部一致。
- §3.5 adaptive penalty controller 设计合理，footnote disclaimer 是好做法。
- §3.6 gradient analysis 定位恰当（"suggestive"）。SNR 5.14× 作为经验度量辅助 intuition。[R2 rebut R1 overclaiming 质疑]
- ε=0.02 deadzone 选择依据未说明。[R1]
- Figure 1 caption 可更自包含。[R2]

### Experiments (§4)
- §4.2 Main results：Table 2 中 30% 全部 3-seed，50% 主表仅 s42（appendix 有 3-seed）。Caption 5 行过长。[W2, M5]
- §4.3 Extended training：iso-compute comparison (BCE 2.71× steps still worse) 有力支撑 KL 优势。
- §4.4 Mask analysis + C1 ablation：论文核心贡献，设计精良但因果推断逻辑有缺陷。[N1]
- §4.5 Ablation：Table 4 全面，但 SPON 2.4% 可能在噪声内，BCE+Gumbel 反常未充分解释。
- §4.6 Scaling & cross-architecture：三 regime 分析有 6 点数据支撑（R2 纠正 R1 的 "4 points" 误读）。14B 结果仅一句话处理。[N2]

### Conclusion
- 极简（2 句话），核心发现覆盖。但过于压缩，缺少 limitations 和 future directions 的一句话总结。

### Limitations
- 全面且诚实。覆盖 PPL 局限性、sparse kernel 缺失、14B 反转、OOD gap、seed variance。
- 14B 反转在此处被承认但分析不足。[N2]
- 缺少对 C1 confound 局限性的讨论。[N1]

### Ethics & Checklist
- 完整且认真填写，无遗漏。Qwen-2.5-14B 的 license 信息已包含。

### Appendix
- 13 个 section 全部在正文中有 explicit reference。组织合理，补充了 hyperparameter sensitivity、OOD、stability、SNR、mask visualization 等完整数据。
- Appendix E 的 3-seed 数据应上浮至主表。[W2]

### 格式合规
| 检查项 | 状态 |
|--------|------|
| 正文 ≤8 页 | ✅ |
| ACL template [review] | ✅ |
| Limitations 位置 | ✅ |
| 行号开启 | ✅ |
| 引用格式 (natbib) | ✅ |
| 匿名化 | ✅ |
| 图表字体 ≥7pt | ✅ |
| 附录被正文引用 | ✅ |
| 双栏格式 | ✅ |