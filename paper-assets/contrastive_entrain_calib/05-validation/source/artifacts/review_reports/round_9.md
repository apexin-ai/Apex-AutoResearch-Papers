---
round: 9
review_mode: fresh
overall_score: 3.0 - Findings
timestamp: 2026-05-24T23:07:37.219974+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# Round 9 审稿报告

**Venue**: EMNLP 2026 (via ARR)  
**Format**: Long paper (8-page limit)  
**Reviewers**: R1 (方法严谨性 + 实验设计), R2 (新颖性 + 完整性)  
**轮次**: Round 9 (fresh mode)  
**收敛**: 1 轮初审 + 交叉回应即达成共识，无需追加轮次

---

## Summary

本文系统诊断了 probe-based reward signals（linear probing direction d_syc）用于 GRPO 训练时的失败模式，并报告了一种 "probe reward trap" 现象——SFT 训练中 probe reward 持续上升但行为能力在约 1,300 步后崩溃（behavioral death）。论文对比了 Activation-Conditional Training (ACT) 的 100% 成功率与 GRPO 的 14% 成功率 (4/28)，试图从 reward signal 语义局限和 supervision granularity 两个角度解释差异。

论文的诊断方法系统且工程执行完整，但核心结论受制于：(1) probe reward trap 仅 1 seed 验证，(2) ACT vs GRPO 对比存在 5+ 未控制 confounds，(3) gs=8 ablation 样本严重不足。

---

## Strengths

**S1 [R1+R2 共识]**: 系统性诊断框架——论文不是简单报告失败，而是构建了多层次诊断链（direction quality → cosine failure → probe trap），逐步排除替代解释。这种方法论对社区理解 reward misalignment 有教育价值。

**S2 [R1+R2 共识]**: Probe reward trap 的 temporal decoupling 量化——probe reward 持续上升而行为在 ~1,300 步后崩溃，且 entropy 监控无法提前预警。这一 temporal 结构是论文最独特的经验贡献。

**S3 [R1]**: Cosine reward failure chain 分析（Table 2）清晰展示了 cosine similarity 作为 reward signal 的系统性缺陷。

**S4 [R2]**: 实验覆盖面广——6 种 GRPO reward 配置 × 多种消融，对 negative results 的报告系统全面。

**S5 [R1+R2]**: ACT 方法本身表现强劲（47/47 checkpoints 保持 ToF > 0），提供了可行的替代方案。

---

## Weaknesses

### Critical

**W1 [R1+R2 共识]: Probe reward trap 仅 n=1 seed 支撑**  
标题级贡献（probe reward trap 及 1,300-step lag）基于单一实验观察。两位 Reviewer 一致认为：(a) 需验证现象是否跨 seed 稳定复现，(b) 需报告 lag 时间的方差——如果不同 seed 下从 500 到 3,000 步不等，entropy 监控失效论证的实践意义显著不同。**建议至少追加 2-3 seeds，报告 mean±std。**

**W2 [R1+R2 共识]: ACT vs GRPO 对比存在严重 confounds，因果声明过强**  
两种方法在以下维度同时不同：(1) supervision granularity (per-token vs per-completion)，(2) 序列长度 (1024 vs 256 tokens)，(3) 数据源 (contrastive pairs vs policy rollouts)，(4) dropout 策略，(5) reward signal 形式。256-token truncation 使 d_syc AUROC 从 0.76 降至 0.60。论文中 "strongest candidate explanation" 等因果声明未经充分隔离实验支撑。  
R2 进一步指出：即使去掉 d_syc (R3-only GRPO)，GRPO 仍然失败（4/28），说明 truncation 对 d_syc 的影响不是唯一因素；但 R3 (NLI reward) 在 256-token 上的性能也未报告。**目前无法排序 supervision granularity vs seq_len 的相对重要性。**

**W3 [R1+R2 共识]: gs=8 ablation 样本量严重不足**  
gs=8 ablation 仅 3 checkpoints (0/3)，以 "declining trajectory" 为由 early termination。(a) early termination 的决策标准未明确——如果是人工判断，引入选择偏差；(b) 如果对 gs=2 实验也应用同样的 early termination 规则，4/28 是否会更少？(c) 3 个 checkpoint 的 declining trajectory 不能排除 group size 不足是 GRPO 失败主因这一替代假说。

**W4 [R1]: Contrastive pairs 无人工验证**  
全部 181 对由 GPT-4.1 生成，evidence strength 标注无 inter-annotator agreement。论文用 cross-model generalization (Qwen 上训练的 probe 用 GPT 数据) 作为间接验证，但不能排除 probe 捕捉的是生成风格而非 sycophancy 语义。建议人工标注 50 对验证。

**W5 [R2]: 核心命题与 Goodhart's Law regressional variant 高度同构**  
"discriminability ≠ reward utility" 本质上是 Goodhart's Law 的 regressional variant（Manheim & Garrabrant, 2019）。论文引用该工作但仅一句话，未与四分类体系（regressional/extremal/causal/adversarial）进行实质对话。增量贡献（temporal decoupling 量化）应被更锐利地定位。

**W6 [R2]: Conclusion 因果归因逻辑错误**  
Conclusion 将 d_syc 语义局限归因为**所有** GRPO 配置失败的原因，但 R3-only GRPO 不使用 d_syc。这是逻辑错误而非措辞问题——R3-only 的失败需要独立解释（per-completion granularity? NLI 在截断文本上的退化?），不能统一归于 d_syc。

### Warning

**W7 [R1+R2]**: 4/31 vs 4/28 数字不一致——Introduction 使用 "4 of 31 (12.9%)"，Table 4 使用 "4/28 across two seeds"。31 混合了 gs=2 (28) 和 gs=8 (3) 数据，分母不同且无解释，损害内部一致性。

**W8 [R1+R2]**: Cross-seed 分析仅 2 seeds，R3-only GRPO oscillation (Δ≈0.069 between seeds) 可能反映 gs=2 方差而非训练动态不稳定性。

**W9 [R2]**: SMART (per-step process reward) 讨论存在逻辑张力——如果几何不可分是根本限制，per-step rewards 为何能绕过？未解释 reasoning trajectory 的时序结构如何解决此矛盾。

**W10 [R2]**: §3 "captures evidential granularity" 与 §5-§6 "does not encode evidential warrant" 措辞矛盾，未做出 correlation-vs-encoding 的明确区分。

**W11 [R1]**: Table 4 ACT seed 2 的 ToF/NoF 标记为 "--"，应补全数据或解释缺失原因。

**W12 [R1]**: Train/eval 数据完全重叠（181 pairs），held-out split (146/35) 仅验证 ACT 且性能仅为 full-data 的 72%，GRPO 未做 held-out 验证。

---

## Questions

**Q1**: 不同 seed 下 probe reward trap 的 behavioral death timing 方差是多少？1,300 步是 mean 还是单次观察？

**Q2**: R3 (NLI behavioral reward) 在 256-token 截断 vs 全长文本上的分类准确率分别是多少？truncation 对 NLI 判断的影响程度如何？

**Q3**: gs=8 early termination 的精确决策标准是什么？是人工判断还是预设阈值？

**Q4**: 如果对 gs=2 实验也应用同样的 early termination 规则（3 连续 checkpoint declining），4/28 会变成多少？

**Q5**: 47/47 ACT 成功率是否包含 reduced-LoRA 消融变体？如果是，应分开报告（31/31 full + 16/16 reduced-LoRA）。

**Q6**: "Direction quality is not the bottleneck"（§3）——但训练时 AUROC 仅 0.60（truncation 后），这如何支撑 "high discriminability fails as reward" 的叙事？

---

## Missing References

1. **Hewitt & Liang (2019)** — "Designing and Interpreting Probes with Control Tasks"：probing 方法论的 selectivity 问题，直接影响本文 linear probe 结论的解释力
2. **Belinkov (2022)** — "Probing Classifiers: Promises, Shortcomings, and Advances"：probing 方法论综述，本文大量使用 linear probing 但未讨论其已知局限
3. **Lightman et al. (2023)** — "Let's Verify Step by Step"：PRM 文献，与论文讨论的 per-step vs per-completion reward granularity 直接相关
4. **Uesato et al. (2022)** — "Solving math word problems with process- and outcome-based feedback"：outcome vs process reward 对比的先驱工作
5. **Vennemeyer et al. (2025)** — "Sycophancy Is Not One Thing" (arXiv:2509.21305)：证明 sycophancy 多维可分解，提供 d_syc 失败的替代解释（待验证论文存在性）

---

## External Review

**状态**: 未请求

---

## Visual Layout Check（非评分项）

**状态**: ✅ 完成 (2026-05-24, 耗时 2m27s)  
**统计**: 0 critical, 2 warning, 6 info

| 严重度 | 位置 | 发现 |
|--------|------|------|
| ⚠️ warning | Page 3-4 | 连续两页纯文字，Page 3 仅 Eq.(1) 作为视觉断点，Page 4 无 display item。建议将 Figure 2 或方法示意图前移 |
| ⚠️ warning | Page 5 | 三个 display items (Table 1 + Table 2 + Figure 2) 集中同一页，与 Pages 3-4 形成明显密度不均 |
| ℹ️ info | Page 5 | Figure 2 legend 文字偏小，打印版接近可读性下限 |
| ℹ️ info | Page 5 | Table 2 "Root Cause" 列文字紧凑，检查是否 ≥8pt |
| ℹ️ info | Page 2 | Figure 1(b) 红/橙色在色盲视角下可能难区分，建议用 marker shape 辅助 |
| ℹ️ info | Page 8 | Figure 4 多条曲线灰度打印下难区分，建议添加不同 line style |
| ℹ️ info | Page 7 | Table 4 未标注次优结果（仅加粗最优） |
| ℹ️ info | Page 12 | 末页内容约 70-75%，略低于理想 80%+ 但可接受 |

---

## Overall Assessment

**Overall Score: 3.0 / 5 — Findings**

**理由**: 论文提供了一份系统性的诊断报告，对 probe-based reward 在 GRPO 中失败的多种模式进行了有条理的分析。probe reward trap 的 temporal decoupling 现象具有新颖性和实践警示价值。然而，核心结论受到三重限制：(1) 标题级贡献仅 n=1 支撑，(2) ACT vs GRPO 对比的多维 confounds 使因果归因不可靠，(3) gs=8 ablation 的样本量和 early termination 程序无法排除关键替代假说。此外，Conclusion 存在逻辑归因错误（将 d_syc 局限归因于不使用 d_syc 的配置），novelty 定位相对于 Goodhart's Law 不够锐利。

**升级路径 (→ 3.5 Borderline Conference)**:
1. 补充 2-3 seeds 验证 probe reward trap temporal decoupling 的稳定性，报告 lag mean±std
2. 统一 4/31 vs 4/28 数字，修正 Conclusion 因果归因逻辑
3. 降级因果声明（"strongest candidate explanation" → "one plausible explanation"）
4. 补充 Goodhart 四分类讨论，锐化增量贡献定位
5. 报告 R3 (NLI) 在 256-token 上的性能

**Reviewer 评分一致性**: R1 = 3.0, R2 = 3.0。双方交叉后无分歧。

---

## Detailed Comments

### 方法论

1. **Probe reward trap 证据强度**: 核心发现（1,300-step lag, entropy 监控失效）极度依赖单次实验。即使现象真实，不报告方差就无法判断其实践影响——如果 lag 高度可变，则 entropy 监控在某些 seed 下可能仍然有效。
2. **Sequence length confound 的分层影响**: truncation 对 d_syc-based GRPO 的影响路径清晰（AUROC 0.76→0.60），但对 R3-only GRPO 的影响需通过 NLI 性能报告来量化。两者不应混为一谈。
3. **gs=8 ablation 的选择偏差**: "declining trajectory" 作为 early termination 条件未预注册，且仅 3 个数据点。如果 gs=8 需要更多步数才能收敛（因为 group 内方差更大），early termination 可能过早截断了一个可能成功的实验。

### 新颖性与定位

4. **Goodhart's Law 关系**: probe reward trap = reward model 与 target behavior 之间的 regressional Goodhart 效应。论文的增量贡献在于量化了 temporal decoupling 结构——这在 alignment 文献中鲜有精确报告。建议显式定位为 "regressional Goodhart 的一个具有独特时间结构的实例"。
5. **三种 framing 游移**: 论文在 (a) systematic negative result, (b) 新现象发现 (probe reward trap), (c) 通用原则 (discriminability ≠ utility) 之间游移。建议选定 primary framing 并贯穿始终。(a)+(b) 最有证据支撑，(c) 证据不足。

### 写作与格式

6. **数字一致性**: 4/31 vs 4/28、0.827 vs 0.76→0.60、47/47（含 reduced-LoRA?）——多处数字需统一。
7. **术语定义**: "behavioral death" 贯穿全文但仅以 ToF=0 操作性描述，建议在首次出现时正式定义。
8. **缺失引用**: probing 方法论（Hewitt & Liang 2019, Belinkov 2022）和 PRM 文献（Lightman et al. 2023）与论文核心方法直接相关，应引用并讨论。