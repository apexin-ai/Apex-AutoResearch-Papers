---
round: 11
overall_score: 3.0
timestamp: 2026-05-18T13:19:18.260223+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告 — Round 12

**论文**: Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models
**目标 Venue**: EMNLP 2026 (via ARR May 2026 cycle)
**Reviewer 编排**: R1 (方法严谨性 + 实验设计) + R2 (新颖性 + 写作质量 + 完整性)
**审稿轮次**: Round 12 (重新审稿，fresh mode)
**外部审稿**: 未请求（项目无 external_review 配置）

---

## Summary

本文研究 reasoning model self-jailbreak 过程中 Safety Commitment Point (CP) 的检测，系统比较 hidden-state (HS) probe 与 text-based monitor。核心方法学发现：layer selection metric 的选择可以逆转 HS 优势结论——composite metric 中的 crossing rate 系统性偏向 shallow layers，在 corrected deep layers 上所有四个模型的 HS probe 对 384d text baseline 有显著 precision 优势（+15.4 to +32.5pp, Holm-Bonferroni corrected）。但换用 1024d encoder 后仅 1/4 模型保持显著性。覆盖 4 个模型（2 架构 × 2 规模），报告 7 种替代方法的负面结果。论文自我定位为 characterization study。

---

## Strengths

**S1. Layer selection sensitivity 是一个有真实价值的方法学发现** [R1-S1, R2-S1, 完全共识]
五指标消融（Section 4.2, Table 2, Figure 1）清晰展示 crossing rate 如何系统性偏向 shallow layers，representation compression analysis（Appendix B）提供因果解释。这一发现对整个 probing 文献有广泛意义，类比 Hewitt & Manning 2019 对 control tasks 的贡献。

**S2. 统计严谨性高于同类工作** [R1-S5, R2-S2, 完全共识]
12-test Holm-Bonferroni step-down + exact sign-flip permutation test 交叉验证 + 5-seed stability + control task selectivity + PCA capacity control + position residualization + encoder robustness + threshold sensitivity + K-ablation，构成罕见的多层次验证体系。

**S3. 极高的透明度** [R1-S2, R2-S5, 完全共识]
主动披露累积超参数空间（2,240 configs）、CP annotation IAA 缺失、32B 样本量限制、FPR 39-52%、M002 bug disclosure（Appendix I）。Bug disclosure 在学术论文中极为罕见，值得赞赏。

**S4. 7-8B 结果稳健** [R1-S3, 完全共识]
R1-8B 和 OT-7B precision 优势在 5-seed stability 下 std < 8pp，control task selectivity 12.5-19.7pp 超过推荐的 5pp 阈值。

**S5. 负面结果系统性且有信息量** [R1-S4, R2-S3, 完全共识]
7 种替代方法的失败模式详细分析，特别是 RepE 的 metric-dependent discrepancy 分析和 BOCPD/CUSUM 在 gradual transition 上的失败，切实收窄了未来研究空间。

**S6. 写作质量良好** [R2-S4]
无 em-dash/en-dash 解释性滥用，无 -ing 分词短语结尾。Abstract ~220 words，回答四个必答问题。

---

## Weaknesses

### Must-Fix（影响接收决定）

**MF1. [Critical] Headline claim 依赖弱基线，encoder-conditional 性质未充分体现** [R1-N1 partial + R2-N1, 完全共识]

384d MiniLM（2020 年小型蒸馏模型）对 4096-5120d hidden state 存在先验可预期的信息论劣势。换用 BGE-large-1024d 后仅 1/4 模型通过 Holm-Bonferroni。PCA-384d capacity control 证明 modality effect 存在（all four pass HB at matched dimensionality），但 Abstract/Introduction/Conclusion 仍以 384d 为 headline 数字，1024d 结果被处理为 caveat。

- 论文自己的数据表明优势有两个可分离成分：robust modality effect + encoder-dependent magnitude，但叙事权重分配不反映这一结构。
- R1 补充：更准确表述应为 "encoder quality-conditional" 而非仅 "dimensionality-conditional"。
- **要求修改**: Abstract/Introduction/Conclusion 将 encoder-conditional 从 caveat 提升为核心发现；384d 和 1024d 结果并列呈现。

**MF2. [Critical] 32B 模型证据脆弱，"all four models" claim 具有误导性** [R1-N1+N2, R2-N2, 完全共识]

两个 32B 模型各有严重 caveat:

*QwQ-32B*: Position-only baseline BA(0.832) > HS BA(0.796)（Table 5）。HS 相对 position 的 precision 和 FPR 优势不显著（+4.5pp, p=0.133; +2.5pp, p=0.279）。HS 击败了比 trivial position baseline 更弱的 text probe——这种胜利信息量有限。

*R1-32B*: 仅 W=1 通过 HB，coverage 25%（5/20 traces）。5-seed precision std=0.128（range 0.441-0.750），FPR std=0.145（seed-0 outlier FPR=0.483）。

"All four models pass Holm-Bonferroni" 形式上成立（HS vs 384d text），但 32B 证据极其脆弱。

- **要求修改**: (1) 明确区分两个 evidence tier（7-8B robust, 32B suggestive），在 Abstract/Conclusion 不再使用 "all four models" 无差别 claim；(2) 报告 5-seed HB passing rate；(3) R1-32B 标注为 marginal；(4) 补充 QwQ-32B position-residualized HS vs text 的 HB comparison。

**MF3. [Critical → Should-Fix, 分歧] Joint (layer, W) validation 不完整** [R1-N3 Must-Fix, R2-REBUT→Should-Fix]

仅对 QwQ-32B 做了 (layer, W) grid search（192 configs），R1-32B 完全缺失。

- R1 观点: 对以 "layer selection sensitivity" 为标题的论文，只在 1/4 模型上验证 joint stability 是严重方法学缺口。
- R2 反驳: (1) 五指标消融已在全部 4 模型完成，joint search 是二次验证；(2) QwQ 和 R1-32B 共享 Qwen-32B 架构，有一定可迁移性；(3) R1-32B 根本瓶颈是 n=20 而非 joint validation 缺失。
- **Director 判定**: 降为 Should-Fix。R2 的论证合理——核心层选择证据（五指标消融）已全模型覆盖，joint grid search 是补充验证。但仍建议在 Limitations 中明确讨论此缺失。

### Should-Fix

**SF1. CP annotation IAA 未知，威胁 lead time 结论** [R1-W1, R2-W3, 完全共识]
CP "permanently ceases" 定义在操作上有歧义，标注协议未说明标注者数量和资质。如标注误差 ≥2 steps，QwQ-32B lead time (-1.2 to +1.9 steps) 完全落入噪声。Limitations 已有讨论但应强化量化影响。

**SF2. "Characterization" 定位与 Discussion deployment 建议矛盾** [R2-W1, R1-AGREE]
论文多处声明 "characterize rather than production detectors" 但 Discussion 给出 "W=3-15 as starting configuration" 的部署建议。建议改为条件性语言。

**SF3. Discussion 与 Conclusion 高度重叠** [R2-W5, R1-AGREE]
重叠约 60-70%，浪费正文空间。建议压缩 Conclusion。

**SF4. Joint (layer, W) grid search 缺 R1-32B** [原 MF3，降级]
至少在 Limitations 中明确讨论缺失原因和影响。

**SF5. Canonical split vs 5-seed mean 数值一致性** [R1-W3]
R1-8B canonical ΔPrec = +32.5pp，但 5-seed mean precision = 0.590±0.072。需报告 5-seed mean ΔPrec 以确认 headline 数字是 typical 还是 best case。

**SF6. Negative results contribution 叙事定位** [R2-W4, R1-partial REBUT]
每种方法有诊断性解释（R1 认为定位清晰），但读者可能读为 "七种方法都不行只能用 LR"。建议在 Section 4.5 开头强化 framing：这些失败本身揭示了 commitment structure 的 gradual 和 model-specific 特性。

### Minor

- m1: Introduction "Naïve reasoning suggests HS should dominate" 从信息论角度暗示 HS>text 是预期结果，削弱 Contribution 2 的 surprise value [R2, R1-AGREE]
- m2: R1-32B std=0.128 应在主文突出而非仅在 Table 3 脚注 [R1-m2]
- m3: Abstract 第 2 段信息密度过高（PCA、two components 细节可移至正文）[R2]
- m4: Position residualization 缺 R1-32B 结果 [R1-m5]
- m5: K=5 "pre-selection" 无 pre-registration 证据 [R1-m4]
- m6: Bib 中 3 条 "and others" 条目应列全作者 [R11-N5，历史遗留]
- m7: 正文仅 2 个 Figure，信息密度偏低 [R7-W5，历史遗留]
- m8: 补充 Geiger et al. 2024 (causal abstraction) 引用 [R2，R1-AGREE]

---

## Reviewer Consensus [AGREE]

1. **Layer selection sensitivity 是有价值的方法学贡献**（两位独立确认，类比 Hewitt & Manning 2019）
2. **"All four models" headline claim 具有误导性**（QwQ-32B position confound + R1-32B fragility → 需两级 framing）
3. **Encoder-conditional 性质应提升为核心发现**（384d headline + 1024d caveat 的叙事权重分配不当）
4. **7-8B 结果稳健，32B 结果为 suggestive 级别**
5. **统计方法和透明度高于同类工作**
6. **Overall 3.0 (Findings)**——适合 Findings 接收，不足以支撑 Main conference

## Reviewer Divergence [REBUT]

1. **Joint (layer, W) validation 严重等级**: R1=Must-Fix, R2=Should-Fix
   - Director 判定: Should-Fix（R2 论证合理，核心证据已全模型覆盖）
2. **贡献新颖性是否构成 Must-Fix**: R2=Must-Fix (N3), R1=部分 rebut
   - R1 认为 ARR guidelines 反对 penalizing negative results/simplicity，但同意当前证据更适合 Findings
   - Director 判定: 作为评分理由记录，不作为作者 action item（贡献定位难以通过修订改变）
3. **PCA-384d 措辞**: R1=Should-Fix (过强), R2=REBUT (已足够审慎)
   - Director 判定: 当前措辞可接受（"rules out a *pure* capacity explanation but not all encoder-quality effects"）
4. **Related Work 风格**: R2=偏列举, R1=survey-with-positioning 可接受
   - Director 判定: 当前水平可接受，不列入 action items

---

## Questions for Authors

Q1. 5-seed 条件下各模型 HB passing rate 是多少？（判断 "all four pass HB" 的可重复性）
Q2. QwQ-32B position-residualized HS vs text 的 HB 结果？（判断 QwQ-32B HS advantage 是否超出 position contribution）
Q3. 5-seed mean ΔPrec (HS-text) 及其 std？（判断 canonical +32.5pp 是 typical 还是 best case）
Q4. 是否考虑测试 LLM-based text encoder（如 E5-Mistral-7B, 4096d）？如消除 HS 优势，核心发现需根本性重新定位。
Q5. Layer selection bias 是否在非安全 probing 任务中也存在？如能复现，Contribution 1 影响力大幅提升。
Q6. CP annotation 标注协议和操作化细节？标注者数量和资质？

---

## Missing References

- Geiger et al. 2024, "Causal Abstraction" [R2 提出, R1 AGREE]
- Ravichander et al. 2021, "Probing the Probing Paradigm" [R2 提出, R1 认为非必要但可补充]

---

## External Review (Stanford Agentic Reviewer)

未请求（项目未配置 external_review）。

---

## Overall Assessment

**3.0 — Findings (可被 Findings 接收)**

**置信度**: 4/5（两位 Reviewer 均熟悉 probing methodology、bootstrap inference、LLM safety）

| 维度 | R1 | R2 | 综合 |
|------|-----|-----|------|
| Soundness | 3/5 | 3.5/5 | 3.0/5 |
| Excitement | 3.5/5 | 2.5/5 | 3.0/5 |
| Reproducibility | 3/5 | 4/5 | 3.5/5 |

**核心判断**: Layer selection sensitivity 是一个有真实价值的方法学发现，对 probing 文献有广泛意义，统计严谨性和透明度均高于同类工作。但：(1) headline claim 系统性依赖弱基线，1024d encoder 下仅 1/4 模型保持显著性；(2) 32B 模型证据极其脆弱（QwQ-32B position confound, R1-32B 25% coverage + 高 variance），"all four models" 无差别 claim 具有误导性；(3) 作为 characterization study 不提出新方法，excitement 有限。

**提升至 3.5 (Borderline Conference) 的路径**:
1. 将 "7-8B robust / 32B suggestive" 两级 framing 提升至 Abstract/Introduction
2. 将 encoder-conditional 从 caveat 提升为核心发现（并列 384d 和 1024d）
3. 报告 5-seed HB passing rate 和 mean ΔPrec
4. 补充 QwQ-32B position-residualized modality comparison
5. （可选但高回报）验证 layer selection bias 在非安全 probing 任务中也存在

---

## Detailed Comments

### Abstract
- 以 384d 为 headline（+15.4 to +32.5pp），1024d 仅作 caveat → 叙事权重需调整
- "all four models" 应改为含 32B caveat 的措辞
- "At 32B (n=19-20, sample-limited)" 已有但不够突出
- 第 2 段信息密度过高（PCA-384d, two separable components 细节可移至正文）
- ~220 words，在 150-250 范围内

### Introduction
- "Naïve reasoning suggests HS features should dominate" 从信息论暗示 HS>text 为预期，削弱 Contribution 2
- 五段结构完整
- Characterization scope statement 在末尾出现

### Related Work
- 覆盖较完整（54 references），按子主题分组
- 缺 Geiger et al. 2024 (causal abstraction)
- 第 2-3 段有轻微列举倾向（R2 指出，R1 认为可接受）

### Method
- Layer selection sensitivity 论证清晰（Section 3.3）
- Evaluation protocol 严格（Section 3.5）
- PCA capacity control 措辞已审慎（"rules out pure capacity explanation"）

### Experiments
- 7-8B 结果稳健且充分
- 32B 需补充材料（5-seed HB rate, position-residualized comparison）
- Negative results 系统但可强化 framing（Section 4.5 开头）
- Table 3 列过多，384d/1024d 可考虑拆分

### Discussion
- 与 Conclusion 重叠 ~60-70%
- Deployment 建议（W=3-15）与 characterization 定位矛盾
- Encoder-conditional advantage 分析合理但叙事权重未反映在 headline

### Limitations
- 内容充实（32B caveats, FPR, cumulative DoF, CP annotation, scope）
- 建议强化 CP annotation uncertainty 的量化影响

### Format
- ACL template [review] ✓
- Double-blind ✓
- Limitations section ✓
- Responsible NLP Checklist ✓
- Bib: 3 条 "and others" 待修复