# Director coordination — Part 4 of 5

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Conversation logs

[← Part 3](part-003.md) · [Transcript overview](../director-coordination-copy-2.md) · [Part 5 →](part-005.md) · [Structured JSON](../../../sessions/55/55aa43168feffca83e03.json)

## Round 93

### Tool call

_source line 955 · 2026-05-20T16:07:50.451012+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "2",
  "project": "vla-ssd",
  "text": "## Round 13 继续审稿：呈现性修改验证\n\n你是 Reviewer 2，负责验证论文的呈现性修改（格式、写作、引用）是否充分回应了 Round 12 的 issues。\n\n**Venue**: CoRL 2026 | **截止日期**: 2026-05-29 | **8 页正文** | **Double-blind** | `corl_2026` 模板\n\n**论文文件**:\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/main.pdf`\n\n**核心任务**：逐条检查以下 open issues，对每条标注 **[RESOLVED]**、**[PARTIALLY_RESOLVED]**、或 **[STILL_OPEN]** + 理由。同时检查修改是否引入新问题。\n\n---\n\n### Critical Issues 待验证\n\n**R12-N2 [critical] 正文超出 CoRL 8 页限制约 0.7 页**\n- Round 12 诊断：Discussion+Conclusion 延伸到第 9 页\n- 已观察到的修改：Conclusion 现在在第 8 页结束\n- 请精确测量：正文（§1-Conclusion）是否在 8 页内？References 从第几页开始？\n- 注意检查 `\\setlength` spacing hacks 是否在合理范围内\n\n**R12-N3 [critical] Abstract/Introduction 信息过载**\n- Round 12 诊断：Abstract 塞入 15+ 定量结果，Introduction 与 Abstract 高度重复\n- 已观察到的修改：Abstract 显著精简\n- 请验证：(a) Abstract 现在包含多少个定量值？是否降至合理水平？(b) Introduction 与 Abstract 的重复度是否降低？(c) 精简后是否丢失了关键信息？\n\n---\n\n### Warning Issues 待验证\n\n**R12-W1 [warning] 无首页 teaser figure**\n- 已观察到：Figure 1 现在在第 1 页，包含 (a) 架构概览 (b) instruction attention redistribution 图\n- 请验证：(a) Figure 1 是否有效传达核心发现？(b) Caption 是否自包含？(c) 尺寸和分辨率是否适当？\n\n**R12-W2 [warning] 层编号 off-by-one**\n- 已观察到：§3.2 修正为 \"L1–L32 the hidden states after each of the 32 transformer layers, with L32 including the final layer norm\"\n- 请验证：(a) 定义是否清晰？(b) 全文使用是否一致？(c) \"L32 including the final layer norm\" 是否有歧义（L32 是 transformer block 32 的输出，还是 layer norm 后的输出？）\n\n**R12-W3 [warning] 多条引用使用 arXiv 而非已发表版本**\n- 已观察到：OpenVLA [2] 改为 CoRL 2024 proceedings；Prismatic VLMs [7] 改为 ICML 2024；Häon [6] 改为 CoRL 2025 proceedings\n- 请验证：(a) 还有哪些引用仍使用 arXiv 但已有正式版本？(b) 特别检查 Llama 2 [10]、π₀ [14]、Belrose [23]\n\n**R12-W4 [warning] 缺失 6 篇重要 related work**\n- Round 12 提出 6 篇 missing references\n- 已观察到：新增了 [3] Seeing is Understanding, [4] Rethinking Causal Mask, [15] AVA-VLA, [43] visual token 相关\n- 请验证：6 篇中有多少被加入？是否有遗漏的关键文献？\n\n**R12-W5 [warning] 与 Grant/Häon 区分不够清晰**\n- 已观察到：Related Work \"Behavioral and mechanistic analysis of VLAs\" 段落新增显式对比\n- 请验证：(a) 对比内容是否准确？(b) 是否充分区分了 what (Häon) vs where (本文) vs feature-level (Grant)？\n\n---\n\n### Info Issues 待验证\n\n**R12-I1 [info] 术语不一致（readout token vs last_preaction 等）**\n- 请抽查 5 处使用，判断是否统一。\n\n**R12-I2 [info] Limitations 未作为独立 section**\n- 请确认当前 Limitations 的呈现形式。\n\n---\n\n### 新问题检查\n\n请特别关注：\n- 新增的 Figure 1（teaser）是否挤压了后续内容导致排版问题？\n- 新增引用后 reference 数量和格式是否规范？\n- Abstract 精简后是否读起来流畅？\n- Related Work 新段落是否与周围段落过渡自然？\n- 是否有新的 AI 写作痕迹？\n\n请以标准格式输出：Issue-by-Issue Verdict → New Issues → Strengths of Revision → Remaining Concerns → Updated Overall Assessment（含评分调整建议）。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "2",
    "project": "vla-ssd",
    "text": "## Round 13 继续审稿：呈现性修改验证\n\n你是 Reviewer 2，负责验证论文的呈现性修改（格式、写作、引用）是否充分回应了 Round 12 的 issues。\n\n**Venue**: CoRL 2026 | **截止日期**: 2026-05-29 | **8 页正文** | **Double-blind** | `corl_2026` 模板\n\n**论文文件**:\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/main.pdf`\n\n**核心任务**：逐条检查以下 open issues，对每条标注 **[RESOLVED]**、**[PARTIALLY_RESOLVED]**、或 **[STILL_OPEN]** + 理由。同时检查修改是否引入新问题。\n\n---\n\n### Critical Issues 待验证\n\n**R12-N2 [critical] 正文超出 CoRL 8 页限制约 0.7 页**\n- Round 12 诊断：Discussion+Conclusion 延伸到第 9 页\n- 已观察到的修改：Conclusion 现在在第 8 页结束\n- 请精确测量：正文（§1-Conclusion）是否在 8 页内？References 从第几页开始？\n- 注意检查 `\\setlength` spacing hacks 是否在合理范围内\n\n**R12-N3 [critical] Abstract/Introduction 信息过载**\n- Round 12 诊断：Abstract 塞入 15+ 定量结果，Introduction 与 Abstract 高度重复\n- 已观察到的修改：Abstract 显著精简\n- 请验证：(a) Abstract 现在包含多少个定量值？是否降至合理水平？(b) Introduction 与 Abstract 的重复度是否降低？(c) 精简后是否丢失了关键信息？\n\n---\n\n### Warning Issues 待验证\n\n**R12-W1 [warning] 无首页 teaser figure**\n- 已观察到：Figure 1 现在在第 1 页，包含 (a) 架构概览 (b) instruction attention redistribution 图\n- 请验证：(a) Figure 1 是否有效传达核心发现？(b) Caption 是否自包含？(c) 尺寸和分辨率是否适当？\n\n**R12-W2 [warning] 层编号 off-by-one**\n- 已观察到：§3.2 修正为 \"L1–L32 the hidden states after each of the 32 transformer layers, with L32 including the final layer norm\"\n- 请验证：(a) 定义是否清晰？(b) 全文使用是否一致？(c) \"L32 including the final layer norm\" 是否有歧义（L32 是 transformer block 32 的输出，还是 layer norm 后的输出？）\n\n**R12-W3 [warning] 多条引用使用 arXiv 而非已发表版本**\n- 已观察到：OpenVLA [2] 改为 CoRL 2024 proceedings；Prismatic VLMs [7] 改为 ICML 2024；Häon [6] 改为 CoRL 2025 proceedings\n- 请验证：(a) 还有哪些引用仍使用 arXiv 但已有正式版本？(b) 特别检查 Llama 2 [10]、π₀ [14]、Belrose [23]\n\n**R12-W4 [warning] 缺失 6 篇重要 related work**\n- Round 12 提出 6 篇 missing references\n- 已观察到：新增了 [3] Seeing is Understanding, [4] Rethinking Causal Mask, [15] AVA-VLA, [43] visual token 相关\n- 请验证：6 篇中有多少被加入？是否有遗漏的关键文献？\n\n**R12-W5 [warning] 与 Grant/Häon 区分不够清晰**\n- 已观察到：Related Work \"Behavioral and mechanistic analysis of VLAs\" 段落新增显式对比\n- 请验证：(a) 对比内容是否准确？(b) 是否充分区分了 what (Häon) vs where (本文) vs feature-level (Grant)？\n\n---\n\n### Info Issues 待验证\n\n**R12-I1 [info] 术语不一致（readout token vs last_preaction 等）**\n- 请抽查 5 处使用，判断是否统一。\n\n**R12-I2 [info] Limitations 未作为独立 section**\n- 请确认当前 Limitations 的呈现形式。\n\n---\n\n### 新问题检查\n\n请特别关注：\n- 新增的 Figure 1（teaser）是否挤压了后续内容导致排版问题？\n- 新增引用后 reference 数量和格式是否规范？\n- Abstract 精简后是否读起来流畅？\n- Related Work 新段落是否与周围段落过渡自然？\n- 是否有新的 AI 写作痕迹？\n\n请以标准格式输出：Issue-by-Issue Verdict → New Issues → Strengths of Revision → Remaining Concerns → Updated Overall Assessment（含评分调整建议）。"
  }
}
```

</details>

---


### Tool result

_source line 956 · 2026-05-20T16:07:51.858594+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1407
}
```

</details>

---


### Assistant

_source line 957 · 2026-05-20T16:09:43.618640+00:00_

Round 13 审稿进行中，已派发两位 Reviewer 和视觉审查 Agent，正在等待审稿结果返回：

- **Reviewer 1**（实质性修改验证）：framing/overclaiming、CoRL 相关性、跨架构声明等
- **Reviewer 2**（呈现质量验证）：页数合规、摘要、teaser figure、参考文献、related work 等
- **视觉审查 Agent**：PDF 排版质量检查

收到 Reviewer 审稿意见后，将进行交叉分享 → 收敛判断 → 汇总报告。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director"
}
```

</details>

---


## Round 94

## Round 94

2 recorded events


### User

_source line 958 · 2026-05-20T16:13:13.163776+00:00_

[Reviewer 1 审稿意见]:

# Reviewer 1 — Round 13 修改验证报告

**论文**: "Vision Encodes, Language Reorganizes: Token-Level Representational Analysis of VLA Fine-Tuning"
**Venue**: CoRL 2026

---

## Issue-by-Issue Verdict

---

### R12-N1 [critical] 因果 overclaiming：Title "Routes" + weak specificity

**[RESOLVED]**

验证结果：

**(a) Title**: "Language Routes" → "Language Reorganizes"，副标题 "Functional Specialization" → "Representational Analysis"。"Reorganizes" 描述的是 observational pattern（attention distribution 的重组），不暗示已被证实的因果机制。相比 "Routes"（暗示主动的信息转发机制），"Reorganizes" 是对 attention redistribution 现象的恰当描述。

**(b) 全文一致性**：对全部 .tex 文件执行 grep `\brouting\b`，**返回零匹配**。所有关键位置均已替换：
- Section 4.3 标题: "VLA Fine-Tuning **Redistributes** Instruction Attention"（原 "Front-Loads Instruction Routing"）
- experiments.tex line 53: "a **redistribution** beyond inherited priors"
- experiments.tex line 84: "instruction attention **redistribution** is an entry-layer phenomenon"
- discussion.tex line 6: "**redistributes** instruction attention rather than reshaping visual geometry"
- discussion.tex line 7: "Seven analyses support L1 **redistribution**"
- conclusion.tex: "**redistributes** instruction attention to entry-exit layers"

清理非常彻底。唯一保留的 "mechanism" 出现在 method.tex line 42（"revealing the mechanism through which instruction information reaches the readout token"），这是对分析目标的描述，不是因果声称，可接受。

**(c) 三级证据分类**：Discussion §5 保留了 "interventional (dose-response, counterfactual) / supporting (gradient, ablation, trajectory) / constraining (p-values, z-scores)" 分类。在 "redistributes" 框架下，此分类更为恰当——dose-response 和 counterfactual ablation 确实是 interventional 手段（即使是 crude interventions），且论文不再声称这些 intervention 揭示了因果 "routing mechanism"，而是描述了 attention redistribution 的功能后果。

---

### R4-N1 [critical] Finding 3（image token instruction-blindness）是架构必然结果

**[RESOLVED]**

**(a) Abstract 措辞**：
- 旧版: "Token-level analysis **reveals strict** functional specialization"
- 新版: "token-level analysis **confirms expected** functional specialization—image tokens remain instruction-blind while the readout token integrates multimodal information—**consistent with the causal attention mask and serving as a framework sanity check**"

"confirms expected" + "consistent with the causal attention mask" + "framework sanity check" 三重降格，充分承认这是架构约束的验证而非实证发现。

**(b) Title "Vision Encodes"**：仍保留。这可以有两种理解：(1) 声称发现了 vision tokens 的行为（overclaiming），或 (2) 描述模型的功能组织（vision modality 负责 encoding）。在 Abstract 和正文已明确标注为 sanity check 的前提下，Title 作为修辞性 shorthand 可以接受。如果 R2 仍有异议，可进一步讨论，但我认为当前处理已达到 reasonable balance。

**(c) Contributions 列表**（Introduction line 21）：
- Contribution (iii): "a systematic framework for token-level representational analysis of VLAs with factorial controls, **including token specialization as a methodology validation**"

Finding 3 被明确定位为方法论验证（methodology validation），不再作为独立发现呈现。这是恰当的处理。

---

### R9-N1 [wont_fix] 跨架构泛化不足

**[RESOLVED]** — claim 已恰当弱化

**(a) 全文一致性**：关键位置均使用限定语：
- Abstract: "across two **causal-decoder** VLA architectures"
- Introduction line 18: "two **causal-decoder** VLAs"
- Introduction line 21 (Contributions): "**two causal-decoder** VLAs" + "the two **causal-decoder architectures studied**"
- experiments.tex line 71: "consistent across **causal-decoder** architectures"
- experiments.tex line 73: "convergent reorganization across **the two architectures studied**"
- Conclusion: "consistent across **two causal-decoder** VLAs"

qualification 非常一致。未发现任何 unqualified generalization。

**(b) Limitations**（discussion.tex lines 10-11）：明确指出 "Both architectures are causal-decoder; **flow-matching [π₀] and diffusion [Octo] VLAs use cross-attention**, so findings may not generalize to non-autoregressive decoders." 直接回应了 R2-N3 关于缺少 flow-matching/diffusion 架构的批评。

**(c) Discussion 预测**：已移除。旧版 Discussion 包含 "cross-attention VLAs should lack L1 routing heads" 等推测性预测。新版 Discussion 更聚焦于已有证据的总结。

---

### R9-N2 [wont_fix] 无 closed-loop 机器人评估

**[PARTIALLY_RESOLVED]** — 诚实承认但 framing 有问题

discussion.tex lines 13-14:
> "All analyses are open-loop, as in concurrent VLA representation studies [Grant, Häon]; however, representational analysis has independent design value—our entry-exit profile yields a concrete diagnostic (L1 attention entropy monitoring during fine-tuning), and the readout-vs-image dissociation directly informs token pruning strategies. Closed-loop validation on downstream task success is **an orthogonal contribution** and a natural next step."

**正面**：(1) 诚实承认 open-loop；(2) 引用同期工作（Grant, Häon）建立 precedent；(3) 给出两个具体的 actionable implications（L1 attention entropy 监控、token pruning）。

**问题**："orthogonal contribution" 措辞暗示 closed-loop validation 是独立的、可选的研究方向，而非验证本文 claims 的必要步骤。实际上，只有 closed-loop 实验才能验证 "attention redistribution 对任务成功率的影响" 这一关键问题。"Orthogonal" 一词过于 dismissive。建议改为 "a complementary and necessary next step" 或 "an essential validation step that we leave for future work"。

此外，两个 actionable implications 仍未被实验验证——论文没有实际实现 L1 attention entropy 监控或 token pruning。这些仍是推测性建议。

---

### R9-W1 [critical→open] CoRL scope fit

**[PARTIALLY_RESOLVED]**

相比旧版的改善：
1. Discussion 现在提出了两个具体的 robotics-relevant implications（L1 entropy 监控、token pruning strategy），而非之前的宽泛预测
2. Limitations 诚实承认了 open-loop 和架构局限
3. Related Work 更好地定位了论文在 VLA 研究中的位置

仍然存在的问题：
1. 两个 actionable implications 均未经验证——仍是推测性建议
2. "representational analysis has independent design value" 的论证力度对 CoRL 审稿人而言可能不足
3. 无 LIBERO rollout、无 real-robot、无 sim-to-real evidence

**我的判断**：论文在 scope framing 上有明显改善，但核心缺陷（纯 open-loop 分析）无法仅通过 writing 修改解决。对 CoRL 而言，这仍是一个 borderline concern，但鉴于同期 VLA 解释性工作（Grant 2026, Häon 2025, Swann 2026）也是 open-loop 分析，论文至少与该新兴子领域的标准一致。

---

### R9-W4 [warning] Cohen's d 独立性

**[RESOLVED]**

experiments.tex line 87:
> "token-level Cohen's d = 0.65; **trajectory-level d = 2.943**, Appendix"

现在同时报告 token-level 和 trajectory-level d。trajectory-level d (2.943) 是在 demo 层面聚合后计算的，避免了 token-level 的独立性问题。两者同时报告使读者可以评估聚合层级对 effect size 的影响。

---

### R12-W6 [warning] FDR 校正细节

**[RESOLVED]**

experiments.tex line 147:
> "surviving **Benjamini–Hochberg** FDR correction (**α = 0.05**, **33-layer family per metric**) at 29–30/33 layers."

现在明确指定：(1) BH 方法、(2) α = 0.05、(3) 33-layer family per metric（即每个 metric 独立做 33 次比较的校正）。完整且透明。

---

### R12-DIV1 [warning] Title "Language Routes" 误导

**[RESOLVED]**

"Language Routes" → "Language Reorganizes"。"Reorganizes" 准确描述了 attention distribution 的重组现象，不暗示主动的信息转发机制。全文 grep 确认零残留 "routing"。

---

## 新问题检查

### NEW-1 [minor] Title "Language Reorganizes" — "Language" 仍作为 agent

Title "Vision Encodes, Language **Reorganizes**" 中，"Language" 是语法主语，暗示语言 token 主动执行了 reorganization。更准确地说，是 **VLA fine-tuning** reorganizes attention patterns，而非 language tokens 自身。但这是一个修辞性 title convention（类似 "Attention Is All You Need" 中 attention 也不是 literal agent），且正文已全面使用 "VLA fine-tuning redistributes" 的准确措辞。

**严重程度**：info。不影响接收决定。

### NEW-2 [minor] "Orthogonal contribution" framing 过于 dismissive

如上 R9-N2 分析所述。"Orthogonal" 暗示 closed-loop 验证与本文 claims 无关，而实际上它是验证本文 claims 实用价值的必要步骤。

**严重程度**：warning。建议在 camera-ready 中修改措辞。

### NEW-3 [info] 附录中 "convergent" 措辞较主文更强

主文 (experiments.tex line 73): "**consistent with** convergent reorganization" — 恰当的 hedging
附录 (appendix.tex line 904): "This convergent outcome from divergent starting points suggests that mid-layer action specialization is a **robust attractor** of VLA training" — 较强的因果暗示

"Robust attractor" 暗示动力系统的稳定固定点，从 N=2 架构观察中得出这一结论偏强。但这在附录中，不影响主文 claims。

**严重程度**：info。

### NEW-4 [info] 页面压缩激进

main.tex 的 spacing 参数（\textfloatsep=6pt, \abovecaptionskip=2pt, \vspace{-2pt} before §5）较为激进。Discussion 被压缩到 page 8 的下半部分。视觉上不影响可读性，但接近 CoRL 格式规范的边界。当前版本 main text 约 8 页，References 从 page 9 开始，符合页限。

**严重程度**：info。在限制内。

### 未引入重大新问题

Abstract 精简后仍保留了三个 findings 的核心信息（redistributes attention、middle-layer peak、expected specialization as sanity check），加上关键数字（R² +0.069, Δ=0.003）。未丢失关键信息。跨架构 claim 弱化后，论文的核心贡献（attention redistribution phenomenon + systematic analysis framework）仍然成立。

---

## Strengths of Revision

1. **语言一致性极高**：全文 grep 确认零残留 "routing" 和 "strict"。从 Title 到 Conclusion，"redistributes instruction attention" 贯穿始终。这是非常认真的修改。

2. **Finding 3 的降格处理精准**：Abstract "confirms expected" + "causal attention mask" + "framework sanity check" 三重标注；Contribution (iii) 定位为 "methodology validation"；Section 4.2 title 保持 "Framework Validation"。没有过度削弱（sanity check 仍然有方法论价值），也没有残留 overclaiming。

3. **跨架构限定一致彻底**：所有出现 cross-architecture claim 的位置（7+处）均加上 "causal-decoder" 或 "the two architectures studied" 限定。Limitations 明确列出 flow-matching/diffusion 架构。

4. **Teaser figure 添加**：page 1 现在有 Figure 1（架构 overview + attention redistribution 图），显著改善了首页可读性。

5. **Missing references 全部补充**：wang2025seeing, pei2025rethinking (causal mask papers), xiao2025ava (AVA-VLA), fan2026visual, neo2025interpreting, long2026understanding, wei2024phase (VLM token analysis) — Related Work 覆盖面显著增强。

6. **技术修复完成**：层编号修正（L1-L32）、Cohen's d 双级报告（token + trajectory）、FDR 细节完整（BH, α=0.05, 33-layer family）。

7. **Related Work 显式区分**：Related Work lines 18-20 明确区分 Grant ("what" features dominate)、Häon ("what" semantic directions)、本文 ("where" across layers and token positions)。

---

## Remaining Concerns

| Issue | Status | 严重程度 | 备注 |
|-------|--------|---------|------|
| R9-N2 closed-loop | PARTIALLY_RESOLVED | warning | "orthogonal contribution" 措辞 dismissive，且 actionable implications 仍未验证 |
| R9-W1 CoRL scope | PARTIALLY_RESOLVED | warning | 改善明显但核心缺陷（open-loop only）无法仅通过 writing 解决 |
| NEW-1 "Language" as agent in title | info | — | 修辞性 convention，正文已准确 |
| NEW-2 "orthogonal" framing | warning | — | 建议 camera-ready 修改 |
| NEW-3 附录 "robust attractor" | info | — | 仅在附录，不影响主文 |

---

## Updated Overall Assessment

**Overall**: 3.5 / 5（Borderline Accept，上调 0.5）
**Confidence**: 4 / 5

**评分变化理由**：

从 3.0 上调至 3.5，基于以下改善：
1. 因果语言的全面修正消除了最严重的 methodological criticism（R12-N1 fully resolved）
2. Finding 3 的 framing 修正使论文 claims 与 evidence 匹配（R4-N1 fully resolved）
3. 跨架构 claim 的诚实限定增强了可信度（R9-N1 resolved）
4. 多项技术修复（层编号、Cohen's d 双级、FDR 细节）提升了严谨性
5. 新增 teaser figure 和 missing references 改善了整体呈现

**未上调至 4.0 的原因**：
1. 纯 open-loop 分析对 CoRL 仍是核心局限——论文仍无法回答 "这些 attention patterns 对机器人实际执行有什么影响？"
2. Actionable implications（L1 entropy 监控、token pruning）仍为推测性建议
3. "Orthogonal contribution" framing 暗示对 closed-loop 验证的回避态度

**我对接收的态度**：如果 committee 认为 VLA 解释性分析本身对 CoRL 有价值（类似接受 Grant 2026、Häon 2025 等同类工作），本文的 methodological rigor 和 revision quality 足以支持 borderline accept。如果 committee 要求 closed-loop evidence，则仍在 reject 边界。我的评分反映了这一不确定性。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 959 · 2026-05-20T16:13:27.809278+00:00_

Reviewer 1 报告已收到。评分从 3.0 上调至 3.5/5（Borderline Accept）。

主要结论：
- **5 项 RESOLVED**：R12-N1（overclaiming）、R4-N1（Finding 3 架构必然性）、R9-N1（跨架构泛化）、R12-W6（FDR）、R12-DIV1（title 误导）
- **2 项 PARTIALLY_RESOLVED**：R9-N2（closed-loop，"orthogonal contribution" 措辞 dismissive）、R9-W1（CoRL scope，open-loop 核心局限无法靠 writing 解决）
- **4 项新发现**：均为 info/minor 级别，不影响接收决定

等待 Reviewer 2 报告到达后启动交叉分享。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director"
}
```

</details>

---


## Round 95

## Round 95

8 recorded events


### User

_source line 960 · 2026-05-20T16:13:33.676785+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 Round 2 验证报告：呈现性修改

---

## Issue-by-Issue Verdict

### Critical Issues

**R12-N2 [critical] 正文超出 CoRL 8 页限制 → [RESOLVED]**

精确测量：Section 5 (Discussion) 的 "Conclusions" 段落在 page 8 底部结束，最后一句为 "Code and data will be released upon acceptance." References 从 page 9 顶部开始。正文（§1–Conclusions）严格控制在 8 页内。

**Spacing hacks 评估**：main.tex 第 16-22 行使用了 6 个 `\setlength` 命令压缩浮动体间距：
- `\textfloatsep`: 6pt（默认 ~20pt，压缩约 70%）
- `\intextsep`: 6pt（默认 ~12pt）
- `\abovecaptionskip`: 2pt（默认 ~10pt）
- `\belowdisplayskip`: 6pt（默认 ~12pt）

这些压缩幅度较大但尚在可接受范围内——从 PDF 渲染效果看，图表与正文之间仍有可辨识的间隔，文本不显拥挤。CoRL 模板未明确禁止此类调整。许多顶会投稿使用类似策略。**判定：合规但处于边界**。如 reviewer 对排版敏感，可能被标记。

---

**R12-N3 [critical] Abstract/Introduction 信息过载 → [RESOLVED]**

**(a) Abstract 定量值数量**：
- 旧版：15+ 个显式数值（r=0.48→0.61, α=0.63-0.67, p=0.032, R²Δ≈+0.001, Δρ=0.017, Δ<0.001 等）
- 新版：仅 "32 LLM layers" 1 个结构性数值 + 3 个 section 引用（§4.3, §4.4, §4.2）
- **从 15+ 降至 ~1 个定量值**，改善显著

**(b) Introduction 与 Abstract 重复度**：
- 新版 Introduction（page 2）增加了方法论细节（"four complementary analyses: cross-instruction probes, L1 attention pattern analysis, RSA, MLP probes"）和对比定位（"Existing analyses have not combined systematic per-layer probing with factorial controls"），不再逐字重复 abstract
- Introduction 中仅保留 R²≈0.001 和 Δ≈0.01 两个数值，且出现在不同叙事语境中
- 重复度大幅降低

**(c) 关键信息保留**：
- 三个 findings 的 high-level 描述完整保留
- 方法论框架（factorial controls, 7 complementary analyses）保留
- 仅删去了过度细致的 inline 数值，未丢失核心论点

---

### Warning Issues

**R12-W1 [warning] 无首页 teaser figure → [RESOLVED]**

Figure 1 现在位于 page 1 顶部，包含：
- **(a) Architecture overview**：清晰展示 vision encoder → projector → LLM backbone → action tokens 的 pipeline，标注了 image/instruction/readout token 位置
- **(b) Instruction attention redistribution**：per-layer instruction-dominant heads 对比图，三条件（VLA-trained / Pretrained / Untrained）颜色区分明确

**(a) 信息传达**：Figure 1 有效传达了核心发现——VLA 训练如何重新分配 instruction attention。读者在读 abstract 后即可通过图表理解主要 pattern。✓
**(b) Caption 自包含性**：Caption 完整解释了每个 panel 的含义和关键观察（"Pretrained Llama-2 peaks at mid-depth; VLA-trained OpenVLA concentrates at L1 and L32"）。✓
**(c) 尺寸/分辨率**：`width=0.88\linewidth, height=2in, keepaspectratio`，在单栏页面上比例合理，文字清晰可读。✓

---

**R12-W2 [warning] 层编号 off-by-one → [RESOLVED]**

**(a) 新定义**（Section 3.2, page 3-4）："Throughout, L0 denotes the embedding layer output, L1 to L32 the hidden states after each of the 32 transformer layers, with L32 including the final layer norm."
- L1-L32 = 32 个索引 = 32 个 transformer layers ✓，off-by-one 已修正

**(b) 全文一致性**：抽查确认——
- Figure 1 caption: "L1 and L32" ✓
- Section 4.3 (page 5-6): 引用 L1 层 ✓
- Table 2 (page 7): 层索引与新约定一致 ✓
- Figure 3 (page 8): x 轴标签与 L1-L32 约定一致 ✓

**(c) L32 歧义**：轻微残留问题。"L32 including the final layer norm" 有两种解读：(i) L32 = transformer block 32 输出 + final LN（即 LN 后的输出），(ii) L32 = transformer block 32 输出（其中包含 block 内的 LN）。根据 Llama-2 HuggingFace 实现，L32 应是第 32 个 decoder block 的输出经过 final RMSNorm 后的 hidden state。建议改为 "L32 denotes the output after the final layer norm applied to the 32nd transformer layer" 以消除歧义。**影响极小，不阻碍理解。**

---

**R12-W3 [warning] arXiv 引用 → [PARTIALLY_RESOLVED]**

已修正（3/3 被要求修改的）：
- ✅ kim2024_openvla: arXiv → CoRL 2024 proceedings
- ✅ karamcheti2024: arXiv → ICML 2024
- ✅ haon2025: arXiv → CoRL 2025 proceedings

仍为 arXiv 但有正式出版版本（2 条）：
- ⚠️ belrose2023_tunedlens: 仍为 "arXiv:2303.08112"，但已发表于 **NeurIPS 2023**
- ⚠️ padalkar2023_oxe: 仍为 "arXiv:2310.08864"，但已发表于 **ICRA 2024**

以下 arXiv 引用无正式出版版本，保持现状合理：
- touvron2023_llama2（技术报告）、brohan2023_rt2（技术报告）、black2024_pi0（2024 arXiv）
- 各 2025-2026 年 VLA interpretability 新工作（grant2026, swann2026, buurmeijer2026 等）

**建议**：更新 belrose2023 和 padalkar2023 为正式出版版本。低优先级修复。

---

**R12-W4 [warning] 缺失 6 篇 related work → [RESOLVED]**

全部 6/6 已添加并在正文中引用：

| # | 论文 | Bib key | 引用位置 |
|---|------|---------|----------|
| 1 | "What Do Visual Tokens Really Encode?" (CVPR 2026) | fan2026visual | related_work.tex L24 |
| 2 | "Towards Interpreting Visual Information Processing in VLMs" (ICLR 2025) | neo2025interpreting | related_work.tex L24 |
| 3 | "Seeing is Understanding" (arXiv:2503.02597) | wang2025seeing | introduction.tex L5 |
| 4 | "Phase Diagram of VLM Inference" (arXiv:2411.00646) | wei2024phase | related_work.tex L24 |
| 5 | "Understanding Language Prior of LVLMs" (ICLR 2026) | long2026understanding | related_work.tex L24 |
| 6 | AVA-VLA (CVPR 2026) | xiao2025ava | related_work.tex L4 |

额外添加：pei2025rethinking ("Rethinking Causal Mask Attention", arXiv:2505.18605) — 在 introduction.tex L5 引用，支持 causal mask 对 visual token 影响的讨论。

引用总数从 52 增至 59（+7），cross-check 显示 0 orphan + 0 missing，格式规范。

---

**R12-W5 [warning] 与 Grant/Häon 区分不够清晰 → [RESOLVED]**

Related Work (page 2-3) 新增显式对比段落：

- **Grant et al. [5]**：定位为 "feature-level mechanistic study" + "found visual dominance" → feature-level analysis
- **Häon et al. [6]**：定位为 "identified sparse semantic directions linked to action selection" → addressing *what* to steer
- **本文**：定位为 "where in the processing pipeline information is routed" + "systematic per-layer probing with factorial trained/pretrained/untrained controls" → *where* + controlled comparison

对比准确且充分区分了三者的 level of analysis（feature-level / steering-direction / token-level per-layer）和研究问题（visual dominance / what to steer / where routing happens）。新段落自然衔接了前述 VLA 系统工作的描述和后续方法论 gap 的论述。

---

### Info Issues

**R12-I1 [info] 术语一致性 → [PARTIALLY_RESOLVED]**

抽查 5 处：
1. Abstract (page 1): "readout token" ✓
2. Section 3.2 (page 3): "LLM readout" — 指代相同概念但措辞稍异
3. Section 4.2 (page 5): "Readout token as multimodal hub" ✓
4. Table 1 (page 5): 列标签使用 "last_preaction" — 技术标签，与叙事文本的 "readout token" 存在命名差异
5. Section 4.3 (page 6): "readout position" ✓

**判定**：叙事文本中 "readout token" 基本统一。Table 1 的 "last_preaction" 是代码层面的技术标签，与 "readout token" 的映射在 Section 3.2 中有定义。可接受，但建议在 Table 1 caption 中加一句 "(last_preaction = readout token)" 以明确对应。

---

**R12-I2 [info] Limitations 独立 section → [PARTIALLY_RESOLVED]**

当前呈现：Section 5 中使用加粗段落标题 "**Limitations and scope.**" 和 "**Conclusions.**"，而非独立 `\subsection`。内容覆盖了关键 limitations（仅 2 架构、仅 LIBERO、causal-decoder 架构限制、cross-attention 架构不适用性）。

CoRL 2026 要求 "include a Limitations section" 但未要求必须是独立编号 section。当前格式在技术上合规，但将其改为 `\subsection*{Limitations}` 可更明确满足要求。低优先级。

---

## New Issues 检查

**NEW-1 [info] Title 变更：需确认与审稿流程的一致性**

标题从 "Vision Encodes, Language **Routes**" 改为 "Vision Encodes, Language **Reorganizes**"。这显著改善了我在 Round 1 W1 中指出的 "Routes 暗示因果机制" 问题——"Reorganizes" 更准确描述了 fine-tuning 的效果（重新组织 attention patterns），避免了因果性 overclaim。

但 "Language Reorganizes" 仍有轻微不精确：严格来说是 LLM backbone（而非 "language"）在 reorganize。不过这是可接受的修辞手法。**不构成问题。**

**NEW-2 [positive] "expected functional specialization" 措辞改善**

Abstract 现在将 Finding 3 描述为 "expected functional specialization—...consistent with the causal attention mask and serving as a framework sanity check"。这直接回应了我 Round 1 N1 的核心关切（image token instruction-blindness 是 causal mask 的架构约束）。论文不再将此作为 novel finding 呈现，而是明确定位为 validation/sanity check。**重大改善。**

**NEW-3 [info] Spacing 压缩的边界效应**

`\textfloatsep` 从默认 ~20pt 压缩到 6pt 使得部分图表与正文之间的视觉间隔偏紧（特别是 page 5-6 的 Table 1 和 Table 2 区域），但未达到不可读程度。CoRL 模板未禁止此操作。如果有余量，建议将 `\textfloatsep` 恢复至 8-10pt。

**NEW-4 [info] 无新增 AI 写作痕迹**

新增文本（abstract、introduction、related work 新段落）读感自然，未发现典型 AI 写作模式（如 "Notably"、"It is worth noting"、"In this paper, we" 等）。句式变化合理，学术用语规范。

---

## Strengths of Revision

1. **Abstract 精简效果显著**：从 15+ 定量值压缩到 ~1 个，三个 findings 以清晰的 First/Second/Third 结构呈现，可读性大幅提升
2. **Figure 1 teaser 有效**：page 1 的架构概览 + attention redistribution 图为读者提供了即时的视觉理解入口
3. **所有 6 篇缺失引用均已补齐**：且正确放置在 related work 的对应段落中，引用格式规范
4. **Finding 3 的定位修正**：从 "novel finding" 降级为 "framework sanity check, consistent with causal attention mask"——这是对 R2-N1 最核心关切的直接回应
5. **Title 修改合理**："Routes" → "Reorganizes" 降低了因果性 overclaim
6. **Related Work 区分度提升**：Grant/Häon/本文的 what-vs-where-vs-feature-level 区分清晰
7. **页面控制在限制内**：尽管使用了 spacing hacks，但最终效果合规且可读

---

## Remaining Concerns

1. **[minor] 2 条引用仍可更新为正式出版版本**（belrose2023 → NeurIPS 2023, padalkar2023 → ICRA 2024）
2. **[minor] L32 定义的轻微歧义**（transformer output vs post-LN output）
3. **[minor] Table 1 的 "last_preaction" 与正文 "readout token" 的映射可在 caption 中显式说明
4. **[minor] Spacing 压缩处于边界**，`\textfloatsep` = 6pt 偏紧

以上均为低优先级修复，不影响接收决定。

---

## Updated Overall Assessment

**呈现性修改评分调整建议**：

| 维度 | Round 1 | Round 2 | 变化原因 |
|------|---------|---------|----------|
| Clarity | 7/10 | 8/10 | Abstract 精简、Figure 1 teaser、Introduction 冗余消除、术语改善 |
| Format compliance | 未单独评 | Pass | 8 页内、引用完整、模板正确 |

**其他维度（Originality, Quality, Significance, Relevance）不在本轮验证范围内，评分不变。**

本轮修改有效回应了所有 critical 呈现性问题和大部分 warning 问题。剩余的 minor 问题可在 camera-ready 阶段处理。呈现性修改质量较高，未引入新的实质性问题。

---

[Reviewer 1 审稿结果]:
Round 13 验证报告已提交。

核心结论：6 个 critical/warning issues 中 4 个 fully resolved（因果 overclaiming、Finding 3 降格、跨架构限定、FDR/Cohen's d 技术修复），2 个 partially resolved（closed-loop 缺失的 framing、CoRL scope fit）。评分建议从 3.0 上调至 3.5/5（Borderline Accept）。主要残留问题是 "orthogonal contribution" 对 closed-loop 验证的 dismissive 措辞，以及 actionable implications 仍未经实验验证。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 961 · 2026-05-20T16:13:53.815585+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_post_to_reviewer",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_post_to_reviewer",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 962 · 2026-05-20T16:13:53.866171+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 963 · 2026-05-20T16:14:14.332650+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "13",
  "text": "以下是 Reviewer 2 的完整 Round 13 验证报告，请逐条回应：对每个判定，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 Round 2 验证报告：呈现性修改\n\n### Critical Issues\n\n**R12-N2 [critical] 正文超出 CoRL 8 页限制 → [RESOLVED]**\n精确测量：Section 5 (Discussion) 的 \"Conclusions\" 段落在 page 8 底部结束。References 从 page 9 顶部开始。正文严格控制在 8 页内。Spacing hacks（\\textfloatsep=6pt, \\abovecaptionskip=2pt 等）压缩幅度较大但尚在可接受范围内。判定：合规但处于边界。\n\n**R12-N3 [critical] Abstract/Introduction 信息过载 → [RESOLVED]**\nAbstract 定量值从 15+ 降至 ~1 个。Introduction 不再逐字重复 abstract。关键信息保留完整。\n\n### Warning Issues\n\n**R12-W1 [warning] 无首页 teaser figure → [RESOLVED]**\nFigure 1 位于 page 1 顶部，包含 architecture overview + instruction attention redistribution 对比图。Caption 自包含，尺寸合理。\n\n**R12-W2 [warning] 层编号 off-by-one → [RESOLVED]**\nL1-L32 = 32 层，全文一致。轻微残留：L32 定义歧义（transformer output vs post-LN output），影响极小。\n\n**R12-W3 [warning] arXiv 引用 → [PARTIALLY_RESOLVED]**\n3/3 被要求修改的已更新。仍有 2 条可更新：belrose2023（→NeurIPS 2023）、padalkar2023（→ICRA 2024）。\n\n**R12-W4 [warning] 缺失 6 篇 related work → [RESOLVED]**\n全部 6/6 已添加并正确引用。引用总数 52→59，0 orphan + 0 missing。\n\n**R12-W5 [warning] 与 Grant/Häon 区分不够清晰 → [RESOLVED]**\n新增显式对比段落，what-vs-where-vs-feature-level 区分清晰。\n\n### Info Issues\n\n**R12-I1 [info] 术语一致性 → [PARTIALLY_RESOLVED]**\n叙事文本中 \"readout token\" 基本统一。Table 1 的 \"last_preaction\" 是代码技术标签，建议 caption 中加映射说明。\n\n**R12-I2 [info] Limitations 独立 section → [PARTIALLY_RESOLVED]**\n使用加粗段落标题而非独立 \\subsection。技术上合规，低优先级。\n\n### New Issues\n- NEW-1 [info]: Title 变更一致性，不构成问题\n- NEW-2 [positive]: Finding 3 \"expected functional specialization\" 措辞改善\n- NEW-3 [info]: Spacing 压缩边界效应（\\textfloatsep=6pt 偏紧）\n- NEW-4 [info]: 无 AI 写作痕迹\n\n### Remaining Concerns\n1. [minor] 2 条引用可更新为正式出版版本\n2. [minor] L32 定义轻微歧义\n3. [minor] Table 1 caption 可显式说明 last_preaction = readout token\n4. [minor] Spacing 压缩处于边界\n\nClarity 评分：7→8/10。\n\n---\n\n请逐条回应。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "13",
    "text": "以下是 Reviewer 2 的完整 Round 13 验证报告，请逐条回应：对每个判定，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 Round 2 验证报告：呈现性修改\n\n### Critical Issues\n\n**R12-N2 [critical] 正文超出 CoRL 8 页限制 → [RESOLVED]**\n精确测量：Section 5 (Discussion) 的 \"Conclusions\" 段落在 page 8 底部结束。References 从 page 9 顶部开始。正文严格控制在 8 页内。Spacing hacks（\\textfloatsep=6pt, \\abovecaptionskip=2pt 等）压缩幅度较大但尚在可接受范围内。判定：合规但处于边界。\n\n**R12-N3 [critical] Abstract/Introduction 信息过载 → [RESOLVED]**\nAbstract 定量值从 15+ 降至 ~1 个。Introduction 不再逐字重复 abstract。关键信息保留完整。\n\n### Warning Issues\n\n**R12-W1 [warning] 无首页 teaser figure → [RESOLVED]**\nFigure 1 位于 page 1 顶部，包含 architecture overview + instruction attention redistribution 对比图。Caption 自包含，尺寸合理。\n\n**R12-W2 [warning] 层编号 off-by-one → [RESOLVED]**\nL1-L32 = 32 层，全文一致。轻微残留：L32 定义歧义（transformer output vs post-LN output），影响极小。\n\n**R12-W3 [warning] arXiv 引用 → [PARTIALLY_RESOLVED]**\n3/3 被要求修改的已更新。仍有 2 条可更新：belrose2023（→NeurIPS 2023）、padalkar2023（→ICRA 2024）。\n\n**R12-W4 [warning] 缺失 6 篇 related work → [RESOLVED]**\n全部 6/6 已添加并正确引用。引用总数 52→59，0 orphan + 0 missing。\n\n**R12-W5 [warning] 与 Grant/Häon 区分不够清晰 → [RESOLVED]**\n新增显式对比段落，what-vs-where-vs-feature-level 区分清晰。\n\n### Info Issues\n\n**R12-I1 [info] 术语一致性 → [PARTIALLY_RESOLVED]**\n叙事文本中 \"readout token\" 基本统一。Table 1 的 \"last_preaction\" 是代码技术标签，建议 caption 中加映射说明。\n\n**R12-I2 [info] Limitations 独立 section → [PARTIALLY_RESOLVED]**\n使用加粗段落标题而非独立 \\subsection。技术上合规，低优先级。\n\n### New Issues\n- NEW-1 [info]: Title 变更一致性，不构成问题\n- NEW-2 [positive]: Finding 3 \"expected functional specialization\" 措辞改善\n- NEW-3 [info]: Spacing 压缩边界效应（\\textfloatsep=6pt 偏紧）\n- NEW-4 [info]: 无 AI 写作痕迹\n\n### Remaining Concerns\n1. [minor] 2 条引用可更新为正式出版版本\n2. [minor] L32 定义轻微歧义\n3. [minor] Table 1 caption 可显式说明 last_preaction = readout token\n4. [minor] Spacing 压缩处于边界\n\nClarity 评分：7→8/10。\n\n---\n\n请逐条回应。"
  }
}
```

</details>

---


### Tool result

_source line 964 · 2026-05-20T16:14:38.418421+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 24085
}
```

</details>

---


### Tool call

_source line 965 · 2026-05-20T16:14:38.571119+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "13",
  "text": "以下是 Reviewer 1 的完整 Round 13 验证报告，请逐条回应：对每个判定，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 1 Round 13 修改验证报告\n\n### Issue-by-Issue Verdict\n\n**R12-N1 [critical] 因果 overclaiming → [RESOLVED]**\nTitle \"Routes\"→\"Reorganizes\"。全文 grep 零残留 \"routing\"。所有关键位置使用 \"redistributes\"。三级证据分类在 \"redistributes\" 框架下更恰当。\n\n**R4-N1 [critical] Finding 3 是架构必然结果 → [RESOLVED]**\nAbstract: \"confirms expected\" + \"consistent with the causal attention mask\" + \"framework sanity check\" 三重降格。Contribution (iii) 定位为 \"methodology validation\"。Title \"Vision Encodes\" 作为修辞性 shorthand 可接受。\n\n**R9-N1 [wont_fix] 跨架构泛化不足 → [RESOLVED]**\n所有 7+ 处 cross-architecture claim 均加上 \"causal-decoder\" 限定。Limitations 明确指出 flow-matching/diffusion 架构不适用。Discussion 推测性预测已移除。\n\n**R9-N2 [wont_fix] 无 closed-loop 机器人评估 → [PARTIALLY_RESOLVED]**\n诚实承认 open-loop，引用同期工作建立 precedent，给出两个具体 actionable implications。但 \"orthogonal contribution\" 措辞过于 dismissive——closed-loop validation 不是 orthogonal 的，而是验证本文 claims 实用价值的必要步骤。建议改为 \"a complementary and necessary next step\"。两个 actionable implications 仍未经实验验证。\n\n**R9-W1 [critical→open] CoRL scope fit → [PARTIALLY_RESOLVED]**\n改善：两个具体 robotics-relevant implications、诚实 limitations、更好的 related work 定位。仍存在：implications 未经验证、\"independent design value\" 论证力度可能不足、无 LIBERO rollout/real-robot/sim-to-real。判断：scope framing 改善但核心缺陷（纯 open-loop）无法仅通过 writing 解决。与同期工作（Grant, Häon）标准一致。\n\n**R9-W4 [warning] Cohen's d 独立性 → [RESOLVED]**\n现同时报告 token-level 和 trajectory-level d（2.943）。\n\n**R12-W6 [warning] FDR 校正细节 → [RESOLVED]**\n明确指定 BH 方法、α=0.05、33-layer family per metric。\n\n**R12-DIV1 [warning] Title \"Language Routes\" 误导 → [RESOLVED]**\n\n### New Issues\n- NEW-1 [info]: \"Language Reorganizes\" 中 Language 仍作为 agent，修辞性 convention，不影响接收\n- NEW-2 [warning]: \"orthogonal contribution\" framing 过于 dismissive，建议 camera-ready 修改\n- NEW-3 [info]: 附录 \"robust attractor\" 措辞较主文更强（N=2 架构偏强），仅在附录\n- NEW-4 [info]: 页面压缩激进但在限制内\n\n### Overall: 3.5/5（Borderline Accept，从 3.0 上调 0.5）\n上调理由：因果语言全面修正、Finding 3 降格处理、跨架构诚实限定、技术修复完成、teaser figure + missing references。\n未达 4.0 原因：纯 open-loop 对 CoRL 仍是核心局限、actionable implications 未验证、\"orthogonal\" framing dismissive。\n\n---\n\n请逐条回应。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "13",
    "text": "以下是 Reviewer 1 的完整 Round 13 验证报告，请逐条回应：对每个判定，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 1 Round 13 修改验证报告\n\n### Issue-by-Issue Verdict\n\n**R12-N1 [critical] 因果 overclaiming → [RESOLVED]**\nTitle \"Routes\"→\"Reorganizes\"。全文 grep 零残留 \"routing\"。所有关键位置使用 \"redistributes\"。三级证据分类在 \"redistributes\" 框架下更恰当。\n\n**R4-N1 [critical] Finding 3 是架构必然结果 → [RESOLVED]**\nAbstract: \"confirms expected\" + \"consistent with the causal attention mask\" + \"framework sanity check\" 三重降格。Contribution (iii) 定位为 \"methodology validation\"。Title \"Vision Encodes\" 作为修辞性 shorthand 可接受。\n\n**R9-N1 [wont_fix] 跨架构泛化不足 → [RESOLVED]**\n所有 7+ 处 cross-architecture claim 均加上 \"causal-decoder\" 限定。Limitations 明确指出 flow-matching/diffusion 架构不适用。Discussion 推测性预测已移除。\n\n**R9-N2 [wont_fix] 无 closed-loop 机器人评估 → [PARTIALLY_RESOLVED]**\n诚实承认 open-loop，引用同期工作建立 precedent，给出两个具体 actionable implications。但 \"orthogonal contribution\" 措辞过于 dismissive——closed-loop validation 不是 orthogonal 的，而是验证本文 claims 实用价值的必要步骤。建议改为 \"a complementary and necessary next step\"。两个 actionable implications 仍未经实验验证。\n\n**R9-W1 [critical→open] CoRL scope fit → [PARTIALLY_RESOLVED]**\n改善：两个具体 robotics-relevant implications、诚实 limitations、更好的 related work 定位。仍存在：implications 未经验证、\"independent design value\" 论证力度可能不足、无 LIBERO rollout/real-robot/sim-to-real。判断：scope framing 改善但核心缺陷（纯 open-loop）无法仅通过 writing 解决。与同期工作（Grant, Häon）标准一致。\n\n**R9-W4 [warning] Cohen's d 独立性 → [RESOLVED]**\n现同时报告 token-level 和 trajectory-level d（2.943）。\n\n**R12-W6 [warning] FDR 校正细节 → [RESOLVED]**\n明确指定 BH 方法、α=0.05、33-layer family per metric。\n\n**R12-DIV1 [warning] Title \"Language Routes\" 误导 → [RESOLVED]**\n\n### New Issues\n- NEW-1 [info]: \"Language Reorganizes\" 中 Language 仍作为 agent，修辞性 convention，不影响接收\n- NEW-2 [warning]: \"orthogonal contribution\" framing 过于 dismissive，建议 camera-ready 修改\n- NEW-3 [info]: 附录 \"robust attractor\" 措辞较主文更强（N=2 架构偏强），仅在附录\n- NEW-4 [info]: 页面压缩激进但在限制内\n\n### Overall: 3.5/5（Borderline Accept，从 3.0 上调 0.5）\n上调理由：因果语言全面修正、Finding 3 降格处理、跨架构诚实限定、技术修复完成、teaser figure + missing references。\n未达 4.0 原因：纯 open-loop 对 CoRL 仍是核心局限、actionable implications 未验证、\"orthogonal\" framing dismissive。\n\n---\n\n请逐条回应。"
  }
}
```

</details>

---


### Tool result

_source line 966 · 2026-05-20T16:14:40.031742+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1460
}
```

</details>

---


### Assistant

_source line 967 · 2026-05-20T16:14:43.368702+00:00_

交叉分享已发送。等待两位 Reviewer 的逐条回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director"
}
```

</details>

---


## Round 96

## Round 96

2 recorded events


### User

_source line 968 · 2026-05-20T16:14:45.957680+00:00_

[Reviewer 2 审稿结果]:
Round 2 验证报告已提交。

**总结**：7 个待验证 issue 中，5 个 **[RESOLVED]**，2 个 **[PARTIALLY_RESOLVED]**（arXiv 引用还剩 2 条可更新；术语一致性和 Limitations 格式为 minor 残留）。所有 critical issues 已解决。未发现新的实质性问题。Clarity 评分建议从 7/10 上调至 8/10。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 969 · 2026-05-20T16:14:51.156044+00:00_

收到 Reviewer 2 的总结确认。等待两位 Reviewer 的交叉回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director"
}
```

</details>

---


## Round 97

## Round 97

2 recorded events


### User

_source line 970 · 2026-05-20T16:15:36.466456+00:00_

[Reviewer 1 审稿意见]:

# Reviewer 1 交叉回应：逐条回应 Reviewer 2 Round 2 验证报告

---

## Critical Issues

### R12-N2 [critical] 正文超出 CoRL 8 页限制 → [RESOLVED]

**[AGREE]。**

我独立验证了页面布局：Section 5 Discussion（含 Limitations 和 Conclusion paragraph）在 page 8 底部结束，References 从 page 9 顶部开始。主文严格 ≤8 页。

关于 spacing hacks——R2 指出 \textfloatsep=6pt, \abovecaptionskip=2pt 等压缩幅度较大。我在 NEW-4 (info) 中也标注了同一观察。这些值确实激进（CoRL 模板默认值约 8-10pt），但 (a) 没有违反模板 \usepackage{corl_2026} 的硬约束（模板未锁定这些参数），(b) 视觉可读性未受明显损害。判定合规但 borderline，与 R2 一致。

---

### R12-N3 [critical] Abstract/Introduction 信息过载 → [RESOLVED]

**[AGREE]。**

修改后 Abstract 仅保留 ~2 个定量值（R² +0.069, Δ = 0.003），其余全部用 qualitative 描述替代（"seven complementary analyses including dose-response and counterfactual ablation"）。Introduction 不再复制 Abstract 的数字。三个 findings 的核心信息完整保留，可读性显著提升。

---

## Warning Issues

### R12-W1 [warning] 无首页 teaser figure → [RESOLVED]

**[AGREE]。**

Figure 1 位于 page 1 顶部（main.tex lines 36-44），包含 (a) 架构 schematic + token 类型标注，(b) 32-layer instruction-dominant head count 对比（untrained/Llama-2/VLA-trained）。Caption 自包含，清晰传达核心发现。这是本轮修改中对可读性改善最大的单项变更。

---

### R12-W2 [warning] 层编号 off-by-one → [RESOLVED]

**[AGREE]，包括 R2 指出的 L32 轻微歧义。**

method.tex line 26 现为："L1--L32 the hidden states after each of the 32 transformer layers, with L32 including the final layer norm。"

Off-by-one 已修复（L1-L32 = 32 层）。R2 指出的 L32 歧义（transformer 第 32 层的 output vs 该 output 经过 final LN 后的结果）确实存在——"with L32 including the final layer norm" 可理解为 L32 = transformer_output + LN，这在技术上是准确的（LLaMA-2 的 final LN 在最后一个 transformer 层之后），但措辞可以更明确。影响极小，[info] 级别。

---

### R12-W3 [warning] arXiv 引用 → [PARTIALLY_RESOLVED]

**[AGREE]。**

R2 指出 3/3 被要求的已更新，仍有 2 条可更新：belrose2023（Tuned Lens，NeurIPS 2023）和 padalkar2023（Open X-Embodiment，ICRA 2024）。这是合理的 minor fix。我在 Round 1 引用验证中也发现了类似问题（kim2024_openvla → CoRL 2024, karamcheti2024 → ICML 2024），R2 确认这些已更新。剩余 2 条属于 camera-ready 级别修改。

---

### R12-W4 [warning] 缺失 6 篇 related work → [RESOLVED]

**[AGREE]。**

我独立确认 Related Work (related_work.tex) 现包含：wang2025seeing (line 5 引用于 Introduction), pei2025rethinking (同), xiao2025ava (line 4), fan2026visual (line 24), neo2025interpreting (line 24), long2026understanding (line 24), wei2024phase (line 24)。其中 fan2026visual、neo2025interpreting、long2026understanding、wei2024phase 被恰当地整合到 Section 2 的 "Token-level functional specialization in transformers" 段落中，扩展了 VLM token analysis 的相关文献覆盖。

---

### R12-W5 [warning] 与 Grant/Häon 区分不够清晰 → [RESOLVED]

**[AGREE]。**

related_work.tex lines 18-20 现在有显式对比段落：
> "Grant et al. performed a feature-level mechanistic study and found visual dominance; Häon et al. identified sparse semantic directions linked to action selection, addressing *what* information VLAs encode. Our analysis is complementary: we address *where* instruction information is redistributed across layers and token positions..."

What (Grant/Häon) vs Where (本文) 的区分清晰且准确。这解决了 R2-W3（Round 1）和 R12-W5 的 concern。

---

## Info Issues

### R12-I1 [info] 术语一致性 → [PARTIALLY_RESOLVED]

**[AGREE]。**

主文叙事中 "readout token" 使用统一（我在 Round 1 交叉回应中曾 AGREE R3-W5 关于此问题）。R2 指出 Table 1 中 "last_preaction" 是代码技术标签——这是合理的观察。在 caption 中加一句 "(last_preaction = readout token)" 即可，属于 camera-ready 级别。

---

### R12-I2 [info] Limitations 独立 section → [PARTIALLY_RESOLVED]

**[AGREE]。**

discussion.tex line 9 使用 \paragraph{Limitations and scope.} 而非 \subsection。CoRL 要求 "必须包含 Limitations section"，\paragraph 在技术上是 section-level 以下的排版单位。但从审稿角度看，(a) Limitations 内容实质存在且有意义，(b) 加粗段落标题在视觉上可识别，(c) 这是 formatting 而非 content 问题。低优先级，与 R2 判定一致。

---

## New Issues

### R2-NEW-1 [info] Title 变更一致性

**[AGREE]，不构成问题。** Title "Vision Encodes, Language Reorganizes" 在全文中得到一致的 "redistributes" 表述支持。我在 NEW-1 (info) 中也标注了 "Language 作为 grammatical agent" 的修辞问题，但同意这是 convention 而非 factual error。

### R2-NEW-2 [positive] Finding 3 措辞改善

**[AGREE]。** "confirms expected functional specialization" + "consistent with the causal attention mask" + "framework sanity check" 是恰当的三重降格。R2 的 positive 评价与我的 R4-N1 [RESOLVED] 判定一致。

### R2-NEW-3 [info] Spacing 压缩边界效应

**[AGREE]。** 与我的 NEW-4 (info) 一致。在合规范围内但处于边界。

### R2-NEW-4 [info] 无 AI 写作痕迹

**[AGREE]。** 论文写作风格自然，术语使用专业，无明显 LLM 生成文本特征。

---

## R1 与 R2 Round 2 判定对照

| Issue | R1 判定 | R2 判定 | 一致性 |
|-------|--------|--------|--------|
| R12-N1 因果 overclaiming | RESOLVED | —（R2 未专项验证） | — |
| R12-N2 页限 | RESOLVED | RESOLVED | ✓ |
| R12-N3 信息过载 | RESOLVED | RESOLVED | ✓ |
| R4-N1 Finding 3 overclaiming | RESOLVED | RESOLVED (NEW-2 positive) | ✓ |
| R9-N1 跨架构 | RESOLVED | —（R2 未专项验证） | — |
| R9-N2 closed-loop | PARTIALLY_RESOLVED | —（R2 未专项验证） | — |
| R12-W1 teaser figure | RESOLVED | RESOLVED | ✓ |
| R12-W2 层编号 | RESOLVED | RESOLVED | ✓ |
| R12-W3 arXiv 引用 | —（我未专项复查） | PARTIALLY_RESOLVED | AGREE |
| R12-W4 missing refs | —（我在 Round 1 确认过） | RESOLVED | ✓ |
| R12-W5 Grant/Häon 区分 | RESOLVED（交叉回应） | RESOLVED | ✓ |
| R12-I1 术语一致性 | RESOLVED（交叉回应） | PARTIALLY_RESOLVED | AGREE |
| R12-I2 Limitations section | PARTIALLY_RESOLVED | PARTIALLY_RESOLVED | ✓ |
| CoRL scope fit | PARTIALLY_RESOLVED | —（R2 未专项验证） | — |

**共识**：R1 和 R2 在所有重叠项上判定一致。分歧仅在覆盖范围（R1 侧重方法论/因果 issues，R2 侧重呈现/格式 issues）。

**整体判断**：R2 的验证报告全面且准确，所有判定有充分的文本证据支持。4 项 remaining concerns 均为 minor/camera-ready 级别，不影响接收决定。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 971 · 2026-05-20T16:15:44.380262+00:00_

Reviewer 1 交叉回应已收到——全部 [AGREE]，与 Reviewer 2 在所有重叠项上判定一致。等待 Reviewer 2 对 Reviewer 1 报告的交叉回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director"
}
```

</details>

---


## Round 98

## Round 98

18 recorded events


### User

_source line 972 · 2026-05-20T16:15:46.971589+00:00_

[Reviewer 1 审稿结果]:
已提交交叉回应。R1 与 R2 在所有重叠验证项上判定完全一致，无分歧。剩余 4 项 remaining concerns（2 条 arXiv 引用更新、L32 定义歧义、Table caption 术语映射、spacing 边界）均为 camera-ready 级别 minor fixes。

---

[Reviewer 2 审稿意见]:
## Reviewer 2 交叉回应：逐条回应 Reviewer 1 Round 13 验证报告

---

### Issue-by-Issue Verdicts

**[AGREE] R12-N1 [critical] 因果 overclaiming → [RESOLVED]**

同意。Title "Routes"→"Reorganizes" 是对我 Round 1 W1 和 R1 原始 N2 的有效回应。"Reorganizes" 准确描述了 fine-tuning 的观测效果（attention pattern 的重新分布），避免了 "Routes" 隐含的主动因果机制声明。"redistributes" 作为全文的核心动词选择也恰当——它描述的是分布变化，不是因果机制。

**[AGREE] R4-N1 [critical] Finding 3 是架构必然结果 → [RESOLVED]**

同意。这是对我 Round 1 N1（本轮最核心的关切）的直接回应。三重降格处理（"confirms expected" + "consistent with the causal attention mask" + "framework sanity check"）精确地将 Finding 3 从 "novel discovery" 重新定位为 "methodology validation"。这在我 Round 2 验证中已确认为 **重大改善**（标注为 NEW-2 [positive]）。"Vision Encodes" 作为标题中的修辞性 shorthand 可接受——它描述的是 vision encoder 的功能角色，不构成 overclaim。

**[AGREE] R9-N1 [wont_fix] 跨架构泛化不足 → [RESOLVED]**

同意。所有 cross-architecture claims 添加 "causal-decoder" 限定词直接回应了我 Round 1 N3 和 R1 原始 N3 的核心关切。Limitations 中明确指出 flow-matching/diffusion 架构不适用表明作者理解泛化边界。推测性预测的移除也是正确的做法——在仅有 2 个同质架构数据的情况下，任何超出观测范围的预测都不合理。

**[AGREE] R9-N2 [wont_fix] 无 closed-loop 机器人评估 → [PARTIALLY_RESOLVED]**

同意 R1 的 PARTIALLY_RESOLVED 判定及其具体理由。补充：

1. **"orthogonal contribution" 措辞问题**：R1 指出 closed-loop validation 不是 orthogonal 而是 complementary and necessary。我完全同意。"Orthogonal" 暗示本文的分析贡献与行为验证是独立的、互不相关的维度。但事实上，本文的核心 claims（instruction routing redistribution 影响 action generation）的 practical significance 恰恰取决于这些 representational patterns 是否在 closed-loop 行为中起因果作用。建议改为 "a complementary and natural next step" 或 R1 建议的 "a complementary and necessary next step"。

2. **两个 actionable implications 的验证缺失**：论文提出 (a) L1 routing probes 可标记 instruction-discriminative tasks，(b) L1 attention entropy 可监控 instruction under-attendance。这两个 implications 的价值完全取决于实证验证——probe accuracy 与 task success rate 是否相关？attention entropy 阈值对 failure prediction 的 precision/recall 如何？未经验证的 implications 在 CoRL 语境下只是 speculation。

**[AGREE] R9-W1 [critical→open] CoRL scope fit → [PARTIALLY_RESOLVED]**

同意 R1 的判定和分析。Writing-level 改善（具体 implications、诚实 limitations、better positioning）已做到最好，但核心缺陷——纯 open-loop representational analysis 无任何 behavioral validation——无法通过写作修复。

对于 R1 提到的 "与同期工作（Grant, Häon）标准一致" 这一论点，我补充一个重要区分：Häon et al. [6] 不仅做了 mechanistic analysis，还展示了基于发现的 **zero-shot behavioral steering**（在 LIBERO simulation 和 UR5 真实机器人上验证），即他们的分析直接导致了 actionable intervention 并在 closed-loop 中验证了效果。Grant et al. [5] 虽然也是分析性工作，但其 feature-level contrastive identification 直接生成了 Action Atlas 工具。相比之下，本文的两个 actionable implications 均未经验证。因此，"与同期工作标准一致" 的论证在严格比较下可能不完全成立。

不过，本文的 factorial controls 方法论框架和 per-layer decomposition 确实提供了独立的方法论价值，这在 Grant/Häon 中均未见。scope fit 的最终判断取决于 CoRL AC 对纯分析性工作的接受阈值。

**[AGREE] R9-W4 [warning] Cohen's d 独立性 → [RESOLVED]**

同意。同时报告 token-level 和 trajectory-level d（2.943）解决了独立性假设的担忧。Trajectory-level aggregation 的 effect size 仍然很大（d=2.943），说明主要发现在适当的统计单元下仍然 robust。

**[AGREE] R12-W6 [warning] FDR 校正细节 → [RESOLVED]**

同意。BH 方法 + α=0.05 + 33-layer family per metric 的规范化报告完整回应了 R1 和我在 Round 1 交叉回应中的关切。

**[AGREE] R12-DIV1 [warning] Title "Language Routes" 误导 → [RESOLVED]**

同意，与 R12-N1 一致。

---

### New Issues 回应

**[AGREE] NEW-1 [info]: "Language Reorganizes" 中 Language 作为 agent**

同意这是修辞性 convention。在 NLP/ML 论文中，以模态名称作为句子主语是常见做法（如 "Attention Is All You Need" 中 attention 并非字面意义上的 agent）。不影响技术解读。

**[AGREE] NEW-2 [warning]: "orthogonal contribution" framing 过于 dismissive**

强烈同意，如上述 R9-N2 回应中详述。"Orthogonal" 不仅是 framing 问题，还暗示了对 closed-loop validation 重要性的低估。建议在 camera-ready 中修改为 "a complementary and necessary next step"。

**[AGREE] NEW-3 [info]: 附录 "robust attractor" 措辞**

同意。"Robust attractor" 暗示动力系统层面的收敛保证，但仅基于 N=2 架构的观察。作为附录中的描述性语言尚可接受，但如果 reviewer 严格审查可能被标记。建议改为 "consistent convergence pattern" 或类似描述性措辞。

**[AGREE] NEW-4 [info]: 页面压缩激进但在限制内**

同意，与我 Round 2 报告一致（我将 `\textfloatsep`=6pt 标注为 "合规但处于边界"）。

---

### Overall Assessment 回应

**同意 R1 的 3.5/5 评分和上调理由。**

R1 的评分变化轨迹（3.0 → 3.5）反映了修改的实际改善幅度：

**上调合理性**：
- 因果语言全面修正（Routes→Reorganizes, routing→redistributes）消除了最突出的 overclaiming
- Finding 3 降格为 sanity check 修正了 novelty framing
- Cross-architecture claims 的诚实限定提升了论文的 intellectual integrity
- Teaser figure + missing references 改善了可读性和学术完整性

**未达 4.0 合理性**：
- 纯 open-loop + 无 behavioral validation 是结构性缺陷，writing 无法补偿
- Actionable implications 未验证意味着 "why it matters for robotics" 的论证链不完整
- CoRL 的 robotics relevance 要求是 hard constraint，不是 soft preference

**我的对应评分调整**：从 Round 1 的 4/10 (Borderline Reject) 上调至 **5/10 (Borderline)**。上调 1 分反映：(1) Finding 3 的 novelty overclaim 已修正（我的 N1 解决）；(2) 呈现性改善显著（Clarity 从 7→8）；(3) Related work 完整性提升。未达 6/10 因为 CoRL scope fit（我的 N2）和跨架构泛化（我的 N3，现已限定但未增加新数据）的核心问题仍然存在。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 973 · 2026-05-20T16:16:05.504857+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__read_local_file,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__submit_review_report_to_research_director",
  "max_results": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__read_local_file,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__submit_review_report_to_research_director",
    "max_results": "5"
  }
}
```

</details>

---


### Tool result

_source line 974 · 2026-05-20T16:16:05.555492+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 975 · 2026-05-20T16:16:08.440532+00:00_

called mcp__agent-ml-research__get_visual_check_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_visual_check_status</summary>

```json
{
  "project": "vla-ssd"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "tool_args": {
    "project": "vla-ssd"
  }
}
```

</details>

---


### Tool result

_source line 976 · 2026-05-20T16:16:08.892681+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"done\", \"started_at\": \"2026-05-20T16:07:03.821050+00:00\", \"completed_at\": \"2026-05-20T16:10:23.886751+00:00\", \"findings\": [{\"severity\": \"warning\", \"dimension\": \"page 2-4\", \"message\": \"连续 3 页纯文本，无任何 display item。Related Work 和 Method 开头形成文字墙，审稿人在此段可能失去耐心。建议在 Section 3 (Model and Data) 中加入 pipeline 示意图或方法概览表，拆解文字密度\"}, {\"severity\": \"warning\", \"dimension\": \"page 6\", \"message\": \"结果段纯文本页——cross-architecture generalization、dose-response gradient、counterfactual analysis 等 5 组实验结果全用行内数字描述，无任何图表支撑。审稿人需要在密集数字中自行构建 mental model。建议将 dose-response 或 counterfactual 结果可视化为一个 figure\"}, {\"severity\": \"warning\", \"dimension\": \"page 31\", \"message\": \"末页仅 ~7 行文字，~90% 空白。附录最后一页严重浪费空间。建议合并至前页或补充内容\"}, {\"severity\": \"info\", \"dimension\": \"page 1\", \"message\": \"Figure 1 子面板中部分标签文字偏小（尤其是 (a) 架构图中的模块名称和 (c)(d) 的 y 轴刻度标签），打印后可能处于可读性边界。建议确保最小字号 ≥ 8pt\"}, {\"severity\": \"info\", \"dimension\": \"page 5\", \"message\": \"Table 1 格式良好：booktabs 风格、最优值加粗、精度一致。但 caption 较长（5 行），可考虑精简\"}, {\"severity\": \"info\", \"dimension\": \"page 7\", \"message\": \"Figure 2 (a)(b) 柱状图颜色方案可区分，但 5 种条件的颜色区分度在灰度打印下可能不足，建议增加 hatching pattern 辅助\"}, {\"severity\": \"info\", \"dimension\": \"page 8\", \"message\": \"Figure 3 线图使用蓝/橙/绿三色，色盲友好。legend 清晰，caption 自包含\"}, {\"severity\": \"info\", \"dimension\": \"page 7\", \"message\": \"Table 2 使用 booktabs 风格，格式规范。best/underline 标注清晰\"}, {\"severity\": \"info\", \"dimension\": \"page 8\", \"message\": \"Table 3 标注了 bold（best）和 underline（second），符合惯例。footnote 说明了 peak 的含义\"}, {\"severity\": \"info\", \"dimension\": \"page 13-20\", \"message\": \"附录 display items 密度高（Figure 4-14, Table 4-7+），与正文形成反差——部分可视化（如 Figure 9 dose-response gradient、Figure 10 pretrained LLM diagnostics）信息价值高，考虑提升至正文以改善 pp.2-6 的视觉节奏\"}, {\"severity\": \"info\", \"dimension\": \"page 25\", \"message\": \"Figure 16-17 stacked bar chart 颜色方案（instruction/image/action/BOS）区分度良好\"}, {\"severity\": \"inf
…[truncated 203 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 977 · 2026-05-20T16:16:08.893782+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "vla-ssd"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "vla-ssd"
  }
}
```

</details>

---


### Tool result

_source line 978 · 2026-05-20T16:16:09.044623+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 150
}
```

</details>

---


### Tool call

_source line 979 · 2026-05-20T16:16:09.095237+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
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

_source line 980 · 2026-05-20T16:16:09.195971+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "ToolSearch",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 981 · 2026-05-20T16:16:14.568249+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/review_issues.yaml"
  }
}
```

</details>

---


### Tool result

_source line 982 · 2026-05-20T16:16:14.619512+00:00_

1	issues:
2	  # ============================================================
3	  # Round 1-8 历史 issues（全部 resolved，压缩保留）
4	  # ============================================================
5	  - id: R1-N1-old
6	    summary: "Untrained baseline 无法隔离 VLA fine-tuning vs Llama-2 语言预训练的贡献"
7	    category: experiment
8	    severity: critical
9	    status: resolved
10	    first_raised_round: 1
11	    last_seen_round: 2
12	    resolution: "三条件数据完整整合。"
13	    resolution_round: 3
14	    mentions: []
15	    action_items: []
16	  - id: R1-N2-old
17	    summary: "单一模型 Title/Abstract 使用复数 'VLAs' 构成 overclaim"
18	    category: framing
19	    severity: critical
20	    status: resolved
21	    first_raised_round: 1
22	    last_seen_round: 2
23	    resolution: "Title 改为单数。"
24	    resolution_round: 3
25	    mentions: []
26	    action_items: []
27	  - id: R1-N4-old
28	    summary: "Design implications 完全基于 correlational evidence"
29	    category: framing
30	    severity: critical
31	    status: resolved
32	    first_raised_round: 1
33	    last_seen_round: 2
34	    resolution: "Abstract 使用 hedge 语气。"
35	    resolution_round: 3
36	    mentions: []
37	    action_items: []
38	  - id: R1-N3-old
39	    summary: "RSA best-vs-best selection bias"
40	    category: experiment
41	    severity: warning
42	    status: resolved
43	    first_raised_round: 1
44	    last_seen_round: 2
45	    resolution: "Same-layer comparison 为 primary evidence。"
46	    resolution_round: 3
47	    mentions: []
48	    action_items: []
49	  - id: R2-N1-old
50	    summary: "Neo et al. (ICLR 2025) 未引用"
51	    category: framing
52	    severity: warning
53	    status: resolved
54	    first_raised_round: 1
55	    last_seen_round: 2
56	    resolution: "已引用。"
57	    resolution_round: 3
58	    mentions: []
59	    action_items: []
60	  - id: R2-W1-old
61	    summary: "Related Work 引用覆盖度不足"
62	    category: writing
63	    severity: warning
64	    status: resolved
65	    first_raised_round: 1
66	    last_seen_round: 2
67	    resoluti
…[truncated 21365 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 983 · 2026-05-20T16:19:31.731537+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "vla-ssd",
  "issues_yaml": "issues:\n  # ============================================================\n  # Round 1-8 历史 issues（全部 resolved，压缩保留）\n  # ============================================================\n  - id: R1-N1-old\n    summary: \"Untrained baseline 无法隔离 VLA fine-tuning vs Llama-2 语言预训练的贡献\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    resolution: \"三条件数据完整整合。\"\n    resolution_round: 3\n    mentions: []\n    action_items: []\n  - id: R1-N2-old\n    summary: \"单一模型 Title/Abstract 使用复数 'VLAs' 构成 overclaim\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    resolution: \"Title 改为单数。\"\n    resolution_round: 3\n    mentions: []\n    action_items: []\n  - id: R1-N4-old\n    summary: \"Design implications 完全基于 correlational evidence\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    resolution: \"Abstract 使用 hedge 语气。\"\n    resolution_round: 3\n    mentions: []\n    action_items: []\n  - id: R1-N3-old\n    summary: \"RSA best-vs-best selection bias\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    resolution: \"Same-layer comparison 为 primary evidence。\"\n    resolution_round: 3\n    mentions: []\n    action_items: []\n  - id: R2-N1-old\n    summary: \"Neo et al. (ICLR 2025) 未引用\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    resolution: \"已引用。\"\n    resolution_round: 3\n    mentions: []\n    action_items: []\n  - id: R2-W1-old\n    summary: \"Related Work 引用覆盖度不足\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    resolution: \"引用数量达标。\"\n    resolution_round: 3\n    mentions: []\n    action_items: []\n  - id: R1-W1-old\n    summary: \"'Instruction-blind' claim 过强\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    resolution: \"MLP probe 双重验证。\"\n    resolution_round: 3\n    mentions: []\n    action_items: []\n  - id: R1-W2-old\n    summary: \"CKA 反转 RSA 排序处理不充分\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    resolution: \"Method 新增 'Why RSA over CKA'。\"\n    resolution_round: 2\n    mentions: []\n    action_items: []\n  - id: R3-N1-old\n    summary: \"Limitations 格式\"\n    category: format\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    resolution: \"改为 subsection。\"\n    resolution_round: 3\n    mentions: []\n    action_items: []\n  - id: R3-N2-old\n    summary: \"em-dash AI 写作标志\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    resolution: \"零残留。\"\n    resolution_round: 2\n    mentions: []\n    action_items: []\n  - id: R3-W5-old\n    summary: \"无 code/data 释放声明\"\n    category: format\n    severity: info\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    resolution: \"Conclusion 加声明。\"\n    resolution_round: 3\n    mentions: []\n    action_items: []\n\n  # ============================================================\n  # Round 4-8 issues（全部 resolved）\n  # ============================================================\n  - id: R4-N1\n    summary: \"C1 是 causal mask 必然结果 + probe trivially easy\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 13\n    resolution: \"Abstract 'confirms expected' + 'consistent with causal attention mask' + 'framework sanity check' 三重降格。Contribution (iii) 定位为 methodology validation。全文一致。\"\n    resolution_round: 13\n    mentions:\n      - round: 9\n        reviewers: [1, 2]\n        note: \"R9-W2: C1 在 Abstract/Introduction 占比失衡。\"\n      - round: 10\n        reviewers: [1, 2]\n        note: \"RESOLVED。降格处理到位。\"\n      - round: 12\n        reviewers: [2, 3]\n        note: \"复发。R2-N1: 虽已降为 sanity check，但 Title 'Vision Encodes, Language Routes' 和 Abstract 'strict functional specialization' 仍将架构约束呈现为核心贡献。R3 agree with nuance。\"\n      - round: 13\n        reviewers: [1, 2]\n        note: \"RESOLVED。三重降格处理精准，Title 'Vision Encodes' 作为修辞性 shorthand 可接受。R1+R2 共识。\"\n    action_items:\n      - round: 12\n        action: \"Title 不再暗示 token specialization 是实证发现；Abstract 'strict' 改为 'expected'\"\n        assigned_to: research_director\n        status: done\n  - id: R4-N2\n    summary: \"RSA inverted-U metric-dependent，CKA 反转\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 8\n    resolution: \"C3 降为 qualified observation + §4.4 CKA 正文讨论。\"\n    resolution_round: 8\n    mentions: []\n    action_items: []\n  - id: R4-N3\n    summary: \"L1 ablation 使用 5 demos\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 5\n    resolution: \"改用 50 demos (N=63,228)。\"\n    resolution_round: 5\n    mentions: []\n    action_items: []\n  - id: R4-W1\n    summary: \"RSA best-vs-best n.s. 未标注\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 5\n    resolution: \"已标注。\"\n    resolution_round: 5\n    mentions: []\n    action_items: []\n  - id: R4-W2\n    summary: \"缺乏多重比较校正\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 5\n    resolution: \"FDR 已应用。\"\n    resolution_round: 5\n    mentions: []\n    action_items: []\n  - id: R4-W3\n    summary: \"Probe N 未报告，MLP capacity 控制不充分\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 7\n    resolution: \"Demo-level split 完全消除时间泄漏。\"\n    resolution_round: 7\n    mentions: []\n    action_items: []\n  - id: R4-W4\n    summary: \"Frozen encoder confound\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 5\n    resolution: \"Introduction + Discussion 说明。\"\n    resolution_round: 5\n    mentions: []\n    action_items: []\n\n  # ============================================================\n  # Round 9-11 issues\n  # ============================================================\n  - id: R9-N1\n    summary: \"单一模型(OpenVLA-7B)单一基准(LIBERO)，无法支撑 VLA 通用性\"\n    category: experiment\n    severity: critical\n    status: wont_fix\n    first_raised_round: 9\n    last_seen_round: 13\n    mentions:\n      - round: 9\n        reviewers: [1, 2]\n        note: \"双方 AGREE critical。\"\n      - round: 10\n        reviewers: [1, 2]\n        note: \"STILL_OPEN。Residual scope limitation。\"\n      - round: 11\n        reviewers: [1]\n        note: \"维持 wont_fix。Rebuttal 准备就绪。\"\n      - round: 12\n        reviewers: [1, 2, 3]\n        note: \"R12 fresh review 再次提出。R1-N3 + R2-N3: 2 个同质架构不足以支撑 cross-architecture claim。三位 Reviewer 全部 AGREE。\"\n      - round: 13\n        reviewers: [1, 2]\n        note: \"Claims 已恰当弱化：所有位置加 'causal-decoder' 限定（7+ 处），Limitations 明确指出 flow-matching/diffusion 不适用。R1 判 RESOLVED（claim 层面），R2 AGREE。维持 wont_fix 因实验数据未增加。\"\n    action_items:\n      - round: 10\n        action: \"Rebuttal 应对：causal mask 泛化 + testable predictions + Discussion 已列预测\"\n        assigned_to: research_director\n        status: pending\n    resolution: \"Claims 已限定为 'causal-decoder VLAs'。实验数据仍为 2 个同质架构，结构性局限不变。Rebuttal 应对。\"\n    resolution_round: null\n\n  - id: R9-N2\n    summary: \"所有分析均为 open-loop，无 closed-loop 机器人评估\"\n    category: experiment\n    severity: critical\n    status: wont_fix\n    first_raised_round: 9\n    last_seen_round: 13\n    mentions:\n      - round: 9\n        reviewers: [1, 2]\n        note: \"双方 AGREE critical。\"\n      - round: 10\n        reviewers: [1, 2]\n        note: \"STILL_OPEN。D074 放弃。\"\n      - round: 11\n        reviewers: [1]\n        note: \"维持 wont_fix。Open-loop triangulation rebuttal 准备就绪。\"\n      - round: 12\n        reviewers: [1, 2, 3]\n        note: \"R12 fresh review 再次以最高优先级提出。R1-N1 + R2-N2: 纯 open-loop analysis 对 CoRL 是致命缺陷。三位 Reviewer 最强共识项。\"\n      - round: 13\n        reviewers: [1, 2]\n        note: \"PARTIALLY_RESOLVED。诚实承认 open-loop + 引用同期工作 precedent + 两个 actionable implications。但 'orthogonal contribution' 措辞 dismissive——closed-loop 不是 orthogonal 而是 complementary and necessary。R2 补充：Häon 有 zero-shot behavioral steering 验证，Grant 有 Action Atlas 工具，本文 implications 均未验证。\"\n    action_items:\n      - round: 10\n        action: \"Rebuttal 应对：open-loop 三角验证有独立价值\"\n        assigned_to: research_director\n        status: pending\n      - round: 13\n        action: \"将 'orthogonal contribution' 改为 'complementary and necessary next step'\"\n        assigned_to: research_director\n        status: pending\n    resolution: \"D074 放弃（SR=0/3）。Open-loop triangulation rebuttal 应对。R13 framing 改善但 'orthogonal' 措辞仍需修改。\"\n    resolution_round: null\n\n  - id: R9-N3\n    summary: \"'Causal' 术语在 observational open-loop 分析中使用不当\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 9\n    last_seen_round: 10\n    resolution: \"Discussion 'Causal' → 'Interventional'；§4.3 heading 改为 'Open-loop functional sensitivity'。\"\n    resolution_round: 10\n    mentions:\n      - round: 10\n        reviewers: [1, 2]\n        note: \"RESOLVED。\"\n    action_items: []\n\n  - id: R9-N4\n    summary: \"Ablation 使 R² 增加的 paradox 未充分解释\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 9\n    last_seen_round: 11\n    resolution: \"Discussion 加 information-computation dissociation 解释。MSE 证据 (ΔMSE≈0) 支撑。\"\n    resolution_round: 11\n    mentions:\n      - round: 10\n        reviewers: [1, 2]\n        note: \"PARTIALLY_RESOLVED。\"\n      - round: 11\n        reviewers: [1]\n        note: \"RESOLVED。\"\n    action_items: []\n\n  - id: R9-N5\n    summary: \"Counterfactual 的 'semantic distance' 概念未定义且不可测量\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 9\n    last_seen_round: 10\n    resolution: \"改用 Jaccard token overlap / token novelty (1 - Jaccard)。\"\n    resolution_round: 10\n    mentions:\n      - round: 10\n        reviewers: [1, 2]\n        note: \"RESOLVED。\"\n    action_items: []\n\n  - id: R9-N6\n    summary: \"N=10 tasks 的 RSA bootstrap 统计功效不足\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 9\n    last_seen_round: 12\n    resolution: \"§4.4 加 power limitation 声明。\"\n    resolution_round: 11\n    mentions:\n      - round: 11\n        reviewers: [1]\n        note: \"RESOLVED。\"\n      - round: 12\n        reviewers: [1, 2]\n        note: \"R12 重新提及为 warning (R1-W2)。声明存在但 N=10 根本局限未变。不升级 severity。\"\n    action_items: []\n\n  - id: R9-W1\n    summary: \"CoRL scope fit 有限：纯 representational analysis，无物理机器人实验\"\n    category: framing\n    severity: critical\n    status: open\n    first_raised_round: 9\n    last_seen_round: 13\n    resolution: \"\"\n    resolution_round: null\n    mentions:\n      - round: 10\n        reviewers: [1, 2]\n        note: \"PARTIALLY_RESOLVED。\"\n      - round: 11\n        reviewers: [1]\n        note: \"RESOLVED。Actionable implication + hedging 恰当。\"\n      - round: 12\n        reviewers: [1, 2, 3]\n        note: \"R12 fresh review 将此升级为 critical。R2-N2: Discussion 的 actionable implications 均为 speculative，未验证。三位 Reviewer AGREE。\"\n      - round: 13\n        reviewers: [1, 2]\n        note: \"PARTIALLY_RESOLVED。Writing-level 改善（具体 implications、诚实 limitations、better positioning）。但核心缺陷——纯 open-loop 无 behavioral validation——无法通过写作修复。R2 补充：Häon 有 closed-loop 验证，Grant 有 Action Atlas，本文 implications 均未验证，'与同期工作标准一致' 论证在严格比较下不完全成立。最终判断取决于 CoRL AC 对纯分析性工作的接受阈值。\"\n    action_items:\n      - round: 12\n        action: \"验证至少一个 actionable implication（如 L1 entropy monitor → closed-loop failure prediction），或改投 ML venue\"\n        assigned_to: research_director\n        status: pending\n\n  - id: R9-W2\n    summary: \"C1 在 Abstract/Introduction/Contributions 中占比失衡\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 9\n    last_seen_round: 10\n    resolution: \"C1 降为末句 sanity check + 末位 + (iii) framework。\"\n    resolution_round: 10\n    mentions:\n      - round: 10\n        reviewers: [1, 2]\n        note: \"RESOLVED。\"\n    action_items: []\n\n  - id: R9-W3\n    summary: \"Vision representation 训练效果微弱，framing 未充分反映\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 9\n    last_seen_round: 10\n    resolution: \"§4.4 标题改为 'Training primarily enhances readout decodability'。\"\n    resolution_round: 10\n    mentions:\n      - round: 10\n        reviewers: [1, 2]\n        note: \"RESOLVED。\"\n    action_items: []\n\n  - id: R9-W4\n    summary: \"Cohen's d 独立性假设违反\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 9\n    last_seen_round: 13\n    resolution: \"新增 trajectory-level d (2.943)，与 token-level d (0.65) 同时报告。\"\n    resolution_round: 10\n    mentions:\n      - round: 10\n        reviewers: [1, 2]\n        note: \"RESOLVED。\"\n      - round: 12\n        reviewers: [1, 2, 3]\n        note: \"R12 再次提及 (R1-W1)。Trajectory-level d 存在但主文仍以 token-level d 为主要报告。\"\n      - round: 13\n        reviewers: [1, 2]\n        note: \"RESOLVED。双级报告充分，trajectory-level d=2.943 确认主要发现 robust。\"\n    action_items: []\n\n  - id: R9-W5\n    summary: \"Pretrained Llama-2 base 的 9/32 heads 可能因 text in-distribution bias\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 9\n    last_seen_round: 10\n    resolution: \"Discussion 新增替代解释承认。\"\n    resolution_round: 10\n    mentions:\n      - round: 10\n        reviewers: [1, 2]\n        note: \"RESOLVED。\"\n    action_items: []\n\n  - id: R9-W6\n    summary: \"Specificity control 效果有限(d ratio 1.08×)\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 9\n    last_seen_round: 11\n    resolution: \"四组 matched-size 比较，framing 'distributed routing'。\"\n    resolution_round: 11\n    mentions:\n      - round: 11\n        reviewers: [1]\n        note: \"标 resolved（论文文本 well-calibrated）。\"\n    action_items: []\n\n  - id: R9-W7\n    summary: \"N=63,228 观测的独立性——有效独立单元远小于报告值\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 9\n    last_seen_round: 12\n    resolution: \"§4.1 新增 N_eff 说明。\"\n    resolution_round: 10\n    mentions:\n      - round: 10\n        reviewers: [1, 2]\n        note: \"RESOLVED。\"\n      - round: 12\n        reviewers: [1, 2]\n        note: \"R12 再次提及 (R1-W3)。N_eff 存在但 method section 未明确标注哪些分析用 token-level vs aggregated。\"\n    action_items: []\n\n  - id: R9-I1\n    summary: \"缺失引用：Octo (Ghosh et al. 2024)\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 9\n    last_seen_round: 10\n    resolution: \"references.bib 新增。\"\n    resolution_round: 10\n    mentions: []\n    action_items: []\n\n  - id: R9-I2\n    summary: \"Häon et al. 2025 的 sparse semantic directions 与 L1 routing heads 的关系未讨论\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 9\n    last_seen_round: 11\n    resolution: \"Discussion 加 where/what 互补连接。\"\n    resolution_round: 11\n    mentions: []\n    action_items: []\n\n  - id: R9-I3\n    summary: \"多处小问题：Table 1 caption、脚注、accessed date\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 9\n    last_seen_round: 10\n    resolution: \"已修复。\"\n    resolution_round: 10\n    mentions: []\n    action_items: []\n\n  - id: R10-Q1\n    summary: \"Per-task MSE breakdown：消融后 MSE 不变是否存在 task-level cancellation\"\n    category: experiment\n    severity: info\n    status: resolved\n    first_raised_round: 10\n    last_seen_round: 11\n    resolution: \"Appendix 加 per-task breakdown。\"\n    resolution_round: 11\n    mentions: []\n    action_items: []\n\n  # ============================================================\n  # Round 12 (fresh review) issues — updated with R13 verdicts\n  # ============================================================\n\n  - id: R12-N1\n    summary: \"因果 overclaiming：Title 'Routes' 暗示因果机制，但证据为 correlational + weak specificity（d ratio 仅 1.08×）\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 12\n    last_seen_round: 13\n    mentions:\n      - round: 12\n        reviewers: [1, 2, 3]\n        note: \"R1-N2 提出，R2 AGREE（与其 W2 一致），R3 AGREE with nuance。\"\n      - round: 13\n        reviewers: [1, 2]\n        note: \"RESOLVED。Title 'Routes'→'Reorganizes'。全文 grep 零残留 'routing'。所有关键位置使用 'redistributes'。三级证据分类在新框架下恰当。R1+R2 共识。\"\n    action_items:\n      - round: 12\n        action: \"将 Title 'Routes' 降级或改为更审慎表述；主文 framing 区分 interventional evidence 和 causal mechanism\"\n        assigned_to: research_director\n        status: done\n    resolution: \"Title 'Routes'→'Reorganizes'，全文 'routing'→'redistributes'，零残留。\"\n    resolution_round: 13\n\n  - id: R12-N2\n    summary: \"正文超出 CoRL 8 页限制约 0.7 页（Discussion+Conclusion 延伸到第 9 页）\"\n    category: format\n    severity: critical\n    status: resolved\n    first_raised_round: 12\n    last_seen_round: 13\n    mentions:\n      - round: 12\n        reviewers: [1, 2, 3]\n        note: \"R3-N1 提出，R1+R2 AGREE。超页限是 desk rejection 常见理由。\"\n      - round: 13\n        reviewers: [1, 2]\n        note: \"RESOLVED。Conclusion 在 page 8 底部结束，References 从 page 9 开始。Spacing hacks 激进但合规。R1+R2 共识。\"\n    action_items:\n      - round: 12\n        action: \"压缩至 8 页\"\n        assigned_to: research_director\n        status: done\n    resolution: \"正文严格控制在 8 页内。Spacing 参数激进（textfloatsep=6pt）但合规。\"\n    resolution_round: 13\n\n  - id: R12-N3\n    summary: \"Abstract/Introduction 信息过载：Abstract 塞入 15+ 定量结果，Introduction 与 Abstract 高度重复\"\n    category: writing\n    severity: critical\n    status: resolved\n    first_raised_round: 12\n    last_seen_round: 13\n    mentions:\n      - round: 12\n        reviewers: [1, 2, 3]\n        note: \"R3-N2 提出，R1+R2 AGREE。\"\n      - round: 13\n        reviewers: [1, 2]\n        note: \"RESOLVED。Abstract 定量值从 15+ 降至 ~1 个。Introduction 不再复制 Abstract 数字。关键信息完整保留。R1+R2 共识。\"\n    action_items:\n      - round: 12\n        action: \"重写 Abstract（精简至 3 个定性发现 + 最关键数字）；Introduction 去重\"\n        assigned_to: research_director\n        status: done\n    resolution: \"Abstract 精简至 ~1 个定量值 + 定性发现。Introduction 去重。\"\n    resolution_round: 13\n\n  - id: R12-W1\n    summary: \"无首页 teaser figure：Figure 1 直到第 6-7 页才出现，前 4 页纯文字墙\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 12\n    last_seen_round: 13\n    mentions:\n      - round: 12\n        reviewers: [2, 3]\n        note: \"R3-W1 提出，R2 AGREE。\"\n      - round: 13\n        reviewers: [1, 2]\n        note: \"RESOLVED。Figure 1 位于 page 1 顶部（architecture overview + attention redistribution 对比图）。Caption 自包含，尺寸合理。R1+R2 共识。\"\n    action_items:\n      - round: 12\n        action: \"在 page 1 或 2 增加 overview/teaser figure\"\n        assigned_to: research_director\n        status: done\n    resolution: \"Page 1 新增 Figure 1（architecture overview + instruction attention redistribution）。\"\n    resolution_round: 13\n\n  - id: R12-W2\n    summary: \"层编号 off-by-one：'L1--L31 the 32 transformer layers' 实为 31 个索引\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 12\n    last_seen_round: 13\n    mentions:\n      - round: 12\n        reviewers: [2, 3]\n        note: \"R3-W2 提出，R2 AGREE。\"\n      - round: 13\n        reviewers: [1, 2]\n        note: \"RESOLVED。L1-L32 = 32 层，全文一致。L32 定义轻微歧义（post-LN output），影响极小。R1+R2 共识。\"\n    action_items:\n      - round: 12\n        action: \"统一层标号定义\"\n        assigned_to: research_director\n        status: done\n    resolution: \"L1-L32 = 32 层。L32 定义轻微歧义为 camera-ready 修复项。\"\n    resolution_round: 13\n\n  - id: R12-W3\n    summary: \"多条引用使用 arXiv preprint 而非已发表版本（OpenVLA, Prismatic VLMs, Llama 2 等）\"\n    category: writing\n    severity: warning\n    status: in_progress\n    first_raised_round: 12\n    last_seen_round: 13\n    mentions:\n      - round: 12\n        reviewers: [2, 3]\n        note: \"R3-W3 提出，R2 AGREE。\"\n      - round: 13\n        reviewers: [1, 2]\n        note: \"PARTIALLY_RESOLVED。3/3 被要求的已更新（kim2024→CoRL, karamcheti2024→ICML, haon2025→CoRL）。仍有 2 条可更新：belrose2023（→NeurIPS 2023）、padalkar2023（→ICRA 2024）。Camera-ready 级别。R1+R2 共识。\"\n    action_items:\n      - round: 12\n        action: \"更新所有已发表论文的引用至正式版本\"\n        assigned_to: research_director\n        status: in_progress\n      - round: 13\n        action: \"更新 belrose2023→NeurIPS 2023, padalkar2023→ICRA 2024\"\n        assigned_to: research_director\n        status: pending\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R12-W4\n    summary: \"缺失 6 篇重要 related work（visual token encoding, causal mask analysis, VIP, AVA-VLA 等）\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 12\n    last_seen_round: 13\n    mentions:\n      - round: 12\n        reviewers: [2]\n        note: \"R2 提出 6 篇 missing references。\"\n      - round: 13\n        reviewers: [1, 2]\n        note: \"RESOLVED。6/6 全部添加并正确引用。额外添加 pei2025rethinking（causal mask）。引用总数 52→59，0 orphan + 0 missing。R1+R2 共识。\"\n    action_items:\n      - round: 12\n        action: \"验证并引用相关文献\"\n        assigned_to: research_director\n        status: done\n    resolution: \"6/6 缺失引用全部补齐 + 1 篇额外添加。引用总数 52→59。\"\n    resolution_round: 13\n\n  - id: R12-W5\n    summary: \"与 Grant et al. (2026) 和 Häon et al. (2025) 的区分不够清晰\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 12\n    last_seen_round: 13\n    mentions:\n      - round: 12\n        reviewers: [2, 3]\n        note: \"R2-W3 提出，R3 AGREE。\"\n      - round: 13\n        reviewers: [1, 2]\n        note: \"RESOLVED。Related Work 新增显式对比段落：Grant (feature-level, what) / Häon (steering-direction, what) / 本文 (token-level per-layer, where)。区分清晰准确。R1+R2 共识。\"\n    action_items:\n      - round: 12\n        action: \"Related Work 或 Discussion 加与 Grant/Häon 的对比段落\"\n        assigned_to: research_director\n        status: done\n    resolution: \"Related Work 加显式 what-vs-where 对比段落。\"\n    resolution_round: 13\n\n  - id: R12-W6\n    summary: \"FDR 多重比较校正细节不足（未说明方法类型、family scope、adjusted p-values）\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 12\n    last_seen_round: 13\n    mentions:\n      - round: 12\n        reviewers: [1, 2]\n        note: \"R1-W4 提出，R2 AGREE。\"\n      - round: 13\n        reviewers: [1, 2]\n        note: \"RESOLVED。明确指定 Benjamini-Hochberg 方法、α=0.05、33-layer family per metric。R1+R2 共识。\"\n    action_items:\n      - round: 12\n        action: \"明确报告 FDR method、correction family scope\"\n        assigned_to: research_director\n        status: done\n    resolution: \"BH 方法 + α=0.05 + 33-layer family per metric 完整报告。\"\n    resolution_round: 13\n\n  - id: R12-I1\n    summary: \"术语不一致：readout token vs last_preaction, instruction-dominant vs dominant heads\"\n    category: writing\n    severity: info\n    status: in_progress\n    first_raised_round: 12\n    last_seen_round: 13\n    mentions:\n      - round: 12\n        reviewers: [2, 3]\n        note: \"R3-W5 提出，R2 AGREE。\"\n      - round: 13\n        reviewers: [1, 2]\n        note: \"PARTIALLY_RESOLVED。叙事文本中 'readout token' 基本统一。Table 1 的 'last_preaction' 为代码技术标签，建议 caption 中加映射说明。Camera-ready 级别。R1+R2 共识。\"\n    action_items:\n      - round: 13\n        action: \"Table 1 caption 加 '(last_preaction = readout token)' 映射说明\"\n        assigned_to: research_director\n        status: pending\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R12-I2\n    summary: \"Limitations 未作为独立 section（CoRL 要求 Limitations section）\"\n    category: format\n    severity: info\n    status: in_progress\n    first_raised_round: 12\n    last_seen_round: 13\n    mentions:\n      - round: 12\n        reviewers: [2, 3]\n        note: \"R3-W4 提出，R2 部分 REBUT。\"\n      - round: 13\n        reviewers: [1, 2]\n        note: \"PARTIALLY_RESOLVED。使用 \\\\paragraph{Limitations and scope.} 而非 \\\\subsection。内容覆盖关键 limitations。技术上合规但建议改为 \\\\subsection*{Limitations}。低优先级。R1+R2 共识。\"\n    action_items:\n      - round: 13\n        action: \"考虑将 Limitations 改为 \\\\subsection*{Limitations}\"\n        assigned_to: research_director\n        status: pending\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R12-DIV1\n    summary: \"Title 'Language Routes' 是否误导——R3 REBUT（三条件 0/9/24 heads 证明非纯 positional），R2 维持\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 12\n    last_seen_round: 13\n    mentions:\n      - round: 12\n        reviewers: [2, 3]\n        note: \"DIVERGENT。R2-W1 vs R3 REBUT。\"\n      - round: 13\n        reviewers: [1, 2]\n        note: \"RESOLVED。Title 改为 'Language Reorganizes'，消除了 'Routes' 的因果误导。R1+R2 共识。\"\n    action_items: []\n    resolution: \"Title 'Routes'→'Reorganizes' 消除误导。\"\n    resolution_round: 13\n\n  # ============================================================\n  # Round 13 — NEW issues\n  # ============================================================\n\n  - id: R13-W1\n    summary: \"'Orthogonal contribution' 措辞对 closed-loop validation 过于 dismissive\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 13\n    last_seen_round: 13\n    mentions:\n      - round: 13\n        reviewers: [1, 2]\n        note: \"R1 NEW-2 提出，R2 强烈 AGREE。'Orthogonal' 暗示 closed-loop 验证与本文 claims 无关，实际上是验证 practical significance 的必要步骤。建议改为 'complementary and necessary next step'。\"\n    action_items:\n      - round: 13\n        action: \"Discussion 中 'orthogonal contribution' 改为 'complementary and necessary next step' 或类似措辞\"\n        assigned_to: research_director\n        status: pending\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R13-I1\n    summary: \"附录 'robust attractor' 措辞较主文更强（N=2 架构偏强）\"\n    category: framing\n    severity: info\n    status: open\n    first_raised_round: 13\n    last_seen_round: 13\n    mentions:\n      - round: 13\n        reviewers: [1, 2]\n        note: \"R1 NEW-3 提出，R2 AGREE。仅在附录，不影响主文 claims。建议改为 'consistent convergence pattern'。\"\n    action_items:\n      - round: 13\n        action: \"附录 'robust attractor' 考虑改为 'consistent convergence pattern'\"\n        assigned_to: research_director\n        status: pending\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R13-I2\n    summary: \"Spacing 压缩激进（textfloatsep=6pt, abovecaptionskip=2pt），合规但处于边界\"\n    category: format\n    severity: info\n    status: open\n    first_raised_round: 13\n    last_seen_round: 13\n    mentions:\n      - round: 13\n        reviewers: [1, 2]\n        note: \"R1 NEW-4 + R2 NEW-3。合规但处于 CoRL 模板边界。建议 textfloatsep 恢复至 8-10pt 如有余量。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "vla-ssd",
    "issues_yaml": "issues:\n  # ============================================================\n  # Round 1-8 历史 issues（全部 resolved，压缩保留）\n  # ============================================================\n  - id: R1-N1-old\n    summary: \"Untrained baseline 无法隔离 VLA fine-tuning vs Llama-2 语言预训练的贡献\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    resolution: \"三条件数据完整整合。\"\n    resolution_round: 3\n    mentions: []\n    action_items: []\n  - id: R1-N2-old\n    summary: \"单一模型 Title/Abstract 使用复数 'VLAs' 构成 overclaim\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    resolution: \"Title 改为单数。\"\n    resolution_round: 3\n    mentions: []\n    action_items: []\n  - id: R1-N4-old\n    summary: \"Design implications 完全基于 correlational evidence\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    resolution: \"Abstract 使用 hedge 语气。\"\n    resolution_round: 3\n    mentions: []\n    action_items: []\n  - id: R1-N3-old\n    summary: \"RSA best-vs-best selection bias\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    resolution: \"Same-layer comparison 为 primary evidence。\"\n    resolution_round: 3\n    mentions: []\n    action_items: []\n  - id: R2-N1-old\n    summary: \"Neo et al. (ICLR 2025) 未引用\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    resolution: \"已引用。\"\n    resolution_round: 3\n    mentions: []\n    action_items: []\n  - id: R2-W1-old\n    summary: \"Related Work 引用覆盖度不足\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    resolution: \"引用数量达标。\"\n    resolution_round: 3\n    mentions: []\n    action_items: []\n  - id: R1-W1-old\n    summary: \"'Instruction-blind' claim 过强\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    resolution: \"MLP probe 双重验证。\"\n    resolution_round: 3\n    mentions: []\n    action_items: []\n  - id: R1-W2-old\n    summary: \"CKA 反转 RSA 排序处理不充分\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    resolution: \"Method 新增 'Why RSA over CKA'。\"\n    resolution_round: 2\n    mentions: []\n    action_items: []\n  - id: R3-N1-old\n    summary: \"Limitations 格式\"\n    category: format\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    resolution: \"改为 subsection。\"\n    resolution_round: 3\n    mentions: []\n    action_items: []\n  - id: R3-N2-old\n    summary: \"em-dash AI 写作标志\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    resolution: \"零残留。\"\n    resolution_round: 2\n    mentions: []\n    action_items: []\n  - id: R3-W5-old\n    summary: \"无 code/data 释放声明\"\n    category: format\n    severity: info\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    resolution: \"Conclusion 加声明。\"\n    resolution_round: 3\n    mentions: []\n    action_items: []\n\n  # ============================================================\n  # Round 4-8 issues（全部 resolved）\n  # ============================================================\n  - id: R4-N1\n    summary: \"C1 是 causal mask 必然结果 + probe trivially easy\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 13\n    resolution: \"Abstract 'confirms expected' + 'consistent with causal attention mask' + 'framework sanity check' 三重降格。Contribution (iii) 定位为 methodology validation。全文一致。\"\n    resolution_round: 13\n    mentions:\n      - round: 9\n        reviewers: [1, 2]\n        note: \"R9-W2: C1 在 Abstract/Introduction 占比失衡。\"\n      - round: 10\n        reviewers: [1, 2]\n        note: \"RESOLVED。降格处理到位。\"\n      - round: 12\n        reviewers: [2, 3]\n        note: \"复发。R2-N1: 虽已降为 sanity check，但 Title 'Vision Encodes, Language Routes' 和 Abstract 'strict functional specialization' 仍将架构约束呈现为核心贡献。R3 agree with nuance。\"\n      - round: 13\n        reviewers: [1, 2]\n        note: \"RESOLVED。三重降格处理精准，Title 'Vision Encodes' 作为修辞性 shorthand 可接受。R1+R2 共识。\"\n    action_items:\n      - round: 12\n        action: \"Title 不再暗示 token specialization 是实证发现；Abstract 'strict' 改为 'expected'\"\n        assigned_to: research_director\n        status: done\n  - id: R4-N2\n    summary: \"RSA inverted-U metric-dependent，CKA 反转\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 8\n    resolution: \"C3 降为 qualified observation + §4.4 CKA 正文讨论。\"\n    resolution_round: 8\n    mentions: []\n    action_items: []\n  - id: R4-N3\n    summary: \"L1 ablation 使用 5 demos\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 5\n    resolution: \"改用 50 demos (N=63,228)。\"\n    resolution_round: 5\n    mentions: []\n    action_items: []\n  - id: R4-W1\n    summary: \"RSA best-vs-best n.s. 未标注\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 5\n    resolution: \"已标注。\"\n    resolution_round: 5\n    mentions: []\n    action_items: []\n  - id: R4-W2\n    summary: \"缺乏多重比较校正\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 5\n    resolution: \"FDR 已应用。\"\n    resolution_round: 5\n    mentions: []\n    action_items: []\n  - id: R4-W3\n    summary: \"Probe N 未报告，MLP capacity 控制不充分\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 7\n    resolution: \"Demo-level split 完全消除时间泄漏。\"\n    resolution_round: 7\n    mentions: []\n    action_items: []\n  - id: R4-W4\n    summary: \"Frozen encoder confound\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 5\n    resolution: \"Introduction + Discussion 说明。\"\n    resolution_round: 5\n    mentions: []\n    action_items: []\n\n  # ============================================================\n  # Round 9-11 issues\n  # ============================================================\n  - id: R9-N1\n    summary: \"单一模型(OpenVLA-7B)单一基准(LIBERO)，无法支撑 VLA 通用性\"\n    category: experiment\n    severity: critical\n    status: wont_fix\n    first_raised_round: 9\n    last_seen_round: 13\n    mentions:\n      - round: 9\n        reviewers: [1, 2]\n        note: \"双方 AGREE critical。\"\n      - round: 10\n        reviewers: [1, 2]\n        note: \"STILL_OPEN。Residual scope limitation。\"\n      - round: 11\n        reviewers: [1]\n        note: \"维持 wont_fix。Rebuttal 准备就绪。\"\n      - round: 12\n        reviewers: [1, 2, 3]\n        note: \"R12 fresh review 再次提出。R1-N3 + R2-N3: 2 个同质架构不足以支撑 cross-architecture claim。三位 Reviewer 全部 AGREE。\"\n      - round: 13\n        reviewers: [1, 2]\n        note: \"Claims 已恰当弱化：所有位置加 'causal-decoder' 限定（7+ 处），Limitations 明确指出 flow-matching/diffusion 不适用。R1 判 RESOLVED（claim 层面），R2 AGREE。维持 wont_fix 因实验数据未增加。\"\n    action_items:\n      - round: 10\n        action: \"Rebuttal 应对：causal mask 泛化 + testable predictions + Discussion 已列预测\"\n        assigned_to: research_director\n        status: pending\n    resolution: \"Claims 已限定为 'causal-decoder VLAs'。实验数据仍为 2 个同质架构，结构性局限不变。Rebuttal 应对。\"\n    resolution_round: null\n\n  - id: R9-N2\n    summary: \"所有分析均为 open-loop，无 closed-loop 机器人评估\"\n    category: experiment\n    severity: critical\n    status: wont_fix\n    first_raised_round: 9\n    last_seen_round: 13\n    mentions:\n      - round: 9\n        reviewers: [1, 2]\n        note: \"双方 AGREE critical。\"\n      - round: 10\n        reviewers: [1, 2]\n        note: \"STILL_OPEN。D074 放弃。\"\n      - round: 11\n        reviewers: [1]\n        note: \"维持 wont_fix。Open-loop triangulation rebuttal 准备就绪。\"\n      - round: 12\n        reviewers: [1, 2, 3]\n        note: \"R12 fresh review 再次以最高优先级提出。R1-N1 + R2-N2: 纯 open-loop analysis 对 CoRL 是致命缺陷。三位 Reviewer 最强共识项。\"\n      - round: 13\n        reviewers: [1, 2]\n        note: \"PARTIALLY_RESOLVED。诚实承认 open-loop + 引用同期工作 precedent + 两个 actionable implications。但 'orthogonal contribution' 措辞 dismissive——closed-loop 不是 orthogonal 而是 complementary and necessary。R2 补充：Häon 有 zero-shot behavioral steering 验证，Grant 有 Action Atlas 工具，本文 implications 均未验证。\"\n    action_items:\n      - round: 10\n        action: \"Rebuttal 应对：open-loop 三角验证有独立价值\"\n        assigned_to: research_director\n        status: pending\n      - round: 13\n        action: \"将 'orthogonal contribution' 改为 'complementary and necessary next step'\"\n        assigned_to: research_director\n        status: pending\n    resolution: \"D074 放弃（SR=0/3）。Open-loop triangulation rebuttal 应对。R13 framing 改善但 'orthogonal' 措辞仍需修改。\"\n    resolution_round: null\n\n  - id: R9-N3\n    summary: \"'Causal' 术语在 observational open-loop 分析中使用不当\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 9\n    last_seen_round: 10\n    resolution: \"Discussion 'Causal' → 'Interventional'；§4.3 heading 改为 'Open-loop functional sensitivity'。\"\n    resolution_round: 10\n    mentions:\n      - round: 10\n        reviewers: [1, 2]\n        note: \"RESOLVED。\"\n    action_items: []\n\n  - id: R9-N4\n    summary: \"Ablation 使 R² 增加的 paradox 未充分解释\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 9\n    last_seen_round: 11\n    resolution: \"Discussion 加 information-computation dissociation 解释。MSE 证据 (ΔMSE≈0) 支撑。\"\n    resolution_round: 11\n    mentions:\n      - round: 10\n        reviewers: [1, 2]\n        note: \"PARTIALLY_RESOLVED。\"\n      - round: 11\n        reviewers: [1]\n        note: \"RESOLVED。\"\n    action_items: []\n\n  - id: R9-N5\n    summary: \"Counterfactual 的 'semantic distance' 概念未定义且不可测量\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 9\n    last_seen_round: 10\n    resolution: \"改用 Jaccard token overlap / token novelty (1 - Jaccard)。\"\n    resolution_round: 10\n    mentions:\n      - round: 10\n        reviewers: [1, 2]\n        note: \"RESOLVED。\"\n    action_items: []\n\n  - id: R9-N6\n    summary: \"N=10 tasks 的 RSA bootstrap 统计功效不足\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 9\n    last_seen_round: 12\n    resolution: \"§4.4 加 power limitation 声明。\"\n    resolution_round: 11\n    mentions:\n      - round: 11\n        reviewers: [1]\n        note: \"RESOLVED。\"\n      - round: 12\n        reviewers: [1, 2]\n        note: \"R12 重新提及为 warning (R1-W2)。声明存在但 N=10 根本局限未变。不升级 severity。\"\n    action_items: []\n\n  - id: R9-W1\n    summary: \"CoRL scope fit 有限：纯 representational analysis，无物理机器人实验\"\n    category: framing\n    severity: critical\n    status: open\n    first_raised_round: 9\n    last_seen_round: 13\n    resolution: \"\"\n    resolution_round: null\n    mentions:\n      - round: 10\n        reviewers: [1, 2]\n        note: \"PARTIALLY_RESOLVED。\"\n      - round: 11\n        reviewers: [1]\n        note: \"RESOLVED。Actionable implication + hedging 恰当。\"\n      - round: 12\n        reviewers: [1, 2, 3]\n        note: \"R12 fresh review 将此升级为 critical。R2-N2: Discussion 的 actionable implications 均为 speculative，未验证。三位 Reviewer AGREE。\"\n      - round: 13\n        reviewers: [1, 2]\n        note: \"PARTIALLY_RESOLVED。Writing-level 改善（具体 implications、诚实 limitations、better positioning）。但核心缺陷——纯 open-loop 无 behavioral validation——无法通过写作修复。R2 补充：Häon 有 closed-loop 验证，Grant 有 Action Atlas，本文 implications 均未验证，'与同期工作标准一致' 论证在严格比较下不完全成立。最终判断取决于 CoRL AC 对纯分析性工作的接受阈值。\"\n    action_items:\n      - round: 12\n        action: \"验证至少一个 actionable implication（如 L1 entropy monitor → closed-loop failure prediction），或改投 ML venue\"\n        assigned_to: research_director\n        status: pending\n\n  - id: R9-W2\n    summary: \"C1 在 Abstract/Introduction/Contributions 中占比失衡\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 9\n    last_seen_round: 10\n    resolution: \"C1 降为末句 sanity check + 末位 + (iii) framework。\"\n    resolution_round: 10\n    mentions:\n      - round: 10\n        reviewers: [1, 2]\n        note: \"RESOLVED。\"\n    action_items: []\n\n  - id: R9-W3\n    summary: \"Vision representation 训练效果微弱，framing 未充分反映\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 9\n    last_seen_round: 10\n    resolution: \"§4.4 标题改为 'Training primarily enhances readout decodability'。\"\n    resolution_round: 10\n    mentions:\n      - round: 10\n        reviewers: [1, 2]\n        note: \"RESOLVED。\"\n    action_items: []\n\n  - id: R9-W4\n    summary: \"Cohen's d 独立性假设违反\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 9\n    last_seen_round: 13\n    resolution: \"新增 trajectory-level d (2.943)，与 token-level d (0.65) 同时报告。\"\n    resolution_round: 10\n    mentions:\n      - round: 10\n        reviewers: [1, 2]\n        note: \"RESOLVED。\"\n      - round: 12\n        reviewers: [1, 2, 3]\n        note: \"R12 再次提及 (R1-W1)。Trajectory-level d 存在但主文仍以 token-level d 为主要报告。\"\n      - round: 13\n        reviewers: [1, 2]\n        note: \"RESOLVED。双级报告充分，trajectory-level d=2.943 确认主要发现 robust。\"\n    action_items: []\n\n  - id: R9-W5\n    summary: \"Pretrained Llama-2 base 的 9/32 heads 可能因 text in-distribution bias\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 9\n    last_seen_round: 10\n    resolution: \"Discussion 新增替代解释承认。\"\n    resolution_round: 10\n    mentions:\n      - round: 10\n        reviewers: [1, 2]\n        note: \"RESOLVED。\"\n    action_items: []\n\n  - id: R9-W6\n    summary: \"Specificity control 效果有限(d ratio 1.08×)\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 9\n    last_seen_round: 11\n    resolution: \"四组 matched-size 比较，framing 'distributed routing'。\"\n    resolution_round: 11\n    mentions:\n      - round: 11\n        reviewers: [1]\n        note: \"标 resolved（论文文本 well-calibrated）。\"\n    action_items: []\n\n  - id: R9-W7\n    summary: \"N=63,228 观测的独立性——有效独立单元远小于报告值\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 9\n    last_seen_round: 12\n    resolution: \"§4.1 新增 N_eff 说明。\"\n    resolution_round: 10\n    mentions:\n      - round: 10\n        reviewers: [1, 2]\n        note: \"RESOLVED。\"\n      - round: 12\n        reviewers: [1, 2]\n        note: \"R12 再次提及 (R1-W3)。N_eff 存在但 method section 未明确标注哪些分析用 token-level vs aggregated。\"\n    action_items: []\n\n  - id: R9-I1\n    summary: \"缺失引用：Octo (Ghosh et al. 2024)\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 9\n    last_seen_round: 10\n    resolution: \"references.bib 新增。\"\n    resolution_round: 10\n    mentions: []\n    action_items: []\n\n  - id: R9-I2\n    summary: \"Häon et al. 2025 的 sparse semantic directions 与 L1 routing heads 的关系未讨论\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 9\n    last_seen_round: 11\n    resolution: \"Discussion 加 where/what 互补连接。\"\n    resolution_round: 11\n    mentions: []\n    action_items: []\n\n  - id: R9-I3\n    summary: \"多处小问题：Table 1 caption、脚注、accessed date\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 9\n    last_seen_round: 10\n    resolution: \"已修复。\"\n    resolution_round: 10\n    mentions: []\n    action_items: []\n\n  - id: R10-Q1\n    summary: \"Per-task MSE breakdown：消融后 MSE 不变是否存在 task-level cancellation\"\n    category: experiment\n    severity: info\n    status: resolved\n    first_raised_round: 10\n    last_seen_round: 11\n    resolution: \"Appendix 加 per-task breakdown。\"\n    resolution_round: 11\n    mentions: []\n    action_items: []\n\n  # ============================================================\n  # Round 12 (fresh review) issues — updated with R13 verdicts\n  # ============================================================\n\n  - id: R12-N1\n    summary: \"因果 overclaiming：Title 'Routes' 暗示因果机制，但证据为 correlational + weak specificity（d ratio 仅 1.08×）\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 12\n    last_seen_round: 13\n    mentions:\n      - round: 12\n        reviewers: [1, 2, 3]\n        note: \"R1-N2 提出，R2 AGREE（与其 W2 一致），R3 AGREE with nuance。\"\n      - round: 13\n        reviewers: [1, 2]\n        note: \"RESOLVED。Title 'Routes'→'Reorganizes'。全文 grep 零残留 'routing'。所有关键位置使用 'redistributes'。三级证据分类在新框架下恰当。R1+R2 共识。\"\n    action_items:\n      - round: 12\n        action: \"将 Title 'Routes' 降级或改为更审慎表述；主文 framing 区分 interventional evidence 和 causal mechanism\"\n        assigned_to: research_director\n        status: done\n    resolution: \"Title 'Routes'→'Reorganizes'，全文 'routing'→'redistributes'，零残留。\"\n    resolution_round: 13\n\n  - id: R12-N2\n    summary: \"正文超出 CoRL 8 页限制约 0.7 页（Discussion+Conclusion 延伸到第 9 页）\"\n    category: format\n    severity: critical\n    status: resolved\n    first_raised_round: 12\n    last_seen_round: 13\n    mentions:\n      - round: 12\n        reviewers: [1, 2, 3]\n        note: \"R3-N1 提出，R1+R2 AGREE。超页限是 desk rejection 常见理由。\"\n      - round: 13\n        reviewers: [1, 2]\n        note: \"RESOLVED。Conclusion 在 page 8 底部结束，References 从 page 9 开始。Spacing hacks 激进但合规。R1+R2 共识。\"\n    action_items:\n      - round: 12\n        action: \"压缩至 8 页\"\n        assigned_to: research_director\n        status: done\n    resolution: \"正文严格控制在 8 页内。Spacing 参数激进（textfloatsep=6pt）但合规。\"\n    resolution_round: 13\n\n  - id: R12-N3\n    summary: \"Abstract/Introduction 信息过载：Abstract 塞入 15+ 定量结果，Introduction 与 Abstract 高度重复\"\n    category: writing\n    severity: critical\n    status: resolved\n    first_raised_round: 12\n    last_seen_round: 13\n    mentions:\n      - round: 12\n        reviewers: [1, 2, 3]\n        note: \"R3-N2 提出，R1+R2 AGREE。\"\n      - round: 13\n        reviewers: [1, 2]\n        note: \"RESOLVED。Abstract 定量值从 15+ 降至 ~1 个。Introduction 不再复制 Abstract 数字。关键信息完整保留。R1+R2 共识。\"\n    action_items:\n      - round: 12\n        action: \"重写 Abstract（精简至 3 个定性发现 + 最关键数字）；Introduction 去重\"\n        assigned_to: research_director\n        status: done\n    resolution: \"Abstract 精简至 ~1 个定量值 + 定性发现。Introduction 去重。\"\n    resolution_round: 13\n\n  - id: R12-W1\n    summary: \"无首页 teaser figure：Figure 1 直到第 6-7 页才出现，前 4 页纯文字墙\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 12\n    last_seen_round: 13\n    mentions:\n      - round: 12\n        reviewers: [2, 3]\n        note: \"R3-W1 提出，R2 AGREE。\"\n      - round: 13\n        reviewers: [1, 2]\n        note: \"RESOLVED。Figure 1 位于 page 1 顶部（architecture overview + attention redistribution 对比图）。Caption 自包含，尺寸合理。R1+R2 共识。\"\n    action_items:\n      - round: 12\n        action: \"在 page 1 或 2 增加 overview/teaser figure\"\n        assigned_to: research_director\n        status: done\n    resolution: \"Page 1 新增 Figure 1（architecture overview + instruction attention redistribution）。\"\n    resolution_round: 13\n\n  - id: R12-W2\n    summary: \"层编号 off-by-one：'L1--L31 the 32 transformer layers' 实为 31 个索引\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 12\n    last_seen_round: 13\n    mentions:\n      - round: 12\n        reviewers: [2, 3]\n        note: \"R3-W2 提出，R2 AGREE。\"\n      - round: 13\n        reviewers: [1, 2]\n        note: \"RESOLVED。L1-L32 = 32 层，全文一致。L32 定义轻微歧义（post-LN output），影响极小。R1+R2 共识。\"\n    action_items:\n      - round: 12\n        action: \"统一层标号定义\"\n        assigned_to: research_director\n        status: done\n    resolution: \"L1-L32 = 32 层。L32 定义轻微歧义为 camera-ready 修复项。\"\n    resolution_round: 13\n\n  - id: R12-W3\n    summary: \"多条引用使用 arXiv preprint 而非已发表版本（OpenVLA, Prismatic VLMs, Llama 2 等）\"\n    category: writing\n    severity: warning\n    status: in_progress\n    first_raised_round: 12\n    last_seen_round: 13\n    mentions:\n      - round: 12\n        reviewers: [2, 3]\n        note: \"R3-W3 提出，R2 AGREE。\"\n      - round: 13\n        reviewers: [1, 2]\n        note: \"PARTIALLY_RESOLVED。3/3 被要求的已更新（kim2024→CoRL, karamcheti2024→ICML, haon2025→CoRL）。仍有 2 条可更新：belrose2023（→NeurIPS 2023）、padalkar2023（→ICRA 2024）。Camera-ready 级别。R1+R2 共识。\"\n    action_items:\n      - round: 12\n        action: \"更新所有已发表论文的引用至正式版本\"\n        assigned_to: research_director\n        status: in_progress\n      - round: 13\n        action: \"更新 belrose2023→NeurIPS 2023, padalkar2023→ICRA 2024\"\n        assigned_to: research_director\n        status: pending\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R12-W4\n    summary: \"缺失 6 篇重要 related work（visual token encoding, causal mask analysis, VIP, AVA-VLA 等）\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 12\n    last_seen_round: 13\n    mentions:\n      - round: 12\n        reviewers: [2]\n        note: \"R2 提出 6 篇 missing references。\"\n      - round: 13\n        reviewers: [1, 2]\n        note: \"RESOLVED。6/6 全部添加并正确引用。额外添加 pei2025rethinking（causal mask）。引用总数 52→59，0 orphan + 0 missing。R1+R2 共识。\"\n    action_items:\n      - round: 12\n        action: \"验证并引用相关文献\"\n        assigned_to: research_director\n        status: done\n    resolution: \"6/6 缺失引用全部补齐 + 1 篇额外添加。引用总数 52→59。\"\n    resolution_round: 13\n\n  - id: R12-W5\n    summary: \"与 Grant et al. (2026) 和 Häon et al. (2025) 的区分不够清晰\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 12\n    last_seen_round: 13\n    mentions:\n      - round: 12\n        reviewers: [2, 3]\n        note: \"R2-W3 提出，R3 AGREE。\"\n      - round: 13\n        reviewers: [1, 2]\n        note: \"RESOLVED。Related Work 新增显式对比段落：Grant (feature-level, what) / Häon (steering-direction, what) / 本文 (token-level per-layer, where)。区分清晰准确。R1+R2 共识。\"\n    action_items:\n      - round: 12\n        action: \"Related Work 或 Discussion 加与 Grant/Häon 的对比段落\"\n        assigned_to: research_director\n        status: done\n    resolution: \"Related Work 加显式 what-vs-where 对比段落。\"\n    resolution_round: 13\n\n  - id: R12-W6\n    summary: \"FDR 多重比较校正细节不足（未说明方法类型、family scope、adjusted p-values）\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 12\n    last_seen_round: 13\n    mentions:\n      - round: 12\n        reviewers: [1, 2]\n        note: \"R1-W4 提出，R2 AGREE。\"\n      - round: 13\n        reviewers: [1, 2]\n        note: \"RESOLVED。明确指定 Benjamini-Hochberg 方法、α=0.05、33-layer family per metric。R1+R2 共识。\"\n    action_items:\n      - round: 12\n        action: \"明确报告 FDR method、correction family scope\"\n        assigned_to: research_director\n        status: done\n    resolution: \"BH 方法 + α=0.05 + 33-layer family per metric 完整报告。\"\n    resolution_round: 13\n\n  - id: R12-I1\n    summary: \"术语不一致：readout token vs last_preaction, instruction-dominant vs dominant heads\"\n    category: writing\n    severity: info\n    status: in_progress\n    first_raised_round: 12\n    last_seen_round: 13\n    mentions:\n      - round: 12\n        reviewers: [2, 3]\n        note: \"R3-W5 提出，R2 AGREE。\"\n      - round: 13\n        reviewers: [1, 2]\n        note: \"PARTIALLY_RESOLVED。叙事文本中 'readout token' 基本统一。Table 1 的 'last_preaction' 为代码技术标签，建议 caption 中加映射说明。Camera-ready 级别。R1+R2 共识。\"\n    action_items:\n      - round: 13\n        action: \"Table 1 caption 加 '(last_preaction = readout token)' 映射说明\"\n        assigned_to: research_director\n        status: pending\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R12-I2\n    summary: \"Limitations 未作为独立 section（CoRL 要求 Limitations section）\"\n    category: format\n    severity: info\n    status: in_progress\n    first_raised_round: 12\n    last_seen_round: 13\n    mentions:\n      - round: 12\n        reviewers: [2, 3]\n        note: \"R3-W4 提出，R2 部分 REBUT。\"\n      - round: 13\n        reviewers: [1, 2]\n        note: \"PARTIALLY_RESOLVED。使用 \\\\paragraph{Limitations and scope.} 而非 \\\\subsection。内容覆盖关键 limitations。技术上合规但建议改为 \\\\subsection*{Limitations}。低优先级。R1+R2 共识。\"\n    action_items:\n      - round: 13\n        action: \"考虑将 Limitations 改为 \\\\subsection*{Limitations}\"\n        assigned_to: research_director\n        status: pending\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R12-DIV1\n    summary: \"Title 'Language Routes' 是否误导——R3 REBUT（三条件 0/9/24 heads 证明非纯 positional），R2 维持\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 12\n    last_seen_round: 13\n    mentions:\n      - round: 12\n        reviewers: [2, 3]\n        note: \"DIVERGENT。R2-W1 vs R3 REBUT。\"\n      - round: 13\n        reviewers: [1, 2]\n        note: \"RESOLVED。Title 改为 'Language Reorganizes'，消除了 'Routes' 的因果误导。R1+R2 共识。\"\n    action_items: []\n    resolution: \"Title 'Routes'→'Reorganizes' 消除误导。\"\n    resolution_round: 13\n\n  # ============================================================\n  # Round 13 — NEW issues\n  # ============================================================\n\n  - id: R13-W1\n    summary: \"'Orthogonal contribution' 措辞对 closed-loop validation 过于 dismissive\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 13\n    last_seen_round: 13\n    mentions:\n      - round: 13\n        reviewers: [1, 2]\n        note: \"R1 NEW-2 提出，R2 强烈 AGREE。'Orthogonal' 暗示 closed-loop 验证与本文 claims 无关，实际上是验证 practical significance 的必要步骤。建议改为 'complementary and necessary next step'。\"\n    action_items:\n      - round: 13\n        action: \"Discussion 中 'orthogonal contribution' 改为 'complementary and necessary next step' 或类似措辞\"\n        assigned_to: research_director\n        status: pending\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R13-I1\n    summary: \"附录 'robust attractor' 措辞较主文更强（N=2 架构偏强）\"\n    category: framing\n    severity: info\n    status: open\n    first_raised_round: 13\n    last_seen_round: 13\n    mentions:\n      - round: 13\n        reviewers: [1, 2]\n        note: \"R1 NEW-3 提出，R2 AGREE。仅在附录，不影响主文 claims。建议改为 'consistent convergence pattern'。\"\n    action_items:\n      - round: 13\n        action: \"附录 'robust attractor' 考虑改为 'consistent convergence pattern'\"\n        assigned_to: research_director\n        status: pending\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R13-I2\n    summary: \"Spacing 压缩激进（textfloatsep=6pt, abovecaptionskip=2pt），合规但处于边界\"\n    category: format\n    severity: info\n    status: open\n    first_raised_round: 13\n    last_seen_round: 13\n    mentions:\n      - round: 13\n        reviewers: [1, 2]\n        note: \"R1 NEW-4 + R2 NEW-3。合规但处于 CoRL 模板边界。建议 textfloatsep 恢复至 8-10pt 如有余量。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null"
  }
}
```

</details>

---


### Tool result

_source line 984 · 2026-05-20T16:19:31.832899+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/review_issues.yaml\", \"bytes\": 26190}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 985 · 2026-05-20T16:21:18.032751+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "project": "vla-ssd",
  "report": "# Round 13 审稿报告（Continue Review）\n\n**论文**: \"Vision Encodes, Language Reorganizes: Token-Level Representational Analysis of VLA Fine-Tuning\"\n**Venue**: CoRL 2026（截止 2026-05-29）\n**审稿模式**: 继续审稿（基于 Round 12 修改验证）\n**Reviewer 编排**: 2 人（R1: 方法/实验/因果 framing; R2: 呈现/格式/引用）\n**轮次**: 1 轮独立审稿 + 交叉分享，首轮即达成完全共识\n\n---\n\n## Summary\n\n本轮为 Round 12（Weak Reject, 4/10）之后的修改验证审稿。作者对 Round 12 提出的 6 个 critical issues 和 8 个 warning issues 进行了全面回应。修改涉及：标题重写（Routes→Reorganizes）、因果语言全文替换（routing→redistributes）、Finding 3 降格为 sanity check、跨架构 claim 限定为 causal-decoder、Abstract 精简（15+ 数值→~1）、新增 page 1 teaser figure、补齐 7 篇缺失引用、FDR 细节完善、层编号修正、页面压缩至 8 页内。修改质量高、覆盖面广、执行彻底。\n\n---\n\n## Strengths\n\n1. **因果语言修正彻底**：全文 grep 零残留 \"routing\"。Title→\"Reorganizes\"，正文全部使用 \"redistributes\"。三级证据分类（interventional / supporting / constraining）在新框架下更恰当。这是本轮最重要的改善。\n\n2. **Finding 3 降格处理精准**：Abstract \"confirms expected\" + \"consistent with the causal attention mask\" + \"framework sanity check\" 三重标注。Contribution (iii) 定位为 \"methodology validation\"。既不过度削弱（sanity check 仍有方法论价值），也不残留 overclaiming。\n\n3. **跨架构限定一致无遗漏**：所有 7+ 处 cross-architecture claim 均加上 \"causal-decoder\" 或 \"the two architectures studied\" 限定。Limitations 明确指出 flow-matching/diffusion 架构不适用。推测性预测已移除。\n\n4. **Abstract 精简效果显著**：从 15+ 定量值压缩到 ~1 个，三个 findings 以 First/Second/Third 结构呈现。Introduction 不再复制 Abstract 数字。可读性大幅提升。\n\n5. **Teaser Figure 有效**：page 1 的 Figure 1（architecture overview + attention redistribution 对比图）为读者提供了即时的视觉理解入口。Caption 自包含，尺寸合理。\n\n6. **缺失引用全部补齐**：6/6 被要求的引用 + 1 篇额外添加（pei2025rethinking），引用总数 52→59。Related Work 新增 Grant/Häon 显式对比段落（what-vs-where 区分清晰）。\n\n7. **技术修复完成**：层编号 L1-L32 修正、Cohen's d 双级报告（token-level + trajectory-level d=2.943）、FDR 完整规范（BH, α=0.05, 33-layer family per metric）。\n\n8. **修改一致性极高**：从 Title 到 Conclusion，\"redistributes instruction attention\" 贯穿始终。无残留不一致。\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**W1 [critical, structural] 纯 open-loop 分析，无 behavioral validation（R9-N2 + R9-W1）**\n\n论文所有分析均为 open-loop representational analysis，未提供任何 closed-loop 机器人评估。Discussion 提出两个 actionable implications——(a) L1 attention entropy 监控 fine-tuning 质量，(b) token pruning strategy——但均未经实验验证。\n\n修改后 Discussion 使用 \"orthogonal contribution\" 描述 closed-loop validation，暗示其与本文 claims 无关。实际上，closed-loop validation 是验证本文 claims 实用价值的 **必要** 步骤，不是 orthogonal 的。R2 补充关键对比：Häon et al. 不仅做了 mechanistic analysis，还展示了基于发现的 zero-shot behavioral steering（LIBERO + UR5 真实机器人验证）；Grant et al. 生成了 Action Atlas 工具。本文的两个 implications 均无类似验证。因此，\"与同期工作标准一致\" 的论证在严格比较下不完全成立。\n\n这是 **结构性缺陷**，无法通过 writing 修复。最终判断取决于 CoRL AC 对纯分析性工作的接受阈值。\n\n### Should-Fix（camera-ready 前修复）\n\n**W2 [warning] \"orthogonal contribution\" 措辞 dismissive（R13-W1, NEW）**\n\nDiscussion 中 \"Closed-loop validation on downstream task success is an orthogonal contribution\" 的措辞过于 dismissive。建议改为 \"a complementary and necessary next step\" 或 \"an essential validation step that we leave for future work\"。R1 提出，R2 强烈 AGREE。\n\n**W3 [warning] 2 条 arXiv 引用仍可更新（R12-W3 残留）**\n\nbelrose2023（Tuned Lens）仍为 arXiv，已发表于 NeurIPS 2023。padalkar2023（Open X-Embodiment）仍为 arXiv，已发表于 ICRA 2024。低优先级。\n\n### Nice-to-Have\n\n**W4 [info] L32 定义轻微歧义**：\"with L32 including the final layer norm\" 可更明确为 \"L32 denotes the output after the final RMSNorm applied to the 32nd transformer layer\"。\n\n**W5 [info] Table 1 术语映射**：caption 中建议加 \"(last_preaction = readout token)\" 以明确代码标签与叙事术语的对应。\n\n**W6 [info] Limitations 格式**：当前使用 \\paragraph{Limitations and scope.}，建议改为 \\subsection*{Limitations} 以更明确满足 CoRL 要求。\n\n**W7 [info] 附录 \"robust attractor\" 措辞偏强**：附录中 \"robust attractor of VLA training\" 从 N=2 架构得出偏强。建议改为 \"consistent convergence pattern\"。\n\n**W8 [info] Spacing 压缩处于边界**：\\textfloatsep=6pt（默认~20pt），合规但激进。如有余量建议恢复至 8-10pt。\n\n---\n\n## Reviewer Consensus\n\n所有交叉回应均为 [AGREE]，零 [REBUT]。以下为完全共识项：\n\n| Issue | 判定 | 共识强度 |\n|-------|------|---------|\n| R12-N1 因果 overclaiming | **RESOLVED** | 强（R1+R2 一致） |\n| R4-N1 Finding 3 overclaiming | **RESOLVED** | 强（R1+R2 一致） |\n| R9-N1 跨架构泛化 claim | **RESOLVED**（claim 层面） | 强 |\n| R12-N2 页面超限 | **RESOLVED** | 强 |\n| R12-N3 信息过载 | **RESOLVED** | 强 |\n| R12-W1 Teaser figure | **RESOLVED** | 强 |\n| R12-W2 层编号 | **RESOLVED** | 强 |\n| R12-W4 缺失引用 | **RESOLVED** | 强 |\n| R12-W5 Grant/Häon 区分 | **RESOLVED** | 强 |\n| R12-W6 FDR 细节 | **RESOLVED** | 强 |\n| R9-W4 Cohen's d | **RESOLVED** | 强 |\n| R12-DIV1 Title 误导 | **RESOLVED** | 强 |\n| R9-N2 closed-loop | **PARTIALLY_RESOLVED** | 强（\"orthogonal\" dismissive） |\n| R9-W1 CoRL scope | **PARTIALLY_RESOLVED** | 强（writing 改善，structural 不变） |\n| R12-W3 arXiv 引用 | **PARTIALLY_RESOLVED** | 强（2 条残留） |\n| R13-W1 \"orthogonal\" 措辞 | **NEW warning** | 强 |\n\n---\n\n## Reviewer Divergence\n\n**无分歧。** 本轮所有交叉回应均为 [AGREE]。\n\n---\n\n## Questions\n\n1. Discussion 中 \"orthogonal contribution\" 是否为有意选择？如果是，请解释为何 closed-loop validation 被认为与本文 claims 的实用价值无关。\n2. 两个 actionable implications（L1 entropy 监控、token pruning）是否有任何初步实验验证（即使是 pilot data）？\n\n---\n\n## Missing References\n\nRound 12 提出的 6 篇缺失引用已全部补齐。仍有 2 条引用可从 arXiv 更新为正式出版版本：\n- belrose2023 (Tuned Lens): arXiv → NeurIPS 2023\n- padalkar2023 (Open X-Embodiment): arXiv → ICRA 2024\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n**状态：未请求。** 本项目未配置外部审稿。\n\n---\n\n## Visual Layout Check\n\n**状态：已完成**（耗时 ~3 分钟）\n\n3 warnings + 9 info items：\n\n**Warnings:**\n1. **Pages 2-4 文字墙**：连续 3 页纯文本（Related Work + Method 开头），无 display item。建议 Section 3 加 pipeline 示意图或方法概览表。\n2. **Page 6 结果段纯文本**：5 组实验结果全用行内数字描述，无图表支撑。建议将 dose-response 或 counterfactual 结果可视化。\n3. **Page 31 末页空白**：附录末页仅 ~7 行文字，~90% 空白。\n\n**Info items（不影响接收）:**\n- Figure 1 子面板部分标签偏小（建议 ≥8pt）\n- Table 1 caption 较长（5 行）\n- Figure 2 灰度打印区分度可能不足（建议加 hatching）\n- Figure 3 色盲友好 ✓\n- Table 2/3 格式规范 ✓\n- 附录 display items 密度高，部分可视化（Figure 9 dose-response、Figure 10 diagnostics）可考虑提升至正文\n- Table 25 信息密度极高\n\n---\n\n## Overall Assessment\n\n**评分: 5/10 — Borderline**\n**置信度: 4/5**\n\n**评分变化: 4/10 (Round 12, Weak Reject) → 5/10 (Round 13, Borderline)，上调 1 分**\n\n### 上调理由\n\n1. **因果语言全面修正**（+0.5）：Routes→Reorganizes + routing→redistributes 消除了 Round 12 最突出的 methodological criticism。执行彻底，零残留。\n2. **Finding 3 降格 + 跨架构限定**（+0.25）：论文 claims 与 evidence 的匹配度显著提升。\"Confirms expected\" + \"causal-decoder VLAs\" 的诚实限定增强了学术可信度。\n3. **呈现性全面改善**（+0.25）：Abstract 精简、Teaser figure、引用补齐、Related Work 区分、技术细节完善。Clarity 从 7/10 提升至 8/10。\n\n### 未达 6/10 (Weak Accept) 的原因\n\n1. **纯 open-loop 分析是结构性缺陷**：论文无法回答 \"这些 attention patterns 对机器人实际执行有什么影响？\" 同期工作（Häon: zero-shot behavioral steering + 真实机器人验证; Grant: Action Atlas 工具）已设定了更高的 actionability 标准。\n2. **Actionable implications 未经验证**：L1 entropy 监控和 token pruning 仍为推测性建议。\"Representational analysis has independent design value\" 的论证力度对 CoRL 审稿人可能不足。\n3. **CoRL scope fit 取决于 AC 判断**：如果 committee 认为 VLA 解释性分析本身对 CoRL 有价值（类似同期 open-loop 分析工作），论文的 methodological rigor 和 revision quality 足以支持 borderline accept。如果要求 closed-loop evidence，则仍在 reject 边界。\n\n### Reviewer 评分\n\n| Reviewer | Round 12 | Round 13 | 变化 |\n|----------|----------|----------|------|\n| R1 (方法/实验) | 3.0/5 | 3.5/5 (Borderline Accept) | +0.5 |\n| R2 (呈现/格式) | 4/10 | 5/10 (Borderline) | +1 |\n\n### 修改质量评价\n\n本轮修改质量 **优秀**。作者认真回应了几乎所有 Round 12 issues，执行彻底且一致性极高。12 个 Round 12 issues 中 10 个 fully resolved，2 个 partially resolved（arXiv 引用残留、术语映射）。核心 framing 问题（overclaiming、Finding 3、cross-architecture）的修正尤其出色。唯一新增的 warning 级问题是 \"orthogonal contribution\" 措辞。\n\n残留问题集中在两个结构性限制上（open-loop + CoRL scope），这些无法通过 writing 修复，需要在 rebuttal 中正面应对。\n\n---\n\n## Detailed Comments\n\n### Section 1: Introduction\n- ✅ 不再复制 Abstract 数字，增加方法论细节和对比定位\n- ✅ 引用 wang2025seeing, pei2025rethinking 支持 causal mask 讨论\n- ✅ Contribution (iii) 明确定位 Finding 3 为 \"methodology validation\"\n\n### Section 2: Related Work\n- ✅ 新增 Grant/Häon 显式对比段落（what-vs-where 区分清晰）\n- ✅ 7 篇新引用正确放置在对应段落\n- ✅ AVA-VLA, causal mask analysis 文献覆盖到位\n\n### Section 3: Method\n- ✅ L1-L32 层编号统一，定义明确\n- ⚠️ L32 post-LN 定义轻微歧义（info 级别）\n\n### Section 4: Experiments\n- ✅ \"Redistributes\" 贯穿全文，零 \"routing\" 残留\n- ✅ Cohen's d 双级报告（token-level 0.65 + trajectory-level 2.943）\n- ✅ FDR: BH, α=0.05, 33-layer family per metric\n- ✅ Cross-architecture claims 全部加 \"causal-decoder\" 限定\n- ⚠️ Page 6 仍为纯文本结果页（视觉审查 warning）\n\n### Section 5: Discussion\n- ✅ \"Redistributes instruction attention\" 为核心总结\n- ✅ Limitations 覆盖：2 架构、LIBERO only、causal-decoder 限制、flow-matching 不适用\n- ⚠️ \"Orthogonal contribution\" 措辞需修改\n- ⚠️ Limitations 使用 \\paragraph 而非 \\subsection（技术上合规）\n\n### Abstract\n- ✅ 从 15+ 定量值精简到 ~1 个\n- ✅ Finding 3 标注为 \"expected\" + \"sanity check\"\n- ✅ \"Two causal-decoder VLA architectures\" 限定\n\n### Title\n- ✅ \"Routes\" → \"Reorganizes\"，避免因果 overclaim\n- ℹ️ \"Language Reorganizes\" 中 Language 作为语法主语是修辞性 convention\n\n### References\n- ✅ 3/3 被要求更新的已完成（kim2024→CoRL, karamcheti2024→ICML, haon2025→CoRL）\n- ⚠️ 2 条可更新残留（belrose2023→NeurIPS 2023, padalkar2023→ICRA 2024）\n\n### Appendix\n- ℹ️ \"Robust attractor\" 措辞较主文更强（N=2 偏强）\n- ℹ️ Page 31 末页 ~90% 空白",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "borderline",
  "review_chat_id": "oc_554a5023cde4d603635cf97e6ab8151a"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "project": "vla-ssd",
    "report": "# Round 13 审稿报告（Continue Review）\n\n**论文**: \"Vision Encodes, Language Reorganizes: Token-Level Representational Analysis of VLA Fine-Tuning\"\n**Venue**: CoRL 2026（截止 2026-05-29）\n**审稿模式**: 继续审稿（基于 Round 12 修改验证）\n**Reviewer 编排**: 2 人（R1: 方法/实验/因果 framing; R2: 呈现/格式/引用）\n**轮次**: 1 轮独立审稿 + 交叉分享，首轮即达成完全共识\n\n---\n\n## Summary\n\n本轮为 Round 12（Weak Reject, 4/10）之后的修改验证审稿。作者对 Round 12 提出的 6 个 critical issues 和 8 个 warning issues 进行了全面回应。修改涉及：标题重写（Routes→Reorganizes）、因果语言全文替换（routing→redistributes）、Finding 3 降格为 sanity check、跨架构 claim 限定为 causal-decoder、Abstract 精简（15+ 数值→~1）、新增 page 1 teaser figure、补齐 7 篇缺失引用、FDR 细节完善、层编号修正、页面压缩至 8 页内。修改质量高、覆盖面广、执行彻底。\n\n---\n\n## Strengths\n\n1. **因果语言修正彻底**：全文 grep 零残留 \"routing\"。Title→\"Reorganizes\"，正文全部使用 \"redistributes\"。三级证据分类（interventional / supporting / constraining）在新框架下更恰当。这是本轮最重要的改善。\n\n2. **Finding 3 降格处理精准**：Abstract \"confirms expected\" + \"consistent with the causal attention mask\" + \"framework sanity check\" 三重标注。Contribution (iii) 定位为 \"methodology validation\"。既不过度削弱（sanity check 仍有方法论价值），也不残留 overclaiming。\n\n3. **跨架构限定一致无遗漏**：所有 7+ 处 cross-architecture claim 均加上 \"causal-decoder\" 或 \"the two architectures studied\" 限定。Limitations 明确指出 flow-matching/diffusion 架构不适用。推测性预测已移除。\n\n4. **Abstract 精简效果显著**：从 15+ 定量值压缩到 ~1 个，三个 findings 以 First/Second/Third 结构呈现。Introduction 不再复制 Abstract 数字。可读性大幅提升。\n\n5. **Teaser Figure 有效**：page 1 的 Figure 1（architecture overview + attention redistribution 对比图）为读者提供了即时的视觉理解入口。Caption 自包含，尺寸合理。\n\n6. **缺失引用全部补齐**：6/6 被要求的引用 + 1 篇额外添加（pei2025rethinking），引用总数 52→59。Related Work 新增 Grant/Häon 显式对比段落（what-vs-where 区分清晰）。\n\n7. **技术修复完成**：层编号 L1-L32 修正、Cohen's d 双级报告（token-level + trajectory-level d=2.943）、FDR 完整规范（BH, α=0.05, 33-layer family per metric）。\n\n8. **修改一致性极高**：从 Title 到 Conclusion，\"redistributes instruction attention\" 贯穿始终。无残留不一致。\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**W1 [critical, structural] 纯 open-loop 分析，无 behavioral validation（R9-N2 + R9-W1）**\n\n论文所有分析均为 open-loop representational analysis，未提供任何 closed-loop 机器人评估。Discussion 提出两个 actionable implications——(a) L1 attention entropy 监控 fine-tuning 质量，(b) token pruning strategy——但均未经实验验证。\n\n修改后 Discussion 使用 \"orthogonal contribution\" 描述 closed-loop validation，暗示其与本文 claims 无关。实际上，closed-loop validation 是验证本文 claims 实用价值的 **必要** 步骤，不是 orthogonal 的。R2 补充关键对比：Häon et al. 不仅做了 mechanistic analysis，还展示了基于发现的 zero-shot behavioral steering（LIBERO + UR5 真实机器人验证）；Grant et al. 生成了 Action Atlas 工具。本文的两个 implications 均无类似验证。因此，\"与同期工作标准一致\" 的论证在严格比较下不完全成立。\n\n这是 **结构性缺陷**，无法通过 writing 修复。最终判断取决于 CoRL AC 对纯分析性工作的接受阈值。\n\n### Should-Fix（camera-ready 前修复）\n\n**W2 [warning] \"orthogonal contribution\" 措辞 dismissive（R13-W1, NEW）**\n\nDiscussion 中 \"Closed-loop validation on downstream task success is an orthogonal contribution\" 的措辞过于 dismissive。建议改为 \"a complementary and necessary next step\" 或 \"an essential validation step that we leave for future work\"。R1 提出，R2 强烈 AGREE。\n\n**W3 [warning] 2 条 arXiv 引用仍可更新（R12-W3 残留）**\n\nbelrose2023（Tuned Lens）仍为 arXiv，已发表于 NeurIPS 2023。padalkar2023（Open X-Embodiment）仍为 arXiv，已发表于 ICRA 2024。低优先级。\n\n### Nice-to-Have\n\n**W4 [info] L32 定义轻微歧义**：\"with L32 including the final layer norm\" 可更明确为 \"L32 denotes the output after the final RMSNorm applied to the 32nd transformer layer\"。\n\n**W5 [info] Table 1 术语映射**：caption 中建议加 \"(last_preaction = readout token)\" 以明确代码标签与叙事术语的对应。\n\n**W6 [info] Limitations 格式**：当前使用 \\paragraph{Limitations and scope.}，建议改为 \\subsection*{Limitations} 以更明确满足 CoRL 要求。\n\n**W7 [info] 附录 \"robust attractor\" 措辞偏强**：附录中 \"robust attractor of VLA training\" 从 N=2 架构得出偏强。建议改为 \"consistent convergence pattern\"。\n\n**W8 [info] Spacing 压缩处于边界**：\\textfloatsep=6pt（默认~20pt），合规但激进。如有余量建议恢复至 8-10pt。\n\n---\n\n## Reviewer Consensus\n\n所有交叉回应均为 [AGREE]，零 [REBUT]。以下为完全共识项：\n\n| Issue | 判定 | 共识强度 |\n|-------|------|---------|\n| R12-N1 因果 overclaiming | **RESOLVED** | 强（R1+R2 一致） |\n| R4-N1 Finding 3 overclaiming | **RESOLVED** | 强（R1+R2 一致） |\n| R9-N1 跨架构泛化 claim | **RESOLVED**（claim 层面） | 强 |\n| R12-N2 页面超限 | **RESOLVED** | 强 |\n| R12-N3 信息过载 | **RESOLVED** | 强 |\n| R12-W1 Teaser figure | **RESOLVED** | 强 |\n| R12-W2 层编号 | **RESOLVED** | 强 |\n| R12-W4 缺失引用 | **RESOLVED** | 强 |\n| R12-W5 Grant/Häon 区分 | **RESOLVED** | 强 |\n| R12-W6 FDR 细节 | **RESOLVED** | 强 |\n| R9-W4 Cohen's d | **RESOLVED** | 强 |\n| R12-DIV1 Title 误导 | **RESOLVED** | 强 |\n| R9-N2 closed-loop | **PARTIALLY_RESOLVED** | 强（\"orthogonal\" dismissive） |\n| R9-W1 CoRL scope | **PARTIALLY_RESOLVED** | 强（writing 改善，structural 不变） |\n| R12-W3 arXiv 引用 | **PARTIALLY_RESOLVED** | 强（2 条残留） |\n| R13-W1 \"orthogonal\" 措辞 | **NEW warning** | 强 |\n\n---\n\n## Reviewer Divergence\n\n**无分歧。** 本轮所有交叉回应均为 [AGREE]。\n\n---\n\n## Questions\n\n1. Discussion 中 \"orthogonal contribution\" 是否为有意选择？如果是，请解释为何 closed-loop validation 被认为与本文 claims 的实用价值无关。\n2. 两个 actionable implications（L1 entropy 监控、token pruning）是否有任何初步实验验证（即使是 pilot data）？\n\n---\n\n## Missing References\n\nRound 12 提出的 6 篇缺失引用已全部补齐。仍有 2 条引用可从 arXiv 更新为正式出版版本：\n- belrose2023 (Tuned Lens): arXiv → NeurIPS 2023\n- padalkar2023 (Open X-Embodiment): arXiv → ICRA 2024\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n**状态：未请求。** 本项目未配置外部审稿。\n\n---\n\n## Visual Layout Check\n\n**状态：已完成**（耗时 ~3 分钟）\n\n3 warnings + 9 info items：\n\n**Warnings:**\n1. **Pages 2-4 文字墙**：连续 3 页纯文本（Related Work + Method 开头），无 display item。建议 Section 3 加 pipeline 示意图或方法概览表。\n2. **Page 6 结果段纯文本**：5 组实验结果全用行内数字描述，无图表支撑。建议将 dose-response 或 counterfactual 结果可视化。\n3. **Page 31 末页空白**：附录末页仅 ~7 行文字，~90% 空白。\n\n**Info items（不影响接收）:**\n- Figure 1 子面板部分标签偏小（建议 ≥8pt）\n- Table 1 caption 较长（5 行）\n- Figure 2 灰度打印区分度可能不足（建议加 hatching）\n- Figure 3 色盲友好 ✓\n- Table 2/3 格式规范 ✓\n- 附录 display items 密度高，部分可视化（Figure 9 dose-response、Figure 10 diagnostics）可考虑提升至正文\n- Table 25 信息密度极高\n\n---\n\n## Overall Assessment\n\n**评分: 5/10 — Borderline**\n**置信度: 4/5**\n\n**评分变化: 4/10 (Round 12, Weak Reject) → 5/10 (Round 13, Borderline)，上调 1 分**\n\n### 上调理由\n\n1. **因果语言全面修正**（+0.5）：Routes→Reorganizes + routing→redistributes 消除了 Round 12 最突出的 methodological criticism。执行彻底，零残留。\n2. **Finding 3 降格 + 跨架构限定**（+0.25）：论文 claims 与 evidence 的匹配度显著提升。\"Confirms expected\" + \"causal-decoder VLAs\" 的诚实限定增强了学术可信度。\n3. **呈现性全面改善**（+0.25）：Abstract 精简、Teaser figure、引用补齐、Related Work 区分、技术细节完善。Clarity 从 7/10 提升至 8/10。\n\n### 未达 6/10 (Weak Accept) 的原因\n\n1. **纯 open-loop 分析是结构性缺陷**：论文无法回答 \"这些 attention patterns 对机器人实际执行有什么影响？\" 同期工作（Häon: zero-shot behavioral steering + 真实机器人验证; Grant: Action Atlas 工具）已设定了更高的 actionability 标准。\n2. **Actionable implications 未经验证**：L1 entropy 监控和 token pruning 仍为推测性建议。\"Representational analysis has independent design value\" 的论证力度对 CoRL 审稿人可能不足。\n3. **CoRL scope fit 取决于 AC 判断**：如果 committee 认为 VLA 解释性分析本身对 CoRL 有价值（类似同期 open-loop 分析工作），论文的 methodological rigor 和 revision quality 足以支持 borderline accept。如果要求 closed-loop evidence，则仍在 reject 边界。\n\n### Reviewer 评分\n\n| Reviewer | Round 12 | Round 13 | 变化 |\n|----------|----------|----------|------|\n| R1 (方法/实验) | 3.0/5 | 3.5/5 (Borderline Accept) | +0.5 |\n| R2 (呈现/格式) | 4/10 | 5/10 (Borderline) | +1 |\n\n### 修改质量评价\n\n本轮修改质量 **优秀**。作者认真回应了几乎所有 Round 12 issues，执行彻底且一致性极高。12 个 Round 12 issues 中 10 个 fully resolved，2 个 partially resolved（arXiv 引用残留、术语映射）。核心 framing 问题（overclaiming、Finding 3、cross-architecture）的修正尤其出色。唯一新增的 warning 级问题是 \"orthogonal contribution\" 措辞。\n\n残留问题集中在两个结构性限制上（open-loop + CoRL scope），这些无法通过 writing 修复，需要在 rebuttal 中正面应对。\n\n---\n\n## Detailed Comments\n\n### Section 1: Introduction\n- ✅ 不再复制 Abstract 数字，增加方法论细节和对比定位\n- ✅ 引用 wang2025seeing, pei2025rethinking 支持 causal mask 讨论\n- ✅ Contribution (iii) 明确定位 Finding 3 为 \"methodology validation\"\n\n### Section 2: Related Work\n- ✅ 新增 Grant/Häon 显式对比段落（what-vs-where 区分清晰）\n- ✅ 7 篇新引用正确放置在对应段落\n- ✅ AVA-VLA, causal mask analysis 文献覆盖到位\n\n### Section 3: Method\n- ✅ L1-L32 层编号统一，定义明确\n- ⚠️ L32 post-LN 定义轻微歧义（info 级别）\n\n### Section 4: Experiments\n- ✅ \"Redistributes\" 贯穿全文，零 \"routing\" 残留\n- ✅ Cohen's d 双级报告（token-level 0.65 + trajectory-level 2.943）\n- ✅ FDR: BH, α=0.05, 33-layer family per metric\n- ✅ Cross-architecture claims 全部加 \"causal-decoder\" 限定\n- ⚠️ Page 6 仍为纯文本结果页（视觉审查 warning）\n\n### Section 5: Discussion\n- ✅ \"Redistributes instruction attention\" 为核心总结\n- ✅ Limitations 覆盖：2 架构、LIBERO only、causal-decoder 限制、flow-matching 不适用\n- ⚠️ \"Orthogonal contribution\" 措辞需修改\n- ⚠️ Limitations 使用 \\paragraph 而非 \\subsection（技术上合规）\n\n### Abstract\n- ✅ 从 15+ 定量值精简到 ~1 个\n- ✅ Finding 3 标注为 \"expected\" + \"sanity check\"\n- ✅ \"Two causal-decoder VLA architectures\" 限定\n\n### Title\n- ✅ \"Routes\" → \"Reorganizes\"，避免因果 overclaim\n- ℹ️ \"Language Reorganizes\" 中 Language 作为语法主语是修辞性 convention\n\n### References\n- ✅ 3/3 被要求更新的已完成（kim2024→CoRL, karamcheti2024→ICML, haon2025→CoRL）\n- ⚠️ 2 条可更新残留（belrose2023→NeurIPS 2023, padalkar2023→ICRA 2024）\n\n### Appendix\n- ℹ️ \"Robust attractor\" 措辞较主文更强（N=2 偏强）\n- ℹ️ Page 31 末页 ~90% 空白",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "borderline",
    "review_chat_id": "oc_554a5023cde4d603635cf97e6ab8151a"
  }
}
```

</details>

---


### Tool result

_source line 986 · 2026-05-20T16:21:18.084142+00:00_

{"result":"{\"success\": false, \"data\": {\"expected_reviewer_ids\": [1, 2, 3], \"missing\": [3]}, \"error\": \"consolidated report is incomplete — reviewer(s) [3] were NOT acknowledged. This project has 3 reviewer(s): [1, 2, 3]. Each reviewer's findings (Must-Fix / Should-Fix / score) must be folded into the report. Re-read the missed reviewer's submission via feishu_read_chat_history or the session log, then call this tool again with reviewer_ids_acknowledged covering all 3 reviewers.\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 987 · 2026-05-20T16:22:31.703230+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "project": "vla-ssd",
  "report": "# Round 13 审稿报告（Continue Review）\n\n**论文**: \"Vision Encodes, Language Reorganizes: Token-Level Representational Analysis of VLA Fine-Tuning\"\n**Venue**: CoRL 2026（截止 2026-05-29）\n**审稿模式**: 继续审稿（基于 Round 12 修改验证）\n**Reviewer 编排**: 2 人（R1: 方法/实验/因果 framing; R2: 呈现/格式/引用）。Round 12 的 R3 未参与本轮——Continue 模式下仅需 2 人做增量验证。\n**轮次**: 1 轮独立审稿 + 交叉分享，首轮即达成完全共识\n\n---\n\n## Summary\n\n本轮为 Round 12（Weak Reject, 4/10）之后的修改验证审稿。作者对 Round 12 提出的 6 个 critical issues 和 8 个 warning issues 进行了全面回应。修改涉及：标题重写（Routes→Reorganizes）、因果语言全文替换（routing→redistributes）、Finding 3 降格为 sanity check、跨架构 claim 限定为 causal-decoder、Abstract 精简（15+ 数值→~1）、新增 page 1 teaser figure、补齐 7 篇缺失引用、FDR 细节完善、层编号修正、页面压缩至 8 页内。修改质量高、覆盖面广、执行彻底。\n\n---\n\n## Strengths\n\n1. **因果语言修正彻底**：全文 grep 零残留 \"routing\"。Title→\"Reorganizes\"，正文全部使用 \"redistributes\"。三级证据分类（interventional / supporting / constraining）在新框架下更恰当。这是本轮最重要的改善。\n\n2. **Finding 3 降格处理精准**：Abstract \"confirms expected\" + \"consistent with the causal attention mask\" + \"framework sanity check\" 三重标注。Contribution (iii) 定位为 \"methodology validation\"。既不过度削弱（sanity check 仍有方法论价值），也不残留 overclaiming。\n\n3. **跨架构限定一致无遗漏**：所有 7+ 处 cross-architecture claim 均加上 \"causal-decoder\" 或 \"the two architectures studied\" 限定。Limitations 明确指出 flow-matching/diffusion 架构不适用。推测性预测已移除。\n\n4. **Abstract 精简效果显著**：从 15+ 定量值压缩到 ~1 个，三个 findings 以 First/Second/Third 结构呈现。Introduction 不再复制 Abstract 数字。可读性大幅提升。\n\n5. **Teaser Figure 有效**：page 1 的 Figure 1（architecture overview + attention redistribution 对比图）为读者提供了即时的视觉理解入口。Caption 自包含，尺寸合理。\n\n6. **缺失引用全部补齐**：6/6 被要求的引用 + 1 篇额外添加（pei2025rethinking），引用总数 52→59。Related Work 新增 Grant/Häon 显式对比段落（what-vs-where 区分清晰）。\n\n7. **技术修复完成**：层编号 L1-L32 修正、Cohen's d 双级报告（token-level + trajectory-level d=2.943）、FDR 完整规范（BH, α=0.05, 33-layer family per metric）。\n\n8. **修改一致性极高**：从 Title 到 Conclusion，\"redistributes instruction attention\" 贯穿始终。无残留不一致。\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**W1 [critical, structural] 纯 open-loop 分析，无 behavioral validation（R9-N2 + R9-W1）**\n\n论文所有分析均为 open-loop representational analysis，未提供任何 closed-loop 机器人评估。Discussion 提出两个 actionable implications——(a) L1 attention entropy 监控 fine-tuning 质量，(b) token pruning strategy——但均未经实验验证。\n\n修改后 Discussion 使用 \"orthogonal contribution\" 描述 closed-loop validation，暗示其与本文 claims 无关。实际上，closed-loop validation 是验证本文 claims 实用价值的 **必要** 步骤，不是 orthogonal 的。R2 补充关键对比：Häon et al. 不仅做了 mechanistic analysis，还展示了基于发现的 zero-shot behavioral steering（LIBERO + UR5 真实机器人验证）；Grant et al. 生成了 Action Atlas 工具。本文的两个 implications 均无类似验证。因此，\"与同期工作标准一致\" 的论证在严格比较下不完全成立。\n\n这是 **结构性缺陷**，无法通过 writing 修复。最终判断取决于 CoRL AC 对纯分析性工作的接受阈值。\n\n### Should-Fix（camera-ready 前修复）\n\n**W2 [warning] \"orthogonal contribution\" 措辞 dismissive（R13-W1, NEW）**\n\nDiscussion 中 \"Closed-loop validation on downstream task success is an orthogonal contribution\" 的措辞过于 dismissive。建议改为 \"a complementary and necessary next step\" 或 \"an essential validation step that we leave for future work\"。R1 提出，R2 强烈 AGREE。\n\n**W3 [warning] 2 条 arXiv 引用仍可更新（R12-W3 残留）**\n\nbelrose2023（Tuned Lens）仍为 arXiv，已发表于 NeurIPS 2023。padalkar2023（Open X-Embodiment）仍为 arXiv，已发表于 ICRA 2024。低优先级。\n\n### Nice-to-Have\n\n**W4 [info] L32 定义轻微歧义**：\"with L32 including the final layer norm\" 可更明确为 \"L32 denotes the output after the final RMSNorm applied to the 32nd transformer layer\"。\n\n**W5 [info] Table 1 术语映射**：caption 中建议加 \"(last_preaction = readout token)\" 以明确代码标签与叙事术语的对应。\n\n**W6 [info] Limitations 格式**：当前使用 \\paragraph{Limitations and scope.}，建议改为 \\subsection*{Limitations} 以更明确满足 CoRL 要求。\n\n**W7 [info] 附录 \"robust attractor\" 措辞偏强**：附录中 \"robust attractor of VLA training\" 从 N=2 架构得出偏强。建议改为 \"consistent convergence pattern\"。\n\n**W8 [info] Spacing 压缩处于边界**：\\textfloatsep=6pt（默认~20pt），合规但激进。如有余量建议恢复至 8-10pt。\n\n---\n\n## Reviewer Consensus\n\n所有交叉回应均为 [AGREE]，零 [REBUT]。以下为完全共识项：\n\n| Issue | 判定 | 共识强度 |\n|-------|------|---------|\n| R12-N1 因果 overclaiming | **RESOLVED** | 强（R1+R2 一致） |\n| R4-N1 Finding 3 overclaiming | **RESOLVED** | 强（R1+R2 一致） |\n| R9-N1 跨架构泛化 claim | **RESOLVED**（claim 层面） | 强 |\n| R12-N2 页面超限 | **RESOLVED** | 强 |\n| R12-N3 信息过载 | **RESOLVED** | 强 |\n| R12-W1 Teaser figure | **RESOLVED** | 强 |\n| R12-W2 层编号 | **RESOLVED** | 强 |\n| R12-W4 缺失引用 | **RESOLVED** | 强 |\n| R12-W5 Grant/Häon 区分 | **RESOLVED** | 强 |\n| R12-W6 FDR 细节 | **RESOLVED** | 强 |\n| R9-W4 Cohen's d | **RESOLVED** | 强 |\n| R12-DIV1 Title 误导 | **RESOLVED** | 强 |\n| R9-N2 closed-loop | **PARTIALLY_RESOLVED** | 强（\"orthogonal\" dismissive） |\n| R9-W1 CoRL scope | **PARTIALLY_RESOLVED** | 强（writing 改善，structural 不变） |\n| R12-W3 arXiv 引用 | **PARTIALLY_RESOLVED** | 强（2 条残留） |\n| R13-W1 \"orthogonal\" 措辞 | **NEW warning** | 强 |\n\n---\n\n## Reviewer Divergence\n\n**无分歧。** 本轮所有交叉回应均为 [AGREE]。\n\n---\n\n## Questions\n\n1. Discussion 中 \"orthogonal contribution\" 是否为有意选择？如果是，请解释为何 closed-loop validation 被认为与本文 claims 的实用价值无关。\n2. 两个 actionable implications（L1 entropy 监控、token pruning）是否有任何初步实验验证（即使是 pilot data）？\n\n---\n\n## Missing References\n\nRound 12 提出的 6 篇缺失引用已全部补齐。仍有 2 条引用可从 arXiv 更新为正式出版版本：\n- belrose2023 (Tuned Lens): arXiv → NeurIPS 2023\n- padalkar2023 (Open X-Embodiment): arXiv → ICRA 2024\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n**状态：未请求。** 本项目未配置外部审稿。\n\n---\n\n## Visual Layout Check\n\n**状态：已完成**（耗时 ~3 分钟）\n\n3 warnings + 9 info items：\n\n**Warnings:**\n1. **Pages 2-4 文字墙**：连续 3 页纯文本（Related Work + Method 开头），无 display item。建议 Section 3 加 pipeline 示意图或方法概览表。\n2. **Page 6 结果段纯文本**：5 组实验结果全用行内数字描述，无图表支撑。建议将 dose-response 或 counterfactual 结果可视化。\n3. **Page 31 末页空白**：附录末页仅 ~7 行文字，~90% 空白。\n\n**Info items（不影响接收）:**\n- Figure 1 子面板部分标签偏小（建议 ≥8pt）\n- Table 1 caption 较长（5 行）\n- Figure 2 灰度打印区分度可能不足（建议加 hatching）\n- Figure 3 色盲友好 ✓\n- Table 2/3 格式规范 ✓\n- 附录 display items 密度高，部分可视化（Figure 9 dose-response、Figure 10 diagnostics）可考虑提升至正文\n- Table 25 信息密度极高\n\n---\n\n## Overall Assessment\n\n**评分: 5/10 — Borderline**\n**置信度: 4/5**\n\n**评分变化: 4/10 (Round 12, Weak Reject) → 5/10 (Round 13, Borderline)，上调 1 分**\n\n### 上调理由\n\n1. **因果语言全面修正**（+0.5）：Routes→Reorganizes + routing→redistributes 消除了 Round 12 最突出的 methodological criticism。执行彻底，零残留。\n2. **Finding 3 降格 + 跨架构限定**（+0.25）：论文 claims 与 evidence 的匹配度显著提升。\"Confirms expected\" + \"causal-decoder VLAs\" 的诚实限定增强了学术可信度。\n3. **呈现性全面改善**（+0.25）：Abstract 精简、Teaser figure、引用补齐、Related Work 区分、技术细节完善。Clarity 从 7/10 提升至 8/10。\n\n### 未达 6/10 (Weak Accept) 的原因\n\n1. **纯 open-loop 分析是结构性缺陷**：论文无法回答 \"这些 attention patterns 对机器人实际执行有什么影响？\" 同期工作（Häon: zero-shot behavioral steering + 真实机器人验证; Grant: Action Atlas 工具）已设定了更高的 actionability 标准。\n2. **Actionable implications 未经验证**：L1 entropy 监控和 token pruning 仍为推测性建议。\"Representational analysis has independent design value\" 的论证力度对 CoRL 审稿人可能不足。\n3. **CoRL scope fit 取决于 AC 判断**：如果 committee 认为 VLA 解释性分析本身对 CoRL 有价值（类似同期 open-loop 分析工作），论文的 methodological rigor 和 revision quality 足以支持 borderline accept。如果要求 closed-loop evidence，则仍在 reject 边界。\n\n### Reviewer 评分\n\n| Reviewer | Round 12 | Round 13 | 变化 |\n|----------|----------|----------|------|\n| R1 (方法/实验) | 3.0/5 | 3.5/5 (Borderline Accept) | +0.5 |\n| R2 (呈现/格式) | 4/10 | 5/10 (Borderline) | +1 |\n| R3 (Round 12 only) | 5/10 | — (未参与 R13) | — |\n\n### 修改质量评价\n\n本轮修改质量 **优秀**。作者认真回应了几乎所有 Round 12 issues，执行彻底且一致性极高。12 个 Round 12 issues 中 10 个 fully resolved，2 个 partially resolved（arXiv 引用残留、术语映射）。核心 framing 问题（overclaiming、Finding 3、cross-architecture）的修正尤其出色。唯一新增的 warning 级问题是 \"orthogonal contribution\" 措辞。\n\n残留问题集中在两个结构性限制上（open-loop + CoRL scope），这些无法通过 writing 修复，需要在 rebuttal 中正面应对。\n\n---\n\n## Detailed Comments\n\n### Section 1: Introduction\n- ✅ 不再复制 Abstract 数字，增加方法论细节和对比定位\n- ✅ 引用 wang2025seeing, pei2025rethinking 支持 causal mask 讨论\n- ✅ Contribution (iii) 明确定位 Finding 3 为 \"methodology validation\"\n\n### Section 2: Related Work\n- ✅ 新增 Grant/Häon 显式对比段落（what-vs-where 区分清晰）\n- ✅ 7 篇新引用正确放置在对应段落\n- ✅ AVA-VLA, causal mask analysis 文献覆盖到位\n\n### Section 3: Method\n- ✅ L1-L32 层编号统一，定义明确\n- ⚠️ L32 post-LN 定义轻微歧义（info 级别）\n\n### Section 4: Experiments\n- ✅ \"Redistributes\" 贯穿全文，零 \"routing\" 残留\n- ✅ Cohen's d 双级报告（token-level 0.65 + trajectory-level 2.943）\n- ✅ FDR: BH, α=0.05, 33-layer family per metric\n- ✅ Cross-architecture claims 全部加 \"causal-decoder\" 限定\n- ⚠️ Page 6 仍为纯文本结果页（视觉审查 warning）\n\n### Section 5: Discussion\n- ✅ \"Redistributes instruction attention\" 为核心总结\n- ✅ Limitations 覆盖：2 架构、LIBERO only、causal-decoder 限制、flow-matching 不适用\n- ⚠️ \"Orthogonal contribution\" 措辞需修改\n- ⚠️ Limitations 使用 \\paragraph 而非 \\subsection（技术上合规）\n\n### Abstract\n- ✅ 从 15+ 定量值精简到 ~1 个\n- ✅ Finding 3 标注为 \"expected\" + \"sanity check\"\n- ✅ \"Two causal-decoder VLA architectures\" 限定\n\n### Title\n- ✅ \"Routes\" → \"Reorganizes\"，避免因果 overclaim\n- ℹ️ \"Language Reorganizes\" 中 Language 作为语法主语是修辞性 convention\n\n### References\n- ✅ 3/3 被要求更新的已完成（kim2024→CoRL, karamcheti2024→ICML, haon2025→CoRL）\n- ⚠️ 2 条可更新残留（belrose2023→NeurIPS 2023, padalkar2023→ICRA 2024）\n\n### Appendix\n- ℹ️ \"Robust attractor\" 措辞较主文更强（N=2 偏强）\n- ℹ️ Page 31 末页 ~90% 空白",
  "reviewer_ids_acknowledged": "[1, 2, 3]",
  "cross_response_reviewer_ids": "[1, 2, 3]",
  "overall_score": "borderline",
  "review_chat_id": "oc_554a5023cde4d603635cf97e6ab8151a"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "project": "vla-ssd",
    "report": "# Round 13 审稿报告（Continue Review）\n\n**论文**: \"Vision Encodes, Language Reorganizes: Token-Level Representational Analysis of VLA Fine-Tuning\"\n**Venue**: CoRL 2026（截止 2026-05-29）\n**审稿模式**: 继续审稿（基于 Round 12 修改验证）\n**Reviewer 编排**: 2 人（R1: 方法/实验/因果 framing; R2: 呈现/格式/引用）。Round 12 的 R3 未参与本轮——Continue 模式下仅需 2 人做增量验证。\n**轮次**: 1 轮独立审稿 + 交叉分享，首轮即达成完全共识\n\n---\n\n## Summary\n\n本轮为 Round 12（Weak Reject, 4/10）之后的修改验证审稿。作者对 Round 12 提出的 6 个 critical issues 和 8 个 warning issues 进行了全面回应。修改涉及：标题重写（Routes→Reorganizes）、因果语言全文替换（routing→redistributes）、Finding 3 降格为 sanity check、跨架构 claim 限定为 causal-decoder、Abstract 精简（15+ 数值→~1）、新增 page 1 teaser figure、补齐 7 篇缺失引用、FDR 细节完善、层编号修正、页面压缩至 8 页内。修改质量高、覆盖面广、执行彻底。\n\n---\n\n## Strengths\n\n1. **因果语言修正彻底**：全文 grep 零残留 \"routing\"。Title→\"Reorganizes\"，正文全部使用 \"redistributes\"。三级证据分类（interventional / supporting / constraining）在新框架下更恰当。这是本轮最重要的改善。\n\n2. **Finding 3 降格处理精准**：Abstract \"confirms expected\" + \"consistent with the causal attention mask\" + \"framework sanity check\" 三重标注。Contribution (iii) 定位为 \"methodology validation\"。既不过度削弱（sanity check 仍有方法论价值），也不残留 overclaiming。\n\n3. **跨架构限定一致无遗漏**：所有 7+ 处 cross-architecture claim 均加上 \"causal-decoder\" 或 \"the two architectures studied\" 限定。Limitations 明确指出 flow-matching/diffusion 架构不适用。推测性预测已移除。\n\n4. **Abstract 精简效果显著**：从 15+ 定量值压缩到 ~1 个，三个 findings 以 First/Second/Third 结构呈现。Introduction 不再复制 Abstract 数字。可读性大幅提升。\n\n5. **Teaser Figure 有效**：page 1 的 Figure 1（architecture overview + attention redistribution 对比图）为读者提供了即时的视觉理解入口。Caption 自包含，尺寸合理。\n\n6. **缺失引用全部补齐**：6/6 被要求的引用 + 1 篇额外添加（pei2025rethinking），引用总数 52→59。Related Work 新增 Grant/Häon 显式对比段落（what-vs-where 区分清晰）。\n\n7. **技术修复完成**：层编号 L1-L32 修正、Cohen's d 双级报告（token-level + trajectory-level d=2.943）、FDR 完整规范（BH, α=0.05, 33-layer family per metric）。\n\n8. **修改一致性极高**：从 Title 到 Conclusion，\"redistributes instruction attention\" 贯穿始终。无残留不一致。\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**W1 [critical, structural] 纯 open-loop 分析，无 behavioral validation（R9-N2 + R9-W1）**\n\n论文所有分析均为 open-loop representational analysis，未提供任何 closed-loop 机器人评估。Discussion 提出两个 actionable implications——(a) L1 attention entropy 监控 fine-tuning 质量，(b) token pruning strategy——但均未经实验验证。\n\n修改后 Discussion 使用 \"orthogonal contribution\" 描述 closed-loop validation，暗示其与本文 claims 无关。实际上，closed-loop validation 是验证本文 claims 实用价值的 **必要** 步骤，不是 orthogonal 的。R2 补充关键对比：Häon et al. 不仅做了 mechanistic analysis，还展示了基于发现的 zero-shot behavioral steering（LIBERO + UR5 真实机器人验证）；Grant et al. 生成了 Action Atlas 工具。本文的两个 implications 均无类似验证。因此，\"与同期工作标准一致\" 的论证在严格比较下不完全成立。\n\n这是 **结构性缺陷**，无法通过 writing 修复。最终判断取决于 CoRL AC 对纯分析性工作的接受阈值。\n\n### Should-Fix（camera-ready 前修复）\n\n**W2 [warning] \"orthogonal contribution\" 措辞 dismissive（R13-W1, NEW）**\n\nDiscussion 中 \"Closed-loop validation on downstream task success is an orthogonal contribution\" 的措辞过于 dismissive。建议改为 \"a complementary and necessary next step\" 或 \"an essential validation step that we leave for future work\"。R1 提出，R2 强烈 AGREE。\n\n**W3 [warning] 2 条 arXiv 引用仍可更新（R12-W3 残留）**\n\nbelrose2023（Tuned Lens）仍为 arXiv，已发表于 NeurIPS 2023。padalkar2023（Open X-Embodiment）仍为 arXiv，已发表于 ICRA 2024。低优先级。\n\n### Nice-to-Have\n\n**W4 [info] L32 定义轻微歧义**：\"with L32 including the final layer norm\" 可更明确为 \"L32 denotes the output after the final RMSNorm applied to the 32nd transformer layer\"。\n\n**W5 [info] Table 1 术语映射**：caption 中建议加 \"(last_preaction = readout token)\" 以明确代码标签与叙事术语的对应。\n\n**W6 [info] Limitations 格式**：当前使用 \\paragraph{Limitations and scope.}，建议改为 \\subsection*{Limitations} 以更明确满足 CoRL 要求。\n\n**W7 [info] 附录 \"robust attractor\" 措辞偏强**：附录中 \"robust attractor of VLA training\" 从 N=2 架构得出偏强。建议改为 \"consistent convergence pattern\"。\n\n**W8 [info] Spacing 压缩处于边界**：\\textfloatsep=6pt（默认~20pt），合规但激进。如有余量建议恢复至 8-10pt。\n\n---\n\n## Reviewer Consensus\n\n所有交叉回应均为 [AGREE]，零 [REBUT]。以下为完全共识项：\n\n| Issue | 判定 | 共识强度 |\n|-------|------|---------|\n| R12-N1 因果 overclaiming | **RESOLVED** | 强（R1+R2 一致） |\n| R4-N1 Finding 3 overclaiming | **RESOLVED** | 强（R1+R2 一致） |\n| R9-N1 跨架构泛化 claim | **RESOLVED**（claim 层面） | 强 |\n| R12-N2 页面超限 | **RESOLVED** | 强 |\n| R12-N3 信息过载 | **RESOLVED** | 强 |\n| R12-W1 Teaser figure | **RESOLVED** | 强 |\n| R12-W2 层编号 | **RESOLVED** | 强 |\n| R12-W4 缺失引用 | **RESOLVED** | 强 |\n| R12-W5 Grant/Häon 区分 | **RESOLVED** | 强 |\n| R12-W6 FDR 细节 | **RESOLVED** | 强 |\n| R9-W4 Cohen's d | **RESOLVED** | 强 |\n| R12-DIV1 Title 误导 | **RESOLVED** | 强 |\n| R9-N2 closed-loop | **PARTIALLY_RESOLVED** | 强（\"orthogonal\" dismissive） |\n| R9-W1 CoRL scope | **PARTIALLY_RESOLVED** | 强（writing 改善，structural 不变） |\n| R12-W3 arXiv 引用 | **PARTIALLY_RESOLVED** | 强（2 条残留） |\n| R13-W1 \"orthogonal\" 措辞 | **NEW warning** | 强 |\n\n---\n\n## Reviewer Divergence\n\n**无分歧。** 本轮所有交叉回应均为 [AGREE]。\n\n---\n\n## Questions\n\n1. Discussion 中 \"orthogonal contribution\" 是否为有意选择？如果是，请解释为何 closed-loop validation 被认为与本文 claims 的实用价值无关。\n2. 两个 actionable implications（L1 entropy 监控、token pruning）是否有任何初步实验验证（即使是 pilot data）？\n\n---\n\n## Missing References\n\nRound 12 提出的 6 篇缺失引用已全部补齐。仍有 2 条引用可从 arXiv 更新为正式出版版本：\n- belrose2023 (Tuned Lens): arXiv → NeurIPS 2023\n- padalkar2023 (Open X-Embodiment): arXiv → ICRA 2024\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n**状态：未请求。** 本项目未配置外部审稿。\n\n---\n\n## Visual Layout Check\n\n**状态：已完成**（耗时 ~3 分钟）\n\n3 warnings + 9 info items：\n\n**Warnings:**\n1. **Pages 2-4 文字墙**：连续 3 页纯文本（Related Work + Method 开头），无 display item。建议 Section 3 加 pipeline 示意图或方法概览表。\n2. **Page 6 结果段纯文本**：5 组实验结果全用行内数字描述，无图表支撑。建议将 dose-response 或 counterfactual 结果可视化。\n3. **Page 31 末页空白**：附录末页仅 ~7 行文字，~90% 空白。\n\n**Info items（不影响接收）:**\n- Figure 1 子面板部分标签偏小（建议 ≥8pt）\n- Table 1 caption 较长（5 行）\n- Figure 2 灰度打印区分度可能不足（建议加 hatching）\n- Figure 3 色盲友好 ✓\n- Table 2/3 格式规范 ✓\n- 附录 display items 密度高，部分可视化（Figure 9 dose-response、Figure 10 diagnostics）可考虑提升至正文\n- Table 25 信息密度极高\n\n---\n\n## Overall Assessment\n\n**评分: 5/10 — Borderline**\n**置信度: 4/5**\n\n**评分变化: 4/10 (Round 12, Weak Reject) → 5/10 (Round 13, Borderline)，上调 1 分**\n\n### 上调理由\n\n1. **因果语言全面修正**（+0.5）：Routes→Reorganizes + routing→redistributes 消除了 Round 12 最突出的 methodological criticism。执行彻底，零残留。\n2. **Finding 3 降格 + 跨架构限定**（+0.25）：论文 claims 与 evidence 的匹配度显著提升。\"Confirms expected\" + \"causal-decoder VLAs\" 的诚实限定增强了学术可信度。\n3. **呈现性全面改善**（+0.25）：Abstract 精简、Teaser figure、引用补齐、Related Work 区分、技术细节完善。Clarity 从 7/10 提升至 8/10。\n\n### 未达 6/10 (Weak Accept) 的原因\n\n1. **纯 open-loop 分析是结构性缺陷**：论文无法回答 \"这些 attention patterns 对机器人实际执行有什么影响？\" 同期工作（Häon: zero-shot behavioral steering + 真实机器人验证; Grant: Action Atlas 工具）已设定了更高的 actionability 标准。\n2. **Actionable implications 未经验证**：L1 entropy 监控和 token pruning 仍为推测性建议。\"Representational analysis has independent design value\" 的论证力度对 CoRL 审稿人可能不足。\n3. **CoRL scope fit 取决于 AC 判断**：如果 committee 认为 VLA 解释性分析本身对 CoRL 有价值（类似同期 open-loop 分析工作），论文的 methodological rigor 和 revision quality 足以支持 borderline accept。如果要求 closed-loop evidence，则仍在 reject 边界。\n\n### Reviewer 评分\n\n| Reviewer | Round 12 | Round 13 | 变化 |\n|----------|----------|----------|------|\n| R1 (方法/实验) | 3.0/5 | 3.5/5 (Borderline Accept) | +0.5 |\n| R2 (呈现/格式) | 4/10 | 5/10 (Borderline) | +1 |\n| R3 (Round 12 only) | 5/10 | — (未参与 R13) | — |\n\n### 修改质量评价\n\n本轮修改质量 **优秀**。作者认真回应了几乎所有 Round 12 issues，执行彻底且一致性极高。12 个 Round 12 issues 中 10 个 fully resolved，2 个 partially resolved（arXiv 引用残留、术语映射）。核心 framing 问题（overclaiming、Finding 3、cross-architecture）的修正尤其出色。唯一新增的 warning 级问题是 \"orthogonal contribution\" 措辞。\n\n残留问题集中在两个结构性限制上（open-loop + CoRL scope），这些无法通过 writing 修复，需要在 rebuttal 中正面应对。\n\n---\n\n## Detailed Comments\n\n### Section 1: Introduction\n- ✅ 不再复制 Abstract 数字，增加方法论细节和对比定位\n- ✅ 引用 wang2025seeing, pei2025rethinking 支持 causal mask 讨论\n- ✅ Contribution (iii) 明确定位 Finding 3 为 \"methodology validation\"\n\n### Section 2: Related Work\n- ✅ 新增 Grant/Häon 显式对比段落（what-vs-where 区分清晰）\n- ✅ 7 篇新引用正确放置在对应段落\n- ✅ AVA-VLA, causal mask analysis 文献覆盖到位\n\n### Section 3: Method\n- ✅ L1-L32 层编号统一，定义明确\n- ⚠️ L32 post-LN 定义轻微歧义（info 级别）\n\n### Section 4: Experiments\n- ✅ \"Redistributes\" 贯穿全文，零 \"routing\" 残留\n- ✅ Cohen's d 双级报告（token-level 0.65 + trajectory-level 2.943）\n- ✅ FDR: BH, α=0.05, 33-layer family per metric\n- ✅ Cross-architecture claims 全部加 \"causal-decoder\" 限定\n- ⚠️ Page 6 仍为纯文本结果页（视觉审查 warning）\n\n### Section 5: Discussion\n- ✅ \"Redistributes instruction attention\" 为核心总结\n- ✅ Limitations 覆盖：2 架构、LIBERO only、causal-decoder 限制、flow-matching 不适用\n- ⚠️ \"Orthogonal contribution\" 措辞需修改\n- ⚠️ Limitations 使用 \\paragraph 而非 \\subsection（技术上合规）\n\n### Abstract\n- ✅ 从 15+ 定量值精简到 ~1 个\n- ✅ Finding 3 标注为 \"expected\" + \"sanity check\"\n- ✅ \"Two causal-decoder VLA architectures\" 限定\n\n### Title\n- ✅ \"Routes\" → \"Reorganizes\"，避免因果 overclaim\n- ℹ️ \"Language Reorganizes\" 中 Language 作为语法主语是修辞性 convention\n\n### References\n- ✅ 3/3 被要求更新的已完成（kim2024→CoRL, karamcheti2024→ICML, haon2025→CoRL）\n- ⚠️ 2 条可更新残留（belrose2023→NeurIPS 2023, padalkar2023→ICRA 2024）\n\n### Appendix\n- ℹ️ \"Robust attractor\" 措辞较主文更强（N=2 偏强）\n- ℹ️ Page 31 末页 ~90% 空白",
    "reviewer_ids_acknowledged": "[1, 2, 3]",
    "cross_response_reviewer_ids": "[1, 2, 3]",
    "overall_score": "borderline",
    "review_chat_id": "oc_554a5023cde4d603635cf97e6ab8151a"
  }
}
```

</details>

---


### Tool result

_source line 988 · 2026-05-20T16:22:35.617488+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_a1d032cbe70bdd2058438e67e0d57613:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 3914
}
```

</details>

---


### Assistant

_source line 989 · 2026-05-20T16:22:41.581415+00:00_

Round 13 审稿报告已投递至 Research Director。

**本轮总结**：

- **评分变化**：4/10 (Weak Reject) → **5/10 (Borderline)**，上调 1 分
- **12 个 Round 12 issues**：10 个 fully resolved，2 个 partially resolved
- **新增问题**：1 个 warning（"orthogonal contribution" 措辞）+ 3 个 info
- **Reviewer 共识**：100% [AGREE]，零分歧
- **核心残留**：纯 open-loop + CoRL scope fit 为结构性限制，无法通过 writing 修复，需 rebuttal 应对
- **修改质量**：优秀。执行彻底、一致性极高。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director"
}
```

</details>

---


## Round 99

## Round 99

68 recorded events


### User

_source line 990 · 2026-05-20T16:22:41.585572+00:00_

[Reviewer 2 审稿结果]:
交叉回应已提交。

R1 的 7 个 verdict 中我全部 AGREE，包括 3 个 RESOLVED、2 个 PARTIALLY_RESOLVED、2 个 info-level。对 4 个 New Issues 也全部 AGREE。

关键共识点：
- 因果语言修正和 Finding 3 降格是有效改善
- "orthogonal contribution" 措辞需修改为 "complementary and necessary"
- CoRL scope fit 的核心缺陷（纯 open-loop）无法通过写作修复
- R1 评分 3.5/5，我对应上调至 5/10 (Borderline)

---

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: vla-ssd
- 论文路径: projects/vla-ssd/docs/paper/main.tex
- 目标 venue: CoRL 2026
- 截止日期: 2026-05-29

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 991 · 2026-05-20T16:22:53.371394+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 992 · 2026-05-20T16:22:53.422476+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 993 · 2026-05-20T16:23:00.699616+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,read_project_file,request_external_review,dispatch_visual_check,director_post_to_reviewer,submit_review_report_to_research_director,get_external_review_status,get_visual_check_status,update_review_issues,WebSearch",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_get_project_overview,read_project_file,request_external_review,dispatch_visual_check,director_post_to_reviewer,submit_review_report_to_research_director,get_external_review_status,get_visual_check_status,update_review_issues,WebSearch",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 994 · 2026-05-20T16:23:00.700086+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 995 · 2026-05-20T16:23:04.367096+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,read_project_file,request_external_review,dispatch_visual_check,director_post_to_reviewer,submit_review_report_to_research_director,get_external_review_status,get_visual_check_status,update_review_issues",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_get_project_overview,read_project_file,request_external_review,dispatch_visual_check,director_post_to_reviewer,submit_review_report_to_research_director,get_external_review_status,get_visual_check_status,update_review_issues",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 996 · 2026-05-20T16:23:04.417722+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 997 · 2026-05-20T16:23:08.186967+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__director_post_to_reviewer",
  "max_results": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__director_post_to_reviewer",
    "max_results": "5"
  }
}
```

</details>

---


### Tool result

_source line 998 · 2026-05-20T16:23:08.237625+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 999 · 2026-05-20T16:23:11.148575+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__update_review_issues",
  "max_results": "4"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__update_review_issues",
    "max_results": "4"
  }
}
```

</details>

---


### Tool result

_source line 1000 · 2026-05-20T16:23:11.199240+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1001 · 2026-05-20T16:23:16.556076+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "vla-ssd"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "vla-ssd"
  }
}
```

</details>

---


### Tool result

_source line 1002 · 2026-05-20T16:23:17.459534+00:00_

{"result":"# 项目 vla-ssd 概况\n\n## 实验状态 (117 个)\n\n- **lg_extract_untrained_r2**: DONE (killed) — \n- **lg_extract_trained_r2**: DONE (killed) — \n- **lg_extract_untrained_r1**: DONE (killed) — \n- **lg_extract_trained_r1**: DONE (killed) — \n- **mvp2_delta_dino**: DONE (success) — \n- **mvp2_delta_untrained**: DONE (success) — \n- **mvp2_delta_trained**: DONE (success) — \n- **mvp2_action_dino**: DONE (success) — \n- **mvp2_action_untrained**: DONE (success) — \n- **mvp2_action_trained**: DONE (success) — \n- **mvp_controlb_untrained**: DONE (success) — \n- **mvp_controlb_trained**: DONE (success) — \n- **mvp_001**: DONE (negative) — \n- **mvp_probe_untrained**: DONE (success) — \n- **mvp_probe_trained**: DONE (negative) — \n\n## 最新报告\n# Handover — 2026-05-20\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n- libero_finetuned_probe（准备中）\n- behavioral_smoketest_diag（准备中）\n- behavioral_pilot_v2: Ablating L1 instruction-dominant heads (24/32) during VLA inference on LIBERO-Goal fine-tuned OpenVLA reduces task success rate, providing behavioral evidence that attention head specialization has functional consequences for task execution.（准备中）\n- behavioral_pilot: Ablating L1 instruction-dominant heads during VLA inference will measurably change task success rate, providing behavioral evidence that these heads serve a functional role beyond representational reorganization measured by probes.（准备中）\n- fulllayer_action_probe（准备中）\n- l1_head_ablation_control8（准备中）\n- l1_head_ablation_50demos（准备中）\n\n## 近期结论\n- **phi3v_untrained_seed_expansion** (success): Expanding Phi3V untrained R² probe from 5 to 15 seeds will tighten confidence intervals on the untrained profile (early peak at L4, monotonic decline), aligning statistical power with the other 3 conditions in the 2×2 matrix (all 15 seeds) and eliminating asymmetric seed count as a reviewer concern. ← 基于 phi3v_r2_untrained_probe\n  [phi3v_untrained_15seed_analysis](/api/workspace-files/projects/vla-ssd/artifacts/
…[truncated 1571 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 903
}
```

</details>

---


### Tool call

_source line 1003 · 2026-05-20T16:23:17.961811+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/main.tex",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/main.tex",
    "limit": "100"
  }
}
```

</details>

---


### Tool result

_source line 1004 · 2026-05-20T16:23:18.514471+00:00_

1	\documentclass{article}
2	
3	\usepackage{corl_2026}
4	
5	\usepackage[utf8]{inputenc}
6	\usepackage[T1]{fontenc}
7	\usepackage{url}
8	\usepackage{booktabs}
9	\usepackage{amsfonts}
10	\usepackage{amsmath}
11	\usepackage{nicefrac}
12	\usepackage[expansion=false]{microtype}
13	\usepackage{graphicx}
14	\usepackage{enumitem}
15	
16	\setlength{\textfloatsep}{6pt plus 1pt minus 3pt}
17	\setlength{\intextsep}{6pt plus 1pt minus 1pt}
18	\setlength{\floatsep}{6pt plus 1pt minus 3pt}
19	\setlength{\abovecaptionskip}{2pt}
20	\setlength{\belowcaptionskip}{0pt}
21	\setlength{\abovedisplayskip}{6pt plus 2pt minus 2pt}
22	\setlength{\belowdisplayskip}{6pt plus 2pt minus 2pt}
23	
24	\title{Vision Encodes, Language Reorganizes:\\ Token-Level Representational Analysis of VLA Fine-Tuning}
25	
26	\author{Anonymous}
27	
28	\begin{document}
29	
30	\maketitle
31	
32	\begin{abstract}
33	\input{abstract}
34	\end{abstract}
35	
36	\begin{figure}[t]
37	\centering
38	\includegraphics[width=0.88\linewidth,height=2in,keepaspectratio]{figures/fig_teaser.pdf}
39	\vspace{-4pt}
40	\caption{\textbf{VLA fine-tuning redistributes instruction attention to entry-exit layers.}
41	(a)~Architecture overview.
42	(b)~Instruction-dominant heads per layer (L1 attention $>0.5$). Pretrained Llama-2 peaks at mid-depth; VLA-trained OpenVLA concentrates at L1 and L32. Untrained: zero heads at all layers.}
43	\label{fig:teaser}
44	\end{figure}
45	
46	\input{introduction}
47	\input{related_work}
48	\input{method}
49	\input{experiments}
50	\input{discussion}
51	\input{conclusion}
52	
53	\bibliography{references}
54	
55	\input{appendix}
56	
57	\end{document}
58	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Read",
  "elapsed_ms": 552
}
```

</details>

---


### Tool call

_source line 1005 · 2026-05-20T16:23:18.514838+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "CoRL 2026 call for papers submission deadline author guidelines"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "CoRL 2026 call for papers submission deadline author guidelines"
  }
}
```

</details>

---


### Tool call

_source line 1006 · 2026-05-20T16:23:18.816252+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "vla-ssd",
  "file": "paper_checklist.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "vla-ssd",
    "file": "paper_checklist.yaml"
  }
}
```

</details>

---


### Tool result

_source line 1007 · 2026-05-20T16:23:29.404168+00:00_

Web search results for query: "CoRL 2026 call for papers submission deadline author guidelines"

Links: [{"title":"CoRL 2026 - Instruction for Authors","url":"https://www.corl.org/contributions/instruction-for-authors"},{"title":"CoRL 2026 - Call for Papers","url":"https://www.corl.org/contributions/call-for-papers"},{"title":"CoRL 2026 - Annoucements","url":"https://www.corl.org/annoucements"},{"title":"CoRL 2026 - Call for Workshops","url":"https://www.corl.org/contributions/call-for-workshops"},{"title":"CoRL 2026","url":"https://www.corl.org/"},{"title":"Update CoRL 2026 conference details · huggingface/ai-deadlines at 0ba012a","url":"https://huggingface.co/spaces/huggingface/ai-deadlines/commit/0ba012abbc2f4e96e0072f99fd68649bfc69d9cf"},{"title":"Robot Learning Foundation","url":"https://www.robot-learning.org/"},{"title":"CoRL 2026 Conference | OpenReview","url":"https://openreview.net/group?id=robot-learning.org%2FCoRL%2F2026%2FConference"},{"title":"Refactor conference data · huggingface/ai-deadlines at f3cc2d7","url":"https://huggingface.co/spaces/huggingface/ai-deadlines/commit/f3cc2d74f8283ae00d3005ff7cca51dd26540377"},{"title":"CoRL 2026 - Contributions","url":"https://www.corl.org/contributions"}]

Based on the search results, here's the information about CoRL 2026's call for papers:

## Submission Deadlines

The abstract submission deadline is May 26, 2026 11:59 UTC, and the paper submission deadline is May 29, 2026 11:59 UTC. The deadlines are final, and accommodations cannot be made for missing the abstract deadline or paper deadline.

## Author Guidelines

**Format and Length:**
The page limit is 8 pages for the main paper, with acknowledgments, references, and appendix (optional) not counting toward the page limit.

**Required Sections:**
All submissions should include a Limitations section (counted toward the 8-page limit), explicitly describing limiting assumptions, failure modes, and other limitations of the results and experiments, and how thes
…[truncated 548 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "WebSearch",
  "elapsed_ms": 10889
}
```

</details>

---


### Tool result

_source line 1008 · 2026-05-20T16:23:29.404706+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"No paper_checklist.yaml found for 'vla-ssd'.\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 10588
}
```

</details>

---


### Tool call

_source line 1009 · 2026-05-20T16:23:36.791112+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "CoRL 2026 instruction for authors review criteria double blind anonymity page limit template site:corl.org"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "CoRL 2026 instruction for authors review criteria double blind anonymity page limit template site:corl.org"
  }
}
```

</details>

---


### Tool call

_source line 1010 · 2026-05-20T16:23:37.293250+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "vla-ssd",
  "file": "decisions.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "vla-ssd",
    "file": "decisions.yaml"
  }
}
```

</details>

---


### Tool call

_source line 1011 · 2026-05-20T16:23:37.996918+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/main.tex",
  "offset": "0",
  "limit": "57"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/main.tex",
    "offset": "0",
    "limit": "57"
  }
}
```

</details>

---


### Tool result

_source line 1012 · 2026-05-20T16:23:43.516853+00:00_

Web search results for query: "CoRL 2026 instruction for authors review criteria double blind anonymity page limit template site:corl.org"

Links: [{"title":"CoRL 2026 - Instruction for Authors","url":"https://www.corl.org/contributions/instruction-for-authors"},{"title":"CoRL 2024 - Instruction for Authors","url":"https://2024.corl.org/contributions/instruction-for-authors"},{"title":"CoRL 2026 - Call for Papers","url":"https://www.corl.org/contributions/call-for-papers"},{"title":"CoRL 2021 - Submission Instructions","url":"https://2021.corl.org/author-information/submission-instructions"},{"title":"Effectiveness of Anonymization in Double-Blind Review","url":"https://arxiv.org/pdf/1709.01609"},{"title":"CoRL 2024 - Instruction for Reviews","url":"https://2024.corl.org/contributions/instruction-for-reviews"},{"title":"CoRL 2021 - Frequently Asked Questions","url":"https://2021.corl.org/author-information/frequently-asked-questions"},{"title":"CoRL 2026 - Annoucements","url":"https://www.corl.org/annoucements"}]

Based on the search results from the CoRL 2026 website, here are the key information about the conference submission requirements:

## Double-Blind Anonymity

CoRL is double-blind, which means all papers must be anonymized. The accepted papers and reviews will be publicly accessible and de-anonymized after decisions are announced.

## Page Limit

The camera-ready paper should follow the template: 9-page main text + acknowledgment + references + appendix (optional), and this year, an additional page has been allowed to accommodate feedback from the review process.

## Review Criteria

The aim is to have at least two reviewers per paper.

## Template

The template is available and authors should make sure to use "\usepackage[final]{corl_2026}.

## Submission Platform

Papers may be submitted through OpenReview via the link provided.

The search results provide information about the submission instructions for authors, but do not contain a comprehensive list 
…[truncated 170 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "WebSearch",
  "elapsed_ms": 6725
}
```

</details>

---


### Tool result

_source line 1013 · 2026-05-20T16:23:43.567987+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/decisions.yaml\", \"content\": \"_next_id: 88\\ndecisions:\\n- id: D001\\n  date: 2026-05-15 11:03 UTC\\n  summary: MVP 三分支判定标准校准：ρ下限0.3→0.5, Δρ加bootstrap CI, subtask gate加DINO baseline对比\\n  rationale: Reviewer 审查发现四项校准缺陷：(1) ρ>0.3 下限过低（DINO-V2 已达0.833，0.3只挡彻底失败）→ 提至0.5；(2)\\n    Δρ>0.1 仅为点估计缺统计检验 → 追加 bootstrapped 95% CI must exclude 0；(3) subtask_AUC>0.7\\n    无 baseline 锚点（不知道 DINO-V2 能做到多少）→ 增加条件 subtask_AUC > DINO_subtask_AUC + 0.05；(4)\\n    layer profile 不入正式判定但作为 mandatory supplementary analysis。修改后标准更严谨，降低 false positive\\n    PASS 风险。\\n  related_experiments:\\n  - exp_id: dino-v2-baseline\\n    role: baseline\\n    result: ρ=0.833\\n  depends_on: []\\n- id: D002\\n  date: 2026-05-15 12:02 UTC\\n  summary: MVP 判定全面切换到 per-task mean ρ，弃用 pooled ρ\\n  rationale: Reviewer 指出 pooled ρ 受 cross-task variance 膨胀（DINO pooled=0.833 vs per-task\\n    mean=0.554）。pooled-vs-pooled 虽对称但偏严（可能 false negative）。切换 per-task mean 与 task-level\\n    bootstrap CI 方法论一致，且是更公平的 apples-to-apples 比较。影响：VLA≥DINO gate 从 ρ≥0.833 变为 per-task\\n    mean≥0.554；ρ>0.5 下限同样改为 per-task mean。\\n  related_experiments:\\n  - exp_id: dinov2_baseline\\n    role: baseline\\n    result: pooled ρ=0.833, per-task mean=0.554\\n  depends_on:\\n  - D001\\n- id: D003\\n  date: 2026-05-15 12:31 UTC\\n  summary: 移除 subtask AUC gate，MVP 判定简化为纯 temporal distance (ρ) 路径\\n  rationale: DINO-V2 subtask AUC = 0.9717，Path B 要求 VLA > DINO + 0.05 = 1.0217，数学不可达（AUC\\n    上限 1.0）。根因：subtask 间视觉差异大，任何强视觉编码器都能高 AUC 区分——subtask discrimination 不是 VLA 的差异化能力。Temporal\\n    distance（连续进度信号）才是 VLA 可能独有的编码维度。简化后判定：PASS 需 VLA_ρ ≥ DINO_ρ (0.833)；CONDITIONAL\\n    需 Δρ > 0.1 但 VLA_ρ < DINO_ρ；FAIL 需 ρ ≤ 0.5 或 Δρ ≤ 0.1。Subtask AUC 保留为补充分析，不参与\\n    gate。\\n  related_experiments:\\n  - exp_id: dinov2_baseline\\n    role: trigger\\n    result: subtask AUC 0.9717 使 Path B 数学不可达\\n  depends_on:\\n  - D001\\n- id:
…[truncated 10879 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 6274
}
```

</details>

---


### Tool result

_source line 1014 · 2026-05-20T16:23:43.568508+00:00_

0	\documentclass{article}
1	
2	\usepackage{corl_2026}
3	
4	\usepackage[utf8]{inputenc}
5	\usepackage[T1]{fontenc}
6	\usepackage{url}
7	\usepackage{booktabs}
8	\usepackage{amsfonts}
9	\usepackage{amsmath}
10	\usepackage{nicefrac}
11	\usepackage[expansion=false]{microtype}
12	\usepackage{graphicx}
13	\usepackage{enumitem}
14	
15	\setlength{\textfloatsep}{6pt plus 1pt minus 3pt}
16	\setlength{\intextsep}{6pt plus 1pt minus 1pt}
17	\setlength{\floatsep}{6pt plus 1pt minus 3pt}
18	\setlength{\abovecaptionskip}{2pt}
19	\setlength{\belowcaptionskip}{0pt}
20	\setlength{\abovedisplayskip}{6pt plus 2pt minus 2pt}
21	\setlength{\belowdisplayskip}{6pt plus 2pt minus 2pt}
22	
23	\title{Vision Encodes, Language Reorganizes:\\ Token-Level Representational Analysis of VLA Fine-Tuning}
24	
25	\author{Anonymous}
26	
27	\begin{document}
28	
29	\maketitle
30	
31	\begin{abstract}
32	\input{abstract}
33	\end{abstract}
34	
35	\begin{figure}[t]
36	\centering
37	\includegraphics[width=0.88\linewidth,height=2in,keepaspectratio]{figures/fig_teaser.pdf}
38	\vspace{-4pt}
39	\caption{\textbf{VLA fine-tuning redistributes instruction attention to entry-exit layers.}
40	(a)~Architecture overview.
41	(b)~Instruction-dominant heads per layer (L1 attention $>0.5$). Pretrained Llama-2 peaks at mid-depth; VLA-trained OpenVLA concentrates at L1 and L32. Untrained: zero heads at all layers.}
42	\label{fig:teaser}
43	\end{figure}
44	
45	\input{introduction}
46	\input{related_work}
47	\input{method}
48	\input{experiments}
49	\input{discussion}
50	\input{conclusion}
51	
52	\bibliography{references}
53	
54	\input{appendix}
55	
56	\end{document}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Read",
  "elapsed_ms": 5571
}
```

</details>

---


### Tool call

_source line 1015 · 2026-05-20T16:23:54.859205+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper"
  }
}
```

</details>

---


### Tool result

_source line 1016 · 2026-05-20T16:23:55.311258+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/corl_example.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/method.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/appendix.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/main.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/experiments.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/discussion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/conclusion.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Glob",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 1017 · 2026-05-20T16:23:55.663083+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "vla-ssd",
  "file": "writing_plan.yaml",
  "max_chars": "0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "vla-ssd",
    "file": "writing_plan.yaml",
    "max_chars": "0"
  }
}
```

</details>

---


### Tool result

_source line 1018 · 2026-05-20T16:23:55.714768+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/writing_plan.yaml\", \"content\": \"venue: CoRL 2026\\nabstract_ddl: 2026-05-26\\npaper_ddl: 2026-05-29\\nformat: \\\"8 pages + references\\\"\\n\\ntitle_candidates:\\n  - \\\"Where Do Action Representations Come From? Dissecting Vision-Language-Action Models\\\"\\n  - \\\"Self-Supervised Geometry is King: Representational Analysis of Vision-Language-Action Models\\\"\\n  - \\\"Vision Encodes, Language Routes: A Representational Decomposition of VLA Action Knowledge\\\"\\n\\n# ============================================================\\n# SECTIONS\\n# ============================================================\\nsections:\\n\\n  - name: Abstract\\n    core_evidence:\\n      - d041_method_b_rsa            # DINO cls=0.692 highest, full per-layer curves\\n      - plan_013_branch_split        # DINOv2 branch=0.619, SigLIP branch=0.621\\n      - plan_012_clip_vit_control    # CLIP RSA=0.557, R²=0.587\\n      - unified_action_probe         # R² unified hyperparams\\n      - d041_training_effect_bootstrap  # best-vs-best Δ=+0.017 n.s., same-layer Δ=+0.079\\n    key_numbers:\\n      - \\\"DINO cls RSA=0.692 (highest); Cross-encoder: DINO patch_mean (0.631) > SigLIP+Proj (0.615) > CLIP (0.557). Self-supervised geometry is king.\\\"\\n      - \\\"R²: DINO (0.634) ≈ Proj (0.630) > CLIP (0.587). last_preaction R²=0.671 (readout concentration, p=0.002 vs Proj).\\\"\\n      - \\\"LLM inverted-U: L0=0.612 → L12=0.628 (peak, above projector 0.615) → L32=0.422.\\\"\\n      - \\\"Training peak shift: best-vs-best Δ=+0.017 n.s.; same-layer L12 Δ=+0.079 p<0.0001.\\\"\\n      - \\\"Instruction invariance: max |Δ|=0.006.\\\"\\n\\n  - name: Introduction\\n    structure:\\n      - para_1_problem: >\\n          VLAs achieve impressive manipulation performance by fine-tuning LLMs on robot data.\\n          Implicit assumption: fine-tuning injects action-relevant represe
…[truncated 29966 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 1019 · 2026-05-20T16:24:01.290102+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 1020 · 2026-05-20T16:24:01.742099+00:00_

1	Vision-language-action models (VLAs) fine-tune large language models on robot demonstrations, but what fine-tuning changes at the representational level remains unclear.
2	We decompose two causal-decoder VLAs---OpenVLA-7B and TraceVLA---across all 32 LLM layers using cross-instruction probes, attention analysis, and functional probes, with factorial trained/pretrained/untrained controls on LIBERO.
3	Three findings emerge.
4	First, VLA fine-tuning redistributes instruction attention from mid-depth to entry-exit layers, supported by seven complementary analyses including dose-response and counterfactual ablation.
5	Second, despite dramatically different untrained profiles (OpenVLA peaks at L0 then collapses; Phi-3-V ramps to L6), both architectures reach similar trained mid-layer peaks ($R^2$ $0.637$ vs.\ $0.634$, $\Delta = 0.003$), consistent with convergent reorganization toward a common functional organization; training effects concentrate at the readout token ($+0.069$) rather than image geometry.
6	Third, token-level analysis confirms expected functional specialization---image tokens remain instruction-blind while the readout token integrates multimodal information---consistent with the causal attention mask and serving as a framework sanity check.
7	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Read",
  "elapsed_ms": 451
}
```

</details>

---


### Tool call

_source line 1021 · 2026-05-20T16:24:01.742451+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 1022 · 2026-05-20T16:24:02.144306+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	What does fine-tuning change inside a Vision-Language-Action model (VLA)?
5	VLAs fine-tune large language models on robot demonstrations to produce actions from visual observations and language instructions~\cite{brohan2023_rt2,kim2024_openvla}, but the decoder-only causal mask prevents image tokens from attending to instructions~\cite{wang2025seeing,pei2025rethinking}.
6	Instruction information must reach action-generating positions through learned attention patterns, yet how fine-tuning reshapes these patterns remains uncharacterized.
7	
8	Recent behavioral studies reveal that VLAs rely disproportionately on visual input~\cite{grant2026}, with language instructions largely ignored by the action pathway~\cite{haon2025}.
9	These findings suggest internal specialization but do not explain \emph{how} instruction information reaches the action-generating readout token, \emph{what} attention strategy fine-tuning learns compared to language pretraining alone, or \emph{whether} training creates new representational structure or reconfigures inherited geometry.
10	Existing analyses have not combined systematic per-layer probing with factorial trained/pretrained/untrained controls, leaving the representational mechanisms of VLA fine-tuning opaque.
11	
12	We address this gap by decomposing OpenVLA-7B~\cite{kim2024_openvla,karamcheti2024}, a VLA chaining a frozen DinoSigLIP vision backbone~\cite{zhai2023_siglip,oquab2024_dinov2}, an MLP projector, and Llama-2 7B~\cite{touvron2023_llama2}.
13	We extract representations from each of 32 LLM layers at both image-token and readout-token positions, and from external baselines (DINOv2~\cite{oquab2024_dinov2}, CLIP~\cite{radford2021_clip}).
14	We compare three LLM conditions (VLA-trained, pretrained Llama-2 base, and randomly initialized) crossed with instruction presence, and apply four complementary analyses: cross-instruction probes for token-level specialization, L1 attenti
…[truncated 2016 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Read",
  "elapsed_ms": 401
}
```

</details>

---


### Tool call

_source line 1023 · 2026-05-20T16:24:02.144673+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 1024 · 2026-05-20T16:24:02.546422+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	We investigate how action-relevant structure is distributed across a VLA by combining four complementary analyses: cross-instruction probes, attention pattern analysis, RSA, and functional probes.
5	
6	%------------------------------------------------------------------
7	\subsection{Model and Data}
8	\label{sec:model_data}
9	
10	We study OpenVLA-7B~\cite{kim2024_openvla,karamcheti2024}, chaining a frozen DinoSigLIP vision backbone~\cite{zhai2023_siglip,oquab2024_dinov2} (DINOv2 ViT-L/14 + SigLIP-SO400M), an MLP projector (2{,}176-D $\to$ 4{,}096-D), and Llama-2 7B~\cite{touvron2023_llama2} (6.74B parameters) that autoregressively decodes 7-D actions.
11	We use the base checkpoint pretrained on Open X-Embodiment~\cite{padalkar2023_oxe} (970K episodes spanning multiple robot platforms and task types) and evaluate on LIBERO-Goal~\cite{liu2023_libero} (10 tasks, 50 demonstrations each), which was not part of the pretraining mixture.
12	We compare three LLM conditions: (1)~VLA-trained (released checkpoint), (2)~Llama-2 base (pretrained backbone, no VLA fine-tuning), and (3)~untrained (6.74B parameters reinitialized via \texttt{from\_config()}); a fourth condition (task-specific fine-tuning on LIBERO) is compared in \S\ref{sec:learned_routing}.
13	All three share the same frozen vision encoder and projector.
14	
15	%------------------------------------------------------------------
16	\subsection{Representation Extraction}
17	\label{sec:repr_extraction}
18	
19	We extract representations from six sources spanning the VLA pipeline:
20	(a)~\textbf{DinoSigLIP+Projector}, the projector output (4{,}096-D), immediately before LLM processing;
21	(b)~\textbf{LLM image\_mean}, the mean image-token activation at each of 32 layers;
22	(c)~\textbf{LLM readout}, the hidden state at the final pre-action token position at each layer (located after both image and instruction tokens in the causal sequence, it can attend to all preceding context 
…[truncated 4182 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Read",
  "elapsed_ms": 401
}
```

</details>

---


### Tool call

_source line 1025 · 2026-05-20T16:24:02.546748+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 1026 · 2026-05-20T16:24:02.647502+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Experimental Setup}
5	\label{sec:setup}
6	
7	We evaluate OpenVLA-7B~\cite{kim2024_openvla,karamcheti2024} on LIBERO-Goal~\cite{liu2023_libero} (10 tasks, 50 demonstrations each).
8	Representations are extracted from six sources spanning the VLA pipeline (\S\ref{sec:repr_extraction}): DinoSigLIP+Projector, LLM image\_mean and readout tokens at each of 32 layers, DINOv2~\cite{oquab2024_dinov2} (\texttt{cls\_token}/\texttt{patch\_mean}), CLIP~\cite{radford2021_clip} (\texttt{patch\_mean}), and branch-split (DINOv2 1{,}024-D / SigLIP 1{,}152-D before fusion).
9	Three LLM conditions are compared: VLA-trained, pretrained Llama-2 base (no VLA fine-tuning), and untrained (6.74B parameters reinitialized to random weights), crossed with instruction presence (\S\ref{sec:model_data}).
10	RSA computes Spearman $\rho$ between cosine-distance representation RDMs and Euclidean-distance action RDMs, with 10{,}000 bootstrap CIs (\S\ref{sec:rsa}).
11	MLP probes (input $\to$ 256 $\to$ 7; Adam, lr${}=10^{-3}$, 50 epochs, early stopping) report mean $R^2$ (\S\ref{sec:probes}).
12	This yields $N = 63{,}228$ observations (after excluding terminal frames without next-action labels; $63{,}728$ total); RSA uses task-level blocking ($N_\text{eff} = 10$) and probes use demo-level train/test splits.
13	All patterns reproduce with a linear probe (Appendix~\ref{sec:linear_probe}).
14	
15	%------------------------------------------------------------------
16	\subsection{Framework Validation: Token-Level Specialization}
17	\label{sec:token_specialization}
18	
19	Cross-instruction probes (\S\ref{sec:cross_instruction_probes}) validate the framework (Table~\ref{tab:dense_routing_main}).
20	As predicted by the causal mask, image\_mean instruction classification stays at chance ($10\%$) across all 32 layers in all conditions; linear and MLP probes corroborate this (Appendix~\ref{sec:instruction_invariance_appendix}).
21	Trained readout a
…[truncated 13103 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 1027 · 2026-05-20T16:24:07.616273+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/experiments.tex",
  "offset": "175"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/experiments.tex",
    "offset": "175"
  }
}
```

</details>

---


### Tool result

_source line 1028 · 2026-05-20T16:24:07.917814+00:00_

&lt;system-reminder>Warning: the file exists but is shorter than the provided offset (175). The file has 175 lines.&lt;/system-reminder>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Read",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 1029 · 2026-05-20T16:24:07.918214+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 1030 · 2026-05-20T16:24:08.420286+00:00_

1	\vspace{-2pt}
2	\section{Discussion}
3	\label{sec:discussion}
4	
5	\paragraph{Synthesis.}
6	VLA fine-tuning redistributes instruction attention rather than reshaping visual geometry: training effects concentrate at the readout ($R^2$ $+0.069$, attention $+46$pp) rather than images ($\Delta \leq 1.7\%$), explaining Grant et al.'s~\cite{grant2026} visual dominance finding ($\rho = 0.692$ for DINOv2, yet readout $R^2 = 0.678$ vs.\ $0.634$).
7	Cross-architecture comparison strengthens this picture: two VLAs with different backbones and opposite untrained profiles both arrive at similar mid-layer peaks ($\Delta = 0.003$), suggesting the redistribution reflects task-structure constraints rather than architecture-specific artifacts.
8	Seven analyses support L1 redistribution: \emph{interventional} (dose-response $d = 0.48 \to 0.64$; counterfactual $d = 0.63$--$0.97$), \emph{supporting} (gradient $0 \to 9 \to 24$ heads; ablation $+0.059$; trajectory $d = 0.65$), and \emph{constraining} ($p = 0.0018$; $z = -3.11$, $0$\textsuperscript{th} percentile; Appendix~\ref{sec:mechanistic_interpretation}--\ref{sec:functional_stages}).
9	
10	\paragraph{Limitations and scope.}
11	We analyze two causal-decoder VLAs on held-out LIBERO; while their starting points are maximally different (base LM vs.\ instruction-tuned LM), extending to flow-matching~\cite{black2024_pi0} and diffusion~\cite{ghosh2024_octo} VLAs with cross-attention is needed to test generality beyond the causal-decoder family.
12	Llama-2's 9/32 pretrained instruction heads may reflect text bias ($+15$-head delta isolates fine-tuning).
13	All analyses are open-loop, as in concurrent VLA representation studies~\cite{grant2026,haon2025}; however, representational analysis has independent design value---convergent mid-layer peaks suggest early-exit inference at ${\sim}1/3$ depth as a testable hypothesis, and the entry-exit profile enables L1 entropy monitoring as a fine-tuning diagnostic.
14	Closed-loop validation would stre
…[truncated 114 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 1031 · 2026-05-20T16:24:08.420762+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 1032 · 2026-05-20T16:24:08.972982+00:00_

1	\paragraph{Conclusion.}
2	VLA fine-tuning redistributes instruction attention to entry-exit layers with L1 as the primary hub, supported by seven complementary analyses.
3	Despite opposite untrained profiles, both causal-decoder architectures reach similar trained representations ($\Delta = 0.003$), with effects concentrated at the readout rather than image geometry. Code and data will be released upon acceptance.
4	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Read",
  "elapsed_ms": 552
}
```

</details>

---


### Tool call

_source line 1033 · 2026-05-20T16:24:08.973318+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 1034 · 2026-05-20T16:24:09.023891+00:00_

1	\section{Related Work}\label{sec:related_work}
2	
3	\paragraph{Vision-language-action models.}
4	VLAs fine-tune large language models on robot demonstrations to produce action tokens conditioned on visual observations and language instructions~\cite{brohan2023_rt2,kim2024_openvla,karamcheti2024,black2024_pi0}; recent work conditions action generation on dynamic visual reweighting~\cite{xiao2025ava}.
5	This architecture family inherits the transformer backbone and its multi-modal fusion mechanisms from vision-language models, but repurposes them for continuous control.
6	A central assumption is that fine-tuning injects action-relevant knowledge into pretrained representations; unlike NLP instruction tuning, which targets behavioral compliance~\cite{wei2022finetuned,ouyang2022training}, we test this at the representational level through per-layer, per-token-type decomposition.
7	
8	\paragraph{Mechanistic interpretability in transformers.}
9	Mechanistic analyses have identified residual stream communication~\cite{elhage2021}, induction heads for in-context learning~\cite{olsson2022}, complete circuits for specific tasks~\cite{wang2023_ioi,conmy2023}, causal tracing for factual recall~\cite{meng2022_rome}, and the tuned lens for per-layer prediction~\cite{belrose2023_tunedlens}, while feature-level methods have scaled to dictionary learning over millions of features~\cite{bills2023language,templeton2024scaling}.
10	Attention probing reveals that individual heads encode syntactic relations~\cite{clark2019}, capture depth-dependent patterns~\cite{vig2019}, and that a small subset accounts for most performance~\cite{voita2019}; Michel et al.~\cite{michel2019sixteen} showed most heads can be pruned without loss.
11	Our L1 analysis extends this to VLAs: we use functional ablation to study attention redistribution and find that 24 of 32 heads become instruction-dominant after fine-tuning, with progressive ablation yielding monotonic rather than threshold-like effects.
12	
1
…[truncated 2951 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1035 · 2026-05-20T16:24:12.813718+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 1036 · 2026-05-20T16:24:13.065897+00:00_

1	\paragraph{Use of Generative AI.}
2	Generative AI tools (Claude, GPT-4) assisted with code implementation and manuscript editing; all scientific content was produced by the authors.
3	
4	\appendix
5	
6	\section{Supplementary Material}
7	\label{sec:appendix}
8	
9	Unless noted otherwise, all analyses use OpenVLA-7B (\texttt{openvla/openvla-7b} on HuggingFace) evaluated on LIBERO-Goal (10 tasks $\times$ 50 demonstrations, $N = 63{,}228$ observations after excluding terminal frames).
10	Model conditions, representation extraction, metric definitions, and probe architectures follow \S\ref{sec:setup}--\S\ref{sec:probes}.
11	Cross-benchmark experiments (\S\ref{sec:cross_benchmark_appendix}) use LIBERO-Spatial with the same protocol (10 tasks $\times$ 50 demonstrations).
12	All experiments ran on 2$\times$ NVIDIA RTX PRO 6000 Blackwell Server Edition GPUs (96\,GB each); random seed is 42 unless stated otherwise.
13	
14	\subsection{CKA Analysis Method}
15	\label{sec:cka_appendix}
16	
17	We employ Centered Kernel Alignment (CKA)~\cite{kornblith2019} alongside RSA as a complementary perspective.
18	While RSA captures local geometric alignment via rank-order preservation, CKA measures global representational similarity through kernel-based comparisons.
19	
20	We compute both \emph{linear CKA}, which uses a linear kernel and is sensitive to second-order statistics, and \emph{RDM kernel CKA}, which operates on the same distance matrices as RSA but aggregates them differently.
21	Using both variants tests whether conclusions about representation structure are robust to the choice of similarity metric.
22	
23	Linear CKA between high-dimensional representations (4{,}096-D for LLM layers) and the 7-D action space is subject to a known dimension mismatch: the linear kernel in the low-dimensional space may not capture the same structure as in the high-dimensional space.
24	RDM kernel CKA avoids this issue by operating on distance matrices of equal size regardless of the original feat
…[truncated 58629 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Read",
  "elapsed_ms": 252
}
```

</details>

---


### Tool call

_source line 1037 · 2026-05-20T16:24:13.116494+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/references.bib",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/references.bib",
    "limit": "100"
  }
}
```

</details>

---


### Tool result

_source line 1038 · 2026-05-20T16:24:13.167180+00:00_

1	% === VLA / Architecture ===
2	
3	@article{zheng2024tracevla,
4	  title     = {{TraceVLA}: Visual Trace Prompting Enhances Spatial-Temporal Awareness for Generalist Robotic Policies},
5	  author    = {Zheng, Ruijie and Liang, Yongyuan and Huang, Shuaiyi and Gao, Jianfeng and Daum{\'e} III, Hal and Kolobov, Andrey and Huang, Furong and Yang, Jianwei},
6	  journal   = {arXiv preprint arXiv:2412.10345},
7	  year      = {2024},
8	}
9	
10	@article{abdin2024phi3,
11	  title     = {Phi-3 Technical Report: A Highly Capable Language Model Locally on Your Phone},
12	  author    = {Abdin, Marah and Jacobs, Sam Ade and Amin, Ammar Ahmad and Aneja, Jyoti and Awadalla, Ahmed and Awadalla, Hany and Bach, Nguyen and Bahree, Amit and Bakber, Arash and Beez, Harkirat and others},
13	  journal   = {arXiv preprint arXiv:2404.14219},
14	  year      = {2024},
15	}
16	
17	@inproceedings{kim2024_openvla,
18	  title     = {{OpenVLA}: An Open-Source Vision-Language-Action Model},
19	  author    = {Kim, Moo Jin and Pertsch, Karl and Karamcheti, Siddharth and Xiao, Ted and Balakrishna, Ashwin and Nair, Suraj and Rafailov, Rafael and Foster, Ethan and Lam, Grace and Sanketi, Pannag and Lu, Quan and Kollar, Thomas and Burchfiel, Benjamin and Tedrake, Russ and Sadigh, Dorsa and Levine, Sergey and Liang, Percy and Finn, Chelsea},
20	  booktitle = {Proceedings of the 8th Conference on Robot Learning (CoRL)},
21	  series    = {PMLR},
22	  volume    = {270},
23	  pages     = {2679--2713},
24	  year      = {2024},
25	}
26	
27	@inproceedings{karamcheti2024,
28	  title     = {Prismatic {VLMs}: Investigating the Design Space of Visually-Conditioned Language Models},
29	  author    = {Karamcheti, Siddharth and Nair, Suraj and Balakrishna, Ashwin and Liang, Percy and Kollar, Thomas and Sadigh, Dorsa},
30	  booktitle = {Proceedings of the 41st International Conference on Machine Learning (ICML)},
31	  series    = {PMLR},
32	  volume    = {235},
33	  pages     = {23123--23144},
34	  year      = {2024},
35	
…[truncated 3091 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1039 · 2026-05-20T16:24:17.935456+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/references.bib",
  "offset": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/references.bib",
    "offset": "100"
  }
}
```

</details>

---


### Tool result

_source line 1040 · 2026-05-20T16:24:18.237180+00:00_

100	}
101	
102	% === Domain-Specific ===
103	
104	@article{grant2026,
105	  title     = {Not All Features Are Created Equal: A Mechanistic Study of Vision-Language-Action Models},
106	  author    = {Grant, Bryce and Zhao, Xijia and Wang, Peng},
107	  journal   = {arXiv preprint arXiv:2603.19233},
108	  year      = {2026},
109	}
110	
111	@inproceedings{haon2025,
112	  title     = {Mechanistic Interpretability for Steering Vision-Language-Action Models},
113	  author    = {H{\"a}on, Bear and Stocking, Kaylene C. and Chuang, Ian and Tomlin, Claire J.},
114	  booktitle = {Proceedings of the 9th Conference on Robot Learning (CoRL)},
115	  series    = {PMLR},
116	  volume    = {305},
117	  pages     = {2743--2762},
118	  year      = {2025},
119	}
120	
121	% === Behavioral Analysis of VLAs ===
122	
123	@article{hou2026,
124	  title     = {{LangGap}: Diagnosing and Closing the Language Gap in Vision-Language-Action Models},
125	  author    = {Hou, Yuchen and Zhao, Lin},
126	  journal   = {arXiv preprint arXiv:2603.00592},
127	  year      = {2026},
128	}
129	
130	@article{fei2025,
131	  title     = {{LIBERO-Plus}: In-depth Robustness Analysis of Vision-Language-Action Models},
132	  author    = {Fei, Senyu and Wang, Siyin and Shi, Junhao and Dai, Zihao and Cai, Jikun and Qian, Pengfang and Ji, Li and He, Xinzhe and Zhang, Shiduo and Fei, Zhaoye and Fu, Jinlan and Gong, Jingjing and Qiu, Xipeng},
133	  journal   = {arXiv preprint arXiv:2510.13626},
134	  year      = {2025},
135	}
136	
137	% === Mechanistic Interpretability of VLAs ===
138	
139	@article{swann2026,
140	  title     = {Sparse Autoencoders Reveal Interpretable and Steerable Features in {VLA} Models},
141	  author    = {Swann, Aiden and McGranahan, Lachlain and Buurmeijer, Hugo and Kennedy, Monroe and Schwager, Mac},
142	  journal   = {arXiv preprint arXiv:2603.19183},
143	  year      = {2026},
144	}
145	
146	@article{buurmeijer2026,
147	  title     = {Observing and Controlling Features in Vision-Language-Action Mo
…[truncated 17279 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Read",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 1041 · 2026-05-20T16:24:18.438459+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "wc -l /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/references.bib",
  "description": "Count lines in references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Bash",
  "tool_args": {
    "command": "wc -l /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/references.bib",
    "description": "Count lines in references.bib"
  }
}
```

</details>

---


### Tool result

_source line 1042 · 2026-05-20T16:24:18.590663+00:00_

496 /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/references.bib

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Bash",
  "elapsed_ms": 152
}
```

</details>

---


### Tool call

_source line 1043 · 2026-05-20T16:24:24.514113+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/main.pdf 2>/dev/null && echo \"PDF_EXISTS\" || echo \"NO_PDF\"",
  "description": "Check if PDF exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/main.pdf 2>/dev/null && echo \"PDF_EXISTS\" || echo \"NO_PDF\"",
    "description": "Check if PDF exists"
  }
}
```

</details>

---


### Tool result

_source line 1044 · 2026-05-20T16:24:25.017151+00:00_

-rw-r--r-- 1 ubuntu ubuntu 651685 May 20 16:13 /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/main.pdf
PDF_EXISTS

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Bash",
  "elapsed_ms": 503
}
```

</details>

---


### Tool call

_source line 1045 · 2026-05-20T16:24:25.771121+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/agent/config.yaml 2>/dev/null || echo \"NO_CONFIG\"",
  "description": "Read project config for external review settings"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/agent/config.yaml 2>/dev/null || echo \"NO_CONFIG\"",
    "description": "Read project config for external review settings"
  }
}
```

</details>

---


### Tool result

_source line 1046 · 2026-05-20T16:24:26.024071+00:00_

NO_CONFIG

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Bash",
  "elapsed_ms": 252
}
```

</details>

---


### Tool call

_source line 1047 · 2026-05-20T16:24:26.426018+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/review_issues.yaml 2>/dev/null || echo \"NO_ISSUES_FILE\"",
  "description": "Check existing review issues tracker"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/review_issues.yaml 2>/dev/null || echo \"NO_ISSUES_FILE\"",
    "description": "Check existing review issues tracker"
  }
}
```

</details>

---


### Tool result

_source line 1048 · 2026-05-20T16:24:26.628165+00:00_

issues:
  # ============================================================
  # Round 1-8 历史 issues（全部 resolved，压缩保留）
  # ============================================================
  - id: R1-N1-old
    summary: "Untrained baseline 无法隔离 VLA fine-tuning vs Llama-2 语言预训练的贡献"
    category: experiment
    severity: critical
    status: resolved
    first_raised_round: 1
    last_seen_round: 2
    resolution: "三条件数据完整整合。"
    resolution_round: 3
    mentions: []
    action_items: []
  - id: R1-N2-old
    summary: "单一模型 Title/Abstract 使用复数 'VLAs' 构成 overclaim"
    category: framing
    severity: critical
    status: resolved
    first_raised_round: 1
    last_seen_round: 2
    resolution: "Title 改为单数。"
    resolution_round: 3
    mentions: []
    action_items: []
  - id: R1-N4-old
    summary: "Design implications 完全基于 correlational evidence"
    category: framing
    severity: critical
    status: resolved
    first_raised_round: 1
    last_seen_round: 2
    resolution: "Abstract 使用 hedge 语气。"
    resolution_round: 3
    mentions: []
    action_items: []
  - id: R1-N3-old
    summary: "RSA best-vs-best selection bias"
    category: experiment
    severity: warning
    status: resolved
    first_raised_round: 1
    last_seen_round: 2
    resolution: "Same-layer comparison 为 primary evidence。"
    resolution_round: 3
    mentions: []
    action_items: []
  - id: R2-N1-old
    summary: "Neo et al. (ICLR 2025) 未引用"
    category: framing
    severity: warning
    status: resolved
    first_raised_round: 1
    last_seen_round: 2
    resolution: "已引用。"
    resolution_round: 3
    mentions: []
    action_items: []
  - id: R2-W1-old
    summary: "Related Work 引用覆盖度不足"
    category: writing
    severity: warning
    status: resolved
    first_raised_round: 1
    last_seen_round: 2
    resolution: "引用数量达标。"
    resolution_round: 3
    mentions: []
    action_items: []
  - id: R1-W1-old
    summary: "'Instruction-blind' claim 过强"
    category: framing
    severity: warning
    status
…[truncated 24190 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Bash",
  "elapsed_ms": 202
}
```

</details>

---


### Tool call

_source line 1049 · 2026-05-20T16:25:03.515550+00:00_

called mcp__agent-ml-research__request_external_review

<details open><summary>🔧 Tool call — mcp__agent-ml-research__request_external_review</summary>

```json
{
  "project": "vla-ssd",
  "paper_pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/main.pdf",
  "venue": "CoRL 2026",
  "note": "Target venue: CoRL 2026. Paper deadline: 2026-05-29. Double-blind. 论文分析 VLA fine-tuning 的表征层面变化。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "mcp__agent-ml-research__request_external_review",
  "tool_args": {
    "project": "vla-ssd",
    "paper_pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/main.pdf",
    "venue": "CoRL 2026",
    "note": "Target venue: CoRL 2026. Paper deadline: 2026-05-29. Double-blind. 论文分析 VLA fine-tuning 的表征层面变化。"
  }
}
```

</details>

---


### Tool call

_source line 1050 · 2026-05-20T16:25:05.473499+00:00_

called mcp__agent-ml-research__dispatch_visual_check

<details open><summary>🔧 Tool call — mcp__agent-ml-research__dispatch_visual_check</summary>

```json
{
  "project": "vla-ssd",
  "review_chat_id": "oc_554a5023cde4d603635cf97e6ab8151a"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "tool_args": {
    "project": "vla-ssd",
    "review_chat_id": "oc_554a5023cde4d603635cf97e6ab8151a"
  }
}
```

</details>

---


### Tool result

_source line 1051 · 2026-05-20T16:25:19.617870+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"pending\", \"message\": \"外部审稿请求已发送到用户群。将在 8 小时后自动提醒。\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "mcp__agent-ml-research__request_external_review",
  "elapsed_ms": 16102
}
```

</details>

---


### Tool result

_source line 1052 · 2026-05-20T16:25:19.618276+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 14144
}
```

</details>

---


### Tool call

_source line 1053 · 2026-05-20T16:25:20.622278+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "你是 Reviewer 1，负责 **方法严谨性 + 实验有效性 + 统计方法论** 审查。\n\n## 论文信息\n- **标题**: Vision Encodes, Language Reorganizes: Token-Level Representational Analysis of VLA Fine-Tuning\n- **目标 Venue**: CoRL 2026\n- **Deadline**: 2026-05-29\n- **格式**: CoRL 2026 模板，double-blind，正文 8 页 + references + appendix（不计入页数）\n- **匿名规则**: Double-blind\n- **论文路径**: projects/vla-ssd/docs/paper/main.tex\n- **PDF 路径**: /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/main.pdf\n\n## 你的审查侧重\n\n请重点审查以下方面：\n\n1. **方法论严谨性**\n   - RSA 方法的适用性和实施正确性（within-task pairing, distance metrics, bootstrap）\n   - Probe 架构设计（MLP probe capacity, overfitting risk, train/test split）\n   - 实验控制设计（trained/untrained/pretrained 三条件, instruction ablation）\n   - Cross-architecture comparison 的有效性（OpenVLA vs TraceVLA 是否构成充分对比）\n\n2. **统计方法论**\n   - Bootstrap CI 和置换检验的正确应用\n   - 多重比较校正（FDR）\n   - 效应量报告（Cohen's d 的独立性假设是否满足）\n   - N=10 tasks 下 RSA 的统计功效\n   - 显著性标注的准确性\n\n3. **实验有效性**\n   - 消融实验设计（L1 head ablation）的因果推断力\n   - Counterfactual instruction analysis 的可靠性\n   - Dose-response 分析的说服力\n   - Linear probe 复现作为 robustness check 的充分性\n\n4. **内部一致性**\n   - 正文与 Appendix 数据一致性\n   - 不同分析方法的结论是否收敛\n   - RSA vs CKA 反转的处理是否充分\n\n请按照标准审稿格式输出：Summary → Strengths → Weaknesses (Must-Fix / Should-Fix / Minor) → Questions → Missing References → Overall Assessment (1-10 分 + 置信度)。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "text": "你是 Reviewer 1，负责 **方法严谨性 + 实验有效性 + 统计方法论** 审查。\n\n## 论文信息\n- **标题**: Vision Encodes, Language Reorganizes: Token-Level Representational Analysis of VLA Fine-Tuning\n- **目标 Venue**: CoRL 2026\n- **Deadline**: 2026-05-29\n- **格式**: CoRL 2026 模板，double-blind，正文 8 页 + references + appendix（不计入页数）\n- **匿名规则**: Double-blind\n- **论文路径**: projects/vla-ssd/docs/paper/main.tex\n- **PDF 路径**: /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/main.pdf\n\n## 你的审查侧重\n\n请重点审查以下方面：\n\n1. **方法论严谨性**\n   - RSA 方法的适用性和实施正确性（within-task pairing, distance metrics, bootstrap）\n   - Probe 架构设计（MLP probe capacity, overfitting risk, train/test split）\n   - 实验控制设计（trained/untrained/pretrained 三条件, instruction ablation）\n   - Cross-architecture comparison 的有效性（OpenVLA vs TraceVLA 是否构成充分对比）\n\n2. **统计方法论**\n   - Bootstrap CI 和置换检验的正确应用\n   - 多重比较校正（FDR）\n   - 效应量报告（Cohen's d 的独立性假设是否满足）\n   - N=10 tasks 下 RSA 的统计功效\n   - 显著性标注的准确性\n\n3. **实验有效性**\n   - 消融实验设计（L1 head ablation）的因果推断力\n   - Counterfactual instruction analysis 的可靠性\n   - Dose-response 分析的说服力\n   - Linear probe 复现作为 robustness check 的充分性\n\n4. **内部一致性**\n   - 正文与 Appendix 数据一致性\n   - 不同分析方法的结论是否收敛\n   - RSA vs CKA 反转的处理是否充分\n\n请按照标准审稿格式输出：Summary → Strengths → Weaknesses (Must-Fix / Should-Fix / Minor) → Questions → Missing References → Overall Assessment (1-10 分 + 置信度)。"
  }
}
```

</details>

---


### Tool result

_source line 1054 · 2026-05-20T16:25:31.976062+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 11353
}
```

</details>

---


### Tool call

_source line 1055 · 2026-05-20T16:25:32.128110+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "你是 Reviewer 2，负责 **新颖性 + CoRL scope fit + related work 覆盖度 + 写作质量** 审查。\n\n## 论文信息\n- **标题**: Vision Encodes, Language Reorganizes: Token-Level Representational Analysis of VLA Fine-Tuning\n- **目标 Venue**: CoRL 2026\n- **Deadline**: 2026-05-29\n- **格式**: CoRL 2026 模板，double-blind，正文 8 页 + references + appendix（不计入页数）\n- **匿名规则**: Double-blind\n- **论文路径**: projects/vla-ssd/docs/paper/main.tex\n- **PDF 路径**: /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/main.pdf\n\n## 你的审查侧重\n\n请重点审查以下方面：\n\n1. **新颖性与贡献**\n   - 三个 findings 各自的新颖度（entry-exit attention redistribution, convergent reorganization, token specialization）\n   - 相对于 Grant et al. 2026, Häon et al. 2025, Lu et al. 2025 等近期工作的增量贡献\n   - Token specialization (Finding 3) 是否确实是 causal mask 的必然结果而非实证发现\n   - Cross-architecture comparison (N=2 architectures) 是否足以支撑 \"convergent reorganization\" claims\n\n2. **CoRL Scope Fit**\n   - CoRL 是机器人学习会议——本文是纯 representational analysis，无机器人实验、无 closed-loop 评估\n   - 论文提出的 actionable implications（如 early-exit inference, L1 entropy monitoring）是否经过验证\n   - 与同 venue 已发表的分析性工作（如 Häon et al. CoRL 2025）的对比——是否达到 CoRL 对分析性论文的接受阈值\n\n3. **Related Work 覆盖度**\n   - 引用是否全面、准确（检查是否遗漏关键工作）\n   - 与最近期相关工作的区分是否清晰\n   - 引用格式是否正确（是否使用已发表版本而非 arXiv preprint）\n\n4. **写作质量**\n   - Abstract 信息密度是否合理\n   - Introduction 叙事结构是否清晰\n   - Figures/Tables 设计质量\n   - 术语一致性\n   - 是否存在 AI 写作痕迹（em-dash 过多、formulaic patterns、过度使用三段式等）\n   - Limitations section 是否满足 CoRL 要求\n   - Generative AI disclosure 是否存在\n\n请按照标准审稿格式输出：Summary → Strengths → Weaknesses (Must-Fix / Should-Fix / Minor) → Questions → Missing References → Overall Assessment (1-10 分 + 置信度)。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "text": "你是 Reviewer 2，负责 **新颖性 + CoRL scope fit + related work 覆盖度 + 写作质量** 审查。\n\n## 论文信息\n- **标题**: Vision Encodes, Language Reorganizes: Token-Level Representational Analysis of VLA Fine-Tuning\n- **目标 Venue**: CoRL 2026\n- **Deadline**: 2026-05-29\n- **格式**: CoRL 2026 模板，double-blind，正文 8 页 + references + appendix（不计入页数）\n- **匿名规则**: Double-blind\n- **论文路径**: projects/vla-ssd/docs/paper/main.tex\n- **PDF 路径**: /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/main.pdf\n\n## 你的审查侧重\n\n请重点审查以下方面：\n\n1. **新颖性与贡献**\n   - 三个 findings 各自的新颖度（entry-exit attention redistribution, convergent reorganization, token specialization）\n   - 相对于 Grant et al. 2026, Häon et al. 2025, Lu et al. 2025 等近期工作的增量贡献\n   - Token specialization (Finding 3) 是否确实是 causal mask 的必然结果而非实证发现\n   - Cross-architecture comparison (N=2 architectures) 是否足以支撑 \"convergent reorganization\" claims\n\n2. **CoRL Scope Fit**\n   - CoRL 是机器人学习会议——本文是纯 representational analysis，无机器人实验、无 closed-loop 评估\n   - 论文提出的 actionable implications（如 early-exit inference, L1 entropy monitoring）是否经过验证\n   - 与同 venue 已发表的分析性工作（如 Häon et al. CoRL 2025）的对比——是否达到 CoRL 对分析性论文的接受阈值\n\n3. **Related Work 覆盖度**\n   - 引用是否全面、准确（检查是否遗漏关键工作）\n   - 与最近期相关工作的区分是否清晰\n   - 引用格式是否正确（是否使用已发表版本而非 arXiv preprint）\n\n4. **写作质量**\n   - Abstract 信息密度是否合理\n   - Introduction 叙事结构是否清晰\n   - Figures/Tables 设计质量\n   - 术语一致性\n   - 是否存在 AI 写作痕迹（em-dash 过多、formulaic patterns、过度使用三段式等）\n   - Limitations section 是否满足 CoRL 要求\n   - Generative AI disclosure 是否存在\n\n请按照标准审稿格式输出：Summary → Strengths → Weaknesses (Must-Fix / Should-Fix / Minor) → Questions → Missing References → Overall Assessment (1-10 分 + 置信度)。"
  }
}
```

</details>

---


### Tool result

_source line 1056 · 2026-05-20T16:25:33.851334+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1723
}
```

</details>

---


### Assistant

_source line 1057 · 2026-05-20T16:25:39.217826+00:00_

圆桌审稿 Round 1 已启动：

- **Reviewer 1** (方法/实验/统计): 已分配
- **Reviewer 2** (新颖性/scope/related work/写作): 已分配
- **外部审稿** (Stanford Agentic Reviewer): 请求已发送，8h 后自动提醒
- **视觉审查 Agent**: 已派发，并行运行中

等待两位 Reviewer 返回独立初审结果。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director"
}
```

</details>

---


## Round 100

## Round 100

2 recorded events


### User

_source line 1058 · 2026-05-20T16:34:30.689331+00:00_

[Reviewer 1 审稿意见]:

# Reviewer 1: 方法严谨性 + 实验有效性 + 统计方法论

**论文**: Vision Encodes, Language Reorganizes: Token-Level Representational Analysis of VLA Fine-Tuning
**Venue**: CoRL 2026

---

## Summary

本文对 VLA（Vision-Language-Action）模型的微调机制进行了 token 级别的表征分析。核心发现：(1) VLA 微调将指令注意力从中层重新分配到入口-出口层（L1 和 L31），(2) 视觉编码器输出在 LLM 中层呈倒 U 型 RSA 曲线，(3) 两种不同架构（OpenVLA/LLaMA-2-7B 和 TraceVLA/Phi-3-V）从截然不同的起点收敛到相似的中层动作特化模式。方法上组合了 RSA、cross-instruction probes、注意力分析、L1 head ablation、counterfactual instruction 分析和 dose-response 曲线，共 7 种互补分析。实验基于 LIBERO-Goal（10 tasks）和 LIBERO-Spatial（10 tasks）。

---

## 官方维度打分（基于 CoRL 2023/2024 review criteria）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Originality | 3.5/5 | Token 级多方法表征分析在 VLA 领域较新；但核心方法（RSA、probing、ablation）均为成熟技术的应用组合 |
| Quality / Soundness | 3/5 | 统计流程整体规范（bootstrap CI、FDR correction），但存在 Cohen's d 独立性假设违反、N=10 统计功效不足、跨架构对比混杂变量等问题 |
| Clarity | 4/5 | 写作清晰、组织合理、正文 8 页密度适当；23 页 appendix 提供充分细节；少数术语不一致 |
| Significance | 3/5 | 对理解 VLA 微调机制有贡献，但纯分析性工作无直接方法改进或机器人实验验证 |
| Relevance | 3/5 | 与 robot learning 社区相关（理解 VLA 表征），但对 CoRL 的直接 robotics 价值有限——无 closed-loop 验证、无新方法/新架构 |

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] Cohen's d 独立性假设违反——效应量可能被高估
- 具体位置：Section 4.3（dose-response, Table 5）、Table 6（counterfactual）、Appendix A.7（Table 4, per-head bootstrap）
- 问题：论文全文使用 Cohen's d 量化 ablation 和 counterfactual 对动作序列的影响。但这些比较本质上是**配对数据**——同一输入在原始模型 vs ablated/counterfactual 模型上产生的动作向量。标准 Cohen's d 假设两组样本独立，而此处两组共享输入方差，导致 pooled SD 高估、d 值被系统性抬升。例如 dose-response（Table 5）的 d = 0.482→0.639 和 counterfactual（Table 6）的 d = 0.625→0.968 的实际效应量可能更小。
- 为什么影响接收：效应量是论文多处核心论证的支撑（"graded rather than binary specialization"、counterfactual ordering），若效应量被系统高估，关键结论的可靠性受损。
- 建议修改方向：(a) 改用配对效应量（Cohen's d_z = mean_diff / sd_diff）；(b) 报告配对相关系数以评估膨胀程度；(c) 至少在 Limitations 中明确讨论。注：bootstrap CI 可能不受此影响（取决于实现），但 d 值本身需要修正。

**N2** [critical] N=10 tasks 下 RSA 的统计功效不足——多处 null result 可能是 power 不足
- 具体位置：Section 3.5（RSA, N_eff = 10）、Section 4.4（"Best-vs-best RSA gain is non-significant on LIBERO-Goal"）、Table 12（training effects）
- 问题：RSA 在 task level 做 bootstrap（N_eff = 10），这是所有 RSA 推断的基础样本量。论文在 Section 4.4（line 143）正确承认了 "The N=10 instruction set limits statistical power"，但未提供 power analysis。关键问题：
  - LIBERO-Goal 上 trained vs untrained 的 RSA best-vs-best 差异 Δ=+0.017 不显著（Table 12），但 LIBERO-Spatial 上 Δ=+0.023 显著（p<0.001）。两者绝对差异仅 0.006——差异在是否显著完全取决于效应量与 N=10 的交互，而非真正的 benchmark 差异。
  - 跨架构对比（OpenVLA vs TraceVLA, Δ=0.003）的 CI 重叠被解读为"convergent"，但 N=10 下 CI 极宽，重叠可能只反映 power 不足而非真正等价。
- 为什么影响接收：论文的多个核心 claim（训练效应的显著性、跨架构收敛）直接依赖 N=10 的统计推断。
- 建议修改方向：(a) 提供 power analysis，报告 N=10 下可检测的最小效应量；(b) 对"non-significant = no effect"的解读加更强的 caveat；(c) 对跨架构"convergence"用等价性检验（TOST）而非仅靠 CI 重叠。

**N3** [critical] 跨架构对比的混杂变量——"convergent reorganization"claim 过强
- 具体位置：Section 4.3（"Cross-architecture generalization"）、Section 5（Discussion）、Appendix A.24
- 问题：OpenVLA（LLaMA-2-7B, 32 layers, SigLIP+DINOv2 vision encoder, 970K episodes pretraining）和 TraceVLA（Phi-3-V, 32 layers, CLIP vision encoder, 不同 pretraining）同时在多个维度上不同：backbone 架构、pretraining 数据量与分布、vision encoder、instruction tuning 状态（Phi-3-V 有 instruction tuning，LLaMA-2 无）、训练数据量（TraceVLA 只用 5 tasks vs OpenVLA 10 tasks, Section 4.3 line 61）。两种架构在 mid-layer peaks 上 Δ=0.003 的"收敛"可能反映：
  - Transformer LLM 的通用归纳偏置（非 VLA 特有）
  - LIBERO 任务结构的约束（tabletop manipulation 的 action space 简单）
  - 32 层结构 + causal decoder 的共同约束
- 为什么影响接收："Convergent reorganization" 是论文的主要 contribution 之一（abstract, introduction, discussion 均强调）。如果收敛仅反映架构共性而非 VLA 训练的通用规律，核心 novelty 受损。
- 建议修改方向：(a) 降低 claim 强度——"suggestive evidence"而非"convergent reorganization"；(b) 增加控制实验：同一 backbone 不同 VLA recipe，或不同 task suite 同一 backbone；(c) 讨论哪些混杂变量最可能解释收敛。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] 多重比较校正范围不充分
- 具体位置：Section 4.4（line 144, FDR correction α=0.05, 33-layer family per metric）
- 问题：FDR 校正仅在每个 metric 的 33 层内进行。但论文的完整测试空间包括：多个 metrics（RSA ρ, R², probe accuracy, attention fraction）× 多个 token positions（image_mean, readout, last_projection）× 多个 conditions（3 training states × 2 architectures）× 多种分析（cross-instruction, attention, ablation, counterfactual）。未对全局 family-wise error rate 进行校正。
- 建议：至少在 appendix 中报告全局 FDR 校正结果，或讨论校正范围选择的 rationale。

**W2** [warning] L1 head ablation 的因果推断力被过度表述
- 具体位置：Section 4.3（"instruction-dominant heads control instruction-specific direction selection"）、Section 5
- 问题：Ablation 证明 necessity（移除后系统退化），但不证明 sufficiency 或 mechanism。"Control" 这个词暗示了因果关系，但 ablation 只说明系统依赖这些 heads。且 matched-size ablation（Table 23）显示 instruction-dominant heads 效应仅比 random heads 大 8%（d = 0.650 vs 0.601），差异较小。
- 建议：将 "control" 替换为 "contribute to" 或 "are necessary for"；强调 8% 的 modest gap。

**W3** [warning] RSA vs CKA 反转的处理不够充分
- 具体位置：Appendix A.1-A.2（Section metric_sensitivity_appendix）
- 问题：Linear CKA 完全反转了 RSA 的 ordering（untrained > trained > DINOv2，Table in A.2），这不是一个小差异而是定性反转。论文仅用 "different geometric properties" 一笔带过。对于一篇以表征分析为核心方法的论文，两种标准 metric 给出相反结论是重大方法论问题。RDM kernel CKA 部分解决了分歧，但论文未充分讨论何时应信任 RSA vs CKA。
- 建议：增加一段讨论 RSA vs CKA 的适用条件，特别是在 high-dim vs low-dim 比较中的行为差异；讨论哪些 claim 对 metric 选择 robust（如中层 peak），哪些不 robust（如 DINOv2 vs VLA 的相对排序）。

**W4** [warning] 仅 LIBERO 生态系统评估——生态效度受限
- 具体位置：Section 3.1、Section 5（Limitations）
- 问题：所有实验使用 LIBERO-Goal（10 tasks）和 LIBERO-Spatial（10 tasks），均为 tabletop manipulation。LIBERO 的特点（7-D action space、短 horizon、10 个有限 tasks、视觉简单的 tabletop 场景）可能是很多发现的充分条件：
  - 倒 U 型 RSA 可能反映 LIBERO 的简单 action space 而非通用 VLA 特性
  - 跨架构收敛可能反映 LIBERO 的 task structure 约束
- 建议：在 Limitations 中明确讨论 LIBERO 特异性风险；提出在更多样的 benchmark（如 multi-task SIMPLER、real-world tasks）上验证的路径。

**W5** [warning] Counterfactual instruction analysis 仅用 3 个 tasks
- 具体位置：Table 6 caption（"computed on 3 representative tasks: cabinet, bowl, plate"）
- 问题：Table 6 的 counterfactual 分析（empty/wrong/paraphrased/shuffled）仅在 3/10 tasks 上进行。3 个 tasks 的 Cohen's d 估计方差很大；"token novelty perfectly predicts divergence ordering (Spearman ρ = 1.0)" 在 4 个条件上 ρ=1.0 不具统计意义（4 点的 Spearman ρ=1.0 的 p=0.042，仅 marginal）。
- 建议：在全部 10 tasks 上复现 counterfactual 分析；或至少报告 3 tasks 选择的 rationale 和 cross-task variance。

**W6** [warning] 单一训练 checkpoint 分析
- 具体位置：Section 3.1
- 问题：OpenVLA-7B 和 TraceVLA 各分析了一个 released checkpoint。虽然 probe seeds（5 或 15）变化了，但底层 trained model 是固定的。不同 training seed / data order 可能产生不同的表征结构。Mechanistic interpretability 文献中这是常见限制，但论文未讨论。
- 建议：在 Limitations 中明确 acknowledge；讨论哪些发现对 training stochasticity 可能 robust（如整体 inverted-U shape）vs sensitive（如具体 peak layer L9 vs L12）。

---

## 小问题（不影响接收）

1. **术语不一致**："readout token" 和 "last_preaction" 在不同 section 交替使用（如 Table 3 vs Table 12 vs Appendix figures）。建议统一为一个术语并在首次出现时定义。

2. **Footnote 1 (p.5)**："R² values differ from Table 1 due to the feature reconstruction pipeline"——值不同需要更详细解释。两个 pipeline 的差异是什么？读者无法判断哪组数字更可靠。

3. **Permutation test 的 shuffle 次数**：Appendix A.15.3 用 1,000 shuffles，而 bootstrap 用 10,000 resamples。虽然效应很大（15-23 SD），但统计实践建议 permutation tests 也用 ≥10,000。

4. **Untrained model 在 L1 达到 100% cross-instruction classification**（Table 1）：这表明 L1 的指令可分类性是架构属性而非训练效应。论文在 Appendix A.18.1 提到这源于 frozen tokenizer embeddings 的高区分度，但正文对此讨论不够——这会弱化 "VLA fine-tuning creates instruction specialization at L1" 的 narrative。

5. **Leave-one-out sensitivity**（Appendix A.22, line 775）："All leave-one-out p-values remain ≤ 0.083"——0.083 > 0.05，意味着部分 task 移除后结果在常规显著性水平不再显著。这应被表述为 "marginal" 而非 "robust"。

6. **参考文献小问题**：verify_references 发现 7 条 first_author mismatch（liu2023_libero: bib=liu vs api=feng; 等），6 条 not_found（均为 blog posts/Transformer Circuits Thread，非正式出版物，可接受）。无严重引用问题。

---

## 主要优势

1. **多方法收敛**：7 种互补分析（RSA、probes、attention、ablation、dose-response、counterfactual、cross-architecture）对同一问题给出一致结论，这种方法论密度在 VLA 文献中少见。
2. **统计实践整体规范**：Bootstrap CI（10,000 resamples）、FDR correction、permutation tests、probe seed sensitivity（5/15 seeds）均为 best practice。
3. **23 页 Appendix 的彻底性**：涵盖 probe architecture sensitivity（A.10）、demo subsample sensitivity（A.15.4）、distance metric invariance（A.15.1）、per-DOF decomposition（A.15.2）、threshold sensitivity（A.18.6）、leave-one-out（A.22）、matched-size control（A.23）等 robustness checks。
4. **信息-计算分离发现**：Ablation 提高 R² 但不降低 ground-truth MSE（Section 4.3, Appendix A.7）是一个有趣且反直觉的发现，具有理论价值。
5. **Pretrained LLM 的 OOD 诊断**（Appendix A.9）：主动验证 Llama-2 base 在从未见过的 projected visual tokens 上的表征质量，体现了对实验控制的严肃态度。
6. **Cross-architecture 比较**：虽有混杂变量（N3），但在 VLA mechanistic interpretability 中提供了罕见的跨架构视角。

---

## Missing References

无明显遗漏。论文覆盖了 VLA interpretability 的核心文献（Grant et al. 2026, Häon et al. 2025, Swann et al. 2026, Buurmeijer et al. 2026）以及 mechanistic interpretability 经典工作（Elhage 2021, Olsson 2022, Wang 2023）。RSA/CKA 方法论引用完整（Kriegeskorte 2008, Kornblith 2019, Nili 2014）。

---

## Overall Assessment

**Overall Score: 6/10**（Marginally above acceptance threshold）

**置信度: 4/5**（方法论和统计问题是我的审查重点，对此有高置信度；对 CoRL 社区的接收标准判断有中等置信度）

**一句话总结**：方法论密度和 robustness checks 的彻底性在 VLA 表征分析中出色，但三个核心统计/实验问题（Cohen's d 独立性、N=10 power、跨架构混杂变量）需要在 camera-ready 前解决；纯分析性工作在 CoRL 的竞争力取决于这些问题的修复程度。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 1059 · 2026-05-20T16:34:40.913076+00:00_

Reviewer 1 审稿已收到（6/10），等待 Reviewer 2 提交后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director"
}
```

</details>

---


## Round 101

## Round 101

2 recorded events


### User

_source line 1060 · 2026-05-20T16:34:43.592006+00:00_

[Reviewer 1 审稿结果]:
审稿意见已提交给 Review Director。

**审稿完成摘要**：

- **Overall Score: 6/10**（Marginally above acceptance threshold）
- **3 个 Must-Fix 问题**：(1) Cohen's d 独立性假设违反导致效应量高估；(2) N=10 tasks 的统计功效不足；(3) 跨架构对比混杂变量过多，"convergent reorganization" claim 过强
- **6 个 Should-Fix 问题**：多重比较校正范围、ablation 因果推断过度表述、RSA vs CKA 反转处理不足、LIBERO-only 生态效度、counterfactual 仅用 3 tasks、单一 training checkpoint
- **主要优势**：7 种互补分析的方法论密度、规范的统计实践、23 页 appendix 的彻底 robustness checks、信息-计算分离的有趣发现

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 1061 · 2026-05-20T16:34:48.448265+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director"
}
```

</details>

---


## Round 102

## Round 102

6 recorded events


### User

_source line 1062 · 2026-05-20T16:35:18.249657+00:00_

[Reviewer 2 审稿意见]:

# Reviewer 2 审稿意见

**论文**: Vision Encodes, Language Reorganizes: Token-Level Representational Analysis of VLA Fine-Tuning
**Venue**: CoRL 2026
**审查侧重**: 新颖性 + CoRL scope fit + related work 覆盖度 + 写作质量

---

## Summary

本文对两个 causal-decoder VLA 模型（OpenVLA/Llama-2-7B 和 TraceVLA/Phi-3-mini）的微调前后内部表征变化进行了系统分析，使用 cross-instruction probes、attention pattern analysis、RSA 和 functional probes 四种互补方法。主要发现三个现象：(1) 微调将 instruction attention 从中间层重分配到 entry-exit 层（尤其 L1）；(2) 两个架构从不同起点收敛到相似的中层 action decodability profile；(3) image tokens 对指令不敏感而 readout token 整合多模态信息。附录极其详尽（21页），包含大量消融实验和鲁棒性验证。

---

## 官方维度打分（基于 CoRL Reviewer Guidelines: Originality / Quality / Clarity / Significance / Relevance / Limitations）

| 维度 | 评分 | 理由摘要 |
|------|------|----------|
| Originality | 2.5/5 | Finding 1 有一定新颖性但方法论（probing/RSA/attention）均为成熟工具的标准应用；Finding 3 是 causal mask 的架构必然结果 |
| Quality | 3.5/5 | 实验设计严谨、控制条件完整、附录详尽；但 N=2 架构、单一 benchmark、效果量极小 |
| Clarity | 4/5 | 写作清晰、术语一致、图表质量好 |
| Significance | 2/5 | 纯观察性分析，所有 "actionable implications" 均未验证；对机器人学习实践的指导有限 |
| Relevance | 2/5 | 纯 representational analysis，无机器人实验、无 closed-loop 评估、无策略改进 |
| Limitations | 4/5 | 诚实讨论了 N=2 架构、无 cross-attention VLA、仅 LIBERO 等局限 |

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] CoRL scope fit 严重不足——纯分析无机器人实验验证

- 具体位置：全文；Section 5 (Limitations)；Section 4.4 (Actionable implications)
- 问题：CoRL 要求论文 "address a problem in robot learning" 并展示对机器人学习的相关性。本文是纯粹的 representational analysis：
  - 无任何机器人实验（模拟或真实）
  - 无 closed-loop policy 评估
  - 无策略改进的实际验证
  - 提出的 actionable implications（early-exit inference, L1 entropy monitoring）在 Section 5 明确标注为 "natural next step"，即**完全未验证**
- 对比 Häon et al. (CoRL 2025)：该论文被 CoRL 接收是因为它不仅分析了内部表征，还**实际演示了通过表征方向进行 VLA 行为引导（steering）**——这是明确的机器人学习贡献。本文缺乏任何类比的实践验证。
- 为什么影响接收：CoRL 对分析性论文的接受阈值要求至少有可验证的实际启示。纯观察性工作更适合 ICML/NeurIPS 的 interpretability track。
- 建议修改方向：至少验证一个 actionable implication。例如，实验验证 early-exit inference 是否真能在保持策略性能的前提下减少计算开销；或验证 L1 attention entropy 是否确实能预测 out-of-distribution 场景下的策略失败。

**N2** [critical] N=2 架构不足以支撑 "convergent reorganization" 的 claim

- 具体位置：Abstract ("convergent reorganization"); Section 4.3 ("Convergent reorganization..."); Title implicit claim
- 问题：论文从仅两个 causal-decoder VLA（OpenVLA 和 TraceVLA）的比较中声称发现了 "convergent reorganization"。这两个模型共享关键架构选择：
  - 均为 causal decoder（autoregressive LLM backbone）
  - 均使用相似规模（3B-7B 参数）
  - 均在同一 benchmark（LIBERO）上训练
  - 均使用 tokenized action 输出
  
  从 N=2 个共享大量架构 DNA 的模型中观察到类似的中层 action decodability peaks，不能排除这只是 causal decoder + action tokenization 的结构性产物。"Convergent" 这个词暗示了跨越不同设计空间的通用规律，但论文的数据无法支撑这一推断。
- 为什么影响接收：这是论文的核心 claim 之一（Finding 2），如果不成立，论文的贡献大幅缩水。
- Appendix A.24 的 cross-architecture 分析确实尝试了比较，但两个架构的 exit-layer R² 差异明显（0.488 vs 0.557），peak layer 也不同，实际上部分削弱了 "convergent" 的论点。
- 建议修改方向：(a) 将 claim 弱化为 "shared tendency" 或 "preliminary evidence for convergence"；(b) 在 Appendix A.24 明确量化两个架构 profile 的差异并讨论；(c) 理想情况下加入至少一个非 causal-decoder 架构（如 cross-attention VLA）作为对照。

**N3** [critical] Finding 3（Token Specialization）是 causal mask 的架构必然结果，不应作为独立发现

- 具体位置：Abstract ("Third, token-level analysis confirms expected functional specialization"); Section 4.2; Table 1
- 问题：在 causal attention 下，序列位置 i 的 token 只能 attend to 位置 ≤i。VLA 的输入序列为 [image tokens | instruction tokens | action tokens]。因此 image tokens 在架构层面上就**不可能**访问 instruction tokens 的信息。论文发现 "image tokens are instruction-blind" 完全是 causal mask 的直接推论，不是实证发现。
  
  论文在 Section 4.2 承认这是 "consistent with the causal attention mask" 并称之为 "framework sanity check"，但在 Abstract 和 Introduction 中仍将其列为三大发现之一（"Third, token-level analysis confirms..."）。这膨胀了贡献数量——实际上论文只有两个实证发现（Finding 1 和 Finding 2）。
- 为什么影响接收：审稿人和 AC 会注意到三个 findings 中有一个是 trivial 的，这降低了论文的整体可信度。
- 建议修改方向：将 Finding 3 明确重新定位为方法论验证（methodology validation），而非独立发现。在 Abstract 中不要将其与 Finding 1/2 并列为 "findings"，改为类似 "We validate our framework by confirming that..." 的表述。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] 相对于近期并发工作的增量贡献不清晰

- 具体位置：Section 2 (Related Work); Section 5 (Discussion)
- 问题：论文与 Grant et al. (2026) 和 Häon et al. (2025) 的差异化不够充分：
  - Grant et al. 使用 contrastive identification 发现了 82+ 可操控的 manipulation concepts 并释放了 Action Atlas——这些是**可操作**的结果。本文的 probing/RSA 分析是纯观察性的。
  - Häon et al. 展示了通过 feedforward 激活投影进行 VLA **steering**。本文没有任何干预实验（counterfactual ablation 除外，但那只是分析工具）。
  - Section 5 的 Discussion 仅用一段（约3行）与 Grant et al. 做对比，不够深入。
- 建议：在 Related Work 或 Discussion 中添加一个明确的表格或段落，逐条对比本文与 Grant/Häon/Swann/Buurmeijer 在方法、发现和 actionability 上的差异。

**W2** [warning] 报告的效果量极小，实际意义存疑

- 具体位置：Section 4.3 (ΔR² ≈ 0.03); Section 4.4 (RSA ρ ≈ 0.02); Table 3 (RSA peak ρ values)
- 问题：
  - 训练带来的 action probe R² 提升为 ΔR² ≈ 0.03（Section 4.3），虽然统计显著但绝对值极小
  - RSA 与 action space 的最高对齐度为 ρ = 0.02（DINOv2, Table 3）——这个数值接近零
  - 论文的核心定量结论建立在这些微小效果量之上
  - 虽然 Table 3 的 footnote 解释了 RSA 值在高维空间中期望较低，但这进一步说明 RSA 可能不是评估此类表征变化的理想工具
- 建议：(a) 添加 effect size 的讨论（Cohen's d 或类似指标）；(b) 明确论证为什么这些微小的定量变化对应有实际意义的表征变化。

**W3** [warning] 标题的因果声明（"Vision Encodes, Language Reorganizes"）超出了观察性证据的支撑

- 具体位置：Title; Abstract
- 问题：标题 "Vision Encodes, Language Reorganizes" 暗示了因果机制——vision encoder 负责编码，language backbone 负责重组织。但论文的所有分析工具（probes, RSA, attention patterns）都是**观察性/相关性**的。论文没有做因果干预实验（如 activation patching, causal tracing）来建立这种因果关系。Counterfactual ablation（Section 4.5）only ablates attention heads，不是对 "vision encodes" vs "language reorganizes" 这一 claim 的因果验证。
- 建议：考虑弱化标题或在 Introduction 中明确声明这是基于观察证据的 working hypothesis 而非因果结论。

**W4** [warning] 单一 benchmark (LIBERO) 的泛化性

- 具体位置：Section 3 (Method); Section 5 (Limitations)
- 问题：所有实验仅在 LIBERO-Goal 的 10 个任务上进行。LIBERO 是桌面操作任务，对象集有限、场景单一。Appendix A.14 虽然在 LIBERO-Spatial 上做了验证，但这仍是同一 benchmark 系列。论文的 findings 是否泛化到：
  - 不同的 embodiment（非桌面操作）？
  - 更大规模的训练数据（如 Open X-Embodiment）？
  - 不同的 action space（连续 vs 离散）？
  这些问题在 Limitations 中仅简略提及。
- 建议：至少在 Limitations 中更详细地讨论泛化性边界。

---

## 小问题（不影响接收）

**M1** 引用格式：部分论文使用 arXiv preprint 但可能已有正式发表版本。例如：
  - `brohan2023_rt2` (RT-2) — 检查是否有正式会议/期刊版本
  - `belrose2023_tunedlens` — 检查是否已发表
  - `black2024_pi0` (π₀) — OpenAlex 未找到此条目，检查引用信息是否完整

**M2** 引用验证结果中有 7 条 first-author mismatch（`liu2023_libero`, `haon2025`, `fei2025`, `neo2025`, `padalkar2023_oxe`, `long2026understanding`, `xiao2025ava`）——可能是 LaTeX 编码问题或实际作者名错误，建议逐条核实。

**M3** 6 条引用在 OpenAlex 中未找到（`elhage2021`, `hewitt2019`, `bills2023language`, `templeton2024scaling`, `nostalgebraist2020`, `black2024_pi0`）。其中大多数是 blog post / technical report 类文献，不在传统学术数据库中，引用本身合理，但建议统一标注为 `misc` 类型并注明 URL。

**M4** Generative AI disclosure 已存在（p.12: "Generative AI tools (Claude, GPT4o) assisted with code implementation and manuscript editing"）——符合 CoRL 2026 要求。

**M5** 写作质量总体良好。未发现明显的 AI 写作痕迹（em-dash 使用正常，无过度 formulaic patterns）。术语使用一致（"readout token", "instruction-dominant heads" 等）。Figure 1 设计清晰有效。

**M6** Limitations section 存在且诚实（Section 5），满足 CoRL 要求。

**M7** 潜在遗漏引用：Aghajanyan et al. (ACL 2021) "Intrinsic Dimensionality Explains the Effectiveness of Language Model Fine-Tuning" — 该工作直接关联 fine-tuning 如何改变表征空间的维度结构，与本文的核心问题高度相关。建议在 Related Work 或 Discussion 中引用讨论。

---

## 主要优势

1. **方法论系统性强**：四种互补分析工具（probes, attention, RSA, functional probes）从不同角度交叉验证，减少了单一方法的偏见。Trained/untrained/factorial 三条件对比设计合理。

2. **Finding 1 有实质价值**：Entry-exit attention redistribution 现象（尤其 L1 concentration）是一个有趣的发现，dose-response 实验（Figure 9, Appendix A.8）和 head ablation（Appendix A.7）提供了有意义的支撑证据。

3. **附录极其详尽**：21页附录覆盖了 CKA vs RSA 比较、probe architecture sensitivity、cross-benchmark validation、leave-one-out sensitivity、matched-size control 等——这是极少见的彻底程度。

4. **实验设计的控制组完整**：包括 untrained VLA baseline、pretrained Llama-2 base、factorial controls，使得 findings 的归因更可靠。

5. **引用管理干净**：59 条引用全部被 cite，无 orphan entries，无 missing bib keys。

---

## Questions for Authors

Q1. Finding 1 中 L1 instruction-dominant heads 的出现是否可能是 VLA 训练时学习率 warmup 的人工产物？即如果第一层权重在训练早期变化最大，L1 attention 的变化是否反映了优化器动态而非功能性重组织？

Q2. 如果将 Finding 3（token specialization）从论文发现中移除并仅作为方法论验证，作者是否认为剩余两个 findings 足以支撑一篇完整的 CoRL 论文？

Q3. Section 4.4 提到 "L1 entropy monitoring" 可以作为部署时的诊断工具。作者是否有任何 preliminary 数据（哪怕是 toy experiment）表明 L1 entropy 确实与 policy failure 相关？

Q4. Appendix A.24 中两个架构的 exit-layer R² 差异明显（OpenVLA 0.488 vs TraceVLA/Phi-3-V 0.557）。这个差异是否足以质疑 "convergent" 的 claim？作者如何定义 "convergent" 的量化标准？

---

## Missing References

1. **Aghajanyan, Zettlemoyer & Gupta (ACL 2021)** — "Intrinsic Dimensionality Explains the Effectiveness of Language Model Fine-Tuning"：直接相关于理解 fine-tuning 如何改变表征空间。

2. **Kumar et al. (NeurIPS 2022)** — "Fine-Tuning can Distort Pretrained Features and Underperform Out-of-Distribution"：讨论 fine-tuning 对 pretrained features 的扭曲效应，与本文 Finding 2（表征重组织）直接相关。

3. 建议检查 **Tong et al. (NeurIPS 2024)** "Eyes Wide Shut? Exploring the Visual Shortcomings of Multimodal LLMs" 是否值得引用——该工作分析了 VLM 的视觉处理局限性。

---

## Overall Assessment

**Overall Score: 4/10 (Borderline reject)**

**置信度: 4/5 (High confidence)**

**一句话总结**: 实验设计严谨、附录详尽的 VLA 表征分析工作，但 CoRL scope fit 严重不足（无任何机器人实验验证）、N=2 架构不足以支撑 "convergent" claims、且三个 findings 中一个是架构必然结果——核心贡献实质上缩减为单一观察性发现（entry-exit attention redistribution），对于 CoRL 这一机器人学习会议而言贡献不够。

**详细评分依据**：
- 论文的分析质量本身是可以的——方法论系统、控制组完整、附录极其彻底
- 但作为 CoRL 投稿有三个根本问题：(1) 零机器人实验验证、零 closed-loop evaluation；(2) "convergent" claim 从 N=2 同类架构中得出，证据不足；(3) 三分之一的 findings 是 trivial 的
- 与同 venue 已接收的分析工作（Häon et al. CoRL 2025）相比，缺乏 actionable 的实践贡献
- 建议转投 ICML/NeurIPS interpretability track，或补充至少一个 actionable implication 的实验验证后重投 CoRL



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 1063 · 2026-05-20T16:36:02.033128+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "以下是 Reviewer 1 的完整审稿意见，请逐条回应：对每个 Must-Fix 和 Should-Fix 条目，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n# Reviewer 1 完整审稿意见\n\n## Must-Fix 问题\n\n**N1** [critical] Cohen's d 独立性假设违反——效应量可能被高估\n- Section 4.3（dose-response, Table 5）、Table 6（counterfactual）、Appendix A.7\n- 论文全文使用 Cohen's d 量化 ablation 和 counterfactual 对动作序列的影响。但这些比较本质上是配对数据——同一输入在原始模型 vs ablated/counterfactual 模型上产生的动作向量。标准 Cohen's d 假设两组样本独立，而此处两组共享输入方差，导致 pooled SD 高估、d 值被系统性抬升。\n- 建议：改用配对效应量（Cohen's d_z = mean_diff / sd_diff）；报告配对相关系数以评估膨胀程度；至少在 Limitations 中明确讨论。\n\n**N2** [critical] N=10 tasks 下 RSA 的统计功效不足——多处 null result 可能是 power 不足\n- Section 3.5（RSA, N_eff = 10）、Section 4.4\n- LIBERO-Goal 上 Δ=+0.017 不显著，LIBERO-Spatial 上 Δ=+0.023 显著（p<0.001），两者绝对差异仅 0.006。\n- 跨架构对比（Δ=0.003）的 CI 重叠被解读为\"convergent\"，但 N=10 下 CI 极宽，重叠可能只反映 power 不足。\n- 建议：提供 power analysis，报告 N=10 下可检测的最小效应量；对跨架构\"convergence\"用等价性检验（TOST）。\n\n**N3** [critical] 跨架构对比的混杂变量——\"convergent reorganization\" claim 过强\n- OpenVLA 和 TraceVLA 同时在多个维度上不同：backbone 架构、pretraining 数据、vision encoder、instruction tuning 状态、训练数据量（5 vs 10 tasks）。\n- 两种架构在 mid-layer peaks 上 Δ=0.003 的\"收敛\"可能反映 Transformer LLM 的通用归纳偏置、LIBERO 任务结构的约束、或 32 层 + causal decoder 的共同约束。\n- 建议：降低 claim 强度——\"suggestive evidence\"而非\"convergent reorganization\"。\n\n## Should-Fix 问题\n\n**W1** 多重比较校正范围不充分——FDR 校正仅在每个 metric 的 33 层内进行，未对全局 family-wise error rate 进行校正。\n\n**W2** L1 head ablation 的因果推断力被过度表述——matched-size ablation 显示 instruction-dominant heads 效应仅比 random heads 大 8%。\n\n**W3** RSA vs CKA 反转的处理不够充分——Linear CKA 完全反转了 RSA 的 ordering，论文仅用 \"different geometric properties\" 一笔带过。\n\n**W4** 仅 LIBERO 生态系统评估——tabletop manipulation 的简单 action space 可能是很多发现的充分条件。\n\n**W5** Counterfactual instruction analysis 仅用 3 个 tasks——Spearman ρ=1.0 在 4 个条件上不具统计意义（p=0.042，marginal）。\n\n**W6** 单一训练 checkpoint 分析——不同 training seed 可能产生不同表征结构。\n\n## 小问题\n1. 术语不一致：\"readout token\" 和 \"last_preaction\" 交替使用\n2. Footnote 1 的两个 pipeline R² 值差异未解释\n3. Permutation test 仅 1,000 shuffles\n4. Untrained model 在 L1 达到 100% classification 弱化了 \"VLA fine-tuning creates instruction specialization at L1\" 的 narrative\n5. Leave-one-out p-values ≤ 0.083 不应表述为 \"robust\"\n\n## Overall Score: 6/10（Marginally above acceptance threshold）\n## 置信度: 4/5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "text": "以下是 Reviewer 1 的完整审稿意见，请逐条回应：对每个 Must-Fix 和 Should-Fix 条目，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n# Reviewer 1 完整审稿意见\n\n## Must-Fix 问题\n\n**N1** [critical] Cohen's d 独立性假设违反——效应量可能被高估\n- Section 4.3（dose-response, Table 5）、Table 6（counterfactual）、Appendix A.7\n- 论文全文使用 Cohen's d 量化 ablation 和 counterfactual 对动作序列的影响。但这些比较本质上是配对数据——同一输入在原始模型 vs ablated/counterfactual 模型上产生的动作向量。标准 Cohen's d 假设两组样本独立，而此处两组共享输入方差，导致 pooled SD 高估、d 值被系统性抬升。\n- 建议：改用配对效应量（Cohen's d_z = mean_diff / sd_diff）；报告配对相关系数以评估膨胀程度；至少在 Limitations 中明确讨论。\n\n**N2** [critical] N=10 tasks 下 RSA 的统计功效不足——多处 null result 可能是 power 不足\n- Section 3.5（RSA, N_eff = 10）、Section 4.4\n- LIBERO-Goal 上 Δ=+0.017 不显著，LIBERO-Spatial 上 Δ=+0.023 显著（p<0.001），两者绝对差异仅 0.006。\n- 跨架构对比（Δ=0.003）的 CI 重叠被解读为\"convergent\"，但 N=10 下 CI 极宽，重叠可能只反映 power 不足。\n- 建议：提供 power analysis，报告 N=10 下可检测的最小效应量；对跨架构\"convergence\"用等价性检验（TOST）。\n\n**N3** [critical] 跨架构对比的混杂变量——\"convergent reorganization\" claim 过强\n- OpenVLA 和 TraceVLA 同时在多个维度上不同：backbone 架构、pretraining 数据、vision encoder、instruction tuning 状态、训练数据量（5 vs 10 tasks）。\n- 两种架构在 mid-layer peaks 上 Δ=0.003 的\"收敛\"可能反映 Transformer LLM 的通用归纳偏置、LIBERO 任务结构的约束、或 32 层 + causal decoder 的共同约束。\n- 建议：降低 claim 强度——\"suggestive evidence\"而非\"convergent reorganization\"。\n\n## Should-Fix 问题\n\n**W1** 多重比较校正范围不充分——FDR 校正仅在每个 metric 的 33 层内进行，未对全局 family-wise error rate 进行校正。\n\n**W2** L1 head ablation 的因果推断力被过度表述——matched-size ablation 显示 instruction-dominant heads 效应仅比 random heads 大 8%。\n\n**W3** RSA vs CKA 反转的处理不够充分——Linear CKA 完全反转了 RSA 的 ordering，论文仅用 \"different geometric properties\" 一笔带过。\n\n**W4** 仅 LIBERO 生态系统评估——tabletop manipulation 的简单 action space 可能是很多发现的充分条件。\n\n**W5** Counterfactual instruction analysis 仅用 3 个 tasks——Spearman ρ=1.0 在 4 个条件上不具统计意义（p=0.042，marginal）。\n\n**W6** 单一训练 checkpoint 分析——不同 training seed 可能产生不同表征结构。\n\n## 小问题\n1. 术语不一致：\"readout token\" 和 \"last_preaction\" 交替使用\n2. Footnote 1 的两个 pipeline R² 值差异未解释\n3. Permutation test 仅 1,000 shuffles\n4. Untrained model 在 L1 达到 100% classification 弱化了 \"VLA fine-tuning creates instruction specialization at L1\" 的 narrative\n5. Leave-one-out p-values ≤ 0.083 不应表述为 \"robust\"\n\n## Overall Score: 6/10（Marginally above acceptance threshold）\n## 置信度: 4/5"
  }
}
```

</details>

---


### Tool result

_source line 1064 · 2026-05-20T16:36:18.107874+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 16074
}
```

</details>

---


### Tool call

_source line 1065 · 2026-05-20T16:36:20.228063+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "以下是 Reviewer 2 的完整审稿意见，请逐条回应：对每个 Must-Fix 和 Should-Fix 条目，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n# Reviewer 2 完整审稿意见\n\n## Must-Fix 问题\n\n**N1** [critical] CoRL scope fit 严重不足——纯分析无机器人实验验证\n- 无任何机器人实验（模拟或真实）、无 closed-loop policy 评估、无策略改进的实际验证\n- Actionable implications（early-exit inference, L1 entropy monitoring）完全未验证\n- 对比 Häon et al. (CoRL 2025)：该论文被接收因为它实际演示了通过表征方向进行 VLA 行为引导（steering）\n- 纯观察性工作更适合 ICML/NeurIPS 的 interpretability track\n- 建议：至少验证一个 actionable implication\n\n**N2** [critical] N=2 架构不足以支撑 \"convergent reorganization\" 的 claim\n- 两个模型共享关键架构选择：均为 causal decoder、相似规模（3B-7B）、同一 benchmark（LIBERO）、tokenized action 输出\n- \"Convergent\" 暗示跨越不同设计空间的通用规律，但数据无法支撑\n- Appendix A.24 中两个架构的 exit-layer R² 差异明显（0.488 vs 0.557），部分削弱 \"convergent\" 论点\n- 建议：弱化为 \"shared tendency\" 或 \"preliminary evidence for convergence\"\n\n**N3** [critical] Finding 3（Token Specialization）是 causal mask 的架构必然结果\n- Image tokens 不可能访问 instruction tokens 的信息——这是 causal mask 的直接推论\n- 论文承认是 \"framework sanity check\" 但在 Abstract 和 Introduction 中仍将其列为三大发现之一\n- 三个 findings 中有一个是 trivial 的，降低了论文的整体可信度\n- 建议：将 Finding 3 明确重新定位为方法论验证，不与 Finding 1/2 并列为 \"findings\"\n\n## Should-Fix 问题\n\n**W1** 相对于近期并发工作（Grant et al. 2026, Häon et al. 2025）的增量贡献不清晰——Grant 提供了可操作的 Action Atlas，Häon 展示了 VLA steering，本文是纯观察性的。\n\n**W2** 报告的效果量极小——训练带来的 ΔR² ≈ 0.03，RSA 最高对齐度 ρ 接近零，核心定量结论建立在微小效果量之上。\n\n**W3** 标题 \"Vision Encodes, Language Reorganizes\" 暗示因果机制，但所有分析工具是观察性/相关性的，无因果干预实验。\n\n**W4** 单一 benchmark (LIBERO) 的泛化性——仅 tabletop manipulation，未在不同 embodiment / 更大规模数据上验证。\n\n## Questions\nQ1. L1 instruction-dominant heads 是否可能是学习率 warmup 的人工产物？\nQ2. 如果移除 Finding 3，剩余两个 findings 是否足以支撑完整 CoRL 论文？\nQ3. 是否有 preliminary 数据表明 L1 entropy 确实与 policy failure 相关？\nQ4. exit-layer R² 差异（0.488 vs 0.557）是否足以质疑 \"convergent\" claim？\n\n## Missing References\n1. Aghajanyan et al. (ACL 2021) — \"Intrinsic Dimensionality Explains the Effectiveness of Language Model Fine-Tuning\"\n2. Kumar et al. (NeurIPS 2022) — \"Fine-Tuning can Distort Pretrained Features and Underperform Out-of-Distribution\"\n3. Tong et al. (NeurIPS 2024) — \"Eyes Wide Shut?\"\n\n## Overall Score: 4/10 (Borderline reject)\n## 置信度: 4/5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "text": "以下是 Reviewer 2 的完整审稿意见，请逐条回应：对每个 Must-Fix 和 Should-Fix 条目，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n# Reviewer 2 完整审稿意见\n\n## Must-Fix 问题\n\n**N1** [critical] CoRL scope fit 严重不足——纯分析无机器人实验验证\n- 无任何机器人实验（模拟或真实）、无 closed-loop policy 评估、无策略改进的实际验证\n- Actionable implications（early-exit inference, L1 entropy monitoring）完全未验证\n- 对比 Häon et al. (CoRL 2025)：该论文被接收因为它实际演示了通过表征方向进行 VLA 行为引导（steering）\n- 纯观察性工作更适合 ICML/NeurIPS 的 interpretability track\n- 建议：至少验证一个 actionable implication\n\n**N2** [critical] N=2 架构不足以支撑 \"convergent reorganization\" 的 claim\n- 两个模型共享关键架构选择：均为 causal decoder、相似规模（3B-7B）、同一 benchmark（LIBERO）、tokenized action 输出\n- \"Convergent\" 暗示跨越不同设计空间的通用规律，但数据无法支撑\n- Appendix A.24 中两个架构的 exit-layer R² 差异明显（0.488 vs 0.557），部分削弱 \"convergent\" 论点\n- 建议：弱化为 \"shared tendency\" 或 \"preliminary evidence for convergence\"\n\n**N3** [critical] Finding 3（Token Specialization）是 causal mask 的架构必然结果\n- Image tokens 不可能访问 instruction tokens 的信息——这是 causal mask 的直接推论\n- 论文承认是 \"framework sanity check\" 但在 Abstract 和 Introduction 中仍将其列为三大发现之一\n- 三个 findings 中有一个是 trivial 的，降低了论文的整体可信度\n- 建议：将 Finding 3 明确重新定位为方法论验证，不与 Finding 1/2 并列为 \"findings\"\n\n## Should-Fix 问题\n\n**W1** 相对于近期并发工作（Grant et al. 2026, Häon et al. 2025）的增量贡献不清晰——Grant 提供了可操作的 Action Atlas，Häon 展示了 VLA steering，本文是纯观察性的。\n\n**W2** 报告的效果量极小——训练带来的 ΔR² ≈ 0.03，RSA 最高对齐度 ρ 接近零，核心定量结论建立在微小效果量之上。\n\n**W3** 标题 \"Vision Encodes, Language Reorganizes\" 暗示因果机制，但所有分析工具是观察性/相关性的，无因果干预实验。\n\n**W4** 单一 benchmark (LIBERO) 的泛化性——仅 tabletop manipulation，未在不同 embodiment / 更大规模数据上验证。\n\n## Questions\nQ1. L1 instruction-dominant heads 是否可能是学习率 warmup 的人工产物？\nQ2. 如果移除 Finding 3，剩余两个 findings 是否足以支撑完整 CoRL 论文？\nQ3. 是否有 preliminary 数据表明 L1 entropy 确实与 policy failure 相关？\nQ4. exit-layer R² 差异（0.488 vs 0.557）是否足以质疑 \"convergent\" claim？\n\n## Missing References\n1. Aghajanyan et al. (ACL 2021) — \"Intrinsic Dimensionality Explains the Effectiveness of Language Model Fine-Tuning\"\n2. Kumar et al. (NeurIPS 2022) — \"Fine-Tuning can Distort Pretrained Features and Underperform Out-of-Distribution\"\n3. Tong et al. (NeurIPS 2024) — \"Eyes Wide Shut?\"\n\n## Overall Score: 4/10 (Borderline reject)\n## 置信度: 4/5"
  }
}
```

</details>

---


### Tool result

_source line 1066 · 2026-05-20T16:36:21.689048+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1460
}
```

</details>

---


### Assistant

_source line 1067 · 2026-05-20T16:36:27.051124+00:00_

交叉分享已发送。等待两位 Reviewer 的逐条回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director"
}
```

</details>

---


## Round 103

## Round 103

2 recorded events


### User

_source line 1068 · 2026-05-20T16:36:29.621567+00:00_

[Reviewer 2 审稿结果]:
审稿完成，已提交给 Review Director。

核心判断：**4/10 (Borderline reject)**。三个主要问题：

1. **CoRL scope fit 严重不足**——纯 representational analysis，无任何机器人实验、无 closed-loop 评估、提出的 actionable implications 全部未验证
2. **N=2 causal-decoder VLA 不足以支撑 "convergent reorganization" 的 claim**——两个架构共享太多设计选择
3. **Finding 3（token specialization）是 causal mask 的架构必然结果**——实际独立贡献缩减为单一观察性发现

建议转投 ICML/NeurIPS interpretability track，或补充实验验证后重投 CoRL。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 1069 · 2026-05-20T16:36:34.236533+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director"
}
```

</details>

---


## Round 104

## Round 104

2 recorded events


### User

_source line 1070 · 2026-05-20T16:38:18.556331+00:00_

[Reviewer 1 审稿意见]:

# Reviewer 1 对 Reviewer 2 审稿意见的逐条回应

---

## Must-Fix 问题

**[AGREE with nuance] R2-N1: CoRL scope fit——纯分析无机器人实验验证**

同意这是本文对 CoRL 的最大风险。论文的确没有 closed-loop 验证或策略改进实验。Discussion (Section 5) 提到的 actionable implications（early-exit inference at ~1/3 depth、L1 entropy monitoring）停留在 "testable hypothesis" 层面。

但需要指出两点 nuance：
1. Reviewer 2 引用 Häon et al. (CoRL 2025) 作为对比标杆，但 Häon 的 steering 实验也是 open-loop representation intervention——并非真正的 closed-loop policy 改进。本文的 L1 head ablation + counterfactual 分析（Section 4.3, Table 5/Table 6）同样是 interventional 的，只是 intervention 目标不同（理解 vs 控制）。
2. CoRL 2023 reviewer guidelines 明确列出 "Significance" 和 "Relevance" 为独立维度，并未要求所有论文包含机器人实验。纯分析性工作如果发现足够深刻，是可以被接收的。问题在于本文的发现是否达到了这个门槛——我认为 borderline。

建议作者至少验证一个 implication（如 L1 attention entropy 与 task failure 的相关性，只需在已有的 LIBERO rollout 数据上计算），成本很低但会显著提升 CoRL relevance。

---

**[AGREE] R2-N2: N=2 架构不足以支撑 "convergent reorganization"**

完全同意。我在自己的审稿意见中也将此列为 critical issue（R1-N3）。两个架构共享过多约束（causal decoder、32 layers、LIBERO benchmark、tokenized actions），Δ=0.003 的 "convergent" R² 在 N=10 bootstrap CI 极宽的前提下（R1-N2）不具说服力。

补充一个 Reviewer 2 提到的具体证据：Appendix A.24 Table 24 的 exit-layer R² 差异确实值得注意——OpenVLA L32 = 0.488 vs TraceVLA L32 = 0.557（Δ=0.069），这个 exit-layer 分歧与 "convergent reorganization" 叙事不一致。论文在 Appendix A.25（line 773）提到 "Exit-layer R² differs (0.488 vs. 0.557), possibly reflecting architectural differences in late-layer processing"，但这个 hedge 不够——如果 mid-layer 收敛但 exit-layer 分歧，那 "convergent" 的范围需要被精确界定。

建议作者弱化为 "shared mid-layer specialization tendency" 并明确 exit-layer 的分歧。

---

**[REBUT] R2-N3: Finding 3（Token Specialization）是 causal mask 的架构必然结果**

Reviewer 2 的论点过于简化。需要区分两个层面：

**(a) Image_mean 保持 chance (10%)——确实是 trivial**。Causal mask 阻止 image tokens 看到 instruction tokens，所以 image_mean 不能分类 instructions。这一点论文自身在 Section 4.2（experiments.tex line 20）承认为 "as predicted by the causal mask"。

**(b) 但 readout token 的三条件梯度不是 trivial**。Causal mask 只保证 readout 能 attend to instruction tokens——它不预测 trained 模型在 L1-L31 全部达到 100% 而 untrained 从 L1 的 100% 衰减到 L31 的 82%（Table 1）。这个衰减模式反映了 randomly initialized 权重在深层逐渐破坏 instruction 信息，是一个关于训练如何保持/维护 instruction signal 的非 trivial 发现。

**(c) 更关键的是，论文的核心 insight 是 image_mean 的 RSA/R² 对训练几乎不变（Δ ≤ 1.7%, Table 13, Appendix A.17），而 readout 的 R² 提升 +0.069（Table 12）**。这不是 causal mask 能预测的——causal mask 只决定 information access，不决定 training 会选择在哪个 token position 上集中改变。训练可以同样改变 image tokens 在被 LLM 处理后的表征结构（through the LLM layers），但事实上没有。

**结论**：Reviewer 2 对 image_mean 结果的批评成立，但将整个 Finding 3 定性为 trivial 是错误的。建议作者在正文中更清晰地将 image_mean at-chance 定位为 "sanity check"，同时强调 readout 的三条件梯度和 training asymmetry 才是真正的 finding。

---

## Should-Fix 问题

**[AGREE with nuance] R2-W1: 相对于并发工作的增量贡献不清晰**

同意论文应更明确地与 Grant et al. (2026) 和 Häon et al. (2025) 定位差异。但 Reviewer 2 的 framing 有偏差——这三篇论文的目标不同：
- Grant: 可视化表征空间（Action Atlas），focus on visualization tool
- Häon: 表征层面的行为引导（steering），focus on intervention
- 本文: token-level 多方法分析 + 跨架构对比，focus on mechanistic understanding

关键差异化：本文的 token-level 粒度（image_mean vs readout 的分离分析）、seven-method convergence 设计、以及跨架构对比在 Grant 和 Häon 中均不存在。建议作者在 Related Work 中增加明确的 "what we add" 段落。

---

**[REBUT] R2-W2: 效果量极小**

Reviewer 2 的表述不准确，存在两处误读：

1. **"RSA 最高对齐度 ρ 接近零"——错误**。DINOv2 cls_token RSA ρ = 0.692（Table 3），VLA trained readout ρ = 0.643，VLA trained image_mean ρ = 0.628。这些都是实质性的正相关，远非"接近零"。Reviewer 2 可能将 *训练带来的变化量*（Δρ = +0.017）与*绝对 RSA 值*混淆了。

2. **"ΔR² ≈ 0.03"——选择性引用**。Image_mean 的 best-vs-best ΔR² = +0.015 确实小（Table 12），但 readout 的 ΔR² = +0.069（p<0.0001, 95% CI [0.047, 0.090]），这是一个中等效应。论文的核心论点恰恰是 training effects 集中在 readout 而非 image tokens——image_mean 的小 Δ 正是 finding 的一部分，不是 weakness。

3. 此外，ablation 和 counterfactual 的效应量很大：dose-response d = 0.482→0.639（Table 5）；counterfactual d = 0.625→0.968（Table 6）；trajectory-level d = 2.943（Appendix A.7）。这些不是"微小效果量"。

不过，我在自己的审稿意见（R1-N1）中指出 Cohen's d 的配对假设可能导致效应量被高估，所以真实效应量可能比报告值小。但即使打折，dose-response 和 counterfactual 的效应仍然实质性的。

---

**[REBUT] R2-W3: 标题暗示因果但分析是观察性的**

论文包含多项 **interventional** 分析：
- L1 head ablation（Section 4.3）：移除 4-32 个 instruction-dominant heads，观察动作序列变化
- Counterfactual instruction analysis（Table 6）：替换 instruction 为 empty/wrong/paraphrased/shuffled
- Random-subset specificity control（Appendix A.7）：30 组随机 head ablation vs instruction-dominant ablation
- Matched-size ablation（Appendix A.23, Table 23）：4 组 24-head ablation 控制实验

这些都是因果干预——改变输入或模型结构，观察输出变化。虽然不是 do-calculus 意义上的完全因果推断（我在 R1-W2 中指出了 ablation 仅证明 necessity 而非 sufficiency），但将论文定性为"无因果干预实验"不符合事实。

---

**[AGREE] R2-W4: 单一 benchmark 的泛化性**

同意，与我的审稿意见（R1-W4）一致。LIBERO 的 tabletop manipulation 特性可能是多个发现的充分条件。

---

## Questions

**Q1: L1 instruction-dominant heads 是否可能是学习率 warmup 的人工产物？**

有趣的问题。但论文的 three-condition comparison 提供了部分控制：Llama-2 base（未经 VLA 训练，无 warmup 影响）已有 9/32 instruction-dominant heads（Table 2, Section 4.3），而 VLA training 增加到 24/32。如果 warmup 是原因，Llama-2 base 不应有 9/32 heads。更可能的解释是 language pretraining 播种了部分 instruction attention，VLA fine-tuning 在此基础上放大。但要彻底排除需要 ablate warmup schedule 的控制实验。

**Q2: 移除 Finding 3 后剩余两个 findings 是否足够？**

我认为 Finding 1（attention redistribution to entry-exit layers, 支撑 evidence: 三条件梯度、dose-response、counterfactual）和 Finding 2（non-monotonic vision refinement, 支撑 evidence: RSA inverted-U、cross-benchmark replication、probe convergence）加上跨架构对比的初步证据，构成了一篇 solid analysis paper 的内容。关键取决于 cross-architecture claim 被弱化到何种程度（R2-N2/R1-N3）。

**Q3: L1 entropy 与 policy failure 的 preliminary 数据？**

论文中无此数据。这是我也建议验证的 actionable implication（见 R2-N1 回应）。

**Q4: Exit-layer R² 差异是否足以质疑 "convergent" claim？**

是的。OpenVLA L32 R² = 0.488 vs TraceVLA L32 R² = 0.557（Δ=0.069）是一个 non-trivial 差异，超过了 mid-layer convergence 的 Δ=0.003。收敛仅限于 mid-layer 而 exit-layer 分歧，说明 "convergent reorganization" 的范围需要精确限定。

---

## Missing References 回应

1. **Aghajanyan et al. (ACL 2021) — Intrinsic Dimensionality**：同意应引用。论文的 inverted-U pattern 与低秩适应有关联，intrinsic dimensionality 可能为 mid-layer specialization 提供理论解释。
2. **Kumar et al. (NeurIPS 2022) — Fine-Tuning Distortion**：同意。与论文的 "vision encodes, language reorganizes" narrative 直接相关——fine-tuning 可能扭曲预训练特征。
3. **Tong et al. (NeurIPS 2024) — Eyes Wide Shut?**：Relevant 但非必要。主要关于 VLM 的 vision 能力缺陷，与本文的 token-level analysis 间接相关。

---

## 总结

与 Reviewer 2 的核心分歧在两个点：
1. **R2-N3（Finding 3 trivial）**：Reviewer 2 过度简化了 causal mask 的预测力。Image_mean at-chance 是 trivial，但 readout 三条件梯度和 training asymmetry 不是。
2. **R2-W2（效果量极小）**：Reviewer 2 混淆了绝对 RSA 值和训练变化量，且忽略了 ablation/counterfactual 的大效应量。

在 N1（scope fit）和 N2（N=2 architecture）上与 Reviewer 2 一致，这两点也是我自己审稿中的 concerns。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 1071 · 2026-05-20T16:38:24.103379+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director"
}
```

</details>

---


## Round 105

## Round 105

4 recorded events


### User

_source line 1072 · 2026-05-20T16:38:26.676999+00:00_

[Reviewer 1 审稿结果]:
已提交对 Reviewer 2 的逐条回应。核心分歧点：

- **R2-N3（Finding 3 trivial）**：[REBUT] — image_mean at-chance 确实是 causal mask 的 trivial 结果，但 readout 三条件梯度（trained 100% vs untrained 82% at L31）和 training asymmetry（readout ΔR²=+0.069 vs image_mean Δ≤1.7%）不是 causal mask 能预测的。
- **R2-W2（效果量极小）**：[REBUT] — Reviewer 2 混淆了绝对 RSA 值（ρ=0.692）与训练变化量（Δρ=0.017），且忽略了 ablation/counterfactual 的大效应量（d=0.48-0.97）。
- **R2-N1（scope）和 R2-N2（N=2 架构）**：[AGREE] — 与我自己的审稿意见一致。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 1073 · 2026-05-20T16:38:50.675516+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "以下是 Reviewer 1 对你审稿意见的逐条回应。请对 Reviewer 1 的每个 [REBUT] 条目进行二次回应：[AGREE] 接受 R1 的反驳理由，或 [MAINTAIN] 维持你的原始立场并补充论据。对 [AGREE] 和 [AGREE with nuance] 条目只需简要确认。\n\n---\n\n# Reviewer 1 的交叉回应\n\n## R2-N1 (CoRL scope fit): [AGREE with nuance]\nR1 同意这是最大风险，但指出两点 nuance：\n1. Häon et al. (CoRL 2025) 的 steering 实验也是 open-loop representation intervention，并非真正 closed-loop\n2. CoRL reviewer guidelines 未要求所有论文包含机器人实验\nR1 建议至少验证一个 implication（如 L1 entropy vs task failure 的相关性，只需在已有 LIBERO rollout 数据上计算）。\n\n## R2-N2 (N=2 架构): [AGREE]\nR1 完全同意。补充指出 Appendix A.24 的 exit-layer R² 差异（OpenVLA 0.488 vs TraceVLA 0.557, Δ=0.069）与 mid-layer convergence (Δ=0.003) 形成矛盾，\"convergent\" 范围需要精确界定。建议弱化为 \"shared mid-layer specialization tendency\"。\n\n## R2-N3 (Finding 3 trivial): [REBUT]\nR1 认为你的论点过于简化，区分三个层面：\n(a) Image_mean at-chance (10%) 确实是 trivial（causal mask 的直接结果）\n(b) 但 readout 三条件梯度不是 trivial——causal mask 保证 readout 能 attend to instruction，但不预测 trained 在 L1-L31 全 100% 而 untrained 从 100% 衰减到 82%\n(c) 更关键的是，training asymmetry（readout ΔR²=+0.069 vs image_mean Δ≤1.7%）不是 causal mask 能预测的——训练可以同样改变 image tokens 的表征结构，但事实上没有\nR1 建议将 image_mean at-chance 定位为 sanity check，同时强调 readout 梯度和 training asymmetry 才是真正发现。\n\n## R2-W1 (增量贡献不清晰): [AGREE with nuance]\nR1 同意应更明确定位差异，但指出 Grant/Häon/本文目标不同（visualization tool / intervention / mechanistic understanding），token-level 粒度和 seven-method convergence 设计在前两者中不存在。\n\n## R2-W2 (效果量极小): [REBUT]\nR1 指出你的表述存在两处误读：\n1. \"RSA 最高对齐度 ρ 接近零\" 是错误的——DINOv2 cls RSA ρ=0.692，远非接近零\n2. \"ΔR² ≈ 0.03\" 是选择性引用——readout ΔR²=+0.069 (p<0.0001)，这是中等效应\n3. Ablation/counterfactual 效应量很大：dose-response d=0.48-0.64, counterfactual d=0.63-0.97, trajectory-level d=2.943\nR1 同意 Cohen's d 的配对假设问题可能导致高估（R1-N1），但即使打折仍实质性的。\n\n## R2-W3 (标题暗示因果): [REBUT]\nR1 指出论文包含多项 interventional 分析：L1 head ablation、counterfactual instruction、random-subset control、matched-size ablation——将论文定性为\"无因果干预实验\"不符合事实。\n\n## R2-W4 (单一 benchmark): [AGREE]\n\n## Missing References: \nR1 同意应引用 Aghajanyan et al. (ACL 2021) 和 Kumar et al. (NeurIPS 2022)。Tong et al. relevant 但非必要。\n\n---\n\n请针对 R1 的三个 REBUT（R2-N3, R2-W2, R2-W3）给出你的二次回应。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "text": "以下是 Reviewer 1 对你审稿意见的逐条回应。请对 Reviewer 1 的每个 [REBUT] 条目进行二次回应：[AGREE] 接受 R1 的反驳理由，或 [MAINTAIN] 维持你的原始立场并补充论据。对 [AGREE] 和 [AGREE with nuance] 条目只需简要确认。\n\n---\n\n# Reviewer 1 的交叉回应\n\n## R2-N1 (CoRL scope fit): [AGREE with nuance]\nR1 同意这是最大风险，但指出两点 nuance：\n1. Häon et al. (CoRL 2025) 的 steering 实验也是 open-loop representation intervention，并非真正 closed-loop\n2. CoRL reviewer guidelines 未要求所有论文包含机器人实验\nR1 建议至少验证一个 implication（如 L1 entropy vs task failure 的相关性，只需在已有 LIBERO rollout 数据上计算）。\n\n## R2-N2 (N=2 架构): [AGREE]\nR1 完全同意。补充指出 Appendix A.24 的 exit-layer R² 差异（OpenVLA 0.488 vs TraceVLA 0.557, Δ=0.069）与 mid-layer convergence (Δ=0.003) 形成矛盾，\"convergent\" 范围需要精确界定。建议弱化为 \"shared mid-layer specialization tendency\"。\n\n## R2-N3 (Finding 3 trivial): [REBUT]\nR1 认为你的论点过于简化，区分三个层面：\n(a) Image_mean at-chance (10%) 确实是 trivial（causal mask 的直接结果）\n(b) 但 readout 三条件梯度不是 trivial——causal mask 保证 readout 能 attend to instruction，但不预测 trained 在 L1-L31 全 100% 而 untrained 从 100% 衰减到 82%\n(c) 更关键的是，training asymmetry（readout ΔR²=+0.069 vs image_mean Δ≤1.7%）不是 causal mask 能预测的——训练可以同样改变 image tokens 的表征结构，但事实上没有\nR1 建议将 image_mean at-chance 定位为 sanity check，同时强调 readout 梯度和 training asymmetry 才是真正发现。\n\n## R2-W1 (增量贡献不清晰): [AGREE with nuance]\nR1 同意应更明确定位差异，但指出 Grant/Häon/本文目标不同（visualization tool / intervention / mechanistic understanding），token-level 粒度和 seven-method convergence 设计在前两者中不存在。\n\n## R2-W2 (效果量极小): [REBUT]\nR1 指出你的表述存在两处误读：\n1. \"RSA 最高对齐度 ρ 接近零\" 是错误的——DINOv2 cls RSA ρ=0.692，远非接近零\n2. \"ΔR² ≈ 0.03\" 是选择性引用——readout ΔR²=+0.069 (p<0.0001)，这是中等效应\n3. Ablation/counterfactual 效应量很大：dose-response d=0.48-0.64, counterfactual d=0.63-0.97, trajectory-level d=2.943\nR1 同意 Cohen's d 的配对假设问题可能导致高估（R1-N1），但即使打折仍实质性的。\n\n## R2-W3 (标题暗示因果): [REBUT]\nR1 指出论文包含多项 interventional 分析：L1 head ablation、counterfactual instruction、random-subset control、matched-size ablation——将论文定性为\"无因果干预实验\"不符合事实。\n\n## R2-W4 (单一 benchmark): [AGREE]\n\n## Missing References: \nR1 同意应引用 Aghajanyan et al. (ACL 2021) 和 Kumar et al. (NeurIPS 2022)。Tong et al. relevant 但非必要。\n\n---\n\n请针对 R1 的三个 REBUT（R2-N3, R2-W2, R2-W3）给出你的二次回应。"
  }
}
```

</details>

---


### Tool result

_source line 1074 · 2026-05-20T16:38:54.393456+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 3717
}
```

</details>

---


### Assistant

_source line 1075 · 2026-05-20T16:38:57.542187+00:00_

交叉分享第二轮已发出。等待 Reviewer 2 对 R1 三个 REBUT 点的二次回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director"
}
```

</details>

---


## Round 106

## Round 106

2 recorded events


### User

_source line 1076 · 2026-05-20T16:40:11.283470+00:00_

[Reviewer 2 审稿意见]:

# Reviewer 2 对 Reviewer 1 审稿意见的逐条回应

---

## Must-Fix 问题

### [REBUT] R1-N1: Cohen's d 独立性假设违反——效应量可能被高估

R1 的方法论关注点（paired data 应使用 paired effect size）是合理的，但其关于**偏差方向**的判断有误。

R1 声称 "pooled SD 高估、d 值被系统性抬升"。实际情况恰好相反：

- 配对数据中，两组共享输入，产出高度正相关（r >> 0）
- Var(X−Y) = Var(X) + Var(Y) − 2·Cov(X,Y)，因此 SD_diff < SD_pooled
- paired Cohen's d_z = mean_diff / SD_diff > standard d = mean_diff / SD_pooled

即：当改用 R1 建议的 paired d_z 后，效应量应**变大而非变小**。论文当前使用的标准 Cohen's d 实际上是对效应量的**保守估计**。

这意味着 R1 的核心担忧（"效应量被高估"）在数学上不成立。使用正确的 paired 统计方法只会**强化**论文的结论，不会削弱。

我仍同意论文应在方法学上更严谨——报告 paired d_z 和配对相关系数 r 是更好的做法（Table 5, Table 6, Appendix A.7）。但这属于 **Should-Fix 级别的方法论完善**，不构成 critical issue，因为修正后结论只会更强。

### [AGREE] R1-N2: N=10 tasks 下 RSA 的统计功效不足

同意。这与我自己的 W2 concern 一致。

具体补充：
- Table 3 中 RSA ρ 最高值仅 0.02（DINOv2 untrained），训练效应 Δ 在 LIBERO-Goal 上 +0.017（不显著）、LIBERO-Spatial 上 +0.023（p<0.001）——两者仅差 0.006，但显著性截然不同，说明 N=10 下结果对样本选择高度敏感
- Section 4.4 中跨架构 RSA Δ=0.003 的 CI 重叠被解读为 "convergent"，但在 N=10 下 CI 宽度本身就足以制造虚假重叠
- R1 建议的 TOST 等价性检验尤其重要——CI 重叠不等于等价性

补充一个 R1 未提及的问题：Table 3 footnote 承认 RSA ρ 值在高维空间中本来就预期很低，这实际上暗示 RSA 可能不是评估此类表征变化的最佳工具，但论文并未讨论这一 methdological implication。

### [AGREE] R1-N3: 跨架构对比混杂变量——"convergent reorganization" claim 过强

完全同意。这与我的 N2 相互印证。

R1 准确识别了混杂变量的完整列表：backbone 架构、pretraining data、vision encoder、instruction tuning 状态、训练 task 数量。我的 N2 侧重于 N=2 的样本量不足问题，R1 进一步指出了 confound 问题——两者是互补的。

补充 R1 未明确提及的一点：Appendix A.24（Table 24, p.29）的 cross-architecture 对比实际上部分**削弱**了 convergent claim：
- Exit-layer R²：OpenVLA 0.488 vs TraceVLA 0.557（差异 0.069，非 trivial）
- Peak layer：OpenVLA L12 vs TraceVLA "L8"（不同层）
- Profile shape：OpenVLA 有 flat plateau，TraceVLA 有更尖锐的 mid-layer peak

这些差异在 Table 24 的数据中清晰可见，但 Section 4.3 的叙述选择性地强调了相似性（"both reach similar mid-layer action decodability peaks"），淡化了差异。

R1 建议的 "suggestive evidence" 表述比 "convergent reorganization" 更准确。

---

## Should-Fix 问题

### [AGREE] R1-W1: 多重比较校正范围不充分

同意。论文在每个 metric 的 33 层内做 FDR 校正，但全文涉及至少 4 种分析方法 × 多个 token 类型 × 多个条件对比，global family-wise error rate 未被控制。

不过这在 ML interpretability 文献中是常见做法（很少有论文做跨分析的全局校正），严格来说是一个 should-fix 而非 critical issue。论文可以在 Appendix 中添加 Bonferroni-adjusted 全局 p-values 作为 robustness check。

### [AGREE] R1-W2: L1 head ablation 的因果推断力被过度表述

同意。

Appendix A.23（Table 23, p.28）的 matched-size ablation 结果确实显示 instruction-dominant heads 的 Cohen's d 仅比 random heads 的 Cohen's d 大一个有限的 margin。具体来看，Table 23 中 Instruction-dominant (24 heads) 的 Cohen's d 与 Direction-selective (24 heads) 的 Cohen's d 相差不大。

更关键的是：ablation 本身只能说明某些 heads 对输出有影响，但不能直接支撑 "instruction attention at L1 is functionally critical" 的因果声明。Ablation 会同时破坏这些 heads 承载的所有功能（不仅是 instruction processing），所以效应不能完全归因于 instruction processing。

### [REBUT] R1-W3: RSA vs CKA 反转的处理

部分反驳。

R1 认为论文 "仅用 'different geometric properties' 一笔带过"。但 Appendix A.1（p.12-13）实际上提供了比 R1 描述的更多讨论：论文解释了 CKA 对 global scale 敏感而 RSA 对 local pairwise 距离保序敏感，两者测量的是不同的表征几何属性。论文选择 RSA 作为主分析工具并给出了合理的方法论理由（RSA 对 task-discriminative structure 更直接相关）。

**但我同意 R1 的底层关切是合理的**：当两个标准 metric 给出相反结论时，论文应该更明确地讨论这意味着什么——是 RSA 更可靠、还是表征变化本身是多面的？当前论文选择了对自己叙事更有利的 metric 而未充分讨论另一个 metric 为何给出不同答案。

总结：R1 对 Appendix A.1 内容的概括 ("一笔带过") 不完全准确，但其核心关切（metric 选择的 principled justification 不足）是成立的。

### [AGREE] R1-W4: 仅 LIBERO 生态系统评估

完全同意，与我的 W4 一致。Appendix A.14 在 LIBERO-Spatial 上的验证仍属同一 benchmark family，不构成真正的 generalization check。

### [AGREE] R1-W5: Counterfactual instruction analysis n=4 统计功效

同意。Section 4.5 使用 4 种 perturbation types（empty, wrong task, paraphrased, shuffled），Spearman ρ = 1.0 在 n=4 时 p = 0.042，这在任何严格标准下都是 marginal 的。

需要补充的是：即使排除 Spearman 相关，counterfactual analysis 本身的定性结论（替换指令后动作改变、不同 perturbation 类型影响不同 token 类型）仍然有 informative value。但论文不应用 ρ = 1.0 的统计检验来支撑因果推断。

### [AGREE] R1-W6: 单一训练 checkpoint

同意，但这是 ML interpretability 领域的普遍局限。Grant et al. (2026)、Häon et al. (2025) 等近期工作同样使用单一 checkpoint。论文应在 Limitations 中明确提及 seed variance 的潜在影响。

---

## 小问题回应

**R1-Minor-1（"readout token" vs "last_preaction" 术语不一致）**: [AGREE] 这确实是写作问题，但我在自己的审稿中未将其视为 significant issue。论文应统一术语。

**R1-Minor-2（Footnote 1 两个 R² 值差异未解释）**: [AGREE] 合理关注，应补充说明。

**R1-Minor-3（Permutation test 仅 1,000 shuffles）**: [AGREE] 对于 p-value 精度要求较高的场景，1,000 shuffles 确实不够。建议增加到 10,000。

**R1-Minor-4（Untrained model L1 100% classification 弱化叙事）**: [AGREE] 这是一个重要观察。Table 1 显示 untrained readout 在 L1 也达到 100% cross-instruction classification accuracy，这意味着 instruction discriminability at L1 是 pretrained backbone 的固有属性，而非 VLA fine-tuning 的产物。这进一步弱化了 Finding 3 的新颖性，也与我的 N3（Finding 3 是架构必然结果）互相支撑。

**R1-Minor-5（Leave-one-out p ≤ 0.083 不应称 "robust"）**: [AGREE] p = 0.083 按任何常规标准都不能称为 robust。

---

## 综合评估

R1 的审稿在统计方法论层面非常细致，我的审稿在 CoRL scope fit 和新颖性层面进行了更深入的评估。两份审稿在以下关键问题上高度一致：

| 问题 | R1 | R2 | 判断 |
|------|----|----|------|
| "Convergent" claim 过强 | N3 (混杂变量) | N2 (N=2 不足) | 一致：互补角度 |
| RSA 效果量极小 | N2 (power 不足) | W2 (实际意义存疑) | 一致 |
| 单一 benchmark | W4 | W4 | 一致 |
| Finding 3 trivial | Minor-4 (untrained L1=100%) | N3 (causal mask 必然) | 一致 |

唯一分歧是 R1-N1（Cohen's d 方向）：R1 认为效应量被高估，我认为根据数学推导，paired d_z 只会更大——当前论文的报告是保守的。这个分歧不影响论文的总体评价，但将 R1-N1 从 critical 降级为 should-fix 是合理的。

我维持 **4/10 (Borderline reject)** 的评分。R1 给出 6/10——我认为差异主要来自 R1 未将 CoRL scope fit 视为核心问题。如果此文投稿 ICML/NeurIPS interpretability track，我的评分会提升到 5-6/10。



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 1077 · 2026-05-20T16:40:16.604049+00:00_

收到 Reviewer 2 的二次回应。现在等待 Reviewer 2 对 Reviewer 1 三个 REBUT 点的回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director"
}
```

</details>

---


## Round 107

## Round 107

2 recorded events


### User

_source line 1078 · 2026-05-20T16:40:32.709598+00:00_

[Reviewer 2 审稿结果]:
交叉回应已提交。总结：

- R1 的 3 个 Must-Fix 中，**N2（RSA power）和 N3（convergent claim）完全同意**，与我的审稿互补；**N1（Cohen's d）反驳了偏差方向**——R1 声称效应量被高估，但数学上 paired d_z 只会更大，当前报告实际上是保守的，建议降级为 Should-Fix
- R1 的 6 个 Should-Fix 中，**5 个同意**（W1 多重比较、W2 L1 ablation、W4 LIBERO-only、W5 counterfactual n=4、W6 单 checkpoint），**W3（RSA vs CKA）部分反驳**——论文在 Appendix A.1 的讨论比 R1 描述的更详细，但核心关切成立
- 两份审稿在 "convergent" claim 过强、RSA 效果量小、Finding 3 trivial 三个关键问题上高度一致

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 1079 · 2026-05-20T16:41:24.543199+00:00_

收到 R2 对 R1 审稿意见的交叉回应。等待 R2 对 R1 三个 REBUT 点（R2-N3, R2-W2, R2-W3）的二次回应后，进入收敛判断和报告合成。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director"
}
```

</details>

---


## Round 108

## Round 108

104 recorded events


### User

_source line 1080 · 2026-05-20T16:44:31.798551+00:00_

[Reviewer 2 审稿意见]:

# Reviewer 2 对 Reviewer 1 交叉回应的二次回应

---

## 已达成共识的条目（简要确认）

**R2-N1 (CoRL scope fit)**: [AGREE with nuance] — 确认。R1 指出 Häon et al. 的 steering 也是 open-loop 是合理的 nuance，但这不改变核心问题：Häon 至少展示了 representation intervention 改变行为的实验，本文连这一步也没有。同意 R1 建议的最低修改方案（在已有 rollout 数据上计算 L1 entropy vs task failure 相关性）是可行且低成本的。

**R2-N2 (N=2 架构)**: [AGREE] — 确认。R1 补充的 exit-layer Δ=0.069 vs mid-layer Δ=0.003 矛盾进一步强化了弱化 claim 的必要性。

**R2-W1 (增量贡献)**: [AGREE with nuance] — 确认。接受 R1 关于 token-level 粒度和 multi-method convergence 设计的差异化论点。

**R2-W4 (单一 benchmark)**: [AGREE] — 确认。

**Missing References**: 确认。

---

## 对 R1 三个 REBUT 的二次回应

### R2-N3 (Finding 3 trivial): [AGREE] — 接受 R1 的反驳，修正我的立场

R1 的三层分解很有说服力，我原始的 "完全是架构必然结果" 表述过于笼统。逐层回应：

**(a) Image_mean at-chance (10%)**：双方一致认为 trivial。无分歧。

**(b) Readout 三条件梯度**：R1 指出 causal mask 保证 readout CAN attend to instruction，但不预测 trained 在 L1-L31 全部 100% 而 untrained 从 100% 衰减到 82%（Table 1, p.5）。我接受这一区分——causal mask 定义了信息访问的上限，但并不预测不同训练状态下 instruction discriminability 如何随层深度变化。Untrained 模型在深层"丢失" instruction identity 是一个需要解释的现象。

**(c) Training asymmetry (readout ΔR²=+0.069 vs image_mean Δ≤1.7%)**：这是 R1 反驳中最有力的论点。我原本认为这是 causal mask 的间接推论（image tokens 无法访问 instruction → 训练信号自然聚焦于 readout）。但 R1 正确指出：训练可以通过 vision encoder fine-tuning 改变 image tokens 的表征结构（使其更适合 action prediction），但实际上 image_mean 的 action probe R² 变化极小。这说明 VLA fine-tuning 选择性地将 action-relevant 表征变化集中在 readout token，而非均匀分布——这不是 causal mask 能直接预测的。

**修正后的立场**：我撤回 "Finding 3 完全是架构必然结果" 的判断。将我的 N3 降级为 Should-Fix 级别：建议论文将 image_mean at-chance 明确标注为 sanity check，同时将 readout 梯度差异和 training asymmetry 作为 Finding 3 的实质内容重新定位。当前 Abstract 中 "Third, token-level analysis confirms expected functional specialization" 的措辞仍然太弱——它暗示结果是 "expected" 的，而 R1 识别的 (b)(c) 恰恰是 non-trivial 的部分，应该在 Abstract 中更精准地表述。

---

### R2-W2 (效果量极小): [AGREE] — 接受 R1 的大部分反驳，承认我的引用有选择性偏差

R1 对我的 W2 提出了三处具体指正：

**关于 readout ΔR²**：R1 指出 readout ΔR² = +0.069（p<0.0001），而我引用的 "ΔR² ≈ 0.03" 来自 Section 4.3 对跨架构平均值的概述。重新检查 p.5 Section 4.3 原文确认 readout ΔR² = 0.069 是准确数字。我原始引用确实有 selective quoting 问题——选择了较小的汇总数字而非更具代表性的 readout-specific 值。

**关于 ablation/counterfactual 效应量**：R1 列举的 dose-response d = 0.48–0.64（Table 5, p.16）、counterfactual d = 0.63–0.97（Table 6）、trajectory d = 2.943 确实是实质性效应。我的 W2 完全忽略了这些 ablation 效应量，仅聚焦于 RSA ρ 和 probe R²——这构成了选择性偏差。

**关于 RSA ρ = 0.692**：这一点我需要指出 R1 可能存在引用错误。重新检查 Table 3（p.7）和论文正文，Section 4.4 明确写道 "DINOv2 achieves the highest geometric RSA (ρ = 0.022)"，且 Table 3 caption 标注 "RSA (ρ = 0.02)"。R1 引用的 0.692 很可能来自 Table 3 的 probe R² 列而非 RSA ρ 列——即 R1 在这一具体数字上混淆了两个不同的 metric。RSA with action space 的 ρ 确实在 0.02 量级，我关于此 specific metric 的原始表述是准确的。

**修正后的立场**：我撤回 W2 中 "效果量极小" 的全面性表述。论文的 ablation/counterfactual 分析确实展示了实质性效应量。我保留对 RSA ρ（with action space）实际意义的关切——ρ ≈ 0.02 即使统计显著也接近噪音水平——但承认这只是论文多条证据链中的一条，不能用它来概括全文的效果量。

---

### R2-W3 (标题暗示因果): [AGREE] — 接受 R1 的反驳，撤回原始表述

R1 正确指出论文包含多项 interventional 分析：
- L1 head ablation（移除特定 heads 观察输出变化）→ 因果干预
- Counterfactual instruction replacement（替换指令测量输出变化）→ 因果干预
- Random-subset control → 对照实验
- Matched-size ablation → 控制变量

我原始表述 "论文的所有分析工具都是观察性/相关性的" 和 "没有做因果干预实验" 不符合事实。论文的 ablation 和 counterfactual 实验在方法论上确实属于 interventional 分析。

**撤回原始 W3**。

不过我保留一个弱化版本的关切（降级为 minor comment）：论文的干预实验验证了 "某些 attention heads/instruction tokens 对输出有影响"，但这与标题 "Vision Encodes, Language Reorganizes" 所暗示的 division-of-labor 因果机制之间仍有逻辑间隙。例如，没有实验直接测试 "如果阻断 vision encoding 而保留 language reorganization，会发生什么"。但这更多是未来工作方向，不构成论文的缺陷。

---

## 评分更新

基于以上修正：
- N3 从 critical 降级为 should-fix（接受 R1 的三层分解）
- W2 撤回全面性表述（保留对 RSA-to-action ρ 的局部关切）
- W3 撤回（接受论文有 interventional 分析）

**修正后评分：5/10（Borderline reject → Marginally below acceptance threshold）**

原始 4/10 → 5/10 的提升反映了：N3 不再是 critical issue，W2/W3 的 severity 降低。但 N1（CoRL scope fit）和 N2（N=2 架构）仍然是核心问题，维持在 critical 级别。



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 1081 · 2026-05-20T16:44:51.304043+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "vla-ssd"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "vla-ssd"
  }
}
```

</details>

---


### Tool result

_source line 1082 · 2026-05-20T16:44:51.505307+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"pending\", \"paper_pdf_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/main.pdf\", \"venue\": \"CoRL 2026\", \"requested_at\": \"2026-05-20T16:25:06.450403+00:00\", \"reminder_hours\": 8, \"chat_id\": \"oc_a1d032cbe70bdd2058438e67e0d57613\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 1083 · 2026-05-20T16:44:51.556104+00:00_

called mcp__agent-ml-research__get_visual_check_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_visual_check_status</summary>

```json
{
  "project": "vla-ssd"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "tool_args": {
    "project": "vla-ssd"
  }
}
```

</details>

---


### Tool result

_source line 1084 · 2026-05-20T16:44:51.607402+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"done\", \"started_at\": \"2026-05-20T16:25:07.686822+00:00\", \"completed_at\": \"2026-05-20T16:28:13.626726+00:00\", \"findings\": [{\"severity\": \"info\", \"dimension\": \"page 1\", \"message\": \"Figure 1 占页面顶部约 40%，提供强视觉锚点（架构图 + 注意力热力图 + 柱状图）。Title/Author/Abstract 排版整洁，匿名格式规范。第一个 display item 有效传达核心 message（VLA fine-tuning 重新分配 instruction attention 到 entry-exit layers）。首页印象良好。\"}, {\"severity\": \"warning\", \"dimension\": \"pages 2-4\", \"message\": \"连续 3 页纯文本（Related Work + Method），无任何 figure/table/display equation 穿插。审稿人在此区间容易失去注意力。建议：在 Method 部分加入一个 pipeline/framework 概览图，或将部分 probe 定义用 display equation 形式化展示以打破纯文本节奏。\"}, {\"severity\": \"info\", \"dimension\": \"page 5\", \"message\": \"Table 1 出现，打破了前序纯文本节奏。表格使用 booktabs 风格，最优值加粗标注，格式规范。底部有脚注说明数值差异来源，审慎。\"}, {\"severity\": \"info\", \"dimension\": \"page 6\", \"message\": \"该页为密集结果段落，大量数字内嵌在正文中（p-values、accuracy、percentages）。虽无 display item，但紧邻 Table 1（上一页）和 Table 2 + Figure 2（下一页），节奏尚可接受。\"}, {\"severity\": \"info\", \"dimension\": \"page 7\", \"message\": \"Table 2（Instruction attention at L1）+ Figure 2（instruction-dominant attention heads 分布）同页，密度适当。Figure 2 的柱状图颜色可区分，图例清晰。\"}, {\"severity\": \"info\", \"dimension\": \"page 8\", \"message\": \"Table 3（RSA ρ and probe R² alignment）+ Figure 3（Per-layer RSA 曲线）。Figure 3 的线条有虚实区分（trained vs. untrained），legend 清晰，置信区间有阴影标注。\"}, {\"severity\": \"info\", \"dimension\": \"page 9\", \"message\": \"Discussion + Conclusion 段落后 references 开始。页面利用率约 100%，无异常空白。Limitations 段简洁但存在。\"}, {\"severity\": \"info\", \"dimension\": \"pages 10-12\", \"message\": \"References 页。未见 [?] 未解析引用。格式基本一致（author 缩写、arXiv preprint 标注）。单栏排版下 references 页数合理。\"}, {\"severity\": \"info\", \"dimension\": \"page 12\", \"message\": \"末尾有 \\\"Use of Generative AI\\\" 声明段落，符合近年顶会要求。\"}, {\"severity\": \"info\", \"dimension\": \"page 13\", \"message\": \"Appendix 起始页。Figure 4（三种相似性度量对比，3 子图横排）出现。子图横排合理利用全宽，CKA/Linear CKA/RDM Kernel CKA 
…[truncated 3110 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 1085 · 2026-05-20T16:49:29.358575+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "vla-ssd",
  "issues_yaml": "issues:\n  # ============================================================\n  # Round 1-8 历史 issues（全部 resolved，压缩保留）\n  # ============================================================\n  - id: R1-N1-old\n    summary: \"Untrained baseline 无法隔离 VLA fine-tuning vs Llama-2 语言预训练的贡献\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    resolution: \"三条件数据完整整合。\"\n    resolution_round: 3\n    mentions: []\n    action_items: []\n  - id: R1-N2-old\n    summary: \"单一模型 Title/Abstract 使用复数 'VLAs' 构成 overclaim\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    resolution: \"Title 改为单数。\"\n    resolution_round: 3\n    mentions: []\n    action_items: []\n  - id: R1-N4-old\n    summary: \"Design implications 完全基于 correlational evidence\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    resolution: \"Abstract 使用 hedge 语气。\"\n    resolution_round: 3\n    mentions: []\n    action_items: []\n  - id: R1-N3-old\n    summary: \"RSA best-vs-best selection bias\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    resolution: \"Same-layer comparison 为 primary evidence。\"\n    resolution_round: 3\n    mentions: []\n    action_items: []\n  - id: R2-N1-old\n    summary: \"Neo et al. (ICLR 2025) 未引用\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    resolution: \"已引用。\"\n    resolution_round: 3\n    mentions: []\n    action_items: []\n  - id: R2-W1-old\n    summary: \"Related Work 引用覆盖度不足\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    resolution: \"引用数量达标。\"\n    resolution_round: 3\n    mentions: []\n    action_items: []\n  - id: R1-W1-old\n    summary: \"'Instruction-blind' claim 过强\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    resolution: \"MLP probe 双重验证。\"\n    resolution_round: 3\n    mentions: []\n    action_items: []\n  - id: R1-W2-old\n    summary: \"CKA 反转 RSA 排序处理不充分\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    resolution: \"Method 新增 'Why RSA over CKA'。\"\n    resolution_round: 2\n    mentions: []\n    action_items: []\n  - id: R3-N1-old\n    summary: \"Limitations 格式\"\n    category: format\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    resolution: \"改为 subsection。\"\n    resolution_round: 3\n    mentions: []\n    action_items: []\n  - id: R3-N2-old\n    summary: \"em-dash AI 写作标志\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    resolution: \"零残留。\"\n    resolution_round: 2\n    mentions: []\n    action_items: []\n  - id: R3-W5-old\n    summary: \"无 code/data 释放声明\"\n    category: format\n    severity: info\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    resolution: \"Conclusion 加声明。\"\n    resolution_round: 3\n    mentions: []\n    action_items: []\n\n  # ============================================================\n  # Round 4-8 issues（全部 resolved）\n  # ============================================================\n  - id: R4-N1\n    summary: \"C1 是 causal mask 必然结果 + probe trivially easy\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 14\n    resolution: \"Abstract 'confirms expected' + 'consistent with causal attention mask' + 'framework sanity check' 三重降格。Contribution (iii) 定位为 methodology validation。全文一致。\"\n    resolution_round: 13\n    mentions:\n      - round: 9\n        reviewers: [1, 2]\n        note: \"R9-W2: C1 在 Abstract/Introduction 占比失衡。\"\n      - round: 10\n        reviewers: [1, 2]\n        note: \"RESOLVED。降格处理到位。\"\n      - round: 12\n        reviewers: [2, 3]\n        note: \"复发。R2-N1: 虽已降为 sanity check，但 Title 和 Abstract 仍将架构约束呈现为核心贡献。\"\n      - round: 13\n        reviewers: [1, 2]\n        note: \"RESOLVED。三重降格处理精准。\"\n      - round: 14\n        reviewers: [1, 2]\n        note: \"R2 初审重提 Finding 3 trivial（N3 critical），但 R1 REBUT 区分三层：(a) image_mean at-chance 确实 trivial；(b) readout 三条件梯度非 trivial；(c) training asymmetry 非 causal mask 可预测。R2 接受反驳，降为 should-fix。共识：image_mean 部分是 sanity check，但 readout 梯度和 training asymmetry 是实质发现，Abstract 措辞需更精准区分。\"\n    action_items:\n      - round: 14\n        action: \"Abstract 'confirms expected functional specialization' 措辞应区分 trivial (image_mean) 和 non-trivial (readout gradient, training asymmetry) 部分\"\n        assigned_to: research_director\n        status: pending\n  - id: R4-N2\n    summary: \"RSA inverted-U metric-dependent，CKA 反转\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 14\n    resolution: \"C3 降为 qualified observation + §4.4 CKA 正文讨论。\"\n    resolution_round: 8\n    mentions:\n      - round: 14\n        reviewers: [1, 2]\n        note: \"R1-W3 再次提出 RSA vs CKA 反转处理不足。R2 部分 REBUT（Appendix A.1 有更多讨论），但同意核心关切成立：metric 选择的 principled justification 不足，应讨论哪些 claim 对 metric robust vs sensitive。\"\n    action_items: []\n  - id: R4-N3\n    summary: \"L1 ablation 使用 5 demos\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 5\n    resolution: \"改用 50 demos (N=63,228)。\"\n    resolution_round: 5\n    mentions: []\n    action_items: []\n  - id: R4-W1\n    summary: \"RSA best-vs-best n.s. 未标注\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 5\n    resolution: \"已标注。\"\n    resolution_round: 5\n    mentions: []\n    action_items: []\n  - id: R4-W2\n    summary: \"缺乏多重比较校正\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 5\n    resolution: \"FDR 已应用。\"\n    resolution_round: 5\n    mentions: []\n    action_items: []\n  - id: R4-W3\n    summary: \"Probe N 未报告，MLP capacity 控制不充分\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 7\n    resolution: \"Demo-level split 完全消除时间泄漏。\"\n    resolution_round: 7\n    mentions: []\n    action_items: []\n  - id: R4-W4\n    summary: \"Frozen encoder confound\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 5\n    resolution: \"Introduction + Discussion 说明。\"\n    resolution_round: 5\n    mentions: []\n    action_items: []\n\n  # ============================================================\n  # Round 9-13 issues（更新 R14 mentions）\n  # ============================================================\n  - id: R9-N1\n    summary: \"单一模型(OpenVLA-7B)单一基准(LIBERO)，无法支撑 VLA 通用性\"\n    category: experiment\n    severity: critical\n    status: wont_fix\n    first_raised_round: 9\n    last_seen_round: 14\n    mentions:\n      - round: 9\n        reviewers: [1, 2]\n        note: \"双方 AGREE critical。\"\n      - round: 14\n        reviewers: [1, 2]\n        note: \"R14 fresh review 再次提出。R1-W4 + R2-W4: LIBERO-only 的 tabletop manipulation 可能是多个发现的充分条件。双方 AGREE。补充新角度：LIBERO 的简单 action space（7-D, 短 horizon）可能驱动 inverted-U 和跨架构收敛。\"\n    action_items:\n      - round: 10\n        action: \"Rebuttal 应对：causal mask 泛化 + testable predictions\"\n        assigned_to: research_director\n        status: pending\n    resolution: \"Claims 已限定为 'causal-decoder VLAs'。实验数据仍为 2 个架构，结构性局限不变。\"\n    resolution_round: null\n\n  - id: R9-N2\n    summary: \"所有分析均为 open-loop，无 closed-loop 机器人评估\"\n    category: experiment\n    severity: critical\n    status: wont_fix\n    first_raised_round: 9\n    last_seen_round: 14\n    mentions:\n      - round: 9\n        reviewers: [1, 2]\n        note: \"双方 AGREE critical。\"\n      - round: 13\n        reviewers: [1, 2]\n        note: \"PARTIALLY_RESOLVED。'orthogonal contribution' 措辞仍需修改。\"\n      - round: 14\n        reviewers: [1, 2]\n        note: \"R14 fresh review 以最高优先级再次提出（R2-N1 critical）。R1 AGREE with nuance（Häon 的 steering 也是 open-loop intervention）。双方共识：至少验证一个 actionable implication（如 L1 entropy vs task failure 相关性）是低成本高收益的最低修改方案。\"\n    action_items:\n      - round: 14\n        action: \"验证至少一个 actionable implication（建议：在已有 LIBERO rollout 数据上计算 L1 attention entropy 与 task failure 的相关性）\"\n        assigned_to: research_director\n        status: pending\n    resolution: \"Open-loop 结构性局限不变。R14 建议了低成本验证方案。\"\n    resolution_round: null\n\n  - id: R9-N3\n    summary: \"'Causal' 术语在 observational open-loop 分析中使用不当\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 9\n    last_seen_round: 10\n    resolution: \"Discussion 'Causal' → 'Interventional'；§4.3 heading 改为 'Open-loop functional sensitivity'。\"\n    resolution_round: 10\n    mentions: []\n    action_items: []\n\n  - id: R9-N4\n    summary: \"Ablation 使 R² 增加的 paradox 未充分解释\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 9\n    last_seen_round: 11\n    resolution: \"Discussion 加 information-computation dissociation 解释。\"\n    resolution_round: 11\n    mentions: []\n    action_items: []\n\n  - id: R9-N5\n    summary: \"Counterfactual 的 'semantic distance' 概念未定义\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 9\n    last_seen_round: 10\n    resolution: \"改用 Jaccard token overlap / token novelty。\"\n    resolution_round: 10\n    mentions: []\n    action_items: []\n\n  - id: R9-N6\n    summary: \"N=10 tasks 的 RSA bootstrap 统计功效不足\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 9\n    last_seen_round: 14\n    resolution: \"\"\n    resolution_round: null\n    mentions:\n      - round: 11\n        reviewers: [1]\n        note: \"RESOLVED（加了 power limitation 声明）。\"\n      - round: 14\n        reviewers: [1, 2]\n        note: \"R14 fresh review 升级为 critical（R1-N2）。R2 AGREE。新角度：(1) LIBERO-Goal Δ=+0.017 n.s. vs LIBERO-Spatial Δ=+0.023 p<0.001，差异仅 0.006 但显著性截然不同；(2) 跨架构 Δ=0.003 的 CI 重叠可能只反映 power 不足而非真正等价；(3) 建议用 TOST 等价性检验。\"\n    action_items:\n      - round: 14\n        action: \"提供 power analysis（N=10 可检测的最小效应量）；对跨架构 convergence 考虑 TOST 等价性检验；加强 non-significant ≠ no effect 的 caveat\"\n        assigned_to: research_director\n        status: pending\n\n  - id: R9-W1\n    summary: \"CoRL scope fit 有限：纯 representational analysis，无物理机器人实验\"\n    category: framing\n    severity: critical\n    status: open\n    first_raised_round: 9\n    last_seen_round: 14\n    resolution: \"\"\n    resolution_round: null\n    mentions:\n      - round: 13\n        reviewers: [1, 2]\n        note: \"PARTIALLY_RESOLVED。Writing-level 改善但核心缺陷无法通过写作修复。\"\n      - round: 14\n        reviewers: [1, 2]\n        note: \"R14 fresh review 以最高优先级提出（R2-N1 critical，R1 AGREE with nuance）。与 Häon et al. CoRL 2025 对比：Häon 有 representation intervention → behavior change 实验，本文 implications 均未验证。双方共识：纯 open-loop 分析在 CoRL 的竞争力取决于 AC 对分析性工作的接受阈值；建议改投 ICML/NeurIPS interpretability track 或补充验证。\"\n    action_items:\n      - round: 14\n        action: \"最低方案：验证一个 implication；最佳方案：补充 closed-loop 评估；备选：改投 ML venue\"\n        assigned_to: research_director\n        status: pending\n\n  - id: R9-W2\n    summary: \"C1 在 Abstract/Introduction/Contributions 中占比失衡\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 9\n    last_seen_round: 10\n    resolution: \"C1 降为末句 sanity check。\"\n    resolution_round: 10\n    mentions: []\n    action_items: []\n\n  - id: R9-W3\n    summary: \"Vision representation 训练效果微弱，framing 未充分反映\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 9\n    last_seen_round: 10\n    resolution: \"§4.4 标题改为 'Training primarily enhances readout decodability'。\"\n    resolution_round: 10\n    mentions: []\n    action_items: []\n\n  - id: R9-W4\n    summary: \"Cohen's d 独立性假设违反\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 9\n    last_seen_round: 14\n    resolution: \"\"\n    resolution_round: null\n    mentions:\n      - round: 10\n        reviewers: [1, 2]\n        note: \"RESOLVED（新增 trajectory-level d）。\"\n      - round: 14\n        reviewers: [1, 2]\n        note: \"R1 以 critical 重提（N1: paired data 应用 paired effect size）。R2 REBUT 偏差方向：paired d_z = mean_diff/SD_diff > standard d（因 SD_diff < SD_pooled），当前报告实际上是保守估计。技术分歧未完全解决，但双方同意应报告 paired d_z 和配对相关系数 r。降为 should-fix 级别。\"\n    action_items:\n      - round: 14\n        action: \"报告 paired Cohen's d_z 和配对相关系数 r（Table 5, Table 6, Appendix A.7）；在 Method 中讨论 paired vs independent d 的选择\"\n        assigned_to: research_director\n        status: pending\n\n  - id: R9-W5\n    summary: \"Pretrained Llama-2 base 的 9/32 heads 可能因 text in-distribution bias\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 9\n    last_seen_round: 10\n    resolution: \"Discussion 新增替代解释承认。\"\n    resolution_round: 10\n    mentions: []\n    action_items: []\n\n  - id: R9-W6\n    summary: \"Specificity control 效果有限(d ratio 1.08×)\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 9\n    last_seen_round: 14\n    resolution: \"四组 matched-size 比较，framing 'distributed routing'。\"\n    resolution_round: 11\n    mentions:\n      - round: 14\n        reviewers: [1, 2]\n        note: \"R1-W2 再次提出 ablation 因果推断过度表述。R2 AGREE：ablation 证明 necessity 不证明 sufficiency，'control' 应改为 'contribute to'。但不升级 severity——论文的 framing 已从早期版本改善。\"\n    action_items: []\n\n  - id: R9-W7\n    summary: \"N=63,228 观测的独立性——有效独立单元远小于报告值\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 9\n    last_seen_round: 12\n    resolution: \"§4.1 新增 N_eff 说明。\"\n    resolution_round: 10\n    mentions: []\n    action_items: []\n\n  - id: R9-I1\n    summary: \"缺失引用：Octo (Ghosh et al. 2024)\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 9\n    last_seen_round: 10\n    resolution: \"references.bib 新增。\"\n    resolution_round: 10\n    mentions: []\n    action_items: []\n\n  - id: R9-I2\n    summary: \"Häon et al. 2025 的 sparse semantic directions 与 L1 routing heads 的关系未讨论\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 9\n    last_seen_round: 11\n    resolution: \"Discussion 加 where/what 互补连接。\"\n    resolution_round: 11\n    mentions: []\n    action_items: []\n\n  - id: R9-I3\n    summary: \"多处小问题：Table 1 caption、脚注、accessed date\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 9\n    last_seen_round: 10\n    resolution: \"已修复。\"\n    resolution_round: 10\n    mentions: []\n    action_items: []\n\n  - id: R10-Q1\n    summary: \"Per-task MSE breakdown：消融后 MSE 不变是否存在 task-level cancellation\"\n    category: experiment\n    severity: info\n    status: resolved\n    first_raised_round: 10\n    last_seen_round: 11\n    resolution: \"Appendix 加 per-task breakdown。\"\n    resolution_round: 11\n    mentions: []\n    action_items: []\n\n  # ============================================================\n  # Round 12 issues — updated with R14 status\n  # ============================================================\n\n  - id: R12-N1\n    summary: \"因果 overclaiming：Title 'Routes' 暗示因果机制\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 12\n    last_seen_round: 13\n    resolution: \"Title 'Routes'→'Reorganizes'，全文 'routing'→'redistributes'，零残留。\"\n    resolution_round: 13\n    mentions: []\n    action_items: []\n\n  - id: R12-N2\n    summary: \"正文超出 CoRL 8 页限制\"\n    category: format\n    severity: critical\n    status: resolved\n    first_raised_round: 12\n    last_seen_round: 13\n    resolution: \"正文严格控制在 8 页内。\"\n    resolution_round: 13\n    mentions: []\n    action_items: []\n\n  - id: R12-N3\n    summary: \"Abstract/Introduction 信息过载\"\n    category: writing\n    severity: critical\n    status: resolved\n    first_raised_round: 12\n    last_seen_round: 13\n    resolution: \"Abstract 精简至 ~1 个定量值 + 定性发现。\"\n    resolution_round: 13\n    mentions: []\n    action_items: []\n\n  - id: R12-W1\n    summary: \"无首页 teaser figure\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 12\n    last_seen_round: 13\n    resolution: \"Page 1 新增 Figure 1。\"\n    resolution_round: 13\n    mentions: []\n    action_items: []\n\n  - id: R12-W2\n    summary: \"层编号 off-by-one\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 12\n    last_seen_round: 13\n    resolution: \"L1-L32 = 32 层，全文一致。\"\n    resolution_round: 13\n    mentions: []\n    action_items: []\n\n  - id: R12-W3\n    summary: \"多条引用使用 arXiv preprint 而非已发表版本\"\n    category: writing\n    severity: warning\n    status: in_progress\n    first_raised_round: 12\n    last_seen_round: 14\n    mentions:\n      - round: 13\n        reviewers: [1, 2]\n        note: \"3/3 已更新。仍有 belrose2023, padalkar2023 待更新。\"\n      - round: 14\n        reviewers: [2]\n        note: \"R2-M1 再次提及：brohan2023 (RT-2)、belrose2023、black2024 (π₀) 需检查是否有正式版本。\"\n    action_items:\n      - round: 14\n        action: \"检查并更新所有可更新的 arXiv 引用至正式版本\"\n        assigned_to: research_director\n        status: pending\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R12-W4\n    summary: \"缺失重要 related work\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 12\n    last_seen_round: 13\n    resolution: \"6/6 缺失引用全部补齐。\"\n    resolution_round: 13\n    mentions: []\n    action_items: []\n\n  - id: R12-W5\n    summary: \"与 Grant et al. 和 Häon et al. 的区分不够清晰\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 12\n    last_seen_round: 14\n    resolution: \"Related Work 加显式 what-vs-where 对比段落。\"\n    resolution_round: 13\n    mentions:\n      - round: 14\n        reviewers: [1, 2]\n        note: \"R2-W1 再次提出增量贡献不清晰。R1 AGREE with nuance（token-level 粒度和 multi-method convergence 设计是差异化）。建议增加明确 'what we add' 段落。\"\n    action_items: []\n\n  - id: R12-W6\n    summary: \"FDR 多重比较校正细节不足\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 12\n    last_seen_round: 14\n    resolution: \"BH 方法 + α=0.05 + 33-layer family per metric 完整报告。\"\n    resolution_round: 13\n    mentions:\n      - round: 14\n        reviewers: [1, 2]\n        note: \"R1-W1 提出更深层关切：FDR 仅在每个 metric 的 33 层内，未对全局 family-wise error rate 校正。R2 AGREE 但指出这是 ML interpretability 文献常见做法，属 should-fix。\"\n    action_items:\n      - round: 14\n        action: \"考虑在 Appendix 添加全局 Bonferroni-adjusted p-values 作为 robustness check\"\n        assigned_to: research_director\n        status: pending\n\n  - id: R12-I1\n    summary: \"术语不一致：readout token vs last_preaction\"\n    category: writing\n    severity: info\n    status: in_progress\n    first_raised_round: 12\n    last_seen_round: 14\n    mentions:\n      - round: 13\n        reviewers: [1, 2]\n        note: \"PARTIALLY_RESOLVED。Table 1 的 'last_preaction' 建议 caption 加映射说明。\"\n      - round: 14\n        reviewers: [1, 2]\n        note: \"R1-Minor-1 再次提出。R2 AGREE。需统一术语。\"\n    action_items:\n      - round: 14\n        action: \"统一为 'readout token'，首次出现时定义；Table caption 加映射说明\"\n        assigned_to: research_director\n        status: pending\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R12-I2\n    summary: \"Limitations 未作为独立 section\"\n    category: format\n    severity: info\n    status: in_progress\n    first_raised_round: 12\n    last_seen_round: 13\n    mentions:\n      - round: 13\n        reviewers: [1, 2]\n        note: \"PARTIALLY_RESOLVED。使用 paragraph 而非 subsection。\"\n      - round: 14\n        reviewers: []\n        note: \"本轮未提及。R2-M6 确认 Limitations section 存在且满足 CoRL 要求。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R12-DIV1\n    summary: \"Title 'Language Routes' 是否误导\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 12\n    last_seen_round: 13\n    resolution: \"Title 'Routes'→'Reorganizes' 消除误导。\"\n    resolution_round: 13\n    mentions: []\n    action_items: []\n\n  # ============================================================\n  # Round 13 issues — updated with R14 status\n  # ============================================================\n\n  - id: R13-W1\n    summary: \"'Orthogonal contribution' 措辞对 closed-loop validation 过于 dismissive\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 13\n    last_seen_round: 14\n    mentions:\n      - round: 13\n        reviewers: [1, 2]\n        note: \"建议改为 'complementary and necessary next step'。\"\n      - round: 14\n        reviewers: []\n        note: \"本轮未直接提及此具体措辞，但 R9-N2/R9-W1 的更广泛 scope fit 讨论涵盖了此问题。Discussion Section 5 仍含 'orthogonal contribution and a natural next step' 原文。\"\n    action_items:\n      - round: 13\n        action: \"'orthogonal contribution' 改为 'complementary and necessary next step'\"\n        assigned_to: research_director\n        status: pending\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R13-I1\n    summary: \"附录 'robust attractor' 措辞较主文更强\"\n    category: framing\n    severity: info\n    status: open\n    first_raised_round: 13\n    last_seen_round: 13\n    mentions:\n      - round: 14\n        reviewers: []\n        note: \"本轮未直接提及，但 R14 对 convergent claim 的全面弱化建议涵盖此问题。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R13-I2\n    summary: \"Spacing 压缩激进\"\n    category: format\n    severity: info\n    status: open\n    first_raised_round: 13\n    last_seen_round: 13\n    mentions:\n      - round: 14\n        reviewers: []\n        note: \"本轮未提及。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  # ============================================================\n  # Round 14 NEW issues\n  # ============================================================\n\n  - id: R14-N1\n    summary: \"'Convergent reorganization' claim 从 N=2 同类架构得出，混杂变量过多，证据不足\"\n    category: framing\n    severity: critical\n    status: open\n    first_raised_round: 14\n    last_seen_round: 14\n    mentions:\n      - round: 14\n        reviewers: [1, 2]\n        note: \"R1-N3 + R2-N2，双方 AGREE。OpenVLA 和 TraceVLA 共享 causal decoder + 32 layers + LIBERO + tokenized actions。Δ=0.003 的 mid-layer 收敛可能反映架构共性而非 VLA 训练通用规律。Exit-layer R² 差异 0.069 与 mid-layer Δ=0.003 形成矛盾。建议弱化为 'shared mid-layer specialization tendency' 或 'preliminary evidence'。\"\n    action_items:\n      - round: 14\n        action: \"将 'convergent reorganization' 弱化为 'shared tendency' 或 'preliminary evidence for convergence'；精确界定收敛范围（仅 mid-layer，exit-layer 分歧）；讨论哪些混杂变量最可能解释收敛\"\n        assigned_to: research_director\n        status: pending\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R14-W1\n    summary: \"Counterfactual instruction analysis 仅用 3/10 tasks，Spearman ρ=1.0 在 n=4 条件下 p=0.042 仅 marginal\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 14\n    last_seen_round: 14\n    mentions:\n      - round: 14\n        reviewers: [1, 2]\n        note: \"R1-W5 提出，R2 AGREE。3 tasks 选择 rationale 未报告，cross-task variance 未讨论。定性结论仍有 informative value，但不应用 ρ=1.0 支撑因果推断。\"\n    action_items:\n      - round: 14\n        action: \"在全部 10 tasks 上复现 counterfactual 分析，或报告 3 tasks 选择 rationale 和 cross-task variance\"\n        assigned_to: research_director\n        status: pending\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R14-W2\n    summary: \"单一训练 checkpoint 分析——不同 training seed 可能产生不同表征结构\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 14\n    last_seen_round: 14\n    mentions:\n      - round: 14\n        reviewers: [1, 2]\n        note: \"R1-W6 提出，R2 AGREE（但指出这是 ML interpretability 普遍局限）。建议 Limitations 中明确讨论哪些发现对 training stochasticity robust vs sensitive。\"\n    action_items:\n      - round: 14\n        action: \"Limitations 中讨论 training seed variance 的潜在影响\"\n        assigned_to: research_director\n        status: pending\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R14-W3\n    summary: \"缺失引用：Aghajanyan et al. (ACL 2021) + Kumar et al. (NeurIPS 2022)\"\n    category: writing\n    severity: warning\n    status: open\n    first_raised_round: 14\n    last_seen_round: 14\n    mentions:\n      - round: 14\n        reviewers: [1, 2]\n        note: \"R2 提出，R1 AGREE。Aghajanyan (intrinsic dimensionality of fine-tuning) 和 Kumar (fine-tuning distorts pretrained features) 与本文核心问题直接相关。\"\n    action_items:\n      - round: 14\n        action: \"引用 Aghajanyan et al. (ACL 2021) 和 Kumar et al. (NeurIPS 2022)\"\n        assigned_to: research_director\n        status: pending\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R14-I1\n    summary: \"Footnote 1 两个 pipeline R² 值差异未解释\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 14\n    last_seen_round: 14\n    mentions:\n      - round: 14\n        reviewers: [1]\n        note: \"R1-Minor-2。两个 pipeline 的差异是什么？读者无法判断哪组数字更可靠。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R14-I2\n    summary: \"Leave-one-out p ≤ 0.083 不应表述为 'robust'\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 14\n    last_seen_round: 14\n    mentions:\n      - round: 14\n        reviewers: [1, 2]\n        note: \"R1-Minor-5 提出，R2 AGREE。p=0.083 按任何常规标准不能称为 robust。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R14-I3\n    summary: \"Permutation test 仅 1,000 shuffles（建议 ≥10,000）\"\n    category: method\n    severity: info\n    status: open\n    first_raised_round: 14\n    last_seen_round: 14\n    mentions:\n      - round: 14\n        reviewers: [1, 2]\n        note: \"R1-Minor-3 提出，R2 AGREE。效应极大（15-23 SD）所以不影响结论，但统计实践建议增加。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "vla-ssd",
    "issues_yaml": "issues:\n  # ============================================================\n  # Round 1-8 历史 issues（全部 resolved，压缩保留）\n  # ============================================================\n  - id: R1-N1-old\n    summary: \"Untrained baseline 无法隔离 VLA fine-tuning vs Llama-2 语言预训练的贡献\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    resolution: \"三条件数据完整整合。\"\n    resolution_round: 3\n    mentions: []\n    action_items: []\n  - id: R1-N2-old\n    summary: \"单一模型 Title/Abstract 使用复数 'VLAs' 构成 overclaim\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    resolution: \"Title 改为单数。\"\n    resolution_round: 3\n    mentions: []\n    action_items: []\n  - id: R1-N4-old\n    summary: \"Design implications 完全基于 correlational evidence\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    resolution: \"Abstract 使用 hedge 语气。\"\n    resolution_round: 3\n    mentions: []\n    action_items: []\n  - id: R1-N3-old\n    summary: \"RSA best-vs-best selection bias\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    resolution: \"Same-layer comparison 为 primary evidence。\"\n    resolution_round: 3\n    mentions: []\n    action_items: []\n  - id: R2-N1-old\n    summary: \"Neo et al. (ICLR 2025) 未引用\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    resolution: \"已引用。\"\n    resolution_round: 3\n    mentions: []\n    action_items: []\n  - id: R2-W1-old\n    summary: \"Related Work 引用覆盖度不足\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    resolution: \"引用数量达标。\"\n    resolution_round: 3\n    mentions: []\n    action_items: []\n  - id: R1-W1-old\n    summary: \"'Instruction-blind' claim 过强\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    resolution: \"MLP probe 双重验证。\"\n    resolution_round: 3\n    mentions: []\n    action_items: []\n  - id: R1-W2-old\n    summary: \"CKA 反转 RSA 排序处理不充分\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    resolution: \"Method 新增 'Why RSA over CKA'。\"\n    resolution_round: 2\n    mentions: []\n    action_items: []\n  - id: R3-N1-old\n    summary: \"Limitations 格式\"\n    category: format\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    resolution: \"改为 subsection。\"\n    resolution_round: 3\n    mentions: []\n    action_items: []\n  - id: R3-N2-old\n    summary: \"em-dash AI 写作标志\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    resolution: \"零残留。\"\n    resolution_round: 2\n    mentions: []\n    action_items: []\n  - id: R3-W5-old\n    summary: \"无 code/data 释放声明\"\n    category: format\n    severity: info\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    resolution: \"Conclusion 加声明。\"\n    resolution_round: 3\n    mentions: []\n    action_items: []\n\n  # ============================================================\n  # Round 4-8 issues（全部 resolved）\n  # ============================================================\n  - id: R4-N1\n    summary: \"C1 是 causal mask 必然结果 + probe trivially easy\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 14\n    resolution: \"Abstract 'confirms expected' + 'consistent with causal attention mask' + 'framework sanity check' 三重降格。Contribution (iii) 定位为 methodology validation。全文一致。\"\n    resolution_round: 13\n    mentions:\n      - round: 9\n        reviewers: [1, 2]\n        note: \"R9-W2: C1 在 Abstract/Introduction 占比失衡。\"\n      - round: 10\n        reviewers: [1, 2]\n        note: \"RESOLVED。降格处理到位。\"\n      - round: 12\n        reviewers: [2, 3]\n        note: \"复发。R2-N1: 虽已降为 sanity check，但 Title 和 Abstract 仍将架构约束呈现为核心贡献。\"\n      - round: 13\n        reviewers: [1, 2]\n        note: \"RESOLVED。三重降格处理精准。\"\n      - round: 14\n        reviewers: [1, 2]\n        note: \"R2 初审重提 Finding 3 trivial（N3 critical），但 R1 REBUT 区分三层：(a) image_mean at-chance 确实 trivial；(b) readout 三条件梯度非 trivial；(c) training asymmetry 非 causal mask 可预测。R2 接受反驳，降为 should-fix。共识：image_mean 部分是 sanity check，但 readout 梯度和 training asymmetry 是实质发现，Abstract 措辞需更精准区分。\"\n    action_items:\n      - round: 14\n        action: \"Abstract 'confirms expected functional specialization' 措辞应区分 trivial (image_mean) 和 non-trivial (readout gradient, training asymmetry) 部分\"\n        assigned_to: research_director\n        status: pending\n  - id: R4-N2\n    summary: \"RSA inverted-U metric-dependent，CKA 反转\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 14\n    resolution: \"C3 降为 qualified observation + §4.4 CKA 正文讨论。\"\n    resolution_round: 8\n    mentions:\n      - round: 14\n        reviewers: [1, 2]\n        note: \"R1-W3 再次提出 RSA vs CKA 反转处理不足。R2 部分 REBUT（Appendix A.1 有更多讨论），但同意核心关切成立：metric 选择的 principled justification 不足，应讨论哪些 claim 对 metric robust vs sensitive。\"\n    action_items: []\n  - id: R4-N3\n    summary: \"L1 ablation 使用 5 demos\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 5\n    resolution: \"改用 50 demos (N=63,228)。\"\n    resolution_round: 5\n    mentions: []\n    action_items: []\n  - id: R4-W1\n    summary: \"RSA best-vs-best n.s. 未标注\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 5\n    resolution: \"已标注。\"\n    resolution_round: 5\n    mentions: []\n    action_items: []\n  - id: R4-W2\n    summary: \"缺乏多重比较校正\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 5\n    resolution: \"FDR 已应用。\"\n    resolution_round: 5\n    mentions: []\n    action_items: []\n  - id: R4-W3\n    summary: \"Probe N 未报告，MLP capacity 控制不充分\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 7\n    resolution: \"Demo-level split 完全消除时间泄漏。\"\n    resolution_round: 7\n    mentions: []\n    action_items: []\n  - id: R4-W4\n    summary: \"Frozen encoder confound\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 5\n    resolution: \"Introduction + Discussion 说明。\"\n    resolution_round: 5\n    mentions: []\n    action_items: []\n\n  # ============================================================\n  # Round 9-13 issues（更新 R14 mentions）\n  # ============================================================\n  - id: R9-N1\n    summary: \"单一模型(OpenVLA-7B)单一基准(LIBERO)，无法支撑 VLA 通用性\"\n    category: experiment\n    severity: critical\n    status: wont_fix\n    first_raised_round: 9\n    last_seen_round: 14\n    mentions:\n      - round: 9\n        reviewers: [1, 2]\n        note: \"双方 AGREE critical。\"\n      - round: 14\n        reviewers: [1, 2]\n        note: \"R14 fresh review 再次提出。R1-W4 + R2-W4: LIBERO-only 的 tabletop manipulation 可能是多个发现的充分条件。双方 AGREE。补充新角度：LIBERO 的简单 action space（7-D, 短 horizon）可能驱动 inverted-U 和跨架构收敛。\"\n    action_items:\n      - round: 10\n        action: \"Rebuttal 应对：causal mask 泛化 + testable predictions\"\n        assigned_to: research_director\n        status: pending\n    resolution: \"Claims 已限定为 'causal-decoder VLAs'。实验数据仍为 2 个架构，结构性局限不变。\"\n    resolution_round: null\n\n  - id: R9-N2\n    summary: \"所有分析均为 open-loop，无 closed-loop 机器人评估\"\n    category: experiment\n    severity: critical\n    status: wont_fix\n    first_raised_round: 9\n    last_seen_round: 14\n    mentions:\n      - round: 9\n        reviewers: [1, 2]\n        note: \"双方 AGREE critical。\"\n      - round: 13\n        reviewers: [1, 2]\n        note: \"PARTIALLY_RESOLVED。'orthogonal contribution' 措辞仍需修改。\"\n      - round: 14\n        reviewers: [1, 2]\n        note: \"R14 fresh review 以最高优先级再次提出（R2-N1 critical）。R1 AGREE with nuance（Häon 的 steering 也是 open-loop intervention）。双方共识：至少验证一个 actionable implication（如 L1 entropy vs task failure 相关性）是低成本高收益的最低修改方案。\"\n    action_items:\n      - round: 14\n        action: \"验证至少一个 actionable implication（建议：在已有 LIBERO rollout 数据上计算 L1 attention entropy 与 task failure 的相关性）\"\n        assigned_to: research_director\n        status: pending\n    resolution: \"Open-loop 结构性局限不变。R14 建议了低成本验证方案。\"\n    resolution_round: null\n\n  - id: R9-N3\n    summary: \"'Causal' 术语在 observational open-loop 分析中使用不当\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 9\n    last_seen_round: 10\n    resolution: \"Discussion 'Causal' → 'Interventional'；§4.3 heading 改为 'Open-loop functional sensitivity'。\"\n    resolution_round: 10\n    mentions: []\n    action_items: []\n\n  - id: R9-N4\n    summary: \"Ablation 使 R² 增加的 paradox 未充分解释\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 9\n    last_seen_round: 11\n    resolution: \"Discussion 加 information-computation dissociation 解释。\"\n    resolution_round: 11\n    mentions: []\n    action_items: []\n\n  - id: R9-N5\n    summary: \"Counterfactual 的 'semantic distance' 概念未定义\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 9\n    last_seen_round: 10\n    resolution: \"改用 Jaccard token overlap / token novelty。\"\n    resolution_round: 10\n    mentions: []\n    action_items: []\n\n  - id: R9-N6\n    summary: \"N=10 tasks 的 RSA bootstrap 统计功效不足\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 9\n    last_seen_round: 14\n    resolution: \"\"\n    resolution_round: null\n    mentions:\n      - round: 11\n        reviewers: [1]\n        note: \"RESOLVED（加了 power limitation 声明）。\"\n      - round: 14\n        reviewers: [1, 2]\n        note: \"R14 fresh review 升级为 critical（R1-N2）。R2 AGREE。新角度：(1) LIBERO-Goal Δ=+0.017 n.s. vs LIBERO-Spatial Δ=+0.023 p<0.001，差异仅 0.006 但显著性截然不同；(2) 跨架构 Δ=0.003 的 CI 重叠可能只反映 power 不足而非真正等价；(3) 建议用 TOST 等价性检验。\"\n    action_items:\n      - round: 14\n        action: \"提供 power analysis（N=10 可检测的最小效应量）；对跨架构 convergence 考虑 TOST 等价性检验；加强 non-significant ≠ no effect 的 caveat\"\n        assigned_to: research_director\n        status: pending\n\n  - id: R9-W1\n    summary: \"CoRL scope fit 有限：纯 representational analysis，无物理机器人实验\"\n    category: framing\n    severity: critical\n    status: open\n    first_raised_round: 9\n    last_seen_round: 14\n    resolution: \"\"\n    resolution_round: null\n    mentions:\n      - round: 13\n        reviewers: [1, 2]\n        note: \"PARTIALLY_RESOLVED。Writing-level 改善但核心缺陷无法通过写作修复。\"\n      - round: 14\n        reviewers: [1, 2]\n        note: \"R14 fresh review 以最高优先级提出（R2-N1 critical，R1 AGREE with nuance）。与 Häon et al. CoRL 2025 对比：Häon 有 representation intervention → behavior change 实验，本文 implications 均未验证。双方共识：纯 open-loop 分析在 CoRL 的竞争力取决于 AC 对分析性工作的接受阈值；建议改投 ICML/NeurIPS interpretability track 或补充验证。\"\n    action_items:\n      - round: 14\n        action: \"最低方案：验证一个 implication；最佳方案：补充 closed-loop 评估；备选：改投 ML venue\"\n        assigned_to: research_director\n        status: pending\n\n  - id: R9-W2\n    summary: \"C1 在 Abstract/Introduction/Contributions 中占比失衡\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 9\n    last_seen_round: 10\n    resolution: \"C1 降为末句 sanity check。\"\n    resolution_round: 10\n    mentions: []\n    action_items: []\n\n  - id: R9-W3\n    summary: \"Vision representation 训练效果微弱，framing 未充分反映\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 9\n    last_seen_round: 10\n    resolution: \"§4.4 标题改为 'Training primarily enhances readout decodability'。\"\n    resolution_round: 10\n    mentions: []\n    action_items: []\n\n  - id: R9-W4\n    summary: \"Cohen's d 独立性假设违反\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 9\n    last_seen_round: 14\n    resolution: \"\"\n    resolution_round: null\n    mentions:\n      - round: 10\n        reviewers: [1, 2]\n        note: \"RESOLVED（新增 trajectory-level d）。\"\n      - round: 14\n        reviewers: [1, 2]\n        note: \"R1 以 critical 重提（N1: paired data 应用 paired effect size）。R2 REBUT 偏差方向：paired d_z = mean_diff/SD_diff > standard d（因 SD_diff < SD_pooled），当前报告实际上是保守估计。技术分歧未完全解决，但双方同意应报告 paired d_z 和配对相关系数 r。降为 should-fix 级别。\"\n    action_items:\n      - round: 14\n        action: \"报告 paired Cohen's d_z 和配对相关系数 r（Table 5, Table 6, Appendix A.7）；在 Method 中讨论 paired vs independent d 的选择\"\n        assigned_to: research_director\n        status: pending\n\n  - id: R9-W5\n    summary: \"Pretrained Llama-2 base 的 9/32 heads 可能因 text in-distribution bias\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 9\n    last_seen_round: 10\n    resolution: \"Discussion 新增替代解释承认。\"\n    resolution_round: 10\n    mentions: []\n    action_items: []\n\n  - id: R9-W6\n    summary: \"Specificity control 效果有限(d ratio 1.08×)\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 9\n    last_seen_round: 14\n    resolution: \"四组 matched-size 比较，framing 'distributed routing'。\"\n    resolution_round: 11\n    mentions:\n      - round: 14\n        reviewers: [1, 2]\n        note: \"R1-W2 再次提出 ablation 因果推断过度表述。R2 AGREE：ablation 证明 necessity 不证明 sufficiency，'control' 应改为 'contribute to'。但不升级 severity——论文的 framing 已从早期版本改善。\"\n    action_items: []\n\n  - id: R9-W7\n    summary: \"N=63,228 观测的独立性——有效独立单元远小于报告值\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 9\n    last_seen_round: 12\n    resolution: \"§4.1 新增 N_eff 说明。\"\n    resolution_round: 10\n    mentions: []\n    action_items: []\n\n  - id: R9-I1\n    summary: \"缺失引用：Octo (Ghosh et al. 2024)\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 9\n    last_seen_round: 10\n    resolution: \"references.bib 新增。\"\n    resolution_round: 10\n    mentions: []\n    action_items: []\n\n  - id: R9-I2\n    summary: \"Häon et al. 2025 的 sparse semantic directions 与 L1 routing heads 的关系未讨论\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 9\n    last_seen_round: 11\n    resolution: \"Discussion 加 where/what 互补连接。\"\n    resolution_round: 11\n    mentions: []\n    action_items: []\n\n  - id: R9-I3\n    summary: \"多处小问题：Table 1 caption、脚注、accessed date\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 9\n    last_seen_round: 10\n    resolution: \"已修复。\"\n    resolution_round: 10\n    mentions: []\n    action_items: []\n\n  - id: R10-Q1\n    summary: \"Per-task MSE breakdown：消融后 MSE 不变是否存在 task-level cancellation\"\n    category: experiment\n    severity: info\n    status: resolved\n    first_raised_round: 10\n    last_seen_round: 11\n    resolution: \"Appendix 加 per-task breakdown。\"\n    resolution_round: 11\n    mentions: []\n    action_items: []\n\n  # ============================================================\n  # Round 12 issues — updated with R14 status\n  # ============================================================\n\n  - id: R12-N1\n    summary: \"因果 overclaiming：Title 'Routes' 暗示因果机制\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 12\n    last_seen_round: 13\n    resolution: \"Title 'Routes'→'Reorganizes'，全文 'routing'→'redistributes'，零残留。\"\n    resolution_round: 13\n    mentions: []\n    action_items: []\n\n  - id: R12-N2\n    summary: \"正文超出 CoRL 8 页限制\"\n    category: format\n    severity: critical\n    status: resolved\n    first_raised_round: 12\n    last_seen_round: 13\n    resolution: \"正文严格控制在 8 页内。\"\n    resolution_round: 13\n    mentions: []\n    action_items: []\n\n  - id: R12-N3\n    summary: \"Abstract/Introduction 信息过载\"\n    category: writing\n    severity: critical\n    status: resolved\n    first_raised_round: 12\n    last_seen_round: 13\n    resolution: \"Abstract 精简至 ~1 个定量值 + 定性发现。\"\n    resolution_round: 13\n    mentions: []\n    action_items: []\n\n  - id: R12-W1\n    summary: \"无首页 teaser figure\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 12\n    last_seen_round: 13\n    resolution: \"Page 1 新增 Figure 1。\"\n    resolution_round: 13\n    mentions: []\n    action_items: []\n\n  - id: R12-W2\n    summary: \"层编号 off-by-one\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 12\n    last_seen_round: 13\n    resolution: \"L1-L32 = 32 层，全文一致。\"\n    resolution_round: 13\n    mentions: []\n    action_items: []\n\n  - id: R12-W3\n    summary: \"多条引用使用 arXiv preprint 而非已发表版本\"\n    category: writing\n    severity: warning\n    status: in_progress\n    first_raised_round: 12\n    last_seen_round: 14\n    mentions:\n      - round: 13\n        reviewers: [1, 2]\n        note: \"3/3 已更新。仍有 belrose2023, padalkar2023 待更新。\"\n      - round: 14\n        reviewers: [2]\n        note: \"R2-M1 再次提及：brohan2023 (RT-2)、belrose2023、black2024 (π₀) 需检查是否有正式版本。\"\n    action_items:\n      - round: 14\n        action: \"检查并更新所有可更新的 arXiv 引用至正式版本\"\n        assigned_to: research_director\n        status: pending\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R12-W4\n    summary: \"缺失重要 related work\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 12\n    last_seen_round: 13\n    resolution: \"6/6 缺失引用全部补齐。\"\n    resolution_round: 13\n    mentions: []\n    action_items: []\n\n  - id: R12-W5\n    summary: \"与 Grant et al. 和 Häon et al. 的区分不够清晰\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 12\n    last_seen_round: 14\n    resolution: \"Related Work 加显式 what-vs-where 对比段落。\"\n    resolution_round: 13\n    mentions:\n      - round: 14\n        reviewers: [1, 2]\n        note: \"R2-W1 再次提出增量贡献不清晰。R1 AGREE with nuance（token-level 粒度和 multi-method convergence 设计是差异化）。建议增加明确 'what we add' 段落。\"\n    action_items: []\n\n  - id: R12-W6\n    summary: \"FDR 多重比较校正细节不足\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 12\n    last_seen_round: 14\n    resolution: \"BH 方法 + α=0.05 + 33-layer family per metric 完整报告。\"\n    resolution_round: 13\n    mentions:\n      - round: 14\n        reviewers: [1, 2]\n        note: \"R1-W1 提出更深层关切：FDR 仅在每个 metric 的 33 层内，未对全局 family-wise error rate 校正。R2 AGREE 但指出这是 ML interpretability 文献常见做法，属 should-fix。\"\n    action_items:\n      - round: 14\n        action: \"考虑在 Appendix 添加全局 Bonferroni-adjusted p-values 作为 robustness check\"\n        assigned_to: research_director\n        status: pending\n\n  - id: R12-I1\n    summary: \"术语不一致：readout token vs last_preaction\"\n    category: writing\n    severity: info\n    status: in_progress\n    first_raised_round: 12\n    last_seen_round: 14\n    mentions:\n      - round: 13\n        reviewers: [1, 2]\n        note: \"PARTIALLY_RESOLVED。Table 1 的 'last_preaction' 建议 caption 加映射说明。\"\n      - round: 14\n        reviewers: [1, 2]\n        note: \"R1-Minor-1 再次提出。R2 AGREE。需统一术语。\"\n    action_items:\n      - round: 14\n        action: \"统一为 'readout token'，首次出现时定义；Table caption 加映射说明\"\n        assigned_to: research_director\n        status: pending\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R12-I2\n    summary: \"Limitations 未作为独立 section\"\n    category: format\n    severity: info\n    status: in_progress\n    first_raised_round: 12\n    last_seen_round: 13\n    mentions:\n      - round: 13\n        reviewers: [1, 2]\n        note: \"PARTIALLY_RESOLVED。使用 paragraph 而非 subsection。\"\n      - round: 14\n        reviewers: []\n        note: \"本轮未提及。R2-M6 确认 Limitations section 存在且满足 CoRL 要求。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R12-DIV1\n    summary: \"Title 'Language Routes' 是否误导\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 12\n    last_seen_round: 13\n    resolution: \"Title 'Routes'→'Reorganizes' 消除误导。\"\n    resolution_round: 13\n    mentions: []\n    action_items: []\n\n  # ============================================================\n  # Round 13 issues — updated with R14 status\n  # ============================================================\n\n  - id: R13-W1\n    summary: \"'Orthogonal contribution' 措辞对 closed-loop validation 过于 dismissive\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 13\n    last_seen_round: 14\n    mentions:\n      - round: 13\n        reviewers: [1, 2]\n        note: \"建议改为 'complementary and necessary next step'。\"\n      - round: 14\n        reviewers: []\n        note: \"本轮未直接提及此具体措辞，但 R9-N2/R9-W1 的更广泛 scope fit 讨论涵盖了此问题。Discussion Section 5 仍含 'orthogonal contribution and a natural next step' 原文。\"\n    action_items:\n      - round: 13\n        action: \"'orthogonal contribution' 改为 'complementary and necessary next step'\"\n        assigned_to: research_director\n        status: pending\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R13-I1\n    summary: \"附录 'robust attractor' 措辞较主文更强\"\n    category: framing\n    severity: info\n    status: open\n    first_raised_round: 13\n    last_seen_round: 13\n    mentions:\n      - round: 14\n        reviewers: []\n        note: \"本轮未直接提及，但 R14 对 convergent claim 的全面弱化建议涵盖此问题。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R13-I2\n    summary: \"Spacing 压缩激进\"\n    category: format\n    severity: info\n    status: open\n    first_raised_round: 13\n    last_seen_round: 13\n    mentions:\n      - round: 14\n        reviewers: []\n        note: \"本轮未提及。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  # ============================================================\n  # Round 14 NEW issues\n  # ============================================================\n\n  - id: R14-N1\n    summary: \"'Convergent reorganization' claim 从 N=2 同类架构得出，混杂变量过多，证据不足\"\n    category: framing\n    severity: critical\n    status: open\n    first_raised_round: 14\n    last_seen_round: 14\n    mentions:\n      - round: 14\n        reviewers: [1, 2]\n        note: \"R1-N3 + R2-N2，双方 AGREE。OpenVLA 和 TraceVLA 共享 causal decoder + 32 layers + LIBERO + tokenized actions。Δ=0.003 的 mid-layer 收敛可能反映架构共性而非 VLA 训练通用规律。Exit-layer R² 差异 0.069 与 mid-layer Δ=0.003 形成矛盾。建议弱化为 'shared mid-layer specialization tendency' 或 'preliminary evidence'。\"\n    action_items:\n      - round: 14\n        action: \"将 'convergent reorganization' 弱化为 'shared tendency' 或 'preliminary evidence for convergence'；精确界定收敛范围（仅 mid-layer，exit-layer 分歧）；讨论哪些混杂变量最可能解释收敛\"\n        assigned_to: research_director\n        status: pending\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R14-W1\n    summary: \"Counterfactual instruction analysis 仅用 3/10 tasks，Spearman ρ=1.0 在 n=4 条件下 p=0.042 仅 marginal\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 14\n    last_seen_round: 14\n    mentions:\n      - round: 14\n        reviewers: [1, 2]\n        note: \"R1-W5 提出，R2 AGREE。3 tasks 选择 rationale 未报告，cross-task variance 未讨论。定性结论仍有 informative value，但不应用 ρ=1.0 支撑因果推断。\"\n    action_items:\n      - round: 14\n        action: \"在全部 10 tasks 上复现 counterfactual 分析，或报告 3 tasks 选择 rationale 和 cross-task variance\"\n        assigned_to: research_director\n        status: pending\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R14-W2\n    summary: \"单一训练 checkpoint 分析——不同 training seed 可能产生不同表征结构\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 14\n    last_seen_round: 14\n    mentions:\n      - round: 14\n        reviewers: [1, 2]\n        note: \"R1-W6 提出，R2 AGREE（但指出这是 ML interpretability 普遍局限）。建议 Limitations 中明确讨论哪些发现对 training stochasticity robust vs sensitive。\"\n    action_items:\n      - round: 14\n        action: \"Limitations 中讨论 training seed variance 的潜在影响\"\n        assigned_to: research_director\n        status: pending\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R14-W3\n    summary: \"缺失引用：Aghajanyan et al. (ACL 2021) + Kumar et al. (NeurIPS 2022)\"\n    category: writing\n    severity: warning\n    status: open\n    first_raised_round: 14\n    last_seen_round: 14\n    mentions:\n      - round: 14\n        reviewers: [1, 2]\n        note: \"R2 提出，R1 AGREE。Aghajanyan (intrinsic dimensionality of fine-tuning) 和 Kumar (fine-tuning distorts pretrained features) 与本文核心问题直接相关。\"\n    action_items:\n      - round: 14\n        action: \"引用 Aghajanyan et al. (ACL 2021) 和 Kumar et al. (NeurIPS 2022)\"\n        assigned_to: research_director\n        status: pending\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R14-I1\n    summary: \"Footnote 1 两个 pipeline R² 值差异未解释\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 14\n    last_seen_round: 14\n    mentions:\n      - round: 14\n        reviewers: [1]\n        note: \"R1-Minor-2。两个 pipeline 的差异是什么？读者无法判断哪组数字更可靠。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R14-I2\n    summary: \"Leave-one-out p ≤ 0.083 不应表述为 'robust'\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 14\n    last_seen_round: 14\n    mentions:\n      - round: 14\n        reviewers: [1, 2]\n        note: \"R1-Minor-5 提出，R2 AGREE。p=0.083 按任何常规标准不能称为 robust。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: R14-I3\n    summary: \"Permutation test 仅 1,000 shuffles（建议 ≥10,000）\"\n    category: method\n    severity: info\n    status: open\n    first_raised_round: 14\n    last_seen_round: 14\n    mentions:\n      - round: 14\n        reviewers: [1, 2]\n        note: \"R1-Minor-3 提出，R2 AGREE。效应极大（15-23 SD）所以不影响结论，但统计实践建议增加。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null"
  }
}
```

</details>

---


### Tool result

_source line 1086 · 2026-05-20T16:49:29.509959+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/review_issues.yaml\", \"bytes\": 25376}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 1087 · 2026-05-20T16:51:42.019529+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__submit_review_report_to_research_director",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__submit_review_report_to_research_director",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 1088 · 2026-05-20T16:51:42.070176+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1089 · 2026-05-20T16:53:22.881818+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "report": "# Consolidated Review Report — Round 14 (Fresh)\n\n**Paper**: \"Vision Encodes, Language Reorganizes: Token-Level Representational Analysis of VLA Fine-Tuning\"\n**Target Venue**: CoRL 2026 (deadline 2026-05-29)\n**Reviewers**: R1 (方法/实验严谨性), R2 (新颖性/scope/完整性)\n**Review Date**: 2026-05-20\n\n---\n\n## Summary\n\n本文对 VLA（Vision-Language-Action）模型的微调过程进行逐层、逐 token 类型的表征分析。以 OpenVLA-7B 为主要分析对象，辅以 TraceVLA 做跨架构对比，提出三个发现：(1) 微调将指令注意力重新分配至 entry-exit 层，L1 为主要 hub；(2) 两个不同架构的 VLA 在训练后达到相似的中层表征（Δ=0.003）；(3) image token 与 readout token 存在功能分化——image token 对指令不敏感，readout token 是多模态整合中心。论文包含 7 项互补分析（interventional、supporting、constraining）和 21 页附录。\n\n---\n\n## Strengths\n\n**S1. 系统性的多层次分析框架** — 论文从注意力头统计、RSA、CKA、线性探针、消融、反事实、剂量-反应等 7 个互补视角对 VLA 微调进行分析，形成 interventional → supporting → constraining 的证据层次。这种三角验证的方法论在 VLA 机制分析中尚属首次，且方法论本身可迁移至其他 VLA 研究。\n\n**S2. Readout token 发现具有实用价值** — 发现 readout token 是多模态整合的主要位点（R²=0.678 vs image_mean 的 chance-level），而 image token 对指令不敏感。这一发现对 VLA 架构设计（如 early-exit 推理、微调诊断）有直接指导意义。\n\n**S3. 训练-未训练因子设计** — 对训练/未训练模型进行成对比较，使用因子控制隔离微调效应，而非仅报告训练后状态。这使得因果推断更可信。\n\n**S4. 附录极为详尽** — 21 页附录覆盖鲁棒性检验（距离度量、per-DOF、permutation、seed、demo subsample）、OOD 诊断、跨 benchmark (LIBERO-Spatial) 验证等，几乎预见性地回应了常见审稿质疑。\n\n**S5. 剂量-反应分析** — 4→32 头渐进消融呈现单调递增而非阈值效应（d=0.48→0.64），为 L1 注意力头的功能重要性提供了介入性证据，超越了纯观察性分析。\n\n---\n\n## Weaknesses\n\n### Must-Fix（不修复则建议拒稿）\n\n**W-MF1. CoRL scope 适配性不足** [R1, R2 共识]\n论文是纯分析/解释性工作，无机器人实验、无闭环验证、无策略改进。CoRL 的核心受众关注 \"what can I build with this\"，而论文的 actionable insight（如 early-exit 推理、L1 entropy 监控）仅作为假设提出，未做任何验证。Discussion 中 \"orthogonal contribution and a natural next step\" 的措辞显得对闭环验证过于轻描淡写。建议：要么补充至少一个 downstream 应用实验（如 early-exit 推理的 latency-accuracy tradeoff），要么将 venue 转向 ICML/NeurIPS 的 interpretability track 或 workshop。\n\n**W-MF2. \"Convergent reorganization\" 声明过强** [R1, R2 共识]\n仅两个模型（OpenVLA, TraceVLA）的 Δ=0.003 不能支撑 \"convergent\" 这一暗示普遍性的术语。N=2 的跨架构比较本质上是 case study，无法排除巧合。标题中 \"Language Reorganizes\" 暗示了因果机制，但证据仅为相关性。建议：将 \"convergent\" 降级为 \"similar\" 或 \"consistent\"；在标题中去除因果暗示或加限定词；在 limitation 中明确声明 N=2 的局限。\n\n**W-MF3. 统计效力不足（N_eff=10）** [R1, R2 共识]\nbootstrap 基于 10 个 task 的聚合，N_eff=10 严重限制了统计推断的可靠性。置信区间（如 Δ=0.003 [−0.012, 0.018]）的宽度相对于 effect size 过大。此外，Spearman ρ 和 R² 的 bootstrap CI 是在 task-level 均值上计算的，掩盖了 demo-level 变异性。建议：报告 demo-level 分布；使用 TOST 等价性检验替代 \"差异小\" 的叙述性声称；在 limitation 中坦诚讨论 power 不足。\n\n### Should-Fix（不影响接收决定，但显著提升论文质量）\n\n**W-SF1. Cohen's d 计算方法需澄清** [R1 提出, R2 部分反驳后达成共识]\nR1 认为对配对数据使用标准 Cohen's d 可能高估效应量（因为忽略了配对相关结构，分母偏大）。R2 反驳指出对配对数据，paired d_z = mean_diff / SD_diff，而 SD_diff < SD_pooled（当 r>0 时），因此 paired d_z 实际更大——即当前报告反而保守。双方未完全达成一致的方向判断，但共识是：应明确报告使用的是哪种 Cohen's d 公式（标准/配对），并在附录给出配对版本的数值供对比。\n\n**W-SF2. 仅 LIBERO 基准** [R1, R2 共识]\n所有实验基于 LIBERO-Long（+ 附录 LIBERO-Spatial），但 LIBERO 是桌面操作的相对简单环境。缺少更复杂或领域不同的 benchmark（如 RLBench、CALVIN、real-world data）。至少应在 Discussion 中讨论 LIBERO 特异性风险，并将跨 benchmark 泛化列为明确的 future work。\n\n**W-SF3. 缺少关键参考文献** [R1, R2 共识]\n缺少以下领域的引用：(1) VLA efficiency/pruning（如 TinyVLA, ECoT）；(2) Diffusion/flow-matching VLA 架构（仅在 limitation 中提及 π0, Octo，但未在 related work 充分讨论）；(3) 机器人基础模型的 scaling 分析。建议在 Related Work 中补充。\n\n**W-SF4. 单 checkpoint 分析** [R2 提出, R1 同意]\n仅分析最终 checkpoint，缺少训练过程中的动态变化。即使不做完整的 training dynamics 研究，至少在几个中间 checkpoint 上报告关键指标（如 L1 注意力头数量、readout R²）的演化趋势，以支持 \"fine-tuning redistributes\" 的叙事。\n\n**W-SF5. Finding 3（token specialization）的定位需强化** [R2 提出 → R1 反驳 → R2 接受]\nR2 初始认为 Finding 3（image token 对指令不敏感）近乎 trivial（image token 在 readout 之前生成，自然缺乏指令信息）。R1 反驳指出：(a) readout gradient（L1 即 100% 而非渐进上升）非显然；(b) training asymmetry（训练不改变 image blindness 但大幅提升 readout）非显然；(c) 构成三层分解的基础。R2 接受此反驳，但建议作者在正文中更清晰地阐述为何该发现非 trivial，避免读者产生同样疑问。\n\n---\n\n## Reviewer Consensus（共识点）\n\n1. **CoRL scope 是首要问题** — 两位审稿人均认为纯分析性论文缺乏 robotics 应用验证是最大短板\n2. **\"Convergent\" 声称过强** — N=2 架构 + N_eff=10 的统计基础不足以支撑此术语\n3. **方法论框架本身有价值** — 三角验证方法论和 readout token 发现是实质贡献\n4. **附录质量高** — 鲁棒性检验详尽，预见性强\n5. **需补充参考文献** — VLA efficiency 和 diffusion VLA 领域引用缺失\n\n## Reviewer Divergence（分歧点）\n\n| 议题 | R1 立场 | R2 立场 | 解决状态 |\n|------|---------|---------|----------|\n| Finding 3 是否 trivial | 非 trivial（readout gradient + training asymmetry） | 初认为 trivial → 接受 R1 反驳 | ✅ 已解决 |\n| Cohen's d 偏差方向 | 标准 d 可能高估效应 | paired d_z > standard d，当前报告保守 | ⚠️ 未完全解决（数学上 R2 更准确，但双方共识需澄清公式） |\n| Effect size 是否 modest | \"Medium at best\" | 部分效应实际很大（d>0.8） | ✅ R2 撤回广泛质疑 |\n| 标题因果暗示 | 未强调 | \"Reorganizes\" 暗示因果 | ✅ R2 接受 R1 观点（降级为 should-fix） |\n\n---\n\n## Questions for Authors\n\n1. L1 的 24/32 instruction-dominant heads 中，是否有 head 在 pretrained Llama-2 中已存在 instruction sensitivity？如果有，fine-tuning 是 amplifying 还是 creating？\n2. Δ=0.003 的等价性检验（如 TOST with ε=0.05）的 p 值是多少？如果不显著，\"convergent\" 声称如何辩护？\n3. 是否考虑过在训练中间 checkpoint 上测量 L1 head count 的演化曲线？这能区分 \"突然切换\" 与 \"渐进积累\" 两种微调机制。\n4. Readout token 的 R²=0.678——剩余 32.2% 的方差来源是什么？是否有证据表明 action 信息也分布在其他 token 位置？\n5. 若在 RLBench 或 real-world manipulation 数据上重复关键实验（如 RSA profile + readout probing），你预期结果会有何不同？\n\n---\n\n## Missing References\n\n- TinyVLA 或其他 VLA compression/efficiency 工作\n- ECoT (Embodied Chain-of-Thought)\n- Diffusion/flow-matching VLA 的表征分析（如 Octo 内部表征研究，若存在）\n- VLA scaling laws 相关工作\n- CALVIN benchmark 上的 VLA 分析\n\n---\n\n## External Review\n\n**外部审稿（Stanford Agentic Reviewer）：pending，未返回。**\n\n---\n\n## Visual Layout Check（非评分项）\n\n由独立视觉审查 Agent 完成，结果如下：\n\n- **Critical (1)**：Page 31（附录末页）约 90% 空白，严重浪费版面\n- **Warnings (4)**：\n  - Pages 2-4：连续 3 页无图表，纯文字密度过高\n  - Page 16：图表标签字号过小，可能不满足打印可读性\n  - Page 21：表格过于密集，建议拆分或调整间距\n  - Page 30：同上，表格密度过高\n- **Info (21)**：其余为次要排版观察\n\n建议：(1) 将 page 31 的孤立内容合并至前页或删除空白页；(2) 考虑在 pages 2-4 之间插入 Figure 以改善视觉节奏。\n\n---\n\n## Overall Assessment\n\n**Overall Score: 5.5/10 → Weak Reject**\n\n| Reviewer | 初始分 | 最终分 | 变化原因 |\n|----------|--------|--------|----------|\n| R1 | 6/10 | 6/10 | 无变化 |\n| R2 | 4/10 | 5/10 | 接受 R1 对 Finding 3 和 effect size 的反驳 |\n\n**核心判断**：论文的方法论框架（三角验证 + 因子设计）和 readout token 发现是实质贡献，但三个结构性问题使其不适合当前形式投稿 CoRL：(1) 纯分析无闭环验证，与 CoRL robotics 受众不匹配；(2) \"convergent\" 声称的统计基础（N=2 架构, N_eff=10）不足；(3) 仅 LIBERO 单一 benchmark。\n\n**建议路径**：\n- **若坚持 CoRL**：补充至少一个 downstream 应用实验（early-exit 推理或 L1 entropy 微调诊断），将 \"convergent\" 降级，补充参考文献\n- **若转投**：ICML/NeurIPS interpretability track 或 CoRL Workshop 可能是更自然的归属\n\n---\n\n## Detailed Comments\n\n### 对正文的具体建议\n\n1. **Abstract L2**: \"convergent reorganization\" → \"consistent reorganization\" 或 \"similar reorganization pattern\"\n2. **Title**: \"Language Reorganizes\" 暗示因果 → 考虑 \"Language Information Is Reorganized\" 或加限定词\n3. **Section 4.3 跨架构段落**: 需要加入 N=2 局限的显式 caveat\n4. **Discussion \"orthogonal contribution\"**: 语气过于轻描淡写 → 改为 \"We acknowledge closed-loop validation as the primary limitation...\"\n5. **Conclusion**: 过短（3 行），缺少 broader impact 讨论和 CoRL 要求的 limitation 总结\n6. **Table 1 caption**: 澄清 \"chance\" 的具体含义（1/10 = 10%?）\n7. **Section 2.5 \"Why RSA over CKA\"**: 很好的主动回应，但建议将 CKA 附录结果的关键数字直接引入正文一句话\n\n### 对附录的建议\n\n8. **Page 31 空白页**: 删除或合并内容\n9. **Appendix 结构**: 21 页附录建议在开头加一个 1-paragraph roadmap\n10. **Table 24/25 (TraceVLA R²)**: 正文只引用了 Δ=0.003，建议在正文给出 TraceVLA 的 peak layer 位置以增强跨架构叙事",
  "project": "vla-ssd",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "weak reject",
  "review_chat_id": "oc_554a5023cde4d603635cf97e6ab8151a"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "report": "# Consolidated Review Report — Round 14 (Fresh)\n\n**Paper**: \"Vision Encodes, Language Reorganizes: Token-Level Representational Analysis of VLA Fine-Tuning\"\n**Target Venue**: CoRL 2026 (deadline 2026-05-29)\n**Reviewers**: R1 (方法/实验严谨性), R2 (新颖性/scope/完整性)\n**Review Date**: 2026-05-20\n\n---\n\n## Summary\n\n本文对 VLA（Vision-Language-Action）模型的微调过程进行逐层、逐 token 类型的表征分析。以 OpenVLA-7B 为主要分析对象，辅以 TraceVLA 做跨架构对比，提出三个发现：(1) 微调将指令注意力重新分配至 entry-exit 层，L1 为主要 hub；(2) 两个不同架构的 VLA 在训练后达到相似的中层表征（Δ=0.003）；(3) image token 与 readout token 存在功能分化——image token 对指令不敏感，readout token 是多模态整合中心。论文包含 7 项互补分析（interventional、supporting、constraining）和 21 页附录。\n\n---\n\n## Strengths\n\n**S1. 系统性的多层次分析框架** — 论文从注意力头统计、RSA、CKA、线性探针、消融、反事实、剂量-反应等 7 个互补视角对 VLA 微调进行分析，形成 interventional → supporting → constraining 的证据层次。这种三角验证的方法论在 VLA 机制分析中尚属首次，且方法论本身可迁移至其他 VLA 研究。\n\n**S2. Readout token 发现具有实用价值** — 发现 readout token 是多模态整合的主要位点（R²=0.678 vs image_mean 的 chance-level），而 image token 对指令不敏感。这一发现对 VLA 架构设计（如 early-exit 推理、微调诊断）有直接指导意义。\n\n**S3. 训练-未训练因子设计** — 对训练/未训练模型进行成对比较，使用因子控制隔离微调效应，而非仅报告训练后状态。这使得因果推断更可信。\n\n**S4. 附录极为详尽** — 21 页附录覆盖鲁棒性检验（距离度量、per-DOF、permutation、seed、demo subsample）、OOD 诊断、跨 benchmark (LIBERO-Spatial) 验证等，几乎预见性地回应了常见审稿质疑。\n\n**S5. 剂量-反应分析** — 4→32 头渐进消融呈现单调递增而非阈值效应（d=0.48→0.64），为 L1 注意力头的功能重要性提供了介入性证据，超越了纯观察性分析。\n\n---\n\n## Weaknesses\n\n### Must-Fix（不修复则建议拒稿）\n\n**W-MF1. CoRL scope 适配性不足** [R1, R2 共识]\n论文是纯分析/解释性工作，无机器人实验、无闭环验证、无策略改进。CoRL 的核心受众关注 \"what can I build with this\"，而论文的 actionable insight（如 early-exit 推理、L1 entropy 监控）仅作为假设提出，未做任何验证。Discussion 中 \"orthogonal contribution and a natural next step\" 的措辞显得对闭环验证过于轻描淡写。建议：要么补充至少一个 downstream 应用实验（如 early-exit 推理的 latency-accuracy tradeoff），要么将 venue 转向 ICML/NeurIPS 的 interpretability track 或 workshop。\n\n**W-MF2. \"Convergent reorganization\" 声明过强** [R1, R2 共识]\n仅两个模型（OpenVLA, TraceVLA）的 Δ=0.003 不能支撑 \"convergent\" 这一暗示普遍性的术语。N=2 的跨架构比较本质上是 case study，无法排除巧合。标题中 \"Language Reorganizes\" 暗示了因果机制，但证据仅为相关性。建议：将 \"convergent\" 降级为 \"similar\" 或 \"consistent\"；在标题中去除因果暗示或加限定词；在 limitation 中明确声明 N=2 的局限。\n\n**W-MF3. 统计效力不足（N_eff=10）** [R1, R2 共识]\nbootstrap 基于 10 个 task 的聚合，N_eff=10 严重限制了统计推断的可靠性。置信区间（如 Δ=0.003 [−0.012, 0.018]）的宽度相对于 effect size 过大。此外，Spearman ρ 和 R² 的 bootstrap CI 是在 task-level 均值上计算的，掩盖了 demo-level 变异性。建议：报告 demo-level 分布；使用 TOST 等价性检验替代 \"差异小\" 的叙述性声称；在 limitation 中坦诚讨论 power 不足。\n\n### Should-Fix（不影响接收决定，但显著提升论文质量）\n\n**W-SF1. Cohen's d 计算方法需澄清** [R1 提出, R2 部分反驳后达成共识]\nR1 认为对配对数据使用标准 Cohen's d 可能高估效应量（因为忽略了配对相关结构，分母偏大）。R2 反驳指出对配对数据，paired d_z = mean_diff / SD_diff，而 SD_diff < SD_pooled（当 r>0 时），因此 paired d_z 实际更大——即当前报告反而保守。双方未完全达成一致的方向判断，但共识是：应明确报告使用的是哪种 Cohen's d 公式（标准/配对），并在附录给出配对版本的数值供对比。\n\n**W-SF2. 仅 LIBERO 基准** [R1, R2 共识]\n所有实验基于 LIBERO-Long（+ 附录 LIBERO-Spatial），但 LIBERO 是桌面操作的相对简单环境。缺少更复杂或领域不同的 benchmark（如 RLBench、CALVIN、real-world data）。至少应在 Discussion 中讨论 LIBERO 特异性风险，并将跨 benchmark 泛化列为明确的 future work。\n\n**W-SF3. 缺少关键参考文献** [R1, R2 共识]\n缺少以下领域的引用：(1) VLA efficiency/pruning（如 TinyVLA, ECoT）；(2) Diffusion/flow-matching VLA 架构（仅在 limitation 中提及 π0, Octo，但未在 related work 充分讨论）；(3) 机器人基础模型的 scaling 分析。建议在 Related Work 中补充。\n\n**W-SF4. 单 checkpoint 分析** [R2 提出, R1 同意]\n仅分析最终 checkpoint，缺少训练过程中的动态变化。即使不做完整的 training dynamics 研究，至少在几个中间 checkpoint 上报告关键指标（如 L1 注意力头数量、readout R²）的演化趋势，以支持 \"fine-tuning redistributes\" 的叙事。\n\n**W-SF5. Finding 3（token specialization）的定位需强化** [R2 提出 → R1 反驳 → R2 接受]\nR2 初始认为 Finding 3（image token 对指令不敏感）近乎 trivial（image token 在 readout 之前生成，自然缺乏指令信息）。R1 反驳指出：(a) readout gradient（L1 即 100% 而非渐进上升）非显然；(b) training asymmetry（训练不改变 image blindness 但大幅提升 readout）非显然；(c) 构成三层分解的基础。R2 接受此反驳，但建议作者在正文中更清晰地阐述为何该发现非 trivial，避免读者产生同样疑问。\n\n---\n\n## Reviewer Consensus（共识点）\n\n1. **CoRL scope 是首要问题** — 两位审稿人均认为纯分析性论文缺乏 robotics 应用验证是最大短板\n2. **\"Convergent\" 声称过强** — N=2 架构 + N_eff=10 的统计基础不足以支撑此术语\n3. **方法论框架本身有价值** — 三角验证方法论和 readout token 发现是实质贡献\n4. **附录质量高** — 鲁棒性检验详尽，预见性强\n5. **需补充参考文献** — VLA efficiency 和 diffusion VLA 领域引用缺失\n\n## Reviewer Divergence（分歧点）\n\n| 议题 | R1 立场 | R2 立场 | 解决状态 |\n|------|---------|---------|----------|\n| Finding 3 是否 trivial | 非 trivial（readout gradient + training asymmetry） | 初认为 trivial → 接受 R1 反驳 | ✅ 已解决 |\n| Cohen's d 偏差方向 | 标准 d 可能高估效应 | paired d_z > standard d，当前报告保守 | ⚠️ 未完全解决（数学上 R2 更准确，但双方共识需澄清公式） |\n| Effect size 是否 modest | \"Medium at best\" | 部分效应实际很大（d>0.8） | ✅ R2 撤回广泛质疑 |\n| 标题因果暗示 | 未强调 | \"Reorganizes\" 暗示因果 | ✅ R2 接受 R1 观点（降级为 should-fix） |\n\n---\n\n## Questions for Authors\n\n1. L1 的 24/32 instruction-dominant heads 中，是否有 head 在 pretrained Llama-2 中已存在 instruction sensitivity？如果有，fine-tuning 是 amplifying 还是 creating？\n2. Δ=0.003 的等价性检验（如 TOST with ε=0.05）的 p 值是多少？如果不显著，\"convergent\" 声称如何辩护？\n3. 是否考虑过在训练中间 checkpoint 上测量 L1 head count 的演化曲线？这能区分 \"突然切换\" 与 \"渐进积累\" 两种微调机制。\n4. Readout token 的 R²=0.678——剩余 32.2% 的方差来源是什么？是否有证据表明 action 信息也分布在其他 token 位置？\n5. 若在 RLBench 或 real-world manipulation 数据上重复关键实验（如 RSA profile + readout probing），你预期结果会有何不同？\n\n---\n\n## Missing References\n\n- TinyVLA 或其他 VLA compression/efficiency 工作\n- ECoT (Embodied Chain-of-Thought)\n- Diffusion/flow-matching VLA 的表征分析（如 Octo 内部表征研究，若存在）\n- VLA scaling laws 相关工作\n- CALVIN benchmark 上的 VLA 分析\n\n---\n\n## External Review\n\n**外部审稿（Stanford Agentic Reviewer）：pending，未返回。**\n\n---\n\n## Visual Layout Check（非评分项）\n\n由独立视觉审查 Agent 完成，结果如下：\n\n- **Critical (1)**：Page 31（附录末页）约 90% 空白，严重浪费版面\n- **Warnings (4)**：\n  - Pages 2-4：连续 3 页无图表，纯文字密度过高\n  - Page 16：图表标签字号过小，可能不满足打印可读性\n  - Page 21：表格过于密集，建议拆分或调整间距\n  - Page 30：同上，表格密度过高\n- **Info (21)**：其余为次要排版观察\n\n建议：(1) 将 page 31 的孤立内容合并至前页或删除空白页；(2) 考虑在 pages 2-4 之间插入 Figure 以改善视觉节奏。\n\n---\n\n## Overall Assessment\n\n**Overall Score: 5.5/10 → Weak Reject**\n\n| Reviewer | 初始分 | 最终分 | 变化原因 |\n|----------|--------|--------|----------|\n| R1 | 6/10 | 6/10 | 无变化 |\n| R2 | 4/10 | 5/10 | 接受 R1 对 Finding 3 和 effect size 的反驳 |\n\n**核心判断**：论文的方法论框架（三角验证 + 因子设计）和 readout token 发现是实质贡献，但三个结构性问题使其不适合当前形式投稿 CoRL：(1) 纯分析无闭环验证，与 CoRL robotics 受众不匹配；(2) \"convergent\" 声称的统计基础（N=2 架构, N_eff=10）不足；(3) 仅 LIBERO 单一 benchmark。\n\n**建议路径**：\n- **若坚持 CoRL**：补充至少一个 downstream 应用实验（early-exit 推理或 L1 entropy 微调诊断），将 \"convergent\" 降级，补充参考文献\n- **若转投**：ICML/NeurIPS interpretability track 或 CoRL Workshop 可能是更自然的归属\n\n---\n\n## Detailed Comments\n\n### 对正文的具体建议\n\n1. **Abstract L2**: \"convergent reorganization\" → \"consistent reorganization\" 或 \"similar reorganization pattern\"\n2. **Title**: \"Language Reorganizes\" 暗示因果 → 考虑 \"Language Information Is Reorganized\" 或加限定词\n3. **Section 4.3 跨架构段落**: 需要加入 N=2 局限的显式 caveat\n4. **Discussion \"orthogonal contribution\"**: 语气过于轻描淡写 → 改为 \"We acknowledge closed-loop validation as the primary limitation...\"\n5. **Conclusion**: 过短（3 行），缺少 broader impact 讨论和 CoRL 要求的 limitation 总结\n6. **Table 1 caption**: 澄清 \"chance\" 的具体含义（1/10 = 10%?）\n7. **Section 2.5 \"Why RSA over CKA\"**: 很好的主动回应，但建议将 CKA 附录结果的关键数字直接引入正文一句话\n\n### 对附录的建议\n\n8. **Page 31 空白页**: 删除或合并内容\n9. **Appendix 结构**: 21 页附录建议在开头加一个 1-paragraph roadmap\n10. **Table 24/25 (TraceVLA R²)**: 正文只引用了 Δ=0.003，建议在正文给出 TraceVLA 的 peak layer 位置以增强跨架构叙事",
    "project": "vla-ssd",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "weak reject",
    "review_chat_id": "oc_554a5023cde4d603635cf97e6ab8151a"
  }
}
```

</details>

---


### Tool result

_source line 1090 · 2026-05-20T16:53:22.932666+00:00_

{"result":"{\"success\": false, \"data\": {\"expected_reviewer_ids\": [1, 2, 3], \"missing\": [3]}, \"error\": \"consolidated report is incomplete — reviewer(s) [3] were NOT acknowledged. This project has 3 reviewer(s): [1, 2, 3]. Each reviewer's findings (Must-Fix / Should-Fix / score) must be folded into the report. Re-read the missed reviewer's submission via feishu_read_chat_history or the session log, then call this tool again with reviewer_ids_acknowledged covering all 3 reviewers.\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1091 · 2026-05-20T16:53:27.801512+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_get_project_overview",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 1092 · 2026-05-20T16:53:27.852075+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1093 · 2026-05-20T16:53:30.161114+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "vla-ssd"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "vla-ssd"
  }
}
```

</details>

---


### Tool result

_source line 1094 · 2026-05-20T16:53:30.760876+00:00_

{"result":"# 项目 vla-ssd 概况\n\n## 实验状态 (117 个)\n\n- **lg_extract_untrained_r2**: DONE (killed) — \n- **lg_extract_trained_r2**: DONE (killed) — \n- **lg_extract_untrained_r1**: DONE (killed) — \n- **lg_extract_trained_r1**: DONE (killed) — \n- **mvp2_delta_dino**: DONE (success) — \n- **mvp2_delta_untrained**: DONE (success) — \n- **mvp2_delta_trained**: DONE (success) — \n- **mvp2_action_dino**: DONE (success) — \n- **mvp2_action_untrained**: DONE (success) — \n- **mvp2_action_trained**: DONE (success) — \n- **mvp_controlb_untrained**: DONE (success) — \n- **mvp_controlb_trained**: DONE (success) — \n- **mvp_001**: DONE (negative) — \n- **mvp_probe_untrained**: DONE (success) — \n- **mvp_probe_trained**: DONE (negative) — \n\n## 最新报告\n# Handover — 2026-05-20\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n- libero_finetuned_probe（准备中）\n- behavioral_smoketest_diag（准备中）\n- behavioral_pilot_v2: Ablating L1 instruction-dominant heads (24/32) during VLA inference on LIBERO-Goal fine-tuned OpenVLA reduces task success rate, providing behavioral evidence that attention head specialization has functional consequences for task execution.（准备中）\n- behavioral_pilot: Ablating L1 instruction-dominant heads during VLA inference will measurably change task success rate, providing behavioral evidence that these heads serve a functional role beyond representational reorganization measured by probes.（准备中）\n- fulllayer_action_probe（准备中）\n- l1_head_ablation_control8（准备中）\n- l1_head_ablation_50demos（准备中）\n\n## 近期结论\n- **phi3v_untrained_seed_expansion** (success): Expanding Phi3V untrained R² probe from 5 to 15 seeds will tighten confidence intervals on the untrained profile (early peak at L4, monotonic decline), aligning statistical power with the other 3 conditions in the 2×2 matrix (all 15 seeds) and eliminating asymmetric seed count as a reviewer concern. ← 基于 phi3v_r2_untrained_probe\n  [phi3v_untrained_15seed_analysis](/api/workspace-files/projects/vla-ssd/artifacts/
…[truncated 1571 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 599
}
```

</details>

---


### Tool call

_source line 1095 · 2026-05-20T16:53:36.715154+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-15-projects-vla-ssd--claude-sessions-review-director-ae8c68a6/",
  "description": "List session directory for transcript files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-15-projects-vla-ssd--claude-sessions-review-director-ae8c68a6/",
    "description": "List session directory for transcript files"
  }
}
```

</details>

---


### Tool result

_source line 1096 · 2026-05-20T16:53:36.866648+00:00_

247a19bc-ff5b-4998-8d4a-5a0eb05ea2f4
247a19bc-ff5b-4998-8d4a-5a0eb05ea2f4.jsonl
8a507cc7-23ff-44c8-a1e3-3fce1be8808f.jsonl
b356f826-c226-4cb3-a4f5-b640539b4a7f.jsonl
de1bde7f-e731-400f-9905-932541adbff4
de1bde7f-e731-400f-9905-932541adbff4.jsonl
memory

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Bash",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 1097 · 2026-05-20T16:53:40.028542+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -l \"Reviewer 3\" /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-15-projects-vla-ssd--claude-sessions-review-director-ae8c68a6/*.jsonl 2>/dev/null | head -5",
  "description": "Find which transcript files mention Reviewer 3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -l \"Reviewer 3\" /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-15-projects-vla-ssd--claude-sessions-review-director-ae8c68a6/*.jsonl 2>/dev/null | head -5",
    "description": "Find which transcript files mention Reviewer 3"
  }
}
```

</details>

---


### Tool result

_source line 1098 · 2026-05-20T16:53:40.079184+00:00_

/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-15-projects-vla-ssd--claude-sessions-review-director-ae8c68a6/8a507cc7-23ff-44c8-a1e3-3fce1be8808f.jsonl
/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-15-projects-vla-ssd--claude-sessions-review-director-ae8c68a6/b356f826-c226-4cb3-a4f5-b640539b4a7f.jsonl
/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-15-projects-vla-ssd--claude-sessions-review-director-ae8c68a6/de1bde7f-e731-400f-9905-932541adbff4.jsonl

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1099 · 2026-05-20T16:53:43.643154+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep \"Reviewer 3\" /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-15-projects-vla-ssd--claude-sessions-review-director-ae8c68a6/de1bde7f-e731-400f-9905-932541adbff4.jsonl | head -5",
  "description": "Check latest transcript for R3 mentions"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Bash",
  "tool_args": {
    "command": "grep \"Reviewer 3\" /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-15-projects-vla-ssd--claude-sessions-review-director-ae8c68a6/de1bde7f-e731-400f-9905-932541adbff4.jsonl | head -5",
    "description": "Check latest transcript for R3 mentions"
  }
}
```

</details>

---


### Tool result

_source line 1100 · 2026-05-20T16:53:43.695223+00:00_

&lt;persisted-output>
Output too large (30.9KB). Full output saved to: /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-15-projects-vla-ssd--claude-sessions-review-director-ae8c68a6/b356f826-c226-4cb3-a4f5-b640539b4a7f/tool-results/b8l1h7sti.txt

Preview (first 2KB):
{"parentUuid":"5bc0097f-c7e2-4119-bbfb-e90494067462","isSidechain":false,"message":{"model":"claude-opus-4-6","id":"msg_019o9dk2yDVJy7yxAxb25Xiq","type":"message","role":"assistant","content":[{"type":"tool_use","id":"toolu_013NQ9MtxUmtJA3BTyNb1Z2Q","name":"mcp__agent-ml-research__director_post_to_reviewer","input":{"reviewer_id":"3","round_number":1,"project":"vla-ssd","text":"你是 Reviewer 3，负责 **写作质量 + 格式合规 + 可复现性**。\n\n## Venue 信息\n- **目标会议**: CoRL 2026 (Conference on Robot Learning)\n- **截止日期**: 2026-05-29\n- **页数限制**: 8 页正文（参考文献、附录不计）\n- **模板**: `\\usepackage{corl_2026}`\n- **匿名规则**: Double-blind（论文中不应出现任何可识别作者身份的信息）\n- **附录**: 允许，可参与审稿\n- **特殊要求**: 必须包含 Limitations section；鼓励提交 video (≤250MB, ≤3min)、code、data 作为 supplementary materials\n- **引用格式**: natbib\n\n## 论文文件\n- LaTeX: `docs/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/main.pdf`\n\n## 你的审查侧重\n\n**核心任务：评估写作质量、格式合规性、以及可复现性。**\n\n请重点审查以下方面：\n\n1. **CoRL 2026 格式合规**\n   - 正文是否在 8 页限制内？（参考文献、附录不计页数）\n   - 是否使用正确的 `corl_2026` 模板？\n   - Double-blind 匿名是否完整？（检查：作者名、机构、acknowledgment、GitHub 链接、self-citation 措辞）\n   - Limitations section 是否存在且充分？\n   - 参考文献格式是否一致？\n\n2. **写作质量**\n   - 论文结构是否清晰？各 section 过渡是否流畅？\n   - Abstract 是否准确概括了主要发现？是否有 overclaim？\n   - 术语使用是否一致？（如 \"readout token\" vs \"action token\", \"instruction routing\" 等）\n   - 是否存在 AI 写作痕迹？（em-dash 过度使用、不自然的 hedging pattern、\"delve into\"/\"it is worth noting\" 等）\n   - 信息密度是否适当？8 页内是否传递了过多内容导致读者难以消化？\n\n3. **图表质量**\n   - Figure 1 是否在第 1 页出现且有效传达核心发现？\n   - 所有图表的 caption 是否自包含（standalone readable）？\n   - 图表分辨率和字体大小是否适合打印？\n   - 表格格式是否使用 booktabs 风格？数据呈现是否清晰？\n\n4. **可复现性**\n   - 实验设置描述是否充分？（模型 chec
…[truncated 326 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Bash",
  "elapsed_ms": 52
}
```

</details>

---


### Tool call

_source line 1101 · 2026-05-20T16:53:47.511441+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -o '\"Reviewer 3[^\"]*\"' /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-15-projects-vla-ssd--claude-sessions-review-director-ae8c68a6/de1bde7f-e731-400f-9905-932541adbff4.jsonl | head -10",
  "description": "Check current transcript for R3 references"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -o '\"Reviewer 3[^\"]*\"' /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-15-projects-vla-ssd--claude-sessions-review-director-ae8c68a6/de1bde7f-e731-400f-9905-932541adbff4.jsonl | head -10",
    "description": "Check current transcript for R3 references"
  }
}
```

</details>

---


### Tool result

_source line 1102 · 2026-05-20T16:53:47.563106+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Bash",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 1103 · 2026-05-20T16:53:51.026114+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep \"reviewer_id.*3\\|Reviewer 3\\|reviewer 3\\|R3\" /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-15-projects-vla-ssd--claude-sessions-review-director-ae8c68a6/de1bde7f-e731-400f-9905-932541adbff4.jsonl | head -5",
  "description": "Search current transcript for any R3 mentions"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Bash",
  "tool_args": {
    "command": "grep \"reviewer_id.*3\\|Reviewer 3\\|reviewer 3\\|R3\" /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-15-projects-vla-ssd--claude-sessions-review-director-ae8c68a6/de1bde7f-e731-400f-9905-932541adbff4.jsonl | head -5",
    "description": "Search current transcript for any R3 mentions"
  }
}
```

</details>

---


### Tool result

_source line 1104 · 2026-05-20T16:53:51.128209+00:00_

&lt;persisted-output>
Output too large (1.9MB). Full output saved to: /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-15-projects-vla-ssd--claude-sessions-review-director-ae8c68a6/b356f826-c226-4cb3-a4f5-b640539b4a7f/tool-results/btg3souwe.txt

Preview (first 2KB):
{"parentUuid":"530949e7-b85d-41ef-91c7-2cf59d00af3b","isSidechain":false,"promptId":"8dc4dff3-4c3d-4989-b3d8-9af87ddec242","type":"user","message":{"role":"user","content":[{"tool_use_id":"toolu_017gdXaXuiZXGDsydGRGbMP7","type":"tool_result","content":"1\t---\n2\tname: review-director-session-start\n3\tdescription: Review Director session 启动初始化流程——圆桌多轮审稿协议。Review Director 角色 session 启动时自动使用。\n4\tpriority: 9\n5\tscope: global\n6\ttags:\n7\t- workflow\n8\t- review\n9\t- session\n10\tversion: 3\n11\troles:\n12\t- review_director\n13\t---\n14\t\n15\t# Review Director Session 启动流程（圆桌会议模式）\n16\t\n17\t## 初始化\n18\t\n19\t1. `director_get_project_overview(project)` — 了解研究现状（实验状态、最新报告）\n20\t2. 读取论文文件状态：检查 `projects/{project}/paper/` 或 `main.tex` 是否存在\n21\t3. 检查是否有来自 Research Director 的论文提交（`[论文提交]` 消息）\n22\t4. 向用户简要汇报：\n23\t   - **投稿目标**：venue 和 deadline\n24\t   - **论文状态**：当前草稿位置和版本\n25\t   - **资料完整性**：提交的材料是否齐全\n26\t   - **下一步**：即将开始的圆桌审稿流程\n27\t\n28\t## 评审流程（收到论文提交后执行）\n29\t\n30\t### Step 0 — 资料检查 + Venue 调研（必须先做，不可跳过）\n31\t\n32\t1. 检查提交资料完整性：论文文件是否存在、是否可读、补充材料是否齐全\n33\t2. 确认目标投稿 venue（从提交消息中获取）\n34\t3. 用 `web_search` 搜索该 venue 当前轮次的 CFP（Call for Papers），关键词示例：\n35\t   - `\"&lt;venue name> 2026 call for papers\" site:aclweb.org`\n36\t   - `\"&lt;venue name> 2026 submission deadline\"`\n37\t   - `\"&lt;venue name> 2026 author guidelines\"`\n38\t4. **验证 deadline 未过期**：今天日期与截止日期对比，若已过期立即通知用户，不继续\n39\t5. 提取当前版本的格式要求：\n40\t   - 页数限制（正文 / 附录 / 参考文献）\n41\t   - 模板（ACL / IEEE / NeurIPS / ICML / ...）\n42\t   - 匿名规则（double-blind / single-blind / open）\n43\t   - 附录规则（是否允许、是否参与审稿）\n44\t   - 引用格式（natbib / biblatex / 特定 .bst）\n45\t6. 将以上信息作为上下文，随任务一起传递给 Reviewer\n46\t\n47\t⚠️ 禁止使用训练知识中的 venue 要求——格式标准每年
…[truncated 325 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Bash",
  "elapsed_ms": 102
}
```

</details>

---


### Tool call

_source line 1105 · 2026-05-20T16:53:58.405388+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep \"director_post_to_reviewer\" /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-15-projects-vla-ssd--claude-sessions-review-director-ae8c68a6/de1bde7f-e731-400f-9905-932541adbff4.jsonl | grep -o '\"reviewer_id\":\"[^\"]*\"' | sort -u",
  "description": "Check which reviewers were dispatched in current session"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Bash",
  "tool_args": {
    "command": "grep \"director_post_to_reviewer\" /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-15-projects-vla-ssd--claude-sessions-review-director-ae8c68a6/de1bde7f-e731-400f-9905-932541adbff4.jsonl | grep -o '\"reviewer_id\":\"[^\"]*\"' | sort -u",
    "description": "Check which reviewers were dispatched in current session"
  }
}
```

</details>

---


### Tool result

_source line 1106 · 2026-05-20T16:53:58.507239+00:00_

"reviewer_id":"1"
"reviewer_id":"2"
"reviewer_id":"3"

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Bash",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 1107 · 2026-05-20T16:54:01.670141+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep \"Reviewer 3.*审稿\" /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-15-projects-vla-ssd--claude-sessions-review-director-ae8c68a6/de1bde7f-e731-400f-9905-932541adbff4.jsonl | head -5",
  "description": "Find R3 review submission messages"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Bash",
  "tool_args": {
    "command": "grep \"Reviewer 3.*审稿\" /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-15-projects-vla-ssd--claude-sessions-review-director-ae8c68a6/de1bde7f-e731-400f-9905-932541adbff4.jsonl | head -5",
    "description": "Find R3 review submission messages"
  }
}
```

</details>

---


### Tool result

_source line 1108 · 2026-05-20T16:54:01.771595+00:00_

&lt;persisted-output>
Output too large (30.9KB). Full output saved to: /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-15-projects-vla-ssd--claude-sessions-review-director-ae8c68a6/b356f826-c226-4cb3-a4f5-b640539b4a7f/tool-results/b4n4sgjk9.txt

Preview (first 2KB):
{"parentUuid":"5bc0097f-c7e2-4119-bbfb-e90494067462","isSidechain":false,"message":{"model":"claude-opus-4-6","id":"msg_019o9dk2yDVJy7yxAxb25Xiq","type":"message","role":"assistant","content":[{"type":"tool_use","id":"toolu_013NQ9MtxUmtJA3BTyNb1Z2Q","name":"mcp__agent-ml-research__director_post_to_reviewer","input":{"reviewer_id":"3","round_number":1,"project":"vla-ssd","text":"你是 Reviewer 3，负责 **写作质量 + 格式合规 + 可复现性**。\n\n## Venue 信息\n- **目标会议**: CoRL 2026 (Conference on Robot Learning)\n- **截止日期**: 2026-05-29\n- **页数限制**: 8 页正文（参考文献、附录不计）\n- **模板**: `\\usepackage{corl_2026}`\n- **匿名规则**: Double-blind（论文中不应出现任何可识别作者身份的信息）\n- **附录**: 允许，可参与审稿\n- **特殊要求**: 必须包含 Limitations section；鼓励提交 video (≤250MB, ≤3min)、code、data 作为 supplementary materials\n- **引用格式**: natbib\n\n## 论文文件\n- LaTeX: `docs/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/main.pdf`\n\n## 你的审查侧重\n\n**核心任务：评估写作质量、格式合规性、以及可复现性。**\n\n请重点审查以下方面：\n\n1. **CoRL 2026 格式合规**\n   - 正文是否在 8 页限制内？（参考文献、附录不计页数）\n   - 是否使用正确的 `corl_2026` 模板？\n   - Double-blind 匿名是否完整？（检查：作者名、机构、acknowledgment、GitHub 链接、self-citation 措辞）\n   - Limitations section 是否存在且充分？\n   - 参考文献格式是否一致？\n\n2. **写作质量**\n   - 论文结构是否清晰？各 section 过渡是否流畅？\n   - Abstract 是否准确概括了主要发现？是否有 overclaim？\n   - 术语使用是否一致？（如 \"readout token\" vs \"action token\", \"instruction routing\" 等）\n   - 是否存在 AI 写作痕迹？（em-dash 过度使用、不自然的 hedging pattern、\"delve into\"/\"it is worth noting\" 等）\n   - 信息密度是否适当？8 页内是否传递了过多内容导致读者难以消化？\n\n3. **图表质量**\n   - Figure 1 是否在第 1 页出现且有效传达核心发现？\n   - 所有图表的 caption 是否自包含（standalone readable）？\n   - 图表分辨率和字体大小是否适合打印？\n   - 表格格式是否使用 booktabs 风格？数据呈现是否清晰？\n\n4. **可复现性**\n   - 实验设置描述是否充分？（模型 chec
…[truncated 326 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Bash",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 1109 · 2026-05-20T16:54:06.053184+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -n \"Reviewer 3.*审稿意见\\|Reviewer 3.*审稿结果\\|\\\\[Reviewer 3\" /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-15-projects-vla-ssd--claude-sessions-review-director-ae8c68a6/de1bde7f-e731-400f-9905-932541adbff4.jsonl 2>/dev/null | head -20",
  "description": "Find R3 review result messages"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -n \"Reviewer 3.*审稿意见\\|Reviewer 3.*审稿结果\\|\\\\[Reviewer 3\" /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-15-projects-vla-ssd--claude-sessions-review-director-ae8c68a6/de1bde7f-e731-400f-9905-932541adbff4.jsonl 2>/dev/null | head -20",
    "description": "Find R3 review result messages"
  }
}
```

</details>

---


### Tool result

_source line 1110 · 2026-05-20T16:54:06.104160+00:00_

&lt;persisted-output>
Output too large (118.2KB). Full output saved to: /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-15-projects-vla-ssd--claude-sessions-review-director-ae8c68a6/b356f826-c226-4cb3-a4f5-b640539b4a7f/tool-results/b6oe1i0s7.txt

Preview (first 2KB):
81:{"type":"queue-operation","operation":"enqueue","timestamp":"2026-05-20T11:45:41.189Z","sessionId":"de1bde7f-e731-400f-9905-932541adbff4","content":"[服务器重启后首条消息 — Director] 项目: vla-ssd | 当前日期: 2026-05-20\n服务器刚重启，你的对话记忆已丢失。在处理用户消息前，先执行：\n1. `feishu_read_chat_history(chat_id=\"oc_554a5023cde4d603635cf97e6ab8151a\", limit=30)` 恢复近期对话上下文\n2. `get_project_status(\"vla-ssd\")` 检查配置\n3. `director_get_project_overview(\"vla-ssd\")` 了解现状\n如果有缺失配置，先向用户确认。\n\n**用户消息：** [Reviewer 3 审稿意见]:\n## Reviewer 3 审稿报告：写作质量 + 格式合规 + 可复现性\n\n**论文**: \"Vision Encodes, Language Routes: Token-Level Functional Specialization in a Vision-Language-Action Model\"  \n**Venue**: CoRL 2026  \n**审稿模式**: Fresh review\n\n---\n\n## 总体评分\n**Overall**: 5/10 — Borderline reject  \n**一句话总结**: 技术内容扎实、分析全面，但正文严重超出 8 页限制（约 8.7 页），且写作密度过高导致可读性受损，这两个问题在当前状态下足以影响接收决定。\n\n## 官方维度打分（基于 CoRL review criteria: significance/novelty, relevance to robotics, soundness, clarity, reproducibility）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Significance & Novelty | 6/10 | 对 VLA 内部表征的系统性分析有价值，但主要是 observational/diagnostic 工作，没有直接的方法改进或 actionable 发现用于改进机器人系统 |\n| Relevance to Robotics | 5/10 | 研究对象是机器人 VLA 模型，但发现（L1 routing、middle-layer peak）目前缺乏实际机器人应用验证（全部是 open-loop 分析） |\n| Soundness | 7/10 | 实验设计严谨（factorial controls、7 种互补分析、cross-architecture 验证），统计方法得当 |\n| Clarity | 4/10 | 信息密度过高，abstract 塞了过多定量细节，introduction 重复 abstract 80% 内容，Discussion 段落过长 |\n| Reproducibility | 7/10 | 模型 checkpoint、数据集、seed、compute 均报告；承诺 code release；probe 架构完整描述 |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] 正文超出 8 页限制\n- 具体位置：PDF pages 1–9；Section 5 (Discussion) + Conclusion 延伸到第 9 页，References 从第 9 页约 1/3 处开始\n- 问题：CoRL 202
…[truncated 327 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1111 · 2026-05-20T16:54:09.321546+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-15-projects-vla-ssd--claude-sessions-review-director-ae8c68a6/b356f826-c226-4cb3-a4f5-b640539b4a7f/tool-results/b6oe1i0s7.txt",
  "limit": "200"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-15-projects-vla-ssd--claude-sessions-review-director-ae8c68a6/b356f826-c226-4cb3-a4f5-b640539b4a7f/tool-results/b6oe1i0s7.txt",
    "limit": "200"
  }
}
```

</details>

---


### Tool result

_source line 1112 · 2026-05-20T16:54:09.623013+00:00_

File content (45207 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Read",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 1113 · 2026-05-20T16:54:13.086092+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-15-projects-vla-ssd--claude-sessions-review-director-ae8c68a6/b356f826-c226-4cb3-a4f5-b640539b4a7f/tool-results/b6oe1i0s7.txt",
  "limit": "100",
  "offset": "0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-15-projects-vla-ssd--claude-sessions-review-director-ae8c68a6/b356f826-c226-4cb3-a4f5-b640539b4a7f/tool-results/b6oe1i0s7.txt",
    "limit": "100",
    "offset": "0"
  }
}
```

</details>

---


### Tool result

_source line 1114 · 2026-05-20T16:54:13.337395+00:00_

File content (45207 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Read",
  "elapsed_ms": 251
}
```

</details>

---


### Tool call

_source line 1115 · 2026-05-20T16:54:18.256251+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "head -1 /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-15-projects-vla-ssd--claude-sessions-review-director-ae8c68a6/b356f826-c226-4cb3-a4f5-b640539b4a7f/tool-results/b6oe1i0s7.txt | python3 -c \"\nimport sys, json\nline = sys.stdin.readline()\ndata = json.loads(line)\ncontent = data.get('content', '')\n# Find R3 review\nimport re\nidx = content.find('Reviewer 3 审稿报告')\nif idx >= 0:\n    print(content[idx:idx+8000])\nelse:\n    print('NOT FOUND in first line')\n\"",
  "description": "Extract R3's review from the transcript entry"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Bash",
  "tool_args": {
    "command": "head -1 /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-15-projects-vla-ssd--claude-sessions-review-director-ae8c68a6/b356f826-c226-4cb3-a4f5-b640539b4a7f/tool-results/b6oe1i0s7.txt | python3 -c \"\nimport sys, json\nline = sys.stdin.readline()\ndata = json.loads(line)\ncontent = data.get('content', '')\n# Find R3 review\nimport re\nidx = content.find('Reviewer 3 审稿报告')\nif idx >= 0:\n    print(content[idx:idx+8000])\nelse:\n    print('NOT FOUND in first line')\n\"",
    "description": "Extract R3's review from the transcript entry"
  }
}
```

</details>

---


### Tool result

_source line 1116 · 2026-05-20T16:54:18.457651+00:00_

Exit code 1
Traceback (most recent call last):
  File "&lt;string>", line 4, in &lt;module>
    data = json.loads(line)
  File "/usr/lib/python3.14/json/__init__.py", line 352, in loads
    return _default_decoder.decode(s)
           ~~~~~~~~~~~~~~~~~~~~~~~^^^
  File "/usr/lib/python3.14/json/decoder.py", line 348, in decode
    raise JSONDecodeError("Extra data", s, end)
json.decoder.JSONDecodeError: Extra data: line 1 column 3 (char 2)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Bash",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 1117 · 2026-05-20T16:54:22.072107+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -o 'Reviewer 3 审稿报告.*' /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-15-projects-vla-ssd--claude-sessions-review-director-ae8c68a6/b356f826-c226-4cb3-a4f5-b640539b4a7f/tool-results/b6oe1i0s7.txt | head -1 | cut -c1-10000",
  "description": "Extract R3 review text"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -o 'Reviewer 3 审稿报告.*' /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-15-projects-vla-ssd--claude-sessions-review-director-ae8c68a6/b356f826-c226-4cb3-a4f5-b640539b4a7f/tool-results/b6oe1i0s7.txt | head -1 | cut -c1-10000",
    "description": "Extract R3 review text"
  }
}
```

</details>

---


### Tool result

_source line 1118 · 2026-05-20T16:54:22.122950+00:00_

Reviewer 3 审稿报告：写作质量 + 格式合规 + 可复现性\n\n**论文**: \"Vision Encodes, Language Routes: Token-Level Functional Specialization in a Vision-Language-Action Model\"  \n**Venue**: CoRL 2026  \n**审稿模式**: Fresh review\n\n---\n\n## 总体评分\n**Overall**: 5/10 — Borderline reject  \n**一句话总结**: 技术内容扎实、分析全面，但正文严重超出 8 页限制（约 8.7 页），且写作密度过高导致可读性受损，这两个问题在当前状态下足以影响接收决定。\n\n## 官方维度打分（基于 CoRL review criteria: significance/novelty, relevance to robotics, soundness, clarity, reproducibility）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Significance & Novelty | 6/10 | 对 VLA 内部表征的系统性分析有价值，但主要是 observational/diagnostic 工作，没有直接的方法改进或 actionable 发现用于改进机器人系统 |\n| Relevance to Robotics | 5/10 | 研究对象是机器人 VLA 模型，但发现（L1 routing、middle-layer peak）目前缺乏实际机器人应用验证（全部是 open-loop 分析） |\n| Soundness | 7/10 | 实验设计严谨（factorial controls、7 种互补分析、cross-architecture 验证），统计方法得当 |\n| Clarity | 4/10 | 信息密度过高，abstract 塞了过多定量细节，introduction 重复 abstract 80% 内容，Discussion 段落过长 |\n| Reproducibility | 7/10 | 模型 checkpoint、数据集、seed、compute 均报告；承诺 code release；probe 架构完整描述 |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] 正文超出 8 页限制\n- 具体位置：PDF pages 1–9；Section 5 (Discussion) + Conclusion 延伸到第 9 页，References 从第 9 页约 1/3 处开始\n- 问题：CoRL 2026 明确规定 \"8 pages maximum for main text\"（Author Instructions 页面确认）。当前正文约 8.7 页，超限约 0.7 页。Discussion 的 Synthesis、Mechanistic interpretation、Functional stages and predictions、Limitations and scope 四个段落 + Conclusion 完全在第 9 页。\n- 为什么影响接收：超页限是 desk rejection 的常见理由。即使不被 desk reject，也会被 reviewer 扣分。\n- 建议修改方向：(1) 将 Discussion 中 Mechanistic interpretation 和 Functional stages 的预测性内容移至 Appendix；(2) 压缩 Introduction 中与 Abstract 重复的量化描述；(3) 减小 float spacing（但当前已压缩至 `\\setlength{\\textfloatsep}{8pt}`，空间有限）。\n\n**N2** [critical] Abstract 和 Introduction 信息过载，可读性差\n- 具体位置：abstract.tex（全文 8 个句子）；introduction.tex（24 行密集文本，大量括号内数字）\n- 问题：Abstract 在 ~200 words 内塞入了至少 15 个定量结果（$d = 0.48 \\to 0.64$、$p = 0.033$、$R^2 +0.069$、$2.5\\times$ 等），远超同领域 CoRL/NeurIPS 论文的 abstract 信息密度。Introduction 几乎逐字重复 abstract 
…[truncated 4909 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1119 · 2026-05-20T16:54:27.693773+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -c \"reviewer_id.*3.*cross\\|Reviewer 3.*交叉\\|R3.*cross\" /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-15-projects-vla-ssd--claude-sessions-review-director-ae8c68a6/de1bde7f-e731-400f-9905-932541adbff4.jsonl 2>/dev/null",
  "description": "Check if R3 did cross-sharing"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -c \"reviewer_id.*3.*cross\\|Reviewer 3.*交叉\\|R3.*cross\" /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-15-projects-vla-ssd--claude-sessions-review-director-ae8c68a6/de1bde7f-e731-400f-9905-932541adbff4.jsonl 2>/dev/null",
    "description": "Check if R3 did cross-sharing"
  }
}
```

</details>

---


### Tool result

_source line 1120 · 2026-05-20T16:54:27.744475+00:00_

22

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1121 · 2026-05-20T16:54:31.942274+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep \"Reviewer 3.*交叉回应\\|\\\\[Reviewer 3 审稿结果\\\\].*交叉\" /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-15-projects-vla-ssd--claude-sessions-review-director-ae8c68a6/de1bde7f-e731-400f-9905-932541adbff4.jsonl | head -3 | cut -c1-2000",
  "description": "Find R3 cross-response messages"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Bash",
  "tool_args": {
    "command": "grep \"Reviewer 3.*交叉回应\\|\\\\[Reviewer 3 审稿结果\\\\].*交叉\" /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-15-projects-vla-ssd--claude-sessions-review-director-ae8c68a6/de1bde7f-e731-400f-9905-932541adbff4.jsonl | head -3 | cut -c1-2000",
    "description": "Find R3 cross-response messages"
  }
}
```

</details>

---


### Tool result

_source line 1122 · 2026-05-20T16:54:32.044229+00:00_

{"type":"queue-operation","operation":"enqueue","timestamp":"2026-05-20T11:51:19.288Z","sessionId":"de1bde7f-e731-400f-9905-932541adbff4","content":"[Reviewer 3 审稿意见]:\n## Reviewer 3 交叉回应：逐条回应 R1 和 R2\n\n---\n\n# 回应 Reviewer 1（方法严谨性 + 实验有效性）\n\n## Must-Fix\n\n**[AGREE] R1-N1: 缺乏闭环行为验证**\n同意这是论文最核心的弱点之一。论文所有分析均为 open-loop（probe R²、RSA ρ、attention 统计量），没有任何一个实验测量 L1 head ablation 对 LIBERO task success rate 的影响。Discussion（§5, line 28）承认 \"All analyses are open-loop; ... closed-loop evaluation is a natural extension\"，但这在 CoRL 这个强调 robotics 实践的 venue 中是不够的。\n\n补充我自己的观察：论文报告了 ablation 后 ground-truth MSE 无显著变化（Appendix A.7, \"$\\Delta\\text{MSE} \\approx 0$\"，原始 MSE=0.498，ablation 后 MSE=0.497），这反而让人困惑——如果 ablation 不改变 action error，那 routing 的功能意义是什么？闭环 success rate 测量将直接回答这个问题。\n\n**[AGREE with nuance] R1-N2: 从观察性到因果/机制性声称的推断过度**\n部分同意。R1 指出 matched-size ablation 的 specificity gap 很小（Table 23: instruction-dominant d=0.650 vs random d=0.601±0.021，差异仅 0.049），这确实削弱了 \"instruction-dominant heads 具有特殊因果角色\" 的声称。论文自己也承认这是 \"distributed, attention-graded routing rather than a dedicated subset\"（Appendix A.6），但主文的 framing 没有充分传达这一 nuance。\n\n但 R1 说证据 \"全是相关性的\" 不完全准确。论文包含多个 interventional 实验：\n- Dose-response ablation（Figure 1b）：4→32 heads ablation 产生 monotonic d 增长（0.482→0.639），这是因果操作\n- Counterfactual instruction analysis（Appendix Table 6）：4 种 perturbation 产生的 divergence 与 token novelty �
{"parentUuid":"aa5c14ea-b381-4bcb-ae78-254fcb1d4de3","isSidechain":false,"promptId":"865f5a08-fc40-4baf-a667-0404d968aaf6","type":"user","message":{"role":"user","content":"[Reviewer 3 审稿意见]:\n## Reviewer 3 交叉回应：逐条回应 R1 和 R2\n\n---\n\n# 回应 Reviewer 1（方法严谨性 + 实验有效性）\n\n## Must-Fix\n\n**[AGREE] R1-N1: 缺乏闭环行为验证**\n同意这是论文最核心的弱点之一。论文所有分析均为 open-loop（probe R²、RSA ρ、attention 统计量），没有任何一个实验测量 L1 head ablation 对 LIBERO task success rate 的影响。Discussion（§5, line 28）承认 \"All analyses are open-loop; ... closed-loop evaluation is a natural extension\"，但这在 CoRL 这个强调 robotics 实践的 venue 中是不够的。\n\n补充我自己的观察：论文报告
…[truncated 2238 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Bash",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 1123 · 2026-05-20T16:54:35.662465+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep \"Reviewer 3.*交叉回应\\|\\\\[Reviewer 3 审稿结果\\\\]\" /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-15-projects-vla-ssd--claude-sessions-review-director-ae8c68a6/de1bde7f-e731-400f-9905-932541adbff4.jsonl | grep \"审稿结果\" | head -3 | cut -c1-3000",
  "description": "Find R3 cross-response result messages"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Bash",
  "tool_args": {
    "command": "grep \"Reviewer 3.*交叉回应\\|\\\\[Reviewer 3 审稿结果\\\\]\" /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-15-projects-vla-ssd--claude-sessions-review-director-ae8c68a6/de1bde7f-e731-400f-9905-932541adbff4.jsonl | grep \"审稿结果\" | head -3 | cut -c1-3000",
    "description": "Find R3 cross-response result messages"
  }
}
```

</details>

---


### Tool result

_source line 1124 · 2026-05-20T16:54:35.764066+00:00_

{"type":"queue-operation","operation":"enqueue","timestamp":"2026-05-20T11:45:59.817Z","sessionId":"de1bde7f-e731-400f-9905-932541adbff4","content":"[Reviewer 3 审稿结果]:\n审稿报告已提交给 Review Director。\n\n核心发现：\n\n1. **[Critical] 超页限**：正文约 8.7 页，超出 CoRL 2026 的 8 页限制约 0.7 页。Discussion + Conclusion 延伸到第 9 页。\n2. **[Critical] 信息过载**：Abstract 塞入 15+ 个定量结果，Introduction 与 Abstract 高度重复，可读性差。\n3. **[Warning] 无首页 Figure**：Figure 1 直到第 6 页才出现。\n4. **[Warning] 层编号错误**：\"L1--L31 the 32 transformer layers\" 实为 31 个索引。\n5. **[Warning] 多条引用未更新为已发表版本**（OpenVLA、Prismatic VLMs 等）。\n6. **[Warning] Limitations 未作为独立 section**。\n\n可复现性方面做得较好（checkpoint、dataset、seed、compute 均报告），但未提交 supplementary code。引用验证无虚假引用。"}
{"parentUuid":"049908b2-2d74-4c9c-b582-63aa38eae686","isSidechain":false,"promptId":"b5b9dc8e-9bad-4304-a793-7ab54bab12dc","type":"user","message":{"role":"user","content":"[Reviewer 3 审稿结果]:\n审稿报告已提交给 Review Director。\n\n核心发现：\n\n1. **[Critical] 超页限**：正文约 8.7 页，超出 CoRL 2026 的 8 页限制约 0.7 页。Discussion + Conclusion 延伸到第 9 页。\n2. **[Critical] 信息过载**：Abstract 塞入 15+ 个定量结果，Introduction 与 Abstract 高度重复，可读性差。\n3. **[Warning] 无首页 Figure**：Figure 1 直到第 6 页才出现。\n4. **[Warning] 层编号错误**：\"L1--L31 the 32 transformer layers\" 实为 31 个索引。\n5. **[Warning] 多条引用未更新为已发表版本**（OpenVLA、Prismatic VLMs 等）。\n6. **[Warning] Limitations 未作为独立 section**。\n\n可复现性方面做得较好（checkpoint、dataset、seed、compute 均报告），但未提交 supplementary code。引用验证无虚假引用。"},"uuid":"35660fe9-e7b6-4ecf-8dd3-d269e8a74997","timestamp":"2026-05-20T11:45:59.895Z","permissionMode":"bypassPermissions","userType":"external","entrypoint":"sdk-cli","cwd":"/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/.claude/sessions/review_director_ae8c68a6","sessionId":"de1bde7f-e731-400f-9905-932541adbff4","version":"2.1.126","gitBranch":"HEAD"}
{"type":"queue-operation","operation":"enqueue","timestamp":"2026-05-20T11:51:31.933Z","sessionId":"de1bde7f-e731-400f-9905-932541adbff4","content":"[Reviewer 2 审稿意见]:\n## Reviewer 2 交叉回应：逐条回应 R1 和 R3\n\n---\
…[truncated 1946 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Bash",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 1125 · 2026-05-20T16:54:40.530968+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -c \"Reviewer 3.*交叉回应\" /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-15-projects-vla-ssd--claude-sessions-review-director-ae8c68a6/de1bde7f-e731-400f-9905-932541adbff4.jsonl",
  "description": "Count R3 cross-responses"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -c \"Reviewer 3.*交叉回应\" /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-15-projects-vla-ssd--claude-sessions-review-director-ae8c68a6/de1bde7f-e731-400f-9905-932541adbff4.jsonl",
    "description": "Count R3 cross-responses"
  }
}
```

</details>

---


### Tool result

_source line 1126 · 2026-05-20T16:54:40.581637+00:00_

7

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1127 · 2026-05-20T16:54:44.596986+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep \"Reviewer 3.*交叉回应\" /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-15-projects-vla-ssd--claude-sessions-review-director-ae8c68a6/de1bde7f-e731-400f-9905-932541adbff4.jsonl | head -2 | cut -c1-500",
  "description": "Check R3 cross-response content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Bash",
  "tool_args": {
    "command": "grep \"Reviewer 3.*交叉回应\" /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-15-projects-vla-ssd--claude-sessions-review-director-ae8c68a6/de1bde7f-e731-400f-9905-932541adbff4.jsonl | head -2 | cut -c1-500",
    "description": "Check R3 cross-response content"
  }
}
```

</details>

---


### Tool result

_source line 1128 · 2026-05-20T16:54:44.647686+00:00_

{"type":"queue-operation","operation":"enqueue","timestamp":"2026-05-20T11:51:19.288Z","sessionId":"de1bde7f-e731-400f-9905-932541adbff4","content":"[Reviewer 3 审稿意见]:\n## Reviewer 3 交叉回应：逐条回应 R1 和 R2\n\n---\n\n# 回应 Reviewer 1（方法严谨性 + 实验有效性）\n\n## Must-Fix\n\n**[AGREE] R1-N1: 缺乏闭环行为验证**\n同意这是论文最核心的弱点之一。论文所有分析均为 open-loop（probe R²、RSA ρ、attention 统计量），没有任�
{"parentUuid":"aa5c14ea-b381-4bcb-ae78-254fcb1d4de3","isSidechain":false,"promptId":"865f5a08-fc40-4baf-a667-0404d968aaf6","type":"user","message":{"role":"user","content":"[Reviewer 3 审稿意见]:\n## Reviewer 3 交叉回应：逐条回应 R1 和 R2\n\n---\n\n# 回应 Reviewer 1（方法严谨性 + 实验有效性）\n\n## Must-Fix\n\n**[AGREE] R1-N1: 缺乏闭环行为验证**\n同意这是论文最核心的弱点之一。论文所有分析均为 open-loop（probe R²、RSA ρ、attention �

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1129 · 2026-05-20T16:54:50.972133+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -A0 \"Reviewer 3 交叉回应：逐条回应 R1 和 R2\" /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-15-projects-vla-ssd--claude-sessions-review-director-ae8c68a6/de1bde7f-e731-400f-9905-932541adbff4.jsonl | head -1 | python3 -c \"\nimport sys\nline = sys.stdin.readline()\n# Extract content between first and second \\\\n---\\\\n or just print a big chunk\nidx = line.find('Reviewer 3 交叉回应')\nif idx >= 0:\n    text = line[idx:idx+12000]\n    # unescape\n    text = text.replace('\\\\\\\\n', '\\n').replace('\\\\n', '\\n')\n    print(text)\n\" 2>/dev/null | head -200",
  "description": "Extract R3 full cross-response text"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -A0 \"Reviewer 3 交叉回应：逐条回应 R1 和 R2\" /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-15-projects-vla-ssd--claude-sessions-review-director-ae8c68a6/de1bde7f-e731-400f-9905-932541adbff4.jsonl | head -1 | python3 -c \"\nimport sys\nline = sys.stdin.readline()\n# Extract content between first and second \\\\n---\\\\n or just print a big chunk\nidx = line.find('Reviewer 3 交叉回应')\nif idx >= 0:\n    text = line[idx:idx+12000]\n    # unescape\n    text = text.replace('\\\\\\\\n', '\\n').replace('\\\\n', '\\n')\n    print(text)\n\" 2>/dev/null | head -200",
    "description": "Extract R3 full cross-response text"
  }
}
```

</details>

---


### Tool result

_source line 1130 · 2026-05-20T16:54:51.073194+00:00_

Reviewer 3 交叉回应：逐条回应 R1 和 R2

---

# 回应 Reviewer 1（方法严谨性 + 实验有效性）

## Must-Fix

**[AGREE] R1-N1: 缺乏闭环行为验证**
同意这是论文最核心的弱点之一。论文所有分析均为 open-loop（probe R²、RSA ρ、attention 统计量），没有任何一个实验测量 L1 head ablation 对 LIBERO task success rate 的影响。Discussion（§5, line 28）承认 \"All analyses are open-loop; ... closed-loop evaluation is a natural extension\"，但这在 CoRL 这个强调 robotics 实践的 venue 中是不够的。

补充我自己的观察：论文报告了 ablation 后 ground-truth MSE 无显著变化（Appendix A.7, \"$\\Delta\\text{MSE} \\approx 0$\"，原始 MSE=0.498，ablation 后 MSE=0.497），这反而让人困惑——如果 ablation 不改变 action error，那 routing 的功能意义是什么？闭环 success rate 测量将直接回答这个问题。

**[AGREE with nuance] R1-N2: 从观察性到因果/机制性声称的推断过度**
部分同意。R1 指出 matched-size ablation 的 specificity gap 很小（Table 23: instruction-dominant d=0.650 vs random d=0.601±0.021，差异仅 0.049），这确实削弱了 \"instruction-dominant heads 具有特殊因果角色\" 的声称。论文自己也承认这是 \"distributed, attention-graded routing rather than a dedicated subset\"（Appendix A.6），但主文的 framing 没有充分传达这一 nuance。

但 R1 说证据 \"全是相关性的\" 不完全准确。论文包含多个 interventional 实验：
- Dose-response ablation（Figure 1b）：4→32 heads ablation 产生 monotonic d 增长（0.482→0.639），这是因果操作
- Counterfactual instruction analysis（Appendix Table 6）：4 种 perturbation 产生的 divergence 与 token novelty 完美相关（Spearman ρ=1.0），这也是 interventional
- L1 vs deeper-layer ablation（§4.5）：L1 效应 > L8 > L13 的 decay pattern 是因果性的

真正的问题不在于证据类型（interventional vs correlational），而在于 specificity 不够强：instruction-dominant heads 的效应仅比 random heads 大 8%。标题 \"Routes\" 暗示的因果 specificity 超过了数据支持的程度。

**[AGREE] R1-N3: 跨架构泛化声称证据不足**
完全同意。2 architectures × 1 benchmark family（LIBERO-Goal + LIBERO-Spatial 仍是同一 benchmark suite）不足以支撑 \"consistent across two VLA architectures\" 的泛化声称。TraceVLA 仅测试了 5 个 tasks（§4.5 line 67: \"matching its training set\"），且 Table 24 显示两个架构的 exit-layer R² 存在差异（0.488 vs 0.557），论文将其归因于 \"possibly reflecting architectural differences in late-layer processing\"（Discussion line 21）——这是 post-hoc speculation。

## Should-Fix

**[AGREE] R1-W1: Cohen's d 独立性假设**
同意这是统计方法上的问题。Token-level observa
…[truncated 8263 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Bash",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 1131 · 2026-05-20T16:55:05.735145+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__read_project_file",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__read_project_file",
    "max_results": "2"
  }
}
```

</details>

---


### Tool result

_source line 1132 · 2026-05-20T16:55:05.785876+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1133 · 2026-05-20T16:55:09.701396+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/review_issues.yaml | head -100",
  "description": "Read current review_issues.yaml header"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/review_issues.yaml | head -100",
    "description": "Read current review_issues.yaml header"
  }
}
```

</details>

---


### Tool result

_source line 1134 · 2026-05-20T16:55:09.752257+00:00_

issues:
  # ============================================================
  # Round 1-8 历史 issues（全部 resolved，压缩保留）
  # ============================================================
  - id: R1-N1-old
    summary: "Untrained baseline 无法隔离 VLA fine-tuning vs Llama-2 语言预训练的贡献"
    category: experiment
    severity: critical
    status: resolved
    first_raised_round: 1
    last_seen_round: 2
    resolution: "三条件数据完整整合。"
    resolution_round: 3
    mentions: []
    action_items: []
  - id: R1-N2-old
    summary: "单一模型 Title/Abstract 使用复数 'VLAs' 构成 overclaim"
    category: framing
    severity: critical
    status: resolved
    first_raised_round: 1
    last_seen_round: 2
    resolution: "Title 改为单数。"
    resolution_round: 3
    mentions: []
    action_items: []
  - id: R1-N4-old
    summary: "Design implications 完全基于 correlational evidence"
    category: framing
    severity: critical
    status: resolved
    first_raised_round: 1
    last_seen_round: 2
    resolution: "Abstract 使用 hedge 语气。"
    resolution_round: 3
    mentions: []
    action_items: []
  - id: R1-N3-old
    summary: "RSA best-vs-best selection bias"
    category: experiment
    severity: warning
    status: resolved
    first_raised_round: 1
    last_seen_round: 2
    resolution: "Same-layer comparison 为 primary evidence。"
    resolution_round: 3
    mentions: []
    action_items: []
  - id: R2-N1-old
    summary: "Neo et al. (ICLR 2025) 未引用"
    category: framing
    severity: warning
    status: resolved
    first_raised_round: 1
    last_seen_round: 2
    resolution: "已引用。"
    resolution_round: 3
    mentions: []
    action_items: []
  - id: R2-W1-old
    summary: "Related Work 引用覆盖度不足"
    category: writing
    severity: warning
    status: resolved
    first_raised_round: 1
    last_seen_round: 2
    resolution: "引用数量达标。"
    resolution_round: 3
    mentions: []
    action_items: []
  - id: R1-W1-old
    summary: "'Instruction-blind' claim 过强"
    category: framing
    severity: warning
    status
…[truncated 628 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1135 · 2026-05-20T16:55:12.613789+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "wc -l /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/review_issues.yaml",
  "description": "Count lines in review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Bash",
  "tool_args": {
    "command": "wc -l /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/review_issues.yaml",
    "description": "Count lines in review_issues.yaml"
  }
}
```

</details>

---


### Tool result

_source line 1136 · 2026-05-20T16:55:12.664444+00:00_

855 /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/review_issues.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1137 · 2026-05-20T16:55:15.525901+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep \"^  - id:\" /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/review_issues.yaml",
  "description": "List all issue IDs"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Bash",
  "tool_args": {
    "command": "grep \"^  - id:\" /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/review_issues.yaml",
    "description": "List all issue IDs"
  }
}
```

</details>

---


### Tool result

_source line 1138 · 2026-05-20T16:55:15.626802+00:00_

  - id: R1-N1-old
  - id: R1-N2-old
  - id: R1-N4-old
  - id: R1-N3-old
  - id: R2-N1-old
  - id: R2-W1-old
  - id: R1-W1-old
  - id: R1-W2-old
  - id: R3-N1-old
  - id: R3-N2-old
  - id: R3-W5-old
  - id: R4-N1
  - id: R4-N2
  - id: R4-N3
  - id: R4-W1
  - id: R4-W2
  - id: R4-W3
  - id: R4-W4
  - id: R9-N1
  - id: R9-N2
  - id: R9-N3
  - id: R9-N4
  - id: R9-N5
  - id: R9-N6
  - id: R9-W1
  - id: R9-W2
  - id: R9-W3
  - id: R9-W4
  - id: R9-W5
  - id: R9-W6
  - id: R9-W7
  - id: R9-I1
  - id: R9-I2
  - id: R9-I3
  - id: R10-Q1
  - id: R12-N1
  - id: R12-N2
  - id: R12-N3
  - id: R12-W1
  - id: R12-W2
  - id: R12-W3
  - id: R12-W4
  - id: R12-W5
  - id: R12-W6
  - id: R12-I1
  - id: R12-I2
  - id: R12-DIV1
  - id: R13-W1
  - id: R13-I1
  - id: R13-I2
  - id: R14-N1
  - id: R14-W1
  - id: R14-W2
  - id: R14-W3
  - id: R14-I1
  - id: R14-I2
  - id: R14-I3

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Bash",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 1139 · 2026-05-20T16:55:19.041051+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -A20 \"id: R14-I3\" /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/review_issues.yaml",
  "description": "Read last issue entry to understand current format"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -A20 \"id: R14-I3\" /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/review_issues.yaml",
    "description": "Read last issue entry to understand current format"
  }
}
```

</details>

---


### Tool result

_source line 1140 · 2026-05-20T16:55:19.091799+00:00_

  - id: R14-I3
    summary: "Permutation test 仅 1,000 shuffles（建议 ≥10,000）"
    category: method
    severity: info
    status: open
    first_raised_round: 14
    last_seen_round: 14
    mentions:
      - round: 14
        reviewers: [1, 2]
        note: "R1-Minor-3 提出，R2 AGREE。效应极大（15-23 SD）所以不影响结论，但统计实践建议增加。"
    action_items: []
    resolution: ""
    resolution_round: null

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1141 · 2026-05-20T16:55:22.906706+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/review_issues.yaml",
  "offset": "790"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/review_issues.yaml",
    "offset": "790"
  }
}
```

</details>

---


### Tool result

_source line 1142 · 2026-05-20T16:55:22.907156+00:00_

790	        status: pending
791	    resolution: ""
792	    resolution_round: null
793	
794	  - id: R14-W3
795	    summary: "缺失引用：Aghajanyan et al. (ACL 2021) + Kumar et al. (NeurIPS 2022)"
796	    category: writing
797	    severity: warning
798	    status: open
799	    first_raised_round: 14
800	    last_seen_round: 14
801	    mentions:
802	      - round: 14
803	        reviewers: [1, 2]
804	        note: "R2 提出，R1 AGREE。Aghajanyan (intrinsic dimensionality of fine-tuning) 和 Kumar (fine-tuning distorts pretrained features) 与本文核心问题直接相关。"
805	    action_items:
806	      - round: 14
807	        action: "引用 Aghajanyan et al. (ACL 2021) 和 Kumar et al. (NeurIPS 2022)"
808	        assigned_to: research_director
809	        status: pending
810	    resolution: ""
811	    resolution_round: null
812	
813	  - id: R14-I1
814	    summary: "Footnote 1 两个 pipeline R² 值差异未解释"
815	    category: writing
816	    severity: info
817	    status: open
818	    first_raised_round: 14
819	    last_seen_round: 14
820	    mentions:
821	      - round: 14
822	        reviewers: [1]
823	        note: "R1-Minor-2。两个 pipeline 的差异是什么？读者无法判断哪组数字更可靠。"
824	    action_items: []
825	    resolution: ""
826	    resolution_round: null
827	
828	  - id: R14-I2
829	    summary: "Leave-one-out p ≤ 0.083 不应表述为 'robust'"
830	    category: writing
831	    severity: info
832	    status: open
833	    first_raised_round: 14
834	    last_seen_round: 14
835	    mentions:
836	      - round: 14
837	        reviewers: [1, 2]
838	        note: "R1-Minor-5 提出，R2 AGREE。p=0.083 按任何常规标准不能称为 robust。"
839	    action_items: []
840	    resolution: ""
841	    resolution_round: null
842	
843	  - id: R14-I3
844	    summary: "Permutation test 仅 1,000 shuffles（建议 ≥10,000）"
845	    category: method
846	    severity: info
847	    status: open
848	    first_raised_round: 14
849	    last_seen_round: 14
850	    mentions:
851	      - round: 14
852	        reviewers: [1, 2]
853	        note: "R1-Minor-3 提出，R2 AGREE。效应极大（15-23 SD）所以不影响结论，但统计实践建
…[truncated 84 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1143 · 2026-05-20T16:55:33.690102+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/review_issues.yaml",
  "limit": "100",
  "offset": "0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/review_issues.yaml",
    "limit": "100",
    "offset": "0"
  }
}
```

</details>

---


### Tool result

_source line 1144 · 2026-05-20T16:55:33.740846+00:00_

0	issues:
1	  # ============================================================
2	  # Round 1-8 历史 issues（全部 resolved，压缩保留）
3	  # ============================================================
4	  - id: R1-N1-old
5	    summary: "Untrained baseline 无法隔离 VLA fine-tuning vs Llama-2 语言预训练的贡献"
6	    category: experiment
7	    severity: critical
8	    status: resolved
9	    first_raised_round: 1
10	    last_seen_round: 2
11	    resolution: "三条件数据完整整合。"
12	    resolution_round: 3
13	    mentions: []
14	    action_items: []
15	  - id: R1-N2-old
16	    summary: "单一模型 Title/Abstract 使用复数 'VLAs' 构成 overclaim"
17	    category: framing
18	    severity: critical
19	    status: resolved
20	    first_raised_round: 1
21	    last_seen_round: 2
22	    resolution: "Title 改为单数。"
23	    resolution_round: 3
24	    mentions: []
25	    action_items: []
26	  - id: R1-N4-old
27	    summary: "Design implications 完全基于 correlational evidence"
28	    category: framing
29	    severity: critical
30	    status: resolved
31	    first_raised_round: 1
32	    last_seen_round: 2
33	    resolution: "Abstract 使用 hedge 语气。"
34	    resolution_round: 3
35	    mentions: []
36	    action_items: []
37	  - id: R1-N3-old
38	    summary: "RSA best-vs-best selection bias"
39	    category: experiment
40	    severity: warning
41	    status: resolved
42	    first_raised_round: 1
43	    last_seen_round: 2
44	    resolution: "Same-layer comparison 为 primary evidence。"
45	    resolution_round: 3
46	    mentions: []
47	    action_items: []
48	  - id: R2-N1-old
49	    summary: "Neo et al. (ICLR 2025) 未引用"
50	    category: framing
51	    severity: warning
52	    status: resolved
53	    first_raised_round: 1
54	    last_seen_round: 2
55	    resolution: "已引用。"
56	    resolution_round: 3
57	    mentions: []
58	    action_items: []
59	  - id: R2-W1-old
60	    summary: "Related Work 引用覆盖度不足"
61	    category: writing
62	    severity: warning
63	    status: resolved
64	    first_raised_round: 1
65	    last_seen_round: 2
66	    resolutio
…[truncated 918 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1145 · 2026-05-20T16:55:39.262430+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/review_issues.yaml",
  "description": "Read full review_issues.yaml for update",
  "timeout": "10000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/review_issues.yaml",
    "description": "Read full review_issues.yaml for update",
    "timeout": "10000"
  }
}
```

</details>

---


### Tool result

_source line 1146 · 2026-05-20T16:55:39.313598+00:00_

issues:
  # ============================================================
  # Round 1-8 历史 issues（全部 resolved，压缩保留）
  # ============================================================
  - id: R1-N1-old
    summary: "Untrained baseline 无法隔离 VLA fine-tuning vs Llama-2 语言预训练的贡献"
    category: experiment
    severity: critical
    status: resolved
    first_raised_round: 1
    last_seen_round: 2
    resolution: "三条件数据完整整合。"
    resolution_round: 3
    mentions: []
    action_items: []
  - id: R1-N2-old
    summary: "单一模型 Title/Abstract 使用复数 'VLAs' 构成 overclaim"
    category: framing
    severity: critical
    status: resolved
    first_raised_round: 1
    last_seen_round: 2
    resolution: "Title 改为单数。"
    resolution_round: 3
    mentions: []
    action_items: []
  - id: R1-N4-old
    summary: "Design implications 完全基于 correlational evidence"
    category: framing
    severity: critical
    status: resolved
    first_raised_round: 1
    last_seen_round: 2
    resolution: "Abstract 使用 hedge 语气。"
    resolution_round: 3
    mentions: []
    action_items: []
  - id: R1-N3-old
    summary: "RSA best-vs-best selection bias"
    category: experiment
    severity: warning
    status: resolved
    first_raised_round: 1
    last_seen_round: 2
    resolution: "Same-layer comparison 为 primary evidence。"
    resolution_round: 3
    mentions: []
    action_items: []
  - id: R2-N1-old
    summary: "Neo et al. (ICLR 2025) 未引用"
    category: framing
    severity: warning
    status: resolved
    first_raised_round: 1
    last_seen_round: 2
    resolution: "已引用。"
    resolution_round: 3
    mentions: []
    action_items: []
  - id: R2-W1-old
    summary: "Related Work 引用覆盖度不足"
    category: writing
    severity: warning
    status: resolved
    first_raised_round: 1
    last_seen_round: 2
    resolution: "引用数量达标。"
    resolution_round: 3
    mentions: []
    action_items: []
  - id: R1-W1-old
    summary: "'Instruction-blind' claim 过强"
    category: framing
    severity: warning
    status
…[truncated 23376 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Bash",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 1147 · 2026-05-20T16:56:59.198351+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts && python3 << 'PYEOF'\nimport yaml\n\nwith open('review_issues.yaml', 'r') as f:\n    data = yaml.safe_load(f)\n\nissues = data['issues']\nissue_map = {i['id']: i for i in issues}\n\n# 1. R12-N2 (page limit) - was resolved R13, R3 says 8.7 pages again → reopen\niss = issue_map['R12-N2']\niss['status'] = 'open'\niss['last_seen_round'] = 14\niss['resolution'] = ''\niss['resolution_round'] = None\niss['mentions'] = iss.get('mentions', [])\niss['mentions'].append({\n    'round': 14,\n    'reviewers': [3],\n    'note': \"R3-N1 critical: 正文约 8.7 页，超出 8 页限制约 0.7 页。Discussion + Conclusion 延伸到第 9 页。R13 声称已修复但 R14 fresh review 发现回归。\"\n})\niss['action_items'] = iss.get('action_items', [])\niss['action_items'].append({\n    'round': 14,\n    'action': '将 Discussion Mechanistic interpretation 和 Functional stages 移至 Appendix，压缩 Introduction 重复内容',\n    'assigned_to': 'research_director',\n    'status': 'pending'\n})\n\n# 2. R12-N3 (info overload) - was resolved R13, R3 says abstract has 15+ quant results → reopen\niss = issue_map['R12-N3']\niss['status'] = 'open'\niss['last_seen_round'] = 14\niss['resolution'] = ''\niss['resolution_round'] = None\niss['mentions'] = iss.get('mentions', [])\niss['mentions'].append({\n    'round': 14,\n    'reviewers': [3],\n    'note': \"R3-N2 critical: Abstract 仍含 15+ 定量结果，Introduction 与 Abstract 80% 重复。R13 声称已修复但 R14 fresh review 发现回归。\"\n})\niss['action_items'] = iss.get('action_items', [])\niss['action_items'].append({\n    'round': 14,\n    'action': 'Abstract 只保留 3 个核心发现的定性描述 + 1-2 个关键数字；Introduction 聚焦 motivation',\n    'assigned_to': 'research_director',\n    'status': 'pending'\n})\n\n# 3. R12-W1 (no teaser figure) - was resolved R13, R3 says Figure 1 on page 6 → reopen\niss = issue_map['R12-W1']\niss['status'] = 'open'\niss['last_seen_round'] = 14\niss['resolution'] = ''\niss['resolution_round'] = None\niss['mentions'] = iss.get('mentions', [])\niss['mentions'].append({\n    'round': 14,\n    'reviewers': [3],\n    'note': \"R3-W1: Figure 1 出现在 PDF page 6 而非 page 1。R13 声称新增 Figure 1 但 R14 发现仍不在首页。\"\n})\n\n# 4. R12-W2 (layer numbering) - was resolved R13, R3 found it again → reopen\niss = issue_map['R12-W2']\niss['status'] = 'open'\niss['last_seen_round'] = 14\niss['resolution'] = ''\niss['resolution_round'] = None\niss['mentions'] = iss.get('mentions', [])\niss['mentions'].append({\n    'round': 14,\n    'reviewers': [3],\n    'note': \"R3-W2: method.tex L26 'L1--L31 the 32 transformer layers' 仍有 off-by-one 错误（31 个索引 ≠ 32 层）。R13 声称已修复但 R14 发现回归。\"\n})\n\n# 5. R12-W3 (arXiv refs) - already in_progress, add R3 to mention\niss = issue_map['R12-W3']\niss['last_seen_round'] = 14\nfor m in iss['mentions']:\n    if m['round'] == 14:\n        m['reviewers'] = sorted(set(m['reviewers'] + [3]))\n        m['note'] += \" R3-W3 独立发现同一问题并列出 6 条具体引用需更新（kim2024_openvla, karamcheti2024, touvron2023, belrose2023, padalkar2023, black2024_pi0）。\"\n        break\n\n# 6. R12-I1 (terminology) - add R3 to mention\niss = issue_map['R12-I1']\niss['last_seen_round'] = 14\nfor m in iss['mentions']:\n    if m['round'] == 14:\n        m['reviewers'] = sorted(set(m['reviewers'] + [3]))\n        m['note'] += \" R3-W5 独立发现同一问题：readout/last_preaction、instruction-dominant/dominant/instruction heads、7-D action vectors/actions 混用。\"\n        break\n\n# 7. R12-I2 (Limitations format) - add R3 mention\niss = issue_map['R12-I2']\niss['last_seen_round'] = 14\niss['mentions'].append({\n    'round': 14,\n    'reviewers': [3],\n    'note': \"R3-W4: Limitations 仍是 Discussion 的 paragraph 而非独立 section，不满足 CoRL 2026 要求。\"\n})\n\n# 8. R9-N2 (closed-loop) - add R3 to R14 mention\niss = issue_map['R9-N2']\nfor m in iss['mentions']:\n    if m['round'] == 14:\n        m['reviewers'] = sorted(set(m['reviewers'] + [3]))\n        m['note'] += \" R3 AGREE，补充：ablation 后 MSE≈0 反而让人困惑——routing 的功能意义需要 closed-loop 验证。\"\n        break\n\n# 9. R9-W1 (CoRL scope) - add R3 to R14 mention\niss = issue_map['R9-W1']\nfor m in iss['mentions']:\n    if m['round'] == 14:\n        m['reviewers'] = sorted(set(m['reviewers'] + [3]))\n        m['note'] += \" R3 强烈 AGREE：更适合 ICML/NeurIPS interpretability track。\"\n        break\n\n# 10. R14-N1 (convergent claim) - add R3\niss = issue_map['R14-N1']\nfor m in iss['mentions']:\n    if m['round'] == 14:\n        m['reviewers'] = sorted(set(m['reviewers'] + [3]))\n        m['note'] += \" R3 完全 AGREE。\"\n        break\n\n# 11. R9-N6 (N=10 bootstrap) - add R3\niss = issue_map['R9-N6']\nfor m in iss['mentions']:\n    if m['round'] == 14:\n        m['reviewers'] = sorted(set(m['reviewers'] + [3]))\n        m['note'] += \" R3 AGREE：N=6 vs N=4 的 Mann-Whitney U p=0.033 在如此小 N 下解释力有限。\"\n        break\n\n# 12. R9-W4 (Cohen's d) - add R3\niss = issue_map['R9-W4']\nfor m in iss['mentions']:\n    if m['round'] == 14:\n        m['reviewers'] = sorted(set(m['reviewers'] + [3]))\n        m['note'] += \" R3 AGREE：token-level observations 有强时序相关性，主文报告 token-level d=0.65 可能高估。\"\n        break\n\n# Add new R14 issues from R3\nnew_issues = [\n    {\n        'id': 'R14-W4',\n        'summary': 'GenAI disclosure 排版位置异常（References 后、Appendix 前）',\n        'category': 'format',\n        'severity': 'info',\n        'status': 'open',\n        'first_raised_round': 14,\n        'last_seen_round': 14,\n        'mentions': [{\n            'round': 14,\n            'reviewers': [3],\n            'note': 'R3-S6: Use of Generative AI 声明出现在 references 之后、appendix 之前的奇怪位置。建议移至论文末尾或 appendix 合适位置。'\n        }],\n        'action_items': [],\n        'resolution': '',\n        'resolution_round': None\n    },\n    {\n        'id': 'R14-W5',\n        'summary': 'Appendix resizebox 可能压缩字体至不可读',\n        'category': 'format',\n        'severity': 'info',\n        'status': 'open',\n        'first_raised_round': 14,\n        'last_seen_round': 14,\n        'mentions': [{\n            'round': 14,\n            'reviewers': [3],\n            'note': 'R3-S4: appendix.tex line 844 Table 17 的 resizebox 可能导致字体被压缩到不可读。建议使用 small/footnotesize。'\n        }],\n        'action_items': [],\n        'resolution': '',\n        'resolution_round': None\n    },\n    {\n        'id': 'R14-W6',\n        'summary': 'setlength float spacing 修改可能与 corl_2026 package 冲突',\n        'category': 'format',\n        'severity': 'info',\n        'status': 'open',\n        'first_raised_round': 14,\n        'last_seen_round': 14,\n        'mentions': [{\n            'round': 14,\n            'reviewers': [3],\n            'note': 'R3-S5: main.tex lines 16-20 的 setlength 调整可能在最终提交时与 corl_2026 package 默认值冲突。需确认这些修改是否被允许。'\n        }],\n        'action_items': [],\n        'resolution': '',\n        'resolution_round': None\n    },\n    {\n        'id': 'R14-W7',\n        'summary': \"Table 2 caption 缩写 'immed./gradual/incid.' 未解释\",\n        'category': 'writing',\n        'severity': 'info',\n        'status': 'open',\n        'first_raised_round': 14,\n        'last_seen_round': 14,\n        'mentions': [{\n            'round': 14,\n            'reviewers': [3],\n            'note': 'R3-S2: caption 中缩写未在 caption 内给出全称，不 standalone readable。'\n        }],\n        'action_items': [],\n        'resolution': '',\n        'resolution_round': None\n    },\n    {\n        'id': 'R14-DIV1',\n        'summary': \"MLP probe capacity：R1 认为过大，R3 认为已充分回应\",\n        'category': 'method',\n        'severity': 'info',\n        'status': 'open',\n        'first_raised_round': 14,\n        'last_seen_round': 14,\n        'mentions': [{\n            'round': 14,\n            'reviewers': [1, 3],\n            'note': 'R1-W5 认为 1.05M 参数 MLP probe capacity 过大。R3 REBUT：Appendix A.6 已用 linear probe 完整复现 inverted-U pattern（peak L14 R²=0.565），trained-untrained gap 更大（ΔR²=+0.324），充分 ruled out capacity concern。'\n        }],\n        'action_items': [],\n        'resolution': '',\n        'resolution_round': None\n    }\n]\n\nissues.extend(new_issues)\ndata['issues'] = issues\n\noutput = yaml.dump(data, allow_unicode=True, default_flow_style=False, sort_keys=False, width=200)\nwith open('review_issues_updated.yaml', 'w') as f:\n    f.write(output)\n\nprint(f\"Updated: {len(issues)} issues total\")\nprint(\"Reopened: R12-N2, R12-N3, R12-W1, R12-W2\")\nprint(\"New: R14-W4, R14-W5, R14-W6, R14-W7, R14-DIV1\")\nPYEOF",
  "description": "Update review_issues.yaml with R3 findings",
  "timeout": "15000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts && python3 << 'PYEOF'\nimport yaml\n\nwith open('review_issues.yaml', 'r') as f:\n    data = yaml.safe_load(f)\n\nissues = data['issues']\nissue_map = {i['id']: i for i in issues}\n\n# 1. R12-N2 (page limit) - was resolved R13, R3 says 8.7 pages again → reopen\niss = issue_map['R12-N2']\niss['status'] = 'open'\niss['last_seen_round'] = 14\niss['resolution'] = ''\niss['resolution_round'] = None\niss['mentions'] = iss.get('mentions', [])\niss['mentions'].append({\n    'round': 14,\n    'reviewers': [3],\n    'note': \"R3-N1 critical: 正文约 8.7 页，超出 8 页限制约 0.7 页。Discussion + Conclusion 延伸到第 9 页。R13 声称已修复但 R14 fresh review 发现回归。\"\n})\niss['action_items'] = iss.get('action_items', [])\niss['action_items'].append({\n    'round': 14,\n    'action': '将 Discussion Mechanistic interpretation 和 Functional stages 移至 Appendix，压缩 Introduction 重复内容',\n    'assigned_to': 'research_director',\n    'status': 'pending'\n})\n\n# 2. R12-N3 (info overload) - was resolved R13, R3 says abstract has 15+ quant results → reopen\niss = issue_map['R12-N3']\niss['status'] = 'open'\niss['last_seen_round'] = 14\niss['resolution'] = ''\niss['resolution_round'] = None\niss['mentions'] = iss.get('mentions', [])\niss['mentions'].append({\n    'round': 14,\n    'reviewers': [3],\n    'note': \"R3-N2 critical: Abstract 仍含 15+ 定量结果，Introduction 与 Abstract 80% 重复。R13 声称已修复但 R14 fresh review 发现回归。\"\n})\niss['action_items'] = iss.get('action_items', [])\niss['action_items'].append({\n    'round': 14,\n    'action': 'Abstract 只保留 3 个核心发现的定性描述 + 1-2 个关键数字；Introduction 聚焦 motivation',\n    'assigned_to': 'research_director',\n    'status': 'pending'\n})\n\n# 3. R12-W1 (no teaser figure) - was resolved R13, R3 says Figure 1 on page 6 → reopen\niss = issue_map['R12-W1']\niss['status'] = 'open'\niss['last_seen_round'] = 14\niss['resolution'] = ''\niss['resolution_round'] = None\niss['mentions'] = iss.get('mentions', [])\niss['mentions'].append({\n    'round': 14,\n    'reviewers': [3],\n    'note': \"R3-W1: Figure 1 出现在 PDF page 6 而非 page 1。R13 声称新增 Figure 1 但 R14 发现仍不在首页。\"\n})\n\n# 4. R12-W2 (layer numbering) - was resolved R13, R3 found it again → reopen\niss = issue_map['R12-W2']\niss['status'] = 'open'\niss['last_seen_round'] = 14\niss['resolution'] = ''\niss['resolution_round'] = None\niss['mentions'] = iss.get('mentions', [])\niss['mentions'].append({\n    'round': 14,\n    'reviewers': [3],\n    'note': \"R3-W2: method.tex L26 'L1--L31 the 32 transformer layers' 仍有 off-by-one 错误（31 个索引 ≠ 32 层）。R13 声称已修复但 R14 发现回归。\"\n})\n\n# 5. R12-W3 (arXiv refs) - already in_progress, add R3 to mention\niss = issue_map['R12-W3']\niss['last_seen_round'] = 14\nfor m in iss['mentions']:\n    if m['round'] == 14:\n        m['reviewers'] = sorted(set(m['reviewers'] + [3]))\n        m['note'] += \" R3-W3 独立发现同一问题并列出 6 条具体引用需更新（kim2024_openvla, karamcheti2024, touvron2023, belrose2023, padalkar2023, black2024_pi0）。\"\n        break\n\n# 6. R12-I1 (terminology) - add R3 to mention\niss = issue_map['R12-I1']\niss['last_seen_round'] = 14\nfor m in iss['mentions']:\n    if m['round'] == 14:\n        m['reviewers'] = sorted(set(m['reviewers'] + [3]))\n        m['note'] += \" R3-W5 独立发现同一问题：readout/last_preaction、instruction-dominant/dominant/instruction heads、7-D action vectors/actions 混用。\"\n        break\n\n# 7. R12-I2 (Limitations format) - add R3 mention\niss = issue_map['R12-I2']\niss['last_seen_round'] = 14\niss['mentions'].append({\n    'round': 14,\n    'reviewers': [3],\n    'note': \"R3-W4: Limitations 仍是 Discussion 的 paragraph 而非独立 section，不满足 CoRL 2026 要求。\"\n})\n\n# 8. R9-N2 (closed-loop) - add R3 to R14 mention\niss = issue_map['R9-N2']\nfor m in iss['mentions']:\n    if m['round'] == 14:\n        m['reviewers'] = sorted(set(m['reviewers'] + [3]))\n        m['note'] += \" R3 AGREE，补充：ablation 后 MSE≈0 反而让人困惑——routing 的功能意义需要 closed-loop 验证。\"\n        break\n\n# 9. R9-W1 (CoRL scope) - add R3 to R14 mention\niss = issue_map['R9-W1']\nfor m in iss['mentions']:\n    if m['round'] == 14:\n        m['reviewers'] = sorted(set(m['reviewers'] + [3]))\n        m['note'] += \" R3 强烈 AGREE：更适合 ICML/NeurIPS interpretability track。\"\n        break\n\n# 10. R14-N1 (convergent claim) - add R3\niss = issue_map['R14-N1']\nfor m in iss['mentions']:\n    if m['round'] == 14:\n        m['reviewers'] = sorted(set(m['reviewers'] + [3]))\n        m['note'] += \" R3 完全 AGREE。\"\n        break\n\n# 11. R9-N6 (N=10 bootstrap) - add R3\niss = issue_map['R9-N6']\nfor m in iss['mentions']:\n    if m['round'] == 14:\n        m['reviewers'] = sorted(set(m['reviewers'] + [3]))\n        m['note'] += \" R3 AGREE：N=6 vs N=4 的 Mann-Whitney U p=0.033 在如此小 N 下解释力有限。\"\n        break\n\n# 12. R9-W4 (Cohen's d) - add R3\niss = issue_map['R9-W4']\nfor m in iss['mentions']:\n    if m['round'] == 14:\n        m['reviewers'] = sorted(set(m['reviewers'] + [3]))\n        m['note'] += \" R3 AGREE：token-level observations 有强时序相关性，主文报告 token-level d=0.65 可能高估。\"\n        break\n\n# Add new R14 issues from R3\nnew_issues = [\n    {\n        'id': 'R14-W4',\n        'summary': 'GenAI disclosure 排版位置异常（References 后、Appendix 前）',\n        'category': 'format',\n        'severity': 'info',\n        'status': 'open',\n        'first_raised_round': 14,\n        'last_seen_round': 14,\n        'mentions': [{\n            'round': 14,\n            'reviewers': [3],\n            'note': 'R3-S6: Use of Generative AI 声明出现在 references 之后、appendix 之前的奇怪位置。建议移至论文末尾或 appendix 合适位置。'\n        }],\n        'action_items': [],\n        'resolution': '',\n        'resolution_round': None\n    },\n    {\n        'id': 'R14-W5',\n        'summary': 'Appendix resizebox 可能压缩字体至不可读',\n        'category': 'format',\n        'severity': 'info',\n        'status': 'open',\n        'first_raised_round': 14,\n        'last_seen_round': 14,\n        'mentions': [{\n            'round': 14,\n            'reviewers': [3],\n            'note': 'R3-S4: appendix.tex line 844 Table 17 的 resizebox 可能导致字体被压缩到不可读。建议使用 small/footnotesize。'\n        }],\n        'action_items': [],\n        'resolution': '',\n        'resolution_round': None\n    },\n    {\n        'id': 'R14-W6',\n        'summary': 'setlength float spacing 修改可能与 corl_2026 package 冲突',\n        'category': 'format',\n        'severity': 'info',\n        'status': 'open',\n        'first_raised_round': 14,\n        'last_seen_round': 14,\n        'mentions': [{\n            'round': 14,\n            'reviewers': [3],\n            'note': 'R3-S5: main.tex lines 16-20 的 setlength 调整可能在最终提交时与 corl_2026 package 默认值冲突。需确认这些修改是否被允许。'\n        }],\n        'action_items': [],\n        'resolution': '',\n        'resolution_round': None\n    },\n    {\n        'id': 'R14-W7',\n        'summary': \"Table 2 caption 缩写 'immed./gradual/incid.' 未解释\",\n        'category': 'writing',\n        'severity': 'info',\n        'status': 'open',\n        'first_raised_round': 14,\n        'last_seen_round': 14,\n        'mentions': [{\n            'round': 14,\n            'reviewers': [3],\n            'note': 'R3-S2: caption 中缩写未在 caption 内给出全称，不 standalone readable。'\n        }],\n        'action_items': [],\n        'resolution': '',\n        'resolution_round': None\n    },\n    {\n        'id': 'R14-DIV1',\n        'summary': \"MLP probe capacity：R1 认为过大，R3 认为已充分回应\",\n        'category': 'method',\n        'severity': 'info',\n        'status': 'open',\n        'first_raised_round': 14,\n        'last_seen_round': 14,\n        'mentions': [{\n            'round': 14,\n            'reviewers': [1, 3],\n            'note': 'R1-W5 认为 1.05M 参数 MLP probe capacity 过大。R3 REBUT：Appendix A.6 已用 linear probe 完整复现 inverted-U pattern（peak L14 R²=0.565），trained-untrained gap 更大（ΔR²=+0.324），充分 ruled out capacity concern。'\n        }],\n        'action_items': [],\n        'resolution': '',\n        'resolution_round': None\n    }\n]\n\nissues.extend(new_issues)\ndata['issues'] = issues\n\noutput = yaml.dump(data, allow_unicode=True, default_flow_style=False, sort_keys=False, width=200)\nwith open('review_issues_updated.yaml', 'w') as f:\n    f.write(output)\n\nprint(f\"Updated: {len(issues)} issues total\")\nprint(\"Reopened: R12-N2, R12-N3, R12-W1, R12-W2\")\nprint(\"New: R14-W4, R14-W5, R14-W6, R14-W7, R14-DIV1\")\nPYEOF",
    "description": "Update review_issues.yaml with R3 findings",
    "timeout": "15000"
  }
}
```

</details>

---


### Tool result

_source line 1148 · 2026-05-20T16:56:59.399693+00:00_

Updated: 62 issues total
Reopened: R12-N2, R12-N3, R12-W1, R12-W2
New: R14-W4, R14-W5, R14-W6, R14-W7, R14-DIV1
Shell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/.claude/sessions/review_director_ae8c68a6

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Bash",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 1149 · 2026-05-20T16:57:03.416121+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/review_issues_updated.yaml | head -30",
  "description": "Verify updated YAML format"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/review_issues_updated.yaml | head -30",
    "description": "Verify updated YAML format"
  }
}
```

</details>

---


### Tool result

_source line 1150 · 2026-05-20T16:57:03.617506+00:00_

issues:
- id: R1-N1-old
  summary: Untrained baseline 无法隔离 VLA fine-tuning vs Llama-2 语言预训练的贡献
  category: experiment
  severity: critical
  status: resolved
  first_raised_round: 1
  last_seen_round: 2
  resolution: 三条件数据完整整合。
  resolution_round: 3
  mentions: []
  action_items: []
- id: R1-N2-old
  summary: 单一模型 Title/Abstract 使用复数 'VLAs' 构成 overclaim
  category: framing
  severity: critical
  status: resolved
  first_raised_round: 1
  last_seen_round: 2
  resolution: Title 改为单数。
  resolution_round: 3
  mentions: []
  action_items: []
- id: R1-N4-old
  summary: Design implications 完全基于 correlational evidence
  category: framing
  severity: critical
  status: resolved
  first_raised_round: 1
  last_seen_round: 2

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Bash",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 1151 · 2026-05-20T16:57:06.779093+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/review_issues_updated.yaml | wc -c",
  "description": "Check file size"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/review_issues_updated.yaml | wc -c",
    "description": "Check file size"
  }
}
```

</details>

---


### Tool result

_source line 1152 · 2026-05-20T16:57:06.981033+00:00_

30310

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Bash",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 1153 · 2026-05-20T16:57:10.042717+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/review_issues_updated.yaml",
  "description": "Read full updated YAML for submission",
  "timeout": "10000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/review_issues_updated.yaml",
    "description": "Read full updated YAML for submission",
    "timeout": "10000"
  }
}
```

</details>

---


### Tool result

_source line 1154 · 2026-05-20T16:57:10.093780+00:00_

&lt;persisted-output>
Output too large (29.6KB). Full output saved to: /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-15-projects-vla-ssd--claude-sessions-review-director-ae8c68a6/b356f826-c226-4cb3-a4f5-b640539b4a7f/tool-results/b1wunnypf.txt

Preview (first 2KB):
issues:
- id: R1-N1-old
  summary: Untrained baseline 无法隔离 VLA fine-tuning vs Llama-2 语言预训练的贡献
  category: experiment
  severity: critical
  status: resolved
  first_raised_round: 1
  last_seen_round: 2
  resolution: 三条件数据完整整合。
  resolution_round: 3
  mentions: []
  action_items: []
- id: R1-N2-old
  summary: 单一模型 Title/Abstract 使用复数 'VLAs' 构成 overclaim
  category: framing
  severity: critical
  status: resolved
  first_raised_round: 1
  last_seen_round: 2
  resolution: Title 改为单数。
  resolution_round: 3
  mentions: []
  action_items: []
- id: R1-N4-old
  summary: Design implications 完全基于 correlational evidence
  category: framing
  severity: critical
  status: resolved
  first_raised_round: 1
  last_seen_round: 2
  resolution: Abstract 使用 hedge 语气。
  resolution_round: 3
  mentions: []
  action_items: []
- id: R1-N3-old
  summary: RSA best-vs-best selection bias
  category: experiment
  severity: warning
  status: resolved
  first_raised_round: 1
  last_seen_round: 2
  resolution: Same-layer comparison 为 primary evidence。
  resolution_round: 3
  mentions: []
  action_items: []
- id: R2-N1-old
  summary: Neo et al. (ICLR 2025) 未引用
  category: framing
  severity: warning
  status: resolved
  first_raised_round: 1
  last_seen_round: 2
  resolution: 已引用。
  resolution_round: 3
  mentions: []
  action_items: []
- id: R2-W1-old
  summary: Related Work 引用覆盖度不足
  category: writing
  severity: warning
  status: resolved
  first_raised_round: 1
  last_seen_round: 2
  resolution: 引用数量达标。
  resolution_round: 3
  mentions: []
  action_items: []
- id: R1-W1-old
  summary: '''Instruction-blind'' claim 过强'
  category: framing
  severity: warning
  status: resolved
  first_raised_round: 1
…[truncated 284 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Bash",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 1155 · 2026-05-20T16:57:13.858663+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-15-projects-vla-ssd--claude-sessions-review-director-ae8c68a6/b356f826-c226-4cb3-a4f5-b640539b4a7f/tool-results/b1wunnypf.txt",
  "limit": "50",
  "offset": "0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-15-projects-vla-ssd--claude-sessions-review-director-ae8c68a6/b356f826-c226-4cb3-a4f5-b640539b4a7f/tool-results/b1wunnypf.txt",
    "limit": "50",
    "offset": "0"
  }
}
```

</details>

---


### Tool result

_source line 1156 · 2026-05-20T16:57:13.909336+00:00_

0	issues:
1	- id: R1-N1-old
2	  summary: Untrained baseline 无法隔离 VLA fine-tuning vs Llama-2 语言预训练的贡献
3	  category: experiment
4	  severity: critical
5	  status: resolved
6	  first_raised_round: 1
7	  last_seen_round: 2
8	  resolution: 三条件数据完整整合。
9	  resolution_round: 3
10	  mentions: []
11	  action_items: []
12	- id: R1-N2-old
13	  summary: 单一模型 Title/Abstract 使用复数 'VLAs' 构成 overclaim
14	  category: framing
15	  severity: critical
16	  status: resolved
17	  first_raised_round: 1
18	  last_seen_round: 2
19	  resolution: Title 改为单数。
20	  resolution_round: 3
21	  mentions: []
22	  action_items: []
23	- id: R1-N4-old
24	  summary: Design implications 完全基于 correlational evidence
25	  category: framing
26	  severity: critical
27	  status: resolved
28	  first_raised_round: 1
29	  last_seen_round: 2
30	  resolution: Abstract 使用 hedge 语气。
31	  resolution_round: 3
32	  mentions: []
33	  action_items: []
34	- id: R1-N3-old
35	  summary: RSA best-vs-best selection bias
36	  category: experiment
37	  severity: warning
38	  status: resolved
39	  first_raised_round: 1
40	  last_seen_round: 2
41	  resolution: Same-layer comparison 为 primary evidence。
42	  resolution_round: 3
43	  mentions: []
44	  action_items: []
45	- id: R2-N1-old
46	  summary: Neo et al. (ICLR 2025) 未引用
47	  category: framing
48	  severity: warning
49	  status: resolved

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1157 · 2026-05-20T16:57:17.623599+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/review_issues_updated.yaml",
  "description": "Read full YAML for mcp update",
  "timeout": "10000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/review_issues_updated.yaml",
    "description": "Read full YAML for mcp update",
    "timeout": "10000"
  }
}
```

</details>

---


### Tool result

_source line 1158 · 2026-05-20T16:57:17.674482+00:00_

&lt;persisted-output>
Output too large (29.6KB). Full output saved to: /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-15-projects-vla-ssd--claude-sessions-review-director-ae8c68a6/b356f826-c226-4cb3-a4f5-b640539b4a7f/tool-results/b4mjg9mo3.txt

Preview (first 2KB):
issues:
- id: R1-N1-old
  summary: Untrained baseline 无法隔离 VLA fine-tuning vs Llama-2 语言预训练的贡献
  category: experiment
  severity: critical
  status: resolved
  first_raised_round: 1
  last_seen_round: 2
  resolution: 三条件数据完整整合。
  resolution_round: 3
  mentions: []
  action_items: []
- id: R1-N2-old
  summary: 单一模型 Title/Abstract 使用复数 'VLAs' 构成 overclaim
  category: framing
  severity: critical
  status: resolved
  first_raised_round: 1
  last_seen_round: 2
  resolution: Title 改为单数。
  resolution_round: 3
  mentions: []
  action_items: []
- id: R1-N4-old
  summary: Design implications 完全基于 correlational evidence
  category: framing
  severity: critical
  status: resolved
  first_raised_round: 1
  last_seen_round: 2
  resolution: Abstract 使用 hedge 语气。
  resolution_round: 3
  mentions: []
  action_items: []
- id: R1-N3-old
  summary: RSA best-vs-best selection bias
  category: experiment
  severity: warning
  status: resolved
  first_raised_round: 1
  last_seen_round: 2
  resolution: Same-layer comparison 为 primary evidence。
  resolution_round: 3
  mentions: []
  action_items: []
- id: R2-N1-old
  summary: Neo et al. (ICLR 2025) 未引用
  category: framing
  severity: warning
  status: resolved
  first_raised_round: 1
  last_seen_round: 2
  resolution: 已引用。
  resolution_round: 3
  mentions: []
  action_items: []
- id: R2-W1-old
  summary: Related Work 引用覆盖度不足
  category: writing
  severity: warning
  status: resolved
  first_raised_round: 1
  last_seen_round: 2
  resolution: 引用数量达标。
  resolution_round: 3
  mentions: []
  action_items: []
- id: R1-W1-old
  summary: '''Instruction-blind'' claim 过强'
  category: framing
  severity: warning
  status: resolved
  first_raised_round: 1
…[truncated 284 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1159 · 2026-05-20T16:57:20.987149+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\nwith open('/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/review_issues_updated.yaml', 'r') as f:\n    content = f.read()\nprint(len(content))\n\"",
  "description": "Get exact YAML size"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"\nwith open('/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/review_issues_updated.yaml', 'r') as f:\n    content = f.read()\nprint(len(content))\n\"",
    "description": "Get exact YAML size"
  }
}
```

</details>

---


### Tool result

_source line 1160 · 2026-05-20T16:57:21.087890+00:00_

25911

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Bash",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 1161 · 2026-05-20T16:57:26.557949+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\nwith open('/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/review_issues_updated.yaml', 'r') as f:\n    content = f.read()\n# Just verify it's valid yaml\nimport yaml\ndata = yaml.safe_load(content)\nprint(f'Valid YAML with {len(data[\\\"issues\\\"])} issues')\n# Print all IDs\nfor i in data['issues']:\n    status = i.get('status','?')\n    sev = i.get('severity','?')\n    print(f'  {i[\\\"id\\\"]:20s} {status:15s} {sev}')\n\"",
  "description": "Validate YAML and list all issues"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"\nwith open('/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/review_issues_updated.yaml', 'r') as f:\n    content = f.read()\n# Just verify it's valid yaml\nimport yaml\ndata = yaml.safe_load(content)\nprint(f'Valid YAML with {len(data[\\\"issues\\\"])} issues')\n# Print all IDs\nfor i in data['issues']:\n    status = i.get('status','?')\n    sev = i.get('severity','?')\n    print(f'  {i[\\\"id\\\"]:20s} {status:15s} {sev}')\n\"",
    "description": "Validate YAML and list all issues"
  }
}
```

</details>

---


### Tool result

_source line 1162 · 2026-05-20T16:57:26.708940+00:00_

Valid YAML with 62 issues
  R1-N1-old            resolved        critical
  R1-N2-old            resolved        critical
  R1-N4-old            resolved        critical
  R1-N3-old            resolved        warning
  R2-N1-old            resolved        warning
  R2-W1-old            resolved        warning
  R1-W1-old            resolved        warning
  R1-W2-old            resolved        warning
  R3-N1-old            resolved        warning
  R3-N2-old            resolved        warning
  R3-W5-old            resolved        info
  R4-N1                resolved        critical
  R4-N2                resolved        critical
  R4-N3                resolved        critical
  R4-W1                resolved        warning
  R4-W2                resolved        warning
  R4-W3                resolved        warning
  R4-W4                resolved        warning
  R9-N1                wont_fix        critical
  R9-N2                wont_fix        critical
  R9-N3                resolved        warning
  R9-N4                resolved        warning
  R9-N5                resolved        warning
  R9-N6                open            warning
  R9-W1                open            critical
  R9-W2                resolved        warning
  R9-W3                resolved        warning
  R9-W4                open            warning
  R9-W5                resolved        warning
  R9-W6                resolved        warning
  R9-W7                resolved        warning
  R9-I1                resolved        info
  R9-I2                resolved        info
  R9-I3                resolved        info
  R10-Q1               resolved        info
  R12-N1               resolved        critical
  R12-N2               open            critical
  R12-N3               open            critical
  R12-W1               open            warning
  R12-W2               open            warning
  R12-W3               in_progress     warning
  R12-W4               resolved        warning
  R
…[truncated 901 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Bash",
  "elapsed_ms": 150
}
```

</details>

---


### Tool call

_source line 1163 · 2026-05-20T16:57:31.075586+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 << 'PYEOF'\nwith open('/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/review_issues_updated.yaml', 'r') as f:\n    yaml_content = f.read()\n# Write to a temp file that we can reference\nwith open('/tmp/review_issues_for_update.yaml', 'w') as f:\n    f.write(yaml_content)\nprint(\"READY\")\nprint(f\"Size: {len(yaml_content)} chars\")\nPYEOF",
  "description": "Prepare YAML content for MCP submission"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 << 'PYEOF'\nwith open('/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/review_issues_updated.yaml', 'r') as f:\n    yaml_content = f.read()\n# Write to a temp file that we can reference\nwith open('/tmp/review_issues_for_update.yaml', 'w') as f:\n    f.write(yaml_content)\nprint(\"READY\")\nprint(f\"Size: {len(yaml_content)} chars\")\nPYEOF",
    "description": "Prepare YAML content for MCP submission"
  }
}
```

</details>

---


### Tool result

_source line 1164 · 2026-05-20T16:57:31.127203+00:00_

READY
Size: 25911 chars

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Bash",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 1165 · 2026-05-20T16:57:33.889793+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/tmp/review_issues_for_update.yaml",
  "limit": "600"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/tmp/review_issues_for_update.yaml",
    "limit": "600"
  }
}
```

</details>

---


### Tool result

_source line 1166 · 2026-05-20T16:57:33.940806+00:00_

1	issues:
2	- id: R1-N1-old
3	  summary: Untrained baseline 无法隔离 VLA fine-tuning vs Llama-2 语言预训练的贡献
4	  category: experiment
5	  severity: critical
6	  status: resolved
7	  first_raised_round: 1
8	  last_seen_round: 2
9	  resolution: 三条件数据完整整合。
10	  resolution_round: 3
11	  mentions: []
12	  action_items: []
13	- id: R1-N2-old
14	  summary: 单一模型 Title/Abstract 使用复数 'VLAs' 构成 overclaim
15	  category: framing
16	  severity: critical
17	  status: resolved
18	  first_raised_round: 1
19	  last_seen_round: 2
20	  resolution: Title 改为单数。
21	  resolution_round: 3
22	  mentions: []
23	  action_items: []
24	- id: R1-N4-old
25	  summary: Design implications 完全基于 correlational evidence
26	  category: framing
27	  severity: critical
28	  status: resolved
29	  first_raised_round: 1
30	  last_seen_round: 2
31	  resolution: Abstract 使用 hedge 语气。
32	  resolution_round: 3
33	  mentions: []
34	  action_items: []
35	- id: R1-N3-old
36	  summary: RSA best-vs-best selection bias
37	  category: experiment
38	  severity: warning
39	  status: resolved
40	  first_raised_round: 1
41	  last_seen_round: 2
42	  resolution: Same-layer comparison 为 primary evidence。
43	  resolution_round: 3
44	  mentions: []
45	  action_items: []
46	- id: R2-N1-old
47	  summary: Neo et al. (ICLR 2025) 未引用
48	  category: framing
49	  severity: warning
50	  status: resolved
51	  first_raised_round: 1
52	  last_seen_round: 2
53	  resolution: 已引用。
54	  resolution_round: 3
55	  mentions: []
56	  action_items: []
57	- id: R2-W1-old
58	  summary: Related Work 引用覆盖度不足
59	  category: writing
60	  severity: warning
61	  status: resolved
62	  first_raised_round: 1
63	  last_seen_round: 2
64	  resolution: 引用数量达标。
65	  resolution_round: 3
66	  mentions: []
67	  action_items: []
68	- id: R1-W1-old
69	  summary: '''Instruction-blind'' claim 过强'
70	  category: framing
71	  severity: warning
72	  status: resolved
73	  first_raised_round: 1
74	  last_seen_round: 2
75	  resolution: MLP probe 双重验证。
76	  resolution_round: 3
77	  ment
…[truncated 16187 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 1167 · 2026-05-20T16:57:40.923610+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\nwith open('/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/review_issues_updated.yaml', 'r') as f:\n    print(f.read())\n\" > /tmp/yaml_for_mcp.txt 2>&1\necho \"Done: $(wc -c < /tmp/yaml_for_mcp.txt) bytes\"",
  "description": "Prepare YAML content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"\nwith open('/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/review_issues_updated.yaml', 'r') as f:\n    print(f.read())\n\" > /tmp/yaml_for_mcp.txt 2>&1\necho \"Done: $(wc -c < /tmp/yaml_for_mcp.txt) bytes\"",
    "description": "Prepare YAML content"
  }
}
```

</details>

---


### Tool result

_source line 1168 · 2026-05-20T16:57:40.974325+00:00_

Done: 30311 bytes

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1169 · 2026-05-20T16:57:45.491596+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 << 'PYEOF'\nimport json\nwith open('/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/review_issues_updated.yaml', 'r') as f:\n    content = f.read()\n# Just print first 100 and last 100 chars to verify\nprint(\"FIRST:\", content[:100])\nprint(\"---\")\nprint(\"LAST:\", content[-100:])\nPYEOF",
  "description": "Verify YAML content boundaries"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 << 'PYEOF'\nimport json\nwith open('/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/review_issues_updated.yaml', 'r') as f:\n    content = f.read()\n# Just print first 100 and last 100 chars to verify\nprint(\"FIRST:\", content[:100])\nprint(\"---\")\nprint(\"LAST:\", content[-100:])\nPYEOF",
    "description": "Verify YAML content boundaries"
  }
}
```

</details>

---


### Tool result

_source line 1170 · 2026-05-20T16:57:45.642755+00:00_

FIRST: issues:
- id: R1-N1-old
  summary: Untrained baseline 无法隔离 VLA fine-tuning vs Llama-2 语言预训练的贡献
  cat
---
LAST: +0.324），充分 ruled out capacity concern。
  action_items: []
  resolution: ''
  resolution_round: null

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Bash",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 1171 · 2026-05-20T16:57:49.708398+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "wc -l /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/review_issues_updated.yaml",
  "description": "Count lines"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Bash",
  "tool_args": {
    "command": "wc -l /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/review_issues_updated.yaml",
    "description": "Count lines"
  }
}
```

</details>

---


### Tool result

_source line 1172 · 2026-05-20T16:57:49.759106+00:00_

975 /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/review_issues_updated.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1173 · 2026-05-20T16:57:53.121677+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/review_issues_updated.yaml",
  "offset": "600"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/review_issues_updated.yaml",
    "offset": "600"
  }
}
```

</details>

---


### Tool result

_source line 1174 · 2026-05-20T16:57:53.172549+00:00_

600	    note: 3/3 已更新。仍有 belrose2023, padalkar2023 待更新。
601	  - round: 14
602	    reviewers:
603	    - 2
604	    - 3
605	    note: R2-M1 再次提及：brohan2023 (RT-2)、belrose2023、black2024 (π₀) 需检查是否有正式版本。 R3-W3 独立发现同一问题并列出 6 条具体引用需更新（kim2024_openvla, karamcheti2024, touvron2023, belrose2023, padalkar2023, black2024_pi0）。
606	  action_items:
607	  - round: 14
608	    action: 检查并更新所有可更新的 arXiv 引用至正式版本
609	    assigned_to: research_director
610	    status: pending
611	  resolution: ''
612	  resolution_round: null
613	- id: R12-W4
614	  summary: 缺失重要 related work
615	  category: writing
616	  severity: warning
617	  status: resolved
618	  first_raised_round: 12
619	  last_seen_round: 13
620	  resolution: 6/6 缺失引用全部补齐。
621	  resolution_round: 13
622	  mentions: []
623	  action_items: []
624	- id: R12-W5
625	  summary: 与 Grant et al. 和 Häon et al. 的区分不够清晰
626	  category: writing
627	  severity: warning
628	  status: resolved
629	  first_raised_round: 12
630	  last_seen_round: 14
631	  resolution: Related Work 加显式 what-vs-where 对比段落。
632	  resolution_round: 13
633	  mentions:
634	  - round: 14
635	    reviewers:
636	    - 1
637	    - 2
638	    note: R2-W1 再次提出增量贡献不清晰。R1 AGREE with nuance（token-level 粒度和 multi-method convergence 设计是差异化）。建议增加明确 'what we add' 段落。
639	  action_items: []
640	- id: R12-W6
641	  summary: FDR 多重比较校正细节不足
642	  category: method
643	  severity: warning
644	  status: resolved
645	  first_raised_round: 12
646	  last_seen_round: 14
647	  resolution: BH 方法 + α=0.05 + 33-layer family per metric 完整报告。
648	  resolution_round: 13
649	  mentions:
650	  - round: 14
651	    reviewers:
652	    - 1
653	    - 2
654	    note: R1-W1 提出更深层关切：FDR 仅在每个 metric 的 33 层内，未对全局 family-wise error rate 校正。R2 AGREE 但指出这是 ML interpretability 文献常见做法，属 should-fix。
655	  action_items:
656	  - round: 14
657	    action: 考虑在 Appendix 添加全局 Bonferroni-adjusted p-values 作为 robustness check
658	    assigned_to: research_director
659	    status: pending
660	- id: R12-I1
661	  summary: 术语不一致：read
…[truncated 9575 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1175 · 2026-05-20T16:57:59.748124+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 << 'PYEOF'\nwith open('/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/review_issues_updated.yaml', 'r') as f:\n    content = f.read()\nprint(content)\nPYEOF",
  "description": "Output YAML content for copy",
  "timeout": "10000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 << 'PYEOF'\nwith open('/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/review_issues_updated.yaml', 'r') as f:\n    content = f.read()\nprint(content)\nPYEOF",
    "description": "Output YAML content for copy",
    "timeout": "10000"
  }
}
```

</details>

---


### Tool result

_source line 1176 · 2026-05-20T16:57:59.849132+00:00_

&lt;persisted-output>
Output too large (29.6KB). Full output saved to: /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-15-projects-vla-ssd--claude-sessions-review-director-ae8c68a6/b356f826-c226-4cb3-a4f5-b640539b4a7f/tool-results/bzbe8ab79.txt

Preview (first 2KB):
issues:
- id: R1-N1-old
  summary: Untrained baseline 无法隔离 VLA fine-tuning vs Llama-2 语言预训练的贡献
  category: experiment
  severity: critical
  status: resolved
  first_raised_round: 1
  last_seen_round: 2
  resolution: 三条件数据完整整合。
  resolution_round: 3
  mentions: []
  action_items: []
- id: R1-N2-old
  summary: 单一模型 Title/Abstract 使用复数 'VLAs' 构成 overclaim
  category: framing
  severity: critical
  status: resolved
  first_raised_round: 1
  last_seen_round: 2
  resolution: Title 改为单数。
  resolution_round: 3
  mentions: []
  action_items: []
- id: R1-N4-old
  summary: Design implications 完全基于 correlational evidence
  category: framing
  severity: critical
  status: resolved
  first_raised_round: 1
  last_seen_round: 2
  resolution: Abstract 使用 hedge 语气。
  resolution_round: 3
  mentions: []
  action_items: []
- id: R1-N3-old
  summary: RSA best-vs-best selection bias
  category: experiment
  severity: warning
  status: resolved
  first_raised_round: 1
  last_seen_round: 2
  resolution: Same-layer comparison 为 primary evidence。
  resolution_round: 3
  mentions: []
  action_items: []
- id: R2-N1-old
  summary: Neo et al. (ICLR 2025) 未引用
  category: framing
  severity: warning
  status: resolved
  first_raised_round: 1
  last_seen_round: 2
  resolution: 已引用。
  resolution_round: 3
  mentions: []
  action_items: []
- id: R2-W1-old
  summary: Related Work 引用覆盖度不足
  category: writing
  severity: warning
  status: resolved
  first_raised_round: 1
  last_seen_round: 2
  resolution: 引用数量达标。
  resolution_round: 3
  mentions: []
  action_items: []
- id: R1-W1-old
  summary: '''Instruction-blind'' claim 过强'
  category: framing
  severity: warning
  status: resolved
  first_raised_round: 1
…[truncated 284 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Bash",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 1177 · 2026-05-20T16:58:13.021331+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/review_issues_updated.yaml > /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/review_issues.yaml\necho \"Copied updated YAML to review_issues.yaml\"",
  "description": "Copy updated YAML to the canonical location"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/review_issues_updated.yaml > /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/review_issues.yaml\necho \"Copied updated YAML to review_issues.yaml\"",
    "description": "Copy updated YAML to the canonical location"
  }
}
```

</details>

---


### Tool result

_source line 1178 · 2026-05-20T16:58:13.072096+00:00_

Copied updated YAML to review_issues.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1179 · 2026-05-20T17:00:48.336405+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "vla-ssd",
  "issues_yaml": "issues:\n- id: R1-N1-old\n  summary: \"Untrained baseline 无法隔离 VLA fine-tuning vs Llama-2 语言预训练的贡献\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  resolution: \"三条件数据完整整合。\"\n  resolution_round: 3\n  mentions: []\n  action_items: []\n- id: R1-N2-old\n  summary: \"单一模型 Title/Abstract 使用复数 'VLAs' 构成 overclaim\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  resolution: \"Title 改为单数。\"\n  resolution_round: 3\n  mentions: []\n  action_items: []\n- id: R1-N4-old\n  summary: \"Design implications 完全基于 correlational evidence\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  resolution: \"Abstract 使用 hedge 语气。\"\n  resolution_round: 3\n  mentions: []\n  action_items: []\n- id: R1-N3-old\n  summary: \"RSA best-vs-best selection bias\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  resolution: \"Same-layer comparison 为 primary evidence。\"\n  resolution_round: 3\n  mentions: []\n  action_items: []\n- id: R2-N1-old\n  summary: \"Neo et al. (ICLR 2025) 未引用\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  resolution: \"已引用。\"\n  resolution_round: 3\n  mentions: []\n  action_items: []\n- id: R2-W1-old\n  summary: \"Related Work 引用覆盖度不足\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  resolution: \"引用数量达标。\"\n  resolution_round: 3\n  mentions: []\n  action_items: []\n- id: R1-W1-old\n  summary: \"'Instruction-blind' claim 过强\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  resolution: \"MLP probe 双重验证。\"\n  resolution_round: 3\n  mentions: []\n  action_items: []\n- id: R1-W2-old\n  summary: \"CKA 反转 RSA 排序处理不充分\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  resolution: \"Method 新增 'Why RSA over CKA'。\"\n  resolution_round: 2\n  mentions: []\n  action_items: []\n- id: R3-N1-old\n  summary: \"Limitations 格式\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  resolution: \"改为 subsection。\"\n  resolution_round: 3\n  mentions: []\n  action_items: []\n- id: R3-N2-old\n  summary: \"em-dash AI 写作标志\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  resolution: \"零残留。\"\n  resolution_round: 2\n  mentions: []\n  action_items: []\n- id: R3-W5-old\n  summary: \"无 code/data 释放声明\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  resolution: \"Conclusion 加声明。\"\n  resolution_round: 3\n  mentions: []\n  action_items: []\n- id: R4-N1\n  summary: \"C1 是 causal mask 必然结果 + probe trivially easy\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 14\n  resolution: \"Abstract 'confirms expected' + 'consistent with causal attention mask' + 'framework sanity check' 三重降格。Contribution (iii) 定位为 methodology validation。全文一致。\"\n  resolution_round: 13\n  mentions:\n    - round: 9\n      reviewers: [1, 2]\n      note: \"R9-W2: C1 在 Abstract/Introduction 占比失衡。\"\n    - round: 10\n      reviewers: [1, 2]\n      note: \"RESOLVED。降格处理到位。\"\n    - round: 12\n      reviewers: [2, 3]\n      note: \"复发。R2-N1: 虽已降为 sanity check，但 Title 和 Abstract 仍将架构约束呈现为核心贡献。\"\n    - round: 13\n      reviewers: [1, 2]\n      note: \"RESOLVED。三重降格处理精准。\"\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R2 初审重提 Finding 3 trivial（N3 critical），但 R1 REBUT 区分三层：(a) image_mean at-chance 确实 trivial；(b) readout 三条件梯度非 trivial；(c) training asymmetry 非 causal mask 可预测。R2 接受反驳，降为 should-fix。共识：image_mean 部分是 sanity check，但 readout 梯度和 training asymmetry 是实质发现，Abstract 措辞需更精准区分。\"\n  action_items:\n    - round: 14\n      action: \"Abstract 'confirms expected functional specialization' 措辞应区分 trivial (image_mean) 和 non-trivial (readout gradient, training asymmetry) 部分\"\n      assigned_to: research_director\n      status: pending\n- id: R4-N2\n  summary: \"RSA inverted-U metric-dependent，CKA 反转\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 14\n  resolution: \"C3 降为 qualified observation + §4.4 CKA 正文讨论。\"\n  resolution_round: 8\n  mentions:\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R1-W3 再次提出 RSA vs CKA 反转处理不足。R2 部分 REBUT（Appendix A.1 有更多讨论），但同意核心关切成立。\"\n  action_items: []\n- id: R4-N3\n  summary: \"L1 ablation 使用 5 demos\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 5\n  resolution: \"改用 50 demos (N=63,228)。\"\n  resolution_round: 5\n  mentions: []\n  action_items: []\n- id: R4-W1\n  summary: \"RSA best-vs-best n.s. 未标注\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 5\n  resolution: \"已标注。\"\n  resolution_round: 5\n  mentions: []\n  action_items: []\n- id: R4-W2\n  summary: \"缺乏多重比较校正\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 5\n  resolution: \"FDR 已应用。\"\n  resolution_round: 5\n  mentions: []\n  action_items: []\n- id: R4-W3\n  summary: \"Probe N 未报告，MLP capacity 控制不充分\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 7\n  resolution: \"Demo-level split 完全消除时间泄漏。\"\n  resolution_round: 7\n  mentions: []\n  action_items: []\n- id: R4-W4\n  summary: \"Frozen encoder confound\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 5\n  resolution: \"Introduction + Discussion 说明。\"\n  resolution_round: 5\n  mentions: []\n  action_items: []\n- id: R9-N1\n  summary: \"单一模型(OpenVLA-7B)单一基准(LIBERO)，无法支撑 VLA 通用性\"\n  category: experiment\n  severity: critical\n  status: wont_fix\n  first_raised_round: 9\n  last_seen_round: 14\n  mentions:\n    - round: 9\n      reviewers: [1, 2]\n      note: \"双方 AGREE critical。\"\n    - round: 14\n      reviewers: [1, 2, 3]\n      note: \"R14 fresh review 再次提出。R1-W4 + R2-W4: LIBERO-only 的 tabletop manipulation 可能是多个发现的充分条件。三位 Reviewer 均 AGREE。\"\n  action_items:\n    - round: 10\n      action: \"Rebuttal 应对：causal mask 泛化 + testable predictions\"\n      assigned_to: research_director\n      status: pending\n  resolution: \"Claims 已限定为 'causal-decoder VLAs'。实验数据仍为 2 个架构，结构性局限不变。\"\n  resolution_round: null\n- id: R9-N2\n  summary: \"所有分析均为 open-loop，无 closed-loop 机器人评估\"\n  category: experiment\n  severity: critical\n  status: wont_fix\n  first_raised_round: 9\n  last_seen_round: 14\n  mentions:\n    - round: 9\n      reviewers: [1, 2]\n      note: \"双方 AGREE critical。\"\n    - round: 13\n      reviewers: [1, 2]\n      note: \"PARTIALLY_RESOLVED。'orthogonal contribution' 措辞仍需修改。\"\n    - round: 14\n      reviewers: [1, 2, 3]\n      note: \"R14 fresh review 以最高优先级再次提出。三位 Reviewer 均 AGREE。R3 补充：ablation 后 MSE≈0 反而让人困惑——routing 的功能意义需要 closed-loop 验证。\"\n  action_items:\n    - round: 14\n      action: \"验证至少一个 actionable implication（建议：在已有 LIBERO rollout 数据上计算 L1 attention entropy 与 task failure 的相关性）\"\n      assigned_to: research_director\n      status: pending\n  resolution: \"Open-loop 结构性局限不变。R14 建议了低成本验证方案。\"\n  resolution_round: null\n- id: R9-N3\n  summary: \"'Causal' 术语在 observational open-loop 分析中使用不当\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 10\n  resolution: \"Discussion 'Causal' → 'Interventional'；§4.3 heading 改为 'Open-loop functional sensitivity'。\"\n  resolution_round: 10\n  mentions: []\n  action_items: []\n- id: R9-N4\n  summary: \"Ablation 使 R² 增加的 paradox 未充分解释\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 11\n  resolution: \"Discussion 加 information-computation dissociation 解释。\"\n  resolution_round: 11\n  mentions: []\n  action_items: []\n- id: R9-N5\n  summary: \"Counterfactual 的 'semantic distance' 概念未定义\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 10\n  resolution: \"改用 Jaccard token overlap / token novelty。\"\n  resolution_round: 10\n  mentions: []\n  action_items: []\n- id: R9-N6\n  summary: \"N=10 tasks 的 RSA bootstrap 统计功效不足\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 9\n  last_seen_round: 14\n  resolution: \"\"\n  resolution_round: null\n  mentions:\n    - round: 11\n      reviewers: [1]\n      note: \"RESOLVED（加了 power limitation 声明）。\"\n    - round: 14\n      reviewers: [1, 2, 3]\n      note: \"R14 fresh review 升级为 critical。三位 AGREE。新角度：TOST 等价性检验；R3 补充 Mann-Whitney U p=0.033 在 N=6 vs N=4 下解释力有限。\"\n  action_items:\n    - round: 14\n      action: \"提供 power analysis；对跨架构 convergence 考虑 TOST 等价性检验\"\n      assigned_to: research_director\n      status: pending\n- id: R9-W1\n  summary: \"CoRL scope fit 有限：纯 representational analysis，无物理机器人实验\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 9\n  last_seen_round: 14\n  resolution: \"\"\n  resolution_round: null\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"PARTIALLY_RESOLVED。Writing-level 改善但核心缺陷无法通过写作修复。\"\n    - round: 14\n      reviewers: [1, 2, 3]\n      note: \"三位 Reviewer 均以最高优先级提出。R3 强烈 AGREE：更适合 ICML/NeurIPS interpretability track。\"\n  action_items:\n    - round: 14\n      action: \"最低方案：验证一个 implication；最佳方案：补充 closed-loop 评估；备选：改投 ML venue\"\n      assigned_to: research_director\n      status: pending\n- id: R9-W2\n  summary: \"C1 在 Abstract/Introduction/Contributions 中占比失衡\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 10\n  resolution: \"C1 降为末句 sanity check。\"\n  resolution_round: 10\n  mentions: []\n  action_items: []\n- id: R9-W3\n  summary: \"Vision representation 训练效果微弱，framing 未充分反映\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 10\n  resolution: \"§4.4 标题改为 'Training primarily enhances readout decodability'。\"\n  resolution_round: 10\n  mentions: []\n  action_items: []\n- id: R9-W4\n  summary: \"Cohen's d 独立性假设违反\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 9\n  last_seen_round: 14\n  resolution: \"\"\n  resolution_round: null\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"RESOLVED（新增 trajectory-level d）。\"\n    - round: 14\n      reviewers: [1, 2, 3]\n      note: \"R1 重提 paired data 应用 paired effect size。R2 REBUT 偏差方向（paired d_z > standard d）。R3 AGREE token-level 有强时序相关性。共识：应报告 paired d_z 和配对相关系数 r。\"\n  action_items:\n    - round: 14\n      action: \"报告 paired Cohen's d_z 和配对相关系数 r；在 Method 中讨论 paired vs independent d\"\n      assigned_to: research_director\n      status: pending\n- id: R9-W5\n  summary: \"Pretrained Llama-2 base 的 9/32 heads 可能因 text in-distribution bias\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 10\n  resolution: \"Discussion 新增替代解释承认。\"\n  resolution_round: 10\n  mentions: []\n  action_items: []\n- id: R9-W6\n  summary: \"Specificity control 效果有限(d ratio 1.08×)\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 14\n  resolution: \"四组 matched-size 比较，framing 'distributed routing'。\"\n  resolution_round: 11\n  mentions:\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R1-W2 再次提出 ablation 因果推断过度表述。R2 AGREE but 不升级 severity。\"\n  action_items: []\n- id: R9-W7\n  summary: \"N=63,228 观测的独立性——有效独立单元远小于报告值\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 12\n  resolution: \"§4.1 新增 N_eff 说明。\"\n  resolution_round: 10\n  mentions: []\n  action_items: []\n- id: R9-I1\n  summary: \"缺失引用：Octo (Ghosh et al. 2024)\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 10\n  resolution: \"references.bib 新增。\"\n  resolution_round: 10\n  mentions: []\n  action_items: []\n- id: R9-I2\n  summary: \"Häon et al. 2025 的 sparse semantic directions 与 L1 routing heads 的关系未讨论\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 11\n  resolution: \"Discussion 加 where/what 互补连接。\"\n  resolution_round: 11\n  mentions: []\n  action_items: []\n- id: R9-I3\n  summary: \"多处小问题：Table 1 caption、脚注、accessed date\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 10\n  resolution: \"已修复。\"\n  resolution_round: 10\n  mentions: []\n  action_items: []\n- id: R10-Q1\n  summary: \"Per-task MSE breakdown：消融后 MSE 不变是否存在 task-level cancellation\"\n  category: experiment\n  severity: info\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 11\n  resolution: \"Appendix 加 per-task breakdown。\"\n  resolution_round: 11\n  mentions: []\n  action_items: []\n- id: R12-N1\n  summary: \"因果 overclaiming：Title 'Routes' 暗示因果机制\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 13\n  resolution: \"Title 'Routes'→'Reorganizes'，全文 'routing'→'redistributes'，零残留。\"\n  resolution_round: 13\n  mentions: []\n  action_items: []\n- id: R12-N2\n  summary: \"正文超出 CoRL 8 页限制\"\n  category: format\n  severity: critical\n  status: open\n  first_raised_round: 12\n  last_seen_round: 14\n  resolution: \"\"\n  resolution_round: null\n  mentions:\n    - round: 14\n      reviewers: [3]\n      note: \"R3-N1 critical: 正文约 8.7 页，超出 8 页限制约 0.7 页。Discussion + Conclusion 延伸到第 9 页。R13 声称已修复但 R14 fresh review 发现回归。\"\n  action_items:\n    - round: 14\n      action: \"将 Discussion Mechanistic interpretation 和 Functional stages 移至 Appendix，压缩 Introduction 重复内容\"\n      assigned_to: research_director\n      status: pending\n- id: R12-N3\n  summary: \"Abstract/Introduction 信息过载\"\n  category: writing\n  severity: critical\n  status: open\n  first_raised_round: 12\n  last_seen_round: 14\n  resolution: \"\"\n  resolution_round: null\n  mentions:\n    - round: 14\n      reviewers: [3]\n      note: \"R3-N2 critical: Abstract 仍含 15+ 定量结果，Introduction 与 Abstract 80% 重复。R13 声称已修复但 R14 fresh review 发现回归。\"\n  action_items:\n    - round: 14\n      action: \"Abstract 只保留 3 个核心发现的定性描述 + 1-2 个关键数字；Introduction 聚焦 motivation\"\n      assigned_to: research_director\n      status: pending\n- id: R12-W1\n  summary: \"无首页 teaser figure\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 12\n  last_seen_round: 14\n  resolution: \"\"\n  resolution_round: null\n  mentions:\n    - round: 14\n      reviewers: [3]\n      note: \"R3-W1: Figure 1 出现在 PDF page 6 而非 page 1。R13 声称新增 Figure 1 但 R14 发现仍不在首页。\"\n  action_items: []\n- id: R12-W2\n  summary: \"层编号 off-by-one\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 12\n  last_seen_round: 14\n  resolution: \"\"\n  resolution_round: null\n  mentions:\n    - round: 14\n      reviewers: [3]\n      note: \"R3-W2: method.tex L26 'L1--L31 the 32 transformer layers' 仍有 off-by-one 错误。R13 声称已修复但 R14 发现回归。\"\n  action_items: []\n- id: R12-W3\n  summary: \"多条引用使用 arXiv preprint 而非已发表版本\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 12\n  last_seen_round: 14\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"3/3 已更新。仍有 belrose2023, padalkar2023 待更新。\"\n    - round: 14\n      reviewers: [2, 3]\n      note: \"R2-M1 + R3-W3 独立发现。R3 列出 6 条具体引用需更新（kim2024_openvla, karamcheti2024, touvron2023, belrose2023, padalkar2023, black2024_pi0）。\"\n  action_items:\n    - round: 14\n      action: \"检查并更新所有可更新的 arXiv 引用至正式版本\"\n      assigned_to: research_director\n      status: pending\n  resolution: \"\"\n  resolution_round: null\n- id: R12-W4\n  summary: \"缺失重要 related work\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 13\n  resolution: \"6/6 缺失引用全部补齐。\"\n  resolution_round: 13\n  mentions: []\n  action_items: []\n- id: R12-W5\n  summary: \"与 Grant et al. 和 Häon et al. 的区分不够清晰\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 14\n  resolution: \"Related Work 加显式 what-vs-where 对比段落。\"\n  resolution_round: 13\n  mentions:\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R2-W1 再次提出增量贡献不清晰。R1 AGREE with nuance。\"\n  action_items: []\n- id: R12-W6\n  summary: \"FDR 多重比较校正细节不足\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 14\n  resolution: \"BH 方法 + α=0.05 + 33-layer family per metric 完整报告。\"\n  resolution_round: 13\n  mentions:\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R1-W1 提出更深层关切：FDR 仅在每个 metric 的 33 层内，未对全局 family-wise error rate 校正。\"\n  action_items:\n    - round: 14\n      action: \"考虑在 Appendix 添加全局 Bonferroni-adjusted p-values 作为 robustness check\"\n      assigned_to: research_director\n      status: pending\n- id: R12-I1\n  summary: \"术语不一致：readout token vs last_preaction\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 12\n  last_seen_round: 14\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"PARTIALLY_RESOLVED。Table 1 的 'last_preaction' 建议 caption 加映射说明。\"\n    - round: 14\n      reviewers: [1, 2, 3]\n      note: \"三位 Reviewer 均独立发现。R3-W5 列出全部混用实例。\"\n  action_items:\n    - round: 14\n      action: \"统一为 'readout token'，首次出现时定义；Table caption 加映射说明\"\n      assigned_to: research_director\n      status: pending\n  resolution: \"\"\n  resolution_round: null\n- id: R12-I2\n  summary: \"Limitations 未作为独立 section\"\n  category: format\n  severity: info\n  status: in_progress\n  first_raised_round: 12\n  last_seen_round: 14\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"PARTIALLY_RESOLVED。使用 paragraph 而非 subsection。\"\n    - round: 14\n      reviewers: [3]\n      note: \"R3-W4: Limitations 仍是 Discussion 的 paragraph 而非独立 section，不满足 CoRL 2026 要求。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n- id: R12-DIV1\n  summary: \"Title 'Language Routes' 是否误导\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 13\n  resolution: \"Title 'Routes'→'Reorganizes' 消除误导。\"\n  resolution_round: 13\n  mentions: []\n  action_items: []\n- id: R13-W1\n  summary: \"'Orthogonal contribution' 措辞对 closed-loop validation 过于 dismissive\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 13\n  last_seen_round: 14\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"建议改为 'complementary and necessary next step'。\"\n    - round: 14\n      reviewers: []\n      note: \"本轮未直接提及但被更广泛的 scope fit 讨论涵盖。Discussion 仍含 'orthogonal contribution' 原文。\"\n  action_items:\n    - round: 13\n      action: \"'orthogonal contribution' 改为 'complementary and necessary next step'\"\n      assigned_to: research_director\n      status: pending\n  resolution: \"\"\n  resolution_round: null\n- id: R13-I1\n  summary: \"附录 'robust attractor' 措辞较主文更强\"\n  category: framing\n  severity: info\n  status: open\n  first_raised_round: 13\n  last_seen_round: 13\n  mentions:\n    - round: 14\n      reviewers: []\n      note: \"本轮未直接提及但被 convergent claim 弱化建议涵盖。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n- id: R13-I2\n  summary: \"Spacing 压缩激进\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 13\n  last_seen_round: 13\n  mentions:\n    - round: 14\n      reviewers: []\n      note: \"本轮未提及。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n- id: R14-N1\n  summary: \"'Convergent reorganization' claim 从 N=2 同类架构得出，证据不足\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 14\n  last_seen_round: 14\n  mentions:\n    - round: 14\n      reviewers: [1, 2, 3]\n      note: \"三位 Reviewer 均 AGREE。Δ=0.003 可能反映架构共性而非训练通用规律。建议弱化为 'preliminary evidence'。\"\n  action_items:\n    - round: 14\n      action: \"将 'convergent reorganization' 弱化为 'shared tendency' 或 'preliminary evidence for convergence'\"\n      assigned_to: research_director\n      status: pending\n  resolution: \"\"\n  resolution_round: null\n- id: R14-W1\n  summary: \"Counterfactual instruction analysis 仅用 3/10 tasks，ρ=1.0 在 n=4 条件下仅 marginal\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 14\n  last_seen_round: 14\n  mentions:\n    - round: 14\n      reviewers: [1, 2]\n      note: \"3 tasks 选择 rationale 未报告，cross-task variance 未讨论。\"\n  action_items:\n    - round: 14\n      action: \"在全部 10 tasks 上复现 counterfactual 分析，或报告选择 rationale 和 cross-task variance\"\n      assigned_to: research_director\n      status: pending\n  resolution: \"\"\n  resolution_round: null\n- id: R14-W2\n  summary: \"单一训练 checkpoint 分析——不同 training seed 可能产生不同表征结构\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 14\n  last_seen_round: 14\n  mentions:\n    - round: 14\n      reviewers: [1, 2]\n      note: \"建议 Limitations 中讨论 training stochasticity 的潜在影响。\"\n  action_items:\n    - round: 14\n      action: \"Limitations 中讨论 training seed variance\"\n      assigned_to: research_director\n      status: pending\n  resolution: \"\"\n  resolution_round: null\n- id: R14-W3\n  summary: \"缺失引用：Aghajanyan et al. (ACL 2021) + Kumar et al. (NeurIPS 2022)\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 14\n  last_seen_round: 14\n  mentions:\n    - round: 14\n      reviewers: [1, 2]\n      note: \"两篇与本文核心问题直接相关的 fine-tuning representation 工作未引用。\"\n  action_items:\n    - round: 14\n      action: \"引用 Aghajanyan et al. (ACL 2021) 和 Kumar et al. (NeurIPS 2022)\"\n      assigned_to: research_director\n      status: pending\n  resolution: \"\"\n  resolution_round: null\n- id: R14-I1\n  summary: \"Footnote 1 两个 pipeline R² 值差异未解释\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 14\n  last_seen_round: 14\n  mentions:\n    - round: 14\n      reviewers: [1]\n      note: \"R1-Minor-2。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n- id: R14-I2\n  summary: \"Leave-one-out p ≤ 0.083 不应表述为 'robust'\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 14\n  last_seen_round: 14\n  mentions:\n    - round: 14\n      reviewers: [1, 2]\n      note: \"p=0.083 按任何常规标准不能称为 robust。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n- id: R14-I3\n  summary: \"Permutation test 仅 1,000 shuffles（建议 ≥10,000）\"\n  category: method\n  severity: info\n  status: open\n  first_raised_round: 14\n  last_seen_round: 14\n  mentions:\n    - round: 14\n      reviewers: [1, 2]\n      note: \"效应极大所以不影响结论，但统计实践建议增加。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n- id: R14-W4\n  summary: \"GenAI disclosure 排版位置异常（References 后、Appendix 前）\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 14\n  last_seen_round: 14\n  mentions:\n    - round: 14\n      reviewers: [3]\n      note: \"R3-S6: 建议移至论文末尾或 appendix 合适位置。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n- id: R14-W5\n  summary: \"Appendix resizebox 可能压缩字体至不可读\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 14\n  last_seen_round: 14\n  mentions:\n    - round: 14\n      reviewers: [3]\n      note: \"R3-S4: appendix.tex Table 17 的 resizebox 导致字体过小。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n- id: R14-W6\n  summary: \"setlength float spacing 修改可能与 corl_2026 package 冲突\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 14\n  last_seen_round: 14\n  mentions:\n    - round: 14\n      reviewers: [3]\n      note: \"R3-S5: main.tex lines 16-20 的 setlength 调整需确认是否被允许。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n- id: R14-W7\n  summary: \"Table 2 caption 缩写 'immed./gradual/incid.' 未解释\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 14\n  last_seen_round: 14\n  mentions:\n    - round: 14\n      reviewers: [3]\n      note: \"R3-S2: caption 中缩写未给出全称，不 standalone readable。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n- id: R14-DIV1\n  summary: \"MLP probe capacity：R1 认为过大，R3 认为已充分回应\"\n  category: method\n  severity: info\n  status: open\n  first_raised_round: 14\n  last_seen_round: 14\n  mentions:\n    - round: 14\n      reviewers: [1, 3]\n      note: \"R1-W5 认为 1.05M 参数过大。R3 REBUT：Appendix A.6 linear probe 完整复现 inverted-U pattern，capacity concern 已 ruled out。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "vla-ssd",
    "issues_yaml": "issues:\n- id: R1-N1-old\n  summary: \"Untrained baseline 无法隔离 VLA fine-tuning vs Llama-2 语言预训练的贡献\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  resolution: \"三条件数据完整整合。\"\n  resolution_round: 3\n  mentions: []\n  action_items: []\n- id: R1-N2-old\n  summary: \"单一模型 Title/Abstract 使用复数 'VLAs' 构成 overclaim\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  resolution: \"Title 改为单数。\"\n  resolution_round: 3\n  mentions: []\n  action_items: []\n- id: R1-N4-old\n  summary: \"Design implications 完全基于 correlational evidence\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  resolution: \"Abstract 使用 hedge 语气。\"\n  resolution_round: 3\n  mentions: []\n  action_items: []\n- id: R1-N3-old\n  summary: \"RSA best-vs-best selection bias\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  resolution: \"Same-layer comparison 为 primary evidence。\"\n  resolution_round: 3\n  mentions: []\n  action_items: []\n- id: R2-N1-old\n  summary: \"Neo et al. (ICLR 2025) 未引用\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  resolution: \"已引用。\"\n  resolution_round: 3\n  mentions: []\n  action_items: []\n- id: R2-W1-old\n  summary: \"Related Work 引用覆盖度不足\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  resolution: \"引用数量达标。\"\n  resolution_round: 3\n  mentions: []\n  action_items: []\n- id: R1-W1-old\n  summary: \"'Instruction-blind' claim 过强\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  resolution: \"MLP probe 双重验证。\"\n  resolution_round: 3\n  mentions: []\n  action_items: []\n- id: R1-W2-old\n  summary: \"CKA 反转 RSA 排序处理不充分\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  resolution: \"Method 新增 'Why RSA over CKA'。\"\n  resolution_round: 2\n  mentions: []\n  action_items: []\n- id: R3-N1-old\n  summary: \"Limitations 格式\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  resolution: \"改为 subsection。\"\n  resolution_round: 3\n  mentions: []\n  action_items: []\n- id: R3-N2-old\n  summary: \"em-dash AI 写作标志\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  resolution: \"零残留。\"\n  resolution_round: 2\n  mentions: []\n  action_items: []\n- id: R3-W5-old\n  summary: \"无 code/data 释放声明\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  resolution: \"Conclusion 加声明。\"\n  resolution_round: 3\n  mentions: []\n  action_items: []\n- id: R4-N1\n  summary: \"C1 是 causal mask 必然结果 + probe trivially easy\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 14\n  resolution: \"Abstract 'confirms expected' + 'consistent with causal attention mask' + 'framework sanity check' 三重降格。Contribution (iii) 定位为 methodology validation。全文一致。\"\n  resolution_round: 13\n  mentions:\n    - round: 9\n      reviewers: [1, 2]\n      note: \"R9-W2: C1 在 Abstract/Introduction 占比失衡。\"\n    - round: 10\n      reviewers: [1, 2]\n      note: \"RESOLVED。降格处理到位。\"\n    - round: 12\n      reviewers: [2, 3]\n      note: \"复发。R2-N1: 虽已降为 sanity check，但 Title 和 Abstract 仍将架构约束呈现为核心贡献。\"\n    - round: 13\n      reviewers: [1, 2]\n      note: \"RESOLVED。三重降格处理精准。\"\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R2 初审重提 Finding 3 trivial（N3 critical），但 R1 REBUT 区分三层：(a) image_mean at-chance 确实 trivial；(b) readout 三条件梯度非 trivial；(c) training asymmetry 非 causal mask 可预测。R2 接受反驳，降为 should-fix。共识：image_mean 部分是 sanity check，但 readout 梯度和 training asymmetry 是实质发现，Abstract 措辞需更精准区分。\"\n  action_items:\n    - round: 14\n      action: \"Abstract 'confirms expected functional specialization' 措辞应区分 trivial (image_mean) 和 non-trivial (readout gradient, training asymmetry) 部分\"\n      assigned_to: research_director\n      status: pending\n- id: R4-N2\n  summary: \"RSA inverted-U metric-dependent，CKA 反转\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 14\n  resolution: \"C3 降为 qualified observation + §4.4 CKA 正文讨论。\"\n  resolution_round: 8\n  mentions:\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R1-W3 再次提出 RSA vs CKA 反转处理不足。R2 部分 REBUT（Appendix A.1 有更多讨论），但同意核心关切成立。\"\n  action_items: []\n- id: R4-N3\n  summary: \"L1 ablation 使用 5 demos\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 5\n  resolution: \"改用 50 demos (N=63,228)。\"\n  resolution_round: 5\n  mentions: []\n  action_items: []\n- id: R4-W1\n  summary: \"RSA best-vs-best n.s. 未标注\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 5\n  resolution: \"已标注。\"\n  resolution_round: 5\n  mentions: []\n  action_items: []\n- id: R4-W2\n  summary: \"缺乏多重比较校正\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 5\n  resolution: \"FDR 已应用。\"\n  resolution_round: 5\n  mentions: []\n  action_items: []\n- id: R4-W3\n  summary: \"Probe N 未报告，MLP capacity 控制不充分\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 7\n  resolution: \"Demo-level split 完全消除时间泄漏。\"\n  resolution_round: 7\n  mentions: []\n  action_items: []\n- id: R4-W4\n  summary: \"Frozen encoder confound\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 5\n  resolution: \"Introduction + Discussion 说明。\"\n  resolution_round: 5\n  mentions: []\n  action_items: []\n- id: R9-N1\n  summary: \"单一模型(OpenVLA-7B)单一基准(LIBERO)，无法支撑 VLA 通用性\"\n  category: experiment\n  severity: critical\n  status: wont_fix\n  first_raised_round: 9\n  last_seen_round: 14\n  mentions:\n    - round: 9\n      reviewers: [1, 2]\n      note: \"双方 AGREE critical。\"\n    - round: 14\n      reviewers: [1, 2, 3]\n      note: \"R14 fresh review 再次提出。R1-W4 + R2-W4: LIBERO-only 的 tabletop manipulation 可能是多个发现的充分条件。三位 Reviewer 均 AGREE。\"\n  action_items:\n    - round: 10\n      action: \"Rebuttal 应对：causal mask 泛化 + testable predictions\"\n      assigned_to: research_director\n      status: pending\n  resolution: \"Claims 已限定为 'causal-decoder VLAs'。实验数据仍为 2 个架构，结构性局限不变。\"\n  resolution_round: null\n- id: R9-N2\n  summary: \"所有分析均为 open-loop，无 closed-loop 机器人评估\"\n  category: experiment\n  severity: critical\n  status: wont_fix\n  first_raised_round: 9\n  last_seen_round: 14\n  mentions:\n    - round: 9\n      reviewers: [1, 2]\n      note: \"双方 AGREE critical。\"\n    - round: 13\n      reviewers: [1, 2]\n      note: \"PARTIALLY_RESOLVED。'orthogonal contribution' 措辞仍需修改。\"\n    - round: 14\n      reviewers: [1, 2, 3]\n      note: \"R14 fresh review 以最高优先级再次提出。三位 Reviewer 均 AGREE。R3 补充：ablation 后 MSE≈0 反而让人困惑——routing 的功能意义需要 closed-loop 验证。\"\n  action_items:\n    - round: 14\n      action: \"验证至少一个 actionable implication（建议：在已有 LIBERO rollout 数据上计算 L1 attention entropy 与 task failure 的相关性）\"\n      assigned_to: research_director\n      status: pending\n  resolution: \"Open-loop 结构性局限不变。R14 建议了低成本验证方案。\"\n  resolution_round: null\n- id: R9-N3\n  summary: \"'Causal' 术语在 observational open-loop 分析中使用不当\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 10\n  resolution: \"Discussion 'Causal' → 'Interventional'；§4.3 heading 改为 'Open-loop functional sensitivity'。\"\n  resolution_round: 10\n  mentions: []\n  action_items: []\n- id: R9-N4\n  summary: \"Ablation 使 R² 增加的 paradox 未充分解释\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 11\n  resolution: \"Discussion 加 information-computation dissociation 解释。\"\n  resolution_round: 11\n  mentions: []\n  action_items: []\n- id: R9-N5\n  summary: \"Counterfactual 的 'semantic distance' 概念未定义\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 10\n  resolution: \"改用 Jaccard token overlap / token novelty。\"\n  resolution_round: 10\n  mentions: []\n  action_items: []\n- id: R9-N6\n  summary: \"N=10 tasks 的 RSA bootstrap 统计功效不足\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 9\n  last_seen_round: 14\n  resolution: \"\"\n  resolution_round: null\n  mentions:\n    - round: 11\n      reviewers: [1]\n      note: \"RESOLVED（加了 power limitation 声明）。\"\n    - round: 14\n      reviewers: [1, 2, 3]\n      note: \"R14 fresh review 升级为 critical。三位 AGREE。新角度：TOST 等价性检验；R3 补充 Mann-Whitney U p=0.033 在 N=6 vs N=4 下解释力有限。\"\n  action_items:\n    - round: 14\n      action: \"提供 power analysis；对跨架构 convergence 考虑 TOST 等价性检验\"\n      assigned_to: research_director\n      status: pending\n- id: R9-W1\n  summary: \"CoRL scope fit 有限：纯 representational analysis，无物理机器人实验\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 9\n  last_seen_round: 14\n  resolution: \"\"\n  resolution_round: null\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"PARTIALLY_RESOLVED。Writing-level 改善但核心缺陷无法通过写作修复。\"\n    - round: 14\n      reviewers: [1, 2, 3]\n      note: \"三位 Reviewer 均以最高优先级提出。R3 强烈 AGREE：更适合 ICML/NeurIPS interpretability track。\"\n  action_items:\n    - round: 14\n      action: \"最低方案：验证一个 implication；最佳方案：补充 closed-loop 评估；备选：改投 ML venue\"\n      assigned_to: research_director\n      status: pending\n- id: R9-W2\n  summary: \"C1 在 Abstract/Introduction/Contributions 中占比失衡\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 10\n  resolution: \"C1 降为末句 sanity check。\"\n  resolution_round: 10\n  mentions: []\n  action_items: []\n- id: R9-W3\n  summary: \"Vision representation 训练效果微弱，framing 未充分反映\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 10\n  resolution: \"§4.4 标题改为 'Training primarily enhances readout decodability'。\"\n  resolution_round: 10\n  mentions: []\n  action_items: []\n- id: R9-W4\n  summary: \"Cohen's d 独立性假设违反\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 9\n  last_seen_round: 14\n  resolution: \"\"\n  resolution_round: null\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"RESOLVED（新增 trajectory-level d）。\"\n    - round: 14\n      reviewers: [1, 2, 3]\n      note: \"R1 重提 paired data 应用 paired effect size。R2 REBUT 偏差方向（paired d_z > standard d）。R3 AGREE token-level 有强时序相关性。共识：应报告 paired d_z 和配对相关系数 r。\"\n  action_items:\n    - round: 14\n      action: \"报告 paired Cohen's d_z 和配对相关系数 r；在 Method 中讨论 paired vs independent d\"\n      assigned_to: research_director\n      status: pending\n- id: R9-W5\n  summary: \"Pretrained Llama-2 base 的 9/32 heads 可能因 text in-distribution bias\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 10\n  resolution: \"Discussion 新增替代解释承认。\"\n  resolution_round: 10\n  mentions: []\n  action_items: []\n- id: R9-W6\n  summary: \"Specificity control 效果有限(d ratio 1.08×)\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 14\n  resolution: \"四组 matched-size 比较，framing 'distributed routing'。\"\n  resolution_round: 11\n  mentions:\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R1-W2 再次提出 ablation 因果推断过度表述。R2 AGREE but 不升级 severity。\"\n  action_items: []\n- id: R9-W7\n  summary: \"N=63,228 观测的独立性——有效独立单元远小于报告值\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 12\n  resolution: \"§4.1 新增 N_eff 说明。\"\n  resolution_round: 10\n  mentions: []\n  action_items: []\n- id: R9-I1\n  summary: \"缺失引用：Octo (Ghosh et al. 2024)\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 10\n  resolution: \"references.bib 新增。\"\n  resolution_round: 10\n  mentions: []\n  action_items: []\n- id: R9-I2\n  summary: \"Häon et al. 2025 的 sparse semantic directions 与 L1 routing heads 的关系未讨论\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 11\n  resolution: \"Discussion 加 where/what 互补连接。\"\n  resolution_round: 11\n  mentions: []\n  action_items: []\n- id: R9-I3\n  summary: \"多处小问题：Table 1 caption、脚注、accessed date\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 10\n  resolution: \"已修复。\"\n  resolution_round: 10\n  mentions: []\n  action_items: []\n- id: R10-Q1\n  summary: \"Per-task MSE breakdown：消融后 MSE 不变是否存在 task-level cancellation\"\n  category: experiment\n  severity: info\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 11\n  resolution: \"Appendix 加 per-task breakdown。\"\n  resolution_round: 11\n  mentions: []\n  action_items: []\n- id: R12-N1\n  summary: \"因果 overclaiming：Title 'Routes' 暗示因果机制\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 13\n  resolution: \"Title 'Routes'→'Reorganizes'，全文 'routing'→'redistributes'，零残留。\"\n  resolution_round: 13\n  mentions: []\n  action_items: []\n- id: R12-N2\n  summary: \"正文超出 CoRL 8 页限制\"\n  category: format\n  severity: critical\n  status: open\n  first_raised_round: 12\n  last_seen_round: 14\n  resolution: \"\"\n  resolution_round: null\n  mentions:\n    - round: 14\n      reviewers: [3]\n      note: \"R3-N1 critical: 正文约 8.7 页，超出 8 页限制约 0.7 页。Discussion + Conclusion 延伸到第 9 页。R13 声称已修复但 R14 fresh review 发现回归。\"\n  action_items:\n    - round: 14\n      action: \"将 Discussion Mechanistic interpretation 和 Functional stages 移至 Appendix，压缩 Introduction 重复内容\"\n      assigned_to: research_director\n      status: pending\n- id: R12-N3\n  summary: \"Abstract/Introduction 信息过载\"\n  category: writing\n  severity: critical\n  status: open\n  first_raised_round: 12\n  last_seen_round: 14\n  resolution: \"\"\n  resolution_round: null\n  mentions:\n    - round: 14\n      reviewers: [3]\n      note: \"R3-N2 critical: Abstract 仍含 15+ 定量结果，Introduction 与 Abstract 80% 重复。R13 声称已修复但 R14 fresh review 发现回归。\"\n  action_items:\n    - round: 14\n      action: \"Abstract 只保留 3 个核心发现的定性描述 + 1-2 个关键数字；Introduction 聚焦 motivation\"\n      assigned_to: research_director\n      status: pending\n- id: R12-W1\n  summary: \"无首页 teaser figure\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 12\n  last_seen_round: 14\n  resolution: \"\"\n  resolution_round: null\n  mentions:\n    - round: 14\n      reviewers: [3]\n      note: \"R3-W1: Figure 1 出现在 PDF page 6 而非 page 1。R13 声称新增 Figure 1 但 R14 发现仍不在首页。\"\n  action_items: []\n- id: R12-W2\n  summary: \"层编号 off-by-one\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 12\n  last_seen_round: 14\n  resolution: \"\"\n  resolution_round: null\n  mentions:\n    - round: 14\n      reviewers: [3]\n      note: \"R3-W2: method.tex L26 'L1--L31 the 32 transformer layers' 仍有 off-by-one 错误。R13 声称已修复但 R14 发现回归。\"\n  action_items: []\n- id: R12-W3\n  summary: \"多条引用使用 arXiv preprint 而非已发表版本\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 12\n  last_seen_round: 14\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"3/3 已更新。仍有 belrose2023, padalkar2023 待更新。\"\n    - round: 14\n      reviewers: [2, 3]\n      note: \"R2-M1 + R3-W3 独立发现。R3 列出 6 条具体引用需更新（kim2024_openvla, karamcheti2024, touvron2023, belrose2023, padalkar2023, black2024_pi0）。\"\n  action_items:\n    - round: 14\n      action: \"检查并更新所有可更新的 arXiv 引用至正式版本\"\n      assigned_to: research_director\n      status: pending\n  resolution: \"\"\n  resolution_round: null\n- id: R12-W4\n  summary: \"缺失重要 related work\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 13\n  resolution: \"6/6 缺失引用全部补齐。\"\n  resolution_round: 13\n  mentions: []\n  action_items: []\n- id: R12-W5\n  summary: \"与 Grant et al. 和 Häon et al. 的区分不够清晰\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 14\n  resolution: \"Related Work 加显式 what-vs-where 对比段落。\"\n  resolution_round: 13\n  mentions:\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R2-W1 再次提出增量贡献不清晰。R1 AGREE with nuance。\"\n  action_items: []\n- id: R12-W6\n  summary: \"FDR 多重比较校正细节不足\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 14\n  resolution: \"BH 方法 + α=0.05 + 33-layer family per metric 完整报告。\"\n  resolution_round: 13\n  mentions:\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R1-W1 提出更深层关切：FDR 仅在每个 metric 的 33 层内，未对全局 family-wise error rate 校正。\"\n  action_items:\n    - round: 14\n      action: \"考虑在 Appendix 添加全局 Bonferroni-adjusted p-values 作为 robustness check\"\n      assigned_to: research_director\n      status: pending\n- id: R12-I1\n  summary: \"术语不一致：readout token vs last_preaction\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 12\n  last_seen_round: 14\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"PARTIALLY_RESOLVED。Table 1 的 'last_preaction' 建议 caption 加映射说明。\"\n    - round: 14\n      reviewers: [1, 2, 3]\n      note: \"三位 Reviewer 均独立发现。R3-W5 列出全部混用实例。\"\n  action_items:\n    - round: 14\n      action: \"统一为 'readout token'，首次出现时定义；Table caption 加映射说明\"\n      assigned_to: research_director\n      status: pending\n  resolution: \"\"\n  resolution_round: null\n- id: R12-I2\n  summary: \"Limitations 未作为独立 section\"\n  category: format\n  severity: info\n  status: in_progress\n  first_raised_round: 12\n  last_seen_round: 14\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"PARTIALLY_RESOLVED。使用 paragraph 而非 subsection。\"\n    - round: 14\n      reviewers: [3]\n      note: \"R3-W4: Limitations 仍是 Discussion 的 paragraph 而非独立 section，不满足 CoRL 2026 要求。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n- id: R12-DIV1\n  summary: \"Title 'Language Routes' 是否误导\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 13\n  resolution: \"Title 'Routes'→'Reorganizes' 消除误导。\"\n  resolution_round: 13\n  mentions: []\n  action_items: []\n- id: R13-W1\n  summary: \"'Orthogonal contribution' 措辞对 closed-loop validation 过于 dismissive\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 13\n  last_seen_round: 14\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"建议改为 'complementary and necessary next step'。\"\n    - round: 14\n      reviewers: []\n      note: \"本轮未直接提及但被更广泛的 scope fit 讨论涵盖。Discussion 仍含 'orthogonal contribution' 原文。\"\n  action_items:\n    - round: 13\n      action: \"'orthogonal contribution' 改为 'complementary and necessary next step'\"\n      assigned_to: research_director\n      status: pending\n  resolution: \"\"\n  resolution_round: null\n- id: R13-I1\n  summary: \"附录 'robust attractor' 措辞较主文更强\"\n  category: framing\n  severity: info\n  status: open\n  first_raised_round: 13\n  last_seen_round: 13\n  mentions:\n    - round: 14\n      reviewers: []\n      note: \"本轮未直接提及但被 convergent claim 弱化建议涵盖。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n- id: R13-I2\n  summary: \"Spacing 压缩激进\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 13\n  last_seen_round: 13\n  mentions:\n    - round: 14\n      reviewers: []\n      note: \"本轮未提及。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n- id: R14-N1\n  summary: \"'Convergent reorganization' claim 从 N=2 同类架构得出，证据不足\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 14\n  last_seen_round: 14\n  mentions:\n    - round: 14\n      reviewers: [1, 2, 3]\n      note: \"三位 Reviewer 均 AGREE。Δ=0.003 可能反映架构共性而非训练通用规律。建议弱化为 'preliminary evidence'。\"\n  action_items:\n    - round: 14\n      action: \"将 'convergent reorganization' 弱化为 'shared tendency' 或 'preliminary evidence for convergence'\"\n      assigned_to: research_director\n      status: pending\n  resolution: \"\"\n  resolution_round: null\n- id: R14-W1\n  summary: \"Counterfactual instruction analysis 仅用 3/10 tasks，ρ=1.0 在 n=4 条件下仅 marginal\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 14\n  last_seen_round: 14\n  mentions:\n    - round: 14\n      reviewers: [1, 2]\n      note: \"3 tasks 选择 rationale 未报告，cross-task variance 未讨论。\"\n  action_items:\n    - round: 14\n      action: \"在全部 10 tasks 上复现 counterfactual 分析，或报告选择 rationale 和 cross-task variance\"\n      assigned_to: research_director\n      status: pending\n  resolution: \"\"\n  resolution_round: null\n- id: R14-W2\n  summary: \"单一训练 checkpoint 分析——不同 training seed 可能产生不同表征结构\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 14\n  last_seen_round: 14\n  mentions:\n    - round: 14\n      reviewers: [1, 2]\n      note: \"建议 Limitations 中讨论 training stochasticity 的潜在影响。\"\n  action_items:\n    - round: 14\n      action: \"Limitations 中讨论 training seed variance\"\n      assigned_to: research_director\n      status: pending\n  resolution: \"\"\n  resolution_round: null\n- id: R14-W3\n  summary: \"缺失引用：Aghajanyan et al. (ACL 2021) + Kumar et al. (NeurIPS 2022)\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 14\n  last_seen_round: 14\n  mentions:\n    - round: 14\n      reviewers: [1, 2]\n      note: \"两篇与本文核心问题直接相关的 fine-tuning representation 工作未引用。\"\n  action_items:\n    - round: 14\n      action: \"引用 Aghajanyan et al. (ACL 2021) 和 Kumar et al. (NeurIPS 2022)\"\n      assigned_to: research_director\n      status: pending\n  resolution: \"\"\n  resolution_round: null\n- id: R14-I1\n  summary: \"Footnote 1 两个 pipeline R² 值差异未解释\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 14\n  last_seen_round: 14\n  mentions:\n    - round: 14\n      reviewers: [1]\n      note: \"R1-Minor-2。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n- id: R14-I2\n  summary: \"Leave-one-out p ≤ 0.083 不应表述为 'robust'\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 14\n  last_seen_round: 14\n  mentions:\n    - round: 14\n      reviewers: [1, 2]\n      note: \"p=0.083 按任何常规标准不能称为 robust。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n- id: R14-I3\n  summary: \"Permutation test 仅 1,000 shuffles（建议 ≥10,000）\"\n  category: method\n  severity: info\n  status: open\n  first_raised_round: 14\n  last_seen_round: 14\n  mentions:\n    - round: 14\n      reviewers: [1, 2]\n      note: \"效应极大所以不影响结论，但统计实践建议增加。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n- id: R14-W4\n  summary: \"GenAI disclosure 排版位置异常（References 后、Appendix 前）\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 14\n  last_seen_round: 14\n  mentions:\n    - round: 14\n      reviewers: [3]\n      note: \"R3-S6: 建议移至论文末尾或 appendix 合适位置。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n- id: R14-W5\n  summary: \"Appendix resizebox 可能压缩字体至不可读\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 14\n  last_seen_round: 14\n  mentions:\n    - round: 14\n      reviewers: [3]\n      note: \"R3-S4: appendix.tex Table 17 的 resizebox 导致字体过小。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n- id: R14-W6\n  summary: \"setlength float spacing 修改可能与 corl_2026 package 冲突\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 14\n  last_seen_round: 14\n  mentions:\n    - round: 14\n      reviewers: [3]\n      note: \"R3-S5: main.tex lines 16-20 的 setlength 调整需确认是否被允许。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n- id: R14-W7\n  summary: \"Table 2 caption 缩写 'immed./gradual/incid.' 未解释\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 14\n  last_seen_round: 14\n  mentions:\n    - round: 14\n      reviewers: [3]\n      note: \"R3-S2: caption 中缩写未给出全称，不 standalone readable。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n- id: R14-DIV1\n  summary: \"MLP probe capacity：R1 认为过大，R3 认为已充分回应\"\n  category: method\n  severity: info\n  status: open\n  first_raised_round: 14\n  last_seen_round: 14\n  mentions:\n    - round: 14\n      reviewers: [1, 3]\n      note: \"R1-W5 认为 1.05M 参数过大。R3 REBUT：Appendix A.6 linear probe 完整复现 inverted-U pattern，capacity concern 已 ruled out。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null"
  }
}
```

</details>

---


### Tool result

_source line 1180 · 2026-05-20T17:00:48.490281+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/review_issues.yaml\", \"bytes\": 23878}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 153
}
```

</details>

---


### Tool call

_source line 1181 · 2026-05-20T17:03:27.020653+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "report": "# Consolidated Review Report — Round 14 (Fresh)\n\n**Paper**: \"Vision Encodes, Language Reorganizes: Token-Level Representational Analysis of VLA Fine-Tuning\"\n**Target Venue**: CoRL 2026 (deadline 2026-05-29)\n**Reviewers**: R1 (方法/实验严谨性), R2 (新颖性/scope/完整性), R3 (写作质量/格式合规/可复现性)\n**Review Date**: 2026-05-20\n\n---\n\n## Summary\n\n本文对 VLA（Vision-Language-Action）模型的微调过程进行逐层、逐 token 类型的表征分析。以 OpenVLA-7B 为主要分析对象，辅以 TraceVLA 做跨架构对比，提出三个发现：(1) 微调将指令注意力重新分配至 entry-exit 层，L1 为主要 hub；(2) 两个不同架构的 VLA 在训练后达到相似的中层表征（Δ=0.003）；(3) image token 与 readout token 存在功能分化——image token 对指令不敏感，readout token 是多模态整合中心。论文包含 7 项互补分析（interventional、supporting、constraining）和 21 页附录。\n\n---\n\n## Strengths\n\n**S1. 系统性的多层次分析框架** [R1, R2, R3 共识] — 从注意力头统计、RSA、CKA、线性探针、消融、反事实、剂量-反应等 7 个互补视角对 VLA 微调进行分析，形成 interventional → supporting → constraining 的证据层次。这种三角验证的方法论在 VLA 机制分析中尚属首次，且方法论本身可迁移至其他 VLA 研究。\n\n**S2. Readout token 发现具有实用价值** [R1, R2] — 发现 readout token 是多模态整合的主要位点（R²=0.678 vs image_mean 的 chance-level），而 image token 对指令不敏感。这一发现对 VLA 架构设计（如 early-exit 推理、微调诊断）有直接指导意义。\n\n**S3. 训练-未训练因子设计** [R1, R3] — 对训练/未训练模型进行成对比较，使用因子控制隔离微调效应，而非仅报告训练后状态。这使得因果推断更可信。\n\n**S4. 附录极为详尽** [R1, R2, R3] — 21 页附录覆盖鲁棒性检验（距离度量、per-DOF、permutation、seed、demo subsample）、OOD 诊断、跨 benchmark (LIBERO-Spatial) 验证等。R3 特别指出可复现性做得好（checkpoint、dataset、seed、compute 均报告）。\n\n**S5. 剂量-反应分析** [R1, R3] — 4→32 头渐进消融呈现单调递增而非阈值效应（d=0.48→0.64），为 L1 注意力头的功能重要性提供了介入性证据。R3 进一步指出 counterfactual instruction analysis 中 shuffled condition (d=0.625) 对 positional sensitivity 的确认也有信息量。\n\n**S6. 实验设计严谨** [R3: Soundness 7/10] — factorial controls、7 种互补分析、cross-architecture 验证、demo-level split 消除时间泄漏、linear probe sensitivity analysis 等方法论质量高。\n\n---\n\n## Weaknesses\n\n### Must-Fix（不修复则建议拒稿）\n\n**W-MF1. CoRL scope 适配性不足** [R1, R2, R3 三方共识——本轮最高优先级问题]\n论文是纯分析/解释性工作，无机器人实验、无闭环验证、无策略改进。CoRL 2026 CFP 明确要求 \"demonstrate the relevance of proposed models, algorithms, datasets, and benchmarks to robotics\" 并警告 \"papers lacking robotics emphasis will be desk-rejected\"。论文的 actionable insight（如 early-exit 推理、L1 entropy 监控）仅作为假设提出，未做任何验证。Discussion 中 \"orthogonal contribution and a natural next step\" 的措辞显得对闭环验证过于轻描淡写。R3 补充了一个尖锐观察：ablation 后 MSE 几乎不变（0.498→0.497），这反而质疑了 routing 的功能意义——闭环 success rate 测量将直接回答这个问题。\n**建议**：要么补充至少一个 downstream 应用实验（如 L1 attention entropy 与 task failure 的相关性——在现有 rollout 数据上即可计算，成本低），要么将 venue 转向 ICML/NeurIPS 的 interpretability track。\n\n**W-MF2. \"Convergent reorganization\" 声称过强** [R1, R2, R3 三方共识]\n仅两个模型（OpenVLA, TraceVLA）的 Δ=0.003 不能支撑 \"convergent\" 这一暗示普遍性的术语。两个架构共享 causal decoder + ~32 layers + LIBERO + tokenized actions，本质上是同一架构家族内的比较。Exit-layer R² 差异 0.069 与 mid-layer Δ=0.003 形成矛盾，论文仅以 post-hoc speculation 解释（\"possibly reflecting architectural differences\"）。N=2 的跨架构比较本质上是 case study，无法排除巧合。\n**建议**：将 \"convergent\" 降级为 \"consistent\" 或 \"preliminary evidence\"；精确界定收敛范围（仅 mid-layer，exit-layer 分歧）。\n\n**W-MF3. 统计效力不足（N_eff=10）** [R1, R2, R3 三方共识]\nBootstrap 基于 10 个 task 的聚合，N_eff=10 严重限制了统计推断的可靠性。LIBERO-Goal Δ=+0.017 n.s. vs LIBERO-Spatial Δ=+0.023 p<0.001——差异仅 0.006 但显著性截然不同，说明 power 不足。R3 补充：Table 11 的 Mann-Whitney U 检验在 N=6 vs N=4 上得到 p=0.033，在如此小 N 下解释力有限。\n**建议**：提供 power analysis（N=10 可检测的最小效应量）；对跨架构 convergence 使用 TOST 等价性检验。\n\n**W-MF4. 正文超出 8 页限制** [R3 独立发现——desk rejection 风险]\n正文约 8.7 页，超出 CoRL 2026 的 8 页限制约 0.7 页。Discussion 的 Synthesis、Mechanistic interpretation、Functional stages、Limitations 四个段落 + Conclusion 延伸到第 9 页。这是 desk rejection 的常见理由。**注意**：此问题在 Round 12-13 曾被修复，但 R14 fresh review 发现回归。\n**建议**：将 Discussion 中 Mechanistic interpretation 和 Functional stages 的预测性内容移至 Appendix；压缩 Introduction 中与 Abstract 重复的量化描述。\n\n**W-MF5. Abstract/Introduction 信息过载** [R3 独立发现]\nAbstract 在 ~200 words 内塞入了至少 15 个定量结果（d=0.48→0.64、p=0.033、R²+0.069、2.5× 等），远超同领域论文的 abstract 信息密度。Introduction 几乎逐字重复 abstract 的所有量化结论。R3 评 Clarity 仅 4/10。**注意**：同 W-MF4，此问题也是回归。\n**建议**：Abstract 只保留 3 个核心发现的定性描述 + 1-2 个关键数字；Introduction 聚焦 motivation。\n\n### Should-Fix（不影响接收决定，但显著提升论文质量）\n\n**W-SF1. Cohen's d 计算方法需澄清** [R1 提出, R2 部分反驳, R3 同意——唯一未完全解决的技术分歧]\nR1 认为对配对数据使用标准 Cohen's d 可能高估效应量。R2 反驳指出 paired d_z = mean_diff / SD_diff > standard d（因 SD_diff < SD_pooled when r>0），当前报告反而保守。R3 从不同角度支持 R1——token-level observations 有强时序相关性。**技术分歧**：偏差方向在数学上 R2 更准确，但三方共识是应明确报告使用的公式和配对版本数值。\n**建议**：报告 paired d_z 和配对相关系数 r；在 Method 中讨论选择。\n\n**W-SF2. 仅 LIBERO 基准** [R1, R2, R3 共识]\n所有实验基于 LIBERO 家族（Goal + Spatial），instruction diversity 有限——10 个 tasks 的差异主要在 object 和 target location。缺少更复杂 benchmark（如 CALVIN、Language-Table）的验证。\n**建议**：至少在 Discussion 中讨论 LIBERO 特异性风险。\n\n**W-SF3. 缺少关键参考文献** [R1, R2, R3 共识]\n(a) Aghajanyan et al. (ACL 2021, intrinsic dimensionality of fine-tuning) 和 Kumar et al. (NeurIPS 2022, fine-tuning distorts pretrained features) 与核心问题直接相关但未引用 [R1, R2]\n(b) VLA efficiency/pruning 工作（如 TinyVLA, ECoT）未覆盖 [R1, R2]\n(c) 多条引用仍使用 arXiv preprint 而非已发表版本——R3 列出 6 条具体条目（kim2024_openvla, karamcheti2024, touvron2023, belrose2023, padalkar2023, black2024_pi0）[R3]\n\n**W-SF4. 单 checkpoint 分析** [R2 提出, R1 同意]\n仅分析最终 checkpoint，缺少训练动态。至少在几个中间 checkpoint 上报告 L1 head count 或 readout R² 的演化趋势。\n\n**W-SF5. Finding 3 定位需强化** [R2→R1 反驳→R2 接受→R3 给出 nuanced 评价]\nR2 初认为 Finding 3（image token instruction-blindness）near trivial——causal mask 的必然结果。R1 反驳区分三层：(a) image_mean at-chance 确实是 expected；(b) readout 从 L1 即 100% 是 non-trivial gradient；(c) training 不改变 image blindness 但大幅提升 readout 是 non-trivial asymmetry。R2 接受。R3 提供了关键 nuance：如果 image tokens 在 instruction tokens 之前（vision-first ordering），则 instruction-blindness 是 causal mask 的必然；但论文未明确声明 token ordering。无论如何，readout gradient 和 training asymmetry 是实质发现。\n**建议**：正文明确声明 token ordering；Abstract 区分 expected（image_mean）vs surprising（readout gradient）部分。\n\n**W-SF6. Figure 1 不在首页** [R3 独立发现——回归问题]\nFigure 1 出现在 PDF page 6，前 5 页全是密集文字。Round 13 曾声称修复但 R14 发现回归。\n\n**W-SF7. Limitations 格式不满足 CoRL 要求** [R3 独立发现]\nLimitations 仍是 Discussion 的 `\\paragraph`，而非独立 section。CoRL 2026 要求 \"All submissions should include a Limitations section\"。\n\n**W-SF8. 层编号 off-by-one** [R3 独立发现——回归问题]\nmethod.tex: \"L1--L31 the 32 transformer layers\"——L1 到 L31 inclusive 只有 31 个索引，与 \"32 transformer layers\" 矛盾。Round 13 曾声称修复但 R14 发现回归。\n\n**W-SF9. 术语不一致** [R1, R2, R3 三方独立发现]\nreadout token / last_preaction；instruction-dominant heads / dominant heads / instruction heads；7-D action vectors / 7-D actions——多组术语混用。\n\n---\n\n## Reviewer Consensus（三方共识）\n\n1. **CoRL scope 是首要问题** — 三位审稿人均认为纯分析性论文缺乏 robotics 应用验证是最大短板。R3 尤其尖锐：ablation 不改变 MSE 质疑了 routing 的功能意义。\n2. **\"Convergent\" 声称过强** — N=2 同质架构 + N_eff=10 的统计基础不足以支撑此术语\n3. **方法论框架本身有价值** — 三角验证方法论和 readout token 发现是实质贡献\n4. **附录质量高** — 鲁棒性检验详尽，可复现性好\n5. **需补充参考文献** — VLA efficiency 和 fine-tuning representation 领域引用缺失；多条 arXiv 引用需更新\n6. **闭环验证缺失** — 三方一致认为至少应验证一个 actionable implication\n\n## Reviewer Divergence（分歧点）\n\n| 议题 | R1 | R2 | R3 | 解决状态 |\n|------|----|----|----|----|\n| Finding 3 trivial? | Non-trivial（三层区分） | 初 trivial → 接受 R1 | Nuanced（需声明 token ordering） | ✅ 基本解决 |\n| Cohen's d 偏差方向 | 可能高估 | paired d_z > standard d（保守） | Token 相关性高估 | ⚠️ 方向未解决，但共识报告配对版 |\n| Title \"Reorganizes\" | 可接受 | 初质疑 → 撤回 | 辩护\"Language Routes\"有数据支持 | ✅ 已解决 |\n| MLP probe capacity | 过大（1.05M params） | 未强调 | 已充分回应（Appendix A.6 linear probe） | ✅ R3 有力反驳 |\n\n---\n\n## Questions for Authors\n\n1. L1 的 24/32 instruction-dominant heads 中，是否有 head 在 pretrained Llama-2 中已存在 instruction sensitivity？Fine-tuning 是 amplifying 还是 creating？\n2. Δ=0.003 的 TOST 等价性检验（ε=0.05）的 p 值是多少？如果不显著，\"convergent\" 声称如何辩护？\n3. 是否考虑过在训练中间 checkpoint 上测量 L1 head count 的演化曲线？\n4. Readout token 的 R²=0.678——剩余 32.2% 的方差来源是什么？\n5. Ablation 后 MSE 几乎不变（0.498→0.497），但 trajectory divergence d>0.6。如何 reconcile？是否意味着 routing 影响 trajectory shape 但不影响 per-step error？\n6. OpenVLA 的 token ordering 是什么？Image tokens 在 instruction tokens 之前还是之后？这直接影响 Finding 3 的 triviality 判断。[R3 提出]\n\n---\n\n## Missing References\n\n**高优先级**（与核心问题直接相关）：\n- Aghajanyan et al. (ACL 2021) — Intrinsic Dimensionality Explains the Effectiveness of Language Model Fine-Tuning\n- Kumar et al. (NeurIPS 2022) — Fine-Tuning Can Distort Pretrained Features and Underperform Out-of-Distribution\n- \"What Do Visual Tokens Really Encode?\" (arXiv:2603.00510) — 直接研究 VLM visual token 编码\n\n**中优先级**：\n- TinyVLA / ECoT 或其他 VLA compression/efficiency 工作\n- Diffusion/flow-matching VLA 表征分析\n- VLA scaling laws 相关工作\n\n**引用版本更新需求**（6 条 arXiv→published）：\nkim2024_openvla, karamcheti2024, touvron2023_llama2, belrose2023_tunedlens, padalkar2023_oxe, black2024_pi0\n\n---\n\n## External Review\n\n**外部审稿（Stanford Agentic Reviewer）：pending，未返回。**\n\n---\n\n## Visual Layout Check（非评分项）\n\n由独立视觉审查 Agent 完成，结果如下：\n\n- **Critical (1)**：Page 31（附录末页）约 90% 空白，严重浪费版面\n- **Warnings (4)**：\n  - Pages 2-4：连续 3 页无图表，纯文字密度过高\n  - Page 16：图表标签字号过小，可能不满足打印可读性\n  - Page 21：表格过于密集，建议拆分或调整间距\n  - Page 30：同上，表格密度过高\n- **Info (21)**：其余为次要排版观察\n\nR3 的独立审查与视觉 Agent 发现一致：pages 2-4 无图（R3-W1: Figure 1 在 page 6）、表格密度高（R3-S4: resizebox 压缩字体）。\n\n---\n\n## Overall Assessment\n\n**Overall Score: 5.0/10 → Weak Reject**\n\n| Reviewer | 侧重 | 初始分 | 最终分 | 变化原因 |\n|----------|------|--------|--------|----------|\n| R1 | 方法/实验严谨性 | 6/10 | 6/10 | 无变化 |\n| R2 | 新颖性/scope/完整性 | 4/10 | 5/10 | 接受 R1 对 Finding 3 和 effect size 的反驳 |\n| R3 | 写作/格式/可复现性 | 5/10 | 5/10 | 无变化 |\n\n**R3 官方维度打分**：Significance & Novelty 6/10, Relevance to Robotics 5/10, Soundness 7/10, Clarity 4/10, Reproducibility 7/10\n\n**核心判断**：论文的方法论框架（三角验证 + 因子设计）和 readout token 发现是实质贡献，但五个结构性问题使其不适合当前形式投稿 CoRL：\n1. **CoRL scope**：纯分析无闭环验证，与 CoRL robotics 受众不匹配\n2. **Convergent claim**：N=2 同质架构 + N_eff=10 统计基础不足\n3. **超页限**：正文 8.7 页，超出 8 页限制——desk rejection 风险\n4. **可读性**：Abstract 信息过载 (R3 Clarity 4/10)，前 5 页无图表\n5. **LIBERO 单一 benchmark**：instruction diversity 有限\n\n**特别警告**：R12-N2（超页限）和 R12-N3（信息过载）在 Round 13 曾被标记为 resolved，但 Round 14 fresh review 发现这些问题回归。Research Director 需要验证这些修复确实生效。\n\n**建议路径**：\n- **若坚持 CoRL**（deadline 2026-05-29，仅剩 9 天）：\n  - 紧急：压缩正文至 8 页、精简 Abstract/Intro\n  - 高优先级：补充 L1 entropy 与 task failure 相关性分析（低成本）\n  - 中优先级：弱化 \"convergent\" 措辞、补充引用、修复层编号/术语\n- **若转投**：ICML/NeurIPS interpretability track 或 CoRL Workshop 可能是更自然的归属\n\n---\n\n## Detailed Comments\n\n### 正文修改建议\n\n1. **Abstract**: \"convergent reorganization\" → \"consistent reorganization pattern\"\n2. **Abstract**: 删除至少 10 个定量数字，只保留 Δ=0.003 和一个 probe 数字\n3. **Abstract**: \"confirms expected functional specialization\" → 区分 trivial (image_mean) vs non-trivial (readout gradient)\n4. **Title**: 当前 \"Reorganizes\" 可接受，但考虑加限定词 \"in Causal-Decoder VLAs\"\n5. **Introduction**: 删除与 Abstract 重复的量化描述，聚焦 gap statement\n6. **Method 层编号**: \"L1--L31 the 32 transformer layers\" → 统一为 \"L1--L32 the 32 transformer layers\" 或修正索引范围\n7. **Method**: 明确声明 token ordering（vision-first? instruction-first?）\n8. **Section 4.3 跨架构**: 加入 N=2 caveat 和 exit-layer 分歧讨论\n9. **Discussion \"orthogonal contribution\"**: → \"complementary and necessary next step\"\n10. **Discussion**: Mechanistic interpretation 和 Functional stages 移至 Appendix（回收 ~0.5 页）\n11. **Conclusion**: 当前 3 行过短，补充 broader impact 和 limitation summary\n12. **Limitations**: 提升为独立 `\\section{Limitations}` 满足 CoRL 要求\n13. **术语**: 全文统一 readout token / instruction-dominant heads / 7-D actions\n\n### 统计方法改进\n\n14. **Cohen's d**: 报告 paired d_z 和配对相关系数 r\n15. **TOST**: 对 Δ=0.003 做等价性检验\n16. **Power analysis**: 报告 N=10 可检测的最小效应量\n17. **Permutation test**: 增加到 ≥10,000 shuffles\n18. **FDR**: 考虑添加全局 Bonferroni-adjusted p-values\n\n### 引用和格式\n\n19. **新增引用**: Aghajanyan 2021, Kumar 2022, visual token encoding (2603.00510)\n20. **更新引用**: 6 条 arXiv → published version\n21. **Figure 1**: 确保出现在 page 1\n22. **GenAI disclosure**: 移至 Appendix 合适位置\n23. **Table 2 caption**: 展开缩写\n24. **Appendix resizebox**: 改用 \\small 或 \\footnotesize\n25. **Page 31 空白**: 合并或删除",
  "project": "vla-ssd",
  "reviewer_ids_acknowledged": "[1, 2, 3]",
  "cross_response_reviewer_ids": "[1, 2, 3]",
  "overall_score": "weak reject",
  "review_chat_id": "oc_554a5023cde4d603635cf97e6ab8151a"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "report": "# Consolidated Review Report — Round 14 (Fresh)\n\n**Paper**: \"Vision Encodes, Language Reorganizes: Token-Level Representational Analysis of VLA Fine-Tuning\"\n**Target Venue**: CoRL 2026 (deadline 2026-05-29)\n**Reviewers**: R1 (方法/实验严谨性), R2 (新颖性/scope/完整性), R3 (写作质量/格式合规/可复现性)\n**Review Date**: 2026-05-20\n\n---\n\n## Summary\n\n本文对 VLA（Vision-Language-Action）模型的微调过程进行逐层、逐 token 类型的表征分析。以 OpenVLA-7B 为主要分析对象，辅以 TraceVLA 做跨架构对比，提出三个发现：(1) 微调将指令注意力重新分配至 entry-exit 层，L1 为主要 hub；(2) 两个不同架构的 VLA 在训练后达到相似的中层表征（Δ=0.003）；(3) image token 与 readout token 存在功能分化——image token 对指令不敏感，readout token 是多模态整合中心。论文包含 7 项互补分析（interventional、supporting、constraining）和 21 页附录。\n\n---\n\n## Strengths\n\n**S1. 系统性的多层次分析框架** [R1, R2, R3 共识] — 从注意力头统计、RSA、CKA、线性探针、消融、反事实、剂量-反应等 7 个互补视角对 VLA 微调进行分析，形成 interventional → supporting → constraining 的证据层次。这种三角验证的方法论在 VLA 机制分析中尚属首次，且方法论本身可迁移至其他 VLA 研究。\n\n**S2. Readout token 发现具有实用价值** [R1, R2] — 发现 readout token 是多模态整合的主要位点（R²=0.678 vs image_mean 的 chance-level），而 image token 对指令不敏感。这一发现对 VLA 架构设计（如 early-exit 推理、微调诊断）有直接指导意义。\n\n**S3. 训练-未训练因子设计** [R1, R3] — 对训练/未训练模型进行成对比较，使用因子控制隔离微调效应，而非仅报告训练后状态。这使得因果推断更可信。\n\n**S4. 附录极为详尽** [R1, R2, R3] — 21 页附录覆盖鲁棒性检验（距离度量、per-DOF、permutation、seed、demo subsample）、OOD 诊断、跨 benchmark (LIBERO-Spatial) 验证等。R3 特别指出可复现性做得好（checkpoint、dataset、seed、compute 均报告）。\n\n**S5. 剂量-反应分析** [R1, R3] — 4→32 头渐进消融呈现单调递增而非阈值效应（d=0.48→0.64），为 L1 注意力头的功能重要性提供了介入性证据。R3 进一步指出 counterfactual instruction analysis 中 shuffled condition (d=0.625) 对 positional sensitivity 的确认也有信息量。\n\n**S6. 实验设计严谨** [R3: Soundness 7/10] — factorial controls、7 种互补分析、cross-architecture 验证、demo-level split 消除时间泄漏、linear probe sensitivity analysis 等方法论质量高。\n\n---\n\n## Weaknesses\n\n### Must-Fix（不修复则建议拒稿）\n\n**W-MF1. CoRL scope 适配性不足** [R1, R2, R3 三方共识——本轮最高优先级问题]\n论文是纯分析/解释性工作，无机器人实验、无闭环验证、无策略改进。CoRL 2026 CFP 明确要求 \"demonstrate the relevance of proposed models, algorithms, datasets, and benchmarks to robotics\" 并警告 \"papers lacking robotics emphasis will be desk-rejected\"。论文的 actionable insight（如 early-exit 推理、L1 entropy 监控）仅作为假设提出，未做任何验证。Discussion 中 \"orthogonal contribution and a natural next step\" 的措辞显得对闭环验证过于轻描淡写。R3 补充了一个尖锐观察：ablation 后 MSE 几乎不变（0.498→0.497），这反而质疑了 routing 的功能意义——闭环 success rate 测量将直接回答这个问题。\n**建议**：要么补充至少一个 downstream 应用实验（如 L1 attention entropy 与 task failure 的相关性——在现有 rollout 数据上即可计算，成本低），要么将 venue 转向 ICML/NeurIPS 的 interpretability track。\n\n**W-MF2. \"Convergent reorganization\" 声称过强** [R1, R2, R3 三方共识]\n仅两个模型（OpenVLA, TraceVLA）的 Δ=0.003 不能支撑 \"convergent\" 这一暗示普遍性的术语。两个架构共享 causal decoder + ~32 layers + LIBERO + tokenized actions，本质上是同一架构家族内的比较。Exit-layer R² 差异 0.069 与 mid-layer Δ=0.003 形成矛盾，论文仅以 post-hoc speculation 解释（\"possibly reflecting architectural differences\"）。N=2 的跨架构比较本质上是 case study，无法排除巧合。\n**建议**：将 \"convergent\" 降级为 \"consistent\" 或 \"preliminary evidence\"；精确界定收敛范围（仅 mid-layer，exit-layer 分歧）。\n\n**W-MF3. 统计效力不足（N_eff=10）** [R1, R2, R3 三方共识]\nBootstrap 基于 10 个 task 的聚合，N_eff=10 严重限制了统计推断的可靠性。LIBERO-Goal Δ=+0.017 n.s. vs LIBERO-Spatial Δ=+0.023 p<0.001——差异仅 0.006 但显著性截然不同，说明 power 不足。R3 补充：Table 11 的 Mann-Whitney U 检验在 N=6 vs N=4 上得到 p=0.033，在如此小 N 下解释力有限。\n**建议**：提供 power analysis（N=10 可检测的最小效应量）；对跨架构 convergence 使用 TOST 等价性检验。\n\n**W-MF4. 正文超出 8 页限制** [R3 独立发现——desk rejection 风险]\n正文约 8.7 页，超出 CoRL 2026 的 8 页限制约 0.7 页。Discussion 的 Synthesis、Mechanistic interpretation、Functional stages、Limitations 四个段落 + Conclusion 延伸到第 9 页。这是 desk rejection 的常见理由。**注意**：此问题在 Round 12-13 曾被修复，但 R14 fresh review 发现回归。\n**建议**：将 Discussion 中 Mechanistic interpretation 和 Functional stages 的预测性内容移至 Appendix；压缩 Introduction 中与 Abstract 重复的量化描述。\n\n**W-MF5. Abstract/Introduction 信息过载** [R3 独立发现]\nAbstract 在 ~200 words 内塞入了至少 15 个定量结果（d=0.48→0.64、p=0.033、R²+0.069、2.5× 等），远超同领域论文的 abstract 信息密度。Introduction 几乎逐字重复 abstract 的所有量化结论。R3 评 Clarity 仅 4/10。**注意**：同 W-MF4，此问题也是回归。\n**建议**：Abstract 只保留 3 个核心发现的定性描述 + 1-2 个关键数字；Introduction 聚焦 motivation。\n\n### Should-Fix（不影响接收决定，但显著提升论文质量）\n\n**W-SF1. Cohen's d 计算方法需澄清** [R1 提出, R2 部分反驳, R3 同意——唯一未完全解决的技术分歧]\nR1 认为对配对数据使用标准 Cohen's d 可能高估效应量。R2 反驳指出 paired d_z = mean_diff / SD_diff > standard d（因 SD_diff < SD_pooled when r>0），当前报告反而保守。R3 从不同角度支持 R1——token-level observations 有强时序相关性。**技术分歧**：偏差方向在数学上 R2 更准确，但三方共识是应明确报告使用的公式和配对版本数值。\n**建议**：报告 paired d_z 和配对相关系数 r；在 Method 中讨论选择。\n\n**W-SF2. 仅 LIBERO 基准** [R1, R2, R3 共识]\n所有实验基于 LIBERO 家族（Goal + Spatial），instruction diversity 有限——10 个 tasks 的差异主要在 object 和 target location。缺少更复杂 benchmark（如 CALVIN、Language-Table）的验证。\n**建议**：至少在 Discussion 中讨论 LIBERO 特异性风险。\n\n**W-SF3. 缺少关键参考文献** [R1, R2, R3 共识]\n(a) Aghajanyan et al. (ACL 2021, intrinsic dimensionality of fine-tuning) 和 Kumar et al. (NeurIPS 2022, fine-tuning distorts pretrained features) 与核心问题直接相关但未引用 [R1, R2]\n(b) VLA efficiency/pruning 工作（如 TinyVLA, ECoT）未覆盖 [R1, R2]\n(c) 多条引用仍使用 arXiv preprint 而非已发表版本——R3 列出 6 条具体条目（kim2024_openvla, karamcheti2024, touvron2023, belrose2023, padalkar2023, black2024_pi0）[R3]\n\n**W-SF4. 单 checkpoint 分析** [R2 提出, R1 同意]\n仅分析最终 checkpoint，缺少训练动态。至少在几个中间 checkpoint 上报告 L1 head count 或 readout R² 的演化趋势。\n\n**W-SF5. Finding 3 定位需强化** [R2→R1 反驳→R2 接受→R3 给出 nuanced 评价]\nR2 初认为 Finding 3（image token instruction-blindness）near trivial——causal mask 的必然结果。R1 反驳区分三层：(a) image_mean at-chance 确实是 expected；(b) readout 从 L1 即 100% 是 non-trivial gradient；(c) training 不改变 image blindness 但大幅提升 readout 是 non-trivial asymmetry。R2 接受。R3 提供了关键 nuance：如果 image tokens 在 instruction tokens 之前（vision-first ordering），则 instruction-blindness 是 causal mask 的必然；但论文未明确声明 token ordering。无论如何，readout gradient 和 training asymmetry 是实质发现。\n**建议**：正文明确声明 token ordering；Abstract 区分 expected（image_mean）vs surprising（readout gradient）部分。\n\n**W-SF6. Figure 1 不在首页** [R3 独立发现——回归问题]\nFigure 1 出现在 PDF page 6，前 5 页全是密集文字。Round 13 曾声称修复但 R14 发现回归。\n\n**W-SF7. Limitations 格式不满足 CoRL 要求** [R3 独立发现]\nLimitations 仍是 Discussion 的 `\\paragraph`，而非独立 section。CoRL 2026 要求 \"All submissions should include a Limitations section\"。\n\n**W-SF8. 层编号 off-by-one** [R3 独立发现——回归问题]\nmethod.tex: \"L1--L31 the 32 transformer layers\"——L1 到 L31 inclusive 只有 31 个索引，与 \"32 transformer layers\" 矛盾。Round 13 曾声称修复但 R14 发现回归。\n\n**W-SF9. 术语不一致** [R1, R2, R3 三方独立发现]\nreadout token / last_preaction；instruction-dominant heads / dominant heads / instruction heads；7-D action vectors / 7-D actions——多组术语混用。\n\n---\n\n## Reviewer Consensus（三方共识）\n\n1. **CoRL scope 是首要问题** — 三位审稿人均认为纯分析性论文缺乏 robotics 应用验证是最大短板。R3 尤其尖锐：ablation 不改变 MSE 质疑了 routing 的功能意义。\n2. **\"Convergent\" 声称过强** — N=2 同质架构 + N_eff=10 的统计基础不足以支撑此术语\n3. **方法论框架本身有价值** — 三角验证方法论和 readout token 发现是实质贡献\n4. **附录质量高** — 鲁棒性检验详尽，可复现性好\n5. **需补充参考文献** — VLA efficiency 和 fine-tuning representation 领域引用缺失；多条 arXiv 引用需更新\n6. **闭环验证缺失** — 三方一致认为至少应验证一个 actionable implication\n\n## Reviewer Divergence（分歧点）\n\n| 议题 | R1 | R2 | R3 | 解决状态 |\n|------|----|----|----|----|\n| Finding 3 trivial? | Non-trivial（三层区分） | 初 trivial → 接受 R1 | Nuanced（需声明 token ordering） | ✅ 基本解决 |\n| Cohen's d 偏差方向 | 可能高估 | paired d_z > standard d（保守） | Token 相关性高估 | ⚠️ 方向未解决，但共识报告配对版 |\n| Title \"Reorganizes\" | 可接受 | 初质疑 → 撤回 | 辩护\"Language Routes\"有数据支持 | ✅ 已解决 |\n| MLP probe capacity | 过大（1.05M params） | 未强调 | 已充分回应（Appendix A.6 linear probe） | ✅ R3 有力反驳 |\n\n---\n\n## Questions for Authors\n\n1. L1 的 24/32 instruction-dominant heads 中，是否有 head 在 pretrained Llama-2 中已存在 instruction sensitivity？Fine-tuning 是 amplifying 还是 creating？\n2. Δ=0.003 的 TOST 等价性检验（ε=0.05）的 p 值是多少？如果不显著，\"convergent\" 声称如何辩护？\n3. 是否考虑过在训练中间 checkpoint 上测量 L1 head count 的演化曲线？\n4. Readout token 的 R²=0.678——剩余 32.2% 的方差来源是什么？\n5. Ablation 后 MSE 几乎不变（0.498→0.497），但 trajectory divergence d>0.6。如何 reconcile？是否意味着 routing 影响 trajectory shape 但不影响 per-step error？\n6. OpenVLA 的 token ordering 是什么？Image tokens 在 instruction tokens 之前还是之后？这直接影响 Finding 3 的 triviality 判断。[R3 提出]\n\n---\n\n## Missing References\n\n**高优先级**（与核心问题直接相关）：\n- Aghajanyan et al. (ACL 2021) — Intrinsic Dimensionality Explains the Effectiveness of Language Model Fine-Tuning\n- Kumar et al. (NeurIPS 2022) — Fine-Tuning Can Distort Pretrained Features and Underperform Out-of-Distribution\n- \"What Do Visual Tokens Really Encode?\" (arXiv:2603.00510) — 直接研究 VLM visual token 编码\n\n**中优先级**：\n- TinyVLA / ECoT 或其他 VLA compression/efficiency 工作\n- Diffusion/flow-matching VLA 表征分析\n- VLA scaling laws 相关工作\n\n**引用版本更新需求**（6 条 arXiv→published）：\nkim2024_openvla, karamcheti2024, touvron2023_llama2, belrose2023_tunedlens, padalkar2023_oxe, black2024_pi0\n\n---\n\n## External Review\n\n**外部审稿（Stanford Agentic Reviewer）：pending，未返回。**\n\n---\n\n## Visual Layout Check（非评分项）\n\n由独立视觉审查 Agent 完成，结果如下：\n\n- **Critical (1)**：Page 31（附录末页）约 90% 空白，严重浪费版面\n- **Warnings (4)**：\n  - Pages 2-4：连续 3 页无图表，纯文字密度过高\n  - Page 16：图表标签字号过小，可能不满足打印可读性\n  - Page 21：表格过于密集，建议拆分或调整间距\n  - Page 30：同上，表格密度过高\n- **Info (21)**：其余为次要排版观察\n\nR3 的独立审查与视觉 Agent 发现一致：pages 2-4 无图（R3-W1: Figure 1 在 page 6）、表格密度高（R3-S4: resizebox 压缩字体）。\n\n---\n\n## Overall Assessment\n\n**Overall Score: 5.0/10 → Weak Reject**\n\n| Reviewer | 侧重 | 初始分 | 最终分 | 变化原因 |\n|----------|------|--------|--------|----------|\n| R1 | 方法/实验严谨性 | 6/10 | 6/10 | 无变化 |\n| R2 | 新颖性/scope/完整性 | 4/10 | 5/10 | 接受 R1 对 Finding 3 和 effect size 的反驳 |\n| R3 | 写作/格式/可复现性 | 5/10 | 5/10 | 无变化 |\n\n**R3 官方维度打分**：Significance & Novelty 6/10, Relevance to Robotics 5/10, Soundness 7/10, Clarity 4/10, Reproducibility 7/10\n\n**核心判断**：论文的方法论框架（三角验证 + 因子设计）和 readout token 发现是实质贡献，但五个结构性问题使其不适合当前形式投稿 CoRL：\n1. **CoRL scope**：纯分析无闭环验证，与 CoRL robotics 受众不匹配\n2. **Convergent claim**：N=2 同质架构 + N_eff=10 统计基础不足\n3. **超页限**：正文 8.7 页，超出 8 页限制——desk rejection 风险\n4. **可读性**：Abstract 信息过载 (R3 Clarity 4/10)，前 5 页无图表\n5. **LIBERO 单一 benchmark**：instruction diversity 有限\n\n**特别警告**：R12-N2（超页限）和 R12-N3（信息过载）在 Round 13 曾被标记为 resolved，但 Round 14 fresh review 发现这些问题回归。Research Director 需要验证这些修复确实生效。\n\n**建议路径**：\n- **若坚持 CoRL**（deadline 2026-05-29，仅剩 9 天）：\n  - 紧急：压缩正文至 8 页、精简 Abstract/Intro\n  - 高优先级：补充 L1 entropy 与 task failure 相关性分析（低成本）\n  - 中优先级：弱化 \"convergent\" 措辞、补充引用、修复层编号/术语\n- **若转投**：ICML/NeurIPS interpretability track 或 CoRL Workshop 可能是更自然的归属\n\n---\n\n## Detailed Comments\n\n### 正文修改建议\n\n1. **Abstract**: \"convergent reorganization\" → \"consistent reorganization pattern\"\n2. **Abstract**: 删除至少 10 个定量数字，只保留 Δ=0.003 和一个 probe 数字\n3. **Abstract**: \"confirms expected functional specialization\" → 区分 trivial (image_mean) vs non-trivial (readout gradient)\n4. **Title**: 当前 \"Reorganizes\" 可接受，但考虑加限定词 \"in Causal-Decoder VLAs\"\n5. **Introduction**: 删除与 Abstract 重复的量化描述，聚焦 gap statement\n6. **Method 层编号**: \"L1--L31 the 32 transformer layers\" → 统一为 \"L1--L32 the 32 transformer layers\" 或修正索引范围\n7. **Method**: 明确声明 token ordering（vision-first? instruction-first?）\n8. **Section 4.3 跨架构**: 加入 N=2 caveat 和 exit-layer 分歧讨论\n9. **Discussion \"orthogonal contribution\"**: → \"complementary and necessary next step\"\n10. **Discussion**: Mechanistic interpretation 和 Functional stages 移至 Appendix（回收 ~0.5 页）\n11. **Conclusion**: 当前 3 行过短，补充 broader impact 和 limitation summary\n12. **Limitations**: 提升为独立 `\\section{Limitations}` 满足 CoRL 要求\n13. **术语**: 全文统一 readout token / instruction-dominant heads / 7-D actions\n\n### 统计方法改进\n\n14. **Cohen's d**: 报告 paired d_z 和配对相关系数 r\n15. **TOST**: 对 Δ=0.003 做等价性检验\n16. **Power analysis**: 报告 N=10 可检测的最小效应量\n17. **Permutation test**: 增加到 ≥10,000 shuffles\n18. **FDR**: 考虑添加全局 Bonferroni-adjusted p-values\n\n### 引用和格式\n\n19. **新增引用**: Aghajanyan 2021, Kumar 2022, visual token encoding (2603.00510)\n20. **更新引用**: 6 条 arXiv → published version\n21. **Figure 1**: 确保出现在 page 1\n22. **GenAI disclosure**: 移至 Appendix 合适位置\n23. **Table 2 caption**: 展开缩写\n24. **Appendix resizebox**: 改用 \\small 或 \\footnotesize\n25. **Page 31 空白**: 合并或删除",
    "project": "vla-ssd",
    "reviewer_ids_acknowledged": "[1, 2, 3]",
    "cross_response_reviewer_ids": "[1, 2, 3]",
    "overall_score": "weak reject",
    "review_chat_id": "oc_554a5023cde4d603635cf97e6ab8151a"
  }
}
```

</details>

---


### Tool result

_source line 1182 · 2026-05-20T17:03:27.021429+00:00_

{"result":"{\"success\": false, \"data\": {\"existing_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/review_reports/round_14.md\", \"round\": 14}, \"error\": \"Round 14 report ALREADY submitted (persisted at `/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/review_reports/round_14.md`). Research Director was triggered once and may still be processing it; re-submitting silently would trigger the protocol again with conflicting content.\\n\\nExisting report frontmatter (first 400 chars):\\n---\\nround: 14\\nreview_mode: fresh\\noverall_score: borderline\\ntimestamp: 2026-05-20T16:22:31.679082+00:00\\nreviewer_ids: [1, 2, 3]\\ncross_response_reviewer_ids: [1, 2, 3]\\nforce_resubmit: False\\n---\\n\\n# Round 13 审稿报告（Continue Review）\\n\\n**论文**: \\\"Vision Encodes, Language Reorganizes: Token-Level Representational Analysis of VLA Fine-Tuning\\\"\\n**Venue**: CoRL 2026（截止 2026-05-29）\\n**审稿模式**: 继续审稿（基于 Round 12 修改验证）\\n\\nIf you intentionally want to replace it (e.g. caught a Step 2 cross-sharing gap and synthesized a corrected report), call again with force_resubmit=True. Otherwise the original submission stands — pause and verify before forcing.\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 0
}
```

</details>

---


### Assistant

_source line 1183 · 2026-05-20T17:04:32.038667+00:00_

已有一份旧的 round 14 报告（内容是 Round 13 Continue Review 的残留），需要用本轮 fresh review 的完整报告替换。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director"
}
```

</details>

---


## Round 109

## Round 109

4 recorded events


### User

_source line 1184 · 2026-05-20T17:04:34.901681+00:00_

[Reviewer 2 审稿结果]:
二次回应已提交。总结：

- **R2-N3**：[AGREE] 接受 R1 的三层分解，撤回 "完全 trivial" 判断，降级为 should-fix
- **R2-W2**：[AGREE] 承认选择性引用偏差，撤回 "效果量极小" 的全面表述；但指出 R1 引用的 "RSA ρ=0.692" 可能是混淆了 probe R² 列
- **R2-W3**：[AGREE] 撤回 "无因果干预" 表述，论文确实有 interventional 分析

评分从 4/10 上调至 5/10，但 N1（CoRL scope fit）和 N2（N=2 convergent claim）仍维持 critical。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 1185 · 2026-05-20T17:06:57.676279+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "report": "# Consolidated Review Report — Round 14 (Fresh)\n\n**Paper**: \"Vision Encodes, Language Reorganizes: Token-Level Representational Analysis of VLA Fine-Tuning\"\n**Target Venue**: CoRL 2026 (deadline 2026-05-29)\n**Reviewers**: R1 (方法/实验严谨性), R2 (新颖性/scope/完整性), R3 (写作质量/格式合规/可复现性)\n**Review Date**: 2026-05-20\n\n---\n\n## Summary\n\n本文对 VLA（Vision-Language-Action）模型的微调过程进行逐层、逐 token 类型的表征分析。以 OpenVLA-7B 为主要分析对象，辅以 TraceVLA 做跨架构对比，提出三个发现：(1) 微调将指令注意力重新分配至 entry-exit 层，L1 为主要 hub；(2) 两个不同架构的 VLA 在训练后达到相似的中层表征（Δ=0.003）；(3) image token 与 readout token 存在功能分化——image token 对指令不敏感，readout token 是多模态整合中心。论文包含 7 项互补分析（interventional、supporting、constraining）和 21 页附录。\n\n---\n\n## Strengths\n\n**S1. 系统性的多层次分析框架** [R1, R2, R3 共识] — 从注意力头统计、RSA、CKA、线性探针、消融、反事实、剂量-反应等 7 个互补视角对 VLA 微调进行分析，形成 interventional → supporting → constraining 的证据层次。这种三角验证的方法论在 VLA 机制分析中尚属首次，且方法论本身可迁移至其他 VLA 研究。\n\n**S2. Readout token 发现具有实用价值** [R1, R2] — 发现 readout token 是多模态整合的主要位点（R²=0.678 vs image_mean 的 chance-level），而 image token 对指令不敏感。这一发现对 VLA 架构设计（如 early-exit 推理、微调诊断）有直接指导意义。\n\n**S3. 训练-未训练因子设计** [R1, R3] — 对训练/未训练模型进行成对比较，使用因子控制隔离微调效应，而非仅报告训练后状态。这使得因果推断更可信。\n\n**S4. 附录极为详尽** [R1, R2, R3] — 21 页附录覆盖鲁棒性检验（距离度量、per-DOF、permutation、seed、demo subsample）、OOD 诊断、跨 benchmark (LIBERO-Spatial) 验证等。R3 特别指出可复现性做得好（checkpoint、dataset、seed、compute 均报告）。\n\n**S5. 剂量-反应分析** [R1, R3] — 4→32 头渐进消融呈现单调递增而非阈值效应（d=0.48→0.64），为 L1 注意力头的功能重要性提供了介入性证据。R3 进一步指出 counterfactual instruction analysis 中 shuffled condition (d=0.625) 对 positional sensitivity 的确认也有信息量。\n\n**S6. 实验设计严谨** [R3: Soundness 7/10] — factorial controls、7 种互补分析、cross-architecture 验证、demo-level split 消除时间泄漏、linear probe sensitivity analysis 等方法论质量高。\n\n---\n\n## Weaknesses\n\n### Must-Fix（不修复则建议拒稿）\n\n**W-MF1. CoRL scope 适配性不足** [R1, R2, R3 三方共识——本轮最高优先级问题]\n论文是纯分析/解释性工作，无机器人实验、无闭环验证、无策略改进。CoRL 2026 CFP 明确要求 \"demonstrate the relevance of proposed models, algorithms, datasets, and benchmarks to robotics\" 并警告 \"papers lacking robotics emphasis will be desk-rejected\"。论文的 actionable insight（如 early-exit 推理、L1 entropy 监控）仅作为假设提出，未做任何验证。Discussion 中 \"orthogonal contribution and a natural next step\" 的措辞显得对闭环验证过于轻描淡写。R3 补充了一个尖锐观察：ablation 后 MSE 几乎不变（0.498→0.497），这反而质疑了 routing 的功能意义——闭环 success rate 测量将直接回答这个问题。\n**建议**：要么补充至少一个 downstream 应用实验（如 L1 attention entropy 与 task failure 的相关性——在现有 rollout 数据上即可计算，成本低），要么将 venue 转向 ICML/NeurIPS 的 interpretability track。\n\n**W-MF2. \"Convergent reorganization\" 声称过强** [R1, R2, R3 三方共识]\n仅两个模型（OpenVLA, TraceVLA）的 Δ=0.003 不能支撑 \"convergent\" 这一暗示普遍性的术语。两个架构共享 causal decoder + ~32 layers + LIBERO + tokenized actions，本质上是同一架构家族内的比较。Exit-layer R² 差异 0.069 与 mid-layer Δ=0.003 形成矛盾，论文仅以 post-hoc speculation 解释（\"possibly reflecting architectural differences\"）。N=2 的跨架构比较本质上是 case study，无法排除巧合。\n**建议**：将 \"convergent\" 降级为 \"consistent\" 或 \"preliminary evidence\"；精确界定收敛范围（仅 mid-layer，exit-layer 分歧）。\n\n**W-MF3. 统计效力不足（N_eff=10）** [R1, R2, R3 三方共识]\nBootstrap 基于 10 个 task 的聚合，N_eff=10 严重限制了统计推断的可靠性。LIBERO-Goal Δ=+0.017 n.s. vs LIBERO-Spatial Δ=+0.023 p<0.001——差异仅 0.006 但显著性截然不同，说明 power 不足。R3 补充：Table 11 的 Mann-Whitney U 检验在 N=6 vs N=4 上得到 p=0.033，在如此小 N 下解释力有限。\n**建议**：提供 power analysis（N=10 可检测的最小效应量）；对跨架构 convergence 使用 TOST 等价性检验。\n\n**W-MF4. 正文超出 8 页限制** [R3 独立发现——desk rejection 风险]\n正文约 8.7 页，超出 CoRL 2026 的 8 页限制约 0.7 页。Discussion 的 Synthesis、Mechanistic interpretation、Functional stages、Limitations 四个段落 + Conclusion 延伸到第 9 页。这是 desk rejection 的常见理由。**注意**：此问题在 Round 12-13 曾被修复，但 R14 fresh review 发现回归。\n**建议**：将 Discussion 中 Mechanistic interpretation 和 Functional stages 的预测性内容移至 Appendix；压缩 Introduction 中与 Abstract 重复的量化描述。\n\n**W-MF5. Abstract/Introduction 信息过载** [R3 独立发现]\nAbstract 在 ~200 words 内塞入了至少 15 个定量结果（d=0.48→0.64、p=0.033、R²+0.069、2.5× 等），远超同领域论文的 abstract 信息密度。Introduction 几乎逐字重复 abstract 的所有量化结论。R3 评 Clarity 仅 4/10。**注意**：同 W-MF4，此问题也是回归。\n**建议**：Abstract 只保留 3 个核心发现的定性描述 + 1-2 个关键数字；Introduction 聚焦 motivation。\n\n### Should-Fix（不影响接收决定，但显著提升论文质量）\n\n**W-SF1. Cohen's d 计算方法需澄清** [R1 提出, R2 部分反驳, R3 同意——唯一未完全解决的技术分歧]\nR1 认为对配对数据使用标准 Cohen's d 可能高估效应量。R2 反驳指出 paired d_z = mean_diff / SD_diff > standard d（因 SD_diff < SD_pooled when r>0），当前报告反而保守。R3 从不同角度支持 R1——token-level observations 有强时序相关性。**技术分歧**：偏差方向在数学上 R2 更准确，但三方共识是应明确报告使用的公式和配对版本数值。\n**建议**：报告 paired d_z 和配对相关系数 r；在 Method 中讨论选择。\n\n**W-SF2. 仅 LIBERO 基准** [R1, R2, R3 共识]\n所有实验基于 LIBERO 家族（Goal + Spatial），instruction diversity 有限——10 个 tasks 的差异主要在 object 和 target location。缺少更复杂 benchmark（如 CALVIN、Language-Table）的验证。\n**建议**：至少在 Discussion 中讨论 LIBERO 特异性风险。\n\n**W-SF3. 缺少关键参考文献** [R1, R2, R3 共识]\n(a) Aghajanyan et al. (ACL 2021, intrinsic dimensionality of fine-tuning) 和 Kumar et al. (NeurIPS 2022, fine-tuning distorts pretrained features) 与核心问题直接相关但未引用 [R1, R2]\n(b) VLA efficiency/pruning 工作（如 TinyVLA, ECoT）未覆盖 [R1, R2]\n(c) 多条引用仍使用 arXiv preprint 而非已发表版本——R3 列出 6 条具体条目（kim2024_openvla, karamcheti2024, touvron2023, belrose2023, padalkar2023, black2024_pi0）[R3]\n\n**W-SF4. 单 checkpoint 分析** [R2 提出, R1 同意]\n仅分析最终 checkpoint，缺少训练动态。至少在几个中间 checkpoint 上报告 L1 head count 或 readout R² 的演化趋势。\n\n**W-SF5. Finding 3 定位需强化** [R2→R1 反驳→R2 接受→R3 nuanced 评价]\nR2 初认为 Finding 3（image token instruction-blindness）near trivial——causal mask 的必然结果。R1 反驳区分三层：(a) image_mean at-chance 确实是 expected；(b) readout 从 L1 即 100% 是 non-trivial gradient；(c) training 不改变 image blindness 但大幅提升 readout 是 non-trivial asymmetry。R2 接受。R3 提供了关键 nuance：如果 image tokens 在 instruction tokens 之前（vision-first ordering），则 instruction-blindness 是 causal mask 的必然；但论文未明确声明 token ordering。\n**建议**：正文明确声明 token ordering；Abstract 区分 expected（image_mean）vs surprising（readout gradient）部分。\n\n**W-SF6. Figure 1 不在首页** [R3——回归问题]\nFigure 1 出现在 PDF page 6，前 5 页全是密集文字。Round 13 曾声称修复但 R14 发现回归。\n\n**W-SF7. Limitations 格式不满足 CoRL 要求** [R3]\nLimitations 仍是 Discussion 的 `\\paragraph`，而非独立 section。\n\n**W-SF8. 层编号 off-by-one** [R3——回归问题]\nmethod.tex: \"L1--L31 the 32 transformer layers\"——31 个索引 ≠ 32 层。\n\n**W-SF9. 术语不一致** [R1, R2, R3 三方独立发现]\nreadout token / last_preaction；instruction-dominant heads / dominant heads / instruction heads 混用。\n\n---\n\n## Reviewer Consensus（三方共识）\n\n1. **CoRL scope 是首要问题** — 三位审稿人均认为纯分析性论文缺乏 robotics 应用验证是最大短板\n2. **\"Convergent\" 声称过强** — N=2 同质架构 + N_eff=10 的统计基础不足\n3. **方法论框架本身有价值** — 三角验证方法论和 readout token 发现是实质贡献\n4. **附录质量高** — 鲁棒性检验详尽，可复现性好\n5. **需补充参考文献** — 多领域引用缺失；多条 arXiv 引用需更新\n6. **闭环验证缺失** — 三方一致认为至少应验证一个 actionable implication\n\n## Reviewer Divergence（分歧点）\n\n| 议题 | R1 | R2 | R3 | 解决状态 |\n|------|----|----|----|----|\n| Finding 3 trivial? | Non-trivial（三层区分） | 初 trivial → 接受 R1 | Nuanced（需声明 token ordering） | ✅ 基本解决 |\n| Cohen's d 偏差方向 | 可能高估 | paired d_z > standard d（保守） | Token 相关性高估 | ⚠️ 方向未解决，共识报告配对版 |\n| MLP probe capacity | 过大（1.05M params） | 未强调 | 已充分回应（Appendix A.6） | ✅ R3 有力反驳 |\n\n---\n\n## Questions for Authors\n\n1. L1 的 24/32 instruction-dominant heads 中，是否有 head 在 pretrained Llama-2 中已存在 instruction sensitivity？Fine-tuning 是 amplifying 还是 creating？\n2. Δ=0.003 的 TOST 等价性检验（ε=0.05）的 p 值是多少？\n3. 是否考虑过在训练中间 checkpoint 上测量 L1 head count 的演化曲线？\n4. Readout token 的 R²=0.678——剩余 32.2% 的方差来源是什么？\n5. Ablation 后 MSE 几乎不变（0.498→0.497），但 trajectory divergence d>0.6。如何 reconcile？\n6. OpenVLA 的 token ordering 是什么？Image tokens 在 instruction tokens 之前还是之后？[R3 提出]\n\n---\n\n## Missing References\n\n**高优先级**：Aghajanyan et al. (ACL 2021), Kumar et al. (NeurIPS 2022), \"What Do Visual Tokens Really Encode?\" (arXiv:2603.00510)\n**中优先级**：TinyVLA/ECoT, diffusion VLA 表征分析, VLA scaling laws\n**引用版本更新**（6 条）：kim2024_openvla, karamcheti2024, touvron2023_llama2, belrose2023_tunedlens, padalkar2023_oxe, black2024_pi0\n\n---\n\n## External Review\n\n**外部审稿（Stanford Agentic Reviewer）：pending，未返回。**\n\n---\n\n## Visual Layout Check（非评分项）\n\n- **Critical (1)**：Page 31 约 90% 空白\n- **Warnings (4)**：Pages 2-4 无图表；Page 16 标签字号小；Pages 21, 30 表格密集\n- **Info (21)**：次要排版观察\n\nR3 的独立审查与视觉 Agent 发现一致。\n\n---\n\n## Overall Assessment\n\n**Overall Score: 5.3/10 → Weak Reject**\n\n| Reviewer | 侧重 | 初始分 | 最终分 | 变化原因 |\n|----------|------|--------|--------|----------|\n| R1 | 方法/实验严谨性 | 6/10 | 6/10 | 无变化 |\n| R2 | 新颖性/scope/完整性 | 4/10 | 5/10 | 接受 R1 对 Finding 3 和 effect size 的反驳 |\n| R3 | 写作/格式/可复现性 | 5/10 | 5/10 | 无变化 |\n\n**R3 官方维度打分**：Significance 6/10, Relevance to Robotics 5/10, Soundness 7/10, Clarity 4/10, Reproducibility 7/10\n\n**核心判断**：方法论框架和 readout token 发现是实质贡献，但五个结构性问题使其不适合当前形式投稿 CoRL：(1) 纯分析无闭环验证；(2) convergent claim 统计基础不足；(3) 超页限（desk rejection 风险）；(4) 可读性差（Clarity 4/10）；(5) LIBERO 单一 benchmark。\n\n**特别警告**：R12-N2（超页限）和 R12-N3（信息过载）在 Round 13 曾被标记为 resolved，但 Round 14 fresh review 发现回归。Research Director 需验证修复生效。\n\n**建议路径**：\n- **若坚持 CoRL**（仅剩 9 天）：紧急压缩至 8 页 + 精简 Abstract/Intro + 补充 L1 entropy 验证（低成本）+ 弱化 convergent + 修复格式回归\n- **若转投**：ICML/NeurIPS interpretability track 或 CoRL Workshop\n\n---\n\n## Detailed Comments\n\n### 正文修改（按优先级排序）\n\n1. 压缩正文至 8 页：Discussion Mechanistic interpretation + Functional stages 移至 Appendix\n2. Abstract 删除至少 10 个定量数字，只保留核心 1-2 个\n3. Introduction 删除与 Abstract 重复的量化描述\n4. \"convergent reorganization\" → \"consistent reorganization pattern\"\n5. \"orthogonal contribution\" → \"complementary and necessary next step\"\n6. Limitations 提升为独立 section\n7. 层编号 off-by-one 修复\n8. 术语统一（readout token / instruction-dominant heads）\n9. Figure 1 确保在 page 1\n10. Token ordering 明确声明\n\n### 统计方法\n\n11. 报告 paired Cohen's d_z 和配对相关系数 r\n12. 对 Δ=0.003 做 TOST 等价性检验\n13. Power analysis（N=10 最小可检测效应量）\n14. Permutation test 增加到 ≥10,000 shuffles\n\n### 引用和格式\n\n15. 新增引用：Aghajanyan 2021, Kumar 2022\n16. 更新 6 条 arXiv → published\n17. GenAI disclosure 移至 Appendix\n18. Table 2 caption 展开缩写\n19. Page 31 空白处理",
  "project": "vla-ssd",
  "reviewer_ids_acknowledged": "[1, 2, 3]",
  "cross_response_reviewer_ids": "[1, 2, 3]",
  "overall_score": "weak reject",
  "review_chat_id": "oc_554a5023cde4d603635cf97e6ab8151a",
  "force_resubmit": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "report": "# Consolidated Review Report — Round 14 (Fresh)\n\n**Paper**: \"Vision Encodes, Language Reorganizes: Token-Level Representational Analysis of VLA Fine-Tuning\"\n**Target Venue**: CoRL 2026 (deadline 2026-05-29)\n**Reviewers**: R1 (方法/实验严谨性), R2 (新颖性/scope/完整性), R3 (写作质量/格式合规/可复现性)\n**Review Date**: 2026-05-20\n\n---\n\n## Summary\n\n本文对 VLA（Vision-Language-Action）模型的微调过程进行逐层、逐 token 类型的表征分析。以 OpenVLA-7B 为主要分析对象，辅以 TraceVLA 做跨架构对比，提出三个发现：(1) 微调将指令注意力重新分配至 entry-exit 层，L1 为主要 hub；(2) 两个不同架构的 VLA 在训练后达到相似的中层表征（Δ=0.003）；(3) image token 与 readout token 存在功能分化——image token 对指令不敏感，readout token 是多模态整合中心。论文包含 7 项互补分析（interventional、supporting、constraining）和 21 页附录。\n\n---\n\n## Strengths\n\n**S1. 系统性的多层次分析框架** [R1, R2, R3 共识] — 从注意力头统计、RSA、CKA、线性探针、消融、反事实、剂量-反应等 7 个互补视角对 VLA 微调进行分析，形成 interventional → supporting → constraining 的证据层次。这种三角验证的方法论在 VLA 机制分析中尚属首次，且方法论本身可迁移至其他 VLA 研究。\n\n**S2. Readout token 发现具有实用价值** [R1, R2] — 发现 readout token 是多模态整合的主要位点（R²=0.678 vs image_mean 的 chance-level），而 image token 对指令不敏感。这一发现对 VLA 架构设计（如 early-exit 推理、微调诊断）有直接指导意义。\n\n**S3. 训练-未训练因子设计** [R1, R3] — 对训练/未训练模型进行成对比较，使用因子控制隔离微调效应，而非仅报告训练后状态。这使得因果推断更可信。\n\n**S4. 附录极为详尽** [R1, R2, R3] — 21 页附录覆盖鲁棒性检验（距离度量、per-DOF、permutation、seed、demo subsample）、OOD 诊断、跨 benchmark (LIBERO-Spatial) 验证等。R3 特别指出可复现性做得好（checkpoint、dataset、seed、compute 均报告）。\n\n**S5. 剂量-反应分析** [R1, R3] — 4→32 头渐进消融呈现单调递增而非阈值效应（d=0.48→0.64），为 L1 注意力头的功能重要性提供了介入性证据。R3 进一步指出 counterfactual instruction analysis 中 shuffled condition (d=0.625) 对 positional sensitivity 的确认也有信息量。\n\n**S6. 实验设计严谨** [R3: Soundness 7/10] — factorial controls、7 种互补分析、cross-architecture 验证、demo-level split 消除时间泄漏、linear probe sensitivity analysis 等方法论质量高。\n\n---\n\n## Weaknesses\n\n### Must-Fix（不修复则建议拒稿）\n\n**W-MF1. CoRL scope 适配性不足** [R1, R2, R3 三方共识——本轮最高优先级问题]\n论文是纯分析/解释性工作，无机器人实验、无闭环验证、无策略改进。CoRL 2026 CFP 明确要求 \"demonstrate the relevance of proposed models, algorithms, datasets, and benchmarks to robotics\" 并警告 \"papers lacking robotics emphasis will be desk-rejected\"。论文的 actionable insight（如 early-exit 推理、L1 entropy 监控）仅作为假设提出，未做任何验证。Discussion 中 \"orthogonal contribution and a natural next step\" 的措辞显得对闭环验证过于轻描淡写。R3 补充了一个尖锐观察：ablation 后 MSE 几乎不变（0.498→0.497），这反而质疑了 routing 的功能意义——闭环 success rate 测量将直接回答这个问题。\n**建议**：要么补充至少一个 downstream 应用实验（如 L1 attention entropy 与 task failure 的相关性——在现有 rollout 数据上即可计算，成本低），要么将 venue 转向 ICML/NeurIPS 的 interpretability track。\n\n**W-MF2. \"Convergent reorganization\" 声称过强** [R1, R2, R3 三方共识]\n仅两个模型（OpenVLA, TraceVLA）的 Δ=0.003 不能支撑 \"convergent\" 这一暗示普遍性的术语。两个架构共享 causal decoder + ~32 layers + LIBERO + tokenized actions，本质上是同一架构家族内的比较。Exit-layer R² 差异 0.069 与 mid-layer Δ=0.003 形成矛盾，论文仅以 post-hoc speculation 解释（\"possibly reflecting architectural differences\"）。N=2 的跨架构比较本质上是 case study，无法排除巧合。\n**建议**：将 \"convergent\" 降级为 \"consistent\" 或 \"preliminary evidence\"；精确界定收敛范围（仅 mid-layer，exit-layer 分歧）。\n\n**W-MF3. 统计效力不足（N_eff=10）** [R1, R2, R3 三方共识]\nBootstrap 基于 10 个 task 的聚合，N_eff=10 严重限制了统计推断的可靠性。LIBERO-Goal Δ=+0.017 n.s. vs LIBERO-Spatial Δ=+0.023 p<0.001——差异仅 0.006 但显著性截然不同，说明 power 不足。R3 补充：Table 11 的 Mann-Whitney U 检验在 N=6 vs N=4 上得到 p=0.033，在如此小 N 下解释力有限。\n**建议**：提供 power analysis（N=10 可检测的最小效应量）；对跨架构 convergence 使用 TOST 等价性检验。\n\n**W-MF4. 正文超出 8 页限制** [R3 独立发现——desk rejection 风险]\n正文约 8.7 页，超出 CoRL 2026 的 8 页限制约 0.7 页。Discussion 的 Synthesis、Mechanistic interpretation、Functional stages、Limitations 四个段落 + Conclusion 延伸到第 9 页。这是 desk rejection 的常见理由。**注意**：此问题在 Round 12-13 曾被修复，但 R14 fresh review 发现回归。\n**建议**：将 Discussion 中 Mechanistic interpretation 和 Functional stages 的预测性内容移至 Appendix；压缩 Introduction 中与 Abstract 重复的量化描述。\n\n**W-MF5. Abstract/Introduction 信息过载** [R3 独立发现]\nAbstract 在 ~200 words 内塞入了至少 15 个定量结果（d=0.48→0.64、p=0.033、R²+0.069、2.5× 等），远超同领域论文的 abstract 信息密度。Introduction 几乎逐字重复 abstract 的所有量化结论。R3 评 Clarity 仅 4/10。**注意**：同 W-MF4，此问题也是回归。\n**建议**：Abstract 只保留 3 个核心发现的定性描述 + 1-2 个关键数字；Introduction 聚焦 motivation。\n\n### Should-Fix（不影响接收决定，但显著提升论文质量）\n\n**W-SF1. Cohen's d 计算方法需澄清** [R1 提出, R2 部分反驳, R3 同意——唯一未完全解决的技术分歧]\nR1 认为对配对数据使用标准 Cohen's d 可能高估效应量。R2 反驳指出 paired d_z = mean_diff / SD_diff > standard d（因 SD_diff < SD_pooled when r>0），当前报告反而保守。R3 从不同角度支持 R1——token-level observations 有强时序相关性。**技术分歧**：偏差方向在数学上 R2 更准确，但三方共识是应明确报告使用的公式和配对版本数值。\n**建议**：报告 paired d_z 和配对相关系数 r；在 Method 中讨论选择。\n\n**W-SF2. 仅 LIBERO 基准** [R1, R2, R3 共识]\n所有实验基于 LIBERO 家族（Goal + Spatial），instruction diversity 有限——10 个 tasks 的差异主要在 object 和 target location。缺少更复杂 benchmark（如 CALVIN、Language-Table）的验证。\n**建议**：至少在 Discussion 中讨论 LIBERO 特异性风险。\n\n**W-SF3. 缺少关键参考文献** [R1, R2, R3 共识]\n(a) Aghajanyan et al. (ACL 2021, intrinsic dimensionality of fine-tuning) 和 Kumar et al. (NeurIPS 2022, fine-tuning distorts pretrained features) 与核心问题直接相关但未引用 [R1, R2]\n(b) VLA efficiency/pruning 工作（如 TinyVLA, ECoT）未覆盖 [R1, R2]\n(c) 多条引用仍使用 arXiv preprint 而非已发表版本——R3 列出 6 条具体条目（kim2024_openvla, karamcheti2024, touvron2023, belrose2023, padalkar2023, black2024_pi0）[R3]\n\n**W-SF4. 单 checkpoint 分析** [R2 提出, R1 同意]\n仅分析最终 checkpoint，缺少训练动态。至少在几个中间 checkpoint 上报告 L1 head count 或 readout R² 的演化趋势。\n\n**W-SF5. Finding 3 定位需强化** [R2→R1 反驳→R2 接受→R3 nuanced 评价]\nR2 初认为 Finding 3（image token instruction-blindness）near trivial——causal mask 的必然结果。R1 反驳区分三层：(a) image_mean at-chance 确实是 expected；(b) readout 从 L1 即 100% 是 non-trivial gradient；(c) training 不改变 image blindness 但大幅提升 readout 是 non-trivial asymmetry。R2 接受。R3 提供了关键 nuance：如果 image tokens 在 instruction tokens 之前（vision-first ordering），则 instruction-blindness 是 causal mask 的必然；但论文未明确声明 token ordering。\n**建议**：正文明确声明 token ordering；Abstract 区分 expected（image_mean）vs surprising（readout gradient）部分。\n\n**W-SF6. Figure 1 不在首页** [R3——回归问题]\nFigure 1 出现在 PDF page 6，前 5 页全是密集文字。Round 13 曾声称修复但 R14 发现回归。\n\n**W-SF7. Limitations 格式不满足 CoRL 要求** [R3]\nLimitations 仍是 Discussion 的 `\\paragraph`，而非独立 section。\n\n**W-SF8. 层编号 off-by-one** [R3——回归问题]\nmethod.tex: \"L1--L31 the 32 transformer layers\"——31 个索引 ≠ 32 层。\n\n**W-SF9. 术语不一致** [R1, R2, R3 三方独立发现]\nreadout token / last_preaction；instruction-dominant heads / dominant heads / instruction heads 混用。\n\n---\n\n## Reviewer Consensus（三方共识）\n\n1. **CoRL scope 是首要问题** — 三位审稿人均认为纯分析性论文缺乏 robotics 应用验证是最大短板\n2. **\"Convergent\" 声称过强** — N=2 同质架构 + N_eff=10 的统计基础不足\n3. **方法论框架本身有价值** — 三角验证方法论和 readout token 发现是实质贡献\n4. **附录质量高** — 鲁棒性检验详尽，可复现性好\n5. **需补充参考文献** — 多领域引用缺失；多条 arXiv 引用需更新\n6. **闭环验证缺失** — 三方一致认为至少应验证一个 actionable implication\n\n## Reviewer Divergence（分歧点）\n\n| 议题 | R1 | R2 | R3 | 解决状态 |\n|------|----|----|----|----|\n| Finding 3 trivial? | Non-trivial（三层区分） | 初 trivial → 接受 R1 | Nuanced（需声明 token ordering） | ✅ 基本解决 |\n| Cohen's d 偏差方向 | 可能高估 | paired d_z > standard d（保守） | Token 相关性高估 | ⚠️ 方向未解决，共识报告配对版 |\n| MLP probe capacity | 过大（1.05M params） | 未强调 | 已充分回应（Appendix A.6） | ✅ R3 有力反驳 |\n\n---\n\n## Questions for Authors\n\n1. L1 的 24/32 instruction-dominant heads 中，是否有 head 在 pretrained Llama-2 中已存在 instruction sensitivity？Fine-tuning 是 amplifying 还是 creating？\n2. Δ=0.003 的 TOST 等价性检验（ε=0.05）的 p 值是多少？\n3. 是否考虑过在训练中间 checkpoint 上测量 L1 head count 的演化曲线？\n4. Readout token 的 R²=0.678——剩余 32.2% 的方差来源是什么？\n5. Ablation 后 MSE 几乎不变（0.498→0.497），但 trajectory divergence d>0.6。如何 reconcile？\n6. OpenVLA 的 token ordering 是什么？Image tokens 在 instruction tokens 之前还是之后？[R3 提出]\n\n---\n\n## Missing References\n\n**高优先级**：Aghajanyan et al. (ACL 2021), Kumar et al. (NeurIPS 2022), \"What Do Visual Tokens Really Encode?\" (arXiv:2603.00510)\n**中优先级**：TinyVLA/ECoT, diffusion VLA 表征分析, VLA scaling laws\n**引用版本更新**（6 条）：kim2024_openvla, karamcheti2024, touvron2023_llama2, belrose2023_tunedlens, padalkar2023_oxe, black2024_pi0\n\n---\n\n## External Review\n\n**外部审稿（Stanford Agentic Reviewer）：pending，未返回。**\n\n---\n\n## Visual Layout Check（非评分项）\n\n- **Critical (1)**：Page 31 约 90% 空白\n- **Warnings (4)**：Pages 2-4 无图表；Page 16 标签字号小；Pages 21, 30 表格密集\n- **Info (21)**：次要排版观察\n\nR3 的独立审查与视觉 Agent 发现一致。\n\n---\n\n## Overall Assessment\n\n**Overall Score: 5.3/10 → Weak Reject**\n\n| Reviewer | 侧重 | 初始分 | 最终分 | 变化原因 |\n|----------|------|--------|--------|----------|\n| R1 | 方法/实验严谨性 | 6/10 | 6/10 | 无变化 |\n| R2 | 新颖性/scope/完整性 | 4/10 | 5/10 | 接受 R1 对 Finding 3 和 effect size 的反驳 |\n| R3 | 写作/格式/可复现性 | 5/10 | 5/10 | 无变化 |\n\n**R3 官方维度打分**：Significance 6/10, Relevance to Robotics 5/10, Soundness 7/10, Clarity 4/10, Reproducibility 7/10\n\n**核心判断**：方法论框架和 readout token 发现是实质贡献，但五个结构性问题使其不适合当前形式投稿 CoRL：(1) 纯分析无闭环验证；(2) convergent claim 统计基础不足；(3) 超页限（desk rejection 风险）；(4) 可读性差（Clarity 4/10）；(5) LIBERO 单一 benchmark。\n\n**特别警告**：R12-N2（超页限）和 R12-N3（信息过载）在 Round 13 曾被标记为 resolved，但 Round 14 fresh review 发现回归。Research Director 需验证修复生效。\n\n**建议路径**：\n- **若坚持 CoRL**（仅剩 9 天）：紧急压缩至 8 页 + 精简 Abstract/Intro + 补充 L1 entropy 验证（低成本）+ 弱化 convergent + 修复格式回归\n- **若转投**：ICML/NeurIPS interpretability track 或 CoRL Workshop\n\n---\n\n## Detailed Comments\n\n### 正文修改（按优先级排序）\n\n1. 压缩正文至 8 页：Discussion Mechanistic interpretation + Functional stages 移至 Appendix\n2. Abstract 删除至少 10 个定量数字，只保留核心 1-2 个\n3. Introduction 删除与 Abstract 重复的量化描述\n4. \"convergent reorganization\" → \"consistent reorganization pattern\"\n5. \"orthogonal contribution\" → \"complementary and necessary next step\"\n6. Limitations 提升为独立 section\n7. 层编号 off-by-one 修复\n8. 术语统一（readout token / instruction-dominant heads）\n9. Figure 1 确保在 page 1\n10. Token ordering 明确声明\n\n### 统计方法\n\n11. 报告 paired Cohen's d_z 和配对相关系数 r\n12. 对 Δ=0.003 做 TOST 等价性检验\n13. Power analysis（N=10 最小可检测效应量）\n14. Permutation test 增加到 ≥10,000 shuffles\n\n### 引用和格式\n\n15. 新增引用：Aghajanyan 2021, Kumar 2022\n16. 更新 6 条 arXiv → published\n17. GenAI disclosure 移至 Appendix\n18. Table 2 caption 展开缩写\n19. Page 31 空白处理",
    "project": "vla-ssd",
    "reviewer_ids_acknowledged": "[1, 2, 3]",
    "cross_response_reviewer_ids": "[1, 2, 3]",
    "overall_score": "weak reject",
    "review_chat_id": "oc_554a5023cde4d603635cf97e6ab8151a",
    "force_resubmit": "True"
  }
}
```

</details>

---


### Tool result

_source line 1186 · 2026-05-20T17:07:01.745120+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_a1d032cbe70bdd2058438e67e0d57613:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4068
}
```

</details>

---


### Assistant

_source line 1187 · 2026-05-20T17:07:10.152557+00:00_

审稿报告已投递至 Research Director。

**Round 14 审稿完成**：

- **三位 Reviewer**：R1 (6/10), R2 (5/10), R3 (5/10)，均值 5.3/10 → **Weak Reject**
- **5 个 Must-Fix**：CoRL scope（三方共识首要问题）、convergent claim 过强、N_eff=10 统计效力、超页限（8.7页，回归）、信息过载（回归）
- **9 个 Should-Fix**：Cohen's d 公式、LIBERO-only、缺失引用、单 checkpoint、Finding 3 定位、Figure 1 位置、Limitations 格式、层编号、术语不一致
- **Issue tracker** 已更新至 62 条（含 R3 的 5 个新 issue + 4 个回归 issue 重开）
- **外部审稿**：pending 未返回
- **视觉审查**：已完成，1 critical + 4 warnings

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director"
}
```

</details>

---


## Round 110

## Round 110

58 recorded events


### User

_source line 1188 · 2026-05-22T13:33:44.203669+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: vla-ssd
- 论文路径: /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/main.tex
- 目标 venue: CoRL 2026
- 截止日期: 2026-05-29
- **引用验证**: ❌ 未启用

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 1189 · 2026-05-22T13:33:52.683249+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 1190 · 2026-05-22T13:33:52.734225+00:00_

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
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1191 · 2026-05-22T13:33:59.761894+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,read_project_file,dispatch_visual_check,request_external_review,director_post_to_reviewer,submit_review_report_to_research_director,update_review_issues,get_external_review_status,get_visual_check_status,WebSearch",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_get_project_overview,read_project_file,dispatch_visual_check,request_external_review,director_post_to_reviewer,submit_review_report_to_research_director,update_review_issues,get_external_review_status,get_visual_check_status,WebSearch",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 1192 · 2026-05-22T13:33:59.812534+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1193 · 2026-05-22T13:34:05.894479+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,read_project_file,dispatch_visual_check,request_external_review,director_post_to_reviewer,submit_review_report_to_research_director,update_review_issues,get_external_review_status,get_visual_check_status",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_get_project_overview,read_project_file,dispatch_visual_check,request_external_review,director_post_to_reviewer,submit_review_report_to_research_director,update_review_issues,get_external_review_status,get_visual_check_status",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 1194 · 2026-05-22T13:34:05.917987+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "ToolSearch",
  "elapsed_ms": 23
}
```

</details>

---


### Tool call

_source line 1195 · 2026-05-22T13:34:12.355460+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 1196 · 2026-05-22T13:34:12.407365+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "ToolSearch",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 1197 · 2026-05-22T13:34:16.087895+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "vla-ssd"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "vla-ssd"
  }
}
```

</details>

---


### Tool result

_source line 1198 · 2026-05-22T13:34:17.447147+00:00_

{"result":"# 项目 vla-ssd 概况\n\n## 实验状态 (147 个)\n\n- **lg_extract_untrained_r2**: DONE (killed) — \n- **lg_extract_trained_r2**: DONE (killed) — \n- **lg_extract_untrained_r1**: DONE (killed) — \n- **lg_extract_trained_r1**: DONE (killed) — \n- **mvp2_delta_dino**: DONE (success) — \n- **mvp2_delta_untrained**: DONE (success) — \n- **mvp2_delta_trained**: DONE (success) — \n- **mvp2_action_dino**: DONE (success) — \n- **mvp2_action_untrained**: DONE (success) — \n- **mvp2_action_trained**: DONE (success) — \n- **mvp_controlb_untrained**: DONE (success) — \n- **mvp_controlb_trained**: DONE (success) — \n- **mvp_001**: DONE (negative) — \n- **mvp_probe_untrained**: DONE (success) — \n- **mvp_probe_trained**: DONE (negative) — \n\n## 最新报告\n# Handover — 2026-05-22\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n- tracvla_spatial_full_v2: TraceVLA (Phi-3-mini) on LIBERO-Spatial shows the convergent entry-exit routing pattern when fine-tuned, and the untrained base model (Phi-3-Vision) lacks this pattern. Cross-suite validation for second architecture.（已分配 ? GPU:?，等待提交）\n- behavioral_smoketest_diag（准备中）\n- behavioral_pilot_v2: Ablating L1 instruction-dominant heads (24/32) during VLA inference on LIBERO-Goal fine-tuned OpenVLA reduces task success rate, providing behavioral evidence that attention head specialization has functional consequences for task execution.（准备中）\n- behavioral_pilot: Ablating L1 instruction-dominant heads during VLA inference will measurably change task success rate, providing behavioral evidence that these heads serve a functional role beyond representational reorganization measured by probes.（准备中）\n- tracvla_spatial_trained（准备中）\n- libero_finetuned_probe（准备中）\n- fulllayer_action_probe（准备中）\n- l1_head_ablation_control8（准备中）\n- l1_head_ablation_50demos（准备中）\n\n## 近期结论\n- **nlp_finetuning_control_v1** (success): NLP-finetuned Llama-2-7b-chat (text-only SFT, no action head) will NOT exhibit R² exit collapse because it lacks visuomotor gr
…[truncated 1790 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 1359
}
```

</details>

---


### Tool call

_source line 1199 · 2026-05-22T13:34:17.598165+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 1200 · 2026-05-22T13:34:17.951174+00:00_

1	\documentclass{article}
2	
3	\usepackage{corl_2026}
4	
5	\usepackage[utf8]{inputenc}
6	\usepackage[T1]{fontenc}
7	\usepackage{url}
8	\usepackage{booktabs}
9	\usepackage{amsfonts}
10	\usepackage{amsmath}
11	\usepackage{nicefrac}
12	\usepackage[expansion=false]{microtype}
13	\usepackage{graphicx}
14	\usepackage{enumitem}
15	
16	\setlength{\textfloatsep}{6pt plus 1pt minus 3pt}
17	\setlength{\intextsep}{6pt plus 1pt minus 1pt}
18	\setlength{\floatsep}{6pt plus 1pt minus 3pt}
19	\setlength{\abovecaptionskip}{2pt}
20	\setlength{\belowcaptionskip}{0pt}
21	\setlength{\abovedisplayskip}{6pt plus 2pt minus 2pt}
22	\setlength{\belowdisplayskip}{6pt plus 2pt minus 2pt}
23	
24	\title{Three Architectures, One Routing Pattern:\\ How VLA Fine-Tuning Reshapes Instruction Flow}
25	
26	\author{Anonymous}
27	
28	\begin{document}
29	
30	\maketitle
31	
32	\begin{abstract}
33	\input{abstract}
34	\end{abstract}
35	
36	\keywords{Vision-Language-Action models, representational analysis, attention routing, fine-tuning}
37	
38	\input{introduction}
39	\input{related_work}
40	\input{method}
41	\input{experiments}
42	\input{discussion}
43	\input{conclusion}
44	
45	\bibliography{references}
46	
47	\input{appendix}
48	
49	\end{document}
50	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Read",
  "elapsed_ms": 353
}
```

</details>

---


### Tool call

_source line 1201 · 2026-05-22T13:34:17.951525+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "CoRL 2026 call for papers submission deadline author guidelines"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "CoRL 2026 call for papers submission deadline author guidelines"
  }
}
```

</details>

---


### Tool call

_source line 1202 · 2026-05-22T13:34:19.457201+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/review_round_15/submitted.pdf 2>/dev/null && echo \"PDF_EXISTS\" || echo \"NO_PDF\"",
  "description": "Check if submitted PDF exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/review_round_15/submitted.pdf 2>/dev/null && echo \"PDF_EXISTS\" || echo \"NO_PDF\"",
    "description": "Check if submitted PDF exists"
  }
}
```

</details>

---


### Tool result

_source line 1203 · 2026-05-22T13:34:19.858866+00:00_

-rw-r--r-- 1 ubuntu ubuntu 695903 May 22 13:32 /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/review_round_15/submitted.pdf
PDF_EXISTS

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Bash",
  "elapsed_ms": 401
}
```

</details>

---


### Tool call

_source line 1204 · 2026-05-22T13:34:19.911103+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/review_issues.yaml 2>/dev/null || echo \"NO_ISSUES_FILE\"",
  "description": "Check existing review issues tracker"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/review_issues.yaml 2>/dev/null || echo \"NO_ISSUES_FILE\"",
    "description": "Check existing review issues tracker"
  }
}
```

</details>

---


### Tool result

_source line 1205 · 2026-05-22T13:34:19.962123+00:00_

&lt;persisted-output>
Output too large (29.3KB). Full output saved to: /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-15-projects-vla-ssd--claude-sessions-review-director-ae8c68a6/42ed2fc5-87c5-4544-bc6c-c6db2f32061c/tool-results/biso4m88o.txt

Preview (first 2KB):
issues:
- id: R1-N1-old
  summary: "Untrained baseline 无法隔离 VLA fine-tuning vs Llama-2 语言预训练的贡献"
  category: experiment
  severity: critical
  status: resolved
  first_raised_round: 1
  last_seen_round: 2
  resolution: "三条件数据完整整合。"
  resolution_round: 3
  mentions: []
  action_items: []
- id: R1-N2-old
  summary: "单一模型 Title/Abstract 使用复数 'VLAs' 构成 overclaim"
  category: framing
  severity: critical
  status: resolved
  first_raised_round: 1
  last_seen_round: 2
  resolution: "Title 改为单数。"
  resolution_round: 3
  mentions: []
  action_items: []
- id: R1-N4-old
  summary: "Design implications 完全基于 correlational evidence"
  category: framing
  severity: critical
  status: resolved
  first_raised_round: 1
  last_seen_round: 2
  resolution: "Abstract 使用 hedge 语气。"
  resolution_round: 3
  mentions: []
  action_items: []
- id: R1-N3-old
  summary: "RSA best-vs-best selection bias"
  category: experiment
  severity: warning
  status: resolved
  first_raised_round: 1
  last_seen_round: 2
  resolution: "Same-layer comparison 为 primary evidence。"
  resolution_round: 3
  mentions: []
  action_items: []
- id: R2-N1-old
  summary: "Neo et al. (ICLR 2025) 未引用"
  category: framing
  severity: warning
  status: resolved
  first_raised_round: 1
  last_seen_round: 2
  resolution: "已引用。"
  resolution_round: 3
  mentions: []
  action_items: []
- id: R2-W1-old
  summary: "Related Work 引用覆盖度不足"
  category: writing
  severity: warning
  status: resolved
  first_raised_round: 1
  last_seen_round: 2
  resolution: "引用数量达标。"
  resolution_round: 3
  mentions: []
  action_items: []
- id: R1-W1-old
  summary: "'Instruction-blind' claim 过强"
  category: framing
  severity: warning
  status: resolved
 
…[truncated 310 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Bash",
  "elapsed_ms": 51
}
```

</details>

---


### Tool result

_source line 1206 · 2026-05-22T13:34:27.543171+00:00_

Web search results for query: "CoRL 2026 call for papers submission deadline author guidelines"

Links: [{"title":"CoRL 2026 - Instruction for Authors","url":"https://www.corl.org/contributions/instruction-for-authors"},{"title":"CoRL 2026 - Call for Papers","url":"https://www.corl.org/contributions/call-for-papers"},{"title":"CoRL 2026 - Annoucements","url":"https://www.corl.org/annoucements"},{"title":"CoRL 2026","url":"https://www.corl.org/"},{"title":"CoRL 2026 - Call for Workshops","url":"https://www.corl.org/contributions/call-for-workshops"},{"title":"Update CoRL 2026 conference details · huggingface/ai-deadlines at 0ba012a","url":"https://huggingface.co/spaces/huggingface/ai-deadlines/commit/0ba012abbc2f4e96e0072f99fd68649bfc69d9cf"},{"title":"CoRL 2026 Conference | OpenReview","url":"https://openreview.net/group?id=robot-learning.org%2FCoRL%2F2026%2FConference"},{"title":"Robot Learning Foundation","url":"https://www.robot-learning.org/"},{"title":"Refactor conference data · huggingface/ai-deadlines at f3cc2d7","url":"https://huggingface.co/spaces/huggingface/ai-deadlines/commit/f3cc2d74f8283ae00d3005ff7cca51dd26540377"},{"title":"CoRL 2026 - Contributions","url":"https://www.corl.org/contributions"}]

Based on the search results, here's the key information about CoRL 2026's submission deadlines and author guidelines:

## Submission Deadlines

The abstract submission deadline is May 26, 2026 11:59 UTC, and the paper submission deadline is May 29, 2026 11:59 UTC.

## Author Guidelines

**Format and Length:**
The page limit is 8 pages for the main paper, with Acknowledgments, References, and Appendix (optional) not counting towards the page limit.

**Required Content:**
All submissions should include a Limitations section (counted toward the 8-page limit), explicitly describing limiting assumptions, failure modes, and other limitations of the results and experiments.

**Reciprocal Review Requirement:**
Every author with 3 or more submissions must agree to ser
…[truncated 759 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "WebSearch",
  "elapsed_ms": 9591
}
```

</details>

---


### Tool call

_source line 1207 · 2026-05-22T13:34:35.021506+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 1208 · 2026-05-22T13:34:35.021902+00:00_

1	Vision-language-action models (VLAs) convert pretrained vision-language backbones into robot controllers through fine-tuning, yet whether the resulting representational changes reflect general training dynamics or architecture-specific artifacts remains unknown.
2	We conduct a systematic cross-architecture analysis of three VLAs built on distinct backbones (Llama-2-7B, Phi-3-mini, Qwen2.5-VL-3B) across four LIBERO task suites, comparing trained and untrained checkpoints with cross-instruction probes, attention profiling, $R^2$ action probes, and counterfactual instruction perturbation.
3	We identify two training effects that generalize across architectures.
4	First, $R^2$ exit collapse, where action-relevant information is selectively discarded at exit layers, consistently emerges when vision-language models are first fine-tuned into VLAs (6/6 cells across two architectures) and re-emerges for spatially demanding tasks when already-pretrained VLAs undergo further specialization (2/4 cells), suggesting that exit-layer reorganization scales with the representational distance between pretraining and target tasks; a chat-finetuned control using the same backbone shows no exit collapse ($\Delta R^2 \approx 0$), confirming this reorganization is specific to action-oriented training.
5	Second, all trained VLAs exhibit substantial counterfactual sensitivity to instruction perturbation (Cohen's $d \geq 0.45$ across two architectures and eight suite combinations), though metric incomparability between trained (action MSE) and untrained (cosine distance) conditions precludes quantifying the trained--untrained gap as a single amplification factor.
6	In contrast, early-layer instruction-dominant attention patterns trace to base-model priors rather than VLA training; one backbone exhibits saturated instruction attention even before fine-tuning.
7	Together, these findings distinguish training-induced routing effects (exit collapse, counterfactual sensitivity) from inherited base
…[truncated 273 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1209 · 2026-05-22T13:34:35.893080+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 1210 · 2026-05-22T13:34:36.144471+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	Vision-language-action models (VLAs) fine-tune pretrained language models on robot demonstrations to produce actions from visual observations and language instructions~\cite{brohan2023_rt2,kim2024_openvla}.
5	In these decoder-only architectures, image tokens precede instruction tokens in the input sequence, and the causal attention mask prevents image tokens from attending to any token that follows them~\cite{wang2025seeing,pei2025rethinking}.
6	Instruction information can reach action-generating positions only through later attention layers, where the readout token (the final position before action decoding) integrates context from all preceding tokens.
7	The readout is thus the sole multimodal integration point by construction.
8	How fine-tuning creates or reshapes the attention patterns at this position, and whether the resulting routing reflects training dynamics or inherited backbone structure, remains unknown.
9	
10	Behavioral studies provide indirect evidence that this question matters.
11	VLAs exhibit visual dominance, relying disproportionately on image input~\cite{grant2026}, and language instructions appear largely unused by the action pathway~\cite{haon2025}.
12	These observations establish that VLAs underweight instructions but do not explain \emph{how} instruction information reaches action-generating positions, \emph{what} routing structure training creates versus what it inherits from the pretrained backbone, or \emph{whether} observed patterns hold across architectures.
13	All existing representational analyses of VLAs target a single architecture.
14	No prior work tests whether instruction routing mechanisms are consistent across backbone families, and none decomposes training-induced effects from inherited base-model priors.
15	Absent cross-architecture evidence, it is impossible to distinguish training dynamics that reflect the causal-decoder structure from architecture-specific artifacts o
…[truncated 3420 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Read",
  "elapsed_ms": 251
}
```

</details>

---


### Tool call

_source line 1211 · 2026-05-22T13:34:36.195111+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 1212 · 2026-05-22T13:34:36.597141+00:00_

1	\section{Related Work}\label{sec:related_work}
2	
3	\paragraph{Vision-language-action models.}
4	VLAs fine-tune large language models on robot demonstrations to produce actions from visual and language input~\cite{brohan2023_rt2,kim2024_openvla,karamcheti2024,black2024_pi0,zheng2024tracevla,hung2025nora,xiao2025ava}.
5	NLP instruction tuning is well-characterized behaviorally~\cite{wei2022finetuned,ouyang2022training}, but the representational effects of VLA fine-tuning remain unexamined.
6	Fine-tuning operates in a low intrinsic dimension~\cite{aghajanyan2021intrinsic} and can distort pretrained features~\cite{kumar2022finetuning}; existing analyses target single architectures and cannot separate training dynamics from backbone artifacts.
7	
8	\paragraph{Mechanistic and behavioral analysis.}
9	Mechanistic interpretability has revealed residual stream communication~\cite{elhage2021}, induction heads~\cite{olsson2022}, and task circuits~\cite{wang2023_ioi,conmy2023}; causal tracing localizes factual recall~\cite{meng2022_rome}; attention probing shows heads encode syntactic relations~\cite{clark2019} and most can be pruned~\cite{michel2019sixteen}.
10	In VLMs, recent work characterizes visual token redundancy~\cite{fan2026visual} and progressive visual-textual alignment~\cite{neo2025interpreting,long2026understanding}.
11	Behavioral evaluations of VLAs reveal visual dominance~\cite{grant2026,hou2026,fei2025}; mechanistic studies identify sparse semantic directions~\cite{haon2025}, interpretable features~\cite{swann2026,buurmeijer2026}, symbolic representations~\cite{lu2025,molinari2025}, and reasoning erosion~\cite{fang2025}.
12	All prior representational analyses target a single architecture; our $3 \times 4$ cross-architecture matrix tests whether mechanisms replicate across backbone families.
13	
14	\paragraph{Probing and similarity methodology.}
15	RSA~\cite{kriegeskorte2008}, CKA~\cite{kornblith2019}, and linear probes~\cite{alain2017,belinkov2022} provide com
…[truncated 303 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Read",
  "elapsed_ms": 402
}
```

</details>

---


### Tool call

_source line 1213 · 2026-05-22T13:34:36.597600+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 1214 · 2026-05-22T13:34:37.060063+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	We investigate how action-relevant representations are organized across three VLA architectures using complementary probing, attention, and perturbation analyses.
5	
6	%------------------------------------------------------------------
7	\subsection{Architectures and Data}
8	\label{sec:arch_data}
9	
10	We study three VLAs that span distinct backbone families (Table~\ref{tab:arch_overview}).
11	\textbf{OpenVLA}~\cite{kim2024_openvla,karamcheti2024} chains a frozen DinoSigLIP vision backbone~\cite{zhai2023_siglip,oquab2024_dinov2} (DINOv2 ViT-L/14 + SigLIP-SO400M), an MLP projector, and Llama-2-7B~\cite{touvron2023_llama2} (6.74B parameters, 32 layers, 32 multi-head attention [MHA] heads) for autoregressive 7-D action decoding.
12	It is pretrained on Open X-Embodiment~\cite{padalkar2023_oxe} (OXE; 970K episodes across multiple robot platforms).
13	\textbf{TracVLA}~\cite{zheng2024tracevla} pairs a SigLIP encoder with Phi-3-mini~\cite{abdin2024phi3} (3.8B parameters, 32 layers, 32 MHA heads).
14	Spatial trace conditioning renders visual trajectory overlays on input images to provide spatial guidance for action prediction.
15	TracVLA is trained on an OXE subset.
16	\textbf{NORA}~\cite{hung2025nora} uses Qwen2.5-VL-3B ($\sim$3B parameters, 36 layers, grouped-query attention [GQA] with 16 query heads and 2 KV heads) with the native Qwen2.5-VL vision encoder, which processes images at dynamic resolution without a separate projection stage.
17	
18	Each architecture is evaluated in trained and untrained conditions.
19	A critical asymmetry distinguishes the untrained baselines: OpenVLA's untrained checkpoint is the OXE-pretrained VLA, already fine-tuned for action prediction on 970K episodes, while TracVLA and NORA untrained checkpoints are pure vision-language models (Phi-3-Vision and Qwen2.5-VL) with no action training.
20	OpenVLA trained-vs-untrained comparisons therefore measure a VLA-to-VLA transition; TracVLA and NORA comparis
…[truncated 5332 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Read",
  "elapsed_ms": 462
}
```

</details>

---


### Tool call

_source line 1215 · 2026-05-22T13:34:37.060453+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 1216 · 2026-05-22T13:34:37.572330+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Experimental Setup}
5	\label{sec:setup}
6	
7	We analyze three VLA architectures across four LIBERO~\cite{liu2023_libero} task suites (Goal, Spatial, Object, Long-Horizon) in a $3 \times 4$ cross-architecture matrix (Table~\ref{tab:cross_arch_matrix}).
8	The architectures span distinct backbone families: OpenVLA~\cite{kim2024_openvla,karamcheti2024} (Llama-2-7B~\cite{touvron2023_llama2}, 32 layers, 32 MHA heads), TracVLA~\cite{zheng2024tracevla} (Phi-3-mini~\cite{abdin2024phi3}, 32 layers, 32 heads), and NORA~\cite{hung2025nora} (Qwen2.5-VL-3B, 36 layers, GQA with 16 query heads and 2 KV heads).
9	Of the 12 matrix cells, 10 are filled; NORA Object and Long-Horizon lack available checkpoints.
10	Each architecture is compared in trained and untrained conditions, with a critical asymmetry between untrained baselines: OpenVLA's untrained checkpoint is the OXE-pretrained~\cite{padalkar2023_oxe} VLA (already fine-tuned for action prediction on 970K episodes), while TracVLA and NORA untrained checkpoints are pure vision-language models (Phi-3-Vision and Qwen2.5-VL) with no action training.
11	Three analyses are applied to each cell (\S\ref{sec:method}): $R^2$ action probes at all layers, L1 attention head profiling for instruction dominance, and counterfactual instruction perturbation.
12	For OpenVLA LIBERO-Goal, $N = 63{,}228$ observations; other cells are at comparable scale.
13	For trained models that produce action outputs, counterfactual sensitivity is measured via Cohen's $d$ on action MSE.
14	For untrained VLMs (Phi-3-Vision, Qwen2.5-VL) that do not produce actions, sensitivity is measured via cosine distance on hidden representations; these metrics operate on different scales and are not directly comparable (\S\ref{sec:cf_sensitivity}).
15	OpenVLA's OXE-pretrained checkpoint produces actions, permitting same-metric (Cohen's $d$) comparison in that condition.
16	Bonferroni correction details appear in
…[truncated 10781 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Read",
  "elapsed_ms": 511
}
```

</details>

---


### Tool call

_source line 1217 · 2026-05-22T13:34:37.572834+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 1218 · 2026-05-22T13:34:38.028795+00:00_

1	\vspace{-2pt}
2	\section{Discussion}
3	\label{sec:discussion}
4	
5	\paragraph{Synthesis.}
6	VLA fine-tuning produces two training-induced representational changes---$R^2$ exit collapse and counterfactual sensitivity---that concentrate at the readout token (training shifts readout $R^2$ by $+0.069$ vs.\ image\_mean by $+0.015$).
7	L1 instruction attention is inherited from base-model pretraining (Phi-3-Vision: 32/32, Qwen2.5-VL: 13--14/16 before training).
8	The NLP control (Llama-2-7b-chat, $\Delta R^2 = 0.000$) confirms exit collapse is specific to action-oriented training.
9	VLA fine-tuning does not build instruction routing from scratch; it reorganizes downstream representations while preserving early-layer attention structure.
10	
11	\paragraph{Cross-architecture consistency and behavioral relevance.}
12	Two VLM-to-VLA transitions converge on the same training-induced effects (6/6 cells, $p = 0.016$), compatible with task-structure constraints of causal-decoder VLA design.
13	OpenVLA confirms in a task-dependent manner under VLA-to-VLA conditions (2/4 cells).
14	The cross-architecture matrix suggests a three-tier gradient (VLM $\to$ general VLA $\to$ task-specific VLA), but Tier~2 contains only one architecture ($n = 1$), limiting this to an observational synthesis (Appendix~\ref{sec:extended_discussion_appendix}).
15	Correlating trained $\Delta R^2$ with LIBERO success rates yields a positive but non-significant trend ($\rho = 0.583$, $p = 0.10$, $n = 9$); within-suite comparisons are uniformly positive but sample size limits statistical power (Appendix~\ref{sec:extended_discussion_appendix}).
16	
17	\paragraph{Limitations.}
18	Cross-architecture evidence rests on two VLM-to-VLA transitions; OpenVLA tests a different transition type.
19	All experiments use LIBERO; benchmarks with richer language grounding (CALVIN, Language-Table) are needed.
20	We analyze only causal-decoder VLAs; flow-matching~\cite{black2024_pi0} and diffusion~\cite{ghosh2024_octo} architec
…[truncated 210 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Read",
  "elapsed_ms": 455
}
```

</details>

---


### Tool call

_source line 1219 · 2026-05-22T13:34:38.029234+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 1220 · 2026-05-22T13:34:38.029499+00:00_

1	\paragraph{Conclusion.}
2	We analyzed three VLA architectures (OpenVLA, TracVLA, NORA) across four LIBERO task suites, comparing trained and untrained checkpoints to decompose VLA fine-tuning into training-induced and inherited representational effects.
3	Two training-induced effects are consistent across two VLM-to-VLA transitions: $R^2$ exit collapse, where action-relevant information encoded at intermediate layers is selectively discarded at exit layers (6/6 cells, sign test $p = 0.016$), and counterfactual sensitivity, where all trained models respond to instruction perturbation (Cohen's $d \geq 0.45$ across eight tested cells).
4	Exit collapse universally marks the VLM-to-VLA transition and re-emerges for spatially demanding tasks under VLA-to-VLA conditions (2/4 cells), suggesting that exit-layer reorganization scales with the representational distance between pretraining and target tasks; an NLP finetuning control on the same backbone ($\Delta R^2 = 0.000$) confirms this effect is specific to action-oriented training.
5	In contrast, L1 instruction-dominant attention is inherited from base-model pretraining: one backbone (Phi-3-Vision) saturates at 32/32 heads before any action training.
6	Metric incomparability between trained (action MSE) and untrained (cosine distance) conditions precludes quantifying counterfactual amplification factors, and the task-dependent nature of VLA-to-VLA collapse (2/4 OpenVLA suites) indicates that exit reorganization is modulated by pretraining-target distance rather than being universally triggered by further fine-tuning.
7	Extending this framework to flow-matching and diffusion VLAs with cross-attention, to benchmarks with richer language grounding, and to intermediate training checkpoints are priorities for future work.
8	Code and data will be released upon acceptance.
9	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1221 · 2026-05-22T13:34:38.783417+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/appendix.tex"
  }
}
```

</details>

---


### Tool call

_source line 1222 · 2026-05-22T13:34:38.984951+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/references.bib"
  }
}
```

</details>

---


### Tool result

_source line 1223 · 2026-05-22T13:34:39.036014+00:00_

1	% === VLA / Architecture ===
2	
3	@article{hung2025nora,
4	  title     = {{NORA}: A Small Open-Sourced Generalist Vision Language Action Model for Embodied Tasks},
5	  author    = {Hung, Chia-Yu and Sun, Qi and Hong, Pengfei and Zadeh, Amir and Li, Chuan and Tan, U-Xuan and Majumder, Navonil and Poria, Soujanya},
6	  journal   = {arXiv preprint arXiv:2504.19854},
7	  year      = {2025},
8	}
9	
10	@article{zheng2024tracevla,
11	  title     = {{TraceVLA}: Visual Trace Prompting Enhances Spatial-Temporal Awareness for Generalist Robotic Policies},
12	  author    = {Zheng, Ruijie and Liang, Yongyuan and Huang, Shuaiyi and Gao, Jianfeng and Daum{\'e} III, Hal and Kolobov, Andrey and Huang, Furong and Yang, Jianwei},
13	  journal   = {arXiv preprint arXiv:2412.10345},
14	  year      = {2024},
15	}
16	
17	@article{abdin2024phi3,
18	  title     = {Phi-3 Technical Report: A Highly Capable Language Model Locally on Your Phone},
19	  author    = {Abdin, Marah and Jacobs, Sam Ade and Amin, Ammar Ahmad and Aneja, Jyoti and Awadalla, Ahmed and Awadalla, Hany and Bach, Nguyen and Bahree, Amit and Bakber, Arash and Beez, Harkirat and others},
20	  journal   = {arXiv preprint arXiv:2404.14219},
21	  year      = {2024},
22	}
23	
24	@inproceedings{kim2024_openvla,
25	  title     = {{OpenVLA}: An Open-Source Vision-Language-Action Model},
26	  author    = {Kim, Moo Jin and Pertsch, Karl and Karamcheti, Siddharth and Xiao, Ted and Balakrishna, Ashwin and Nair, Suraj and Rafailov, Rafael and Foster, Ethan and Lam, Grace and Sanketi, Pannag and Lu, Quan and Kollar, Thomas and Burchfiel, Benjamin and Tedrake, Russ and Sadigh, Dorsa and Levine, Sergey and Liang, Percy and Finn, Chelsea},
27	  booktitle = {Proceedings of the 8th Conference on Robot Learning (CoRL)},
28	  series    = {PMLR},
29	  volume    = {270},
30	  pages     = {2679--2713},
31	  year      = {2024},
32	}
33	
34	@inproceedings{karamcheti2024,
35	  title     = {Prismatic {VLMs}: Investigating the Design Space of Visually-
…[truncated 23990 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool result

_source line 1224 · 2026-05-22T13:34:39.892125+00:00_

File content (26633 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Read",
  "elapsed_ms": 1108
}
```

</details>

---


### Tool call

_source line 1225 · 2026-05-22T13:34:40.043115+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-15-projects-vla-ssd--claude-sessions-review-director-ae8c68a6/42ed2fc5-87c5-4544-bc6c-c6db2f32061c/tool-results/biso4m88o.txt"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-15-projects-vla-ssd--claude-sessions-review-director-ae8c68a6/42ed2fc5-87c5-4544-bc6c-c6db2f32061c/tool-results/biso4m88o.txt"
  }
}
```

</details>

---


### Tool result

_source line 1226 · 2026-05-22T13:34:40.345425+00:00_

1	issues:
2	- id: R1-N1-old
3	  summary: "Untrained baseline 无法隔离 VLA fine-tuning vs Llama-2 语言预训练的贡献"
4	  category: experiment
5	  severity: critical
6	  status: resolved
7	  first_raised_round: 1
8	  last_seen_round: 2
9	  resolution: "三条件数据完整整合。"
10	  resolution_round: 3
11	  mentions: []
12	  action_items: []
13	- id: R1-N2-old
14	  summary: "单一模型 Title/Abstract 使用复数 'VLAs' 构成 overclaim"
15	  category: framing
16	  severity: critical
17	  status: resolved
18	  first_raised_round: 1
19	  last_seen_round: 2
20	  resolution: "Title 改为单数。"
21	  resolution_round: 3
22	  mentions: []
23	  action_items: []
24	- id: R1-N4-old
25	  summary: "Design implications 完全基于 correlational evidence"
26	  category: framing
27	  severity: critical
28	  status: resolved
29	  first_raised_round: 1
30	  last_seen_round: 2
31	  resolution: "Abstract 使用 hedge 语气。"
32	  resolution_round: 3
33	  mentions: []
34	  action_items: []
35	- id: R1-N3-old
36	  summary: "RSA best-vs-best selection bias"
37	  category: experiment
38	  severity: warning
39	  status: resolved
40	  first_raised_round: 1
41	  last_seen_round: 2
42	  resolution: "Same-layer comparison 为 primary evidence。"
43	  resolution_round: 3
44	  mentions: []
45	  action_items: []
46	- id: R2-N1-old
47	  summary: "Neo et al. (ICLR 2025) 未引用"
48	  category: framing
49	  severity: warning
50	  status: resolved
51	  first_raised_round: 1
52	  last_seen_round: 2
53	  resolution: "已引用。"
54	  resolution_round: 3
55	  mentions: []
56	  action_items: []
57	- id: R2-W1-old
58	  summary: "Related Work 引用覆盖度不足"
59	  category: writing
60	  severity: warning
61	  status: resolved
62	  first_raised_round: 1
63	  last_seen_round: 2
64	  resolution: "引用数量达标。"
65	  resolution_round: 3
66	  mentions: []
67	  action_items: []
68	- id: R1-W1-old
69	  summary: "'Instruction-blind' claim 过强"
70	  category: framing
71	  severity: warning
72	  status: resolved
73	  first_raised_round: 1
74	  last_seen_round: 2
75	  resolution: "MLP probe 双重验证。"
76	  resol
…[truncated 27905 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Read",
  "elapsed_ms": 302
}
```

</details>

---


### Tool call

_source line 1227 · 2026-05-22T13:34:59.527440+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "vla-ssd",
  "file": "config",
  "max_chars": "5000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "vla-ssd",
    "file": "config",
    "max_chars": "5000"
  }
}
```

</details>

---


### Tool result

_source line 1228 · 2026-05-22T13:35:00.833336+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"file must be one of ['ARCHITECTURE.md', 'DATA.md', 'EVALUATION.md', 'MODELS.md', 'ROADMAP.md', 'constraints.yaml', 'decisions.yaml', 'ideas.md', 'literature_map.yaml', 'memory.md', 'mistakes.yaml', 'paper_checklist.yaml', 'paper_framing.md', 'paper_provenance.yaml', 'report.md', 'writing_plan.yaml'], got 'config'\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 1305
}
```

</details>

---


### Tool call

_source line 1229 · 2026-05-22T13:35:00.934213+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/appendix.tex",
  "limit": "200"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/appendix.tex",
    "limit": "200"
  }
}
```

</details>

---


### Tool result

_source line 1230 · 2026-05-22T13:35:00.985099+00:00_

1	\paragraph{Use of Generative AI.}
2	Generative AI tools (Claude, GPT-4) assisted with code implementation and manuscript editing; all scientific content was produced by the authors.
3	
4	\appendix
5	
6	\section{Supplementary Material}
7	\label{sec:appendix}
8	
9	Unless noted otherwise, all analyses use OpenVLA-7B (\texttt{openvla/openvla-7b} on HuggingFace) evaluated on LIBERO-Goal (10 tasks $\times$ 50 demonstrations, $N = 63{,}228$ observations after excluding terminal frames).
10	Model conditions, representation extraction, metric definitions, and probe architectures follow \S\ref{sec:method}.
11	Cross-benchmark experiments (\S\ref{sec:cross_benchmark_appendix}) use LIBERO-Spatial with the same protocol (10 tasks $\times$ 50 demonstrations).
12	All experiments ran on 2$\times$ NVIDIA RTX PRO 6000 Blackwell Server Edition GPUs (96\,GB each); random seed is 42 unless stated otherwise.
13	
14	\subsection{OpenVLA-Specific Analysis Methods}
15	\label{sec:openvla_methods_appendix}
16	
17	Three additional analyses are applied to OpenVLA to characterize instruction encoding and representational geometry.
18	
19	\paragraph{Cross-instruction probes.}
20	Each visual frame is paired with all 10 LIBERO-Goal task instructions, producing 10 representation vectors per frame per layer.
21	A 10-way linear classifier identifies which instruction was present, applied separately at image\_mean and readout, with leave-one-out cross-validation (LOOCV) over 10 folds.
22	
23	\paragraph{Representational similarity analysis (RSA).}
24	RSA~\cite{kriegeskorte2008} quantifies geometric alignment between representations and the action space.
25	For each task, we compute pairwise representational dissimilarity matrices (RDMs) using cosine distances for representations and Euclidean distances for 7-D action vectors, from within-task observation pairs across 50 demonstrations.
26	Alignment is measured via Spearman $\rho$ between upper-triangular RDM entries; we report mean $\rho$ across 10 task
…[truncated 16385 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1231 · 2026-05-22T13:35:09.748985+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/agent/config.yaml 2>/dev/null | grep -A5 \"external_review\" || echo \"NO_EXTERNAL_REVIEW_CONFIG\"",
  "description": "Check external review config"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/agent/config.yaml 2>/dev/null | grep -A5 \"external_review\" || echo \"NO_EXTERNAL_REVIEW_CONFIG\"",
    "description": "Check external review config"
  }
}
```

</details>

---


### Tool result

_source line 1232 · 2026-05-22T13:35:09.849862+00:00_

NO_EXTERNAL_REVIEW_CONFIG

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Bash",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 1233 · 2026-05-22T13:35:14.186094+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd -name \"config*\" -o -name \"*.yaml\" 2>/dev/null | head -20",
  "description": "Find config files in project"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd -name \"config*\" -o -name \"*.yaml\" 2>/dev/null | head -20",
    "description": "Find config files in project"
  }
}
```

</details>

---


### Tool result

_source line 1234 · 2026-05-22T13:35:14.286902+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/dream_registry.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/writing_plan.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/paper_provenance.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/literature_map.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/registry.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/constraints.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/mistakes.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/review_issues_updated.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/literature_map.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/dream_reports/dream_20260515T222933/median/review_context.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/dream_reports/dream_20260515T222933/median/imagined_experiments.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/dream_reports/dream_20260515T222933/worst/review_context.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/dream_reports/dream_20260515T222933/worst/imagined_experiments.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/dream_reports/dream_20260515T222933/meta.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/dream_reports/dream_20260515T222933/best/review_context.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/dream_reports/dream_20260515T222933/best/imagined_experiments.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/dream_reports/dream_20260516T011810/median/review_context.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/dream_reports/dream_20260516T01
…[truncated 319 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Bash",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 1235 · 2026-05-22T13:35:19.414993+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -r \"external_review\\|paperreview\" /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/ 2>/dev/null | head -5 || echo \"NOT_FOUND\"",
  "description": "Search for external review config"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -r \"external_review\\|paperreview\" /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/ 2>/dev/null | head -5 || echo \"NOT_FOUND\"",
    "description": "Search for external review config"
  }
}
```

</details>

---


### Tool result

_source line 1236 · 2026-05-22T13:35:19.670008+00:00_

&lt;persisted-output>
Output too large (32.8KB). Full output saved to: /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-15-projects-vla-ssd--claude-sessions-review-director-ae8c68a6/42ed2fc5-87c5-4544-bc6c-c6db2f32061c/tool-results/b2rnqtfpa.txt

Preview (first 2KB):
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/logs/workers/worker_code_sync_figures_local_20260516T081324.log:{"type":"user","message":{"role":"user","content":[{"tool_use_id":"toolu_01W4zCnST2DGLEfExj8NcTxW","type":"tool_result","content":"/home/ubuntu/agent-ml-research/core/__init__.py\n/home/ubuntu/agent-ml-research/core/agents/__init__.py\n/home/ubuntu/agent-ml-research/core/agents/base.py\n/home/ubuntu/agent-ml-research/core/agents/coder.py\n/home/ubuntu/agent-ml-research/core/api/__init__.py\n/home/ubuntu/agent-ml-research/core/agents/sub_agent.py\n/home/ubuntu/agent-ml-research/core/agents/preparing.py\n/home/ubuntu/agent-ml-research/core/agents/spec.py\n/home/ubuntu/agent-ml-research/core/agents/reviewer.py\n/home/ubuntu/agent-ml-research/core/agents/sandbox.py\n/home/ubuntu/agent-ml-research/core/api/routers/__init__.py\n/home/ubuntu/agent-ml-research/core/api/middleware.py\n/home/ubuntu/agent-ml-research/core/api/deps.py\n/home/ubuntu/agent-ml-research/core/api/routers/events.py\n/home/ubuntu/agent-ml-research/core/api/routers/chat.py\n/home/ubuntu/agent-ml-research/core/api/routers/images.py\n/home/ubuntu/agent-ml-research/core/api/routers/files.py\n/home/ubuntu/agent-ml-research/core/api/routers/activity.py\n/home/ubuntu/agent-ml-research/core/api/routers/ideas.py\n/home/ubuntu/agent-ml-research/core/api/routers/experiments.py\n/home/ubuntu/agent-ml-research/core/api/routers/approvals.py\n/home/ubuntu/agent-ml-research/core/api/routers/deployments.py\n/home/ubuntu/agent-ml-research/core/api/routers/crons.py\n/home/ubuntu/agent-ml-research/core/api/routers/health.py\n/home/ubuntu/agent-ml-research/core/api/routers/idea_generator.py\n/home/
…[truncated 326 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "Bash",
  "elapsed_ms": 255
}
```

</details>

---


### Tool call

_source line 1237 · 2026-05-22T13:36:09.937112+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "project": "vla-ssd",
  "text": "你是 Reviewer 1，负责审查 **方法严谨性、统计有效性和实验设计**。\n\n## 论文信息\n- **标题**: \"Three Architectures, One Routing Pattern: How VLA Fine-Tuning Reshapes Instruction Flow\"\n- **Venue**: CoRL 2026（Conference on Robot Learning）\n- **截止日期**: 2026-05-29\n- **格式**: corl_2026 模板，正文 8 页，double-blind\n- **论文路径**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/main.tex`\n- **PDF**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/review_round_15/submitted.pdf`\n\n## 你的审查侧重\n\n**核心任务**：以顶会最严格审稿人标准评估本文的方法论和统计框架。\n\n请重点审查以下方面：\n\n1. **Probe 方法论**:\n   - MLP probe（d_in → 256 → 7）的 capacity 是否过大，是否存在 overfitting 风险\n   - Demo-level train/test split (demos 0-39 vs 40-49) 是否充分防止时序泄漏\n   - R² metric 在 7-D action space 上的适用性\n\n2. **统计检验**:\n   - Sign test (p=0.016, 6/6 cells) 的 power 和适用性\n   - TOST 等价检验的使用是否合理（如论文中有提及）\n   - Paired vs independent Cohen's d 的选择和报告\n   - Bonferroni/FDR 多重比较校正的覆盖范围\n   - Bootstrap 置信区间的方法论\n\n3. **实验设计**:\n   - 3×4 矩阵中 10/12 cells 的 missing data 处理\n   - Trained/untrained 不对称性（OpenVLA: VLA-to-VLA vs TracVLA/NORA: VLM-to-VLA）的方法论影响\n   - Counterfactual 分析中 metric incomparability（Cohen's d vs cosine distance）的处理\n   - L1 attention head classification 的 50% 阈值选择\n   - N=63,228 观测的有效独立单元问题\n\n4. **控制实验**:\n   - NLP control (Llama-2-7b-chat) 作为 specificity evidence 的充分性\n   - Random-weight baseline 的信息量\n   - 单一 training checkpoint 对结论稳健性的影响\n\n请给出：\n- **Strengths**: 方法论优点\n- **Weaknesses**: 方法论缺陷（按严重性排序，标注 Must-Fix / Should-Fix / Minor）\n- **Questions**: 需作者澄清的方法论问题\n- **Overall Assessment**: 方法论总评"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "project": "vla-ssd",
    "text": "你是 Reviewer 1，负责审查 **方法严谨性、统计有效性和实验设计**。\n\n## 论文信息\n- **标题**: \"Three Architectures, One Routing Pattern: How VLA Fine-Tuning Reshapes Instruction Flow\"\n- **Venue**: CoRL 2026（Conference on Robot Learning）\n- **截止日期**: 2026-05-29\n- **格式**: corl_2026 模板，正文 8 页，double-blind\n- **论文路径**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/main.tex`\n- **PDF**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/review_round_15/submitted.pdf`\n\n## 你的审查侧重\n\n**核心任务**：以顶会最严格审稿人标准评估本文的方法论和统计框架。\n\n请重点审查以下方面：\n\n1. **Probe 方法论**:\n   - MLP probe（d_in → 256 → 7）的 capacity 是否过大，是否存在 overfitting 风险\n   - Demo-level train/test split (demos 0-39 vs 40-49) 是否充分防止时序泄漏\n   - R² metric 在 7-D action space 上的适用性\n\n2. **统计检验**:\n   - Sign test (p=0.016, 6/6 cells) 的 power 和适用性\n   - TOST 等价检验的使用是否合理（如论文中有提及）\n   - Paired vs independent Cohen's d 的选择和报告\n   - Bonferroni/FDR 多重比较校正的覆盖范围\n   - Bootstrap 置信区间的方法论\n\n3. **实验设计**:\n   - 3×4 矩阵中 10/12 cells 的 missing data 处理\n   - Trained/untrained 不对称性（OpenVLA: VLA-to-VLA vs TracVLA/NORA: VLM-to-VLA）的方法论影响\n   - Counterfactual 分析中 metric incomparability（Cohen's d vs cosine distance）的处理\n   - L1 attention head classification 的 50% 阈值选择\n   - N=63,228 观测的有效独立单元问题\n\n4. **控制实验**:\n   - NLP control (Llama-2-7b-chat) 作为 specificity evidence 的充分性\n   - Random-weight baseline 的信息量\n   - 单一 training checkpoint 对结论稳健性的影响\n\n请给出：\n- **Strengths**: 方法论优点\n- **Weaknesses**: 方法论缺陷（按严重性排序，标注 Must-Fix / Should-Fix / Minor）\n- **Questions**: 需作者澄清的方法论问题\n- **Overall Assessment**: 方法论总评"
  }
}
```

</details>

---


### Tool result

_source line 1238 · 2026-05-22T13:36:24.656570+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 14719
}
```

</details>

---


### Tool call

_source line 1239 · 2026-05-22T13:36:24.807478+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "project": "vla-ssd",
  "text": "你是 Reviewer 2，负责审查 **新颖性、贡献定位、Related Work 和增量贡献评估**。\n\n## 论文信息\n- **标题**: \"Three Architectures, One Routing Pattern: How VLA Fine-Tuning Reshapes Instruction Flow\"\n- **Venue**: CoRL 2026（Conference on Robot Learning）\n- **截止日期**: 2026-05-29\n- **格式**: corl_2026 模板，正文 8 页，double-blind\n- **论文路径**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/main.tex`\n- **PDF**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/review_round_15/submitted.pdf`\n\n## 你的审查侧重\n\n**核心任务**：以顶会最严格审稿人标准评估本文的新颖性和学术贡献。\n\n请重点审查以下方面：\n\n1. **新颖性评估**:\n   - R² exit collapse 是否为真正的新发现，还是已知现象的重新表述\n   - Cross-architecture 分析（3 models × 4 suites）相比 single-architecture 分析的增量价值\n   - \"Training-induced vs inherited routing\" 分解框架的原创性\n   - Title 声称 \"One Routing Pattern\" 是否被数据支撑（N=2 VLM-to-VLA transitions）\n\n2. **贡献定位**:\n   - 三个贡献是否 well-defined 且与 claims 一致\n   - \"Convergent/consistent reorganization\" 从 N=2 同类架构得出的说服力\n   - 与 Grant et al. (2026)、Häon et al. (2025)、Swann et al. (2026)、Buurmeijer et al. (2026) 的区分是否清晰\n   - 论文是 confirmatory（确认已知现象跨架构成立）还是 discovery（发现新现象）\n\n3. **Related Work 覆盖度**:\n   - VLA mechanistic interpretability 文献是否完整\n   - VLM representational analysis（Neo et al. ICLR 2025, Long et al. ICLR 2026, Fan et al. CVPR 2026）是否充分讨论\n   - Fine-tuning representation theory（Aghajanyan et al. 2021, Kumar et al. 2022）是否引用\n   - 是否有重要遗漏的 2025-2026 相关工作\n\n4. **Claims 与 Evidence 匹配**:\n   - Abstract/Introduction 中的 claims 是否被实验数据支撑\n   - \"Consistent across architectures\" 在 10/12 filled cells 中是否 overclaimed\n   - Counterfactual sensitivity \"d ≥ 0.45\" 的 framing 是否准确\n   - NLP control 单独是否足以支撑 \"VLA-specific\" claim\n\n请给出：\n- **Strengths**: 新颖性和贡献优点\n- **Weaknesses**: 新颖性和贡献缺陷（按严重性排序，标注 Must-Fix / Should-Fix / Minor）\n- **Missing References**: 遗漏的重要相关工作\n- **Questions**: 需作者澄清的定位问题\n- **Overall Assessment**: 新颖性和贡献总评"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "project": "vla-ssd",
    "text": "你是 Reviewer 2，负责审查 **新颖性、贡献定位、Related Work 和增量贡献评估**。\n\n## 论文信息\n- **标题**: \"Three Architectures, One Routing Pattern: How VLA Fine-Tuning Reshapes Instruction Flow\"\n- **Venue**: CoRL 2026（Conference on Robot Learning）\n- **截止日期**: 2026-05-29\n- **格式**: corl_2026 模板，正文 8 页，double-blind\n- **论文路径**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/main.tex`\n- **PDF**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/review_round_15/submitted.pdf`\n\n## 你的审查侧重\n\n**核心任务**：以顶会最严格审稿人标准评估本文的新颖性和学术贡献。\n\n请重点审查以下方面：\n\n1. **新颖性评估**:\n   - R² exit collapse 是否为真正的新发现，还是已知现象的重新表述\n   - Cross-architecture 分析（3 models × 4 suites）相比 single-architecture 分析的增量价值\n   - \"Training-induced vs inherited routing\" 分解框架的原创性\n   - Title 声称 \"One Routing Pattern\" 是否被数据支撑（N=2 VLM-to-VLA transitions）\n\n2. **贡献定位**:\n   - 三个贡献是否 well-defined 且与 claims 一致\n   - \"Convergent/consistent reorganization\" 从 N=2 同类架构得出的说服力\n   - 与 Grant et al. (2026)、Häon et al. (2025)、Swann et al. (2026)、Buurmeijer et al. (2026) 的区分是否清晰\n   - 论文是 confirmatory（确认已知现象跨架构成立）还是 discovery（发现新现象）\n\n3. **Related Work 覆盖度**:\n   - VLA mechanistic interpretability 文献是否完整\n   - VLM representational analysis（Neo et al. ICLR 2025, Long et al. ICLR 2026, Fan et al. CVPR 2026）是否充分讨论\n   - Fine-tuning representation theory（Aghajanyan et al. 2021, Kumar et al. 2022）是否引用\n   - 是否有重要遗漏的 2025-2026 相关工作\n\n4. **Claims 与 Evidence 匹配**:\n   - Abstract/Introduction 中的 claims 是否被实验数据支撑\n   - \"Consistent across architectures\" 在 10/12 filled cells 中是否 overclaimed\n   - Counterfactual sensitivity \"d ≥ 0.45\" 的 framing 是否准确\n   - NLP control 单独是否足以支撑 \"VLA-specific\" claim\n\n请给出：\n- **Strengths**: 新颖性和贡献优点\n- **Weaknesses**: 新颖性和贡献缺陷（按严重性排序，标注 Must-Fix / Should-Fix / Minor）\n- **Missing References**: 遗漏的重要相关工作\n- **Questions**: 需作者澄清的定位问题\n- **Overall Assessment**: 新颖性和贡献总评"
  }
}
```

</details>

---


### Tool result

_source line 1240 · 2026-05-22T13:36:43.912051+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 19104
}
```

</details>

---


### Tool call

_source line 1241 · 2026-05-22T13:36:44.113282+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "3",
  "round_number": "1",
  "project": "vla-ssd",
  "text": "你是 Reviewer 3，负责审查 **CoRL scope fit、格式合规性和写作质量**。\n\n## 论文信息\n- **标题**: \"Three Architectures, One Routing Pattern: How VLA Fine-Tuning Reshapes Instruction Flow\"\n- **Venue**: CoRL 2026（Conference on Robot Learning）\n- **截止日期**: 2026-05-29\n- **格式要求**:\n  - corl_2026 模板\n  - 正文 8 页限制（Limitations 计入，References/Appendix 不计入）\n  - Double-blind 匿名提交\n  - 必须包含 Limitations section（计入页数）\n  - GenAI 使用声明必需\n  - 并行投稿规则：禁止与已发表/并行投稿的 substantially similar 论文\n- **论文路径**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/main.tex`\n- **PDF**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/review_round_15/submitted.pdf`\n\n## 你的审查侧重\n\n**核心任务**：以顶会最严格审稿人标准评估本文的 venue 适配性、格式合规和写作质量。\n\n请重点审查以下方面：\n\n1. **CoRL Scope Fit**:\n   - 本文是纯 representational/mechanistic analysis，无物理机器人实验、无 closed-loop 评估、无 sim-to-real 验证——这对 CoRL（a robotics conference）是否合适\n   - 论文的 robotics community 受众匹配度\n   - 发现的 actionable implications 对机器人研究者的价值\n   - 是否更适合 ICML/NeurIPS interpretability track 或 ICLR\n\n2. **格式合规**:\n   - 正文页数是否 ≤ 8 页（检查 PDF：Discussion + Conclusion 是否在第 8 页内结束）\n   - Limitations 是否作为独立 section 或 subsection（CoRL 要求）\n   - 匿名性：是否有 de-anonymizing 信息（作者名、GitHub 链接、机构标识）\n   - GenAI disclosure 是否存在且位置合理\n   - `\\usepackage{corl_2026}` 模板使用是否正确\n   - main.tex 中的 `\\setlength` spacing 修改是否可能与模板冲突\n   - 引用格式是否一致（所有 arXiv 引用是否应更新为正式版本）\n\n3. **写作质量**:\n   - Abstract 长度和信息密度是否合理（是否信息过载）\n   - Introduction 与 Abstract 的重复度\n   - 术语一致性（readout token vs last_preaction 等）\n   - Table/Figure caption 是否 standalone readable\n   - Appendix 中 Table 的 resizebox 是否导致字体过小\n   - 是否有 AI 写作痕迹（em-dash、过度形式化、机械式列举）\n\n4. **可读性**:\n   - 对 CoRL 受众（机器人研究者，非 NLP/interpretability 专家）是否 accessible\n   - 核心发现是否在 Introduction 中清晰传达\n   - Figures 是否直观传达核心信息\n   - 符号和缩写是否在首次出现时定义\n\n请给出：\n- **Strengths**: scope/格式/写作优点\n- **Weaknesses**: 缺陷（按严重性排序，标注 Must-Fix / Should-Fix / Minor）\n- **Questions**: 需作者澄清的问题\n- **Overall Assessment**: scope fit 和写作总评"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "3",
    "round_number": "1",
    "project": "vla-ssd",
    "text": "你是 Reviewer 3，负责审查 **CoRL scope fit、格式合规性和写作质量**。\n\n## 论文信息\n- **标题**: \"Three Architectures, One Routing Pattern: How VLA Fine-Tuning Reshapes Instruction Flow\"\n- **Venue**: CoRL 2026（Conference on Robot Learning）\n- **截止日期**: 2026-05-29\n- **格式要求**:\n  - corl_2026 模板\n  - 正文 8 页限制（Limitations 计入，References/Appendix 不计入）\n  - Double-blind 匿名提交\n  - 必须包含 Limitations section（计入页数）\n  - GenAI 使用声明必需\n  - 并行投稿规则：禁止与已发表/并行投稿的 substantially similar 论文\n- **论文路径**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/main.tex`\n- **PDF**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/review_round_15/submitted.pdf`\n\n## 你的审查侧重\n\n**核心任务**：以顶会最严格审稿人标准评估本文的 venue 适配性、格式合规和写作质量。\n\n请重点审查以下方面：\n\n1. **CoRL Scope Fit**:\n   - 本文是纯 representational/mechanistic analysis，无物理机器人实验、无 closed-loop 评估、无 sim-to-real 验证——这对 CoRL（a robotics conference）是否合适\n   - 论文的 robotics community 受众匹配度\n   - 发现的 actionable implications 对机器人研究者的价值\n   - 是否更适合 ICML/NeurIPS interpretability track 或 ICLR\n\n2. **格式合规**:\n   - 正文页数是否 ≤ 8 页（检查 PDF：Discussion + Conclusion 是否在第 8 页内结束）\n   - Limitations 是否作为独立 section 或 subsection（CoRL 要求）\n   - 匿名性：是否有 de-anonymizing 信息（作者名、GitHub 链接、机构标识）\n   - GenAI disclosure 是否存在且位置合理\n   - `\\usepackage{corl_2026}` 模板使用是否正确\n   - main.tex 中的 `\\setlength` spacing 修改是否可能与模板冲突\n   - 引用格式是否一致（所有 arXiv 引用是否应更新为正式版本）\n\n3. **写作质量**:\n   - Abstract 长度和信息密度是否合理（是否信息过载）\n   - Introduction 与 Abstract 的重复度\n   - 术语一致性（readout token vs last_preaction 等）\n   - Table/Figure caption 是否 standalone readable\n   - Appendix 中 Table 的 resizebox 是否导致字体过小\n   - 是否有 AI 写作痕迹（em-dash、过度形式化、机械式列举）\n\n4. **可读性**:\n   - 对 CoRL 受众（机器人研究者，非 NLP/interpretability 专家）是否 accessible\n   - 核心发现是否在 Introduction 中清晰传达\n   - Figures 是否直观传达核心信息\n   - 符号和缩写是否在首次出现时定义\n\n请给出：\n- **Strengths**: scope/格式/写作优点\n- **Weaknesses**: 缺陷（按严重性排序，标注 Must-Fix / Should-Fix / Minor）\n- **Questions**: 需作者澄清的问题\n- **Overall Assessment**: scope fit 和写作总评"
  }
}
```

</details>

---


### Tool call

_source line 1242 · 2026-05-22T13:36:45.266968+00:00_

called mcp__agent-ml-research__dispatch_visual_check

<details open><summary>🔧 Tool call — mcp__agent-ml-research__dispatch_visual_check</summary>

```json
{
  "project": "vla-ssd",
  "review_chat_id": "oc_554a5023cde4d603635cf97e6ab8151a"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "tool_args": {
    "project": "vla-ssd",
    "review_chat_id": "oc_554a5023cde4d603635cf97e6ab8151a"
  }
}
```

</details>

---


### Tool result

_source line 1243 · 2026-05-22T13:36:45.623100+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:reviewer_3\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1509
}
```

</details>

---


### Tool result

_source line 1244 · 2026-05-22T13:36:47.292063+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 2025
}
```

</details>

---


### Assistant

_source line 1245 · 2026-05-22T13:37:01.102845+00:00_

**Round 15 Step 1 已启动**：

- ✅ Reviewer 1（方法/统计）— 已派发
- ✅ Reviewer 2（新颖性/贡献）— 已派发
- ✅ Reviewer 3（Scope/格式/写作）— 已派发
- ✅ 视觉审查 Agent — 已派发（fire-and-forget）
- ⏭️ 外部审稿 — 跳过（未配置）

等待三位 Reviewer 独立审稿返回。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_554a5023cde4d603635cf97e6ab8151a:director"
}
```

</details>

---


## Round 111

## Round 111

2 recorded events
