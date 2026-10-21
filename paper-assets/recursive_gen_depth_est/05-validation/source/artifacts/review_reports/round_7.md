---
round: 7
overall_score: borderline accept
timestamp: 2026-05-17T09:03:02.625478+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: True
---

# Round 9 审稿报告 — 修订版论文圆桌共识汇总

**论文**: How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints
**Venue**: EMNLP 2026 Findings (ARR May 2026 cycle)
**Reviewers**: R1（方法严谨性+实验有效性）、R2（新颖性+写作完整性+引用覆盖）
**交叉回应**: 完成（高度共识，1 处实质分歧）
**注**: 本报告替代 Round 8 报告，基于修订版论文重新审稿。

---

## ⚠️ 重要：Director Paper Summary 与实际论文不一致

两位 Reviewer 独立验证确认：Director 提交论文时的描述包含当前 tex 文件中**不存在**的内容：
- **14B 实验** (Qwen2.5-14B, FP16, 76.2%): 论文最大模型为 8B
- **Prompted generation** (92.8% retention): 论文仅有 BOS-seeded
- **Two-stage pipeline** (§5.4, 75.2%): Limitations 提及概念但无实验
- **Wild-data on RedPajama-v2/Dolma**: 论文使用 WikiText-103 和 C4
- **论文标题**: 实际为 "How Deep Is Your Data?"，非 Director 描述的 "Ordinal Depth Estimation..."

**本报告基于实际 tex 文件内容。如果计划内容会在提交前纳入，需要重新审稿。**

---

## Summary

论文形式化了 recursive generation depth estimation 任务（ordinal classification），构建 180K 样本 3×3 atlas benchmark，发现 perplexity tail statistics 一致主导 depth discrimination，提出 EDD metric。修订版相比 Round 8 有实质改善：Related Work 补全（Schaeffer 2025, McCullagh 1980, CCNet）、LoRA rank ablation 新增、novelty positioning 修正（Dohmatob bridge statement）、Discussion curation 叙事诚实化、Abstract 精简并删除 §4.4 引用、em-dash 全文清除、"universal and scale-variant" 矛盾修正。

---

## Strengths

1. **任务新颖性**: Ordinal depth estimation 填补 binary detection → multi-depth 空白。EDD metric 有概念贡献。[R1 S1, R2 S1]
2. **系统性实验设计**: 3×3 atlas + 7 generalization axes + reverse-chain control + cross-seed replication + LoRA rank ablation（新增）。[R1 S2, R2 S2]
3. **Related Work 显著改善**: Schaeffer 2025（反驳 collapse 必然性）、McCullagh/Frank/Rennie（ordinal 经典）、CCNet 全部补齐。Dohmatob positioning 清晰。[R1 S3, R2 S6]
4. **特征可解释性三重验证**: Gini + permutation + SHAP, Kendall W=0.90。Top-5 features = 97.6% full accuracy。[R1 S4, R2 S5]
5. **诚实的 Limitations**: 8 段覆盖主要 caveats。Curation PoC 改为 "inconclusive"。[R1 S5, R2 S4]
6. **Surface-text ablation**: Zero-shot LLMs 30-36% vs RF 78.2%，42pp gap。[R2 S3]
7. **LoRA rank ablation 新增**: r=4,16,64 spread 4.65pp。[R1 S6]
8. **Reference model ablation 扩展**: 三个 reference architectures（但 Table 16 数据不完整）。[R1 S7]

---

## Weaknesses

### Must-Fix（Blocking）

**[W-MF1] Table 16 reference model 消融数据缺失** [共识: R2 N1 critical + R1 完全 AGREE]
- method.tex line 41, conclusion.tex line 39, Introduction contribution bullet 3 均声称 "three reference architectures" 和 "67-79%"。
- Table 16 仅有 2 行数据：Pythia-1.4B (78.6%) 和 OLMo-1B (74.5%)。**GPT-2 XL reference 结果完全缺失**。
- "67%" 的下界无法 verify。
- **修复**: 补入 GPT-2 XL 数据到 Table 16，或将所有 "three" 改为 "two" 并调整范围。

---

### Should-Fix（影响评分但不 blocking）

**[W-SF1] "signal universality" 遗漏修改** [共识]
- generalization.tex line 108 仍有 "signal universality"。Introduction 已修正但此处遗漏。
- **修复**: → "signal robustness across model boundaries"。

**[W-SF2] Table 2/5 仍缺 std/CI** [R1 moderate, R2 should-fix]
- 多轮 persistent issue。Cross-scale 有 CI，主表没有。
- **修复**: Table 2 加 ±std 或 caption 注明 fold-level std ≤0.8pp。

**[W-SF3] Abstract "70-85%" 取整** [共识]
- 实际 69.6%--85.4%。
- **修复**: "69.6--85.4%" 或 "approximately 70--85%"。

**[W-SF4] Contribution bullet 3 信息过载** [共识]
- **修复**: 拆为两条或只列 axis 名称。

**[W-SF5] 跨策略迁移实用性讨论不足** [共识, R1 认为更重要]
- d1-d3 仅 45.9%; strategy 未知时可能 inverted predictions。
- **修复**: Limitations 增加一段讨论 strategy-unknown 部署场景。

**[W-SF6] BOS-seeded 生态效度限制** [共识]
- 无 prompted generation 数据点。
- **修复**: （建议）小规模 pilot 或更充分 Limitations 讨论。

---

### Minor

- 2 个 orphan bib 条目（c2pa2024, chen2024spin）
- RAID benchmark (Dugan et al., ACL 2024) 未引用
- C4 FPR ground truth 假设应注明 crawl year
- EDD 仍未显式声明为 operational measure
- Abstract 括号内列举不完整

---

## Reviewer Consensus

完全一致：Table 16 数据缺失（唯一 blocking）、"signal universality" 遗漏、Abstract 取整、Contribution 过载、跨策略讨论不足、BOS 限制、orphan bibs、RAID 未引。

## Reviewer Divergence

| 问题 | R1 | R2 | Director 裁定 |
|------|-----|-----|--------------|
| Cross-scale "marginally above chance" | moderate | partial REBUT (2.32× chance) | R2 更准确 |
| Depth vs quality confound | moderate | partial REBUT (间接证据充分) | 不 blocking; 间接证据可接受 |
| Accumulation scenario | moderate | future work acceptable | 不 blocking; Limitations 已 acknowledge |

---

## Questions for Authors

1. Table 16 中 GPT-2 XL reference 实验是否完成？为什么未列入？
2. LoRA rank ablation per-rank accuracy 和 feature importance？rank 对 EDD 影响？
3. Curation PoC 不显著——depth estimation 的主要应用场景？
4. Qwen2.5-7B U-shaped AUC recovery 原因？base Qwen trajectory？
5. Director summary 中 14B/prompted/two-stage/RedPajama 是否计划纳入？

---

## Missing References

- RAID (Dugan et al., ACL 2024)
- 2 orphan bibs 需清理

---

## External Review

未配置。

---

## Overall Assessment

**Overall Score**: 3.5 / 5（Borderline Accept for Findings，conditional on W-MF1 修复）

**评分理由**:
- (+) 修订版解决了 Round 8 大部分问题
- (+) 任务新颖，实验系统，Limitations 诚实
- (+) Feature importance 三重验证，方法学严谨
- (-) Table 16 claim-evidence 矛盾（blocking but trivial fix）
- (-) 几处遗漏文本修改（trivial）
- (-) BOS-only, accumulation 未验证（合理 scope limitation）
- (-) Cross-strategy 45.9% 限制实际部署价值

**Confidence**: 4/5

**建议**:
- W-MF1 必须立即修复（补数据或改文字）
- W-SF1/SF3/SF4 是 trivial 文本替换
- W-SF2 rebuttal 承诺即可
- 如果 Director 描述的 14B/prompted/two-stage 纳入，Overall 可升至 4.0
- 当前版本 solid for Findings track

---

## 相比 Round 8 的进展

| 类别 | Round 8 | Round 9 |
|------|---------|---------|
| Related Work 遗漏 | ❌ 4 篇未引 | ✅ 全部补齐 |
| Novelty positioning | ⚠️ 增量不清 | ✅ Dohmatob bridge 准确 |
| Abstract 过载 | ⚠️ 20+ 数字 | ✅ 精简 |
| LoRA rank ablation | ❌ 未做 | ✅ 新增 |
| Curation narrative | ❌ "enables" | ✅ "inconclusive" |
| "universal" overclaim | ❌ 3 处 | ⚠️ 2/3 修复 |
| Em-dash | ❌ 6+ 处 | ✅ 清除 |
| Table CI | ⚠️ 缺 | ⚠️ 仍缺 |
| Ref model ablation | ⚠️ 1 个 | ⚠️ 3 个但 Table 不完整 |