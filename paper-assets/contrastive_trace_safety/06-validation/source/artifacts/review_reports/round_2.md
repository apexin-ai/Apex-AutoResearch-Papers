---
round: 2
overall_score: borderline
timestamp: 2026-05-17T11:50:53.914136+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告 — Round 3

**论文**: "Temporal Probing for Safety Commitment Detection in Reasoning Models"
**Venue**: EMNLP 2026 via ARR May cycle (Deadline: 2026-05-25)
**Reviewers**: R1 (方法严谨性+实验设计) + R2 (新颖性+完整性+写作质量)
**外部审稿**: 未请求（项目无 external_review 配置）

---

## Summary

本文首次系统评估了推理模型中 safety commitment point 检测的两种信号模态（hidden-state probes vs text monitors），覆盖 4 个模型（R1-8B, OT-7B, R1-32B, QwQ-32B）、2 种架构（Llama, Qwen）、2 种训练方法（R1 distillation, STILL）、2 种规模（7-8B, 32B）。核心发现：temporal windowing 提供 universal gains；HS probe 优势在 7-8B 显著（5/12 tests 通过 Holm-Bonferroni），在 32B 消失。全面的负面结果（BOCPD、Mahalanobis distance、cross-model transfer 均失败）定义了当前方法边界。

---

## Strengths

1. **研究问题定义精准有实际意义**：在多步推理中检测 safety commitment，应读 hidden states 还是 text？问题清晰、动机明确、对 deployment safety monitoring 有直接指导价值。
2. **实验设计控制变量严谨**：4 模型覆盖 2×2×2 design space，OT-7B 的引入帮助解耦 architecture/training/scale confound。同一条件下两种 modality 使用相同 W 做公平比较。
3. **统计方法论审慎**：Holm-Bonferroni 12-test correction、metric 间相关性坦诚讨论（|r|=0.42-0.69）、每个 p-value 配 effect size、paired permutation test on trace-level values。
4. **负面结果系统报告有领域导向价值**：TrajGuard fails on reasoning models、BOCPD/CUSUM fails because commitment is gradual、cross-model transfer fails entirely——指明了哪些方向不可行。
5. **科学透明度高**：Appendix F bug disclosure 主动披露 QwQ-32B text probe 初始化 bug，所有 reported numbers 为修正后结果。
6. **Control task 验证规范**：Hewitt & Liang (2019) selectivity framework + position-only baseline，4 模型均 >5pp threshold。
7. **Temporal windowing finding 有实践价值**：作为 practitioner-friendly takeaway，"无论 modality 选择如何，增加时间窗口是最稳健的设计默认"在所有条件下一致成立。

---

## Weaknesses

### Critical（影响接收决定）

**[W1] Contribution 1 overclaim: "temporal dominates modality" 在 7-8B 不成立 [共识]**
- Introduction Contribution 1 宣称 "The bottleneck in commitment detection is temporal, not informational"
- 实际数据：R1-8B modality gap +22.4pp precision > temporal gain +12.9pp；OT-7B modality gap +21.2pp > temporal gain +6.1pp
- "Temporal dominates" 仅在 32B 成立（modality gap 不显著），不是 universal finding
- Introduction 声称 "counterintuitive" 进一步构成 overclaim——expanding input window improving classification 是标准 ML 预期
- **必须修改**：重写为 "Temporal context provides universal gains; modality remains dominant at 7-8B; scale determines which factor dominates"

**[W2] Negative results 仅在 R1-8B 验证但结论泛化到所有模型 [共识]**
- BOCPD/CUSUM full sweep (Table 5, Appendix E) 和 Mahalanobis distance 仅覆盖 R1-8B
- Contribution 3 和 Section 6 使用全称判断："safety commitment is gradual rather than abrupt"
- QwQ-32B 的 optimal layer 在 3.1% depth（与 R1-8B 44% 完全不同），transition dynamics 可能本质不同
- **必须修改**：至少在一个额外模型上验证，或严格限定 claim scope

**[W3] Layer selection metric（accuracy × crossing rate）缺乏论证 + OT-7B 矛盾 [共识]**
- 未解释为什么用乘法而非其他复合方式（加法、带约束优化等）
- OT-7B Table: layer 0 score 35.5 > layer 16 score 21.8，但选了 layer 16——暗示 bug 修复后更改了 criterion 但未声明
- QwQ-32B 因此选到 layer 2 (3.1% depth)，Section 5.4 承认该层 "encodes primarily positional features"
- 如果替换 criterion，scale-dependent narrative 可能改变
- **必须修改**：(1) 提供 metric justification 或 ablation；(2) 解释 OT-7B 矛盾；(3) 报告 QwQ-32B alternative layer 结果

### Warning（影响评分但不一票否决）

**[W4] 纯 empirical study 无新方法，main track 竞争力存疑 [分歧]**
- R2: critical（所有方法均为现有直接应用）
- R1: rebut（ARR 接受 empirical benchmark studies，benchmark 贡献有独立价值）
- 共识：main track 竞争力不足，Findings track 更合适

**[W5] 32B 统计功效不足以支撑 "scale-dependent" claim [共识]**
- R1-32B (n=20) precision +9.4pp (p=0.050) 同方向 effect，non-significance 可能反映 power 不足
- QwQ-32B +5.7pp (p=0.346) 才是 genuine null
- 两个 32B 模型证据不一致不足以支撑 "scale as primary moderator"
- 建议：R1-32B 标为 inconclusive，不归入 "no significant advantage"

**[W6] Text encoder confound (MiniLM 384d vs HS 3584-5120d) 未在结论中 qualify [共识]**
- W=15 时 HS 61440d vs text 5760d (10:1)
- Limitations 已讨论但 Contribution 2 未加 qualifier
- Coverage 差异（text 95.4% vs HS 72.1%）可能导致 precision-undefined trace 排除的系统性偏差
- 建议：Contribution 2 加 "under current text encoder choice" qualifier

**[W7] GRU 评估协议不一致 [分歧]**
- R1: critical（main text +4.5 vs Appendix 7.0 步 lead，浮动 60%，影响 oracle gap 计算）
- R2: warning（不同 split 已声明，variance 是 GRU 固有特征，不改变 "enormous gap" 定性结论）
- 共识：main text 70/30 split 的 per-seed 结果应补充

**[W8] Cross-model transfer claim overclaimed (PCA ≠ alignment) [共识]**
- PCA 是 dimensionality reduction 而非 alignment，Procrustes/CCA/learned map 均未尝试
- "Safety representations are model-specific" 过强，应限定为 "PCA-based transfer fails"

**[W9] QwQ-32B position baseline (70.6%) > HS probe (67.8%) [共识]**
- Position 比 HS probe 更 informative 意味着 layer 2 选择本身有问题
- 与 W3 (layer selection) 强耦合——更深层可能改变结果
- Selectivity 15.3pp 确认 learned structure，但实用价值存疑

**[W10] Related Work 遗漏 5 篇 2025-2026 高相关论文 [共识，Director 已验证]**
- Zhang et al. 2025 (arXiv:2504.05419): probing reasoning model hidden states for correctness — 方法论高度重叠
- Luo et al. 2026 (arXiv:2603.17305, CRAFT): contrastive hidden-state alignment for reasoning safety
- Zhou et al. 2025 (arXiv:2502.12659): R1 safety assessment — 背景必引
- arXiv:2604.18946 (AltTrain): reasoning structure + safety alignment
- arXiv:2603.17368: pre-CoT safety decision-making
- 另需补充 Li et al. 2024 (Inference-Time Intervention)

**[W11] Precision-undefined trace 排除未做偏差分析 [共识]**
- 未报告排除了多少 traces
- HS/text coverage 差异（72.1% vs 95.4%）导致不同 traces 被排除，可能系统性放大 modality gap

### Info（不影响接收）

**[W12] Abstract 仍含 7+ 统计量，叙事性弱** — 建议保留 2-3 关键数字
**[W13] "Temporal context dominates" 全文重复 7+ 次** — 每 section 应用不同角度
**[W14] 轻微 AI 写作痕迹** — -ing phrase 结尾多处出现，不严重

---

## Reviewer Consensus [AGREE]

1. **Contribution 1 需要重写**：数据不支持 "temporal dominates modality" 的无条件表述（7-8B 上 modality gap > temporal gain）
2. **Negative results 需要多模型验证**：单模型泛化结论不可接受
3. **Layer selection 需要论证和消融**：当前 metric 无 justification 且 OT-7B 存在矛盾
4. **32B "scale-dependent" claim 需要 qualify**：R1-32B 是 inconclusive 而非 null
5. **Findings track 是合适的定位**：实验执行质量高但 contribution novelty 不足 main track
6. **Text encoder confound 需要 qualifier**：Contribution 2 应注明 encoder choice 的影响
7. **Missing references 需要补充**：5 篇 verified 高相关论文（特别是 Zhang et al. 2025）

## Reviewer Divergence [REBUT]

1. **新颖性是否构成 reject 理由**
   - R2: "temporal context helps" 是 trivially expected，纯 empirical study 应 reject
   - R1: temporal gain 的 universality vs modality advantage 的 inconsistency 不是 trivially expected；text probes 从 temporal context 获益更大支持机制性解释；ARR 接受 benchmark studies
   - **Director 判断**：R1 论证更有力。"Universal gain vs conditional advantage" 的对比确实超越简单的 "more features = better"。但 "counterintuitive" framing 确实不当。

2. **GRU 协议不一致严重性**
   - R1: critical（oracle gap 计算基础不牢）
   - R2: warning（variance 是固有特征，定性结论不变）
   - **Director 判断**：R2 更合理——77% vs 89% 的 gap 范围不改变 "enormous gap" 结论，降为 warning。

3. **跨模型 W confound (R1-W8)**
   - R1: 不同 W 使跨模型 modality gap 不可比
   - R2: within-model comparison 是 matched 的，gap 一致性构成 replication evidence
   - **Director 判断**：R2 有效反驳。每个模型内 HS/text 用相同 W，precision gap 的跨模型一致性是合法的 replication argument。

---

## Questions（需作者澄清）

1. OT-7B layer sweep: Layer 0 score (35.5) > Layer 16 (21.8)，为什么最终选了 layer 16？Bug 修复后 selection criterion 是否改变？
2. 在 7-8B 上 modality gap > temporal gain，"temporal dominates" 在什么 interpretation 下成立？
3. QwQ-32B layer 2 (3.1% depth) 的 probe 与 R1-8B layer 14 (44% depth) 是否本质上是不同类型的 classifier？可否有意义地做 modality comparison？
4. Safe trace FPR 39-62% 远高于 jailbreak pre-CP FPR 4.83-32%，原因是什么？
5. MiniLM-L6-v2 (384d) 选择的理由？是否测试过更强 encoder？
6. Oracle gap 比较中 oracle 用 K=5、method 用 K=1 是否构成 fair comparison？

---

## Missing References（已验证真实）

| 论文 | 相关性 | 优先级 |
|------|--------|--------|
| Zhang et al. 2025, arXiv:2504.05419 — Probing Hidden States for Self-Verification | 方法论直接重叠 | Must-cite |
| Luo et al. 2026, arXiv:2603.17305 (CRAFT) — Contrastive Reasoning Alignment | Contrastive hidden-space 直接相关 | Must-cite |
| Zhou et al. 2025, arXiv:2502.12659 — Hidden Risks of R1 | R1 安全背景 | Should-cite |
| arXiv:2604.18946 (AltTrain) — Reasoning Structure + Safety | 相关方法 | Should-cite |
| arXiv:2603.17368 — Pre-CoT Safety Decision | 补充视角 | Should-cite |
| Li et al. 2024 — Inference-Time Intervention (ITI) | HS intervention precedent | Should-cite |

---

## Overall Assessment

**Score: borderline (weak reject / weak accept boundary)**

**推荐定位: Findings track weak accept**

**置信度: 4/5**

**理由**：
- 研究问题有价值，temporal windowing 的 universal gain finding 在所有模型一致可复现，对 practitioner 有直接指导意义
- 实验执行质量高、统计严谨、透明度佳
- 但核心 contribution framing 存在 overclaim（W1）、negative results 缺多模型验证（W2）、layer selection 缺论证（W3）
- 纯 empirical study 无新方法在 main track 竞争力不足（R1/R2 共识定位 Findings）
- 32B "scale-dependent" claim 基于不充分证据（n=19-20, effect 方向不一致）

**如果作者修复 W1-W3（重写 contribution framing + 至少一个额外模型验证 negative results + layer selection 论证/消融），论文可升至 Findings track accept。**

---

## Detailed Comments

### Section-by-Section

**Abstract**: 内容密度高但统计量过多（7+数字在 191 words 中）。建议保留 temporal gain range + scale-dependent pattern 的 2-3 个关键数字，其余移入正文。删除 "counterintuitive" 暗示。

**Introduction**: 叙事线清晰但 Contribution 1 与 Section 5 数据不一致。"The bottleneck is temporal, not informational" 在 7-8B 不成立。建议改为 "Temporal context provides the most robust, universal improvement" 而非与 modality 做排他性对比。

**Related Work**: 6 段主题式结构覆盖合理，但 2025-2026 reasoning model safety 文献有 5 篇 verified 遗漏。特别是 Zhang et al. 2025（同样 probe reasoning model hidden states）必须讨论并明确 positioning。

**Method (Section 3)**: Layer selection metric (accuracy × crossing rate) 是核心缺陷——无 justification，OT-7B 选择存在矛盾，QwQ-32B 因此选到 essentially positional layer。需要 metric ablation。

**Experiments (Section 5)**: 总体设计严谨。主要问题：(1) negative results 仅 R1-8B；(2) GRU 两套协议数字差异大；(3) precision-undefined trace 排除未分析偏差。

**Discussion + Conclusion (Section 6)**: 已合并但核心 finding 仍过度重复。"Temporal context dominates" 在 Abstract/Intro/Contributions/Section 5.1/5.2/Section 6 中出现 7+ 次。建议 Section 6 聚焦 implications + limitations + future work，不再重述数字。

**Limitations**: 全面诚实，覆盖了 power/causality/CP-definition/FPR/encoder/architecture diversity。但 text encoder confound 的讨论应 propagate 到 Contribution 2 的 qualifier。

**Appendix**: 信息密度高（A-G 共 7 个 appendix section）。Transfer 实现（Appendix G）现已详尽但 claim 需 scope down。Bug disclosure (Appendix F) 值得称赞。

### 对比前轮（Round 1-2）改进评估

Round 1-2 的关键问题修复情况：
- ✅ 模板/格式问题全部修复
- ✅ Meta-analysis 问题已修复（改为 per-model reporting）
- ✅ Control task 已完整实现
- ✅ 多重比较校正已恰当实施
- ✅ HS 提取/text baseline 描述已清晰
- ⚠️ Contribution framing 改善但仍存在 overclaim（从 "universally" → "temporal dominates" 但仍不准确）
- ⚠️ Related Work 从 14→32 篇但仍有遗漏
- ⚠️ 32B power 问题持续存在（结构性限制）
- ❌ Layer selection metric 问题新暴露且为 critical（Round 1 修复了 implementation bug 但未解决 metric justification）
- ❌ Negative results 单模型泛化问题首次在本轮作为 critical 提出