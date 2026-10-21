---
round: 0
review_mode: 
overall_score: Dream Best 3.5 | Dream Median 3.0 | Dream Worst 2.5 | Actual v1 2.5 | Actual v2 2.5 | Actual v3 2.5 — 不建议当前版本投稿，reframe degradation chain 后目标 3.0
timestamp: 2026-05-21T13:24:08.375062+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: True
---

# 审稿报告（最终版 v6）：irt_personfit_contam — 6 篇论文综合评估

**Target Venue**: EMNLP 2026 (ARR), Long paper, 8-page limit
**Round**: 1
**Reviewers**: R1 (方法/实验严谨性), R2 (新颖性/完整性)
**收敛状态**: 六份审稿评分完全一致（R1 = R2），无分歧

⚠️ **本报告为最终版 v6**，替换此前所有提交。覆盖 3 个 dream 版本 + 3 个实际论文版本。

---

## 评分总览

| # | 版本 | 标题关键词 | R1 | R2 | 共识 | 投稿建议 |
|---|------|-----------|----|----|------|---------|
| 1 | Dream Best | Detecting Benchmark Contamination | 3.5 | 3.5 | ✅ | 理想目标 |
| 2 | Dream Median | Characterizing Detection Frontier | 3.0 | 3.0 | ✅ | — |
| 3 | Dream Worst | Binary Response Bottleneck | 2.5 | 2.5 | ✅ | — |
| 4 | Actual v1 | Psychometric Diagnostics | 2.5 | 2.5 | ✅ | 不投 |
| 5 | Actual v2 | When Can Binary Response Patterns | 2.5 | 2.5 | ✅ | 不投 |
| 6 | **Actual v3** | **Person-Fit Statistics (HT variant)** | **2.5** | **2.5** | ✅ | **不投** |

**核心结论：三版实际论文均 2.5（Borderline Findings）。最新版（v3）暴露了此前未识别的 critical finding：HT ≈ lz*，4PL IRT 框架的全部复杂性被证明不必要。**

---

## 最新版实际论文评估（v3, HT variant — 最高优先级）

### 标题
"IRT-FIT: Person-Fit Statistics for LLM Benchmark Contamination Detection at the Minimal-Information Operating Point"

### Summary
论文将 IRT person-fit 统计量（lz* 和 HT）应用于 LLM benchmark contamination 检测。4 model families × 3 benchmarks × 6 contamination levels 控制实验。核心检测在 Qwen/Llama × MMLU 可行，Gemma/Mistral 失败，post-RL 后所有方法信号消失。

### 本轮最重要的新发现

**CRITICAL: 完整 Degradation Chain（4PL → HT → accuracy z-score）**

R1 识别、R2 确认的 degradation chain 是本轮审稿的核心结论：

1. **4PL lz* → HT（1-param）**：HT 仅用 item difficulty，在所有条件下 |d_HT - d_lz*| < 0.3, p>0.3。Discrimination (a)、guessing (c)、feasibility (d) 对检测力零贡献。
2. **HT → accuracy z-score**：结合此前审稿发现（lz* ≈ z-score +0.02-0.03 AUROC），三级简化均不损失检测力。
3. **Implication**：论文的全部 psychometric sophistication（4PL 拟合、lz* 计算、Snijders 标准化、PSN-IRT 依赖）是 unnecessary overhead。一个简单的 accuracy z-score 做到同样的事。

R2 评价："这是最后一根稻草。论文从 'complex method doesn't beat simple baseline' 升级为 'complex method doesn't even beat its own simplified version'。"

**这个发现应成为论文的核心叙事，而非 buried in results。**

### Strengths（R1/R2 一致）

**S1. Cross-disciplinary bridge genuinely novel**。将 60+ 年 psychometric person-fit 文献引入 LLM contamination detection，建立 vocabulary bridge。

**S2. Detection frontier / information access hierarchy**。Binary < re-test < token probs < weights 的层级 framing，使 "low AUROC" 不再是 failure 而是 "cost of minimal information"。

**S3. Post-RL boundary 明确划定**。|d|<0.5, ALL methods AUROC 0.51-0.53。诚实的 negative result，与 Wang et al. (2025) 一致。

**S4. θ-shift mechanism + memorization fraction**。SFT 通过全局 θ 提升（非 item-specific cheating）的机制解释。Memorization fraction（Qwen/Llama 0.32-0.35 vs Gemma/Mistral 0.15-0.17）提供 model-family boundary。

**S5. Scope-honest framing**。2/4 families × 1/3 benchmarks 显著的情况下没有 overclaim。

### Weaknesses（按严重度排序）

**W1 [Critical]: HT ≈ lz* undermines 4PL IRT necessity（NEW）**
- 整个 4PL 框架是 unnecessary overhead
- 论文未将此作为核心发现
- 应 reframe 为 "psychometric complexity is unnecessary for binary contamination detection"
- θ-shift mechanism 解释了 why：SFT contamination 不表现为 item-specific aberrance

**W2 [Major]: n=3 seeds 不报告 CI**
- Cohen's d 在 n=3 下 CI ≈ ±1.2
- Mistral/Gemma 仅 single seed → point estimates unreliable
- 所有 effect size claims 缺乏统计支撑

**W3 [Major]: 0 figures, 14+ tables**
- Characterization study 需要 visual characterization
- 缺少 detection frontier diagram、dose-response curves、ROC curves
- 严重影响 accessibility 和 persuasiveness

**W4 [Major]: Post-RL failure 限制 practical scope**
- 2025-2026 几乎所有 deployed LLMs 经过 RLHF/DPO/GRPO
- 方法仅限 SFT-only models

**W5 [Moderate]: 检测阈值过高**
- MMLU 10-15%, GSM8K 25%+
- 实际关注的 3-5% low-level contamination 无法检测

**W6 [Moderate]: 缺少 accuracy z-score baseline**
- 结合 W1（HT ≈ lz*），如果 z-score ≈ HT ≈ lz*，整个 person-fit framework 无附加值
- 必须加入以验证或否定

**W7 [Moderate]: Thin sections 浪费篇幅**
- lz,m: 一段话，负面结果 → 一句话
- Natural experiment n=5: p>0.28 → 删除或 appendix
- 释放空间给 figures/CI/HT discussion

**W8 [Minor]: 14 references, 无独立 Related Work**
- 远低于 EMNLP 标准
- 缺少 person-fit、contamination detection、LLM evaluation 核心文献

### Triple Threat（R2 分析）

n=3 seeds + 高检测阈值 + 无 simple baseline 的组合效应：
- 不确定方法是否有效（n=3 CI 太宽）
- 即使有效也只抓大问题（高阈值）
- 可能一个简单 z-score 就够（无 baseline 验证）
- 三者交集使 positive claims 基本无可靠支撑

### Overall Score: 2.5 (Borderline Findings)

4 Major issues (W1-W4)。HT ≈ lz* 是最 damaging 的发现——论文方法论的 raison d'être 被自己的数据否定。正面贡献（cross-disciplinary bridge, θ-shift, memorization fraction, detection frontier, degradation chain itself）足以考虑 Findings，但需要 substantial reframing + statistical fix。

---

## 跨版本一致性分析

### 6 版论文共同的正面贡献
1. Power function 理论框架（概念有价值，即使 R²=0.65）
2. Detection frontier / information access hierarchy
3. θ-shift mechanism + memorization fraction
4. 诚实的 negative result 呈现

### 6 版论文共同的问题
1. 0 figures（所有版本）
2. References 不足（7-14 篇）
3. 单一污染机制（QLoRA SFT）
4. Post-RL signal loss
5. IRT 参数适用性未验证

### 实际论文的累积问题（v1→v2→v3）
| 问题 | v1 | v2 | v3 |
|------|----|----|-----|
| lz* ≈ z-score | ✓ | ✓ | ✓ |
| HT ≈ lz* | — | — | **NEW** ✓ |
| n=3 seeds/no CI | — | ✓ | ✓ |
| R²=0.65 | — | ✓ | — |
| 10 pages | ✓ | ✓ | ✓ |
| 0 figures | ✓ | ✓ | ✓ |

**v3 的 HT ≈ lz* 是决定性的新发现**，完成了 4PL→HT→z-score 的 degradation chain，彻底否定了 IRT complexity 的附加值。

---

## 对 Research Director 的行动建议

### 不建议当前版本投 EMNLP 2026

理由：4 Major weaknesses（HT≈lz* + n=3 no CI + 0 figures + post-RL failure），R1/R2 一致 2.5。

### 建议 Reframing 方向

**核心叙事转型**：从 "IRT-FIT as detection tool" 转为 **"Why psychometric complexity fails for LLM contamination detection: the degradation chain and θ-shift mechanism"**

关键 message：
1. 4PL IRT → HT (1-param) → accuracy z-score，每步简化不损失 detection power
2. θ-shift mechanism 解释 why：SFT contamination 通过全局能力提升而非 item-specific cheating
3. Memorization fraction 量化了 generalization 对 signal 的稀释程度
4. Post-RL 是所有 binary methods 的 hard boundary（不仅是 IRT）

### 修复优先级

**Must-fix（投稿前提）**：
1. Seeds ≥10 + CI for all Cohen's d
2. 压缩至 8 页（删 thin sections，加 3-4 figures）
3. 加 accuracy z-score baseline（验证 degradation chain 最后一环）
4. 将 HT ≈ lz* 和 degradation chain 提升为核心发现
5. References ≥20 + 独立 Related Work section

**Should-fix（提升至 3.0）**：
6. 讨论 "when does full IRT parameterization matter"
7. 更多 model families 验证
8. 明确讨论检测阈值的 practical implications

### 投稿时间线

- **2026-05-25 deadline**：不投
- **下一 ARR cycle（~2026-07）**：完成 reframing + must-fix，目标 3.0 (Findings)
- **如 post-RL 突破（AUROC ≥0.85）**：目标 3.5 (Borderline Conference)

---

## Questions for Authors

Q1. HT ≈ lz*：是否考虑将 degradation chain (4PL→HT→z-score) 作为论文核心 narrative？

Q2. Accuracy z-score baseline：如果 z-score ≈ HT ≈ lz*，论文的 motivation 需要如何重构？

Q3. n=3 seeds 下 Cohen's d=1.8 的 bootstrap 95% CI 是多少？CI 是否跨越有意义的 threshold（如 d=0.8）？

Q4. Leaderboard audit 放弃原因？如果是 detection power 不足，这本身是重要 negative result。

Q5. Mistral/Gemma 仅 single clean seed 的 d 估计是否应从主文移至 appendix 并标注 "preliminary"？

Q6. 检测阈值（MMLU 10-15%）在实际 benchmark leakage 场景中（通常 3-5%）是否完全无效？

---

## Missing References

**Person-fit statistics：**
Karabatsos (2003); Van der Flier (1982); Drasgow, Levine & Williams (1985)

**Contamination detection：**
Oren et al. (2024) ICLR; Deng et al. (2024) NAACL; Magar & Schwartz (2022) ACL; Polo et al. (2024) ICML; Golchin & Surdeanu (2024)

**LLM evaluation / IRT-for-LLM：**
Burnham et al. (2024); Jacobs et al. (2024)

**Reference verification：** Wang et al. (2025) [Ref 8] 需确认可查证（arXiv ID）；如为未公开工作需标注 "personal communication"。

---

## External Review

外部审稿：未请求。

## Visual Layout Check

视觉审查：未启动（not_started）。

---

## Reviewer 共识记录（最终）

| # | 版本 | R1 | R2 | 共识 |
|---|------|----|----|------|
| 1 | Dream Best | 3.5 | 3.5 | ✅ |
| 2 | Dream Median | 3.0 | 3.0 | ✅ |
| 3 | Dream Worst | 2.5 | 2.5 | ✅ |
| 4 | Actual v1 | 2.5 | 2.5 | ✅ |
| 5 | Actual v2 | 2.5 | 2.5 | ✅ |
| 6 | Actual v3 | 2.5 | 2.5 | ✅ |

**六份审稿完全一致，无任何未解决分歧。**

R1/R2 共同建议：不投当前版本。将 degradation chain (4PL→HT→z-score) 作为核心叙事 reframe，修复统计问题（seeds ≥10 + CI），加 figures + baseline + references，下一 ARR cycle 投出，目标 3.0 (Findings)。