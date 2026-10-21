# Director coordination — Part 9 of 14

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Conversation logs

[← Part 8](part-008.md) · [Transcript overview](../director-coordination.md) · [Part 10 →](part-010.md) · [Structured JSON](../../../sessions/46/46a4a073b0cc4314da71.json)

## Round 221

### Tool call

_source line 2578 · 2026-05-20T17:23:38.584247+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "text": "你是 Reviewer 1（方法严谨性 + 实验设计），这是 Round 34 继续审稿。论文已根据 Round 33 审稿意见修改。\n\n## Venue 信息\n- EMNLP 2026 via ARR, Long Paper, 8 页正文, Double-blind\n- 截止日期: 2026-05-25\n\n## 论文文件\n- LaTeX: `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/main.pdf`\n\n## 你的任务\n\n**本轮不是初审，而是修订评估。** 上一轮评分 3.0 (Findings)。请逐条验证以下 11 条 in_progress issue 是否已被充分修复，标注 [RESOLVED]（已解决）或 [STILL_OPEN]（未解决 + 理由）。同时检查修改是否引入新问题。\n\n## 需验证的 Open/In-Progress Issues\n\n### 你上轮主导的 Critical Issues\n\n**R29-W4** [critical, in_progress] — 3/1/3 partition post-hoc, k-means 仅支持 2-way split\n- 上轮要求：以 2-way split 为核心，3/1/3 降级为 domain-informed refinement\n- 修改声明：§4.2 已重构，2-way binary split as primary (k=2, sil=0.632)，3/1/3 as domain-informed refinement\n- 请验证 results.tex §4.2 的实际表述\n\n**R32-N2** [critical, in_progress] — Entropy min 分类矛盾 (|ρ|=0.40 标为 near-stationary)\n- 上轮要求：标为 boundary feature 或采用 3/2/2 partition\n- 修改声明：entropy_min 已标为 \"boundary feature\"，保留在 non-drifting group\n- 请验证 results.tex 中 entropy min 的实际描述和 Figure 2 caption\n\n**R32-N3** [critical, in_progress] — Tail_decay TOST 仅 4/8 pass\n- 上轮要求：主文明确 borderline 状态，报告 per-generator 通过率\n- 修改声明：Validation paragraph 已报告 8/8, 6/8, 4/8 通过率，OLMo d=0.22 点名，pooled power caveat\n- 请验证 results.tex Validation paragraph\n\n### 你上轮参与的 Major/Warning Issues\n\n**R29-N4** [warning, in_progress] — QLoRA gap 重定位\n- 修改声明：Contribution 3 改为 \"Proof-of-concept classifier\"，§4.3 明确 DDR 贡献是 decomposition\n- 请验证 Introduction contributions list 和 §4.3\n\n**R29-W5** [warning, in_progress] — Baseline 比较结构性不公平\n- 修改声明：§4.3 明确指出 4-det+surface 0.708 优于 7-feature 0.705\n- 请验证 Table 2 周围的文字\n\n**R32-W2** [warning, in_progress] — TOST power analysis 缺失\n- 修改声明：Agent 已派发计算 TOST power\n- 请检查 appendix_tost.tex 是否新增 power analysis 内容（初步检查未发现新增）\n\n### 其他需验证的 Issues\n\n**R29-N2** [critical, in_progress] — Downstream null result framing\n- 修改声明：Abstract/Conclusion 已 reframe downstream claim\n- 请验证 Abstract 是否移除了 downstream claim 或改为更精确表述\n\n**R29-W2** [warning, in_progress] — Cross-model chain confound\n- 修改声明：results.tex 已加 \"not directly comparable\" + 5-generator caveat\n- 请验证 footnote 和周围文字\n\n**R32-N1** [critical, in_progress] — DDR 新颖性 vs diversity loss\n- 修改声明：Discussion 新增 \"Prior work documents what converges... but not what is preserved\"\n- 请验证 Discussion 和 Abstract 中的 novelty positioning\n\n**R32-W1** [warning, in_progress] — F1=0.694 proof-of-concept 定位\n- 修改声明：Discussion 明确 \"proof-of-concept, not a deployable system\"\n- 请验证 Discussion 和 Introduction\n\n**R29-W6** [warning, in_progress] — 缺失引用\n- self_refine orphan 已删除\n- Wang et al., Sun et al. 等 6 篇 references 是否已验证/添加？请检查 references.bib\n\n## 输出格式\n\n对每条 issue：[RESOLVED] 或 [STILL_OPEN] + 具体理由（引用修改后的具体文字）\n\n然后：\n- 修改是否引入新问题？\n- 更新后的 Overall Assessment（是否从 3.0 上调？）\n- Strengths/Weaknesses 变化总结",
  "reviewer_id": "1",
  "project": "gen-depth-fingerprint",
  "round_number": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "text": "你是 Reviewer 1（方法严谨性 + 实验设计），这是 Round 34 继续审稿。论文已根据 Round 33 审稿意见修改。\n\n## Venue 信息\n- EMNLP 2026 via ARR, Long Paper, 8 页正文, Double-blind\n- 截止日期: 2026-05-25\n\n## 论文文件\n- LaTeX: `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/main.pdf`\n\n## 你的任务\n\n**本轮不是初审，而是修订评估。** 上一轮评分 3.0 (Findings)。请逐条验证以下 11 条 in_progress issue 是否已被充分修复，标注 [RESOLVED]（已解决）或 [STILL_OPEN]（未解决 + 理由）。同时检查修改是否引入新问题。\n\n## 需验证的 Open/In-Progress Issues\n\n### 你上轮主导的 Critical Issues\n\n**R29-W4** [critical, in_progress] — 3/1/3 partition post-hoc, k-means 仅支持 2-way split\n- 上轮要求：以 2-way split 为核心，3/1/3 降级为 domain-informed refinement\n- 修改声明：§4.2 已重构，2-way binary split as primary (k=2, sil=0.632)，3/1/3 as domain-informed refinement\n- 请验证 results.tex §4.2 的实际表述\n\n**R32-N2** [critical, in_progress] — Entropy min 分类矛盾 (|ρ|=0.40 标为 near-stationary)\n- 上轮要求：标为 boundary feature 或采用 3/2/2 partition\n- 修改声明：entropy_min 已标为 \"boundary feature\"，保留在 non-drifting group\n- 请验证 results.tex 中 entropy min 的实际描述和 Figure 2 caption\n\n**R32-N3** [critical, in_progress] — Tail_decay TOST 仅 4/8 pass\n- 上轮要求：主文明确 borderline 状态，报告 per-generator 通过率\n- 修改声明：Validation paragraph 已报告 8/8, 6/8, 4/8 通过率，OLMo d=0.22 点名，pooled power caveat\n- 请验证 results.tex Validation paragraph\n\n### 你上轮参与的 Major/Warning Issues\n\n**R29-N4** [warning, in_progress] — QLoRA gap 重定位\n- 修改声明：Contribution 3 改为 \"Proof-of-concept classifier\"，§4.3 明确 DDR 贡献是 decomposition\n- 请验证 Introduction contributions list 和 §4.3\n\n**R29-W5** [warning, in_progress] — Baseline 比较结构性不公平\n- 修改声明：§4.3 明确指出 4-det+surface 0.708 优于 7-feature 0.705\n- 请验证 Table 2 周围的文字\n\n**R32-W2** [warning, in_progress] — TOST power analysis 缺失\n- 修改声明：Agent 已派发计算 TOST power\n- 请检查 appendix_tost.tex 是否新增 power analysis 内容（初步检查未发现新增）\n\n### 其他需验证的 Issues\n\n**R29-N2** [critical, in_progress] — Downstream null result framing\n- 修改声明：Abstract/Conclusion 已 reframe downstream claim\n- 请验证 Abstract 是否移除了 downstream claim 或改为更精确表述\n\n**R29-W2** [warning, in_progress] — Cross-model chain confound\n- 修改声明：results.tex 已加 \"not directly comparable\" + 5-generator caveat\n- 请验证 footnote 和周围文字\n\n**R32-N1** [critical, in_progress] — DDR 新颖性 vs diversity loss\n- 修改声明：Discussion 新增 \"Prior work documents what converges... but not what is preserved\"\n- 请验证 Discussion 和 Abstract 中的 novelty positioning\n\n**R32-W1** [warning, in_progress] — F1=0.694 proof-of-concept 定位\n- 修改声明：Discussion 明确 \"proof-of-concept, not a deployable system\"\n- 请验证 Discussion 和 Introduction\n\n**R29-W6** [warning, in_progress] — 缺失引用\n- self_refine orphan 已删除\n- Wang et al., Sun et al. 等 6 篇 references 是否已验证/添加？请检查 references.bib\n\n## 输出格式\n\n对每条 issue：[RESOLVED] 或 [STILL_OPEN] + 具体理由（引用修改后的具体文字）\n\n然后：\n- 修改是否引入新问题？\n- 更新后的 Overall Assessment（是否从 3.0 上调？）\n- Strengths/Weaknesses 变化总结",
    "reviewer_id": "1",
    "project": "gen-depth-fingerprint",
    "round_number": "2"
  }
}
```

</details>

---


### Tool result

_source line 2579 · 2026-05-20T17:23:58.898565+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 20314
}
```

</details>

---


### Tool call

_source line 2580 · 2026-05-20T17:23:59.099703+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "text": "你是 Reviewer 2（新颖性 + 完整性 + 写作质量），这是 Round 34 继续审稿。论文已根据 Round 33 审稿意见修改。\n\n## Venue 信息\n- EMNLP 2026 via ARR, Long Paper, 8 页正文, Double-blind\n- 截止日期: 2026-05-25\n\n## 论文文件\n- LaTeX: `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/main.pdf`\n\n## 你的任务\n\n**本轮不是初审，而是修订评估。** 上一轮评分 3.0 (Findings)。请逐条验证以下 11 条 in_progress issue 是否已被充分修复，标注 [RESOLVED]（已解决）或 [STILL_OPEN]（未解决 + 理由）。同时检查修改是否引入新问题。\n\n## 需验证的 Open/In-Progress Issues\n\n### 你上轮主导的 Critical Issues\n\n**R32-N1** [critical, in_progress] — DDR 增量新颖性不清晰，可能是 diversity loss 重新表述\n- 上轮要求：证明 location/shape 分解提供已有文献未涵盖的独立洞察；设计实验对比 DDR vs diversity-decline\n- 修改声明：Discussion 新增 \"Prior work documents what converges... but not what is preserved\"；Abstract 新增 shape-invariance 定位\n- 请验证 Abstract、Introduction、Discussion 中的 novelty framing 是否充分回应了 \"DDR 只是 diversity loss 重新表述\" 的批评\n\n**R29-N2** [critical, in_progress] — Downstream null result framing 含糊\n- 上轮要求：Abstract 改为更精确表述；降低 downstream 贡献权重\n- 修改声明：Abstract/Conclusion reframed\n- 请验证 Abstract 是否移除或改善了 downstream claim\n\n### 你上轮参与的 Major Issues\n\n**R29-N4** [warning, in_progress] — QLoRA gap (+11.6pp) 反衬 7-feature 局限\n- 修改声明：Contribution 3 = \"Proof-of-concept classifier\"\n- 请验证 Introduction 和 §4.1 中 QLoRA 的定位\n\n**R32-W1** [warning, in_progress] — F1=0.694 定位为 detecting 但实为 proof-of-concept\n- 修改声明：Discussion \"proof-of-concept, not a deployable system\"\n- 请验证标题是否仍有误导性（\"Detecting\" in title）\n\n### 其他需验证的 Issues\n\n**R29-W4** [critical, in_progress] — 3/1/3 partition → 2-way primary\n- 请验证 §4.2 的重构质量\n\n**R32-N2** [critical, in_progress] — Entropy min boundary feature\n- 请验证 boundary feature 标签是否在 §4.2 和 Figure 2 caption 中清晰呈现\n\n**R32-N3** [critical, in_progress] — Tail_decay TOST 4/8 borderline\n- 请验证主文 Validation paragraph 的透明度\n\n**R29-W5** [warning, in_progress] — Baseline 比较不公平\n- 请验证 §4.3 是否诚实呈现 4-det ensemble 优势\n\n**R29-W2** [warning, in_progress] — Cross-model chain confound\n- 请验证 footnote 和 caveats\n\n**R32-W2** [warning, in_progress] — TOST power analysis 缺失\n- 请检查 appendix_tost.tex\n\n**R29-W6** [warning, in_progress] — 缺失引用\n- 请验证：(1) self_refine orphan 是否已删除；(2) 你上轮建议的 Wang et al. (ACL 2025)、Sun et al. (2026) 是否已添加或有说明；(3) 是否有其他新遗漏\n\n## 额外检查（你的领域）\n- 写作质量：修改后的叙事流是否更清晰？\n- 格式合规：8 页限制？匿名性？\n- Novelty framing：修改后 DDR 的 \"what is preserved\" 论证是否足以区分于 diversity loss 文献？\n\n## 输出格式\n\n对每条 issue：[RESOLVED] 或 [STILL_OPEN] + 具体理由（引用修改后的具体文字）\n\n然后：\n- 修改是否引入新问题？\n- 更新后的 Overall Assessment（是否从 3.0 上调？）\n- Strengths/Weaknesses 变化总结",
  "reviewer_id": "2",
  "project": "gen-depth-fingerprint",
  "round_number": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "text": "你是 Reviewer 2（新颖性 + 完整性 + 写作质量），这是 Round 34 继续审稿。论文已根据 Round 33 审稿意见修改。\n\n## Venue 信息\n- EMNLP 2026 via ARR, Long Paper, 8 页正文, Double-blind\n- 截止日期: 2026-05-25\n\n## 论文文件\n- LaTeX: `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/main.pdf`\n\n## 你的任务\n\n**本轮不是初审，而是修订评估。** 上一轮评分 3.0 (Findings)。请逐条验证以下 11 条 in_progress issue 是否已被充分修复，标注 [RESOLVED]（已解决）或 [STILL_OPEN]（未解决 + 理由）。同时检查修改是否引入新问题。\n\n## 需验证的 Open/In-Progress Issues\n\n### 你上轮主导的 Critical Issues\n\n**R32-N1** [critical, in_progress] — DDR 增量新颖性不清晰，可能是 diversity loss 重新表述\n- 上轮要求：证明 location/shape 分解提供已有文献未涵盖的独立洞察；设计实验对比 DDR vs diversity-decline\n- 修改声明：Discussion 新增 \"Prior work documents what converges... but not what is preserved\"；Abstract 新增 shape-invariance 定位\n- 请验证 Abstract、Introduction、Discussion 中的 novelty framing 是否充分回应了 \"DDR 只是 diversity loss 重新表述\" 的批评\n\n**R29-N2** [critical, in_progress] — Downstream null result framing 含糊\n- 上轮要求：Abstract 改为更精确表述；降低 downstream 贡献权重\n- 修改声明：Abstract/Conclusion reframed\n- 请验证 Abstract 是否移除或改善了 downstream claim\n\n### 你上轮参与的 Major Issues\n\n**R29-N4** [warning, in_progress] — QLoRA gap (+11.6pp) 反衬 7-feature 局限\n- 修改声明：Contribution 3 = \"Proof-of-concept classifier\"\n- 请验证 Introduction 和 §4.1 中 QLoRA 的定位\n\n**R32-W1** [warning, in_progress] — F1=0.694 定位为 detecting 但实为 proof-of-concept\n- 修改声明：Discussion \"proof-of-concept, not a deployable system\"\n- 请验证标题是否仍有误导性（\"Detecting\" in title）\n\n### 其他需验证的 Issues\n\n**R29-W4** [critical, in_progress] — 3/1/3 partition → 2-way primary\n- 请验证 §4.2 的重构质量\n\n**R32-N2** [critical, in_progress] — Entropy min boundary feature\n- 请验证 boundary feature 标签是否在 §4.2 和 Figure 2 caption 中清晰呈现\n\n**R32-N3** [critical, in_progress] — Tail_decay TOST 4/8 borderline\n- 请验证主文 Validation paragraph 的透明度\n\n**R29-W5** [warning, in_progress] — Baseline 比较不公平\n- 请验证 §4.3 是否诚实呈现 4-det ensemble 优势\n\n**R29-W2** [warning, in_progress] — Cross-model chain confound\n- 请验证 footnote 和 caveats\n\n**R32-W2** [warning, in_progress] — TOST power analysis 缺失\n- 请检查 appendix_tost.tex\n\n**R29-W6** [warning, in_progress] — 缺失引用\n- 请验证：(1) self_refine orphan 是否已删除；(2) 你上轮建议的 Wang et al. (ACL 2025)、Sun et al. (2026) 是否已添加或有说明；(3) 是否有其他新遗漏\n\n## 额外检查（你的领域）\n- 写作质量：修改后的叙事流是否更清晰？\n- 格式合规：8 页限制？匿名性？\n- Novelty framing：修改后 DDR 的 \"what is preserved\" 论证是否足以区分于 diversity loss 文献？\n\n## 输出格式\n\n对每条 issue：[RESOLVED] 或 [STILL_OPEN] + 具体理由（引用修改后的具体文字）\n\n然后：\n- 修改是否引入新问题？\n- 更新后的 Overall Assessment（是否从 3.0 上调？）\n- Strengths/Weaknesses 变化总结",
    "reviewer_id": "2",
    "project": "gen-depth-fingerprint",
    "round_number": "2"
  }
}
```

</details>

---


### Tool result

_source line 2581 · 2026-05-20T17:24:00.550109+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1450
}
```

</details>

---


### Assistant

_source line 2582 · 2026-05-20T17:24:09.332926+00:00_

Round 34 审稿任务已派发：
- **视觉审查**: 已启动
- **Reviewer 1** (方法严谨性): 逐条验证 11 条 in_progress issue
- **Reviewer 2** (新颖性+写作): 逐条验证 11 条 in_progress issue + 写作/格式检查

等待两位 Reviewer 返回验证结果。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director"
}
```

</details>

---


## Round 222

## Round 222

2 recorded events


### User

_source line 2583 · 2026-05-20T17:27:11.621006+00:00_

[Reviewer 1 审稿意见]:

## Reviewer 1 — Round 2 修订验证报告

**上一轮评分**: 3.0 (Findings, consensus)
**本轮任务**: 验证 11 条 in_progress issues 的修复状态

---

## 逐条验证

### R29-W4 [critical] — 3/1/3 partition post-hoc → 2-way split 为核心

**[RESOLVED]**

修改到位且措辞精确。关键改动：

1. results.tex L63: **"The primary partition is binary: k=2 clustering in standardized (|ρ|, d) space yields silhouette=0.632, cleanly separating three drifting features from four non-drifting ones; higher k degrades cluster quality (k=3: silhouette=0.499)."** — 二元 split 现在是第一个出现的 partition 描述，k=3 明确标为 quality degradation。

2. L64: **"A domain-informed refinement resolves entropy std as a sole intermediate member"** — 3/1/3 明确标为 "domain-informed refinement"，不再暗示数据驱动。

3. Introduction Contribution 1 (L18): **"Data-driven clustering (k=2, silhouette=0.632) reveals that inference-chain drift separates into a drifting location component and a stable shape component."** — Contribution 语言对齐。

4. Abstract L4: **"a separation validated by five independent effect-size metrics and data-driven clustering (silhouette=0.632)"** — 引用的是 k=2 silhouette。

这是本轮最重要的结构性改进。论文的 DDR 贡献叙事从 over-refined 的 3/1/3 回退到数据支持的 2-way split，同时保留了 domain-informed refinement 作为 secondary analysis。

---

### R32-N2 [critical] — Entropy min 分类矛盾 (|ρ|=0.40 标为 near-stationary)

**[RESOLVED]**

1. results.tex L85: **"Entropy min is a *boundary feature*: its gen-1 vs. gen-2+ effect is near-stationary (d=0.016) despite a substantial pooled |ρ| (0.40) driven by the gen-0/gen-1 transition (Cliff's δ=0.354 confirms shape change without location shift); k=2 clustering places it with non-drifting features."**

2. Figure 2 caption (L70): **"Entropy min (|ρ|=0.40 pooled) is a boundary feature whose sensitivity concentrates at the gen-0/gen-1 transition."**

"Boundary feature" 标签准确反映了 entropy min 的矛盾属性：location-stationary 但 rank-order-sensitive，pooled |ρ| 被 gen-0/gen-1 transition 驱动。同时明确了 k=2 clustering 将它归入 non-drifting，保持了与数据驱动 partition 的一致性。

---

### R32-N3 [critical] — Tail_decay TOST 仅 4/8 pass

**[RESOLVED]**

results.tex L89-91 三句话完整覆盖了要求的所有内容：

1. **"tail decay passes for only 4/8 generators, with OLMo-2-1B (d=0.22) exceeding the equivalence bound"** — 4/8 通过率进入主文，OLMo 被点名。

2. **"but high pooled power (N ≈ 3,500–4,500 per generator) can mask per-generator heterogeneity"** — 承认 pooled bootstrap 的 power caveat。

3. **"Tail decay's 50% per-generator pass rate represents a genuine boundary case: reclassifying it as intermediate preserves the core drifting/non-drifting split and classification performance (F1 change <0.5pp)."** — 明确标为 "genuine boundary case"，并量化了重分类的影响。

相比之前版本（仅在附录中报告 4/8），这是显著改善。主文现在诚实地呈现了 near-stationary partition 在 tail_decay 上的弱点。

---

### R29-N4 [warning] — QLoRA gap 重定位

**[RESOLVED]**

Proof-of-concept 定位一致贯穿全文：

- Introduction L14: **"As a proof of concept, a lightweight 7-feature ensemble..."**
- Contribution 3 (L20): **"Proof-of-concept classifier with boundary analysis"**
- results.tex L17: **"establishing the empirical decomposition---not the specific classifier---as DDR's primary contribution"**
- results.tex L142: **"DDR's primary contribution is not classification performance---where multi-detector ensembles match or marginally exceed it---but the decomposition..."**
- Discussion L11: **"The classifier is a proof-of-concept, not a deployable system"**

五个位置一致传达：分类器是验证 DDR 的工具，不是独立贡献。

---

### R29-W5 [warning] — Baseline 比较结构性不公平

**[RESOLVED]**

results.tex L140-142:

**"The 7-feature ensemble surpasses all individual baselines in 3-class F1 and the pure 4-detector ensemble in binary F1 (0.705 vs. 0.700). Adding DDR's surface features to the four detectors yields the highest binary F1 (0.708), marginally above the 7-feature set at 2.4× the inference cost. This result underscores that DDR's primary contribution is not classification performance---where multi-detector ensembles match or marginally exceed it---but the decomposition of depth signal into location-sensitive and shape-stable components."**

4-det+surface 的优势（0.708 > 0.705）现在被明确承认，且直接用来 pivot 到 DDR 的分析贡献。这是非常好的 framing。

---

### R32-W2 [warning] — TOST power analysis 缺失

**[STILL_OPEN]**

appendix_tost.tex 未新增任何 power analysis 内容（grep 确认无 "power analysis"/"statistical power" 匹配）。

results.tex L90 添加了 **"but high pooled power (N ≈ 3,500–4,500 per generator) can mask per-generator heterogeneity"** — 这是定性 caveat，不是定量 power analysis。

缺失的是：给定 per-generator n≈3,500–4,500、ε=0.20、观测到的方差，TOST 能区分 true d=0.10 vs d=0.20 的 power 是多少？这会帮助读者判断 4/8 pass rate 的信息量。

**严重程度**：从 warning 降级为 minor。理由：(1) 主文已添加 pooled power caveat；(2) tail_decay 的 50% pass rate 被明确标为 "genuine boundary case"；(3) 缺少 formal power calculation 不影响核心结论（2-way drifting/non-drifting split 不依赖 TOST）。建议在 camera-ready 中补充，但不阻碍接收。

---

### R29-N2 [critical] — Downstream null result framing

**[RESOLVED]**

Abstract 中 downstream claim 已 **完全移除**。之前的 "preliminary equivalence testing (TOST ±2%, p < 0.001; n=3 seeds) suggests no downstream training quality degradation" 不再出现。

当前 abstract（abstract.tex）聚焦于 DDR decomposition 和 classification performance，不再提及 downstream utility。Conclusion（conclusion.tex）同样无 downstream claim。

Appendix M 的 downstream 实验仍然保留作为补充材料，这是合适的——实验结果本身是 informative 的（null result），只是不应在 abstract 中作为 contribution 呈现。

---

### R29-W2 [warning] — Cross-model chain confound

**[RESOLVED with minor reservation]**

results.tex L14 footnote: **"5-generator subset (Pythia-2.8B/1B, OLMo-2-1B, Qwen3-0.6B/1.7B); generator-level LOGO with bootstrap CIs (n=2,000). Not directly comparable to 8-generator LOGO due to differing subsets."**

L15: **"Single-generator transfer... confirms the signal is not a mixed-chain artifact"**

**Minor reservation**: Contribution 3 (Introduction L20) 仍以 F1=0.830（cross-model）为 headline 数字而非 0.694（8-gen LOGO）。考虑到 0.830 来自 5-generator subset 且可能受 generator heterogeneity confound 影响，lead with 0.830 仍有些 cherry-picking。但鉴于 "proof-of-concept" 定位和 footnote caveat，这不构成严重问题。

---

### R32-N1 [critical] — DDR 新颖性 vs diversity loss

**[RESOLVED]**

Novelty positioning 现在清晰且在四个位置一致：

- Abstract L5: **"Where prior work on iterative generation documents *what converges*, the novel observation here is *what is preserved*: shape invariance under the same process that compresses location provides the stable reference needed for depth estimation without per-generator calibration."**
- Introduction L11: **"ours is the first to decompose the drift into complementary location and shape components"**
- Contribution 1 (L18): **"Where prior work documents *what converges*, DDR identifies *what is preserved*"**
- Discussion L19: **"Prior work documents *what converges*---diversity loss, attractor dynamics, mode collapse---but not what is *preserved*; this complementary observation is what enables depth detection without per-generator calibration."**

"What converges vs. what is preserved" 的对比框架精准定位了 DDR 相对于 prior work 的增量贡献。Discussion L19 进一步列举了三类 prior work（diversity loss、attractor dynamics、mode collapse）并明确说明 DDR 补充的是 preserved component。

---

### R32-W1 [warning] — F1=0.694 proof-of-concept 定位

**[RESOLVED]**

见 R29-N4 的验证。"Proof-of-concept" 出现在 Introduction L14、Contribution 3 标题、Discussion L11。Discussion L11 进一步量化了局限性："document-level gen-1 per-class F1=0.63 and ~30% error rate are insufficient for automated filtering but sufficient for corpus-level flagging"。

---

### R29-W6 [warning] — 缺失引用

**[PARTIALLY RESOLVED]**

- **self_refine orphan**: ✅ 已从 .bib 和 .tex 中完全删除（grep 确认无匹配）。
- **Wang et al. "Attractor Cycles" / Sun et al. "When AI Settles Down"**: ❌ 未添加（grep 确认无匹配）。但在 Round 1 cross-review 中，我已指出这两篇无法确认存在——R2 未提供 DOI 或完整信息。这不应视为未修复。
- **我自己建议的 3 篇参考文献**（Guo et al. 2024, Li et al. 2024, Zhang et al. 2024）：这些是建议而非硬性要求，未添加不影响评分。

---

## 修改是否引入新问题？

**无重大新问题。** 修改集中在 framing 和文字层面，未改变实验数据或分析方法。一个 minor observation：

- **Contribution 3 headline number**: Introduction L20 以 "binary F1=0.830 on cross-model chains" 为 lead。虽然标注了 "proof-of-concept"，但在贡献列表中使用 confounded 设置的 higher number 而非 primary metric（0.694）仍稍有 cherry-picking 之嫌。建议改为 "binary F1=0.694 under LOGO (0.830 on cross-model chains)"。**严重程度：cosmetic。**

---

## 更新后的 Overall Assessment

**Updated Overall: 3.5 / 5 — Borderline Conference**（从 consensus 3.0 上调 0.5）

| 维度 | 上轮 | 本轮 | 变化理由 |
|------|------|------|----------|
| Soundness | 3.0 | 3.5 | 2-way split 为核心、entropy min 标为 boundary、tail_decay 50% acknowledged — overclaiming 问题大幅缓解 |
| Excitement | 3.0 | 3.0 | 无新实验，scope 不变（base-model-only） |
| Reproducibility | 4.0 | 4.0 | 不变 |
| Overall | 3.0 | 3.5 | Framing 改进将 soundness 提升半档 |

### Strengths 变化
原有优势（S1-S5）全部保留。新增：
- **S6. Framing 诚实度提升。** "Proof-of-concept"、"boundary feature"、"genuine boundary case"、"domain-informed refinement" 等措辞使论文的 claim 与 evidence 更加匹配。这在 EMNLP 投稿中值得肯定。

### Weaknesses 变化
- ~~C1 (3/1/3 post-hoc)~~: **RESOLVED**
- ~~C2 (Entropy min contradiction)~~: **RESOLVED**
- ~~C3 (Tail_decay TOST)~~: **RESOLVED**
- **Remaining**: Base-model-only limitation（不变，已充分 acknowledged）、TOST power analysis（降为 minor）、F1=0.694 moderate performance（已定位为 proof-of-concept）

### 核心判断

修改后的论文在方法论诚实度上有显著提升。三个 critical framing issues（3/1/3 partition、entropy min、tail decay）全部以恰当方式解决——不是删除分析，而是调整 claim 的 granularity 和 confidence level 以匹配 evidence。这种修改方式表明作者理解了审稿意见的核心关切。

当前主要制约因素是 scope（base-model-only）和 excitement（无 actionable downstream utility），这些是论文固有的限制而非 fixable 的 framing 问题。论文以目前状态适合 Borderline Conference 或 strong Findings——DDR 的 2-way decomposition 是 genuine insight，评估极为彻底，framing 现在 match 了 evidence。

**建议**：如果在 camera-ready 前能补充 TOST formal power analysis（即使仅作为附录脚注），并将 Contribution 3 的 headline number 改为 0.694，论文将在所有 reviewer 关切上达到完全解决状态。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 2584 · 2026-05-20T17:27:17.792329+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director"
}
```

</details>

---


## Round 223

## Round 223

2 recorded events


### User

_source line 2585 · 2026-05-20T17:27:20.368463+00:00_

[Reviewer 1 审稿结果]:
Round 2 修订验证报告已提交。

**结果摘要**：
- 11 条 issues 中 **9 条 RESOLVED**，1 条 STILL_OPEN（TOST power analysis，已降为 minor），1 条 PARTIALLY RESOLVED（缺失引用——orphan bib 已修复，不可验证的引用合理地未添加）
- 无重大新问题引入
- **Overall 从 3.0 上调至 3.5（Borderline Conference）**——核心 framing 改进（2-way split 为主、boundary feature 标签、proof-of-concept 定位）使 claim 与 evidence 匹配度显著提升

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 2586 · 2026-05-20T17:27:25.413746+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director"
}
```

</details>

---


## Round 224

## Round 224

6 recorded events


### User

_source line 2587 · 2026-05-20T17:28:29.695055+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 — Round 2 修订评估

**上轮评分**: 3.0 (Findings) → **本轮评分**: 3.5 (Borderline Conference)

### 逐条验证结果

| Issue | Status | 简要理由 |
|-------|--------|---------|
| R32-N1 DDR novelty | ✅ RESOLVED | "what converges vs what is preserved" framing + 可测试预测 + 实验验证 |
| R29-N2 Downstream null | ✅ RESOLVED | Abstract 完全移除 downstream claim；Appendix M 坦诚呈现 null result |
| R29-N4 QLoRA gap | ✅ RESOLVED | Contribution 3 = "Proof-of-concept classifier"；QLoRA 定位为 confirming richer signal |
| R32-W1 "Detecting" in title | ✅ RESOLVED | Body text 3 处明确 "proof-of-concept"；"Detecting" 可读为 task definition |
| R29-W4 2-way partition | ✅ RESOLVED | §4.2 "The primary partition is binary" + k=3 degradation |
| R32-N2 Entropy min boundary | ✅ RESOLVED | 明确标注 "boundary feature" + gen-0/gen-1 transition 机制 |
| R32-N3 Tail_decay TOST 4/8 | ✅ RESOLVED | 主文 "genuine boundary case" + reclassification robustness check |
| R29-W5 Baseline fairness | ✅ RESOLVED | Table 2 诚实展示 4-det+surface > ours > 4-det；DDR 价值锚定在分析 |
| R29-W2 Cross-model confound | ✅ RESOLVED | Footnote "not directly comparable" + single-gen transfer 控制 |
| R32-W2 TOST power | ✅ RESOLVED | SESOI justification + ε sensitivity + high-N masking 承认 |
| R29-W6 Missing refs | ⚠️ STILL_OPEN (minor) | self_refine 已删；Wang et al. (ACL 2025) attractor cycles 仍缺 |

### 上调理由
Novelty framing、downstream honesty、classifier positioning、statistical transparency 四维度均有实质改善。

### 未上调至 4.0 的原因
(1) Base-model-only 限制仍严重约束实际影响力
(2) Wang et al. (ACL 2025) "Unveiling Attractor Cycles" 仍缺
(3) 缺少 shape invariance vs pure diversity decline 的直接消融

### 新问题
无重大新问题。"What converges vs what is preserved" 重复 4+ 次略显密集；Table 1 vs Table 2 的 pooled vs macro 差异可更显式说明。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 2588 · 2026-05-20T17:29:01.037621+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "text": "Reviewer 2 Round 2 验证结果摘要。请仅对两个分歧点回应 [AGREE] 或 [REBUT]：\n\n**分歧 1: R32-W2 TOST power analysis**\n- R2 判断: ✅ RESOLVED — SESOI justification (d=0.20 + LOFO ≤1.5pp 联动) + ε sensitivity analysis + 主文 high-N masking 承认，足以让读者判断 TOST 结论的信息量。\n- 你的判断: ❌ STILL_OPEN (minor) — 缺少 formal power calculation。\n- 你同意 R2 的 RESOLVED 判断吗？还是维持 STILL_OPEN？\n\n**分歧 2: R29-W6 Missing references — Wang et al. (ACL 2025) \"Unveiling Attractor Cycles\"**\n- R2 判断: ⚠️ STILL_OPEN minor — 该论文确实存在且直接相关。\n- 你的判断: PARTIALLY RESOLVED — 该论文真实性无法确认。\n- 你是否能确认或否认 Wang et al. (ACL 2025) 的存在？",
  "reviewer_id": "1",
  "project": "gen-depth-fingerprint",
  "round_number": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "text": "Reviewer 2 Round 2 验证结果摘要。请仅对两个分歧点回应 [AGREE] 或 [REBUT]：\n\n**分歧 1: R32-W2 TOST power analysis**\n- R2 判断: ✅ RESOLVED — SESOI justification (d=0.20 + LOFO ≤1.5pp 联动) + ε sensitivity analysis + 主文 high-N masking 承认，足以让读者判断 TOST 结论的信息量。\n- 你的判断: ❌ STILL_OPEN (minor) — 缺少 formal power calculation。\n- 你同意 R2 的 RESOLVED 判断吗？还是维持 STILL_OPEN？\n\n**分歧 2: R29-W6 Missing references — Wang et al. (ACL 2025) \"Unveiling Attractor Cycles\"**\n- R2 判断: ⚠️ STILL_OPEN minor — 该论文确实存在且直接相关。\n- 你的判断: PARTIALLY RESOLVED — 该论文真实性无法确认。\n- 你是否能确认或否认 Wang et al. (ACL 2025) 的存在？",
    "reviewer_id": "1",
    "project": "gen-depth-fingerprint",
    "round_number": "2"
  }
}
```

</details>

---


### Tool result

_source line 2589 · 2026-05-20T17:29:06.759742+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 5722
}
```

</details>

---


### Tool call

_source line 2590 · 2026-05-20T17:29:07.011771+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "text": "Reviewer 1 Round 2 验证结果摘要。请仅对两个分歧点回应 [AGREE] 或 [REBUT]：\n\n**分歧 1: R32-W2 TOST power analysis**\n- R1 判断: ❌ STILL_OPEN (minor) — 缺少 formal power calculation（给定 n≈3500-4500, ε=0.20，区分 d=0.10 vs d=0.20 的 power）。\n- 你的判断: ✅ RESOLVED — SESOI + ε sensitivity 足够。\n- 你维持 RESOLVED 还是同意 R1 应补充 formal power？\n\n**分歧 2: R29-W6 Missing references — Wang et al. (ACL 2025) \"Unveiling Attractor Cycles\"**\n- R1 判断: PARTIALLY RESOLVED — 无法确认该论文存在，不应因未验证的引用判为未修复。\n- 你的判断: ⚠️ STILL_OPEN — 该论文确实存在且直接相关。\n- 请提供 Wang et al. (ACL 2025) 的具体信息（DOI、arXiv ID、或完整作者列表）以便验证。",
  "reviewer_id": "2",
  "project": "gen-depth-fingerprint",
  "round_number": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "text": "Reviewer 1 Round 2 验证结果摘要。请仅对两个分歧点回应 [AGREE] 或 [REBUT]：\n\n**分歧 1: R32-W2 TOST power analysis**\n- R1 判断: ❌ STILL_OPEN (minor) — 缺少 formal power calculation（给定 n≈3500-4500, ε=0.20，区分 d=0.10 vs d=0.20 的 power）。\n- 你的判断: ✅ RESOLVED — SESOI + ε sensitivity 足够。\n- 你维持 RESOLVED 还是同意 R1 应补充 formal power？\n\n**分歧 2: R29-W6 Missing references — Wang et al. (ACL 2025) \"Unveiling Attractor Cycles\"**\n- R1 判断: PARTIALLY RESOLVED — 无法确认该论文存在，不应因未验证的引用判为未修复。\n- 你的判断: ⚠️ STILL_OPEN — 该论文确实存在且直接相关。\n- 请提供 Wang et al. (ACL 2025) 的具体信息（DOI、arXiv ID、或完整作者列表）以便验证。",
    "reviewer_id": "2",
    "project": "gen-depth-fingerprint",
    "round_number": "2"
  }
}
```

</details>

---


### Tool result

_source line 2591 · 2026-05-20T17:29:08.372300+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1360
}
```

</details>

---


### Assistant

_source line 2592 · 2026-05-20T17:29:13.428222+00:00_

交叉分享已发送，等待两位 Reviewer 对分歧点的回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director"
}
```

</details>

---


## Round 225

## Round 225

2 recorded events


### User

_source line 2593 · 2026-05-20T17:29:15.993963+00:00_

[Reviewer 2 审稿结果]:
审稿报告已提交。总结：11 条 issue 中 **10 条 RESOLVED**，**1 条 STILL_OPEN**（Wang et al. ACL 2025 缺失引用，已降级为 minor）。Overall Assessment 从 3.0 (Findings) **上调至 3.5 (Borderline Conference)**。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 2594 · 2026-05-20T17:29:23.069839+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director"
}
```

</details>

---


## Round 226

## Round 226

2 recorded events


### User

_source line 2595 · 2026-05-20T17:29:57.923007+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 交叉回应 — Round 2 分歧点

### 分歧 1: R32-W2 TOST power analysis
**[AGREE with R1]** — 修改为 STILL_OPEN (minor)。ε sensitivity + SESOI-LOFO 联动是好的补充，但不等价于 formal power calculation。建议 Appendix TOST 新增 1-2 句 post-hoc power statement（如 "At n=4000, ε=0.20, TOST power >99% at d≤0.10 but ~60% at d=0.15"）。

### 分歧 2: Wang et al. (ACL 2025)
**[REBUT R1]** — 该论文确实存在：
- 标题: "Unveiling Attractor Cycles in Large Language Models: A Dynamical Systems View of Successive Paraphrasing"
- 作者: Zhilin Wang, Anji Liu, Hailey Schoelkopf, Guy Van den Broeck, Yejin Choi
- 发表: ACL 2025 Main Conference Long Paper
- ACL Anthology: 2025.acl-long.624
- arXiv: 2502.15208

直接相关：研究 successive paraphrasing 的 2-period attractor cycle convergence，与本文 DDR 的 convergence 讨论和 "~3 distinguishable classes" 结论直接对话。建议在 §2.2 一句话引用即可。Severity 维持 minor。

### 最终评分维持 3.5 (Borderline Conference)，两个 minor open items 不影响总体评估。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 2596 · 2026-05-20T17:30:07.492544+00:00_

R2 交叉回应已收到：
- TOST power: 同意 R1，改为 STILL_OPEN (minor)
- Wang et al.: 提供了完整引用信息（ACL 2025, arXiv:2502.15208），维持 STILL_OPEN minor

等待 R1 的交叉回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director"
}
```

</details>

---


## Round 227

## Round 227

12 recorded events


### User

_source line 2597 · 2026-05-20T17:30:08.596444+00:00_

[Reviewer 1 审稿意见]:

## Reviewer 1 对两个分歧点的最终回应

### 分歧 1: R32-W2 TOST power analysis
**改判为 [RESOLVED]，同意 R2。**

R2 的三层论证成立：(1) SESOI d=0.20 与 LOFO ≤1.5pp F1 drop 联动（appendix_tost.tex L5-6），非 arbitrary；(2) ε sensitivity analysis 在 {0.15, 0.20, 0.25} 下验证 partition robustness；(3) results.tex L90 承认 "high pooled power can mask per-generator heterogeneity"。读者有足够信息判断 TOST 结论的 informative power。Formal power calculation 是 nice-to-have，不是 acceptance-blocking。

### 分歧 2: R29-W6 Wang et al. (ACL 2025)
**同意 R2，确认该论文真实存在。维持 STILL_OPEN minor。**

已通过 web search 验证：Wang et al. "Unveiling Attractor Cycles in Large Language Models: A Dynamical Systems View of Successive Paraphrasing"，发表于 ACL 2025 Long Papers（ACL Anthology: 2025.acl-long.624，arXiv: 2502.15208）。

该论文用动态系统理论分析 successive paraphrasing 中的 attractor cycles（2-period limit cycles），与本文 DDR 直接相关——DDR 的 location/shape 分解可视为 Wang et al. attractor dynamics 的一个细化维度。应添加到 Related Work §2.2，与 Geng et al. [markovian_chains] 和 Mohamed et al. [broken_telephone] 并列。

### 最终评分
维持 **3.5 (Borderline Conference)** 不变。两个分歧的解决不改变整体评价：10/11 issues RESOLVED，1 条 minor reference gap。论文修改质量高，framing 诚实度显著提升。


---

[Reviewer 2 审稿结果]:
已提交。两个分歧点的回应：

1. **TOST power**: 同意 R1，修改为 STILL_OPEN (minor)。建议补充 1-2 句 post-hoc power statement。
2. **Wang et al. (ACL 2025)**: 反驳 R1 的"无法确认"——已提供完整 ACL Anthology 链接 (2025.acl-long.624) 和 arXiv ID (2502.15208)，该论文确实存在且直接相关。

最终评分维持 **3.5 (Borderline Conference)**。

---

[Reviewer 1 审稿结果]:
**[AGREE with R2 — 该论文确实存在且直接相关]**

确认 Wang et al. (ACL 2025) "Unveiling Attractor Cycles in Large Language Models: A Dynamical Systems View of Successive Paraphrasing" 真实存在，发表于 [ACL 2025 Long Papers](https://aclanthology.org/2025.acl-long.624/)（arXiv: [2502.15208](https://arxiv.org/abs/2502.15208)）。

该论文研究 successive paraphrasing 中的 attractor cycle（2-period limit cycles），用动态系统理论分析 LLM 迭代生成的长期行为。与本文的关联非常直接：DDR 的 location drift + shape stability 可以被理解为 Wang et al. 的 attractor dynamics 的一个特定分解维度——他们发现 convergence to periodic states，DDR 进一步区分了 convergence 过程中 what changes (location) vs. what is preserved (shape)。

该引用应添加到 Related Work Section 2.2（Model Collapse and Iterative Generation），与已有的 Geng et al. (2026) [markovian_chains] 和 Mohamed et al. (2025) [broken_telephone] 并列。维持 R29-W6 对此引用为 STILL_OPEN minor。

---

**总结两个分歧的最终判断：**
- R32-W2 TOST power: 改判 **RESOLVED**（同意 R2）
- R29-W6 Wang et al.: 确认 **STILL_OPEN minor**（同意 R2，论文真实存在且应引用）

Overall Assessment 维持 **3.5 (Borderline Conference)** 不变——Wang et al. 的缺失是 minor reference gap，不影响评分。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 2598 · 2026-05-20T17:30:30.041467+00:00_

called mcp__agent-ml-research__get_visual_check_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_visual_check_status</summary>

```json
{
  "project": "gen-depth-fingerprint"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "tool_args": {
    "project": "gen-depth-fingerprint"
  }
}
```

</details>

---


### Tool call

_source line 2599 · 2026-05-20T17:30:30.041813+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "gen-depth-fingerprint"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "gen-depth-fingerprint"
  }
}
```

</details>

---


### Tool result

_source line 2600 · 2026-05-20T17:30:30.092301+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"done\", \"started_at\": \"2026-05-20T17:23:05.756392+00:00\", \"completed_at\": \"2026-05-20T17:26:07.117406+00:00\", \"findings\": [{\"severity\": \"critical\", \"dimension\": \"page 1-4\", \"message\": \"前4页连续纯文本，无任何 display item（figure/table/diagram）。第一个视觉锚点（Table 1）直到第5页才出现，第一个 figure 在第6页。审稿人打开 PDF 后需翻过整个 Abstract + Introduction + Related Work + 大部分 Method 才能看到第一张图表。强烈建议在第1-2页插入 framework overview 图（如 generation chain → feature extraction → DDR decomposition → classification pipeline），建立审稿人对核心方法的视觉锚定\"}, {\"severity\": \"warning\", \"dimension\": \"page 1-7\", \"message\": \"display items 分布严重不均：页1-4零个，页5-7集中了全部5个主文 display items（Table 1, Figure 1, Figure 2, Table 2, Figure 3）。页7尤其拥挤——2 figures + 1 table 挤在同一页。建议将 Figure 1 或概览图前移到第2-3页，平衡视觉节奏\"}, {\"severity\": \"warning\", \"dimension\": \"page 7\", \"message\": \"Figure 2（DDR strip plot）和 Figure 3（F1 vs inference cost）因共享页面空间而偏小，图内文字（axis labels, legend）接近可读性下限。Figure 3 的 legend 条目较密集，在 150dpi 渲染下需仔细辨认\"}, {\"severity\": \"warning\", \"dimension\": \"page 16\", \"message\": \"右栏底部约30%为空白。Table 10（temperature sensitivity）上方文本结束后页面未填满\"}, {\"severity\": \"warning\", \"dimension\": \"page 18\", \"message\": \"Figure 5（confusion matrix）和 Figure 6（per-generator performance）下方约30%页面为空白。可通过调整 float 位置或补充文字消除\"}, {\"severity\": \"warning\", \"dimension\": \"page 24\", \"message\": \"Figure 7（per-feature depth trends）下方约25%页面空白。图本身占据页面上半部分，下方留白明显\"}, {\"severity\": \"warning\", \"dimension\": \"page 33\", \"message\": \"末页（附录最后一页）底部约35%为空白，内容不足页面2/3\"}, {\"severity\": \"info\", \"dimension\": \"page 1\", \"message\": \"Title/Abstract/Author 排版整洁，符合 ACL 匿名投稿模板规范\"}, {\"severity\": \"info\", \"dimension\": \"page 5\", \"message\": \"Table 1 使用 booktabs 风格，最优结果加粗，精度一致（3位小数）。排版专业\"}, {\"severity\": \"info\", \"dimension\": \"page 6\", \"message\": \"Figure 1（strip plot with per-generator variation）清晰可读，颜色区分度好，caption 自包含。作为论文第一个 figure 传达了核心 DDR 发现，信息密度高\"}, {\"sever
…[truncated 1176 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 2601 · 2026-05-20T17:30:30.092704+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"skipped\", \"paper_pdf_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/main.pdf\", \"venue\": \"EMNLP 2026\", \"requested_at\": \"2026-05-20T15:27:36.074221+00:00\", \"reminder_hours\": 8, \"chat_id\": \"oc_dbd68d7879a81efc0c108e9844b15d0b\", \"skipped_at\": \"2026-05-20T15:27:50.184903+00:00\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2602 · 2026-05-20T17:32:25.412402+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "gen-depth-fingerprint",
  "issues_yaml": "- id: \"R29-N1\"\n  summary: \"Base-model-only scope 未在 Abstract 标注\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 29\n  last_seen_round: 32\n  mentions:\n    - {round: 29, reviewers: \"R1+R2\", note: \"共识: Abstract 必须标注 base-model scope\"}\n    - {round: 31, reviewers: \"R1+R2\", note: \"W1: Title/Abstract 仍需 base-model qualifier\"}\n    - {round: 32, reviewers: \"R1+R2\", note: \"升级: 实验设计仅覆盖 base model, 建议扩展或限定 scope\"}\n  action_items:\n    - {round: 29, action: \"Abstract 加 base (pretrained) qualifier\", assigned_to: Agent, status: done}\n    - {round: 32, action: \"Abstract/Conclusion 已有 qualifier; instruct in Discussion\", assigned_to: Director, status: done}\n  resolution: \"Abstract L3 'eight base-model generators'; L7 'restricted to base models'. Title 保持不变(Reviewer 确认). Instruct limitations fully documented.\"\n  resolution_round: 32\n\n- id: \"R29-N2\"\n  summary: \"Downstream TOST underpowered (n=3) + Abstract overclaim\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 29\n  last_seen_round: 34\n  mentions:\n    - {round: 29, reviewers: \"R1+R2\", note: \"n=3 seeds, Abstract 省略 preliminary\"}\n    - {round: 31, reviewers: \"R1+R2\", note: \"W3: TOST n=3 underpowered\"}\n    - {round: 32, reviewers: \"R1+R2\", note: \"升级为 null result: depth-aware curation 不优于 random\"}\n    - {round: 34, reviewers: \"R1+R2\", note: \"RESOLVED: Abstract 完全移除 downstream claim; Appendix M 坦诚呈现 null result\"}\n  action_items:\n    - {round: 29, action: \"Abstract 加 preliminary qualifier\", assigned_to: Agent, status: done}\n    - {round: 32, action: \"Abstract/Conclusion downstream reframing\", assigned_to: Director, status: done}\n  resolution: \"Abstract 完全移除 downstream claim. Appendix M 保留 null result 作为补充材料.\"\n  resolution_round: 34\n\n- id: \"R29-N3\"\n  summary: \"DDR 新颖性 incremental — 缺 concurrent work 系统对比表\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 29\n  last_seen_round: 31\n  mentions:\n    - {round: 29, reviewers: \"R1+R2\", note: \"区分不充分\"}\n    - {round: 31, reviewers: \"R1+R2\", note: \"W12: differentiation insufficient\"}\n  action_items:\n    - {round: 29, action: \"§2.2 加系统对比表\", assigned_to: Agent, status: done}\n  resolution: \"related_work.tex concurrent-comparison table added\"\n  resolution_round: 31\n\n- id: \"R29-N4\"\n  summary: \"QLoRA gap 削弱方法论贡献 — 需重定位\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 29\n  last_seen_round: 34\n  mentions:\n    - {round: 29, reviewers: \"R1+R2\", note: \"7-feat vs QLoRA gap\"}\n    - {round: 31, reviewers: \"R1+R2\", note: \"W4: contribution identity crisis\"}\n    - {round: 32, reviewers: \"R1+R2\", note: \"Contribution 3 仍以 classifier 为卖点\"}\n    - {round: 34, reviewers: \"R1+R2\", note: \"RESOLVED: Contribution 3 = 'Proof-of-concept classifier'; 5处一致传达分析工具定位\"}\n  action_items:\n    - {round: 29, action: \"§1 contribution 重排\", assigned_to: Agent, status: done}\n    - {round: 32, action: \"Proof-of-concept framing\", assigned_to: Director, status: done}\n  resolution: \"Intro L14 'proof of concept'; Contribution 3 'Proof-of-concept classifier with boundary analysis'; results.tex L17+L142; Discussion L11 — 五处一致.\"\n  resolution_round: 34\n\n- id: \"R29-W1\"\n  summary: \"Gemma-2-2B gen-1 F1=0.036 anomaly 解释不充分\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 29\n  last_seen_round: 31\n  mentions:\n    - {round: 29, reviewers: \"R1+R2\", note: \"挑战 DDR universality\"}\n  action_items:\n    - {round: 29, action: \"appendix_9gen_scale 扩展\", assigned_to: Agent, status: done}\n  resolution: \"appendix_9gen_scale expanded\"\n  resolution_round: 31\n\n- id: \"R29-W2\"\n  summary: \"Cross-model chain F1=0.830 可能混淆 depth signal 与 generator identity\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 29\n  last_seen_round: 34\n  mentions:\n    - {round: 29, reviewers: \"R1+R2\", note: \"sample-level CV vs LOGO 矛盾\"}\n    - {round: 31, reviewers: \"R1+R2\", note: \"W11: may be OOD artifact\"}\n    - {round: 32, reviewers: \"R1+R2\", note: \"应标为 upper bound\"}\n    - {round: 34, reviewers: \"R1+R2\", note: \"RESOLVED: footnote 'not directly comparable' + single-gen transfer control. R1 minor note: Contribution 3 仍以 0.830 为 headline\"}\n  action_items:\n    - {round: 29, action: \"results.tex 标注 exploratory\", assigned_to: Agent, status: done}\n    - {round: 32, action: \"caveats added\", assigned_to: Director, status: done}\n  resolution: \"results.tex footnote + L15 single-gen transfer. Caveats sufficient.\"\n  resolution_round: 34\n\n- id: \"R29-W3\"\n  summary: \"温度限制(t<0.9)未在 Abstract 标注\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 29\n  last_seen_round: 32\n  mentions:\n    - {round: 29, reviewers: \"R1+R2\", note: \"cross-temperature transfer 不对称\"}\n  action_items:\n    - {round: 29, action: \"Abstract 加 standard decoding qualifier\", assigned_to: Agent, status: done}\n  resolution: \"Abstract L4 'nucleus sampling (p=0.9, τ≤0.7)'\"\n  resolution_round: 31\n\n- id: \"R29-W4\"\n  summary: \"DDR partition 3/1/3 intermediate 定义不够 principled\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 29\n  last_seen_round: 34\n  mentions:\n    - {round: 29, reviewers: \"R1+R2\", note: \"ε sensitivity 未展示\"}\n    - {round: 31, reviewers: \"R1+R2\", note: \"W13: threshold arbitrary\"}\n    - {round: 32, reviewers: \"R1\", note: \"升级 Critical: k-means k=2 唯一 clean split\"}\n    - {round: 34, reviewers: \"R1+R2\", note: \"RESOLVED: §4.2 'The primary partition is binary' + k=3 degradation + 'domain-informed refinement'\"}\n  action_items:\n    - {round: 29, action: \"partition stability 分析\", assigned_to: Agent, status: done}\n    - {round: 32, action: \"Restructure §4.2: 2-way primary\", assigned_to: Director, status: done}\n  resolution: \"§4.2 leads with k=2 binary (sil=0.632); k=3 explicitly noted as quality degradation (0.499); 3/1/3 = 'domain-informed refinement'. Contribution 1 aligned.\"\n  resolution_round: 34\n\n- id: \"R29-W5\"\n  summary: \"Baseline 范围偏窄 + 比较结构性不公平\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 29\n  last_seen_round: 34\n  mentions:\n    - {round: 29, reviewers: \"R1+R2\", note: \"缺 multi-feature detector\"}\n    - {round: 31, reviewers: \"R1+R2\", note: \"Bonferroni invalidates McNemar\"}\n    - {round: 32, reviewers: \"R1\", note: \"4-det ensemble 实际优于 7-feature\"}\n    - {round: 34, reviewers: \"R1+R2\", note: \"RESOLVED: §4.3 诚实展示 4-det+surface 0.708 > ours 0.705; DDR 价值锚定在分析\"}\n  action_items:\n    - {round: 32, action: \"§4.3 reframed\", assigned_to: Director, status: done}\n  resolution: \"§4.3 L140-142 explicitly states 4-det+surface marginally exceeds 7-feature; pivots to DDR's decomposition contribution.\"\n  resolution_round: 34\n\n- id: \"R29-W6\"\n  summary: \"Related work 引用缺失 + orphan bib entries\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 29\n  last_seen_round: 34\n  mentions:\n    - {round: 29, reviewers: \"R1+R2\", note: \"RAID 未引用; orphans\"}\n    - {round: 31, reviewers: \"R1+R2\", note: \"17 orphan bib entries\"}\n    - {round: 32, reviewers: \"R1+R2\", note: \"self_refine orphan; 6 new missing refs suggested\"}\n    - {round: 34, reviewers: \"R1+R2\", note: \"self_refine 已删; Wang et al. (ACL 2025) 2025.acl-long.624 确认存在且直接相关, 仍未添加. Severity: minor\"}\n  action_items:\n    - {round: 29, action: \"RAID cite + orphan cleanup\", assigned_to: Agent, status: done}\n    - {round: 32, action: \"self_refine deleted; 6 refs under verification\", assigned_to: Agent, status: done}\n    - {round: 34, action: \"Add Wang et al. (ACL 2025) 'Unveiling Attractor Cycles in LLMs' to §2.2\", assigned_to: Agent, status: pending}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R29-W7\"\n  summary: \"Diagnostic not curative 缺具体场景\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 29\n  last_seen_round: 31\n  mentions:\n    - {round: 29, reviewers: \"R1+R2\", note: \"需要 end-to-end 应用案例\"}\n  action_items:\n    - {round: 29, action: \"Discussion 加 2 个场景\", assigned_to: Agent, status: done}\n  resolution: \"discussion.tex 两个诊断场景\"\n  resolution_round: 31\n\n- id: \"R29-W8\"\n  summary: \"Per-generator F1 变异大 (0.633-0.724)\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 29\n  last_seen_round: 31\n  mentions:\n    - {round: 29, reviewers: \"R1+R2\", note: \"generator-unknown 场景实用性受限\"}\n  action_items:\n    - {round: 29, action: \"Discussion caveat\", assigned_to: Agent, status: done}\n  resolution: \"discussion.tex '9.1pp per-generator spread'\"\n  resolution_round: 31\n\n- id: \"R32-N1\"\n  summary: \"DDR 增量新颖性不清晰 — 可能是 diversity loss / mode-seeking 的重新表述\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 32\n  last_seen_round: 34\n  mentions:\n    - {round: 32, reviewers: \"R2+R1\", note: \"DDR 可能是 diversity loss 重新表述\"}\n    - {round: 34, reviewers: \"R1+R2\", note: \"RESOLVED: 'what converges vs what is preserved' framing in Abstract, Intro, Contribution 1, Discussion — 4处一致. R1: shape stability 是新发现, mechanism decomposition 有独立价值\"}\n  action_items:\n    - {round: 32, action: \"Discussion expanded: shape stability as novel contribution\", assigned_to: Director, status: done}\n  resolution: \"Abstract L5, Intro L11, Contribution 1 L18, Discussion L19 — 'what converges vs what is preserved' framing consistently applied.\"\n  resolution_round: 34\n\n- id: \"R32-N2\"\n  summary: \"Entropy min 分类存在根本性矛盾 (|ρ|=0.40 标为 near-stationary)\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 32\n  last_seen_round: 34\n  mentions:\n    - {round: 32, reviewers: \"R1\", note: \"|ρ|=0.40 vs d=0.016 vs δ=0.354 矛盾\"}\n    - {round: 34, reviewers: \"R1+R2\", note: \"RESOLVED: 'boundary feature' label + gen-0/gen-1 transition mechanism + k=2 placement\"}\n  action_items:\n    - {round: 32, action: \"Label as boundary feature\", assigned_to: Director, status: done}\n  resolution: \"results.tex L85 'boundary feature' with full qualification; Figure 2 caption aligned.\"\n  resolution_round: 34\n\n- id: \"R32-N3\"\n  summary: \"Tail_decay near-stationary 归类仅 4/8 generator 通过 TOST (ε=0.20)\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 32\n  last_seen_round: 34\n  mentions:\n    - {round: 32, reviewers: \"R1\", note: \"50% pass rate; OLMo d=0.22\"}\n    - {round: 34, reviewers: \"R1+R2\", note: \"RESOLVED: L89-91 three-sentence coverage — 4/8 rate, OLMo named, pooled power caveat, 'genuine boundary case'\"}\n  action_items:\n    - {round: 32, action: \"Transparent reporting in main text\", assigned_to: Director, status: done}\n  resolution: \"results.tex Validation paragraph: 4/8 pass rate, OLMo d=0.22 named, pooled power caveat, reclassification robustness (<0.5pp).\"\n  resolution_round: 34\n\n- id: \"R32-W1\"\n  summary: \"分类性能 F1=0.694 定位为 detecting 但实为 proof-of-concept\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 32\n  last_seen_round: 34\n  mentions:\n    - {round: 32, reviewers: \"R1+R2\", note: \"~30% 错分率, 标题暗示可部署系统\"}\n    - {round: 34, reviewers: \"R1+R2\", note: \"RESOLVED: Discussion L11 'proof-of-concept, not a deployable system: ~30% error rate'\"}\n  action_items:\n    - {round: 32, action: \"Discussion proof-of-concept framing\", assigned_to: Director, status: done}\n  resolution: \"Intro L14, Contribution 3, Discussion L11 — all say 'proof-of-concept'.\"\n  resolution_round: 34\n\n- id: \"R32-W2\"\n  summary: \"TOST power analysis 缺失\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 32\n  last_seen_round: 34\n  mentions:\n    - {round: 32, reviewers: \"R1\", note: \"大样本 TOST 几乎总检测 equivalence\"}\n    - {round: 34, reviewers: \"R1+R2\", note: \"分歧: R1 最终 RESOLVED (SESOI+ε+caveat 足够); R2 STILL_OPEN minor (建议1-2句 post-hoc power). 共识: 不阻碍接收; camera-ready 建议补充\"}\n  action_items:\n    - {round: 32, action: \"TOST power computation\", assigned_to: Agent, status: wont_fix}\n  resolution: \"SESOI justification (d=0.20 + LOFO ≤1.5pp), ε sensitivity {0.15,0.20,0.25}, high-N masking acknowledged in results.tex L90. Formal power calc recommended for camera-ready but not blocking.\"\n  resolution_round: 34\n\n- id: \"R32-W3\"\n  summary: \"术语混淆: entropy 指代 NLL 不规范\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 32\n  last_seen_round: 32\n  mentions:\n    - {round: 32, reviewers: \"R2\", note: \"NLL 与 Shannon entropy 不同\"}\n  action_items:\n    - {round: 32, action: \"Existing clarification sufficient\", assigned_to: Director, status: wont_fix}\n  resolution: \"method.tex §3.3 L38 explicit clarification.\"\n  resolution_round: 32\n\n- id: \"R32-W4\"\n  summary: \"附录 25 页过大, 关键结果应在主文讨论\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 32\n  last_seen_round: 32\n  mentions:\n    - {round: 32, reviewers: \"R2\", note: \"25 页附录\"}\n  action_items:\n    - {round: 32, action: \"Key numbers already in main text\", assigned_to: Director, status: wont_fix}\n  resolution: \"QLoRA/instruct numbers in §4.1 and Discussion. Full tables in appendix per 8-page limit.\"\n  resolution_round: 32\n\n- id: \"R32-W5\"\n  summary: \"单一解码策略(nucleus only)\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 32\n  last_seen_round: 32\n  mentions:\n    - {round: 32, reviewers: \"R1+R2\", note: \"greedy/top-k 未验证\"}\n  action_items:\n    - {round: 32, action: \"Acknowledged as limitation\", assigned_to: Director, status: wont_fix}\n  resolution: \"Abstract scope qualifier; temperature sensitivity tested.\"\n  resolution_round: 32\n\n- id: \"R32-W6\"\n  summary: \"3-class F1=0.762 因 gen-0 共享而 misleading\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 32\n  last_seen_round: 32\n  mentions:\n    - {round: 32, reviewers: \"R1+R2\", note: \"gen-0 recall 99.4%\"}\n  action_items:\n    - {round: 32, action: \"Binary F1 is primary in Abstract\", assigned_to: Director, status: wont_fix}\n  resolution: \"Abstract uses binary F1 only; §4.1 notes gen-0 inflation.\"\n  resolution_round: 32\n\n- id: \"R32-W7\"\n  summary: \"特征选取缺乏系统性论证\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 32\n  last_seen_round: 32\n  mentions:\n    - {round: 32, reviewers: \"R1+R2\", note: \"R1 major, R2 降级 warning\"}\n  action_items:\n    - {round: 32, action: \"method.tex explains rationale\", assigned_to: Director, status: done}\n  resolution: \"method.tex §3.3 a priori selection + LOFO validation + richer-features tradeoff note.\"\n  resolution_round: 32"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "gen-depth-fingerprint",
    "issues_yaml": "- id: \"R29-N1\"\n  summary: \"Base-model-only scope 未在 Abstract 标注\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 29\n  last_seen_round: 32\n  mentions:\n    - {round: 29, reviewers: \"R1+R2\", note: \"共识: Abstract 必须标注 base-model scope\"}\n    - {round: 31, reviewers: \"R1+R2\", note: \"W1: Title/Abstract 仍需 base-model qualifier\"}\n    - {round: 32, reviewers: \"R1+R2\", note: \"升级: 实验设计仅覆盖 base model, 建议扩展或限定 scope\"}\n  action_items:\n    - {round: 29, action: \"Abstract 加 base (pretrained) qualifier\", assigned_to: Agent, status: done}\n    - {round: 32, action: \"Abstract/Conclusion 已有 qualifier; instruct in Discussion\", assigned_to: Director, status: done}\n  resolution: \"Abstract L3 'eight base-model generators'; L7 'restricted to base models'. Title 保持不变(Reviewer 确认). Instruct limitations fully documented.\"\n  resolution_round: 32\n\n- id: \"R29-N2\"\n  summary: \"Downstream TOST underpowered (n=3) + Abstract overclaim\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 29\n  last_seen_round: 34\n  mentions:\n    - {round: 29, reviewers: \"R1+R2\", note: \"n=3 seeds, Abstract 省略 preliminary\"}\n    - {round: 31, reviewers: \"R1+R2\", note: \"W3: TOST n=3 underpowered\"}\n    - {round: 32, reviewers: \"R1+R2\", note: \"升级为 null result: depth-aware curation 不优于 random\"}\n    - {round: 34, reviewers: \"R1+R2\", note: \"RESOLVED: Abstract 完全移除 downstream claim; Appendix M 坦诚呈现 null result\"}\n  action_items:\n    - {round: 29, action: \"Abstract 加 preliminary qualifier\", assigned_to: Agent, status: done}\n    - {round: 32, action: \"Abstract/Conclusion downstream reframing\", assigned_to: Director, status: done}\n  resolution: \"Abstract 完全移除 downstream claim. Appendix M 保留 null result 作为补充材料.\"\n  resolution_round: 34\n\n- id: \"R29-N3\"\n  summary: \"DDR 新颖性 incremental — 缺 concurrent work 系统对比表\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 29\n  last_seen_round: 31\n  mentions:\n    - {round: 29, reviewers: \"R1+R2\", note: \"区分不充分\"}\n    - {round: 31, reviewers: \"R1+R2\", note: \"W12: differentiation insufficient\"}\n  action_items:\n    - {round: 29, action: \"§2.2 加系统对比表\", assigned_to: Agent, status: done}\n  resolution: \"related_work.tex concurrent-comparison table added\"\n  resolution_round: 31\n\n- id: \"R29-N4\"\n  summary: \"QLoRA gap 削弱方法论贡献 — 需重定位\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 29\n  last_seen_round: 34\n  mentions:\n    - {round: 29, reviewers: \"R1+R2\", note: \"7-feat vs QLoRA gap\"}\n    - {round: 31, reviewers: \"R1+R2\", note: \"W4: contribution identity crisis\"}\n    - {round: 32, reviewers: \"R1+R2\", note: \"Contribution 3 仍以 classifier 为卖点\"}\n    - {round: 34, reviewers: \"R1+R2\", note: \"RESOLVED: Contribution 3 = 'Proof-of-concept classifier'; 5处一致传达分析工具定位\"}\n  action_items:\n    - {round: 29, action: \"§1 contribution 重排\", assigned_to: Agent, status: done}\n    - {round: 32, action: \"Proof-of-concept framing\", assigned_to: Director, status: done}\n  resolution: \"Intro L14 'proof of concept'; Contribution 3 'Proof-of-concept classifier with boundary analysis'; results.tex L17+L142; Discussion L11 — 五处一致.\"\n  resolution_round: 34\n\n- id: \"R29-W1\"\n  summary: \"Gemma-2-2B gen-1 F1=0.036 anomaly 解释不充分\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 29\n  last_seen_round: 31\n  mentions:\n    - {round: 29, reviewers: \"R1+R2\", note: \"挑战 DDR universality\"}\n  action_items:\n    - {round: 29, action: \"appendix_9gen_scale 扩展\", assigned_to: Agent, status: done}\n  resolution: \"appendix_9gen_scale expanded\"\n  resolution_round: 31\n\n- id: \"R29-W2\"\n  summary: \"Cross-model chain F1=0.830 可能混淆 depth signal 与 generator identity\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 29\n  last_seen_round: 34\n  mentions:\n    - {round: 29, reviewers: \"R1+R2\", note: \"sample-level CV vs LOGO 矛盾\"}\n    - {round: 31, reviewers: \"R1+R2\", note: \"W11: may be OOD artifact\"}\n    - {round: 32, reviewers: \"R1+R2\", note: \"应标为 upper bound\"}\n    - {round: 34, reviewers: \"R1+R2\", note: \"RESOLVED: footnote 'not directly comparable' + single-gen transfer control. R1 minor note: Contribution 3 仍以 0.830 为 headline\"}\n  action_items:\n    - {round: 29, action: \"results.tex 标注 exploratory\", assigned_to: Agent, status: done}\n    - {round: 32, action: \"caveats added\", assigned_to: Director, status: done}\n  resolution: \"results.tex footnote + L15 single-gen transfer. Caveats sufficient.\"\n  resolution_round: 34\n\n- id: \"R29-W3\"\n  summary: \"温度限制(t<0.9)未在 Abstract 标注\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 29\n  last_seen_round: 32\n  mentions:\n    - {round: 29, reviewers: \"R1+R2\", note: \"cross-temperature transfer 不对称\"}\n  action_items:\n    - {round: 29, action: \"Abstract 加 standard decoding qualifier\", assigned_to: Agent, status: done}\n  resolution: \"Abstract L4 'nucleus sampling (p=0.9, τ≤0.7)'\"\n  resolution_round: 31\n\n- id: \"R29-W4\"\n  summary: \"DDR partition 3/1/3 intermediate 定义不够 principled\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 29\n  last_seen_round: 34\n  mentions:\n    - {round: 29, reviewers: \"R1+R2\", note: \"ε sensitivity 未展示\"}\n    - {round: 31, reviewers: \"R1+R2\", note: \"W13: threshold arbitrary\"}\n    - {round: 32, reviewers: \"R1\", note: \"升级 Critical: k-means k=2 唯一 clean split\"}\n    - {round: 34, reviewers: \"R1+R2\", note: \"RESOLVED: §4.2 'The primary partition is binary' + k=3 degradation + 'domain-informed refinement'\"}\n  action_items:\n    - {round: 29, action: \"partition stability 分析\", assigned_to: Agent, status: done}\n    - {round: 32, action: \"Restructure §4.2: 2-way primary\", assigned_to: Director, status: done}\n  resolution: \"§4.2 leads with k=2 binary (sil=0.632); k=3 explicitly noted as quality degradation (0.499); 3/1/3 = 'domain-informed refinement'. Contribution 1 aligned.\"\n  resolution_round: 34\n\n- id: \"R29-W5\"\n  summary: \"Baseline 范围偏窄 + 比较结构性不公平\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 29\n  last_seen_round: 34\n  mentions:\n    - {round: 29, reviewers: \"R1+R2\", note: \"缺 multi-feature detector\"}\n    - {round: 31, reviewers: \"R1+R2\", note: \"Bonferroni invalidates McNemar\"}\n    - {round: 32, reviewers: \"R1\", note: \"4-det ensemble 实际优于 7-feature\"}\n    - {round: 34, reviewers: \"R1+R2\", note: \"RESOLVED: §4.3 诚实展示 4-det+surface 0.708 > ours 0.705; DDR 价值锚定在分析\"}\n  action_items:\n    - {round: 32, action: \"§4.3 reframed\", assigned_to: Director, status: done}\n  resolution: \"§4.3 L140-142 explicitly states 4-det+surface marginally exceeds 7-feature; pivots to DDR's decomposition contribution.\"\n  resolution_round: 34\n\n- id: \"R29-W6\"\n  summary: \"Related work 引用缺失 + orphan bib entries\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 29\n  last_seen_round: 34\n  mentions:\n    - {round: 29, reviewers: \"R1+R2\", note: \"RAID 未引用; orphans\"}\n    - {round: 31, reviewers: \"R1+R2\", note: \"17 orphan bib entries\"}\n    - {round: 32, reviewers: \"R1+R2\", note: \"self_refine orphan; 6 new missing refs suggested\"}\n    - {round: 34, reviewers: \"R1+R2\", note: \"self_refine 已删; Wang et al. (ACL 2025) 2025.acl-long.624 确认存在且直接相关, 仍未添加. Severity: minor\"}\n  action_items:\n    - {round: 29, action: \"RAID cite + orphan cleanup\", assigned_to: Agent, status: done}\n    - {round: 32, action: \"self_refine deleted; 6 refs under verification\", assigned_to: Agent, status: done}\n    - {round: 34, action: \"Add Wang et al. (ACL 2025) 'Unveiling Attractor Cycles in LLMs' to §2.2\", assigned_to: Agent, status: pending}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R29-W7\"\n  summary: \"Diagnostic not curative 缺具体场景\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 29\n  last_seen_round: 31\n  mentions:\n    - {round: 29, reviewers: \"R1+R2\", note: \"需要 end-to-end 应用案例\"}\n  action_items:\n    - {round: 29, action: \"Discussion 加 2 个场景\", assigned_to: Agent, status: done}\n  resolution: \"discussion.tex 两个诊断场景\"\n  resolution_round: 31\n\n- id: \"R29-W8\"\n  summary: \"Per-generator F1 变异大 (0.633-0.724)\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 29\n  last_seen_round: 31\n  mentions:\n    - {round: 29, reviewers: \"R1+R2\", note: \"generator-unknown 场景实用性受限\"}\n  action_items:\n    - {round: 29, action: \"Discussion caveat\", assigned_to: Agent, status: done}\n  resolution: \"discussion.tex '9.1pp per-generator spread'\"\n  resolution_round: 31\n\n- id: \"R32-N1\"\n  summary: \"DDR 增量新颖性不清晰 — 可能是 diversity loss / mode-seeking 的重新表述\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 32\n  last_seen_round: 34\n  mentions:\n    - {round: 32, reviewers: \"R2+R1\", note: \"DDR 可能是 diversity loss 重新表述\"}\n    - {round: 34, reviewers: \"R1+R2\", note: \"RESOLVED: 'what converges vs what is preserved' framing in Abstract, Intro, Contribution 1, Discussion — 4处一致. R1: shape stability 是新发现, mechanism decomposition 有独立价值\"}\n  action_items:\n    - {round: 32, action: \"Discussion expanded: shape stability as novel contribution\", assigned_to: Director, status: done}\n  resolution: \"Abstract L5, Intro L11, Contribution 1 L18, Discussion L19 — 'what converges vs what is preserved' framing consistently applied.\"\n  resolution_round: 34\n\n- id: \"R32-N2\"\n  summary: \"Entropy min 分类存在根本性矛盾 (|ρ|=0.40 标为 near-stationary)\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 32\n  last_seen_round: 34\n  mentions:\n    - {round: 32, reviewers: \"R1\", note: \"|ρ|=0.40 vs d=0.016 vs δ=0.354 矛盾\"}\n    - {round: 34, reviewers: \"R1+R2\", note: \"RESOLVED: 'boundary feature' label + gen-0/gen-1 transition mechanism + k=2 placement\"}\n  action_items:\n    - {round: 32, action: \"Label as boundary feature\", assigned_to: Director, status: done}\n  resolution: \"results.tex L85 'boundary feature' with full qualification; Figure 2 caption aligned.\"\n  resolution_round: 34\n\n- id: \"R32-N3\"\n  summary: \"Tail_decay near-stationary 归类仅 4/8 generator 通过 TOST (ε=0.20)\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 32\n  last_seen_round: 34\n  mentions:\n    - {round: 32, reviewers: \"R1\", note: \"50% pass rate; OLMo d=0.22\"}\n    - {round: 34, reviewers: \"R1+R2\", note: \"RESOLVED: L89-91 three-sentence coverage — 4/8 rate, OLMo named, pooled power caveat, 'genuine boundary case'\"}\n  action_items:\n    - {round: 32, action: \"Transparent reporting in main text\", assigned_to: Director, status: done}\n  resolution: \"results.tex Validation paragraph: 4/8 pass rate, OLMo d=0.22 named, pooled power caveat, reclassification robustness (<0.5pp).\"\n  resolution_round: 34\n\n- id: \"R32-W1\"\n  summary: \"分类性能 F1=0.694 定位为 detecting 但实为 proof-of-concept\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 32\n  last_seen_round: 34\n  mentions:\n    - {round: 32, reviewers: \"R1+R2\", note: \"~30% 错分率, 标题暗示可部署系统\"}\n    - {round: 34, reviewers: \"R1+R2\", note: \"RESOLVED: Discussion L11 'proof-of-concept, not a deployable system: ~30% error rate'\"}\n  action_items:\n    - {round: 32, action: \"Discussion proof-of-concept framing\", assigned_to: Director, status: done}\n  resolution: \"Intro L14, Contribution 3, Discussion L11 — all say 'proof-of-concept'.\"\n  resolution_round: 34\n\n- id: \"R32-W2\"\n  summary: \"TOST power analysis 缺失\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 32\n  last_seen_round: 34\n  mentions:\n    - {round: 32, reviewers: \"R1\", note: \"大样本 TOST 几乎总检测 equivalence\"}\n    - {round: 34, reviewers: \"R1+R2\", note: \"分歧: R1 最终 RESOLVED (SESOI+ε+caveat 足够); R2 STILL_OPEN minor (建议1-2句 post-hoc power). 共识: 不阻碍接收; camera-ready 建议补充\"}\n  action_items:\n    - {round: 32, action: \"TOST power computation\", assigned_to: Agent, status: wont_fix}\n  resolution: \"SESOI justification (d=0.20 + LOFO ≤1.5pp), ε sensitivity {0.15,0.20,0.25}, high-N masking acknowledged in results.tex L90. Formal power calc recommended for camera-ready but not blocking.\"\n  resolution_round: 34\n\n- id: \"R32-W3\"\n  summary: \"术语混淆: entropy 指代 NLL 不规范\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 32\n  last_seen_round: 32\n  mentions:\n    - {round: 32, reviewers: \"R2\", note: \"NLL 与 Shannon entropy 不同\"}\n  action_items:\n    - {round: 32, action: \"Existing clarification sufficient\", assigned_to: Director, status: wont_fix}\n  resolution: \"method.tex §3.3 L38 explicit clarification.\"\n  resolution_round: 32\n\n- id: \"R32-W4\"\n  summary: \"附录 25 页过大, 关键结果应在主文讨论\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 32\n  last_seen_round: 32\n  mentions:\n    - {round: 32, reviewers: \"R2\", note: \"25 页附录\"}\n  action_items:\n    - {round: 32, action: \"Key numbers already in main text\", assigned_to: Director, status: wont_fix}\n  resolution: \"QLoRA/instruct numbers in §4.1 and Discussion. Full tables in appendix per 8-page limit.\"\n  resolution_round: 32\n\n- id: \"R32-W5\"\n  summary: \"单一解码策略(nucleus only)\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 32\n  last_seen_round: 32\n  mentions:\n    - {round: 32, reviewers: \"R1+R2\", note: \"greedy/top-k 未验证\"}\n  action_items:\n    - {round: 32, action: \"Acknowledged as limitation\", assigned_to: Director, status: wont_fix}\n  resolution: \"Abstract scope qualifier; temperature sensitivity tested.\"\n  resolution_round: 32\n\n- id: \"R32-W6\"\n  summary: \"3-class F1=0.762 因 gen-0 共享而 misleading\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 32\n  last_seen_round: 32\n  mentions:\n    - {round: 32, reviewers: \"R1+R2\", note: \"gen-0 recall 99.4%\"}\n  action_items:\n    - {round: 32, action: \"Binary F1 is primary in Abstract\", assigned_to: Director, status: wont_fix}\n  resolution: \"Abstract uses binary F1 only; §4.1 notes gen-0 inflation.\"\n  resolution_round: 32\n\n- id: \"R32-W7\"\n  summary: \"特征选取缺乏系统性论证\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 32\n  last_seen_round: 32\n  mentions:\n    - {round: 32, reviewers: \"R1+R2\", note: \"R1 major, R2 降级 warning\"}\n  action_items:\n    - {round: 32, action: \"method.tex explains rationale\", assigned_to: Director, status: done}\n  resolution: \"method.tex §3.3 a priori selection + LOFO validation + richer-features tradeoff note.\"\n  resolution_round: 32"
  }
}
```

</details>

---


### Tool result

_source line 2603 · 2026-05-20T17:32:25.513504+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/review_issues.yaml\", \"bytes\": 14251}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 2604 · 2026-05-20T17:34:39.201319+00:00_

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
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
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

_source line 2605 · 2026-05-20T17:34:39.252748+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "ToolSearch",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 2606 · 2026-05-20T17:35:58.123317+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "report": "# Round 34 审稿报告（继续审稿）\n\n**论文**: Depth Fingerprinting: Detecting Recursive Generation Depth in LLM Text Chains\n**目标 Venue**: EMNLP 2026 (ARR Long Paper)\n**审稿模式**: Continue（基于 Round 33 的修订验证）\n**Reviewer**: R1（方法严谨性 + 统计验证）、R2（新颖性 + 完整性 + 写作）\n\n---\n\n## Summary\n\n本轮为修订验证审稿，基于 Round 33 提出的 11 个 in_progress issue 逐条检查论文修改情况。论文在 framing 层面做了实质性改进：DDR partition 从\"经验发现\"重新定位为\"数据驱动聚类 (k=2, silhouette=0.632)\"；分类器从\"主要贡献\"降级为\"proof-of-concept\"；entropy_min 和 tail_decay 被诚实标注为\"boundary feature\"；基线比较增加了公平性说明；novelty framing 从\"DDR 本身\"转向\"what converges vs what is preserved\"的分析视角。这些修改有效回应了 Round 33 的核心批评。\n\n**11 个 issue 验证结果**: 10 RESOLVED, 1 STILL_OPEN (minor)\n\n---\n\n## Strengths\n\n1. **Framing 改进到位**: 将 DDR partition 锚定在 k=2 聚类 (silhouette=0.632) 上，3/1/3 细分明确标注为 domain-informed refinement，解决了 post-hoc 质疑。\n2. **诚实的 proof-of-concept 定位**: Introduction L14 \"As a proof of concept\"、Discussion L11 \"~30% error rate\" 不再过度宣称分类性能。\n3. **Boundary feature 透明处理**: entropy_min (|ρ|=0.40 pooled but d=0.016 gen-1/gen-2+) 和 tail_decay (4/8 TOST) 的边界性质被充分披露。\n4. **Novelty 重新定位**: \"what converges vs what is preserved\" 的分析框架与 broken_telephone、markovian_chains 形成互补而非重复。\n5. **基线比较公平性**: 承认 4-det+surface (0.708) > 7-feature (0.705)，不再隐藏对自身不利的结果。\n6. **Limitations 全面**: base-model scope、scale boundary、temperature sensitivity、prompt-type dependency 均有充分讨论。\n\n---\n\n## Weaknesses\n\n### 仍然存在的结构性限制（非修改可解决）\n\n1. **[Major] Base-model-only scope 限制泛化价值**: instruct model F1 降至 0.338-0.667，而实际 web text 主要由 instruct/RLHF 模型生成。论文已在 Limitations 中充分讨论，但这仍是制约会议级接收的核心短板。Reviewer 共识：这是 scope limitation 而非 fatal flaw，论文对此的诚实讨论是加分项。\n\n2. **[Major] 分类性能天花板**: Binary F1=0.694 (LOGO) 在检测任务中偏低。proof-of-concept 定位缓解了期望落差，但限制了方法的实际影响力。\n\n3. **[Minor] QLoRA gap 未充分解释**: end-to-end F1=0.905 (+11.6pp) 说明 7 个手工特征丢失了大量信号，但论文未深入分析这些信号是什么，错失了 insight 机会。\n\n### 未修复的遗留问题\n\n4. **[Minor] Wang et al. (ACL 2025) 引用缺失**: \"Unveiling Attractor Cycles in LLMs\" (ACL Anthology: 2025.acl-long.624) 应加入 §2.2 Related Work，与 markovian_chains 的 attractor dynamics 讨论直接相关。（R29-W6，跨 3 轮未修复）\n\n---\n\n## Questions\n\n1. 是否考虑过将 entropy_min 从 near-stationary 组移至独立的 \"boundary\" 类别，使 DDR 成为 4-way partition？当前 3/1/3 中 entropy_min 归入 near-stationary 但 pooled |ρ|=0.40 明显偏高。\n2. QLoRA +11.6pp 的增益来源是否可通过 attention pattern 或 feature importance 分析进一步拆解？\n\n---\n\n## Missing References\n\n- **Wang et al. (ACL 2025)**: \"Unveiling Attractor Cycles in LLMs\" — 直接相关于 §2.2 attractor dynamics 讨论。(2025.acl-long.624, arXiv: 2502.15208)\n\n---\n\n## External Review\n\n未启用外部审稿。\n\n---\n\n## Visual Layout Check\n\n**状态**: 已完成\n\n关键发现：\n- **[Critical]** Pages 1-4（Introduction 至 Method 前半）无任何 display item（图/表），纯文字密度过高，建议前移 Figure 1 或增加早期可视化\n- **[Warning]** 6 项排版警告（含图表位置、空白分布等）\n- **[Info]** 9 项信息提示\n\n视觉审查为非评分项，仅供参考。\n\n---\n\n## Overall Assessment\n\n**评分: 3.5 — Borderline Conference**\n\n**评分依据**:\n\nRound 33 → Round 34 提升 0.5 分的理由：\n- DDR partition 从 post-hoc 标签升级为 data-driven clustering (k=2)，方法论严谨性显著改善\n- proof-of-concept 定位消除了性能过度宣称的问题\n- boundary feature 透明标注体现了科学诚实\n- novelty framing (\"what converges vs what is preserved\") 与相关工作形成清晰区分\n\n未达 4.0 (Conference) 的理由：\n- base-model-only scope 严重限制实际应用价值，web text 场景无法直接使用\n- Binary F1=0.694 作为 proof-of-concept 可接受，但缺乏通向 deployable system 的路径\n- DDR 作为分析框架的 novelty 中等——location drift 在 model collapse 文献中已有充分记录，shape preservation 是新贡献但效果有限\n- QLoRA gap 暗示手工特征设计的上限较低，削弱了特征工程贡献的价值\n\n**Reviewer 共识**: 两位 Reviewer 均从 Round 33 的 3.0 上调至 3.5，认可修改的实质性但维持对 scope 和性能的保留意见。交叉讨论中两个分歧点（TOST power analysis 必要性、QLoRA gap 严重程度）已达成共识。\n\n**建议**: Borderline Conference / Strong Findings。论文作为 empirical analysis 贡献了有价值的分析视角，但 scope 限制和性能天花板制约了主会议接收。若能在 camera-ready 前补充 instruct model 的初步分析路径或 QLoRA 信号分解，将增强 Conference 接收的论据。\n\n---\n\n## Detailed Comments\n\n### Issue Tracker 验证结果（11 项）\n\n| Issue ID | 问题 | 状态 | 说明 |\n|----------|------|------|------|\n| R33-W1 | Base-model scope framing | ✅ RESOLVED | Limitations 充分讨论，abstract/intro 加入 scope qualifier |\n| R33-W2 | DDR novelty vs diversity loss | ✅ RESOLVED | \"what converges vs preserved\" 框架与 concurrent work 区分 |\n| R33-W3 | 3/1/3 partition post-hoc | ✅ RESOLVED | k=2 (silhouette=0.632) 为 primary，3/1/3 为 refinement |\n| R33-W4 | entropy_min 分类矛盾 | ✅ RESOLVED | 标注为 \"boundary feature\"，|ρ|=0.40 但 d=0.016 |\n| R33-W5 | tail_decay TOST borderline | ✅ RESOLVED | 4/8 pass rate 明确报告 |\n| R33-W6 | F1=0.694 proof-of-concept | ✅ RESOLVED | \"proof of concept\" + \"~30% error rate\" 定位 |\n| R33-W7 | Downstream null result | ✅ RESOLVED | 降级处理，不作为主要贡献 |\n| R33-W8 | QLoRA gap 解释 | ✅ RESOLVED | 承认 gap 存在，框架为 \"richer representations\" |\n| R33-W9 | Baseline unfairness | ✅ RESOLVED | 承认 4-det+surface > 7-feature |\n| R33-W10 | TOST power analysis | ✅ RESOLVED | Reviewer 共识：sensitivity analysis 足够 |\n| R29-W6 | Wang et al. reference | ❌ STILL_OPEN | 跨 3 轮未添加，minor |\n\n### 跨轮趋势\n\n- Round 29-32: 初始投稿，多轮修改建立基本框架\n- Round 33: 全面重审，识别 5 Critical + 7 Major + 9 Minor，评分 3.0\n- Round 34: 修订验证，10/11 resolved，评分 3.5（+0.5）\n\n论文在 framing 和诚实度上持续改善，但 scope (base-model-only) 和 performance (F1=0.694) 的结构性限制非短期修改可解决。",
  "project": "gen-depth-fingerprint",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "3.5 — Borderline Conference",
  "review_chat_id": "oc_999770e4e57bfc6eabd12fc1f64af1ef"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "report": "# Round 34 审稿报告（继续审稿）\n\n**论文**: Depth Fingerprinting: Detecting Recursive Generation Depth in LLM Text Chains\n**目标 Venue**: EMNLP 2026 (ARR Long Paper)\n**审稿模式**: Continue（基于 Round 33 的修订验证）\n**Reviewer**: R1（方法严谨性 + 统计验证）、R2（新颖性 + 完整性 + 写作）\n\n---\n\n## Summary\n\n本轮为修订验证审稿，基于 Round 33 提出的 11 个 in_progress issue 逐条检查论文修改情况。论文在 framing 层面做了实质性改进：DDR partition 从\"经验发现\"重新定位为\"数据驱动聚类 (k=2, silhouette=0.632)\"；分类器从\"主要贡献\"降级为\"proof-of-concept\"；entropy_min 和 tail_decay 被诚实标注为\"boundary feature\"；基线比较增加了公平性说明；novelty framing 从\"DDR 本身\"转向\"what converges vs what is preserved\"的分析视角。这些修改有效回应了 Round 33 的核心批评。\n\n**11 个 issue 验证结果**: 10 RESOLVED, 1 STILL_OPEN (minor)\n\n---\n\n## Strengths\n\n1. **Framing 改进到位**: 将 DDR partition 锚定在 k=2 聚类 (silhouette=0.632) 上，3/1/3 细分明确标注为 domain-informed refinement，解决了 post-hoc 质疑。\n2. **诚实的 proof-of-concept 定位**: Introduction L14 \"As a proof of concept\"、Discussion L11 \"~30% error rate\" 不再过度宣称分类性能。\n3. **Boundary feature 透明处理**: entropy_min (|ρ|=0.40 pooled but d=0.016 gen-1/gen-2+) 和 tail_decay (4/8 TOST) 的边界性质被充分披露。\n4. **Novelty 重新定位**: \"what converges vs what is preserved\" 的分析框架与 broken_telephone、markovian_chains 形成互补而非重复。\n5. **基线比较公平性**: 承认 4-det+surface (0.708) > 7-feature (0.705)，不再隐藏对自身不利的结果。\n6. **Limitations 全面**: base-model scope、scale boundary、temperature sensitivity、prompt-type dependency 均有充分讨论。\n\n---\n\n## Weaknesses\n\n### 仍然存在的结构性限制（非修改可解决）\n\n1. **[Major] Base-model-only scope 限制泛化价值**: instruct model F1 降至 0.338-0.667，而实际 web text 主要由 instruct/RLHF 模型生成。论文已在 Limitations 中充分讨论，但这仍是制约会议级接收的核心短板。Reviewer 共识：这是 scope limitation 而非 fatal flaw，论文对此的诚实讨论是加分项。\n\n2. **[Major] 分类性能天花板**: Binary F1=0.694 (LOGO) 在检测任务中偏低。proof-of-concept 定位缓解了期望落差，但限制了方法的实际影响力。\n\n3. **[Minor] QLoRA gap 未充分解释**: end-to-end F1=0.905 (+11.6pp) 说明 7 个手工特征丢失了大量信号，但论文未深入分析这些信号是什么，错失了 insight 机会。\n\n### 未修复的遗留问题\n\n4. **[Minor] Wang et al. (ACL 2025) 引用缺失**: \"Unveiling Attractor Cycles in LLMs\" (ACL Anthology: 2025.acl-long.624) 应加入 §2.2 Related Work，与 markovian_chains 的 attractor dynamics 讨论直接相关。（R29-W6，跨 3 轮未修复）\n\n---\n\n## Questions\n\n1. 是否考虑过将 entropy_min 从 near-stationary 组移至独立的 \"boundary\" 类别，使 DDR 成为 4-way partition？当前 3/1/3 中 entropy_min 归入 near-stationary 但 pooled |ρ|=0.40 明显偏高。\n2. QLoRA +11.6pp 的增益来源是否可通过 attention pattern 或 feature importance 分析进一步拆解？\n\n---\n\n## Missing References\n\n- **Wang et al. (ACL 2025)**: \"Unveiling Attractor Cycles in LLMs\" — 直接相关于 §2.2 attractor dynamics 讨论。(2025.acl-long.624, arXiv: 2502.15208)\n\n---\n\n## External Review\n\n未启用外部审稿。\n\n---\n\n## Visual Layout Check\n\n**状态**: 已完成\n\n关键发现：\n- **[Critical]** Pages 1-4（Introduction 至 Method 前半）无任何 display item（图/表），纯文字密度过高，建议前移 Figure 1 或增加早期可视化\n- **[Warning]** 6 项排版警告（含图表位置、空白分布等）\n- **[Info]** 9 项信息提示\n\n视觉审查为非评分项，仅供参考。\n\n---\n\n## Overall Assessment\n\n**评分: 3.5 — Borderline Conference**\n\n**评分依据**:\n\nRound 33 → Round 34 提升 0.5 分的理由：\n- DDR partition 从 post-hoc 标签升级为 data-driven clustering (k=2)，方法论严谨性显著改善\n- proof-of-concept 定位消除了性能过度宣称的问题\n- boundary feature 透明标注体现了科学诚实\n- novelty framing (\"what converges vs what is preserved\") 与相关工作形成清晰区分\n\n未达 4.0 (Conference) 的理由：\n- base-model-only scope 严重限制实际应用价值，web text 场景无法直接使用\n- Binary F1=0.694 作为 proof-of-concept 可接受，但缺乏通向 deployable system 的路径\n- DDR 作为分析框架的 novelty 中等——location drift 在 model collapse 文献中已有充分记录，shape preservation 是新贡献但效果有限\n- QLoRA gap 暗示手工特征设计的上限较低，削弱了特征工程贡献的价值\n\n**Reviewer 共识**: 两位 Reviewer 均从 Round 33 的 3.0 上调至 3.5，认可修改的实质性但维持对 scope 和性能的保留意见。交叉讨论中两个分歧点（TOST power analysis 必要性、QLoRA gap 严重程度）已达成共识。\n\n**建议**: Borderline Conference / Strong Findings。论文作为 empirical analysis 贡献了有价值的分析视角，但 scope 限制和性能天花板制约了主会议接收。若能在 camera-ready 前补充 instruct model 的初步分析路径或 QLoRA 信号分解，将增强 Conference 接收的论据。\n\n---\n\n## Detailed Comments\n\n### Issue Tracker 验证结果（11 项）\n\n| Issue ID | 问题 | 状态 | 说明 |\n|----------|------|------|------|\n| R33-W1 | Base-model scope framing | ✅ RESOLVED | Limitations 充分讨论，abstract/intro 加入 scope qualifier |\n| R33-W2 | DDR novelty vs diversity loss | ✅ RESOLVED | \"what converges vs preserved\" 框架与 concurrent work 区分 |\n| R33-W3 | 3/1/3 partition post-hoc | ✅ RESOLVED | k=2 (silhouette=0.632) 为 primary，3/1/3 为 refinement |\n| R33-W4 | entropy_min 分类矛盾 | ✅ RESOLVED | 标注为 \"boundary feature\"，|ρ|=0.40 但 d=0.016 |\n| R33-W5 | tail_decay TOST borderline | ✅ RESOLVED | 4/8 pass rate 明确报告 |\n| R33-W6 | F1=0.694 proof-of-concept | ✅ RESOLVED | \"proof of concept\" + \"~30% error rate\" 定位 |\n| R33-W7 | Downstream null result | ✅ RESOLVED | 降级处理，不作为主要贡献 |\n| R33-W8 | QLoRA gap 解释 | ✅ RESOLVED | 承认 gap 存在，框架为 \"richer representations\" |\n| R33-W9 | Baseline unfairness | ✅ RESOLVED | 承认 4-det+surface > 7-feature |\n| R33-W10 | TOST power analysis | ✅ RESOLVED | Reviewer 共识：sensitivity analysis 足够 |\n| R29-W6 | Wang et al. reference | ❌ STILL_OPEN | 跨 3 轮未添加，minor |\n\n### 跨轮趋势\n\n- Round 29-32: 初始投稿，多轮修改建立基本框架\n- Round 33: 全面重审，识别 5 Critical + 7 Major + 9 Minor，评分 3.0\n- Round 34: 修订验证，10/11 resolved，评分 3.5（+0.5）\n\n论文在 framing 和诚实度上持续改善，但 scope (base-model-only) 和 performance (F1=0.694) 的结构性限制非短期修改可解决。",
    "project": "gen-depth-fingerprint",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "3.5 — Borderline Conference",
    "review_chat_id": "oc_999770e4e57bfc6eabd12fc1f64af1ef"
  }
}
```

</details>

---


### Tool result

_source line 2607 · 2026-05-20T17:36:01.716711+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_dbd68d7879a81efc0c108e9844b15d0b:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 3593
}
```

</details>

---


### Assistant

_source line 2608 · 2026-05-20T17:36:06.631120+00:00_

Round 34 审稿报告已投递。

**结果**: 3.5 — Borderline Conference（较 Round 33 的 3.0 上调 0.5 分）。10/11 issue resolved，1 个 minor（Wang et al. 引用）仍 open。报告已送达 Research Director。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director"
}
```

</details>

---


## Round 228

## Round 228

2 recorded events


### User

_source line 2609 · 2026-05-21T00:20:18.249268+00:00_

[Reviewer 1 审稿意见]:
# Dream 审稿报告 — Reviewer 1 (Method Rigor + Experimental Design)

**Dream ID**: 20260520T232427 | **Scenario**: median | **Paper**: Depth Fingerprinting (三梯度 DDR variant)

---

## 总体评分

**Overall**: 3.0 (Findings)

**一句话总结**: 实验覆盖极其全面（15/15 imagined experiments），DDR 三梯度框架比二分法更 nuanced，但 7-feature 优势边际化（+2.2pp over avg_logprob）、generator 多样性不足（5 models / 3 families）、三梯度分界缺乏原则性定义，contribution 定位于 Findings。

---

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3/5 | 统计检验设计合理（bootstrap, TOST, McNemar），但三梯度 DDR 的 moderate/strong/stationary 分界无 formal clustering 支撑；QLoRA 22pp LOGO 退化机制未解释 |
| Excitement | 2.5/5 | Ordinal depth estimation 作为任务定义有新颖性，但 avg_logprob 单指标几乎匹配 7-feature（Δ=2.2pp），削弱了 method contribution |
| Reproducibility | 4/5 | 实验细节完整（5 generator, 3 reference model, 4 domain, 3 prompt type, 多 ablation）；limitations 诚实列举 5 项 |
| Clarity | 3.5/5 | 11 页结构清晰含 7 个附录；三梯度叙事比二分法更诚实但 moderate drift 组内差异过大（|ρ| 0.18–0.52） |
| Overall | 3.0/5 | Findings 水准——DDR 现象有学术价值，但 practical significance 和 scalability 均边界化 |

---

## 维度 A: 方法与实验覆盖

### 实验覆盖评估

**15/15 imagined experiments 全部覆盖**，具体对应关系：

| # | Imagined Experiment | 论文位置 | 覆盖 |
|---|---|---|---|
| 1 | feature_ablation_and_trend | Section 4.1 DDR Analysis, Table 2 | ✓ |
| 2 | cross_generator_evaluation | Section 4.2, Table 3 (LOGO per-gen) | ✓ |
| 3 | cross_family_reference_model | Section 5.1, Table 8 | ✓ |
| 4 | downstream_utility | Section 4.6, Table 7 | ✓ |
| 5 | prompt_type_comparison | Section 5.2, Table 9 | ✓ |
| 6 | paraphrastic_comparison | Appendix G, Table 16 | ✓ |
| 7 | cross_model_chains | Section 4.4 | ✓ |
| 8 | multi_domain_seeds | Appendix F, Table 15 | ✓ |
| 9 | finer_grained_ordinal | Appendix A, Table 10 | ✓ |
| 10 | human_edit_robustness | Appendix B, Table 11 | ✓ |
| 11 | ld_score_feature | Appendix C, Table 12 | ✓ |
| 12 | end_to_end_classifier | Appendix D, Table 13 | ✓ |
| 13 | text_length_control | Appendix E, Table 14 | ✓ |
| 14 | large_scale_generator | Section 4.5, Table 6 | ✓ |
| 15 | ordinal_baseline_comparison | Section 4.3, Table 4/5 | ✓ |

实验覆盖的完整性是本文最显著的优势。每个实验均有对应的 table 和定量分析，附录覆盖了 7 个扩展方向。

### 数值一致性抽查

与 review_context.yaml expected_results 对照：
- LOGO binary F1 = 0.675 ✓（expected: 0.675）
- Cross-model binary F1 = 0.73 ✓（expected: 0.73）
- QLoRA 3-class = 0.882 ✓（expected: 0.882）
- Paraphrastic binary F1 = 0.585 ✓（expected: 0.585）
- Downstream size-matched ppl = 2.370 ✓（expected: 2.37）
- Multi-domain cross-domain LOGO = 0.665 ✓（expected: 0.665）

数值与 expected results 高度一致，实验执行忠实于实验设计。

---

## 维度 B: 新颖性与 Related Work 定位

**任务新颖性**: Ordinal depth estimation（从 binary human-vs-machine 扩展到 ordinal gen-0/1/2+ classification）是一个有价值的任务定义。Related Work 中与 model collapse 文献（Shumailov et al., 2024; Dohmatob et al., 2024）和 attractor theory（Chen et al., 2025）的对话合理。

**DDR 新颖性**: 三梯度 DDR（strong drift / moderate drift / near-stationary）比简单的 binary partition 更诚实地反映了数据。但这也意味着核心发现从"清晰的 location/shape 二分"弱化为"features 在一个连续谱上分布，大致可分三类"——后者的 novelty 和 surprise value 更低。

**与已有 detector 的关系**: avg_logprob（本质上是 NLL mean 的代理）LOGO binary F1 = 0.658，几乎匹配 7-feature 的 0.675。这暗示 depth signal 的主体是 location drift（avg_logprob 直接捕获），7-feature 的额外 surface features（hapax, TTR）仅提供 marginal gain。论文需要更坦诚地讨论这一关系——avg_logprob 不是一个 weak baseline，它几乎是 DDR location component 的直接实现。

---

## Must-Fix 问题（影响接收决定）

**N1** [critical, idea层面] 三梯度 DDR 的分界缺乏原则性标准
- 具体位置：Section 4.1 / Table 2 (DDR Gradient Classification)
- 问题：论文将 7 个 feature 划分为 strong drift (|ρ|>~0.55)、moderate drift (|ρ| 0.18–0.52)、near-stationary (|ρ|<0.10)。但 moderate drift 组内差异巨大：entropy_mean |ρ|=0.52 与 entropy_std |ρ|=0.18 相差近 3 倍。k=2 clustering 只能支撑二分法，论文未报告 k=3 的 silhouette 或任何 formal criterion 来支持三梯度划分。"Moderate drift" 更像是一个 catch-all 类别而非一个 coherent statistical group。
- 为什么影响接收：三梯度 DDR 是 Contribution 1 的核心。如果分界是 ad hoc 的，"gradient of depth sensitivity" 叙事缺乏统计基础，降为定性观察。
- 建议修改方向：(a) 报告 k=3 clustering 的 silhouette 并与 k=2 对比；(b) 给出 moderate drift 的操作化定义（如 Cohen's d + |ρ| 联合阈值）；(c) 或退回二分法并将 entropy_mean/std/min 标注为 boundary cases，以保持诚实。

**N2** [critical, idea层面] 7-Feature 实际优势边际化，practical significance 存疑
- 具体位置：Section 4.3 / Table 4 (Baseline Comparison)
- 问题：7-feature LOGO binary F1 = 0.675 vs avg_logprob 0.658，Δ=2.2pp。Bootstrap 显著（p=0.008）但 avg_logprob 的 CI 极宽 [0.540, 0.740]，覆盖了 7-feature 的点估计。在某些 generator 组合上 avg_logprob 可能等于甚至优于 7-feature。考虑到 avg_logprob 是一个无需 feature engineering 的 single metric，2.2pp 的 practical improvement 难以支撑独立的分类器 contribution。
- 为什么影响接收：论文的 Contribution 3（classifier + evaluation suite）的价值取决于 7-feature 相对于简单 baseline 的增量。若增量仅 2.2pp，reviewers 会质疑 feature engineering 的必要性。
- 建议修改方向：(a) 明确重新定位——DDR 现象本身是 contribution，分类器是 proof-of-concept 而非主要 claim；(b) 分析 avg_logprob 为何如此强（它是 DDR location component 的直接度量），将其整合进理论框架；(c) 展示 7-feature 在 avg_logprob 弱的 generator 子集上的互补优势。

**N3** [critical, idea层面] Generator 多样性不足，cross-generator claim 基础薄弱
- 具体位置：Section 3.2 / Table 3 (LOGO Per-Generator)
- 问题：仅 5 个 generator 来自 3 个 family（Pythia×2, OLMo×1, Qwen×2）。Pythia 家族与 reference model (Pythia-410M) 同源，per-gen F1 最高（0.710–0.715），Qwen3-0.6B 最低（0.620），per-gen range 达 9.5pp。缺少 Llama、Mistral 等主流架构。LOGO 的"leave-one-out"在 5 个 generator 上 effective training set 仅 4 个，统计意义受限。
- 为什么影响接收："Cross-generator generalizability" 是论文的核心卖点（Contribution 2）。5 个模型（其中 2 个同源）不足以支撑此 claim。
- 建议修改方向：(a) 补充至少 1-2 个非 Pythia/OLMo/Qwen family 的 generator；(b) 在 headline metric 旁始终报告 per-gen range（0.620–0.715）而非仅 avg；(c) 将 Section 5.1 的 multi-reference 结果提升至主文以部分缓解 Pythia bias 问题。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning, idea层面] Scale effect 动摇三梯度框架的普适性
- 具体位置：Section 4.5 / Table 6
- 问题：Qwen3-8B 的 entropy_mean |ρ| 降至 0.36（5-gen avg 0.52），逼近 near-stationary。如果 entropy_mean 在 >8B 继续衰减至 |ρ|<0.20，"moderate drift" 组失去最强成员，三梯度退化为二分（surface features drift; entropy features stationary）。论文 Limitation 3 承认了 scale 衰减但未讨论对三梯度框架本身的影响。
- 建议：在 8B 数据上重新执行 k-means clustering，报告 silhouette 是否仍支持三梯度；formal 讨论 "at what scale does moderate drift collapse into near-stationary?"

**W2** [warning, presentation层面] QLoRA LOGO 退化机制未解释
- 具体位置：Appendix D / Table 13
- 问题：QLoRA within-dist binary F1 = 0.840，LOGO binary = 0.620（-22pp drop），而 7-feature 仅 drop ~0.5pp。论文将此归为 "generator-specific overfitting" 但未分析 QLoRA 具体学到了什么 generator-specific pattern。22pp drop 本身是一个有价值的 finding——end-to-end models 在 depth estimation 上的 generalization failure——值得更深入分析。
- 建议：增加 per-generator LOGO 分析（哪个 generator 的 gap 最大？）；讨论是否是 tokenizer artifacts、positional patterns、还是 generator-specific vocabulary。

**W3** [warning, presentation层面] Downstream experiment 统计功效受限
- 具体位置：Section 4.6 / Table 7
- 问题：TOST 在 ±2% margin 下 p=0.00012（显著），但 ±1% margin 下 p=0.087（不显著）。仅 3 seeds。Main text 中 "depth-aware curation does not improve downstream quality" 对 ±1% margin 的 non-significance 未加 caveat。Depth-0-only condition (n=797) 混淆了数据量与深度质量效应。
- 建议：Main text 加入 "equivalence holds at ±2% but not ±1% margin" 的 qualifier；增加 random subsample control at n=797 以分离量与质效应。

**W4** [warning, presentation层面] Temperature operating range 过窄
- 具体位置：Section 6 Limitations Item 2
- 问题：DDR 仅在 τ∈[0.5, 0.7] 可靠，τ=0.9 崩溃。许多实际部署使用 τ=0.7–1.0。论文未报告 τ=0.8 的具体表现——这恰好是 reliable/collapse 之间的关键过渡区。
- 建议：补充 τ=0.8 的 DDR 分析和分类性能；引用 real-world temperature surveys 来论证 [0.5, 0.7] 的实际覆盖率。

**W5** [warning, presentation层面] Cross-model chains 的 framing 过度
- 具体位置：Section 4.4
- 问题：Cross-model binary F1 = 0.73 vs single-model LOGO 0.675（+5.5pp）。review_context 指出这不足以支撑 "heterogeneity amplification" 的强叙事。论文是否使用了这一 framing？如果是，5.5pp 的 amplification 仅为 moderate，且部分来源于 architecture shift 而非 depth-intrinsic signal——需将两者 disentangle。
- 建议：Framing 改为 "heterogeneous chains remain detectable with moderate amplification"，并讨论 architecture shift 与 depth drift 的混淆。

---

## 小问题（不影响接收）

- Appendix G: Paraphrastic attractor convergence depth ~2.8 的估计方法未说明（visual threshold? formal criterion?）
- Section 5.1: 三个 reference model 的 entropy_mean ρ 波动 0.44–0.52（18% relative），但论文称 DDR "robust across references"——应加 "structurally robust though magnitude varies by ~18%"
- Appendix B: LLM rephrase 实现细节不足（哪个 LLM？prompt 内容？rephrase 粒度？影响可复现性）
- Appendix F: Academic domain F1 最低（0.648）仅解释为 "specialized vocabulary"，未给出 feature-level drift 对比
- Table 3: headline LOGO binary F1 仅报告 avg，建议旁附 per-gen range（0.620–0.715）
- Appendix C: LD-Score 与 hapax_ratio 的 Spearman r=0.72，高冗余性解释充分，但 "character-level depth drift" 的理论意义可再展开

---

## 主要优势

1. **实验覆盖极其全面**：15/15 imagined experiments 全部覆盖，含 feature ablation、multi-reference validation、multi-domain、paraphrastic comparison、human edit robustness 等——在 11 页（含附录）内实现了超出 long paper 常见水平的实验密度。
2. **Negative findings 处理诚实**：downstream utility 的 null result（Table 7）、5-class resolution ceiling（Appendix A, F1≈0.495）、QLoRA LOGO 退化（Appendix D, 0.620 < 7-feat 0.675）均如实报告并讨论，增强了论文可信度。
3. **Multi-reference validation 设计优秀**：Section 5.1 使用三个不同 family 的 reference model 验证 DDR 非 Pythia artifact——LOGO F1 跨 ref 差异 <1.5pp，DDR 方向一致，tail_decay 在所有 ref 下保持 |ρ|<0.07。这是一个强 robustness check。
4. **Length confound 排除严谨**：Appendix E 通过 random subsample control at matched n 证明 F1 下降来自样本量减少而非 confound removal（length-matched 0.652 vs random subsample 0.656），方法论值得称赞。
5. **三梯度框架比二分法更诚实**：承认 entropy_mean/std/min 的 intermediate behavior 而非强行归入 drifting 或 stationary。这种 nuanced reporting 是好的科学态度，尽管三梯度的 formal 定义仍需加强。

---

## 维度 C: 整体判断

### 定位建议：Findings (3.0)

**核心判断**：论文在 median 档下提出了一个有价值的新任务（ordinal depth estimation）并提供了全面的实证分析。DDR 现象——递归生成系统性地压缩分布的 location 同时保留 shape——是一个有学术价值的发现，即使三梯度形式下 boundary 更模糊。

**接收障碍**：
1. **Practical significance 边界化**：7-feature vs avg_logprob 仅 +2.2pp，method contribution 的增量难以单独支撑 conference paper
2. **Generator diversity 不足**：5 models / 3 families，Pythia family bias 未充分控制
3. **Three-gradient boundary 缺 formal 支撑**：核心 claim 的操作化定义不清

**升至 3.5 (Borderline Conference) 的条件**：
- 补充 1-2 个非 Pythia/OLMo/Qwen generator 并报告 updated LOGO
- 给出三梯度的 formal clustering 或 threshold 标准
- 将 avg_logprob 的近似等效性整合进 DDR 理论（"avg_logprob 是 location drift 的直接度量"）而非仅作为被超越的 baseline

**idea 层面 vs presentation 层面问题分布**：
- idea 层面 (hard to fix): N1 (三梯度 boundary), N2 (marginal advantage), N3 (generator coverage), W1 (scale fragility) — 4 个
- presentation 层面 (fixable): W2 (QLoRA analysis), W3 (downstream caveat), W4 (temperature), W5 (cross-model framing) — 4 个

idea 层面问题数量较多，其中 N2 和 N3 在 median 档下是结构性的（分别由 moderate DDR signal strength 和 limited generator pool 决定），仅靠修改论文难以根本解决。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 2610 · 2026-05-21T00:20:51.963886+00:00_

Round 34 审稿报告已于上一步提交完毕（Overall 3.5 — Borderline Conference）。

这份 "Dream 审稿报告" 与当前论文版本存在多处不一致：

| 项目 | Dream 报告 | 当前论文 |
|------|-----------|---------|
| Generator 数量 | 5 个 / 3 families | 8 个 / 5 families |
| LOGO binary F1 | 0.675 | 0.694 |
| DDR 框架 | 三梯度 (strong/moderate/near-stationary) | 2-way primary (k=2, silhouette=0.632) + 3/1/3 refinement |
| 7-feat vs avg_logprob Δ | 2.2pp | 不同数值 |

这份报告描述的是一个 **不同版本/scenario 的论文**（标注为 "Scenario: median, 三梯度 DDR variant"），不适用于当前已审稿的版本。

如需启动新一轮审稿，请通过标准提交流程（`[Round N - 继续审稿]` 或 `🚀 审稿阶段已启动`）触发。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director"
}
```

</details>

---


## Round 229

## Round 229

2 recorded events


### User

_source line 2611 · 2026-05-21T00:20:54.590972+00:00_

[Reviewer 1 审稿结果]:
Dream 审稿报告已提交。

**总结**：Dream 论文（median scenario）获评 **3.0 (Findings)**。15/15 实验全部覆盖、negative findings 处理诚实是主要优势。三个 critical issues 均为 idea 层面：三梯度 DDR 分界无 formal 标准、7-feature 优势仅 +2.2pp over avg_logprob、5 generators / 3 families 的多样性不足以支撑 cross-generator claim。四个 should-fix 为 presentation 层面（QLoRA 退化分析、downstream caveat、温度范围、cross-model framing）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 2612 · 2026-05-21T00:21:15.460749+00:00_

Round 34 审稿报告已于上一步成功投递（Overall 3.5 — Borderline Conference）。

Reviewer 1 的 Dream 审稿报告（median scenario, Overall 3.0）已收到，但该报告审查的是一个假设情境下的论文版本（5 generators / 3 families、三梯度 DDR、LOGO binary F1=0.675），与当前实际论文（8 generators / 5 families、k=2 primary partition、LOGO binary F1=0.694）存在显著差异。

本轮审稿已完成，报告已投递。无待办事项。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director"
}
```

</details>

---


## Round 230

## Round 230

58 recorded events


### User

_source line 2613 · 2026-05-21T02:29:11.932922+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: gen-depth-fingerprint
- 论文路径: /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: ARR
- 截止日期: 2026-05-25

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 2614 · 2026-05-21T02:29:18.054392+00:00_

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
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 2615 · 2026-05-21T02:29:18.105509+00:00_

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
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 2616 · 2026-05-21T02:29:26.185395+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__read_project_file",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__read_project_file",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 2617 · 2026-05-21T02:29:26.185869+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 2618 · 2026-05-21T02:29:35.985147+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_project_file,WebSearch",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_project_file,WebSearch",
    "max_results": "2"
  }
}
```

</details>

---


### Tool result

_source line 2619 · 2026-05-21T02:29:36.035704+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2620 · 2026-05-21T02:29:41.376348+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "gen-depth-fingerprint"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "gen-depth-fingerprint"
  }
}
```

</details>

---


### Tool result

_source line 2621 · 2026-05-21T02:29:43.435305+00:00_

{"result":"# 项目 gen-depth-fingerprint 概况\n\n## 实验状态 (66 个)\n\n- **plan-015**: DONE (success) — \n- **plan-004**: DONE (failed) — \n- **plan-003**: DONE (success) — \n- **plan-013**: DONE (success) — \n- **plan-002**: DONE (success) — \n- **plan-002-qwen17b-retry-s1**: DONE (failed) — \n- **plan-002-qwen17b-retry-s0**: DONE (failed) — \n- **plan-002-qwen06b-s1**: DONE (failed) — \n- **plan-002-qwen06b-s0**: DONE (failed) — \n- **plan-002-qwen17b-s1**: DONE (failed) — \n- **plan-002-qwen17b-s0**: DONE (failed) — \n- **plan-002-qwen3-1_7b-s0**: DONE (failed) — \n- **plan-002-qwen3-1_7b-s1**: DONE (killed) — \n- **plan-001**: DONE (success) — \n- **mvp-001**: DONE (success) — \n\n## 最新报告\n# Handover — 2026-05-21\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n（无）\n\n## 近期结论\n- **plan-004-prep** (success): Downstream utility 准备：depth-stratified 数据集 + OLMo-1B fine-tuning 脚本（不开跑，等 Director 确认）\n- **review-exp-a-baseline-ensemble** (killed): 审稿回应实验A：4-baseline ensemble + 统一超参对比，验证 7-feature vs 4-baseline vs 6-feature 在公平条件下的性能差异\n- **multi_domain_t07** (killed): —\n\n## 趋势\n成功 47 / 负向 2 / 失败 12 / 共 66\n\n## 下一步\n（无活跃 idea，请通过 ideas.md 添加）\n\n## 资源状态\nbjb2-18868: 无 GPU 信息\n\n## 告警\n- mvp-001-gen-s0: 已被终止 — unknown\n- mvp-001-gen-s1: 训练失败 — unknown\n- mvp-001-gen-s2: 训练失败 — unknown\n- mvp-001-gen-s3: 训练失败 — unknown\n- plan-001-restore: 已被终止 — unknown\n- plan-002-qwen3-1_7b-s0: 训练失败 — unknown\n- plan-002-qwen3-1_7b-s1: 已被终止 — unknown\n- plan-002-qwen17b-s0: 训练失败 — unknown\n- plan-002-qwen17b-s1: 训练失败 — unknown\n- plan-002-qwen17b-retry-s0: 训练失败 — unknown\n- plan-002-qwen17b-retry-s1: 训练失败 — unknown\n- plan-002-qwen06b-s0: 训练失败 — unknown\n- plan-002-qwen06b-s1: 训练失败 — unknown\n- plan-004: 训练失败 — unknown\n- review-exp-a-baseline-ensemble: 已被终止 — unknown\n- multi_domain_t07: 已被终止 — unknown\n- exp_050_temp_curve_t09: 训练失败 — unknown"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 2058
}
```

</details>

---


### Tool call

_source line 2622 · 2026-05-21T02:29:43.786929+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/main.tex /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/main.pdf 2>&1",
  "description": "Check paper files exist"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/main.tex /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/main.pdf 2>&1",
    "description": "Check paper files exist"
  }
}
```

</details>

---


### Tool result

_source line 2623 · 2026-05-21T02:29:44.741200+00:00_

-rw-r--r-- 1 ubuntu ubuntu 2572894 May 21 02:20 /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/main.pdf
-rw-r--r-- 1 ubuntu ubuntu    3707 May 20 23:22 /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/main.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Bash",
  "elapsed_ms": 954
}
```

</details>

---


### Tool call

_source line 2624 · 2026-05-21T02:29:44.791713+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 call for papers ARR submission guidelines author guidelines site:aclweb.org"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 call for papers ARR submission guidelines author guidelines site:aclweb.org"
  }
}
```

</details>

---


### Tool call

_source line 2625 · 2026-05-21T02:29:44.892466+00:00_

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
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
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

_source line 2626 · 2026-05-21T02:29:45.093845+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "ToolSearch",
  "elapsed_ms": 201
}
```

</details>

---


### Tool result

_source line 2627 · 2026-05-21T02:29:57.514543+00:00_

Web search results for query: "EMNLP 2026 call for papers ARR submission guidelines author guidelines site:aclweb.org"

Links: [{"title":"[EMNLP 2025] First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2025-first-call-papers"},{"title":"EACL 2026: First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eacl-2026-first-call-papers"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"Joint Call for Tutorial Proposals (EACL/ACL) 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-eaclacl-2026"},{"title":"Workshop on Multimodal Interaction in Face-to-Face Dialogue (MINT @ EMNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/workshop-multimodal-interaction-face-face-dialogue-mint-emnlp-2026"},{"title":"Call for Papers: The 20th Linguistic Annotation Workshop (LAW XX), co-located with ACL 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/call-papers-20th-linguistic-annotation-workshop-law-xx-co-located-acl-2026"},{"title":"First Call for Papers – EACL 2026 Student Research Workshop (SRW) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/first-call-papers-eacl-2026-student-research-workshop-srw"},{"title":"EACL/ACL 2026 Joint Call for Workshops | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eaclacl-2026-joint-call-workshops"},{"title":"EMNLP 2024: Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2024-call-papers"},{"title":"The 6th Trustworthy NLP Workshop at ACL 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/6th-trustworthy-nlp-workshop-acl-2026"}]

I found information about EMNLP 2025, but the search didn't return specific results for an EMNLP 2026 main conferenc
…[truncated 4077 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "WebSearch",
  "elapsed_ms": 12722
}
```

</details>

---


### Tool call

_source line 2628 · 2026-05-21T02:30:04.641393+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 submission format page limit template double blind anonymity ARR 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 submission format page limit template double blind anonymity ARR 2026"
  }
}
```

</details>

---


### Tool call

_source line 2629 · 2026-05-21T02:30:06.699394+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/review_issues.yaml 2>&1 || echo \"FILE_NOT_FOUND\"",
  "description": "Check existing review issues tracker"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/review_issues.yaml 2>&1 || echo \"FILE_NOT_FOUND\"",
    "description": "Check existing review issues tracker"
  }
}
```

</details>

---


### Tool result

_source line 2630 · 2026-05-21T02:30:07.654604+00:00_

- id: "R29-N1"
  summary: "Base-model-only scope 未在 Abstract 标注"
  category: framing
  severity: critical
  status: resolved
  first_raised_round: 29
  last_seen_round: 32
  mentions:
    - {round: 29, reviewers: "R1+R2", note: "共识: Abstract 必须标注 base-model scope"}
    - {round: 31, reviewers: "R1+R2", note: "W1: Title/Abstract 仍需 base-model qualifier"}
    - {round: 32, reviewers: "R1+R2", note: "升级: 实验设计仅覆盖 base model, 建议扩展或限定 scope"}
  action_items:
    - {round: 29, action: "Abstract 加 base (pretrained) qualifier", assigned_to: Agent, status: done}
    - {round: 32, action: "Abstract/Conclusion 已有 qualifier; instruct in Discussion", assigned_to: Director, status: done}
  resolution: "Abstract L3 'eight base-model generators'; L7 'restricted to base models'. Title 保持不变(Reviewer 确认). Instruct limitations fully documented."
  resolution_round: 32

- id: "R29-N2"
  summary: "Downstream TOST underpowered (n=3) + Abstract overclaim"
  category: experiment
  severity: critical
  status: resolved
  first_raised_round: 29
  last_seen_round: 34
  mentions:
    - {round: 29, reviewers: "R1+R2", note: "n=3 seeds, Abstract 省略 preliminary"}
    - {round: 31, reviewers: "R1+R2", note: "W3: TOST n=3 underpowered"}
    - {round: 32, reviewers: "R1+R2", note: "升级为 null result: depth-aware curation 不优于 random"}
    - {round: 34, reviewers: "R1+R2", note: "RESOLVED: Abstract 完全移除 downstream claim; Appendix M 坦诚呈现 null result"}
  action_items:
    - {round: 29, action: "Abstract 加 preliminary qualifier", assigned_to: Agent, status: done}
    - {round: 32, action: "Abstract/Conclusion downstream reframing", assigned_to: Director, status: done}
  resolution: "Abstract 完全移除 downstream claim. Appendix M 保留 null result 作为补充材料."
  resolution_round: 34

- id: "R29-N3"
  summary: "DDR 新颖性 incremental — 缺 concurrent work 系统对比表"
  category: framing
  severity: critical
  status: resolved
  first_raised_round: 29
  last_seen_round: 31
  mentions:
    - {round: 29, reviewers: "R1+R2", note: "区分
…[truncated 14241 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Bash",
  "elapsed_ms": 955
}
```

</details>

---


### Tool call

_source line 2631 · 2026-05-21T02:30:07.655085+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/config.yaml 2>&1 | head -80",
  "description": "Check project config for external review settings"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/config.yaml 2>&1 | head -80",
    "description": "Check project config for external review settings"
  }
}
```

</details>

---


### Tool result

_source line 2632 · 2026-05-21T02:30:07.755723+00:00_

cat: /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/config.yaml: No such file or directory

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Bash",
  "elapsed_ms": 100
}
```

</details>

---


### Tool result

_source line 2633 · 2026-05-21T02:30:11.721812+00:00_

Web search results for query: "EMNLP 2026 submission format page limit template double blind anonymity ARR 2026"

Links: [{"title":"EMNLP 2026 LaTeX Template | ACL Style Files & Overleaf | Underleaf","url":"https://www.underleaf.ai/templates/emnlp"},{"title":"Call for Papers: EMNLP 2026 Industry Track - EMNLP 2026","url":"https://2026.emnlp.org/calls/industry_track/"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"EMNLP: Empirical Methods in Natural Language Processing 2027 2026 2025 ...","url":"http://www.wikicfp.com/cfp/program?id=883"},{"title":"Submission Guide","url":"https://nlp4climate.github.io/submissionguide/"},{"title":"EMNLP 2026 Conference | OpenReview","url":"https://openreview.net/group?id=EMNLP%2F2026%2FConference"},{"title":"Confs: 2026 Conference on Empirical Methods in Natural ...","url":"https://www.facebook.com/linguistlist/posts/confs-2026-conference-on-empirical-methods-in-natural-language-processing-emnlp-/1351983883622556/"},{"title":"Application","url":"https://www.eeml.eu/application"}]

Based on the search results, here's information about EMNLP 2026 submission format requirements:

## EMNLP 2026 Main Conference Submission Format

The format is two-column with an 8-page limit for long papers and a 4-page limit for short papers. The mandatory Limitations section is required, placed after the conclusion.

## Double-Blind Anonymity

Industry Track submissions must neither include the authors' names nor their affiliations. The search results also indicate that papers must not include authors' names and affiliations for ARR (ACL Rolling Review) submissions, which aligns with the general double-blind review
…[truncated 752 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "WebSearch",
  "elapsed_ms": 7080
}
```

</details>

---


### Tool call

_source line 2634 · 2026-05-21T02:30:21.911773+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint -name \"*.yaml\" -path \"*/config*\" 2>/dev/null; find /home/ubuntu/.agent-ml-research-idea_gen_0514_3 -maxdepth 2 -name \"config.yaml\" 2>/dev/null; find /home/ubuntu/.agent-ml-research-idea_gen_0514_3 -maxdepth 1 -name \"*.yaml\" 2>/dev/null | head -10",
  "description": "Find project config file"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint -name \"*.yaml\" -path \"*/config*\" 2>/dev/null; find /home/ubuntu/.agent-ml-research-idea_gen_0514_3 -maxdepth 2 -name \"config.yaml\" 2>/dev/null; find /home/ubuntu/.agent-ml-research-idea_gen_0514_3 -maxdepth 1 -name \"*.yaml\" 2>/dev/null | head -10",
    "description": "Find project config file"
  }
}
```

</details>

---


### Tool result

_source line 2635 · 2026-05-21T02:30:21.962402+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_3/workspace.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2636 · 2026-05-21T02:30:22.013045+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"ACL Rolling Review\" 2026 submission guidelines page limit long paper short paper format"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"ACL Rolling Review\" 2026 submission guidelines page limit long paper short paper format"
  }
}
```

</details>

---


### Tool result

_source line 2637 · 2026-05-21T02:30:28.454768+00:00_

Web search results for query: ""ACL Rolling Review" 2026 submission guidelines page limit long paper short paper format"

Links: [{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"Paper formatting guidelines - ACLPUB","url":"https://acl-org.github.io/ACLPUB/formatting.html"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"},{"title":"ACL Rolling Review | ACL Member Portal","url":"https://www.aclweb.org/portal/content/acl-rolling-review"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"EACL 2026: First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eacl-2026-first-call-papers"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"}]

Based on the search results, here's the information about ACL Rolling Review 2026 submission guidelines:

## Page Limits

All ARR submissions are anonymous and in the format of a short paper (up to 4 pages) or long paper (up to 8 pages).

More specifically:
- **Long Papers**: Review versions of long papers may have up to eight (8) pages of content plus unlimited pages for
…[truncated 893 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "WebSearch",
  "elapsed_ms": 6441
}
```

</details>

---


### Tool call

_source line 2638 · 2026-05-21T02:30:32.875273+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/workspace.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/workspace.yaml"
  }
}
```

</details>

---


### Tool result

_source line 2639 · 2026-05-21T02:30:32.926320+00:00_

1	projects: {}
2	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 2640 · 2026-05-21T02:30:37.442900+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint -name \"*.yaml\" -o -name \"*.yml\" 2>/dev/null | grep -i config | head -10; find /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint -maxdepth 1 -name \"*.yaml\" -o -name \"*.yml\" 2>/dev/null | head -10",
  "description": "Find config files in project"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint -name \"*.yaml\" -o -name \"*.yml\" 2>/dev/null | grep -i config | head -10; find /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint -maxdepth 1 -name \"*.yaml\" -o -name \"*.yml\" 2>/dev/null | head -10",
    "description": "Find config files in project"
  }
}
```

</details>

---


### Tool result

_source line 2641 · 2026-05-21T02:30:37.543690+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/dream_registry.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/writing_plan.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/paper_provenance.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/literature_map.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/registry.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/constraints.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/mistakes.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/decisions.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/experiment_plan.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Bash",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 2642 · 2026-05-21T02:30:48.764600+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -r \"external_review\\|paperreview\" /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/ --include=\"*.yaml\" --include=\"*.yml\" 2>/dev/null | head -5; grep -r \"external_review\\|paperreview\" /home/ubuntu/.agent-ml-research-idea_gen_0514_3/ --include=\"*.yaml\" --include=\"*.yml\" -l 2>/dev/null | head -5",
  "description": "Search for external review config"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -r \"external_review\\|paperreview\" /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/ --include=\"*.yaml\" --include=\"*.yml\" 2>/dev/null | head -5; grep -r \"external_review\\|paperreview\" /home/ubuntu/.agent-ml-research-idea_gen_0514_3/ --include=\"*.yaml\" --include=\"*.yml\" -l 2>/dev/null | head -5",
    "description": "Search for external review config"
  }
}
```

</details>

---


### Tool result

_source line 2643 · 2026-05-21T02:30:48.865518+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Bash",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 2644 · 2026-05-21T02:31:21.902658+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 2645 · 2026-05-21T02:31:22.404920+00:00_

1	% EMNLP 2026 ARR Submission — ACL 2023 Template
2	\documentclass[11pt]{article}
3	\usepackage[review]{acl}
4	\usepackage{times}
5	\usepackage{latexsym}
6	\usepackage[T1]{fontenc}
7	\usepackage[utf8]{inputenc}
8	\usepackage{microtype}
9	\usepackage{graphicx}
10	\usepackage{booktabs}
11	\usepackage{enumitem}
12	\usepackage{amsmath}
13	\usepackage{amssymb}
14	\usepackage{placeins}
15	\usepackage{multirow}
16	\usepackage{float}
17	
18	\graphicspath{{../chart/}}
19	
20	\title{Depth Fingerprinting: Detecting Recursive Generation Depth\\in LLM Text Chains}
21	
22	\author{Anonymous}
23	
24	\begin{document}
25	\maketitle
26	
27	\input{abstract}
28	
29	\input{introduction}
30	\input{related_work}
31	\input{method}
32	\input{results}
33	
34	\input{discussion}
35	\input{conclusion}
36	\input{limitations}
37	\input{ethics}
38	
39	\bibliography{references}
40	
41	\appendix
42	
43	\noindent\textbf{Note:} Unless otherwise stated, appendix experiments use the original six-generator subset (Pythia-2.8B/1B, OLMo-2-1B, Qwen3-1.7B/0.6B/8B).
44	Main paper results (\S\ref{sec:results}) use the full eight-generator set (adding Llama-3.2-3B and Mistral-7B-v0.3).
45	
46	\input{appendix_dataset_stats}
47	
48	\section{Length Confound Analysis}
49	\label{app:length}
50	\input{appendix_length}
51	
52	\section{Prompt Type Generalization}
53	\label{app:prompt-type}
54	\input{appendix_prompt_type}
55	
56	\section{Finer-Grained Depth Classification}
57	\label{app:finer-depth}
58	\input{appendix_finer_depth}
59	
60	\section{End-to-End Depth Classification (QLoRA)}
61	\label{app:qlora}
62	\input{appendix_qlora}
63	
64	\section{Leave-One-Feature-Out Analysis}
65	\label{app:lofo}
66	\input{appendix_lofo}
67	
68	\section{Confusion Matrix}
69	\label{app:confusion}
70	\input{appendix_confusion_matrix}
71	
72	\section{Classifier Sensitivity}
73	\label{app:classifier}
74	\input{appendix_classifier}
75	\FloatBarrier
76	
77	\section{Robustness to Text Perturbation}
78	\label{app:human-edit}
79	\input{appendi
…[truncated 2265 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 2646 · 2026-05-21T02:31:22.606058+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/*.tex 2>/dev/null",
  "description": "List all tex files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/*.tex 2>/dev/null",
    "description": "List all tex files"
  }
}
```

</details>

---


### Tool result

_source line 2647 · 2026-05-21T02:31:22.656843+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_9gen_scale.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_ablation.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_classifier.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_confusion_matrix.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_convergence.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_cross_model_detail.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_cross_temp.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_dataset_stats.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_ddr_causality.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_ddr_validation.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_domain.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_downstream.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_error_analysis.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_feature_correlation.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/ge
…[truncated 3420 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2648 · 2026-05-21T02:31:27.040013+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 2649 · 2026-05-21T02:31:27.492179+00:00_

1	% Abstract — Depth Fingerprinting of Recursive LLM Generation Chains
2	\begin{abstract}
3	When LLM outputs re-enter generation pipelines, each recursive step compresses \emph{where} text sits in distributional space while leaving \emph{how} it is shaped nearly unchanged.
4	We formalize this asymmetry as \emph{differential depth response} (DDR) and characterize it across eight base-model generators spanning five architectural families (0.6B--8B parameters): under nucleus sampling ($p{=}0.9$, $\tau \leq 0.7$), NLL location statistics and lexical diversity drift monotonically with generation depth (Cohen's $d{=}0.76$--$1.17$), while distributional shape features remain near-stationary ($d < 0.10$)---a separation validated by five independent effect-size metrics and data-driven clustering (silhouette\,=\,0.632).
5	Where prior work on iterative generation documents \emph{what converges}, the novel observation here is \emph{what is preserved}: shape invariance under the same process that compresses location provides the stable reference needed for depth estimation without per-generator calibration.
6	As a proof of concept, a lightweight 7-feature ensemble exploiting DDR achieves leak-free binary F1\,=\,0.694 under leave-one-generator-out evaluation, confirming that the decomposition yields actionable depth signal; an end-to-end classifier recovers substantially more (F1\,=\,0.905), establishing the analytical framework---not the specific features---as the primary contribution.
7	The signal attenuates under instruction tuning; current applicability is restricted to base models.
8	\end{abstract}
9	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 2650 · 2026-05-21T02:31:27.492679+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 2651 · 2026-05-21T02:31:28.446606+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	AI text detection asks a single binary question---\emph{human or machine?}---and recent methods answer it with increasing reliability \cite{detectgpt,fast_detectgpt,binoculars,ld_score}.
5	Yet this framing elides a richer structure emerging on the open web: as LLM outputs re-enter training corpora \cite{dolma,fineweb} and seed further generation, text accumulates at varying \emph{recursive depths}---an estimated 7--17\% of recent scientific publications already contain substantial LLM-modified content \cite{mapping_llm_science,monitoring_ai_review}---and each generation cycle pushes distributional properties further from both the human source and the first-generation predecessor.
6	Knowing \emph{how many times} text has been recursively generated matters for data provenance \cite{ccnet,dsir} and model collapse analysis \cite{curse_of_recursion,strong_model_collapse}, yet no current method moves beyond the binary boundary.
7	
8	We introduce \emph{depth fingerprinting}: classifying text by ordinal generation depth (gen-0\,/\,gen-1\,/\,gen-2+) and decomposing the distributional drift that accumulates across depths into structurally distinct components.
9	The core empirical finding is a \emph{differential depth response} (DDR): across eight base-model generators spanning five architectural families (0.6B--8B), the NLL distribution's central tendency (mean entropy, lexical diversity) drifts monotonically with depth while its shape (entropy extremes, tail structure) remains an order of magnitude more stable ($d{=}0.76$--$1.17$ vs.\ $d < 0.10$; five independent effect-size metrics converge on this partition).
10	This location/shape asymmetry exposes a structural property of fixed-parameter autoregressive sampling: the decoding mechanism systematically compresses where the output distribution sits while preserving its higher-order form---a pattern mechanistically distinct from the tail-coverage erosion in model collap
…[truncated 1930 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "elapsed_ms": 953
}
```

</details>

---


### Tool call

_source line 2652 · 2026-05-21T02:31:28.497214+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 2653 · 2026-05-21T02:31:28.497666+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	\subsection{Task Formulation}
5	\label{sec:task}
6	
7	Given a text $x$, we predict its \emph{generation depth} $d \in \{0, 1, 2{+}\}$: human-written ($d{=}0$), first-generation LLM output ($d{=}1$), or text produced by two or more recursive LLM generations ($d{=}2{+}$).
8	A generation chain of depth $k$ is defined recursively: $x^{(0)} \sim \mathcal{C}_0$ (human corpus), $x^{(k)} = G(x^{(k-1)})$ for $k \geq 1$, where $G$ denotes stochastic autoregressive generation.
9	Depths beyond 2 are merged into $2{+}$ because feature convergence compresses inter-class margins at deeper levels (\S\ref{sec:results-differential}).
10	
11	\subsection{Generation Chain Construction}
12	\label{sec:generation}
13	
14	We construct generation chains using eight generators spanning five model families: \textbf{Pythia} (2.8B, 1B) \cite{pythia}, \textbf{OLMo} (OLMo-2-1B) \cite{olmo}, \textbf{Qwen} (Qwen3-1.7B, Qwen3-0.6B, Qwen3-8B-Base) \cite{qwen3}, \textbf{Llama} (Llama-3.2-3B) \cite{llama3}, and \textbf{Mistral} (Mistral-7B-v0.3) \cite{mistral7b}.
15	This selection spans parameter scales from 0.6B to 8B and diverse pretraining corpora, enabling evaluation of cross-generator and cross-scale generalization.
16	
17	For each generator, we sample approximately 1{,}000 seed passages from English Wikipedia as $\mathcal{C}_0$.
18	The same pool of seed passages serves as gen-0 for all generators.
19	We use shared seeds across generators so that cross-generator comparisons control for input content and isolate the effect of the generation model from source text variation.
20	In LOGO evaluation, gen-0 samples from the held-out generator's chains also appear (with the same text) in the training generators' chains, creating a potential train--test overlap for the gen-0 class.
21	We address this with a supplementary binary evaluation excluding gen-0 entirely (\S\ref{sec:results-baselines}).
22	Each seed is iteratively fed through the generator to produce a 
…[truncated 5818 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 2654 · 2026-05-21T02:31:28.949128+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/results.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/results.tex"
  }
}
```

</details>

---


### Tool result

_source line 2655 · 2026-05-21T02:31:29.401113+00:00_

1	\section{Results}
2	\label{sec:results}
3	
4	\subsection{Depth Classification Performance}
5	\label{sec:results-classification}
6	
7	Before analyzing the DDR decomposition (\S\ref{sec:results-differential}), we establish that generation depth is classifiable across diverse architectures.
8	The 7-feature ensemble achieves 3-class LOGO F1\,=\,0.762 (95\% CI [0.758, 0.766]; $N$\,=\,37{,}058) across eight generators from five families (Table~\ref{tab:logo-results}).
9	Because gen-0 seeds are shared across generators (\S\ref{sec:generation}), gen-0 classification is near-perfect (per-class F1\,$\approx$\,0.94), inflating the 3-class metric.
10	We therefore adopt \textbf{leak-free binary F1} (gen-1 vs.\ gen-2+)\,=\,0.694 (CI [0.688, 0.700]) as the primary metric throughout: it excludes gen-0 entirely and is unaffected by seed sharing.
11	Per-generator binary F1 ranges from 0.633 (Mistral-7B) to 0.724 (Pythia-2.8B), with the primary difficulty concentrated at the gen-1\,/\,gen-2+ boundary (Appendix~\ref{app:confusion}).
12	
13	\paragraph{Cross-model generalization.}
14	Cross-model chains (randomly selected generator per step) yield binary F1\,=\,0.830 (95\% CI [.818, .841]) under 5-generator LOGO.\footnote{5-generator subset (Pythia-2.8B/1B, OLMo-2-1B, Qwen3-0.6B/1.7B); generator-level LOGO with bootstrap CIs ($n$\,=\,2{,}000). Not directly comparable to 8-generator LOGO due to differing subsets.}
15	Single-generator transfer (Appendix~\ref{app:transfer}) confirms the signal is not a mixed-chain artifact: classifiers trained on one generator transfer to all others with mean binary F1\,=\,0.810; LOFO yields 0.686.
16	A scale effect emerges: Pythia achieves the highest F1 (0.718--0.724) while larger models degrade (Mistral-7B: 0.633), partly reflecting same-family affinity with the Pythia-410M reference (cross-reference spread $\leq$0.013; \S\ref{sec:results-differential}); cross-domain signal persists with variation (Appendix~\ref{app:domain}).
17	An end-to-end QLoRA clas
…[truncated 12064 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "elapsed_ms": 451
}
```

</details>

---


### Tool call

_source line 2656 · 2026-05-21T02:31:29.401545+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 2657 · 2026-05-21T02:31:29.903617+00:00_

1	\section{Discussion}
2	\label{sec:discussion}
3	
4	Recursive generation alters \emph{where} the token-level surprise distribution sits but not \emph{how} it is shaped---a dichotomy that admits a mechanistic interpretation.
5	Under nucleus sampling, top-$p$ truncation selects from a fixed probability-mass fraction at each step, preserving the functional form of the conditional distribution regardless of input content.
6	What changes across recursive steps is the \emph{input} to this truncation: as the model conditions on its own increasingly self-typical outputs, the expected token-level NLL compresses monotonically---each generation feeds slightly more predictable input into the same shape-preserving mechanism.
7	This account yields two testable predictions: (1)~increasing sampling randomness should weaken the location drift by disrupting mode-seeking, and (2)~semantic-preservation constraints should attenuate it by anchoring the input distribution.
8	Both are empirically confirmed: at $t{=}1.0$, the location signal collapses ($\rho$: $-0.60 \to -0.002$; Appendix~\ref{app:sampling-sensitivity}); under elaboration prompts, drift weakens relative to continuation (F1\,=\,0.730 vs.\ 0.781; Appendix~\ref{app:prompt-type}), consistent with \citet{broken_telephone}, while cross-type transfer remains viable (F1\,=\,0.753).
9	Permutation importance, Granger causality, and feature intervention analyses provide further causal evidence: drifting features contribute $5.5\times$ more to classification than near-stationary ones, with 6/7 features exhibiting significant Granger causality (Appendix~\ref{app:ddr-causality}).
10	
11	The classifier is a proof-of-concept, not a deployable system: document-level gen-1 per-class F1\,=\,0.63 and ${\sim}30\%$ error rate are insufficient for automated filtering but sufficient for corpus-level auditing ($O(1/\sqrt{n})$ error scaling), with the primary difficulty being gen-1 vs.\ gen-2+ discrimination (86\% false negatives; Appendix~\ref{app
…[truncated 3980 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 2658 · 2026-05-21T02:31:29.903959+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 2659 · 2026-05-21T02:31:30.355763+00:00_

1	\section{Related Work}
2	\label{sec:related}
3	
4	\subsection{AI-Generated Text Detection}
5	\label{sec:related-detection}
6	
7	The detection literature spans statistical tests \cite{gltr,grover,release_strategies}, zero-shot scoring \cite{detectgpt,fast_detectgpt,binoculars,dna_gpt}, surprisal diversity \cite{diveye}, and learned classifiers \cite{ghostbuster,feat_aug_transformer,reliable_detection,ld_score}; see \citet{wu_survey_2025} and \citet{jawahar_survey} for surveys.
8	RAID \cite{raid} benchmarks binary detection across generators and attacks; we extend the task from binary to ordinal depth estimation.
9	Several recent efforts move beyond the binary boundary---collaboration roles \cite{beyond_binary}, joint detection-attribution \cite{two_birds}, creator-editor modes \cite{beyond_final_actor}, multi-generator attribution \cite{semeval2024_task8}---but all taxonomize by \emph{source} or \emph{production mode}, not recursive generation \emph{depth}; repurposing their scores as depth predictors reveals high cross-generator variance (binary F1\,=\,0.52--0.71; Table~\ref{tab:baselines}) \cite{paraphrase_evades,detection_possibilities}.
10	Our contribution is orthogonal: the task formulation itself (ordinal depth classification \cite{gutierrez_ordinal_survey,coral_ordinal,kasa_ordinality_nlp}) and the finding that drifting and stationary features together yield consistent cross-generator performance where individual detection scores do not \cite{uchendu_attribution,munir_looking_glass}.
11	
12	\subsection{Model Collapse and Iterative Generation}
13	\label{sec:related-collapse}
14	
15	Self-consuming generative models progressively lose distributional coverage \cite{self_consuming_mad,curse_of_recursion,seddik_synthetic_data}, though data mixing mitigates collapse \cite{model_collapse_avoidable,strong_model_collapse}.
16	These studies address \emph{training-loop} degradation where parameter updates erode tail coverage; indeed, \citet{schaeffer_collapse_position} 
…[truncated 2750 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "elapsed_ms": 451
}
```

</details>

---


### Tool call

_source line 2660 · 2026-05-21T02:31:30.556920+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 2661 · 2026-05-21T02:31:30.858424+00:00_

1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	Recursive generation leaves a systematic distributional signature: central-tendency features drift monotonically with depth while shape features remain an order of magnitude more stable---a dichotomy we formalize as differential depth response (DDR), validated across eight generators from five model families.
5	This decomposition enables cross-generator depth classification (leak-free binary F1\,=\,0.694; end-to-end: 0.905) and provides an analytical lens complementary to model collapse: fixed-parameter sampling compresses distributional location while preserving shape, whereas retraining erodes both.
6	Current boundaries are instruction tuning---where alignment reshapes the generation attractor---and frontier scale, where preliminary 14B evidence confirms the partition with attenuated effect sizes.
7	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 2662 · 2026-05-21T02:31:30.909214+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 2663 · 2026-05-21T02:31:31.010296+00:00_

1	\section*{Limitations}
2	\label{sec:limitations}
3	
4	All eight generators are base (pretrained) models.
5	This is a deliberate design choice: base models isolate the generation mechanism from instruction-tuning effects, enabling controlled study of recursive distributional drift.
6	However, web text is predominantly produced by instruction-tuned and RLHF-aligned models.
7	Preliminary instruct experiments confirm that depth signal degrades substantially under instruction tuning: OLMo-2-1B-Instruct drops to within-model 3-class F1\,=\,0.575 (vs.\ 0.754 base) and Llama-3.2-3B to 0.544 (vs.\ 0.742 base; Table~\ref{tab:instruct}).
8	Length-matched analysis yields near-zero correlations ($|\rho| < 0.02$) and binary classification near chance (F1\,$\approx$\,0.5) for Qwen models, leaving interpretation ambiguous.
9	Extending depth fingerprinting to instruct models requires addressing these confounds (length regulation, format constraints, safety-driven distribution shaping) that instruction tuning introduces.
10	
11	Our experiments include generators up to 8.2B parameters (Qwen3-8B).
12	Depth signal persists at this scale (Qwen3-8B 3-class F1\,=\,0.714), but cross-scale transfer incurs a moderate gap vs.\ $\leq$2.8B generators (F1\,=\,0.77--0.81).
13	Gemma-2-2B shows the weakest generalization among nine generators (3-class F1\,=\,0.628), with gen-1 nearly indistinguishable from other classes (per-class F1\,=\,0.036); this architecture-specific limitation is discussed in Appendix~\ref{app:9gen-scale}.
14	Frontier models (70B+) remain untested; their higher fluency may further compress feature margins.
15	
16	Differential depth response strength is prompt-type dependent: within-type 3-class F1 ranges from 0.78 (continuation) to 0.73 (elaboration), with inspired rewriting intermediate at 0.74 (Appendix~\ref{app:prompt-type}).
17	DDR is most reliably detected in continuation-style generation; near-paraphrastic settings approach the method's detection floor.
18	Cross-prompt
…[truncated 2836 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 2664 · 2026-05-21T02:32:06.053811+00:00_

called mcp__agent-ml-research__dispatch_visual_check

<details open><summary>🔧 Tool call — mcp__agent-ml-research__dispatch_visual_check</summary>

```json
{
  "project": "gen-depth-fingerprint",
  "review_chat_id": "oc_999770e4e57bfc6eabd12fc1f64af1ef"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "tool_args": {
    "project": "gen-depth-fingerprint",
    "review_chat_id": "oc_999770e4e57bfc6eabd12fc1f64af1ef"
  }
}
```

</details>

---


### Tool result

_source line 2665 · 2026-05-21T02:32:35.492781+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 29438
}
```

</details>

---


### Tool call

_source line 2666 · 2026-05-21T02:32:35.543445+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "你是 Reviewer 1，负责 **方法严谨性 + 实验设计** 审查。\n\n## 投稿信息\n- **Venue**: EMNLP 2026（通过 ARR May 2026 cycle 提交）\n- **截止日期**: 2026-05-25\n- **格式要求**: Long paper, ACL style template, 正文 ≤ 8 页 + 无限参考文献页; Limitations 必写（不计入页数限制）; 匿名双盲\n- **论文路径**: `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/main.tex`\n- **PDF**: `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/main.pdf`\n\n## 论文概要\n本文提出 \"Depth Fingerprinting\"，将 AI 文本检测从 binary (human/machine) 扩展到 ordinal depth estimation (gen-0/gen-1/gen-2+)。核心发现是 Differential Depth Response (DDR)：NLL location 特征随 generation depth 单调漂移（Cohen's d=0.76-1.17），而 shape 特征保持近稳态（d<0.10）。基于 DDR 的 7-feature XGBoost 在 8-gen LOGO 下达到 binary F1=0.694；QLoRA 达 0.905。\n\n## 你的审查侧重\n\n1. **DDR 分解有效性**：\n   - k=2 聚类 (silhouette=0.632) 是否是 principled 的特征分区方法？还是 post-hoc 的结果拟合？\n   - \"near-stationary\" 的 TOST 验证仅 4/8 (tail_decay) 或 6/8 (entropy_max) generators 通过，这个 pass rate 是否足够？\n   - entropy_min 作为 \"boundary feature\" 的处理是否合理？|ρ|=0.40 vs d=0.016 的矛盾是否被充分解释？\n   - 5 个 effect-size metrics 的一致性是真正的 convergent validation 还是高度相关指标的冗余？\n\n2. **统计检验严谨性**：\n   - TOST equivalence bound ε=0.20 的选择是否有 a priori justification？\n   - Bootstrap CI 的 sample size (n=1000) 是否足够？\n   - Bonferroni correction 的适用范围和影响\n   - 大样本下 TOST 的 power 问题（论文已承认但是否充分处理？）\n\n3. **Baseline 比较公平性**：\n   - 4-det+surface (F1=0.708) > 7-feature (0.705)，论文如何处理这个\"被超越\"的结果？\n   - 将 detection scores 作为 univariate features 是否对 baselines 不公平？（它们设计目的不是 depth classification）\n   - LOGO 评估中 gen-0 seed sharing 问题及其 leak-free binary F1 处理是否充分\n\n4. **实验设计漏洞**：\n   - 8 个 generators 全是 base model，且都 ≤8B——泛化性声明是否 overclaim？\n   - 单一 reference model (Pythia-410M) 的 same-family bias\n   - 温度固定 τ=0.7 的限制\n   - seed sharing 导致的 gen-0 data leakage 是否被完全控制？\n\n5. **消融实验**：\n   - LOFO 分析的充分性\n   - Surface-only vs Reference-only 分解的意义\n   - PCA 替代（PC1 仅损失 1.1pp）对 DDR 贡献声明的影响\n\n请按 ARR/EMNLP 标准给出完整审稿报告，包含 Summary、Strengths、Weaknesses（逐条编号，标注 severity: Critical/Major/Minor）、Questions、Missing References、Overall Assessment（使用 EMNLP 2026 评分标准：5=Award, 4=Conference, 3=Findings, 2=Resubmit, 1=Do not resubmit）。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "text": "你是 Reviewer 1，负责 **方法严谨性 + 实验设计** 审查。\n\n## 投稿信息\n- **Venue**: EMNLP 2026（通过 ARR May 2026 cycle 提交）\n- **截止日期**: 2026-05-25\n- **格式要求**: Long paper, ACL style template, 正文 ≤ 8 页 + 无限参考文献页; Limitations 必写（不计入页数限制）; 匿名双盲\n- **论文路径**: `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/main.tex`\n- **PDF**: `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/main.pdf`\n\n## 论文概要\n本文提出 \"Depth Fingerprinting\"，将 AI 文本检测从 binary (human/machine) 扩展到 ordinal depth estimation (gen-0/gen-1/gen-2+)。核心发现是 Differential Depth Response (DDR)：NLL location 特征随 generation depth 单调漂移（Cohen's d=0.76-1.17），而 shape 特征保持近稳态（d<0.10）。基于 DDR 的 7-feature XGBoost 在 8-gen LOGO 下达到 binary F1=0.694；QLoRA 达 0.905。\n\n## 你的审查侧重\n\n1. **DDR 分解有效性**：\n   - k=2 聚类 (silhouette=0.632) 是否是 principled 的特征分区方法？还是 post-hoc 的结果拟合？\n   - \"near-stationary\" 的 TOST 验证仅 4/8 (tail_decay) 或 6/8 (entropy_max) generators 通过，这个 pass rate 是否足够？\n   - entropy_min 作为 \"boundary feature\" 的处理是否合理？|ρ|=0.40 vs d=0.016 的矛盾是否被充分解释？\n   - 5 个 effect-size metrics 的一致性是真正的 convergent validation 还是高度相关指标的冗余？\n\n2. **统计检验严谨性**：\n   - TOST equivalence bound ε=0.20 的选择是否有 a priori justification？\n   - Bootstrap CI 的 sample size (n=1000) 是否足够？\n   - Bonferroni correction 的适用范围和影响\n   - 大样本下 TOST 的 power 问题（论文已承认但是否充分处理？）\n\n3. **Baseline 比较公平性**：\n   - 4-det+surface (F1=0.708) > 7-feature (0.705)，论文如何处理这个\"被超越\"的结果？\n   - 将 detection scores 作为 univariate features 是否对 baselines 不公平？（它们设计目的不是 depth classification）\n   - LOGO 评估中 gen-0 seed sharing 问题及其 leak-free binary F1 处理是否充分\n\n4. **实验设计漏洞**：\n   - 8 个 generators 全是 base model，且都 ≤8B——泛化性声明是否 overclaim？\n   - 单一 reference model (Pythia-410M) 的 same-family bias\n   - 温度固定 τ=0.7 的限制\n   - seed sharing 导致的 gen-0 data leakage 是否被完全控制？\n\n5. **消融实验**：\n   - LOFO 分析的充分性\n   - Surface-only vs Reference-only 分解的意义\n   - PCA 替代（PC1 仅损失 1.1pp）对 DDR 贡献声明的影响\n\n请按 ARR/EMNLP 标准给出完整审稿报告，包含 Summary、Strengths、Weaknesses（逐条编号，标注 severity: Critical/Major/Minor）、Questions、Missing References、Overall Assessment（使用 EMNLP 2026 评分标准：5=Award, 4=Conference, 3=Findings, 2=Resubmit, 1=Do not resubmit）。"
  }
}
```

</details>

---


### Tool result

_source line 2667 · 2026-05-21T02:32:58.310825+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 22767
}
```

</details>

---


### Tool call

_source line 2668 · 2026-05-21T02:32:58.361418+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "你是 Reviewer 2，负责 **新颖性 + 完整性** 审查。\n\n## 投稿信息\n- **Venue**: EMNLP 2026（通过 ARR May 2026 cycle 提交）\n- **截止日期**: 2026-05-25\n- **格式要求**: Long paper, ACL style template, 正文 ≤ 8 页 + 无限参考文献页; Limitations 必写（不计入页数限制）; 匿名双盲\n- **论文路径**: `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/main.tex`\n- **PDF**: `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/main.pdf`\n\n## 论文概要\n本文提出 \"Depth Fingerprinting\"，将 AI 文本检测从 binary (human/machine) 扩展到 ordinal depth estimation (gen-0/gen-1/gen-2+)。核心发现是 Differential Depth Response (DDR)：NLL location 特征随 generation depth 单调漂移（Cohen's d=0.76-1.17），而 shape 特征保持近稳态（d<0.10）。文章声称 DDR 与 model collapse 机制不同（fixed parameters vs retraining），并提出 \"what is preserved\"（shape stability）是新贡献。\n\n## 你的审查侧重\n\n1. **新颖性评估**：\n   - DDR 是否是 diversity loss / mode-seeking behavior 的重新表述？与 model collapse 文献（curse of recursion, strong model collapse）的区分是否令人信服？\n   - 与 concurrent work 的区分：Broken Telephone (paraphrase chains) vs Markovian Chains (attractor dynamics) vs 本文 (continuation chains + DDR decomposition)。区分度是否充分？\n   - \"what is preserved vs what converges\" 的 framing 是否真正新颖？shape stability 在统计学中是 well-known 的——固定参数下采样机制保持形状本身是否是 trivial observation？\n   - Task formulation (ordinal depth classification) 本身的新颖性 vs 工程贡献\n\n2. **Related Work 覆盖**：\n   - 搜索是否有遗漏的重要 related work（特别是 2025-2026 年的新工作）\n   - 引用格式和完整性检查\n   - 是否有 orphan bib entries（被 .bib 收录但正文未引用）\n   - concurrent work 的处理方式是否公平\n\n3. **写作质量**：\n   - 叙事结构是否清晰：从问题定义到方法到结果的逻辑链\n   - Abstract 是否准确反映了论文的实际贡献和局限\n   - Contribution statement 是否与实际结果匹配\n   - 术语一致性（如 \"entropy\" 实为 NLL 的 shorthand 是否会误导读者）\n   - Limitations 的坦诚度和完整性\n\n4. **格式合规**（EMNLP 2026 / ARR）：\n   - 正文是否 ≤ 8 页？\n   - 是否使用 ACL style template？\n   - 匿名性检查（无作者信息、无 self-citation revealing identity）\n   - Limitations section 是否存在且充分？\n   - Ethics statement 是否存在？\n   - 附录内容是否应移入主文？主文是否引用了附录中的关键结论？\n\n5. **Story 完整性**：\n   - proof-of-concept classifier 的定位是否一致？（F1=0.694 是否被 overclaim/underclaim？）\n   - base-model-only scope 限制是否在 Abstract/Intro/Conclusion 中一致地传达？\n   - downstream utility (null result) 是否被恰当处理？\n   - 14B preliminary evidence 的报告方式是否合适？\n\n请按 ARR/EMNLP 标准给出完整审稿报告，包含 Summary、Strengths、Weaknesses（逐条编号，标注 severity: Critical/Major/Minor）、Questions、Missing References、Overall Assessment（使用 EMNLP 2026 评分标准：5=Award, 4=Conference, 3=Findings, 2=Resubmit, 1=Do not resubmit）。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "text": "你是 Reviewer 2，负责 **新颖性 + 完整性** 审查。\n\n## 投稿信息\n- **Venue**: EMNLP 2026（通过 ARR May 2026 cycle 提交）\n- **截止日期**: 2026-05-25\n- **格式要求**: Long paper, ACL style template, 正文 ≤ 8 页 + 无限参考文献页; Limitations 必写（不计入页数限制）; 匿名双盲\n- **论文路径**: `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/main.tex`\n- **PDF**: `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/main.pdf`\n\n## 论文概要\n本文提出 \"Depth Fingerprinting\"，将 AI 文本检测从 binary (human/machine) 扩展到 ordinal depth estimation (gen-0/gen-1/gen-2+)。核心发现是 Differential Depth Response (DDR)：NLL location 特征随 generation depth 单调漂移（Cohen's d=0.76-1.17），而 shape 特征保持近稳态（d<0.10）。文章声称 DDR 与 model collapse 机制不同（fixed parameters vs retraining），并提出 \"what is preserved\"（shape stability）是新贡献。\n\n## 你的审查侧重\n\n1. **新颖性评估**：\n   - DDR 是否是 diversity loss / mode-seeking behavior 的重新表述？与 model collapse 文献（curse of recursion, strong model collapse）的区分是否令人信服？\n   - 与 concurrent work 的区分：Broken Telephone (paraphrase chains) vs Markovian Chains (attractor dynamics) vs 本文 (continuation chains + DDR decomposition)。区分度是否充分？\n   - \"what is preserved vs what converges\" 的 framing 是否真正新颖？shape stability 在统计学中是 well-known 的——固定参数下采样机制保持形状本身是否是 trivial observation？\n   - Task formulation (ordinal depth classification) 本身的新颖性 vs 工程贡献\n\n2. **Related Work 覆盖**：\n   - 搜索是否有遗漏的重要 related work（特别是 2025-2026 年的新工作）\n   - 引用格式和完整性检查\n   - 是否有 orphan bib entries（被 .bib 收录但正文未引用）\n   - concurrent work 的处理方式是否公平\n\n3. **写作质量**：\n   - 叙事结构是否清晰：从问题定义到方法到结果的逻辑链\n   - Abstract 是否准确反映了论文的实际贡献和局限\n   - Contribution statement 是否与实际结果匹配\n   - 术语一致性（如 \"entropy\" 实为 NLL 的 shorthand 是否会误导读者）\n   - Limitations 的坦诚度和完整性\n\n4. **格式合规**（EMNLP 2026 / ARR）：\n   - 正文是否 ≤ 8 页？\n   - 是否使用 ACL style template？\n   - 匿名性检查（无作者信息、无 self-citation revealing identity）\n   - Limitations section 是否存在且充分？\n   - Ethics statement 是否存在？\n   - 附录内容是否应移入主文？主文是否引用了附录中的关键结论？\n\n5. **Story 完整性**：\n   - proof-of-concept classifier 的定位是否一致？（F1=0.694 是否被 overclaim/underclaim？）\n   - base-model-only scope 限制是否在 Abstract/Intro/Conclusion 中一致地传达？\n   - downstream utility (null result) 是否被恰当处理？\n   - 14B preliminary evidence 的报告方式是否合适？\n\n请按 ARR/EMNLP 标准给出完整审稿报告，包含 Summary、Strengths、Weaknesses（逐条编号，标注 severity: Critical/Major/Minor）、Questions、Missing References、Overall Assessment（使用 EMNLP 2026 评分标准：5=Award, 4=Conference, 3=Findings, 2=Resubmit, 1=Do not resubmit）。"
  }
}
```

</details>

---


### Tool result

_source line 2669 · 2026-05-21T02:33:00.121874+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1760
}
```

</details>

---


### Assistant

_source line 2670 · 2026-05-21T02:33:12.556452+00:00_

Round 1 已启动：

| 角色 | 状态 | 侧重 |
|------|------|------|
| Reviewer 1 | ✅ 已派发 | 方法严谨性 + 实验设计 |
| Reviewer 2 | ✅ 已派发 | 新颖性 + 完整性 |
| 视觉审查 | ✅ 已启动 | 排版质量（非评分项） |
| 外部审稿 | ⏭️ 跳过 | 未配置 paperreview.ai |

等待两位 Reviewer 完成独立初审。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director"
}
```

</details>

---


## Round 231

## Round 231

2 recorded events


### User

_source line 2671 · 2026-05-21T02:38:08.998740+00:00_

[Reviewer 1 审稿意见]:

# Reviewer 1 — Round 1 审稿报告

## Paper: Depth Fingerprinting: Detecting Recursive Generation Depth in LLM Text Chains

---

## Summary

本文提出 Depth Fingerprinting，将 AI 文本检测从二分类（human/machine）扩展到序数深度估计（gen-0/gen-1/gen-2+）。核心发现是 Differential Depth Response (DDR)：NLL location 特征（entropy mean, TTR, hapax ratio）随 generation depth 单调漂移（Cohen's d=0.76–1.17），而 shape 特征（entropy max, tail decay, entropy min）保持近稳态（d<0.10）。基于此的 7-feature XGBoost 在 8-gen LOGO 下实现 leak-free binary F1=0.694；QLoRA 端到端分类器达到 F1=0.905。论文明确将 DDR 分解本身（而非分类器性能）定位为主要贡献。

---

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | DDR 核心发现有多重证据支撑，但 k=2 clustering 验证方法学存在缺陷（7 个点的聚类），TOST 部分通过率不足，5 个 effect-size metrics 冗余度高于声称的 convergent validation |
| Excitement | 3/5 | 从 binary detection 到 ordinal depth estimation 的延伸有新颖性，DDR 分解提供了机械性解释，但实际应用受限于 base model 限制 |
| Reproducibility | 4/5 | 实验设置详尽，超参明确，Bootstrap CI 贯穿全文，承诺开源代码和数据 |
| Overall Assessment | **3.5** (Borderline Conference) | 分析框架新颖且 insight 有价值，但验证方法存在可质疑之处，practical impact 受限于 base-model-only 约束 |
| Reviewer Confidence | 4/5 | 仔细阅读了全部 33 页（含 20 页附录），熟悉 AI 文本检测和统计检验方法 |

---

## Must-Fix 问题（影响接收决定）

**N1** [Critical] k=2 聚类验证在 7 个数据点上不构成 principled validation

- 具体位置：§4.2 第 2 段；Appendix V (Table 28)
- 问题：论文声称 DDR 分区是 "data-driven"（silhouette=0.632），但 k-means 聚类的对象仅有 7 个特征点（在 (|ρ|, d) 二维空间中）。对 7 个点做 k=2 聚类在数学上几乎是 trivial 的——任何存在基本结构的 7 点集合都能产生合理的 silhouette。此外，silhouette 从 k=2 (0.632) 下降到 k=3 (0.499) 再回升到 k=4 (0.571)，这种非单调变化在样本量如此小的情况下不具备统计意义。
- 为什么影响接收：DDR 分区是整篇论文的核心贡献。如果 "data-driven" 验证方法学站不住脚，整个分析框架的可信度会受质疑。
- 建议修改方向：(1) 下调 "data-driven" 的表述强度，承认聚类更多是 visualization 而非 formal validation；(2) 增加 per-generator 层面的聚类分析（对每个 generator 单独计算 (|ρ|, d) 并做聚类），这样样本量从 7 升到 7×8=56，更具说服力；(3) 考虑使用 permutation test 或 gap statistic 来量化 k=2 分区是否显著优于随机分区。

**N2** [Critical] TOST 对 tail_decay 仅 4/8 generators 通过等价性检验，"near-stationary" 分类缺乏充分支撑

- 具体位置：§4.2 Validation 段；Appendix U (Table 26)
- 问题：tail_decay 在 ε=0.20 下仅 4/8 generators 通过 TOST，OLMo-2-1B 的 |d|=0.22 已超过等价界。论文承认这是 "genuine boundary case" 并提出可将其重新分类为 intermediate，但主文中仍将其保留在 near-stationary 组，且 DDR 分区的核心叙事（3 drifting + 1 intermediate + 3 near-stationary）依赖于此分类。
- 为什么影响接收：如果 near-stationary 组中有一个特征实际上在半数 generators 上表现出 non-negligible drift，那么 "shape invariance" 的核心声明被削弱。进一步地，sensitivity analysis (Table 29) 显示 tail_decay 在 ε=0.25 时才达到 7/8 通过率，说明其 near-stationarity 对阈值选择敏感。
- 建议修改方向：(1) 在主文中明确将 DDR 分区描述为 3/1/1/2 或 3/2/2 (entropy std 和 tail_decay 均为 intermediate)，这更诚实地反映数据；(2) 或者提供更强的论证解释为何 50% 通过率足以支撑 near-stationary 分类。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [Major] 5 个 effect-size metrics 的 "convergent validation" 实为高度相关指标的冗余

- 具体位置：§4.2 Quantification 段；Appendix V (Table 32)
- 问题：论文声称 5 个独立 effect-size metrics（Cohen's d, Glass's Δ, KS statistic, Cliff's δ, CV shift）"converge on" DDR 分区。但 Cohen's d 和 Glass's Δ 仅在方差处理上不同（Glass's Δ 用 gen-1 SD 做分母），KS statistic 捕获的也是 location+shape 的联合差异。真正提供互补视角的仅有 Cliff's δ（rank-based）和 CV shift（relative variability）。将 5 个高度相关的指标呈现为 "five independent effect-size metrics" 存在过度声称（overclaim）的风险。
- 建议：将 "five independent" 改为 "five complementary"，并在主文中区分 parametric overlap（Cohen's d ≈ Glass's Δ ≈ KS）与 genuinely independent perspectives（Cliff's δ, CV shift）。

**W2** [Major] 所有 8 个 generators 均为 base model (≤8B)，泛化性声明需更严格限定

- 具体位置：§5 Discussion；§Limitations；Appendix K (Table 15-16)
- 问题：Instruct 模型结果（OLMo-Instruct 3-class F1=0.575 vs base 0.754；Llama-Instruct 0.544 vs 0.742）显示 DDR 在实际部署场景中大幅退化。论文在 Limitations 中承认了这一点，但 Discussion 中关于 DDR 作为 data curation 工具的讨论（§5 第 2 段）暗示了比现有证据支撑的更广泛的适用性。
- 建议：(1) 在 Discussion 中更明确地限定 practical applicability 仅限于 base-model 场景；(2) 讨论 instruct models 为何失败的具体原因（length regulation? RLHF distributional shaping?），而不仅是描述失败本身。

**W3** [Major] Baseline 比较的公平性存疑

- 具体位置：§4.3 (Table 2)
- 问题：(1) 4-det+surface (Bin F1=0.708, 6 features) 超过 7-feature ensemble (0.705, 7 features)，但论文将此结果归为 "marginally above the 7-feature set at 2.4× the inference cost"，实际上 4-det+surface 在两个 metric 上都更好（3-cl F1: 0.795 vs 0.774）。(2) 将 detection scores 作为 univariate features 输入 XGBoost 可能低估了 baselines 的潜力——这些 detectors 的内部特征或多尺度阈值组合可能更适合 depth classification。(3) 论文正确指出 DDR 的贡献是分解而非分类性能，但如果 baseline 方法用更少的特征就能达到更好效果，"为什么需要 DDR 分解？" 这个问题需要更强的回答。
- 建议：(1) 更诚实地呈现 baseline 比较结果——当被超越时不应淡化表述；(2) 讨论为什么 detection scores 能有效预测 depth（可能是因为它们本身就在测量类似的 distributional drift）；(3) 强化 DDR 分解的独特价值论述（interpretability, mechanistic understanding）。

**W4** [Major] TOST 等价界 ε=0.20 的 justification 存在循环论证

- 具体位置：§4.2 Validation 段；Appendix U 第 1 段
- 问题：论文以 Cohen's conventional small effect size (d=0.20) 作为 SESOI，然后用 LOFO 分析（"removing any near-stationary feature changes F1 by ≤1.5pp"）作为辅助支撑。但这个论证是循环的：特征先被分类为 near-stationary（基于 d<0.20），然后被证明对分类影响小（LOFO ≤1.5pp），然后这个小影响被用来 justify d=0.20 的选择。真正需要的是一个 a priori 的、基于任务需求的 SESOI 论证。
- 建议：(1) 在论文中承认 ε=0.20 是 conventional 选择而非 task-specific derivation；(2) sensitivity analysis (Table 29) 已经做了 ε∈{0.15, 0.20, 0.25}，结论基本稳定，这比单点 ε 更有说服力——应在主文中强调这一点而非放在附录。

**W5** [Major] 下游实用性实验（Appendix M）显示 null result，但未在主文中充分讨论

- 具体位置：Appendix M (Table 19)；§5 Discussion
- 问题：深度感知的数据筛选（depth 0-1 only, ppl=2.387）并未优于随机子采样（ppl=2.367），TOST 确认两者等价。这直接挑战了论文在 Discussion 中提出的 "training-data curation pipeline" 应用场景。虽然论文在附录中诚实报告了这一结果，但 Discussion 第 2 段关于 curation 应用的论述未提及此 null result。
- 建议：在 Discussion 中至少用一句话提及 downstream fine-tuning 的 null result，并调整 curation 应用的 claim strength。

---

## 小问题（不影响接收）

**M1** [Minor] entropy_min 的 Cliff's δ=0.354 ("medium") 与 Cohen's d=0.016 之间的矛盾虽有脚注解释（Table 32 脚注 †），但主文中 "d<0.10" 的总结性表述遮盖了这一细微差别。建议在主文首次提到 entropy_min 时加一句 rank-based measures 的 caveat。

**M2** [Minor] Bootstrap CI 使用 n=1000 iterations（§3.4），这在 pooled sample (N≈37K) 上产生了极窄的 CI。例如 Table 1 中 binary F1=0.694 [0.688, 0.700] 仅 1.2pp 宽度。但这仅反映采样变异性，不反映 generator selection uncertainty。真正的 generalization uncertainty 更大——LOGO per-generator F1 从 0.633 (Mistral) 到 0.724 (Pythia-2.8B)，span 9.1pp。建议区分 sampling CI 和 generalization variability。

**M3** [Minor] §3.2 提到 generation chain 深度为 4（gen-0 through gen-4），但 depths 2-4 合并为 2+。为什么选择 depth 4 而非更深或更浅？是否有预实验 justify 这个选择？

**M4** [Minor] Table 1 脚注中提到 "3-class F1 carries upward bias because gen-0 seeds are shared"，但 3-class F1 仍作为 Table 2 baseline 比较的指标之一。建议在 Table 2 中也加注或统一使用 binary F1 作为 primary comparison。

**M5** [Minor] §2.1 Related Work 中将本文与 model collapse 文献区分，但 §5 Discussion 最后又详细讨论两者的联系。建议在 Related Work 中预告这一区分，使叙事更连贯。

**M6** [Minor] Appendix W (Generator Subset Summary, Table 33) 是个好的 transparency measure，但正文中有时不够清楚哪些结果对应哪个 generator subset（如 cross-model chains 使用 5-generator subset，但脚注较小容易忽略）。

---

## Questions to Authors

Q1. 如果将 tail_decay 重新分类为 intermediate（使分区变为 3/2/2），对分类性能和 DDR 叙事有何具体影响？能否提供这一替代分区下的 ablation 结果？

Q2. 论文提到 Gemma-2-2B 的泛化最弱（3-class F1=0.628, per-class gen-1 F1=0.036）。这是否暗示 DDR 在某些架构上根本不成立？Gemma 的具体失败模式是什么？

Q3. QLoRA 在 instruct data 上恢复到 F1=0.89-0.91，但 7-feature DDR-based 方法在 instruct 上严重退化。这是否意味着 DDR 分解对 instruct models 失效，而 token-level patterns 仍然存在？如果是，DDR 分解框架的 generality 如何自圆其说？

Q4. 关于 Downstream Utility (Appendix M)：如果 depth-aware curation 不优于 random subsampling，论文在 §5 中讨论的 data curation 应用场景的具体 value proposition 是什么？

Q5. Cross-reference model 实验（Appendix S, spread ≤0.013）仅使用了 3 个 reference models（Pythia-410M, OLMo-2-1B, Qwen3-0.6B），是否考虑过使用完全不同架构（如 decoder-only vs encoder-decoder）的 reference model？

---

## Missing References

- Tian et al. (2024) "GPTZero" 系列工作未在 baseline 中讨论
- Kirchenbauer et al. (2023) watermarking 方法作为替代检测方案未在 Related Work 中对比讨论其与 depth detection 的关系（虽然引用了但讨论不足）
- Sadasivan et al. (2024) "Can AI-Generated Text be Reliably Detected?" 已引用但未讨论其 adversarial robustness findings 对 DDR 的潜在影响

---

## 主要优势

1. **研究问题新颖且有价值**：从 binary (human/machine) 到 ordinal depth estimation 的扩展是自然且有意义的研究方向，填补了检测文献中的空白。

2. **DDR 分解提供了机械性解释**：location drifts while shape is preserved 的发现不仅是经验性的，还通过 top-p truncation 的功能形式给出了机械性解释（§5 第 1 段），并通过温度消融和 prompt type 消融提供了两个可检验的预测。

3. **实验控制极其详尽**：seed-sharing control、length confound control、independent-seed experiment、cross-reference model、cross-temperature、cross-domain——几乎所有能想到的混淆变量都有对应的控制实验。

4. **诚实的限制讨论**：论文坦承 instruct model 失败、baseline 在某些 metric 上超越、downstream utility 的 null result。这种学术诚实度在投稿论文中较为少见。

5. **写作质量**：论文结构清晰，主文 8 页信息密度高，附录组织合理。Figure 1（DDR trajectory）和 Figure 2（DDR scatter）有效传达了核心发现。

6. **可复现性**：超参、数据统计、评估协议详细记录，承诺开源。

---

## 总体评分

**Overall**: 3.5 (Borderline Conference)

**一句话总结**：DDR 分解是一个有洞察力的分析框架，实验控制详尽且写作诚实，但核心分区验证方法（7 点聚类）在方法学上有缺陷、near-stationary 组内 tail_decay 的 TOST 通过率仅 50%、且方法对 instruct models 失效限制了实际影响力。作为 analytical contribution 足以进入 Findings；若能补强 N1（分区验证）和 N2（tail_decay 分类），有望达到 Conference 水平。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 2672 · 2026-05-21T02:38:16.466713+00:00_

Reviewer 1 报告已收到（Overall: 3.5 Borderline Conference）。等待 Reviewer 2 报告后进入交叉分享。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director"
}
```

</details>

---


## Round 232

## Round 232

2 recorded events


### User

_source line 2673 · 2026-05-21T02:38:20.958459+00:00_

[Reviewer 1 审稿结果]:
审稿报告已提交给 Review Director。

总结：作为 Reviewer 1（方法严谨性 + 实验设计），我给出 **Overall 3.5 (Borderline Conference)** 的评分。

核心判断：
- **2 个 Critical 问题**：(1) k=2 聚类在 7 个点上做 "data-driven" validation 方法学不足；(2) tail_decay 仅 4/8 generators 通过 TOST，削弱 "near-stationary" 声明
- **5 个 Major 问题**：effect-size metrics 冗余性 overclaim、base-model-only 限制、baseline 比较公平性、TOST ε 循环论证、downstream null result 未在主文讨论
- **主要优势**：研究问题新颖、DDR 分解有机械性解释、实验控制极其详尽、写作诚实

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 2674 · 2026-05-21T02:38:33.710716+00:00_

收到 Reviewer 1 报告。等待 Reviewer 2 报告后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director"
}
```

</details>

---


## Round 233

## Round 233

6 recorded events


### User

_source line 2675 · 2026-05-21T02:41:16.882122+00:00_

[Reviewer 2 审稿意见]:

# Reviewer 2 审稿报告：Depth Fingerprinting: Detecting Recursive Generation Depth in LLM Text Chains

## 总体评分
**Overall**: 3.5 (Borderline Conference)
**一句话总结**: 任务定义新颖、实验设计严谨，但核心 shape stability 发现可能是采样机制的 trivial 推论，且与 concurrent work (Markovian Chains) 重叠显著，加之 base-model-only 的窄适用范围和 null downstream utility，介于 Conference 和 Findings 之间。

---

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | 方法论整体严谨（LOGO CV、Cohen's d、TOST、bootstrap CI），但 shape stability 的理论解释不充分；downstream utility 的 TOST 仅用 n=3 seeds，统计效力偏低 |
| Excitement | 3.0/5 | Ordinal depth classification 的任务定义有新意，DDR 分解提供了有用的实证框架；但与 Markovian Chains 的增量性较明显，实际应用受限 |
| Overall | 3.5/5 | 经验充分的 empirical study + 新颖任务定义，但核心洞察可能 trivial、实用范围窄 |
| Confidence | 4/5 | 仔细阅读了全部 33 页（正文+附录），交叉验证了引用，搜索了 concurrent work |

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] Shape stability 可能是固定采样机制的 trivial 推论，论文未充分讨论
- 具体位置：Section 5 (Discussion), Section 4.2, Abstract
- 问题：论文将 shape stability（NLL shape 特征 d<0.10）作为核心贡献之一，以 "what is preserved vs what converges" 的 framing 呈现。但 Section 5 自己承认："Under nucleus sampling, top-p truncation selects from a fixed probability-mass fraction at each step, preserving the functional form of the conditional distribution regardless of input context." 既然 top-p 截断在固定参数下天然保持条件分布的函数形式，那么 shape stability 就不是一个 emergent property，而是采样机制的直接推论。这削弱了 "novel observation" 的定位。
- 为什么影响接收：如果论文声称的两大贡献之一（DDR 的 shape stability 维度）实际上是 trivial 的，则论文的 novelty 大打折扣。
- 建议修改方向：(1) 明确讨论 shape stability 在什么条件下会被打破（如变温度/top-p 是否会打破 shape？附录 P 的跨温度实验部分涉及但未系统讨论 shape 维度）；(2) 如果无法证明 shape stability 在更广条件下成立或有非 trivial 的理论意义，应降低对其作为独立贡献的强调。

**N2** [critical] 与 Markovian Chains (Geng et al., 2026) 的区分度不足
- 具体位置：Section 2.2 (Related Work), Section 5 (Discussion)
- 问题：Markovian Chains 同样研究 continuation chains under fixed parameters，同样文档了 attractor dynamics 和收敛行为。本文与之的区分仅在于 (a) location/shape 分解 和 (b) ordinal classification 应用。但 Section 2.2 对此区分仅用了一句话处理（"We study inference chains where parameters are fixed and only the input distribution evolves"），没有系统性对比。尤其是 Markovian Chains 的 "attractor dynamics" 本质上描述的就是 location drift 的收敛现象。
- 为什么影响接收：如果审稿人认为 DDR 本质上是 Markovian Chains 的 attractor dynamics 加上一个 location/shape 标签的重新包装，novelty claim 不成立。
- 建议修改方向：增加与 Markovian Chains 的系统性实验对比或定性分析表，明确说明两者在 (1) chain construction、(2) feature space、(3) 分析目标上的具体差异；讨论 DDR 是否可以被视为 attractor dynamics 的 NLL 特征空间投影。

**N3** [critical] Instruction-tuned models 下 DDR 信号严重退化，限制实际适用性
- 具体位置：Appendix K (Table 15-16), Limitations (p.9)
- 问题：Appendix K 显示 instruction tuning 将 3-class F1 从 main experiments 的 ~0.694 降低了 3.7 倍（Table 15 average F1=0.321 under 5-fold CV for instruct models vs base models）。OLMo-2-1B 在 instruction tuning 后几乎丧失所有 depth signal，entropy mean 从 drifting 转为 near-stationary。鉴于现实中绝大多数 LLM 输出来自 instruction-tuned/RLHF 模型，这严重限制了 depth fingerprinting 的实际应用场景。
- 为什么影响接收：Abstract 和 Introduction 的 motivation 引用了 data governance pipelines 和 recursive contamination 的实际场景（"7-17% of recent scientific publications already contain substantial LLM-modified content"），但这些场景中的文本绝大多数来自 instruction-tuned models。论文的 base-model-only scope 与其 motivation narrative 存在较大张力。
- 建议修改方向：(1) 在 Abstract 中更早、更明确地限定 scope 为 base models；(2) 讨论为什么 instruction tuning 会破坏 DDR 信号（是因为 RLHF alignment 改变了 NLL 分布形状？还是指令遵从引入了额外变异性？）；(3) 如果空间允许，提出缓解策略的假设。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [major] Downstream utility 为 null result，削弱实际 motivation
- 具体位置：Appendix M (Table 19-20)
- 问题：Appendix M 的 downstream utility 实验测试 depth-aware data curation 是否能改善语言模型质量，结论是 TOST equivalence（depth-aware curation ≈ random subsampling）。论文诚实地报告了这一结果，但这直接削弱了 Introduction 中 "knowing the generation depth of a document does not, by itself, make it more or less useful for training" 之前的 data governance motivation。
- 建议：论文已经较好地处理了这一 null result（称之为 "preliminary observation"），但可以进一步讨论为什么 depth 信号未能转化为 downstream utility——是因为 3 seeds 太少（n=3 的统计效力确实很低），还是因为 NLL location shift 不影响训练质量？

**W2** [major] 术语 "entropy" 用作 NLL 的简写可能误导读者
- 具体位置：Section 3.3, 全文
- 问题：Section 3.3 的脚注声明 "We use 'entropy' as shorthand for token-level NLL throughout"，但在后续文本中，"entropy mean"、"entropy std"、"entropy max"、"entropy min" 这些术语反复出现。Token-level NLL (−log p(x_t | x_{<t})) 和 Shannon entropy (−Σ p log p) 是不同的量。NLL 衡量的是 reference model 下特定 token 的 surprisal，而非词表上概率分布的熵。这种术语混用在 AI text detection 文献中虽然有先例，但对于强调 statistical rigor 的 empirical study 来说，不够精确。
- 建议：至少在 Section 3.3 的特征定义处使用精确术语（如 "NLL mean" 或 "surprisal mean"），脚注中解释简写惯例即可；或在相关工作中引用使用同一简写的先前工作以建立术语传统。

**W3** [minor→major] `attractor_cycles` (Wang et al., 2025) 的 bib entry 缺少 title 字段
- 具体位置：References (p.13), .bib file
- 问题：引用验证工具检测到 `attractor_cycles` bib entry 的 title 字段为空。虽然 PDF 中该条目渲染时标题 "Unveiling Attractor Cycles in LLMs" 出现了（可能通过 LaTeX 的其他机制注入），但 .bib 文件本身的格式不规范。这是一个 camera-ready 前必须修复的问题。
- 建议：补全 bib entry 的 title 字段。

**W4** [minor] Proof-of-concept classifier 的定位在正文各处不完全一致
- 具体位置：Abstract, Section 4.1, Conclusion
- 问题：Abstract 称 "a lightweight 7-feature ensemble... achieves leak-free binary F1=0.694"——但 0.694 是 3-class macro-F1（Table 1），binary F1 实际是 0.762（也在 Table 1）。Conclusion 更清晰地区分了两者。Abstract 的措辞可能让读者误认为 binary 分类的 F1 只有 0.694。
- 建议：Abstract 中明确区分 binary F1 和 3-class macro-F1 的数值。

**W5** [minor] 14B preliminary evidence 的报告方式需斟酌
- 具体位置：Section 5 (Discussion), p.8
- 问题：Section 5 报告了 Qwen3-14B-Base 的初步证据（Cohen's d=0.78-1.12），但仅限于 effect size 报告，无 classification performance、无 cross-validation 数据。在 Discussion 中报告未经充分验证的初步结果存在风险——读者可能将其视为正式结果。
- 建议：要么移入附录并标注 "preliminary"，要么补充分类实验结果。当前的报告方式（Discussion 正文中一段话）容易被过度解读。

---

## 小问题（不影响接收）

- **M1**: Figure 1 (p.6) 的 strip plot 信息密度很高但 x 轴标签 "Generation Depth" 重复了 7 次，可考虑共享 x 轴。
- **M2**: Table 1 (p.5) 的 "Params" 列使用了 "0.4B" 等缩写，但 Table 3 (p.13) 用 "3B" "7B"，单位格式不一致。
- **M3**: Section 3.2 提到 "we use 'entropy' as shorthand"，但这个脚注实际在 Section 3.3 的 reference-model features 定义处。引用位置可以前移到首次使用处。
- **M4**: Appendix Z.5 (Token-Level NLL Distribution, p.33) 中的 kernel density plot 是论文中信息密度最高、最有 mechanistic insight 的可视化之一，建议考虑是否可以将其核心信息（如一个代表性示例）提升到主文。
- **M5**: 引用验证显示 5 条 bib entries 存在 first_author mismatch（Cohen 1988、self_consuming_mad、qwen3、gutierrez_ordinal_survey、llama3），主要是 LaTeX 编码 vs API 索引的差异，建议 camera-ready 前检查。

---

## Missing References

引用覆盖整体良好（66 条引用，0 orphan，0 missing），concurrent work 的覆盖合理。以下是可能值得考虑但不构成必须引用的工作：

1. **"Variation is the Key: A Variation-Based Framework for LLM-Generated Text Detection"** (arXiv:2602.13226, 2026) — 提出了基于 LLM rewriting 前后 variation 的检测方法，与本文的 generation-depth-dependent distributional shift 有概念联系，但研究目标不同（binary detection vs depth classification）。属于 nice-to-have 而非 must-cite。

2. 无发现重大遗漏的 related work。Broken Telephone、Markovian Chains、attractor_cycles 三篇核心 concurrent work 均已引用。Model collapse 文献覆盖充分（curse_of_recursion、strong_model_collapse、model_collapse_avoidable、schaeffer_collapse_position）。Detection 方法覆盖全面。

---

## 引用格式检查

- **Orphan bib entries**: 0（所有 .bib 条目均在正文中引用）
- **Missing bib entries**: 0（所有 \cite 命令均有对应 .bib 条目）
- **问题条目**: `attractor_cycles` 缺少 title（W3）；5 条 first_author mismatch（M5）
- **在线验证**: 54/66 条在 OpenAlex 验证通过；6 条 not_found（均为知名论文，系 OpenAlex 索引覆盖问题：DetectGPT、Pythia、XGBoost、detection_possibilities、reliable_detection、aaronson_watermark）

---

## 格式合规（EMNLP 2026 / ARR）

| 检查项 | 状态 | 备注 |
|--------|------|------|
| 正文 ≤ 8 页 | ✅ | 正文结束于 p.8 (Section 6 Conclusion)；Limitations 从 p.9 开始 |
| ACL style template | ✅ | 使用 acl_natbib 模板 |
| 匿名性 | ✅ | 标题页标注 "Anonymous ACL submission"，未发现自引泄露身份 |
| Limitations section | ✅ | p.9，涵盖 base-model scope、English-only、Wikipedia text、scale limitations |
| Ethics statement | ✅ | p.9-10，讨论隐私影响和负责任部署 |
| 附录引用 | ✅ | 主文频繁引用附录内容（Appendix A-Z），引用方向正确 |

---

## 主要优势

1. **任务定义的新颖性**：将 AI text detection 从 binary (human/machine) 扩展到 ordinal depth classification (gen-0/1/2+) 是一个有意义的概念推进，具有清晰的 practical motivation（data governance, contamination tracking）。

2. **实验设计的系统性和统计严谨性**：8 个生成器、5 个模型家族、LOGO cross-validation、Cohen's d effect sizes、bootstrap CIs、TOST equivalence tests——这是一篇在统计方法论上非常自觉的 empirical study。

3. **附录的详尽程度**：20+ 页附录覆盖了 confusion matrix、cross-temperature transfer、text perturbation robustness、cross-domain generalization、instruction-tuned models、downstream utility、UMAP visualization、Granger causality、generator split validation 等，展示了对潜在质疑的充分预判。

4. **DDR 分解的实证框架**：将 distributional drift 分解为 location（漂移）和 shape（近稳态）两个维度，即使 shape stability 的理论新颖性存疑，这个分析框架本身对后续研究仍有组织价值。

5. **诚实处理 null results**：downstream utility 的 TOST equivalence（null result）和 instruction-tuned models 下的性能退化都被坦诚报告，没有选择性呈现。

6. **写作质量**：叙事结构清晰，从问题定义到方法到结果到 mechanistic interpretation 的逻辑链连贯，语言精练。

---

## 主要弱点总结

1. **核心贡献之一（shape stability）可能是 trivial observation**（N1）
2. **与 Markovian Chains 的区分度不足**（N2）
3. **Base-model-only scope 与 motivation narrative 的张力**（N3）
4. **Null downstream utility 削弱实际应用叙事**（W1）
5. **术语 "entropy" 的精确性问题**（W2）

---

## Questions to Authors

1. 你们是否尝试过在不同 top-p 值（如 p=0.5, 0.7, 0.95）下测试 shape stability？如果 shape stability 在 top-p 变化时被打破，这将支持 "shape stability 是采样机制的 trivial 推论" 的解释。反之，如果在不同 top-p 下 shape 仍然保持稳定，则该发现更有意义。

2. DDR 的 location drift 与 Markovian Chains 的 "attractor convergence" 在定量层面是否等价？是否可以将 Markovian Chains 的 attractor 指标映射到你们的 NLL 特征空间？

3. Instruction tuning 破坏 DDR 的 mechanistic explanation 是什么？是 RLHF 改变了 NLL 分布的形状（从而打破 shape stability），还是指令遵从引入了额外的 context-dependent variability？

4. 如果 depth fingerprinting 在 instruction-tuned models 上不 work，论文的主要应用场景是什么？是否存在现实的 pipeline 使用 base model 生成大量文本？

5. Appendix M 的 downstream utility 实验仅用了 n=3 seeds。你们是否有计划增加 seeds 数量以提高统计效力，还是认为当前的 equivalence 结论已经足够稳健？


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 2676 · 2026-05-21T02:42:12.541275+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "## 交叉审稿：请逐条回应 Reviewer 1 的审稿意见\n\n以下是 Reviewer 1（方法严谨性 + 实验设计）的完整审稿意见。请逐条回应：\n- **[AGREE]** 同意并说明理由\n- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）\n\n注意：你需要回应所有 Must-Fix (N1, N2) 和 Should-Fix (W1-W5) 问题。Minor 问题可选择性回应。\n\n---\n\n## Reviewer 1 的完整审稿意见\n\n### Overall: 3.5 (Borderline Conference)\n\n### Must-Fix 问题\n\n**N1** [Critical] k=2 聚类验证在 7 个数据点上不构成 principled validation\n- §4.2 第 2 段；Appendix V (Table 28)\n- 论文声称 DDR 分区是 \"data-driven\"（silhouette=0.632），但 k-means 聚类的对象仅有 7 个特征点（在 (|ρ|, d) 二维空间中）。对 7 个点做 k=2 聚类在数学上几乎是 trivial 的——任何存在基本结构的 7 点集合都能产生合理的 silhouette。此外，silhouette 从 k=2 (0.632) 下降到 k=3 (0.499) 再回升到 k=4 (0.571)，这种非单调变化在样本量如此小的情况下不具备统计意义。\n- 建议：(1) 下调 \"data-driven\" 的表述强度；(2) 增加 per-generator 层面的聚类分析（7×8=56 点）；(3) 使用 permutation test 或 gap statistic。\n\n**N2** [Critical] TOST 对 tail_decay 仅 4/8 generators 通过等价性检验，\"near-stationary\" 分类缺乏充分支撑\n- §4.2 Validation 段；Appendix U (Table 26)\n- tail_decay 在 ε=0.20 下仅 4/8 通过，OLMo-2-1B |d|=0.22 超过等价界。论文承认 \"genuine boundary case\" 但主文仍保留在 near-stationary 组。\n- 建议：(1) 改为 3/2/2 分区（entropy std + tail_decay 均为 intermediate）；(2) 或提供更强论证。\n\n### Should-Fix 问题\n\n**W1** [Major] 5 个 effect-size metrics 的 \"convergent validation\" 实为高度相关指标的冗余\n- Cohen's d 和 Glass's Δ 仅在方差处理上不同，KS statistic 也捕获 location+shape 联合差异。真正互补的仅有 Cliff's δ 和 CV shift。\"five independent\" 存在 overclaim。\n\n**W2** [Major] 所有 8 个 generators 均为 base model (≤8B)，泛化性声明需更严格限定\n- Instruct 结果大幅退化（OLMo-Instruct F1=0.575 vs base 0.754）。Discussion 中 data curation 讨论暗示了比证据支撑更广的适用性。\n\n**W3** [Major] Baseline 比较的公平性存疑\n- 4-det+surface (Bin F1=0.708) > 7-feature (0.705)；将 detection scores 作为 univariate features 可能低估 baselines。\"为什么需要 DDR 分解？\" 需更强回答。\n\n**W4** [Major] TOST 等价界 ε=0.20 的 justification 存在循环论证\n- 特征先被分类为 near-stationary（基于 d<0.20），然后 LOFO 证明影响小，然后小影响用来 justify ε=0.20。\n\n**W5** [Major] 下游实用性实验（Appendix M）显示 null result，但未在主文中充分讨论\n\n### Minor 问题\nM1-M6: entropy_min Cliff's δ 矛盾、Bootstrap CI vs generalization variability、chain depth 4 选择、Table 2 metric 一致性、Related Work 叙事连贯性、generator subset 标注清晰度。\n\n### Questions\nQ1. tail_decay 重分类为 intermediate 的影响？\nQ2. Gemma-2-2B 的具体失败模式？\nQ3. QLoRA 在 instruct 上恢复但 DDR 失效——DDR 分解的 generality 如何自圆？\nQ4. downstream null result 下 data curation 的 value proposition？\nQ5. 是否考虑过 encoder-decoder 架构的 reference model？"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "text": "## 交叉审稿：请逐条回应 Reviewer 1 的审稿意见\n\n以下是 Reviewer 1（方法严谨性 + 实验设计）的完整审稿意见。请逐条回应：\n- **[AGREE]** 同意并说明理由\n- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）\n\n注意：你需要回应所有 Must-Fix (N1, N2) 和 Should-Fix (W1-W5) 问题。Minor 问题可选择性回应。\n\n---\n\n## Reviewer 1 的完整审稿意见\n\n### Overall: 3.5 (Borderline Conference)\n\n### Must-Fix 问题\n\n**N1** [Critical] k=2 聚类验证在 7 个数据点上不构成 principled validation\n- §4.2 第 2 段；Appendix V (Table 28)\n- 论文声称 DDR 分区是 \"data-driven\"（silhouette=0.632），但 k-means 聚类的对象仅有 7 个特征点（在 (|ρ|, d) 二维空间中）。对 7 个点做 k=2 聚类在数学上几乎是 trivial 的——任何存在基本结构的 7 点集合都能产生合理的 silhouette。此外，silhouette 从 k=2 (0.632) 下降到 k=3 (0.499) 再回升到 k=4 (0.571)，这种非单调变化在样本量如此小的情况下不具备统计意义。\n- 建议：(1) 下调 \"data-driven\" 的表述强度；(2) 增加 per-generator 层面的聚类分析（7×8=56 点）；(3) 使用 permutation test 或 gap statistic。\n\n**N2** [Critical] TOST 对 tail_decay 仅 4/8 generators 通过等价性检验，\"near-stationary\" 分类缺乏充分支撑\n- §4.2 Validation 段；Appendix U (Table 26)\n- tail_decay 在 ε=0.20 下仅 4/8 通过，OLMo-2-1B |d|=0.22 超过等价界。论文承认 \"genuine boundary case\" 但主文仍保留在 near-stationary 组。\n- 建议：(1) 改为 3/2/2 分区（entropy std + tail_decay 均为 intermediate）；(2) 或提供更强论证。\n\n### Should-Fix 问题\n\n**W1** [Major] 5 个 effect-size metrics 的 \"convergent validation\" 实为高度相关指标的冗余\n- Cohen's d 和 Glass's Δ 仅在方差处理上不同，KS statistic 也捕获 location+shape 联合差异。真正互补的仅有 Cliff's δ 和 CV shift。\"five independent\" 存在 overclaim。\n\n**W2** [Major] 所有 8 个 generators 均为 base model (≤8B)，泛化性声明需更严格限定\n- Instruct 结果大幅退化（OLMo-Instruct F1=0.575 vs base 0.754）。Discussion 中 data curation 讨论暗示了比证据支撑更广的适用性。\n\n**W3** [Major] Baseline 比较的公平性存疑\n- 4-det+surface (Bin F1=0.708) > 7-feature (0.705)；将 detection scores 作为 univariate features 可能低估 baselines。\"为什么需要 DDR 分解？\" 需更强回答。\n\n**W4** [Major] TOST 等价界 ε=0.20 的 justification 存在循环论证\n- 特征先被分类为 near-stationary（基于 d<0.20），然后 LOFO 证明影响小，然后小影响用来 justify ε=0.20。\n\n**W5** [Major] 下游实用性实验（Appendix M）显示 null result，但未在主文中充分讨论\n\n### Minor 问题\nM1-M6: entropy_min Cliff's δ 矛盾、Bootstrap CI vs generalization variability、chain depth 4 选择、Table 2 metric 一致性、Related Work 叙事连贯性、generator subset 标注清晰度。\n\n### Questions\nQ1. tail_decay 重分类为 intermediate 的影响？\nQ2. Gemma-2-2B 的具体失败模式？\nQ3. QLoRA 在 instruct 上恢复但 DDR 失效——DDR 分解的 generality 如何自圆？\nQ4. downstream null result 下 data curation 的 value proposition？\nQ5. 是否考虑过 encoder-decoder 架构的 reference model？"
  }
}
```

</details>

---


### Tool result

_source line 2677 · 2026-05-21T02:42:34.142666+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 21601
}
```

</details>

---


### Tool call

_source line 2678 · 2026-05-21T02:42:38.960350+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "## 交叉审稿：请逐条回应 Reviewer 2 的审稿意见\n\n以下是 Reviewer 2（新颖性 + 完整性）的完整审稿意见。请逐条回应：\n- **[AGREE]** 同意并说明理由\n- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）\n\n注意：你需要回应所有 Must-Fix (N1, N2, N3) 和 Should-Fix (W1-W5) 问题。Minor 问题可选择性回应。\n\n---\n\n## Reviewer 2 的完整审稿意见\n\n### Overall: 3.5 (Borderline Conference)\n\n### Must-Fix 问题\n\n**N1** [Critical] Shape stability 可能是固定采样机制的 trivial 推论\n- Section 5 自己承认 top-p truncation preserves functional form of conditional distribution。既然 top-p 截断在固定参数下天然保持条件分布的函数形式，shape stability 就不是 emergent property，而是采样机制的直接推论。\n- 建议：明确讨论 shape stability 在什么条件下会被打破；或降低其作为独立贡献的强调。\n\n**N2** [Critical] 与 Markovian Chains (Geng et al., 2026) 的区分度不足\n- Markovian Chains 同样研究 continuation chains under fixed parameters，文档了 attractor dynamics。本文的区分仅在于 location/shape 分解和 ordinal classification。但 attractor dynamics 本质上就是 location drift 的收敛现象。\n- 建议：增加系统性对比表，明确差异。\n\n**N3** [Critical] Instruction-tuned models 下 DDR 信号严重退化\n- OLMo-2-1B instruction tuning 后几乎丧失所有 depth signal。现实中绝大多数 LLM 输出来自 instruction-tuned models，base-model-only scope 与 motivation narrative 存在张力。\n- 建议：Abstract 更早限定 scope；讨论为何 instruction tuning 破坏 DDR。\n\n### Should-Fix 问题\n\n**W1** [Major] Downstream utility 为 null result，削弱实际 motivation\n- depth-aware curation ≈ random subsampling (TOST equivalence)。直接削弱 Introduction 中 data governance motivation。\n\n**W2** [Major] 术语 \"entropy\" 用作 NLL 的简写可能误导读者\n- Token-level NLL 和 Shannon entropy 是不同的量。对强调 statistical rigor 的 empirical study 来说不够精确。\n\n**W3** [Minor→Major] `attractor_cycles` bib entry 缺少 title 字段\n\n**W4** [Minor] Proof-of-concept classifier 的定位在正文各处不完全一致\n- Abstract 称 binary F1=0.694，但实际 0.694 是 binary (gen-1 vs gen-2+) 而非传统的 binary (human vs machine)。\n\n**W5** [Minor] 14B preliminary evidence 的报告方式需斟酌\n\n### Questions\nQ1. 不同 top-p 值下 shape stability 是否被打破？\nQ2. DDR location drift 与 Markovian Chains attractor convergence 是否定量等价？\nQ3. Instruction tuning 破坏 DDR 的 mechanistic explanation？\nQ4. 如果 instruct 不 work，主要应用场景是什么？\nQ5. Downstream utility n=3 seeds 是否会增加？"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "text": "## 交叉审稿：请逐条回应 Reviewer 2 的审稿意见\n\n以下是 Reviewer 2（新颖性 + 完整性）的完整审稿意见。请逐条回应：\n- **[AGREE]** 同意并说明理由\n- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）\n\n注意：你需要回应所有 Must-Fix (N1, N2, N3) 和 Should-Fix (W1-W5) 问题。Minor 问题可选择性回应。\n\n---\n\n## Reviewer 2 的完整审稿意见\n\n### Overall: 3.5 (Borderline Conference)\n\n### Must-Fix 问题\n\n**N1** [Critical] Shape stability 可能是固定采样机制的 trivial 推论\n- Section 5 自己承认 top-p truncation preserves functional form of conditional distribution。既然 top-p 截断在固定参数下天然保持条件分布的函数形式，shape stability 就不是 emergent property，而是采样机制的直接推论。\n- 建议：明确讨论 shape stability 在什么条件下会被打破；或降低其作为独立贡献的强调。\n\n**N2** [Critical] 与 Markovian Chains (Geng et al., 2026) 的区分度不足\n- Markovian Chains 同样研究 continuation chains under fixed parameters，文档了 attractor dynamics。本文的区分仅在于 location/shape 分解和 ordinal classification。但 attractor dynamics 本质上就是 location drift 的收敛现象。\n- 建议：增加系统性对比表，明确差异。\n\n**N3** [Critical] Instruction-tuned models 下 DDR 信号严重退化\n- OLMo-2-1B instruction tuning 后几乎丧失所有 depth signal。现实中绝大多数 LLM 输出来自 instruction-tuned models，base-model-only scope 与 motivation narrative 存在张力。\n- 建议：Abstract 更早限定 scope；讨论为何 instruction tuning 破坏 DDR。\n\n### Should-Fix 问题\n\n**W1** [Major] Downstream utility 为 null result，削弱实际 motivation\n- depth-aware curation ≈ random subsampling (TOST equivalence)。直接削弱 Introduction 中 data governance motivation。\n\n**W2** [Major] 术语 \"entropy\" 用作 NLL 的简写可能误导读者\n- Token-level NLL 和 Shannon entropy 是不同的量。对强调 statistical rigor 的 empirical study 来说不够精确。\n\n**W3** [Minor→Major] `attractor_cycles` bib entry 缺少 title 字段\n\n**W4** [Minor] Proof-of-concept classifier 的定位在正文各处不完全一致\n- Abstract 称 binary F1=0.694，但实际 0.694 是 binary (gen-1 vs gen-2+) 而非传统的 binary (human vs machine)。\n\n**W5** [Minor] 14B preliminary evidence 的报告方式需斟酌\n\n### Questions\nQ1. 不同 top-p 值下 shape stability 是否被打破？\nQ2. DDR location drift 与 Markovian Chains attractor convergence 是否定量等价？\nQ3. Instruction tuning 破坏 DDR 的 mechanistic explanation？\nQ4. 如果 instruct 不 work，主要应用场景是什么？\nQ5. Downstream utility n=3 seeds 是否会增加？"
  }
}
```

</details>

---


### Tool result

_source line 2679 · 2026-05-21T02:42:40.672476+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1712
}
```

</details>

---


### Assistant

_source line 2680 · 2026-05-21T02:42:46.183705+00:00_

交叉分享已派发。等待两位 Reviewer 的逐条 [AGREE]/[REBUT] 回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director"
}
```

</details>

---


## Round 234

## Round 234

2 recorded events


### User

_source line 2681 · 2026-05-21T02:42:48.975733+00:00_

[Reviewer 2 审稿结果]:
审稿报告已提交给 Review Director。

**总结**：以 Reviewer 2 身份完成了针对 "Depth Fingerprinting" 论文的新颖性 + 完整性审查，给出 Overall 3.5 (Borderline Conference)。

主要发现：
- **3 个 Critical 问题**：(1) shape stability 可能是固定采样机制的 trivial 推论而非 novel insight；(2) 与 Markovian Chains (Geng et al., 2026) 重叠显著，区分度不足；(3) instruction-tuned models 下信号退化 3.7 倍，与 motivation narrative 存在张力
- **5 个 Should-Fix**：null downstream utility、"entropy" 术语误导、`attractor_cycles` bib 缺 title、classifier 数值表述不一致、14B evidence 报告方式
- **格式合规**：全部通过（8 页正文、匿名、Limitations/Ethics 齐全）
- **引用完整性**：66 条引用，0 orphan，0 missing，无重大遗漏

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 2682 · 2026-05-21T02:42:53.878833+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director"
}
```

</details>

---


## Round 235

## Round 235

2 recorded events


### User

_source line 2683 · 2026-05-21T02:44:12.737821+00:00_

[Reviewer 2 审稿意见]:

# Reviewer 2 交叉回应 Reviewer 1 审稿意见

---

## Must-Fix 问题

**[AGREE] R1-N1: k=2 聚类在 7 个数据点上的 "data-driven" 声明过强**

同意 R1 的判断。对 7 个特征点做 k=2 聚类在统计上接近 trivial——任何存在基本分离结构的小样本集合都能产生可观的 silhouette。论文 Abstract 中称 "data-driven clustering (silhouette=0.632)" 给人一种由数据驱动发现的印象，实际上 7 点 k-means 更像是对先验直觉的定量确认。

R1 提出的 per-generator 层面聚类（7×8=56 点）是可操作的改进方向。我补充一点：论文 Appendix V 的 holdout generator split validation（Table 29-30）实际上提供了比 k-means 更有说服力的 partition robustness 证据——split A 和 split B 产生了一致的 DDR zone 分配。建议作者在修改时将 "data-driven" 的重心从 k-means silhouette 转移到 generator-split consistency 上。

---

**[AGREE with nuance] R1-N2: tail_decay 的 near-stationary 分类证据不足**

同意 tail_decay 在 ε=0.20 下仅 4/8 通过 TOST 是一个实质性的 concern。从我自己的审查来看（我的 N1），shape stability 作为核心贡献本身就可能是采样机制的 trivial 推论。tail_decay 作为 shape 组中最弱的特征被质疑，进一步削弱了 shape stability 作为独立发现的力度。

但我不完全同意 R1 建议的 3/2/2 分区方案（将 entropy_std 和 tail_decay 均移入 intermediate）。entropy_std 的 Cohen's d=0.76-1.17 和 Spearman |ρ| 在所有 generator 上一致为 large effect，将其从 drifting 降级为 intermediate 缺乏数据支持。tail_decay 单独降级为 intermediate 更合理，这会导致 3/2/1+1 的格局（3 drifting, 2 intermediate, 1 near-stationary entropy_min + 1 boundary case tail_decay）。

实际上，这一修改不会颠覆论文的核心叙事——location features 仍然单调漂移，entropy_min 仍然稳定。但它确实要求作者更诚实地处理 tail_decay 的 boundary status，而非将其归入 near-stationary 以构建更整齐的二分法叙事。

---

## Should-Fix 问题

**[AGREE] R1-W1: 五个 effect-size metrics 的 "convergent validation" 存在冗余**

完全同意。Cohen's d 和 Glass's Δ 在数学上只是方差选择的差异（pooled vs reference group），KS statistic 也主要捕获 location shift（在 shape 稳定时）。真正提供独立信息的仅有 Cliff's δ（ordinal/rank-based）和 CV shift（变异系数）。论文将五个指标称为 "five independent effect-size metrics"（Abstract, Section 4.2）属于 overclaim。

建议作者保留所有五个指标的报告（附录中的完整数据是有价值的），但在主文中降低 "independent" 的修辞强度，改为 "five complementary effect-size measures"，并明确说明哪些指标之间存在高度相关性。

---

**[AGREE] R1-W2: Base model scope 下泛化性声明需更严格限定**

与我的 N3 一致。Appendix K 的 instruction-tuned model 结果（F1 退化 3.7×）是论文最大的实际适用性限制。R1 指出 Discussion 中 data curation 讨论暗示了比证据支撑更广的适用性——我在审查中也标注了 Introduction 的 motivation narrative（"7-17% of scientific publications contain LLM-modified content"）与 base-model-only scope 之间的张力。这些场景中的文本几乎全部来自 instruction-tuned models。

两位 reviewer 在此问题上形成共识，作者应在修改中优先处理。

---

**[REBUT with partial agreement] R1-W3: Baseline 比较的公平性**

R1 指出 4-det+surface (Bin F1=0.708) 略优于 7-feature ensemble (0.705)，质疑 DDR 分解的增量价值。这个观察是准确的，但我认为 R1 的结论过强：

1. **论文的主要贡献不是分类器**。论文明确将分类器定位为 "proof-of-concept"（Abstract, Section 3.4）。DDR 的核心价值在于 analytical framework（将 distributional shift 分解为 location/shape），而非分类性能的 SOTA 追求。

2. **7-feature ensemble 在 3-class 上优于 baselines**。Table 2（p.5）显示 7-feature ensemble 的 3-class LOGO F1=0.694，而 4-det+surface 的对应数据需要从附录获取。论文的核心 task 是 ordinal depth classification（3-class），不是 binary detection。仅比较 binary F1 不公平地忽略了 DDR features 在 ordinal task 上的优势。

3. 但 R1 提出的核心问题——"为什么需要 DDR 分解？"——是合理的。如果 detection scores 已经隐式编码了 depth 信息，DDR 分解的 added value 需要更明确的论证。建议作者补充一个分析：DDR partition 如何指导 feature selection/engineering，以及 DDR 的 interpretability 相对于 black-box detection scores 的优势。

---

**[AGREE] R1-W4: TOST ε=0.20 的循环论证**

R1 的分析精确：特征先按 d<0.20 分类为 near-stationary → LOFO 验证这些特征贡献小 → LOFO 结果用来 justify ε=0.20 的合理性。这确实是一个方法论上的循环。

但我想补充一个 mitigating factor：ε=0.20 的选择并非完全 ad hoc，它对应 Cohen (1988) 的 "small effect" 传统阈值（论文 Appendix U 也引用了 Cohen）。因此存在 external justification。然而，如果作者能展示 partition 对 ε 的 robustness（如在 ε∈[0.15, 0.25] 范围内 partition 是否稳定），将大幅缓解 R1 的 concern。实际上 Appendix V (Table 30) 的 partition stability across ε 分析已经部分做到了这一点——showing that "the three drifting features remain drifting for all ε∈[0.10, 0.75]"。建议作者在主文中更显著地引用此 robustness check。

---

**[AGREE] R1-W5: Null downstream result 应在主文中讨论**

完全同意。这也是我的 W1。Appendix M 的 TOST equivalence result（depth-aware curation ≈ random subsampling）直接关系到论文的 practical motivation，不应仅在附录中出现。

主文 Discussion (Section 5) 目前讨论了 model collapse 区分和 instruction-tuning limitations，但对 downstream utility 的 null result 只字未提。建议在 Discussion 或 Conclusion 中加入一段话，明确承认当前证据不支持 depth-aware curation 的 downstream value proposition，并讨论可能的原因。

---

## Minor 问题（选择性回应）

**[AGREE] R1-M1: entropy_min Cliff's δ 矛盾**
如果 entropy_min 的 Cliff's δ 显示 non-negligible effect 而 Cohen's d 显示 near-zero，这恰好说明 W1 中指出的 metrics 非独立性问题。不同 effect-size metrics 给出矛盾信号时，应讨论原因而非只报告一致的那些。

**[AGREE] R1-M3: Chain depth=4 的选择未充分 justify**
论文选择最大 generation depth=4 但未在主文中解释为什么不是 3 或 5。Appendix D 的 finer-grained evaluation (5-class) 部分回答了这个问题，但主文中应至少提供一句 justification。

**[No comment] R1-M2, M4-M6**: 未在我的审查中重点关注，无额外补充。

---

## 对 Reviewer 1 Questions 的补充意见

**Q3 (QLoRA instruct 恢复 vs DDR 失效)**: 这是一个我也关注的张力。如果 QLoRA fine-tuning 能在 instruct models 上恢复分类性能（Appendix E, Table 6），但 DDR 的 location/shape partition 不再成立（Appendix K 的 summary statistics 显示 entropy_mean 变为 near-stationary），那么恢复的分类能力可能来自 DDR 以外的信号（如 stylistic patterns, formatting artifacts）。这质疑了 DDR 作为 "the" explanatory framework 的普适性。建议作者在修改中讨论 QLoRA 分类器在 instruct 上学到的是什么——是 DDR features 还是 confound features？

**Q4 (downstream null result 下 data curation 的 value)**: 与 R1 一致。如果 depth 信号不能转化为 downstream utility，论文需要明确 reframe 其 value proposition——从 "depth-aware data curation improves model quality" 转向 "depth classification as a data provenance / audit tool"。后者的价值主张不依赖于 downstream performance。

---

## 总结

与 Reviewer 1 在以下问题上形成共识：
- k-means 聚类 "data-driven" 声明过强（N1）
- tail_decay near-stationary 分类证据不足（N2，我有 nuanced disagreement on 具体方案）
- Five "independent" metrics 是 overclaim（W1）
- Base-model-only scope 限制被低估（W2，与我的 N3 一致）
- Null downstream result 需要主文讨论（W5，与我的 W1 一致）

与 Reviewer 1 部分分歧：
- Baseline 比较公平性（W3）：R1 的观察准确，但结论过强——分类器不是论文的主要贡献，且应以 3-class 而非 binary 为主要比较维度
- TOST 循环论证（W4）：循环存在，但 ε=0.20 有 Cohen (1988) 的 external justification，且 Appendix V 已提供 partial robustness evidence

维持我的 Overall: 3.5 (Borderline Conference) 评分不变。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 2684 · 2026-05-21T02:44:20.754091+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director"
}
```

</details>

---


## Round 236

## Round 236

2 recorded events


### User

_source line 2685 · 2026-05-21T02:44:23.541281+00:00_

[Reviewer 2 审稿结果]:
交叉审稿回应已提交。对 R1 的 7 个主要问题（N1-N2, W1-W5）逐条给出了 [AGREE] 或 [REBUT] 判断：

- **6 项同意**：k-means data-driven overclaim (N1)、tail_decay 分类不足 (N2, 但对具体分区方案有 nuanced disagreement)、five "independent" metrics overclaim (W1)、base-model scope (W2)、TOST 循环 (W4)、null downstream (W5)
- **1 项部分反驳**：baseline 比较公平性 (W3)——分类器是 proof-of-concept，应以 3-class 而非 binary 为主比较维度

维持 Overall 3.5 评分。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 2686 · 2026-05-21T02:44:28.180885+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director"
}
```

</details>

---


## Round 237

## Round 237

12 recorded events


### User

_source line 2687 · 2026-05-21T02:45:23.423089+00:00_

[Reviewer 1 审稿意见]:

# Reviewer 1 交叉审稿：逐条回应 Reviewer 2 意见

---

## Must-Fix 问题回应

### [REBUT] R2-N1: Shape stability 是 top-p 的 trivial 推论

R2 论点成立的前提是：如果机制可解释，发现就不重要。我不同意这个逻辑。

**反驳理由：**

1. **机制可解释 ≠ 经验上 trivial。** 万有引力的"解释"是质量弯曲时空，但引力波的经验检测仍然是重大发现。DDR 的贡献不是 shape stability 本身（§5 确实给出了机制解释），而是 *shape stability 与 location drift 之间的定量不对称性可被利用做 depth classification*。这一可操作性推论并非从 top-p 机制直接推出的。

2. **温度消融表明 shape stability 不是无条件成立的。** Appendix Z.1 (Table 38) 显示在 τ=0.9 时，tail_decay 和 entropy_max 已从 near-stationary 漂移到 intermediate（|d| 从 0.09 升至 0.11-0.15），而 τ=1.0 时 location signal 几乎完全坍缩（§5: ρ 从 -0.60 降至 -0.002）。如果 shape stability 真的是 sampling 机制的 trivial 推论，它不应该随温度变化——但它确实在高温下开始被打破。这恰恰说明 shape stability 是一个有边界条件的经验现象，不是一个定理。

3. **论文已提供两个可检验预测并得到验证（§5 第 1 段）：** (a) 增加采样随机性应削弱 location drift → 在 t=1.0 时确认；(b) 语义保持约束应减弱 drift → elaboration prompts 下 F1 从 0.781 降至 0.730 确认。这超越了"trivial 推论"的层次。

**但我部分同意的是：** 论文应更清楚地区分 mechanistic explanation（§5）和 empirical contribution（§4.2）。当前叙事中两者有所混淆，导致 R2 产生了"这只是对已知机制的描述"的印象。建议在§5 开头明确：机制解释是 post-hoc rationalization，核心贡献是经验性的分解和分区。

---

### [AGREE] R2-N2: 与 Markovian Chains 的区分度不足

同意需要更系统的对比。

**理由：**

1. §2.2 的区分确实存在（"DDR isolates *what* converges from what is preserved"），但停留在单句叙述层面，缺乏定量对比。
2. 两篇工作都研究 fixed-parameter inference chains 下的 convergence dynamics，核心 setup 重叠度高。论文声称的区分点——location/shape 分解和 ordinal classification——需要更强的论证来说明这不仅仅是对同一现象的不同视角。
3. §2.2 最后一段提到"三种方法独立收敛到约 3 个可区分深度类"这一有趣的 convergence，但这恰好支持了 R2 的观点：如果结论一致，区分在哪里？

**不过 R2 说 "attractor dynamics 本质上就是 location drift 的收敛现象" 是一个过度简化。** Markovian Chains 的 attractor dynamics 描述的是完整分布的收敛（包括 shape），而 DDR 的关键发现是 shape 不收敛（或极缓慢收敛）。如果作者能量化 Markovian Chains 的 attractor 是否也存在 location/shape 不对称性，这将大大强化区分论证。

**建议：** 增加一张对比表（如 R2 所建议），维度包括：(1) chain type (continuation vs paraphrase), (2) 是否分解 location/shape, (3) 是否做 ordinal classification, (4) generator 规模和数量, (5) 核心 insight。

---

### [AGREE] R2-N3: Instruction-tuned models 下 DDR 退化

同意，且我在自己的审稿中也将此列为 Should-Fix (W2)。

**补充观点：**

1. 数据更详细地说明了退化程度：OLMo-Instruct 3-class F1=0.575（vs base 0.754），DDR silhouette 从 0.632 降至 0.338（§5 第 5 段），feature correlations 甚至出现反转。这不仅是"退化"，而是 DDR 结构的根本性改变。

2. 但 R2 将此评为 Critical 我认为**稍偏重**。原因：(a) 论文明确将 scope 限定为 base models（§1 最后一句："We restrict to base (pretrained) models to isolate the generation dynamics from alignment artifacts"）；(b) QLoRA 在 instruct data 上恢复到 0.89-0.91（Appendix K），说明 token-level depth signal 存在但 DDR 的 7-feature 分解无法捕获——这本身是一个有信息量的 negative result。

3. 我同意 R2 的建议：Abstract 应更早限定 scope。当前 Abstract 第 1 句直接说 "LLM outputs re-enter generation pipelines"，暗示了比 base-model-only 更广的适用性。

---

## Should-Fix 问题回应

### [AGREE] R2-W1: Downstream utility null result 削弱 motivation

完全同意。我在自己的审稿中也标记为 W5。

Appendix M (Table 19) 明确显示 depth-aware curation (ppl=2.387) 不优于 random subsampling (ppl=2.367)，TOST 确认等价。但 §5 第 2 段仍然讨论 "training-data curation pipeline" 应用场景而未提及此 null result。这是 selective reporting。

---

### [REBUT] R2-W2: "entropy" 用作 NLL 的简写

**部分反驳。**

§3.3 第 2 段已明确声明："We use 'entropy' as shorthand for token-level NLL throughout, following convention in prior detection work; these are point-wise NLL values, not Shannon entropy of the full distribution." 这不是遗漏，而是有意识的术语选择并附带了解释。

Prior detection work（DetectGPT, Fast-DetectGPT, Binoculars）普遍使用类似的 NLL-based "entropy" 简写。在该领域的读者不太可能产生混淆。

**但 R2 有一点 valid concern：** 对于来自 information theory 背景的读者，这个简写确实可能造成初始混淆。建议将 §3.3 的术语说明移至首次使用（§1 或 §3.1），而非埋在 feature extraction 的中间段落。这是 presentation improvement，不是 soundness 问题。

---

### [REBUT] R2-W3: `attractor_cycles` bib entry 缺少 title 字段

**这一 finding 不正确。**

我检查了 `references.bib` (line 324-327)：

```bibtex
@inproceedings{attractor_cycles,
  title = {{Unveiling Attractor Cycles in {LLM}s}},
  author = {Wang, Yibo and Li, Haotian and Tan, Boyu and ...},
  booktitle = {Proceedings of the Annual Meeting of the ACL},
```

`attractor_cycles` 条目有完整的 title 字段（"Unveiling Attractor Cycles in LLMs"）。R2 可能查看了不同版本的 bib 文件，或将其与另一个条目混淆。

---

### [AGREE] R2-W4: Binary F1=0.694 的定义在 Abstract 中可能误导读者

同意。

Abstract 说 "leak-free binary F1=0.694 under leave-one-generator-out evaluation"，但未明确说明 "binary" 指的是 gen-1 vs gen-2+（排除 gen-0）。对于 AI text detection 领域的读者，"binary" 的默认理解是 human vs machine。虽然 §4.1 第 1 段有详细定义，但 Abstract 是大多数读者首先（可能唯一）阅读的部分。

建议在 Abstract 中改为 "leak-free binary F1=0.694 (gen-1 vs gen-2+, excluding shared gen-0 seeds)" 以消除歧义。

---

### [AGREE] R2-W5: 14B preliminary evidence 的报告方式

部分同意。

§5 第 3 段报告 Qwen3-14B-Base 结果时使用了 "preliminary evidence" 限定语，且明确了样本量（single generator）。但将具体数字（d=0.78-1.12, ρ attenuates by 21-35%）放在 Discussion 正文中，读者可能高估其证据等级。

建议将 14B 结果移至 Appendix（类似 Gemma-2-2B 在 Appendix AB 的处理方式），在 Discussion 中仅用一句话引用。

---

## R2 Questions 的简要评论

**Q1 (不同 top-p 值下 shape stability)**：好问题。论文未测试 top-p 变化，仅固定 p=0.9（§3.2）。cross-temp 附录有脚注提到 t=1.0 时用了 p=0.95（Appendix P 脚注 6），但未分离 top-p 和温度效果。这是一个 gap。

**Q2 (DDR vs attractor convergence 定量等价性)**：关键问题。如果两者定量等价，DDR 就只是 Markovian Chains 的 feature-level restatement。作者需要回答。

**Q3 (Instruct 破坏 DDR 的机制)**：§5 第 5 段给出了 "alignment fundamentally reshapes the generation dynamics" 的解释，但缺乏具体机制（是 RLHF 的 reward shaping？还是 SFT 的 format constraints？还是 length regulation？）。我在 W2 中也提出了同样的 concern。

**Q4 (主要应用场景)**：论文在 §5 第 2 段给出了 corpus-level auditing 的场景，这对 base-model 生成的 pretraining data 是合理的。但如 W1 中讨论，downstream utility 的 null result 削弱了此叙事。

**Q5 (Downstream n=3 seeds)**：合理的后续实验请求，但我认为这不应是接收条件——Appendix M 的 null result 已经通过 TOST 确认等价，增加 seeds 不太可能改变结论方向。

---

## 与我自己审稿的 Alignment 总结

| R2 Issue | R1 对应 | 一致性 |
|----------|---------|--------|
| R2-N1 (shape trivial) | — (R1 未覆盖) | 部分反驳 |
| R2-N2 (Markovian Chains) | — (R1 未覆盖) | 同意 |
| R2-N3 (Instruct failure) | R1-W2 | 同意（但 severity 从 Critical 降为 Major） |
| R2-W1 (Downstream null) | R1-W5 | 完全同意 |
| R2-W2 (Entropy terminology) | — | 部分反驳 |
| R2-W3 (bib error) | — | 事实性错误，反驳 |
| R2-W4 (Binary F1 ambiguity) | R1-M4 | 同意 |
| R2-W5 (14B evidence) | — | 部分同意 |

**总体评价：** R2 的 N2（Markovian Chains 区分）和 W1（downstream null result）是有效的高优先级意见。N1（shape trivial）有合理内核但结论过强——shape stability 是有边界条件的经验发现，不是 trivial 推论。W3（bib error）是事实性错误，建议核实。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 2688 · 2026-05-21T02:45:58.312272+00:00_

called mcp__agent-ml-research__get_visual_check_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_visual_check_status</summary>

```json
{
  "project": "gen-depth-fingerprint"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "tool_args": {
    "project": "gen-depth-fingerprint"
  }
}
```

</details>

---


### Tool result

_source line 2689 · 2026-05-21T02:45:58.513566+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"done\", \"started_at\": \"2026-05-21T02:32:09.743172+00:00\", \"completed_at\": \"2026-05-21T02:36:07.046713+00:00\", \"findings\": [{\"severity\": \"warning\", \"dimension\": \"page 1-4\", \"message\": \"连续 4 页纯文本无任何 display item（figure/table/equation）。审稿人前 2 分钟只看到密集文字，无法建立视觉锚点。建议在 page 2 前插入概念图/pipeline 图或将 Figure 1 前移\"}, {\"severity\": \"warning\", \"dimension\": \"page 1-2\", \"message\": \"缺少方法概览图（overview/pipeline figure）。作为实证论文，审稿人期望在 Method 开始前看到一个直观展示 generation chain → feature extraction → classification 流程的概念图\"}, {\"severity\": \"warning\", \"dimension\": \"page 7\", \"message\": \"display item 过度密集：2 figures (Fig 2, Fig 3) + 1 table (Table 2) 挤在同一页，而相邻的 page 4 和 page 8 全是纯文本。建议分散 float 位置\"}, {\"severity\": \"warning\", \"dimension\": \"page 8-9\", \"message\": \"Discussion + Conclusion + Limitations + Ethics 连续 2 页纯文本，虽然章节性质决定了文字为主，但仍可考虑将一个核心结果汇总表/图移入 Discussion\"}, {\"severity\": \"info\", \"dimension\": \"page 6\", \"message\": \"Figure 1 使用 8+ 条彩色线表示不同 generator，线条在小尺寸下区分度不足，尤其 (a) Entropy Mean 和 (b) Hapax Ratio 面板中多条线重叠严重。建议使用 marker shape + line style 辅助区分，或按 generator family 分组\"}, {\"severity\": \"info\", \"dimension\": \"page 7\", \"message\": \"Figure 2（DDR 散点图）和 Figure 3（F1 vs cost）均为单栏宽度，点标记和轴标签字号偏小，打印后可读性受限\"}, {\"severity\": \"info\", \"dimension\": \"page 5\", \"message\": \"Table 1 最优结果已加粗，格式规范；但 95% CI 列与主 F1 列紧挨，视觉上略拥挤\"}, {\"severity\": \"info\", \"dimension\": \"page 14\", \"message\": \"Figure 4 violin plots 占满整页，7 个子图色彩鲜明可读。但 hapax_ratio 子图的 y 轴范围（0-1.0）使得大部分数据集中在底部，可考虑裁剪 y 轴\"}, {\"severity\": \"info\", \"dimension\": \"page 24\", \"message\": \"Figure 8 和 Figure 9 共占一整页，Figure 9 UMAP 两面板中的散点颜色与 Figure 8 中的 generator 颜色体系不一致\"}, {\"severity\": \"info\", \"dimension\": \"page 33\", \"message\": \"最后一页内容约占 65%，未充分利用空间\"}, {\"severity\": \"info\", \"dimension\": \"全局\", \"message\": \"正文 8 页仅 5 个 display items（3 fig + 2 table），对于以实证为主的论文偏少（通常 5-8 个）。大量实验结果被推入 appendix，正文信息密度可提升
…[truncated 103 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 2690 · 2026-05-21T02:45:58.513947+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "gen-depth-fingerprint"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "gen-depth-fingerprint"
  }
}
```

</details>

---


### Tool result

_source line 2691 · 2026-05-21T02:45:58.664634+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 150
}
```

</details>

---


### Tool call

_source line 2692 · 2026-05-21T02:46:52.908604+00:00_

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
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
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

_source line 2693 · 2026-05-21T02:46:53.310318+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "ToolSearch",
  "elapsed_ms": 401
}
```

</details>

---


### Tool call

_source line 2694 · 2026-05-21T02:50:16.381048+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "gen-depth-fingerprint",
  "issues_yaml": "\n# === Round 29-34 历史 Issues（保留完整记录）===\n\n- id: \"R29-N1\"\n  summary: \"Base-model-only scope 未在 Abstract 标注\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 29\n  last_seen_round: 32\n  mentions:\n    - {round: 29, reviewers: \"R1+R2\", note: \"共识: Abstract 必须标注 base-model scope\"}\n    - {round: 31, reviewers: \"R1+R2\", note: \"W1: Title/Abstract 仍需 base-model qualifier\"}\n    - {round: 32, reviewers: \"R1+R2\", note: \"升级: 实验设计仅覆盖 base model, 建议扩展或限定 scope\"}\n  action_items:\n    - {round: 29, action: \"Abstract 加 base (pretrained) qualifier\", assigned_to: Agent, status: done}\n    - {round: 32, action: \"Abstract/Conclusion 已有 qualifier; instruct in Discussion\", assigned_to: Director, status: done}\n  resolution: \"Abstract L3 'eight base-model generators'; L7 'restricted to base models'. Title 保持不变(Reviewer 确认). Instruct limitations fully documented.\"\n  resolution_round: 32\n\n- id: \"R29-N2\"\n  summary: \"Downstream TOST underpowered (n=3) + Abstract overclaim\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 29\n  last_seen_round: 34\n  mentions:\n    - {round: 29, reviewers: \"R1+R2\", note: \"n=3 seeds, Abstract 省略 preliminary\"}\n    - {round: 31, reviewers: \"R1+R2\", note: \"W3: TOST n=3 underpowered\"}\n    - {round: 32, reviewers: \"R1+R2\", note: \"升级为 null result: depth-aware curation 不优于 random\"}\n    - {round: 34, reviewers: \"R1+R2\", note: \"RESOLVED: Abstract 完全移除 downstream claim; Appendix M 坦诚呈现 null result\"}\n  action_items:\n    - {round: 29, action: \"Abstract 加 preliminary qualifier\", assigned_to: Agent, status: done}\n    - {round: 32, action: \"Abstract/Conclusion downstream reframing\", assigned_to: Director, status: done}\n  resolution: \"Abstract 完全移除 downstream claim. Appendix M 保留 null result 作为补充材料.\"\n  resolution_round: 34\n\n- id: \"R29-N3\"\n  summary: \"DDR 新颖性 incremental — 缺 concurrent work 系统对比表\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 29\n  last_seen_round: 31\n  mentions:\n    - {round: 29, reviewers: \"R1+R2\", note: \"区分不充分\"}\n    - {round: 31, reviewers: \"R1+R2\", note: \"W12: differentiation insufficient\"}\n  action_items:\n    - {round: 29, action: \"§2.2 加系统对比表\", assigned_to: Agent, status: done}\n  resolution: \"related_work.tex concurrent-comparison table added\"\n  resolution_round: 31\n\n- id: \"R29-N4\"\n  summary: \"QLoRA gap 削弱方法论贡献 — 需重定位\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 29\n  last_seen_round: 34\n  mentions:\n    - {round: 29, reviewers: \"R1+R2\", note: \"7-feat vs QLoRA gap\"}\n    - {round: 31, reviewers: \"R1+R2\", note: \"W4: contribution identity crisis\"}\n    - {round: 32, reviewers: \"R1+R2\", note: \"Contribution 3 仍以 classifier 为卖点\"}\n    - {round: 34, reviewers: \"R1+R2\", note: \"RESOLVED: Contribution 3 = 'Proof-of-concept classifier'; 5处一致传达分析工具定位\"}\n  action_items:\n    - {round: 29, action: \"§1 contribution 重排\", assigned_to: Agent, status: done}\n    - {round: 32, action: \"Proof-of-concept framing\", assigned_to: Director, status: done}\n  resolution: \"Intro L14 'proof of concept'; Contribution 3 'Proof-of-concept classifier with boundary analysis'; results.tex L17+L142; Discussion L11 — 五处一致.\"\n  resolution_round: 34\n\n- id: \"R29-W1\"\n  summary: \"Gemma-2-2B gen-1 F1=0.036 anomaly 解释不充分\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 29\n  last_seen_round: 31\n  mentions:\n    - {round: 29, reviewers: \"R1+R2\", note: \"挑战 DDR universality\"}\n  action_items:\n    - {round: 29, action: \"appendix_9gen_scale 扩展\", assigned_to: Agent, status: done}\n  resolution: \"appendix_9gen_scale expanded\"\n  resolution_round: 31\n\n- id: \"R29-W2\"\n  summary: \"Cross-model chain F1=0.830 可能混淆 depth signal 与 generator identity\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 29\n  last_seen_round: 34\n  mentions:\n    - {round: 29, reviewers: \"R1+R2\", note: \"sample-level CV vs LOGO 矛盾\"}\n    - {round: 31, reviewers: \"R1+R2\", note: \"W11: may be OOD artifact\"}\n    - {round: 32, reviewers: \"R1+R2\", note: \"应标为 upper bound\"}\n    - {round: 34, reviewers: \"R1+R2\", note: \"RESOLVED: footnote 'not directly comparable' + single-gen transfer control\"}\n  action_items:\n    - {round: 29, action: \"results.tex 标注 exploratory\", assigned_to: Agent, status: done}\n    - {round: 32, action: \"caveats added\", assigned_to: Director, status: done}\n  resolution: \"results.tex footnote + L15 single-gen transfer. Caveats sufficient.\"\n  resolution_round: 34\n\n- id: \"R29-W3\"\n  summary: \"温度限制(t<0.9)未在 Abstract 标注\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 29\n  last_seen_round: 32\n  mentions:\n    - {round: 29, reviewers: \"R1+R2\", note: \"cross-temperature transfer 不对称\"}\n  action_items:\n    - {round: 29, action: \"Abstract 加 standard decoding qualifier\", assigned_to: Agent, status: done}\n  resolution: \"Abstract L4 'nucleus sampling (p=0.9, t<=0.7)'\"\n  resolution_round: 31\n\n- id: \"R29-W4\"\n  summary: \"DDR partition 3/1/3 intermediate 定义不够 principled\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 29\n  last_seen_round: 34\n  mentions:\n    - {round: 29, reviewers: \"R1+R2\", note: \"epsilon sensitivity 未展示\"}\n    - {round: 31, reviewers: \"R1+R2\", note: \"W13: threshold arbitrary\"}\n    - {round: 32, reviewers: \"R1\", note: \"升级 Critical: k-means k=2 唯一 clean split\"}\n    - {round: 34, reviewers: \"R1+R2\", note: \"RESOLVED: binary primary partition + k=3 degradation + domain-informed refinement\"}\n  action_items:\n    - {round: 29, action: \"partition stability 分析\", assigned_to: Agent, status: done}\n    - {round: 32, action: \"Restructure 4.2: 2-way primary\", assigned_to: Director, status: done}\n  resolution: \"k=2 binary (sil=0.632); k=3 degradation (0.499); 3/1/3 = domain-informed refinement.\"\n  resolution_round: 34\n\n- id: \"R29-W5\"\n  summary: \"Baseline 范围偏窄 + 比较结构性不公平\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 29\n  last_seen_round: 35\n  mentions:\n    - {round: 29, reviewers: \"R1+R2\", note: \"缺 multi-feature detector\"}\n    - {round: 31, reviewers: \"R1+R2\", note: \"Bonferroni invalidates McNemar\"}\n    - {round: 32, reviewers: \"R1\", note: \"4-det ensemble 实际优于 7-feature\"}\n    - {round: 34, reviewers: \"R1+R2\", note: \"RESOLVED: honest presentation of 4-det+surface 0.708 > ours 0.705\"}\n    - {round: 35, reviewers: \"R1\", note: \"R1 再次质疑 baseline 公平性; R2 部分反驳: classifier 是 proof-of-concept, 应以 3-class 为主比较维度\"}\n  action_items:\n    - {round: 32, action: \"reframed\", assigned_to: Director, status: done}\n  resolution: \"4.3 honestly presents 4-det+surface marginally exceeding. R2 rebuts severity: DDR contribution is decomposition not classification.\"\n  resolution_round: 34\n\n- id: \"R29-W6\"\n  summary: \"Related work 引用缺失 + orphan bib entries\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 29\n  last_seen_round: 35\n  mentions:\n    - {round: 29, reviewers: \"R1+R2\", note: \"RAID 未引用; orphans\"}\n    - {round: 31, reviewers: \"R1+R2\", note: \"17 orphan bib entries\"}\n    - {round: 32, reviewers: \"R1+R2\", note: \"self_refine orphan; 6 new missing refs suggested\"}\n    - {round: 34, reviewers: \"R1+R2\", note: \"Wang et al. (ACL 2025) 仍未添加\"}\n    - {round: 35, reviewers: \"R1+R2\", note: \"本轮引用检查: 66条, 0 orphan, 0 missing. R2确认覆盖良好\"}\n  action_items:\n    - {round: 29, action: \"RAID cite + orphan cleanup\", assigned_to: Agent, status: done}\n    - {round: 32, action: \"self_refine deleted; 6 refs under verification\", assigned_to: Agent, status: done}\n    - {round: 34, action: \"Wang et al. added\", assigned_to: Director, status: done}\n  resolution: \"Round 35 确认: 66条引用, 0 orphan, 0 missing. 引用覆盖良好.\"\n  resolution_round: 35\n\n- id: \"R29-W7\"\n  summary: \"Diagnostic not curative 缺具体场景\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 29\n  last_seen_round: 31\n  mentions:\n    - {round: 29, reviewers: \"R1+R2\", note: \"需要 end-to-end 应用案例\"}\n  action_items:\n    - {round: 29, action: \"Discussion 加 2 个场景\", assigned_to: Agent, status: done}\n  resolution: \"discussion.tex 两个诊断场景\"\n  resolution_round: 31\n\n- id: \"R29-W8\"\n  summary: \"Per-generator F1 变异大 (0.633-0.724)\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 29\n  last_seen_round: 31\n  mentions:\n    - {round: 29, reviewers: \"R1+R2\", note: \"generator-unknown 场景实用性受限\"}\n  action_items:\n    - {round: 29, action: \"Discussion caveat\", assigned_to: Agent, status: done}\n  resolution: \"discussion.tex '9.1pp per-generator spread'\"\n  resolution_round: 31\n\n- id: \"R32-N1\"\n  summary: \"DDR 增量新颖性不清晰 — 可能是 diversity loss / mode-seeking 的重新表述\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 32\n  last_seen_round: 35\n  mentions:\n    - {round: 32, reviewers: \"R2+R1\", note: \"DDR 可能是 diversity loss 重新表述\"}\n    - {round: 34, reviewers: \"R1+R2\", note: \"RESOLVED: 'what converges vs what is preserved' framing\"}\n    - {round: 35, reviewers: \"R2\", note: \"R2-N1: Shape stability 可能是 top-p 采样机制的 trivial 推论; R1 REBUT: 温度消融证明非无条件成立, 有边界条件的经验发现. 分歧保留\"}\n  action_items:\n    - {round: 32, action: \"Discussion expanded: shape stability as novel contribution\", assigned_to: Director, status: done}\n    - {round: 35, action: \"区分 mechanistic explanation (post-hoc) 和 empirical contribution (DDR partition); 讨论 shape stability 在何条件下被打破\", assigned_to: Director, status: pending}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R32-N2\"\n  summary: \"Entropy min 分类存在根本性矛盾 (|rho|=0.40 标为 near-stationary)\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 32\n  last_seen_round: 34\n  mentions:\n    - {round: 32, reviewers: \"R1\", note: \"|rho|=0.40 vs d=0.016 vs delta=0.354 矛盾\"}\n    - {round: 34, reviewers: \"R1+R2\", note: \"RESOLVED: 'boundary feature' label + gen-0/gen-1 transition mechanism + k=2 placement\"}\n  action_items:\n    - {round: 32, action: \"Label as boundary feature\", assigned_to: Director, status: done}\n  resolution: \"results.tex L85 'boundary feature' with full qualification; Figure 2 caption aligned.\"\n  resolution_round: 34\n\n- id: \"R32-N3\"\n  summary: \"Tail_decay near-stationary 归类仅 4/8 generator 通过 TOST (epsilon=0.20)\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 32\n  last_seen_round: 35\n  mentions:\n    - {round: 32, reviewers: \"R1\", note: \"50% pass rate; OLMo d=0.22\"}\n    - {round: 34, reviewers: \"R1+R2\", note: \"RESOLVED: L89-91 three-sentence coverage\"}\n    - {round: 35, reviewers: \"R1+R2\", note: \"R1-N2: 4/8 TOST 通过率不足以支撑 near-stationary; R2 AGREE (但反对 R1 的 3/2/2 方案, 建议 tail_decay 单独降级为 intermediate). 共识: 主文应更诚实处理 tail_decay 的 boundary status\"}\n  action_items:\n    - {round: 32, action: \"Transparent reporting in main text\", assigned_to: Director, status: done}\n    - {round: 35, action: \"将 tail_decay 降级为 intermediate 或提供更强论证; 不应以 neat 二分法遮盖 50% 通过率\", assigned_to: Director, status: pending}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R32-W1\"\n  summary: \"分类性能 F1=0.694 定位为 detecting 但实为 proof-of-concept\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 32\n  last_seen_round: 34\n  mentions:\n    - {round: 32, reviewers: \"R1+R2\", note: \"~30% 错分率\"}\n    - {round: 34, reviewers: \"R1+R2\", note: \"RESOLVED: Discussion L11 'proof-of-concept, not a deployable system'\"}\n  action_items:\n    - {round: 32, action: \"Discussion proof-of-concept framing\", assigned_to: Director, status: done}\n  resolution: \"Intro L14, Contribution 3, Discussion L11 — all say 'proof-of-concept'.\"\n  resolution_round: 34\n\n- id: \"R32-W2\"\n  summary: \"TOST power analysis 缺失\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 32\n  last_seen_round: 34\n  mentions:\n    - {round: 32, reviewers: \"R1\", note: \"大样本 TOST 几乎总检测 equivalence\"}\n    - {round: 34, reviewers: \"R1+R2\", note: \"共识: SESOI+epsilon+caveat 足够, 不阻碍接收\"}\n  action_items:\n    - {round: 32, action: \"TOST power computation\", assigned_to: Agent, status: wont_fix}\n  resolution: \"SESOI justification + epsilon sensitivity + high-N masking acknowledged.\"\n  resolution_round: 34\n\n- id: \"R32-W3\"\n  summary: \"术语混淆: entropy 指代 NLL 不规范\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 32\n  last_seen_round: 35\n  mentions:\n    - {round: 32, reviewers: \"R2\", note: \"NLL 与 Shannon entropy 不同\"}\n    - {round: 35, reviewers: \"R2\", note: \"R2-W2 再次提出; R1 REBUT: 3.3 已有显式声明且符合领域惯例. 共识: presentation issue, 建议将术语说明移至首次使用处\"}\n  action_items:\n    - {round: 32, action: \"Existing clarification sufficient\", assigned_to: Director, status: wont_fix}\n  resolution: \"method.tex 3.3 L38 explicit clarification. Round 35 R1 confirms field convention. Suggestion: move disclaimer to first use.\"\n  resolution_round: 32\n\n- id: \"R32-W4\"\n  summary: \"附录 25 页过大, 关键结果应在主文讨论\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 32\n  last_seen_round: 32\n  mentions:\n    - {round: 32, reviewers: \"R2\", note: \"25 页附录\"}\n  action_items:\n    - {round: 32, action: \"Key numbers already in main text\", assigned_to: Director, status: wont_fix}\n  resolution: \"QLoRA/instruct numbers in 4.1 and Discussion. Full tables in appendix per 8-page limit.\"\n  resolution_round: 32\n\n- id: \"R32-W5\"\n  summary: \"单一解码策略(nucleus only)\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 32\n  last_seen_round: 32\n  mentions:\n    - {round: 32, reviewers: \"R1+R2\", note: \"greedy/top-k 未验证\"}\n  action_items:\n    - {round: 32, action: \"Acknowledged as limitation\", assigned_to: Director, status: wont_fix}\n  resolution: \"Abstract scope qualifier; temperature sensitivity tested.\"\n  resolution_round: 32\n\n- id: \"R32-W6\"\n  summary: \"3-class F1=0.762 因 gen-0 共享而 misleading\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 32\n  last_seen_round: 32\n  mentions:\n    - {round: 32, reviewers: \"R1+R2\", note: \"gen-0 recall 99.4%\"}\n  action_items:\n    - {round: 32, action: \"Binary F1 is primary in Abstract\", assigned_to: Director, status: wont_fix}\n  resolution: \"Abstract uses binary F1 only; 4.1 notes gen-0 inflation.\"\n  resolution_round: 32\n\n- id: \"R32-W7\"\n  summary: \"特征选取缺乏系统性论证\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 32\n  last_seen_round: 32\n  mentions:\n    - {round: 32, reviewers: \"R1+R2\", note: \"R1 major, R2 降级 warning\"}\n  action_items:\n    - {round: 32, action: \"method.tex explains rationale\", assigned_to: Director, status: done}\n  resolution: \"method.tex 3.3 a priori selection + LOFO validation + richer-features tradeoff note.\"\n  resolution_round: 32\n\n- id: \"R34-W1\"\n  summary: \"Base-model-only scope 限制泛化价值 (结构性)\"\n  category: experiment\n  severity: warning\n  status: wont_fix\n  first_raised_round: 34\n  last_seen_round: 35\n  mentions:\n    - {round: 34, reviewers: \"R1+R2\", note: \"instruct model F1=0.338-0.667. 共识: scope limitation 非 fatal flaw\"}\n    - {round: 35, reviewers: \"R1+R2\", note: \"R1-W2+R2-N3: instruct 退化 3.7x, motivation narrative (7-17% publications) 与 base-only scope 存在张力. R1 认为 Major, R2 认为 Critical. 共识: Abstract 应更早限定 scope; Discussion 中 curation 讨论应限定为 base-model 场景\"}\n  action_items:\n    - {round: 34, action: \"Rebuttal: base model 是实验控制; QLoRA instruct recovery\", assigned_to: Director, status: done}\n    - {round: 35, action: \"Abstract 更早限定 scope; Discussion curation 场景限定\", assigned_to: Director, status: pending}\n  resolution: \"结构性限制, 论文已在 Limitations 充分讨论. 但 Round 35 指出 Abstract/Discussion 的 scope 传达仍不够严格.\"\n  resolution_round: null\n\n- id: \"R34-W2\"\n  summary: \"F1=0.694 性能天花板 (结构性)\"\n  category: experiment\n  severity: warning\n  status: wont_fix\n  first_raised_round: 34\n  last_seen_round: 34\n  mentions:\n    - {round: 34, reviewers: \"R1+R2\", note: \"proof-of-concept 定位缓解期望落差, 但限制实际影响力\"}\n  action_items:\n    - {round: 34, action: \"Rebuttal: DDR 贡献是分析框架; LOGO 是最严格下界\", assigned_to: Director, status: done}\n  resolution: \"结构性限制, proof-of-concept 定位已到位.\"\n  resolution_round: 34\n\n- id: \"R34-W3\"\n  summary: \"QLoRA gap (+11.6pp) 未充分解释\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 34\n  last_seen_round: 35\n  mentions:\n    - {round: 34, reviewers: \"R1+R2\", note: \"7 个手工特征丢失大量信号, 未深入分析信号来源\"}\n    - {round: 35, reviewers: \"R1+R2\", note: \"本轮未作为独立 issue 提出, 但 R2 交叉回应中提及 QLoRA instruct 恢复暗示 DDR 以外的信号存在\"}\n  action_items:\n    - {round: 34, action: \"Discussion 补充: token-order dependencies + positional patterns\", assigned_to: Director, status: done}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R34-V1\"\n  summary: \"Pages 1-4 无任何 display item, 纯文字密度过高\"\n  category: format\n  severity: warning\n  status: open\n  first_raised_round: 34\n  last_seen_round: 35\n  mentions:\n    - {round: 34, reviewers: \"R1+R2\", note: \"Critical visual: 前 4 页纯文字\"}\n    - {round: 35, reviewers: \"Visual Check\", note: \"视觉审查确认: 连续 4 页纯文本无 display item; 缺 method overview 图; p.7 display items 过度密集 (2 fig + 1 table)\"}\n  action_items:\n    - {round: 34, action: \"Figure 2 前移至 Introduction 末尾\", assigned_to: Director, status: done}\n    - {round: 35, action: \"仍需改善: 考虑增加 pipeline/overview figure 在 p.2 前; 分散 p.7 的 float 位置\", assigned_to: Director, status: pending}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R34-W4\"\n  summary: \"14B entropy_mean |rho|=0.39 跨过 drifting boundary 未明确报告\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 34\n  last_seen_round: 35\n  mentions:\n    - {round: 34, reviewers: \"Reviewer\", note: \"Discussion 只写 'attenuates by 21-35%', 未明确说 entropy_mean 已跨界\"}\n    - {round: 35, reviewers: \"R1+R2\", note: \"R2-W5: 14B 初步证据放在 Discussion 正文中, 读者可能高估证据等级. R1 AGREE: 建议移至 Appendix\"}\n  action_items:\n    - {round: 34, action: \"Discussion 精确化\", assigned_to: Director, status: done}\n    - {round: 35, action: \"14B 结果移至 Appendix, Discussion 仅用一句话引用\", assigned_to: Director, status: pending}\n  resolution: \"\"\n  resolution_round: null\n\n# === Round 35 新 Issues ===\n\n- id: \"R35-N1\"\n  summary: \"k=2 聚类在 7 个数据点上做 data-driven validation 方法学不足\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 35\n  last_seen_round: 35\n  mentions:\n    - {round: 35, reviewers: \"R1+R2\", note: \"共识: 7 点 k-means 在数学上近 trivial; silhouette=0.632 不具统计意义; 'data-driven' 声称过强. R2 补充: Appendix V 的 holdout generator split validation 比 k-means 更有说服力\"}\n  action_items:\n    - {round: 35, action: \"下调 data-driven 表述; 重心从 k-means silhouette 转向 generator-split consistency; 考虑 per-generator 聚类 (56 点) 或 permutation test\", assigned_to: Director, status: pending}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R35-N2\"\n  summary: \"与 Markovian Chains (Geng et al., 2026) 区分度不足\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 35\n  last_seen_round: 35\n  mentions:\n    - {round: 35, reviewers: \"R1+R2\", note: \"共识: 两者均研究 fixed-parameter inference chains 的 convergence, setup 重叠度高. 当前区分仅一句话. R1 补充: 'attractor dynamics 本质上就是 location drift' 是过度简化, 但需要系统性对比表. 三种方法独立收敛到 ~3 类 depth 反而强化了重叠性\"}\n  action_items:\n    - {round: 35, action: \"增加与 Markovian Chains 和 Broken Telephone 的系统对比表 (chain type / feature space / 分析目标 / generator 规模 / 核心 insight)\", assigned_to: Director, status: pending}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R35-W1\"\n  summary: \"Five 'independent' effect-size metrics 实为高度相关指标的冗余 overclaim\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 35\n  last_seen_round: 35\n  mentions:\n    - {round: 35, reviewers: \"R1+R2\", note: \"共识: Cohen's d ~ Glass's Delta ~ KS 在数学上高度相关; 真正独立的仅 Cliff's delta 和 CV shift. 'five independent' 应改为 'five complementary'\"}\n  action_items:\n    - {round: 35, action: \"将 'five independent' 改为 'five complementary'; 主文中区分 parametric overlap 与 genuinely independent perspectives\", assigned_to: Director, status: pending}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R35-W2\"\n  summary: \"TOST epsilon=0.20 的 justification 存在循环论证\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 35\n  last_seen_round: 35\n  mentions:\n    - {round: 35, reviewers: \"R1+R2\", note: \"R1 指出循环: 先按 d<0.20 分类 -> LOFO 验证贡献小 -> 用 LOFO 结果 justify epsilon. R2 AGREE 但指出 mitigating factor: epsilon=0.20 对应 Cohen (1988) small effect 传统阈值, 非完全 ad hoc. Appendix V partition stability across epsilon 已部分缓解\"}\n  action_items:\n    - {round: 35, action: \"主文承认 epsilon=0.20 是 conventional 而非 task-specific; 将 Appendix V 的 epsilon robustness 结果提升到主文引用\", assigned_to: Director, status: pending}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R35-W3\"\n  summary: \"Downstream null result 未在主文 Discussion 中讨论\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 35\n  last_seen_round: 35\n  mentions:\n    - {round: 35, reviewers: \"R1+R2\", note: \"共识: Appendix M TOST equivalence (depth-aware curation approx random) 直接关系到 Discussion 中 data curation pipeline 应用叙事, 但 Discussion 只字未提. Selective reporting concern. R2 补充: value proposition 应从 'improves training' reframe 为 'data provenance / audit tool'\"}\n  action_items:\n    - {round: 35, action: \"Discussion 加一段: 承认 downstream null result; reframe curation 为 provenance/audit 而非 training quality improvement\", assigned_to: Director, status: pending}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R35-W4\"\n  summary: \"Abstract 中 binary F1=0.694 的定义可能误导读者\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 35\n  last_seen_round: 35\n  mentions:\n    - {round: 35, reviewers: \"R1+R2\", note: \"共识: Abstract 中 'leak-free binary F1=0.694' 未明确 binary 指 gen-1 vs gen-2+ (排除 gen-0), 而非传统的 human vs machine. 建议加 '(gen-1 vs gen-2+, excluding shared gen-0 seeds)'\"}\n  action_items:\n    - {round: 35, action: \"Abstract 中明确 binary F1 的定义\", assigned_to: Director, status: pending}\n  resolution: \"\"\n  resolution_round: null\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "gen-depth-fingerprint",
    "issues_yaml": "\n# === Round 29-34 历史 Issues（保留完整记录）===\n\n- id: \"R29-N1\"\n  summary: \"Base-model-only scope 未在 Abstract 标注\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 29\n  last_seen_round: 32\n  mentions:\n    - {round: 29, reviewers: \"R1+R2\", note: \"共识: Abstract 必须标注 base-model scope\"}\n    - {round: 31, reviewers: \"R1+R2\", note: \"W1: Title/Abstract 仍需 base-model qualifier\"}\n    - {round: 32, reviewers: \"R1+R2\", note: \"升级: 实验设计仅覆盖 base model, 建议扩展或限定 scope\"}\n  action_items:\n    - {round: 29, action: \"Abstract 加 base (pretrained) qualifier\", assigned_to: Agent, status: done}\n    - {round: 32, action: \"Abstract/Conclusion 已有 qualifier; instruct in Discussion\", assigned_to: Director, status: done}\n  resolution: \"Abstract L3 'eight base-model generators'; L7 'restricted to base models'. Title 保持不变(Reviewer 确认). Instruct limitations fully documented.\"\n  resolution_round: 32\n\n- id: \"R29-N2\"\n  summary: \"Downstream TOST underpowered (n=3) + Abstract overclaim\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 29\n  last_seen_round: 34\n  mentions:\n    - {round: 29, reviewers: \"R1+R2\", note: \"n=3 seeds, Abstract 省略 preliminary\"}\n    - {round: 31, reviewers: \"R1+R2\", note: \"W3: TOST n=3 underpowered\"}\n    - {round: 32, reviewers: \"R1+R2\", note: \"升级为 null result: depth-aware curation 不优于 random\"}\n    - {round: 34, reviewers: \"R1+R2\", note: \"RESOLVED: Abstract 完全移除 downstream claim; Appendix M 坦诚呈现 null result\"}\n  action_items:\n    - {round: 29, action: \"Abstract 加 preliminary qualifier\", assigned_to: Agent, status: done}\n    - {round: 32, action: \"Abstract/Conclusion downstream reframing\", assigned_to: Director, status: done}\n  resolution: \"Abstract 完全移除 downstream claim. Appendix M 保留 null result 作为补充材料.\"\n  resolution_round: 34\n\n- id: \"R29-N3\"\n  summary: \"DDR 新颖性 incremental — 缺 concurrent work 系统对比表\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 29\n  last_seen_round: 31\n  mentions:\n    - {round: 29, reviewers: \"R1+R2\", note: \"区分不充分\"}\n    - {round: 31, reviewers: \"R1+R2\", note: \"W12: differentiation insufficient\"}\n  action_items:\n    - {round: 29, action: \"§2.2 加系统对比表\", assigned_to: Agent, status: done}\n  resolution: \"related_work.tex concurrent-comparison table added\"\n  resolution_round: 31\n\n- id: \"R29-N4\"\n  summary: \"QLoRA gap 削弱方法论贡献 — 需重定位\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 29\n  last_seen_round: 34\n  mentions:\n    - {round: 29, reviewers: \"R1+R2\", note: \"7-feat vs QLoRA gap\"}\n    - {round: 31, reviewers: \"R1+R2\", note: \"W4: contribution identity crisis\"}\n    - {round: 32, reviewers: \"R1+R2\", note: \"Contribution 3 仍以 classifier 为卖点\"}\n    - {round: 34, reviewers: \"R1+R2\", note: \"RESOLVED: Contribution 3 = 'Proof-of-concept classifier'; 5处一致传达分析工具定位\"}\n  action_items:\n    - {round: 29, action: \"§1 contribution 重排\", assigned_to: Agent, status: done}\n    - {round: 32, action: \"Proof-of-concept framing\", assigned_to: Director, status: done}\n  resolution: \"Intro L14 'proof of concept'; Contribution 3 'Proof-of-concept classifier with boundary analysis'; results.tex L17+L142; Discussion L11 — 五处一致.\"\n  resolution_round: 34\n\n- id: \"R29-W1\"\n  summary: \"Gemma-2-2B gen-1 F1=0.036 anomaly 解释不充分\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 29\n  last_seen_round: 31\n  mentions:\n    - {round: 29, reviewers: \"R1+R2\", note: \"挑战 DDR universality\"}\n  action_items:\n    - {round: 29, action: \"appendix_9gen_scale 扩展\", assigned_to: Agent, status: done}\n  resolution: \"appendix_9gen_scale expanded\"\n  resolution_round: 31\n\n- id: \"R29-W2\"\n  summary: \"Cross-model chain F1=0.830 可能混淆 depth signal 与 generator identity\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 29\n  last_seen_round: 34\n  mentions:\n    - {round: 29, reviewers: \"R1+R2\", note: \"sample-level CV vs LOGO 矛盾\"}\n    - {round: 31, reviewers: \"R1+R2\", note: \"W11: may be OOD artifact\"}\n    - {round: 32, reviewers: \"R1+R2\", note: \"应标为 upper bound\"}\n    - {round: 34, reviewers: \"R1+R2\", note: \"RESOLVED: footnote 'not directly comparable' + single-gen transfer control\"}\n  action_items:\n    - {round: 29, action: \"results.tex 标注 exploratory\", assigned_to: Agent, status: done}\n    - {round: 32, action: \"caveats added\", assigned_to: Director, status: done}\n  resolution: \"results.tex footnote + L15 single-gen transfer. Caveats sufficient.\"\n  resolution_round: 34\n\n- id: \"R29-W3\"\n  summary: \"温度限制(t<0.9)未在 Abstract 标注\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 29\n  last_seen_round: 32\n  mentions:\n    - {round: 29, reviewers: \"R1+R2\", note: \"cross-temperature transfer 不对称\"}\n  action_items:\n    - {round: 29, action: \"Abstract 加 standard decoding qualifier\", assigned_to: Agent, status: done}\n  resolution: \"Abstract L4 'nucleus sampling (p=0.9, t<=0.7)'\"\n  resolution_round: 31\n\n- id: \"R29-W4\"\n  summary: \"DDR partition 3/1/3 intermediate 定义不够 principled\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 29\n  last_seen_round: 34\n  mentions:\n    - {round: 29, reviewers: \"R1+R2\", note: \"epsilon sensitivity 未展示\"}\n    - {round: 31, reviewers: \"R1+R2\", note: \"W13: threshold arbitrary\"}\n    - {round: 32, reviewers: \"R1\", note: \"升级 Critical: k-means k=2 唯一 clean split\"}\n    - {round: 34, reviewers: \"R1+R2\", note: \"RESOLVED: binary primary partition + k=3 degradation + domain-informed refinement\"}\n  action_items:\n    - {round: 29, action: \"partition stability 分析\", assigned_to: Agent, status: done}\n    - {round: 32, action: \"Restructure 4.2: 2-way primary\", assigned_to: Director, status: done}\n  resolution: \"k=2 binary (sil=0.632); k=3 degradation (0.499); 3/1/3 = domain-informed refinement.\"\n  resolution_round: 34\n\n- id: \"R29-W5\"\n  summary: \"Baseline 范围偏窄 + 比较结构性不公平\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 29\n  last_seen_round: 35\n  mentions:\n    - {round: 29, reviewers: \"R1+R2\", note: \"缺 multi-feature detector\"}\n    - {round: 31, reviewers: \"R1+R2\", note: \"Bonferroni invalidates McNemar\"}\n    - {round: 32, reviewers: \"R1\", note: \"4-det ensemble 实际优于 7-feature\"}\n    - {round: 34, reviewers: \"R1+R2\", note: \"RESOLVED: honest presentation of 4-det+surface 0.708 > ours 0.705\"}\n    - {round: 35, reviewers: \"R1\", note: \"R1 再次质疑 baseline 公平性; R2 部分反驳: classifier 是 proof-of-concept, 应以 3-class 为主比较维度\"}\n  action_items:\n    - {round: 32, action: \"reframed\", assigned_to: Director, status: done}\n  resolution: \"4.3 honestly presents 4-det+surface marginally exceeding. R2 rebuts severity: DDR contribution is decomposition not classification.\"\n  resolution_round: 34\n\n- id: \"R29-W6\"\n  summary: \"Related work 引用缺失 + orphan bib entries\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 29\n  last_seen_round: 35\n  mentions:\n    - {round: 29, reviewers: \"R1+R2\", note: \"RAID 未引用; orphans\"}\n    - {round: 31, reviewers: \"R1+R2\", note: \"17 orphan bib entries\"}\n    - {round: 32, reviewers: \"R1+R2\", note: \"self_refine orphan; 6 new missing refs suggested\"}\n    - {round: 34, reviewers: \"R1+R2\", note: \"Wang et al. (ACL 2025) 仍未添加\"}\n    - {round: 35, reviewers: \"R1+R2\", note: \"本轮引用检查: 66条, 0 orphan, 0 missing. R2确认覆盖良好\"}\n  action_items:\n    - {round: 29, action: \"RAID cite + orphan cleanup\", assigned_to: Agent, status: done}\n    - {round: 32, action: \"self_refine deleted; 6 refs under verification\", assigned_to: Agent, status: done}\n    - {round: 34, action: \"Wang et al. added\", assigned_to: Director, status: done}\n  resolution: \"Round 35 确认: 66条引用, 0 orphan, 0 missing. 引用覆盖良好.\"\n  resolution_round: 35\n\n- id: \"R29-W7\"\n  summary: \"Diagnostic not curative 缺具体场景\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 29\n  last_seen_round: 31\n  mentions:\n    - {round: 29, reviewers: \"R1+R2\", note: \"需要 end-to-end 应用案例\"}\n  action_items:\n    - {round: 29, action: \"Discussion 加 2 个场景\", assigned_to: Agent, status: done}\n  resolution: \"discussion.tex 两个诊断场景\"\n  resolution_round: 31\n\n- id: \"R29-W8\"\n  summary: \"Per-generator F1 变异大 (0.633-0.724)\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 29\n  last_seen_round: 31\n  mentions:\n    - {round: 29, reviewers: \"R1+R2\", note: \"generator-unknown 场景实用性受限\"}\n  action_items:\n    - {round: 29, action: \"Discussion caveat\", assigned_to: Agent, status: done}\n  resolution: \"discussion.tex '9.1pp per-generator spread'\"\n  resolution_round: 31\n\n- id: \"R32-N1\"\n  summary: \"DDR 增量新颖性不清晰 — 可能是 diversity loss / mode-seeking 的重新表述\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 32\n  last_seen_round: 35\n  mentions:\n    - {round: 32, reviewers: \"R2+R1\", note: \"DDR 可能是 diversity loss 重新表述\"}\n    - {round: 34, reviewers: \"R1+R2\", note: \"RESOLVED: 'what converges vs what is preserved' framing\"}\n    - {round: 35, reviewers: \"R2\", note: \"R2-N1: Shape stability 可能是 top-p 采样机制的 trivial 推论; R1 REBUT: 温度消融证明非无条件成立, 有边界条件的经验发现. 分歧保留\"}\n  action_items:\n    - {round: 32, action: \"Discussion expanded: shape stability as novel contribution\", assigned_to: Director, status: done}\n    - {round: 35, action: \"区分 mechanistic explanation (post-hoc) 和 empirical contribution (DDR partition); 讨论 shape stability 在何条件下被打破\", assigned_to: Director, status: pending}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R32-N2\"\n  summary: \"Entropy min 分类存在根本性矛盾 (|rho|=0.40 标为 near-stationary)\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 32\n  last_seen_round: 34\n  mentions:\n    - {round: 32, reviewers: \"R1\", note: \"|rho|=0.40 vs d=0.016 vs delta=0.354 矛盾\"}\n    - {round: 34, reviewers: \"R1+R2\", note: \"RESOLVED: 'boundary feature' label + gen-0/gen-1 transition mechanism + k=2 placement\"}\n  action_items:\n    - {round: 32, action: \"Label as boundary feature\", assigned_to: Director, status: done}\n  resolution: \"results.tex L85 'boundary feature' with full qualification; Figure 2 caption aligned.\"\n  resolution_round: 34\n\n- id: \"R32-N3\"\n  summary: \"Tail_decay near-stationary 归类仅 4/8 generator 通过 TOST (epsilon=0.20)\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 32\n  last_seen_round: 35\n  mentions:\n    - {round: 32, reviewers: \"R1\", note: \"50% pass rate; OLMo d=0.22\"}\n    - {round: 34, reviewers: \"R1+R2\", note: \"RESOLVED: L89-91 three-sentence coverage\"}\n    - {round: 35, reviewers: \"R1+R2\", note: \"R1-N2: 4/8 TOST 通过率不足以支撑 near-stationary; R2 AGREE (但反对 R1 的 3/2/2 方案, 建议 tail_decay 单独降级为 intermediate). 共识: 主文应更诚实处理 tail_decay 的 boundary status\"}\n  action_items:\n    - {round: 32, action: \"Transparent reporting in main text\", assigned_to: Director, status: done}\n    - {round: 35, action: \"将 tail_decay 降级为 intermediate 或提供更强论证; 不应以 neat 二分法遮盖 50% 通过率\", assigned_to: Director, status: pending}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R32-W1\"\n  summary: \"分类性能 F1=0.694 定位为 detecting 但实为 proof-of-concept\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 32\n  last_seen_round: 34\n  mentions:\n    - {round: 32, reviewers: \"R1+R2\", note: \"~30% 错分率\"}\n    - {round: 34, reviewers: \"R1+R2\", note: \"RESOLVED: Discussion L11 'proof-of-concept, not a deployable system'\"}\n  action_items:\n    - {round: 32, action: \"Discussion proof-of-concept framing\", assigned_to: Director, status: done}\n  resolution: \"Intro L14, Contribution 3, Discussion L11 — all say 'proof-of-concept'.\"\n  resolution_round: 34\n\n- id: \"R32-W2\"\n  summary: \"TOST power analysis 缺失\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 32\n  last_seen_round: 34\n  mentions:\n    - {round: 32, reviewers: \"R1\", note: \"大样本 TOST 几乎总检测 equivalence\"}\n    - {round: 34, reviewers: \"R1+R2\", note: \"共识: SESOI+epsilon+caveat 足够, 不阻碍接收\"}\n  action_items:\n    - {round: 32, action: \"TOST power computation\", assigned_to: Agent, status: wont_fix}\n  resolution: \"SESOI justification + epsilon sensitivity + high-N masking acknowledged.\"\n  resolution_round: 34\n\n- id: \"R32-W3\"\n  summary: \"术语混淆: entropy 指代 NLL 不规范\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 32\n  last_seen_round: 35\n  mentions:\n    - {round: 32, reviewers: \"R2\", note: \"NLL 与 Shannon entropy 不同\"}\n    - {round: 35, reviewers: \"R2\", note: \"R2-W2 再次提出; R1 REBUT: 3.3 已有显式声明且符合领域惯例. 共识: presentation issue, 建议将术语说明移至首次使用处\"}\n  action_items:\n    - {round: 32, action: \"Existing clarification sufficient\", assigned_to: Director, status: wont_fix}\n  resolution: \"method.tex 3.3 L38 explicit clarification. Round 35 R1 confirms field convention. Suggestion: move disclaimer to first use.\"\n  resolution_round: 32\n\n- id: \"R32-W4\"\n  summary: \"附录 25 页过大, 关键结果应在主文讨论\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 32\n  last_seen_round: 32\n  mentions:\n    - {round: 32, reviewers: \"R2\", note: \"25 页附录\"}\n  action_items:\n    - {round: 32, action: \"Key numbers already in main text\", assigned_to: Director, status: wont_fix}\n  resolution: \"QLoRA/instruct numbers in 4.1 and Discussion. Full tables in appendix per 8-page limit.\"\n  resolution_round: 32\n\n- id: \"R32-W5\"\n  summary: \"单一解码策略(nucleus only)\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 32\n  last_seen_round: 32\n  mentions:\n    - {round: 32, reviewers: \"R1+R2\", note: \"greedy/top-k 未验证\"}\n  action_items:\n    - {round: 32, action: \"Acknowledged as limitation\", assigned_to: Director, status: wont_fix}\n  resolution: \"Abstract scope qualifier; temperature sensitivity tested.\"\n  resolution_round: 32\n\n- id: \"R32-W6\"\n  summary: \"3-class F1=0.762 因 gen-0 共享而 misleading\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 32\n  last_seen_round: 32\n  mentions:\n    - {round: 32, reviewers: \"R1+R2\", note: \"gen-0 recall 99.4%\"}\n  action_items:\n    - {round: 32, action: \"Binary F1 is primary in Abstract\", assigned_to: Director, status: wont_fix}\n  resolution: \"Abstract uses binary F1 only; 4.1 notes gen-0 inflation.\"\n  resolution_round: 32\n\n- id: \"R32-W7\"\n  summary: \"特征选取缺乏系统性论证\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 32\n  last_seen_round: 32\n  mentions:\n    - {round: 32, reviewers: \"R1+R2\", note: \"R1 major, R2 降级 warning\"}\n  action_items:\n    - {round: 32, action: \"method.tex explains rationale\", assigned_to: Director, status: done}\n  resolution: \"method.tex 3.3 a priori selection + LOFO validation + richer-features tradeoff note.\"\n  resolution_round: 32\n\n- id: \"R34-W1\"\n  summary: \"Base-model-only scope 限制泛化价值 (结构性)\"\n  category: experiment\n  severity: warning\n  status: wont_fix\n  first_raised_round: 34\n  last_seen_round: 35\n  mentions:\n    - {round: 34, reviewers: \"R1+R2\", note: \"instruct model F1=0.338-0.667. 共识: scope limitation 非 fatal flaw\"}\n    - {round: 35, reviewers: \"R1+R2\", note: \"R1-W2+R2-N3: instruct 退化 3.7x, motivation narrative (7-17% publications) 与 base-only scope 存在张力. R1 认为 Major, R2 认为 Critical. 共识: Abstract 应更早限定 scope; Discussion 中 curation 讨论应限定为 base-model 场景\"}\n  action_items:\n    - {round: 34, action: \"Rebuttal: base model 是实验控制; QLoRA instruct recovery\", assigned_to: Director, status: done}\n    - {round: 35, action: \"Abstract 更早限定 scope; Discussion curation 场景限定\", assigned_to: Director, status: pending}\n  resolution: \"结构性限制, 论文已在 Limitations 充分讨论. 但 Round 35 指出 Abstract/Discussion 的 scope 传达仍不够严格.\"\n  resolution_round: null\n\n- id: \"R34-W2\"\n  summary: \"F1=0.694 性能天花板 (结构性)\"\n  category: experiment\n  severity: warning\n  status: wont_fix\n  first_raised_round: 34\n  last_seen_round: 34\n  mentions:\n    - {round: 34, reviewers: \"R1+R2\", note: \"proof-of-concept 定位缓解期望落差, 但限制实际影响力\"}\n  action_items:\n    - {round: 34, action: \"Rebuttal: DDR 贡献是分析框架; LOGO 是最严格下界\", assigned_to: Director, status: done}\n  resolution: \"结构性限制, proof-of-concept 定位已到位.\"\n  resolution_round: 34\n\n- id: \"R34-W3\"\n  summary: \"QLoRA gap (+11.6pp) 未充分解释\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 34\n  last_seen_round: 35\n  mentions:\n    - {round: 34, reviewers: \"R1+R2\", note: \"7 个手工特征丢失大量信号, 未深入分析信号来源\"}\n    - {round: 35, reviewers: \"R1+R2\", note: \"本轮未作为独立 issue 提出, 但 R2 交叉回应中提及 QLoRA instruct 恢复暗示 DDR 以外的信号存在\"}\n  action_items:\n    - {round: 34, action: \"Discussion 补充: token-order dependencies + positional patterns\", assigned_to: Director, status: done}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R34-V1\"\n  summary: \"Pages 1-4 无任何 display item, 纯文字密度过高\"\n  category: format\n  severity: warning\n  status: open\n  first_raised_round: 34\n  last_seen_round: 35\n  mentions:\n    - {round: 34, reviewers: \"R1+R2\", note: \"Critical visual: 前 4 页纯文字\"}\n    - {round: 35, reviewers: \"Visual Check\", note: \"视觉审查确认: 连续 4 页纯文本无 display item; 缺 method overview 图; p.7 display items 过度密集 (2 fig + 1 table)\"}\n  action_items:\n    - {round: 34, action: \"Figure 2 前移至 Introduction 末尾\", assigned_to: Director, status: done}\n    - {round: 35, action: \"仍需改善: 考虑增加 pipeline/overview figure 在 p.2 前; 分散 p.7 的 float 位置\", assigned_to: Director, status: pending}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R34-W4\"\n  summary: \"14B entropy_mean |rho|=0.39 跨过 drifting boundary 未明确报告\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 34\n  last_seen_round: 35\n  mentions:\n    - {round: 34, reviewers: \"Reviewer\", note: \"Discussion 只写 'attenuates by 21-35%', 未明确说 entropy_mean 已跨界\"}\n    - {round: 35, reviewers: \"R1+R2\", note: \"R2-W5: 14B 初步证据放在 Discussion 正文中, 读者可能高估证据等级. R1 AGREE: 建议移至 Appendix\"}\n  action_items:\n    - {round: 34, action: \"Discussion 精确化\", assigned_to: Director, status: done}\n    - {round: 35, action: \"14B 结果移至 Appendix, Discussion 仅用一句话引用\", assigned_to: Director, status: pending}\n  resolution: \"\"\n  resolution_round: null\n\n# === Round 35 新 Issues ===\n\n- id: \"R35-N1\"\n  summary: \"k=2 聚类在 7 个数据点上做 data-driven validation 方法学不足\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 35\n  last_seen_round: 35\n  mentions:\n    - {round: 35, reviewers: \"R1+R2\", note: \"共识: 7 点 k-means 在数学上近 trivial; silhouette=0.632 不具统计意义; 'data-driven' 声称过强. R2 补充: Appendix V 的 holdout generator split validation 比 k-means 更有说服力\"}\n  action_items:\n    - {round: 35, action: \"下调 data-driven 表述; 重心从 k-means silhouette 转向 generator-split consistency; 考虑 per-generator 聚类 (56 点) 或 permutation test\", assigned_to: Director, status: pending}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R35-N2\"\n  summary: \"与 Markovian Chains (Geng et al., 2026) 区分度不足\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 35\n  last_seen_round: 35\n  mentions:\n    - {round: 35, reviewers: \"R1+R2\", note: \"共识: 两者均研究 fixed-parameter inference chains 的 convergence, setup 重叠度高. 当前区分仅一句话. R1 补充: 'attractor dynamics 本质上就是 location drift' 是过度简化, 但需要系统性对比表. 三种方法独立收敛到 ~3 类 depth 反而强化了重叠性\"}\n  action_items:\n    - {round: 35, action: \"增加与 Markovian Chains 和 Broken Telephone 的系统对比表 (chain type / feature space / 分析目标 / generator 规模 / 核心 insight)\", assigned_to: Director, status: pending}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R35-W1\"\n  summary: \"Five 'independent' effect-size metrics 实为高度相关指标的冗余 overclaim\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 35\n  last_seen_round: 35\n  mentions:\n    - {round: 35, reviewers: \"R1+R2\", note: \"共识: Cohen's d ~ Glass's Delta ~ KS 在数学上高度相关; 真正独立的仅 Cliff's delta 和 CV shift. 'five independent' 应改为 'five complementary'\"}\n  action_items:\n    - {round: 35, action: \"将 'five independent' 改为 'five complementary'; 主文中区分 parametric overlap 与 genuinely independent perspectives\", assigned_to: Director, status: pending}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R35-W2\"\n  summary: \"TOST epsilon=0.20 的 justification 存在循环论证\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 35\n  last_seen_round: 35\n  mentions:\n    - {round: 35, reviewers: \"R1+R2\", note: \"R1 指出循环: 先按 d<0.20 分类 -> LOFO 验证贡献小 -> 用 LOFO 结果 justify epsilon. R2 AGREE 但指出 mitigating factor: epsilon=0.20 对应 Cohen (1988) small effect 传统阈值, 非完全 ad hoc. Appendix V partition stability across epsilon 已部分缓解\"}\n  action_items:\n    - {round: 35, action: \"主文承认 epsilon=0.20 是 conventional 而非 task-specific; 将 Appendix V 的 epsilon robustness 结果提升到主文引用\", assigned_to: Director, status: pending}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R35-W3\"\n  summary: \"Downstream null result 未在主文 Discussion 中讨论\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 35\n  last_seen_round: 35\n  mentions:\n    - {round: 35, reviewers: \"R1+R2\", note: \"共识: Appendix M TOST equivalence (depth-aware curation approx random) 直接关系到 Discussion 中 data curation pipeline 应用叙事, 但 Discussion 只字未提. Selective reporting concern. R2 补充: value proposition 应从 'improves training' reframe 为 'data provenance / audit tool'\"}\n  action_items:\n    - {round: 35, action: \"Discussion 加一段: 承认 downstream null result; reframe curation 为 provenance/audit 而非 training quality improvement\", assigned_to: Director, status: pending}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R35-W4\"\n  summary: \"Abstract 中 binary F1=0.694 的定义可能误导读者\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 35\n  last_seen_round: 35\n  mentions:\n    - {round: 35, reviewers: \"R1+R2\", note: \"共识: Abstract 中 'leak-free binary F1=0.694' 未明确 binary 指 gen-1 vs gen-2+ (排除 gen-0), 而非传统的 human vs machine. 建议加 '(gen-1 vs gen-2+, excluding shared gen-0 seeds)'\"}\n  action_items:\n    - {round: 35, action: \"Abstract 中明确 binary F1 的定义\", assigned_to: Director, status: pending}\n  resolution: \"\"\n  resolution_round: null\n"
  }
}
```

</details>

---


### Tool result

_source line 2695 · 2026-05-21T02:50:16.482338+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/review_issues.yaml\", \"bytes\": 21600}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 2696 · 2026-05-21T02:53:00.731891+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "project": "gen-depth-fingerprint",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "3.5 - Borderline Conference",
  "review_chat_id": "oc_999770e4e57bfc6eabd12fc1f64af1ef",
  "report": "\n# 审稿报告：Depth Fingerprinting: Detecting Recursive Generation Depth in LLM Text Chains\n\n**Venue**: EMNLP 2026 (ARR May 2026 cycle)\n**审稿模式**: Fresh (初审)\n**Reviewers**: R1 (方法严谨性 + 实验设计) + R2 (新颖性 + 完整性)\n**交叉审稿**: 完成，双向逐条 [AGREE]/[REBUT]\n\n---\n\n## Summary\n\n本文提出 Depth Fingerprinting，将 AI 文本检测从 binary (human/machine) 扩展到 ordinal depth estimation (gen-0/gen-1/gen-2+)。核心发现是 Differential Depth Response (DDR)：在 8 个 base-model generators（5 个架构家族，0.6B-8B）上，NLL location 特征随 generation depth 单调漂移（Cohen's d=0.76-1.17），而 shape 特征保持近稳态（d<0.10）。基于 DDR 的 7-feature XGBoost 在 LOGO 下达 leak-free binary F1=0.694；QLoRA 端到端达 0.905。论文将 DDR 分解本身（而非分类器性能）定位为主要贡献。\n\n---\n\n## Strengths\n\n**S1. 任务定义新颖且有价值。** 从 binary detection 到 ordinal depth classification 的扩展填补了检测文献中的空白，具有清晰的 data provenance 和 model collapse 分析 motivation。[R1+R2 共识]\n\n**S2. DDR 分解提供机械性解释。** Location drifts while shape is preserved 的发现通过 top-p truncation 给出了机制解释，并通过温度消融和 prompt type 消融提供了两个可检验的预测，均得到验证。[R1]\n\n**S3. 实验控制极其详尽。** Seed-sharing control、length confound control、independent-seed experiment、cross-reference model、cross-temperature、cross-domain、cross-prompt-type、TOST equivalence testing——几乎所有合理的混淆变量均有控制实验。附录 20+ 页系统性消融展示了对潜在质疑的充分预判。[R1+R2 共识]\n\n**S4. 诚实处理 null results 和限制。** Downstream utility 的 TOST equivalence (null result)、instruction-tuned models 下的性能退化、baseline 在某些 metric 上超越——均被坦诚报告。这种学术诚实度在投稿论文中较为少见。[R1+R2 共识]\n\n**S5. 统计方法论自觉。** Cohen's d effect sizes、bootstrap CIs、TOST equivalence tests、Bonferroni correction、LOGO cross-validation 贯穿全文。[R2]\n\n**S6. 写作质量。** 叙事结构清晰，从问题定义到方法到结果到 mechanistic interpretation 的逻辑链连贯，语言精练。主文 8 页信息密度高。[R1+R2 共识]\n\n**S7. 格式合规。** 正文 ≤8 页、ACL template、匿名、Limitations/Ethics 齐全。[R2 验证]\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**N1** [Critical, 共识] **k=2 聚类在 7 个数据点上的 \"data-driven\" 验证方法学不足。**\nDDR 分区是论文核心贡献，但 k-means 聚类对象仅 7 个特征点。对 7 个点做 k=2 聚类在数学上接近 trivial——任何存在基本分离结构的小样本集合都能产生可观的 silhouette。silhouette 从 k=2 (0.632) 到 k=3 (0.499) 到 k=4 (0.571) 的非单调变化在此样本量下不具统计意义。论文 Abstract 和 §4.2 中的 \"data-driven clustering\" 表述给人以由数据驱动发现的印象，实际上更接近对先验直觉的定量确认。R2 补充指出 Appendix V 的 holdout generator split validation 比 k-means 更有说服力，但当前叙事重心未对准。\n→ 建议：(1) 下调 \"data-driven\" 表述；(2) 将验证重心转向 generator-split consistency；(3) 考虑 per-generator 聚类 (7×8=56 点) 或 permutation test。\n\n**N2** [Critical, 共识] **tail_decay 的 near-stationary 分类证据不足（TOST 仅 4/8 通过）。**\ntail_decay 在 ε=0.20 下仅 4/8 generators 通过 TOST，OLMo-2-1B 的 |d|=0.22 超过等价界。论文承认 \"genuine boundary case\" 但主文仍将其归入 near-stationary 组以维持整齐的二分法叙事（3 drifting + 1 intermediate + 3 near-stationary）。Sensitivity analysis 显示 tail_decay 在 ε=0.25 时才达 7/8 通过率，说明其 near-stationarity 对阈值敏感。R2 建议将 tail_decay 单独降级为 intermediate（3/2/1+1 格局），而非 R1 建议的 3/2/2。\n→ 建议：主文更诚实处理 tail_decay 的 boundary status；不应以 neat 二分法遮盖 50% 通过率。\n\n**N3** [Critical, 共识] **与 Markovian Chains (Geng et al., 2026) 的区分度不足。**\nMarkovian Chains 同样研究 fixed-parameter inference chains 下的 convergence dynamics，核心 setup 重叠度高。当前 §2.2 仅用一句话区分。三种独立方法（Markovian dynamics、information-theoretic loss、DDR feature compression）收敛到 ~3 个可区分深度类——这反而强化了重叠性的质疑。R1 补充：\"attractor dynamics = location drift\" 是过度简化，但需要量化对比。\n→ 建议：增加系统性对比表（chain type / feature space / 分析目标 / generator 规模 / 核心 insight）。\n\n### Should-Fix（影响评分但不一票否决）\n\n**W1** [Major, 共识] **Base-model-only scope 与 motivation narrative 存在张力。**\nIntroduction 引用 \"7-17% of scientific publications contain LLM-modified content\" 作为 motivation，但这些文本几乎全部来自 instruction-tuned models。Appendix K 显示 instruct models 下 DDR 退化 3.7×（OLMo-Instruct 3-class F1=0.575 vs base 0.754），DDR silhouette 从 0.632 降至 0.338，feature correlations 甚至反转。QLoRA 在 instruct 上恢复到 0.89-0.91，说明 token-level depth signal 存在但 DDR 的 7-feature 分解无法捕获——这本身质疑了 DDR 作为通用 explanatory framework 的地位。R1 评为 Major，R2 评为 Critical。\n→ 建议：Abstract 更早限定 scope；Discussion curation 场景限定为 base-model pipeline。\n\n**W2** [Major, 共识] **Five \"independent\" effect-size metrics 存在 overclaim。**\nCohen's d 和 Glass's Δ 仅在方差处理上不同，KS statistic 也主要捕获 location shift。真正提供独立信息的仅有 Cliff's δ (rank-based) 和 CV shift (relative variability)。\"Five independent effect-size metrics\" 的表述属于 overclaim。\n→ 建议：改为 \"five complementary effect-size measures\"；区分 parametric overlap 与 genuinely independent perspectives。\n\n**W3** [Major, 共识] **TOST ε=0.20 的 justification 存在循环论证。**\n特征先按 d<0.20 分类为 near-stationary → LOFO 验证贡献小 → LOFO 结果 justify ε=0.20。R2 指出 mitigating factor：ε=0.20 对应 Cohen (1988) 的 small effect 传统阈值，非完全 ad hoc。Appendix V 的 partition stability across ε 已部分缓解。\n→ 建议：主文承认 ε=0.20 是 conventional 选择；将 Appendix V 的 robustness check 提升到主文引用。\n\n**W4** [Major, 共识] **Downstream null result 未在主文 Discussion 中讨论。**\nAppendix M 的 TOST equivalence (depth-aware curation ≈ random subsampling) 直接关系到 §5 中 data curation pipeline 应用叙事，但 Discussion 只字未提。这构成 selective reporting concern。\n→ 建议：Discussion 加一段承认 null result；reframe value proposition 从 \"improves training\" 转向 \"data provenance / audit tool\"。\n\n**W5** [Divergent: R2 Critical / R1 Rebut] **Shape stability 可能是固定采样机制的 trivial 推论。**\nR2 指出 §5 自己承认 top-p truncation preserves functional form，因此 shape stability 不是 emergent property 而是采样机制的直接推论。R1 反驳：(1) 机制可解释 ≠ 经验上 trivial；(2) 温度消融表明 shape stability 在 τ≥0.9 时开始被打破，证明其有边界条件而非无条件成立；(3) 论文提供了两个可检验预测并得到验证。R1 建议区分 mechanistic explanation (post-hoc) 和 empirical contribution (DDR partition)。\n→ **分歧保留，记入报告。** 如修改时能明确 shape stability 的成立条件和边界，将大幅缓解此 concern。\n\n### Minor\n\n**M1** [Info, 共识] Abstract 中 \"leak-free binary F1=0.694\" 未明确 binary 指 gen-1 vs gen-2+（排除 gen-0），而非传统的 human vs machine。建议加 \"(gen-1 vs gen-2+, excluding shared gen-0 seeds)\"。\n\n**M2** [Info, R1+R2 agree] 14B preliminary evidence 放在 Discussion 正文中，读者可能高估证据等级。建议移至 Appendix。\n\n**M3** [Info, R1] Bootstrap CI 仅反映采样变异性，不反映 generator selection uncertainty（per-generator F1 span 9.1pp）。建议区分 sampling CI 和 generalization variability。\n\n**M4** [Info, R1] Chain depth=4 的选择未在主文中 justify。\n\n**M5** [Info, R2] 5 条 bib entries 存在 first_author mismatch（LaTeX 编码 vs API 索引差异），camera-ready 前应检查。\n\n---\n\n## Reviewer Consensus\n\n以下问题两位 Reviewer 达成共识 [AGREE]：\n\n1. **k=2 聚类 \"data-driven\" overclaim** — 7 点 k-means 不构成 principled validation（N1）\n2. **tail_decay near-stationary 证据不足** — 4/8 TOST 通过率不支撑分类（N2）\n3. **Markovian Chains 区分不足** — 需系统性对比表（N3）\n4. **Base-model scope 与 motivation 张力** — instruct 退化严重，Abstract 应更早限定（W1）\n5. **Five \"independent\" metrics overclaim** — 改为 \"complementary\"（W2）\n6. **TOST ε 循环论证** — 有 external justification 但需承认（W3）\n7. **Downstream null result 未在主文讨论** — selective reporting concern（W4）\n8. **Binary F1 定义模糊** — Abstract 应明确（M1）\n\n---\n\n## Reviewer Divergence\n\n| 问题 | R1 | R2 | 评估 |\n|------|----|----|------|\n| Shape stability trivial (W5) | REBUT: 有边界条件的经验发现，非 trivial | Critical: top-p 直接推论 | R1 反驳有力（温度消融证据），但 R2 核心论点仍成立——需更明确区分机制解释与经验贡献 |\n| Instruct failure severity (W1) | Major: scope 已限定 | Critical: motivation 张力 | 介于两者之间，定为 Major-to-Critical |\n| Baseline fairness (R1-W3) | Major: 被超越应更诚实 | Partial rebut: classifier 是 proof-of-concept | R2 反驳有效——DDR 贡献是分解非分类，不降低此 issue severity 但需注意 |\n| Entropy terminology (R2-W2) | Rebut: 领域惯例 | Major: 不够精确 | R1 反驳有效——已有显式声明且符合惯例，降为 Minor presentation issue |\n\n---\n\n## Questions（需作者在 rebuttal 中回答）\n\n1. **[高优先级]** 如果将 tail_decay 重新分类为 intermediate，对分类性能和 DDR 核心叙事有何具体影响？能否提供替代分区下的 ablation 结果？\n2. **[高优先级]** DDR 的 location drift 与 Markovian Chains 的 attractor convergence 在定量层面是否等价？DDR 是否可被视为 attractor dynamics 的 NLL 特征空间投影？\n3. **[高优先级]** QLoRA 在 instruct data 上恢复到 F1=0.89-0.91，但 DDR 7-feature 方法严重退化。QLoRA 在 instruct 上学到的是 DDR features 还是 confound features？这对 DDR 框架的 generality 有何影响？\n4. **[中优先级]** 是否测试过不同 top-p 值（如 p=0.5, 0.7, 0.95）下的 shape stability？如果 shape 在 top-p 变化时被打破，支持 \"trivial 推论\" 解释；反之则支持其作为 non-trivial 发现。\n5. **[中优先级]** Downstream null result (Appendix M) 下，depth fingerprinting 的主要应用场景是什么？是否存在现实 pipeline 使用 base model 生成大量文本？\n6. **[低优先级]** Gemma-2-2B 的 gen-1 F1=0.036 暗示 DDR 在某些架构上不成立——具体失败模式是什么？\n\n---\n\n## Missing References\n\n两位 Reviewer 均未发现重大遗漏。引用覆盖良好：66 条引用，0 orphan，0 missing。concurrent work (Broken Telephone, Markovian Chains, attractor_cycles) 均已引用。\n\nR2 建议考虑但不要求引用：\n- \"Variation is the Key: A Variation-Based Framework for LLM-Generated Text Detection\" (arXiv:2602.13226, 2026) — 概念联系但研究目标不同\n\nR1 建议加强讨论（非缺失引用）：\n- Sadasivan et al. (2024) adversarial robustness findings 对 DDR 的潜在影响\n- Kirchenbauer et al. (2023) watermarking 与 depth detection 的关系\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n未请求。\n\n---\n\n## Visual Layout Check（非评分项）\n\n**状态**: done (4 warning, 7 info)\n\n**Warnings:**\n1. **Pages 1-4 连续 4 页纯文本无 display item** — 审稿人前 2 分钟只看到密集文字，无法建立视觉锚点。建议在 p.2 前插入概念图/pipeline 图或将核心图前移。\n2. **缺少方法概览图 (overview/pipeline figure)** — 作为实证论文，期望在 Method 开始前看到 generation chain → feature extraction → classification 流程的概念图。\n3. **Page 7 display items 过度密集** — 2 figures + 1 table 挤在同一页，而相邻 p.4 和 p.8 全是纯文本。建议分散 float 位置。\n4. **Pages 8-9 连续纯文本** — Discussion + Conclusion + Limitations + Ethics 连续 2 页无 display item。\n\n**Info:**\n- Figure 1 的 8+ 条彩色线在小尺寸下区分度不足\n- Figure 2/3 点标记和轴标签字号偏小\n- Table 1 CI 列与 F1 列视觉拥挤\n- Appendix 中 Figure 4 hapax_ratio y 轴可裁剪\n- Figure 8/9 颜色体系不一致\n- 正文 8 页仅 5 个 display items（3 fig + 2 table），对实证论文偏少\n\n---\n\n## Overall Assessment\n\n**Overall**: **3.5 (Borderline Conference)**\n\n**Soundness**: 3.5/5 — DDR 核心发现有多重证据支撑且实验控制详尽，但 k=2 聚类验证方法学存在缺陷（N1），tail_decay 部分通过率不足（N2），五个 effect-size metrics 冗余度高于声称的 convergent validation（W2）。\n\n**Excitement**: 3.0/5 — 从 binary detection 到 ordinal depth estimation 的延伸有新颖性，DDR 分解提供了有用的实证框架，但与 Markovian Chains 重叠显著（N3），shape stability 的理论新颖性存疑（W5 divergent），实际应用受限于 base-model-only 约束（W1）。\n\n**Reproducibility**: 4.0/5 — 实验设置详尽，超参明确，Bootstrap CI 贯穿全文。\n\n**Confidence**: 4/5 — 两位 Reviewer 均仔细阅读了全部 33 页（含 20 页附录），交叉验证了引用。\n\n**判断依据**：\n- **支持接收的因素**：任务定义新颖（ordinal depth classification 是合理且有价值的研究方向）；实验控制在 empirical study 中属于顶级水平；DDR 分解对后续研究有组织价值；写作诚实且统计方法论自觉。\n- **阻碍接收的因素**：核心分区验证（7 点 k-means）方法学薄弱；tail_decay 的 near-stationary 分类仅半数 generators 支撑；与 Markovian Chains 的增量性需更强论证；base-model-only scope 严重限制实际影响力；downstream utility 为 null result。\n- **总结**：分析框架新颖且 insight 有价值，但验证方法存在可质疑之处，practical impact 受限于 base-model-only 约束。作为 analytical contribution 足以进入 Findings；若能补强 N1（分区验证）、N2（tail_decay 分类）和 N3（concurrent work 区分），有望达到 Conference 水平。\n\n---\n\n## Detailed Comments\n\n### §1 Introduction\n- 第 1 句 \"LLM outputs re-enter generation pipelines\" 暗示了比 base-model-only 更广的适用性——应更早限定 scope。\n- Contribution list 清晰，proof-of-concept 定位到位。但 \"data-driven clustering (k=2, silhouette=0.632)\" 的表述在 Contribution 1 中需降调。\n\n### §2 Related Work\n- Detection 文献覆盖全面。Model collapse 区分到位。\n- 与 Markovian Chains 的区分仅一句话（\"We study inference chains...\"），需要系统性对比表（N3）。\n- §2.2 最后一段关于三种方法收敛到 ~3 classes 的讨论是好的学术 contextualization，但应更明确说明 DDR 的独特增量。\n\n### §3 Method\n- Task formulation (§3.1) 和 generation chain construction (§3.2) 清晰完整。\n- Feature extraction (§3.3) 的 a priori design rationale 合理（dual-view: reference-model + surface）。\n- \"entropy\" 用作 NLL shorthand 已有显式声明且符合领域惯例（R1 反驳有效），但建议将声明移至首次使用处。\n- Evaluation protocol (§3.4) 详尽：LOGO + LOFO + binary leak-free metric + length confound control。\n\n### §4 Results\n- §4.1 诚实呈现了 gen-0 seed sharing 导致的 3-class F1 inflation，采用 leak-free binary F1 作为 primary metric——good practice。\n- §4.2 DDR 分解是论文核心。k=2 聚类验证需补强（N1）；tail_decay 处理需更诚实（N2）；\"five independent\" 应降调（W2）。\n- TOST validation 段落中大样本 power masking 的坦诚承认值得肯定，但 ε=0.20 需 external justification（W3）。\n- §4.3 Baseline 比较：4-det+surface 超越 7-feature 时的处理尚可接受（DDR 贡献是分解非分类），但可更诚实。\n\n### §5 Discussion\n- Mechanistic interpretation（top-p preserves shape）+ 两个可检验预测是亮点。\n- 但需更明确区分 post-hoc rationalization 和 empirical contribution（W5）。\n- Data curation pipeline 讨论需提及 downstream null result（W4）。\n- 14B preliminary evidence 建议移至 Appendix（M2）。\n- Instruct failure 的 mechanistic explanation 不足——是 RLHF reward shaping？SFT format constraints？还是 length regulation？\n\n### §6 Conclusion\n简洁到位，与 Abstract 一致。\n\n### Limitations\n覆盖全面：base-model scope、scale、prompt-type、temperature、English-only、reference model dependency。是本文最强的章节之一。\n\n### 附录\n详尽且组织合理。特别值得注意的优质内容：\n- Appendix V (DDR Partition Validation) 的 generator-split consistency 比 k-means 更有说服力——应在主文中更显著引用\n- Appendix Z.5 (Token-Level NLL Distribution) 的 kernel density plot 信息密度最高——可考虑将代表性示例提升到主文\n- Appendix M (Downstream Utility) 的 null result 必须在主文中讨论\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "project": "gen-depth-fingerprint",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "3.5 - Borderline Conference",
    "review_chat_id": "oc_999770e4e57bfc6eabd12fc1f64af1ef",
    "report": "\n# 审稿报告：Depth Fingerprinting: Detecting Recursive Generation Depth in LLM Text Chains\n\n**Venue**: EMNLP 2026 (ARR May 2026 cycle)\n**审稿模式**: Fresh (初审)\n**Reviewers**: R1 (方法严谨性 + 实验设计) + R2 (新颖性 + 完整性)\n**交叉审稿**: 完成，双向逐条 [AGREE]/[REBUT]\n\n---\n\n## Summary\n\n本文提出 Depth Fingerprinting，将 AI 文本检测从 binary (human/machine) 扩展到 ordinal depth estimation (gen-0/gen-1/gen-2+)。核心发现是 Differential Depth Response (DDR)：在 8 个 base-model generators（5 个架构家族，0.6B-8B）上，NLL location 特征随 generation depth 单调漂移（Cohen's d=0.76-1.17），而 shape 特征保持近稳态（d<0.10）。基于 DDR 的 7-feature XGBoost 在 LOGO 下达 leak-free binary F1=0.694；QLoRA 端到端达 0.905。论文将 DDR 分解本身（而非分类器性能）定位为主要贡献。\n\n---\n\n## Strengths\n\n**S1. 任务定义新颖且有价值。** 从 binary detection 到 ordinal depth classification 的扩展填补了检测文献中的空白，具有清晰的 data provenance 和 model collapse 分析 motivation。[R1+R2 共识]\n\n**S2. DDR 分解提供机械性解释。** Location drifts while shape is preserved 的发现通过 top-p truncation 给出了机制解释，并通过温度消融和 prompt type 消融提供了两个可检验的预测，均得到验证。[R1]\n\n**S3. 实验控制极其详尽。** Seed-sharing control、length confound control、independent-seed experiment、cross-reference model、cross-temperature、cross-domain、cross-prompt-type、TOST equivalence testing——几乎所有合理的混淆变量均有控制实验。附录 20+ 页系统性消融展示了对潜在质疑的充分预判。[R1+R2 共识]\n\n**S4. 诚实处理 null results 和限制。** Downstream utility 的 TOST equivalence (null result)、instruction-tuned models 下的性能退化、baseline 在某些 metric 上超越——均被坦诚报告。这种学术诚实度在投稿论文中较为少见。[R1+R2 共识]\n\n**S5. 统计方法论自觉。** Cohen's d effect sizes、bootstrap CIs、TOST equivalence tests、Bonferroni correction、LOGO cross-validation 贯穿全文。[R2]\n\n**S6. 写作质量。** 叙事结构清晰，从问题定义到方法到结果到 mechanistic interpretation 的逻辑链连贯，语言精练。主文 8 页信息密度高。[R1+R2 共识]\n\n**S7. 格式合规。** 正文 ≤8 页、ACL template、匿名、Limitations/Ethics 齐全。[R2 验证]\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**N1** [Critical, 共识] **k=2 聚类在 7 个数据点上的 \"data-driven\" 验证方法学不足。**\nDDR 分区是论文核心贡献，但 k-means 聚类对象仅 7 个特征点。对 7 个点做 k=2 聚类在数学上接近 trivial——任何存在基本分离结构的小样本集合都能产生可观的 silhouette。silhouette 从 k=2 (0.632) 到 k=3 (0.499) 到 k=4 (0.571) 的非单调变化在此样本量下不具统计意义。论文 Abstract 和 §4.2 中的 \"data-driven clustering\" 表述给人以由数据驱动发现的印象，实际上更接近对先验直觉的定量确认。R2 补充指出 Appendix V 的 holdout generator split validation 比 k-means 更有说服力，但当前叙事重心未对准。\n→ 建议：(1) 下调 \"data-driven\" 表述；(2) 将验证重心转向 generator-split consistency；(3) 考虑 per-generator 聚类 (7×8=56 点) 或 permutation test。\n\n**N2** [Critical, 共识] **tail_decay 的 near-stationary 分类证据不足（TOST 仅 4/8 通过）。**\ntail_decay 在 ε=0.20 下仅 4/8 generators 通过 TOST，OLMo-2-1B 的 |d|=0.22 超过等价界。论文承认 \"genuine boundary case\" 但主文仍将其归入 near-stationary 组以维持整齐的二分法叙事（3 drifting + 1 intermediate + 3 near-stationary）。Sensitivity analysis 显示 tail_decay 在 ε=0.25 时才达 7/8 通过率，说明其 near-stationarity 对阈值敏感。R2 建议将 tail_decay 单独降级为 intermediate（3/2/1+1 格局），而非 R1 建议的 3/2/2。\n→ 建议：主文更诚实处理 tail_decay 的 boundary status；不应以 neat 二分法遮盖 50% 通过率。\n\n**N3** [Critical, 共识] **与 Markovian Chains (Geng et al., 2026) 的区分度不足。**\nMarkovian Chains 同样研究 fixed-parameter inference chains 下的 convergence dynamics，核心 setup 重叠度高。当前 §2.2 仅用一句话区分。三种独立方法（Markovian dynamics、information-theoretic loss、DDR feature compression）收敛到 ~3 个可区分深度类——这反而强化了重叠性的质疑。R1 补充：\"attractor dynamics = location drift\" 是过度简化，但需要量化对比。\n→ 建议：增加系统性对比表（chain type / feature space / 分析目标 / generator 规模 / 核心 insight）。\n\n### Should-Fix（影响评分但不一票否决）\n\n**W1** [Major, 共识] **Base-model-only scope 与 motivation narrative 存在张力。**\nIntroduction 引用 \"7-17% of scientific publications contain LLM-modified content\" 作为 motivation，但这些文本几乎全部来自 instruction-tuned models。Appendix K 显示 instruct models 下 DDR 退化 3.7×（OLMo-Instruct 3-class F1=0.575 vs base 0.754），DDR silhouette 从 0.632 降至 0.338，feature correlations 甚至反转。QLoRA 在 instruct 上恢复到 0.89-0.91，说明 token-level depth signal 存在但 DDR 的 7-feature 分解无法捕获——这本身质疑了 DDR 作为通用 explanatory framework 的地位。R1 评为 Major，R2 评为 Critical。\n→ 建议：Abstract 更早限定 scope；Discussion curation 场景限定为 base-model pipeline。\n\n**W2** [Major, 共识] **Five \"independent\" effect-size metrics 存在 overclaim。**\nCohen's d 和 Glass's Δ 仅在方差处理上不同，KS statistic 也主要捕获 location shift。真正提供独立信息的仅有 Cliff's δ (rank-based) 和 CV shift (relative variability)。\"Five independent effect-size metrics\" 的表述属于 overclaim。\n→ 建议：改为 \"five complementary effect-size measures\"；区分 parametric overlap 与 genuinely independent perspectives。\n\n**W3** [Major, 共识] **TOST ε=0.20 的 justification 存在循环论证。**\n特征先按 d<0.20 分类为 near-stationary → LOFO 验证贡献小 → LOFO 结果 justify ε=0.20。R2 指出 mitigating factor：ε=0.20 对应 Cohen (1988) 的 small effect 传统阈值，非完全 ad hoc。Appendix V 的 partition stability across ε 已部分缓解。\n→ 建议：主文承认 ε=0.20 是 conventional 选择；将 Appendix V 的 robustness check 提升到主文引用。\n\n**W4** [Major, 共识] **Downstream null result 未在主文 Discussion 中讨论。**\nAppendix M 的 TOST equivalence (depth-aware curation ≈ random subsampling) 直接关系到 §5 中 data curation pipeline 应用叙事，但 Discussion 只字未提。这构成 selective reporting concern。\n→ 建议：Discussion 加一段承认 null result；reframe value proposition 从 \"improves training\" 转向 \"data provenance / audit tool\"。\n\n**W5** [Divergent: R2 Critical / R1 Rebut] **Shape stability 可能是固定采样机制的 trivial 推论。**\nR2 指出 §5 自己承认 top-p truncation preserves functional form，因此 shape stability 不是 emergent property 而是采样机制的直接推论。R1 反驳：(1) 机制可解释 ≠ 经验上 trivial；(2) 温度消融表明 shape stability 在 τ≥0.9 时开始被打破，证明其有边界条件而非无条件成立；(3) 论文提供了两个可检验预测并得到验证。R1 建议区分 mechanistic explanation (post-hoc) 和 empirical contribution (DDR partition)。\n→ **分歧保留，记入报告。** 如修改时能明确 shape stability 的成立条件和边界，将大幅缓解此 concern。\n\n### Minor\n\n**M1** [Info, 共识] Abstract 中 \"leak-free binary F1=0.694\" 未明确 binary 指 gen-1 vs gen-2+（排除 gen-0），而非传统的 human vs machine。建议加 \"(gen-1 vs gen-2+, excluding shared gen-0 seeds)\"。\n\n**M2** [Info, R1+R2 agree] 14B preliminary evidence 放在 Discussion 正文中，读者可能高估证据等级。建议移至 Appendix。\n\n**M3** [Info, R1] Bootstrap CI 仅反映采样变异性，不反映 generator selection uncertainty（per-generator F1 span 9.1pp）。建议区分 sampling CI 和 generalization variability。\n\n**M4** [Info, R1] Chain depth=4 的选择未在主文中 justify。\n\n**M5** [Info, R2] 5 条 bib entries 存在 first_author mismatch（LaTeX 编码 vs API 索引差异），camera-ready 前应检查。\n\n---\n\n## Reviewer Consensus\n\n以下问题两位 Reviewer 达成共识 [AGREE]：\n\n1. **k=2 聚类 \"data-driven\" overclaim** — 7 点 k-means 不构成 principled validation（N1）\n2. **tail_decay near-stationary 证据不足** — 4/8 TOST 通过率不支撑分类（N2）\n3. **Markovian Chains 区分不足** — 需系统性对比表（N3）\n4. **Base-model scope 与 motivation 张力** — instruct 退化严重，Abstract 应更早限定（W1）\n5. **Five \"independent\" metrics overclaim** — 改为 \"complementary\"（W2）\n6. **TOST ε 循环论证** — 有 external justification 但需承认（W3）\n7. **Downstream null result 未在主文讨论** — selective reporting concern（W4）\n8. **Binary F1 定义模糊** — Abstract 应明确（M1）\n\n---\n\n## Reviewer Divergence\n\n| 问题 | R1 | R2 | 评估 |\n|------|----|----|------|\n| Shape stability trivial (W5) | REBUT: 有边界条件的经验发现，非 trivial | Critical: top-p 直接推论 | R1 反驳有力（温度消融证据），但 R2 核心论点仍成立——需更明确区分机制解释与经验贡献 |\n| Instruct failure severity (W1) | Major: scope 已限定 | Critical: motivation 张力 | 介于两者之间，定为 Major-to-Critical |\n| Baseline fairness (R1-W3) | Major: 被超越应更诚实 | Partial rebut: classifier 是 proof-of-concept | R2 反驳有效——DDR 贡献是分解非分类，不降低此 issue severity 但需注意 |\n| Entropy terminology (R2-W2) | Rebut: 领域惯例 | Major: 不够精确 | R1 反驳有效——已有显式声明且符合惯例，降为 Minor presentation issue |\n\n---\n\n## Questions（需作者在 rebuttal 中回答）\n\n1. **[高优先级]** 如果将 tail_decay 重新分类为 intermediate，对分类性能和 DDR 核心叙事有何具体影响？能否提供替代分区下的 ablation 结果？\n2. **[高优先级]** DDR 的 location drift 与 Markovian Chains 的 attractor convergence 在定量层面是否等价？DDR 是否可被视为 attractor dynamics 的 NLL 特征空间投影？\n3. **[高优先级]** QLoRA 在 instruct data 上恢复到 F1=0.89-0.91，但 DDR 7-feature 方法严重退化。QLoRA 在 instruct 上学到的是 DDR features 还是 confound features？这对 DDR 框架的 generality 有何影响？\n4. **[中优先级]** 是否测试过不同 top-p 值（如 p=0.5, 0.7, 0.95）下的 shape stability？如果 shape 在 top-p 变化时被打破，支持 \"trivial 推论\" 解释；反之则支持其作为 non-trivial 发现。\n5. **[中优先级]** Downstream null result (Appendix M) 下，depth fingerprinting 的主要应用场景是什么？是否存在现实 pipeline 使用 base model 生成大量文本？\n6. **[低优先级]** Gemma-2-2B 的 gen-1 F1=0.036 暗示 DDR 在某些架构上不成立——具体失败模式是什么？\n\n---\n\n## Missing References\n\n两位 Reviewer 均未发现重大遗漏。引用覆盖良好：66 条引用，0 orphan，0 missing。concurrent work (Broken Telephone, Markovian Chains, attractor_cycles) 均已引用。\n\nR2 建议考虑但不要求引用：\n- \"Variation is the Key: A Variation-Based Framework for LLM-Generated Text Detection\" (arXiv:2602.13226, 2026) — 概念联系但研究目标不同\n\nR1 建议加强讨论（非缺失引用）：\n- Sadasivan et al. (2024) adversarial robustness findings 对 DDR 的潜在影响\n- Kirchenbauer et al. (2023) watermarking 与 depth detection 的关系\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n未请求。\n\n---\n\n## Visual Layout Check（非评分项）\n\n**状态**: done (4 warning, 7 info)\n\n**Warnings:**\n1. **Pages 1-4 连续 4 页纯文本无 display item** — 审稿人前 2 分钟只看到密集文字，无法建立视觉锚点。建议在 p.2 前插入概念图/pipeline 图或将核心图前移。\n2. **缺少方法概览图 (overview/pipeline figure)** — 作为实证论文，期望在 Method 开始前看到 generation chain → feature extraction → classification 流程的概念图。\n3. **Page 7 display items 过度密集** — 2 figures + 1 table 挤在同一页，而相邻 p.4 和 p.8 全是纯文本。建议分散 float 位置。\n4. **Pages 8-9 连续纯文本** — Discussion + Conclusion + Limitations + Ethics 连续 2 页无 display item。\n\n**Info:**\n- Figure 1 的 8+ 条彩色线在小尺寸下区分度不足\n- Figure 2/3 点标记和轴标签字号偏小\n- Table 1 CI 列与 F1 列视觉拥挤\n- Appendix 中 Figure 4 hapax_ratio y 轴可裁剪\n- Figure 8/9 颜色体系不一致\n- 正文 8 页仅 5 个 display items（3 fig + 2 table），对实证论文偏少\n\n---\n\n## Overall Assessment\n\n**Overall**: **3.5 (Borderline Conference)**\n\n**Soundness**: 3.5/5 — DDR 核心发现有多重证据支撑且实验控制详尽，但 k=2 聚类验证方法学存在缺陷（N1），tail_decay 部分通过率不足（N2），五个 effect-size metrics 冗余度高于声称的 convergent validation（W2）。\n\n**Excitement**: 3.0/5 — 从 binary detection 到 ordinal depth estimation 的延伸有新颖性，DDR 分解提供了有用的实证框架，但与 Markovian Chains 重叠显著（N3），shape stability 的理论新颖性存疑（W5 divergent），实际应用受限于 base-model-only 约束（W1）。\n\n**Reproducibility**: 4.0/5 — 实验设置详尽，超参明确，Bootstrap CI 贯穿全文。\n\n**Confidence**: 4/5 — 两位 Reviewer 均仔细阅读了全部 33 页（含 20 页附录），交叉验证了引用。\n\n**判断依据**：\n- **支持接收的因素**：任务定义新颖（ordinal depth classification 是合理且有价值的研究方向）；实验控制在 empirical study 中属于顶级水平；DDR 分解对后续研究有组织价值；写作诚实且统计方法论自觉。\n- **阻碍接收的因素**：核心分区验证（7 点 k-means）方法学薄弱；tail_decay 的 near-stationary 分类仅半数 generators 支撑；与 Markovian Chains 的增量性需更强论证；base-model-only scope 严重限制实际影响力；downstream utility 为 null result。\n- **总结**：分析框架新颖且 insight 有价值，但验证方法存在可质疑之处，practical impact 受限于 base-model-only 约束。作为 analytical contribution 足以进入 Findings；若能补强 N1（分区验证）、N2（tail_decay 分类）和 N3（concurrent work 区分），有望达到 Conference 水平。\n\n---\n\n## Detailed Comments\n\n### §1 Introduction\n- 第 1 句 \"LLM outputs re-enter generation pipelines\" 暗示了比 base-model-only 更广的适用性——应更早限定 scope。\n- Contribution list 清晰，proof-of-concept 定位到位。但 \"data-driven clustering (k=2, silhouette=0.632)\" 的表述在 Contribution 1 中需降调。\n\n### §2 Related Work\n- Detection 文献覆盖全面。Model collapse 区分到位。\n- 与 Markovian Chains 的区分仅一句话（\"We study inference chains...\"），需要系统性对比表（N3）。\n- §2.2 最后一段关于三种方法收敛到 ~3 classes 的讨论是好的学术 contextualization，但应更明确说明 DDR 的独特增量。\n\n### §3 Method\n- Task formulation (§3.1) 和 generation chain construction (§3.2) 清晰完整。\n- Feature extraction (§3.3) 的 a priori design rationale 合理（dual-view: reference-model + surface）。\n- \"entropy\" 用作 NLL shorthand 已有显式声明且符合领域惯例（R1 反驳有效），但建议将声明移至首次使用处。\n- Evaluation protocol (§3.4) 详尽：LOGO + LOFO + binary leak-free metric + length confound control。\n\n### §4 Results\n- §4.1 诚实呈现了 gen-0 seed sharing 导致的 3-class F1 inflation，采用 leak-free binary F1 作为 primary metric——good practice。\n- §4.2 DDR 分解是论文核心。k=2 聚类验证需补强（N1）；tail_decay 处理需更诚实（N2）；\"five independent\" 应降调（W2）。\n- TOST validation 段落中大样本 power masking 的坦诚承认值得肯定，但 ε=0.20 需 external justification（W3）。\n- §4.3 Baseline 比较：4-det+surface 超越 7-feature 时的处理尚可接受（DDR 贡献是分解非分类），但可更诚实。\n\n### §5 Discussion\n- Mechanistic interpretation（top-p preserves shape）+ 两个可检验预测是亮点。\n- 但需更明确区分 post-hoc rationalization 和 empirical contribution（W5）。\n- Data curation pipeline 讨论需提及 downstream null result（W4）。\n- 14B preliminary evidence 建议移至 Appendix（M2）。\n- Instruct failure 的 mechanistic explanation 不足——是 RLHF reward shaping？SFT format constraints？还是 length regulation？\n\n### §6 Conclusion\n简洁到位，与 Abstract 一致。\n\n### Limitations\n覆盖全面：base-model scope、scale、prompt-type、temperature、English-only、reference model dependency。是本文最强的章节之一。\n\n### 附录\n详尽且组织合理。特别值得注意的优质内容：\n- Appendix V (DDR Partition Validation) 的 generator-split consistency 比 k-means 更有说服力——应在主文中更显著引用\n- Appendix Z.5 (Token-Level NLL Distribution) 的 kernel density plot 信息密度最高——可考虑将代表性示例提升到主文\n- Appendix M (Downstream Utility) 的 null result 必须在主文中讨论\n"
  }
}
```

</details>

---


### Tool result

_source line 2697 · 2026-05-21T02:53:05.052657+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_dbd68d7879a81efc0c108e9844b15d0b:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4320
}
```

</details>

---


### Assistant

_source line 2698 · 2026-05-21T02:53:18.850132+00:00_

审稿报告已投递至 Research Director。

**本轮审稿总结**：

- **Overall**: **3.5 (Borderline Conference)**
- **Reviewers**: R1 + R2 均评 3.5，经交叉审稿后维持评分
- **3 个 Critical 共识问题**: (1) k=2 聚类 7 点 "data-driven" 验证方法学不足；(2) tail_decay TOST 仅 4/8 通过；(3) 与 Markovian Chains 区分度不足
- **4 个 Major 共识问题**: base-model scope 张力、five "independent" metrics overclaim、TOST ε 循环论证、downstream null result 未在主文讨论
- **1 个分歧保留**: shape stability 是否 trivial（R2 认为 trivial 推论，R1 以温度消融反驳）
- **判断**: 分析框架新颖、实验控制顶级、写作诚实，足以进入 Findings；若补强 N1-N3，有望达 Conference

Issue Tracker 已同步更新（7 个新 issue + 5 个历史 issue 追加本轮 mention）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director"
}
```

</details>

---


## Round 238

## Round 238

2 recorded events


### User

_source line 2699 · 2026-05-21T02:53:21.717255+00:00_

[Reviewer 1 审稿结果]:
交叉审稿回应已提交。

总结：对 R2 的 8 个问题（3 Must-Fix + 5 Should-Fix），我的回应分布为：

- **3 个 AGREE**：N2（Markovian Chains 区分不足）、N3（instruct 退化，但建议降级为 Major）、W1（downstream null result）
- **3 个 REBUT**：N1（shape stability 非 trivial，有边界条件的经验发现）、W2（entropy 术语已在§3.3 说明）、W3（bib 条目实际上有 title，R2 事实错误）
- **2 个部分同意**：W4（binary F1 定义需在 Abstract 中澄清）、W5（14B 结果建议移至 Appendix）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 2700 · 2026-05-21T02:53:35.816838+00:00_

审稿报告已投递至 Research Director。

**本轮审稿总结**:

- **评分**: 3.5 (Borderline Conference)，R1 和 R2 一致
- **3 个 Critical 共识**: (1) k=2 聚类 7 点 "data-driven" 验证方法学不足；(2) tail_decay TOST 仅 4/8 通过；(3) 与 Markovian Chains 区分度不足
- **4 个 Major 共识**: base-model scope 与 motivation 张力、five "independent" metrics overclaim、TOST ε 循环论证、downstream null result 未在主文讨论
- **1 个分歧保留**: shape stability 是否 trivial（R1 反驳有力但 R2 核心论点仍成立）
- **视觉审查**: 4 warning（前 4 页无 display item、缺 pipeline 图、p.7 过密、p.8-9 纯文本）
- **Issue Tracker**: 已更新，7 个新 open issues + 3 个历史 issue 重新打开/追加

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director"
}
```

</details>

---


## Round 239

## Round 239

42 recorded events


### User

_source line 2701 · 2026-05-21T03:34:59.307931+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: gen-depth-fingerprint
- 论文路径: /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: ARR
- 截止日期: 2026-05-25

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 2702 · 2026-05-21T03:35:06.095641+00:00_

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
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 2703 · 2026-05-21T03:35:06.146384+00:00_

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
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2704 · 2026-05-21T03:35:12.226531+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__get_visual_check_status",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__get_visual_check_status",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 2705 · 2026-05-21T03:35:12.227043+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 2706 · 2026-05-21T03:35:15.690138+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "gen-depth-fingerprint"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "gen-depth-fingerprint"
  }
}
```

</details>

---


### Tool result

_source line 2707 · 2026-05-21T03:35:17.546293+00:00_

{"result":"# 项目 gen-depth-fingerprint 概况\n\n## 实验状态 (66 个)\n\n- **plan-015**: DONE (success) — \n- **plan-004**: DONE (failed) — \n- **plan-003**: DONE (success) — \n- **plan-013**: DONE (success) — \n- **plan-002**: DONE (success) — \n- **plan-002-qwen17b-retry-s1**: DONE (failed) — \n- **plan-002-qwen17b-retry-s0**: DONE (failed) — \n- **plan-002-qwen06b-s1**: DONE (failed) — \n- **plan-002-qwen06b-s0**: DONE (failed) — \n- **plan-002-qwen17b-s1**: DONE (failed) — \n- **plan-002-qwen17b-s0**: DONE (failed) — \n- **plan-002-qwen3-1_7b-s0**: DONE (failed) — \n- **plan-002-qwen3-1_7b-s1**: DONE (killed) — \n- **plan-001**: DONE (success) — \n- **mvp-001**: DONE (success) — \n\n## 最新报告\n# Handover — 2026-05-21\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n（无）\n\n## 近期结论\n- **plan-004-prep** (success): Downstream utility 准备：depth-stratified 数据集 + OLMo-1B fine-tuning 脚本（不开跑，等 Director 确认）\n- **review-exp-a-baseline-ensemble** (killed): 审稿回应实验A：4-baseline ensemble + 统一超参对比，验证 7-feature vs 4-baseline vs 6-feature 在公平条件下的性能差异\n- **multi_domain_t07** (killed): —\n\n## 趋势\n成功 47 / 负向 2 / 失败 12 / 共 66\n\n## 下一步\n（无活跃 idea，请通过 ideas.md 添加）\n\n## 资源状态\nbjb2-18868: 无 GPU 信息\n\n## 告警\n- mvp-001-gen-s0: 已被终止 — unknown\n- mvp-001-gen-s1: 训练失败 — unknown\n- mvp-001-gen-s2: 训练失败 — unknown\n- mvp-001-gen-s3: 训练失败 — unknown\n- plan-001-restore: 已被终止 — unknown\n- plan-002-qwen3-1_7b-s0: 训练失败 — unknown\n- plan-002-qwen3-1_7b-s1: 已被终止 — unknown\n- plan-002-qwen17b-s0: 训练失败 — unknown\n- plan-002-qwen17b-s1: 训练失败 — unknown\n- plan-002-qwen17b-retry-s0: 训练失败 — unknown\n- plan-002-qwen17b-retry-s1: 训练失败 — unknown\n- plan-002-qwen06b-s0: 训练失败 — unknown\n- plan-002-qwen06b-s1: 训练失败 — unknown\n- plan-004: 训练失败 — unknown\n- review-exp-a-baseline-ensemble: 已被终止 — unknown\n- multi_domain_t07: 已被终止 — unknown\n- exp_050_temp_curve_t09: 训练失败 — unknown"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 1856
}
```

</details>

---


### Tool call

_source line 2708 · 2026-05-21T03:35:17.697116+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/main.tex /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/main.pdf 2>&1",
  "description": "Check paper files exist"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/main.tex /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/main.pdf 2>&1",
    "description": "Check paper files exist"
  }
}
```

</details>

---


### Tool result

_source line 2709 · 2026-05-21T03:35:17.847894+00:00_

-rw-r--r-- 1 ubuntu ubuntu 2588849 May 21 03:31 /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/main.pdf
-rw-r--r-- 1 ubuntu ubuntu    3834 May 21 03:31 /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/main.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Bash",
  "elapsed_ms": 150
}
```

</details>

---


### Tool call

_source line 2710 · 2026-05-21T03:35:17.898356+00:00_

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
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
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

_source line 2711 · 2026-05-21T03:35:17.948886+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2712 · 2026-05-21T03:35:30.098480+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 call for papers ARR submission guidelines",
  "allowed_domains": "['aclweb.org', '2026.emnlp.org', 'openreview.net']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 call for papers ARR submission guidelines",
    "allowed_domains": "['aclweb.org', '2026.emnlp.org', 'openreview.net']"
  }
}
```

</details>

---


### Tool call

_source line 2713 · 2026-05-21T03:35:31.305055+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review 2026 author guidelines page limit template",
  "allowed_domains": "['aclrollingreview.org', 'aclweb.org']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review 2026 author guidelines page limit template",
    "allowed_domains": "['aclrollingreview.org', 'aclweb.org']"
  }
}
```

</details>

---


### Tool call

_source line 2714 · 2026-05-21T03:35:31.706733+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/review_issues.yaml 2>&1 || echo \"FILE_NOT_FOUND\"",
  "description": "Check existing review issues tracker"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/review_issues.yaml 2>&1 || echo \"FILE_NOT_FOUND\"",
    "description": "Check existing review issues tracker"
  }
}
```

</details>

---


### Tool result

_source line 2715 · 2026-05-21T03:35:31.808371+00:00_

# === Round 29-34 历史 Issues（保留完整记录）===

- id: "R29-N1"
  summary: "Base-model-only scope 未在 Abstract 标注"
  category: framing
  severity: critical
  status: resolved
  first_raised_round: 29
  last_seen_round: 32
  mentions:
    - {round: 29, reviewers: "R1+R2", note: "共识: Abstract 必须标注 base-model scope"}
    - {round: 31, reviewers: "R1+R2", note: "W1: Title/Abstract 仍需 base-model qualifier"}
    - {round: 32, reviewers: "R1+R2", note: "升级: 实验设计仅覆盖 base model, 建议扩展或限定 scope"}
  action_items:
    - {round: 29, action: "Abstract 加 base (pretrained) qualifier", assigned_to: Agent, status: done}
    - {round: 32, action: "Abstract/Conclusion 已有 qualifier; instruct in Discussion", assigned_to: Director, status: done}
  resolution: "Abstract L3 'eight base-model generators'; L7 'restricted to base models'. Title 保持不变(Reviewer 确认). Instruct limitations fully documented."
  resolution_round: 32

- id: "R29-N2"
  summary: "Downstream TOST underpowered (n=3) + Abstract overclaim"
  category: experiment
  severity: critical
  status: resolved
  first_raised_round: 29
  last_seen_round: 34
  mentions:
    - {round: 29, reviewers: "R1+R2", note: "n=3 seeds, Abstract 省略 preliminary"}
    - {round: 31, reviewers: "R1+R2", note: "W3: TOST n=3 underpowered"}
    - {round: 32, reviewers: "R1+R2", note: "升级为 null result: depth-aware curation 不优于 random"}
    - {round: 34, reviewers: "R1+R2", note: "RESOLVED: Abstract 完全移除 downstream claim; Appendix M 坦诚呈现 null result"}
  action_items:
    - {round: 29, action: "Abstract 加 preliminary qualifier", assigned_to: Agent, status: done}
    - {round: 32, action: "Abstract/Conclusion downstream reframing", assigned_to: Director, status: done}
  resolution: "Abstract 完全移除 downstream claim. Appendix M 保留 null result 作为补充材料."
  resolution_round: 34

- id: "R29-N3"
  summary: "DDR 新颖性 incremental — 缺 concurrent work 系统对比表"
  category: framing
  severity: critical
  status: resolved
  first_raised_round: 29
  last_seen_round: 31
  mentions:
    - {
…[truncated 20214 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Bash",
  "elapsed_ms": 101
}
```

</details>

---


### Tool result

_source line 2716 · 2026-05-21T03:35:37.899453+00:00_

Web search results for query: "EMNLP 2026 call for papers ARR submission guidelines"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"*SEM 2026: Commitment Link for ARR-Reviewed Papers (Deadline: 10 April 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/sem-2026-commitment-link-arr-reviewed-papers-deadline-10-april-2026"},{"title":"Workshop on Multimodal Interaction in Face-to-Face Dialogue (MINT @ EMNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/workshop-multimodal-interaction-face-face-dialogue-mint-emnlp-2026"},{"title":"EACL/ACL 2026 Joint Call for Workshops | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eaclacl-2026-joint-call-workshops"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"[EMNLP 2025] First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2025-first-call-papers"},{"title":"Joint Call for Tutorial Proposals (EACL/ACL) 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-eaclacl-2026"},{"title":"Jan. 2025 ACL Standing Committee on Peer Review (COPR) Report 1","url":"https://www.aclweb.org/adminwiki/images/9/9e/COPR-5-cycle-report-to-publish.pdf"},{"title":"EMNLP 2026 Workshop WiNLP ARR Commitment | OpenReview","url":"https://openreview.net/group?id=EMNLP%2F2026%2FWorkshop%2FWiNLP_ARR_Commitment"},{"title":"Call for Papers: The 20th Linguistic Annotation Workshop (LAW XX), co-located with ACL 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/call-papers-20th-linguistic-annotation-workshop-law-xx-co-located-acl-2026"}]

Based on the search results, here is the information about EMNLP 2026 call for papers and ARR submission guidelines:

## EM
…[truncated 1627 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "WebSearch",
  "elapsed_ms": 7800
}
```

</details>

---


### Tool result

_source line 2717 · 2026-05-21T03:35:37.950855+00:00_

Web search results for query: "ACL Rolling Review 2026 author guidelines page limit template"

Links: [{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"}]

Based on the search results, here's what I found about ACL Rolling Review 2026 author guidelines:

## Author Guidelines and Templates

There is an official Overleaf template for submissions. This template has a [review] setting that must be on for the submission.

ARR abandons the MS Word Template for conference submissions, and submissions based on the Word template will be desk-rejected starting from March 2026.

## Page Limits

Final versions of accepted papers will be given one additional page of content (up to 9 pages for long papers, up to 5 pages for shor
…[truncated 693 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "WebSearch",
  "elapsed_ms": 6645
}
```

</details>

---


### Tool call

_source line 2718 · 2026-05-21T03:36:07.510018+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 2719 · 2026-05-21T03:36:07.510429+00:00_

1	% EMNLP 2026 ARR Submission — ACL 2023 Template
2	\documentclass[11pt]{article}
3	\usepackage[review]{acl}
4	\usepackage{times}
5	\usepackage{latexsym}
6	\usepackage[T1]{fontenc}
7	\usepackage[utf8]{inputenc}
8	\usepackage{microtype}
9	\usepackage{graphicx}
10	\usepackage{booktabs}
11	\usepackage{enumitem}
12	\usepackage{amsmath}
13	\usepackage{amssymb}
14	\usepackage{placeins}
15	\usepackage{multirow}
16	\usepackage{float}
17	
18	\graphicspath{{../chart/}}
19	
20	\title{Depth Fingerprinting: Detecting Recursive Generation Depth\\in LLM Text Chains}
21	
22	\author{Anonymous}
23	
24	\begin{document}
25	\maketitle
26	
27	\input{abstract}
28	
29	\input{introduction}
30	\input{related_work}
31	\input{method}
32	\input{results}
33	
34	\input{discussion}
35	\input{conclusion}
36	\input{limitations}
37	\input{ethics}
38	
39	\bibliography{references}
40	
41	\appendix
42	
43	\noindent\textbf{Note:} Unless otherwise stated, appendix experiments use the original six-generator subset (Pythia-2.8B/1B, OLMo-2-1B, Qwen3-1.7B/0.6B/8B).
44	Main paper results (\S\ref{sec:results}) use the full eight-generator set (adding Llama-3.2-3B and Mistral-7B-v0.3).
45	
46	\input{appendix_dataset_stats}
47	
48	\section{Length Confound Analysis}
49	\label{app:length}
50	\input{appendix_length}
51	
52	\section{Prompt Type Generalization}
53	\label{app:prompt-type}
54	\input{appendix_prompt_type}
55	
56	\section{Finer-Grained Depth Classification}
57	\label{app:finer-depth}
58	\input{appendix_finer_depth}
59	
60	\section{End-to-End Depth Classification (QLoRA)}
61	\label{app:qlora}
62	\input{appendix_qlora}
63	
64	\section{Leave-One-Feature-Out Analysis}
65	\label{app:lofo}
66	\input{appendix_lofo}
67	
68	\section{Confusion Matrix}
69	\label{app:confusion}
70	\input{appendix_confusion_matrix}
71	
72	\section{Classifier Sensitivity}
73	\label{app:classifier}
74	\input{appendix_classifier}
75	\FloatBarrier
76	
77	\section{Robustness to Text Perturbation}
78	\label{app:human-edit}
79	\input{appendi
…[truncated 2404 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 2720 · 2026-05-21T03:36:12.277969+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 2721 · 2026-05-21T03:36:12.579763+00:00_

1	% Abstract — Depth Fingerprinting of Recursive LLM Generation Chains
2	\begin{abstract}
3	When LLM outputs re-enter generation pipelines, each recursive step compresses \emph{where} text sits in distributional space while leaving \emph{how} it is shaped nearly unchanged.
4	We formalize this asymmetry as \emph{differential depth response} (DDR) and characterize it across eight \textbf{base-model} generators spanning five architectural families (0.6B--8B parameters): under nucleus sampling ($p{=}0.9$, $\tau \leq 0.7$), NLL location statistics and lexical diversity drift monotonically with generation depth (Cohen's $d{=}0.76$--$1.17$), while distributional shape features remain near-stationary ($d < 0.10$)---a separation confirmed by five complementary effect-size measures and clustering-based validation (silhouette\,=\,0.660).
5	Where prior work on iterative generation documents \emph{what converges}, the novel observation here is \emph{what is preserved}: shape invariance under the same process that compresses location provides the stable reference needed for depth estimation without per-generator calibration.
6	As a proof of concept, a lightweight 7-feature ensemble exploiting DDR achieves leak-free binary F1\,=\,0.694 (gen-1 vs.\ gen-2+, excluding shared gen-0 seeds) under leave-one-generator-out evaluation, confirming that the decomposition yields actionable depth signal; an end-to-end classifier recovers substantially more (F1\,=\,0.905), establishing the analytical framework---not the specific features---as the primary contribution.
7	The signal attenuates under instruction tuning; current applicability is restricted to base models.
8	\end{abstract}
9	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 2722 · 2026-05-21T03:36:12.630404+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 2723 · 2026-05-21T03:36:13.132695+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	AI text detection asks a single binary question---\emph{human or machine?}---and recent methods answer it with increasing reliability \cite{detectgpt,fast_detectgpt,binoculars,ld_score}.
5	Yet this framing elides a richer structure emerging on the open web: as LLM outputs re-enter training corpora \cite{dolma,fineweb} and seed further generation, text accumulates at varying \emph{recursive depths}---an estimated 7--17\% of recent scientific publications already contain substantial LLM-modified content \cite{mapping_llm_science,monitoring_ai_review}---and each generation cycle pushes distributional properties further from both the human source and the first-generation predecessor.
6	While most deployed LLM outputs use instruction-tuned models, base-model generation pipelines remain prevalent in synthetic data production, pre-training corpus construction, and recursive data augmentation.
7	Knowing \emph{how many times} text has been recursively generated matters for data provenance \cite{ccnet,dsir} and model collapse analysis \cite{curse_of_recursion,strong_model_collapse}, yet no current method moves beyond the binary boundary.
8	
9	We introduce \emph{depth fingerprinting}: classifying text by ordinal generation depth (gen-0\,/\,gen-1\,/\,gen-2+) and decomposing the distributional drift that accumulates across depths into structurally distinct components.
10	The core empirical finding is a \emph{differential depth response} (DDR): across eight base-model generators spanning five architectural families (0.6B--8B), the NLL distribution's central tendency (mean entropy, lexical diversity) drifts monotonically with depth while its shape (entropy extremes, tail structure) remains an order of magnitude more stable ($d{=}0.76$--$1.17$ vs.\ $d < 0.10$; five complementary effect-size measures converge on this partition).
11	This location/shape asymmetry exposes a structural property of fixed-parameter autoregressive sa
…[truncated 2150 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 2724 · 2026-05-21T03:36:13.133033+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 2725 · 2026-05-21T03:36:13.233693+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	\subsection{Task Formulation}
5	\label{sec:task}
6	
7	Given a text $x$, we predict its \emph{generation depth} $d \in \{0, 1, 2{+}\}$: human-written ($d{=}0$), first-generation LLM output ($d{=}1$), or text produced by two or more recursive LLM generations ($d{=}2{+}$).
8	A generation chain of depth $k$ is defined recursively: $x^{(0)} \sim \mathcal{C}_0$ (human corpus), $x^{(k)} = G(x^{(k-1)})$ for $k \geq 1$, where $G$ denotes stochastic autoregressive generation.
9	Depths beyond 2 are merged into $2{+}$ because feature convergence compresses inter-class margins at deeper levels (\S\ref{sec:results-differential}).
10	
11	\subsection{Generation Chain Construction}
12	\label{sec:generation}
13	
14	We construct generation chains using eight generators spanning five model families: \textbf{Pythia} (2.8B, 1B) \cite{pythia}, \textbf{OLMo} (OLMo-2-1B) \cite{olmo}, \textbf{Qwen} (Qwen3-1.7B, Qwen3-0.6B, Qwen3-8B-Base) \cite{qwen3}, \textbf{Llama} (Llama-3.2-3B) \cite{llama3}, and \textbf{Mistral} (Mistral-7B-v0.3) \cite{mistral7b}.
15	This selection spans parameter scales from 0.6B to 8B and diverse pretraining corpora, enabling evaluation of cross-generator and cross-scale generalization.
16	
17	For each generator, we sample approximately 1{,}000 seed passages from English Wikipedia as $\mathcal{C}_0$.
18	The same pool of seed passages serves as gen-0 for all generators.
19	We use shared seeds across generators so that cross-generator comparisons control for input content and isolate the effect of the generation model from source text variation.
20	In LOGO evaluation, gen-0 samples from the held-out generator's chains also appear (with the same text) in the training generators' chains, creating a potential train--test overlap for the gen-0 class.
21	We address this with a supplementary binary evaluation excluding gen-0 entirely (\S\ref{sec:results-baselines}).
22	Each seed is iteratively fed through the generator to produce a 
…[truncated 6045 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 2726 · 2026-05-21T03:36:16.647834+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/results.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/results.tex"
  }
}
```

</details>

---


### Tool result

_source line 2727 · 2026-05-21T03:36:17.000039+00:00_

1	\section{Results}
2	\label{sec:results}
3	
4	\subsection{Depth Classification Performance}
5	\label{sec:results-classification}
6	
7	Before analyzing the DDR decomposition (\S\ref{sec:results-differential}), we establish that generation depth is classifiable across diverse architectures.
8	The 7-feature ensemble achieves 3-class LOGO F1\,=\,0.762 (95\% CI [0.758, 0.766]; $N$\,=\,37{,}058) across eight generators from five families (Table~\ref{tab:logo-results}).
9	Bootstrap CIs reflect sampling variability within each LOGO fold; the cross-generator F1 spread (9.1\,pp) additionally captures generator selection uncertainty.
10	Because gen-0 seeds are shared across generators (\S\ref{sec:generation}), gen-0 classification is near-perfect (per-class F1\,$\approx$\,0.94), inflating the 3-class metric.
11	We therefore adopt \textbf{leak-free binary F1} (gen-1 vs.\ gen-2+)\,=\,0.694 (CI [0.688, 0.700]) as the primary metric throughout: it excludes gen-0 entirely and is unaffected by seed sharing.
12	Per-generator binary F1 ranges from 0.633 (Mistral-7B) to 0.724 (Pythia-2.8B), with the primary difficulty concentrated at the gen-1\,/\,gen-2+ boundary (Appendix~\ref{app:confusion}).
13	
14	\paragraph{Cross-model generalization.}
15	Cross-model chains (randomly selected generator per step) yield binary F1\,=\,0.830 (95\% CI [.818, .841]) under 5-generator LOGO.\footnote{5-generator subset (Pythia-2.8B/1B, OLMo-2-1B, Qwen3-0.6B/1.7B); generator-level LOGO with bootstrap CIs ($n$\,=\,2{,}000). Not directly comparable to 8-generator LOGO due to differing subsets.}
16	Single-generator transfer (Appendix~\ref{app:transfer}) confirms the signal is not a mixed-chain artifact: classifiers trained on one generator transfer to all others with mean binary F1\,=\,0.810; LOFO yields 0.686.
17	A scale effect emerges: Pythia achieves the highest F1 (0.718--0.724) while larger models degrade (Mistral-7B: 0.633), partly reflecting same-family affinity with the Pythia-410M reference (cross-r
…[truncated 13510 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "elapsed_ms": 352
}
```

</details>

---


### Tool call

_source line 2728 · 2026-05-21T03:36:17.000426+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 2729 · 2026-05-21T03:36:17.051041+00:00_

1	\section{Discussion}
2	\label{sec:discussion}
3	
4	Recursive generation alters \emph{where} the token-level surprise distribution sits but not \emph{how} it is shaped---a dichotomy that admits a mechanistic interpretation.
5	Under nucleus sampling, top-$p$ truncation selects from a fixed probability-mass fraction at each step, preserving the functional form of the conditional distribution regardless of input content.
6	What changes across recursive steps is the \emph{input} to this truncation: as the model conditions on its own increasingly self-typical outputs, the expected token-level NLL compresses monotonically---each generation feeds slightly more predictable input into the same shape-preserving mechanism.
7	This account yields two testable predictions: (1)~increasing sampling randomness should weaken the location drift by disrupting mode-seeking, and (2)~semantic-preservation constraints should attenuate it by anchoring the input distribution.
8	Both are empirically confirmed: at $t{=}1.0$, the location signal collapses ($\rho$: $-0.60 \to -0.002$; Appendix~\ref{app:sampling-sensitivity}); under elaboration prompts, drift weakens relative to continuation (F1\,=\,0.730 vs.\ 0.781; Appendix~\ref{app:prompt-type}), consistent with \citet{broken_telephone}, while cross-type transfer remains viable (F1\,=\,0.753).
9	Permutation importance, Granger causality, and feature intervention analyses provide further causal evidence: drifting features contribute $5.5\times$ more to classification than near-stationary ones, with 6/7 features exhibiting significant Granger causality (Appendix~\ref{app:ddr-causality}).
10	
11	The classifier is a proof-of-concept, not a deployable system: document-level gen-1 per-class F1\,=\,0.63 and ${\sim}30\%$ error rate are insufficient for automated filtering but sufficient for corpus-level auditing ($O(1/\sqrt{n})$ error scaling), with the primary difficulty being gen-1 vs.\ gen-2+ discrimination (86\% false negatives; Appendix~\ref{app
…[truncated 4068 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2730 · 2026-05-21T03:36:17.453523+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 2731 · 2026-05-21T03:36:18.809456+00:00_

1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	Recursive generation leaves a systematic distributional signature: central-tendency features drift monotonically with depth while shape features remain an order of magnitude more stable---a dichotomy we formalize as differential depth response (DDR), validated across eight generators from five model families.
5	This decomposition enables cross-generator depth classification (leak-free binary F1\,=\,0.694; end-to-end: 0.905) and provides an analytical lens complementary to model collapse: fixed-parameter sampling compresses distributional location while preserving shape, whereas retraining erodes both.
6	Current boundaries are instruction tuning---where alignment reshapes the generation attractor---and frontier scale, where preliminary 14B evidence confirms the partition with attenuated effect sizes.
7	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "elapsed_ms": 1355
}
```

</details>

---


### Tool call

_source line 2732 · 2026-05-21T03:36:18.860208+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 2733 · 2026-05-21T03:36:18.910896+00:00_

1	\section{Related Work}
2	\label{sec:related}
3	
4	\subsection{AI-Generated Text Detection}
5	\label{sec:related-detection}
6	
7	The detection literature spans statistical tests \cite{gltr,grover,release_strategies}, zero-shot scoring \cite{detectgpt,fast_detectgpt,binoculars,dna_gpt}, surprisal diversity \cite{diveye}, and learned classifiers \cite{ghostbuster,feat_aug_transformer,reliable_detection,ld_score}; see \citet{wu_survey_2025} and \citet{jawahar_survey} for surveys.
8	RAID \cite{raid} benchmarks binary detection across generators and attacks; we extend the task from binary to ordinal depth estimation.
9	Several recent efforts move beyond the binary boundary---collaboration roles \cite{beyond_binary}, joint detection-attribution \cite{two_birds}, creator-editor modes \cite{beyond_final_actor}, multi-generator attribution \cite{semeval2024_task8}---but all taxonomize by \emph{source} or \emph{production mode}, not recursive generation \emph{depth}; repurposing their scores as depth predictors reveals high cross-generator variance (binary F1\,=\,0.52--0.71; Table~\ref{tab:baselines}) \cite{paraphrase_evades,detection_possibilities}.
10	Our contribution is orthogonal: the task formulation itself (ordinal depth classification \cite{gutierrez_ordinal_survey,coral_ordinal,kasa_ordinality_nlp}) and the finding that drifting and stationary features together yield consistent cross-generator performance where individual detection scores do not \cite{uchendu_attribution,munir_looking_glass}.
11	
12	\subsection{Model Collapse and Iterative Generation}
13	\label{sec:related-collapse}
14	
15	Self-consuming generative models progressively lose distributional coverage \cite{self_consuming_mad,curse_of_recursion,seddik_synthetic_data}, though data mixing mitigates collapse \cite{model_collapse_avoidable,strong_model_collapse}.
16	These studies address \emph{training-loop} degradation where parameter updates erode tail coverage; indeed, \citet{schaeffer_collapse_position} 
…[truncated 2865 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2734 · 2026-05-21T03:36:38.051935+00:00_

called mcp__agent-ml-research__dispatch_visual_check

<details open><summary>🔧 Tool call — mcp__agent-ml-research__dispatch_visual_check</summary>

```json
{
  "project": "gen-depth-fingerprint",
  "review_chat_id": "oc_999770e4e57bfc6eabd12fc1f64af1ef"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "tool_args": {
    "project": "gen-depth-fingerprint",
    "review_chat_id": "oc_999770e4e57bfc6eabd12fc1f64af1ef"
  }
}
```

</details>

---


### Tool call

_source line 2735 · 2026-05-21T03:36:40.861420+00:00_

called mcp__agent-ml-research__request_external_review

<details open><summary>🔧 Tool call — mcp__agent-ml-research__request_external_review</summary>

```json
{
  "project": "gen-depth-fingerprint",
  "paper_pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/main.pdf",
  "venue": "EMNLP 2026",
  "note": "Round 36 fresh review. Deadline 2026-05-25."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__request_external_review",
  "tool_args": {
    "project": "gen-depth-fingerprint",
    "paper_pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/main.pdf",
    "venue": "EMNLP 2026",
    "note": "Round 36 fresh review. Deadline 2026-05-25."
  }
}
```

</details>

---


### Tool result

_source line 2736 · 2026-05-21T03:36:59.245363+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 21193
}
```

</details>

---


### Tool result

_source line 2737 · 2026-05-21T03:36:59.245757+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"pending\", \"message\": \"外部审稿请求已发送到用户群。将在 8 小时后自动提醒。\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__request_external_review",
  "elapsed_ms": 18384
}
```

</details>

---


### Tool call

_source line 2738 · 2026-05-21T03:36:59.697893+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "text": "你是 Reviewer 1，负责**方法严谨性**审查。\n\n## 论文信息\n- 标题: Depth Fingerprinting: Detecting Recursive Generation Depth in LLM Text Chains\n- 论文路径: /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/main.tex\n- PDF: /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/main.pdf\n- 目标 venue: EMNLP 2026 (ARR)\n- Deadline: 2026-05-25\n\n## Venue 要求\n- ARR 统一审稿，double-blind\n- Long paper: 8 页正文限制（不含 references/limitations/ethics）\n- ACL 模板，\\usepackage[review]{acl}\n- 必须有 Limitations section\n- Overall Assessment 评分: 5=Award, 4=Conference, 3=Findings, 2=Resubmit, 1=Do not resubmit\n\n## 你的审查侧重\n\n**方法严谨性**，重点关注：\n\n1. **DDR 分析框架的统计严谨性**:\n   - k=2 聚类在 7 个特征点上是否方法论充分？silhouette 分数的统计意义？\n   - TOST 等价性检验: epsilon=0.20 的选择是否有循环论证问题？tail_decay 仅 4/8 generator 通过 TOST 的处理是否诚实？\n   - 五种 effect-size measures 是否真正\"independent\"？parametric measures 之间的相关性？\n   - permutation test (p=0.030) 是否足够有力？\n\n2. **实验设计与评估协议**:\n   - LOGO 评估是否存在信息泄露（gen-0 共享种子）？binary F1 排除 gen-0 是否充分解决？\n   - 长度混淆控制是否到位？\n   - 种子共享控制（demeaning, independent-seed）是否充分？\n   - 温度/prompt 类型泛化测试的覆盖度\n\n3. **统计报告的完整性和诚实度**:\n   - 所有统计声明是否有充分支撑？是否存在 overclaim？\n   - Bootstrap CI 是否反映正确的不确定性来源？per-generator spread 9.1pp 与 sampling CI 的关系？\n   - QLoRA +11.6pp baseline 标注是否一致（vs 6-gen 还是 8-gen）？\n\n4. **可复现性**:\n   - 实验细节是否完整（超参数、种子、数据集大小）？\n   - 代码/数据承诺？\n\n请阅读完整论文（包括相关附录），给出详细审稿意见，格式为:\n- Summary (2-3 句)\n- Strengths (逐条)\n- Weaknesses (逐条，标注 [Critical/Major/Minor])\n- Questions (需要作者回答)\n- Missing References\n- Overall Assessment (评分 + 理由)",
  "reviewer_id": "1",
  "project": "gen-depth-fingerprint",
  "round_number": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "text": "你是 Reviewer 1，负责**方法严谨性**审查。\n\n## 论文信息\n- 标题: Depth Fingerprinting: Detecting Recursive Generation Depth in LLM Text Chains\n- 论文路径: /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/main.tex\n- PDF: /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/main.pdf\n- 目标 venue: EMNLP 2026 (ARR)\n- Deadline: 2026-05-25\n\n## Venue 要求\n- ARR 统一审稿，double-blind\n- Long paper: 8 页正文限制（不含 references/limitations/ethics）\n- ACL 模板，\\usepackage[review]{acl}\n- 必须有 Limitations section\n- Overall Assessment 评分: 5=Award, 4=Conference, 3=Findings, 2=Resubmit, 1=Do not resubmit\n\n## 你的审查侧重\n\n**方法严谨性**，重点关注：\n\n1. **DDR 分析框架的统计严谨性**:\n   - k=2 聚类在 7 个特征点上是否方法论充分？silhouette 分数的统计意义？\n   - TOST 等价性检验: epsilon=0.20 的选择是否有循环论证问题？tail_decay 仅 4/8 generator 通过 TOST 的处理是否诚实？\n   - 五种 effect-size measures 是否真正\"independent\"？parametric measures 之间的相关性？\n   - permutation test (p=0.030) 是否足够有力？\n\n2. **实验设计与评估协议**:\n   - LOGO 评估是否存在信息泄露（gen-0 共享种子）？binary F1 排除 gen-0 是否充分解决？\n   - 长度混淆控制是否到位？\n   - 种子共享控制（demeaning, independent-seed）是否充分？\n   - 温度/prompt 类型泛化测试的覆盖度\n\n3. **统计报告的完整性和诚实度**:\n   - 所有统计声明是否有充分支撑？是否存在 overclaim？\n   - Bootstrap CI 是否反映正确的不确定性来源？per-generator spread 9.1pp 与 sampling CI 的关系？\n   - QLoRA +11.6pp baseline 标注是否一致（vs 6-gen 还是 8-gen）？\n\n4. **可复现性**:\n   - 实验细节是否完整（超参数、种子、数据集大小）？\n   - 代码/数据承诺？\n\n请阅读完整论文（包括相关附录），给出详细审稿意见，格式为:\n- Summary (2-3 句)\n- Strengths (逐条)\n- Weaknesses (逐条，标注 [Critical/Major/Minor])\n- Questions (需要作者回答)\n- Missing References\n- Overall Assessment (评分 + 理由)",
    "reviewer_id": "1",
    "project": "gen-depth-fingerprint",
    "round_number": "1"
  }
}
```

</details>

---


### Tool result

_source line 2739 · 2026-05-21T03:37:14.955176+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 15257
}
```

</details>

---


### Tool call

_source line 2740 · 2026-05-21T03:37:15.407336+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "text": "你是 Reviewer 2，负责**新颖性与完整性**审查。\n\n## 论文信息\n- 标题: Depth Fingerprinting: Detecting Recursive Generation Depth in LLM Text Chains\n- 论文路径: /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/main.tex\n- PDF: /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/main.pdf\n- 目标 venue: EMNLP 2026 (ARR)\n- Deadline: 2026-05-25\n\n## Venue 要求\n- ARR 统一审稿，double-blind\n- Long paper: 8 页正文限制（不含 references/limitations/ethics）\n- ACL 模板，\\usepackage[review]{acl}\n- 必须有 Limitations section\n- Overall Assessment 评分: 5=Award, 4=Conference, 3=Findings, 2=Resubmit, 1=Do not resubmit\n\n## 你的审查侧重\n\n**新颖性与完整性**，重点关注：\n\n1. **贡献的新颖性和增量性**:\n   - DDR 是否只是 diversity loss / mode collapse 的重新表述？\"what is preserved\" vs \"what converges\" 的区分是否实质性？\n   - 与 Markovian Chains (Geng et al., 2026) 和 Broken Telephone (Sharoff, 2025) 的区分度是否充分？\n   - 从 binary detection 到 ordinal depth classification 的 task formulation 新颖性如何？\n   - shape stability 是否只是 nucleus sampling 的 trivial 推论？\n\n2. **Framing 一致性**:\n   - Abstract/Intro/Results/Discussion 的 claim 是否一致？scope 限定（base-model only, tau<=0.7）是否在各处清晰标注？\n   - Contribution 列表是否与实际内容匹配？proof-of-concept 定位是否贯穿全文？\n   - Downstream null result（Appendix M）是否在 Discussion 中被诚实讨论？\n\n3. **Related Work 覆盖度**:\n   - 是否缺少重要的相关工作？特别是 2025-2026 年的新工作？\n   - 引用格式和完整性（orphan entries, phantom citations, first-author mismatch）\n   - 对比表（如有）是否公平准确？\n\n4. **写作质量**:\n   - 论文 story 是否连贯？前 4 页无图表的纯文字密度是否影响可读性？\n   - 术语使用是否一致（entropy = NLL shorthand 的声明）？\n   - 附录结构是否合理？关键信息是否在主文有足够讨论？\n\n5. **格式合规**:\n   - 页数是否符合 8 页限制？\n   - Limitations section 是否存在且有实质内容？\n   - 匿名性是否完好？\n\n请阅读完整论文（包括相关附录），给出详细审稿意见，格式为:\n- Summary (2-3 句)\n- Strengths (逐条)\n- Weaknesses (逐条，标注 [Critical/Major/Minor])\n- Questions (需要作者回答)\n- Missing References\n- Overall Assessment (评分 + 理由)",
  "reviewer_id": "2",
  "project": "gen-depth-fingerprint",
  "round_number": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "text": "你是 Reviewer 2，负责**新颖性与完整性**审查。\n\n## 论文信息\n- 标题: Depth Fingerprinting: Detecting Recursive Generation Depth in LLM Text Chains\n- 论文路径: /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/main.tex\n- PDF: /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/main.pdf\n- 目标 venue: EMNLP 2026 (ARR)\n- Deadline: 2026-05-25\n\n## Venue 要求\n- ARR 统一审稿，double-blind\n- Long paper: 8 页正文限制（不含 references/limitations/ethics）\n- ACL 模板，\\usepackage[review]{acl}\n- 必须有 Limitations section\n- Overall Assessment 评分: 5=Award, 4=Conference, 3=Findings, 2=Resubmit, 1=Do not resubmit\n\n## 你的审查侧重\n\n**新颖性与完整性**，重点关注：\n\n1. **贡献的新颖性和增量性**:\n   - DDR 是否只是 diversity loss / mode collapse 的重新表述？\"what is preserved\" vs \"what converges\" 的区分是否实质性？\n   - 与 Markovian Chains (Geng et al., 2026) 和 Broken Telephone (Sharoff, 2025) 的区分度是否充分？\n   - 从 binary detection 到 ordinal depth classification 的 task formulation 新颖性如何？\n   - shape stability 是否只是 nucleus sampling 的 trivial 推论？\n\n2. **Framing 一致性**:\n   - Abstract/Intro/Results/Discussion 的 claim 是否一致？scope 限定（base-model only, tau<=0.7）是否在各处清晰标注？\n   - Contribution 列表是否与实际内容匹配？proof-of-concept 定位是否贯穿全文？\n   - Downstream null result（Appendix M）是否在 Discussion 中被诚实讨论？\n\n3. **Related Work 覆盖度**:\n   - 是否缺少重要的相关工作？特别是 2025-2026 年的新工作？\n   - 引用格式和完整性（orphan entries, phantom citations, first-author mismatch）\n   - 对比表（如有）是否公平准确？\n\n4. **写作质量**:\n   - 论文 story 是否连贯？前 4 页无图表的纯文字密度是否影响可读性？\n   - 术语使用是否一致（entropy = NLL shorthand 的声明）？\n   - 附录结构是否合理？关键信息是否在主文有足够讨论？\n\n5. **格式合规**:\n   - 页数是否符合 8 页限制？\n   - Limitations section 是否存在且有实质内容？\n   - 匿名性是否完好？\n\n请阅读完整论文（包括相关附录），给出详细审稿意见，格式为:\n- Summary (2-3 句)\n- Strengths (逐条)\n- Weaknesses (逐条，标注 [Critical/Major/Minor])\n- Questions (需要作者回答)\n- Missing References\n- Overall Assessment (评分 + 理由)",
    "reviewer_id": "2",
    "project": "gen-depth-fingerprint",
    "round_number": "1"
  }
}
```

</details>

---


### Tool result

_source line 2741 · 2026-05-21T03:37:17.067026+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1659
}
```

</details>

---


### Assistant

_source line 2742 · 2026-05-21T03:37:23.641816+00:00_

Round 1 全部派发完毕：

| 任务 | 状态 |
|------|------|
| Reviewer 1（方法严谨性） | 已派发，独立审稿中 |
| Reviewer 2（新颖性/完整性） | 已派发，独立审稿中 |
| 视觉审查 Agent | 已启动，与 Reviewer 并行 |
| 外部审稿（Stanford Agentic Reviewer） | 已发送请求，8h 后自动提醒 |

等待两位 Reviewer 返回初审意见后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director"
}
```

</details>

---


## Round 240

## Round 240

2 recorded events


### User

_source line 2743 · 2026-05-21T03:45:14.833728+00:00_

[Reviewer 2 审稿意见]:

# Reviewer 2 审稿意见：Depth Fingerprinting（新颖性与完整性）

## 总体评分
**Overall Assessment**: 3.0 — Findings
**一句话总结**: DDR 分解（drifting vs. stationary features）是一个有意义的经验性贡献，但相对于已有的 model collapse 和 iterative generation 文献，新颖性增量有限；base-model-only 范围和 downstream null result 制约了实际影响力；主文页数可能超过 8 页限制。

---

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | 实验设计严谨（LOGO CV、shared seeds、TOST equivalence testing），统计方法充分；但 shape stability 是否为 nucleus sampling 的 trivial 推论未被充分论证，reference model 选择（Pythia-410M）引入潜在偏差 |
| Excitement | 2.5/5 | DDR 分解角度有一定新意，ordinal depth task formulation 有价值；但实际应用受限（base-model only, 3-class 粒度, downstream null result），不太可能改变社区对 AI text detection 的研究方向 |
| Reproducibility | 4/5 | 特征定义清晰（Section 3.3），数据构建流程明确（Section 3.2），超参数完整（Table 1 注释 + Appendix W），承诺释放代码和模型；唯一不确定性是 Wikipedia seed 的具体选取标准 |
| Overall Assessment | 3.0/5 | Findings 水平：经验分析扎实但增量性较强，实际影响力不足以支撑主会议接收 |

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] 主文页数可能超过 8 页限制
- 具体位置：Page 9 — Section 6 (Conclusion) 结束于约页面 75% 处，Limitations 从该处开始
- 问题：EMNLP 2026 long paper 严格限制主文 8 页（Limitations/Ethics 不计入）。从 Page 1（含 title + abstract）到 Section 6 Conclusion 结束，主文约占 8.5–8.7 页。Discussion（Section 5）独占整个 Page 8 并延续至 Page 9 上部约 1/3，然后 Conclusion 再占约 1/3。
- 为什么影响接收：格式违规是 desk reject 的直接原因，ARR 对此执行严格。
- 建议修改方向：压缩 Discussion（约 1.3 页）至 ~0.8 页——将部分讨论移至附录，或精简 cross-family reference model 和 temperature sensitivity 的重复论述（已有 Appendix H/Z.1 详细覆盖）。Conclusion 也可适当压缩。

**N2** [critical] DDR 与 model collapse / diversity loss 的区分度不足
- 具体位置：Section 1 (Introduction, p.1), Section 4.2 (p.5-6), Section 5 (Discussion, p.8)
- 问题：DDR 的三个 "drifting" 特征——entropy_mean 下降、TTR 下降、hapax_ratio 下降——本质上就是 model collapse 文献中反复记录的 diversity loss / entropy erosion 现象（Shumailov et al., 2024; Guo et al., 2024; Dohmatob et al., 2025）。论文声称 DDR 的新颖性在于 "what is preserved"（shape stability），但这是否只是 nucleus sampling 在固定 p=0.9 下的 trivial 推论？当 nucleus sampling 在固定概率质量阈值处截断时，tail structure（entropy_max, tail_decay）保持稳定几乎是 by design 的结果。
  
  论文在 Section 4.2 提到 "structural property of fixed-parameter autoregressive sampling" 和 Abstract 中 "shape invariance under...the same process that compresses location"，但没有提供反驳证据——例如：在不同解码策略（greedy, top-k, temperature-only）下 shape stability 是否同样成立？如果只在 nucleus sampling 下成立，这更像是 sampling 机制的已知属性而非新发现。
- 为什么影响接收：这是论文核心贡献的新颖性问题。如果 DDR 的 "novel observation" 是 sampling 机制的 trivial 推论，论文的主要创新贡献将大幅缩水。
- 建议修改方向：(1) 在不同 decoding 策略下验证 shape stability 是否保持，以证明这不仅仅是 nucleus sampling 的产物；(2) 提供更明确的理论论证，说明为什么 location/shape 分解提供了超越 "diversity loss 的另一面" 的洞察；(3) 明确承认与 model collapse 文献的重叠度，并精准界定增量贡献。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [major] Downstream null result 在主文中讨论不充分
- 具体位置：Section 5 Discussion (p.8), Appendix M (p.22-23)
- 问题：Appendix M 的 TOST equivalence testing 清晰地表明 depth-aware data curation 与 random subsampling 在 downstream perplexity 上无实质差异。这是一个重要的 null result，直接关系到论文在 Introduction 中提出的 data provenance 动机（"Knowing how many times text has been recursively generated matters for data provenance", p.1）。主文 Discussion 只用一句带过："We note, however, that depth-aware data curation does not yet translate into downstream training gains"（p.8），但这个发现本应在 Contribution 列表或 Discussion 中获得更显著的位置。
- 建议：在 Discussion 中增加一个专门段落讨论这一 null result 的含义，以及在什么条件下 depth signal 可能转化为实际 downstream benefit。

**W2** [major] Base-model-only 范围严重限制实际适用性
- 具体位置：Limitations (p.9), Appendix K (p.20-21)
- 问题：Appendix K 显示 instruction-tuned models 下 3-class F1 下降 3.7-19.6pp，binary F1 从 ~0.69 降至 ~0.45-0.49。在 2025-2026 年，绝大多数部署的 LLM 都是 instruction-tuned 的。论文在 Limitations 中承认了这一点，但 Abstract 和 Introduction 的措辞（"When LLM outputs re-enter generation pipelines"）给读者的印象是方法具有广泛适用性。
- 建议：(1) 在 Abstract 中更显式地标注 "base-model continuation chains" 的范围限定；(2) 将 Appendix K 的关键数字（F1 下降幅度）简要纳入主文 Discussion 或 Limitations。

**W3** [major] 3-class 粒度的实际价值论证不足
- 具体位置：Section 3.1 (p.3), Appendix D (p.14, Table 4-5)
- 问题：论文将 depth 2+ 合并为一类（因为 deeper depths become indistinguishable, Appendix D 的 5-class F1 进一步下降），最终只能区分 gen-0 / gen-1 / gen-2+。从 binary detection 到 3-class ordinal 的提升是论文声称的 task formulation 新颖性，但 3-class 相比 binary 的实际增量价值是什么？论文没有给出令人信服的 use case 来说明为什么区分 gen-1 和 gen-2+ 在实际中有意义。
- 建议：提供具体的应用场景说明 3-class 分类的实际价值——例如在 data curation pipeline 中，区分 gen-1 和 gen-2+ 如何导致不同的处理决策。

**W4** [minor-major] 前 3.5 页无任何图表，信息密度不均
- 具体位置：Pages 1-4（Abstract 到 Section 3.3 中部）
- 问题：作为 empirical paper，前 3.5 页全是纯文字（第一个视觉元素 Table 1 出现在 Page 4 下半部分，Figure 1 出现在 Page 5-6）。这对可读性有负面影响。Related Work (Section 2) 超过 1.5 页且缺乏结构化对比（无对比表）。
- 建议：(1) 在 Section 1 或 Section 2 加入一个 method comparison table，将本文与 Broken Telephone、Markovian Chains、binary detection 的 task/method/finding 差异可视化；(2) 考虑将 Figure 1 或 Figure 2 的简化版前移到 Method 或 Introduction。

**W5** [minor] Reference model (Pythia-410M) 选择的 confound 在主文讨论不足
- 具体位置：Section 3.3 (p.3-4), Appendix S (p.26)
- 问题：所有 entropy-based features 都依赖 Pythia-410M 作为 reference model。Appendix S 验证了 cross-family reference model 的信号保持，但主文仅用 "cross-family reference model experiments (§4.2)" 一笔带过。当 8 个 generator 中有 2 个来自 Pythia family（Pythia-2.8B, 1B），reference model 同家族偏差应在主文明确讨论。
- 建议：在 Section 3.3 或 Section 5 中简要讨论 reference model 选择的潜在偏差及 Appendix S 的缓解结果。

---

## 小问题（不影响接收）

- **术语精度**：Section 3.3 声明 "We use 'entropy' as shorthand for token-level NLL"。严格来说 entropy ≠ NLL（entropy 是分布属性，NLL 是单点损失），虽然在 LM 上下文中常互换使用，但在论文中明确等同可能引起审稿人质疑。建议改用 "token-level NLL (which we term entropy for brevity)" 或直接使用 NLL。
- **Table 1 可读性**：8 generators × 多列指标，字体较小。可考虑分组或高亮关键对比。
- **Appendix 编号**：从 A 到 Z.6，共 26+ 个附录，编号方案在 Z 之后使用 Z.1-Z.6 子编号，略显不规范。

---

## Questions（需要作者回答）

**Q1**: Shape stability (entropy_max, tail_decay 的近稳态) 是否在 greedy decoding 或 top-k sampling 下同样成立？如果仅在 nucleus sampling 下成立，如何论证这不是 sampling truncation 的 trivial 推论？

**Q2**: Downstream null result (Appendix M) 表明 depth-aware curation ≈ random subsampling。在什么条件下作者预期 depth signal 能转化为实际 downstream benefit？是否有初步证据？

**Q3**: 论文 claim "proof-of-concept" 定位（Section 1, p.2），但 Contribution 列表中的第 4 条（"drifting and stationary features together yield cross-model cross-generator performance"）读起来像是一个较强的 generalization claim。如何调和这两者？

**Q4**: Appendix K 显示 instruction-tuned models 的 DDR structure 被压缩但未消除。作者是否尝试过在 instruction-tuned chain 上重新训练分类器（而非用 base-model 训练的分类器直接迁移）？这可能显著改善 instruction-tuned 场景下的性能。

**Q5**: 为什么选择 continuation chain（无语义保持约束）而非 paraphrase chain 作为研究对象？Paraphrase chain 在实际场景中更常见（如 AI rewriting tools），且与 Broken Telephone 有更直接的对比价值。

---

## Missing References

引用整体覆盖面较好（66 entries, 0 orphans, 0 missing bib）。以下是可能值得补充的工作：

1. **Tulchinskii et al. (2024)** "Intrinsic Dimension Estimation for Robust Detection of AI-Generated Texts" (ICLR 2024) — 使用几何/拓扑特征检测 AI 文本，与本文的统计特征方法互补，可在 Related Work 2.1 中讨论。
2. **RADAR (Hu et al., 2023)** "RADAR: Robust AI-Text Detection via Adversarial Learning" — 训练式 detector baseline，可补充到 Section 4.3 的 baseline comparison 讨论中。
3. **Decoding strategy 对文本统计特性的影响** — 如果存在研究不同 decoding strategy 对 token-level NLL distribution shape 影响的工作，应当引用以支撑或反驳 shape stability 的 nucleus-sampling-specific 解释。

引用验证工具发现 5 个 first-author mismatch（cohen1988statistical, self_consuming_mad, qwen3, gutierrez_ordinal_survey, llama3），大多为 API 匹配问题（团队作者、LaTeX 编码），非实质性错误。6 个 "not_found"（detectgpt, reliable_detection, detection_possibilities, aaronson_watermark, pythia, xgboost）均为知名论文，属于 OpenAlex 索引覆盖不全。

---

## 主要优势

1. **Task formulation 有价值**：从 binary detection 到 ordinal depth classification 是一个自然且有意义的延伸，定义清晰（Section 3.1）。
2. **实验设计严谨**：LOGO cross-validation 避免 generator leakage，shared seeds 控制 input content，TOST equivalence testing 处理 null result，Bonferroni correction 处理多重比较——统计方法论水准高于多数 detection 论文。
3. **诚实的 proof-of-concept 定位**：论文没有过度宣传分类性能，明确承认范围限制，这在当前 AI detection 文献中难能可贵。
4. **附录极其详尽**：24 页附录覆盖了几乎所有可预见的 reviewer 问题（cross-domain, instruction-tuning, perturbation robustness, feature ablation, error analysis, downstream utility）。
5. **引用规范**：66 条引用全部被使用，无 orphan 无 phantom，覆盖 2019-2026 文献，包括最新 arXiv preprint。
6. **DDR 分解的可解释性**：location vs. shape 的二元分解提供了一个简洁的 mental model，比纯 black-box detection 更有解释价值。

---

## Framing 一致性评估

- **Abstract vs Results 一致性**：基本一致。Abstract 声称的 "binary F1 = 0.694" 和 "leak-free" 定义在 Section 4.1 中有明确解释。τ ≤ 0.7 的范围限定在 Abstract 中标注。
- **Proof-of-concept 贯穿度**：Section 1 (p.2) 明确声称 "proof of concept"，Section 5 和 6 基本保持一致。但 Contribution 第 4 条的措辞略有越界。
- **Scope 标注一致性**：Abstract 和 Limitations 均注明 base-model only，但 Introduction 的开头语 ("When LLM outputs re-enter generation pipelines") 暗示更广泛的适用范围。Section 5 Discussion (p.8) 才提到 instruction-tuning 限制，但已经是结尾部分。建议在 Introduction 第一段就明确 scope。

---

## 总结

这是一篇在实验执行和统计方法上高于平均水准的 empirical study，DDR 分解的角度有一定新意。但核心贡献的新颖性相对于 model collapse 和 iterative generation 文献是增量的，base-model-only 的范围限制和 downstream null result 削弱了实际影响力。如果能（1）在不同 decoding 策略下验证 shape stability 的非 trivial 性，（2）解决页数超限问题，（3）更好地界定与现有工作的增量边界，本文有潜力成为一篇合格的 Findings 论文。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 2744 · 2026-05-21T03:45:22.358357+00:00_

Reviewer 2 审稿意见已收到。等待 Reviewer 1 提交后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director"
}
```

</details>

---


## Round 241

## Round 241

2 recorded events


### User

_source line 2745 · 2026-05-21T03:45:28.993989+00:00_

[Reviewer 2 审稿结果]:
审稿完成，已提交给 Review Director。

**审稿结论**：Overall 3.0（Findings 水平）

**两个 Critical 问题**：
1. 主文约 8.5-8.7 页，超过 EMNLP 8 页严格限制
2. DDR 核心贡献（shape stability）可能是 nucleus sampling 固定 p=0.9 的 trivial 推论，与 model collapse 文献的区分度不足

**三个 Major 问题**：downstream null result 讨论不充分、base-model-only 范围限制实际适用性、3-class 粒度的实际价值未论证

**主要优势**：实验设计严谨（LOGO CV、TOST equivalence testing）、诚实的 proof-of-concept 定位、24 页详尽附录、引用规范（66 entries 零 orphan）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 2746 · 2026-05-21T03:45:35.299643+00:00_

Reviewer 2 意见已收到。等待 Reviewer 1 完成初审后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director"
}
```

</details>

---


## Round 242

## Round 242

6 recorded events


### User

_source line 2747 · 2026-05-21T03:46:50.982942+00:00_

[Reviewer 1 审稿意见]:

# Reviewer 1 审稿意见 — Depth Fingerprinting (方法严谨性审查)

## 总体评分
**Overall**: 3.5 (Borderline Conference)
**一句话总结**: 论文提出"深度指纹"这一新颖检测范式，DDR 分析框架有概念贡献，实验覆盖面广且附录详尽（34 页中 24 页附录）；但核心统计框架存在多处方法论短板——7 特征上的 k=2 聚类统计效力不足、TOST 等价性检验 tail_decay 仅 4/8 generator 通过、排列检验仅边际显著 (p=0.030)、ε=0.20 缺乏问题特定正当性——不足以支撑其较强的方法论声明。加之仅评估 base model、instruction-tuned 模型退化严重却仅放附录，限制了实际影响力。

## 官方维度打分（来自 ACL ARR review form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3/5 | DDR 核心声明的统计支撑偏弱；分类实验设计合理但 generator-level 方差被 bootstrap CI 低估 |
| Excitement | 3.5/5 | 深度检测作为新任务有创新性；location/shape 分解有洞察力；但 base-model-only 评估和简单特征集限制影响 |
| Reproducibility | 4/5 | 超参数、数据集构建、评估协议记录详细；承诺代码/数据发布 |
| Overall Assessment | 3.5 | Borderline Conference |
| Reviewer Confidence | 4/5 | 熟悉统计检验方法、NLP 检测方法论、实验设计 |

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] DDR 分区的核心统计基础不够稳固：k=2 聚类在 n=7 特征点上缺乏统计效力

- **具体位置**：Section 4.2 / Appendix V (Table 28)
- **问题**：DDR 框架的核心声明——7 个特征自然分成 drifting vs. near-stationary 两组——依赖 k-means 在 7 个数据点（7 个特征的 (μ, d) 坐标）上的聚类（silhouette = 0.660）。n=7 的 k-means 本质上是描述性的而非推断性的：C(7,2)+C(7,3)=56 种可能的 2-划分中，获得较高 silhouette 并不罕见。排列检验 p=0.030 仅边际显著（<0.05 但远非 <0.01）。论文提供了 holdout generator split 验证（Appendix V, Table 31）和 partition stability（Table 30）作为补充证据，但这些仍是描述性的，不构成严格的推断性检验。
- **为什么影响接收**：DDR 分区是论文方法论框架的基石——后续的特征选择逻辑、分类器设计、"drifting vs. stationary" 叙事都建立在此分区之上。如果分区缺乏统计支撑，整个分析框架的 validity 受到质疑。
- **建议修改方向**：(1) 补充 sample-level bootstrap：对 N=37K 样本做 bootstrap resampling，重新计算每次 resample 的 (μ, d)，检验聚类标签在样本扰动下的稳定性；(2) 用 gap statistic 或 prediction strength 替代 silhouette 评估聚类有效性；(3) 对排列检验做 power analysis，报告检测给定 effect size 的统计功效。

**N2** [critical] TOST 等价性检验中 tail_decay 仅 4/8 generator 通过——"near-stationary" 分类名不副实

- **具体位置**：Section 4.2 / Appendix U (Table 26, Table 29)
- **问题**：论文将 tail_decay 归为"near-stationary"特征（|d| < 0.10），但 TOST 等价性检验（ε = 0.20）仅在 4/8 generator 上拒绝非等价假设（Table 26 的 ✗ 标记）。这意味着对一半的 generator，tail_decay 的代际变化实际上超过了 "small effect" 阈值。同时，Granger causality（Table 39, p = 0.375）和 permutation importance（Table 38, tail_decay rank 7/7）均显示 tail_decay 对深度预测几乎无贡献——这与 TOST 50% 失败率一致，但从另一面说明该特征实际上并非"near-stationary"而是"noisy/inconsistent"。论文在 Appendix U 标记了问题但主文中几乎未讨论。
- **为什么影响接收**：如果 3 个 "near-stationary" 特征中有 1 个实际并不稳定，DDR 的三分区（drifting / intermediate / near-stationary）的清晰性被削弱。论文叙事中 "shape features remain flat" 的核心主张过于绝对。
- **建议修改方向**：(1) 在主文中明确将 tail_decay 重分类为 "weakly stationary" 或 "inconsistent across generators"，与 entropy_max、entropy_min 区分；(2) 补充 sensitivity analysis：移除 tail_decay 后分类性能和 DDR 分区是否变化；(3) 在 Figure 2 的 DDR 图中为 tail_decay 使用不同标记以反映其边界地位。

**N3** [critical] ε = 0.20 等价阈值缺乏问题特定的正当性——存在循环论证风险

- **具体位置**：Section 4.2 / Appendix U / Appendix V (Table 30)
- **问题**：TOST 使用 ε = 0.20（Cohen's d "small effect" 阈值，Cohen 1988）作为等价边界。这是行为科学的通用惯例，但论文未论证为什么在 "生成深度检测" 这个特定问题中 0.20 是合理的。Table 30 显示：当 ε 收紧至 0.10 时，entropy_std 从 intermediate 变为 stationary 分类；当 ε 放宽至 0.25 时，分区更稳固。这表明分区结果在一定程度上是阈值选择的函数而非纯数据驱动。论文虽在 Appendix V 展示了多阈值 sensitivity，但未从 downstream task 角度给出 ε 的独立正当性。
- **为什么影响接收**：等价性检验的核心在于 ε 必须有先验的、独立于数据的正当性。当阈值选择影响结论时，这构成方法论循环。审稿人和读者无法判断 DDR 分区反映的是数据的内在结构还是研究者的阈值偏好。
- **建议修改方向**：(1) 从下游任务角度论证 ε——例如 "d < 0.20 对应的分类 F1 影响 < X pp，因此实践中可忽略"；(2) 绘制 equivalence frontier 图，展示分区在 ε ∈ [0.05, 0.50] 连续变化时的稳定区间；(3) 引入 smallest effect size of interest (SESOI) 框架，使 ε 的选择可审计。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [major] 仅评估 base model，instruction-tuned 模型结果显著退化但放在附录

- **具体位置**：Appendix K / Limitations (Section 9)
- **问题**：主实验使用 8 个 base model generator，但真实世界 LLM 输出主要来自 instruction-tuned 模型。Appendix K 显示 instruction tuning 后 3-class F1 从 0.754 降至 0.575（OLMo-2-1B）和 0.544（Llama-3.2-3B），降幅 17-21pp。DDR 分区的 silhouette 从 0.660 降至 0.372，drifting/near-stationary 分离被大幅压缩（Figure 7）。这一结果对论文的实际适用性构成重大限制，但主文仅在 Limitations 中一笔带过（"eight generators are base (pretrained) models"）。
- **建议**：(1) 在主文 Section 4 或 Section 5 中用至少一段讨论 instruct 模型退化及其机制解释；(2) 考虑在 Table 1 中包含 1-2 个 instruct 模型结果以呈现完整图景。

**W2** [major] QLoRA +11.6pp 改进的基线比较存在跨子集不一致

- **具体位置**：Appendix E (Table 6) / Section 5
- **问题**：Appendix E 声称 QLoRA 相比 XGBoost 有 +11.6pp binary F1 改进，但该比较基于 **6-generator 子集**（XGBoost baseline = 0.789，脚注说明），而主文 Table 1 的 **8-generator LOGO** binary F1 = 0.694。两个基线相差 9.5pp。读者容易将 "+11.6pp" 误解为相对于 Table 1 主结果的提升。Discussion (§5) 中引用 "QLoRA recovers 0.905" 时也未标注是 6-gen 结果。
- **建议**：(1) 在 Appendix E 和 Discussion 中每次提及 QLoRA 结果时明确标注 "(6-gen subset)"；(2) 补报 8-gen LOGO 下 QLoRA 结果作为直接可比较的数据点；(3) 避免在 Discussion 中用跨子集 delta 做总结性声明。

**W3** [major] Bootstrap CI 未能捕获 generator-level 方差

- **具体位置**：Table 1 / Section 4.1
- **问题**：Table 1 报告 8-gen LOGO macro F1 = 0.762，95% CI [0.738, 0.786]，宽度仅 4.8pp。但 per-generator binary F1 的 range 达 28.8pp（Qwen3-1.7B: 0.536 至 Pythia-2.8B: 0.824）。Bootstrap CI 仅捕获 sample-level 重采样不确定性，不反映 generator-level 变异——后者是实际部署中的主要不确定性来源。此外，Pythia 系列 F1 系统性高于其他 family（0.742-0.824 vs 0.536-0.738），可能反映 Pythia-410M 参考模型的 same-family 优势而非 depth signal 本身。
- **建议**：(1) 补充 generator-level variance 统计量（如 across-generator SD）与 bootstrap CI 并列报告；(2) 讨论 same-family reference bias 对 Pythia generator 的影响；(3) 考虑 hierarchical bootstrap 来同时建模两层不确定性。

**W4** [minor] 五种 effect-size measures 的 "complementarity" 未验证

- **具体位置**：Section 4.2 (abstract 和正文均声称 "five complementary effect-size measures")
- **问题**：Cohen's d 和 Glass's Δ 在组间方差接近时高度相关（数学上 Glass's Δ = Cohen's d × SD_pooled/SD_control）。KS 统计量虽测量分布差异，但在 location shift 主导时与 Cohen's d 也强相关。五个指标可能本质上测量相同底层量——"五重验证"会过度膨胀置信度。
- **建议**：(1) 报告五个 measures 之间的 inter-measure 相关矩阵；(2) 或精简为 "一个 parametric (Cohen's d) + 一个 rank-based (Cliff's δ) + 一个 distributional (KS)" 的组合，明确承认冗余。

**W5** [minor] 温度/prompt 泛化测试覆盖度有限

- **具体位置**：Appendix C (3 种 prompt type) / Appendix I (Table 10, 3 个温度点)
- **问题**：温度泛化仅涵盖 t ∈ {0.5, 0.7, 0.9}，高温 (t=0.9) 导致 binary F1 下降 9.3-26.0pp，但很多 deployment 使用 t=1.0。Prompt 泛化仅测试 3 种 continuation 变体，缺少 QA、summarization、instruction-following 等更现实的 prompt 类型。
- **建议**：补充 t=1.0 和至少 2 种非 continuation prompt 类型的结果。

---

## 小问题（不影响接收）

1. Table 1 中 "LOGO family-level" 行的定义不清——LOGO 是 per-generator 还是 per-family leave-one-out？主文 §3.4 说 "LOGO holds out individual generators"，但 "family-level" 暗示按 family 分组。需澄清。
2. Figure 1 strip plot 的纵轴标签字号偏小，建议增大以提高可读性。
3. 引用验证结果：66 条 bib entry 中 55 条 verified，6 条 not_found（含 DetectGPT、Pythia、XGBoost 等高知名度论文，应为 OpenAlex 索引问题），5 条 mismatch 均为 first_author 编码差异（如 bib 用 "Team" 而 API 返回具体作者名），无实质性错误。所有 cited key 均在 bib 中找到，无 orphan 或 missing。引用质量良好。
4. Appendix 极为丰富（A-Z.6，24 页）但缺少一个总索引/目录，读者难以快速定位特定补充实验。

---

## Questions（需要作者回答）

**Q1. DDR 分区的 falsifiability**：如果增加更多特征（如 n-gram diversity、句法复杂度、discourse coherence），DDR 的 drifting/near-stationary 二分是否仍然成立？目前 7 个特征中 5 个基于 token-level NLL，特征空间的局限性是否预设了分区结果？

**Q2. TOST ε 的 downstream justification**：是否尝试过从分类任务角度反推 ε——例如，在多大的 d 值以下，该特征对分类 F1 的边际贡献低于 1pp？

**Q3. Instruction-tuned 模型的 DDR 压缩机制**：Appendix K 显示 instruct 模型下 silhouette 从 0.660 降至 0.372——这是否意味着 instruction tuning 从根本上改变了生成文本的分布动态，使得 DDR 框架的 "drifting/stationary 分离" 前提不再成立？

**Q4. Reference model 尺度效应**：所有 NLL 特征依赖 Pythia-410M 作为参考模型。Appendix S 仅测试了 ≤1B 替代参考。使用 2.8B 或 7B 参考模型是否会改变特征判别力和 DDR 分区？

**Q5. Pythia same-family 优势**：Table 1 中 Pythia generators 的 F1 系统性高于其他 family（Pythia-2.8B: 0.824 vs Qwen3-1.7B: 0.536）。在使用 Pythia-410M 参考模型计算 NLL 的情况下，这一差异在多大程度上反映 same-family architectural affinity 而非 depth signal？Cross-family reference 实验（Appendix S）的 spread 仅 0.013——但该数据是 pooled across generators，能否分 generator 报告 reference model 切换的影响？

---

## Missing References

1. **Tulchinskii et al. (2024) "Intrinsic Dimension Estimation for Robust Detection of AI-Generated Texts"** (ICLR 2024) — 使用内在维度作为检测特征，与本文的 distributional statistics 方法有直接对比价值。
2. 代码域检测工作（论文 Appendix J 测试了 Code 域但 Related Work 未引用代码域检测先前工作）。
3. **Xu et al. (2024) "DNA-GPT" 之外的 perturbation-based 检测**（如 Re-Detect 系列），可补充 Section 2.1 的覆盖面。

---

## 主要优势

1. **新颖的问题定义**：将 AI 文本检测从二分类扩展到序数深度估计，在 data provenance 和 model collapse 预防中有清晰的应用场景。"知道递归了多少次" 比 "是否为 AI 生成" 提供了更丰富的信号。

2. **DDR 概念有洞察力**：location/shape 分离——drifting features（entropy mean, TTR, hapax_ratio）单调漂移而 shape features（entropy_max, tail_decay, entropy_min）近似不变——是一个有趣的实证发现。即使统计验证需要加强，这个 decomposition 本身为理解 LLM 生成文本的分布演化提供了新视角。

3. **实验覆盖面极广、问题预判到位**：17+ 项补充实验（TOST、LOFO、cross-domain、temperature、prompt type、instruction tuning、QLoRA、Granger causality、cross-generator transfer、perturbation robustness 等）系统性地回答了大部分可预见的 reviewer 质疑。即使个别实验的统计细节有待改进，整体的实验工程量和诚实度是值得肯定的。

4. **泄露控制设计合理**：gen-0 种子共享的潜在泄露通过三重机制验证——leak-free binary F1（排除 gen-0）、seed-level demeaning（F1=0.701）、independent-seed control（F1=0.688）——差距仅 0.6pp，令人信服。

5. **与检测 baseline 的公平对比**：Table 2 使用相同 XGBoost pipeline 和 LOGO 协议对比 Avg-LogProb、FastDetectGPT、LD-Score、Binoculars 四种方法，确保了方法论层面的公平性。7-feature ensemble 在所有条件下均优于单特征 baseline。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 2748 · 2026-05-21T03:47:25.985002+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "text": "以下是 Reviewer 2 的完整审稿意见，请逐条回应。对每个 Must-Fix 和 Should-Fix 问题，请标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n# Reviewer 2 审稿意见（新颖性与完整性）\n\n**Overall**: 3.0 (Findings)\n\n## Must-Fix 问题\n\n**N1** [critical] 主文页数可能超过 8 页限制\n- Page 9 — Section 6 (Conclusion) 结束于约页面 75% 处，Limitations 从该处开始\n- 从 Page 1 到 Section 6 Conclusion 结束，主文约占 8.5–8.7 页\n- Discussion 独占整个 Page 8 并延续至 Page 9 上部约 1/3，然后 Conclusion 再占约 1/3\n- 格式违规是 desk reject 的直接原因\n\n**N2** [critical] DDR 与 model collapse / diversity loss 的区分度不足\n- DDR 的三个 drifting 特征本质上就是 model collapse 文献中反复记录的 diversity loss / entropy erosion\n- Shape stability 是否只是 nucleus sampling 在固定 p=0.9 下的 trivial 推论？\n- 缺少不同解码策略（greedy, top-k, temperature-only）下 shape stability 验证\n- 如果只在 nucleus sampling 下成立，这更像是 sampling 机制的已知属性\n\n## Should-Fix 问题\n\n**W1** [major] Downstream null result 在主文中讨论不充分\n- Appendix M 的 TOST 显示 depth-aware curation ≈ random subsampling\n- Discussion 只用一句带过\n\n**W2** [major] Base-model-only 范围严重限制实际适用性\n- Appendix K 显示 instruction-tuned F1 降 17-21pp\n- Abstract/Introduction 措辞暗示更广泛适用性\n\n**W3** [major] 3-class 粒度的实际价值论证不足\n- 3-class vs binary 的增量价值未有令人信服的 use case\n\n**W4** [minor-major] 前 3.5 页无任何图表，信息密度不均\n\n**W5** [minor] Reference model (Pythia-410M) 选择的 confound 讨论不足\n\n## Questions\nQ1: Shape stability 是否在 greedy/top-k 下同样成立？\nQ2: 什么条件下 depth signal 能转化为 downstream benefit？\nQ3: Proof-of-concept 定位与 Contribution 列表第 4 条的 generalization claim 如何调和？\nQ4: 是否尝试过在 instruction-tuned chain 上重新训练分类器？\nQ5: 为什么选 continuation chain 而非 paraphrase chain？\n\n## Missing References\n1. Tulchinskii et al. (2024) \"Intrinsic Dimension Estimation\" (ICLR 2024)\n2. RADAR (Hu et al., 2023)\n3. Decoding strategy 对 NLL distribution shape 影响的相关工作\n\n## 主要优势\n1. Task formulation 有价值\n2. 实验设计严谨（LOGO CV, TOST, Bonferroni）\n3. 诚实的 proof-of-concept 定位\n4. 附录极其详尽\n5. 引用规范\n6. DDR 分解的可解释性\n\n---\n\n请逐条回应上述意见。",
  "reviewer_id": "1",
  "project": "gen-depth-fingerprint",
  "round_number": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "text": "以下是 Reviewer 2 的完整审稿意见，请逐条回应。对每个 Must-Fix 和 Should-Fix 问题，请标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n# Reviewer 2 审稿意见（新颖性与完整性）\n\n**Overall**: 3.0 (Findings)\n\n## Must-Fix 问题\n\n**N1** [critical] 主文页数可能超过 8 页限制\n- Page 9 — Section 6 (Conclusion) 结束于约页面 75% 处，Limitations 从该处开始\n- 从 Page 1 到 Section 6 Conclusion 结束，主文约占 8.5–8.7 页\n- Discussion 独占整个 Page 8 并延续至 Page 9 上部约 1/3，然后 Conclusion 再占约 1/3\n- 格式违规是 desk reject 的直接原因\n\n**N2** [critical] DDR 与 model collapse / diversity loss 的区分度不足\n- DDR 的三个 drifting 特征本质上就是 model collapse 文献中反复记录的 diversity loss / entropy erosion\n- Shape stability 是否只是 nucleus sampling 在固定 p=0.9 下的 trivial 推论？\n- 缺少不同解码策略（greedy, top-k, temperature-only）下 shape stability 验证\n- 如果只在 nucleus sampling 下成立，这更像是 sampling 机制的已知属性\n\n## Should-Fix 问题\n\n**W1** [major] Downstream null result 在主文中讨论不充分\n- Appendix M 的 TOST 显示 depth-aware curation ≈ random subsampling\n- Discussion 只用一句带过\n\n**W2** [major] Base-model-only 范围严重限制实际适用性\n- Appendix K 显示 instruction-tuned F1 降 17-21pp\n- Abstract/Introduction 措辞暗示更广泛适用性\n\n**W3** [major] 3-class 粒度的实际价值论证不足\n- 3-class vs binary 的增量价值未有令人信服的 use case\n\n**W4** [minor-major] 前 3.5 页无任何图表，信息密度不均\n\n**W5** [minor] Reference model (Pythia-410M) 选择的 confound 讨论不足\n\n## Questions\nQ1: Shape stability 是否在 greedy/top-k 下同样成立？\nQ2: 什么条件下 depth signal 能转化为 downstream benefit？\nQ3: Proof-of-concept 定位与 Contribution 列表第 4 条的 generalization claim 如何调和？\nQ4: 是否尝试过在 instruction-tuned chain 上重新训练分类器？\nQ5: 为什么选 continuation chain 而非 paraphrase chain？\n\n## Missing References\n1. Tulchinskii et al. (2024) \"Intrinsic Dimension Estimation\" (ICLR 2024)\n2. RADAR (Hu et al., 2023)\n3. Decoding strategy 对 NLL distribution shape 影响的相关工作\n\n## 主要优势\n1. Task formulation 有价值\n2. 实验设计严谨（LOGO CV, TOST, Bonferroni）\n3. 诚实的 proof-of-concept 定位\n4. 附录极其详尽\n5. 引用规范\n6. DDR 分解的可解释性\n\n---\n\n请逐条回应上述意见。",
    "reviewer_id": "1",
    "project": "gen-depth-fingerprint",
    "round_number": "1"
  }
}
```

</details>

---


### Tool result

_source line 2749 · 2026-05-21T03:47:43.031251+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 17046
}
```

</details>

---


### Tool call

_source line 2750 · 2026-05-21T03:47:44.486409+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "text": "以下是 Reviewer 1 的完整审稿意见，请逐条回应。对每个 Must-Fix 和 Should-Fix 问题，请标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n# Reviewer 1 审稿意见（方法严谨性）\n\n**Overall**: 3.5 (Borderline Conference)\n\n## Must-Fix 问题\n\n**N1** [critical] k=2 聚类在 n=7 特征点上缺乏统计效力\n- n=7 的 k-means 本质上是描述性的而非推断性的\n- 排列检验 p=0.030 仅边际显著\n- generator-split 验证和 partition stability 仍是描述性的\n- 建议补充 sample-level bootstrap、gap statistic、power analysis\n\n**N2** [critical] TOST 中 tail_decay 仅 4/8 generator 通过——\"near-stationary\" 名不副实\n- tail_decay 的 Granger causality (p=0.375) 和 permutation importance (rank 7/7) 均显示无贡献\n- 3 个 near-stationary 特征中 1 个实际不稳定，削弱 DDR 三分区清晰性\n- 建议重分类为 \"weakly stationary\" 或 \"inconsistent\"\n\n**N3** [critical] ε=0.20 等价阈值缺乏问题特定正当性——存在循环论证风险\n- Cohen 的通用惯例未必适用于生成深度检测\n- Table 30 显示分区结果是阈值选择的函数\n- 建议从 downstream task 角度给出独立正当性\n\n## Should-Fix 问题\n\n**W1** [major] 仅评估 base model，instruction-tuned 结果显著退化但放附录\n- 3-class F1 从 0.754 降至 0.575 (OLMo) / 0.544 (Llama)\n- DDR silhouette 从 0.660 降至 0.372\n\n**W2** [major] QLoRA +11.6pp 基线比较存在跨子集不一致\n- 基于 6-gen 子集的 XGBoost baseline = 0.789\n- 主文 Table 1 的 8-gen LOGO binary F1 = 0.694\n- 读者容易将 \"+11.6pp\" 误解为相对于主结果的提升\n\n**W3** [major] Bootstrap CI 未能捕获 generator-level 方差\n- per-generator binary F1 range 达 28.8pp\n- Pythia 系列系统性高于其他 family，可能反映 same-family reference bias\n\n**W4** [minor] 五种 effect-size measures 的 \"complementarity\" 未验证\n- Cohen's d 和 Glass's Δ 高度相关\n- \"五重验证\" 可能过度膨胀置信度\n\n**W5** [minor] 温度/prompt 泛化测试覆盖度有限\n- 仅 3 个温度点，缺 t=1.0\n- 仅 3 种 continuation 变体，缺 QA/summarization 等\n\n## Questions\nQ1: 增加更多特征后 DDR 二分是否仍成立？\nQ2: 是否尝试从分类 F1 角度反推 ε？\nQ3: Instruction-tuned 下 silhouette 降至 0.372，DDR 框架前提是否不再成立？\nQ4: 使用 2.8B/7B 参考模型是否改变 DDR 分区？\nQ5: Pythia same-family 优势在多大程度上反映 architectural affinity？\n\n## Missing References\n1. Tulchinskii et al. (2024) \"Intrinsic Dimension Estimation\" (ICLR 2024)\n2. 代码域检测先前工作\n3. Re-Detect 系列 perturbation-based 检测\n\n## 主要优势\n1. 新颖的问题定义\n2. DDR 概念有洞察力\n3. 实验覆盖面极广\n4. 泄露控制设计合理\n5. 与检测 baseline 的公平对比\n\n---\n\n请逐条回应上述意见。",
  "reviewer_id": "2",
  "project": "gen-depth-fingerprint",
  "round_number": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "text": "以下是 Reviewer 1 的完整审稿意见，请逐条回应。对每个 Must-Fix 和 Should-Fix 问题，请标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n# Reviewer 1 审稿意见（方法严谨性）\n\n**Overall**: 3.5 (Borderline Conference)\n\n## Must-Fix 问题\n\n**N1** [critical] k=2 聚类在 n=7 特征点上缺乏统计效力\n- n=7 的 k-means 本质上是描述性的而非推断性的\n- 排列检验 p=0.030 仅边际显著\n- generator-split 验证和 partition stability 仍是描述性的\n- 建议补充 sample-level bootstrap、gap statistic、power analysis\n\n**N2** [critical] TOST 中 tail_decay 仅 4/8 generator 通过——\"near-stationary\" 名不副实\n- tail_decay 的 Granger causality (p=0.375) 和 permutation importance (rank 7/7) 均显示无贡献\n- 3 个 near-stationary 特征中 1 个实际不稳定，削弱 DDR 三分区清晰性\n- 建议重分类为 \"weakly stationary\" 或 \"inconsistent\"\n\n**N3** [critical] ε=0.20 等价阈值缺乏问题特定正当性——存在循环论证风险\n- Cohen 的通用惯例未必适用于生成深度检测\n- Table 30 显示分区结果是阈值选择的函数\n- 建议从 downstream task 角度给出独立正当性\n\n## Should-Fix 问题\n\n**W1** [major] 仅评估 base model，instruction-tuned 结果显著退化但放附录\n- 3-class F1 从 0.754 降至 0.575 (OLMo) / 0.544 (Llama)\n- DDR silhouette 从 0.660 降至 0.372\n\n**W2** [major] QLoRA +11.6pp 基线比较存在跨子集不一致\n- 基于 6-gen 子集的 XGBoost baseline = 0.789\n- 主文 Table 1 的 8-gen LOGO binary F1 = 0.694\n- 读者容易将 \"+11.6pp\" 误解为相对于主结果的提升\n\n**W3** [major] Bootstrap CI 未能捕获 generator-level 方差\n- per-generator binary F1 range 达 28.8pp\n- Pythia 系列系统性高于其他 family，可能反映 same-family reference bias\n\n**W4** [minor] 五种 effect-size measures 的 \"complementarity\" 未验证\n- Cohen's d 和 Glass's Δ 高度相关\n- \"五重验证\" 可能过度膨胀置信度\n\n**W5** [minor] 温度/prompt 泛化测试覆盖度有限\n- 仅 3 个温度点，缺 t=1.0\n- 仅 3 种 continuation 变体，缺 QA/summarization 等\n\n## Questions\nQ1: 增加更多特征后 DDR 二分是否仍成立？\nQ2: 是否尝试从分类 F1 角度反推 ε？\nQ3: Instruction-tuned 下 silhouette 降至 0.372，DDR 框架前提是否不再成立？\nQ4: 使用 2.8B/7B 参考模型是否改变 DDR 分区？\nQ5: Pythia same-family 优势在多大程度上反映 architectural affinity？\n\n## Missing References\n1. Tulchinskii et al. (2024) \"Intrinsic Dimension Estimation\" (ICLR 2024)\n2. 代码域检测先前工作\n3. Re-Detect 系列 perturbation-based 检测\n\n## 主要优势\n1. 新颖的问题定义\n2. DDR 概念有洞察力\n3. 实验覆盖面极广\n4. 泄露控制设计合理\n5. 与检测 baseline 的公平对比\n\n---\n\n请逐条回应上述意见。",
    "reviewer_id": "2",
    "project": "gen-depth-fingerprint",
    "round_number": "1"
  }
}
```

</details>

---


### Tool result

_source line 2751 · 2026-05-21T03:47:46.099148+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1612
}
```

</details>

---


### Assistant

_source line 2752 · 2026-05-21T03:47:48.595722+00:00_

交叉分享已派发。等待两位 Reviewer 的逐条回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director"
}
```

</details>

---


## Round 243

## Round 243

2 recorded events


### User

_source line 2753 · 2026-05-21T03:47:51.387437+00:00_

[Reviewer 1 审稿结果]:
审稿意见已提交给 Review Director。

**审稿完成摘要**：

- **Overall**: 3.5 (Borderline Conference)
- 识别了 **3 个 Critical 问题**：(1) DDR 分区的 k=2 聚类在 n=7 上统计效力不足且排列检验仅边际显著 (p=0.030)；(2) TOST 等价性检验中 tail_decay 仅 4/8 generator 通过，"near-stationary" 标签过于宽泛；(3) ε=0.20 阈值缺乏问题特定正当性，分区结果受阈值选择影响
- 识别了 **5 个 Should-Fix 问题**：base-model-only 评估、QLoRA 跨子集基线不一致、Bootstrap CI 未捕获 generator-level 方差、5 种 effect-size measures 冗余性、温度/prompt 泛化覆盖不足
- 同时肯定了论文的新颖问题定义、DDR 概念洞察力、极广的实验覆盖面、合理的泄露控制设计

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 2754 · 2026-05-21T03:47:55.741853+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director"
}
```

</details>

---


## Round 244

## Round 244

2 recorded events


### User

_source line 2755 · 2026-05-21T03:52:28.768683+00:00_

[Reviewer 2 审稿意见]:

# Reviewer 2 对 Reviewer 1 审稿意见的逐条回应

---

## Must-Fix 问题

### R1-N1: k=2 聚类在 n=7 特征点上缺乏统计效力

**[AGREE]**（部分同意，严重程度需下调）

R1 正确指出 k-means 在 n=7 上统计效力不足，permutation test p=0.030 仅边际显著。但我认为 R1 低估了论文提供的多重收敛证据：

1. **Generator-split validation**（Appendix V, Table 31, p.28）：将 8 个 generator 分为两组互补 split（A={Pythia-2.8B, Qwen3-1.7B, OLMo, Mistral} vs B={Pythia-1B, Qwen3-0.6B, Qwen3-8B, Llama}），两组独立产生完全相同的 7 特征分区，selection/validation 子集最大 Δ|d| = 0.05。
2. **Holdout split**（Figure 12, p.29）：(|d|, d̄) 空间中 selection/validation 子集的 zone assignment 完全一致。
3. **跨 ε 稳定性**（Table 30, p.28）：drifting/stationary 分区在 ε ∈ [0.10, 0.75] 区间内完全不变，唯一阈值敏感特征是 entropy_std（d ≈ 0.35，在 ε > 0.55 时变为 stationary）。

这些证据链说明 partition 不是 n=7 的统计噪音产物。但我同意 R1 的建议——补充 gap statistic 和 bootstrap 分析会使论证更完整。**建议将严重性从 critical 降为 major**，因为现有 validation 已足以支撑 descriptive claim，只是 inferential rigor 有提升空间。

---

### R1-N2: tail_decay 仅 4/8 generator 通过 TOST——"near-stationary" 名不副实

**[AGREE]**

R1 的事实判断准确。Table 29（p.27）明确显示 tail_decay 在 ε=0.20 下仅 4/8 generator 通过 TOST，是三个 near-stationary 特征中最不稳定的。论文自身也承认 "tail_decay is the most ε-sensitive near-stationary feature"（p.27）。

补充两点：
1. 论文提供了部分缓解证据：非通过的 4 个 generator 的 |d| = 0.15–0.22（p.27），远低于 drifting 阈值（>0.50），说明 tail_decay 虽未通过严格 near-stationary 判定，但也不属于 drifting。
2. Permutation importance 中 tail_decay 排名 7/7（最低），Granger causality p=0.375——这些证据进一步证实它对分类的贡献微乎其微。

R1 建议重分类为 "weakly stationary" 或 "inconsistent" 是合理的。当前三分区（3 drifting / 1 intermediate / 3 near-stationary）中有 1 个 near-stationary 实际表现不稳定，确实削弱了 DDR 框架的清晰度。建议作者至少将 tail_decay 单独标注为 "weakly stationary" 并在主文讨论其异质性。

---

### R1-N3: ε=0.20 等价阈值缺乏问题特定正当性——循环论证风险

**[REBUT]**（部分反驳）

R1 关于 ε 选择的问题方向是对的——domain-specific justification 优于通用惯例。但 **"循环论证"** 的判断过重，原因如下：

1. **Table 30（p.28）直接反驳阈值敏感性**：drifting/stationary 分区在 ε ∈ [0.10, 0.75] 内完全不变。3 个 drifting 特征（pooled d = 0.68–1.17）和 2 个 near-stationary 特征（entropy_max, entropy_min, pooled d = 0.08）的分类在任何合理 ε 下都不会改变。唯一的阈值敏感点是 entropy_std（d ≈ 0.35），且论文已将其归为 "intermediate"。因此，"分区结果是阈值选择的函数" 这一表述不适用于核心分区——它只适用于 entropy_std 的归属。
2. **Cohen's d = 0.20 是被广泛接受的 "small effect" 标准**（Cohen, 1988），不是作者自创的阈值。论文引用了这一来源（p.27）。
3. 但我同意，从 downstream task 反推 ε 会更有说服力（如 R1-Q2 所建议的：从分类 F1 角度确定 "可忽略效应" 的操作定义）。

**建议从 critical 降为 major**：ε=0.20 的选择有合理依据，分区对 ε 高度稳定，但补充 task-specific justification 确实能加强论证。

---

## Should-Fix 问题

### R1-W1: 仅评估 base model，instruction-tuned 结果放附录

**[AGREE]**

完全同意。这与我自己审稿意见中的 W2 一致。Appendix K（p.20-21）的关键数据（3-class F1 降至 0.575/0.544, silhouette 从 0.660 降至 0.372）应在主文 Discussion 中获得更显著的讨论空间，因为这直接关系到方法的实际部署前景。

---

### R1-W2: QLoRA +11.6pp 基线比较存在跨子集不一致

**[AGREE]**

R1 准确识别了一个容易误导读者的表述问题。6-gen 子集的 XGBoost baseline F1 = 0.789（Appendix E, p.16）vs 主文 Table 1 的 8-gen LOGO binary F1 = 0.694——这两个数字出现在不同上下文中，但 "+11.6pp" 的表述容易被误读为相对于主结果的提升。建议在 Appendix E 中明确标注 "This comparison uses the 6-generator subset where QLoRA features are available; the XGBoost baseline on this subset is 0.789, not the 8-generator LOGO result of 0.694 reported in Table 1."

---

### R1-W3: Bootstrap CI 未能捕获 generator-level 方差

**[AGREE]**

Per-generator binary F1 range 达 28.8pp（Table 1, p.5：从 Mistral-7B 的 0.633 到 Pythia-2.8B 的 0.724），这一异质性确实未被 aggregate bootstrap CI 充分反映。Pythia 系列系统性高于其他 family（Pythia-2.8B: 0.724, Pythia-1B: 0.690 vs OLMo: 0.649, Llama: 0.675），与 Pythia-410M reference model 的同家族亲和性吻合（论文在 p.5 主文和 Appendix S 都承认 "same-family affinity"）。

Appendix S（p.26）通过 cross-family reference models（OLMo-2 1B, Qwen3-0.6B）验证信号保持（F1 spread 0.013），这是有效的缓解措施。但主文的 CI 报告应补充 generator-level variance 的量化，例如 per-generator F1 的 IQR 或 SD。

---

### R1-W4: 五种 effect-size measures 的 "complementarity" 未验证

**[AGREE]**（部分同意）

R1 的核心观察正确：Cohen's d 和 Glass's Δ 共享相同的分子（均差），仅分母不同（pooled SD vs single-group SD），在方差相近时高度相关。"五重验证" 的措辞确实可能过度膨胀置信度。

但需要指出，这五种 measure 并非完全冗余：
- Cohen's d / Glass's Δ → 参数化、对称/非对称
- Cliff's δ → 非参数、序数级别
- KS statistic → 分布级别（非仅均值）
- Pearson correlation → 区间的方向性

它们捕获不同层面的 effect（location shift vs. distributional divergence vs. rank ordering），所以 convergence across all five 确实提供了一些独立信息。建议作者将 "complementarity" 改为 "convergence across parametric and non-parametric measures"，并在 Appendix Q 中补充度量间的相关矩阵。

---

### R1-W5: 温度/prompt 泛化测试覆盖度有限

**[REBUT]**（部分反驳 + 部分同意）

**R1 关于 "缺 t=1.0" 的事实判断有误。** Table 10（Appendix H, p.17）明确列出了 t ∈ {0.5, 0.7, 1.0} 三个温度条件下 4 个 generator（Pythia-2.8B, OLMo-2 1B, Qwen3-1.7B, Qwen3-0.6B）的分类结果。论文文本明确写道 "Degradation onset at t=1.0 defines the practical upper bound"（p.17）。t=1.0 不仅被测试了，而且是分析的关键边界点。

**但我同意 prompt type 覆盖度有限。** Appendix C（p.15）仅测试 3 种 continuation 变体（continuation, elaboration, inspired rewriting），缺少 QA、summarization、translation 等实际场景中更常见的 chain 类型。鉴于论文 scope 是 "continuation chains"，这一限制是设计选择而非遗漏，但应在 Limitations 中更明确地讨论。

另外注意：温度实验仅覆盖 4/8 generator（Table 10），非全部 8 个。这是一个 R1 未提及但值得补充的覆盖度限制。

---

## Questions 回应

### R1-Q1: 增加更多特征后 DDR 二分是否仍成立？

有效问题。当前 7 个特征（全部基于 token-level NLL 和 lexical diversity）是一个狭窄的特征空间。加入 embedding-level 特征（如 intrinsic dimension, sentence-level perplexity）后分区可能更复杂。论文 Appendix Q（p.25）的 feature ablation 显示 surface-only（2 features）和 reference-only（5 features）都独立保持信号，但未测试特征扩展后的分区变化。这是一个合理的 future work 方向。

### R1-Q2: 是否尝试从分类 F1 角度反推 ε？

优秀的建议。例如：找到使 near-stationary 特征被移除后分类 F1 不显著下降的最小 effect size，即 "operationally negligible" 的 ε。这比依赖 Cohen 惯例更有问题特定的正当性。论文未做此分析。

### R1-Q3: Instruction-tuned 下 silhouette 降至 0.372，DDR 框架前提是否不再成立？

这是我也关注的问题。Silhouette 从 0.660 降至 0.372 意味着 drifting/stationary 的分离度大幅削弱。论文在 Limitations（p.9）承认 "silhouette compresses from 0.660 to 0.372" 但没有讨论这对 DDR 框架有效性的含义。如果 DDR 的核心 premise（存在清晰的 drifting/stationary 二分）在 instruction-tuned 模型下不再成立，那论文的理论贡献将局限于 base models——这是一个比纯分类性能下降更深层的问题。

### R1-Q4: 使用 2.8B/7B 参考模型是否改变 DDR 分区？

Appendix S（p.26）验证了 cross-family reference models 的分类信号保持（F1 spread 0.013），但**未报告 DDR 分区本身是否改变**。这是一个重要遗漏——Table 24（p.27）虽显示 cross-family reference 的 LOGO F1 一致，但 drifting/stationary 特征的 effect sizes 可能因 reference model 而变化。建议补充。

### R1-Q5: Pythia same-family 优势在多大程度上反映 architectural affinity？

Table 1（p.5）显示 Pythia-2.8B F1 = 0.724 vs 非 Pythia generator 平均 ~0.66。Appendix S 的 cross-family reference（OLMo-2 1B, Qwen3-0.6B）使 spread 缩小至 0.013，说明 architectural affinity 是一个因素但非唯一因素。论文正文（p.5）也承认 "same-family affinity with the Pythia-410M reference"。但主文未量化 affinity 的贡献比例——这可通过对比 same-family vs cross-family 的 per-generator F1 差来估算。

---

## Missing References 回应

1. **Tulchinskii et al. (2024)**: [AGREE] 我在自己的审稿中也独立建议补充。Intrinsic dimension 方法与本文的统计特征互补。
2. **代码域检测先前工作**: [AGREE] 论文在 Table 14（p.20）测试 Code 域但未引用代码检测文献，轻微遗漏。
3. **Re-Detect 系列**: [AGREE 但优先级较低] 作为 perturbation-based detection baseline 有参考价值，但论文的比较重点是 zero-shot 和 statistical 方法而非 perturbation-based。

---

## R1 主要优势的回应

完全同意 R1 识别的 5 个优势。特别是：
- **泄露控制**（LOGO + shared seeds + independent seed control, Appendix T）是我见过的 AI text detection 论文中最严谨的设计之一。
- **与检测 baseline 的对比**（Table 2, Figure 3, p.7）公平且信息量大——论文不仅展示 DDR 特征的互补性，还诚实地指出 multi-detector ensemble 仅在 2.4× cost 下微弱超过 7-feature set。

---

## 总结

R1 的审稿意见整体扎实，特别是 N2（tail_decay 稳定性）和 W2（QLoRA 跨子集对比）指出了论文的真实问题。但 **N1 和 N3 的严重程度我认为应降级**：N1 的收敛证据（generator-split, holdout, ε-stability）已相当充分，N3 的 "循环论证" 判断被 Table 30 的跨阈值稳定性数据反驳。R1 的 W5 中关于 "缺 t=1.0" 的判断是事实错误（Table 10 明确测试了 t=1.0）。

我维持 **Overall 3.0 (Findings)** 的评分，与 R1 的 3.5 (Borderline Conference) 之间的差距主要在于我对新颖性增量（DDR vs model collapse）的评估更保守。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 2756 · 2026-05-21T03:52:33.481934+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director"
}
```

</details>

---


## Round 245

## Round 245

2 recorded events


### User

_source line 2757 · 2026-05-21T03:52:43.965295+00:00_

[Reviewer 2 审稿结果]:
已完成对 R1 审稿意见的逐条交叉回应并提交给 Review Director。

核心判断：
- **N1** (k=2 聚类效力)：同意统计效力不足，但 generator-split/holdout/ε-stability 三重验证将严重性从 critical 降为 major
- **N2** (tail_decay 不稳定)：同意，4/8 TOST 通过率确实削弱 "near-stationary" 标签
- **N3** (ε=0.20 循环论证)：部分反驳——Table 30 证明分区在 ε∈[0.10, 0.75] 内不变，核心分区不依赖阈值选择
- **W5** (缺 t=1.0)：事实纠正——Table 10 明确测试了 t=1.0，R1 判断有误
- 其余 W1-W4 基本同意，与我自己审稿意见一致

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 2758 · 2026-05-21T03:52:55.211738+00:00_

Reviewer 2 的交叉回应已收到。等待 Reviewer 1 对 Reviewer 2 意见的交叉回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director"
}
```

</details>

---


## Round 246

## Round 246

12 recorded events


### User

_source line 2759 · 2026-05-21T03:53:48.005814+00:00_

[Reviewer 1 审稿意见]:

# Reviewer 1 对 Reviewer 2 审稿意见的逐条交叉回应

---

## Must-Fix 问题

**[AGREE] R2-N1: 主文页数可能超过 8 页限制**

同意，已通过 PDF 视觉检查核实。Section 5 (Discussion) 填满 page 8 并延续至 page 9 的约 30-35%；Section 6 (Conclusion) 再占 page 9 的约 20%。主文（Sections 1-6）合计约 **8.5-8.55 页**，超过 EMNLP 2026 的 8 页限制。Limitations 和 Ethics 虽不计入页数，但 Discussion 和 Conclusion 属于主文。这是格式违规，确实可能导致 desk reject。

**补充发现**：Discussion 信息密度高但篇幅过长（约 1.3 页），其中 model collapse 的区分、instruct model 讨论、QLoRA 解读、14B preliminary results 等内容可精简或移至附录，释放约 0.5 页使主文回到 8 页以内。

---

**[部分 REBUT / 部分 AGREE] R2-N2: DDR 与 model collapse / diversity loss 的区分度**

**[REBUT] "DDR = diversity loss" 的定性判断**：

R2 声称 DDR 的三个 drifting 特征"本质上就是 model collapse 文献中反复记录的 diversity loss"。但论文在 Discussion (Section 5, p.8) 和 Appendix Z.6 (Table 41, p.34) 中做了清晰的区分——两个不同现象：

1. **Model collapse** = 模型在合成数据上**重训练**导致的权重更新级别退化
2. **Recursive generation** = **固定参数**模型对文本反复推理

论文原文 (p.8): *"Prior work documents what converges—diversity loss (Guo et al., 2024), attractor dynamics (Geng et al., 2026), model collapse (Shumailov et al., 2024)—but not what is preserved; this complementary observation is what enables depth detection without per-generator calibration."*

DDR 的核心贡献不是发现 diversity loss（这确实不新颖），而是发现 **location/shape 分离**——即在 recursive generation 中，location features 单调漂移而 shape features 保持稳定。这一 decomposition 在 model collapse 文献中未被报告，且正是因为有 stable reference（shape features），depth classification 才成为可能。Table 41 (Appendix Z.6) 系统对比了本文与 Broken Telephone 和 Markovian Chains 的差异（链运算符、分析焦点、下游目标），进一步支持了区分的有效性。

因此，R2 将 DDR 等同于已知的 diversity loss 是**过度简化**。

**[AGREE] nucleus sampling 的 shape stability 验证缺失**：

R2 指出 shape stability 可能是 nucleus sampling (p=0.9) 的 trivial 推论——这是一个**精准且有力的方法论质疑**。论文自己在 Discussion (p.8) 中承认 nucleus sampling "selects from a fixed probability mass fraction at each step, preserving the functional form of the conditional distribution"——这恰恰暗示 shape stability 可能是 sampling 机制的数学性质而非生成过程的深层发现。

关键实验空白：
- 论文的温度泛化（Appendix I, Z.1）**仅在 nucleus sampling 框架内**变化温度，未测试 greedy decoding、pure top-k（无 top-p）、beam search
- 如果 shape stability 在非 nucleus sampling 下不成立，则 DDR 框架的泛化性和新颖性被显著削弱——它变成了 "nucleus sampling 的已知属性 + 已知的 diversity loss"

我在 R1-W5 中提到了温度覆盖不足，但 R2 的指出更根本——问题不仅是温度范围窄，而是**整个 decoding paradigm 的覆盖缺失**。建议将此升级为 **must-fix 级别的补充实验**（至少 greedy + top-k 各一个实验）。

---

## Should-Fix 问题

**[AGREE] R2-W1: Downstream null result 讨论不充分**

同意。Appendix M 的 TOST 显示 depth-aware curation ≈ 随机抽样——这直接影响论文在 Introduction 中建立的 "data quality" motivation。但 Discussion (p.8) 仅用一句话带过：*"depth-aware data curation does not yet translate into downstream training gain"*。一个会影响论文 motivation 的 null result 需要更充分的讨论：(1) 为什么 depth signal 不能转化为下游收益？(2) 在什么条件下可能产生差异？(3) 这是否暗示 depth features 主要捕获统计冗余信息？

**[AGREE] R2-W2: Base-model-only 限制**

完全同意。与我在 R1-W1 中的 concern 一致。Abstract 写 *"recursive generation leaves a systematic distributional signature"*——措辞暗示普适性，但 Appendix K 显示 instruct 模型 F1 降 17-21pp、DDR silhouette 从 0.660 降至 0.372。主文应明确限定 scope。

**[部分 AGREE] R2-W3: 3-class 粒度的价值**

R2 的 concern 有道理——论文缺乏令人信服的量化 use case。但我认为 depth detection 的**科学价值**独立于即时应用——证明 depth 是 detectable 本身就是贡献。论文在 Section 5 提到了 data contamination detection 和 provenance auditing，但确实缺乏量化论证。建议补充 1-2 个具体 scenario（如：training data audit 中 gen-1 vs gen-2+ 的不同处理策略）。不完全同意 R2 将此定为接近 major 的权重。

**[AGREE] R2-W4: 前 3.5 页无图表**

同意，且 R2 的估计偏保守——实际上前 **4 整页**（pages 1-4）均无任何图表，首个视觉元素（Figure 1 + Table 1）直到 page 5 才出现。这在 ACL 两栏论文中信息密度不均衡。建议将 Figure 1（或概要框架图）提前到 Introduction 末尾或 Method 开头。

**[AGREE] R2-W5: Reference model confound**

同意，与我在 R1-W3 和 R1-Q5 中提出的 concern 一致。Pythia-410M 参考模型与 Pythia 系列 generator 共享架构，Appendix S 仅测试了 ≤1B 替代参考。Table 1 中 Pythia generators 的 F1 系统性高于其他 family（0.742-0.824 vs Qwen3 系列 0.536-0.645），same-family bias 可能是重要混淆因素。

---

## Questions 回应

**R2-Q1 (greedy/top-k 下的 shape stability)**：[AGREE] 关键问题，与 N2 直接相关。建议作为 must-fix 级别补充实验。

**R2-Q2 (depth signal → downstream benefit)**：[AGREE] 与 W1 相关。当前 null result 可能因 perplexity 不够敏感或样本量不足——建议测试下游分类任务或更大规模 filtering 实验。

**R2-Q3 (proof-of-concept vs generalization claim 的张力)**：[AGREE] 有效的 tension。Limitations 自称 proof-of-concept，但 Abstract/Contribution 列表的语气更接近 established method。建议统一语气。

**R2-Q4 (instruct chain 上重新训练分类器)**：[AGREE] 合理建议。Appendix K 仅测试 base-trained classifier 在 instruct 数据上的泛化，未测试在 instruct chain 上重新训练。这是重要的消融实验空白。

**R2-Q5 (continuation vs paraphrase chain)**：[部分 REBUT] 论文在 Appendix Z.6 (Table 41, p.34) 讨论了此选择：*"Our continuation-chain setting, which imposes no semantic preservation constraint, permits richer depth signal and enables the location/shape decomposition that defines DDR."* 这一选择有方法论理由（continuation chain 语义自由度更高，允许更充分的 distributional drift）。但 R2 的隐含关切是有效的——结果可能不推广到 paraphrase 场景。建议在主文简要讨论此选择。

---

## Missing References

1. **Tulchinskii et al. (2024)**：[AGREE] 我在 R1 中也建议补充。
2. **RADAR (Hu et al., 2023)**：[AGREE] adversarial training-based 检测方法，与 feature-based 方法形成对比。
3. **Decoding strategy 对 NLL shape 的影响**：[AGREE] 直接关联 R2-N2 核心 concern。

---

## 综合评估

R2 的审稿意见质量较高，多数 concern 有理有据。**核心分歧在 N2**：

- 我**反对** R2 将 DDR 等同于 "diversity loss" 的判断——论文的 location/shape 分离是新贡献，在 model collapse 文献中未见
- 但我**支持** R2 关于 nucleus sampling confound 的质疑——shape stability 可能是 sampling 机制的已知属性，需要非 nucleus sampling 实验验证

R2 的 **3.0 (Findings)** 评分偏保守。考虑到：(1) 问题定义的新颖性；(2) 实验覆盖面（17+ 补充实验，远超平均水平）；(3) DDR 的 location/shape 分离确实是新发现（即使需要更强验证），**3.5 (Borderline Conference)** 更合适。

但如果 R2-N1 (页数违规) 确认且无法修复，或 R2-N2 (decoding strategy 验证) 的实验空白被视为 fundamental flaw，降至 3.0 可以接受。

**我维持 Overall: 3.5 (Borderline Conference)**。

### 两位 Reviewer 共识问题汇总

以下问题 R1 和 R2 **同时提出**，权重应加倍：
1. **Base-model-only 限制**（R1-W1, R2-W2）
2. **Reference model (Pythia-410M) same-family confound**（R1-W3/Q5, R2-W5）
3. **缺少 Tulchinskii et al. (2024) 引用**（R1-Missing Refs, R2-Missing Refs）
4. **Instruction-tuned 退化应在主文讨论**（R1-W1, R2-W2）
5. **Downstream null result 处理不足**（隐含在 R1 对 motivation 的评价中, R2-W1 显式提出）


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 2760 · 2026-05-21T03:54:12.067193+00:00_

called mcp__agent-ml-research__get_visual_check_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_visual_check_status</summary>

```json
{
  "project": "gen-depth-fingerprint"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "tool_args": {
    "project": "gen-depth-fingerprint"
  }
}
```

</details>

---


### Tool result

_source line 2761 · 2026-05-21T03:54:12.067676+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"done\", \"started_at\": \"2026-05-21T03:36:41.718894+00:00\", \"completed_at\": \"2026-05-21T03:41:04.152447+00:00\", \"findings\": [{\"severity\": \"warning\", \"dimension\": \"page 1-4\", \"message\": \"前 4 页连续纯文本，无任何 display item（figure/table/equation）。审稿人打开 PDF 后需翻到第 5 页才看到第一个视觉锚点（Table 1）。对于一篇 empirical 论文，这会显著削弱第一印象。建议将 Figure 1（strip plot，当前在 page 6）或一个核心结果 mini-table 提前到 page 2-3 区域。\"}, {\"severity\": \"warning\", \"dimension\": \"page 1-4\", \"message\": \"第一个 display item（Table 1）出现在第 5 页，Figure 1 出现在第 6 页。审稿人在前 2 分钟（约 2-3 页）内无法建立对核心发现的视觉认知。Figure 1 的 strip plot 是传达 DDR 核心 message 的最佳锚点，应尽量前置。\"}, {\"severity\": \"warning\", \"dimension\": \"page 8-9\", \"message\": \"Discussion（Section 5）跨 page 8 至 page 9 上半部分，约 1.5 页连续纯文本无 display item。虽然 Discussion 本身文本密集可接受，但结合前面 pages 1-4 的纯文本段，整篇论文的\\\"文本墙\\\"比例偏高。\"}, {\"severity\": \"warning\", \"dimension\": \"page 9\", \"message\": \"主文本（Abstract 至 Conclusion 末尾）延伸至第 9 页约 2/3 处（Limitations 从此处开始）。EMNLP 2026 主文本限 8 页（Limitations/Ethics 不计入），当前主文本约 8.7 页，可能超页。需用 LaTeX 的 \\\\textheight 精确确认，如超出则需压缩 Discussion 或合并 Method 中的文字描述。\"}, {\"severity\": \"info\", \"dimension\": \"page 5\", \"message\": \"Table 1 使用 booktabs 风格，最优结果加粗标注，格式规范。\"}, {\"severity\": \"info\", \"dimension\": \"page 6\", \"message\": \"Figure 1（strip plot）颜色区分度尚可，但 8 个 generator 使用 8 种颜色，部分颜色在黑白打印或色弱条件下可能难以区分。建议为关键 generator 添加 marker shape 区分。\"}, {\"severity\": \"info\", \"dimension\": \"page 7\", \"message\": \"Figure 2（DDR bar chart）和 Figure 3（baseline comparison）布局紧凑，与 Table 2 共处一页，display item 密度适当。Figure 2 的 caption 自包含，说明了 drifting/near-stationary 分类逻辑。\"}, {\"severity\": \"info\", \"dimension\": \"page 7\", \"message\": \"Table 2 与 Figure 3 排列合理，传达了 depth profiling vs. baseline detection 的核心对比。\"}, {\"severity\": \"info\", \"dimension\": \"page 15\", \"message\": \"Figure 4（violin plots）占整页约 3/4，页面底部约 1/4 为空白。附录中可将后续文字提前填充此空白。用户规则要求附录图嵌入文字附近且避免大量空白——此处有改进空间。\"}, {\"severity\": \"inf
…[truncated 1560 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 2762 · 2026-05-21T03:54:12.218404+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "gen-depth-fingerprint"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "gen-depth-fingerprint"
  }
}
```

</details>

---


### Tool result

_source line 2763 · 2026-05-21T03:54:12.319164+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"skipped\", \"paper_pdf_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/main.pdf\", \"venue\": \"EMNLP 2026\", \"requested_at\": \"2026-05-21T03:36:42.716427+00:00\", \"reminder_hours\": 8, \"chat_id\": \"oc_dbd68d7879a81efc0c108e9844b15d0b\", \"skipped_at\": \"2026-05-21T03:44:00.991901+00:00\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 2764 · 2026-05-21T03:54:30.395194+00:00_

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
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
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

_source line 2765 · 2026-05-21T03:54:30.445707+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2766 · 2026-05-21T03:58:29.669769+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "gen-depth-fingerprint",
  "issues_yaml": "# === Round 29-34 历史 Issues（保留完整记录）===\n\n- id: \"R29-N1\"\n  summary: \"Base-model-only scope 未在 Abstract 标注\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 29\n  last_seen_round: 32\n  mentions:\n    - {round: 29, reviewers: \"R1+R2\", note: \"共识: Abstract 必须标注 base-model scope\"}\n    - {round: 31, reviewers: \"R1+R2\", note: \"W1: Title/Abstract 仍需 base-model qualifier\"}\n    - {round: 32, reviewers: \"R1+R2\", note: \"升级: 实验设计仅覆盖 base model, 建议扩展或限定 scope\"}\n  action_items:\n    - {round: 29, action: \"Abstract 加 base (pretrained) qualifier\", assigned_to: Agent, status: done}\n    - {round: 32, action: \"Abstract/Conclusion 已有 qualifier; instruct in Discussion\", assigned_to: Director, status: done}\n  resolution: \"Abstract L3 'eight base-model generators'; L7 'restricted to base models'. Title 保持不变(Reviewer 确认). Instruct limitations fully documented.\"\n  resolution_round: 32\n\n- id: \"R29-N2\"\n  summary: \"Downstream TOST underpowered (n=3) + Abstract overclaim\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 29\n  last_seen_round: 34\n  mentions:\n    - {round: 29, reviewers: \"R1+R2\", note: \"n=3 seeds, Abstract 省略 preliminary\"}\n    - {round: 31, reviewers: \"R1+R2\", note: \"W3: TOST n=3 underpowered\"}\n    - {round: 32, reviewers: \"R1+R2\", note: \"升级为 null result: depth-aware curation 不优于 random\"}\n    - {round: 34, reviewers: \"R1+R2\", note: \"RESOLVED: Abstract 完全移除 downstream claim; Appendix M 坦诚呈现 null result\"}\n  action_items:\n    - {round: 29, action: \"Abstract 加 preliminary qualifier\", assigned_to: Agent, status: done}\n    - {round: 32, action: \"Abstract/Conclusion downstream reframing\", assigned_to: Director, status: done}\n  resolution: \"Abstract 完全移除 downstream claim. Appendix M 保留 null result 作为补充材料.\"\n  resolution_round: 34\n\n- id: \"R29-N3\"\n  summary: \"DDR 新颖性 incremental — 缺 concurrent work 系统对比表\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 29\n  last_seen_round: 31\n  mentions:\n    - {round: 29, reviewers: \"R1+R2\", note: \"区分不充分\"}\n    - {round: 31, reviewers: \"R1+R2\", note: \"W12: differentiation insufficient\"}\n  action_items:\n    - {round: 29, action: \"§2.2 加系统对比表\", assigned_to: Agent, status: done}\n  resolution: \"related_work.tex concurrent-comparison table added\"\n  resolution_round: 31\n\n- id: \"R29-N4\"\n  summary: \"QLoRA gap 削弱方法论贡献 — 需重定位\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 29\n  last_seen_round: 34\n  mentions:\n    - {round: 29, reviewers: \"R1+R2\", note: \"7-feat vs QLoRA gap\"}\n    - {round: 31, reviewers: \"R1+R2\", note: \"W4: contribution identity crisis\"}\n    - {round: 32, reviewers: \"R1+R2\", note: \"Contribution 3 仍以 classifier 为卖点\"}\n    - {round: 34, reviewers: \"R1+R2\", note: \"RESOLVED: Contribution 3 = 'Proof-of-concept classifier'; 5处一致传达分析工具定位\"}\n  action_items:\n    - {round: 29, action: \"§1 contribution 重排\", assigned_to: Agent, status: done}\n    - {round: 32, action: \"Proof-of-concept framing\", assigned_to: Director, status: done}\n  resolution: \"Intro L14 'proof of concept'; Contribution 3 'Proof-of-concept classifier with boundary analysis'; results.tex L17+L142; Discussion L11 — 五处一致.\"\n  resolution_round: 34\n\n- id: \"R29-W1\"\n  summary: \"Gemma-2-2B gen-1 F1=0.036 anomaly 解释不充分\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 29\n  last_seen_round: 31\n  mentions:\n    - {round: 29, reviewers: \"R1+R2\", note: \"挑战 DDR universality\"}\n  action_items:\n    - {round: 29, action: \"appendix_9gen_scale 扩展\", assigned_to: Agent, status: done}\n  resolution: \"appendix_9gen_scale expanded\"\n  resolution_round: 31\n\n- id: \"R29-W2\"\n  summary: \"Cross-model chain F1=0.830 可能混淆 depth signal 与 generator identity\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 29\n  last_seen_round: 34\n  mentions:\n    - {round: 29, reviewers: \"R1+R2\", note: \"sample-level CV vs LOGO 矛盾\"}\n    - {round: 31, reviewers: \"R1+R2\", note: \"W11: may be OOD artifact\"}\n    - {round: 32, reviewers: \"R1+R2\", note: \"应标为 upper bound\"}\n    - {round: 34, reviewers: \"R1+R2\", note: \"RESOLVED: footnote 'not directly comparable' + single-gen transfer control\"}\n  action_items:\n    - {round: 29, action: \"results.tex 标注 exploratory\", assigned_to: Agent, status: done}\n    - {round: 32, action: \"caveats added\", assigned_to: Director, status: done}\n  resolution: \"results.tex footnote + L15 single-gen transfer. Caveats sufficient.\"\n  resolution_round: 34\n\n- id: \"R29-W3\"\n  summary: \"温度限制(t<0.9)未在 Abstract 标注\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 29\n  last_seen_round: 32\n  mentions:\n    - {round: 29, reviewers: \"R1+R2\", note: \"cross-temperature transfer 不对称\"}\n  action_items:\n    - {round: 29, action: \"Abstract 加 standard decoding qualifier\", assigned_to: Agent, status: done}\n  resolution: \"Abstract L4 'nucleus sampling (p=0.9, t<=0.7)'\"\n  resolution_round: 31\n\n- id: \"R29-W4\"\n  summary: \"DDR partition 3/1/3 intermediate 定义不够 principled\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 29\n  last_seen_round: 34\n  mentions:\n    - {round: 29, reviewers: \"R1+R2\", note: \"epsilon sensitivity 未展示\"}\n    - {round: 31, reviewers: \"R1+R2\", note: \"W13: threshold arbitrary\"}\n    - {round: 32, reviewers: \"R1\", note: \"升级 Critical: k-means k=2 唯一 clean split\"}\n    - {round: 34, reviewers: \"R1+R2\", note: \"RESOLVED: binary primary partition + k=3 degradation + domain-informed refinement\"}\n  action_items:\n    - {round: 29, action: \"partition stability 分析\", assigned_to: Agent, status: done}\n    - {round: 32, action: \"Restructure 4.2: 2-way primary\", assigned_to: Director, status: done}\n  resolution: \"k=2 binary (sil=0.632); k=3 degradation (0.499); 3/1/3 = domain-informed refinement.\"\n  resolution_round: 34\n\n- id: \"R29-W5\"\n  summary: \"Baseline 范围偏窄 + 比较结构性不公平\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 29\n  last_seen_round: 35\n  mentions:\n    - {round: 29, reviewers: \"R1+R2\", note: \"缺 multi-feature detector\"}\n    - {round: 31, reviewers: \"R1+R2\", note: \"Bonferroni invalidates McNemar\"}\n    - {round: 32, reviewers: \"R1\", note: \"4-det ensemble 实际优于 7-feature\"}\n    - {round: 34, reviewers: \"R1+R2\", note: \"RESOLVED: honest presentation of 4-det+surface 0.708 > ours 0.705\"}\n    - {round: 35, reviewers: \"R1\", note: \"R1 再次质疑 baseline 公平性; R2 部分反驳: classifier 是 proof-of-concept\"}\n  action_items:\n    - {round: 32, action: \"reframed\", assigned_to: Director, status: done}\n  resolution: \"4.3 honestly presents 4-det+surface marginally exceeding. R2 rebuts severity: DDR contribution is decomposition not classification.\"\n  resolution_round: 34\n\n- id: \"R29-W6\"\n  summary: \"Related work 引用缺失 + orphan bib entries\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 29\n  last_seen_round: 35\n  mentions:\n    - {round: 29, reviewers: \"R1+R2\", note: \"RAID 未引用; orphans\"}\n    - {round: 31, reviewers: \"R1+R2\", note: \"17 orphan bib entries\"}\n    - {round: 32, reviewers: \"R1+R2\", note: \"self_refine orphan; 6 new missing refs suggested\"}\n    - {round: 34, reviewers: \"R1+R2\", note: \"Wang et al. (ACL 2025) 仍未添加\"}\n    - {round: 35, reviewers: \"R1+R2\", note: \"66条, 0 orphan, 0 missing. 覆盖良好\"}\n  action_items:\n    - {round: 29, action: \"RAID cite + orphan cleanup\", assigned_to: Agent, status: done}\n    - {round: 32, action: \"self_refine deleted; 6 refs under verification\", assigned_to: Agent, status: done}\n    - {round: 34, action: \"Wang et al. added\", assigned_to: Director, status: done}\n  resolution: \"Round 35 确认: 66条引用, 0 orphan, 0 missing.\"\n  resolution_round: 35\n\n- id: \"R29-W7\"\n  summary: \"Diagnostic not curative 缺具体场景\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 29\n  last_seen_round: 31\n  mentions:\n    - {round: 29, reviewers: \"R1+R2\", note: \"需要 end-to-end 应用案例\"}\n  action_items:\n    - {round: 29, action: \"Discussion 加 2 个场景\", assigned_to: Agent, status: done}\n  resolution: \"discussion.tex 两个诊断场景\"\n  resolution_round: 31\n\n- id: \"R29-W8\"\n  summary: \"Per-generator F1 变异大 (0.633-0.724)\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 29\n  last_seen_round: 31\n  mentions:\n    - {round: 29, reviewers: \"R1+R2\", note: \"generator-unknown 场景实用性受限\"}\n  action_items:\n    - {round: 29, action: \"Discussion caveat\", assigned_to: Agent, status: done}\n  resolution: \"discussion.tex '9.1pp per-generator spread'\"\n  resolution_round: 31\n\n- id: \"R32-N1\"\n  summary: \"DDR 增量新颖性不清晰 — 可能是 diversity loss / mode-seeking 的重新表述\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 32\n  last_seen_round: 36\n  mentions:\n    - {round: 32, reviewers: \"R2+R1\", note: \"DDR 可能是 diversity loss 重新表述\"}\n    - {round: 34, reviewers: \"R1+R2\", note: \"RESOLVED: 'what converges vs what is preserved' framing\"}\n    - {round: 35, reviewers: \"R2\", note: \"Shape stability 可能是 top-p 采样机制的 trivial 推论; R1 REBUT: 温度消融证明非无条件成立\"}\n    - {round: 36, reviewers: \"R1+R2\", note: \"R2 再次质疑: shape stability 是 nucleus sampling 的 by-design 结果; R1 部分反驳 DDR≠diversity loss (location/shape 分离是新贡献) 但同意 nucleus sampling confound 需要非 nucleus 实验验证\"}\n  action_items:\n    - {round: 32, action: \"Discussion expanded: shape stability as novel contribution\", assigned_to: Director, status: done}\n    - {round: 35, action: \"区分 mechanistic explanation 和 empirical contribution; 强调边界条件 (τ≥0.9)\", assigned_to: Agent, status: in_progress}\n    - {round: 36, action: \"补充 greedy/top-k decoding 下 shape stability 验证实验; 或明确承认 nucleus-sampling-specific 并精准界定增量贡献\", assigned_to: Agent, status: pending}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R32-N2\"\n  summary: \"Entropy min 分类存在根本性矛盾 (|rho|=0.40 标为 near-stationary)\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 32\n  last_seen_round: 34\n  mentions:\n    - {round: 32, reviewers: \"R1\", note: \"|rho|=0.40 vs d=0.016 vs delta=0.354 矛盾\"}\n    - {round: 34, reviewers: \"R1+R2\", note: \"RESOLVED: 'boundary feature' label + gen-0/gen-1 transition mechanism + k=2 placement\"}\n  action_items:\n    - {round: 32, action: \"Label as boundary feature\", assigned_to: Director, status: done}\n  resolution: \"results.tex L85 'boundary feature' with full qualification; Figure 2 caption aligned.\"\n  resolution_round: 34\n\n- id: \"R32-N3\"\n  summary: \"Tail_decay near-stationary 归类仅 4/8 generator 通过 TOST (epsilon=0.20)\"\n  category: method\n  severity: critical\n  status: in_progress\n  first_raised_round: 32\n  last_seen_round: 36\n  mentions:\n    - {round: 32, reviewers: \"R1\", note: \"50% pass rate; OLMo d=0.22\"}\n    - {round: 34, reviewers: \"R1+R2\", note: \"RESOLVED: L89-91 three-sentence coverage\"}\n    - {round: 35, reviewers: \"R1+R2\", note: \"4/8 TOST 通过率不足; 共识: 主文应更诚实处理 boundary status\"}\n    - {round: 36, reviewers: \"R1+R2\", note: \"共识: tail_decay 应重分类为 'weakly stationary' 或 'inconsistent'; Granger p=0.375 + importance rank 7/7 进一步证实不稳定; 非通过 generators |d|=0.15-0.22 虽远低于 drifting 但不满足 near-stationary\"}\n  action_items:\n    - {round: 32, action: \"Transparent reporting in main text\", assigned_to: Director, status: done}\n    - {round: 35, action: \"验证 <0.5pp claim 溯源; 确认措辞足够诚实\", assigned_to: Agent, status: in_progress}\n    - {round: 36, action: \"主文将 tail_decay 重分类为 weakly stationary 并讨论异质性; 在 Figure 2 中用不同标记区分\", assigned_to: Agent, status: pending}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R32-W1\"\n  summary: \"分类性能 F1=0.694 定位为 detecting 但实为 proof-of-concept\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 32\n  last_seen_round: 34\n  mentions:\n    - {round: 32, reviewers: \"R1+R2\", note: \"~30% 错分率\"}\n    - {round: 34, reviewers: \"R1+R2\", note: \"RESOLVED: Discussion L11 'proof-of-concept, not a deployable system'\"}\n  action_items:\n    - {round: 32, action: \"Discussion proof-of-concept framing\", assigned_to: Director, status: done}\n  resolution: \"Intro L14, Contribution 3, Discussion L11 — all say 'proof-of-concept'.\"\n  resolution_round: 34\n\n- id: \"R32-W2\"\n  summary: \"TOST power analysis 缺失\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 32\n  last_seen_round: 34\n  mentions:\n    - {round: 32, reviewers: \"R1\", note: \"大样本 TOST 几乎总检测 equivalence\"}\n    - {round: 34, reviewers: \"R1+R2\", note: \"共识: SESOI+epsilon+caveat 足够\"}\n  action_items:\n    - {round: 32, action: \"TOST power computation\", assigned_to: Agent, status: wont_fix}\n  resolution: \"SESOI justification + epsilon sensitivity + high-N masking acknowledged.\"\n  resolution_round: 34\n\n- id: \"R32-W3\"\n  summary: \"术语混淆: entropy 指代 NLL 不规范\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 32\n  last_seen_round: 35\n  mentions:\n    - {round: 32, reviewers: \"R2\", note: \"NLL 与 Shannon entropy 不同\"}\n    - {round: 35, reviewers: \"R2\", note: \"再次提出; R1 REBUT: 已有声明且符合领域惯例\"}\n  action_items:\n    - {round: 32, action: \"Existing clarification sufficient\", assigned_to: Director, status: wont_fix}\n  resolution: \"method.tex 3.3 L38 explicit clarification. Round 35 R1 confirms field convention.\"\n  resolution_round: 32\n\n- id: \"R32-W4\"\n  summary: \"附录 25 页过大, 关键结果应在主文讨论\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 32\n  last_seen_round: 32\n  mentions:\n    - {round: 32, reviewers: \"R2\", note: \"25 页附录\"}\n  action_items:\n    - {round: 32, action: \"Key numbers already in main text\", assigned_to: Director, status: wont_fix}\n  resolution: \"QLoRA/instruct numbers in 4.1 and Discussion. Full tables in appendix per 8-page limit.\"\n  resolution_round: 32\n\n- id: \"R32-W5\"\n  summary: \"单一解码策略(nucleus only)\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 32\n  last_seen_round: 36\n  mentions:\n    - {round: 32, reviewers: \"R1+R2\", note: \"greedy/top-k 未验证\"}\n    - {round: 36, reviewers: \"R1+R2\", note: \"升级: nucleus sampling confound 直接关联 DDR 核心新颖性; shape stability 可能是 top-p truncation 的 by-design 结果; 需 greedy/top-k 实验验证\"}\n  action_items:\n    - {round: 32, action: \"Acknowledged as limitation\", assigned_to: Director, status: done}\n    - {round: 36, action: \"补充至少 greedy + top-k 各一个实验验证 shape stability; 或在 Discussion 明确承认 nucleus-sampling-specific\", assigned_to: Agent, status: pending}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R32-W6\"\n  summary: \"3-class F1=0.762 因 gen-0 共享而 misleading\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 32\n  last_seen_round: 32\n  mentions:\n    - {round: 32, reviewers: \"R1+R2\", note: \"gen-0 recall 99.4%\"}\n  action_items:\n    - {round: 32, action: \"Binary F1 is primary in Abstract\", assigned_to: Director, status: wont_fix}\n  resolution: \"Abstract uses binary F1 only; 4.1 notes gen-0 inflation.\"\n  resolution_round: 32\n\n- id: \"R32-W7\"\n  summary: \"特征选取缺乏系统性论证\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 32\n  last_seen_round: 32\n  mentions:\n    - {round: 32, reviewers: \"R1+R2\", note: \"R1 major, R2 降级 warning\"}\n  action_items:\n    - {round: 32, action: \"method.tex explains rationale\", assigned_to: Director, status: done}\n  resolution: \"method.tex 3.3 a priori selection + LOFO validation + richer-features tradeoff note.\"\n  resolution_round: 32\n\n- id: \"R34-W1\"\n  summary: \"Base-model-only scope 限制泛化价值 (结构性)\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 34\n  last_seen_round: 36\n  mentions:\n    - {round: 34, reviewers: \"R1+R2\", note: \"instruct model F1=0.338-0.667. scope limitation 非 fatal flaw\"}\n    - {round: 35, reviewers: \"R1+R2\", note: \"instruct 退化 3.7x; motivation narrative 与 base-only scope 存在张力. Abstract 应更早限定 scope; Discussion curation 场景限定\"}\n    - {round: 36, reviewers: \"R1+R2\", note: \"共识: Appendix K 关键数据 (F1 降 17-21pp, silhouette 0.660→0.372) 应在主文 Discussion 讨论; Abstract/Intro 措辞暗示广泛适用性需修正\"}\n  action_items:\n    - {round: 34, action: \"Rebuttal: base model 是实验控制; QLoRA instruct recovery\", assigned_to: Director, status: done}\n    - {round: 35, action: \"Abstract 加 base-model scope 限定; Introduction reframe synthetic data pipeline; Discussion curation 场景限定\", assigned_to: Agent, status: in_progress}\n    - {round: 36, action: \"主文 Discussion 补充 instruct 退化段落; Intro 第一段明确 base-model scope\", assigned_to: Agent, status: pending}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R34-W2\"\n  summary: \"F1=0.694 性能天花板 (结构性)\"\n  category: experiment\n  severity: warning\n  status: wont_fix\n  first_raised_round: 34\n  last_seen_round: 34\n  mentions:\n    - {round: 34, reviewers: \"R1+R2\", note: \"proof-of-concept 定位缓解期望落差\"}\n  action_items:\n    - {round: 34, action: \"Rebuttal: DDR 贡献是分析框架; LOGO 是最严格下界\", assigned_to: Director, status: done}\n  resolution: \"结构性限制, proof-of-concept 定位已到位.\"\n  resolution_round: 34\n\n- id: \"R34-W3\"\n  summary: \"QLoRA gap (+11.6pp) 未充分解释\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 34\n  last_seen_round: 36\n  mentions:\n    - {round: 34, reviewers: \"R1+R2\", note: \"7 个手工特征丢失大量信号\"}\n    - {round: 35, reviewers: \"R2\", note: \"QLoRA instruct 恢复暗示 DDR 以外信号存在\"}\n    - {round: 36, reviewers: \"R1+R2\", note: \"共识: +11.6pp 比较基于 6-gen subset (XGBoost=0.789) 而非 8-gen LOGO (0.694); 读者容易误读; 需在 Appendix E 和 Discussion 每次引用时标注 '(6-gen subset)'\"}\n  action_items:\n    - {round: 34, action: \"Discussion 补充: token-order dependencies + positional patterns\", assigned_to: Director, status: done}\n    - {round: 35, action: \"修复 +11.6pp baseline 标注不一致 (vs 6-gen not 8-gen)\", assigned_to: Agent, status: in_progress}\n    - {round: 36, action: \"Appendix E + Discussion 所有 QLoRA 引用标注 '(6-gen subset)'; 补报 8-gen LOGO 下 QLoRA 结果\", assigned_to: Agent, status: pending}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R34-V1\"\n  summary: \"Pages 1-4 无任何 display item, 纯文字密度过高\"\n  category: format\n  severity: warning\n  status: open\n  first_raised_round: 34\n  last_seen_round: 36\n  mentions:\n    - {round: 34, reviewers: \"R1+R2\", note: \"Critical visual: 前 4 页纯文字\"}\n    - {round: 35, reviewers: \"Visual Check\", note: \"连续 4 页纯文本; 缺 overview figure; p.7 过密\"}\n    - {round: 36, reviewers: \"R1+R2+Visual Check\", note: \"三方共识: 前 4 页纯文字严重影响 empirical paper 可读性; 建议将 Figure 1 或 method comparison table 前移到 p.2-3\"}\n  action_items:\n    - {round: 34, action: \"Figure 2 前移至 Introduction 末尾\", assigned_to: Director, status: done}\n    - {round: 35, action: \"考虑 pipeline overview figure; 分散 p.7 float\", assigned_to: Director, status: pending}\n    - {round: 36, action: \"将 Figure 1 (strip plot) 前移至 Introduction 末尾或 Method 开头; 或在 Related Work 加入结构化对比表\", assigned_to: Agent, status: pending}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R34-W4\"\n  summary: \"14B entropy_mean |rho|=0.39 跨过 drifting boundary 未明确报告\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 34\n  last_seen_round: 36\n  mentions:\n    - {round: 34, reviewers: \"Reviewer\", note: \"Discussion 只写 'attenuates by 21-35%'\"}\n    - {round: 35, reviewers: \"R1+R2\", note: \"14B 初步证据放正文中读者可能高估. Research Reviewer 建议保留但缩到 1 句\"}\n    - {round: 36, reviewers: \"R1+R2\", note: \"本轮未单独提及，Discussion 中 14B 内容为压缩页数的候选删除对象\"}\n  action_items:\n    - {round: 34, action: \"Discussion 精确化\", assigned_to: Director, status: done}\n    - {round: 35, action: \"缩到 1 句, full results 引用 Appendix\", assigned_to: Agent, status: in_progress}\n  resolution: \"\"\n  resolution_round: null\n\n# === Round 35 Issues ===\n\n- id: \"R35-N1\"\n  summary: \"k=2 聚类在 7 个数据点上做 data-driven validation 方法学不足\"\n  category: method\n  severity: critical\n  status: in_progress\n  first_raised_round: 35\n  last_seen_round: 36\n  mentions:\n    - {round: 35, reviewers: \"R1+R2\", note: \"共识: 7 点 k-means 近 trivial; silhouette 不具统计意义; Appendix V generator-split 更有说服力\"}\n    - {round: 36, reviewers: \"R1+R2\", note: \"R1 维持 critical (描述性非推断性, p=0.030 仅边际显著); R2 降级为 major (generator-split/holdout/ε-stability 三重验证已相当充分); 共识: 补充 gap statistic 或 sample-level bootstrap 可强化论证\"}\n  action_items:\n    - {round: 35, action: \"Abstract/Intro 下调 data-driven; §4.2 提升 generator-split consistency 为 primary validation; permutation test 补充\", assigned_to: Agent, status: in_progress}\n    - {round: 36, action: \"补充 gap statistic / prediction strength 替代 silhouette; 考虑 sample-level bootstrap 重采样验证聚类稳定性\", assigned_to: Agent, status: pending}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R35-N2\"\n  summary: \"与 Markovian Chains (Geng et al., 2026) 区分度不足\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 35\n  last_seen_round: 36\n  mentions:\n    - {round: 35, reviewers: \"R1+R2\", note: \"共识: setup 重叠度高; 当前区分仅一句话; 需系统性对比表\"}\n    - {round: 36, reviewers: \"R1+R2\", note: \"本轮未作为独立 issue 单独提出; R1 交叉回应中引用 Table 41 (Appendix Z.6) 作为已有缓解; Related Work §2.2 最后一段有对比讨论\"}\n  action_items:\n    - {round: 35, action: \"WebSearch 补全细节 + §2.2 加系统对比表 (chain type / feature space / 目标 / scale / insight)\", assigned_to: Agent, status: in_progress}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R35-W1\"\n  summary: \"Five 'independent' effect-size metrics overclaim\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 35\n  last_seen_round: 36\n  mentions:\n    - {round: 35, reviewers: \"R1+R2\", note: \"共识: Cohen's d ~ Glass's Delta ~ KS 高度相关; 真正独立的仅 Cliff's delta 和 CV shift\"}\n    - {round: 36, reviewers: \"R1+R2\", note: \"共识: 'five complementary' 仍有 overclaim 嫌疑; 建议改为 'convergence across parametric and non-parametric measures'; 补充度量间相关矩阵\"}\n  action_items:\n    - {round: 35, action: \"'five independent' → 'five complementary'; 区分 parametric overlap 与 genuinely independent perspectives\", assigned_to: Agent, status: in_progress}\n    - {round: 36, action: \"Abstract/§4.2 措辞改为 'convergence across parametric and non-parametric measures'; Appendix 补充 inter-measure 相关矩阵\", assigned_to: Agent, status: pending}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R35-W2\"\n  summary: \"TOST epsilon=0.20 循环论证\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 35\n  last_seen_round: 36\n  mentions:\n    - {round: 35, reviewers: \"R1+R2\", note: \"共识: 先按 d<0.20 分类 → LOFO 验证 → 用 LOFO justify epsilon. Mitigating: Cohen (1988) conventional threshold\"}\n    - {round: 36, reviewers: \"R1+R2\", note: \"R1 维持 critical; R2 部分反驳 (Table 30 证明核心分区在 ε∈[0.10,0.75] 内不变); 共识: Cohen 惯例有合理基础但需补充 downstream task 角度的独立正当性\"}\n  action_items:\n    - {round: 35, action: \"承认 epsilon=0.20 是 conventional; 主文引用 Appendix V epsilon robustness\", assigned_to: Agent, status: in_progress}\n    - {round: 36, action: \"从分类 F1 角度反推 SESOI (操作上可忽略的最小效应); 或绘制 equivalence frontier 图\", assigned_to: Agent, status: pending}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R35-W3\"\n  summary: \"Downstream null result 未在主文 Discussion 讨论\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 35\n  last_seen_round: 36\n  mentions:\n    - {round: 35, reviewers: \"R1+R2\", note: \"共识: Appendix M TOST equivalence 未在 Discussion 提及; selective reporting concern; reframe 为 provenance/audit\"}\n    - {round: 36, reviewers: \"R1+R2\", note: \"共识: Discussion 中仅一句带过不充分; 需专门段落讨论 null result 含义、为什么 depth signal 不能转化下游收益、在什么条件下可能产生差异\"}\n  action_items:\n    - {round: 35, action: \"Discussion 加一段承认 null result; reframe value 为 provenance/audit\", assigned_to: Agent, status: in_progress}\n    - {round: 36, action: \"Discussion 增加专门段落讨论 downstream null result 的机制解释和边界条件\", assigned_to: Agent, status: pending}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R35-W4\"\n  summary: \"Abstract 中 binary F1=0.694 定义模糊\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 35\n  last_seen_round: 36\n  mentions:\n    - {round: 35, reviewers: \"R1+R2\", note: \"共识: 未明确 binary 指 gen-1 vs gen-2+, 非 human vs machine\"}\n    - {round: 36, reviewers: \"R2\", note: \"Abstract 声称的定义在 §4.1 中有明确解释，基本一致\"}\n  action_items:\n    - {round: 35, action: \"Abstract 加 '(gen-1 vs gen-2+, excluding shared gen-0 seeds)'\", assigned_to: Agent, status: in_progress}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R35-M3\"\n  summary: \"Bootstrap CI 不反映 generator selection uncertainty\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 35\n  last_seen_round: 36\n  mentions:\n    - {round: 35, reviewers: \"R1\", note: \"per-generator F1 span 9.1pp 未区分于 sampling CI\"}\n    - {round: 36, reviewers: \"R1+R2\", note: \"共识: bootstrap CI 宽度仅 4.8pp 但 per-generator range 达 28.8pp; Pythia 系列系统性高于其他 family; 需补充 generator-level variance 统计量 (SD/IQR) 与 bootstrap CI 并列报告\"}\n  action_items:\n    - {round: 35, action: \"§4.1 加一句区分 sampling CI 和 generalization variability\", assigned_to: Agent, status: in_progress}\n    - {round: 36, action: \"Table 1 或正文补充 across-generator SD; 讨论 hierarchical bootstrap 或 generator-level variance\", assigned_to: Agent, status: pending}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R35-M4\"\n  summary: \"Chain depth=4 选择未在主文 justify\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 35\n  last_seen_round: 36\n  mentions:\n    - {round: 35, reviewers: \"R1\", note: \"depth=4 的选择未解释\"}\n    - {round: 36, reviewers: \"R1+R2\", note: \"本轮未单独提及; §3.2 已有 justification (depth 2-4 indistinguishable → gen-2+ collapse)\"}\n  action_items:\n    - {round: 35, action: \"§3.2 加 depth=4 justification, 引用 finer-grained analysis appendix\", assigned_to: Agent, status: in_progress}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R35-M5\"\n  summary: \"5 条 bib entries first_author mismatch\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 35\n  last_seen_round: 36\n  mentions:\n    - {round: 35, reviewers: \"R2\", note: \"LaTeX 编码 vs API 索引差异导致 first_author mismatch\"}\n    - {round: 36, reviewers: \"R1+R2\", note: \"R1 确认 5 个 mismatch 均为编码差异 (Team vs 具体作者名), 非实质性错误; 0 orphan, 0 missing\"}\n  action_items:\n    - {round: 35, action: \"待定位具体 5 条 entries 后修复\", assigned_to: Agent, status: pending}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R35-E1\"\n  summary: \"+11.6pp 标注 baseline 不一致 (vs 6-gen 而非 8-gen)\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 35\n  last_seen_round: 36\n  mentions:\n    - {round: 35, reviewers: \"Research Reviewer\", note: \"+11.6pp = 0.905-0.789 (vs 6-gen), 非 0.905-0.762 (vs 8-gen). 读者计算 14.3pp ≠ 11.6pp 会困惑\"}\n    - {round: 36, reviewers: \"R1+R2\", note: \"共识: 跨子集 delta 容易误导; 需在每次引用时标注 (6-gen subset)\"}\n  action_items:\n    - {round: 35, action: \"+11.6pp 后加 '(vs 6-gen XGBoost; Table 2)'\", assigned_to: Agent, status: in_progress}\n    - {round: 36, action: \"与 R34-W3 合并处理: 所有 QLoRA 引用标注子集信息\", assigned_to: Agent, status: pending}\n  resolution: \"\"\n  resolution_round: null\n\n# === Round 36 新 Issues ===\n\n- id: \"R36-N1\"\n  summary: \"主文页数超过 EMNLP 8 页限制 (约 8.5-8.7 页)\"\n  category: format\n  severity: critical\n  status: open\n  first_raised_round: 36\n  last_seen_round: 36\n  mentions:\n    - {round: 36, reviewers: \"R1+R2+Visual Check\", note: \"三方独立确认: Discussion 跨 p.8-p.9, Conclusion 在 p.9; 主文合计约 8.5-8.7 页; 格式违规可导致 desk reject\"}\n  action_items:\n    - {round: 36, action: \"压缩 Discussion 从 ~1.3 页至 ~0.8 页 (model collapse 区分、14B 结果、温度重复论述移至附录); 压缩 Conclusion\", assigned_to: Agent, status: pending}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R36-W1\"\n  summary: \"3-class 粒度的实际价值论证不足\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 36\n  last_seen_round: 36\n  mentions:\n    - {round: 36, reviewers: \"R2\", note: \"3-class vs binary 的增量价值缺乏令人信服的 use case; R1 部分同意但认为科学价值独立于即时应用\"}\n  action_items:\n    - {round: 36, action: \"Discussion 补充 1-2 个量化 use case (如 training data audit 中 gen-1 vs gen-2+ 的不同处理策略)\", assigned_to: Agent, status: pending}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R36-W2\"\n  summary: \"Reference model (Pythia-410M) same-family confound 主文讨论不足\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 36\n  last_seen_round: 36\n  mentions:\n    - {round: 36, reviewers: \"R1+R2\", note: \"共识: Pythia generators F1 系统性高于其他 family (0.718-0.724 vs avg ~0.66); Appendix S cross-family 验证有效但主文仅一笔带过; 需分 generator 报告 reference model 切换影响\"}\n  action_items:\n    - {round: 36, action: \"§3.3 或 §5 补充 reference model bias 讨论; 考虑分 generator 报告 cross-reference 影响\", assigned_to: Agent, status: pending}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R36-R1\"\n  summary: \"缺少 Tulchinskii et al. (2024) 'Intrinsic Dimension Estimation' (ICLR 2024) 引用\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 36\n  last_seen_round: 36\n  mentions:\n    - {round: 36, reviewers: \"R1+R2\", note: \"两位 Reviewer 独立建议补充; 使用几何/拓扑特征检测 AI 文本, 与本文 distributional statistics 方法互补\"}\n  action_items:\n    - {round: 36, action: \"§2.1 Related Work 补充引用\", assigned_to: Agent, status: pending}\n  resolution: \"\"\n  resolution_round: null"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "gen-depth-fingerprint",
    "issues_yaml": "# === Round 29-34 历史 Issues（保留完整记录）===\n\n- id: \"R29-N1\"\n  summary: \"Base-model-only scope 未在 Abstract 标注\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 29\n  last_seen_round: 32\n  mentions:\n    - {round: 29, reviewers: \"R1+R2\", note: \"共识: Abstract 必须标注 base-model scope\"}\n    - {round: 31, reviewers: \"R1+R2\", note: \"W1: Title/Abstract 仍需 base-model qualifier\"}\n    - {round: 32, reviewers: \"R1+R2\", note: \"升级: 实验设计仅覆盖 base model, 建议扩展或限定 scope\"}\n  action_items:\n    - {round: 29, action: \"Abstract 加 base (pretrained) qualifier\", assigned_to: Agent, status: done}\n    - {round: 32, action: \"Abstract/Conclusion 已有 qualifier; instruct in Discussion\", assigned_to: Director, status: done}\n  resolution: \"Abstract L3 'eight base-model generators'; L7 'restricted to base models'. Title 保持不变(Reviewer 确认). Instruct limitations fully documented.\"\n  resolution_round: 32\n\n- id: \"R29-N2\"\n  summary: \"Downstream TOST underpowered (n=3) + Abstract overclaim\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 29\n  last_seen_round: 34\n  mentions:\n    - {round: 29, reviewers: \"R1+R2\", note: \"n=3 seeds, Abstract 省略 preliminary\"}\n    - {round: 31, reviewers: \"R1+R2\", note: \"W3: TOST n=3 underpowered\"}\n    - {round: 32, reviewers: \"R1+R2\", note: \"升级为 null result: depth-aware curation 不优于 random\"}\n    - {round: 34, reviewers: \"R1+R2\", note: \"RESOLVED: Abstract 完全移除 downstream claim; Appendix M 坦诚呈现 null result\"}\n  action_items:\n    - {round: 29, action: \"Abstract 加 preliminary qualifier\", assigned_to: Agent, status: done}\n    - {round: 32, action: \"Abstract/Conclusion downstream reframing\", assigned_to: Director, status: done}\n  resolution: \"Abstract 完全移除 downstream claim. Appendix M 保留 null result 作为补充材料.\"\n  resolution_round: 34\n\n- id: \"R29-N3\"\n  summary: \"DDR 新颖性 incremental — 缺 concurrent work 系统对比表\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 29\n  last_seen_round: 31\n  mentions:\n    - {round: 29, reviewers: \"R1+R2\", note: \"区分不充分\"}\n    - {round: 31, reviewers: \"R1+R2\", note: \"W12: differentiation insufficient\"}\n  action_items:\n    - {round: 29, action: \"§2.2 加系统对比表\", assigned_to: Agent, status: done}\n  resolution: \"related_work.tex concurrent-comparison table added\"\n  resolution_round: 31\n\n- id: \"R29-N4\"\n  summary: \"QLoRA gap 削弱方法论贡献 — 需重定位\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 29\n  last_seen_round: 34\n  mentions:\n    - {round: 29, reviewers: \"R1+R2\", note: \"7-feat vs QLoRA gap\"}\n    - {round: 31, reviewers: \"R1+R2\", note: \"W4: contribution identity crisis\"}\n    - {round: 32, reviewers: \"R1+R2\", note: \"Contribution 3 仍以 classifier 为卖点\"}\n    - {round: 34, reviewers: \"R1+R2\", note: \"RESOLVED: Contribution 3 = 'Proof-of-concept classifier'; 5处一致传达分析工具定位\"}\n  action_items:\n    - {round: 29, action: \"§1 contribution 重排\", assigned_to: Agent, status: done}\n    - {round: 32, action: \"Proof-of-concept framing\", assigned_to: Director, status: done}\n  resolution: \"Intro L14 'proof of concept'; Contribution 3 'Proof-of-concept classifier with boundary analysis'; results.tex L17+L142; Discussion L11 — 五处一致.\"\n  resolution_round: 34\n\n- id: \"R29-W1\"\n  summary: \"Gemma-2-2B gen-1 F1=0.036 anomaly 解释不充分\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 29\n  last_seen_round: 31\n  mentions:\n    - {round: 29, reviewers: \"R1+R2\", note: \"挑战 DDR universality\"}\n  action_items:\n    - {round: 29, action: \"appendix_9gen_scale 扩展\", assigned_to: Agent, status: done}\n  resolution: \"appendix_9gen_scale expanded\"\n  resolution_round: 31\n\n- id: \"R29-W2\"\n  summary: \"Cross-model chain F1=0.830 可能混淆 depth signal 与 generator identity\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 29\n  last_seen_round: 34\n  mentions:\n    - {round: 29, reviewers: \"R1+R2\", note: \"sample-level CV vs LOGO 矛盾\"}\n    - {round: 31, reviewers: \"R1+R2\", note: \"W11: may be OOD artifact\"}\n    - {round: 32, reviewers: \"R1+R2\", note: \"应标为 upper bound\"}\n    - {round: 34, reviewers: \"R1+R2\", note: \"RESOLVED: footnote 'not directly comparable' + single-gen transfer control\"}\n  action_items:\n    - {round: 29, action: \"results.tex 标注 exploratory\", assigned_to: Agent, status: done}\n    - {round: 32, action: \"caveats added\", assigned_to: Director, status: done}\n  resolution: \"results.tex footnote + L15 single-gen transfer. Caveats sufficient.\"\n  resolution_round: 34\n\n- id: \"R29-W3\"\n  summary: \"温度限制(t<0.9)未在 Abstract 标注\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 29\n  last_seen_round: 32\n  mentions:\n    - {round: 29, reviewers: \"R1+R2\", note: \"cross-temperature transfer 不对称\"}\n  action_items:\n    - {round: 29, action: \"Abstract 加 standard decoding qualifier\", assigned_to: Agent, status: done}\n  resolution: \"Abstract L4 'nucleus sampling (p=0.9, t<=0.7)'\"\n  resolution_round: 31\n\n- id: \"R29-W4\"\n  summary: \"DDR partition 3/1/3 intermediate 定义不够 principled\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 29\n  last_seen_round: 34\n  mentions:\n    - {round: 29, reviewers: \"R1+R2\", note: \"epsilon sensitivity 未展示\"}\n    - {round: 31, reviewers: \"R1+R2\", note: \"W13: threshold arbitrary\"}\n    - {round: 32, reviewers: \"R1\", note: \"升级 Critical: k-means k=2 唯一 clean split\"}\n    - {round: 34, reviewers: \"R1+R2\", note: \"RESOLVED: binary primary partition + k=3 degradation + domain-informed refinement\"}\n  action_items:\n    - {round: 29, action: \"partition stability 分析\", assigned_to: Agent, status: done}\n    - {round: 32, action: \"Restructure 4.2: 2-way primary\", assigned_to: Director, status: done}\n  resolution: \"k=2 binary (sil=0.632); k=3 degradation (0.499); 3/1/3 = domain-informed refinement.\"\n  resolution_round: 34\n\n- id: \"R29-W5\"\n  summary: \"Baseline 范围偏窄 + 比较结构性不公平\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 29\n  last_seen_round: 35\n  mentions:\n    - {round: 29, reviewers: \"R1+R2\", note: \"缺 multi-feature detector\"}\n    - {round: 31, reviewers: \"R1+R2\", note: \"Bonferroni invalidates McNemar\"}\n    - {round: 32, reviewers: \"R1\", note: \"4-det ensemble 实际优于 7-feature\"}\n    - {round: 34, reviewers: \"R1+R2\", note: \"RESOLVED: honest presentation of 4-det+surface 0.708 > ours 0.705\"}\n    - {round: 35, reviewers: \"R1\", note: \"R1 再次质疑 baseline 公平性; R2 部分反驳: classifier 是 proof-of-concept\"}\n  action_items:\n    - {round: 32, action: \"reframed\", assigned_to: Director, status: done}\n  resolution: \"4.3 honestly presents 4-det+surface marginally exceeding. R2 rebuts severity: DDR contribution is decomposition not classification.\"\n  resolution_round: 34\n\n- id: \"R29-W6\"\n  summary: \"Related work 引用缺失 + orphan bib entries\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 29\n  last_seen_round: 35\n  mentions:\n    - {round: 29, reviewers: \"R1+R2\", note: \"RAID 未引用; orphans\"}\n    - {round: 31, reviewers: \"R1+R2\", note: \"17 orphan bib entries\"}\n    - {round: 32, reviewers: \"R1+R2\", note: \"self_refine orphan; 6 new missing refs suggested\"}\n    - {round: 34, reviewers: \"R1+R2\", note: \"Wang et al. (ACL 2025) 仍未添加\"}\n    - {round: 35, reviewers: \"R1+R2\", note: \"66条, 0 orphan, 0 missing. 覆盖良好\"}\n  action_items:\n    - {round: 29, action: \"RAID cite + orphan cleanup\", assigned_to: Agent, status: done}\n    - {round: 32, action: \"self_refine deleted; 6 refs under verification\", assigned_to: Agent, status: done}\n    - {round: 34, action: \"Wang et al. added\", assigned_to: Director, status: done}\n  resolution: \"Round 35 确认: 66条引用, 0 orphan, 0 missing.\"\n  resolution_round: 35\n\n- id: \"R29-W7\"\n  summary: \"Diagnostic not curative 缺具体场景\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 29\n  last_seen_round: 31\n  mentions:\n    - {round: 29, reviewers: \"R1+R2\", note: \"需要 end-to-end 应用案例\"}\n  action_items:\n    - {round: 29, action: \"Discussion 加 2 个场景\", assigned_to: Agent, status: done}\n  resolution: \"discussion.tex 两个诊断场景\"\n  resolution_round: 31\n\n- id: \"R29-W8\"\n  summary: \"Per-generator F1 变异大 (0.633-0.724)\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 29\n  last_seen_round: 31\n  mentions:\n    - {round: 29, reviewers: \"R1+R2\", note: \"generator-unknown 场景实用性受限\"}\n  action_items:\n    - {round: 29, action: \"Discussion caveat\", assigned_to: Agent, status: done}\n  resolution: \"discussion.tex '9.1pp per-generator spread'\"\n  resolution_round: 31\n\n- id: \"R32-N1\"\n  summary: \"DDR 增量新颖性不清晰 — 可能是 diversity loss / mode-seeking 的重新表述\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 32\n  last_seen_round: 36\n  mentions:\n    - {round: 32, reviewers: \"R2+R1\", note: \"DDR 可能是 diversity loss 重新表述\"}\n    - {round: 34, reviewers: \"R1+R2\", note: \"RESOLVED: 'what converges vs what is preserved' framing\"}\n    - {round: 35, reviewers: \"R2\", note: \"Shape stability 可能是 top-p 采样机制的 trivial 推论; R1 REBUT: 温度消融证明非无条件成立\"}\n    - {round: 36, reviewers: \"R1+R2\", note: \"R2 再次质疑: shape stability 是 nucleus sampling 的 by-design 结果; R1 部分反驳 DDR≠diversity loss (location/shape 分离是新贡献) 但同意 nucleus sampling confound 需要非 nucleus 实验验证\"}\n  action_items:\n    - {round: 32, action: \"Discussion expanded: shape stability as novel contribution\", assigned_to: Director, status: done}\n    - {round: 35, action: \"区分 mechanistic explanation 和 empirical contribution; 强调边界条件 (τ≥0.9)\", assigned_to: Agent, status: in_progress}\n    - {round: 36, action: \"补充 greedy/top-k decoding 下 shape stability 验证实验; 或明确承认 nucleus-sampling-specific 并精准界定增量贡献\", assigned_to: Agent, status: pending}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R32-N2\"\n  summary: \"Entropy min 分类存在根本性矛盾 (|rho|=0.40 标为 near-stationary)\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 32\n  last_seen_round: 34\n  mentions:\n    - {round: 32, reviewers: \"R1\", note: \"|rho|=0.40 vs d=0.016 vs delta=0.354 矛盾\"}\n    - {round: 34, reviewers: \"R1+R2\", note: \"RESOLVED: 'boundary feature' label + gen-0/gen-1 transition mechanism + k=2 placement\"}\n  action_items:\n    - {round: 32, action: \"Label as boundary feature\", assigned_to: Director, status: done}\n  resolution: \"results.tex L85 'boundary feature' with full qualification; Figure 2 caption aligned.\"\n  resolution_round: 34\n\n- id: \"R32-N3\"\n  summary: \"Tail_decay near-stationary 归类仅 4/8 generator 通过 TOST (epsilon=0.20)\"\n  category: method\n  severity: critical\n  status: in_progress\n  first_raised_round: 32\n  last_seen_round: 36\n  mentions:\n    - {round: 32, reviewers: \"R1\", note: \"50% pass rate; OLMo d=0.22\"}\n    - {round: 34, reviewers: \"R1+R2\", note: \"RESOLVED: L89-91 three-sentence coverage\"}\n    - {round: 35, reviewers: \"R1+R2\", note: \"4/8 TOST 通过率不足; 共识: 主文应更诚实处理 boundary status\"}\n    - {round: 36, reviewers: \"R1+R2\", note: \"共识: tail_decay 应重分类为 'weakly stationary' 或 'inconsistent'; Granger p=0.375 + importance rank 7/7 进一步证实不稳定; 非通过 generators |d|=0.15-0.22 虽远低于 drifting 但不满足 near-stationary\"}\n  action_items:\n    - {round: 32, action: \"Transparent reporting in main text\", assigned_to: Director, status: done}\n    - {round: 35, action: \"验证 <0.5pp claim 溯源; 确认措辞足够诚实\", assigned_to: Agent, status: in_progress}\n    - {round: 36, action: \"主文将 tail_decay 重分类为 weakly stationary 并讨论异质性; 在 Figure 2 中用不同标记区分\", assigned_to: Agent, status: pending}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R32-W1\"\n  summary: \"分类性能 F1=0.694 定位为 detecting 但实为 proof-of-concept\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 32\n  last_seen_round: 34\n  mentions:\n    - {round: 32, reviewers: \"R1+R2\", note: \"~30% 错分率\"}\n    - {round: 34, reviewers: \"R1+R2\", note: \"RESOLVED: Discussion L11 'proof-of-concept, not a deployable system'\"}\n  action_items:\n    - {round: 32, action: \"Discussion proof-of-concept framing\", assigned_to: Director, status: done}\n  resolution: \"Intro L14, Contribution 3, Discussion L11 — all say 'proof-of-concept'.\"\n  resolution_round: 34\n\n- id: \"R32-W2\"\n  summary: \"TOST power analysis 缺失\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 32\n  last_seen_round: 34\n  mentions:\n    - {round: 32, reviewers: \"R1\", note: \"大样本 TOST 几乎总检测 equivalence\"}\n    - {round: 34, reviewers: \"R1+R2\", note: \"共识: SESOI+epsilon+caveat 足够\"}\n  action_items:\n    - {round: 32, action: \"TOST power computation\", assigned_to: Agent, status: wont_fix}\n  resolution: \"SESOI justification + epsilon sensitivity + high-N masking acknowledged.\"\n  resolution_round: 34\n\n- id: \"R32-W3\"\n  summary: \"术语混淆: entropy 指代 NLL 不规范\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 32\n  last_seen_round: 35\n  mentions:\n    - {round: 32, reviewers: \"R2\", note: \"NLL 与 Shannon entropy 不同\"}\n    - {round: 35, reviewers: \"R2\", note: \"再次提出; R1 REBUT: 已有声明且符合领域惯例\"}\n  action_items:\n    - {round: 32, action: \"Existing clarification sufficient\", assigned_to: Director, status: wont_fix}\n  resolution: \"method.tex 3.3 L38 explicit clarification. Round 35 R1 confirms field convention.\"\n  resolution_round: 32\n\n- id: \"R32-W4\"\n  summary: \"附录 25 页过大, 关键结果应在主文讨论\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 32\n  last_seen_round: 32\n  mentions:\n    - {round: 32, reviewers: \"R2\", note: \"25 页附录\"}\n  action_items:\n    - {round: 32, action: \"Key numbers already in main text\", assigned_to: Director, status: wont_fix}\n  resolution: \"QLoRA/instruct numbers in 4.1 and Discussion. Full tables in appendix per 8-page limit.\"\n  resolution_round: 32\n\n- id: \"R32-W5\"\n  summary: \"单一解码策略(nucleus only)\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 32\n  last_seen_round: 36\n  mentions:\n    - {round: 32, reviewers: \"R1+R2\", note: \"greedy/top-k 未验证\"}\n    - {round: 36, reviewers: \"R1+R2\", note: \"升级: nucleus sampling confound 直接关联 DDR 核心新颖性; shape stability 可能是 top-p truncation 的 by-design 结果; 需 greedy/top-k 实验验证\"}\n  action_items:\n    - {round: 32, action: \"Acknowledged as limitation\", assigned_to: Director, status: done}\n    - {round: 36, action: \"补充至少 greedy + top-k 各一个实验验证 shape stability; 或在 Discussion 明确承认 nucleus-sampling-specific\", assigned_to: Agent, status: pending}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R32-W6\"\n  summary: \"3-class F1=0.762 因 gen-0 共享而 misleading\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 32\n  last_seen_round: 32\n  mentions:\n    - {round: 32, reviewers: \"R1+R2\", note: \"gen-0 recall 99.4%\"}\n  action_items:\n    - {round: 32, action: \"Binary F1 is primary in Abstract\", assigned_to: Director, status: wont_fix}\n  resolution: \"Abstract uses binary F1 only; 4.1 notes gen-0 inflation.\"\n  resolution_round: 32\n\n- id: \"R32-W7\"\n  summary: \"特征选取缺乏系统性论证\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 32\n  last_seen_round: 32\n  mentions:\n    - {round: 32, reviewers: \"R1+R2\", note: \"R1 major, R2 降级 warning\"}\n  action_items:\n    - {round: 32, action: \"method.tex explains rationale\", assigned_to: Director, status: done}\n  resolution: \"method.tex 3.3 a priori selection + LOFO validation + richer-features tradeoff note.\"\n  resolution_round: 32\n\n- id: \"R34-W1\"\n  summary: \"Base-model-only scope 限制泛化价值 (结构性)\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 34\n  last_seen_round: 36\n  mentions:\n    - {round: 34, reviewers: \"R1+R2\", note: \"instruct model F1=0.338-0.667. scope limitation 非 fatal flaw\"}\n    - {round: 35, reviewers: \"R1+R2\", note: \"instruct 退化 3.7x; motivation narrative 与 base-only scope 存在张力. Abstract 应更早限定 scope; Discussion curation 场景限定\"}\n    - {round: 36, reviewers: \"R1+R2\", note: \"共识: Appendix K 关键数据 (F1 降 17-21pp, silhouette 0.660→0.372) 应在主文 Discussion 讨论; Abstract/Intro 措辞暗示广泛适用性需修正\"}\n  action_items:\n    - {round: 34, action: \"Rebuttal: base model 是实验控制; QLoRA instruct recovery\", assigned_to: Director, status: done}\n    - {round: 35, action: \"Abstract 加 base-model scope 限定; Introduction reframe synthetic data pipeline; Discussion curation 场景限定\", assigned_to: Agent, status: in_progress}\n    - {round: 36, action: \"主文 Discussion 补充 instruct 退化段落; Intro 第一段明确 base-model scope\", assigned_to: Agent, status: pending}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R34-W2\"\n  summary: \"F1=0.694 性能天花板 (结构性)\"\n  category: experiment\n  severity: warning\n  status: wont_fix\n  first_raised_round: 34\n  last_seen_round: 34\n  mentions:\n    - {round: 34, reviewers: \"R1+R2\", note: \"proof-of-concept 定位缓解期望落差\"}\n  action_items:\n    - {round: 34, action: \"Rebuttal: DDR 贡献是分析框架; LOGO 是最严格下界\", assigned_to: Director, status: done}\n  resolution: \"结构性限制, proof-of-concept 定位已到位.\"\n  resolution_round: 34\n\n- id: \"R34-W3\"\n  summary: \"QLoRA gap (+11.6pp) 未充分解释\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 34\n  last_seen_round: 36\n  mentions:\n    - {round: 34, reviewers: \"R1+R2\", note: \"7 个手工特征丢失大量信号\"}\n    - {round: 35, reviewers: \"R2\", note: \"QLoRA instruct 恢复暗示 DDR 以外信号存在\"}\n    - {round: 36, reviewers: \"R1+R2\", note: \"共识: +11.6pp 比较基于 6-gen subset (XGBoost=0.789) 而非 8-gen LOGO (0.694); 读者容易误读; 需在 Appendix E 和 Discussion 每次引用时标注 '(6-gen subset)'\"}\n  action_items:\n    - {round: 34, action: \"Discussion 补充: token-order dependencies + positional patterns\", assigned_to: Director, status: done}\n    - {round: 35, action: \"修复 +11.6pp baseline 标注不一致 (vs 6-gen not 8-gen)\", assigned_to: Agent, status: in_progress}\n    - {round: 36, action: \"Appendix E + Discussion 所有 QLoRA 引用标注 '(6-gen subset)'; 补报 8-gen LOGO 下 QLoRA 结果\", assigned_to: Agent, status: pending}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R34-V1\"\n  summary: \"Pages 1-4 无任何 display item, 纯文字密度过高\"\n  category: format\n  severity: warning\n  status: open\n  first_raised_round: 34\n  last_seen_round: 36\n  mentions:\n    - {round: 34, reviewers: \"R1+R2\", note: \"Critical visual: 前 4 页纯文字\"}\n    - {round: 35, reviewers: \"Visual Check\", note: \"连续 4 页纯文本; 缺 overview figure; p.7 过密\"}\n    - {round: 36, reviewers: \"R1+R2+Visual Check\", note: \"三方共识: 前 4 页纯文字严重影响 empirical paper 可读性; 建议将 Figure 1 或 method comparison table 前移到 p.2-3\"}\n  action_items:\n    - {round: 34, action: \"Figure 2 前移至 Introduction 末尾\", assigned_to: Director, status: done}\n    - {round: 35, action: \"考虑 pipeline overview figure; 分散 p.7 float\", assigned_to: Director, status: pending}\n    - {round: 36, action: \"将 Figure 1 (strip plot) 前移至 Introduction 末尾或 Method 开头; 或在 Related Work 加入结构化对比表\", assigned_to: Agent, status: pending}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R34-W4\"\n  summary: \"14B entropy_mean |rho|=0.39 跨过 drifting boundary 未明确报告\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 34\n  last_seen_round: 36\n  mentions:\n    - {round: 34, reviewers: \"Reviewer\", note: \"Discussion 只写 'attenuates by 21-35%'\"}\n    - {round: 35, reviewers: \"R1+R2\", note: \"14B 初步证据放正文中读者可能高估. Research Reviewer 建议保留但缩到 1 句\"}\n    - {round: 36, reviewers: \"R1+R2\", note: \"本轮未单独提及，Discussion 中 14B 内容为压缩页数的候选删除对象\"}\n  action_items:\n    - {round: 34, action: \"Discussion 精确化\", assigned_to: Director, status: done}\n    - {round: 35, action: \"缩到 1 句, full results 引用 Appendix\", assigned_to: Agent, status: in_progress}\n  resolution: \"\"\n  resolution_round: null\n\n# === Round 35 Issues ===\n\n- id: \"R35-N1\"\n  summary: \"k=2 聚类在 7 个数据点上做 data-driven validation 方法学不足\"\n  category: method\n  severity: critical\n  status: in_progress\n  first_raised_round: 35\n  last_seen_round: 36\n  mentions:\n    - {round: 35, reviewers: \"R1+R2\", note: \"共识: 7 点 k-means 近 trivial; silhouette 不具统计意义; Appendix V generator-split 更有说服力\"}\n    - {round: 36, reviewers: \"R1+R2\", note: \"R1 维持 critical (描述性非推断性, p=0.030 仅边际显著); R2 降级为 major (generator-split/holdout/ε-stability 三重验证已相当充分); 共识: 补充 gap statistic 或 sample-level bootstrap 可强化论证\"}\n  action_items:\n    - {round: 35, action: \"Abstract/Intro 下调 data-driven; §4.2 提升 generator-split consistency 为 primary validation; permutation test 补充\", assigned_to: Agent, status: in_progress}\n    - {round: 36, action: \"补充 gap statistic / prediction strength 替代 silhouette; 考虑 sample-level bootstrap 重采样验证聚类稳定性\", assigned_to: Agent, status: pending}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R35-N2\"\n  summary: \"与 Markovian Chains (Geng et al., 2026) 区分度不足\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 35\n  last_seen_round: 36\n  mentions:\n    - {round: 35, reviewers: \"R1+R2\", note: \"共识: setup 重叠度高; 当前区分仅一句话; 需系统性对比表\"}\n    - {round: 36, reviewers: \"R1+R2\", note: \"本轮未作为独立 issue 单独提出; R1 交叉回应中引用 Table 41 (Appendix Z.6) 作为已有缓解; Related Work §2.2 最后一段有对比讨论\"}\n  action_items:\n    - {round: 35, action: \"WebSearch 补全细节 + §2.2 加系统对比表 (chain type / feature space / 目标 / scale / insight)\", assigned_to: Agent, status: in_progress}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R35-W1\"\n  summary: \"Five 'independent' effect-size metrics overclaim\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 35\n  last_seen_round: 36\n  mentions:\n    - {round: 35, reviewers: \"R1+R2\", note: \"共识: Cohen's d ~ Glass's Delta ~ KS 高度相关; 真正独立的仅 Cliff's delta 和 CV shift\"}\n    - {round: 36, reviewers: \"R1+R2\", note: \"共识: 'five complementary' 仍有 overclaim 嫌疑; 建议改为 'convergence across parametric and non-parametric measures'; 补充度量间相关矩阵\"}\n  action_items:\n    - {round: 35, action: \"'five independent' → 'five complementary'; 区分 parametric overlap 与 genuinely independent perspectives\", assigned_to: Agent, status: in_progress}\n    - {round: 36, action: \"Abstract/§4.2 措辞改为 'convergence across parametric and non-parametric measures'; Appendix 补充 inter-measure 相关矩阵\", assigned_to: Agent, status: pending}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R35-W2\"\n  summary: \"TOST epsilon=0.20 循环论证\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 35\n  last_seen_round: 36\n  mentions:\n    - {round: 35, reviewers: \"R1+R2\", note: \"共识: 先按 d<0.20 分类 → LOFO 验证 → 用 LOFO justify epsilon. Mitigating: Cohen (1988) conventional threshold\"}\n    - {round: 36, reviewers: \"R1+R2\", note: \"R1 维持 critical; R2 部分反驳 (Table 30 证明核心分区在 ε∈[0.10,0.75] 内不变); 共识: Cohen 惯例有合理基础但需补充 downstream task 角度的独立正当性\"}\n  action_items:\n    - {round: 35, action: \"承认 epsilon=0.20 是 conventional; 主文引用 Appendix V epsilon robustness\", assigned_to: Agent, status: in_progress}\n    - {round: 36, action: \"从分类 F1 角度反推 SESOI (操作上可忽略的最小效应); 或绘制 equivalence frontier 图\", assigned_to: Agent, status: pending}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R35-W3\"\n  summary: \"Downstream null result 未在主文 Discussion 讨论\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 35\n  last_seen_round: 36\n  mentions:\n    - {round: 35, reviewers: \"R1+R2\", note: \"共识: Appendix M TOST equivalence 未在 Discussion 提及; selective reporting concern; reframe 为 provenance/audit\"}\n    - {round: 36, reviewers: \"R1+R2\", note: \"共识: Discussion 中仅一句带过不充分; 需专门段落讨论 null result 含义、为什么 depth signal 不能转化下游收益、在什么条件下可能产生差异\"}\n  action_items:\n    - {round: 35, action: \"Discussion 加一段承认 null result; reframe value 为 provenance/audit\", assigned_to: Agent, status: in_progress}\n    - {round: 36, action: \"Discussion 增加专门段落讨论 downstream null result 的机制解释和边界条件\", assigned_to: Agent, status: pending}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R35-W4\"\n  summary: \"Abstract 中 binary F1=0.694 定义模糊\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 35\n  last_seen_round: 36\n  mentions:\n    - {round: 35, reviewers: \"R1+R2\", note: \"共识: 未明确 binary 指 gen-1 vs gen-2+, 非 human vs machine\"}\n    - {round: 36, reviewers: \"R2\", note: \"Abstract 声称的定义在 §4.1 中有明确解释，基本一致\"}\n  action_items:\n    - {round: 35, action: \"Abstract 加 '(gen-1 vs gen-2+, excluding shared gen-0 seeds)'\", assigned_to: Agent, status: in_progress}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R35-M3\"\n  summary: \"Bootstrap CI 不反映 generator selection uncertainty\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 35\n  last_seen_round: 36\n  mentions:\n    - {round: 35, reviewers: \"R1\", note: \"per-generator F1 span 9.1pp 未区分于 sampling CI\"}\n    - {round: 36, reviewers: \"R1+R2\", note: \"共识: bootstrap CI 宽度仅 4.8pp 但 per-generator range 达 28.8pp; Pythia 系列系统性高于其他 family; 需补充 generator-level variance 统计量 (SD/IQR) 与 bootstrap CI 并列报告\"}\n  action_items:\n    - {round: 35, action: \"§4.1 加一句区分 sampling CI 和 generalization variability\", assigned_to: Agent, status: in_progress}\n    - {round: 36, action: \"Table 1 或正文补充 across-generator SD; 讨论 hierarchical bootstrap 或 generator-level variance\", assigned_to: Agent, status: pending}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R35-M4\"\n  summary: \"Chain depth=4 选择未在主文 justify\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 35\n  last_seen_round: 36\n  mentions:\n    - {round: 35, reviewers: \"R1\", note: \"depth=4 的选择未解释\"}\n    - {round: 36, reviewers: \"R1+R2\", note: \"本轮未单独提及; §3.2 已有 justification (depth 2-4 indistinguishable → gen-2+ collapse)\"}\n  action_items:\n    - {round: 35, action: \"§3.2 加 depth=4 justification, 引用 finer-grained analysis appendix\", assigned_to: Agent, status: in_progress}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R35-M5\"\n  summary: \"5 条 bib entries first_author mismatch\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 35\n  last_seen_round: 36\n  mentions:\n    - {round: 35, reviewers: \"R2\", note: \"LaTeX 编码 vs API 索引差异导致 first_author mismatch\"}\n    - {round: 36, reviewers: \"R1+R2\", note: \"R1 确认 5 个 mismatch 均为编码差异 (Team vs 具体作者名), 非实质性错误; 0 orphan, 0 missing\"}\n  action_items:\n    - {round: 35, action: \"待定位具体 5 条 entries 后修复\", assigned_to: Agent, status: pending}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R35-E1\"\n  summary: \"+11.6pp 标注 baseline 不一致 (vs 6-gen 而非 8-gen)\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 35\n  last_seen_round: 36\n  mentions:\n    - {round: 35, reviewers: \"Research Reviewer\", note: \"+11.6pp = 0.905-0.789 (vs 6-gen), 非 0.905-0.762 (vs 8-gen). 读者计算 14.3pp ≠ 11.6pp 会困惑\"}\n    - {round: 36, reviewers: \"R1+R2\", note: \"共识: 跨子集 delta 容易误导; 需在每次引用时标注 (6-gen subset)\"}\n  action_items:\n    - {round: 35, action: \"+11.6pp 后加 '(vs 6-gen XGBoost; Table 2)'\", assigned_to: Agent, status: in_progress}\n    - {round: 36, action: \"与 R34-W3 合并处理: 所有 QLoRA 引用标注子集信息\", assigned_to: Agent, status: pending}\n  resolution: \"\"\n  resolution_round: null\n\n# === Round 36 新 Issues ===\n\n- id: \"R36-N1\"\n  summary: \"主文页数超过 EMNLP 8 页限制 (约 8.5-8.7 页)\"\n  category: format\n  severity: critical\n  status: open\n  first_raised_round: 36\n  last_seen_round: 36\n  mentions:\n    - {round: 36, reviewers: \"R1+R2+Visual Check\", note: \"三方独立确认: Discussion 跨 p.8-p.9, Conclusion 在 p.9; 主文合计约 8.5-8.7 页; 格式违规可导致 desk reject\"}\n  action_items:\n    - {round: 36, action: \"压缩 Discussion 从 ~1.3 页至 ~0.8 页 (model collapse 区分、14B 结果、温度重复论述移至附录); 压缩 Conclusion\", assigned_to: Agent, status: pending}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R36-W1\"\n  summary: \"3-class 粒度的实际价值论证不足\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 36\n  last_seen_round: 36\n  mentions:\n    - {round: 36, reviewers: \"R2\", note: \"3-class vs binary 的增量价值缺乏令人信服的 use case; R1 部分同意但认为科学价值独立于即时应用\"}\n  action_items:\n    - {round: 36, action: \"Discussion 补充 1-2 个量化 use case (如 training data audit 中 gen-1 vs gen-2+ 的不同处理策略)\", assigned_to: Agent, status: pending}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R36-W2\"\n  summary: \"Reference model (Pythia-410M) same-family confound 主文讨论不足\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 36\n  last_seen_round: 36\n  mentions:\n    - {round: 36, reviewers: \"R1+R2\", note: \"共识: Pythia generators F1 系统性高于其他 family (0.718-0.724 vs avg ~0.66); Appendix S cross-family 验证有效但主文仅一笔带过; 需分 generator 报告 reference model 切换影响\"}\n  action_items:\n    - {round: 36, action: \"§3.3 或 §5 补充 reference model bias 讨论; 考虑分 generator 报告 cross-reference 影响\", assigned_to: Agent, status: pending}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R36-R1\"\n  summary: \"缺少 Tulchinskii et al. (2024) 'Intrinsic Dimension Estimation' (ICLR 2024) 引用\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 36\n  last_seen_round: 36\n  mentions:\n    - {round: 36, reviewers: \"R1+R2\", note: \"两位 Reviewer 独立建议补充; 使用几何/拓扑特征检测 AI 文本, 与本文 distributional statistics 方法互补\"}\n  action_items:\n    - {round: 36, action: \"§2.1 Related Work 补充引用\", assigned_to: Agent, status: pending}\n  resolution: \"\"\n  resolution_round: null"
  }
}
```

</details>

---


### Tool result

_source line 2767 · 2026-05-21T03:58:29.771109+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/review_issues.yaml\", \"bytes\": 28528}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 2768 · 2026-05-21T04:01:20.458152+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "report": "# Round 36 审稿报告 — Depth Fingerprinting: Detecting Recursive Generation Depth in LLM Text Chains\n\n**Venue**: EMNLP 2026 (ARR) | **Deadline**: 2026-05-25 | **审稿模式**: Fresh (初审)\n**Reviewer 编排**: R1 (方法严谨性) + R2 (新颖性/完整性) | **轮次**: 1 轮 + 交叉回应\n\n---\n\n## Summary\n\n论文提出 \"depth fingerprinting\"：将 AI 文本检测从二分类扩展到序数深度估计（gen-0/gen-1/gen-2+），核心发现为 differential depth response (DDR)——在 8 个 base-model generator（5 个架构家族, 0.6B-8B）的递归生成链中，NLL 位置统计量单调漂移而分布形状特征保持稳定。基于 DDR 的 7 特征 ensemble 在 leave-one-generator-out 评估下达到 binary F1=0.694；端到端 QLoRA 分类器达到 0.905。\n\n---\n\n## Strengths\n\n1. **新颖的问题定义** [R1+R2 共识]：从 binary detection 到 ordinal depth classification 是自然且有意义的延伸，在 data provenance 和 model collapse 预防中有清晰的应用场景。\n2. **DDR 分解有洞察力** [R1+R2 共识]：location/shape 分离——drifting features 单调漂移而 shape features 近似不变——是一个有趣的实证发现，为理解 LLM 递归生成的分布演化提供了新视角。\n3. **实验覆盖面极广且预判到位** [R1+R2 共识]：17+ 项补充实验（TOST、LOFO、cross-domain、temperature、prompt type、instruction tuning、QLoRA、Granger causality、transfer、perturbation robustness 等），24 页附录系统性回答了大部分可预见质疑。\n4. **泄露控制设计严谨** [R1]：三重机制——leak-free binary F1、seed-level demeaning (F1=0.701)、independent-seed control (F1=0.680)——差距仅 1.4pp，令人信服。\n5. **诚实的 proof-of-concept 定位** [R2]：论文没有过度宣传分类性能，明确承认 ~30% 错分率和范围限制。\n6. **与 baseline 的公平对比** [R1+R2 共识]：Table 2 使用相同 XGBoost pipeline 和 LOGO 协议，方法论公平。\n7. **引用规范** [R2]：66 条引用，0 orphan，0 phantom，覆盖 2019-2026 文献。\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**N1** [Critical | R1+R2+Visual Check 三方共识] **主文页数超过 EMNLP 8 页限制**\n- Discussion 跨 page 8-9（约 1.3 页），Conclusion 在 page 9 约 20%，主文合计约 8.5-8.7 页。\n- EMNLP 2026 严格限制主文 8 页（Limitations/Ethics 不计入）。格式违规可导致 desk reject。\n- **修复方向**：压缩 Discussion 至 ~0.8 页（model collapse 区分、14B 初步结果、温度重复论述可移至附录）。\n\n**N2** [Critical | R2 提出, R1 部分同意] **DDR 核心新颖性的 nucleus sampling confound**\n- DDR 的 shape stability（entropy_max, tail_decay 稳定）可能是 nucleus sampling 在固定 p=0.9 下截断的 by-design 结果。Discussion (p.8) 原文 \"top-p truncation selects from a fixed probability mass fraction...preserving the functional form\" 恰恰暗示这是采样机制的数学性质。\n- 论文**仅在 nucleus sampling 框架内**变化温度，未测试 greedy decoding、pure top-k、beam search。如果 shape stability 在非 nucleus sampling 下不成立，DDR 框架的泛化性和新颖性将显著缩水——变成 \"nucleus sampling 的已知属性 + 已知的 diversity loss\"。\n- **R1 交叉回应中的关键判断**：\"问题不仅是温度范围窄，而是整个 decoding paradigm 的覆盖缺失\"，建议升级为 must-fix 级补充实验。\n- **R2 的核心论点**：drifting features（entropy_mean↓, TTR↓, hapax↓）本质上是 model collapse 文献中已记录的 diversity loss / entropy erosion；论文声称的新颖性在于 \"what is preserved\"，但如果 preservation 是采样机制的固有属性，增量贡献有限。\n- **R1 的部分反驳**：location/shape 分离作为 decomposition 在 model collapse 文献中未被报告，且正是有 stable reference 才使 cross-generator depth detection 成为可能——DDR ≠ diversity loss 的简单重述。\n- **分歧状态**：R1 认为 location/shape 分离有独立贡献但同意需要实验验证；R2 认为增量性更强。两人均同意 nucleus sampling confound 需要至少 greedy + top-k 验证实验。\n- **修复方向**：(1) 补充 greedy/top-k 下 shape stability 验证；(2) 或明确承认 nucleus-sampling-specific 并精准界定增量贡献。\n\n**N3** [Critical→Major, R1 提出, R2 降级] **k=2 聚类在 n=7 特征点上统计效力不足**\n- DDR 分区依赖 k-means 在 7 个数据点上的聚类（silhouette=0.660），本质上是描述性的而非推断性的。排列检验 p=0.030 仅边际显著。\n- **缓解证据**（R2 指出，R1 同意其存在但认为不充分）：generator-split validation 两组独立产生完全相同分区；holdout split 中 zone assignment 完全一致；跨 ε 稳定性在 [0.10, 0.75] 内核心分区不变。\n- **严重性分歧**：R1 维持 critical（描述性非推断性），R2 降级为 major（三重验证已相当充分）。\n- **综合判断**：降为 **Major**——现有 validation 支撑 descriptive claim，但 inferential rigor 有提升空间。\n- **修复方向**：补充 gap statistic 或 prediction strength；考虑 sample-level bootstrap 验证聚类稳定性。\n\n**N4** [Critical→Major, R1 提出, R2 同意] **TOST 中 tail_decay 仅 4/8 generator 通过——\"near-stationary\" 名不副实**\n- tail_decay 在 ε=0.20 下仅 4/8 generator 通过 TOST；非通过 generators |d|=0.15-0.22。Granger causality p=0.375，permutation importance rank 7/7（最低）——均指向 \"noisy/inconsistent\" 而非 \"near-stationary\"。\n- R1 和 R2 均同意应重分类。DDR 三分区（3/1/3）中 near-stationary 组有 1/3 不稳定，削弱框架清晰度。\n- **修复方向**：主文将 tail_decay 重分类为 \"weakly stationary\"；补充移除 tail_decay 后的分类和分区 sensitivity analysis；Figure 2 中用不同标记区分。\n\n**N5** [Critical→Major, R1 提出, R2 部分反驳] **ε=0.20 等价阈值缺乏问题特定正当性**\n- Cohen's d=0.20 是行为科学通用惯例，未论证在生成深度检测中的合理性。\n- **R2 反驳要点**：Table 30 证明核心分区在 ε∈[0.10, 0.75] 内完全不变——\"分区结果是阈值函数\" 仅适用于 entropy_std 的归属，不适用于核心 drifting/stationary 分区。\n- **综合判断**：降为 **Major**——核心分区对 ε 高度稳定，但补充 task-specific justification 会增强论证。\n- **修复方向**：从分类 F1 角度反推 SESOI（操作上可忽略的最小效应）；或绘制 equivalence frontier 图。\n\n### Should-Fix（影响评分但不一票否决）\n\n**W1** [Major | R1+R2 共识] **Base-model-only 范围限制实际适用性**\n- Appendix K 显示 instruction-tuned models 3-class F1 降至 0.575/0.544（降幅 17-21pp），DDR silhouette 从 0.660 降至 0.372。2025-2026 年绝大多数部署 LLM 都是 instruction-tuned。\n- Abstract/Introduction 措辞 (\"When LLM outputs re-enter generation pipelines\") 暗示广泛适用性，与 base-model-only 范围存在张力。\n- **修复方向**：Discussion 增加专门段落讨论 instruct 退化机制；Introduction 第一段明确 scope。\n\n**W2** [Major | R2 提出, R1 同意] **Downstream null result 在主文中讨论不充分**\n- Appendix M 的 TOST 明确显示 depth-aware curation ≈ random subsampling。这直接关系到 Introduction 中 \"data provenance matters\" 的动机。Discussion 仅用一句话带过。\n- **修复方向**：Discussion 增加专门段落讨论 null result 含义、为什么 depth signal 不能转化下游收益、在什么条件下可能有差异；重新定位价值为 provenance/audit 而非 curation。\n\n**W3** [Major | R1 提出, R2 同意] **QLoRA +11.6pp 基线比较跨子集不一致**\n- +11.6pp 基于 6-gen subset (XGBoost baseline=0.789)，而主文 Table 1 的 8-gen LOGO binary F1=0.694。两个基线相差 9.5pp。Discussion 引用 \"QLoRA recovers 0.905\" 时未标注是 6-gen 结果，读者容易误读。\n- **修复方向**：所有 QLoRA 引用标注 \"(6-gen subset)\"；补报 8-gen LOGO 下 QLoRA 结果。\n\n**W4** [Major | R1 提出, R2 同意] **Bootstrap CI 未捕获 generator-level 方差**\n- 8-gen LOGO macro F1=0.762，95% CI 宽度仅 4.8pp。但 per-generator binary F1 range 达 9.1pp (0.633-0.724)。Pythia 系列系统性高于其他 family，可能反映 Pythia-410M 参考模型的 same-family 优势。\n- **修复方向**：补充 across-generator SD/IQR 与 bootstrap CI 并列报告；讨论 same-family reference bias。\n\n**W5** [Minor-Major | R1+R2+Visual Check 共识] **前 4 页无任何图表，信息密度不均**\n- 作为 empirical paper，前 4 整页纯文字，首个视觉元素 (Table 1) 在 page 5，Figure 1 在 page 6。Related Work 1.5+ 页无结构化对比。\n- **修复方向**：将 Figure 1 (strip plot) 前移至 Introduction 末尾或 Method 开头；Related Work 加入 method comparison table。\n\n**W6** [Minor | R1 提出, R2 部分同意] **五种 effect-size measures 的 \"complementarity\" 过度宣称**\n- Cohen's d 和 Glass's Δ 在组间方差接近时高度相关；KS 在 location shift 主导时也与 Cohen's d 强相关。\"五重验证\" 可能过度膨胀置信度。\n- **修复方向**：改为 \"convergence across parametric and non-parametric measures\"；补充 inter-measure 相关矩阵。\n\n**W7** [Minor | R1+R2 共识] **Reference model (Pythia-410M) same-family confound 主文讨论不足**\n- 8 个 generator 中 2 个来自 Pythia family，reference model 同家族。Appendix S 验证了 cross-family reference 信号保持（spread 0.013），但主文仅一笔带过。\n- **修复方向**：§3.3 或 §5 补充 reference model bias 讨论；分 generator 报告 cross-reference 影响。\n\n---\n\n## Reviewer Consensus [AGREE]\n\n1. **页数超限** (~8.5 页) 需立即修复——desk reject 风险\n2. **tail_decay 应重分类**——4/8 TOST 通过率不支持 \"near-stationary\" 标签\n3. **Base-model-only 限制**需在主文更显著讨论\n4. **QLoRA +11.6pp 跨子集不一致**需标注子集信息\n5. **Bootstrap CI + generator-level variance** 需补充报告\n6. **Downstream null result** 需在 Discussion 获得更充分讨论\n7. **前 4 页无图表**需改善信息密度分布\n8. **Proof-of-concept 定位总体良好**，论文在大多数位置保持一致\n9. **引用质量良好**（66 条, 0 orphan, 0 missing），建议补充 Tulchinskii et al. (2024)\n\n## Reviewer Divergence [REBUT]\n\n1. **DDR 新颖性** [核心分歧]\n   - R1 (3.5): location/shape 分离是新贡献，在 model collapse 文献中未见——DDR ≠ diversity loss 的简单重述；即使需更强验证，decomposition 本身有独立价值\n   - R2 (3.0): drifting features 本质是已知的 diversity loss，shape stability 可能是 nucleus sampling 的 trivial 推论，增量贡献有限\n   - **两人共识**：无论如何，nucleus sampling confound 需要实验验证（greedy/top-k）\n\n2. **k=2 聚类严重性**\n   - R1: critical（描述性非推断性，p=0.030 仅边际显著）\n   - R2: major（generator-split/holdout/ε-stability 三重验证已相当充分）\n\n3. **ε=0.20 循环论证严重性**\n   - R1: critical（缺乏 domain-specific justification）\n   - R2: major（Table 30 证明核心分区对 ε 高度稳定，\"循环论证\" 判断过重）\n\n4. **3-class 粒度的价值**\n   - R1: 科学价值独立于即时应用，证明 depth 可检测本身就是贡献\n   - R2: 缺乏量化 use case，增量价值论证不足\n\n---\n\n## Questions\n\n1. Shape stability 是否在 greedy decoding / pure top-k 下同样成立？如果仅在 nucleus sampling 下成立，如何论证这不是 sampling truncation 的 trivial 推论？[R1+R2]\n2. Downstream null result (Appendix M) 表明 depth-aware curation ≈ random subsampling。在什么条件下预期 depth signal 能转化为实际 downstream benefit？[R2]\n3. 增加更多特征（n-gram diversity, 句法复杂度, discourse coherence）后 DDR 的 drifting/stationary 二分是否仍成立？当前 7 特征中 5 个基于 token-level NLL，特征空间局限性是否预设了分区结果？[R1]\n4. Instruction-tuned 下 silhouette 降至 0.372——DDR 框架的 drifting/stationary 分离前提是否在 instruction-tuned 模型下不再成立？这是否意味着论文的理论贡献局限于 base models？[R1+R2]\n5. 使用 2.8B/7B 参考模型是否会改变 DDR 分区本身（不仅是分类 F1）？Appendix S 未报告此项。[R1]\n6. 是否尝试过从分类 F1 角度反推 ε（操作上可忽略的最小效应）？[R1]\n7. 是否尝试过在 instruction-tuned chain 上重新训练分类器（而非 base-trained 分类器直接迁移）？[R2]\n\n---\n\n## Missing References\n\n以下由两位 Reviewer 独立建议：\n1. **Tulchinskii et al. (2024)** \"Intrinsic Dimension Estimation for Robust Detection of AI-Generated Texts\" (ICLR 2024) — R1+R2 共同建议，使用几何/拓扑特征检测 AI 文本，与本文 distributional statistics 方法互补\n2. **RADAR (Hu et al., 2023)** — R2 建议，adversarial training-based detector\n3. 代码域检测先前工作 — R1 建议，论文在 Appendix J 测试了 Code 域但未引用相关文献\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n**状态**: 已跳过（用户未提交）\n\n---\n\n## Visual Layout Check（非评分项）\n\n**状态**: 完成 | 4 warnings, 14 info\n\n**关键发现**：\n- **[Warning]** Pages 1-4 连续纯文本，无任何 display item。审稿人需翻到 page 5 才看到第一个视觉锚点 (Table 1)。建议将 Figure 1 (strip plot) 前移至 page 2-3。\n- **[Warning]** 第一个 display item 出现在 page 5，Figure 1 在 page 6——审稿人在前 2 分钟内无法建立核心发现的视觉认知。\n- **[Warning]** Discussion 跨 page 8-9，约 1.5 页连续纯文本。结合前面 pages 1-4 的纯文本段，全文 \"文本墙\" 比例偏高。\n- **[Warning]** 主文延伸至 page 9 约 2/3 处，约 8.7 页，可能超页。\n- **[Info]** Table 1/2 格式规范（booktabs, 加粗最优结果）。Figure 2+3+Table 2 在 page 7 密度适当。Figure 7 (base vs instruct DDR) 颜色清晰。Figure 1 strip plot 中 8 色在黑白/色弱条件下可能难以区分，建议添加 marker shape。Appendix 中 page 15 (Figure 4) 底部约 1/4 空白、page 25 (Figure 8) 子面板字号偏小（约正文 60%）。\n\n---\n\n## Overall Assessment\n\n**综合评分: 3.0 (Findings)**\n**置信度: 4/5**\n\n| 维度 | R1 | R2 | 综合 |\n|------|-----|-----|------|\n| Soundness | 3/5 | 3.5/5 | 3/5 |\n| Excitement | 3.5/5 | 2.5/5 | 3/5 |\n| Reproducibility | 4/5 | 4/5 | 4/5 |\n| Overall | 3.5 | 3.0 | 3.0 |\n\n**评分理由**：\n\n论文在实验执行和统计方法上高于平均水准，DDR 的 location/shape 分解角度有一定新意，问题定义从 binary 到 ordinal 是有意义的延伸。但以下因素将评分压至 Findings 水平：\n\n1. **格式违规** (N1): 主文约 8.5-8.7 页，超过 8 页限制，存在 desk reject 风险。这是可修复的但当前状态下是硬伤。\n2. **核心新颖性存疑** (N2): shape stability 可能是 nucleus sampling 的 by-design 属性——论文未提供非 nucleus sampling 的验证实验，而 Discussion 原文恰恰暗示了这一机制解释。如果这一质疑成立，DDR 的 \"novel observation\" 将缩水为 \"nucleus sampling + 已知 diversity loss\"。R1 认为 location/shape 分离本身有独立贡献 (3.5)，R2 认为增量性更强 (3.0)——这是评分差异的核心来源。\n3. **统计框架的方法论短板** (N3-N5): k=2 聚类在 n=7 上虽有辅助验证但统计效力先天不足；tail_decay \"near-stationary\" 标签不准确（4/8 TOST）；ε=0.20 缺乏 domain-specific justification。这些单独看是可修复的 major 问题，但累积起来削弱了 DDR 分析框架的 methodological rigor。\n4. **实际影响力受限**: base-model-only scope + downstream null result + 3-class 粒度限制了论文的应用前景。\n\n**如果以下条件满足，评分可提升至 3.5 (Borderline Conference)**：\n- 修复页数超限\n- 补充 greedy/top-k 下 shape stability 验证（或令人信服地论证为何 nucleus-sampling-specific 仍有独立贡献）\n- 修正 tail_decay 分类标签\n- Discussion 充分讨论 instruct 退化和 downstream null result\n\n---\n\n## Detailed Comments\n\n### Section 1 (Introduction)\n- 开头 \"When LLM outputs re-enter generation pipelines\" 暗示广泛适用性，但论文仅覆盖 base model continuation chains。建议第一段明确 scope。\n- Contribution 列表从 3 条缩减到 2 条 + 一个 \"additionally provide\"——结构清晰但 \"additionally\" 部分读起来像第三个贡献。\n- R2-Q5: 为什么选 continuation chain 而非 paraphrase chain？R1 引用 Appendix Z.6 Table 41 解释了方法论原因（语义自由度更高），但主文未讨论此设计选择。\n\n### Section 2 (Related Work)\n- §2.2 最后一段对 Broken Telephone / Markovian Chains 的区分较好，但 R2 认为仍可加入结构化对比表以增强说服力。\n- 缺 Tulchinskii et al. (2024) [R1+R2 共识]。\n\n### Section 3 (Method)\n- §3.3 \"entropy as shorthand for NLL\" 声明存在但可考虑更精确的措辞（R2 minor）。\n- §3.4 \"LOGO family-level\" 行定义需澄清——是 per-generator 还是 per-family leave-one-out（R1 minor）。\n- Reference model 选择的潜在偏差应在此处或 §5 明确讨论。\n\n### Section 4 (Results)\n- §4.1: bootstrap CI [0.758, 0.766] 宽度仅 0.8pp，而 per-generator spread 9.1pp。需补充 generator-level variance。\n- §4.2: \"five complementary effect-size measures\" → 建议改为 \"convergence across parametric and non-parametric measures\"。\n- §4.2: tail_decay 的 4/8 TOST 在主文已有三句覆盖 (L89-91)，但 \"near-stationary\" 标签仍过于宽泛。\n- §4.3: Table 2 显示 4-det+surface (0.708) > 7-feature (0.705)——论文诚实报告，DDR 贡献定位为 decomposition 而非 classification performance。\n\n### Section 5 (Discussion)\n- 篇幅过长（~1.3 页），是页数超限的主要原因。\n- 14B preliminary results 可移至附录。\n- Model collapse 区分的讨论虽重要但可精简。\n- Downstream null result 仅一句话——需扩展。\n- QLoRA \"0.905\" 引用未标注 6-gen subset。\n\n### Section 6 (Conclusion)\n- \"preliminary 14B evidence confirms the partition\" 用词偏强——14B 是 preliminary 且仅 1 个模型。\n- 可适当压缩。\n\n### R1 事实纠正\nR1-W5 声称 \"缺 t=1.0\"，但 Table 10 (Appendix H) 明确测试了 t∈{0.5, 0.7, 1.0}。R2 在交叉回应中纠正了此事实错误。温度覆盖度限制在于仅 4/8 generator 参与温度实验，而非缺少特定温度点。",
  "project": "gen-depth-fingerprint",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "3.0 (Findings)",
  "review_chat_id": "oc_999770e4e57bfc6eabd12fc1f64af1ef"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "report": "# Round 36 审稿报告 — Depth Fingerprinting: Detecting Recursive Generation Depth in LLM Text Chains\n\n**Venue**: EMNLP 2026 (ARR) | **Deadline**: 2026-05-25 | **审稿模式**: Fresh (初审)\n**Reviewer 编排**: R1 (方法严谨性) + R2 (新颖性/完整性) | **轮次**: 1 轮 + 交叉回应\n\n---\n\n## Summary\n\n论文提出 \"depth fingerprinting\"：将 AI 文本检测从二分类扩展到序数深度估计（gen-0/gen-1/gen-2+），核心发现为 differential depth response (DDR)——在 8 个 base-model generator（5 个架构家族, 0.6B-8B）的递归生成链中，NLL 位置统计量单调漂移而分布形状特征保持稳定。基于 DDR 的 7 特征 ensemble 在 leave-one-generator-out 评估下达到 binary F1=0.694；端到端 QLoRA 分类器达到 0.905。\n\n---\n\n## Strengths\n\n1. **新颖的问题定义** [R1+R2 共识]：从 binary detection 到 ordinal depth classification 是自然且有意义的延伸，在 data provenance 和 model collapse 预防中有清晰的应用场景。\n2. **DDR 分解有洞察力** [R1+R2 共识]：location/shape 分离——drifting features 单调漂移而 shape features 近似不变——是一个有趣的实证发现，为理解 LLM 递归生成的分布演化提供了新视角。\n3. **实验覆盖面极广且预判到位** [R1+R2 共识]：17+ 项补充实验（TOST、LOFO、cross-domain、temperature、prompt type、instruction tuning、QLoRA、Granger causality、transfer、perturbation robustness 等），24 页附录系统性回答了大部分可预见质疑。\n4. **泄露控制设计严谨** [R1]：三重机制——leak-free binary F1、seed-level demeaning (F1=0.701)、independent-seed control (F1=0.680)——差距仅 1.4pp，令人信服。\n5. **诚实的 proof-of-concept 定位** [R2]：论文没有过度宣传分类性能，明确承认 ~30% 错分率和范围限制。\n6. **与 baseline 的公平对比** [R1+R2 共识]：Table 2 使用相同 XGBoost pipeline 和 LOGO 协议，方法论公平。\n7. **引用规范** [R2]：66 条引用，0 orphan，0 phantom，覆盖 2019-2026 文献。\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**N1** [Critical | R1+R2+Visual Check 三方共识] **主文页数超过 EMNLP 8 页限制**\n- Discussion 跨 page 8-9（约 1.3 页），Conclusion 在 page 9 约 20%，主文合计约 8.5-8.7 页。\n- EMNLP 2026 严格限制主文 8 页（Limitations/Ethics 不计入）。格式违规可导致 desk reject。\n- **修复方向**：压缩 Discussion 至 ~0.8 页（model collapse 区分、14B 初步结果、温度重复论述可移至附录）。\n\n**N2** [Critical | R2 提出, R1 部分同意] **DDR 核心新颖性的 nucleus sampling confound**\n- DDR 的 shape stability（entropy_max, tail_decay 稳定）可能是 nucleus sampling 在固定 p=0.9 下截断的 by-design 结果。Discussion (p.8) 原文 \"top-p truncation selects from a fixed probability mass fraction...preserving the functional form\" 恰恰暗示这是采样机制的数学性质。\n- 论文**仅在 nucleus sampling 框架内**变化温度，未测试 greedy decoding、pure top-k、beam search。如果 shape stability 在非 nucleus sampling 下不成立，DDR 框架的泛化性和新颖性将显著缩水——变成 \"nucleus sampling 的已知属性 + 已知的 diversity loss\"。\n- **R1 交叉回应中的关键判断**：\"问题不仅是温度范围窄，而是整个 decoding paradigm 的覆盖缺失\"，建议升级为 must-fix 级补充实验。\n- **R2 的核心论点**：drifting features（entropy_mean↓, TTR↓, hapax↓）本质上是 model collapse 文献中已记录的 diversity loss / entropy erosion；论文声称的新颖性在于 \"what is preserved\"，但如果 preservation 是采样机制的固有属性，增量贡献有限。\n- **R1 的部分反驳**：location/shape 分离作为 decomposition 在 model collapse 文献中未被报告，且正是有 stable reference 才使 cross-generator depth detection 成为可能——DDR ≠ diversity loss 的简单重述。\n- **分歧状态**：R1 认为 location/shape 分离有独立贡献但同意需要实验验证；R2 认为增量性更强。两人均同意 nucleus sampling confound 需要至少 greedy + top-k 验证实验。\n- **修复方向**：(1) 补充 greedy/top-k 下 shape stability 验证；(2) 或明确承认 nucleus-sampling-specific 并精准界定增量贡献。\n\n**N3** [Critical→Major, R1 提出, R2 降级] **k=2 聚类在 n=7 特征点上统计效力不足**\n- DDR 分区依赖 k-means 在 7 个数据点上的聚类（silhouette=0.660），本质上是描述性的而非推断性的。排列检验 p=0.030 仅边际显著。\n- **缓解证据**（R2 指出，R1 同意其存在但认为不充分）：generator-split validation 两组独立产生完全相同分区；holdout split 中 zone assignment 完全一致；跨 ε 稳定性在 [0.10, 0.75] 内核心分区不变。\n- **严重性分歧**：R1 维持 critical（描述性非推断性），R2 降级为 major（三重验证已相当充分）。\n- **综合判断**：降为 **Major**——现有 validation 支撑 descriptive claim，但 inferential rigor 有提升空间。\n- **修复方向**：补充 gap statistic 或 prediction strength；考虑 sample-level bootstrap 验证聚类稳定性。\n\n**N4** [Critical→Major, R1 提出, R2 同意] **TOST 中 tail_decay 仅 4/8 generator 通过——\"near-stationary\" 名不副实**\n- tail_decay 在 ε=0.20 下仅 4/8 generator 通过 TOST；非通过 generators |d|=0.15-0.22。Granger causality p=0.375，permutation importance rank 7/7（最低）——均指向 \"noisy/inconsistent\" 而非 \"near-stationary\"。\n- R1 和 R2 均同意应重分类。DDR 三分区（3/1/3）中 near-stationary 组有 1/3 不稳定，削弱框架清晰度。\n- **修复方向**：主文将 tail_decay 重分类为 \"weakly stationary\"；补充移除 tail_decay 后的分类和分区 sensitivity analysis；Figure 2 中用不同标记区分。\n\n**N5** [Critical→Major, R1 提出, R2 部分反驳] **ε=0.20 等价阈值缺乏问题特定正当性**\n- Cohen's d=0.20 是行为科学通用惯例，未论证在生成深度检测中的合理性。\n- **R2 反驳要点**：Table 30 证明核心分区在 ε∈[0.10, 0.75] 内完全不变——\"分区结果是阈值函数\" 仅适用于 entropy_std 的归属，不适用于核心 drifting/stationary 分区。\n- **综合判断**：降为 **Major**——核心分区对 ε 高度稳定，但补充 task-specific justification 会增强论证。\n- **修复方向**：从分类 F1 角度反推 SESOI（操作上可忽略的最小效应）；或绘制 equivalence frontier 图。\n\n### Should-Fix（影响评分但不一票否决）\n\n**W1** [Major | R1+R2 共识] **Base-model-only 范围限制实际适用性**\n- Appendix K 显示 instruction-tuned models 3-class F1 降至 0.575/0.544（降幅 17-21pp），DDR silhouette 从 0.660 降至 0.372。2025-2026 年绝大多数部署 LLM 都是 instruction-tuned。\n- Abstract/Introduction 措辞 (\"When LLM outputs re-enter generation pipelines\") 暗示广泛适用性，与 base-model-only 范围存在张力。\n- **修复方向**：Discussion 增加专门段落讨论 instruct 退化机制；Introduction 第一段明确 scope。\n\n**W2** [Major | R2 提出, R1 同意] **Downstream null result 在主文中讨论不充分**\n- Appendix M 的 TOST 明确显示 depth-aware curation ≈ random subsampling。这直接关系到 Introduction 中 \"data provenance matters\" 的动机。Discussion 仅用一句话带过。\n- **修复方向**：Discussion 增加专门段落讨论 null result 含义、为什么 depth signal 不能转化下游收益、在什么条件下可能有差异；重新定位价值为 provenance/audit 而非 curation。\n\n**W3** [Major | R1 提出, R2 同意] **QLoRA +11.6pp 基线比较跨子集不一致**\n- +11.6pp 基于 6-gen subset (XGBoost baseline=0.789)，而主文 Table 1 的 8-gen LOGO binary F1=0.694。两个基线相差 9.5pp。Discussion 引用 \"QLoRA recovers 0.905\" 时未标注是 6-gen 结果，读者容易误读。\n- **修复方向**：所有 QLoRA 引用标注 \"(6-gen subset)\"；补报 8-gen LOGO 下 QLoRA 结果。\n\n**W4** [Major | R1 提出, R2 同意] **Bootstrap CI 未捕获 generator-level 方差**\n- 8-gen LOGO macro F1=0.762，95% CI 宽度仅 4.8pp。但 per-generator binary F1 range 达 9.1pp (0.633-0.724)。Pythia 系列系统性高于其他 family，可能反映 Pythia-410M 参考模型的 same-family 优势。\n- **修复方向**：补充 across-generator SD/IQR 与 bootstrap CI 并列报告；讨论 same-family reference bias。\n\n**W5** [Minor-Major | R1+R2+Visual Check 共识] **前 4 页无任何图表，信息密度不均**\n- 作为 empirical paper，前 4 整页纯文字，首个视觉元素 (Table 1) 在 page 5，Figure 1 在 page 6。Related Work 1.5+ 页无结构化对比。\n- **修复方向**：将 Figure 1 (strip plot) 前移至 Introduction 末尾或 Method 开头；Related Work 加入 method comparison table。\n\n**W6** [Minor | R1 提出, R2 部分同意] **五种 effect-size measures 的 \"complementarity\" 过度宣称**\n- Cohen's d 和 Glass's Δ 在组间方差接近时高度相关；KS 在 location shift 主导时也与 Cohen's d 强相关。\"五重验证\" 可能过度膨胀置信度。\n- **修复方向**：改为 \"convergence across parametric and non-parametric measures\"；补充 inter-measure 相关矩阵。\n\n**W7** [Minor | R1+R2 共识] **Reference model (Pythia-410M) same-family confound 主文讨论不足**\n- 8 个 generator 中 2 个来自 Pythia family，reference model 同家族。Appendix S 验证了 cross-family reference 信号保持（spread 0.013），但主文仅一笔带过。\n- **修复方向**：§3.3 或 §5 补充 reference model bias 讨论；分 generator 报告 cross-reference 影响。\n\n---\n\n## Reviewer Consensus [AGREE]\n\n1. **页数超限** (~8.5 页) 需立即修复——desk reject 风险\n2. **tail_decay 应重分类**——4/8 TOST 通过率不支持 \"near-stationary\" 标签\n3. **Base-model-only 限制**需在主文更显著讨论\n4. **QLoRA +11.6pp 跨子集不一致**需标注子集信息\n5. **Bootstrap CI + generator-level variance** 需补充报告\n6. **Downstream null result** 需在 Discussion 获得更充分讨论\n7. **前 4 页无图表**需改善信息密度分布\n8. **Proof-of-concept 定位总体良好**，论文在大多数位置保持一致\n9. **引用质量良好**（66 条, 0 orphan, 0 missing），建议补充 Tulchinskii et al. (2024)\n\n## Reviewer Divergence [REBUT]\n\n1. **DDR 新颖性** [核心分歧]\n   - R1 (3.5): location/shape 分离是新贡献，在 model collapse 文献中未见——DDR ≠ diversity loss 的简单重述；即使需更强验证，decomposition 本身有独立价值\n   - R2 (3.0): drifting features 本质是已知的 diversity loss，shape stability 可能是 nucleus sampling 的 trivial 推论，增量贡献有限\n   - **两人共识**：无论如何，nucleus sampling confound 需要实验验证（greedy/top-k）\n\n2. **k=2 聚类严重性**\n   - R1: critical（描述性非推断性，p=0.030 仅边际显著）\n   - R2: major（generator-split/holdout/ε-stability 三重验证已相当充分）\n\n3. **ε=0.20 循环论证严重性**\n   - R1: critical（缺乏 domain-specific justification）\n   - R2: major（Table 30 证明核心分区对 ε 高度稳定，\"循环论证\" 判断过重）\n\n4. **3-class 粒度的价值**\n   - R1: 科学价值独立于即时应用，证明 depth 可检测本身就是贡献\n   - R2: 缺乏量化 use case，增量价值论证不足\n\n---\n\n## Questions\n\n1. Shape stability 是否在 greedy decoding / pure top-k 下同样成立？如果仅在 nucleus sampling 下成立，如何论证这不是 sampling truncation 的 trivial 推论？[R1+R2]\n2. Downstream null result (Appendix M) 表明 depth-aware curation ≈ random subsampling。在什么条件下预期 depth signal 能转化为实际 downstream benefit？[R2]\n3. 增加更多特征（n-gram diversity, 句法复杂度, discourse coherence）后 DDR 的 drifting/stationary 二分是否仍成立？当前 7 特征中 5 个基于 token-level NLL，特征空间局限性是否预设了分区结果？[R1]\n4. Instruction-tuned 下 silhouette 降至 0.372——DDR 框架的 drifting/stationary 分离前提是否在 instruction-tuned 模型下不再成立？这是否意味着论文的理论贡献局限于 base models？[R1+R2]\n5. 使用 2.8B/7B 参考模型是否会改变 DDR 分区本身（不仅是分类 F1）？Appendix S 未报告此项。[R1]\n6. 是否尝试过从分类 F1 角度反推 ε（操作上可忽略的最小效应）？[R1]\n7. 是否尝试过在 instruction-tuned chain 上重新训练分类器（而非 base-trained 分类器直接迁移）？[R2]\n\n---\n\n## Missing References\n\n以下由两位 Reviewer 独立建议：\n1. **Tulchinskii et al. (2024)** \"Intrinsic Dimension Estimation for Robust Detection of AI-Generated Texts\" (ICLR 2024) — R1+R2 共同建议，使用几何/拓扑特征检测 AI 文本，与本文 distributional statistics 方法互补\n2. **RADAR (Hu et al., 2023)** — R2 建议，adversarial training-based detector\n3. 代码域检测先前工作 — R1 建议，论文在 Appendix J 测试了 Code 域但未引用相关文献\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n**状态**: 已跳过（用户未提交）\n\n---\n\n## Visual Layout Check（非评分项）\n\n**状态**: 完成 | 4 warnings, 14 info\n\n**关键发现**：\n- **[Warning]** Pages 1-4 连续纯文本，无任何 display item。审稿人需翻到 page 5 才看到第一个视觉锚点 (Table 1)。建议将 Figure 1 (strip plot) 前移至 page 2-3。\n- **[Warning]** 第一个 display item 出现在 page 5，Figure 1 在 page 6——审稿人在前 2 分钟内无法建立核心发现的视觉认知。\n- **[Warning]** Discussion 跨 page 8-9，约 1.5 页连续纯文本。结合前面 pages 1-4 的纯文本段，全文 \"文本墙\" 比例偏高。\n- **[Warning]** 主文延伸至 page 9 约 2/3 处，约 8.7 页，可能超页。\n- **[Info]** Table 1/2 格式规范（booktabs, 加粗最优结果）。Figure 2+3+Table 2 在 page 7 密度适当。Figure 7 (base vs instruct DDR) 颜色清晰。Figure 1 strip plot 中 8 色在黑白/色弱条件下可能难以区分，建议添加 marker shape。Appendix 中 page 15 (Figure 4) 底部约 1/4 空白、page 25 (Figure 8) 子面板字号偏小（约正文 60%）。\n\n---\n\n## Overall Assessment\n\n**综合评分: 3.0 (Findings)**\n**置信度: 4/5**\n\n| 维度 | R1 | R2 | 综合 |\n|------|-----|-----|------|\n| Soundness | 3/5 | 3.5/5 | 3/5 |\n| Excitement | 3.5/5 | 2.5/5 | 3/5 |\n| Reproducibility | 4/5 | 4/5 | 4/5 |\n| Overall | 3.5 | 3.0 | 3.0 |\n\n**评分理由**：\n\n论文在实验执行和统计方法上高于平均水准，DDR 的 location/shape 分解角度有一定新意，问题定义从 binary 到 ordinal 是有意义的延伸。但以下因素将评分压至 Findings 水平：\n\n1. **格式违规** (N1): 主文约 8.5-8.7 页，超过 8 页限制，存在 desk reject 风险。这是可修复的但当前状态下是硬伤。\n2. **核心新颖性存疑** (N2): shape stability 可能是 nucleus sampling 的 by-design 属性——论文未提供非 nucleus sampling 的验证实验，而 Discussion 原文恰恰暗示了这一机制解释。如果这一质疑成立，DDR 的 \"novel observation\" 将缩水为 \"nucleus sampling + 已知 diversity loss\"。R1 认为 location/shape 分离本身有独立贡献 (3.5)，R2 认为增量性更强 (3.0)——这是评分差异的核心来源。\n3. **统计框架的方法论短板** (N3-N5): k=2 聚类在 n=7 上虽有辅助验证但统计效力先天不足；tail_decay \"near-stationary\" 标签不准确（4/8 TOST）；ε=0.20 缺乏 domain-specific justification。这些单独看是可修复的 major 问题，但累积起来削弱了 DDR 分析框架的 methodological rigor。\n4. **实际影响力受限**: base-model-only scope + downstream null result + 3-class 粒度限制了论文的应用前景。\n\n**如果以下条件满足，评分可提升至 3.5 (Borderline Conference)**：\n- 修复页数超限\n- 补充 greedy/top-k 下 shape stability 验证（或令人信服地论证为何 nucleus-sampling-specific 仍有独立贡献）\n- 修正 tail_decay 分类标签\n- Discussion 充分讨论 instruct 退化和 downstream null result\n\n---\n\n## Detailed Comments\n\n### Section 1 (Introduction)\n- 开头 \"When LLM outputs re-enter generation pipelines\" 暗示广泛适用性，但论文仅覆盖 base model continuation chains。建议第一段明确 scope。\n- Contribution 列表从 3 条缩减到 2 条 + 一个 \"additionally provide\"——结构清晰但 \"additionally\" 部分读起来像第三个贡献。\n- R2-Q5: 为什么选 continuation chain 而非 paraphrase chain？R1 引用 Appendix Z.6 Table 41 解释了方法论原因（语义自由度更高），但主文未讨论此设计选择。\n\n### Section 2 (Related Work)\n- §2.2 最后一段对 Broken Telephone / Markovian Chains 的区分较好，但 R2 认为仍可加入结构化对比表以增强说服力。\n- 缺 Tulchinskii et al. (2024) [R1+R2 共识]。\n\n### Section 3 (Method)\n- §3.3 \"entropy as shorthand for NLL\" 声明存在但可考虑更精确的措辞（R2 minor）。\n- §3.4 \"LOGO family-level\" 行定义需澄清——是 per-generator 还是 per-family leave-one-out（R1 minor）。\n- Reference model 选择的潜在偏差应在此处或 §5 明确讨论。\n\n### Section 4 (Results)\n- §4.1: bootstrap CI [0.758, 0.766] 宽度仅 0.8pp，而 per-generator spread 9.1pp。需补充 generator-level variance。\n- §4.2: \"five complementary effect-size measures\" → 建议改为 \"convergence across parametric and non-parametric measures\"。\n- §4.2: tail_decay 的 4/8 TOST 在主文已有三句覆盖 (L89-91)，但 \"near-stationary\" 标签仍过于宽泛。\n- §4.3: Table 2 显示 4-det+surface (0.708) > 7-feature (0.705)——论文诚实报告，DDR 贡献定位为 decomposition 而非 classification performance。\n\n### Section 5 (Discussion)\n- 篇幅过长（~1.3 页），是页数超限的主要原因。\n- 14B preliminary results 可移至附录。\n- Model collapse 区分的讨论虽重要但可精简。\n- Downstream null result 仅一句话——需扩展。\n- QLoRA \"0.905\" 引用未标注 6-gen subset。\n\n### Section 6 (Conclusion)\n- \"preliminary 14B evidence confirms the partition\" 用词偏强——14B 是 preliminary 且仅 1 个模型。\n- 可适当压缩。\n\n### R1 事实纠正\nR1-W5 声称 \"缺 t=1.0\"，但 Table 10 (Appendix H) 明确测试了 t∈{0.5, 0.7, 1.0}。R2 在交叉回应中纠正了此事实错误。温度覆盖度限制在于仅 4/8 generator 参与温度实验，而非缺少特定温度点。",
    "project": "gen-depth-fingerprint",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "3.0 (Findings)",
    "review_chat_id": "oc_999770e4e57bfc6eabd12fc1f64af1ef"
  }
}
```

</details>

---


### Tool result

_source line 2769 · 2026-05-21T04:01:24.630052+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_dbd68d7879a81efc0c108e9844b15d0b:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4171
}
```

</details>

---


### Assistant

_source line 2770 · 2026-05-21T04:01:34.107501+00:00_

Round 36 审稿完成，报告已投递给 Research Director。

**综合评分：3.0 (Findings)**

**核心问题汇总**：
1. **[Critical]** 主文约 8.5-8.7 页，超过 EMNLP 8 页限制——desk reject 风险
2. **[Critical]** Shape stability 可能是 nucleus sampling 的 by-design 属性，缺少 greedy/top-k 验证实验——DDR 核心新颖性存疑
3. **[Major]** k=2 聚类在 n=7 上统计效力不足（permutation test p=0.030 仅边际显著）
4. **[Major]** tail_decay 仅 4/8 generator 通过 TOST——"near-stationary" 标签不准确
5. **[Major]** ε=0.20 缺乏 domain-specific justification
6. **[Major]** Base-model-only 限制 + downstream null result + QLoRA 跨子集不一致

**评分分歧**：R1=3.5 vs R2=3.0，核心在于 DDR location/shape 分离的新颖性判断——R1 认为有独立贡献，R2 认为增量。两人均同意需要非 nucleus sampling 验证实验。

Issue tracker 已同步更新（新增 4 个 Round 36 issue，更新 12 个历史 issue 的最新状态）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director"
}
```

</details>

---


## Round 247

## Round 247

2 recorded events


### User

_source line 2771 · 2026-05-21T04:01:36.831911+00:00_

[Reviewer 1 审稿结果]:
交叉回应已提交给 Review Director。

**摘要**：对 R2 的 13 个审稿点逐条回应——

- **N1 (页数)**: [AGREE]，PDF 确认主文约 8.5 页，超限
- **N2 (DDR vs model collapse)**: [部分 REBUT] — 反对"DDR = diversity loss"的等式（论文的 location/shape 分离是新发现），但 [AGREE] nucleus sampling 下 shape stability 可能是 sampling 机制的 trivial 推论，缺少 greedy/top-k 验证是显著实验空白
- **W1-W5**: 基本同意，其中 W2 (base-model-only) 和 W5 (reference model confound) 与 R1 自身 concern 重合
- **Q1-Q5**: 多数同意，Q5 (continuation vs paraphrase) 部分反驳——论文在 Appendix Z.6 Table 41 有讨论
- 维持 **Overall 3.5 (Borderline Conference)**，认为 R2 的 3.0 偏保守

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 2772 · 2026-05-21T04:01:47.449861+00:00_

Round 36 审稿完成。

**审稿报告已投递给 Research Director。**

**综合评分: 3.0 (Findings)**

核心问题汇总：
- **N1** [Critical] 主文约 8.5-8.7 页，超过 EMNLP 8 页限制——desk reject 风险
- **N2** [Critical] Shape stability 可能是 nucleus sampling 的 by-design 属性，缺少 greedy/top-k 验证实验——核心新颖性存疑
- **N3-N5** [Major] DDR 统计框架方法论短板：k=2 聚类效力不足、tail_decay "near-stationary" 名不副实、ε=0.20 缺 domain-specific justification

R1 评 3.5 (Borderline Conference)，R2 评 3.0 (Findings)。分歧核心在 DDR 新颖性评估：R1 认为 location/shape 分离有独立贡献，R2 认为相对 model collapse 文献增量有限。两人均同意 nucleus sampling confound 需要实验验证。

Issue Tracker 已同步更新（新增 4 个 issue，更新 12 个既有 issue）。视觉审查已完成（4 warnings），外部审稿已跳过。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director"
}
```

</details>

---


## Round 248

## Round 248

48 recorded events


### User

_source line 2773 · 2026-05-21T04:22:58.792013+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: gen-depth-fingerprint
- 论文路径: projects/gen-depth-fingerprint/docs/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: ARR
- 截止日期: 2026-05-25

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 2774 · 2026-05-21T04:23:04.018586+00:00_

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
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 2775 · 2026-05-21T04:23:04.069629+00:00_

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
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 2776 · 2026-05-21T04:23:12.268182+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,director_post_to_reviewer,dispatch_visual_check,get_external_review_status,get_visual_check_status,request_external_review,submit_review_report_to_research_director,update_review_issues,read_project_file",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_get_project_overview,director_post_to_reviewer,dispatch_visual_check,get_external_review_status,get_visual_check_status,request_external_review,submit_review_report_to_research_director,update_review_issues,read_project_file",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 2777 · 2026-05-21T04:23:12.318867+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2778 · 2026-05-21T04:23:15.781453+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__read_project_file",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__read_project_file",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 2779 · 2026-05-21T04:23:15.832586+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "ToolSearch",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 2780 · 2026-05-21T04:23:18.494555+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_local_file,WebSearch",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_local_file,WebSearch",
    "max_results": "3"
  }
}
```

</details>

---


### Tool result

_source line 2781 · 2026-05-21T04:23:18.494929+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 2782 · 2026-05-21T04:23:18.947735+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "gen-depth-fingerprint"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "gen-depth-fingerprint"
  }
}
```

</details>

---


### Tool result

_source line 2783 · 2026-05-21T04:23:19.148899+00:00_

{"result":"# 项目 gen-depth-fingerprint 概况\n\n## 实验状态 (66 个)\n\n- **plan-015**: DONE (success) — \n- **plan-004**: DONE (failed) — \n- **plan-003**: DONE (success) — \n- **plan-013**: DONE (success) — \n- **plan-002**: DONE (success) — \n- **plan-002-qwen17b-retry-s1**: DONE (failed) — \n- **plan-002-qwen17b-retry-s0**: DONE (failed) — \n- **plan-002-qwen06b-s1**: DONE (failed) — \n- **plan-002-qwen06b-s0**: DONE (failed) — \n- **plan-002-qwen17b-s1**: DONE (failed) — \n- **plan-002-qwen17b-s0**: DONE (failed) — \n- **plan-002-qwen3-1_7b-s0**: DONE (failed) — \n- **plan-002-qwen3-1_7b-s1**: DONE (killed) — \n- **plan-001**: DONE (success) — \n- **mvp-001**: DONE (success) — \n\n## 最新报告\n# Handover — 2026-05-21\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n（无）\n\n## 近期结论\n- **plan-004-prep** (success): Downstream utility 准备：depth-stratified 数据集 + OLMo-1B fine-tuning 脚本（不开跑，等 Director 确认）\n- **review-exp-a-baseline-ensemble** (killed): 审稿回应实验A：4-baseline ensemble + 统一超参对比，验证 7-feature vs 4-baseline vs 6-feature 在公平条件下的性能差异\n- **multi_domain_t07** (killed): —\n\n## 趋势\n成功 47 / 负向 2 / 失败 12 / 共 66\n\n## 下一步\n（无活跃 idea，请通过 ideas.md 添加）\n\n## 资源状态\nbjb2-18868: 无 GPU 信息\n\n## 告警\n- mvp-001-gen-s0: 已被终止 — unknown\n- mvp-001-gen-s1: 训练失败 — unknown\n- mvp-001-gen-s2: 训练失败 — unknown\n- mvp-001-gen-s3: 训练失败 — unknown\n- plan-001-restore: 已被终止 — unknown\n- plan-002-qwen3-1_7b-s0: 训练失败 — unknown\n- plan-002-qwen3-1_7b-s1: 已被终止 — unknown\n- plan-002-qwen17b-s0: 训练失败 — unknown\n- plan-002-qwen17b-s1: 训练失败 — unknown\n- plan-002-qwen17b-retry-s0: 训练失败 — unknown\n- plan-002-qwen17b-retry-s1: 训练失败 — unknown\n- plan-002-qwen06b-s0: 训练失败 — unknown\n- plan-002-qwen06b-s1: 训练失败 — unknown\n- plan-004: 训练失败 — unknown\n- review-exp-a-baseline-ensemble: 已被终止 — unknown\n- multi_domain_t07: 已被终止 — unknown\n- exp_050_temp_curve_t09: 训练失败 — unknown"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 2784 · 2026-05-21T04:23:26.976504+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/main.tex",
  "limit": "80"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/main.tex",
    "limit": "80"
  }
}
```

</details>

---


### Tool result

_source line 2785 · 2026-05-21T04:23:28.232928+00:00_

1	% EMNLP 2026 ARR Submission — ACL 2023 Template
2	\documentclass[11pt]{article}
3	\usepackage[review]{acl}
4	\usepackage{times}
5	\usepackage{latexsym}
6	\usepackage[T1]{fontenc}
7	\usepackage[utf8]{inputenc}
8	\usepackage{microtype}
9	\usepackage{graphicx}
10	\usepackage{booktabs}
11	\usepackage{enumitem}
12	\usepackage{amsmath}
13	\usepackage{amssymb}
14	\usepackage{placeins}
15	\usepackage{multirow}
16	\usepackage{float}
17	
18	\graphicspath{{../chart/}}
19	
20	\title{Depth Fingerprinting: Detecting Recursive Generation Depth\\in LLM Text Chains}
21	
22	\author{Anonymous}
23	
24	\begin{document}
25	\maketitle
26	
27	\input{abstract}
28	
29	\input{introduction}
30	\input{related_work}
31	\input{method}
32	\input{results}
33	
34	\input{discussion}
35	\input{conclusion}
36	\input{limitations}
37	\input{ethics}
38	
39	\bibliography{references}
40	
41	\appendix
42	
43	\noindent\textbf{Note:} Unless otherwise stated, appendix experiments use the original six-generator subset (Pythia-2.8B/1B, OLMo-2-1B, Qwen3-1.7B/0.6B/8B).
44	Main paper results (\S\ref{sec:results}) use the full eight-generator set (adding Llama-3.2-3B and Mistral-7B-v0.3).
45	
46	\input{appendix_dataset_stats}
47	
48	\section{Length Confound Analysis}
49	\label{app:length}
50	\input{appendix_length}
51	
52	\section{Prompt Type Generalization}
53	\label{app:prompt-type}
54	\input{appendix_prompt_type}
55	
56	\section{Finer-Grained Depth Classification}
57	\label{app:finer-depth}
58	\input{appendix_finer_depth}
59	
60	\section{End-to-End Depth Classification (QLoRA)}
61	\label{app:qlora}
62	\input{appendix_qlora}
63	
64	\section{Leave-One-Feature-Out Analysis}
65	\label{app:lofo}
66	\input{appendix_lofo}
67	
68	\section{Confusion Matrix}
69	\label{app:confusion}
70	\input{appendix_confusion_matrix}
71	
72	\section{Classifier Sensitivity}
73	\label{app:classifier}
74	\input{appendix_classifier}
75	\FloatBarrier
76	
77	\section{Robustness to Text Perturbation}
78	\label{app:human-edit}
79	\input{appendi
…[truncated 17 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "elapsed_ms": 1256
}
```

</details>

---


### Tool call

_source line 2786 · 2026-05-21T04:23:28.333865+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 call for papers submission guidelines ARR site:aclweb.org"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 call for papers submission guidelines ARR site:aclweb.org"
  }
}
```

</details>

---


### Tool call

_source line 2787 · 2026-05-21T04:23:28.735950+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "gen-depth-fingerprint"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "gen-depth-fingerprint"
  }
}
```

</details>

---


### Tool call

_source line 2788 · 2026-05-21T04:23:29.539418+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "gen-depth-fingerprint",
  "file": "report.md",
  "max_chars": "3000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "gen-depth-fingerprint",
    "file": "report.md",
    "max_chars": "3000"
  }
}
```

</details>

---


### Tool result

_source line 2789 · 2026-05-21T04:23:34.810806+00:00_

Web search results for query: "EMNLP 2026 call for papers submission guidelines ARR site:aclweb.org"

Links: [{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"Workshop on Multimodal Interaction in Face-to-Face Dialogue (MINT @ EMNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/workshop-multimodal-interaction-face-face-dialogue-mint-emnlp-2026"},{"title":"*SEM 2026: Commitment Link for ARR-Reviewed Papers (Deadline: 10 April 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/sem-2026-commitment-link-arr-reviewed-papers-deadline-10-april-2026"},{"title":"EACL/ACL 2026 Joint Call for Workshops | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eaclacl-2026-joint-call-workshops"},{"title":"[EMNLP 2025] First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2025-first-call-papers"},{"title":"Joint Call for Tutorial Proposals (EACL/ACL) 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-eaclacl-2026"},{"title":"The 64th Annual Meeting of the Association for Computational Linguistics - ACL 2026","url":"https://2026.aclweb.org/"},{"title":"Call for Papers: The 20th Linguistic Annotation Workshop (LAW XX), co-located with ACL 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/call-papers-20th-linguistic-annotation-workshop-law-xx-co-located-acl-2026"},{"title":"Jan. 2025 ACL Standing Committee on Peer Review (COPR) Report 1","url":"https://www.aclweb.org/adminwiki/images/9/9e/COPR-5-cycle-report-to-publish.pdf"},{"title":"The 2nd BabyLM Workshop | ACL Member Portal","url":"https://www.aclweb.org/portal/content/2nd-babylm-workshop"}]

Based on my search results, I found information about EMNLP 2026, though not a specific main conference call for papers. Here's
…[truncated 1162 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "WebSearch",
  "elapsed_ms": 6476
}
```

</details>

---


### Tool result

_source line 2790 · 2026-05-21T04:23:35.011986+00:00_

{"result":"# 项目 gen-depth-fingerprint 概况\n\n## 实验状态 (66 个)\n\n- **plan-015**: DONE (success) — \n- **plan-004**: DONE (failed) — \n- **plan-003**: DONE (success) — \n- **plan-013**: DONE (success) — \n- **plan-002**: DONE (success) — \n- **plan-002-qwen17b-retry-s1**: DONE (failed) — \n- **plan-002-qwen17b-retry-s0**: DONE (failed) — \n- **plan-002-qwen06b-s1**: DONE (failed) — \n- **plan-002-qwen06b-s0**: DONE (failed) — \n- **plan-002-qwen17b-s1**: DONE (failed) — \n- **plan-002-qwen17b-s0**: DONE (failed) — \n- **plan-002-qwen3-1_7b-s0**: DONE (failed) — \n- **plan-002-qwen3-1_7b-s1**: DONE (killed) — \n- **plan-001**: DONE (success) — \n- **mvp-001**: DONE (success) — \n\n## 最新报告\n# Handover — 2026-05-21\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n（无）\n\n## 近期结论\n- **plan-004-prep** (success): Downstream utility 准备：depth-stratified 数据集 + OLMo-1B fine-tuning 脚本（不开跑，等 Director 确认）\n- **review-exp-a-baseline-ensemble** (killed): 审稿回应实验A：4-baseline ensemble + 统一超参对比，验证 7-feature vs 4-baseline vs 6-feature 在公平条件下的性能差异\n- **multi_domain_t07** (killed): —\n\n## 趋势\n成功 47 / 负向 2 / 失败 12 / 共 66\n\n## 下一步\n（无活跃 idea，请通过 ideas.md 添加）\n\n## 资源状态\nbjb2-18868: 无 GPU 信息\n\n## 告警\n- mvp-001-gen-s0: 已被终止 — unknown\n- mvp-001-gen-s1: 训练失败 — unknown\n- mvp-001-gen-s2: 训练失败 — unknown\n- mvp-001-gen-s3: 训练失败 — unknown\n- plan-001-restore: 已被终止 — unknown\n- plan-002-qwen3-1_7b-s0: 训练失败 — unknown\n- plan-002-qwen3-1_7b-s1: 已被终止 — unknown\n- plan-002-qwen17b-s0: 训练失败 — unknown\n- plan-002-qwen17b-s1: 训练失败 — unknown\n- plan-002-qwen17b-retry-s0: 训练失败 — unknown\n- plan-002-qwen17b-retry-s1: 训练失败 — unknown\n- plan-002-qwen06b-s0: 训练失败 — unknown\n- plan-002-qwen06b-s1: 训练失败 — unknown\n- plan-004: 训练失败 — unknown\n- review-exp-a-baseline-ensemble: 已被终止 — unknown\n- multi_domain_t07: 已被终止 — unknown\n- exp_050_temp_curve_t09: 训练失败 — unknown"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 6276
}
```

</details>

---


### Tool result

_source line 2791 · 2026-05-21T04:23:35.012513+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/report.md\", \"content\": \"# Handover — 2026-05-21\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n（无）\\n\\n## 待处理\\n（无）\\n\\n## 近期结论\\n- **plan-004-prep** (success): Downstream utility 准备：depth-stratified 数据集 + OLMo-1B fine-tuning 脚本（不开跑，等 Director 确认）\\n- **review-exp-a-baseline-ensemble** (killed): 审稿回应实验A：4-baseline ensemble + 统一超参对比，验证 7-feature vs 4-baseline vs 6-feature 在公平条件下的性能差异\\n- **multi_domain_t07** (killed): —\\n\\n## 趋势\\n成功 47 / 负向 2 / 失败 12 / 共 66\\n\\n## 下一步\\n（无活跃 idea，请通过 ideas.md 添加）\\n\\n## 资源状态\\nbjb2-18868: 无 GPU 信息\\n\\n## 告警\\n- mvp-001-gen-s0: 已被终止 — unknown\\n- mvp-001-gen-s1: 训练失败 — unknown\\n- mvp-001-gen-s2: 训练失败 — unknown\\n- mvp-001-gen-s3: 训练失败 — unknown\\n- plan-001-restore: 已被终止 — unknown\\n- plan-002-qwen3-1_7b-s0: 训练失败 — unknown\\n- plan-002-qwen3-1_7b-s1: 已被终止 — unknown\\n- plan-002-qwen17b-s0: 训练失败 — unknown\\n- plan-002-qwen17b-s1: 训练失败 — unknown\\n- plan-002-qwen17b-retry-s0: 训练失败 — unknown\\n- plan-002-qwen17b-retry-s1: 训练失败 — unknown\\n- plan-002-qwen06b-s0: 训练失败 — unknown\\n- plan-002-qwen06b-s1: 训练失败 — unknown\\n- plan-004: 训练失败 — unknown\\n- review-exp-a-baseline-ensemble: 已被终止 — unknown\\n- multi_domain_t07: 已被终止 — unknown\\n- exp_050_temp_curve_t09: 训练失败 — unknown\\n\", \"total_chars\": 1130, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 5473
}
```

</details>

---


### Tool call

_source line 2792 · 2026-05-21T04:23:40.031760+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review ARR 2026 submission deadline June cycle"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review ARR 2026 submission deadline June cycle"
  }
}
```

</details>

---


### Tool call

_source line 2793 · 2026-05-21T04:23:40.533694+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 main conference submission guidelines page limit format"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 main conference submission guidelines page limit format"
  }
}
```

</details>

---


### Tool call

_source line 2794 · 2026-05-21T04:23:41.944766+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/review_issues.yaml 2>/dev/null || echo \"FILE_NOT_FOUND\"",
  "description": "Check existing review issues tracker"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/review_issues.yaml 2>/dev/null || echo \"FILE_NOT_FOUND\"",
    "description": "Check existing review issues tracker"
  }
}
```

</details>

---


### Tool result

_source line 2795 · 2026-05-21T04:23:42.397826+00:00_

&lt;persisted-output>
Output too large (31.1KB). Full output saved to: /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-3-projects-gen-depth-fingerprint--claude-sessions-review-director-fec00603/1d09cdd5-00ac-4676-8013-cd78df9c94fc/tool-results/bbem3um0m.txt

Preview (first 2KB):
# === Round 29-34 历史 Issues（保留完整记录）===

- id: "R29-N1"
  summary: "Base-model-only scope 未在 Abstract 标注"
  category: framing
  severity: critical
  status: resolved
  first_raised_round: 29
  last_seen_round: 32
  mentions:
    - {round: 29, reviewers: "R1+R2", note: "共识: Abstract 必须标注 base-model scope"}
    - {round: 31, reviewers: "R1+R2", note: "W1: Title/Abstract 仍需 base-model qualifier"}
    - {round: 32, reviewers: "R1+R2", note: "升级: 实验设计仅覆盖 base model, 建议扩展或限定 scope"}
  action_items:
    - {round: 29, action: "Abstract 加 base (pretrained) qualifier", assigned_to: Agent, status: done}
    - {round: 32, action: "Abstract/Conclusion 已有 qualifier; instruct in Discussion", assigned_to: Director, status: done}
  resolution: "Abstract L3 'eight base-model generators'; L7 'restricted to base models'. Title 保持不变(Reviewer 确认). Instruct limitations fully documented."
  resolution_round: 32

- id: "R29-N2"
  summary: "Downstream TOST underpowered (n=3) + Abstract overclaim"
  category: experiment
  severity: critical
  status: resolved
  first_raised_round: 29
  last_seen_round: 34
  mentions:
    - {round: 29, reviewers: "R1+R2", note: "n=3 seeds, Abstract 省略 preliminary"}
    - {round: 31, reviewers: "R1+R2", note: "W3: TOST n=3 underpowered"}
    - {round: 32, reviewers: "R1+R2", note: "升级为 null result: depth-aware curation 不优于 random"}
    - {round: 34, reviewers: "R1+R2", note: "RESOLVED: Abstract 完全移除 downstream claim; Appendix M 坦诚呈现 null result"}
  action_items:
    - {round: 29, action: "Abstract 加 preliminary qualifier", assigned_to: Agent, status: done}
    - {round: 32, action: "Abstract/Conclusion downstream reframing", assigned_to: Director, statu
…[truncated 331 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Bash",
  "elapsed_ms": 453
}
```

</details>

---


### Tool call

_source line 2796 · 2026-05-21T04:23:42.750970+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/config.yaml 2>/dev/null | head -100",
  "description": "Check project config for external review settings"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/config.yaml 2>/dev/null | head -100",
    "description": "Check project config for external review settings"
  }
}
```

</details>

---


### Tool result

_source line 2797 · 2026-05-21T04:23:42.801622+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 2798 · 2026-05-21T04:23:44.608394+00:00_

Web search results for query: "ACL Rolling Review ARR 2026 submission deadline June cycle"

Links: [{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/"},{"title":"aclrollingreview/dates.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/dates.md"},{"title":"ACLRollingReview (@ReviewAcl) / Posts / X","url":"https://x.com/ReviewAcl"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"ACL ARR | OpenReview","url":"https://openreview.net/group?id=aclweb.org%2FACL%2FARR"}]

Based on the search results, I found relevant information about the ACL Rolling Review (ARR) 2026 submission deadlines. However, the search results don't show a specific June 2026 cycle deadline. Here's what I found:

After extensive deliberation and soliciting community feedback, the ACL Peer Review Committee recommended switching to 10-week cycles, with the new schedule starting in May 2025. This means that instead of 6 cycles a year there will generally be 5.

For 2026 specifically, the January 2026 submission deadline is January 5, 2026. The search results mention 10-week review cycles for 2026, but the specific June cycle deadline information 
…[truncated 351 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "WebSearch",
  "elapsed_ms": 4576
}
```

</details>

---


### Tool result

_source line 2799 · 2026-05-21T04:23:45.914151+00:00_

Web search results for query: "EMNLP 2026 main conference submission guidelines page limit format"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"EMNLP 2026 LaTeX Template | ACL Style Files & Overleaf | Underleaf","url":"https://www.underleaf.ai/templates/emnlp"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"},{"title":"EMNLP: Empirical Methods in Natural Language Processing 2027 2026 2025 ...","url":"http://www.wikicfp.com/cfp/program?id=883"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"EMNLP 2026 Conference | OpenReview","url":"https://openreview.net/group?id=EMNLP%2F2026%2FConference"},{"title":"Confs: 2026 Conference on Empirical Methods in Natural ...","url":"https://www.facebook.com/linguistlist/posts/confs-2026-conference-on-empirical-methods-in-natural-language-processing-emnlp-/1351983883622556/"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"}]

Based on the search results, here are the submission guidelines for EMNLP 2026 main conference papers:

**Page Limits:**
The format is two-column with an 8-page limit for long papers and a 4-page limit for short papers. More specifically, long papers have 8 pages of content plus unlimited references, while short papers have 4 pages of content plus unlimited references. Additionally, the Limitations section doesn't count toward the page limit.

**Format:**
EMNLP uses the standard ACL style 
…[truncated 553 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "WebSearch",
  "elapsed_ms": 5380
}
```

</details>

---


### Tool call

_source line 2800 · 2026-05-21T04:24:02.884309+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint -name \"*.yaml\" -path \"*/config*\" -o -name \"config.yaml\" 2>/dev/null | head -10",
  "description": "Find project config file"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint -name \"*.yaml\" -path \"*/config*\" -o -name \"config.yaml\" 2>/dev/null | head -10",
    "description": "Find project config file"
  }
}
```

</details>

---


### Tool result

_source line 2801 · 2026-05-21T04:24:03.286184+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Bash",
  "elapsed_ms": 401
}
```

</details>

---


### Tool call

_source line 2802 · 2026-05-21T04:24:03.437022+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 call for papers ARR commitment deadline page limit anonymity",
  "allowed_domains": "['2026.emnlp.org']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 call for papers ARR commitment deadline page limit anonymity",
    "allowed_domains": "['2026.emnlp.org']"
  }
}
```

</details>

---


### Tool call

_source line 2803 · 2026-05-21T04:24:04.341621+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/main.tex",
  "offset": "80",
  "limit": "40"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/main.tex",
    "offset": "80",
    "limit": "40"
  }
}
```

</details>

---


### Tool result

_source line 2804 · 2026-05-21T04:24:04.393085+00:00_

80	
81	\section{Cross-Domain Generalization}
82	\label{app:domain}
83	\input{appendix_domain}
84	
85	\section{Instruction-Tuned Model Analysis}
86	\label{app:instruct}
87	\input{appendix_instruct}
88	
89	\section{Error Analysis of Binary Classification}
90	\label{app:error-analysis}
91	\input{appendix_error_analysis}
92	
93	\section{Downstream Utility}
94	\label{app:downstream}
95	\input{appendix_downstream}
96	
97	\section{Cross-Model Chain Per-Class Detail}
98	\label{app:cross-model-detail}
99	\input{appendix_cross_model_detail}
100	
101	\section{Feature Distribution Analysis}
102	\label{app:feature-distributions}
103	\input{appendix_feature_distributions}
104	
105	\section{Cross-Temperature Transfer}
106	\label{app:cross-temp}
107	\input{appendix_cross_temp}
108	\FloatBarrier
109	
110	\section{Feature Ablation}
111	\label{app:ablation-table}
112	\input{appendix_ablation}
113	
114	\input{appendix_feature_correlation}
115	
116	\section{Cross-Family Reference Models}
117	\label{app:cross-ref}
118	\input{table4}
119	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool result

_source line 2805 · 2026-05-21T04:24:09.662978+00:00_

Web search results for query: "EMNLP 2026 call for papers ARR commitment deadline page limit anonymity"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"The 2026 Conference on Empirical Methods in Natural Language Processing - EMNLP 2026","url":"https://2026.emnlp.org/"},{"title":"Call for Papers: EMNLP 2026 Industry Track - EMNLP 2026","url":"https://2026.emnlp.org/calls/industry_track/"},{"title":"Call for Workshop Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/workshops/"},{"title":"Call for Tutorials - EMNLP 2026","url":"https://2026.emnlp.org/calls/tutorials/"},{"title":"FAQ - EMNLP 2026","url":"https://2026.emnlp.org/faq/"},{"title":"Registration Information for EMNLP 2025 - EMNLP 2026","url":"https://2026.emnlp.org/registration/"},{"title":"EMNLP 2026 Paper Integrity Policy - EMNLP 2026","url":"https://2026.emnlp.org/paper-integrity-policy/"},{"title":"EMNLP 2026 AI Reviewing Experiment - EMNLP 2026","url":"https://2026.emnlp.org/ai-reviewing-experiment/"},{"title":"EMNLP 2026 Blog - EMNLP 2026","url":"https://2026.emnlp.org/blog/"}]

Based on the search results, here's information about EMNLP 2026's call for papers regarding ARR commitment, deadlines, page limits, and anonymity:

## ARR Commitment Deadline

Papers must be submitted, at latest, by the ARR 2026 May cycle. Papers that have received reviews and a meta-review from ARR (whether from the ARR 2026 May cycle or an earlier ARR cycle) may be committed to EMNLP via the commitment link.

## ARR Submission Policy

Given that the ARR 2026 May cycle is aligned with two conferences (EMNLP and AACL), authors will need to explicitly declare which conference they intend to commit to at submission time. This choice will be binding for EMNLP 2026: i.e., ARR 2026 May submissions that do not select EMNLP 2026 during submission will not be able to commit to EMNLP 2026.

## Anonymity Policy

Following the ACL and ARR pol
…[truncated 436 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "WebSearch",
  "elapsed_ms": 6225
}
```

</details>

---


### Tool call

_source line 2806 · 2026-05-21T04:24:15.549349+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_3 -maxdepth 3 -name \"*.yaml\" -path \"*gen-depth*\" 2>/dev/null | head -20",
  "description": "Find project YAML files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_3 -maxdepth 3 -name \"*.yaml\" -path \"*gen-depth*\" 2>/dev/null | head -20",
    "description": "Find project YAML files"
  }
}
```

</details>

---


### Tool result

_source line 2807 · 2026-05-21T04:24:16.101881+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/dream_registry.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/writing_plan.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/paper_provenance.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/literature_map.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/registry.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/constraints.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/mistakes.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/decisions.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/experiment_plan.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/config/projects/gen-depth-fingerprint.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Bash",
  "elapsed_ms": 552
}
```

</details>

---


### Tool call

_source line 2808 · 2026-05-21T04:24:16.102212+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "site:2026.emnlp.org calls main conference papers"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "site:2026.emnlp.org calls main conference papers"
  }
}
```

</details>

---


### Tool result

_source line 2809 · 2026-05-21T04:24:21.524639+00:00_

Web search results for query: "site:2026.emnlp.org calls main conference papers"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"Call for Workshop Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/workshops/"},{"title":"Call for Papers: EMNLP 2026 Industry Track - EMNLP 2026","url":"https://2026.emnlp.org/calls/industry_track/"},{"title":"EMNLP 2026 Blog - EMNLP 2026","url":"https://2026.emnlp.org/blog/"},{"title":"Call for Tutorials - EMNLP 2026","url":"https://2026.emnlp.org/calls/tutorials/"},{"title":"Leveraging Large Language Models for Improved Understanding of Communications With Patients With Cancer in a Call Center Setting: Proof-of-Concept Study","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11669882/"},{"title":"Natural language processing for humanitarian action: Opportunities, challenges, and the path toward humanitarian NLP","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10080095/"}]

The search found relevant information about EMNLP 2026's call for main conference papers. Here are the key details:

EMNLP 2026 invites the submission of long and short papers featuring substantial, original, and unpublished research on empirical methods for Natural Language Processing. Papers may contribute negative findings, survey an area, announce the creation of a new resource, argue a position, report novel linguistic insights derived using existing computational techniques, and reproduce (or fail to reproduce) previous results.

Regarding submission procedures, for the ARR 2026 May cycle aligned with EMNLP, authors must explicitly declare which conference they intend to commit to at submission time, and this choice is binding for EMNLP 2026. Dual submissions are not allowed.

Additionally, some presentations at the conference will be of papers accepted by the Transactions of the ACL (TACL) and the Computational Linguistics (CL) journals.


REMINDER: You MUST i
…[truncated 80 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "WebSearch",
  "elapsed_ms": 5422
}
```

</details>

---


### Tool call

_source line 2810 · 2026-05-21T04:24:24.832333+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/config/projects/gen-depth-fingerprint.yaml",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/config/projects/gen-depth-fingerprint.yaml",
    "limit": "100"
  }
}
```

</details>

---


### Tool result

_source line 2811 · 2026-05-21T04:24:24.832793+00:00_

1	execution:
2	  gpu_ids:
3	  - cuda:0
4	  - cuda:1
5	  project_path: /root/gen-depth-fingerprint
6	  servers:
7	  - bjb2-18868
8	feishu:
9	  chat_id: oc_dbd68d7879a81efc0c108e9844b15d0b
10	  operational_chat_id: oc_a189a3add89efad7437b5c9f3e05fbf3
11	  review_mode: fresh
12	  review_paper_path: projects/gen-depth-fingerprint/docs/paper/main.tex
13	  review_paper_pdf_path: /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/main.pdf
14	  review_round: 37
15	  review_supplementary_paths: ''
16	  submission_chat_id: oc_999770e4e57bfc6eabd12fc1f64af1ef
17	project:
18	  created_at: '2026-05-14T16:13:51.441Z'
19	  description: Provenance Depth Estimation for Risk-Aware Curation of Synthetic Text
20	  name: gen-depth-fingerprint
21	  phase: research
22	  source_idea_id: idea_009
23	rules:
24	  research: []
25	  writing:
26	  - created_at: '2026-05-17T17:22:45Z'
27	    id: 89ee27
28	    text: overall framework参考已发表EMNLP论文的风格，图中的信息密度要高，视觉美观，高度浓缩method部分信息
29	  - created_at: '2026-05-20T16:25:45Z'
30	    id: '799680'
31	    text: 参考已发表同类文章（如本文是empirical）的写作风格，如用词，写作逻辑，架构，语气，改善本篇的写作，要将整个story讲的高级一些，体现技术深度同时有创新性
32	  - created_at: '2026-05-20T16:43:51Z'
33	    id: c60e8a
34	    text: 附录中的可视化图要嵌入在文字中，出现在论文中需要用到图的附近位置，同时注意latex排版，避免大量空白的存在
35	  - created_at: '2026-05-21T03:45:29Z'
36	    id: dacdf2
37	    text: 图表不要默认在页面的居中位置，前面有留白要及时补齐，动态调整文字和配图（全宽/半宽），同时要注意图片和文字位置的匹配程度
38	venue: emnlp-2026
39	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 2812 · 2026-05-21T04:24:36.229904+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/main.pdf 2>/dev/null && echo \"PDF_EXISTS\" || echo \"PDF_NOT_FOUND\"",
  "description": "Check if paper PDF exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/main.pdf 2>/dev/null && echo \"PDF_EXISTS\" || echo \"PDF_NOT_FOUND\"",
    "description": "Check if paper PDF exists"
  }
}
```

</details>

---


### Tool result

_source line 2813 · 2026-05-21T04:24:36.280555+00:00_

-rw-r--r-- 1 ubuntu ubuntu 2580057 May 21 04:18 /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/main.pdf
PDF_EXISTS

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2814 · 2026-05-21T04:24:58.175388+00:00_

called mcp__agent-ml-research__dispatch_visual_check

<details open><summary>🔧 Tool call — mcp__agent-ml-research__dispatch_visual_check</summary>

```json
{
  "project": "gen-depth-fingerprint",
  "review_chat_id": "oc_999770e4e57bfc6eabd12fc1f64af1ef"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "tool_args": {
    "project": "gen-depth-fingerprint",
    "review_chat_id": "oc_999770e4e57bfc6eabd12fc1f64af1ef"
  }
}
```

</details>

---


### Tool result

_source line 2815 · 2026-05-21T04:25:12.143002+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 13967
}
```

</details>

---


### Tool call

_source line 2816 · 2026-05-21T04:25:12.293896+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "project": "gen-depth-fingerprint",
  "text": "你是 Reviewer 1，负责**方法严谨性与实验设计**的审查。\n\n## 投稿信息\n- **Venue**: EMNLP 2026（通过 ARR May 2026 cycle 提交）\n- **Deadline**: 2026-05-25\n- **格式**: Long paper，正文 8 页 + 无限参考文献，ACL 模板，double-blind\n- **Limitations section**: 必须有，不计入页数限制\n- **论文路径**: projects/gen-depth-fingerprint/docs/paper/main.tex\n- **PDF 路径**: /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/main.pdf\n\n## 你的审查侧重\n\n### 1. 方法论严谨性\n- DDR/特征工程的理论基础是否充分？特征选择是否有信息论或统计支撑？\n- 是否存在数据泄漏风险（如训练/测试集划分、特征计算是否用到目标信息）？\n- 实验设计是否存在混淆因素（如文本长度、领域、prompt 类型）？\n\n### 2. 统计有效性\n- 分类性能指标是否有置信区间或显著性检验？\n- 消融实验是否充分（特征消融、模型消融、数据消融）？\n- 样本量是否足够支撑结论？\n\n### 3. Baseline 公平性\n- baseline 选择是否全面且公平？是否有遗漏的关键 baseline？\n- baseline 和提出方法是否在同等条件下（相同数据、相同预处理、相同超参搜索空间）比较？\n- 是否有 oracle/上界对比？\n\n### 4. 可复现性\n- 实验设置细节是否完整（超参数、数据处理流程、软件版本）？\n- 是否提供代码/数据？\n\n### 5. 格式合规\n- 正文是否超过 8 页？\n- Limitations section 是否存在？\n- 是否有违反匿名规则的地方？\n\n请严格、客观、不留情面地审稿。输出结构：Summary → Strengths → Weaknesses（逐条编号，标注 severity: critical/major/minor） → Questions → Missing References → Overall Assessment（评分 + 置信度）。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "project": "gen-depth-fingerprint",
    "text": "你是 Reviewer 1，负责**方法严谨性与实验设计**的审查。\n\n## 投稿信息\n- **Venue**: EMNLP 2026（通过 ARR May 2026 cycle 提交）\n- **Deadline**: 2026-05-25\n- **格式**: Long paper，正文 8 页 + 无限参考文献，ACL 模板，double-blind\n- **Limitations section**: 必须有，不计入页数限制\n- **论文路径**: projects/gen-depth-fingerprint/docs/paper/main.tex\n- **PDF 路径**: /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/main.pdf\n\n## 你的审查侧重\n\n### 1. 方法论严谨性\n- DDR/特征工程的理论基础是否充分？特征选择是否有信息论或统计支撑？\n- 是否存在数据泄漏风险（如训练/测试集划分、特征计算是否用到目标信息）？\n- 实验设计是否存在混淆因素（如文本长度、领域、prompt 类型）？\n\n### 2. 统计有效性\n- 分类性能指标是否有置信区间或显著性检验？\n- 消融实验是否充分（特征消融、模型消融、数据消融）？\n- 样本量是否足够支撑结论？\n\n### 3. Baseline 公平性\n- baseline 选择是否全面且公平？是否有遗漏的关键 baseline？\n- baseline 和提出方法是否在同等条件下（相同数据、相同预处理、相同超参搜索空间）比较？\n- 是否有 oracle/上界对比？\n\n### 4. 可复现性\n- 实验设置细节是否完整（超参数、数据处理流程、软件版本）？\n- 是否提供代码/数据？\n\n### 5. 格式合规\n- 正文是否超过 8 页？\n- Limitations section 是否存在？\n- 是否有违反匿名规则的地方？\n\n请严格、客观、不留情面地审稿。输出结构：Summary → Strengths → Weaknesses（逐条编号，标注 severity: critical/major/minor） → Questions → Missing References → Overall Assessment（评分 + 置信度）。"
  }
}
```

</details>

---


### Tool result

_source line 2817 · 2026-05-21T04:25:25.483007+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 13189
}
```

</details>

---


### Tool call

_source line 2818 · 2026-05-21T04:25:25.634802+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "project": "gen-depth-fingerprint",
  "text": "你是 Reviewer 2，负责**新颖性与完整性**的审查。\n\n## 投稿信息\n- **Venue**: EMNLP 2026（通过 ARR May 2026 cycle 提交）\n- **Deadline**: 2026-05-25\n- **格式**: Long paper，正文 8 页 + 无限参考文献，ACL 模板，double-blind\n- **Limitations section**: 必须有，不计入页数限制\n- **论文路径**: projects/gen-depth-fingerprint/docs/paper/main.tex\n- **PDF 路径**: /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/main.pdf\n\n## 你的审查侧重\n\n### 1. 新颖性评估\n- \"Depth fingerprinting\" 作为概念的原创性如何？是否只是已有检测方法的简单延伸？\n- DDR (Differential Depth Response) 特征是否有真正的技术创新？还是标准 NLP 特征的重新包装？\n- 这篇工作相对于 AI text detection、model collapse、iterative rewriting 等已有文献的增量贡献有多大？\n\n### 2. Related Work 覆盖\n- 是否遗漏了关键相关工作？特别关注：\n  - AI text detection（DetectGPT, Fast-DetectGPT, watermarking approaches, Binoculars 等）\n  - Model collapse / iterative generation（Shumailov et al., Dohmatob et al.）\n  - Text provenance / fingerprinting\n  - Stylistic analysis of machine-generated text\n- 对相关工作的 positioning 是否准确、公平？\n\n### 3. Story 完整性与叙事质量\n- Abstract → Introduction → Method → Results → Discussion → Conclusion 的逻辑链是否连贯？\n- 动机是否令人信服？为什么 depth detection 重要？应用场景是否切实？\n- Claims 与 evidence 是否匹配？是否有 overclaim？\n- Discussion 是否充分讨论了局限性和未来方向？\n\n### 4. 写作质量\n- 英文学术写作水平如何？用词是否精准专业？\n- 是否有 AI 痕迹（过度使用 \"crucial\"、\"comprehensive\"、\"delve\" 等词）？\n- 图表标题和说明是否信息充足？\n- 段落组织和节奏是否得当？\n\n### 5. 格式与呈现\n- 正文是否控制在 8 页以内？\n- 图表是否清晰、有信息密度？\n- 参考文献格式是否一致？\n\n请严格、客观、不留情面地审稿。输出结构：Summary → Strengths → Weaknesses（逐条编号，标注 severity: critical/major/minor） → Questions → Missing References → Overall Assessment（评分 + 置信度）。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "project": "gen-depth-fingerprint",
    "text": "你是 Reviewer 2，负责**新颖性与完整性**的审查。\n\n## 投稿信息\n- **Venue**: EMNLP 2026（通过 ARR May 2026 cycle 提交）\n- **Deadline**: 2026-05-25\n- **格式**: Long paper，正文 8 页 + 无限参考文献，ACL 模板，double-blind\n- **Limitations section**: 必须有，不计入页数限制\n- **论文路径**: projects/gen-depth-fingerprint/docs/paper/main.tex\n- **PDF 路径**: /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/main.pdf\n\n## 你的审查侧重\n\n### 1. 新颖性评估\n- \"Depth fingerprinting\" 作为概念的原创性如何？是否只是已有检测方法的简单延伸？\n- DDR (Differential Depth Response) 特征是否有真正的技术创新？还是标准 NLP 特征的重新包装？\n- 这篇工作相对于 AI text detection、model collapse、iterative rewriting 等已有文献的增量贡献有多大？\n\n### 2. Related Work 覆盖\n- 是否遗漏了关键相关工作？特别关注：\n  - AI text detection（DetectGPT, Fast-DetectGPT, watermarking approaches, Binoculars 等）\n  - Model collapse / iterative generation（Shumailov et al., Dohmatob et al.）\n  - Text provenance / fingerprinting\n  - Stylistic analysis of machine-generated text\n- 对相关工作的 positioning 是否准确、公平？\n\n### 3. Story 完整性与叙事质量\n- Abstract → Introduction → Method → Results → Discussion → Conclusion 的逻辑链是否连贯？\n- 动机是否令人信服？为什么 depth detection 重要？应用场景是否切实？\n- Claims 与 evidence 是否匹配？是否有 overclaim？\n- Discussion 是否充分讨论了局限性和未来方向？\n\n### 4. 写作质量\n- 英文学术写作水平如何？用词是否精准专业？\n- 是否有 AI 痕迹（过度使用 \"crucial\"、\"comprehensive\"、\"delve\" 等词）？\n- 图表标题和说明是否信息充足？\n- 段落组织和节奏是否得当？\n\n### 5. 格式与呈现\n- 正文是否控制在 8 页以内？\n- 图表是否清晰、有信息密度？\n- 参考文献格式是否一致？\n\n请严格、客观、不留情面地审稿。输出结构：Summary → Strengths → Weaknesses（逐条编号，标注 severity: critical/major/minor） → Questions → Missing References → Overall Assessment（评分 + 置信度）。"
  }
}
```

</details>

---


### Tool result

_source line 2819 · 2026-05-21T04:25:27.199888+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1565
}
```

</details>

---


### Assistant

_source line 2820 · 2026-05-21T04:25:37.644128+00:00_

Round 1 已启动：

- ✅ **视觉审查 Agent** — 已派发（与 Reviewer 并行，fire-and-forget）
- ✅ **Reviewer 1**（方法严谨性 + 实验设计）— 已分配
- ✅ **Reviewer 2**（新颖性 + 完整性）— 已分配

等待两位 Reviewer 返回初审结果，收到后进入交叉分享阶段（Step 2）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director"
}
```

</details>

---


## Round 249

## Round 249

2 recorded events


### User

_source line 2821 · 2026-05-21T04:32:49.032728+00:00_

[Reviewer 2 审稿意见]:

# Reviewer 2 审稿报告：Depth Fingerprinting: Detecting Recursive Generation Depth in LLM Text Chains

## 总体评分
**Overall**: 3.0 (Findings)
**Confidence**: 4/5（熟悉 AI text detection 和 NLP 评估方法论，仔细阅读了全文含 33 页附录）
**一句话总结**: 任务定义新颖、实证分析极其扎实，但技术创新有限（标准特征+标准分类器），核心结果偏弱（binary F1=0.694），且实际适用场景受限于 base model + 英文的实验范围，适合 Findings 但不够主会议。

---

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| **Soundness** | 4/5 | 方法论严谨：LOGO 交叉验证、TOST 等价性检验、length confound 控制、多维消融，极少有实证论文做到这个程度。扣分原因：depth 2-4 合并为 gen-2+ 后实际只是 binary 任务（§4.2 承认 "depth resolution is bounded at three classes"），削弱了 "depth fingerprinting" 的完整性。 |
| **Excitement** | 2.5/5 | 任务角度新颖（从 binary detection 扩展到 ordinal depth），但手工特征+XGBoost 方案技术壁垒低，headline F1=0.694 对实际部署意义有限。QLoRA 端到端方案（F1~0.9）效果显著更好但被放在附录，主贡献的实用价值存疑。 |
| **Reproducibility** | 4/5 | 明确承诺释放代码/数据/模型（Ethics Statement），生成器和参考模型均为公开模型，超参数详细（§3, Appendix A）。唯一缺陷是部分消融实验的种子选择细节不完整。 |

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] **"Depth fingerprinting" 的实际分辨率与标题承诺不符**
- 具体位置：§4.2 ("depth resolution is bounded at three classes... with depths 2-4 mutually indistinguishable"), Appendix D (5-class F1 drops to 0.50 in 6-gen LOGO subset), Limitations §7
- 问题：论文标题和 Abstract 声称 "detecting recursive generation depth"，暗示可以区分具体的 depth 级别。但实际上，系统的有效分辨率仅为 gen-0 / gen-1 / gen-2+，本质上是一个三分类（实操中 gen-0 接近 perfect，所以核心贡献是 gen-1 vs. gen-2+ 的 binary 区分）。5-class 细粒度分类在 LOGO 下严重退化。这构成 overclaim：论文宣称 "depth fingerprinting" 但只能可靠区分 "生成过一次" vs. "生成过多次"。
- 为什么影响接收：核心 claim 与实验证据之间存在显著 gap，reviewer 对论文 positioning 的信任度降低。
- 建议修改方向：（1）在标题/Abstract 中更准确地表述能力边界，如 "detecting whether text has undergone single vs. multiple recursive generations"；（2）将 5-class 结果从附录提升到正文，正面讨论分辨率天花板的理论/实践含义。

**N2** [critical] **手工特征方案 vs. 端到端方案的定位失衡**
- 具体位置：§4.1 (binary F1=0.694 for 7-feature ensemble), Appendix E (QLoRA binary F1=0.905, 3-class F1=0.89-0.91)
- 问题：论文主贡献是 7 个手工特征的 DDR 分解框架（F1=0.694），但 Appendix E 的 QLoRA 端到端方案在相同评估协议下达到 F1=0.905——性能差距 >0.2。论文用 "可解释性" 为主打手工特征辩护（§4.1: "establishing the analytical framework—not the specific features—as the primary contribution"），但这个论点薄弱：（a）如果目标是可解释性，那么应该用可解释性的量化指标来比较两种方案；（b）如果目标是实用，手工特征方案的 30% 错误率使其难以部署；（c）这种安排让读者觉得 "真正有效的方法被藏在附录里"。
- 为什么影响接收：核心贡献的价值主张不清晰——既不是最有效的方法，"可解释性优势" 也未被严格论证。
- 建议修改方向：（1）将 QLoRA 对比提升到正文，作为 "accuracy-interpretability tradeoff" 正面讨论；（2）或者重新定位论文为 "empirical analysis paper"，将手工特征视为分析工具而非部署方案。

**N3** [critical] **仅限 base model 的实验范围严重限制贡献的普适性**
- 具体位置：§3.2（8 个生成器全部是 base model），Limitations §7（"extending the method to RLHF-aligned models... requires addressing confounds"），Appendix K（instruction-tuned 分析）
- 问题：所有主实验的生成器都是 base model（0.6B-7B），使用 open-ended continuation 作为生成方式。在 2026 年的实际场景中，绝大多数 LLM 生成文本来自 instruction-tuned/RLHF 模型。Appendix K 提供了有限的 instruction-tuned 分析，但结果令人担忧：DDR partition 被 "substantially compressed"，分类性能退化，引用的 Qwen3-instruct 结果出现 "3-class inversion"。这意味着核心发现（DDR 分解、drifting/non-drifting partition）可能不适用于最常见的 LLM 使用场景。
- 为什么影响接收：论文声称 DDR 是 recursive generation 的 "structural property"（Abstract），但如果该属性在 instruction-tuned 模型上不成立，则贡献的实际影响力大幅缩减。
- 建议修改方向：（1）至少在正文中纳入 2-3 个主流 instruction-tuned 模型（如 Llama-3-8B-Instruct, Qwen2.5-7B-Instruct）的完整评估；（2）若无法完成，则需在 Abstract/Introduction 中明确限定 "base-model generation chains" 而非笼统的 "LLM text chains"。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [major] **DDR "drifting/non-drifting" 分解的新颖性被过度包装**
- 具体位置：§1 ("our novel observation here is that..."), §3.3 ("these features exhibit a differential depth response"), §4.2 全节, Appendix V
- 问题：DDR 分解的核心发现是——随着 recursive generation depth 增加，entropy mean/TTR/hapax ratio 单调漂移（drifting），而 entropy max/min/tail_decay 保持稳定（non-drifting）。这一观察本身是有趣的，但从已有 model collapse 文献的角度看并不令人意外：Shumailov et al. (2024) 已经描述了 iterative generation 导致分布的 "location shift + tail erosion"；Geng et al. (2026) 在 Table 41 的对比中明确提到 "greedy decoding collapses to 1-4 recurrent outputs"。DDR 分解本质上是用 k-means 在 7 个特征上做了聚类验证（silhouette=0.660），将已知现象量化——这是有价值的实证贡献，但论文将其包装为 "novel observation"（§1）和 "primary contribution"（§1 Contributions 第 1 点）过度了。
- 建议：诚实地定位为 "quantitative characterization of a known phenomenon"，而非 "novel observation"。

**W2** [major] **与 concurrent work（Mohamed et al. 2025, Geng et al. 2026）的区分不够清晰**
- 具体位置：§2.2 简要提及，Table 41（Appendix Z.5，最后一页）
- 问题：Mohamed et al. (2025, "LLM as a Broken Telephone") 和 Geng et al. (2026, "Markovian Generation Chains") 都研究了 iterative LLM generation 的分布变化。Table 41 提供了三方对比，但被放在附录最后一页。从对比来看，本文的独特贡献是 (a) 将分析框架化为分类任务 (b) DDR 分解。但 (a) 中分类性能有限，(b) 的新颖性如 W1 所述有争议。论文应在正文 Related Work 中更深入地讨论与这两篇 concurrent work 的区别和互补性，而非仅在附录中一带而过。
- 建议：将 Table 41 的核心对比内容移入 §2.2，明确阐述本文的增量贡献相对于这两篇工作的具体差异。

**W3** [major] **Reference model 依赖未充分讨论**
- 具体位置：§3.3（"A held-out reference model (Pythia-410M)"）
- 问题：7 个特征中有 5 个依赖参考模型（Pythia-410M）计算 token-level NLL。这引入了一个强假设：用户需要有参考模型，且该模型必须与目标文本的分布有合理匹配。Appendix S 测试了 cross-family reference model 但仅限于 Pythia-410M vs. OLMo-2-1B。论文未讨论：（a）参考模型大小对结果的影响；（b）参考模型与生成器模型距离过大或过小时的行为；（c）与无需参考模型的检测方法（如 TTR/hapax ratio 单独使用）的 tradeoff。Table 2 显示 surface-only features (TTR + hapax) 的 F1 = 0.688，与 full 7-feature 的 0.708 差距很小（+0.02），这暗示参考模型特征的边际贡献可能不值得其额外依赖。
- 建议：在 Discussion 中加入 "reference model dependency" 段落，讨论 surface-only 特征接近全特征性能的含义。

**W4** [minor] **部分实验设计的混淆变量控制不完整**
- 具体位置：§3.2（"We use shared seeds across generators"）, §4.1
- 问题：所有生成器共享同一批 seed。虽然论文用 LOGO 排除了 generator-level leakage，但 seed-level leakage 的控制仅在 Appendix T 中简要讨论。Appendix T 显示 independent-seed 与 shared-seed 的 F1 差距 < 1.4 pp，表明 seed sharing 不是主要问题，但该分析仅在 3 个生成器（Pythia-2.8B, OLMo-2-1B, Qwen3-1.7B）上进行，样本量小（200 seeds per domain × 3 domains）。此外，LOGO 的 fold 数等于生成器数（8），意味着每个 fold 排除 1 个生成器——如果某些生成器的训练数据重叠（如 Pythia 和 OLMo 都部分训练于 The Pile/Dolma），LOGO 可能高估了泛化能力。
- 建议：讨论生成器之间训练数据重叠对 LOGO 泛化性估计的潜在影响。

---

## 小问题（不影响接收）

**M1** [minor] **Abstract 信息密度可优化**：Abstract 最后一句 "current applicability is restricted to base models" 是重要的 scope limitation，但被放在最后一句容易被忽略。建议前置到 method 描述处，如 "across eight base-model generators (scope limited to base models)"。

**M2** [minor] **Figure 3 的 x 轴（inference cost）刻度不直观**：Figure 3 用 "binary F1 vs. inference cost" 对比检测方法，但 inference cost 的单位和计算方式未在图标题中说明，需要翻到 §4.3 正文才能理解。

**M3** [minor] **引用格式一致性**：大部分引用格式一致，但 `aaronson_watermark` (2022) 类型为 `misc`（Technical Talk），其他均为正式出版物。考虑用脚注引用非正式来源。

**M4** [minor] **Appendix 过于庞大**（25 页），部分内容（如 Appendix X 定性示例仅 1 页、Appendix W 生成器列表）信息量低，可考虑精简或合并。

---

## 缺失的相关工作

论文的 Related Work 覆盖面已经相当全面（67 篇引用，经验证全部真实），但以下方向可考虑补充：

1. **Text provenance 和 supply chain tracking**：论文提到 "provenance" 但未引用 digital provenance / content authenticity 领域的工作，如 C2PA (Coalition for Content Provenance and Authenticity) 标准和相关技术文献。虽然这些侧重多媒体，但概念上与 text provenance tracking 相关。

2. **Supervised neural detection baselines for depth task**：论文仅与 zero-shot 统计检测器对比（Table 2）。缺少与 supervised neural detector（如 fine-tuned RoBERTa/DeBERTa）在 depth 任务上的直接对比。虽然论文重点是手工特征的可解释性，但 supervised baseline 能帮助量化 "可解释性 vs. 性能" 的 tradeoff。

3. **Information-theoretic analysis of iterative generation**：Seddik et al. (2024) 从统计角度分析了 model collapse，但更广泛的 information-theoretic 视角（如 rate-distortion theory 应用于 iterative generation 的信息损失）可以为 DDR 的 "drifting" 行为提供理论基础。

---

## 主要优势

1. **新颖的任务定义**：将 recursive generation depth 从 model collapse 的副产品提升为一个独立的分类任务，这个 reframing 本身有价值，为后续研究打开了一个新方向。

2. **极其扎实的实证工作**：25 页附录覆盖了几乎所有可以想到的消融和鲁棒性检验——length confound、prompt type、temperature sensitivity、cross-domain、text perturbation、classifier alternatives、reference model variants、TOST equivalence testing、Granger causality。这是我近期审稿中见过的最 thorough 的实证分析之一。

3. **评估协议设计严谨**：LOGO 排除 generator-level leakage + 排除 gen-0 避免 trivial human/machine 分类 + length-matched subsampling 控制长度混淆——每一步都反映了对实验公平性的深思熟虑。

4. **与 model collapse 文献的有机连接**：Discussion §5 将 depth fingerprinting 与 model collapse 的 "convergence lens" 联系起来，指出 "what converges—diversity loss" 和 "what is preserved"，这个双向视角是有洞见的。

5. **写作质量整体较好**：英文学术写作水平在平均线以上，行文流畅，术语使用准确。未发现明显 AI 写作痕迹（无 "crucial"/"comprehensive"/"delve"/"landscape" 等高频 AI 词汇滥用）。段落组织和节奏得当，Introduction 的 motivation 从 re-enter generation pipelines 到 data governance 的逻辑链条清晰。

---

## Questions for Authors

1. Table 2 显示 surface-only features（TTR + hapax ratio）的 binary F1 = 0.688，仅比 7-feature ensemble 的 0.708 低 2 pp。这是否意味着不需要参考模型就能获得接近的性能？如果是，这对论文 DDR 框架的价值主张意味着什么？

2. Appendix K 显示 instruction-tuned 模型的 DDR partition 被 "substantially compressed"。你们是否测试过 depth > 2 的 instruction-tuned generation chains？如果 instruction tuning 消除了 depth signal，这是否意味着 depth fingerprinting 仅适用于 base model 这一越来越小众的使用场景？

3. 论文使用 Pythia-410M 作为固定参考模型。如果生成器是一个 much larger model（如 70B），参考模型与生成器之间的 capacity gap 是否会改变 DDR 特征的行为？

4. Binary F1 = 0.694 对应约 30% 的预测错误。对于论文声称的 "data governance" 应用场景，这个错误率是否可接受？是否有 precision/recall tradeoff 的分析（如调整分类阈值偏向 high-precision）？

---

## 格式检查

- ✅ 正文 8 页（Section 1-6 + Limitations + Ethics Statement 在第 8 页结束）
- ✅ ACL 模板，double-blind
- ✅ Limitations section 存在且实质性（§7）
- ✅ Ethics Statement 存在
- ✅ 参考文献格式基本一致
- ⚠️ 附录 25 页——虽然 ARR 允许无限附录，但体量异常庞大

---

## 总结

这是一篇实证质量极高但技术新颖性有限的 empirical analysis paper。任务定义（generation depth classification）是新颖的，实验设计和执行堪称模范。然而，三个核心限制——(1) 实际深度分辨率仅限于 gen-1 vs. gen-2+ 的 binary 区分，与 "depth fingerprinting" 的宏大标题不符；(2) 手工特征方案（F1=0.694）与附录中端到端方案（F1=0.905）的巨大性能差距使主贡献的价值定位模糊；(3) 仅 base model 实验在 2026 年限制了实际影响力——使其更适合 Findings 而非主会议。

**评分依据**：Soundness 4/5 + Excitement 2.5/5 → Overall 3.0 (Findings)。若作者能 (a) 诚实调整 framing 以匹配实际能力，(b) 将端到端方案纳入正文形成 accuracy-interpretability spectrum，(c) 补充至少 2 个 instruction-tuned 模型的完整评估，评分可上调至 3.5 (Borderline Conference)。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 2822 · 2026-05-21T04:32:57.931995+00:00_

Reviewer 2 审稿已收到。评分 3.0 (Findings)，核心问题集中在 depth 分辨率 overclaim、手工特征 vs. 端到端方案定位失衡、以及 base-model-only 范围限制。

等待 Reviewer 1 审稿返回后启动交叉分享。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director"
}
```

</details>

---


## Round 250

## Round 250

2 recorded events


### User

_source line 2823 · 2026-05-21T04:33:03.217271+00:00_

[Reviewer 2 审稿结果]:
审稿报告已提交给 Review Director。

**审稿结论摘要**：

- **Overall: 3.0 (Findings)**，Soundness 4/5，Excitement 2.5/5，Confidence 4/5
- **3 个 Critical 问题**：
  1. "Depth fingerprinting" 标题承诺与实际分辨率不符——有效区分仅限 gen-1 vs. gen-2+，构成 overclaim
  2. 手工特征方案（F1=0.694）与附录中 QLoRA 端到端方案（F1=0.905）性能差距 >0.2，主贡献价值定位模糊
  3. 仅 base model 实验，instruction-tuned 结果显示 DDR partition 退化，限制 2026 年的实际影响力
- **3 个 Major 问题**：DDR 分解新颖性被过度包装；与 concurrent work 的区分被藏在附录最后一页；reference model 依赖的 tradeoff 未充分讨论
- **主要优势**：任务定义新颖、实证分析极其扎实（25 页附录）、评估协议严谨、写作质量好

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 2824 · 2026-05-21T04:33:08.015518+00:00_

Reviewer 2 的报告已收到。等待 Reviewer 1 的报告返回后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director"
}
```

</details>

---


## Round 251

## Round 251

6 recorded events


### User

_source line 2825 · 2026-05-21T04:33:46.567486+00:00_

[Reviewer 1 审稿意见]:

## Reviewer 1 审稿报告：Depth Fingerprinting: Detecting Recursive Generation Depth in LLM Text Chains

---

## 总体评分

**Overall**: 3.5 / 5 — Borderline Conference
**Confidence**: 4 / 5 — Quite sure, I checked the important points carefully
**一句话总结**: 新颖的任务定义和扎实的实证分析框架，但 instruction-tuned 模型上的严重失效和狭窄的实验场景削弱了实际意义。

---

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| **Soundness** | 3.5/5 | DDR 分解有充分实验支撑，LOGO/LOFO 协议设计严谨；但核心 claim "DDR captures generation-process invariants" 在 instruct 模型上不成立（Appendix K: 3-gen instruct LOGO F1=0.487），理论基础仅为非正式论证 |
| **Excitement** | 3/5 | 将 AI 文本检测从二分类推广到深度估计是有趣的重新定义；DDR 的 location/shape 分解提供了新的分析视角；但实用性受限于 base model only + 单一域 |
| **Reproducibility** | 4/5 | 超参数、数据处理流程、软件版本齐全（§7 Compute budget, Software）；承诺开源代码和数据；Pythia-410M 参考模型固定且公开 |
| **Datasets** | 3/5 | 数据集设计合理（8 generators, 5 families, 37K texts），但仅限 English Wikipedia continuation chains，泛化性有限 |
| **Software** | 3/5 | 承诺发布但目前未附带代码 |

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] **Instruction-tuned 模型上 DDR 信号严重退化，实际可用性存疑**
- 具体位置：Appendix K (pp.19-20), Limitations §7 (p.8)
- 问题：主实验全部使用 base（pretrained）models。Appendix K 测试 instruction-tuned variants 后发现：(1) 3-generator instruct LOGO binary F1 = 0.487，几乎是随机水平；(2) OLMo-Instruct 几乎完全丢失深度信号（retrained F1 仍仅 0.590-0.660，远低于 base 的 0.69-0.72）；(3) instruction tuning 将 DDR partition 从 3-zone 压缩为更模糊的结构（silhouette 从 0.660 降至 0.372）。
- 为什么影响接收：论文声称 DDR 捕获的是 "generation-process invariants"（Conclusion §6: "DDR captures generation-process invariants"），但这一 claim 在 instruction-tuned 模型上不成立。而现实中几乎所有部署的 LLM 都经过 instruction tuning。这使得论文的 framing 从 "检测 recursive generation depth 的通用工具" 退化为 "base model continuation chain 上的现象描述"。
- 建议修改方向：(1) 将 Conclusion 中的 "generation-process invariants" 改为更受限的表述；(2) 至少在 main paper 正文中用一段报告 instruct 结果而非仅放在 Appendix；(3) 讨论为什么 alignment 会破坏 DDR 并提出可能的修复方向。

**N2** [critical] **特征集不优于已有检测分数的组合，分类贡献被高估**
- 具体位置：Table 2 (p.7), §4.3 (p.7)
- 问题：Table 2 显示 4-detector ensemble (Avg-LogProb + FastDetectGPT + LD-Score + Binoculars) 在同一 XGBoost+LOGO 条件下 binary F1 = 0.706，而 7-feature DDR ensemble = 0.705。4-det + surface combined = 0.708。DDR 特征在分类性能上并未超越已有检测分数的简单组合。论文在 §4.3 末尾承认 "DDR's primary contribution is not classification performance"，但 Abstract 和 Introduction 中 "surpassing individual detection baselines" 的措辞选择性地突出了优于*单个* baseline 的结论，可能误导读者。
- 为什么影响接收：如果 DDR 特征的分类性能不优于 baseline 组合，论文的贡献仅限于分析框架（DDR decomposition），而非实际的检测工具。这需要在 framing 中更坦诚地反映。
- 建议修改方向：(1) Abstract 中补充 DDR 特征与 baseline ensemble 性能相当的信息；(2) 更清楚地将论文定位为 empirical analysis paper 而非 detection method paper。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [major] **实验范围过窄：仅 English Wikipedia + continuation prompting + nucleus sampling**
- 具体位置：§3.2 (p.3), Appendix J (pp.18-19), Appendix H (p.17), Limitations §7 (p.8)
- 问题：(1) 所有 seed texts 来自 English Wikipedia，cross-domain 实验（Appendix J）仅 200 seeds/domain，且 binary F1 从 0.692 降至 0.647；(2) 仅 continuation prompting（"Continue the following text"），未测试 instruction-following、QA、摘要等真实使用场景；(3) 固定 nucleus sampling p=0.9, τ≤0.7，Appendix H 显示温度敏感性存在 generator-dependent 差异（Qwen3-1.7B F1 从 0.948 降至 0.418 in cross-temperature conditions）。
- 建议：至少扩展一个非 continuation prompting 任务（如 instruction-following），展示 DDR 在不同生成范式下的鲁棒性。

**W2** [major] **DDR 理论基础薄弱，缺少信息论或统计学正式推导**
- 具体位置：§3.1 (p.3), §5 (p.7-8)
- 问题：DDR 的核心直觉——"decoding mechanism systematically compresses where the output distribution sits while preserving its higher-order form"——仅为非正式论证。论文未提供：(1) 为什么这 7 个特征是充分的（或最优的）的信息论论证；(2) NLL location 单调递减的形式化证明（即使在简化假设下）；(3) shape features 近似不变的解析解释。Section 5 的 Discussion 试图从 model collapse 文献桥接，但连接不紧密。
- 建议：即使完整理论推导超出范围，至少可以在简化设置（如 temperature scaling 的马尔可夫链）下证明 entropy 单调递减，为实证发现提供理论锚点。

**W3** [major] **LOFO 跨家族泛化 F1 = 0.634，显示约 9% 的信号来自 family-specific artifacts**
- 具体位置：Table 5 (p.5), §4.1 (p.5)
- 问题：LOGO F1 = 0.694 vs LOFO F1 = 0.634，差距 6pp。LOFO 是更严格的测试（hold out entire family），F1 下降说明 classifier 部分依赖 family-specific 信号（如 tokenizer 差异、training data 分布）。Table 5 进一步显示 per-class F1 averaged across all six LOFO folds：gen-0 F1 = 0.921，gen-1 F1 = 0.634，gen-2+ F1 = 0.268 / 0.259 / 0.453。gen-2+ 的 F1 极低（0.268-0.453），说明深度较大的样本在跨家族条件下几乎无法被正确分类。
- 建议：分析 LOFO 失败案例——哪些 family 被 hold out 时 F1 下降最大？是否与 model scale 相关？

**W4** [major] **Binary task 排除 gen-0，headline metric 不反映完整实际场景**
- 具体位置：§3.4 (p.4), §4.1 (p.4-5)
- 问题：主 metric "leak-free binary F1 = 0.694" 定义为 gen-1 vs gen-2+，完全排除 gen-0（human text）。这是为了避免 gen-0 过于容易分类而膨胀 F1（论文已解释），但实际应用需要回答 "这段文本是人类写的、生成一次的、还是多次递归生成的？"。3-class LOGO F1 = 0.789（Table 1），但其中 gen-0 near-perfect（F1 > 0.9），gen-2+ F1 仅约 0.60-0.70（Table 4），这一不均衡应该在 main paper 中更显著地呈现。
- 建议：在 main paper 中展示 per-class F1 breakdown，而非仅在附录（Table 4）中报告。

**W5** [minor→major] **缺失 fine-tuned transformer baseline under LOGO**
- 具体位置：§4.3 (p.7), Appendix E (p.15)
- 问题：Appendix E 显示 QLoRA end-to-end classifier 在 within-model 5-fold CV 下达到 3-class F1 = 0.905，远超 7-feature XGBoost。但 QLoRA 实验使用的是 within-model CV 而非 LOGO，因此不可直接对比。缺少关键实验：fine-tuned transformer（如 RoBERTa/DeBERTa）在 LOGO 下的表现。这将回答核心问题——是 handcrafted features 足以捕获 depth signal，还是需要更丰富的表示？
- 建议：在 LOGO 协议下跑一个 fine-tuned small LM baseline，与 7-feature XGBoost 直接对比。

---

## 小问题（不影响接收）

- **M1** [minor] TOST 等价性检验（Appendix U）使用 d=0.20 作为等价边界，但未充分 justify 这一阈值选择。Cohen's d=0.20 是 "small effect" 标准，但在此 context 下什么算 "practically meaningful equivalence" 需要 domain-specific 论证。
- **M2** [minor] Table 1 和 Table 2 中 "N/T" (not profiled) 标注的 ms/text 列不一致——7-feature ensemble 在 Table 2 标 N/T 但在 Table 1 没有推理成本信息。如果 DDR 特征的计算成本是优势之一，应该完整报告。
- **M3** [minor] Figure 1 (p.6) strip plot 的颜色编码与 Figure 2 (p.7) 不一致——Figure 1 用不同颜色区分 generator，Figure 2 用颜色区分 feature group。建议统一 colormap。
- **M4** [minor] 引用格式：部分 arXiv preprint（如 ld_score, feat_aug_transformer, chainwash）标注为 2026 年发表，但作为 preprint 可能尚未经过同行评审。建议区分已发表和 preprint 的引用。
- **M5** [minor] Appendix Z.4 (p.31) 讨论 9-generator 评估（添加 Gemma-2-2B），发现 Gemma 表现异常（gen-0→gen-1 F1 = 0.036，几乎完全失败）。论文将此归因于 "architecture-specific generalization limitation"，但未排除数据质量问题（Gemma 的 SentencePiece tokenizer 与其他 BPE tokenizer 差异）。

---

## 缺失引用

- **Liang et al. (2024)** "Monitoring AI-Modified Content at Scale" 已引用，但未引用同时期的 **Guo et al. (2023)** "How Close is ChatGPT to Human Experts? Comparison Corpus, Evaluation, and Detection" (AAAI)，这是一篇研究 LLM 输出统计特征的相关工作。
- 论文讨论了 model collapse 但未引用 **Briesch et al. (2023)** "Large Language Models Suffer From Their Own Output" 或 **Padmakumar & He (2024)** "Does Writing with Language Models Reduce Content Diversity?" 后者虽引用但在 Related Work 中讨论不足。
- 深度估计作为 ordinal regression 的 framing 可以引用 **Diaz & Karampatziakis (2019)** "Soft Labels for Ordinal Regression" 作为方法论参考。

---

## 主要优势

1. **新颖且定义良好的任务**：将 AI 文本检测从 binary (human vs machine) 推广到 ordinal depth estimation 是一个有意义的概念贡献。DDR 的 drifting/stationary 分解提供了一个分析 iterative generation 的新框架。
2. **评估协议设计严谨**：LOGO (leave-one-generator-out) + LOFO (leave-one-family-out) 双重交叉验证确保了 claim 的泛化性；seed-sharing 控制实验（Appendix T）、length-matched subsampling（§4.1, Appendix B）、temperature sensitivity（Appendix H）等混淆因素控制系统而全面。
3. **实验深度突出**：25+ 附录涵盖了几乎所有可预见的 reviewer concern（DDR partition 验证、TOST 等价检验、Granger 因果性、confusion matrix、UMAP、cross-domain、cross-temperature、perturbation robustness 等）。这一实验覆盖度在 empirical NLP 论文中属于上乘。
4. **统计学严谨**：全面使用 Bootstrap 95% CI、Cohen's d、TOST 等价检验、Spearman 相关、Granger causality 等统计工具。Appendix V 的 exhaustive partition enumeration 和 bootstrap stability 分析尤其令人印象深刻。
5. **可解释性**：7 个 handcrafted features 的设计允许清晰的 ablation 和 feature-level 解释，与黑盒 neural 方法形成有意义的对比。LOFO 分析（Table 7）清楚展示了每个 feature 的边际贡献。

---

## 格式合规

- **正文页数**：8 页正文（至 §7 Limitations + Ethics Statement），符合 EMNLP Long paper 8 页限制 ✓
- **Limitations section**：存在（§7, p.8），内容充实 ✓
- **匿名**：标题页标注 "Anonymous ACL submission"，全文未发现违反匿名规则之处 ✓
- **References**：67 条引用，0 orphan / 0 missing，在线验证 56/67 confirmed（其余为 API 索引限制导致的 false negative，非假引用）✓


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 2826 · 2026-05-21T04:34:30.530185+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "project": "gen-depth-fingerprint",
  "text": "## 交叉分享：Reviewer 2 的完整审稿意见\n\n请逐条回应 Reviewer 2 的每个发现：\n- **[AGREE]**：同意并说明理由\n- **[REBUT]**：反驳并提供具体证据（cite Section/Table/Figure）\n\n---\n\n以下是 Reviewer 2 的完整审稿原文：\n\n### Overall: 3.0 (Findings), Confidence 4/5, Soundness 4/5, Excitement 2.5/5\n\n### Must-Fix (Critical)\n\n**N1** \"Depth fingerprinting\" 的实际分辨率与标题承诺不符\n- §4.2 (\"depth resolution is bounded at three classes... with depths 2-4 mutually indistinguishable\"), Appendix D (5-class F1 drops to 0.50 in 6-gen LOGO subset)\n- 系统有效分辨率仅为 gen-0/gen-1/gen-2+，本质上核心贡献是 gen-1 vs. gen-2+ 的 binary 区分。标题声称 \"detecting recursive generation depth\" 构成 overclaim。\n\n**N2** 手工特征方案 vs. 端到端方案的定位失衡\n- §4.1 binary F1=0.694 for 7-feature ensemble vs Appendix E QLoRA binary F1=0.905，性能差距 >0.2\n- \"可解释性\"辩护薄弱：(a) 未用可解释性量化指标比较；(b) 30% 错误率难以部署；(c) \"真正有效的方法被藏在附录里\"\n\n**N3** 仅限 base model 实验严重限制贡献普适性\n- 8 个生成器全是 base model。Appendix K instruction-tuned 结果：DDR partition 被 \"substantially compressed\"，Qwen3-instruct 出现 \"3-class inversion\"\n- 论文声称 DDR 是 \"structural property\" 但在 instruction-tuned 上不成立\n\n### Should-Fix (Major)\n\n**W1** DDR \"drifting/non-drifting\" 分解新颖性被过度包装——Shumailov et al. (2024) 已描述 \"location shift + tail erosion\"，DDR 本质是用 k-means 量化已知现象\n\n**W2** 与 concurrent work（Mohamed et al. 2025, Geng et al. 2026）的区分被藏在附录最后一页（Table 41），应在正文 §2.2 深入讨论\n\n**W3** Reference model 依赖未充分讨论——Table 2 显示 surface-only (TTR+hapax) F1=0.688 vs full 7-feature F1=0.708，仅差 2pp，暗示参考模型边际贡献有限\n\n### Minor\n\n**M1** Abstract scope limitation 放在最后一句容易被忽略\n**M2** Figure 3 x 轴 inference cost 单位未在图标题中说明\n**M3** aaronson_watermark 引用格式（misc vs 正式出版物）\n**M4** Appendix 25 页过于庞大\n\n### 缺失引用\n1. C2PA content provenance 标准\n2. Supervised neural detector (RoBERTa/DeBERTa) 在 depth task 的对比\n3. Information-theoretic analysis of iterative generation\n\n### Questions\n1. Surface-only F1=0.688 vs 7-feature F1=0.708 仅差 2pp，是否不需要参考模型？\n2. Instruction-tuned depth > 2 链是否测试过？\n3. 参考模型 capacity gap（410M vs 70B）的影响？\n4. Binary F1=0.694 对应 30% 错误率，data governance 场景是否可接受？\n\n---\n\n请对以上每个 N/W/M/Question 逐条给出 [AGREE] 或 [REBUT] 回应。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "project": "gen-depth-fingerprint",
    "text": "## 交叉分享：Reviewer 2 的完整审稿意见\n\n请逐条回应 Reviewer 2 的每个发现：\n- **[AGREE]**：同意并说明理由\n- **[REBUT]**：反驳并提供具体证据（cite Section/Table/Figure）\n\n---\n\n以下是 Reviewer 2 的完整审稿原文：\n\n### Overall: 3.0 (Findings), Confidence 4/5, Soundness 4/5, Excitement 2.5/5\n\n### Must-Fix (Critical)\n\n**N1** \"Depth fingerprinting\" 的实际分辨率与标题承诺不符\n- §4.2 (\"depth resolution is bounded at three classes... with depths 2-4 mutually indistinguishable\"), Appendix D (5-class F1 drops to 0.50 in 6-gen LOGO subset)\n- 系统有效分辨率仅为 gen-0/gen-1/gen-2+，本质上核心贡献是 gen-1 vs. gen-2+ 的 binary 区分。标题声称 \"detecting recursive generation depth\" 构成 overclaim。\n\n**N2** 手工特征方案 vs. 端到端方案的定位失衡\n- §4.1 binary F1=0.694 for 7-feature ensemble vs Appendix E QLoRA binary F1=0.905，性能差距 >0.2\n- \"可解释性\"辩护薄弱：(a) 未用可解释性量化指标比较；(b) 30% 错误率难以部署；(c) \"真正有效的方法被藏在附录里\"\n\n**N3** 仅限 base model 实验严重限制贡献普适性\n- 8 个生成器全是 base model。Appendix K instruction-tuned 结果：DDR partition 被 \"substantially compressed\"，Qwen3-instruct 出现 \"3-class inversion\"\n- 论文声称 DDR 是 \"structural property\" 但在 instruction-tuned 上不成立\n\n### Should-Fix (Major)\n\n**W1** DDR \"drifting/non-drifting\" 分解新颖性被过度包装——Shumailov et al. (2024) 已描述 \"location shift + tail erosion\"，DDR 本质是用 k-means 量化已知现象\n\n**W2** 与 concurrent work（Mohamed et al. 2025, Geng et al. 2026）的区分被藏在附录最后一页（Table 41），应在正文 §2.2 深入讨论\n\n**W3** Reference model 依赖未充分讨论——Table 2 显示 surface-only (TTR+hapax) F1=0.688 vs full 7-feature F1=0.708，仅差 2pp，暗示参考模型边际贡献有限\n\n### Minor\n\n**M1** Abstract scope limitation 放在最后一句容易被忽略\n**M2** Figure 3 x 轴 inference cost 单位未在图标题中说明\n**M3** aaronson_watermark 引用格式（misc vs 正式出版物）\n**M4** Appendix 25 页过于庞大\n\n### 缺失引用\n1. C2PA content provenance 标准\n2. Supervised neural detector (RoBERTa/DeBERTa) 在 depth task 的对比\n3. Information-theoretic analysis of iterative generation\n\n### Questions\n1. Surface-only F1=0.688 vs 7-feature F1=0.708 仅差 2pp，是否不需要参考模型？\n2. Instruction-tuned depth > 2 链是否测试过？\n3. 参考模型 capacity gap（410M vs 70B）的影响？\n4. Binary F1=0.694 对应 30% 错误率，data governance 场景是否可接受？\n\n---\n\n请对以上每个 N/W/M/Question 逐条给出 [AGREE] 或 [REBUT] 回应。"
  }
}
```

</details>

---


### Tool result

_source line 2827 · 2026-05-21T04:34:52.983712+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 22453
}
```

</details>

---


### Tool call

_source line 2828 · 2026-05-21T04:34:54.389752+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "project": "gen-depth-fingerprint",
  "text": "## 交叉分享：Reviewer 1 的完整审稿意见\n\n请逐条回应 Reviewer 1 的每个发现：\n- **[AGREE]**：同意并说明理由\n- **[REBUT]**：反驳并提供具体证据（cite Section/Table/Figure）\n\n---\n\n以下是 Reviewer 1 的完整审稿原文：\n\n### Overall: 3.5 (Borderline Conference), Confidence 4/5, Soundness 3.5/5, Excitement 3/5\n\n### Must-Fix (Critical)\n\n**N1** Instruction-tuned 模型上 DDR 信号严重退化，实际可用性存疑\n- Appendix K: 3-gen instruct LOGO binary F1=0.487（接近随机），OLMo-Instruct retrained F1 仅 0.590-0.660\n- Silhouette 从 0.660 降至 0.372\n- Conclusion 中 \"generation-process invariants\" claim 在 instruct 模型上不成立\n\n**N2** 特征集不优于已有检测分数的组合，分类贡献被高估\n- Table 2: 4-detector ensemble binary F1=0.706 vs 7-feature DDR F1=0.705\n- Abstract/Introduction \"surpassing individual detection baselines\" 选择性措辞可能误导读者\n\n### Should-Fix (Major)\n\n**W1** 实验范围过窄：仅 English Wikipedia + continuation prompting + nucleus sampling\n- Cross-domain F1 从 0.692 降至 0.647；温度敏感性存在 generator-dependent 差异（Qwen3-1.7B cross-temp F1 从 0.948 降至 0.418）\n\n**W2** DDR 理论基础薄弱，缺少信息论或统计学正式推导\n- \"decoding mechanism systematically compresses where the output distribution sits while preserving its higher-order form\" 仅为非正式论证\n\n**W3** LOFO 跨家族泛化 F1=0.634，显示约 9% 信号来自 family-specific artifacts\n- gen-2+ 的 LOFO per-class F1 极低（0.268-0.453）\n\n**W4** Binary task 排除 gen-0，headline metric 不反映完整实际场景\n- 3-class LOGO F1=0.789 中 gen-0 near-perfect，gen-2+ F1 仅 0.60-0.70\n\n**W5** 缺失 fine-tuned transformer baseline under LOGO\n- QLoRA 用 within-model CV 而非 LOGO，无法直接对比\n\n### Minor\n\n**M1** TOST d=0.20 阈值未充分 justify\n**M2** Table 1/2 ms/text 标注不一致\n**M3** Figure 1 和 Figure 2 颜色编码不一致\n**M4** 部分 arXiv preprint 引用标注为 2026 已发表\n**M5** Appendix Z.4 Gemma 异常未排除 tokenizer 差异\n\n### 缺失引用\n- Guo et al. (2023) \"How Close is ChatGPT to Human Experts?\" (AAAI)\n- Briesch et al. (2023) \"Large Language Models Suffer From Their Own Output\"\n- Diaz & Karampatziakis (2019) \"Soft Labels for Ordinal Regression\"\n\n### Strengths\n1. 新颖且定义良好的任务\n2. 评估协议设计严谨（LOGO+LOFO）\n3. 25+ 附录实验深度突出\n4. 统计学严谨（Bootstrap CI, Cohen's d, TOST, Granger causality）\n5. 可解释性\n\n---\n\n请对以上每个 N/W/M 逐条给出 [AGREE] 或 [REBUT] 回应。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "project": "gen-depth-fingerprint",
    "text": "## 交叉分享：Reviewer 1 的完整审稿意见\n\n请逐条回应 Reviewer 1 的每个发现：\n- **[AGREE]**：同意并说明理由\n- **[REBUT]**：反驳并提供具体证据（cite Section/Table/Figure）\n\n---\n\n以下是 Reviewer 1 的完整审稿原文：\n\n### Overall: 3.5 (Borderline Conference), Confidence 4/5, Soundness 3.5/5, Excitement 3/5\n\n### Must-Fix (Critical)\n\n**N1** Instruction-tuned 模型上 DDR 信号严重退化，实际可用性存疑\n- Appendix K: 3-gen instruct LOGO binary F1=0.487（接近随机），OLMo-Instruct retrained F1 仅 0.590-0.660\n- Silhouette 从 0.660 降至 0.372\n- Conclusion 中 \"generation-process invariants\" claim 在 instruct 模型上不成立\n\n**N2** 特征集不优于已有检测分数的组合，分类贡献被高估\n- Table 2: 4-detector ensemble binary F1=0.706 vs 7-feature DDR F1=0.705\n- Abstract/Introduction \"surpassing individual detection baselines\" 选择性措辞可能误导读者\n\n### Should-Fix (Major)\n\n**W1** 实验范围过窄：仅 English Wikipedia + continuation prompting + nucleus sampling\n- Cross-domain F1 从 0.692 降至 0.647；温度敏感性存在 generator-dependent 差异（Qwen3-1.7B cross-temp F1 从 0.948 降至 0.418）\n\n**W2** DDR 理论基础薄弱，缺少信息论或统计学正式推导\n- \"decoding mechanism systematically compresses where the output distribution sits while preserving its higher-order form\" 仅为非正式论证\n\n**W3** LOFO 跨家族泛化 F1=0.634，显示约 9% 信号来自 family-specific artifacts\n- gen-2+ 的 LOFO per-class F1 极低（0.268-0.453）\n\n**W4** Binary task 排除 gen-0，headline metric 不反映完整实际场景\n- 3-class LOGO F1=0.789 中 gen-0 near-perfect，gen-2+ F1 仅 0.60-0.70\n\n**W5** 缺失 fine-tuned transformer baseline under LOGO\n- QLoRA 用 within-model CV 而非 LOGO，无法直接对比\n\n### Minor\n\n**M1** TOST d=0.20 阈值未充分 justify\n**M2** Table 1/2 ms/text 标注不一致\n**M3** Figure 1 和 Figure 2 颜色编码不一致\n**M4** 部分 arXiv preprint 引用标注为 2026 已发表\n**M5** Appendix Z.4 Gemma 异常未排除 tokenizer 差异\n\n### 缺失引用\n- Guo et al. (2023) \"How Close is ChatGPT to Human Experts?\" (AAAI)\n- Briesch et al. (2023) \"Large Language Models Suffer From Their Own Output\"\n- Diaz & Karampatziakis (2019) \"Soft Labels for Ordinal Regression\"\n\n### Strengths\n1. 新颖且定义良好的任务\n2. 评估协议设计严谨（LOGO+LOFO）\n3. 25+ 附录实验深度突出\n4. 统计学严谨（Bootstrap CI, Cohen's d, TOST, Granger causality）\n5. 可解释性\n\n---\n\n请对以上每个 N/W/M 逐条给出 [AGREE] 或 [REBUT] 回应。"
  }
}
```

</details>

---


### Tool result

_source line 2829 · 2026-05-21T04:34:55.797760+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1408
}
```

</details>

---


### Assistant

_source line 2830 · 2026-05-21T04:34:58.899638+00:00_

交叉分享已派发。两位 Reviewer 正在逐条回应对方的审稿意见，等待交叉回应结果返回。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director"
}
```

</details>

---


## Round 252

## Round 252

2 recorded events


### User

_source line 2831 · 2026-05-21T04:35:01.555922+00:00_

[Reviewer 1 审稿结果]:
审稿报告已提交给 Review Director。

**审稿结论**：Overall 3.5/5（Borderline Conference），Soundness 3.5，Excitement 3.0。

核心判断：
- **两个 critical 问题**：(1) Instruction-tuned 模型上 DDR 信号严重退化（3-gen instruct LOGO F1 = 0.487），论文 "generation-process invariants" 的 claim 在实际部署模型上不成立；(2) 7-feature DDR ensemble 分类性能未超越已有检测分数组合（Table 2: 0.705 vs 4-det 0.706），Abstract 的 framing 有选择性。
- **四个 major 问题**：实验范围过窄（English Wikipedia + continuation only）、DDR 理论基础仅为非正式论证、LOFO 跨家族泛化下降 9%、binary metric 排除 gen-0 不反映完整场景。
- **主要优势**：任务新颖、评估协议严谨（LOGO+LOFO）、25+ 附录覆盖度极高、统计学使用规范。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 2832 · 2026-05-21T04:35:05.654831+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director"
}
```

</details>

---


## Round 253

## Round 253

2 recorded events


### User

_source line 2833 · 2026-05-21T04:36:44.668886+00:00_

[Reviewer 1 审稿意见]:

## Reviewer 1 对 Reviewer 2 审稿意见的逐条交叉回应

---

### Must-Fix

**[AGREE] R2-N1: "Depth fingerprinting" 有效分辨率仅 3 class，标题存在 overclaim**

同意。我的独立审查也确认了这一点。§4.2 明确承认 "depth resolution is bounded at three classes"，Table 4 的 5-class LOGO 显示 gen-2/gen-3/gen-4 的 per-class F1 极低（gen-2 = 0.268, gen-3 = 0.259, gen-4 = 0.453, Table 5 per-class），深度 2-4 基本不可区分。标题 "Detecting Recursive Generation Depth" 暗示逐步分辨能力，而实际系统仅能区分 "未经递归 / 递归一次 / 递归多次"。

不过我要补充一个 nuance：3-class 分辨率本身仍有实际意义（区分 "first-generation AI text" 与 "multiply-recycled text" 对数据污染检测有用），但 **标题和 abstract 应当反映这一限制**。

---

**[REBUT] R2-N2: 手工特征 vs QLoRA 的定位失衡**

部分反驳。R2 的核心论据——F1=0.694 vs QLoRA F1=0.905 差距 >0.2——存在 **评估协议不可比** 的问题：

1. **QLoRA 使用 within-model 5-fold CV**（Appendix E, p.15: "within-model 5-fold CV"），而 7-feature F1=0.694 使用 LOGO（leave-one-generator-out）。LOGO 是显著更难的泛化测试——classifier 从未见过 test generator 的任何样本。将 within-model CV 与 LOGO 直接比较在方法论上不合理。
2. **论文自身对此有明确说明**（§4.3 末段）："DDR's primary contribution is not classification performance... but the decomposition of depth signal into location-sensitive and shape-stable components."

但我同意 R2 的一个子论点：**缺少 QLoRA under LOGO 的实验是一个缺口**（我在自己的审稿 W5 中也指出了这一点）。如果 QLoRA 在 LOGO 下仍远超 7-feature，则 DDR 的分析框架价值需要重新论证。论文应补充此实验或解释为何缺失。

R2 称可解释性辩护 "薄弱" 需要量化指标——这一要求过高。在 ML safety 和 data governance 领域，handcrafted feature 的 per-feature ablation 可解释性（Table 7: LOFO 分析）本身就是一种广泛接受的可解释性形式，不必要求 SHAP/LIME 等后验方法。

---

**[AGREE] R2-N3: Base model only 严重限制贡献普适性**

完全同意，这与我的 N1 一致。Appendix K 数据毁灭性强：
- 3-gen instruct LOGO binary F1 = 0.487（接近随机）
- DDR partition silhouette 从 0.660 降至 0.372
- OLMo-Instruct 的 entropy_mean 从 near-stationary 变为 intermediate

论文 Conclusion 中 "DDR captures generation-process invariants" 在 instruct 条件下不成立。这是本文最严重的问题。

---

### Should-Fix

**[REBUT] R2-W1: DDR 新颖性被过度贬低**

R2 称 DDR "本质是用 k-means 量化已知现象"，引用 Shumailov et al. (2024) 已描述 "location shift + tail erosion"。这一对比不准确：

1. **研究对象不同**：Shumailov et al. (2024) 研究的是 **model collapse**——在递归生成数据上 *重新训练* 模型导致的分布退化。DDR 研究的是 **generation chains**——同一固定模型反复 *推理* 产生的文本统计变化。前者是 training dynamics，后者是 inference dynamics，机制完全不同。
2. **发现方向相反**：Shumailov et al. 发现 "tail erosion"（尾部分布萎缩），而 DDR 的核心发现恰恰是 **shape features (包括 tail_decay) 近似不变**（Table 26, Appendix U: TOST 对所有 near-stationary features 均 reject non-equivalence, p < 10⁻¹⁰）。这是一个 **与 model collapse 文献预期相反** 的实证发现。
3. **k-means 是验证手段而非贡献本身**：DDR 的贡献是 drifting/stationary 分解的 empirical discovery + 分类框架。Appendix V 的 k-means 和 exhaustive partition enumeration 是验证该分解 non-trivial 的工具。

R2 的批评低估了 "generation chain inference ≠ model collapse training" 这一关键区分。

---

**[AGREE] R2-W2: 与 concurrent work 的对比应放入正文**

同意。Appendix Z.5（p.33, Table 41）对 Mohamed et al. (2025) "Broken Telephone" 和 Geng et al. (2026) "Markovian Chains" 的对比被放在最后一页，大多数 reviewer 不会读到。这两篇是最直接的 concurrent work，区分点（continuation chain vs meaning-preserving paraphrase、feature decomposition vs convergence dynamics vs distributional decomposition）应在 §2.2 Related Work 中用至少一段讨论。

---

**[REBUT] R2-W3: Reference model 边际贡献被低估**

R2 引用 "surface-only F1=0.688 vs full 7-feature F1=0.708, 仅差 2pp"。这组数字有问题：

1. **3-class F1 差距为 9pp 而非 2pp**：§4.2 (p.6) 明确报告 "The full 7-feature set (F1 = 0.77) outperforms surface-only (0.68) and reference-only (0.713)"。3-class macro F1: surface-only = 0.68, full = 0.77, 差距 9pp。这不是 marginal。
2. **R2 可能混淆了不同 metric 或 condition 的数字**。Table 2 中 "4-det + surface" 的 0.708 包含了 4 个 detector scores + surface features，与 "surface-only (TTR + hapax + tail_decay)" 是不同的特征集。
3. **Reference model 提供了不可替代的信号维度**：Table 7 LOFO 分析显示 entropy_max 是单特征中影响最大的（drop = -1.5pp），且 entropy_min 虽个体冗余，但 PCA（Appendix R）显示 4 个 entropy 特征 共享一个独立的潜在维度，与 surface features 正交。

不过，我同意参考模型贡献 **应该被更明确地量化**——surface-only vs ref-only vs full 的 binary F1 对比目前仅在 3-class 下报告（§4.2），应补充 binary 维度的对比。

---

### Minor

**[AGREE] R2-M1**: Abstract scope limitation 放在最后一句确实容易被忽视。建议将 "base model, English Wikipedia" 限定提前到 contribution list 附近。

**[AGREE] R2-M2**: Figure 3 x 轴 inference cost 单位应在图标题中标注，当前仅在正文中说明。

**[AGREE] R2-M3**: aaronson_watermark 引用为 misc 类型。引用验证也确认此条 not_found（非正式出版物），应注明 "blog post" 或改引后续正式发表版本。

**[REBUT] R2-M4**: 25 页附录 "过于庞大" 不应作为负面评价。ARR 对附录无页数限制。论文的实验深度是其核心优势之一（我在审稿优势 #3 中专门提到）。附录覆盖了几乎所有可预见的 reviewer concern（DDR partition 验证、TOST、Granger causality、confusion matrix、UMAP、cross-domain、cross-temperature 等）。问题不在于附录太多，而在于 **某些关键结果（如 instruct 模型、concurrent work 对比）应从附录提升到正文**。

---

### Questions 回应

**Q1: Surface-only vs 7-feature 是否不需要参考模型？**
[REBUT] 如上 W3 所述，3-class 差距为 9pp（0.68 → 0.77），不是 2pp。参考模型特征提供了 surface features 无法捕获的 NLL location 信号维度。但需承认：如果部署场景不允许运行参考模型（如纯 CPU 环境），surface-only 仍有 0.68 的可用性。

**Q2: Instruction-tuned depth > 2 链是否测试过？**
[AGREE] 好问题。Appendix K 仅测试到 instruct 模型的 depth 0-4，但未报告 depth > 2 的 per-depth instruct 结果。如果 instruct 模型在 depth 2+ 完全收敛（如 DDR partition 压缩所暗示），则 depth > 2 的链对 instruct 模型可能完全无区分度。这应被明确讨论。

**Q3: 参考模型 capacity gap（410M vs 70B）？**
[REBUT] 论文已在 Appendix Y (p.25) 回答此问题：Cross-family reference model evaluation 使用 3 个不同参考模型，LOGO F1 spread 仅 ±0.013。此外，Appendix Z.4 (p.31-32) 测试了 14B 参数生成器（Qwen3-14B-Base），发现 DDR pattern 保持一致（Cohen's d 仍在 large-effect 范围 0.78-1.12），虽然绝对效应量略有压缩。但确实 **70B+ 规模的生成器未测试**，这是一个合理的开放问题。

**Q4: Binary F1=0.694 对应 ~30% 错误率，data governance 是否可接受？**
[AGREE] 完全同意这是一个实际部署障碍。30% 错误率在高 stakes 场景（学术不端检测、内容审核）下不可接受。论文将 classifier 定位为 "proof of concept"（§1），但未充分讨论实际 deployment 所需的性能门槛。建议在 Discussion 或 Limitations 中加入对 precision-recall tradeoff 在不同 application 下的分析。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 2834 · 2026-05-21T04:36:48.663782+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director"
}
```

</details>

---


## Round 254

## Round 254

2 recorded events


### User

_source line 2835 · 2026-05-21T04:36:52.265524+00:00_

[Reviewer 1 审稿结果]:
交叉回应已提交给 Review Director。

总结：在 R2 的 3 个 Must-Fix 中，我完全同意 N1（标题 overclaim）和 N3（base model 限制），部分反驳 N2（QLoRA 对比协议不可比）。在 3 个 Should-Fix 中，我反驳了 W1（DDR 新颖性被低估，generation chain ≠ model collapse）和 W3（reference model 贡献在 3-class 上为 9pp 非 2pp），同意 W2（concurrent work 对比应提升到正文）。4 个 Minor 中同意 3 个，反驳 M4（附录深度是优势而非劣势）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 2836 · 2026-05-21T04:36:55.951129+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director"
}
```

</details>

---


## Round 255

## Round 255

12 recorded events


### User

_source line 2837 · 2026-05-21T04:39:51.798996+00:00_

[Reviewer 2 审稿意见]:

# Reviewer 2 交叉回应：对 Reviewer 1 审稿意见的逐条评判

---

## Must-Fix (Critical)

### [AGREE] R1-N1: Instruction-tuned 模型上 DDR 信号退化

同意 R1 的判断，且我在自己的 N3 中独立提出了相同问题。补充证据：

Appendix K（page 19）论文自己承认 "instruction tuning degrades 3-class F1 by 3.7–19.9 pp across all three families"，且 DDR partition 被 "substantially compressed"。不过需要对 R1 引用的具体数字做一个 caveat：论文在 Appendix K 明确说 binary F1 变化较小（"|Δ| ≤ 3.2 pp" for within-model CV），R1 引用的 "3-gen instruct LOGO binary F1=0.487（接近随机）" 可能来自一个仅含 3 个 instruction-tuned 生成器的 LOGO 评估——该配置下 fold 数极少（仅 3 折），统计方差很大，且论文自己注明 "cross-model numbers are not directly comparable across rows"。因此 0.487 这个数字可能夸大了退化程度，but the directional conclusion stands：instruction-tuned 模型上 DDR 信号确实不可靠。

**我的补充**：更核心的问题不是具体 F1 数字，而是 Abstract 中 "structural property of fixed-parameter autoregressive sampling" 这一 claim 如果在 instruction-tuned 模型上不成立，就不能称为 "structural property"——它更像是 base-model continuation 的 empirical regularity。

### [AGREE] R1-N2: 特征集不优于已有检测分数组合

验证了 R1 的核心数据：**Table 3（page 7）明确显示 4-detector ensemble Binary F1=0.706 vs 7-feature DDR Binary F1=0.705，差距仅 0.001。** R1 的批评完全成立。

补充分析：
1. 论文 Abstract 说 "surpassing individual detection baselines" 确实是选择性措辞——Figure 3 的可视化也刻意突出 "individual detectors" 作为对比对象，而将 ensemble 比较放在相对不显眼的 Table 3 中。
2. 论文为此提出的辩护是 **cost-efficiency**（Figure 3: 7-feature 方案不需要多个检测器的 GPU 前向传播，"2.4× lower inference cost"），以及 §4.3 最后一段指出贡献在于 "the decomposition of depth signal into location-sensitive and shape-stable components, a structural distinction absent from both binary detection methods and model collapse analyses"——即分析框架的价值而非分类性能。
3. **然而，我对这个辩护也有保留**：7-feature 方案仍需 Pythia-410M 参考模型的前向传播来计算 5 个特征，所以 cost 优势并没有 Figure 3 暗示的那么大。而且 Table 22（Appendix Q, page 25）显示 surface-only features（TTR+hapax ratio, 无需参考模型）F1=0.688，仅比 full 7-feature 低 2 pp，进一步削弱了参考模型特征的边际价值。

**结论**：R1 的 N2 是本文最致命的弱点之一——如果标准检测器组合已经能达到相同性能，DDR 的分类贡献确实被高估了。论文需要将价值主张从 "better classifier" 转向 "analytical decomposition framework"。

---

## Should-Fix (Major)

### [AGREE] R1-W1: 实验范围过窄（English Wikipedia + continuation + nucleus sampling）

同意。我在自己的审稿中也标注了这个限制。补充一个 R1 发现的重要细节：**Qwen3-1.7B 在 cross-temperature 评估中 F1 从 0.948 降至 0.418**（Appendix P, page 24）。这说明 DDR 的稳定性是 generator-dependent 的，而非论文声称的 "generation-process invariant"。论文虽然在 Appendix P 讨论了这一异常并将其归因于 Qwen3-1.7B 的 temperature sensitivity，但这恰恰说明 DDR 对生成器配置的脆弱性比正文暗示的更大。

### [PARTIALLY REBUT] R1-W2: DDR 理论基础薄弱

R1 要求 "信息论或统计学正式推导" 有其道理，但这个要求可能对一篇 empirical analysis paper 过于严苛。

**反驳理由**：
1. 论文在 §5 Discussion 中给出了 mechanistic interpretation："under nucleus sampling, top-p truncation preserves the functional form of the conditional distribution at each step; what changes is the *input*: as the model conditions on increasingly self-typical outputs, expected NLL compresses monotonically."（page 8）这不是 formal proof，但提供了一个可测试的机制假说。
2. 很多高影响力的 empirical papers（如 Shumailov et al. 2024 在 Nature 上发表的 model collapse 论文）也主要依靠实验观察而非 formal 推导。要求 formal information-theoretic 推导本质上是在要求一篇不同性质的论文。
3. **但 R1 的方向是对的**：论文声称 DDR 是 "structural property" 却没有理论支撑，这使得 claim 的泛化性无法被评估。一个 sketch-level 的分析（如 bounding the entropy drift rate under nucleus sampling）会大幅增强论文的说服力。

**结论**：R1 的诊断正确（缺少理论基础），但处方过重（不应要求 formal 推导）。建议作者补充 sketch-level 理论分析而非完整证明。

### [AGREE] R1-W3: LOFO 跨家族泛化偏弱

验证了 R1 的数据：page 5 确认 LOFO（Leave-One-Family-Out）binary F1=0.634。从 LOGO 的 0.694 下降到 0.634，绝对值降幅 6 pp，相对降幅 ~8.6%。R1 将此解读为 "约 9% 信号来自 family-specific artifacts" 是合理的。

**补充分析**：
1. 论文自己承认部分下降源于 "same-family affinity with the Pythia-410M reference"（page 5），这意味着参考模型选择引入了系统性偏差——当 test family 与参考模型同族（如 Pythia 生成器 + Pythia-410M 参考）时性能较好。
2. R1 指出 gen-2+ 的 LOFO per-class F1 极低（0.268-0.453）。这意味着当整个模型家族被 held out 时，系统几乎无法识别多次生成的文本——这对 "depth fingerprinting" 的实用性是严重打击。
3. Appendix S（page 25, Table 24）的 cross-family reference model 实验确认 "drift direction is consistent (negative) across all three references; magnitude varies with capacity"，但 LOGO F1 仅 ±0.013，表明换参考模型帮助有限。

### [AGREE] R1-W4: Binary task 排除 gen-0 使 headline metric 不反映完整场景

同意。我在 N1 中从不同角度提出了类似问题。

**补充证据**：Table 9（page 16）的 confusion matrix 清楚显示 gen-0 分类接近完美（99.4% recall），这意味着 3-class LOGO F1=0.789 中 gen-0 的贡献极大地拉高了整体数字。真正的 "depth fingerprinting" 挑战（gen-1 vs gen-2+）的性能才是核心指标，而这个指标只有 0.694——论文选择将 gen-0 排除后的 binary F1 作为 headline metric 是合理的设计选择（避免 trivial human/machine signal inflating results），但 R1 的批评也有道理：实际部署中用户面对的是三类或更多类的完整场景，binary metric 确实不完整。

**不过，我对 R1 的措辞有一个小 caveat**：论文选择排除 gen-0 恰恰是为了避免 inflated metric——如果保留 gen-0，headline F1 会更高（~0.79）但更不诚实。排除 gen-0 是一个负责任的评估选择，尽管它确实隐藏了完整场景的复杂性。

### [AGREE] R1-W5: QLoRA 未在 LOGO 下评估

这是一个重要的方法论问题。Appendix E 使用 within-model 5-fold CV（page 19 confirms "within-model 5-fold CV on single-generator chains"），而主实验使用 LOGO。这意味着 QLoRA F1=0.905 和 7-feature LOGO F1=0.694 不可直接对比——前者可能因 generator-specific signal leakage 而偏高。

**补充**：这个问题也影响到我自己的 N2（手工特征 vs 端到端方案的定位失衡）。如果 QLoRA 在 LOGO 下评估也会下降（这是很可能的），那么两种方案的性能差距可能比 0.694 vs 0.905 小得多。这实际上可以 partially 缓解我提出的 N2 concern——但论文应该做这个实验来 settle the question，而不是让 reviewer 猜测。

---

## Minor

### [PARTIALLY REBUT] R1-M1: TOST d=0.20 阈值未充分 justify

论文引用了 Cohen (1988) 的 "conventional small effect size" d=0.20 和 Lakens (2017) 的等价性检验框架。d=0.20 是行为科学中最广泛使用的 "small effect" 标准，几乎所有使用 TOST 的论文都以此为默认阈值。R1 要求额外 justification 的标准偏高。

**但 R1 有一点道理**：在 NLP 任务中，d=0.20 的实际意义可能与行为科学不同。论文可以补充一句说明 d=0.20 在本任务中对应的实际特征变化幅度（如 entropy mean 的绝对变化量），增强可解释性。

### [AGREE] R1-M2: Table 1/2 ms/text 标注不一致

Table 3 中 7-feature 方案的 ms/text 标注为 "N/A"，但该方案仍需 Pythia-410M 的前向传播，应有非零 inference cost。这与 Figure 3 的 cost comparison 存在矛盾。

### [AGREE] R1-M3: Figure 1 和 Figure 2 颜色编码不一致

Figure 1 用深浅蓝色区分 drifting/non-drifting；Figure 2 用不同色系。统一颜色编码会提升可读性。

### [AGREE] R1-M4: 部分 arXiv preprint 标注问题

引用验证显示部分条目的 year 在 bib 文件和 API 记录间存在小差异（如 `self_consuming_mad` 2024 vs OpenAlex 2023, `strong_model_collapse` 2025 vs 2024）。虽然这些可能是 camera-ready 版本 vs arXiv 版本的正常差异，但应确保引用最终发表版本。

### [AGREE] R1-M5: Appendix Z.4 Gemma 异常

R1 指出 Gemma-2 可能因 tokenizer 差异（SentencePiece vs BPE）导致参考模型 NLL 特征的异常行为。论文确实在 page 32 提到 "Gemma-2's distinct attention mechanism and SentencePiece tokenizer with a larger vocabulary may produce first-generation continuations whose feature-space signature closely resembles human text"，但未正式排除 tokenizer confound。这是一个合理的 concern——至少应在正文的 Limitations 中提及 tokenizer 依赖性。

---

## 缺失引用

### Guo et al. (2023) "How Close is ChatGPT to Human Experts?"
[PARTIALLY REBUT] 该论文关注 ChatGPT vs human 的质量对比，与 depth fingerprinting 的关联较弱。如果要引用，应放在 §2.1 作为 "broader context of AI text analysis" 而非核心相关工作。nice-to-have 但非 must-have。

### Briesch et al. (2023) "Large Language Models Suffer From Their Own Output"
[AGREE] 这篇直接研究 LLM iterative generation 的退化现象，与论文主题高度相关，应在 §2.2 Model Collapse 部分引用。

### Diaz & Karampatziakis (2019) "Soft Labels for Ordinal Regression"
[AGREE] 论文在 §2.2 讨论了 ordinal regression methods（引用了 Gutiérrez et al. 2016, CORAL, CORN），补充这篇关于 soft labels 的工作是合理的，尤其是论文的 depth task 本身具有 ordinal 性质。

---

## R1 优势评价的交叉确认

R1 列出的 5 项优势（新颖任务定义、LOGO+LOFO 评估协议、附录深度、统计严谨性、可解释性）我全部同意。特别是：

1. **评估协议**（R1 Strength 2）：LOGO 排除 generator leakage + length-matched subsampling + bootstrap CI 的组合确实是我近期审稿中见过的最严谨的实验设计之一。
2. **统计学素养**（R1 Strength 4）：TOST 等价性检验、Granger causality、Cohen's d + Cliff's δ 双重效应量——很少有 NLP 论文达到这个统计学标准。

---

## 综合评判

**R1 给出 Overall 3.5 (Borderline Conference)，我给出 3.0 (Findings)。** 差异主要在 Excitement 维度：R1 给 3/5，我给 2.5/5。

**我们的共识**：
- 任务定义是新颖的
- 实证工作极其扎实
- 但实际影响力受限于 base-model 范围和 modest performance
- DDR 的分类贡献被 oversold（R1-N2 + 我的 N2 从不同角度确认了这一点）

**分歧**：我对 headline result 的实用价值更悲观——F1=0.694（≈0.705 考虑 Table 3 的 LOGO 数字）且不优于检测器组合，结合 instruction-tuned 退化和 depth resolution ceiling（只能区分 gen-1 vs gen-2+），使得论文的 practical contribution 更适合 Findings。R1 给 3.5 可能考虑了 DDR 作为分析框架的潜在影响力，这个判断有其合理性。

**建议最终评分区间**：3.0–3.5，取决于 AC 对 "empirical analysis paper with limited novelty but exceptional thoroughness" 的接收标准。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 2838 · 2026-05-21T04:40:30.394672+00:00_

called mcp__agent-ml-research__get_visual_check_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_visual_check_status</summary>

```json
{
  "project": "gen-depth-fingerprint"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "tool_args": {
    "project": "gen-depth-fingerprint"
  }
}
```

</details>

---


### Tool result

_source line 2839 · 2026-05-21T04:40:30.545792+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"done\", \"started_at\": \"2026-05-21T04:25:01.610666+00:00\", \"completed_at\": \"2026-05-21T04:29:13.471301+00:00\", \"findings\": [{\"severity\": \"critical\", \"dimension\": \"pages 1-4\", \"message\": \"前4页连续纯文本，无任何 display item（figure/table/equation）。首个 display item（Table 1）直到第5页才出现。对于实证为主的论文，审稿人在前2分钟内看不到任何视觉锚点，第一印象极差。建议将核心概念图或 Figure 1 的简化版提前到第1-2页\"}, {\"severity\": \"warning\", \"dimension\": \"page 33\", \"message\": \"最后一页 Table 41 仅占页面上部约 1/3，下方约 60% 为空白。末页内容严重不足，空间浪费明显\"}, {\"severity\": \"warning\", \"dimension\": \"pages 5-7 vs 1-4\", \"message\": \"Display item 分布严重不均：pages 1-4 零个 display item，page 5 有 Table 1，page 6 有 Figure 1，page 7 密集堆叠 Figure 2 + Table 2 + Figure 3 共3个。布局节奏失衡——前半部分空旷，后半部分拥挤\"}, {\"severity\": \"warning\", \"dimension\": \"page 7\", \"message\": \"Figure 2（DDR 分布图）和 Figure 3（F1 vs 推理成本散点图）尺寸偏小，子面板中的 y 轴特征名称和数据标注在打印后可能难以辨认。Figure 3 位于右栏底部，面积极小\"}, {\"severity\": \"warning\", \"dimension\": \"page 13\", \"message\": \"Figure 4（violin plots，7 个面板）占据整页但页面底部 caption 下方仍有约 15% 空白。附录可视化图应嵌入文字中而非独占整页（违反用户写作规则：附录中的可视化图要嵌入在文字中）\"}, {\"severity\": \"warning\", \"dimension\": \"page 23\", \"message\": \"Figure 8（7 个 per-feature depth trends 面板）+ Figure 9（2 个 UMAP 面板）堆叠在同一页。Figure 8 各面板极小，个别生成器的彩色线条难以区分。建议拆分到两页并增大面板尺寸\"}, {\"severity\": \"info\", \"dimension\": \"page 1\", \"message\": \"Title / Author / Abstract 排版整洁，双栏格式符合 ACL 模板规范，无溢出或拥挤\"}, {\"severity\": \"info\", \"dimension\": \"page 5\", \"message\": \"Table 1 使用 booktabs 风格，最优结果已加粗，格式专业。Caption 自包含\"}, {\"severity\": \"info\", \"dimension\": \"page 6\", \"message\": \"Figure 1 四面板 strip plot 颜色可区分，整体可读，但单个面板字号接近可读下限（约为正文 70%）\"}, {\"severity\": \"info\", \"dimension\": \"page 7\", \"message\": \"Table 2 格式规范，使用 booktabs，最优结果加粗，列对齐良好\"}, {\"severity\": \"info\", \"dimension\": \"pages 9-11\", \"message\": \"参考文献页排版正常，未见 [?] 未解析引用，格式统一\"}, {\"severity\": \"info\", \"dimension\": \"page 8\", \"message\": \"Conclusion + Limitations + 
…[truncated 603 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 2840 · 2026-05-21T04:40:30.546117+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "gen-depth-fingerprint"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "gen-depth-fingerprint"
  }
}
```

</details>

---


### Tool result

_source line 2841 · 2026-05-21T04:40:34.160992+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 3614
}
```

</details>

---


### Tool call

_source line 2842 · 2026-05-21T04:40:34.311840+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-3-projects-gen-depth-fingerprint--claude-sessions-review-director-fec00603/1d09cdd5-00ac-4676-8013-cd78df9c94fc/tool-results/bbem3um0m.txt"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-3-projects-gen-depth-fingerprint--claude-sessions-review-director-fec00603/1d09cdd5-00ac-4676-8013-cd78df9c94fc/tool-results/bbem3um0m.txt"
  }
}
```

</details>

---


### Tool result

_source line 2843 · 2026-05-21T04:40:34.664220+00:00_

1	# === Round 29-34 历史 Issues（保留完整记录）===
2	
3	- id: "R29-N1"
4	  summary: "Base-model-only scope 未在 Abstract 标注"
5	  category: framing
6	  severity: critical
7	  status: resolved
8	  first_raised_round: 29
9	  last_seen_round: 32
10	  mentions:
11	    - {round: 29, reviewers: "R1+R2", note: "共识: Abstract 必须标注 base-model scope"}
12	    - {round: 31, reviewers: "R1+R2", note: "W1: Title/Abstract 仍需 base-model qualifier"}
13	    - {round: 32, reviewers: "R1+R2", note: "升级: 实验设计仅覆盖 base model, 建议扩展或限定 scope"}
14	  action_items:
15	    - {round: 29, action: "Abstract 加 base (pretrained) qualifier", assigned_to: Agent, status: done}
16	    - {round: 32, action: "Abstract/Conclusion 已有 qualifier; instruct in Discussion", assigned_to: Director, status: done}
17	  resolution: "Abstract L3 'eight base-model generators'; L7 'restricted to base models'. Title 保持不变(Reviewer 确认). Instruct limitations fully documented."
18	  resolution_round: 32
19	
20	- id: "R29-N2"
21	  summary: "Downstream TOST underpowered (n=3) + Abstract overclaim"
22	  category: experiment
23	  severity: critical
24	  status: resolved
25	  first_raised_round: 29
26	  last_seen_round: 34
27	  mentions:
28	    - {round: 29, reviewers: "R1+R2", note: "n=3 seeds, Abstract 省略 preliminary"}
29	    - {round: 31, reviewers: "R1+R2", note: "W3: TOST n=3 underpowered"}
30	    - {round: 32, reviewers: "R1+R2", note: "升级为 null result: depth-aware curation 不优于 random"}
31	    - {round: 34, reviewers: "R1+R2", note: "RESOLVED: Abstract 完全移除 downstream claim; Appendix M 坦诚呈现 null result"}
32	  action_items:
33	    - {round: 29, action: "Abstract 加 preliminary qualifier", assigned_to: Agent, status: done}
34	    - {round: 32, action: "Abstract/Conclusion downstream reframing", assigned_to: Director, status: done}
35	  resolution: "Abstract 完全移除 downstream claim. Appendix M 保留 null result 作为补充材料."
36	  resolution_round: 34
37	
38	- id: "R29-N3"
39	  summary: "DDR 新颖性 incremental — 缺 concurrent work 系统对比表"
40	  category: fra
…[truncated 29044 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_999770e4e57bfc6eabd12fc1f64af1ef:director",
  "tool": "Read",
  "elapsed_ms": 352
}
```

</details>

---
