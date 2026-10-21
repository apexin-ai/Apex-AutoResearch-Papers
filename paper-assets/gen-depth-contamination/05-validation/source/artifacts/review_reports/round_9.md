---
round: 9
review_mode: continue
overall_score: 4.0 (Conference)
timestamp: 2026-05-19T13:27:40.579461+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 圆桌审稿报告 — Round 9

**论文**: Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary
**Venue**: EMNLP 2026 (ARR May 2026)
**Reviewer 编排**: 2 名 Reviewer（R1: 方法严谨性 + 实验有效性；R2: 新颖性 + 完整性 + 写作质量）
**轮次**: Round 9（继续审稿模式，基于 Round 8 修订的评估）
**交叉分享**: 1 轮，完全收敛

---

## Summary

本文定义并系统测量递归合成文本的 generational discrimination boundary K*（相邻代际可区分的最大深度）。使用 15 维统计特征和 OBD-LightGBM 分类器，在 9 个模型配置（5 架构族，1B-14B）、4 个源域（C4、arXiv、Wikipedia、Code）、4 种解码策略下测量 K*。核心发现：web text K*=2（8/9 配置），arXiv K*=3，Code K*=1-2，Wikipedia K*=1，呈现域依赖的有界饱和模式。LOFO cross-validation 验证 θ=0.60 的跨家族一致性（C4 89%, arXiv 100%）。Retrain-chain K*=7（两模型两架构族收敛）确认 prompt-chain 为保守上界。

---

## Strengths

**S1** [两位共识] K* discrimination boundary 是定义清晰的新概念，填补了 binary detection 与 model collapse 理论之间的空白。无 prior work 显式定义和测量 adjacent-generation discrimination boundary。

**S2** [两位共识] 实验覆盖面系统全面：9 配置 × 4 域 × 4 解码策略 × 多维 ablation。统计方法严谨度在 ACL/EMNLP papers 中属上乘（bootstrap CI with GroupKFold, permutation test, LOFO CV, Holm-Bonferroni, ANOVA, power analysis）。

**S3** [两位共识] 边界案例处理诚实透明：Mistral K*=1、Qwen-cont marginal、Wikipedia LOFO 失败、Pythia Code K*=1 均主动报告和讨论。

**S4** [两位共识] 4-domain ordering（arXiv(3) > C4(2) ≥ Code(1-2) ≥ Wikipedia(1)）在全 θ 范围和跨 5 个架构族保持不变。Mistral 跨 3 域 K*={1,2,3} 是 domain-governs-K* 的最强单模型证据。

**S5** [两位共识] LOFO cross-validation 为 θ=0.60 提供了有意义的独立验证。方法论设计（gap-midpoint + held-out prediction + failure mode analysis for Wikipedia）超越简单 sensitivity analysis，是可复用的 threshold validation 方法。

**S6** [两位共识] Retrain-chain K*=7 双架构族收敛（Qwen-1.5B + Pythia-1.4B，不同 LoRA 参数化、不同 decay profile），暗示 retrain-chain information loss 有某种 universal upper bound。

**S7** [两位共识] Claims 系统性降级（sole→primary, unqualified→tested, pipeline→consistency check, DPI proves→DPI motivates），建立了 "每个 claim 都有 explicit qualifier" 的文风，整体可信度高。

**S8** [两位共识] Code domain 作为第 4 域（4 家族 5 模型 + cross-scorer validation）将 domain coverage 从 natural language 扩展到 programming language，cross-modality confirmation 实质提升 contribution。

---

## Weaknesses

### Should-Fix（影响评分但不一票否决）

**SF-1** [两位共识, R10-N1 + R9-N1] **McNemar claim 证据链断裂**

Introduction L28 和 Discussion L19 声称 "McNemar p > 0.05" 证明 OBD 与 frontier LLMs beyond K* 无显著差异。但：
1. Appendix §B.9 的 McNemar 测试比较的是 OBD vs baseline classifiers（LogReg/SVC/RF）在 1v2 task 上——与 "beyond K*" 的 claim 是**不同的比较**
2. LLM zero-shot section (Table S3c) 无对应 McNemar test 表格
3. Table S3c per-depth recall 显示 LLMs 在 depths ≥ 2 **系统性优于** OBD（GPT-5.5: 23.3%, Claude: 25.0% vs OBD: 18.3%），与 "neither... improve" 措辞存在**数据方向性矛盾**
4. Citation chain 断裂：Introduction → Section 6 → Appendix 无法追溯到 LLM McNemar 数据

**建议**（两位共识）：(a) 补充 OBD vs LLM beyond-K* McNemar test 表格；(b) 根据实际结果调整 claim 措辞——若 McNemar 显著，改为 "all methods achieve near-chance multi-class accuracy beyond K* (OBD: 18.3%, GPT-5.5: 23.3%, Claude: 25.0% at depths ≥ 2; random baseline: 20%)"，强调所有方法的**绝对性能接近 chance**，而非方法间无差异。R1 倾向改措辞（选项 B），R2 建议补表格+改措辞（A+B）。

**SF-2** [两位共识, R8-W4] **Transfer matrix 仅覆盖 4/9 配置**

Table S1 仍仅含 4 个配置（Qwen-rw, Pythia, OLMo, Qwen-cont），均为 ≤1.5B 模型。"80-92% accuracy retention"（Introduction contribution (c)）缺少 7B-14B 模型数据。Introduction L30 已添加 "tested" 限定词，但 Abstract L42 仍使用无限定的 "among continuation-mode generators"。

**建议**：(a) 至少补充 LLaMA-8B transfer 数据（论文中 borderline 配置）；(b) Abstract 与 Introduction 统一添加 "tested" 限定词；(c) 或在 Limitations 显式说明 transfer 验证仅覆盖 ≤1.5B 模型。

### Minor

**M-1** [R2] 4 个 bib entries 有 OpenAlex mismatch（alemohammad: first_author, wu: year 2023→2025, mehta: first_author, levy: lévy→levy），不影响 correctness 但应修正。

**M-2** [R1] appendix_extended L512 "sole rewrite-mode model" 虽为合法事实描述，reader 可能与旧版 "sole dominant factor" 联想，可改为 "only"。

---

## Reviewer Consensus

以下判定两位 Reviewer 交叉分享后完全一致：
- R8-N1 θ post-hoc: **RESOLVED**（LOFO + permutation + stability 三重验证）
- R8-N2 prompt-chain: **RESOLVED**（四处限定 + retrain-chain 双模型收敛）
- R8-N3 "sole": **RESOLVED**（全文替换为 "primary"）
- R8-W1 DPI: **RESOLVED**（"motivates" 非 "proves"）
- R8-W2 Qwen 5/9: **RESOLVED**（family-level reporting）
- R8-W3 Filtering: **RESOLVED**（consistency check framing）
- R8-W4 Transfer: **STILL_OPEN**（4/9 configs, ≤1.5B only）
- R8-W5 Cross-scorer: **RESOLVED**（20/22 preservation + ANOVA）
- R8-W6 One-wash: **RESOLVED**（精确化表述）
- R8-W7 arXiv CI: **RESOLVED**
- R10-N1 McNemar: **STILL_OPEN**（证据链断裂 + 数据方向性矛盾）
- R10-N2 Code domain: **RESOLVED**（4 家族 5 模型完整整合）
- R8-M1 Eq.1: **RESOLVED**（CI_low 形式）
- R8-M2 References: **RESOLVED**（49 entries, 0 orphan）
- R8-M3 -ing phrases: **RESOLVED**
- R8-M4 Abstract/probe: **RESOLVED**
- Overall: **4.0 (Conference)** — 两位完全一致

**Issue resolution 统计**: 15/17 RESOLVED, 2 STILL_OPEN (均为 warning/should-fix level)

## Reviewer Divergence

**Soundness 子维度**：R1 交叉后下调至 3.5/5（McNemar 数据方向性矛盾比预期严重），R2 维持 4/5。综合 3.75/5。

**McNemar 修复方案**：R1 倾向仅改措辞（选项 B），R2 建议补表格+改措辞（A+B）。两位均同意这是 should-fix 而非 must-fix，不影响 overall 评分。

**Excitement**：交叉后一致于 3.5/5。R2 上调（3→3.5，承认 domain ordering 和 retrain gap 是 non-trivial contributions），R1 下调（3.5→3，接受 confirmatory measurement 论点）后各自回到 3.5/5。

---

## Questions

1. 补充 OBD vs frontier LLM beyond-K* McNemar test 后，p-value 方向是否与当前 claim 一致？Table S3c 数据暗示可能不一致。
2. LLaMA-8B（borderline K*=2）的 cross-model transfer retention 是否仍在 80-92% 范围内？

---

## Missing References

Round 8 指出的所有缺失引用（CORAL, LightGBM, Oren, DivEye）已补齐。verify_references 确认 49 entries, 0 orphan, 0 missing。4 个 minor bib mismatch 需修正（见 M-1）。

---

## External Review

外部审稿未请求（external_review.paperreview_ai.enabled 未启用）。

---

## Visual Layout Check

视觉审查未执行（PDF 编译文件未找到）。建议在最终提交前进行 PDF 排版检查。

---

## Overall Assessment

**评分：4.0 (Conference)**

**置信度：4/5**（两位 Reviewer 独立给出相同 Overall 评分，交叉分享后 15/17 issues 判定完全一致）

**与 Round 8 对比**：3.5 (Borderline Conference) → **4.0 (Conference)**

**升分理由**：
1. θ=0.60 post-hoc 问题（R8-N1, 上轮最大 blocker）通过 LOFO + permutation + stability 三重验证充分解决
2. "sole" → "primary" 全文修正，claims 系统性降级
3. Code domain 作为第 4 域（4 家族 5 模型 + cross-scorer）实质扩展 domain coverage 和 ordering claim
4. Retrain-chain K*=7 双架构族收敛，增强 prompt-chain/retrain-chain 对比的可信度
5. DPI 论证正确降格为 motivation
6. 写作质量显著提升：active voice、术语一致、引用完整（49 entries）

**剩余问题**：
- McNemar claim 证据链断裂（should-fix，补表+改措辞，预计数小时内可修复）
- Transfer matrix 覆盖不足（should-fix，contribution (c) 证据偏弱但已加限定词）
- 4 个 bib mismatch + 1 个 "sole" 残留（minor）

核心发现（K*=2, 4-domain ordering, retrain gap）的证据体系不受上述问题影响。论文达到 EMNLP 2026 Main conference 接收水准。

| 维度 | R1 | R2 | 综合 |
|------|-----|-----|------|
| Soundness | 3.5/5 | 4/5 | 3.75/5 |
| Excitement | 3.5/5 | 3.5/5 | 3.5/5 |
| Reproducibility | 4/5 | 4/5 | 4/5 |
| Clarity | 4/5 | — | 4/5 |
| Overall | 4.0 | 4.0 | **4.0 (Conference)** |

---

## Detailed Comments

### Should-Fix
1. **McNemar claim**：补充 OBD vs LLM beyond-K* McNemar test 表格（Appendix LLM zero-shot section）+ 根据实际结果调整 Introduction L28 和 Discussion L19 措辞（"near-chance accuracy" 替代 "no significant difference"）
2. **Transfer matrix**：(a) 补充 LLaMA-8B transfer row，或 (b) Abstract L42 添加 "tested" 限定词 + Limitations 说明 ≤1.5B 限制

### Minor
1. 4 个 bib entry author/year mismatch 修正（alemohammad, wu, mehta, levy）
2. appendix_extended L512 "sole" → "only"