---
round: 3
overall_score: 3.5 - Borderline Conference
timestamp: 2026-05-18T02:32:58.633964+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告 — Round 5 圆桌审稿（EMNLP 2026 Main）

**论文**: "Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary"
**Venue**: EMNLP 2026 Main Conference (ARR May 2026 cycle)
**截止日期**: 2026-05-25
**审稿日期**: 2026-05-18
**Reviewer 编排**: 2 人（R1 方法严谨性 + 实验统计, R2 新颖性 + 完整性 + Framing）
**外部审稿**: 未启用

---

## Summary

本文定义并测量了递归合成文本的世代深度判别边界 K*。使用 15 维统计特征 + OBD-LightGBM 分类器，在 θ=0.60 阈值下，跨 8 种模型配置（1B-8B, 5 architecture families）、3 个域（C4, arXiv, Wikipedia）、4 种解码策略，发现 K* 由域结构决定：arXiv K*=3, C4 K*=2, Wikipedia K*=1。论文通过 cross-model transfer (80-92%)、cross-scorer validation、neural probe、frontier LLM zero-shot 对比和 6 策略下游过滤实验构建多维证据网络。

**Round 5 核心变化**: Round 4 提出的全部 8 个 critical/major issues 均已充分修复，论文方法论和叙事质量显著提升。但修改过程引入了新的完成度问题——主文引用的 ANOVA 表格和 LLaMA-8B bootstrap CI 为空占位符。

---

## Strengths

**S1. 问题定义新颖且经过验证。** 经广泛文献搜索确认无 prior work 直接估计递归生成深度。"首次系统测量 K*_empirical" 的 novelty claim 成立。[R1-S1, R2-S1 一致]

**S2. 实验覆盖面强。** 8 model configs × 5 architecture families × 3 domains × 4 decoding strategies。Cross-scorer validation、neural probe、frontier LLM zero-shot 从不同角度交叉验证。Triangulation 设计远超一般 empirical paper。[R1-S2, R2-S2 一致]

**S3. Round 4 issues 全部充分解决。** 8 个遗留 critical/major issues 逐一得到实质性回应：self_BLEU leakage 的三层回应（CV 隔离 + 14D ablation + 部署方案）、θ 三重 justification (Cohen's h + permutation test + discontinuity)、cross-scorer K*=1 坦诚披露、structural confound 分析。非表面修补。[R1-S1, R2 一致]

**S4. Domain ordering 发现高度 compelling。** arXiv (K*=3) > C4 (K*=2) > Wikipedia (K*=1) 跨 6 个模型、4 个 architecture families 一致。Mistral 的 cross-domain profile (C4: K*=1, arXiv: K*=3) 证明域结构而非模型身份决定 K*。[R1-S3]

**S5. 下游验证有 practical value。** 6 种过滤策略对比验证 K*=2 的 actionability。Graduated filtering 随 α 增大单调收敛到 binary 的实验将理论测量转化为可证伪预测。Binary filtering 在所有 contamination ratio 下保持优势 (HellaSwag p ≤ 0.004)。[R1-S4, R2-S5 一致]

**S6. 叙事主线统一。** Abstract → Introduction → Method → Experiments → Discussion → Conclusion 形成连贯 story。Round 4 的 framing 问题（"data property" overclaiming, "invariant" 表述）已全面修正。[R1-S6, R2 Framing Check 一致]

**S7. Limitations 异常诚实。** 7 个具体限制条件 + Extended Limitations，包括 cross-scorer K*=1 的主动披露和 512-token 边界弱化。[R1-S5, R2-S4 一致]

---

## Weaknesses

### Must-Fix（Critical / Major，两位 Reviewer 交叉确认一致）

**W1 [Critical — 共识]. ANOVA 表格 (tab:anova_crossscorer) 数据全空但被主文引用。**
- 位置: appendix_extended.tex line 22-39; 主文 experiments_c1.tex line 81
- 主文声称 "A three-way ANOVA (Generator × Scorer × Depth-Pair; N=400; Table tab:anova_crossscorer) formally tests this independence"，但该表所有 F/p/η² 单元格均为 "---" 占位符。
- 审稿人无法验证 scorer independence claim 的统计基础。"formally tests" 一词暗示分析已完成但读者无法核实。
- **建议**: 填入实际 ANOVA 结果（F值、p值、η²_p），或删除主文 ANOVA 引用改用已有的 cross-scorer feature ranking ρ>0.90 作为 independence 证据。
- **来源**: R1-N1 Critical + R2-N1 Critical（独立发现，交叉一致）

**W2 [Major — 共识]. LLaMA-8B 主文 claim K*=2 但写着 "pending bootstrap CI"。**
- 位置: experiments_c1.tex line 44; Table tab:kstar_ci_extended LLaMA-8B 列全为 "---"
- 主文声称 "LLaMA-3.1-8B yields K*=2 (0v1 AUC = 0.9225, 1v2 AUC = 0.6123; borderline: 1/5 folds falls below θ, pending bootstrap CI)"。
- "pending bootstrap CI" 不应出现在投稿论文中，意味着统计验证未完成。
- LLaMA-8B 是两个 7B+ 模型之一，"K*=2 persists from 1.5B through 8B" 的 scale invariance claim 依赖此数据点。"1/5 folds falls below θ" 信号已表明 borderline 状态。
- 若补充 CI 后 lower bound < θ，"7/8 configurations yield K*=2" 需调整为 "6/8" 并重新评估 scale invariance 措辞。
- **建议**: 补充 bootstrap CI；根据 CI 结果决定是否调整 headline claim。
- **来源**: R1-N2 Major; R2 初评 Warning 后交叉升级为 Major

### Should-Fix（Minor，有共识）

**W3 [Minor — 共识]. Introduction "fail comparably" 基于非显著性检验做等价性断言。**
- 位置: Introduction line 20
- "Both supervised OBD and zero-shot frontier LLMs fail comparably beyond K* (McNemar p > 0.05)" — 非显著性 ≠ 等价性，N=500 检验力有限。
- **建议**: 改为 "show no statistically significant difference (McNemar p > 0.05, N=500)"。
- **来源**: R2-N3 Minor → R1 [AGREE]

**W4 [Minor — 共识]. Abstract "80-92% cross-model transfer" 缺 continuation-mode 限定。**
- 位置: Abstract (main.tex line 38)
- Rewrite→continuation 仅 61-63%。80-92% 仅针对 continuation-mode pairs。
- **建议**: 加 "among continuation-mode generators"。
- **来源**: R2 (FR4-5 partial fix) → R1 交叉 [AGREE，承认自己遗漏]

### Nice-to-Fix（Warning / Minor）

**W5 [Warning — 共识]. Appendix 多个表格为空占位符。**
- Table S10 (Pythia decoding), S12 (Domain ablation), S13 (Scorer sensitivity) 全空；S11 (Length ablation) AUC 行空。
- S10/S12/S13 无 \ref 引用（dead tables）。"experiment pending" 字样不应出现在投稿材料中。
- **建议**: 填入数据或删除空表格。
- **来源**: R1-N3 Warning + R2-N2 Warning（独立发现，一致）

**W6 [Minor — 共识]. "51 total runs" 计数来源不明。**
- 位置: experiments_c3.tex line 6
- 5 strategies × 5 seeds = 25; 5 α values × 5 seeds = 25; total = 50（非 51）。
- **建议**: 核实并添加计数分解说明。
- **来源**: R2-N4 Minor → R1 [AGREE]

**W7 [Minor]. Table tab:domain_model_kstar_full Wikipedia 列 boundary AUC 全缺。**
- 数据存在于 Table wiki_domain (appendix_extended.tex)，属格式遗漏。
- **来源**: R1-N4 Minor → R2 [AGREE]

---

## Reviewer Consensus（交叉确认一致）

| 问题 | R1 | R2 | 交叉结果 |
|------|-----|-----|----------|
| ANOVA 空表 (Critical) | N1 独立发现 | N1 独立发现 | **双方 AGREE** |
| LLaMA-8B pending CI (Major) | N2 独立标记 Major | 初评 Warning → 升级 Major | **双方 AGREE (severity aligned)** |
| Round 4 全部 8 issues 已修复 | 逐条确认 | 逐条确认 | **双方 AGREE** |
| "fail comparably" 逻辑 (Minor) | 交叉 AGREE | N3 独立发现 | **双方 AGREE** |
| Abstract 80-92% 缺限定 (Minor) | 交叉 AGREE（自认遗漏） | FR4-5 partial fix | **双方 AGREE** |
| 空 appendix 表格 (Warning) | N3 独立发现 | N2 独立发现 | **双方 AGREE** |
| "51 runs" 计数 (Minor) | 交叉 AGREE | N4 独立发现 | **双方 AGREE** |

## Reviewer Divergence

| 问题 | R1 | R2 | 备注 |
|------|-----|-----|------|
| Excitement | 3.5/5 | 4.0/5 | R1 认为 K*∈{1,2,3} low dynamic range 限制 excitement；R2 认为 first-of-its-kind framing 值得更高分。**Director 判定**: 合理主观分歧，取中值 3.75 |

---

## Questions（需作者澄清）

**Q1.** ANOVA (tab:anova_crossscorer) 分析是否已实际完成？若已完成请填入数据；若未完成请删除主文引用并改用 feature ranking ρ>0.90 支撑 scorer independence claim。

**Q2.** LLaMA-8B bootstrap CI 何时可计算完成？若 CI lower bound < θ=0.60，scale invariance claim 需要如何调整？

**Q3.** "51 total runs" 的精确分解是什么？

---

## Missing References

Round 4 要求的全部 6 篇已补入（R2 通过 OpenAlex + arXiv 验证）：Dohmatob 2025, SemEval-2024 Task 8, Gerstgrasser 2024, Guo 2024, Briesch 2023, Padmakumar & He 2024。当前 31 references 覆盖充分。**本轮无新增遗漏引用。**

引用真实性: R2 抽查确认全部通过。

---

## External Review (Stanford Agentic Reviewer)

外部审稿：未启用（项目配置 `external_review.paperreview_ai.enabled = false`）

---

## Overall Assessment

**评分: 3.5/5 (Borderline Conference)**
**EMNLP 2026 ARR 评分: 3.5 (Borderline Conference)**
**置信度: 4/5**

| 维度 | R1 | R2 | 综合 |
|------|-----|-----|------|
| Soundness | 3.5 | 3.5 | **3.5** — 核心方法论 sound; θ justification, CV design, cross-scorer validation 均达标。ANOVA 空表 (W1) 和 LLaMA-8B pending CI (W2) 是可修复的 soundness gap |
| Excitement | 3.5 | 4.0 | **3.75** — 首个 generational depth estimation 框架, domain ordering 有 insight, one-wash effect actionable。K*∈{1,2,3} low dynamic range 略限制实用广度 |
| Reproducibility | 3.0 | 3.0 | **3.0** — 方法描述充分，但空 appendix 表格和 pending CI 损害完成度印象。Code release upon acceptance |
| Overall | 3.5 | 3.5 | **3.5** — Borderline Conference |

### 核心判断

**Round 5 的论文在科学贡献和叙事质量上已达到 EMNLP Main Conference 水平。** Round 4 的全部 critical/major issues（self_BLEU leakage、θ "invariant" overclaiming、cross-scorer K*=1、structural confound、text length ablation 等）均已通过实质性修改解决，非表面修补。叙事主线（问题定义 → 方法 → 发现 → 验证 → 机制解释）连贯统一。

**当前唯一阻碍升至 4.0 的因素是完成度问题：**
1. ANOVA 空表被主文 "formally tests" 引用 — soundness 硬伤
2. LLaMA-8B "pending bootstrap CI" — scale invariance argument 的关键证据缺统计确认

这两个问题均为**数据填入工作**（非实验重做、非方法论变更），预计可在 deadline (2026-05-25) 前完成。

### 升分路径（3.5 → 4.0）

| 优先级 | 修改项 | 工作量 |
|--------|--------|--------|
| **Must** | W1: 填入 ANOVA F/p/η² 或删除主文引用 | 数据填入 |
| **Must** | W2: 补 LLaMA-8B bootstrap CI + 根据结果调整 claim | 计算 + 措辞调整 |
| **Should** | W3: "fail comparably" → "no significant difference" | 措辞修改 |
| **Should** | W4: Abstract 80-92% 加 continuation-mode 限定 | 措辞修改 |
| **Nice** | W5: 删除空 appendix 表格 | 删除 |
| **Nice** | W6: 修正 "51 runs" 计数 | 核实 |
| **Nice** | W7: 补 Wikipedia AUC | 数据复制 |

**Must-Fix 完成后评分可升至 4.0 (Conference Accept)。**

---

## Detailed Comments（按论文节次）

### Abstract
- "80-92% cross-model transfer" → 加 "among continuation-mode generators"（W4）
- 其余修改已到位（"dominant mode (7/8)"、"converging evidence"）

### Section 1 (Introduction)
- Line 20: "fail comparably" → "show no statistically significant difference (McNemar p > 0.05, N=500)"（W3）
- CoDeC 归类修正已到位
- Prompt-chain vs retrain-chain 区分已到位

### Section 3 (Method)
- self_BLEU CV 隔离流程说明已到位
- θ 三重 justification 已到位
- OBD 缩写无新问题

### Section 4 (Experiments)
- Section 4.2 line 81: ANOVA 引用需要数据支撑或删除（W1, Critical）
- Section 4.1 line 44: LLaMA-8B "pending bootstrap CI" 必须填入（W2, Major）
- "8 model configurations + 4 decoding strategies" 分离表述已到位
- Cross-scorer validation 坦诚披露已到位
- Neural probe reconciliation 已到位

### Section 5 (Filtering)
- experiments_c3.tex line 6: "51 total runs" 核实计数（W6）
- 统计处理（Holm-Bonferroni）无新问题
- 100% synthetic upper-bound caveat 已到位

### Section 6 (Discussion)
- "Converging evidence" 替代 "confirms" 已到位
- "Representation dependence" reconciliation 已到位
- "Scorer sensitivity" 段落清晰合理

### Conclusion
- 限定词已到位

### Limitations
- 7 条详尽，包括 cross-scorer K*=1 和 512-token 边界弱化
- N=500 McNemar power limitation 可考虑补充（与 W3 相关）

### Appendix
- ANOVA 表填入数据（W1）
- S10/S12/S13 空表删除或填入（W5）
- S11 AUC 行补入（W5）
- LLaMA-8B extended table 补入（W2）
- Wikipedia AUC 补入 full table（W7）

---

## Round 4 → Round 5 Issue Resolution Summary

| Round 4 Issue | Severity | Round 5 Status |
|---------------|----------|----------------|
| FR-3: self_BLEU leakage | Critical | ✅ Resolved |
| FR-1: θ=0.60 "invariant" | Critical | ✅ Resolved |
| W2: Cross-scorer K*→1 | Critical | ✅ Resolved |
| FR4-1: Table S2 bootstrap CI | Major | ✅ Resolved |
| FR4-2: Structural confound | Major | ✅ Resolved |
| FR4-3: Text length ablation | Major | ✅ Resolved |
| FR-6: "9 conditions" | Warning | ✅ Resolved |
| FR4-7: "mode > model" | Minor | ✅ Resolved |

**8/8 resolved** — 这是 5 轮审稿中首次所有遗留问题全部清零。