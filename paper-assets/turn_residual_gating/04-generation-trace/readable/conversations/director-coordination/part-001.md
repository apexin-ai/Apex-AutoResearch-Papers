# Director coordination — Part 1 of 2

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Conversation logs

[Transcript overview](../director-coordination.md) · [Part 2 →](part-002.md) · [Structured JSON](../../../sessions/1a/1ad2ecd083aa9ebb6dd0.json)

## Round 1

## Round 1

16 recorded events


### User

_source line 1 · 2026-05-19T15:41:18.274621+00:00_

[Reviewer 2 审稿意见]:

# Reviewer 2 审稿报告：Novelty & Related Work

**论文**: "Why Lightweight Gating Cannot Fix Multi-Turn Attention Degradation: A Mechanistic Analysis"
**Venue**: EMNLP 2026 (via ACL Rolling Review)

---

## 总体评分

**Overall (ARR)**: 2.5 / 5 — Borderline Findings
**Overall (6-point)**: 3 / 6 — Weak Reject
**一句话总结**: 实验方法论尚可，但两个核心失败机制（梯度竞争 + exposure bias）均为已知现象在新场景的确认性验证，novelty 不足以支撑 main conference 或稳定的 Findings 接收。

---

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| **Soundness** | 3 / 5 | 实验设计合理（双模型、消融、bootstrap CI），但范围窄（仅标量门控）、GAR 单指标依赖、scheduled sampling p≈0.07 未达显著 |
| **Excitement** | 2 / 5 | 负面结果的解释力有限——确认已知失败模式而非揭示意外机制，可操作洞察匮乏 |
| **Reproducibility** | 3.5 / 5 | 报告了超参、种子、模型版本；但代码/数据未提供，且核心先行工作 Dongre et al. (2026) 不可查证 |
| **Reviewer Confidence** | 4 / 5 | 本人熟悉 exposure bias、multi-task optimization 和 transformer 机制分析文献 |

**Director 要求的子分数（6-point scale）：**
- **Novelty**: 2 / 6
- **Significance**: 2 / 6
- **Clarity**: 4 / 6

---

## Must-Fix 问题（影响接收决定）

### N1 [critical] Novelty 声称过高——两个核心机制均为已知现象的直接应用

- **具体位置**: §1 Abstract "first quantitative measurement"；§6.1 gradient competition；§6.4 exposure bias
- **问题**: 
  论文声称的两个 failure mechanism：
  1. **NTP-GAR 梯度竞争**（7–15× 幅度比）= 多任务梯度冲突（multi-task gradient conflict），这是 multi-task learning 领域 2018 年以来的经典问题。GradNorm (Chen et al., 2018) 定义了 gradient magnitude balancing，PCGrad (Yu et al., NeurIPS 2020) 定义了 gradient direction conflict 的 surgery 方法。论文将一个已有成熟解决方案的已知问题重新"发现"却完全不引用这些文献。
  2. **Teacher-forcing distribution shift** = exposure bias (Bengio et al., 2015)。论文自己在 §2 和 §6.4 中引用了 exposure bias 文献，却在 Abstract 和 contributions 中声称这是"first quantitative measurement"。Exposure bias 导致 auxiliary loss 在 teacher-forcing 下训练但 autoregressive 推理时失效，这在概念上是完全预期的。
  
  30× gap 的具体数值是新的，但数值本身不构成方法论贡献。这类似于报告"水在 100°C 沸腾"的精确温度——现象本身已知。

- **为什么影响接收**: ACL ARR 的 Excitement 维度要求论文提供 "new insights" 而非对已知现象的确认。如果审稿人认为核心发现是预期的（expected），论文难以超过 Findings 门槛。
- **建议修改方向**: (1) 在 §2 增加 multi-task gradient conflict 子节，引用 GradNorm/PCGrad/CAGrad 并解释为什么这些已知方法不能直接解决本文场景；(2) 将 contribution 从"first measurement"重新定位为"first empirical demonstration in the attention-steering context with quantitative characterization"；(3) 补充实验：用 PCGrad 或 GradNorm 缓解梯度竞争，观察是否能减小 30× gap——如果能，说明问题有已知解；如果不能，这才是真正的新洞察。

### N2 [critical] 标题 "Cannot" 过度声称——证据仅支持 "fails to" under tested conditions

- **具体位置**: 标题；§7 Discussion "our findings are specific to lightweight residual gating with auxiliary GAR losses"
- **问题**: 
  标题使用 "Cannot"（不可能），但论文仅测试了：
  - 一种门控架构（标量 per-layer gate via ReZero）
  - 一种辅助目标（GAR loss）
  - 一种训练方式（joint NTP+GAR）
  - 两个模型家族（Qwen-2.5-7B, Llama-3.1-8B）
  
  §7 Discussion 自己承认 "our findings are specific to lightweight residual gating with auxiliary GAR losses"，这与标题的绝对否定矛盾。更关键的是，scheduled sampling 将 gap 从 30× 降至 12.3×（§7），说明改变训练策略就能部分修复——这直接反驳了 "cannot"。
  
  未测试的替代方案包括：向量门控（vector gate per dimension）、attention-head-specific gate、不同 loss 权重调度、curriculum learning 等。

- **为什么影响接收**: 审稿人最厌恶的是 overclaiming。标题是论文最高频被阅读的部分，overclaim 会直接降低可信度。
- **建议修改方向**: 改为 "Why Lightweight Scalar Gating Fails to Fix Multi-Turn Attention Degradation" 或 "How Exposure Bias Undermines Gating-Based Attention Steering"。

### N3 [critical] 核心先行工作 Dongre et al. (2026) 不可查证

- **具体位置**: 全文核心依赖——§1 motivation, §3 GAR 定义, §5.1 baseline
- **问题**: 
  论文的整个动机链建立在 Dongre et al. (2026) 之上：GAR 指标定义、multi-turn degradation 的量化、residual stream persistence 发现。引用验证显示该文献在 OpenAlex 中完全不可查（similarity score 仅 0.336）。Bib 条目标注为 "Proceedings of NAACL 2026"，但无法验证该论文是否已被接收或发表。
  
  如果这篇论文不存在或无法获取，则本文的整个实验框架（GAR 指标、probe AUC baseline、"27–48% drop" 数据）均缺乏可验证的基础。

- **为什么影响接收**: ARR reviewer guidelines 要求 soundness 评估包括 claims 的 supporting evidence。如果核心 prior work 不可验证，所有基于其上的 claim 均悬空。
- **建议修改方向**: 如果 Dongre et al. 尚未发表，需要 (1) 在论文中自包含地重新定义 GAR 并提供独立验证，(2) 明确标注为 "under review" 或提供 preprint 链接。

### N4 [critical] Related Work 缺失关键文献：Multi-task Gradient Conflict

- **具体位置**: §2 Related Work（整节未提及 multi-task optimization 文献）
- **问题**: 
  §6.1 的核心发现是 NTP 和 GAR 梯度存在方向冲突和幅度不平衡。这正是 multi-task gradient conflict 的定义。但 §2 完全未讨论以下直接相关文献：
  - **GradNorm** (Chen et al., ICML 2018): 动态调整 loss 权重以平衡梯度幅度
  - **PCGrad** (Yu et al., NeurIPS 2020): 投影消除梯度方向冲突
  - **CAGrad** (Liu et al., NeurIPS 2021): 冲突感知梯度下降
  - **Nash-MTL** (Navon et al., ICML 2022): 纳什博弈框架下的多任务优化
  
  这些方法为梯度竞争提供了成熟的解决方案。论文不讨论这些方法，既削弱了 related work 的完整性，也错失了重要的实验 baseline——如果 PCGrad 能解决梯度竞争问题，则本文的"失败"可能仅仅是因为没有使用正确的优化策略，而非 gating 本身的固有局限。

- **为什么影响接收**: Related work 不完整直接影响 Soundness 评分。审稿人会问："你说梯度竞争导致失败，但你试过已知的梯度冲突解决方案吗？"
- **建议修改方向**: (1) §2 增加 multi-task gradient conflict 子节；(2) 实验中加入至少一种 gradient surgery baseline（如 PCGrad）并报告结果。

---

## Should-Fix 问题（影响评分但不一票否决）

### W1 [warning] 范围过窄——仅标量门控，不足以支撑 "lightweight gating" 的一般性结论

- **具体位置**: §4.1 ThreadGate Architecture; 标题中 "Lightweight Gating"
- **问题**: 标题说 "Lightweight Gating"（轻量门控），但实际仅测试了最简单的标量 per-layer gate（Eq. 2, ReZero 风格）。"Lightweight gating" 的合理范围至少应包括：(a) vector gate (per-dimension)，(b) attention-head-specific gate，(c) low-rank gate，(d) layer-group gate。仅测试一种变体就声称"轻量门控不行"，有以偏概全之嫌。
- **建议**: 至少讨论其他变体为什么未测试，或补充 1-2 种变体的实验。

### W2 [warning] Scheduled sampling 实验统计不显著（p ≈ 0.07）

- **具体位置**: §7 Discussion; Table 7
- **问题**: Contribution 4 声称 "suggestive evidence from scheduled-sampling mitigation (gap 30×→12.3×, p≈0.07)"。p=0.07 在传统统计标准下不显著（α=0.05），论文用 "suggestive" 对冲但仍将其列为正式 contribution。Table 7 显示 SS+TG 的 inference GAR 仅从 0.016 提升到 0.019p，这个绝对提升量极小。
- **建议**: 要么增加 bootstrap 样本量/实验重复以获得更强统计支持，要么将此发现从 contributions 降级为 discussion 中的初步观察。

### W3 [warning] GAR 作为唯一注意力退化指标的局限性未充分讨论

- **具体位置**: §3 Background; §5.5 Statistical Validation
- **问题**: 整篇论文的所有实验结论都建立在 GAR（Goal Attention Ratio）这一单一指标上。§6.5 虽然报告了 instruction compliance 作为下游验证（r=0.82 Pearson correlation），但这是事后验证而非独立指标。如果 GAR 本身的定义有问题（例如，goal token 的选择方式、position bias 的影响），所有结论都会受影响。论文未讨论 GAR 的 limitations 或与其他注意力质量指标的对比。
- **建议**: 讨论 GAR 可能的失效场景；如果可能，增加至少一个替代指标（如 attention entropy over goal tokens, goal-relevant hidden state similarity）。

### W4 [warning] 论文长度明显低于 EMNLP long paper 上限

- **具体位置**: 全文结构
- **问题**: EMNLP 2026 long paper 限 8 页正文。本文正文约 6 页（§1-§8 Conclusion 在第 6 页结束），远低于上限。这意味着有约 2 页空间可以补充缺失的 related work、更多门控变体实验、gradient surgery baseline 等。未充分利用页面预算会让审稿人认为 contribution 不够充实。
- **建议**: 利用剩余页面预算充实 related work 和实验。

### W5 [warning] liu2016attention 引用可能错配

- **具体位置**: §2 Related Work "attention supervision (Liu et al., 2016)"
- **问题**: Bib 条目 `liu2016attention` 的标题是 "Attention-Based Models for Speech Recognition"（语音识别），但在 §2 中被引用为 "attention supervision" 方法（transformer 注意力引导）。引用验证显示 first author 不匹配（bib=Liu, API=Chorowski）。这可能是引用错配——语音识别的注意力模型与多轮对话的注意力引导是不同话题。
- **建议**: 核实此引用是否指向正确论文；如果讨论的是 attention supervision for NMT/dialogue，应替换为更相关的参考文献。

### W6 [warning] 4 个 orphan bib 条目未被引用

- **具体位置**: References section
- **问题**: 引用验证发现以下 bib 条目存在但未在正文中引用：`vaswani2017attention`（Attention is All You Need）、`elhage2021mathematical`（Transformer Circuits）、`olsson2022context`（Induction Heads）、`efron1994bootstrap`（Bootstrap 统计）。其中 Vaswani (2017) 作为 transformer 基础论文理应被引用；Elhage (2021) 和 Olsson (2022) 对理解 residual stream 机制直接相关。这些遗漏暗示引用管理不完善。
- **建议**: 清理 bib 文件，移除未引用条目或在正文中引用它们。

---

## 小问题（不影响接收）

- §1 p.1 "probe AUC up to 0.98" — AUC 基线和计算方法应在正文简述（目前仅引用 Dongre et al.），方便不了解该先行工作的读者理解。
- §4.2 Loss Design：v7 loss 的选择过程（"We explored seven loss configurations (v1–v7)"）仅一句带过，读者无法理解为什么 v7 最优。建议至少在 Appendix 提供 v1–v6 的简要描述和性能。
- Table 1: "Relative drop" 行的 70.8% 和 69% 是相对于 Turn 1 计算的，但表头未明确标注基线。
- §5.5 Table 5: bootstrap CI 包含零 ([-0.012, 0.019] 和 [-0.008, 0.019])，正文说"statistically indistinguishable from zero"——这支持了 null result 但应更明确地说明这意味着 ThreadGate 的增量效果可能完全不存在。
- p.1 Abstract: "30× training–inference gap" 的表述有歧义——是 GAR 值的比值（0.48/0.016=30）还是相对退化幅度？应更精确定义。

---

## 主要优势

1. **实验设计的方法论规范性**: 双模型验证（Qwen + Llama），4-way 消融设计将 gating / LoRA / loss 解耦，bootstrap CI 提供统计保障。这比许多 negative result 论文更严格。
2. **清晰的叙事结构**: 从问题定义（§1-3）→ 方法设计（§4）→ 负面结果（§5）→ 机制分析（§6）→ 缓解探索（§7）的逻辑链条连贯。
3. **诚实的 hedging**: §7 Discussion 承认结果的范围限制，Contribution 4 用 "suggestive evidence" 而非断言。这种学术诚实值得肯定。
4. **Per-layer gradient 分析的粒度**: Table 6 的逐层梯度统计（conflict fraction、magnitude ratio）提供了比纯总体数字更丰富的分析。

---

## 对 Director 指定问题的逐项回答

### Q1: Novelty Assessment

**负面结果是否 genuinely novel and surprising?** 不够。对于熟悉 exposure bias 和 multi-task gradient conflict 文献的研究者，"在 teacher-forcing 下训练的 auxiliary attention loss 在 autoregressive inference 时失效" 是可预期的。30× 的具体幅度是新的，但量化一个预期现象不等于新洞察。

**机制解释是否 new insights?** 更多是 restatements。梯度竞争 = multi-task gradient conflict (GradNorm/PCGrad 文献)；distribution shift = exposure bias (Bengio et al., 2015)。论文的贡献在于将这两个已知现象映射到 attention steering 场景并提供具体数值，但解释框架本身不新。

**30× gap 的意义**: 作为一个具体 benchmark 数字有参考价值，但不足以单独构成一个 contribution。

### Q2: Related Work Completeness

**关键缺失**: Multi-task gradient conflict 文献（GradNorm, PCGrad, CAGrad, Nash-MTL）——这是本文 §6.1 核心机制的直接上位文献，完全缺失是重大遗漏。

**与 Dongre et al. 的定位**: 论文在 §1 和 §7 对 Dongre et al. 的定位清晰——"他们发现了问题和 residual 信息持久性，我们测试能否通过 gating 利用这种持久性"。但 §7 提到 Dongre et al. 的 Appendix B 已注意到 goal re-injection 的失败，论文应更明确地区分自己的增量贡献。

**缺失的替代方案讨论**: 
- Inference-time intervention (ITI, Li et al., 2024) 和 representation engineering (Zou et al., 2023) 在 §2 被引用但仅一句带过。这些方法在推理时直接操作 hidden states，避开了 exposure bias，是更有希望的方向。论文应深入讨论为什么这些方法可能更适合，以增强自身的"轻量训练时方法不行"的论点。

### Q3: Contribution Significance for Top Venues

**对于 acceptance rate ~25% 的顶会**: 不足。负面结果论文的门槛是 (1) 尝试的方法必须合理且被广泛期望能成功，(2) 失败分析必须提供深层、可操作的洞察，(3) 发现必须泛化到被测试的具体设置之外。本文在 (1) 上勉强通过（residual gating 确实是 reasonable hypothesis），但在 (2) 上不达标（洞察归结为已知的 exposure bias + gradient conflict），在 (3) 上也不达标（仅测试标量门控）。

**对于 Findings track**: Borderline。如果补充 multi-task gradient conflict 的讨论和实验（如 PCGrad baseline），并修正标题为 "fails to"，质量可能达到 Findings 门槛。

**范围是否过窄**: 是。"Lightweight gating" 涵盖多种架构，但仅测试最简单的标量变体。如果向量门控或 head-specific 门控也失败，结论的说服力会大幅增强。

### Q4: Writing Quality

**叙事连贯性**: 好。故事线清晰：问题→假设→验证→失败→分析→缓解。
**组织**: 好。§ 编排合理。
**Hedging 与 overclaiming**: §7 Discussion 的 hedging 诚实，但标题 "Cannot" 和 Abstract 的 "first quantitative measurement" 与正文的谦逊不一致。标题和 abstract 是最高频阅读部分，它们的 overclaim 伤害大于正文 hedging 的补救。

**引用状态**: ⚠️ 注意——Director 指出 "ALL citations are broken (appear as '?')"，但我在渲染的 PDF（best version, dream_20260519T145320）中观察到引用均正常渲染（如 p.1 "Dongre et al. (2026)"、p.2 "(Zheng et al., 2024)" 等均可读）。References 节格式完整。可能 Director 看到的是不同版本。如果提交版本确实有引用全坏的问题，那是 desk reject 级别的格式缺陷。

### Q5: Framing Assessment

**"Cannot" vs "Struggles to" vs "Fails to"**: 
- "Cannot" = 声称不可能 → **过度声称**，证据不支持
- "Struggles to" = 声称困难 → 相对合适，但对 30× gap 来说又有些轻描淡写
- "Fails to" = 声称在测试条件下失败 → **最准确**的表述

推荐标题改为: "Why Lightweight Scalar Gating Fails to Fix Multi-Turn Attention Degradation: A Mechanistic Analysis"

**Setup-specific vs. generalizable**: §7 Limitations 做了合理区分。但标题和 Abstract 的用语暗示一般性结论（"Lightweight Gating" 而非 "Scalar Residual Gating"），与正文的谨慎不一致。

### Q6: Missing Perspectives

**未考虑的替代解释**:
1. **GAR 指标本身的局限**: GAR 衡量 attention mass 在 goal tokens 上的分布，但 attention ≠ information flow。模型可能通过 value vectors 而非 attention weights 传递 goal 信息。attention weight 上的 GAR 衰减不一定意味着功能性退化。
2. **标量门控容量不足**: 每层一个标量参数可能simply too few parameters 来学习复杂的 turn-conditioned 行为。失败可能不是 exposure bias，而是容量不足。
3. **LoRA rank 的交互效应**: §4.3 用 LoRA rank 16 应用到所有 attention projection matrices。不同 rank 选择可能改变梯度竞争的动态。
4. **训练数据量**: 仅 1,000 对话可能不足以让 gate 学习稳健的模式。

**应讨论的 positive-result approaches**:
- **ITI (Li et al., 2024)** 和 **RepE (Zou et al., 2023)**: 推理时干预方法，绕过 exposure bias
- **Activation patching**: 直接在特定层修改激活值
- **KV-cache manipulation**: 在推理时对 key-value cache 做选择性操作
- 这些方法的成功案例与本文的失败案例形成对比，能更好地定位本文贡献

---

## 总结

论文的实验执行和叙事结构达到了出版标准，但 novelty 是致命短板：两个核心机制（gradient conflict + exposure bias）是成熟的已知问题，且论文遗漏了直接相关的 multi-task optimization 文献。标题 "Cannot" overclaims，而核心依赖的 Dongre et al. (2026) 无法查证。建议 (1) 补充 gradient surgery baseline 实验，(2) 扩展门控变体范围，(3) 修正标题和 contribution 声称，(4) 解决 Dongre et al. 的可查证性问题后重新提交。当前状态下评为 Borderline Findings (ARR 2.5)。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 2 · 2026-05-19T15:41:30.302618+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status",
    "max_results": "3"
  }
}
```

</details>

---


### Tool result

_source line 3 · 2026-05-19T15:41:30.353272+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 4 · 2026-05-19T15:41:33.133325+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "turn_residual_gating"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "turn_residual_gating"
  }
}
```

</details>

---


### Tool result

_source line 5 · 2026-05-19T15:41:33.590293+00:00_

{"result":"# 项目 turn_residual_gating 概况\n\n## 实验状态 (16 个)\n\n- **analysis_gradient_conflict**: DONE (success) — \n- **phase2_tg_s42_v8_schedsampling**: PREPARING — \n- **phase2_4way_eval_heldout**: DONE (success) — \n- **phase2_4way_eval**: DONE (negative) — \n- **phase2_lora_only_s42**: DONE (success) — \n- **phase2_ug_s42**: DONE (success) — \n- **phase2_tg_s42_v7**: DONE (success) — \n- **phase2_tg_s42_v6**: DONE (negative) — \n- **phase2_tg_s42_v5**: DONE (negative) — \n- **phase2_tg_s42_v4**: DONE (failed) — \n- **phase2_tg_s42_v3b**: DONE (success) — \n- **phase2_tg_s42_v3**: DONE (negative) — \n- **phase2_tg_s42_v2**: DONE (killed) — \n- **phase2_tg_s42**: DONE (negative) — \n- **phase1_gar_diag**: DONE (success) — \n\n## 最新报告\n# Handover — 2026-05-19\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n- phase2_tg_s42_v8_schedsampling: Scheduled sampling 应用到 GAR loss（线性从 0→0.5 混合 teacher-forced + model-generated contexts）能缩小 v7 的 30x training-inference GAR gap。机制：在 model-generated context 上计算 GAR loss 迫使 attention pattern 适应推理时分布，直接 address teacher-forcing distribution shift。成功标准：inference GAR 显著高于 v7 的 0.016，PPL 不显著恶化（≤2.78+0.2）。（准备中）\n\n## 近期结论\n- **analysis_attention_heatmap** (success): 四模型（Base/TG/UG/LoRA-only）的 goal attention 衰减模式是否一致？如果 TG 的 attention decay 与 LoRA-only 无差异，则 gating 机制对 attention 分布零增量。 ← 基于 phase2_tg_s42_v7\n- **analysis_gradient_conflict** (success): NTP-GAR 梯度冲突在 v7 训练过程中是否逐层普遍存在？量化 cos_sim 和 magnitude ratio 的演化，验证 NTP 是否在训练中逐渐完全压制 GAR 信号。 ← 基于 phase2_tg_s42_v7\n- **phase2_4way_eval_heldout** (success): 四路消融的三路趋同结论（TG≈UG≈LoRA-only，gating 零增量）在 held-out eval 数据（idx≥8000，与训练集无重叠）上复现，排除数据重叠 confound。预期：相对比较保持（三路趋同），绝对 GAR 值可能变化。 ← 基于 phase2_4way_eval\n\n## 趋势\n成功 8 / 负向 5 / 失败 1 / 共 15\n\n## 下一步\n（无活跃 idea，请通过 ideas.md 添加）\n\n## 资源状态\nwestd-20861: 无 GPU 信息\n\n## 告警\n- phase2_tg_s42_v2: 已被终止 — unknown\n- phase2_tg_s42_v4: 训练失败 — unknown"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 456
}
```

</details>

---


### Tool call

_source line 6 · 2026-05-19T15:41:33.590724+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "turn_residual_gating"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "turn_residual_gating"
  }
}
```

</details>

---


### Tool result

_source line 7 · 2026-05-19T15:41:33.641183+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 8 · 2026-05-19T15:41:33.641550+00:00_

called mcp__agent-ml-research__get_visual_check_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_visual_check_status</summary>

```json
{
  "project": "turn_residual_gating"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "tool_args": {
    "project": "turn_residual_gating"
  }
}
```

</details>

---


### Tool result

_source line 9 · 2026-05-19T15:41:33.742458+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 10 · 2026-05-19T15:41:43.215756+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_project_file",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_project_file",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 11 · 2026-05-19T15:41:43.266378+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 12 · 2026-05-19T15:41:47.433311+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/review_reports/**",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/review_reports/**",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating"
  }
}
```

</details>

---


### Tool result

_source line 13 · 2026-05-19T15:41:47.885454+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "Glob",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 14 · 2026-05-19T15:41:47.986163+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/review_issues.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/review_issues.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating"
  }
}
```

</details>

---


### Tool result

_source line 15 · 2026-05-19T15:41:48.036940+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Assistant

_source line 16 · 2026-05-19T15:42:27.857236+00:00_

已收到 Reviewer 2 (Novelty & Related Work 方向) 的 Round 1 审稿报告。

**R2 核心发现摘要：**
- **Overall**: ARR 2.5 / 5（Borderline Findings）
- **4 个 Critical 问题**：
  - N1: 两个核心机制（gradient conflict + exposure bias）均为已知现象，novelty 声称过高
  - N2: 标题 "Cannot" 过度声称，证据仅支持 "Fails to"
  - N3: 核心先行工作 Dongre et al. (2026) 不可查证
  - N4: Related Work 完全缺失 multi-task gradient conflict 文献（GradNorm/PCGrad/CAGrad）
- **6 个 Warning**：范围过窄（仅标量门控）、scheduled sampling 统计不显著、GAR 单指标依赖、论文长度偏短、引用错配、orphan bib 条目

R2 的审查角度和深度符合预期，特别是在 multi-task optimization 文献缺失这一点上的发现非常关键。

**当前状态**：等待 Reviewer 1（方法/实验方向）的 Round 1 报告返回。两位 Reviewer 均提交后，进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director"
}
```

</details>

---


## Round 2

## Round 2

30 recorded events


### User

_source line 17 · 2026-05-19T15:42:28.956904+00:00_

[Reviewer 1 审稿意见]:

# Reviewer 1 审稿报告：Methods & Experiments

**论文**: "Why Lightweight Gating Cannot Fix Multi-Turn Attention Degradation: A Mechanistic Analysis"
**审稿侧重**: 方法设计、实验设计、统计严谨性、可复现性、消融完整性

---

## 总体评分

**Overall Assessment**: 3.0 / 5（Findings acceptance）
**一句话总结**: 有价值的负面结果论文，机制分析思路清晰，但单种子+小样本+关键消融缺失使核心 claim 的支撑不够牢靠，引用全部失效是投稿级硬伤。

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| **Soundness** | 3/5 (Acceptable) | 两个模型上的训练-推理 GAR gap 和梯度冲突证据互相印证，scheduled sampling 实验提供因果方向。但单种子、50 样本评估、缺少 λ 敏感性消融使结论泛化性存疑。 |
| **Excitement** | 3/5 (Interesting) | 负面结果+机制归因对社区有参考价值（"为什么不行"比"不行"更有信息量）。但范围窄（仅标量门控、两个 7-8B 模型），对后续工作的指导停留在定性层面。 |
| **Reproducibility** | 2/5 | λ_GAR、λ_div、λ_MSE 具体数值未报告；batch size、优化器、学习率调度未说明；v1-v6 loss 细节缺失；UltraChat 子集选择标准未交代。 |
| **Confidence** | 4/5 | 实验方法论在我的专业领域内，对论文进行了仔细审读。 |

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] 所有引用均渲染为 "?"——bibliography 编译失败
- 具体位置：全文所有 \citep/\citet 命令（共 37 处）
- 问题：PDF 中每一处引用都显示为 "?" 而非作者名，说明 bibtex/biber 未正确编译。这使得审稿人无法验证任何基于先行工作的 claim。
- 引用审计结果：24 条 bib 条目中，3 条在 OpenAlex 上未找到（dongre2026——论文的核心基础参考、zou2023representation、elhage2021mathematical），5 条存在作者或年份不匹配（xiao2024efficient, vaswani2017attention, liu2016attention, yang2024qwen2, dubey2024llama3），4 条定义在 .bib 但从未被引用（orphan entries）。
- 为什么影响接收：这是投稿级基本合规问题，ARR 审稿明确要求可验证的引用。即使编译修复后，核心参考 dongre2026（GAR 指标的来源）在 OpenAlex 上无法查到，需要确认该文确实存在且已公开。
- 建议修改方向：修复 bibtex 编译流程；确认 dongre2026 的可验证性（如提供 arXiv/会议 URL）；清理 5 处作者/年份不一致。

**N2** [critical] 单种子实验支撑 "Cannot" 级别的强断言
- 具体位置：标题 "Cannot Fix"；Abstract "fails to transfer"；Section 5.2 全部数据
- 问题：所有实验均使用 seed=42 单次运行。论文标题使用 "Cannot"（绝对否定），但实验证据只来自单次随机初始化。30× 训练-推理 gap 在不同 seed 下是否稳定？Gate 初始化对 gradient conflict 的影响未探索。负面结果论文的证据标准应**高于**正面结果——因为 claim 是 "这个方法不可能 work"，需要排除 seed 偶然性。
- 为什么影响接收：如果在 seed=7 下 gap 只有 5×，核心结论就不成立。单种子无法排除这种可能性。
- 建议修改方向：（1）至少 3 个 seed，报告 mean±std；（2）或将标题改为 "Struggles to" / "Often Fails to"，弱化 claim 与证据强度匹配。

**N3** [critical] 评估样本量过小（50 conversations）且统计功效存疑
- 具体位置：Section 5.5, Table 5 (bootstrap CI)
- 问题：50 conversations 用于计算所有 GAR 指标和 bootstrap CI。虽然 10K bootstrap resamples 可以估算 50 个样本内的抽样分布，但无法弥补 50 本身偏小的问题——bootstrap 估计的是你手中数据的不确定性，不是总体的代表性。Cohen's d ≈ 0.22 是小效应量，在 n=50 下 power 不足以检测出真实的中等效应。且 scheduled sampling 结果 p≈0.07（Section 6.4, Table 7）被论文用作因果证据，但 α=0.05 下并不显著。
- 为什么影响接收：核心 claim 的统计基础不够坚实。审稿人会质疑 "零增益" 是真正的零还是 underpowered 的假阴性。
- 建议修改方向：（1）增加评估样本到 200-500 conversations；（2）进行 power analysis 说明 50 是否足够检测目标效应量；（3）scheduled sampling p≈0.07 需要明确标注为 "marginally significant" 或 "not significant at α=0.05"。

**N4** [critical] 损失函数超参数和组件定义缺失——无法复现
- 具体位置：Section 4.2, Eq. 3
- 问题：Eq. 3 定义 L = L_NTP + λ_GAR·L_GAR + λ_div·L_div + ...，但 λ_GAR、λ_div 的具体数值从未在正文或附录中给出。L_div "encourages diversity across layer-wise gate values to prevent collapse" 只有一句话描述，没有数学定义。此外，论文提到探索了 v1-v7 共 7 个 loss 配置，但仅描述 v7，v1-v6 完全没有细节。这使得：（a）其他研究者无法复现 v7 训练；（b）无法判断 v1-v6 的失败是设计问题还是超参问题。
- 为什么影响接收：对于一篇声称某方法 "不可行" 的论文，读者需要确信作者已经做了充分的努力。隐藏了 6 个失败变体的细节和关键超参数，损害了这种信任。
- 建议修改方向：（1）在 appendix 中列出所有 7 个 loss 变体的数学定义和训练结果；（2）正文报告 λ_GAR、λ_div 的具体值和选择理由；（3）增加 λ_GAR 敏感性实验。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] Llama 上未测试 Uniform Gate——跨模型验证不完整
- 具体位置：Table 3（Llama 3-way eval）vs Table 2（Qwen 4-way eval）
- 问题：Qwen 有 4 组对照（Base/LoRA-only/ThreadGate/Uniform Gate），Llama 只有 3 组（无 Uniform Gate）。Uniform Gate 是排除 "per-layer specialization 是否有价值" 的关键对照。缺少这一组，Llama 上无法确认学习到的门控是否优于均匀门控。
- 建议：在 Llama 上补充 Uniform Gate 实验，或解释为何省略。

**W2** [warning] 无 λ_GAR 敏感性消融
- 具体位置：Section 4.2
- 问题：论文仅测试一个 λ_GAR 值。梯度冲突（NTP 7-15× dominance）的严重程度直接取决于 λ_GAR 的大小。如果 λ_GAR 增大 10 倍使 NTP:GAR magnitude ratio 降到 ~1×，gate 行为可能完全不同。仅一个 λ_GAR 值不能支撑 "lightweight gating 本质上不行" 的结论。
- 建议：测试 λ_GAR ∈ {0.1, 0.5, 1.0, 5.0} 的 grid，观察 gradient ratio 和 inference GAR 的变化趋势。

**W3** [warning] 训练数据量（1,000 conversations）可能是混淆变量
- 具体位置：Section 4.3
- 问题：1,000 conversations 对于 LoRA fine-tuning 一个 7B 模型来说非常少。论文的核心发现是 "训练有效但推理不 transfer"，但这也可能是数据不足导致 gate 没有学到足够 robust 的模式。论文的 Limitations 未讨论这一点。
- 建议：（1）增加数据量到 5K-10K conversations 看趋势变化，或（2）在 Discussion 中明确讨论为何 1,000 足够排除数据不足假说。

**W4** [warning] 缺少可视化——论文关于注意力退化却没有注意力热力图
- 具体位置：Section 6.3（提到 "attention heatmaps are visually indistinguishable"）, Table 7
- 问题：论文核心主题是 multi-turn attention degradation，但全文没有一张 figure。Section 6.3 声称 "The four models' attention heatmaps are visually indistinguishable at inference time" 但只提供 Table 7 的数字摘要，未展示实际热力图让读者自行判断。训练曲线（描述了 3 个 phase 的训练动态）也只有文字描述（Appendix A），没有可视化。
- 建议：至少加入（1）attention heatmap 对比图（Base vs ThreadGate, training vs inference）；（2）GAR 训练曲线（含 3 phase 标注）；（3）gate value 分布图。

**W5** [warning] Scheduled sampling 因果推断的局限性未充分讨论
- 具体位置：Section 6.4, Table 7
- 问题：SS 实验只测试了一个 SS ratio (50%)。剩余 4.3× gap 被归因于 "gradient competition"，但这是排除法推理，没有直接证据。p≈0.07 在严格标准下不显著。此外，SS 对 NTP 性能的影响（PPL 变化）未报告——如果 SS 显著损害了 NTP quality，那 gap 缩小可能只是因为模型整体退化。
- 建议：（1）测试 SS ratio ∈ {25%, 50%, 75%, 100%}；（2）报告 SS 对 PPL 的影响；（3）p≈0.07 需在正文中明确标注为 "does not reach statistical significance at α=0.05"。

**W6** [warning] "Reverse turn conditioning"（Section 6.2）的证据是间接的
- 具体位置：Section 6.2
- 问题：论文声称 gate 学会在早期 turn（GAR 自然高）抑制 sublayer output、在晚期 turn（GAR 低，需要干预）变得 passive——这是一个有趣的发现。但证据仅为：（1）gate mean close to 1.0 (93-98%)，attenuation 仅 2-7%；（2）27/28 layers 在 Qwen 上显示负的 gate difference（turn 1 vs last turn）。在 2-7% 的 attenuation 范围内，这些 "差异" 可能只是数值噪声。没有对 gate difference 做显著性检验。
- 建议：对 per-layer gate difference 进行 paired test（across conversations），报告 effect size。

---

## 小问题（不影响接收）

1. **标题与 Director 描述不一致**: 论文 PDF 标题为 "Cannot Fix"，Director 提供的标题为 "Struggles to Fix"。需确认正式版本。
2. **Appendix Table 编号**: Appendix B 的表格编号可能与正文冲突（主文 Table 5 是 bootstrap CI vs Appendix 也有类似编号的 instruction compliance 表）。需检查整篇论文的表格编号连续性。
3. **4 条孤立 bib 条目**: efron1994bootstrap（bootstrap 经典教科书）、elhage2021mathematical、olsson2022context、vaswani2017attention 在 .bib 中定义但未在正文中引用。应清理或引用。
4. **无 Limitations section 独立标题**: 论文的局限性讨论嵌入 Section 7 (Discussion) 内，没有作为独立 section。ACL venues 通常期望明确的 Limitations section（虽然已有 mandatory limitations 不计入页数的规定）。
5. **Eq. 1 GAR 定义**中的符号：$\mathcal{G}$ 代表 goal token positions 的集合，但论文未明确说明 goal token 的标注方式（是手动还是自动？是用 position matching 还是语义匹配？）。

---

## 主要优势

1. **有价值的负面结果**：社区需要知道 "训练时优化 GAR 不等于推理时 GAR 提升" 这一事实。两个失败机制（NTP 梯度主导 + teacher-forcing 分布偏移）的归因为后续工作提供了明确的避坑方向。
2. **跨模型一致性**：Qwen-2.5-7B 和 Llama-3.1-8B 两个不同架构上的结果方向一致（30× vs 26× gap, 67-79% vs 65-56% conflict rate），增强了结论的可信度。
3. **实验设计的控制组思路合理**：4-way ablation（Qwen）有效隔离了 LoRA 贡献 vs 门控贡献 vs 均匀门控 vs 基线。Uniform Gate 对照组是亮点——证明了 per-layer specialization 没有提供额外增益。
4. **Scheduled sampling 因果实验**：虽然统计功效不足，但思路正确——通过减少 exposure bias 来测试其对 gap 的贡献，是一个有说服力的实验设计。
5. **梯度冲突分析**（Table 6）：量化 NTP vs GAR 梯度的 magnitude ratio 和 directional conflict，是论文最有说服力的机制证据。

---

## 对 Director 问题的逐项回应

### 1. Experimental soundness
中等。核心实验设计（4-way ablation + cross-model validation + scheduled sampling causal test）思路合理，但执行层面有显著缺陷：单种子、小样本、关键超参未报告。控制组设计（Uniform Gate）是亮点。

### 2. Statistical rigor
不足。Bootstrap CI 方法选择正确，但 n=50 的 power 太低；p≈0.07 的 scheduled sampling 结果不能作为强因果证据；无 multi-seed variance 估计。负面结果论文需要更高的统计标准（要证明 "不存在效果" 而非 "没检测到效果"）。

### 3. Ablation completeness
部分完整。Qwen 4-way 是好的，但 Llama 少了 Uniform Gate。更关键的缺失是 λ_GAR 敏感性和训练数据量的消融。如果论文声称方法 "本质上" 不行，需要证明在合理的超参空间内都不行。

### 4. Reproducibility
不足（2/5）。缺少 λ 值、batch size、optimizer、learning rate schedule、UltraChat 子集选择标准、v1-v6 details。Seed 和 epoch 数有报告。

### 5. Missing experiments
- Multi-seed（最关键）
- λ_GAR sensitivity sweep
- 更大训练集
- Llama Uniform Gate
- 更多 SS ratios
- Attention heatmap 可视化
- Gate value 分布随训练的变化
- PPL 在 SS 条件下的变化

### 6. Methodological concerns
ThreadGate 设计作为 "最简单的门控方案" 是合理的——论文的 point 是即使最基本的门控也不 work。但这也意味着结论只适用于 scalar gating，不能推广到 vector gating 或更复杂的门控机制。GAR 作为代理指标有一定效度（instruction compliance r=0.82），但下游验证有限。

### 7. Presentation
表格清晰但缺少图形化呈现。全文 0 figure，对于研究注意力行为的论文来说是重大遗憾。引用全部失效是最严重的呈现问题。

---

**Director 要求的 6-point scale 评分**（补充映射）：

| 维度 | 分数 | 说明 |
|------|------|------|
| Soundness | 3/6 (Weak Reject) | 方法思路合理但执行层面有显著统计和消融缺陷 |
| Significance | 4/6 (Weak Accept) | 有价值的负面结果，机制归因对社区有参考意义 |
| Clarity | 2/6 (Reject) | 引用全部失效；无 figure；损失函数定义不完整 |
| **Overall** | **3/6 (Weak Reject)** | 核心贡献有价值但需要 major revision：修复引用、multi-seed、补充消融、增加可视化 |

**ARR Overall Assessment**: 3.0（Findings acceptance）——如果引用修复、补充 multi-seed 和关键消融，可达 Findings 水平。当前状态更接近 2.5（Borderline Findings）。


---

[Reviewer 2 审稿结果]:
审稿报告已提交给 Review Director。

核心结论：**ARR Overall 2.5（Borderline Findings）**，6-point Overall 3（Weak Reject）。

主要问题：
1. **Novelty 不足**——梯度竞争和 exposure bias 是已知现象，论文在新场景确认但未提供意外洞察
2. **标题 "Cannot" overclaims**——仅测试标量门控一种变体，且 scheduled sampling 能部分缓解
3. **Dongre et al. (2026) 不可查证**——整个实验框架的基础引用无法验证
4. **Related work 缺失 multi-task gradient conflict 文献**（GradNorm/PCGrad 等），恰好是论文核心机制的直接上位文献

主要优势：实验方法论规范（双模型、4-way 消融、bootstrap CI），叙事结构清晰。

---

[Reviewer 1 审稿结果]:
审稿完成。已向 Review Director 提交 Reviewer 1 的完整审稿报告，核心结论：

- **ARR Overall**: 3.0（Findings acceptance），当前状态接近 2.5（Borderline Findings）
- **4 个 Must-Fix**：引用全部失效（编译问题+核心参考 dongre2026 不可查）、单种子支撑绝对否定 claim、50 样本统计功效不足、损失函数超参数未报告
- **6 个 Should-Fix**：Llama 缺 Uniform Gate 对照、无 λ_GAR 敏感性消融、训练数据量可能是混淆变量、全文无图（注意力论文无注意力热力图）、scheduled sampling p≈0.07 未达显著、reverse turn conditioning 证据间接
- **主要优势**：有价值的负面结果、跨模型一致性、4-way ablation 设计合理、梯度冲突量化分析是最有力的机制证据

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 18 · 2026-05-19T15:42:51.088282+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 19 · 2026-05-19T15:42:51.540703+00:00_

1	---
2	name: review-director-session-start
3	description: Review Director session 启动初始化流程——圆桌多轮审稿协议。Review Director 角色 session 启动时自动使用。
4	priority: 9
5	scope: global
6	tags:
7	- workflow
8	- review
9	- session
10	version: 3
11	roles:
12	- review_director
13	---
14	
15	# Review Director Session 启动流程（圆桌会议模式）
16	
17	## 初始化
18	
19	1. `director_get_project_overview(project)` — 了解研究现状（实验状态、最新报告）
20	2. 读取论文文件状态：检查 `projects/{project}/paper/` 或 `main.tex` 是否存在
21	3. 检查是否有来自 Research Director 的论文提交（`[论文提交]` 消息）
22	4. 向用户简要汇报：
23	   - **投稿目标**：venue 和 deadline
24	   - **论文状态**：当前草稿位置和版本
25	   - **资料完整性**：提交的材料是否齐全
26	   - **下一步**：即将开始的圆桌审稿流程
27	
28	## 评审流程（收到论文提交后执行）
29	
30	### Step 0 — 资料检查 + Venue 调研（必须先做，不可跳过）
31	
32	1. 检查提交资料完整性：论文文件是否存在、是否可读、补充材料是否齐全
33	2. 确认目标投稿 venue（从提交消息中获取）
34	3. 用 `web_search` 搜索该 venue 当前轮次的 CFP（Call for Papers），关键词示例：
35	   - `"&lt;venue name> 2026 call for papers" site:aclweb.org`
36	   - `"&lt;venue name> 2026 submission deadline"`
37	   - `"&lt;venue name> 2026 author guidelines"`
38	4. **验证 deadline 未过期**：今天日期与截止日期对比，若已过期立即通知用户，不继续
39	5. 提取当前版本的格式要求：
40	   - 页数限制（正文 / 附录 / 参考文献）
41	   - 模板（ACL / IEEE / NeurIPS / ICML / ...）
42	   - 匿名规则（double-blind / single-blind / open）
43	   - 附录规则（是否允许、是否参与审稿）
44	   - 引用格式（natbib / biblatex / 特定 .bst）
45	6. 将以上信息作为上下文，随任务一起传递给 Reviewer
46	
47	⚠️ 禁止使用训练知识中的 venue 要求——格式标准每年都会更新，必须实时搜索确认。
48	
49	### Step 0.5 — 决定 Reviewer 编排
50	
51	根据 venue 类型和论文特点，决定：
52	- 需要几个 Reviewer（1-5 人）
53	- 每个 Reviewer 的审查侧重
54	
55	参考：
56	- **顶会长文**（NeurIPS/ICML/ACL）：3 人（方法/实验 + novelty/related work + 格式/ethics）
57	- **一般会议**（EMNLP/NAACL）：2 人（方法严谨性 + 新颖性/完整性）
58	- **Workshop / 短文**：1 人（全面审查）
59	
60	向 Group C（即项目配置中的 `feishu.review_chat_id` 审稿群）汇报编排决定。
61	
62	### Step 0.6 — 外部审稿线（与 Step 1 并行）
63	
64	检查项目配置中 `external_review.paperreview_ai.enabled` 是否为 `true`：
65	- 如果启用：调用 `request_external_review(project, paper_pdf_path, venue)` 向用户群发送协助提交卡片
66	- 这一步与 Step 1（内部 Reviewer 分配）**并行执行**，不阻塞内部审稿流程
67	- 外部结果到达后（用户在群里粘贴），纳入 Step 4 最终报告
68	- 如果到 Ste
…[truncated 3027 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 20 · 2026-05-19T15:42:51.692193+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "turn_residual_gating",
  "file": "paper_checklist.yaml",
  "max_chars": "3000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "turn_residual_gating",
    "file": "paper_checklist.yaml",
    "max_chars": "3000"
  }
}
```

</details>

---


### Tool result

_source line 21 · 2026-05-19T15:42:51.742767+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"No paper_checklist.yaml found for 'turn_residual_gating'.\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 22 · 2026-05-19T15:42:59.225281+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review",
    "max_results": "3"
  }
}
```

</details>

---


### Tool result

_source line 23 · 2026-05-19T15:42:59.276863+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "ToolSearch",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 24 · 2026-05-19T15:43:02.544117+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_local_file",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_local_file",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 25 · 2026-05-19T15:43:02.595093+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 26 · 2026-05-19T15:43:06.399449+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/agent"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/agent"
  }
}
```

</details>

---


### Tool result

_source line 27 · 2026-05-19T15:43:06.701827+00:00_

&lt;tool_use_error>Directory does not exist: /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/agent. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/review_director_889420d1.&lt;/tool_use_error>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "Glob",
  "elapsed_ms": 302
}
```

</details>

---


### Tool call

_source line 28 · 2026-05-19T15:43:06.702228+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.pdf",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.pdf",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating"
  }
}
```

</details>

---


### Tool result

_source line 29 · 2026-05-19T15:43:06.753749+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T135115/best/paper.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T135115/median/paper.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T135115/worst/paper.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T143220/best/paper.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T143220/median/paper.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T145320/best/paper.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T145320/median/paper.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T145320/worst/paper.pdf

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "Glob",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 30 · 2026-05-19T15:43:09.665266+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/config.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/config.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating"
  }
}
```

</details>

---


### Tool result

_source line 31 · 2026-05-19T15:43:09.665739+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 32 · 2026-05-19T15:43:12.628555+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "*.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "*.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating"
  }
}
```

</details>

---


### Tool result

_source line 33 · 2026-05-19T15:43:12.679382+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/literature_map.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/mistakes.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/manifest.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T135115/best/imagined_experiments.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T135115/median/imagined_experiments.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T135115/worst/imagined_experiments.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T135115/best/review_context.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T143220/best/imagined_experiments.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T143220/median/imagined_experiments.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/decisions.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T145320/best/imagined_experiments.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T145320/median/imagined_experiments.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T145320/worst/imagined_experiments.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/dream_registry.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dre
…[truncated 539 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 34 · 2026-05-19T15:43:16.596692+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/turn_residual_gating.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/turn_residual_gating.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11"
  }
}
```

</details>

---


### Tool result

_source line 35 · 2026-05-19T15:43:16.998384+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_11/config/projects/turn_residual_gating.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "Glob",
  "elapsed_ms": 401
}
```

</details>

---


### Tool call

_source line 36 · 2026-05-19T15:43:17.048935+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/projects.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/projects.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11"
  }
}
```

</details>

---


### Tool result

_source line 37 · 2026-05-19T15:43:17.099507+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 38 · 2026-05-19T15:43:19.714238+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/config/projects/turn_residual_gating.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/config/projects/turn_residual_gating.yaml"
  }
}
```

</details>

---


### Tool result

_source line 39 · 2026-05-19T15:43:19.766005+00:00_

1	execution:
2	  gpu_ids:
3	  - westd-20861:cuda:0
4	  project_path: /root/turn_residual_gating
5	  servers:
6	  - westd-20861
7	feishu:
8	  chat_id: oc_640e53b6afbbd5e34eb7273cd5a707a0
9	  operational_chat_id: oc_934666158b769e82a2351d9206410118
10	  submission_chat_id: oc_9287ee173cf15d688adcd081f5d861f5
11	project:
12	  created_at: '2026-05-18T04:42:05.519Z'
13	  description: 'ThreadGate: Goal-Accessibility-Guided Residual Intervention for Multi-Turn
14	    Degradation'
15	  name: turn_residual_gating
16	  phase: research
17	  source_idea_id: idea_011
18	venue: emnlp-2026
19	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 40 · 2026-05-19T15:43:28.000084+00:00_

called mcp__agent-ml-research__dispatch_visual_check

<details open><summary>🔧 Tool call — mcp__agent-ml-research__dispatch_visual_check</summary>

```json
{
  "project": "turn_residual_gating",
  "review_chat_id": "oc_9287ee173cf15d688adcd081f5d861f5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "tool_args": {
    "project": "turn_residual_gating",
    "review_chat_id": "oc_9287ee173cf15d688adcd081f5d861f5"
  }
}
```

</details>

---


### Tool result

_source line 41 · 2026-05-19T15:43:28.503560+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"未找到投稿论文 PDF 路径（review_paper_pdf_path 未配置）。请确认 Director 提交审稿时填写了 paper_pdf_path。\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 503
}
```

</details>

---


### Tool call

_source line 42 · 2026-05-19T15:44:03.049753+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "## 交叉分享：Reviewer 2 的完整审稿意见\n\n请逐条回应 Reviewer 2 的每个 Must-Fix 和 Should-Fix 问题。对每条使用 **[AGREE]** 同意并说明理由，或 **[REBUT]** 反驳并引用具体 Section/Table/Figure 作为证据。\n\n---\n\n以下是 Reviewer 2 的完整审稿原文：\n\n# Reviewer 2 审稿报告：Novelty &amp; Related Work\n\n**论文**: \"Why Lightweight Gating Cannot Fix Multi-Turn Attention Degradation: A Mechanistic Analysis\"\n**Venue**: EMNLP 2026 (via ACL Rolling Review)\n\n## 总体评分\n**Overall (ARR)**: 2.5 / 5 — Borderline Findings\n**Overall (6-point)**: 3 / 6 — Weak Reject\n\n## Must-Fix 问题\n\n### N1 [critical] Novelty 声称过高——两个核心机制均为已知现象的直接应用\n- **具体位置**: §1 Abstract \"first quantitative measurement\"；§6.1 gradient competition；§6.4 exposure bias\n- **问题**: \n  论文声称的两个 failure mechanism：\n  1. **NTP-GAR 梯度竞争**（7–15× 幅度比）= 多任务梯度冲突（multi-task gradient conflict），这是 multi-task learning 领域 2018 年以来的经典问题。GradNorm (Chen et al., 2018) 定义了 gradient magnitude balancing，PCGrad (Yu et al., NeurIPS 2020) 定义了 gradient direction conflict 的 surgery 方法。论文将一个已有成熟解决方案的已知问题重新\"发现\"却完全不引用这些文献。\n  2. **Teacher-forcing distribution shift** = exposure bias (Bengio et al., 2015)。论文自己在 §2 和 §6.4 中引用了 exposure bias 文献，却在 Abstract 和 contributions 中声称这是\"first quantitative measurement\"。\n  30× gap 的具体数值是新的，但数值本身不构成方法论贡献。\n\n### N2 [critical] 标题 \"Cannot\" 过度声称——证据仅支持 \"fails to\" under tested conditions\n- Scheduled sampling 将 gap 从 30× 降至 12.3×，说明改变训练策略就能部分修复——直接反驳 \"cannot\"。\n- 未测试向量门控、attention-head-specific gate 等替代方案。\n\n### N3 [critical] 核心先行工作 Dongre et al. (2026) 不可查证\n- OpenAlex 中完全不可查（similarity score 仅 0.336）。\n- 如果这篇论文不存在或无法获取，则本文的整个实验框架（GAR 指标、probe AUC baseline）均缺乏可验证的基础。\n\n### N4 [critical] Related Work 缺失关键文献：Multi-task Gradient Conflict\n- §6.1 的核心发现是 NTP 和 GAR 梯度存在方向冲突和幅度不平衡——这正是 multi-task gradient conflict 的定义。但 §2 完全未讨论 GradNorm/PCGrad/CAGrad/Nash-MTL。\n- 如果 PCGrad 能解决梯度竞争问题，则本文的\"失败\"可能仅仅是因为没有使用正确的优化策略。\n\n## Should-Fix 问题\n\n### W1 [warning] 范围过窄——仅标量门控，不足以支撑 \"lightweight gating\" 的一般性结论\n### W2 [warning] Scheduled sampling 实验统计不显著（p ≈ 0.07）\n### W3 [warning] GAR 作为唯一注意力退化指标的局限性未充分讨论\n### W4 [warning] 论文长度明显低于 EMNLP long paper 上限（正文约 6 页 vs 限制 8 页）\n### W5 [warning] liu2016attention 引用可能错配\n### W6 [warning] 4 个 orphan bib 条目未被引用\n\n## 主要优势\n1. 实验设计的方法论规范性（双模型、4-way 消融、bootstrap CI）\n2. 清晰的叙事结构\n3. 诚实的 hedging（§7 Discussion）\n4. Per-layer gradient 分析的粒度\n\n---\n\n请对上述每个 Must-Fix（N1-N4）和 Should-Fix（W1-W6）逐条给出 [AGREE] 或 [REBUT] 回应。重点关注你作为方法/实验审稿人的视角是否与 novelty 审稿人的判断一致或有分歧。",
  "project": "turn_residual_gating",
  "chat_id": "oc_9287ee173cf15d688adcd081f5d861f5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "text": "## 交叉分享：Reviewer 2 的完整审稿意见\n\n请逐条回应 Reviewer 2 的每个 Must-Fix 和 Should-Fix 问题。对每条使用 **[AGREE]** 同意并说明理由，或 **[REBUT]** 反驳并引用具体 Section/Table/Figure 作为证据。\n\n---\n\n以下是 Reviewer 2 的完整审稿原文：\n\n# Reviewer 2 审稿报告：Novelty &amp; Related Work\n\n**论文**: \"Why Lightweight Gating Cannot Fix Multi-Turn Attention Degradation: A Mechanistic Analysis\"\n**Venue**: EMNLP 2026 (via ACL Rolling Review)\n\n## 总体评分\n**Overall (ARR)**: 2.5 / 5 — Borderline Findings\n**Overall (6-point)**: 3 / 6 — Weak Reject\n\n## Must-Fix 问题\n\n### N1 [critical] Novelty 声称过高——两个核心机制均为已知现象的直接应用\n- **具体位置**: §1 Abstract \"first quantitative measurement\"；§6.1 gradient competition；§6.4 exposure bias\n- **问题**: \n  论文声称的两个 failure mechanism：\n  1. **NTP-GAR 梯度竞争**（7–15× 幅度比）= 多任务梯度冲突（multi-task gradient conflict），这是 multi-task learning 领域 2018 年以来的经典问题。GradNorm (Chen et al., 2018) 定义了 gradient magnitude balancing，PCGrad (Yu et al., NeurIPS 2020) 定义了 gradient direction conflict 的 surgery 方法。论文将一个已有成熟解决方案的已知问题重新\"发现\"却完全不引用这些文献。\n  2. **Teacher-forcing distribution shift** = exposure bias (Bengio et al., 2015)。论文自己在 §2 和 §6.4 中引用了 exposure bias 文献，却在 Abstract 和 contributions 中声称这是\"first quantitative measurement\"。\n  30× gap 的具体数值是新的，但数值本身不构成方法论贡献。\n\n### N2 [critical] 标题 \"Cannot\" 过度声称——证据仅支持 \"fails to\" under tested conditions\n- Scheduled sampling 将 gap 从 30× 降至 12.3×，说明改变训练策略就能部分修复——直接反驳 \"cannot\"。\n- 未测试向量门控、attention-head-specific gate 等替代方案。\n\n### N3 [critical] 核心先行工作 Dongre et al. (2026) 不可查证\n- OpenAlex 中完全不可查（similarity score 仅 0.336）。\n- 如果这篇论文不存在或无法获取，则本文的整个实验框架（GAR 指标、probe AUC baseline）均缺乏可验证的基础。\n\n### N4 [critical] Related Work 缺失关键文献：Multi-task Gradient Conflict\n- §6.1 的核心发现是 NTP 和 GAR 梯度存在方向冲突和幅度不平衡——这正是 multi-task gradient conflict 的定义。但 §2 完全未讨论 GradNorm/PCGrad/CAGrad/Nash-MTL。\n- 如果 PCGrad 能解决梯度竞争问题，则本文的\"失败\"可能仅仅是因为没有使用正确的优化策略。\n\n## Should-Fix 问题\n\n### W1 [warning] 范围过窄——仅标量门控，不足以支撑 \"lightweight gating\" 的一般性结论\n### W2 [warning] Scheduled sampling 实验统计不显著（p ≈ 0.07）\n### W3 [warning] GAR 作为唯一注意力退化指标的局限性未充分讨论\n### W4 [warning] 论文长度明显低于 EMNLP long paper 上限（正文约 6 页 vs 限制 8 页）\n### W5 [warning] liu2016attention 引用可能错配\n### W6 [warning] 4 个 orphan bib 条目未被引用\n\n## 主要优势\n1. 实验设计的方法论规范性（双模型、4-way 消融、bootstrap CI）\n2. 清晰的叙事结构\n3. 诚实的 hedging（§7 Discussion）\n4. Per-layer gradient 分析的粒度\n\n---\n\n请对上述每个 Must-Fix（N1-N4）和 Should-Fix（W1-W6）逐条给出 [AGREE] 或 [REBUT] 回应。重点关注你作为方法/实验审稿人的视角是否与 novelty 审稿人的判断一致或有分歧。",
    "project": "turn_residual_gating",
    "chat_id": "oc_9287ee173cf15d688adcd081f5d861f5"
  }
}
```

</details>

---


### Tool result

_source line 43 · 2026-05-19T15:44:24.638430+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 21588
}
```

</details>

---


### Tool call

_source line 44 · 2026-05-19T15:44:24.891594+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "## 交叉分享：Reviewer 1 的完整审稿意见\n\n请逐条回应 Reviewer 1 的每个 Must-Fix 和 Should-Fix 问题。对每条使用 **[AGREE]** 同意并说明理由，或 **[REBUT]** 反驳并引用具体 Section/Table/Figure 作为证据。\n\n---\n\n以下是 Reviewer 1 的完整审稿原文：\n\n# Reviewer 1 审稿报告：Methods &amp; Experiments\n\n**论文**: \"Why Lightweight Gating Cannot Fix Multi-Turn Attention Degradation: A Mechanistic Analysis\"\n**审稿侧重**: 方法设计、实验设计、统计严谨性、可复现性、消融完整性\n\n## 总体评分\n**Overall Assessment**: 3.0 / 5（Findings acceptance）\n**Overall (6-point)**: 3 / 6 — Weak Reject\n\n## Must-Fix 问题\n\n### N1 [critical] 所有引用均渲染为 \"?\"——bibliography 编译失败\n- PDF 中每一处引用都显示为 \"?\" 而非作者名。\n- 引用审计：24 条 bib 条目中，3 条在 OpenAlex 上未找到（dongre2026、zou2023representation、elhage2021mathematical），5 条存在作者或年份不匹配，4 条 orphan entries。\n\n### N2 [critical] 单种子实验支撑 \"Cannot\" 级别的强断言\n- 所有实验均使用 seed=42 单次运行。\n- 30× 训练-推理 gap 在不同 seed 下是否稳定？负面结果论文的证据标准应高于正面结果。\n\n### N3 [critical] 评估样本量过小（50 conversations）且统计功效存疑\n- Cohen's d ≈ 0.22 是小效应量，在 n=50 下 power 不足。\n- scheduled sampling 结果 p≈0.07 在 α=0.05 下不显著。\n\n### N4 [critical] 损失函数超参数和组件定义缺失——无法复现\n- λ_GAR、λ_div 具体数值未报告。\n- L_div 无数学定义。v1-v6 完全没有细节。\n\n## Should-Fix 问题\n\n### W1 [warning] Llama 上未测试 Uniform Gate——跨模型验证不完整\n### W2 [warning] 无 λ_GAR 敏感性消融\n### W3 [warning] 训练数据量（1,000 conversations）可能是混淆变量\n### W4 [warning] 缺少可视化——论文关于注意力退化却没有注意力热力图\n### W5 [warning] Scheduled sampling 因果推断的局限性未充分讨论\n### W6 [warning] \"Reverse turn conditioning\"（Section 6.2）的证据是间接的\n\n## 主要优势\n1. 有价值的负面结果——两个失败机制的归因为后续工作提供避坑方向\n2. 跨模型一致性（Qwen 30× vs Llama 26× gap）\n3. 4-way ablation 设计合理（Uniform Gate 对照组是亮点）\n4. Scheduled sampling 因果实验思路正确\n5. 梯度冲突量化分析（Table 6）是最有说服力的机制证据\n\n---\n\n请对上述每个 Must-Fix（N1-N4）和 Should-Fix（W1-W6）逐条给出 [AGREE] 或 [REBUT] 回应。重点关注你作为 novelty 审稿人的视角是否与方法/实验审稿人的判断一致或有分歧。",
  "project": "turn_residual_gating",
  "chat_id": "oc_9287ee173cf15d688adcd081f5d861f5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "text": "## 交叉分享：Reviewer 1 的完整审稿意见\n\n请逐条回应 Reviewer 1 的每个 Must-Fix 和 Should-Fix 问题。对每条使用 **[AGREE]** 同意并说明理由，或 **[REBUT]** 反驳并引用具体 Section/Table/Figure 作为证据。\n\n---\n\n以下是 Reviewer 1 的完整审稿原文：\n\n# Reviewer 1 审稿报告：Methods &amp; Experiments\n\n**论文**: \"Why Lightweight Gating Cannot Fix Multi-Turn Attention Degradation: A Mechanistic Analysis\"\n**审稿侧重**: 方法设计、实验设计、统计严谨性、可复现性、消融完整性\n\n## 总体评分\n**Overall Assessment**: 3.0 / 5（Findings acceptance）\n**Overall (6-point)**: 3 / 6 — Weak Reject\n\n## Must-Fix 问题\n\n### N1 [critical] 所有引用均渲染为 \"?\"——bibliography 编译失败\n- PDF 中每一处引用都显示为 \"?\" 而非作者名。\n- 引用审计：24 条 bib 条目中，3 条在 OpenAlex 上未找到（dongre2026、zou2023representation、elhage2021mathematical），5 条存在作者或年份不匹配，4 条 orphan entries。\n\n### N2 [critical] 单种子实验支撑 \"Cannot\" 级别的强断言\n- 所有实验均使用 seed=42 单次运行。\n- 30× 训练-推理 gap 在不同 seed 下是否稳定？负面结果论文的证据标准应高于正面结果。\n\n### N3 [critical] 评估样本量过小（50 conversations）且统计功效存疑\n- Cohen's d ≈ 0.22 是小效应量，在 n=50 下 power 不足。\n- scheduled sampling 结果 p≈0.07 在 α=0.05 下不显著。\n\n### N4 [critical] 损失函数超参数和组件定义缺失——无法复现\n- λ_GAR、λ_div 具体数值未报告。\n- L_div 无数学定义。v1-v6 完全没有细节。\n\n## Should-Fix 问题\n\n### W1 [warning] Llama 上未测试 Uniform Gate——跨模型验证不完整\n### W2 [warning] 无 λ_GAR 敏感性消融\n### W3 [warning] 训练数据量（1,000 conversations）可能是混淆变量\n### W4 [warning] 缺少可视化——论文关于注意力退化却没有注意力热力图\n### W5 [warning] Scheduled sampling 因果推断的局限性未充分讨论\n### W6 [warning] \"Reverse turn conditioning\"（Section 6.2）的证据是间接的\n\n## 主要优势\n1. 有价值的负面结果——两个失败机制的归因为后续工作提供避坑方向\n2. 跨模型一致性（Qwen 30× vs Llama 26× gap）\n3. 4-way ablation 设计合理（Uniform Gate 对照组是亮点）\n4. Scheduled sampling 因果实验思路正确\n5. 梯度冲突量化分析（Table 6）是最有说服力的机制证据\n\n---\n\n请对上述每个 Must-Fix（N1-N4）和 Should-Fix（W1-W6）逐条给出 [AGREE] 或 [REBUT] 回应。重点关注你作为 novelty 审稿人的视角是否与方法/实验审稿人的判断一致或有分歧。",
    "project": "turn_residual_gating",
    "chat_id": "oc_9287ee173cf15d688adcd081f5d861f5"
  }
}
```

</details>

---


### Tool result

_source line 45 · 2026-05-19T15:44:26.257876+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1366
}
```

</details>

---


### Assistant

_source line 46 · 2026-05-19T15:44:39.706254+00:00_

**Round 1 交叉分享已派发。** 当前状态：

| 步骤 | 状态 |
|------|------|
| R1 初审（方法/实验） | ✅ 完成 — ARR 3.0 |
| R2 初审（Novelty/Related Work） | ✅ 完成 — ARR 2.5 |
| 交叉分享 → R1 看 R2 意见 | ⏳ 等待回应 |
| 交叉分享 → R2 看 R1 意见 | ⏳ 等待回应 |
| 外部审稿 | ⊘ 未配置 |
| 视觉审查 | ⚠️ 失败（`review_paper_pdf_path` 未配置，Step 4 报告中标注） |

**两位 Reviewer 的初步共识方向**：
- 标题 "Cannot" overclaiming（R1+R2 均提出）
- Dongre et al. (2026) 不可查证（R1+R2 均提出）
- 引用编译失效（R1 为 critical，R2 观察到的 PDF 版本引用正常——需确认）
- 统计功效不足（R1 主张，R2 附议 p≈0.07）

**潜在分歧点**：
- R1 给 Excitement 3/5，R2 给 2/5（R2 对 novelty 更严格）
- R1 认为负面结果有参考价值（Significance 4/6），R2 认为仅为已知现象的确认性验证（Significance 2/6）

等待两位 Reviewer 完成交叉回应后进入收敛判断（Step 3）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director"
}
```

</details>

---


## Round 3

## Round 3

10 recorded events


### User

_source line 47 · 2026-05-19T15:44:40.781748+00:00_

[Reviewer 2 审稿意见]:

# Reviewer 2 交叉回应：对 R1 审稿意见的逐条评价

---

## 对 R1 主要发现的回应

### 实验 Soundness 方面

[AGREE] R1-Ablation-Asymmetry: Llama 仅 3-way 消融（无 Uniform Gate）确实削弱了跨模型声称的说服力。我补充一点：论文标题用 "Lightweight Gating"（泛称）而非 "Scalar Residual Gating"（具体），但跨模型验证本身也不完整——两个模型均为相似规模（7-8B）的 decoder-only transformer，没有测试不同架构（如 MoE、encoder-decoder）或不同规模（1B, 70B），泛化性主张需要更谨慎。

[AGREE] R1-Downstream-r072: r=0.72 的 GAR-instruction compliance 相关性确实只解释约 52% 方差。我的 W3 也提出了 GAR 单指标依赖的问题。但我想补充：r=0.72 对于一个 proxy metric 来说并不差——问题不在于相关性是否"够高"，而在于论文将所有机制分析（gradient conflict、distribution shift）都建立在 GAR 上。如果 GAR 衰减的 48% 未解释方差来自 GAR 指标本身的噪声（如 position bias、tokenization artifacts），则机制解释的可靠性会打折扣。

[AGREE] R1-Single-Seed: 单种子（42）是实质性限制。我在 Soundness 评分中考虑了这一点但未单独列为 Must-Fix。R1 的分析更精确：bootstrap CI 覆盖推理时方差但不覆盖训练方差。Gate 初始化、LoRA 初始化、数据 shuffling 的随机性都可能影响 30× gap 的具体数值。建议至少 3 个种子。

### 统计严格性方面

[AGREE] R1-Llama-Underpowered: Llama 的 CI [−0.008, 0.041] 和 d=0.22 表明检测小效应的统计功效不足。这与我对论文跨模型声称的担忧一致——Llama 上的"directional consistency"可能仅仅是 underpowered test 的 null result。

[AGREE] R1-p007-Honest: p≈0.07 的诚实报告确实值得肯定。我在 W2 中也提到了这一点。我们对此的评价一致：报告本身恰当，但将其列为正式 contribution 需要更强证据。

### 可重复性方面

[AGREE] R1-v1v6-Missing: v1-v6 loss 配置未详述是一个遗漏。我在"小问题"中提到了这一点。论文声称 "explored seven loss configurations" 但仅报告 v7 的结果——读者无法判断 v7 是否通过 principled selection 还是 cherry-picking 得出。至少应在 Appendix 提供 v1-v6 的描述和关键指标。

[AGREE] R1-No-Code: 无代码/数据发布降低可重复性。对于 negative result 论文尤其重要——读者需要能验证负面结果不是实现 bug。

### 缺失实验方面

[AGREE] R1-Zero-Figures: **这是我遗漏的一个重要观察。** 一篇标题含 "Mechanistic Analysis" 的论文零图表确实是严重缺陷。Attention heatmap（可视化 GAR 衰减）、training curve（展示三阶段动态）、per-layer gradient heatmap（展示冲突模式）——这些都是 mechanistic analysis 的标准视觉证据。9 个 table 的纯数值呈现大幅降低了分析的直观说服力和读者体验。我应在初次审稿中将此列为 Should-Fix。

[AGREE] R1-SS-Qwen-Only: Scheduled sampling 仅在 Qwen 上测试、未在 Llama 上验证，确实削弱了 Contribution 4 的跨模型泛化性。这与 N2（overclaiming）问题叠加——论文不仅在门控变体上范围窄，在缓解实验上也是单模型的。

---

## 对 R1 具体问题的回答

### Q1: "First quantitative measurement" novelty claim 是否成立？

**不成立。** 这是我 N1 (critical) 的核心论点。详细理由：

1. **Exposure bias 的量化早已存在。** Ranzato et al. (2016)、Wiseman & Rush (2016) 等在 sequence generation 任务中量化了 teacher-forcing 与 autoregressive generation 之间的性能 gap。本文的"30× gap"是在一个新指标（GAR）上的测量，不是对一个新现象的首次量化。

2. **Multi-task gradient conflict 的量化也已有先例。** GradNorm (Chen et al., 2018) 通过监控 gradient magnitude ratios 来平衡任务权重——论文的 7-15× magnitude ratio 测量方法与 GradNorm 的诊断方法本质相同。

3. **"First" claim 的合理缩小范围**: 如果改为 "first empirical demonstration that exposure bias critically undermines auxiliary attention-steering objectives in modern LLMs"，这个 claim 会更准确，但也暴露了贡献本质是 application of known insights to a new setting，而非 new insights themselves。

结论：这是对已知现象在新场景中的**确认性量化**（confirmatory quantification），而非**首次量化**（first quantitative measurement）。Novelty 应相应降级。

### Q2: 仅测试标量门控对 negative result 价值的影响？

**严重限制。** 理由如下：

负面结果论文的说服力与"排除的假设空间"成正比。本文排除了一个极窄的假设——"标量 per-layer ReZero gate + joint NTP-GAR training 能修复 multi-turn attention degradation"。这距离排除 "lightweight gating" 这个大类还很远：

| 未测试变体 | 为什么可能表现不同 |
|-----------|-------------------|
| Vector gate (per-dim) | 更高容量，可学习 dimension-specific 行为 |
| Head-specific gate | 不同 attention head 可能有不同的 goal-tracking role |
| Low-rank gate | 介于标量和全矩阵之间的容量权衡 |
| 分离训练（先 GAR 后 NTP）| 避免梯度竞争，但可能引入其他问题 |
| Gradient surgery (PCGrad) | 直接解决 §6.1 诊断的梯度冲突 |

如果论文能证明即使用 PCGrad 消除梯度竞争 + vector gate 增加容量，exposure bias 仍然导致 30× gap，那"轻量门控不行"的结论就有坚实基础。目前只测试了最简单的配置就下了"cannot"的结论，说服力不足。

**量化估计**: 如果 "lightweight gating" 包含上述 5 种变体，本文仅覆盖了 1/5 = 20% 的假设空间。对于声称 "cannot" 的论文，这远远不够。

### Q3: 是否更适合作为 workshop paper 或 short paper？

**我倾向于 workshop paper，具体理由：**

| 因素 | Workshop | Short Paper | Long Paper |
|------|----------|-------------|------------|
| 范围 | ✓ 适合窄范围探索 | ✓ 适合有限但完整的贡献 | ✗ 范围不够 |
| Novelty | ✓ Workshop 对 novelty 门槛更低 | △ Short paper 仍需 non-trivial insight | ✗ 不够 |
| 方法论完整性 | △ 当前水平可接受 | △ 需补统计严格性 | ✗ 需大量补充实验 |
| 实际长度 | △ 目前 ~6 页正文偏长 | ✓ 缩到 4 页很合适 | ✗ 内容撑不满 8 页 |

最佳定位：**ACL Workshop on Insights from Negative Results**（真实存在的 workshop）。这个 workshop 专门接收负面结果论文，评审标准侧重"是否提供了有价值的失败信息"而非 novelty 的绝对高度。本文的实验方法论在 workshop 标准下是扎实的。

如果坚持主会投稿：建议作为 **short paper** 提交到 ARR，聚焦在 "exposure bias undermines auxiliary attention losses" 这一个 takeaway，削减不必要的 overclaiming，补充 1-2 个 gradient surgery baseline 以增加 actionable insight。

---

## 评分更新

在看到 R1 的发现后（特别是零图表问题和 Llama 评估不对称性），我对部分评分做微调：

| 维度 | 原评分 | 更新 | 理由 |
|------|--------|------|------|
| Soundness (ARR) | 3/5 | 2.5/5 | 零图表+单种子+Llama 不完整消融，叠加后更接近"Poor: some main claims not sufficiently supported" |
| Excitement (ARR) | 2/5 | 2/5 | 不变 |
| Clarity (6-pt) | 4/6 | 3/6 | R1 关于零图表的观察有理——"mechanistic analysis" 无可视化是叙事缺陷 |
| **Overall (ARR)** | **2.5/5** | **2.5/5** | **维持 Borderline Findings**——补充了更多弱点但实验方法论的基础仍在 |
| **Overall (6-pt)** | **3/6** | **3/6** | **维持 Weak Reject** |

---

## R1-R2 共识总结

R1 和 R2 在以下关键判断上一致：
1. 实验方法论基础合理但有显著 gaps（单种子、跨模型不对称、零图表）
2. 论文处于 Weak Reject / Borderline Findings 区间
3. Contribution 不足以支撑 main conference acceptance
4. 存在 overclaiming（标题和 contribution 声称过度）
5. 缺少关键视觉证据（R1 首先发现，R2 同意）

R2 额外强调的 R1 未覆盖的问题：
- Multi-task gradient conflict 文献缺失（N4）
- Dongre et al. (2026) 不可查证（N3）
- 标题 "Cannot" 的具体 overclaiming 分析（N2）
- 缺失正面结果替代方案的深入讨论


---

[Reviewer 2 审稿结果]:
交叉回应已提交。对 R1 的全部观察逐条给出了 [AGREE]/[REBUT] 判断，回答了 R1 的三个问题（novelty claim 不成立、标量门控范围过窄、建议定位为 workshop paper），并根据 R1 发现的零图表和 Llama 评估不对称性问题微调了 Soundness 和 Clarity 评分。Overall 维持 2.5/5 (Borderline Findings) / 3/6 (Weak Reject)。

---

[Reviewer 1 审稿意见]:

# R1 对 R2 审稿意见的交叉回应

---

## 对 R2 主要观察的逐条回应

### Novelty

[AGREE] R2-Novelty-1: 负面结果 + 30× gap 量化是 incremental novelty，同意。我的审稿也将 Excitement 定为 3/5 (Interesting)，未达到 4 (Exciting) 的门槛。

[AGREE] R2-Novelty-2: NTP 主导 auxiliary loss 确实是 multi-task learning 的已知现象。但我认为 R2 略微低估了这一发现在 residual gating 语境中的价值——论文不只是说 "主损失压制辅助损失"，而是量化了这种压制如何导致 gate 学到 reverse turn conditioning（在 early turns 抑制、late turns passive），这比泛泛的梯度冲突更具体。Table 6 的 per-epoch conflict% + magnitude ratio 是有信息量的。

[AGREE] R2-Novelty-3: "Reverse turn conditioning" 确实是最新颖的机制发现。不过如我在 W6 中指出，这一发现的证据是间接的（gate attenuation 仅 2-7%，无显著性检验），新颖性打了折扣。

[AGREE] R2-Novelty-4: Scalar gate 范围限制是我们共同的关切。我在审稿中明确指出 "结论只适用于 scalar gating，不能推广到 vector gating 或更复杂的门控机制"。

### Related Work

[AGREE] R2-RelatedWork-1: 引用全部失效——我在 N1 中已标记为 critical，且补充了引用审计数据（3 条 OpenAlex 未找到，含核心参考 dongre2026；5 条 author/year mismatch；4 条 orphan entries）。

[AGREE] R2-RelatedWork-2: 缺少 inference-time attention intervention baselines。论文 Section 2 提到了 Li et al. (inference-time intervention)、Meng et al. (activation editing)、Zou et al. (representation engineering)，但只是列举，没有讨论为何不将它们作为 baseline 或与 ThreadGate 对比。这是一个合理的 gap。

[AGREE] R2-RelatedWork-3: Exposure bias 讨论确实局限于经典方法。

### Significance

[AGREE] R2-Significance-1: 窄范围（2 models, 1 dataset, scalar gates only）+ 负面结果 + 无 convincing positive path 确实是 borderline 贡献。

[AGREE] R2-Significance-2: "Thorough on Qwen but ambiguous on Llama"——完全同意。Llama 少了 Uniform Gate 对照（我的 W1），使跨模型验证 incomplete。

[AGREE] R2-Significance-3: Scheduled sampling p≈0.07 太弱——我在 W5 中详细讨论了这一点，包括缺少 SS 对 PPL 影响的报告和更多 SS ratio 的测试。

### Writing

[AGREE] R2-Writing-1: 无 figure 是重大弱点——我在 W4 中列出了至少需要的 3 类可视化（attention heatmap、训练曲线、gate 分布）。

[REBUT] R2-Writing-2: R2 说 "'Struggles to' title framing is reasonable"——但据我阅读的 PDF（page 1），论文标题是 **"Why Lightweight Gating Cannot Fix Multi-Turn Attention Degradation"**，用的是 "Cannot"（绝对否定），而非 "Struggles to"。这一点我在 N2 中已标记为 critical issue，因为 "Cannot" 的 claim 强度与单种子证据不匹配。请 Director 确认我们审阅的是否为同一版本。

---

## 回答 R2 的三个问题

### Q1: 单种子是 critical limitation 还是 bootstrap CIs 可以弥补？

**单种子是 critical limitation，bootstrap CIs 无法弥补。**

这涉及两种本质不同的不确定性来源：

- **Bootstrap CI 估计的是**：给定这 50 个 conversations 的评估样本，如果从中重抽样，指标会波动多少？→ 这是 **evaluation variance**（评估层面的抽样不确定性）。
- **Multi-seed 要解决的是**：如果用不同的随机种子重新训练模型，gate 参数、gradient dynamics、最终 GAR 会有多大变化？→ 这是 **training variance**（训练层面的随机性）。

Bootstrap 处理的是下游、训练后的 evaluation noise；它对训练过程中的随机性——权重初始化、mini-batch 顺序、dropout mask——完全无法估计。论文的核心 claim 是 "30× gap 是结构性的、不可避免的"，但在只有一次训练的情况下，我们无法区分：
- 30× gap 是该方法的固有特性（论文的 claim）
- 30× gap 是 seed=42 的偶然表现，seed=7 下可能只有 5×

对于正面结果论文（"我们的方法好"），单种子是常见妥协。但对于负面结果论文（"这个方法不可能 work"），证明标准更高——你需要排除 "你没调好" 的质疑。Multi-seed 是最低要求。

### Q2: 4-way ablation 在无 multi-seed 时是否足够？

**不足够，但接近足够。**

4-way ablation 的 **设计** 是好的——Base/LoRA-only/ThreadGate/Uniform Gate 有效隔离了：
- LoRA 本身的贡献（LoRA-only vs Base）
- 门控的增量贡献（ThreadGate vs LoRA-only）
- Per-layer specialization 的价值（ThreadGate vs Uniform Gate）

Table 2（Qwen）显示所有 fine-tuned variants 收敛到几乎相同的 GAR 和 PPL（GAR-D: 0.013-0.016, PPL: 2.62-2.65），这一 pattern 在 4 组条件间的一致性本身就是间接证据——如果 4 个独立训练的模型都 converge 到同一点，seed 依赖性可能较低。

但 "可能较低" 不等于 "已验证为低"。关键问题是：Table 2 的 4 组数据来自 4 次独立训练（不同配置），不是同一配置的 4 次重复。它们的一致性说明 **配置间** variance 小，但不能说明 **配置内** (across-seed) variance 小。

如果补充 3 个 seed，并且 4-way pattern 在所有 seed 上稳定复现，这将是非常强的证据。当前状态是 "suggestive but not conclusive"。

### Q3: 下游验证（GAR-instruction compliance 相关性）是否充分建立 GAR 的有效性？

**提供了中等支撑，但不充分。**

首先，一个数据修正：我在论文 Section 6.5 中读到的 Pearson correlation 是 **r = 0.82**（p < 0.01），而非 R2 提到的 r = 0.72。请 Director 确认——如果是 0.82 则是 strong correlation，如果是 0.72 则是 moderate。以下基于我阅读的 r = 0.82 分析。

**r = 0.82 的优势**：
- Large effect size（解释 67% 的方差），说明 GAR 确实 capture 了 instruction following 的相关维度
- 在 50 conversations × 2 models 上计算，覆盖了一定的样本量

**r = 0.82 仍然不充分的原因**：
1. **相关性 ≠ 因果性**：GAR 和 instruction compliance 可能都受第三个变量驱动（例如模型的整体 generation quality），而非 GAR → compliance 的因果路径。
2. **Instruction compliance 本身是代理指标**：论文未详细说明 compliance 的测量方式。如果是 "always respond in bullet points" 之类的格式遵守检查，这比语义层面的 instruction following 浅得多。
3. **仅一个下游任务**：如果 GAR 真的 capture 了 multi-turn attention quality，它应该与多个下游指标相关——not just instruction compliance, but also topic coherence, reference resolution, long-range coreference 等。
4. **样本量限制**：50 conversations 下的 r = 0.82 的 95% CI 大约是 [0.70, 0.90]（fisher z 估计），置信区间较宽。

**结论**：r = 0.82 通过了 "GAR 不是无意义指标" 的 sanity check，但不足以建立 GAR 作为 multi-turn dialogue quality 的 gold-standard proxy。论文需要在 Discussion 中明确 GAR 的 construct validity 局限。

---

## R1-R2 共识总结

| 问题 | R1 | R2 | 共识 |
|------|----|----|------|
| 引用全部失效 | N1 critical | Critical | **一致：disqualifying** |
| 单种子 | N2 critical | Mentioned | **一致：critical limitation** |
| 无 figure | W4 warning | Significant weakness | **一致：major weakness** |
| Scalar gate 范围窄 | Noted in W2 context | Novelty limitation | **一致** |
| SS p≈0.07 | W5 warning | Too weak | **一致** |
| Llama 缺 Uniform Gate | W1 warning | "Ambiguous on Llama" | **一致** |
| Overall | 3.0 ARR / 3 (6pt) | 3/6 (Weak Reject) | **一致：Weak Reject → Borderline Findings** |

**标题问题存在分歧**——我读到 "Cannot"（需要弱化），R2 认为 "Struggles to" 是合理的。请 Director 确认版本。


---

[Reviewer 1 审稿结果]:
交叉回应已提交。核心结论：与 R2 在所有主要问题上达成共识（引用失效、单种子、无 figure、scope 窄、SS 统计功效不足），Overall 均为 Weak Reject / Borderline Findings。唯一分歧是标题用词（"Cannot" vs "Struggles to"），需 Director 确认审阅版本。

---

[Reviewer 2 审稿意见]:

# Reviewer 2 最终评估（Post-Convergence）

---

## 对 Director 收敛讨论的回应

### 对 R1 问题回应的补充意见

**"First quantitative measurement" claim**: Director 的判断——"partially justified, novelty in measurement not mechanism"——我部分同意但倾向更严格。原因：量化本身的价值取决于量化结果是否出乎意料。如果 exposure bias 文献已经让我们预期 teacher-forcing 下训练的 auxiliary loss 会在 autoregressive inference 时大幅衰减，那么 30× 这个具体数字的信息量是有限的。它告诉我们"衰减很严重"，但并未改变我们的 prior belief。相比之下，如果量化结果是"gap 仅为 1.2×"，那才是真正意外的发现。我维持 N1 的判断：这是 confirmatory quantification，novelty 有限。

**范围问题**: 完全同意 Director 的分析。我补充一个角度——即使在标量门控这个窄范围内，论文也只测试了一种初始化策略（gate 初始化为 0，即 ReZero）。如果初始化为 0.5（让门控从"半开"开始而非"全关"），或者用 learnable sigmoid gating（输出在 [0,1] 之间），行为可能不同。"最简单配置的最简单变体"不足以代表一个类别。

**Workshop vs. Main Conference**: 同意 Director 的定位——当前状态接近 workshop paper。我想强调一点：修复引用和加图表是 necessary but not sufficient。即使这些 presentation 问题全部修复，核心 novelty 限制仍在。补充 gradient surgery baseline（如 PCGrad）并展示其也无法解决问题，才是从 workshop 升级到 Findings 的关键路径。

### 与 R1 的共识确认

完全同意 Director 总结的四个共识点。我对每个共识的信心度：

1. **Qwen 方法论合理 / Llama 较弱** — 高信心。4-way vs 3-way 消融的不对称性是客观事实。
2. **Bootstrap CI 正确且诚实** — 高信心。统计方法本身无误。
3. **零图表是 #2 问题** — 高信心。R1 首先发现此问题，我在交叉回应中已采纳。对于 "mechanistic analysis" 论文，Figure 0 是不可接受的。
4. **v1–v7 loss 设计欠文档** — 中等信心。这可能是 Appendix 空间限制的结果，但论文有 ~2 页未使用的正文空间，没有理由不补充。

### 补充细微差异

**Soundness 3.5/6 (R1) vs 2.5/5 ARR (R2)**: 这两个评分在不同量表上大致对齐。R1 的 3.5/6 ≈ 58%，我的 2.5/5 = 50%。差异来源：我更重视 multi-task gradient conflict 文献的缺失（N4）——如果论文声称梯度竞争是核心机制但不引用该领域成熟方法，这直接影响 soundness 而不仅是 related work completeness。R1 可能将此归入 significance 而非 soundness。

**Downstream validation (r=0.72)**: 同意 Director 的正面评价。许多 negative result 论文完全不提供 proxy metric 的外部验证。r=0.72 虽然 moderate，但至少建立了 GAR 与实际任务性能之间的联系。这是论文的一个相对优势。

---

## R2 最终评分

| 维度 | 初次评分 | 交叉回应后 | 最终评分 | 变化理由 |
|------|----------|------------|----------|----------|
| **Novelty** (6-pt) | 2/6 | 2/6 | **2.5/6** | Director 指出"specific 30× gap number is indeed new"有一定道理。从 2 上调至 2.5，承认在特定领域的量化贡献，但不改变"已知机制的组合应用"判断 |
| **Significance** (6-pt) | 2/6 | 2/6 | **2.5/6** | 考虑到 downstream validation 和诚实的 hedging，略微上调。但 "no convincing positive path forward" 的限制仍在 |
| **Clarity** (6-pt) | 4/6 → 3/6 | 3/6 | **3/6** | 零图表+引用问题（如果提交版确实坏了）。纯文字叙事质量本身是 4/6，但 presentation 问题拉低 |
| **Soundness** (ARR) | 3/5 → 2.5/5 | 2.5/5 | **2.5/5** | 维持。单种子+不对称消融+零图表 = 部分主要 claims 支撑不足 |
| **Excitement** (ARR) | 2/5 | 2/5 | **2/5** | 维持。确认性结果，有限的惊喜度 |
| **Overall** (ARR) | 2.5/5 | 2.5/5 | **2.5/5 — Borderline Findings** | 维持 |
| **Overall** (6-pt) | 3/6 | 3/6 | **3/6 — Weak Reject** | 维持 |

---

## 与 Director 评分的对齐

Director 最终给出 Novelty 3/6, Significance 3/6, Clarity 3/6, Overall 3/6。

我的最终评分（Novelty 2.5, Significance 2.5, Clarity 3, Overall 3）略低于 Director 在 Novelty 和 Significance 上。差异来源：

- **Novelty**: 我对 "composition of known mechanisms" 的 novelty discount 更大。Director 认可 "new quantification in specific domain" 的价值，我承认但认为这个价值更小。半分差异（3 vs 2.5）反映了对 confirmatory vs. novel 的不同权重。
- **Significance**: Director 说 "informative but narrow; no convincing positive path forward"——我完全同意这个描述，但我从中推导出的分数更低，因为 "no positive path forward" 对负面结果论文的价值是致命的。好的负面结果论文不仅说"这不行"，还要指明"什么可能行"。本文的 §7 Discussion 仅给出模糊的 future directions（inference-time intervention、decoupled goal processing），缺乏具体的实验路径。

**结论**: R1 (3/6)、R2 (3/6)、Director (3/6) 三方 Overall 评分一致为 Weak Reject。这个共识是稳固的。

---

## 给作者的建设性修改路径（如果选择重投）

按优先级排序：

1. **[必须] 修复引用** — 如果提交版引用全坏，这是 desk reject 级别问题。检查 natbib/biblatex 编译链。
2. **[必须] 加图表** — 至少 3 张：(a) training curve（GAR + NTP loss 随 epoch 变化，展示三阶段），(b) attention heatmap（base model vs ThreadGate，展示 GAR 衰减），(c) per-layer gradient conflict 热力图。
3. **[强烈建议] 加 gradient surgery baseline** — 用 PCGrad 或 GradNorm 平衡 NTP-GAR 梯度，报告结果。如果 gap 仍在 → 论文 novelty 大幅提升（"即使消除梯度竞争，exposure bias 仍然致命"）；如果 gap 缩小 → 论文的 insight 变为"梯度竞争是可解的，真正的瓶颈是 exposure bias"。
4. **[建议] 扩展门控变体** — 至少加一种 vector gate 或 head-specific gate。如果也失败，结论说服力倍增。
5. **[建议] 多种子训练** — 至少 2-3 个种子，报告均值±标准差。
6. **[建议] 修正标题** — "Cannot" → "Fails to" 或更具体的 "Why Scalar Residual Gating Fails to..."
7. **[建议] 补充 multi-task gradient conflict 文献** — §2 增加子节，定位本文在该领域的位置。
8. **[可选] Llama 对称消融** — 加上 Uniform Gate 条件使两模型消融对齐。
9. **[可选] Scheduled sampling 在 Llama 上验证** — 增强 Contribution 4 的泛化性。

如果完成 1-4 项，论文大概率可达 Findings 水平（ARR 3.0）。如果 1-7 项全部完成且 gradient surgery baseline 给出有趣结果，可能触及 Borderline Conference（ARR 3.5）。


---

[Reviewer 1 审稿意见]:

# R1 Final Assessment (Post-Convergence)

---

## 对 Director 收敛讨论的回应

### 1. R2 问题的最终立场

**Single-seed**: 同意 Director 的框架——bootstrap 处理 eval variance 而非 training variance。我补充一点：论文 Table 2 中 4 个不同配置收敛到相似 GAR（0.013-0.016），这提供了间接的稳定性信号，但不等于 multi-seed 验证。最终判断：**genuine limitation, 论文 underestimates it**，与 Director 一致。

**4-way ablation**: 同意 "adequate for Qwen, missed opportunity on Llama" 的判断。我此前将 Llama 缺 Uniform Gate 列为 W1 (warning) 而非 critical，与 Director "not fatal" 的定性一致。

**GAR validation**: Director 提到 r=0.72，我在 PDF 中读到的是 r=0.82（Section 6.5）。无论是 0.72 还是 0.82，我同意 "acceptable as face validity but not strong enough to fully establish GAR as a proxy" 的判断。论文在 Discussion 中承认了这一局限，但可以更明确。

### 2. 与 R2 的共识确认

以下几点 R1-R2 完全一致，我无异议：

- 引用失效 = disqualifying（R1-N1, R2 同意）
- 无 figure = critical weakness（R1-W4, R2 同意）
- Novelty moderate = 已知概念在新 setting 的量化应用
- 范围窄但论文诚实——scope 限制在 Discussion 中有讨论

### 3. 细微分歧的最终立场

**Clarity 评分拆分**: 同意 Director 的 nuance。R2 给 2.5/6 偏低是因为把 formatting issues 和 prose quality 混在一起。论文的行文逻辑清晰、claim 表述有节制（"this is not a bug" 的 framing, Limitations section 的坦诚）。如果拆分：
- Prose clarity: 4/6（逻辑清楚、结构合理、claim 有边界）
- Presentation: 2/6（引用失效、零 figure、table numbering 可能冲突）
- 综合 Clarity: **3/6**（prose 拉不回 presentation 的硬伤）

**"First quantitative measurement" claim**: 这是论文最有说服力的贡献定位。如果 dongre2026 确实存在且是第一篇量化 GAR 退化的工作，那本文是第一篇量化 "修复尝试为何失败" 的工作——这是有价值的。但这依赖 dongre2026 的真实性和可验证性（我的 N1 中标记了该引用在 OpenAlex 未找到）。

**标题问题结论**: 经过交叉审阅，我确认 PDF 标题为 "Cannot Fix"。如果论文最终版确实用 "Cannot"，这与 Director 汇总中提到的 "Struggles to" 不一致。无论哪个版本，"Cannot" 对单种子证据来说过强，"Struggles to" 更合适。

---

## R1 最终评分（Post-Convergence）

我基本接受 Director 的收敛评分，有微调：

| 维度 | R1 初始 | Director 建议 | R1 最终 | 变化理由 |
|------|---------|--------------|---------|----------|
| Soundness | 3/6 | 3.5/6 | **3.5/6** | 接受上调——方法论思路确实 solid（4-way ablation、scheduled sampling causal design），缺陷在执行层面（seed/sample size）而非设计层面 |
| Significance | 4/6 | 3/6 | **3/6** | 接受下调——重新评估后，narrow scope + 无 positive path forward 确实限制了 significance |
| Clarity | 2/6 | 3/6 | **3/6** | 接受上调——区分 prose quality (good) vs presentation (broken) 是合理的 |
| **Overall** | **3/6** | **3/6** | **3/6 (Weak Reject)** | 维持不变 |

**ARR 维度映射**:

| ARR 维度 | 分数 | 说明 |
|----------|------|------|
| Soundness | 3/5 (Acceptable) | 主要 claim 有支撑，但 single-seed + small sample 留下缺口 |
| Excitement | 2.5/5 | 介于 "Potentially Interesting" 和 "Interesting" 之间 |
| Overall Assessment | **2.5-3.0** (Borderline Findings to Findings) | 当前状态 2.5；修复引用+补 figure 后可达 3.0 |
| Confidence | 4/5 | 实验方法论在专业领域内 |

---

## 最终弱点排序（与 Director 一致）

1. **ALL references broken** — 投稿级 disqualifying issue
2. **Zero figures** — 机制分析论文无可视化，严重影响说服力
3. **Single-seed training** — 负面结果论文需要更高的证据标准
4. **Asymmetric experiments** — Llama 缺 Uniform Gate, SS 仅在 Qwen 测试
5. **No code/data release** — 可复现性的最后一道防线也缺失

## 最终建议

**Revision path to Findings (3.0)**:
1. 修复 bibtex 编译，清理 bib 条目
2. 增加 2-3 张 key figures（训练曲线、attention heatmap、gate 分布）
3. 至少 3 个 seed 的 mean±std
4. 报告所有 λ 值和 loss component 定义

**Revision path to Borderline Conference (3.5)**:
- 以上全部 + Llama Uniform Gate + λ_GAR sensitivity + SS ratio sweep + 更大评估集

---

*R1 审稿完成。如需进一步讨论特定问题，随时可以继续。*


---

[Reviewer 2 审稿结果]:
最终评估已提交。三轮审稿总结：

- **Overall: 3/6 (Weak Reject) / ARR 2.5 (Borderline Findings)**
- R1、R2、Director 三方 Overall 一致为 Weak Reject
- 核心问题排序：(1) 引用全坏 (2) 零图表 (3) novelty 有限（已知机制的组合应用）(4) 范围过窄（仅标量门控）(5) 无统计显著的正面缓解方案
- 给出了 9 项优先级排序的修改建议，完成前 4 项可望达到 Findings 水平

---

[Reviewer 1 审稿结果]:
R1 最终审稿报告已提交。最终评分 Overall 3/6 (Weak Reject)，ARR Overall Assessment 2.5-3.0 (Borderline Findings)。核心问题排序：引用失效 > 零 figure > 单种子 > 实验不对称 > 无代码发布。给出了 Findings (3.0) 和 Borderline Conference (3.5) 两条修改路径。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 48 · 2026-05-19T15:44:54.009713+00:00_

called mcp__agent-ml-research__get_visual_check_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_visual_check_status</summary>

```json
{
  "project": "turn_residual_gating"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "tool_args": {
    "project": "turn_residual_gating"
  }
}
```

</details>

---


### Tool result

_source line 49 · 2026-05-19T15:44:54.060250+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 50 · 2026-05-19T15:45:00.284495+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__submit_review_report_to_research_director",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__submit_review_report_to_research_director",
    "max_results": "2"
  }
}
```

</details>

---


### Tool result

_source line 51 · 2026-05-19T15:45:00.284965+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 52 · 2026-05-19T15:46:21.144269+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "turn_residual_gating",
  "issues_yaml": "\n# Review Issues Tracker — turn_residual_gating\n# Round 1 (2026-05-19)\n\n- id: \"R1-N1\"\n  summary: \"所有引用渲染为 '?'——bibliography 编译失败，37 处引用不可读\"\n  category: format\n  severity: critical\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"R1 首先发现并做了引用审计（3 条 OpenAlex 未找到、5 条 author/year 不匹配、4 条 orphan entries）；R2 交叉回应 [AGREE]。双方一致认定为 disqualifying issue。\"\n  action_items:\n    - round: 1\n      action: \"修复 bibtex/biber 编译流程，确保所有 \\\\citep/\\\\citet 正确渲染\"\n      assigned_to: author\n      status: open\n    - round: 1\n      action: \"清理 5 处 author/year 不匹配和 4 条 orphan bib entries\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-N2\"\n  summary: \"单种子 (seed=42) 支撑 'Cannot' 级别绝对否定——无法排除 seed 偶然性\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"R1 列为 Must-Fix，R2 交叉回应 [AGREE]。共识：bootstrap CI 仅覆盖 eval variance 不覆盖 training variance，负面结果论文需更高证据标准。\"\n  action_items:\n    - round: 1\n      action: \"至少 3 个 seed 训练，报告 mean±std\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-N3\"\n  summary: \"评估样本量过小（50 conversations），Cohen's d≈0.22 统计功效不足\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1]\n      note: \"Bootstrap 10K resamples 无法弥补 n=50 本身偏小的问题。Scheduled sampling p≈0.07 在 α=0.05 下不显著。\"\n  action_items:\n    - round: 1\n      action: \"增加评估样本到 200-500 conversations 或提供 power analysis\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-N4\"\n  summary: \"损失函数超参数（λ_GAR, λ_div）和 v1-v6 配置定义缺失——无法复现\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"R1 列为 Must-Fix，R2 交叉回应 [AGREE]。7 个 loss 配置仅报告 v7，读者无法判断是否 cherry-picking。\"\n  action_items:\n    - round: 1\n      action: \"正文报告 λ_GAR/λ_div 具体值；Appendix 列出 v1-v7 全部定义和结果\"\n      assigned_to: author\n      status: open\n    - round: 1\n      action: \"增加 λ_GAR 敏感性实验 (grid: 0.1, 0.5, 1.0, 5.0)\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-N1\"\n  summary: \"Novelty 声称过高——梯度竞争和 exposure bias 均为已知现象的直接应用\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"R2 列为 critical，R1 交叉回应 [AGREE]（novelty incremental）。共识：30× gap 数值是新的但 confirmatory quantification，不构成方法论贡献。\"\n  action_items:\n    - round: 1\n      action: \"将 contribution 从 'first measurement' 重新定位为 'first empirical demonstration in attention-steering context'\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-N2\"\n  summary: \"标题 'Cannot' 过度声称——证据仅支持 'fails to' under tested conditions\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"R2 首先提出，R1 在交叉回应中确认 PDF 标题为 'Cannot Fix'。共识：scheduled sampling 能部分缓解 (30×→12.3×) 直接反驳 'cannot'；仅测试标量门控一种变体不能支撑绝对否定。\"\n  action_items:\n    - round: 1\n      action: \"标题改为 'Why Lightweight Scalar Gating Fails to Fix...' 或类似弱化表述\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-N3\"\n  summary: \"核心先行工作 Dongre et al. (2026) 不可查证——OpenAlex similarity 仅 0.336\"\n  category: format\n  severity: critical\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"论文的整个动机链（GAR 定义、probe AUC baseline、27-48% drop 数据）依赖此引用。如果该文不存在或不可获取，实验框架基础悬空。\"\n  action_items:\n    - round: 1\n      action: \"确认 dongre2026 的可验证性（提供 arXiv/会议 URL），或自包含地重新定义 GAR 并独立验证\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-N4\"\n  summary: \"Related Work 缺失 multi-task gradient conflict 文献（GradNorm/PCGrad/CAGrad/Nash-MTL）\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"R2 列为 critical，R1 交叉回应 [AGREE]。论文 §6.1 核心机制正是 multi-task gradient conflict，但 §2 完全未讨论该领域成熟方法。如果 PCGrad 能解决梯度竞争，论文的'失败'可能仅因未使用正确优化策略。\"\n  action_items:\n    - round: 1\n      action: \"§2 增加 multi-task gradient conflict 子节；实验中加入至少一种 gradient surgery baseline（如 PCGrad）\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-W1\"\n  summary: \"Llama 上未测试 Uniform Gate——跨模型消融不对称（4-way vs 3-way）\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"R1 列为 Should-Fix，R2 交叉回应 [AGREE]。Uniform Gate 是排除 per-layer specialization 价值的关键对照。\"\n  action_items:\n    - round: 1\n      action: \"在 Llama 上补充 Uniform Gate 实验\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-W2\"\n  summary: \"无 λ_GAR 敏感性消融——仅一个 λ 值不能支撑 'gating 本质上不行' 的结论\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1]\n      note: \"梯度冲突严重程度直接取决于 λ_GAR 大小。如果 λ_GAR 增大 10 倍使 NTP:GAR ratio 降到 ~1×，行为可能完全不同。\"\n  action_items:\n    - round: 1\n      action: \"测试 λ_GAR ∈ {0.1, 0.5, 1.0, 5.0} 的 grid\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-W3\"\n  summary: \"训练数据量（1,000 conversations）可能是混淆变量\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1]\n      note: \"1,000 conversations 对 7B 模型 LoRA 微调偏少，gate 可能未学到 robust 模式。Limitations 未讨论。\"\n  action_items:\n    - round: 1\n      action: \"增加数据量到 5K-10K 或在 Discussion 中明确讨论为何 1,000 足够\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-W4\"\n  summary: \"全文零 figure——机制分析论文无注意力热力图、训练曲线、gate 分布可视化\"\n  category: writing\n  severity: critical\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"R1 首先发现，R2 交叉回应称'这是我遗漏的重要观察'并升级为 major weakness。共识：标题含 'Mechanistic Analysis' 但 0 figure 是不可接受的。至少需要 attention heatmap、training curve、gate distribution。\"\n  action_items:\n    - round: 1\n      action: \"增加至少 3 张图：(a) training curve (b) attention heatmap (c) per-layer gradient/gate 分布\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-W5\"\n  summary: \"Scheduled sampling 因果推断局限——p≈0.07 不显著，仅测试单一 SS ratio 和单模型\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"R1 列为 Should-Fix，R2 [AGREE]。SS 对 PPL 影响未报告；仅 Qwen 未在 Llama 验证；仅 50% ratio。\"\n  action_items:\n    - round: 1\n      action: \"测试 SS ratio ∈ {25%, 50%, 75%, 100%}，报告 SS 对 PPL 影响，在 Llama 上验证\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-W6\"\n  summary: \"Reverse turn conditioning（§6.2）证据间接——gate attenuation 仅 2-7%，无显著性检验\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1]\n      note: \"Gate mean 93-98%（接近 1.0），2-7% attenuation 范围内的差异可能是数值噪声。\"\n  action_items:\n    - round: 1\n      action: \"对 per-layer gate difference 进行 paired test，报告 effect size\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-W1\"\n  summary: \"范围过窄——仅标量门控，不足以支撑 'lightweight gating' 的一般性结论\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"共识。未测试 vector gate、head-specific gate、low-rank gate 等变体。论文仅覆盖约 20% 的 lightweight gating 假设空间。\"\n  action_items:\n    - round: 1\n      action: \"至少补充 1-2 种门控变体（如 vector gate 或 head-specific gate）\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-W3\"\n  summary: \"GAR 作为唯一注意力退化指标的局限性未充分讨论\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"R2 提出，R1 在交叉回应中讨论了 r=0.82 的下游验证局限。共识：GAR 通过了 sanity check 但不足以作为 gold-standard proxy。\"\n  action_items:\n    - round: 1\n      action: \"Discussion 中明确讨论 GAR 的 construct validity 局限；如可能增加替代指标\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-W5\"\n  summary: \"liu2016attention 引用可能错配——语音识别 vs 注意力引导\"\n  category: format\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [2]\n      note: \"Bib 条目标题是 'Attention-Based Models for Speech Recognition'，但在 §2 中被引用为 attention supervision 方法。First author 不匹配。\"\n  action_items:\n    - round: 1\n      action: \"核实并替换为正确的参考文献\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-W6\"\n  summary: \"4 个 orphan bib 条目未被引用（vaswani2017, elhage2021, olsson2022, efron1994）\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"其中 vaswani2017 和 elhage2021/olsson2022 与论文主题直接相关，应在正文中引用或清理。\"\n  action_items:\n    - round: 1\n      action: \"清理 bib 文件：移除未引用条目或在正文中引用\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-MISC\"\n  summary: \"无代码/数据发布——negative result 论文的可复现性最后防线缺失\"\n  category: format\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"R1 在 Reproducibility 维度给 2/5。对于声称某方法'不可行'的论文，读者需要验证负面结果不是实现 bug。\"\n  action_items:\n    - round: 1\n      action: \"提供代码和数据（或至少核心训练/评估脚本）\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "turn_residual_gating",
    "issues_yaml": "\n# Review Issues Tracker — turn_residual_gating\n# Round 1 (2026-05-19)\n\n- id: \"R1-N1\"\n  summary: \"所有引用渲染为 '?'——bibliography 编译失败，37 处引用不可读\"\n  category: format\n  severity: critical\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"R1 首先发现并做了引用审计（3 条 OpenAlex 未找到、5 条 author/year 不匹配、4 条 orphan entries）；R2 交叉回应 [AGREE]。双方一致认定为 disqualifying issue。\"\n  action_items:\n    - round: 1\n      action: \"修复 bibtex/biber 编译流程，确保所有 \\\\citep/\\\\citet 正确渲染\"\n      assigned_to: author\n      status: open\n    - round: 1\n      action: \"清理 5 处 author/year 不匹配和 4 条 orphan bib entries\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-N2\"\n  summary: \"单种子 (seed=42) 支撑 'Cannot' 级别绝对否定——无法排除 seed 偶然性\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"R1 列为 Must-Fix，R2 交叉回应 [AGREE]。共识：bootstrap CI 仅覆盖 eval variance 不覆盖 training variance，负面结果论文需更高证据标准。\"\n  action_items:\n    - round: 1\n      action: \"至少 3 个 seed 训练，报告 mean±std\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-N3\"\n  summary: \"评估样本量过小（50 conversations），Cohen's d≈0.22 统计功效不足\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1]\n      note: \"Bootstrap 10K resamples 无法弥补 n=50 本身偏小的问题。Scheduled sampling p≈0.07 在 α=0.05 下不显著。\"\n  action_items:\n    - round: 1\n      action: \"增加评估样本到 200-500 conversations 或提供 power analysis\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-N4\"\n  summary: \"损失函数超参数（λ_GAR, λ_div）和 v1-v6 配置定义缺失——无法复现\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"R1 列为 Must-Fix，R2 交叉回应 [AGREE]。7 个 loss 配置仅报告 v7，读者无法判断是否 cherry-picking。\"\n  action_items:\n    - round: 1\n      action: \"正文报告 λ_GAR/λ_div 具体值；Appendix 列出 v1-v7 全部定义和结果\"\n      assigned_to: author\n      status: open\n    - round: 1\n      action: \"增加 λ_GAR 敏感性实验 (grid: 0.1, 0.5, 1.0, 5.0)\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-N1\"\n  summary: \"Novelty 声称过高——梯度竞争和 exposure bias 均为已知现象的直接应用\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"R2 列为 critical，R1 交叉回应 [AGREE]（novelty incremental）。共识：30× gap 数值是新的但 confirmatory quantification，不构成方法论贡献。\"\n  action_items:\n    - round: 1\n      action: \"将 contribution 从 'first measurement' 重新定位为 'first empirical demonstration in attention-steering context'\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-N2\"\n  summary: \"标题 'Cannot' 过度声称——证据仅支持 'fails to' under tested conditions\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"R2 首先提出，R1 在交叉回应中确认 PDF 标题为 'Cannot Fix'。共识：scheduled sampling 能部分缓解 (30×→12.3×) 直接反驳 'cannot'；仅测试标量门控一种变体不能支撑绝对否定。\"\n  action_items:\n    - round: 1\n      action: \"标题改为 'Why Lightweight Scalar Gating Fails to Fix...' 或类似弱化表述\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-N3\"\n  summary: \"核心先行工作 Dongre et al. (2026) 不可查证——OpenAlex similarity 仅 0.336\"\n  category: format\n  severity: critical\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"论文的整个动机链（GAR 定义、probe AUC baseline、27-48% drop 数据）依赖此引用。如果该文不存在或不可获取，实验框架基础悬空。\"\n  action_items:\n    - round: 1\n      action: \"确认 dongre2026 的可验证性（提供 arXiv/会议 URL），或自包含地重新定义 GAR 并独立验证\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-N4\"\n  summary: \"Related Work 缺失 multi-task gradient conflict 文献（GradNorm/PCGrad/CAGrad/Nash-MTL）\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"R2 列为 critical，R1 交叉回应 [AGREE]。论文 §6.1 核心机制正是 multi-task gradient conflict，但 §2 完全未讨论该领域成熟方法。如果 PCGrad 能解决梯度竞争，论文的'失败'可能仅因未使用正确优化策略。\"\n  action_items:\n    - round: 1\n      action: \"§2 增加 multi-task gradient conflict 子节；实验中加入至少一种 gradient surgery baseline（如 PCGrad）\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-W1\"\n  summary: \"Llama 上未测试 Uniform Gate——跨模型消融不对称（4-way vs 3-way）\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"R1 列为 Should-Fix，R2 交叉回应 [AGREE]。Uniform Gate 是排除 per-layer specialization 价值的关键对照。\"\n  action_items:\n    - round: 1\n      action: \"在 Llama 上补充 Uniform Gate 实验\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-W2\"\n  summary: \"无 λ_GAR 敏感性消融——仅一个 λ 值不能支撑 'gating 本质上不行' 的结论\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1]\n      note: \"梯度冲突严重程度直接取决于 λ_GAR 大小。如果 λ_GAR 增大 10 倍使 NTP:GAR ratio 降到 ~1×，行为可能完全不同。\"\n  action_items:\n    - round: 1\n      action: \"测试 λ_GAR ∈ {0.1, 0.5, 1.0, 5.0} 的 grid\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-W3\"\n  summary: \"训练数据量（1,000 conversations）可能是混淆变量\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1]\n      note: \"1,000 conversations 对 7B 模型 LoRA 微调偏少，gate 可能未学到 robust 模式。Limitations 未讨论。\"\n  action_items:\n    - round: 1\n      action: \"增加数据量到 5K-10K 或在 Discussion 中明确讨论为何 1,000 足够\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-W4\"\n  summary: \"全文零 figure——机制分析论文无注意力热力图、训练曲线、gate 分布可视化\"\n  category: writing\n  severity: critical\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"R1 首先发现，R2 交叉回应称'这是我遗漏的重要观察'并升级为 major weakness。共识：标题含 'Mechanistic Analysis' 但 0 figure 是不可接受的。至少需要 attention heatmap、training curve、gate distribution。\"\n  action_items:\n    - round: 1\n      action: \"增加至少 3 张图：(a) training curve (b) attention heatmap (c) per-layer gradient/gate 分布\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-W5\"\n  summary: \"Scheduled sampling 因果推断局限——p≈0.07 不显著，仅测试单一 SS ratio 和单模型\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"R1 列为 Should-Fix，R2 [AGREE]。SS 对 PPL 影响未报告；仅 Qwen 未在 Llama 验证；仅 50% ratio。\"\n  action_items:\n    - round: 1\n      action: \"测试 SS ratio ∈ {25%, 50%, 75%, 100%}，报告 SS 对 PPL 影响，在 Llama 上验证\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-W6\"\n  summary: \"Reverse turn conditioning（§6.2）证据间接——gate attenuation 仅 2-7%，无显著性检验\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1]\n      note: \"Gate mean 93-98%（接近 1.0），2-7% attenuation 范围内的差异可能是数值噪声。\"\n  action_items:\n    - round: 1\n      action: \"对 per-layer gate difference 进行 paired test，报告 effect size\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-W1\"\n  summary: \"范围过窄——仅标量门控，不足以支撑 'lightweight gating' 的一般性结论\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"共识。未测试 vector gate、head-specific gate、low-rank gate 等变体。论文仅覆盖约 20% 的 lightweight gating 假设空间。\"\n  action_items:\n    - round: 1\n      action: \"至少补充 1-2 种门控变体（如 vector gate 或 head-specific gate）\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-W3\"\n  summary: \"GAR 作为唯一注意力退化指标的局限性未充分讨论\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"R2 提出，R1 在交叉回应中讨论了 r=0.82 的下游验证局限。共识：GAR 通过了 sanity check 但不足以作为 gold-standard proxy。\"\n  action_items:\n    - round: 1\n      action: \"Discussion 中明确讨论 GAR 的 construct validity 局限；如可能增加替代指标\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-W5\"\n  summary: \"liu2016attention 引用可能错配——语音识别 vs 注意力引导\"\n  category: format\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [2]\n      note: \"Bib 条目标题是 'Attention-Based Models for Speech Recognition'，但在 §2 中被引用为 attention supervision 方法。First author 不匹配。\"\n  action_items:\n    - round: 1\n      action: \"核实并替换为正确的参考文献\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-W6\"\n  summary: \"4 个 orphan bib 条目未被引用（vaswani2017, elhage2021, olsson2022, efron1994）\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"其中 vaswani2017 和 elhage2021/olsson2022 与论文主题直接相关，应在正文中引用或清理。\"\n  action_items:\n    - round: 1\n      action: \"清理 bib 文件：移除未引用条目或在正文中引用\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-MISC\"\n  summary: \"无代码/数据发布——negative result 论文的可复现性最后防线缺失\"\n  category: format\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"R1 在 Reproducibility 维度给 2/5。对于声称某方法'不可行'的论文，读者需要验证负面结果不是实现 bug。\"\n  action_items:\n    - round: 1\n      action: \"提供代码和数据（或至少核心训练/评估脚本）\"\n      assigned_to: author\n      status: open\n  resolution: \"\"\n  resolution_round: null\n"
  }
}
```

</details>

---


### Tool result

_source line 53 · 2026-05-19T15:46:21.246696+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_issues.yaml\", \"bytes\": 10183}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 102
}
```

</details>

---


### Tool call

_source line 54 · 2026-05-19T15:48:40.189733+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "project": "turn_residual_gating",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "weak reject",
  "review_chat_id": "oc_9287ee173cf15d688adcd081f5d861f5",
  "report": "\n# 圆桌审稿报告（Round 1）\n\n**论文**: \"Why Lightweight Gating Cannot Fix Multi-Turn Attention Degradation: A Mechanistic Analysis\"\n**Venue**: EMNLP 2026 via ACL Rolling Review\n**审稿人**: Reviewer 1（方法/实验）、Reviewer 2（Novelty/Related Work）\n**日期**: 2026-05-19\n\n---\n\n## Summary\n\n本文提出 ThreadGate——一种基于标量残差门控的轻量方法，试图通过辅助 GAR（Goal Attention Ratio）损失修复多轮对话中的注意力退化问题。在 Qwen-2.5-7B 和 Llama-3.1-8B 上的实验表明，尽管训练时 GAR 显著提升（0.48），推理时 GAR 仅为 0.016，产生约 30× 的训练-推理鸿沟。论文将此失败归因于两个机制：NTP-GAR 梯度竞争（NTP 梯度幅度 7-15× 主导 GAR）和 teacher-forcing 分布偏移（exposure bias）。Scheduled sampling 将 gap 从 30× 缩小至 12.3×（p≈0.07），提供了 exposure bias 作为主因的间接因果证据。\n\n---\n\n## Strengths\n\n**S1. 有价值的负面结果**：社区需要知道\"训练时优化 GAR 不等于推理时 GAR 提升\"。两个失败机制的归因（梯度竞争 + exposure bias）为后续工作提供了明确的避坑方向。[R1, R2 共识]\n\n**S2. 实验设计方法论规范**：Qwen 上的 4-way 消融（Base/LoRA-only/ThreadGate/Uniform Gate）有效隔离了各组件贡献。Uniform Gate 对照组证明 per-layer specialization 无额外增益，是消融设计亮点。Bootstrap CI（10K resamples）提供了统计保障的框架。[R1 主导发现]\n\n**S3. 跨模型方向一致性**：Qwen（30× gap, 67-79% conflict rate）和 Llama（26× gap, 65-56% conflict rate）的结果方向一致，增强了核心发现的可信度。[R1, R2 共识]\n\n**S4. 梯度冲突量化分析**：Table 6 的逐层、逐 epoch 梯度统计（conflict fraction、magnitude ratio）提供了比总体数字更丰富的机制证据，是论文最有说服力的分析。[R1, R2 共识]\n\n**S5. 诚实的学术 hedging**：§7 Discussion 坦承结果的范围限制，Contribution 4 用\"suggestive evidence\"而非断言，Limitations 部分明确了适用条件。[R2 主导发现]\n\n**S6. 清晰的叙事结构**：从问题定义（§1-3）→ 方法设计（§4）→ 负面结果（§5）→ 机制分析（§6）→ 缓解探索（§7）的逻辑链条连贯。[R2]\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**MF1. [format/critical] 所有引用渲染为 \"?\"——bibliography 编译失败** [R1-N1, R2 同意]\nPDF 中 37 处 \\citep/\\citet 均显示为 \"?\"。引用审计发现：3 条 bib 在 OpenAlex 未找到（含核心依赖 dongre2026）、5 条 author/year 不匹配、4 条 orphan entries。这是投稿级 disqualifying issue，审稿人无法验证任何基于先行工作的 claim。\n\n**MF2. [framing/critical] 标题 \"Cannot\" 过度声称** [R2-N2, R1 确认]\n标题使用绝对否定\"Cannot\"，但：(a) 仅测试标量 per-layer gate 一种变体；(b) scheduled sampling 将 gap 从 30× 降至 12.3×，说明训练策略变化即可部分修复；(c) §7 自己承认\"our findings are specific to lightweight residual gating with auxiliary GAR losses\"。标题的绝对性与证据范围严重不匹配。\n\n**MF3. [framing/critical] Novelty 声称过高——两个核心机制均为已知现象** [R2-N1, R1 同意]\n梯度竞争 = multi-task gradient conflict（GradNorm 2018, PCGrad 2020 已有成熟方案）；distribution shift = exposure bias（Bengio et al. 2015）。论文在 Abstract 声称\"first quantitative measurement\"，但量化一个预期现象的具体数值不构成方法论贡献。两位 Reviewer 共识：这是 confirmatory quantification，novelty 有限。\n\n**MF4. [framing/critical] Related Work 缺失 multi-task gradient conflict 关键文献** [R2-N4, R1 同意]\n§6.1 核心机制正是 multi-task gradient conflict，但 §2 完全未讨论 GradNorm/PCGrad/CAGrad/Nash-MTL。更关键的是，如果 PCGrad 能解决梯度竞争，论文的\"失败\"可能仅因未使用正确优化策略而非 gating 固有局限——缺少 gradient surgery baseline 使核心结论悬空。\n\n**MF5. [experiment/critical] 单种子 (seed=42) 支撑绝对否定 claim** [R1-N2, R2 同意]\n所有实验仅一次训练。Bootstrap CI 覆盖 eval variance 但不覆盖 training variance（权重初始化、batch shuffling、dropout）。对于声称\"不可能 work\"的论文，无法排除\"seed=7 下 gap 仅 5×\"的可能性。负面结果论文的证据标准应高于正面结果论文。\n\n**MF6. [experiment/critical] 评估样本量过小（50 conversations），统计功效不足** [R1-N3]\nCohen's d ≈ 0.22（小效应量）在 n=50 下 power 不足以区分\"真零效应\"与\"underpowered 假阴性\"。Scheduled sampling p≈0.07 在 α=0.05 下不显著但被列为正式 Contribution。\n\n**MF7. [method/critical] 损失函数超参数和 v1-v6 配置定义缺失** [R1-N4, R2 同意]\nλ_GAR、λ_div 具体数值从未报告；L_div 无数学定义；v1-v6 共 6 个 loss 变体完全无细节。读者无法判断 v7 是 principled selection 还是 cherry-picking，无法复现任何实验。\n\n**MF8. [format/critical] 核心先行工作 Dongre et al. (2026) 不可查证** [R2-N3, R1 同意]\n论文整个动机链（GAR 定义、probe AUC baseline、\"27-48% drop\"数据）依赖此引用，但 OpenAlex 查证 similarity score 仅 0.336，无法确认该文是否存在或已发表。如不可验证，实验框架基础悬空。\n\n### Should-Fix（影响评分但不一票否决）\n\n**SF1. [writing/critical] 全文零 figure——\"Mechanistic Analysis\" 论文无可视化** [R1-W4, R2 同意升级]\n9 个 table 的纯数值呈现无法替代 attention heatmap、training curve、gate distribution 等标准机制分析视觉证据。§6.3 声称\"attention heatmaps are visually indistinguishable\"但不展示让读者判断。R1 首先发现，R2 在交叉回应中承认遗漏并升级为 major weakness。\n\n**SF2. [experiment/warning] Llama 上未测试 Uniform Gate——跨模型消融不对称** [R1-W1, R2 同意]\nQwen 4-way vs Llama 3-way。Uniform Gate 是排除 per-layer specialization 价值的关键对照，Llama 缺失使跨模型声称不完整。\n\n**SF3. [method/warning] 范围过窄——仅标量门控不足以支撑 \"lightweight gating\" 一般性结论** [R2-W1, R1 同意]\n未测试 vector gate、head-specific gate、low-rank gate 等变体。论文仅覆盖约 20% 的 lightweight gating 假设空间。标题用泛称\"Lightweight Gating\"但证据仅针对最简单的标量变体。\n\n**SF4. [experiment/warning] 无 λ_GAR 敏感性消融** [R1-W2]\n梯度冲突严重程度直接取决于 λ_GAR 大小。仅一个 λ 值不能支撑\"本质上不行\"的结论。\n\n**SF5. [experiment/warning] Scheduled sampling 因果推断局限** [R1-W5, R2 同意]\n仅测试 50% ratio、仅 Qwen、p≈0.07 不显著、SS 对 PPL 影响未报告。Contribution 4 的支撑不足。\n\n**SF6. [experiment/warning] 训练数据量（1,000 conversations）可能是混淆变量** [R1-W3]\n对 7B 模型 LoRA 微调偏少，gate 可能未学到 robust 模式。Limitations 未讨论。\n\n**SF7. [method/warning] GAR 单指标依赖的局限性未充分讨论** [R2-W3, R1 同意]\n所有机制分析建立在 GAR 上。下游验证 r=0.82 通过 sanity check 但不足以建立 gold-standard proxy 地位。未讨论 GAR 的 construct validity 局限或替代指标。\n\n**SF8. [experiment/warning] Reverse turn conditioning 证据间接** [R1-W6]\nGate attenuation 仅 2-7%（mean 93-98%），无显著性检验，差异可能是数值噪声。\n\n**SF9. [format/warning] 无代码/数据发布** [R1, R2 共识]\n负面结果论文的可复现性尤为重要——读者需要验证负面结果非实现 bug。\n\n### Minor Issues\n\n- §1 \"probe AUC up to 0.98\" 基线和计算方法应在正文简述\n- §4.2 v1-v7 loss 选择过程仅一句带过\n- Table 1 \"Relative drop\" 行未明确标注基线\n- §5.5 Table 5 bootstrap CI 包含零，应更明确说明 ThreadGate 增量效果可能完全不存在\n- Abstract \"30× training-inference gap\" 表述有歧义（比值还是相对退化幅度）\n- 正文约 6 页，远低于 EMNLP long paper 8 页上限，有空间补充缺失内容\n- liu2016attention 引用可能错配（语音识别 vs 注意力引导）\n- 4 条 orphan bib 条目（vaswani2017, elhage2021, olsson2022, efron1994）\n- 无独立 Limitations section 标题（嵌入 §7 Discussion 内）\n- Appendix 表格编号可能与正文冲突\n\n---\n\n## Reviewer Consensus [AGREE]\n\n两位 Reviewer 在以下关键判断上完全一致：\n\n1. **引用全部失效是 disqualifying issue**——投稿级硬伤，必须修复\n2. **标题 \"Cannot\" overclaims**——证据仅支持 \"fails to\" under tested conditions\n3. **零 figure 是重大弱点**——\"Mechanistic Analysis\" 论文无可视化不可接受\n4. **单种子不足以支撑负面结论**——bootstrap CI 不覆盖 training variance\n5. **Novelty 有限**——两个核心机制是已知现象（gradient conflict + exposure bias）的组合应用\n6. **范围过窄**——仅标量门控不能代表 \"lightweight gating\" 类别\n7. **Overall 评分一致**：Weak Reject / Borderline Findings\n\n## Reviewer Divergence [REBUT]\n\n仅一处分歧（已在交叉回应中澄清）：\n\n- **标题版本问题**：R1 确认 PDF 标题为 \"Cannot Fix\"，R2 初审中提到 Director 描述的标题为 \"Struggles to Fix\"。经核实 PDF 原文使用 \"Cannot\"。分歧已消解——双方一致认为 \"Cannot\" 过强。\n\n---\n\n## Questions（需要作者澄清）\n\n1. Dongre et al. (2026) 是否已公开发表？请提供 arXiv 链接或会议接收确认。\n2. λ_GAR 和 λ_div 的具体数值是什么？v1-v6 的 loss 配置和关键结果？\n3. Goal token 的标注方式（手动/自动，position matching/语义匹配）？\n4. 是否考虑过 PCGrad 或 GradNorm 来缓解梯度竞争？如果是，结果如何？\n5. 在不同 seed 下 30× gap 是否稳定复现？\n6. Instruction compliance 的具体测量方式是什么（格式遵守 vs 语义遵循）？\n7. 引用编译失败是提交版本问题还是编译环境问题？\n\n---\n\n## Missing References\n\n以下文献与论文核心机制直接相关但完全未被引用：\n\n| 文献 | 相关性 |\n|------|--------|\n| GradNorm (Chen et al., ICML 2018) | 动态调整 loss 权重以平衡梯度幅度——直接对应 §6.1 梯度竞争 |\n| PCGrad (Yu et al., NeurIPS 2020) | 投影消除梯度方向冲突——§6.1 核心机制的已知解决方案 |\n| CAGrad (Liu et al., NeurIPS 2021) | 冲突感知梯度下降——multi-task gradient conflict 方向 |\n| Nash-MTL (Navon et al., ICML 2022) | 纳什博弈框架下的多任务优化 |\n| Ranzato et al. (2016), Wiseman & Rush (2016) | Exposure bias 在 sequence generation 中的量化先例 |\n\n已引用但讨论不足：\n- Li et al. (ITI, 2024) 和 Zou et al. (RepE, 2023)：推理时干预方法，绕过 exposure bias，是更有希望的替代方向，论文仅一句列举\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n**状态**：未请求。项目配置中未启用外部审稿（`external_review.paperreview_ai.enabled` 未配置）。\n\n---\n\n## Visual Layout Check（非评分项）\n\n**状态**：未启动。视觉审查 Agent 因 `review_paper_pdf_path` 未配置而派发失败。\n\n基于 Reviewer 观察的排版问题摘要：\n- 全文 0 figure（9 tables only）\n- 正文约 6 页，低于 EMNLP long paper 8 页上限\n- 引用全部显示为 \"?\"\n- Appendix 表格编号可能与正文冲突\n- 无独立 Limitations section 标题\n\n---\n\n## Overall Assessment\n\n### 评分汇总\n\n| 维度 | R1 最终 | R2 最终 | 综合 |\n|------|---------|---------|------|\n| **Soundness** (ARR 5-pt) | 3/5 | 2.5/5 | **2.5/5** |\n| **Excitement** (ARR 5-pt) | 2.5/5 | 2/5 | **2/5** |\n| **Reproducibility** (ARR 5-pt) | 2/5 | 3.5/5 | **2.5/5** |\n| **Soundness** (6-pt) | 3.5/6 | — | **3/6** |\n| **Novelty** (6-pt) | — | 2.5/6 | **2.5/6** |\n| **Significance** (6-pt) | 3/6 | 2.5/6 | **2.5/6** |\n| **Clarity** (6-pt) | 3/6 | 3/6 | **3/6** |\n| **Overall** (ARR 5-pt) | 2.5-3.0 | 2.5 | **2.5/5 — Borderline Findings** |\n| **Overall** (6-pt) | 3/6 | 3/6 | **3/6 — Weak Reject** |\n\n### 综合判断\n\n**ARR Overall Assessment: 2.5 / 5 — Borderline Findings**\n\n论文提出了一个合理的研究问题（轻量门控能否修复多轮注意力退化），实验设计框架（4-way 消融 + 跨模型验证 + scheduled sampling 因果测试）方法论思路正确，梯度冲突量化分析有信息价值。\n\n但论文有 8 个 critical 级别问题和 9 个 warning 级别问题。核心障碍：\n\n1. **格式硬伤**：引用全部失效 + 零 figure——即使内容过关，这两个 presentation 问题在 ARR 审稿中可能直接拉低 1-2 个 notch\n2. **Novelty 不足**：两个核心机制（gradient conflict + exposure bias）是已知现象的组合应用，缺少 multi-task gradient conflict 领域的关键文献和 baseline\n3. **证据不足以支撑 claim 强度**：标题\"Cannot\"与单种子、标量门控唯一变体、50 样本的证据范围严重不匹配\n4. **可复现性低**：关键超参未报告、核心引用不可查证、无代码发布\n\n**当前状态不满足 EMNLP 2026 Main Conference 接收标准（需 ≥4.0）。** Findings 接收（≥3.0）需要至少修复：引用编译、增加图表、多种子训练、报告全部超参。Borderline Conference（≥3.5）还需补充 gradient surgery baseline 和更多门控变体。\n\n### 修改路径\n\n**达到 Findings (3.0) 的最低要求**：\n1. 修复 bibtex 编译，清理引用\n2. 增加 2-3 张关键 figure（training curve、attention heatmap、gate distribution）\n3. 至少 3 个 seed 的 mean±std\n4. 报告所有 λ 值和 loss component 定义\n5. 修正标题：\"Cannot\" → \"Fails to\"\n\n**达到 Borderline Conference (3.5) 的路径**：\n- 以上全部 + gradient surgery baseline（PCGrad）+ 至少一种非标量门控变体 + Llama Uniform Gate + λ_GAR sensitivity sweep + 更大评估集\n\n### Reviewer 信心\n\n- R1 Confidence: 4/5（实验方法论在专业领域内）\n- R2 Confidence: 4/5（熟悉 exposure bias、multi-task optimization 和 transformer 机制分析文献）\n\n---\n\n## Detailed Comments\n\n### §1 Introduction\n- \"first quantitative measurement\" 声称需降级为 \"first empirical demonstration in the attention-steering context\"\n- \"probe AUC up to 0.98\" 需在正文简述计算方法\n- \"30× training-inference gap\" 表述有歧义，需精确定义\n\n### §2 Related Work\n- 完全缺失 multi-task gradient conflict 子节（GradNorm/PCGrad/CAGrad/Nash-MTL）\n- ITI 和 RepE 仅一句列举，应深入讨论为什么推理时方法可能更适合\n- liu2016attention 可能错配（语音识别 vs 注意力引导）\n\n### §3 Background\n- GAR 定义依赖 Dongre et al. (2026)，如该引用不可验证需自包含重新定义\n- Goal token 标注方式未说明\n\n### §4 Method\n- §4.1: 仅标量门控（ReZero 风格），未讨论为何不测试 vector gate 等变体\n- §4.2: λ_GAR、λ_div 数值缺失；L_div 无数学定义；v1-v6 无任何细节\n- §4.3: 1,000 conversations 是否足够未讨论\n\n### §5 Experiments\n- 单种子（seed=42）是核心限制\n- n=50 评估样本统计功效不足\n- Table 2 Qwen 4-way 设计好，Table 3 Llama 缺 Uniform Gate\n- Table 5 bootstrap CI 包含零——应更明确说明增量效果可能完全不存在\n\n### §6 Mechanistic Analysis\n- §6.1: 梯度竞争分析有价值（Table 6），但本质是 multi-task gradient conflict 的 re-discovery\n- §6.2: Reverse turn conditioning 证据间接（2-7% attenuation 无显著性检验）\n- §6.3: 声称 heatmaps \"visually indistinguishable\" 但不展示——需要图表\n- §6.4: Exposure bias 归因概念上预期；scheduled sampling p≈0.07 不显著\n- §6.5: 下游验证 r=0.82 通过 sanity check 但不充分\n\n### §7 Discussion\n- Hedging 诚实，但与标题/Abstract 的 overclaiming 不一致\n- Scheduled sampling 仅 Qwen、仅 50% ratio、PPL 影响未报告\n- Future directions 过于模糊，缺乏具体实验路径\n\n### 格式/呈现\n- 全文 0 figure，9 tables——机制分析论文不可接受\n- 引用全部失效（\"?\"）\n- 正文 ~6 页 vs EMNLP 8 页上限——有空间补充内容\n- 4 条 orphan bib entries\n- 无独立 Limitations section 标题\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "project": "turn_residual_gating",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "weak reject",
    "review_chat_id": "oc_9287ee173cf15d688adcd081f5d861f5",
    "report": "\n# 圆桌审稿报告（Round 1）\n\n**论文**: \"Why Lightweight Gating Cannot Fix Multi-Turn Attention Degradation: A Mechanistic Analysis\"\n**Venue**: EMNLP 2026 via ACL Rolling Review\n**审稿人**: Reviewer 1（方法/实验）、Reviewer 2（Novelty/Related Work）\n**日期**: 2026-05-19\n\n---\n\n## Summary\n\n本文提出 ThreadGate——一种基于标量残差门控的轻量方法，试图通过辅助 GAR（Goal Attention Ratio）损失修复多轮对话中的注意力退化问题。在 Qwen-2.5-7B 和 Llama-3.1-8B 上的实验表明，尽管训练时 GAR 显著提升（0.48），推理时 GAR 仅为 0.016，产生约 30× 的训练-推理鸿沟。论文将此失败归因于两个机制：NTP-GAR 梯度竞争（NTP 梯度幅度 7-15× 主导 GAR）和 teacher-forcing 分布偏移（exposure bias）。Scheduled sampling 将 gap 从 30× 缩小至 12.3×（p≈0.07），提供了 exposure bias 作为主因的间接因果证据。\n\n---\n\n## Strengths\n\n**S1. 有价值的负面结果**：社区需要知道\"训练时优化 GAR 不等于推理时 GAR 提升\"。两个失败机制的归因（梯度竞争 + exposure bias）为后续工作提供了明确的避坑方向。[R1, R2 共识]\n\n**S2. 实验设计方法论规范**：Qwen 上的 4-way 消融（Base/LoRA-only/ThreadGate/Uniform Gate）有效隔离了各组件贡献。Uniform Gate 对照组证明 per-layer specialization 无额外增益，是消融设计亮点。Bootstrap CI（10K resamples）提供了统计保障的框架。[R1 主导发现]\n\n**S3. 跨模型方向一致性**：Qwen（30× gap, 67-79% conflict rate）和 Llama（26× gap, 65-56% conflict rate）的结果方向一致，增强了核心发现的可信度。[R1, R2 共识]\n\n**S4. 梯度冲突量化分析**：Table 6 的逐层、逐 epoch 梯度统计（conflict fraction、magnitude ratio）提供了比总体数字更丰富的机制证据，是论文最有说服力的分析。[R1, R2 共识]\n\n**S5. 诚实的学术 hedging**：§7 Discussion 坦承结果的范围限制，Contribution 4 用\"suggestive evidence\"而非断言，Limitations 部分明确了适用条件。[R2 主导发现]\n\n**S6. 清晰的叙事结构**：从问题定义（§1-3）→ 方法设计（§4）→ 负面结果（§5）→ 机制分析（§6）→ 缓解探索（§7）的逻辑链条连贯。[R2]\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**MF1. [format/critical] 所有引用渲染为 \"?\"——bibliography 编译失败** [R1-N1, R2 同意]\nPDF 中 37 处 \\citep/\\citet 均显示为 \"?\"。引用审计发现：3 条 bib 在 OpenAlex 未找到（含核心依赖 dongre2026）、5 条 author/year 不匹配、4 条 orphan entries。这是投稿级 disqualifying issue，审稿人无法验证任何基于先行工作的 claim。\n\n**MF2. [framing/critical] 标题 \"Cannot\" 过度声称** [R2-N2, R1 确认]\n标题使用绝对否定\"Cannot\"，但：(a) 仅测试标量 per-layer gate 一种变体；(b) scheduled sampling 将 gap 从 30× 降至 12.3×，说明训练策略变化即可部分修复；(c) §7 自己承认\"our findings are specific to lightweight residual gating with auxiliary GAR losses\"。标题的绝对性与证据范围严重不匹配。\n\n**MF3. [framing/critical] Novelty 声称过高——两个核心机制均为已知现象** [R2-N1, R1 同意]\n梯度竞争 = multi-task gradient conflict（GradNorm 2018, PCGrad 2020 已有成熟方案）；distribution shift = exposure bias（Bengio et al. 2015）。论文在 Abstract 声称\"first quantitative measurement\"，但量化一个预期现象的具体数值不构成方法论贡献。两位 Reviewer 共识：这是 confirmatory quantification，novelty 有限。\n\n**MF4. [framing/critical] Related Work 缺失 multi-task gradient conflict 关键文献** [R2-N4, R1 同意]\n§6.1 核心机制正是 multi-task gradient conflict，但 §2 完全未讨论 GradNorm/PCGrad/CAGrad/Nash-MTL。更关键的是，如果 PCGrad 能解决梯度竞争，论文的\"失败\"可能仅因未使用正确优化策略而非 gating 固有局限——缺少 gradient surgery baseline 使核心结论悬空。\n\n**MF5. [experiment/critical] 单种子 (seed=42) 支撑绝对否定 claim** [R1-N2, R2 同意]\n所有实验仅一次训练。Bootstrap CI 覆盖 eval variance 但不覆盖 training variance（权重初始化、batch shuffling、dropout）。对于声称\"不可能 work\"的论文，无法排除\"seed=7 下 gap 仅 5×\"的可能性。负面结果论文的证据标准应高于正面结果论文。\n\n**MF6. [experiment/critical] 评估样本量过小（50 conversations），统计功效不足** [R1-N3]\nCohen's d ≈ 0.22（小效应量）在 n=50 下 power 不足以区分\"真零效应\"与\"underpowered 假阴性\"。Scheduled sampling p≈0.07 在 α=0.05 下不显著但被列为正式 Contribution。\n\n**MF7. [method/critical] 损失函数超参数和 v1-v6 配置定义缺失** [R1-N4, R2 同意]\nλ_GAR、λ_div 具体数值从未报告；L_div 无数学定义；v1-v6 共 6 个 loss 变体完全无细节。读者无法判断 v7 是 principled selection 还是 cherry-picking，无法复现任何实验。\n\n**MF8. [format/critical] 核心先行工作 Dongre et al. (2026) 不可查证** [R2-N3, R1 同意]\n论文整个动机链（GAR 定义、probe AUC baseline、\"27-48% drop\"数据）依赖此引用，但 OpenAlex 查证 similarity score 仅 0.336，无法确认该文是否存在或已发表。如不可验证，实验框架基础悬空。\n\n### Should-Fix（影响评分但不一票否决）\n\n**SF1. [writing/critical] 全文零 figure——\"Mechanistic Analysis\" 论文无可视化** [R1-W4, R2 同意升级]\n9 个 table 的纯数值呈现无法替代 attention heatmap、training curve、gate distribution 等标准机制分析视觉证据。§6.3 声称\"attention heatmaps are visually indistinguishable\"但不展示让读者判断。R1 首先发现，R2 在交叉回应中承认遗漏并升级为 major weakness。\n\n**SF2. [experiment/warning] Llama 上未测试 Uniform Gate——跨模型消融不对称** [R1-W1, R2 同意]\nQwen 4-way vs Llama 3-way。Uniform Gate 是排除 per-layer specialization 价值的关键对照，Llama 缺失使跨模型声称不完整。\n\n**SF3. [method/warning] 范围过窄——仅标量门控不足以支撑 \"lightweight gating\" 一般性结论** [R2-W1, R1 同意]\n未测试 vector gate、head-specific gate、low-rank gate 等变体。论文仅覆盖约 20% 的 lightweight gating 假设空间。标题用泛称\"Lightweight Gating\"但证据仅针对最简单的标量变体。\n\n**SF4. [experiment/warning] 无 λ_GAR 敏感性消融** [R1-W2]\n梯度冲突严重程度直接取决于 λ_GAR 大小。仅一个 λ 值不能支撑\"本质上不行\"的结论。\n\n**SF5. [experiment/warning] Scheduled sampling 因果推断局限** [R1-W5, R2 同意]\n仅测试 50% ratio、仅 Qwen、p≈0.07 不显著、SS 对 PPL 影响未报告。Contribution 4 的支撑不足。\n\n**SF6. [experiment/warning] 训练数据量（1,000 conversations）可能是混淆变量** [R1-W3]\n对 7B 模型 LoRA 微调偏少，gate 可能未学到 robust 模式。Limitations 未讨论。\n\n**SF7. [method/warning] GAR 单指标依赖的局限性未充分讨论** [R2-W3, R1 同意]\n所有机制分析建立在 GAR 上。下游验证 r=0.82 通过 sanity check 但不足以建立 gold-standard proxy 地位。未讨论 GAR 的 construct validity 局限或替代指标。\n\n**SF8. [experiment/warning] Reverse turn conditioning 证据间接** [R1-W6]\nGate attenuation 仅 2-7%（mean 93-98%），无显著性检验，差异可能是数值噪声。\n\n**SF9. [format/warning] 无代码/数据发布** [R1, R2 共识]\n负面结果论文的可复现性尤为重要——读者需要验证负面结果非实现 bug。\n\n### Minor Issues\n\n- §1 \"probe AUC up to 0.98\" 基线和计算方法应在正文简述\n- §4.2 v1-v7 loss 选择过程仅一句带过\n- Table 1 \"Relative drop\" 行未明确标注基线\n- §5.5 Table 5 bootstrap CI 包含零，应更明确说明 ThreadGate 增量效果可能完全不存在\n- Abstract \"30× training-inference gap\" 表述有歧义（比值还是相对退化幅度）\n- 正文约 6 页，远低于 EMNLP long paper 8 页上限，有空间补充缺失内容\n- liu2016attention 引用可能错配（语音识别 vs 注意力引导）\n- 4 条 orphan bib 条目（vaswani2017, elhage2021, olsson2022, efron1994）\n- 无独立 Limitations section 标题（嵌入 §7 Discussion 内）\n- Appendix 表格编号可能与正文冲突\n\n---\n\n## Reviewer Consensus [AGREE]\n\n两位 Reviewer 在以下关键判断上完全一致：\n\n1. **引用全部失效是 disqualifying issue**——投稿级硬伤，必须修复\n2. **标题 \"Cannot\" overclaims**——证据仅支持 \"fails to\" under tested conditions\n3. **零 figure 是重大弱点**——\"Mechanistic Analysis\" 论文无可视化不可接受\n4. **单种子不足以支撑负面结论**——bootstrap CI 不覆盖 training variance\n5. **Novelty 有限**——两个核心机制是已知现象（gradient conflict + exposure bias）的组合应用\n6. **范围过窄**——仅标量门控不能代表 \"lightweight gating\" 类别\n7. **Overall 评分一致**：Weak Reject / Borderline Findings\n\n## Reviewer Divergence [REBUT]\n\n仅一处分歧（已在交叉回应中澄清）：\n\n- **标题版本问题**：R1 确认 PDF 标题为 \"Cannot Fix\"，R2 初审中提到 Director 描述的标题为 \"Struggles to Fix\"。经核实 PDF 原文使用 \"Cannot\"。分歧已消解——双方一致认为 \"Cannot\" 过强。\n\n---\n\n## Questions（需要作者澄清）\n\n1. Dongre et al. (2026) 是否已公开发表？请提供 arXiv 链接或会议接收确认。\n2. λ_GAR 和 λ_div 的具体数值是什么？v1-v6 的 loss 配置和关键结果？\n3. Goal token 的标注方式（手动/自动，position matching/语义匹配）？\n4. 是否考虑过 PCGrad 或 GradNorm 来缓解梯度竞争？如果是，结果如何？\n5. 在不同 seed 下 30× gap 是否稳定复现？\n6. Instruction compliance 的具体测量方式是什么（格式遵守 vs 语义遵循）？\n7. 引用编译失败是提交版本问题还是编译环境问题？\n\n---\n\n## Missing References\n\n以下文献与论文核心机制直接相关但完全未被引用：\n\n| 文献 | 相关性 |\n|------|--------|\n| GradNorm (Chen et al., ICML 2018) | 动态调整 loss 权重以平衡梯度幅度——直接对应 §6.1 梯度竞争 |\n| PCGrad (Yu et al., NeurIPS 2020) | 投影消除梯度方向冲突——§6.1 核心机制的已知解决方案 |\n| CAGrad (Liu et al., NeurIPS 2021) | 冲突感知梯度下降——multi-task gradient conflict 方向 |\n| Nash-MTL (Navon et al., ICML 2022) | 纳什博弈框架下的多任务优化 |\n| Ranzato et al. (2016), Wiseman & Rush (2016) | Exposure bias 在 sequence generation 中的量化先例 |\n\n已引用但讨论不足：\n- Li et al. (ITI, 2024) 和 Zou et al. (RepE, 2023)：推理时干预方法，绕过 exposure bias，是更有希望的替代方向，论文仅一句列举\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n**状态**：未请求。项目配置中未启用外部审稿（`external_review.paperreview_ai.enabled` 未配置）。\n\n---\n\n## Visual Layout Check（非评分项）\n\n**状态**：未启动。视觉审查 Agent 因 `review_paper_pdf_path` 未配置而派发失败。\n\n基于 Reviewer 观察的排版问题摘要：\n- 全文 0 figure（9 tables only）\n- 正文约 6 页，低于 EMNLP long paper 8 页上限\n- 引用全部显示为 \"?\"\n- Appendix 表格编号可能与正文冲突\n- 无独立 Limitations section 标题\n\n---\n\n## Overall Assessment\n\n### 评分汇总\n\n| 维度 | R1 最终 | R2 最终 | 综合 |\n|------|---------|---------|------|\n| **Soundness** (ARR 5-pt) | 3/5 | 2.5/5 | **2.5/5** |\n| **Excitement** (ARR 5-pt) | 2.5/5 | 2/5 | **2/5** |\n| **Reproducibility** (ARR 5-pt) | 2/5 | 3.5/5 | **2.5/5** |\n| **Soundness** (6-pt) | 3.5/6 | — | **3/6** |\n| **Novelty** (6-pt) | — | 2.5/6 | **2.5/6** |\n| **Significance** (6-pt) | 3/6 | 2.5/6 | **2.5/6** |\n| **Clarity** (6-pt) | 3/6 | 3/6 | **3/6** |\n| **Overall** (ARR 5-pt) | 2.5-3.0 | 2.5 | **2.5/5 — Borderline Findings** |\n| **Overall** (6-pt) | 3/6 | 3/6 | **3/6 — Weak Reject** |\n\n### 综合判断\n\n**ARR Overall Assessment: 2.5 / 5 — Borderline Findings**\n\n论文提出了一个合理的研究问题（轻量门控能否修复多轮注意力退化），实验设计框架（4-way 消融 + 跨模型验证 + scheduled sampling 因果测试）方法论思路正确，梯度冲突量化分析有信息价值。\n\n但论文有 8 个 critical 级别问题和 9 个 warning 级别问题。核心障碍：\n\n1. **格式硬伤**：引用全部失效 + 零 figure——即使内容过关，这两个 presentation 问题在 ARR 审稿中可能直接拉低 1-2 个 notch\n2. **Novelty 不足**：两个核心机制（gradient conflict + exposure bias）是已知现象的组合应用，缺少 multi-task gradient conflict 领域的关键文献和 baseline\n3. **证据不足以支撑 claim 强度**：标题\"Cannot\"与单种子、标量门控唯一变体、50 样本的证据范围严重不匹配\n4. **可复现性低**：关键超参未报告、核心引用不可查证、无代码发布\n\n**当前状态不满足 EMNLP 2026 Main Conference 接收标准（需 ≥4.0）。** Findings 接收（≥3.0）需要至少修复：引用编译、增加图表、多种子训练、报告全部超参。Borderline Conference（≥3.5）还需补充 gradient surgery baseline 和更多门控变体。\n\n### 修改路径\n\n**达到 Findings (3.0) 的最低要求**：\n1. 修复 bibtex 编译，清理引用\n2. 增加 2-3 张关键 figure（training curve、attention heatmap、gate distribution）\n3. 至少 3 个 seed 的 mean±std\n4. 报告所有 λ 值和 loss component 定义\n5. 修正标题：\"Cannot\" → \"Fails to\"\n\n**达到 Borderline Conference (3.5) 的路径**：\n- 以上全部 + gradient surgery baseline（PCGrad）+ 至少一种非标量门控变体 + Llama Uniform Gate + λ_GAR sensitivity sweep + 更大评估集\n\n### Reviewer 信心\n\n- R1 Confidence: 4/5（实验方法论在专业领域内）\n- R2 Confidence: 4/5（熟悉 exposure bias、multi-task optimization 和 transformer 机制分析文献）\n\n---\n\n## Detailed Comments\n\n### §1 Introduction\n- \"first quantitative measurement\" 声称需降级为 \"first empirical demonstration in the attention-steering context\"\n- \"probe AUC up to 0.98\" 需在正文简述计算方法\n- \"30× training-inference gap\" 表述有歧义，需精确定义\n\n### §2 Related Work\n- 完全缺失 multi-task gradient conflict 子节（GradNorm/PCGrad/CAGrad/Nash-MTL）\n- ITI 和 RepE 仅一句列举，应深入讨论为什么推理时方法可能更适合\n- liu2016attention 可能错配（语音识别 vs 注意力引导）\n\n### §3 Background\n- GAR 定义依赖 Dongre et al. (2026)，如该引用不可验证需自包含重新定义\n- Goal token 标注方式未说明\n\n### §4 Method\n- §4.1: 仅标量门控（ReZero 风格），未讨论为何不测试 vector gate 等变体\n- §4.2: λ_GAR、λ_div 数值缺失；L_div 无数学定义；v1-v6 无任何细节\n- §4.3: 1,000 conversations 是否足够未讨论\n\n### §5 Experiments\n- 单种子（seed=42）是核心限制\n- n=50 评估样本统计功效不足\n- Table 2 Qwen 4-way 设计好，Table 3 Llama 缺 Uniform Gate\n- Table 5 bootstrap CI 包含零——应更明确说明增量效果可能完全不存在\n\n### §6 Mechanistic Analysis\n- §6.1: 梯度竞争分析有价值（Table 6），但本质是 multi-task gradient conflict 的 re-discovery\n- §6.2: Reverse turn conditioning 证据间接（2-7% attenuation 无显著性检验）\n- §6.3: 声称 heatmaps \"visually indistinguishable\" 但不展示——需要图表\n- §6.4: Exposure bias 归因概念上预期；scheduled sampling p≈0.07 不显著\n- §6.5: 下游验证 r=0.82 通过 sanity check 但不充分\n\n### §7 Discussion\n- Hedging 诚实，但与标题/Abstract 的 overclaiming 不一致\n- Scheduled sampling 仅 Qwen、仅 50% ratio、PPL 影响未报告\n- Future directions 过于模糊，缺乏具体实验路径\n\n### 格式/呈现\n- 全文 0 figure，9 tables——机制分析论文不可接受\n- 引用全部失效（\"?\"）\n- 正文 ~6 页 vs EMNLP 8 页上限——有空间补充内容\n- 4 条 orphan bib entries\n- 无独立 Limitations section 标题\n"
  }
}
```

</details>

---


### Tool result

_source line 55 · 2026-05-19T15:48:44.750120+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_640e53b6afbbd5e34eb7273cd5a707a0:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4560
}
```

</details>

---


### Assistant

_source line 56 · 2026-05-19T15:48:55.672311+00:00_

审稿报告已投递至 Research Director。

**圆桌审稿总结**：

- **参与审稿人**：R1（方法/实验）、R2（Novelty/Related Work），完成 1 轮独立审稿 + 交叉回应，所有关键问题达成共识
- **Overall**：**ARR 2.5/5（Borderline Findings）/ 6-pt 3/6（Weak Reject）**
- **8 个 critical 问题**：引用全坏、标题 overclaim、novelty 有限（已知机制组合应用）、缺失 gradient conflict 文献、单种子、样本量不足、超参缺失、核心引用不可查证
- **9 个 warning 问题**：零 figure、Llama 消融不对称、门控范围窄、无 λ 敏感性、SS 因果推断弱、数据量混淆、GAR 单指标局限、reverse conditioning 证据间接、无代码发布
- **修改路径**：修复引用 + 加图 + 多种子 + 报告超参 → Findings（3.0）；再加 gradient surgery baseline + 门控变体 → Borderline Conference（3.5）

Issue Tracker 已同步写入 `artifacts/review_issues.yaml`（20 条 issue）。外部审稿未配置，视觉审查因 PDF 路径未配置未启动。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director"
}
```

</details>

---


## Round 4

## Round 4

2 recorded events


### User

_source line 57 · 2026-05-19T15:48:56.732933+00:00_

[Reviewer 1 审稿意见]:

# R1 对 R2 完整审稿意见的逐条交叉回应

---

## Must-Fix 问题回应

### [AGREE with nuance] R2-N1: Novelty 声称过高——两个核心机制均为已知现象的直接应用

R2 的核心论点成立：NTP-GAR 梯度竞争是 multi-task gradient conflict 的实例，exposure bias 是已知问题。论文确实缺少 GradNorm/PCGrad/CAGrad 等关键引用。

**但我补充一个 nuance**：论文的贡献定位应该是 "在 residual gating + attention steering 这个具体 setting 下的量化实证"，而非 "发现了新机制"。如果论文将 Abstract 中的 "first quantitative measurement" 改为 "first empirical demonstration that these known failure modes manifest in lightweight residual gating for attention steering, with specific quantification of their severity"，novelty claim 就更准确。30× gap 本身不是方法论贡献，但它为社区提供了一个有用的 calibration point——"不要在这条路上浪费时间，除非你先解决梯度冲突和 exposure bias"。

**关键分歧点**：R2 认为 "如果 PCGrad 能解决梯度竞争问题，则本文的失败可能仅仅是因为没有使用正确的优化策略"。从方法/实验角度，这是一个 **valid criticism but not a fatal one**。论文的 scope 是 "lightweight gating"——如果你需要 PCGrad + scheduled sampling + vector gates 才能让它 work，那它就不再是 "lightweight" 了。但论文确实应该在 §7 Discussion 中明确讨论 gradient surgery 方法作为 potential fix，而不是完全忽略。

**最终判断**：同意 R2 的诊断（novelty overclaimed），但认为修改 claim 措辞 + 补充 multi-task gradient conflict 文献即可，不需要推翻整篇论文。Critical 但 fixable。

---

### [AGREE] R2-N2: 标题 "Cannot" 过度声称

完全同意。这与我的 N2 一致。补充两点证据：

1. **Scheduled sampling 已部分修复**（Section 6.4, Table 7）：gap 从 30× 降至 4.3×（约 7× reduction），说明改变训练策略确实有效果——这直接反驳 "cannot"。如果 "cannot" 成立，任何训练策略改变都不应缩小 gap。
2. **论文自己在 §7 提出了 constructive directions**：包括 inference-time interventions、decoupled goal-processing pathways、GAR-aware decoding。如果作者自己认为有替代路径，"cannot" 就自相矛盾。

建议标题改为 "Why Lightweight Scalar Gating Struggles to Fix..." 或 "Limitations of Lightweight Gating for..."。

---

### [AGREE] R2-N3: 核心先行工作 Dongre et al. (2026) 不可查证

完全同意。我在 R1-N1 的引用审计中已独立发现这一问题（OpenAlex similarity 0.336，远低于 0.82 阈值）。

从方法/实验角度补充：**论文对 Dongre et al. 的依赖是全方位的**——GAR 指标定义（§3 Eq. 1 引用 Dongre 的定义）、probe AUC baseline（§1 "probe AUC up to 0.98" 引用 Dongre 的实验）、residual stream persistence 发现（§3 引用 Dongre 的结论）。如果这篇文献无法验证：
- GAR 指标本身的合理性失去了外部锚点
- Probe AUC 0.98 的 baseline claim 无法确认
- 论文的整个 motivation chain 断裂

这是比单纯的引用格式问题更深层的风险。论文需要（1）提供 Dongre et al. 的可访问链接/预印本，或（2）在论文内自包含地定义和验证 GAR 指标，不依赖外部参考。

---

### [AGREE with reservation] R2-N4: Related Work 缺失 Multi-task Gradient Conflict 文献

同意这是一个 gap——§6.1 的发现就是 multi-task gradient conflict，不引用 GradNorm/PCGrad 确实是遗漏。

**Reservation**：R2 暗示 "如果 PCGrad 能解决问题，论文的结论就不成立"。从实验角度，我认为这个反事实推理需要实际实验验证，不能仅凭 PCGrad 在其他 setting 上 work 就推断它在这里也 work。PCGrad 解决的是梯度 direction conflict，但论文 Table 6 显示的问题不仅是方向冲突（67-79%），还有 magnitude ratio（7-15×）。PCGrad 的 gradient projection 不直接解决 magnitude imbalance（那是 GradNorm 的范畴）。而且即使梯度问题解决，exposure bias 仍然存在。

**但我同意**：论文至少应该（1）在 Related Work 讨论这些方法；（2）在 §7 Discussion 中将 gradient surgery 列为 explicit future work；（3）ideally，做一个 GradNorm/PCGrad 的消融实验。如果 PCGrad 确实能消除 gradient conflict 但 gap 仍然存在（因为 exposure bias），那反而会**加强**论文的结论。

---

## Should-Fix 问题回应

### [AGREE] R2-W1: 范围过窄——仅标量门控

同意。我在初始审稿中已指出 "结论只适用于 scalar gating，不能推广到 vector gating 或更复杂的门控机制"。论文标题用 "Lightweight Gating" 而非 "Scalar Gating" 是 overclaim。

从实验角度补充：scalar gate 每层只有 1 个参数（总共 28 或 32 个参数，取决于模型层数）。这可能太少了，不是 "gating doesn't work" 而是 "gating with 28 parameters doesn't work"。Vector gate（per-hidden-dim）会有 4096 个参数/层，表达能力完全不同。

---

### [AGREE] R2-W2: Scheduled sampling p≈0.07 统计不显著

完全同意，与我的 W5 一致。p=0.07 在 α=0.05 下不显著，论文应明确标注。

---

### [AGREE] R2-W3: GAR 作为唯一指标的局限性

同意。我在回答 R2-Q3 时已详细讨论：r=0.82 的 instruction compliance 相关性是必要的 sanity check 但不充分。论文应讨论 GAR 的 construct validity 局限，并 acknowledge 它可能无法 capture 所有维度的 multi-turn quality（如 topic coherence、coreference resolution 等）。

---

### [REBUT] R2-W4: 论文长度明显低于 EMNLP long paper 上限（正文约 6 页 vs 限制 8 页）

**不同意这是一个 weakness。**

1. EMNLP 2026 的 8 页是**上限**而非**下限**。ARR reviewer guidelines 从未要求论文必须用满 8 页。论文应该 "as long as needed, as short as possible"。
2. 论文正文约 6 页覆盖了 Introduction → Related Work → Background → Method → Experiments → Analysis → Discussion → Conclusion 的完整结构。如果内容完整，6 页比 8 页灌水更好。
3. **但我承认**：如果增加 figures（attention heatmap、训练曲线——我的 W4）和补充缺失的 λ 值和 loss 定义（我的 N4），论文自然会接近 7-8 页。所以这不是 "论文太短" 的问题，而是 "有些该写的内容没写" 的问题。

R2 这条 W4 的实质关切是对的（内容有缺失），但 framing 为 "长度不够" 不准确。

---

### [AGREE] R2-W5: liu2016attention 引用可能错配

同意。我的引用审计发现该条目 first_author mismatch（bib=liu vs API=chorowski）。这是一个 bib 条目错误，需要修正。

---

### [AGREE] R2-W6: 4 个 orphan bib 条目

同意。我的引用审计独立发现了同样的 4 条 orphan entries（efron1994bootstrap, elhage2021mathematical, olsson2022context, vaswani2017attention）。其中 efron1994bootstrap（bootstrap 经典教科书）和 vaswani2017attention（Transformer 原始论文）可能是作者准备引用但最终没用上的。应清理或在正文中引用。

---

## R1-R2 最终一致性评估

| R2 Issue | R1 判断 | 一致性 |
|----------|---------|--------|
| N1 Novelty overclaim | AGREE with nuance | 实质一致，R1 认为 fixable |
| N2 "Cannot" overclaim | AGREE | 完全一致 |
| N3 Dongre 不可查证 | AGREE | 完全一致 |
| N4 Missing MTL literature | AGREE with reservation | 实质一致，R1 认为缺 PCGrad 实验不 fatal |
| W1 Scope too narrow | AGREE | 一致 |
| W2 SS not significant | AGREE | 一致 |
| W3 GAR limitation | AGREE | 一致 |
| W4 Paper too short | REBUT | R1 认为问题是内容缺失而非长度不够 |
| W5 liu2016 mismatch | AGREE | 一致（引用审计独立发现） |
| W6 Orphan bib | AGREE | 一致（引用审计独立发现） |

**总体**：R1-R2 在 9/10 条上实质一致。唯一分歧是 W4 的 framing（长度 vs 内容），实质关切相同。两位 reviewer 均给出 Overall 3/6 (Weak Reject) / ARR 2.5-3.0 (Borderline Findings)。


---

[Reviewer 1 审稿结果]:
R1 对 R2 全部 10 条审稿意见（N1-N4, W1-W6）的逐条交叉回应已提交。9/10 实质一致，唯一分歧在 W4（论文长度）的 framing——R2 认为 "太短"，R1 认为问题是 "内容缺失而非长度不够"。

---

[Reviewer 2 审稿意见]:

# Reviewer 2 逐条交叉回应：R1 完整审稿意见

---

## Must-Fix 问题逐条回应

### [AGREE] R1-N1: 所有引用均渲染为 "?"

同意这是 critical 级别问题。补充说明：

我在 `dream_20260519T145320/best/paper.pdf` 版本中观察到引用**正常渲染**（如 p.1 "Dongre et al. (2026)"、p.2 "(Zheng et al., 2024)" 均可读）。因此存在两种可能：(a) R1 审查的是不同版本（如 median 或 worst），(b) 我审查的 "best" 版本已修复此问题。

无论哪种情况，**如果提交版确实引用全坏，这是 desk reject 级别缺陷**，我完全同意 R1 的判断。引用审计结果（3 not_found, 5 mismatch, 4 orphan）我在初次审稿中也独立验证并在 N3 中重点标记了 Dongre et al. (2026) 不可查证的问题。

**R2 视角补充**: 从 novelty 审稿角度，引用全坏还有一个额外影响——审稿人无法确认作者是否 properly attribute prior work，这直接影响 novelty claim 的可信度。如果审稿人看到 "first quantitative measurement" 却无法追溯引用链验证这个 "first" 是否成立，会本能地怀疑 overclaiming。

### [AGREE] R1-N2: 单种子实验支撑 "Cannot" 级别强断言

完全同意，且这与我的 N2（标题 "Cannot" overclaims）形成互补。R1 从统计角度、我从逻辑/范围角度分别论证了同一个问题：**证据强度不匹配声称强度**。

具体量化补充：
- 30× gap = GAR 从 0.48(train) 降到 0.016(infer)。如果不同种子下 training GAR 的方差是 ±0.05（0.43–0.53），inference GAR 的方差是 ±0.005（0.011–0.021），则 gap 范围为 20×–48×。这个范围的上下界差 2.4 倍——"30×" 这个数字的精度依赖单种子，不可靠。
- 负面结果论文确实应有更高证据标准，因为 burden of proof 在作者一方：你需要证明"真的不行"而非"你没做对"。单种子无法排除后者。

**R2 视角补充**: 从 novelty 角度，如果 30× 在不同种子下波动剧烈（如 10×–50×），则 "30× gap" 作为 headline contribution 的信息价值大幅缩水。Novelty claim 的精度不应超过数据支持的精度。

### [AGREE] R1-N3: 评估样本量过小且统计功效存疑

同意 R1 的统计分析。补充两个角度：

**1. Power analysis 视角**: R1 指出 d=0.22 在 n=50 下 power 不足。具体而言，双侧 t 检验在 n=50、d=0.2、α=0.05 下的 power 约为 0.29——即有 71% 概率漏检真实的小效应。这意味着 Table 5 中 TG-LO difference "statistically indistinguishable from zero" 的结论可能仅仅是 Type II error。论文不能在 underpowered test 的基础上声称"gating provides zero incremental benefit"（§5.3 标题）。

**2. Novelty 视角**: scheduled sampling 的 p≈0.07 被列为 Contribution 4（"suggestive evidence"）。如果这是论文唯一指向正面方向的结果，其统计不显著意味着论文实际上没有提供任何 actionable insight——既不能确定"gating cannot work"（因为单种子+overclaim），也不能确定"scheduled sampling is the path forward"（因为 p=0.07）。这使论文处于一个尴尬的 limbo：负面结论不够强，正面线索不够确定。

**与 R1 的细微分歧**: R1 将此定为 critical。我认为 50 conversations 的样本量对于**主效应**（30× gap）来说是足够的——当 effect size 这么大时，即使 n=10 也能检测到。R1 的 power concern 更适用于**比较效应**（TG vs LoRA-only, scheduled sampling vs baseline），这些确实是小效应。我会将此分级为 **N3 对主效应: should-fix, 对比较效应: critical**。

### [AGREE] R1-N4: 损失函数超参数和组件定义缺失

同意。从可复现性角度这是 critical。

具体缺失清单核实：
- **λ_GAR、λ_div 数值**: §4.2 Eq. 3 给出 L = L_NTP + λ_GAR · L_GAR + λ_div · L_div，但我在论文中未找到 λ_GAR 和 λ_div 的具体数值。如果它们隐含在 "v7 achieved stable training convergence" 的描述中，那这正是 R1 批评的问题——v7 的具体配置未详述。
- **L_div 定义**: §4.2 提到 L_div "encourages diversity across layer-wise gate values to prevent collapse"，但未给出数学公式。一个没有数学定义的 loss component 是无法复现的。
- **v1–v6 缺失**: 论文声称探索了 7 种 loss 配置但仅报告 v7。这是 cherry-picking 的潜在风险——如果 v3 或 v5 效果更好但不符合论文叙事怎么办？

**R2 视角补充**: 从 novelty 角度，ThreadGate + v7 loss 是论文提出的"方法"，如果方法本身不可复现，则任何基于该方法的负面结论都不可验证。这不仅是可复现性问题，也是 soundness 问题——审稿人无法确认失败是方法的固有局限还是实现细节的问题。

---

## Should-Fix 问题逐条回应

### [AGREE] R1-W1: Llama 上未测试 Uniform Gate

同意。我在交叉回应中已提及此问题。Uniform Gate 是关键对照——它区分了"学到的 per-layer gating pattern 是否比均匀 gating 更优"。Qwen 上的 4-way 消融表明 ThreadGate ≈ Uniform Gate ≈ LoRA-only，这个结论在 Llama 上缺少 Uniform Gate 一环。缺失原因可能是计算预算限制，但应至少在 Limitations 中说明。

### [AGREE] R1-W2: 无 λ_GAR 敏感性消融

同意，且从 novelty 角度这个遗漏尤其有意义。论文的 gradient competition 分析（§6.1）表明 NTP 梯度 dominate GAR 梯度 7–15×。那么一个自然的问题是：**如果大幅增加 λ_GAR（如 10×、50×）来对抗这种 dominance，会发生什么？** 如果增大 λ_GAR 能缩小 gap，则问题不是 "gating cannot work" 而是 "default hyperparameters don't work"。如果增大 λ_GAR 导致 NTP loss 崩坏，这反而是一个更强的负面结果——说明 NTP-GAR 之间存在 fundamental tradeoff。无论哪种结果都比当前更有 insight。

### [AGREE] R1-W3: 训练数据量（1,000 conversations）可能是混淆变量

同意。1,000 conversations 对于训练 gate + LoRA 来说可能不足。如果 gate 需要更多数据来学习稳健的 turn-conditioned 行为，则"gate 没用"可能仅仅是 underfitting。这与我在"Missing Perspectives"中提到的"训练数据量不足"是同一问题。

补充一个 novelty 角度：如果增加数据量到 10k conversations 后 gap 从 30× 缩小到 5×，则论文的核心 claim 不成立。论文未排除这个可能性。

### [AGREE] R1-W4: 缺少可视化

强烈同意。我在交叉回应中已将此采纳为重要遗漏。一篇标题含 "Mechanistic Analysis" 的论文应有：
- Attention heatmap（直观展示 GAR 衰减）
- Training curve（展示三阶段动态和 loss 演化）
- Gradient conflict 热力图（per-layer × per-epoch 的 conflict fraction / magnitude ratio）
- Gate value profile 可视化（per-layer gate 在不同 turn 的变化）

当前 9 tables + 0 figures 的呈现方式严重削弱 "mechanistic" 的说服力。Table 6 的数据如果用热力图展示会直观十倍。

### [AGREE] R1-W5: Scheduled sampling 因果推断局限性未充分讨论

同意。§6.4 用 scheduled sampling 建立 exposure bias 为 "causal factor" 的论证链，但：
1. SS 同时改变了 training distribution（增加了 autoregressive 采样比例）和 model capacity utilization（模型需要处理更多样化的输入），因此 gap 缩小可以归因于 exposure bias 减少，也可以归因于更丰富的训练信号。
2. SS 率从 0% 到 50% 是一个 confound——SS 本身改变了训练动态，不仅仅是"减少了 exposure bias"。

这个局限性在 §7 有部分讨论（"the SS ratio caps at 50%, the remaining teacher-forced samples maintain some distribution mismatch"），但不够系统化。

### [REBUT] R1-W6: "Reverse turn conditioning"（§6.2）证据是间接的

**部分反驳。** R1 认为 §6.2 的 reverse turn conditioning 证据是间接的。我认为 Table 6 实际上提供了**较强的间接证据**，在此场景下是合理的：

- Table 6 显示 Qwen 28 层中 27 层的 gate difference（turn 1 minus turn 21）为正值——gate 在早期 turn 更活跃，晚期 turn 被抑制。这与 "reverse turn conditioning"（在最需要干预的晚期 turn 反而 gate 关闭）的预测完全一致。
- 推理时 gate mean 在 0.93–0.98 范围内，标准差仅 2–7%——gate 几乎不活动，sublayer 输出几乎未被调制。
- 这些数据虽然不能证明因果链（NTP dominance → reverse conditioning → gate inertness），但 pattern 的一致性（27/28 层同方向）使得替代解释难以成立。

**然而**，我同意缺少可视化（如 gate profile 随 turn 变化的折线图）削弱了这个论点的 presentation。数据支持结论，但展示方式不够直观。评级：从 R1 的 warning 降为 minor concern——数据本身可以，展示需要改善。

---

## 对 R1 "主要优势" 的评价

| R1 优势 | R2 评价 |
|---------|---------|
| 1. 有价值的负面结果 | 部分同意。失败机制的归因有价值，但归因的 novelty 有限（已知机制组合）。对于不熟悉 exposure bias 文献的 dialogue 研究者确实有 informative value。 |
| 2. 跨模型一致性 (30× vs 26×) | 同意。这是论文相对较强的一面——两个不同架构/训练的模型呈现同方向结果增加了可信度，尽管 Llama 消融不完整。 |
| 3. 4-way ablation 设计 | 强烈同意。Uniform Gate 对照组是实验设计的亮点，将 "per-layer gating pattern" 与 "任意 gating" 解耦。 |
| 4. Scheduled sampling 因果思路 | 同意思路正确，但执行不足（单模型、p=0.07、confound 未讨论）。 |
| 5. 梯度冲突量化 (Table 6) | 同意这是最有说服力的分析。Per-layer 粒度、conflict fraction、magnitude ratio 的三维度量化是扎实的。但缺少 multi-task gradient conflict 文献的上下文定位（我的 N4）削弱了其 novelty。 |

---

## R1-R2 最终共识矩阵

| 问题 | R1 评级 | R2 评级 | 共识 |
|------|---------|---------|------|
| 引用全坏 | Critical | Critical | ✅ 一致（R2 补充：审查版本可能已修复） |
| 单种子 | Critical | Critical | ✅ 一致 |
| 样本量/功效 | Critical | Critical(比较效应) / Should-fix(主效应) | ⚠️ 细微分歧——30× gap 本身 robust，小效应比较 underpowered |
| Loss 超参缺失 | Critical | Critical | ✅ 一致 |
| Llama 消融不对称 | Warning | Warning | ✅ 一致 |
| λ_GAR 敏感性 | Warning | Warning（升级倾向） | ⚠️ R2 认为这可能应升至 critical——直接影响核心结论 |
| 训练数据量 | Warning | Warning | ✅ 一致 |
| 零图表 | Warning | Warning（接近 critical） | ⚠️ R2 认为对 "mechanistic analysis" 论文接近 critical |
| SS 因果局限 | Warning | Warning | ✅ 一致 |
| Reverse turn conditioning | Warning | Minor（数据支持，展示需改善） | ⚠️ 分歧——R2 认为 Table 6 的 27/28 层一致性较强 |

**R2 额外标记的 R1 未覆盖问题**:
- N3: Dongre et al. (2026) 不可查证 → R1 在 N1 引用审计中提到但未单独列为 critical
- N4: Multi-task gradient conflict 文献完全缺失 → R1 未提及
- W1: 仅标量门控的范围局限 → R1 未单独列出但在叙述中提及
- W3: GAR 单指标依赖 → R1 在文中提到 r=0.72 的局限但未列为 warning
- W5: liu2016attention 引用可能错配 → R1 未提及


---

[Reviewer 2 审稿结果]:
已提交对 R1 完整审稿意见的逐条交叉回应。10 个问题中 9 个 [AGREE]、1 个 [REBUT]（R1-W6 reverse turn conditioning 证据强度），并补充了 R2 独有的 5 个 R1 未覆盖问题。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 58 · 2026-05-19T15:49:28.058846+00:00_

两位 Reviewer 的 Step 2 交叉回应已收齐。审稿报告此前已合成并提交给 Research Director。

**汇总交叉回应关键发现**：

- **R1 对 R2**：9/10 条 [AGREE]，唯一 [REBUT] 是 R2-W4（论文长度）——R1 认为问题是"内容缺失"而非"长度不够"
- **R2 对 R1**：9/10 条 [AGREE]，唯一 [REBUT] 是 R1-W6（reverse turn conditioning 证据强度）——R2 认为 Table 6 的 27/28 层一致性构成较强间接证据

两位 Reviewer 在所有 critical 问题上完全一致。两处 [REBUT] 均为 minor framing 分歧，不影响 overall 判断。

审稿报告已于本轮早些时候提交（Overall: **2.5/5 ARR — Borderline Findings / 3/6 — Weak Reject**），Issue Tracker 已同步写入 19 条 issue。报告内容已涵盖这些交叉回应中的所有共识和分歧点，无需重新提交。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director"
}
```

</details>

---


## Round 5

## Round 5

64 recorded events


### User

_source line 59 · 2026-05-22T08:31:20.512322+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: turn_residual_gating
- 论文路径: /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: Long Paper (ARR August cycle)
- 截止日期: 2026-08-03
- **引用验证**: ❌ 未启用

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 60 · 2026-05-22T08:31:27.467794+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 61 · 2026-05-22T08:31:27.519012+00:00_

1	---
2	name: review-director-session-start
3	description: Review Director session 启动初始化流程——圆桌多轮审稿协议。Review Director 角色 session 启动时自动使用。
4	priority: 9
5	scope: global
6	tags:
7	- workflow
8	- review
9	- session
10	version: 3
11	roles:
12	- review_director
13	---
14	
15	# Review Director Session 启动流程（圆桌会议模式）
16	
17	## 初始化
18	
19	1. `director_get_project_overview(project)` — 了解研究现状（实验状态、最新报告）
20	2. 读取论文文件状态：检查 `projects/{project}/paper/` 或 `main.tex` 是否存在
21	3. 检查是否有来自 Research Director 的论文提交（`[论文提交]` 消息）
22	4. 向用户简要汇报：
23	   - **投稿目标**：venue 和 deadline
24	   - **论文状态**：当前草稿位置和版本
25	   - **资料完整性**：提交的材料是否齐全
26	   - **下一步**：即将开始的圆桌审稿流程
27	
28	## 评审流程（收到论文提交后执行）
29	
30	### Step 0 — 资料检查 + Venue 调研（必须先做，不可跳过）
31	
32	1. 检查提交资料完整性：论文文件是否存在、是否可读、补充材料是否齐全
33	2. 确认目标投稿 venue（从提交消息中获取）
34	3. 用 `web_search` 搜索该 venue 当前轮次的 CFP（Call for Papers），关键词示例：
35	   - `"&lt;venue name> 2026 call for papers" site:aclweb.org`
36	   - `"&lt;venue name> 2026 submission deadline"`
37	   - `"&lt;venue name> 2026 author guidelines"`
38	4. **验证 deadline 未过期**：今天日期与截止日期对比，若已过期立即通知用户，不继续
39	5. 提取当前版本的格式要求：
40	   - 页数限制（正文 / 附录 / 参考文献）
41	   - 模板（ACL / IEEE / NeurIPS / ICML / ...）
42	   - 匿名规则（double-blind / single-blind / open）
43	   - 附录规则（是否允许、是否参与审稿）
44	   - 引用格式（natbib / biblatex / 特定 .bst）
45	6. 将以上信息作为上下文，随任务一起传递给 Reviewer
46	
47	⚠️ 禁止使用训练知识中的 venue 要求——格式标准每年都会更新，必须实时搜索确认。
48	
49	### Step 0.5 — 决定 Reviewer 编排
50	
51	根据 venue 类型和论文特点，决定：
52	- 需要几个 Reviewer（1-5 人）
53	- 每个 Reviewer 的审查侧重
54	
55	参考：
56	- **顶会长文**（NeurIPS/ICML/ACL）：3 人（方法/实验 + novelty/related work + 格式/ethics）
57	- **一般会议**（EMNLP/NAACL）：2 人（方法严谨性 + 新颖性/完整性）
58	- **Workshop / 短文**：1 人（全面审查）
59	
60	向 Group C（即项目配置中的 `feishu.review_chat_id` 审稿群）汇报编排决定。
61	
62	### Step 0.6 — 外部审稿线（与 Step 1 并行）
63	
64	检查项目配置中 `external_review.paperreview_ai.enabled` 是否为 `true`：
65	- 如果启用：调用 `request_external_review(project, paper_pdf_path, venue)` 向用户群发送协助提交卡片
66	- 这一步与 Step 1（内部 Reviewer 分配）**并行执行**，不阻塞内部审稿流程
67	- 外部结果到达后（用户在群里粘贴），纳入 Step 4 最终报告
68	- 如果到 Ste
…[truncated 3286 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 62 · 2026-05-22T08:31:33.566597+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,dispatch_visual_check,request_external_review,get_external_review_status,get_visual_check_status,director_post_to_reviewer,submit_review_report_to_research_director,update_review_issues,read_project_file",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_get_project_overview,dispatch_visual_check,request_external_review,get_external_review_status,get_visual_check_status,director_post_to_reviewer,submit_review_report_to_research_director,update_review_issues,read_project_file",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 63 · 2026-05-22T08:31:33.567040+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 64 · 2026-05-22T08:31:37.492144+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__read_project_file",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__read_project_file",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 65 · 2026-05-22T08:31:37.492539+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 66 · 2026-05-22T08:31:40.631258+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "turn_residual_gating"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "turn_residual_gating"
  }
}
```

</details>

---


### Tool result

_source line 67 · 2026-05-22T08:31:41.135190+00:00_

{"result":"# 项目 turn_residual_gating 概况\n\n## 实验状态 (37 个)\n\n- **phase2_tg_s42_v7**: DONE (success) — \n- **phase2_tg_s42_v9_pcgrad**: DONE (success) — \n- **phase2_lora_only_s42**: DONE (success) — \n- **phase2_ug_s42**: DONE (success) — \n- **phase2_tg_s42_v8_schedsampling**: DONE (failed) — \n- **analysis_attention_heatmap**: DONE (success) — \n- **analysis_gradient_conflict**: DONE (success) — \n- **phase2_4way_eval_heldout**: DONE (success) — \n- **phase2_4way_eval**: DONE (negative) — \n- **phase2_tg_s42_v5**: DONE (negative) — \n- **phase2_tg_s42_v4**: DONE (failed) — \n- **phase2_tg_s42_v3b**: DONE (success) — \n- **phase2_tg_s42_v3**: DONE (negative) — \n- **phase2_tg_s42_v2**: DONE (killed) — \n- **phase1_gar_diag**: DONE (success) — \n\n## 最新报告\n# Handover — 2026-05-22\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n- llama_tg_training（准备中）\n\n## 近期结论\n- **eval_llama_ar_n20** (success): N=20 AR eval stabilizes Llama 3-way (Base/TG/LoRA-only) autoregressive GAR estimates. N=5 suffered from outlier influence (3/5 conv had GAR>0.4 outlier turns); N=20 provides robust mean±std. ← 基于 eval_llama_lora_only_s42\n- **eval_llama_lora_only_s42** (success): LoRA-only ablation (no gate) on Llama-3.1-8B: if TG's GAR improvement comes from the gate, LoRA-only should show minimal GAR recovery vs base. ← 基于 llama_lora_only_s42\n- **llama_lora_only_s42** (success): Llama-3.1-8B LoRA-only baseline (gate=none, 无 gating 机制): 与 Llama TG s42 对比，验证 gating 对 Llama 的增量贡献。如果 LoRA-only GAR ≈ TG GAR → gating 零增量与 Qwen 结论一致（C5 跨模型）。 ← 基于 llama_tg_s42\n\n## 趋势\n成功 27 / 负向 5 / 失败 3 / 共 36\n\n## 下一步\n（无活跃 idea，请通过 ideas.md 添加）\n\n## 资源状态\nwestd-20861: 无 GPU 信息\n\n## 告警\n- phase2_tg_s42_v2: 已被终止 — unknown\n- phase2_tg_s42_v4: 训练失败 — unknown\n- phase2_tg_s42_v8_schedsampling: 训练失败 — unknown\n- phase2_tg_s42_v8b_ss_fixed: 训练失败 — unknown"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 503
}
```

</details>

---


### Tool call

_source line 68 · 2026-05-22T08:31:41.135842+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_local_file,WebSearch",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_local_file,WebSearch",
    "max_results": "2"
  }
}
```

</details>

---


### Tool result

_source line 69 · 2026-05-22T08:31:41.186348+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 70 · 2026-05-22T08:31:45.506228+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 call for papers ARR submission guidelines author instructions"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 call for papers ARR submission guidelines author instructions"
  }
}
```

</details>

---


### Tool call

_source line 71 · 2026-05-22T08:31:47.021862+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/main.tex",
  "limit": "80"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/main.tex",
    "limit": "80"
  }
}
```

</details>

---


### Tool result

_source line 72 · 2026-05-22T08:31:47.477684+00:00_

1	\documentclass[11pt]{article}
2	\usepackage[review]{acl}
3	\usepackage{times}
4	\usepackage{latexsym}
5	\usepackage[T1]{fontenc}
6	\usepackage[utf8]{inputenc}
7	\usepackage{microtype}
8	\usepackage{inconsolata}
9	\usepackage{graphicx}
10	\usepackage{amsmath}
11	\usepackage{amssymb}
12	\usepackage{booktabs}
13	\usepackage{multirow}
14	\usepackage{xcolor}
15	\usepackage{url}
16	\usepackage{subcaption}
17	
18	\graphicspath{{../figures/paper/}}
19	
20	\title{Why Lightweight Gating Fails to Fix Multi-Turn Attention Degradation:\\A Mechanistic Analysis}
21	
22	\author{Anonymous}
23	
24	\begin{document}
25	\maketitle
26	
27	\input{sections/abstract}
28	\input{sections/introduction}
29	\input{sections/related_work}
30	\input{sections/method}
31	\input{sections/experiments}
32	\input{sections/analysis}
33	\input{sections/discussion}
34	\input{sections/conclusion}
35	\input{sections/limitations}
36	
37	\bibliographystyle{acl_natbib}
38	\bibliography{references}
39	
40	\appendix
41	\input{sections/appendix}
42	
43	\end{document}
44	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "Read",
  "elapsed_ms": 455
}
```

</details>

---


### Tool call

_source line 73 · 2026-05-22T08:31:47.478090+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_local_file",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_local_file",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 74 · 2026-05-22T08:31:47.528591+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 75 · 2026-05-22T08:31:55.265355+00:00_

Web search results for query: "EMNLP 2026 call for papers ARR submission guidelines author instructions"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"Submission Guide","url":"https://nlp4climate.github.io/submissionguide/"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"[EMNLP 2025] First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2025-first-call-papers"}]

Based on the web search results, here's a comprehensive overview of the EMNLP 2026 call for papers, ARR submission guidelines, and author instructions:

## Submission Process

EMNLP 2026 uses ACL Rolling Review (ARR) as a reviewing system with final decisions made by the conference. Authors submit articles to ARR where they receive reviews and meta-reviews from ARR reviewers and action editors, then commit their reviewed articles to EMNLP 2026 where Senior Area Chairs and Program Chairs make acceptance decisions.

## Important Dates

The ARR submission deadline for long and short 
…[truncated 1542 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "WebSearch",
  "elapsed_ms": 9759
}
```

</details>

---


### Tool call

_source line 76 · 2026-05-22T08:31:59.650747+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review 2026 paper format requirements page limits long short paper",
  "allowed_domains": "['aclrollingreview.org', '2026.emnlp.org', 'aclweb.org']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review 2026 paper format requirements page limits long short paper",
    "allowed_domains": "['aclrollingreview.org', '2026.emnlp.org', 'aclweb.org']"
  }
}
```

</details>

---


### Tool call

_source line 77 · 2026-05-22T08:32:01.064613+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_1/submitted.pdf 2>/dev/null && echo \"PDF_EXISTS\" || echo \"NO_PDF\"",
  "description": "Check if submitted PDF exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_1/submitted.pdf 2>/dev/null && echo \"PDF_EXISTS\" || echo \"NO_PDF\"",
    "description": "Check if submitted PDF exists"
  }
}
```

</details>

---


### Tool result

_source line 78 · 2026-05-22T08:32:02.028523+00:00_

-rw-r--r-- 1 ubuntu ubuntu 415753 May 22 08:29 /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_1/submitted.pdf
PDF_EXISTS

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "Bash",
  "elapsed_ms": 963
}
```

</details>

---


### Tool call

_source line 79 · 2026-05-22T08:32:02.433596+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_issues.yaml 2>/dev/null && cat /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_issues.yaml || echo \"NO_ISSUES_FILE\"",
  "description": "Check existing review issues tracker"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_issues.yaml 2>/dev/null && cat /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_issues.yaml || echo \"NO_ISSUES_FILE\"",
    "description": "Check existing review issues tracker"
  }
}
```

</details>

---


### Tool result

_source line 80 · 2026-05-22T08:32:02.536212+00:00_

-rw-r--r-- 1 ubuntu ubuntu 11100 May 19 16:59 /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_issues.yaml

# Review Issues Tracker — turn_residual_gating
# Round 1 (2026-05-19, dream_20260519T145320)
# Action Matrix finalized D025 (2026-05-19)

- id: "R1-N1"
  summary: "所有引用渲染为 '?'——bibliography 编译失败，37 处引用不可读"
  category: format
  severity: critical
  status: open
  first_raised_round: 1
  last_seen_round: 1
  mentions:
    - round: 1
      reviewers: [1, 2]
      note: "Dream paper artifact。真论文由 Paper Agent 写作时确保编译。"
  action_items:
    - round: 1
      action: "Paper Agent 写作时确保 bibtex 编译正确"
      assigned_to: paper_agent
      status: open
  resolution: ""
  resolution_round: null

- id: "R1-N2"
  summary: "单种子 (seed=42) 支撑负面结论——无法排除 seed 偶然性"
  category: experiment
  severity: critical
  status: in_progress
  first_raised_round: 1
  last_seen_round: 1
  mentions:
    - round: 1
      reviewers: [1, 2]
      note: "Bootstrap CI 仅覆盖 eval variance，不覆盖 training variance。"
  action_items:
    - round: 1
      action: "plan_019: seed=123 extra training (TG+LoRA-only, 6h GPU). 1 extra seed 足够因 30x gap effect size 极大。"
      assigned_to: agent
      status: in_progress
  resolution: ""
  resolution_round: null

- id: "R1-N3"
  summary: "评估样本量过小（50 conversations），统计功效不足"
  category: experiment
  severity: critical
  status: in_progress
  first_raised_round: 1
  last_seen_round: 1
  mentions:
    - round: 1
      reviewers: [1]
      note: "Cohen's d≈0.22 在 n=50 下 power 不足。"
  action_items:
    - round: 1
      action: "plan_020: 扩展到 200 conversations (idx>=7000), 2h GPU"
      assigned_to: agent
      status: in_progress
  resolution: ""
  resolution_round: null

- id: "R1-N4"
  summary: "损失函数超参数（λ_GAR, λ_div）和 v1-v6 配置定义缺失"
  category: method
  severity: critical
  status: in_progress
  first_raised_round: 1
  last_seen_round: 1
  mentions:
    - round: 1
      reviewers: [1, 2]
      note: "v1-v7 配置仅报告 v7，无法判断是否 cherry-p
…[truncated 8025 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "Bash",
  "elapsed_ms": 102
}
```

</details>

---


### Tool result

_source line 81 · 2026-05-22T08:32:05.109182+00:00_

Web search results for query: "ACL Rolling Review 2026 paper format requirements page limits long short paper"

Links: [{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"EACL 2026: First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eacl-2026-first-call-papers"},{"title":"ACL Rolling Review | ACL Member Portal","url":"https://www.aclweb.org/portal/content/acl-rolling-review"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"},{"title":"Industry Track — Call for Papers @ EACL 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/industry-track-call-papers-eacl-2026"},{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"First Call for Papers – EACL 2026 Student Research Workshop (SRW) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/first-call-papers-eacl-2026-student-research-workshop-srw"}]

Based on the search results, here is the ACL Rolling Review 2026 paper format requirements regarding page limits for long and short papers:

## Page Limits

Short papers have a maximum of 4 content pages, while long papers have a maximum of 8 content pages.

## Sections Not Counting Toward Page Limit

Sections on ethical considerations and limitations do not count towards the page limit. Additionally, appendices should come after the references in the submitted PDF, but do not count towards the page limit.

## Mandatory Limitations Section

Authors are required to discuss the limitation
…[truncated 501 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "WebSearch",
  "elapsed_ms": 5458
}
```

</details>

---


### Tool call

_source line 82 · 2026-05-22T08:32:20.076612+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/ && wc -l /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/*.tex",
  "description": "List paper sections and their sizes"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/ && wc -l /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/*.tex",
    "description": "List paper sections and their sizes"
  }
}
```

</details>

---


### Tool call

_source line 83 · 2026-05-22T08:32:20.127326+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "turn_residual_gating"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "turn_residual_gating"
  }
}
```

</details>

---


### Tool result

_source line 84 · 2026-05-22T08:32:20.178054+00:00_

total 88
drwxr-xr-x 2 ubuntu ubuntu  4096 May 22 08:19 .
drwxr-xr-x 3 ubuntu ubuntu  4096 May 22 08:29 ..
-rw-r--r-- 1 ubuntu ubuntu  1500 May 22 08:16 abstract.tex
-rw-r--r-- 1 ubuntu ubuntu 10053 May 22 08:19 analysis.tex
-rw-r--r-- 1 ubuntu ubuntu  1775 May 20 18:21 appendix.tex
-rw-r--r-- 1 ubuntu ubuntu  2487 May 20 10:56 background.tex
-rw-r--r-- 1 ubuntu ubuntu   539 May 22 08:16 conclusion.tex
-rw-r--r-- 1 ubuntu ubuntu  2481 May 22 05:00 discussion.tex
-rw-r--r-- 1 ubuntu ubuntu  7985 May 22 00:38 experiments.tex
-rw-r--r-- 1 ubuntu ubuntu  6635 May 22 08:16 introduction.tex
-rw-r--r-- 1 ubuntu ubuntu  1948 May 22 08:16 limitations.tex
-rw-r--r-- 1 ubuntu ubuntu  3680 May 20 18:21 method.tex
-rw-r--r-- 1 ubuntu ubuntu 14410 May 22 04:43 references.bib
-rw-r--r-- 1 ubuntu ubuntu  4680 May 22 05:00 related_work.tex
    3 /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/abstract.tex
   52 /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/analysis.tex
   26 /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex
   17 /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/background.tex
    3 /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/conclusion.tex
    9 /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/discussion.tex
   61 /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/experiments.tex
   17 /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/introduction.tex
   12 /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/limitations.tex
   45 /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/method.tex
   18 /home/ubuntu/.ag
…[truncated 106 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "Bash",
  "elapsed_ms": 101
}
```

</details>

---


### Tool result

_source line 85 · 2026-05-22T08:32:20.379714+00:00_

{"result":"# 项目 turn_residual_gating 概况\n\n## 实验状态 (37 个)\n\n- **phase2_tg_s42_v7**: DONE (success) — \n- **phase2_tg_s42_v9_pcgrad**: DONE (success) — \n- **phase2_lora_only_s42**: DONE (success) — \n- **phase2_ug_s42**: DONE (success) — \n- **phase2_tg_s42_v8_schedsampling**: DONE (failed) — \n- **analysis_attention_heatmap**: DONE (success) — \n- **analysis_gradient_conflict**: DONE (success) — \n- **phase2_4way_eval_heldout**: DONE (success) — \n- **phase2_4way_eval**: DONE (negative) — \n- **phase2_tg_s42_v5**: DONE (negative) — \n- **phase2_tg_s42_v4**: DONE (failed) — \n- **phase2_tg_s42_v3b**: DONE (success) — \n- **phase2_tg_s42_v3**: DONE (negative) — \n- **phase2_tg_s42_v2**: DONE (killed) — \n- **phase1_gar_diag**: DONE (success) — \n\n## 最新报告\n# Handover — 2026-05-22\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n- llama_tg_training（准备中）\n\n## 近期结论\n- **eval_llama_ar_n20** (success): N=20 AR eval stabilizes Llama 3-way (Base/TG/LoRA-only) autoregressive GAR estimates. N=5 suffered from outlier influence (3/5 conv had GAR>0.4 outlier turns); N=20 provides robust mean±std. ← 基于 eval_llama_lora_only_s42\n- **eval_llama_lora_only_s42** (success): LoRA-only ablation (no gate) on Llama-3.1-8B: if TG's GAR improvement comes from the gate, LoRA-only should show minimal GAR recovery vs base. ← 基于 llama_lora_only_s42\n- **llama_lora_only_s42** (success): Llama-3.1-8B LoRA-only baseline (gate=none, 无 gating 机制): 与 Llama TG s42 对比，验证 gating 对 Llama 的增量贡献。如果 LoRA-only GAR ≈ TG GAR → gating 零增量与 Qwen 结论一致（C5 跨模型）。 ← 基于 llama_tg_s42\n\n## 趋势\n成功 27 / 负向 5 / 失败 3 / 共 36\n\n## 下一步\n（无活跃 idea，请通过 ideas.md 添加）\n\n## 资源状态\nwestd-20861: 无 GPU 信息\n\n## 告警\n- phase2_tg_s42_v2: 已被终止 — unknown\n- phase2_tg_s42_v4: 训练失败 — unknown\n- phase2_tg_s42_v8_schedsampling: 训练失败 — unknown\n- phase2_tg_s42_v8b_ss_fixed: 训练失败 — unknown"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 252
}
```

</details>

---


### Tool call

_source line 86 · 2026-05-22T08:32:24.212228+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 87 · 2026-05-22T08:32:24.714775+00:00_

1	\begin{abstract}
2	Multi-turn dialogue with Large Language Models (LLMs) suffers from progressive attention decay toward system prompt goal tokens. On Qwen-2.5-7B-Instruct, the Goal Attention Ratio (GAR) declines by 70.8\% between early and mid-conversation turns, yet linear probes recover goal content from the residual stream with AUC\,=\,0.98. We introduce ThreadGate, a per-layer content-and-turn-conditioned MLP gate ($x_{l+1} = x_l + g_l \cdot f_l(x_l)$) trained jointly with next-token prediction (NTP) and an auxiliary GAR loss. A five-way comparison reveals that training succeeds (teacher-forced GAR\,=\,0.50) but autoregressive GAR drops to 0.015--0.025, a 20--33$\times$ gap; gating contributes zero measurable benefit and PCGrad-based causal exclusion rules out gradient conflict. The failure traces to exposure bias: attention patterns optimized under teacher-forced prefixes do not transfer to model-generated text. Inference-time steering ($\beta$\,=\,5) recovers GAR from 0.064 to 0.727, providing constructive evidence that attention misallocation---not representation degradation---is the proximal cause. Scheduled sampling compresses the gap to 1.57$\times$ with no PPL cost (single seed), and cross-model evaluation on Llama-3.1-8B confirms the gap (27$\times$ by median). These findings characterize how exposure bias selectively destroys auxiliary objective generalization under the tested conditions (Qwen-2.5-7B and Llama-3.1-8B, UltraChat, GAR-family losses).
3	\end{abstract}
4	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 88 · 2026-05-22T08:32:24.715210+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 89 · 2026-05-22T08:32:25.620673+00:00_

1	\section{Introduction}\label{sec:introduction}
2	
3	Multi-turn dialogue is the dominant mode of interaction with large language models (LLMs), and system prompts that specify task goals form the foundation of instruction following. As conversations grow longer, however, models progressively lose track of these goal specifications. \citet{dongre2026attention} quantified this degradation across 12 models: the Goal Attention Ratio (GAR), which measures how much attention the model allocates to goal tokens in the system prompt, declines by 27--48\% between early and mid-conversation turns. We replicate and extend this finding on Qwen-2.5-7B-Instruct, observing a 70.8\% relative decline in GAR from 0.0418 at turn~1 to 0.0122 at mid-conversation. We attribute the steeper decline partly to our use of last-token GAR, which captures summary-position attention more sensitively than the all-token average of \citet{dongre2026attention}, and partly to Qwen-2.5-7B's stronger instruction-following fidelity in early turns. This attention decay represents a systematic failure of multi-turn models to maintain task coherence, and it grows worse with each additional turn.
4	
5	A striking aspect of this degradation is what it does \emph{not} affect. \citet{dongre2026attention} showed that goal-relevant information persists in the residual stream throughout the conversation: linear discriminant analysis probes recover goal content with AUC\,=\,0.98 even at late turns where attention to goal tokens has collapsed. The information is present in the hidden states, but the attention mechanism fails to route it toward the output computation. This dissociation between information availability and information utilization suggests a natural intervention: if the residual stream already carries goal information, a learnable gate on the residual pathway could amplify or attenuate layer contributions to recover goal attention. This reasoning motivates ThreadGate, which modulates each residual updat
…[truncated 4680 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "Read",
  "elapsed_ms": 905
}
```

</details>

---


### Tool call

_source line 90 · 2026-05-22T08:32:25.621115+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 91 · 2026-05-22T08:32:26.023665+00:00_

1	\section{Related Work}\label{sec:related}
2	
3	\paragraph{Multi-turn attention degradation.}
4	Recent work has established that LLMs systematically degrade across conversation turns. \citet{laban2025lost} showed that model performance drops on tasks placed in later turns, even when the tasks are identical to earlier ones. \citet{liu2026intent} traced a related failure to intent mismatch, where models progressively shift from the user's original intent as dialogue extends. MT-Bench-101 \citep{bai2024mtbench101} provides fine-grained multi-turn evaluation across 1388 turn-level instances, revealing that capability varies substantially across task categories. \citet{dongre2026attention} established the quantitative foundation for this line of work: they defined the Goal Attention Ratio (GAR) and showed that attention to system-prompt goal tokens decays by 27--48\% across turns in 12 models, while residual stream probes retain goal information with AUC\,=\,0.98. We observe a steeper 70.8\% decline on Qwen-2.5-7B-Instruct (\S\ref{sec:experiments}). This dissociation between attention collapse and residual persistence motivates our gating intervention. Their work characterizes the phenomenon; ours attempts the first systematic cure and, in doing so, uncovers why lightweight interventions fail to transfer from training to inference.
5	
6	\paragraph{Instruction stability.}
7	\citet{li2024measuring} independently quantified instruction instability in multi-turn dialogs and proposed split-softmax---separating instruction from conversation tokens during attention computation---as an inference-time remedy. Our work adds causal diagnosis (five-way factorial + PCGrad exclusion), exposure bias attribution, and training-time mitigation via scheduled sampling; our $\beta$-steering complements split-softmax as an alternative inference-time approach (\S\ref{sec:discussion}).
8	
9	\paragraph{Residual gating and adaptive depth.}
10	ReZero \citep{bachlechner2021rezero} showed that resi
…[truncated 2728 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "Read",
  "elapsed_ms": 402
}
```

</details>

---


### Tool call

_source line 92 · 2026-05-22T08:32:26.074572+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 93 · 2026-05-22T08:32:26.528781+00:00_

1	\section{Method}\label{sec:method}
2	
3	\subsection{Preliminaries}\label{sec:background}
4	
5	\paragraph{Goal Attention Ratio.}
6	We denote the task specification tokens in the system prompt as \emph{goal tokens} $\mathcal{G}$. \citet{dongre2026attention} defined the Goal Attention Ratio (GAR) for a model with $L$ layers and $H$ heads at turn $\tau$ as
7	\begin{equation}\label{eq:gar}
8	  \text{GAR}(\tau) = \frac{1}{L \cdot H \cdot |\mathcal{R}_\tau|} \sum_{\ell=1}^{L} \sum_{h=1}^{H} \sum_{i \in \mathcal{R}_\tau} \sum_{j \in \mathcal{G}} A_{i,j}^{(\ell,h)},
9	\end{equation}
10	where $\mathcal{R}_\tau$ is the set of response tokens at turn $\tau$ and $A_{i,j}^{(\ell,h)}$ is the attention weight from token $i$ to token $j$ at layer $\ell$, head $h$.
11	
12	\paragraph{Two GAR variants.}
13	\textbf{GAR-Dongre} is the original definition (Eq.~\ref{eq:gar}), averaging over all response tokens. \textbf{GAR-ours} restricts the measurement to the \emph{last token} of each assistant turn:
14	\begin{equation}\label{eq:gar-ours}
15	  \text{GAR\text{-}ours}(\tau) = \frac{1}{L \cdot H} \sum_{\ell=1}^{L} \sum_{h=1}^{H} \sum_{j \in \mathcal{G}} A_{t_\tau,\, j}^{(\ell,h)},
16	\end{equation}
17	where $t_\tau$ is the last token index at turn $\tau$. Attention at this position reflects the information drawn upon for continuation; we use GAR-ours as the optimization target for $\mathcal{L}_\text{GAR}$ (\S\ref{sec:loss}).
18	
19	\subsection{ThreadGate Architecture}
20	
21	Inspired by the residual scaling idea of ReZero \citep{bachlechner2021rezero}, ThreadGate modulates the residual stream with a content-and-turn-conditioned gate at each transformer layer. The gated residual update at layer $l$ is
22	\begin{equation}
23	  x_{l+1} = x_l + g_l \cdot f_l(x_l),
24	\end{equation}
25	where $f_l$ denotes the sublayer computation (self-attention or FFN). The gate $g_l$ is produced by a two-layer MLP:
26	\begin{equation}\label{eq:gate}
27	  g_l = \sigma\!\bigl(W_2\,\text{ReLU}(W_1\,[\text{proj}
…[truncated 1809 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "Read",
  "elapsed_ms": 454
}
```

</details>

---


### Tool call

_source line 94 · 2026-05-22T08:32:26.579544+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 95 · 2026-05-22T08:32:27.031710+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Setup}
5	
6	We fine-tune Qwen-2.5-7B-Instruct on 8K multi-turn conversations from the UltraChat training split, a dataset of naturalistic dialogues across diverse topics. LoRA adapters (rank 16, $\alpha$=32) are applied to query and value projection layers (\texttt{q\_proj}, \texttt{v\_proj}). The combined loss $\mathcal{L} = \mathcal{L}_\text{NTP} + \lambda_\text{GAR}\mathcal{L}_\text{GAR} + \lambda_\text{div}\mathcal{L}_\text{div}$ uses $\lambda_\text{GAR} = \lambda_\text{div} = 1.0$ with MSE target $\tau = 0.5$ (\S\ref{sec:loss}). We train for 3 epochs with AdamW (lr $= 2 \times 10^{-4}$, batch size 1, gradient accumulation 8, seed 42; ThreadGate additionally with seed 123); each variant requires approximately 6 hours on a single NVIDIA RTX PRO 6000 Blackwell Server Edition GPU (102\,GB). Full hyperparameters are provided in Appendix~\ref{sec:appendix-hyper}.
7	
8	We evaluate five configurations that form a factorial design isolating four causal factors. \textbf{ThreadGate}: full system with 28 gate networks (Eq.~\ref{eq:gate}) and three-term loss. \textbf{+PCGrad}: ThreadGate with PCGrad \citep{yu2020pcgrad} projecting conflicting gradients (isolates gradient conflict). \textbf{Uniform Gate}: gates without turn embedding (isolates turn conditioning). \textbf{LoRA-only}: gates fixed at 1.0, trained with $\mathcal{L}_\text{NTP} + \mathcal{L}_\text{GAR}$ only (isolates gating mechanism). \textbf{Base}: pretrained model (isolates fine-tuning). All fine-tuned variants share training data, LoRA configuration, optimizer, and seed. We evaluate under \emph{IID} (same-distribution UltraChat text) and \emph{held-out} (50 non-overlapping conversations) teacher-forced protocols, reporting GAR-ours (last-token attention to goals, \S\ref{sec:background}), GAR-Dongre \citep{dongre2026attention} (all-token average), and PPL.
9	
10	\subsection{Main Results}
11	
12	Table~\ref{tab:four-way} presents the five-way com
…[truncated 6162 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 96 · 2026-05-22T08:32:27.032233+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/analysis.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/analysis.tex"
  }
}
```

</details>

---


### Tool result

_source line 97 · 2026-05-22T08:32:27.534714+00:00_

1	\section{Analysis}\label{sec:analysis}
2	
3	The five-way comparison in \S\ref{sec:experiments} established that gating produces no measurable benefit over LoRA-only fine-tuning. This section traces the failure through a three-step causal chain: we first show that gates learn behavior opposite to the design intent (\S\ref{subsec:gate-conditioning}), then rule out gradient conflict as the explanation through a causal exclusion experiment (\S\ref{subsec:pcgrad}), and finally identify distribution shift as the root cause (\S\ref{subsec:dist-shift}). \S\ref{subsec:mechanism-specificity} confirms this selectivity with an orthogonal hidden-state metric, and \S\ref{subsec:cross-model} confirms the failure generalizes across architecturally distinct LLMs.
4	
5	\subsection{Gate Turn Conditioning}\label{subsec:gate-conditioning}
6	
7	The design intent of ThreadGate is to modulate the residual stream more aggressively at late conversation turns, where GAR naturally decays (\S\ref{sec:background}). We test whether the learned gates achieve this by comparing gate values at turn~1 (early) and turn~21 (late) across all 28 layers of the trained model.
8	
9	The gates do the opposite. In 27 of 28 layers, the gate value at turn~1 is lower than at turn~21 (Wilcoxon signed-rank test: $p = 3.73 \times 10^{-8}$, effect size $r = 0.975$). At layer~23, the gate is 0.769 at turn~1 and 0.979 at turn~21; at layer~14, it is 0.747 at turn~1 and 0.928 at turn~21. The pattern is consistent: gates suppress the residual stream more at early turns (where GAR is already high) and become nearly passive at late turns (where intervention is most needed). This inversion has a straightforward explanation. NTP loss pressure is highest at late turns, where the model must predict tokens conditioned on a long context. The NTP gradient pushes gates toward 1.0 to preserve the full sublayer computation, and this pressure is strongest precisely where GAR-based attenuation would be most useful.
10	
11	The resultin
…[truncated 8203 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 98 · 2026-05-22T08:32:27.585264+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 99 · 2026-05-22T08:32:28.037156+00:00_

1	\section{Discussion}\label{sec:discussion}
2	
3	The failure traces to an incompatibility between teacher-forcing and GAR-family auxiliary losses, not to the gating architecture. NTP gradient pressure (7.5--14.7$\times$ the GAR magnitude) pushes gates toward identity (2--7\% attenuation), while inference-time steering ($\beta$\,=\,5) recovers GAR from 0.064 to 0.727, providing constructive evidence that attention misallocation is the proximal cause (\S\ref{subsec:steering}). Split-softmax \citep{li2024measuring} offers a complementary inference-time approach that restructures attention computation rather than applying additive bias.
4	
5	\paragraph{Scheduled sampling as training-time mitigation.} A preliminary experiment (single seed) applies scheduled sampling \citep{bengio2015scheduled}, linearly mixing teacher-forced and model-generated contexts. Autoregressive GAR-ours increases from 0.016 to 0.318 (20$\times$), compressing the ${\sim}$31$\times$ gap to 1.57$\times$ with negligible PPL change (1.38 vs.\ 1.36). GAR-Dongre also rises (0.019$\to$0.353), suggesting indirect improvement of all-token goal attention. The two paths are complementary: $\beta$\,=\,5 achieves the strongest GAR recovery but incurs 24\% PPL cost (1.43\,$\to$\,1.77); $\beta$\,=\,3 offers a more balanced tradeoff (PPL +9\%). Scheduled sampling incurs no fluency cost but requires retraining. A second seed trained from scratch (rather than resumed from a standard-trained epoch) yields AR GAR\,=\,0.418 (gap 1.20$\times$), versus 5\% seed variance in standard ThreadGate training, suggesting that early scheduled sampling exposure---before the model consolidates teacher-forced attention patterns---may further compress the gap; systematic schedule ablation is deferred.
6	
7	\paragraph{Instruction retention under steering.} Across 18 system-prompt constraint types, $\beta$\,=\,3 steering increases content constraint compliance by +23.8\,pp (GAR-compliance $r$\,=\,0.200, $p$\,=\,0.007; McNemar $p$\,=\
…[truncated 502 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "Read",
  "elapsed_ms": 451
}
```

</details>

---


### Tool call

_source line 100 · 2026-05-22T08:32:28.037825+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 101 · 2026-05-22T08:32:28.539984+00:00_

1	\section{Conclusion}\label{sec:conclusion}
2	
3	ThreadGate modulates the residual stream with per-layer gated MLP networks and an auxiliary GAR loss. Training succeeds (TF GAR\,=\,0.50), but autoregressive GAR collapses 20--33$\times$ (exposure bias), confirmed on Llama-3.1-8B (27$\times$ by median). Inference-time steering ($\beta$\,=\,5, GAR 0.727) and scheduled sampling (gap ${\sim}$31$\times$$\to$1.57$\times$, no PPL cost, single seed) both demonstrate attention misallocation---not representation degradation---as the proximal cause.
4	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 102 · 2026-05-22T08:32:28.590528+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 103 · 2026-05-22T08:32:31.554164+00:00_

1	\section{Limitations}\label{sec:limitations}
2	
3	The five-way factorial uses seed\,=\,42; ThreadGate is additionally validated with seed\,=\,123 (TF/AR GAR-ours within $\pm$0.001, gap 30.5--32.1$\times$). The remaining three variants use a single seed; cross-variant convergence provides indirect robustness evidence but does not substitute for multi-seed validation.
4	
5	We test only one type of auxiliary attention loss (GAR with MSE target $\tau = 0.5$). Other attention steering objectives, such as head-specific or layer-specific attention losses, may exhibit different sensitivity to exposure bias. Our negative result applies to the GAR family; it does not rule out all auxiliary attention interventions.
6	
7	Training uses 8K conversations from UltraChat. Larger-scale training could alter gate dynamics, particularly if the model encounters sufficient distributional diversity to reduce the training-inference mismatch.
8	
9	All experiments use two model families (Qwen-2.5-7B and Llama-3.1-8B); while cross-model evaluation confirms the exposure bias gap, $N$\,=\,2 does not establish universality. The Llama evaluation includes ThreadGate and LoRA-only; the full five-way ablation (Uniform Gate, +PCGrad) has not been replicated, and all experiments use a single dataset (UltraChat). The instruction retention analysis is exploratory: a single model, 18 system-prompt constraint types, and a single $\beta$ value without grid search.
10	
11	The PCGrad causal exclusion addresses gradient direction conflict only. Magnitude imbalance (GradNorm; \citealp{chen2018gradnorm}) and Nash equilibrium approaches (Nash-MTL; \citealp{navon2022nash}) remain untested and could reveal additional failure modes or interaction effects.
12	
13	All four fine-tuned variants share the same GAR auxiliary loss. This design isolates the gating mechanism but does not test whether gating could be effective without an auxiliary attention loss or under a different training objective.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "Read",
  "elapsed_ms": 2963
}
```

</details>

---


### Tool call

_source line 104 · 2026-05-22T08:32:31.654935+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 105 · 2026-05-22T08:32:31.705609+00:00_

1	\section{Training Hyperparameters}\label{sec:appendix-hyper}
2	
3	All fine-tuned variants share the following configuration: Qwen-2.5-7B-Instruct base model, LoRA rank 16 ($\alpha$=32) on \texttt{q\_proj} and \texttt{v\_proj}, AdamW optimizer (lr = $2 \times 10^{-4}$, $\beta_1$=0.9, $\beta_2$=0.999), batch size 1 with gradient accumulation 8, 3 epochs over 8K UltraChat conversations, maximum sequence length 2048, seed 42. ThreadGate gates use a 10$\times$ learning rate multiplier and initial bias 1.5 ($\sigma(1.5) \approx 0.82$).
4	
5	\section{Loss Formulation Search}\label{sec:appendix-loss}
6	
7	Table~\ref{tab:loss-iterations} summarizes the seven loss configurations explored before arriving at the final MSE + gate diversity formulation (\S\ref{sec:loss}). Configurations v1--v6 span three alternative loss families; none converged during training.
8	
9	\begin{table}[h]
10	\centering\small
11	\caption{Loss formulation iterations on Qwen-2.5-7B-Instruct. GAR-ours (teacher-forced) and PPL are reported only for the converged configuration.}
12	\label{tab:loss-iterations}
13	\begin{tabular}{l l l c c}
14	\toprule
15	 & \textbf{Loss Family} & \textbf{Status} & \textbf{GAR} & \textbf{PPL} \\
16	\midrule
17	v1  & Cumulative            & \texttimes~GAR loss $\to$ 0     & ---  & ---  \\
18	v2  & Cumulative + $\varepsilon$ & \texttimes~same trajectory & ---  & ---  \\
19	v3  & Maximize ($\lambda$=2)  & \texttimes~gate frozen        & ---  & ---  \\
20	v3b & Maximize ($\lambda$=10) & \texttimes~identity collapse   & ---  & ---  \\
21	v5  & Maximize ($\lambda$=1)  & \texttimes~identity collapse   & ---  & ---  \\
22	v6  & Smooth saturation       & \texttimes~identity collapse   & ---  & ---  \\
23	v7  & MSE + gate div          & \checkmark~converged           & 0.50 & 2.78 \\
24	\bottomrule
25	\end{tabular}
26	\end{table}
27	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 106 · 2026-05-22T08:32:39.955934+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/references.bib"
  }
}
```

</details>

---


### Tool result

_source line 107 · 2026-05-22T08:32:40.898934+00:00_

1	% ============================================================
2	% Layer Importance
3	% ============================================================
4	
5	@inproceedings{gromov2024deeper,
6	  author    = {Gromov and others},
7	  title     = {{The Unreasonable Ineffectiveness of the Deeper Layers}},
8	  booktitle = {International Conference on Learning Representations},
9	  year      = {2024},
10	  url       = {https://arxiv.org/abs/2403.17887}
11	}
12	
13	@article{men2024shortgpt,
14	  author  = {Men and others},
15	  title   = {{ShortGPT: Layers in Large Language Models are More Redundant Than You Expect}},
16	  journal = {arXiv preprint arXiv:2403.03853},
17	  year    = {2024},
18	  url     = {https://arxiv.org/abs/2403.03853}
19	}
20	
21	@inproceedings{sun2025curse,
22	  author    = {Sun and others},
23	  title     = {{The Curse of Depth in Large Language Models}},
24	  booktitle = {Advances in Neural Information Processing Systems},
25	  year      = {2025},
26	  url       = {https://arxiv.org/abs/2502.05795}
27	}
28	
29	@article{lu2024reassessing,
30	  author  = {Lu, Yao and others},
31	  title   = {{Reassessing Layer Pruning in LLMs: New Insights and Methods}},
32	  journal = {arXiv preprint arXiv:2411.15558},
33	  year    = {2024},
34	  url     = {https://arxiv.org/abs/2411.15558}
35	}
36	
37	@inproceedings{fan2020layerdrop,
38	  author    = {Fan and others},
39	  title     = {{Reducing Transformer Depth on Demand with Structured Dropout (LayerDrop)}},
40	  booktitle = {International Conference on Learning Representations},
41	  year      = {2020},
42	  url       = {https://arxiv.org/abs/1909.11556}
43	}
44	
45	% ============================================================
46	% Multi-Turn Attention
47	% ============================================================
48	
49	@article{dongre2026attention,
50	  author  = {Dongre and Hsieh and Lai and Yoon and Bui and Hakkani-Tur},
51	  title   = {{When Attention Closes: How LLMs Lose the Thread in Multi-Turn Interac
…[truncated 16154 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "Read",
  "elapsed_ms": 942
}
```

</details>

---


### Tool call

_source line 108 · 2026-05-22T08:32:41.024904+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/agent/config.yaml 2>/dev/null | grep -A5 \"external_review\" || echo \"NO_CONFIG_OR_NO_EXTERNAL_REVIEW\"",
  "description": "Check external review config"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/agent/config.yaml 2>/dev/null | grep -A5 \"external_review\" || echo \"NO_CONFIG_OR_NO_EXTERNAL_REVIEW\"",
    "description": "Check external review config"
  }
}
```

</details>

---


### Tool result

_source line 109 · 2026-05-22T08:32:41.125689+00:00_

NO_CONFIG_OR_NO_EXTERNAL_REVIEW

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "Bash",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 110 · 2026-05-22T08:32:49.461560+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/agent/ -name \"*.yaml\" -o -name \"*.yml\" | head -10 && echo \"---\" && cat /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/agent/config.yaml 2>/dev/null || find /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/ -maxdepth 2 -name \"config*\" 2>/dev/null",
  "description": "Find project config file"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/agent/ -name \"*.yaml\" -o -name \"*.yml\" | head -10 && echo \"---\" && cat /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/agent/config.yaml 2>/dev/null || find /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/ -maxdepth 2 -name \"config*\" 2>/dev/null",
    "description": "Find project config file"
  }
}
```

</details>

---


### Tool result

_source line 111 · 2026-05-22T08:32:49.562388+00:00_

find: ‘/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/agent/’: No such file or directory
---
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.git/config

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "Bash",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 112 · 2026-05-22T08:32:54.603531+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_11/ -maxdepth 1 -name \"*.yaml\" -o -name \"*.yml\" | head -10 && echo \"---\" && ls /home/ubuntu/.agent-ml-research-idea_gen_0509_11/config* 2>/dev/null || echo \"no top config\" && cat /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/registry.yaml 2>/dev/null | head -30",
  "description": "Find external review config"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_11/ -maxdepth 1 -name \"*.yaml\" -o -name \"*.yml\" | head -10 && echo \"---\" && ls /home/ubuntu/.agent-ml-research-idea_gen_0509_11/config* 2>/dev/null || echo \"no top config\" && cat /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/registry.yaml 2>/dev/null | head -30",
    "description": "Find external review config"
  }
}
```

</details>

---


### Tool result

_source line 113 · 2026-05-22T08:32:54.704530+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_11/workspace.yaml
---
approvals.yaml
backend.yaml
claude_sessions.json
crons.yaml
email_tokens.json
feishu.yaml
keepalive.json
mcp_config.json
mcp_config_briefer.json
mcp_config_director.json
mcp_config_dream_review_director.json
mcp_config_no_project.json
mcp_config_paper_agent.json
mcp_config_review_director.json
mcp_config_review_reviewer_1.json
mcp_config_review_reviewer_2.json
mcp_config_reviewer.json
mcp_config_worker_011f2b23898fb17ffb1bfb29640bf50c.json
mcp_config_worker_0a99ddd77d013c2bbf51ffccc89dfcc9.json
mcp_config_worker_0aa51d591547913249ab7a68dc681be8.json
mcp_config_worker_116db043ffcfd41b2805e6feba9eb07d.json
mcp_config_worker_12093ef55c63229acbf88fd2b9106dce.json
mcp_config_worker_14d296b01755362efedfab08bc7a4e38.json
mcp_config_worker_193ba176326e072476b8e0add22cb54b.json
mcp_config_worker_197fc88774b454742a451a7d3e7c4259.json
mcp_config_worker_20757da2008e6f2d0301511436122d29.json
mcp_config_worker_29834432f6498e7996daf9a6d4e8eda9.json
mcp_config_worker_33c066fe8f41bfaa9b9c844bb47eca4f.json
mcp_config_worker_34467933ed5c0782ad72826a9574d432.json
mcp_config_worker_34a94861e96b7887a157fa6d27e375e0.json
mcp_config_worker_34b8beca3d3e38da8c29b9af314ca15a.json
mcp_config_worker_3683e51e3c097c93488562d683342ec7.json
mcp_config_worker_3ab953c77b6b0e7621a87cc89f47e64a.json
mcp_config_worker_4117895cca10a53e32a904aa47517ffe.json
mcp_config_worker_421decd2032b14f2ef6566c2172240c1.json
mcp_config_worker_4974dcce7f322a9c6739cc105546eff9.json
mcp_config_worker_52f0337c0eb747cb4b38db8eace91307.json
mcp_config_worker_5304abbd56fd7a7f12edca904ca28ec0.json
mcp_config_worker_567fac45f9ef5ad1a9223cbb3364faf1.json
mcp_config_worker_58a2c13c6faae79a50aeb3914e8975c6.json
mcp_config_worker_5fb1f955b45e38e31789286a1790398d.json
mcp_config_worker_62ef4f182cec190b443fa992f93a181e.json
mcp_config_worker_6679bd63c74f529fddfcffaa0a492c96.json
mcp_config_worker_69e382e805b6f185c49ecc4b6d1f2d44.json
mcp_config_worker_6fd17e67a8715a
…[truncated 3118 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "Bash",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 114 · 2026-05-22T08:32:58.123676+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_11/workspace.yaml 2>/dev/null | grep -A 10 \"external_review\" || echo \"NO_EXTERNAL_REVIEW_CONFIG\"",
  "description": "Check external review config in workspace"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_11/workspace.yaml 2>/dev/null | grep -A 10 \"external_review\" || echo \"NO_EXTERNAL_REVIEW_CONFIG\"",
    "description": "Check external review config in workspace"
  }
}
```

</details>

---


### Tool result

_source line 115 · 2026-05-22T08:32:58.174317+00:00_

NO_EXTERNAL_REVIEW_CONFIG

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 116 · 2026-05-22T08:33:39.251570+00:00_

called mcp__agent-ml-research__dispatch_visual_check

<details open><summary>🔧 Tool call — mcp__agent-ml-research__dispatch_visual_check</summary>

```json
{
  "project": "turn_residual_gating",
  "review_chat_id": "oc_9287ee173cf15d688adcd081f5d861f5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "tool_args": {
    "project": "turn_residual_gating",
    "review_chat_id": "oc_9287ee173cf15d688adcd081f5d861f5"
  }
}
```

</details>

---


### Tool result

_source line 117 · 2026-05-22T08:33:52.938821+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 13687
}
```

</details>

---


### Tool call

_source line 118 · 2026-05-22T08:33:55.764629+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "text": "你是 Reviewer 1，负责 **方法严谨性 + 实验设计** 审查。\n\n## Venue 信息\n- **目标 venue**: EMNLP 2026（通过 ARR August cycle 提交）\n- **Commitment deadline**: 2026-08-02\n- **格式**: ACL 模板, Long paper 正文 ≤8 页, 参考文献不限, Limitations 必填(不计页数)\n- **匿名**: Double-blind\n\n## 论文文件\n- LaTeX: `/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_1/submitted.pdf`\n\n## 审查侧重\n\n请重点评估以下方面：\n\n1. **因果推断链条的严谨性**：五路 factorial comparison 的设计是否真正隔离了声称的四个因素？每对对比的控制变量是否充分？PCGrad 因果排除（modus tollens）的逻辑是否成立？\n2. **统计功效与可靠性**：seed 数量是否足够支撑结论？20-33× gap 的 bootstrap CI/显著性检验？样本量（N=50 held-out, N=5/50 steering）的统计功效？\n3. **Exposure bias 归因的充分性**：是否存在其他未排除的替代解释？Scheduled sampling 实验（单 seed）能否充分验证归因？TRC 作为 orthogonal metric 是否真正正交？\n4. **实验可复现性**：超参数报告是否完整？训练/评估细节是否足以复现？代码/数据发布计划？\n5. **方法贡献 vs 经验发现**：ThreadGate 本身是否有方法论贡献，还是仅作为负面结果的载体？\n\n请按 ARR 标准格式输出审稿报告：Summary → Strengths → Weaknesses → Questions → Minor Issues → Overall Assessment（含评分和置信度）。Weaknesses 是重点——必须严格、不留情面。",
  "reviewer_id": "1",
  "project": "turn_residual_gating",
  "round_number": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "text": "你是 Reviewer 1，负责 **方法严谨性 + 实验设计** 审查。\n\n## Venue 信息\n- **目标 venue**: EMNLP 2026（通过 ARR August cycle 提交）\n- **Commitment deadline**: 2026-08-02\n- **格式**: ACL 模板, Long paper 正文 ≤8 页, 参考文献不限, Limitations 必填(不计页数)\n- **匿名**: Double-blind\n\n## 论文文件\n- LaTeX: `/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_1/submitted.pdf`\n\n## 审查侧重\n\n请重点评估以下方面：\n\n1. **因果推断链条的严谨性**：五路 factorial comparison 的设计是否真正隔离了声称的四个因素？每对对比的控制变量是否充分？PCGrad 因果排除（modus tollens）的逻辑是否成立？\n2. **统计功效与可靠性**：seed 数量是否足够支撑结论？20-33× gap 的 bootstrap CI/显著性检验？样本量（N=50 held-out, N=5/50 steering）的统计功效？\n3. **Exposure bias 归因的充分性**：是否存在其他未排除的替代解释？Scheduled sampling 实验（单 seed）能否充分验证归因？TRC 作为 orthogonal metric 是否真正正交？\n4. **实验可复现性**：超参数报告是否完整？训练/评估细节是否足以复现？代码/数据发布计划？\n5. **方法贡献 vs 经验发现**：ThreadGate 本身是否有方法论贡献，还是仅作为负面结果的载体？\n\n请按 ARR 标准格式输出审稿报告：Summary → Strengths → Weaknesses → Questions → Minor Issues → Overall Assessment（含评分和置信度）。Weaknesses 是重点——必须严格、不留情面。",
    "reviewer_id": "1",
    "project": "turn_residual_gating",
    "round_number": "1"
  }
}
```

</details>

---


### Tool result

_source line 119 · 2026-05-22T08:34:03.404125+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 7639
}
```

</details>

---


### Tool call

_source line 120 · 2026-05-22T08:34:05.572123+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "text": "你是 Reviewer 2，负责 **新颖性 + 完整性 + 格式** 审查。\n\n## Venue 信息\n- **目标 venue**: EMNLP 2026（通过 ARR August cycle 提交）\n- **Commitment deadline**: 2026-08-02\n- **格式**: ACL 模板, Long paper 正文 ≤8 页, 参考文献不限, Limitations 必填(不计页数)\n- **匿名**: Double-blind\n\n## 论文文件\n- LaTeX: `/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_1/submitted.pdf`\n\n## 审查侧重\n\n请重点评估以下方面：\n\n1. **新颖性与贡献声称**：论文声称的四项贡献（因果诊断框架、exposure bias 刻画、inference-time steering、负面 baseline）分别有多强？\"first empirical characterization\" 是否过度声称？负面结果论文在 EMNLP 的竞争力如何？\n2. **Related Work 覆盖度**：multi-turn degradation、residual gating、attention manipulation、exposure bias、multi-task gradient conflict 五个方向是否有重要遗漏？Li et al. (2024) split-softmax 的对比是否充分？\n3. **写作质量**：论证叙事是否清晰连贯？Abstract/Introduction 的 claim 是否与 Results 一致？标题是否准确反映内容？Discussion 是否恰当？\n4. **格式合规**：ARR/ACL 模板使用、页数限制、Limitations 章节、匿名性、引用格式（natbib）、图表质量\n5. **引用质量**：bib 条目格式一致性？是否有不可查证的引用（特别注意 Dongre et al. 2026）？是否有 orphan 条目？引用是否准确对应文中描述？\n\n请按 ARR 标准格式输出审稿报告：Summary → Strengths → Weaknesses → Questions → Minor Issues → Overall Assessment（含评分和置信度）。Weaknesses 是重点——必须严格、不留情面。",
  "reviewer_id": "2",
  "project": "turn_residual_gating",
  "round_number": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "text": "你是 Reviewer 2，负责 **新颖性 + 完整性 + 格式** 审查。\n\n## Venue 信息\n- **目标 venue**: EMNLP 2026（通过 ARR August cycle 提交）\n- **Commitment deadline**: 2026-08-02\n- **格式**: ACL 模板, Long paper 正文 ≤8 页, 参考文献不限, Limitations 必填(不计页数)\n- **匿名**: Double-blind\n\n## 论文文件\n- LaTeX: `/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_1/submitted.pdf`\n\n## 审查侧重\n\n请重点评估以下方面：\n\n1. **新颖性与贡献声称**：论文声称的四项贡献（因果诊断框架、exposure bias 刻画、inference-time steering、负面 baseline）分别有多强？\"first empirical characterization\" 是否过度声称？负面结果论文在 EMNLP 的竞争力如何？\n2. **Related Work 覆盖度**：multi-turn degradation、residual gating、attention manipulation、exposure bias、multi-task gradient conflict 五个方向是否有重要遗漏？Li et al. (2024) split-softmax 的对比是否充分？\n3. **写作质量**：论证叙事是否清晰连贯？Abstract/Introduction 的 claim 是否与 Results 一致？标题是否准确反映内容？Discussion 是否恰当？\n4. **格式合规**：ARR/ACL 模板使用、页数限制、Limitations 章节、匿名性、引用格式（natbib）、图表质量\n5. **引用质量**：bib 条目格式一致性？是否有不可查证的引用（特别注意 Dongre et al. 2026）？是否有 orphan 条目？引用是否准确对应文中描述？\n\n请按 ARR 标准格式输出审稿报告：Summary → Strengths → Weaknesses → Questions → Minor Issues → Overall Assessment（含评分和置信度）。Weaknesses 是重点——必须严格、不留情面。",
    "reviewer_id": "2",
    "project": "turn_residual_gating",
    "round_number": "1"
  }
}
```

</details>

---


### Tool result

_source line 121 · 2026-05-22T08:34:07.708422+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 2136
}
```

</details>

---


### Assistant

_source line 122 · 2026-05-22T08:34:14.044387+00:00_

已派发完毕：
- 视觉审查 Agent：已启动（fire-and-forget）
- Reviewer 1（方法严谨性 + 实验设计）：已分配
- Reviewer 2（新颖性 + 完整性 + 格式）：已分配

等待两位 Reviewer 完成 Round 1 独立初审。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director"
}
```

</details>

---


## Round 6

## Round 6

2 recorded events


### User

_source line 123 · 2026-05-22T08:40:05.386103+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 — Round 1 审稿报告

**论文**: "Why Lightweight Gating Fails to Fix Multi-Turn Attention Degradation: A Mechanistic Analysis"
**审查侧重**: 新颖性 + 完整性 + 格式

---

## Summary

本文提出 ThreadGate，一个 per-layer content-and-turn-conditioned MLP 门控机制，试图修复多轮对话中 attention 向 system prompt goal tokens 衰减的问题（以 GAR 指标衡量）。核心发现是**负面结果**：ThreadGate 在 teacher-forced 评估下 GAR 达到 0.50，但自回归生成时崩溃至 0.015–0.025（20–33× gap）。通过五路 factorial comparison 排除了门控机制、turn conditioning、梯度冲突等因素后，论文将失败归因于 exposure bias——辅助 attention loss 在 teacher forcing 下学到的模式无法迁移到自回归生成。Inference-time attention steering（β=5）恢复 GAR 至 0.727 提供了建设性证据。

---

## 总体评分

**Overall**: 3.0 (Findings)
**一句话总结**: 有价值的负面结果论文，但 "causal" 分析的过度声称、缺乏下游任务验证、以及关键实验的单 seed 问题使其止步于 Findings 级别。

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | Factorial 设计合理，但 "causal" 声称过度；缺少 GAR 与下游性能的关联验证 |
| Excitement | 3.0/5 | Exposure bias 选择性破坏辅助 objective 的发现有价值，但范围窄（1 指标×1 数据集×2 模型） |
| Reproducibility | 3.5/5 | 超参数提供完整，但多项关键结果为单 seed；未提及代码开源 |
| Confidence | 4/5 | 仔细阅读全文，熟悉 exposure bias、multi-task learning、attention manipulation 文献 |

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] GAR 指标的下游有效性未经验证

- 具体位置：全文（§1–§7 均以 GAR 为核心评估指标）；§6 Discussion "Instruction retention under steering" 段落
- 问题：论文的整个叙事建立在 "GAR 衰减导致多轮对话性能下降" 的前提上，但**从未展示 autoregressive GAR 的提升是否带来实际任务性能改善**。唯一的下游验证是 §6 的指令保留分析，但仅使用单模型、18 种 system prompt 约束、单一 β 值，且 McNemar 检验 p=0.077（不显著）。GAR-compliance 相关系数 r=0.200，关系极弱。
- 为什么影响接收：如果 GAR 改善不能转化为实际的指令遵循改善或生成质量提升，论文的全部分析就失去了实践意义。负面结果论文的价值取决于 "什么失败了" 是否重要——如果 GAR 本身不重要，ThreadGate 的失败就没有研究价值。
- 建议修改方向：在 §4 Experiments 或 §6 Discussion 中加入 β-steering 前后的**任务级评估**（如 constraint satisfaction rate、MT-Bench-101 子集、instruction following accuracy），证明 GAR 恢复确实改善了功能性指标。至少需要在 held-out 评估集上展示 β=3/5 时的生成质量对比。

**N2** [critical] "Causal" 分析框架严重过度声称

- 具体位置：§1 Contribution (1) "a systematic causal diagnostic framework"；§5 Analysis 标题及内容；§5.2 "PCGrad Causal Exclusion"
- 问题：论文反复使用 "causal" 一词（contribution list、section titles、analysis 全文），但实际方法论是**消融实验**（ablation study），而非真正的因果推断。PCGrad 排除了梯度方向冲突，但论文自身承认（§8 Limitations）梯度幅度不平衡（GradNorm）和 Nash 均衡方法未经测试。"Modus tollens" 论证（§5.2）形式上正确，但前提不完整——direction conflict 只是 gradient conflict 的一个维度，排除它不等于排除 gradient conflict 整体。
- 为什么影响接收：将消融研究包装为 "因果分析框架" 是对方法论的误导性呈现，违反了 soundness 标准。如果审稿人或读者按真正的因果推断标准来评判（如 do-calculus、instrument variables），论文会被认为不够格。
- 建议修改方向：将 "causal diagnostic framework" 改为 "systematic ablation framework" 或 "factorial diagnostic framework"；将 "causal exclusion" 改为 "ablation-based exclusion"；在 §5.2 中明确说明 PCGrad 只排除方向冲突而非梯度冲突的全部形式。

**N3** [critical] 关键引用的事实性错误——GAR 全称写错

- 具体位置：§3.1 Preliminaries ("Dongre et al. (2026) defined the Goal Attention Ratio (GAR)")；Abstract；Introduction；全文所有出现 "Goal Attention Ratio" 的地方
- 问题：经验证，Dongre et al. (2026)（arXiv:2605.12922）原文中 GAR 的全称是 **"Goal Accessibility Ratio"**，而非本文所写的 "Goal Attention Ratio"。这是对论文核心指标来源的事实性错误。
- 为什么影响接收：GAR 是本文的基础指标，对其来源的错误引用直接影响学术严谨性。审稿人和读者引用时会传播此错误。
- 建议修改方向：全文将 "Goal Attention Ratio" 更正为 "Goal Accessibility Ratio"，或如果作者有意采用不同命名，需在 §3.1 明确说明 "Dongre et al. (2026) introduced the Goal Accessibility Ratio (GAR); we adopt this metric under the name Goal Attention Ratio to emphasize..." 并提供理由。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] 关键结果的统计可靠性不足——单 seed 问题

- 具体位置：§6 Discussion "Scheduled sampling" 段落；§4.1 Setup (seed=42, ThreadGate additionally seed=123)；§8 Limitations 第一段
- 问题：Scheduled sampling 结果（gap 从 ~31× 压缩到 1.57×）是**单 seed** 实验。这是全文最具可操作性的发现，但缺乏统计验证。论文提到第二个 seed（从 scratch 训练）得到 AR GAR=0.418（gap 1.20×），但这不是同一配置的重复，而是不同起点的变体——5% seed variance 的对比标的和 scheduled sampling 的变异性无法直接比较。Factorial 中除 ThreadGate 外其余变体也只有单 seed。
- 建议：为 scheduled sampling 至少补充 3 个 seed 的结果（mean ± std），验证 1.57× gap 的可重复性。对 factorial 中的其余变体补充第二个 seed 的验证。

**W2** [warning] Exposure bias 归因存在 underdetermination

- 具体位置：§5.3 Distribution Shift Analysis；§4.3 Inference-Time Attention Steering
- 问题：论文将 20–33× GAR gap 归因于 exposure bias，但证据链存在替代解释：
  - Teacher-forced 下 GAR 工作、自回归下不工作 → 这与 exposure bias 一致，但也可能是任何训练-推理分布差异造成的（如 KV cache 动态、长度外推、自回归 token 的 representation drift）
  - β-steering 恢复 GAR → 这证明 attention misallocation 可以被修复，但不证明 exposure bias 是其原因
  - Scheduled sampling 部分修复 → 与 exposure bias 一致，但 scheduled sampling 改变了训练动态的多个方面，不仅仅是 exposure
- 建议：在 §5.3 中讨论替代假说并说明为什么 exposure bias 是最简约的解释，而非唯一的解释。将 "the proximal cause" 软化为 "a proximal cause consistent with our evidence"。

**W3** [warning] Li et al. (2024) split-softmax 缺乏实验对比

- 具体位置：§2 Related Work "Instruction stability" 段落；§6 Discussion
- 问题：Li et al. (2024) 的 split-softmax 是本文最直接的竞争方法——同样针对多轮对话中 instruction attention 衰减，且同样是 inference-time intervention。论文在 Related Work 和 Discussion 中两次提及 split-softmax 但只说 "complementary"，从未进行实验对比。对于声称发现 "inference-time steering recovers GAR" 的论文，不与同类 inference-time 方法对比是显著遗漏。
- 建议：在 §4.3 或 §6 中加入 split-softmax 的对比实验，或至少定性分析两种方法的机制差异及适用场景。

**W4** [warning] 写作冗余度高——同一数字重复 5–6 次

- 具体位置：Abstract、§1 Introduction、§4.2 Main Results、§5.3 Distribution Shift、§6 Discussion、§7 Conclusion
- 问题："20–33× gap"、"0.015–0.025"、"0.064 to 0.727" 等关键数字在 Abstract、Introduction、Experiments、Analysis、Discussion、Conclusion 中各出现一次以上。Abstract 本身就是 Introduction + Results 的压缩重复。这使论文读起来像是在用不同措辞反复陈述同一发现，而非逐步深入分析。在 8 页正文限制下，这些重复占用了本可用于更多分析（如下游评估、额外 seed、split-softmax 对比）的空间。
- 建议：将数字的首次精确呈现放在 §4，Abstract/Introduction 只给高层结论（如 "an order-of-magnitude gap"），Discussion/Conclusion 侧重 implication 而非重复数据。

**W5** [warning] Scheduled sampling 结果应从 Discussion 提升至正式实验

- 具体位置：§6 Discussion "Scheduled sampling as training-time mitigation" 段落
- 问题：Scheduled sampling 将 gap 从 ~31× 压缩到 1.57× 且无 PPL 损失，这是全文最具实践价值的发现，但被放在 Discussion 中作为 "preliminary experiment"。这一发现本身比主实验（ThreadGate 失败）更有 actionable insight，但因位置和 framing 被降级。如果进行多 seed 验证后确认，它应该是论文的核心贡献之一。
- 建议：补充多 seed 实验后将 scheduled sampling 提升为 §4 的正式子节（§4.4），或在 Discussion 中给予更突出的位置和更详细的分析。

**W6** [warning] Contribution (1) 过度声称泛化性

- 具体位置：§1 Contribution (1) "this design pattern is in principle applicable to other auxiliary objective analyses"
- 问题：论文只测试了一种辅助目标（GAR with MSE target τ=0.5）。声称框架 "in principle applicable to other auxiliary objective analyses" 是未经验证的泛化。§8 Limitations 第二段承认了这一点，但 Contribution list 中的声明仍然成立。
- 建议：在 Contribution (1) 中加入限定语："we demonstrate this framework on GAR-family losses; its applicability to other auxiliary objectives remains to be validated"。

---

## 小问题（不影响接收）

- **Dongre et al. (2026) 发表时间极近**（arXiv:2605.12922, 2026年5月13日发布）：作为本文的基础参考，审稿人需注意该参考在投稿时可能仅发布数周，其结论尚未经过社区验证。
- **bib 格式不一致**：部分条目用 "and others"（如 Gromov and others），部分列出完整作者（如 Yu, Kumar, Gupta, Levine, Hausman, Finn）。应统一处理。
- **Figure 1 信息密度过高**：Overview 图包含大量文字标注和颜色编码，在打印或小屏幕上可能难以辨认。建议简化标注。
- **§3.1 中 GAR-Dongre 和 GAR-ours 的区分**：虽然论文解释了两种变体的差异，但后续 §4–§5 中频繁切换使用，偶尔容易混淆。建议在首次引入后统一使用一种简写约定。
- **Appendix 较薄**：仅包含 Training Hyperparameters 和 Loss Formulation Search 两个小节，缺少 scheduled sampling 的详细配置、steering 实验的完整结果、cross-model 实验的补充数据等。
- **标题 "Why Lightweight Gating Fails"**：标题暗示论文解释了失败原因，但 exposure bias 作为解释已是 well-known phenomenon。更准确的标题应强调论文的真正发现：exposure bias 选择性破坏辅助 attention objective。

---

## 主要优势

- **S1**: 五路 factorial 实验设计干净且有系统性，逐步排除因素的逻辑链清晰（turn conditioning → gating mechanism → gradient conflict → exposure bias）
- **S2**: Exposure bias 选择性破坏辅助 attention objective（而非主 NTP 目标）的发现具有新颖性，现有 exposure bias 文献聚焦生成质量，未涉及 auxiliary distributional objectives
- **S3**: Inference-time β-steering 提供了建设性的正面证据，将负面结果论文从 "什么不行" 提升为 "什么不行 + 为什么 + 什么可以行"
- **S4**: Cross-model 验证（Llama-3.1-8B, 27× gap）增加了结论的泛化性
- **S5**: 论文的 scope 和 limitations 表述诚实——§8 明确列出了未测试的方面（GradNorm、Nash-MTL、其他辅助目标、更多模型/数据集），这在负面结果论文中尤为重要
- **S6**: ARR guidelines 明确鼓励负面结果论文的发表，本文的结论（lightweight gating + auxiliary attention loss 在 exposure bias 下无效）对后续研究者有避坑价值

---

## Questions for Authors

1. 是否尝试过在自回归 GAR 评估中使用 sampling temperature > 0 或 nucleus sampling？当前的自回归评估使用的是 greedy decoding 还是其他策略？不同解码策略是否影响 GAR collapse 的程度？
2. Scheduled sampling 的 linear mixing schedule 具体参数是什么（起始比例、终止比例、总步数）？是否尝试过其他 schedule（exponential、inverse sigmoid）？
3. β-steering 恢复 GAR 的同时，生成文本的**内容质量**如何变化？是否有人工评估或自动评估（如 GPT-4 judge）的结果？
4. 为什么选择 τ=0.5 作为 GAR 目标？base model 的 GAR-ours 在 turn 1 只有 0.0418——直接将目标设为 0.5（12× 放大）是否过于激进？是否尝试过更温和的目标（如 τ=0.1 或 0.2）？

---

**Reviewer 2 评分汇总**: Overall 3.0 (Findings) | Soundness 3.5 | Excitement 3.0 | Reproducibility 3.5 | Confidence 4

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 124 · 2026-05-22T08:40:26.068380+00:00_

已收到 Reviewer 2 的 Round 1 审稿报告（Overall 3.0 / Findings）。

关键发现记录：
- **N1** [critical]: GAR 指标缺乏下游任务验证，全文实践意义悬空
- **N2** [critical]: "Causal" 框架过度声称，实为消融实验
- **N3** [critical]: GAR 全称写错——原文是 "Goal Accessibility Ratio" 非 "Goal Attention Ratio"
- **W1-W6**: 单 seed、exposure bias 归因 underdetermination、缺 split-softmax 对比、写作冗余、scheduled sampling 定位偏低、贡献泛化过度声称

等待 Reviewer 1 的报告到达后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director"
}
```

</details>

---


## Round 7

## Round 7

6 recorded events


### User

_source line 125 · 2026-05-22T08:40:27.459449+00:00_

[Reviewer 2 审稿结果]:
审稿报告已提交给 Review Director。

核心发现总结：

**Overall: 3.0 (Findings)**，3 个 Must-Fix + 6 个 Should-Fix。

**三个 Must-Fix 问题：**
1. **GAR 指标缺乏下游任务验证** — 全文围绕 GAR 展开但从未证明 GAR 改善能带来实际任务性能提升，唯一的指令保留分析 p=0.077 不显著
2. **"Causal" 分析框架过度声称** — 实际是消融实验，PCGrad 只排除了梯度方向冲突而非梯度冲突整体，不应包装为因果推断
3. **GAR 全称写错** — Dongre et al. (2026) 原文是 "Goal Accessibility Ratio"，本文全文写成 "Goal Attention Ratio"，属于对核心指标来源的事实性错误

**主要优势：** 五路 factorial 设计干净、exposure bias 选择性破坏辅助 objective 的发现有新颖性、inference-time steering 提供了建设性正面证据。

---

[Reviewer 1 审稿意见]:
## Reviewer 1 审稿报告：方法严谨性 + 实验设计

### 总体评分
**Overall**: 3.0 / 5（Findings）
**一句话总结**: 系统性诊断轻量 gating 失败机制的负面结果论文，核心洞察有价值，但统计功效严重不足，因果归因链存在逻辑缺口。

### 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.0 / 5 | 因果框架合理但关键实验单 seed、PCGrad 因果排除不完备（仅覆盖方向冲突）、scheduled sampling 两个 seed 结果差异 31% |
| Excitement | 3.0 / 5 | 负面结果有社区价值，exposure bias 对辅助目标的选择性破坏是新发现，但方法贡献有限 |
| Reproducibility | 3 / 5 | 超参数基本完整，但未提及代码/数据发布计划，UltraChat 8K 筛选标准未说明 |
| Confidence | 4 / 5 | 熟悉 attention mechanism、exposure bias、multi-task learning 文献 |

---

### Must-Fix 问题（3 个 critical）

**N1** [critical] 统计功效严重不足——五路对比中 4/5 条件为单 seed
- 位置：Section 4.1、Table 1、Section 8
- 核心 claim "四个 fine-tuned variants 收敛到 0.75 pp 以内"（Section 4.2）没有方差估计，无法做统计检验。单 seed 下 0.75 pp 差异可能完全在 seed variance 范围内。ARR 标准 R5 要求主要结果需统计显著性评估。
- 建议：每个 variant 至少跑 3 seed，报告 mean±std，做配对检验。

**N2** [critical] PCGrad 因果排除逻辑不完备——仅排除方向冲突，忽略幅度失衡
- 位置：Section 5.2、Section 8
- PCGrad 仅解决梯度方向冲突，不解决幅度失衡（NTP 梯度幅度是 GAR 的 7.5–14.7 倍）。正文 claim "gradient conflict is not the cause"，实际只能 claim "directional gradient conflict is not the cause"。幅度优势本身可能是 gates 被推向 identity 的机制（Section 5.1）。GradNorm 未测试是重大遗漏。
- 建议：测试 GradNorm，或精确限定 claim 为 directional conflict。

**N3** [critical] Exposure bias 归因存在未排除的替代解释
- 位置：Section 5.3、Section 6
- 证据链缺口：(1) Inference-time steering 证明 misallocation 可修正，不等于 exposure bias 是原因；(2) Scheduled sampling 改变整个训练分布，不仅是 exposure bias；(3) 未排除 KV cache 累积方式差异（TF 一次性计算 vs AR 逐 token 追加）作为独立原因。
- 建议：设计实验区分 exposure bias 和 KV cache 效应，或弱化 claim 为 "training-inference distributional mismatch"。

---

### Should-Fix 问题（6 个 warning）

**W1** [warning] GAR 缺乏下游任务效果验证——唯一尝试 McNemar p=0.077（不显著），r=0.200
- 位置：Section 6

**W2** [warning] Table 1 缺少 autoregressive GAR 数据——论文最关键发现（20–33× gap）只在正文口头描述，未在表格中呈现
- 位置：Table 1

**W3** [warning] "五路 factorial comparison" 命名不当——实际是消融研究（5/16 条件），无交互效应检验
- 位置：Section 1、Section 4.1

**W4** [warning] Scheduled sampling 两个 seed 使用不同训练协议（resumed vs from scratch），无法分离效应
- 位置：Section 6

**W5** [warning] 标题 overclaim——"Lightweight Gating" 暗示一类方法，实际仅测试 ThreadGate 一种
- 位置：标题

**W6** [warning] Cross-model validation 不完整——Llama 仅 3/5 条件，N=20，未复现 PCGrad
- 位置：Section 5.5

---

### 小问题
- 页数边界：Conclusion (Section 7) 起始于第 9 页顶部，可能轻微超 8 页正文限制
- "20–33× gap" 表述可能误导——fine-tuned AR GAR (0.015–0.025) 实际比 Base (0.01) 有改善
- Introduction 与 Abstract 重复度过高
- Bib 部分条目用 "and others" 代替完整作者列表

---

### 主要优势
1. 负面结果的系统性诊断有社区价值（ARR guidelines 明确支持）
2. PCGrad 作为因果分析工具的使用有新意
3. Inference-time steering 提供 constructive evidence（GAR 0.064→0.727）
4. 写作逻辑清晰：观察→干预→失败→诊断→归因→验证
5. TRC 作为 orthogonal metric 增强了 selectivity 论点

---

### Questions to Authors
1. 为什么没有测试 GradNorm？NTP/GAR 梯度幅度差 7.5–14.7× 是比方向冲突更直接的候选原因。
2. UltraChat 8K 的筛选标准？
3. AR GAR 崩溃时模型生成文本质量如何？有 case study 吗？
4. Scheduled sampling seed 2 用不同协议的原因？
5. τ=0.5 选取依据？测试过其他 target 值吗？

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 126 · 2026-05-22T08:41:00.940161+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "text": "以下是 Reviewer 2 的完整审稿意见，请逐条回应：对每个 Must-Fix 和 Should-Fix，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 — Round 1 审稿报告\n\n**论文**: \"Why Lightweight Gating Fails to Fix Multi-Turn Attention Degradation: A Mechanistic Analysis\"\n**审查侧重**: 新颖性 + 完整性 + 格式\n\n---\n\n### Must-Fix 问题\n\n**N1** [critical] GAR 指标的下游有效性未经验证\n- 全文以 GAR 为核心评估指标，但从未展示 autoregressive GAR 的提升是否带来实际任务性能改善。唯一的下游验证是 §6 的指令保留分析，但仅使用单模型、18 种 system prompt 约束、单一 β 值，且 McNemar 检验 p=0.077（不显著）。GAR-compliance 相关系数 r=0.200，关系极弱。\n\n**N2** [critical] \"Causal\" 分析框架严重过度声称\n- 论文反复使用 \"causal\" 一词，但实际方法论是消融实验。PCGrad 排除了梯度方向冲突，但论文自身承认梯度幅度不平衡和 Nash 均衡方法未经测试。将消融研究包装为 \"因果分析框架\" 是对方法论的误导性呈现。\n\n**N3** [critical] GAR 全称写错\n- Dongre et al. (2026) 原文中 GAR 的全称是 \"Goal Accessibility Ratio\"，而非本文所写的 \"Goal Attention Ratio\"。这是对论文核心指标来源的事实性错误。\n\n### Should-Fix 问题\n\n**W1** 关键结果的统计可靠性不足——单 seed 问题\n**W2** Exposure bias 归因存在 underdetermination\n**W3** Li et al. (2024) split-softmax 缺乏实验对比\n**W4** 写作冗余度高——同一数字重复 5–6 次\n**W5** Scheduled sampling 结果应从 Discussion 提升至正式实验\n**W6** Contribution (1) 过度声称泛化性\n\n### 主要优势\n- S1: 五路 factorial 实验设计干净且有系统性\n- S2: Exposure bias 选择性破坏辅助 attention objective 的发现具有新颖性\n- S3: Inference-time β-steering 提供了建设性的正面证据\n- S4: Cross-model 验证增加了结论的泛化性\n- S5: Scope 和 limitations 表述诚实\n- S6: ARR guidelines 明确鼓励负面结果论文\n\n### Questions for Authors\n1. 是否尝试过不同解码策略？\n2. Scheduled sampling 的具体 mixing schedule 参数？\n3. β-steering 恢复 GAR 的同时内容质量变化？\n4. 为什么选择 τ=0.5 作为 GAR 目标？\n\n---\n\n请逐条回应每个 Must-Fix (N1-N3) 和 Should-Fix (W1-W6)。",
  "reviewer_id": "1",
  "project": "turn_residual_gating",
  "round_number": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "text": "以下是 Reviewer 2 的完整审稿意见，请逐条回应：对每个 Must-Fix 和 Should-Fix，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 — Round 1 审稿报告\n\n**论文**: \"Why Lightweight Gating Fails to Fix Multi-Turn Attention Degradation: A Mechanistic Analysis\"\n**审查侧重**: 新颖性 + 完整性 + 格式\n\n---\n\n### Must-Fix 问题\n\n**N1** [critical] GAR 指标的下游有效性未经验证\n- 全文以 GAR 为核心评估指标，但从未展示 autoregressive GAR 的提升是否带来实际任务性能改善。唯一的下游验证是 §6 的指令保留分析，但仅使用单模型、18 种 system prompt 约束、单一 β 值，且 McNemar 检验 p=0.077（不显著）。GAR-compliance 相关系数 r=0.200，关系极弱。\n\n**N2** [critical] \"Causal\" 分析框架严重过度声称\n- 论文反复使用 \"causal\" 一词，但实际方法论是消融实验。PCGrad 排除了梯度方向冲突，但论文自身承认梯度幅度不平衡和 Nash 均衡方法未经测试。将消融研究包装为 \"因果分析框架\" 是对方法论的误导性呈现。\n\n**N3** [critical] GAR 全称写错\n- Dongre et al. (2026) 原文中 GAR 的全称是 \"Goal Accessibility Ratio\"，而非本文所写的 \"Goal Attention Ratio\"。这是对论文核心指标来源的事实性错误。\n\n### Should-Fix 问题\n\n**W1** 关键结果的统计可靠性不足——单 seed 问题\n**W2** Exposure bias 归因存在 underdetermination\n**W3** Li et al. (2024) split-softmax 缺乏实验对比\n**W4** 写作冗余度高——同一数字重复 5–6 次\n**W5** Scheduled sampling 结果应从 Discussion 提升至正式实验\n**W6** Contribution (1) 过度声称泛化性\n\n### 主要优势\n- S1: 五路 factorial 实验设计干净且有系统性\n- S2: Exposure bias 选择性破坏辅助 attention objective 的发现具有新颖性\n- S3: Inference-time β-steering 提供了建设性的正面证据\n- S4: Cross-model 验证增加了结论的泛化性\n- S5: Scope 和 limitations 表述诚实\n- S6: ARR guidelines 明确鼓励负面结果论文\n\n### Questions for Authors\n1. 是否尝试过不同解码策略？\n2. Scheduled sampling 的具体 mixing schedule 参数？\n3. β-steering 恢复 GAR 的同时内容质量变化？\n4. 为什么选择 τ=0.5 作为 GAR 目标？\n\n---\n\n请逐条回应每个 Must-Fix (N1-N3) 和 Should-Fix (W1-W6)。",
    "reviewer_id": "1",
    "project": "turn_residual_gating",
    "round_number": "1"
  }
}
```

</details>

---


### Tool result

_source line 127 · 2026-05-22T08:41:09.504455+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 8564
}
```

</details>

---


### Tool call

_source line 128 · 2026-05-22T08:41:10.813050+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "text": "以下是 Reviewer 1 的完整审稿意见，请逐条回应：对每个 Must-Fix 和 Should-Fix，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 1 审稿报告：方法严谨性 + 实验设计\n\n**Overall**: 3.0 / 5（Findings）\n\n### Must-Fix 问题（3 个 critical）\n\n**N1** [critical] 统计功效严重不足——五路对比中 4/5 条件为单 seed\n- 核心 claim \"四个 fine-tuned variants 收敛到 0.75 pp 以内\"（Section 4.2）没有方差估计，无法做统计检验。单 seed 下 0.75 pp 差异可能完全在 seed variance 范围内。\n\n**N2** [critical] PCGrad 因果排除逻辑不完备——仅排除方向冲突，忽略幅度失衡\n- PCGrad 仅解决梯度方向冲突，不解决幅度失衡（NTP 梯度幅度是 GAR 的 7.5–14.7 倍）。正文 claim \"gradient conflict is not the cause\"，实际只能 claim \"directional gradient conflict is not the cause\"。GradNorm 未测试是重大遗漏。\n\n**N3** [critical] Exposure bias 归因存在未排除的替代解释\n- (1) Inference-time steering 证明 misallocation 可修正，不等于 exposure bias 是原因；(2) Scheduled sampling 改变整个训练分布，不仅是 exposure bias；(3) 未排除 KV cache 累积方式差异（TF 一次性计算 vs AR 逐 token 追加）作为独立原因。\n\n### Should-Fix 问题（6 个 warning）\n\n**W1** GAR 缺乏下游任务效果验证——唯一尝试 McNemar p=0.077（不显著），r=0.200\n**W2** Table 1 缺少 autoregressive GAR 数据——论文最关键发现（20–33× gap）只在正文口头描述\n**W3** \"五路 factorial comparison\" 命名不当——实际是消融研究（5/16 条件），无交互效应检验\n**W4** Scheduled sampling 两个 seed 使用不同训练协议（resumed vs from scratch），无法分离效应\n**W5** 标题 overclaim——\"Lightweight Gating\" 暗示一类方法，实际仅测试 ThreadGate 一种\n**W6** Cross-model validation 不完整——Llama 仅 3/5 条件，N=20，未复现 PCGrad\n\n### 主要优势\n1. 负面结果的系统性诊断有社区价值\n2. PCGrad 作为因果分析工具的使用有新意\n3. Inference-time steering 提供 constructive evidence\n4. 写作逻辑清晰\n5. TRC 作为 orthogonal metric 增强了 selectivity 论点\n\n### Questions to Authors\n1. 为什么没有测试 GradNorm？\n2. UltraChat 8K 的筛选标准？\n3. AR GAR 崩溃时模型生成文本质量如何？\n4. Scheduled sampling seed 2 用不同协议的原因？\n5. τ=0.5 选取依据？\n\n---\n\n请逐条回应每个 Must-Fix (N1-N3) 和 Should-Fix (W1-W6)。",
  "reviewer_id": "2",
  "project": "turn_residual_gating",
  "round_number": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "text": "以下是 Reviewer 1 的完整审稿意见，请逐条回应：对每个 Must-Fix 和 Should-Fix，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 1 审稿报告：方法严谨性 + 实验设计\n\n**Overall**: 3.0 / 5（Findings）\n\n### Must-Fix 问题（3 个 critical）\n\n**N1** [critical] 统计功效严重不足——五路对比中 4/5 条件为单 seed\n- 核心 claim \"四个 fine-tuned variants 收敛到 0.75 pp 以内\"（Section 4.2）没有方差估计，无法做统计检验。单 seed 下 0.75 pp 差异可能完全在 seed variance 范围内。\n\n**N2** [critical] PCGrad 因果排除逻辑不完备——仅排除方向冲突，忽略幅度失衡\n- PCGrad 仅解决梯度方向冲突，不解决幅度失衡（NTP 梯度幅度是 GAR 的 7.5–14.7 倍）。正文 claim \"gradient conflict is not the cause\"，实际只能 claim \"directional gradient conflict is not the cause\"。GradNorm 未测试是重大遗漏。\n\n**N3** [critical] Exposure bias 归因存在未排除的替代解释\n- (1) Inference-time steering 证明 misallocation 可修正，不等于 exposure bias 是原因；(2) Scheduled sampling 改变整个训练分布，不仅是 exposure bias；(3) 未排除 KV cache 累积方式差异（TF 一次性计算 vs AR 逐 token 追加）作为独立原因。\n\n### Should-Fix 问题（6 个 warning）\n\n**W1** GAR 缺乏下游任务效果验证——唯一尝试 McNemar p=0.077（不显著），r=0.200\n**W2** Table 1 缺少 autoregressive GAR 数据——论文最关键发现（20–33× gap）只在正文口头描述\n**W3** \"五路 factorial comparison\" 命名不当——实际是消融研究（5/16 条件），无交互效应检验\n**W4** Scheduled sampling 两个 seed 使用不同训练协议（resumed vs from scratch），无法分离效应\n**W5** 标题 overclaim——\"Lightweight Gating\" 暗示一类方法，实际仅测试 ThreadGate 一种\n**W6** Cross-model validation 不完整——Llama 仅 3/5 条件，N=20，未复现 PCGrad\n\n### 主要优势\n1. 负面结果的系统性诊断有社区价值\n2. PCGrad 作为因果分析工具的使用有新意\n3. Inference-time steering 提供 constructive evidence\n4. 写作逻辑清晰\n5. TRC 作为 orthogonal metric 增强了 selectivity 论点\n\n### Questions to Authors\n1. 为什么没有测试 GradNorm？\n2. UltraChat 8K 的筛选标准？\n3. AR GAR 崩溃时模型生成文本质量如何？\n4. Scheduled sampling seed 2 用不同协议的原因？\n5. τ=0.5 选取依据？\n\n---\n\n请逐条回应每个 Must-Fix (N1-N3) 和 Should-Fix (W1-W6)。",
    "reviewer_id": "2",
    "project": "turn_residual_gating",
    "round_number": "1"
  }
}
```

</details>

---


### Tool result

_source line 129 · 2026-05-22T08:41:12.478796+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1665
}
```

</details>

---


### Assistant

_source line 130 · 2026-05-22T08:41:18.052910+00:00_

交叉分享已发出。等待两位 Reviewer 的逐条回应。

当前进度：
- **Step 0–0.7**：✅ 资料检查 + Venue 调研 + Reviewer 编排 + 视觉审查派发
- **Step 1**：✅ Round 1 独立审稿完成（R1: 3.0, R2: 3.0）
- **Step 2**：⏳ 交叉分享已发出，等待回应
- **Step 3–4**：待交叉回应收集后执行

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director"
}
```

</details>

---


## Round 8

## Round 8

4 recorded events


### User

_source line 131 · 2026-05-22T08:41:19.568049+00:00_

[Reviewer 1 审稿结果]:
审稿报告已提交给 Review Director。

总结：Overall 3.0/5（Findings 档位）。3 个 critical 问题：(1) 统计功效不足（4/5 条件单 seed）；(2) PCGrad 因果排除不完备（忽略梯度幅度失衡）；(3) exposure bias 归因存在未排除的替代解释。6 个 warning 级问题涉及 GAR 下游验证缺失、Table 1 缺 AR 数据、factorial 命名不当、scheduled sampling 协议混淆、标题 overclaim、cross-model 验证不完整。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 132 · 2026-05-22T08:41:25.361618+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_local_file",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_local_file",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 133 · 2026-05-22T08:41:25.412330+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Assistant

_source line 134 · 2026-05-22T08:41:50.381996+00:00_

已收到 Reviewer 1 初审报告确认。交叉分享任务已发出，等待两位 Reviewer 的交叉回应（[AGREE]/[REBUT]）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director"
}
```

</details>

---


## Round 9

## Round 9

2 recorded events


### User

_source line 135 · 2026-05-22T08:42:54.346791+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 对 Reviewer 1 审稿意见的逐条回应

---

### Must-Fix 问题

**[AGREE] R1-N1: 统计功效不足——4/5 条件单 seed**

同意这是 critical 问题。论文在 §4.2 声称 "GAR-ours spans only 0.75 percentage points" 作为 "all four fine-tuned variants converge to nearly identical performance" 的证据，但这是**单次观测**的点估计，没有置信区间。ThreadGate 的双 seed 验证（seed 42 vs 123，§4.2 末段 "TF GAR-ours 0.504±0.001"）仅覆盖 1/5 条件。

补充我的观察：这一问题在 scheduled sampling 上更严重（我的 W1）——那是全文最有价值的 actionable 发现（gap 31× → 1.57×），却只有单 seed，且第二个 seed 用了不同训练协议（§6 Discussion），使得仅有的两个数据点也不可比。在 8 页篇幅限制下，3 个 seed 的 scheduled sampling 验证比当前 §5 Analysis 中的部分重复性分析更有边际价值。

**[AGREE] R1-N2: PCGrad 因果排除逻辑不完备**

完全同意。这与我的 N2 一致。论文 §5.2 使用 modus tollens 论证："if direction conflict causes the failure, removing it should prevent it; PCGrad removes it; the failure persists; therefore direction conflict is not the cause"——但这个三段论的大前提过窄。实际只能得出 "directional gradient conflict（在 gate parameters 上的）is not the cause"。

具体未排除的路径：
1. **幅度失衡**（§5.2 明确记录 NTP 梯度幅度 7.5–14.7× GAR，但未用 GradNorm 测试）
2. **PCGrad 的作用范围**——§5.2 明确说 "We apply PCGrad to gate parameters only"，LoRA 参数上的梯度冲突完全未触及
3. **Nash 均衡效应**（§8 Limitations 承认 Nash-MTL 未测试）

论文在 Contribution (1) 中将此包装为 "systematic causal diagnostic framework"，但漏掉 2/3 的梯度冲突维度的排除不能称为 "systematic"。建议 R1 的修改方向完全合理——应将 claim 降级为 "directional gradient conflict on gate parameters"。

**[AGREE with nuance] R1-N3: Exposure bias 归因的替代解释**

大体同意，与我的 W2 方向一致，但我对 R1 提出的 KV cache 假说有细微补充。

R1 提出的三个替代解释中：
- **(1) β-steering 不等于 exposure bias 是原因**：完全同意。§4.3 的 steering 实验证明 attention misallocation 是可修复的 proximal failure，但不证明 exposure bias 是导致该 misallocation 的 root cause。论文在 §4.3 末段试图等价这两者（"providing constructive evidence that attention misallocation—not representation degradation—is the proximal cause of exposure-bias-induced GAR failure"），但这是 circulat reasoning——将 "exposure-bias-induced" 嵌入结论本身。
- **(2) Scheduled sampling 改变多个训练动态因素**：同意。Scheduled sampling 除了缓解 exposure bias，还改变了 loss landscape、梯度分布、甚至隐式 data augmentation 效果。
- **(3) KV cache 差异**：这是一个有趣的替代假说，我未在初轮审稿中提出。不过我认为这个假说的解释力有限——现代 transformer 实现中，TF 和 AR 的 attention 计算在数学上应该是等价的（区别仅在 KV 是一次算还是逐步追加），因此 KV cache 差异更可能导致**数值精度差异**而非 20–33× 的系统性 GAR 崩溃。但论文确实应该讨论并排除这一可能。

**总结**：论文的证据与 exposure bias 解释**一致但非排他**。建议将 "the proximal cause" 降级为 "a proximal cause consistent with our converging evidence"，并在 Discussion 中列出并讨论替代假说。

---

### Should-Fix 问题

**[AGREE] R1-W1: GAR 缺乏下游任务验证**

强烈同意——我将此列为 **N1 (critical)**，比 R1 的定级（warning）更高。理由同我的初轮审稿：如果 GAR 改善不能转化为实际任务性能提升，论文全部分析的实践意义存疑。§6 Discussion 中的 instruction retention 分析（McNemar p=0.077, r=0.200）不仅不显著，而且效应量极小，无法作为 GAR 下游有效性的支撑。

**[AGREE] R1-W2: Table 1 缺少 autoregressive GAR 数据**

同意，这是一个明显的呈现缺陷。论文的核心发现是 teacher-forced 与 autoregressive GAR 之间 20–33× 的 gap，但 Table 1 只呈现了 teacher-forced 的 IID/held-out 数据。AR GAR 数字散见于 §4.2 正文描述（"GAR-ours drops to 0.015–0.025"）和 §5.3，但从未以表格形式系统呈现。读者需要在多个段落间拼凑关键数据，这在负面结果论文中尤其有问题——结论的说服力高度依赖数据的系统性呈现。

建议：在 Table 1 中增加 "Autoregressive" 列（或新建 Table 2），与 TF 数据并列呈现，并加入 TF/AR ratio 列。

**[AGREE] R1-W3: "Factorial comparison" 命名不当**

同意。真正的 factorial design（4 因素 × 2 水平）应有 2⁴=16 条件并检验交互效应。论文的 5 条件是结构化消融（每次添加/移除一个因素），只能测试主效应，无法检测因素间交互。例如："turn conditioning 在有/无 PCGrad 下效果是否不同？" 这类问题当前设计无法回答。

不过我要补充：即使命名不准确，5 条件的消融设计本身是**合理且有信息量的**——它成功展示了没有任何单一因素（gating、turn conditioning、gradient conflict elimination）能 rescue autoregressive GAR。问题在于用语（"factorial"），而非实验设计本身的价值。

**[AGREE] R1-W4: Scheduled sampling 两个 seed 的训练协议不同**

同意。§6 Discussion 描述 seed 1 为标准训练，seed 2 "trained from scratch (rather than resumed from a standard-trained epoch)"——这意味着两个 seed 不仅随机初始化不同，训练流程也不同。将它们视为同一实验的 replication 是方法论错误。AR GAR 从 0.318（seed 1, resumed）到 0.418（seed 2, from scratch）的差异可能来自训练协议差异而非 seed variance。

论文实际上用 seed 2 的结果推导了一个有趣的猜测（"early scheduled sampling exposure...may further compress the gap"），但这个 observation 基于 N=1 的对比，不具备推断力。

**[REBUT] R1-W5: 标题 overclaim "Lightweight Gating"**

部分反驳。R1 认为标题用 "Lightweight Gating" 暗示一类方法但只测试了 ThreadGate 一种，我认为论文的实验设计部分回应了这一批评：

- §4 的 5 条件中 **Uniform Gate**（无 turn embedding 的门控）和 **LoRA-only**（门控固定为 1.0）共同表明，gating mechanism 本身（而非 ThreadGate 的特定实现）不提供 benefit——Table 1 显示所有变体 GAR-ours 收敛到 0.50–0.51
- §5.1 Gate Turn Conditioning 分析（27/28 层门控值在 late turns 趋近 1.0）表明这是 NTP pressure 对任何标量门控的压制，机制上不限于 ThreadGate

但我同意标题的模糊性确实存在——"Lightweight Gating" 可以包含 MoE-style 路由、token-level gating 等完全不同的机制，论文未测试这些。建议修改为更精确的表述，如 "per-layer residual gating" 或 "scalar residual gating"。

**[AGREE] R1-W6: Cross-model validation 不完整**

同意。Llama-3.1-8B 实验（§5.5）只复现了 3/5 条件（Base, ThreadGate, LoRA-only），缺少 +PCGrad 和 Uniform Gate。虽然 Qwen 上 PCGrad 和 Uniform Gate 的结果与 ThreadGate/LoRA-only 无差异，但在 Llama 上未验证这一点就声称 cross-model generality 是不完整的。此外 N=20（vs Qwen 的 N=50），且用 median 而非 mean 报告结果（因 heavy-tailed distributions），进一步降低了统计功效。

---

### 总结

R1 的 3 个 Must-Fix 中我**全部同意**（N3 附加细微补充）。6 个 Should-Fix 中我**同意 5 个**（W1-W4, W6），**部分反驳 1 个**（W5 标题 overclaim）。

值得注意的是，R1 和我的审稿在多个关键问题上独立收敛：
- **统计可靠性/单 seed 问题**（R1-N1 ↔ 我的 W1）
- **PCGrad/"causal" 过度声称**（R1-N2 ↔ 我的 N2）
- **Exposure bias 归因的 underdetermination**（R1-N3 ↔ 我的 W2）
- **GAR 下游有效性缺失**（R1-W1 ↔ 我的 N1）

两位 reviewer 独立识别相同核心问题增强了这些问题的可信度。我的评分维持不变：**Overall 3.0 (Findings)**。论文作为负面结果有社区价值，但 overclaim 和验证不足使其暂不满足主会议接收标准。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 136 · 2026-05-22T08:43:02.844555+00:00_

Reviewer 2 交叉回应已收到。等待 Reviewer 1 对 Reviewer 2 的交叉回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director"
}
```

</details>

---


## Round 10

## Round 10

10 recorded events


### User

_source line 137 · 2026-05-22T08:43:04.161387+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 交叉回应 Reviewer 2

### Must-Fix 逐条回应

**[AGREE] R2-N1 (GAR 下游有效性)**: 同意，与我的 W1 一致。Section 6 的 McNemar p=0.077 不显著，r=0.200 极弱。如果 GAR 恢复对任务表现无意义，论文 motivation 根基不成立。列为 Critical 合理。

**[AGREE with nuance] R2-N2 ("Causal" overclaim)**: 基本同意，与我的 W3+N2 一致。但 modus tollens 推理形式本身合法，问题在于 PCGrad 只移除方向冲突这一子维度，前提不完备导致结论过宽。建议保留推理框架但限定 scope（"directional gradient conflict" → not "gradient conflict"），去掉 "causal" 标签改用 "systematic diagnostic"。

**[REBUT] R2-N3 (GAR 全称错误)**: 无法独立证实此 claim。但即使属实，反对列为 Critical。理由：(1) Eq. 1 定义自包含，"Attention Ratio" 描述性准确（字面计算 attention weights）；(2) 修改成本极低；(3) 不影响方法论/结论。应降为 Minor。请 R2 提供 Dongre et al. 原文具体 Section/Page 佐证。

### Should-Fix 逐条回应

**[AGREE] R2-W1 (单 seed)**: 完全同意，与我的 N1 (Critical) 一致。我认为严重性应高于 R2 定级。

**[AGREE] R2-W2 (Exposure bias underdetermination)**: 同意，与我的 N3 (Critical) 一致。

**[AGREE with caveat] R2-W3 (split-softmax 对比)**: 部分同意，但属于 ARR H13 ("extra experiments beyond claims")。论文 scope 是诊断 gating 失败，不是 benchmark 所有修复方法。应作为建议而非 weakness。

**[AGREE] R2-W4 (写作冗余)**: 同意。

**[AGREE with caveat] R2-W5 (Scheduled sampling 提升)**: 方向同意但有重要前提——当前仅 2 seed 且协议不同（差异 31%），提升为正式实验前必须先补 ≥3 seed 统一协议数据，否则反而削弱证据标准。

**[AGREE] R2-W6 (Contribution 1 泛化性 overclaim)**: 同意。

### 两位 Reviewer 共识
1. 统计功效不足（R1 列 Critical，R2 列 Should-Fix）
2. Exposure bias 归因 underdetermination（两者均认为核心问题）
3. GAR 下游有效性未验证
4. "Causal/factorial" 标签 overclaim
5. 写作冗余

### 分歧
- R2-N3（GAR 全称）：R2 列 Critical，R1 认为应降为 Minor
- Scheduled sampling 提升：R2 建议直接提升，R1 认为须先补 multi-seed

---

[Reviewer 2 审稿结果]:
已将逐条回应提交给 Review Director。

核心结论：R1 的 3 个 Must-Fix 全部同意（N3 附加 KV cache 假说的补充讨论），6 个 Should-Fix 同意 5 个、部分反驳 1 个（W5 标题 overclaim——论文的 Uniform Gate + LoRA-only 消融部分回应了 "只测一种方法" 的批评，但标题确实应更精确）。两位 reviewer 在四个核心问题上独立收敛：单 seed 统计可靠性、PCGrad causal 过度声称、exposure bias 归因 underdetermination、GAR 下游有效性缺失。评分维持 Overall 3.0 (Findings)。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 138 · 2026-05-22T08:43:27.557683+00:00_

called mcp__agent-ml-research__get_visual_check_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_visual_check_status</summary>

```json
{
  "project": "turn_residual_gating"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "tool_args": {
    "project": "turn_residual_gating"
  }
}
```

</details>

---


### Tool result

_source line 139 · 2026-05-22T08:43:27.679068+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"done\", \"started_at\": \"2026-05-22T08:33:43.778645+00:00\", \"completed_at\": \"2026-05-22T08:37:03.474478+00:00\", \"findings\": [{\"severity\": \"info\", \"dimension\": \"page 1\", \"message\": \"首页无视觉锚点（纯 Abstract + Introduction 文本）。Figure 1 出现在 page 2 顶部（全宽概览图），在前 3 页内，可接受。Title/Author/Abstract 排版整洁专业。\"}, {\"severity\": \"info\", \"dimension\": \"page 2\", \"message\": \"Figure 1 概览图信息密度高，有效传达 Observation→Intervention→Root Cause 框架。但内部文字标签（如 colored box 中的小字、公式 x_l = x_l + g · f(x_l)）在缩小打印时可能偏小，建议适当增大关键标签字号或简化非核心细节。\"}, {\"severity\": \"info\", \"dimension\": \"page 2\", \"message\": \"Figure 1 caption 较长且自包含，能独立理解图表核心信息，符合规范。\"}, {\"severity\": \"info\", \"dimension\": \"pages 3-4\", \"message\": \"连续 2 页无 figure/table（Related Work + Method Preliminaries），但 page 4 包含 7 个公式，提供了充分的视觉节奏。理论/方法叙述密集段落，属合理例外。\"}, {\"severity\": \"info\", \"dimension\": \"page 4\", \"message\": \"公式 (1)-(7) 渲染正确，无 LaTeX 残留错误，行距正常，display math 与行内公式混用得当。\"}, {\"severity\": \"info\", \"dimension\": \"page 5\", \"message\": \"Figure 2 线图清晰，teacher-forced 与 autoregressive 曲线对比明确，有置信区间阴影。Legend 可读。Y 轴标签和 tick 字号尚可。\"}, {\"severity\": \"info\", \"dimension\": \"page 6\", \"message\": \"Table 1 使用 booktabs 风格（水平线，无竖线），格式规范。小数精度一致（2 位）。但由于核心发现是\\\"所有 fine-tuned variants 性能接近\\\"，最优值未加粗标注——虽然此处差异极小（0.75 pp），仍建议对 GAR-O 最高值加粗以符合惯例。\"}, {\"severity\": \"info\", \"dimension\": \"page 6\", \"message\": \"Figure 3 双面板 subfigure（bar chart + 注释），展示 inference-time attention steering 结果。面板内标注文字（如 \\\"High / results are consistent\\\"）字号偏小但仍可读。Caption 自包含。\"}, {\"severity\": \"warning\", \"dimension\": \"page 7\", \"message\": \"Figure 4（2 panels）和 Figure 5（2 panels）共 4 个子图压缩在同一页。轴标签、tick marks、legend 字号明显偏小（目测 ≤6pt），尤其 Figure 4(a) 的 per-layer bar chart 和 Figure 5(a) 的 cosine similarity 曲线标注在打印尺寸下接近可读下限。建议：(1) 将 Figure 4 或 5 之一移至 page 8 以分散密度；(2) 增大子图字号至 ≥8pt。\"}, {\"severity\": \"warning\", \"dimension\": \"pages 8-9\", \"message\": \"连续 2 页纯文本无任
…[truncated 1416 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 121
}
```

</details>

---


### Tool call

_source line 140 · 2026-05-22T08:43:27.710981+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "turn_residual_gating"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "turn_residual_gating"
  }
}
```

</details>

---


### Tool result

_source line 141 · 2026-05-22T08:43:27.778649+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 67
}
```

</details>

---


### Tool call

_source line 142 · 2026-05-22T08:49:07.231742+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "turn_residual_gating",
  "issues_yaml": "# Review Issues Tracker — turn_residual_gating\n# Round 1 (2026-05-19, dream_20260519T145320)\n# Round 2 (2026-05-22, fresh re-review of revised paper)\n\n# ============================================================\n# Issues from Round 1 — status updates based on Round 2\n# ============================================================\n\n- id: \"R1-N1\"\n  summary: \"所有引用渲染为 '?'——bibliography 编译失败\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"Dream paper artifact。\"\n    - round: 2\n      reviewers: []\n      note: \"视觉审查确认无 [?] 未解析引用。已修复。\"\n  action_items:\n    - round: 1\n      action: \"Paper Agent 确保 bibtex 编译正确\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"Round 2 视觉审查确认已修复。\"\n  resolution_round: 2\n\n- id: \"R1-N2\"\n  summary: \"单种子支撑结论——统计功效不足\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"Bootstrap CI 仅覆盖 eval variance，不覆盖 training variance。\"\n    - round: 2\n      reviewers: [1, 2]\n      note: \"ThreadGate 已补 seed=123，但其余 4/5 条件仍为单 seed。SS 仅 1 seed 且第二 seed 协议不同不可比。两位 Reviewer 独立列为 Critical。\"\n  action_items:\n    - round: 1\n      action: \"plan_019: seed=123 extra training\"\n      assigned_to: agent\n      status: done\n    - round: 2\n      action: \"每个 variant 至少 3 seed (mean±std + 配对检验)。SS 优先。\"\n      assigned_to: agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-N3\"\n  summary: \"评估样本量过小\"\n  category: experiment\n  severity: info\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1]\n      note: \"Cohen's d≈0.22 在 n=50 下 power 不足。\"\n    - round: 2\n      reviewers: []\n      note: \"Round 2 使用 N=50 held-out + N=50 steering + N=20 Llama。未再被提出。\"\n  action_items: []\n  resolution: \"N=50 评估已在论文中体现。\"\n  resolution_round: 2\n\n- id: \"R1-N4\"\n  summary: \"损失函数超参数和 v1-v6 配置定义缺失\"\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"v1-v7 配置仅报告 v7。\"\n    - round: 2\n      reviewers: []\n      note: \"§3.3 报告 λ_GAR=λ_div=1.0。Appendix Table 2 列出 v1-v7。未再被提出。\"\n  action_items: []\n  resolution: \"§3.3 + Appendix B Table 2 已提供完整信息。\"\n  resolution_round: 2\n\n- id: \"R2-N1\"\n  summary: \"Novelty/causal 声称过高——'causal diagnostic framework' 过度包装\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"'first quantitative measurement' overclaim。\"\n    - round: 2\n      reviewers: [1, 2]\n      note: \"Round 1 overclaim 已降级，但 Round 2 发现新 overclaim：Contribution (1) 'systematic causal diagnostic framework' 实际是消融。PCGrad 仅覆盖方向冲突。'factorial' 是 5 条件消融非 16 条件。两位 Reviewer 均 Critical。\"\n  action_items:\n    - round: 1\n      action: \"'first quantitative measurement' 降级\"\n      assigned_to: director\n      status: done\n    - round: 2\n      action: \"'causal' → 'systematic diagnostic/ablation'；限定 PCGrad scope；修正 'factorial' 命名\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-N2\"\n  summary: \"标题过度声称\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"'Cannot Fix' → 已改为 'Fails to Fix'。\"\n    - round: 2\n      reviewers: [1, 2]\n      note: \"'Lightweight Gating' 暗示一类方法但仅测试 ThreadGate。R2 部分反驳（UG+LO 消融已部分覆盖）。建议改为 'per-layer/scalar residual gating'。\"\n  action_items:\n    - round: 2\n      action: \"标题改为更精确表述\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-N3\"\n  summary: \"Dongre et al. (2026) 引用准确性 + GAR 全称\"\n  category: format\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"论文动机链依赖此引用。\"\n    - round: 2\n      reviewers: [2]\n      note: \"R2 指出 Dongre 原文为 'Goal Accessibility Ratio'，本文写为 'Goal Attention Ratio'。R1 反驳（定义自包含）。Director 裁定 Warning。\"\n  action_items:\n    - round: 2\n      action: \"确认 Dongre 原文全称并更正或说明差异理由\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-N4\"\n  summary: \"Related Work 缺失 gradient conflict 文献 + PCGrad baseline\"\n  category: framing\n  severity: info\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"如果 PCGrad 能解决梯度竞争，论文核心结论悬空。\"\n    - round: 2\n      reviewers: []\n      note: \"PCGrad 已纳入五路对比，§2 已覆盖 gradient conflict 文献。\"\n  action_items: []\n  resolution: \"PCGrad 已纳入五路对比 + Related Work 已覆盖。\"\n  resolution_round: 2\n\n- id: \"R1-W1\"\n  summary: \"Llama 跨模型消融不完整（缺 PCGrad + Uniform Gate）\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"边际信息量不值 6h GPU。\"\n    - round: 2\n      reviewers: [1, 2]\n      note: \"仍仅 3/5 条件，N=20，用 median。两位 Reviewer 再次指出。\"\n  action_items:\n    - round: 2\n      action: \"补充 Llama PCGrad+UG，或论文明确说明理由\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-W2\"\n  summary: \"无 λ_GAR 敏感性消融\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - round: 1\n      reviewers: [1]\n      note: \"梯度冲突取决于 λ_GAR。\"\n    - round: 2\n      reviewers: []\n      note: \"§3.3 报告 λ=1.0 但仍无敏感性分析。未被 Round 2 reviewer 独立提出为 must-fix。\"\n  action_items:\n    - round: 1\n      action: \"plan_022: λ_GAR=10 敏感性测试\"\n      assigned_to: agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-W3\"\n  summary: \"训练数据量混淆变量\"\n  category: experiment\n  severity: info\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1]\n      note: \"1,000 convs 偏少。\"\n    - round: 2\n      reviewers: []\n      note: \"Round 2 使用 8K conversations。\"\n  action_items: []\n  resolution: \"训练数据量增加至 8K。\"\n  resolution_round: 2\n\n- id: \"R1-W4\"\n  summary: \"全文零 figure\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"Dream paper artifact.\"\n    - round: 2\n      reviewers: []\n      note: \"Round 2 有 5 figures + 2 tables。\"\n  action_items: []\n  resolution: \"Figure 1-5 + Table 1-2 已就位。\"\n  resolution_round: 2\n\n- id: \"R1-W5\"\n  summary: \"Scheduled sampling 统计支撑不足\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"单 seed，单 ratio，PPL 未报告。\"\n    - round: 2\n      reviewers: [1, 2]\n      note: \"PPL 已报告，但仍单 seed，第二 seed 协议不同不可比。\"\n  action_items:\n    - round: 2\n      action: \"补充 ≥3 seed 统一协议 SS 实验\"\n      assigned_to: agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-W6\"\n  summary: \"Reverse turn conditioning 证据间接\"\n  category: experiment\n  severity: info\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1]\n      note: \"差异可能是噪声。\"\n  resolution: \"Wilcoxon p=3.73e-8, r=0.975。已在 §5.1 报告。\"\n  resolution_round: 2\n\n- id: \"R2-W1\"\n  summary: \"范围过窄——仅标量门控不代表 lightweight gating 类别\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"未测试 vector gate 等变体。\"\n    - round: 2\n      reviewers: [1, 2]\n      note: \"标题仍为 'Lightweight Gating'。R2 部分反驳。建议更精确标题。\"\n  action_items:\n    - round: 2\n      action: \"标题改为更精确表述，或 Limitations 讨论 scope\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-W3\"\n  summary: \"GAR 单指标依赖——缺乏下游任务验证\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"r=0.82 sanity check 不足以作为 gold-standard proxy。\"\n    - round: 2\n      reviewers: [1, 2]\n      note: \"§6 instruction retention 分析 McNemar p=0.077 不显著，r=0.200 极弱。两位 Reviewer 升级为 Critical。\"\n  action_items:\n    - round: 2\n      action: \"加入 β-steering 前后任务级评估（constraint satisfaction, instruction following accuracy）\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-W5\"\n  summary: \"liu2016attention 引用可能错配\"\n  category: format\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [2]\n      note: \"语音识别 vs 注意力引导。\"\n    - round: 2\n      reviewers: []\n      note: \"Round 2 未提及，待确认。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-W6\"\n  summary: \"Bib 格式不一致 + orphan 条目\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"vaswani2017, elhage2021, olsson2022, efron1994。\"\n    - round: 2\n      reviewers: [2]\n      note: \"部分用 'and others' 部分列完整作者，格式不一致。\"\n  action_items:\n    - round: 2\n      action: \"统一 bib 格式，清理 orphan 条目\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-MISC\"\n  summary: \"无代码/数据发布\"\n  category: format\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"负面结果论文可复现性最后防线。\"\n    - round: 2\n      reviewers: [1]\n      note: \"仍未提及代码开源。Reproducibility 3.0/5。\"\n  action_items:\n    - round: 2\n      action: \"投稿前准备匿名 GitHub repo\"\n      assigned_to: agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# New issues from Round 2\n# ============================================================\n\n- id: \"R2-C3\"\n  summary: \"Exposure bias 归因存在未排除的替代解释\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - round: 2\n      reviewers: [1, 2]\n      note: \"β-steering 不等于 exposure bias 是原因（循环论证）；SS 改变多个训练动态；KV cache 差异未排除。\"\n  action_items:\n    - round: 2\n      action: \"'the proximal cause' → 'a proximal cause consistent with evidence'；Discussion 讨论替代假说\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-W1-new\"\n  summary: \"Table 1 缺少 autoregressive GAR 数据\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - round: 2\n      reviewers: [1, 2]\n      note: \"核心发现 20-33× gap 未在表格中系统呈现。\"\n  action_items:\n    - round: 2\n      action: \"Table 1 增加 AR 列或新建 Table 2\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-W4-new\"\n  summary: \"写作冗余——关键数字在多个 section 重复\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - round: 2\n      reviewers: [1, 2]\n      note: \"'20-33× gap' 等在 Abstract/Intro/Experiments/Analysis/Discussion/Conclusion 各出现多次。\"\n  action_items:\n    - round: 2\n      action: \"Abstract/Intro 用高层结论，Discussion/Conclusion 侧重 implication\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-W6-new\"\n  summary: \"Contribution (1) 过度声称泛化性\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - round: 2\n      reviewers: [1, 2]\n      note: \"'in principle applicable to other auxiliary objective analyses' 未经验证。\"\n  action_items:\n    - round: 2\n      action: \"加入限定语或删除泛化声称\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-W7-new\"\n  summary: \"Li et al. (2024) split-softmax 缺乏实验对比\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - round: 2\n      reviewers: [2]\n      note: \"最直接竞争 inference-time 方法。R1 认为超出 scope。定为建议。\"\n  action_items:\n    - round: 2\n      action: \"加入 split-softmax 对比或定性机制分析\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "turn_residual_gating",
    "issues_yaml": "# Review Issues Tracker — turn_residual_gating\n# Round 1 (2026-05-19, dream_20260519T145320)\n# Round 2 (2026-05-22, fresh re-review of revised paper)\n\n# ============================================================\n# Issues from Round 1 — status updates based on Round 2\n# ============================================================\n\n- id: \"R1-N1\"\n  summary: \"所有引用渲染为 '?'——bibliography 编译失败\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"Dream paper artifact。\"\n    - round: 2\n      reviewers: []\n      note: \"视觉审查确认无 [?] 未解析引用。已修复。\"\n  action_items:\n    - round: 1\n      action: \"Paper Agent 确保 bibtex 编译正确\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"Round 2 视觉审查确认已修复。\"\n  resolution_round: 2\n\n- id: \"R1-N2\"\n  summary: \"单种子支撑结论——统计功效不足\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"Bootstrap CI 仅覆盖 eval variance，不覆盖 training variance。\"\n    - round: 2\n      reviewers: [1, 2]\n      note: \"ThreadGate 已补 seed=123，但其余 4/5 条件仍为单 seed。SS 仅 1 seed 且第二 seed 协议不同不可比。两位 Reviewer 独立列为 Critical。\"\n  action_items:\n    - round: 1\n      action: \"plan_019: seed=123 extra training\"\n      assigned_to: agent\n      status: done\n    - round: 2\n      action: \"每个 variant 至少 3 seed (mean±std + 配对检验)。SS 优先。\"\n      assigned_to: agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-N3\"\n  summary: \"评估样本量过小\"\n  category: experiment\n  severity: info\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1]\n      note: \"Cohen's d≈0.22 在 n=50 下 power 不足。\"\n    - round: 2\n      reviewers: []\n      note: \"Round 2 使用 N=50 held-out + N=50 steering + N=20 Llama。未再被提出。\"\n  action_items: []\n  resolution: \"N=50 评估已在论文中体现。\"\n  resolution_round: 2\n\n- id: \"R1-N4\"\n  summary: \"损失函数超参数和 v1-v6 配置定义缺失\"\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"v1-v7 配置仅报告 v7。\"\n    - round: 2\n      reviewers: []\n      note: \"§3.3 报告 λ_GAR=λ_div=1.0。Appendix Table 2 列出 v1-v7。未再被提出。\"\n  action_items: []\n  resolution: \"§3.3 + Appendix B Table 2 已提供完整信息。\"\n  resolution_round: 2\n\n- id: \"R2-N1\"\n  summary: \"Novelty/causal 声称过高——'causal diagnostic framework' 过度包装\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"'first quantitative measurement' overclaim。\"\n    - round: 2\n      reviewers: [1, 2]\n      note: \"Round 1 overclaim 已降级，但 Round 2 发现新 overclaim：Contribution (1) 'systematic causal diagnostic framework' 实际是消融。PCGrad 仅覆盖方向冲突。'factorial' 是 5 条件消融非 16 条件。两位 Reviewer 均 Critical。\"\n  action_items:\n    - round: 1\n      action: \"'first quantitative measurement' 降级\"\n      assigned_to: director\n      status: done\n    - round: 2\n      action: \"'causal' → 'systematic diagnostic/ablation'；限定 PCGrad scope；修正 'factorial' 命名\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-N2\"\n  summary: \"标题过度声称\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"'Cannot Fix' → 已改为 'Fails to Fix'。\"\n    - round: 2\n      reviewers: [1, 2]\n      note: \"'Lightweight Gating' 暗示一类方法但仅测试 ThreadGate。R2 部分反驳（UG+LO 消融已部分覆盖）。建议改为 'per-layer/scalar residual gating'。\"\n  action_items:\n    - round: 2\n      action: \"标题改为更精确表述\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-N3\"\n  summary: \"Dongre et al. (2026) 引用准确性 + GAR 全称\"\n  category: format\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"论文动机链依赖此引用。\"\n    - round: 2\n      reviewers: [2]\n      note: \"R2 指出 Dongre 原文为 'Goal Accessibility Ratio'，本文写为 'Goal Attention Ratio'。R1 反驳（定义自包含）。Director 裁定 Warning。\"\n  action_items:\n    - round: 2\n      action: \"确认 Dongre 原文全称并更正或说明差异理由\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-N4\"\n  summary: \"Related Work 缺失 gradient conflict 文献 + PCGrad baseline\"\n  category: framing\n  severity: info\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"如果 PCGrad 能解决梯度竞争，论文核心结论悬空。\"\n    - round: 2\n      reviewers: []\n      note: \"PCGrad 已纳入五路对比，§2 已覆盖 gradient conflict 文献。\"\n  action_items: []\n  resolution: \"PCGrad 已纳入五路对比 + Related Work 已覆盖。\"\n  resolution_round: 2\n\n- id: \"R1-W1\"\n  summary: \"Llama 跨模型消融不完整（缺 PCGrad + Uniform Gate）\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"边际信息量不值 6h GPU。\"\n    - round: 2\n      reviewers: [1, 2]\n      note: \"仍仅 3/5 条件，N=20，用 median。两位 Reviewer 再次指出。\"\n  action_items:\n    - round: 2\n      action: \"补充 Llama PCGrad+UG，或论文明确说明理由\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-W2\"\n  summary: \"无 λ_GAR 敏感性消融\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - round: 1\n      reviewers: [1]\n      note: \"梯度冲突取决于 λ_GAR。\"\n    - round: 2\n      reviewers: []\n      note: \"§3.3 报告 λ=1.0 但仍无敏感性分析。未被 Round 2 reviewer 独立提出为 must-fix。\"\n  action_items:\n    - round: 1\n      action: \"plan_022: λ_GAR=10 敏感性测试\"\n      assigned_to: agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-W3\"\n  summary: \"训练数据量混淆变量\"\n  category: experiment\n  severity: info\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1]\n      note: \"1,000 convs 偏少。\"\n    - round: 2\n      reviewers: []\n      note: \"Round 2 使用 8K conversations。\"\n  action_items: []\n  resolution: \"训练数据量增加至 8K。\"\n  resolution_round: 2\n\n- id: \"R1-W4\"\n  summary: \"全文零 figure\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"Dream paper artifact.\"\n    - round: 2\n      reviewers: []\n      note: \"Round 2 有 5 figures + 2 tables。\"\n  action_items: []\n  resolution: \"Figure 1-5 + Table 1-2 已就位。\"\n  resolution_round: 2\n\n- id: \"R1-W5\"\n  summary: \"Scheduled sampling 统计支撑不足\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"单 seed，单 ratio，PPL 未报告。\"\n    - round: 2\n      reviewers: [1, 2]\n      note: \"PPL 已报告，但仍单 seed，第二 seed 协议不同不可比。\"\n  action_items:\n    - round: 2\n      action: \"补充 ≥3 seed 统一协议 SS 实验\"\n      assigned_to: agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-W6\"\n  summary: \"Reverse turn conditioning 证据间接\"\n  category: experiment\n  severity: info\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1]\n      note: \"差异可能是噪声。\"\n  resolution: \"Wilcoxon p=3.73e-8, r=0.975。已在 §5.1 报告。\"\n  resolution_round: 2\n\n- id: \"R2-W1\"\n  summary: \"范围过窄——仅标量门控不代表 lightweight gating 类别\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"未测试 vector gate 等变体。\"\n    - round: 2\n      reviewers: [1, 2]\n      note: \"标题仍为 'Lightweight Gating'。R2 部分反驳。建议更精确标题。\"\n  action_items:\n    - round: 2\n      action: \"标题改为更精确表述，或 Limitations 讨论 scope\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-W3\"\n  summary: \"GAR 单指标依赖——缺乏下游任务验证\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"r=0.82 sanity check 不足以作为 gold-standard proxy。\"\n    - round: 2\n      reviewers: [1, 2]\n      note: \"§6 instruction retention 分析 McNemar p=0.077 不显著，r=0.200 极弱。两位 Reviewer 升级为 Critical。\"\n  action_items:\n    - round: 2\n      action: \"加入 β-steering 前后任务级评估（constraint satisfaction, instruction following accuracy）\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-W5\"\n  summary: \"liu2016attention 引用可能错配\"\n  category: format\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [2]\n      note: \"语音识别 vs 注意力引导。\"\n    - round: 2\n      reviewers: []\n      note: \"Round 2 未提及，待确认。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-W6\"\n  summary: \"Bib 格式不一致 + orphan 条目\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"vaswani2017, elhage2021, olsson2022, efron1994。\"\n    - round: 2\n      reviewers: [2]\n      note: \"部分用 'and others' 部分列完整作者，格式不一致。\"\n  action_items:\n    - round: 2\n      action: \"统一 bib 格式，清理 orphan 条目\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-MISC\"\n  summary: \"无代码/数据发布\"\n  category: format\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"负面结果论文可复现性最后防线。\"\n    - round: 2\n      reviewers: [1]\n      note: \"仍未提及代码开源。Reproducibility 3.0/5。\"\n  action_items:\n    - round: 2\n      action: \"投稿前准备匿名 GitHub repo\"\n      assigned_to: agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# New issues from Round 2\n# ============================================================\n\n- id: \"R2-C3\"\n  summary: \"Exposure bias 归因存在未排除的替代解释\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - round: 2\n      reviewers: [1, 2]\n      note: \"β-steering 不等于 exposure bias 是原因（循环论证）；SS 改变多个训练动态；KV cache 差异未排除。\"\n  action_items:\n    - round: 2\n      action: \"'the proximal cause' → 'a proximal cause consistent with evidence'；Discussion 讨论替代假说\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-W1-new\"\n  summary: \"Table 1 缺少 autoregressive GAR 数据\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - round: 2\n      reviewers: [1, 2]\n      note: \"核心发现 20-33× gap 未在表格中系统呈现。\"\n  action_items:\n    - round: 2\n      action: \"Table 1 增加 AR 列或新建 Table 2\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-W4-new\"\n  summary: \"写作冗余——关键数字在多个 section 重复\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - round: 2\n      reviewers: [1, 2]\n      note: \"'20-33× gap' 等在 Abstract/Intro/Experiments/Analysis/Discussion/Conclusion 各出现多次。\"\n  action_items:\n    - round: 2\n      action: \"Abstract/Intro 用高层结论，Discussion/Conclusion 侧重 implication\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-W6-new\"\n  summary: \"Contribution (1) 过度声称泛化性\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - round: 2\n      reviewers: [1, 2]\n      note: \"'in principle applicable to other auxiliary objective analyses' 未经验证。\"\n  action_items:\n    - round: 2\n      action: \"加入限定语或删除泛化声称\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-W7-new\"\n  summary: \"Li et al. (2024) split-softmax 缺乏实验对比\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - round: 2\n      reviewers: [2]\n      note: \"最直接竞争 inference-time 方法。R1 认为超出 scope。定为建议。\"\n  action_items:\n    - round: 2\n      action: \"加入 split-softmax 对比或定性机制分析\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null"
  }
}
```

</details>

---


### Tool result

_source line 143 · 2026-05-22T08:49:07.333760+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_issues.yaml\", \"bytes\": 12299}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 102
}
```

</details>

---


### Tool call

_source line 144 · 2026-05-22T08:51:12.487721+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "report": "# 审稿报告 — turn_residual_gating Round 2\n\n**论文**: \"Why Lightweight Gating Fails to Fix Multi-Turn Attention Degradation: A Mechanistic Analysis\"\n**目标 Venue**: EMNLP 2026 (ARR August cycle)\n**Reviewers**: R1 (方法严谨性+实验设计), R2 (新颖性+完整性+格式)\n**审稿轮次**: Round 1 (fresh re-review)\n**日期**: 2026-05-22\n\n---\n\n## Summary\n\n本文提出 ThreadGate，一种 per-layer content-and-turn-conditioned MLP 门控机制，试图修复多轮对话中对 system prompt goal tokens 的注意力衰减（以 GAR 指标衡量）。核心发现为负面结果：ThreadGate 在 teacher-forced 评估下 GAR 达到 0.50，但自回归生成时崩溃至 0.015–0.025（20–33× gap）。五路消融对比排除了门控机制、turn conditioning、梯度方向冲突等因素后，论文将失败归因于 exposure bias。Inference-time attention steering（β=5）恢复 GAR 至 0.727，scheduled sampling 将 gap 压缩至 1.57×（单 seed）。跨模型验证（Llama-3.1-8B）确认了 27× gap。\n\n## Strengths\n\n**S1** [R1, R2 共识]: 五路消融实验设计系统性强，逐步排除因素的逻辑链清晰（turn conditioning → gating mechanism → gradient conflict → fine-tuning），每对对比有明确的控制变量隔离目标。\n\n**S2** [R1, R2 共识]: Exposure bias 选择性破坏辅助 attention objective（20–33× GAR gap）而非主 NTP 目标的发现具有新颖性，现有 exposure bias 文献聚焦生成质量退化，未涉及辅助分布目标的失败模式。\n\n**S3** [R1, R2 共识]: Inference-time β-steering 提供了建设性的正面证据（GAR 0.064→0.727），将论文从纯负面结果提升为\"什么不行 + 为什么 + 什么可以行\"的完整叙事。\n\n**S4** [R1, R2 共识]: Cross-model 验证（Llama-3.1-8B, 27× gap by median）增加了结论的泛化性。\n\n**S5** [R1]: TRC（Turn-level Residual Coherence）作为正交 hidden-state metric 增强了 selectivity 论点——exposure bias 破坏 attention routing 而非 representation。\n\n**S6** [R2]: 论文的 scope 和 limitations 表述诚实——§8 明确列出未测试方面。ARR guidelines 鼓励负面结果论文发表。\n\n**S7** [R1]: 写作逻辑清晰：观察→干预→失败→诊断→归因→验证。\n\n## Weaknesses\n\n### Must-Fix（Critical，影响接收决定）\n\n**C1** [R1-N1 + R2-W1, 共识 Critical] **统计功效严重不足——五路对比中 4/5 条件为单 seed**\n\n核心 claim \"四个 fine-tuned variants 收敛到 0.75 pp 以内\"（§4.2）是单次观测的点估计，无置信区间或统计检验。单 seed 下 0.75 pp 差异可能在 seed variance 范围内。仅 ThreadGate 有双 seed 验证（seed 42/123）。Scheduled sampling 结果（gap 31×→1.57×）——全文最具操作性的发现——也仅为单 seed，且第二个 seed 使用不同训练协议（resumed vs from-scratch），两个数据点不可比。ARR 标准 R5 要求主要结果需统计显著性评估。\n建议：每个 variant 至少 3 seed，报告 mean±std，做配对检验。Scheduled sampling 优先补充。\n\n**C2** [R1-N2 + R2-N2, 共识 Critical] **\"Causal\" 分析框架过度声称**\n\n论文 Contribution (1) 声称 \"systematic causal diagnostic framework\"，§5 标题和内容反复使用 \"causal\"。实际方法论是结构化消融实验，而非因果推断。PCGrad 因果排除（§5.2 modus tollens 论证）形式合法但前提不完备：(1) 仅排除梯度方向冲突，未排除幅度失衡（NTP 梯度幅度 7.5–14.7× GAR）；(2) PCGrad 仅应用于 gate parameters，LoRA 参数上的梯度冲突未触及；(3) GradNorm、Nash-MTL 均未测试。\"五路 factorial comparison\" 实际是 5 条件消融（真正的 4 因素 factorial 应有 16 条件），无交互效应检验。\n建议：将 \"causal diagnostic framework\" 改为 \"systematic diagnostic/ablation framework\"；限定 PCGrad 排除 scope 为 \"directional gradient conflict on gate parameters\"；或补充 GradNorm 实验。\n\n**C3** [R1-N3 + R2-W2, 共识 Critical] **Exposure bias 归因存在未排除的替代解释**\n\n证据链缺口：(1) β-steering 证明 attention misallocation 可修正，不等于 exposure bias 是其原因——§4.3 末段将 \"exposure-bias-induced\" 嵌入结论本身，存在循环论证；(2) Scheduled sampling 改变整个训练分布（loss landscape、梯度分布、隐式 data augmentation），不仅仅缓解 exposure bias；(3) KV cache 累积方式差异（TF 一次性计算 vs AR 逐 token 追加）未被排除（R2 补充：现代实现中数学等价，解释力可能有限，但应讨论）。\n建议：将 \"the proximal cause\" 降级为 \"a proximal cause consistent with our converging evidence\"；在 Discussion 中列出并讨论替代假说。\n\n**C4** [R2-N1 + R1-W1, 共识 Critical] **GAR 指标缺乏下游任务验证**\n\n全文以 GAR 为核心评估指标，但从未展示 autoregressive GAR 提升带来实际任务性能改善。唯一的下游验证（§6 instruction retention）McNemar p=0.077（不显著），GAR-compliance r=0.200（极弱）。如果 GAR 改善不能转化为指令遵循改善或生成质量提升，论文全部分析的实践意义存疑。负面结果论文的价值取决于\"什么失败了\"是否重要。\n建议：加入 β-steering 前后的任务级评估（constraint satisfaction rate、instruction following accuracy），证明 GAR 恢复确实改善功能性指标。\n\n### Should-Fix（Warning，影响评分）\n\n**W1** [R1-W2, R2 同意] **Table 1 缺少 autoregressive GAR 数据**——论文最关键发现（20–33× gap）只在正文散见描述，未在表格中系统呈现。建议增加 AR 列或新建 Table 2。\n\n**W2** [R1-W5 + R2 部分反驳] **标题 \"Lightweight Gating\" 过度声称**——暗示一类方法但仅测试 ThreadGate。R2 指出 Uniform Gate + LoRA-only 消融部分回应此批评，但 \"Lightweight Gating\" 可包含 MoE-style routing、token-level gating 等未测试方法。建议改为 \"per-layer residual gating\" 或 \"scalar residual gating\"。\n\n**W3** [R1-W6, R2 同意] **Cross-model validation 不完整**——Llama-3.1-8B 仅复现 3/5 条件，缺少 PCGrad 和 Uniform Gate。N=20（vs Qwen N=50），用 median 而非 mean 报告。\n\n**W4** [R2-W4, R1 同意] **写作冗余度高**——\"20–33× gap\"、\"0.015–0.025\"、\"0.064 to 0.727\" 等关键数字在 Abstract、Introduction、Experiments、Analysis、Discussion、Conclusion 中各出现多次。8 页限制下冗余占用可用于更多分析的空间。\n\n**W5** [R2-W5, R1 有保留同意] **Scheduled sampling 结果应从 Discussion 提升**——Gap 31×→1.57× 且无 PPL 损失，是全文最具实践价值的发现，但被放在 Discussion。R1 附加条件：须先补 ≥3 seed 统一协议数据。\n\n**W6** [R2-W6, R1 同意] **Contribution (1) 过度声称泛化性**——\"in principle applicable to other auxiliary objective analyses\" 未经验证。应加入限定语。\n\n**W7** [R2-W3, R1 部分同意] **Li et al. (2024) split-softmax 缺乏实验对比**——最直接的竞争 inference-time 方法，仅定性讨论。R1 认为属 ARR H13（超出 claims scope），定为建议而非硬性要求。\n\n**W8** [R2-N3, R1 反驳降级] **GAR 全称可能与 Dongre 原文不一致**——R2 指出 Dongre et al. (2026) 原文为 \"Goal Accessibility Ratio\"，本文写为 \"Goal Attention Ratio\"。R1 反驳：Eq.1 定义自包含，\"Attention Ratio\" 描述性准确，修改成本极低，不影响方法论/结论。Director 裁定为 Warning。\n\n## Reviewer Consensus\n\n两位 Reviewer 独立收敛的核心问题（增强问题可信度）：\n1. **[AGREE]** 统计功效不足/单 seed（R1 Critical, R2 升为 Critical）\n2. **[AGREE]** PCGrad/\"causal\" 过度声称（R1 + R2 均 Critical）\n3. **[AGREE]** Exposure bias 归因 underdetermination（R1 Critical, R2 Warning→同意 R1）\n4. **[AGREE]** GAR 下游有效性缺失（R2 Critical, R1 Warning→同意 R2）\n5. **[AGREE]** 写作冗余、Contribution 泛化 overclaim、cross-model 不完整\n\n## Reviewer Divergence\n\n1. **GAR 全称 \"Goal Attention Ratio\" vs \"Goal Accessibility Ratio\"**\n   - R2: Critical（事实性错误）\n   - R1: [REBUT] Minor（定义自包含，不影响结论）\n   - Director 裁定：Warning——引用准确性需修正，但不影响方法论\n\n2. **标题 overclaim 程度** (R1-W5)\n   - R1: Warning（\"Lightweight Gating\" 暗示一类方法）\n   - R2: 部分反驳（Uniform Gate + LoRA-only 消融已部分覆盖）\n   - 共识：标题需更精确但非 critical\n\n3. **Split-softmax 对比** (R2-W3)\n   - R2: Should-Fix\n   - R1: 超出 paper scope (ARR H13)\n   - 共识：定为建议\n\n## Questions\n\n1. 是否测试过 GradNorm 以排除梯度幅度失衡？[R1, R2]\n2. GAR 目标 τ=0.5 的选取依据？Base model GAR-ours 仅 0.0418——12× 放大是否过于激进？[R1, R2]\n3. 自回归评估使用何种解码策略？不同策略是否影响 GAR collapse 程度？[R2]\n4. β-steering 恢复 GAR 后生成文本内容质量如何变化？有 case study 或自动评估吗？[R1, R2]\n5. UltraChat 8K 训练集的筛选标准？[R1]\n6. Scheduled sampling 第二个 seed 使用不同协议的原因？[R1, R2]\n\n## Missing References\n\n- **GradNorm** (Chen et al., 2018)：虽在 Related Work 提及但未实验测试，考虑到梯度幅度失衡是核心分析对象，缺少 GradNorm baseline 是实验遗漏。[R1, R2]\n- **Split-softmax** (Li et al., 2024)：最直接的竞争 inference-time 方法，缺乏实验对比。[R2]\n- Related Work 对 multi-turn degradation、residual gating、attention manipulation、multi-task gradient conflict、exposure bias 五个方向均有涉及，无明显文献遗漏。\n\n## External Review (Stanford Agentic Reviewer)\n\n外部审稿：未请求。\n\n## Visual Layout Check（非评分项）\n\n视觉审查已完成（0 critical, 2 warnings, 14 info）。\n\n**Warnings：**\n- **Page 7**：Figure 4（2 panels）+ Figure 5（2 panels）共 4 个子图压缩在同一页，轴标签和 tick marks 字号偏小（≤6pt），接近可读下限。建议分散到两页或增大字号至 ≥8pt。\n- **Pages 8-9**：连续 2 页纯文本无 display item（§5.5 + §6 + §7 + §8）。Discussion 中 scheduled sampling 对比适合用小型汇总表辅助传达。\n\n**页数边界提醒**：§7 Conclusion 起始于 page 9 上部。如 main text（§1–§7）超出 page 8 边界，可能违反 EMNLP 2026 的 8 页正文限制（Limitations 不计入）。\n\n**积极面**：Figure 1 概览图有效传达框架、引用全部正确解析（无 [?]）、booktabs 表格格式规范、颜色方案对色盲友好。\n\n## Overall Assessment\n\n**Overall Score: 3.0 (Findings)**\n**EMNLP 2026 评分标准: 3 = Findings（可被 Findings 接收）**\n**置信度: 4/5**\n\nR1 评分：3.0 (Soundness 3.0, Excitement 3.0, Reproducibility 3.0)\nR2 评分：3.0 (Soundness 3.5, Excitement 3.0, Reproducibility 3.5)\n交叉讨论后双方均维持评分。\n\n**评分理由**：论文作为负面结果有社区价值——系统性排除了 ThreadGate（per-layer scalar gating + GAR auxiliary loss）的多个潜在失败原因，发现了 exposure bias 选择性破坏辅助 attention objective 的现象，并提供了 inference-time steering 和 scheduled sampling 两条建设性路径。\n\n但四个 Critical 问题阻碍主会议接收：(1) 统计功效不足（4/5 条件单 seed），(2) \"causal\" 框架过度声称（仅排除梯度方向冲突），(3) exposure bias 归因存在未排除的替代解释，(4) GAR 指标缺乏下游任务验证。这些问题涉及 soundness 和 claim 可信度，需补充实验或实质性修改。\n\n**修改路径**：如果作者能 (a) 为关键 variants 补充多 seed 验证（尤其 scheduled sampling），(b) 降级或限定 \"causal\" 相关声称，(c) 讨论替代假说并弱化归因，(d) 加入最小化的下游任务验证，则论文有潜力达到 Findings 接收标准。其中 (b)(c) 为写作修改成本低，(a)(d) 需要额外实验。\n\n## Detailed Comments\n\n### §1 Introduction\n- Contribution list 过长（4 项 × 多行），考虑精简。Contribution (1) 中 \"in principle applicable\" 未经验证。\n- Abstract 与 Introduction 重复度过高。\n\n### §3 Method\n- GAR 全称应确认是否与 Dongre et al. (2026) 原文一致。\n- §3.3 λ_GAR = λ_div = 1.0 已报告，但无敏感性分析。\n\n### §4 Experiments\n- Table 1 应增加 AR GAR 列。\n- §4.2 \"0.75 pp spread\" 需方差估计支撑。\n- §4.3 β=3 操作点应讨论 robustness。\n\n### §5 Analysis\n- §5.2 \"gradient conflict is not the cause\" → 应限定为 \"directional gradient conflict on gate parameters is not the cause\"。\n- §5.3 应讨论替代假说（KV cache 差异等）。\n- §5.5 Cross-model 应补充 PCGrad/UG 变体或说明理由。\n\n### §6 Discussion\n- Scheduled sampling 是全文最有价值内容之一，统计支撑最弱。优先补充多 seed。\n- Instruction retention 的 McNemar p=0.077 应标注为 exploratory evidence。\n\n### §7 Conclusion\n- 确认是否超出 page 8 边界。\n\n### §8 Limitations\n- 诚实且全面，是论文优势之一。\n\n### Bib\n- 格式不一致（\"and others\" vs 完整作者列表）。\n- 需检查是否有 orphan 条目。",
  "project": "turn_residual_gating",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "3.0 (Findings)",
  "review_chat_id": "oc_9287ee173cf15d688adcd081f5d861f5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "report": "# 审稿报告 — turn_residual_gating Round 2\n\n**论文**: \"Why Lightweight Gating Fails to Fix Multi-Turn Attention Degradation: A Mechanistic Analysis\"\n**目标 Venue**: EMNLP 2026 (ARR August cycle)\n**Reviewers**: R1 (方法严谨性+实验设计), R2 (新颖性+完整性+格式)\n**审稿轮次**: Round 1 (fresh re-review)\n**日期**: 2026-05-22\n\n---\n\n## Summary\n\n本文提出 ThreadGate，一种 per-layer content-and-turn-conditioned MLP 门控机制，试图修复多轮对话中对 system prompt goal tokens 的注意力衰减（以 GAR 指标衡量）。核心发现为负面结果：ThreadGate 在 teacher-forced 评估下 GAR 达到 0.50，但自回归生成时崩溃至 0.015–0.025（20–33× gap）。五路消融对比排除了门控机制、turn conditioning、梯度方向冲突等因素后，论文将失败归因于 exposure bias。Inference-time attention steering（β=5）恢复 GAR 至 0.727，scheduled sampling 将 gap 压缩至 1.57×（单 seed）。跨模型验证（Llama-3.1-8B）确认了 27× gap。\n\n## Strengths\n\n**S1** [R1, R2 共识]: 五路消融实验设计系统性强，逐步排除因素的逻辑链清晰（turn conditioning → gating mechanism → gradient conflict → fine-tuning），每对对比有明确的控制变量隔离目标。\n\n**S2** [R1, R2 共识]: Exposure bias 选择性破坏辅助 attention objective（20–33× GAR gap）而非主 NTP 目标的发现具有新颖性，现有 exposure bias 文献聚焦生成质量退化，未涉及辅助分布目标的失败模式。\n\n**S3** [R1, R2 共识]: Inference-time β-steering 提供了建设性的正面证据（GAR 0.064→0.727），将论文从纯负面结果提升为\"什么不行 + 为什么 + 什么可以行\"的完整叙事。\n\n**S4** [R1, R2 共识]: Cross-model 验证（Llama-3.1-8B, 27× gap by median）增加了结论的泛化性。\n\n**S5** [R1]: TRC（Turn-level Residual Coherence）作为正交 hidden-state metric 增强了 selectivity 论点——exposure bias 破坏 attention routing 而非 representation。\n\n**S6** [R2]: 论文的 scope 和 limitations 表述诚实——§8 明确列出未测试方面。ARR guidelines 鼓励负面结果论文发表。\n\n**S7** [R1]: 写作逻辑清晰：观察→干预→失败→诊断→归因→验证。\n\n## Weaknesses\n\n### Must-Fix（Critical，影响接收决定）\n\n**C1** [R1-N1 + R2-W1, 共识 Critical] **统计功效严重不足——五路对比中 4/5 条件为单 seed**\n\n核心 claim \"四个 fine-tuned variants 收敛到 0.75 pp 以内\"（§4.2）是单次观测的点估计，无置信区间或统计检验。单 seed 下 0.75 pp 差异可能在 seed variance 范围内。仅 ThreadGate 有双 seed 验证（seed 42/123）。Scheduled sampling 结果（gap 31×→1.57×）——全文最具操作性的发现——也仅为单 seed，且第二个 seed 使用不同训练协议（resumed vs from-scratch），两个数据点不可比。ARR 标准 R5 要求主要结果需统计显著性评估。\n建议：每个 variant 至少 3 seed，报告 mean±std，做配对检验。Scheduled sampling 优先补充。\n\n**C2** [R1-N2 + R2-N2, 共识 Critical] **\"Causal\" 分析框架过度声称**\n\n论文 Contribution (1) 声称 \"systematic causal diagnostic framework\"，§5 标题和内容反复使用 \"causal\"。实际方法论是结构化消融实验，而非因果推断。PCGrad 因果排除（§5.2 modus tollens 论证）形式合法但前提不完备：(1) 仅排除梯度方向冲突，未排除幅度失衡（NTP 梯度幅度 7.5–14.7× GAR）；(2) PCGrad 仅应用于 gate parameters，LoRA 参数上的梯度冲突未触及；(3) GradNorm、Nash-MTL 均未测试。\"五路 factorial comparison\" 实际是 5 条件消融（真正的 4 因素 factorial 应有 16 条件），无交互效应检验。\n建议：将 \"causal diagnostic framework\" 改为 \"systematic diagnostic/ablation framework\"；限定 PCGrad 排除 scope 为 \"directional gradient conflict on gate parameters\"；或补充 GradNorm 实验。\n\n**C3** [R1-N3 + R2-W2, 共识 Critical] **Exposure bias 归因存在未排除的替代解释**\n\n证据链缺口：(1) β-steering 证明 attention misallocation 可修正，不等于 exposure bias 是其原因——§4.3 末段将 \"exposure-bias-induced\" 嵌入结论本身，存在循环论证；(2) Scheduled sampling 改变整个训练分布（loss landscape、梯度分布、隐式 data augmentation），不仅仅缓解 exposure bias；(3) KV cache 累积方式差异（TF 一次性计算 vs AR 逐 token 追加）未被排除（R2 补充：现代实现中数学等价，解释力可能有限，但应讨论）。\n建议：将 \"the proximal cause\" 降级为 \"a proximal cause consistent with our converging evidence\"；在 Discussion 中列出并讨论替代假说。\n\n**C4** [R2-N1 + R1-W1, 共识 Critical] **GAR 指标缺乏下游任务验证**\n\n全文以 GAR 为核心评估指标，但从未展示 autoregressive GAR 提升带来实际任务性能改善。唯一的下游验证（§6 instruction retention）McNemar p=0.077（不显著），GAR-compliance r=0.200（极弱）。如果 GAR 改善不能转化为指令遵循改善或生成质量提升，论文全部分析的实践意义存疑。负面结果论文的价值取决于\"什么失败了\"是否重要。\n建议：加入 β-steering 前后的任务级评估（constraint satisfaction rate、instruction following accuracy），证明 GAR 恢复确实改善功能性指标。\n\n### Should-Fix（Warning，影响评分）\n\n**W1** [R1-W2, R2 同意] **Table 1 缺少 autoregressive GAR 数据**——论文最关键发现（20–33× gap）只在正文散见描述，未在表格中系统呈现。建议增加 AR 列或新建 Table 2。\n\n**W2** [R1-W5 + R2 部分反驳] **标题 \"Lightweight Gating\" 过度声称**——暗示一类方法但仅测试 ThreadGate。R2 指出 Uniform Gate + LoRA-only 消融部分回应此批评，但 \"Lightweight Gating\" 可包含 MoE-style routing、token-level gating 等未测试方法。建议改为 \"per-layer residual gating\" 或 \"scalar residual gating\"。\n\n**W3** [R1-W6, R2 同意] **Cross-model validation 不完整**——Llama-3.1-8B 仅复现 3/5 条件，缺少 PCGrad 和 Uniform Gate。N=20（vs Qwen N=50），用 median 而非 mean 报告。\n\n**W4** [R2-W4, R1 同意] **写作冗余度高**——\"20–33× gap\"、\"0.015–0.025\"、\"0.064 to 0.727\" 等关键数字在 Abstract、Introduction、Experiments、Analysis、Discussion、Conclusion 中各出现多次。8 页限制下冗余占用可用于更多分析的空间。\n\n**W5** [R2-W5, R1 有保留同意] **Scheduled sampling 结果应从 Discussion 提升**——Gap 31×→1.57× 且无 PPL 损失，是全文最具实践价值的发现，但被放在 Discussion。R1 附加条件：须先补 ≥3 seed 统一协议数据。\n\n**W6** [R2-W6, R1 同意] **Contribution (1) 过度声称泛化性**——\"in principle applicable to other auxiliary objective analyses\" 未经验证。应加入限定语。\n\n**W7** [R2-W3, R1 部分同意] **Li et al. (2024) split-softmax 缺乏实验对比**——最直接的竞争 inference-time 方法，仅定性讨论。R1 认为属 ARR H13（超出 claims scope），定为建议而非硬性要求。\n\n**W8** [R2-N3, R1 反驳降级] **GAR 全称可能与 Dongre 原文不一致**——R2 指出 Dongre et al. (2026) 原文为 \"Goal Accessibility Ratio\"，本文写为 \"Goal Attention Ratio\"。R1 反驳：Eq.1 定义自包含，\"Attention Ratio\" 描述性准确，修改成本极低，不影响方法论/结论。Director 裁定为 Warning。\n\n## Reviewer Consensus\n\n两位 Reviewer 独立收敛的核心问题（增强问题可信度）：\n1. **[AGREE]** 统计功效不足/单 seed（R1 Critical, R2 升为 Critical）\n2. **[AGREE]** PCGrad/\"causal\" 过度声称（R1 + R2 均 Critical）\n3. **[AGREE]** Exposure bias 归因 underdetermination（R1 Critical, R2 Warning→同意 R1）\n4. **[AGREE]** GAR 下游有效性缺失（R2 Critical, R1 Warning→同意 R2）\n5. **[AGREE]** 写作冗余、Contribution 泛化 overclaim、cross-model 不完整\n\n## Reviewer Divergence\n\n1. **GAR 全称 \"Goal Attention Ratio\" vs \"Goal Accessibility Ratio\"**\n   - R2: Critical（事实性错误）\n   - R1: [REBUT] Minor（定义自包含，不影响结论）\n   - Director 裁定：Warning——引用准确性需修正，但不影响方法论\n\n2. **标题 overclaim 程度** (R1-W5)\n   - R1: Warning（\"Lightweight Gating\" 暗示一类方法）\n   - R2: 部分反驳（Uniform Gate + LoRA-only 消融已部分覆盖）\n   - 共识：标题需更精确但非 critical\n\n3. **Split-softmax 对比** (R2-W3)\n   - R2: Should-Fix\n   - R1: 超出 paper scope (ARR H13)\n   - 共识：定为建议\n\n## Questions\n\n1. 是否测试过 GradNorm 以排除梯度幅度失衡？[R1, R2]\n2. GAR 目标 τ=0.5 的选取依据？Base model GAR-ours 仅 0.0418——12× 放大是否过于激进？[R1, R2]\n3. 自回归评估使用何种解码策略？不同策略是否影响 GAR collapse 程度？[R2]\n4. β-steering 恢复 GAR 后生成文本内容质量如何变化？有 case study 或自动评估吗？[R1, R2]\n5. UltraChat 8K 训练集的筛选标准？[R1]\n6. Scheduled sampling 第二个 seed 使用不同协议的原因？[R1, R2]\n\n## Missing References\n\n- **GradNorm** (Chen et al., 2018)：虽在 Related Work 提及但未实验测试，考虑到梯度幅度失衡是核心分析对象，缺少 GradNorm baseline 是实验遗漏。[R1, R2]\n- **Split-softmax** (Li et al., 2024)：最直接的竞争 inference-time 方法，缺乏实验对比。[R2]\n- Related Work 对 multi-turn degradation、residual gating、attention manipulation、multi-task gradient conflict、exposure bias 五个方向均有涉及，无明显文献遗漏。\n\n## External Review (Stanford Agentic Reviewer)\n\n外部审稿：未请求。\n\n## Visual Layout Check（非评分项）\n\n视觉审查已完成（0 critical, 2 warnings, 14 info）。\n\n**Warnings：**\n- **Page 7**：Figure 4（2 panels）+ Figure 5（2 panels）共 4 个子图压缩在同一页，轴标签和 tick marks 字号偏小（≤6pt），接近可读下限。建议分散到两页或增大字号至 ≥8pt。\n- **Pages 8-9**：连续 2 页纯文本无 display item（§5.5 + §6 + §7 + §8）。Discussion 中 scheduled sampling 对比适合用小型汇总表辅助传达。\n\n**页数边界提醒**：§7 Conclusion 起始于 page 9 上部。如 main text（§1–§7）超出 page 8 边界，可能违反 EMNLP 2026 的 8 页正文限制（Limitations 不计入）。\n\n**积极面**：Figure 1 概览图有效传达框架、引用全部正确解析（无 [?]）、booktabs 表格格式规范、颜色方案对色盲友好。\n\n## Overall Assessment\n\n**Overall Score: 3.0 (Findings)**\n**EMNLP 2026 评分标准: 3 = Findings（可被 Findings 接收）**\n**置信度: 4/5**\n\nR1 评分：3.0 (Soundness 3.0, Excitement 3.0, Reproducibility 3.0)\nR2 评分：3.0 (Soundness 3.5, Excitement 3.0, Reproducibility 3.5)\n交叉讨论后双方均维持评分。\n\n**评分理由**：论文作为负面结果有社区价值——系统性排除了 ThreadGate（per-layer scalar gating + GAR auxiliary loss）的多个潜在失败原因，发现了 exposure bias 选择性破坏辅助 attention objective 的现象，并提供了 inference-time steering 和 scheduled sampling 两条建设性路径。\n\n但四个 Critical 问题阻碍主会议接收：(1) 统计功效不足（4/5 条件单 seed），(2) \"causal\" 框架过度声称（仅排除梯度方向冲突），(3) exposure bias 归因存在未排除的替代解释，(4) GAR 指标缺乏下游任务验证。这些问题涉及 soundness 和 claim 可信度，需补充实验或实质性修改。\n\n**修改路径**：如果作者能 (a) 为关键 variants 补充多 seed 验证（尤其 scheduled sampling），(b) 降级或限定 \"causal\" 相关声称，(c) 讨论替代假说并弱化归因，(d) 加入最小化的下游任务验证，则论文有潜力达到 Findings 接收标准。其中 (b)(c) 为写作修改成本低，(a)(d) 需要额外实验。\n\n## Detailed Comments\n\n### §1 Introduction\n- Contribution list 过长（4 项 × 多行），考虑精简。Contribution (1) 中 \"in principle applicable\" 未经验证。\n- Abstract 与 Introduction 重复度过高。\n\n### §3 Method\n- GAR 全称应确认是否与 Dongre et al. (2026) 原文一致。\n- §3.3 λ_GAR = λ_div = 1.0 已报告，但无敏感性分析。\n\n### §4 Experiments\n- Table 1 应增加 AR GAR 列。\n- §4.2 \"0.75 pp spread\" 需方差估计支撑。\n- §4.3 β=3 操作点应讨论 robustness。\n\n### §5 Analysis\n- §5.2 \"gradient conflict is not the cause\" → 应限定为 \"directional gradient conflict on gate parameters is not the cause\"。\n- §5.3 应讨论替代假说（KV cache 差异等）。\n- §5.5 Cross-model 应补充 PCGrad/UG 变体或说明理由。\n\n### §6 Discussion\n- Scheduled sampling 是全文最有价值内容之一，统计支撑最弱。优先补充多 seed。\n- Instruction retention 的 McNemar p=0.077 应标注为 exploratory evidence。\n\n### §7 Conclusion\n- 确认是否超出 page 8 边界。\n\n### §8 Limitations\n- 诚实且全面，是论文优势之一。\n\n### Bib\n- 格式不一致（\"and others\" vs 完整作者列表）。\n- 需检查是否有 orphan 条目。",
    "project": "turn_residual_gating",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "3.0 (Findings)",
    "review_chat_id": "oc_9287ee173cf15d688adcd081f5d861f5"
  }
}
```

</details>

---


### Tool result

_source line 145 · 2026-05-22T08:51:16.907795+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_640e53b6afbbd5e34eb7273cd5a707a0:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4420
}
```

</details>

---


### Assistant

_source line 146 · 2026-05-22T08:51:26.875256+00:00_

审稿报告已投递至 Research Director。

**审稿结论：Overall 3.0 (Findings)**

两位 Reviewer 独立评分一致（均 3.0），交叉讨论后维持不变。

**4 个 Critical 问题**：
1. 统计功效不足（4/5 条件单 seed）
2. "Causal" 框架过度声称（仅排除梯度方向冲突）
3. Exposure bias 归因存在未排除替代解释
4. GAR 指标缺乏下游任务验证

**7 个主要优势**：五路消融设计系统性强、exposure bias 选择性破坏辅助目标的新颖发现、inference-time steering 建设性证据、cross-model 验证、TRC 正交验证、limitations 诚实、写作逻辑清晰。

**1 处分歧**：GAR 全称是否为事实性错误（R2: Critical, R1: Minor, Director 裁定 Warning）。

Issue Tracker 已同步更新（Round 1 → Round 2：7 个旧 issue 确认修复，8 个持续存在，4 个新增）。视觉审查结果已纳入报告（2 warnings：page 7 图表密度过高、pages 8-9 纯文本段落偏长）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director"
}
```

</details>

---


## Round 11

## Round 11

2 recorded events


### User

_source line 147 · 2026-05-22T08:51:29.711934+00:00_

[Reviewer 1 审稿结果]:
交叉回应已提交给 Review Director。

核心判断：与 R2 在 5 个问题上达成共识（统计功效、exposure bias 归因、GAR 有效性、causal overclaim、写作冗余），在 1 个问题上反驳（GAR 全称错误不应为 Critical），在 2 个问题上有条件同意（split-softmax 对比属建议非 weakness，scheduled sampling 提升须先补 multi-seed）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 148 · 2026-05-22T08:51:49.692760+00:00_

审稿圆桌已完成全部流程：

- **Round 1 初审**：2 位 Reviewer 独立评审 → 均给出 3.0 (Findings)
- **交叉分享**：逐条 [AGREE]/[REBUT]，4 个核心问题独立收敛
- **收敛判断**：关键问题高度共识，无需 Round 2
- **报告投递**：已提交至 Research Director，Issue Tracker 已同步更新

**Overall Score: 3.0 (Findings)**，4 个 Critical 问题：统计功效不足（单 seed）、"causal" 框架过度声称、exposure bias 归因 underdetermination、GAR 下游验证缺失。8 个 Warning 级问题。视觉审查 2 warnings（page 7 图表密度、pages 8-9 纯文本段）。外部审稿未请求。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director"
}
```

</details>

---


## Round 12

## Round 12

56 recorded events


### User

_source line 149 · 2026-05-22T12:46:10.125219+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: turn_residual_gating
- 论文路径: /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: ARR August 2026
- 截止日期: 2026-08-03
- **引用验证**: ❌ 未启用

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 150 · 2026-05-22T12:46:27.670763+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 151 · 2026-05-22T12:46:27.721745+00:00_

1	---
2	name: review-director-session-start
3	description: Review Director session 启动初始化流程——圆桌多轮审稿协议。Review Director 角色 session 启动时自动使用。
4	priority: 9
5	scope: global
6	tags:
7	- workflow
8	- review
9	- session
10	version: 3
11	roles:
12	- review_director
13	---
14	
15	# Review Director Session 启动流程（圆桌会议模式）
16	
17	## 初始化
18	
19	1. `director_get_project_overview(project)` — 了解研究现状（实验状态、最新报告）
20	2. 读取论文文件状态：检查 `projects/{project}/paper/` 或 `main.tex` 是否存在
21	3. 检查是否有来自 Research Director 的论文提交（`[论文提交]` 消息）
22	4. 向用户简要汇报：
23	   - **投稿目标**：venue 和 deadline
24	   - **论文状态**：当前草稿位置和版本
25	   - **资料完整性**：提交的材料是否齐全
26	   - **下一步**：即将开始的圆桌审稿流程
27	
28	## 评审流程（收到论文提交后执行）
29	
30	### Step 0 — 资料检查 + Venue 调研（必须先做，不可跳过）
31	
32	1. 检查提交资料完整性：论文文件是否存在、是否可读、补充材料是否齐全
33	2. 确认目标投稿 venue（从提交消息中获取）
34	3. 用 `web_search` 搜索该 venue 当前轮次的 CFP（Call for Papers），关键词示例：
35	   - `"&lt;venue name> 2026 call for papers" site:aclweb.org`
36	   - `"&lt;venue name> 2026 submission deadline"`
37	   - `"&lt;venue name> 2026 author guidelines"`
38	4. **验证 deadline 未过期**：今天日期与截止日期对比，若已过期立即通知用户，不继续
39	5. 提取当前版本的格式要求：
40	   - 页数限制（正文 / 附录 / 参考文献）
41	   - 模板（ACL / IEEE / NeurIPS / ICML / ...）
42	   - 匿名规则（double-blind / single-blind / open）
43	   - 附录规则（是否允许、是否参与审稿）
44	   - 引用格式（natbib / biblatex / 特定 .bst）
45	6. 将以上信息作为上下文，随任务一起传递给 Reviewer
46	
47	⚠️ 禁止使用训练知识中的 venue 要求——格式标准每年都会更新，必须实时搜索确认。
48	
49	### Step 0.5 — 决定 Reviewer 编排
50	
51	根据 venue 类型和论文特点，决定：
52	- 需要几个 Reviewer（1-5 人）
53	- 每个 Reviewer 的审查侧重
54	
55	参考：
56	- **顶会长文**（NeurIPS/ICML/ACL）：3 人（方法/实验 + novelty/related work + 格式/ethics）
57	- **一般会议**（EMNLP/NAACL）：2 人（方法严谨性 + 新颖性/完整性）
58	- **Workshop / 短文**：1 人（全面审查）
59	
60	向 Group C（即项目配置中的 `feishu.review_chat_id` 审稿群）汇报编排决定。
61	
62	### Step 0.6 — 外部审稿线（与 Step 1 并行）
63	
64	检查项目配置中 `external_review.paperreview_ai.enabled` 是否为 `true`：
65	- 如果启用：调用 `request_external_review(project, paper_pdf_path, venue)` 向用户群发送协助提交卡片
66	- 这一步与 Step 1（内部 Reviewer 分配）**并行执行**，不阻塞内部审稿流程
67	- 外部结果到达后（用户在群里粘贴），纳入 Step 4 最终报告
68	- 如果到 Ste
…[truncated 3286 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 152 · 2026-05-22T12:46:37.562102+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,dispatch_visual_check,request_external_review,get_external_review_status,director_post_to_reviewer,submit_review_report_to_research_director,update_review_issues,get_visual_check_status,WebSearch,WebFetch",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_get_project_overview,dispatch_visual_check,request_external_review,get_external_review_status,director_post_to_reviewer,submit_review_report_to_research_director,update_review_issues,get_visual_check_status,WebSearch,WebFetch",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 153 · 2026-05-22T12:46:37.614602+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "ToolSearch",
  "elapsed_ms": 52
}
```

</details>

---


### Tool call

_source line 154 · 2026-05-22T12:46:49.912593+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,dispatch_visual_check,request_external_review,get_external_review_status,director_post_to_reviewer,submit_review_report_to_research_director,update_review_issues,get_visual_check_status,read_project_file,read_local_file",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_get_project_overview,dispatch_visual_check,request_external_review,get_external_review_status,director_post_to_reviewer,submit_review_report_to_research_director,update_review_issues,get_visual_check_status,read_project_file,read_local_file",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 155 · 2026-05-22T12:46:49.963229+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 156 · 2026-05-22T12:46:55.737584+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "turn_residual_gating"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "turn_residual_gating"
  }
}
```

</details>

---


### Tool result

_source line 157 · 2026-05-22T12:46:57.149033+00:00_

{"result":"# 项目 turn_residual_gating 概况\n\n## 实验状态 (38 个)\n\n- **phase2_tg_s42_v7**: DONE (success) — \n- **phase2_tg_s42_v9_pcgrad**: DONE (success) — \n- **phase2_lora_only_s42**: DONE (success) — \n- **phase2_ug_s42**: DONE (success) — \n- **phase2_tg_s42_v8_schedsampling**: DONE (failed) — \n- **analysis_attention_heatmap**: DONE (success) — \n- **analysis_gradient_conflict**: DONE (success) — \n- **phase2_4way_eval_heldout**: DONE (success) — \n- **phase2_4way_eval**: DONE (negative) — \n- **phase2_tg_s42_v5**: DONE (negative) — \n- **phase2_tg_s42_v4**: DONE (failed) — \n- **phase2_tg_s42_v3b**: DONE (success) — \n- **phase2_tg_s42_v3**: DONE (negative) — \n- **phase2_tg_s42_v2**: DONE (killed) — \n- **phase1_gar_diag**: DONE (success) — \n\n## 最新报告\n# Handover — 2026-05-22\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\n|--------|------|------|---------|-----|\n| d048_ss_s42 | Scheduled sampling (ratio=0.3) with ThreadGate reduces the ~30× TF-AR GAR gap by exposing the model to its own generated text during training. Multi-seed run (s42) under D048 unified protocol to establish mean±std for statistical testing. SS is the strongest mitigation candidate (prior single-seed showed gap 31×→1.57×). | — | — | — |\n\n## 待处理\n- llama_tg_training（准备中）\n\n## 近期结论\n- **eval_llama_ar_n20** (success): N=20 AR eval stabilizes Llama 3-way (Base/TG/LoRA-only) autoregressive GAR estimates. N=5 suffered from outlier influence (3/5 conv had GAR>0.4 outlier turns); N=20 provides robust mean±std. ← 基于 eval_llama_lora_only_s42\n- **eval_llama_lora_only_s42** (success): LoRA-only ablation (no gate) on Llama-3.1-8B: if TG's GAR improvement comes from the gate, LoRA-only should show minimal GAR recovery vs base. ← 基于 llama_lora_only_s42\n- **llama_lora_only_s42** (success): Llama-3.1-8B LoRA-only baseline (gate=none, 无 gating 机制): 与 Llama TG s42 对比，验证 gating 对 Llama 的增量贡献。如果 LoRA-only GAR ≈ TG GAR → gating 零增量与 Qwen 结论一致（C5 跨模型）。 ← 基于 llama_tg_s42\n
…[truncated 286 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 1411
}
```

</details>

---


### Tool call

_source line 158 · 2026-05-22T12:46:57.651626+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/main.tex",
  "limit": "80"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/main.tex",
    "limit": "80"
  }
}
```

</details>

---


### Tool result

_source line 159 · 2026-05-22T12:46:58.605913+00:00_

1	\documentclass[11pt]{article}
2	\usepackage[review]{acl}
3	\usepackage{times}
4	\usepackage{latexsym}
5	\usepackage[T1]{fontenc}
6	\usepackage[utf8]{inputenc}
7	\usepackage{microtype}
8	\usepackage{inconsolata}
9	\usepackage{graphicx}
10	\usepackage{amsmath}
11	\usepackage{amssymb}
12	\usepackage{booktabs}
13	\usepackage{multirow}
14	\usepackage{xcolor}
15	\usepackage{url}
16	\usepackage{subcaption}
17	
18	\graphicspath{{../figures/paper/}}
19	
20	\title{Why Per-Layer Residual Gating Fails to Fix Multi-Turn Attention Degradation:\\A Mechanistic Analysis}
21	
22	\author{Anonymous}
23	
24	\begin{document}
25	\maketitle
26	
27	\input{sections/abstract}
28	\input{sections/introduction}
29	\input{sections/related_work}
30	\input{sections/method}
31	\input{sections/experiments}
32	\input{sections/analysis}
33	\input{sections/discussion}
34	\input{sections/conclusion}
35	\input{sections/limitations}
36	
37	\bibliographystyle{acl_natbib}
38	\bibliography{references}
39	
40	\appendix
41	\input{sections/appendix}
42	
43	\end{document}
44	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "Read",
  "elapsed_ms": 954
}
```

</details>

---


### Tool call

_source line 160 · 2026-05-22T12:46:58.656543+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 ACL Rolling Review call for papers submission guidelines author instructions"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 ACL Rolling Review call for papers submission guidelines author instructions"
  }
}
```

</details>

---


### Tool call

_source line 161 · 2026-05-22T12:46:58.807559+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "turn_residual_gating",
  "file": "artifacts/review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "turn_residual_gating",
    "file": "artifacts/review_issues.yaml"
  }
}
```

</details>

---


### Tool result

_source line 162 · 2026-05-22T12:47:08.557932+00:00_

Web search results for query: "EMNLP 2026 ACL Rolling Review call for papers submission guidelines author instructions"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"Submission Guide","url":"https://nlp4climate.github.io/submissionguide/"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"},{"title":"First Call for Papers – EACL 2026 Student Research Workshop (SRW) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/first-call-papers-eacl-2026-student-research-workshop-srw"},{"title":"EACL 2026: First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eacl-2026-first-call-papers"},{"title":"EACL/ACL 2026 Joint Call for Workshops | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eaclacl-2026-joint-call-workshops"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"}]

I found comprehensive information about EMNLP 2026 and ACL Rolling Review (ARR) submission guidelines. Here are the key details:

## EMNLP 2026 Overview

EMNLP 2026 will use ACL Rolling Review (ARR) as a reviewing system, but final decisions will be made by the conference.

## Submission Process

Authors will follow a two-step process: submit articles to ARR, where submissions receive reviews and meta-reviews from ARR reviewers and action editors; then commit their reviewed a
…[truncated 1054 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "WebSearch",
  "elapsed_ms": 9901
}
```

</details>

---


### Tool result

_source line 163 · 2026-05-22T12:47:08.609593+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"file must be one of ['ARCHITECTURE.md', 'DATA.md', 'EVALUATION.md', 'MODELS.md', 'ROADMAP.md', 'constraints.yaml', 'decisions.yaml', 'ideas.md', 'literature_map.yaml', 'memory.md', 'mistakes.yaml', 'paper_checklist.yaml', 'paper_framing.md', 'paper_provenance.yaml', 'report.md', 'writing_plan.yaml'], got 'artifacts/review_issues.yaml'\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 9802
}
```

</details>

---


### Tool call

_source line 164 · 2026-05-22T12:47:17.466334+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://2026.emnlp.org/calls/main_conference_papers/",
  "prompt": "Extract the complete submission guidelines: page limits (long/short paper), template requirements, anonymity rules, appendix rules, citation format, important dates (especially ARR submission deadlines for EMNLP 2026 commitment), and any other author requirements."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://2026.emnlp.org/calls/main_conference_papers/",
    "prompt": "Extract the complete submission guidelines: page limits (long/short paper), template requirements, anonymity rules, appendix rules, citation format, important dates (especially ARR submission deadlines for EMNLP 2026 commitment), and any other author requirements."
  }
}
```

</details>

---


### Tool call

_source line 165 · 2026-05-22T12:47:18.972682+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "http://aclrollingreview.org/cfp",
  "prompt": "Extract the complete submission guidelines for ACL Rolling Review: page limits for long and short papers, formatting requirements, anonymity rules, supplementary material rules, responsible NLP checklist requirements, and submission deadlines for 2026."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "WebFetch",
  "tool_args": {
    "url": "http://aclrollingreview.org/cfp",
    "prompt": "Extract the complete submission guidelines for ACL Rolling Review: page limits for long and short papers, formatting requirements, anonymity rules, supplementary material rules, responsible NLP checklist requirements, and submission deadlines for 2026."
  }
}
```

</details>

---


### Tool call

_source line 166 · 2026-05-22T12:47:19.926444+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "http://aclrollingreview.org/dates",
  "prompt": "Extract the ARR submission deadlines for 2026, especially the August 2026 cycle deadlines and EMNLP 2026 commitment deadline."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "WebFetch",
  "tool_args": {
    "url": "http://aclrollingreview.org/dates",
    "prompt": "Extract the ARR submission deadlines for 2026, especially the August 2026 cycle deadlines and EMNLP 2026 commitment deadline."
  }
}
```

</details>

---


### Tool call

_source line 167 · 2026-05-22T12:47:21.784883+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_issues.yaml 2>/dev/null || echo \"FILE_NOT_FOUND\"",
  "description": "Read review issues tracker"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_issues.yaml 2>/dev/null || echo \"FILE_NOT_FOUND\"",
    "description": "Read review issues tracker"
  }
}
```

</details>

---


### Tool result

_source line 168 · 2026-05-22T12:47:21.988225+00:00_

# Review Issues Tracker — turn_residual_gating
# Round 1 (2026-05-19, dream_20260519T145320)
# Round 2 (2026-05-22, fresh re-review of revised paper)

# ============================================================
# Issues from Round 1 — status updates based on Round 2 + D048
# ============================================================

- id: "R1-N1"
  summary: "所有引用渲染为 '?'——bibliography 编译失败"
  category: format
  severity: info
  status: resolved
  first_raised_round: 1
  last_seen_round: 1
  mentions:
    - round: 1
      reviewers: [1, 2]
      note: "Dream paper artifact。"
    - round: 2
      reviewers: []
      note: "视觉审查确认无 [?] 未解析引用。已修复。"
  action_items:
    - round: 1
      action: "Paper Agent 确保 bibtex 编译正确"
      assigned_to: paper_agent
      status: done
  resolution: "Round 2 视觉审查确认已修复。"
  resolution_round: 2

- id: "R1-N2"
  summary: "单种子支撑结论——统计功效不足"
  category: experiment
  severity: critical
  status: in_progress
  first_raised_round: 1
  last_seen_round: 2
  mentions:
    - round: 1
      reviewers: [1, 2]
      note: "Bootstrap CI 仅覆盖 eval variance，不覆盖 training variance。"
    - round: 2
      reviewers: [1, 2]
      note: "ThreadGate 已补 seed=123，但其余 4/5 条件仍为单 seed。SS 仅 1 seed 且第二 seed 协议不同不可比。两位 Reviewer 独立列为 Critical。"
  action_items:
    - round: 1
      action: "plan_019: seed=123 extra training"
      assigned_to: agent
      status: done
    - round: 2
      action: "D048: 5 条件 × 3 seeds from-scratch (Base/TG/LO/UG/SS)，SS 最高优先级。~45h GPU。"
      assigned_to: agent
      status: in_progress
  resolution: ""
  resolution_round: null

- id: "R1-N3"
  summary: "评估样本量过小"
  category: experiment
  severity: info
  status: resolved
  first_raised_round: 1
  last_seen_round: 1
  mentions:
    - round: 1
      reviewers: [1]
      note: "Cohen's d≈0.22 在 n=50 下 power 不足。"
    - round: 2
      reviewers: []
      note: "Round 2 使用 N=50 held-out + N=50 steering + N=20 Llama。未再被提出。"
  action_items: []
  resolution: "N=50 评估已在论文中体现。"
  resolution_round
…[truncated 12293 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "Bash",
  "elapsed_ms": 203
}
```

</details>

---


### Tool result

_source line 169 · 2026-05-22T12:47:23.395639+00:00_

# EMNLP 2026 Submission Guidelines

## Page Limits
- **Long Papers:** 8 pages (9 pages in final camera-ready version)
- **Short Papers:** 4 pages (5 pages in final camera-ready version)

## Key Deadlines
- **ARR Submission:** May 25, 2026
- **Reviewer Registration:** May 27, 2026
- **EMNLP Commitment:** August 2, 2026
- **Acceptance Notification:** August 20, 2026
- **Camera-Ready Due:** September 20, 2026
- **Conference Dates:** October 24-29, 2026

*Note: All deadlines are 11:59 PM UTC-12:00 ("anywhere on Earth")*

## Anonymity Rules
The review process maintains "double-blind" standards. The document states: "Reviewers will not see authors, nor will authors see reviewers and reviews on ARR will not be made publicly visible." However, authors may opt to make anonymized submissions publicly visible.

## Authorship Requirements
Authors cannot modify the author list during commitment (no additions/deletions allowed), though reordering authors is permitted.

## Submission Process
Papers must be submitted through ACL Rolling Review (ARR) first, then committed to EMNLP 2026 via Open Review platform.

## Additional Requirements
Authors must comply with:
- ARR submission standards
- Two-way anonymized review instructions
- ACL Publication Ethics Policy
- Responsible NLP research checklist
- Paper integrity policies (including restrictions on hallucinated citations and AI-generated content)
- Mandatory reviewing workload for all submitting authors

## Other Details
- Supplementary materials permitted
- AI writing assistance allowed
- All papers require presentation at conference for proceedings inclusion
- Both in-person and virtual presentation options available

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "WebFetch",
  "elapsed_ms": 5929
}
```

</details>

---


### Tool result

_source line 170 · 2026-05-22T12:47:24.606306+00:00_

# ACL Rolling Review Submission Guidelines Summary

## Page Limits

**Long Papers:** Up to 8 pages of content, plus unlimited space for required limitations section and optional ethical considerations section, plus unlimited reference pages.

**Short Papers:** Up to 4 pages of content, plus unlimited space for required limitations section and optional ethical considerations section, plus unlimited reference pages.

Papers exceeding length requirements or lacking a limitations section face desk rejection.

## Formatting Requirements

Submissions must follow the "official ACL style template" and conform to "*ACL" conference formatting guidelines regarding paper size, margins, and font size. The template is available on GitHub (acl-org/acl-style-files). Non-compliant submissions are rejected without review. Appendices must use double-column format with limited exceptions.

## Anonymity Rules

Papers must exclude author names, affiliations, and self-identifying references. Instead of "We previously showed," use "Smith previously showed." Supplementary materials require anonymization, and cloud storage services like Dropbox that track downloads are prohibited. Violations result in desk rejection.

## Supplementary Materials

Optional appendices, software, and data are encouraged for reproducibility. Appendices follow references and don't count toward page limits. Software/data should be submitted as single compressed archives. However, reviewers aren't required to review appendices—critical technical content belongs in the main paper.

## Responsible NLP Checklist

Authors must complete this checklist during submission. "Incorrect, incomplete or misleading information in the checklist can result in desk rejection." Checklist responses inform the review process.

## 2026 Submission Deadlines

The document does not specify 2026 deadline dates. It references May 2025 and other cycles but directs readers to check the "Dates & Venues" page for current deadline information.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "WebFetch",
  "elapsed_ms": 5633
}
```

</details>

---


### Tool result

_source line 171 · 2026-05-22T12:47:31.642196+00:00_

# ARR 2026 Submission Deadlines

Based on the ARR schedule, here are the key 2026 deadlines:

**August 2026 Cycle:**
- Submission deadline: August 3, 2026
- The page notes that "Reviews due" and other subsequent dates are "TBA" for this cycle

**EMNLP 2026 Commitment:**
- Final ARR submission deadline: May 25, 2026
- Commitment date to EMNLP 2026: August 2, 2026

The table indicates that August 2026 cycle details beyond the submission date have not yet been finalized, while the May 2026 cycle (with its August 2 commitment window) represents the final opportunity to submit to EMNLP 2026.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "WebFetch",
  "elapsed_ms": 11715
}
```

</details>

---


### Tool call

_source line 172 · 2026-05-22T12:47:43.091604+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 173 · 2026-05-22T12:47:43.443290+00:00_

1	\begin{abstract}
2	Multi-turn dialogue with Large Language Models (LLMs) suffers from progressive attention decay toward system prompt goal tokens. On Qwen-2.5-7B-Instruct, the Goal Attention Ratio (GAR) declines by 70.8\% between early and mid-conversation turns, yet linear probes recover goal content from the residual stream with AUC\,=\,0.98. We introduce ThreadGate, a per-layer content-and-turn-conditioned MLP gate ($x_{l+1} = x_l + g_l \cdot f_l(x_l)$) trained jointly with next-token prediction (NTP) and an auxiliary GAR loss. A five-way comparison reveals that training succeeds (teacher-forced GAR\,=\,0.50) but autoregressive GAR drops to 0.015--0.025, a 20--33$\times$ gap; gating contributes zero measurable benefit and a PCGrad-based exclusion experiment rules out gradient conflict. The failure traces to exposure bias: attention patterns optimized under teacher-forced prefixes do not transfer to model-generated text. Inference-time steering ($\beta$\,=\,5) recovers GAR from 0.064 to 0.727, providing constructive evidence that attention misallocation---not representation degradation---is a proximal cause consistent with our evidence. Scheduled sampling compresses the gap to 1.57$\times$ with no PPL cost (single seed), and cross-model evaluation on Llama-3.1-8B confirms the gap (27$\times$ by median). These findings characterize how exposure bias selectively destroys auxiliary objective generalization under the tested conditions (Qwen-2.5-7B and Llama-3.1-8B, UltraChat, GAR-family losses).
3	\end{abstract}
4	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "Read",
  "elapsed_ms": 351
}
```

</details>

---


### Tool call

_source line 174 · 2026-05-22T12:47:43.443731+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 175 · 2026-05-22T12:47:43.945819+00:00_

1	\section{Introduction}\label{sec:introduction}
2	
3	Multi-turn dialogue is the dominant mode of interaction with large language models (LLMs), and system prompts that specify task goals form the foundation of instruction following. As conversations grow longer, however, models progressively lose track of these goal specifications. \citet{dongre2026attention} quantified this degradation across 12 models: the Goal Attention Ratio (GAR), which measures how much attention the model allocates to goal tokens in the system prompt, declines by 27--48\% between early and mid-conversation turns. We replicate and extend this finding on Qwen-2.5-7B-Instruct, observing a 70.8\% relative decline in GAR from 0.0418 at turn~1 to 0.0122 at mid-conversation. We attribute the steeper decline partly to our use of last-token GAR, which captures summary-position attention more sensitively than the all-token average of \citet{dongre2026attention}, and partly to Qwen-2.5-7B's stronger instruction-following fidelity in early turns. This attention decay represents a systematic failure of multi-turn models to maintain task coherence, and it grows worse with each additional turn.
4	
5	A striking aspect of this degradation is what it does \emph{not} affect. \citet{dongre2026attention} showed that goal-relevant information persists in the residual stream throughout the conversation: linear discriminant analysis probes recover goal content with AUC\,=\,0.98 even at late turns where attention to goal tokens has collapsed. The information is present in the hidden states, but the attention mechanism fails to route it toward the output computation. This dissociation between information availability and information utilization suggests a natural intervention: if the residual stream already carries goal information, a learnable gate on the residual pathway could amplify or attenuate layer contributions to recover goal attention. This reasoning motivates ThreadGate, which modulates each residual updat
…[truncated 4569 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 176 · 2026-05-22T12:47:43.946287+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 177 · 2026-05-22T12:47:44.399793+00:00_

1	\section{Method}\label{sec:method}
2	
3	\subsection{Preliminaries}\label{sec:background}
4	
5	\paragraph{Goal Attention Ratio.}
6	We denote the task specification tokens in the system prompt as \emph{goal tokens} $\mathcal{G}$. \citet{dongre2026attention} defined the Goal Attention Ratio (GAR) for a model with $L$ layers and $H$ heads at turn $\tau$ as
7	\begin{equation}\label{eq:gar}
8	  \text{GAR}(\tau) = \frac{1}{L \cdot H \cdot |\mathcal{R}_\tau|} \sum_{\ell=1}^{L} \sum_{h=1}^{H} \sum_{i \in \mathcal{R}_\tau} \sum_{j \in \mathcal{G}} A_{i,j}^{(\ell,h)},
9	\end{equation}
10	where $\mathcal{R}_\tau$ is the set of response tokens at turn $\tau$ and $A_{i,j}^{(\ell,h)}$ is the attention weight from token $i$ to token $j$ at layer $\ell$, head $h$.
11	
12	\paragraph{Two GAR variants.}
13	\textbf{GAR-Dongre} is the original definition (Eq.~\ref{eq:gar}), averaging over all response tokens. \textbf{GAR-ours} restricts the measurement to the \emph{last token} of each assistant turn:
14	\begin{equation}\label{eq:gar-ours}
15	  \text{GAR\text{-}ours}(\tau) = \frac{1}{L \cdot H} \sum_{\ell=1}^{L} \sum_{h=1}^{H} \sum_{j \in \mathcal{G}} A_{t_\tau,\, j}^{(\ell,h)},
16	\end{equation}
17	where $t_\tau$ is the last token index at turn $\tau$. Attention at this position reflects the information drawn upon for continuation; we use GAR-ours as the optimization target for $\mathcal{L}_\text{GAR}$ (\S\ref{sec:loss}).
18	
19	\subsection{ThreadGate Architecture}
20	
21	Inspired by the residual scaling idea of ReZero \citep{bachlechner2021rezero}, ThreadGate modulates the residual stream with a content-and-turn-conditioned gate at each transformer layer. The gated residual update at layer $l$ is
22	\begin{equation}
23	  x_{l+1} = x_l + g_l \cdot f_l(x_l),
24	\end{equation}
25	where $f_l$ denotes the sublayer computation (self-attention or FFN). The gate $g_l$ is produced by a two-layer MLP:
26	\begin{equation}\label{eq:gate}
27	  g_l = \sigma\!\bigl(W_2\,\text{ReLU}(W_1\,[\text{proj}
…[truncated 1960 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "Read",
  "elapsed_ms": 453
}
```

</details>

---


### Tool call

_source line 178 · 2026-05-22T12:47:44.400158+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 179 · 2026-05-22T12:47:44.862711+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Setup}
5	
6	We fine-tune Qwen-2.5-7B-Instruct on 8K multi-turn conversations from the UltraChat training split, a dataset of naturalistic dialogues across diverse topics. LoRA adapters (rank 16, $\alpha$=32) are applied to query and value projection layers (\texttt{q\_proj}, \texttt{v\_proj}). The combined loss $\mathcal{L} = \mathcal{L}_\text{NTP} + \lambda_\text{GAR}\mathcal{L}_\text{GAR} + \lambda_\text{div}\mathcal{L}_\text{div}$ uses $\lambda_\text{GAR} = \lambda_\text{div} = 1.0$ with MSE target $\tau = 0.5$ (\S\ref{sec:loss}). We train for 3 epochs with AdamW (lr $= 2 \times 10^{-4}$, batch size 1, gradient accumulation 8, seed 42; ThreadGate additionally with seed 123); each variant requires approximately 6 hours on a single NVIDIA RTX PRO 6000 Blackwell Server Edition GPU (102\,GB). Full hyperparameters are provided in Appendix~\ref{sec:appendix-hyper}.
7	
8	We evaluate five configurations that form a controlled comparison isolating four factors. \textbf{ThreadGate}: full system with 28 gate networks (Eq.~\ref{eq:gate}) and three-term loss. \textbf{+PCGrad}: ThreadGate with PCGrad \citep{yu2020pcgrad} projecting conflicting gradients (isolates gradient conflict). \textbf{Uniform Gate}: identical gate architecture with turn embedding replaced by a learned constant vector (content-conditioned but turn-unaware; isolates the contribution of turn conditioning). \textbf{LoRA-only}: gates fixed at 1.0, trained with $\mathcal{L}_\text{NTP} + \mathcal{L}_\text{GAR}$ only (isolates gating mechanism). \textbf{Base}: pretrained model (isolates fine-tuning). All fine-tuned variants share training data, LoRA configuration, optimizer, and seed. We evaluate under \emph{IID} (same-distribution UltraChat text) and \emph{held-out} (50 non-overlapping conversations) teacher-forced protocols, reporting GAR-ours (last-token attention to goals, \S\ref{sec:background}), GAR-Dongre \citep{dongre2026attention} (all-t
…[truncated 6470 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "Read",
  "elapsed_ms": 462
}
```

</details>

---


### Tool call

_source line 180 · 2026-05-22T12:47:44.955007+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/analysis.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/analysis.tex"
  }
}
```

</details>

---


### Tool result

_source line 181 · 2026-05-22T12:47:45.841618+00:00_

1	\section{Analysis}\label{sec:analysis}
2	
3	The five-way comparison in \S\ref{sec:experiments} established that gating produces no measurable benefit over LoRA-only fine-tuning. This section traces the failure through a three-step diagnostic chain: we first show that gates learn behavior opposite to the design intent (\S\ref{subsec:gate-conditioning}), then rule out gradient conflict as the explanation through an exclusion experiment (\S\ref{subsec:pcgrad}), and finally identify distribution shift as the root cause (\S\ref{subsec:dist-shift}). \S\ref{subsec:mechanism-specificity} confirms this selectivity with an orthogonal hidden-state metric, and \S\ref{subsec:cross-model} confirms the failure generalizes across architecturally distinct LLMs.
4	
5	\subsection{Gate Turn Conditioning}\label{subsec:gate-conditioning}
6	
7	The design intent of ThreadGate is to modulate the residual stream more aggressively at late conversation turns, where GAR naturally decays (\S\ref{sec:background}). We test whether the learned gates achieve this by comparing gate values at turn~1 (early) and turn~21 (late) across all 28 layers of the trained model.
8	
9	The gates do the opposite. In 27 of 28 layers, the gate value at turn~1 is lower than at turn~21 (Wilcoxon signed-rank test: $p = 3.73 \times 10^{-8}$, effect size $r = 0.975$). At layer~23, the gate is 0.769 at turn~1 and 0.979 at turn~21; at layer~14, it is 0.747 at turn~1 and 0.928 at turn~21. The pattern is consistent: gates suppress the residual stream more at early turns (where GAR is already high) and become nearly passive at late turns (where intervention is most needed). This inversion has a straightforward explanation. NTP loss pressure is highest at late turns, where the model must predict tokens conditioned on a long context. The NTP gradient pushes gates toward 1.0 to preserve the full sublayer computation, and this pressure is strongest precisely where GAR-based attenuation would be most useful.
10	
11	The resulting 
…[truncated 8200 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "Read",
  "elapsed_ms": 886
}
```

</details>

---


### Tool call

_source line 182 · 2026-05-22T12:47:45.841988+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 183 · 2026-05-22T12:47:46.319611+00:00_

1	\section{Discussion}\label{sec:discussion}
2	
3	The failure traces to an incompatibility between teacher-forcing and GAR-family auxiliary losses, not to the gating architecture. NTP gradient pressure (7.5--14.7$\times$ the GAR magnitude) pushes gates toward identity (2--7\% attenuation), while inference-time steering ($\beta$\,=\,5) recovers GAR from 0.064 to 0.727, providing constructive evidence that attention misallocation is a proximal cause (\S\ref{subsec:steering}). Alternative hypotheses remain open: progressive attention drift unrelated to exposure bias, KV cache accumulation effects at long context lengths, or implicit label smoothing from the auxiliary loss could each contribute to the observed gap. Our evidence is consistent with exposure bias as the dominant factor, but does not exclude these alternatives. Split-softmax \citep{li2024measuring} offers a complementary inference-time approach that restructures attention computation rather than applying additive bias; unlike $\beta$-steering, it addresses the training-inference mismatch at the architectural level but cannot resolve exposure bias in auxiliary losses that require retraining.
4	
5	\paragraph{Scheduled sampling as training-time mitigation.} A preliminary experiment (single seed) applies scheduled sampling \citep{bengio2015scheduled}, linearly mixing teacher-forced and model-generated contexts. Autoregressive GAR-ours increases from 0.016 to 0.318 (20$\times$), compressing the ${\sim}$31$\times$ gap to 1.57$\times$ with negligible PPL change (1.38 vs.\ 1.36), consistent with exposure bias as a primary driver of the gap. GAR-Dongre also rises (0.019$\to$0.353), suggesting indirect improvement of all-token goal attention. The two paths are complementary: $\beta$\,=\,5 achieves the strongest GAR recovery but incurs 24\% PPL cost (1.43\,$\to$\,1.77); $\beta$\,=\,3 offers a more balanced tradeoff (PPL +9\%). Scheduled sampling incurs no fluency cost but requires retraining. A second seed trained fro
…[truncated 1090 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "Read",
  "elapsed_ms": 477
}
```

</details>

---


### Tool call

_source line 184 · 2026-05-22T12:47:46.335769+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 185 · 2026-05-22T12:47:46.336163+00:00_

1	\section{Conclusion}\label{sec:conclusion}
2	
3	ThreadGate modulates the residual stream with per-layer gated MLP networks and an auxiliary GAR loss. Training succeeds (TF GAR\,=\,0.50), but autoregressive GAR collapses by more than an order of magnitude (exposure bias), confirmed on Llama-3.1-8B (27$\times$ by median). Inference-time steering ($\beta$\,=\,5, GAR 0.727) and scheduled sampling (gap ${\sim}$31$\times$$\to$1.57$\times$, no PPL cost, single seed) both point to attention misallocation---not representation degradation---as a proximal cause consistent with our evidence.
4	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 186 · 2026-05-22T12:47:46.788084+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 187 · 2026-05-22T12:47:46.888939+00:00_

1	\section{Limitations}\label{sec:limitations}
2	
3	The five-way comparison uses seed\,=\,42; ThreadGate is additionally validated with seed\,=\,123 (TF/AR GAR-ours within $\pm$0.001, gap 30.5--32.1$\times$). The remaining three variants use a single seed; cross-variant convergence provides indirect robustness evidence but does not substitute for multi-seed validation.
4	
5	We test only one type of auxiliary attention loss (GAR with MSE target $\tau = 0.5$). Other attention steering objectives, such as head-specific or layer-specific attention losses, may exhibit different sensitivity to exposure bias. Our negative result applies to the GAR family; it does not rule out all auxiliary attention interventions.
6	
7	Training uses 8K conversations from UltraChat. Larger-scale training could alter gate dynamics, particularly if the model encounters sufficient distributional diversity to reduce the training-inference mismatch.
8	
9	All experiments use two model families (Qwen-2.5-7B and Llama-3.1-8B); while cross-model evaluation confirms the exposure bias gap, $N$\,=\,2 does not establish universality. The Llama evaluation includes ThreadGate and LoRA-only; the full five-way ablation (Uniform Gate, +PCGrad) has not been replicated, and all experiments use a single dataset (UltraChat). The instruction retention analysis is exploratory: a single model, 18 system-prompt constraint types, and a single $\beta$ value without grid search.
10	
11	The PCGrad exclusion experiment addresses gradient direction conflict only. Magnitude imbalance (GradNorm; \citealp{chen2018gradnorm}) and Nash equilibrium approaches (Nash-MTL; \citealp{navon2022nash}) remain untested and could reveal additional failure modes or interaction effects.
12	
13	All four fine-tuned variants share the same GAR auxiliary loss. This design isolates the gating mechanism but does not test whether gating could be effective without an auxiliary attention loss or under a different training objective.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 188 · 2026-05-22T12:47:47.290807+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 189 · 2026-05-22T12:47:47.742875+00:00_

1	\section{Related Work}\label{sec:related}
2	
3	\paragraph{Multi-turn attention degradation.}
4	Recent work has established that LLMs systematically degrade across conversation turns. \citet{laban2025lost} showed that model performance drops on tasks placed in later turns, even when the tasks are identical to earlier ones. \citet{liu2026intent} traced a related failure to intent mismatch, where models progressively shift from the user's original intent as dialogue extends. MT-Bench-101 \citep{bai2024mtbench101} provides fine-grained multi-turn evaluation across 1388 turn-level instances, revealing that capability varies substantially across task categories. \citet{dongre2026attention} established the quantitative foundation for this line of work: they defined the Goal Attention Ratio (GAR) and showed that attention to system-prompt goal tokens decays by 27--48\% across turns in 12 models, while residual stream probes retain goal information with AUC\,=\,0.98. We observe a steeper 70.8\% decline on Qwen-2.5-7B-Instruct (\S\ref{sec:experiments}). This dissociation between attention collapse and residual persistence motivates our gating intervention. Their work characterizes the phenomenon; ours attempts the first systematic cure and, in doing so, uncovers why lightweight interventions fail to transfer from training to inference.
5	
6	\paragraph{Instruction stability.}
7	\citet{li2024measuring} independently quantified instruction instability in multi-turn dialogs and proposed split-softmax---separating instruction from conversation tokens during attention computation---as an inference-time remedy. Split-softmax restructures the attention mechanism itself and requires no retraining, but cannot address exposure bias in auxiliary losses that depend on training-time optimization. Our work adds systematic diagnosis (five-way controlled comparison + PCGrad exclusion), exposure bias attribution, and training-time mitigation via scheduled sampling; our $\beta$-steering compl
…[truncated 2921 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 190 · 2026-05-22T12:47:47.743251+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 191 · 2026-05-22T12:47:48.145032+00:00_

1	\section{Training Hyperparameters}\label{sec:appendix-hyper}
2	
3	All fine-tuned variants share the following configuration: Qwen-2.5-7B-Instruct base model, LoRA rank 16 ($\alpha$=32) on \texttt{q\_proj} and \texttt{v\_proj}, AdamW optimizer (lr = $2 \times 10^{-4}$, $\beta_1$=0.9, $\beta_2$=0.999), batch size 1 with gradient accumulation 8, 3 epochs over 8K UltraChat conversations, maximum sequence length 2048, seed 42. ThreadGate gates use a 10$\times$ learning rate multiplier and initial bias 1.5 ($\sigma(1.5) \approx 0.82$).
4	
5	\section{Loss Formulation Search}\label{sec:appendix-loss}
6	
7	Table~\ref{tab:loss-iterations} summarizes the seven loss configurations explored before arriving at the final MSE + gate diversity formulation (\S\ref{sec:loss}). Configurations v1--v6 span three alternative loss families; none converged during training.
8	
9	\begin{table}[h]
10	\centering\small
11	\caption{Loss formulation iterations on Qwen-2.5-7B-Instruct. GAR-ours (teacher-forced) and PPL are reported only for the converged configuration.}
12	\label{tab:loss-iterations}
13	\begin{tabular}{l l l c c}
14	\toprule
15	 & \textbf{Loss Family} & \textbf{Status} & \textbf{GAR} & \textbf{PPL} \\
16	\midrule
17	v1  & Cumulative            & \texttimes~GAR loss $\to$ 0     & ---  & ---  \\
18	v2  & Cumulative + $\varepsilon$ & \texttimes~same trajectory & ---  & ---  \\
19	v3  & Maximize ($\lambda$=2)  & \texttimes~gate frozen        & ---  & ---  \\
20	v3b & Maximize ($\lambda$=10) & \texttimes~identity collapse   & ---  & ---  \\
21	v5  & Maximize ($\lambda$=1)  & \texttimes~identity collapse   & ---  & ---  \\
22	v6  & Smooth saturation       & \texttimes~identity collapse   & ---  & ---  \\
23	v7  & MSE + gate div          & \checkmark~converged           & 0.50 & 2.78 \\
24	\bottomrule
25	\end{tabular}
26	\end{table}
27	
28	Maximize-family losses ($-\text{mean}(\text{GAR})$) consistently drove gates toward identity: the unbounded objective rewards full pass-through ($g \
…[truncated 201 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "Read",
  "elapsed_ms": 401
}
```

</details>

---


### Tool call

_source line 192 · 2026-05-22T12:47:48.145593+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/references.bib"
  }
}
```

</details>

---


### Tool result

_source line 193 · 2026-05-22T12:47:48.196757+00:00_

1	% ============================================================
2	% Multi-Turn Attention
3	% ============================================================
4	
5	@article{dongre2026attention,
6	  author  = {Dongre, Vardhan and Hsieh, Joseph and Lai, Viet Dac and Yoon, Seunghyun and Bui, Trung and Hakkani-T\"{u}r, Dilek},
7	  title   = {{When Attention Closes: How LLMs Lose the Thread in Multi-Turn Interaction}},
8	  journal = {arXiv preprint arXiv:2605.12922},
9	  year    = {2026},
10	  url     = {https://arxiv.org/abs/2605.12922}
11	}
12	
13	@article{laban2025lost,
14	  author  = {Laban, Philippe and Hayashi, Hiroaki and Zhou, Yingbo and Neville, Jennifer},
15	  title   = {{LLMs Get Lost In Multi-Turn Conversation}},
16	  journal = {arXiv preprint arXiv:2505.06120},
17	  year    = {2025},
18	  url     = {https://arxiv.org/abs/2505.06120}
19	}
20	
21	@article{liu2026intent,
22	  author  = {Liu, Geng and Zhu, Fei and Feng, Rong and Ma, Changyi and Wang, Shiqi and Meng, Gaofeng},
23	  title   = {{Intent Mismatch Causes LLMs to Get Lost in Multi-Turn Conversation}},
24	  journal = {arXiv preprint arXiv:2602.07338},
25	  year    = {2026},
26	  url     = {https://arxiv.org/abs/2602.07338}
27	}
28	
29	@inproceedings{bai2024mtbench101,
30	  author    = {Bai, Ge and Liu, Jie and Bu, Xingyuan and He, Yancheng and Liu, Jiaheng and Zhou, Zhanhui and Lin, Zhuoran and Su, Wenbo and Ge, Tiezheng and Zheng, Bo and Ouyang, Wanli},
31	  title     = {{MT-Bench-101: A Fine-Grained Benchmark for Evaluating Large Language Models in Multi-Turn Dialogues}},
32	  booktitle = {Annual Meeting of the Association for Computational Linguistics},
33	  year      = {2024},
34	  url       = {https://arxiv.org/abs/2402.14762}
35	}
36	
37	% ============================================================
38	% Residual Gating and Adaptive Depth
39	% ============================================================
40	
41	@inproceedings{fan2020layerdrop,
42	  author    = {Fan, Angela and Grave, Edouard and Joulin
…[truncated 9013 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 194 · 2026-05-22T12:48:15.065136+00:00_

called mcp__agent-ml-research__dispatch_visual_check

<details open><summary>🔧 Tool call — mcp__agent-ml-research__dispatch_visual_check</summary>

```json
{
  "project": "turn_residual_gating",
  "review_chat_id": "oc_9287ee173cf15d688adcd081f5d861f5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "tool_args": {
    "project": "turn_residual_gating",
    "review_chat_id": "oc_9287ee173cf15d688adcd081f5d861f5"
  }
}
```

</details>

---


### Tool call

_source line 195 · 2026-05-22T12:48:15.520649+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "turn_residual_gating"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "turn_residual_gating"
  }
}
```

</details>

---


### Tool result

_source line 196 · 2026-05-22T12:48:35.987763+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 20922
}
```

</details>

---


### Tool result

_source line 197 · 2026-05-22T12:48:35.988215+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 20467
}
```

</details>

---


### Tool call

_source line 198 · 2026-05-22T12:48:36.140631+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "project": "turn_residual_gating",
  "reviewer_id": "1",
  "round_number": "1",
  "text": "你是 Reviewer 1，负责 **方法严谨性 + 实验设计** 审查。\n\n## Venue 信息\n- **目标**: EMNLP 2026 via ACL Rolling Review (ARR August 2026 cycle)\n- **截止日期**: 2026-08-03\n- **格式**: Long paper, 正文 8 页, 参考文献不限, Limitations 章节必须有但不计入页数\n- **模板**: ACL style template (`\\usepackage[review]{acl}`)\n- **匿名**: Double-blind\n\n## 论文路径\n- LaTeX 源码: `/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/main.tex`\n- 各 section 在 `paper/sections/` 下\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_2/submitted.pdf`\n\n## 论文概要\n标题: \"Why Per-Layer Residual Gating Fails to Fix Multi-Turn Attention Degradation: A Mechanistic Analysis\"\n\n提出 ThreadGate（per-layer content-and-turn-conditioned MLP gate），与 NTP + auxiliary GAR loss 联合训练。五路对比（ThreadGate, +PCGrad, Uniform Gate, LoRA-only, Base）显示 gating 无效，teacher-forced GAR=0.50 但 autoregressive GAR 跌至 0.015-0.025（20-33× gap）。归因于 exposure bias，inference-time steering 和 scheduled sampling 作为 mitigation。跨模型在 Llama-3.1-8B 确认。\n\n## 你的审查侧重\n\n请重点审查以下方面：\n\n1. **五路对比的实验控制质量**：每对对比是否真正隔离了声称的单一因素？控制变量是否充分？\n2. **统计支撑**：多少条件有 multi-seed？样本量是否充分？Bootstrap CI / 显著性检验是否恰当？\n3. **Exposure bias 归因的因果链**：从观察到的 TF-AR gap → exposure bias 的推理是否严密？有无未排除的替代假说？PCGrad exclusion 的 modus tollens 论证是否成立？\n4. **Scheduled sampling 实验**：单 seed 的统计可靠性？gap 从 31× 压缩到 1.57× 的声称是否过强？\n5. **Cross-model 评估**：Llama 上仅 3/5 条件，用 median 而非 mean，N=20——这些设计选择是否充分？\n6. **Instruction retention 实验**：McNemar p=0.077 不显著，r=0.200 极弱——是否应该从 contribution 中移除或大幅降级？\n7. **格式合规**：8 页限制、匿名、Limitations 章节是否满足 EMNLP 要求\n\n请按 ARR Overall Assessment 评分标准给出评分（1-5），并提供 Strengths、Weaknesses（逐条）、Questions、Missing References。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "project": "turn_residual_gating",
    "reviewer_id": "1",
    "round_number": "1",
    "text": "你是 Reviewer 1，负责 **方法严谨性 + 实验设计** 审查。\n\n## Venue 信息\n- **目标**: EMNLP 2026 via ACL Rolling Review (ARR August 2026 cycle)\n- **截止日期**: 2026-08-03\n- **格式**: Long paper, 正文 8 页, 参考文献不限, Limitations 章节必须有但不计入页数\n- **模板**: ACL style template (`\\usepackage[review]{acl}`)\n- **匿名**: Double-blind\n\n## 论文路径\n- LaTeX 源码: `/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/main.tex`\n- 各 section 在 `paper/sections/` 下\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_2/submitted.pdf`\n\n## 论文概要\n标题: \"Why Per-Layer Residual Gating Fails to Fix Multi-Turn Attention Degradation: A Mechanistic Analysis\"\n\n提出 ThreadGate（per-layer content-and-turn-conditioned MLP gate），与 NTP + auxiliary GAR loss 联合训练。五路对比（ThreadGate, +PCGrad, Uniform Gate, LoRA-only, Base）显示 gating 无效，teacher-forced GAR=0.50 但 autoregressive GAR 跌至 0.015-0.025（20-33× gap）。归因于 exposure bias，inference-time steering 和 scheduled sampling 作为 mitigation。跨模型在 Llama-3.1-8B 确认。\n\n## 你的审查侧重\n\n请重点审查以下方面：\n\n1. **五路对比的实验控制质量**：每对对比是否真正隔离了声称的单一因素？控制变量是否充分？\n2. **统计支撑**：多少条件有 multi-seed？样本量是否充分？Bootstrap CI / 显著性检验是否恰当？\n3. **Exposure bias 归因的因果链**：从观察到的 TF-AR gap → exposure bias 的推理是否严密？有无未排除的替代假说？PCGrad exclusion 的 modus tollens 论证是否成立？\n4. **Scheduled sampling 实验**：单 seed 的统计可靠性？gap 从 31× 压缩到 1.57× 的声称是否过强？\n5. **Cross-model 评估**：Llama 上仅 3/5 条件，用 median 而非 mean，N=20——这些设计选择是否充分？\n6. **Instruction retention 实验**：McNemar p=0.077 不显著，r=0.200 极弱——是否应该从 contribution 中移除或大幅降级？\n7. **格式合规**：8 页限制、匿名、Limitations 章节是否满足 EMNLP 要求\n\n请按 ARR Overall Assessment 评分标准给出评分（1-5），并提供 Strengths、Weaknesses（逐条）、Questions、Missing References。"
  }
}
```

</details>

---


### Tool result

_source line 199 · 2026-05-22T12:48:52.867919+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 16727
}
```

</details>

---


### Tool call

_source line 200 · 2026-05-22T12:48:53.070674+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "project": "turn_residual_gating",
  "reviewer_id": "2",
  "round_number": "1",
  "text": "你是 Reviewer 2，负责 **新颖性 + 完整性 + 写作质量** 审查。\n\n## Venue 信息\n- **目标**: EMNLP 2026 via ACL Rolling Review (ARR August 2026 cycle)\n- **截止日期**: 2026-08-03\n- **格式**: Long paper, 正文 8 页, 参考文献不限, Limitations 章节必须有但不计入页数\n- **模板**: ACL style template (`\\usepackage[review]{acl}`)\n- **匿名**: Double-blind\n\n## 论文路径\n- LaTeX 源码: `/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/main.tex`\n- 各 section 在 `paper/sections/` 下\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_2/submitted.pdf`\n\n## 论文概要\n标题: \"Why Per-Layer Residual Gating Fails to Fix Multi-Turn Attention Degradation: A Mechanistic Analysis\"\n\n提出 ThreadGate（per-layer content-and-turn-conditioned MLP gate），与 NTP + auxiliary GAR loss 联合训练。五路对比（ThreadGate, +PCGrad, Uniform Gate, LoRA-only, Base）显示 gating 无效，teacher-forced GAR=0.50 但 autoregressive GAR 跌至 0.015-0.025（20-33× gap）。归因于 exposure bias，inference-time steering 和 scheduled sampling 作为 mitigation。跨模型在 Llama-3.1-8B 确认。\n\n## 你的审查侧重\n\n请重点审查以下方面：\n\n1. **Contribution 声称是否合理**：\n   - (1) \"systematic diagnostic framework\" 实际是五路消融——是否过度包装？\"in principle applicable to other auxiliary objective analyses\" 有经验验证吗？\n   - (2) \"first empirical characterization of how exposure bias selectively destroys auxiliary attention loss generalization\" 是否准确？有无 prior work 已涉及？\n   - (3) 标题 \"Per-Layer Residual Gating\" 是否足够精确？仅测试了 ThreadGate + Uniform Gate\n   - (4) \"principled negative baseline\" 价值如何？\n2. **Related Work 覆盖**：\n   - 是否遗漏了重要的竞争方法？Li et al. (2024) split-softmax 覆盖是否充分？\n   - Exposure bias 文献是否完整？\n   - Multi-turn dialogue 改善方法是否有遗漏？\n3. **写作质量**：\n   - \"20-33× gap\" 等关键数字在 Abstract/Intro/Experiments/Analysis/Discussion/Conclusion 中重复出现——是否冗余？\n   - 行文是否简洁？是否有不必要的重复？\n   - Figure/Table caption 是否准确、不含 overclaim？\n4. **Framing 合理性**：\n   - \"a proximal cause consistent with our evidence\" 这一措辞是否恰当？是否仍有 overclaim？\n   - Negative result 的叙事策略是否有效？读者能从中获得什么 actionable insight？\n5. **引用准确性**：\n   - GAR 在 Dongre et al. 中的原始全称是什么？本文用的 \"Goal Attention Ratio\" 是否正确？\n   - Bib 格式是否一致？\n6. **格式合规**：页数、匿名、Limitations 章节\n\n请按 ARR Overall Assessment 评分标准给出评分（1-5），并提供 Strengths、Weaknesses（逐条）、Questions、Missing References。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "project": "turn_residual_gating",
    "reviewer_id": "2",
    "round_number": "1",
    "text": "你是 Reviewer 2，负责 **新颖性 + 完整性 + 写作质量** 审查。\n\n## Venue 信息\n- **目标**: EMNLP 2026 via ACL Rolling Review (ARR August 2026 cycle)\n- **截止日期**: 2026-08-03\n- **格式**: Long paper, 正文 8 页, 参考文献不限, Limitations 章节必须有但不计入页数\n- **模板**: ACL style template (`\\usepackage[review]{acl}`)\n- **匿名**: Double-blind\n\n## 论文路径\n- LaTeX 源码: `/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/main.tex`\n- 各 section 在 `paper/sections/` 下\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_2/submitted.pdf`\n\n## 论文概要\n标题: \"Why Per-Layer Residual Gating Fails to Fix Multi-Turn Attention Degradation: A Mechanistic Analysis\"\n\n提出 ThreadGate（per-layer content-and-turn-conditioned MLP gate），与 NTP + auxiliary GAR loss 联合训练。五路对比（ThreadGate, +PCGrad, Uniform Gate, LoRA-only, Base）显示 gating 无效，teacher-forced GAR=0.50 但 autoregressive GAR 跌至 0.015-0.025（20-33× gap）。归因于 exposure bias，inference-time steering 和 scheduled sampling 作为 mitigation。跨模型在 Llama-3.1-8B 确认。\n\n## 你的审查侧重\n\n请重点审查以下方面：\n\n1. **Contribution 声称是否合理**：\n   - (1) \"systematic diagnostic framework\" 实际是五路消融——是否过度包装？\"in principle applicable to other auxiliary objective analyses\" 有经验验证吗？\n   - (2) \"first empirical characterization of how exposure bias selectively destroys auxiliary attention loss generalization\" 是否准确？有无 prior work 已涉及？\n   - (3) 标题 \"Per-Layer Residual Gating\" 是否足够精确？仅测试了 ThreadGate + Uniform Gate\n   - (4) \"principled negative baseline\" 价值如何？\n2. **Related Work 覆盖**：\n   - 是否遗漏了重要的竞争方法？Li et al. (2024) split-softmax 覆盖是否充分？\n   - Exposure bias 文献是否完整？\n   - Multi-turn dialogue 改善方法是否有遗漏？\n3. **写作质量**：\n   - \"20-33× gap\" 等关键数字在 Abstract/Intro/Experiments/Analysis/Discussion/Conclusion 中重复出现——是否冗余？\n   - 行文是否简洁？是否有不必要的重复？\n   - Figure/Table caption 是否准确、不含 overclaim？\n4. **Framing 合理性**：\n   - \"a proximal cause consistent with our evidence\" 这一措辞是否恰当？是否仍有 overclaim？\n   - Negative result 的叙事策略是否有效？读者能从中获得什么 actionable insight？\n5. **引用准确性**：\n   - GAR 在 Dongre et al. 中的原始全称是什么？本文用的 \"Goal Attention Ratio\" 是否正确？\n   - Bib 格式是否一致？\n6. **格式合规**：页数、匿名、Limitations 章节\n\n请按 ARR Overall Assessment 评分标准给出评分（1-5），并提供 Strengths、Weaknesses（逐条）、Questions、Missing References。"
  }
}
```

</details>

---


### Tool result

_source line 201 · 2026-05-22T12:48:54.672229+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1601
}
```

</details>

---


### Tool call

_source line 202 · 2026-05-22T12:49:01.467205+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "turn_residual_gating"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "turn_residual_gating"
  }
}
```

</details>

---


### Tool result

_source line 203 · 2026-05-22T12:49:01.773260+00:00_

{"result":"# 项目 turn_residual_gating 概况\n\n## 实验状态 (38 个)\n\n- **phase2_tg_s42_v7**: DONE (success) — \n- **phase2_tg_s42_v9_pcgrad**: DONE (success) — \n- **phase2_lora_only_s42**: DONE (success) — \n- **phase2_ug_s42**: DONE (success) — \n- **phase2_tg_s42_v8_schedsampling**: DONE (failed) — \n- **analysis_attention_heatmap**: DONE (success) — \n- **analysis_gradient_conflict**: DONE (success) — \n- **phase2_4way_eval_heldout**: DONE (success) — \n- **phase2_4way_eval**: DONE (negative) — \n- **phase2_tg_s42_v5**: DONE (negative) — \n- **phase2_tg_s42_v4**: DONE (failed) — \n- **phase2_tg_s42_v3b**: DONE (success) — \n- **phase2_tg_s42_v3**: DONE (negative) — \n- **phase2_tg_s42_v2**: DONE (killed) — \n- **phase1_gar_diag**: DONE (success) — \n\n## 最新报告\n# Handover — 2026-05-22\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\n|--------|------|------|---------|-----|\n| d048_ss_s42 | Scheduled sampling (ratio=0.3) with ThreadGate reduces the ~30× TF-AR GAR gap by exposing the model to its own generated text during training. Multi-seed run (s42) under D048 unified protocol to establish mean±std for statistical testing. SS is the strongest mitigation candidate (prior single-seed showed gap 31×→1.57×). | — | — | — |\n\n## 待处理\n- llama_tg_training（准备中）\n\n## 近期结论\n- **eval_llama_ar_n20** (success): N=20 AR eval stabilizes Llama 3-way (Base/TG/LoRA-only) autoregressive GAR estimates. N=5 suffered from outlier influence (3/5 conv had GAR>0.4 outlier turns); N=20 provides robust mean±std. ← 基于 eval_llama_lora_only_s42\n- **eval_llama_lora_only_s42** (success): LoRA-only ablation (no gate) on Llama-3.1-8B: if TG's GAR improvement comes from the gate, LoRA-only should show minimal GAR recovery vs base. ← 基于 llama_lora_only_s42\n- **llama_lora_only_s42** (success): Llama-3.1-8B LoRA-only baseline (gate=none, 无 gating 机制): 与 Llama TG s42 对比，验证 gating 对 Llama 的增量贡献。如果 LoRA-only GAR ≈ TG GAR → gating 零增量与 Qwen 结论一致（C5 跨模型）。 ← 基于 llama_tg_s42\n
…[truncated 286 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 306
}
```

</details>

---


### Assistant

_source line 204 · 2026-05-22T12:49:20.902337+00:00_

**Round 3 审稿启动汇报**

| 项目 | 状态 |
|------|------|
| Venue 确认 | EMNLP 2026 / ARR Aug cycle / deadline 2026-08-03 / 8页 / double-blind |
| Reviewer 1 | 已派发 — 方法严谨性 + 实验设计 |
| Reviewer 2 | 已派发 — 新颖性 + 完整性 + 写作质量 |
| 视觉审查 | 已派发（独立 Agent，不阻塞） |
| 外部审稿 | 未配置，本轮不使用 |
| Issue Tracker | 已读取 Round 1/2 共 20 条 issue（7 resolved, 13 open/in_progress） |

等待两位 Reviewer 的 Round 1 独立初审结果。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director"
}
```

</details>

---


## Round 13

## Round 13

2 recorded events


### User

_source line 205 · 2026-05-22T12:53:49.531977+00:00_

[Reviewer 1 审稿意见]:
## 总体评分
**Overall**: 3.0 / 5 — Findings（可被 Findings 接收）
**一句话总结**: 诊断框架设计精良、负面结果对社区有价值，但核心 AR 评估样本量过小（N=5）、scheduled sampling 单种子可靠性不足、exposure bias 归因缺少替代假说的排除实验，统计支撑尚不足以支撑 conference-level 接收。

---

## 官方维度打分（来自 ACL Rolling Review review form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.0/5 | 诊断链逻辑通顺（gate inversion → PCGrad exclusion → distribution shift → TRC specificity），但 AR 评估 N=5、无 CI/显著性检验、scheduled sampling 双种子差异大（GAR 0.318 vs 0.418），核心 claim 的统计支撑不充分 |
| Excitement | 3.0/5 | "auxiliary loss 在 AR 下因 exposure bias 选择性失效"这一发现对多任务 LLM 训练有参考价值，但 exposure bias 本身是已知现象，novelty 主要在诊断框架而非机制发现 |
| Reproducibility | 3.5/5 | 超参数、loss 迭代过程（Table 2）、训练细节披露充分；但缺少代码/数据承诺，AR 评估 N=5 使复现验证困难 |
| Overall Assessment | 3.0/5 | Findings-level：诊断框架 solid，但需统计加强才能达到 conference 标准 |

**Reviewer Confidence**: 4/5 — 对 multi-task learning、exposure bias、attention mechanism 分析熟悉，仔细检查了实验设计和统计方法。

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] AR 评估样本量过小，核心 claim 缺乏统计检验

- 具体位置：Table 1, §4.2, §4.3
- 问题：论文的核心发现——20-33× TF-AR gap——在 AR 端仅基于 **N=5 条 10-turn 对话**。五个配置的 AR GAR-ours 分别为 0.012, 0.016, 0.015, 0.015, 0.025，这些差异（尤其 LoRA-only 的 0.025 vs 其余的 0.015-0.016）在 N=5 下无法判断是否具有统计显著性。论文未报告 AR GAR 的 confidence interval 或任何条件间的显著性检验。
- 唯一的多种子验证仅覆盖 ThreadGate 一个条件（seed 42 vs 123），且 ±0.001 的精度在 N=5 下可信度存疑。其余四个条件均为单种子。
- 为什么影响接收："20-33× gap persists across all five configurations" 是全文论证的基石。如果该 gap 的大小在不同种子/样本下有显著变化，归因链条（§5 整节）的可靠性将受到根本性质疑。
- 建议修改方向：(1) 将 AR 评估扩大至至少 N=50（与 steering 实验的 N=50 对齐）；(2) 报告 bootstrap 95% CI；(3) 对五个条件的 AR GAR 做成对检验（例如 paired bootstrap test），明确条件间差异是否显著；(4) 至少为 LoRA-only 和 Uniform Gate 增加第二种子。

**N2** [critical] Scheduled sampling 实验的统计可靠性不足以支撑 contribution-level 声称

- 具体位置：§6 Discussion ("Scheduled sampling as training-time mitigation"), Abstract, §1 contributions (2)
- 问题：该实验仅有两个种子，结果差异很大：seed 1 AR GAR=0.318（gap 1.57×），seed 2（from scratch）AR GAR=0.418（gap 1.20×）。两个种子的 GAR 相差 31%，gap 相差 24%。论文在 abstract 中写 "Scheduled sampling compresses the gap to 1.57×"（仅引用 seed 1），在 contributions 中将其列为 contribution (2) 的一部分，这种呈现方式给读者以较高确定性的印象。
- 更重要的是，两个种子的训练策略不同（seed 1 是标准训练后 resume，seed 2 是从头训练），无法分离种子随机性 vs 训练策略的效应。
- 为什么影响接收：如果 reviewer 或 AC 将 scheduled sampling 视为该论文的 actionable contribution（而非仅是 negative result），其可靠性直接影响论文价值判断。
- 建议修改方向：(1) 至少 3 个种子采用相同训练策略，报告 mean±std；(2) 在 abstract 和 contributions 中明确标注 "preliminary, single-seed"；(3) 或者将 scheduled sampling 从 contribution 列表中移除，仅作为 Discussion 中的 future direction。

**N3** [critical] Exposure bias 归因的因果链不完整——替代假说未被排除

- 具体位置：§5.3 Distribution Shift Analysis, §6 Discussion
- 问题：论文的因果推理是：TF GAR 高 + AR GAR 低 → exposure bias。但从观察到的 TF-AR gap 到 exposure bias 的推理存在未排除的替代假说：
  1. **KV cache drift**：论文在 Discussion 中提到 "KV cache accumulation effects at long context lengths" 但未测试。在 10-turn 对话中，KV cache 长度远超 teacher-forced 片段，可能导致 attention softmax 分母膨胀而非 exposure bias。
  2. **Model-generated text 的统计特性差异**：自回归生成的文本可能系统性地更 repetitive、token 分布更集中，导致 attention entropy 降低。这与 exposure bias 相关但可区分——exposure bias 强调 training distribution mismatch，而 text statistics 差异可通过 teacher-forcing 使用 model-generated text（但非 scheduled sampling 的渐进方式）来隔离。
  3. **GAR-ours 指标在 AR 下的有效性**：GAR-ours 仅测量 last token 对 goal tokens 的 attention。在 AR 下，last token 的 attention 分配可能因 generation dynamics（如 sampling temperature、top-p）而与 TF 不同，即使模型仍然"知道"目标。论文的 TRC 实验（§5.4）部分回应了这一点，但 TRC 测量的是 hidden state 相似性而非 attention 路由。
- Inference-time steering 实验（§4.3）表面上支持 "attention misallocation" 假说，但其推论存在循环性：在 goal tokens 上加 additive bias 当然会增加 goal attention，无论 GAR 低的原因是什么。这不能区分 exposure bias 和上述替代假说。
- 论文在 Discussion 中确实提到了部分替代假说（"progressive attention drift unrelated to exposure bias, KV cache accumulation effects..."），但仅是列举而未排除。
- 为什么影响接收：标题中的 "mechanistic analysis" 意味着超越相关性的因果理解。如果替代假说同样能解释观测，则 exposure bias 归因的 claim 过强。
- 建议修改方向：(1) 设计一个实验区分 exposure bias 和 KV cache drift——例如在 AR 生成后用 ground-truth prefix（而非 model-generated prefix）替换中间 turn 的文本并重新评估 GAR，观察 GAR 是否恢复；(2) 或者将 claim 从 "the failure traces to exposure bias" 弱化为 "the failure is consistent with exposure bias among other possible causes"；(3) 在 inference-time steering 论证中明确承认循环性风险。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] Cross-model evaluation 设计选择的 justification 不充分

- 具体位置：§5.5 Cross-Model Generality
- 问题：
  1. 仅测试 3/5 条件（Base, ThreadGate, LoRA-only），缺少 +PCGrad 和 Uniform Gate。PCGrad exclusion 是核心论证之一，未在 Llama 上复现削弱了 "generality" claim。
  2. 使用 median 而非 mean：论文称 "5-8% of turn-level measurements exhibit sporadic attention spikes" 导致 heavy-tailed distribution，因此用 median。但 (a) 未报告 mean 作为对照；(b) 未解释 spikes 的成因——如果 spikes 是 systematic behavior 而非 noise，丢弃它们可能隐藏重要信号；(c) N=20 with median 已经是 low-power 的估计。
  3. AR 评估 N=20，teacher-forced N=50，两者不匹配。
- 建议：(1) 报告 mean 和 median 双指标；(2) 展示 AR GAR 的完整分布（e.g., boxplot）；(3) 解释 attention spikes 的成因。

**W2** [warning] PCGrad exclusion 的 modus tollens 论证范围被过度概括

- 具体位置：§5.2 PCGrad Gradient Conflict Exclusion
- 问题：论文使用 modus tollens 论证排除 gradient conflict：PCGrad 消除 direction conflict → failure 仍在 → direction conflict 非 cause。但 PCGrad 仅处理梯度方向冲突，未处理：
  1. **Magnitude imbalance**（NTP 梯度 7.5-14.7× 大于 GAR，论文自身报告了这一点）——这是 multi-task learning 中已知的独立失效模式，GradNorm (Chen et al., 2018) 专门针对此问题。
  2. **Nash equilibrium violations**（Navon et al., 2022）
  论文在 Limitations 中承认了这些限制，但在主体叙述（§5.2 最后一段 "With gradient conflict ruled out..."）中写法过于绝对，给人以 gradient conflict 已被完全排除的印象。
- 建议：在 §5.2 中将 "gradient conflict" 精确限定为 "gradient direction conflict"，并在论证结论处明确提及 magnitude imbalance 未被排除。

**W3** [warning] Instruction retention 实验不显著，应更明确降级

- 具体位置：§6 Discussion ("Instruction retention under steering")
- 问题：McNemar p=0.077（α=0.05 下不显著），GAR-compliance r=0.200（极弱相关）。虽然标注为 "exploratory evidence"，但仍占用了 Discussion 中约 1/4 的篇幅，且在 contributions (3) 中被包含（"providing constructive evidence that attention misallocation—not representation degradation—is a proximal cause"）。
- 这个实验基于单模型、18 种 constraint types、单一 β 值，统计功效非常低。
- 建议：(1) 压缩至 1-2 句话或移至 Appendix；(2) 从 contribution list 中移除或明确标注 "exploratory, not statistically significant"。

**W4** [warning] 五路对比的控制变量分析存在盲区

- 具体位置：§4.1, Table 1
- 问题：论文声称每对对比 "isolates one factor"，但存在以下控制问题：
  1. **LoRA-only vs ThreadGate**：差异不仅是 gate 的有无，还包括 diversity loss（LoRA-only 无 L_div）。如果 diversity loss 对 NTP 有轻微负面影响（恰好被 gating 的正面效应抵消），则两者打平并不意味着 gating 无效。
  2. **Uniform Gate**：用 learned constant vector 替代 turn embedding。但 constant vector 仍是可学习的——它可以学到一个 average turn embedding，部分保留 turn conditioning 的效应。更干净的消融是用固定的 random vector 或 zero vector。
  3. 所有 fine-tuned variants 共享相同的 LoRA rank (16)、α (32)、target modules (q_proj, v_proj)。如果 LoRA 的容量已经足以学到 GAR pattern（仅在 TF 下），那么额外的 gate 参数自然不会提供增量收益。这不是 "gating 无效" 的结论，而是 "LoRA 已经饱和了 TF GAR target" 的结论。
- 建议：(1) 在 §4.1 或 §5 中讨论 LoRA capacity saturation 这一替代解释；(2) 考虑一个无 GAR loss 的 LoRA-only baseline（纯 NTP 训练）来建立 GAR loss 本身的增量效应。

---

## 小问题（不影响接收）

- §1, "0.0418 at turn 1 to 0.0122 at mid-conversation" — 这是 base model 的 GAR-Dongre 还是 GAR-ours？应明确标注。
- Table 1 caption: "GAR-O = GAR-ours; GAR-D = GAR-Dongre" 在 caption 末尾，但表头缩写出现在第一行，建议移到 caption 开头。
- §5.1: Wilcoxon signed-rank test p = 3.73 × 10⁻⁸ — 这是对 27/28 layers 的 paired test？应说明具体 paired 在什么上（across samples? across layers?）。
- §5.5: "excluding the first two turns" 的 justification 不充分——为什么排除？如果 GAR 在 early turns 本来就高，排除它们会 downward bias 中位数。
- Figure 1 overview diagram 信息密度高，但 "ROOT" 标签的位置和意义可以更清晰。
- §3.2: gate initialization near 0.82 with 10× lr multiplier — 选择 0.82 的依据？是否做过 sensitivity analysis？

---

## 主要优势

1. **诊断框架设计精良**：五路对比系统性地隔离了 turn conditioning、gating mechanism、gradient direction conflict、fine-tuning 四个因素，逻辑结构清晰。每一步排除都有明确的实验对应。
2. **诚实且有价值的负面结果**：不伪装成正面结果，直接呈现 gating 失败并分析原因，对 multi-task LLM 训练社区有实际参考价值。
3. **多层证据链**：TRC specificity（§5.4）验证 exposure bias 的选择性、inference-time steering 提供 constructive evidence、cross-model replication 增强泛化性。
4. **Loss formulation search 的透明度**：Table 2（Appendix B）展示了 7 次迭代中 6 次失败的完整记录，增强了方法论的可信度。
5. **写作结构清晰**：从 observation → intervention → failure → diagnosis 的叙事弧线自然流畅，Related Work 对 exposure bias / multi-task gradient conflict / residual gating 的文献覆盖充分。

---

## Missing References

- **Ranzato et al., 2016** ("Sequence Level Training with Recurrent Neural Networks") — scheduled sampling 之外的 sequence-level training 方法，论文讨论 exposure bias mitigation 时应提及。（注：论文已引用此文。）
- **Zhang et al., 2019** ("Bridging the Gap between Training and Inference for Neural Machine Translation") — exposure bias 在 NMT 中的经典分析，使用 oracle word 和 sampling 策略，与本文的 scheduled sampling 直接相关。
- **Lamb et al., 2016** ("Professor Forcing") — 已引用，但值得注意该方法用 GAN 判别训练/推理分布差异，可作为本文归因的补充实验思路。（已引用。）

---

## Questions to Authors

1. 如果将 AR 评估从 N=5 扩大到 N=50（与 steering 实验对齐），五个条件的 AR GAR 排序和 gap 大小是否保持不变？
2. 是否考虑过一个 "LoRA-only + NTP only"（无 GAR loss）baseline？这将直接回答 GAR loss 本身贡献了多少 TF GAR 提升。
3. Scheduled sampling 的两个种子采用了不同的训练策略（resume vs from scratch）。在相同策略下做 3+ 种子是否可行？
4. Inference-time steering 的 β=3 operating point 在 held-out 对话中的 instruction retention 效果是否在 Llama 上也做了测试？
5. 论文提到 "5-8% of turn-level measurements exhibit sporadic attention spikes"——这些 spikes 出现在特定的 turn position 还是随机分布？它们的成因是什么？

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 206 · 2026-05-22T12:53:58.428794+00:00_

Reviewer 1 审稿意见已收到。等待 Reviewer 2 完成初审后进行交叉分享。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director"
}
```

</details>

---


## Round 14

## Round 14

2 recorded events


### User

_source line 207 · 2026-05-22T12:54:11.467893+00:00_

[Reviewer 1 审稿结果]:
Round 1 审稿完成，已通过 `review_reviewer_post_to_director` 提交给 Review Director。

**评分摘要**：Overall 3.0/5（Findings），Soundness 3.0/5，Excitement 3.0/5。

**3 个 Must-Fix**：
- **N1**: AR 评估 N=5 过小，核心 20-33× gap 无 CI/显著性检验
- **N2**: Scheduled sampling 双种子结果差异大（GAR 0.318 vs 0.418），但 abstract 仅引用单种子数据
- **N3**: Exposure bias 归因未排除 KV cache drift、model-generated text statistics 等替代假说，inference-time steering 论证存在循环性风险

**4 个 Should-Fix**：cross-model 仅 3/5 条件 + median 选择缺乏 justification、PCGrad modus tollens 范围被过度概括、instruction retention 不显著但篇幅过多、五路对比存在 LoRA capacity saturation 等未讨论的替代解释。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 208 · 2026-05-22T12:54:16.303650+00:00_

Reviewer 1 意见已收到。等待 Reviewer 2 完成后进行交叉分享。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director"
}
```

</details>

---


## Round 15

## Round 15

6 recorded events


### User

_source line 209 · 2026-05-22T12:54:21.026928+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 审稿报告（新颖性 + 完整性 + 写作质量）

**论文**: "Why Per-Layer Residual Gating Fails to Fix Multi-Turn Attention Degradation: A Mechanistic Analysis"
**Venue**: EMNLP 2026 via ACL Rolling Review

---

## 总体评分
**Overall**: 3.0 (Findings)
**一句话总结**: 论文提出了一个有意义的 negative result（gating 无法修复多轮注意力衰减，root cause 是 exposure bias），诊断链条完整，但核心指标 GAR 的全称引用错误（原文是 Goal Accessibility Ratio，非 Goal Attention Ratio），contribution 包装过度，且写作冗余严重，关键数字在六个章节中反复出现。

## 官方维度打分（来自 ARR review form）
| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3/5 | 五路对比设计合理，PCGrad exclusion 逻辑清晰，但 GAR 全称引用错误（N1）动摇了对基础定义准确性的信任；scheduled sampling 仅 single seed，steering 实验的 downstream task evaluation 缺失 |
| Excitement | 2.5/5 | Negative result 本身有价值，exposure bias 对 auxiliary loss 的选择性破坏是新颖发现，但 actionable insight 有限（steering 需要 oracle access to goal tokens，scheduled sampling 仅 preliminary） |
| Reproducibility | 3.5/5 | 超参、数据量、硬件均已报告；代码未提供但方法描述充分；seed 42+123 双 seed 验证仅覆盖 ThreadGate |
| Overall Assessment | 3.0 | 可被 Findings 接收，但 Must-Fix 问题（N1 GAR 命名错误、N2 页数超限）需先修正 |
| Reviewer Confidence | 4/5 | 仔细阅读了全文和附录，验证了 Dongre et al. 原文的 GAR 定义 |

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] GAR 全称引用错误：原文为 "Goal Accessibility Ratio"，非 "Goal Attention Ratio"
- 具体位置：Abstract (line 1), §1 Introduction (line 3, line 5), §3.1 Preliminaries (line 6), §2 Related Work (line 4), 以及全文所有出现 "Goal Attention Ratio" 的位置
- 问题：Dongre et al. (2026, arXiv:2605.12922) 原文定义为 **"Goal Accessibility Ratio (GAR)"**，本文在所有引用处均误写为 "Goal Attention Ratio"。我已通过 arXiv abstract 验证原文措辞："We introduce the Goal Accessibility Ratio (GAR), measuring attention from generated tokens to task-defining goal tokens"。
- 为什么影响接收：这是论文最核心的度量指标，全称引用错误直接损害学术严谨性。Reviewer 和 AC 会质疑作者是否仔细阅读了所引用的基础文献。此外，"Attention" vs "Accessibility" 有语义差异——原作者选择 "Accessibility" 而非 "Attention" 可能有其考量（accessibility 暗示 information routing 而非单纯 attention weight）。
- 建议修改方向：全文替换 "Goal Attention Ratio" → "Goal Accessibility Ratio"。如果作者有意使用不同名称，应明确说明与原文术语的区别及理由。

**N2** [critical] 正文疑似超过 8 页限制
- 具体位置：PDF 第 8-9 页
- 问题：根据 PDF 排版，§6 Discussion 从第 8 页底部开始，延续到第 9 页约 60% 处；§7 Conclusion 在第 9 页上半部分。Limitations（§8）和 References 从第 9 页下半部分开始。EMNLP 2026 long paper 正文限制为 **严格 8 页**（Limitations 和 References 不计入）。§7 Conclusion 属于正文，因此正文约占 8.4 页，超出约 0.4 页。
- 为什么影响接收：ARR 格式检查可能直接 desk-reject 超页论文，即使内容合格。
- 建议修改方向：压缩 §6 Discussion（instruction retention under steering 段落可移入 appendix）和 §5 Analysis（部分 per-layer 细节可精简）。Conclusion 已经足够简短，无需进一步压缩。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] "20–33× gap" 在六个章节中过度重复
- 具体位置：Abstract, §1 Introduction (至少 3 次), §4.2 Main Results, §5.3 Distribution Shift, §6 Discussion, §7 Conclusion
- 问题：同一数字 "20–33×" 在全文至少出现 8 次，"0.015–0.025" 出现至少 5 次。这不是 reinforcement，而是冗余。读者在 Abstract 就已记住这个数字，后续章节每次 re-state 都减少信息密度。对于 8 页限制的论文，信息密度至关重要。
- 建议：Abstract 和 Introduction 各保留一次完整数字，后续章节引用 "the order-of-magnitude TF–AR gap (§4.2)" 即可。节省的空间可用于更深入的分析或解决 N2 页数问题。

**W2** [warning] Contribution (1) "systematic diagnostic framework" 过度包装
- 具体位置：§1 Introduction, contribution 列表第 (1) 项
- 问题：五路消融 + PCGrad exclusion + per-layer gradient 分析确实是系统性的实验设计，但称之为 "framework" 暗示可复用性和通用性。论文声称 "in principle applicable to other auxiliary objective analyses" 但无任何验证。实际上这是一个精心设计的消融实验，而非一个可移植的诊断工具。
- 建议：改为 "systematic diagnostic methodology" 或 "controlled ablation protocol"，并删除 "in principle applicable" 的泛化声称，或在 Limitations 中明确说明未验证其迁移性。

**W3** [warning] 标题 "Per-Layer Residual Gating" 暗示测试了广泛的 gating 方法，实际仅测试两种
- 具体位置：标题
- 问题：标题使用泛化表述 "Per-Layer Residual Gating"，但论文仅测试了 ThreadGate（content-and-turn-conditioned）和 Uniform Gate（content-only）两种变体。其他 per-layer gating 方法（如 Mixture-of-Depths 的 learned routing, CALM 的 early exit）均未测试。标题的 scope 暗示比实际覆盖面更广。
- 建议：考虑改为 "Why Content-and-Turn-Conditioned Residual Gating Fails..." 或在 Limitations 中明确讨论未覆盖的 gating 类型。

**W4** [warning] 缺少重要相关工作：Rhea (2025)
- 具体位置：§2 Related Work
- 问题：Rhea (arXiv:2512.06869, Dec 2025) 提出 Role-aware Heuristic Episodic Attention，专门针对多轮对话中的注意力污染/稀释/漂移问题，通过 Instructional Memory 维持 system prompt 保真度（IAR > 8.1），且是 inference-time 方案。这与本文的 §4.3 inference-time steering 和 §6 Discussion 中对 split-softmax 的讨论高度相关。未引用 Rhea 使 Related Work 中 "Attention manipulation" 和 "Instruction stability" 的覆盖不完整。
- 建议：在 §2 "Attention manipulation" 或 "Instruction stability" 段落中引用 Rhea，并在 §6 Discussion 中与 β-steering 做简要对比（两者都是 inference-time 方案，但 Rhea 不需要 oracle access to goal tokens）。

**W5** [warning] Contribution (2) "first empirical characterization" 的 novelty claim 需更谨慎
- 具体位置：§1 Introduction, contribution 列表第 (2) 项
- 问题：声称 "the first empirical characterization of how exposure bias selectively destroys auxiliary attention loss generalization"。虽然我未找到完全相同的先行工作，但 "first" 声明在 reviewer 眼中风险很高——如果存在任何相关工作（例如 multi-task learning 中 auxiliary loss 的 train-test gap 研究），这一声明就会被直接挑战。更安全的措辞不会减弱实际贡献。
- 建议：改为 "a detailed empirical characterization of..." 或 "to our knowledge, the first..."。

**W6** [warning] Scheduled sampling 结果基于 single seed，但论文多处引用时未始终标注
- 具体位置：§6 Discussion, §7 Conclusion, Abstract
- 问题：Abstract 中 "Scheduled sampling compresses the gap to 1.57× with no PPL cost (single seed)" 有标注，但 Conclusion 中 "scheduled sampling (gap ~31×→1.57×, no PPL cost, single seed)" 虽有标注，§1 Introduction 的 contribution (2) 中 "a preliminary demonstration that scheduled sampling compresses this gap from ~31× to 1.57× (single seed)" 也有标注。一致性可以，但 single-seed 结果作为 contribution 的一部分，其可靠性值得质疑。论文已提到第二个 seed 从头训练得到 AR GAR=0.418 (gap 1.20×)，这与 0.318 (gap 1.57×) 差异较大（31%），暗示高 variance。
- 建议：要么移除 scheduled sampling 作为 contribution 的一部分（降级为 Discussion 中的 preliminary observation），要么补充多 seed 验证。

---

## 小问题（不影响接收）

- §5 Analysis, Figure 4 caption: "the gap persists across all five variants (TG, +PCGrad, UG, LoRA-only, Base), the gap persists across all five tested configurations" —— 同一句话内重复同一信息。
- §3.1 中 GAR 的定义同时出现在 Method 的 Preliminaries 和 background.tex（未被 include），LaTeX 结构上无问题但可能是遗留文件。
- Bib 格式：大部分条目一致，但 `grattafiori2024llama3` 使用 `author = {Grattafiori, Aaron and others}`，而其他条目列出完整作者列表。建议统一。
- §4.1 Setup: "approximately 6 hours on a single NVIDIA RTX PRO 6000 Blackwell Server Edition GPU (102 GB)" —— 这一 GPU 型号在 2026 年 5 月时可能尚未广泛可用，建议确认型号名称准确性（可能是 RTX 6000 Ada 或 RTX PRO 6000 Blackwell？）。

---

## 主要优势

1. **实验设计严谨**：五路对比实验中每对配置隔离一个因素，PCGrad exclusion 作为 modus tollens 逻辑推理工具使用得当——这比简单的消融研究更有说服力。
2. **Negative result 诚实且有深度**：论文没有停留在 "gating 不 work" 的表面结论，而是追溯到 exposure bias 的机制，并通过 inference-time steering 提供了 constructive evidence（attention misallocation 而非 representation degradation）。TRC 指标作为 orthogonal probe 增强了论证。
3. **Hedging 适度**："a proximal cause consistent with our evidence" 比之前可能用的 "the root cause" 更准确；Discussion 中 explicitly 列出了 alternative hypotheses（attention drift, KV cache effects, implicit label smoothing）。
4. **Loss formulation 搜索**（Table 2, Appendix B）记录了七次迭代中六次失败，为后续工作节省了探索成本。
5. **跨模型验证**（Llama-3.1-8B）增强了结论的泛化性，尽管覆盖面有限（N=2 model families）。

---

## Questions for Authors

Q1: GAR 在 Dongre et al. (2026) 中的原始全称是 "Goal Accessibility Ratio"。你们使用 "Goal Attention Ratio" 是有意的术语修改还是引用错误？如果是有意的，请解释为什么选择不同的名称。

Q2: Scheduled sampling 的两个 seed 结果差异较大（GAR 0.318 vs 0.418, gap 1.57× vs 1.20×）。作者是否有更多 seed 的初步结果？这一 variance 是否影响对 "exposure bias is the primary driver" 的置信度？

Q3: Inference-time steering (β-steering) 需要 oracle access to goal token positions。在实际部署中如何确定 goal tokens？这与 Rhea 或 split-softmax 等不需要 explicit goal token identification 的方法相比，实用性如何？

Q4: 论文声称 "token-level self-recovery (He et al., 2019) does not extend to auxiliary objectives"。但 He et al. 的 self-recovery 是关于 NTP 的，而 GAR 是一个 distributional property of attention。是否有理论依据说明为什么 self-recovery 应该能 extend 到 attention distributions？如果没有，这一"发现"可能只是在确认一个 trivially expected 的结果。

---

## Missing References

1. **Rhea** (arXiv:2512.06869, Dec 2025): Role-aware Heuristic Episodic Attention，inference-time 方案维持多轮对话中的 instruction fidelity。与本文 §4.3 steering 和 §6 Discussion 直接相关。
2. 建议检查 "Beyond Single-Turn: A Survey on Multi-Turn Interactions with Large Language Models" (arXiv:2504.04717, 2025) 是否覆盖了额外的多轮对话改善方法。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 210 · 2026-05-22T12:55:07.622903+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "project": "turn_residual_gating",
  "reviewer_id": "2",
  "round_number": "1",
  "text": "以下是 Reviewer 1 的完整 Round 1 审稿意见。请逐条回应：对每个 Must-Fix 和 Should-Fix 问题标注 **[AGREE]** 同意并说明理由，或 **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 1 的审稿意见\n\n**Overall**: 3.0 / 5 — Findings\n**一句话总结**: 诊断框架设计精良、负面结果对社区有价值，但核心 AR 评估样本量过小（N=5）、scheduled sampling 单种子可靠性不足、exposure bias 归因缺少替代假说的排除实验，统计支撑尚不足以支撑 conference-level 接收。\n\n### Must-Fix\n\n**N1** [critical] AR 评估样本量过小，核心 claim 缺乏统计检验\n- Table 1 的 AR 列仅基于 N=5 条 10-turn 对话。五个配置的 AR GAR-ours 分别为 0.012, 0.016, 0.015, 0.015, 0.025，这些差异在 N=5 下无法判断是否具有统计显著性。论文未报告 AR GAR 的 confidence interval 或任何条件间的显著性检验。\n- 唯一的多种子验证仅覆盖 ThreadGate（seed 42 vs 123），其余四个条件均为单种子。\n- 建议：AR 评估扩大至 N=50，报告 bootstrap 95% CI，对五个条件做成对检验。\n\n**N2** [critical] Scheduled sampling 双种子结果差异大（GAR 0.318 vs 0.418），abstract 仅引用单种子\n- 两个种子采用不同训练策略（resume vs from scratch），无法分离种子随机性 vs 训练策略效应。\n- 建议：至少 3 个种子采用相同策略，或从 contribution 中移除。\n\n**N3** [critical] Exposure bias 归因未排除替代假说\n- KV cache drift（10-turn 中 KV cache 长度远超 TF 片段）、model-generated text 统计特性差异、GAR-ours 在 AR 下的有效性均未排除。\n- Inference-time steering 论证存在循环性：加 goal token bias 当然增加 goal attention，无论 GAR 低的原因是什么。\n- 建议：设计实验区分 exposure bias 和 KV cache drift，或弱化 claim。\n\n### Should-Fix\n\n**W1** Cross-model 仅 3/5 条件、用 median、N=20、AR/TF 样本量不匹配\n**W2** PCGrad modus tollens 范围过度概括——magnitude imbalance 未排除\n**W3** Instruction retention McNemar p=0.077 不显著但占 Discussion 1/4 篇幅\n**W4** 五路对比存在 LoRA capacity saturation 替代解释——LoRA 已饱和 TF GAR target，gate 自然无增量\n\n### 小问题\n- §1 GAR-ours vs GAR-Dongre 未标注\n- Table 1 caption 缩写位置\n- §5.1 Wilcoxon test 的 pairing 说明\n- §5.5 排除前两 turn 的 justification\n- Gate init 0.82 的依据\n\n---\n\n请逐条回应上述所有 Must-Fix 和 Should-Fix 问题。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "project": "turn_residual_gating",
    "reviewer_id": "2",
    "round_number": "1",
    "text": "以下是 Reviewer 1 的完整 Round 1 审稿意见。请逐条回应：对每个 Must-Fix 和 Should-Fix 问题标注 **[AGREE]** 同意并说明理由，或 **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 1 的审稿意见\n\n**Overall**: 3.0 / 5 — Findings\n**一句话总结**: 诊断框架设计精良、负面结果对社区有价值，但核心 AR 评估样本量过小（N=5）、scheduled sampling 单种子可靠性不足、exposure bias 归因缺少替代假说的排除实验，统计支撑尚不足以支撑 conference-level 接收。\n\n### Must-Fix\n\n**N1** [critical] AR 评估样本量过小，核心 claim 缺乏统计检验\n- Table 1 的 AR 列仅基于 N=5 条 10-turn 对话。五个配置的 AR GAR-ours 分别为 0.012, 0.016, 0.015, 0.015, 0.025，这些差异在 N=5 下无法判断是否具有统计显著性。论文未报告 AR GAR 的 confidence interval 或任何条件间的显著性检验。\n- 唯一的多种子验证仅覆盖 ThreadGate（seed 42 vs 123），其余四个条件均为单种子。\n- 建议：AR 评估扩大至 N=50，报告 bootstrap 95% CI，对五个条件做成对检验。\n\n**N2** [critical] Scheduled sampling 双种子结果差异大（GAR 0.318 vs 0.418），abstract 仅引用单种子\n- 两个种子采用不同训练策略（resume vs from scratch），无法分离种子随机性 vs 训练策略效应。\n- 建议：至少 3 个种子采用相同策略，或从 contribution 中移除。\n\n**N3** [critical] Exposure bias 归因未排除替代假说\n- KV cache drift（10-turn 中 KV cache 长度远超 TF 片段）、model-generated text 统计特性差异、GAR-ours 在 AR 下的有效性均未排除。\n- Inference-time steering 论证存在循环性：加 goal token bias 当然增加 goal attention，无论 GAR 低的原因是什么。\n- 建议：设计实验区分 exposure bias 和 KV cache drift，或弱化 claim。\n\n### Should-Fix\n\n**W1** Cross-model 仅 3/5 条件、用 median、N=20、AR/TF 样本量不匹配\n**W2** PCGrad modus tollens 范围过度概括——magnitude imbalance 未排除\n**W3** Instruction retention McNemar p=0.077 不显著但占 Discussion 1/4 篇幅\n**W4** 五路对比存在 LoRA capacity saturation 替代解释——LoRA 已饱和 TF GAR target，gate 自然无增量\n\n### 小问题\n- §1 GAR-ours vs GAR-Dongre 未标注\n- Table 1 caption 缩写位置\n- §5.1 Wilcoxon test 的 pairing 说明\n- §5.5 排除前两 turn 的 justification\n- Gate init 0.82 的依据\n\n---\n\n请逐条回应上述所有 Must-Fix 和 Should-Fix 问题。"
  }
}
```

</details>

---


### Tool result

_source line 211 · 2026-05-22T12:55:29.871781+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 22248
}
```

</details>

---


### Tool call

_source line 212 · 2026-05-22T12:55:32.231206+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "project": "turn_residual_gating",
  "reviewer_id": "1",
  "round_number": "1",
  "text": "以下是 Reviewer 2 的完整 Round 1 审稿意见。请逐条回应：对每个 Must-Fix 和 Should-Fix 问题标注 **[AGREE]** 同意并说明理由，或 **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 的审稿意见\n\n**Overall**: 3.0 / 5 — Findings\n**一句话总结**: 论文提出了一个有意义的 negative result，诊断链条完整，但核心指标 GAR 的全称引用错误（原文是 Goal Accessibility Ratio，非 Goal Attention Ratio），contribution 包装过度，且写作冗余严重。\n\n### Must-Fix\n\n**N1** [critical] GAR 全称引用错误：原文 Dongre et al. (2026) 定义为 \"Goal Accessibility Ratio\"，本文误写为 \"Goal Attention Ratio\"\n- 通过 arXiv abstract 验证，原文措辞为 \"We introduce the Goal Accessibility Ratio (GAR)\"。\n- \"Attention\" vs \"Accessibility\" 有语义差异——原作者选择 \"Accessibility\" 可能有其考量（accessibility 暗示 information routing 而非单纯 attention weight）。\n- 建议：全文替换为正确全称。\n\n**N2** [critical] 正文疑似超过 8 页限制\n- §6 Discussion 延续到第 9 页约 60%，§7 Conclusion 在第 9 页上半。Conclusion 属于正文，正文约 8.4 页，超出约 0.4 页。\n- EMNLP 2026 严格 8 页限制，ARR 格式检查可能 desk-reject。\n- 建议：压缩 §6 Discussion（instruction retention 移入 appendix）和 §5 Analysis。\n\n### Should-Fix\n\n**W1** \"20–33× gap\" 在六个章节至少出现 8 次，\"0.015–0.025\" 至少 5 次——冗余严重，浪费页面空间\n**W2** Contribution (1) \"systematic diagnostic framework\" 过度包装——实际是消融实验，\"in principle applicable\" 未验证\n**W3** 标题 \"Per-Layer Residual Gating\" 暗示广泛测试，实际仅两种变体（ThreadGate + Uniform Gate）\n**W4** 缺少重要相关工作 Rhea (arXiv:2512.06869, Dec 2025)——inference-time multi-turn attention 方案\n**W5** Contribution (2) \"first empirical characterization\" 风险高——建议改为 \"a detailed\" 或 \"to our knowledge, the first\"\n**W6** Scheduled sampling single-seed 结果作为 contribution 可靠性不足\n\n### 小问题\n- Figure 4 caption 同一句话内重复\n- Bib 格式不一致（grattafiori2024llama3 用 \"and others\"）\n- GPU 型号 \"RTX PRO 6000 Blackwell Server Edition\" 准确性待确认\n\n### Missing References\n1. Rhea (arXiv:2512.06869, Dec 2025)\n2. \"Beyond Single-Turn: A Survey on Multi-Turn Interactions with LLMs\" (arXiv:2504.04717, 2025)\n\n### Questions\nQ1: GAR 名称是有意修改还是引用错误？\nQ2: Scheduled sampling 两种子差异大，是否有更多 seed？\nQ3: β-steering 需要 oracle access to goal tokens，实用性如何？\nQ4: \"token-level self-recovery does not extend to auxiliary objectives\" 是否是 trivially expected 的结果？\n\n---\n\n请逐条回应上述所有 Must-Fix 和 Should-Fix 问题。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "project": "turn_residual_gating",
    "reviewer_id": "1",
    "round_number": "1",
    "text": "以下是 Reviewer 2 的完整 Round 1 审稿意见。请逐条回应：对每个 Must-Fix 和 Should-Fix 问题标注 **[AGREE]** 同意并说明理由，或 **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 的审稿意见\n\n**Overall**: 3.0 / 5 — Findings\n**一句话总结**: 论文提出了一个有意义的 negative result，诊断链条完整，但核心指标 GAR 的全称引用错误（原文是 Goal Accessibility Ratio，非 Goal Attention Ratio），contribution 包装过度，且写作冗余严重。\n\n### Must-Fix\n\n**N1** [critical] GAR 全称引用错误：原文 Dongre et al. (2026) 定义为 \"Goal Accessibility Ratio\"，本文误写为 \"Goal Attention Ratio\"\n- 通过 arXiv abstract 验证，原文措辞为 \"We introduce the Goal Accessibility Ratio (GAR)\"。\n- \"Attention\" vs \"Accessibility\" 有语义差异——原作者选择 \"Accessibility\" 可能有其考量（accessibility 暗示 information routing 而非单纯 attention weight）。\n- 建议：全文替换为正确全称。\n\n**N2** [critical] 正文疑似超过 8 页限制\n- §6 Discussion 延续到第 9 页约 60%，§7 Conclusion 在第 9 页上半。Conclusion 属于正文，正文约 8.4 页，超出约 0.4 页。\n- EMNLP 2026 严格 8 页限制，ARR 格式检查可能 desk-reject。\n- 建议：压缩 §6 Discussion（instruction retention 移入 appendix）和 §5 Analysis。\n\n### Should-Fix\n\n**W1** \"20–33× gap\" 在六个章节至少出现 8 次，\"0.015–0.025\" 至少 5 次——冗余严重，浪费页面空间\n**W2** Contribution (1) \"systematic diagnostic framework\" 过度包装——实际是消融实验，\"in principle applicable\" 未验证\n**W3** 标题 \"Per-Layer Residual Gating\" 暗示广泛测试，实际仅两种变体（ThreadGate + Uniform Gate）\n**W4** 缺少重要相关工作 Rhea (arXiv:2512.06869, Dec 2025)——inference-time multi-turn attention 方案\n**W5** Contribution (2) \"first empirical characterization\" 风险高——建议改为 \"a detailed\" 或 \"to our knowledge, the first\"\n**W6** Scheduled sampling single-seed 结果作为 contribution 可靠性不足\n\n### 小问题\n- Figure 4 caption 同一句话内重复\n- Bib 格式不一致（grattafiori2024llama3 用 \"and others\"）\n- GPU 型号 \"RTX PRO 6000 Blackwell Server Edition\" 准确性待确认\n\n### Missing References\n1. Rhea (arXiv:2512.06869, Dec 2025)\n2. \"Beyond Single-Turn: A Survey on Multi-Turn Interactions with LLMs\" (arXiv:2504.04717, 2025)\n\n### Questions\nQ1: GAR 名称是有意修改还是引用错误？\nQ2: Scheduled sampling 两种子差异大，是否有更多 seed？\nQ3: β-steering 需要 oracle access to goal tokens，实用性如何？\nQ4: \"token-level self-recovery does not extend to auxiliary objectives\" 是否是 trivially expected 的结果？\n\n---\n\n请逐条回应上述所有 Must-Fix 和 Should-Fix 问题。"
  }
}
```

</details>

---


### Tool result

_source line 213 · 2026-05-22T12:55:33.743620+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1512
}
```

</details>

---


### Assistant

_source line 214 · 2026-05-22T12:55:41.648793+00:00_

交叉分享已发送。等待两位 Reviewer 的逐条回应。

**当前进度**：
- Round 1 初审 ✅（R1: 3.0, R2: 3.0，均为 Findings）
- 交叉分享 ✅（已发送）
- 视觉审查：进行中
- 外部审稿：未配置，不适用
- 等待：两位 Reviewer 的交叉回应

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director"
}
```

</details>

---


## Round 16

## Round 16

2 recorded events


### User

_source line 215 · 2026-05-22T12:55:44.287970+00:00_

[Reviewer 2 审稿结果]:
审稿报告已提交给 Review Director。

核心发现总结：

- **Overall: 3.0 (Findings)**
- **2 个 Must-Fix**：GAR 全称引用错误（原文是 "Goal Accessibility Ratio" 而非 "Goal Attention Ratio"，已通过 arXiv 原文验证），以及正文疑似超 8 页限制
- **6 个 Should-Fix**：数字冗余（"20–33×" 出现 8+ 次）、contribution 包装过度（"framework"/"first"）、标题 scope 过宽、缺少 Rhea (2025) 引用、scheduled sampling single-seed 结果可靠性
- **优势**：五路消融设计严谨、negative result 诚实有深度、hedging 措辞得当、loss 搜索历程有参考价值

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 216 · 2026-05-22T12:55:49.136035+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director"
}
```

</details>

---


## Round 17

## Round 17

2 recorded events


### User

_source line 217 · 2026-05-22T12:56:52.267745+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 对 Reviewer 1 Round 1 意见的交叉回应

---

### Must-Fix

**[AGREE] R1-N1: AR 评估样本量过小（N=5）**
同意这是一个需要解决的问题，但程度判断有细微分歧。

核心 TF-AR gap（0.50 vs 0.015–0.025，即 20–33×）跨越一个数量级以上，即使 N=5 也不可能是随机波动——这一点与 seed 42/123 双种子结果一致（§4.2: gap 30.5–32.1×, TF GAR-ours 0.504±0.001, AR 0.016±0.001）。因此 R1 的批评不应被理解为"gap 本身可能不存在"，而是"五个配置之间 AR GAR 的差异（0.012–0.025）在 N=5 下无法做统计区分"。

具体而言：LoRA-only 的 AR GAR=0.025 看似高于 ThreadGate 的 0.016，但在 N=5 下这一差异无法判断是否有意义。论文的核心 claim 是"所有配置的 AR GAR 都 collapse 到同一水平"，但 N=5 下"同一水平"缺乏统计支撑。

注意论文在 §4.3 steering 实验中已有 N=50 评估（39 条 ≥3 turns），且 §5.5 cross-model 有 N=20。扩大 Table 1 AR 评估至 N≥30 并补充 CI 是可行的，且能显著增强 "all variants collapse equally" 这一 claim 的说服力。

建议定级维持 **critical**，但修复方式建议更精确：补充 N≥30 AR 评估 + bootstrap CI，核心是验证"五个配置间 AR GAR 无显著差异"。

---

**[AGREE] R1-N2: Scheduled sampling 双种子差异大，abstract 仅引 single seed**
完全同意。这与我的 W6 一致。

两个种子不仅结果差异大（GAR 0.318 vs 0.418，gap 1.57× vs 1.20×），而且训练策略不同（resume vs from scratch），如 §6 Discussion 所述："A second seed trained from scratch (rather than resumed from a standard-trained epoch) yields AR GAR=0.418"。这使得无法分离 seed variance 和 training strategy effect。

更关键的是：scheduled sampling 被列为 contribution (2) 的一部分（§1: "a preliminary demonstration that scheduled sampling compresses this gap from ~31× to 1.57× (single seed)"），这对一个 preliminary single-seed 结果赋予了过高的 contribution 地位。

建议修复：要么从 contribution 列表中移除 scheduled sampling（降级为 Discussion 中的 exploratory observation），要么补充 ≥3 个使用相同策略的种子。当前写法中 "preliminary" 一词存在但不够显著。

---

**[REBUT] R1-N3: Exposure bias 归因未排除替代假说——部分同意，但 critical 定级过高**

R1 提出三个替代假说（KV cache drift、model-generated text 统计差异、GAR-ours 在 AR 下的有效性）并指出 steering 论证存在循环性。我逐一评估：

**(a) KV cache drift**: 合理的替代假说，但论文在 §5.4 (Mechanism Specificity) 提供了部分排除证据。TRC（Turn-level Residual Coherence）在 TF 和 AR 下几乎相同（ThreadGate: 0.334 vs 0.332; LoRA-only: 0.349 vs 0.411）。如果 KV cache drift 导致广泛的 representation degradation，TRC 应该显示 comparable gap，但实际没有。这不完全排除 KV cache drift 影响 attention routing 的可能，但确实缩小了替代假说的空间。

**(b) Steering 论证的循环性**: R1 的批评有道理——"加 goal token bias 增加 goal attention"本身是 tautological。但论文的 inference 不仅是"GAR 增加了"，而是"GAR 增加的同时 hidden states 的 coherence 未变（TRC stable）且 PPL 仅增加 9%（β=3）"。这组合证据表明 attention misallocation 是独立于 representation quality 的 failure mode。如果 root cause 是 representation degradation 而非 attention routing，β-steering 应该无法恢复 meaningful GAR（因为 hidden states 中没有 goal information 可 route），但实际恢复了 11× (§4.3)。

**(c) 论文的 hedging**: 论文确实使用了 "a proximal cause consistent with our evidence"（§4.3, §7 Conclusion），§6 Discussion 明确列出了 alternative hypotheses："progressive attention drift unrelated to exposure bias, KV cache accumulation effects at long context lengths, or implicit label smoothing from the auxiliary loss could each contribute"。这一 hedging 水平在我看来是适度的。

**我的判断**：R1 的批评核心合理——exposure bias 归因确实不是 conclusive 的。但论文已经做了合理的 hedging，且 TRC + steering 组合提供了 non-trivial evidence。将此定为 **critical** 过高；建议降级为 **should-fix**，具体修复方向是：(1) 在 §5.3 或 §6 中加一段明确讨论 KV cache drift 作为 confound（当前仅在 Discussion 中一句带过），(2) 承认 steering 论证在逻辑上不排除 KV cache drift。但不需要额外的实验来排除每个替代假说——negative result paper 的标准不应等同于 causal inference paper。

---

### Should-Fix

**[AGREE] R1-W1: Cross-model 验证不充分（3/5 条件、median、N=20）**
同意。§5.5 仅覆盖 ThreadGate、LoRA-only、Base 三个条件，缺少 +PCGrad 和 Uniform Gate。使用 median 而非 mean 有合理理由（heavy-tailed distributions，§5.5 已说明），但 N=20 偏小，且 AR/TF 样本量不对称（TF N=50 vs AR N=20）降低了 gap 估计的可比性。

补充：论文对此有部分 acknowledgment（§8 Limitations: "the full five-way ablation (Uniform Gate, +PCGrad) has not been replicated"），但不够显著。建议在 §5.5 正文中也明确标注这一局限。

---

**[AGREE] R1-W2: PCGrad modus tollens scope 过度概括**
同意。论文在 §5.2 正文中确实写了 "magnitude imbalance (Chen et al., 2018) and Nash equilibrium violations (Navon et al., 2022) remain untested"，在 §8 Limitations 中也重复了这一点。但 §1 Introduction 的 contribution (1) 中描述为 "PCGrad-based exclusion via gradient surgery" 时未加限定词，读者可能误以为排除了所有 gradient conflict，而实际只排除了 directional conflict。

建议在 §1 contribution (1) 中加入 "directional" 修饰：改 "gradient conflict" 为 "gradient direction conflict"。

---

**[AGREE] R1-W3: Instruction retention McNemar p=0.077 不显著但占 Discussion 过多篇幅**
同意。p=0.077 未达常规显著性阈值（0.05），但 §6 Discussion 中 "Instruction retention under steering" 段落占据了约 3-4 行（不算很长），且包含 GAR-compliance correlation（r=0.200, p=0.007）。

但考虑到论文已面临页数超限问题（我的 N2），这段内容是压缩的首选候选。建议将 instruction retention 分析移入 appendix，或压缩为一句提及（"exploratory analysis suggests downstream compliance benefit, details in Appendix X"）。这同时帮助解决页数问题。

---

**[REBUT] R1-W4: LoRA capacity saturation 替代解释**
部分不同意。

R1 的论点是：如果 LoRA 已经饱和了 TF GAR target（0.50），gates 自然无法提供增量，因此 "gating 无用" 的结论可能是 capacity ceiling artifact。

这个 concern 对 "gating 无用" 的 claim 是有效的，但**不影响论文的核心结论**。论文的主要 finding 不是"gating 不 work"，而是"所有 training-time interventions（包括 LoRA-only）在 TF 下 work 但在 AR 下 collapse"——即 TF-AR gap。即使 LoRA 确实在 TF 下饱和了 GAR target，这不解释为什么 AR GAR 从 0.50 跌到 0.015–0.025。

具体证据：
1. LoRA-only（无 gate）的 TF GAR=0.50，AR GAR=0.025——gap 同样存在（Table 1）
2. Base model 的 AR GAR=0.012 vs LoRA-only 的 0.025——fine-tuning 本身对 AR 的改善微乎其微
3. Inference-time steering（§4.3）在不改变任何训练参数的情况下将 AR GAR 从 0.064 恢复到 0.727

这些证据表明 failure mode 在 TF→AR transition，而非 training capacity。R1 的 concern 更适用于 "gating vs LoRA-only 对比" 的解读，而非论文的 central claim。

建议将此定为 **minor**：在 §4.2 或 §6 中加一句 acknowledge 这一 alternative interpretation（"The convergence of all fine-tuned variants at TF GAR ≈ 0.50 could partly reflect LoRA capacity saturation rather than gating ineffectiveness per se; however, the TF-AR gap—the paper's central finding—persists regardless of this interpretation"）。

---

### 总结

| R1 Issue | R2 判断 | 理由 |
|----------|---------|------|
| N1 AR N=5 | [AGREE] critical | 核心 claim "all collapse equally" 缺统计支撑 |
| N2 SS dual-seed | [AGREE] critical | 与我的 W6 一致；contribution 中应降级 |
| N3 Exposure bias | [REBUT] 降为 should-fix | 论文 hedging 适度，TRC+steering 提供了 non-trivial evidence，但应加强 KV cache drift 讨论 |
| W1 Cross-model | [AGREE] | 覆盖不完整，应在正文中标注 |
| W2 PCGrad scope | [AGREE] | §1 contribution 措辞需加 "directional" |
| W3 Instruction retention | [AGREE] | 不显著结果占过多篇幅，建议移入 appendix |
| W4 LoRA saturation | [REBUT] 降为 minor | 不影响核心 TF-AR gap claim |

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 218 · 2026-05-22T12:56:56.956326+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director"
}
```

</details>

---


## Round 18

## Round 18

2 recorded events


### User

_source line 219 · 2026-05-22T12:57:01.926153+00:00_

[Reviewer 2 审稿结果]:
交叉回应已提交给 Review Director。

总结：对 R1 的 3 个 Must-Fix 中，N1（AR N=5）和 N2（scheduled sampling 单种子）我同意维持 critical；N3（exposure bias 归因）我认为应降级为 should-fix——论文的 hedging 和 TRC+steering 组合证据提供了 non-trivial support，但需加强 KV cache drift 的讨论。4 个 Should-Fix 中同意 W1-W3，对 W4（LoRA saturation）反驳降为 minor，因为它不影响论文的核心 TF-AR gap 结论。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 220 · 2026-05-22T12:59:09.175059+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director"
}
```

</details>

---


## Round 19

## Round 19

10 recorded events


### User

_source line 221 · 2026-05-22T12:59:09.186711+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 对 Reviewer 2 Round 1 意见的逐条回应

---

### Must-Fix

**[AGREE] R2-N1: GAR 全称引用错误**

同意这是需要修正的引用错误。如果 Dongre et al. (2026) 原文定义为 "Goal Accessibility Ratio"，则论文中 §3.1（Eq. 1-2）、§1 Introduction、Abstract 等所有出现 "Goal Attention Ratio" 的地方均应修正。R2 指出的语义差异也有道理——"Accessibility" 强调信息的可达性（与论文引用的 AUC=0.98 linear probe 结果一致，即 information 是 accessible 的），而 "Attention" 缩窄到了注意力权重这一具体机制。不过，论文自定义的 GAR-ours 变体（Eq. 2）确实专注于 attention weight，作者可以考虑在修正原始定义全称的同时，说明自己的变体为何聚焦 attention。

**[AGREE] R2-N2: 正文疑似超过 8 页限制**

同意。从 PDF 渲染来看，§6 Discussion 延续到第 9 页，§7 Conclusion 也在第 9 页上半部分。即使 §8 Limitations 不计入页数，Discussion 和 Conclusion 属于正文，超出了 EMNLP 2026 的 8 页严格限制。ARR 格式检查阶段这一问题可能导致 desk-reject。

R2 提出的压缩方案合理：§6 中 instruction retention 段落（McNemar p=0.077, r=0.200）统计上不显著（我在 R1-W3 中也提出了同样的问题），移入 Appendix 可节省约 0.3 页。此外，§5 Analysis 中部分冗余表述（见 W1）也可压缩。

---

### Should-Fix

**[AGREE] R2-W1: "20–33× gap" 和 "0.015–0.025" 冗余过多**

同意。论文的诊断链结构（§4 → §5 → §6）确实需要在各节之间建立连贯性，适度回溯核心数字是合理的。但在 abstract、§1 contributions、§4.2、§5.3、§5.5、§6、§7 中重复出现 8+ 次确实过度。在页面空间紧张（见 N2 超页问题）的情况下，削减冗余复述是低成本高收益的改进。建议保留首次出现（§4.2 Table 1）和 conclusion 中的总结性引用，中间各节改用 "the TF-AR gap (Table 1)" 等简洁回指。

**[REBUT] R2-W2: "Systematic diagnostic framework" 过度包装**

部分不同意。R2 将其等同于 "就是消融实验"，我认为低估了实验设计的结构性。普通消融实验逐一去除组件观察性能变化；本文的五路对比不仅做了消融（ThreadGate vs Uniform Gate vs LoRA-only），还包含了 PCGrad exclusion 作为因果排除工具（§5.2 的 modus tollens 论证），以及 TRC（§5.4）作为正交验证。这种 "排除法 + 正交验证" 的组合在方法论上超出了标准消融。

但 R2 指出 "in principle applicable 未验证" 是合理的——论文没有在其他 auxiliary loss 或其他任务上测试该框架的迁移性。建议 (1) 保留 "diagnostic framework" 但删除 "systematic"，(2) 明确说明当前仅在 GAR-family losses 上验证。这是一个措辞调整而非实质性问题。

**[REBUT] R2-W3: 标题暗示广泛测试，实际仅两种变体**

不同意。标题 "Why Per-Layer Residual Gating Fails to Fix Multi-Turn Attention Degradation" 描述的是一个具体的失败机制分析，而非声称穷举了所有可能的 gating 方案。论文实际测试了三种 gate-related 条件：ThreadGate（content + turn conditioned）、Uniform Gate（content-only, turn-unaware）、LoRA-only（gate 固定为 1.0, 即无 gating）——这覆盖了 gating 的 presence/absence 和 turn conditioning 两个维度。

更重要的是，论文的核心论点不是 "所有 gating 都不行"，而是 "在 GAR auxiliary loss + teacher-forcing 训练范式下，gating 无法克服 exposure bias"——这是一个关于训练范式的结论，而非关于 gating 架构的穷举性结论。标题中的 "Per-Layer Residual Gating" 准确描述了所测试的具体方法类型。如果标题改为更宽泛的 "Residual Gating" 反而会过度泛化。

**[AGREE] R2-W4: 缺少 Rhea (arXiv:2512.06869)**

无法独立验证该引用的真实性（作为 reviewer 我不应检索论文之外的材料来验证引用），但如果该工作确实提出了 inference-time multi-turn attention 方案，则与本文的 §4.3 inference-time steering 直接相关，应在 §2 Related Work 的 "Attention manipulation" 段落中讨论。建议作者查证并引用。

R2 提到的另一篇 survey "Beyond Single-Turn" (arXiv:2504.04717) 相关性较弱——survey 类文献引用为可选而非必须。

**[AGREE] R2-W5: "First empirical characterization" 风险高**

同意。"First" claim 在学术写作中是高风险表述，审稿人和 AC 往往会因为未能确认优先性而扣分。改为 "to our knowledge, the first" 或 "a detailed" 是低成本的安全改进，不影响 contribution 的实质。论文 §1 contributions (2) 中的原文应修改。

**[AGREE] R2-W6: Scheduled sampling single-seed 作为 contribution 可靠性不足**

强烈同意。这与我的 R1-N2（Must-Fix）完全一致。两个种子（GAR 0.318 vs 0.418，gap 1.57× vs 1.20×）的差异已经说明了高方差。在 abstract 和 contributions 中以 "compresses the gap to 1.57×" 呈现单种子结果，给读者过高的确定性印象。必须 (1) 增加种子数量，或 (2) 在所有提及处明确标注 "preliminary, single-seed"，或 (3) 从 contribution list 中降级。

---

### R2 Questions 的补充意见

**Q4: "token-level self-recovery does not extend to auxiliary objectives" 是否 trivially expected？**

这是一个值得讨论的问题。He et al. (2019) 的 token-level self-recovery 是关于 primary objective (NTP) 的，auxiliary loss 不具备相同的 self-correction mechanism 可以说是 "事后看来显然" 的。但论文的贡献不在于预测了这一点，而在于 empirically 量化了 primary vs auxiliary objective 在 exposure bias 下的不同表现（Table 1 中 PPL 不变但 GAR 崩溃）。如果这个结果是 trivially expected，那么同样可以说所有 negative result 都是 "事后看来显然" 的。关键是论文是否提供了超越直觉的定量证据和机制理解——我认为诊断链（§5.1-5.4）提供了这一点，尽管统计支撑需加强（R1-N1）。

---

[Reviewer 1 审稿结果]:
Round 1 交叉回应已提交给 Review Director。

总结：对 R2 的 2 个 Must-Fix 全部 **[AGREE]**（GAR 全称错误、超页问题均属实）；6 个 Should-Fix 中 4 个 **[AGREE]**（冗余、缺引用、first claim 风险、scheduled sampling 可靠性），2 个 **[REBUT]**（diagnostic framework 不等同于普通消融、标题范围与论文 claim 匹配）。对 Q4 补充了 "negative result 的价值不在于是否 trivially expected" 的观点。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 222 · 2026-05-22T12:59:40.786581+00:00_

called mcp__agent-ml-research__get_visual_check_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_visual_check_status</summary>

```json
{
  "project": "turn_residual_gating"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "tool_args": {
    "project": "turn_residual_gating"
  }
}
```

</details>

---


### Tool result

_source line 223 · 2026-05-22T12:59:40.938986+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"done\", \"started_at\": \"2026-05-22T12:48:19.756767+00:00\", \"completed_at\": \"2026-05-22T12:50:53.715031+00:00\", \"findings\": [{\"severity\": \"info\", \"dimension\": \"page 1\", \"message\": \"首页无 display item（纯 Abstract + Introduction 文字）。第一个视觉锚点 Figure 1 在第 2 页顶部出现，属可接受范围，但若能在第 1 页底部放一个 teaser 或将 Figure 1 提前，审稿人第一印象更佳\"}, {\"severity\": \"info\", \"dimension\": \"page 2\", \"message\": \"Figure 1 全宽概念图（Observation → Intervention → Result & Root Cause）信息传达清晰，caption 自包含，颜色（绿/橙/蓝）区分度好。图内部分小字（如 \\\"Natural hypothesis\\\" 标注、数学公式 $x_l = x_l + g_l \\\\cdot f_l(x_l)$）字号偏小，建议放大至正文字号的 80% 以上\"}, {\"severity\": \"warning\", \"dimension\": \"page 3\", \"message\": \"纯文本页（Related Work），与第 4 页（Method 正文 + 公式，无 figure/table）合计形成连续 2 页无 figure/table 的文字密集区。第 4 页有 5 个公式提供视觉节奏，但审稿人快速翻页时仍感知为\\\"文字墙\\\"\"}, {\"severity\": \"info\", \"dimension\": \"page 4\", \"message\": \"公式 (1)-(5) 渲染正确，排版整洁。Section heading \\\"3 Method\\\" 位置合理，后有充足正文\"}, {\"severity\": \"info\", \"dimension\": \"page 5\", \"message\": \"Figure 2（单栏折线图）字号偏小——axis label 和 legend 文字约为正文字号的 60-65%，建议增大。图表本身信息传达清晰（per-turn GAR 趋势 + error bars）\"}, {\"severity\": \"info\", \"dimension\": \"page 5-6\", \"message\": \"Table 1 为全宽表，使用 booktabs 风格（toprule/midrule/bottomrule），最优值加粗标注，格式规范。小数精度统一（2-3 位）\"}, {\"severity\": \"info\", \"dimension\": \"page 6\", \"message\": \"Figure 3 双面板（a: N=5, b: N=30）清晰可读。带 error bars 和虚线 baseline 参照。Section 5 Analysis 起始位置合理\"}, {\"severity\": \"warning\", \"dimension\": \"page 7\", \"message\": \"Figure 4 和 Figure 5 同页，display item 密度高。Figure 5 有 4 个子面板，每个面板的 axis label 和 legend 字号非常小（约正文 55-60%），审稿人在屏幕上阅读可能需要放大才能看清。建议：(1) 增大 Figure 5 字号，或 (2) 将 Figure 5 改为全宽 figure* 以获得更多空间\"}, {\"severity\": \"warning\", \"dimension\": \"page 8\", \"message\": \"纯文本页（Discussion 正文），与第 9 页上半部（Conclusion + Limitations）合计形成连续约 1.5 页无 display item 的区域。Discussion 章节通常如此，但若能在 Discussion 中加入一个总结性表格或示意图会改善视觉节奏\"}, {\"severity\": \"info\", \"dimens
…[truncated 1154 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 152
}
```

</details>

---


### Tool call

_source line 224 · 2026-05-22T12:59:40.939478+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "turn_residual_gating"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "turn_residual_gating"
  }
}
```

</details>

---


### Tool result

_source line 225 · 2026-05-22T12:59:41.043582+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 104
}
```

</details>

---


### Tool call

_source line 226 · 2026-05-22T13:05:55.418123+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "turn_residual_gating",
  "issues_yaml": "# Review Issues Tracker — turn_residual_gating\n# Round 1 (2026-05-19, dream_20260519T145320)\n# Round 2 (2026-05-22, fresh re-review of revised paper)\n# Round 3 (2026-05-22, fresh re-review — current round)\n\n# ============================================================\n# Issues from Round 1 — status updates through Round 3\n# ============================================================\n\n- id: \"R1-N1\"\n  summary: \"所有引用渲染为 '?'——bibliography 编译失败\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"Dream paper artifact。\"\n    - round: 2\n      reviewers: []\n      note: \"视觉审查确认无 [?] 未解析引用。已修复。\"\n    - round: 3\n      reviewers: []\n      note: \"Round 3 视觉审查确认无未解析引用。维持 resolved。\"\n  action_items:\n    - round: 1\n      action: \"Paper Agent 确保 bibtex 编译正确\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"Round 2 视觉审查确认已修复。\"\n  resolution_round: 2\n\n- id: \"R1-N2\"\n  summary: \"单种子支撑结论——统计功效不足\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 3\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"Bootstrap CI 仅覆盖 eval variance，不覆盖 training variance。\"\n    - round: 2\n      reviewers: [1, 2]\n      note: \"ThreadGate 已补 seed=123，但其余 4/5 条件仍为单 seed。SS 仅 1 seed 且第二 seed 协议不同不可比。两位 Reviewer 独立列为 Critical。\"\n    - round: 3\n      reviewers: [1, 2]\n      note: \"Round 3 两位 Reviewer 再次独立列为 Critical。R1-N1 指出 AR 评估仅 N=5，核心 claim 'all variants collapse equally' 缺统计检验。R1-N2 指出 SS 双种子差异大（GAR 0.318 vs 0.418）且策略不同。两项均为 Must-Fix。\"\n  action_items:\n    - round: 1\n      action: \"plan_019: seed=123 extra training\"\n      assigned_to: agent\n      status: done\n    - round: 2\n      action: \"D048: 5 条件 × 3 seeds from-scratch (Base/TG/LO/UG/SS)，SS 最高优先级。~45h GPU。\"\n      assigned_to: agent\n      status: in_progress\n    - round: 3\n      action: \"AR 评估扩大至 N≥30 + bootstrap 95% CI + 条件间成对检验\"\n      assigned_to: agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-N3\"\n  summary: \"评估样本量过小\"\n  category: experiment\n  severity: info\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1]\n      note: \"Cohen's d≈0.22 在 n=50 下 power 不足。\"\n    - round: 2\n      reviewers: []\n      note: \"Round 2 使用 N=50 held-out + N=50 steering + N=20 Llama。未再被提出。\"\n    - round: 3\n      reviewers: []\n      note: \"TF 评估样本量已充分。但 AR 评估 N=5 问题在 R1-N2 中追踪。\"\n  action_items: []\n  resolution: \"N=50 评估已在论文中体现。AR N=5 问题移至 R1-N2 追踪。\"\n  resolution_round: 2\n\n- id: \"R1-N4\"\n  summary: \"损失函数超参数和 v1-v6 配置定义缺失\"\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"v1-v7 配置仅报告 v7。\"\n    - round: 2\n      reviewers: []\n      note: \"§3.3 报告 λ_GAR=λ_div=1.0。Appendix Table 2 列出 v1-v7。未再被提出。\"\n  action_items: []\n  resolution: \"§3.3 + Appendix B Table 2 已提供完整信息。\"\n  resolution_round: 2\n\n- id: \"R1-W1\"\n  summary: \"Llama 跨模型消融不完整（缺 PCGrad + Uniform Gate）\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 3\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"边际信息量不值 6h GPU。\"\n    - round: 2\n      reviewers: [1, 2]\n      note: \"仍仅 3/5 条件，N=20，用 median。两位 Reviewer 再次指出。\"\n    - round: 3\n      reviewers: [1, 2]\n      note: \"Round 3 两位 Reviewer 再次指出。额外问题：使用 median 而非 mean 但未报告 mean 对照；AR/TF 样本量不匹配（TF N=50 vs AR N=20）；attention spikes 成因未解释。\"\n  action_items:\n    - round: 2\n      action: \"D048: 补充 Llama PCGrad+UG 训练+评估，完成 5-way 跨模型对比。~14h GPU。\"\n      assigned_to: agent\n      status: in_progress\n    - round: 3\n      action: \"报告 mean+median 双指标，展示 AR GAR 完整分布（boxplot），解释 attention spikes 成因\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-W2\"\n  summary: \"无 λ_GAR 敏感性消融\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - round: 1\n      reviewers: [1]\n      note: \"梯度冲突取决于 λ_GAR。\"\n    - round: 2\n      reviewers: []\n      note: \"§3.3 报告 λ=1.0 但仍无敏感性分析。未被 Round 2 reviewer 独立提出为 must-fix。\"\n    - round: 3\n      reviewers: []\n      note: \"Round 3 未被提及。可能因论文核心 claim 转向 exposure bias 而非 loss 配置，优先级降低。待 Research Director 确认。\"\n  action_items:\n    - round: 1\n      action: \"plan_022: λ_GAR=10 敏感性测试\"\n      assigned_to: agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-W3\"\n  summary: \"训练数据量混淆变量\"\n  category: experiment\n  severity: info\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1]\n      note: \"1,000 convs 偏少。\"\n    - round: 2\n      reviewers: []\n      note: \"Round 2 使用 8K conversations。\"\n  action_items: []\n  resolution: \"训练数据量增加至 8K。\"\n  resolution_round: 2\n\n- id: \"R1-W4\"\n  summary: \"全文零 figure\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"Dream paper artifact.\"\n    - round: 2\n      reviewers: []\n      note: \"Round 2 有 5 figures + 2 tables。\"\n  action_items: []\n  resolution: \"Figure 1-5 + Table 1-2 已就位。\"\n  resolution_round: 2\n\n- id: \"R1-W5\"\n  summary: \"Scheduled sampling 统计支撑不足\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 3\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"单 seed，单 ratio，PPL 未报告。\"\n    - round: 2\n      reviewers: [1, 2]\n      note: \"PPL 已报告，但仍单 seed，第二 seed 协议不同不可比。\"\n    - round: 3\n      reviewers: [1, 2]\n      note: \"Round 3 两位 Reviewer 再次独立列为 Must-Fix/Critical。双种子差异大（GAR 0.318 vs 0.418, gap 1.57× vs 1.20×）且策略不同（resume vs from scratch）。Abstract 仅引用 seed 1。两位 Reviewer 建议从 contribution 降级或补充 ≥3 同策略种子。\"\n  action_items:\n    - round: 2\n      action: \"D048: SS 3-seed from-scratch 作为 multi-seed 最高优先级条件\"\n      assigned_to: agent\n      status: in_progress\n    - round: 3\n      action: \"从 contribution 列表降级为 Discussion preliminary observation，或补充 ≥3 同策略种子后恢复\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-W6\"\n  summary: \"Reverse turn conditioning 证据间接\"\n  category: experiment\n  severity: info\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1]\n      note: \"差异可能是噪声。\"\n  resolution: \"Wilcoxon p=3.73e-8, r=0.975。已在 §5.1 报告。\"\n  resolution_round: 2\n\n# ============================================================\n# Issues from Round 2\n# ============================================================\n\n- id: \"R2-N1\"\n  summary: \"Novelty/causal 声称过高——'causal diagnostic framework' 过度包装\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 3\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"'first quantitative measurement' overclaim。\"\n    - round: 2\n      reviewers: [1, 2]\n      note: \"Round 1 overclaim 已降级，但 Round 2 发现新 overclaim：Contribution (1) 'systematic causal diagnostic framework' 实际是消融。\"\n    - round: 3\n      reviewers: [1, 2]\n      note: \"Round 3 R2 再次指出 contribution (1) 'systematic diagnostic framework' 过度包装 + 'in principle applicable' 未验证。R1 部分反驳（认为超出标准消融），但同意删除泛化声称。R2 还指出 'first empirical characterization' 风险高。两位 Reviewer 共识：删除 'in principle applicable'，'first' → 'to our knowledge, the first'。\"\n  action_items:\n    - round: 1\n      action: \"'first quantitative measurement' 降级\"\n      assigned_to: director\n      status: done\n    - round: 2\n      action: \"D048: 'causal' → 'systematic diagnostic/ablation'；限定 PCGrad scope\"\n      assigned_to: paper_agent\n      status: in_progress\n    - round: 3\n      action: \"删除 'in principle applicable to other auxiliary objective analyses'；'first empirical characterization' → 'to our knowledge, the first' 或 'a detailed'\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-N2\"\n  summary: \"标题过度声称\"\n  category: framing\n  severity: info\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 3\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"'Cannot Fix' → 已改为 'Fails to Fix'。\"\n    - round: 2\n      reviewers: [1, 2]\n      note: \"'Lightweight Gating' 暗示一类方法但仅测试 ThreadGate。\"\n    - round: 3\n      reviewers: [2]\n      note: \"R2 认为 'Per-Layer Residual Gating' 暗示广泛测试但仅两种变体。R1 反驳：标题准确描述所测试方法，核心结论关于训练范式非 gating 穷举。Director 裁定：当前标题可接受。\"\n  action_items:\n    - round: 2\n      action: \"D048: 标题改为更精确表述\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"Round 3 Director 裁定当前标题可接受——R1 反驳有理，标题描述的是具体测试方法类型而非穷举声称。\"\n  resolution_round: 3\n\n- id: \"R2-N3\"\n  summary: \"Dongre et al. (2026) GAR 全称引用错误\"\n  category: format\n  severity: critical\n  status: open\n  first_raised_round: 1\n  last_seen_round: 3\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"论文动机链依赖此引用。\"\n    - round: 2\n      reviewers: [2]\n      note: \"R2 指出 Dongre 原文为 'Goal Accessibility Ratio'，本文写为 'Goal Attention Ratio'。\"\n    - round: 3\n      reviewers: [1, 2]\n      note: \"Round 3 R2 通过 arXiv 原文验证确认为 'Goal Accessibility Ratio (GAR)'。R1 完全同意。两位 Reviewer 共识列为 Critical Must-Fix。语义差异：'Accessibility' 强调信息可达性，'Attention' 缩窄到注意力权重。\"\n  action_items:\n    - round: 2\n      action: \"D048: 确认 Dongre 原文全称并更正\"\n      assigned_to: paper_agent\n      status: in_progress\n    - round: 3\n      action: \"全文替换 'Goal Attention Ratio' → 'Goal Accessibility Ratio'。可保留说明 GAR-ours 变体聚焦 attention weight。\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-N4\"\n  summary: \"Related Work 缺失 gradient conflict 文献 + PCGrad baseline\"\n  category: framing\n  severity: info\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"如果 PCGrad 能解决梯度竞争，论文核心结论悬空。\"\n    - round: 2\n      reviewers: []\n      note: \"PCGrad 已纳入五路对比，§2 已覆盖 gradient conflict 文献。\"\n  action_items: []\n  resolution: \"PCGrad 已纳入五路对比 + Related Work 已覆盖。\"\n  resolution_round: 2\n\n- id: \"R2-C3\"\n  summary: \"Exposure bias 归因存在未排除的替代解释\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 2\n  last_seen_round: 3\n  mentions:\n    - round: 2\n      reviewers: [1, 2]\n      note: \"β-steering 不等于 exposure bias 是原因（循环论证）；SS 改变多个训练动态；KV cache 差异未排除。\"\n    - round: 3\n      reviewers: [1, 2]\n      note: \"R1 列为 Critical（KV cache drift/text statistics/GAR-ours 有效性未排除，steering 循环性）。R2 降为 Should-Fix（论文 hedging 适度，TRC+steering 组合提供 non-trivial evidence）。Director 裁定 Should-Fix：不要求额外排除实验，但需加强 KV cache drift 讨论。\"\n  action_items:\n    - round: 2\n      action: \"D048: 'the proximal cause' → 'a proximal cause consistent with evidence'；Discussion 讨论替代假说\"\n      assigned_to: paper_agent\n      status: in_progress\n    - round: 3\n      action: \"在 §5.3 或 §6 加一段明确讨论 KV cache drift 作为 confound；承认 steering 论证循环性风险\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-W3\"\n  summary: \"GAR 单指标依赖——缺乏下游任务验证\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 3\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"r=0.82 sanity check 不足以作为 gold-standard proxy。\"\n    - round: 2\n      reviewers: [1, 2]\n      note: \"§6 instruction retention 分析 McNemar p=0.077 不显著，r=0.200 极弱。\"\n    - round: 3\n      reviewers: [1, 2]\n      note: \"Round 3 两位 Reviewer 均指出 instruction retention 不显著但占 Discussion 过多篇幅。建议移入 Appendix（也有助于解决超页问题）。\"\n  action_items:\n    - round: 2\n      action: \"D048: N=200 扩容指令保持实验\"\n      assigned_to: agent\n      status: in_progress\n    - round: 3\n      action: \"Instruction retention 段落移入 Appendix 或压缩至一句\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-W5\"\n  summary: \"liu2016attention 引用可能错配\"\n  category: format\n  severity: warning\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [2]\n      note: \"语音识别 vs 注意力引导。\"\n    - round: 2\n      reviewers: []\n      note: \"Round 2 未提及，待确认。\"\n    - round: 3\n      reviewers: []\n      note: \"Round 3 未提及。可能已修复或不在当前版本中。待 Research Director 确认。\"\n  action_items:\n    - round: 2\n      action: \"Paper Agent 确认引用准确性\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-W6\"\n  summary: \"Bib 格式不一致 + orphan 条目\"\n  category: format\n  severity: info\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 3\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"vaswani2017, elhage2021, olsson2022, efron1994。\"\n    - round: 2\n      reviewers: [2]\n      note: \"部分用 'and others' 部分列完整作者，格式不一致。\"\n    - round: 3\n      reviewers: [2]\n      note: \"grattafiori2024llama3 使用 'and others'，其他条目列完整作者列表。格式不一致仍存在。\"\n  action_items:\n    - round: 2\n      action: \"统一 bib 格式，清理 orphan 条目\"\n      assigned_to: paper_agent\n      status: in_progress\n    - round: 3\n      action: \"统一 bib 格式（全部列完整作者或全部用 et al.）\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-MISC\"\n  summary: \"无代码/数据发布\"\n  category: format\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"负面结果论文可复现性最后防线。\"\n    - round: 2\n      reviewers: [1]\n      note: \"仍未提及代码开源。Reproducibility 3.0/5。\"\n    - round: 3\n      reviewers: []\n      note: \"Round 3 未被独立提出，但 Reproducibility 评分仍为 3.5/5。待投稿前解决。\"\n  action_items:\n    - round: 2\n      action: \"投稿前准备匿名 GitHub repo\"\n      assigned_to: agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-W1-new\"\n  summary: \"Table 1 缺少 autoregressive GAR 数据\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 2\n  last_seen_round: 3\n  mentions:\n    - round: 2\n      reviewers: [1, 2]\n      note: \"核心发现 20-33× gap 未在表格中系统呈现。\"\n    - round: 3\n      reviewers: [1, 2]\n      note: \"Table 1 AR 列存在但仅 N=5。Round 3 核心问题转为 AR 评估样本量不足（见 R1-N2）。\"\n  action_items:\n    - round: 2\n      action: \"D048: Table 1 增加 AR 列或新建 AR 对比表\"\n      assigned_to: paper_agent\n      status: done\n    - round: 3\n      action: \"AR 列扩大评估至 N≥30 + CI（与 R1-N2 联动）\"\n      assigned_to: agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-W4-new\"\n  summary: \"写作冗余——关键数字在多个 section 重复\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 2\n  last_seen_round: 3\n  mentions:\n    - round: 2\n      reviewers: [1, 2]\n      note: \"'20-33× gap' 等在 Abstract/Intro/Experiments/Analysis/Discussion/Conclusion 各出现多次。\"\n    - round: 3\n      reviewers: [1, 2]\n      note: \"Round 3 两位 Reviewer 再次指出。'20-33×' 出现 8+ 次，'0.015-0.025' 出现 5+ 次。在 8 页限制下严重浪费空间，加剧超页问题。\"\n  action_items:\n    - round: 2\n      action: \"D048: Abstract/Intro 用高层结论，Discussion/Conclusion 侧重 implication，减少重复\"\n      assigned_to: paper_agent\n      status: in_progress\n    - round: 3\n      action: \"Abstract/§4.2 各保留一次完整数字，后续章节改用 'the TF-AR gap (Table 1)' 简洁回指\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-W6-new\"\n  summary: \"Contribution (1) 过度声称泛化性\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 2\n  last_seen_round: 3\n  mentions:\n    - round: 2\n      reviewers: [1, 2]\n      note: \"'in principle applicable to other auxiliary objective analyses' 未经验证。\"\n    - round: 3\n      reviewers: [1, 2]\n      note: \"Round 3 合并至 R2-N1 追踪。R2 再次指出，R1 同意删除泛化声称但保留 framework 表述。\"\n  action_items:\n    - round: 2\n      action: \"D048: 加入限定语或删除泛化声称\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"合并至 R2-N1 追踪。\"\n  resolution_round: null\n\n- id: \"R2-W7-new\"\n  summary: \"Li et al. (2024) split-softmax 缺乏实验对比\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - round: 2\n      reviewers: [2]\n      note: \"最直接竞争 inference-time 方法。R1 认为超出 scope。定为建议。\"\n    - round: 3\n      reviewers: []\n      note: \"Round 3 未被独立提出。§6 Discussion 已有定性对比。\"\n  action_items:\n    - round: 2\n      action: \"D048: 加入定性机制分析\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# Supplementary items from Round 2\n# ============================================================\n\n- id: \"R2-SUPP-1\"\n  summary: \"Figure caption overclaim（如 Fig 5 attention steering）\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 2\n  last_seen_round: 3\n  mentions:\n    - round: 2\n      reviewers: []\n      note: \"Reviewer 独立评估发现 figure caption 可能有与正文一致的 overclaim 需同步修正。\"\n    - round: 3\n      reviewers: [2]\n      note: \"Figure 4 caption 存在同一句话内重复：'the gap persists across all five variants... the gap persists across all five tested configurations'。\"\n  action_items:\n    - round: 2\n      action: \"Paper Agent 审查所有 figure caption 是否含 overclaim，与正文 claim 降级同步\"\n      assigned_to: paper_agent\n      status: in_progress\n    - round: 3\n      action: \"修正 Figure 4 caption 重复句\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-SUPP-2\"\n  summary: \"Multi-seed 完成后 Abstract/Intro 数字需更新\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - round: 2\n      reviewers: []\n      note: \"Multi-seed 实验完成后，Abstract/Intro 的 gap 数字需从单 seed 值更新为 mean±std。\"\n    - round: 3\n      reviewers: []\n      note: \"仍为 open，待 D048 multi-seed 实验完成。\"\n  action_items:\n    - round: 2\n      action: \"Multi-seed 完成后 Paper Agent 更新所有 Abstract/Intro/Conclusion 中的数字\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-SUPP-3\"\n  summary: \"SS variance 风险应急计划\"\n  category: experiment\n  severity: info\n  status: open\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - round: 2\n      reviewers: []\n      note: \"SS 的 3-seed 若 variance 极大（seed-dependent），需应急 framing。\"\n    - round: 3\n      reviewers: []\n      note: \"仍为 open。Round 3 两位 Reviewer 的 SS 种子差异（31%）进一步增加了此应急计划的重要性。\"\n  action_items:\n    - round: 2\n      action: \"SS multi-seed 结果出来后评估 variance，若 CoV>50% 调整 framing\"\n      assigned_to: director\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# New issues from Round 3\n# ============================================================\n\n- id: \"R3-MF2\"\n  summary: \"正文超过 EMNLP 2026 的 8 页限制（约 8.4 页）\"\n  category: format\n  severity: critical\n  status: open\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n    - round: 3\n      reviewers: [1, 2]\n      note: \"§6 Discussion 延续到第 9 页约 60%，§7 Conclusion 在第 9 页上半。正文约 8.4 页，超出约 0.4 页。ARR 格式检查可能 desk-reject。两位 Reviewer 共识列为 Critical。\"\n  action_items:\n    - round: 3\n      action: \"将 §6 instruction retention 段落移入 Appendix（~0.3 页）+ 压缩写作冗余（与 R2-W4-new 联动）\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-SF4\"\n  summary: \"PCGrad modus tollens scope 过度概括——仅排除 direction conflict\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n    - round: 3\n      reviewers: [1, 2]\n      note: \"PCGrad 仅处理梯度方向冲突，magnitude imbalance (GradNorm) 和 Nash equilibrium 未测试。§1 contribution (1) 中 'gradient conflict' 未加 'directional' 限定词。两位 Reviewer 共识 Should-Fix。\"\n  action_items:\n    - round: 3\n      action: \"§1 contribution (1) 和 §5.2 结论处：'gradient conflict' → 'gradient direction conflict'；提及 magnitude imbalance 未排除\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-SF6\"\n  summary: \"缺少 Rhea (arXiv:2512.06869, 2025) 引用\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n    - round: 3\n      reviewers: [1, 2]\n      note: \"Rhea 提出 Role-aware Heuristic Episodic Attention，inference-time 多轮对话注意力方案。与 §4.3 steering 和 §6 Discussion 直接相关。R2 提出，R1 同意（但无法独立验证）。\"\n  action_items:\n    - round: 3\n      action: \"查证并引用 Rhea，在 §2 Attention manipulation 段落讨论，§6 与 β-steering 对比\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-MINOR-1\"\n  summary: \"LoRA capacity saturation 替代解释未讨论\"\n  category: method\n  severity: info\n  status: open\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n    - round: 3\n      reviewers: [1]\n      note: \"R1 提出 LoRA 可能已饱和 TF GAR target，gate 自然无增量。R2 反驳：不影响核心 TF-AR gap claim。Director 裁定 minor。\"\n  action_items:\n    - round: 3\n      action: \"在 §4.2 加一句 acknowledge：'The convergence could partly reflect LoRA capacity saturation; however, the TF-AR gap persists regardless'\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-MINOR-2\"\n  summary: \"GPU 型号名称准确性待确认\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n    - round: 3\n      reviewers: [2]\n      note: \"§4.1 'NVIDIA RTX PRO 6000 Blackwell Server Edition GPU (102 GB)' — 型号名称在 2026 年 5 月可能尚未广泛可用，建议确认准确性。\"\n  action_items:\n    - round: 3\n      action: \"确认 GPU 型号名称准确性\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "turn_residual_gating",
    "issues_yaml": "# Review Issues Tracker — turn_residual_gating\n# Round 1 (2026-05-19, dream_20260519T145320)\n# Round 2 (2026-05-22, fresh re-review of revised paper)\n# Round 3 (2026-05-22, fresh re-review — current round)\n\n# ============================================================\n# Issues from Round 1 — status updates through Round 3\n# ============================================================\n\n- id: \"R1-N1\"\n  summary: \"所有引用渲染为 '?'——bibliography 编译失败\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"Dream paper artifact。\"\n    - round: 2\n      reviewers: []\n      note: \"视觉审查确认无 [?] 未解析引用。已修复。\"\n    - round: 3\n      reviewers: []\n      note: \"Round 3 视觉审查确认无未解析引用。维持 resolved。\"\n  action_items:\n    - round: 1\n      action: \"Paper Agent 确保 bibtex 编译正确\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"Round 2 视觉审查确认已修复。\"\n  resolution_round: 2\n\n- id: \"R1-N2\"\n  summary: \"单种子支撑结论——统计功效不足\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 3\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"Bootstrap CI 仅覆盖 eval variance，不覆盖 training variance。\"\n    - round: 2\n      reviewers: [1, 2]\n      note: \"ThreadGate 已补 seed=123，但其余 4/5 条件仍为单 seed。SS 仅 1 seed 且第二 seed 协议不同不可比。两位 Reviewer 独立列为 Critical。\"\n    - round: 3\n      reviewers: [1, 2]\n      note: \"Round 3 两位 Reviewer 再次独立列为 Critical。R1-N1 指出 AR 评估仅 N=5，核心 claim 'all variants collapse equally' 缺统计检验。R1-N2 指出 SS 双种子差异大（GAR 0.318 vs 0.418）且策略不同。两项均为 Must-Fix。\"\n  action_items:\n    - round: 1\n      action: \"plan_019: seed=123 extra training\"\n      assigned_to: agent\n      status: done\n    - round: 2\n      action: \"D048: 5 条件 × 3 seeds from-scratch (Base/TG/LO/UG/SS)，SS 最高优先级。~45h GPU。\"\n      assigned_to: agent\n      status: in_progress\n    - round: 3\n      action: \"AR 评估扩大至 N≥30 + bootstrap 95% CI + 条件间成对检验\"\n      assigned_to: agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-N3\"\n  summary: \"评估样本量过小\"\n  category: experiment\n  severity: info\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1]\n      note: \"Cohen's d≈0.22 在 n=50 下 power 不足。\"\n    - round: 2\n      reviewers: []\n      note: \"Round 2 使用 N=50 held-out + N=50 steering + N=20 Llama。未再被提出。\"\n    - round: 3\n      reviewers: []\n      note: \"TF 评估样本量已充分。但 AR 评估 N=5 问题在 R1-N2 中追踪。\"\n  action_items: []\n  resolution: \"N=50 评估已在论文中体现。AR N=5 问题移至 R1-N2 追踪。\"\n  resolution_round: 2\n\n- id: \"R1-N4\"\n  summary: \"损失函数超参数和 v1-v6 配置定义缺失\"\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"v1-v7 配置仅报告 v7。\"\n    - round: 2\n      reviewers: []\n      note: \"§3.3 报告 λ_GAR=λ_div=1.0。Appendix Table 2 列出 v1-v7。未再被提出。\"\n  action_items: []\n  resolution: \"§3.3 + Appendix B Table 2 已提供完整信息。\"\n  resolution_round: 2\n\n- id: \"R1-W1\"\n  summary: \"Llama 跨模型消融不完整（缺 PCGrad + Uniform Gate）\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 3\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"边际信息量不值 6h GPU。\"\n    - round: 2\n      reviewers: [1, 2]\n      note: \"仍仅 3/5 条件，N=20，用 median。两位 Reviewer 再次指出。\"\n    - round: 3\n      reviewers: [1, 2]\n      note: \"Round 3 两位 Reviewer 再次指出。额外问题：使用 median 而非 mean 但未报告 mean 对照；AR/TF 样本量不匹配（TF N=50 vs AR N=20）；attention spikes 成因未解释。\"\n  action_items:\n    - round: 2\n      action: \"D048: 补充 Llama PCGrad+UG 训练+评估，完成 5-way 跨模型对比。~14h GPU。\"\n      assigned_to: agent\n      status: in_progress\n    - round: 3\n      action: \"报告 mean+median 双指标，展示 AR GAR 完整分布（boxplot），解释 attention spikes 成因\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-W2\"\n  summary: \"无 λ_GAR 敏感性消融\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - round: 1\n      reviewers: [1]\n      note: \"梯度冲突取决于 λ_GAR。\"\n    - round: 2\n      reviewers: []\n      note: \"§3.3 报告 λ=1.0 但仍无敏感性分析。未被 Round 2 reviewer 独立提出为 must-fix。\"\n    - round: 3\n      reviewers: []\n      note: \"Round 3 未被提及。可能因论文核心 claim 转向 exposure bias 而非 loss 配置，优先级降低。待 Research Director 确认。\"\n  action_items:\n    - round: 1\n      action: \"plan_022: λ_GAR=10 敏感性测试\"\n      assigned_to: agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-W3\"\n  summary: \"训练数据量混淆变量\"\n  category: experiment\n  severity: info\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1]\n      note: \"1,000 convs 偏少。\"\n    - round: 2\n      reviewers: []\n      note: \"Round 2 使用 8K conversations。\"\n  action_items: []\n  resolution: \"训练数据量增加至 8K。\"\n  resolution_round: 2\n\n- id: \"R1-W4\"\n  summary: \"全文零 figure\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"Dream paper artifact.\"\n    - round: 2\n      reviewers: []\n      note: \"Round 2 有 5 figures + 2 tables。\"\n  action_items: []\n  resolution: \"Figure 1-5 + Table 1-2 已就位。\"\n  resolution_round: 2\n\n- id: \"R1-W5\"\n  summary: \"Scheduled sampling 统计支撑不足\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 3\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"单 seed，单 ratio，PPL 未报告。\"\n    - round: 2\n      reviewers: [1, 2]\n      note: \"PPL 已报告，但仍单 seed，第二 seed 协议不同不可比。\"\n    - round: 3\n      reviewers: [1, 2]\n      note: \"Round 3 两位 Reviewer 再次独立列为 Must-Fix/Critical。双种子差异大（GAR 0.318 vs 0.418, gap 1.57× vs 1.20×）且策略不同（resume vs from scratch）。Abstract 仅引用 seed 1。两位 Reviewer 建议从 contribution 降级或补充 ≥3 同策略种子。\"\n  action_items:\n    - round: 2\n      action: \"D048: SS 3-seed from-scratch 作为 multi-seed 最高优先级条件\"\n      assigned_to: agent\n      status: in_progress\n    - round: 3\n      action: \"从 contribution 列表降级为 Discussion preliminary observation，或补充 ≥3 同策略种子后恢复\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-W6\"\n  summary: \"Reverse turn conditioning 证据间接\"\n  category: experiment\n  severity: info\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1]\n      note: \"差异可能是噪声。\"\n  resolution: \"Wilcoxon p=3.73e-8, r=0.975。已在 §5.1 报告。\"\n  resolution_round: 2\n\n# ============================================================\n# Issues from Round 2\n# ============================================================\n\n- id: \"R2-N1\"\n  summary: \"Novelty/causal 声称过高——'causal diagnostic framework' 过度包装\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 3\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"'first quantitative measurement' overclaim。\"\n    - round: 2\n      reviewers: [1, 2]\n      note: \"Round 1 overclaim 已降级，但 Round 2 发现新 overclaim：Contribution (1) 'systematic causal diagnostic framework' 实际是消融。\"\n    - round: 3\n      reviewers: [1, 2]\n      note: \"Round 3 R2 再次指出 contribution (1) 'systematic diagnostic framework' 过度包装 + 'in principle applicable' 未验证。R1 部分反驳（认为超出标准消融），但同意删除泛化声称。R2 还指出 'first empirical characterization' 风险高。两位 Reviewer 共识：删除 'in principle applicable'，'first' → 'to our knowledge, the first'。\"\n  action_items:\n    - round: 1\n      action: \"'first quantitative measurement' 降级\"\n      assigned_to: director\n      status: done\n    - round: 2\n      action: \"D048: 'causal' → 'systematic diagnostic/ablation'；限定 PCGrad scope\"\n      assigned_to: paper_agent\n      status: in_progress\n    - round: 3\n      action: \"删除 'in principle applicable to other auxiliary objective analyses'；'first empirical characterization' → 'to our knowledge, the first' 或 'a detailed'\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-N2\"\n  summary: \"标题过度声称\"\n  category: framing\n  severity: info\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 3\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"'Cannot Fix' → 已改为 'Fails to Fix'。\"\n    - round: 2\n      reviewers: [1, 2]\n      note: \"'Lightweight Gating' 暗示一类方法但仅测试 ThreadGate。\"\n    - round: 3\n      reviewers: [2]\n      note: \"R2 认为 'Per-Layer Residual Gating' 暗示广泛测试但仅两种变体。R1 反驳：标题准确描述所测试方法，核心结论关于训练范式非 gating 穷举。Director 裁定：当前标题可接受。\"\n  action_items:\n    - round: 2\n      action: \"D048: 标题改为更精确表述\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"Round 3 Director 裁定当前标题可接受——R1 反驳有理，标题描述的是具体测试方法类型而非穷举声称。\"\n  resolution_round: 3\n\n- id: \"R2-N3\"\n  summary: \"Dongre et al. (2026) GAR 全称引用错误\"\n  category: format\n  severity: critical\n  status: open\n  first_raised_round: 1\n  last_seen_round: 3\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"论文动机链依赖此引用。\"\n    - round: 2\n      reviewers: [2]\n      note: \"R2 指出 Dongre 原文为 'Goal Accessibility Ratio'，本文写为 'Goal Attention Ratio'。\"\n    - round: 3\n      reviewers: [1, 2]\n      note: \"Round 3 R2 通过 arXiv 原文验证确认为 'Goal Accessibility Ratio (GAR)'。R1 完全同意。两位 Reviewer 共识列为 Critical Must-Fix。语义差异：'Accessibility' 强调信息可达性，'Attention' 缩窄到注意力权重。\"\n  action_items:\n    - round: 2\n      action: \"D048: 确认 Dongre 原文全称并更正\"\n      assigned_to: paper_agent\n      status: in_progress\n    - round: 3\n      action: \"全文替换 'Goal Attention Ratio' → 'Goal Accessibility Ratio'。可保留说明 GAR-ours 变体聚焦 attention weight。\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-N4\"\n  summary: \"Related Work 缺失 gradient conflict 文献 + PCGrad baseline\"\n  category: framing\n  severity: info\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"如果 PCGrad 能解决梯度竞争，论文核心结论悬空。\"\n    - round: 2\n      reviewers: []\n      note: \"PCGrad 已纳入五路对比，§2 已覆盖 gradient conflict 文献。\"\n  action_items: []\n  resolution: \"PCGrad 已纳入五路对比 + Related Work 已覆盖。\"\n  resolution_round: 2\n\n- id: \"R2-C3\"\n  summary: \"Exposure bias 归因存在未排除的替代解释\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 2\n  last_seen_round: 3\n  mentions:\n    - round: 2\n      reviewers: [1, 2]\n      note: \"β-steering 不等于 exposure bias 是原因（循环论证）；SS 改变多个训练动态；KV cache 差异未排除。\"\n    - round: 3\n      reviewers: [1, 2]\n      note: \"R1 列为 Critical（KV cache drift/text statistics/GAR-ours 有效性未排除，steering 循环性）。R2 降为 Should-Fix（论文 hedging 适度，TRC+steering 组合提供 non-trivial evidence）。Director 裁定 Should-Fix：不要求额外排除实验，但需加强 KV cache drift 讨论。\"\n  action_items:\n    - round: 2\n      action: \"D048: 'the proximal cause' → 'a proximal cause consistent with evidence'；Discussion 讨论替代假说\"\n      assigned_to: paper_agent\n      status: in_progress\n    - round: 3\n      action: \"在 §5.3 或 §6 加一段明确讨论 KV cache drift 作为 confound；承认 steering 论证循环性风险\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-W3\"\n  summary: \"GAR 单指标依赖——缺乏下游任务验证\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 3\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"r=0.82 sanity check 不足以作为 gold-standard proxy。\"\n    - round: 2\n      reviewers: [1, 2]\n      note: \"§6 instruction retention 分析 McNemar p=0.077 不显著，r=0.200 极弱。\"\n    - round: 3\n      reviewers: [1, 2]\n      note: \"Round 3 两位 Reviewer 均指出 instruction retention 不显著但占 Discussion 过多篇幅。建议移入 Appendix（也有助于解决超页问题）。\"\n  action_items:\n    - round: 2\n      action: \"D048: N=200 扩容指令保持实验\"\n      assigned_to: agent\n      status: in_progress\n    - round: 3\n      action: \"Instruction retention 段落移入 Appendix 或压缩至一句\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-W5\"\n  summary: \"liu2016attention 引用可能错配\"\n  category: format\n  severity: warning\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [2]\n      note: \"语音识别 vs 注意力引导。\"\n    - round: 2\n      reviewers: []\n      note: \"Round 2 未提及，待确认。\"\n    - round: 3\n      reviewers: []\n      note: \"Round 3 未提及。可能已修复或不在当前版本中。待 Research Director 确认。\"\n  action_items:\n    - round: 2\n      action: \"Paper Agent 确认引用准确性\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-W6\"\n  summary: \"Bib 格式不一致 + orphan 条目\"\n  category: format\n  severity: info\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 3\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"vaswani2017, elhage2021, olsson2022, efron1994。\"\n    - round: 2\n      reviewers: [2]\n      note: \"部分用 'and others' 部分列完整作者，格式不一致。\"\n    - round: 3\n      reviewers: [2]\n      note: \"grattafiori2024llama3 使用 'and others'，其他条目列完整作者列表。格式不一致仍存在。\"\n  action_items:\n    - round: 2\n      action: \"统一 bib 格式，清理 orphan 条目\"\n      assigned_to: paper_agent\n      status: in_progress\n    - round: 3\n      action: \"统一 bib 格式（全部列完整作者或全部用 et al.）\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-MISC\"\n  summary: \"无代码/数据发布\"\n  category: format\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"负面结果论文可复现性最后防线。\"\n    - round: 2\n      reviewers: [1]\n      note: \"仍未提及代码开源。Reproducibility 3.0/5。\"\n    - round: 3\n      reviewers: []\n      note: \"Round 3 未被独立提出，但 Reproducibility 评分仍为 3.5/5。待投稿前解决。\"\n  action_items:\n    - round: 2\n      action: \"投稿前准备匿名 GitHub repo\"\n      assigned_to: agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-W1-new\"\n  summary: \"Table 1 缺少 autoregressive GAR 数据\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 2\n  last_seen_round: 3\n  mentions:\n    - round: 2\n      reviewers: [1, 2]\n      note: \"核心发现 20-33× gap 未在表格中系统呈现。\"\n    - round: 3\n      reviewers: [1, 2]\n      note: \"Table 1 AR 列存在但仅 N=5。Round 3 核心问题转为 AR 评估样本量不足（见 R1-N2）。\"\n  action_items:\n    - round: 2\n      action: \"D048: Table 1 增加 AR 列或新建 AR 对比表\"\n      assigned_to: paper_agent\n      status: done\n    - round: 3\n      action: \"AR 列扩大评估至 N≥30 + CI（与 R1-N2 联动）\"\n      assigned_to: agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-W4-new\"\n  summary: \"写作冗余——关键数字在多个 section 重复\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 2\n  last_seen_round: 3\n  mentions:\n    - round: 2\n      reviewers: [1, 2]\n      note: \"'20-33× gap' 等在 Abstract/Intro/Experiments/Analysis/Discussion/Conclusion 各出现多次。\"\n    - round: 3\n      reviewers: [1, 2]\n      note: \"Round 3 两位 Reviewer 再次指出。'20-33×' 出现 8+ 次，'0.015-0.025' 出现 5+ 次。在 8 页限制下严重浪费空间，加剧超页问题。\"\n  action_items:\n    - round: 2\n      action: \"D048: Abstract/Intro 用高层结论，Discussion/Conclusion 侧重 implication，减少重复\"\n      assigned_to: paper_agent\n      status: in_progress\n    - round: 3\n      action: \"Abstract/§4.2 各保留一次完整数字，后续章节改用 'the TF-AR gap (Table 1)' 简洁回指\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-W6-new\"\n  summary: \"Contribution (1) 过度声称泛化性\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 2\n  last_seen_round: 3\n  mentions:\n    - round: 2\n      reviewers: [1, 2]\n      note: \"'in principle applicable to other auxiliary objective analyses' 未经验证。\"\n    - round: 3\n      reviewers: [1, 2]\n      note: \"Round 3 合并至 R2-N1 追踪。R2 再次指出，R1 同意删除泛化声称但保留 framework 表述。\"\n  action_items:\n    - round: 2\n      action: \"D048: 加入限定语或删除泛化声称\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"合并至 R2-N1 追踪。\"\n  resolution_round: null\n\n- id: \"R2-W7-new\"\n  summary: \"Li et al. (2024) split-softmax 缺乏实验对比\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - round: 2\n      reviewers: [2]\n      note: \"最直接竞争 inference-time 方法。R1 认为超出 scope。定为建议。\"\n    - round: 3\n      reviewers: []\n      note: \"Round 3 未被独立提出。§6 Discussion 已有定性对比。\"\n  action_items:\n    - round: 2\n      action: \"D048: 加入定性机制分析\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# Supplementary items from Round 2\n# ============================================================\n\n- id: \"R2-SUPP-1\"\n  summary: \"Figure caption overclaim（如 Fig 5 attention steering）\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 2\n  last_seen_round: 3\n  mentions:\n    - round: 2\n      reviewers: []\n      note: \"Reviewer 独立评估发现 figure caption 可能有与正文一致的 overclaim 需同步修正。\"\n    - round: 3\n      reviewers: [2]\n      note: \"Figure 4 caption 存在同一句话内重复：'the gap persists across all five variants... the gap persists across all five tested configurations'。\"\n  action_items:\n    - round: 2\n      action: \"Paper Agent 审查所有 figure caption 是否含 overclaim，与正文 claim 降级同步\"\n      assigned_to: paper_agent\n      status: in_progress\n    - round: 3\n      action: \"修正 Figure 4 caption 重复句\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-SUPP-2\"\n  summary: \"Multi-seed 完成后 Abstract/Intro 数字需更新\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - round: 2\n      reviewers: []\n      note: \"Multi-seed 实验完成后，Abstract/Intro 的 gap 数字需从单 seed 值更新为 mean±std。\"\n    - round: 3\n      reviewers: []\n      note: \"仍为 open，待 D048 multi-seed 实验完成。\"\n  action_items:\n    - round: 2\n      action: \"Multi-seed 完成后 Paper Agent 更新所有 Abstract/Intro/Conclusion 中的数字\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-SUPP-3\"\n  summary: \"SS variance 风险应急计划\"\n  category: experiment\n  severity: info\n  status: open\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - round: 2\n      reviewers: []\n      note: \"SS 的 3-seed 若 variance 极大（seed-dependent），需应急 framing。\"\n    - round: 3\n      reviewers: []\n      note: \"仍为 open。Round 3 两位 Reviewer 的 SS 种子差异（31%）进一步增加了此应急计划的重要性。\"\n  action_items:\n    - round: 2\n      action: \"SS multi-seed 结果出来后评估 variance，若 CoV>50% 调整 framing\"\n      assigned_to: director\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# New issues from Round 3\n# ============================================================\n\n- id: \"R3-MF2\"\n  summary: \"正文超过 EMNLP 2026 的 8 页限制（约 8.4 页）\"\n  category: format\n  severity: critical\n  status: open\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n    - round: 3\n      reviewers: [1, 2]\n      note: \"§6 Discussion 延续到第 9 页约 60%，§7 Conclusion 在第 9 页上半。正文约 8.4 页，超出约 0.4 页。ARR 格式检查可能 desk-reject。两位 Reviewer 共识列为 Critical。\"\n  action_items:\n    - round: 3\n      action: \"将 §6 instruction retention 段落移入 Appendix（~0.3 页）+ 压缩写作冗余（与 R2-W4-new 联动）\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-SF4\"\n  summary: \"PCGrad modus tollens scope 过度概括——仅排除 direction conflict\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n    - round: 3\n      reviewers: [1, 2]\n      note: \"PCGrad 仅处理梯度方向冲突，magnitude imbalance (GradNorm) 和 Nash equilibrium 未测试。§1 contribution (1) 中 'gradient conflict' 未加 'directional' 限定词。两位 Reviewer 共识 Should-Fix。\"\n  action_items:\n    - round: 3\n      action: \"§1 contribution (1) 和 §5.2 结论处：'gradient conflict' → 'gradient direction conflict'；提及 magnitude imbalance 未排除\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-SF6\"\n  summary: \"缺少 Rhea (arXiv:2512.06869, 2025) 引用\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n    - round: 3\n      reviewers: [1, 2]\n      note: \"Rhea 提出 Role-aware Heuristic Episodic Attention，inference-time 多轮对话注意力方案。与 §4.3 steering 和 §6 Discussion 直接相关。R2 提出，R1 同意（但无法独立验证）。\"\n  action_items:\n    - round: 3\n      action: \"查证并引用 Rhea，在 §2 Attention manipulation 段落讨论，§6 与 β-steering 对比\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-MINOR-1\"\n  summary: \"LoRA capacity saturation 替代解释未讨论\"\n  category: method\n  severity: info\n  status: open\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n    - round: 3\n      reviewers: [1]\n      note: \"R1 提出 LoRA 可能已饱和 TF GAR target，gate 自然无增量。R2 反驳：不影响核心 TF-AR gap claim。Director 裁定 minor。\"\n  action_items:\n    - round: 3\n      action: \"在 §4.2 加一句 acknowledge：'The convergence could partly reflect LoRA capacity saturation; however, the TF-AR gap persists regardless'\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-MINOR-2\"\n  summary: \"GPU 型号名称准确性待确认\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n    - round: 3\n      reviewers: [2]\n      note: \"§4.1 'NVIDIA RTX PRO 6000 Blackwell Server Edition GPU (102 GB)' — 型号名称在 2026 年 5 月可能尚未广泛可用，建议确认准确性。\"\n  action_items:\n    - round: 3\n      action: \"确认 GPU 型号名称准确性\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null"
  }
}
```

</details>

---


### Tool result

_source line 227 · 2026-05-22T13:05:55.569542+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_issues.yaml\", \"bytes\": 21348}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 228 · 2026-05-22T13:08:16.987855+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "project": "turn_residual_gating",
  "report": "# Round 3 审稿报告 — turn_residual_gating\n\n**论文**: \"Why Per-Layer Residual Gating Fails to Fix Multi-Turn Attention Degradation: A Mechanistic Analysis\"\n**Venue**: EMNLP 2026 via ACL Rolling Review (ARR August 2026 cycle)\n**截止日期**: 2026-08-03\n**审稿模式**: Fresh (重新审稿)\n**Reviewer 编排**: 2 人（R1: 方法严谨性+实验设计, R2: 新颖性+完整性+写作质量）\n\n---\n\n## Summary\n\n本文提出 ThreadGate，一种 per-layer content-and-turn-conditioned MLP gate，通过调制 residual stream 并结合 GAR auxiliary loss 来解决多轮对话中的注意力衰减问题。五路对比实验（ThreadGate, +PCGrad, Uniform Gate, LoRA-only, Base）显示所有训练时干预在 teacher-forced 下成功（GAR=0.50），但在 autoregressive 生成下 GAR 跌至 0.015–0.025（20–33× gap），gating 无增量贡献。论文将此归因于 exposure bias，并通过 inference-time attention steering 和 scheduled sampling 提供 mitigation 证据。跨模型在 Llama-3.1-8B 上确认了该 gap（27×）。\n\n---\n\n## Strengths\n\n1. **五路对比实验设计精良**：系统性隔离 turn conditioning、gating mechanism、gradient direction conflict、fine-tuning 四个因素，每对对比有明确实验支撑。PCGrad 作为因果排除工具（modus tollens）的使用超出标准消融范式。[AGREE: R1, R2]\n2. **诚实且有深度的 negative result**：不伪装成正面结果，直接呈现 gating 失败并追溯到 exposure bias 机制。TRC 指标作为正交验证增强了论证。[AGREE: R1, R2]\n3. **Hedging 措辞适度**：\"a proximal cause consistent with our evidence\" 比 \"the root cause\" 更准确；Discussion 明确列出了 alternative hypotheses（attention drift, KV cache effects, implicit label smoothing）。[AGREE: R1, R2]\n4. **Loss formulation 搜索透明**：Table 2 (Appendix B) 记录 7 次迭代中 6 次失败的完整历程，为后续工作节省探索成本。[AGREE: R1, R2]\n5. **跨模型验证**（Llama-3.1-8B）增强结论泛化性，尽管覆盖有限（2 model families, 3/5 conditions）。[AGREE: R1, R2]\n\n---\n\n## Weaknesses — Must-Fix (影响接收决定)\n\n### MF-1 [Critical] GAR 全称引用错误 [AGREE: R1, R2]\n\nDongre et al. (2026, arXiv:2605.12922) 原文定义为 **\"Goal Accessibility Ratio\"**，本文在 Abstract、§1、§3.1 等所有位置误写为 \"Goal Attention Ratio\"。已通过 arXiv 原文验证。这是论文最核心度量指标的定义错误，直接损害学术严谨性。\"Accessibility\" 强调信息可达性（与论文引用的 AUC=0.98 linear probe 结果一致），\"Attention\" 缩窄到注意力权重。\n\n**修复**: 全文替换为正确全称。可保留说明 GAR-ours 变体聚焦 attention weight。\n\n### MF-2 [Critical] 正文超过 EMNLP 2026 的 8 页限制 [AGREE: R1, R2]\n\n§6 Discussion 延续到第 9 页约 60%，§7 Conclusion 在第 9 页上半。正文约 8.4 页，超出约 0.4 页。ARR 格式检查可能 desk-reject。\n\n**修复**: 将 §6 instruction retention 段落移入 Appendix（~0.3 页）+ 压缩写作冗余（见 SF-3）。\n\n### MF-3 [Critical] AR 评估样本量过小（N=5），核心 claim 缺乏统计检验 [AGREE: R1, R2]\n\nTable 1 的 AR GAR 列仅基于 N=5 条 10-turn 对话。五个配置的 AR GAR (0.012–0.025) 差异在 N=5 下无法做统计区分。论文未报告 AR GAR 的 confidence interval 或条件间显著性检验。\"all variants collapse equally\" 这一核心 claim 缺乏统计支撑。\n\n注：TF-AR gap 本身（0.50 vs 0.015–0.025，跨越一个数量级）即使 N=5 也不太可能是随机波动，且 seed 42/123 双种子结果一致。问题在于五个条件之间的 AR GAR 差异无法判断是否有意义。\n\n**修复**: AR 评估扩大至 N≥30（与 steering 实验 N=50 对齐），报告 bootstrap 95% CI，做条件间成对检验。\n\n### MF-4 [Critical] Scheduled sampling 单种子结果作为 contribution 可靠性不足 [AGREE: R1, R2]\n\n两个种子结果差异大（GAR 0.318 vs 0.418，gap 1.57× vs 1.20×，差异 31%），且训练策略不同（resume vs from scratch），无法分离 seed variance 和 strategy effect。Abstract 仅引用 seed 1 数据（gap 1.57×），给读者过高确定性印象。\n\n**修复**: 从 contribution 列表降级为 Discussion 中的 preliminary observation，或补充 ≥3 个同策略种子。\n\n---\n\n## Weaknesses — Should-Fix (影响评分但不一票否决)\n\n### SF-1 [Warning] Exposure bias 归因未完全排除替代假说 [R1: Critical, R2: Should-Fix → Director 裁定: Should-Fix]\n\nKV cache drift（10-turn 中 KV cache 长度远超 TF 片段）、model-generated text 统计差异、GAR-ours 在 AR 下的有效性等替代假说在 Discussion 中仅一句带过。Steering 论证存在循环性风险（加 goal bias 当然增加 goal attention，无论原因是什么）。\n\n但论文的 hedging 适度（\"a proximal cause consistent with our evidence\"），TRC+steering 组合提供了 non-trivial evidence：如果 root cause 是 representation degradation 而非 attention routing，β-steering 应无法恢复 meaningful GAR，但实际恢复了 11×。Negative result paper 不应被要求达到 causal inference 标准。\n\n**修复**: 在 §5.3 或 §6 加一段明确讨论 KV cache drift 作为 confound（当前仅一句带过），承认 steering 论证的局限。不要求额外排除实验。\n\n### SF-2 [Warning] Cross-model 验证不完整 [AGREE: R1, R2]\n\n仅 3/5 条件（缺 +PCGrad, Uniform Gate），使用 median 而非 mean（未报告 mean 对照），N=20 偏小且与 TF N=50 不匹配。Attention spikes（5–8%）成因未解释。\n\n**修复**: 报告 mean+median 双指标，展示 AR GAR 完整分布，在正文标注覆盖局限。\n\n### SF-3 [Warning] \"20–33× gap\" 等数字在六个章节重复 8+ 次 [AGREE: R1, R2]\n\n同一数字在 Abstract/§1/§4.2/§5.3/§5.5/§6/§7 反复出现，信息密度低，浪费页面空间（加剧 MF-2 超页问题）。\n\n**修复**: Abstract 和 §4.2 各保留一次完整数字，后续章节改用 \"the TF-AR gap (Table 1)\" 等简洁回指。\n\n### SF-4 [Warning] PCGrad modus tollens scope 过度概括 [AGREE: R1, R2]\n\n§5.2 排除了 gradient direction conflict，但 magnitude imbalance (GradNorm) 和 Nash equilibrium violations 未测试。§1 contribution (1) 中 \"gradient conflict\" 未加 \"directional\" 限定词。\n\n**修复**: \"gradient conflict\" → \"gradient direction conflict\"；结论处提及 magnitude imbalance 未排除。\n\n### SF-5 [Warning] Contribution 声称需调整 [AGREE: R1, R2 (部分)]\n\n- Contribution (1): \"systematic diagnostic framework\" + \"in principle applicable to other auxiliary objective analyses\" 未验证泛化性。R2 认为等同消融，R1 反驳认为 PCGrad exclusion + TRC 正交验证超出标准消融。**共识**: 删除 \"in principle applicable\"，保留 framework 表述。\n- Contribution (2): \"first empirical characterization\" 风险高。**共识**: 改为 \"to our knowledge, the first\" 或 \"a detailed\"。\n- 标题: R2 认为 \"Per-Layer Residual Gating\" 过宽（仅两种变体），R1 反驳标题准确描述所测试方法。**Director 裁定: 当前标题可接受**。\n\n### SF-6 [Warning] 缺少 Rhea (arXiv:2512.06869, 2025) 引用 [AGREE: R1, R2]\n\nRole-aware Heuristic Episodic Attention，inference-time multi-turn attention 方案，与 §4.3 steering 和 §6 Discussion 直接相关。\n\n**修复**: 在 §2 \"Attention manipulation\" 段落引用，§6 与 β-steering 对比（Rhea 不需要 oracle access to goal tokens）。\n\n### SF-7 [Warning] Instruction retention 分析不显著但占 Discussion 过多篇幅 [AGREE: R1, R2]\n\nMcNemar p=0.077 不显著，r=0.200 极弱。在超页压力下应优先压缩。\n\n**修复**: 移入 Appendix 或压缩至一句（同时帮助解决 MF-2 超页问题）。\n\n---\n\n## Reviewer Consensus [AGREE]\n\n1. GAR 全称引用错误必须修正（Critical）\n2. 页数超限必须解决（Critical）\n3. AR 评估 N=5 不足以支撑核心 claim \"all collapse equally\"（Critical）\n4. Scheduled sampling 不应作为 contribution-level 声称——单种子 + 不同策略（Critical）\n5. 写作冗余需压缩，关键数字回引简化\n6. 论文是有价值的 negative result，五路对比设计超出标准消融\n7. **两位 Reviewer 均给出 3.0/5 (Findings)**\n\n---\n\n## Reviewer Divergence\n\n### 分歧 1: Exposure bias 归因严重性 [R1: Critical → R2: Should-Fix]\n\n- **R1**: 替代假说（KV cache drift, text statistics）未排除，steering 论证存在循环性，\"mechanistic analysis\" 标题要求超越相关性的因果理解\n- **R2**: 论文 hedging 适度，TRC+steering 组合提供 non-trivial evidence，negative result paper 不应等同 causal inference 标准\n- **Director 裁定**: **Should-Fix**。论文已做合理 hedging，但 KV cache drift 讨论确实过于简略。不要求额外排除实验。\n\n### 分歧 2: LoRA capacity saturation [R1: Should-Fix → R2: Minor]\n\n- **R1**: LoRA 可能已饱和 TF GAR target，\"gating 无用\"结论可能是 capacity ceiling artifact\n- **R2**: 此问题不影响核心 TF-AR gap claim——即使 LoRA 在 TF 饱和，也不解释 AR 崩溃\n- **Director 裁定**: **Minor**。R2 反驳有理——LoRA saturation 仅影响 \"gating vs LoRA-only\" 对比解读，不影响论文核心结论。在 §4.2 加一句 acknowledge 即可。\n\n---\n\n## Questions\n\n1. 如果 AR 评估扩大到 N=50，五个条件的 AR GAR 排序和 gap 大小是否保持不变？\n2. Scheduled sampling 两个种子采用不同策略（resume vs from scratch），相同策略下 3+ 种子是否可行？\n3. GAR 在 Dongre et al. 中的原始全称是 \"Goal Accessibility Ratio\"。使用 \"Goal Attention Ratio\" 是有意修改还是引用错误？\n4. β-steering 需要 oracle access to goal token positions，在实际部署中如何确定 goal tokens？\n5. \"token-level self-recovery does not extend to auxiliary objectives\" 是否是 trivially expected？论文贡献在于定量证据还是概念发现？\n6. Cross-model 评估中 \"5–8% sporadic attention spikes\" 的成因是什么？systematic behavior 还是 noise？\n\n---\n\n## Missing References\n\n1. **Rhea** (arXiv:2512.06869, Dec 2025): Role-aware Heuristic Episodic Attention，inference-time 多轮对话注意力方案 [AGREE: R1, R2]\n2. **\"Beyond Single-Turn: A Survey on Multi-Turn Interactions with LLMs\"** (arXiv:2504.04717, 2025): 多轮对话综述 [R2 提出，R1 认为可选]\n3. **Zhang et al., 2019** (\"Bridging the Gap between Training and Inference for NMT\"): exposure bias 在 NMT 中的经典分析 [R1 提出]\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n外部审稿：未请求（项目未配置外部审稿）。\n\n---\n\n## Visual Layout Check（非评分项）\n\n视觉审查已完成（0 critical, 4 warning, 12 info）。\n\n**Warnings**:\n- p3–4: Related Work + Method 连续 2 页无 figure/table，形成文字墙\n- p7: Figure 4+5 同页，Figure 5 子面板 axis label 字号过小（~55–60% 正文字号），建议放大或改为全宽 figure*\n- p8: Discussion 纯文本页，无 display item，建议加总结性表格\n- p11: Appendix 最后页 ~70% 空白，建议合并 Appendix A 内容\n\n**Info（选摘）**:\n- Figure 1 全宽概念图信息清晰，颜色区分度好\n- Table 1 booktabs 风格规范，float 位置良好\n- 全文 5 figures + 2 tables = 7 个 display items，合理\n- 无 margin 溢出、未解析引用或 LaTeX 错误残留\n\n---\n\n## Overall Assessment\n\n**Overall Score: 3.0 / 5 — Findings（可被 Findings 接收）**\n\n**Reviewer Confidence: 4/5**\n\n**Findings 而非 Conference 的核心原因**：4 个 critical must-fix 中，GAR 命名错误和超页属于格式/准确性问题可快速修复；但 AR 评估样本量不足（N=5）和 scheduled sampling 统计可靠性不足是实质性问题，需要额外实验才能解决。在补充多种子 AR 评估和 SS 实验之前，论文的统计基础不足以支撑 conference-level 接收。\n\n**达到 Findings 标准的原因**：五路对比设计精良且超出标准消融（PCGrad exclusion + TRC 正交验证），negative result 对 multi-task LLM 训练社区有实际参考价值，exposure bias 对 auxiliary loss 的选择性破坏是有意义的发现，hedging 适度。论文的实验框架和分析深度超出一般 workshop paper。\n\n**距 Conference (4.0) 的差距**：(1) AR 评估样本量和多种子覆盖需大幅加强；(2) scheduled sampling 需统计验证或从 contribution 降级；(3) 写作冗余需压缩以满足 8 页限制；(4) exposure bias 归因需更充分讨论替代假说。\n\n---\n\n## Detailed Comments\n\n### Abstract\n- \"Goal Attention Ratio\" → \"Goal Accessibility Ratio\"\n- \"Scheduled sampling compresses the gap to 1.57×\" → 加强 \"preliminary, single-seed\" 标注或移除\n\n### §1 Introduction\n- Contribution (1): 删除 \"in principle applicable to other auxiliary objective analyses\"\n- Contribution (2): \"first empirical characterization\" → \"to our knowledge, the first\" 或 \"a detailed\"\n- Contribution (2): scheduled sampling 从 contribution 降级或加强 preliminary 标注\n\n### §3.1 Preliminaries\n- \"Goal Attention Ratio\" → \"Goal Accessibility Ratio\"（全文替换）\n- 可保留说明 GAR-ours 变体聚焦 attention weight\n\n### §4.1 Setup\n- 确认 GPU 型号 \"RTX PRO 6000 Blackwell Server Edition\" 准确性\n\n### §4.2 Main Results\n- Table 1 AR 列: 扩大评估至 N≥30 + bootstrap 95% CI\n- Table 1 caption: \"GAR-O\" 缩写在首句解释\n- 加一句 acknowledge LoRA capacity saturation 替代解释\n\n### §4.3 Inference-Time Steering\n- 承认 β-steering 论证的循环性风险\n- 明确 steering 证据 + TRC 组合的 inferential scope\n\n### §5.2 PCGrad\n- \"gradient conflict\" → \"gradient direction conflict\"\n- 结论处提及 magnitude imbalance 未排除\n\n### §5.5 Cross-Model\n- 报告 mean + median 双指标\n- 展示 AR GAR 完整分布\n- 说明排除前两 turn 的理由\n- 在正文标注 3/5 条件覆盖的局限\n\n### §6 Discussion\n- Instruction retention 段落移入 Appendix（解决超页问题）\n- 加强 KV cache drift 讨论（不能仅一句带过）\n- Scheduled sampling: 标注 \"preliminary, single-seed, high-variance (GAR 0.318 vs 0.418 across two seeds)\"\n\n### §7 Conclusion\n- 数字回引简化，不重复 \"20–33×\"\n\n### Figure 4 caption\n- 删除重复句：\"the gap persists across all five variants..., the gap persists across all five tested configurations\"\n\n### Bib\n- grattafiori2024llama3: 统一作者列表格式\n- 全文 \"Goal Attention Ratio\" → \"Goal Accessibility Ratio\"",
  "reviewer_ids_acknowledged": "[\"1\", \"2\"]",
  "cross_response_reviewer_ids": "[\"1\", \"2\"]",
  "overall_score": "3.0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "project": "turn_residual_gating",
    "report": "# Round 3 审稿报告 — turn_residual_gating\n\n**论文**: \"Why Per-Layer Residual Gating Fails to Fix Multi-Turn Attention Degradation: A Mechanistic Analysis\"\n**Venue**: EMNLP 2026 via ACL Rolling Review (ARR August 2026 cycle)\n**截止日期**: 2026-08-03\n**审稿模式**: Fresh (重新审稿)\n**Reviewer 编排**: 2 人（R1: 方法严谨性+实验设计, R2: 新颖性+完整性+写作质量）\n\n---\n\n## Summary\n\n本文提出 ThreadGate，一种 per-layer content-and-turn-conditioned MLP gate，通过调制 residual stream 并结合 GAR auxiliary loss 来解决多轮对话中的注意力衰减问题。五路对比实验（ThreadGate, +PCGrad, Uniform Gate, LoRA-only, Base）显示所有训练时干预在 teacher-forced 下成功（GAR=0.50），但在 autoregressive 生成下 GAR 跌至 0.015–0.025（20–33× gap），gating 无增量贡献。论文将此归因于 exposure bias，并通过 inference-time attention steering 和 scheduled sampling 提供 mitigation 证据。跨模型在 Llama-3.1-8B 上确认了该 gap（27×）。\n\n---\n\n## Strengths\n\n1. **五路对比实验设计精良**：系统性隔离 turn conditioning、gating mechanism、gradient direction conflict、fine-tuning 四个因素，每对对比有明确实验支撑。PCGrad 作为因果排除工具（modus tollens）的使用超出标准消融范式。[AGREE: R1, R2]\n2. **诚实且有深度的 negative result**：不伪装成正面结果，直接呈现 gating 失败并追溯到 exposure bias 机制。TRC 指标作为正交验证增强了论证。[AGREE: R1, R2]\n3. **Hedging 措辞适度**：\"a proximal cause consistent with our evidence\" 比 \"the root cause\" 更准确；Discussion 明确列出了 alternative hypotheses（attention drift, KV cache effects, implicit label smoothing）。[AGREE: R1, R2]\n4. **Loss formulation 搜索透明**：Table 2 (Appendix B) 记录 7 次迭代中 6 次失败的完整历程，为后续工作节省探索成本。[AGREE: R1, R2]\n5. **跨模型验证**（Llama-3.1-8B）增强结论泛化性，尽管覆盖有限（2 model families, 3/5 conditions）。[AGREE: R1, R2]\n\n---\n\n## Weaknesses — Must-Fix (影响接收决定)\n\n### MF-1 [Critical] GAR 全称引用错误 [AGREE: R1, R2]\n\nDongre et al. (2026, arXiv:2605.12922) 原文定义为 **\"Goal Accessibility Ratio\"**，本文在 Abstract、§1、§3.1 等所有位置误写为 \"Goal Attention Ratio\"。已通过 arXiv 原文验证。这是论文最核心度量指标的定义错误，直接损害学术严谨性。\"Accessibility\" 强调信息可达性（与论文引用的 AUC=0.98 linear probe 结果一致），\"Attention\" 缩窄到注意力权重。\n\n**修复**: 全文替换为正确全称。可保留说明 GAR-ours 变体聚焦 attention weight。\n\n### MF-2 [Critical] 正文超过 EMNLP 2026 的 8 页限制 [AGREE: R1, R2]\n\n§6 Discussion 延续到第 9 页约 60%，§7 Conclusion 在第 9 页上半。正文约 8.4 页，超出约 0.4 页。ARR 格式检查可能 desk-reject。\n\n**修复**: 将 §6 instruction retention 段落移入 Appendix（~0.3 页）+ 压缩写作冗余（见 SF-3）。\n\n### MF-3 [Critical] AR 评估样本量过小（N=5），核心 claim 缺乏统计检验 [AGREE: R1, R2]\n\nTable 1 的 AR GAR 列仅基于 N=5 条 10-turn 对话。五个配置的 AR GAR (0.012–0.025) 差异在 N=5 下无法做统计区分。论文未报告 AR GAR 的 confidence interval 或条件间显著性检验。\"all variants collapse equally\" 这一核心 claim 缺乏统计支撑。\n\n注：TF-AR gap 本身（0.50 vs 0.015–0.025，跨越一个数量级）即使 N=5 也不太可能是随机波动，且 seed 42/123 双种子结果一致。问题在于五个条件之间的 AR GAR 差异无法判断是否有意义。\n\n**修复**: AR 评估扩大至 N≥30（与 steering 实验 N=50 对齐），报告 bootstrap 95% CI，做条件间成对检验。\n\n### MF-4 [Critical] Scheduled sampling 单种子结果作为 contribution 可靠性不足 [AGREE: R1, R2]\n\n两个种子结果差异大（GAR 0.318 vs 0.418，gap 1.57× vs 1.20×，差异 31%），且训练策略不同（resume vs from scratch），无法分离 seed variance 和 strategy effect。Abstract 仅引用 seed 1 数据（gap 1.57×），给读者过高确定性印象。\n\n**修复**: 从 contribution 列表降级为 Discussion 中的 preliminary observation，或补充 ≥3 个同策略种子。\n\n---\n\n## Weaknesses — Should-Fix (影响评分但不一票否决)\n\n### SF-1 [Warning] Exposure bias 归因未完全排除替代假说 [R1: Critical, R2: Should-Fix → Director 裁定: Should-Fix]\n\nKV cache drift（10-turn 中 KV cache 长度远超 TF 片段）、model-generated text 统计差异、GAR-ours 在 AR 下的有效性等替代假说在 Discussion 中仅一句带过。Steering 论证存在循环性风险（加 goal bias 当然增加 goal attention，无论原因是什么）。\n\n但论文的 hedging 适度（\"a proximal cause consistent with our evidence\"），TRC+steering 组合提供了 non-trivial evidence：如果 root cause 是 representation degradation 而非 attention routing，β-steering 应无法恢复 meaningful GAR，但实际恢复了 11×。Negative result paper 不应被要求达到 causal inference 标准。\n\n**修复**: 在 §5.3 或 §6 加一段明确讨论 KV cache drift 作为 confound（当前仅一句带过），承认 steering 论证的局限。不要求额外排除实验。\n\n### SF-2 [Warning] Cross-model 验证不完整 [AGREE: R1, R2]\n\n仅 3/5 条件（缺 +PCGrad, Uniform Gate），使用 median 而非 mean（未报告 mean 对照），N=20 偏小且与 TF N=50 不匹配。Attention spikes（5–8%）成因未解释。\n\n**修复**: 报告 mean+median 双指标，展示 AR GAR 完整分布，在正文标注覆盖局限。\n\n### SF-3 [Warning] \"20–33× gap\" 等数字在六个章节重复 8+ 次 [AGREE: R1, R2]\n\n同一数字在 Abstract/§1/§4.2/§5.3/§5.5/§6/§7 反复出现，信息密度低，浪费页面空间（加剧 MF-2 超页问题）。\n\n**修复**: Abstract 和 §4.2 各保留一次完整数字，后续章节改用 \"the TF-AR gap (Table 1)\" 等简洁回指。\n\n### SF-4 [Warning] PCGrad modus tollens scope 过度概括 [AGREE: R1, R2]\n\n§5.2 排除了 gradient direction conflict，但 magnitude imbalance (GradNorm) 和 Nash equilibrium violations 未测试。§1 contribution (1) 中 \"gradient conflict\" 未加 \"directional\" 限定词。\n\n**修复**: \"gradient conflict\" → \"gradient direction conflict\"；结论处提及 magnitude imbalance 未排除。\n\n### SF-5 [Warning] Contribution 声称需调整 [AGREE: R1, R2 (部分)]\n\n- Contribution (1): \"systematic diagnostic framework\" + \"in principle applicable to other auxiliary objective analyses\" 未验证泛化性。R2 认为等同消融，R1 反驳认为 PCGrad exclusion + TRC 正交验证超出标准消融。**共识**: 删除 \"in principle applicable\"，保留 framework 表述。\n- Contribution (2): \"first empirical characterization\" 风险高。**共识**: 改为 \"to our knowledge, the first\" 或 \"a detailed\"。\n- 标题: R2 认为 \"Per-Layer Residual Gating\" 过宽（仅两种变体），R1 反驳标题准确描述所测试方法。**Director 裁定: 当前标题可接受**。\n\n### SF-6 [Warning] 缺少 Rhea (arXiv:2512.06869, 2025) 引用 [AGREE: R1, R2]\n\nRole-aware Heuristic Episodic Attention，inference-time multi-turn attention 方案，与 §4.3 steering 和 §6 Discussion 直接相关。\n\n**修复**: 在 §2 \"Attention manipulation\" 段落引用，§6 与 β-steering 对比（Rhea 不需要 oracle access to goal tokens）。\n\n### SF-7 [Warning] Instruction retention 分析不显著但占 Discussion 过多篇幅 [AGREE: R1, R2]\n\nMcNemar p=0.077 不显著，r=0.200 极弱。在超页压力下应优先压缩。\n\n**修复**: 移入 Appendix 或压缩至一句（同时帮助解决 MF-2 超页问题）。\n\n---\n\n## Reviewer Consensus [AGREE]\n\n1. GAR 全称引用错误必须修正（Critical）\n2. 页数超限必须解决（Critical）\n3. AR 评估 N=5 不足以支撑核心 claim \"all collapse equally\"（Critical）\n4. Scheduled sampling 不应作为 contribution-level 声称——单种子 + 不同策略（Critical）\n5. 写作冗余需压缩，关键数字回引简化\n6. 论文是有价值的 negative result，五路对比设计超出标准消融\n7. **两位 Reviewer 均给出 3.0/5 (Findings)**\n\n---\n\n## Reviewer Divergence\n\n### 分歧 1: Exposure bias 归因严重性 [R1: Critical → R2: Should-Fix]\n\n- **R1**: 替代假说（KV cache drift, text statistics）未排除，steering 论证存在循环性，\"mechanistic analysis\" 标题要求超越相关性的因果理解\n- **R2**: 论文 hedging 适度，TRC+steering 组合提供 non-trivial evidence，negative result paper 不应等同 causal inference 标准\n- **Director 裁定**: **Should-Fix**。论文已做合理 hedging，但 KV cache drift 讨论确实过于简略。不要求额外排除实验。\n\n### 分歧 2: LoRA capacity saturation [R1: Should-Fix → R2: Minor]\n\n- **R1**: LoRA 可能已饱和 TF GAR target，\"gating 无用\"结论可能是 capacity ceiling artifact\n- **R2**: 此问题不影响核心 TF-AR gap claim——即使 LoRA 在 TF 饱和，也不解释 AR 崩溃\n- **Director 裁定**: **Minor**。R2 反驳有理——LoRA saturation 仅影响 \"gating vs LoRA-only\" 对比解读，不影响论文核心结论。在 §4.2 加一句 acknowledge 即可。\n\n---\n\n## Questions\n\n1. 如果 AR 评估扩大到 N=50，五个条件的 AR GAR 排序和 gap 大小是否保持不变？\n2. Scheduled sampling 两个种子采用不同策略（resume vs from scratch），相同策略下 3+ 种子是否可行？\n3. GAR 在 Dongre et al. 中的原始全称是 \"Goal Accessibility Ratio\"。使用 \"Goal Attention Ratio\" 是有意修改还是引用错误？\n4. β-steering 需要 oracle access to goal token positions，在实际部署中如何确定 goal tokens？\n5. \"token-level self-recovery does not extend to auxiliary objectives\" 是否是 trivially expected？论文贡献在于定量证据还是概念发现？\n6. Cross-model 评估中 \"5–8% sporadic attention spikes\" 的成因是什么？systematic behavior 还是 noise？\n\n---\n\n## Missing References\n\n1. **Rhea** (arXiv:2512.06869, Dec 2025): Role-aware Heuristic Episodic Attention，inference-time 多轮对话注意力方案 [AGREE: R1, R2]\n2. **\"Beyond Single-Turn: A Survey on Multi-Turn Interactions with LLMs\"** (arXiv:2504.04717, 2025): 多轮对话综述 [R2 提出，R1 认为可选]\n3. **Zhang et al., 2019** (\"Bridging the Gap between Training and Inference for NMT\"): exposure bias 在 NMT 中的经典分析 [R1 提出]\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n外部审稿：未请求（项目未配置外部审稿）。\n\n---\n\n## Visual Layout Check（非评分项）\n\n视觉审查已完成（0 critical, 4 warning, 12 info）。\n\n**Warnings**:\n- p3–4: Related Work + Method 连续 2 页无 figure/table，形成文字墙\n- p7: Figure 4+5 同页，Figure 5 子面板 axis label 字号过小（~55–60% 正文字号），建议放大或改为全宽 figure*\n- p8: Discussion 纯文本页，无 display item，建议加总结性表格\n- p11: Appendix 最后页 ~70% 空白，建议合并 Appendix A 内容\n\n**Info（选摘）**:\n- Figure 1 全宽概念图信息清晰，颜色区分度好\n- Table 1 booktabs 风格规范，float 位置良好\n- 全文 5 figures + 2 tables = 7 个 display items，合理\n- 无 margin 溢出、未解析引用或 LaTeX 错误残留\n\n---\n\n## Overall Assessment\n\n**Overall Score: 3.0 / 5 — Findings（可被 Findings 接收）**\n\n**Reviewer Confidence: 4/5**\n\n**Findings 而非 Conference 的核心原因**：4 个 critical must-fix 中，GAR 命名错误和超页属于格式/准确性问题可快速修复；但 AR 评估样本量不足（N=5）和 scheduled sampling 统计可靠性不足是实质性问题，需要额外实验才能解决。在补充多种子 AR 评估和 SS 实验之前，论文的统计基础不足以支撑 conference-level 接收。\n\n**达到 Findings 标准的原因**：五路对比设计精良且超出标准消融（PCGrad exclusion + TRC 正交验证），negative result 对 multi-task LLM 训练社区有实际参考价值，exposure bias 对 auxiliary loss 的选择性破坏是有意义的发现，hedging 适度。论文的实验框架和分析深度超出一般 workshop paper。\n\n**距 Conference (4.0) 的差距**：(1) AR 评估样本量和多种子覆盖需大幅加强；(2) scheduled sampling 需统计验证或从 contribution 降级；(3) 写作冗余需压缩以满足 8 页限制；(4) exposure bias 归因需更充分讨论替代假说。\n\n---\n\n## Detailed Comments\n\n### Abstract\n- \"Goal Attention Ratio\" → \"Goal Accessibility Ratio\"\n- \"Scheduled sampling compresses the gap to 1.57×\" → 加强 \"preliminary, single-seed\" 标注或移除\n\n### §1 Introduction\n- Contribution (1): 删除 \"in principle applicable to other auxiliary objective analyses\"\n- Contribution (2): \"first empirical characterization\" → \"to our knowledge, the first\" 或 \"a detailed\"\n- Contribution (2): scheduled sampling 从 contribution 降级或加强 preliminary 标注\n\n### §3.1 Preliminaries\n- \"Goal Attention Ratio\" → \"Goal Accessibility Ratio\"（全文替换）\n- 可保留说明 GAR-ours 变体聚焦 attention weight\n\n### §4.1 Setup\n- 确认 GPU 型号 \"RTX PRO 6000 Blackwell Server Edition\" 准确性\n\n### §4.2 Main Results\n- Table 1 AR 列: 扩大评估至 N≥30 + bootstrap 95% CI\n- Table 1 caption: \"GAR-O\" 缩写在首句解释\n- 加一句 acknowledge LoRA capacity saturation 替代解释\n\n### §4.3 Inference-Time Steering\n- 承认 β-steering 论证的循环性风险\n- 明确 steering 证据 + TRC 组合的 inferential scope\n\n### §5.2 PCGrad\n- \"gradient conflict\" → \"gradient direction conflict\"\n- 结论处提及 magnitude imbalance 未排除\n\n### §5.5 Cross-Model\n- 报告 mean + median 双指标\n- 展示 AR GAR 完整分布\n- 说明排除前两 turn 的理由\n- 在正文标注 3/5 条件覆盖的局限\n\n### §6 Discussion\n- Instruction retention 段落移入 Appendix（解决超页问题）\n- 加强 KV cache drift 讨论（不能仅一句带过）\n- Scheduled sampling: 标注 \"preliminary, single-seed, high-variance (GAR 0.318 vs 0.418 across two seeds)\"\n\n### §7 Conclusion\n- 数字回引简化，不重复 \"20–33×\"\n\n### Figure 4 caption\n- 删除重复句：\"the gap persists across all five variants..., the gap persists across all five tested configurations\"\n\n### Bib\n- grattafiori2024llama3: 统一作者列表格式\n- 全文 \"Goal Attention Ratio\" → \"Goal Accessibility Ratio\"",
    "reviewer_ids_acknowledged": "[\"1\", \"2\"]",
    "cross_response_reviewer_ids": "[\"1\", \"2\"]",
    "overall_score": "3.0"
  }
}
```

</details>

---


### Tool result

_source line 229 · 2026-05-22T13:08:21.356769+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_640e53b6afbbd5e34eb7273cd5a707a0:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4368
}
```

</details>

---


### Assistant

_source line 230 · 2026-05-22T13:08:31.882617+00:00_

Round 3 审稿完成，报告已投递给 Research Director。

**审稿结果摘要**：

- **Overall: 3.0/5 — Findings**（两位 Reviewer 独立给出相同评分）
- **4 个 Must-Fix**：GAR 全称错误（Goal Accessibility → Goal Attention）、正文超 8 页、AR 评估 N=5 不足、Scheduled sampling 单种子不可靠
- **7 个 Should-Fix**：exposure bias 替代假说讨论不足、cross-model 覆盖不完整、写作冗余、PCGrad scope 过度概括、contribution 措辞调整、缺 Rhea 引用、instruction retention 不显著应移入 appendix
- **1 处分歧裁定**：exposure bias 归因严重性（R1 Critical → R2 Should-Fix → Director 裁定 Should-Fix）
- **Issue Tracker 已同步**：新增 5 条 Round 3 issue，更新 10+ 条已有 issue 的 Round 3 mentions

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director"
}
```

</details>

---


## Round 20

## Round 20

42 recorded events


### User

_source line 231 · 2026-05-22T22:49:40.016506+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: turn_residual_gating
- 论文路径: projects/turn_residual_gating/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: ARR May cycle, Long paper
- 截止日期: 2026-05-25
- **引用验证**: ❌ 未启用

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 232 · 2026-05-22T22:49:46.103692+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 233 · 2026-05-22T22:49:46.204753+00:00_

1	---
2	name: review-director-session-start
3	description: Review Director session 启动初始化流程——圆桌多轮审稿协议。Review Director 角色 session 启动时自动使用。
4	priority: 9
5	scope: global
6	tags:
7	- workflow
8	- review
9	- session
10	version: 3
11	roles:
12	- review_director
13	---
14	
15	# Review Director Session 启动流程（圆桌会议模式）
16	
17	## 初始化
18	
19	1. `director_get_project_overview(project)` — 了解研究现状（实验状态、最新报告）
20	2. 读取论文文件状态：检查 `projects/{project}/paper/` 或 `main.tex` 是否存在
21	3. 检查是否有来自 Research Director 的论文提交（`[论文提交]` 消息）
22	4. 向用户简要汇报：
23	   - **投稿目标**：venue 和 deadline
24	   - **论文状态**：当前草稿位置和版本
25	   - **资料完整性**：提交的材料是否齐全
26	   - **下一步**：即将开始的圆桌审稿流程
27	
28	## 评审流程（收到论文提交后执行）
29	
30	### Step 0 — 资料检查 + Venue 调研（必须先做，不可跳过）
31	
32	1. 检查提交资料完整性：论文文件是否存在、是否可读、补充材料是否齐全
33	2. 确认目标投稿 venue（从提交消息中获取）
34	3. 用 `web_search` 搜索该 venue 当前轮次的 CFP（Call for Papers），关键词示例：
35	   - `"&lt;venue name> 2026 call for papers" site:aclweb.org`
36	   - `"&lt;venue name> 2026 submission deadline"`
37	   - `"&lt;venue name> 2026 author guidelines"`
38	4. **验证 deadline 未过期**：今天日期与截止日期对比，若已过期立即通知用户，不继续
39	5. 提取当前版本的格式要求：
40	   - 页数限制（正文 / 附录 / 参考文献）
41	   - 模板（ACL / IEEE / NeurIPS / ICML / ...）
42	   - 匿名规则（double-blind / single-blind / open）
43	   - 附录规则（是否允许、是否参与审稿）
44	   - 引用格式（natbib / biblatex / 特定 .bst）
45	6. 将以上信息作为上下文，随任务一起传递给 Reviewer
46	
47	⚠️ 禁止使用训练知识中的 venue 要求——格式标准每年都会更新，必须实时搜索确认。
48	
49	### Step 0.5 — 决定 Reviewer 编排
50	
51	根据 venue 类型和论文特点，决定：
52	- 需要几个 Reviewer（1-5 人）
53	- 每个 Reviewer 的审查侧重
54	
55	参考：
56	- **顶会长文**（NeurIPS/ICML/ACL）：3 人（方法/实验 + novelty/related work + 格式/ethics）
57	- **一般会议**（EMNLP/NAACL）：2 人（方法严谨性 + 新颖性/完整性）
58	- **Workshop / 短文**：1 人（全面审查）
59	
60	向 Group C（即项目配置中的 `feishu.review_chat_id` 审稿群）汇报编排决定。
61	
62	### Step 0.6 — 外部审稿线（与 Step 1 并行）
63	
64	检查项目配置中 `external_review.paperreview_ai.enabled` 是否为 `true`：
65	- 如果启用：调用 `request_external_review(project, paper_pdf_path, venue)` 向用户群发送协助提交卡片
66	- 这一步与 Step 1（内部 Reviewer 分配）**并行执行**，不阻塞内部审稿流程
67	- 外部结果到达后（用户在群里粘贴），纳入 Step 4 最终报告
68	- 如果到 Ste
…[truncated 3286 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "Read",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 234 · 2026-05-22T22:49:54.941959+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 235 · 2026-05-22T22:49:54.942390+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 236 · 2026-05-22T22:50:00.062569+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "turn_residual_gating"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "turn_residual_gating"
  }
}
```

</details>

---


### Tool result

_source line 237 · 2026-05-22T22:50:01.920101+00:00_

{"result":"# 项目 turn_residual_gating 概况\n\n## 实验状态 (39 个)\n\n- **phase2_tg_s42_v7**: DONE (success) — \n- **phase2_tg_s42_v9_pcgrad**: DONE (success) — \n- **phase2_lora_only_s42**: DONE (success) — \n- **phase2_ug_s42**: DONE (success) — \n- **phase2_tg_s42_v8_schedsampling**: DONE (failed) — \n- **analysis_attention_heatmap**: DONE (success) — \n- **analysis_gradient_conflict**: DONE (success) — \n- **phase2_4way_eval_heldout**: DONE (success) — \n- **phase2_4way_eval**: DONE (negative) — \n- **phase2_tg_s42_v5**: DONE (negative) — \n- **phase2_tg_s42_v4**: DONE (failed) — \n- **phase2_tg_s42_v3b**: DONE (success) — \n- **phase2_tg_s42_v3**: DONE (negative) — \n- **phase2_tg_s42_v2**: DONE (killed) — \n- **phase1_gar_diag**: DONE (success) — \n\n## 最新报告\n&lt;!-- AUTO-FACTS-BEGIN (generated 2026-05-22T15:51:55Z; do not edit — regenerated by auto_build_report_facts) -->\n## 📊 当前状态（auto-derived from registry）\n\n**总计**: 38 个实验 — DONE 37, PREPARING 1\n**DONE 分布**: failed 4, killed 1, negative 5, success 27\n\n### 💾 磁盘余量\n- **westd-20861**:\n  - `/init`: 150M/150M 可用（已用 1%）\n  - `/autodl-pub`: 5.3T/7.3T 可用（已用 24%）\n  - `/usr/bin/nvidia-smi`: 430G/879G 可用（已用 49%）\n\n### 🏃 RUNNING\n_（无）_\n\n### 📌 最近完成 (top 5)\n- `d048_ss_s42` [failed] — 2026-05-22T15:51:54 — CUDA OOM: CUDA out of memory. Tried to allocate 424.00 MiB. GPU 0 has a total ca\n- `eval_llama_ar_n20` [success] — 2026-05-22T08:38:33\n- `eval_llama_lora_only_s42` [success] — 2026-05-22T07:51:32\n- `llama_lora_only_s42` [success] — 2026-05-22T07:39:06\n- `phase2_tg_s42_v6` [negative] — 2026-05-22T04:37:13\n\n### 🔴 最近失败原因 (top 3)\n- `d048_ss_s42`: CUDA OOM: CUDA out of memory. Tried to allocate 424.00 MiB. GPU 0 has a total capacity of 94.97 GiB of which 218.56 MiB is free. Including non-PyTorch memory, this process has 26.13 GiB memory in use.\n\n&lt;!-- AUTO-FACTS-END -->\n\n---\n\n# Handover — 2026-05-22\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n- llama_tg_training（准备中）\n\n## 近期结论\n- **d048_ss_s4
…[truncated 1122 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 1857
}
```

</details>

---


### Tool call

_source line 238 · 2026-05-22T22:50:02.522848+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/main.tex 2>/dev/null && echo \"MAIN_TEX_EXISTS\" || echo \"MAIN_TEX_MISSING\"",
  "description": "Check paper main.tex existence"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/main.tex 2>/dev/null && echo \"MAIN_TEX_EXISTS\" || echo \"MAIN_TEX_MISSING\"",
    "description": "Check paper main.tex existence"
  }
}
```

</details>

---


### Tool result

_source line 239 · 2026-05-22T22:50:03.477702+00:00_

-rw-r--r-- 1 ubuntu ubuntu 907 May 22 16:08 /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/main.tex
MAIN_TEX_EXISTS

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "Bash",
  "elapsed_ms": 954
}
```

</details>

---


### Tool call

_source line 240 · 2026-05-22T22:50:03.980615+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_3/submitted.pdf 2>/dev/null && echo \"PDF_EXISTS\" || echo \"PDF_MISSING\"",
  "description": "Check submitted PDF existence"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_3/submitted.pdf 2>/dev/null && echo \"PDF_EXISTS\" || echo \"PDF_MISSING\"",
    "description": "Check submitted PDF existence"
  }
}
```

</details>

---


### Tool result

_source line 241 · 2026-05-22T22:50:04.231984+00:00_

-rw-r--r-- 1 ubuntu ubuntu 612729 May 22 17:48 /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_3/submitted.pdf
PDF_EXISTS

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "Bash",
  "elapsed_ms": 251
}
```

</details>

---


### Tool call

_source line 242 · 2026-05-22T22:50:04.232330+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebSearch",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebSearch",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 243 · 2026-05-22T22:50:04.283072+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 244 · 2026-05-22T22:50:14.737748+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 ARR call for papers submission guidelines page limit",
  "allowed_domains": "['aclweb.org', 'openreview.net', '2026.emnlp.org']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 ARR call for papers submission guidelines page limit",
    "allowed_domains": "['aclweb.org', 'openreview.net', '2026.emnlp.org']"
  }
}
```

</details>

---


### Tool call

_source line 245 · 2026-05-22T22:50:14.788377+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review 2026 May cycle submission deadline author guidelines",
  "allowed_domains": "['aclweb.org', 'openreview.net']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review 2026 May cycle submission deadline author guidelines",
    "allowed_domains": "['aclweb.org', 'openreview.net']"
  }
}
```

</details>

---


### Tool call

_source line 246 · 2026-05-22T22:50:15.290400+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "turn_residual_gating",
  "file": "review_issues.yaml",
  "max_chars": "0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "turn_residual_gating",
    "file": "review_issues.yaml",
    "max_chars": "0"
  }
}
```

</details>

---


### Tool result

_source line 247 · 2026-05-22T22:50:19.135598+00:00_

Web search results for query: "EMNLP 2026 ARR call for papers submission guidelines page limit"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"EMNLP 2026 Conference | OpenReview","url":"https://openreview.net/group?id=EMNLP%2F2026%2FConference"},{"title":"EACL 2026: First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eacl-2026-first-call-papers"},{"title":"EMNLP 2026 Workshop NLLP ARR Commitment | OpenReview","url":"https://openreview.net/group?id=EMNLP%2F2026%2FWorkshop%2FNLLP_ARR_Commitment"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"EACL/ACL 2026 Joint Call for Workshops | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eaclacl-2026-joint-call-workshops"},{"title":"Call for Papers: The 20th Linguistic Annotation Workshop (LAW XX), co-located with ACL 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/call-papers-20th-linguistic-annotation-workshop-law-xx-co-located-acl-2026"},{"title":"EMNLP 2026 Workshop WiNLP ARR Commitment | OpenReview","url":"https://openreview.net/group?id=EMNLP%2F2026%2FWorkshop%2FWiNLP_ARR_Commitment"},{"title":"[EMNLP 2025] First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2025-first-call-papers"},{"title":"EMNLP 2025: Call for System Demonstrations | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2025-call-system-demonstrations"}]

Based on the search results, I found information about EMNLP 2026 and ARR submission guidelines. However, the specific page limit information for EMNLP 2026 main conference papers was not included in the first search result's content snippet. The EMNLP 2026 Call for Main Conference Papers indicates that papers must be submitted thr
…[truncated 536 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "WebSearch",
  "elapsed_ms": 4397
}
```

</details>

---


### Tool result

_source line 248 · 2026-05-22T22:50:22.046501+00:00_

Web search results for query: "ACL Rolling Review 2026 May cycle submission deadline author guidelines"

Links: [{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"ACL Rolling Review | ACL Member Portal","url":"https://www.aclweb.org/portal/content/acl-rolling-review"},{"title":"Authorship Changes Policy for ACL Venue Papers - Admin Wiki","url":"https://www.aclweb.org/adminwiki/index.php/Authorship_Changes_Policy_for_ACL_Venue_Papers"},{"title":"ACL ARR 2026 January | OpenReview","url":"https://openreview.net/group?id=aclweb.org%2FACL%2FARR%2F2026%2FJanuary"},{"title":"ACL ARR | OpenReview","url":"https://openreview.net/group?id=aclweb.org%2FACL%2FARR"},{"title":"ACL Policies for Review and Citation - Admin Wiki","url":"https://www.aclweb.org/adminwiki/index.php/ACL_Policies_for_Review_and_Citation"},{"title":"EACL 2026: First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eacl-2026-first-call-papers"},{"title":"ACL ARR 2026 May | OpenReview","url":"https://openreview.net/group?id=aclweb.org%2FACL%2FARR%2F2026%2FMay"},{"title":"ACL Policy on Publication Ethics - Admin Wiki","url":"https://www.aclweb.org/adminwiki/index.php/ACL_Policy_on_Publication_Ethics"},{"title":"ACL ARR 2025 May | OpenReview","url":"https://openreview.net/group?id=aclweb.org%2FACL%2FARR%2F2025%2FMay"}]

Based on the web search results, here's information about the ACL Rolling Review 2026 May cycle:

## Submission Deadline

ACL Rolling Review has a deadline on the 15th of each month, which means the May 2026 submission deadline would be May 15, 2026.

## Author Guidelines and Requirements

ACL 2026 invites the submission of long and short papers featuring substantial, original, and unpublished research in all aspects of Computational Linguistics and Natural Language Processing.

In addition to traditional research results, papers may contribute negative findings, survey an area, announce the creation o
…[truncated 1178 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "WebSearch",
  "elapsed_ms": 7258
}
```

</details>

---


### Tool result

_source line 249 · 2026-05-22T22:50:22.046977+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"file must be one of ['ARCHITECTURE.md', 'DATA.md', 'EVALUATION.md', 'MODELS.md', 'ROADMAP.md', 'constraints.yaml', 'decisions.yaml', 'ideas.md', 'literature_map.yaml', 'memory.md', 'mistakes.yaml', 'paper_checklist.yaml', 'paper_framing.md', 'paper_provenance.yaml', 'report.md', 'writing_plan.yaml'], got 'review_issues.yaml'\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 6756
}
```

</details>

---


### Tool call

_source line 250 · 2026-05-22T22:50:26.415623+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review 2026 submission guidelines long paper page limit template anonymity"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review 2026 submission guidelines long paper page limit template anonymity"
  }
}
```

</details>

---


### Tool call

_source line 251 · 2026-05-22T22:50:28.320907+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_issues.yaml"
  }
}
```

</details>

---


### Tool result

_source line 252 · 2026-05-22T22:50:28.672551+00:00_

1	# Review Issues Tracker — turn_residual_gating
2	# Round 1 (2026-05-19, dream_20260519T145320)
3	# Round 2 (2026-05-22, fresh re-review of revised paper)
4	# Round 3 (2026-05-22, fresh re-review — current round)
5	
6	# ============================================================
7	# Issues from Round 1 — status updates through Round 3
8	# ============================================================
9	
10	- id: "R1-N1"
11	  summary: "所有引用渲染为 '?'——bibliography 编译失败"
12	  category: format
13	  severity: info
14	  status: resolved
15	  first_raised_round: 1
16	  last_seen_round: 1
17	  mentions:
18	    - round: 1
19	      reviewers: [1, 2]
20	      note: "Dream paper artifact。"
21	    - round: 2
22	      reviewers: []
23	      note: "视觉审查确认无 [?] 未解析引用。已修复。"
24	    - round: 3
25	      reviewers: []
26	      note: "Round 3 视觉审查确认无未解析引用。维持 resolved。"
27	  action_items:
28	    - round: 1
29	      action: "Paper Agent 确保 bibtex 编译正确"
30	      assigned_to: paper_agent
31	      status: done
32	  resolution: "Round 2 视觉审查确认已修复。"
33	  resolution_round: 2
34	
35	- id: "R1-N2"
36	  summary: "单种子支撑结论——统计功效不足 + AR 评估 N=5 过小"
37	  category: experiment
38	  severity: critical
39	  status: in_progress
40	  first_raised_round: 1
41	  last_seen_round: 3
42	  mentions:
43	    - round: 1
44	      reviewers: [1, 2]
45	      note: "Bootstrap CI 仅覆盖 eval variance，不覆盖 training variance。"
46	    - round: 2
47	      reviewers: [1, 2]
48	      note: "ThreadGate 已补 seed=123，但其余 4/5 条件仍为单 seed。SS 仅 1 seed 且第二 seed 协议不同不可比。"
49	    - round: 3
50	      reviewers: [1, 2]
51	      note: "AR 评估仅 N=5，核心 claim 'all variants collapse equally' 缺统计检验。两位 Reviewer 独立列为 Critical Must-Fix。"
52	  action_items:
53	    - round: 1
54	      action: "plan_019: seed=123 extra training"
55	      assigned_to: agent
56	      status: done
57	    - round: 2
58	      action: "D048: 6 条件 × 3 seeds from-scratch"
59	      assigned_to: agent
60	      status: in_progress
61	    - round: 3
62	      action: "AR 评估扩大至 N=50（5 Qwen 
…[truncated 19903 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "Read",
  "elapsed_ms": 351
}
```

</details>

---


### Tool call

_source line 253 · 2026-05-22T22:50:28.672916+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_local_file",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_local_file",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 254 · 2026-05-22T22:50:28.773393+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "ToolSearch",
  "elapsed_ms": 100
}
```

</details>

---


### Tool result

_source line 255 · 2026-05-22T22:50:32.485525+00:00_

Web search results for query: "ACL Rolling Review 2026 submission guidelines long paper page limit template anonymity"

Links: [{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"EACL 2026: First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eacl-2026-first-call-papers"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"ACL Rolling Review | ACL Member Portal","url":"https://www.aclweb.org/portal/content/acl-rolling-review"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"Paper formatting guidelines - ACLPUB","url":"https://acl-org.github.io/ACLPUB/formatting.html"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"}]

Based on the search results for ACL Rolling Review 2026, here are the key submission guidelines:

## Page Limits

Review versions of long papers may have up to eight (8) pages of content plus unlimited pages for references. Upon acceptance, final versions of long papers will be given one additional page – up to nine (9) pages of content plus unlimited pages for acknowledgments and references – so that reviewers' comments can be taken into account.

## Anonymity

Papers must not include authors' names and affiliations. Furthermore, self-references that reveal the authors' identities, e.g., "We previously showed (Smith, 1991)…" mus
…[truncated 573 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "WebSearch",
  "elapsed_ms": 6069
}
```

</details>

---


### Tool call

_source line 256 · 2026-05-22T22:50:50.463156+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_3/submitted.pdf",
  "pages": "1-10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_3/submitted.pdf",
    "pages": "1-10"
  }
}
```

</details>

---


### Tool call

_source line 257 · 2026-05-22T22:50:50.463724+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "turn_residual_gating"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "turn_residual_gating"
  }
}
```

</details>

---


### Tool result

_source line 258 · 2026-05-22T22:50:51.121198+00:00_

PDF pages extracted: 10 page(s) from /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_3/submitted.pdf (598.4KB)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "Read",
  "elapsed_ms": 658
}
```

</details>

---


### Tool result

_source line 259 · 2026-05-22T22:50:51.343592+00:00_

{"result":"# 项目 turn_residual_gating 概况\n\n## 实验状态 (39 个)\n\n- **phase2_tg_s42_v7**: DONE (success) — \n- **phase2_tg_s42_v9_pcgrad**: DONE (success) — \n- **phase2_lora_only_s42**: DONE (success) — \n- **phase2_ug_s42**: DONE (success) — \n- **phase2_tg_s42_v8_schedsampling**: DONE (failed) — \n- **analysis_attention_heatmap**: DONE (success) — \n- **analysis_gradient_conflict**: DONE (success) — \n- **phase2_4way_eval_heldout**: DONE (success) — \n- **phase2_4way_eval**: DONE (negative) — \n- **phase2_tg_s42_v5**: DONE (negative) — \n- **phase2_tg_s42_v4**: DONE (failed) — \n- **phase2_tg_s42_v3b**: DONE (success) — \n- **phase2_tg_s42_v3**: DONE (negative) — \n- **phase2_tg_s42_v2**: DONE (killed) — \n- **phase1_gar_diag**: DONE (success) — \n\n## 最新报告\n&lt;!-- AUTO-FACTS-BEGIN (generated 2026-05-22T15:51:55Z; do not edit — regenerated by auto_build_report_facts) -->\n## 📊 当前状态（auto-derived from registry）\n\n**总计**: 38 个实验 — DONE 37, PREPARING 1\n**DONE 分布**: failed 4, killed 1, negative 5, success 27\n\n### 💾 磁盘余量\n- **westd-20861**:\n  - `/init`: 150M/150M 可用（已用 1%）\n  - `/autodl-pub`: 5.3T/7.3T 可用（已用 24%）\n  - `/usr/bin/nvidia-smi`: 430G/879G 可用（已用 49%）\n\n### 🏃 RUNNING\n_（无）_\n\n### 📌 最近完成 (top 5)\n- `d048_ss_s42` [failed] — 2026-05-22T15:51:54 — CUDA OOM: CUDA out of memory. Tried to allocate 424.00 MiB. GPU 0 has a total ca\n- `eval_llama_ar_n20` [success] — 2026-05-22T08:38:33\n- `eval_llama_lora_only_s42` [success] — 2026-05-22T07:51:32\n- `llama_lora_only_s42` [success] — 2026-05-22T07:39:06\n- `phase2_tg_s42_v6` [negative] — 2026-05-22T04:37:13\n\n### 🔴 最近失败原因 (top 3)\n- `d048_ss_s42`: CUDA OOM: CUDA out of memory. Tried to allocate 424.00 MiB. GPU 0 has a total capacity of 94.97 GiB of which 218.56 MiB is free. Including non-PyTorch memory, this process has 26.13 GiB memory in use.\n\n&lt;!-- AUTO-FACTS-END -->\n\n---\n\n# Handover — 2026-05-22\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n- llama_tg_training（准备中）\n\n## 近期结论\n- **d048_ss_s4
…[truncated 1122 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 879
}
```

</details>

---


### Tool call

_source line 260 · 2026-05-22T22:51:55.129963+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "turn_residual_gating"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "turn_residual_gating"
  }
}
```

</details>

---


### Tool result

_source line 261 · 2026-05-22T22:51:55.531306+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 401
}
```

</details>

---


### Tool call

_source line 262 · 2026-05-22T22:51:56.987124+00:00_

called mcp__agent-ml-research__dispatch_visual_check

<details open><summary>🔧 Tool call — mcp__agent-ml-research__dispatch_visual_check</summary>

```json
{
  "project": "turn_residual_gating",
  "review_chat_id": "oc_9287ee173cf15d688adcd081f5d861f5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "tool_args": {
    "project": "turn_residual_gating",
    "review_chat_id": "oc_9287ee173cf15d688adcd081f5d861f5"
  }
}
```

</details>

---


### Tool result

_source line 263 · 2026-05-22T22:52:16.890600+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 19903
}
```

</details>

---


### Tool call

_source line 264 · 2026-05-22T22:52:17.041911+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "## 审稿任务 — Round 1\n\n**论文**：Why Per-Layer Residual Gating Fails to Fix Multi-Turn Attention Degradation: A Mechanistic Analysis\n**PDF 路径**：`/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_3/submitted.pdf`\n**LaTeX 路径**：`projects/turn_residual_gating/paper/main.tex`（sections 在 `paper/sections/` 下）\n\n### Venue 要求\n- **目标 venue**：EMNLP 2026（ARR May cycle）\n- **截止日期**：2026-05-25\n- **页数限制**：正文 8 页（不含 references、limitations、ethical considerations）\n- **模板**：ACL/ARR 标准模板\n- **匿名规则**：Double-blind（论文中不能出现作者姓名和机构信息）\n- **附录**：允许，参与审稿\n\n### 你的审查侧重：方法严谨性 + 实验设计\n\n请重点检查以下方面：\n\n1. **实验方法论**：\n   - 五路对比设计（ThreadGate, +PCGrad, Uniform Gate, LoRA-only, Base）是否公平、变量控制是否到位\n   - 训练和评估 protocol 的合理性（数据集选择、超参数、训练 epoch 等）\n   - GAR 指标定义和测量方法是否严谨（GAR-ours vs GAR-Dongre 的区分）\n\n2. **统计有效性**：\n   - 种子数量是否充分（论文使用 seed=42 + seed=123 for ThreadGate，其他条件单种子）\n   - AR 评估的样本量（N=5 for Qwen, N=20 for Llama）是否支撑结论\n   - 置信区间、显著性检验是否到位\n   - Scheduled sampling 的单种子证据是否足够\n\n3. **消融完整性**：\n   - PCGrad 排除实验是否足以排除梯度冲突假说\n   - 门控反转（§5.1）和推理时注意力偏置（§4.3）的论证逻辑\n   - 跨模型验证（Llama-3.1-8B）仅覆盖 3/5 条件是否足够\n   - Exposure bias 归因是否排除了其他替代假说（如 KV cache drift）\n\n4. **技术正确性**：\n   - 数学公式（Eq. 1-7）是否正确\n   - 梯度冲突分析（§5.2）的方法和结论\n   - TRC 分析（§5.4）的设计合理性\n\n5. **可复现性**：\n   - 超参数是否完整报告\n   - 代码/数据是否承诺发布\n\n请按照 ARR 标准评审格式输出审稿意见：Summary → Strengths → Weaknesses → Questions → Missing References → Overall Assessment（含评分和置信度）。\n\nWeaknesses 按严重程度分级：Critical Must-Fix / Should-Fix / Minor。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "text": "## 审稿任务 — Round 1\n\n**论文**：Why Per-Layer Residual Gating Fails to Fix Multi-Turn Attention Degradation: A Mechanistic Analysis\n**PDF 路径**：`/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_3/submitted.pdf`\n**LaTeX 路径**：`projects/turn_residual_gating/paper/main.tex`（sections 在 `paper/sections/` 下）\n\n### Venue 要求\n- **目标 venue**：EMNLP 2026（ARR May cycle）\n- **截止日期**：2026-05-25\n- **页数限制**：正文 8 页（不含 references、limitations、ethical considerations）\n- **模板**：ACL/ARR 标准模板\n- **匿名规则**：Double-blind（论文中不能出现作者姓名和机构信息）\n- **附录**：允许，参与审稿\n\n### 你的审查侧重：方法严谨性 + 实验设计\n\n请重点检查以下方面：\n\n1. **实验方法论**：\n   - 五路对比设计（ThreadGate, +PCGrad, Uniform Gate, LoRA-only, Base）是否公平、变量控制是否到位\n   - 训练和评估 protocol 的合理性（数据集选择、超参数、训练 epoch 等）\n   - GAR 指标定义和测量方法是否严谨（GAR-ours vs GAR-Dongre 的区分）\n\n2. **统计有效性**：\n   - 种子数量是否充分（论文使用 seed=42 + seed=123 for ThreadGate，其他条件单种子）\n   - AR 评估的样本量（N=5 for Qwen, N=20 for Llama）是否支撑结论\n   - 置信区间、显著性检验是否到位\n   - Scheduled sampling 的单种子证据是否足够\n\n3. **消融完整性**：\n   - PCGrad 排除实验是否足以排除梯度冲突假说\n   - 门控反转（§5.1）和推理时注意力偏置（§4.3）的论证逻辑\n   - 跨模型验证（Llama-3.1-8B）仅覆盖 3/5 条件是否足够\n   - Exposure bias 归因是否排除了其他替代假说（如 KV cache drift）\n\n4. **技术正确性**：\n   - 数学公式（Eq. 1-7）是否正确\n   - 梯度冲突分析（§5.2）的方法和结论\n   - TRC 分析（§5.4）的设计合理性\n\n5. **可复现性**：\n   - 超参数是否完整报告\n   - 代码/数据是否承诺发布\n\n请按照 ARR 标准评审格式输出审稿意见：Summary → Strengths → Weaknesses → Questions → Missing References → Overall Assessment（含评分和置信度）。\n\nWeaknesses 按严重程度分级：Critical Must-Fix / Should-Fix / Minor。"
  }
}
```

</details>

---


### Tool result

_source line 265 · 2026-05-22T22:52:35.136745+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 18094
}
```

</details>

---


### Tool call

_source line 266 · 2026-05-22T22:52:35.290634+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "## 审稿任务 — Round 1\n\n**论文**：Why Per-Layer Residual Gating Fails to Fix Multi-Turn Attention Degradation: A Mechanistic Analysis\n**PDF 路径**：`/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_3/submitted.pdf`\n**LaTeX 路径**：`projects/turn_residual_gating/paper/main.tex`（sections 在 `paper/sections/` 下）\n\n### Venue 要求\n- **目标 venue**：EMNLP 2026（ARR May cycle）\n- **截止日期**：2026-05-25\n- **页数限制**：正文 8 页（不含 references、limitations、ethical considerations）\n- **模板**：ACL/ARR 标准模板\n- **匿名规则**：Double-blind（论文中不能出现作者姓名和机构信息）\n- **附录**：允许，参与审稿\n\n### 你的审查侧重：新颖性 + 写作完整性\n\n请重点检查以下方面：\n\n1. **Novelty 评估**：\n   - 论文的核心贡献（exposure bias 归因 + 五路诊断框架 + β-steering）是否足够新颖\n   - 与 Li et al. (2024) split-softmax、Rhea (Hong et al., 2025)、StreamingLLM 等最相近工作的区分度\n   - 负面结果论文（gating 无效）的 novelty 标准是否达标\n   - \"to our knowledge, the first\" 等声称是否合理\n\n2. **Related Work 覆盖**：\n   - 多轮对话退化文献是否完整（Dongre et al., Laban et al., Liu et al., Bai et al.）\n   - 注意力操控文献（StreamingLLM, Rhea, split-softmax）是否全面\n   - Exposure bias 文献（Bengio et al., Arora et al., He et al., SEARNN, Professor Forcing）\n   - 是否遗漏重要直接竞争者\n\n3. **写作质量**：\n   - 论证逻辑是否清晰（观察 → 干预 → 失败 → 诊断 → 根因）\n   - 是否有 overclaim（标题、abstract、contribution list）\n   - 关键数字（20-33× gap 等）是否重复过多\n   - Figure/Table caption 是否准确、不含 causal overclaim\n   - 术语一致性（GAR-ours, GAR-Dongre, Goal Accessibility Ratio 全称是否正确）\n\n4. **格式合规**：\n   - 正文是否在 8 页限制内（检查 §7 Conclusion 是否在第 8 页结束）\n   - 匿名性（是否暴露作者信息）\n   - 引用格式（natbib, bib 条目完整性和一致性）\n   - Limitations 章节是否存在且内容适当（ARR 必须有）\n   - Figure/Table 编号和引用是否正确\n\n5. **Contribution 声称**：\n   - 四条 contribution（诊断框架 + exposure bias 刻画 + β-steering + 负面 baseline）的合理性\n   - 是否有泛化声称（\"in principle applicable\" 等）超出实验范围\n   - Conclusion 是否准确反映实际发现\n\n请按照 ARR 标准评审格式输出审稿意见：Summary → Strengths → Weaknesses → Questions → Missing References → Overall Assessment（含评分和置信度）。\n\nWeaknesses 按严重程度分级：Critical Must-Fix / Should-Fix / Minor。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "text": "## 审稿任务 — Round 1\n\n**论文**：Why Per-Layer Residual Gating Fails to Fix Multi-Turn Attention Degradation: A Mechanistic Analysis\n**PDF 路径**：`/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_round_3/submitted.pdf`\n**LaTeX 路径**：`projects/turn_residual_gating/paper/main.tex`（sections 在 `paper/sections/` 下）\n\n### Venue 要求\n- **目标 venue**：EMNLP 2026（ARR May cycle）\n- **截止日期**：2026-05-25\n- **页数限制**：正文 8 页（不含 references、limitations、ethical considerations）\n- **模板**：ACL/ARR 标准模板\n- **匿名规则**：Double-blind（论文中不能出现作者姓名和机构信息）\n- **附录**：允许，参与审稿\n\n### 你的审查侧重：新颖性 + 写作完整性\n\n请重点检查以下方面：\n\n1. **Novelty 评估**：\n   - 论文的核心贡献（exposure bias 归因 + 五路诊断框架 + β-steering）是否足够新颖\n   - 与 Li et al. (2024) split-softmax、Rhea (Hong et al., 2025)、StreamingLLM 等最相近工作的区分度\n   - 负面结果论文（gating 无效）的 novelty 标准是否达标\n   - \"to our knowledge, the first\" 等声称是否合理\n\n2. **Related Work 覆盖**：\n   - 多轮对话退化文献是否完整（Dongre et al., Laban et al., Liu et al., Bai et al.）\n   - 注意力操控文献（StreamingLLM, Rhea, split-softmax）是否全面\n   - Exposure bias 文献（Bengio et al., Arora et al., He et al., SEARNN, Professor Forcing）\n   - 是否遗漏重要直接竞争者\n\n3. **写作质量**：\n   - 论证逻辑是否清晰（观察 → 干预 → 失败 → 诊断 → 根因）\n   - 是否有 overclaim（标题、abstract、contribution list）\n   - 关键数字（20-33× gap 等）是否重复过多\n   - Figure/Table caption 是否准确、不含 causal overclaim\n   - 术语一致性（GAR-ours, GAR-Dongre, Goal Accessibility Ratio 全称是否正确）\n\n4. **格式合规**：\n   - 正文是否在 8 页限制内（检查 §7 Conclusion 是否在第 8 页结束）\n   - 匿名性（是否暴露作者信息）\n   - 引用格式（natbib, bib 条目完整性和一致性）\n   - Limitations 章节是否存在且内容适当（ARR 必须有）\n   - Figure/Table 编号和引用是否正确\n\n5. **Contribution 声称**：\n   - 四条 contribution（诊断框架 + exposure bias 刻画 + β-steering + 负面 baseline）的合理性\n   - 是否有泛化声称（\"in principle applicable\" 等）超出实验范围\n   - Conclusion 是否准确反映实际发现\n\n请按照 ARR 标准评审格式输出审稿意见：Summary → Strengths → Weaknesses → Questions → Missing References → Overall Assessment（含评分和置信度）。\n\nWeaknesses 按严重程度分级：Critical Must-Fix / Should-Fix / Minor。"
  }
}
```

</details>

---


### Tool result

_source line 267 · 2026-05-22T22:52:36.868669+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1578
}
```

</details>

---


### Tool call

_source line 268 · 2026-05-22T22:52:59.907618+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/agent/config.yaml 2>/dev/null | grep -A 5 \"external_review\" || echo \"NO_EXTERNAL_REVIEW_CONFIG\"",
  "description": "Check external review config"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/agent/config.yaml 2>/dev/null | grep -A 5 \"external_review\" || echo \"NO_EXTERNAL_REVIEW_CONFIG\"",
    "description": "Check external review config"
  }
}
```

</details>

---


### Tool result

_source line 269 · 2026-05-22T22:53:00.108745+00:00_

NO_EXTERNAL_REVIEW_CONFIG

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "Bash",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 270 · 2026-05-22T22:53:04.725753+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating -name \"*.yaml\" -o -name \"*.yml\" | head -20 && echo \"---\" && grep -r \"external_review\\|paperreview\" /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/agent/ 2>/dev/null | head -5 || echo \"NOT_FOUND\"",
  "description": "Search for external review config"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating -name \"*.yaml\" -o -name \"*.yml\" | head -20 && echo \"---\" && grep -r \"external_review\\|paperreview\" /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/agent/ 2>/dev/null | head -5 || echo \"NOT_FOUND\"",
    "description": "Search for external review config"
  }
}
```

</details>

---


### Tool result

_source line 271 · 2026-05-22T22:53:04.776558+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/distill_tmp/bai2024mt.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/distill_tmp/sirdeshmukh2025multichallenge.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/distill_tmp/xiao2024efficient.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/distill_tmp/liu2023lost.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/distill_tmp/wang2018skipnet.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/distill_tmp/peng2024yarn.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/distill_tmp/schuster2022confident.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/distill_tmp/han2024lm.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/distill_tmp/li2024measuring.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/distill_tmp/bengio2015scheduled.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/distill_tmp/luo2025adaptive.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/distill_tmp/ko2024found.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/distill_tmp/fan2020reducing.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/distill_tmp/ildiz2024self.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/distill_tmp/sun2025curse.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/distill_tmp/dubois2024length.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/distill_tmp/chiang2024chatbot.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/distill_tmp/ranz
…[truncated 252 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Assistant

_source line 272 · 2026-05-22T22:53:14.827761+00:00_

外部审稿未在项目中配置，跳过。

当前状态：
- Reviewer 1（方法严谨性）：审稿中
- Reviewer 2（新颖性+完整性）：审稿中
- 视觉审查 Agent：运行中
- 外部审稿：未配置，跳过

等待 Reviewer 返回审稿意见。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director"
}
```

</details>

---


## Round 21

## Round 21

2 recorded events


### User

_source line 273 · 2026-05-22T23:00:13.879688+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 审稿意见 — Round 1

**论文**：Why Per-Layer Residual Gating Fails to Fix Multi-Turn Attention Degradation: A Mechanistic Analysis

---

## Summary

本文提出 ThreadGate，一种在 transformer 每层残差路径上添加 content-and-turn-conditioned MLP gate 的方法，目标是恢复多轮对话中衰减的 system prompt 注意力（GAR）。通过五路对照实验（ThreadGate / +PCGrad / Uniform Gate / LoRA-only / Base），作者发现在 teacher-forced 条件下 GAR 收敛至目标值 0.50，但自回归生成时 GAR 坍塌至 0.015–0.025（20–33× gap）。论文进一步通过 PCGrad 排除梯度方向冲突、通过 gate 值分析排除架构缺陷，将失败归因于 exposure bias：辅助注意力损失在 teacher-forcing 下优化的模式无法迁移到自回归推理。β-steering（β=5）将 GAR 从 0.064 恢复至 0.727，scheduled sampling（单 seed）将 gap 从 31× 压缩至 1.57×。跨模型验证在 Llama-3.1-8B 上确认了 27× gap。

---

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | 五路对照和 PCGrad 排除实验方法论严谨，主要 claims 有充分支撑。但 GAR 与下游任务性能的关联未被验证（p=0.077 不显著），scheduled sampling 仅单 seed，削弱了部分结论的可靠性。 |
| Excitement | 3/5 | 负面结果 + 暴露偏差归因对社区有参考价值，但论文最终未提供一个可工作的解决方案。β-steering 需要预知 goal token 位置，scheduled sampling 是初步结果。实际影响有限。 |
| Reproducibility | 4/5 | 超参数文档完整（Appendix A），模型和数据集均公开可获取，seed 已指定。但未提及是否开源代码。 |
| Confidence | 4/5 | 仔细阅读了全文，熟悉注意力操控、多任务学习、exposure bias 相关文献。 |

---

## 主要优势

**S1. 实验设计严谨的五路对照框架。** 每对配置精确隔离一个因素（turn conditioning / gating mechanism / gradient conflict / fine-tuning），逻辑链条清晰。PCGrad 排除实验遵循 modus tollens 推理范式，说服力强（§5.2, Table 1）。

**S2. 负面结果的诚实报告与深入诊断。** 论文没有停留在"方法不 work"的层面，而是系统追溯失败机制——gate 值反转（§5.1, 27/28 layers, Wilcoxon p = 3.73×10⁻⁸）→ 排除梯度冲突（§5.2）→ 分布偏移归因（§5.3）→ 机制特异性确认（§5.4）→ 跨模型泛化（§5.5）。这种诊断深度在负面结果论文中少见。

**S3. Exposure bias 对辅助注意力损失的选择性破坏是真正新颖的发现。** 先前 exposure bias 文献（Bengio et al. 2015, Arora et al. 2022, He et al. 2019）聚焦于主生成目标的质量退化。本文首次展示 exposure bias 可以选择性摧毁辅助注意力目标（GAR 20–33× 坍塌），同时保留主任务（NTP/PPL 不变），且 token-level self-recovery（He et al. 2019）不能拯救注意力分布属性。这一区分有理论贡献。

**S4. β-steering 实验提供建设性证据。** 通过直接操控注意力 logits 恢复 GAR（0.064→0.727），有效区分了"表征退化"和"注意力路由失败"两种假说（§4.3）。N=50 的 larger-scale 验证增强了可信度。

**S5. 写作中的 scoping hedges 使用得当。** 论文频繁使用 "under the tested conditions", "consistent with our evidence", "proximal cause" 等限定语，避免了不当泛化。Limitations 章节全面、诚实（§8）。

---

## Must-Fix 问题（Critical，影响接收决定）

**N1** [critical] **GAR 指标与下游任务性能之间缺乏因果验证**
- 具体位置：§4.3（steering）、§6（Discussion）、Appendix C（instruction retention）
- 问题：论文的核心叙事建立在 GAR（对 system prompt goal token 的注意力比例）之上，但从未验证 GAR 的提升是否真正改善了指令遵循质量。唯一的下游评估是 Appendix C 的 instruction retention 分析，结果为 McNemar p=0.077（不显著）、相关性 r=0.200。论文自己也承认这是 "exploratory"。但问题在于：如果 GAR 的提升不能可靠地改善实际对话质量，那么整个 "GAR 坍塌 = 失败" 的叙事基础就不稳固。一个模型可能 GAR 很低但指令遵循很好（通过其他注意力路径），也可能 GAR 很高但生成质量差（如 β=10 时 PPL 退化到 4.22）。
- 为什么影响接收：这不是一个次要缺陷——它影响论文的核心 claim 是否有实际意义。如果 GAR 只是一个注意力统计量而非指令遵循的可靠代理指标，那么 "exposure bias 摧毁辅助注意力目标" 这个发现虽然技术上有趣，但其实际重要性大打折扣。
- 建议修改方向：在 β=0/3/5 条件下评估实际指令遵循质量（如 IFEval、MT-Bench、或自定义 system prompt compliance 评估），建立 GAR↔downstream 的量化关联。如果无法做到，需在论文中明确承认这一局限并降低 claim 强度。

**N2** [critical] **Scheduled sampling 结果承载过重但证据不足**
- 具体位置：§6 Discussion（"gap from ~31× to 1.57×"）、Abstract（"compresses the gap to 1.57×"）、Conclusion
- 问题：Scheduled sampling 是论文中唯一展示 training-time mitigation 可行性的证据，在 abstract、intro（contribution 2）、discussion、conclusion 中均被引用。但该结果仅基于单个 seed。虽然论文提到第二个 seed 得到 GAR=0.418（gap 1.20×），这两个 seed 的结果差异很大（0.318 vs 0.418，即 gap 1.57× vs 1.20×），这本身说明结果的方差很高。以单 seed 结果作为关键 contribution 的一部分（contribution 2 中提到 "a preliminary demonstration that scheduled sampling compresses this gap"），且在 abstract 中以确定性语气呈现（"Scheduled sampling compresses the gap to 1.57×"），存在 overclaim 风险。
- 为什么影响接收：ARR reviewer guidelines 要求 soundness 评分必须由 review text 中的具体 evidence 支撑。单 seed 结果缺乏统计可靠性，特别是当两个 seed 的 variance 如此之大时。如果 scheduled sampling 结果在多 seed 下不稳定，论文的核心叙事（exposure bias 是可解决的）就会被削弱。
- 建议修改方向：(1) 在 abstract/conclusion 中明确标注 "single seed, preliminary"；(2) 至少运行 3-5 个 seed 并报告 mean±std；(3) 如果时间不允许，在 abstract 中移除这一 claim 或大幅弱化措辞。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] **标题暗示 gating 固有失败，但实际发现是 exposure bias 对所有 teacher-forced 辅助损失的通用问题**
- 具体位置：Title, §7 Conclusion
- 问题：标题 "Why Per-Layer Residual Gating Fails" 将失败归因于 gating 架构，但论文的核心发现恰恰是 gating 本身不是问题——LoRA-only（无 gate）表现完全相同。真正的发现是 teacher-forced 辅助注意力损失在自回归条件下失效，这与 gating 无关。当前标题可能误导读者认为 gating 是问题所在，而实际上替换成任何其他 teacher-forced 注意力干预都会有同样的失败。
- 建议：标题改为更准确反映核心发现的表述，例如 "Exposure Bias Selectively Destroys Auxiliary Attention Objectives in Multi-Turn LLM Dialogue" 或在标题中明确 exposure bias 的角色。

**W2** [warning] **缺少与最近直接竞争者的实验对比**
- 具体位置：§2 Related Work（li2024measuring, hong2025rhea）
- 问题：Split-softmax (Li et al. 2024) 和 Rhea (Hong et al. 2025) 在 related work 中被讨论为互补方法，但没有实验对比。论文声称 split-softmax "cannot address exposure bias in auxiliary losses"（§2, ¶2），Rhea 同样 "cannot resolve exposure bias in auxiliary losses requiring retraining"（§6）。但这些声称缺乏实验验证——split-softmax 是否也表现出类似的 TF-AR gap？如果 split-softmax 在推理时直接修改注意力而无需训练辅助损失，它是否可以避免 exposure bias 问题？这些问题的实验回答会显著加强论文的定位。
- 建议：至少在一个模型上运行 split-softmax baseline，或明确承认缺乏直接对比是一个局限。

**W3** [warning] **"To our knowledge, the first" 声称过于狭窄且不可证伪**
- 具体位置：§1 Introduction, Contribution (2)
- 问题：Contribution (2) 声称 "to our knowledge the first empirical characterization of how exposure bias selectively destroys auxiliary attention loss generalization"。这一声称非常狭窄——它是第一个研究 exposure bias 对 "auxiliary attention loss" 在 "multi-turn dialogue" 中影响的工作。但这种狭窄的 "first" 声称本质上不可证伪（因为 niche 太窄），且不增加实际的新颖性论证。真正的新颖性在于发现本身，不在于 "first" 的标签。
- 建议：删除 "to our knowledge, the first" 修饰语，直接陈述贡献内容。让 reviewer 自行判断新颖性。

**W4** [warning] **仅两个模型家族（7B-8B scale），泛化性受限**
- 具体位置：§5.5 Cross-Model Generality, §8 Limitations
- 问题：所有实验在 Qwen-2.5-7B 和 Llama-3.1-8B 上进行，且 Llama 上只复制了 ThreadGate 和 LoRA-only（未做完整五路对照）。论文在 §8 承认 "N=2 does not establish universality"，但叙事中仍使用 "cross-model generality" 这样的标题暗示更广泛的泛化。此外，没有在更大规模模型（>13B）或不同架构族（如 Mixtral/MoE）上的验证。
- 建议：将 §5.5 标题改为 "Cross-Model Replication" 而非 "Cross-Model Generality"，降低泛化暗示。

**W5** [warning] **关键数字重复过多**
- 具体位置：Abstract, §1 (×3), Figure 1 caption, §4.2, §5.3, Figure 4 caption
- 问题："20–33× gap" 在论文中出现至少 7 次（abstract 1次、intro 3次、figure 1 caption、experiments、analysis、figure 4 caption）。虽然这是核心发现，但过度重复降低了信息密度，给人 padding 的感觉。类似地，"0.064 to 0.727" 出现 4 次以上。
- 建议：在 abstract 和核心结果处保留精确数字，后续引用时使用 "order-of-magnitude gap" 或 "the TF-AR gap (§4.2)" 等简洁回指。

**W6** [warning] **Table 1 四舍五入与正文数字不一致**
- 具体位置：§4.2 vs Table 1
- 问题：§4.2 称 "GAR-ours spans only 0.75 percentage points (pp) across ThreadGate (0.50), +PCGrad (0.50), Uniform Gate (0.51), and LoRA-only (0.50)"。但 Table 1 显示的数值只保留两位小数（0.50, 0.50, 0.51, 0.50），从这些数字计算 spread 应该是 1 pp 而非 0.75 pp。这意味着实际值在更高精度下不同（如 0.5025 vs 0.5100），但 table 的四舍五入导致读者无法验证这一 claim。
- 建议：Table 1 增加一位小数，或在正文中使用与 table 一致的精度。

---

## 小问题（不影响接收）

- **M1**：Abstract 过于密集（约 180 词），信息压缩度极高，首次阅读时难以消化。建议精简 contribution 罗列，留更多空间给核心发现的叙事。
- **M2**：§5.5 Llama 结果使用 median 而非 mean 报告 AR GAR-ours，理由是 heavy-tailed distribution。虽然统计上合理，但在主实验（Table 1）使用 mean 的情况下切换统计量有 metric selection 之嫌。建议同时报告 mean 和 median。
- **M3**：部分 bib 条目格式不一致——已发表的会议论文使用 @inproceedings（正确），但 Raposo et al. 2024 (Mixture-of-Depths) 使用 @article + arXiv 格式，该论文已被 ICML 2024 接收，应更新为会议版本。同样，Gromov et al. 2024 标注 year=2025 但 booktitle 为 ICLR，需确认年份一致性。
- **M4**：§6 Discussion 提到 KV cache drift 作为替代假说，仅一句话。如果要提出这一替代假说，应至少简述为什么当前实验不能区分 exposure bias 和 KV cache drift。
- **M5**：Conclusion（§7）仅 3 句话，虽然简洁但可能过于简短。建议增加 1-2 句关于 future directions 或 broader implications。
- **M6**：论文未提及代码是否开源。ARR reproducibility 评分需要考虑这一因素。

---

## Questions to Authors

**Q1**：Table 1 中 LoRA-only 的 AR GAR-ours (0.025) 反而高于所有 gating variants (0.015-0.016)。虽然差异很小，但方向是 gating 反而降低了 AR GAR。这是否意味着 gate 的 2-7% attenuation 在推理时略微有害？

**Q2**：β-steering 实验中，β=0 时 N=5（10-turn）的 baseline GAR 为 0.028，但 N=50 的 baseline GAR 为 0.064（mean），差异超过 2×。论文解释为 "short conversations with high baseline GAR" 导致均值偏高。但这是否意味着 GAR 作为指标对对话长度高度敏感，从而削弱了跨实验设置的可比性？

**Q3**：Scheduled sampling 的第二个 seed 得到 GAR=0.418（gap 1.20×）vs 第一个 seed 的 0.318（gap 1.57×）。两个 seed 之间 AR GAR 相差 31%（0.318 vs 0.418）。作者是否能解释这种高方差的来源？这是否暗示 scheduled sampling 的效果对随机初始化非常敏感？

**Q4**：论文使用 LoRA rank 16 进行微调。是否尝试过更高的 rank（如 64 或 128）？gate 的无效性是否可能部分归因于 LoRA 容量已经足够，而非 gating 本身无用？

---

## Missing References

1. **Zhang et al. (2024) "Tell Your Model Where to Attend"** — 与 β-steering 思路相似的推理时注意力操控方法，应在 §2 Attention Manipulation 段落中讨论。
2. **Xu et al. (2025) 或类似的 multi-turn instruction following benchmarks** — 论文缺少对多轮指令遵循质量的标准化评估（如 IFEval multi-turn variant），这些基准应在 §4.1 Setup 中被提及。
3. 建议核实 Raposo et al. (2024) Mixture-of-Depths 是否已在 ICML 2024 正式发表，如是则应更新 bib 条目。

---

## Overall Assessment

**Overall**: 3.5 / 5 — Borderline Conference

**一句话总结**：方法论严谨的负面结果论文，exposure bias 对辅助注意力目标的选择性破坏是真正新颖的发现，但 GAR 指标缺乏下游验证这一根本缺陷削弱了核心 claim 的实际意义。

**详细理由**：

本文的核心强项在于实验设计的严谨性和诊断链的完整性——五路对照、PCGrad 排除、gate 值分析、跨模型验证构成了一个令人信服的论证结构。Exposure bias 对辅助注意力损失的选择性破坏确实是文献中未被系统研究的现象，具有理论贡献。

但论文有两个 critical 弱点阻碍其达到 Conference 水平：(1) GAR 指标与实际指令遵循质量之间的 gap 未被 bridge——整个论文围绕一个注意力统计量展开，但从未证明这个统计量的改善对用户可感知的对话质量有意义；(2) Scheduled sampling 作为唯一的 training-time mitigation evidence 仅有单 seed 支撑，且两个 seed 间方差很大。如果补充下游任务验证和多 seed scheduled sampling 实验，论文将达到 4.0 (Conference) 水平。

当前状态适合 Findings 接收。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 274 · 2026-05-22T23:00:27.139573+00:00_

Reviewer 2 审稿意见已收到（3.5/5 Borderline Conference）。等待 Reviewer 1 完成初审后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director"
}
```

</details>

---


## Round 22

## Round 22

6 recorded events


### User

_source line 275 · 2026-05-22T23:00:29.757225+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 — Round 1 审稿意见

**论文**：Why Per-Layer Residual Gating Fails to Fix Multi-Turn Attention Degradation: A Mechanistic Analysis
**审查侧重**：方法严谨性 + 实验设计

---

## 总体评分
**Overall**: 3.0 / 5 — Findings
**一句话总结**: 研究问题有价值，诊断框架设计合理，但自回归评估样本量过小（N=5）、单种子为主的实验设计、以及对 exposure bias 归因缺乏对替代假说的排除，使得核心因果声明缺乏充分统计支撑。

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3 / 5 | 主要 claims 在定性层面有支撑，但定量证据不足（N=5 AR、单种子、KV cache drift 未排除） |
| Excitement | 3 / 5 | 负面结果+诊断框架对社区有用，但 exposure bias 作为根因的发现可预见性较强 |
| Reproducibility | 3 / 5 | 超参数基本完整但部分关键参数缺失（r_min），无代码发布承诺 |
| Confidence | 4 / 5 | 仔细检查了实验方法论和技术细节 |

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] 自回归评估样本量严重不足（N=5）
- 具体位置：§4.1, Table 1 AR 列
- 问题：核心发现（TF GAR 0.50 → AR GAR 0.015-0.025 的坍塌）完全基于 Qwen 上 5 条自回归对话。N=5 无法提供有意义的统计推断力。Table 1 报告 GAR-ours 到 ±0.025 精度但 N=5 下缺乏统计基础。Llama AR 评估同样使用 N=5 pilot。§5.5 中 "N = 20 mid-turn" 含义模糊。
- 为什么影响接收：核心量化证据基于 N=5，远低于该领域可接受标准。0.015 vs 0.025（ThreadGate vs LoRA-only）的差异无法判断统计显著性。
- 建议：AR 评估扩展到至少 N=50；报告置信区间和显著性检验；统一 N 的定义。

**N2** [critical] Exposure bias 归因缺乏对替代假说的充分排除
- 具体位置：§5.3, §6, §8 Limitations
- 问题：论文将 exposure bias 定位为 "proximal cause"，但 §6 承认 KV cache drift 未被排除，§8 明确说 "disentangling prefix-level and cache-level contributions is left to future work"。对 "mechanistic analysis" 论文而言，将核心替代假说留给 future work 不可接受。
- 建议：设计实验区分 prefix-level exposure bias 和 cache-level drift（如 teacher-forced prefix 到第 k 轮后切换 AR，观察 GAR 退化转折点）。

**N3** [critical] 绝大多数实验条件为单种子
- 具体位置：§4.1, Table 1, §8
- 问题：5 路对比中仅 ThreadGate 有 2 个种子，其余 4 个条件单种子。"gating produces no measurable benefit over LoRA-only"、"eliminating direction conflict changes nothing" 等结论均基于单次运行。Scheduled sampling 的两个种子（GAR 0.727 vs 0.418）差异巨大，进一步暴露单种子不可靠性。
- 建议：至少 3 种子覆盖全部条件；报告均值±标准差；关键对比做显著性检验。

---

## Should-Fix 问题

**W1** [warning] 跨模型验证不完整（Llama 仅 3/5 条件）
- §5.5: 缺 +PCGrad 和 Uniform Gate。削弱 cross-model generality 声明。

**W2** [warning] "Mechanistic Analysis" 标题与分析深度不匹配
- 当前分析为宏观层面（门控值、梯度余弦、注意力偏置），非 circuit-level mechanistic interpretability。建议改为 "Diagnostic Analysis"。

**W3** [warning] Scheduled sampling 证据过于单薄
- 单种子，且两种子间变异极大（0.727 vs 0.418）。不宜作为独立贡献。

**W4** [warning] GAR 改善与生成质量（PPL）脱节
- 所有 fine-tuned variants PPL ≈ 2.78，且残差流 AUC ≈ 0.98。GAR 与下游质量关系未充分讨论。

**W5** [warning] GAR-D 全条件接近零
- 即使 TF 下 ThreadGate GAR-D = 0.02。干预仅在 last token 成功，泛化性问题未讨论。

---

## 小问题
- M1: r_min 数值正文未报告
- M2: Table 1 AR 列缺 GAR-D 和 PPL
- M3: N 含义在不同上下文中不一致
- M4: Figure 4/6 双栏打印尺寸下辨认困难
- M5: §7 中 steering 结果措辞可能误导为训练时方案
- M6: 匿名性和格式合规，无问题
- M7: 页数符合 8 页限制

---

## 主要优势
1. 研究问题有价值——理解干预*为什么*失败比提出新方法更有诊断意义
2. 五路对比设计原则上合理，控制变量思路清晰
3. 多维度诊断（PCGrad排除、门控反转、注意力偏置、TRC）构建证据链
4. 推理时注意力偏置的 phase transition（β=2→3 跳变）是有趣发现
5. Loss formulation search（Table 2）增强方法选择透明度

---

## Questions to Authors
1. Scheduled sampling 两种子 GAR 差异 72%（0.727 vs 0.418），如何解释？
2. LoRA-only AR GAR (0.025) 高于 gated variants (0.015)，多种子下是否稳定？
3. 是否计划公开代码？
4. r_min 具体数值？
5. Teacher-forced prefix 到第 k 轮后切换 AR，GAR 退化临界 k 是多少？

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 276 · 2026-05-22T23:01:23.206137+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "## 交叉分享 — Reviewer 2 的完整审稿意见\n\n请逐条回应 Reviewer 2 的每个 Must-Fix、Should-Fix 和 Minor 问题：\n- **[AGREE]** 同意并说明理由\n- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）\n\n特别注意以下分歧点：\n1. Reviewer 2 给出 3.5（Borderline Conference），你给出 3.0（Findings）——请说明你认为哪些差距导致了评分差异\n2. Reviewer 2 的 N1（GAR 缺乏下游验证）vs 你的 W4（GAR 与 PPL 脱节）——是否为同一问题的不同表述？\n3. Reviewer 2 认为 \"exposure bias 对辅助注意力目标的选择性破坏是真正新颖的发现\"（S3），你认为 \"可预见性较强\"——请明确你的立场\n\n---\n\n以下是 Reviewer 2 的完整审稿意见：\n\n## Summary\n\n本文提出 ThreadGate，一种在 transformer 每层残差路径上添加 content-and-turn-conditioned MLP gate 的方法，目标是恢复多轮对话中衰减的 system prompt 注意力（GAR）。通过五路对照实验（ThreadGate / +PCGrad / Uniform Gate / LoRA-only / Base），作者发现在 teacher-forced 条件下 GAR 收敛至目标值 0.50，但自回归生成时 GAR 坍塌至 0.015–0.025（20–33× gap）。论文进一步通过 PCGrad 排除梯度方向冲突、通过 gate 值分析排除架构缺陷，将失败归因于 exposure bias：辅助注意力损失在 teacher-forcing 下优化的模式无法迁移到自回归推理。β-steering（β=5）将 GAR 从 0.064 恢复至 0.727，scheduled sampling（单 seed）将 gap 从 31× 压缩至 1.57×。跨模型验证在 Llama-3.1-8B 上确认了 27× gap。\n\n## 官方维度打分\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | 五路对照和 PCGrad 排除实验方法论严谨，主要 claims 有充分支撑。但 GAR 与下游任务性能的关联未被验证（p=0.077 不显著），scheduled sampling 仅单 seed，削弱了部分结论的可靠性。 |\n| Excitement | 3/5 | 负面结果 + 暴露偏差归因对社区有参考价值，但论文最终未提供一个可工作的解决方案。β-steering 需要预知 goal token 位置，scheduled sampling 是初步结果。实际影响有限。 |\n| Reproducibility | 4/5 | 超参数文档完整（Appendix A），模型和数据集均公开可获取，seed 已指定。但未提及是否开源代码。 |\n| Confidence | 4/5 | 仔细阅读了全文，熟悉注意力操控、多任务学习、exposure bias 相关文献。 |\n\n## Must-Fix 问题\n\n**N1** [critical] GAR 指标与下游任务性能之间缺乏因果验证\n- 具体位置：§4.3（steering）、§6（Discussion）、Appendix C（instruction retention）\n- 问题：论文的核心叙事建立在 GAR 之上，但从未验证 GAR 的提升是否真正改善了指令遵循质量。唯一的下游评估是 Appendix C 的 instruction retention 分析，结果为 McNemar p=0.077（不显著）、相关性 r=0.200。如果 GAR 的提升不能可靠地改善实际对话质量，那么整个 \"GAR 坍塌 = 失败\" 的叙事基础就不稳固。\n- 建议：在 β=0/3/5 条件下评估实际指令遵循质量（如 IFEval、MT-Bench），建立 GAR↔downstream 的量化关联。\n\n**N2** [critical] Scheduled sampling 结果承载过重但证据不足\n- 具体位置：§6, Abstract, Conclusion\n- 问题：单 seed，两 seed 差异大（0.318 vs 0.418），overclaim 风险。\n- 建议：至少 3-5 个 seed 并报告 mean±std；或在 abstract 中移除/弱化。\n\n## Should-Fix 问题\n\n**W1** [warning] 标题暗示 gating 固有失败，但实际发现是 exposure bias 对所有 teacher-forced 辅助损失的通用问题\n**W2** [warning] 缺少与最近直接竞争者的实验对比（Split-softmax, Rhea）\n**W3** [warning] \"To our knowledge, the first\" 声称过于狭窄且不可证伪\n**W4** [warning] 仅两个模型家族（7B-8B scale），泛化性受限\n**W5** [warning] 关键数字重复过多（\"20-33× gap\" 出现 7+ 次）\n**W6** [warning] Table 1 四舍五入与正文数字不一致\n\n## 小问题\nM1: Abstract 过密 | M2: Llama 用 median 而非 mean | M3: Bib 格式不一致 | M4: KV cache drift 讨论不足 | M5: Conclusion 过短 | M6: 无代码发布声明\n\n## Questions\nQ1: LoRA-only AR GAR 高于 gating variants 是否说明 gate 有害？\nQ2: GAR 对对话长度敏感性（N=5 vs N=50 baseline 差 2×）\nQ3: SS 两 seed 方差来源？\nQ4: LoRA rank 是否影响结论？\n\n## Missing References\n1. Zhang et al. (2024) \"Tell Your Model Where to Attend\"\n2. Multi-turn instruction following benchmarks (IFEval etc.)\n3. Raposo et al. (2024) bib 更新\n\n## Overall: 3.5 / 5 — Borderline Conference"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "text": "## 交叉分享 — Reviewer 2 的完整审稿意见\n\n请逐条回应 Reviewer 2 的每个 Must-Fix、Should-Fix 和 Minor 问题：\n- **[AGREE]** 同意并说明理由\n- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）\n\n特别注意以下分歧点：\n1. Reviewer 2 给出 3.5（Borderline Conference），你给出 3.0（Findings）——请说明你认为哪些差距导致了评分差异\n2. Reviewer 2 的 N1（GAR 缺乏下游验证）vs 你的 W4（GAR 与 PPL 脱节）——是否为同一问题的不同表述？\n3. Reviewer 2 认为 \"exposure bias 对辅助注意力目标的选择性破坏是真正新颖的发现\"（S3），你认为 \"可预见性较强\"——请明确你的立场\n\n---\n\n以下是 Reviewer 2 的完整审稿意见：\n\n## Summary\n\n本文提出 ThreadGate，一种在 transformer 每层残差路径上添加 content-and-turn-conditioned MLP gate 的方法，目标是恢复多轮对话中衰减的 system prompt 注意力（GAR）。通过五路对照实验（ThreadGate / +PCGrad / Uniform Gate / LoRA-only / Base），作者发现在 teacher-forced 条件下 GAR 收敛至目标值 0.50，但自回归生成时 GAR 坍塌至 0.015–0.025（20–33× gap）。论文进一步通过 PCGrad 排除梯度方向冲突、通过 gate 值分析排除架构缺陷，将失败归因于 exposure bias：辅助注意力损失在 teacher-forcing 下优化的模式无法迁移到自回归推理。β-steering（β=5）将 GAR 从 0.064 恢复至 0.727，scheduled sampling（单 seed）将 gap 从 31× 压缩至 1.57×。跨模型验证在 Llama-3.1-8B 上确认了 27× gap。\n\n## 官方维度打分\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | 五路对照和 PCGrad 排除实验方法论严谨，主要 claims 有充分支撑。但 GAR 与下游任务性能的关联未被验证（p=0.077 不显著），scheduled sampling 仅单 seed，削弱了部分结论的可靠性。 |\n| Excitement | 3/5 | 负面结果 + 暴露偏差归因对社区有参考价值，但论文最终未提供一个可工作的解决方案。β-steering 需要预知 goal token 位置，scheduled sampling 是初步结果。实际影响有限。 |\n| Reproducibility | 4/5 | 超参数文档完整（Appendix A），模型和数据集均公开可获取，seed 已指定。但未提及是否开源代码。 |\n| Confidence | 4/5 | 仔细阅读了全文，熟悉注意力操控、多任务学习、exposure bias 相关文献。 |\n\n## Must-Fix 问题\n\n**N1** [critical] GAR 指标与下游任务性能之间缺乏因果验证\n- 具体位置：§4.3（steering）、§6（Discussion）、Appendix C（instruction retention）\n- 问题：论文的核心叙事建立在 GAR 之上，但从未验证 GAR 的提升是否真正改善了指令遵循质量。唯一的下游评估是 Appendix C 的 instruction retention 分析，结果为 McNemar p=0.077（不显著）、相关性 r=0.200。如果 GAR 的提升不能可靠地改善实际对话质量，那么整个 \"GAR 坍塌 = 失败\" 的叙事基础就不稳固。\n- 建议：在 β=0/3/5 条件下评估实际指令遵循质量（如 IFEval、MT-Bench），建立 GAR↔downstream 的量化关联。\n\n**N2** [critical] Scheduled sampling 结果承载过重但证据不足\n- 具体位置：§6, Abstract, Conclusion\n- 问题：单 seed，两 seed 差异大（0.318 vs 0.418），overclaim 风险。\n- 建议：至少 3-5 个 seed 并报告 mean±std；或在 abstract 中移除/弱化。\n\n## Should-Fix 问题\n\n**W1** [warning] 标题暗示 gating 固有失败，但实际发现是 exposure bias 对所有 teacher-forced 辅助损失的通用问题\n**W2** [warning] 缺少与最近直接竞争者的实验对比（Split-softmax, Rhea）\n**W3** [warning] \"To our knowledge, the first\" 声称过于狭窄且不可证伪\n**W4** [warning] 仅两个模型家族（7B-8B scale），泛化性受限\n**W5** [warning] 关键数字重复过多（\"20-33× gap\" 出现 7+ 次）\n**W6** [warning] Table 1 四舍五入与正文数字不一致\n\n## 小问题\nM1: Abstract 过密 | M2: Llama 用 median 而非 mean | M3: Bib 格式不一致 | M4: KV cache drift 讨论不足 | M5: Conclusion 过短 | M6: 无代码发布声明\n\n## Questions\nQ1: LoRA-only AR GAR 高于 gating variants 是否说明 gate 有害？\nQ2: GAR 对对话长度敏感性（N=5 vs N=50 baseline 差 2×）\nQ3: SS 两 seed 方差来源？\nQ4: LoRA rank 是否影响结论？\n\n## Missing References\n1. Zhang et al. (2024) \"Tell Your Model Where to Attend\"\n2. Multi-turn instruction following benchmarks (IFEval etc.)\n3. Raposo et al. (2024) bib 更新\n\n## Overall: 3.5 / 5 — Borderline Conference"
  }
}
```

</details>

---


### Tool result

_source line 277 · 2026-05-22T23:01:43.038966+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 19832
}
```

</details>

---


### Tool call

_source line 278 · 2026-05-22T23:01:43.240309+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "## 交叉分享 — Reviewer 1 的完整审稿意见\n\n请逐条回应 Reviewer 1 的每个 Must-Fix、Should-Fix 和 Minor 问题：\n- **[AGREE]** 同意并说明理由\n- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）\n\n特别注意以下分歧点：\n1. Reviewer 1 给出 3.0（Findings），你给出 3.5（Borderline Conference）——请说明你认为差距在哪里\n2. Reviewer 1 的 N2（exposure bias 归因缺乏替代假说排除）——你在 M4 也提到 KV cache drift，但未列为 critical。请明确你的严重性判断\n3. Reviewer 1 认为 exposure bias 发现 \"可预见性较强\"，你认为是 \"真正新颖的发现\"——请明确你的立场并提供文献依据\n\n---\n\n以下是 Reviewer 1 的完整审稿意见：\n\n## 总体评分\n**Overall**: 3.0 / 5 — Findings\n\n## 官方维度打分\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3 / 5 | 主要 claims 在定性层面有支撑，但定量证据不足（N=5 AR、单种子、KV cache drift 未排除） |\n| Excitement | 3 / 5 | 负面结果+诊断框架对社区有用，但 exposure bias 作为根因的发现可预见性较强 |\n| Reproducibility | 3 / 5 | 超参数基本完整但部分关键参数缺失（r_min），无代码发布承诺 |\n| Confidence | 4 / 5 | 仔细检查了实验方法论和技术细节 |\n\n## Must-Fix 问题\n\n**N1** [critical] 自回归评估样本量严重不足（N=5）\n- 核心发现完全基于 Qwen 上 5 条自回归对话。N=5 无法提供有意义的统计推断力。\n- 建议：AR 评估扩展到至少 N=50；报告置信区间和显著性检验。\n\n**N2** [critical] Exposure bias 归因缺乏对替代假说的充分排除\n- §6 承认 KV cache drift 未被排除，§8 明确说留给 future work。对 \"mechanistic analysis\" 论文而言不可接受。\n- 建议：设计实验区分 prefix-level exposure bias 和 cache-level drift。\n\n**N3** [critical] 绝大多数实验条件为单种子\n- 5 路对比中仅 ThreadGate 有 2 个种子，其余 4 个条件单种子。SS 两种子差异 72%。\n- 建议：至少 3 种子覆盖全部条件。\n\n## Should-Fix 问题\n\n**W1** [warning] 跨模型验证不完整（Llama 仅 3/5 条件）\n**W2** [warning] \"Mechanistic Analysis\" 标题与分析深度不匹配——建议改为 \"Diagnostic Analysis\"\n**W3** [warning] Scheduled sampling 证据过于单薄\n**W4** [warning] GAR 改善与生成质量（PPL）脱节\n**W5** [warning] GAR-D 全条件接近零——干预仅在 last token 成功\n\n## 小问题\nM1: r_min 正文未报告 | M2: Table 1 AR 列缺 GAR-D 和 PPL | M3: N 定义不一致 | M4: Figure 4/6 打印尺寸 | M5: §7 steering 措辞 | M6: 匿名合规 | M7: 8 页限制合规\n\n## 主要优势\n1. 研究问题有价值 2. 五路对比设计合理 3. 多维度诊断链 4. β steering phase transition 5. Loss search 透明\n\n## Questions\n1. SS 两种子 GAR 差异 72% 如何解释？\n2. LoRA-only AR GAR 高于 gated variants 多种子下是否稳定？\n3. 代码发布计划？\n4. r_min 数值？\n5. TF→AR 切换临界轮次 k？"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "text": "## 交叉分享 — Reviewer 1 的完整审稿意见\n\n请逐条回应 Reviewer 1 的每个 Must-Fix、Should-Fix 和 Minor 问题：\n- **[AGREE]** 同意并说明理由\n- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）\n\n特别注意以下分歧点：\n1. Reviewer 1 给出 3.0（Findings），你给出 3.5（Borderline Conference）——请说明你认为差距在哪里\n2. Reviewer 1 的 N2（exposure bias 归因缺乏替代假说排除）——你在 M4 也提到 KV cache drift，但未列为 critical。请明确你的严重性判断\n3. Reviewer 1 认为 exposure bias 发现 \"可预见性较强\"，你认为是 \"真正新颖的发现\"——请明确你的立场并提供文献依据\n\n---\n\n以下是 Reviewer 1 的完整审稿意见：\n\n## 总体评分\n**Overall**: 3.0 / 5 — Findings\n\n## 官方维度打分\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3 / 5 | 主要 claims 在定性层面有支撑，但定量证据不足（N=5 AR、单种子、KV cache drift 未排除） |\n| Excitement | 3 / 5 | 负面结果+诊断框架对社区有用，但 exposure bias 作为根因的发现可预见性较强 |\n| Reproducibility | 3 / 5 | 超参数基本完整但部分关键参数缺失（r_min），无代码发布承诺 |\n| Confidence | 4 / 5 | 仔细检查了实验方法论和技术细节 |\n\n## Must-Fix 问题\n\n**N1** [critical] 自回归评估样本量严重不足（N=5）\n- 核心发现完全基于 Qwen 上 5 条自回归对话。N=5 无法提供有意义的统计推断力。\n- 建议：AR 评估扩展到至少 N=50；报告置信区间和显著性检验。\n\n**N2** [critical] Exposure bias 归因缺乏对替代假说的充分排除\n- §6 承认 KV cache drift 未被排除，§8 明确说留给 future work。对 \"mechanistic analysis\" 论文而言不可接受。\n- 建议：设计实验区分 prefix-level exposure bias 和 cache-level drift。\n\n**N3** [critical] 绝大多数实验条件为单种子\n- 5 路对比中仅 ThreadGate 有 2 个种子，其余 4 个条件单种子。SS 两种子差异 72%。\n- 建议：至少 3 种子覆盖全部条件。\n\n## Should-Fix 问题\n\n**W1** [warning] 跨模型验证不完整（Llama 仅 3/5 条件）\n**W2** [warning] \"Mechanistic Analysis\" 标题与分析深度不匹配——建议改为 \"Diagnostic Analysis\"\n**W3** [warning] Scheduled sampling 证据过于单薄\n**W4** [warning] GAR 改善与生成质量（PPL）脱节\n**W5** [warning] GAR-D 全条件接近零——干预仅在 last token 成功\n\n## 小问题\nM1: r_min 正文未报告 | M2: Table 1 AR 列缺 GAR-D 和 PPL | M3: N 定义不一致 | M4: Figure 4/6 打印尺寸 | M5: §7 steering 措辞 | M6: 匿名合规 | M7: 8 页限制合规\n\n## 主要优势\n1. 研究问题有价值 2. 五路对比设计合理 3. 多维度诊断链 4. β steering phase transition 5. Loss search 透明\n\n## Questions\n1. SS 两种子 GAR 差异 72% 如何解释？\n2. LoRA-only AR GAR 高于 gated variants 多种子下是否稳定？\n3. 代码发布计划？\n4. r_min 数值？\n5. TF→AR 切换临界轮次 k？"
  }
}
```

</details>

---


### Tool result

_source line 279 · 2026-05-22T23:01:44.657785+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1417
}
```

</details>

---


### Assistant

_source line 280 · 2026-05-22T23:01:47.408668+00:00_

交叉分享已发送。等待两位 Reviewer 的逐条回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director"
}
```

</details>

---


## Round 23

## Round 23

10 recorded events


### User

_source line 281 · 2026-05-22T23:01:48.466311+00:00_

[Reviewer 1 审稿结果]:
审稿意见已提交给 Review Director。

总结：本轮审稿识别出 3 个 Critical Must-Fix（N=5 样本量不足、exposure bias 归因不完整、单种子实验）和 5 个 Should-Fix（跨模型不完整、标题 overclaim、scheduled sampling 单薄、GAR-PPL 脱节、GAR-D 接近零）。整体评分 Overall 3.0 / Soundness 3 / Excitement 3，建议 Findings 级别接收，但需要显著增强统计证据后才能支撑当前的因果声明。

---

[Reviewer 2 审稿结果]:
审稿意见已提交给 Review Director。

**审稿完成摘要：**

- **Overall: 3.5/5 (Borderline Conference)**，当前状态适合 Findings
- **Soundness 3.5/5, Excitement 3/5, Reproducibility 4/5**

**2 个 Critical 问题：**
1. GAR 指标与下游任务性能之间缺乏因果验证——instruction retention 分析 p=0.077 不显著，整个论文围绕一个未被验证的注意力统计量展开
2. Scheduled sampling 结果（gap 31×→1.57×）仅单 seed，两个 seed 间 AR GAR 相差 31%（0.318 vs 0.418），在 abstract/conclusion 中以确定性语气呈现存在 overclaim 风险

**6 个 Should-Fix 问题：** 标题误导（暗示 gating 固有失败而非 exposure bias 通用问题）、缺少与 split-softmax/Rhea 的实验对比、"to our knowledge, the first" 声称不可证伪、仅两个 7-8B 模型、关键数字重复过多、Table 1 精度与正文不一致

**核心判断：** 方法论严谨的负面结果 + 新颖的 exposure bias 归因，但 GAR→downstream 的 gap 是根本弱点。补充下游验证和多 seed 实验后可达 Conference (4.0) 水平。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 282 · 2026-05-22T23:02:23.502331+00:00_

called mcp__agent-ml-research__get_visual_check_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_visual_check_status</summary>

```json
{
  "project": "turn_residual_gating"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "tool_args": {
    "project": "turn_residual_gating"
  }
}
```

</details>

---


### Tool result

_source line 283 · 2026-05-22T23:02:23.502791+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"done\", \"started_at\": \"2026-05-22T22:52:00.573642+00:00\", \"completed_at\": \"2026-05-22T22:54:26.855808+00:00\", \"findings\": [{\"severity\": \"info\", \"dimension\": \"page 1\", \"message\": \"首页无视觉锚点，Figure 1 出现在 Page 2 顶部——在 3 页阈值内，可接受。若能将 Figure 1 上提至 Page 1 底部会进一步强化第一印象\"}, {\"severity\": \"warning\", \"dimension\": \"page 3-4\", \"message\": \"连续两页无 figure/table。虽然 Page 4 有 GAR 公式和架构公式提供视觉节奏，但 Page 3（Related Work 全文字）和 Page 4 上半段纯文本连续感较强\"}, {\"severity\": \"info\", \"dimension\": \"page 2\", \"message\": \"Figure 1 右侧 \\\"Mechanism analysis\\\" 区域文字偏小（约 6-7pt），特别是 \\\"Gradient conflict → PCGrad\\\" 和 \\\"Attribution shift (exposure bias)\\\" 标注，在打印或低分辨率屏幕上可能难以辨认\"}, {\"severity\": \"info\", \"dimension\": \"page 5\", \"message\": \"Figure 2 线图清晰，图例可读，颜色区分度好（蓝/橙/绿/红）。但 y 轴标签 \\\"GAR-ours (τ=0.5)\\\" 字号略小\"}, {\"severity\": \"info\", \"dimension\": \"page 6\", \"message\": \"Table 1 使用 booktabs 风格，最优结果加粗标注，专业。GAR-O 列标题含义需依赖 caption 解释——caption 已自包含，合格\"}, {\"severity\": \"info\", \"dimension\": \"page 7\", \"message\": \"Figure 4（gate turn conditioning）和 Figure 5（gradient cosine similarity + IID eval）两个多面板图堆叠在同一页。Figure 4 的 bar chart 标签（层号 1-28）字号极小（约 5-6pt），Figure 5 的四个子面板各自标签也偏小。这是全文视觉密度最高的页面，信息量大但可读性有压力\"}, {\"severity\": \"warning\", \"dimension\": \"page 7\", \"message\": \"Figure 5 四面板中 (c) \\\"Gradient direction conflict\\\" 和 (d) \\\"IID outcomes unchanged\\\" 的 y 轴数值标签重叠或过于密集，在 150dpi 下已显拥挤\"}, {\"severity\": \"info\", \"dimension\": \"page 8\", \"message\": \"Discussion + Conclusion 全文本页，无 display item。作为论文倒数第一正文页可接受，但若能在 Discussion 中放一个总结性 figure 或 insight 表格会增强收尾感\"}, {\"severity\": \"info\", \"dimension\": \"page 6\", \"message\": \"Figure 3 的两个子面板（a）（b）使用了一致的颜色方案（蓝色为 ThreadGate），与 Figure 2 配色保持一致，色彩语义一致性好\"}, {\"severity\": \"info\", \"dimension\": \"page 9\", \"message\": \"Limitations 段落简洁（约 3 个要点），符合 EMNLP 规范。References 格式统一，无可见的 [?] 未解析引用\"}, {\"severity\": \"info\", \"dimension\": 
…[truncated 573 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 284 · 2026-05-22T23:02:23.553211+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "turn_residual_gating"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "turn_residual_gating"
  }
}
```

</details>

---


### Tool result

_source line 285 · 2026-05-22T23:02:23.653934+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 286 · 2026-05-22T23:07:11.745347+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "turn_residual_gating",
  "issues_yaml": "# Review Issues Tracker — turn_residual_gating\n# Round 1 (2026-05-19, dream_20260519T145320)\n# Round 2 (2026-05-22, fresh re-review of revised paper)\n# Round 3 (2026-05-22, fresh re-review)\n# Round 4 (2026-05-22, fresh re-review — current round)\n\n# ============================================================\n# Issues from Round 1 — status updates through Round 4\n# ============================================================\n\n- id: \"R1-N1\"\n  summary: \"所有引用渲染为 '?'——bibliography 编译失败\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"Dream paper artifact。\"\n    - round: 2\n      reviewers: []\n      note: \"视觉审查确认无 [?] 未解析引用。已修复。\"\n    - round: 3\n      reviewers: []\n      note: \"Round 3 视觉审查确认无未解析引用。维持 resolved。\"\n    - round: 4\n      reviewers: []\n      note: \"Round 4 视觉审查确认无未解析引用。维持 resolved。\"\n  action_items:\n    - round: 1\n      action: \"Paper Agent 确保 bibtex 编译正确\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"Round 2 视觉审查确认已修复。\"\n  resolution_round: 2\n\n- id: \"R1-N2\"\n  summary: \"单种子支撑结论——统计功效不足 + AR 评估 N=5 过小\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 1\n  last_seen_round: 4\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"Bootstrap CI 仅覆盖 eval variance，不覆盖 training variance。\"\n    - round: 2\n      reviewers: [1, 2]\n      note: \"ThreadGate 已补 seed=123，但其余 4/5 条件仍为单 seed。SS 仅 1 seed 且第二 seed 协议不同不可比。\"\n    - round: 3\n      reviewers: [1, 2]\n      note: \"AR 评估仅 N=5，核心 claim 'all variants collapse equally' 缺统计检验。\"\n    - round: 4\n      reviewers: [1, 2]\n      note: \"两位 Reviewer 独立列为 Critical Must-Fix。R1 强调 N=5 无法提供有意义统计推断力，0.015 vs 0.025 差异无法判断显著性。R2 确认这是核心量化证据的根本缺陷。5 路对比中仅 ThreadGate 有 2 seeds，其余单 seed。\"\n  action_items:\n    - round: 1\n      action: \"plan_019: seed=123 extra training\"\n      assigned_to: agent\n      status: done\n    - round: 2\n      action: \"D048: 6 条件 × 3 seeds from-scratch\"\n      assigned_to: agent\n      status: in_progress\n    - round: 3\n      action: \"AR 评估扩大至 N=50 + bootstrap 95% CI + 条件间成对检验\"\n      assigned_to: agent\n      status: in_progress\n    - round: 4\n      action: \"AR 评估 N≥50 + 至少 3 seeds 覆盖全部 5 条件 + 显著性检验 + CI\"\n      assigned_to: agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-N3\"\n  summary: \"评估样本量过小\"\n  category: experiment\n  severity: info\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1]\n      note: \"Cohen's d≈0.22 在 n=50 下 power 不足。\"\n    - round: 2\n      reviewers: []\n      note: \"Round 2 使用 N=50 held-out + N=50 steering + N=20 Llama。未再被提出。\"\n    - round: 4\n      reviewers: []\n      note: \"TF 评估样本量已充分。AR N=5 问题在 R1-N2 中追踪。\"\n  action_items: []\n  resolution: \"N=50 评估已在论文中体现。AR N=5 问题移至 R1-N2 追踪。\"\n  resolution_round: 2\n\n- id: \"R1-N4\"\n  summary: \"损失函数超参数和 v1-v6 配置定义缺失\"\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"v1-v7 配置仅报告 v7。\"\n    - round: 2\n      reviewers: []\n      note: \"§3.3 报告 λ_GAR=λ_div=1.0。Appendix Table 2 列出 v1-v7。\"\n    - round: 4\n      reviewers: []\n      note: \"本轮未提及。维持 resolved。\"\n  action_items: []\n  resolution: \"§3.3 + Appendix B Table 2 已提供完整信息。\"\n  resolution_round: 2\n\n- id: \"R1-W1\"\n  summary: \"Llama 跨模型消融不完整（缺 PCGrad + Uniform Gate）\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 4\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"边际信息量不值 6h GPU。\"\n    - round: 2\n      reviewers: [1, 2]\n      note: \"仍仅 3/5 条件，N=20，用 median。\"\n    - round: 3\n      reviewers: [1, 2]\n      note: \"额外问题：mean/median 未双报，AR/TF 样本量不匹配，attention spikes 未解释。\"\n    - round: 4\n      reviewers: [1, 2]\n      note: \"R1 列 Should-Fix（仅 3/5 条件削弱 cross-model generality 声明）。R2 建议标题改为 'Cross-Model Replication'。R2-M2 指出 median vs mean 切换有 metric selection 之嫌。\"\n  action_items:\n    - round: 2\n      action: \"D048: 补充 Llama PCGrad+UG 训练+评估\"\n      assigned_to: agent\n      status: in_progress\n    - round: 4\n      action: \"补齐 Llama 5-way 对比 + mean/median 双报 + §5.5 改标题为 Cross-Model Replication\"\n      assigned_to: agent\n      status: open\n\n- id: \"R1-W2\"\n  summary: \"无 λ_GAR 敏感性消融\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - round: 1\n      reviewers: [1]\n      note: \"梯度冲突取决于 λ_GAR。\"\n    - round: 2\n      reviewers: []\n      note: \"Round 2/3 未被独立提出。论文核心 claim 已转向 exposure bias。\"\n    - round: 4\n      reviewers: []\n      note: \"本轮未提及。\"\n  action_items:\n    - round: 1\n      action: \"plan_022: λ_GAR=10 敏感性测试\"\n      assigned_to: agent\n      status: in_progress\n\n- id: \"R1-W3\"\n  summary: \"训练数据量混淆变量\"\n  category: experiment\n  severity: info\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1]\n      note: \"1,000 convs 偏少。\"\n    - round: 2\n      reviewers: []\n      note: \"Round 2 使用 8K conversations。\"\n  action_items: []\n  resolution: \"训练数据量增加至 8K。\"\n  resolution_round: 2\n\n- id: \"R1-W4\"\n  summary: \"全文零 figure\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"Dream paper artifact.\"\n    - round: 2\n      reviewers: []\n      note: \"Round 2 有 5 figures + 2 tables。\"\n  action_items: []\n  resolution: \"Figure 1-5 + Table 1-2 已就位。\"\n  resolution_round: 2\n\n- id: \"R1-W5\"\n  summary: \"Scheduled sampling 统计支撑不足\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 1\n  last_seen_round: 4\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"单 seed，单 ratio，PPL 未报告。\"\n    - round: 2\n      reviewers: [1, 2]\n      note: \"PPL 已报告，但仍单 seed，第二 seed 协议不同不可比。\"\n    - round: 3\n      reviewers: [1, 2]\n      note: \"双种子差异大（GAR 0.318 vs 0.418）且策略不同。\"\n    - round: 4\n      reviewers: [1, 2]\n      note: \"两位 Reviewer 独立标记。R1 列 Critical（两 seed GAR 差异 72%）。R2 列 Critical（abstract 以确定性语气呈现单 seed 结果存在 overclaim）。两 seed 间 AR GAR 相差 31%（0.318 vs 0.418），说明方差极高。\"\n  action_items:\n    - round: 2\n      action: \"D048: SS 3-seed from-scratch\"\n      assigned_to: agent\n      status: in_progress\n    - round: 4\n      action: \"至少 3-5 seeds + mean±std；abstract/conclusion 明确标注 'single seed, preliminary' 或移除 claim\"\n      assigned_to: agent\n      status: open\n\n- id: \"R1-W6\"\n  summary: \"Reverse turn conditioning 证据间接\"\n  category: experiment\n  severity: info\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1]\n      note: \"差异可能是噪声。\"\n  resolution: \"Wilcoxon p=3.73e-8, r=0.975。已在 §5.1 报告。\"\n  resolution_round: 2\n\n# ============================================================\n# Issues from Round 2 — status updates through Round 4\n# ============================================================\n\n- id: \"R2-N1\"\n  summary: \"Novelty/causal 声称过高——contribution 措辞需调整\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 4\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"'first quantitative measurement' overclaim。\"\n    - round: 2\n      reviewers: [1, 2]\n      note: \"'systematic causal diagnostic framework' 实际是消融。\"\n    - round: 3\n      reviewers: [1, 2]\n      note: \"删除 'in principle applicable'。'first' → 'to our knowledge, the first'。\"\n    - round: 4\n      reviewers: [2]\n      note: \"R2-W3: 'to our knowledge, the first' 仍被质疑——声称过于狭窄且不可证伪。建议直接删除 'first' 修饰语。\"\n  action_items:\n    - round: 1\n      action: \"'first quantitative measurement' 降级\"\n      assigned_to: director\n      status: done\n    - round: 4\n      action: \"删除 'to our knowledge, the first' 修饰语，直接陈述贡献内容\"\n      assigned_to: paper_agent\n      status: open\n\n- id: \"R2-N2\"\n  summary: \"标题过度声称\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 4\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"'Cannot Fix' → 'Fails to Fix'。\"\n    - round: 2\n      reviewers: [1, 2]\n      note: \"'Lightweight Gating' 过宽。\"\n    - round: 3\n      reviewers: [2]\n      note: \"R2 仍有异议但 R1 反驳有理。Director 裁定当前标题可接受。\"\n    - round: 4\n      reviewers: [1, 2]\n      note: \"R2-W1: 标题暗示 gating 固有失败，但实际发现是 exposure bias 对所有 TF 辅助损失的通用问题（LoRA-only 无 gate 表现相同）。R1-W2: 'Mechanistic Analysis' 副标题与分析深度不匹配（宏观层面非 circuit-level），建议改为 'Diagnostic Analysis'。\"\n  action_items:\n    - round: 2\n      action: \"标题改为 'Per-Layer Residual Gating'\"\n      assigned_to: paper_agent\n      status: done\n    - round: 4\n      action: \"考虑标题更准确反映 exposure bias 为核心发现；副标题 'Mechanistic' → 'Diagnostic'\"\n      assigned_to: paper_agent\n      status: open\n\n- id: \"R2-N3\"\n  summary: \"Dongre et al. GAR 全称引用错误\"\n  category: format\n  severity: critical\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 3\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"论文动机链依赖此引用。\"\n    - round: 2\n      reviewers: [2]\n      note: \"原文为 'Goal Accessibility Ratio'。\"\n    - round: 3\n      reviewers: [1, 2]\n      note: \"arXiv 原文验证确认。Critical Must-Fix。\"\n    - round: 4\n      reviewers: []\n      note: \"本轮 Reviewer 未独立提出。待确认是否已修复。\"\n  action_items:\n    - round: 3\n      action: \"全文替换 'Goal Attention Ratio' → 'Goal Accessibility Ratio'\"\n      assigned_to: agent\n      status: in_progress\n\n- id: \"R2-N4\"\n  summary: \"Related Work 缺失 gradient conflict 文献 + PCGrad baseline\"\n  category: framing\n  severity: info\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"如果 PCGrad 能解决梯度竞争，论文核心结论悬空。\"\n    - round: 2\n      reviewers: []\n      note: \"PCGrad 已纳入五路对比，§2 已覆盖。\"\n  action_items: []\n  resolution: \"PCGrad 已纳入五路对比 + Related Work 已覆盖。\"\n  resolution_round: 2\n\n- id: \"R2-C3\"\n  summary: \"Exposure bias 归因——替代假说讨论不足\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 2\n  last_seen_round: 4\n  mentions:\n    - round: 2\n      reviewers: [1, 2]\n      note: \"β-steering 循环论证；KV cache 差异未排除。\"\n    - round: 3\n      reviewers: [1, 2]\n      note: \"R1 列 Critical，R2 降 Should-Fix。\"\n    - round: 4\n      reviewers: [1, 2]\n      note: \"R1 列 Critical（N2）：§6 承认 KV cache drift 未排除，§8 留给 future work，对 'mechanistic analysis' 论文不可接受。建议设计实验区分 prefix-level exposure bias 和 cache-level drift。R2-M4 也提出 KV cache drift 讨论不足但列 Minor。严重性分歧：R1 认为是核心因果声明的漏洞，R2 认为在 scoping hedges 存在的情况下可接受。\"\n  action_items:\n    - round: 2\n      action: \"'the proximal cause' → 'a proximal cause consistent with evidence'\"\n      assigned_to: paper_agent\n      status: done\n    - round: 4\n      action: \"设计 TF→AR 切换实验（teacher-forced prefix 到第 k 轮后切换 AR，观察 GAR 退化转折点）以区分 prefix-level exposure bias 和 cache-level drift\"\n      assigned_to: agent\n      status: open\n\n- id: \"R2-W3\"\n  summary: \"GAR 单指标——instruction retention 不显著但占页过多\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 4\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"r=0.82 sanity check 不足。\"\n    - round: 2\n      reviewers: [1, 2]\n      note: \"McNemar p=0.077 不显著。\"\n    - round: 3\n      reviewers: [1, 2]\n      note: \"占 Discussion 过多篇幅。建议移入 Appendix。\"\n    - round: 4\n      reviewers: [1, 2]\n      note: \"升级为更根本的问题：R2 列 Critical（N1）——GAR 指标与下游任务性能之间缺乏因果验证，整个论文围绕一个未经验证的注意力统计量展开。R1-W4 同意 GAR 改善与 PPL 脱节（所有 variants PPL≈2.78）。β=10 时 PPL 退化到 4.22 进一步说明 GAR 极端提升可能有害。\"\n  action_items:\n    - round: 2\n      action: \"D048: N=200 扩容指令保持实验\"\n      assigned_to: agent\n      status: in_progress\n    - round: 4\n      action: \"在 β=0/3/5 条件下评估实际指令遵循质量（IFEval/MT-Bench/自定义 system prompt compliance），建立 GAR↔downstream 关联\"\n      assigned_to: agent\n      status: open\n\n- id: \"R2-W5\"\n  summary: \"liu2016attention 引用可能错配\"\n  category: format\n  severity: warning\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [2]\n      note: \"语音识别 vs 注意力引导。\"\n    - round: 4\n      reviewers: []\n      note: \"本轮未提及。待确认。\"\n  action_items:\n    - round: 2\n      action: \"Paper Agent 确认引用准确性\"\n      assigned_to: paper_agent\n      status: in_progress\n\n- id: \"R2-W6\"\n  summary: \"Bib 格式不一致\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 1\n  last_seen_round: 4\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"orphan 条目。\"\n    - round: 2\n      reviewers: [2]\n      note: \"'and others' vs 完整作者列表不一致。\"\n    - round: 3\n      reviewers: [2]\n      note: \"grattafiori2024llama3 格式不一致。\"\n    - round: 4\n      reviewers: [2]\n      note: \"R2-M3: Raposo et al. 2024 (Mixture-of-Depths) 使用 @article + arXiv，该论文已被 ICML 2024 接收应更新。Gromov et al. 2024 标注 year=2025 但 booktitle 为 ICLR 需确认年份一致性。\"\n  action_items:\n    - round: 4\n      action: \"统一 bib 格式：更新 Raposo et al. 为 ICML 2024 @inproceedings；确认 Gromov et al. 年份一致性\"\n      assigned_to: paper_agent\n      status: open\n\n- id: \"R1-MISC\"\n  summary: \"无代码/数据发布\"\n  category: format\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 4\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"负面结果论文可复现性最后防线。\"\n    - round: 2\n      reviewers: [1]\n      note: \"Reproducibility 3.0/5。\"\n    - round: 4\n      reviewers: [1, 2]\n      note: \"R1 Reproducibility 3/5，R2 Reproducibility 4/5。两位均指出无代码发布承诺。R1-M6、R2-M6 均提出。\"\n  action_items:\n    - round: 2\n      action: \"投稿前准备匿名 GitHub repo\"\n      assigned_to: agent\n      status: open\n\n- id: \"R2-W1-new\"\n  summary: \"Table 1 AR 列需扩容\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 2\n  last_seen_round: 4\n  mentions:\n    - round: 2\n      reviewers: [1, 2]\n      note: \"核心发现未在表格中呈现。\"\n    - round: 3\n      reviewers: [1, 2]\n      note: \"AR 列存在但仅 N=5。\"\n    - round: 4\n      reviewers: [1]\n      note: \"R1-M2: Table 1 AR 列缺 GAR-D 和 PPL。与 R1-N2 联动——N=5 不可接受。\"\n  action_items:\n    - round: 4\n      action: \"AR 列更新为 N≥50 数据 + CI + GAR-D + PPL\"\n      assigned_to: agent\n      status: open\n\n- id: \"R2-W4-new\"\n  summary: \"写作冗余——关键数字重复 8+ 次\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 2\n  last_seen_round: 4\n  mentions:\n    - round: 2\n      reviewers: [1, 2]\n      note: \"'20-33× gap' 多章节重复。\"\n    - round: 3\n      reviewers: [1, 2]\n      note: \"出现 8+ 次。\"\n    - round: 4\n      reviewers: [2]\n      note: \"R2-W5: '20-33× gap' 至少 7 次（abstract, intro ×3, fig1 caption, §4.2, §5.3, fig4 caption）。'0.064 to 0.727' 出现 4+ 次。建议 abstract/核心结果保留精确数字，其余用回指。\"\n  action_items:\n    - round: 4\n      action: \"Abstract/§4.2 保留完整数字，其余改用 'the TF-AR gap (Table 1)' 或 'order-of-magnitude gap' 回指\"\n      assigned_to: paper_agent\n      status: open\n\n- id: \"R2-W6-new\"\n  summary: \"Contribution (1) 泛化声称\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 2\n  last_seen_round: 4\n  mentions:\n    - round: 2\n      reviewers: [1, 2]\n      note: \"'in principle applicable' 未验证。\"\n    - round: 4\n      reviewers: [2]\n      note: \"合并至 R2-N1 追踪。R2-W3 进一步指出 'first' 声称不可证伪。\"\n  action_items:\n    - round: 4\n      action: \"删除泛化声称，合并至 R2-N1\"\n      assigned_to: paper_agent\n      status: open\n\n- id: \"R2-W7-new\"\n  summary: \"Li et al. split-softmax 缺实验对比\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 2\n  last_seen_round: 4\n  mentions:\n    - round: 2\n      reviewers: [2]\n      note: \"最直接竞争方法。R1 认为超 scope。\"\n    - round: 4\n      reviewers: [2]\n      note: \"R2-W2: 仍缺实验对比。论文声称 split-softmax 'cannot address exposure bias' 但未实验验证。Rhea 同理。\"\n  action_items:\n    - round: 4\n      action: \"至少在一个模型上运行 split-softmax baseline，或明确承认缺乏直接对比是局限\"\n      assigned_to: agent\n      status: open\n\n# ============================================================\n# Supplementary items from Round 2\n# ============================================================\n\n- id: \"R2-SUPP-1\"\n  summary: \"Figure/Table caption overclaim + 重复句\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 2\n  last_seen_round: 3\n  mentions:\n    - round: 2\n      reviewers: []\n      note: \"Figure caption 可能有 overclaim。\"\n    - round: 3\n      reviewers: [2]\n      note: \"Figure 4 caption 重复句。\"\n    - round: 4\n      reviewers: []\n      note: \"本轮未独立提出。R2 的 overclaim 关注点集中在标题和 contribution list。\"\n  action_items:\n    - round: 3\n      action: \"修正 Fig 3b/Table 1/Fig 4 caption 的 overclaim + 删除 Fig 4 重复句\"\n      assigned_to: paper_agent\n      status: in_progress\n\n- id: \"R2-SUPP-2\"\n  summary: \"Multi-seed 完成后数字更新\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - round: 2\n      reviewers: []\n      note: \"Abstract/Intro gap 数字需从单 seed 更新为 mean±std。\"\n    - round: 4\n      reviewers: []\n      note: \"仍待 multi-seed 实验完成。\"\n  action_items:\n    - round: 2\n      action: \"Multi-seed 完成后统一更新\"\n      assigned_to: paper_agent\n      status: open\n\n- id: \"R2-SUPP-3\"\n  summary: \"SS variance 风险应急计划\"\n  category: experiment\n  severity: info\n  status: open\n  first_raised_round: 2\n  last_seen_round: 4\n  mentions:\n    - round: 2\n      reviewers: []\n      note: \"SS 3-seed variance 极大时需应急 framing。\"\n    - round: 4\n      reviewers: []\n      note: \"Round 4 两 seed 差异 31% 进一步增加应急计划紧迫性。\"\n  action_items:\n    - round: 2\n      action: \"SS multi-seed 结果出来后评估 variance\"\n      assigned_to: director\n      status: open\n\n# ============================================================\n# Issues from Round 3 — status updates through Round 4\n# ============================================================\n\n- id: \"R3-MF2\"\n  summary: \"正文超过 EMNLP 8 页限制\"\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 4\n  mentions:\n    - round: 3\n      reviewers: [1, 2]\n      note: \"约 8.4 页。Paper Agent 已压缩至 8.0 页。\"\n    - round: 4\n      reviewers: [1]\n      note: \"R1-M7: 页数符合 8 页限制。\"\n  resolution: \"Round 4 确认页数合规。\"\n  resolution_round: 4\n\n- id: \"R3-SF4\"\n  summary: \"PCGrad scope 过度概括\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n    - round: 3\n      reviewers: [1, 2]\n      note: \"'gradient conflict' 未加 'directional' 限定。\"\n    - round: 4\n      reviewers: []\n      note: \"本轮未独立提出。\"\n  action_items:\n    - round: 3\n      action: \"'gradient conflict' → 'gradient direction conflict'；结论提及 magnitude imbalance 未排除\"\n      assigned_to: paper_agent\n      status: in_progress\n\n- id: \"R3-SF6\"\n  summary: \"缺少 Rhea (arXiv:2512.06869) 引用\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 3\n  last_seen_round: 4\n  mentions:\n    - round: 3\n      reviewers: [1, 2]\n      note: \"Rhea: Role-aware Heuristic Episodic Attention。\"\n    - round: 4\n      reviewers: [2]\n      note: \"R2-W2 确认 Rhea 在 related work 中被讨论但缺实验对比。合并至 R2-W7-new 追踪。\"\n  action_items:\n    - round: 3\n      action: \"添加 bib 条目 + §2/§6 引用对比\"\n      assigned_to: paper_agent\n      status: in_progress\n\n- id: \"R3-MINOR-1\"\n  summary: \"LoRA capacity saturation 未讨论\"\n  category: method\n  severity: info\n  status: open\n  first_raised_round: 3\n  last_seen_round: 4\n  mentions:\n    - round: 3\n      reviewers: [1]\n      note: \"R1 提出，R2 反驳（不影响 TF-AR gap）。\"\n    - round: 4\n      reviewers: [2]\n      note: \"R2-Q4: LoRA rank 16 是否影响结论？是否尝试过更高 rank？\"\n  action_items:\n    - round: 4\n      action: \"§4.2 或 Limitations 加一句 acknowledge LoRA rank 可能影响 gate 效用上界\"\n      assigned_to: paper_agent\n      status: open\n\n- id: \"R3-MINOR-2\"\n  summary: \"GPU 型号名称准确性\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n    - round: 3\n      reviewers: [2]\n      note: \"'NVIDIA RTX PRO 6000 Blackwell Server Edition GPU (102 GB)' 待确认。\"\n    - round: 4\n      reviewers: []\n      note: \"本轮未提及。\"\n  action_items:\n    - round: 3\n      action: \"确认准确性\"\n      assigned_to: agent\n      status: open\n\n- id: \"R3-NEW-1\"\n  summary: \"UG 描述不清——未说明仍为可学习 MLP\"\n  category: method\n  severity: info\n  status: in_progress\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n    - round: 3\n      reviewers: []\n      note: \"UG 描述仅说 'gates without turn embedding'，未明确仍是可学习的 content-conditioned MLP。\"\n    - round: 4\n      reviewers: []\n      note: \"本轮未提及。\"\n  action_items:\n    - round: 3\n      action: \"§4.1 或 §3 加一句说明\"\n      assigned_to: paper_agent\n      status: in_progress\n\n- id: \"R3-NEW-2\"\n  summary: \"Contribution (4) 混淆开发迭代与系统消融\"\n  category: framing\n  severity: info\n  status: in_progress\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n    - round: 3\n      reviewers: []\n      note: \"'seven loss formulations and four training configurations' 混淆了 v1-v7 loss iteration 和五路系统消融。\"\n    - round: 4\n      reviewers: []\n      note: \"本轮未提及。\"\n  action_items:\n    - round: 3\n      action: \"拆分为 'loss design iterations (Appendix A)' + 'systematic conditions comparison (Table 1)'\"\n      assigned_to: paper_agent\n      status: in_progress\n\n# ============================================================\n# New issues from Round 4\n# ============================================================\n\n- id: \"R4-N1\"\n  summary: \"GAR 指标与下游任务性能之间缺乏因果验证\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 4\n  last_seen_round: 4\n  mentions:\n    - round: 4\n      reviewers: [1, 2]\n      note: \"R2 列 Critical：论文核心叙事建立在 GAR 之上，但 instruction retention 分析 McNemar p=0.077 不显著、r=0.200。β=10 时 PPL 退化到 4.22 说明 GAR 极端提升可能有害。R1-W4 同意 GAR-PPL 脱节（所有 variants PPL≈2.78, AUC≈0.98）。GAR 是否是指令遵循的可靠代理指标未经验证。\"\n  action_items:\n    - round: 4\n      action: \"在 β=0/3/5 条件下评估实际指令遵循质量（IFEval/MT-Bench/自定义 compliance metric），建立 GAR↔downstream 关联。若无法完成，需在论文中明确承认并降低 claim 强度。\"\n      assigned_to: agent\n      status: open\n\n- id: \"R4-W1\"\n  summary: \"GAR-D 全条件接近零——干预仅在 last token 成功\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 4\n  last_seen_round: 4\n  mentions:\n    - round: 4\n      reviewers: [1]\n      note: \"R1-W5: 即使 TF 下 ThreadGate GAR-D = 0.02。干预仅在 τ-masked last token 成功，泛化性问题未讨论。\"\n  action_items:\n    - round: 4\n      action: \"讨论 GAR-ours vs GAR-D 差异的含义——为什么 last-token masking 成功但 Dongre 分布式衡量失败\"\n      assigned_to: paper_agent\n      status: open\n\n- id: \"R4-W2\"\n  summary: \"Table 1 四舍五入与正文数字精度不一致\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 4\n  last_seen_round: 4\n  mentions:\n    - round: 4\n      reviewers: [2]\n      note: \"R2-W6: §4.2 称 spread 为 0.75pp 但 Table 1 两位小数显示 1pp（0.50-0.51）。需增加精度或统一。\"\n  action_items:\n    - round: 4\n      action: \"Table 1 增加一位小数，或正文使用与 table 一致的精度\"\n      assigned_to: paper_agent\n      status: open\n\n- id: \"R4-W3\"\n  summary: \"r_min 数值正文未报告\"\n  category: method\n  severity: info\n  status: open\n  first_raised_round: 4\n  last_seen_round: 4\n  mentions:\n    - round: 4\n      reviewers: [1]\n      note: \"R1-M1: r_min 数值在正文中未报告，影响可复现性。\"\n  action_items:\n    - round: 4\n      action: \"在 §3 或 Appendix A 中报告 r_min 数值\"\n      assigned_to: paper_agent\n      status: open\n\n- id: \"R4-MR1\"\n  summary: \"缺少 Zhang et al. 2024 'Tell Your Model Where to Attend' 引用\"\n  category: framing\n  severity: info\n  status: open\n  first_raised_round: 4\n  last_seen_round: 4\n  mentions:\n    - round: 4\n      reviewers: [2]\n      note: \"与 β-steering 思路相似的推理时注意力操控方法，应在 §2 讨论。\"\n  action_items:\n    - round: 4\n      action: \"确认引用存在性并在 §2 Attention Manipulation 段落引用对比\"\n      assigned_to: paper_agent\n      status: open\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "turn_residual_gating",
    "issues_yaml": "# Review Issues Tracker — turn_residual_gating\n# Round 1 (2026-05-19, dream_20260519T145320)\n# Round 2 (2026-05-22, fresh re-review of revised paper)\n# Round 3 (2026-05-22, fresh re-review)\n# Round 4 (2026-05-22, fresh re-review — current round)\n\n# ============================================================\n# Issues from Round 1 — status updates through Round 4\n# ============================================================\n\n- id: \"R1-N1\"\n  summary: \"所有引用渲染为 '?'——bibliography 编译失败\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"Dream paper artifact。\"\n    - round: 2\n      reviewers: []\n      note: \"视觉审查确认无 [?] 未解析引用。已修复。\"\n    - round: 3\n      reviewers: []\n      note: \"Round 3 视觉审查确认无未解析引用。维持 resolved。\"\n    - round: 4\n      reviewers: []\n      note: \"Round 4 视觉审查确认无未解析引用。维持 resolved。\"\n  action_items:\n    - round: 1\n      action: \"Paper Agent 确保 bibtex 编译正确\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"Round 2 视觉审查确认已修复。\"\n  resolution_round: 2\n\n- id: \"R1-N2\"\n  summary: \"单种子支撑结论——统计功效不足 + AR 评估 N=5 过小\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 1\n  last_seen_round: 4\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"Bootstrap CI 仅覆盖 eval variance，不覆盖 training variance。\"\n    - round: 2\n      reviewers: [1, 2]\n      note: \"ThreadGate 已补 seed=123，但其余 4/5 条件仍为单 seed。SS 仅 1 seed 且第二 seed 协议不同不可比。\"\n    - round: 3\n      reviewers: [1, 2]\n      note: \"AR 评估仅 N=5，核心 claim 'all variants collapse equally' 缺统计检验。\"\n    - round: 4\n      reviewers: [1, 2]\n      note: \"两位 Reviewer 独立列为 Critical Must-Fix。R1 强调 N=5 无法提供有意义统计推断力，0.015 vs 0.025 差异无法判断显著性。R2 确认这是核心量化证据的根本缺陷。5 路对比中仅 ThreadGate 有 2 seeds，其余单 seed。\"\n  action_items:\n    - round: 1\n      action: \"plan_019: seed=123 extra training\"\n      assigned_to: agent\n      status: done\n    - round: 2\n      action: \"D048: 6 条件 × 3 seeds from-scratch\"\n      assigned_to: agent\n      status: in_progress\n    - round: 3\n      action: \"AR 评估扩大至 N=50 + bootstrap 95% CI + 条件间成对检验\"\n      assigned_to: agent\n      status: in_progress\n    - round: 4\n      action: \"AR 评估 N≥50 + 至少 3 seeds 覆盖全部 5 条件 + 显著性检验 + CI\"\n      assigned_to: agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-N3\"\n  summary: \"评估样本量过小\"\n  category: experiment\n  severity: info\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1]\n      note: \"Cohen's d≈0.22 在 n=50 下 power 不足。\"\n    - round: 2\n      reviewers: []\n      note: \"Round 2 使用 N=50 held-out + N=50 steering + N=20 Llama。未再被提出。\"\n    - round: 4\n      reviewers: []\n      note: \"TF 评估样本量已充分。AR N=5 问题在 R1-N2 中追踪。\"\n  action_items: []\n  resolution: \"N=50 评估已在论文中体现。AR N=5 问题移至 R1-N2 追踪。\"\n  resolution_round: 2\n\n- id: \"R1-N4\"\n  summary: \"损失函数超参数和 v1-v6 配置定义缺失\"\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"v1-v7 配置仅报告 v7。\"\n    - round: 2\n      reviewers: []\n      note: \"§3.3 报告 λ_GAR=λ_div=1.0。Appendix Table 2 列出 v1-v7。\"\n    - round: 4\n      reviewers: []\n      note: \"本轮未提及。维持 resolved。\"\n  action_items: []\n  resolution: \"§3.3 + Appendix B Table 2 已提供完整信息。\"\n  resolution_round: 2\n\n- id: \"R1-W1\"\n  summary: \"Llama 跨模型消融不完整（缺 PCGrad + Uniform Gate）\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 4\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"边际信息量不值 6h GPU。\"\n    - round: 2\n      reviewers: [1, 2]\n      note: \"仍仅 3/5 条件，N=20，用 median。\"\n    - round: 3\n      reviewers: [1, 2]\n      note: \"额外问题：mean/median 未双报，AR/TF 样本量不匹配，attention spikes 未解释。\"\n    - round: 4\n      reviewers: [1, 2]\n      note: \"R1 列 Should-Fix（仅 3/5 条件削弱 cross-model generality 声明）。R2 建议标题改为 'Cross-Model Replication'。R2-M2 指出 median vs mean 切换有 metric selection 之嫌。\"\n  action_items:\n    - round: 2\n      action: \"D048: 补充 Llama PCGrad+UG 训练+评估\"\n      assigned_to: agent\n      status: in_progress\n    - round: 4\n      action: \"补齐 Llama 5-way 对比 + mean/median 双报 + §5.5 改标题为 Cross-Model Replication\"\n      assigned_to: agent\n      status: open\n\n- id: \"R1-W2\"\n  summary: \"无 λ_GAR 敏感性消融\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - round: 1\n      reviewers: [1]\n      note: \"梯度冲突取决于 λ_GAR。\"\n    - round: 2\n      reviewers: []\n      note: \"Round 2/3 未被独立提出。论文核心 claim 已转向 exposure bias。\"\n    - round: 4\n      reviewers: []\n      note: \"本轮未提及。\"\n  action_items:\n    - round: 1\n      action: \"plan_022: λ_GAR=10 敏感性测试\"\n      assigned_to: agent\n      status: in_progress\n\n- id: \"R1-W3\"\n  summary: \"训练数据量混淆变量\"\n  category: experiment\n  severity: info\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1]\n      note: \"1,000 convs 偏少。\"\n    - round: 2\n      reviewers: []\n      note: \"Round 2 使用 8K conversations。\"\n  action_items: []\n  resolution: \"训练数据量增加至 8K。\"\n  resolution_round: 2\n\n- id: \"R1-W4\"\n  summary: \"全文零 figure\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"Dream paper artifact.\"\n    - round: 2\n      reviewers: []\n      note: \"Round 2 有 5 figures + 2 tables。\"\n  action_items: []\n  resolution: \"Figure 1-5 + Table 1-2 已就位。\"\n  resolution_round: 2\n\n- id: \"R1-W5\"\n  summary: \"Scheduled sampling 统计支撑不足\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 1\n  last_seen_round: 4\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"单 seed，单 ratio，PPL 未报告。\"\n    - round: 2\n      reviewers: [1, 2]\n      note: \"PPL 已报告，但仍单 seed，第二 seed 协议不同不可比。\"\n    - round: 3\n      reviewers: [1, 2]\n      note: \"双种子差异大（GAR 0.318 vs 0.418）且策略不同。\"\n    - round: 4\n      reviewers: [1, 2]\n      note: \"两位 Reviewer 独立标记。R1 列 Critical（两 seed GAR 差异 72%）。R2 列 Critical（abstract 以确定性语气呈现单 seed 结果存在 overclaim）。两 seed 间 AR GAR 相差 31%（0.318 vs 0.418），说明方差极高。\"\n  action_items:\n    - round: 2\n      action: \"D048: SS 3-seed from-scratch\"\n      assigned_to: agent\n      status: in_progress\n    - round: 4\n      action: \"至少 3-5 seeds + mean±std；abstract/conclusion 明确标注 'single seed, preliminary' 或移除 claim\"\n      assigned_to: agent\n      status: open\n\n- id: \"R1-W6\"\n  summary: \"Reverse turn conditioning 证据间接\"\n  category: experiment\n  severity: info\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1]\n      note: \"差异可能是噪声。\"\n  resolution: \"Wilcoxon p=3.73e-8, r=0.975。已在 §5.1 报告。\"\n  resolution_round: 2\n\n# ============================================================\n# Issues from Round 2 — status updates through Round 4\n# ============================================================\n\n- id: \"R2-N1\"\n  summary: \"Novelty/causal 声称过高——contribution 措辞需调整\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 4\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"'first quantitative measurement' overclaim。\"\n    - round: 2\n      reviewers: [1, 2]\n      note: \"'systematic causal diagnostic framework' 实际是消融。\"\n    - round: 3\n      reviewers: [1, 2]\n      note: \"删除 'in principle applicable'。'first' → 'to our knowledge, the first'。\"\n    - round: 4\n      reviewers: [2]\n      note: \"R2-W3: 'to our knowledge, the first' 仍被质疑——声称过于狭窄且不可证伪。建议直接删除 'first' 修饰语。\"\n  action_items:\n    - round: 1\n      action: \"'first quantitative measurement' 降级\"\n      assigned_to: director\n      status: done\n    - round: 4\n      action: \"删除 'to our knowledge, the first' 修饰语，直接陈述贡献内容\"\n      assigned_to: paper_agent\n      status: open\n\n- id: \"R2-N2\"\n  summary: \"标题过度声称\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 4\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"'Cannot Fix' → 'Fails to Fix'。\"\n    - round: 2\n      reviewers: [1, 2]\n      note: \"'Lightweight Gating' 过宽。\"\n    - round: 3\n      reviewers: [2]\n      note: \"R2 仍有异议但 R1 反驳有理。Director 裁定当前标题可接受。\"\n    - round: 4\n      reviewers: [1, 2]\n      note: \"R2-W1: 标题暗示 gating 固有失败，但实际发现是 exposure bias 对所有 TF 辅助损失的通用问题（LoRA-only 无 gate 表现相同）。R1-W2: 'Mechanistic Analysis' 副标题与分析深度不匹配（宏观层面非 circuit-level），建议改为 'Diagnostic Analysis'。\"\n  action_items:\n    - round: 2\n      action: \"标题改为 'Per-Layer Residual Gating'\"\n      assigned_to: paper_agent\n      status: done\n    - round: 4\n      action: \"考虑标题更准确反映 exposure bias 为核心发现；副标题 'Mechanistic' → 'Diagnostic'\"\n      assigned_to: paper_agent\n      status: open\n\n- id: \"R2-N3\"\n  summary: \"Dongre et al. GAR 全称引用错误\"\n  category: format\n  severity: critical\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 3\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"论文动机链依赖此引用。\"\n    - round: 2\n      reviewers: [2]\n      note: \"原文为 'Goal Accessibility Ratio'。\"\n    - round: 3\n      reviewers: [1, 2]\n      note: \"arXiv 原文验证确认。Critical Must-Fix。\"\n    - round: 4\n      reviewers: []\n      note: \"本轮 Reviewer 未独立提出。待确认是否已修复。\"\n  action_items:\n    - round: 3\n      action: \"全文替换 'Goal Attention Ratio' → 'Goal Accessibility Ratio'\"\n      assigned_to: agent\n      status: in_progress\n\n- id: \"R2-N4\"\n  summary: \"Related Work 缺失 gradient conflict 文献 + PCGrad baseline\"\n  category: framing\n  severity: info\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"如果 PCGrad 能解决梯度竞争，论文核心结论悬空。\"\n    - round: 2\n      reviewers: []\n      note: \"PCGrad 已纳入五路对比，§2 已覆盖。\"\n  action_items: []\n  resolution: \"PCGrad 已纳入五路对比 + Related Work 已覆盖。\"\n  resolution_round: 2\n\n- id: \"R2-C3\"\n  summary: \"Exposure bias 归因——替代假说讨论不足\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 2\n  last_seen_round: 4\n  mentions:\n    - round: 2\n      reviewers: [1, 2]\n      note: \"β-steering 循环论证；KV cache 差异未排除。\"\n    - round: 3\n      reviewers: [1, 2]\n      note: \"R1 列 Critical，R2 降 Should-Fix。\"\n    - round: 4\n      reviewers: [1, 2]\n      note: \"R1 列 Critical（N2）：§6 承认 KV cache drift 未排除，§8 留给 future work，对 'mechanistic analysis' 论文不可接受。建议设计实验区分 prefix-level exposure bias 和 cache-level drift。R2-M4 也提出 KV cache drift 讨论不足但列 Minor。严重性分歧：R1 认为是核心因果声明的漏洞，R2 认为在 scoping hedges 存在的情况下可接受。\"\n  action_items:\n    - round: 2\n      action: \"'the proximal cause' → 'a proximal cause consistent with evidence'\"\n      assigned_to: paper_agent\n      status: done\n    - round: 4\n      action: \"设计 TF→AR 切换实验（teacher-forced prefix 到第 k 轮后切换 AR，观察 GAR 退化转折点）以区分 prefix-level exposure bias 和 cache-level drift\"\n      assigned_to: agent\n      status: open\n\n- id: \"R2-W3\"\n  summary: \"GAR 单指标——instruction retention 不显著但占页过多\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 4\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"r=0.82 sanity check 不足。\"\n    - round: 2\n      reviewers: [1, 2]\n      note: \"McNemar p=0.077 不显著。\"\n    - round: 3\n      reviewers: [1, 2]\n      note: \"占 Discussion 过多篇幅。建议移入 Appendix。\"\n    - round: 4\n      reviewers: [1, 2]\n      note: \"升级为更根本的问题：R2 列 Critical（N1）——GAR 指标与下游任务性能之间缺乏因果验证，整个论文围绕一个未经验证的注意力统计量展开。R1-W4 同意 GAR 改善与 PPL 脱节（所有 variants PPL≈2.78）。β=10 时 PPL 退化到 4.22 进一步说明 GAR 极端提升可能有害。\"\n  action_items:\n    - round: 2\n      action: \"D048: N=200 扩容指令保持实验\"\n      assigned_to: agent\n      status: in_progress\n    - round: 4\n      action: \"在 β=0/3/5 条件下评估实际指令遵循质量（IFEval/MT-Bench/自定义 system prompt compliance），建立 GAR↔downstream 关联\"\n      assigned_to: agent\n      status: open\n\n- id: \"R2-W5\"\n  summary: \"liu2016attention 引用可能错配\"\n  category: format\n  severity: warning\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [2]\n      note: \"语音识别 vs 注意力引导。\"\n    - round: 4\n      reviewers: []\n      note: \"本轮未提及。待确认。\"\n  action_items:\n    - round: 2\n      action: \"Paper Agent 确认引用准确性\"\n      assigned_to: paper_agent\n      status: in_progress\n\n- id: \"R2-W6\"\n  summary: \"Bib 格式不一致\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 1\n  last_seen_round: 4\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"orphan 条目。\"\n    - round: 2\n      reviewers: [2]\n      note: \"'and others' vs 完整作者列表不一致。\"\n    - round: 3\n      reviewers: [2]\n      note: \"grattafiori2024llama3 格式不一致。\"\n    - round: 4\n      reviewers: [2]\n      note: \"R2-M3: Raposo et al. 2024 (Mixture-of-Depths) 使用 @article + arXiv，该论文已被 ICML 2024 接收应更新。Gromov et al. 2024 标注 year=2025 但 booktitle 为 ICLR 需确认年份一致性。\"\n  action_items:\n    - round: 4\n      action: \"统一 bib 格式：更新 Raposo et al. 为 ICML 2024 @inproceedings；确认 Gromov et al. 年份一致性\"\n      assigned_to: paper_agent\n      status: open\n\n- id: \"R1-MISC\"\n  summary: \"无代码/数据发布\"\n  category: format\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 4\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"负面结果论文可复现性最后防线。\"\n    - round: 2\n      reviewers: [1]\n      note: \"Reproducibility 3.0/5。\"\n    - round: 4\n      reviewers: [1, 2]\n      note: \"R1 Reproducibility 3/5，R2 Reproducibility 4/5。两位均指出无代码发布承诺。R1-M6、R2-M6 均提出。\"\n  action_items:\n    - round: 2\n      action: \"投稿前准备匿名 GitHub repo\"\n      assigned_to: agent\n      status: open\n\n- id: \"R2-W1-new\"\n  summary: \"Table 1 AR 列需扩容\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 2\n  last_seen_round: 4\n  mentions:\n    - round: 2\n      reviewers: [1, 2]\n      note: \"核心发现未在表格中呈现。\"\n    - round: 3\n      reviewers: [1, 2]\n      note: \"AR 列存在但仅 N=5。\"\n    - round: 4\n      reviewers: [1]\n      note: \"R1-M2: Table 1 AR 列缺 GAR-D 和 PPL。与 R1-N2 联动——N=5 不可接受。\"\n  action_items:\n    - round: 4\n      action: \"AR 列更新为 N≥50 数据 + CI + GAR-D + PPL\"\n      assigned_to: agent\n      status: open\n\n- id: \"R2-W4-new\"\n  summary: \"写作冗余——关键数字重复 8+ 次\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 2\n  last_seen_round: 4\n  mentions:\n    - round: 2\n      reviewers: [1, 2]\n      note: \"'20-33× gap' 多章节重复。\"\n    - round: 3\n      reviewers: [1, 2]\n      note: \"出现 8+ 次。\"\n    - round: 4\n      reviewers: [2]\n      note: \"R2-W5: '20-33× gap' 至少 7 次（abstract, intro ×3, fig1 caption, §4.2, §5.3, fig4 caption）。'0.064 to 0.727' 出现 4+ 次。建议 abstract/核心结果保留精确数字，其余用回指。\"\n  action_items:\n    - round: 4\n      action: \"Abstract/§4.2 保留完整数字，其余改用 'the TF-AR gap (Table 1)' 或 'order-of-magnitude gap' 回指\"\n      assigned_to: paper_agent\n      status: open\n\n- id: \"R2-W6-new\"\n  summary: \"Contribution (1) 泛化声称\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 2\n  last_seen_round: 4\n  mentions:\n    - round: 2\n      reviewers: [1, 2]\n      note: \"'in principle applicable' 未验证。\"\n    - round: 4\n      reviewers: [2]\n      note: \"合并至 R2-N1 追踪。R2-W3 进一步指出 'first' 声称不可证伪。\"\n  action_items:\n    - round: 4\n      action: \"删除泛化声称，合并至 R2-N1\"\n      assigned_to: paper_agent\n      status: open\n\n- id: \"R2-W7-new\"\n  summary: \"Li et al. split-softmax 缺实验对比\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 2\n  last_seen_round: 4\n  mentions:\n    - round: 2\n      reviewers: [2]\n      note: \"最直接竞争方法。R1 认为超 scope。\"\n    - round: 4\n      reviewers: [2]\n      note: \"R2-W2: 仍缺实验对比。论文声称 split-softmax 'cannot address exposure bias' 但未实验验证。Rhea 同理。\"\n  action_items:\n    - round: 4\n      action: \"至少在一个模型上运行 split-softmax baseline，或明确承认缺乏直接对比是局限\"\n      assigned_to: agent\n      status: open\n\n# ============================================================\n# Supplementary items from Round 2\n# ============================================================\n\n- id: \"R2-SUPP-1\"\n  summary: \"Figure/Table caption overclaim + 重复句\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 2\n  last_seen_round: 3\n  mentions:\n    - round: 2\n      reviewers: []\n      note: \"Figure caption 可能有 overclaim。\"\n    - round: 3\n      reviewers: [2]\n      note: \"Figure 4 caption 重复句。\"\n    - round: 4\n      reviewers: []\n      note: \"本轮未独立提出。R2 的 overclaim 关注点集中在标题和 contribution list。\"\n  action_items:\n    - round: 3\n      action: \"修正 Fig 3b/Table 1/Fig 4 caption 的 overclaim + 删除 Fig 4 重复句\"\n      assigned_to: paper_agent\n      status: in_progress\n\n- id: \"R2-SUPP-2\"\n  summary: \"Multi-seed 完成后数字更新\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - round: 2\n      reviewers: []\n      note: \"Abstract/Intro gap 数字需从单 seed 更新为 mean±std。\"\n    - round: 4\n      reviewers: []\n      note: \"仍待 multi-seed 实验完成。\"\n  action_items:\n    - round: 2\n      action: \"Multi-seed 完成后统一更新\"\n      assigned_to: paper_agent\n      status: open\n\n- id: \"R2-SUPP-3\"\n  summary: \"SS variance 风险应急计划\"\n  category: experiment\n  severity: info\n  status: open\n  first_raised_round: 2\n  last_seen_round: 4\n  mentions:\n    - round: 2\n      reviewers: []\n      note: \"SS 3-seed variance 极大时需应急 framing。\"\n    - round: 4\n      reviewers: []\n      note: \"Round 4 两 seed 差异 31% 进一步增加应急计划紧迫性。\"\n  action_items:\n    - round: 2\n      action: \"SS multi-seed 结果出来后评估 variance\"\n      assigned_to: director\n      status: open\n\n# ============================================================\n# Issues from Round 3 — status updates through Round 4\n# ============================================================\n\n- id: \"R3-MF2\"\n  summary: \"正文超过 EMNLP 8 页限制\"\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 4\n  mentions:\n    - round: 3\n      reviewers: [1, 2]\n      note: \"约 8.4 页。Paper Agent 已压缩至 8.0 页。\"\n    - round: 4\n      reviewers: [1]\n      note: \"R1-M7: 页数符合 8 页限制。\"\n  resolution: \"Round 4 确认页数合规。\"\n  resolution_round: 4\n\n- id: \"R3-SF4\"\n  summary: \"PCGrad scope 过度概括\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n    - round: 3\n      reviewers: [1, 2]\n      note: \"'gradient conflict' 未加 'directional' 限定。\"\n    - round: 4\n      reviewers: []\n      note: \"本轮未独立提出。\"\n  action_items:\n    - round: 3\n      action: \"'gradient conflict' → 'gradient direction conflict'；结论提及 magnitude imbalance 未排除\"\n      assigned_to: paper_agent\n      status: in_progress\n\n- id: \"R3-SF6\"\n  summary: \"缺少 Rhea (arXiv:2512.06869) 引用\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 3\n  last_seen_round: 4\n  mentions:\n    - round: 3\n      reviewers: [1, 2]\n      note: \"Rhea: Role-aware Heuristic Episodic Attention。\"\n    - round: 4\n      reviewers: [2]\n      note: \"R2-W2 确认 Rhea 在 related work 中被讨论但缺实验对比。合并至 R2-W7-new 追踪。\"\n  action_items:\n    - round: 3\n      action: \"添加 bib 条目 + §2/§6 引用对比\"\n      assigned_to: paper_agent\n      status: in_progress\n\n- id: \"R3-MINOR-1\"\n  summary: \"LoRA capacity saturation 未讨论\"\n  category: method\n  severity: info\n  status: open\n  first_raised_round: 3\n  last_seen_round: 4\n  mentions:\n    - round: 3\n      reviewers: [1]\n      note: \"R1 提出，R2 反驳（不影响 TF-AR gap）。\"\n    - round: 4\n      reviewers: [2]\n      note: \"R2-Q4: LoRA rank 16 是否影响结论？是否尝试过更高 rank？\"\n  action_items:\n    - round: 4\n      action: \"§4.2 或 Limitations 加一句 acknowledge LoRA rank 可能影响 gate 效用上界\"\n      assigned_to: paper_agent\n      status: open\n\n- id: \"R3-MINOR-2\"\n  summary: \"GPU 型号名称准确性\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n    - round: 3\n      reviewers: [2]\n      note: \"'NVIDIA RTX PRO 6000 Blackwell Server Edition GPU (102 GB)' 待确认。\"\n    - round: 4\n      reviewers: []\n      note: \"本轮未提及。\"\n  action_items:\n    - round: 3\n      action: \"确认准确性\"\n      assigned_to: agent\n      status: open\n\n- id: \"R3-NEW-1\"\n  summary: \"UG 描述不清——未说明仍为可学习 MLP\"\n  category: method\n  severity: info\n  status: in_progress\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n    - round: 3\n      reviewers: []\n      note: \"UG 描述仅说 'gates without turn embedding'，未明确仍是可学习的 content-conditioned MLP。\"\n    - round: 4\n      reviewers: []\n      note: \"本轮未提及。\"\n  action_items:\n    - round: 3\n      action: \"§4.1 或 §3 加一句说明\"\n      assigned_to: paper_agent\n      status: in_progress\n\n- id: \"R3-NEW-2\"\n  summary: \"Contribution (4) 混淆开发迭代与系统消融\"\n  category: framing\n  severity: info\n  status: in_progress\n  first_raised_round: 3\n  last_seen_round: 3\n  mentions:\n    - round: 3\n      reviewers: []\n      note: \"'seven loss formulations and four training configurations' 混淆了 v1-v7 loss iteration 和五路系统消融。\"\n    - round: 4\n      reviewers: []\n      note: \"本轮未提及。\"\n  action_items:\n    - round: 3\n      action: \"拆分为 'loss design iterations (Appendix A)' + 'systematic conditions comparison (Table 1)'\"\n      assigned_to: paper_agent\n      status: in_progress\n\n# ============================================================\n# New issues from Round 4\n# ============================================================\n\n- id: \"R4-N1\"\n  summary: \"GAR 指标与下游任务性能之间缺乏因果验证\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 4\n  last_seen_round: 4\n  mentions:\n    - round: 4\n      reviewers: [1, 2]\n      note: \"R2 列 Critical：论文核心叙事建立在 GAR 之上，但 instruction retention 分析 McNemar p=0.077 不显著、r=0.200。β=10 时 PPL 退化到 4.22 说明 GAR 极端提升可能有害。R1-W4 同意 GAR-PPL 脱节（所有 variants PPL≈2.78, AUC≈0.98）。GAR 是否是指令遵循的可靠代理指标未经验证。\"\n  action_items:\n    - round: 4\n      action: \"在 β=0/3/5 条件下评估实际指令遵循质量（IFEval/MT-Bench/自定义 compliance metric），建立 GAR↔downstream 关联。若无法完成，需在论文中明确承认并降低 claim 强度。\"\n      assigned_to: agent\n      status: open\n\n- id: \"R4-W1\"\n  summary: \"GAR-D 全条件接近零——干预仅在 last token 成功\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 4\n  last_seen_round: 4\n  mentions:\n    - round: 4\n      reviewers: [1]\n      note: \"R1-W5: 即使 TF 下 ThreadGate GAR-D = 0.02。干预仅在 τ-masked last token 成功，泛化性问题未讨论。\"\n  action_items:\n    - round: 4\n      action: \"讨论 GAR-ours vs GAR-D 差异的含义——为什么 last-token masking 成功但 Dongre 分布式衡量失败\"\n      assigned_to: paper_agent\n      status: open\n\n- id: \"R4-W2\"\n  summary: \"Table 1 四舍五入与正文数字精度不一致\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 4\n  last_seen_round: 4\n  mentions:\n    - round: 4\n      reviewers: [2]\n      note: \"R2-W6: §4.2 称 spread 为 0.75pp 但 Table 1 两位小数显示 1pp（0.50-0.51）。需增加精度或统一。\"\n  action_items:\n    - round: 4\n      action: \"Table 1 增加一位小数，或正文使用与 table 一致的精度\"\n      assigned_to: paper_agent\n      status: open\n\n- id: \"R4-W3\"\n  summary: \"r_min 数值正文未报告\"\n  category: method\n  severity: info\n  status: open\n  first_raised_round: 4\n  last_seen_round: 4\n  mentions:\n    - round: 4\n      reviewers: [1]\n      note: \"R1-M1: r_min 数值在正文中未报告，影响可复现性。\"\n  action_items:\n    - round: 4\n      action: \"在 §3 或 Appendix A 中报告 r_min 数值\"\n      assigned_to: paper_agent\n      status: open\n\n- id: \"R4-MR1\"\n  summary: \"缺少 Zhang et al. 2024 'Tell Your Model Where to Attend' 引用\"\n  category: framing\n  severity: info\n  status: open\n  first_raised_round: 4\n  last_seen_round: 4\n  mentions:\n    - round: 4\n      reviewers: [2]\n      note: \"与 β-steering 思路相似的推理时注意力操控方法，应在 §2 讨论。\"\n  action_items:\n    - round: 4\n      action: \"确认引用存在性并在 §2 Attention Manipulation 段落引用对比\"\n      assigned_to: paper_agent\n      status: open\n"
  }
}
```

</details>

---


### Tool result

_source line 287 · 2026-05-22T23:07:11.899884+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/review_issues.yaml\", \"bytes\": 23152}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9287ee173cf15d688adcd081f5d861f5:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 154
}
```

</details>

---
