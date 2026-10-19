---
round: 2
review_mode: fresh
overall_score: weak reject
timestamp: 2026-05-19T02:11:40.043920+00:00
reviewer_ids: [1, 2, 3]
cross_response_reviewer_ids: [1, 2, 3]
force_resubmit: False
---

# 审稿报告 — Round 2 (Fresh Review)

**论文**: "Correction Over Selection: Dissecting Inference-Time Action Refinement for Frozen VLAs"
**目标 venue**: CoRL 2026 Main Conference
**Deadline**: 2026-05-29（距今 10 天）
**审稿模式**: Fresh（独立初审）
**Reviewer 编排**: 3 人（R1: 方法/实验/统计; R2: 新颖性/Related Work/写作/格式; R3: CoRL venue fit/格式合规/可重复性）
**外部审稿**: 未配置，跳过

---

## Summary

本文提出 sample-select-correct pipeline 对 frozen flow-matching VLA 进行 inference-time action refinement：抽 K=10 个 action sample，L2 argmin 选择最接近均值的候选，再用 ~327K 参数的 MLP（CRM）预测有界残差修正（‖δ‖₂ ≤ ε）。在 LIBERO-Object 上实现 17.6±2.6% vs 11.6±1.1%（p=0.003, Mann-Whitney U），在 LIBERO-Spatial 上无提升（30-35%）。Component decomposition 表明 learned correction 是主要机制而 multi-sampling 是使能条件。论文同时报告 conformal features 失效（progressive collapse to 0%）和 tokenized VLA 不适用的 negative results。

---

## Strengths

- **S1: 系统化 component decomposition** [R1-S1, R2-S3, R3 隐含, 三方共识]
  通过 K=1 correction、selection-only、random selection 等控制实验清楚拆解各组件贡献。"Selection alone 无显著帮助、K=1 correction 低于 baseline、二者结合才有效"的发现对 embodied test-time compute scaling 有洞察价值，与 LLM test-time scaling 的 selection-dominant 范式形成有意义的对比。

- **S2: 有价值的 negative results** [R1-S2, R2-S4, 共识]
  Conformal features 的失败（obs_only 14.3-17.6% vs perdof collapse 至 0%）和 tokenized VLA 不适用性，为后续研究提供指导。

- **S3: 统计方法严谨** [R1-S3, R2-S2, R3-S3, 三方共识]
  Seed-level Mann-Whitney U + sign test，正确处理 within-seed episode 非独立性。相比 Round 1（Fisher test）已大幅改善。

- **S4: 写作质量高** [R1-S4, R2-S1/S5, R3-S1, 三方共识]
  Pipeline 描述精确，符号一致，AI 写作痕迹几乎为零。Limitations section 诚实全面。

- **S5: 实验可重复性基础尚可** [R3-S2]
  关键超参数记录完整（Adam lr=1e-3, batch 32, 50 epochs, seed 42, augmentation noise），SmolVLA checkpoint 路径已给出。

---

## Weaknesses（按严重程度排序）

### Critical（影响接收决定）— 7 项三方共识

**W-C1: 正文超出 8 页限制（约 9 页）** [R3-W5, R1/R2 AGREE]
R3 确认正文（Section 1-7 + AI Disclosure）延伸至约第 9 页。CoRL 2026 规定 main text 最多 8 页（Limitations 和 AI Disclosure 计入），CoRL 2024 review instructions 明确将格式违规列为 desk rejection 标准。这是最紧急的 action item。
*优先级：P0（desk reject 风险）*

**W-C2: 极低绝对性能限制所有发现的泛化性** [R2-W1, R1/R3 AGREE]
VLA-only baseline 仅 11.6%，pipeline 达 17.6%——整个评估处于 base policy 几乎不工作的 regime。Per-task 分析显示 improvement 集中在 4/10 tasks（chocolate_pudding +40pp, bbq_sauce/ketchup +20pp, salad_dressing +10pp），其余 6 task 基本无变化或退化。Component decomposition 结论能否外推到更强 base policy（如 >50%）完全未知。R3 指出在更强 base policy 下 selection 可能就够用，correction 的相对贡献可能完全不同。

**W-C3: 评估范围极窄** [R2-W2, R1-N4, R3-W1, 三方共识]
(a) 仅 SmolVLA（450M）一个 backbone，但标题用 "Frozen VLAs"（复数）；(b) 仅 LIBERO 一个 benchmark family（且只有 Object 有效）；(c) 纯仿真，无 real-robot 实验或 sim-to-real 论证。CoRL CFP 明确鼓励 "real-robot experiments or simulation evidence demonstrating transferability to physical robots"，论文两者皆无。

**W-C4: CRM 在 eval 任务 demo 上训练，无 held-out 泛化验证** [R1-N1, R2/R3 AGREE]
CRM 训练数据来自 20 个 LIBERO tasks 的 demo = 评估的 Object 10 + Spatial 10。无法区分 task-specific memorization 和 generalizable correction。Per-task concentrated improvement（4/10 tasks）与 memorization 假说兼容。需要 leave-task-out 实验。

**W-C5: 缺少 A2C2 实验对比** [R1-N2, R2-W5, R3 AGREE, 三方共识]
A2C2 被论文认定为 "closest concurrent work"，详细列出三点方法差异，但从未作为 baseline 运行。A2C2 correction head 可直接 attach 到同一 frozen SmolVLA checkpoint 做 controlled comparison。"Different training regime" 辩护不成立。

**W-C6: 动机与评估断裂** [R2-W4, R1/R3 AGREE]
Introduction 用 LIBERO+ 数据（π₀ 94.2%→6.6%）motivate distribution shift，但实验在标准 LIBERO 上。SmolVLA 11.6% baseline 原因未解释。R3 指出可能非 distribution shift 而是 checkpoint 本身弱，若如此则 Introduction 的整个 robustness 叙事框架 misleading。

**W-C7: K=10 forward passes latency 未量化** [R3-W2, R1/R2 AGREE]
SmolVLA 450M 单次 forward pass ~50ms，K=10 约 500ms，对应 ~2 Hz，远低于 10-20 Hz 操作频率。论文仅提 "~0.3ms CRM overhead"，将 CRM 作为 overhead 代表但回避了 10x VLA pass 的主要开销。R1 指出这与论文批评 VLA-Pilot "2.41s per control step" 同类。

### Critical — Seed 数量问题

**W-C8: Seed 数量小且不平衡** [R1-N3, R2/R3 AGREE]
obs_only 7, VLA-only 5, Argmin 6, Random 3, VLA-mean 4, scalar 4。主要对比（U=35=U_max, p=0.0025）在给定样本量下已是最强结果，但次要对比严重 underpowered：Random 仅 3 seeds 的 "statistically indistinguishable" 结论不成立（R3 补充：n1=3,n2=5 即使完全分离也只能 p=0.036）。

### Warning — 8 项

**W-W1: "Dissecting" 分析深度不足** [R2-W7, R1/R3 AGREE]
缺 correction vector 分布、trajectory 阶段分析、成功/失败 pattern 对比、trajectory 可视化。当前为 ablation 而非 dissection。

**W-W2: Applicability boundary 基于单一对比** [R1-W3, R2/R3 AGREE]
仅 OpenVLA T=0.5。未测更高 temperature 或其他 VLA。"Architectural boundary" 是强 claim 但证据仅一个 data point。

**W-W3: Spatial null result 分析不足** [R1-W4, R2/R3 AGREE]
仅 seed 42 单点，无 per-task Spatial 表，无 failure case 分析。若作为 contribution 需大幅加深。

**W-W4: ε 敏感性分析不完整** [R1-W2, R2 AGREE]
scalar 仅 ε=0.1 一个点，各 ε 点 seed 数 n=1-7 不一致。

**W-W5: 可重复性缺口** [R3-W8/W9/W10, R1/R2 AGREE]
(a) 硬件环境和训练耗时未报告；(b) SmolVLA checkpoint 无 commit hash；(c) Precompute flow-matching random seed 未明确。

**W-W6: "Geometric medoid" 术语不正确** [R1-W1, R2/R3 AGREE]
实际是 argmin-to-centroid（squared L2），非经典 geometric medoid。

**W-W7: DAgger 引用误用** [R1-W5, R2/R3 AGREE]
DAgger 是 interactive dataset aggregation，非 static Gaussian noise augmentation。

**W-W8: Related Work 遗漏 + bib 格式** [R2-W6, R1 部分 REBUT]
R2 列出 5 篇遗漏（ADPro/GPC/Recurrent-Depth VLA/Residual Policy Adaptation/Compose Your Policies!）。R1 认为 32 条引用在 CoRL 正常范围但同意 bib venue 需更新。RT-2/OpenVLA/Octo 应从 @misc 更新为 @inproceedings。

---

## Reviewer Consensus [AGREE]

以下问题获得三方一致认同（零 REBUT）：

| # | 问题 | R1 | R2 | R3 |
|---|------|----|----|-----|
| 1 | 无 real-robot + 低绝对性能 + latency 未量化 | N4 | W1/W2/W8 | W1/W2/W3 |
| 2 | CRM 训练/评估任务重叠 | N1 | AGREE | AGREE |
| 3 | 缺少 A2C2 baseline | N2 | W5 | AGREE |
| 4 | Seed 数量不平衡 | N3 | AGREE w/ nuance | AGREE |
| 5 | 评估范围窄 | AGREE | W2 | AGREE |
| 6 | 动机-评估断裂 | AGREE | W4 | AGREE |
| 7 | 正文超页 | AGREE | AGREE w/ caveat | W5 |

## Reviewer Divergence [REBUT]

| # | 问题 | 分歧方 | 理由 |
|---|------|--------|------|
| 1 | 方法新颖性严重程度 | R2: critical; R1/R3: warning | R1/R3 认为 component decomposition 有独立价值，真正问题是实验规模 |
| 2 | Venue fit 归因 | R3: 应投 ML venue; R1/R2: REBUT | R1/R2 认为主题是 robotics-specific 的，问题在于执行（sim-only）而非 contribution 类型 |
| 3 | Orphan bib entries | R3: Gauss1857/Lagrange1788 存在; R2: REBUT | R2 核验 bib 文件确认不存在这些条目，R3 可能混淆 |

---

## Questions for Authors

1. SmolVLA 在标准 LIBERO-Object 上 baseline 为何只有 11.6%？原论文报告多少？是 distribution shift 还是 checkpoint 本身性能差？
2. CRM 是否曾在 held-out tasks 上测试？15 task 训练 / 5 held-out 评估结果如何？
3. 在 base policy >50% 的 setting 下，correction > selection 是否仍成立？
4. K=10 forward passes 在 SmolVLA 上的 wall-clock latency？在 10-20 Hz 控制频率下是否可行？
5. A2C2 correction head 能否 attach 到同一 frozen SmolVLA？为什么不做对比？
6. Table 1 LIBERO-Spatial Random "---" 原因？
7. 能否公布每个 seed 的具体成功率？
8. perdof 在 ε=0.03 达 14%，K 更大时 conformal features 是否可能有用？
9. Precompute pipeline 的 flow-matching random seed 是什么？与 evaluation seed 是否相同？
10. SmolVLA checkpoint 的 HuggingFace commit hash？

---

## Missing References

**R2 提出（frozen generative policy + inference-time enhancement 方向）**：
- ADPro (2025, arXiv 2508.06266)
- GPC (2025, arXiv 2502.00622)
- Recurrent-Depth VLA (2026, arXiv 2602.07845)
- Compose Your Policies! (2025, arXiv 2510.01068)

**R1 提出**：
- ACT temporal ensembling (Zhao et al. 2023)
- Best-of-N sampling in robotics

**bib 格式**：RT-2/OpenVLA/Octo 需更新 @misc → @inproceedings + venue 信息。

---

## External Review (Stanford Agentic Reviewer)

未配置（项目未启用 `external_review.paperreview_ai`），跳过。

---

## Overall Assessment

**Score: weak reject**
**Confidence: high**

| Reviewer | Score | Confidence |
|----------|-------|------------|
| R1 (方法/实验/统计) | weak reject | high |
| R2 (新颖性/写作/格式) | weak reject | high |
| R3 (venue fit/格式/可重复性) | weak reject | high |

**核心判断**：论文在写作质量、统计严谨性和 component decomposition 设计上有实质性优势。相比 Round 1 在统计方法（Fisher→MW-U）、framing（claim reframe）、格式（AI Disclosure、标题、CP subsection）方面有显著改进（Round 1 的 7 个 critical 中 4 个已 resolved）。

但持续存在的结构性问题——评估范围过窄（单 VLA/单 benchmark/sim-only）、绝对性能极低（17.6%）、缺少 A2C2 对比、CRM 泛化未验证——加上新发现的页数超限（desk reject 风险）、动机-评估断裂、latency 未量化，共同构成在 CoRL 2026 录用标准下的 significant gap。这些不是 writing fix 能解决的问题，需要额外实验。

**给 Research Director 的建议优先级**：

| 优先级 | 问题 | 可行性（10 天内） | 影响 |
|--------|------|-------------------|------|
| P0 | 页数压缩至 8 页 | ✅ 高 | 避免 desk reject |
| P1 | A2C2 baseline 实现 | ⚠️ 中（需实现+跑实验） | 填补 positioning 核心缺陷 |
| P1 | Held-out task split | ⚠️ 中（需 re-train + re-eval） | 验证 generalization vs memorization |
| P1 | Latency breakdown 表格 | ✅ 高（仅需测量） | 量化 real-time 可行性 |
| P2 | 动机-评估 framing 对齐 | ✅ 高（writing fix） | 修复叙事逻辑缺口 |
| P2 | Spatial multi-seed | ⚠️ 中 | 强化 null result claim |
| P3 | 第二个 VLA backbone | ❌ 低（需大量实验） | 支撑 "Frozen VLAs" 复数 |
| P3 | Real-robot 实验 | ❌ 极低 | CoRL venue fit |

即使 P0-P1 全部完成，论文仍面临 "单 VLA backbone + sim-only + 低绝对性能" 的结构性限制。建议 Research Director 评估是否将目标 venue 调整为 CoRL Workshop 或改投 ICRA 2027/RSS Workshop 等对 simulation-only 分析类论文更友好的场所。
