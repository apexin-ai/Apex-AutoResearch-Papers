---
round: 8
review_mode: fresh
overall_score: 3.0 (Findings)
timestamp: 2026-05-24T18:25:54.283767+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---


# Round 8 审稿报告：How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in Reasoning LLMs

**Venue**: EMNLP 2026 (via ARR)  
**Reviewers**: R1（方法严谨性）, R2（新颖性/完整性）  
**审稿模式**: Fresh（重新审稿）  
**交叉回应**: 完成，1 轮即收敛（分歧明确且不可调和，不启动额外轮次）

---

## Summary

本文研究结构化 MLP 剪枝准则对推理型 LLM 后续恢复训练（SFT + GRPO）的影响。核心发现：(1) CKA-based diversity-preserving pruning 在 GRPO reward recovery 上显著优于 importance-based pruning（3-seed, p=0.0009, Cohen's d=11.1）；(2) 所有方法 GRPO 后精度增量 <1pp（"reward-accuracy decoupling"）；(3) 提出 RASP scoring 结合 importance 与 diversity。实验基于 DeepSeek-R1-Distill-Qwen-7B，在 GSM8K/MATH-500/MBPP 上评估，20% sparsity 为主设定。

---

## Strengths

**S1. 研究问题有真实价值。** 剪枝准则如何影响 RLVR 恢复是一个未被充分研究的问题，对部署优化有直接意义。

**S2. 核心统计设计严谨。** CKA-only vs Standard 的 3-seed 比较 + Welch's t-test (p=0.0009) + Cohen's d=11.1 + 95% CI [3.62, 5.47]pp，在同类实验论文中属上乘。

**S3. Dose-response 方法论引入。** 将药理学 dose-response 框架应用于剪枝超参分析（α-sweep），方法论思路新颖。

**S4. TOST 等价性检验。** 使用 TOST 形式化 "decoupling"（ε=2pp, 7/8 通过），方法论意识优于多数同类工作。

**S5. 透明度高。** 诚实报告 RASP 单 seed、TOST 不同 ε 值结果、MBPP 不显著等不利信息。

**S6. 多维评估。** GSM8K + MATH-500 (OOD) + MBPP (跨域)，加 throughput/memory 效率指标。

---

## Weaknesses

### Critical

**C1. RASP 方法贡献 validity 存疑——单 seed + 叙事自相矛盾 [共识]**

RASP（论文的核心方法贡献）存在双重问题：
- **统计**：RASP α=2.0 优于 CKA-only 仅 +1.72pp (66.11% vs 64.39%)，基于单 seed。CKA-only 的 3-seed σ=0.18pp 暗示此差距可能显著，但 RASP 自身方差未知。Dose-response 非单调性（α=2.0→3.0 降 4.65pp，α=3.0→4.0 升 1.31pp）在 N=1 下极可能为噪声。
- **叙事**：论文声称 RASP "平衡 importance 与 diversity"，但 α=1.0（名义平衡点）collapse（52.83%），最优 α=2.0 中 diversity 权重为 importance 的 (1-F)^2 ≈ 4×，本质是 CKA-dominant。"平衡"叙事不准确。
- **函数形式**：乘法形式 I(h)×(1-F(h))^α 使 importance=0 时 score=0，可能人为导致 α=1.0 collapse。加法形式下此问题可能不存在，但论文未讨论选择理由。

**R1 Critical / R2 Critical（叙事）+ Minor（统计）。Director 综合判定 Critical**——R1 正确指出 R2 自身的叙事矛盾论证逻辑上依赖 RASP 统计可靠性，二者不可分。如多 seed 验证失败，论文方法贡献归零。

**C2. Cross-architecture 泛化严重不足，Title overclaim [共识 Critical]**

Title "Reasoning LLMs"（复数）但所有完整 SFT+GRPO 验证仅在 Qwen2.5 架构族内：DeepSeek-R1-Distill-Qwen-7B（主实验）+ DeepSeek-R1-Distill-Qwen-1.5B（cross-scale）。Qwen2.5-Math-7B 仅有 SFT 验证，GRPO 被推迟到 future work。两个共享 Qwen2.5 底层的模型不构成 cross-architecture 验证。Appendix O "Cross-Architecture Validation" 标题具有误导性。

**C3. Reward-accuracy decoupling 可能是训练不足的 artifact [分歧：R2 Critical / R1 Warning]**

100 步 GRPO（扩展 300 步）远少于典型 RLVR 训练（1000+ 步）。<1pp 精度增量可能仅反映训练不充分：
- SFT 贡献 ~60pp 恢复（post-prune ~1% → 59-64%），GRPO <1pp。GRPO 有 ~27pp 理论 headroom 但仅利用 <4%。
- **论文自身 15% sparsity 数据反证**：Section 4.3 报告 15% 下 GRPO 放大了 CKA-only 优势（SFT gap 5.69pp → GRPO gap 7.20pp），说明当 headroom 更大时 GRPO 有增量贡献——undermines decoupling 的普遍性。
- **300 步扩展选择性省略 accuracy**：Appendix E 仅报告 reward gap 维持（5.5×），关键性地缺失 accuracy 数据。
- **R1 反论**：Standard 的 reward 在 100 步已 collapse 到 0.054（peak 0.081），300 步仍未恢复。这是结构性崩溃而非简单欠拟合——"训练更久就能恢复"需要更强证据。

**Director 判定**：核心 decoupling claim 的 robustness 存在合理质疑，但 reward collapse 的结构性证据也不能忽视。保留为 Critical 级讨论点，建议作者提供至少 1000 步 accuracy 数据或限定 claim scope。

### Warning

**W1. Dose-response max_completion_length 混杂 [共识]**

主实验中 Random 用 512 tokens（其他方法 1024）。此不对称恰好压低 Random 的 reward，强化了论文 spectrum 叙事。核心 CKA-only vs Standard 比较（均 1024）未受影响，但 Random 在 spectrum 中的排序不可靠。

**W2. Discussion/Conclusion 过于单薄 [共识]**

Section 5 仅约 7-8 行。对于有如此丰富发现的论文，Discussion 应至少讨论：spectrum 部署指导意义、SFT vs GRPO 角色分离、与 Ji et al. (2026) self-healing 结论的对话、CKA-only 机制解释。

**W3. Calibration 数据量 M=512 未在正文说明理由 [共识]**

Section 3.2 定义 D_cal 但未给出 M 值或选择依据。

**W4. Title/叙事焦点与实际恢复来源错位 [共识]**

Title 聚焦 "Post-RLVR Recovery" 但 SFT 完成 95%+ 的恢复。GRPO 独特贡献在 reward trajectory 差异化但不转化为 accuracy。Discussion 应显式分离两者角色。

**W5. 缺失 3 篇高度相关文献 [R2 提出，R1 部分同意]**

1. "When Reasoning Meets Compression" (Li et al., 2025, arXiv:2504.02010) — 直接 benchmark 剪枝对 DeepSeek-R1 推理影响
2. "Can Pruning Improve Reasoning?" (2025, arXiv:2505.14582) — 标题直接相关
3. "GPrune-LLM" (2026, arXiv:2603.13418) — generalization-aware pruning（可能时间上来不及）

**W6. TOST ε=2pp 未 justify [共识 Minor-Warning]**

ε=2pp 未预注册。ε=1pp 功效不足（Appendix T），ε=3pp 全通过。论文透明度是加分项，但应在正文 justify 2pp 选择的合理性。

**W7. MBPP 不显著结果被引用为支持证据 [共识]**

Appendix G 承认 MBPP 不显著，但 Section 4.3 仍引用其支持 decoupling。需加注或降低引用强度。

### Minor

- **M1**: Recovery capacity 概念先用后定义（abstract/intro 中使用但 Section 3 才定义）
- **M2**: Figure 2 信息密度过高（structural analysis + scoring + pipeline + spectrum 合一图）
- **M3**: "Reward-accuracy decoupling" 术语引入时未充分建立先验预期（为何二者应耦合）
- **M4**: 无代码/checkpoint 发布承诺（对 controlled experiment 论文尤为重要）
- **M5**: Lottery Ticket Hypothesis 类比过于表面（LTH: pruning at initialization vs 本文: post-training structured pruning）

---

## Reviewer Consensus [AGREE]

1. **Cross-architecture overclaiming**: Title "Reasoning LLMs" 远超证据支撑范围（仅 Qwen2.5 家族）→ 需限定或补实验
2. **RASP 叙事不准确**: "平衡 importance 与 diversity" 与 α=2.0 CKA-dominant 现实不符 → 需修改叙事
3. **Discussion 单薄**: 发现丰富但讨论不足
4. **Calibration M 未说明**: 正文遗漏
5. **SFT 主导恢复但叙事聚焦 GRPO**: 比例失衡应讨论
6. **30% sparsity 全 collapse**: 有效窗口窄（20-25%），应讨论突破方向
7. **缺失引用**: 至少 2 篇高度相关工作未引用

---

## Reviewer Divergence [REBUT]

| 议题 | R1 | R2 | Director 裁定 |
|------|-----|-----|--------------|
| GRPO 训练步数 / SFT ceiling | Warning（reward collapse 证据使 "训练更久" 不 plausible） | **Critical**（15% 数据自相矛盾 + 300 步省略 accuracy） | Critical-leaning（数据 gap 真实存在） |
| RASP 单 seed 统计 | **Critical**（方法贡献 validity 核心） | Minor（RASP 非核心 claim 支撑） | Critical（R1 论证 R2 W3 逻辑上依赖此点） |
| Random baseline 不公平 | Critical（影响 spectrum 排序） | Warning（Random 非核心对比对象） | Warning（核心比较 CKA vs Standard 未受影响） |
| CKA 双重角色 / 循环论证 | Warning | **Minor**（两种 CKA 计算技术上不同） | Minor（R2 技术论证成立，但建议加说明） |

---

## Questions for Authors

1. **300 步 GRPO 的 accuracy 数据是什么？** Appendix E 仅报告 reward。如果 Standard 的 accuracy 在 300 步仍无改善而 CKA-only 有提升，这会大幅强化 decoupling；反之则 weaken。
2. **RASP α=2.0 的多 seed 结果？** 哪怕 2 seeds 也能大幅减少不确定性。如 +1.72pp 优势不可复现，RASP 作为方法贡献是否应降级？
3. **为何选择乘法形式而非加法？** 是否尝试过 βI(h) + (1-β)(1-F(h))？
4. **15% sparsity 下 GRPO amplifies gap 与 20% decoupling 的张力如何解释？** 这是 sparsity-dependent 现象吗？
5. **Appendix O "Cross-Architecture" 标题的修改计划？** Qwen2.5-Math-7B 共享底层架构。

---

## Missing References

1. **Li et al. (2025). "When Reasoning Meets Compression."** arXiv:2504.02010. 直接在 DeepSeek-R1 上 benchmark 剪枝对推理的影响——与本文有直接可比性。
2. **"Can Pruning Improve Reasoning?" (2025).** arXiv:2505.14582. 研究剪枝是否能改善推理能力，与 recovery capacity spectrum 有对话空间。
3. **"GPrune-LLM: Generalization-Aware Structured Pruning" (2026).** arXiv:2603.13418. "Generalization-aware" 与 "recovery-aware" 有概念亲缘性（可在 camera-ready 补充）。

---

## External Review (Stanford Agentic Reviewer)

**状态：未请求。** 本轮未配置外部审稿。

---

## Visual Layout Check（非评分项）

**状态：已完成** (耗时 ~3 分钟)

**Findings (2 Warning, 9 Info):**

- ⚠️ **Page 16**（Appendix 末页）：仅约 1/4 有内容（Table 16 + AI 声明），3/4 空白。视觉不专业。
- ⚠️ **Page 7-8**：Figure 3/5/6 面板较小，axis labels/legend/tick labels 字号偏小（≤6pt），审稿人可能需放大。Page 8 尤其密集。
- ℹ️ Page 1 无视觉锚点（首个 display item 在 page 2，可接受）
- ℹ️ Page 3-4 连续密集文本（Method section，有公式节奏，合理）
- ℹ️ Page 5 Figure 2 出现稍晚于理想位置但质量好
- ℹ️ Figure 1 色盲友好，caption 自包含
- ℹ️ Table 1/2 booktabs 规范
- ℹ️ Figure 5 灰度打印下可能难以区分
- ℹ️ Limitations 简短精炼（3 点），符合 EMNLP 2026
- ℹ️ Appendix 表格格式统一
- ℹ️ References 格式统一，无 [?] 未解析

**总评**：排版整体合格，无 critical 排版问题。Page 7-8 图表密度和字号是唯一需关注的视觉问题。

---

## Overall Assessment

**评分：3.0 (Findings)**

**置信度：4/5（High）**

### 评分理由

**核心贡献评估：**

1. **Recovery capacity spectrum（CKA-only ≫ Standard）**：有 3-seed 统计支撑，核心发现 sound。但 scope 被严重 overclaim（仅 Qwen2.5 family, 20-25% sparsity window）。
2. **Reward-accuracy decoupling**：新颖观察，但存在合理的训练充分性质疑，15% 数据自相矛盾，300 步 accuracy 缺失。
3. **RASP method**：单 seed、叙事矛盾、函数形式未推导——方法贡献不可靠。

**为何 3.0 而非 3.5：**
- 如果 RASP 多 seed 不可复现（当前证据不足以判断），论文核心贡献变为纯 empirical finding——spectrum ordering 有价值但 novelty 有限（CKA/diversity-preserving pruning 优于 importance-based 不令人意外）。
- Title/scope overclaiming 是系统性问题（已连续 4 轮提出），修复后论文叙事需大幅调整。
- Decoupling 作为独立贡献在训练充分性未验证前难以成立。

**升分条件（→ 3.5 Borderline Conference）：**
- (a) RASP α=2.0 多 seed 验证确认 +1.72pp 优势显著
- (b) 1000 步 GRPO accuracy 数据证实 decoupling 持续存在
- (c) 至少一个非 Qwen2.5 架构的完整 SFT+GRPO 验证
- 满足 (a)+(b) 或 (a)+(c) 即可升至 3.5

**当前论文适合 Findings track**——empirical findings 有价值但方法贡献和 claim scope 问题阻碍 Main Conference 接收。

---

## Detailed Comments

### Abstract
- "holds across sparsity levels" overclaims（仅 20-25% 成立，15% 下 GRPO amplifies，30% collapse）→ 改为 "at moderate sparsity (20-25%)"
- "Reasoning LLMs" 复数 overclaim → 限定为 Qwen2.5 family 或加 "A Case Study"
- 考虑加代码发布承诺

### Section 1 (Introduction)
- Recovery capacity 概念先用后定义——首次出现时加括号简述
- "Reward-accuracy decoupling" 首次使用时应建立先验预期（为何二者通常耦合）

### Section 2 (Related Work)
- Lottery Ticket Hypothesis 类比表面——LTH 研究 pruning at initialization，与本文场景有本质区别。弱化类比或加说明
- 缺失 Li et al. (2025) 和 "Can Pruning Improve Reasoning?" (2025)

### Section 3 (Method)
- **3.2**: D_cal 的 M=512 未在正文指定
- **Eq. 3 (RASP)**: 乘法形式选择未讨论理由。应解释为何 I(h)×(1-F(h))^α 而非 βI(h)+(1-β)(1-F(h))
- RASP "平衡 importance 与 diversity" 叙事需修改为 "CKA-dominant with importance correction"

### Section 4 (Experiments)
- **4.1**: Random baseline max_completion_length=512 应标注并讨论影响
- **4.2 (Dose-response)**: α 值间 max_completion_length 不一致是关键混杂。Inverted-U 峰值不可靠直到统一条件后复现
- **4.3**: 引用 MBPP 时需注明统计不显著
- **4.3**: 15% vs 20% sparsity 对 GRPO 行为的差异应讨论——这是 decoupling 非普遍性的内部证据
- **4.4 (TOST)**: ε=2pp 选择需 justify
- **4.5 (Layer-wise CKA)**: 虽然 intra-layer CKA（剪枝）与 layer-wise CKA（分析）技术上不同，应加一句说明避免循环论证印象

### Section 5 (Discussion/Conclusion)
- 显著扩充 Discussion：加入 SFT vs GRPO 角色分离、spectrum 实用指导、与 self-healing 文献对话、30% ceiling 突破方向
- Throughput regression (-19%) 应在 Limitations 讨论

### Appendix
- **Appendix E**: 补充 300 步 accuracy 数据（关键缺失）
- **Appendix O**: "Cross-Architecture Validation" 标题误导——Qwen2.5-Math-7B 共享架构。建议改为 "Cross-Model Validation within Qwen2.5 Family"
- RASP 所有 α 值和 Random 应标注 "single seed" 脚注

---

**R1 评分**: 3.5 (Borderline Conference)  
**R2 评分**: 3.0 (Findings)  
**Director 综合**: 3.0 (Findings)

综合评分倾向 R2 的 3.0 而非 R1 的 3.5，原因：(1) RASP 方法贡献在多 seed 验证前不可靠——如果方法贡献归零，novelty 降为 empirical observation level；(2) scope overclaiming 是系统性问题；(3) decoupling 的训练充分性质疑虽非定论但合理。R1 的 3.5 基于 "decoupling 发现本身有 novelty"，这一立场成立但需要更强的 robustness 证据。
