---
round: 4
overall_score: borderline
timestamp: 2026-05-18T02:05:46.636733+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 圆桌审稿报告 — Round 5

**论文**: "Vision Encodes, Language Routes: Token-Level Functional Specialization in a Vision-Language-Action Model"
**Venue**: CoRL 2026 (Paper deadline: 2026-05-29, double-blind, 8pp + refs + appendix)
**Reviewers**: R1 (方法/实验严谨性), R2 (新颖性/意义 + 相关工作 + Framing)
**交叉回应**: 完成。R2 对 R1 全部 AGREE; R1 对 R2 有 7 AGREE + 2 partial REBUT（C1 框架独立价值、引用数量 vs gap）。共识程度高。

---

## Summary

论文对 OpenVLA-7B 在 LIBERO 上进行了系统性 token 级表征分析，使用 trained/pretrained/untrained 三条件 factorial 设计结合四种互补方法（cross-instruction probes, attention analysis, RSA, functional probes）。核心发现是 VLA fine-tuning 将 instruction routing 从 mid-depth (L9-L16) 前移至 entry-exit pattern (L0-L1, L31)，效果集中在 readout token (+0.069 R², +46pp attention) 而非 image tokens。论文方法论系统、统计分析充分、对 metric dependence 坦诚报告。与 Round 4 相比，C1 reframe、RSA qualifier、50-demo ablation 等 critical issues 已修复，但出现新的方法论问题（ablation per-head normalization、probe overparameterization 误解读）。

---

## Strengths

1. **系统性四分析方法 + 三条件控制**：cross-instruction probes × attention × RSA × functional probes，交叉 trained/pretrained/untrained × instruction presence，是 VLA 分析文献中首个此级别的系统化框架。（R1+R2 共识）
2. **C2 routing finding 有真正新颖性**：三条件 routing gradient (0/32 → 9/32 → 24/32 heads at L1) + entry-exit vs mid-depth pattern 的发现，是 genuine empirical contribution。Grant et al. 2026 做 feature-level analysis，本文做 token-level + layer-level decomposition，深度互补。（R2 强调）
3. **统计严谨性和 robustness 分析充分**：Bootstrap CIs (10,000)、LOOCV、permutation tests、distance metric invariance (r > 0.989)、seed sensitivity (0.655 ± 0.002)、demo subsampling (r = 0.97)、threshold sensitivity (30%-70%)、cross-benchmark (LIBERO-Spatial)、FDR correction (Benjamini-Hochberg, 29-30/33 layers)。（R1 确认）
4. **Metric dependence 坦诚报告**：CKA 与 RSA 分歧在 Abstract、Method ("Why RSA over CKA")、Appendix 中均如实呈现，增强可信度。（R1+R2 共识）
5. **Round 4 critical issues 实质性修复**：C1 reframe 到位、50-demo ablation 消除 underfitting confound、RSA qualifier 全面、FDR correction 已应用、straw man 已消除、头数统一为 24/32。（R1+R2 共识）
6. **写作质量高，AI 痕迹极少**：无 em-dash、无 AI 典型用词、结构清晰。（R2 确认）

---

## Weaknesses（按严重性排序）

### Critical（影响接收决定，全票共识）

**W-Critical-1: L1 Ablation 的 "3.5× specificity" claim 在 per-head normalization 后仅剩 ~15% excess**
- 位置：Section 4.2, experiments.tex lines 78-82
- 问题：Ablating 24 dominant heads → +0.059 R²; ablating 8 non-dominant heads → +0.017。论文声称 "3.5× smaller" 证明 graded specificity。Per-head: dominant = 0.059/24 ≈ 0.00246, non-dominant = 0.017/8 ≈ 0.00213，差异仅 ~15%。外推 24 heads at non-dominant rate = 0.051，观测 0.059，excess 仅 0.008 (16%)。
- 影响：这是 C2 "VLA fine-tuning front-loads instruction routing" 的唯一因果证据。"3.5×" 混淆了 head 数量差异和 per-head specificity。
- 缓解因素（R2 补充）：layer confinement (L1: +0.059, L8: +0.018, L13: ≈0) 不受 head 数量 confound，是更干净的 specificity 证据。
- **修复方案**：(a) 报告 per-head normalized effect size; (b) 弱化 "3.5×" 为 aggregate comparison; (c) 将 layer confinement 作为 specificity 主要证据; (d) 理想情况补充 random-subset ablation (随机 24/32 heads, k 次)。
- **全票共识 (R1 critical, R2 AGREE)**

**W-Critical-2: N/params ≈ 0.06 被错误解读为 "ensuring adequate training signal"**
- 位置：Section 4.1, experiments.tex line 12
- 问题：MLP probe (4096→256→7) ≈ 1.05M params, N = 63,228。N/params ≈ 0.06 意味着参数量是数据量的 ~17 倍，是严重 overparameterized regime。Belinkov (2022) 指出高容量 probe 可从任何表征 decode 信息。论文称此 ratio "ensuring adequate training signal" 是错误的。
- 缓解因素：(a) 使用 early stopping (patience 5)；(b) 核心 claims 基于 Δ 而非 absolute R²，Δ 不受 absolute inflation 影响（假设 overfitting degree 跨条件相似）；(c) seed sensitivity < 0.01 std。
- **修复方案**：(a) 修正措辞为 "probe is overparameterized; we rely on early stopping"; (b) 补充 linear probe 或 small MLP (64 hidden) baseline; (c) Method 中引用 Belinkov 2022 讨论 probe complexity-capability tradeoff。
- **全票共识 (R1 critical, R2 AGREE)**

### Warning（影响评分，全票或多数共识）

**W-Warning-1: 单模型 scope 对 C2 generalizability 的约束 + Limitations 讨论不够具体**
- Discussion 以架构类推（RT-2, π₀）论证潜在 generalizability，但类推不等于验证：RT-2 用 PaLM-E，π₀ 用 flow matching。Grant 2026 在 6 VLAs 上分析表明 cross-model 验证可行。
- Contributions list 已限定 "demonstrated on OpenVLA-7B/LIBERO"，但 Limitations 应具体列举可能改变 routing 的架构变量（backbone size/family, decoder type, frozen vs unfrozen encoder, projector arch, pretraining data）。
- **R2 标 critical, R1 倾向 strong warning（scope 已限定）。合并为 warning。**

**W-Warning-2: Discussion "Architectural implications" 的 early-layer fine-tuning suggestion 属 speculative leap**
- probe R² 变化 ≠ behavioral performance 变化。L31 也有 18 heads instruction-dominant，直接矛盾 "only early-layer" 暗示。论文自己承认 "requires task-level evaluation beyond this work"。
- **修复**：弱化 "suggests" → "raises the hypothesis"；标注 speculative；讨论 L31 complication。
- **全票共识 (R2 critical, R1 AGREE → 合并为 warning，因措辞已部分 hedged)**

**W-Warning-3: Pretrained Llama-2 condition 的 OOD confound 未讨论**
- Llama-2 base 从未见过 projected visual tokens (DinoSigLIP 4096-D)。9/32 instruction-dominant heads 可能反映 OOD 输入下的 default attention fallback，而非 language pretraining 对 instruction routing 的真正 "seeding"。
- 影响 C2 叙事："language pretraining seeds routing, VLA fine-tuning amplifies it" 可能 too clean。
- **全票共识 (R1 提出, R2 AGREE)**

**W-Warning-4: Bootstrap CI 缺具体 [lower, upper] 数值**
- RSA best-vs-best Δ=+0.017 及多处核心数据仅标 "CI incl. 0" / "excl. 0"，未给区间。LIBERO-Spatial 有完整 CI [0.012, 0.036]，主实验的缺失更显眼。
- **全票共识 (R1 提出, R2 AGREE)**

**W-Warning-5: C3 non-monotonic observation 在 Abstract/Intro 权重过高**
- RSA inverted-U 在 CKA 下不成立（monotonic increase），不应与 C2 等权呈现。当前 Abstract 中 C3 获得与 C1/C2 等量篇幅。
- **修复**：缩减 C3 Abstract 篇幅或将 metric divergence 前置。
- **全票共识 (R2 提出, R1 AGREE)**

**W-Warning-6: Related Work 缺 causal tracing / activation patching + tuned lens**
- 缺 Meng et al. 2022 (NeurIPS, "Locating and Editing Factual Associations in GPT") — 与 L1 ablation 方法论直接相关
- 缺 Belrose et al. 2023 (tuned lens) — 与 per-layer probing 紧密相关
- 当前 29 citations，补充后 ~31-33，引用密度合理。
- **全票共识 (R2 提出, R1 AGREE)**

### Info（低严重性）

**I1**: conclusion.tex 存在但未被 main.tex `\input`。Discussion 以 Limitations 收尾，叙事以消极信息结束。（R4-I1 仍未修复）
**I2**: Appendix A.6 single-seed three-condition analysis 应补 3+ seeds（main results 有 5-seed sensitivity）。
**I3**: Abstract 渲染后词数可能超 250 words（raw LaTeX ~241）。
**I4**: -ing 分词短语约 15+ 处（", enabling/indicating/confirming/suggesting..."），密度偏高但不构成严重问题。

---

## Reviewer Consensus [AGREE]

所有 Reviewer 达成共识的关键判断：
1. **Ablation per-head normalization 是新发现的最大方法论问题**——"3.5× specificity" 在归一化后仅 ~15% excess，C2 因果证据被削弱（但 layer confinement 提供替代 specificity 证据）
2. **Probe overparameterization 的错误解读需修正**——措辞错误但有缓解因素（early stopping, Δ claims）
3. **单模型 scope 是最大的 significance 限制**——Contributions 已限定 scope，但 Limitations 讨论不够具体
4. **Design implications 缺乏 behavioral validation 属 speculative**——当前措辞部分 hedged 但仍 overcommitted
5. **Round 4 的 3 个 critical issues (C1 reframe, RSA qualifier, 50-demo ablation) 全部实质性修复**
6. **写作质量高，统计报告整体透明**

---

## Reviewer Divergence [REBUT]

| 分歧点 | R1 立场 | R2 立场 | 最终处理 |
|--------|---------|---------|----------|
| 单模型 severity | strong warning（scope 已限定） | critical（generalizability 根本约束） | warning（Intro 已限定 scope，但 Limitations 需更具体） |
| C1 框架独立价值 | 有独立方法学贡献（REBUT R2-W1） | 混合框架+验证，验证部分说服力有限 | 保留 R2-W1 为 info — 措辞可改进但不影响接收 |
| Quality 评分 | 3/5（ablation N1+N2 严重） | 3.5/5（statistical apparatus 加分） | 取中间值 3.25/5 |
| 引用数量 | 数量不是问题，gap 是问题（REBUT R2-I3） | 29 篇中等偏低 | 采纳 R1 判断——补充 W6 指出的 gap 后 ~31-33 篇，量级合理 |

---

## Questions（需作者澄清）

1. **[R1-Q1, R2 AGREE]** 能否提供 random-subset ablation（随机抽 24/32 heads ablated，重复 k 次）的 R² 分布？这是明确 dominant-head specificity 的 gold standard。
2. **[R1-Q2, R2 AGREE]** 是否尝试过 smaller probes (4096→32→7 或 linear)？如果 inverted-U 和 Δ 在低容量 probe 下 reproduce，大幅增强可信度。
3. **[R1-Q3]** Pretrained Llama-2 处理 OOD visual tokens 时，intermediate activations 是否在 reasonable range？（排除 OOD 导致的 degenerate behavior）
4. **[R2-Q1]** C2 的 entry-exit pattern 是否可能是 Llama-2 7B 特定 backbone 的 artifact？不同 backbone（如 Mistral, Phi）是否预期同样的 reorganization？
5. **[R2-Q2]** L1 ablation 对 instruction-following accuracy（cross-instruction classification）的影响是否测量过？这将完善 capacity trade-off 论证。
6. **[R2-Q3]** 是否考虑过验证 early-layer-only fine-tuning 的 behavioral performance？即使 5-10 episodes 也有价值。

---

## Missing References

| 引用 | 重要性 | 理由 |
|------|--------|------|
| Meng et al. 2022, "Locating and Editing Factual Associations in GPT" (NeurIPS) | **High** | 与 L1 ablation 方法论直接相关（causal tracing / activation patching） |
| Belrose et al. 2023, "Eliciting Latent Predictions from Transformers with the Tuned Lens" | **High** | 与 per-layer probing 紧密相关（tuned lens → per-layer learned mapping） |
| Goldowsky-Dill et al. 2023, "Localizing Model Behavior with Path Patching" | Medium | 更全面的 patching methodology |

---

## External Review (Stanford Agentic Reviewer)

外部审稿：未配置/未请求。

---

## Overall Assessment

**Score: Borderline (6/10)**
**Confidence: High (4/5)**

| Reviewer | Initial | Post-Cross | 变化理由 |
|----------|---------|------------|----------|
| R1 | 6/10 | 6/10 | 维持。R2 的 concerns 与自身互补但不改变总评 |
| R2 | 6/10 | 6/10 | 维持。R1 的 per-head normalization 分析加强了 ablation concern 但有 layer confinement 缓解 |
| **Consensus** | **6/10** | **Borderline** | |

### 维度评分（R1+R2 加权平均）

| 维度 | 分数 | 说明 |
|------|------|------|
| Originality | 6/10 | C2 routing finding 有真正新颖性；C1 框架有方法论价值；C3 被 metric dependence 削弱 |
| Quality | 6.5/10 | 统计 apparatus 充分，但 ablation 因果推断有缺陷 + probe overparameterization 误解读 |
| Clarity | 8/10 | 写作清晰，AI 痕迹极少，结构合理 |
| Significance | 5/10 | 单模型 scope + 无 behavioral validation + speculative implications 限制 practical impact |
| Relevance | 8/10 | 直接面向 CoRL 核心关注：VLA 内部机制理解 |
| Limitations | 7/10 | 主要限制已报告，但单模型讨论不够具体 + probe 解读错误 |

### 核心判断

论文是一篇方法论严谨的 VLA 分析论文，C2 routing finding 有真正新颖性，三条件 factorial 设计是该领域的方法学进步，Round 4 的 critical issues 已实质性修复。但存在两类新问题削弱了 contribution strength：

1. **方法论瑕疵**（可修复）：ablation "3.5× specificity" 的 per-head normalization 问题 + probe overparameterization 的错误解读。这些是 framing/reporting 问题而非根本性实验缺陷——layer confinement 提供替代 specificity 证据，comparative Δ 不受 absolute R² inflation 影响。
2. **Significance ceiling**（难以快速修复）：单模型 scope + 无 behavioral validation + speculative design implications。对 CoRL 社区而言，representation → behavior 的连接是核心价值。

**Rebuttal 路径**：
- **Likely sufficient**：(a) 修正 ablation framing（报告 per-head effect + 强调 layer confinement）; (b) 修正 probe 措辞; (c) 充实 single-model limitations; (d) 弱化 architectural implications; (e) 补充缺失引用
- **Would strengthen significantly**：(a) random-subset ablation baseline; (b) linear/small probe reproducing inverted-U; (c) Llama-2 OOD analysis
- **Ideal but out of scope for deadline**：second VLA / behavioral rollout

---

## Detailed Comments（逐节）

### Abstract (~241 words raw)
- C1 reframe 到位："verify and quantify architecture-expected token specialization"
- C3 metric-dependent qualifier 到位："metric-dependent"
- **问题**：C3 与 C1/C2 等权篇幅，建议缩减 C3 让出空间给 C2 ablation detail
- "non-significant" marker 已加（Δρ ≤ 0.017, non-significant）

### Introduction
- 五段结构完整，从 gap 切入
- Straw man 已消除（"remains uncharacterized" / "opaque"）
- Contributions (i) 混合框架+验证——建议更强调框架 reusability
- **新问题**：无 Llama-2 OOD confound 讨论

### Related Work
- 五段主题组织清晰（VLAs, mechanistic interpretability, behavioral analysis, token specialization, RSA methodology）
- 29 citations，密度中等
- **缺失**：causal tracing / activation patching (Meng 2022); tuned lens (Belrose 2023)
- 与 Grant 2026 的 differentiation 清晰（三点对比）

### Method
- Factorial design 清晰
- "Why RSA over CKA" 段落解决了 R4-W2
- **新问题**：N/params ratio 解读错误（Section 4.1）；未讨论 probe complexity-capability tradeoff (Belinkov 2022)

### Experiments
- 三条件 gradient 数据完整（Table 2, Figure 1）
- Ablation 已改用 50 demos (N=63,228)
- **新问题**：Section 4.2 "3.5×" claim 需 per-head normalization 修正
- FDR correction 已应用

### Discussion
- Synthesis 段准确
- Mechanism-behavior connection 有价值
- Speculative mechanistic interpretation 合理标注
- **新问题**：Architectural implications 最后一句 overcommitted（early-layer-only suggestion + L31 complication）
- Limitations 提到单模型但不够具体

### Appendix
- Robustness suite 全面（distance metric, per-DOF, permutation, seeds, demo subsample, threshold, cross-benchmark）
- A.6 single-seed 应补 multi-seed
- CKA divergence 报告充分

### References (29 entries)
- 覆盖 VLA, benchmarks, RSA/CKA, vision encoders, mechanistic interpretability, probing, attention analysis
- **缺失**：activation patching (Meng 2022), tuned lens (Belrose 2023)
- 格式总体规范；nostalgebraist 2020 blog post 格式可接受