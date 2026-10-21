---
round: 5
overall_score: weak reject
timestamp: 2026-05-18T09:17:22.000543+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿圆桌报告 — Round 6 (Fresh Review)

**论文**: Vision Encodes, Language Routes: Token-Level Functional Specialization in a Vision-Language-Action Model
**Venue**: CoRL 2026 (Deadline: May 29, 2026)
**Reviewers**: R1 (方法严谨性 + 实验设计) + R2 (新颖性 + 叙事完整性 + 格式合规)
**交叉回应**: R1↔R2 完成，Round 1 即收敛

---

## Summary

本文对 OpenVLA-7B 在 LIBERO 上进行 token 级表征分析，使用 cross-instruction probes、attention analysis、RSA 和 MLP probes，配合 trained/pretrained/untrained 三条件阶乘设计。三个发现：(1) image tokens instruction-blind（架构必然），(2) VLA fine-tuning 将 instruction routing 从 mid-depth 重组为 entry-exit 模式，(3) vision encoder 表征呈 metric-dependent 非单调变换。实验设计严谨，统计报告完整，但核心新颖性受限且存在方法论缺陷。

---

## Strengths

- **S1 [共识]**: 三条件阶乘设计（trained/pretrained/untrained × instruction presence）是该领域罕见的严格控制方案，能有效隔离语言预训练和 VLA fine-tuning 的各自贡献。优于 Grant 2026 等仅分析 trained model 的工作。
- **S2 [共识]**: 统计报告标准高——bootstrap CI (10,000 resamples)、FDR 校正 (Benjamini-Hochberg)、permutation test、seed sensitivity、demo subsampling sensitivity。在 VLA interpretability 文献中罕见。
- **S3 [共识]**: C2（routing reorganization）是最有实质价值的发现。三条件梯度（untrained 0/32 → Llama-2 base 9/32 → trained 24/32 heads at L1）在 30%-70% 阈值范围内稳定，有 cross-benchmark (LIBERO-Spatial) 复现。
- **S4 [共识]**: 四种分析方法（probing, attention, RSA, cross-instruction）从不同角度交叉验证，方法互补性好。RSA/CKA 分歧被坦诚报告而非回避。
- **S5 [共识]**: Related Work 与 Grant 2026 的三点差异化清晰有力，positioning 准确。

---

## Weaknesses

### Must-Fix（影响接收决定）

**W1 [CRITICAL, 共识]: Ablation 因果推断方向有根本性问题**
- 位置: Section 4.3, Appendix E
- 所有 ablation（dominant 24 heads: +0.042, random 24 heads: +0.077）都 INCREASE action R²
- 如果 instruction-dominant heads 功能重要，ablation 应 DECREASE R²
- "Dual routing-encoding function" 是 post-hoc rationalization；更 parsimonious 的解释是 L1 heads 普遍添加 interference
- 仅 N=10 random subsets，z-test 统计功效极低
- 这是论文唯一的因果证据——如果不成立，C2 的证据链从 "相关+因果" 降级为 "仅相关"
- **R1 评价更严厉**：认为这是 fundamental directionality problem，R2 同意并升级

**W2 [CRITICAL, 共识]: Probe train/test split 未说明 + 时间步自相关 + linear vs MLP 20× gap**
- 位置: Section 3.6, Section 4.1
- Train/test split 策略从未明确说明——R² 在哪个数据集上计算？
- 63,228 observations 来自 50 demos × 10 tasks × ~127 timesteps，相邻帧高度自相关
- 如果 random timestep split，test set 与 train set 近乎重叠，R² 严重高估
- Linear probe trained-untrained gap (Δ=+0.324 at L14) vs MLP gap (Δ=+0.015 at L8) 差 ~20×，说明 MLP 过强 rescue untrained representations，压缩条件差异
- Bootstrap CI 基于独立假设，时间自相关导致 CI 被低估

**W3 [CRITICAL, 共识]: 单模型 + 单 benchmark + Abstract overclaim**
- 位置: Abstract line 7, Introduction, Discussion
- Abstract 写 "instruction routing reorganization is the primary learned contribution of VLA fine-tuning"，这是对所有 VLA 的一般性声称，但证据仅来自 OpenVLA-7B + LIBERO
- Grant 2026 覆盖 6 个 VLA（80M-7B）形成鲜明对比
- LIBERO-Spatial 仍在同一框架（tabletop manipulation），不算独立泛化验证
- π₀ 使用 flow matching，entry-exit routing pattern 可能完全不同
- Limitations 列举了架构变量但 Abstract/Introduction 的 framing 未相应 qualify

**W4 [CRITICAL, 共识]: 缺少 behavioral validation**
- 位置: Discussion Section 5
- 论文所有发现在 representation space，从未连接到 task success rate
- R² 是离线指标，不等于 behavioral importance
- "Early-layer parameters may suffice for instruction adaptation"（Discussion）完全 speculative，无实验支撑
- 对 CoRL（机器人学习会议）是重大结构性缺口
- 即使 pilot 级别的 rollout 验证（L1 ablation → success rate）也能显著提升说服力

### Should-Fix（影响评分但不一票否决）

**W5 [WARNING, 共识]: C1 novelty 不足——架构必然 + probe trivially easy**
- C1 列为三大 contribution 之首，但 image tokens instruction-blind 是 causal mask + frozen encoder 的直接推论
- 10-way cross-instruction probe 在所有三条件 L1 均达 99.6-100%（含 untrained），任务 trivially easy
- Appendix K.1 作者自承 "even incidental attention (~12%) suffices"
- Round 5 已 reframe 为 "framework + verification"，但仍列为 contribution (i)
- 如果 C1 实质上是 sanity check，论文核心新颖性实质上只有 C2（+ C3 qualified）
- **注意**: 这本身是 WARNING 而非 rejection reason，但与 W1-W4 联合降低了整体 novelty bar

**W6 [WARNING, 共识]: RSA/CKA 分歧对 C3 影响被低估**
- Linear CKA 完全反转 RSA：per-layer 单调递增（无 inverted-U），encoder ordering 也反转
- 论文选择 RSA 作为主叙事，但未论证为何 rank-order geometry 比 covariance structure 对 action prediction 更 relevant
- C3 的 metric-dependence 使其作为独立 contribution 的 robustness 存疑
- R2 指出 metric selection 看起来 results-driven 而非 hypothesis-driven

**W7 [WARNING, 共识]: RSA 统计推断中 pairwise dependency 未处理**
- RDM 上三角 N(N-1)/2 entries 不独立，标准 bootstrap 低估 variance
- Permutation test 仅测试 structure 存在性，不测试条件间差异
- Same-layer L12 Δ=+0.079 的 significance 可能在正确统计下减弱
- Nili et al. (2014) 对此问题有标准处理方案

**W8 [WARNING, 共识]: 缺少 Generative AI 使用声明**
- CoRL 2026 Instruction for Authors 明确要求 Generative AI 使用声明
- main.tex 中未找到此声明
- 有 desk reject 风险

---

## Reviewer Consensus [AGREE]

两位 Reviewer 在以下关键判断上完全一致：

1. **C1 novelty 问题**：架构必然 + probe trivially easy，不应作为独立 contribution
2. **Ablation 方向性问题**：所有 ablation increase R²，dual-function 解释不 convincing
3. **Probe 方法论漏洞**：train/test split 未说明 + 自相关 + MLP/linear 20× gap
4. **单模型泛化性 + overclaim**：Abstract 一般化措辞 vs 单模型证据
5. **缺少 behavioral validation**：对 CoRL 是重大缺口
6. **C3 metric-dependence**：RSA/CKA 分歧未充分处理

---

## Reviewer Divergence [REBUT]

分歧极小，仅在以下次要点：

| 议题 | R1 | R2 | 解决 |
|------|----|----|------|
| Abstract 数据密度 (R2-W6) | REBUT → INFO | WARNING | 降为 INFO（部分数字核心支撑应保留，z-score 等移除） |
| Q4 baseline R² 差异 | 论文脚注已解释 | 提问 | R1 指出 Section 4.3 脚注 1 已明确回答 |
| Mantel test (Q6) | 建议 | PARTIAL REBUT | R2 认为 stimulus-level bootstrap 更合适，但核心关切一致 |
| 评分 | 5/10 | 4/10 | R1 对 C2 routing reorganization 评价稍高 |

---

## Questions for Authors

1. Action probe R² 在 training set 还是 held-out test set 上计算？Train/test split 策略是什么（random timestep / demo-level / task-level）？
2. 所有 head ablation（dominant 和 random）都 increase R²。是否意味着 L1 heads 对 action prediction 是 net-negative 的？如果是，"dual routing-encoding function" 如何成立？
3. Untrained readout 在 L1 达到 100% classification，但 untrained 有 0/32 instruction-dominant heads。如果 12% incidental attention 已够 100% 分类，VLA training 将 attention 提高到 57.7% 的功能意义是什么？
4. Linear probe gap (Δ=+0.324 at L14) vs MLP probe gap (Δ=+0.015 at L8) 差 ~20 倍，对结果解释有何影响？论文应以哪个为主？
5. Pretrained Llama-2 的 mid-depth routing pattern 是 meaningful processing 还是 OOD response？用 random noise tokens 替代 visual tokens 是否会产生类似 pattern？
6. Bootstrap CI 的 resampling unit 是什么？如何处理同一 demo 内时间步的高度自相关？
7. RSA 显示 DINOv2 几何最优 (ρ=0.692)，R² 显示 VLA readout 功能最优 (0.678)。"Vision encoder quality emerges as a key design lever" 的操作化定义是什么？

---

## Missing References

- **Hewitt & Liang (2019)** "Designing and Interpreting Probes with Control Tasks" [probe selectivity，直接相关方法论]
- **Nili et al. (2014)** "A Toolbox for Representational Similarity Analysis" [RSA 统计推断最佳实践]
- **Bills et al. (2023)** "Language models can explain neurons in language models" [mechanistic interp 方法论基础]
- **Templeton et al. (2024)** "Scaling monosemanticity" [SAE 方法论，与 Swann 2026 相关]

---

## External Review (Stanford Agentic Reviewer)

外部审稿：未请求（项目未配置外部审稿）。

---

## Overall Assessment

**Score: Weak Reject (4.5/10)**

| 维度 | R1 | R2 | 共识 |
|------|----|----|------|
| Originality | 6/10 | 4/10 | 5/10 |
| Quality/Soundness | 4/10 | 7/10 | 5.5/10 |
| Clarity | 7/10 | 6/10 | 6.5/10 |
| Significance | 5/10 | 4/10 | 4.5/10 |
| Relevance to CoRL | 5/10 | 7/10 | 6/10 |

**Confidence: High**

**核心判断**: 实验设计和统计报告质量优秀，C2（routing reorganization）有实质价值。但存在四个结构性问题的联合影响：(1) ablation 因果推断方向反直觉且解释不 convincing，(2) probe 方法论有未公开的关键细节（train/test split, 自相关），(3) 单模型证据 vs 一般化声称，(4) 纯 representation analysis 无 behavioral validation 对 CoRL 不够。三大 contribution 中 C1 是架构验证、C3 是 metric-dependent observation，实质新颖性集中在 C2，而 C2 的因果证据链（ablation）存在方向性问题。当前版本 below acceptance threshold。

**可修复性评估**: W1 (ablation) 需要新实验（细粒度 ablation curve + selective ablation + 更多 random subsets）或叙事大幅修改；W2 (probe split) 可通过补充说明和 demo-level split 重分析修复；W3 (overclaim) 可通过 framing 修改修复；W4 (behavioral validation) 需要 rollout 实验。如果时间允许（deadline May 29），W2+W3 可在 11 天内完成；W1 的新实验和 W4 的 rollout 验证时间紧张但可能可行。

---

## Detailed Comments

### Abstract
- 数据密度过高（~15 个数字），z=-2.73 和具体头数不适合 Abstract
- "instruction routing reorganization is the primary learned contribution of VLA fine-tuning" 是 overclaim
- 建议保留 2-3 个核心数字，移除统计细节

### Introduction
- 5 段结构完整，叙事逻辑清晰
- Contribution (i) "verifying architecture-expected specialization" 作为 contribution 列首位降低 novelty 感知
- Contribution (iii) 在 contribution 列表中提及 "CKA diverges" 让读者困惑

### Related Work
- 覆盖全面（VLAs, mechanistic interp, behavioral analysis, token specialization, similarity methods）
- 与 Grant 2026 差异化清晰
- 缺 Hewitt & Liang 2019 (probe design) 和 Nili 2014 (RSA statistics)

### Method
- 清晰可复现，四种方法选择有 justify
- "Why RSA over CKA" 段落理由合理但不完全令人信服（未论证 rank-order 对 action prediction 更 relevant）
- 缺少 train/test split 的明确说明

### Experiments
- Section 4.2: 结果 clean 但 C1 novelty 问题持续
- Section 4.3: 最强贡献，三条件梯度有说服力。但 ablation 方向性问题（所有 ablation increase R²）严重削弱因果推断
- Section 4.4: 数据详实但 CKA 矛盾仅在 Appendix 讨论

### Discussion
- 过于简短。Limitations 仅半段，嵌入 Discussion 而非独立 section
- "Speculative mechanistic interpretation" 标题过于自我贬低
- 缺少对 probe methodology limitations 和 behavioral validation gap 的讨论

### Appendix
- 内容丰富且组织良好（robustness, cross-benchmark, diagnostics）
- CKA 矛盾结果和 QA probe 的 1pp 差异对主文叙事有重大影响，应在正文 summarize