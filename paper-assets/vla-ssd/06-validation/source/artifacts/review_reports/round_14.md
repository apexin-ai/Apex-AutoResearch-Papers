---
round: 14
review_mode: fresh
overall_score: weak reject
timestamp: 2026-05-20T17:06:57.667033+00:00
reviewer_ids: [1, 2, 3]
cross_response_reviewer_ids: [1, 2, 3]
force_resubmit: True
---

# Consolidated Review Report — Round 14 (Fresh)

**Paper**: "Vision Encodes, Language Reorganizes: Token-Level Representational Analysis of VLA Fine-Tuning"
**Target Venue**: CoRL 2026 (deadline 2026-05-29)
**Reviewers**: R1 (方法/实验严谨性), R2 (新颖性/scope/完整性), R3 (写作质量/格式合规/可复现性)
**Review Date**: 2026-05-20

---

## Summary

本文对 VLA（Vision-Language-Action）模型的微调过程进行逐层、逐 token 类型的表征分析。以 OpenVLA-7B 为主要分析对象，辅以 TraceVLA 做跨架构对比，提出三个发现：(1) 微调将指令注意力重新分配至 entry-exit 层，L1 为主要 hub；(2) 两个不同架构的 VLA 在训练后达到相似的中层表征（Δ=0.003）；(3) image token 与 readout token 存在功能分化——image token 对指令不敏感，readout token 是多模态整合中心。论文包含 7 项互补分析（interventional、supporting、constraining）和 21 页附录。

---

## Strengths

**S1. 系统性的多层次分析框架** [R1, R2, R3 共识] — 从注意力头统计、RSA、CKA、线性探针、消融、反事实、剂量-反应等 7 个互补视角对 VLA 微调进行分析，形成 interventional → supporting → constraining 的证据层次。这种三角验证的方法论在 VLA 机制分析中尚属首次，且方法论本身可迁移至其他 VLA 研究。

**S2. Readout token 发现具有实用价值** [R1, R2] — 发现 readout token 是多模态整合的主要位点（R²=0.678 vs image_mean 的 chance-level），而 image token 对指令不敏感。这一发现对 VLA 架构设计（如 early-exit 推理、微调诊断）有直接指导意义。

**S3. 训练-未训练因子设计** [R1, R3] — 对训练/未训练模型进行成对比较，使用因子控制隔离微调效应，而非仅报告训练后状态。这使得因果推断更可信。

**S4. 附录极为详尽** [R1, R2, R3] — 21 页附录覆盖鲁棒性检验（距离度量、per-DOF、permutation、seed、demo subsample）、OOD 诊断、跨 benchmark (LIBERO-Spatial) 验证等。R3 特别指出可复现性做得好（checkpoint、dataset、seed、compute 均报告）。

**S5. 剂量-反应分析** [R1, R3] — 4→32 头渐进消融呈现单调递增而非阈值效应（d=0.48→0.64），为 L1 注意力头的功能重要性提供了介入性证据。R3 进一步指出 counterfactual instruction analysis 中 shuffled condition (d=0.625) 对 positional sensitivity 的确认也有信息量。

**S6. 实验设计严谨** [R3: Soundness 7/10] — factorial controls、7 种互补分析、cross-architecture 验证、demo-level split 消除时间泄漏、linear probe sensitivity analysis 等方法论质量高。

---

## Weaknesses

### Must-Fix（不修复则建议拒稿）

**W-MF1. CoRL scope 适配性不足** [R1, R2, R3 三方共识——本轮最高优先级问题]
论文是纯分析/解释性工作，无机器人实验、无闭环验证、无策略改进。CoRL 2026 CFP 明确要求 "demonstrate the relevance of proposed models, algorithms, datasets, and benchmarks to robotics" 并警告 "papers lacking robotics emphasis will be desk-rejected"。论文的 actionable insight（如 early-exit 推理、L1 entropy 监控）仅作为假设提出，未做任何验证。Discussion 中 "orthogonal contribution and a natural next step" 的措辞显得对闭环验证过于轻描淡写。R3 补充了一个尖锐观察：ablation 后 MSE 几乎不变（0.498→0.497），这反而质疑了 routing 的功能意义——闭环 success rate 测量将直接回答这个问题。
**建议**：要么补充至少一个 downstream 应用实验（如 L1 attention entropy 与 task failure 的相关性——在现有 rollout 数据上即可计算，成本低），要么将 venue 转向 ICML/NeurIPS 的 interpretability track。

**W-MF2. "Convergent reorganization" 声称过强** [R1, R2, R3 三方共识]
仅两个模型（OpenVLA, TraceVLA）的 Δ=0.003 不能支撑 "convergent" 这一暗示普遍性的术语。两个架构共享 causal decoder + ~32 layers + LIBERO + tokenized actions，本质上是同一架构家族内的比较。Exit-layer R² 差异 0.069 与 mid-layer Δ=0.003 形成矛盾，论文仅以 post-hoc speculation 解释（"possibly reflecting architectural differences"）。N=2 的跨架构比较本质上是 case study，无法排除巧合。
**建议**：将 "convergent" 降级为 "consistent" 或 "preliminary evidence"；精确界定收敛范围（仅 mid-layer，exit-layer 分歧）。

**W-MF3. 统计效力不足（N_eff=10）** [R1, R2, R3 三方共识]
Bootstrap 基于 10 个 task 的聚合，N_eff=10 严重限制了统计推断的可靠性。LIBERO-Goal Δ=+0.017 n.s. vs LIBERO-Spatial Δ=+0.023 p<0.001——差异仅 0.006 但显著性截然不同，说明 power 不足。R3 补充：Table 11 的 Mann-Whitney U 检验在 N=6 vs N=4 上得到 p=0.033，在如此小 N 下解释力有限。
**建议**：提供 power analysis（N=10 可检测的最小效应量）；对跨架构 convergence 使用 TOST 等价性检验。

**W-MF4. 正文超出 8 页限制** [R3 独立发现——desk rejection 风险]
正文约 8.7 页，超出 CoRL 2026 的 8 页限制约 0.7 页。Discussion 的 Synthesis、Mechanistic interpretation、Functional stages、Limitations 四个段落 + Conclusion 延伸到第 9 页。这是 desk rejection 的常见理由。**注意**：此问题在 Round 12-13 曾被修复，但 R14 fresh review 发现回归。
**建议**：将 Discussion 中 Mechanistic interpretation 和 Functional stages 的预测性内容移至 Appendix；压缩 Introduction 中与 Abstract 重复的量化描述。

**W-MF5. Abstract/Introduction 信息过载** [R3 独立发现]
Abstract 在 ~200 words 内塞入了至少 15 个定量结果（d=0.48→0.64、p=0.033、R²+0.069、2.5× 等），远超同领域论文的 abstract 信息密度。Introduction 几乎逐字重复 abstract 的所有量化结论。R3 评 Clarity 仅 4/10。**注意**：同 W-MF4，此问题也是回归。
**建议**：Abstract 只保留 3 个核心发现的定性描述 + 1-2 个关键数字；Introduction 聚焦 motivation。

### Should-Fix（不影响接收决定，但显著提升论文质量）

**W-SF1. Cohen's d 计算方法需澄清** [R1 提出, R2 部分反驳, R3 同意——唯一未完全解决的技术分歧]
R1 认为对配对数据使用标准 Cohen's d 可能高估效应量。R2 反驳指出 paired d_z = mean_diff / SD_diff > standard d（因 SD_diff < SD_pooled when r>0），当前报告反而保守。R3 从不同角度支持 R1——token-level observations 有强时序相关性。**技术分歧**：偏差方向在数学上 R2 更准确，但三方共识是应明确报告使用的公式和配对版本数值。
**建议**：报告 paired d_z 和配对相关系数 r；在 Method 中讨论选择。

**W-SF2. 仅 LIBERO 基准** [R1, R2, R3 共识]
所有实验基于 LIBERO 家族（Goal + Spatial），instruction diversity 有限——10 个 tasks 的差异主要在 object 和 target location。缺少更复杂 benchmark（如 CALVIN、Language-Table）的验证。
**建议**：至少在 Discussion 中讨论 LIBERO 特异性风险。

**W-SF3. 缺少关键参考文献** [R1, R2, R3 共识]
(a) Aghajanyan et al. (ACL 2021, intrinsic dimensionality of fine-tuning) 和 Kumar et al. (NeurIPS 2022, fine-tuning distorts pretrained features) 与核心问题直接相关但未引用 [R1, R2]
(b) VLA efficiency/pruning 工作（如 TinyVLA, ECoT）未覆盖 [R1, R2]
(c) 多条引用仍使用 arXiv preprint 而非已发表版本——R3 列出 6 条具体条目（kim2024_openvla, karamcheti2024, touvron2023, belrose2023, padalkar2023, black2024_pi0）[R3]

**W-SF4. 单 checkpoint 分析** [R2 提出, R1 同意]
仅分析最终 checkpoint，缺少训练动态。至少在几个中间 checkpoint 上报告 L1 head count 或 readout R² 的演化趋势。

**W-SF5. Finding 3 定位需强化** [R2→R1 反驳→R2 接受→R3 nuanced 评价]
R2 初认为 Finding 3（image token instruction-blindness）near trivial——causal mask 的必然结果。R1 反驳区分三层：(a) image_mean at-chance 确实是 expected；(b) readout 从 L1 即 100% 是 non-trivial gradient；(c) training 不改变 image blindness 但大幅提升 readout 是 non-trivial asymmetry。R2 接受。R3 提供了关键 nuance：如果 image tokens 在 instruction tokens 之前（vision-first ordering），则 instruction-blindness 是 causal mask 的必然；但论文未明确声明 token ordering。
**建议**：正文明确声明 token ordering；Abstract 区分 expected（image_mean）vs surprising（readout gradient）部分。

**W-SF6. Figure 1 不在首页** [R3——回归问题]
Figure 1 出现在 PDF page 6，前 5 页全是密集文字。Round 13 曾声称修复但 R14 发现回归。

**W-SF7. Limitations 格式不满足 CoRL 要求** [R3]
Limitations 仍是 Discussion 的 `\paragraph`，而非独立 section。

**W-SF8. 层编号 off-by-one** [R3——回归问题]
method.tex: "L1--L31 the 32 transformer layers"——31 个索引 ≠ 32 层。

**W-SF9. 术语不一致** [R1, R2, R3 三方独立发现]
readout token / last_preaction；instruction-dominant heads / dominant heads / instruction heads 混用。

---

## Reviewer Consensus（三方共识）

1. **CoRL scope 是首要问题** — 三位审稿人均认为纯分析性论文缺乏 robotics 应用验证是最大短板
2. **"Convergent" 声称过强** — N=2 同质架构 + N_eff=10 的统计基础不足
3. **方法论框架本身有价值** — 三角验证方法论和 readout token 发现是实质贡献
4. **附录质量高** — 鲁棒性检验详尽，可复现性好
5. **需补充参考文献** — 多领域引用缺失；多条 arXiv 引用需更新
6. **闭环验证缺失** — 三方一致认为至少应验证一个 actionable implication

## Reviewer Divergence（分歧点）

| 议题 | R1 | R2 | R3 | 解决状态 |
|------|----|----|----|----|
| Finding 3 trivial? | Non-trivial（三层区分） | 初 trivial → 接受 R1 | Nuanced（需声明 token ordering） | ✅ 基本解决 |
| Cohen's d 偏差方向 | 可能高估 | paired d_z > standard d（保守） | Token 相关性高估 | ⚠️ 方向未解决，共识报告配对版 |
| MLP probe capacity | 过大（1.05M params） | 未强调 | 已充分回应（Appendix A.6） | ✅ R3 有力反驳 |

---

## Questions for Authors

1. L1 的 24/32 instruction-dominant heads 中，是否有 head 在 pretrained Llama-2 中已存在 instruction sensitivity？Fine-tuning 是 amplifying 还是 creating？
2. Δ=0.003 的 TOST 等价性检验（ε=0.05）的 p 值是多少？
3. 是否考虑过在训练中间 checkpoint 上测量 L1 head count 的演化曲线？
4. Readout token 的 R²=0.678——剩余 32.2% 的方差来源是什么？
5. Ablation 后 MSE 几乎不变（0.498→0.497），但 trajectory divergence d>0.6。如何 reconcile？
6. OpenVLA 的 token ordering 是什么？Image tokens 在 instruction tokens 之前还是之后？[R3 提出]

---

## Missing References

**高优先级**：Aghajanyan et al. (ACL 2021), Kumar et al. (NeurIPS 2022), "What Do Visual Tokens Really Encode?" (arXiv:2603.00510)
**中优先级**：TinyVLA/ECoT, diffusion VLA 表征分析, VLA scaling laws
**引用版本更新**（6 条）：kim2024_openvla, karamcheti2024, touvron2023_llama2, belrose2023_tunedlens, padalkar2023_oxe, black2024_pi0

---

## External Review

**外部审稿（Stanford Agentic Reviewer）：pending，未返回。**

---

## Visual Layout Check（非评分项）

- **Critical (1)**：Page 31 约 90% 空白
- **Warnings (4)**：Pages 2-4 无图表；Page 16 标签字号小；Pages 21, 30 表格密集
- **Info (21)**：次要排版观察

R3 的独立审查与视觉 Agent 发现一致。

---

## Overall Assessment

**Overall Score: 5.3/10 → Weak Reject**

| Reviewer | 侧重 | 初始分 | 最终分 | 变化原因 |
|----------|------|--------|--------|----------|
| R1 | 方法/实验严谨性 | 6/10 | 6/10 | 无变化 |
| R2 | 新颖性/scope/完整性 | 4/10 | 5/10 | 接受 R1 对 Finding 3 和 effect size 的反驳 |
| R3 | 写作/格式/可复现性 | 5/10 | 5/10 | 无变化 |

**R3 官方维度打分**：Significance 6/10, Relevance to Robotics 5/10, Soundness 7/10, Clarity 4/10, Reproducibility 7/10

**核心判断**：方法论框架和 readout token 发现是实质贡献，但五个结构性问题使其不适合当前形式投稿 CoRL：(1) 纯分析无闭环验证；(2) convergent claim 统计基础不足；(3) 超页限（desk rejection 风险）；(4) 可读性差（Clarity 4/10）；(5) LIBERO 单一 benchmark。

**特别警告**：R12-N2（超页限）和 R12-N3（信息过载）在 Round 13 曾被标记为 resolved，但 Round 14 fresh review 发现回归。Research Director 需验证修复生效。

**建议路径**：
- **若坚持 CoRL**（仅剩 9 天）：紧急压缩至 8 页 + 精简 Abstract/Intro + 补充 L1 entropy 验证（低成本）+ 弱化 convergent + 修复格式回归
- **若转投**：ICML/NeurIPS interpretability track 或 CoRL Workshop

---

## Detailed Comments

### 正文修改（按优先级排序）

1. 压缩正文至 8 页：Discussion Mechanistic interpretation + Functional stages 移至 Appendix
2. Abstract 删除至少 10 个定量数字，只保留核心 1-2 个
3. Introduction 删除与 Abstract 重复的量化描述
4. "convergent reorganization" → "consistent reorganization pattern"
5. "orthogonal contribution" → "complementary and necessary next step"
6. Limitations 提升为独立 section
7. 层编号 off-by-one 修复
8. 术语统一（readout token / instruction-dominant heads）
9. Figure 1 确保在 page 1
10. Token ordering 明确声明

### 统计方法

11. 报告 paired Cohen's d_z 和配对相关系数 r
12. 对 Δ=0.003 做 TOST 等价性检验
13. Power analysis（N=10 最小可检测效应量）
14. Permutation test 增加到 ≥10,000 shuffles

### 引用和格式

15. 新增引用：Aghajanyan 2021, Kumar 2022
16. 更新 6 条 arXiv → published
17. GenAI disclosure 移至 Appendix
18. Table 2 caption 展开缩写
19. Page 31 空白处理