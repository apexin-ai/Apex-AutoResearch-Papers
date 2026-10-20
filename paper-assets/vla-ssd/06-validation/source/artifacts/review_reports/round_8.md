---
round: 8
review_mode: fresh
overall_score: weak reject
timestamp: 2026-05-19T01:05:13.427943+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告 — Round 9 (Fresh Review)

**论文**: "Vision Encodes, Language Routes: Token-Level Functional Specialization in a Vision-Language-Action Model"
**Venue**: CoRL 2026 (deadline: 2026-05-29)
**审稿模式**: fresh (重新审稿)
**Reviewer 编排**: 2 人（R1: 方法严谨性+实验设计；R2: 新颖性+叙事+CoRL适配性）
**轮次**: 1 轮（交叉后关键问题达成共识，无需额外轮次）

---

## Summary

本文对 OpenVLA-7B 在 LIBERO 上进行系统的 token-level representational analysis，结合 cross-instruction probes、attention analysis、RSA、functional probes 以及 factorial trained/pretrained/untrained controls，提出三个发现：(1) image tokens instruction-blind、readout token 为唯一多模态汇聚点（架构验证）；(2) VLA fine-tuning 将 instruction routing 从 mid-depth 前移至 entry-exit layers (L0-L1, L31)；(3) vision encoder 表征呈 metric-dependent 中间层峰值。七项互补分析（dose-response、counterfactual、specificity control 等）支持 C2。

---

## Strengths

1. **多方法互证框架**：结合七项互补分析（cross-instruction probes、attention analysis、RSA、functional probes、dose-response ablation、counterfactual analysis、specificity controls），形成迄今最系统的 VLA 内部表征分析。 [AGREE R1, R2]
2. **三条件 factorial 设计**（trained/pretrained/untrained）是该领域的方法论进步，大多数先前工作缺少 untrained 和 pretrained baselines 的对比。 [AGREE R1, R2]
3. **透明报告 metric divergence**：RSA 与 CKA 的分歧被正面讨论（§4.4, Appendix A.1-A.2），C1 标为 sanity check，C3 的 metric-dependent 性质明确说明。 [AGREE R1, R2]
4. **丰富的 robustness 分析**：seed sensitivity (5 seeds)、demo subsampling、distance metric invariance、threshold sensitivity、linear vs MLP probe、cross-benchmark (LIBERO-Spatial)，覆盖面超过同领域大多数论文。 [AGREE R1, R2]
5. **核心发现 C2 有价值**：Entry-exit routing pattern 与 Llama-2 base 的 mid-depth pattern 的对比是 genuine insight，有多条 converging evidence 支持。 [AGREE R1, R2]
6. **写作清晰**：主文紧凑，结构合理，关键发现在 Introduction 和 Discussion 中有一致的叙事线。 [AGREE R1, R2]

---

## Weaknesses

### Critical (影响接收决定)

**C-1. 单模型(OpenVLA-7B)单基准(LIBERO)范围严重限制 generalizability** [AGREE R1, R2]
- 仅研究 OpenVLA-7B 一个模型。LIBERO-Spatial 交叉验证属同一模拟器/同一机器人/同一动作空间，不算 model-level generalization。Discussion §5 对 π₀ (cross-attention)、RT-2 (decoder-only)、更大 VLA 做了三条预测，但无一验证。VLA 领域正快速多样化（π₀ cross-attention、Octo diffusion heads、不同 embodiment/action space），单模型发现的迁移性无法判断。
- **Impact**: 读者无法判断哪些是 OpenVLA-7B 的特性、哪些是 VLA 的通用机制。Contribution (i) 声称 "a systematic experimental framework"，但 framework 的泛化性仅在同一模型上验证过。

**C-2. 完全缺失 closed-loop / task-performance 验证** [AGREE R1, R2]
- 所有分析均为 representational/open-loop。论文声称的最具 robotics 价值的 implications（L1 routing monitoring 可检测 routing integrity、L14-L32 约 56% 参数为 pruning targets、instruction-discriminative tasks 对 L1 routing 依赖更强）均为未验证猜测。
- probe R² 和 trajectory divergence (Cohen's d) 衡量表征质量和动作偏移，而非任务完成率。后面的层可能负责 action token decoding 的 fine-grained timing（如 gripper 时机），恰好是 R² 无法捕捉的。
- CoRL 评审标准要求 "explicitly address a learning question for physical robots" 或 "test the proposed learning solution on physical robots"。

### Warning (影响评分但不一票否决)

**W-1. Discussion 使用 'Causal' 标签分类证据，在 open-loop 设定下构成 overclaim** [AGREE R1, R2; R1 原定 critical, 交叉后降为 warning]
- Discussion §5 第 1 段明确将 dose-response 和 counterfactual 标记为 "Causal" 证据。虽符合 NLP mechanistic interpretability 惯例（Meng et al. 2022, Wang et al. 2023），但 CoRL 读者以 robotics 背景为主，易误解为 closed-loop 因果。应改为 "interventional evidence"。

**W-2. Ablation R² 结果与核心 routing 叙事存在张力** [R1: critical; R2: warning; 综合定级 warning]
- Dominant-head ablation 使 action R² 增加 +0.042，random-subset ablation 增加更多 (+0.077±0.013, z=-2.73, p=0.003)。如果 instruction-dominant heads 携带功能性 routing signal，ablation 应降低 R²，但实验显示相反。
- "Structured noise for the probe" 的解释是 post-hoc rationalization，缺乏独立验证。
- **R1 与 R2 分歧**：R1 认为此结果动摇 routing 叙事根基；R2 认为 routing claim 有五条独立证据线（dose-response、counterfactual、task-dependent routing、trajectory d、三条件 attention gradient），R² ablation 只是其中之一。R2 指出 trajectory d (dominant 0.65 vs control 0.41) 与 routing function 的关联更直接。
- **综合判断**：R² 解释确实 post-hoc，但核心 routing claim 不完全依赖此结果。定级 warning，但需更清晰讨论 R² vs d 的分离机制。

**W-3. Counterfactual ordering 与 semantic distance 叙事不一致** [AGREE R1, R2]
- §4.3: paraphrased (d=0.697) > shuffled (d=0.625)，但 paraphrase 语义上更接近原始 instruction。实际数据暗示模型对 lexical/token identity 比 semantic content 更敏感。
- **R1 与 R2 分歧**：R1 推断此结果支持 Grant et al. 的 "language ignored" 结论；R2 反驳称所有条件 d > 0.6 证明 instructions ARE influencing actions，只是影响路径走 token identity 而非 semantic distance。
- **综合判断**：ordering anomaly 成立，§4.3 "follows semantic distance" 措辞需修正。但 d > 0.6 确实表明 instructions 有功能影响，"language ignored" 推断过强。

**W-4. N=10 tasks 的 RSA bootstrap 统计功效不足** [AGREE R1, R2]
- §4.4 "training enhances decodability, not geometry" 基于 underpowered n.s. (N=10, Δρ=0.017, CI includes 0) 得出 negative conclusion。论文自己在 Appendix A.10 承认 "reflects limited statistical power"。LIBERO-Spatial (Δ=+0.023, p<0.001) 反驳了 null。
- 主文应引入 LIBERO-Spatial significant result 作为对冲，将 "not geometry" 改为 "limited geometric gain under current sample size"。

**W-5. C1 (architecture validation) 在 Abstract/Introduction/Contributions 中占比失衡** [AGREE R1, R2]
- C1 是 causal mask + frozen encoder 的必然结果（论文自称 sanity check），但占据 Abstract 最长的 finding 描述、Introduction 第一个 finding、§4.2 完整 subsection + Table 1、Contribution (i)。建议压缩释放空间给 C2。

**W-6. Vision representation 训练效果微弱，framing 未充分反映** [AGREE R1, R2]
- Image_mean: RSA Δρ=+0.017 (n.s.), R² Δ=+0.015 (borderline p=0.006)。与 last_preaction 效果（R² Δ=+0.069, attention +46pp）差一个数量级。§4.4 标题 "Training enhances decodability" 用 "enhances" 描述 image_mean R² Δ=+0.015 有夸大嫌疑。

**W-7. Cohen's d 独立性假设违反** [AGREE R1, R2]
- Trajectory 内 action tokens 强自相关。将每个 token 作为独立观测计算 d 系统性高估 effect size。d 值的绝对值 (0.48-0.97) 不可靠，但相对排序不受影响（自相关对所有条件方向一致）。建议以 trajectory 为单位计算 d。

**W-8. Pretrained Llama-2 base 的 in-distribution text bias 替代解释** [R1: warning; R2: partial agree]
- Llama-2 base 在 L1 的 9/32 instruction-dominant heads 可能因 instruction tokens 是 in-distribution text（image tokens 是 OOD），而非 "pretraining seeds partial routing"。OOD diagnostics (Appendix A.9) 排除退化但未排除此混淆。
- R2 指出：无论 9/32 的原因如何，pretrained→trained 的 delta (+15 heads) 仍然是 VLA fine-tuning 效应。

**W-9. Specificity control 效果有限** [AGREE R1, R2]
- Top-24 vs Bottom-24 overlap 16 heads。d ratio 仅 1.15×，KL ratio 1.56×，两指标不一致。不构成 strong specificity evidence。

**W-10. CoRL scope fit 有限** [R2: critical; R1: REBUT 降为 warning]
- 纯 representational analysis，无物理机器人实验、无 closed-loop 评估、无学习算法改进。Related Work 过度对标 NLP interp 文献。
- R1 反驳：CoRL 接受 analysis papers；分析对象 (VLA+LIBERO) 是 robotics-specific；entry-exit routing 是 VLA fine-tuning 特有的，非 LLM 通用属性。
- **综合判断**：降为 warning。CoRL 历史上接收过纯分析论文，但当前版本的 robotics-specific implications 确实不够具体。

**W-11. N=63,228 的有效独立单元数未说明** [AGREE R1, R2 partial]
- RSA 已 task-level blocking，probe 已 demo-level split，但论文未明确说明有效 N 和 blocking 策略，N=63,228 给读者错误印象。

### Info (不影响接收)

**I-1. 缺失引用**：Octo (Ghosh et al. 2024) 未引用；Häon et al. 2025 的 sparse semantic directions 与 L1 routing heads 的互补关系未讨论；引用密度 46 篇偏低。

**I-2. 小问题合集**：Table 1 caption 不清晰、§4.3 脚注 R² pipeline 差异易混淆、Appendix Table A5 control 行数据缺失、nostalgebraist2020 accessed date 暴露写作时间。

---

## Reviewer Consensus [AGREE]

1. **单模型单基准是最大局限** — 需至少一个额外架构验证 C2
2. **无闭环验证削弱 robotics relevance** — 至少需一项 closed-loop experiment (pruning/monitoring)
3. **Counterfactual ordering 不符 semantic distance** — §4.3 措辞需修正
4. **N=10 underpowered n.s. → negative conclusion 是 inferential error** — 引入 LIBERO-Spatial result + 修正措辞
5. **方法论框架有价值** — factorial design + 多方法互证是该领域的方法论进步
6. **C2 (entry-exit routing) 是 genuine insight** — 有 converging evidence 支持
7. **Ablation R² 解释需加强** — post-hoc "structured noise" 需独立验证或更清晰的理论框架

## Reviewer Divergence [REBUT]

| 问题 | R1 | R2 | Director 综合 |
|------|----|----|-------------|
| Ablation R² 矛盾严重度 | Critical (动摇整个 routing 叙事) | Warning (五条独立证据，R² 只是其一) | **Warning** — R2 的论点更有说服力：routing claim 有多条独立证据线 |
| "Causal" 术语 | Critical | Warning (符合 interp 惯例) | **Warning** — 术语修改低成本高收益 |
| Counterfactual → "language ignored" | 支持 Grant et al. | 反驳 (all d > 0.6 ≠ ignored) | **R2 更有说服力** — d > 0.6 证明 instructions 有功能影响 |
| CoRL scope fit | Warning | Critical | **Warning** — CoRL 接受 analysis papers，但需增强 robotics implications |
| Probe 过参数化 | Warning | REBUT (Appendix A.8 已回应) | **已充分回应** — linear probe 复现定性模式且 gap 更大 |

---

## Questions for Authors

1. 是否有条件在 π₀ 或 RT-2 上验证 L1 routing pattern？即使只做 32-layer attention profile 比较也可大幅增强 generalizability。
2. 是否考虑过基于 routing analysis 做 layer pruning 并在 LIBERO 上跑 closed-loop success rate？这对 CoRL 读者的价值远大于 probe R²。
3. 如何排除以下解释：instruction routing 实际上是与 action prediction 无关（甚至有害）的 artifact，而非功能性贡献？R² 结果似乎支持此解释。
4. paraphrased 和 shuffled instructions 的 token overlap rate 是多少？如果 paraphrased 的 token overlap 远低于 shuffled，ordering 反映的是 token-level sensitivity 而非 semantic distance。
5. Discussion 预测 cross-attention VLAs 不会有 L1 routing heads。如果成立，C2 仅适用于 decoder-only VLAs，进一步缩小 generalizability scope。如何看待这一 tension？

---

## Missing References

1. **Octo** (Ghosh et al. 2024) — 开源 cross-attention VLA，与 Discussion 中对 cross-attention 架构的预测直接相关
2. **Häon et al. 2025 的深入讨论** — sparse semantic directions 与 L1 routing heads 的互补关系

---

## Overall Assessment

**评分: 5/10 — Weak Reject (marginally below acceptance threshold)**
**置信度: 4/5**

本文是一篇方法论扎实、数据分析严谨的 representational analysis 论文。核心贡献 C2（VLA fine-tuning 将 instruction routing 前置到 entry-exit layers）是有价值的发现，七项互补分析形成有说服力的证据链。三条件 factorial design 和丰富的 robustness checks 超过同领域大多数论文。

然而，两个 critical 问题使其在 CoRL 的接收前景不乐观：(1) 单模型 (OpenVLA-7B) 单基准 (LIBERO) 范围严重限制 generalizability，Discussion 的三条预测均未验证；(2) 完全缺失 closed-loop 验证，Discussion 的所有 design implications（pruning targets、routing monitoring、task-dependent routing）均为未验证猜测，probe R² 和 trajectory d 不等价于 task success rate。

此外，多项 warning 级问题（"Causal" overclaim、ablation R² 矛盾的 post-hoc 解释、counterfactual semantic distance 叙事不符、N=10 underpowered negative conclusion、C1 权重失衡）累积削弱了论文的整体说服力。

**建议**：
- 如果能在 deadline 前补充 (a) 至少一个额外 VLA 架构的 attention profile 验证 + (b) 至少一项基于 routing analysis 的 closed-loop experiment（如 layer pruning → task success），论文将显著增强竞争力，有望达到 borderline accept。
- 当前版本更适合投往 NeurIPS/ICML 的 interpretability track，其中 closed-loop 验证和 multi-model 覆盖的期望较低。

---

*Report generated by Review Director (Round 9, Fresh Review)*
*Reviewers: R1 (方法严谨性+实验设计), R2 (新颖性+叙事+CoRL适配性)*
*Cross-response completed: R1 ↔ R2*