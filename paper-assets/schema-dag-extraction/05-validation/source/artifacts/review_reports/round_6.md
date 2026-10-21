---
round: 6
overall_score: weak reject
timestamp: 2026-05-16T14:04:47.520178+00:00
reviewer_ids: [1, 2, 3]
cross_response_reviewer_ids: [1, 2, 3]
force_resubmit: False
---

# 审稿报告 — Round 6

**论文**: "Does Type Confusability Shape Schema-Induced Degradation in Training-Free LLM Information Extraction?"
**目标 Venue**: ACL ARR May 2025 — Main Conference Long Paper
**审稿人**: Reviewer 1（方法论+统计）、Reviewer 2（新颖性+逻辑）、Reviewer 3（格式+可复现性）
**审稿模式**: Fresh review（独立于历史轮次）

---

## Summary

本文研究 training-free LLM IE 中 schema 复杂度导致的性能下降，提出 Schema Confusability Score (SCS) 和 Batch Confusability Score (BCS) 量化 type 间语义相似度，通过 count curves 和 BCS-controlled 两种实验范式在 Few-NERD (NER)、FewRel (RE)、DocRED (doc-level RE)、MAVEN (ED) 四个数据集上进行 controlled study。主要发现：(1) type count 和 type confusability 构成两个可区分的降级维度——count 驱动 recall 下降，confusability 驱动 type substitution；(2) pairwise SCS 与 type confusion 显著相关（r=0.112–0.129），batch-level BCS 解释 22–53% 准确率方差；(3) 同域 schema (MAVEN) 存在 centrality confound；(4) schema 分解对 NER 因 merge amplification 而失败，对 RE 在 oracle routing 下仅产生不显著的 +1.4pp 改善。

---

## Strengths

**S1. 精良的 controlled experimental design**（三人共识）
BCS-controlled 范式在 zero-shot IE 文献中属首次。Within-pool analysis 控制 pool composition confound，permutation test 确认 slope 跨条件一致性。实验逻辑链完整。

**S2. 统计报告的高透明度**（三人共识）
非显著结果（factorial p=0.50, SDGD +1.4pp p≈0.19, within-pool quartile CI 过零）、modest effect sizes（r²=1.3–1.7%）均如实报告。

**S3. Centrality confound 分析**（三人共识）
识别 MAVEN 上 per-type BCS 正相关为 spurious signal，partial correlation 控制后信号消失。对社区有方法论示范价值。

**S4. 负结果的诊断价值**（三人共识）
SDGD 的 merge amplification 机制诊断（precision 0.563→0.210）对 schema decomposition 研究者有警示价值。

**S5. Cross-task/cross-model replication**
Channel 1 在 Llama-3.1-8B 完全复现，Channel 2 在 RE 上跨模型复现。DocRED 扩展到 document-level（R²=0.53）。Prompt sensitivity analysis (v1/v2) 少见但重要。

---

## Weaknesses

### Must-Fix（影响接收决定）

**W1 [Critical — 三人共识] "Empirically separable channels" 缺乏 formal 统计支撑**

唯一的 formal separability 检验——Few-NERD 2×2 factorial interaction——不显著（z=−0.67, p=0.50）。FewRel 上未做 factorial test。实际 separability 证据来自 error taxonomy 的定性分离（IntraSub ρ=0.954 随 BCS 单调；missed rate 与 BCS 无关），但此论证基础在正文中不够清晰。R2 指出这与 two-channel model 概念深度不足叠加——统计上无法证明分离性则 "model" 仅是未被证伪的 hypothesis。

→ 建议：'empirically separable' → 'mechanistically distinguishable'；或补做 FewRel factorial / TOST equivalence test。

**W2 [Critical — 三人共识] Abstract/Intro 以 extreme-batch gap (31.2pp) 为 headline，typical effect (2.2pp) 被弱化**

全文 31.2pp 出现 ≥8 次，2.2pp 仅 3 次。31.2pp 来自人工极化的 extreme batches（methodological upper-bound），typical random batch 差异仅 2.2pp（CI: [0.4, 4.0]），quartile gap 3.9–5.3pp。§5.3 做了诚实披露但高曝光位置未反映。

→ 建议：Abstract/Intro/Conclusion 以 typical gap 为主锚；31.2pp 标注为 methodological upper-bound 仅在实验细节中报告。

**W3 [Critical — R2 主导，R1/R3 同意] Two-channel model 概念 novelty 不足**

"Count → recall decline" 已是社区共识；"Similar types → confusion" 被 LLM-PEE 隐式 operationalize。论文贡献在于 controlled evidence 而非概念框架。Contribution 1 的 "Two-channel degradation model" 措辞暗示 theoretical contribution。

→ 建议：Contribution 1 改为 "Controlled empirical evidence for two distinguishable degradation dimensions"。

**W4 [Critical — R3 主导，R1/R2 同意] 正文可能超 8 页限制**

从内容量估算正文约 8.5–9 页，超出 ACL ARR ≤8 页限制。格式违规可导致 desk reject。

→ 建议：编译验证；§6 detailed protocol 移入 Appendix 释放空间。

### Should-Fix（影响评分）

**W5 [Major] "首次 controlled study" 声称需限定** — LLM-PEE/Haystack-to-Needle 已部分覆盖。建议改为 "the first to formally isolate confusability from count via stratified design in zero-shot LLM IE"。

**W6 [Major — 三人共识] Oracle routing 限制 RQ3** — 所有 RE positive evidence 依赖 oracle routing；full 80-rel p=0.76 不显著。RQ3 实际答案为 negative result。建议重措辞。

**W7 [Major] Few-NERD 采样策略未说明** — 66 types 长尾分布，非分层采样影响 pairwise analysis 代表性。

**W8 [Major] Count curves 5 batches/level + 种子未报告** — 影响可复现性和 count-curve 稳定性评估。

**W9 [Major] Pairwise SCS 解释力极低 (r²=1.3–1.7%)** — Typical-batch 2.2pp 可能 within noise（prompt variation 5.7pp 更大）。未讨论 pre-hoc alternatives（如 perplexity-based similarity）。

**W10 [Minor-to-Major] 多重比较未校正** — 边界显著结果可能受影响；核心 p<0.001 结论稳健。

**W11 [Minor-to-Major] Cross-model 仅 2 模型** — R2 反驳分析性研究标准可降低；Channel 2 在 8B NER 未复现。

### Minor

- Channel 1/2 标签应在 Introduction 首次定义
- "Training-free" vs "Zero-shot" 需声明等价
- NER text-match metric 补充 partial overlap 处理
- SDGD 脚注 "internal project designation" 有匿名性风险
- Checklist B1 补 DocRED + Llama \cite
- Bootstrap B=1000 vs B=10000 需说明为 deliberate choice

---

## Reviewer Consensus [AGREE]

| 问题 | R1 | R2 | R3 | 状态 |
|------|----|----|-----|------|
| Framing 失衡 (31.2pp vs 2.2pp) | N2 | N1 | AGREE | **共识** |
| Factorial / "separable" 证据不足 | N1 | AGREE | AGREE | **共识** |
| Two-channel "model" overclaim | AGREE | N3 | AGREE | **共识** |
| Oracle routing 限制 RQ3 | W3 | W3 | AGREE | **共识** |
| 页数超限 | AGREE | AGREE | N1 | **共识** |
| Few-NERD sampling | AGREE | AGREE | N2 | **共识** |

## Reviewer Divergence [REBUT]

| 问题 | 分歧 | 结论 |
|------|------|------|
| Cross-model 覆盖 (R1-W2) | R2: 分析性研究 2 models 足够 | 降级 should-fix |
| Count curves 5 batches (R1-W4) | R2: trend 够用 | R3 强同意 R1，保持 should-fix |
| 多重比较 (R1-W5) | R3: 跨数据集是 replication | 核心不受影响，secondary 需 acknowledge |
| Bootstrap B 不一致 (R3-W3) | R1: 方法论合理 | 需说明是 deliberate choice |
| NER metric (R3-W5) | R2: comparative study 内恒定 | 降为 minor |
| SCS proxy validity (R1-W1) | R3: batch R²=22% 有用 | 保持 should-fix |

---

## Questions to Authors

1. **Typical-batch gap 的工程意义**：2.2pp (CI: [0.4, 4.0]) vs prompt variation 5.7pp——何种场景下 SCS-based schema design 值得投入？
2. **为什么不做 FewRel factorial test？** FewRel balanced design 更适合 2×2 crossing。
3. **Embedding 选择**：Few-NERD 用 Qwen3 而其余用 MiniLM——对 SCS 作为 model-agnostic proxy 的定位有何影响？
4. **FewRel contamination**：train-origin vs val-origin accuracy 差异？p=0.06 单侧近显著。
5. **Merge amplification vs decomposition**：union-merge 的问题是否等于 decomposition 的问题？Learned merge 是否可能恢复？

## Missing References

1. "From Haystack to Needle: Label Space Reduction for Zero-shot Classification" (2025)
2. Label confusion / noisy label learning 方向经典工作
3. Many-shot ICL (NeurIPS 2024) — label set scaling degradation
4. LLM calibration 对 multi-pass 融合的理论基础

## External Review (Stanford Agentic Reviewer)

项目配置 `external_review.paperreview_ai.enabled: false`。未请求外部审稿。

---

## Overall Assessment

**评分**: **Weak Reject** (Main Conference) / **Weak Accept** (Findings track)

**综合评分**: 3.0–3.2 / 5
- R1: 3.0 / 5 (Soundness 3, Excitement 3)
- R2: 3.0 / 5 (Soundness 3.5, Excitement 2.5)
- R3: 3.5 / 5 (Soundness 3.5, Excitement 3)

**置信度**: 4/5

**理由**：

论文在 zero-shot IE schema degradation 领域做了一项 well-designed 的分析性研究。实验设计严谨、统计报告透明、centrality confound 和 merge amplification 分析有价值。

三个 structural 问题限制 main conference 竞争力：
1. **Framing-evidence mismatch**：typical effect 仅 2.2pp 但以 31.2pp 为 headline；"separable channels" 缺 formal 统计支撑（factorial p=0.50）；"two-channel model" 包装 near-trivial 分解。
2. **Practical impact 有限**：SCS pairwise r²=1.3–1.7%；decomposition 为 negative result；typical-batch effect 可能 within engineering noise。
3. **方法论缺口**：页数可能超限；采样和种子信息不全；多重比较未讨论。

**修订建议**：(1) framing 校准至 typical magnitude；(2) "two-channel model" → "controlled empirical evidence"；(3) 补 factorial test 或弱化 separability claim；(4) 修复页数和 sampling。修订后适合 **Findings track** 发表。Main conference 需更强 novelty 或更大 practical effect size。