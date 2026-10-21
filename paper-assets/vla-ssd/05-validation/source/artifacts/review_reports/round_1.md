---
round: 1
overall_score: weak reject
timestamp: 2026-05-17T04:44:22.453130+00:00
reviewer_ids: [1, 2, 3]
cross_response_reviewer_ids: [1, 2, 3]
force_resubmit: False
---

# 圆桌审稿报告 — Round 1

**论文**: "Vision Encodes, Language Routes: A Representational Decomposition of Vision-Language-Action Models"
**Venue**: CoRL 2026 (Deadline: 2026-05-28)
**Reviewers**: R1 (方法/实验), R2 (新颖性/意义), R3 (写作/格式)

---

## Summary

论文对 OpenVLA-7B 进行了 token-level 表征分解，结合 cross-instruction probes、attention analysis、RSA 和 functional probes，在 LIBERO 上发现三个现象：(1) image tokens 与 readout token 的功能特化；(2) 训练学习了 deliberate instruction routing；(3) LLM 对 vision encoder 输出的 non-monotonic refinement（inverted-U）。分析设计系统、robustness checks 全面、写作清晰，但存在根本性的实验设计缺陷和 overclaiming 问题。

---

## Strengths

1. **系统化分析框架**：四种互补方法 + 2×2 factorial design + trained/untrained 对照，比单一 metric 更有说服力（R1, R2 共识）
2. **统计严谨性**：Bootstrap CI、LOOCV、permutation test、seed sensitivity、cross-benchmark replication、demo subsampling——附录 robustness analyses 扎实（R1 强调）
3. **写作清晰度高**：叙事主线统一（specialization → routing → geometry），三个 findings 层层递进，图表信息密度高（R3 确认）
4. **诚实报告 null/adverse results**：RSA best-vs-best CI 包含 0、CKA 反转 RSA、peak convergence 不跨 benchmark 复制等均如实报告（R1 认可）
5. **有潜在的 design insight 价值**：如果 findings 经因果验证成立，对 VLA 架构设计有实际指导意义

---

## Weaknesses（按严重性排序）

### Critical（影响接收决定，全票共识）

**W-Critical-1: Untrained baseline 无法隔离 VLA fine-tuning 的贡献**
- 论文将 trained (Llama-2 pretrained + VLA fine-tuned) 与 untrained (6.74B random weights) 对比，声称差异反映 "training learns deliberate routing"
- 这混淆了两个因素：(1) Llama-2 语言预训练；(2) VLA fine-tuning。25/32 heads 翻转为 instruction-dominant 可能是语言预训练的产物
- 缺失关键中间对照：Llama-2 base checkpoint (pretrained but not VLA-finetuned)
- 影响范围：论文核心 Finding 2（routing）和所有 trained vs untrained Δ 值的解释
- **全票共识 (R1 critical, R2 AGREE, R3 AGREE)**

**W-Critical-2: 单一模型 + 单一 benchmark family，结论过度泛化**
- 仅 OpenVLA-7B (DinoSigLIP + Llama-2) 在 LIBERO (tabletop manipulation) 上验证
- Title 使用复数 "Vision-Language-Action Models"，Abstract/Discussion 给出一般性架构设计建议
- 直接竞争者 Grant 2026 已覆盖 6 模型 + 4 benchmark
- OpenVLA 的 frozen vision encoder 是特定设计选择，其他 VLA 可能 fine-tune encoder——此时 "instruction-blind image tokens" 可能是 trivial 推论
- **全票共识 (R1 critical, R2 critical, R3 AGREE)**

**W-Critical-3: Design implications 完全 speculative，无因果验证**
- "Vision encoder quality is the primary design lever"、"action heads should read from L12-L13"、"optimize routing" 均无任何 intervention/ablation 支撑
- Probing R² 证明 information extractable，不证明 model uses it (encoding ≠ use，Belinkov 2022)
- CKA 完全反转 RSA 的 encoder 排序 (Linear CKA: untrained > trained > DINOv2)，表明 design recommendation 是 metric-dependent
- Discussion 自承 "RSA does not establish causal contribution" 但随即给出未加限定的祈使语气建议
- **全票共识 (R1 critical, R2 critical, R3 AGREE)**

**W-Critical-4: "First token-level decomposition" novelty claim 不成立**
- Neo et al. (ICLR 2025) 已对 VLM (LLaVA) 做 token-level 分析 (object localization + cross-layer alignment + last-token integration)
- Grant 2026 (Action Atlas) 对 6 个 VLA 做 per-token SAE 分析 (424 SAEs)
- 论文未引用 Neo et al.，Related Work 调研存在明显遗漏
- **R2 critical, R1 部分同意（Neo 是 VLM 非 VLA，但 Grant 2026 覆盖），R3 AGREE**

### Warning（影响评分，全票或多数共识）

**W-Warning-1: RSA best-vs-best 存在 selection bias**
- 32 层取 max 有正偏置 (winner's curse)；主 benchmark LIBERO-Goal 结果 n.s. (CI incl. 0)
- 用 LIBERO-Spatial 显著结果 rescue 主实验零结果方法论存疑
- R3 rebut：same-layer comparison (L12, Δ=+0.079, p<0.0001) 已提供——但论文以 best-vs-best 作为 primary framing 是问题
- **2:1 共识 (R1 critical, R2 AGREE, R3 REBUT)**

**W-Warning-2: Related Work 严重不足**
- 21 篇引用、3 段 15 行，属 CoRL 论文 bottom 5% 水平
- 缺失：Neo et al. (ICLR 2025)、logit lens、Raghu et al. 2021、Hewitt & Manning 2019、attention interpretability (Clark et al. 2019)
- 缺失整个类别：VLM analysis、LLM interpretability、representation geometry
- **全票共识**

**W-Warning-3: "Instruction-blind" / "purely visual" claim 过强**
- 仅 linear probe 为 chance，未用 MLP probe 测 instruction classification on image tokens
- 方法不对称：action prediction 用 MLP probe，instruction classification 用 linear probe
- **全票共识**

**W-Warning-4: CKA 与 RSA 矛盾仅放 appendix，主文选择性呈现**
- Linear CKA 完全反转核心结论 (DINOv2 最优 → CKA 下最差)
- 两个标准度量给出相反结论，选择支持叙事的指标有 confirmation bias 外观
- **全票共识**

**W-Warning-5: Limitations 格式不满足 CoRL 2026 要求**
- 当前是 Discussion 内 \paragraph{}，非独立 section/subsection
- 缺少 failure modes 描述 (CoRL 明确要求)
- **全票共识 (R3 标为 critical 格式合规问题)**

**W-Warning-6: AI 写作痕迹 (em-dash)**
- 正文至少 8 处解释性 em-dash，是最显著 AI 生成标志
- **全票共识**

---

## Reviewer Consensus [AGREE]

所有 Reviewer 达成共识的关键判断：
1. Untrained baseline confound 是最根本的 internal validity 问题
2. 单模型泛化性 + speculative implications 叠加使论文 significance 不足
3. Related Work 密度明确低于 CoRL 标准
4. 写作质量本身良好，但 claim 强度系统性超出证据支撑范围
5. Robustness analyses 做得扎实，统计报告总体透明

---

## Reviewer Divergence [REBUT]

| 分歧点 | 立场 | 理由 |
|--------|------|------|
| RSA selection bias 严重性 | R1+R2: critical / R3: REBUT | R3 认为 same-layer comparison 已充分处理 |
| 方法创新是否必须 | R2: critical / R1+R3: REBUT | R1+R3 认为分析论文可通过 insight novelty 弥补 |
| Real-robot 是否必须 | R2+R3: concern / R1: REBUT | R1 认为分析论文不必做 system contribution |
| Em-dash 是否 critical | R3: critical / R1+R2: warning | R1+R2 认为不影响科学质量 |

---

## Questions（需作者澄清）

1. 是否有 Llama-2 base checkpoint（无 VLA fine-tuning）的 attention 和 routing 数据？
2. Random features baseline 在同维度同样本量下做 10-way classification 的精度？
3. MLP probe 对 image_mean 做 instruction classification 的结果？
4. 为何选择 RSA 而非 CKA 作为 primary metric 的 principled justification？
5. 是否计划做任何 architectural intervention 验证（如 early-exit、encoder swap）？

---

## Missing References

1. **Neo et al. (ICLR 2025)** — "Towards Interpreting Visual Information Processing in Vision-Language Models" — VLM token-level analysis 直接先行工作
2. **Elhage et al. 2021** — "A Mathematical Framework for Transformer Circuits" — residual stream / information flow
3. **Raghu et al. (NeurIPS 2021)** — "Do Vision Transformers See Like CNNs?" — ViT layer-wise representation analysis
4. **Hewitt & Manning 2019** — structural probes + control tasks for probing methodology
5. **Clark et al. 2019** — attention pattern analysis in Transformers
6. **logit lens (nostalgebraist 2020)** — layer-wise prediction decomposition

---

## Overall Assessment

**Score: Weak Reject (4.5/10)**
**Confidence: High (4/5)**

| Reviewer | Score | Post-cross-response |
|----------|-------|-------------------|
| R1 | 5/10 | 维持 |
| R2 | 4/10 | 调整至 5/10（如修复 N1+限定 claims 可升至 6） |
| R3 | 6/10 | 维持（写作/格式视角） |
| **Consensus** | **4.5/10** | **Weak Reject** |

**核心判断**：论文提出了有价值的分析框架，写作质量良好，robustness checks 全面。但存在三个相互叠加的根本性问题使其低于 acceptance threshold：
1. **Internal validity**：untrained baseline 的 confound 使核心 "training learns routing" 叙事的因果归因不成立
2. **External validity**：单模型 + 单 benchmark family 无法支撑一般性结论，title/abstract 系统性 overclaim
3. **Practical significance**：design implications 完全 speculative，CKA 反转 RSA 表明 recommendations 是 metric-dependent

**Rebuttal 路径（如能实质性解决以下任一，可重新评估）**：
- 补充 Llama-2 base checkpoint 中间对照（解决 internal validity）
- 补充至少一个 architectural intervention 实验（解决 practical significance）
- 大幅限定所有 claims 至 OpenVLA-specific + correlational（解决 overclaiming，但可能降低 impact）

---

## Detailed Comments（逐节）

### Abstract
- "LOOCV-verified" 未展开；建议改为 "cross-validated"
- 最后一句 "VLA architectures should..." 语气过强，缺乏因果支撑
- 约 200 words，长度合适

### Introduction
- 五段结构完整，叙事从 gap 切入
- L8 仅引用 grant2026 作为 visual dominance 唯一支撑——建议补充 fei2025、hou2026
- Contribution list (L27) "the first..." claim 需限定

### Related Work
- 3 段 ~16 行严重不足
- 缺失整个类别：VLM analysis、probing methodology、attention interpretability
- 未与 Grant 2026、Swann 2026 做明确 differentiation

### Method
- 2×2 factorial design 清晰
- "untrained control by reinitializing all LLM parameters" 的描述准确但未讨论其局限
- 列表项 em-dash 格式问题（改用冒号）

### Experiments
- 数据呈现严谨，所有数值有 CI/p-value
- Table 1 caption 声称 "L0-L8 shown" 但实际含 L16, L31
- Fig 3 和 Fig 5(a) 信息重叠，空间效率低
- §4.3 应以 same-layer comparison 为 primary evidence，best-vs-best 为 supplementary

### Discussion
- Implications 段是全文最弱环节——definitive 语气 + correlational evidence = 内部矛盾
- Limitations 内容基本到位但格式不合规，缺 failure modes
- RSA-R² peak offset 的讨论有价值

### Conclusion
- 几乎逐字重复 Abstract，阅读价值低
- 建议增加 1 句 future direction 或 broader implication

### Appendix
- CKA metric sensitivity 分析应部分移入正文
- Robustness analyses (seed, demo subsample, distance metric, permutation) 全面且支持 pattern 稳定性
- Cross-benchmark (LIBERO-Spatial) replication 有价值但仍是同一 benchmark family