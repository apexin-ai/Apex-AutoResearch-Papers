---
round: 7
review_mode: continue
overall_score: borderline accept
timestamp: 2026-05-29T00:55:29.551156+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# Round 7 审稿报告：Why Token Pruning Crashes Some Robot Policies but Not Others

**Venue**: CoRL 2026 | **Deadline**: 2026-05-29 | **审稿模式**: Continue (基于 Round 6)
**Round 6 评分**: 5/10 (Weak Reject) | **Round 7 评分**: 6/10 (Borderline Accept)

---

## Summary

论文从 Round 6 显著改进。新增 zero-mask ablation（分离 position disruption vs information loss，89pp gap）、attention-based scoring double dissociation（connector 决定哪种 scoring 有效）、π₀.5 Long 5-seed 验证、OpenVLA 全 4 suite 数据。Table 2 主表完整化，Limitations section 独立且全面。两个 Round 6 critical issue 已 resolved（attention baseline、OpenVLA multi-suite）。但发现一个严重退化——7+ concurrent works 被从引用中删除——以及因果语言 "primary determinant" 仍未替换，与 Limitations 中 "cannot be causally isolated" 自相矛盾。

---

## Strengths

**S1** [R1+R2 共识] **Attention scoring double dissociation 是论文最有 insight 的新发现。** L2 对 independent connectors 有效（π₀.5 Goal +35.2pp），attention 对 entangling connectors 有效（X-VLA ≥92.8%），且两者不可互换（π₀.5 Object attention −31.6pp, X-VLA L2 −27.2pp）。Table tab:scoring_crossover_summary 的 2×2 矩阵清晰展示了 connector-dependent scoring reversal。这比 Round 6 提供的任何 contribution 都更有 depth。

**S2** [R1+R2 共识] **Zero-mask ablation 实验设计 elegant。** 将 10% token embedding 置零（100% 信息损失，0% 位置变化）保留 98.0% SR vs hard pruning（位置变化）崩溃到 9.0%——如果信息丢失是主因，zero-masking 应更差，但实际结果相反，清晰归因于 position disruption。

**S3** [R1+R2 共识] **Table 2 主表完整化 + multi-seed 验证大幅提高可信度。** 主表 3 模型 × 4 suite × 3 k-values 无缺失。π₀.5 Long n=5 seeds（s.d. ≤2.7pp）确认 V-shaped random recovery 是 structural property。

**S4** [R1+R2 共识] **Limitations section 扎实诚实。** 独立 section，7 句话覆盖 sim-only/causal isolation/N=4/VTR generalization/scoring methods/single-seed + AI disclosure。

**S5** [R2] **论文 identity 更清晰。** 从 Round 6 的 "observation-heavy empirical study" 进化为有 mechanistic insight 的分析——zero-mask 和 attention scoring 各自提供了 WHY 层面的解释。

---

## Weaknesses (Must-Fix)

**W-MF1** [R2 发现, R1 AGREE, Director 独立验证] **7+ concurrent works 被从引用中删除——Related Work 覆盖严重退化。**

Director 独立验证确认：`references.bib` 中存在以下条目但活跃 .tex 文件中无 `\cite{}`：
- **jabbour2025dontrun** ("Don't Run with Scissors") — 最接近的 concurrent work，也发现 pruning breaks VLA 并提出 recovery method
- **wang2025specprunevla** (SpecPrune-VLA) — VLA pruning 方法
- **feng2026seewhatmatters** ("See What Matters", ICML 2026) — VLA pruning
- **zhang2025sparsevlm** (SparseVLM) — VLM token sparsification
- **khaki2025sparsevila** (SparseVILA) — VLM token sparsification
- **ye2025fitprune** (FitPrune) — VLM token pruning
- **shi2024crossget** (CrossGET) — ViT token pruning

Round 6 论文引用了这些工作；Round 7 修改中被移除。在 blind review 中删除最接近的 concurrent work 极其危险——reviewer 若了解 "Don't Run with Scissors" 会认为故意回避比较。

**W-MF2** [R1+R2 全员共识] **因果语言 "primary determinant" 未替换——Round 6 明确要求但未执行。**

Director 独立 grep 确认：
- `introduction.tex`: "identifying the vision-language connector as the **primary determinant** of pruning robustness"
- `abstract.tex`: "the **primary architectural factor** governing pruning tolerance"
- `conclusion.tex`: "Connector architecture is the **primary factor** governing VLA token compressibility"

Round 6 修复声明称已替换为 "most consistent structural factor"，但实际未执行。`limitations.tex` 写 "preventing full causal isolation of the connector effect"——与主文 "primary determinant" 自相矛盾。这是第三轮提出此问题（Round 4 → 5 → 6 → 7），属于反复回归。

---

## Weaknesses (Should-Fix)

**W-SF1** [R1+R2 共识] **CV diagnostic 仍仅 N=4 闭环模型，无新数据。**

Table 1 不变：π₀.5, X-VLA, OpenVLA, SmolVLA（闭环）+ π₀, OFT（offline）。CogACT 仅从文献引用（74.2% SR under 78% pruning），无原始 CV 数据。论文已将 claim 收窄为 "validated on four closed-loop architectures"，Limitations 承认 "too few for a general law"，属正确降级。从 Round 6 的 critical 降级为 major warning——claims 已适当收窄，但 evidence base 未增加的事实不变。

**W-SF2** [R2] **X-VLA Goal attention 结果在 Table tab:attention_pruning 中合并为 "98.2*"。** 其他三个 suite 分别列出 attn_last/attn_mean/attn_rollout，Goal 合并为 "Best of three attention variants"。不一致暗示选择性报告。应展开为三列或标注 "all three ≥X%"。

**W-SF3** [R2] **OpenVLA 移至附录造成主文叙事断裂。** Table 2 仅 3 个模型（π₀.5, X-VLA, SmolVLA），CV spectrum 缺少 0.215 的 MLP calibration 点。论文声称 "six architectures" 但主表仅 50% 模型。建议至少加入 OpenVLA Object 行。

**W-SF4** [R2] **Appendix Table 4 caption 说 "Full results" 但仍有 ~14% "--" 缺失。** OpenVLA k=0.95/0.7/0.5 大部分缺失；X-VLA k=0.7 Spatial/Long 缺失。应改 caption 为 "available results" 或补全。

**W-SF5** [R2] **代码/数据发布计划仍缺失。** Round 6 R3-W3 要求添加发布声明，Round 7 未见。

---

## Weaknesses (Info / Minor)

**I1** [R2] Abstract 数字密度仍高（~16 个数值），Round 6 要求从 ~17 降到 ~5 未充分回应。新增内容（zero-mask, scoring reversal）有价值但数字未精简。

**I2** [R2] Zero-mask ablation 的 "entirely attributable to position disruption" 应限定为 "on π₀.5"，因机制与 RoPE 相关，不一定 generalize 到 non-RoPE 架构。

**I3** [R1] Abstract 使用 π₀ (offline-only) 的 CV=0.038 作为 spectrum 下界，未标注 offline。

---

## Questions

**Q1** X-VLA Goal attention 三种 variant 各自的 SR 是多少？如果差异 <2pp 为何不展开？如果差异大为何只报告 best？

**Q2** Zero-mask 是否在其他模型（X-VLA、OpenVLA）上测试过？如果是，结果如何？如果否，为什么不？

**Q3** Round 7 Related Work 为何删除了 7+ concurrent works 的引用？是有意精简还是修改过程中的疏忽？

---

## Missing References

以下引用在 `references.bib` 中存在但未在正文引用——应恢复：

1. Jabbour et al., "Don't Run with Scissors: Pruning Breaks VLA Models but They Can Be Recovered," 2025
2. Wang et al., SpecPrune-VLA, 2025
3. Feng et al., "See What Matters," ICML 2026
4. Zhang et al., SparseVLM, 2025
5. Khaki et al., SparseVILA, 2025
6. Ye et al., FitPrune, 2025
7. Shi et al., CrossGET, 2024

---

## External Review

外部审稿未请求（Round 7 为 continue 模式）。

---

## Visual Layout Check（非评分项）

视觉审查 Agent 已完成（4 分钟）。结果：**0 critical, 0 warning, 9 info**。

- 首页无 display item（Figure 1 在 page 2），建议但非必须
- Figure 1(b)/Figure 2 架构图组件标签字号偏小（~6-7pt），建议放大
- Figure 4(b) 散点图标注字号偏小，建议 ≥8pt
- Table 2 格式规范 ✓（booktabs + 加粗最优值）
- 附录 Table 4 密度高但可接受
- Figure 9 使用颜色+标记双编码，打印友好 ✓
- 正文 8 页合规 ✓

---

## Round 6 → Round 7 Issue 追踪总结

| Issue | Round 6 状态 | Round 7 状态 | 变化 |
|-------|-------------|-------------|------|
| R6-C1 (CV N=4) | critical/in_progress | warning/in_progress | Claims 收窄，降级 |
| R6-C2 (Table 2 gaps) | critical/in_progress | info/resolved | 主表完整 |
| R6-C3 (Causal language) | critical/resolved | critical/in_progress | **REGRESSION** |
| R6-C4 (Attention baseline) | critical/in_progress | **resolved** | 3 模型全覆盖 |
| R6-W5 (OpenVLA multi-suite) | warning/in_progress | **resolved** | 4 suite 数据 |
| R6-W6 (Code release) | warning/resolved | warning/in_progress | 回归 |
| R6-I2 (Abstract density) | info/resolved | info/in_progress | 未改善 |
| R7-N1 (Citations deleted) | — | **critical/open** | 新发现 |
| R7-W1 (Goal attention merge) | — | warning/open | 新发现 |

**净变化**：+2 resolved (C4, W5)，+1 regression (C3)，+1 new critical (N1)，1 downgraded (C1)

---

## Overall Assessment

**Round 7 评分：6/10（Borderline Accept）**

**升分理由（5→6）**：
- Attention scoring double dissociation 是 genuine insight（S1）——connector 决定哪种 scoring 有效，没有 universal winner
- Zero-mask ablation 实验设计 elegant，清晰分离 position disruption vs information loss（S2）
- Table 2 完整化 + π₀.5 Long n=5 multi-seed 消除关键统计疑虑（S3）
- 两个 Round 6 critical issue resolved（attention baseline、OpenVLA multi-suite）
- Limitations section 扎实诚实

**未达 7/10 的理由**：
- **7+ concurrent works 被删除是 unacceptable regression**——必须在提交前修复（W-MF1）
- **"Primary determinant" 因果语言第三轮未修正**——与 Limitations 自相矛盾（W-MF2）
- CV diagnostic 仍仅 N=4 闭环模型，evidence base 未增加（W-SF1）
- Simulation-only 对 CoRL 的 practical impact 有限
- VTR 仅在 SmolVLA 验证，MLP adapter 达到 comparable 性能

**从 6→7 需要**：
1. 恢复所有被删除的 concurrent work 引用，"Don't Run with Scissors" 需专门段落
2. 全文统一非因果措辞（"strongest predictor" 或 "most consistent structural factor"）
3. 展开 X-VLA Goal attention 数据

---

## Detailed Comments

### Round 7 修改亮点

论文在实验深度上有显著进步。Attention scoring 从 zero 覆盖扩展到 3 个模型 × 4 个 suite 的系统比较，揭示了 connector-dependent scoring reversal——这是 Round 6 版本完全缺失的 mechanistic insight。Zero-mask ablation 用优雅的实验设计回答了 "为什么 10% token 移除会导致 89pp 崩溃" 这个核心问题。π₀.5 Long 的 5-seed 验证将关键数据点从单一观察提升为可重复发现。

### 遗留问题优先级

1. **P0（阻止提交）**：恢复 7+ concurrent work 引用。"Don't Run with Scissors" 是最近的 concurrent work——在 blind review 中遗漏它等同于放弃通过 novelty 检查的机会。
2. **P0（阻止提交）**：统一因果语言。这是第三轮相同问题，abstract/intro/conclusion 各用不同措辞且与 limitations 矛盾。30 分钟文本替换即可解决。
3. **P1**：展开 X-VLA Goal attention 数据。
4. **P2**：Appendix table caption 修正（"available" not "full"）；Abstract 数字精简。