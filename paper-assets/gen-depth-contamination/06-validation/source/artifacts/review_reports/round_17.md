---
round: 17
review_mode: fresh
overall_score: 3.0
timestamp: 2026-05-20T04:19:22.257308+00:00
reviewer_ids: ['1', '2']
cross_response_reviewer_ids: ['1', '2']
force_resubmit: False
---

# 审稿报告：Generational Depth Estimation of Recursive Synthetic Text

**Venue**: EMNLP 2026 (ARR May 2026)
**审稿轮次**: Round 14 (Fresh Review)
**Reviewer 编排**: 2 人（R1: 方法严谨性 + 实验设计; R2: 新颖性 + 论文完整性 + 写作质量）

---

## Summary

本文提出 generational depth estimation 作为新问题，定义了 K*（在 CI-based AUC 准则下分类器能可靠区分相邻递归生成深度的最大层数），使用 15 维统计特征 + OBD-LightGBM 分类器，在 9 个模型配置（5 架构家族，1B-14B）上实验发现 prompt-chain web text K*=2（8/9 配置），arXiv K*=3，Wikipedia K*=1，Code K*=1-2。DeBERTa-v3-base 在 C4 上无法突破 K*=2（1.5B/14B/32B）但在 Wikipedia 和 arXiv 上各恢复 +1 深度，建立了 domain-dependent 的 two-tier ceiling。Filtering 实验作为 proof-of-concept 验证 K*=2 与 binary > graduated 策略排序一致。

---

## Strengths

1. **问题定义新颖且有实用价值**：将递归合成文本的生成深度估计从 binary detection 和 model collapse 中独立出来，K* 的形式化定义（Eq. 1）清晰，DPI 理论动机合理。[R1, R2 共识]

2. **CI-based 统计框架严谨**：用 bootstrap CI lower bound 决定边界，配合 10,000-iteration permutation test（p < 0.001），避免 sampling noise 导致的虚假 K* 估计。三因素 ANOVA 确认 Scorer η²_p = 0.192 远小于 Depth-Pair（0.998）。[R1 S2, S3]

3. **实验覆盖度极高**：9 配置 × 5 家族 × 4 领域 × 4 解码策略 × 1.5B-32B 规模 × 22 组 cross-scorer 验证。附录 18 页涵盖 power analysis、LOFO、feature ablation、LaTeX markup ablation、retrain-chain 等。[R1 S7, R2 S2]

4. **Two-tier ceiling 发现有洞察力**：DeBERTa 在 C4 无法突破 K*=2 但在 Wiki/arXiv 恢复 +1，揭示 domain structural complexity 对判别边界的根本性约束。Mistral-7B 的 C4 K*=1 vs arXiv K*=3 清晰论证了 domain 而非 model identity 的主导作用。[R1 S4, S6; R2 S4]

5. **θ 敏感性分析和 domain ordering**：Figure 3 展示 domain ordering 的 θ-invariance（arXiv > C4 ≥ Code > Wikipedia），比绝对 K* 值更稳健。[R1 S5]

6. **写作质量整体扎实**：Related Work 覆盖全面（MAUVE、nucleus sampling、model collapse、data curation），Limitations 极其坦诚（9 条）。52 篇引用，0 孤立条目。[R2 S5, S6]

---

## Weaknesses

### Must-Fix（3 条，影响接收决定）

**MF-1. K* 对阈值 θ 的依赖性被低估，核心 claim 稳健性受损** [R1-W2, R2-N1; 共识]
- 论文声称 K*=2 在 θ∈[0.575, 0.625] 稳定，但该窗口仅 5pp。θ=0.625 时 OLMo 已降至 K*=1；LLaMA-8B CI lower=0.603 仅比 θ 高 0.003（1/5 folds 低于 θ）。LOFO 验证（8/9 匹配）用同一数据集的不同子集推导 θ，不构成外部验证。
- 真正有价值的发现是 1v2 vs 2v3 AUC 之间的 5-11pp gap（1v2 集中 0.61-0.70，2v3 集中 0.55-0.59），K*=2 是该 gap 在特定 θ 下的离散化。
- **建议**：并行报告 AUC gap + K*；各 θ 下配置细分；降低 K*=2 的 definitiveness；明确 K* 是 (feature set, θ) 联合条件下的操作性量。

**MF-2. Eq. 1 的 "max" 运算隐含未证明的单调性假设** [R1-W1; R2 AGREE]
- K* = max{k ≥ 1 : CI_low(AUC_{k-1,k}) > θ} 隐含假设 AUC_{k-1,k} 单调递减。DPI 保证 I(X;Y_k) 单调下降，但不保证相邻对 AUC 单调递减。若某一代引入特殊分布 artifact 导致 AUC 局部回升，"max" 会给出误导性 K*。
- Table 2 实证显示单调递减，method.tex L21 做了经验验证，但形式化定义不应依赖实证巧合。修改成本极低。
- **建议**：改用 K* = max{k : CI_low(AUC_{j-1,j}) > θ, ∀ j ≤ k}，或补充单调性作为显式假设。

**MF-3. Qwen 家族 5/9 配置导致独立证据被夸大** [R1-W3, R2-W2; 共识]
- 非 Qwen 证据：Pythia K*=2（clear），OLMo K*=2（clear），LLaMA K*=2（borderline, CI lower=0.603），Mistral K*=1（反例）。"8/9 configurations" 中 Qwen 贡献 5 个正例，仅 4 个独立架构的证据实为 2 clear + 1 borderline + 1 反例。
- **建议**：Abstract 改为 per-family 表述（"4/5 families"）；正文区分 within-family（scale/mode invariance）与 cross-family（4 个独立数据点）证据。

### Should-Fix（6 条）

**SF-1. 跨模型 transfer boundary fragile 但论文正面表述** [R1-W5, R2-W5; 共识]
- Section 4.2 承认 7B 4/6 off-diagonal 1v2 pairs 低于 θ，但标题 "Largely Generator-Independent Transfer"、Abstract 均未提及。"generator-independent" vs "largely generator-independent" vs "fixed reference scorer" 术语不一致。
- **建议**：统一术语，限定为 "within continuation mode"；Abstract/Conclusion 加 caveat。

**SF-2. Filtering 实验 framing 不一致** [R1-W6, R2-N2 部分; 共识]
- Introduction contribution (c) 提升 filtering 为贡献，但 Section 5 自身定位为 "consistency check"。0.77pp MMLU 改善，mixed contamination 效应量缩小 3-6×。arXiv K*=3 下 graduated filtering 同样失败（discriminability ≠ filtering utility）。
- **建议**：对齐 Intro contribution (c) 与 Section 5 表述；降低 Abstract 中 filtering claim 强度。

**SF-3. 正文超 8 页限制** [R2-W1; Visual Check 确认 critical]
- 主文（Discussion + Conclusion）延伸至第 9 页约 60%，Limitations 从页面下部约 40% 处开始。正文约 8.6 页，超出 EMNLP 2026 严格 8 页限制，有 desk reject 风险。
- **建议**：压缩 Section 5-7 约 0.5-0.6 页。

**SF-4. Bootstrap 重采样次数不一致** [R1-W4; R2 AGREE]
- 主表（Table 2）使用 1,000 resamples，其他表使用 10,000。borderline 配置（OLMo CI lower=0.605, LLaMA CI lower=0.603）在更精确 CI 下可能翻转 K* 判定。
- **建议**：统一使用 10,000 resamples。

**SF-5. Retrain-chain fold-based CI 方法论** [R1-W8; R2 AGREE]
- Retrain-chain 用 fold-based CI（x̄ ± 1.96·s/√K, K=5），df=4 下应使用 t 分布而非正态分布，可能低估方差。
- **建议**：使用 t 分布（df=4）。

**SF-6. 规模外推讨论不足** [R2-W3; R1 部分同意]
- Table 4 显示 1.5B→32B LightGBM 1v2 AUC 从 0.626 微降到 0.618。若趋势延续，70B+ 可能坍缩到 K*=1。Discussion 应讨论此趋势。

### Minor（4 条）

- Abstract 信息密度过高，建议精简至 3-4 核心 claim [R2-W4; R1 AGREE 降级 Minor]
- alemohammad2024selfconsuming OpenAlex first author mismatch，应核实 [R2]
- 附录表格编号不连续（Table 23 出现在 Table 9-10 之间）[Visual Check]
- Neural probe 仅覆盖 3 个 ≤1.5B 模型 [R1-W12]

---

## Reviewer Consensus [AGREE]

两位 Reviewer 在以下关键问题上达成完全共识：
1. **θ 依赖性是核心弱点**：K*=2 的稳定窗口窄于论文声称，LOFO 不构成外部验证
2. **Qwen 家族不平衡**：5/9 配置夸大了独立证据强度
3. **Transfer fragility 与正面表述矛盾**：boundary-level 在 7B 下 4/6 pairs 低于 θ
4. **Filtering framing 不一致**：Intro contribution (c) vs Section 5 "consistency check"
5. **Eq. 1 需修订**：单调性假设应显式化或改用更保守的定义

---

## Reviewer Divergence [REBUT]

**方法论新颖性是否构成 critical issue**：
- **R2 (3.0)**: 15D 手工特征 + OBD-LightGBM 均为成熟技术组合，方法论新颖性不足以支撑 Conference 定位，应降级为 Findings。
- **R1 (3.5)**: 贡献在 problem formulation（K*）而非分类器；使用成熟工具反而证明 K*=2 不依赖 fancy 模型；方法论新颖性应反映在 Excitement 维度而非 Soundness。ARR 评审应评估 claim support 而非 novelty。
- **Director 判断**：R1 的论点更符合 ARR 评审标准（Soundness 评估 claim support）。但 R2 的 Excitement 2.5/5 评分合理反映了方法贡献有限的事实。此分歧不影响核心修复建议。

**其他小分歧**（已解决）：
- arXiv n=2,200 可比性：R2 REBUT R1-W7，引用 power analysis（n≥2,000 sufficiency），合理。
- 多重比较校正：R2 REBUT R1-W9，K* 为描述性测量且 p << 0.001，Bonferroni 36× 后仍远低于阈值，合理。

---

## Questions（需作者澄清）

1. Eq. 1 实验中是否遇到过非单调 AUC_{k-1,k}？如果 AUC_{2v3} < θ 但 AUC_{3v4} > θ，K* 应如何定义？
2. Table 2 从 1,000 升级到 10,000 bootstrap resamples 后，OLMo 和 LLaMA-8B 的 K* 判定是否改变？
3. Retrain-chain fold-based CI 改用 t 分布（df=4）后，K*=7 判定是否改变？
4. DeBERTa arXiv K*=4 是否有跨模型 transfer 结果？
5. 10% 污染时 binary vs no-filter 的 MMLU exact pp 差距？

---

## Missing References

- Levin & Peres 2017, *Markov Chains and Mixing Times*（强化 DPI → K* 有限性论证） [R1]
- Singh et al. 2024, *Beyond Human Data: Scaling Self-Training*（iterative self-improvement 视角） [R1]
- Longpre et al. (data provenance/attribution), CCNet (web corpus quality) [R2, 可选]

---

## External Review (Stanford Agentic Reviewer)

外部审稿：未配置，未请求。

---

## Visual Layout Check（非评分项）

视觉审查已完成（耗时 ~4.5 分钟）。

| 严重度 | 数量 | 主要发现 |
|--------|------|----------|
| Critical | 1 | **正文超 8 页限制**（约 8.6 页），Discussion + Conclusion 延伸至第 9 页 60% 处，desk reject 风险 |
| Warning | 3 | Figure 4 红绿色阶对色盲不友好（建议 viridis）；附录表格编号不连续（Table 23 跳跃）；附录 pp.19-20 表格密度过高 |
| Info | 6 | 首页无视觉锚点（Figure 1 在第 2 页，可接受）；Figure 3-4 尺寸偏小；Figure 11 对比度偏低；p.26 底部空白；正文 display items 密度高但可接受；booktabs 格式专业统一 |

---

## Overall Assessment

### 评分

| 维度 | R1 | R2 | 综合 |
|------|------|------|------|
| Soundness | 3.5/5 | 4/5 | 3.5/5 |
| Excitement | 3.5/5 | 2.5/5 | 3/5 |
| Reproducibility | 4/5 | 4/5 | 4/5 |

**Overall Score: 3.0 (Findings)**

**置信度: 4/5**（两位 Reviewer 完整阅读全部 27 页含附录，交叉回应达成 13/15 共识）

### 评分理由

论文定义了一个有意义的新问题（generational depth estimation），实验覆盖极其充分（9 配置 × 4 领域 × 多种消融），统计方法论整体严谨。Two-tier ceiling 和 domain ordering 是有洞察力的发现。

但以下因素限制了评分：(1) K*=2 作为核心 claim 高度依赖 post-hoc 阈值 θ=0.60，稳定窗口仅 5pp，LOFO 非外部验证；(2) 方法论为成熟技术的直接组合，无新特征类型或分类框架；(3) 实际下游影响微弱（0.77pp MMLU），且 discriminability ≠ filtering utility；(4) Qwen 5/9 配置夸大了独立证据强度；(5) 正文超 8 页限制，有 desk reject 风险。

MF-1（θ 依赖性）和 MF-3（家族不平衡）是 framing 问题，可通过修订解决。MF-2（Eq.1 单调性）修改成本极低。SF-3（页数）是硬约束，必须修复。

**修复路径**：解决全部 Must-Fix + SF-3（页数）后，论文可达 3.5 (Borderline Conference)。若同时将 1v2-vs-2v3 AUC gap 作为主发现、增加非 Qwen 模型数据、并重新定位 filtering 为 consistency check，有望达到 4.0 (Conference)。

---

## Detailed Comments

### Section 1 (Introduction)
- Contribution (c) "practical validation" 与 Section 5 "consistency check" 定位不一致。降级 filtering 或统一表述。
- L7 的 prompt-chain vs retrain-chain 区分清晰，是对之前版本的明显改进。

### Section 3 (Method)
- Eq. 1 的 "max" 应改为 "∀ j ≤ k" 形式（修改成本极低）。
- θ=0.60 的 post-hoc 选择论证已相当充分（permutation test + LOFO + sensitivity analysis），但应更坦诚地承认 LOFO 是 internal consistency check 而非 external validation。
- 建议在 θ 讨论中补充：K* 是 operational parameter，应由用户根据应用场景校准。

### Section 4 (Experiments)
- "8/9 configurations" 应区分 within-family vs cross-family 证据。
- Section 4.2 标题 "Largely Generator-Independent Transfer" 与 boundary fragile 矛盾。
- Cross-scorer 20/22 的 2 个例外恰为最关键边界配置，应在正文而非仅附录讨论。

### Section 5 (Filtering)
- "consistency check" 定位准确，但 Introduction contribution (c) 需对齐。
- arXiv 上 K*=3 但 graduated filtering 失败，这一发现（discriminability ≠ filtering utility）本身值得在 Discussion 中展开。

### Section 6 (Discussion)
- Two-tier ceiling 段落是论文亮点。
- 规模外推趋势（1.5B→32B AUC 微降）值得补充讨论 70B+ 预测。

### Limitations
- 9 条 limitations 极其坦诚详尽，是论文强项。
- Limitation (8) 已承认 Qwen 家族偏重，但主文 framing 未充分体现。

### Format
- **页数超限是最紧急的修复项**（desk reject 风险）。
- Figure 4 应改用色盲安全 colormap。
- 附录表格编号跳跃需修复。