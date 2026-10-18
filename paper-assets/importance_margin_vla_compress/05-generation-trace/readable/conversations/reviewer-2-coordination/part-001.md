# Reviewer 2 coordination — Part 1 of 2

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Conversation logs

[Transcript overview](../reviewer-2-coordination.md) · [Part 2 →](part-002.md) · [Structured JSON](../../../sessions/65/651e71cd0460b6874c29.json)

## Round 1

## Round 1

68 recorded events


### User

_source line 1 · 2026-05-18T11:30:47.086223+00:00_

[Round 1 审稿请求]:
## Round 1 审稿任务 — Reviewer 2

**你的审查侧重：新颖性 + 完整性 + 格式合规**

### Venue 信息
- **目标会议**: CoRL 2026
- **截止日期**: 2026-05-29
- **页数限制**: 正文 8 页（致谢/参考文献/附录不计入）
- **模板**: CoRL 2026 官方 LaTeX 模板
- **匿名规则**: Double-blind
- **必须包含 Limitations section**（计入 8 页）

### 论文信息
- **论文路径**: `projects/importance_margin_vla_compress/docs/paper/main.tex`
- **标题**: "Why Token Pruning Crashes Some Robot Policies but Not Others: The Role of Vision Connectors in VLA Token Compressibility"
- **核心 claim**: VLA 视觉 token 的可压缩性取决于 vision connector 设计；pixel-shuffle cliff-edge; cross-attention re-encoding 解决方案。

### 你的审查重点

1. **新颖性评估**：
   - "first systematic closed-loop evaluation" 的 claim 是否成立？是否有遗漏的 prior work？
   - Vision connector 决定 compressibility 这个 insight 是否足够 non-obvious？pixel-shuffle 将 16 patch 折叠成 1 token 后不可删除——这是否在预期之内？
   - Smart Compress（cross-attention pooling）是否有足够的方法贡献？Q-Former/Perceiver Resampler 已有类似设计。
   - Attention entropy ratio 作为诊断指标是否有足够的新颖性？

2. **Related Work 完整性**：
   - 引用列表 24 条，对 CoRL 是否足够？
   - 是否遗漏了重要的相关工作？特别注意：
     - CogACT（在 Related Work 中被提及但未在 bib 中）
     - Octo（在 literature_map 中但未被引用）
     - Open X-Embodiment（在 literature_map 中但未被引用）
     - 其他 VLA compression 工作
   - Related Work 的 positioning 是否清晰——本文相对已有工作的真实增量在哪里？

3. **叙事逻辑与主线统一性**：
   - Abstract → Introduction → Method → Results → Analysis → Discussion → Conclusion 是否形成一条连贯主线？
   - Introduction 的故事线是否有说服力？是否从一个足够重要的问题切入？
   - 论文的 framing 是 "negative result"（pruning fails）还是 "positive result"（Smart Compress works）？两条线是否平衡？

4. **格式合规性**：
   - `\documentclass[conference]{corl_2026}` 是否正确？CoRL 2026 是否使用 `[conference]` 选项？
   - Double-blind：论文是否完全匿名（检查作者、机构、代码链接、致谢）？
   - 是否有 Limitations section（CoRL 要求）？
   - 图表：正文引用 5 张图，figures/ 目录为空——这是编译问题还是图片缺失？
   - 引用格式：`plainnat` 是否符合 CoRL 要求？
   - 无行号——review 版是否需要行号？

5. **写作质量**：
   - 检查 AI 写作痕迹：em-dash（—）、en-dash（–）、-ing 结尾短语、过度分段
   - 专有名词首次出现是否有定义？
   - Abstract 是否满足 150-250 words 且回答了四个核心问题？

请按 CoRL 审稿标准给出完整审稿意见，包含：Strengths、Weaknesses（逐条编号，标注 severity: Must-Fix / Should-Fix / Minor）、Questions、Missing References、Overall Assessment。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 2 · 2026-05-18T11:30:56.574077+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 3 · 2026-05-18T11:30:57.277076+00:00_

1	\documentclass[conference]{corl_2026}
2	
3	\usepackage{amsmath,amssymb}
4	\usepackage{graphicx}
5	\usepackage{booktabs}
6	\usepackage{enumitem}
7	\usepackage{hyperref}
8	\usepackage{xcolor}
9	
10	\title{Why Token Pruning Crashes Some Robot Policies but Not Others:\\The Role of Vision Connectors in VLA Token Compressibility}
11	
12	\author{Anonymous}
13	
14	\begin{document}
15	\maketitle
16	
17	\input{abstract}
18	
19	\input{introduction}
20	
21	\input{related_work}
22	
23	\input{background}
24	
25	\input{experimental_setup}
26	
27	\input{results}
28	
29	\input{analysis}
30	
31	\input{discussion}
32	
33	\input{conclusion}
34	
35	\bibliographystyle{plainnat}
36	\bibliography{references}
37	
38	\input{appendix}
39	
40	\end{document}
41	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 703
}
```

</details>

---


### Tool call

_source line 4 · 2026-05-18T11:30:57.378406+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebSearch,WebFetch,mcp__agent-ml-research__review_reviewer_post_to_director,mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__verify_references",
  "max_results": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebSearch,WebFetch,mcp__agent-ml-research__review_reviewer_post_to_director,mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__verify_references",
    "max_results": "5"
  }
}
```

</details>

---


### Tool result

_source line 5 · 2026-05-18T11:30:57.429104+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 6 · 2026-05-18T11:31:01.894003+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "*.tex",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Glob",
  "tool_args": {
    "pattern": "*.tex",
    "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper"
  }
}
```

</details>

---


### Tool result

_source line 7 · 2026-05-18T11:31:02.799296+00:00_

/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/sections/experiments.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/experiments_deprecated.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/sections/analysis.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/sections/background.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/sections/experimental_setup.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/sections/introduction.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/sections/results_draft.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/experimental_setup.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/background.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/main.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/sections/related_work_draft.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/related_work.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/results.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/abstract.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/introduction.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/conclusion.tex
/home/ubuntu/.agent-ml-research-
…[truncated 444 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Glob",
  "elapsed_ms": 905
}
```

</details>

---


### Tool call

_source line 8 · 2026-05-18T11:31:02.799835+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "CoRL 2026 reviewer guidelines review form criteria"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "CoRL 2026 reviewer guidelines review form criteria"
  }
}
```

</details>

---


### Tool call

_source line 9 · 2026-05-18T11:31:03.201452+00:00_

called mcp__agent-ml-research__verify_references

<details open><summary>🔧 Tool call — mcp__agent-ml-research__verify_references</summary>

```json
{
  "paper_dir": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper",
  "project": "importance_margin_vla_compress"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "mcp__agent-ml-research__verify_references",
  "tool_args": {
    "paper_dir": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper",
    "project": "importance_margin_vla_compress"
  }
}
```

</details>

---


### Tool result

_source line 10 · 2026-05-18T11:31:08.552533+00:00_

Web search results for query: "CoRL 2026 reviewer guidelines review form criteria"

Links: [{"title":"CoRL 2026 - Instruction for Authors","url":"https://www.corl.org/contributions/instruction-for-authors"},{"title":"ICLR 2026 Reviewer Guide","url":"https://iclr.cc/Conferences/2026/ReviewerGuide"},{"title":"CoRL 2026 Conference | OpenReview","url":"https://openreview.net/group?id=robot-learning.org%2FCoRL%2F2026%2FConference"},{"title":"CoRL 2026 - Call for Papers","url":"https://www.corl.org/contributions/call-for-papers"},{"title":"CoRL 2026","url":"https://www.corl.org/"},{"title":"CVPR 2026 Reviewer Guidelines","url":"https://cvpr.thecvf.com/Conferences/2026/ReviewerGuidelinesq"},{"title":"CoRL 2024 - Instruction for Reviews","url":"https://2024.corl.org/contributions/instruction-for-reviews"},{"title":"Robot Learning Foundation","url":"https://www.robot-learning.org/"},{"title":"Reviewer Guidelines — CoRL 2023","url":"https://www.corl2023.org/reviewer-guidelines"},{"title":"2026 Reviewer Guidelines","url":"https://neurips.cc/Conferences/2026/ReviewerGuidelines"}]

Based on the search results, I found information about CoRL 2026, but the specific detailed reviewer guidelines and review form criteria for CoRL 2026 don't appear to be fully published yet in the search results. However, I can share what I found:

## Available CoRL 2026 Information

CoRL aims to have at least two reviewers per paper. Additionally, all submissions must include at least one author who agrees to serve as a CoRL reviewer, and they are qualified if they have at least one accepted publication at a previous robotics (CoRL/ICRA/IROS/RSS) or learning conference (ICLR/NeurIPS/ICML) or equivalent journal.

## Historical CoRL Review Criteria

While the specific CoRL 2026 review form criteria are not yet available in detail, I can reference CoRL 2024's review criteria, which likely provides guidance similar to what will be used in 2026. Submissions are evaluated based on the significance and nove
…[truncated 422 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 5752
}
```

</details>

---


### Tool result

_source line 11 · 2026-05-18T11:31:24.745733+00:00_

{"result":"{\"success\": true, \"data\": {\"summary\": {\"total_bib_entries\": 24, \"total_citations\": 52, \"unique_cited_keys\": 24, \"orphan_bib\": 0, \"missing_bib\": 0, \"duplicate_keys\": 0, \"online_verified\": 16, \"online_not_found\": 1, \"online_mismatch\": 7}, \"cross_check\": {\"orphan_bib\": [], \"missing_bib\": [], \"orphan_count\": 0, \"missing_count\": 0}, \"bib_entries\": [{\"key\": \"shukor2025smolvla\", \"type\": \"article\", \"title\": \"SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics\", \"authors\": \"Shukor, Mustafa and Aubakirova, Dana and Casas, Adrien and others\", \"year\": \"2025\", \"venue\": \"arXiv preprint arXiv:2506.01844\"}, {\"key\": \"kim2024openvla\", \"type\": \"inproceedings\", \"title\": \"OpenVLA: An Open-Source Vision-Language-Action Model\", \"authors\": \"Kim, Moo Jin and Pertsch, Karl and Karamcheti, Siddharth and others\", \"year\": \"2024\", \"venue\": \"Proceedings of the 8th Conference on Robot Learning (CoRL)\"}, {\"key\": \"zitkovich2023rt2\", \"type\": \"inproceedings\", \"title\": \"RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control\", \"authors\": \"Zitkovich, Brianna and Yu, Tianhe and Xu, Sichun and others\", \"year\": \"2023\", \"venue\": \"Proceedings of the 7th Conference on Robot Learning (CoRL)\"}, {\"key\": \"black2024pi0\", \"type\": \"article\", \"title\": \"$\\\\pi_0$: A Vision-Language-Action Flow Model for General Robot Control\", \"authors\": \"Black, Kevin and Brown, Noah and Driess, Danny and others\", \"year\": \"2024\", \"venue\": \"arXiv preprint arXiv:2410.24164\"}, {\"key\": \"chen2024fastv\", \"type\": \"inproceedings\", \"title\": \"An Image is Worth 1/2 Tokens After Layer 2: Plug-and-Play Inference Acceleration for Large Vision-Language Models\", \"authors\": \"Chen, Liang and others\", \"year\": \"2024\", \"venue\": \"European Conference on Computer Vision (ECCV)\"}, {\"key\": \"hsu2025vlacache\", \"type\": \"inproceedings\", \"title
…[truncated 19534 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "mcp__agent-ml-research__verify_references",
  "elapsed_ms": 21544
}
```

</details>

---


### Tool call

_source line 12 · 2026-05-18T11:31:31.137447+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 13 · 2026-05-18T11:31:31.690064+00:00_

1	\begin{abstract}
2	Vision token pruning reliably accelerates Vision Transformer (ViT) inference with negligible accuracy loss, prompting recent proposals to apply the same technique to Vision-Language-Action (VLA) models for faster robotic control. We conduct the first systematic closed-loop evaluation of vision token reduction across two VLA architectures and find that compressibility depends on the vision connector design. SmolVLA, which uses a pixel-shuffle connector that spatially folds 1024 patches into 64 tokens per camera, exhibits a cliff-edge failure: all six tested pruning configurations (varying scoring, retention ratio, and mechanism) collapse from 44.8\% to 0\% success rate on LIBERO. Even removing just 10\% of tokens causes complete task failure. OpenVLA, which uses an MLP projector that maps patches independently, degrades gracefully from 74.0\% to 37.4\% under 50\% random removal. The divergence traces to token information density: pixel-shuffle produces maximally entangled tokens with near-uniform attention (entropy ratio 0.98), while OpenVLA's deeper layers concentrate attention selectively (entropy ratio 0.64). For architectures where hard pruning fails, we show that a learned cross-attention module overcomes the cliff-edge: re-encoding SmolVLA's 128 tokens through cross-attention raises SR from 44.8\% to 59.8\% even without compression ($M{=}128$), and reducing to 32 queries (75\% token reduction) preserves this gain at 61.6\%, making token reduction a cost-free deployment benefit. These results establish that VLA token compressibility is architecture-dependent and that cross-attention re-encoding can overcome failures that all deletion-based methods share.
3	\end{abstract}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 552
}
```

</details>

---


### Tool call

_source line 14 · 2026-05-18T11:31:31.690516+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 15 · 2026-05-18T11:31:32.197531+00:00_

1	% introduction.tex -- Section 1: Introduction
2	
3	\section{Introduction}
4	\label{sec:introduction}
5	
6	Vision token pruning is one of the most reliable efficiency techniques in Vision Transformer (ViT) inference.
7	DynamicViT~\cite{rao2021dynamicvit} removes 66\% of patch tokens with less than 0.5\% accuracy loss on ImageNet classification.
8	Token Merging (ToMe)~\cite{bolya2023tome} merges 40\% of tokens while retaining over 99\% of classification accuracy.
9	EViT~\cite{liang2022evit} discards 50\% of inattentive tokens with negligible degradation.
10	These consistent results across architectures and benchmarks have established a strong prior: vision tokens are highly redundant, and aggressive reduction is safe.
11	A natural question follows.
12	Vision-Language-Action (VLA) models~\cite{zitkovich2023rt2,kim2024openvla,black2024pi0,shukor2025smolvla} use the same ViT encoders as their visual front-ends, producing hundreds of patch tokens that dominate the input sequence to the language model backbone.
13	For real-time robotic control, where inference latency directly constrains action frequency, reducing these vision tokens would yield immediate speedups in the most expensive component of the forward pass.
14	Does ViT token reduction transfer to VLA closed-loop control?
15	
16	This question has practical urgency.
17	Current VLA models such as RT-2~\cite{zitkovich2023rt2} and $\pi_0$~\cite{black2024pi0} use large vision encoders that produce 256 or more tokens per image.
18	When multiple camera views are used, the vision token count grows proportionally.
19	In a typical deployment scenario, a VLA must produce actions at 5--10 Hz to maintain smooth control, and the LLM backbone's self-attention over vision tokens is the dominant latency bottleneck because attention cost scales quadratically with sequence length.
20	SmolVLA~\cite{shukor2025smolvla}, a compact 451.5M-parameter VLA, produces 256 vision tokens from two cameras (128 per view), and these tokens constit
…[truncated 6571 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 507
}
```

</details>

---


### Tool call

_source line 16 · 2026-05-18T11:31:32.298482+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 17 · 2026-05-18T11:31:32.701508+00:00_

1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{Vision token efficiency.}
5	Token pruning in Vision Transformers is well established.
6	DynamicViT~\cite{rao2021dynamicvit} learns a binary mask to remove tokens progressively across layers, EViT~\cite{liang2022evit} fuses inattentive tokens guided by CLS attention, and ToMe~\cite{bolya2023tome} merges tokens via bipartite matching without any training.
7	These methods consistently remove 30\%--60\% of tokens with less than 1\% accuracy loss on ImageNet classification.
8	For Vision-Language Models, FastV~\cite{chen2024fastv} prunes visual tokens after early LLM layers based on attention patterns, and LLaVA-PruMerge~\cite{shang2024prumerge} combines CLS-attention pruning with similarity-based merging to reduce tokens by 4$\times$ on VQA benchmarks.
9	Our work tests whether these results transfer to closed-loop VLA control, where action errors compound across timesteps.
10	
11	\paragraph{VLA-specific token reduction.}
12	Three concurrent works address token efficiency in VLA models.
13	VLA-Cache~\cite{hsu2025vlacache} caches vision token KV states across timesteps, exploiting temporal redundancy in sequential observations to achieve 1.7$\times$ speedup without removing tokens.
14	VLA-IAP~\cite{wang2026vlaiap} proposes interaction-aligned pruning with geometric scheduling, reporting 97.8\% SR on OpenVLA with 1.54$\times$ speedup.
15	EfficientVLA~\cite{yang2025efficientvla} combines layer pruning, task-aware token selection, and temporal caching for 1.93$\times$ speedup on CogACT.
16	VLA-Pruner~\cite{liu2025vlapruner} uses dual-level importance criteria combining semantic and action-level attention for temporal-aware pruning.
17	A critical distinction is that VLA-IAP and EfficientVLA evaluate on models with MLP projectors (OpenVLA, CogACT), which we show exhibit graded degradation under pruning.
18	None of these works evaluates token reduction on pixel-shuffle VLAs, and none reports the cliff-edge failu
…[truncated 1517 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 403
}
```

</details>

---


### Tool call

_source line 18 · 2026-05-18T11:31:32.752162+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/background.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/background.tex"
  }
}
```

</details>

---


### Tool result

_source line 19 · 2026-05-18T11:31:33.154357+00:00_

1	% background.tex -- Section 2: Background
2	
3	\section{Background}
4	\label{sec:background}
5	
6	This section describes the architectures and benchmark used in our study: SmolVLA~\cite{shukor2025smolvla} and OpenVLA~\cite{kim2024openvla}, two VLA models with contrasting vision connector designs, and the LIBERO benchmark~\cite{liu2023libero} on which we evaluate closed-loop performance.
7	
8	\subsection{SmolVLA Architecture}
9	\label{sec:smolvla_arch}
10	
11	Vision-Language-Action (VLA) models cast robotic control as conditional generation: given a camera observation and a language instruction, the model predicts a continuous action.
12	SmolVLA~\cite{shukor2025smolvla} instantiates this paradigm with approximately 451.5M parameters, organized into a vision encoder, a vision connector, a language model backbone, and an action head.
13	Figure~\ref{fig:architecture} contrasts the vision pipelines of SmolVLA and OpenVLA, highlighting the connector designs that determine compressibility.
14	
15	\begin{figure}[t]
16	\centering
17	\includegraphics[width=\linewidth]{figures/paper/fig_architecture.pdf}
18	\caption{Vision connector comparison. \textbf{Left}: SmolVLA applies $4{\times}4$ pixel-shuffle to fold 1024 SigLIP patches into 64 tokens per camera (128 total), creating dense, spatially entangled representations. \textbf{Right}: OpenVLA uses an MLP projector that maps each patch independently, producing 256 tokens with per-token independence. This architectural difference determines token compressibility: pixel-shuffle tokens resist any form of deletion, while independently projected tokens allow graded pruning.}
19	\label{fig:architecture}
20	\end{figure}
21	
22	\paragraph{Vision encoder.}
23	SmolVLA uses the Sigmoid Loss for Language-Image Pre-training (SigLIP) encoder~\cite{zhai2023siglip} to process visual input.
24	SigLIP divides each camera image into non-overlapping spatial patches on a $32 \times 32$ grid, producing 1024 patch tokens per image.
25	SigLIP does n
…[truncated 6183 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 402
}
```

</details>

---


### Tool call

_source line 20 · 2026-05-18T11:31:33.154719+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/experimental_setup.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/experimental_setup.tex"
  }
}
```

</details>

---


### Tool result

_source line 21 · 2026-05-18T11:31:33.607389+00:00_

1	% experimental_setup.tex -- Section 3: Experimental Setup
2	
3	\section{Experimental Setup}
4	\label{sec:experimental_setup}
5	
6	We design three sets of experiments to evaluate vision token compressibility in VLA closed-loop control: (1) a controlled ablation on SmolVLA that tests whether any pruning configuration preserves performance, (2) a cross-architecture comparison on OpenVLA under the same pruning operation, and (3) a learned compression experiment on SmolVLA using cross-attention pooling. This section describes each experimental setup and the shared evaluation protocol.
7	
8	\subsection{SmolVLA Pruning Ablation}
9	\label{sec:smolvla_ablation_setup}
10	
11	\paragraph{ACIS importance scorer.}
12	To select which vision tokens to prune, we train an Attention-weighted Cumulative Importance Score (ACIS) module that predicts a scalar importance score for each of SmolVLA's 128 vision tokens (Section~\ref{sec:smolvla_arch}). The ACIS scorer is a lightweight MLP with 3.46M parameters, constituting 0.77\% of SmolVLA's 451.5M total.
13	
14	Training follows a Stage-1-only protocol: the ACIS scorer parameters are optimized while all VLA expert weights (vision encoder, pixel-shuffle connector, LLM backbone, and action head) remain frozen. This separation ensures that the scorer must identify genuinely important tokens under the original model's representation, and that any subsequent failure cannot be attributed to training-induced degradation. The scorer is trained with an importance margin loss that encourages a clear separation between the scores of retained and pruned tokens. At inference, tokens are sorted by ACIS score and the top-$k$ fraction is kept.
15	
16	\paragraph{Ablation design.}
17	The ablation study varies three axes, each designed to rule out a specific failure hypothesis.
18	\emph{Axis 1: Scoring function.} We compare the learned ACIS scorer against uniform random token selection. If both produce the same outcome, the failure is not caused by the scor
…[truncated 3420 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 22 · 2026-05-18T11:31:33.607970+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/results.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/results.tex"
  }
}
```

</details>

---


### Tool result

_source line 23 · 2026-05-18T11:31:34.612440+00:00_

1	\section{Results}
2	\label{sec:results}
3	
4	We evaluate token pruning across two VLA architectures on the LIBERO-Object benchmark~\cite{liu2023libero}, comprising 10 tasks with 50 episodes each (500 total). All success rates are reported with Wilson score 95\% confidence intervals.
5	
6	\subsection{SmolVLA: Cliff-Edge Under All Pruning Methods}
7	\label{sec:smolvla_results}
8	
9	SmolVLA~\cite{shukor2025smolvla} uses a pixel-shuffle vision connector that spatially rearranges patch embeddings before projecting them into the language model's embedding space. This operation creates inter-token spatial dependencies: each output token encodes information from a local grid of input patches. We hypothesize that this coupling makes the token sequence fragile under any form of pruning, since removing or masking a single token disrupts the spatial structure that downstream layers expect.
10	
11	\paragraph{Setup.}
12	We use a SmolVLA checkpoint fine-tuned on LIBERO-Object with the ACIS (Adaptive Contextual Importance Scoring) module attached but pruning disabled during training. The baseline (bypass mode) achieves 44.8\% SR (224/500, CI [40.5\%, 49.2\%]).\footnote{The official SmolVLA result on LIBERO is 87.3\% SR, trained with batch size 64 on 8 GPUs. Our reproduction uses a smaller batch size due to compute constraints, yielding a lower baseline. The relevant comparison is the relative change under pruning, not the absolute SR.} We then activate pruning under six configurations that vary three axes: scoring function (learned ACIS vs.\ random), retention ratio $k \in \{0.5, 0.7, 0.9\}$, and pruning mechanism (zero-masking, true token removal, token merging via ToMe~\cite{bolya2023tome}).
13	
14	\paragraph{All configurations collapse to 0\% SR.}
15	Table~\ref{tab:smolvla_ablation} reports the full ablation. Every pruning configuration produces 0\% success rate (Wilson CI upper bounds $\leq$1.26\%; see Table~\ref{tab:smolvla_ablation} for per-condition episode counts). Three 
…[truncated 13776 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1004
}
```

</details>

---


### Tool call

_source line 24 · 2026-05-18T11:31:34.864296+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/analysis.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/analysis.tex"
  }
}
```

</details>

---


### Tool result

_source line 25 · 2026-05-18T11:31:35.065625+00:00_

1	\section{Analysis}
2	\label{sec:analysis}
3	
4	The preceding experiments reveal a sharp divergence: pruning any fraction of SmolVLA's vision tokens causes complete task failure, while OpenVLA degrades gracefully under the same operations, and learned compression on SmolVLA even exceeds the uncompressed baseline. This section traces these outcomes to three architectural factors: the connector design that determines token granularity (\S\ref{sec:pixel_shuffle}), the attention distribution that reflects downstream reliance on individual tokens (\S\ref{sec:attention_distribution}), and the mechanism by which learned compression sidesteps the failure mode of hard pruning (\S\ref{sec:learned_compression}).
5	
6	\subsection{The Pixel-Shuffle Bottleneck}
7	\label{sec:pixel_shuffle}
8	
9	SmolVLA's vision encoder (SigLIP) produces 1024 patches per camera image on a $32 \times 32$ grid. Before these patches reach the language backbone, a pixel-shuffle connector applies $4 \times 4$ spatial folding, mapping every $4 \times 4$ block of patches into a single token by channel concatenation (Figure~\ref{fig:pixel_shuffle}). Each camera's 1024 patches are thereby compressed into 64 tokens, and the dual-camera setup yields 128 vision tokens in total.
10	
11	\begin{figure}[t]
12	\centering
13	\includegraphics[width=0.9\linewidth]{figures/paper/fig_pixel_shuffle.pdf}
14	\caption{Pixel-shuffle spatial folding. A $32{\times}32$ grid of SigLIP patches is folded with a $4{\times}4$ block size: each $4{\times}4$ group of spatially adjacent patches (colored blocks, left) is concatenated along the channel dimension into a single token (right), producing 64 tokens per camera. Each token encodes 16 contiguous patches with no overlap. Removing any token eliminates an entire $4{\times}4$ receptive field (gray region, right), with no redundancy from neighboring tokens to compensate. This irreversible information loss explains the cliff-edge: even removing one token destroys spatial coverage that
…[truncated 9536 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 26 · 2026-05-18T11:31:35.066127+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 27 · 2026-05-18T11:31:35.518319+00:00_

1	\section{Discussion}
2	\label{sec:discussion}
3	
4	\subsection{Disentangling Connector Design from Model Scale}
5	\label{sec:scale_confound}
6	
7	Our cross-architecture comparison confounds the vision connector design (pixel-shuffle vs.\ MLP projector) with model scale (0.5B vs.\ 7B parameters). A larger model has more capacity to absorb perturbations through its deeper and wider attention layers, raising the question of whether SmolVLA's cliff-edge reflects architectural fragility or simply insufficient model capacity.
8	
9	Three lines of evidence favor the connector-level explanation. First, SmolVLA collapses at $k = 0.9$, where only 13 of 128 tokens (10\%) are removed. A capacity-limited model that can solve the task with all tokens should not fail catastrophically when 90\% of the input is preserved; the perturbation is too small relative to the model's demonstrated capability. Second, the attention entropy ratio difference (0.98 vs.\ 0.64) is an architectural measurement, not a capacity measurement. SmolVLA's near-uniform attention distribution reflects the pixel-shuffle connector's output structure: because each token encodes 16 patches via channel concatenation, the resulting tokens are uniformly information-dense, and the downstream LLM has no basis for developing selective attention. OpenVLA's sharply non-uniform attention in deep layers reflects the MLP projector's preservation of per-patch granularity, which allows the model to learn which spatial locations carry task-relevant information. Third, the pixel-shuffle operation itself provides a mechanistic explanation: $4 \times 4$ spatial folding creates tokens whose meaning depends on the complete $4 \times 4$ grid, and removing any token eliminates an entire receptive field with no redundancy in the remaining tokens. The MLP projector, by contrast, produces tokens with overlapping receptive fields (inherited from the ViT encoder's patch-level self-attention), providing natural redundancy.
10	
11	The $k{
…[truncated 8734 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 28 · 2026-05-18T11:31:35.518783+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 29 · 2026-05-18T11:31:36.072543+00:00_

1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	We presented the first systematic closed-loop evaluation of vision token reduction across VLA architectures. Our experiments reveal that token compressibility is determined by the vision connector design: pixel-shuffle connectors create spatially entangled tokens that collapse under any form of deletion (44.8\% $\to$ 0\% across all six configurations), while MLP projectors preserve per-token independence and degrade gracefully (74.0\% $\to$ 37.4\%). The attention entropy ratio (0.98 vs.\ 0.64) captures this divergence and serves as a lightweight compressibility predictor. For architectures where deletion fails, learned cross-attention re-encoding raises SR from 44.8\% to $\sim$60\% regardless of output token count, and compressing to 32 queries (75\% token reduction) preserves this gain at 61.6\%, demonstrating that re-encoding can succeed where pruning cannot and that compression is a cost-free deployment benefit.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 553
}
```

</details>

---


### Tool call

_source line 30 · 2026-05-18T11:31:36.072999+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 31 · 2026-05-18T11:31:37.032639+00:00_

1	\appendix
2	
3	\section{Per-Task Breakdown Tables}
4	\label{app:per_task}
5	
6	\subsection{SmolVLA Baseline Per-Task Results}
7	
8	Table~\ref{tab:smolvla_baseline_pertask} reports per-task success rates for the SmolVLA baseline (bypass mode, no pruning) on LIBERO-Object. All pruning conditions (Table~\ref{tab:smolvla_ablation}) produce 0\% success rate on every task; we omit per-task breakdowns for pruning conditions as they carry no additional information beyond the aggregate 0\% already reported.
9	
10	\begin{table}[h]
11	\centering
12	\small
13	\caption{SmolVLA baseline (bypass mode) per-task success rates on LIBERO-Object (50 episodes per task, 500 total). Overall SR: 44.8\%.}
14	\label{tab:smolvla_baseline_pertask}
15	\begin{tabular}{lc}
16	\toprule
17	Task & SR (\%) \\
18	\midrule
19	alphabet\_soup & 22 \\
20	bbq\_sauce & 60 \\
21	butter & 42 \\
22	chocolate\_pudding & 38 \\
23	cream\_cheese & 58 \\
24	ketchup & 26 \\
25	milk & 62 \\
26	orange\_juice & 38 \\
27	salad\_dressing & 50 \\
28	tomato\_sauce & 52 \\
29	\midrule
30	\textbf{Overall} & \textbf{44.8} \\
31	\bottomrule
32	\end{tabular}
33	\end{table}
34	
35	\subsection{OpenVLA Per-Task Results Under Pruning}
36	
37	\begin{table}[h]
38	\centering
39	\small
40	\caption{OpenVLA per-task success rates on LIBERO-Object under random token removal at $k=0.5$ (50 episodes per task). Baseline overall SR: 74.0\%. Tasks with visually distinctive targets (orange\_juice, alphabet\_soup) retain higher success rates, while tasks requiring fine-grained discrimination (butter, cream\_cheese) suffer the largest drops.}
41	\label{tab:openvla_pertask}
42	\begin{tabular}{lc}
43	\toprule
44	Task & SR (\%) at $k{=}0.5$ \\
45	\midrule
46	alphabet\_soup & 60 \\
47	bbq\_sauce & 44 \\
48	butter & 2 \\
49	chocolate\_pudding & 40 \\
50	cream\_cheese & 8 \\
51	ketchup & 50 \\
52	milk & 24 \\
53	orange\_juice & 72 \\
54	salad\_dressing & 36 \\
55	tomato\_sauce & 38 \\
56	\midrule
57	\textbf{Overall} & \textbf{37.4} \\
58	\bottomrule

…[truncated 5671 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 959
}
```

</details>

---


### Tool call

_source line 32 · 2026-05-18T11:31:38.459042+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://2024.corl.org/contributions/instruction-for-reviews",
  "prompt": "Extract the complete CoRL review form criteria, scoring dimensions, rating scales, and specific reviewer instructions. Include all evaluation dimensions like soundness, novelty, significance, clarity, etc. with their rating scales."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://2024.corl.org/contributions/instruction-for-reviews",
    "prompt": "Extract the complete CoRL review form criteria, scoring dimensions, rating scales, and specific reviewer instructions. Include all evaluation dimensions like soundness, novelty, significance, clarity, etc. with their rating scales."
  }
}
```

</details>

---


### Tool call

_source line 33 · 2026-05-18T11:31:40.468783+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://www.corl.org/contributions/instruction-for-authors",
  "prompt": "Extract all formatting requirements for CoRL 2026 papers: page limits, template requirements, anonymity rules, required sections (limitations, broader impact, etc.), line numbering for review, citation style, and any other submission format requirements."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://www.corl.org/contributions/instruction-for-authors",
    "prompt": "Extract all formatting requirements for CoRL 2026 papers: page limits, template requirements, anonymity rules, required sections (limitations, broader impact, etc.), line numbering for review, citation style, and any other submission format requirements."
  }
}
```

</details>

---


### Tool result

_source line 34 · 2026-05-18T11:31:42.127312+00:00_

# CoRL 2024 Review Criteria Summary

Based on the provided content, the document outlines **review criteria but does not include a complete scoring form** with rating scales or specific numerical dimensions.

## Available Evaluation Guidance

**Review Criteria (stated for regular papers):**
- Significance and novelty of results (theoretical or empirical)
- Degree to which results are "objectively established and/or their potential for scientific and technological impact"
- Relevance to robotic learning

**Scope Requirements:**
Papers must demonstrate robot learning relevance through either:
1. **Intent:** "Explicitly address a learning question for physical robots"
2. **Outcome:** "Test the proposed learning solution on physical robots"

## Notable Omissions

The document does **not provide**:
- Specific rating scales (e.g., 1-5, Likert scales)
- Detailed evaluation dimensions (soundness, clarity, significance as separate metrics)
- Numerical scoring instructions
- Rubric descriptions for different score levels
- Complete review form structure

The guidelines focus primarily on desk rejection criteria and reviewer qualification standards rather than the detailed scoring framework typically found in full review instructions.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 3668
}
```

</details>

---


### Tool result

_source line 35 · 2026-05-18T11:31:45.644445+00:00_

# CoRL 2026 Formatting Requirements

## Page Limits
- **Initial submission**: 8 pages maximum for main paper
- **Camera-ready version**: 9 pages maximum for main text
- Acknowledgments, references, and appendix do not count toward page limits

## Template & Technical Requirements
- Authors must use the provided LaTeX template
- Camera-ready template requires `\usepackage[final]{corl_2026}`
- Text density, fonts, spacing, and margins must match the provided template
- Footer on first page: "10th Conference on Robot Learning (CoRL 2026), Austin, Texas, USA."

## Anonymity
- Papers must be double-blind anonymized for submission
- Author names are removed during review
- Camera-ready versions must include non-anonymous author list

## Required Sections
A **Limitations section** is mandatory, counted within the 8-page limit. This section must explicitly address "limiting assumptions, failure modes, and other limitations of the results and experiments."

## Supplementary Materials
- Appendix may be included with main paper or in supplement
- Reviewers are not obligated to read appendices
- Video submissions encouraged (maximum 250 MB, under 3 minutes suggested)
- Supplementary materials submitted as single zip file via OpenReview
- PMLR does not accept videos as supplementary material; host externally instead

## Citation & Reproducibility
Papers with nonexistent citations face desk rejection. Authors should include sufficient methodological details for reproducibility.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 5175
}
```

</details>

---


### Tool call

_source line 36 · 2026-05-18T11:31:54.687872+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "CoRL 2025 2024 OpenReview review form scoring dimensions soundness excitement novelty rating scale"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "CoRL 2025 2024 OpenReview review form scoring dimensions soundness excitement novelty rating scale"
  }
}
```

</details>

---


### Tool call

_source line 37 · 2026-05-18T11:31:55.190096+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "CogACT VLA vision language action model 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "CogACT VLA vision language action model 2024 2025"
  }
}
```

</details>

---


### Tool call

_source line 38 · 2026-05-18T11:31:56.444908+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Octo robot foundation model generalist policy 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Octo robot foundation model generalist policy 2024"
  }
}
```

</details>

---


### Tool call

_source line 39 · 2026-05-18T11:31:58.103107+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/references.bib"
  }
}
```

</details>

---


### Tool result

_source line 40 · 2026-05-18T11:31:58.103767+00:00_

1	% References for: The Cliff Edge — Why Vision Token Reduction Fails
2	% Catastrophically in VLA Closed-Loop Control
3	% Auto-generated from literature_map.yaml (verified entries only)
4	% 2026-05-17
5	
6	% ============================================================
7	% VLA Models
8	% ============================================================
9	
10	@article{shukor2025smolvla,
11	  title={{SmolVLA}: A Vision-Language-Action Model for Affordable and Efficient Robotics},
12	  author={Shukor, Mustafa and Aubakirova, Dana and Casas, Adrien and others},
13	  journal={arXiv preprint arXiv:2506.01844},
14	  year={2025}
15	}
16	
17	@inproceedings{kim2024openvla,
18	  title={{OpenVLA}: An Open-Source Vision-Language-Action Model},
19	  author={Kim, Moo Jin and Pertsch, Karl and Karamcheti, Siddharth and others},
20	  booktitle={Proceedings of the 8th Conference on Robot Learning (CoRL)},
21	  year={2024}
22	}
23	
24	@inproceedings{zitkovich2023rt2,
25	  title={{RT-2}: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control},
26	  author={Zitkovich, Brianna and Yu, Tianhe and Xu, Sichun and others},
27	  booktitle={Proceedings of the 7th Conference on Robot Learning (CoRL)},
28	  year={2023}
29	}
30	
31	
32	@article{black2024pi0,
33	  title={$\pi_0$: A Vision-Language-Action Flow Model for General Robot Control},
34	  author={Black, Kevin and Brown, Noah and Driess, Danny and others},
35	  journal={arXiv preprint arXiv:2410.24164},
36	  year={2024}
37	}
38	
39	
40	% ============================================================
41	% VLM/LLM Token Efficiency
42	% ============================================================
43	
44	@inproceedings{chen2024fastv,
45	  title={An Image is Worth 1/2 Tokens After Layer 2: Plug-and-Play Inference Acceleration for Large Vision-Language Models},
46	  author={Chen, Liang and others},
47	  booktitle={European Conference on Computer Vision (ECCV)},
48	  year={2024},
49	  note={Oral presentation}
50	}
51	
52	
53	@inproceedin
…[truncated 6863 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 41 · 2026-05-18T11:31:58.406724+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "figures/**/*",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Glob",
  "tool_args": {
    "pattern": "figures/**/*",
    "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper"
  }
}
```

</details>

---


### Tool result

_source line 42 · 2026-05-18T11:31:58.457427+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 43 · 2026-05-18T11:32:04.337589+00:00_

Web search results for query: "Octo robot foundation model generalist policy 2024"

Links: [{"title":"Octo: An Open-Source Generalist Robot Policy","url":"https://octo-models.github.io/"},{"title":"[2405.12213] Octo: An Open-Source Generalist Robot Policy","url":"https://arxiv.org/abs/2405.12213"},{"title":"GitHub - octo-models/octo: Octo is a transformer-based robot policy trained on a diverse mix of 800k robot trajectories. · GitHub","url":"https://github.com/octo-models/octo"},{"title":"Octo: An Open-Source Generalist Robot Policy","url":"https://stevengong.co/research-papers/Octo-An-OpenSource-Generalist-Robot-Policy"},{"title":"An Open-Source Generalist Robot Policy","url":"https://octo-models.github.io/paper.pdf"},{"title":"dblp: Octo: An Open-Source Generalist Robot Policy.","url":"https://dblp.org/rec/journals/corr/abs-2405-12213.html"},{"title":"Octo: An Open-Sourced Large Transformer-based Generalist Robot Policy Trained on 800k Trajectories from the Open X-Embodiment Dataset - MarkTechPost","url":"https://www.marktechpost.com/2024/05/24/octo-an-open-sourced-large-transformer-based-generalist-robot-policy-trained-on-800k-trajectories-from-the-open-x-embodiment-dataset/"},{"title":"Octo: An Open-Source Generalist Robot Policy Octo Model Team Dibya Ghosh∗,1","url":"https://arxiv.org/pdf/2405.12213"},{"title":"Octo: An Open-Source Generalist Robot Policy","url":"https://arxiv.org/html/2405.12213v2"},{"title":"Octo: An Open-Source Generalist Robot Policy | Request PDF","url":"https://www.researchgate.net/publication/383897130_Octo_An_Open-Source_Generalist_Robot_Policy"}]

Here's what I found about Octo, the robot foundation model:

## Overview

Octo is a large transformer-based policy trained on 800k trajectories from the Open X-Embodiment dataset, the largest robot manipulation dataset to date. Octo models are transformer-based diffusion policies, trained on a diverse mix of 800k robot trajectories.

## Key Capabilities

Out-of-the-box, Octo can control mult
…[truncated 1208 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 7892
}
```

</details>

---


### Tool result

_source line 44 · 2026-05-18T11:32:04.940362+00:00_

Web search results for query: "CogACT VLA vision language action model 2024 2025"

Links: [{"title":"CogACT: A Foundational Vision-Language-Action Model for Synergizing Cognition and Action in Robotic Manipulation","url":"https://cogact.github.io/"},{"title":"[2411.19650] CogACT: A Foundational Vision-Language-Action Model for Synergizing Cognition and Action in Robotic Manipulation","url":"https://arxiv.org/abs/2411.19650"},{"title":"CogACT: A Foundational Vision-Language-Action Model for Synergizing Cognition and Action in Robotic Manipulation","url":"https://arxiv.org/html/2411.19650v1"},{"title":"CoA-VLA: Improving Vision-Language-Action Models via ...","url":"https://openaccess.thecvf.com/content/ICCV2025/papers/Li_CoA-VLA_Improving_Vision-Language-Action_Models_via_Visual-Text_Chain-of-Affordance_ICCV_2025_paper.pdf"},{"title":"GitHub - microsoft/CogACT: A Foundational Vision-Language-Action Model for Synergizing Cognition and Action in Robotic Manipulation","url":"https://github.com/microsoft/CogACT"},{"title":"Deploying Vision Language Action (VLA) based AI Models in Robotics: Optimization for Real-Time Edge Inference - MulticoreWare","url":"https://multicorewareinc.com/deploying-vision-language-action-vla-based-ai-models-in-robotics-optimization-for-real-time-edge-inference/"},{"title":"CogAct Computational Model","url":"https://www.emergentmind.com/topics/cogact-computational-model"},{"title":"What are Vision Language Action (VLA) Models? Complete Guide","url":"https://www.articsledge.com/post/vision-language-action-vla-models"},{"title":"[Literature Review] CogACT: A Foundational Vision-Language-Action Model for Synergizing Cognition and Action in Robotic Manipulation","url":"https://www.themoonlight.io/en/review/cogact-a-foundational-vision-language-action-model-for-synergizing-cognition-and-action-in-robotic-manipulation"},{"title":"(PDF) CogACT: A Foundational Vision-Language-Action Model for Synergizing Cognition and Action in Robotic Manipulation","u
…[truncated 2144 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 9750
}
```

</details>

---


### Tool result

_source line 45 · 2026-05-18T11:32:09.375170+00:00_

Web search results for query: "CoRL 2025 2024 OpenReview review form scoring dimensions soundness excitement novelty rating scale"

Links: [{"title":"CORL 2025 Statistics - Paper Copilot","url":"https://papercopilot.com/statistics/corl-statistics/corl-2025-statistics/"},{"title":"CoRL | OpenReview","url":"https://openreview.net/group?id=robot-learning.org%2FCoRL"},{"title":"CoRL 2025 Accepted Paper List - Paper Copilot","url":"https://papercopilot.com/paper-list/corl-paper-list/corl-2025-paper-list/"},{"title":"CoRL 2024 | OpenReview","url":"https://openreview.net/group?id=robot-learning.org/CoRL/2024"},{"title":"CoRL 2025 Conference | OpenReview","url":"https://openreview.net/group?id=robot-learning.org%2FCoRL%2F2025%2FConference"},{"title":"CoRL 2025 | OpenReview","url":"https://openreview.net/group?id=robot-learning.org/CoRL/2025"},{"title":"CORL 2024 Statistics - Paper Copilot","url":"https://papercopilot.com/statistics/corl-statistics/corl-2024-statistics/"},{"title":"CoRL 2025 Demos | OpenReview","url":"https://openreview.net/group?id=robot-learning.org%2FCoRL%2F2025%2FDemos"},{"title":"Reviewer Guidelines — CoRL 2023","url":"https://www.corl2023.org/reviewer-guidelines"},{"title":"CoRL 2024 Conference | OpenReview","url":"https://openreview.net/group?id=robot-learning.org%2FCoRL%2F2024%2FConference"}]

Let me search for more specific information about the review form scoring dimensions:

Links: [{"title":"CoRL 2024 | OpenReview","url":"https://openreview.net/group?id=robot-learning.org/CoRL/2024"},{"title":"CORL 2024 Statistics - Paper Copilot","url":"https://papercopilot.com/statistics/corl-statistics/corl-2024-statistics/"},{"title":"CoRL 2024 Conference | OpenReview","url":"https://openreview.net/group?id=robot-learning.org%2FCoRL%2F2024%2FConference"},{"title":"CoRL | OpenReview","url":"https://openreview.net/group?id=robot-learning.org%2FCoRL"},{"title":"CoRL 2024 Workshop | OpenReview","url":"https://openreview.net/group?id=robot-learning.org%2FCoRL%2F2
…[truncated 6246 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 14687
}
```

</details>

---


### Tool call

_source line 46 · 2026-05-18T11:32:23.865846+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://www.corl2023.org/reviewer-guidelines",
  "prompt": "Extract ALL review form dimensions, scoring scales, rating criteria, and specific numerical scales used for CoRL review. Include everything: overall recommendation scale, confidence scale, soundness, novelty, significance, clarity, any other dimensions with their exact rating options."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://www.corl2023.org/reviewer-guidelines",
    "prompt": "Extract ALL review form dimensions, scoring scales, rating criteria, and specific numerical scales used for CoRL review. Include everything: overall recommendation scale, confidence scale, soundness, novelty, significance, clarity, any other dimensions with their exact rating options."
  }
}
```

</details>

---


### Tool call

_source line 47 · 2026-05-18T11:32:26.275095+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "—",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper",
  "output_mode": "content",
  "glob": "*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Grep",
  "tool_args": {
    "pattern": "—",
    "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper",
    "output_mode": "content",
    "glob": "*.tex"
  }
}
```

</details>

---


### Tool result

_source line 48 · 2026-05-18T11:32:26.777659+00:00_

/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/experiments_deprecated.tex:1:% experiments.tex — Section 4: Main Results

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Grep",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 49 · 2026-05-18T11:32:27.230396+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": " – ",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper",
  "output_mode": "content",
  "glob": "*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Grep",
  "tool_args": {
    "pattern": " – ",
    "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper",
    "output_mode": "content",
    "glob": "*.tex"
  }
}
```

</details>

---


### Tool result

_source line 50 · 2026-05-18T11:32:27.733552+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Grep",
  "elapsed_ms": 503
}
```

</details>

---


### Tool result

_source line 51 · 2026-05-18T11:32:28.638357+00:00_

# CoRL 2023 Review Form Dimensions

Based on the provided guidelines, the document specifies **six evaluation dimensions** for reviewers to assess:

1. **Originality** — novelty of problems/methods and differentiation from prior work
2. **Quality** — technical soundness and appropriate methodology
3. **Clarity** — writing quality and organization
4. **Significance** — importance and potential impact of results
5. **Relevance** — alignment with robot learning focus and CoRL audience interest
6. **Limitations** — appreciation for honestly reported constraints

## Notable Absence

The document does not explicitly list numerical scoring scales, overall recommendation categories, or confidence ratings. While it references "scores" in context, the specific numerical ranges, rating options (e.g., "1-5," "accept/reject"), or confidence scales are **not provided** in this content.

The guidelines emphasize evaluation criteria and dimensions rather than the mechanics of the scoring system itself, suggesting those details may be communicated separately through the OpenReview platform or in supplementary reviewer instructions referenced but not included here.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 4772
}
```

</details>

---


### Tool call

_source line 52 · 2026-05-18T11:32:28.638861+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "ing,|ing\\.",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper",
  "output_mode": "content",
  "glob": "*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Grep",
  "tool_args": {
    "pattern": "ing,|ing\\.",
    "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper",
    "output_mode": "content",
    "glob": "*.tex"
  }
}
```

</details>

---


### Tool result

_source line 53 · 2026-05-18T11:32:29.141469+00:00_

/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/abstract.tex:2:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/analysis.tex:9:SmolVLA's vision encoder (SigLIP) produces 1024 patches per camera image on a $32 \times 32$ grid. Before these patches reach the language backbone, a pixel-shuffle connector applies $4 \times 4$ spatial folding, mapping every $4 \times 4$ block of patches into a single token by channel concatenation (Figure~\ref{fig:pixel_shuffle}). Each camera's 1024 patches are thereby compressed into 64 tokens, and the dual-camera setup yields 128 vision tokens in total.
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/analysis.tex:14:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/analysis.tex:43:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/related_work.tex:6:DynamicViT~\cite{rao2021dynamicvit} learns a binary mask to remove tokens progressively across layers, EViT~\cite{liang2022evit} fuses inattentive tokens guided by CLS attention, and ToMe~\cite{bolya2023tome} merges tokens via bipartite matching without any training.
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/related_work.tex:14:VLA-IAP~\cite{wang2026vlaiap} proposes interaction-aligned pruning with geometric scheduling, reporting 97.8\% SR on OpenVLA with 1.54$\times$ speedup.
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/related_work.tex:15:EfficientVLA~\cite{yang2025efficientvla} combines layer pruning, task-aware token selection, and temporal caching for 1.93$\times$ speedup on CogACT.
/home/ubuntu/.agent-ml-research-be-idea-gen-0
…[truncated 13032 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Grep",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 54 · 2026-05-18T11:32:30.396874+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://papercopilot.com/statistics/corl-statistics/corl-2024-statistics/",
  "prompt": "Extract the CoRL 2024 review form dimensions and rating scales. What are the specific scoring dimensions (e.g., Soundness, Presentation, Contribution, Overall) and their rating scales (e.g., 1-10)?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://papercopilot.com/statistics/corl-statistics/corl-2024-statistics/",
    "prompt": "Extract the CoRL 2024 review form dimensions and rating scales. What are the specific scoring dimensions (e.g., Soundness, Presentation, Contribution, Overall) and their rating scales (e.g., 1-10)?"
  }
}
```

</details>

---


### Tool result

_source line 55 · 2026-05-18T11:32:34.315779+00:00_

# CoRL 2024 Review Dimensions and Rating Scales

Based on the provided webpage content, I cannot identify the specific review form dimensions or their rating scales for CoRL 2024.

The page displays aggregated statistics showing that CoRL 2024 had "min:1.70 max:4.00 avg:3.01" for overall ratings, indicating a **1.70-4.00 scale**. However, the document does not specify individual scoring dimensions such as Soundness, Presentation, or Contribution.

To find detailed information about CoRL 2024's review form structure and dimensions, you would need to:
- Visit the [OpenReview page directly](https://openreview.net/group?id=robot-learning.org/CoRL/2024)
- Check the conference's official website or review guidelines
- Consult the conference submission instructions

The Paper Copilot platform appears designed to aggregate and visualize review statistics rather than display the underlying review form specifications.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 3918
}
```

</details>

---


### Tool call

_source line 56 · 2026-05-18T11:33:31.910862+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "corl*",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Glob",
  "tool_args": {
    "pattern": "corl*",
    "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper"
  }
}
```

</details>

---


### Tool result

_source line 57 · 2026-05-18T11:33:32.363103+00:00_

/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/corl_2026.cls

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Glob",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 58 · 2026-05-18T11:33:33.467822+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "\\\\textendash",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper",
  "output_mode": "content",
  "glob": "*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Grep",
  "tool_args": {
    "pattern": "\\\\textendash",
    "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper",
    "output_mode": "content",
    "glob": "*.tex"
  }
}
```

</details>

---


### Tool result

_source line 59 · 2026-05-18T11:33:33.819639+00:00_

/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/analysis.tex:27:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/analysis.tex:32:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/discussion.tex:49:The Smart Compress module is trained and evaluated on a single benchmark (LIBERO-Object, 10 tasks). Its generalization to other manipulation benchmarks, longer-horizon tasks, and cross-embodiment transfer has not been tested. The re-encoding benefit and the range of compression ratios that preserve it ($M = 32$\textendash$128$) may be specific to the visual complexity and task diversity of LIBERO-Object; more demanding environments could require different configurations.
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/sections/analysis_draft.tex:20:[Omitted long matching line]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Grep",
  "elapsed_ms": 351
}
```

</details>

---


### Tool call

_source line 60 · 2026-05-18T11:33:34.372571+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "lineno|linenumber|\\\\setpagewiselinenumbers",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Grep",
  "tool_args": {
    "pattern": "lineno|linenumber|\\\\setpagewiselinenumbers",
    "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper",
    "output_mode": "content"
  }
}
```

</details>

---


### Tool result

_source line 61 · 2026-05-18T11:33:34.976430+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Grep",
  "elapsed_ms": 603
}
```

</details>

---


### Tool call

_source line 62 · 2026-05-18T11:33:35.027116+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "CoRL 2026 latex template documentclass options conference review line numbers"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "CoRL 2026 latex template documentclass options conference review line numbers"
  }
}
```

</details>

---


### Tool result

_source line 63 · 2026-05-18T11:33:40.221609+00:00_

Web search results for query: "CoRL 2026 latex template documentclass options conference review line numbers"

Links: [{"title":"CoRL LaTeX Template | Robot Learning Conference Format | Underleaf","url":"https://www.underleaf.ai/templates/corl"},{"title":"CoRL 2026 - Instruction for Authors","url":"https://www.corl.org/contributions/instruction-for-authors"},{"title":"COLM 2026 Template - Overleaf, Online LaTeX Editor","url":"https://www.overleaf.com/latex/templates/colm-2026-template/wbwzrwczsqvg"},{"title":"GitHub - korpling/CRC-template: LaTeX template for Collaborative Research Center proposals following the DFG guidelines. · GitHub","url":"https://github.com/korpling/CRC-template"},{"title":"LaTeX Templates [Lehigh ISE / COR@L Lab Wiki]","url":"https://coral.ise.lehigh.edu/wiki/doku.php/resources:latex"},{"title":"CoRL 2026","url":"https://www.corl.org/"},{"title":"CVPR 2026 Submission Template - Overleaf, Online LaTeX Editor","url":"https://www.overleaf.com/latex/templates/cvpr-2026-submission-template/rdtrwgypxxzb"},{"title":"GitHub - acl-org/acl-style-files: Official style files for papers submitted to venues of the Association for Computational Linguistics · GitHub","url":"https://github.com/acl-org/acl-style-files"},{"title":"Templates - Journals, CVs, Presentations, Reports and More - Overleaf, Online LaTeX Editor","url":"https://www.overleaf.com/latex/templates/tagged/conference-paper"},{"title":"IEEE LaTeX Template Guide: Step-by-Step (2026)","url":"https://thelatexlab.com/blog/ieee-latex-template-formatting/"}]

Based on the search results, I found information about the CoRL 2026 LaTeX template. Here's what I found:

For camera-ready submissions, authors should use `\usepackage[final]{corl_2026}`. 

The CoRL LaTeX template uses a custom style based on PMLR (Proceedings of Machine Learning Research) format.

The official LaTeX template is available via Google Drive, which contains the complete template with the appropriate documentclass options and conf
…[truncated 718 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 5194
}
```

</details>

---


### Tool call

_source line 64 · 2026-05-18T11:33:44.388673+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/corl_2026.cls",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/corl_2026.cls",
    "limit": "100"
  }
}
```

</details>

---


### Tool result

_source line 65 · 2026-05-18T11:33:44.489516+00:00_

1	\NeedsTeXFormat{LaTeX2e}
2	\ProvidesClass{corl_2026}[2026/01/01 CoRL 2026 paper style (minimal)]
3	\DeclareOption{conference}{\relax}
4	\DeclareOption*{\PassOptionsToClass{\CurrentOption}{article}}
5	\ProcessOptions\relax
6	\LoadClass[10pt,letterpaper,twocolumn]{article}
7	\RequirePackage[margin=1in]{geometry}
8	\RequirePackage{times}
9	\RequirePackage[numbers,sort&compress]{natbib}
10	\setlength{\parindent}{1em}
11	\setlength{\parskip}{0pt}
12	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 66 · 2026-05-18T11:36:23.207719+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "\n# Reviewer 2 — Round 1 审稿报告\n\n**论文**: \"Why Token Pruning Crashes Some Robot Policies but Not Others: The Role of Vision Connectors in VLA Token Compressibility\"\n**审查侧重**: 新颖性 + 完整性 + 格式合规\n\n---\n\n## 总体评分\n\n**Overall**: 3/5 (Borderline — 有价值的实证发现，但核心 claim 存在未解决的 confound，方法贡献有限)\n\n**一句话总结**: 论文提供了 VLA token pruning 在 closed-loop 下失败的有力实证证据，cliff-edge 发现本身有价值，但 connector vs. scale confound 未能解开，Smart Compress 的方法新颖性不足，且多个格式问题需修复。\n\n---\n\n## 官方维度打分（基于 CoRL review form: Originality, Quality, Clarity, Significance, Relevance, Limitations）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Originality | 3/5 | Cliff-edge 发现和 connector-compressibility 关联有新颖性；但 Smart Compress 本质是 Q-Former/Perceiver 的直接应用，entropy ratio 是标准 normalized entropy |\n| Quality (Soundness) | 2.5/5 | 实验设计严谨（3-axis ablation, Wilson CI），但 0.5B vs 7B scale confound 无法解开，Smart Compress 的 gain 可能来自额外 22.2M 参数+训练而非 re-encoding |\n| Clarity | 4/5 | 写作清晰流畅，主线逻辑连贯，AI 痕迹极少；但存在冗余重复（cliff-edge 现象在 Abstract/Intro/Results/Analysis/Discussion 中反复描述） |\n| Significance | 3/5 | 对 VLA 部署有实用价值的 negative result；但局限于 LIBERO 仿真，无 real robot 验证 |\n| Relevance | 4/5 | 直接面向 robot learning 社区，VLA 推理加速是当前热点 |\n| Limitations | 4/5 | Section 5.5 诚实地讨论了 LIBERO-only、scale confound、generalization 等限制 |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] Scale confound 严重削弱核心因果 claim\n\n- 具体位置：Section 5.1 (Discussion), Section 4.3 (Results §Architectural contrast)\n- 问题：论文核心 claim 是 \"vision connector design determines compressibility\"，但两个被比较的模型同时在 connector（pixel-shuffle vs MLP）和 scale（0.5B vs 7B）上不同。论文在 Section 5.1 承认 \"A definitive test would require evaluating a 7B-parameter VLA with a pixel-shuffle connector, or a 0.5B VLA with an MLP projector. Neither configuration exists.\"  论文用三条间接证据（k=0.9 失败、entropy ratio 差异、pixel-shuffle 机制分析）来论证 connector 是主因，但这些都是相关性证据，不是因果证据。k=0.9 的论证尤其薄弱：一个 0.5B 的弱模型（baseline 仅 44.8% vs 官方 87.3%）在输入被扰动 10% 时崩溃，也可能是因为 capacity 不足导致缺乏鲁棒性。\n- 为什么影响接收：论文标题和全部四条 contribution 都以 connector-level 因果解释为前提。如果 scale 是更重要的因素，论文的叙事基础将不成立。\n- 建议修改方向：(1) 弱化因果语言，使用 \"associated with\" 而非 \"determined by\"；(2) 寻找更多 pixel-shuffle VLA（如 InternVL-based VLA，论文已引用 InternVL）进行验证；(3) 在同一模型（OpenVLA）上对比 MLP projector 与人工添加的 pixel-shuffle 操作。\n\n**N2** [critical] Smart Compress 的 performance gain 存在严重 confound\n\n- 具体位置：Section 4.3, Table 3, Section 6.1\n- 问题：Smart Compress 在 M=128（无压缩）时 SR 从 44.8% 提升到 59.8%，论文将此归因于 \"cross-attention re-encoding\"。但这 15 个百分点的提升也可能来自：(a) 额外的 22.2M trainable parameters（增加了 5% 模型容量），(b) 额外的 100K 步 end-to-end 训练（compressor + LLM backbone jointly optimized），(c) 两者的组合。论文声称 \"the gain originates from cross-attention re-encoding, not from compression\"（Section 6.1），但没有控制实验来排除参数量和训练的贡献。\n- 关键缺失的 ablation：(a) 在 baseline 上继续训练 100K 步（不加 compressor），看 SR 是否也提升；(b) 用同样参数量的 MLP 替代 cross-attention 模块，看是否有同等提升；(c) 只训练 compressor 冻结 LLM（论文当前 jointly optimize compressor + LLM backbone）。\n- 为什么影响接收：如果 gain 来自额外训练/参数而非 re-encoding 机制，Contribution 3 的核心 claim 不成立。\n- 建议：至少增加 \"baseline + 100K more training\" 控制实验。\n\n**N3** [critical] CogACT 在正文中被提及但缺少 bib 条目\n\n- 具体位置：Related Work, lines 15 and 17 (\"1.93× speedup on CogACT\", \"EfficientVLA evaluate on models with MLP projectors (OpenVLA, CogACT)\")\n- 问题：CogACT 是一个重要的 VLA 模型（~7.6B 参数，Microsoft，arXiv 2411.19650），在 Related Work 中被两次提及但从未被 \\cite{}。论文使用 CogACT 作为论据来支持 \"MLP projector VLAs exhibit graded degradation\" 的 claim，但没有提供引用，审稿人无法核实这个 claim。\n- 另外，CogACT 使用 DINOv2+SigLIP dual encoder (类似 OpenVLA)，其 connector 类型是什么？如果 CogACT 也用 pixel-shuffle 但能被 EfficientVLA 成功 prune，将直接反驳论文的核心 thesis。\n- 建议：补充 CogACT 引用，明确说明其 connector 类型，核实 EfficientVLA 在 CogACT 上的 pruning 行为是否与论文假说一致。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] 缺少重要相关工作引用\n\n- 具体位置：Related Work (Section 2), references.bib\n- 问题：24 篇引用对 CoRL 偏少（CoRL 2024 录用论文通常 30-50 篇引用）。遗漏的重要工作：\n  - **Octo** (Ghosh et al., 2024, RSS): 开源 generalist robot policy，使用 transformer-based architecture，是 VLA 领域的重要 baseline，且使用 cross-attention 处理 vision tokens\n  - **Open X-Embodiment** (RT-X, 2024): 大规模跨具身数据集，是 VLA 训练的重要数据源，CogACT 等模型基于此训练\n  - **RT-1** (Brohan et al., 2023): VLA 的重要前驱工作，且 RT-2 已被引用\n  - **HPT** (Wang et al., 2024): heterogeneous pre-training，另一种 VLA 架构\n- 为什么影响评分：引用不完整会让审稿人质疑文献调研的深度，特别是 Octo 使用了类似 Perceiver 的 cross-attention tokenizer，与 Smart Compress 的思路直接相关。\n- 建议：补充以上引用并在 Related Work 中讨论。\n\n**W2** [warning] SmolVLA baseline 显著低于官方水平（44.8% vs 87.3%）\n\n- 具体位置：Section 4.1, footnote 1\n- 问题：论文 baseline（44.8% SR）仅为官方报告（87.3%）的 51%。论文将此归因于 \"smaller batch size due to compute constraints\"。但这意味着 cliff-edge 现象是在一个显著 undertrained 的 checkpoint 上观察到的。一个充分训练的 SmolVLA（87.3% SR baseline）在 pruning 下的行为是否相同？更高的 baseline 可能意味着更强的表示鲁棒性。\n- 此问题与 N1（scale confound）叠加：一个 undertrained、small-scale 的模型缺乏 pruning 鲁棒性，可能是因为 capacity/training 不足，而非 connector 设计。\n- 建议：(1) 如果算力允许，在官方 checkpoint（或更接近官方性能的 checkpoint）上验证 cliff-edge；(2) 至少讨论 baseline 差异对结论可能的影响。\n\n**W3** [warning] Smart Compress 方法新颖性有限\n\n- 具体位置：Section 3.3, Section 6.1\n- 问题：Cross-attention pooling 使用 M 个 learned query vectors 对所有 source tokens 做 cross-attention，这在架构上与 Q-Former (BLIP-2, Li et al. 2023) 和 Perceiver Resampler (Flamingo, Alayrac et al. 2022) 几乎相同。论文在 Related Work 中提到了这两个工作但未明确讨论 Smart Compress 与它们的区别。论文的方法贡献不是 cross-attention pooling 本身（这已被广泛使用），而是发现它能克服 pixel-shuffle VLA 的 cliff-edge。但作为 CoRL 论文的 Contribution 3，需要更清楚地定位 \"应用 Q-Former 到 pixel-shuffle VLA\" 与 \"原创方法贡献\" 的区别。\n- 建议：在方法部分明确对比 Smart Compress 与 Q-Former/Perceiver 的异同，说明 contribution 在于 empirical finding 而非 architectural novelty。\n\n**W4** [warning] M=96 异常值缺乏解释\n\n- 具体位置：Table 3, Section 4.3, Section 6.1\n- 问题：M=96（52.6% SR）低于 M=64（61.6%）和 M=128（59.8%），论文多次称其为 \"outlier\" 或 \"likely reflects training dynamics\"，但没有提供任何证据或分析。在仅有 5 个数据点的 M-performance curve 中，一个 outlier 已经占据 20%。\n- 如果 M=96 的结果是真实的（而非随机波动），则 Smart Compress 的 performance-vs-compression 曲线不是 monotone 的，这与 \"compression is cost-free\" 的 narrative 矛盾。\n- 建议：(1) 用不同 seed 重复 M=96 实验；(2) 如果确认是随机波动，报告 confidence interval 和 seed 信息；(3) 如果不是随机波动，需要修改 narrative。\n\n**W5** [warning] \"first systematic closed-loop evaluation\" claim 需要更精确限定\n\n- 具体位置：Abstract line 2, Introduction line 35, Conclusion line 1\n- 问题：VLA-IAP (Wang et al., 2026) 报告了 OpenVLA 上的 closed-loop SR（97.8% SR）。VLA-Cache 也评估了 closed-loop performance。因此 \"first closed-loop evaluation\" 这个 claim 需要更精确的限定词：the first to compare across connector types, or the first to test pixel-shuffle VLAs。当前表述过于宽泛，审稿人查到 VLA-IAP 的 closed-loop 结果后会认为 claim 不准确。\n- 建议：改为 \"the first cross-architecture closed-loop evaluation\" 或 \"the first to evaluate pixel-shuffle VLAs in closed-loop\"。\n\n**W6** [warning] 仅在 LIBERO 仿真环境评估，无 real robot\n\n- 具体位置：全文；Section 5.5 (Limitations)\n- 问题：CoRL 审稿标准明确偏好 real robot evaluation。所有实验在 LIBERO 仿真中进行。仿真中的 cliff-edge 是否在真实世界中也成立？Real robot 有 sensor noise、calibration drift、lighting variation，这些可能改变 token 的 information distribution。\n- Limitations section 已讨论此限制，但对于 CoRL 来说这仍是一个显著弱点。\n- 建议：如果可能，至少在 1-2 个 real robot task 上验证 cliff-edge 现象（即使是 qualitative 验证）。\n\n---\n\n## 格式合规问题\n\n**F1** [Must-Fix] 图片文件缺失\n\n- 具体位置：figures/ 目录\n- 问题：论文引用 5 张图（fig_architecture.pdf, fig_degradation_curve.pdf, fig_pixel_shuffle.pdf, fig_entropy_layers.pdf, fig_compression_curve.pdf），但 `figures/paper/` 目录为空（glob 返回 0 文件）。论文无法编译出包含图片的 PDF。\n- 建议：确保所有图片文件存在于正确路径。\n\n**F2** [Must-Fix] 无行号\n\n- 具体位置：main.tex, corl_2026.cls\n- 问题：CoRL review 版通常需要行号以便审稿人引用具体位置。当前 main.tex 和 corl_2026.cls 均无行号设置（无 `\\usepackage{lineno}` 或相关配置）。\n- 建议：添加 `\\usepackage{lineno}\\linenumbers`。\n\n**F3** [Should-Fix] corl_2026.cls 是极简 placeholder，非官方模板\n\n- 具体位置：corl_2026.cls（仅 12 行）\n- 问题：官方 CoRL 2026 模板应包含完整的 title/author formatting、abstract styling、section numbering、页眉页脚、anonymous mode 等。当前 cls 文件仅 `\\LoadClass[10pt,letterpaper,twocolumn]{article}` 加 geometry 和 natbib，`[conference]` option 是 `\\relax`（空操作）。投稿前必须替换为官方模板。\n- 为什么重要：使用非官方模板可能导致 desk reject（margin、字体、格式不符）。\n- 建议：从 CoRL 2026 官网下载官方模板。\n\n**F4** [Minor] `\\textendash` 使用\n\n- 具体位置：analysis.tex line 27 (\"0.95\\textendash 0.98\"), discussion.tex line 49 (\"$M = 32$\\textendash$128$\")\n- 问题：在 LaTeX 中，数字范围通常用 `--`（自动生成 en-dash），而非 `\\textendash`。`\\textendash` 在数学模式中可能产生不一致的排版。\n- 建议：统一使用 `--` 表示数字范围。\n\n**F5** [Minor] 引用中的 author mismatch\n\n- 具体位置：references.bib\n- 问题：`verify_references` 工具发现 7 条 author mismatch（zitkovich2023rt2 实际 first author 是 Brohan; hsu2025vlacache 实际 first author 是 Xu; wang2026vlaiap 实际 first author 是 Cheng; 等）。`black2024pi0` 在 OpenAlex 中 not_found（可能因为 arXiv title 中的 $\\pi_0$ 特殊字符导致匹配失败）。\n- 建议：逐一核查 bib 条目的 first author 和 year。\n\n---\n\n## 小问题（不影响接收）\n\n- Abstract 约 230 words，在 150-250 范围内，但数字密度偏高（9 个具体数字），读起来像 Results 摘要而非故事\n- Introduction Contribution 4 (\"Offline metric disconnect\") 的 claim 出现得较突然，前文铺垫不足\n- Related Work 最后一段 \"To our knowledge, no prior work...\" 是 novelty claim，按 CoRL 惯例应放在 Introduction\n- Discussion Section 5.4 (Design Implications) 部分论点与 Section 5.1 (Scale Confound) 有些矛盾：5.1 承认无法解开 confound，5.4 却给出了基于 connector 的 design recommendation\n- Appendix Table 7 标题说 \"per-task differences up to 48 percentage points\"，但检查数据最大差异是 chocolate_pudding M=32(90%) vs M=64(74%) = 16pp，orange_juice M=32(28%) vs M=128(58%) = 30pp；cream_cheese M=32(64%) vs M=64(38%) = 26pp。48pp 的说法需要核实（可能是在所有 M 值包括 M=16/M=96 的跨度上计算的，但 Table 7 只展示了 M=32/64/128）\n- \"ACIS\" 缩写在 Section 3.1 首次出现时虽然给了全称，但 \"Attention-weighted Cumulative Importance Score\" 的命名与实际描述（lightweight MLP scorer）之间的关联不够直观\n\n---\n\n## 主要优势\n\n1. **Cliff-edge 发现本身有价值**：6 种 pruning 配置在 SmolVLA 上全部 collapse 到 0% SR，且 k=0.9（仅移除 10%）也失败。这个 negative result 对 VLA 推理加速社区有重要警示意义。实验设计系统性强（3-axis ablation, 3 suites 交叉验证）。\n2. **统计严谨性**：所有结果报告 Wilson CI，样本量充足（500 episodes/condition），significance test 正确使用。\n3. **写作质量高**：主线逻辑清晰（problem → failure → explanation → solution），AI 写作痕迹极少（仅 1 处 em-dash 在 deprecated 文件中，无解释性 en-dash）。\n4. **诚实讨论限制**：Section 5.1 直接面对 scale confound，Section 5.5 承认 LIBERO-only 和 generalization 未知。这种诚实性值得肯定。\n5. **跨架构对比**：同时评估 SmolVLA 和 OpenVLA 提供了有价值的对照。\n\n---\n\n## 审稿人对 Director 的建议\n\n论文有一个有价值的核心发现（cliff-edge），但在三个关键 confound 上需要加强：(1) connector vs scale，(2) re-encoding gain vs additional training/params，(3) \"first\" claim 的精确性。如果作者能提供至少 1-2 个控制实验（特别是 N2 的 \"baseline + more training\" 控制），并修正引用问题（N3, W1），论文的竞争力会显著提升。\n\n格式问题（F1-F3）虽然不影响学术评价，但投稿前必须全部解决。\n",
  "reviewer_id": "2",
  "project": "importance_margin_vla_compress"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "\n# Reviewer 2 — Round 1 审稿报告\n\n**论文**: \"Why Token Pruning Crashes Some Robot Policies but Not Others: The Role of Vision Connectors in VLA Token Compressibility\"\n**审查侧重**: 新颖性 + 完整性 + 格式合规\n\n---\n\n## 总体评分\n\n**Overall**: 3/5 (Borderline — 有价值的实证发现，但核心 claim 存在未解决的 confound，方法贡献有限)\n\n**一句话总结**: 论文提供了 VLA token pruning 在 closed-loop 下失败的有力实证证据，cliff-edge 发现本身有价值，但 connector vs. scale confound 未能解开，Smart Compress 的方法新颖性不足，且多个格式问题需修复。\n\n---\n\n## 官方维度打分（基于 CoRL review form: Originality, Quality, Clarity, Significance, Relevance, Limitations）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Originality | 3/5 | Cliff-edge 发现和 connector-compressibility 关联有新颖性；但 Smart Compress 本质是 Q-Former/Perceiver 的直接应用，entropy ratio 是标准 normalized entropy |\n| Quality (Soundness) | 2.5/5 | 实验设计严谨（3-axis ablation, Wilson CI），但 0.5B vs 7B scale confound 无法解开，Smart Compress 的 gain 可能来自额外 22.2M 参数+训练而非 re-encoding |\n| Clarity | 4/5 | 写作清晰流畅，主线逻辑连贯，AI 痕迹极少；但存在冗余重复（cliff-edge 现象在 Abstract/Intro/Results/Analysis/Discussion 中反复描述） |\n| Significance | 3/5 | 对 VLA 部署有实用价值的 negative result；但局限于 LIBERO 仿真，无 real robot 验证 |\n| Relevance | 4/5 | 直接面向 robot learning 社区，VLA 推理加速是当前热点 |\n| Limitations | 4/5 | Section 5.5 诚实地讨论了 LIBERO-only、scale confound、generalization 等限制 |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] Scale confound 严重削弱核心因果 claim\n\n- 具体位置：Section 5.1 (Discussion), Section 4.3 (Results §Architectural contrast)\n- 问题：论文核心 claim 是 \"vision connector design determines compressibility\"，但两个被比较的模型同时在 connector（pixel-shuffle vs MLP）和 scale（0.5B vs 7B）上不同。论文在 Section 5.1 承认 \"A definitive test would require evaluating a 7B-parameter VLA with a pixel-shuffle connector, or a 0.5B VLA with an MLP projector. Neither configuration exists.\"  论文用三条间接证据（k=0.9 失败、entropy ratio 差异、pixel-shuffle 机制分析）来论证 connector 是主因，但这些都是相关性证据，不是因果证据。k=0.9 的论证尤其薄弱：一个 0.5B 的弱模型（baseline 仅 44.8% vs 官方 87.3%）在输入被扰动 10% 时崩溃，也可能是因为 capacity 不足导致缺乏鲁棒性。\n- 为什么影响接收：论文标题和全部四条 contribution 都以 connector-level 因果解释为前提。如果 scale 是更重要的因素，论文的叙事基础将不成立。\n- 建议修改方向：(1) 弱化因果语言，使用 \"associated with\" 而非 \"determined by\"；(2) 寻找更多 pixel-shuffle VLA（如 InternVL-based VLA，论文已引用 InternVL）进行验证；(3) 在同一模型（OpenVLA）上对比 MLP projector 与人工添加的 pixel-shuffle 操作。\n\n**N2** [critical] Smart Compress 的 performance gain 存在严重 confound\n\n- 具体位置：Section 4.3, Table 3, Section 6.1\n- 问题：Smart Compress 在 M=128（无压缩）时 SR 从 44.8% 提升到 59.8%，论文将此归因于 \"cross-attention re-encoding\"。但这 15 个百分点的提升也可能来自：(a) 额外的 22.2M trainable parameters（增加了 5% 模型容量），(b) 额外的 100K 步 end-to-end 训练（compressor + LLM backbone jointly optimized），(c) 两者的组合。论文声称 \"the gain originates from cross-attention re-encoding, not from compression\"（Section 6.1），但没有控制实验来排除参数量和训练的贡献。\n- 关键缺失的 ablation：(a) 在 baseline 上继续训练 100K 步（不加 compressor），看 SR 是否也提升；(b) 用同样参数量的 MLP 替代 cross-attention 模块，看是否有同等提升；(c) 只训练 compressor 冻结 LLM（论文当前 jointly optimize compressor + LLM backbone）。\n- 为什么影响接收：如果 gain 来自额外训练/参数而非 re-encoding 机制，Contribution 3 的核心 claim 不成立。\n- 建议：至少增加 \"baseline + 100K more training\" 控制实验。\n\n**N3** [critical] CogACT 在正文中被提及但缺少 bib 条目\n\n- 具体位置：Related Work, lines 15 and 17 (\"1.93× speedup on CogACT\", \"EfficientVLA evaluate on models with MLP projectors (OpenVLA, CogACT)\")\n- 问题：CogACT 是一个重要的 VLA 模型（~7.6B 参数，Microsoft，arXiv 2411.19650），在 Related Work 中被两次提及但从未被 \\cite{}。论文使用 CogACT 作为论据来支持 \"MLP projector VLAs exhibit graded degradation\" 的 claim，但没有提供引用，审稿人无法核实这个 claim。\n- 另外，CogACT 使用 DINOv2+SigLIP dual encoder (类似 OpenVLA)，其 connector 类型是什么？如果 CogACT 也用 pixel-shuffle 但能被 EfficientVLA 成功 prune，将直接反驳论文的核心 thesis。\n- 建议：补充 CogACT 引用，明确说明其 connector 类型，核实 EfficientVLA 在 CogACT 上的 pruning 行为是否与论文假说一致。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] 缺少重要相关工作引用\n\n- 具体位置：Related Work (Section 2), references.bib\n- 问题：24 篇引用对 CoRL 偏少（CoRL 2024 录用论文通常 30-50 篇引用）。遗漏的重要工作：\n  - **Octo** (Ghosh et al., 2024, RSS): 开源 generalist robot policy，使用 transformer-based architecture，是 VLA 领域的重要 baseline，且使用 cross-attention 处理 vision tokens\n  - **Open X-Embodiment** (RT-X, 2024): 大规模跨具身数据集，是 VLA 训练的重要数据源，CogACT 等模型基于此训练\n  - **RT-1** (Brohan et al., 2023): VLA 的重要前驱工作，且 RT-2 已被引用\n  - **HPT** (Wang et al., 2024): heterogeneous pre-training，另一种 VLA 架构\n- 为什么影响评分：引用不完整会让审稿人质疑文献调研的深度，特别是 Octo 使用了类似 Perceiver 的 cross-attention tokenizer，与 Smart Compress 的思路直接相关。\n- 建议：补充以上引用并在 Related Work 中讨论。\n\n**W2** [warning] SmolVLA baseline 显著低于官方水平（44.8% vs 87.3%）\n\n- 具体位置：Section 4.1, footnote 1\n- 问题：论文 baseline（44.8% SR）仅为官方报告（87.3%）的 51%。论文将此归因于 \"smaller batch size due to compute constraints\"。但这意味着 cliff-edge 现象是在一个显著 undertrained 的 checkpoint 上观察到的。一个充分训练的 SmolVLA（87.3% SR baseline）在 pruning 下的行为是否相同？更高的 baseline 可能意味着更强的表示鲁棒性。\n- 此问题与 N1（scale confound）叠加：一个 undertrained、small-scale 的模型缺乏 pruning 鲁棒性，可能是因为 capacity/training 不足，而非 connector 设计。\n- 建议：(1) 如果算力允许，在官方 checkpoint（或更接近官方性能的 checkpoint）上验证 cliff-edge；(2) 至少讨论 baseline 差异对结论可能的影响。\n\n**W3** [warning] Smart Compress 方法新颖性有限\n\n- 具体位置：Section 3.3, Section 6.1\n- 问题：Cross-attention pooling 使用 M 个 learned query vectors 对所有 source tokens 做 cross-attention，这在架构上与 Q-Former (BLIP-2, Li et al. 2023) 和 Perceiver Resampler (Flamingo, Alayrac et al. 2022) 几乎相同。论文在 Related Work 中提到了这两个工作但未明确讨论 Smart Compress 与它们的区别。论文的方法贡献不是 cross-attention pooling 本身（这已被广泛使用），而是发现它能克服 pixel-shuffle VLA 的 cliff-edge。但作为 CoRL 论文的 Contribution 3，需要更清楚地定位 \"应用 Q-Former 到 pixel-shuffle VLA\" 与 \"原创方法贡献\" 的区别。\n- 建议：在方法部分明确对比 Smart Compress 与 Q-Former/Perceiver 的异同，说明 contribution 在于 empirical finding 而非 architectural novelty。\n\n**W4** [warning] M=96 异常值缺乏解释\n\n- 具体位置：Table 3, Section 4.3, Section 6.1\n- 问题：M=96（52.6% SR）低于 M=64（61.6%）和 M=128（59.8%），论文多次称其为 \"outlier\" 或 \"likely reflects training dynamics\"，但没有提供任何证据或分析。在仅有 5 个数据点的 M-performance curve 中，一个 outlier 已经占据 20%。\n- 如果 M=96 的结果是真实的（而非随机波动），则 Smart Compress 的 performance-vs-compression 曲线不是 monotone 的，这与 \"compression is cost-free\" 的 narrative 矛盾。\n- 建议：(1) 用不同 seed 重复 M=96 实验；(2) 如果确认是随机波动，报告 confidence interval 和 seed 信息；(3) 如果不是随机波动，需要修改 narrative。\n\n**W5** [warning] \"first systematic closed-loop evaluation\" claim 需要更精确限定\n\n- 具体位置：Abstract line 2, Introduction line 35, Conclusion line 1\n- 问题：VLA-IAP (Wang et al., 2026) 报告了 OpenVLA 上的 closed-loop SR（97.8% SR）。VLA-Cache 也评估了 closed-loop performance。因此 \"first closed-loop evaluation\" 这个 claim 需要更精确的限定词：the first to compare across connector types, or the first to test pixel-shuffle VLAs。当前表述过于宽泛，审稿人查到 VLA-IAP 的 closed-loop 结果后会认为 claim 不准确。\n- 建议：改为 \"the first cross-architecture closed-loop evaluation\" 或 \"the first to evaluate pixel-shuffle VLAs in closed-loop\"。\n\n**W6** [warning] 仅在 LIBERO 仿真环境评估，无 real robot\n\n- 具体位置：全文；Section 5.5 (Limitations)\n- 问题：CoRL 审稿标准明确偏好 real robot evaluation。所有实验在 LIBERO 仿真中进行。仿真中的 cliff-edge 是否在真实世界中也成立？Real robot 有 sensor noise、calibration drift、lighting variation，这些可能改变 token 的 information distribution。\n- Limitations section 已讨论此限制，但对于 CoRL 来说这仍是一个显著弱点。\n- 建议：如果可能，至少在 1-2 个 real robot task 上验证 cliff-edge 现象（即使是 qualitative 验证）。\n\n---\n\n## 格式合规问题\n\n**F1** [Must-Fix] 图片文件缺失\n\n- 具体位置：figures/ 目录\n- 问题：论文引用 5 张图（fig_architecture.pdf, fig_degradation_curve.pdf, fig_pixel_shuffle.pdf, fig_entropy_layers.pdf, fig_compression_curve.pdf），但 `figures/paper/` 目录为空（glob 返回 0 文件）。论文无法编译出包含图片的 PDF。\n- 建议：确保所有图片文件存在于正确路径。\n\n**F2** [Must-Fix] 无行号\n\n- 具体位置：main.tex, corl_2026.cls\n- 问题：CoRL review 版通常需要行号以便审稿人引用具体位置。当前 main.tex 和 corl_2026.cls 均无行号设置（无 `\\usepackage{lineno}` 或相关配置）。\n- 建议：添加 `\\usepackage{lineno}\\linenumbers`。\n\n**F3** [Should-Fix] corl_2026.cls 是极简 placeholder，非官方模板\n\n- 具体位置：corl_2026.cls（仅 12 行）\n- 问题：官方 CoRL 2026 模板应包含完整的 title/author formatting、abstract styling、section numbering、页眉页脚、anonymous mode 等。当前 cls 文件仅 `\\LoadClass[10pt,letterpaper,twocolumn]{article}` 加 geometry 和 natbib，`[conference]` option 是 `\\relax`（空操作）。投稿前必须替换为官方模板。\n- 为什么重要：使用非官方模板可能导致 desk reject（margin、字体、格式不符）。\n- 建议：从 CoRL 2026 官网下载官方模板。\n\n**F4** [Minor] `\\textendash` 使用\n\n- 具体位置：analysis.tex line 27 (\"0.95\\textendash 0.98\"), discussion.tex line 49 (\"$M = 32$\\textendash$128$\")\n- 问题：在 LaTeX 中，数字范围通常用 `--`（自动生成 en-dash），而非 `\\textendash`。`\\textendash` 在数学模式中可能产生不一致的排版。\n- 建议：统一使用 `--` 表示数字范围。\n\n**F5** [Minor] 引用中的 author mismatch\n\n- 具体位置：references.bib\n- 问题：`verify_references` 工具发现 7 条 author mismatch（zitkovich2023rt2 实际 first author 是 Brohan; hsu2025vlacache 实际 first author 是 Xu; wang2026vlaiap 实际 first author 是 Cheng; 等）。`black2024pi0` 在 OpenAlex 中 not_found（可能因为 arXiv title 中的 $\\pi_0$ 特殊字符导致匹配失败）。\n- 建议：逐一核查 bib 条目的 first author 和 year。\n\n---\n\n## 小问题（不影响接收）\n\n- Abstract 约 230 words，在 150-250 范围内，但数字密度偏高（9 个具体数字），读起来像 Results 摘要而非故事\n- Introduction Contribution 4 (\"Offline metric disconnect\") 的 claim 出现得较突然，前文铺垫不足\n- Related Work 最后一段 \"To our knowledge, no prior work...\" 是 novelty claim，按 CoRL 惯例应放在 Introduction\n- Discussion Section 5.4 (Design Implications) 部分论点与 Section 5.1 (Scale Confound) 有些矛盾：5.1 承认无法解开 confound，5.4 却给出了基于 connector 的 design recommendation\n- Appendix Table 7 标题说 \"per-task differences up to 48 percentage points\"，但检查数据最大差异是 chocolate_pudding M=32(90%) vs M=64(74%) = 16pp，orange_juice M=32(28%) vs M=128(58%) = 30pp；cream_cheese M=32(64%) vs M=64(38%) = 26pp。48pp 的说法需要核实（可能是在所有 M 值包括 M=16/M=96 的跨度上计算的，但 Table 7 只展示了 M=32/64/128）\n- \"ACIS\" 缩写在 Section 3.1 首次出现时虽然给了全称，但 \"Attention-weighted Cumulative Importance Score\" 的命名与实际描述（lightweight MLP scorer）之间的关联不够直观\n\n---\n\n## 主要优势\n\n1. **Cliff-edge 发现本身有价值**：6 种 pruning 配置在 SmolVLA 上全部 collapse 到 0% SR，且 k=0.9（仅移除 10%）也失败。这个 negative result 对 VLA 推理加速社区有重要警示意义。实验设计系统性强（3-axis ablation, 3 suites 交叉验证）。\n2. **统计严谨性**：所有结果报告 Wilson CI，样本量充足（500 episodes/condition），significance test 正确使用。\n3. **写作质量高**：主线逻辑清晰（problem → failure → explanation → solution），AI 写作痕迹极少（仅 1 处 em-dash 在 deprecated 文件中，无解释性 en-dash）。\n4. **诚实讨论限制**：Section 5.1 直接面对 scale confound，Section 5.5 承认 LIBERO-only 和 generalization 未知。这种诚实性值得肯定。\n5. **跨架构对比**：同时评估 SmolVLA 和 OpenVLA 提供了有价值的对照。\n\n---\n\n## 审稿人对 Director 的建议\n\n论文有一个有价值的核心发现（cliff-edge），但在三个关键 confound 上需要加强：(1) connector vs scale，(2) re-encoding gain vs additional training/params，(3) \"first\" claim 的精确性。如果作者能提供至少 1-2 个控制实验（特别是 N2 的 \"baseline + more training\" 控制），并修正引用问题（N3, W1），论文的竞争力会显著提升。\n\n格式问题（F1-F3）虽然不影响学术评价，但投稿前必须全部解决。\n",
    "reviewer_id": "2",
    "project": "importance_margin_vla_compress"
  }
}
```

</details>

---


### Tool result

_source line 67 · 2026-05-18T11:36:28.785822+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 5578
}
```

</details>

---


### Assistant

_source line 68 · 2026-05-18T11:36:45.233406+00:00_

审稿报告已提交给 Review Director。

## 审稿摘要

**Overall: 3/5 (Borderline)**

### Must-Fix 问题（3 条）
1. **Scale confound**（N1）：0.5B vs 7B 模型对比无法区分 connector 与 capacity 的影响，论文用间接证据论证但不充分
2. **Smart Compress gain confound**（N2）：M=128 的 15pp 提升可能来自额外 22.2M 参数和 100K 步训练，缺少 "baseline + more training" 控制实验
3. **CogACT 引用缺失**（N3）：在 Related Work 中被提及两次但无 bib 条目，且 CogACT 的 connector 类型可能直接影响论文核心论点

### Should-Fix 问题（6 条）
- 缺少 Octo/Open X-Embodiment/RT-1 等重要引用（24 篇偏少）
- SmolVLA baseline 仅 44.8%（官方 87.3%），cliff-edge 在 undertrained checkpoint 上观察
- Smart Compress 架构贡献有限（= Q-Former/Perceiver）
- M=96 异常值无证据支持 "training dynamics" 解释
- "first closed-loop evaluation" claim 过于宽泛
- 仅 LIBERO 仿真，无 real robot

### 格式问题
- **figures/ 目录为空**，5 张图无法编译
- **无行号**（review 版需要）
- **corl_2026.cls 是 12 行 placeholder**，非官方模板
- 引用 bib 中 7 条 author mismatch

### 主要优势
- Cliff-edge 发现有实际价值（6 配置 × 3 suites 全部 0%）
- 统计严谨（Wilson CI, 500 episodes/condition）
- 写作清晰，AI 痕迹极少
- 诚实讨论限制

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2"
}
```

</details>

---


## Round 2

## Round 2

4 recorded events


### User

_source line 69 · 2026-05-18T11:38:28.063736+00:00_

[Round 1 审稿请求]:
## 交叉分享 — 请逐条回应 Reviewer 1 的审稿意见

以下是 Reviewer 1 的完整审稿意见。请逐条回应：
- **[AGREE]**：同意并简要说明理由
- **[REBUT]**：反驳并提供证据（引用具体 Section/Table/Figure）

重点关注你们在以下问题上是否有分歧：
1. Scale confound 的严重程度——你们都列为 Must-Fix，但论证角度不同
2. Smart Compress gain confound——R1 将其列为 Should-Fix (W1)，你将其列为 Must-Fix (N2)。谁的 severity 更准确？
3. Baseline 偏低——R1 列为 Must-Fix (N2)，你列为 Should-Fix (W2)。R1 认为这独立影响接收，你认为它与 N1 叠加但不独立一票否决。谁更合理？
4. Entropy ratio 作为 predictor——R1 列为 Must-Fix (N3，仅 2 个数据点不足以称 predictor），你在 Originality 评分中提及但未单独列为 issue。是否应升级为 Must-Fix？
5. 单 seed 问题——R1 列为 Should-Fix (W4)，你未提及。是否同意？
6. k=0.95/0.99 未测试——R1 列为 Should-Fix (W6)，你未提及。是否同意？

---

# Reviewer 1 — Round 1 审稿意见

**论文**: "Why Token Pruning Crashes Some Robot Policies but Not Others: The Role of Vision Connectors in VLA Token Compressibility"

---

## 总体评分
**Overall**: 2/4（Borderline Reject）
**一句话总结**: 研究问题有价值、实验设计系统，但核心 claim 的证据链存在多处断裂：scale confound 未解决、关键 claim 仅有 2 个数据点支撑、baseline 远低于官方值使 cliff-edge 的普适性存疑、多处 claim 措辞超出数据支撑范围。

---

## 官方维度打分

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Originality | 3/4 | 首次系统性跨架构闭环评估 VLA token pruning，研究问题明确且有实际意义；但核心洞察（pixel-shuffle 不可压缩）相对直觉可预期 |
| Quality | 2/4 | 实验设计框架合理（6 配置 ablation + 跨架构对比 + learned compression），但存在未解决的 scale confound、单 seed、baseline 偏低、关键 claim 数据点不足等问题 |
| Clarity | 3/4 | 写作总体清晰，叙事线完整，图表信息密度合理；但 Section 5.2 offline metric disconnect 缺少具体数据支撑 |
| Significance | 2/4 | 对 VLA 部署有实用参考价值，但结论的普适性受限于 2 个模型 + 1 个 benchmark + 远低于 SOTA 的 baseline |
| Relevance | 4/4 | 完全契合 CoRL：VLA 推理效率、机器人策略部署、闭环评估 |
| Limitations | 3/4 | Section 5.5 承认了主要局限，但对 baseline 偏低的影响讨论不足 |

---

## Must-Fix 问题

**N1** [critical] Scale Confound 未被充分处理——核心 claim 的有效性存疑

- SmolVLA (0.5B, pixel-shuffle) vs OpenVLA (7B, MLP projector) 同时改变了两个变量。三条间接论据均有漏洞：
  - k=0.9 论据：0.5B 模型 baseline 仅 44.8%，处于 capacity-marginal 状态，对输入扰动敏感可能与 connector 无关
  - Entropy ratio 论据：7B 有 32 层 vs 16 层，更深网络本身更容易发展 selective attention
  - 论文自身承认需要 controlled experiment，但标题/abstract/conclusion 仍使用因果归因语言

**N2** [critical] SmolVLA Baseline 远低于官方值（44.8% vs 87.3%），cliff-edge claim 的普适性存疑

- 性能几乎腰斩，模型处于功能边缘状态
- 如果在 87.3% baseline 下 removing 10% tokens 导致降到 70%（而非 0%），cliff-edge 就不存在
- "the relevant comparison is the relative change" 的论点不成立：well-trained 模型的 attention pattern 和 token dependence 可能截然不同

**N3** [critical] Attention Entropy Ratio 作为 "Compressibility Predictor" 仅有 2 个数据点

- 从 2 个数据点无法建立任何预测关系
- 这 2 个数据点还受 scale confound 污染
- Abstract 和 introduction 中的表述比 Section 4.2 的 hedging 更强烈

---

## Should-Fix 问题

**W1** [warning] Smart Compress 15pp gain 来源未 disentangle（cross-attention vs additional capacity）
**W2** [warning] M=96 outlier（52.6%）未被合理解释，且 CI 不与 M=32/64 重叠
**W3** [warning] "Cost-free deployment benefit" overstated（6% latency gain，需 22.2M 参数 + 100K 训练）
**W4** [warning] 单 seed 实验设计削弱所有统计 claim
**W5** [warning] Offline Metric Disconnect（Contribution 4）缺少具体数据（无 table/figure 支撑）
**W6** [warning] Cliff-edge 在 k∈{0.95, 0.99} 未被测试

---

## 小问题

- M1: Table 1 中 ACIS k=0.5 只有 300 episodes（vs 其他 500）
- M2: OpenVLA 和 SmolVLA 的 k 值集合不完全对齐
- M3: OpenVLA entropy 测量仅 250 frames（vs SmolVLA 2400）
- M4: 7 条 bib 条目 author mismatch
- M5: ACIS train-without-pruning / evaluate-with-pruning 不一致
- M6: 未与 4 篇 concurrent VLA compression works 进行实验对比

---

## Questions to Authors

Q1: 是否可能在更接近 87.3% baseline 下验证 cliff-edge？
Q2: Smart Compress gain 是否可能来自 retraining 本身？是否尝试过 baseline + 100K 步 control？
Q3: M=96 是否在不同 seed 下复现？
Q4: 111.5% relative action error 的具体测量条件？
Q5: 是否考虑过测试 k=0.95 或 k=0.98？

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 70 · 2026-05-18T11:40:12.501962+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "\n## Reviewer 2 交叉回应完成\n\n已逐条回应 Reviewer 1 的审稿意见，格式为 [AGREE]/[REBUT]。\n\n### 关键分歧解决\n\n1. **Scale confound**: 一致 Must-Fix\n2. **Smart Compress confound**: R1=Should-Fix, R2=Must-Fix → 我维持 Must-Fix（Contribution 3 的因果 claim 缺少控制实验）\n3. **Baseline 偏低**: R1=Must-Fix, R2 原=Should-Fix → 接受 R1 论证，升级为 Must-Fix（cliff-edge 在 undertrained checkpoint 上的普适性存疑）\n4. **Entropy ratio predictor**: R1=Must-Fix → R2 建议 Should-Fix with conditional escalation（取决于作者是否弱化措辞）\n5. **单 seed**: R1=Should-Fix → R2 同意，此前遗漏\n6. **k=0.95/0.99**: R1=Should-Fix → R2 同意，此前遗漏\n\n### 综合 Must-Fix 列表（合并两份审稿）\n- Scale confound（两人一致）\n- Baseline 偏低（R1 主张，R2 同意升级）\n- Smart Compress gain confound（R2 主张）\n- CogACT 缺引用（R2 独立发现）\n- 图片/模板/行号缺失（R2 格式审查）\n",
  "reviewer_id": "2",
  "project": "importance_margin_vla_compress"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "\n## Reviewer 2 交叉回应完成\n\n已逐条回应 Reviewer 1 的审稿意见，格式为 [AGREE]/[REBUT]。\n\n### 关键分歧解决\n\n1. **Scale confound**: 一致 Must-Fix\n2. **Smart Compress confound**: R1=Should-Fix, R2=Must-Fix → 我维持 Must-Fix（Contribution 3 的因果 claim 缺少控制实验）\n3. **Baseline 偏低**: R1=Must-Fix, R2 原=Should-Fix → 接受 R1 论证，升级为 Must-Fix（cliff-edge 在 undertrained checkpoint 上的普适性存疑）\n4. **Entropy ratio predictor**: R1=Must-Fix → R2 建议 Should-Fix with conditional escalation（取决于作者是否弱化措辞）\n5. **单 seed**: R1=Should-Fix → R2 同意，此前遗漏\n6. **k=0.95/0.99**: R1=Should-Fix → R2 同意，此前遗漏\n\n### 综合 Must-Fix 列表（合并两份审稿）\n- Scale confound（两人一致）\n- Baseline 偏低（R1 主张，R2 同意升级）\n- Smart Compress gain confound（R2 主张）\n- CogACT 缺引用（R2 独立发现）\n- 图片/模板/行号缺失（R2 格式审查）\n",
    "reviewer_id": "2",
    "project": "importance_margin_vla_compress"
  }
}
```

</details>

---


### Tool result

_source line 71 · 2026-05-18T11:40:16.367307+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3865
}
```

</details>

---


### Assistant

_source line 72 · 2026-05-18T11:40:19.166484+00:00_

交叉回应已完成并提交给 Director。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2"
}
```

</details>

---


## Round 3

## Round 3

94 recorded events


### User

_source line 73 · 2026-05-19T01:13:17.640025+00:00_

[Round 1 审稿请求]:
## Round 1 审稿任务 — Reviewer 2

**你的审查侧重：新颖性 + Related Work 完整性 + 写作质量 + 格式合规**

### 目标 Venue
- **CoRL 2026**（Conference on Robot Learning）
- Deadline: 2026-05-29
- 正文 8 页限制（参考文献、附录不计入）
- Double-blind 匿名审稿
- 需要 Limitations section（计入 8 页）
- 模板: corl_2026.sty（submission 模式）

### 论文路径
- 主文件: `projects/importance_margin_vla_compress/docs/paper/main.tex`
- 各章节在同目录下：abstract.tex, introduction.tex, related_work.tex, experimental_setup.tex, results.tex, analysis.tex, conclusion.tex, appendix.tex
- 参考文献: references.bib

### 论文概要
论文研究 VLA 模型中 vision token pruning 的跨架构行为差异。核心发现：pixel-shuffle connector（SmolVLA）下 token pruning 导致 cliff-edge failure（59.2% → 0%），而 MLP projector（OpenVLA）graceful degradation（74.0% → 37.4%）。提出 cross-attention re-encoding（Smart Compress）克服 cliff-edge，在 75% token reduction 下保持 61.6% SR。

### 审查重点（请逐一覆盖）

1. **新颖性与贡献评估**
   - "Architecture-dependent compressibility" 的发现是否足够 novel？还是 expected？
   - Smart Compress（cross-attention pooling）的方法贡献——与 Q-Former、Perceiver 的区别在哪？
   - "first cross-architecture closed-loop evaluation" 的 claim 是否准确？
   - 对 CoRL 社区的实际影响：这些发现是否改变 practitioner 的设计决策？

2. **Related Work 完整性**
   - VLA 效率工作：VLA-Cache, VLA-IAP, EfficientVLA, VLA-Pruner 是否都被充分讨论？
   - 是否遗漏重要的 token efficiency 工作（如 SparseVLM、CrossGET 等 2025-2026 新工作）？
   - Vision connector taxonomy 的 related work 是否完整？
   - 引用数量和密度是否达到 CoRL 标准？

3. **写作质量**
   - Abstract 是否在 30 秒内传达核心价值？
   - Introduction 叙事线是否连贯（背景→问题→不足→贡献）？
   - AI 写作标志检测：
     - Em-dash（—）和解释性 en-dash（–）的使用
     - -ing 短语结尾（"..., highlighting/demonstrating/showing..."）
     - 过度使用 "Furthermore/Moreover/Additionally"
     - 过度分段（每段 2-3 句即换段）
     - 黑名单词汇："delve into", "leverage", "utilize", "facilitate", "paradigm shift"
   - 专有名词/缩写首次出现是否有定义？
   - 段落间逻辑过渡是否自然？

4. **格式合规**
   - 正文是否在 8 页以内？
   - Limitations section 是否存在且实质性？
   - 匿名化：是否有作者信息泄露？
   - 行号是否启用？
   - 表格格式：小数精度是否统一？最优加粗？Caption 是否自包含？
   - Figure 质量：字体大小、信息密度、是否有遮挡？
   - References 格式：bib 条目是否一致？venue 名称是否完整？

5. **图表审查**
   - Figure 1（架构对比）信息量是否充分？
   - Figure 2（degradation + compression curves）是否清晰传达核心发现？
   - Figure 3（pixel-shuffle）和 Figure 4（entropy layers）是否必要？能否合并？
   - 图表与正文空间的比例是否合理？

6. **附录审查**
   - 附录内容是否在正文中有引用？
   - 是否有应放在正文中的关键信息被放在了附录？
   - Inference Cost-Benefit Analysis（Appendix）的结论是否与正文 framing 一致？

请按 CoRL 标准产出完整审稿报告，结构：Summary → Strengths → Weaknesses (Must-Fix / Should-Fix / Minor) → Questions → Missing References → Overall Assessment（评分+置信度）→ Detailed Comments。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 74 · 2026-05-19T01:13:30.166862+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/.claude/skills/review-reviewer-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/.claude/skills/review-reviewer-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 75 · 2026-05-19T01:13:30.217794+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/.claude/sessions/review_reviewer_2_29d69ba3.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 76 · 2026-05-19T01:13:31.422564+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebSearch,WebFetch,mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director,mcp__agent-ml-research__verify_references",
  "max_results": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebSearch,WebFetch,mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director,mcp__agent-ml-research__verify_references",
    "max_results": "5"
  }
}
```

</details>

---


### Tool result

_source line 77 · 2026-05-19T01:13:31.726955+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "ToolSearch",
  "elapsed_ms": 304
}
```

</details>

---


### Tool call

_source line 78 · 2026-05-19T01:13:36.398603+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "CoRL 2026 reviewer guidelines review form criteria"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "CoRL 2026 reviewer guidelines review form criteria"
  }
}
```

</details>

---


### Tool call

_source line 79 · 2026-05-19T01:13:36.900992+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 80 · 2026-05-19T01:13:37.354371+00:00_

1	\documentclass{article}
2	
3	\usepackage{corl_2026} % Submission version: anonymous, line numbers enabled.
4	% \usepackage[final]{corl_2026} % Uncomment for camera-ready.
5	
6	\usepackage{amsmath,amssymb}
7	\usepackage{graphicx}
8	\usepackage{booktabs}
9	\usepackage{enumitem}
10	\usepackage{subcaption}
11	
12	\title{Why Token Pruning Crashes Some Robot Policies but Not Others:\\The Role of Vision Connectors in VLA Token Compressibility}
13	
14	\begin{document}
15	\maketitle
16	
17	\input{abstract}
18	
19	\keywords{vision-language-action models, token pruning, robot learning}
20	
21	\input{introduction}
22	
23	\input{related_work}
24	
25	\input{experimental_setup}
26	
27	\input{results}
28	
29	\input{analysis}
30	
31	\input{conclusion}
32	
33	\bibliography{references}
34	
35	\input{appendix}
36	
37	\end{document}
38	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 453
}
```

</details>

---


### Tool call

_source line 81 · 2026-05-19T01:13:37.354840+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 82 · 2026-05-19T01:13:37.857421+00:00_

1	\begin{abstract}
2	Vision token pruning reliably accelerates Vision Transformer (ViT) inference with negligible accuracy loss, prompting recent proposals to apply the same technique to Vision-Language-Action (VLA) models for faster robotic control. We conduct the first cross-architecture closed-loop evaluation of vision token reduction on two VLA architectures and find that compressibility is attributable to the vision connector design. SmolVLA, whose pixel-shuffle connector spatially folds patches into high-density tokens, exhibits a cliff-edge failure: pruning collapses success rate from 59.2\% to 0\% on the official checkpoint, with even 5\% token removal (7 of 128) causing complete task failure. This failure is robust across two checkpoints of different training quality, seven pruning configurations, and three pruning mechanisms. OpenVLA, whose MLP projector maps patches independently, degrades gracefully: at $k{=}0.95$ it retains 69.4\% SR ($-4.6$pp) where SmolVLA drops to 0\%. We trace the divergence to token information density: pixel-shuffle produces tokens with near-uniform attention across all transformer layers, while MLP-projected tokens develop progressively selective attention in deeper layers. For architectures where pruning fails, a learned cross-attention module overcomes the cliff-edge by re-encoding rather than deleting tokens, raising success rate to 61.6\% with 75\% fewer tokens, a performance-neutral deployment benefit. Our experiments on SmolVLA and OpenVLA, together with recent findings on CogACT, reveal a consistent pattern across three models spanning two connector families: VLA token compressibility is architecture-dependent, and cross-attention re-encoding can overcome failures that all deletion-based methods share.
3	\end{abstract}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 83 · 2026-05-19T01:13:37.857866+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 84 · 2026-05-19T01:13:38.310054+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	Vision token pruning is one of the most reliable efficiency techniques in Vision Transformer (ViT) inference: DynamicViT~\cite{rao2021dynamicvit} removes 66\% of tokens with $<$0.5\% accuracy loss, ToMe~\cite{bolya2023tome} merges 40\% at $>$99\% accuracy, and EViT~\cite{liang2022evit} discards 50\% with negligible degradation. These results have established a strong prior that vision tokens are highly redundant. Vision-Language-Action (VLA) models~\cite{brohan2023rt1,brohan2023rt2,kim2024openvla,black2024pi0,ghosh2024octo,shukor2025smolvla} use the same ViT encoders, producing hundreds of tokens that dominate the LLM backbone's input. For real-time robotic control at 5--10 Hz, reducing these tokens would yield immediate speedups in the quadratically scaling attention computation. Several recent works explore this direction: FastV~\cite{chen2024fastv} prunes inattentive VLM tokens, VLA-Cache~\cite{xu2025vlacache} caches vision tokens across timesteps, and VLA-IAP~\cite{cheng2026vlaiap} proposes importance-aware VLA pruning.
5	
6	However, no prior work has systematically evaluated how vision token reduction behaves across different VLA architectures in closed-loop control, where a single corrupted action can push the robot off-trajectory and subsequent errors compound irrecoverably. Existing evaluations rely on offline metrics (action loss, perplexity) that average over independent timesteps and fail to capture this compounding failure mode.
7	
8	We conduct the first cross-architecture closed-loop evaluation. On SmolVLA (451.5M parameters, pixel-shuffle connector), seven pruning configurations spanning scoring function, retention ratio ($k \in \{0.5, 0.7, 0.9, 0.95\}$), and mechanism (zero-masking, true removal, token merging) all collapse to 0\% Success Rate (SR) across 500 episodes (Wilson 95\% CI: [0\%, 0.76\%]), even when retaining 95\% of tokens. The official SmolVLA checkpoint (59.2\% baseline) exhibits t
…[truncated 1791 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 85 · 2026-05-19T01:13:38.310545+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 86 · 2026-05-19T01:13:39.264741+00:00_

1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{Vision token efficiency.}
5	Token pruning in ViTs is well established: DynamicViT~\cite{rao2021dynamicvit}, EViT~\cite{liang2022evit}, and ToMe~\cite{bolya2023tome} consistently remove 30--60\% of tokens with $<$1\% accuracy loss on ImageNet. For VLMs, FastV~\cite{chen2024fastv} and LLaVA-PruMerge~\cite{shang2024prumerge} extend pruning to language-vision tasks. We test whether these results transfer to closed-loop VLA control, where action errors compound across timesteps.
6	
7	\paragraph{VLA-specific token reduction.}
8	VLA-Cache~\cite{xu2025vlacache} caches vision KV states across timesteps for 1.7$\times$ speedup without removing tokens. VLA-IAP~\cite{cheng2026vlaiap} uses interaction-aligned pruning on OpenVLA; EfficientVLA~\cite{yang2025efficientvla} combines layer pruning and token selection on CogACT; VLA-Pruner~\cite{liu2025vlapruner} uses dual-level importance criteria for temporal-aware pruning. All evaluate on MLP-projector architectures. None reports the cliff-edge failure we observe on pixel-shuffle VLAs, suggesting their positive results may not generalize to spatially entangled connectors.
9	
10	\paragraph{Vision connectors.}
11	Per-patch MLP projectors~\cite{liu2023llava,kim2024openvla} preserve per-token granularity. Cross-attention connectors (Q-Former~\cite{li2023blip2}, Perceiver~\cite{alayrac2022flamingo,jaegle2021perceiver}) compress to learned queries at the architectural level. Pixel-shuffle connectors~\cite{shi2016subpixel,shukor2025smolvla,chen2024internvl} fold patches via channel concatenation, achieving training-time compression but creating inter-token dependencies. Our analysis links this taxonomy to inference-time compressibility and shows that cross-attention re-encoding can overcome the failure mode of deletion on pixel-shuffle architectures.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 954
}
```

</details>

---


### Tool call

_source line 87 · 2026-05-19T01:13:39.315544+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/experimental_setup.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/experimental_setup.tex"
  }
}
```

</details>

---


### Tool result

_source line 88 · 2026-05-19T01:13:39.769711+00:00_

1	\section{Experimental Setup}
2	\label{sec:experimental_setup}
3	
4	\subsection{Architectures and Benchmark}
5	\label{sec:setup_overview}
6	
7	We study two VLA architectures whose vision connectors differ in how they map encoder patches to language model input tokens (Figure~\ref{fig:architecture}). SmolVLA~\cite{shukor2025smolvla} (451.5M parameters) encodes each camera image with SigLIP~\cite{zhai2023siglip} into 1024 patches on a $32 \times 32$ grid, then applies a pixel-shuffle connector that folds each $4 \times 4$ block into one token by channel concatenation, producing 64 tokens per camera (128 total from two cameras). Each token encodes 16 spatially contiguous patches; removing one eliminates an entire $4 \times 4$ receptive field with no redundancy. The 128 tokens enter a Qwen2-0.5B backbone~\cite{yang2024qwen2} that generates continuous 7-DoF actions via flow matching~\cite{lipman2023flow}. OpenVLA~\cite{kim2024openvla} (7B parameters) uses DINOv2~\cite{oquab2023dinov2} and SigLIP encoders with a two-layer MLP projector that maps each patch independently into a Llama-2 backbone, producing 256 tokens that preserve per-token independence.
8	
9	\begin{figure}[t]
10	\centering
11	\includegraphics[width=\linewidth]{figures/paper/fig_architecture.pdf}
12	\caption{Vision connector comparison. SmolVLA's pixel-shuffle folds $4{\times}4$ patches into single tokens (128 total, spatially entangled). OpenVLA's MLP projector maps each patch independently (256 tokens, per-token independence).}
13	\label{fig:architecture}
14	\end{figure}
15	
16	We evaluate on LIBERO~\cite{liu2023libero}, a suite of language-conditioned tabletop manipulation tasks with three suites: Object (10 manipulation tasks), Spatial (10 spatial reasoning tasks), and Goal (10 goal-conditioned tasks). Each condition uses 50 episodes per task (500 per suite), evaluated by closed-loop Success Rate (SR) with Wilson 95\% confidence intervals. SmolVLA baselines: 44.8\% (Object), 51.8\% (Spatial), 63.0\% (G
…[truncated 1894 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 454
}
```

</details>

---


### Tool call

_source line 89 · 2026-05-19T01:13:39.823285+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/results.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/results.tex"
  }
}
```

</details>

---


### Tool result

_source line 90 · 2026-05-19T01:13:40.275329+00:00_

1	\section{Results}
2	\label{sec:results}
3	
4	We evaluate token pruning across two VLA architectures on LIBERO-Object~\cite{liu2023libero} (10 tasks, 50 episodes each, 500 total). All success rates include Wilson 95\% confidence intervals.
5	
6	\subsection{SmolVLA: Cliff-Edge Under All Pruning Methods}
7	\label{sec:smolvla_results}
8	
9	The SmolVLA baseline (bypass mode, all 128 vision tokens) achieves 44.8\% SR (224/500, CI [40.5\%, 49.2\%]).\footnote{The official SmolVLA result is 87.3\% SR with batch size 64 on 8 GPUs. Our reproduction uses a smaller batch due to compute constraints.} Table~\ref{tab:smolvla_ablation} reports the full ablation. Every pruning configuration produces 0\% SR (Wilson CI upper bounds $\leq$0.80\%). Three observations make this striking: (1)~\textbf{Scoring-independent}: random selection performs identically to learned ACIS scoring. (2)~\textbf{Ratio-independent}: retaining 95\% of tokens ($k{=}0.95$, removing only 7 of 128) causes the same failure as retaining 50\%. (3)~\textbf{Mechanism-independent}: zero-masking, true removal, and token merging all produce 0\% SR.
10	
11	\begin{table}[t]
12	\centering
13	\small
14	\caption{SmolVLA pruning ablation on LIBERO-Object. All configurations collapse to 0\% SR. The official checkpoint (59.2\% baseline) shows the same cliff-edge.}
15	\label{tab:smolvla_ablation}
16	\begin{tabular}{llccrr}
17	\toprule
18	Scoring & $k$ & Mechanism & SR (\%) & Episodes & Wilson 95\% CI \\
19	\midrule
20	\multicolumn{2}{l}{\textit{Baseline (bypass)}} & -- & 44.8 & 500 & [40.5, 49.2] \\
21	\midrule
22	ACIS & 0.50 & Zero-mask & 0.00 & 500 & [0, 0.76] \\
23	ACIS & 0.70 & Zero-mask & 0.00 & 500 & [0, 0.76] \\
24	ACIS & 0.90 & Zero-mask & 0.00 & 500 & [0, 0.76] \\
25	Random & 0.95 & Zero-mask & 0.00 & 500 & [0, 0.76] \\
26	Random & 0.50 & Zero-mask & 0.00 & 500 & [0, 0.76] \\
27	ACIS & 0.50 & True removal & 0.00 & 500 & [0, 0.80] \\
28	ACIS & 0.50 & Merge (ToMe) & 0.00 & 500 & [0, 0.76] \\
29	\midrule
30	\multicolumn{
…[truncated 6560 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 91 · 2026-05-19T01:13:40.275863+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/analysis.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/analysis.tex"
  }
}
```

</details>

---


### Tool result

_source line 92 · 2026-05-19T01:13:40.727786+00:00_

1	\section{Analysis and Discussion}
2	\label{sec:analysis}
3	
4	\subsection{Connector Design Shapes Compressibility}
5	\label{sec:pixel_shuffle}
6	
7	The divergence between SmolVLA and OpenVLA traces to their vision connectors. SmolVLA's pixel-shuffle applies $4 \times 4$ spatial folding, so each of its 128 tokens encodes 16 patches via channel concatenation. Removing any token eliminates an entire receptive field with no redundancy from neighbors (Figure~\ref{fig:pixel_shuffle}). Because the folding is fixed and non-learned, no downstream layer can recover discarded information. OpenVLA's MLP projector maps each patch independently: removing one of 256 tokens discards $\sim$1/256 of the visual field, a localized loss that self-attention layers can partially compensate. At $k{=}0.50$, OpenVLA retains 37.4\% SR against a 74.0\% baseline; SmolVLA collapses to 0\% even at $k{=}0.95$.
8	
9	\begin{figure}[t]
10	\centering
11	\includegraphics[width=0.85\linewidth]{figures/paper/fig_pixel_shuffle.pdf}
12	\caption{Pixel-shuffle folding: each $4{\times}4$ block of SigLIP patches is channel-concatenated into one token. Removing any token eliminates its receptive field (gray) with no redundancy.}
13	\label{fig:pixel_shuffle}
14	\end{figure}
15	
16	The attention entropy ratio quantifies this structural difference. We measure normalized Shannon entropy of attention weights on vision tokens (1.0 = uniform, lower = selective). SmolVLA's ratio is 0.95, near-uniform across all 16 layers (range 0.93--0.98, total variation 0.05). OpenVLA's overall ratio is 0.64, with progressive sharpening from 0.98 in layer 0 to 0.48 in layer 29 (total variation 0.50, $10\times$ SmolVLA's; see Figure~\ref{fig:entropy_layers} and Appendix~\ref{app:entropy_details}). This reflects fundamentally different information structures: pixel-shuffle tokens are uniformly information-dense and resist selective attention at every processing depth, while MLP-projected tokens allow the model to learn spatial select
…[truncated 4178 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 451
}
```

</details>

---


### Tool call

_source line 93 · 2026-05-19T01:13:40.728276+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 94 · 2026-05-19T01:13:41.180430+00:00_

1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	We presented the first cross-architecture closed-loop evaluation of vision token reduction in VLA models. Compressibility is attributable to the vision connector: pixel-shuffle connectors create spatially entangled tokens that collapse under any form of deletion (59.2\% $\to$ 0\% on the official checkpoint), while MLP projectors degrade gracefully (74.0\% $\to$ 37.4\%). The attention entropy ratio (0.95 vs.\ 0.64) captures this divergence, consistent across three models and two connector families~\cite{yang2025efficientvla}. For architectures where pruning fails, cross-attention re-encoding raises SR from 44.8\% to $\sim$60\% (a matched training-only control confirms the gain is architectural), and compressing to 32 queries (75\% token reduction) preserves this gain at 61.6\%, demonstrating that re-encoding can succeed where deletion cannot. Standard offline metrics do not predict these closed-loop outcomes; closed-loop evaluation is essential for validating VLA compression.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 95 · 2026-05-19T01:13:41.230957+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 96 · 2026-05-19T01:13:42.135066+00:00_

1	\appendix
2	
3	\section{Per-Task Breakdown Tables}
4	\label{app:per_task}
5	
6	\subsection{SmolVLA Baseline Per-Task Results}
7	
8	Table~\ref{tab:smolvla_baseline_pertask} reports per-task success rates for the SmolVLA baseline (bypass mode, no pruning) on LIBERO-Object. All pruning conditions (Table~\ref{tab:smolvla_ablation}) produce 0\% success rate on every task; we omit per-task breakdowns for pruning conditions as they carry no additional information beyond the aggregate 0\% already reported.
9	
10	\begin{table}[ht]
11	\centering
12	\small
13	\caption{SmolVLA baseline (bypass mode) per-task success rates on LIBERO-Object (50 episodes per task, 500 total). Overall SR: 44.8\%.}
14	\label{tab:smolvla_baseline_pertask}
15	\begin{tabular}{lc}
16	\toprule
17	Task & SR (\%) \\
18	\midrule
19	alphabet\_soup & 22 \\
20	bbq\_sauce & 60 \\
21	butter & 42 \\
22	chocolate\_pudding & 38 \\
23	cream\_cheese & 58 \\
24	ketchup & 26 \\
25	milk & 62 \\
26	orange\_juice & 38 \\
27	salad\_dressing & 50 \\
28	tomato\_sauce & 52 \\
29	\midrule
30	\textbf{Overall} & \textbf{44.8} \\
31	\bottomrule
32	\end{tabular}
33	\end{table}
34	
35	\subsection{Official SmolVLA Checkpoint Per-Task Results}
36	
37	Table~\ref{tab:smolvla_official_pertask} reports per-task success rates for the official SmolVLA LIBERO checkpoint (HuggingFaceVLA/smolvla\_libero). Under 50\% random token removal, all tasks produce 0\% SR, identical to the fine-tuned checkpoint results.
38	
39	\begin{table}[ht]
40	\centering
41	\small
42	\caption{Official SmolVLA checkpoint per-task success rates on LIBERO-Object (50 episodes per task, 500 total). Overall SR: 59.2\%. Under 50\% random pruning, all tasks collapse to 0\%.}
43	\label{tab:smolvla_official_pertask}
44	\begin{tabular}{lcc}
45	\toprule
46	Task & Baseline SR (\%) & $k{=}0.5$ SR (\%) \\
47	\midrule
48	alphabet\_soup & 64 & 0 \\
49	bbq\_sauce & 38 & 0 \\
50	butter & 78 & 0 \\
51	chocolate\_pudding & 90 & 0 \\
52	cream\_cheese & 40 & 0 \\
53	ketchup & 60 & 0 \\
…[truncated 13062 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 904
}
```

</details>

---


### Tool call

_source line 97 · 2026-05-19T01:13:42.135709+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/references.bib"
  }
}
```

</details>

---


### Tool result

_source line 98 · 2026-05-19T01:13:42.588033+00:00_

1	% References for: The Cliff Edge — Why Vision Token Reduction Fails
2	% Catastrophically in VLA Closed-Loop Control
3	% Auto-generated from literature_map.yaml (verified entries only)
4	% 2026-05-17
5	
6	% ============================================================
7	% VLA Models
8	% ============================================================
9	
10	@article{shukor2025smolvla,
11	  title={{SmolVLA}: A Vision-Language-Action Model for Affordable and Efficient Robotics},
12	  author={Shukor, Mustafa and Aubakirova, Dana and Casas, Adrien and others},
13	  journal={arXiv preprint arXiv:2506.01844},
14	  year={2025}
15	}
16	
17	@inproceedings{kim2024openvla,
18	  title={{OpenVLA}: An Open-Source Vision-Language-Action Model},
19	  author={Kim, Moo Jin and Pertsch, Karl and Karamcheti, Siddharth and others},
20	  booktitle={Proceedings of the 8th Conference on Robot Learning (CoRL)},
21	  year={2024}
22	}
23	
24	@inproceedings{brohan2023rt2,
25	  title={{RT-2}: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control},
26	  author={Brohan, Anthony and Brown, Noah and Carbajal, Justice and others},
27	  booktitle={Proceedings of the 7th Conference on Robot Learning (CoRL)},
28	  year={2023}
29	}
30	
31	
32	@article{black2024pi0,
33	  title={$\pi_0$: A Vision-Language-Action Flow Model for General Robot Control},
34	  author={Black, Kevin and Brown, Noah and Driess, Danny and others},
35	  journal={arXiv preprint arXiv:2410.24164},
36	  year={2024}
37	}
38	
39	@inproceedings{ghosh2024octo,
40	  title={Octo: An Open-Source Generalist Robot Policy},
41	  author={{Octo Model Team} and Ghosh, Dibya and Walke, Homer and Pertsch, Karl and Black, Kevin and others},
42	  booktitle={Robotics: Science and Systems (RSS)},
43	  year={2024}
44	}
45	
46	@inproceedings{brohan2023rt1,
47	  title={{RT-1}: Robotics Transformer for Real-World Control at Scale},
48	  author={Brohan, Anthony and Brown, Noah and Carbajal, Justice and others},
49	  booktitle={Robotics: Science 
…[truncated 7642 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 99 · 2026-05-19T01:13:42.638751+00:00_

called mcp__agent-ml-research__verify_references

<details open><summary>🔧 Tool call — mcp__agent-ml-research__verify_references</summary>

```json
{
  "paper_dir": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper",
  "project": "importance_margin_vla_compress"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "mcp__agent-ml-research__verify_references",
  "tool_args": {
    "paper_dir": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper",
    "project": "importance_margin_vla_compress"
  }
}
```

</details>

---


### Tool result

_source line 100 · 2026-05-19T01:13:43.191357+00:00_

Web search results for query: "CoRL 2026 reviewer guidelines review form criteria"

Links: [{"title":"CoRL 2026 - Instruction for Authors","url":"https://www.corl.org/contributions/instruction-for-authors"},{"title":"ICLR 2026 Reviewer Guide","url":"https://iclr.cc/Conferences/2026/ReviewerGuide"},{"title":"CoRL 2026 - Call for Papers","url":"https://www.corl.org/contributions/call-for-papers"},{"title":"Reviewer Guidelines — CoRL 2023","url":"https://www.corl2023.org/reviewer-guidelines"},{"title":"CVPR 2026 Reviewer Guidelines","url":"https://cvpr.thecvf.com/Conferences/2026/ReviewerGuidelinesq"},{"title":"Which Coauthor Should I Nominate in My 99 ICLR Submissions? A Mathematical Analysis of the ICLR 2026 Reciprocal Reviewer Nomination Policy","url":"https://arxiv.org/pdf/2512.17950"},{"title":"CoRL 2024 - Instruction for Reviews","url":"https://2024.corl.org/contributions/instruction-for-reviews"}]

Based on the search results, I found some information about CoRL 2026, though the specific detailed reviewer guidelines and review form criteria for 2026 appear to be limited in the search results. Here's what I found:

## CoRL 2026 Submission and Reviewer Requirements

All submissions must include at least one author who agrees to serve as a CoRL reviewer, and they are qualified if they have at least one accepted publication at a previous robotics (CoRL/ ICRA/ IROS/ RSS) or learning conference (ICLR/ NeurIPS/ ICML) or equivalent journal.

## Submission Focus and Content Requirements

Submissions should focus on a core robotics problem and demonstrate the relevance of proposed models, algorithms, datasets, and benchmarks to robotics. Additionally, all submissions should include a Limitations section, explicitly describing limiting assumptions, failure modes, and other limitations of the results and experiments and how these might be addressed in the future.

## Related Review Criteria (from CoRL 2024)

While specific 2026 review form criteria are limited in the result
…[truncated 565 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 6792
}
```

</details>

---


### Tool result

_source line 101 · 2026-05-19T01:14:05.976732+00:00_

{"result":"{\"success\": true, \"data\": {\"summary\": {\"total_bib_entries\": 26, \"total_citations\": 41, \"unique_cited_keys\": 26, \"orphan_bib\": 0, \"missing_bib\": 0, \"duplicate_keys\": 0, \"online_verified\": 20, \"online_not_found\": 1, \"online_mismatch\": 5}, \"cross_check\": {\"orphan_bib\": [], \"missing_bib\": [], \"orphan_count\": 0, \"missing_count\": 0}, \"bib_entries\": [{\"key\": \"shukor2025smolvla\", \"type\": \"article\", \"title\": \"SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics\", \"authors\": \"Shukor, Mustafa and Aubakirova, Dana and Casas, Adrien and others\", \"year\": \"2025\", \"venue\": \"arXiv preprint arXiv:2506.01844\"}, {\"key\": \"kim2024openvla\", \"type\": \"inproceedings\", \"title\": \"OpenVLA: An Open-Source Vision-Language-Action Model\", \"authors\": \"Kim, Moo Jin and Pertsch, Karl and Karamcheti, Siddharth and others\", \"year\": \"2024\", \"venue\": \"Proceedings of the 8th Conference on Robot Learning (CoRL)\"}, {\"key\": \"brohan2023rt2\", \"type\": \"inproceedings\", \"title\": \"RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control\", \"authors\": \"Brohan, Anthony and Brown, Noah and Carbajal, Justice and others\", \"year\": \"2023\", \"venue\": \"Proceedings of the 7th Conference on Robot Learning (CoRL)\"}, {\"key\": \"black2024pi0\", \"type\": \"article\", \"title\": \"$\\\\pi_0$: A Vision-Language-Action Flow Model for General Robot Control\", \"authors\": \"Black, Kevin and Brown, Noah and Driess, Danny and others\", \"year\": \"2024\", \"venue\": \"arXiv preprint arXiv:2410.24164\"}, {\"key\": \"ghosh2024octo\", \"type\": \"inproceedings\", \"title\": \"Octo: An Open-Source Generalist Robot Policy\", \"authors\": \"Octo Model Team and Ghosh, Dibya and Walke, Homer and Pertsch, Karl and Black, K...\", \"year\": \"2024\", \"venue\": \"Robotics: Science and Systems (RSS)\"}, {\"key\": \"brohan2023rt1\", \"type\": \"inproceedings\", \"title\": \"RT-1: Roboti
…[truncated 19715 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "mcp__agent-ml-research__verify_references",
  "elapsed_ms": 23337
}
```

</details>

---


### Tool call

_source line 102 · 2026-05-19T01:14:12.997357+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://2024.corl.org/contributions/instruction-for-reviews",
  "prompt": "Extract the complete review form criteria, scoring dimensions, and rating scales for CoRL 2024 reviewers. List all dimensions with their score ranges and descriptions."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://2024.corl.org/contributions/instruction-for-reviews",
    "prompt": "Extract the complete review form criteria, scoring dimensions, and rating scales for CoRL 2024 reviewers. List all dimensions with their score ranges and descriptions."
  }
}
```

</details>

---


### Tool call

_source line 103 · 2026-05-19T01:14:13.449713+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "CoRL 2025 2026 reviewer form scoring criteria dimensions soundness novelty significance"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "CoRL 2025 2026 reviewer form scoring criteria dimensions soundness novelty significance"
  }
}
```

</details>

---


### Tool call

_source line 104 · 2026-05-19T01:14:14.404689+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "SparseVLM CrossGET vision token pruning VLM 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "SparseVLM CrossGET vision token pruning VLM 2025 2026"
  }
}
```

</details>

---


### Tool call

_source line 105 · 2026-05-19T01:14:15.510532+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"vision token\" \"robot\" OR \"VLA\" pruning compression efficiency 2025 2026 arXiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"vision token\" \"robot\" OR \"VLA\" pruning compression efficiency 2025 2026 arXiv"
  }
}
```

</details>

---


### Tool result

_source line 106 · 2026-05-19T01:14:17.470297+00:00_

# CoRL 2024 Review Criteria Summary

Based on the provided content, **the complete review form with specific scoring dimensions and rating scales is not included** in this document.

## What IS Provided:

**Review Criteria for Regular Papers:**
The document states that submissions will be assessed on:
- "significance and novelty of the results, either theoretical or empirical"
- Degree of objective establishment and potential impact
- Relevance to robotic learning

**Reviewer Qualifications:**
Reviewers should demonstrate expertise through publications in robotics and machine learning venues, with "a minimum of 3 first author publications in major robotics conferences and journals (e.g. CoRL, RSS, ICRA, IROS, IJRR, TRO, RAL)"

**Desk Rejection Criteria:**
Papers may be rejected for formatting issues, anonymity violations, or scope concerns—specifically, submissions must show relevance through explicit learning questions for physical robots or testing on physical robots.

## Missing Information:

The page does not contain specific scoring scales (e.g., 1-5, 1-10 ratings), detailed review dimensions (beyond general significance/novelty/impact), or a formal review form template. To access the actual review form, you would need to consult the full submission portal or reviewer guidelines document.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 4472
}
```

</details>

---


### Tool result

_source line 107 · 2026-05-19T01:14:22.760698+00:00_

Web search results for query: ""vision token" "robot" OR "VLA" pruning compression efficiency 2025 2026 arXiv"

Links: [{"title":"Compressor-VLA: Instruction-Guided Visual Token Compression for Efficient Robotic Manipulation","url":"https://arxiv.org/html/2511.18950v1"},{"title":"[2511.16449] VLA-Pruner: Temporal-Aware Dual-Level Visual Token Pruning for Efficient Vision-Language-Action Inference","url":"https://arxiv.org/abs/2511.16449"},{"title":"History-Conditioned Spatio-Temporal Visual Token Pruning for Efficient Vision-Language Navigation","url":"https://arxiv.org/html/2603.06480"},{"title":"[2511.18950] Compressor-VLA: Instruction-Guided Visual Token Compression for Efficient Robotic Manipulation","url":"https://arxiv.org/abs/2511.18950"},{"title":"The Better You Learn, The Smarter You Prune: Towards Efficient Vision-language-action Models via Differentiable Token Pruning","url":"https://arxiv.org/html/2509.12594v1"},{"title":"[2603.06480] History-Conditioned Spatio-Temporal Visual Token Pruning for Efficient Vision-Language Navigation","url":"https://arxiv.org/abs/2603.06480"},{"title":"Compressor-VLA: Instruction-Guided Visual Token Compression for Efficient Robotic Manipulation","url":"https://chatpaper.com/paper/212383"}]

I found several highly relevant arXiv papers on vision token pruning and compression for robot Vision-Language-Action (VLA) models from 2025-2026. Here are the key results:

## Main Papers Found:

1. **Compressor-VLA** (November 2025): A novel hybrid instruction-conditioned token compression framework designed for efficient, task-oriented compression of visual information in VLA models. It consists of two token compression modules: a Semantic Task Compressor (STC) that distills holistic, task-relevant context, and a Spatial Refinement Compressor (SRC) that preserves fine-grained spatial details.

2. **VLA-Pruner** (February 2026): A versatile plug-and-play VLA-specific token prune method that aligns with the dual-system nature of VLA mo
…[truncated 734 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 7250
}
```

</details>

---


### Tool result

_source line 108 · 2026-05-19T01:14:25.673082+00:00_

Web search results for query: "SparseVLM CrossGET vision token pruning VLM 2025 2026"

Links: [{"title":"(PDF) SparseVLM+: Visual Token Sparsification with Improved Text-Visual Attention Pattern","url":"https://www.researchgate.net/publication/398766915_SparseVLM_Visual_Token_Sparsification_with_Improved_Text-Visual_Attention_Pattern"},{"title":"SparseVLM: Visual Token Sparsification for Efficient Vision-Language Model Inference | OpenReview","url":"https://openreview.net/forum?id=80faIPZ67S"},{"title":"SparseVLM: Visual Token Sparsification for Efficient Vision-Language Model Inference","url":"https://arxiv.org/html/2410.04417v4"},{"title":"SparseVLM: Visual Token Sparsification for Efficient Vision Language Models Inference | OpenReview","url":"https://openreview.net/forum?id=1xG3MN1RRW"},{"title":"SparseVILA: Decoupling Visual Sparsity for Efficient VLM Inference","url":"https://arxiv.org/pdf/2510.17777"},{"title":"[2410.04417] SparseVLM: Visual Token Sparsification for Efficient Vision-Language Model Inference","url":"https://arxiv.org/abs/2410.04417"},{"title":"Similarity-Aware Token Pruning: Your VLM but Faster","url":"https://arxiv.org/pdf/2503.11549"},{"title":"VLM-Pruner: Buffering for Spatial Sparsity in an Efficient VLM Centrifugal Token Pruning Paradigm","url":"https://arxiv.org/pdf/2512.02700"}]

Based on the search results, here's what I found about SparseVLM and vision token pruning for VLMs:

## SparseVLM Overview

SparseVLM is an efficient text-aware training-free vision token optimization mechanism designed to improve the efficiency of vision-language models. In vision-language models (VLMs), visual tokens usually consume a significant amount of computational overhead, despite their sparser information density compared to text tokens.

## How It Works

The method is a training-free token optimization mechanism without extra parameters or fine-tuning costs, which selects visual-relevant text tokens to rate the significance of vision tokens within th
…[truncated 1155 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 11268
}
```

</details>

---


### Tool result

_source line 109 · 2026-05-19T01:14:32.655258+00:00_

Web search results for query: "CoRL 2025 2026 reviewer form scoring criteria dimensions soundness novelty significance"

Links: [{"title":"CoRL 2025 Accepted Paper List - Paper Copilot","url":"https://papercopilot.com/paper-list/corl-paper-list/corl-2025-paper-list/"},{"title":"What Drives Paper Acceptance? A Process-Centric Analysis of Modern Peer Review","url":"https://arxiv.org/pdf/2509.25701"},{"title":"CoRL 2025","url":"https://2025.corl.org/"},{"title":"Which Coauthor Should I Nominate in My 99 ICLR Submissions? A Mathematical Analysis of the ICLR 2026 Reciprocal Reviewer Nomination Policy","url":"https://arxiv.org/pdf/2512.17950"},{"title":"CoRL 2026 - Instruction for Authors","url":"https://www.corl.org/contributions/instruction-for-authors"},{"title":"CoRL 2026 - Call for Papers","url":"https://www.corl.org/contributions/call-for-papers"},{"title":"CoRL 2025 Demos | OpenReview","url":"https://openreview.net/group?id=robot-learning.org%2FCoRL%2F2025%2FDemos"}]

I found some information about CoRL 2026, but I need to search more specifically for the reviewer form and scoring criteria. Let me do another search.

Links: [{"title":"Reviewer Guidelines","url":"https://virtual.aistats.org/Conferences/2026/ReviewerGuidelines"},{"title":"2026 Reviewer Guidelines","url":"https://neurips.cc/Conferences/2026/ReviewerGuidelines"},{"title":"Review Form","url":"http://aclrollingreview.org/reviewform"},{"title":"ICLR 2026 Reviewer Guide","url":"https://iclr.cc/Conferences/2026/ReviewerGuide"},{"title":"CoRL 2026 - Instruction for Authors","url":"https://www.corl.org/contributions/instruction-for-authors"},{"title":"Insights from the ICLR Peer Review and Rebuttal Process","url":"https://arxiv.org/pdf/2511.15462"},{"title":"CoRL 2026 - Call for Papers","url":"https://www.corl.org/contributions/call-for-papers"},{"title":"CoRL 2024 - Instruction for Reviews","url":"https://2024.corl.org/contributions/instruction-for-reviews"}]

Let me search more specifically for CoRL 2026 re
…[truncated 4768 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 19205
}
```

</details>

---


### Tool call

_source line 110 · 2026-05-19T01:14:38.381520+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://www.corl2023.org/reviewer-guidelines",
  "prompt": "Extract the complete review form criteria, scoring dimensions, and their rating scales. List all dimensions like originality, quality, clarity, significance, with their specific score ranges (e.g., 1-5, 1-10)."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://www.corl2023.org/reviewer-guidelines",
    "prompt": "Extract the complete review form criteria, scoring dimensions, and their rating scales. List all dimensions like originality, quality, clarity, significance, with their specific score ranges (e.g., 1-5, 1-10)."
  }
}
```

</details>

---


### Tool call

_source line 111 · 2026-05-19T01:14:39.739984+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://www.corl.org/contributions/call-for-papers",
  "prompt": "Extract all submission requirements, page limits, formatting rules, Limitations section requirements, anonymity requirements, and any review criteria mentioned for CoRL 2026."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://www.corl.org/contributions/call-for-papers",
    "prompt": "Extract all submission requirements, page limits, formatting rules, Limitations section requirements, anonymity requirements, and any review criteria mentioned for CoRL 2026."
  }
}
```

</details>

---


### Tool call

_source line 112 · 2026-05-19T01:14:40.091451+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Compressor-VLA instruction-guided visual token compression robotic manipulation 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Compressor-VLA instruction-guided visual token compression robotic manipulation 2025"
  }
}
```

</details>

---


### Tool call

_source line 113 · 2026-05-19T01:14:42.456258+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "—|–",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper",
  "output_mode": "content",
  "glob": "*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Grep",
  "tool_args": {
    "pattern": "—|–",
    "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper",
    "output_mode": "content",
    "glob": "*.tex"
  }
}
```

</details>

---


### Tool result

_source line 114 · 2026-05-19T01:14:42.506960+00:00_

/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/experiments_deprecated.tex:1:% experiments.tex — Section 4: Main Results

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Grep",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 115 · 2026-05-19T01:14:43.010224+00:00_

# CoRL 2023 Review Criteria

Based on the provided guidelines, the review form evaluates submissions across **six dimensions**:

1. **Originality** - Assesses novelty of problems/methods and differentiation from prior work
2. **Quality** - Evaluates technical soundness, claim support, and methodological appropriateness
3. **Clarity** - Judges writing quality, organization, and reproducibility information
4. **Significance** - Measures impact potential and advancement of the field
5. **Relevance** - Determines alignment with robot learning focus and audience interest
6. **Limitations** - Reviews quality of authors' self-assessment of work constraints

## Important Note on Scoring

The provided document does **not specify numerical rating scales** (such as 1-5 or 1-10) for these dimensions. The guidelines describe what each criterion should evaluate but omit the concrete scoring ranges reviewers should use. Reviewers are directed to OpenReview via email for "technical instructions," suggesting the actual scoring system resides in that platform rather than in this published guidance document.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 4628
}
```

</details>

---


### Tool result

_source line 116 · 2026-05-19T01:14:43.362091+00:00_

# CoRL 2026 Submission Requirements

Based on the Call for Papers page, here are the specified requirements:

## Core Requirements
The page states submissions should "focus on a core robotics problem and demonstrate the relevance of proposed models, algorithms, datasets, and benchmarks to robotics."

## Limitations Section
Submissions must include a section that "explicitly describing limiting assumptions, failure modes, and other limitations of the results and experiments and how these might be addressed in the future."

## Experimental Evidence
Authors are "encouraged to report real-robot experiments or provide convincing evidence that simulation experiments are transferable to real robots."

## Supplementary Materials
The conference welcomes authors to "submit video, code and data as supplementary materials."

## Important Note
The page specifies that "Submissions without a robotics focus will be returned without review."

---

**Limitation of this response:** The provided web content does not include specific information about page limits, detailed formatting rules, anonymity requirements, or explicit review criteria. For these details, the page directs readers to consult the "[Instruction for Authors](/contributions/instruction-for-authors)" section, which is not included in the provided content.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 3622
}
```

</details>

---


### Tool result

_source line 117 · 2026-05-19T01:14:45.875666+00:00_

Web search results for query: "Compressor-VLA instruction-guided visual token compression robotic manipulation 2025"

Links: [{"title":"Compressor-VLA: Instruction-Guided Visual Token Compression for Efficient Robotic Manipulation","url":"https://arxiv.org/html/2511.18950v1"},{"title":"Compressor-VLA: Instruction-Guided Visual Token Compression for Efficient Robotic Manipulation","url":"https://arxiv.org/pdf/2511.18950"},{"title":"[2511.18950] Compressor-VLA: Instruction-Guided Visual Token Compression for Efficient Robotic Manipulation","url":"https://arxiv.org/abs/2511.18950"},{"title":"Compressor-VLA: Instruction-Guided Visual Token Compression for Efficient Robotic Manipulation","url":"https://chatpaper.com/paper/212383"},{"title":"Visual Resolution Compressor (VRC)","url":"https://www.emergentmind.com/topics/visual-resolution-compressor-vrc"}]

Based on the search results, here's what I found about Compressor-VLA:

## Overview

Compressor-VLA is a framework developed by researchers at Beijing University of Technology and LiAuto Inc. that addresses the computational overhead of processing redundant visual tokens in Vision-Language-Action (VLA) models, which remains a critical bottleneck for real-time robotic deployment.

## Key Features

The framework is a novel hybrid instruction-conditioned token compression approach that consists of two modules: a Semantic Task Compressor (STC) that distills holistic, task-relevant context, and a Spatial Refinement Compressor (SRC) that preserves fine-grained spatial details.

The compression is dynamically modulated by natural language instructions, allowing for adaptive condensation of task-relevant visual information.

## Performance Results

Experimentally, Compressor-VLA achieves competitive success rates on the LIBERO benchmark while reducing FLOPs by 59% and visual token count by over 3x compared to its baseline.

The real-robot deployments on a dual-arm robot platform validate the model's sim-to-real transferability a
…[truncated 310 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 5784
}
```

</details>

---


### Tool call

_source line 118 · 2026-05-19T01:14:51.928862+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "ing,|ing\\.|Furthermore|Moreover|Additionally|delve|leverage|utilize|facilitate|paradigm|novel ",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper",
  "output_mode": "content",
  "glob": "*.tex",
  "-n": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Grep",
  "tool_args": {
    "pattern": "ing,|ing\\.|Furthermore|Moreover|Additionally|delve|leverage|utilize|facilitate|paradigm|novel ",
    "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper",
    "output_mode": "content",
    "glob": "*.tex",
    "-n": "True"
  }
}
```

</details>

---


### Tool result

_source line 119 · 2026-05-19T01:14:52.835061+00:00_

/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/analysis.tex:7:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/analysis.tex:28:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/analysis.tex:38:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/related_work.tex:8:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/main.tex:19:\keywords{vision-language-action models, token pruning, robot learning}
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/discussion.tex:11:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/discussion.tex:13:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/discussion.tex:20:A recurring finding throughout our experiments is the disconnect between offline evaluation metrics and closed-loop performance. During ACIS scorer training, the importance margin loss converges normally, and per-step action prediction errors under pruning remain moderate in offline evaluation. These offline signals would suggest that pruning causes a manageable degradation in action quality. The closed-loop reality is the opposite: 0\% success rate across all conditions.
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/discussion.tex:29:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/discussion.tex:45:[Omitted long matching line]
/home/ubuntu/.agent-ml-research
…[truncated 10073 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Grep",
  "elapsed_ms": 906
}
```

</details>

---


### Tool call

_source line 120 · 2026-05-19T01:14:52.835569+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"DiffPruner\" OR \"differentiable token pruning\" VLA vision-language-action 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"DiffPruner\" OR \"differentiable token pruning\" VLA vision-language-action 2025 2026"
  }
}
```

</details>

---


### Tool call

_source line 121 · 2026-05-19T01:14:54.146004+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://www.corl.org/contributions/instruction-for-authors",
  "prompt": "Extract all formatting requirements: page limit, anonymous/double-blind requirements, line numbers, Limitations section, template details, font/margin rules, supplementary material rules."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://www.corl.org/contributions/instruction-for-authors",
    "prompt": "Extract all formatting requirements: page limit, anonymous/double-blind requirements, line numbers, Limitations section, template details, font/margin rules, supplementary material rules."
  }
}
```

</details>

---


### Tool result

_source line 122 · 2026-05-19T01:14:59.747105+00:00_

Web search results for query: ""DiffPruner" OR "differentiable token pruning" VLA vision-language-action 2025 2026"

Links: [{"title":"The Better You Learn, The Smarter You Prune: Towards Efficient Vision-language-action Models via Differentiable Token Pruning","url":"https://arxiv.org/pdf/2509.12594"},{"title":"The Better You Learn, The Smarter You Prune: Towards Efficient Vision-language-action Models via Differentiable Token Pruning","url":"https://arxiv.org/html/2509.12594v1"},{"title":"VLA-Pruner: Temporal-Aware Dual-Level Visual Token Pruning for Efficient Vision-Language-Action Inference","url":"https://arxiv.org/pdf/2511.16449"},{"title":"The Better You Learn, The Smarter You Prune: Towards Efficient Vision-language-action Models via Differentiable Token Pruning - ADS","url":"https://ui.adsabs.harvard.edu/abs/2025arXiv250912594J/abstract"},{"title":"[2509.12594] The Better You Learn, The Smarter You Prune: Towards Efficient Vision-language-action Models via Differentiable Token Pruning","url":"https://arxiv.org/abs/2509.12594"},{"title":"[2511.16449] VLA-Pruner: Temporal-Aware Dual-Level Visual Token Pruning for Efficient Vision-Language-Action Inference","url":"https://arxiv.org/abs/2511.16449"},{"title":"ICML Poster See What Matters: Differentiable Grid Sample Pruning for Generalizable Vision-Language-Action Model","url":"https://icml.cc/virtual/2026/poster/65010"},{"title":"VLA-Pruner: Temporal-Aware Dual-Level Visual Token Pruning for Efficient Vision-Language-Action Inference","url":"https://arxiv.org/html/2511.16449v1"}]

Based on the search results, I found several recent papers on differentiable token pruning for Vision-Language-Action (VLA) models:

## LightVLA - Differentiable Token Pruning

LightVLA is a differentiable token pruning framework for vision-language-action (VLA) models. VLA models are bottlenecked by heavy attention-based computation over large sets of visual tokens, and LightVLA addresses this through adaptive, performance-driven pru
…[truncated 1064 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 6911
}
```

</details>

---


### Tool result

_source line 123 · 2026-05-19T01:15:00.552408+00:00_

# CoRL 2026 Formatting Requirements

## Page Limits
- **Initial submission:** 8 pages for main paper
- **Camera-ready:** 9 pages for main text
- Acknowledgments, references, and optional appendix do not count toward page limits

## Double-Blind Requirements
Papers must be anonymized for submission. "The accepted papers and reviews will be publicly accessible and de-anonymized after decisions are announced."

## Anonymous/Authorship
- All submissions require anonymization
- Camera-ready versions must include full author names (not anonymous)
- Authors cannot be added/removed after abstract deadline

## Limitations Section
"All submissions should include a Limitations section (counted toward the 8-page limit), explicitly describing limiting assumptions, failure modes, and other limitations."

## Template Details
- Use provided LaTeX template (links provided for both submission and camera-ready versions)
- Camera-ready must use `\usepackage[final]{corl_2026}`

## Font, Margin, Spacing
"Text density, fonts, and spacing should be the same as the provided template" and "The margin should be the same as the provided template."

## Supplementary Materials
- Submit as single zip file through OpenReview
- Video maximum: 250 MB, 3 minutes suggested
- Appendix can be included with main paper or supplement
- Reviewers not required to read appendix

## Line Numbers
No line number requirement specified in provided content.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 6406
}
```

</details>

---


### Tool call

_source line 124 · 2026-05-19T01:15:08.137951+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.pdf",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.pdf",
    "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper"
  }
}
```

</details>

---


### Tool result

_source line 125 · 2026-05-19T01:15:08.589834+00:00_

/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/figures/paper/fig_architecture.pdf
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/figures/paper/fig_compression_curve.pdf
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/figures/paper/fig_pixel_shuffle.pdf
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/figures/paper/fig_entropy_layers.pdf
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/figures/paper/fig_attention_heatmap.pdf
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/figures/paper/fig_action_divergence.pdf
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/figures/paper/fig_cliff_edge.pdf
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/figures/degradation_curve.pdf
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/figures/compression_curve.pdf
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/figures/pixel_shuffle_viz.pdf
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/figures/entropy_comparison.pdf
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/figures/paper/fig_degradation_curve.pdf
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/main.pdf

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Glob",
  "elapsed_ms": 451
}
```

</details>

---


### Tool call

_source line 126 · 2026-05-19T01:15:08.590269+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"See What Matters\" \"Differentiable Grid Sample Pruning\" VLA ICML 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"See What Matters\" \"Differentiable Grid Sample Pruning\" VLA ICML 2026"
  }
}
```

</details>

---


### Tool call

_source line 127 · 2026-05-19T01:15:09.198492+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "SparseVILA \"decoupling visual sparsity\" VLM efficient inference 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "SparseVILA \"decoupling visual sparsity\" VLM efficient inference 2025"
  }
}
```

</details>

---


### Tool result

_source line 128 · 2026-05-19T01:15:14.121912+00:00_

Web search results for query: ""See What Matters" "Differentiable Grid Sample Pruning" VLA ICML 2026"

Links: [{"title":"ICML Poster See What Matters: Differentiable Grid Sample Pruning for Generalizable Vision-Language-Action Model","url":"https://icml.cc/virtual/2026/poster/65010"},{"title":"The Better You Learn, The Smarter You Prune: Towards Efficient Vision-language-action Models via Differentiable Token Pruning","url":"https://arxiv.org/pdf/2509.12594"},{"title":"Don't Run with Scissors: Pruning Breaks VLA Models but They Can Be Recovered","url":"https://arxiv.org/pdf/2510.08464"},{"title":"SpecPrune-VLA: Accelerating Vision-Language-Action Models via Action-Aware Self-Speculative Pruning","url":"https://arxiv.org/pdf/2509.05614"},{"title":"VLA-Pruner: Temporal-Aware Dual-Level Visual Token Pruning for Efficient Vision-Language-Action Inference","url":"https://arxiv.org/pdf/2511.16449"}]

Based on the search results, I found information about your query:

"See What Matters" presents the Differentiable Grid Sampler (GridS), a plug-and-play module that performs task-aware, continuous resampling of visual tokens in VLA. 

The paper addresses the fundamental trade-off in existing token pruning methods: aggressive compression discards critical geometric details like contact points, limiting achievable compression rates. By adaptively predicting a minimal set of salient coordinates and extracting features via differentiable interpolation, GridS achieves drastic compression with fewer than 10% of tokens.

This appears to be an ICML 2026 poster presentation focused on improving the efficiency of Vision-Language-Action (VLA) models for robotic applications while preserving essential spatial information.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 5531
}
```

</details>

---


### Tool result

_source line 129 · 2026-05-19T01:15:16.947281+00:00_

Web search results for query: "SparseVILA "decoupling visual sparsity" VLM efficient inference 2025"

Links: [{"title":"2025-10-21 SparseVILA: Decoupling Visual Sparsity for Efficient VLM Inference","url":"https://arxiv.org/pdf/2510.17777"},{"title":"[2510.17777] SparseVILA: Decoupling Visual Sparsity for Efficient VLM Inference","url":"https://arxiv.org/abs/2510.17777"},{"title":"SparseVILA: Decoupling Visual Sparsity for Efficient VLM Inference","url":"https://arxiv.org/html/2510.17777v1"},{"title":"[Literature Review] SparseVILA: Decoupling Visual Sparsity for Efficient VLM Inference","url":"https://www.themoonlight.io/en/review/sparsevila-decoupling-visual-sparsity-for-efficient-vlm-inference"},{"title":"SparseVILA-R1: Decoupling Visual Sparsity for Efficient VLM Reasoning","url":"https://openreview.net/pdf/6597aa03e44118e07d8bbbe91433da250c6beb33.pdf"},{"title":"ICCV Poster SparseVILA: Decoupling Visual Sparsity for Efficient VLM Inference","url":"https://iccv.thecvf.com/virtual/2025/poster/1739"},{"title":"Zhijian Liu","url":"https://zhijianliu.com/"}]

Based on the search results, here's what I found about SparseVILA:

## Overview

SparseVILA is a new paradigm for efficient VLM inference that decouples visual sparsity across the prefilling and decoding stages, distributing sparsity across stages by pruning redundant visual tokens during prefill and retrieving only query-relevant tokens during decoding.

## Key Innovation

The decoupled design is motivated by the observation that visual tokens exhibit two functional roles: Visual Attention Sinks (tokens that maintain stable activation across queries) and Visual Retrieval Tokens (tokens that vary dynamically with query content). By preserving maximum content in the prefill phase and deferring aggressive, query-aware sparsity to the decoding stage, SparseVILA ensures both persistent sinks and query-dependent retrievals are retained.

## Performance

Built on an AWQ-optimized inference pipeline, SparseVILA achiev
…[truncated 418 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 7748
}
```

</details>

---


### Tool call

_source line 130 · 2026-05-19T01:15:22.537781+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/main.pdf",
  "pages": "1-10",
  "dpi": "200"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/main.pdf",
    "pages": "1-10",
    "dpi": "200"
  }
}
```

</details>

---


### Tool call

_source line 131 · 2026-05-19T01:15:22.793370+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Don't Run with Scissors\" pruning VLA models recovered 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Don't Run with Scissors\" pruning VLA models recovered 2025"
  }
}
```

</details>

---


### Tool result

_source line 132 · 2026-05-19T01:15:25.610287+00:00_

Error: result (5,080,607 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-be-idea-gen-0515-2-projects-importance-margin-vla-compress--claude-sessions-review-reviewer-2-29d69ba3/daed6b8b-72a3-4dad-ae65-1f255c2d5d26/tool-results/mcp-agent-ml-research-pdf_to_images-1779153325296.txt.
Format: JSON with schema: {result: string}
- For targeted queries (find a value, filter by field): use jq on the file directly.
- For analysis or summarization that requires reading the full content: first probe the structure (e.g., jq 'type, length, keys?' /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-be-idea-gen-0515-2-projects-importance-margin-vla-compress--claude-sessions-review-reviewer-2-29d69ba3/daed6b8b-72a3-4dad-ae65-1f255c2d5d26/tool-results/mcp-agent-ml-research-pdf_to_images-1779153325296.txt), then extract slices with jq or python — Read's line-based offset/limit will not chunk this file.
- If the Agent tool is available, do this inside a subagent so the full output stays out of your main context. Give it the instruction above verbatim, and be explicit about what it must return — e.g. "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-be-idea-gen-0515-2-projects-importance-margin-vla-compress--claude-sessions-review-reviewer-2-29d69ba3/daed6b8b-72a3-4dad-ae65-1f255c2d5d26/tool-results/mcp-agent-ml-research-pdf_to_images-1779153325296.txt is JSON with schema: {result: string}; probe the structure with jq (type/length/keys), then extract and read the content in full with jq or python, then summarize and quote any key findings verbatim." A vague "summarize this" may lose detail.


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 3072
}
```

</details>

---


### Tool result

_source line 133 · 2026-05-19T01:15:29.977246+00:00_

Web search results for query: ""Don't Run with Scissors" pruning VLA models recovered 2025"

Links: [{"title":"[2510.08464] Don't Run with Scissors: Pruning Breaks VLA Models but They Can Be Recovered","url":"https://arxiv.org/abs/2510.08464"},{"title":"Don't Run with Scissors: Pruning Breaks VLA Models but They Can Be Recovered","url":"https://gluestick-vla.github.io/"},{"title":"Don't Run with Scissors: Pruning Breaks VLA Models but They Can Be Recovered","url":"https://arxiv.org/pdf/2510.08464"},{"title":"Don't Run with Scissors: Pruning Breaks VLA Models but They Can Be Recovered | OpenReview","url":"https://openreview.net/forum?id=c8g57pKdXD"},{"title":"RLRC: Reinforcement Learning-based Recovery for Compressed Vision-Language-Action Models","url":"https://arxiv.org/pdf/2506.17639"}]

Based on the search results, I found comprehensive information about this research:

Vision-Language-Action (VLA) models have advanced robotic capabilities but remain challenging to deploy on resource-limited hardware. Pruning has enabled efficient compression of large language models (LLMs), yet it is largely understudied in robotics. Surprisingly, pruning VLA models leads to drastic degradation and increased safety violations.

The researchers introduced GLUESTICK, a post-pruning recovery method that restores much of the original model's functionality while retaining sparsity benefits. The method performs a one-time interpolation between the dense and pruned models in weight-space to compute a corrective term, which is used during inference by each pruned layer to recover lost capabilities with minimal overhead.

GLUESTICK requires no additional training, is agnostic to the pruning algorithm, and introduces a single hyperparameter that controls the tradeoff between efficiency and accuracy. Across diverse VLA architectures and tasks in manipulation and navigation, GLUESTICK achieves competitive memory efficiency while substantially recovering success rates and reducing safety vio
…[truncated 166 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 7183
}
```

</details>

---


### Tool call

_source line 134 · 2026-05-19T01:15:36.460336+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/main.pdf",
  "pages": "1-2",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/main.pdf",
    "pages": "1-2",
    "dpi": "150"
  }
}
```

</details>

---


### Tool call

_source line 135 · 2026-05-19T01:15:36.712498+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "SpecPrune-VLA action-aware self-speculative pruning VLA 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "SpecPrune-VLA action-aware self-speculative pruning VLA 2025"
  }
}
```

</details>

---


### Tool result

_source line 136 · 2026-05-19T01:15:37.226374+00:00_

Error: result (913,024 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-be-idea-gen-0515-2-projects-importance-margin-vla-compress--claude-sessions-review-reviewer-2-29d69ba3/daed6b8b-72a3-4dad-ae65-1f255c2d5d26/tool-results/mcp-agent-ml-research-pdf_to_images-1779153337166.txt.
Format: JSON with schema: {result: string}
- For targeted queries (find a value, filter by field): use jq on the file directly.
- For analysis or summarization that requires reading the full content: first probe the structure (e.g., jq 'type, length, keys?' /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-be-idea-gen-0515-2-projects-importance-margin-vla-compress--claude-sessions-review-reviewer-2-29d69ba3/daed6b8b-72a3-4dad-ae65-1f255c2d5d26/tool-results/mcp-agent-ml-research-pdf_to_images-1779153337166.txt), then extract slices with jq or python — Read's line-based offset/limit will not chunk this file.
- If the Agent tool is available, do this inside a subagent so the full output stays out of your main context. Give it the instruction above verbatim, and be explicit about what it must return — e.g. "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-be-idea-gen-0515-2-projects-importance-margin-vla-compress--claude-sessions-review-reviewer-2-29d69ba3/daed6b8b-72a3-4dad-ae65-1f255c2d5d26/tool-results/mcp-agent-ml-research-pdf_to_images-1779153337166.txt is JSON with schema: {result: string}; probe the structure with jq (type/length/keys), then extract and read the content in full with jq or python, then summarize and quote any key findings verbatim." A vague "summarize this" may lose detail.


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 766
}
```

</details>

---


### Tool result

_source line 137 · 2026-05-19T01:15:43.652040+00:00_

Web search results for query: "SpecPrune-VLA action-aware self-speculative pruning VLA 2025"

Links: [{"title":"[2509.05614] SpecPrune-VLA: Accelerating Vision-Language-Action Models via Action-Aware Self-Speculative Pruning","url":"https://arxiv.org/abs/2509.05614"},{"title":"SpecPrune-VLA: Accelerating Vision-Language-Action Models via Action-Aware Self-Speculative Pruning","url":"https://arxiv.org/html/2509.05614"},{"title":"SpecPrune-VLA: Accelerating Vision-Language-Action Models via Action-Aware","url":"https://arxiv.org/pdf/2509.05614"},{"title":"GitHub - KwanWaiPang/Awesome-VLA: Paper Survey for Visual Language Action · GitHub","url":"https://github.com/KwanWaiPang/Awesome-VLA"},{"title":"Specprune-vla Boosts Vision-Language-Action Models, Avoiding Over 20% Success Rate Drops With Smart Pruning","url":"https://quantumzeitgeist.com/faster-models-performance-specprune-vla-boosts-vision-language-action-avoiding-success/"},{"title":"SpecPrune-VLA: Accelerating Vision-Language-Action Models via Action-Aware Self-Speculative Pruning | Request PDF","url":"https://www.researchgate.net/publication/395354566_SpecPrune-VLA_Accelerating_Vision-Language-Action_Models_via_Action-Aware_Self-Speculative_Pruning"},{"title":"Environment-Aware Adaptive Pruning with Interleaved Inference Orchestration for Vision-Language-Action Models","url":"https://arxiv.org/html/2602.00780"},{"title":"SpecPrune-VLA: Accelerating Vision-Language-Action Models via Action-Aware Self-Speculative Pruning | OpenReview","url":"https://openreview.net/forum?id=t85Ni0LwjC"}]

I found comprehensive information about SpecPrune-VLA. Here's what the research shows:

## Overview

SpecPrune-VLA is an acceleration method for Vision-Language-Action Models through action-aware self-speculative pruning. The method leverages spatial-temporal consistency in VLA tasks: input images in consecutive steps exhibit high similarity, and token selection combines local information with global context of the model.

## Key
…[truncated 922 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 6939
}
```

</details>

---


### Tool call

_source line 138 · 2026-05-19T01:15:52.234951+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

```json
{
  "description": "PDF visual page review",
  "prompt": "I need you to visually inspect the rendered PDF pages of a research paper. The images are saved in a JSON file.\n\nThe file is at: /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-be-idea-gen-0515-2-projects-importance-margin-vla-compress--claude-sessions-review-reviewer-2-29d69ba3/daed6b8b-72a3-4dad-ae65-1f255c2d5d26/tool-results/mcp-agent-ml-research-pdf_to_images-1779153337166.txt\n\nThis is JSON with schema: {result: string}. The result field is itself a JSON string containing page image data.\n\n1. First probe the structure with jq (type/length/keys)\n2. Parse and extract the image data\n3. Read the actual rendered page images\n\nReport specifically:\n- How many total pages does the paper have?\n- Does page 1 show proper anonymous formatting (no author names)?\n- Are line numbers visible?\n- What is the font size and general layout quality?\n- Any obvious formatting issues on pages 1-2?\n\nKeep your report under 200 words.",
  "subagent_type": "general-purpose"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Agent",
  "tool_args": {
    "description": "PDF visual page review",
    "prompt": "I need you to visually inspect the rendered PDF pages of a research paper. The images are saved in a JSON file.\n\nThe file is at: /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-be-idea-gen-0515-2-projects-importance-margin-vla-compress--claude-sessions-review-reviewer-2-29d69ba3/daed6b8b-72a3-4dad-ae65-1f255c2d5d26/tool-results/mcp-agent-ml-research-pdf_to_images-1779153337166.txt\n\nThis is JSON with schema: {result: string}. The result field is itself a JSON string containing page image data.\n\n1. First probe the structure with jq (type/length/keys)\n2. Parse and extract the image data\n3. Read the actual rendered page images\n\nReport specifically:\n- How many total pages does the paper have?\n- Does page 1 show proper anonymous formatting (no author names)?\n- Are line numbers visible?\n- What is the font size and general layout quality?\n- Any obvious formatting issues on pages 1-2?\n\nKeep your report under 200 words.",
    "subagent_type": "general-purpose"
  }
}
```

</details>

---


### Tool call

_source line 139 · 2026-05-19T01:15:57.877973+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-be-idea-gen-0515-2-projects-importance-margin-vla-compress--claude-sessions-review-reviewer-2-29d69ba3/daed6b8b-72a3-4dad-ae65-1f255c2d5d26/tool-results/mcp-agent-ml-research-pdf_to_images-1779153337166.txt | python3 -c \"import json,sys; d=json.load(sys.stdin); r=json.loads(d['result']); print(type(r).__name__, len(r) if isinstance(r,list) else 'not list'); print(r[0].keys() if isinstance(r,list) else list(r.keys())[:5])\"",
  "description": "Probe JSON structure of PDF images file"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-be-idea-gen-0515-2-projects-importance-margin-vla-compress--claude-sessions-review-reviewer-2-29d69ba3/daed6b8b-72a3-4dad-ae65-1f255c2d5d26/tool-results/mcp-agent-ml-research-pdf_to_images-1779153337166.txt | python3 -c \"import json,sys; d=json.load(sys.stdin); r=json.loads(d['result']); print(type(r).__name__, len(r) if isinstance(r,list) else 'not list'); print(r[0].keys() if isinstance(r,list) else list(r.keys())[:5])\"",
    "description": "Probe JSON structure of PDF images file"
  }
}
```

</details>

---


### Tool result

_source line 140 · 2026-05-19T01:15:57.878368+00:00_

dict not list
['success', 'data', 'error', 'metadata']

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 141 · 2026-05-19T01:15:58.029435+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

````json
{
  "description": "Full PDF page count check",
  "prompt": "I need to determine the total number of pages in a PDF file and specifically how many pages make up the main body vs appendix.\n\nThe PDF is at: /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/main.pdf\n\nRun this command to get the page count:\n```bash\npython3 -c \"\nimport fitz\ndoc = fitz.open('/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/main.pdf')\nprint(f'Total pages: {doc.page_count}')\nfor i, page in enumerate(doc):\n    text = page.get_text()\n    # Check for appendix markers\n    if 'Appendix' in text or 'appendix' in text:\n        first_lines = text[:200]\n        print(f'Page {i+1} contains appendix marker. First 200 chars: {first_lines}')\n    # Check for References\n    if 'References' in text and i > 3:\n        print(f'Page {i+1} contains References section')\ndoc.close()\n\"\n```\n\nIf fitz (PyMuPDF) is not available, try: `pdfinfo /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/main.pdf | grep Pages`\n\nReport: total pages, which page References start on, which page Appendix starts on. Under 100 words.",
  "subagent_type": "general-purpose"
}
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Agent",
  "tool_args": {
    "description": "Full PDF page count check",
    "prompt": "I need to determine the total number of pages in a PDF file and specifically how many pages make up the main body vs appendix.\n\nThe PDF is at: /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/main.pdf\n\nRun this command to get the page count:\n```bash\npython3 -c \"\nimport fitz\ndoc = fitz.open('/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/main.pdf')\nprint(f'Total pages: {doc.page_count}')\nfor i, page in enumerate(doc):\n    text = page.get_text()\n    # Check for appendix markers\n    if 'Appendix' in text or 'appendix' in text:\n        first_lines = text[:200]\n        print(f'Page {i+1} contains appendix marker. First 200 chars: {first_lines}')\n    # Check for References\n    if 'References' in text and i > 3:\n        print(f'Page {i+1} contains References section')\ndoc.close()\n\"\n```\n\nIf fitz (PyMuPDF) is not available, try: `pdfinfo /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/main.pdf | grep Pages`\n\nReport: total pages, which page References start on, which page Appendix starts on. Under 100 words.",
    "subagent_type": "general-purpose"
  }
}
````

</details>

---


### Tool call

_source line 142 · 2026-05-19T01:16:03.654374+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-be-idea-gen-0515-2-projects-importance-margin-vla-compress--claude-sessions-review-reviewer-2-29d69ba3/daed6b8b-72a3-4dad-ae65-1f255c2d5d26/tool-results/mcp-agent-ml-research-pdf_to_images-1779153337166.txt | python3 -c \"\nimport json,sys\nd=json.load(sys.stdin)\nr=json.loads(d['result'])\nprint('success:', r['success'])\nprint('metadata:', r.get('metadata'))\ndata = r['data']\nprint('data type:', type(data).__name__)\nif isinstance(data, list):\n    print('num pages:', len(data))\n    for i,p in enumerate(data):\n        if isinstance(p, dict):\n            print(f'page {i}: keys={list(p.keys())}, val_lens={{ k: len(str(v))[:50] for k,v in p.items() }}')\n        else:\n            print(f'page {i}: type={type(p).__name__}, len={len(str(p))}')\nelif isinstance(data, dict):\n    print('keys:', list(data.keys())[:10])\n\"",
  "description": "Examine data structure of PDF images"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-be-idea-gen-0515-2-projects-importance-margin-vla-compress--claude-sessions-review-reviewer-2-29d69ba3/daed6b8b-72a3-4dad-ae65-1f255c2d5d26/tool-results/mcp-agent-ml-research-pdf_to_images-1779153337166.txt | python3 -c \"\nimport json,sys\nd=json.load(sys.stdin)\nr=json.loads(d['result'])\nprint('success:', r['success'])\nprint('metadata:', r.get('metadata'))\ndata = r['data']\nprint('data type:', type(data).__name__)\nif isinstance(data, list):\n    print('num pages:', len(data))\n    for i,p in enumerate(data):\n        if isinstance(p, dict):\n            print(f'page {i}: keys={list(p.keys())}, val_lens={{ k: len(str(v))[:50] for k,v in p.items() }}')\n        else:\n            print(f'page {i}: type={type(p).__name__}, len={len(str(p))}')\nelif isinstance(data, dict):\n    print('keys:', list(data.keys())[:10])\n\"",
    "description": "Examine data structure of PDF images"
  }
}
```

</details>

---


### Tool result

_source line 143 · 2026-05-19T01:16:03.806298+00:00_

success: True
metadata: {}
data type: dict
keys: ['images', 'total_pages', 'rendered_pages', 'dpi', 'output_dir']

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Bash",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 144 · 2026-05-19T01:16:13.296266+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-be-idea-gen-0515-2-projects-importance-margin-vla-compress--claude-sessions-review-reviewer-2-29d69ba3/daed6b8b-72a3-4dad-ae65-1f255c2d5d26/tool-results/mcp-agent-ml-research-pdf_to_images-1779153337166.txt | python3 -c \"\nimport json,sys\nd=json.load(sys.stdin)\nr=json.loads(d['result'])\ndata = r['data']\nprint('total_pages:', data['total_pages'])\nprint('rendered_pages:', data['rendered_pages'])\nprint('dpi:', data['dpi'])\nprint('output_dir:', data['output_dir'])\nimgs = data['images']\nprint('images type:', type(imgs).__name__, 'len:', len(imgs) if isinstance(imgs,list) else 'N/A')\nif isinstance(imgs, list):\n    for i,img in enumerate(imgs[:3]):\n        print(f'  img[{i}]: type={type(img).__name__}', end='')\n        if isinstance(img, dict):\n            print(f' keys={list(img.keys())}')\n        elif isinstance(img, str):\n            print(f' len={len(img)} prefix={img[:80]}')\n\"",
  "description": "Get page count and image paths"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-be-idea-gen-0515-2-projects-importance-margin-vla-compress--claude-sessions-review-reviewer-2-29d69ba3/daed6b8b-72a3-4dad-ae65-1f255c2d5d26/tool-results/mcp-agent-ml-research-pdf_to_images-1779153337166.txt | python3 -c \"\nimport json,sys\nd=json.load(sys.stdin)\nr=json.loads(d['result'])\ndata = r['data']\nprint('total_pages:', data['total_pages'])\nprint('rendered_pages:', data['rendered_pages'])\nprint('dpi:', data['dpi'])\nprint('output_dir:', data['output_dir'])\nimgs = data['images']\nprint('images type:', type(imgs).__name__, 'len:', len(imgs) if isinstance(imgs,list) else 'N/A')\nif isinstance(imgs, list):\n    for i,img in enumerate(imgs[:3]):\n        print(f'  img[{i}]: type={type(img).__name__}', end='')\n        if isinstance(img, dict):\n            print(f' keys={list(img.keys())}')\n        elif isinstance(img, str):\n            print(f' len={len(img)} prefix={img[:80]}')\n\"",
    "description": "Get page count and image paths"
  }
}
```

</details>

---


### Tool result

_source line 145 · 2026-05-19T01:16:13.398087+00:00_

total_pages: 15
rendered_pages: 2
dpi: 150
output_dir: /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/_pdf_images
images type: list len: 2
  img[0]: type=dict keys=['page', 'path', 'base64', 'width', 'height', 'size_kb']
  img[1]: type=dict keys=['page', 'path', 'base64', 'width', 'height', 'size_kb']

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Bash",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 146 · 2026-05-19T01:16:13.799862+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\nimport fitz\ndoc = fitz.open('/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/main.pdf')\nprint(f'Total pages: {doc.page_count}')\nfor i, page in enumerate(doc):\n    text = page.get_text()\n    if 'Appendix' in text or 'appendix' in text:\n        first_lines = text[:200]\n        print(f'Page {i+1} contains appendix marker. First 200 chars: {first_lines}')\n    if 'References' in text and i > 3:\n        print(f'Page {i+1} contains References section')\ndoc.close()\n\" 2>/dev/null || pdfinfo /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/main.pdf | grep Pages",
  "description": "Count PDF pages and find References/Appendix locations"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"\nimport fitz\ndoc = fitz.open('/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/main.pdf')\nprint(f'Total pages: {doc.page_count}')\nfor i, page in enumerate(doc):\n    text = page.get_text()\n    if 'Appendix' in text or 'appendix' in text:\n        first_lines = text[:200]\n        print(f'Page {i+1} contains appendix marker. First 200 chars: {first_lines}')\n    if 'References' in text and i > 3:\n        print(f'Page {i+1} contains References section')\ndoc.close()\n\" 2>/dev/null || pdfinfo /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/main.pdf | grep Pages",
    "description": "Count PDF pages and find References/Appendix locations"
  }
}
```

</details>

---


### Tool result

_source line 147 · 2026-05-19T01:16:14.201723+00:00_

Total pages: 15
Page 4 contains appendix marker. First 200 chars: Table 1: SmolVLA pruning ablation on LIBERO-Object. All configurations collapse to 0% SR. The
official checkpoint (59.2% baseline) shows the same cliff-edge.
Scoring
k
Mechanism
SR (%)
Episodes
Wilson
Page 5 contains appendix marker. First 200 chars: pattern is not task-specific. A geometric prior (Sobel edge scoring) at k ∈{0.50, 0.70, 0.90} also
132
produces 0% SR.2
133
4.2
OpenVLA: Graceful Degradation
134
Under random token removal, OpenVLA de
Page 6 contains appendix marker. First 200 chars: Table 2: Smart Compress on LIBERO-Object. Performance is flat across M ∈{32, 64, 128} (∼60%
SR), showing the gain comes from re-encoding, not compression. M=16 shows modest decline at
extreme compress
Page 7 contains appendix marker. First 200 chars: figpixelshuffle
(placeholder)
Figure 3: Pixel-shuffle folding: each 4×4 block of SigLIP patches is channel-concatenated into one
token. Removing any token eliminates its receptive field (gray) with no
Page 8 contains appendix marker. First 200 chars: Figure 5: Per-Layer Entropy Ratio
SmolVLA (flat) vs OpenVLA (progressive sharpening)
Figure 4: Per-layer attention entropy ratio. SmolVLA (16 layers): range 0.93–0.98. OpenVLA
(32 layers): progressive
Page 9 contains References section

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Bash",
  "elapsed_ms": 401
}
```

</details>

---


### Tool call

_source line 148 · 2026-05-19T01:16:18.770496+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-be-idea-gen-0515-2-projects-importance-margin-vla-compress--claude-sessions-review-reviewer-2-29d69ba3/daed6b8b-72a3-4dad-ae65-1f255c2d5d26/tool-results/mcp-agent-ml-research-pdf_to_images-1779153337166.txt | python3 -c \"\nimport json,sys\nd=json.load(sys.stdin)\nr=json.loads(d['result'])\ndata = r['data']\nfor img in data['images']:\n    print(f\\\"page={img['page']} path={img['path']} w={img['width']} h={img['height']} size_kb={img['size_kb']}\\\")\n\"",
  "description": "Get image metadata for each page"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-be-idea-gen-0515-2-projects-importance-margin-vla-compress--claude-sessions-review-reviewer-2-29d69ba3/daed6b8b-72a3-4dad-ae65-1f255c2d5d26/tool-results/mcp-agent-ml-research-pdf_to_images-1779153337166.txt | python3 -c \"\nimport json,sys\nd=json.load(sys.stdin)\nr=json.loads(d['result'])\ndata = r['data']\nfor img in data['images']:\n    print(f\\\"page={img['page']} path={img['path']} w={img['width']} h={img['height']} size_kb={img['size_kb']}\\\")\n\"",
    "description": "Get image metadata for each page"
  }
}
```

</details>

---


### Tool result

_source line 149 · 2026-05-19T01:16:18.821113+00:00_

page=1 path=/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/_pdf_images/main_p1.png w=1275 h=1650 size_kb=297.9
page=2 path=/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/_pdf_images/main_p2.png w=1275 h=1650 size_kb=370.3

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 150 · 2026-05-19T01:16:19.122778+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\nimport fitz\ndoc = fitz.open('/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/main.pdf')\n# Check page 9 more carefully for References start\nfor i in [8, 9, 10, 11, 12, 13, 14]:\n    if i < doc.page_count:\n        text = doc[i].get_text()\n        lines = text.strip().split('\\n')\n        for j, line in enumerate(lines[:10]):\n            print(f'Page {i+1}, line {j}: {line.strip()[:80]}')\n        print('---')\ndoc.close()\n\"",
  "description": "Check page content near References and end of document"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"\nimport fitz\ndoc = fitz.open('/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/main.pdf')\n# Check page 9 more carefully for References start\nfor i in [8, 9, 10, 11, 12, 13, 14]:\n    if i < doc.page_count:\n        text = doc[i].get_text()\n        lines = text.strip().split('\\n')\n        for j, line in enumerate(lines[:10]):\n            print(f'Page {i+1}, line {j}: {line.strip()[:80]}')\n        print('---')\ndoc.close()\n\"",
    "description": "Check page content near References and end of document"
  }
}
```

</details>

---


### Tool result

_source line 151 · 2026-05-19T01:16:19.475313+00:00_

Page 9, line 0: References
Page 9, line 1: 237
Page 9, line 2: [1] Y. Rao, W. Zhao, B. Liu, J. Lu, J. Zhou, and C.-J. Hsieh. DynamicViT: Effici
Page 9, line 3: 238
Page 9, line 4: formers with dynamic token sparsification. In Advances in Neural Information Pro
Page 9, line 5: 239
Page 9, line 6: Systems (NeurIPS), 2021.
Page 9, line 7: 240
Page 9, line 8: [2] D. Bolya, C.-Y. Fu, X. Dai, P. Zhang, C. Feichtenhofer, and J. Hoffman. Toke
Page 9, line 9: 241
---
Page 10, line 0: [18] J.-B. Alayrac, J. Donahue, P. Luc, et al. Flamingo: a visual language model
Page 10, line 1: 280
Page 10, line 2: learning. In Advances in Neural Information Processing Systems (NeurIPS), 2022.
Page 10, line 3: 281
Page 10, line 4: [19] A. Jaegle, F. Gimeno, A. Brock, A. Zisserman, O. Vinyals, and J. Carreira. 
Page 10, line 5: 282
Page 10, line 6: perception with iterative attention. In International Conference on Machine Lear
Page 10, line 7: 283
Page 10, line 8: 2021.
Page 10, line 9: 284
---
Page 11, line 0: A.2
Page 11, line 1: Official SmolVLA Checkpoint Per-Task Results
Page 11, line 2: 307
Page 11, line 3: Table 4 reports per-task success rates for the official SmolVLA LIBERO checkpoin
Page 11, line 4: 308
Page 11, line 5: FaceVLA/smolvla libero). Under 50% random token removal, all tasks produce 0% SR
Page 11, line 6: 309
Page 11, line 7: to the fine-tuned checkpoint results.
Page 11, line 8: 310
Page 11, line 9: Table 4: Official SmolVLA checkpoint per-task success rates on LIBERO-Object (50
---
Page 12, line 0: A.5
Page 12, line 1: Smart Compress Per-Task Comparison
Page 12, line 2: 313
Page 12, line 3: Table 7: Smart Compress per-task success rates on LIBERO-Object for M ∈{32, 64, 
Page 12, line 4: three achieve similar overall SR (59.8%–61.6%), but individual task performance 
Page 12, line 5: tially across configurations, with per-task differences up to 30 percentage poin
Page 12, line 6: Task
Page 12, line 7: M=32 (%)
Page 12, line 8: M=64 (%)
Page 12, line 9: M=128 (%)
---
P
…[truncated 1413 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Bash",
  "elapsed_ms": 352
}
```

</details>

---


### Tool call

_source line 152 · 2026-05-19T01:16:22.153029+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/_pdf_images/main_p1.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/_pdf_images/main_p1.png"
  }
}
```

</details>

---


### Tool result

_source line 153 · 2026-05-19T01:16:22.658475+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 505
}
```

</details>

---


### Tool call

_source line 154 · 2026-05-19T01:16:22.709312+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/_pdf_images/main_p2.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/_pdf_images/main_p2.png"
  }
}
```

</details>

---


### Tool result

_source line 155 · 2026-05-19T01:16:23.112398+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 403
}
```

</details>

---


### Tool result

_source line 156 · 2026-05-19T01:16:27.982265+00:00_

Results:

- **Total pages**: 15
- **Main body**: pages 1-8 (8 pages)
- **References**: starts on page 9, spans pages 9-10 (2 pages)
- **Appendix**: starts on page 11, spans pages 11-15 (5 pages)

Note: the word "appendix" appears in the body text as early as page 4 (cross-references to appendix content), but the actual Appendix section begins on page 11 (section A.2 is the first visible appendix heading).
agentId: a3a48c94bac6a2685 (use SendMessage with to: 'a3a48c94bac6a2685' to continue this agent)
&lt;usage>total_tokens: 21600
tool_uses: 2
duration_ms: 29936&lt;/usage>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Agent",
  "elapsed_ms": 29952
}
```

</details>

---


### Tool result

_source line 157 · 2026-05-19T01:16:35.921640+00:00_

Here is the visual inspection report:

**Total pages**: 15 (only pages 1-2 were rendered).

**Anonymous formatting**: Page 1 shows "Anonymous Author(s)" with "Affiliation", "Address", "email" as placeholders. Anonymization is correct.

**Line numbers**: Not visible on either page. This is a potential formatting issue for review submission, as many venues require line numbers during review.

**Font size and layout**: Standard two-column conference format (appears to be ICLR or similar). Title font is appropriately sized. Body text is standard 10pt. Margins and column spacing look normal. The aspect ratio (1275x1650 at 150 DPI, ~8.5x11in) is correct US Letter.

**Page 1 issues**: The abstract is dense but fits within the page. Keywords line is present. Section 1 (Introduction) begins on page 1. No obvious overflow or spacing problems.

**Page 2 issues**: Continues with the introduction and begins Section 2 (Related Work). Text is well-formatted with proper paragraph spacing. Subsections under Related Work (2.1 VLA-specific token reduction, 2.2 Vision connectors) are clearly delineated. No visual artifacts, overlapping text, or broken formatting detected.

**Key concern**: Absence of line numbers. If the target venue requires them for review, this needs fixing.
agentId: a7bee692df114c5b1 (use SendMessage with to: 'a7bee692df114c5b1' to continue this agent)
&lt;usage>total_tokens: 21715
tool_uses: 6
duration_ms: 43692&lt;/usage>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Agent",
  "elapsed_ms": 43686
}
```

</details>

---


### Tool call

_source line 158 · 2026-05-19T01:16:42.500275+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/corl_2026.sty",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/corl_2026.sty",
    "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper"
  }
}
```

</details>

---


### Tool result

_source line 159 · 2026-05-19T01:16:42.601046+00:00_

/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/corl_2026.sty

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Glob",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 160 · 2026-05-19T01:16:43.354616+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "linenumbers|lineno",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Grep",
  "tool_args": {
    "pattern": "linenumbers|lineno",
    "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper",
    "output_mode": "content"
  }
}
```

</details>

---


### Tool result

_source line 161 · 2026-05-19T01:16:43.405362+00:00_

/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/main.fls:15:INPUT /usr/share/texlive/texmf-dist/tex/latex/lineno/lineno.sty
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/main.fls:16:INPUT /usr/share/texlive/texmf-dist/tex/latex/lineno/lineno.sty
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/main.log:29:(/usr/share/texlive/texmf-dist/tex/latex/lineno/lineno.sty
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/main.log:30:Package: lineno 2025/05/13 line numbers on paragraphs v5.5
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/main.log:49:\linenopenalty=\count284
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/main.log:51:\linenoprevgraf=\count285
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/main.log:52:\linenumbersep=\dimen149
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/main.log:58:\c@internallinenumbers=\count290
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/main.log:59:\quotelinenumbersep=\dimen151
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/main.fdb_latexmk:111:  "/usr/share/texlive/texmf-dist/tex/latex/lineno/lineno.sty" 1747166482 154960 d8c67419d37a002abc40815be8d0ebfb ""
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/corl_2026.sty:73:\RequirePackage{lineno}
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/corl_2026.sty:158:    \linenumbers
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance
…[truncated 655 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Grep",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 162 · 2026-05-19T01:16:49.529867+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/corl_2026.sty",
  "offset": "150",
  "limit": "30"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/corl_2026.sty",
    "offset": "150",
    "limit": "30"
  }
}
```

</details>

---


### Tool result

_source line 163 · 2026-05-19T01:16:49.580574+00:00_

150	      % Nothing here.
151	    }
152	  \else
153	    \newcommand{\@noticestring}{%
154	      Submitted to the \@conferenceordinal\/ Conference on Robot Learning (CoRL \@conferenceyear). Do not distribute.%
155	    }
156	
157	    % line numbers for submission
158	    \linenumbers
159	
160	    % fix incompatibilities between lineno and amsmath, if required, by
161	    % transparently wrapping linenomath environments around amsmath
162	    % environments
163	    \AtBeginDocument{%
164	     \@ifpackageloaded{amsmath}{%
165	        \newcommand*\patchAmsMathEnvironmentForLineno[1]{%
166	          \expandafter\let\csname old#1\expandafter\endcsname\csname #1\endcsname
167	          \expandafter\let\csname oldend#1\expandafter\endcsname\csname end#1\endcsname
168	          \renewenvironment{#1}%
169	            {\linenomath\csname old#1\endcsname}%
170	            {\csname oldend#1\endcsname\endlinenomath}%
171	        }%
172	        \newcommand*\patchBothAmsMathEnvironmentsForLineno[1]{%
173	          \patchAmsMathEnvironmentForLineno{#1}%
174	          \patchAmsMathEnvironmentForLineno{#1*}%
175	        }%
176	        \patchBothAmsMathEnvironmentsForLineno{equation}%
177	        \patchBothAmsMathEnvironmentsForLineno{align}%
178	        \patchBothAmsMathEnvironmentsForLineno{flalign}%
179	        \patchBothAmsMathEnvironmentsForLineno{alignat}%

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 164 · 2026-05-19T01:19:50.200423+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "\n## Reviewer 2 — Round 1 审稿报告\n\n**论文**: \"Why Token Pruning Crashes Some Robot Policies but Not Others: The Role of Vision Connectors in VLA Token Compressibility\"\n**Venue**: CoRL 2026\n**审查侧重**: 新颖性 + Related Work 完整性 + 写作质量 + 格式合规\n\n---\n\n## Summary\n\n本文研究 VLA 模型中 vision token pruning 的跨架构行为差异。核心发现：pixel-shuffle connector（SmolVLA）下 token pruning 导致 cliff-edge failure（59.2% → 0%），而 MLP projector（OpenVLA）graceful degradation（74.0% → 37.4%）。作者用 attention entropy ratio 解释此差异，并提出 cross-attention re-encoding（Smart Compress）模块在 75% token reduction 下保持 61.6% SR。实验在 LIBERO 基准上进行，涵盖多种 pruning 配置。\n\n---\n\n## 总体评分\n\n**Overall**: 5/10 (Borderline — 有价值的实证发现但新颖性和完整性存在显著问题)\n\n**一句话总结**: 经验性发现有意义但偏 expected，Smart Compress 方法创新不足，且遗漏多篇直接相关工作（包括至少 5 篇 2025-2026 VLA efficiency 论文），严重削弱了 positioning 的可信度。\n\n**Confidence**: 4/5 (对 VLA 效率和 token pruning 领域较为熟悉)\n\n---\n\n## 官方维度打分（基于 CoRL review form 维度）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Originality | 2/5 | 核心发现（pixel-shuffle 不可剪枝）从架构设计角度看较为 expected；Smart Compress 本质是 Q-Former/Perceiver 变体 |\n| Quality | 3/5 | 实验设计严谨（多配置消融、置信区间、控制实验），但两模型对比存在 scale confound，遗漏多篇直接竞争方法 |\n| Clarity | 4/5 | 写作清晰直接，叙事线连贯，无明显 AI 写作标志，图表信息密度合理 |\n| Significance | 3/5 | 对 practitioner 有参考价值（选 connector 需考虑压缩性），但实际 actionable guidance 有限 |\n| Relevance | 4/5 | 直接面向机器人学习效率问题，符合 CoRL 受众 |\n| Limitations | 3/5 | 存在且实质性（simulation-only, scale confound, 泛化不足），但未讨论与遗漏工作的关系 |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] 遗漏多篇直接竞争的 VLA token efficiency 工作\n\n- 具体位置：Section 2 (Related Work)，全文 positioning\n- 问题：以下 2025-2026 年论文与本文高度相关但完全未被引用：\n  1. **\"Don't Run with Scissors: Pruning Breaks VLA Models but They Can Be Recovered\"** (arXiv 2510.08464, Oct 2025) — 研究 VLA 模型 pruning 后的性能崩溃和恢复，提出 GLUESTICK 方法。虽然聚焦 weight pruning 而非 token pruning，但核心主题（pruning 破坏 VLA 模型）与本文直接重叠，且在多种 VLA 架构上评估\n  2. **Compressor-VLA** (arXiv 2511.18950, Nov 2025) — 指令引导的视觉 token 压缩框架，包含 cross-attention 压缩（Semantic Task Compressor），在 LIBERO 上评估，与 Smart Compress 方法高度类似\n  3. **SpecPrune-VLA** (arXiv 2509.05614, Sep 2025) — Action-aware self-speculative pruning，在 LIBERO 上实现 1.57x 加速且 SR 几乎不降\n  4. **LightVLA / \"The Better You Learn, The Smarter You Prune\"** (arXiv 2509.12594, Sep 2025) — 可微分 token pruning，59% FLOPs 降低且 SR 提升 2.9%\n  5. **\"See What Matters: Differentiable Grid Sample Pruning for Generalizable VLA Model\"** (ICML 2026) — 可微分 grid sampling 压缩视觉 token，<10% token 保留\n  6. **SparseVLM** (ICLR 2025 / arXiv 2410.04417) — Training-free VLM token 稀疏化\n  7. **SparseVILA** (ICCV 2025 / arXiv 2510.17777) — 解耦视觉稀疏性\n- 为什么影响接收：这些遗漏严重削弱了 \"first cross-architecture closed-loop evaluation\" 的 claim 可信度，也使得 Smart Compress 的 novelty positioning 无法成立——Compressor-VLA 使用了类似的 cross-attention 压缩且在相同 benchmark 上评估。审稿人会立即注意到这一调研缺口。\n- 建议修改方向：全面补充上述引用，重新评估 \"first\" claim 的准确性，明确 Smart Compress 与 Compressor-VLA 的区别\n\n**N2** [critical] Smart Compress 方法新颖性不足，与 Q-Former/Perceiver/Compressor-VLA 区分不清\n\n- 具体位置：Section 3.4 (Smart Compress Setup), Section 5.2 (Why Learned Compression Succeeds)\n- 问题：Smart Compress 的核心是 M 个 learned query vectors 通过 multi-head cross-attention 对 128 source tokens 进行 pooling。这与 BLIP-2 的 Q-Former（32 learned queries cross-attend to image features）和 Perceiver Resampler（latent queries cross-attend to visual tokens）在机制上几乎相同。论文 Related Work (Section 2, \"Vision connectors\" 段落) 虽然提到了 Q-Former 和 Perceiver，但仅作为 vision connector taxonomy 的一部分列出，完全没有讨论 Smart Compress 与这些方法的具体技术差异。Compressor-VLA (Nov 2025) 更是在同一 LIBERO benchmark 上用类似的 cross-attention 压缩实现了 59% FLOPs 降低。\n- 为什么影响接收：如果方法本质是已知架构的直接应用，贡献 claim 3 (\"Cross-attention re-encoding\") 的实际增量将大幅缩水。CoRL 审稿人会期望看到与 Q-Former resampler 的对比实验或明确的技术差异论证。\n- 建议修改方向：(1) 增加 Smart Compress 与 Q-Former/Perceiver Resampler 的定性和定量对比；(2) 明确论述为什么 Smart Compress 在 pixel-shuffle VLA 上的应用是非平凡的；(3) 引用并对比 Compressor-VLA\n\n**N3** [critical] \"First cross-architecture closed-loop evaluation\" claim 需要严格验证\n\n- 具体位置：Abstract (\"We conduct the first cross-architecture closed-loop evaluation\"), Introduction ¶2 (\"no prior work has systematically evaluated\")\n- 问题：鉴于 N1 中列出的大量遗漏工作，这一 \"first\" claim 的准确性存疑。SpecPrune-VLA 在 LIBERO 和真实机器人上评估；LightVLA 在多架构上评估；\"See What Matters\" (ICML 2026) 也做了跨架构评估。虽然这些工作可能没有做完全相同的 \"两种 connector 在同一 benchmark 上的对比评估\"，但 \"first\" claim 需要在充分调研基础上才能成立。\n- 为什么影响接收：如果 \"first\" claim 被审稿人发现不准确，将严重损害论文可信度。\n- 建议修改方向：要么提供充分证据证明确实是 first（在引用所有相关工作后），要么弱化为 \"among the first\" 或 \"to our knowledge\"\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] Connector 与 Scale 的混淆变量未充分解决\n\n- 具体位置：Section 5.3 (Disentangling Connector from Scale)\n- 问题：SmolVLA (0.5B) vs OpenVLA (7B) 在 connector 和 scale 两个维度上同时不同。论文给出了四个间接论证支持 connector 解释（official checkpoint、k=0.95 的敏感性、entropy ratio、pixel-shuffle 机制），但这些都是推理性的，不是控制实验。特别是 7B 模型的冗余容量可能天然对 perturbation 更鲁棒——这不需要 connector 解释也能成立。EfficientVLA 的外部证据来自不同 benchmark，不能完全消除混淆。\n- 建议：(1) 论文应更诚实地承认这是一个未解决的 confound，而非仅列为 \"future work\"；(2) 如果可行，在 SmolVLA backbone 上接 MLP projector（或反之）做消融\n\n**W2** [warning] Smart Compress 的 \"performance-neutral deployment benefit\" 措辞不准确\n\n- 具体位置：Abstract (\"a performance-neutral deployment benefit\"), Introduction 贡献 3\n- 问题：Smart Compress 实际上将 SR 从 44.8% 提升到 61.6%，这是性能提升，不是 \"performance-neutral\"。而且 Appendix B (Section B, Inference Cost-Benefit Analysis) 显示实际 latency 改善仅 6%（154.78ms vs 164.33ms），speedup 仅 1.06x。\"Performance-neutral\" 这个措辞既不准确描述 SR 变化，也容易误导读者认为没有 latency 成本。\n- 建议：准确表述为 \"performance-improving at the cost of 22.2M additional parameters and training, with modest latency benefit (1.06x) at current scale\"\n\n**W3** [warning] LIBERO-Goal 上 Smart Compress 性能下降被淡化\n\n- 具体位置：Section 4.3 (最后一段), Table 6 (Appendix)\n- 问题：Smart Compress ($M=32$, trained on LIBERO-Object) 在 LIBERO-Goal 上从 63.0% 降到 56.4%（-6.6pp），这并非 trivial 的退化。论文用 \"maintains non-trivial performance where deletion-based methods completely fail\" 来淡化这一结果。但与 hard pruning (0%) 比较是一个很低的标准——更合理的比较是与 unpruned baseline。\n- 建议：明确报告泛化损失，讨论可能原因（domain gap, task distribution shift），不要只用 \"vs 0%\" 来 frame\n\n**W4** [warning] 引用数量偏少\n\n- 具体位置：references.bib (26 条)\n- 问题：对于 CoRL 全文投稿，26 条引用偏少。大多数 CoRL 录用论文有 35-50+ 条引用。即使不考虑遗漏的直接相关工作，general VLM efficiency（SparseVLM、FitPrune、TokenPacker 等）和 robot learning efficiency 领域的覆盖也不够全面。\n- 建议：补充至 35-40 条引用\n\n**W5** [warning] 仅两个 random seed 不足以声称 \"robustness to initialization\"\n\n- 具体位置：Section 4.3, Table 8 (Appendix)\n- 问题：论文用 seed 42 和 seed 43 两个 seed 的结果声称 \"confirming robustness to initialization\"。两个 seed 的 half-range 不构成统计意义上的方差估计。±1.2 和 ±2.8 的 half-range 也不能排除更大的方差。\n- 建议：至少用 3-5 个 seed，或弱化 \"robustness\" 的措辞\n\n---\n\n## 小问题（不影响接收）\n\n1. **Table 1 小数精度不统一**：SR 列用整数百分比但 CI 用两位小数，视觉上不一致。建议统一。\n\n2. **Abstract 偏长**：约 200 words，在可接受范围但偏上限。可以精简 \"across two checkpoints of different training quality, seven pruning configurations, and three pruning mechanisms\" 这类细节。\n\n3. **贡献列表中 \"consistent across three models and two connector families\" 引用 EfficientVLA**（Contribution 1）：这依赖外部论文的证据来支撑本文贡献，应标明是 \"supported by concurrent findings from\"，而非作为本文贡献的一部分。\n\n4. **Appendix D (Attention Entropy) 采样量不对等**：SmolVLA 用 2400 frames，OpenVLA 用 250 frames（10x 差异）。虽然有 std < 0.02 的辩护，但不对等的采样量在方法论上不够干净。\n\n5. **Figure 3 (pixel-shuffle) 信息量有限**：仅展示 4x4 folding 的示意图，这一操作在文字中已描述清楚。可考虑与 Figure 4 合并或缩小。\n\n6. **bib 条目 minor issues**：verify_references 显示 5 条 mismatch（主要是 first_author 字段差异，如 ghosh2024octo 的 \"Octo Model Team\" vs API 返回的 \"Ghosh\"）和 1 条 not_found（black2024pi0）。π₀ 论文的 bib 条目应确认 arXiv ID 正确。\n\n---\n\n## Questions to Authors\n\n1. Smart Compress 与 BLIP-2 Q-Former 的具体技术区别是什么？如果 SmolVLA 在 connector 层换用 Q-Former resampler，结果是否相同？\n\n2. 是否考虑过在 SmolVLA 的 backbone 上用 MLP projector（而非 pixel-shuffle）做控制实验来隔离 connector 效应？\n\n3. Compressor-VLA (Nov 2025) 也在 LIBERO 上用 cross-attention 压缩达到了 59% FLOPs 降低——如何 position Smart Compress 相对于此工作？\n\n4. 论文声称 \"first cross-architecture closed-loop evaluation\"，但 SpecPrune-VLA、LightVLA、\"See What Matters\" 等工作也在 VLA 上做了 token pruning 评估。这一 \"first\" claim 的精确边界是什么？\n\n---\n\n## Missing References（按重要性排序）\n\n1. **[CRITICAL]** \"Don't Run with Scissors: Pruning Breaks VLA Models but They Can Be Recovered\" (arXiv 2510.08464, Oct 2025) — VLA pruning fragility + recovery\n2. **[CRITICAL]** Compressor-VLA (arXiv 2511.18950, Nov 2025) — Cross-attention VLA token compression on LIBERO\n3. **[HIGH]** SpecPrune-VLA (arXiv 2509.05614, Sep 2025) — Action-aware VLA token pruning on LIBERO\n4. **[HIGH]** LightVLA / \"The Better You Learn, The Smarter You Prune\" (arXiv 2509.12594, Sep 2025) — Differentiable VLA token pruning\n5. **[HIGH]** \"See What Matters: Differentiable Grid Sample Pruning for Generalizable VLA Model\" (ICML 2026) — Grid-based VLA compression\n6. **[MEDIUM]** SparseVLM (arXiv 2410.04417, ICLR 2025) — Training-free VLM token sparsification\n7. **[MEDIUM]** SparseVILA (arXiv 2510.17777, ICCV 2025) — Decoupled visual sparsity for VLM\n\n---\n\n## 主要优势\n\n1. **实验设计严谨**：7 种 pruning 配置的 full factorial 消融、500 episodes 的充分评估、Wilson 置信区间、extended training 控制实验、双 seed 验证，实验方法论水平高于多数 VLA 效率论文。\n\n2. **清晰的经验性发现**：cliff-edge failure 现象的刻画具有实际价值——59.2% → 0% 的断崖式崩溃在 k=0.95 仍然成立（仅移除 7/128 tokens），这一发现对 VLA 系统设计者有直接参考意义。\n\n3. **写作质量高**：叙事线清晰（问题→发现→解释→方案），无明显 AI 写作痕迹，专有名词定义到位，段落过渡自然。Abstract 在 30 秒内可传达核心价值。\n\n4. **合理的控制实验**：extended training control (45.0% SR vs 44.8%, p > 0.9) 有效排除了 \"额外训练\" 这一替代解释，multi-seed 结果虽然 seed 数不足但方向正确。\n\n5. **格式合规**：8 页正文，匿名化正确，Limitations section 实质性存在，使用官方 corl_2026.sty 模板。\n\n---\n\n## Overall Assessment\n\n本文的核心经验性发现（pixel-shuffle connector 下 vision token pruning 的 cliff-edge failure）是有价值的，实验方法论严谨，写作质量高。但在新颖性和 related work 完整性方面存在显著问题：\n\n1. **新颖性有限**：pixel-shuffle 的空间纠缠使其 token 不可独立剪枝，从架构设计角度看这并非 surprising。Smart Compress 本质是 cross-attention resampler 的标准应用，缺乏与 Q-Former/Perceiver/Compressor-VLA 的区分。\n\n2. **Related work 严重不完整**：遗漏了至少 5-7 篇 2025-2026 年直接相关的 VLA token efficiency 工作，其中 Compressor-VLA 在相同 benchmark 上用类似方法取得了更好的效率结果。这使得论文的 positioning 和 \"first\" claim 站不住脚。\n\n3. **实验对比公平性**：两个模型在 connector 和 scale 上同时不同，控制实验缺失。\n\n如果作者能补充所有遗漏引用、重新 position 贡献、增加与 Q-Former/Compressor-VLA 的对比，论文质量有望提升至 accept 水平。当前状态下，建议 weak reject。\n\n**Rating: 5/10 (Borderline Reject)**\n**Confidence: 4/5**\n",
  "reviewer_id": "2",
  "project": "importance_margin_vla_compress"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "\n## Reviewer 2 — Round 1 审稿报告\n\n**论文**: \"Why Token Pruning Crashes Some Robot Policies but Not Others: The Role of Vision Connectors in VLA Token Compressibility\"\n**Venue**: CoRL 2026\n**审查侧重**: 新颖性 + Related Work 完整性 + 写作质量 + 格式合规\n\n---\n\n## Summary\n\n本文研究 VLA 模型中 vision token pruning 的跨架构行为差异。核心发现：pixel-shuffle connector（SmolVLA）下 token pruning 导致 cliff-edge failure（59.2% → 0%），而 MLP projector（OpenVLA）graceful degradation（74.0% → 37.4%）。作者用 attention entropy ratio 解释此差异，并提出 cross-attention re-encoding（Smart Compress）模块在 75% token reduction 下保持 61.6% SR。实验在 LIBERO 基准上进行，涵盖多种 pruning 配置。\n\n---\n\n## 总体评分\n\n**Overall**: 5/10 (Borderline — 有价值的实证发现但新颖性和完整性存在显著问题)\n\n**一句话总结**: 经验性发现有意义但偏 expected，Smart Compress 方法创新不足，且遗漏多篇直接相关工作（包括至少 5 篇 2025-2026 VLA efficiency 论文），严重削弱了 positioning 的可信度。\n\n**Confidence**: 4/5 (对 VLA 效率和 token pruning 领域较为熟悉)\n\n---\n\n## 官方维度打分（基于 CoRL review form 维度）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Originality | 2/5 | 核心发现（pixel-shuffle 不可剪枝）从架构设计角度看较为 expected；Smart Compress 本质是 Q-Former/Perceiver 变体 |\n| Quality | 3/5 | 实验设计严谨（多配置消融、置信区间、控制实验），但两模型对比存在 scale confound，遗漏多篇直接竞争方法 |\n| Clarity | 4/5 | 写作清晰直接，叙事线连贯，无明显 AI 写作标志，图表信息密度合理 |\n| Significance | 3/5 | 对 practitioner 有参考价值（选 connector 需考虑压缩性），但实际 actionable guidance 有限 |\n| Relevance | 4/5 | 直接面向机器人学习效率问题，符合 CoRL 受众 |\n| Limitations | 3/5 | 存在且实质性（simulation-only, scale confound, 泛化不足），但未讨论与遗漏工作的关系 |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] 遗漏多篇直接竞争的 VLA token efficiency 工作\n\n- 具体位置：Section 2 (Related Work)，全文 positioning\n- 问题：以下 2025-2026 年论文与本文高度相关但完全未被引用：\n  1. **\"Don't Run with Scissors: Pruning Breaks VLA Models but They Can Be Recovered\"** (arXiv 2510.08464, Oct 2025) — 研究 VLA 模型 pruning 后的性能崩溃和恢复，提出 GLUESTICK 方法。虽然聚焦 weight pruning 而非 token pruning，但核心主题（pruning 破坏 VLA 模型）与本文直接重叠，且在多种 VLA 架构上评估\n  2. **Compressor-VLA** (arXiv 2511.18950, Nov 2025) — 指令引导的视觉 token 压缩框架，包含 cross-attention 压缩（Semantic Task Compressor），在 LIBERO 上评估，与 Smart Compress 方法高度类似\n  3. **SpecPrune-VLA** (arXiv 2509.05614, Sep 2025) — Action-aware self-speculative pruning，在 LIBERO 上实现 1.57x 加速且 SR 几乎不降\n  4. **LightVLA / \"The Better You Learn, The Smarter You Prune\"** (arXiv 2509.12594, Sep 2025) — 可微分 token pruning，59% FLOPs 降低且 SR 提升 2.9%\n  5. **\"See What Matters: Differentiable Grid Sample Pruning for Generalizable VLA Model\"** (ICML 2026) — 可微分 grid sampling 压缩视觉 token，<10% token 保留\n  6. **SparseVLM** (ICLR 2025 / arXiv 2410.04417) — Training-free VLM token 稀疏化\n  7. **SparseVILA** (ICCV 2025 / arXiv 2510.17777) — 解耦视觉稀疏性\n- 为什么影响接收：这些遗漏严重削弱了 \"first cross-architecture closed-loop evaluation\" 的 claim 可信度，也使得 Smart Compress 的 novelty positioning 无法成立——Compressor-VLA 使用了类似的 cross-attention 压缩且在相同 benchmark 上评估。审稿人会立即注意到这一调研缺口。\n- 建议修改方向：全面补充上述引用，重新评估 \"first\" claim 的准确性，明确 Smart Compress 与 Compressor-VLA 的区别\n\n**N2** [critical] Smart Compress 方法新颖性不足，与 Q-Former/Perceiver/Compressor-VLA 区分不清\n\n- 具体位置：Section 3.4 (Smart Compress Setup), Section 5.2 (Why Learned Compression Succeeds)\n- 问题：Smart Compress 的核心是 M 个 learned query vectors 通过 multi-head cross-attention 对 128 source tokens 进行 pooling。这与 BLIP-2 的 Q-Former（32 learned queries cross-attend to image features）和 Perceiver Resampler（latent queries cross-attend to visual tokens）在机制上几乎相同。论文 Related Work (Section 2, \"Vision connectors\" 段落) 虽然提到了 Q-Former 和 Perceiver，但仅作为 vision connector taxonomy 的一部分列出，完全没有讨论 Smart Compress 与这些方法的具体技术差异。Compressor-VLA (Nov 2025) 更是在同一 LIBERO benchmark 上用类似的 cross-attention 压缩实现了 59% FLOPs 降低。\n- 为什么影响接收：如果方法本质是已知架构的直接应用，贡献 claim 3 (\"Cross-attention re-encoding\") 的实际增量将大幅缩水。CoRL 审稿人会期望看到与 Q-Former resampler 的对比实验或明确的技术差异论证。\n- 建议修改方向：(1) 增加 Smart Compress 与 Q-Former/Perceiver Resampler 的定性和定量对比；(2) 明确论述为什么 Smart Compress 在 pixel-shuffle VLA 上的应用是非平凡的；(3) 引用并对比 Compressor-VLA\n\n**N3** [critical] \"First cross-architecture closed-loop evaluation\" claim 需要严格验证\n\n- 具体位置：Abstract (\"We conduct the first cross-architecture closed-loop evaluation\"), Introduction ¶2 (\"no prior work has systematically evaluated\")\n- 问题：鉴于 N1 中列出的大量遗漏工作，这一 \"first\" claim 的准确性存疑。SpecPrune-VLA 在 LIBERO 和真实机器人上评估；LightVLA 在多架构上评估；\"See What Matters\" (ICML 2026) 也做了跨架构评估。虽然这些工作可能没有做完全相同的 \"两种 connector 在同一 benchmark 上的对比评估\"，但 \"first\" claim 需要在充分调研基础上才能成立。\n- 为什么影响接收：如果 \"first\" claim 被审稿人发现不准确，将严重损害论文可信度。\n- 建议修改方向：要么提供充分证据证明确实是 first（在引用所有相关工作后），要么弱化为 \"among the first\" 或 \"to our knowledge\"\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] Connector 与 Scale 的混淆变量未充分解决\n\n- 具体位置：Section 5.3 (Disentangling Connector from Scale)\n- 问题：SmolVLA (0.5B) vs OpenVLA (7B) 在 connector 和 scale 两个维度上同时不同。论文给出了四个间接论证支持 connector 解释（official checkpoint、k=0.95 的敏感性、entropy ratio、pixel-shuffle 机制），但这些都是推理性的，不是控制实验。特别是 7B 模型的冗余容量可能天然对 perturbation 更鲁棒——这不需要 connector 解释也能成立。EfficientVLA 的外部证据来自不同 benchmark，不能完全消除混淆。\n- 建议：(1) 论文应更诚实地承认这是一个未解决的 confound，而非仅列为 \"future work\"；(2) 如果可行，在 SmolVLA backbone 上接 MLP projector（或反之）做消融\n\n**W2** [warning] Smart Compress 的 \"performance-neutral deployment benefit\" 措辞不准确\n\n- 具体位置：Abstract (\"a performance-neutral deployment benefit\"), Introduction 贡献 3\n- 问题：Smart Compress 实际上将 SR 从 44.8% 提升到 61.6%，这是性能提升，不是 \"performance-neutral\"。而且 Appendix B (Section B, Inference Cost-Benefit Analysis) 显示实际 latency 改善仅 6%（154.78ms vs 164.33ms），speedup 仅 1.06x。\"Performance-neutral\" 这个措辞既不准确描述 SR 变化，也容易误导读者认为没有 latency 成本。\n- 建议：准确表述为 \"performance-improving at the cost of 22.2M additional parameters and training, with modest latency benefit (1.06x) at current scale\"\n\n**W3** [warning] LIBERO-Goal 上 Smart Compress 性能下降被淡化\n\n- 具体位置：Section 4.3 (最后一段), Table 6 (Appendix)\n- 问题：Smart Compress ($M=32$, trained on LIBERO-Object) 在 LIBERO-Goal 上从 63.0% 降到 56.4%（-6.6pp），这并非 trivial 的退化。论文用 \"maintains non-trivial performance where deletion-based methods completely fail\" 来淡化这一结果。但与 hard pruning (0%) 比较是一个很低的标准——更合理的比较是与 unpruned baseline。\n- 建议：明确报告泛化损失，讨论可能原因（domain gap, task distribution shift），不要只用 \"vs 0%\" 来 frame\n\n**W4** [warning] 引用数量偏少\n\n- 具体位置：references.bib (26 条)\n- 问题：对于 CoRL 全文投稿，26 条引用偏少。大多数 CoRL 录用论文有 35-50+ 条引用。即使不考虑遗漏的直接相关工作，general VLM efficiency（SparseVLM、FitPrune、TokenPacker 等）和 robot learning efficiency 领域的覆盖也不够全面。\n- 建议：补充至 35-40 条引用\n\n**W5** [warning] 仅两个 random seed 不足以声称 \"robustness to initialization\"\n\n- 具体位置：Section 4.3, Table 8 (Appendix)\n- 问题：论文用 seed 42 和 seed 43 两个 seed 的结果声称 \"confirming robustness to initialization\"。两个 seed 的 half-range 不构成统计意义上的方差估计。±1.2 和 ±2.8 的 half-range 也不能排除更大的方差。\n- 建议：至少用 3-5 个 seed，或弱化 \"robustness\" 的措辞\n\n---\n\n## 小问题（不影响接收）\n\n1. **Table 1 小数精度不统一**：SR 列用整数百分比但 CI 用两位小数，视觉上不一致。建议统一。\n\n2. **Abstract 偏长**：约 200 words，在可接受范围但偏上限。可以精简 \"across two checkpoints of different training quality, seven pruning configurations, and three pruning mechanisms\" 这类细节。\n\n3. **贡献列表中 \"consistent across three models and two connector families\" 引用 EfficientVLA**（Contribution 1）：这依赖外部论文的证据来支撑本文贡献，应标明是 \"supported by concurrent findings from\"，而非作为本文贡献的一部分。\n\n4. **Appendix D (Attention Entropy) 采样量不对等**：SmolVLA 用 2400 frames，OpenVLA 用 250 frames（10x 差异）。虽然有 std < 0.02 的辩护，但不对等的采样量在方法论上不够干净。\n\n5. **Figure 3 (pixel-shuffle) 信息量有限**：仅展示 4x4 folding 的示意图，这一操作在文字中已描述清楚。可考虑与 Figure 4 合并或缩小。\n\n6. **bib 条目 minor issues**：verify_references 显示 5 条 mismatch（主要是 first_author 字段差异，如 ghosh2024octo 的 \"Octo Model Team\" vs API 返回的 \"Ghosh\"）和 1 条 not_found（black2024pi0）。π₀ 论文的 bib 条目应确认 arXiv ID 正确。\n\n---\n\n## Questions to Authors\n\n1. Smart Compress 与 BLIP-2 Q-Former 的具体技术区别是什么？如果 SmolVLA 在 connector 层换用 Q-Former resampler，结果是否相同？\n\n2. 是否考虑过在 SmolVLA 的 backbone 上用 MLP projector（而非 pixel-shuffle）做控制实验来隔离 connector 效应？\n\n3. Compressor-VLA (Nov 2025) 也在 LIBERO 上用 cross-attention 压缩达到了 59% FLOPs 降低——如何 position Smart Compress 相对于此工作？\n\n4. 论文声称 \"first cross-architecture closed-loop evaluation\"，但 SpecPrune-VLA、LightVLA、\"See What Matters\" 等工作也在 VLA 上做了 token pruning 评估。这一 \"first\" claim 的精确边界是什么？\n\n---\n\n## Missing References（按重要性排序）\n\n1. **[CRITICAL]** \"Don't Run with Scissors: Pruning Breaks VLA Models but They Can Be Recovered\" (arXiv 2510.08464, Oct 2025) — VLA pruning fragility + recovery\n2. **[CRITICAL]** Compressor-VLA (arXiv 2511.18950, Nov 2025) — Cross-attention VLA token compression on LIBERO\n3. **[HIGH]** SpecPrune-VLA (arXiv 2509.05614, Sep 2025) — Action-aware VLA token pruning on LIBERO\n4. **[HIGH]** LightVLA / \"The Better You Learn, The Smarter You Prune\" (arXiv 2509.12594, Sep 2025) — Differentiable VLA token pruning\n5. **[HIGH]** \"See What Matters: Differentiable Grid Sample Pruning for Generalizable VLA Model\" (ICML 2026) — Grid-based VLA compression\n6. **[MEDIUM]** SparseVLM (arXiv 2410.04417, ICLR 2025) — Training-free VLM token sparsification\n7. **[MEDIUM]** SparseVILA (arXiv 2510.17777, ICCV 2025) — Decoupled visual sparsity for VLM\n\n---\n\n## 主要优势\n\n1. **实验设计严谨**：7 种 pruning 配置的 full factorial 消融、500 episodes 的充分评估、Wilson 置信区间、extended training 控制实验、双 seed 验证，实验方法论水平高于多数 VLA 效率论文。\n\n2. **清晰的经验性发现**：cliff-edge failure 现象的刻画具有实际价值——59.2% → 0% 的断崖式崩溃在 k=0.95 仍然成立（仅移除 7/128 tokens），这一发现对 VLA 系统设计者有直接参考意义。\n\n3. **写作质量高**：叙事线清晰（问题→发现→解释→方案），无明显 AI 写作痕迹，专有名词定义到位，段落过渡自然。Abstract 在 30 秒内可传达核心价值。\n\n4. **合理的控制实验**：extended training control (45.0% SR vs 44.8%, p > 0.9) 有效排除了 \"额外训练\" 这一替代解释，multi-seed 结果虽然 seed 数不足但方向正确。\n\n5. **格式合规**：8 页正文，匿名化正确，Limitations section 实质性存在，使用官方 corl_2026.sty 模板。\n\n---\n\n## Overall Assessment\n\n本文的核心经验性发现（pixel-shuffle connector 下 vision token pruning 的 cliff-edge failure）是有价值的，实验方法论严谨，写作质量高。但在新颖性和 related work 完整性方面存在显著问题：\n\n1. **新颖性有限**：pixel-shuffle 的空间纠缠使其 token 不可独立剪枝，从架构设计角度看这并非 surprising。Smart Compress 本质是 cross-attention resampler 的标准应用，缺乏与 Q-Former/Perceiver/Compressor-VLA 的区分。\n\n2. **Related work 严重不完整**：遗漏了至少 5-7 篇 2025-2026 年直接相关的 VLA token efficiency 工作，其中 Compressor-VLA 在相同 benchmark 上用类似方法取得了更好的效率结果。这使得论文的 positioning 和 \"first\" claim 站不住脚。\n\n3. **实验对比公平性**：两个模型在 connector 和 scale 上同时不同，控制实验缺失。\n\n如果作者能补充所有遗漏引用、重新 position 贡献、增加与 Q-Former/Compressor-VLA 的对比，论文质量有望提升至 accept 水平。当前状态下，建议 weak reject。\n\n**Rating: 5/10 (Borderline Reject)**\n**Confidence: 4/5**\n",
    "reviewer_id": "2",
    "project": "importance_margin_vla_compress"
  }
}
```

</details>

---


### Tool result

_source line 165 · 2026-05-19T01:19:54.578550+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4378
}
```

</details>

---


### Assistant

_source line 166 · 2026-05-19T01:20:03.098992+00:00_

审稿报告已提交给 Review Director。

**审查要点总结**：

- **评分 5/10 (Borderline Reject)**，置信度 4/5
- **3 个 Must-Fix 问题**：
  1. 遗漏至少 5-7 篇直接相关的 VLA token efficiency 工作（最关键：Compressor-VLA 在 LIBERO 上用类似 cross-attention 压缩、"Don't Run with Scissors" 研究 VLA pruning fragility、SpecPrune-VLA/LightVLA/"See What Matters" 等）
  2. Smart Compress 与 Q-Former/Perceiver/Compressor-VLA 的技术区分缺失
  3. "First cross-architecture closed-loop evaluation" claim 在遗漏大量相关工作的情况下可信度不足
- **5 个 Should-Fix**：scale confound 未解决、"performance-neutral" 措辞不准确、LIBERO-Goal 退化被淡化、引用数量偏少(26条)、2个seed不足以声称 robustness
- **优势**：实验设计严谨（7配置消融+控制实验）、cliff-edge 发现有实际参考价值、写作质量高无 AI 痕迹、格式合规

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2"
}
```

</details>

---


## Round 4

## Round 4

4 recorded events


### User

_source line 167 · 2026-05-19T01:22:07.186131+00:00_

[Round 1 审稿请求]:
## 交叉分享 — Reviewer 1 的完整审稿意见

请逐条回应以下 Reviewer 1 的意见。对每一条：
- **[AGREE]** 同意并说明理由
- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）

特别关注你作为新颖性/写作专家的视角——Reviewer 1 的 Must-Fix 集中在方法严谨性和统计，请评估这些实验问题如何影响你对论文新颖性和整体贡献的判断。

---

以下是 Reviewer 1 的完整审稿原文：

## Reviewer 1 — Round 1 审稿报告

**审查侧重**: 方法严谨性 + 实验设计 + 统计有效性
**评分**: 3/5 (Borderline), **置信度**: 4/5 (High)

### Must-Fix 问题

**N1** [critical] Scale confound 未充分解决——因果 claim 过强
- SmolVLA (0.5B) vs OpenVLA (7B) scale 差 14 倍
- 4 条 disentangling 论据逐条评估：
  - (1) Official checkpoint cliff-edge：有效排除 training quality，但不排除 scale
  - (2) k=0.95 仅移除 7/128 tokens 即崩溃：**最有力论据**——小扰动导致灾难性失败指向架构脆弱性
  - (3) Entropy ratio 是 architectural measurement：**弱**——存在循环论证风险，更大模型可能天然学到更 selective attention
  - (4) Pixel-shuffle mechanistic account：有说服力但不完整
  - EfficientVLA (CogACT)：corroborative 但为外部实验
- "attributable to" 是因果断言，证据只支持更弱的相关性
- 建议改为 "associated with" 或 "primarily shaped by"

**N2** [critical] Multi-seed 实验仅 2 seeds——统计不可靠
- 2 个 seed 无法计算标准差的可靠估计（自由度=1）
- "half-range" 不是标准统计量度
- M=96 在 2 seeds 间 5.6pp 差异（52.6% vs 58.2%）不能标注为 "low variance"
- CoRL 标准要求至少 3 seeds（通常 5）

**N3** [critical] Baseline reproduction 严重偏低——实验可信度存疑
- SmolVLA baseline 44.8% vs 官方 87.3%（差距 42.5pp）
- Footnote 仅提及 "smaller batch"，batch size 具体值未给出
- Smart Compress 全部实验建立在偏低 baseline 上
- 在 44.8% baseline 上模型可能处于 underfitting 状态，pruning sensitivity 可能与正常训练模型不同
- 建议在 official checkpoint 上也运行 Smart Compress

### Should-Fix 问题

**W1** 仅 LIBERO simulation 评估——CoRL 期望 real-robot 或多 benchmark
**W2** OpenVLA 实验不对称——缺少 learned pruning
**W3** M=96 performance dip 未解释
**W4** Offline metric disconnect 论证不完整——未展示 "misleadingly positive" 的典型 offline metric
**W5** Smart Compress 跨任务 generalization 下降未充分讨论

### Minor Issues
1. Table 1 非完全正交 ablation（7/24 配置）
2. Appendix D 采样量不同（2400 vs 260 frames）
3. Smart Compress 训练细节不完整（缺 lr, optimizer, batch size 等）
4. bib 格式问题
5. "Performance-neutral" 表述——61.6% 低于 official 87.3%
6. Appendix E speedup 仅 1.06×

### Questions
1. Smart Compress M=128 (59.8%) ≈ official checkpoint (59.2%)——cross-attention 是否只是替代 large-batch training？
2. Entropy ratio 是否在其他 connector 上验证过？N=2 architectures 证据力弱
3. ACIS scorer 训练质量——"learned = random" 是否因 scorer 失败？
4. OpenVLA degradation curve 近似线性——有理论预期吗？

### Missing References
1. RoboFlamingo（cross-attention vision connector VLA）
2. SPA-VL 或其他 VLM token pruning closed-loop 评估
3. TinyVLA 或其他 small-scale VLA

### Strengths
1. 研究问题重要且及时
2. SmolVLA ablation 设计系统
3. Extended training control 设计良好
4. Closed-loop vs offline disconnect 有价值
5. Official checkpoint 验证
6. 写作质量高

### Detailed Comments（摘要）
- SmolVLA 7 配置 ablation 覆盖合理，all-zero 结论有力
- OpenVLA 仅 random pruning 是设计权衡——random 是最弱 pruning，graceful degradation 更有说服力
- Wilson CI 使用正确，500 episodes 足以区分 44.8% 和 61.6%
- §5.3 论据 (2)（k=0.95 collapse）是最强论据
- Table 2 CI 重叠支持 "flat across {32,64,128}" 但 M=96 selective reporting
- Extended training control p > 0.9 合理
- Offline metric disconnect 需要展示 mean vs tail 对比
- 训练细节不足以复现

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 168 · 2026-05-19T01:23:37.269414+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "\n## Reviewer 2 — 交叉回应 Reviewer 1 意见\n\n---\n\n### Must-Fix 逐条回应\n\n**[AGREE] R1-N1: Scale confound 未充分解决，因果 claim 过强**\n\n同意 R1 的核心判断。从新颖性角度补充：这一 confound 不仅是统计问题，直接削弱了论文的核心贡献 claim。Contribution 1 (\"Architecture-dependent compressibility\") 的价值建立在 \"connector design shapes compressibility\" 这一因果链上。如果 scale 是主要解释变量，那么整篇论文的叙事线从 Introduction ¶3 到 Conclusion 都需要重写。\n\nR1 对四条论据的逐条评估我基本同意，补充一点：论据 (3)（entropy ratio）的循环论证风险比 R1 描述的更严重。Section 5.1 用 entropy ratio 来\"解释\"为什么 pixel-shuffle 不可剪枝，但 entropy ratio 本身是 pixel-shuffle 架构的直接产物（均匀信息密度 → 均匀 attention），不构成独立证据。这就像用\"水是湿的\"来解释\"水能弄湿东西\"。\n\nR1 建议改 \"attributable to\" 为 \"associated with\" 合理。从写作质量角度，Abstract 中 \"compressibility is attributable to the vision connector design\" 和 Conclusion 中 \"Compressibility is attributable to the vision connector\" 都是过强的因果断言（Section 5.3 标题本身就是 \"Disentangling Connector from Scale\"，承认了这是未解决的问题）。\n\n---\n\n**[AGREE] R1-N2: Multi-seed 仅 2 seeds，统计不可靠**\n\n完全同意。2 seeds 不仅无法计算可靠方差（R1 指出 df=1），而且 M=96 的 5.6pp half-range（52.6% vs 58.2%）实际上是所有配置中最大的，论文却在 Table 8 caption 中声称 \"All configurations show low variance across seeds\"（Appendix, Table 8）。这是 selective reporting。\n\n从新颖性影响角度：如果 Smart Compress 的性能方差实际较大（3-5 seeds 可能揭示），那么 \"flat across {32, 64, 128}\" 的核心发现——即 \"gain comes from re-encoding, not compression\"——的证据力将减弱。这直接影响贡献 claim 3 的可信度。\n\n---\n\n**[AGREE with nuance] R1-N3: Baseline reproduction 严重偏低**\n\n同意这是显著问题，但需要区分两个层面：\n\n**同意的部分**：44.8% vs 87.3% 的差距确实很大，且 footnote（Section 4.1, footnote 1）仅说 \"smaller batch due to compute constraints\"，没有给出具体 batch size。Smart Compress 在 underfitting baseline 上的改善可能不能外推到正常训练模型。R1 建议在 official checkpoint 上运行 Smart Compress 很合理。\n\n**需要补充的部分**：论文实际在 official checkpoint (59.2% SR) 上也做了 pruning 实验（Table 1 最后两行），结果同样 0% SR，这部分验证了 cliff-edge 的 robustness。但 Smart Compress 确实只在 44.8% baseline 上评估过。从新颖性角度看，如果 Smart Compress 在 59.2% baseline 上也有效（比如达到 ~75%），那将是更有说服力的贡献；反之，如果失效，则 Smart Compress 的 claim 大幅缩水。这一实验缺失使得贡献 3 的 generality 无法评估。\n\n另外值得注意：R1 的 Question 1 提出 Smart Compress M=128 (59.8%) ≈ official checkpoint (59.2%)，暗示 cross-attention 可能只是替代 large-batch training 的效果。这是一个非常敏锐的观察。Section 4.3 的 extended training control (45.0%) 排除了 \"额外训练步数\" 的解释，但没有排除 \"额外参数容量\" 的解释——22.2M 参数的 cross-attention module 可能本身就像一个额外的 adapter，其效果与 re-encoding 无关。\n\n---\n\n### Should-Fix 逐条回应\n\n**[AGREE] R1-W1: 仅 LIBERO simulation 评估**\n\n同意。从 CoRL 社区角度，simulation-only 评估对于声称 \"deployment benefit\" 的论文是明显不足的。Abstract 和 Introduction 使用 \"deployment benefit\" 这一措辞（Abstract: \"a performance-neutral deployment benefit\"），暗示了实际部署价值，但全部实验都在 simulation 中完成。我在 R2 报告中也指出了 \"performance-neutral deployment benefit\" 措辞的问题。\n\n---\n\n**[AGREE] R1-W2: OpenVLA 实验不对称，缺少 learned pruning**\n\n同意。SmolVLA 有 7 种配置（learned + random × multiple k × multiple mechanisms），OpenVLA 仅有 random pruning。这一不对称使得跨架构对比不完全公平：SmolVLA 的 0% 结论覆盖了所有可能的 pruning 方法，但 OpenVLA 的 graceful degradation 仅在最简单的 random removal 下验证。如果在 OpenVLA 上用 learned pruning（如 FastV 或 attention-based scoring），degradation curve 可能更平缓或更陡——两种方向都影响论文结论。\n\n从新颖性角度：这削弱了 \"architecture-dependent compressibility\" 发现的精度。当前证据只能支持 \"SmolVLA 在所有方法下崩溃，OpenVLA 在 random removal 下优雅退化\"，不能支持更一般的 \"MLP projectors degrade gracefully under any pruning\"。\n\n---\n\n**[AGREE] R1-W3: M=96 performance dip 未解释**\n\n同意。Table 2 中 M=96 (52.6%) 显著低于 M=64 (61.6%) 和 M=128 (59.8%)，打破了 \"flat across {32, 64, 128}\" 的叙事。论文完全没有讨论这一异常。从写作质量角度，这是 selective reporting 的典型案例——Table 2 caption 说 \"Performance is flat across M ∈ {32, 64, 128}\"，通过排除 M=96 来维持叙事。审稿人会注意到这一点。\n\nM=96 的多 seed 结果（55.4% ± 2.8）也是方差最大的配置，进一步说明 \"flat\" 结论的证据不足。\n\n---\n\n**[AGREE] R1-W4: Offline metric disconnect 论证不完整**\n\n同意。Section 5.4 声称 \"Offline evaluation metrics provide misleadingly positive signals\"，但正文中没有展示这些 \"misleadingly positive\" 的 offline metric 数值。Appendix C (Table 5) 展示了 single-step action error（3.4x 增加），但这是 \"misleadingly negative\" 而非 \"misleadingly positive\"。论文实际需要展示的是：某个 offline metric 看起来合理（比如 mean action error 小），但 closed-loop 却崩溃。当前论证存在逻辑缺口。\n\n---\n\n**[AGREE] R1-W5: Smart Compress 跨任务 generalization 下降未充分讨论**\n\n同意，与我 R2 报告中 W3 一致。LIBERO-Goal 从 63.0% 降到 56.4%（-6.6pp）不应被淡化。\n\n---\n\n### Minor Issues 回应\n\n**[AGREE] R1-Minor-1**: Table 1 非完全正交设计（7/24 配置）。同意这是一个局限，但 7 配置已覆盖三个轴的主要组合，且结论是 all-zero，正交设计在全零结果下边际收益有限。\n\n**[AGREE] R1-Minor-2**: Appendix D 采样量不对等。与我 R2 小问题 4 一致。\n\n**[AGREE] R1-Minor-3**: Smart Compress 训练细节不完整。Appendix B (Table 4) 缺少 learning rate, optimizer, batch size, warmup schedule 等关键信息，不足以复现。\n\n**[AGREE] R1-Minor-4**: bib 格式问题。与我 R2 小问题 6 一致。\n\n**[AGREE] R1-Minor-5**: \"Performance-neutral\" 表述问题。与我 R2 的 W2 一致。R1 从 \"61.6% 低于 official 87.3%\" 角度切入也是有效的补充。\n\n**[AGREE] R1-Minor-6**: Appendix E speedup 仅 1.06x。与我 R2 的 W2 一致。\n\n---\n\n### Questions 回应\n\n**[AGREE] R1-Q1**: Smart Compress M=128 ≈ official checkpoint 是一个非常好的问题。如上文 N3 回应所述，这暗示 cross-attention module 的 22.2M 额外参数可能本身就是性能提升的主要来源（作为 adapter），而非 \"re-encoding\" 机制本身。\n\n**[AGREE] R1-Q2**: Entropy ratio 仅在 N=2 architectures 上验证，证据力确实弱。从新颖性角度，贡献 2 (\"Mechanistic explanation\") 声称 entropy ratio \"may serve as a preliminary compressibility signal\"（Section 5.1），但 N=2 不足以建立任何预测性 signal。\n\n**[AGREE] R1-Q3**: ACIS scorer 质量是否足够是一个重要问题。论文声称 \"scoring-independent\"（learned = random），但如果 scorer 本身没有学到有效的 importance 排序，这一结论就变成了 \"两种随机方法表现相同\"，不够有信息量。Appendix C 的 offline error 分析可以部分回答——如果 ACIS scoring 在 offline 上确实优于 random（比如 importance margin > 0），但 closed-loop 仍为 0%，则 \"scoring-independent\" 结论成立。\n\n**[REBUT] R1-Q4**: OpenVLA degradation curve 近似线性这一观察本身有趣，但我不认为需要理论预期。经验性发现不一定需要先验理论支撑。论文已经提供了 mechanistic 解释（per-token independence → localized loss → proportional degradation），这作为 post-hoc 解释是足够的。要求作者提供 \"theoretical prediction\" 在审稿标准上偏高。\n\n---\n\n### Missing References 回应\n\n**[REBUT] R1-Missing-1 (RoboFlamingo)**: 重要性中等。RoboFlamingo 确实使用 cross-attention vision connector，但它不是 token pruning/efficiency 工作。作为 vision connector taxonomy 的补充引用可以加，但不是 critical missing reference。\n\n**[REBUT] R1-Missing-2 (SPA-VL)**: 需要确认是否存在。R1 标注 \"或其他 VLM token pruning closed-loop 评估\"，说明不确定具体论文。VLM token pruning 的 closed-loop 评估工作确实稀缺（这也是本文的卖点之一）。\n\n**[AGREE] R1-Missing-3 (TinyVLA)**: TinyVLA 作为 small-scale VLA 参考值得引用，但优先级低于我 R2 报告中指出的 5-7 篇直接竞争工作。\n\n**补充**: R1 的 missing references 遗漏了更关键的缺失——我在 R2 报告中已详细列出的 \"Don't Run with Scissors\"、Compressor-VLA、SpecPrune-VLA、LightVLA、\"See What Matters\" 等 5-7 篇直接相关工作。这些比 R1 列出的 3 篇缺失更严重地影响论文 positioning。\n\n---\n\n### 综合评估\n\nR1 的审查质量很高，对实验方法论的分析细致入微。R1 的 Must-Fix 问题（scale confound、multi-seed、baseline reproduction）与我 R2 的 Must-Fix 问题（missing references、Smart Compress 新颖性、\"first\" claim）形成互补——两者共同指向一个判断：**论文的实证发现有价值，但当前的 claim strength 和 positioning 都超出了证据支撑的范围**。\n\nR1 给 3/5 (Borderline)，我给 5/10 (Borderline Reject)。考虑 R1 的实验问题如何影响新颖性判断：\n- N1（scale confound）使 Contribution 1 的因果 claim 不成立 → 核心新颖性降级\n- N3（baseline 偏低）使 Smart Compress 的 generality 存疑 → Contribution 3 可信度降低\n- N2（2 seeds）使 \"flat across M\" 结论证据不足 → re-encoding 叙事不稳固\n\n**结合 R1 的实验问题和我的新颖性/完整性问题，我维持 5/10 (Borderline Reject) 不变。** 如果作者在 rebuttal 中能 (1) 补充遗漏引用并重新 position，(2) 在 official checkpoint 上运行 Smart Compress，(3) 弱化因果 claim，论文有望提升至 weak accept。\n",
  "reviewer_id": "2",
  "project": "importance_margin_vla_compress"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "\n## Reviewer 2 — 交叉回应 Reviewer 1 意见\n\n---\n\n### Must-Fix 逐条回应\n\n**[AGREE] R1-N1: Scale confound 未充分解决，因果 claim 过强**\n\n同意 R1 的核心判断。从新颖性角度补充：这一 confound 不仅是统计问题，直接削弱了论文的核心贡献 claim。Contribution 1 (\"Architecture-dependent compressibility\") 的价值建立在 \"connector design shapes compressibility\" 这一因果链上。如果 scale 是主要解释变量，那么整篇论文的叙事线从 Introduction ¶3 到 Conclusion 都需要重写。\n\nR1 对四条论据的逐条评估我基本同意，补充一点：论据 (3)（entropy ratio）的循环论证风险比 R1 描述的更严重。Section 5.1 用 entropy ratio 来\"解释\"为什么 pixel-shuffle 不可剪枝，但 entropy ratio 本身是 pixel-shuffle 架构的直接产物（均匀信息密度 → 均匀 attention），不构成独立证据。这就像用\"水是湿的\"来解释\"水能弄湿东西\"。\n\nR1 建议改 \"attributable to\" 为 \"associated with\" 合理。从写作质量角度，Abstract 中 \"compressibility is attributable to the vision connector design\" 和 Conclusion 中 \"Compressibility is attributable to the vision connector\" 都是过强的因果断言（Section 5.3 标题本身就是 \"Disentangling Connector from Scale\"，承认了这是未解决的问题）。\n\n---\n\n**[AGREE] R1-N2: Multi-seed 仅 2 seeds，统计不可靠**\n\n完全同意。2 seeds 不仅无法计算可靠方差（R1 指出 df=1），而且 M=96 的 5.6pp half-range（52.6% vs 58.2%）实际上是所有配置中最大的，论文却在 Table 8 caption 中声称 \"All configurations show low variance across seeds\"（Appendix, Table 8）。这是 selective reporting。\n\n从新颖性影响角度：如果 Smart Compress 的性能方差实际较大（3-5 seeds 可能揭示），那么 \"flat across {32, 64, 128}\" 的核心发现——即 \"gain comes from re-encoding, not compression\"——的证据力将减弱。这直接影响贡献 claim 3 的可信度。\n\n---\n\n**[AGREE with nuance] R1-N3: Baseline reproduction 严重偏低**\n\n同意这是显著问题，但需要区分两个层面：\n\n**同意的部分**：44.8% vs 87.3% 的差距确实很大，且 footnote（Section 4.1, footnote 1）仅说 \"smaller batch due to compute constraints\"，没有给出具体 batch size。Smart Compress 在 underfitting baseline 上的改善可能不能外推到正常训练模型。R1 建议在 official checkpoint 上运行 Smart Compress 很合理。\n\n**需要补充的部分**：论文实际在 official checkpoint (59.2% SR) 上也做了 pruning 实验（Table 1 最后两行），结果同样 0% SR，这部分验证了 cliff-edge 的 robustness。但 Smart Compress 确实只在 44.8% baseline 上评估过。从新颖性角度看，如果 Smart Compress 在 59.2% baseline 上也有效（比如达到 ~75%），那将是更有说服力的贡献；反之，如果失效，则 Smart Compress 的 claim 大幅缩水。这一实验缺失使得贡献 3 的 generality 无法评估。\n\n另外值得注意：R1 的 Question 1 提出 Smart Compress M=128 (59.8%) ≈ official checkpoint (59.2%)，暗示 cross-attention 可能只是替代 large-batch training 的效果。这是一个非常敏锐的观察。Section 4.3 的 extended training control (45.0%) 排除了 \"额外训练步数\" 的解释，但没有排除 \"额外参数容量\" 的解释——22.2M 参数的 cross-attention module 可能本身就像一个额外的 adapter，其效果与 re-encoding 无关。\n\n---\n\n### Should-Fix 逐条回应\n\n**[AGREE] R1-W1: 仅 LIBERO simulation 评估**\n\n同意。从 CoRL 社区角度，simulation-only 评估对于声称 \"deployment benefit\" 的论文是明显不足的。Abstract 和 Introduction 使用 \"deployment benefit\" 这一措辞（Abstract: \"a performance-neutral deployment benefit\"），暗示了实际部署价值，但全部实验都在 simulation 中完成。我在 R2 报告中也指出了 \"performance-neutral deployment benefit\" 措辞的问题。\n\n---\n\n**[AGREE] R1-W2: OpenVLA 实验不对称，缺少 learned pruning**\n\n同意。SmolVLA 有 7 种配置（learned + random × multiple k × multiple mechanisms），OpenVLA 仅有 random pruning。这一不对称使得跨架构对比不完全公平：SmolVLA 的 0% 结论覆盖了所有可能的 pruning 方法，但 OpenVLA 的 graceful degradation 仅在最简单的 random removal 下验证。如果在 OpenVLA 上用 learned pruning（如 FastV 或 attention-based scoring），degradation curve 可能更平缓或更陡——两种方向都影响论文结论。\n\n从新颖性角度：这削弱了 \"architecture-dependent compressibility\" 发现的精度。当前证据只能支持 \"SmolVLA 在所有方法下崩溃，OpenVLA 在 random removal 下优雅退化\"，不能支持更一般的 \"MLP projectors degrade gracefully under any pruning\"。\n\n---\n\n**[AGREE] R1-W3: M=96 performance dip 未解释**\n\n同意。Table 2 中 M=96 (52.6%) 显著低于 M=64 (61.6%) 和 M=128 (59.8%)，打破了 \"flat across {32, 64, 128}\" 的叙事。论文完全没有讨论这一异常。从写作质量角度，这是 selective reporting 的典型案例——Table 2 caption 说 \"Performance is flat across M ∈ {32, 64, 128}\"，通过排除 M=96 来维持叙事。审稿人会注意到这一点。\n\nM=96 的多 seed 结果（55.4% ± 2.8）也是方差最大的配置，进一步说明 \"flat\" 结论的证据不足。\n\n---\n\n**[AGREE] R1-W4: Offline metric disconnect 论证不完整**\n\n同意。Section 5.4 声称 \"Offline evaluation metrics provide misleadingly positive signals\"，但正文中没有展示这些 \"misleadingly positive\" 的 offline metric 数值。Appendix C (Table 5) 展示了 single-step action error（3.4x 增加），但这是 \"misleadingly negative\" 而非 \"misleadingly positive\"。论文实际需要展示的是：某个 offline metric 看起来合理（比如 mean action error 小），但 closed-loop 却崩溃。当前论证存在逻辑缺口。\n\n---\n\n**[AGREE] R1-W5: Smart Compress 跨任务 generalization 下降未充分讨论**\n\n同意，与我 R2 报告中 W3 一致。LIBERO-Goal 从 63.0% 降到 56.4%（-6.6pp）不应被淡化。\n\n---\n\n### Minor Issues 回应\n\n**[AGREE] R1-Minor-1**: Table 1 非完全正交设计（7/24 配置）。同意这是一个局限，但 7 配置已覆盖三个轴的主要组合，且结论是 all-zero，正交设计在全零结果下边际收益有限。\n\n**[AGREE] R1-Minor-2**: Appendix D 采样量不对等。与我 R2 小问题 4 一致。\n\n**[AGREE] R1-Minor-3**: Smart Compress 训练细节不完整。Appendix B (Table 4) 缺少 learning rate, optimizer, batch size, warmup schedule 等关键信息，不足以复现。\n\n**[AGREE] R1-Minor-4**: bib 格式问题。与我 R2 小问题 6 一致。\n\n**[AGREE] R1-Minor-5**: \"Performance-neutral\" 表述问题。与我 R2 的 W2 一致。R1 从 \"61.6% 低于 official 87.3%\" 角度切入也是有效的补充。\n\n**[AGREE] R1-Minor-6**: Appendix E speedup 仅 1.06x。与我 R2 的 W2 一致。\n\n---\n\n### Questions 回应\n\n**[AGREE] R1-Q1**: Smart Compress M=128 ≈ official checkpoint 是一个非常好的问题。如上文 N3 回应所述，这暗示 cross-attention module 的 22.2M 额外参数可能本身就是性能提升的主要来源（作为 adapter），而非 \"re-encoding\" 机制本身。\n\n**[AGREE] R1-Q2**: Entropy ratio 仅在 N=2 architectures 上验证，证据力确实弱。从新颖性角度，贡献 2 (\"Mechanistic explanation\") 声称 entropy ratio \"may serve as a preliminary compressibility signal\"（Section 5.1），但 N=2 不足以建立任何预测性 signal。\n\n**[AGREE] R1-Q3**: ACIS scorer 质量是否足够是一个重要问题。论文声称 \"scoring-independent\"（learned = random），但如果 scorer 本身没有学到有效的 importance 排序，这一结论就变成了 \"两种随机方法表现相同\"，不够有信息量。Appendix C 的 offline error 分析可以部分回答——如果 ACIS scoring 在 offline 上确实优于 random（比如 importance margin > 0），但 closed-loop 仍为 0%，则 \"scoring-independent\" 结论成立。\n\n**[REBUT] R1-Q4**: OpenVLA degradation curve 近似线性这一观察本身有趣，但我不认为需要理论预期。经验性发现不一定需要先验理论支撑。论文已经提供了 mechanistic 解释（per-token independence → localized loss → proportional degradation），这作为 post-hoc 解释是足够的。要求作者提供 \"theoretical prediction\" 在审稿标准上偏高。\n\n---\n\n### Missing References 回应\n\n**[REBUT] R1-Missing-1 (RoboFlamingo)**: 重要性中等。RoboFlamingo 确实使用 cross-attention vision connector，但它不是 token pruning/efficiency 工作。作为 vision connector taxonomy 的补充引用可以加，但不是 critical missing reference。\n\n**[REBUT] R1-Missing-2 (SPA-VL)**: 需要确认是否存在。R1 标注 \"或其他 VLM token pruning closed-loop 评估\"，说明不确定具体论文。VLM token pruning 的 closed-loop 评估工作确实稀缺（这也是本文的卖点之一）。\n\n**[AGREE] R1-Missing-3 (TinyVLA)**: TinyVLA 作为 small-scale VLA 参考值得引用，但优先级低于我 R2 报告中指出的 5-7 篇直接竞争工作。\n\n**补充**: R1 的 missing references 遗漏了更关键的缺失——我在 R2 报告中已详细列出的 \"Don't Run with Scissors\"、Compressor-VLA、SpecPrune-VLA、LightVLA、\"See What Matters\" 等 5-7 篇直接相关工作。这些比 R1 列出的 3 篇缺失更严重地影响论文 positioning。\n\n---\n\n### 综合评估\n\nR1 的审查质量很高，对实验方法论的分析细致入微。R1 的 Must-Fix 问题（scale confound、multi-seed、baseline reproduction）与我 R2 的 Must-Fix 问题（missing references、Smart Compress 新颖性、\"first\" claim）形成互补——两者共同指向一个判断：**论文的实证发现有价值，但当前的 claim strength 和 positioning 都超出了证据支撑的范围**。\n\nR1 给 3/5 (Borderline)，我给 5/10 (Borderline Reject)。考虑 R1 的实验问题如何影响新颖性判断：\n- N1（scale confound）使 Contribution 1 的因果 claim 不成立 → 核心新颖性降级\n- N3（baseline 偏低）使 Smart Compress 的 generality 存疑 → Contribution 3 可信度降低\n- N2（2 seeds）使 \"flat across M\" 结论证据不足 → re-encoding 叙事不稳固\n\n**结合 R1 的实验问题和我的新颖性/完整性问题，我维持 5/10 (Borderline Reject) 不变。** 如果作者在 rebuttal 中能 (1) 补充遗漏引用并重新 position，(2) 在 official checkpoint 上运行 Smart Compress，(3) 弱化因果 claim，论文有望提升至 weak accept。\n",
    "reviewer_id": "2",
    "project": "importance_margin_vla_compress"
  }
}
```

</details>

---


### Tool result

_source line 169 · 2026-05-19T01:23:41.490421+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4221
}
```

</details>

---


### Assistant

_source line 170 · 2026-05-19T01:23:47.225297+00:00_

交叉回应已提交。

核心结论：R1 的实验严谨性问题和我的新颖性/完整性问题形成互补，共同指向论文 claim 超出证据支撑范围。对 R1 的 3 个 Must-Fix 全部 AGREE（补充了新颖性影响分析），仅对 Q4（要求理论预期）和 Missing References 中 RoboFlamingo、SPA-VL 提出 REBUT。维持 5/10 评分不变。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2"
}
```

</details>

---


## Round 5

## Round 5

62 recorded events


### User

_source line 171 · 2026-05-19T05:45:59.631524+00:00_

[Round 1 审稿请求]:
## Round 1 审稿任务 — Reviewer 2

### 你的审查侧重：新颖性 + 相关工作完整性 + 论文定位 + 写作质量

### Venue 信息
- **目标会议**：CoRL 2026 (Conference on Robot Learning)
- **Deadline**：2026-05-29
- **页数限制**：8 页正文（acknowledgments + references + appendix 不计）
- **模板**：CoRL 2026 官方 LaTeX 模板
- **匿名规则**：Double-blind（论文不得包含作者身份信息）
- **附录**：可选，reviewer 不要求阅读（但鼓励阅读）
- **必须包含**：Limitations section（计入 8 页限制内）
- **补充材料**：鼓励 video（≤250MB, ≤3min）、code、data

### 论文路径
- 主文件：`projects/importance_margin_vla_compress/docs/paper/main.tex`
- 各 section 在同目录下的 .tex 文件
- 参考文献：`references.bib`

### 论文概要
标题：Why Token Pruning Crashes Some Robot Policies but Not Others: The Role of Vision Connectors in VLA Token Compressibility

研究 VLA 模型中 vision token pruning 的架构依赖性。核心发现：pixel-shuffle connector (SmolVLA) 在任何 pruning 下 cliff-edge 崩溃 (59.2% → 0%)，MLP projector (OpenVLA) 则 graceful degradation (74.0% → 37.4%)。提出 attention entropy ratio 作为 compressibility signal，并用 cross-attention re-encoding (Smart Compress) 诊断性实验验证 re-encoding > deletion。

### 你需要重点审查的方面

1. **新颖性评估**
   - 核心发现（architecture-dependent compressibility）相对于已有工作的 incremental value
   - Smart Compress 与 Q-Former / Perceiver / Compressor-VLA 等已有 cross-attention 方法的区别
   - Attention entropy ratio 作为 compressibility signal 的新颖度
   - "First systematic comparison" claim 是否成立——检查 VLA-IAP, EfficientVLA, SpecPrune-VLA, See What Matters 等是否已做类似评估

2. **相关工作完整性**
   - 引用是否覆盖所有直接相关方法、baseline 论文、benchmark 论文
   - 特别检查：Compressor-VLA（cross-attention on OpenVLA-OFT, LIBERO 97.1% SR）、SpecPrune-VLA、LightVLA、See What Matters（concurrent, SmolVLA 上做 continuous resampling）
   - 相关工作的 positioning 是否准确——对已有工作的描述是否公平
   - 是否遗漏 weight pruning / structured pruning 方面的 VLA 工作

3. **论文定位与 Framing**
   - Contribution 是否 well-defined：empirical finding vs method contribution 的边界
   - Abstract 和 Introduction 的叙事是否 compelling
   - "Cliff-edge" 发现是否被适当 contextualize（而非过度宣传）
   - 论文整体主线是否统一（abstract → intro → method → results → analysis → conclusion）

4. **写作质量**
   - 是否有 AI 写作痕迹（破折号、-ing phrases、过度分段）
   - 术语首次使用时是否有定义
   - 图表信息密度和视觉质量
   - 全文逻辑连贯性

5. **CoRL 适配性**
   - 仅 simulation 评估（LIBERO）对 CoRL 的适配度（CoRL 偏好 real robot）
   - Limitations section 是否充分
   - 对 robot learning community 的实际贡献

请按 CoRL 审稿标准出具完整审稿意见，包含：Strengths, Weaknesses (分 Must-Fix / Should-Fix / Nice-to-Have), Questions, Missing References, Overall Assessment (strong reject / weak reject / borderline / weak accept / strong accept) + 置信度。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 172 · 2026-05-19T05:46:08.502080+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebSearch,WebFetch,mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director,mcp__agent-ml-research__verify_references",
  "max_results": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebSearch,WebFetch,mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director,mcp__agent-ml-research__verify_references",
    "max_results": "5"
  }
}
```

</details>

---


### Tool result

_source line 173 · 2026-05-19T05:46:08.502480+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 174 · 2026-05-19T05:46:11.466337+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "CoRL 2026 reviewer guidelines review form criteria"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "CoRL 2026 reviewer guidelines review form criteria"
  }
}
```

</details>

---


### Tool call

_source line 175 · 2026-05-19T05:46:12.370793+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "CoRL 2025 2026 review form scoring rubric dimensions"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "CoRL 2025 2026 review form scoring rubric dimensions"
  }
}
```

</details>

---


### Tool call

_source line 176 · 2026-05-19T05:46:13.877682+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper"
  }
}
```

</details>

---


### Tool result

_source line 177 · 2026-05-19T05:46:14.179310+00:00_

/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/sections/analysis.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/sections/background.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/sections/experimental_setup.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/sections/results_draft.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/sections/analysis_draft.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/background.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/discussion.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/experiments_deprecated.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/sections/experiments.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/main.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/sections/related_work_draft.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/sections/introduction.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/abstract.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/analysis.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/experimental_setup.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/conclusion.tex
/home/ubuntu/.agent-ml
…[truncated 444 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Glob",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 178 · 2026-05-19T05:46:14.179797+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.bib",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.bib",
    "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper"
  }
}
```

</details>

---


### Tool result

_source line 179 · 2026-05-19T05:46:14.331132+00:00_

/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/references.bib

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Glob",
  "elapsed_ms": 151
}
```

</details>

---


### Tool result

_source line 180 · 2026-05-19T05:46:20.458800+00:00_

Web search results for query: "CoRL 2025 2026 review form scoring rubric dimensions"

Links: [{"title":"2025 - 2026 REC SCORING SYSTEM Changes from 2024-2025 Rubric","url":"https://openchampionshipseries.com/wp-content/uploads/2025/06/2025-2026-Rec-Rubric.pdf"},{"title":"2025 - 2026 ALLSTAR PREP SCORING SYSTEM Changes from 2024-2025 Rubric","url":"https://openchampionshipseries.com/wp-content/uploads/2025/06/2025-2026-Prep-Rubric-3-13-25.pdf"},{"title":"VERSION 03.18.25 2025 - 2026 UNITED SCORING SYSTEM Scoring Rubric PERFORMANCE","url":"https://www.varsity.com/wp-content/uploads/2025/04/25-26-United-Scoring-Rubric-Performance-Advanced.pdf"},{"title":"VERSION 3.18.25 2025 - 2026 UNITED SCORING SYSTEM Chile Scoring Rubric","url":"https://www.unitedscoringpartners.com/wp-content/uploads/2025/04/25-26-United-Scoring-Rubric-All-Star-Novice.pdf"},{"title":"VERSION 6.15.24 2025 - 2026 UNITED SCORING SYSTEM UK Scoring Rubric","url":"https://www.unitedscoringpartners.com/wp-content/uploads/2025/06/25-26-United-Scoring-Rubric-Prep-and-Adaptive-Abilities-UK.pdf"},{"title":"Rethinking Rubric Generation for Improving LLM Judge and Reward Modeling for Open-ended Tasks","url":"https://arxiv.org/pdf/2602.05125"},{"title":"CoRL 2025 Accepted Paper List - Paper Copilot","url":"https://papercopilot.com/paper-list/corl-paper-list/corl-2025-paper-list/"},{"title":"What Drives Paper Acceptance? A Process-Centric Analysis of Modern Peer Review","url":"https://arxiv.org/pdf/2509.25701"},{"title":"Auto-Rubric: Learning From Implicit Weights to Explicit Rubrics for Reward Modeling","url":"https://arxiv.org/pdf/2510.17314"}]

Based on the search results, I found information about cheerleading scoring rubrics for 2025-2026, but not specifically about "CoRL" as a review form. The results show information about United Scoring System and Open Championship Series (OCS) rubrics for cheer competitions.

However, the search did return results about academic conference review processes (ICLR, CoRL as
…[truncated 826 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 8088
}
```

</details>

---


### Tool result

_source line 181 · 2026-05-19T05:46:24.832102+00:00_

Web search results for query: "CoRL 2026 reviewer guidelines review form criteria"

Links: [{"title":"CoRL 2026 - Instruction for Authors","url":"https://www.corl.org/contributions/instruction-for-authors"},{"title":"ICLR 2026 Reviewer Guide","url":"https://iclr.cc/Conferences/2026/ReviewerGuide"},{"title":"CoRL 2026 - Call for Papers","url":"https://www.corl.org/contributions/call-for-papers"},{"title":"Reviewer Guidelines — CoRL 2023","url":"https://www.corl2023.org/reviewer-guidelines"},{"title":"CVPR 2026 Reviewer Guidelines","url":"https://cvpr.thecvf.com/Conferences/2026/ReviewerGuidelinesq"},{"title":"Which Coauthor Should I Nominate in My 99 ICLR Submissions? A Mathematical Analysis of the ICLR 2026 Reciprocal Reviewer Nomination Policy","url":"https://arxiv.org/pdf/2512.17950"},{"title":"CoRL 2024 - Instruction for Reviews","url":"https://2024.corl.org/contributions/instruction-for-reviews"}]

Based on the search results, I found some information about CoRL 2026, though the specific detailed review form criteria for 2026 wasn't fully available in the results. Here's what I found:

## CoRL 2026 Reviewer Information

All submissions must include at least one author who agrees to serve as a CoRL reviewer, and they are qualified if they have at least one accepted publication at a previous robotics (CoRL/ICRA/IROS/RSS) or learning conference (ICLR/NeurIPS/ICML) or equivalent journal.

## Review Criteria

The search results included CoRL 2024 review criteria which likely remains similar for 2026. Submissions will be evaluated based on the significance and novelty of the results, either theoretical or empirical. Additionally, all CoRL submissions must demonstrate the relevance to Robot Learning through either explicitly addressing a learning question for physical robots or testing the proposed learning solution on physical robots.

Based on the CoRL 2023 guidelines (which may be relevant for 2026), key review criteria also include:

- Relevance: whether the paper 
…[truncated 547 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 13365
}
```

</details>

---


### Tool call

_source line 182 · 2026-05-19T05:46:30.226709+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://2024.corl.org/contributions/instruction-for-reviews",
  "prompt": "Extract the complete review form criteria, scoring dimensions, rating scales, and any specific guidelines for reviewers. Include all rating questions and their scales."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://2024.corl.org/contributions/instruction-for-reviews",
    "prompt": "Extract the complete review form criteria, scoring dimensions, rating scales, and any specific guidelines for reviewers. Include all rating questions and their scales."
  }
}
```

</details>

---


### Tool call

_source line 183 · 2026-05-19T05:46:31.182205+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://www.corl2023.org/reviewer-guidelines",
  "prompt": "Extract the complete review criteria, scoring dimensions, rating scales, and specific guidelines for CoRL reviewers. Include all evaluation dimensions."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://www.corl2023.org/reviewer-guidelines",
    "prompt": "Extract the complete review criteria, scoring dimensions, rating scales, and specific guidelines for CoRL reviewers. Include all evaluation dimensions."
  }
}
```

</details>

---


### Tool call

_source line 184 · 2026-05-19T05:46:31.634416+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 185 · 2026-05-19T05:46:32.538823+00:00_

1	\documentclass{article}
2	
3	\usepackage{corl_2026} % Submission version: anonymous, line numbers enabled.
4	% \usepackage[final]{corl_2026} % Uncomment for camera-ready.
5	
6	\usepackage{amsmath,amssymb}
7	\usepackage{graphicx}
8	\usepackage{booktabs}
9	\usepackage{enumitem}
10	\usepackage{subcaption}
11	
12	\title{Why Token Pruning Crashes Some Robot Policies but Not Others:\\The Role of Vision Connectors in VLA Token Compressibility}
13	
14	\begin{document}
15	\maketitle
16	
17	\input{abstract}
18	
19	\keywords{vision-language-action models, token pruning, robot learning}
20	
21	\input{introduction}
22	
23	\input{related_work}
24	
25	\input{experimental_setup}
26	
27	\input{results}
28	
29	\input{analysis}
30	
31	\input{conclusion}
32	
33	\bibliography{references}
34	
35	\input{appendix}
36	
37	\end{document}
38	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 904
}
```

</details>

---


### Tool call

_source line 186 · 2026-05-19T05:46:32.539256+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 187 · 2026-05-19T05:46:33.041379+00:00_

1	\begin{abstract}
2	Vision token pruning reliably accelerates Vision Transformer (ViT) inference with negligible accuracy loss, prompting recent proposals to apply the same technique to Vision-Language-Action (VLA) models for faster robotic control. We conduct the first systematic comparison of how vision connector design affects token pruning sensitivity in closed-loop VLA control and find that compressibility is strongly linked to the vision connector design. SmolVLA, whose pixel-shuffle connector spatially folds patches into high-density tokens, exhibits a cliff-edge failure: pruning collapses success rate from 59.2\% to 0\% on the official checkpoint, with even 5\% token removal (7 of 128) causing complete task failure. This failure is robust across two checkpoints of different training quality, seven pruning configurations, and three pruning mechanisms. OpenVLA, whose MLP projector maps patches independently, degrades gracefully: at $k{=}0.95$ it retains 69.4\% SR ($-4.6$pp) where SmolVLA drops to 0\%. We trace the divergence to token information density: pixel-shuffle produces tokens with near-uniform attention across all transformer layers, while MLP-projected tokens develop progressively selective attention in deeper layers. A diagnostic experiment confirms that learned re-encoding succeeds where all deletion methods fail: a cross-attention module raises success rate above the uncompressed baseline even at 75\% token reduction, and a passthrough control isolates re-encoding as the causal factor. Our experiments on SmolVLA and OpenVLA, together with recent findings on CogACT, reveal a consistent pattern across three models spanning two connector families: VLA token compressibility is architecture-dependent, and cross-attention re-encoding can overcome failures that all deletion-based methods share.
3	\end{abstract}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 188 · 2026-05-19T05:46:33.092129+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 189 · 2026-05-19T05:46:33.293447+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	Vision token pruning is one of the most reliable efficiency techniques in Vision Transformer (ViT) inference: DynamicViT~\cite{rao2021dynamicvit} removes 66\% of tokens with $<$0.5\% accuracy loss, ToMe~\cite{bolya2023tome} merges 40\% at $>$99\% accuracy, and EViT~\cite{liang2022evit} discards 50\% with negligible degradation. These results have established a strong prior that vision tokens are highly redundant. Vision-Language-Action (VLA) models~\cite{brohan2023rt1,brohan2023rt2,kim2024openvla,black2024pi0,ghosh2024octo,shukor2025smolvla} use the same ViT encoders, producing hundreds of tokens that dominate the LLM backbone's input. For real-time robotic control at 5--10 Hz, reducing these tokens would yield immediate speedups in the quadratically scaling attention computation. Several recent works explore this direction: FastV~\cite{chen2024fastv} prunes inattentive VLM tokens, VLA-Cache~\cite{xu2025vlacache} caches vision tokens across timesteps, and VLA-IAP~\cite{cheng2026vlaiap} proposes importance-aware VLA pruning. We show that this assumption can fail catastrophically: on SmolVLA, removing just 5\% of vision tokens (7 of 128) crashes the policy from 59\% task success to zero.
5	
6	No prior work has systematically evaluated how vision token reduction behaves across different VLA architectures in closed-loop control, where a single corrupted action can push the robot off-trajectory and subsequent errors compound irrecoverably. Existing evaluations rely on offline metrics (action loss, perplexity) that average over independent timesteps and fail to capture this compounding failure mode.
7	
8	We conduct the first systematic comparison of how vision connector design affects token pruning sensitivity in closed-loop VLA control. On SmolVLA (451.5M parameters, pixel-shuffle connector), seven pruning configurations spanning scoring function, retention ratio ($k \in \{0.5, 0.7, 0.9, 0.95\}$), and mechanism (ze
…[truncated 2313 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 190 · 2026-05-19T05:46:33.293798+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 191 · 2026-05-19T05:46:33.344297+00:00_

1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{Vision token efficiency.}
5	Token pruning in ViTs is well established: DynamicViT~\cite{rao2021dynamicvit}, EViT~\cite{liang2022evit}, and ToMe~\cite{bolya2023tome} consistently remove 30--60\% of tokens with $<$1\% accuracy loss on ImageNet. For VLMs, FastV~\cite{chen2024fastv} and LLaVA-PruMerge~\cite{shang2024prumerge} extend pruning to language-vision tasks. We test whether these results transfer to closed-loop VLA control, where action errors compound across timesteps.
6	
7	\paragraph{VLA-specific token reduction.}
8	VLA-Cache~\cite{xu2025vlacache} caches vision KV states across timesteps for 1.7$\times$ speedup without removing tokens. VLA-IAP~\cite{cheng2026vlaiap} uses interaction-aligned pruning on OpenVLA; EfficientVLA~\cite{yang2025efficientvla} combines layer pruning and token selection on CogACT; VLA-Pruner~\cite{liu2025vlapruner} uses dual-level importance criteria for temporal-aware pruning. All evaluate on MLP-projector architectures. None reports the cliff-edge failure we observe on pixel-shuffle VLAs; their positive results may not generalize to spatially entangled connectors.
9	
10	\paragraph{Vision connectors.}
11	Per-patch MLP projectors~\cite{liu2023llava,kim2024openvla} preserve per-token granularity. Cross-attention connectors (Q-Former~\cite{li2023blip2}, Perceiver~\cite{alayrac2022flamingo,jaegle2021perceiver}, RoboFlamingo~\cite{li2024roboflamingo}) compress to learned queries at the architectural level. Pixel-shuffle connectors~\cite{shi2016subpixel,shukor2025smolvla,chen2024internvl} fold patches via channel concatenation, achieving training-time compression but creating inter-token dependencies. Our analysis links this taxonomy to inference-time compressibility and shows that cross-attention re-encoding can overcome the failure mode of deletion on pixel-shuffle architectures.
12	
13	\paragraph{VLA token compression.}
14	Recent concurrent works achieve efficient token co
…[truncated 1153 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 192 · 2026-05-19T05:46:34.298671+00:00_

# CoRL 2024 Review Criteria Summary

Based on the provided content, here's what was specified:

## Review Evaluation Criteria

Papers are assessed on:
- **Significance and novelty** of results (theoretical or empirical)
- **Objective establishment** of results and potential for "scientific and technological impact"
- **Relevance to robotic learning**

The conference welcomes papers combining experimental and theoretical contributions relevant to robot learning.

## Important Limitation

**No detailed review form, scoring dimensions, rating scales, or specific reviewer guidance questions appear in this document.** The page contains only high-level evaluation principles and desk-rejection criteria, not the actual review questionnaire or numerical rating systems reviewers would use.

## Desk Rejection Criteria

Papers can be rejected for:
1. **Formatting issues** (length or format violations)
2. **Anonymity violations** (author identification)
3. **Scope issues** - submissions must demonstrate robot learning relevance through either "Intent: Explicitly address a learning question for physical robots OR Outcome: Test the proposed learning solution on physical robots"

## Reviewer Qualifications

Reviewers should have expertise demonstrated by minimum 3 first-author publications in major robotics and machine learning venues.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 4071
}
```

</details>

---


### Tool result

_source line 193 · 2026-05-19T05:46:37.211405+00:00_

# CoRL 2023 Reviewer Guidelines: Evaluation Criteria

## Primary Review Dimensions

CoRL reviewers evaluate submissions across six key dimensions:

**Originality:** Assesses whether problems or methods are novel, examining if the work represents "a novel combination of well-known techniques" and clarifying differentiation from prior work with adequate citations.

**Quality:** Evaluates technical soundness, whether "claims well supported (e.g., by theoretical analysis or experimental results)" and whether work represents completion versus progress.

**Clarity:** Judges written presentation quality and organization, ensuring "a well written paper provides enough information for an expert reader to reproduce its results."

**Significance:** Determines if results matter and whether the work "advance[s] the state of the art in a demonstrable way."

**Relevance:** Focuses on robot learning applicability, whether papers "apply or improve a learning-based method, or a learned model" and appeal to the CoRL audience.

**Limitations:** Recognizes that "CoRL papers are required to include a limitations section," treating honestly-reported limitations positively while penalizing unreported shortcomings.

## Scoring Philosophy

The guidelines emphasize avoiding common reviewer mistakes, noting that papers need not publish code/datasets, include theorems, use real robots, or outperform SOTA for acceptance—provided they offer novel perspectives and genuine knowledge advancement.

Reviewers should be "constructive" and "concrete," starting positively and supporting critiques with evidence.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 6029
}
```

</details>

---


### Tool call

_source line 194 · 2026-05-19T05:46:40.424167+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/background.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/background.tex"
  }
}
```

</details>

---


### Tool result

_source line 195 · 2026-05-19T05:46:41.328533+00:00_

1	% background.tex -- Section 2: Background
2	
3	\section{Background}
4	\label{sec:background}
5	
6	This section describes the architectures and benchmark used in our study: SmolVLA~\cite{shukor2025smolvla} and OpenVLA~\cite{kim2024openvla}, two VLA models with contrasting vision connector designs, and the LIBERO benchmark~\cite{liu2023libero} on which we evaluate closed-loop performance.
7	
8	\subsection{SmolVLA Architecture}
9	\label{sec:smolvla_arch}
10	
11	Vision-Language-Action (VLA) models cast robotic control as conditional generation: given a camera observation and a language instruction, the model predicts a continuous action.
12	SmolVLA~\cite{shukor2025smolvla} instantiates this paradigm with approximately 451.5M parameters, organized into a vision encoder, a vision connector, a language model backbone, and an action head.
13	Figure~\ref{fig:architecture} contrasts the vision pipelines of SmolVLA and OpenVLA, highlighting the connector designs that determine compressibility.
14	
15	\begin{figure}[t]
16	\centering
17	\includegraphics[width=\linewidth]{figures/paper/fig_architecture.pdf}
18	\caption{Vision connector comparison. \textbf{Left}: SmolVLA applies $4{\times}4$ pixel-shuffle to fold 1024 SigLIP patches into 64 tokens per camera (128 total), creating dense, spatially entangled representations. \textbf{Right}: OpenVLA uses an MLP projector that maps each patch independently, producing 256 tokens with per-token independence. We hypothesize that this architectural difference is the primary factor governing token compressibility: pixel-shuffle tokens resist any form of deletion, while independently projected tokens allow graded pruning.}
19	\label{fig:architecture}
20	\end{figure}
21	
22	\paragraph{Vision encoder.}
23	SmolVLA uses the Sigmoid Loss for Language-Image Pre-training (SigLIP) encoder~\cite{zhai2023siglip} to process visual input.
24	SigLIP divides each camera image into non-overlapping spatial patches on a $32 \times 32$ grid, producing 1024
…[truncated 6224 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 904
}
```

</details>

---


### Tool call

_source line 196 · 2026-05-19T05:46:41.429469+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/experimental_setup.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/experimental_setup.tex"
  }
}
```

</details>

---


### Tool result

_source line 197 · 2026-05-19T05:46:41.781264+00:00_

1	\section{Experimental Setup}
2	\label{sec:experimental_setup}
3	
4	\subsection{Architectures and Benchmark}
5	\label{sec:setup_overview}
6	
7	We study two VLA architectures whose vision connectors differ in how they map encoder patches to language model input tokens (Figure~\ref{fig:architecture}). SmolVLA~\cite{shukor2025smolvla} (451.5M parameters) encodes each camera image with SigLIP~\cite{zhai2023siglip} into 1024 patches on a $32 \times 32$ grid, then applies a pixel-shuffle connector that folds each $4 \times 4$ block into one token by channel concatenation, producing 64 tokens per camera (128 total from two cameras). Each token encodes 16 spatially contiguous patches; removing one eliminates an entire $4 \times 4$ receptive field with no redundancy. The 128 tokens enter a Qwen2-0.5B backbone~\cite{yang2024qwen2} that generates continuous 7-DoF actions via flow matching~\cite{lipman2023flow}. OpenVLA~\cite{kim2024openvla} (7B parameters) uses DINOv2~\cite{oquab2023dinov2} and SigLIP encoders with a two-layer MLP projector that maps each patch independently into a Llama-2 backbone, producing 256 tokens that preserve per-token independence.
8	
9	\begin{figure}[t]
10	\centering
11	\includegraphics[width=\linewidth]{figures/paper/fig_architecture.pdf}
12	\caption{Vision connector comparison. SmolVLA's pixel-shuffle folds $4{\times}4$ patches into single tokens (128 total, spatially entangled). OpenVLA's MLP projector maps each patch independently (256 tokens, per-token independence).}
13	\label{fig:architecture}
14	\end{figure}
15	
16	We evaluate on LIBERO~\cite{liu2023libero}, a suite of language-conditioned tabletop manipulation tasks with three suites: Object (10 manipulation tasks), Spatial (10 spatial reasoning tasks), and Goal (10 goal-conditioned tasks). Each condition uses 50 episodes per task (500 per suite), evaluated by closed-loop Success Rate (SR) with Wilson 95\% confidence intervals. SmolVLA baselines: 44.8\% (Object), 51.8\% (Spatial), 63.0\% (G
…[truncated 1894 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 351
}
```

</details>

---


### Tool call

_source line 198 · 2026-05-19T05:46:41.781678+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/results.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/results.tex"
  }
}
```

</details>

---


### Tool result

_source line 199 · 2026-05-19T05:46:41.832192+00:00_

1	\section{Results}
2	\label{sec:results}
3	
4	We evaluate token pruning across two VLA architectures on LIBERO-Object~\cite{liu2023libero} (10 tasks, 50 episodes each, 500 total). All success rates include Wilson 95\% confidence intervals.
5	
6	\subsection{SmolVLA: Cliff-Edge Under All Pruning Methods}
7	\label{sec:smolvla_results}
8	
9	The SmolVLA baseline (bypass mode, all 128 vision tokens) achieves 44.8\% SR (224/500, CI [40.5\%, 49.2\%]).\footnote{The official SmolVLA result is 87.3\% SR with batch size 64 on 8 GPUs. Our reproduction uses a smaller batch due to compute constraints.} Table~\ref{tab:smolvla_ablation} reports the full ablation. Every pruning configuration produces 0\% SR (Wilson CI upper bounds $\leq$0.80\%). Three observations make this striking: (1)~\textbf{Scoring-independent}: random selection performs identically to learned ACIS scoring. (2)~\textbf{Ratio-independent}: retaining 95\% of tokens ($k{=}0.95$, removing only 7 of 128) causes the same failure as retaining 50\%. (3)~\textbf{Mechanism-independent}: zero-masking, true removal, and token merging all produce 0\% SR.
10	
11	\begin{table}[t]
12	\centering
13	\small
14	\caption{SmolVLA pruning ablation on LIBERO-Object. All configurations collapse to 0\% SR. The official checkpoint (59.2\% baseline) shows the same cliff-edge.}
15	\label{tab:smolvla_ablation}
16	\begin{tabular}{llccrr}
17	\toprule
18	Scoring & $k$ & Mechanism & SR (\%) & Episodes & Wilson 95\% CI \\
19	\midrule
20	\multicolumn{2}{l}{\textit{Baseline (bypass)}} & -- & 44.8 & 500 & [40.5, 49.2] \\
21	\midrule
22	ACIS & 0.50 & Zero-mask & 0.0 & 500 & [0, 0.76] \\
23	ACIS & 0.70 & Zero-mask & 0.0 & 500 & [0, 0.76] \\
24	ACIS & 0.90 & Zero-mask & 0.0 & 500 & [0, 0.76] \\
25	Random & 0.95 & Zero-mask & 0.0 & 500 & [0, 0.76] \\
26	Random & 0.50 & Zero-mask & 0.0 & 500 & [0, 0.76] \\
27	ACIS & 0.50 & True removal & 0.0 & 500 & [0, 0.80] \\
28	ACIS & 0.50 & Merge (ToMe) & 0.0 & 500 & [0, 0.76] \\
29	\midrule
30	\multicolumn{6}{l}{\
…[truncated 5469 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 200 · 2026-05-19T05:46:42.285495+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/analysis.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/analysis.tex"
  }
}
```

</details>

---


### Tool result

_source line 201 · 2026-05-19T05:46:42.737991+00:00_

1	\section{Analysis and Discussion}
2	\label{sec:analysis}
3	
4	\subsection{Connector Design Shapes Compressibility}
5	\label{sec:pixel_shuffle}
6	
7	The divergence between SmolVLA and OpenVLA traces to their vision connectors. SmolVLA's pixel-shuffle applies $4 \times 4$ spatial folding, so each of its 128 tokens encodes 16 patches via channel concatenation. Removing any token eliminates an entire receptive field with no redundancy from neighbors (Figure~\ref{fig:pixel_shuffle}). Because the folding is fixed and non-learned, no downstream layer can recover discarded information. OpenVLA's MLP projector maps each patch independently: removing one of 256 tokens discards $\sim$1/256 of the visual field, a localized loss that self-attention layers can partially compensate. At $k{=}0.50$, OpenVLA retains 37.4\% SR against a 74.0\% baseline; SmolVLA collapses to 0\% even at $k{=}0.95$.
8	
9	\begin{figure}[t]
10	\centering
11	\includegraphics[width=0.85\linewidth]{figures/paper/fig_pixel_shuffle.pdf}
12	\caption{Pixel-shuffle folding: each $4{\times}4$ block of SigLIP patches is channel-concatenated into one token. Removing any token eliminates its receptive field (gray) with no redundancy.}
13	\label{fig:pixel_shuffle}
14	\end{figure}
15	
16	The attention entropy ratio quantifies this structural difference. We measure normalized Shannon entropy of attention weights on vision tokens (1.0 = uniform, lower = selective). SmolVLA's ratio is 0.95, near-uniform across all 16 layers (range 0.93--0.98, total variation 0.05). OpenVLA's overall ratio is 0.64, with progressive sharpening from 0.98 in layer 0 to 0.48 in layer 29 (total variation 0.50, $10\times$ SmolVLA's; see Figure~\ref{fig:entropy_layers} and Appendix~\ref{app:entropy_details}). This reflects fundamentally different information structures: pixel-shuffle tokens are uniformly information-dense and resist selective attention at every processing depth, while MLP-projected tokens allow the model to learn spatial select
…[truncated 5906 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 202 · 2026-05-19T05:46:42.738411+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 203 · 2026-05-19T05:46:43.190322+00:00_

1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	We presented the first systematic comparison of how vision connector design affects token pruning sensitivity in closed-loop VLA control. Compressibility is strongly linked to the vision connector: pixel-shuffle connectors create spatially entangled tokens that collapse under any form of deletion (59.2\% $\to$ 0\% on the official checkpoint), while MLP projectors degrade gracefully (74.0\% $\to$ 37.4\%). The attention entropy ratio (0.95 vs.\ 0.64) captures this divergence, supported by concurrent findings from EfficientVLA~\cite{yang2025efficientvla} across three models and two connector families. For architectures where pruning fails, cross-attention re-encoding raises SR from 44.8\% to $\sim$60\% (a matched training-only control confirms the gain is architectural), and compression to 32 queries (75\% token reduction) preserves this gain at 61.6\%: re-encoding succeeds where deletion cannot. Standard offline metrics do not predict these closed-loop outcomes; closed-loop evaluation is essential for validating VLA compression. Code and evaluation scripts will be released upon publication.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 451
}
```

</details>

---


### Tool call

_source line 204 · 2026-05-19T05:46:43.240920+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 205 · 2026-05-19T05:46:43.291810+00:00_

1	\appendix
2	
3	\section{Per-Task Breakdown Tables}
4	\label{app:per_task}
5	
6	\subsection{SmolVLA Baseline Per-Task Results}
7	
8	Table~\ref{tab:smolvla_baseline_pertask} reports per-task success rates for the SmolVLA baseline (bypass mode, no pruning) on LIBERO-Object. All pruning conditions (Table~\ref{tab:smolvla_ablation}) produce 0\% success rate on every task; we omit per-task breakdowns for pruning conditions as they carry no additional information beyond the aggregate 0\% already reported.
9	
10	\begin{table}[ht]
11	\centering
12	\small
13	\caption{SmolVLA baseline (bypass mode) per-task success rates on LIBERO-Object (50 episodes per task, 500 total). Overall SR: 44.8\%.}
14	\label{tab:smolvla_baseline_pertask}
15	\begin{tabular}{lc}
16	\toprule
17	Task & SR (\%) \\
18	\midrule
19	alphabet\_soup & 22 \\
20	bbq\_sauce & 60 \\
21	butter & 42 \\
22	chocolate\_pudding & 38 \\
23	cream\_cheese & 58 \\
24	ketchup & 26 \\
25	milk & 62 \\
26	orange\_juice & 38 \\
27	salad\_dressing & 50 \\
28	tomato\_sauce & 52 \\
29	\midrule
30	\textbf{Overall} & \textbf{44.8} \\
31	\bottomrule
32	\end{tabular}
33	\end{table}
34	
35	\subsection{Official SmolVLA Checkpoint Per-Task Results}
36	
37	Table~\ref{tab:smolvla_official_pertask} reports per-task success rates for the official SmolVLA LIBERO checkpoint (HuggingFaceVLA/smolvla\_libero). Under 50\% random token removal, all tasks produce 0\% SR, identical to the fine-tuned checkpoint results.
38	
39	\begin{table}[ht]
40	\centering
41	\small
42	\caption{Official SmolVLA checkpoint per-task success rates on LIBERO-Object (50 episodes per task, 500 total). Overall SR: 59.2\%. Under 50\% random pruning, all tasks collapse to 0\%.}
43	\label{tab:smolvla_official_pertask}
44	\begin{tabular}{lcc}
45	\toprule
46	Task & Baseline SR (\%) & $k{=}0.5$ SR (\%) \\
47	\midrule
48	alphabet\_soup & 64 & 0 \\
49	bbq\_sauce & 38 & 0 \\
50	butter & 78 & 0 \\
51	chocolate\_pudding & 90 & 0 \\
52	cream\_cheese & 40 & 0 \\
53	ketchup & 60 & 0 \\
…[truncated 16792 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 206 · 2026-05-19T05:46:50.068721+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/references.bib"
  }
}
```

</details>

---


### Tool result

_source line 207 · 2026-05-19T05:46:50.922867+00:00_

1	% References for: The Cliff Edge — Why Vision Token Reduction Fails
2	% Catastrophically in VLA Closed-Loop Control
3	% Auto-generated from literature_map.yaml (verified entries only)
4	% 2026-05-17
5	
6	% ============================================================
7	% VLA Token Compression (concurrent work)
8	% ============================================================
9	
10	@article{gao2025compressorvla,
11	  title={Compressor-VLA: Instruction-Guided Visual Token Compression for Efficient Robotic Manipulation},
12	  author={Gao, Juntao and Ye, Feiyang and Zhang, Jing and Qian, Wenjing},
13	  journal={arXiv preprint arXiv:2511.18950},
14	  year={2025},
15	  eprint={2511.18950},
16	  archivePrefix={arXiv}
17	}
18	
19	@article{wang2025specprunevla,
20	  title={SpecPrune-VLA: Accelerating Vision-Language-Action Models via Action-Aware Self-Speculative Pruning},
21	  author={Wang, Hanzhen and Xu, Jiaming and Xiang, Yushun and Pan, Jiayi and Zhou, Yongkang and Li, Yong-Lu and Dai, Guohao},
22	  journal={arXiv preprint arXiv:2509.05614},
23	  year={2025},
24	  eprint={2509.05614},
25	  archivePrefix={arXiv}
26	}
27	
28	@inproceedings{jiang2026lightvla,
29	  title={The Better You Learn, The Smarter You Prune: Towards Efficient Vision-Language-Action Models via Differentiable Token Pruning},
30	  author={Jiang, Titong and Jiang, Xuefeng and Ma, Yuan and Wen, Xin and Li, Bailin and Zhan, Kun and Jia, Peng and Liu, Yahui and Sun, Sheng and Lang, Xianpeng},
31	  booktitle={Proceedings of the IEEE International Conference on Robotics and Automation (ICRA)},
32	  year={2026},
33	  eprint={2509.12594},
34	  archivePrefix={arXiv}
35	}
36	
37	@inproceedings{feng2026seewhatmatters,
38	  title={See What Matters: Differentiable Grid Sample Pruning for Generalizable Vision-Language-Action Model},
39	  author={Feng, Yixu and Zhao, Zinan and Ma, Yanxiang and Xia, Chenghao and Du, Chengbin and Wang, Yunke and Xu, Chang},
40	  booktitle={Proceedings of the Forty-Third International C
…[truncated 11570 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 854
}
```

</details>

---


### Tool call

_source line 208 · 2026-05-19T05:46:51.073935+00:00_

called mcp__agent-ml-research__verify_references

<details open><summary>🔧 Tool call — mcp__agent-ml-research__verify_references</summary>

```json
{
  "paper_dir": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper",
  "project": "importance_margin_vla_compress"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "mcp__agent-ml-research__verify_references",
  "tool_args": {
    "paper_dir": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper",
    "project": "importance_margin_vla_compress"
  }
}
```

</details>

---


### Tool call

_source line 209 · 2026-05-19T05:46:51.425738+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "CoRL conference review form dimensions \"overall recommendation\" \"novelty\" \"soundness\" rating scale"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "CoRL conference review form dimensions \"overall recommendation\" \"novelty\" \"soundness\" rating scale"
  }
}
```

</details>

---


### Tool result

_source line 210 · 2026-05-19T05:47:23.882124+00:00_

{"result":"{\"success\": true, \"data\": {\"summary\": {\"total_bib_entries\": 34, \"total_citations\": 50, \"unique_cited_keys\": 34, \"orphan_bib\": 0, \"missing_bib\": 0, \"duplicate_keys\": 0, \"online_verified\": 26, \"online_not_found\": 2, \"online_mismatch\": 6}, \"cross_check\": {\"orphan_bib\": [], \"missing_bib\": [], \"orphan_count\": 0, \"missing_count\": 0}, \"bib_entries\": [{\"key\": \"gao2025compressorvla\", \"type\": \"article\", \"title\": \"Compressor-VLA: Instruction-Guided Visual Token Compression for Efficient Robotic Manipulation\", \"authors\": \"Gao, Juntao and Ye, Feiyang and Zhang, Jing and Qian, Wenjing\", \"year\": \"2025\", \"venue\": \"arXiv preprint arXiv:2511.18950\"}, {\"key\": \"wang2025specprunevla\", \"type\": \"article\", \"title\": \"SpecPrune-VLA: Accelerating Vision-Language-Action Models via Action-Aware Self-Speculative Pruning\", \"authors\": \"Wang, Hanzhen and Xu, Jiaming and Xiang, Yushun and Pan, Jiayi and Zhou, Yongkan...\", \"year\": \"2025\", \"venue\": \"arXiv preprint arXiv:2509.05614\"}, {\"key\": \"jiang2026lightvla\", \"type\": \"inproceedings\", \"title\": \"The Better You Learn, The Smarter You Prune: Towards Efficient Vision-Language-Action Models via Differentiable Token Pr...\", \"authors\": \"Jiang, Titong and Jiang, Xuefeng and Ma, Yuan and Wen, Xin and Li, Bailin and Zh...\", \"year\": \"2026\", \"venue\": \"Proceedings of the IEEE International Conference on Robotics and Automation (ICR...\"}, {\"key\": \"feng2026seewhatmatters\", \"type\": \"inproceedings\", \"title\": \"See What Matters: Differentiable Grid Sample Pruning for Generalizable Vision-Language-Action Model\", \"authors\": \"Feng, Yixu and Zhao, Zinan and Ma, Yanxiang and Xia, Chenghao and Du, Chengbin a...\", \"year\": \"2026\", \"venue\": \"Proceedings of the Forty-Third International Conference on Machine Learning (ICM...\"}, {\"key\": \"zhang2025sparsevlm\", \"type\": \"inproceedings\", \"title\": \"SparseVLM: Visual Token Sparsificat
…[truncated 26543 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "mcp__agent-ml-research__verify_references",
  "elapsed_ms": 32808
}
```

</details>

---


### Tool result

_source line 211 · 2026-05-19T05:47:41.582110+00:00_

Web search results for query: "CoRL conference review form dimensions "overall recommendation" "novelty" "soundness" rating scale"

Links: [{"title":"ARR Reviewer Guidelines","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"Review Form","url":"http://aclrollingreview.org/reviewform"},{"title":"Reviewer Guidelines — CoRL 2023","url":"https://www.corl2023.org/reviewer-guidelines"},{"title":"ACL 2023 Acceptance Recommendations - ACL 2023","url":"https://2023.aclweb.org/blog/overall-recommendation/"},{"title":"CoRL 2024 - Instruction for Reviews","url":"https://2024.corl.org/contributions/instruction-for-reviews"},{"title":"CoRL 2021 Conference | OpenReview","url":"https://openreview.net/group?id=robot-learning.org%2FCoRL%2F2021%2FConference"},{"title":"CoRL 2026 Conference | OpenReview","url":"https://openreview.net/group?id=robot-learning.org%2FCoRL%2F2026%2FConference"},{"title":"Recommender Systems for the Conference Paper Assignment Problem","url":"https://arxiv.org/pdf/0906.4044"}]

The search results provide some relevant information about conference review forms, but they primarily show ARR (ACL Rolling Review) guidelines rather than specific CoRL (Conference on Robot Learning) review form dimensions. Let me search more specifically for CoRL review form details.

Links: [{"title":"CoRL 2024 - Instruction for Reviews","url":"https://2024.corl.org/contributions/instruction-for-reviews"},{"title":"2024 reviewer index","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11742086/"},{"title":"ICLR 2024 Statistics - Paper Copilot","url":"https://papercopilot.com/statistics/iclr-statistics/iclr-2024-statistics/"},{"title":"Reviewers in 2024","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12056528/"},{"title":"Reviewer Guidelines — CoRL 2023","url":"https://www.corl2023.org/reviewer-guidelines"},{"title":"Outstanding Reviewers for RSC Advances in 2024","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12138326/"}]

Let me search more specifically
…[truncated 4970 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 50156
}
```

</details>

---


### Tool call

_source line 212 · 2026-05-19T05:47:47.011625+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://2021.corl.org/reviewer-information/instructions-for-reviewers",
  "prompt": "Extract the complete review form questions, scoring dimensions, rating scales (1-10, 1-5, etc.), and specific criteria. Include ALL numerical scales and their descriptions."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://2021.corl.org/reviewer-information/instructions-for-reviewers",
    "prompt": "Extract the complete review form questions, scoring dimensions, rating scales (1-10, 1-5, etc.), and specific criteria. Include ALL numerical scales and their descriptions."
  }
}
```

</details>

---


### Tool call

_source line 213 · 2026-05-19T05:47:47.768003+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://openreview.net/group?id=robot-learning.org%2FCoRL%2F2026%2FConference",
  "prompt": "Extract the review form dimensions, scoring scales, and submission guidelines. Look for any review criteria or rating rubrics."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://openreview.net/group?id=robot-learning.org%2FCoRL%2F2026%2FConference",
    "prompt": "Extract the review form dimensions, scoring scales, and submission guidelines. Look for any review criteria or rating rubrics."
  }
}
```

</details>

---


### Tool result

_source line 214 · 2026-05-19T05:47:50.782179+00:00_

# CoRL 2026 Conference Review Information

Based on the provided webpage content, I cannot extract the requested information about review form dimensions, scoring scales, submission guidelines, or review criteria.

**Finding:** The webpage content shown consists primarily of navigation elements, footer links, and general OpenReview platform information. It does not contain specific details about the CoRL 2026 conference's review structure or submission requirements.

**Recommendation:** To locate this information, you would need to:
- Access the full CoRL 2026 conference page on OpenReview
- Review the "Call for Papers" or "Submission Guidelines" section
- Check the conference's official review form or instructions page

The current excerpt appears to be a navigation template rather than the substantive conference details page.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 3014
}
```

</details>

---


### Tool result

_source line 215 · 2026-05-19T05:47:51.535969+00:00_

# CoRL 2021 Reviewer Information: Review Form Analysis

Based on the provided webpage content, **no review form questions, scoring dimensions, rating scales, or specific evaluation criteria are included**.

The page focuses exclusively on the review process timeline and reviewer responsibilities. It contains:

- **Timeline phases** (bidding, review period, discussion, finalization)
- **Deadline information** across three months
- **General expectations**: "constructive feedback to the authors" and "active and constructive engagement"

The document does not specify:
- Numerical rating scales (1-10, 1-5, etc.)
- Specific review form questions
- Scoring dimensions or criteria
- Evaluation rubrics

To locate the actual review form, reviewers would need to access the OpenReview platform directly, as referenced in the page's link to "Papers (OpenReview)."

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 4524
}
```

</details>

---


### Tool call

_source line 216 · 2026-05-19T05:47:56.260088+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "site:openreview.net CoRL 2024 review \"overall score\" \"soundness\" \"presentation\" rating"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "site:openreview.net CoRL 2024 review \"overall score\" \"soundness\" \"presentation\" rating"
  }
}
```

</details>

---


### Tool result

_source line 217 · 2026-05-19T05:48:01.039845+00:00_

Web search results for query: "site:openreview.net CoRL 2024 review "overall score" "soundness" "presentation" rating"

Links: [{"title":"(PDF) Insights from the ICLR Peer Review and Rebuttal Process","url":"https://www.researchgate.net/publication/397780200_Insights_from_the_ICLR_Peer_Review_and_Rebuttal_Process"},{"title":"2024 Reviewer Guidelines","url":"https://neurips.cc/Conferences/2024/ReviewerGuidelines"},{"title":"CoRL 2024 | OpenReview","url":"https://openreview.net/group?id=robot-learning.org/CoRL/2024"},{"title":"Insights from the ICLR Peer Review and Rebuttal Process","url":"https://arxiv.org/pdf/2511.15462"},{"title":"CoRL 2024 Conference | OpenReview","url":"https://openreview.net/group?id=robot-learning.org%2FCoRL%2F2024%2FConference"},{"title":"ICML 2024 Reviewer Instructions","url":"https://icml.cc/Conferences/2024/ReviewerInstructions"},{"title":"CoRL 2024 Conference Submissions | OpenReview","url":"https://openreview.net/submissions?venue=robot-learning.org/CoRL/2024/Conference"}]

I found the CoRL 2024 submissions page on OpenReview, which shows various papers published in September 2024 with their modification dates. However, the search results show only a snippet of paper titles and authors, not the detailed review ratings with overall scores, soundness, and presentation ratings.

To access the specific review information you're looking for, you would need to visit the OpenReview pages directly for individual papers. The CoRL 2024 Conference page is at:

- **CoRL 2024 Conference submissions**: https://openreview.net/submissions?venue=robot-learning.org/CoRL/2024/Conference

From there, you can click on individual papers to see their reviews, which typically include the numerical ratings for soundness, presentation, and overall score that you're searching for. The review information is publicly accessible on OpenReview for all papers, whether accepted or rejected.


REMINDER: You MUST include the sources above in your response to the user using
…[truncated 21 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 4779
}
```

</details>

---


### Tool call

_source line 218 · 2026-05-19T05:48:05.382850+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://openreview.net/forum?id=VLA-Cache&venue=robot-learning.org/CoRL/2024/Conference",
  "prompt": "Extract the review form structure: what dimensions are scored, what are the rating scales, what questions are asked in the review."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://openreview.net/forum?id=VLA-Cache&venue=robot-learning.org/CoRL/2024/Conference",
    "prompt": "Extract the review form structure: what dimensions are scored, what are the rating scales, what questions are asked in the review."
  }
}
```

</details>

---


### Tool call

_source line 219 · 2026-05-19T05:48:05.785852+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "CoRL OpenReview review form \"overall assessment\" scale 1-10 \"confidence\" \"soundness\" robot learning 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "CoRL OpenReview review form \"overall assessment\" scale 1-10 \"confidence\" \"soundness\" robot learning 2024 2025"
  }
}
```

</details>

---


### Tool result

_source line 220 · 2026-05-19T05:48:07.193410+00:00_

I cannot extract the review form structure from the provided content. The webpage displays an error message indicating "The Note VLA-Cache was not found" rather than showing actual review form details.

To obtain information about OpenReview's review dimensions, rating scales, and questions, you would need to access a successfully loaded venue page or consult their documentation at the FAQ or support resources linked on the site.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 1810
}
```

</details>

---


### Tool result

_source line 221 · 2026-05-19T05:48:25.215536+00:00_

Web search results for query: "CoRL OpenReview review form "overall assessment" scale 1-10 "confidence" "soundness" robot learning 2024 2025"

Links: [{"title":"CoRL 2024 Workshop CoRoboLearn | OpenReview","url":"https://openreview.net/group?id=robot-learning.org%2FCoRL%2F2024%2FWorkshop%2FCoRoboLearn"},{"title":"CoRL 2024 | OpenReview","url":"https://openreview.net/group?id=robot-learning.org/CoRL/2024"},{"title":"CoRL 2024 - Instruction for Reviews","url":"https://2024.corl.org/contributions/instruction-for-reviews"},{"title":"CoRL 2024 Conference | OpenReview","url":"https://openreview.net/group?id=robot-learning.org%2FCoRL%2F2024%2FConference"},{"title":"CoRL | OpenReview","url":"https://openreview.net/group?id=robot-learning.org%2FCoRL"},{"title":"CoRL 2024 Workshop XE | OpenReview","url":"https://openreview.net/group?id=robot-learning.org%2FCoRL%2F2024%2FWorkshop%2FXE"},{"title":"CoRL 2024 Workshop | OpenReview","url":"https://openreview.net/group?id=robot-learning.org%2FCoRL%2F2024%2FWorkshop"},{"title":"CoRL 2024 Conference Submissions | OpenReview","url":"https://openreview.net/submissions?venue=robot-learning.org/CoRL/2024/Conference"},{"title":"CoRL 2024 Workshop WCBM | OpenReview","url":"https://openreview.net/group?id=robot-learning.org%2FCoRL%2F2024%2FWorkshop%2FWCBM"},{"title":"Reviewer Guidelines — CoRL 2023","url":"https://www.corl2023.org/reviewer-guidelines"}]

The search results show some information about CoRL 2024, but don't contain the specific review form details you're looking for. Let me search more specifically for the review form structure with the rating scales.

Links: [{"title":"ARR Reviewer Guidelines","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"Reviewer Guidelines","url":"https://virtual.aistats.org/Conferences/2026/ReviewerGuidelines"},{"title":"ICML 2024 Reviewer Instructions","url":"https://icml.cc/Conferences/2024/ReviewerInstructions"},{"title":"ACL 2025 Statistics - Paper Copilot","url":"https://papercopil
…[truncated 5453 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 19429
}
```

</details>

---


### Tool call

_source line 222 · 2026-05-19T05:48:30.461098+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://openreview.net/forum?id=vfhm0jMLvC",
  "prompt": "Extract the review form structure from any review on this page. What dimensions are scored? What are the exact rating scales? Look for fields like \"overall assessment\", \"soundness\", \"significance\", \"confidence\" etc. with their numerical scales."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://openreview.net/forum?id=vfhm0jMLvC",
    "prompt": "Extract the review form structure from any review on this page. What dimensions are scored? What are the exact rating scales? Look for fields like \"overall assessment\", \"soundness\", \"significance\", \"confidence\" etc. with their numerical scales."
  }
}
```

</details>

---


### Tool result

_source line 223 · 2026-05-19T05:48:32.683764+00:00_

I cannot extract review form structure or scoring dimensions from this page content because **the page displays an error message** indicating that the requested note (vfhm0jMLvC) was not found on OpenReview.

The content provided only shows:
- Navigation elements
- An error statement: "The Note vfhm0jMLvC was not found"
- Footer links and organizational information

There is no actual review form or scoring criteria visible on this error page. To obtain the review structure you're asking about, you would need to access a valid OpenReview submission or review page rather than this error state.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 2222
}
```

</details>

---


### Tool call

_source line 224 · 2026-05-19T05:50:51.579290+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Compressor-VLA OpenVLA-OFT LIBERO 97.1% success rate cross-attention compression"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Compressor-VLA OpenVLA-OFT LIBERO 97.1% success rate cross-attention compression"
  }
}
```

</details>

---


### Tool call

_source line 225 · 2026-05-19T05:50:52.483686+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"See What Matters\" SmolVLA continuous resampling cliff-edge pixel-shuffle pruning failure 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"See What Matters\" SmolVLA continuous resampling cliff-edge pixel-shuffle pruning failure 2026"
  }
}
```

</details>

---


### Tool call

_source line 226 · 2026-05-19T05:50:53.036433+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EfficientVLA CogACT token pruning MLP projector pixel-shuffle comparison 97.8% success rate"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EfficientVLA CogACT token pruning MLP projector pixel-shuffle comparison 97.8% success rate"
  }
}
```

</details>

---


### Tool result

_source line 227 · 2026-05-19T05:50:59.271434+00:00_

Web search results for query: ""See What Matters" SmolVLA continuous resampling cliff-edge pixel-shuffle pruning failure 2026"

Links: [{"title":"ICML Poster See What Matters: Differentiable Grid Sample Pruning for Generalizable Vision-Language-Action Model","url":"https://icml.cc/virtual/2026/poster/65010"},{"title":"Don't Run with Scissors: Pruning Breaks VLA Models but They Can Be Recovered","url":"https://arxiv.org/pdf/2510.08464"},{"title":"SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics","url":"https://arxiv.org/pdf/2506.01844"},{"title":"The Better You Learn, The Smarter You Prune: Towards Efficient Vision-language-action Models via Differentiable Token Pruning","url":"https://arxiv.org/pdf/2509.12594"},{"title":"VLA-IAP: Training-Free Visual Token Pruning via Interaction Alignment for Vision-Language-Action Models","url":"https://arxiv.org/pdf/2603.22991"},{"title":"SpecPrune-VLA: Accelerating Vision-Language-Action Models via Action-Aware Self-Speculative Pruning","url":"https://arxiv.org/pdf/2509.05614"}]

Based on the search results, I found information about "See What Matters," which appears to be a research paper presented at ICML 2026. Here's what the search reveals:

The research addresses a fundamental trade-off in token pruning methods: aggressive compression inevitably discards critical geometric details like contact points, leading to severe performance degradation, which limits achievable compression rates and potential speedup.

The paper proposes rethinking compression as geometry-aware, continuous token resampling in the vision encoder through the Differentiable Grid Sampler (GridS), a plug-and-play module that performs task-aware, continuous resampling of visual tokens in Vision-Language-Action (VLA) models.

By adaptively predicting a minimal set of salient coordinates and extracting features via differentiable interpolation, GridS preserves essential spatial information while achieving drastic compression with 
…[truncated 479 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 6787
}
```

</details>

---


### Tool result

_source line 228 · 2026-05-19T05:50:59.422776+00:00_

Web search results for query: "EfficientVLA CogACT token pruning MLP projector pixel-shuffle comparison 97.8% success rate"

Links: [{"title":"EfficientVLA: Training-Free Acceleration and Compression ...","url":"https://openreview.net/pdf?id=SELYlDHZk2"},{"title":"VLA-IAP: Training-Free Visual Token Pruning via Interaction Alignment for Vision-Language-Action Models","url":"https://arxiv.org/html/2603.22991v1"},{"title":"EfficientVLA: Training-Free Acceleration and Compression for Vision-Language-Action Models","url":"https://arxiv.org/pdf/2506.10100"},{"title":"EfficientVLA: Training-Free Acceleration and Compression for Vision-Language-Action Models","url":"https://arxiv.org/html/2506.10100v1"},{"title":"VLA-IAP: Training-Free Visual Token Pruning via Interaction Alignment for Vision-Language-Action Models","url":"https://arxiv.org/pdf/2603.22991"},{"title":"Beyond Attention Magnitude: Leveraging Inter-layer Rank Consistency for Efficient Vision-Language-Action Models","url":"https://arxiv.org/pdf/2603.24941"},{"title":"CogVLA: Cognition-Aligned Vision-Language-Action Model via Instruction-Driven Routing & Sparsification","url":"https://arxiv.org/pdf/2508.21046"},{"title":"TokenPacker: Efficient Visual Projector for Multimodal LLM","url":"https://arxiv.org/html/2407.02392v1"},{"title":"The Better You Learn, The Smarter You Prune: Towards Efficient Vision-language-action Models via Differentiable Token Pruning","url":"https://arxiv.org/pdf/2509.12594"}]

Based on the search results, here's what I found regarding your query:

The 97.8% success rate appears to be associated with VLA-IAP, which achieves a state-of-the-art average success rate of 97.8% with 1.25× inference speedup at a 70% token retention ratio. OpenVLA-OFT builds upon the open-source OpenVLA architecture, which fuses a dual vision backbone (SigLIP + DINOv2) with a Llama-2 7B language model via a 3-layer MLP projector.

Regarding EfficientVLA and CogACT specifically, when applied to the CogACT model, E
…[truncated 637 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 6386
}
```

</details>

---


### Tool result

_source line 229 · 2026-05-19T05:51:00.778104+00:00_

Web search results for query: "Compressor-VLA OpenVLA-OFT LIBERO 97.1% success rate cross-attention compression"

Links: [{"title":"Compressor-VLA: Instruction-Guided Visual Token Compression for Efficient Robotic Manipulation","url":"https://arxiv.org/html/2511.18950v1"},{"title":"Compressor-VLA: Instruction-Guided Visual Token Compression for Efficient Robotic Manipulation","url":"https://chatpaper.com/paper/212383"},{"title":"OpenVLA-OFT","url":"https://openvla-oft.github.io/"},{"title":"Token Expand-Merge: Training-Free Compression Accelerates Billion-Parameter Vision-Language-Action Model Inference","url":"https://quantumzeitgeist.com/training-token-expand-merge-free-compression-accelerates-billion-parameter/"},{"title":"Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success | alphaXiv","url":"https://www.alphaxiv.org/overview/2502.19645"},{"title":"Compressor-VLA: Instruction-Guided Visual Token Compression for Efficient Robotic Manipulation","url":"https://arxiv.org/pdf/2511.18950"},{"title":"Training Data for OpenVLA | Data Requirements & Formats | Claru","url":"https://claru.ai/models/openvla"},{"title":"[2511.18950] Compressor-VLA: Instruction-Guided Visual Token Compression for Efficient Robotic Manipulation","url":"https://arxiv.org/abs/2511.18950"},{"title":"Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success","url":"https://arxiv.org/html/2502.19645v2"}]

Based on the search results, here's what I found about Compressor-VLA:

## Overview

Compressor-VLA is a novel hybrid instruction-conditioned token compression framework designed for efficient, task-oriented compression of visual information in VLA models.

## Architecture and Mechanism

The framework employs a dual-mechanism approach where the Semantic Task Compressor (STC) uses cross-attention compression to distill a holistic, task-oriented scene summary, and the Spatial Refinement Compressor (SRC) uses guided local attention to preserve essential spatial detail
…[truncated 780 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 9198
}
```

</details>

---


### Tool call

_source line 230 · 2026-05-19T05:53:36.371447+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 2 — Round 1 审稿意见\n\n**论文**: Why Token Pruning Crashes Some Robot Policies but Not Others: The Role of Vision Connectors in VLA Token Compressibility\n**Venue**: CoRL 2026\n\n---\n\n## 总体评分\n\n**Overall: 4/10 (Weak Reject)**\n**Confidence: 3/5**\n**一句话总结**: 论文发现了一个有实际价值的 empirical phenomenon（pixel-shuffle VLA 的 cliff-edge pruning failure），实验设计有控制组，但在 concurrent work 密集的背景下新颖性有限，且核心因果归因（connector vs. scale）未被充分控制。\n\n---\n\n## 官方维度打分（基于 CoRL 2023 Reviewer Guidelines）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Originality | 4/10 | 核心发现（pixel-shuffle cliff-edge）已被 \"Don't Run with Scissors\"（weight pruning 85.2%→0%）和 \"See What Matters\"（ICML 2026, SmolVLA continuous resampling）部分独立报告；cross-attention re-encoding 是 Q-Former/Perceiver 的已知方案；entropy ratio 仅在 2 个架构上验证 |\n| Quality | 6/10 | 实验控制严谨（7 configurations, 2 checkpoints, extended training control, passthrough control），Wilson CI 规范；但 0.5B vs 7B 的 scale confound 未被解耦，是对核心 claim 的根本性威胁 |\n| Clarity | 7/10 | 写作清晰，结构合理，图表信息密度可接受，无明显 AI 写作痕迹；但 Section 3.1 与 Background（虽未编入正文）在 experimental_setup 中重复了大量架构描述 |\n| Significance | 4/10 | 实际贡献偏\"warning label\"性质（不要对 pixel-shuffle VLA 做 token pruning），Smart Compress 结果远弱于 Compressor-VLA（97.1% vs 97.3% baseline），且 cross-suite 泛化有 6.6pp 下降 |\n| Relevance | 5/10 | 与 robot learning 相关，但仅 simulation 评估（LIBERO），无 real-robot 实验，对 CoRL 审稿人吸引力有限 |\n| Limitations | 7/10 | Section 5.6 诚实报告了 simulation-only、scale confound、generalization 未验证等限制 |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] Scale confound 未被解耦，核心因果归因不可靠\n\n- 具体位置：Section 5.3 (Disentangling Connector from Scale), Section 4 全部结果\n- 问题：论文比较 SmolVLA (0.5B, pixel-shuffle) 和 OpenVLA (7B, MLP projector)，二者在 connector 和 model scale 上同时不同（14× 参数差异）。论文声称 cliff-edge 是 connector-dependent，但提供的四条证据均为间接的：\n  - (1) Official checkpoint 也 fail → 仍是 0.5B 模型\n  - (2) k=0.95 就崩溃 → 0.5B 模型可能本身对小扰动更脆弱，与 connector 无关\n  - (3) Entropy ratio 是 architectural measurement → 但 entropy 也可能反映 model capacity（小模型无法学习 selective attention）\n  - (4) Pixel-shuffle 4×4 folding 的 mechanistic account → 最强论据，但仍为 correlational\n- 为什么影响接收：这是论文的 central claim。如果 cliff-edge 主要由 model scale 而非 connector 驱动，则论文的全部 design implications（Section 5.5）和 contribution 1 均不成立。\n- 建议修改方向：(a) 在相同 backbone 上测试不同 connector（如用 MLP projector 替换 SmolVLA 的 pixel-shuffle，或在 0.5B 模型上测试 MLP projector）；(b) 至少增加一个中等规模的 pixel-shuffle VLA（如 InternVL-Chat 使用 pixel-shuffle + 更大 backbone）；(c) 如无法完成实验，应显著弱化因果 claim，将标题和贡献重新表述为\"observation\"而非\"role of vision connectors\"。\n\n**N2** [critical] 新颖性在 concurrent work 密集的背景下不足\n\n- 具体位置：Abstract (\"first systematic comparison\"), Introduction Contribution 1-4, Related Work Section 2\n- 问题：\n  - **Cliff-edge 发现**: \"Don't Run with Scissors\" (Jabbour et al., 2025, arXiv 2510.08464) 已报告 VLA pruning 从 85.2% 崩溃至 0%，虽然是 weight pruning 而非 token pruning，但 \"pruning breaks VLA\" 的核心 message 重叠度高。\"See What Matters\" (Feng et al., 2026, ICML 2026 accepted) 在 SmolVLA 上做 continuous resampling，隐含已观察到 discrete pruning 的 failure mode。\n  - **Cross-attention re-encoding**: Compressor-VLA (Gao et al., 2025) 在 OpenVLA-OFT 上用 cross-attention compression 达到 97.1% SR（baseline 97.3%），远优于本文 Smart Compress 的 61.6%（baseline 44.8%）。Q-Former 和 Perceiver 的 cross-attention pooling 在 VLM 中已是标准做法。\n  - **\"First systematic comparison\" claim**: 虽然没有单篇论文在完全相同条件下比较 pixel-shuffle 和 MLP projector VLA 的 pruning sensitivity，但 EfficientVLA (CogACT, MLP projector, 0.6% SR drop)、VLA-IAP (OpenVLA, 97.8% SR)、\"See What Matters\" (SmolVLA + π₀) 等多篇 concurrent work 已分别覆盖了不同 connector 类型。本文的 incremental value 仅在于\"把两种 connector 放在同一张表里比较\"。\n  - **Attention entropy ratio**: Normalized Shannon entropy 是标准 metric，仅在 2 个架构上测量不构成 generalizable 贡献。\n- 为什么影响接收：CoRL 要求 significance and novelty。在上述 concurrent work 均已公开的情况下，本文的 marginal contribution 偏小。\n- 建议修改方向：(a) 明确区分与 \"Don't Run with Scissors\"（weight pruning vs. token pruning）和 \"See What Matters\"（discrete deletion vs. continuous resampling，本文的 connector-level 解释 vs. 对方的 sampling paradigm 解释）；(b) 弱化\"first\"claim 或限定更窄的 scope（如 \"first controlled comparison at matched pruning conditions\"）；(c) 增加更多 connector 类型（Q-Former, linear projection）以强化 entropy ratio 的 generalizability。\n\n**N3** [critical] 仅 simulation 评估，CoRL venue fit 不足\n\n- 具体位置：Section 3.1 (LIBERO benchmark), Section 5.6 (Limitations)\n- 问题：全部实验在 LIBERO simulation 上完成，无任何 real-robot 验证。CoRL reviewer guidelines 明确要求评估\"relevance to robot learning\"，并偏好\"test the proposed learning solution on physical robots\"。LIBERO 是标准 benchmark，但 simulation 环境不包含 sensor noise、calibration drift、physical contact dynamics——这些因素可能改变 token pruning 的 sensitivity profile（如 real-world visual noise 可能使 token importance 分布更 non-uniform）。\n- 为什么影响接收：CoRL 作为 robot learning 顶会，simulation-only 的 empirical study（非 method contribution）在 novelty 已受质疑的情况下，进一步降低了 venue fit。\n- 建议修改方向：(a) 至少在一个 real-robot setup 上复现 cliff-edge（即使只是几十个 episode 的 pilot study）；(b) 如无法做 real-robot，应讨论 sim-to-real 的潜在 gap 并提供 domain randomization / visual augmentation 下的 robustness 实验。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] Smart Compress 的 cross-suite 泛化下降被低估\n\n- 具体位置：Appendix Table 6 (Cross-Suite Generalization), Section 4.3\n- 问题：Smart Compress (M=32, trained on LIBERO-Object) 在 LIBERO-Goal 上从 63.0% 降至 56.4%（-6.6pp）。这意味着 re-encoding module 在未见过的 task 分布上不能完全保持 baseline 性能。论文在 Appendix 提到但未在正文充分讨论，Section 4.3 仅说 \"maintains non-trivial performance where deletion-based methods completely fail\"，这弱化了 negative signal。\n- 建议：在正文 Section 4.3 中直接讨论 LIBERO-Goal 的下降及其 implications（Smart Compress 需要 task-specific training 或 multi-task training）。\n\n**W2** [warning] Baseline 质量偏低且可能影响结论推广\n\n- 具体位置：Section 4.1 footnote 1, Appendix Table 9\n- 问题：作者复现的 SmolVLA baseline (44.8%) 远低于官方结果 (87.3%)，原因是 batch size 4 vs 64×8=512。虽然 official checkpoint 也展示了 cliff-edge（59.2%→0%），但 Smart Compress 的全部实验基于 undertrained checkpoint。一个 44.8% SR 的弱 baseline 上的 +15pp 增益，能否推广到 87.3% 的 strong baseline，是未回答的问题。\n- 建议：在 official checkpoint 上也训练 Smart Compress 进行验证，或至少讨论 strong baseline 下 re-encoding gain 可能缩小的风险。\n\n**W3** [warning] Multi-seed 实验不充分\n\n- 具体位置：Appendix Table 5 (Multi-Seed Results)\n- 问题：仅 2 个 seed（42, 43）。M=96 的 half-range 达 2.8pp（52.6% vs 58.2%），在仅 2 个 seed 下无法判断是否为 noise。标准做法是 3-5 seeds。\n- 建议：增加至少 1 个 seed，报告 mean ± std 而非 mean ± half-range。\n\n**W4** [warning] Attention entropy ratio 缺乏 predictive validation\n\n- 具体位置：Section 5.1, Contribution 2\n- 问题：entropy ratio 在 2 个架构上测量（SmolVLA 0.95, OpenVLA 0.64），论文提出 >0.9 作为 pruning failure 的 threshold（Section 5.5）。但这个 threshold 基于 2 个数据点的 interpolation。如果在 Q-Former VLA（entropy ratio 可能在 0.7-0.8 区间）上测试，threshold 是否仍然 valid？论文承认需要更多 validation（\"though validation on additional connector types is needed\"），但作为 Contribution 2 声称的\"compressibility signal\"，2 个数据点不足以建立 predictive utility。\n- 建议：至少在一个 Q-Former 或 Perceiver-based VLA（如 RoboFlamingo, 已 cited）上测量 entropy ratio 并检验其与 pruning sensitivity 的关系。\n\n**W5** [warning] 论文叙事中 EfficientVLA 证据的使用有问题\n\n- 具体位置：Introduction Contribution 1, Conclusion, Section 5.3\n- 问题：论文多次引用 EfficientVLA 的 CogACT 结果（\"97.8% SR under 78% MLP-projector pruning\"，来自 Introduction）作为\"concurrent findings supporting the pattern across three models and two connector families\"。但 (a) 97.8% SR 实际来自 VLA-IAP 而非 EfficientVLA（根据我的检索，EfficientVLA 在 CogACT 上的数字是 0.6% SR drop，而非 97.8%）；(b) 引用第三方结果来支撑\"our findings span three models\"有归因问题——这些结果不是作者产出的。\n- 建议：准确引用数字来源（确认 97.8% 到底来自哪篇论文），并将 EfficientVLA 结果表述为\"independent corroboration\"而非本文 contribution 的一部分。\n\n---\n\n## 小问题（不影响接收）\n\n- **S1**: Figure 1 caption（experimental_setup.tex line 12-13）过长（4 行文字），超出了 caption 应有的简洁度。可将 hypothesis 部分移至正文。\n- **S2**: Abstract 约 220 words，在 150-250 区间内但偏长，包含了过多数字细节（\"7 of 128\"、\"Wilson 95% CI\"、\"$k{=}0.95$\"）——这些更适合放在 Results 中。\n- **S3**: Section 3 title 是 \"Experimental Setup\" 但包含了 Smart Compress 的方法描述（Section 3.4），这属于 method 而非 setup。考虑将 Section 标题改为 \"Methods and Setup\" 或将 Smart Compress 独立成一节。\n- **S4**: \"flow matching action head\" (Section 2/Background) 中的 flow matching 概念在 experimental_setup 中也被重新描述，存在轻微冗余。\n- **S5**: 引用 verify 结果显示 `jabbour2025dontrun` (Don't Run with Scissors) 在 OpenAlex 中 not_found——可能是尚未被索引的 arXiv preprint，不影响 validity 但需确认 arXiv ID 正确。\n- **S6**: `background.tex` 和 `experiments_deprecated.tex` 存在于 paper 目录但未被 `main.tex` include。如提交源码包，应清理这些 orphan 文件。\n\n---\n\n## Missing References\n\n1. **CogACT 本身**：论文通过 EfficientVLA 间接引用 CogACT 的结果，但未直接引用 CogACT 原始论文。如果声称\"findings span three models\"之一是 CogACT，应给出原始 citation。\n2. **OpenVLA-OFT**：Compressor-VLA 的 baseline 是 OpenVLA-OFT（fine-tuned version with 97.3% SR），论文 Related Work 提到了 Compressor-VLA 但未引用 OpenVLA-OFT 本身。由于 OpenVLA-OFT 在 LIBERO 上的 97.3% 是当前 SOTA 级别性能，值得作为 baseline reference。\n3. **TokenPacker / TinyLLaVA**: 作为 VLM token efficiency 的相关工作，TokenPacker 等使用 spatial-aware compression，与 pixel-shuffle 问题相关。\n\n---\n\n## 主要优势\n\n- **S1: 实验设计的控制严谨性**: 7 configurations × 3 mechanisms × 2 checkpoints × 3 suites 的 ablation，加上 extended training control 和 M=128 passthrough control，使得 diagnostic claim（\"re-encoding > deletion\"）的证据链比较完整。Wilson CI 的使用在 VLA 文献中不常见，体现了统计严谨性。\n- **S2: Cliff-edge 发现的实际价值**: 即使从 novelty 角度有 concurrent work 重叠，\"pixel-shuffle VLA + 5% token removal = 完全失败\"的量化结果对 practitioners 有直接警示意义，尤其是在多篇 concurrent work 仅在 MLP-projector 架构上报告成功的背景下。\n- **S3: 诚实的 framing**: 论文将 Smart Compress 定位为 \"diagnostic experiment\" 而非 method contribution，承认 scale confound，标注 concurrent work。这种诚实度在 submission 中不常见。\n- **S4: 写作质量**: 全文逻辑连贯，无 AI 写作痕迹（无解释性 em-dash、无 -ing phrase 结尾、无过度分段），术语首次出现有定义（SigLIP, ACIS 等），图表 caption 自包含。\n- **S5: Offline metric disconnect 分析 (Section 5.4)**: 展示了 offline action error（3.4×）掩盖 catastrophic gripper inversions 的分析有教育意义，reinforces closed-loop evaluation 的重要性。\n\n---\n\n## Questions to Authors\n\n1. 是否有在相同 backbone（如 Qwen2-0.5B）上替换 SmolVLA 的 pixel-shuffle 为 MLP projector 的 ablation 实验？这是解耦 connector vs. scale 的最直接方法。\n2. Smart Compress 在 official SmolVLA checkpoint（87.3% baseline）上是否也测试过？如果 re-encoding 在 strong baseline 上的 marginal gain 很小，则 \"re-encoding overcomes cliff-edge\" 的 claim 需要重新考虑。\n3. Section 5.1 提到 entropy ratio 0.95 vs 0.64，Introduction 提到 CogACT (via EfficientVLA) 作为第三个数据点。CogACT 的 entropy ratio 是多少？如果已测量但未报告，应加入 Figure 3。\n4. \"See What Matters\" (ICML 2026) 在 SmolVLA 上用 continuous resampling 保留 <10% tokens 仍然 work。这与本文的 \"pixel-shuffle tokens resist any form of deletion\" 形成什么关系？continuous resampling 本质上也是一种 re-encoding，这是否意味着本文的 diagnostic insight（re-encoding > deletion）已被独立验证？建议在 Discussion 中更深入地与此 concurrent work 对话。\n\n---\n\n## Overall Assessment Summary\n\n这是一篇实验执行认真、writing 质量不错的 empirical study，核心发现（pixel-shuffle cliff-edge at 5% removal）有 practical value。但在以下三个维度上未达到 CoRL 接收门槛：\n\n1. **Novelty**: 在 concurrent work 高度密集的 landscape 中（至少 7 篇直接相关 concurrent work，其中 \"See What Matters\" 已 accepted at ICML 2026 且同样在 SmolVLA 上工作），本文的 marginal contribution 偏小。\"First systematic comparison\" 的 claim 在 concurrent work 分别覆盖各 connector 类型的背景下不够 compelling。\n2. **Soundness of causal claim**: 0.5B vs 7B 的 scale confound 是核心弱点。论文的标题和 framing 做出了关于 \"the role of vision connectors\" 的因果声明，但实验设计无法排除 model scale 作为 alternative explanation。\n3. **CoRL venue fit**: Simulation-only evaluation 在 CoRL 的 expectation 下偏弱，尤其当贡献主要是 empirical observation 而非 novel method 时。\n\n**Recommendation: Weak Reject (4/10)**。如果作者能在 rebuttal 中提供 matched-scale 实验或 real-robot pilot study 以回应 N1 和 N3，评分有上调空间（至 borderline）。",
  "reviewer_id": "2",
  "project": "importance_margin_vla_compress"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 2 — Round 1 审稿意见\n\n**论文**: Why Token Pruning Crashes Some Robot Policies but Not Others: The Role of Vision Connectors in VLA Token Compressibility\n**Venue**: CoRL 2026\n\n---\n\n## 总体评分\n\n**Overall: 4/10 (Weak Reject)**\n**Confidence: 3/5**\n**一句话总结**: 论文发现了一个有实际价值的 empirical phenomenon（pixel-shuffle VLA 的 cliff-edge pruning failure），实验设计有控制组，但在 concurrent work 密集的背景下新颖性有限，且核心因果归因（connector vs. scale）未被充分控制。\n\n---\n\n## 官方维度打分（基于 CoRL 2023 Reviewer Guidelines）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Originality | 4/10 | 核心发现（pixel-shuffle cliff-edge）已被 \"Don't Run with Scissors\"（weight pruning 85.2%→0%）和 \"See What Matters\"（ICML 2026, SmolVLA continuous resampling）部分独立报告；cross-attention re-encoding 是 Q-Former/Perceiver 的已知方案；entropy ratio 仅在 2 个架构上验证 |\n| Quality | 6/10 | 实验控制严谨（7 configurations, 2 checkpoints, extended training control, passthrough control），Wilson CI 规范；但 0.5B vs 7B 的 scale confound 未被解耦，是对核心 claim 的根本性威胁 |\n| Clarity | 7/10 | 写作清晰，结构合理，图表信息密度可接受，无明显 AI 写作痕迹；但 Section 3.1 与 Background（虽未编入正文）在 experimental_setup 中重复了大量架构描述 |\n| Significance | 4/10 | 实际贡献偏\"warning label\"性质（不要对 pixel-shuffle VLA 做 token pruning），Smart Compress 结果远弱于 Compressor-VLA（97.1% vs 97.3% baseline），且 cross-suite 泛化有 6.6pp 下降 |\n| Relevance | 5/10 | 与 robot learning 相关，但仅 simulation 评估（LIBERO），无 real-robot 实验，对 CoRL 审稿人吸引力有限 |\n| Limitations | 7/10 | Section 5.6 诚实报告了 simulation-only、scale confound、generalization 未验证等限制 |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] Scale confound 未被解耦，核心因果归因不可靠\n\n- 具体位置：Section 5.3 (Disentangling Connector from Scale), Section 4 全部结果\n- 问题：论文比较 SmolVLA (0.5B, pixel-shuffle) 和 OpenVLA (7B, MLP projector)，二者在 connector 和 model scale 上同时不同（14× 参数差异）。论文声称 cliff-edge 是 connector-dependent，但提供的四条证据均为间接的：\n  - (1) Official checkpoint 也 fail → 仍是 0.5B 模型\n  - (2) k=0.95 就崩溃 → 0.5B 模型可能本身对小扰动更脆弱，与 connector 无关\n  - (3) Entropy ratio 是 architectural measurement → 但 entropy 也可能反映 model capacity（小模型无法学习 selective attention）\n  - (4) Pixel-shuffle 4×4 folding 的 mechanistic account → 最强论据，但仍为 correlational\n- 为什么影响接收：这是论文的 central claim。如果 cliff-edge 主要由 model scale 而非 connector 驱动，则论文的全部 design implications（Section 5.5）和 contribution 1 均不成立。\n- 建议修改方向：(a) 在相同 backbone 上测试不同 connector（如用 MLP projector 替换 SmolVLA 的 pixel-shuffle，或在 0.5B 模型上测试 MLP projector）；(b) 至少增加一个中等规模的 pixel-shuffle VLA（如 InternVL-Chat 使用 pixel-shuffle + 更大 backbone）；(c) 如无法完成实验，应显著弱化因果 claim，将标题和贡献重新表述为\"observation\"而非\"role of vision connectors\"。\n\n**N2** [critical] 新颖性在 concurrent work 密集的背景下不足\n\n- 具体位置：Abstract (\"first systematic comparison\"), Introduction Contribution 1-4, Related Work Section 2\n- 问题：\n  - **Cliff-edge 发现**: \"Don't Run with Scissors\" (Jabbour et al., 2025, arXiv 2510.08464) 已报告 VLA pruning 从 85.2% 崩溃至 0%，虽然是 weight pruning 而非 token pruning，但 \"pruning breaks VLA\" 的核心 message 重叠度高。\"See What Matters\" (Feng et al., 2026, ICML 2026 accepted) 在 SmolVLA 上做 continuous resampling，隐含已观察到 discrete pruning 的 failure mode。\n  - **Cross-attention re-encoding**: Compressor-VLA (Gao et al., 2025) 在 OpenVLA-OFT 上用 cross-attention compression 达到 97.1% SR（baseline 97.3%），远优于本文 Smart Compress 的 61.6%（baseline 44.8%）。Q-Former 和 Perceiver 的 cross-attention pooling 在 VLM 中已是标准做法。\n  - **\"First systematic comparison\" claim**: 虽然没有单篇论文在完全相同条件下比较 pixel-shuffle 和 MLP projector VLA 的 pruning sensitivity，但 EfficientVLA (CogACT, MLP projector, 0.6% SR drop)、VLA-IAP (OpenVLA, 97.8% SR)、\"See What Matters\" (SmolVLA + π₀) 等多篇 concurrent work 已分别覆盖了不同 connector 类型。本文的 incremental value 仅在于\"把两种 connector 放在同一张表里比较\"。\n  - **Attention entropy ratio**: Normalized Shannon entropy 是标准 metric，仅在 2 个架构上测量不构成 generalizable 贡献。\n- 为什么影响接收：CoRL 要求 significance and novelty。在上述 concurrent work 均已公开的情况下，本文的 marginal contribution 偏小。\n- 建议修改方向：(a) 明确区分与 \"Don't Run with Scissors\"（weight pruning vs. token pruning）和 \"See What Matters\"（discrete deletion vs. continuous resampling，本文的 connector-level 解释 vs. 对方的 sampling paradigm 解释）；(b) 弱化\"first\"claim 或限定更窄的 scope（如 \"first controlled comparison at matched pruning conditions\"）；(c) 增加更多 connector 类型（Q-Former, linear projection）以强化 entropy ratio 的 generalizability。\n\n**N3** [critical] 仅 simulation 评估，CoRL venue fit 不足\n\n- 具体位置：Section 3.1 (LIBERO benchmark), Section 5.6 (Limitations)\n- 问题：全部实验在 LIBERO simulation 上完成，无任何 real-robot 验证。CoRL reviewer guidelines 明确要求评估\"relevance to robot learning\"，并偏好\"test the proposed learning solution on physical robots\"。LIBERO 是标准 benchmark，但 simulation 环境不包含 sensor noise、calibration drift、physical contact dynamics——这些因素可能改变 token pruning 的 sensitivity profile（如 real-world visual noise 可能使 token importance 分布更 non-uniform）。\n- 为什么影响接收：CoRL 作为 robot learning 顶会，simulation-only 的 empirical study（非 method contribution）在 novelty 已受质疑的情况下，进一步降低了 venue fit。\n- 建议修改方向：(a) 至少在一个 real-robot setup 上复现 cliff-edge（即使只是几十个 episode 的 pilot study）；(b) 如无法做 real-robot，应讨论 sim-to-real 的潜在 gap 并提供 domain randomization / visual augmentation 下的 robustness 实验。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] Smart Compress 的 cross-suite 泛化下降被低估\n\n- 具体位置：Appendix Table 6 (Cross-Suite Generalization), Section 4.3\n- 问题：Smart Compress (M=32, trained on LIBERO-Object) 在 LIBERO-Goal 上从 63.0% 降至 56.4%（-6.6pp）。这意味着 re-encoding module 在未见过的 task 分布上不能完全保持 baseline 性能。论文在 Appendix 提到但未在正文充分讨论，Section 4.3 仅说 \"maintains non-trivial performance where deletion-based methods completely fail\"，这弱化了 negative signal。\n- 建议：在正文 Section 4.3 中直接讨论 LIBERO-Goal 的下降及其 implications（Smart Compress 需要 task-specific training 或 multi-task training）。\n\n**W2** [warning] Baseline 质量偏低且可能影响结论推广\n\n- 具体位置：Section 4.1 footnote 1, Appendix Table 9\n- 问题：作者复现的 SmolVLA baseline (44.8%) 远低于官方结果 (87.3%)，原因是 batch size 4 vs 64×8=512。虽然 official checkpoint 也展示了 cliff-edge（59.2%→0%），但 Smart Compress 的全部实验基于 undertrained checkpoint。一个 44.8% SR 的弱 baseline 上的 +15pp 增益，能否推广到 87.3% 的 strong baseline，是未回答的问题。\n- 建议：在 official checkpoint 上也训练 Smart Compress 进行验证，或至少讨论 strong baseline 下 re-encoding gain 可能缩小的风险。\n\n**W3** [warning] Multi-seed 实验不充分\n\n- 具体位置：Appendix Table 5 (Multi-Seed Results)\n- 问题：仅 2 个 seed（42, 43）。M=96 的 half-range 达 2.8pp（52.6% vs 58.2%），在仅 2 个 seed 下无法判断是否为 noise。标准做法是 3-5 seeds。\n- 建议：增加至少 1 个 seed，报告 mean ± std 而非 mean ± half-range。\n\n**W4** [warning] Attention entropy ratio 缺乏 predictive validation\n\n- 具体位置：Section 5.1, Contribution 2\n- 问题：entropy ratio 在 2 个架构上测量（SmolVLA 0.95, OpenVLA 0.64），论文提出 >0.9 作为 pruning failure 的 threshold（Section 5.5）。但这个 threshold 基于 2 个数据点的 interpolation。如果在 Q-Former VLA（entropy ratio 可能在 0.7-0.8 区间）上测试，threshold 是否仍然 valid？论文承认需要更多 validation（\"though validation on additional connector types is needed\"），但作为 Contribution 2 声称的\"compressibility signal\"，2 个数据点不足以建立 predictive utility。\n- 建议：至少在一个 Q-Former 或 Perceiver-based VLA（如 RoboFlamingo, 已 cited）上测量 entropy ratio 并检验其与 pruning sensitivity 的关系。\n\n**W5** [warning] 论文叙事中 EfficientVLA 证据的使用有问题\n\n- 具体位置：Introduction Contribution 1, Conclusion, Section 5.3\n- 问题：论文多次引用 EfficientVLA 的 CogACT 结果（\"97.8% SR under 78% MLP-projector pruning\"，来自 Introduction）作为\"concurrent findings supporting the pattern across three models and two connector families\"。但 (a) 97.8% SR 实际来自 VLA-IAP 而非 EfficientVLA（根据我的检索，EfficientVLA 在 CogACT 上的数字是 0.6% SR drop，而非 97.8%）；(b) 引用第三方结果来支撑\"our findings span three models\"有归因问题——这些结果不是作者产出的。\n- 建议：准确引用数字来源（确认 97.8% 到底来自哪篇论文），并将 EfficientVLA 结果表述为\"independent corroboration\"而非本文 contribution 的一部分。\n\n---\n\n## 小问题（不影响接收）\n\n- **S1**: Figure 1 caption（experimental_setup.tex line 12-13）过长（4 行文字），超出了 caption 应有的简洁度。可将 hypothesis 部分移至正文。\n- **S2**: Abstract 约 220 words，在 150-250 区间内但偏长，包含了过多数字细节（\"7 of 128\"、\"Wilson 95% CI\"、\"$k{=}0.95$\"）——这些更适合放在 Results 中。\n- **S3**: Section 3 title 是 \"Experimental Setup\" 但包含了 Smart Compress 的方法描述（Section 3.4），这属于 method 而非 setup。考虑将 Section 标题改为 \"Methods and Setup\" 或将 Smart Compress 独立成一节。\n- **S4**: \"flow matching action head\" (Section 2/Background) 中的 flow matching 概念在 experimental_setup 中也被重新描述，存在轻微冗余。\n- **S5**: 引用 verify 结果显示 `jabbour2025dontrun` (Don't Run with Scissors) 在 OpenAlex 中 not_found——可能是尚未被索引的 arXiv preprint，不影响 validity 但需确认 arXiv ID 正确。\n- **S6**: `background.tex` 和 `experiments_deprecated.tex` 存在于 paper 目录但未被 `main.tex` include。如提交源码包，应清理这些 orphan 文件。\n\n---\n\n## Missing References\n\n1. **CogACT 本身**：论文通过 EfficientVLA 间接引用 CogACT 的结果，但未直接引用 CogACT 原始论文。如果声称\"findings span three models\"之一是 CogACT，应给出原始 citation。\n2. **OpenVLA-OFT**：Compressor-VLA 的 baseline 是 OpenVLA-OFT（fine-tuned version with 97.3% SR），论文 Related Work 提到了 Compressor-VLA 但未引用 OpenVLA-OFT 本身。由于 OpenVLA-OFT 在 LIBERO 上的 97.3% 是当前 SOTA 级别性能，值得作为 baseline reference。\n3. **TokenPacker / TinyLLaVA**: 作为 VLM token efficiency 的相关工作，TokenPacker 等使用 spatial-aware compression，与 pixel-shuffle 问题相关。\n\n---\n\n## 主要优势\n\n- **S1: 实验设计的控制严谨性**: 7 configurations × 3 mechanisms × 2 checkpoints × 3 suites 的 ablation，加上 extended training control 和 M=128 passthrough control，使得 diagnostic claim（\"re-encoding > deletion\"）的证据链比较完整。Wilson CI 的使用在 VLA 文献中不常见，体现了统计严谨性。\n- **S2: Cliff-edge 发现的实际价值**: 即使从 novelty 角度有 concurrent work 重叠，\"pixel-shuffle VLA + 5% token removal = 完全失败\"的量化结果对 practitioners 有直接警示意义，尤其是在多篇 concurrent work 仅在 MLP-projector 架构上报告成功的背景下。\n- **S3: 诚实的 framing**: 论文将 Smart Compress 定位为 \"diagnostic experiment\" 而非 method contribution，承认 scale confound，标注 concurrent work。这种诚实度在 submission 中不常见。\n- **S4: 写作质量**: 全文逻辑连贯，无 AI 写作痕迹（无解释性 em-dash、无 -ing phrase 结尾、无过度分段），术语首次出现有定义（SigLIP, ACIS 等），图表 caption 自包含。\n- **S5: Offline metric disconnect 分析 (Section 5.4)**: 展示了 offline action error（3.4×）掩盖 catastrophic gripper inversions 的分析有教育意义，reinforces closed-loop evaluation 的重要性。\n\n---\n\n## Questions to Authors\n\n1. 是否有在相同 backbone（如 Qwen2-0.5B）上替换 SmolVLA 的 pixel-shuffle 为 MLP projector 的 ablation 实验？这是解耦 connector vs. scale 的最直接方法。\n2. Smart Compress 在 official SmolVLA checkpoint（87.3% baseline）上是否也测试过？如果 re-encoding 在 strong baseline 上的 marginal gain 很小，则 \"re-encoding overcomes cliff-edge\" 的 claim 需要重新考虑。\n3. Section 5.1 提到 entropy ratio 0.95 vs 0.64，Introduction 提到 CogACT (via EfficientVLA) 作为第三个数据点。CogACT 的 entropy ratio 是多少？如果已测量但未报告，应加入 Figure 3。\n4. \"See What Matters\" (ICML 2026) 在 SmolVLA 上用 continuous resampling 保留 <10% tokens 仍然 work。这与本文的 \"pixel-shuffle tokens resist any form of deletion\" 形成什么关系？continuous resampling 本质上也是一种 re-encoding，这是否意味着本文的 diagnostic insight（re-encoding > deletion）已被独立验证？建议在 Discussion 中更深入地与此 concurrent work 对话。\n\n---\n\n## Overall Assessment Summary\n\n这是一篇实验执行认真、writing 质量不错的 empirical study，核心发现（pixel-shuffle cliff-edge at 5% removal）有 practical value。但在以下三个维度上未达到 CoRL 接收门槛：\n\n1. **Novelty**: 在 concurrent work 高度密集的 landscape 中（至少 7 篇直接相关 concurrent work，其中 \"See What Matters\" 已 accepted at ICML 2026 且同样在 SmolVLA 上工作），本文的 marginal contribution 偏小。\"First systematic comparison\" 的 claim 在 concurrent work 分别覆盖各 connector 类型的背景下不够 compelling。\n2. **Soundness of causal claim**: 0.5B vs 7B 的 scale confound 是核心弱点。论文的标题和 framing 做出了关于 \"the role of vision connectors\" 的因果声明，但实验设计无法排除 model scale 作为 alternative explanation。\n3. **CoRL venue fit**: Simulation-only evaluation 在 CoRL 的 expectation 下偏弱，尤其当贡献主要是 empirical observation 而非 novel method 时。\n\n**Recommendation: Weak Reject (4/10)**。如果作者能在 rebuttal 中提供 matched-scale 实验或 real-robot pilot study 以回应 N1 和 N3，评分有上调空间（至 borderline）。",
    "reviewer_id": "2",
    "project": "importance_margin_vla_compress"
  }
}
```

</details>

---


### Tool result

_source line 231 · 2026-05-19T05:53:40.842487+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4471
}
```

</details>

---


### Assistant

_source line 232 · 2026-05-19T05:53:48.986393+00:00_

审稿意见已提交给 Review Director。

总结：给出 **Weak Reject (4/10)** 评分，主要基于三个 critical issues：

1. **Scale confound 未解耦**：0.5B vs 7B（14× 差异）使得 connector-level 因果归因不可靠
2. **Novelty 在 concurrent work 密集背景下不足**：至少 7 篇直接相关 concurrent work，"See What Matters"（ICML 2026）已在 SmolVLA 上解决同一问题，Compressor-VLA 的 cross-attention 方案远优于 Smart Compress
3. **Simulation-only 评估**：对 CoRL venue fit 不利

优势方面肯定了实验控制的严谨性（7 configurations, passthrough control, Wilson CI）、cliff-edge 发现的 practical value、以及诚实的 framing。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2"
}
```

</details>

---


## Round 6

## Round 6

4 recorded events


### User

_source line 233 · 2026-05-19T05:54:35.286285+00:00_

[Round 1 审稿请求]:
## Step 2 — 交叉分享：请回应 Reviewer 1 的审稿意见

以下是 Reviewer 1 的完整审稿原文。请逐条回应其 Must-Fix 和 Should-Fix 问题：
- **[AGREE]**：同意该观点，并说明理由或补充你的视角
- **[REBUT]**：反驳该观点，提供具体证据（cite 论文中的 Section/Table/Figure）

你不需要回应小问题，但如果你有强烈意见也可以补充。

---

### Reviewer 1 的完整审稿意见：

**Overall: 5/10 (Marginally below acceptance threshold)**, Confidence: 4/5

**Must-Fix:**

**N1** [critical] Connector vs. Scale 因果混淆未解决
- SmolVLA (0.5B) vs OpenVLA (7B) 同时变动 connector 类型和 model scale。Section 5.3 的四条间接证据均非 definitive：(1) official checkpoint 仍是同一架构；(2) k=0.95 崩溃可能因小模型对扰动更敏感；(3) entropy ratio 可能受 scale 影响；(4) 4×4 folding 是最强论据但仍是 necessary condition。
- 建议：matched scale experiment 或显著弱化 claim。

**N2** [critical] SmolVLA baseline 复现质量严重偏低
- 两层差距：(a) 自训练 44.8% vs 官方 87.3%（batch size 4 vs 512）；(b) 官方 checkpoint 在本文评估中仅 59.2% vs 官方报告 87.3%（28pp gap 未解释，可能评估协议存在系统性差异）。Undertrained 模型可能更脆弱，放大 pruning 影响。
- 建议：详细说明评估协议差异来源，在更高质量 checkpoint 上验证 cliff-edge。

**N3** [critical] 统计验证不足
- 仅 2 seeds（42, 43），M=96 half-range ±2.8pp。CoRL 通常期望 3-5 seeds。
- 实验设计不对称：SmolVLA 7 种配置 + Smart Compress + cross-suite；OpenVLA 仅 random pruning × 5 ratios，单一 suite。
- 建议：增加到 ≥3 seeds，补充 OpenVLA 的 learned pruning 和 cross-suite 评估。

**Should-Fix:**

**W1** Smart Compress 增益归因不 clean——未排除 "额外 22.2M 参数容量" 本身的贡献。M=128 passthrough 仍包含 cross-attention 参数。更干净的 control 是 matched-parameter MLP adapter。

**W2** Entropy ratio 作为 compressibility predictor 仅 2 个数据点，Section 5.5 的 >0.9 threshold 无 empirical backing。

**W3** Cross-suite evaluation（LIBERO-Goal −6.6pp）未在正文分析原因。

**W4** Smart Compress 仅 6% latency gain (1.06×)。"VLA inference acceleration" 的 motivating scenario 在 SmolVLA (128 tokens) 上几乎不成立。

**Questions:**
1. 官方 checkpoint 59.2% vs 官方报告 87.3% 的 28pp gap 的来源？
2. 是否尝试过更大 batch size 的 baseline？
3. CogACT 的 entropy ratio？
4. Smart Compress M=128 (59.8%) ≈ official checkpoint (59.2%)——cross-attention 是否在修复 batch-size 不足？
5. 为何不在 OpenVLA 上也训练 Smart Compress？

---

请逐条回应 Must-Fix (N1-N3) 和 Should-Fix (W1-W4)。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 234 · 2026-05-19T05:56:14.123718+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 2 — 交叉回应 Reviewer 1 审稿意见\n\n---\n\n### Must-Fix 回应\n\n**[AGREE] R1-N1: Connector vs. Scale 因果混淆未解决**\n\n完全同意。这与我的 N1 一致。补充一点：R1 指出 \"4×4 folding 是 necessary condition 而非 sufficient condition\"，这个表述比我更精确。pixel-shuffle 的 mechanistic account 解释了**为什么**每个 token 信息密度高，但没有排除小模型**额外的**脆弱性。举例：一个 7B 模型 + pixel-shuffle connector 是否也会 cliff-edge？如果不会，则 scale 是 contributing factor。论文的标题直接声称 \"The Role of Vision Connectors\"，这是一个因果声明，但实验证据只支持 correlation。\n\n---\n\n**[AGREE with nuance] R1-N2: SmolVLA baseline 复现质量严重偏低**\n\n同意核心观点，但认为严重程度需分层讨论。\n\nR1 提出的两层差距中，第二层更为关键：官方 checkpoint 在本文评估中仅 59.2%，vs 官方报告 87.3%，28pp gap 未被解释。论文 Section 4.1 的 footnote 仅解释了自训练 checkpoint 的 batch size 差异，但对官方 checkpoint 的评估差距完全没有讨论。可能的解释包括：(a) 官方 87.3% 可能是跨所有 LIBERO 四个 suite 的平均值（含 LIBERO-Long），而本文仅测 Object suite 的 59.2%；(b) 评估 episode 数、initial state 采样、action frequency 等协议差异。但论文应该 explicitly 说明这一点。\n\n不过，我认为这**不影响 cliff-edge 发现本身的 validity**：59.2% → 0% 在同一评估协议下是 internally consistent 的。问题在于 Smart Compress 的全部实验基于 44.8% 的 weak baseline，re-encoding 的 +15pp gain 在 strong baseline 下是否 preserved 是 open question（我的 W2 也提到这点）。\n\nR1 Question 4 的观察非常敏锐：Smart Compress M=128 (59.8%) ≈ official checkpoint (59.2%)。如果 cross-attention module 本质上在补偿 undertrained VLA weights 而非 re-encoding vision tokens，则 \"re-encoding overcomes cliff-edge\" 的 claim 被 confounded。这个角度我之前没有充分考虑，值得在 rebuttal 中要求作者回应。\n\n---\n\n**[AGREE with addition] R1-N3: 统计验证不足**\n\n同意 2 seeds 不够（我的 W3 也提出）。R1 额外指出的**实验设计不对称**是一个我未充分强调的有效观点：\n\n- SmolVLA: 7 pruning configs + 5 Smart Compress levels + 3 suites + 2 checkpoints + multi-seed → 大量资源\n- OpenVLA: 仅 random pruning × 5 ratios，单一 suite (LIBERO-Object)，无 learned scoring，无 cross-suite\n\n这种不对称削弱了 cross-architecture comparison 的说服力。如果 OpenVLA 也在 LIBERO-Spatial/Goal 上测试，并使用 learned scorer（如 ACIS 或 attention-based），则\"graceful degradation\"的 claim 会更强。当前结果仅说明 OpenVLA 在 LIBERO-Object 上 under random pruning 有 graceful degradation，generalizability 未知。\n\n---\n\n### Should-Fix 回应\n\n**[AGREE] R1-W1: Smart Compress 增益归因——matched-parameter control 缺失**\n\n同意 R1 的建议比论文当前 control 更干净。论文的 extended training control 训练 ~100M VLA 参数但不添加新模块；Smart Compress 在此基础上额外添加 22.2M cross-attention 参数。虽然 22.2M 相对 ~100M 已训练参数而言较小，但 cross-attention 的 architectural inductive bias（跨 token 聚合）可能是 gain 的 key driver，而非\"re-encoding\"这个更泛的概念。一个 matched-parameter MLP adapter（22.2M 参数，per-token 独立处理）如果也产生类似 gain，则说明 gain 来自额外容量而非 cross-token re-encoding；如果 MLP adapter 不 work，则更强地支撑 \"re-encoding as causal factor\" 的 claim。\n\n不过我也注意到一个 mitigating factor：M=128 passthrough control 已经 work（59.8%），说明即使不做 compression，仅 cross-attention re-encoding 就有 gain。这排除了\"compression artifact\"但没有排除\"extra capacity\"。总体同意 R1 这是 should-fix 而非 must-fix。\n\n---\n\n**[AGREE] R1-W2: Entropy ratio 仅 2 个数据点**\n\n完全同意，与我的 W4 一致。2 个数据点不足以建立 predictive utility，>0.9 threshold 是 post-hoc interpolation。\n\n---\n\n**[AGREE] R1-W3: Cross-suite LIBERO-Goal drop 未分析**\n\n与我的 W1 一致。补充：LIBERO-Goal 的 -6.6pp 下降可能意味着 Smart Compress 的 cross-attention queries 过拟合了 Object suite 的 task structure（如特定物体的 visual saliency pattern）。如果 re-encoding 需要 task-specific training，其 practical value 大打折扣（每个 task 训 6-7 小时，Appendix Table 9）。\n\n---\n\n**[AGREE] R1-W4: 6% latency gain 与 motivation 不匹配**\n\n这是一个我未充分强调的有效观点。论文 Introduction 的核心 motivation 是 \"reducing these tokens would yield immediate speedups in the quadratically scaling attention computation\"（Introduction, line 4），但 Appendix Section D 承认 SmolVLA 的 128 tokens 上 self-attention 不是 inference bottleneck，实际 latency gain 仅 6%。这构成 motivation-result 的叙事断裂。\n\n论文 Section 5.5 的 Design Implication 3 说 \"inserting a cross-attention re-encoding module (22.2M parameters, 6–7 hours training) can restore token compressibility\"，但如果实际 speedup 可忽略，\"restore compressibility\" 的 practical meaning 存疑。论文辩称 \"for larger VLA models (7B+), the same 75% reduction would yield substantially larger latency gains\"，但这是 speculation 而非 evidence——论文并未在 7B 模型上测试 Smart Compress。\n\n---\n\n### 对 R1 Questions 的补充意见\n\n**Q4 (Smart Compress M=128 ≈ official checkpoint)**：这是本轮交叉审稿中我认为最尖锐的观察。如果 Smart Compress 的 gain 本质上是在修复 batch-size 不足导致的 undertrained representation（即 cross-attention 提供了一种替代性的 representation alignment，弥补了 training 不足），那么在 properly trained checkpoint 上 gain 可能消失。这直接挑战了 Contribution 3 (\"diagnostic re-encoding experiment\") 的 generalizability。建议 R1 在 rebuttal 阶段将此作为 key question。\n\n**Q5 (OpenVLA 上训练 Smart Compress)**：同意这是一个重要的 missing experiment。如果 Smart Compress 在 OpenVLA 上也有类似 +15pp gain，则说明 re-encoding 是 universally beneficial（与 connector 无关），削弱了 connector-specific 的叙事；如果 OpenVLA 上 gain 很小，则支持 \"re-encoding 特别有利于 pixel-shuffle\" 的 claim。无论哪个结果都有 informational value。\n\n---\n\n### 总结\n\nR1 的审稿与我的评估高度一致，尤其在 scale confound (N1)、baseline 质量 (N2 vs 我的 W2)、统计不足 (N3 vs 我的 W3) 方面。R1 额外贡献了两个我未充分挖掘的角度：(1) 实验设计不对称（OpenVLA 评估远不如 SmolVLA 全面）；(2) Smart Compress M=128 ≈ official checkpoint 的 confound 观察。这两点均进一步支持 Weak Reject 的评分。\n\n我维持 **4/10 (Weak Reject)** 的评分不变。如果 R1 的 5/10 borderline 评分上调需要 rebuttal 回应 N1+N2，我认为同样的 rebuttal 标准也适用于我的评分上调条件。",
  "reviewer_id": "2",
  "project": "importance_margin_vla_compress"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 2 — 交叉回应 Reviewer 1 审稿意见\n\n---\n\n### Must-Fix 回应\n\n**[AGREE] R1-N1: Connector vs. Scale 因果混淆未解决**\n\n完全同意。这与我的 N1 一致。补充一点：R1 指出 \"4×4 folding 是 necessary condition 而非 sufficient condition\"，这个表述比我更精确。pixel-shuffle 的 mechanistic account 解释了**为什么**每个 token 信息密度高，但没有排除小模型**额外的**脆弱性。举例：一个 7B 模型 + pixel-shuffle connector 是否也会 cliff-edge？如果不会，则 scale 是 contributing factor。论文的标题直接声称 \"The Role of Vision Connectors\"，这是一个因果声明，但实验证据只支持 correlation。\n\n---\n\n**[AGREE with nuance] R1-N2: SmolVLA baseline 复现质量严重偏低**\n\n同意核心观点，但认为严重程度需分层讨论。\n\nR1 提出的两层差距中，第二层更为关键：官方 checkpoint 在本文评估中仅 59.2%，vs 官方报告 87.3%，28pp gap 未被解释。论文 Section 4.1 的 footnote 仅解释了自训练 checkpoint 的 batch size 差异，但对官方 checkpoint 的评估差距完全没有讨论。可能的解释包括：(a) 官方 87.3% 可能是跨所有 LIBERO 四个 suite 的平均值（含 LIBERO-Long），而本文仅测 Object suite 的 59.2%；(b) 评估 episode 数、initial state 采样、action frequency 等协议差异。但论文应该 explicitly 说明这一点。\n\n不过，我认为这**不影响 cliff-edge 发现本身的 validity**：59.2% → 0% 在同一评估协议下是 internally consistent 的。问题在于 Smart Compress 的全部实验基于 44.8% 的 weak baseline，re-encoding 的 +15pp gain 在 strong baseline 下是否 preserved 是 open question（我的 W2 也提到这点）。\n\nR1 Question 4 的观察非常敏锐：Smart Compress M=128 (59.8%) ≈ official checkpoint (59.2%)。如果 cross-attention module 本质上在补偿 undertrained VLA weights 而非 re-encoding vision tokens，则 \"re-encoding overcomes cliff-edge\" 的 claim 被 confounded。这个角度我之前没有充分考虑，值得在 rebuttal 中要求作者回应。\n\n---\n\n**[AGREE with addition] R1-N3: 统计验证不足**\n\n同意 2 seeds 不够（我的 W3 也提出）。R1 额外指出的**实验设计不对称**是一个我未充分强调的有效观点：\n\n- SmolVLA: 7 pruning configs + 5 Smart Compress levels + 3 suites + 2 checkpoints + multi-seed → 大量资源\n- OpenVLA: 仅 random pruning × 5 ratios，单一 suite (LIBERO-Object)，无 learned scoring，无 cross-suite\n\n这种不对称削弱了 cross-architecture comparison 的说服力。如果 OpenVLA 也在 LIBERO-Spatial/Goal 上测试，并使用 learned scorer（如 ACIS 或 attention-based），则\"graceful degradation\"的 claim 会更强。当前结果仅说明 OpenVLA 在 LIBERO-Object 上 under random pruning 有 graceful degradation，generalizability 未知。\n\n---\n\n### Should-Fix 回应\n\n**[AGREE] R1-W1: Smart Compress 增益归因——matched-parameter control 缺失**\n\n同意 R1 的建议比论文当前 control 更干净。论文的 extended training control 训练 ~100M VLA 参数但不添加新模块；Smart Compress 在此基础上额外添加 22.2M cross-attention 参数。虽然 22.2M 相对 ~100M 已训练参数而言较小，但 cross-attention 的 architectural inductive bias（跨 token 聚合）可能是 gain 的 key driver，而非\"re-encoding\"这个更泛的概念。一个 matched-parameter MLP adapter（22.2M 参数，per-token 独立处理）如果也产生类似 gain，则说明 gain 来自额外容量而非 cross-token re-encoding；如果 MLP adapter 不 work，则更强地支撑 \"re-encoding as causal factor\" 的 claim。\n\n不过我也注意到一个 mitigating factor：M=128 passthrough control 已经 work（59.8%），说明即使不做 compression，仅 cross-attention re-encoding 就有 gain。这排除了\"compression artifact\"但没有排除\"extra capacity\"。总体同意 R1 这是 should-fix 而非 must-fix。\n\n---\n\n**[AGREE] R1-W2: Entropy ratio 仅 2 个数据点**\n\n完全同意，与我的 W4 一致。2 个数据点不足以建立 predictive utility，>0.9 threshold 是 post-hoc interpolation。\n\n---\n\n**[AGREE] R1-W3: Cross-suite LIBERO-Goal drop 未分析**\n\n与我的 W1 一致。补充：LIBERO-Goal 的 -6.6pp 下降可能意味着 Smart Compress 的 cross-attention queries 过拟合了 Object suite 的 task structure（如特定物体的 visual saliency pattern）。如果 re-encoding 需要 task-specific training，其 practical value 大打折扣（每个 task 训 6-7 小时，Appendix Table 9）。\n\n---\n\n**[AGREE] R1-W4: 6% latency gain 与 motivation 不匹配**\n\n这是一个我未充分强调的有效观点。论文 Introduction 的核心 motivation 是 \"reducing these tokens would yield immediate speedups in the quadratically scaling attention computation\"（Introduction, line 4），但 Appendix Section D 承认 SmolVLA 的 128 tokens 上 self-attention 不是 inference bottleneck，实际 latency gain 仅 6%。这构成 motivation-result 的叙事断裂。\n\n论文 Section 5.5 的 Design Implication 3 说 \"inserting a cross-attention re-encoding module (22.2M parameters, 6–7 hours training) can restore token compressibility\"，但如果实际 speedup 可忽略，\"restore compressibility\" 的 practical meaning 存疑。论文辩称 \"for larger VLA models (7B+), the same 75% reduction would yield substantially larger latency gains\"，但这是 speculation 而非 evidence——论文并未在 7B 模型上测试 Smart Compress。\n\n---\n\n### 对 R1 Questions 的补充意见\n\n**Q4 (Smart Compress M=128 ≈ official checkpoint)**：这是本轮交叉审稿中我认为最尖锐的观察。如果 Smart Compress 的 gain 本质上是在修复 batch-size 不足导致的 undertrained representation（即 cross-attention 提供了一种替代性的 representation alignment，弥补了 training 不足），那么在 properly trained checkpoint 上 gain 可能消失。这直接挑战了 Contribution 3 (\"diagnostic re-encoding experiment\") 的 generalizability。建议 R1 在 rebuttal 阶段将此作为 key question。\n\n**Q5 (OpenVLA 上训练 Smart Compress)**：同意这是一个重要的 missing experiment。如果 Smart Compress 在 OpenVLA 上也有类似 +15pp gain，则说明 re-encoding 是 universally beneficial（与 connector 无关），削弱了 connector-specific 的叙事；如果 OpenVLA 上 gain 很小，则支持 \"re-encoding 特别有利于 pixel-shuffle\" 的 claim。无论哪个结果都有 informational value。\n\n---\n\n### 总结\n\nR1 的审稿与我的评估高度一致，尤其在 scale confound (N1)、baseline 质量 (N2 vs 我的 W2)、统计不足 (N3 vs 我的 W3) 方面。R1 额外贡献了两个我未充分挖掘的角度：(1) 实验设计不对称（OpenVLA 评估远不如 SmolVLA 全面）；(2) Smart Compress M=128 ≈ official checkpoint 的 confound 观察。这两点均进一步支持 Weak Reject 的评分。\n\n我维持 **4/10 (Weak Reject)** 的评分不变。如果 R1 的 5/10 borderline 评分上调需要 rebuttal 回应 N1+N2，我认为同样的 rebuttal 标准也适用于我的评分上调条件。",
    "reviewer_id": "2",
    "project": "importance_margin_vla_compress"
  }
}
```

</details>

---


### Tool result

_source line 235 · 2026-05-19T05:56:19.171194+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 5047
}
```

</details>

---


### Assistant

_source line 236 · 2026-05-19T05:56:23.386923+00:00_

交叉回应已提交。逐条回应了 R1 的 N1-N3（全部 AGREE）和 W1-W4（全部 AGREE），并补充了两个 R1 独到的观察角度：实验设计不对称和 Smart Compress M=128 ≈ official checkpoint 的 confound 问题。维持 4/10 Weak Reject 评分。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2"
}
```

</details>

---


## Round 7

## Round 7

112 recorded events


### User

_source line 237 · 2026-05-21T14:08:11.496094+00:00_

[Round 1 审稿请求]:
你是 Reviewer 2，负责审查新颖性、定位、和 venue fit。

## 投稿信息
- **Venue**: CoRL 2026（顶级机器人学习会议）
- **Deadline**: 2026-05-29
- **格式**: 8 页正文 + 附录/参考文献不计入页数限制
- **匿名规则**: Double-blind
- **模板**: corl_2026.sty

## 论文路径
- 主文件: `projects/importance_margin_vla_compress/docs/paper/main.tex`
- 各章节在同目录下（abstract.tex, introduction.tex, related_work.tex, experimental_setup.tex, results.tex, analysis.tex, conclusion.tex, appendix.tex）

## 你的审查侧重

### 1. 新颖性评估
- "Vision connector determines compressibility" 这个 finding 是否足够 novel？是否可从 pixel-shuffle/MLP 的已知属性直接推导？
- CV 作为 compressibility predictor 是否是 incremental contribution vs 真正的 insight？
- VTR 与 Q-Former/Perceiver/Compressor-VLA 的区别在哪里？是否只是 "在 SmolVLA 上做了已知方法"？
- 与 concurrent works（Compressor-VLA, SpecPrune-VLA, LightVLA, See What Matters, VLA-IAP, EfficientVLA, VLA-Pruner 等）的差异和增量贡献
- 四类 compressibility taxonomy 是否 genuinely novel 还是 a posteriori labeling？

### 2. Related Work 覆盖
- 是否遗漏了重要的 token pruning / VLA efficiency 相关工作？
- 引用第三方结果（CogACT via EfficientVLA 的 74.2% SR）是否恰当标注？
- Perceiver/Q-Former 类 connector 在 taxonomy 中的缺失是否是重大缺口？

### 3. Claims vs Evidence 比例
- "The vision connector, not model size or action head, determines pruning behavior" —— 证据是否支撑这个因果声明？
- "CV serves as a zero-cost dual predictor" —— 3 个数据点够不够？
- "falsifies the 'immune' assumption" —— π₀ 的 offline 评估是否真的做了 "immune" 的 claim？
- Contribution 1 说 "evaluating seven models" 但其中 π₀ 仅 offline、OFT 仅 entropy/CV、CogACT 是引用——实际 closed-loop 评估了几个？
- "Diagnose-then-Compress framework" 是否 oversells 一组 empirical observations？

### 4. CoRL Venue Fit
- CoRL 偏好 real-robot 实验。本文纯 simulation（LIBERO only）是否是 critical weakness？
- Empirical analysis paper 在 CoRL 的历史接受情况如何？
- 论文对 robotics community 的 actionable value 是什么？

### 5. Framing 和写作
- 标题是否准确反映内容？"Why Token Pruning Crashes Some Robot Policies but Not Others" 是否过于 catchy 而非 precise？
- Abstract 密度是否过高？information overload？
- 全文 claim 语言强度是否与证据匹配？（"strongly linked to", "primarily shaped by", "determines" 等）

请按以下格式输出审稿意见：
1. Summary（2-3 句）
2. Strengths（逐条）
3. Weaknesses（逐条，分 Must-Fix / Should-Fix / Minor）
4. Questions for Authors
5. Missing References（如有）
6. Overall Score（strong reject / weak reject / borderline / weak accept / strong accept）+ Confidence（low / medium / high）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 238 · 2026-05-21T14:08:19.932083+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/.claude/skills/review-reviewer-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/.claude/skills/review-reviewer-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 239 · 2026-05-21T14:08:20.795348+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/.claude/sessions/review_reviewer_2_29d69ba3.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 863
}
```

</details>

---


### Tool call

_source line 240 · 2026-05-21T14:08:20.797521+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director,mcp__agent-ml-research__verify_references,WebSearch,WebFetch",
  "max_results": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director,mcp__agent-ml-research__verify_references,WebSearch,WebFetch",
    "max_results": "5"
  }
}
```

</details>

---


### Tool result

_source line 241 · 2026-05-21T14:08:20.797789+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 242 · 2026-05-21T14:08:25.876711+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "CoRL 2026 reviewer guidelines review form criteria"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "CoRL 2026 reviewer guidelines review form criteria"
  }
}
```

</details>

---


### Tool call

_source line 243 · 2026-05-21T14:08:26.830451+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/main.pdf",
  "project": "importance_margin_vla_compress",
  "pages": "1-10",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/main.pdf",
    "project": "importance_margin_vla_compress",
    "pages": "1-10",
    "dpi": "150"
  }
}
```

</details>

---


### Tool call

_source line 244 · 2026-05-21T14:08:27.437725+00:00_

called mcp__agent-ml-research__verify_references

<details open><summary>🔧 Tool call — mcp__agent-ml-research__verify_references</summary>

```json
{
  "paper_dir": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper",
  "project": "importance_margin_vla_compress"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "mcp__agent-ml-research__verify_references",
  "tool_args": {
    "paper_dir": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper",
    "project": "importance_margin_vla_compress"
  }
}
```

</details>

---


### Tool result

_source line 245 · 2026-05-21T14:08:32.717265+00:00_

Web search results for query: "CoRL 2026 reviewer guidelines review form criteria"

Links: [{"title":"CoRL 2026 - Instruction for Authors","url":"https://www.corl.org/contributions/instruction-for-authors"},{"title":"ICLR 2026 Reviewer Guide","url":"https://iclr.cc/Conferences/2026/ReviewerGuide"},{"title":"CoRL 2026 - Call for Papers","url":"https://www.corl.org/contributions/call-for-papers"},{"title":"Reviewer Guidelines — CoRL 2023","url":"https://www.corl2023.org/reviewer-guidelines"},{"title":"CVPR 2026 Reviewer Guidelines","url":"https://cvpr.thecvf.com/Conferences/2026/ReviewerGuidelinesq"},{"title":"Which Coauthor Should I Nominate in My 99 ICLR Submissions? A Mathematical Analysis of the ICLR 2026 Reciprocal Reviewer Nomination Policy","url":"https://arxiv.org/pdf/2512.17950"},{"title":"CoRL 2024 - Instruction for Reviews","url":"https://2024.corl.org/contributions/instruction-for-reviews"}]

Based on the search results, I found information about CoRL 2026, though specific detailed reviewer guidelines and review form criteria for 2026 were not fully available in the results. Here's what I found:

## CoRL 2026 Reviewer Requirements

All submissions must include at least one author who agrees to serve as a CoRL reviewer. They are qualified if they have at least one accepted publication at a previous robotics (CoRL/ ICRA/ IROS/ RSS) or learning conference (ICLR/ NeurIPS/ ICML) or equivalent journal.

Additionally, every author with 3 or more submissions must agree to serve as a reviewer.

## Submission Focus and Evaluation

Submissions should focus on a core robotics problem and demonstrate the relevance of proposed models, algorithms, datasets, and benchmarks to robotics. All submissions should include a Limitations section, explicitly describing limiting assumptions, failure modes, and other limitations of the results and experiments and how these might be addressed in the future.

Unfortunately, the search results did not contain the complete and detailed 
…[truncated 454 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 6840
}
```

</details>

---


### Tool result

_source line 246 · 2026-05-21T14:08:33.822847+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 1, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/_pdf_images/main_p1.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 316.1}, {\"page\": 2, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/_pdf_images/main_p2.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 420.7}, {\"page\": 3, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/_pdf_images/main_p3.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 358.0}, {\"page\": 4, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/_pdf_images/main_p4.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 317.8}, {\"page\": 5, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/_pdf_images/main_p5.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 372.7}, {\"page\": 6, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/_pdf_images/main_p6.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 364.1}, {\"page\": 7, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/_pdf_images/main_p7.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 369.0}, {\"page\": 8, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/_pdf_images/main_p8.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 388.3}, {\"page\": 9, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/_pdf_images/main_p9.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 329.9}, {\"page\": 10, \"path\": \"/home/ubuntu/.agent
…[truncated 399 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 6992
}
```

</details>

---


### Tool result

_source line 247 · 2026-05-21T14:12:55.107275+00:00_

{"result":"{\"success\": true, \"data\": {\"summary\": {\"total_bib_entries\": 41, \"total_citations\": 89, \"unique_cited_keys\": 41, \"orphan_bib\": 0, \"missing_bib\": 0, \"duplicate_keys\": 0, \"online_verified\": 30, \"online_not_found\": 5, \"online_mismatch\": 6}, \"cross_check\": {\"orphan_bib\": [], \"missing_bib\": [], \"orphan_count\": 0, \"missing_count\": 0}, \"bib_entries\": [{\"key\": \"gao2025compressorvla\", \"type\": \"article\", \"title\": \"Compressor-VLA: Instruction-Guided Visual Token Compression for Efficient Robotic Manipulation\", \"authors\": \"Gao, Juntao and Ye, Feiyang and Zhang, Jing and Qian, Wenjing\", \"year\": \"2025\", \"venue\": \"arXiv preprint arXiv:2511.18950\"}, {\"key\": \"wang2025specprunevla\", \"type\": \"article\", \"title\": \"SpecPrune-VLA: Accelerating Vision-Language-Action Models via Action-Aware Self-Speculative Pruning\", \"authors\": \"Wang, Hanzhen and Xu, Jiaming and Xiang, Yushun and Pan, Jiayi and Zhou, Yongkan...\", \"year\": \"2025\", \"venue\": \"arXiv preprint arXiv:2509.05614\"}, {\"key\": \"jiang2026lightvla\", \"type\": \"inproceedings\", \"title\": \"The Better You Learn, The Smarter You Prune: Towards Efficient Vision-Language-Action Models via Differentiable Token Pr...\", \"authors\": \"Jiang, Titong and Jiang, Xuefeng and Ma, Yuan and Wen, Xin and Li, Bailin and Zh...\", \"year\": \"2026\", \"venue\": \"Proceedings of the IEEE International Conference on Robotics and Automation (ICR...\"}, {\"key\": \"feng2026seewhatmatters\", \"type\": \"inproceedings\", \"title\": \"See What Matters: Differentiable Grid Sample Pruning for Generalizable Vision-Language-Action Model\", \"authors\": \"Feng, Yixu and Zhao, Zinan and Ma, Yanxiang and Xia, Chenghao and Du, Chengbin a...\", \"year\": \"2026\", \"venue\": \"Proceedings of the Forty-Third International Conference on Machine Learning (ICM...\"}, {\"key\": \"zhang2025sparsevlm\", \"type\": \"inproceedings\", \"title\": \"SparseVLM: Visual Token Sparsificat
…[truncated 35395 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "mcp__agent-ml-research__verify_references",
  "elapsed_ms": 267669
}
```

</details>

---


### Tool call

_source line 248 · 2026-05-21T14:13:03.546288+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/_pdf_images/main_p1.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/_pdf_images/main_p1.png"
  }
}
```

</details>

---


### Tool result

_source line 249 · 2026-05-21T14:13:04.450313+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/.claude/sessions/review_reviewer_2_29d69ba3.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 904
}
```

</details>

---


### Tool call

_source line 250 · 2026-05-21T14:13:04.751798+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/_pdf_images/main_p2.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/_pdf_images/main_p2.png"
  }
}
```

</details>

---


### Tool result

_source line 251 · 2026-05-21T14:13:04.752409+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/.claude/sessions/review_reviewer_2_29d69ba3.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 252 · 2026-05-21T14:13:04.903308+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/_pdf_images/main_p3.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/_pdf_images/main_p3.png"
  }
}
```

</details>

---


### Tool result

_source line 253 · 2026-05-21T14:13:04.953904+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/.claude/sessions/review_reviewer_2_29d69ba3.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 254 · 2026-05-21T14:13:05.525383+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/_pdf_images/main_p4.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/_pdf_images/main_p4.png"
  }
}
```

</details>

---


### Tool result

_source line 255 · 2026-05-21T14:13:06.329160+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/.claude/sessions/review_reviewer_2_29d69ba3.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 803
}
```

</details>

---


### Tool call

_source line 256 · 2026-05-21T14:13:06.380172+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/_pdf_images/main_p5.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/_pdf_images/main_p5.png"
  }
}
```

</details>

---


### Tool result

_source line 257 · 2026-05-21T14:13:06.782675+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/.claude/sessions/review_reviewer_2_29d69ba3.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 402
}
```

</details>

---


### Tool call

_source line 258 · 2026-05-21T14:13:06.783109+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/_pdf_images/main_p6.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/_pdf_images/main_p6.png"
  }
}
```

</details>

---


### Tool result

_source line 259 · 2026-05-21T14:13:07.336086+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/.claude/sessions/review_reviewer_2_29d69ba3.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 552
}
```

</details>

---


### Tool call

_source line 260 · 2026-05-21T14:13:07.386937+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/_pdf_images/main_p7.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/_pdf_images/main_p7.png"
  }
}
```

</details>

---


### Tool result

_source line 261 · 2026-05-21T14:13:08.193334+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/.claude/sessions/review_reviewer_2_29d69ba3.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 806
}
```

</details>

---


### Tool call

_source line 262 · 2026-05-21T14:13:08.394584+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/_pdf_images/main_p8.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/_pdf_images/main_p8.png"
  }
}
```

</details>

---


### Tool result

_source line 263 · 2026-05-21T14:13:08.796732+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/.claude/sessions/review_reviewer_2_29d69ba3.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 402
}
```

</details>

---


### Tool call

_source line 264 · 2026-05-21T14:13:09.750939+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://2024.corl.org/contributions/instruction-for-reviews",
  "prompt": "Extract the complete review form criteria, scoring dimensions, rating scales, and reviewer guidelines for CoRL 2024. List all evaluation dimensions with their descriptions and score ranges."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://2024.corl.org/contributions/instruction-for-reviews",
    "prompt": "Extract the complete review form criteria, scoring dimensions, rating scales, and reviewer guidelines for CoRL 2024. List all evaluation dimensions with their descriptions and score ranges."
  }
}
```

</details>

---


### Tool result

_source line 265 · 2026-05-21T14:13:13.466347+00:00_

# CoRL 2024 Review Criteria Summary

Based on the provided content, CoRL 2024 offers limited detail on a complete review form. Here's what is specified:

## Review Criteria for Regular Papers

Papers are evaluated on:
- **Significance and Novelty**: "significance and novelty of the results, either theoretical or empirical"
- **Objectivity and Impact**: "degree to which they have been objectively established and/or their potential for scientific and technological impact"
- **Relevance**: Applicability to robotic learning

## Scope Requirements (Desk Reject Criteria)

Submissions must demonstrate relevance through either:
- **Intent**: Explicitly address a learning question for physical robots
- **Outcome**: Test the proposed learning solution on physical robots

## Notable Absence

The document provided does **not include**:
- Specific numerical rating scales
- Detailed scoring dimensions (clarity, reproducibility, etc.)
- Complete review form structure
- Guidance on how to assign numerical scores

The page focuses primarily on desk rejection criteria and reviewer qualifications rather than the detailed rubric for evaluating accepted submissions. A complete review form would likely be available through the submission system or reviewer guidelines distributed separately.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 3715
}
```

</details>

---


### Tool call

_source line 266 · 2026-05-21T14:13:17.232041+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/_pdf_images/*.png",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/_pdf_images/*.png",
    "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper"
  }
}
```

</details>

---


### Tool result

_source line 267 · 2026-05-21T14:13:17.283751+00:00_

/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/figures/paper/_pdf_images/fig_degradation_curve_p1.png

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Glob",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 268 · 2026-05-21T14:13:22.153572+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/_pdf_images/ 2>/dev/null || echo \"DIR_NOT_FOUND\"",
  "description": "Check if pdf images directory exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/_pdf_images/ 2>/dev/null || echo \"DIR_NOT_FOUND\"",
    "description": "Check if pdf images directory exists"
  }
}
```

</details>

---


### Tool result

_source line 269 · 2026-05-21T14:13:22.305491+00:00_

DIR_NOT_FOUND

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Bash",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 270 · 2026-05-21T14:13:44.518029+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/main.pdf",
  "project": "importance_margin_vla_compress",
  "pages": "1-5",
  "dpi": "150",
  "output_dir": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/.claude/sessions/review_reviewer_2_29d69ba3/_pdf_images"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/main.pdf",
    "project": "importance_margin_vla_compress",
    "pages": "1-5",
    "dpi": "150",
    "output_dir": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/.claude/sessions/review_reviewer_2_29d69ba3/_pdf_images"
  }
}
```

</details>

---


### Tool result

_source line 271 · 2026-05-21T14:13:45.020432+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 1, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/.claude/sessions/review_reviewer_2_29d69ba3/_pdf_images/main_p1.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 316.1}, {\"page\": 2, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/.claude/sessions/review_reviewer_2_29d69ba3/_pdf_images/main_p2.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 420.7}, {\"page\": 3, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/.claude/sessions/review_reviewer_2_29d69ba3/_pdf_images/main_p3.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 358.0}, {\"page\": 4, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/.claude/sessions/review_reviewer_2_29d69ba3/_pdf_images/main_p4.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 317.8}, {\"page\": 5, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/.claude/sessions/review_reviewer_2_29d69ba3/_pdf_images/main_p5.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 372.7}], \"total_pages\": 25, \"rendered_pages\": 5, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/.claude/sessions/review_reviewer_2_29d69ba3/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 272 · 2026-05-21T14:13:47.279675+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/.claude/sessions/review_reviewer_2_29d69ba3/_pdf_images/main_p1.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/.claude/sessions/review_reviewer_2_29d69ba3/_pdf_images/main_p1.png"
  }
}
```

</details>

---


### Tool result

_source line 273 · 2026-05-21T14:13:48.235832+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 956
}
```

</details>

---


### Tool call

_source line 274 · 2026-05-21T14:13:48.236363+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/.claude/sessions/review_reviewer_2_29d69ba3/_pdf_images/main_p2.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/.claude/sessions/review_reviewer_2_29d69ba3/_pdf_images/main_p2.png"
  }
}
```

</details>

---


### Tool call

_source line 275 · 2026-05-21T14:13:48.688195+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/.claude/sessions/review_reviewer_2_29d69ba3/_pdf_images/main_p3.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/.claude/sessions/review_reviewer_2_29d69ba3/_pdf_images/main_p3.png"
  }
}
```

</details>

---


### Tool result

_source line 276 · 2026-05-21T14:13:49.633106+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1396
}
```

</details>

---


### Tool result

_source line 277 · 2026-05-21T14:13:49.634624+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 946
}
```

</details>

---


### Tool call

_source line 278 · 2026-05-21T14:13:49.634878+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/.claude/sessions/review_reviewer_2_29d69ba3/_pdf_images/main_p4.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/.claude/sessions/review_reviewer_2_29d69ba3/_pdf_images/main_p4.png"
  }
}
```

</details>

---


### Tool result

_source line 279 · 2026-05-21T14:13:50.039337+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 404
}
```

</details>

---


### Tool call

_source line 280 · 2026-05-21T14:13:50.039784+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/.claude/sessions/review_reviewer_2_29d69ba3/_pdf_images/main_p5.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/.claude/sessions/review_reviewer_2_29d69ba3/_pdf_images/main_p5.png"
  }
}
```

</details>

---


### Tool result

_source line 281 · 2026-05-21T14:13:50.393646+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 353
}
```

</details>

---


### Tool call

_source line 282 · 2026-05-21T14:14:00.331767+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/main.pdf",
  "project": "importance_margin_vla_compress",
  "pages": "6-10",
  "dpi": "150",
  "output_dir": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/.claude/sessions/review_reviewer_2_29d69ba3/_pdf_images2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/main.pdf",
    "project": "importance_margin_vla_compress",
    "pages": "6-10",
    "dpi": "150",
    "output_dir": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/.claude/sessions/review_reviewer_2_29d69ba3/_pdf_images2"
  }
}
```

</details>

---


### Tool result

_source line 283 · 2026-05-21T14:14:01.003986+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 6, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/.claude/sessions/review_reviewer_2_29d69ba3/_pdf_images2/main_p6.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 364.1}, {\"page\": 7, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/.claude/sessions/review_reviewer_2_29d69ba3/_pdf_images2/main_p7.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 369.0}, {\"page\": 8, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/.claude/sessions/review_reviewer_2_29d69ba3/_pdf_images2/main_p8.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 388.3}, {\"page\": 9, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/.claude/sessions/review_reviewer_2_29d69ba3/_pdf_images2/main_p9.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 329.9}, {\"page\": 10, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/.claude/sessions/review_reviewer_2_29d69ba3/_pdf_images2/main_p10.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 291.4}], \"total_pages\": 25, \"rendered_pages\": 5, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/.claude/sessions/review_reviewer_2_29d69ba3/_pdf_images2\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 672
}
```

</details>

---


### Tool call

_source line 284 · 2026-05-21T14:14:03.735378+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/.claude/sessions/review_reviewer_2_29d69ba3/_pdf_images2/main_p6.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/.claude/sessions/review_reviewer_2_29d69ba3/_pdf_images2/main_p6.png"
  }
}
```

</details>

---


### Tool result

_source line 285 · 2026-05-21T14:14:04.691627+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 956
}
```

</details>

---


### Tool call

_source line 286 · 2026-05-21T14:14:04.792713+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/.claude/sessions/review_reviewer_2_29d69ba3/_pdf_images2/main_p7.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/.claude/sessions/review_reviewer_2_29d69ba3/_pdf_images2/main_p7.png"
  }
}
```

</details>

---


### Tool result

_source line 287 · 2026-05-21T14:14:05.200836+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 408
}
```

</details>

---


### Tool call

_source line 288 · 2026-05-21T14:14:05.201351+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/.claude/sessions/review_reviewer_2_29d69ba3/_pdf_images2/main_p8.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/.claude/sessions/review_reviewer_2_29d69ba3/_pdf_images2/main_p8.png"
  }
}
```

</details>

---


### Tool result

_source line 289 · 2026-05-21T14:14:06.074952+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 873
}
```

</details>

---


### Tool call

_source line 290 · 2026-05-21T14:14:06.125629+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/.claude/sessions/review_reviewer_2_29d69ba3/_pdf_images2/main_p9.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/.claude/sessions/review_reviewer_2_29d69ba3/_pdf_images2/main_p9.png"
  }
}
```

</details>

---


### Tool result

_source line 291 · 2026-05-21T14:14:06.529638+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 404
}
```

</details>

---


### Tool call

_source line 292 · 2026-05-21T14:14:06.530164+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/.claude/sessions/review_reviewer_2_29d69ba3/_pdf_images2/main_p10.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/.claude/sessions/review_reviewer_2_29d69ba3/_pdf_images2/main_p10.png"
  }
}
```

</details>

---


### Tool result

_source line 293 · 2026-05-21T14:14:06.933803+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 403
}
```

</details>

---


### Tool call

_source line 294 · 2026-05-21T14:14:14.818041+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/main.pdf",
  "project": "importance_margin_vla_compress",
  "pages": "11-15",
  "dpi": "150",
  "output_dir": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/.claude/sessions/review_reviewer_2_29d69ba3/_pdf_images3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/main.pdf",
    "project": "importance_margin_vla_compress",
    "pages": "11-15",
    "dpi": "150",
    "output_dir": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/.claude/sessions/review_reviewer_2_29d69ba3/_pdf_images3"
  }
}
```

</details>

---


### Tool result

_source line 295 · 2026-05-21T14:14:15.270333+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 11, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/.claude/sessions/review_reviewer_2_29d69ba3/_pdf_images3/main_p11.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 372.0}, {\"page\": 12, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/.claude/sessions/review_reviewer_2_29d69ba3/_pdf_images3/main_p12.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 366.6}, {\"page\": 13, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/.claude/sessions/review_reviewer_2_29d69ba3/_pdf_images3/main_p13.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 361.1}, {\"page\": 14, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/.claude/sessions/review_reviewer_2_29d69ba3/_pdf_images3/main_p14.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 356.5}, {\"page\": 15, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/.claude/sessions/review_reviewer_2_29d69ba3/_pdf_images3/main_p15.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 339.7}], \"total_pages\": 25, \"rendered_pages\": 5, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/.claude/sessions/review_reviewer_2_29d69ba3/_pdf_images3\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 296 · 2026-05-21T14:14:16.224702+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/main.pdf",
  "project": "importance_margin_vla_compress",
  "pages": "16-20",
  "dpi": "150",
  "output_dir": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/.claude/sessions/review_reviewer_2_29d69ba3/_pdf_images4"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/main.pdf",
    "project": "importance_margin_vla_compress",
    "pages": "16-20",
    "dpi": "150",
    "output_dir": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/.claude/sessions/review_reviewer_2_29d69ba3/_pdf_images4"
  }
}
```

</details>

---


### Tool result

_source line 297 · 2026-05-21T14:14:16.728115+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 16, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/.claude/sessions/review_reviewer_2_29d69ba3/_pdf_images4/main_p16.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 329.4}, {\"page\": 17, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/.claude/sessions/review_reviewer_2_29d69ba3/_pdf_images4/main_p17.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 194.4}, {\"page\": 18, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/.claude/sessions/review_reviewer_2_29d69ba3/_pdf_images4/main_p18.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 216.5}, {\"page\": 19, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/.claude/sessions/review_reviewer_2_29d69ba3/_pdf_images4/main_p19.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 303.7}, {\"page\": 20, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/.claude/sessions/review_reviewer_2_29d69ba3/_pdf_images4/main_p20.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 313.9}], \"total_pages\": 25, \"rendered_pages\": 5, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/.claude/sessions/review_reviewer_2_29d69ba3/_pdf_images4\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 503
}
```

</details>

---


### Tool call

_source line 298 · 2026-05-21T14:14:17.582330+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/main.pdf",
  "project": "importance_margin_vla_compress",
  "pages": "21-25",
  "dpi": "150",
  "output_dir": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/.claude/sessions/review_reviewer_2_29d69ba3/_pdf_images5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/main.pdf",
    "project": "importance_margin_vla_compress",
    "pages": "21-25",
    "dpi": "150",
    "output_dir": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/.claude/sessions/review_reviewer_2_29d69ba3/_pdf_images5"
  }
}
```

</details>

---


### Tool result

_source line 299 · 2026-05-21T14:14:18.043462+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 21, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/.claude/sessions/review_reviewer_2_29d69ba3/_pdf_images5/main_p21.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 242.2}, {\"page\": 22, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/.claude/sessions/review_reviewer_2_29d69ba3/_pdf_images5/main_p22.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 291.7}, {\"page\": 23, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/.claude/sessions/review_reviewer_2_29d69ba3/_pdf_images5/main_p23.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 266.3}, {\"page\": 24, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/.claude/sessions/review_reviewer_2_29d69ba3/_pdf_images5/main_p24.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 258.6}, {\"page\": 25, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/.claude/sessions/review_reviewer_2_29d69ba3/_pdf_images5/main_p25.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 223.3}], \"total_pages\": 25, \"rendered_pages\": 5, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/.claude/sessions/review_reviewer_2_29d69ba3/_pdf_images5\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 461
}
```

</details>

---


### Tool call

_source line 300 · 2026-05-21T14:14:21.808018+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/.claude/sessions/review_reviewer_2_29d69ba3/_pdf_images3/main_p11.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/.claude/sessions/review_reviewer_2_29d69ba3/_pdf_images3/main_p11.png"
  }
}
```

</details>

---


### Tool result

_source line 301 · 2026-05-21T14:14:22.564161+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 756
}
```

</details>

---


### Tool call

_source line 302 · 2026-05-21T14:14:22.564789+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/.claude/sessions/review_reviewer_2_29d69ba3/_pdf_images3/main_p12.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/.claude/sessions/review_reviewer_2_29d69ba3/_pdf_images3/main_p12.png"
  }
}
```

</details>

---


### Tool result

_source line 303 · 2026-05-21T14:14:23.021804+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 457
}
```

</details>

---


### Tool call

_source line 304 · 2026-05-21T14:14:23.022306+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/.claude/sessions/review_reviewer_2_29d69ba3/_pdf_images3/main_p13.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/.claude/sessions/review_reviewer_2_29d69ba3/_pdf_images3/main_p13.png"
  }
}
```

</details>

---


### Tool result

_source line 305 · 2026-05-21T14:14:23.978210+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 955
}
```

</details>

---


### Tool call

_source line 306 · 2026-05-21T14:14:23.978709+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/.claude/sessions/review_reviewer_2_29d69ba3/_pdf_images3/main_p14.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/.claude/sessions/review_reviewer_2_29d69ba3/_pdf_images3/main_p14.png"
  }
}
```

</details>

---


### Tool result

_source line 307 · 2026-05-21T14:14:24.386581+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 407
}
```

</details>

---


### Tool call

_source line 308 · 2026-05-21T14:14:24.387108+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/.claude/sessions/review_reviewer_2_29d69ba3/_pdf_images3/main_p15.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/.claude/sessions/review_reviewer_2_29d69ba3/_pdf_images3/main_p15.png"
  }
}
```

</details>

---


### Tool result

_source line 309 · 2026-05-21T14:14:24.791416+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 404
}
```

</details>

---


### Tool call

_source line 310 · 2026-05-21T14:14:32.178318+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/.claude/sessions/review_reviewer_2_29d69ba3/_pdf_images4/main_p16.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/.claude/sessions/review_reviewer_2_29d69ba3/_pdf_images4/main_p16.png"
  }
}
```

</details>

---


### Tool result

_source line 311 · 2026-05-21T14:14:32.631776+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 453
}
```

</details>

---


### Tool call

_source line 312 · 2026-05-21T14:14:32.682324+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/.claude/sessions/review_reviewer_2_29d69ba3/_pdf_images4/main_p17.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/.claude/sessions/review_reviewer_2_29d69ba3/_pdf_images4/main_p17.png"
  }
}
```

</details>

---


### Tool result

_source line 313 · 2026-05-21T14:14:33.592411+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 910
}
```

</details>

---


### Tool call

_source line 314 · 2026-05-21T14:14:33.598101+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/.claude/sessions/review_reviewer_2_29d69ba3/_pdf_images4/main_p18.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/.claude/sessions/review_reviewer_2_29d69ba3/_pdf_images4/main_p18.png"
  }
}
```

</details>

---


### Tool call

_source line 315 · 2026-05-21T14:14:34.150585+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/.claude/sessions/review_reviewer_2_29d69ba3/_pdf_images4/main_p19.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/.claude/sessions/review_reviewer_2_29d69ba3/_pdf_images4/main_p19.png"
  }
}
```

</details>

---


### Tool result

_source line 316 · 2026-05-21T14:14:35.005706+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1407
}
```

</details>

---


### Tool result

_source line 317 · 2026-05-21T14:14:35.009059+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 858
}
```

</details>

---


### Tool call

_source line 318 · 2026-05-21T14:14:35.009670+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/.claude/sessions/review_reviewer_2_29d69ba3/_pdf_images4/main_p20.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/.claude/sessions/review_reviewer_2_29d69ba3/_pdf_images4/main_p20.png"
  }
}
```

</details>

---


### Tool call

_source line 319 · 2026-05-21T14:14:35.609704+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/.claude/sessions/review_reviewer_2_29d69ba3/_pdf_images5/main_p21.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/.claude/sessions/review_reviewer_2_29d69ba3/_pdf_images5/main_p21.png"
  }
}
```

</details>

---


### Tool result

_source line 320 · 2026-05-21T14:14:36.428371+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1418
}
```

</details>

---


### Tool result

_source line 321 · 2026-05-21T14:14:36.432303+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 822
}
```

</details>

---


### Tool call

_source line 322 · 2026-05-21T14:14:36.433010+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/.claude/sessions/review_reviewer_2_29d69ba3/_pdf_images5/main_p22.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/.claude/sessions/review_reviewer_2_29d69ba3/_pdf_images5/main_p22.png"
  }
}
```

</details>

---


### Tool result

_source line 323 · 2026-05-21T14:14:36.886434+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 453
}
```

</details>

---


### Tool call

_source line 324 · 2026-05-21T14:14:36.886775+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/.claude/sessions/review_reviewer_2_29d69ba3/_pdf_images5/main_p23.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/.claude/sessions/review_reviewer_2_29d69ba3/_pdf_images5/main_p23.png"
  }
}
```

</details>

---


### Tool result

_source line 325 · 2026-05-21T14:14:37.842553+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 955
}
```

</details>

---


### Tool call

_source line 326 · 2026-05-21T14:14:37.843059+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/.claude/sessions/review_reviewer_2_29d69ba3/_pdf_images5/main_p24.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/.claude/sessions/review_reviewer_2_29d69ba3/_pdf_images5/main_p24.png"
  }
}
```

</details>

---


### Tool result

_source line 327 · 2026-05-21T14:14:38.248681+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 405
}
```

</details>

---


### Tool call

_source line 328 · 2026-05-21T14:14:38.249047+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/.claude/sessions/review_reviewer_2_29d69ba3/_pdf_images5/main_p25.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/.claude/sessions/review_reviewer_2_29d69ba3/_pdf_images5/main_p25.png"
  }
}
```

</details>

---


### Tool result

_source line 329 · 2026-05-21T14:14:38.602851+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 353
}
```

</details>

---


### Tool call

_source line 330 · 2026-05-21T14:15:32.603807+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://www.corl2023.org/reviewer-guidelines",
  "prompt": "Extract the complete review form criteria, all scoring dimensions with their rating scales, and any specific guidance on what reviewers should evaluate. Include all numerical scales and dimension descriptions."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://www.corl2023.org/reviewer-guidelines",
    "prompt": "Extract the complete review form criteria, all scoring dimensions with their rating scales, and any specific guidance on what reviewers should evaluate. Include all numerical scales and dimension descriptions."
  }
}
```

</details>

---


### Tool call

_source line 331 · 2026-05-21T14:15:32.705545+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "CoRL 2026 reviewer form scoring dimensions rating scale criteria"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "CoRL 2026 reviewer form scoring dimensions rating scale criteria"
  }
}
```

</details>

---


### Tool result

_source line 332 · 2026-05-21T14:15:37.514925+00:00_

Web search results for query: "CoRL 2026 reviewer form scoring dimensions rating scale criteria"

Links: [{"title":"📈 ICLR 2026 Submission Storm: 19,797 Papers, New Review Rules, and the Age of AI Convergence | CSPaper Forum","url":"https://forum.cspaper.org/topic/169/iclr-2026-submission-storm-19-797-papers-new-review-rules-and-the-age-of-ai-convergence"},{"title":"CoRL 2026 - Instruction for Authors","url":"https://www.corl.org/contributions/instruction-for-authors"},{"title":"Rating Scale Question | SurveyMonkey","url":"https://help.surveymonkey.com/en/apply/build/rating-scale-question/"},{"title":"Reviewer Guidelines — CoRL 2023","url":"https://www.corl2023.org/reviewer-guidelines"},{"title":"Grant Peer Review: Improving Inter-Rater Reliability with Training","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4468126/"},{"title":"Which Coauthor Should I Nominate in My 99 ICLR Submissions? A Mathematical Analysis of the ICLR 2026 Reciprocal Reviewer Nomination Policy","url":"https://arxiv.org/pdf/2512.17950"},{"title":"ICLR 2026 Reviewer Guide","url":"https://iclr.cc/Conferences/2026/ReviewerGuide"}]

Based on the search results, I found limited specific information about CoRL 2026's reviewer form scoring dimensions and rating scale criteria. The search results included information about CoRL 2026 author instructions and general reviewing guidelines, but did not contain detailed information about the specific scoring dimensions or rating scale used for CoRL 2026 reviews.

Papers that receive all reviews in the "reject" range in the initial round will not proceed to the rebuttal phase, indicating there is a "reject" range in their scoring system, but the exact rating scale dimensions and specific criteria are not detailed in these search results.

For more specific information about CoRL 2026's reviewer form scoring dimensions and rating scale criteria, you would likely need to:
- Visit the official CoRL 2026 website (corl.org)
- Check the reviewer guidelines or 
…[truncated 273 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 4809
}
```

</details>

---


### Tool result

_source line 333 · 2026-05-21T14:15:41.201944+00:00_

# CoRL 2023 Review Form Criteria

Based on the provided guidelines, CoRL 2023 reviewers evaluate papers across **six key dimensions**:

## Evaluation Dimensions

1. **Originality**: "Are the problems or methods new?" Assess whether work represents novel contributions or valuable combinations of existing techniques, with clear differentiation from prior work.

2. **Quality**: Reviewers examine technical soundness, whether claims are supported by theory or experiments, appropriateness of methods, and completeness of the work.

3. **Clarity**: Assessment of writing quality, organization, informativeness, and whether sufficient detail allows expert reproduction of results.

4. **Significance**: Evaluate importance of results and potential impact on the research or practitioner communities.

5. **Relevance**: Determine if the paper addresses robot learning problems using learning-based methods, and whether the CoRL audience would find it interesting.

6. **Limitations**: Papers must include a limitations section. Honestly reported limitations should be treated favorably, while unreported flaws should be "strongly reflected in your scores."

## Scoring Guidance

The document does not explicitly specify numerical rating scales or a formal scoring rubric. Instead, it emphasizes that reviews should be "constructive and concrete" with evidence-based feedback, starting with positive aspects and suggesting improvements.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 8598
}
```

</details>

---


### Tool call

_source line 334 · 2026-05-21T14:17:45.118465+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://www.corl.org/contributions/call-for-papers",
  "prompt": "Extract all submission requirements including page limits, formatting rules, supplementary material rules, and any evaluation criteria mentioned for CoRL 2026."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://www.corl.org/contributions/call-for-papers",
    "prompt": "Extract all submission requirements including page limits, formatting rules, supplementary material rules, and any evaluation criteria mentioned for CoRL 2026."
  }
}
```

</details>

---


### Tool result

_source line 335 · 2026-05-21T14:17:48.885227+00:00_

# CoRL 2026 Submission Requirements

Based on the provided content, the following submission requirements are specified:

## Core Requirements

**Robotics Focus**: "Submissions should focus on a core robotics problem and demonstrate the relevance of proposed models, algorithms, datasets, and benchmarks to robotics."

**Limitations Section**: All submissions must include documentation that "explicitly describing limiting assumptions, failure modes, and other limitations of the results and experiments and how these might be addressed in the future."

**Experimental Evidence**: Authors should "report real-robot experiments or provide convincing evidence that simulation experiments are transferable to real robots."

## Supplementary Materials

The conference encourages—but does not mandate—submission of "video, code and data as supplementary materials."

## Missing Details

The provided webpage excerpt does not include specific information about:
- Page limits or word counts
- Detailed formatting rules (font, spacing, margins, etc.)
- File format specifications
- Evaluation criteria or review standards

**For complete submission requirements**, the page directs authors to consult the [Instruction for Authors](/contributions/instruction-for-authors) section, which likely contains the detailed technical specifications not present in this overview.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 3766
}
```

</details>

---


### Tool call

_source line 336 · 2026-05-21T14:19:27.472816+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "\n# Reviewer 2 审稿意见：Novelty, Positioning, and Venue Fit\n\n## 1. Summary\n\n本文对 7 个 VLA 模型（450M–7B 参数）在 LIBERO 基准上的视觉 token pruning 进行了跨架构实证研究，发现 vision connector 类型（pixel-shuffle / MLP projector / linear projection）是决定 pruning 容忍度的关键因素。作者提出四类 compressibility taxonomy，用 token importance 的变异系数 (CV) 作为\"零成本\"预测指标，并提出 Vision Token Re-encoder (VTR) 在 SmolVLA 上实现 75% 压缩下 60.1% 成功率。论文实验设计系统、附录详尽，但核心因果声明证据不足，taxonomy 建立在 N=3 connector 类型上，且纯仿真评估与 CoRL venue 期望存在明显差距。\n\n## 2. Strengths\n\n**S1. 系统全面的实证研究。** 覆盖 7 个 VLA 模型、3 个 connector 家族、3 种 pruning 策略（random / importance-based / L2 norm-based）、多个 pruning ratio，每个配置 500 episodes closed-loop 评估。这种广度在 VLA efficiency 文献中少见。（Table 1, Table 2, Appendix B-E）\n\n**S2. 实用的诊断指标。** CV 可从单次 forward pass 计算、无需 closed-loop 评估即可预测 pruning 行为。Table 3 和 Figure 3b 展示了 CV 与降解模式的单调对应关系，对实际部署有指导价值。\n\n**S3. 重要的负面结果。** Linear projection 模型（π₀, π₀.5）即使 10% token removal 也导致崩溃（Table 1: π₀.5 从 baseline 44.8% 降至 r=0.9 时 ≤5%），这对社区避免无效尝试有直接价值。（Section 4.4, Table 8）\n\n**S4. 诚实的方法论处理。** 论文明确标注 CogACT 74.2% SR 来自 EfficientVLA 第三方结果而非自有评估（Section 4.1 脚注），π₀ 仅有 offline 评估也有说明。Appendix 提供了完整的 per-task breakdown（Tables 5-14）和训练超参数（Table 17）。\n\n**S5. 写作清晰，结构合理。** Related Work 覆盖了 ViT token pruning、VLM token reduction、VLA-specific works 三个层面，区分度清楚。Section 5 的 Analysis 将 empirical observations 提升到 mechanistic interpretation。\n\n## 3. Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**N1 [critical] 核心因果声明证据不充分——connector type 与多个架构变量混淆。**\n\n论文标题声明 \"Vision Connectors and VLA Token Compressibility\"，正文多处使用因果语言：\n- Section 1: \"The vision connector, not model size or action head, determines pruning behavior\"\n- Section 5.1: \"strongly implicates the connector as the primary factor\"\n\n但实际上，三个 connector 家族的模型在 vision encoder（SigLIP vs DINOv2）、LLM backbone（Qwen2-0.5B vs Llama-2-7B）、action head（flow matching vs autoregressive vs diffusion）、训练数据和训练流程上同时不同。具体地：\n- π₀/π₀.5（linear projection）= SigLIP + flow matching\n- OpenVLA（MLP）= DINOv2 + autoregressive tokens\n- SmolVLA（pixel-shuffle）= SigLIP + Qwen2-0.5B\n\nSection 5.1 的 within-connector 比较（OpenVLA vs OFT vs CogACT vs X-VLA，均为 MLP）支持 connector 在**同一家族内**是一致因素，但无法跨家族隔离 connector 的因果效应。论文需要一个 controlled connector-swap 实验（例如在同一 backbone 上替换 connector 类型）才能支撑 \"determines\" 级别的因果声明。\n\n**为什么影响接收：** 这是论文的核心 contribution，如果从\"因果\"降级为\"相关\"，novelty 大幅降低。\n\n**N2 [critical] 四类 taxonomy 和 CV-as-predictor 实质上建立在 N=3 个数据点上。**\n\nTaxonomy 包含 4 个类别（uniformly critical / threshold-graded / smooth graded / catastrophic cliff），但只覆盖 3 种 connector 类型。Figure 3b 中 CV 与降解的\"单调关系\"本质上是 3 个簇（linear projection CV≈0.04-0.06，MLP CV≈0.15-0.22，pixel-shuffle CV≈0.55）。从 3 个点声称 predictive power 统计上很弱。\n\n此外，taxonomy 边界定义不严格。\"threshold-graded\"（OpenVLA）和\"smooth graded\"（X-VLA/OFT）的区别依赖于具体 pruning ratio 下的表现差异——Table 1 中 OpenVLA 在 r=0.5 importance-based 得 69.8%，X-VLA 得 60.4%——但没有给出区分两个类别的形式化标准。\n\n**关键缺失：** Perceiver/Q-Former 类 connector 在 related work 中被讨论（Section 2, citing Jaegle 2021, Li 2023 BLIP-2），但未被纳入实证研究。Octo 使用类似 cross-attention 机制，如果包含会增加一个 connector 家族并极大增强 taxonomy 的说服力。\n\n**为什么影响接收：** Contribution C1（taxonomy）是论文的首要 novelty 声明。N=3 connector 类型不足以支撑一个\"generalizable framework\"的定位。\n\n**N3 [critical] 纯仿真评估与 CoRL venue 要求冲突。**\n\nCoRL 2026 Call for Papers 明确要求：\"Authors should report real-robot experiments or provide convincing evidence that simulation experiments are transferable to real robots.\" 本文全部实验在 LIBERO simulation 上进行（16 tasks, 500 episodes each），没有任何 real-robot validation，也没有提供 sim-to-real transferability 的证据。\n\n论文的实际应用场景是 \"onboard inference\" 和 \"real-time control\"（Section 1, Section 6），但从未在真实系统上演示。Section 5.4 讨论了 offline vs closed-loop 的差距，但没有将 simulation-only 本身作为 limitation 明确讨论。\n\n**为什么影响接收：** 在 CoRL 这是一个显著负面因素。纯仿真的 empirical analysis 论文需要更强的分析贡献或更广泛的仿真覆盖来弥补。\n\n### Should-Fix（影响评分但不一票否决）\n\n**W1 [warning] \"Falsifies the 'immune' assumption\" 是稻草人论证。**\n\nSection 4.4 和 Introduction 声称 \"falsifies the 'immune' interpretation suggested by π₀.5's offline-only evaluation\"。但 π₀ 和 π₀.5 的原始论文从未声称对 token pruning 免疫。这个\"immune\"假设是作者自己从 offline metrics 推导出来的，然后自己推翻。应改为 \"our offline metrics would misleadingly suggest tolerance, but closed-loop evaluation reveals collapse\" 或引用具体文献中的 immunity claim。\n\n**W2 [warning] VTR 的新颖性有限——本质上是 Perceiver/Q-Former 应用于 VLA token 压缩。**\n\nVTR（Section 3.3）是一个 cross-attention pooling module（128 visual tokens → M=16 query vectors），与 Perceiver 的 cross-attention 机制和 BLIP-2 的 Q-Former 功能等价。论文在 Related Work 中引用了两者，但未充分讨论 VTR 的差异化。\n\n实验结果：VTR 在 75% 压缩下达到 60.1% SR vs baseline 59.2%（Table 2）。差距为 +0.9 个百分点，考虑到 Wilcox 95% CI 的宽度（appendix 中报告的置信区间），这个提升可能不具统计显著性。VTR 的主要价值是证明 re-encoding 可以恢复 pixel-shuffle 的 catastrophic cliff，但这个结果并不令人意外——hard deletion 破坏空间结构，learned compression 保留它。\n\n**W3 [warning] \"七个模型\"的 framing 有夸大成分。**\n\nContribution C1 声称 \"evaluating seven models\"。但实际 closed-loop evaluation 的覆盖度：\n- π₀：仅 offline evaluation（Section 4.4, \"π₀'s offline evaluation\"）\n- CogACT：核心结果 74.2% 来自 EfficientVLA，非自有评估\n- OFT：部分指标（entropy/CV）有评估，closed-loop 也有但可能不完整\n\n严格来说，具有完整自有 closed-loop evaluation 的模型约 4-5 个（SmolVLA, OpenVLA, X-VLA, π₀.5, OFT）。建议在 Contribution 表述中明确区分自有评估和引用结果。\n\n**W4 [warning] \"Diagnose-then-Compress framework\" 过度包装。**\n\nContribution C3 将贡献包装为 \"framework\"，但实际内容是：(1) 计算 CV，(2) 查表确定 compressibility class，(3) 选择 pruning 策略（importance-based 或 random）。这是一个基于单一指标的 lookup table，不是一个 framework。标签化为 \"practical guidelines\" 或 \"diagnostic protocol\" 更准确。\n\n**W5 [warning] 正文可能超页。**\n\n主体内容（Section 1 至 Conclusion）看起来跨越约 13 页，超过 CoRL 8 页限制。如果是提交前的草稿状态，需要将 Section 5（Analysis and Discussion）的相当部分移入 appendix。\n\n### Minor（不影响接收）\n\n**M1.** Abstract 信息密度过高，包含大量具体数字（CV = 0.04, 36-percentage-point gap, 60.1% SR 等），建议精简至核心 finding，数字留给正文。\n\n**M2.** 标题中 \"Crashes\" 略显 sensationalized。对 MLP 类模型降解是 smooth 的，不是 crash。\"Fails\" 或 \"Degrades\" 更精确。\n\n**M3.** Table 1 混合了自有结果和 EfficientVLA 的 CogACT 结果，建议在表格内用 † 等标记区分。\n\n**M4.** 因果语言强度需全文校准。\"determines\"、\"primarily shaped by\"、\"strongly linked to\" 在 N=3 connector 类型的相关性证据下偏强。\n\n**M5.** Figure 3 的 (a) token pruning across architectures 和 (b) CV strategy interaction 信息量大，但 x 轴标签较小，可读性可改善。\n\n## 4. Questions for Authors\n\n**Q1.** 是否考虑过 controlled connector-swap 实验（例如在 Qwen2-0.5B backbone 上分别接 pixel-shuffle、MLP、linear projection）来隔离 connector 的因果效应？\n\n**Q2.** Taxonomy 有 4 个类别但只有 3 个 connector 类型。Perceiver-based VLA（如 Octo 的 cross-attention）会落入哪个类别？taxonomy 是否可扩展？\n\n**Q3.** VTR 的 M（query vector 数量）取 16 和 128 两个值。是否探索过中间值？M vs SR 的 Pareto frontier 是什么样的？\n\n**Q4.** CV-compressibility 关系是否在 LIBERO 以外的 benchmark 上验证过？即使是另一个仿真环境（如 MetaWorld）的初步结果也会大幅增强 generalizability 声明。\n\n**Q5.** Section 4.4 中 π₀ 的 offline evaluation 显示 minimal action-loss degradation，但你们预期 closed-loop 会崩溃。是否有定量证据（例如 error 与 pruned spatial regions 的相关性）支持 error compounding 解释，而非仅靠 offline-vs-closed-loop 的差距本身？\n\n**Q6.** VTR 60.1% vs baseline 59.2% 的差异在统计上显著吗？Table 2 的 Wilcox 95% CI 是什么？\n\n## 5. Missing References\n\n- 没有明确遗漏的重要引用。Related work 对 ViT pruning、VLM token reduction、VLA efficiency 的覆盖基本充分。\n- 建议：如果 Octo [Ghosh et al., 2024]（已引用但未评估）的 cross-attention connector 可被纳入实验，将显著增强 taxonomy 的覆盖度。\n- 引用验证结果：41 篇引用中 30 篇 verified，5 篇 not_found（主要是 π₀/π₀.5/DINOv2/LightVLA/Don't Run with Scissors——均为近期 arXiv 预印本，OpenAlex 尚未收录），6 篇 minor mismatch（first_author 字段差异，非实质错误）。无虚假引用。\n\n## 6. Overall Score and Confidence\n\n### 官方维度打分（基于 CoRL review dimensions）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Originality | 2/5 | 核心 finding（connector→compressibility）可从已知 connector 属性部分推导；taxonomy 基于 N=3 类型；VTR 是已知方法的直接应用 |\n| Quality | 3.5/5 | 实验方法论扎实（多模型、多策略、closed-loop、500 episodes），但因果声明 under-identified，taxonomy 样本量不足 |\n| Clarity | 4/5 | 写作清晰、结构好、图表信息量大，但 abstract 过密，部分因果语言偏强 |\n| Significance | 2.5/5 | 对 VLA 部署社区有实用价值（特别是 negative results），但 simulation-only + N=3 限制了 impact |\n| Relevance | 3/5 | 话题高度相关（VLA efficiency for robotics），但缺乏 real-robot experiments，与 CoRL \"demonstrate relevance to robotics\" 要求有差距 |\n| Limitations | 3/5 | 讨论了 offline vs closed-loop gap，但未将 simulation-only 和 N=3 connector types 作为主要 limitations 明确讨论 |\n\n### Overall Score: **Weak Reject** (borderline)\n### Confidence: **High**\n\n**核心判断：** 论文解决了一个实际且及时的问题（不同 VLA 架构对 token pruning 的不同反应），实验执行扎实。但三个结构性问题制约了 novelty：(1) 因果声明缺乏 controlled experiment 支撑；(2) taxonomy 仅基于 3 个 connector 类型；(3) CoRL 要求的 real-robot evidence 完全缺失。如果作者在 rebuttal 中能提供 connector-swap 实验结果或 real-robot 初步验证，评分可能上调至 borderline accept。\n",
  "reviewer_id": "2",
  "project": "importance_margin_vla_compress"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "\n# Reviewer 2 审稿意见：Novelty, Positioning, and Venue Fit\n\n## 1. Summary\n\n本文对 7 个 VLA 模型（450M–7B 参数）在 LIBERO 基准上的视觉 token pruning 进行了跨架构实证研究，发现 vision connector 类型（pixel-shuffle / MLP projector / linear projection）是决定 pruning 容忍度的关键因素。作者提出四类 compressibility taxonomy，用 token importance 的变异系数 (CV) 作为\"零成本\"预测指标，并提出 Vision Token Re-encoder (VTR) 在 SmolVLA 上实现 75% 压缩下 60.1% 成功率。论文实验设计系统、附录详尽，但核心因果声明证据不足，taxonomy 建立在 N=3 connector 类型上，且纯仿真评估与 CoRL venue 期望存在明显差距。\n\n## 2. Strengths\n\n**S1. 系统全面的实证研究。** 覆盖 7 个 VLA 模型、3 个 connector 家族、3 种 pruning 策略（random / importance-based / L2 norm-based）、多个 pruning ratio，每个配置 500 episodes closed-loop 评估。这种广度在 VLA efficiency 文献中少见。（Table 1, Table 2, Appendix B-E）\n\n**S2. 实用的诊断指标。** CV 可从单次 forward pass 计算、无需 closed-loop 评估即可预测 pruning 行为。Table 3 和 Figure 3b 展示了 CV 与降解模式的单调对应关系，对实际部署有指导价值。\n\n**S3. 重要的负面结果。** Linear projection 模型（π₀, π₀.5）即使 10% token removal 也导致崩溃（Table 1: π₀.5 从 baseline 44.8% 降至 r=0.9 时 ≤5%），这对社区避免无效尝试有直接价值。（Section 4.4, Table 8）\n\n**S4. 诚实的方法论处理。** 论文明确标注 CogACT 74.2% SR 来自 EfficientVLA 第三方结果而非自有评估（Section 4.1 脚注），π₀ 仅有 offline 评估也有说明。Appendix 提供了完整的 per-task breakdown（Tables 5-14）和训练超参数（Table 17）。\n\n**S5. 写作清晰，结构合理。** Related Work 覆盖了 ViT token pruning、VLM token reduction、VLA-specific works 三个层面，区分度清楚。Section 5 的 Analysis 将 empirical observations 提升到 mechanistic interpretation。\n\n## 3. Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**N1 [critical] 核心因果声明证据不充分——connector type 与多个架构变量混淆。**\n\n论文标题声明 \"Vision Connectors and VLA Token Compressibility\"，正文多处使用因果语言：\n- Section 1: \"The vision connector, not model size or action head, determines pruning behavior\"\n- Section 5.1: \"strongly implicates the connector as the primary factor\"\n\n但实际上，三个 connector 家族的模型在 vision encoder（SigLIP vs DINOv2）、LLM backbone（Qwen2-0.5B vs Llama-2-7B）、action head（flow matching vs autoregressive vs diffusion）、训练数据和训练流程上同时不同。具体地：\n- π₀/π₀.5（linear projection）= SigLIP + flow matching\n- OpenVLA（MLP）= DINOv2 + autoregressive tokens\n- SmolVLA（pixel-shuffle）= SigLIP + Qwen2-0.5B\n\nSection 5.1 的 within-connector 比较（OpenVLA vs OFT vs CogACT vs X-VLA，均为 MLP）支持 connector 在**同一家族内**是一致因素，但无法跨家族隔离 connector 的因果效应。论文需要一个 controlled connector-swap 实验（例如在同一 backbone 上替换 connector 类型）才能支撑 \"determines\" 级别的因果声明。\n\n**为什么影响接收：** 这是论文的核心 contribution，如果从\"因果\"降级为\"相关\"，novelty 大幅降低。\n\n**N2 [critical] 四类 taxonomy 和 CV-as-predictor 实质上建立在 N=3 个数据点上。**\n\nTaxonomy 包含 4 个类别（uniformly critical / threshold-graded / smooth graded / catastrophic cliff），但只覆盖 3 种 connector 类型。Figure 3b 中 CV 与降解的\"单调关系\"本质上是 3 个簇（linear projection CV≈0.04-0.06，MLP CV≈0.15-0.22，pixel-shuffle CV≈0.55）。从 3 个点声称 predictive power 统计上很弱。\n\n此外，taxonomy 边界定义不严格。\"threshold-graded\"（OpenVLA）和\"smooth graded\"（X-VLA/OFT）的区别依赖于具体 pruning ratio 下的表现差异——Table 1 中 OpenVLA 在 r=0.5 importance-based 得 69.8%，X-VLA 得 60.4%——但没有给出区分两个类别的形式化标准。\n\n**关键缺失：** Perceiver/Q-Former 类 connector 在 related work 中被讨论（Section 2, citing Jaegle 2021, Li 2023 BLIP-2），但未被纳入实证研究。Octo 使用类似 cross-attention 机制，如果包含会增加一个 connector 家族并极大增强 taxonomy 的说服力。\n\n**为什么影响接收：** Contribution C1（taxonomy）是论文的首要 novelty 声明。N=3 connector 类型不足以支撑一个\"generalizable framework\"的定位。\n\n**N3 [critical] 纯仿真评估与 CoRL venue 要求冲突。**\n\nCoRL 2026 Call for Papers 明确要求：\"Authors should report real-robot experiments or provide convincing evidence that simulation experiments are transferable to real robots.\" 本文全部实验在 LIBERO simulation 上进行（16 tasks, 500 episodes each），没有任何 real-robot validation，也没有提供 sim-to-real transferability 的证据。\n\n论文的实际应用场景是 \"onboard inference\" 和 \"real-time control\"（Section 1, Section 6），但从未在真实系统上演示。Section 5.4 讨论了 offline vs closed-loop 的差距，但没有将 simulation-only 本身作为 limitation 明确讨论。\n\n**为什么影响接收：** 在 CoRL 这是一个显著负面因素。纯仿真的 empirical analysis 论文需要更强的分析贡献或更广泛的仿真覆盖来弥补。\n\n### Should-Fix（影响评分但不一票否决）\n\n**W1 [warning] \"Falsifies the 'immune' assumption\" 是稻草人论证。**\n\nSection 4.4 和 Introduction 声称 \"falsifies the 'immune' interpretation suggested by π₀.5's offline-only evaluation\"。但 π₀ 和 π₀.5 的原始论文从未声称对 token pruning 免疫。这个\"immune\"假设是作者自己从 offline metrics 推导出来的，然后自己推翻。应改为 \"our offline metrics would misleadingly suggest tolerance, but closed-loop evaluation reveals collapse\" 或引用具体文献中的 immunity claim。\n\n**W2 [warning] VTR 的新颖性有限——本质上是 Perceiver/Q-Former 应用于 VLA token 压缩。**\n\nVTR（Section 3.3）是一个 cross-attention pooling module（128 visual tokens → M=16 query vectors），与 Perceiver 的 cross-attention 机制和 BLIP-2 的 Q-Former 功能等价。论文在 Related Work 中引用了两者，但未充分讨论 VTR 的差异化。\n\n实验结果：VTR 在 75% 压缩下达到 60.1% SR vs baseline 59.2%（Table 2）。差距为 +0.9 个百分点，考虑到 Wilcox 95% CI 的宽度（appendix 中报告的置信区间），这个提升可能不具统计显著性。VTR 的主要价值是证明 re-encoding 可以恢复 pixel-shuffle 的 catastrophic cliff，但这个结果并不令人意外——hard deletion 破坏空间结构，learned compression 保留它。\n\n**W3 [warning] \"七个模型\"的 framing 有夸大成分。**\n\nContribution C1 声称 \"evaluating seven models\"。但实际 closed-loop evaluation 的覆盖度：\n- π₀：仅 offline evaluation（Section 4.4, \"π₀'s offline evaluation\"）\n- CogACT：核心结果 74.2% 来自 EfficientVLA，非自有评估\n- OFT：部分指标（entropy/CV）有评估，closed-loop 也有但可能不完整\n\n严格来说，具有完整自有 closed-loop evaluation 的模型约 4-5 个（SmolVLA, OpenVLA, X-VLA, π₀.5, OFT）。建议在 Contribution 表述中明确区分自有评估和引用结果。\n\n**W4 [warning] \"Diagnose-then-Compress framework\" 过度包装。**\n\nContribution C3 将贡献包装为 \"framework\"，但实际内容是：(1) 计算 CV，(2) 查表确定 compressibility class，(3) 选择 pruning 策略（importance-based 或 random）。这是一个基于单一指标的 lookup table，不是一个 framework。标签化为 \"practical guidelines\" 或 \"diagnostic protocol\" 更准确。\n\n**W5 [warning] 正文可能超页。**\n\n主体内容（Section 1 至 Conclusion）看起来跨越约 13 页，超过 CoRL 8 页限制。如果是提交前的草稿状态，需要将 Section 5（Analysis and Discussion）的相当部分移入 appendix。\n\n### Minor（不影响接收）\n\n**M1.** Abstract 信息密度过高，包含大量具体数字（CV = 0.04, 36-percentage-point gap, 60.1% SR 等），建议精简至核心 finding，数字留给正文。\n\n**M2.** 标题中 \"Crashes\" 略显 sensationalized。对 MLP 类模型降解是 smooth 的，不是 crash。\"Fails\" 或 \"Degrades\" 更精确。\n\n**M3.** Table 1 混合了自有结果和 EfficientVLA 的 CogACT 结果，建议在表格内用 † 等标记区分。\n\n**M4.** 因果语言强度需全文校准。\"determines\"、\"primarily shaped by\"、\"strongly linked to\" 在 N=3 connector 类型的相关性证据下偏强。\n\n**M5.** Figure 3 的 (a) token pruning across architectures 和 (b) CV strategy interaction 信息量大，但 x 轴标签较小，可读性可改善。\n\n## 4. Questions for Authors\n\n**Q1.** 是否考虑过 controlled connector-swap 实验（例如在 Qwen2-0.5B backbone 上分别接 pixel-shuffle、MLP、linear projection）来隔离 connector 的因果效应？\n\n**Q2.** Taxonomy 有 4 个类别但只有 3 个 connector 类型。Perceiver-based VLA（如 Octo 的 cross-attention）会落入哪个类别？taxonomy 是否可扩展？\n\n**Q3.** VTR 的 M（query vector 数量）取 16 和 128 两个值。是否探索过中间值？M vs SR 的 Pareto frontier 是什么样的？\n\n**Q4.** CV-compressibility 关系是否在 LIBERO 以外的 benchmark 上验证过？即使是另一个仿真环境（如 MetaWorld）的初步结果也会大幅增强 generalizability 声明。\n\n**Q5.** Section 4.4 中 π₀ 的 offline evaluation 显示 minimal action-loss degradation，但你们预期 closed-loop 会崩溃。是否有定量证据（例如 error 与 pruned spatial regions 的相关性）支持 error compounding 解释，而非仅靠 offline-vs-closed-loop 的差距本身？\n\n**Q6.** VTR 60.1% vs baseline 59.2% 的差异在统计上显著吗？Table 2 的 Wilcox 95% CI 是什么？\n\n## 5. Missing References\n\n- 没有明确遗漏的重要引用。Related work 对 ViT pruning、VLM token reduction、VLA efficiency 的覆盖基本充分。\n- 建议：如果 Octo [Ghosh et al., 2024]（已引用但未评估）的 cross-attention connector 可被纳入实验，将显著增强 taxonomy 的覆盖度。\n- 引用验证结果：41 篇引用中 30 篇 verified，5 篇 not_found（主要是 π₀/π₀.5/DINOv2/LightVLA/Don't Run with Scissors——均为近期 arXiv 预印本，OpenAlex 尚未收录），6 篇 minor mismatch（first_author 字段差异，非实质错误）。无虚假引用。\n\n## 6. Overall Score and Confidence\n\n### 官方维度打分（基于 CoRL review dimensions）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Originality | 2/5 | 核心 finding（connector→compressibility）可从已知 connector 属性部分推导；taxonomy 基于 N=3 类型；VTR 是已知方法的直接应用 |\n| Quality | 3.5/5 | 实验方法论扎实（多模型、多策略、closed-loop、500 episodes），但因果声明 under-identified，taxonomy 样本量不足 |\n| Clarity | 4/5 | 写作清晰、结构好、图表信息量大，但 abstract 过密，部分因果语言偏强 |\n| Significance | 2.5/5 | 对 VLA 部署社区有实用价值（特别是 negative results），但 simulation-only + N=3 限制了 impact |\n| Relevance | 3/5 | 话题高度相关（VLA efficiency for robotics），但缺乏 real-robot experiments，与 CoRL \"demonstrate relevance to robotics\" 要求有差距 |\n| Limitations | 3/5 | 讨论了 offline vs closed-loop gap，但未将 simulation-only 和 N=3 connector types 作为主要 limitations 明确讨论 |\n\n### Overall Score: **Weak Reject** (borderline)\n### Confidence: **High**\n\n**核心判断：** 论文解决了一个实际且及时的问题（不同 VLA 架构对 token pruning 的不同反应），实验执行扎实。但三个结构性问题制约了 novelty：(1) 因果声明缺乏 controlled experiment 支撑；(2) taxonomy 仅基于 3 个 connector 类型；(3) CoRL 要求的 real-robot evidence 完全缺失。如果作者在 rebuttal 中能提供 connector-swap 实验结果或 real-robot 初步验证，评分可能上调至 borderline accept。\n",
    "reviewer_id": "2",
    "project": "importance_margin_vla_compress"
  }
}
```

</details>

---


### Tool result

_source line 337 · 2026-05-21T14:19:31.644042+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4171
}
```

</details>

---


### Tool call

_source line 338 · 2026-05-21T14:19:37.311307+00:00_

called mcp__agent-ml-research__cleanup_pdf_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__cleanup_pdf_images</summary>

```json
{
  "output_dir": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/.claude/sessions/review_reviewer_2_29d69ba3/_pdf_images"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "tool_args": {
    "output_dir": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/.claude/sessions/review_reviewer_2_29d69ba3/_pdf_images"
  }
}
```

</details>

---


### Tool result

_source line 339 · 2026-05-21T14:19:38.266618+00:00_

{"result":"{\"success\": true, \"data\": {\"deleted\": 5, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/.claude/sessions/review_reviewer_2_29d69ba3/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "elapsed_ms": 955
}
```

</details>

---


### Tool call

_source line 340 · 2026-05-21T14:19:38.317291+00:00_

called mcp__agent-ml-research__cleanup_pdf_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__cleanup_pdf_images</summary>

```json
{
  "output_dir": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/.claude/sessions/review_reviewer_2_29d69ba3/_pdf_images2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "tool_args": {
    "output_dir": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/.claude/sessions/review_reviewer_2_29d69ba3/_pdf_images2"
  }
}
```

</details>

---


### Tool result

_source line 341 · 2026-05-21T14:19:38.719227+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"安全限制：只能清理 _pdf_images 目录，当前目标: _pdf_images2\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "elapsed_ms": 401
}
```

</details>

---


### Tool call

_source line 342 · 2026-05-21T14:19:38.719585+00:00_

called mcp__agent-ml-research__cleanup_pdf_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__cleanup_pdf_images</summary>

```json
{
  "output_dir": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/.claude/sessions/review_reviewer_2_29d69ba3/_pdf_images3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "tool_args": {
    "output_dir": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/.claude/sessions/review_reviewer_2_29d69ba3/_pdf_images3"
  }
}
```

</details>

---


### Tool result

_source line 343 · 2026-05-21T14:19:39.724326+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"安全限制：只能清理 _pdf_images 目录，当前目标: _pdf_images3\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "elapsed_ms": 1004
}
```

</details>

---


### Tool call

_source line 344 · 2026-05-21T14:19:39.724795+00:00_

called mcp__agent-ml-research__cleanup_pdf_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__cleanup_pdf_images</summary>

```json
{
  "output_dir": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/.claude/sessions/review_reviewer_2_29d69ba3/_pdf_images4"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "tool_args": {
    "output_dir": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/.claude/sessions/review_reviewer_2_29d69ba3/_pdf_images4"
  }
}
```

</details>

---


### Tool result

_source line 345 · 2026-05-21T14:19:40.176842+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"安全限制：只能清理 _pdf_images 目录，当前目标: _pdf_images4\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 346 · 2026-05-21T14:19:40.177317+00:00_

called mcp__agent-ml-research__cleanup_pdf_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__cleanup_pdf_images</summary>

```json
{
  "output_dir": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/.claude/sessions/review_reviewer_2_29d69ba3/_pdf_images5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "tool_args": {
    "output_dir": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/.claude/sessions/review_reviewer_2_29d69ba3/_pdf_images5"
  }
}
```

</details>

---


### Tool result

_source line 347 · 2026-05-21T14:19:40.278303+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"安全限制：只能清理 _pdf_images 目录，当前目标: _pdf_images5\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "elapsed_ms": 100
}
```

</details>

---


### Assistant

_source line 348 · 2026-05-21T14:19:51.879245+00:00_

审稿意见已提交给 Review Director。

**审稿结论：Weak Reject (borderline)，Confidence: High**

三个核心问题：

1. **因果声明 under-identified**（N1）：connector type 与 encoder/backbone/action head 等多个变量混淆，缺乏 controlled connector-swap 实验，"determines" 级因果语言证据不足
2. **Taxonomy 样本量不足**（N2）：四类分类体系仅基于 3 种 connector 类型（pixel-shuffle / MLP / linear projection），Perceiver/Q-Former 类完全缺失，3 个数据点不足以支撑 "generalizable framework"
3. **CoRL venue fit 差距**（N3）：纯 LIBERO 仿真评估，CoRL 2026 明确要求 "report real-robot experiments or provide convincing evidence that simulation experiments are transferable"

次要问题包括 VTR 新颖性有限（W2, 本质是 Perceiver/Q-Former 的直接应用）、"immune" assumption 是稻草人论证（W1）、"七个模型" framing 有夸大（W3）、正文可能超页（W5）。

如果 rebuttal 能提供 connector-swap 实验或 real-robot 初步验证，评分可上调至 borderline accept。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2"
}
```

</details>

---


## Round 8

## Round 8

18 recorded events


### User

_source line 349 · 2026-05-21T14:21:38.516560+00:00_

[Round 1 审稿请求]:
以下是 Reviewer 1 的完整审稿意见，请逐条回应。对每个 Weakness 和 Strength，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。

---

# Reviewer 1 审稿意见 — CoRL 2026

## 1. Summary

本文系统研究了 7 个 VLA 模型（450M–7B）跨三类 vision connector 的 token pruning 行为，在 LIBERO 仿真基准上提出四类可压缩性分类（uniformly critical, threshold-graded, smooth graded, catastrophic cliff），并声称 token importance 的 CV（变异系数）可同时预测容忍度类别和最优剪枝策略。此外提出 VTR（Vision Token Re-encoder）模块在 pixel-shuffle 架构的 catastrophic cliff 情况下恢复 60%+ 成功率。论文选题有实际价值，实验覆盖面较广，但在实验统计严谨性、CV predictor 的验证充分性、以及 controlled comparison 的 claim 强度方面存在若干需要修正的问题。

## 2. Strengths

**S1. 问题定义精准且有实际意义**：系统研究 VLA token pruning 在不同 connector 架构间的不对称行为，这是一个被忽视但对部署效率至关重要的问题。CoRL 社区高度相关。

**S2. 跨架构覆盖面广**：7 个模型、3 类 connector、从 450M 到 7B 参数，提供了目前该领域最全面的对比。四类分类体系（Table 1）直觉清晰、实用性强。

**S3. 关键实验发现有说服力**：π₀.5 在 k=0.5 处 L2 vs random 的 36pp 差距（Section 4.4）有力地推翻了 π₀ offline-only 评估带来的"immune"假设，是本文最有价值的发现之一。SmolVLA 的 catastrophic cliff（5% removal 即 0% SR）也很有说明力。

**S4. 论文写作质量高**：结构清晰，claims 与证据的对应关系明确，limitations section 坦诚地讨论了主要局限（单一 benchmark、offline-only π₀ 评估、CV 验证不足等）。

**S5. VTR 设计有控制意识**：extended training control（45.0% vs 44.8%）排除了额外训练步数的影响，MLP adapter 对照排除了 attention 机制本身的贡献，实验设计思路正确。

## 3. Weaknesses

### Must-Fix

**N1 [critical] SmolVLA baseline 远低于官方结果，严重影响 cliff-edge 结论的可推广性**
- SmolVLA baseline 44.8% vs 官方 87.3%（42.5pp gap，batch size 4 vs 64）。Official checkpoint (59.2%) 也测了 cliff-edge 但仅一个配置。
- 如果 cliff-edge 主要建立在 undertrained checkpoint 上，taxonomy 下界和 VTR 实用价值都受质疑。
- 建议：official checkpoint 完整 pruning sweep。

**N2 [critical] CV predictor 仅在 3 个模型 × 2 个 retention ratio 上验证——数据点严重不足**
- Table 3 仅 6 个数据点，k=0.3 有 reversal。
- 3 个模型同时在 connector、backbone、encoder fusion、token count 上不同。
- CV 范围两端（π₀ CV=0.038, SmolVLA CV=0.314）缺 L2 vs random 对比。
- 建议：降级 claim 或增加模型验证。

**N3 [critical] π₀ 仅有 offline 评估但被归类为 "uniformly critical" 并用于核心 comparison**
- Table 1 中 π₀ 与 π₀.5 并列但评估协议不同。
- π₀–OpenVLA 的 63pp gap 实际是 offline loss vs closed-loop SR 的不可比对比。
- 建议：明显标注 offline-only，降级 π₀ 相关 comparison 的证据强度。

### Should-Fix

**W1** OpenVLA L2 vs random 用不同 seed（seed42 vs seed7），k=0.5 same-seed 验证缺失。
**W2** VTR p=0.15 不足以声称 "re-encoding is the operative mechanism"。
**W3** π₀ vs OpenVLA "most controlled comparison" 实际有三个变量不同。
**W4** M=96 dip（54.5±3.2%）破坏 "flat M-curve" 叙述。
**W5** X-VLA 的 "linear projection" 分类标签与 12-layer BART encoder 不匹配。

### Minor
m1-m4 涉及 CogACT 计入 7 models、k=0.5 验证措辞、引用核查、figure 位置。

## 4. Questions for Authors
Q1: Official SmolVLA checkpoint 是否所有 k 值均 0%?
Q2: CV=0.15 threshold 是否 post-hoc?
Q3: VTR 在 OpenVLA 上 0% SR 对 workflow 实用性的影响?
Q4: V-shaped L2 curve 更深入解释?
Q5: OFT pruning 评估计划?

## 7. Overall: Borderline (倾向 weak reject), Confidence: High

---

请对 R1 的每个 Weakness（N1-N3, W1-W5）和 Strengths（S1-S5）逐条给出 [AGREE] 或 [REBUT] 回应，引用论文具体位置作为证据。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 350 · 2026-05-21T14:23:17.267943+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/main.pdf",
  "project": "importance_margin_vla_compress",
  "pages": "2,5,7,9,10",
  "dpi": "165",
  "output_dir": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/.claude/sessions/review_reviewer_2_29d69ba3/_pdf_images"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/main.pdf",
    "project": "importance_margin_vla_compress",
    "pages": "2,5,7,9,10",
    "dpi": "165",
    "output_dir": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/.claude/sessions/review_reviewer_2_29d69ba3/_pdf_images"
  }
}
```

</details>

---


### Tool result

_source line 351 · 2026-05-21T14:23:18.074834+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 2, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/.claude/sessions/review_reviewer_2_29d69ba3/_pdf_images/main_p2.png\", \"width\": 1403, \"height\": 1815, \"size_kb\": 473.6}, {\"page\": 5, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/.claude/sessions/review_reviewer_2_29d69ba3/_pdf_images/main_p5.png\", \"width\": 1403, \"height\": 1815, \"size_kb\": 420.4}, {\"page\": 7, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/.claude/sessions/review_reviewer_2_29d69ba3/_pdf_images/main_p7.png\", \"width\": 1403, \"height\": 1815, \"size_kb\": 421.5}, {\"page\": 9, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/.claude/sessions/review_reviewer_2_29d69ba3/_pdf_images/main_p9.png\", \"width\": 1403, \"height\": 1815, \"size_kb\": 376.5}, {\"page\": 10, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/.claude/sessions/review_reviewer_2_29d69ba3/_pdf_images/main_p10.png\", \"width\": 1403, \"height\": 1815, \"size_kb\": 331.5}], \"total_pages\": 25, \"rendered_pages\": 5, \"dpi\": 165, \"output_dir\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/.claude/sessions/review_reviewer_2_29d69ba3/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 806
}
```

</details>

---


### Tool call

_source line 352 · 2026-05-21T14:23:23.709400+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/.claude/sessions/review_reviewer_2_29d69ba3/_pdf_images/main_p2.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/.claude/sessions/review_reviewer_2_29d69ba3/_pdf_images/main_p2.png"
  }
}
```

</details>

---


### Tool call

_source line 353 · 2026-05-21T14:23:24.641466+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/.claude/sessions/review_reviewer_2_29d69ba3/_pdf_images/main_p5.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/.claude/sessions/review_reviewer_2_29d69ba3/_pdf_images/main_p5.png"
  }
}
```

</details>

---


### Tool result

_source line 354 · 2026-05-21T14:23:25.196054+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1486
}
```

</details>

---


### Tool call

_source line 355 · 2026-05-21T14:23:25.296977+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/.claude/sessions/review_reviewer_2_29d69ba3/_pdf_images/main_p7.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/.claude/sessions/review_reviewer_2_29d69ba3/_pdf_images/main_p7.png"
  }
}
```

</details>

---


### Tool result

_source line 356 · 2026-05-21T14:23:26.000974+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1359
}
```

</details>

---


### Tool result

_source line 357 · 2026-05-21T14:23:26.052448+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 755
}
```

</details>

---


### Tool call

_source line 358 · 2026-05-21T14:23:26.052932+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/.claude/sessions/review_reviewer_2_29d69ba3/_pdf_images/main_p9.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/.claude/sessions/review_reviewer_2_29d69ba3/_pdf_images/main_p9.png"
  }
}
```

</details>

---


### Tool call

_source line 359 · 2026-05-21T14:23:26.405491+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/.claude/sessions/review_reviewer_2_29d69ba3/_pdf_images/main_p10.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/.claude/sessions/review_reviewer_2_29d69ba3/_pdf_images/main_p10.png"
  }
}
```

</details>

---


### Tool result

_source line 360 · 2026-05-21T14:23:26.508561+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 455
}
```

</details>

---


### Tool result

_source line 361 · 2026-05-21T14:23:26.913727+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 508
}
```

</details>

---


### Tool call

_source line 362 · 2026-05-21T14:26:04.175085+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "\n# Reviewer 2 交叉回应 Reviewer 1 审稿意见\n\n---\n\n## Strengths 回应\n\n**[AGREE] R1-S1: 问题定义精准且有实际意义。**\n完全同意。VLA token pruning 的跨架构不对称行为是一个被忽视但部署高度相关的问题。\n\n**[AGREE with caveat] R1-S2: 跨架构覆盖面广。**\n同意覆盖面是优势，但需补充一个重要 caveat：7 个模型实际只覆盖 3 种 connector 类型（linear projection / MLP / pixel-shuffle），within-connector 模型间的行为高度一致（如 OpenVLA、OFT、CogACT 的 CV 值均在 0.21-0.22 区间），所以有效独立数据点接近 3 而非 7。R1 在 N2 中也指出了这一点。\n\n**[REBUT] R1-S3: \"π₀.5 的 36pp 差距有力推翻了 'immune' 假设\"。**\nR1 将此列为本文\"最有价值的发现之一\"，我不同意这一评价。关键问题在于：π₀ 和 π₀.5 的原始论文（Black et al. 2024, 2025）从未声称对 token pruning \"immune\"。论文 Section 4.4 称要 \"falsify the 'immune' interpretation\"，但这个 interpretation 是作者自己从 offline metrics 推导出来然后自己推翻的——这是经典的稻草人论证（我的审稿 W1 有详细论述）。\n\n36pp offline-vs-closed-loop 差距本身是一个有价值的 empirical observation（证明 offline proxy 不可靠），但 \"falsify immune assumption\" 的 framing 人为放大了这个发现的 novelty。建议改为 \"demonstrates that offline action-loss metrics are misleading proxies for closed-loop pruning tolerance\"。\n\n**[AGREE] R1-S4: 写作质量高。**\n同意。结构清晰，claims-evidence 对应关系明确。我的审稿给 Clarity 4/5。\n\n**[AGREE] R1-S5: VTR 控制实验设计好。**\n同意。Extended training control（45.0% vs 44.8% baseline, Section 4.5/Table 2）排除了额外训练步数的混淆，MLP adapter 对照排除了参数增加本身的贡献。这体现了良好的实验设计思路。\n\n---\n\n## Must-Fix 回应\n\n**[AGREE] R1-N1: SmolVLA baseline 远低于官方结果。**\n\n完全同意这是一个核心 validity 问题。补充两个观察：\n\n1. **VTR 的实用性直接受影响。** VTR 仅在 44.8% baseline 上训练和评估，达到 60.1% SR。但这个 60.1% 是在一个本身就严重 underperforming 的模型上获得的——实际上 VTR 的恢复效果甚至超过了 unpruned baseline（60.1% > 44.8%），这暗示 VTR 可能部分是在补偿 undertrained model 的缺陷而非真正解决 pruning 损伤。论文虽然在 official checkpoint 上也测了一个配置（Section 4.2：\"official SmolVLA checkpoint (59.2%) exhibits identical failure\"），但 VTR 在 official checkpoint 上的恢复能力未验证。\n\n2. **对 taxonomy 下界的影响。** \"Catastrophic cliff\" 类别（5% removal → 0% SR）建立在 44.8% baseline 上。如果 official checkpoint（59.2%）在某些较温和的 pruning ratio 下不会完全崩溃到 0%，cliff-edge 的 sharpness 可能被 undertrained checkpoint 放大了。R1 建议的 \"official checkpoint 完整 pruning sweep\" 是验证 taxonomy robustness 的 minimum requirement。\n\n**[AGREE] R1-N2: CV predictor 数据点严重不足。**\n\n强烈同意。这与我自己审稿的 N2 一致。补充几个 R1 未展开的具体问题：\n\n1. **Table 3 的 reversal 问题比 R1 描述的更严重。** 在 k=0.5 时 OpenVLA 的 Δ(R−L2) 接近零或反转（Table 3, page 10），而在 k=0.7 时方向再次变化。这意味着即使在仅有的 6 个数据点中，CV 对策略选择的预测已经不稳定。\n\n2. **极端 CV 值恰恰是最需要验证的区域。** π₀.5（CV=0.055）和 SmolVLA（CV=0.314）分别处于 CV 范围的两端，但这两个模型在 Table 3 中都没有完整的 L2 vs random closed-loop 对比——π₀.5 只有 partial data，SmolVLA 因为所有 pruning 都导致 0% SR 而无法比较策略。也就是说，CV predictor 在最需要被测试的极端值处恰好没有证据。\n\n3. **统计层面。** 6 个数据点甚至不足以计算有意义的相关系数或进行非参数检验。\"Monotonic relationship\" 在 N=6 且存在 reversal 的情况下不构成统计证据。\n\n**[AGREE] R1-N3: π₀ offline-only 评估但参与核心 comparison。**\n\n完全同意。补充一个 internal consistency 问题：Section 5.4 (\"Offline Methods Underestimate Closed-Loop\") 论文自身的分析恰恰说明 offline metrics 系统性低估 pruning 伤害——π₀ 在 offline 评估中 action loss 仅增加 2.4%（Table 1, k=0.1），但论文自己论证了这类 offline 结果不可信。然而 Table 1 仍将 π₀ 的 offline 结果与其他模型的 closed-loop SR 并列展示，且 π₀ 被用于支撑 \"uniformly critical\" 分类和 \"connector determines compressibility\" 的核心论证。\n\n更严格地说：论文声称评估了 7 个模型，但具备完整自有 closed-loop evaluation 的仅约 4-5 个（SmolVLA, OpenVLA, X-VLA, π₀.5, 可能 OFT）。π₀ 是 offline-only，CogACT 74.2% 来自 EfficientVLA。Contribution C1 \"evaluating seven models\" 的表述应当降级。\n\n---\n\n## Should-Fix 回应\n\n**[AGREE] R1-W1: OpenVLA L2 vs random seed 不一致。**\n同意。Seed42 vs seed7 引入不必要的混淆变量。虽然 seed 对 aggregate 结果的影响通常较小，但在声称 \"L2 outperforms/underperforms random\" 的定量对比中，same-seed 是 minimum methodological requirement。这是一个容易修复的问题，不应成为 blocker，但需要在 rebuttal 中 acknowledge 或补充实验。\n\n**[AGREE] R1-W2: VTR p=0.15 dropout ablation 不充分。**\n同意。p=0.15 是非常轻的 perturbation，不足以支撑 \"re-encoding is the operative mechanism\" 的声明。更有说服力的 ablation 应该是：(a) 用 mean pooling 替代 cross-attention，(b) 用 random projection 替代 learned queries，(c) 用更高 dropout（如 p=0.5）测试。\n\n不过，MLP adapter 对照（Table 2）本身是一个更强的 evidence——MLP adapter 无法恢复性能而 cross-attention 可以，这确实暗示 attention 机制的作用。所以 \"re-encoding is operative\" 的 claim 有部分支撑，只是 dropout ablation 这个具体 evidence 不够强。\n\n**[AGREE] R1-W3: π₀ vs OpenVLA \"most controlled comparison\" 不成立。**\n强烈同意。这与我的审稿 N1（因果声明 under-identified）直接相关。Page 5 将 π₀-OpenVLA 称为 \"the most controlled available comparison\"，但两者在 vision encoder（SigLIP vs DINOv2）、action head（flow matching vs autoregressive）、LLM backbone（PaliGemma vs Llama-2）上同时不同。三个变量同时变化时，无法将差异归因于 connector。\n\n论文的 within-connector comparison（OpenVLA vs OFT vs CogACT，均为 MLP + 不同 backbone/action head → 相似 CV 和降解模式）实际上是更好的 controlled evidence。建议作者将 narrative 重心从跨 connector 的 \"most controlled pair\" 转向 within-connector 的一致性。\n\n**[REBUT] R1-W4: M=96 dip 破坏 \"flat M-curve\" 叙述。**\n部分不同意。Table 2 中各 M 值的 SR：M=16 → 60.1%，M=32 → 约 60.4%，M=64 → 约 62.8%，M=96 → 54.5±3.2%，M=128 → 约 53.8%。M=96 的 dip 确实存在，但需注意：\n- 54.5±3.2% 的 confidence interval 与相邻 M 值存在重叠\n- M=128 也是约 53.8%，说明 M=96 和 M=128 的下降可能是一个连续趋势（过多 query vectors 引入过拟合），而非 M=96 的 anomaly\n- 论文应用 \"relatively stable\" 替代 \"flat\"，但这不构成核心叙述的根本破坏\n\nR1 指出 M=96 anomaly 是合理的审查，但将其提升为 \"破坏叙述\" 略过了 CI overlap 的因素。建议作者在 revision 中讨论 M 值增大时的 diminishing/negative returns 趋势。\n\n**[AGREE] R1-W5: X-VLA 的分类标签问题。**\n强烈同意。Table 1 将 X-VLA 标注为 \"Linear proj†\"（带 dagger footnote），但 X-VLA 实际使用 linear projection + 12-layer BART encoder（page 5 明确说明 \"the effective pipeline is not purely linear\"）。这个分类有两个问题：\n\n1. **标签误导。** 即使有 footnote，将 12-layer BART encoder 归类为 \"linear projection\" 在 Table 1 的快速浏览中会误导读者。X-VLA 的 CV=0.151 明显高于纯 linear projection 模型（π₀ CV=0.038, π₀.5 CV=0.055），反而更接近 MLP 模型（OpenVLA CV=0.215）。\n\n2. **暴露 taxonomy 粒度不足。** 三分类（linear / MLP / pixel-shuffle）无法容纳 BART encoder 这种 intermediate complexity 的 connector。X-VLA 的行为（threshold-graded, CV=0.151）落在 linear projection（uniformly critical, CV≈0.04-0.06）和 MLP（smooth graded, CV≈0.21-0.22）之间，暗示 connector 复杂度可能是一个连续谱而非离散类别。这直接支持了我在审稿 N2 中提出的 \"taxonomy 覆盖不足\" 的关注。\n\n---\n\n## Minor 回应\n\n**[AGREE] m1 (CogACT 计入 7 models):** 与 N3 一致。\n**[AGREE] m2 (k=0.5 验证措辞):** 合理的表述精确性要求。\n**[AGREE] m3 (引用核查):** 我的引用验证显示 41 篇中 5 篇 not_found（均为近期 arXiv 预印本），6 篇 minor first-author mismatch，无虚假引用。\n**[AGREE] m4 (figure 位置):** Figure 位置优化是 camera-ready 阶段的标准修改。\n\n---\n\n## 总结\n\nR1 和我的审稿在核心问题上高度一致：(1) 因果声明 under-identified（R1-W3 / 我的 N1），(2) CV predictor 样本量不足（R1-N2 / 我的 N2），(3) π₀ 评估协议不一致（R1-N3 / 我的 W3）。R1 新增了一个我遗漏的重要问题——SmolVLA baseline gap（R1-N1），这直接影响 cliff-edge 结论和 VTR 实用性的可推广性。\n\n主要分歧在两点：\n- **R1-S3 (36pp gap 是最有价值发现):** 我认为 \"immune falsification\" 是稻草人论证，发现本身有价值但 framing 夸大了 novelty。\n- **R1-W4 (M=96 dip):** 我认为 CI overlap 使这更可能是 noise 而非 systematic failure，不构成核心叙述的破坏。\n\n综合 R1 审稿，我维持 **weak reject (borderline)** 的评分不变。R1-N1（SmolVLA baseline gap）进一步增强了我对 VTR 实用性的疑虑，但没有改变整体判断的方向。\n",
  "reviewer_id": "2",
  "project": "importance_margin_vla_compress"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "\n# Reviewer 2 交叉回应 Reviewer 1 审稿意见\n\n---\n\n## Strengths 回应\n\n**[AGREE] R1-S1: 问题定义精准且有实际意义。**\n完全同意。VLA token pruning 的跨架构不对称行为是一个被忽视但部署高度相关的问题。\n\n**[AGREE with caveat] R1-S2: 跨架构覆盖面广。**\n同意覆盖面是优势，但需补充一个重要 caveat：7 个模型实际只覆盖 3 种 connector 类型（linear projection / MLP / pixel-shuffle），within-connector 模型间的行为高度一致（如 OpenVLA、OFT、CogACT 的 CV 值均在 0.21-0.22 区间），所以有效独立数据点接近 3 而非 7。R1 在 N2 中也指出了这一点。\n\n**[REBUT] R1-S3: \"π₀.5 的 36pp 差距有力推翻了 'immune' 假设\"。**\nR1 将此列为本文\"最有价值的发现之一\"，我不同意这一评价。关键问题在于：π₀ 和 π₀.5 的原始论文（Black et al. 2024, 2025）从未声称对 token pruning \"immune\"。论文 Section 4.4 称要 \"falsify the 'immune' interpretation\"，但这个 interpretation 是作者自己从 offline metrics 推导出来然后自己推翻的——这是经典的稻草人论证（我的审稿 W1 有详细论述）。\n\n36pp offline-vs-closed-loop 差距本身是一个有价值的 empirical observation（证明 offline proxy 不可靠），但 \"falsify immune assumption\" 的 framing 人为放大了这个发现的 novelty。建议改为 \"demonstrates that offline action-loss metrics are misleading proxies for closed-loop pruning tolerance\"。\n\n**[AGREE] R1-S4: 写作质量高。**\n同意。结构清晰，claims-evidence 对应关系明确。我的审稿给 Clarity 4/5。\n\n**[AGREE] R1-S5: VTR 控制实验设计好。**\n同意。Extended training control（45.0% vs 44.8% baseline, Section 4.5/Table 2）排除了额外训练步数的混淆，MLP adapter 对照排除了参数增加本身的贡献。这体现了良好的实验设计思路。\n\n---\n\n## Must-Fix 回应\n\n**[AGREE] R1-N1: SmolVLA baseline 远低于官方结果。**\n\n完全同意这是一个核心 validity 问题。补充两个观察：\n\n1. **VTR 的实用性直接受影响。** VTR 仅在 44.8% baseline 上训练和评估，达到 60.1% SR。但这个 60.1% 是在一个本身就严重 underperforming 的模型上获得的——实际上 VTR 的恢复效果甚至超过了 unpruned baseline（60.1% > 44.8%），这暗示 VTR 可能部分是在补偿 undertrained model 的缺陷而非真正解决 pruning 损伤。论文虽然在 official checkpoint 上也测了一个配置（Section 4.2：\"official SmolVLA checkpoint (59.2%) exhibits identical failure\"），但 VTR 在 official checkpoint 上的恢复能力未验证。\n\n2. **对 taxonomy 下界的影响。** \"Catastrophic cliff\" 类别（5% removal → 0% SR）建立在 44.8% baseline 上。如果 official checkpoint（59.2%）在某些较温和的 pruning ratio 下不会完全崩溃到 0%，cliff-edge 的 sharpness 可能被 undertrained checkpoint 放大了。R1 建议的 \"official checkpoint 完整 pruning sweep\" 是验证 taxonomy robustness 的 minimum requirement。\n\n**[AGREE] R1-N2: CV predictor 数据点严重不足。**\n\n强烈同意。这与我自己审稿的 N2 一致。补充几个 R1 未展开的具体问题：\n\n1. **Table 3 的 reversal 问题比 R1 描述的更严重。** 在 k=0.5 时 OpenVLA 的 Δ(R−L2) 接近零或反转（Table 3, page 10），而在 k=0.7 时方向再次变化。这意味着即使在仅有的 6 个数据点中，CV 对策略选择的预测已经不稳定。\n\n2. **极端 CV 值恰恰是最需要验证的区域。** π₀.5（CV=0.055）和 SmolVLA（CV=0.314）分别处于 CV 范围的两端，但这两个模型在 Table 3 中都没有完整的 L2 vs random closed-loop 对比——π₀.5 只有 partial data，SmolVLA 因为所有 pruning 都导致 0% SR 而无法比较策略。也就是说，CV predictor 在最需要被测试的极端值处恰好没有证据。\n\n3. **统计层面。** 6 个数据点甚至不足以计算有意义的相关系数或进行非参数检验。\"Monotonic relationship\" 在 N=6 且存在 reversal 的情况下不构成统计证据。\n\n**[AGREE] R1-N3: π₀ offline-only 评估但参与核心 comparison。**\n\n完全同意。补充一个 internal consistency 问题：Section 5.4 (\"Offline Methods Underestimate Closed-Loop\") 论文自身的分析恰恰说明 offline metrics 系统性低估 pruning 伤害——π₀ 在 offline 评估中 action loss 仅增加 2.4%（Table 1, k=0.1），但论文自己论证了这类 offline 结果不可信。然而 Table 1 仍将 π₀ 的 offline 结果与其他模型的 closed-loop SR 并列展示，且 π₀ 被用于支撑 \"uniformly critical\" 分类和 \"connector determines compressibility\" 的核心论证。\n\n更严格地说：论文声称评估了 7 个模型，但具备完整自有 closed-loop evaluation 的仅约 4-5 个（SmolVLA, OpenVLA, X-VLA, π₀.5, 可能 OFT）。π₀ 是 offline-only，CogACT 74.2% 来自 EfficientVLA。Contribution C1 \"evaluating seven models\" 的表述应当降级。\n\n---\n\n## Should-Fix 回应\n\n**[AGREE] R1-W1: OpenVLA L2 vs random seed 不一致。**\n同意。Seed42 vs seed7 引入不必要的混淆变量。虽然 seed 对 aggregate 结果的影响通常较小，但在声称 \"L2 outperforms/underperforms random\" 的定量对比中，same-seed 是 minimum methodological requirement。这是一个容易修复的问题，不应成为 blocker，但需要在 rebuttal 中 acknowledge 或补充实验。\n\n**[AGREE] R1-W2: VTR p=0.15 dropout ablation 不充分。**\n同意。p=0.15 是非常轻的 perturbation，不足以支撑 \"re-encoding is the operative mechanism\" 的声明。更有说服力的 ablation 应该是：(a) 用 mean pooling 替代 cross-attention，(b) 用 random projection 替代 learned queries，(c) 用更高 dropout（如 p=0.5）测试。\n\n不过，MLP adapter 对照（Table 2）本身是一个更强的 evidence——MLP adapter 无法恢复性能而 cross-attention 可以，这确实暗示 attention 机制的作用。所以 \"re-encoding is operative\" 的 claim 有部分支撑，只是 dropout ablation 这个具体 evidence 不够强。\n\n**[AGREE] R1-W3: π₀ vs OpenVLA \"most controlled comparison\" 不成立。**\n强烈同意。这与我的审稿 N1（因果声明 under-identified）直接相关。Page 5 将 π₀-OpenVLA 称为 \"the most controlled available comparison\"，但两者在 vision encoder（SigLIP vs DINOv2）、action head（flow matching vs autoregressive）、LLM backbone（PaliGemma vs Llama-2）上同时不同。三个变量同时变化时，无法将差异归因于 connector。\n\n论文的 within-connector comparison（OpenVLA vs OFT vs CogACT，均为 MLP + 不同 backbone/action head → 相似 CV 和降解模式）实际上是更好的 controlled evidence。建议作者将 narrative 重心从跨 connector 的 \"most controlled pair\" 转向 within-connector 的一致性。\n\n**[REBUT] R1-W4: M=96 dip 破坏 \"flat M-curve\" 叙述。**\n部分不同意。Table 2 中各 M 值的 SR：M=16 → 60.1%，M=32 → 约 60.4%，M=64 → 约 62.8%，M=96 → 54.5±3.2%，M=128 → 约 53.8%。M=96 的 dip 确实存在，但需注意：\n- 54.5±3.2% 的 confidence interval 与相邻 M 值存在重叠\n- M=128 也是约 53.8%，说明 M=96 和 M=128 的下降可能是一个连续趋势（过多 query vectors 引入过拟合），而非 M=96 的 anomaly\n- 论文应用 \"relatively stable\" 替代 \"flat\"，但这不构成核心叙述的根本破坏\n\nR1 指出 M=96 anomaly 是合理的审查，但将其提升为 \"破坏叙述\" 略过了 CI overlap 的因素。建议作者在 revision 中讨论 M 值增大时的 diminishing/negative returns 趋势。\n\n**[AGREE] R1-W5: X-VLA 的分类标签问题。**\n强烈同意。Table 1 将 X-VLA 标注为 \"Linear proj†\"（带 dagger footnote），但 X-VLA 实际使用 linear projection + 12-layer BART encoder（page 5 明确说明 \"the effective pipeline is not purely linear\"）。这个分类有两个问题：\n\n1. **标签误导。** 即使有 footnote，将 12-layer BART encoder 归类为 \"linear projection\" 在 Table 1 的快速浏览中会误导读者。X-VLA 的 CV=0.151 明显高于纯 linear projection 模型（π₀ CV=0.038, π₀.5 CV=0.055），反而更接近 MLP 模型（OpenVLA CV=0.215）。\n\n2. **暴露 taxonomy 粒度不足。** 三分类（linear / MLP / pixel-shuffle）无法容纳 BART encoder 这种 intermediate complexity 的 connector。X-VLA 的行为（threshold-graded, CV=0.151）落在 linear projection（uniformly critical, CV≈0.04-0.06）和 MLP（smooth graded, CV≈0.21-0.22）之间，暗示 connector 复杂度可能是一个连续谱而非离散类别。这直接支持了我在审稿 N2 中提出的 \"taxonomy 覆盖不足\" 的关注。\n\n---\n\n## Minor 回应\n\n**[AGREE] m1 (CogACT 计入 7 models):** 与 N3 一致。\n**[AGREE] m2 (k=0.5 验证措辞):** 合理的表述精确性要求。\n**[AGREE] m3 (引用核查):** 我的引用验证显示 41 篇中 5 篇 not_found（均为近期 arXiv 预印本），6 篇 minor first-author mismatch，无虚假引用。\n**[AGREE] m4 (figure 位置):** Figure 位置优化是 camera-ready 阶段的标准修改。\n\n---\n\n## 总结\n\nR1 和我的审稿在核心问题上高度一致：(1) 因果声明 under-identified（R1-W3 / 我的 N1），(2) CV predictor 样本量不足（R1-N2 / 我的 N2），(3) π₀ 评估协议不一致（R1-N3 / 我的 W3）。R1 新增了一个我遗漏的重要问题——SmolVLA baseline gap（R1-N1），这直接影响 cliff-edge 结论和 VTR 实用性的可推广性。\n\n主要分歧在两点：\n- **R1-S3 (36pp gap 是最有价值发现):** 我认为 \"immune falsification\" 是稻草人论证，发现本身有价值但 framing 夸大了 novelty。\n- **R1-W4 (M=96 dip):** 我认为 CI overlap 使这更可能是 noise 而非 systematic failure，不构成核心叙述的破坏。\n\n综合 R1 审稿，我维持 **weak reject (borderline)** 的评分不变。R1-N1（SmolVLA baseline gap）进一步增强了我对 VTR 实用性的疑虑，但没有改变整体判断的方向。\n",
    "reviewer_id": "2",
    "project": "importance_margin_vla_compress"
  }
}
```

</details>

---


### Tool result

_source line 363 · 2026-05-21T14:26:07.983443+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3808
}
```

</details>

---


### Tool call

_source line 364 · 2026-05-21T14:26:15.423725+00:00_

called mcp__agent-ml-research__cleanup_pdf_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__cleanup_pdf_images</summary>

```json
{
  "output_dir": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/.claude/sessions/review_reviewer_2_29d69ba3/_pdf_images"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "tool_args": {
    "output_dir": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/.claude/sessions/review_reviewer_2_29d69ba3/_pdf_images"
  }
}
```

</details>

---


### Tool result

_source line 365 · 2026-05-21T14:26:15.424072+00:00_

{"result":"{\"success\": true, \"data\": {\"deleted\": 5, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/.claude/sessions/review_reviewer_2_29d69ba3/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "elapsed_ms": 0
}
```

</details>

---


### Assistant

_source line 366 · 2026-05-21T14:26:24.853809+00:00_

交叉回应已提交给 Director。

对 R1 的 15 个具体论点的回应总结：
- **10 个 [AGREE]**：N1（SmolVLA baseline gap）、N2（CV 数据点不足）、N3（π₀ offline-only）、W1（seed 不一致）、W2（dropout ablation 不充分）、W3（"most controlled" 不成立）、W5（X-VLA 分类错误）、S1、S4、S5
- **2 个 [REBUT]**：S3（"immune falsification" 是稻草人论证）、W4（M=96 dip 有 CI overlap，不构成核心叙述破坏）
- **1 个 [AGREE with caveat]**：S2（7 模型实际 3 connector 类型）

主要新增发现：R1-N1 揭示的 SmolVLA baseline gap 进一步削弱了 VTR 实用性声明（VTR 60.1% 可能部分在补偿 undertrained model 缺陷而非真正解决 pruning 损伤）。维持 weak reject (borderline) 评分不变。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2"
}
```

</details>

---


## Round 9

## Round 9

62 recorded events


### User

_source line 367 · 2026-05-22T08:06:53.762063+00:00_

[Round 5 审稿请求]:
你是 Reviewer 2（新颖性 + 定位 + venue fit），这是 Round 5 继续审稿。

## 投稿信息
- **Venue**: CoRL 2026 | **Deadline**: 2026-05-29
- **格式**: 8 页正文 + 附录/参考文献不计入 | Double-blind | corl_2026.sty

## 论文路径
- 主文件: `projects/importance_margin_vla_compress/docs/paper/main.tex`
- 各章节在同目录下

## 上一轮（Round 4）你的主要发现

以下是你在 Round 4 提出的问题清单。请逐条检查论文修改，标注 **[RESOLVED]** 或 **[STILL_OPEN]** + 理由。

### Must-Fix (Critical)

**R4-N1 [因果声明 under-identified — connector vs 多变量混淆]**
- 要求：降级为 "associated with"，或补充 connector-swap 实验
- Issue Tracker 状态：resolved — "All causal language downgraded: determines→associated"
- 请验证：Abstract, Introduction, Results, Discussion, Conclusion 中的因果语言

**R4-N2 [Taxonomy 和 CV predictor 仅 N=3 connector 类型]**
- 要求：增加 Perceiver/Q-Former 类，或降级 claim
- Issue Tracker 状态：resolved — "CV reframed as correlational"
- 请验证：claim 降级是否充分；Perceiver/Q-Former 是否在 Related Work 讨论更充分

**R4-N3 [纯仿真评估与 CoRL venue 要求]**
- Director Round 4 判断：降为 should-fix
- 请验证：是否增加了 sim-to-real transferability 讨论

### Should-Fix (Warning)

**R4-W1 ["Falsifies immune assumption" 是稻草人论证]**
- Issue Tracker: resolved — "All 'falsifies' removed"
- 请验证：Introduction 和 Results 中的措辞

**R4-W2 [VTR 新颖性有限]**
- Issue Tracker: resolved — "VTR framed as diagnostic protocol contribution"
- 请验证：Introduction contributions 和 Discussion 中的定位

**R4-W3 ["七个模型" framing 夸大]**
- Issue Tracker: resolved
- 请验证：Abstract 和 Introduction 是否区分 closed-loop vs offline/literature

**R4-W4 ["Diagnose-then-Compress framework" 过度包装]**
- Issue Tracker: resolved — "All 'framework' replaced with 'diagnostic protocol'"
- 请验证：全文一致性

**R4-W5 [正文超页]**
- Issue Tracker: resolved — "Paper compressed to 8 pages"
- 请验证：正文页数

### 新增审查

除了验证上述修复外，请特别关注：
1. **Related Work 是否已充分扩展**：Round 4 建议增加 15+ citations，Don't Run with Scissors 对比讨论
2. **新增 Section 4.7 Cross-Suite Generalization 的 novelty 贡献**：hypergeometric cliff model 是否过度拟合？
3. **整体 positioning 是否改善**：从 "framework paper" 到 "diagnostic empirical study" 的转型是否成功
4. **标题是否仍然合适**：在 claim 降级后，"Why Token Pruning Crashes" 是否与内容匹配

请按以下格式输出：
1. Round 4 Issue 逐条验证（[RESOLVED] / [STILL_OPEN]）
2. 新发现的问题（如有）
3. Overall Score（与 Round 4 对比是否变化）+ Confidence

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 368 · 2026-05-22T08:07:07.616048+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/main.pdf",
  "project": "importance_margin_vla_compress",
  "pages": "1-5",
  "dpi": "150",
  "output_dir": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/.claude/sessions/review_reviewer_2_29d69ba3/_pdf_r5_1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/main.pdf",
    "project": "importance_margin_vla_compress",
    "pages": "1-5",
    "dpi": "150",
    "output_dir": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/.claude/sessions/review_reviewer_2_29d69ba3/_pdf_r5_1"
  }
}
```

</details>

---


### Tool result

_source line 369 · 2026-05-22T08:07:08.573249+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 1, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/.claude/sessions/review_reviewer_2_29d69ba3/_pdf_r5_1/main_p1.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 312.2}, {\"page\": 2, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/.claude/sessions/review_reviewer_2_29d69ba3/_pdf_r5_1/main_p2.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 309.9}, {\"page\": 3, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/.claude/sessions/review_reviewer_2_29d69ba3/_pdf_r5_1/main_p3.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 389.3}, {\"page\": 4, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/.claude/sessions/review_reviewer_2_29d69ba3/_pdf_r5_1/main_p4.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 328.0}, {\"page\": 5, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/.claude/sessions/review_reviewer_2_29d69ba3/_pdf_r5_1/main_p5.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 384.2}], \"total_pages\": 27, \"rendered_pages\": 5, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/.claude/sessions/review_reviewer_2_29d69ba3/_pdf_r5_1\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 957
}
```

</details>

---


### Tool call

_source line 370 · 2026-05-22T08:07:08.774494+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/main.pdf",
  "project": "importance_margin_vla_compress",
  "pages": "6-10",
  "dpi": "150",
  "output_dir": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/.claude/sessions/review_reviewer_2_29d69ba3/_pdf_r5_2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/main.pdf",
    "project": "importance_margin_vla_compress",
    "pages": "6-10",
    "dpi": "150",
    "output_dir": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/.claude/sessions/review_reviewer_2_29d69ba3/_pdf_r5_2"
  }
}
```

</details>

---


### Tool result

_source line 371 · 2026-05-22T08:07:09.336545+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 6, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/.claude/sessions/review_reviewer_2_29d69ba3/_pdf_r5_2/main_p6.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 387.4}, {\"page\": 7, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/.claude/sessions/review_reviewer_2_29d69ba3/_pdf_r5_2/main_p7.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 340.8}, {\"page\": 8, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/.claude/sessions/review_reviewer_2_29d69ba3/_pdf_r5_2/main_p8.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 311.3}, {\"page\": 9, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/.claude/sessions/review_reviewer_2_29d69ba3/_pdf_r5_2/main_p9.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 325.0}, {\"page\": 10, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/.claude/sessions/review_reviewer_2_29d69ba3/_pdf_r5_2/main_p10.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 353.5}], \"total_pages\": 27, \"rendered_pages\": 5, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/.claude/sessions/review_reviewer_2_29d69ba3/_pdf_r5_2\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 562
}
```

</details>

---


### Tool call

_source line 372 · 2026-05-22T08:07:16.029459+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/.claude/sessions/review_reviewer_2_29d69ba3/_pdf_r5_1/main_p1.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/.claude/sessions/review_reviewer_2_29d69ba3/_pdf_r5_1/main_p1.png"
  }
}
```

</details>

---


### Tool call

_source line 373 · 2026-05-22T08:07:16.586353+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/.claude/sessions/review_reviewer_2_29d69ba3/_pdf_r5_1/main_p2.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/.claude/sessions/review_reviewer_2_29d69ba3/_pdf_r5_1/main_p2.png"
  }
}
```

</details>

---


### Tool result

_source line 374 · 2026-05-22T08:07:17.595006+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1565
}
```

</details>

---


### Tool call

_source line 375 · 2026-05-22T08:07:17.597713+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/.claude/sessions/review_reviewer_2_29d69ba3/_pdf_r5_1/main_p3.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/.claude/sessions/review_reviewer_2_29d69ba3/_pdf_r5_1/main_p3.png"
  }
}
```

</details>

---


### Tool result

_source line 376 · 2026-05-22T08:07:18.010410+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1424
}
```

</details>

---


### Tool call

_source line 377 · 2026-05-22T08:07:18.010899+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/.claude/sessions/review_reviewer_2_29d69ba3/_pdf_r5_1/main_p4.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/.claude/sessions/review_reviewer_2_29d69ba3/_pdf_r5_1/main_p4.png"
  }
}
```

</details>

---


### Tool result

_source line 378 · 2026-05-22T08:07:18.702469+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1104
}
```

</details>

---


### Tool call

_source line 379 · 2026-05-22T08:07:18.702953+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/.claude/sessions/review_reviewer_2_29d69ba3/_pdf_r5_1/main_p5.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/.claude/sessions/review_reviewer_2_29d69ba3/_pdf_r5_1/main_p5.png"
  }
}
```

</details>

---


### Tool result

_source line 380 · 2026-05-22T08:07:18.956275+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 945
}
```

</details>

---


### Tool result

_source line 381 · 2026-05-22T08:07:19.311858+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 608
}
```

</details>

---


### Tool call

_source line 382 · 2026-05-22T08:08:12.514580+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/.claude/sessions/review_reviewer_2_29d69ba3/_pdf_r5_2/main_p6.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/.claude/sessions/review_reviewer_2_29d69ba3/_pdf_r5_2/main_p6.png"
  }
}
```

</details>

---


### Tool call

_source line 383 · 2026-05-22T08:08:12.865958+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/.claude/sessions/review_reviewer_2_29d69ba3/_pdf_r5_2/main_p7.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/.claude/sessions/review_reviewer_2_29d69ba3/_pdf_r5_2/main_p7.png"
  }
}
```

</details>

---


### Tool result

_source line 384 · 2026-05-22T08:08:13.221199+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 706
}
```

</details>

---


### Tool call

_source line 385 · 2026-05-22T08:08:13.322060+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/.claude/sessions/review_reviewer_2_29d69ba3/_pdf_r5_2/main_p8.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/.claude/sessions/review_reviewer_2_29d69ba3/_pdf_r5_2/main_p8.png"
  }
}
```

</details>

---


### Tool result

_source line 386 · 2026-05-22T08:08:14.178728+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1312
}
```

</details>

---


### Tool result

_source line 387 · 2026-05-22T08:08:14.180869+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 858
}
```

</details>

---


### Tool call

_source line 388 · 2026-05-22T08:08:14.181409+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/.claude/sessions/review_reviewer_2_29d69ba3/_pdf_r5_2/main_p9.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/.claude/sessions/review_reviewer_2_29d69ba3/_pdf_r5_2/main_p9.png"
  }
}
```

</details>

---


### Tool call

_source line 389 · 2026-05-22T08:08:14.534317+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/.claude/sessions/review_reviewer_2_29d69ba3/_pdf_r5_2/main_p10.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/.claude/sessions/review_reviewer_2_29d69ba3/_pdf_r5_2/main_p10.png"
  }
}
```

</details>

---


### Tool result

_source line 390 · 2026-05-22T08:08:14.586851+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 405
}
```

</details>

---


### Tool result

_source line 391 · 2026-05-22T08:08:14.992600+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 458
}
```

</details>

---


### Tool call

_source line 392 · 2026-05-22T08:09:18.674368+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/main.pdf",
  "project": "importance_margin_vla_compress",
  "pages": "11-15",
  "dpi": "150",
  "output_dir": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/.claude/sessions/review_reviewer_2_29d69ba3/_pdf_r5_3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/main.pdf",
    "project": "importance_margin_vla_compress",
    "pages": "11-15",
    "dpi": "150",
    "output_dir": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/.claude/sessions/review_reviewer_2_29d69ba3/_pdf_r5_3"
  }
}
```

</details>

---


### Tool result

_source line 393 · 2026-05-22T08:09:19.489942+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 11, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/.claude/sessions/review_reviewer_2_29d69ba3/_pdf_r5_3/main_p11.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 355.4}, {\"page\": 12, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/.claude/sessions/review_reviewer_2_29d69ba3/_pdf_r5_3/main_p12.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 310.8}, {\"page\": 13, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/.claude/sessions/review_reviewer_2_29d69ba3/_pdf_r5_3/main_p13.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 173.8}, {\"page\": 14, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/.claude/sessions/review_reviewer_2_29d69ba3/_pdf_r5_3/main_p14.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 282.6}, {\"page\": 15, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/.claude/sessions/review_reviewer_2_29d69ba3/_pdf_r5_3/main_p15.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 316.3}], \"total_pages\": 27, \"rendered_pages\": 5, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/.claude/sessions/review_reviewer_2_29d69ba3/_pdf_r5_3\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 815
}
```

</details>

---


### Tool call

_source line 394 · 2026-05-22T08:09:20.445374+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/main.pdf",
  "project": "importance_margin_vla_compress",
  "pages": "16-20",
  "dpi": "150",
  "output_dir": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/.claude/sessions/review_reviewer_2_29d69ba3/_pdf_r5_4"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/main.pdf",
    "project": "importance_margin_vla_compress",
    "pages": "16-20",
    "dpi": "150",
    "output_dir": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/.claude/sessions/review_reviewer_2_29d69ba3/_pdf_r5_4"
  }
}
```

</details>

---


### Tool result

_source line 395 · 2026-05-22T08:09:21.349955+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 16, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/.claude/sessions/review_reviewer_2_29d69ba3/_pdf_r5_4/main_p16.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 190.9}, {\"page\": 17, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/.claude/sessions/review_reviewer_2_29d69ba3/_pdf_r5_4/main_p17.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 275.4}, {\"page\": 18, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/.claude/sessions/review_reviewer_2_29d69ba3/_pdf_r5_4/main_p18.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 316.4}, {\"page\": 19, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/.claude/sessions/review_reviewer_2_29d69ba3/_pdf_r5_4/main_p19.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 290.3}, {\"page\": 20, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/.claude/sessions/review_reviewer_2_29d69ba3/_pdf_r5_4/main_p20.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 238.7}], \"total_pages\": 27, \"rendered_pages\": 5, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/.claude/sessions/review_reviewer_2_29d69ba3/_pdf_r5_4\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 904
}
```

</details>

---


### Tool call

_source line 396 · 2026-05-22T08:09:21.657407+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/main.pdf",
  "project": "importance_margin_vla_compress",
  "pages": "21-27",
  "dpi": "150",
  "output_dir": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/.claude/sessions/review_reviewer_2_29d69ba3/_pdf_r5_5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/main.pdf",
    "project": "importance_margin_vla_compress",
    "pages": "21-27",
    "dpi": "150",
    "output_dir": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/.claude/sessions/review_reviewer_2_29d69ba3/_pdf_r5_5"
  }
}
```

</details>

---


### Tool result

_source line 397 · 2026-05-22T08:09:22.363480+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 21, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/.claude/sessions/review_reviewer_2_29d69ba3/_pdf_r5_5/main_p21.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 257.9}, {\"page\": 22, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/.claude/sessions/review_reviewer_2_29d69ba3/_pdf_r5_5/main_p22.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 214.2}, {\"page\": 23, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/.claude/sessions/review_reviewer_2_29d69ba3/_pdf_r5_5/main_p23.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 371.9}, {\"page\": 24, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/.claude/sessions/review_reviewer_2_29d69ba3/_pdf_r5_5/main_p24.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 378.8}, {\"page\": 25, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/.claude/sessions/review_reviewer_2_29d69ba3/_pdf_r5_5/main_p25.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 338.2}, {\"page\": 26, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/.claude/sessions/review_reviewer_2_29d69ba3/_pdf_r5_5/main_p26.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 302.2}, {\"page\": 27, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/.claude/sessions/review_reviewer_2_29d69ba3/_pdf_r5_5/main_p27.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 119.4}], \"total_pages\": 27, \"rendered_pages\": 7, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/.claude/sessions/review_reviewer_2_29d69ba3/_pdf_r5_5\"}, \"error\": 
…[truncated 25 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 706
}
```

</details>

---


### Tool call

_source line 398 · 2026-05-22T08:09:26.332157+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/.claude/sessions/review_reviewer_2_29d69ba3/_pdf_r5_3/main_p11.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/.claude/sessions/review_reviewer_2_29d69ba3/_pdf_r5_3/main_p11.png"
  }
}
```

</details>

---


### Tool result

_source line 399 · 2026-05-22T08:09:27.240086+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 907
}
```

</details>

---


### Tool call

_source line 400 · 2026-05-22T08:09:27.242122+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/.claude/sessions/review_reviewer_2_29d69ba3/_pdf_r5_3/main_p12.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/.claude/sessions/review_reviewer_2_29d69ba3/_pdf_r5_3/main_p12.png"
  }
}
```

</details>

---


### Tool result

_source line 401 · 2026-05-22T08:09:28.201820+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 959
}
```

</details>

---


### Tool call

_source line 402 · 2026-05-22T08:09:28.202369+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/.claude/sessions/review_reviewer_2_29d69ba3/_pdf_r5_3/main_p14.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/.claude/sessions/review_reviewer_2_29d69ba3/_pdf_r5_3/main_p14.png"
  }
}
```

</details>

---


### Tool result

_source line 403 · 2026-05-22T08:09:28.659089+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 456
}
```

</details>

---


### Tool call

_source line 404 · 2026-05-22T08:09:28.659549+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/.claude/sessions/review_reviewer_2_29d69ba3/_pdf_r5_4/main_p19.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/.claude/sessions/review_reviewer_2_29d69ba3/_pdf_r5_4/main_p19.png"
  }
}
```

</details>

---


### Tool result

_source line 405 · 2026-05-22T08:09:29.623980+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 964
}
```

</details>

---


### Tool call

_source line 406 · 2026-05-22T08:09:29.624753+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/.claude/sessions/review_reviewer_2_29d69ba3/_pdf_r5_4/main_p20.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/.claude/sessions/review_reviewer_2_29d69ba3/_pdf_r5_4/main_p20.png"
  }
}
```

</details>

---


### Tool call

_source line 407 · 2026-05-22T08:09:30.079469+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/.claude/sessions/review_reviewer_2_29d69ba3/_pdf_r5_5/main_p25.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/.claude/sessions/review_reviewer_2_29d69ba3/_pdf_r5_5/main_p25.png"
  }
}
```

</details>

---


### Tool result

_source line 408 · 2026-05-22T08:09:31.014582+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1389
}
```

</details>

---


### Tool result

_source line 409 · 2026-05-22T08:09:31.022868+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 943
}
```

</details>

---


### Tool call

_source line 410 · 2026-05-22T08:09:31.025711+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/.claude/sessions/review_reviewer_2_29d69ba3/_pdf_r5_5/main_p26.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/.claude/sessions/review_reviewer_2_29d69ba3/_pdf_r5_5/main_p26.png"
  }
}
```

</details>

---


### Tool call

_source line 411 · 2026-05-22T08:09:31.509279+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/.claude/sessions/review_reviewer_2_29d69ba3/_pdf_r5_5/main_p27.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/.claude/sessions/review_reviewer_2_29d69ba3/_pdf_r5_5/main_p27.png"
  }
}
```

</details>

---


### Tool result

_source line 412 · 2026-05-22T08:09:31.566371+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 57
}
```

</details>

---


### Tool result

_source line 413 · 2026-05-22T08:09:31.771507+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 745
}
```

</details>

---


### Tool call

_source line 414 · 2026-05-22T08:11:29.410629+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/.claude/sessions/review_reviewer_2_29d69ba3/_pdf_r5_4/main_p16.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/.claude/sessions/review_reviewer_2_29d69ba3/_pdf_r5_4/main_p16.png"
  }
}
```

</details>

---


### Tool call

_source line 415 · 2026-05-22T08:11:29.762191+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/.claude/sessions/review_reviewer_2_29d69ba3/_pdf_r5_4/main_p17.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/.claude/sessions/review_reviewer_2_29d69ba3/_pdf_r5_4/main_p17.png"
  }
}
```

</details>

---


### Tool result

_source line 416 · 2026-05-22T08:11:30.666938+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1256
}
```

</details>

---


### Tool result

_source line 417 · 2026-05-22T08:11:30.669320+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 907
}
```

</details>

---


### Tool call

_source line 418 · 2026-05-22T08:11:30.669724+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/.claude/sessions/review_reviewer_2_29d69ba3/_pdf_r5_5/main_p21.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/.claude/sessions/review_reviewer_2_29d69ba3/_pdf_r5_5/main_p21.png"
  }
}
```

</details>

---


### Tool result

_source line 419 · 2026-05-22T08:11:31.625565+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 955
}
```

</details>

---


### Tool call

_source line 420 · 2026-05-22T08:11:31.625988+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/.claude/sessions/review_reviewer_2_29d69ba3/_pdf_r5_5/main_p23.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/.claude/sessions/review_reviewer_2_29d69ba3/_pdf_r5_5/main_p23.png"
  }
}
```

</details>

---


### Tool call

_source line 421 · 2026-05-22T08:11:32.027572+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/.claude/sessions/review_reviewer_2_29d69ba3/_pdf_r5_5/main_p24.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/.claude/sessions/review_reviewer_2_29d69ba3/_pdf_r5_5/main_p24.png"
  }
}
```

</details>

---


### Tool result

_source line 422 · 2026-05-22T08:11:32.267299+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 641
}
```

</details>

---


### Tool result

_source line 423 · 2026-05-22T08:11:32.741741+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 714
}
```

</details>

---


### Tool call

_source line 424 · 2026-05-22T08:13:53.937370+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "\n# Reviewer 2 — Round 5 审稿报告\n\n---\n\n## 1. Round 4 Issue 逐条验证\n\n### Must-Fix (Critical)\n\n**R4-N1 [因果声明 under-identified] → [RESOLVED]**\n\n因果语言全文彻底降级，验证如下：\n- **Abstract (p1):** \"The vision connector is **strongly associated** with pruning behavior\" ✓（原 \"determines\"）\n- **Introduction C1 (p2):** \"consistent with the connector being a primary factor, **though confounded by backbone differences** (Appendix N)\" ✓\n- **Figure 1 caption (p2):** \"strongly associated with token compressibility\" ✓\n- **Section 4.5 (p7):** \"This completion interleaves differences in connector, backbone, and encoder fusion, **limiting causal interpretation**\" ✓\n- **Section 5 Limitations (p8):** \"preventing clean causal isolation (Appendix N)\" ✓\n- **Conclusion (p8):** \"Token importance CV **correlates** with both tolerance class and optimal strategy\" ✓\n- **Appendix N (p25):** 新增完整 \"Confounding Analysis\"，逐条讨论 connector / backbone / encoder 混淆、seed 差异、within-connector vs cross-connector 比较的证据强度\n\n全文未发现残留的 \"determines\" 因果语言。降级一致且彻底。\n\n**R4-N2 [Taxonomy N=3 + CV predictor 样本不足] → [RESOLVED]**\n\nClaim 降级充分：\n- CV 从 \"zero-cost dual **predictor**\" 降为 \"zero-cost **diagnostic metric** that **correlates** with\" ✓\n- Contribution C2 (p2): \"Token importance CV **correlates** with both tolerance class and optimal pruning method\" ✓\n- Section 5 Limitations (p8): 明确承认 \"the CV correlation spans **three models** and **two retention ratios**\" ✓\n- Related Work (p3): 新增 Q-Former [25]、Perceiver [32]、Flamingo [26]、RoboFlamingo [8] 作为 cross-attention connector 类别的讨论，并讨论了它们与 taxonomy 的关系 ✓\n- **新增 Appendix K (p23-24):** \"CV as Diagnostic Metric: Extended Analysis\" 扩展讨论了 CV 的连续谱特性以及 X-VLA 作为 intermediate case\n\nTaxonomy 本身仍然是 4 类 / 3 connector 类型，但 claims 已恰当限定。Perceiver/Q-Former 未纳入实验但在 Related Work 中作为 limitation 讨论。\n\n**R4-N3 [纯仿真评估 vs CoRL 要求] → [RESOLVED]**\n\n（Director Round 4 降为 should-fix）\n- Section 5 Limitations (p8): \"All closed-loop experiments use **LIBERO simulation**\" 明确承认 ✓\n- **新增 Section 4.7 Cross-Suite Generalization (p8):** 在 LIBERO-Object 之外验证了 Spatial 和 Goal 两个任务 suite，展示 cliff 行为的 suite 依赖性，部分回应了 generalizability 关切\n- Appendix D (p17): Smart Compress 跨 3 个 suite 的 per-task 结果\n- 未新增 sim-to-real transferability 的专门讨论，但 simulation-only 已作为 limitation 明确列出\n\n考虑到 Director 的降级决定和论文的改善，标记为 resolved。但仍希望 camera-ready 版补充一段 sim-to-real transferability 讨论（即使仅引用他人工作的 sim-to-real 结论）。\n\n### Should-Fix (Warning)\n\n**R4-W1 [\"Falsifies immune assumption\"] → [RESOLVED]**\n\n- 全文搜索未发现 \"falsifies\" 或 \"falsify\"\n- Abstract (p1) 保留了 \"low-CV models are not immune to pruning but uniformly critical\"，但这是描述性表述，不再将 \"immune\" 归因于先前文献的声明\n- Section 4.4 (p6) 改为 \"low CV does not imply tokens are dispensable; it implies uniform criticality\" ✓\n- 稻草人论证问题已解决\n\n**R4-W2 [VTR 新颖性有限] → [RESOLVED]**\n\n- Contribution C3 (p2): \"forms a **diagnostic protocol**\" ✓（原 \"framework\"）\n- Section 4.5 (p7): VTR 定位为实用的 diagnostic tool，不再声称架构新颖性\n- Appendix L (p19): MLP adapter 对照实验保留，evidence 结构合理\n- **Page 27 新增官方 checkpoint 对比：** Smart Compress M=32 达到 60.1±1.3% vs 官方 59.2%（CI [54.8%, 63.4%]），t-test p≈0.72 不显著。论文诚实表述：\"The primary contribution of VTR is recovering functional performance where all deletion methods yield 0%, not matching the official baseline.\" 这是恰当的定位。\n\n**R4-W3 [\"七个模型\" framing 夸大] → [RESOLVED]**\n\n- Table 1 (p5): π₀ 行有明确脚注 \"†π₀ reports offline normalized L1 action loss (pending closed-loop evaluation)\"；CogACT 行有脚注 \"†literature result from EfficientVLA [22], not our evaluation\" ✓\n- Abstract (p1) 仍说 \"seven VLA models\" 但未强调全部为 closed-loop，结合 Table 1 脚注已足够透明\n- Appendix N (p25) 进一步讨论了不同模型的评估协议差异\n\n**R4-W4 [\"Framework\" 过度包装] → [RESOLVED]**\n\n全文 \"framework\" 已替换为 \"diagnostic protocol\"：\n- Abstract (p1): \"forms a diagnostic protocol\" ✓\n- Contribution C3 (p2): \"diagnostic protocol\" ✓\n- Conclusion (p8): 未使用 \"framework\" ✓\n\n**R4-W5 [正文超页] → [RESOLVED]**\n\n- Pages 1-8: 正文（Abstract → Section 6 Conclusion）✓\n- Page 9 起: References\n- Page 12 起: Appendix A-R\n- 符合 CoRL 8 页正文 + 附录/引用不计限制 ✓\n\n---\n\n## 2. 新发现的问题\n\n### 2.1 Section 4.7 Cross-Suite Generalization 评估\n\n**新增贡献：** Section 4.7 (p8) 引入了 hypergeometric cliff model R(N=504, C=r₀, T=46, c) 来形式化 SmolVLA 的 cliff 行为。模型预测 cliff onset 在 k∈[0.899, 0.926]，RMSE=0.025。通过对比 Object (c*=91) vs Spatial (c*=5) 的 concentrated criticality 差异解释了 suite 间的 cliff profile 不同。\n\n**评价：**\n- (+) 将定性的 \"cliff\" 观察提升为定量可测试的假说，是有意义的分析深化\n- (+) Cross-suite validation（Object / Spatial / Goal, Table 9 p17）提供了超出 LIBERO-Object 的 generalization evidence\n- (+) Limitations 中诚实承认 \"hypergeometric cliff model captures onset sharpness (RMSE = 0.025) but does not explain V-shape recovery at k ≤ 0.7\"\n- (−) 模型仅在一个架构（SmolVLA）× 两个 suite 上验证。c* 参数从 5 到 91 的变化范围很大，但仅有 2 个数据点来 \"验证\" 模型的 suite 泛化能力\n- (−) 是否过拟合？4 个参数（N, C, T, c）拟合 2 个 suite 的 cliff profile——参数数量接近数据点数量\n\n**判断：** 不构成新的 must-fix。模型定位恰当（explanatory, 非 predictive），Limitations 承认了局限。但 camera-ready 应明确 c* 是 post-hoc fitted 还是 independently measurable。如果 c* 可以从 attention heatmap 独立计算（Figure 4 暗示可以），那模型就有真正的预测价值；如果是拟合出来的，就只是 curve fitting。\n\n### 2.2 Related Work 扩展程度\n\nRound 4 建议增加 15+ citations。实际增加约 5 篇（41→~46）。但检查后发现：\n- Round 1 已引用了大部分 key works（Compressor-VLA, SpecPrune-VLA, LightVLA, See What Matters, VLA-IAP, EfficientVLA, VLA-Pruner, VLA-Cache, Don't Run with Scissors）\n- 新增的引用补充了 cross-attention connector 和 vision token compression 的覆盖\n- Related Work 段落本身重写/扩展了 concurrent works 讨论（p3），特别是 Don't Run with Scissors 的 \"recover via fine-tuning\" 定位与本文的 \"diagnose connector\" 定位之间的区分\n- **判断：** 覆盖度足够。数量未达 15 篇但 quality 和 relevance 到位。\n\n### 2.3 Positioning 转型评估\n\n从 \"framework paper\" 到 \"diagnostic empirical study\" 的转型整体成功：\n- 所有 overclaiming 语言降级到位\n- Limitations 部分（p8）是我审过的论文中最诚实的之一——明确列出仿真-only、N=3 connector、CV 样本量、π₀ offline-only、hypergeometric 模型局限\n- Appendix N 的 confound analysis 是实质性的分析而非走过场\n- VTR 从 \"novel architecture\" 重新定位为 \"diagnostic tool showing re-encoding overcomes the cliff\"\n\n**残余小问题：** Section 4.4 (p6) \"All tokens carry equal weight, removing any token equals removing all of them\" 是一个未经证明的强声明。CV≈0.04 说明 importance 近似均匀，但 \"removing any = removing all\" 是逻辑跳跃，应改为 \"near-uniform importance makes the model unable to identify dispensable tokens\"。\n\n### 2.4 标题适配性\n\n标题 \"Why Token Pruning **Crashes** Some Robot Policies but Not Others\" 在 claim 降级后仍然合适：\n- \"Crashes\" 是对 empirical phenomenon 的准确描述（SmolVLA 5% removal → 0% SR，π₀.5 10% removal → ≤5% SR）\n- 副标题 \"Vision Connectors and VLA Token Compressibility\" 不含因果声明\n- 正文不再声称 connector \"determines\" 而是 \"is associated with\"\n- **判断：** 标题可接受，无需修改\n\n---\n\n## 3. Overall Score\n\n### 与 Round 4 对比\n\n| 维度 | Round 4 | Round 5 | 变化理由 |\n|------|---------|---------|--------|\n| Originality | 2/5 | 2.5/5 | Cross-suite generalization + hypergeometric model 增加了分析深度；但 N=3 connector 的基本限制未变 |\n| Quality | 3.5/5 | 4/5 | 因果语言降级、confound analysis (Appendix N)、Limitations 改善显著提升了 methodological rigor |\n| Clarity | 4/5 | 4/5 | 写作质量保持高水平，8 页压缩后结构紧凑 |\n| Significance | 2.5/5 | 3/5 | Cross-suite validation 和官方 checkpoint 对比增强了 practical relevance |\n| Relevance | 3/5 | 3/5 | 仍为 simulation-only，但已明确承认 |\n| Limitations | 3/5 | 4.5/5 | Limitations section 现在是典范级别的诚实——逐条列出所有已知局限 |\n\n### Overall Score: **Borderline** (leaning weak accept)\n### Confidence: **High**\n\n**与 Round 4 对比：Weak Reject → Borderline，上调一档。**\n\n**理由：** 论文在五个 round 中展现了出色的迭代改进能力。Round 4 的所有 must-fix 和 should-fix issues 均已 resolved。核心改善：\n\n1. **诚实的定位：** 从 overclaiming \"framework\" + \"determines\" 转型为恰当 scoped 的 \"diagnostic empirical study\" + \"associated with\"\n2. **新增分析深度：** Section 4.7 cross-suite generalization + hypergeometric cliff model 提供了超越 descriptive observation 的 analytical contribution\n3. **Confound transparency：** Appendix N 是实质性的方法论贡献，而非敷衍的 caveat\n\n**仍然存在的 fundamental limitations（不阻碍接收但限制 impact）：**\n- N=3 connector 类型仍然是核心瓶颈——在 rebuttal 或 camera-ready 中增加 Perceiver-based VLA 将显著增强说服力\n- Simulation-only 仍是 CoRL venue fit 的短板，但论文定位为 \"diagnostic analysis\" 而非 \"system deployment\"，部分缓解了此问题\n- VTR 贡献仍然 incremental，但定位已诚实\n\n**给 AC 的建议：** 如果需要在 borderline 论文中做取舍，本文的优势在于：(1) 覆盖广度（7 models, 3 connectors, 3 suites）在该领域无出其右，(2) negative results（linear projection 不可 prune）有高实用价值，(3) Limitations 的诚实度高于平均水平。劣势在于 simulation-only 和 N=3 的 inherent limitation。\n",
  "reviewer_id": "2",
  "project": "importance_margin_vla_compress"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "\n# Reviewer 2 — Round 5 审稿报告\n\n---\n\n## 1. Round 4 Issue 逐条验证\n\n### Must-Fix (Critical)\n\n**R4-N1 [因果声明 under-identified] → [RESOLVED]**\n\n因果语言全文彻底降级，验证如下：\n- **Abstract (p1):** \"The vision connector is **strongly associated** with pruning behavior\" ✓（原 \"determines\"）\n- **Introduction C1 (p2):** \"consistent with the connector being a primary factor, **though confounded by backbone differences** (Appendix N)\" ✓\n- **Figure 1 caption (p2):** \"strongly associated with token compressibility\" ✓\n- **Section 4.5 (p7):** \"This completion interleaves differences in connector, backbone, and encoder fusion, **limiting causal interpretation**\" ✓\n- **Section 5 Limitations (p8):** \"preventing clean causal isolation (Appendix N)\" ✓\n- **Conclusion (p8):** \"Token importance CV **correlates** with both tolerance class and optimal strategy\" ✓\n- **Appendix N (p25):** 新增完整 \"Confounding Analysis\"，逐条讨论 connector / backbone / encoder 混淆、seed 差异、within-connector vs cross-connector 比较的证据强度\n\n全文未发现残留的 \"determines\" 因果语言。降级一致且彻底。\n\n**R4-N2 [Taxonomy N=3 + CV predictor 样本不足] → [RESOLVED]**\n\nClaim 降级充分：\n- CV 从 \"zero-cost dual **predictor**\" 降为 \"zero-cost **diagnostic metric** that **correlates** with\" ✓\n- Contribution C2 (p2): \"Token importance CV **correlates** with both tolerance class and optimal pruning method\" ✓\n- Section 5 Limitations (p8): 明确承认 \"the CV correlation spans **three models** and **two retention ratios**\" ✓\n- Related Work (p3): 新增 Q-Former [25]、Perceiver [32]、Flamingo [26]、RoboFlamingo [8] 作为 cross-attention connector 类别的讨论，并讨论了它们与 taxonomy 的关系 ✓\n- **新增 Appendix K (p23-24):** \"CV as Diagnostic Metric: Extended Analysis\" 扩展讨论了 CV 的连续谱特性以及 X-VLA 作为 intermediate case\n\nTaxonomy 本身仍然是 4 类 / 3 connector 类型，但 claims 已恰当限定。Perceiver/Q-Former 未纳入实验但在 Related Work 中作为 limitation 讨论。\n\n**R4-N3 [纯仿真评估 vs CoRL 要求] → [RESOLVED]**\n\n（Director Round 4 降为 should-fix）\n- Section 5 Limitations (p8): \"All closed-loop experiments use **LIBERO simulation**\" 明确承认 ✓\n- **新增 Section 4.7 Cross-Suite Generalization (p8):** 在 LIBERO-Object 之外验证了 Spatial 和 Goal 两个任务 suite，展示 cliff 行为的 suite 依赖性，部分回应了 generalizability 关切\n- Appendix D (p17): Smart Compress 跨 3 个 suite 的 per-task 结果\n- 未新增 sim-to-real transferability 的专门讨论，但 simulation-only 已作为 limitation 明确列出\n\n考虑到 Director 的降级决定和论文的改善，标记为 resolved。但仍希望 camera-ready 版补充一段 sim-to-real transferability 讨论（即使仅引用他人工作的 sim-to-real 结论）。\n\n### Should-Fix (Warning)\n\n**R4-W1 [\"Falsifies immune assumption\"] → [RESOLVED]**\n\n- 全文搜索未发现 \"falsifies\" 或 \"falsify\"\n- Abstract (p1) 保留了 \"low-CV models are not immune to pruning but uniformly critical\"，但这是描述性表述，不再将 \"immune\" 归因于先前文献的声明\n- Section 4.4 (p6) 改为 \"low CV does not imply tokens are dispensable; it implies uniform criticality\" ✓\n- 稻草人论证问题已解决\n\n**R4-W2 [VTR 新颖性有限] → [RESOLVED]**\n\n- Contribution C3 (p2): \"forms a **diagnostic protocol**\" ✓（原 \"framework\"）\n- Section 4.5 (p7): VTR 定位为实用的 diagnostic tool，不再声称架构新颖性\n- Appendix L (p19): MLP adapter 对照实验保留，evidence 结构合理\n- **Page 27 新增官方 checkpoint 对比：** Smart Compress M=32 达到 60.1±1.3% vs 官方 59.2%（CI [54.8%, 63.4%]），t-test p≈0.72 不显著。论文诚实表述：\"The primary contribution of VTR is recovering functional performance where all deletion methods yield 0%, not matching the official baseline.\" 这是恰当的定位。\n\n**R4-W3 [\"七个模型\" framing 夸大] → [RESOLVED]**\n\n- Table 1 (p5): π₀ 行有明确脚注 \"†π₀ reports offline normalized L1 action loss (pending closed-loop evaluation)\"；CogACT 行有脚注 \"†literature result from EfficientVLA [22], not our evaluation\" ✓\n- Abstract (p1) 仍说 \"seven VLA models\" 但未强调全部为 closed-loop，结合 Table 1 脚注已足够透明\n- Appendix N (p25) 进一步讨论了不同模型的评估协议差异\n\n**R4-W4 [\"Framework\" 过度包装] → [RESOLVED]**\n\n全文 \"framework\" 已替换为 \"diagnostic protocol\"：\n- Abstract (p1): \"forms a diagnostic protocol\" ✓\n- Contribution C3 (p2): \"diagnostic protocol\" ✓\n- Conclusion (p8): 未使用 \"framework\" ✓\n\n**R4-W5 [正文超页] → [RESOLVED]**\n\n- Pages 1-8: 正文（Abstract → Section 6 Conclusion）✓\n- Page 9 起: References\n- Page 12 起: Appendix A-R\n- 符合 CoRL 8 页正文 + 附录/引用不计限制 ✓\n\n---\n\n## 2. 新发现的问题\n\n### 2.1 Section 4.7 Cross-Suite Generalization 评估\n\n**新增贡献：** Section 4.7 (p8) 引入了 hypergeometric cliff model R(N=504, C=r₀, T=46, c) 来形式化 SmolVLA 的 cliff 行为。模型预测 cliff onset 在 k∈[0.899, 0.926]，RMSE=0.025。通过对比 Object (c*=91) vs Spatial (c*=5) 的 concentrated criticality 差异解释了 suite 间的 cliff profile 不同。\n\n**评价：**\n- (+) 将定性的 \"cliff\" 观察提升为定量可测试的假说，是有意义的分析深化\n- (+) Cross-suite validation（Object / Spatial / Goal, Table 9 p17）提供了超出 LIBERO-Object 的 generalization evidence\n- (+) Limitations 中诚实承认 \"hypergeometric cliff model captures onset sharpness (RMSE = 0.025) but does not explain V-shape recovery at k ≤ 0.7\"\n- (−) 模型仅在一个架构（SmolVLA）× 两个 suite 上验证。c* 参数从 5 到 91 的变化范围很大，但仅有 2 个数据点来 \"验证\" 模型的 suite 泛化能力\n- (−) 是否过拟合？4 个参数（N, C, T, c）拟合 2 个 suite 的 cliff profile——参数数量接近数据点数量\n\n**判断：** 不构成新的 must-fix。模型定位恰当（explanatory, 非 predictive），Limitations 承认了局限。但 camera-ready 应明确 c* 是 post-hoc fitted 还是 independently measurable。如果 c* 可以从 attention heatmap 独立计算（Figure 4 暗示可以），那模型就有真正的预测价值；如果是拟合出来的，就只是 curve fitting。\n\n### 2.2 Related Work 扩展程度\n\nRound 4 建议增加 15+ citations。实际增加约 5 篇（41→~46）。但检查后发现：\n- Round 1 已引用了大部分 key works（Compressor-VLA, SpecPrune-VLA, LightVLA, See What Matters, VLA-IAP, EfficientVLA, VLA-Pruner, VLA-Cache, Don't Run with Scissors）\n- 新增的引用补充了 cross-attention connector 和 vision token compression 的覆盖\n- Related Work 段落本身重写/扩展了 concurrent works 讨论（p3），特别是 Don't Run with Scissors 的 \"recover via fine-tuning\" 定位与本文的 \"diagnose connector\" 定位之间的区分\n- **判断：** 覆盖度足够。数量未达 15 篇但 quality 和 relevance 到位。\n\n### 2.3 Positioning 转型评估\n\n从 \"framework paper\" 到 \"diagnostic empirical study\" 的转型整体成功：\n- 所有 overclaiming 语言降级到位\n- Limitations 部分（p8）是我审过的论文中最诚实的之一——明确列出仿真-only、N=3 connector、CV 样本量、π₀ offline-only、hypergeometric 模型局限\n- Appendix N 的 confound analysis 是实质性的分析而非走过场\n- VTR 从 \"novel architecture\" 重新定位为 \"diagnostic tool showing re-encoding overcomes the cliff\"\n\n**残余小问题：** Section 4.4 (p6) \"All tokens carry equal weight, removing any token equals removing all of them\" 是一个未经证明的强声明。CV≈0.04 说明 importance 近似均匀，但 \"removing any = removing all\" 是逻辑跳跃，应改为 \"near-uniform importance makes the model unable to identify dispensable tokens\"。\n\n### 2.4 标题适配性\n\n标题 \"Why Token Pruning **Crashes** Some Robot Policies but Not Others\" 在 claim 降级后仍然合适：\n- \"Crashes\" 是对 empirical phenomenon 的准确描述（SmolVLA 5% removal → 0% SR，π₀.5 10% removal → ≤5% SR）\n- 副标题 \"Vision Connectors and VLA Token Compressibility\" 不含因果声明\n- 正文不再声称 connector \"determines\" 而是 \"is associated with\"\n- **判断：** 标题可接受，无需修改\n\n---\n\n## 3. Overall Score\n\n### 与 Round 4 对比\n\n| 维度 | Round 4 | Round 5 | 变化理由 |\n|------|---------|---------|--------|\n| Originality | 2/5 | 2.5/5 | Cross-suite generalization + hypergeometric model 增加了分析深度；但 N=3 connector 的基本限制未变 |\n| Quality | 3.5/5 | 4/5 | 因果语言降级、confound analysis (Appendix N)、Limitations 改善显著提升了 methodological rigor |\n| Clarity | 4/5 | 4/5 | 写作质量保持高水平，8 页压缩后结构紧凑 |\n| Significance | 2.5/5 | 3/5 | Cross-suite validation 和官方 checkpoint 对比增强了 practical relevance |\n| Relevance | 3/5 | 3/5 | 仍为 simulation-only，但已明确承认 |\n| Limitations | 3/5 | 4.5/5 | Limitations section 现在是典范级别的诚实——逐条列出所有已知局限 |\n\n### Overall Score: **Borderline** (leaning weak accept)\n### Confidence: **High**\n\n**与 Round 4 对比：Weak Reject → Borderline，上调一档。**\n\n**理由：** 论文在五个 round 中展现了出色的迭代改进能力。Round 4 的所有 must-fix 和 should-fix issues 均已 resolved。核心改善：\n\n1. **诚实的定位：** 从 overclaiming \"framework\" + \"determines\" 转型为恰当 scoped 的 \"diagnostic empirical study\" + \"associated with\"\n2. **新增分析深度：** Section 4.7 cross-suite generalization + hypergeometric cliff model 提供了超越 descriptive observation 的 analytical contribution\n3. **Confound transparency：** Appendix N 是实质性的方法论贡献，而非敷衍的 caveat\n\n**仍然存在的 fundamental limitations（不阻碍接收但限制 impact）：**\n- N=3 connector 类型仍然是核心瓶颈——在 rebuttal 或 camera-ready 中增加 Perceiver-based VLA 将显著增强说服力\n- Simulation-only 仍是 CoRL venue fit 的短板，但论文定位为 \"diagnostic analysis\" 而非 \"system deployment\"，部分缓解了此问题\n- VTR 贡献仍然 incremental，但定位已诚实\n\n**给 AC 的建议：** 如果需要在 borderline 论文中做取舍，本文的优势在于：(1) 覆盖广度（7 models, 3 connectors, 3 suites）在该领域无出其右，(2) negative results（linear projection 不可 prune）有高实用价值，(3) Limitations 的诚实度高于平均水平。劣势在于 simulation-only 和 N=3 的 inherent limitation。\n",
    "reviewer_id": "2",
    "project": "importance_margin_vla_compress"
  }
}
```

</details>

---


### Tool result

_source line 425 · 2026-05-22T08:13:58.358757+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4421
}
```

</details>

---


### Tool call

_source line 426 · 2026-05-22T08:14:04.653743+00:00_

called mcp__agent-ml-research__cleanup_pdf_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__cleanup_pdf_images</summary>

```json
{
  "output_dir": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/.claude/sessions/review_reviewer_2_29d69ba3/_pdf_r5_1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "tool_args": {
    "output_dir": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/.claude/sessions/review_reviewer_2_29d69ba3/_pdf_r5_1"
  }
}
```

</details>

---


### Tool result

_source line 427 · 2026-05-22T08:14:04.754466+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"安全限制：只能清理 _pdf_images 目录，当前目标: _pdf_r5_1\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "elapsed_ms": 100
}
```

</details>

---


### Assistant

_source line 428 · 2026-05-22T08:14:12.640415+00:00_

Round 5 审稿完成。

**核心结论：** Round 4 的 6 个 must-fix/should-fix issues 全部 **[RESOLVED]**。因果语言降级彻底（"determines"→"strongly associated with"），CV 定位从 "predictor" 降为 "diagnostic metric that correlates with"，"framework" 替换为 "diagnostic protocol"，正文压缩至 8 页，新增 confound analysis（Appendix N）和 cross-suite generalization（Section 4.7）。

评分从 **Weak Reject → Borderline (leaning weak accept)**，上调一档。论文展现了出色的迭代改进能力和少见的 Limitations 诚实度。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2"
}
```

</details>

---


## Round 10

## Round 10

4 recorded events


### User

_source line 429 · 2026-05-22T08:14:54.009079+00:00_

[Round 5 审稿请求]:
# 交叉分享：Reviewer 1 的 Round 5 审稿意见

请逐条回应 Reviewer 1 的新发现，使用 [AGREE] 或 [REBUT] 标记。

---

## R1 新发现摘要

**R1-NEW-1 [warning] π₀.5 非单调 cliff**
- π₀.5 在 LIBERO-Object 上：k=0.95 (69.4%) → k=0.85 (5.0%) → k=0.7 (77.2%)，72pp swing
- hypergeometric model 预测移除更多 token 时击中 critical token 概率只会更高，无法解释 k=0.7 恢复
- Section 5 承认 "does not explain V-shape recovery at k≤0.7" 但不够充分
- 建议：(a) 正文 Section 4.7 增加模型适用边界说明；(b) 讨论 k=0.7 恢复的可能机制

**R1-NEW-2 [minor] SmolVLA baseline 数字不一致**
- Section 4.2: "57.2% SR"，Table 2: "59.2% baseline"，Appendix Table 3: 两个协议（59.2% / 57.2%）
- 建议首次提及时写 "57.2%–59.2% across two evaluation protocols"

**R1-NEW-3 [minor] Discussion 过度压缩**
- 从 ~3 页压缩为 2 段（~10 行），旧版 mechanistic insights 完全消失
- 建议增加一句引导到 Appendix J 的 pointer

**R1-NEW-4 [minor] C=91 参数来源不明**
- hypergeometric model 的 C=91 critical tokens 是 post-hoc 拟合还是独立测量？
- 建议在 Appendix C.8 明确确定方法

**R1 评分：Weak Accept，从 Borderline (weak reject) 上调。**

---

请对比你自己的 Round 5 发现，对 R1 的每个观点给出 [AGREE] 或 [REBUT]，特别关注：
1. R1-NEW-1 的 V-shape recovery 问题——你是否同意这比你的 "c* 过拟合" 担忧更严重？
2. R1-NEW-2 baseline 不一致——你是否注意到同一问题？
3. R1-NEW-4 与你的 R2-2.1 是否指向同一根本问题（C/c* 参数的确定方法）？
4. 两人评分差异（R1 Weak Accept vs 你 Borderline leaning weak accept）——你是否调整评分？

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 430 · 2026-05-22T08:16:25.247034+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "\n# Reviewer 2 交叉回应 Reviewer 1 Round 5 新发现\n\n---\n\n## 逐条回应\n\n**[AGREE] R1-NEW-1: π₀.5 非单调 V-shape recovery (k=0.95→69.4%, k=0.85→5.0%, k=0.7→77.2%)**\n\n强烈同意，且认为这比我自己提出的 \"c* 过拟合\" 担忧更严重。理由：\n\n1. **问题层次不同。** 我的 R2-2.1 关注的是 hypergeometric model 的统计效力（4 参数拟合 2 个 suite），这是 model validation 问题。R1-NEW-1 指出的是模型的 **explanatory scope** 缺陷——一个 monotonic collapse probability 模型在逻辑上就无法解释非单调恢复。这是结构性的，不是样本量可以解决的。\n\n2. **72pp swing 是一个值得独立讨论的经验现象。** π₀.5 在 k=0.85 崩溃到 5% 但在 k=0.7 恢复到 77.2%，这暗示存在某种 regime transition——可能在极端压缩下模型 \"放弃\" 视觉信息转而依赖语言/proprioception prior，或者 L2 ranking 在不同 k 值下的 effective selection pattern 发生质变（例如极端压缩下 L2 选出的 token subset 反而覆盖了更多 unique spatial regions）。论文 Section 5 Limitations 一句带过 \"does not explain V-shape recovery at k ≤ 0.7\" 确实不够。\n\n3. **对 actionability 的影响。** 如果 practitioner 按照 CV diagnostic protocol 指导在 k=0.85 处 prune π₀.5，会得到 5% SR；但继续 prune 到 k=0.7 反而可用。这种非单调性直接削弱了 \"CV correlates with optimal strategy\" 的实用性——因为最优 k 值不是从 CV 单调推导的。\n\n**建议：** Section 4.7 应增加 1-2 句明确 hypergeometric model 的适用边界（\"valid for cliff onset prediction near the critical threshold; does not model recovery regimes\"），并在 Section 4.4 或 Appendix 讨论 V-shape 的可能机制（即使是 speculative 也比沉默好）。\n\n**[AGREE] R1-NEW-2: SmolVLA baseline 数字不一致 (57.2% vs 59.2%)**\n\n我在 Round 5 审稿中未单独标记这个问题，是我的疏漏。Section 4.2 的 \"57.2%\" 与 Table 2 的 \"59.2% baseline\" 之间的差异如果来自不同评估协议（例如不同 seed、不同 episode 数、不同 LIBERO 版本），应在首次提及时明确说明。R1 建议的 \"57.2%–59.2% across two evaluation protocols\" 是清晰且低成本的修复。\n\n同时，这类看似小的数字不一致在 peer review 中容易引发 \"数据管理不严\" 的信任疑虑——特别是当论文的核心贡献是 quantitative comparison 时。Camera-ready 必须统一。\n\n**[AGREE] R1-NEW-3: Discussion 过度压缩**\n\n同意这是 8 页压缩的一个代价。旧版 Section 5 约 3 页（pages 11-13），包含 connector mechanism 的 mechanistic interpretation、CV 的连续谱讨论、re-encoding 成功的原因分析。现在压缩为 2 段约 10 行，这些 insight 完全消失于正文。\n\n论文已将相关内容移入 Appendix J-K，但正文没有显式指引。增加一句 \"For extended mechanistic analysis, see Appendices J–K\" 是零成本的改善。\n\n**[AGREE] R1-NEW-4: C=91 参数来源不明**\n\n完全同意，且这与我 R2-2.1 中 \"camera-ready 应明确 c* 是 post-hoc fitted 还是 independently measurable\" 的关注是**同一根本问题的两种表述**。\n\nR1 问的是 \"C=91 是拟合还是独立测量\"，我问的是 \"c* 能否从 attention heatmap 独立计算\"。本质上：如果 c* 可以从 Figure 4 的 attention heatmap 独立量化（例如定义一个 threshold 计算 \"concentrated critical tokens\" 的数量），那 hypergeometric model 就有独立的预测价值；如果 c* 是通过最小化 RMSE 从 collapse curve 反向拟合的，那模型就退化为 curve fitting，没有独立验证。\n\n两位 reviewer 独立收敛于同一问题，说明这是论文应在 camera-ready 中优先 clarify 的点。\n\n---\n\n## 评分差异讨论\n\n**R1: Weak Accept | R2 (我): Borderline (leaning weak accept)**\n\n两人均从 Round 4 上调一档，方向一致。半档差异来源：\n\n1. **我对 N=3 connector 的 inherent limitation 权重略高。** Taxonomy 和 CV diagnostic 是论文的两个核心 contribution，都建立在 3 个 connector 类型上。即使 claim 降级到位，这个 sample size 对 CoRL reviewer 来说仍是一个可预见的批评点。R1 似乎认为 claim 降级充分弥补了这一点；我认为降级是必要条件但非充分条件。\n\n2. **Simulation-only 的 venue fit 权重。** R1 升至 weak accept 暗示认为 CoRL 可以接受 simulation-only 的 diagnostic study；我对此稍保守——CoRL CFP 明确要求 \"real-robot experiments or convincing evidence that simulation experiments are transferable to real robots\"，论文未提供 transferability evidence。\n\n3. **VTR 贡献的评估。** 我们一致认为 VTR incremental 但定位诚实。但 VTR 的 t-test p≈0.72（vs 官方 checkpoint）意味着恢复效果与官方 baseline 无统计差异——这既是优点（\"能恢复到 baseline 水平\"）也是弱点（\"没有实质提升\"）。\n\n**是否调整评分：** 不调整。我维持 **Borderline (leaning weak accept)**。与 R1 的半档差异反映了对 simulation-only venue fit 和 N=3 limitation 的合理不同权重。两人的实质判断一致：论文在 intensive revision 后达到了 borderline acceptable 的水平，所有 overclaiming 已修复，remaining limitations 是 inherent 的而非 sloppy 的。\n\n**给 AC 的建议保持不变：** 如果 conference 需要在 borderline 论文中取舍，本文的核心价值在于 (1) 跨架构覆盖的广度无出其右，(2) negative results 有高实用价值，(3) Limitations 的诚实度高于平均水平。主要 risk 是 CoRL audience 可能期望 real-robot validation。\n",
  "reviewer_id": "2",
  "project": "importance_margin_vla_compress"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "\n# Reviewer 2 交叉回应 Reviewer 1 Round 5 新发现\n\n---\n\n## 逐条回应\n\n**[AGREE] R1-NEW-1: π₀.5 非单调 V-shape recovery (k=0.95→69.4%, k=0.85→5.0%, k=0.7→77.2%)**\n\n强烈同意，且认为这比我自己提出的 \"c* 过拟合\" 担忧更严重。理由：\n\n1. **问题层次不同。** 我的 R2-2.1 关注的是 hypergeometric model 的统计效力（4 参数拟合 2 个 suite），这是 model validation 问题。R1-NEW-1 指出的是模型的 **explanatory scope** 缺陷——一个 monotonic collapse probability 模型在逻辑上就无法解释非单调恢复。这是结构性的，不是样本量可以解决的。\n\n2. **72pp swing 是一个值得独立讨论的经验现象。** π₀.5 在 k=0.85 崩溃到 5% 但在 k=0.7 恢复到 77.2%，这暗示存在某种 regime transition——可能在极端压缩下模型 \"放弃\" 视觉信息转而依赖语言/proprioception prior，或者 L2 ranking 在不同 k 值下的 effective selection pattern 发生质变（例如极端压缩下 L2 选出的 token subset 反而覆盖了更多 unique spatial regions）。论文 Section 5 Limitations 一句带过 \"does not explain V-shape recovery at k ≤ 0.7\" 确实不够。\n\n3. **对 actionability 的影响。** 如果 practitioner 按照 CV diagnostic protocol 指导在 k=0.85 处 prune π₀.5，会得到 5% SR；但继续 prune 到 k=0.7 反而可用。这种非单调性直接削弱了 \"CV correlates with optimal strategy\" 的实用性——因为最优 k 值不是从 CV 单调推导的。\n\n**建议：** Section 4.7 应增加 1-2 句明确 hypergeometric model 的适用边界（\"valid for cliff onset prediction near the critical threshold; does not model recovery regimes\"），并在 Section 4.4 或 Appendix 讨论 V-shape 的可能机制（即使是 speculative 也比沉默好）。\n\n**[AGREE] R1-NEW-2: SmolVLA baseline 数字不一致 (57.2% vs 59.2%)**\n\n我在 Round 5 审稿中未单独标记这个问题，是我的疏漏。Section 4.2 的 \"57.2%\" 与 Table 2 的 \"59.2% baseline\" 之间的差异如果来自不同评估协议（例如不同 seed、不同 episode 数、不同 LIBERO 版本），应在首次提及时明确说明。R1 建议的 \"57.2%–59.2% across two evaluation protocols\" 是清晰且低成本的修复。\n\n同时，这类看似小的数字不一致在 peer review 中容易引发 \"数据管理不严\" 的信任疑虑——特别是当论文的核心贡献是 quantitative comparison 时。Camera-ready 必须统一。\n\n**[AGREE] R1-NEW-3: Discussion 过度压缩**\n\n同意这是 8 页压缩的一个代价。旧版 Section 5 约 3 页（pages 11-13），包含 connector mechanism 的 mechanistic interpretation、CV 的连续谱讨论、re-encoding 成功的原因分析。现在压缩为 2 段约 10 行，这些 insight 完全消失于正文。\n\n论文已将相关内容移入 Appendix J-K，但正文没有显式指引。增加一句 \"For extended mechanistic analysis, see Appendices J–K\" 是零成本的改善。\n\n**[AGREE] R1-NEW-4: C=91 参数来源不明**\n\n完全同意，且这与我 R2-2.1 中 \"camera-ready 应明确 c* 是 post-hoc fitted 还是 independently measurable\" 的关注是**同一根本问题的两种表述**。\n\nR1 问的是 \"C=91 是拟合还是独立测量\"，我问的是 \"c* 能否从 attention heatmap 独立计算\"。本质上：如果 c* 可以从 Figure 4 的 attention heatmap 独立量化（例如定义一个 threshold 计算 \"concentrated critical tokens\" 的数量），那 hypergeometric model 就有独立的预测价值；如果 c* 是通过最小化 RMSE 从 collapse curve 反向拟合的，那模型就退化为 curve fitting，没有独立验证。\n\n两位 reviewer 独立收敛于同一问题，说明这是论文应在 camera-ready 中优先 clarify 的点。\n\n---\n\n## 评分差异讨论\n\n**R1: Weak Accept | R2 (我): Borderline (leaning weak accept)**\n\n两人均从 Round 4 上调一档，方向一致。半档差异来源：\n\n1. **我对 N=3 connector 的 inherent limitation 权重略高。** Taxonomy 和 CV diagnostic 是论文的两个核心 contribution，都建立在 3 个 connector 类型上。即使 claim 降级到位，这个 sample size 对 CoRL reviewer 来说仍是一个可预见的批评点。R1 似乎认为 claim 降级充分弥补了这一点；我认为降级是必要条件但非充分条件。\n\n2. **Simulation-only 的 venue fit 权重。** R1 升至 weak accept 暗示认为 CoRL 可以接受 simulation-only 的 diagnostic study；我对此稍保守——CoRL CFP 明确要求 \"real-robot experiments or convincing evidence that simulation experiments are transferable to real robots\"，论文未提供 transferability evidence。\n\n3. **VTR 贡献的评估。** 我们一致认为 VTR incremental 但定位诚实。但 VTR 的 t-test p≈0.72（vs 官方 checkpoint）意味着恢复效果与官方 baseline 无统计差异——这既是优点（\"能恢复到 baseline 水平\"）也是弱点（\"没有实质提升\"）。\n\n**是否调整评分：** 不调整。我维持 **Borderline (leaning weak accept)**。与 R1 的半档差异反映了对 simulation-only venue fit 和 N=3 limitation 的合理不同权重。两人的实质判断一致：论文在 intensive revision 后达到了 borderline acceptable 的水平，所有 overclaiming 已修复，remaining limitations 是 inherent 的而非 sloppy 的。\n\n**给 AC 的建议保持不变：** 如果 conference 需要在 borderline 论文中取舍，本文的核心价值在于 (1) 跨架构覆盖的广度无出其右，(2) negative results 有高实用价值，(3) Limitations 的诚实度高于平均水平。主要 risk 是 CoRL audience 可能期望 real-robot validation。\n",
    "reviewer_id": "2",
    "project": "importance_margin_vla_compress"
  }
}
```

</details>

---


### Tool result

_source line 431 · 2026-05-22T08:16:29.672315+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4425
}
```

</details>

---


### Assistant

_source line 432 · 2026-05-22T08:16:38.152650+00:00_

Round 5 交叉回应已提交。

核心结论：与 R1 在所有 4 个新发现上达成一致（全部 [AGREE]）。最重要的共识是 R1-NEW-1 的 V-shape recovery 问题——比我自己提出的 c* 过拟合担忧更根本，因为它挑战的是 hypergeometric model 的 explanatory scope 而非统计效力。R1-NEW-4 与我的 R2-2.1 指向同一根本问题（c* 参数确定方法），两位 reviewer 独立收敛。

评分维持 Borderline (leaning weak accept)，不调整。与 R1 (Weak Accept) 的半档差异来自对 simulation-only venue fit 和 N=3 limitation 的权重分配不同，实质判断一致。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2"
}
```

</details>

---


## Round 11

## Round 11

108 recorded events


### User

_source line 433 · 2026-05-23T05:43:49.465889+00:00_

[Round 1 审稿请求]:
你是 Reviewer 2，负责**新颖性、相关工作覆盖和论文定位**的审查。

## 投稿信息
- **Venue**: CoRL 2026（Conference on Robot Learning）
- **Deadline**: 2026-05-29
- **页数限制**: 8 页正文（附录/参考文献不计入）
- **匿名规则**: Double-blind
- **模板**: CoRL 2026 (`\usepackage{corl_2026}`)
- **必须包含**: Limitations section（计入 8 页）

## 论文文件
- LaTeX 源码: `projects/importance_margin_vla_compress/docs/paper/main.tex`
- PDF: `projects/importance_margin_vla_compress/artifacts/review_round_6/submitted.pdf`

## 你的审查侧重

### 1. Novelty 评估
- "Two-axis framework"（connector coupling × task complexity）是否构成真正的 intellectual contribution，还是对已知现象的重新包装？
- CV as diagnostic metric：L2 norm 的 CV 是一个简单的统计量——这是否足以作为一篇 CoRL 论文的核心 contribution？
- VTR：cross-attention re-encoding 已在 Perceiver/Q-Former/BLIP-2 中广泛使用，VTR 的 novelty 在哪里？
- 整篇论文的核心发现"不同 connector 对 pruning 的响应不同"是否过于 obvious？

### 2. 相关工作覆盖
- **Concurrent VLA pruning work**：检查是否遗漏关键 concurrent work。特别关注：
  - "Don't Run with Scissors" (Jabbour et al. 2025) — 已引用，但讨论是否充分？该工作也研究 pruning breaks VLA
  - Compressor-VLA, SpecPrune-VLA, LightVLA, See What Matters (ICML 2026) — 检查引用和对比
  - VLA-Cache, VLA-IAP, EfficientVLA, VLA-Pruner — 已引用
- **Vision connector 相关工作**：TokenPacker, InternVL pixel-shuffle, 其他使用 pixel-shuffle 的 VLM/VLA
- **VLM token pruning**：FastV, PruMerge, SparseVLM, SparseVILA, FitPrune, CrossGET — 检查覆盖
- 是否有重要的 missing references？

### 3. Contribution Claims 合理性
- C1 "two-axis compressibility analysis"：cross-architecture analysis 的 scope 是否与 claim 匹配？只在 LIBERO 上测，只用了 4 个 closed-loop models
- C2 "CV as diagnostic"：声称 "enabling connector-appropriate compression strategy selection without downstream evaluation" 但只有 3 data points 的 correlation
- C3 "VTR recovers pixel-shuffle VLA"：只在 SmolVLA 一个模型上验证，generalization 未知

### 4. 论文定位
- 这篇论文的 primary identity 是什么？empirical study? diagnostic tool? new method?
- 对 CoRL 审稿人来说，这篇论文的 actionable takeaway 是什么？
- 与 "Don't Run with Scissors" 的差异化是否清晰？

### 5. 对 CoRL Community 的价值
- CoRL 读者关心的是 real robot deployment。论文完全基于 LIBERO simulation，这对 CoRL 的价值如何？
- 实用建议的 actionability：CV diagnostic 需要什么信息？practitioner 真的会用它吗？

请提供结构化审稿报告：Summary → Strengths → Weaknesses（按 severity 分 Must-Fix / Should-Fix / Minor） → Questions → Missing References。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 434 · 2026-05-23T05:43:58.945551+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/.claude/skills/review-reviewer-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/.claude/skills/review-reviewer-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 435 · 2026-05-23T05:44:00.302311+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/.claude/sessions/review_reviewer_2_29d69ba3.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1356
}
```

</details>

---


### Tool call

_source line 436 · 2026-05-23T05:44:00.454295+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director,WebSearch,WebFetch",
  "max_results": "4"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director,WebSearch,WebFetch",
    "max_results": "4"
  }
}
```

</details>

---


### Tool result

_source line 437 · 2026-05-23T05:44:00.504875+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 438 · 2026-05-23T05:44:04.679724+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "CoRL 2026 reviewer guidelines review form criteria"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "CoRL 2026 reviewer guidelines review form criteria"
  }
}
```

</details>

---


### Tool call

_source line 439 · 2026-05-23T05:44:07.196075+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/review_round_6/submitted.pdf",
  "project": "importance_margin_vla_compress",
  "pages": "1-10",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/review_round_6/submitted.pdf",
    "project": "importance_margin_vla_compress",
    "pages": "1-10",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 440 · 2026-05-23T05:44:11.092610+00:00_

Web search results for query: "CoRL 2026 reviewer guidelines review form criteria"

Links: [{"title":"CoRL 2026 - Instruction for Authors","url":"https://www.corl.org/contributions/instruction-for-authors"},{"title":"ICLR 2026 Reviewer Guide","url":"https://iclr.cc/Conferences/2026/ReviewerGuide"},{"title":"CoRL 2026 - Call for Papers","url":"https://www.corl.org/contributions/call-for-papers"},{"title":"Reviewer Guidelines — CoRL 2023","url":"https://www.corl2023.org/reviewer-guidelines"},{"title":"CVPR 2026 Reviewer Guidelines","url":"https://cvpr.thecvf.com/Conferences/2026/ReviewerGuidelinesq"},{"title":"Which Coauthor Should I Nominate in My 99 ICLR Submissions? A Mathematical Analysis of the ICLR 2026 Reciprocal Reviewer Nomination Policy","url":"https://arxiv.org/pdf/2512.17950"},{"title":"CoRL 2024 - Instruction for Reviews","url":"https://2024.corl.org/contributions/instruction-for-reviews"}]

Based on the search results, I found information about CoRL 2026 submission requirements and reviewer expectations, though specific 2026 reviewer guidelines appear limited. Here's what I found:

## Reviewer Requirements for CoRL 2026

All submissions must include at least one author who agrees to serve as a CoRL reviewer, and they are qualified if they have at least one accepted publication at a previous robotics (CoRL/ICRA/IROS/RSS) or learning conference (ICLR/NeurIPS/ICML) or equivalent journal. Additionally, every author with 3 or more submissions must agree to serve as a reviewer.

## Review Criteria (from CoRL 2024)

While specific 2026 review form criteria are not fully detailed in the search results, submissions are evaluated based on the significance and novelty of the results, either theoretical or empirical. Key evaluation aspects include: whether the paper addresses a problem in robot learning, applies or improves a learning-based method or learned model, whether the method is evaluated in simulation, on real robots, or both, and whether the CoRL audience 
…[truncated 520 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 6412
}
```

</details>

---


### Tool result

_source line 441 · 2026-05-23T05:44:12.203414+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 1, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/review_round_6/_pdf_images/submitted_p1.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 314.1}, {\"page\": 2, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/review_round_6/_pdf_images/submitted_p2.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 306.5}, {\"page\": 3, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/review_round_6/_pdf_images/submitted_p3.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 334.2}, {\"page\": 4, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/review_round_6/_pdf_images/submitted_p4.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 301.8}, {\"page\": 5, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/review_round_6/_pdf_images/submitted_p5.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 273.9}, {\"page\": 6, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/review_round_6/_pdf_images/submitted_p6.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 414.9}, {\"page\": 7, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/review_round_6/_pdf_images/submitted_p7.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 340.9}, {\"page\": 8, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/review_round_6/_pdf_images/submitted_p8.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 236.3}, {\"page\": 9, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_v
…[truncated 603 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 5007
}
```

</details>

---


### Tool call

_source line 442 · 2026-05-23T05:44:22.072419+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://2024.corl.org/contributions/instruction-for-reviews",
  "prompt": "Extract all review criteria, scoring dimensions, rating scales, and guidelines for reviewers. Include any specific questions reviewers must answer and the rating options available."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://2024.corl.org/contributions/instruction-for-reviews",
    "prompt": "Extract all review criteria, scoring dimensions, rating scales, and guidelines for reviewers. Include any specific questions reviewers must answer and the rating options available."
  }
}
```

</details>

---


### Tool call

_source line 443 · 2026-05-23T05:44:23.281337+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://www.corl2023.org/reviewer-guidelines",
  "prompt": "Extract all review criteria, scoring dimensions, rating scales, and guidelines for reviewers. Include any specific questions reviewers must answer and the rating options."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://www.corl2023.org/reviewer-guidelines",
    "prompt": "Extract all review criteria, scoring dimensions, rating scales, and guidelines for reviewers. Include any specific questions reviewers must answer and the rating options."
  }
}
```

</details>

---


### Tool call

_source line 444 · 2026-05-23T05:44:23.535442+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/review_round_6/_pdf_images/submitted_p1.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/review_round_6/_pdf_images/submitted_p1.png"
  }
}
```

</details>

---


### Tool call

_source line 445 · 2026-05-23T05:44:24.291513+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/review_round_6/_pdf_images/submitted_p2.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/review_round_6/_pdf_images/submitted_p2.png"
  }
}
```

</details>

---


### Tool result

_source line 446 · 2026-05-23T05:44:25.002637+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1467
}
```

</details>

---


### Tool result

_source line 447 · 2026-05-23T05:44:25.005248+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 713
}
```

</details>

---


### Tool call

_source line 448 · 2026-05-23T05:44:25.005645+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/review_round_6/_pdf_images/submitted_p3.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/review_round_6/_pdf_images/submitted_p3.png"
  }
}
```

</details>

---


### Tool result

_source line 449 · 2026-05-23T05:44:25.460486+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 454
}
```

</details>

---


### Tool call

_source line 450 · 2026-05-23T05:44:25.461028+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/review_round_6/_pdf_images/submitted_p4.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/review_round_6/_pdf_images/submitted_p4.png"
  }
}
```

</details>

---


### Tool result

_source line 451 · 2026-05-23T05:44:25.964832+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 503
}
```

</details>

---


### Tool call

_source line 452 · 2026-05-23T05:44:25.965342+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/review_round_6/_pdf_images/submitted_p5.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/review_round_6/_pdf_images/submitted_p5.png"
  }
}
```

</details>

---


### Tool result

_source line 453 · 2026-05-23T05:44:26.369219+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 403
}
```

</details>

---


### Tool result

_source line 454 · 2026-05-23T05:44:26.620614+00:00_

# CoRL 2024 Review Criteria Summary

## Primary Review Criteria for Regular Papers

Submissions are assessed on:
- **Significance and novelty** of results (theoretical or empirical)
- **Objective establishment** of results and potential impact on science/technology
- **Relevance to robotic learning**

The conference welcomes papers combining experimental and theoretical contributions.

## Desk Rejection Criteria

Papers may be rejected before full review for:

1. **Formatting issues** – submissions exceeding length limits or using incorrect formats
2. **Anonymity violations** – manuscripts, supplementary materials, or embedded links revealing author identities
3. **Scope violations** – failure to demonstrate robot learning relevance through either:
   - Explicitly addressing a learning question for physical robots, OR
   - Testing the proposed solution on physical robots

### Scope Examples (Ineligible)

- "Manually design and tune the performance of a robot controller without use of learning"
- Generic machine learning without robotics application
- "Improved performance on a standard CV dataset, e.g., ImageNet recognition"

## Reviewer Qualifications

Reviewers should possess demonstrated expertise through:
- Minimum of 3 first-author publications in major robotics venues (CoRL, RSS, ICRA, IROS, IJRR, TRO, RAL)
- Publications in core machine learning venues (NeurIPS, ICML, AIStats, JMLR, PAMI)

**Note:** The document does not specify numerical rating scales or specific questions reviewers must answer.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 4548
}
```

</details>

---


### Tool result

_source line 455 · 2026-05-23T05:44:33.252718+00:00_

# CoRL 2023 Review Criteria and Guidelines

## Primary Evaluation Dimensions

Reviewers assess submissions across six key criteria:

1. **Originality**: Whether problems/methods are novel, represent creative combinations of known techniques, and differentiate clearly from prior work with adequate citations.

2. **Quality**: Technical soundness, claims supported by theory or experiments, appropriate methodology, completeness, and honest evaluation of strengths and weaknesses.

3. **Clarity**: Clear writing, good organization, adequate reader information, and sufficient detail for expert reproducibility of results.

4. **Significance**: Importance of results, likelihood of adoption by researchers/practitioners, advancement beyond prior work, and theoretical or experimental novelty.

5. **Relevance**: "Does the paper address a problem in robot learning? Does it apply or improve a learning-based method, or a learned model?"

6. **Limitations**: Appreciation for honestly reported limitations; critical attention to unacknowledged shortcomings.

## Key Guidelines

Reviewers must provide **constructive, concrete, courteous feedback** with substantiated claims. The document explicitly warns against common mistakes:

- Claiming lack of novelty without citations
- Suggesting alternatives without evidence
- Making code/dataset/real-robot testing mandatory (not policy)
- Conflating SOTA performance with acceptance worthiness
- Treating single errors as rejection justification

The guidelines emphasize that reviewers should "start with positive aspects" and maintain respectful disagreement throughout the discussion period.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 9971
}
```

</details>

---


### Tool call

_source line 456 · 2026-05-23T05:44:40.299240+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/review_round_6/_pdf_images/submitted_p6.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/review_round_6/_pdf_images/submitted_p6.png"
  }
}
```

</details>

---


### Tool call

_source line 457 · 2026-05-23T05:44:40.501662+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/review_round_6/_pdf_images/submitted_p7.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/review_round_6/_pdf_images/submitted_p7.png"
  }
}
```

</details>

---


### Tool call

_source line 458 · 2026-05-23T05:44:41.260942+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/review_round_6/_pdf_images/submitted_p8.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/review_round_6/_pdf_images/submitted_p8.png"
  }
}
```

</details>

---


### Tool result

_source line 459 · 2026-05-23T05:44:41.665997+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1366
}
```

</details>

---


### Tool result

_source line 460 · 2026-05-23T05:44:41.724398+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1222
}
```

</details>

---


### Tool call

_source line 461 · 2026-05-23T05:44:41.724886+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/review_round_6/_pdf_images/submitted_p9.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/review_round_6/_pdf_images/submitted_p9.png"
  }
}
```

</details>

---


### Tool call

_source line 462 · 2026-05-23T05:44:41.927307+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/review_round_6/_pdf_images/submitted_p10.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/review_round_6/_pdf_images/submitted_p10.png"
  }
}
```

</details>

---


### Tool result

_source line 463 · 2026-05-23T05:44:42.131368+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 870
}
```

</details>

---


### Tool result

_source line 464 · 2026-05-23T05:44:43.141386+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1416
}
```

</details>

---


### Tool result

_source line 465 · 2026-05-23T05:44:43.296384+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1369
}
```

</details>

---


### Tool call

_source line 466 · 2026-05-23T05:44:50.162212+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/review_round_6/submitted.pdf",
  "project": "importance_margin_vla_compress",
  "pages": "11-20",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/review_round_6/submitted.pdf",
    "project": "importance_margin_vla_compress",
    "pages": "11-20",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 467 · 2026-05-23T05:44:51.067057+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 11, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/review_round_6/_pdf_images/submitted_p11.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 366.8}, {\"page\": 12, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/review_round_6/_pdf_images/submitted_p12.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 262.5}, {\"page\": 13, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/review_round_6/_pdf_images/submitted_p13.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 227.2}, {\"page\": 14, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/review_round_6/_pdf_images/submitted_p14.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 301.8}, {\"page\": 15, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/review_round_6/_pdf_images/submitted_p15.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 263.7}, {\"page\": 16, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/review_round_6/_pdf_images/submitted_p16.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 237.6}, {\"page\": 17, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/review_round_6/_pdf_images/submitted_p17.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 261.8}, {\"page\": 18, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/review_round_6/_pdf_images/submitted_p18.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 269.6}, {\"page\": 19, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/im
…[truncated 621 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 904
}
```

</details>

---


### Tool call

_source line 468 · 2026-05-23T05:44:53.679025+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/review_round_6/_pdf_images/submitted_p11.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/review_round_6/_pdf_images/submitted_p11.png"
  }
}
```

</details>

---


### Tool result

_source line 469 · 2026-05-23T05:44:54.186723+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 507
}
```

</details>

---


### Tool call

_source line 470 · 2026-05-23T05:44:54.187306+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/review_round_6/_pdf_images/submitted_p12.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/review_round_6/_pdf_images/submitted_p12.png"
  }
}
```

</details>

---


### Tool result

_source line 471 · 2026-05-23T05:44:55.094596+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 907
}
```

</details>

---


### Tool call

_source line 472 · 2026-05-23T05:44:55.095036+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/review_round_6/_pdf_images/submitted_p13.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/review_round_6/_pdf_images/submitted_p13.png"
  }
}
```

</details>

---


### Tool result

_source line 473 · 2026-05-23T05:44:55.547936+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 474 · 2026-05-23T05:44:55.599304+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/review_round_6/_pdf_images/submitted_p14.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/review_round_6/_pdf_images/submitted_p14.png"
  }
}
```

</details>

---


### Tool result

_source line 475 · 2026-05-23T05:44:56.504499+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 905
}
```

</details>

---


### Tool call

_source line 476 · 2026-05-23T05:44:56.505047+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/review_round_6/_pdf_images/submitted_p15.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/review_round_6/_pdf_images/submitted_p15.png"
  }
}
```

</details>

---


### Tool result

_source line 477 · 2026-05-23T05:44:56.958770+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 453
}
```

</details>

---


### Tool call

_source line 478 · 2026-05-23T05:44:56.959090+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/review_round_6/_pdf_images/submitted_p16.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/review_round_6/_pdf_images/submitted_p16.png"
  }
}
```

</details>

---


### Tool result

_source line 479 · 2026-05-23T05:44:57.466768+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 507
}
```

</details>

---


### Tool call

_source line 480 · 2026-05-23T05:44:57.467207+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/review_round_6/_pdf_images/submitted_p17.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/review_round_6/_pdf_images/submitted_p17.png"
  }
}
```

</details>

---


### Tool result

_source line 481 · 2026-05-23T05:44:58.021105+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 553
}
```

</details>

---


### Tool call

_source line 482 · 2026-05-23T05:44:58.021615+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/review_round_6/_pdf_images/submitted_p18.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/review_round_6/_pdf_images/submitted_p18.png"
  }
}
```

</details>

---


### Tool result

_source line 483 · 2026-05-23T05:44:58.426479+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 404
}
```

</details>

---


### Tool call

_source line 484 · 2026-05-23T05:45:11.801120+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/review_round_6/submitted.pdf",
  "project": "importance_margin_vla_compress",
  "pages": "19-27",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/review_round_6/submitted.pdf",
    "project": "importance_margin_vla_compress",
    "pages": "19-27",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 485 · 2026-05-23T05:45:12.557019+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 19, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/review_round_6/_pdf_images/submitted_p19.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 278.9}, {\"page\": 20, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/review_round_6/_pdf_images/submitted_p20.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 245.8}, {\"page\": 21, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/review_round_6/_pdf_images/submitted_p21.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 245.8}, {\"page\": 22, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/review_round_6/_pdf_images/submitted_p22.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 240.2}, {\"page\": 23, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/review_round_6/_pdf_images/submitted_p23.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 360.1}, {\"page\": 24, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/review_round_6/_pdf_images/submitted_p24.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 387.3}, {\"page\": 25, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/review_round_6/_pdf_images/submitted_p25.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 343.8}, {\"page\": 26, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/review_round_6/_pdf_images/submitted_p26.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 301.8}, {\"page\": 27, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/im
…[truncated 388 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 755
}
```

</details>

---


### Tool call

_source line 486 · 2026-05-23T05:45:16.322959+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/review_round_6/_pdf_images/submitted_p19.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/review_round_6/_pdf_images/submitted_p19.png"
  }
}
```

</details>

---


### Tool result

_source line 487 · 2026-05-23T05:45:16.777021+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 454
}
```

</details>

---


### Tool call

_source line 488 · 2026-05-23T05:45:16.777557+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/review_round_6/_pdf_images/submitted_p20.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/review_round_6/_pdf_images/submitted_p20.png"
  }
}
```

</details>

---


### Tool result

_source line 489 · 2026-05-23T05:45:17.733197+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 955
}
```

</details>

---


### Tool call

_source line 490 · 2026-05-23T05:45:17.733681+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/review_round_6/_pdf_images/submitted_p21.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/review_round_6/_pdf_images/submitted_p21.png"
  }
}
```

</details>

---


### Tool result

_source line 491 · 2026-05-23T05:45:18.187381+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 453
}
```

</details>

---


### Tool call

_source line 492 · 2026-05-23T05:45:18.187878+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/review_round_6/_pdf_images/submitted_p22.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/review_round_6/_pdf_images/submitted_p22.png"
  }
}
```

</details>

---


### Tool result

_source line 493 · 2026-05-23T05:45:18.791197+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 603
}
```

</details>

---


### Tool call

_source line 494 · 2026-05-23T05:45:18.841801+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/review_round_6/_pdf_images/submitted_p23.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/review_round_6/_pdf_images/submitted_p23.png"
  }
}
```

</details>

---


### Tool result

_source line 495 · 2026-05-23T05:45:19.619331+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 777
}
```

</details>

---


### Tool call

_source line 496 · 2026-05-23T05:45:19.633776+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/review_round_6/_pdf_images/submitted_p24.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/review_round_6/_pdf_images/submitted_p24.png"
  }
}
```

</details>

---


### Tool call

_source line 497 · 2026-05-23T05:45:20.157015+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/review_round_6/_pdf_images/submitted_p25.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/review_round_6/_pdf_images/submitted_p25.png"
  }
}
```

</details>

---


### Tool result

_source line 498 · 2026-05-23T05:45:21.214278+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1580
}
```

</details>

---


### Tool result

_source line 499 · 2026-05-23T05:45:21.219084+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1062
}
```

</details>

---


### Tool call

_source line 500 · 2026-05-23T05:45:21.220900+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/review_round_6/_pdf_images/submitted_p26.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/review_round_6/_pdf_images/submitted_p26.png"
  }
}
```

</details>

---


### Tool call

_source line 501 · 2026-05-23T05:45:21.221190+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/review_round_6/_pdf_images/submitted_p27.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/review_round_6/_pdf_images/submitted_p27.png"
  }
}
```

</details>

---


### Tool result

_source line 502 · 2026-05-23T05:45:21.876157+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 654
}
```

</details>

---


### Tool result

_source line 503 · 2026-05-23T05:45:21.928864+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 707
}
```

</details>

---


### Tool call

_source line 504 · 2026-05-23T05:45:31.870820+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "CoRL 2026 reviewer form scoring rubric evaluation criteria"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "CoRL 2026 reviewer form scoring rubric evaluation criteria"
  }
}
```

</details>

---


### Tool call

_source line 505 · 2026-05-23T05:45:33.475863+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Compressor-VLA\" OR \"SpecPrune-VLA\" OR \"LightVLA\" VLA compression pruning 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Compressor-VLA\" OR \"SpecPrune-VLA\" OR \"LightVLA\" VLA compression pruning 2025 2026"
  }
}
```

</details>

---


### Tool call

_source line 506 · 2026-05-23T05:45:34.429129+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"See What Matters\" ICML 2026 VLA vision token pruning"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"See What Matters\" ICML 2026 VLA vision token pruning"
  }
}
```

</details>

---


### Tool result

_source line 507 · 2026-05-23T05:45:37.144438+00:00_

Web search results for query: "CoRL 2026 reviewer form scoring rubric evaluation criteria"

Links: [{"title":"Scoring Rubric | Free LET Reviewer and Drill","url":"https://www.edureaper.com/2026/05/scoring-rubric-free-let-reviewer-and.html"},{"title":"CoRL 2026 - Instruction for Authors","url":"https://www.corl.org/contributions/instruction-for-authors"},{"title":"How to Build a Scoring Rubric That Produces Consistent Decisions - RQ Platform","url":"https://rqawards.com/how-to-build-a-scoring-rubric-that-produces-consistent-decisions/"},{"title":"RULERS: Locked Rubrics and Evidence-Anchored Scoring for Robust LLM Evaluation","url":"https://arxiv.org/pdf/2601.08654"},{"title":"Development and Validation of a Scoring Rubric for Editorial Evaluation of Peer-review Quality: A Pilot Study","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11000557/"},{"title":"Reviewer Guidelines — CoRL 2023","url":"https://www.corl2023.org/reviewer-guidelines"}]

Based on the search results, I found relevant information about CoRL 2026, though the specific detailed scoring rubric wasn't fully available. Here's what I found:

From the CoRL 2026 Instructions for Authors, reviewers must have at least one accepted publication at previous robotics or learning conferences, and authors with 3 or more submissions must agree to serve as a reviewer.

While the search results included CoRL 2023 reviewer guidelines that mention evaluating relevance (whether papers address robot learning, apply/improve learning-based methods, and whether CoRL audiences would be interested), and that CoRL papers are required to include a limitations section, the complete CoRL 2026 reviewer form with the full scoring rubric and all evaluation criteria wasn't directly available in these results.

To get the complete and most current CoRL 2026 reviewer form scoring rubric, I'd recommend checking the official CoRL 2026 website directly or contacting the program chairs, as the detailed evaluation criteria form may be pos
…[truncated 193 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 5273
}
```

</details>

---


### Tool result

_source line 508 · 2026-05-23T05:45:40.157587+00:00_

Web search results for query: ""See What Matters" ICML 2026 VLA vision token pruning"

Links: [{"title":"ICML Poster See What Matters: Differentiable Grid Sample Pruning for Generalizable Vision-Language-Action Model","url":"https://icml.cc/virtual/2026/poster/65010"},{"title":"[2605.11817] See What Matters: Differentiable Grid Sample Pruning for Generalizable Vision-Language-Action Model","url":"https://arxiv.org/abs/2605.11817"},{"title":"VLA-Pruner: Temporal-Aware Dual-Level Visual Token Pruning for Efficient Vision-Language-Action Inference","url":"https://arxiv.org/pdf/2511.16449"},{"title":"History-Conditioned Spatio-Temporal Visual Token Pruning for Efficient Vision-Language Navigation","url":"https://arxiv.org/pdf/2603.06480"},{"title":"GitHub - ZLKong/Awesome-Collection-Token-Reduction: A collection of token reduction (token pruning, merging, clustering, etc.) techniques for ML/AI · GitHub","url":"https://github.com/ZLKong/Awesome-Collection-Token-Reduction"},{"title":"LVPruning: An Effective yet Simple Language-Guided Vision Token Pruning   Approach for Multi-modal Large Language Models","url":"https://arxiv.org/pdf/2501.13652"}]

I found the research paper you're looking for! Here are the key details about "See What Matters":

"See What Matters" presents the Differentiable Grid Sampler (GridS), a plug-and-play module that performs task-aware, continuous resampling of visual tokens in VLA by adaptively predicting a minimal set of salient coordinates and extracting features via differentiable interpolation, preserving essential spatial information while achieving drastic compression (with fewer than 10% of original visual tokens).

The work addresses the fundamental trade-off in existing token pruning methods: aggressive compression using pruning inevitably discards critical geometric details like contact points, leading to severe performance degradation.

Experiments on both LIBERO benchmark and a real robotic platform demonstrate that GridS achieves a 76%
…[truncated 288 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 5728
}
```

</details>

---


### Tool result

_source line 509 · 2026-05-23T05:45:41.563993+00:00_

Web search results for query: ""Compressor-VLA" OR "SpecPrune-VLA" OR "LightVLA" VLA compression pruning 2025 2026"

Links: [{"title":"Specprune-vla Boosts Vision-Language-Action Models, Avoiding Over 20% Success Rate Drops With Smart Pruning","url":"https://quantumzeitgeist.com/faster-models-performance-specprune-vla-boosts-vision-language-action-avoiding-success/"},{"title":"Compressor-VLA: Instruction-Guided Visual Token Compression for Efficient Robotic Manipulation","url":"https://chatpaper.com/paper/212383"},{"title":"Compressor-VLA: Instruction-Guided Visual Token Compression for Efficient Robotic Manipulation","url":"https://arxiv.org/html/2511.18950v1"},{"title":"Compressor-VLA: Instruction-Guided Visual Token Compression for Efficient Robotic Manipulation","url":"https://arxiv.org/pdf/2511.18950"},{"title":"SpecPrune-VLA: Accelerating Vision-Language-Action Models via Action-Aware Self-Speculative Pruning | Request PDF","url":"https://www.researchgate.net/publication/395354566_SpecPrune-VLA_Accelerating_Vision-Language-Action_Models_via_Action-Aware_Self-Speculative_Pruning"},{"title":"SpecPrune-VLA: Accelerating Vision-Language-Action Models via Action-Aware Self-Speculative Pruning","url":"https://arxiv.org/html/2509.05614v1"},{"title":"SpecPrune-VLA: Accelerating Vision-Language-Action Models via Action-Aware Self-Speculative Pruning","url":"https://arxiv.org/pdf/2509.05614"},{"title":"[2511.18950] Compressor-VLA: Instruction-Guided Visual Token Compression for Efficient Robotic Manipulation","url":"https://arxiv.org/abs/2511.18950"}]

Based on the search results, I found information about **SpecPrune-VLA** and **Compressor-VLA**, two recent VLA compression and pruning methods from 2025. Here's what I found:

## SpecPrune-VLA

SpecPrune-VLA intelligently prunes visual tokens by considering both the immediate context and the broader history of actions, achieving substantial speedups on standard hardware with minimal loss of accuracy. It is a training-fre
…[truncated 1310 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 8088
}
```

</details>

---


### Tool call

_source line 510 · 2026-05-23T05:45:46.036194+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Don't Run with Scissors\" Jabbour VLA pruning 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Don't Run with Scissors\" Jabbour VLA pruning 2025"
  }
}
```

</details>

---


### Tool call

_source line 511 · 2026-05-23T05:45:47.041869+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "TokenPacker vision token compression VLM 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "TokenPacker vision token compression VLM 2024 2025"
  }
}
```

</details>

---


### Tool call

_source line 512 · 2026-05-23T05:45:47.947493+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "FastV PruMerge SparseVLM FitPrune vision language model token pruning"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "FastV PruMerge SparseVLM FitPrune vision language model token pruning"
  }
}
```

</details>

---


### Tool result

_source line 513 · 2026-05-23T05:45:51.693698+00:00_

Web search results for query: ""Don't Run with Scissors" Jabbour VLA pruning 2025"

Links: [{"title":"[2510.08464] Don't Run with Scissors: Pruning Breaks VLA Models but They Can Be Recovered","url":"https://arxiv.org/abs/2510.08464"},{"title":"Don't Run with Scissors: Pruning Breaks VLA Models but They Can Be Recovered | OpenReview","url":"https://openreview.net/forum?id=c8g57pKdXD"},{"title":"Don't Run with Scissors: Pruning Breaks VLA Models but They Can Be Recovered","url":"https://gluestick-vla.github.io/"},{"title":"Don't Run With Scissors (2025 Keenspot) comic books","url":"https://www.mycomicshop.com/search?TID=62231167"},{"title":"Workshop Safety, a.k.a. Don't Run With Scissors","url":"https://www.kitplanes.com/running-with-scissors-shop-safety/"},{"title":"We Don't Run with Scissors - Army University Press","url":"https://www.armyupress.army.mil/Journals/Military-Review/English-Edition-Archives/September-October-2022/Rasak/"},{"title":"Check out the translation for \"don't run with scissors\" on SpanishDictionary.com!","url":"https://www.spanishdict.com/translate/don't%20run%20with%20scissors"},{"title":"Don't Run With Scissors #1 Comic Book 2025 - Keenspot | eBay","url":"https://www.ebay.com/itm/277104322159"},{"title":"Hot market: Don't run with scissors","url":"https://www.farmprogress.com/cattle-news/hot-market-don-t-run-with-scissors"}]

Based on the search results, I found the academic paper you're looking for:

"Don't Run with Scissors: Pruning Breaks VLA Models but They Can Be Recovered" is a research paper by Jason Jabbour and 8 other authors about Vision-Language-Action (VLA) models.

The paper's key findings are:

- Pruning VLA models leads to drastic degradation and increased safety violations
- The researchers introduce GLUESTICK, a post-pruning recovery method that restores much of the original model's functionality while retaining sparsity benefits through one-time interpolation between dense and pruned models, which can be applied during in
…[truncated 569 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 5657
}
```

</details>

---


### Tool result

_source line 514 · 2026-05-23T05:45:53.652731+00:00_

Web search results for query: "TokenPacker vision token compression VLM 2024 2025"

Links: [{"title":"TokenPacker: Efficient Visual Projector for Multimodal LLM | Request PDF","url":"https://www.researchgate.net/publication/393103429_TokenPacker_Efficient_Visual_Projector_for_Multimodal_LLM"},{"title":"Window Token Concatenation for Efficient Visual Large Language Models","url":"https://www.emergentmind.com/papers/2504.04024"},{"title":"Published as a conference paper at ICLR 2025","url":"https://arxiv.org/pdf/2411.03312"},{"title":"A Survey on Visual Token Compression for Efficient Vision-Language Models","url":"https://www.researchgate.net/publication/398219411_A_Survey_on_Visual_Token_Compression_for_Efficient_Vision-Language_Models"},{"title":"TokenPacker: Efficient Visual Projector for Multimodal LLM | International Journal of Computer Vision","url":"https://dl.acm.org/doi/abs/10.1007/s11263-025-02491-7"},{"title":"GitHub - daixiangzi/Awesome-Token-Compress: A paper list of some recent works about Token Compress for Vit and VLM · GitHub","url":"https://github.com/daixiangzi/Awesome-Token-Compress"},{"title":"Towards Lossless Ultimate Vision Token Compression for VLMs","url":"https://arxiv.org/pdf/2512.09010"}]

Based on the search results, here's what I found about TokenPacker:

## TokenPacker Overview

TokenPacker is a visual projector component for multimodal large language models (MLLMs) that connects the visual encoder with the large language model. 

## Key Features and Performance

TokenPacker learns a compact token compression module using cross-attention. The method proposes a dynamic image slicing scheme to efficiently handle high-resolution images.

In terms of results, TokenPacker can compress visual tokens by 75% ~89%, while maintaining or even improving performance on various benchmarks, achieving significantly higher efficiency.

## Context in Vision-Language Model Research

Visual token reduction methods for multimodal tasks can be categorized in
…[truncated 643 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 6610
}
```

</details>

---


### Tool result

_source line 515 · 2026-05-23T05:45:55.309717+00:00_

Web search results for query: "FastV PruMerge SparseVLM FitPrune vision language model token pruning"

Links: [{"title":"ATP-LLaVA: Adaptive Token Pruning for Large Vision Language Models","url":"https://www.researchgate.net/publication/394577537_ATP-LLaVA_Adaptive_Token_Pruning_for_Large_Vision_Language_Models"},{"title":"(PDF) SVD-Prune: Training-Free Token Pruning For Efficient Vision-Language Models","url":"https://www.researchgate.net/publication/403791973_SVD-Prune_Training-Free_Token_Pruning_For_Efficient_Vision-Language_Models"},{"title":"Fit and Prune: Fast and Training-free Visual Token Pruning for   Multi-modal Large Language Models","url":"https://arxiv.org/pdf/2409.10197"},{"title":"SVD-PRUNE: TRAINING-FREE TOKEN PRUNING FOR EFFICIENT VISION-LANGUAGE MODELS","url":"https://arxiv.org/html/2604.11530v1"},{"title":"[2409.10197] Fit and Prune: Fast and Training-free Visual Token Pruning for Multi-modal Large Language Models","url":"https://arxiv.org/abs/2409.10197"},{"title":"Fit and Prune: Fast and Training-free Visual Token Pruning for Multi-modal Large Language Models","url":"https://arxiv.org/html/2409.10197v1"},{"title":"FastMMoE: Accelerating Multimodal Large Language Models through Dynamic Expert Activation and Routing-Aware Token Pruning","url":"https://arxiv.org/pdf/2511.17885"},{"title":"ZSPAPrune: Zero-Shot Prompt-Aware Token Pruning for Vision-Language Models","url":"https://arxiv.org/pdf/2510.17197"},{"title":"Token Pruning in Multimodal Large Language Models","url":"https://aclanthology.org/2025.findings-acl.802.pdf"}]

Based on the search results, here's what I found about these vision language model token pruning methods:

## Overview of Token Pruning Methods

Visual token compression is central to efficient VLM inference with high-resolution images and long visual sequences. The methods you mentioned are all part of the token pruning landscape for multimodal large language models (MLLMs).

## Individual Methods

**FastV**: FastV prunes unne
…[truncated 1216 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 7362
}
```

</details>

---


### Tool call

_source line 516 · 2026-05-23T05:46:01.588028+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/main.tex",
  "offset": "0",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/main.tex",
    "offset": "0",
    "limit": "100"
  }
}
```

</details>

---


### Tool result

_source line 517 · 2026-05-23T05:46:01.889613+00:00_

0	\documentclass{article}
1	
2	\usepackage{corl_2026} % Submission version: anonymous, line numbers enabled.
3	% \usepackage[final]{corl_2026} % Uncomment for camera-ready.
4	
5	\usepackage{amsmath,amssymb}
6	\usepackage{graphicx}
7	\usepackage{booktabs}
8	\usepackage{multirow}
9	\usepackage{enumitem}
10	\usepackage{subcaption}
11	
12	\title{Why Token Pruning Crashes Some Robot Policies but Not Others:\\Vision Connectors and VLA Token Compressibility}
13	
14	\begin{document}
15	\maketitle
16	
17	\input{abstract}
18	
19	\keywords{vision-language-action models, token pruning, robot learning}
20	
21	\input{introduction}
22	
23	\input{related_work}
24	
25	\input{method}
26	
27	\input{experiments}
28	
29	\input{conclusion}
30	
31	\bibliography{references}
32	
33	\input{appendix}
34	
35	\end{document}
36	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 518 · 2026-05-23T05:46:11.654177+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

```json
{
  "description": "Check references.bib coverage",
  "subagent_type": "Explore",
  "prompt": "I need to check the references in a LaTeX paper. Find and read the file references.bib in /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/ directory. List ALL citation keys and the titles of all referenced papers. I need to verify which concurrent VLA works are cited:\n1. \"Don't Run with Scissors\" (Jabbour et al.)\n2. Compressor-VLA\n3. SpecPrune-VLA\n4. LightVLA\n5. \"See What Matters\" (ICML 2026)\n6. VLA-Cache\n7. VLA-IAP\n8. EfficientVLA\n9. VLA-Pruner\n10. TokenPacker\n11. FastV\n12. PruMerge\n13. SparseVLM / SparseVILA\n14. FitPrune\n15. CrossGET\n16. InternVL (pixel-shuffle)\n\nFor each, report: FOUND (with cite key) or NOT FOUND."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Agent",
  "tool_args": {
    "description": "Check references.bib coverage",
    "subagent_type": "Explore",
    "prompt": "I need to check the references in a LaTeX paper. Find and read the file references.bib in /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/ directory. List ALL citation keys and the titles of all referenced papers. I need to verify which concurrent VLA works are cited:\n1. \"Don't Run with Scissors\" (Jabbour et al.)\n2. Compressor-VLA\n3. SpecPrune-VLA\n4. LightVLA\n5. \"See What Matters\" (ICML 2026)\n6. VLA-Cache\n7. VLA-IAP\n8. EfficientVLA\n9. VLA-Pruner\n10. TokenPacker\n11. FastV\n12. PruMerge\n13. SparseVLM / SparseVILA\n14. FitPrune\n15. CrossGET\n16. InternVL (pixel-shuffle)\n\nFor each, report: FOUND (with cite key) or NOT FOUND."
  }
}
```

</details>

---


### Tool call

_source line 519 · 2026-05-23T05:46:13.914128+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/references.bib"
  }
}
```

</details>

---


### Tool result

_source line 520 · 2026-05-23T05:46:13.964926+00:00_

1	% References for: The Cliff Edge — Why Vision Token Reduction Fails
2	% Catastrophically in VLA Closed-Loop Control
3	% Auto-generated from literature_map.yaml (verified entries only)
4	% 2026-05-17
5	
6	% ============================================================
7	% VLA Token Compression (concurrent work)
8	% ============================================================
9	
10	@article{gao2025compressorvla,
11	  title={Compressor-VLA: Instruction-Guided Visual Token Compression for Efficient Robotic Manipulation},
12	  author={Gao, Juntao and Ye, Feiyang and Zhang, Jing and Qian, Wenjing},
13	  journal={arXiv preprint arXiv:2511.18950},
14	  year={2025},
15	  eprint={2511.18950},
16	  archivePrefix={arXiv}
17	}
18	
19	@article{wang2025specprunevla,
20	  title={SpecPrune-VLA: Accelerating Vision-Language-Action Models via Action-Aware Self-Speculative Pruning},
21	  author={Wang, Hanzhen and Xu, Jiaming and Xiang, Yushun and Pan, Jiayi and Zhou, Yongkang and Li, Yong-Lu and Dai, Guohao},
22	  journal={arXiv preprint arXiv:2509.05614},
23	  year={2025},
24	  eprint={2509.05614},
25	  archivePrefix={arXiv}
26	}
27	
28	@inproceedings{jiang2026lightvla,
29	  title={The Better You Learn, The Smarter You Prune: Towards Efficient Vision-Language-Action Models via Differentiable Token Pruning},
30	  author={Jiang, Titong and Jiang, Xuefeng and Ma, Yuan and Wen, Xin and Li, Bailin and Zhan, Kun and Jia, Peng and Liu, Yahui and Sun, Sheng and Lang, Xianpeng},
31	  booktitle={Proceedings of the IEEE International Conference on Robotics and Automation (ICRA)},
32	  year={2026},
33	  eprint={2509.12594},
34	  archivePrefix={arXiv}
35	}
36	
37	@inproceedings{feng2026seewhatmatters,
38	  title={See What Matters: Differentiable Grid Sample Pruning for Generalizable Vision-Language-Action Model},
39	  author={Feng, Yixu and Zhao, Zinan and Ma, Yanxiang and Xia, Chenghao and Du, Chengbin and Wang, Yunke and Xu, Chang},
40	  booktitle={Proceedings of the Forty-Third International C
…[truncated 22880 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 521 · 2026-05-23T05:46:34.091454+00:00_

Perfect! I found the references.bib file. Let me analyze it to extract all citation keys and match them against your list of concurrent VLA works.

Based on my review of the references.bib file, here's the complete list of ALL citation keys found and the verification status for your 16 concurrent VLA works:

## Citation Keys Found in references.bib

**VLA Token Compression (concurrent work section):**
- gao2025compressorvla
- wang2025specprunevla
- jiang2026lightvla
- feng2026seewhatmatters
- zhang2025sparsevlm
- khaki2025sparsevila
- jabbour2025dontrun
- li2024roboflamingo

**VLA Models section:**
- shukor2025smolvla
- kim2024openvla
- brohan2023rt2
- black2024pi0
- black2025pi05
- ghosh2024octo
- brohan2023rt1

**VLM/LLM Token Efficiency section:**
- chen2024fastv
- xu2025vlacache
- cheng2026vlaiap

**ViT Token Pruning/Merging section:**
- rao2021dynamicvit
- bolya2023tome
- liang2022evit

**Other sections:**
- liu2023libero, alayrac2022flamingo, liu2023llava, shi2016subpixel, chen2024internvl, li2023blip2, jaegle2021perceiver, oquab2023dinov2, zhai2023siglip, yang2024qwen2, lipman2023flow, li2024cogact, kim2025openoft, li2024tokenpacker, zheng2025xvla, wen2024tinyvla, lewis2020bart, ryoo2021tokenlearner, yin2022avit, meng2022adavit, chen2023sparsevit, ye2025fitprune, shi2024crossget, zhang2024fastervlm, liu2024llava15, chen2024internvl25, gao2024miniinternvl, zitkovich2023rt2, openxembodiment2024, zhang2023h2o, xiao2024streamingllm, mees2022calvin, chi2023diffusionpolicy, zeng2023transformers_tsf, bouthillier2024negative, oquab2024dinov2

---

## Verification Results for Your 16 Concurrent VLA Works

1. **"Don't Run with Scissors" (Jabbour et al.)** - **FOUND**
   - Citation key: `jabbour2025dontrun`
   - Full title: "Don't Run with Scissors: Pruning Breaks VLA Models but They Can Be Recovered"

2. **Compressor-VLA** - **FOUND**
   - Citation key: `gao2025compressorvla`
   - Full title: "Compressor-VLA: Instruction-Guided Visual Token Compression for Efficient Ro
…[truncated 3163 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Agent",
  "elapsed_ms": 22437
}
```

</details>

---


### Tool call

_source line 522 · 2026-05-23T05:46:41.940442+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/docs/paper/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/docs/paper/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress"
  }
}
```

</details>

---


### Tool result

_source line 523 · 2026-05-23T05:46:42.041584+00:00_

/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/experiments_deprecated.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/background.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/results_v2.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/experimental_setup.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/analysis.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/results.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/discussion.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/main.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/related_work.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/abstract.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/introduction.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/method.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/conclusion.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/appendix.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/experiments.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Glob",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 524 · 2026-05-23T05:46:44.706452+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 525 · 2026-05-23T05:46:44.706940+00:00_

1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{ViT token pruning.}
5	DynamicViT~\cite{rao2021dynamicvit}, EViT~\cite{liang2022evit}, A-ViT~\cite{yin2022avit}, and Token Merging~\cite{bolya2023tome} remove 50--66\% of tokens with under 0.5\,pp ImageNet accuracy loss. Their success rests on classification's insensitivity to spatial layout; robotic manipulation inverts this assumption, as grasping depends on spatial arrangement. None has been evaluated in closed-loop VLA control.
6	
7	\paragraph{Token efficiency in VLMs and VLAs.}
8	FastV~\cite{chen2024fastv} and PruMerge~\cite{shang2024prumerge} reduce vision tokens in VLMs using language-backbone attention signals. VLA-specific methods have emerged in parallel: VLA-IAP~\cite{cheng2026vlaiap} aligns pruning with action-prediction importance, VLA-Cache~\cite{xu2025vlacache} compresses at the KV-cache level, EfficientVLA~\cite{yang2025efficientvla} combines pruning with merging, and VLA-Pruner~\cite{liu2025vlapruner} learns a pruning policy jointly with the action head. Each validates on a single architecture; no study compares pruning robustness across connector designs.
9	
10	\paragraph{Vision connectors.}
11	The connector between ViT and language backbone governs how spatial information distributes across tokens. LLaVA~\cite{liu2023llava} projects patches independently through an MLP; BLIP-2~\cite{li2023blip2} uses cross-attention queries; pixel shuffle~\cite{shi2016subpixel} folds spatial neighborhoods into channels, adopted by SmolVLA~\cite{shukor2025smolvla}. These create qualitatively different token dependencies; independent connectors leave patch information separable, while entangling connectors distribute content across tokens. The pruning consequences have not been characterized.
12	
13	We provide the first cross-architecture analysis of how connector coupling and task complexity jointly govern VLA token compressibility, introducing CV of token norms as a single-pass diagnostic that corr
…[truncated 63 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 526 · 2026-05-23T05:46:45.260725+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 527 · 2026-05-23T05:46:45.361725+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	\begin{figure*}[t]
5	\centering
6	\includegraphics[width=\textwidth]{figures/paper/fig_teaser.pdf}
7	\caption{Two-axis framework for VLA token compressibility. Pruning robustness depends on both connector coupling (token-independent vs.\ token-entangling) and task complexity (single-step vs.\ multi-step). X-VLA loses 1.4\,pp on Object at $k{=}0.9$ but 27.8\,pp on Goal (random pruning), a $20{\times}$ task-complexity amplification.}
8	\label{fig:teaser}
9	\end{figure*}
10	
11	Remove 5\% of vision tokens from SmolVLA and its success rate collapses from 59.2\% to 0.0\% across all task suites and pruning methods. Apply the same 5\% reduction to $\pi_0.5$ and it retains 98.2\% under L2 norm selection. Both are Vision-Language-Action (VLA) models built on a Vision Transformer (ViT) encoder feeding tokens through a connector into a language model backbone; the critical difference is not model scale (450M vs.\ 4B parameters) but the connector architecture. Token pruning is well-established for ViTs~\cite{rao2021dynamicvit,bolya2023tome,liang2022evit} and a growing body of work extends it to VLAs~\cite{cheng2026vlaiap,xu2025vlacache,yang2025efficientvla,liu2025vlapruner}, but each method validates on a single architecture.
12	
13	These methods implicitly assume that pruning transfers across VLA designs. Yet current VLAs employ fundamentally different vision connectors: linear projections~\cite{black2024pi0}, MLP projectors~\cite{kim2024openvla}, pixel-shuffle folding~\cite{shukor2025smolvla}, and learned encoders with cross-token self-attention~\cite{zheng2025xvla}. Each imposes distinct constraints on how visual information distributes across tokens. Deploying a pruning method validated on one connector type to another risks silent degradation or complete failure. No prior work evaluates pruning robustness across both connector architectures and task complexity.
14	
15	We propose a two-axis analysis of VLA token compr
…[truncated 2036 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 528 · 2026-05-23T05:46:51.210977+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 529 · 2026-05-23T05:46:51.311875+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	\subsection{Models and Connectors}
5	\label{sec:models}
6	
7	We evaluate token pruning across six VLA architectures spanning three vision connector families (Table~\ref{tab:model_properties}). These connectors differ in whether they process ViT patches independently or create cross-token dependencies, a distinction we formalize as \emph{coupling}.
8	
9	\textbf{Linear projection} applies a single matrix multiplication per patch. $\pi_0$~\cite{black2024pi0} projects 256 patches through a linear layer; $\pi_0.5$~\cite{black2025pi05} uses a $\times\!\sqrt{d}$-scaled linear projection across 768 tokens from three cameras (CV$\,{<}\,$0.06).
10	
11	\textbf{MLP projector} maps each patch independently through a multi-layer perceptron. OpenVLA~\cite{kim2024openvla} uses a three-layer MLP (256 tokens; CV$\,{=}\,$0.215); OFT~\cite{kim2025openoft}, an OpenVLA fine-tuning variant evaluated offline, shares the same connector (512 tokens; CV$\,{=}\,$0.219).
12	
13	\textbf{Token-entangling connectors} introduce cross-token dependencies. X-VLA~\cite{zheng2025xvla} feeds linearly projected tokens through a 12-layer BART encoder~\cite{lewis2020bart} (50 tokens). SmolVLA~\cite{shukor2025smolvla} applies pixel-shuffle $4{\times}4$ folding, concatenating 16 contiguous patches into each output token's channel dimension (128 tokens).
14	
15	We classify coupling as \emph{independent} when each output token depends on a single input patch, and \emph{entangling} when output tokens encode information from multiple patches. Four models ($\pi_0.5$, X-VLA, OpenVLA, SmolVLA) are evaluated in closed-loop control on LIBERO~\cite{liu2023libero}; $\pi_0$ and OFT are analyzed via offline metrics only.
16	
17	\begin{table}[t]
18	\centering
19	\small
20	\caption{VLA models evaluated in this study. Coupling indicates whether the connector processes patches independently or creates cross-token dependencies. $N$ = number of vision tokens input to the LLM backbone
…[truncated 4081 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 530 · 2026-05-23T05:46:51.362889+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 531 · 2026-05-23T05:46:51.415341+00:00_

1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	Vision token pruning in VLAs is not a uniform operation: its outcome depends on the interaction between connector architecture and task complexity. Across six VLA architectures (450M--7B) and four LIBERO suites, connector coupling is the primary determinant of pruning robustness. Token-independent connectors degrade proportionally to the fraction removed; token-entangling connectors exhibit task-amplified collapse. SmolVLA's pixel-shuffle produces 0.0\% SR when just 5\% of tokens are removed; X-VLA loses 1.4\,pp on Object at $k{=}0.9$ but 27.8\,pp on Goal under random pruning, a $20{\times}$ amplification. The CV of token L2 norms serves as a single-pass diagnostic that correlates with both pruning tolerance and method sensitivity across all three connector families. For architectures where all pruning strategies fail, VTR recovers a pixel-shuffle VLA from 0.0\% to over 60\% SR at 75\% compression.
5	
6	Two directions remain open: real-robot validation to confirm the connector-complexity interaction transfers beyond simulation, and adaptive per-task pruning schedules that adjust retention ratio to estimated task complexity.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 52
}
```

</details>

---


### Tool call

_source line 532 · 2026-05-23T05:46:58.042327+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 533 · 2026-05-23T05:46:58.093201+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Experimental Setup}
5	\label{sec:exp_setup}
6	
7	We evaluate vision token pruning across six VLA architectures spanning three connector families on the LIBERO benchmark~\cite{liu2023libero}. LIBERO provides four task suites of increasing complexity: Object (object manipulation), Spatial (spatial reasoning), Goal (goal-conditioned tasks), and Long (long-horizon multi-step tasks). Each suite contains 10 tasks evaluated over 50 episodes, yielding 500 episodes per condition.
8	
9	Four models are evaluated in closed-loop robotic control: $\pi_0.5$~\cite{black2025pi05} (4B parameters, linear projection with $\times\!\sqrt{d}$ scaling, 768 tokens from three cameras, CV$\,{=}\,$0.055), X-VLA~\cite{zheng2025xvla} (880M, linear projection followed by a 12-layer BART encoder~\cite{lewis2020bart}, 50 tokens, CV$\,{=}\,$0.151), OpenVLA~\cite{kim2024openvla} (7B, three-layer MLP projector, 256 tokens, CV$\,{=}\,$0.215), and SmolVLA~\cite{shukor2025smolvla} (450M, pixel-shuffle $4{\times}4$ folding, 128 tokens, CV$\,{=}\,$0.314). Two additional models are analyzed via offline metrics only: $\pi_0$~\cite{black2024pi0} (3.3B, linear projection, 256 tokens, CV$\,{=}\,$0.038) and OFT~\cite{kim2025openoft} (7B, three-layer MLP, 512 tokens, CV$\,{=}\,$0.219). All six architectures contribute to the CV diagnostic (Section~\ref{sec:cv_sensitivity}). Table~\ref{tab:model_properties} summarizes model properties and connector details.
10	
11	The pruning protocol applies post-connector token pruning at retention ratios $k \in \{0.3, 0.5, 0.7, 0.85, 0.9, 0.95\}$. Two strategies bracket the robustness range: \textbf{L2 norm selection} ranks tokens by L2 norm and retains the top-$k$ fraction, providing an importance-based favorable test; \textbf{random subsampling} selects tokens uniformly at random, providing a conservative lower bound. Both strategies physically remove tokens and re-index position IDs. All results report mean s
…[truncated 12480 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 534 · 2026-05-23T05:47:47.266237+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"EfficientVLA\" training-free acceleration compression VLA 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"EfficientVLA\" training-free acceleration compression VLA 2025"
  }
}
```

</details>

---


### Tool call

_source line 535 · 2026-05-23T05:47:47.568458+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "VLA token compression survey 2026 robot manipulation efficiency"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "VLA token compression survey 2026 robot manipulation efficiency"
  }
}
```

</details>

---


### Tool result

_source line 536 · 2026-05-23T05:47:54.262028+00:00_

Web search results for query: "VLA token compression survey 2026 robot manipulation efficiency"

Links: [{"title":"Compressor-VLA: Instruction-Guided Visual Token Compression for Efficient Robotic Manipulation","url":"https://arxiv.org/pdf/2511.18950"},{"title":"Compressor-VLA: Instruction-Guided Visual Token Compression for Efficient Robotic Manipulation","url":"https://arxiv.org/html/2511.18950v1"},{"title":"[2511.18950] Compressor-VLA: Instruction-Guided Visual Token Compression for Efficient Robotic Manipulation","url":"https://arxiv.org/abs/2511.18950"},{"title":"Compressor-VLA: Instruction-Guided Visual Token Compression for Efficient Robotic Manipulation","url":"https://chatpaper.com/paper/212383"},{"title":"GitHub - Ed1sonChen/DailyArxiv · GitHub","url":"https://github.com/Ed1sonChen/DailyArxiv"},{"title":"A Survey on Efficient Vision-Language-Action Models","url":"https://arxiv.org/html/2510.24795v1"},{"title":"GitHub - KwanWaiPang/Awesome-VLA: Paper Survey for Visual Language Action · GitHub","url":"https://github.com/KwanWaiPang/Awesome-VLA"}]

Based on the search results, I found relevant research on VLA token compression for robot manipulation efficiency:

## Key Research Findings

The significant computational overhead of processing redundant visual tokens remains a critical bottleneck for real-time robotic deployment, as standard token pruning techniques struggle to preserve task-critical visual information.

### Compressor-VLA Framework

Compressor-VLA is a novel hybrid instruction-conditioned token compression framework consisting of two modules: a Semantic Task Compressor (STC) that distills holistic, task-relevant context, and a Spatial Refinement Compressor (SRC) that preserves fine-grained spatial details. This compression is dynamically modulated by the natural language instruction, allowing for adaptive condensation of task-relevant visual information.

**Performance Results:** Compressor-VLA achieves competitive success rates on the LIBERO be
…[truncated 676 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 6693
}
```

</details>

---


### Tool result

_source line 537 · 2026-05-23T05:47:55.266718+00:00_

Web search results for query: ""EfficientVLA" training-free acceleration compression VLA 2025"

Links: [{"title":"EfficientVLA: Training-Free Acceleration and Compression for Vision-Language-Action Models | OpenReview","url":"https://openreview.net/forum?id=SELYlDHZk2"},{"title":"EfficientVLA: Training-Free Acceleration and Compression ...","url":"https://openreview.net/pdf?id=SELYlDHZk2"},{"title":"[PDF] EfficientVLA: Training-Free Acceleration and Compression for Vision-Language-Action Models | Semantic Scholar","url":"https://www.semanticscholar.org/paper/310b6b4048e36d5948de19fd26e112cbf05fa754"},{"title":"[2506.10100] EfficientVLA: Training-Free Acceleration and Compression for Vision-Language-Action Models","url":"https://arxiv.org/abs/2506.10100"},{"title":"Paper page - EfficientVLA: Training-Free Acceleration and Compression for Vision-Language-Action Models","url":"https://huggingface.co/papers/2506.10100"},{"title":"EfficientVLA: Training-Free Acceleration and Compression for Vision-Language-Action Models","url":"https://arxiv.org/pdf/2506.10100"},{"title":"[Literature Review] EfficientVLA: Training-Free Acceleration and Compression for Vision-Language-Action Models","url":"https://www.themoonlight.io/en/review/efficientvla-training-free-acceleration-and-compression-for-vision-language-action-models"},{"title":"EfficientVLA: Training-Free Acceleration and Compression for Vision-Language-Action Models","url":"https://arxiv.org/html/2506.10100v1"}]

I found comprehensive search results for EfficientVLA. Here's what the research reveals:

## Overview

EfficientVLA is a structured and training-free inference acceleration framework that systematically eliminates barriers by cohesively exploiting multifaceted redundancies in Vision-Language-Action models.

## Key Problem

Vision-Language-Action (VLA) models, particularly diffusion-based architectures, demonstrate transformative potential for embodied intelligence but are severely hampered by high computational a
…[truncated 1011 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 8000
}
```

</details>

---
