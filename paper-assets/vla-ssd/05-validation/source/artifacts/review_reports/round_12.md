---
round: 12
review_mode: fresh
overall_score: weak reject
timestamp: 2026-05-20T11:57:09.335755+00:00
reviewer_ids: [1, 2, 3]
cross_response_reviewer_ids: [1, 2, 3]
force_resubmit: False
---

# 审稿报告：Vision Encodes, Language Routes — CoRL 2026

**项目**: vla-ssd
**论文**: "Vision Encodes, Language Routes: Token-Level Functional Specialization in a Vision-Language-Action Model"
**目标 Venue**: CoRL 2026 | **截止日期**: 2026-05-29
**审稿模式**: Fresh review（Round 12）
**Reviewer 配置**: R1（方法/实验）+ R2（新颖性/CoRL Relevance）+ R3（写作/格式/可复现性）

---

## Summary

本文对 OpenVLA-7B（SigLIP+DINOv2 → MLP → Llama-2 7B）在 LIBERO benchmark 上进行 token-level 表征分析，结合 cross-instruction probes、L1 attention 分析、RSA、MLP probes 四种互补方法，在 2×2 factorial design（trained/untrained × instruction present/absent）+ Llama-2 base 第三条件下，提出三个发现：(1) VLA fine-tuning 将 instruction attention 从 mid-depth 前移至 entry-exit layers（L0-L1 + L31）；(2) vision encoder 表征在中间层达 RSA/probe 峰值；(3) image tokens 全层保持 instruction-blind，readout token 是多模态整合位点。在 TraceVLA (Phi-3-V) 上做了跨架构验证。论文附录充实（19 页），包含 dose-response ablation、counterfactual instruction analysis、seed sensitivity 等补充实验。

---

## Strengths

**S1.** **系统的 factorial 实验设计**：2×2（trained/untrained × with/without instruction）+ Llama-2 base 第三条件 + DINOv2/CLIP 外部 baseline，是目前 VLA interpretability 文献中最系统的实验框架。[R1, R2, R3 共识]

**S2.** **多方法三角验证**：7 种互补分析（cross-instruction probes, attention analysis, RSA, MLP probes, dose-response ablation, counterfactual perturbation, cross-architecture validation）从不同角度支撑核心发现，减少单一方法偏差。[R1, R2 共识]

**S3.** **统计严谨性高于同行**：Bootstrap CI (10,000 resamples)、task-level blocking、FDR correction、Cohen's d、permutation tests 的使用远超大部分 mechanistic interpretability 论文。[R1]

**S4.** **Finding 1 有实证价值**：VLA fine-tuning 将 instruction attention 从 mid-depth 重新分配到 entry-exit layers 的发现不能从架构定义中推导，需要实证验证。三条件梯度（untrained 0/32 → Llama-2 base 9/32 → VLA-trained 24/32 instruction-dominant heads at L1）清晰展示了 VLA training 的 specific effects。[R1, R2, R3 共识]

**S5.** **附录透明度**：19 页附录涵盖 robustness checks、seed sensitivity、subsample sensitivity、linear probe 对照、matched-size ablation controls，体现了对可复现性的认真态度。[R1, R3]

**S6.** **诚实报告**：如实报告了 CKA 与 RSA 的 metric divergence (Appendix A.1-A.2)、RSA best-vs-best 非显著性 (§4.4)、specificity control 有限效应 (d ratio 1.08×)，没有回避不利结果。[R1, R3]

---

## Weaknesses

### Must-Fix（影响接收决定）

**N1 [critical] 缺乏闭环行为验证——CoRL 核心缺陷** [R1-N1, R2-N2, R3 | 三位 Reviewer 最强共识]
- 所有发现通过 probe R²、RSA ρ、attention 统计量度量，从未连接到 LIBERO task success rate。
- §4.3 的 L1 ablation 度量 R² 变化而非 task completion。Appendix A.7 报告 ablation 后 ΔMSE ≈ 0——如果 ablation 不改变 action error，routing 的功能意义存疑。
- §5 Discussion 提出的 actionable implications（L1 entropy runtime monitor、pruning ~56%）均为推测，未经任何验证。
- CoRL 2026 CFP 明确要求 "demonstrate relevance to robotics" 并鼓励 "real-robot experiments or convincing simulation-to-real evidence"。
- **建议**：(a) Ablation → LIBERO rollout 测量 task success rate；(b) 验证 probe R² 与 per-task success rate 的 rank correlation；(c) 或改投对 robotics relevance 无硬性要求的 ML venue（ICML/NeurIPS interpretability track）。

**N2 [critical] 因果 overclaiming：Title "Routes" vs correlational evidence** [R1-N2, R2-W2, R3 | 三位 Reviewer 共识]
- Title "Language Routes" 和 §5 "instruction routing" 使用机制性语言，但核心证据的 causal specificity 有限。
- Table 23: instruction-dominant heads ablation d=0.650 vs random 24 heads d=0.601±0.021 (95% CI [0.568, 0.622])，差异仅 ~8%。R3 指出："distributed, attention-graded routing rather than a dedicated subset"（Appendix A.6），但主文 framing 未充分传达这一 nuance。
- Dose-response 和 counterfactual perturbation 是 interventional evidence（非纯 correlational），但 specificity gap 不够强以支撑 "routing" 的机制性含义。
- R² 增加 paradox 的 "information-computation dissociation" 解释（§5）是 post-hoc 的，未经独立检验。
- **建议**：(a) Title/Abstract 将 "routes" 改为更审慎表述（如 "instruction-correlated attention redistribution"）；(b) 做 activation patching 获取更精确因果链路；(c) 或明确在 abstract 中标注 interventional 但 low-specificity。

**N3 [critical] 跨架构泛化声称证据不足** [R1-N3, R2-N3 | 三位 Reviewer 共识]
- 仅 2 个架构（OpenVLA/Llama-2-7B, TraceVLA/Phi-3-mini），共享几乎相同的架构模式（dual frozen vision encoder → MLP projector → causal LLM decoder + autoregressive action decoding）。
- TracVLA 仅 5 个 LIBERO-Goal tasks（vs OpenVLA 10 个 LIBERO-Spatial tasks），任务集不同，pre-VLA baseline 不同（Llama-2 base vs Phi-3-Instruct）。
- Table 24 显示差异：peak layer L9 vs L11、exit-layer R² 0.488 vs 0.557、profile shape "flat plateau" vs "ramp→plateau"。
- 缺失关键架构类型：flow-matching VLAs (π₀)、diffusion-based (Octo)、cross-attention fusion architectures。
- Abstract "consistent across two VLA architectures" 构成 overclaim。
- **建议**：(a) Claim 弱化为 "consistent across two causal-decoder VLAs with shared vision backbone"；(b) 明确讨论为什么发现可能不适用于 flow-matching/diffusion-based VLAs。

**N4 [critical] Finding 3（image token instruction-blindness）是 causal attention mask 的架构必然结果** [R2-N1, R3 agree with nuance]
- OpenVLA 使用 causal decoder，image tokens 在序列中位于 instruction tokens 之前。Causal mask 在数学上保证 image tokens 无法 attend to instruction tokens。
- Cross-instruction probe accuracy = chance (1/10) 在 image_mean 上是架构约束的直接推论，不是实证发现。
- 论文在 §4.2 标注 "(expected)" 并在 abstract 末句称其为 "framework sanity check"——定位方向正确。但 Title "Vision Encodes, Language Routes" 和 Abstract "strict functional specialization" 仍将此架构约束呈现为核心贡献。
- 缺失引用：(a) "Seeing is Understanding: Unlocking Causal Attention into Modality-Mutual Attention" (arXiv:2503.02597)；(b) "Rethinking Causal Mask Attention for Vision-Language Inference" (arXiv:2505.18605)。
- **建议**：Title 不再暗示 token specialization 是实证发现；Abstract "strict" 改为 "expected"；引用 causal mask 相关文献。

**N5 [critical] 正文超出 CoRL 8 页限制** [R3-N1, R1+R2 agree]
- PDF 正文约 8.7 页。§5 Discussion (Synthesis + Mechanistic interpretation + Functional stages + Limitations and scope) 和 Conclusion 延伸到第 9 页，References 从第 9 页约 1/3 处开始。
- 超页限是 desk rejection 的常见理由。
- **建议**：将 Discussion 的 Mechanistic interpretation 和 Functional stages predictions 移至 Appendix；精简 Abstract/Introduction 冗余。

**N6 [critical] Abstract/Introduction 信息过载** [R3-N2, R1+R2 agree]
- Abstract (~200 words) 塞入 15+ 定量结果（d=0.48→0.64, p=0.033, R²+0.069, Δρ=0.017, 2.5× 等）。
- Introduction 几乎逐字重复 Abstract 的所有量化结论。
- 信息密度远超 CoRL/NeurIPS 同领域论文，robotics 背景的审稿人可能对过度密集的 interpretability 语言缺乏耐心。
- **建议**：Abstract 只保留 3 个 headline findings 的定性描述 + 1-2 个关键数字；Introduction 聚焦 motivation 和 high-level contribution。

### Should-Fix（影响评分但不一票否决）

**W1 [warning] 无首页 teaser figure** [R3-W1, R2 agree, 视觉审查 critical]
- Figure 1 直到 PDF page 6-7 才出现。前 4 页连续纯文本，无 figure/table/equation。
- 审稿人前 2 分钟内看不到任何视觉锚点。
- **建议**：创建 overview figure（左：VLA 架构示意，右：L1 routing 核心发现），放在第 1 页。

**W2 [warning] 层编号 off-by-one 错误** [R3-W2, R2 agree]
- §3.2: "L1--L31 the 32 transformer layers"——L1-L31 仅 31 个索引。Llama-2-7B 有 32 blocks，应为 L1-L32。
- L32 的定义（第 32 个 transformer block output vs final layer norm output）存在歧义。

**W3 [warning] 多条引用使用 arXiv preprint 而非已发表版本** [R3-W3, R2 agree]
- OpenVLA、Prismatic VLMs、Llama 2、Tuned Lens、Open X-Embodiment、π₀ 等均有已发表版本但引用 arXiv。

**W4 [warning] 缺失 6 篇重要 related work** [R2]
- "What Do Visual Tokens Really Encode?" (arXiv:2603.00510, 2026)
- "Towards Interpreting Visual Information Processing in VLMs" (ICLR 2025, arXiv:2410.07149)
- "Seeing is Understanding" (arXiv:2503.02597, 2025)
- "Phase Diagram of Vision LLMs Inference" (arXiv:2411.00646, 2024)
- "Understanding Language Prior of LVLMs" (arXiv:2509.23050, 2025)
- AVA-VLA (arXiv:2511.18960, 2025)
- 需验证真实性后酌情加入。

**W5 [warning] 与 Grant et al. (2026) 和 Häon et al. (2025) 的区分不够清晰** [R2-W3, R3 agree]
- Grant 的 "visual dominance" 与本文 "vision encodes" 的关系未充分阐述。
- Discussion §5 line 6 做了 where/what 区分但太晚——应在 Related Work 中出现。

**W6 [warning] Cohen's d 独立性假设** [R1-W1, R2+R3 agree]
- Token-level observations 在 trajectory 内具有强时序相关性。主文以 token-level d 为主要报告（d=0.65），Appendix 有 trajectory-level d (2.943) 但不突出。
- N_eff 报告存在但 method section 未明确标注哪些分析用 token-level vs aggregated。

**W7 [warning] FDR 多重比较校正细节不足** [R1-W4, R2 agree]
- §4.3 提到 "surviving FDR correction at 29-30/33 layers" 但未指明 FDR 方法、α 水平、adjustment 针对的假设族。

**W8 [warning] LIBERO 单一 benchmark，instruction diversity 有限** [R2-W4, R1-W2, R3 agree]
- 10 个 tasks 的 instruction 差异主要在 object identity，cross-instruction probe 本质上是 10-way object/target classification。
- LIBERO-Spatial cross-benchmark validation 仍在 LIBERO family 内。

---

## Reviewer Consensus [AGREE]

以下问题三位 Reviewer 达成强共识（全部 AGREE 或 AGREE with nuance）：

1. **无闭环验证 / CoRL relevance 不足**（N1）——最强共识项。纯 open-loop analysis 对 CoRL 是致命缺陷。
2. **跨架构泛化 overclaim**（N3）——2 个同质架构不够，claim 需弱化。
3. **因果 overclaiming**（N2）——interventional evidence 存在但 specificity 不足以支撑 "routing" 机制性语言。
4. **超页限**（N5）——8.7 页 vs 8 页限制。
5. **Abstract/Intro 信息过载**（N6）——信息密度过高，Introduction 与 Abstract 高度重复。
6. **Finding 1 是最有价值的贡献**——三位 Reviewer 均肯定 instruction routing 前移是 genuinely novel 的实证发现。

## Reviewer Divergence [REBUT]

**DIV1: Title "Language Routes" 是否误导**
- R2 (W1): 认为是 positional routing 而非 language routing——readout token 碰巧在 instruction 之后，routing 是 positional 必然。
- R3 (REBUT): 三条件对比 0→9→24 instruction-dominant heads 证明 language pretraining 有贡献；counterfactual analysis 证明 routing 对 language content 敏感（paraphrased d=0.697 vs shuffled d=0.625）。不是纯 positional。
- **Director 判断**：R3 的 REBUT 有数据支持，但 R2 的 concern 也有部分道理（positional advantage 是 necessary condition）。Title 的问题更在于 "Routes" 的因果含义（见 N2），而非 "Language" vs "Positional"。

**DIV2: MLP probe capacity 是否过大**
- R1 (W5): 1.05M 参数偏大，缺 hidden size sensitivity。
- R3 (REBUT): Appendix A.6 的 linear probe 完整复现了 per-layer pattern，且 linear probe 下 trained-untrained gap 更大，系统性排除了 MLP capacity concern。
- **Director 判断**：R3 的 REBUT 成立。Linear probe 对照充分。此项降级为 info。

**DIV3: Limitations 是否需独立 section**
- R3 (W4): CoRL 要求 Limitations section，当前为 paragraph。
- R2 (partial REBUT): CoRL 未硬性要求独立 numbered section。
- **Director 判断**：低风险，但建议拆分为 subsection。降级为 info。

---

## Questions for Authors

Q1. 是否有 L1 head ablation → LIBERO closed-loop success rate 的实验数据？
Q2. Table 23 中 instruction-dominant vs random ablation 的 Cohen's d 差异（0.650 vs 0.601±0.021）是否有正式 permutation test 的 p-value？
Q3. Cohen's d 是在 token level 还是 demo-averaged level 计算的？主文为何优先报告 token-level 而非 trajectory-level？
Q4. 是否有训练中间 checkpoint 的分析（instruction routing emergence dynamics）？
Q5. OpenVLA 中 image tokens 与 instruction tokens 的序列顺序是什么？如果 image-first，应明确标注以回应 causal mask concern。
Q6. FDR correction 使用的是 Benjamini-Hochberg 还是 Benjamini-Yekutieli？Correction family 是每个 metric 内跨层还是跨所有 metrics？

---

## Missing References

由 R2 提出，需验证真实性后酌情加入：
1. "What Do Visual Tokens Really Encode? Uncovering Sparsity and Redundancy in MLLMs" (arXiv:2603.00510, 2026)
2. "Towards Interpreting Visual Information Processing in Vision-Language Models" (ICLR 2025, arXiv:2410.07149)
3. "Seeing is Understanding: Unlocking Causal Attention into Modality-Mutual Attention for MLLMs" (arXiv:2503.02597, 2025)
4. "Phase Diagram of Vision Large Language Models Inference" (arXiv:2411.00646, 2024)
5. "Understanding Language Prior of LVLMs by Contrasting Chain-of-Embedding" (arXiv:2509.23050, 2025)
6. AVA-VLA (arXiv:2511.18960, 2025)

由 R3 引用验证确认：52 条引用中无 fabricated citation，6 条 not_found 均为 blog posts/technical reports（正常），5 条 author name mismatch 为 API 比对问题。

---

## External Review (Stanford Agentic Reviewer)

外部审稿：未请求（项目未配置 paperreview.ai）。

---

## Visual Layout Check（非评分项）

**状态**: done（耗时 2m47s）

关键发现：
- **[critical]** 前 4 页连续纯文本，无 figure/table/equation。审稿人前 2 分钟内看不到任何视觉锚点。
- **[critical]** 核心发现（attention routing pattern、layer-wise profile）全部压在 page 5-8，第一印象风险极高。
- **[warning]** Abstract 偏长（约占页面 60%），信息密度高但视觉拥挤。
- **[warning]** Figure 1 底部 heatmap panel 尺寸偏小，打印时可能难辨。
- **[warning]** Figure 2 线条较细，legend 字号偏小（约正文 60-65%）。
- **[warning]** Table 1+2 分处两页无 figure 穿插，视觉节奏单调。
- **[warning]** Appendix page 30 约 50% 空白。
- **[info]** 所有表格统一使用 booktabs 风格，专业规范。无 margin 溢出、LaTeX 渲染错误或未解析引用。颜色使用合理。

---

## Overall Assessment

**Overall Score: Weak Reject (4/10)**

**置信度**: 4/5（三位 Reviewer 在核心问题上达成强共识，交叉验证充分）

**理由**：

论文在实验设计（factorial controls、多方法三角验证）和统计严谨性方面优于同期 VLA interpretability 工作，Finding 1（instruction routing 前移至 entry-exit layers）是有实证价值的发现。附录的深度和透明度值得肯定。

然而，论文面临三个结构性问题，使其不适合当前形态投稿 CoRL：

1. **CoRL relevance 根本性不足**：纯 open-loop representational analysis，无闭环实验、无真实机器人验证、无基于分析结果的 actionable improvement。这不是写作或 framing 能解决的——需要新实验。
2. **多层面 overclaiming**：(a) Title "Routes" 暗示因果机制但证据 specificity 仅 ~8%；(b) "consistent across architectures" 基于 2 个同质架构；(c) Finding 3（token specialization）是 causal mask 的架构推论但 title/abstract 仍作为发现呈现。
3. **格式问题**：超页限 ~0.7 页（desk rejection 风险）、Abstract 信息过载、无首页 teaser figure。

**建议路径**：
- **路径 A（CoRL rebuttal）**：补充 L1 ablation → LIBERO rollout closed-loop 实验（最关键）+ 压缩至 8 页 + 降级因果语言 + 弱化跨架构 claim。如果 closed-loop 实验证实了 routing 的行为后果，评分可从 4/10 提升至 6-7/10。
- **路径 B（改投）**：本文的方法论贡献更适合 ICML/NeurIPS interpretability track，那里对 robotics relevance 无硬性要求，且 analysis-only 论文有成功先例。

---

## Detailed Comments（逐节）

### Abstract
- 信息过载（15+ 定量结果），应精简至 3 个 headline findings + 1-2 关键数字
- "strict functional specialization" → "expected functional specialization"（causal mask 约束）

### §1 Introduction
- 与 Abstract 重复度 ~80%，需大幅去重
- 聚焦 motivation（why token-level analysis matters for VLA design）而非提前报告所有数字

### §2 Related Work
- 与 Grant et al. (2026) 和 Häon et al. (2025) 的 explicit comparison 缺失
- 缺少 causal mask 对 visual token 信息流限制的讨论和引用

### §3 Method
- 层编号 off-by-one (L1-L31 = 31 个索引，应为 L1-L32)
- Image-instruction token ordering 未明确说明，影响对 causal mask argument 的评估

### §4 Experiments
- §4.2: Finding 3 的 "(expected)" 标注方向正确，但需在 contributions 中一致降级
- §4.3: FDR method 和 family scope 需补充
- §4.5: Dose-response ablation 效应 modest (d=0.48→0.64)；specificity control d ratio 1.08×
- §4.6: TracVLA validation 的限制（5 tasks、不同 task set、不同 pre-VLA baseline）需显式承认

### §5 Discussion
- Mechanistic interpretation 和 Functional stages predictions 是 speculative，建议移至 Appendix 以控制页数
- "Our routing analysis (where) complements Häon et al.'s (what)" 很好，但应出现在 Related Work

### Conclusion
- "Code and data will be released upon acceptance"——正面，但未提交 supplementary code

### Appendix
- 内容充实、透明度高
- Table 17 的 `\resizebox` 可能导致字体过小
- Page 30 大面积空白可优化

---

**报告生成日期**: 2026-05-20
**Reviewer IDs**: R1, R2, R3（均完成独立初审 + 交叉回应）