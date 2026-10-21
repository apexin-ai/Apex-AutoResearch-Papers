---
round: 10
overall_score: borderline
timestamp: 2026-05-16T19:56:30.820029+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# Round 10 审稿报告 — simgate-modular-routing

**论文**: "Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld"
**Venue**: EMNLP 2026 Main Conference Long Paper (ARR May cycle, deadline 2026-05-25)
**Reviewer 编排**: 2 人（R1: 方法严谨性+实验设计; R2: 新颖性+完整性）
**流程**: Round 1 独立审稿 → 交叉分享 → 1 轮即达共识

---

## Summary

本文提出 episode-level counterfactual analysis 框架和 Death Avoidance Factor (DAF) 指标，分解 modular LLM agent 的 routing signal 来源。在 ScienceWorld（11/30 task types, N=245, Qwen2.5-7B-Instruct）上发现 78.9% 的 non-tie routing labels（75/95, penalty-independent）由 death asymmetry 驱动；DAF=90.4%（P=100, score-level）。一个探索性 router 在 held-out episodes 上低于 chance（47.1% vs 50%）。跨环境（MATH N=300, ALFWorld N=135）和跨模型（Llama-3.1-8B, N=70）对比提供方向性辅助证据。

---

## Strengths

**S1. 问题定位有价值。** 在 routing 文献专注 "how to route" 时，追问 "what drives routing signal" 是更基础的元问题，具有方法论价值。

**S2. 统计报告诚实严格。** 主动报告 partial r=0.02 暴露 r=0.97 的数学必然性；标注 MATH p=0.079 "not reaching α=0.05"（power=0.42, N≈770）；bootstrap/LOO/Spearman 三重 robustness；8-seed cross-split evaluation。在 LLM agent 论文中属上乘。

**S3. 框架设计清晰可复现。** Algorithm 1 完备无歧义，penalty-independent (78.9%) 与 penalty-dependent (DAF) 两个互补指标的区分有思考，环境间异质性验证框架灵活性。

**S4. Negative result 诚实且有诊断价值。** Router failure + always-deterministic near-optimality + majority-class collapse 的组合对社区有建设性信息。

**S5. Limitations 实质性强。** 19/30 exclusion、penalty amplification、single-pass ReAct、distribution shift（DAgger）、7-8B scale 限制均主动列出。

**S6. 相对前几轮的改进明显。** 78.9% 现为 primary metric、r=0.97 标注 "largely mathematical consequence"、MATH 报告 power analysis、Llama 收窄到 "directional consistency"、within-sample CI caveat 添加——历次审稿意见得到了认真 addressing。

---

## Weaknesses

### Must-Fix (Critical) — 5 条

**C1. df=27 统计错误 [Consensus, NEW]**
- Section 4.1: "partial r = 0.02 (p = 0.91, df = 27)"。散点图 n=11 task types，控制 1 变量后 df 应为 8。若 episode-level（N=245）则 df=242。df=27 在任何合理计算下不成立。
- 虽然 r=0.02 极小（结论大概率不变），但这是论文 "r=0.97 is mathematical artifact" 论证的核心支撑，统计报告错误削弱方法论可信度。
- **要求**：明确计算 level，报告正确 df 和 p-value。

**C2. 核心发现 novelty 不足——DAF 接近 tautological [Consensus]**
- DAF = δP/(δP + Δ_nd) 在 P >> Δ_nd 时数学上必然趋近 1。P=100 而 Δ_nd=2.84，DAF 高是算术必然而非经验发现。论文多处自承 "mathematical consequence"。
- 真正的 empirical content 是 δ=0.2653（42.9% vs 16.3% death rate）和 Δ_nd=2.84（排除 death 后近乎无差异）。78.9% label fraction 是 penalty-independent 的经验发现。
- 论文已将 78.9% 置于 primary 位置（R9 修复），但 contribution framing 仍将 DAF 作为 key metric，且 title 暗示 "discovery"。对 EMNLP main conference，contribution sizing 存疑。
- **要求**：重构 contribution 叙事——以 δ 和 Δ_nd 的经验发现为核心，DAF 为 summary tool。或补充第二环境数据提升 convincingness。

**C3. 单一环境证据——无 death-dominance 的跨环境 REPLICATION [Consensus]**
- MATH: absence-of-evidence（no death → no death signal，power=0.42）。ALFWorld: 不同 mechanism。Llama: direction-only。Title 说 "the Dominant Routing Signal" 但仅 ScienceWorld 验证。
- 论文 Contribution 3 现为 "cross-context applicability"——改善但仍 overselling。Discussion 自承需 NetHack/Crafter。
- **要求**：Option A: pilot-scale 50-100 episodes 在第二个 catastrophic-failure 环境复现。Option B: 收缩到 "ScienceWorld-specific case study + framework proposal"，Findings track 定位。

**C4. Data scaling ablation 方法论缺陷 [Consensus]**
- Paraphrase augmentation 将 majority class 从 89.6% 膨胀至 97.7%，不生成新 routing patterns。Internal recall=0.0 at all scales（完全 majority-class collapse）可能反映 3.7% 极端 class imbalance 而非 structural limitation。
- Appendix 有 hedging（"real-data scaling remains open"），但 Section 4.5 仍有 "rules out step-level data scarcity" 表述——不一致。
- **要求**：主文统一为 "augmentation-based scaling provides no improvement; real-data scaling (requiring ~1,350 pairs for 50 minority-class examples) remains open"。明确区分 step-level paraphrase diversity（ruled out）vs episode-level minority-class diversity（open）。

**C5. Capacity scaling confound 未控制 [Consensus]**
- 0.6B: 50.7%, 1.7B: 47.1%, 4B: 59.0% — non-monotonic。1.7B 用 8 seeds vs 0.6B/4B 用 4 seeds。
- "only 4B exceeds the baseline" 是 key claim 但基于 confounded comparison。1.7B 低于 0.6B 已不支持 "capacity matters" 的单调叙事。
- **要求**：相同配置重跑 OR 显式承认 "comparison is confounded, causal inference not supported" 并弱化结论。

### Should-Fix (Warning) — 7 条

**W1. Router "validates" 措辞过强 [Consensus]**
- 一个架构（Qwen3-1.7B）失败 ≠ 框架被 validated。缺失：task-type classifier router、death-risk predictor、real-data scaling。4B 趋势上升（+9pp）不支持 "disproportionate cost" 作为绝对判断。
- **建议**："validates" → "is consistent with" / "provides evidence that at current scales..."

**W2. "Environment-agnostic" overclaim [Consensus]**
- 框架要求 binary catastrophic outcome + deterministic paired episodes + meaningful modality。ALFWorld 已暴露 modality 定义从 computation mode 到 information access 的漂移。
- **建议**：弱化为 "applicable to environments with binary catastrophic outcomes and controllable modality comparison"。

**W3. Related work 遗漏 [Consensus]**
- 缺：AgentBench (Liu+ ICLR24)、LATS (Zhou+ ICML24)、Safe RLHF (Dai+ ICLR24)、ToolBench (Qin+ ICLR24)、SelfCheckGPT (Manakul+ EMNLP23)、NetHack (Küttler+ NeurIPS20)、Crafter (Hafner ICLR22)。
- "Hallucination → death" 是核心机制但无 hallucination detection 文献引用。

**W4. Bootstrap CI 需 cluster-level sensitivity [Consensus]**
- Episodes within same task type 共享结构（env dynamics, death risk profile），违反 i.i.d.。Cluster bootstrap（11 task-type clusters）CI 会更宽但更诚实。
- **建议**：报告 cluster bootstrap CI 作为 sensitivity analysis。

**W5. Cross-model 证据弱——仅覆盖 similar-capability 7-8B models [Consensus]**
- Llama-3.1-8B 复制仅证明 "another 7-8B model dies more in internal mode"——考虑 hallucination rate 本身高，不令人惊讶。
- **建议**：frame 为 "preliminary pilot"，将 70B 和 Reflexion 作为 explicit testable predictions。

**W6. MATH "consistent with prediction" 在 power=0.42 下 overclaimed [Consensus]**
- 42% power 的 non-significant result 与任何 prediction 都 consistent（包括 null）。不是 confirmatory evidence。
- **建议**："The MATH evaluation was inconclusive due to insufficient power (0.42); a definitive test requires N≈770."

**W7. Task selection survivorship bias / SCI [Consensus]**
- SCI=0.2147 "systematic phenomenon" 仅在 11 个已选 task types 上成立。63% exclusion 后，routing signal 集中在 37% task space。
- **建议**：弱化为 "systematic across all task types exhibiting routing signal"。

### Nice-to-Fix (Info) — 3 条

**M1. Modality 定义与实际 tool-use routing 的 gap 需讨论**
- Oracle state ≠ imperfect tools (code interpreter, API calls)。框架定位为 diagnostic（oracle as upper bound）是合理的，但需 1-2 段讨论 implications for practical tool-use design。

**M2. Title "the Dominant" 仅单环境验证**
- 建议 "a Dominant" 或保持但确保 scope 清晰。

**M3. 其他小问题**
- NetHack/Crafter 在 Conclusion 提到但未 cite
- Ethics Statement 未报 GPU 型号
- P=0 时 DAF CI 包含负数（ill-defined）——应注明 well-definedness 条件
- "Oracle degeneracy" 首次使用未定义
- Abstract 数字密集（5 百分比 + 3 p-value + CI），建议精简

---

## Reviewer Consensus

两位 Reviewer 在以下判断上完全一致 [AGREE]：
1. df=27 是统计错误，需立即修正
2. DAF=90.4% 的 headline 价值接近 tautological；78.9% 是更稳健的 empirical content
3. Cross-env evidence 无一 replicate death-dominance finding
4. Data scaling augmentation 不能 rule out real-data scarcity
5. Capacity scaling 的 non-monotonicity 使因果推断不可靠
6. 方法论框架本身（Algorithm 1 + 双指标设计）是 solid 的
7. Negative result（router fails）有 community diagnostic value
8. 统计报告透明度在 NLP 论文中属上乘
9. 论文处于 borderline / Findings track 水平
10. Bootstrap 需 cluster sensitivity；MATH claim overclaimed；cross-model 仅 direction-consistent

---

## Reviewer Divergence

| 问题 | R1 | R2 | Director 判定 |
|------|----|----|--------------|
| Modality 定义与 tool-use 脱节（R2-N3） | Partial REBUT: oracle is standard diagnostic methodology | Critical: readers expect practical routing implications | **Info**: oracle comparison 合理但需补 practical gap 讨论。降级为 M1 |
| Algorithm 1 隐含假设（R1-W4） | Should-Fix: both-dead 不区分 early/late death | Partial REBUT: paper already addresses in multiple locations | **Resolved in current version**: 35 both-dead episodes excluded from all analysis; integer scores justify exact comparison; impact limited |
| 论文定位（main vs Findings） | 2.5/5, "resubmit next cycle" | 3.0/5, "Findings track recommended" | 综合：**borderline**，修复 C1-C5 framing issues（无需新实验）可达 Findings weak accept；补充第二环境可达 main conference |

---

## Questions（需作者回应）

**Q1.** Partial correlation df=27 的来源？Task-level（df=8）还是 episode-level（df=242）？

**Q2.** 在 death-asymmetry 的 75 个 labels 中，有多少 episodes 即使未死也会产生相同 label（score comparison 一致）？这量化 death-asymmetry labeling 的 "redundancy"。

**Q3.** 如果用 task-type 作为 routing feature（one-hot），router 的 episode-level accuracy 是多少？这直接验证 "routing signal = task type" claim。

**Q4.** 1.7B 在 4-seed 配置下的 episode-level accuracy？这判断 non-monotonicity 是否是 artifact。

**Q5.** 为什么不在 NetHack/Crafter 中做 50-100 episodes 的 pilot replication？这是提升 generalization 证据力度最直接的路径。

**Q6.** Score-comparison labels（20 个）中，det vs int 分数差的中位数和分布？如果多数 <5 points，practical significance 需讨论。

**Q7.** 30-step budget 的选择依据？更大 budget 下 internal death rate 是收敛还是继续上升？

---

## Missing References

- **Liu et al. (2024)**. AgentBench: Evaluating LLMs as Agents. ICLR 2024.
- **Zhou et al. (2024)**. Language Agent Tree Search. ICML 2024.
- **Manakul et al. (2023)**. SelfCheckGPT: Zero-Resource Black-Box Hallucination Detection. EMNLP 2023.
- **Dai et al. (2024)**. Safe RLHF. ICLR 2024.
- **Qin et al. (2024)**. ToolBench. ICLR 2024.
- **Küttler et al. (2020)**. The NetHack Learning Environment. NeurIPS 2020.
- **Hafner (2022)**. Benchmarking the Spectrum of Agent Capabilities (Crafter). ICLR 2022.
- **Lakens (2017)**. Equivalence Tests. — 已 cite，确认 ✓
- **Ren et al. (2024)**. When to Trust Language Models: Safety and Reliability Survey.

---

## External Review (Stanford Agentic Reviewer)

外部审稿：未请求（项目配置中未检测到 `external_review.paperreview_ai.enabled: true`）。

---

## Overall Assessment

**评分**: borderline (2.75/5)
**置信度**: 4/5

| 维度 | R1 | R2 | 综合 |
|------|----|----|------|
| Soundness | 3.0 | 3.5 | 3.25 |
| Excitement / Novelty | 2.5 | 2.5 | 2.5 |
| Reproducibility | 3.5 | 4.0 | 3.75 |
| Overall | 2.5 | 3.0 | **2.75** |

**综合判断**：

方法论框架设计 solid（Algorithm 1 + 双指标），统计报告诚实（自我批判 r=0.97、报告 negative result），对社区有建设性。但存在 5 个 Critical 问题：

1. **df=27 统计错误**——可修复但暴露审校不足
2. **核心发现接近 tautological**——DAF 是 P 的数学函数非经验发现，contribution sizing for EMNLP main 存疑
3. **单环境证据**——title claims "the Dominant" 但仅 ScienceWorld 验证，cross-env checks 均非 replication
4. **Data scaling ablation 方法论缺陷**——augmentation ≠ real data, "structural limitation" 结论过强
5. **Capacity scaling confound**——seed 配置不一致使因果推断不可靠

这些问题中，C1/C4/C5 是 framing/reporting 修复（无需新实验），C2 需要 reframing contribution narrative，C3 最理想需要新实验数据（或降级定位）。

**可接收路径**：
- **Findings track (最小修改)**：修复 C1 统计错误 + C4/C5 claim 弱化 + C2 贡献重新定位为 "single-environment case study + framework proposal" + C3 title/contribution 收窄。纯 writing/framing 修改，无需新实验。
- **Main conference (需新数据)**：上述全部 + NetHack/Crafter pilot replication（50-100 episodes）+ 相同配置 capacity scaling 重跑。

当前论文处于 Findings track borderline 水平。相比 Round 9，论文在 framing（78.9% primary）、power analysis 报告、claim scoping 方面有明显改善，但核心 contribution sizing 问题（novelty + single-environment）未改变——这是结构性问题而非 writing 修复可解。

---

## Detailed Comments

### Abstract
- 数字密集，建议精简到 2-3 key numbers + insight statement
- "largely a mathematical consequence" qualifier 到位（R9 修复确认）
- 结尾 "routing problem reduces to safety-first modality selection" qualifier "in environments with catastrophic failure modes" 在位但 structurally 不够突出——reader fast-scanning 可能遗漏

### §3.4 (DAF Definition)
- "DAF should be interpreted relative to the environment's penalty magnitude" caveat 已存在 — good
- 建议补充：当 P → 0，DAF → 0 且 CI 包含负数（Table 8, P=0: [-36.7, 83.1]），说明 metric 仅在 P 显著时 well-defined

### §4.1 (Death Decomposition)
- df=27 需立即修正
- r=0.97 降级为 "internal consistency check" — good（R9 修复确认）
- partial r 的 "controlling for δ·P" 语义需澄清：在 task-level 这等于控制 δ（因 P 恒定），需解释

### §4.3 (MATH)
- Power analysis 添加 — good
- "consistent with framework prediction" 需降级为 "inconclusive"

### §4.5 (Router Diagnostic)
- "validates" → "is consistent with"
- "rules out step-level data scarcity" 需与 appendix hedging 统一
- Non-monotonicity 正文需 acknowledge（不仅 caption）

### Contribution List (Introduction)
- Contribution 2: "capacity-dependent limitation" 基于 confounded data，需加 caveat
- Contribution 3: "cross-context applicability" → "cross-context illustration" 或 "framework flexibility demonstration"

### Related Work
- 补充 hallucination detection 段落（SelfCheckGPT 等）——"hallucination → death" 是核心机制但未连接到 hallucination literature
- AgentBench/LATS 补充到 LLM Agent 段落
- Safe RLHF 补充到 Safe RL 段落