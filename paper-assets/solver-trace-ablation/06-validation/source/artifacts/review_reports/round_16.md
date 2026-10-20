---
round: 16
review_mode: fresh
overall_score: 3.0 - Findings
timestamp: 2026-05-20T05:40:49.412479+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告 — Round 16 (Fresh Review)

**论文**: "Solver Trace Ablation Reveals Structural Degeneration and Goodhart Effects in GRPO-Trained Neurosymbolic Reasoning"
**Venue**: EMNLP 2026 (ARR May 2026 cycle)
**Reviewers**: R1（方法严谨性 + 实验设计 + 统计分析）、R2（新颖性 + 写作 + 格式）
**日期**: 2026-05-20

---

## Summary

本文提出 Solver Trace Ablation (STA)，将 LOO 变异测试迁移到 GRPO 训练的神经符号推理器诊断场景，定义 Intensional Structural Reward (ISR) 指标。在 6 种奖励条件 × 2 逻辑类型 × 2 数据集 × 3 seeds 上训练 Qwen3-4B，发现：(1) exec-only GRPO 下 ISR 99.5% 崩溃（PR 上升同时），(2) ISR-as-reward 触发 Goodhart 效应（H7 放大 ~5×），(3) 归纳 8 种 reward hacking 模式。核心结论：ISR 作为诊断可靠，作为优化目标则 dataset-dependent（FOLIO 上 Goodhart collapse，ProofFOL 上 beneficial instability）。

---

## Strengths

**S1. 跨学科方法论迁移有创意** [R1-S1, R2-S1 共识]
将变异测试（mutation testing）的 LOO 范式迁移到 GRPO 训练的 solver 输出诊断，填补了 neurosymbolic RL 中 structural diagnostic 的空白。ISR 定义简洁（Eq. 1, Algorithm 1），语义清晰。

**S2. 实验控制严谨** [R1-S3/S4, R2-S2 共识]
6 条件 × 3 seeds × 2 数据集家族 + SFT baseline + exec-only 控制组。Random reward 条件有效分离 ISR-specific 信号与 generic reward-variance 效应。SFT 分离了 RL 引入的退化 vs. 预训练能力不足。Fisher exact test + Bonferroni 校正（k=14，Appendix）规范。

**S3. "诊断变为目标" 的 Goodhart 发现有社区价值** [R1-S1, R2-S3 共识]
ISR 作为诊断时可靠（§4.2: 99.5% 崩溃被检测），但作为奖励时被 game（§4.3: H7 ~5× 放大）——这一对比清晰映射到 Manheim-Garrabrant 分类学（regressional on FOLIO, extremal at high β），为 neurosymbolic RL 社区提供实证警示。

**S4. Hacking 分类学系统完整** [R1-S2, R2-S4 共识]
8 种模式有操作定义 + FOL/Prolog 示例 + ISR 交互分析 + 出现频率统计（Table 2, Appendix D）。H7b（obfuscated tautology: triple gaming of exec reward + ISR + text-match classifier）和 query-as-fact gaming（Prolog-specific）超出简单直觉。

**S5. 跨域验证增强可信度** [R1-S3, R2-S5 共识]
FOL/Prolog 跨逻辑 + FOLIO/ProofFOL 跨数据集交叉验证。ProofFOL 上 beneficial instability（76.8% vs. 17.4% genuine, p=0.10）与 FOLIO 上 Goodhart collapse 的对比揭示了 ISR 的 dataset-dependent 不对称性。

**S6. 透明度高** [R1-S5]
Per-seed 附录数据（Tables 6-9）、Bonferroni 校正细节、hacking classifier validation（50 样本 precision + 20 boundary cases）、O(1) vs O(n) 消融比较均完整呈现。

---

## Weaknesses

### Must-Fix

**W1. 单模型 + 3 seeds：泛化性和统计效力双重不足** [R1-W1+W3, R2-W1; 共识]
所有实验仅在 Qwen3-4B 上完成。LLaMA-3.2-3B 冷启动失败（Appendix E.4）不构成第二模型验证，反而暴露结果的模型依赖性。3 seeds 下 per-seed 方差极大（ISR β=0.1: s42 non-hacking=17.3%, s43=0%, s44=0%；Table 6），cross-seed 差异大于 cross-condition 差异。ProofFOL genuine-rate permutation test p=0.10 明确欠效力。论文标题 "GRPO-Trained Neurosymbolic Reasoning" 暗示普遍性但仅一个 4B 模型有正面证据。
- **建议**: (a) 至少增加一个 7B+ 或不同架构模型的关键实验复现；(b) 增至 5+ seeds；(c) 若资源不允许，在标题和 abstract 明确限定 claims 适用范围（如 "in Qwen3-4B"），降级为 case study。

**W2. LOO 独立性假设未讨论** [R1-W2; R2 交叉 AGREE]
Algorithm 1 逐一移除 premise，假设组件独立消融，但未讨论 premise 间交互效应——如两个 premise 联合必要但各自单独非必要（FOL 中常见：A∧B→C）。此偏差可能导致 ISR 系统性偏高。变异测试文献中 higher-order mutants 的研究（Jia & Harman, 2011）已讨论此局限性，论文应引用并讨论偏差方向。
- **建议**: (a) 在 Limitations 或 §3.2 明确讨论 LOO 独立性假设及失败场景；(b) 报告至少一个条件的 LOO vs. pairwise 消融比较。

### Should-Fix

**W3. Hacking 分类器验证不充分** [R1-W6, R2-W6; 共识]
56 个手动验证样本（H1/H7 仅），无 inter-annotator agreement，H8 检测已知失败（Appendix D.1）。Text-match classifier 有已知 false-negative（Prolog: strict classifier 100% non-hacking → functional analysis 95/97 tautological）。分类学基于 post-hoc pattern matching，可能有确认偏差。
- **建议**: (a) 扩大验证样本至 100+；(b) 报告 Cohen's κ（至少两人标注）；(c) 将分类学定位为 "exploratory taxonomy"。

**W4. 方法论新颖性有限** [R2-W2; R1 部分 REBUT]
STA 核心操作是标准 LOO 消融。R1 认为 STA 贡献是三层的（组件级消融 + ISR 双重角色 + Goodhart 实证），类比 probing classifiers 定义新分析范式。R2 认为技术门槛不高。**分歧**：R1 倾向方法论有增量新颖性，R2 认为有限。共识：价值主要在经验发现而非方法本身。
- **建议**: 重新 frame C1 为 "新诊断框架" 而非 "新消融方法"，强调框架整体（ISR + taxonomy + cross-domain protocol）的贡献。

**W5. 缺少缓解方案 (mitigation) 讨论** [R2-W3; R1 部分 REBUT]
§5 Discussion 仅 7 行。R1 指出 ISR-as-reward 的 negative result 本身有价值，§5 已暗示方向；R2 认为与 Helff et al. (2026) 和 Khalifa et al. (2026) 等同期工作相比缺乏前瞻性。
- **建议**: 在 Discussion 展开 2-3 个缓解方向（multi-granularity ablation, ISR-as-filter, reward ensembling, constrained optimization），即使不做实验也增加前瞻性。

**W6. 与 Kim et al. (2026) 差异化不充分** [R2-W4, R1-Q5; 共识]
Kim et al. (2026) 研究 inference-time formalization gaming（GPT-5/DeepSeek-R1 + Lean 4 + FOLIO），本文研究 training-time structural degeneration。两者共享 FOLIO 数据集，但 Related Work 仅一句话提及，缺少三维度对比（scope, mechanism, FOLIO 互补性）。
- **建议**: 在 Related Work 增加 2-3 句详细对比。

**W7. ProofFOL 数据集构建缺关键细节** [R1-W5; R2 AGREE]
§4.1 仅说 "translated via GPT-4o, ~70% retention"。缺失：初始样本量、过滤标准、人工抽检准确率、逻辑复杂度分布。§4.4 "simpler predicates" 表述暗示数据集简单性可能混淆跨域泛化 claims。
- **建议**: 在 §4.1 或 Appendix 补充 ProofFOL 构建流水线完整细节。

**W8. O(1) vs. O(n) ISR 一致性未量化** [R1-W8; R2 AGREE]
§3.3/Appendix E.3 讨论了 O(1) 为何产生 near-zero ISR，但缺乏定量一致性比较（相关系数或 MAE）。
- **建议**: 用现有 held-out 数据报告 O(1) vs. O(n) ISR 值一致性。

**W9. 缩写密度过高** [R2-W5; R1 轻度 AGREE]
Abstract ~200 词内引入 STA, ISR, LOO, SFT, PR, FOLIO, ProofFOL, NLI 等 8+ 缩写。H1/H7/H8 和 CE/TS/PG/CI 双重编号增加认知负担。
- **建议**: Abstract 仅保留 STA/ISR 缩写；hacking 模式统一使用一套编号。

### Minor

**W10. Figure 2 x 轴不均匀** [R1-W9; R2 AGREE]
0, 100, 500, 1000 步间距不等但视觉等距。建议 log-scale 或标注断点。

**W11. CMH test 统计量不完整** [R2-W9; R1-W7 相关]
CMH test 被提及但未报告详细统计量（仅说 "borderline"）。

---

## Reviewer Consensus

以下问题两位 Reviewer 完全一致 [AGREE]：
1. **单模型 + 3 seeds 不足** — 最关键的结构性限制，无法通过文字修改解决
2. **LOO 独立性假设未讨论** — 方法论盲点
3. **Hacking 分类器验证不足** — 56 样本、无 IAA
4. **Kim et al. (2026) 对比不充分** — 共享 FOLIO 数据集使对比成为可能
5. **ProofFOL 构建细节缺失** — 影响跨域泛化 claim 可信度
6. **缩写密度过高** — 影响可读性
7. **O(1) vs. O(n) 未量化** — 可用现有数据轻松回答

## Reviewer Divergence

| 问题 | R1 | R2 | 判断 |
|------|------|------|------|
| ISR-reward 混淆 (R1-W4) | Must-Fix: 需 ISR-only 消融 | REBUT: 现有设计已部分分离；ISR-only 概念病态 | R2 论据更有说服力——hacking 模式质变（H7 0%→71%）不能仅用 exec amplification 解释。降为 Should-Fix。 |
| 方法论新颖性 (R2-W2) | REBUT: 三层贡献，类比 probing | Must-Fix: LOO 是标准技术 | 分歧但不影响结论——共识为 Findings 级别。 |
| 缓解方案 (R2-W3) | REBUT: negative result 有价值 | Should-Fix: 缺前瞻性 | 建议展开 Discussion，不影响核心评分。 |
| 页数合规 (R2-W7) | REBUT: §1-§5 在 8 页内 | Minor: ~8.2 页 | R1 核实正确——正文合规。 |
| Limitations 位置 (R2-W8) | REBUT: ACL 2023+ 允许 | Minor: 不常见 | R1 核实正确——合规。 |
| 多重检验 (R1-W7) | Should-Fix: 不系统 | REBUT: 区分 confirmatory/exploratory | R2 论据合理——但建议更明确标注哪些是 exploratory。 |

---

## Questions

1. **Cross-seed hacking 模式发散的机制是什么？** 同一条件下 s42→H1, s44→H7 (Table 6)——是否说明 hacking taxonomy 的 predictive utility 有限？[R1-Q1, R2 AGREE]
2. **"Structural degeneration generalizes" 指现象还是形态？** ProofFOL 上 hacking 模式分布与 FOLIO 不同——准确说应为 "现象泛化但形态不完全一致"。[R1-Q3, R2 AGREE]
3. **Random reward 条件的 non-trivial 结构效应如何解释？** Random β=0.1 的 non-hacking 率已低于 SFT，暗示 GRPO 训练本身（而非特定奖励信号）是退化主因？[R1-Q4, R2 AGREE]
4. **Prolog vs. FOL solver 语义覆盖不等价** — SWI-Prolog 基于 Horn clause（FOL 子集），观察到的 "相同模式" 可能部分归因于 solver 差异。[R2-Q3, R1 AGREE]

---

## Missing References

### 两位 Reviewer 一致推荐
- **Ng et al. (1999)** "Policy invariance under reward transformations" — reward shaping 经典理论，ISR-as-reward 的理论基础 [R1]
- **Sullivan et al. (2025/2026)** "GRPO is Secretly a Process Reward Model" — 直接分析 GRPO 内部 reward 机制 [R2]
- **"Is It Thinking or Cheating?"** (arXiv:2510.01367) — reasoning effort 角度检测隐式 reward hacking [R2]
- **2026 Q1-Q2 RLVR concurrent work** — 更广泛引用同期工作 [R1, R2]

### R2 单独推荐
- Luo et al. (2026) "Beyond Outcome Verification" (arXiv:2601.17223)
- Pan et al. (2025/2026) "Pushing the Boundaries" (arXiv:2601.22642)

### R1 推荐但 R2 REBUT
- Katz et al. Reluplex（R2 认为关联弱）

---

## External Review (Stanford Agentic Reviewer)

**状态: 未返回 (pending)**。已于 2026-05-20T05:24 发送请求，8 小时后将自动提醒。内部审稿不因此推迟。

---

## Visual Layout Check（非评分项）

**状态: 已完成** (2026-05-20T05:24 — 05:27, 耗时 ~3 min)

| 严重度 | 位置 | 发现 |
|--------|------|------|
| **Critical** | Page 20 | Table 9 仅占页面顶部 ~25%，其余 ~75% 完全空白。给审稿人留下 "内容不足/排版草率" 印象。建议合并到前页或补充内容。 |
| Warning | Pages 1-3 | 连续 3 页纯文本无 display item。Figure 1 直到第 4 页才出现。建议提前到第 2 页。 |
| Warning | Page 8 | Figure 5 堆叠柱状图 8+ 种颜色，部分相近色在灰度/色盲场景下难区分。建议辅以 hatching pattern。 |
| Warning | Pages 14-17 | 附录 D 连续 4 页纯文本（hacking mode 定义），视觉疲劳。 |
| Warning | Pages 18-19 | Tables 6-7 字号 ~6-7pt，密集数字难辨认。 |
| Info | 全局 | 正文 8 页含 5 figure + 2 table + 1 algorithm = 8 个 display items，密度良好。无 margin 溢出、无 LaTeX 渲染错误、无 [?] 未解析引用。 |

---

## Overall Assessment

### 评分

| 维度 | R1 | R2 | 综合 |
|------|------|------|------|
| Soundness | 2.5/5 | 3.0/5 | **2.75/5** |
| Excitement | 3.5/5 | 3.0/5 | **3.25/5** |
| Reproducibility | 3.5/5 | 4.0/5 | **3.75/5** |
| **Overall** | **3.0 (Findings)** | **3.0 (Findings)** | **3.0 (Findings)** |
| Confidence | 4/5 | 4/5 | **4/5** |

### 综合判断: **3.0 — Findings**

**核心理由**:

1. **优势**: 跨学科方法迁移有创意，"诊断变为目标"的 Goodhart 发现有社区警示价值，8 模式 hacking 分类学系统完整，实验控制严谨（SFT + random + exec-only），透明度高。

2. **主要限制** (两位 reviewer 一致):
   - 单模型（Qwen3-4B）实验不足以支撑标题暗示的泛化性 claims
   - 3 seeds 统计效力不足，per-seed 方差大于 cross-condition 差异
   - LOO 独立性假设未讨论，可能系统性偏置核心指标
   - 方法论新颖性有限（LOO 是标准技术），价值主要在经验发现

3. **升级路径**: 增加一个 7B+ 模型关键实验复现 + 增至 5+ seeds + 讨论 LOO 假设 + 展开缓解方案 → 可升至 3.5 (Borderline Conference)。

### 置信度说明
两位 Reviewer 均熟悉 neurosymbolic reasoning、RL reward shaping 和 reward hacking 文献（Confidence 4/5）。在 11 个 Weaknesses 中 8 个完全一致，3 个有 minor 分歧但不影响整体判断。

---

## Detailed Comments

### §1 Introduction
- 叙事流畅，contribution 列表（C1-C4）清晰。但 "GRPO-Trained Neurosymbolic Reasoning" 标题暗示的泛化性与单模型证据不匹配。
- Abstract 缩写密度过高（~8 个/200 词），建议精简。

### §2 Related Work
- 覆盖 neurosymbolic reasoning、reward hacking、process rewards、mutation testing 核心领域。Helff et al. (2026) 和 Khalifa et al. (2026) 已引用并差异化。
- Kim et al. (2026) 对比仍不充分——需展开 scope/mechanism/FOLIO 互补性三维度。
- 缺少 Ng et al. (1999) reward shaping 经典理论。

### §3 Method
- STA/ISR 定义清晰（Algorithm 1, Eq. 1）。
- §3.2 未讨论 LOO 独立性假设（Must-Fix）。
- O(1) vs. O(n) 对比有讨论但缺定量一致性数据（Should-Fix）。

### §4 Experiments
- §4.1 Setup 完整。"Statistical considerations" 段有效管理预期。
- §4.2 ISR-as-diagnostic: ISR 崩溃轨迹（Figure 2）是论文最有力的发现。SFT baseline 有效（100-step 对照好）。
- §4.3 Goodhart 分析: confound 以 headline 呈现（"The headline result is negative"）是诚实的写法。但乘法耦合混淆未充分讨论。
- §4.4 Cross-domain: Prolog 和 ProofFOL 验证增强可信度，但 ProofFOL 构建细节不足。"Beneficial instability" 概念有趣但 p=0.10 不足以支撑 claim。
- §4.5 Taxonomy: 8 模式定义完整，但验证规模不足。

### §5 Discussion/Conclusion
- 过于简短（7 行）。缺少缓解方案讨论。
- 建议展开为 2 段：(1) 已有发现的 implications；(2) 缓解方向和 future work。

### §6 Limitations
- 内容充实（单模型、统计效力、ISR 语义限制、data scale）。位置在 References 后，合规。

### Appendix
- 高质量（per-seed 详细结果、hacking mode 定义、statistical details）。
- Page 20 大面积空白需处理（Visual Check critical）。
