---
round: 2
overall_score: borderline accept - findings
timestamp: 2026-05-14T18:06:33.166559+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告 — Round 2

**论文**: Death Avoidance Dominates Routing Signal in LLM Agent Computation
**Venue**: EMNLP 2026 via ACL ARR May cycle — **Short Paper（4 页）**
**ARR 截止日期**: 2026-05-25（距今 11 天）
**审稿编排**: 2 名 Reviewer（R1: 方法严谨性+实验设计；R2: 新颖性+相关工作+写作）
**交叉回应**: 完成，13/13 issue 判定一致
**Round 变更**: Round 1 为 Main Conference 长文 (weak reject 2.25/5) → Round 2 转为 Short Paper

---

## Summary

论文提出 episode-level counterfactual analysis，分析 LLM agent 在 ScienceWorld 中 internal reasoning 与 deterministic computation 的 routing signal。245 episodes 跨 11 task types 显示 DAF = 90.41%——deterministic computation 的优势约 90% 来自避免 agent 死亡。Round 2 修订转为短文 track，新增独立 Limitations 节（含 MATH pilot 和 ALFWorld 跨环境证据）、Ethics Statement、95% CI、Labeling Quality Audit 和 Per-Task Decomposition appendix。Related Work 扩至 20 篇含 Concurrent Work 段。

---

## Round 1 → Round 2 修改评估

### RESOLVED（4 项）
| Issue | 说明 |
|-------|------|
| R1-N2 Limitations 格式 | 独立 `\section*{Limitations}` 已添加，含跨环境证据 |
| R1-W1 90%→95% CI | Table 1 现使用 95% Bootstrap CIs |
| R2-W3 Abstract 数字堆砌 | 精简至 ~3-4 核心数字，可读性显著改善 |
| R1-W6 Ethics Statement | 已添加，报告 ~40 GPU-hours、无人类参与、公开数据 |

### PARTIALLY_RESOLVED（5 项）
| Issue | 说明 |
|-------|------|
| R2-N1 DAF triviality | MATH/ALFWorld 跨环境证据提供定性支撑，但 penalty sensitivity analysis（post-hoc，成本极低）仍缺 |
| R1-N1 Scope 不匹配 | Abstract 增加 scope 限定，但标题未改——"in LLM Agent Computation" 仍暗示跨环境结论 |
| R2-N3 Related Work | 13→20 篇，Concurrent Work 段质量高。Safe RL 方向仍缺 |
| R1-W5 Label noise | Appendix A 回应了 oracle circularity，但非 step-level mislabeling |
| R1-W3 DAF near-zero | Appendix B 有 per-task 数据，实际无此问题，但 metric 定义层面讨论缺失 |

### STILL_OPEN（4 项）
| Issue | 说明 |
|-------|------|
| R1-N3 Train/test split | Appendix A 提到 "95 training labels" 但 test set 仍未描述。Table 1 Trained Router 分数来源不明 |
| R1-W2 Prescreening | Appendix B 列出 included 的 11 tasks，excluded 的 19 tasks 和 prescreening 标准仍不透明 |
| R1-W4 Death-aware baseline | 未出现。短文下降级为 nice-to-have |
| R2-W1 图表不足 | 主文 1 fig + 1 tab，短文下可接受 |

### 新发现问题（Round 2，4 项）
| Issue | Severity | 说明 |
|-------|----------|------|
| R2-NEW-1 ALFWorld 证据解读 | warning | Internal 3% success 可能是 agent 能力差异而非 catastrophic failure avoidance。ScienceWorld（42.9% 死亡率，agent 有基础能力）与 ALFWorld（3% success，agent 近乎无法工作）的机制不同 |
| R1-NEW-2 Conclusion 措辞偏强 | warning | "structural driver" 描述 preliminary evidence 不合适。建议改为 "suggestive of" |
| R1-NEW-4 页数合规性 | warning | 正文内容量可能超 4 页（§4.3 Router Training 4 段详细内容）。超页导致 desk rejection |
| R2-NEW-2 Orphan bib entry | info | dagger-2011 在 bib 中未被引用 |

---

## Strengths（延续 + 新增）

1. **研究问题有价值**：分析 routing 学到了什么，而非如何 route 更好。[R1, R2 共识，延续]
2. **Episode-level counterfactual 方法论**：解决 sparse-reward 下 per-step oracle 退化（97.4% tie rate）。[延续]
3. **统计证据扎实**：r = 0.9698，95% CI 报告规范。[延续，CI 改善]
4. **诚实报告 negative result**：router ≈ always-deterministic。[延续]
5. **Concurrent Work 定位好** [新增]：4 篇 2026 concurrent papers 讨论 tool overuse/tax/timing，论文提供了最具体的量化答案（~90% 来自 death avoidance），时效性价值高。
6. **Labeling Quality Audit** [新增]：Appendix A 系统性回应 oracle circularity concern，death-only retrain 57.3% ≈ full retrain 57.6%。
7. **跨环境初步证据** [新增]：MATH（无死亡→signal 消失）和 ALFWorld（catastrophic failure 模式类似）提供了方向性支撑，诚实放在 Limitations 节。

---

## Weaknesses

### 仍需解决的关键问题（3 个 Low-Cost Blockers）

**两位 Reviewer 一致认为：以下三项中完成任意两项即可达到 Findings 接收标准。**

**[Blocker 1] 标题加 scope 限定** [R1-N1, 低成本/高影响]
- 当前："Death Avoidance Dominates Routing Signal in LLM Agent Computation"
- 建议："...on ScienceWorld" 或 "...in a Sparse-Reward Science Environment"
- 短文 track 下标题 generality 与 4 页实验量的张力比长文更大

**[Blocker 2] Train/test 划分在正文中明确说明** [R1-N3, 低成本/必须]
- §4.3 或 Appendix 中需明确：95 个有标签 episodes 如何划分为 train/test，Table 1 Trained Router 分数来自哪些数据
- 这是基本实验设计合规性要求

**[Blocker 3] Penalty sensitivity post-hoc analysis** [R2-N1, 低成本/直接回应 triviality]
- 对已有 245 episodes 的 score 做 post-hoc recalculation：将 death episodes 的 -100 替换为 -50/-25/-10 重算 DAF
- 不需新实验，仅需数据处理
- 直接回应 "DAF ≈ δ·P/(δ·P+Δ_nd) 是 penalty 的数学函数" 的 triviality 论证

### 次要问题

- **Related Work**：Safe RL（García & Fernández 2015）引用仍缺——一句话即可建立 death avoidance = safety constraint 的理论连接
- **ALFWorld 证据解读**：3% internal success 的机制可能与 ScienceWorld（42.9% 死亡率）不同，Limitations 节应区分
- **Conclusion 措辞**："structural driver" 对 preliminary evidence 偏强
- **页数合规性**：正文可能超 4 页，§4.3 技术细节可压缩或移至 Appendix
- **Orphan bib entry**：dagger-2011 未被引用
- **Prescreening 标准**：19 个排除 task types 未列出（Appendix B 脚注说明即可）

---

## Reviewer Consensus

**完全共识**：13/13 issue 判定一致（R2 在交叉回应中修正了 R1-W5 的判定）。所有新发现问题双方 AGREE。3 个 low-cost blockers 完全一致。

## Reviewer Divergence

**评分差异 0.5 分**（R1=3.0 vs R2=2.5），源于：
1. **Excitement 权重**：R1 对 concurrent work 时效性和 negative result 实用价值给予更多权重（Excitement 3.0 vs R2 的 2.5）
2. **ALFWorld capability 混淆**：R2 认为 ALFWorld 3% success 是 agent 能力问题而非 routing signal，削弱跨环境 claim；R1 同意但未反映在评分中
3. **Penalty sensitivity 权重**：R2 更强调 cost-near-zero 但未做的分析影响 non-triviality 论证

R2 明确表示：3 个 blockers 中完成 2 个（特别是 penalty sensitivity + 标题），会提升到 3.0。

---

## Questions（需作者澄清）

1. Table 1 Trained Router 的 -10.70 分数是在训练集还是 held-out 集上计算的？数据划分策略是什么？
2. 已有 penalty sensitivity analysis 的数据吗？将 -100 替换为 -50/-25/-10 后 DAF 分别是多少？
3. 论文编译后正文是否在 4 页以内？
4. 97.4% vs Round 1 的 98.2% 是数据修正吗？原因是什么？
5. ALFWorld 中 internal 3% success rate——这是 agent 能力不足还是 catastrophic failure？与 ScienceWorld 42.9% 死亡率的机制差异如何解释？

---

## Missing References（缩减后）

短文框架下仅 1 个 critical 缺失方向：
- **Safe RL survey**：García & Fernández (2015) "A comprehensive survey on safe reinforcement learning"——一句话引用即可建立 death avoidance routing 与 safety constraint 的理论连接

---

## External Review (Stanford Agentic Reviewer)

外部审稿：未请求。

---

## Overall Assessment

**Overall Score: Borderline Accept — Findings (2.75/5)**

| 维度 | R1 R1 | R1 R2 | R2 R1 | R2 R2 | 合并 R2 |
|------|-------|-------|-------|-------|---------|
| Soundness | 3.0 | 3.0 | 3.0 | 3.0 | 3.0 |
| Excitement | 2.5 | 3.0 | 2.0 | 2.5 | 2.75 |
| Reproducibility | 3.0 | 3.5 | 3.0 | 3.0 | 3.25 |
| Overall | 2.5 | 3.0 | 2.0 | 2.5 | **2.75** |

**置信度**: 4/5

**判断理由**：

Round 2 修订显著改善了论文质量。Track 从长文转短文是明智的战略调整——单环境+单模型的实验量对短文可接受，降低了 scope 与 claim 的张力。格式问题全部解决（Limitations 节、Ethics Statement、95% CI）。Abstract 精简、Labeling Quality Audit、Per-Task Decomposition 增加了实验透明度。Concurrent Work 段展现了时效性价值。

论文从 Round 1 的 **Weak Reject (2.25)** 提升至 **Borderline Accept — Findings (2.75)**。

**距离 Findings 接收的 gap 清晰且低成本**：3 个 blockers 中完成 2 个即可——penalty sensitivity analysis（post-hoc recalculation，无需新实验）、标题加 scope 限定（改几个词）、train/test split 说明（加一段话）。这些修改的工程量以小时计，不涉及新实验或新数据。

**建议**：如果作者在 ARR 截止前（2026-05-25）完成上述修改，本文适合 EMNLP 2026 **Findings** track 投稿。核心方法论贡献（episode-level counterfactual in sparse-reward）和 actionable negative result（complex routing ≈ always-deterministic in death-dominated environments）对 Findings track 有充分价值。

---

## Detailed Comments

### Title
仍为 "Death Avoidance Dominates Routing Signal in LLM Agent Computation"。建议改为 "Death Avoidance Dominates Routing Signal Between Internal Reasoning and Deterministic Computation on ScienceWorld" 或更简洁的 "Death Avoidance as the Primary Routing Signal in a Sparse-Reward Agent Environment"。

### Abstract
大幅改善。Scope 限定有效（"with a Qwen2.5-7B-Instruct backbone"），数字精简得当。

### §1 Introduction
97.4% 替代了 Round 1 的 98.2%——应在修订说明中注明原因。其余结构不变，清晰有效。

### §2 Method
DAF 定义处 Δ_no_death → Δ_nd 符号简化合理。但 DAF 定义仍未讨论与 penalty magnitude 的解析关系。

### §3 Experiments
95% CI 改善了统计报告。但 §4.3 内容详实度可能导致超页——gradient accumulation 对比、cross-seed stability 等细节在短文中可移至 Appendix。**Train/test 划分是硬伤，必须修复。**

### §4 Related Work
Concurrent Work 段是本轮最有价值的新增内容。Safe RL 缺失仍是唯一实质性遗漏。

### §5 Conclusion
引用 Limitations 节数据（MATH/ALFWorld）需弱化措辞。"structural driver" → "suggestive of a general pattern"。

### Limitations
跨环境证据放在此处是诚实的选择。但 ALFWorld 的 3% internal success 需讨论 agent capability vs catastrophic failure avoidance 的区分。

### Appendix A (Labeling Quality Audit)
高质量补充。Zero tie-breaking labels + death-only retrain 一致性有效回应了 oracle circularity concern。

### Appendix B (Per-Task Decomposition)
有价值的透明度补充。但缺 prescreening 标准说明和被排除 task types 列表。
