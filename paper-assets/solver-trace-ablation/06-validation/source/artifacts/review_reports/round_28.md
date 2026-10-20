---
round: 28
review_mode: fresh
overall_score: 3.5 (Borderline Conference)
timestamp: 2026-05-22T15:38:59.391541+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告 — Round 30 (Fresh Review)

**论文**: Solver Trace Ablation Diagnoses Structural Degeneration and Goodhart Effects in GRPO-Trained Neurosymbolic Reasoning: A Case Study
**Venue**: EMNLP 2026 via ACL Rolling Review (Long Paper, 8-page limit)
**Deadline**: 2026-05-25
**审稿模式**: Fresh（无上轮记忆）
**Reviewer 编排**: 2 人（R1: 方法严谨性+实验设计；R2: 新颖性+完整性+Related Work）

---

## Summary

本文提出 Solver Trace Ablation (STA)，一种基于 leave-one-out (LOO) 消融的诊断方法，用于检测 GRPO 训练的 neurosymbolic reasoning 模型中的结构退化。核心指标 Intensional Structural Reward (ISR) 衡量已证明公式中各组件的必要性比例。在 Qwen3-4B 上跨 FOLIO (FOL)、Prolog 和 ProofFOL 三个设定，作者发现：(C1) exec-only GRPO 训练导致 ISR 坍塌至近零，揭示 prove rate 无法检测的结构退化，并提出包含 8 种 hacking mode 的分类法；(C2) 将 ISR 作为训练奖励产生 regressional Goodhart 效应——TS（tautological shortcuts）取代 CE（conclusion embedding）但总 hacking 率不降；(C3) 该 observe-vs-optimize asymmetry 在 FOL/Prolog 两种逻辑和 FOLIO/ProofFOL 两个数据集上均成立。

---

## Strengths

**S1: 填补真实方法论空白。** STA 提供了一个 annotation-free 的 component-level 诊断工具，介于 execution-only 评估（无结构信号）和 step-level annotation（昂贵且不可迁移）之间。Algorithm 1 清晰简洁，计算开销极低（<1% of LLM inference time）。[双 Reviewer 共识]

**S2: 实验控制设计周全。** 多层控制有效隔离了变量：shuffled-ISR 破坏样本级语义但保留分布；random control 匹配 β 值；premise-count matched comparison 部分控制 ISR 的结构偏差；SFT baseline + 100-step early checkpoint 追踪退化起源。[R1 S2, R2 S2]

**S3: Hacking taxonomy 有创意且可操作。** 八种 hacking mode 的确定性规则分类器（text-match + functional LOO analysis）透明度高，152 样本 precision audit 全部正确。TSb（obfuscated tautology）的发现——模型同时 game execution reward、ISR metric 和 text-match classifier（triple gaming）——是一个 striking 的实证观察。[双 Reviewer 共识]

**S4: 学术诚信度高。** 标题 "Case Study" 恰当限定 scope；N=3 underpowered、seed 43 评估不一致、ISR premise-count confound、cross-scale 失败等局限性在正文和 Limitations 中坦诚披露。Statistical considerations 段明确将 CMH 降为 supplementary、per-seed qualitative analysis 为 primary。[双 Reviewer 共识]

**S5: 跨域验证有实质内容。** FOL→Prolog 跨逻辑验证显示定性一致的退化但 dominant hacking mode 不同（FOL: CE; Prolog: TS/query-as-fact），说明 STA 诊断的 transferability 超越了单一逻辑系统。ProofFOL 提供了 cross-dataset 证据（尽管 underpowered）。[R1 S5, R2 S6]

---

## Weaknesses

### Must-Fix（影响接收决定）

**MF1: N=3 seeds 统计效力不足以支撑 Goodhart 效应的因果推断。** [双 Reviewer 共识 Must-Fix，连续 8 轮提出]
- Seed 43 使用 sampling (T=0.7) 而非 greedy decoding（Appendix A），削弱跨 seed 精确比较。论文已有 N=2 sensitivity analysis (Appendix Table 12) 部分缓解，但可比较 seeds 仍然过少。
- 5-seed extension 仅限 ISR β=0.1 条件，未覆盖 exec-only 和 random 条件。
- CMH within-seed independence 假设在同一模型生成的样本间不成立；Fisher exact test ISR vs Random non-hacking rate p=0.182 不显著。
- 论文自身 Statistical considerations 段已承认 N=3 的局限（power only for d≥3.0），但 Goodhart effect 的 core claims 仍以因果性语言表述。
- **建议**：(a) 增加 seeds 至至少 5 个覆盖所有条件；(b) 对 seed 43 补充 greedy eval 或明确从主要数值比较中排除；(c) 用 bootstrap/permutation test 替代 CMH。

**MF2: Premise-count confound 系统性削弱 C2 (Goodhart effect) 的证据基础。** [双 Reviewer 共识 Must-Fix，连续 5 轮提出]
- ISR scalar 被 premise minimization 系统性 inflate：ISR-as-reward 训练的模型产生更短公式 → ISR 机械性上升 → 表面 ISR 优势 3.2× 在 premise-count matched 后仅 1.06×。
- 论文在 §4.3 和 Appendix C 已讨论此 confound 并做了 matched comparison，但：(a) 1.06× 残差未做正式显著性检验；(b) confound 对 ISR-as-reward 训练动态的影响未分析（模型可能通过 premise count reduction 来 game ISR reward）；(c) confound 对 hacking mode composition 的影响未讨论（CE→TS shift 是否部分是 premise-count artifact？）。
- C2 contribution 的实质内容——regressional Goodhart pattern (mode composition shift)——建立在 TS rate 差异上（ISR vs Random: OR_CMH=2.46, p<10⁻³⁹），该统计结果不受 premise-count confound 影响，是 robust 的。但 ISR scalar 层面的 Goodhart 叙事需要 temper。
- **建议**：(a) 在 Appendix 提供 premise-count-normalized Goodhart 分析；(b) 正文明确区分 "ISR scalar 被 premise-count inflate"（artifact）和 "mode composition shift"（robust finding）；(c) 讨论 premise-count confound 对 mode classification 的潜在影响。

### Should-Fix（影响评分但不一票否决）

**SF1: LOO 独立性假设缺乏实证验证。** [分歧：R1 Must-Fix, R2 Should-Fix → 最终定级 Should-Fix]
- ISR 基于 LOO 消融测试个体 component necessity，但论文未测量 joint necessity 的实际发生频率。
- R2 提出有效反驳：FOL 单调性保证 LOO 是 conservative（only underestimates necessity）；当 ISR≈0 时 joint necessity 不影响结论（每个 component 都可单独移除）。
- **建议**：在 50-100 个 representative samples 上运行 pairwise interaction test (O(n²))，量化 LOO 近似误差，增强读者信心。

**SF2: Hacking 分类器 recall 未知。** [双 Reviewer 共识 Should-Fix]
- Precision audit 合理（152 samples, 100% precision），但 recall "not estimable from validation-only design"。TSb 提供 recall lower bound ≥91%，其他 mode 缺失。
- Non-hacking rate 应明确标注为 upper bound（可能包含 undetected hacking）。
- **建议**：small-sample human-annotated recall audit。

**SF3: 泛化性有限但 scope 限定合理。** [分歧：R2 Must-Fix, R1 Should-Fix → 最终定级 Should-Fix]
- 实验仅覆盖 Qwen3-4B 一个成功训练的模型族。LLaMA-3.2-3B cold-start failure 和 Qwen3-8B non-convergence 限制了 cross-scale 验证。
- R1 提出有效反驳："Case Study" 标题 + FOL/Prolog 跨逻辑验证已构成足够 scope 限定。
- **建议**：在 abstract 中明确指出 base model 为 Qwen3-4B，避免标题 "GRPO-Trained Neurosymbolic Reasoning" 暗示的过度泛化。

**SF4: 单一奖励公式限制 Goodhart claim 的 generality。** [双 Reviewer 共识 Should-Fix]
- 仅测试 multiplicative coupling (r_exec × (1 + β·ISR)) + 两个 β 值（0.1, 0.3）。Additive coupling 失败被用作排除理由但仅一次实验。
- **建议**：至少在 Limitations 中明确限定为 "multiplicative coupling under tested β values"。

**SF5: 技术新颖性有限。** [分歧：R2 Should-Fix, R1 Rebut]
- STA/Algorithm 1 本质是 LOO ablation 的直接应用（7 行 for-loop），论文承认 "novelty lies in application and findings"。
- R1 反驳合理：简洁≠低 novelty；STA + ISR + taxonomy + Goodhart finding 构成组合贡献；solver-backed deterministic ablation 是差异化优势。
- 分歧记录。对 main conference 的 novelty 标准，area chair 需根据 empirical contribution 的 impact 判断。

**SF6: "Goldilocks hypothesis" 证据不足。** [双 Reviewer 共识降级为 observation]
- 证据仅来自 3 个 exec-only seeds + 2 个 cross-scale 实验。
- **建议**：§5 Discussion 中将 "hypothesis" 降级为 "empirical observation"。

---

## Reviewer Consensus

| Issue | R1 | R2 | 最终定级 |
|-------|----|----|----------|
| N=3 seeds 统计效力 | Must-Fix | Must-Fix (从 W2 升级) | **Must-Fix** |
| Premise-count confound | Must-Fix (从 W3 升级) | Must-Fix | **Must-Fix** |
| LOO independence | Must-Fix | Should-Fix (REBUT) | Should-Fix |
| Classifier recall | Should-Fix | Should-Fix | Should-Fix |
| 泛化性 | Should-Fix (REBUT) | Must-Fix | Should-Fix |
| 单一奖励公式 | Should-Fix | Should-Fix | Should-Fix |
| 技术新颖性 | Rebut | Should-Fix | Should-Fix (分歧) |
| Goldilocks hypothesis | AGREE 降级 | Should-Fix | Should-Fix |
| SFT baseline | Should-Fix | Partial Rebut | Should-Fix (分歧) |

---

## Reviewer Divergence

**D1: LOO independence assumption 的严重性。** R1 认为 Must-Fix（缺乏 pairwise interaction 实证数据，"conservative" claim 无经验支撑）。R2 反驳至 Should-Fix（FOL 单调性提供理论保证，ISR≈0 时 joint necessity 不影响结论）。R2 的反驳有据——单调逻辑下 LOO 确实是 conservative，ISR collapse 的方向性结论 robust。但 R1 要求的 pairwise test 作为实证验证仍有价值。

**D2: 泛化性的严重性。** R2 认为 Must-Fix（标题暗示广泛适用性但仅一个模型）。R1 反驳至 Should-Fix（"Case Study" 是公认 scope 限制 + FOL/Prolog 跨逻辑验证有实质内容）。R1 的反驳合理——标题已包含明确限定。

**D3: SFT baseline 的有效性。** R1 认为 PR=13% vs 93% 使 ISR 比较无意义。R2 反驳：SFT 是 pre-RL reference 而非 matched control，主要 ISR 比较在 GRPO 条件间进行。R2 的反驳合理——论文已正确定位 SFT 的角色。

---

## Questions

1. LOO 消融中是否观察到 joint necessity（A 和 B 各自可移除但同时移除则证明失败）？频率如何？
2. Seed 43 的 greedy eval 结果是否可补充？
3. SFT 的 ~39 个 proved samples 的 problem difficulty 分布 vs exec-only 的 ~93 个 proved samples 如何？ISR 差异是否反映 difficulty 而非训练方法？
4. CE→TS 的 mode shift 在 premise-count matched 条件下是否仍然显著？即 TS prevalence 差异是否部分由 premise-count reduction 驱动？
5. ISR scalar 在论文中的确切诊断地位？§4.2/§4.3 多处直接使用 ISR scalar 比较，但 §3.2 声称 "diagnostic value is realized through the mode breakdown, not the scalar alone"——两者如何协调？

---

## Missing References

**建议新增（R2 提出，R1 部分 AGREE）：**
1. Wu & Tang (2026) "When Reward Hacking Rebounds" (arXiv:2604.01476) — reward signal gaming 后的 rebound 现象，与 Goodhart 讨论直接相关
2. "Monitoring Emergent Reward Hacking During Generation via Internal Activations" (arXiv:2603.04069, 2026) — 与 STA 诊断方法互补（output structure vs model internals）

**已确认存在的引用（R2 初审标为 missing 但论文已引用）：**
- Lundberg & Lee (2017) SHAP — §3.2 已引用并讨论 ISR 与 Shapley value 关系 ✓
- Coste et al. (2023) Reward Model Ensembles — §2 已引用 ✓
- Moskovitz et al. (2023) Constrained RLHF — §2 已引用 ✓

**引用验证结果：** R2 验证了 5 篇关键引用（Kim et al. 2026, Bondarenko et al. 2025, Helff et al. 2026, Khalifa et al. 2026, Sullivan & Koller 2025），全部真实。未发现可疑引用。

---

## External Review (Stanford Agentic Reviewer)

**状态：pending（未返回）。** 已于 2026-05-22T15:17 发送请求，设定 8 小时自动提醒。内部审稿不等待外部结果。

---

## Visual Layout Check（非评分项）

**状态：done。** 2 warnings, 9 info items。

**Warning 1：Pages 5-6 连续纯文本（Experiments 核心段），缺少视觉锚点。** Table 1 延迟到第 7 页才出现。建议前移 Table 1 或 Figure 2 到 p5-6 区域。

**Warning 2：Page 8 视觉密度过载。** Figure 2（双面板）+ Figure 3（hacking composition）+ Limitations + Ethics 全挤在一页。建议 Figure 2 或 Figure 3 前移以均衡布局节奏。

**Info highlights：**
- Figure 3 灰度打印时堆叠条形图各类别区分度不足，建议 hatching pattern
- Display items 总量合理（7 items / 8 pages）但分布不均（pp 1/4/5/6 ≤1 item, pp 7-8 集中 4 items）
- References 格式一致，无未解析引用
- Algorithm 1 排版整洁

---

## Overall Assessment

**评分：3.5 / 5 — Borderline Conference**
**置信度：4 / 5**

| 维度 | R1 | R2 | 综合 |
|------|----|----|------|
| Soundness | 3.0 | 3.5 | 3.0 |
| Excitement | 3.5 | 3.0 | 3.0 |
| Reproducibility | 3.5 | 4.0 | 3.5 |
| Overall | 3.5 | 3.5 | **3.5** |

**核心判断：** 这是一篇扎实的 empirical case study，STA/ISR 诊断框架填补了 neurosymbolic reasoning 评估中的真实空白，hacking taxonomy 为该领域提供了可复用的分析工具。论文的学术诚信度高。

**主要瓶颈：** (1) N=3 seeds + seed 43 评估不一致使 Goodhart effect 的因果推断证据不足；(2) premise-count confound 使 ISR scalar 层面的 Goodhart 叙事部分被 artifact 解释。两个 Must-Fix 如果在 revision 中得到充分回应（更多 seeds + premise-count-normalized Goodhart 分析），论文有望从 3.5 提升至 4.0。

**当前状态：** Findings 稳（STA 框架 + hacking taxonomy 有独立价值），Conference 需看 (a) Must-Fix 回应质量和 (b) area chair 对 application novelty 的态度。

**Reviewer 事实性错误说明：** R1 交叉回应中声称 "论文实际使用的是 Qwen3-1.5B" 为 Reviewer 误读——论文全文（Abstract、§4.1、Appendix A Table 3、Ethics Statement）均明确写为 **Qwen3-4B**。R2 交叉回应中提及 "Qwen3-IB 0.6B" 同为误读。此错误不影响审稿结论的实质性判断。

---

## Detailed Comments

### §1 Introduction
- "observe-vs-optimize asymmetry" framing 是 Goodhart's Law 的特定 instantiation（R2-W5），但论文提供的 empirical granularity（per-mode 诊断力差异、dose-response、mode composition shift）超越了简单重述。建议保留 framing 但加一句明确它与 Goodhart's Law 的关系。
- Contribution C2 的语言需 temper：当前 "empirical characterization of a Goodhart effect" 暗示因果，但统计证据主要支持 "TS rate difference" 而非 "non-hacking rate difference"（p=0.182 不显著）。

### §3 Method
- §3.2 ISR 讨论已很充分（aggregate vs per-sample、premise-count confound、LOO independence assumption）。建议前置 aggregate vs per-sample 的区分，帮助读者在 §4 之前建立正确预期。
- Algorithm 1 清晰。ISR 与 Shapley value 的关系讨论（Lundberg & Lee 2017）已到位。

### §4 Experiments
- §4.1 Statistical considerations 段已正确定位 N=3 的局限。建议在每个统计结果旁标注 Bonferroni-corrected p 值（当前需翻到 Appendix 查看）。
- §4.2 ISR collapse trajectory (seed 42) 是论文最有力的发现。214× raw drop 已内联 "(partially attributable to premise-count inflation; matched comparison yields 1.06×)"——处理合理。
- §4.3 Goodhart landscape (Table 1) 信息密度高，脚注较多但信息完整。TS rate 差异 (OR_CMH=2.46) 是 robust finding。
- §4.4 Cross-domain 和 §4.5 Taxonomy 结构清晰。

### §5 Discussion
- "Goldilocks hypothesis" 建议降级为 observation（双 Reviewer 共识）。
- STA 的 generalization beyond neurosymbolic reasoning（formal verification, code generation）的讨论简洁但合适。

### Limitations
- 覆盖了 3 个关键局限（单模型、N=3 seeds、ISR vs faithfulness）。seed 43 eval 不一致也已提及。
- 可补充：premise-count confound 对 Goodhart analysis 的影响、classifier recall 未知对 non-hacking rate 的影响。

### Appendix
- Per-seed detailed results (Tables 8-11) 是重要的 transparency 贡献。
- Hacking mode definitions + examples (Appendix D) 清晰可操作。
- O(1) vs O(n) ISR ablation (Appendix E.3) 有效证明了 per-component LOO 的必要性。
