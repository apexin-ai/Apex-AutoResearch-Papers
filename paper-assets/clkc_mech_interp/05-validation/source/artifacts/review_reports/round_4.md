---
round: 4
review_mode: fresh
overall_score: 3.0 - Findings
timestamp: 2026-05-25T21:33:12.670498+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# Round 4 审稿报告 — clkc_mech_interp

**Target Venue**: EMNLP 2026 (via ARR) | **Deadline**: 2026-06-15
**Paper**: "English-Chinese Knowledge Conflict Signals Are Consistent With General Cross-Lingual Asymmetries"
**Reviewers**: R1 (方法严谨性) + R2 (新颖性/完整性) | **Cross-sharing**: 完成

---

## Summary

本文将知识冲突信号的 probing 分析从单语扩展到英-中跨语言设置，在三个 LLM（Llama-3.1-8B-Instruct、Qwen3-8B、Gemma-2-9B-IT）上训练残差流探针、构建 XNLI 非冲突基线、执行 COMET/token overlap/EN-DE 混淆排除、并进行因果 steering 实验。主要发现：(1) 冲突信号在所有模型和方向上线性可检测；(2) ZH→EN ~7pp 迁移优势与 XNLI 一致，反映一般跨语言结构；(3) 仅 Llama L13 (41% depth) steering 成功，Qwen/Gemma 无效，据此提出 detection≠decision dissociation。

---

## Strengths

1. **混淆因素控制设计出色**：COMET 翻译质量分层 + XNLI 非冲突基线 + EN-DE 类型学控制的三层设计是可复用的方法论贡献。EN-DE Jaccard 14.8% vs EN-ZH 3.8% 但 Δ≈0 有效排除 token overlap。[R1-S2/S3, R2-S1]
2. **多模型验证**：三个架构差异显著的模型仅 3.5% 问题重叠，构成近似独立复制。方向一致性 binomial p = 0.016。[R1-S1, R2-S2]
3. **统计方法规范**：Bootstrap CI (n=2000)、Bonferroni 校正、Fisher 精确检验、selectivity control (gap 21-40pp)、matched-condition 控制均达标。[R1-S4/S5, R2-S3]
4. **诚实报告负面结果**：Qwen/Gemma steering 失败、asymmetry 非冲突特异性的如实报告优于领域平均水平。[R2-S4]
5. **Seed replication**：独立 seed 复现 Llama L13 因果效应 (N=201)，排除单次 split 偶然性。[R2-S5]
6. **代码可用 + AI 使用声明透明**：匿名代码仓库提供，AI 辅助使用明确标注。

---

## Weaknesses

### Critical（影响接收决定）

**[C1] Detection ≠ Decision 核心 claim 过度概括（R1-W1, R2-N1; 双方 AGREE）**
- 正面因果证据仅来自 Llama L13 一层。Qwen (L14) 和 Gemma (L17) 各仅测 1 层即宣告 null，但 Llama 自身因果窗口仅 ~4 层 (L13-L16)，遗漏相邻层完全可能。
- 替代解释未排除：非线性因果通路、不同因果窗口位置、样本量功效不足 (n=131/171)、线性 steering 方法本身的局限性。
- Basu et al. (2026) "Interpretability without actionability" 已在单语中建立 detection-steering dissociation。本文差异化论述仅 Section 5 一句话，过于单薄。
- **Action required**: (1) Qwen/Gemma 补充至少 3 层相邻层 steering；(2) 若无法执行，将 claim 严格限定为 Llama-specific observation；(3) 增加与 Basu et al. 的逐点差异化段落。

**[C2] Asymmetry "consistent across all three models" 统计不充分（R1-W2; R2 交叉 AGREE）**
- Qwen Δ_asym = +7.2pp, CI [-0.6, 13.7] 跨越零，α=0.05 下不显著。
- 三模型 Bonferroni 校正（阈值 0.017）：Llama p=0.038 不显著、Gemma p=0.006 显著、Qwen n.s.——仅 1/3 模型通过校正。
- Section 4.3 "consistent in direction across all three architectures" 措辞超越了证据能支撑的范围。
- **Action required**: (1) 明确报告 Qwen 不显著；(2) 报告 Bonferroni 校正后结果；(3) 主要论据改为方向一致性 binomial test (p=0.016) + XNLI 六点复制。

**[C3] COMET tercile 混淆排除欠功效，Gemma 趋势未解释（R1-W3; R2 部分 AGREE）**
- MDE = 25.3pp at 80% power，对中等效应完全不敏感。
- Gemma Δ = +10.3pp 在混淆方向，p=0.278 在低功效下不排除实质效应。
- 多层控制（XNLI + EN-DE）部分缓解，但 COMET 分析作为独立证据线本质无效。
- **Action required**: 增加连续回归 (COMET score vs probe accuracy) 替代 tercile；对 Gemma 趋势深入调查。

### Warning（影响评分）

**[W1] 单一 train/test split 贯穿全文（R1-W5, R2-W2; 双方 AGREE）**
- Bootstrap CI 仅捕获 split 内变异。Δ_asym arithmetic diff (11.0pp) vs bootstrap mean (7.3pp) 差距 3.7pp 暗示 peak layer 不稳定。
- **Action**: 当前版本完成至少 3-fold CV 主要结果。

**[W2] TOST 等价检验功效 1.4%，uninformative（R1-W4; R2 AGREE）**
- ±2pp 边界对 n~200、SE~5-8pp 注定失败。报告无信息量检验有空洞分析之嫌。
- **Action**: 删除 TOST 或用合理边界 (±5pp) 重做。

**[W3] Steering 仅英文数据，未测试跨语言因果干预（R1-W8; R2 AGREE）**
- 论文主题是跨语言冲突，但因果实验仅用英文侧。缺少 ZH 输入 steering 和 cross-lingual steering。
- **Action**: 至少在 Llama L13 测试中文输入 steering。

**[W4] 全文多重假设检验缺乏整体 FWER 控制（R1-W7; R2 部分 AGREE）**
- ~100+ 检验仅 steering per-layer Bonferroni。Asymmetry 三模型属同一族未校正。
- **Action**: 对 asymmetry 做 Bonferroni/Holm 校正并报告。

**[W5] Qwen3-8B 同时作为翻译模型和实验对象（R1-W6; 分歧）**
- R2 反驳称不同代际（Qwen3 vs Qwen2.5），但论文 Section 3.2 和 4.1 均为 Qwen3-8B——R2 事实判断有误，R1 担忧成立。
- Llama/Gemma 独立验证相同 pattern 部分缓解。
- **Action**: 正文更显著标注；或用独立翻译模型验证。

**[W6] 贡献权重不均衡 / C2 定位争议（R2-W1/N3 vs R1 REBUT; 分歧）**
- R2 认为 C2 (asymmetry = general structure) 是 null result 包装为贡献；R1 反驳 ruling-out 有方法论价值。
- **共识**：不论定位，当前统计证据 (Qwen CI 含零、TOST 无效) 不足以支撑 claim 的强度。
- **Action**: 降低措辞强度或并入 C1。

**[W7] 机制深度偏浅（R2-W4; R1 部分 AGREE）**
- Logistic regression probing + linear steering 在 mechanistic interpretability 谱系中属浅层。Discussion 列三个假说均未验证。
- **Action**: 重新定位为 empirical probing study 或补充 activation patching。

### Info

**[I1] Fisher's exact test 用于 paired steering data（R1-W9; R2 AGREE）**
- Steering vs random control 是 paired design，McNemar's test 更合适。对 L13 (p=0.002) 不改变结论，但应在修改稿中统一。

---

## Reviewer Consensus

| 问题 | R1 | R2 | 状态 |
|------|----|----|------|
| Detection≠decision 过度概括 | W1 [critical] | N1 [critical] | **[AGREE]** |
| Qwen CI 含零 / Bonferroni 后仅 Gemma 显著 | W2 [critical] | 交叉 AGREE | **[AGREE]** |
| COMET tercile 欠功效 | W3 [critical] | 部分 AGREE（多层设计部分缓解）| **[AGREE-partial]** |
| 单 split 无 CV | W5 [warning] | W2 [warning] | **[AGREE]** |
| TOST 1.4% uninformative | W4 [warning] | AGREE | **[AGREE]** |
| Steering 仅英文 | W8 [warning] | AGREE | **[AGREE]** |
| Global FWER | W7 [warning] | 部分 AGREE | **[AGREE-partial]** |
| Fisher on paired data | W9 [info] | AGREE | **[AGREE]** |

## Reviewer Divergence

| 问题 | R1 | R2 | 分歧本质 |
|------|----|----|----------|
| 标题 "General" overclaim | REBUT（标题说 "Consistent With" 无问题）| N2 [critical] | 语义解读差异；R1 认为标题准确，R2 认为实验覆盖不足 |
| C2 是否为 null result | REBUT（ruling-out 有价值）| N3 [critical] | 方法论哲学差异；共识是证据力度不足 |
| Qwen 翻译模型双重角色 | W6 [warning] | REBUT（不同代际）| R2 事实判断有误（论文确为同一模型 Qwen3-8B）|
| 跨语言知识编辑文献 | REBUT（不同方向）| W5 [warning] | 相关性判断差异；R1 认为 editing ≠ probing/steering |

---

## Questions to Authors（汇总，去重后 10 条）

1. Basu et al. (2026) 已建立单语 detection-steering dissociation。本文跨语言设定具体揭示了哪些单语无法观察到的现象？
2. Qwen/Gemma 是否测试了目标层 ±2 层范围？如果 Llama 因果窗口仅 4 层宽，仅测 1 层的 null 能否排除存在因果位点？
3. Qwen Δ_asym CI [-0.6, 13.7] 包含零。三模型 Bonferroni 校正后仅 Gemma 显著。如何维护 "consistent" 论断？
4. Table 1 Δ_asym (bootstrap mean 7.3pp) 与算术差 (11.0pp) 差距 3.7pp 的来源？是否暗示 peak layer 在 bootstrap 样本间偏移？
5. Gemma COMET tercile Δ=+10.3pp 在混淆方向——能否提供 COMET score 与 probe accuracy 的连续回归结果？
6. EN-DE 已翻译完成（Section 3.5）——为何不做完整四方向探测实验以直接支持泛化 claim？
7. Steering 为何仅在英文数据评估？中文输入 + ZH→EN probe steering 的结果？
8. 如果选择 ±5pp 等价边界重做 TOST，预计结论是否改变？
9. 论文称 Gemma ConflictQA 保留 1590 样本，但 probe accuracy 最高 (88.9% at L17)。保留率最高+准确率最高是否暗示 probe 捕获了 task-irrelevant 信号？
10. All-position injection 与 last-token injection 在 L13 产生 "identical results"——具体数字？

---

## Missing References

**R2 建议（R1 部分反驳）**：
- "Editing Across Languages: A Survey of Multilingual Knowledge Editing" (2025)
- CLM-Bench (2026)
- BMIKE-53 (53-language knowledge editing benchmark)

R1 认为 knowledge editing (参数修改) 与 probing/steering (推理时干预) 方法论不同，8 页限制下引用需选择性。建议选择性引用最相关的 1 篇。

---

## External Review

**状态**: 未配置（项目未启用 paperreview.ai）

---

## Visual Layout Check（非评分项）

**状态**: ✅ 完成 | 0 critical, 0 warning, 3 info

排版质量良好，仅有三个建议性意见：
1. **Page 6**: 单页堆叠 3 个 display items (Figure 3 + Table 1 + Figure 4)，每个尺寸偏小，Figure 3 axis label 和 legend 字号接近可读下限
2. **Page 12**: 末页 appendix 底部约 35% 空白
3. **Page 5**: 纯文本高密度页（Experimental Setup），可考虑将部分细节移至 appendix

---

## Overall Assessment

### 评分: 3.0 — Findings

**R1**: 3.0 (Findings) | Confidence 4/5
**R2**: 3.0 (Findings) | Confidence 4/5
**Director 综合**: **3.0 (Findings)**

### 评分理由

**为什么不是 3.5 (Borderline Conference)**：
- 核心因果贡献 (detection≠decision) 仅 1/3 模型 1/32 层支持，替代解释未排除
- 与 Basu et al. (2026) 差异化不清晰——核心 insight 已被单语工作建立
- Asymmetry "consistency" 统计不充分（Bonferroni 后仅 1/3 模型显著）
- 四个贡献中两个薄弱（C2 统计不足、C3 证据单薄）

**为什么不是 2.5 (Borderline Findings)**：
- 混淆因素控制设计 (XNLI + EN-DE + COMET) 是真正可复用的方法论贡献
- 三模型 × 两任务方向一致性 (binomial p=0.016) 提供跨架构描述性证据
- 统计方法总体规范（bootstrap、Bonferroni、selectivity control）
- 诚实报告负面结果 + 代码公开
- Seed replication 增强 Llama L13 因果 claim 可信度

**一句话总结**：方法论控制设计出色的跨语言 probing 研究，描述性发现扎实，但核心因果 claim 证据单薄且新颖性被 Basu et al. (2026) 部分消解。修改后适合 Findings 接收。

---

## Detailed Comments（逐节）

**Abstract**: 约 164 words，符合 ≤200 要求。"these findings indicate that linear detectability does not imply causal relevance" 措辞需降级——这仅在 Llama 观察到，不构成三模型的一般性结论。

**Introduction**: Figure 1 有效传达核心问题。三个 RQ 设置清晰。但 Contributions 4→3 是否更诚实（将 C2 并入 C1）值得考虑。

**Related Work**: 覆盖充分（Zhao/Basu/Hewitt/Belinkov/Li/Turner/Marks/Pokharel/Sundar/Gurgurov 均已引用）。Basu et al. 差异化可更突出。跨语言 knowledge editing 方向可选择性引用 1 篇。

**Method**: 清晰规范。COMET back-translation 验证、selectivity control、random direction control 设计得当。Bonferroni 阈值说明清楚。

**Experiments 4.1-4.2**: 检测结果扎实，三模型一致。

**Experiments 4.3-4.4**: Asymmetry + XNLI baseline 是论文亮点，但需修正统计措辞（Qwen 不显著、报告校正后结果）。

**Experiments 4.5**: COMET tercile 作为辅助证据可保留，但需明确标注功效限制 + 对 Gemma 趋势做进一步分析。

**Experiments 4.6**: Steering 是论文核心贡献所在，Llama L13 证据（含 seed replication）可信。但跨模型 null result 的解释需更审慎。

**Discussion**: 三个假说框架合理，但未验证任何一个。重新定位为开放问题而非论文贡献。

**Conclusion**: 存在但过于简短（2 句）。核心 takeaway 的措辞需与 Weaknesses 修改同步调整。

**Limitations**: 诚实且覆盖主要局限。CV 承诺 + Qwen dual role + steering 方法局限均已提及。

**Appendix**: Boundary replication (N=201)、seed replication、AUROC、matched-condition 均有价值。

---

## 格式合规

| 检查项 | 结果 |
|--------|------|
| 正文 ≤ 8 页 | ✓ |
| Limitations 存在且位置正确 | ✓ (p.9, 正文后) |
| Abstract ≤ 200 words | ✓ (~164 words) |
| Double-blind 匿名化 | ✓ |
| ACL 模板 | ✓ (\usepackage[review]{acl}) |
| 代码可用性声明 | ✓ (anonymous.4open.science) |
| AI 使用声明 | ✓ (Appendix A) |

---

## Issue Tracker 更新摘要

- **Round 3 resolved in R4**: R3-N1 (Mirror→Consistent With), R3-W3 (selectivity), R3-W4 (AUROC), R3-W5 (α justification), R3-M1 (COMET version), R3-M2 (Jaccard floor), R3-M4 (random control), R3-M5 (Figure 3 band)
- **Round 3 still open in R4**: R3-N2 (COMET power), R3-N3/R1-N2 (detection≠decision), R3-W1 (single split), R3-W2 (Qwen dual role), R3-W6 (hypotheses untested), R3-NOV (Basu novelty)
- **New in R4**: R4-N1 (Qwen CI zero + Bonferroni), R4-W1 (FWER), R4-W2 (EN-only steering), R4-W3 (TOST), R4-W4 (contribution weight), R4-I1 (Fisher paired)
