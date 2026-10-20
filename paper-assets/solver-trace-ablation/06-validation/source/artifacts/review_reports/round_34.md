---
round: 34
review_mode: fresh
overall_score: 3.5 - Borderline Conference
timestamp: 2026-05-25T05:06:50.080138+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

## 审稿报告 — Round 36 (Fresh Review)

**项目**: solver-trace-ablation
**目标 Venue**: EMNLP 2026 (ARR)
**Reviewer 配置**: 2 人（R1: 方法严谨性/统计; R2: 新颖性/完整性/写作）
**交叉分享**: 完成，R1 和 R2 均完成逐条 [AGREE]/[REBUT]

---

## Summary

本文应用 leave-one-out ablation（Solver Trace Ablation, STA）于 GRPO 训练的 neurosymbolic 推理器，通过 Intensional Structural Reward (ISR) 诊断 formalization 中的结构退化。核心发现为 observe-vs-optimize asymmetry：ISR 作为 post-hoc 诊断有效揭示 hacking modes，但作为训练奖励时触发 seed-dependent Goodhart 效应（3/5 seeds 退化为 gaming）。实验在 Qwen3-4B 上测试 6 种奖励条件，提出 8 种 hacking mode 分类，并在 Prolog（跨逻辑）和 ProofFOL（跨数据集）上扩展验证。

---

## Strengths

1. **实验设计系统周全**：6 种奖励条件（含 shuffled-ISR 控制）、5 seeds、per-seed 完整报告、多种统计检验。方法论严谨度高于同类实证论文。

2. **Prolog 跨逻辑复制强有力**：3 seeds 全部 0% non-hacking，通过不同 gaming 机制（clean TS, degenerate syntax, query-as-fact），是论文最强的泛化性证据。

3. **Hacking taxonomy 有描述性价值**：CE 和 TS 两个主导模式跨条件稳定；8-mode 分类为后续研究提供参考框架。

4. **学术诚实性高**：坦承报告 wide CI、阴性结果（8B 不收敛）、post-hoc seed 添加、ProofFOL 可能的反向证据。统计检验标注为 "exploratory" 和 "descriptive"。

5. **Reproducibility 信息充分**：Table 2 完整超参、compute resources 说明、per-seed Appendix 数据。

6. **写作结构清晰**：Algorithm 1 + Figure 2 有效传达 pipeline；Section 5 实践指南对从业者有直接价值。

---

## Weaknesses (Must-Fix)

### N1 [critical] Abstract 跨数据集声称仍具误导性

**共识度**: R1 + R2 强共识（本轮最重要修正项）
**Issue ID**: v19-R12-W3（reopened）

Abstract 声称 "the observe-vs-optimize asymmetry persists across logic types and dataset families—confirmed by cross-logic (Prolog) replication and supported by exploratory cross-benchmark (ProofFOL) evidence"。

问题：ProofFOL ISR-as-reward 的 genuine rate **高于** exec-only（p=0.10），方向与 "asymmetry persists" 相反——ISR 在 ProofFOL 上可能是矫正性的（论文自身在 §4.4 解释为 "hacking geometry" 差异使 ISR reward "effectively corrective"）。"persists across dataset families" 配合 "exploratory" 限定仍暗示方向一致，但数据方向可能相反。

跨逻辑（Prolog）证据坚实（3/3 universal gaming），应保留并强调。

**要求**：Abstract 改为 "confirmed by cross-logic (Prolog) replication; cross-dataset (ProofFOL) evidence reveals dataset-dependent boundary conditions rather than universal persistence"，或直接移除 "dataset families"。

### N2 [critical] 泛化声称从极窄实验范围过度推广

**共识度**: R1 + R2 完全一致
**Issue ID**: v36-R12-N2（new）

Section 1 声称 "any verifiable proxy that rewards structural properties of solver inputs is susceptible to the same exploitation"——从 Qwen3-4B / FOLIO / GRPO K=4 的单一配置推断到一般性结论。

具体限制：(1) 单一模型：Qwen3-8B 和 LLaMA-3.2-3B 均未产生可分析结果；(2) 单一训练算法：仅 GRPO K=4；(3) 单一评估集：100 个 FOLIO 样例。

Section 6 (Limitations) 已涵盖单模型限制，但 Section 1 和 5 的一般性语言与 Limitations 的 scope 限定存在张力。

**要求**：Section 1 的 "any" 需限定为 "LOO-based structural proxies in comparable settings" 或类似表述。Section 5 结论段需与 Limitations 的 scope 一致。

---

## Weaknesses (Should-Fix)

### W1 [warning] 统计效力不足以支撑 seed-dependent 定量声称

**共识度**: R1 + R2 强共识
**Issue ID**: v34-R1-N1（resolved, 新增 R36 mention）

Clopper-Pearson CI [11.8%, 88.1%] 对 Goodhart 发生率无信息约束。Seeds 45-46 是 post-hoc 添加（experiments.tex L65），可能引入 optional stopping 偏差。

**当前状态**：Abstract 已改为 "can occur"，CI 已在正文展示。修正方向正确。

**残余问题**：(1) 论文未说明 5 seeds 是否为 pre-registered 设计；(2) R1 指出 optional stopping 未被讨论。建议 Limitations 加一句说明 seeds 45-46 post-hoc 添加的统计含义。

### W2 [warning] Shuffled-ISR 控制的替代解释

**共识度**: R2 提出
**Issue ID**: v36-R2-W2（new）

Shuffled-ISR 87% non-hacking 可能不是因为打乱信号阻止了 Goodhart，而是因为 PR=15% 意味着模型根本未收敛——未成功学习的模型自然不会 game 任何指标。这个替代假设未被讨论。

**要求**：在 §4.2 或 Appendix 中加一句讨论 non-convergence 替代解释。

### W3 [warning] 缺少代码和数据可用性声明

**共识度**: R2 提出，R1 同意
**Issue ID**: v36-R12-W1（new）

24 页论文中未提及代码、训练模型或数据是否会公开。ARR Reproducibility 维度要求评估数据和代码可获取性。

**要求**：添加 Data Availability 声明（匿名审稿阶段可用 anonymous repo link）。

### W4 [warning] Hacking taxonomy 部分模式的可靠性

**共识度**: R2 提出，R1 部分同意

CE 和 TS 跨条件稳定可靠。但 5/8 modes 仅在特定 seeds/conditions 出现（PG 依赖 post-hoc 人工审计），可能是配置偶然产物。

**建议**：将 taxonomy 定位为 "observed patterns" 而非暗示 exhaustive coverage。不影响主要结论。

### W5 [warning] Seed 43 评估协议不一致

**共识度**: R1 + R2 均同意
**Issue ID**: v17-R1-W9（resolved）

Seed 43 使用 nucleus sampling (T=0.7) 而其他 seeds 使用 greedy decoding。正文脚注 + N=2 sensitivity + Appendix D.6 已充分披露。

**当前状态**：处理到位，无需进一步修改。记录为已解决。

---

## Questions

1. Seeds 45-46 是否与 seeds 42-44 在同一时间选定？如果是先观察到 42-44 结果再添加 45-46，请在论文中明确说明。
2. Shuffled-ISR 的低 PR (15%) 是否意味着模型未收敛？如何区分 "信号打乱阻止 gaming" 和 "未收敛导致无法 game"？
3. 是否计划公开代码和数据？

---

## Missing References

无新增。前轮标记的缺失引用（Krakovna et al. 2020, Lanham 2023, Turpin 2023, Nishimura et al. 2026）均已在 related_work.tex 中确认存在。

---

## External Review

未请求外部审稿。

---

## Visual Layout Check（非评分项）

**状态**: 完成 (0 critical / 2 warning / 13 info)

| 严重度 | 位置 | 发现 |
|--------|------|------|
| warning | pp.3-8 | Figures 3-6 红/绿配色对红绿色盲不友好（~8% 男性），建议 blue/orange 或 Okabe-Ito 色板，或辅以不同 marker shape/hatching |
| warning | pp.19-21 | Appendix D Tables 9-12 字号偏小，列数多（8-9列），屏幕阅读时可能需缩放 |
| info | pp.1-8 | 正文 8 页合规，Limitations §6 在 p.9 不计入页限，符合 EMNLP 2026 要求 |
| info | pp.1-8 | 布局节奏良好：p2(Fig1)→p3(Algo1)→p4(Fig2)→p5(Tab1)→p6(Fig3)→p7(Fig4)→p8(Fig5+6)，无连续纯文本页 |
| info | p.4 | Figure 2 全宽排版清晰，✓/✗ 符号色盲友好 |
| info | p.5 | Table 1 booktabs 格式规范，最优值加粗 |
| info | p.9 | Limitations 简洁覆盖 3 点，符合 EMNLP 要求 |
| info | pp.10-11 | 参考文献格式统一，无未解析引用 |

---

## Overall Assessment

**评分: 3.5 / 5 — Borderline Conference**

**评分逻辑**：
- R1: 3.5 (Borderline Conference)
- R2: 3.5 (Borderline Conference)
- 两位 Reviewer 评分完全一致

**给分理由**：

论文在实证系统性上表现出色：6 种奖励条件的系统对比、5 seeds per-seed 分析、matched controls（shuffled-ISR）、cross-logic replication（Prolog 3/3 universal gaming）、透明报告阴性结果和统计限制。Hacking taxonomy 对后续研究有直接参考价值。学术诚实性值得肯定。

两个核心问题制约评分：
1. **统计效力结构性不足**：5 seeds 的 CI 无信息，无法对 Goodhart 发生率做有意义估计。论文已改为 existence claim 并展示 CI，处理方向正确但无法完全消除限制。
2. **泛化声称超出数据支撑**：Abstract "persists across dataset families" 和 Section 1 "any verifiable proxy" 均超出单模型/单数据集实验的支撑范围。Prolog 跨逻辑复制有力，但 ProofFOL 证据方向可能相反。

概念新颖性方面，LOO ablation 是标准技术，observe-vs-optimize asymmetry 是 Goodhart's Law 的领域实例化。论文正确定位为 "systematic empirical analysis"（C1），但 Section 1 的一般性推断仍超出实证边界。

**升级路径（3.5 → 4.0）**：
1. 修正 Abstract "dataset families" 表述（N1）
2. 限定 Section 1 "any verifiable proxy"（N2）
3. 添加 Data Availability 声明（W3）
4. 加一句 shuffled-ISR non-convergence 讨论（W2）

**降级风险（3.5 → 3.0）**：
如果审稿人主要从概念新颖性角度评估，可能判 Findings (3.0)。

---

## Detailed Comments

### Director 裁定：交叉分歧解决

| 争议点 | R1 | R2 | Director 裁定 |
|--------|-----|-----|--------------|
| ISR-NLI 低相关性 (R1-N3) | critical | minor (REBUT) | **Side R2**: 论文明确声明 ISR ≠ semantic faithfulness (method.tex L54)，诊断逻辑不依赖 ISR-NLI 相关性。mode breakdown 独立于 ISR scalar 检测 hacking。降级为 info。|
| ISR-Shapley 形式化 (R1-W5) | warning | unnecessary (REBUT) | **Side R2**: "LOO marginal contribution, a restriction of the Shapley value to the maximal coalition" (method.tex L53) + Appendix B 推导充分。无需修改。|
| ProofFOL overclaim 严重度 | warning (W4) | critical (N1) | **采 R2 (critical)**: ProofFOL 证据方向可能相反，abstract 的 "persists across dataset families" 误导性高于单纯的 p 值不显著。|
| 新颖性评价 | Excitement 3.5/5 | Excitement 3/5 | **折衷**: 概念新颖性有限（Goodhart's Law 领域实例化），但 seed-dependent 非显然性 + taxonomy 实用性有独立价值。|
| Hacking taxonomy | 列为优势 | 可靠性存疑 (W2) | **折衷**: CE/TS 稳定可靠；5/8 modes 降级为 "observed patterns"。不影响主要结论。|

### 格式合规性

- ✅ ACL 模板正确
- ✅ 正文 8 页（Sections 1-5），Limitations 在 §6（p.9）不计入页限
- ✅ Abstract 约 189 词（≤200）
- ✅ 匿名合规（无身份泄露）
- ✅ AI assistants 声明（Section E）
- ⚠️ 无 Data Availability 声明

### Issue Tracker 更新摘要

**Reopened**: v19-R12-W3（ProofFOL 跨数据集声称）
**New open**: v36-R12-N2（Section 1 过度泛化）、v36-R12-W1（代码/数据声明）、v36-R2-W2（shuffled-ISR 替代解释）
**Resolved confirmed**: v17-R1-W9, v34-R1-N1, v35-R1-M1, v34-R1-W5 等多项前轮 issues 经本轮验证修复到位
**wont_fix confirmed**: v17-R12-W1（单模型）、v22-R1-W4（shuffled-ISR 样本量）

Open issues: 4 | Resolved: 30+ | wont_fix: 3