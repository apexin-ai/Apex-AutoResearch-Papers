---
round: 9
review_mode: fresh
overall_score: 3.0 Findings
timestamp: 2026-05-25T21:33:48.271971+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# Round 9 审稿报告

**Venue**: EMNLP 2026 (via ARR)
**论文**: "How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in Reasoning LLMs"
**评审人**: Reviewer 1（方法严谨性 + 实验设计）、Reviewer 2（新颖性 + 完整性）
**模式**: Fresh（重新审稿）

---

## Summary

本文提出 RASP（Recovery-Aware Structured Pruning），通过乘法形式结合 importance score 和 CKA-based diversity score 进行 MLP 结构化剪枝，并系统研究不同剪枝标准对 GRPO 恢复训练的影响。核心发现是 "recovery capacity spectrum"（CKA-only > RASP > Random > Standard）和 "reward-accuracy decoupling"（GRPO 提升 reward 但 accuracy 改变 <1pp）。

然而，RASP 方法被自身消融实验否定：CKA-only（RASP 的 α→∞ 极端情况）在 recovery capacity 上与 RASP 最优配置（α=2.0）完全相同（Peak Rew = 0.354），而 accuracy 差异仅 1.72pp（单 seed，不可信）。论文最终推荐 CKA-only 而非 RASP——方法贡献不成立。

---

## Strengths

**S1** [双 Reviewer 共识] 受控实验设计理念在 pruning 文献中罕见——isolation design 使得 criterion effect 可比较。实验设计哲学值得推广。

**S2** [双 Reviewer 共识] Reward-accuracy decoupling 是 genuinely surprising 的实证发现，对 RLVR 社区理解 post-pruning RL recovery 有参考价值。

**S3** [Reviewer 1] f₀/gradient norm/KL divergence 等多维训练动态分析工具有独立价值，提供了比 final accuracy 更丰富的诊断视角。

**S4** [Reviewer 1] 跨模型（Qwen2.5-Math-7B SFT）、跨尺度（1.5B）验证展示了系统性 validation 意识，即使覆盖面有限。

**S5** [Reviewer 2] Recovery capacity spectrum 作为描述性框架有参考价值（即使 RASP 贡献不成立）。

**S6** [双 Reviewer 共识] 写作清晰，Figure 2 有效传达实验设计，超参数报告详尽，代码已匿名开源。Reproducibility 评 4/5。

---

## Weaknesses

### Critical

**C1** [双 Reviewer 共识] **RASP 方法贡献被全参数空间否定**
- α=1.0（名义"平衡"点）：reward collapse（Peak Rew 0.061，四方法最差）
- α=2.0（最优配置）：Peak Rew = CKA-only Peak Rew = 0.354（完全相同）；accuracy +1.72pp 为单 seed 不可信
- α→∞：即 CKA-only 本身
- 论文最终推荐 CKA-only 而非 RASP——当提出的方法被其自身特例超越时，方法贡献不成立
- **影响**: 论文定位需从 "method paper" 转为 "empirical study"

**C2** [双 Reviewer 共识] **乘法形式 I(h)=0 退化未与加法替代对比**
- $S_{RASP}(h) = I(h) \times (1-F(h))^\alpha$ 意味着 $I(h)=0$ 的结构无论 diversity 多高都被零化
- 这恰恰是 α=1.0 collapse 的可能机制——高 diversity 但低 importance 的结构被不当移除
- 加法形式 $S = \beta \cdot I(h) + (1-\beta) \cdot (1-F(h))$ 不存在此退化，是自然的 ablation 对照
- 缺少此对照无法判断 collapse 是乘法 artifact 还是 tradeoff 本质
- 先例存在：Molchanov et al. (2019) "Importance Estimation for Neural Network Pruning"

**C3** [双 Reviewer 共识] **RASP 全部 α 变体仅单 seed，dose-response 曲线不可靠**
- CKA-only/Standard/Random 各 3 seeds，但 RASP 全部 α 值（0.5-4.0）均单 seed
- Inverted-U 结论完全基于单次运行
- α=2.0 的 66.11% vs CKA-only 64.39±0.19% 的 1.72pp 差距：RASP 方差未知
- 如果 RASP 方差与 CKA-only 相当（~0.19pp），1.72pp 可能显著；但 RASP 跨 α 表现巨变（从 collapse 到 66%）暗示高方差
- **连续 5 轮 Critical 未解决**（Round 5 至今）

**C4** [Reviewer 2, R1 部分同意] **Reward-accuracy decoupling 可能是 SFT 天花板效应 artifact**
- SFT 已恢复 ~60pp accuracy（从 post-prune ~4% 到 ~64%），GRPO 无 headroom
- 15% sparsity 数据自相矛盾：GRPO amplifies CKA-only vs Standard gap (+1.51pp)，说明低 sparsity 下 GRPO 确实能放大差异——暗示 20% 下的 "decoupling" 是 headroom 耗尽
- 需消融实验：在 SFT 恢复不充分条件下验证 GRPO 是否产生 accuracy 差异

**C5** [双 Reviewer 共识] **Cross-architecture 泛化严重不足——所有模型共享 Qwen2.5 base**
- Title 用 "Reasoning LLMs"（复数）但仅验证 Qwen2.5 架构族
- Qwen2.5-Math-7B 仅有 SFT 验证，GRPO 缺失
- 1.5B 同属 Qwen2.5 family（跨尺度但非跨架构）
- **连续 5 轮 Critical 未解决**（Round 5 至今）

### Warning

**W1** [双 Reviewer 共识] Random baseline max_completion_length=512 vs 其他方法 1024，违反受控设计自称的 "hold everything else constant"。核心 CKA vs Standard 比较不受影响，但 spectrum 含 Random 的排序不可信。

**W2** [双 Reviewer 共识] TOST ε=2pp 缺乏 a priori justification。如果 ε=1pp，部分 "等价" 结论不成立。需引用文献或 power analysis 论证 2pp 的实际意义。

**W3** [Reviewer 1, R2 同意] 15% sparsity 下 GRPO 放大 CKA 优势（+1.51pp），Standard Δ=-0.93pp 接近 1pp 边界——decoupling 并非在所有 "moderate sparsity" 下普遍成立。

**W4** [Reviewer 1, R2 同意] 300-step extended training 仅报告终值（100 步和 300 步），缺少中间步骤 accuracy trajectory。300 步远少于 RLVR 文献常见预算（1000-5000 步）。

**W5** [Reviewer 2] Title/叙事焦点与 SFT-dominant 发现错位——SFT 贡献 ~60pp 恢复而 GRPO <1pp，但叙事聚焦 GRPO。

**W6** [Reviewer 2] Ji et al. (2026) 对比 overclaiming——实验设置差异未充分讨论。

**W7** [Reviewer 2] Discussion 被放 Appendix，正文 Section 5 仅约 7-8 行，缺少 spectrum 部署指导意义和机制解释。

**W8** [Reviewer 1, R2 同意] Limitations 关于 Random seed 的表述（称 "单 seed"）与正文矛盾（实际 3 seeds）。此类不一致降低审稿人对其他声称的信任度。

**W9** [Reviewer 2] 有效窗口仅 20-25% MLP sparsity（实际压缩比约 12-15%），30% 全面崩塌。Abstract 用 "moderate sparsity" 模糊处理。论文定位 controlled study 可接受，但需诚实面对实用限制。

### Minor

**M1** [Reviewer 1, R2 同意] Recovery capacity 概念先用后定义——Section 1 使用该术语但 Section 3 才定义。

**M2** [Reviewer 1] Calibration M=512 importance score 稳定性未独立验证（CKA ranking 稳定性已验证但 importance 未验证）。R2 部分反驳：Taylor expansion 是标准做法，M=512 超过 LLM-Pruner 的 calibration 规模。

**M3** [Reviewer 1, R2 同意] 25% sparsity 单 seed，Standard Δ=+0.99pp 恰在 1pp 边界。R2 反驳严重程度：25% 非核心 claim 支撑。

---

## Questions

Q1: 如果跑 additive baseline $S = \beta \cdot I(h) + (1-\beta) \cdot (1-F(h))$，α=1.0 对应配置是否仍 collapse？这将判定 collapse 归因于乘法 artifact 还是 tradeoff 本质。

Q2: 如果 α=2.0 补跑 3 seeds 方差很大（e.g., σ>1pp），RASP 相关叙事是否需要全部删除？

Q3: 在 SFT 步数减少（如仅 50% SFT steps）的条件下，GRPO 是否能产生显著 accuracy 差异？这将验证 decoupling 是否为天花板效应。

Q4: 为什么不统一 Random 的 max_completion_length 为 1024？成本极低（单 seed 约几小时 GPU）。

Q5: 15% sparsity 下 GRPO 放大差异与 20% 下 decoupling 的矛盾如何解释？

Q6: Extended training 150-200 步的 accuracy 曲线是否可用？

---

## Missing References

1. **Molchanov et al. (2019)** "Importance Estimation for Neural Network Pruning" — 加法形式多标准组合先例，直接相关于 RASP vs additive 对比
2. **Li et al. (2025, arXiv:2504.02010)** "When Reasoning Meets Compression" — 直接 benchmark 剪枝对 DeepSeek-R1 推理影响（Round 8 已提出，仍缺失）
3. **"Can Pruning Improve Reasoning?" (2025, arXiv:2505.14582)** — 剪枝与推理能力关系（Round 8 已提出，仍缺失）

---

## External Review

**状态**: 未请求（not_requested）

---

## Visual Layout Check

**状态**: Agent 错误（rate limit hit）
- 视觉审查 Agent 因 rate limit 退出，未产出有效 findings
- 建议后续手动检查或重试

---

## Overall Assessment

**Score: 3.0 (Findings)**
**Confidence: 4/5**
**双 Reviewer 一致**

### 评分理由

**为什么不是 3.5+ (Conference)**:
- 核心方法贡献 RASP 被自身消融否定——论文的方法新颖性基本为零
- 乘法形式缺少加法对照，无法判断核心消融结论的归因
- RASP 全部 α 变体单 seed，dose-response 结论统计不可靠
- 跨架构泛化严重不足（连续 5 轮未解决）
- Decoupling 可能是 SFT 天花板 artifact（未排除）

**为什么不是 2.5 (Borderline Findings)**:
- 受控实验设计哲学在 pruning 文献中有方法论价值
- Reward-accuracy decoupling 即使是初步发现也对 RLVR 社区有参考价值
- 核心比较（CKA-only vs Standard）有 3-seed 统计验证
- 写作质量高，再现性好
- Training dynamics 多维分析工具有独立价值

### 修改路径建议（如目标 Findings 接收）

1. **必做**: 重新定位为 empirical study；RASP 降级为 exploratory analysis
2. **必做**: Title 限定为具体架构或加 "A Case Study"
3. **强烈建议**: 跑 additive baseline（成本低），α=2.0 至少 3 seeds
4. **强烈建议**: 统一 Random max_completion_length=1024
5. **建议**: 正文 Discussion 扩充；诚实标注 12-15% 实际压缩比

---

## Detailed Comments

### 给作者的核心建议

本文最大的问题不是实验不够多，而是**定位错误**。当前论文试图同时作为 method paper（RASP）和 empirical study（spectrum + decoupling），但数据明确否定了 RASP 的方法贡献。如果重新定位为纯 empirical study——"受控实验揭示 CKA-based diversity preservation 是 RLVR recovery 的关键因素，且 reward 信号与 accuracy 解耦"——现有数据足以支撑 Findings 级别的贡献。

具体来说：
- Section 3.3 的 RASP 公式推导可保留但作为 "exploration of criterion combination" 而非核心方法贡献
- Abstract 的第一句应改为 empirical finding 而非 method proposal
- 核心贡献列表应以 controlled experiment framework 和 decoupling finding 为主

### Reviewer 交叉共识度

| 问题 | R1 | R2 | 共识 |
|------|----|----|------|
| RASP 全空间否定 | Critical (N1) | Critical (C2) | 完全一致 |
| 乘法 vs 加法 | Critical (N2) | AGREE | 完全一致 |
| 单 seed 不可靠 | Critical (N4) | Critical (强烈同意) | 完全一致 |
| Random 超参不一致 | Critical (N3) | Warning (nuance) | 方向一致，严重程度小分歧 |
| SFT 天花板 | Warning (隐含) | Critical (C1) | 方向一致，R2 更强硬 |
| 有效窗口窄 | Warning (W2/W3) | Critical (C3) | 方向一致，R2 更强硬 |
| TOST ε=2pp | Warning (W1) | AGREE | 一致 |
| 25% sparsity | Warning (W3) | REBUT (非核心) | 小分歧 |
| Calibration M=512 | Warning (W6) | REBUT (标准做法) | 小分歧 |

交叉回应后无未解决的重大矛盾。