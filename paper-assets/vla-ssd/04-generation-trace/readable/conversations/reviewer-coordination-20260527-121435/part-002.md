# Reviewer coordination (archived snapshot) — Part 2 of 2

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Conversation logs

[← Part 1](part-001.md) · [Transcript overview](../reviewer-coordination-20260527-121435.md) · [Structured JSON](../../../sessions/71/71f81e4a4baf81592b26.json)

## Round 24

### Tool result

_source line 570 · 2026-05-27T08:43:08.638128+00:00_

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
14	TracVLA is trained on an OXE subset with spatial trace conditioning.
15	\textbf{NORA}~\cite{hung2025nora} uses Qwen2.5-VL-3B ($\sim$3B parameters, 36 layers, grouped-query attention [GQA] with 16 query heads and 2 KV heads) with the native Qwen2.5-VL vision encoder, which processes images at dynamic resolution without a separate projection stage.
16	
17	Each architecture is evaluated in trained and reference conditions; we define the \emph{reference checkpoint} as the corresponding pretrained model before LIBERO fine-tuning.
18	A critical asymmetry distinguishes the reference baselines: the OpenVLA reference is an OXE-pretrained VLA, already fine-tuned for action prediction on 970K episodes, while the TracVLA and NORA references are pure vision-language models (Phi-3-Vision and Qwen2.5-VL) with no action training.
19	OpenVLA trained-vs-reference comparisons therefore measure a VLA-to-VLA transition; TracVLA and NORA comparisons measur
…[truncated 4743 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 571 · 2026-05-27T08:43:13.457391+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/appendix.tex",
  "offset": "1150",
  "limit": "30"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/appendix.tex",
    "offset": "1150",
    "limit": "30"
  }
}
```

</details>

---


### Tool result

_source line 572 · 2026-05-27T08:43:13.558227+00:00_

1150	\centering
1151	\includegraphics[width=0.55\columnwidth]{figures/fig_training_dynamics.pdf}
1152	\caption{\textbf{$\Delta R^2$ across training pathways.} Each point is one architecture-suite cell; markers distinguish backbone families. Exit collapse (above dashed line) is confined to VLM-to-VLA transitions and does not intensify during VLA-to-VLA fine-tuning.}
1153	\label{fig:training_dynamics}
1154	\end{figure}
1155	
1156	\subsection{Extended Practical Implications}
1157	\label{sec:extended_practical_implications}
1158	
1159	The main text identifies three use cases for the entry-exit decomposition; here we elaborate on each.
1160	
1161	\paragraph{Checkpoint selection.}
1162	$\Delta R^2$ provides a probe-based screening signal ($> 0.10$ flags reorganization) requiring only a forward pass and a linear probe.
1163	Its wall-clock cost scales with model size rather than environment complexity, unlike rollout evaluation which requires physics simulation and multi-step execution.
1164	Practitioners can rank checkpoints by $\Delta R^2$ and reserve rollout budgets for the top candidates, substantially reducing the number of expensive closed-loop evaluations needed during model selection.
1165	
1166	\paragraph{Transfer learning strategy.}
1167	The flat VLA-to-VLA $\Delta R^2$ profile (\S\ref{sec:r2_collapse}) shows that VLA-to-VLA transitions preserve exit structure, justifying staged pipelines (VLM$\to$VLA$\to$task) that reuse the first-stage action head without re-learning exit representations.
1168	Inherited L1 routing can further serve as a frozen prior, reducing tunable parameters during domain transfer.
1169	This suggests that practitioners adapting a general-purpose VLA to a new task suite may benefit from freezing early layers while focusing capacity on mid-to-late layer adaptation.
1170	
1171	\paragraph{Mid-layer probe value.}
1172	Where exit collapse is pronounced, mid-layer representations ($R^2$ peak at L9--L11 across architectures) outperform exit-layer fea
…[truncated 774 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 573 · 2026-05-27T08:43:49.501480+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__pdf_to_images",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__pdf_to_images",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 574 · 2026-05-27T08:43:49.552081+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 575 · 2026-05-27T08:43:52.765434+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/main.pdf",
  "project": "vla-ssd",
  "pages": "7-8",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/main.pdf",
    "project": "vla-ssd",
    "pages": "7-8",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 576 · 2026-05-27T08:43:53.117229+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 7, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/_pdf_images/main_p7.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 281.4}, {\"page\": 8, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/_pdf_images/main_p8.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 344.7}], \"total_pages\": 43, \"rendered_pages\": 2, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 351
}
```

</details>

---


### Tool call

_source line 577 · 2026-05-27T08:43:56.077309+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/_pdf_images/main_p7.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/_pdf_images/main_p7.png"
  }
}
```

</details>

---


### Tool call

_source line 578 · 2026-05-27T08:43:56.278451+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/_pdf_images/main_p8.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/_pdf_images/main_p8.png"
  }
}
```

</details>

---


### Tool result

_source line 579 · 2026-05-27T08:43:56.481119+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "Read",
  "elapsed_ms": 403
}
```

</details>

---


### Tool result

_source line 580 · 2026-05-27T08:43:56.834088+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "Read",
  "elapsed_ms": 555
}
```

</details>

---


### Tool call

_source line 581 · 2026-05-27T08:44:06.221053+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/main.pdf",
  "project": "vla-ssd",
  "pages": "1,9",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/main.pdf",
    "project": "vla-ssd",
    "pages": "1,9",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 582 · 2026-05-27T08:44:06.422686+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 1, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/_pdf_images/main_p1.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 279.2}, {\"page\": 9, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/_pdf_images/main_p9.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 348.7}], \"total_pages\": 43, \"rendered_pages\": 2, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 583 · 2026-05-27T08:44:10.388600+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/_pdf_images/main_p1.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/_pdf_images/main_p1.png"
  }
}
```

</details>

---


### Tool call

_source line 584 · 2026-05-27T08:44:10.539747+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/_pdf_images/main_p9.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/_pdf_images/main_p9.png"
  }
}
```

</details>

---


### Tool result

_source line 585 · 2026-05-27T08:44:10.742533+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "Read",
  "elapsed_ms": 353
}
```

</details>

---


### Tool result

_source line 586 · 2026-05-27T08:44:11.095360+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "Read",
  "elapsed_ms": 555
}
```

</details>

---


### Tool call

_source line 587 · 2026-05-27T08:45:54.137194+00:00_

called mcp__agent-ml-research__reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__reviewer_post_to_director</summary>

```json
{
  "text": "[severity: info] 纯写作层面进攻空间评估——逐项分析\n\n**前置约束**：目视确认 §5 Discussion 已在第 9 页（与 References 同页），主体内容紧贴 8 页上限。任何文本新增都需要等量删除。这是所有建议的硬约束。\n\n---\n\n### 1. Introduction motivation — 边际收益 ~1pp，不建议动\n\n**当前写法**：以科学问题开头（\"which representational changes reflect action training vs inherited?\"），然后引 behavioral studies，然后指出 gap，然后 findings。\n\n**可改进方向**：用实践问题开钩（\"VLA practitioners lack cheap diagnostics to assess fine-tuning quality...\"），然后引出科学问题。这更贴 robotics 审稿人的关注点。\n\n**不建议动的原因**：\n- 当前 framing 在 Abstract → Intro → Method → Experiments → Discussion 全链条上内部一致\n- 改动 opening hook 有级联不一致风险\n- 实践角度已在 Discussion 中体现（ΔR² as screening signal）\n- Intro 已引 Grant (2026) 和 Haon (2025) 两篇 robotics-relevant behavioral studies 建立 relevance\n- **风险 > 收益**：2 天内改 framing 可能引入叙事裂缝\n\n### 2. Contribution statement — 边际收益 <0.5pp，不建议动\n\n**当前写法**：\n1. \"A cross-architecture representational analysis...\"（描述性）\n2. \"Evidence that R² exit collapse is associated with...\"（谨慎 hedge）\n3. \"A decomposition of VLA instruction routing into...\"（描述性）\n\n**可改进方向**：\n- \"The first cross-architecture...\" → 有 \"first\" 风险\n- \"We demonstrate that...\" → 对 N=2 过度声称\n- 加入规模数字（\"107 experiments across a 3×4 matrix\"）→ 字数膨胀\n\n**不建议动的原因**：\n当前 hedging 程度是 N=2 VLM→VLA transitions 下的正确校准。加强措辞开放审稿人攻击面（\"overclaimed given limited sample size\"）。Contribution 2 的 \"Evidence that\" 比 \"We show that\" 更安全——permutation test p=0.008 支撑 \"evidence\"，但 N=2 不支撑 \"demonstrate\"。\n\n### 3. Discussion / Broader Impact — 边际收益 ~1-2pp，**有一个微操作值得考虑**\n\n**当前写法**（14 行，2 段）：\n- Limitations 段：correlational, N=2, LIBERO-only, open-loop, underpowered correlation\n- Practical implications 段：ΔR² screening, staged pipelines, mid-layer features, uniform pruning, appendix 指向\n\n**页面硬约束**：Discussion 在第 9 页顶部，下方紧跟 References。无法加整段。\n\n**唯一可行的微操作**：将现有观察性表述改为设计指南性表述（同字数），例如：\n\n现在：\"The flat VLA-to-VLA ΔR² profile justifies staged pipelines that preserve exit structure\"\n可改：\"Practitioners adapting VLAs to new tasks should prefer staged pipelines (VLM→VLA→task) that preserve exit structure, as the flat VLA-to-VLA ΔR² profile shows this pathway does not reintroduce exit collapse\"\n\n现在：\"mid-layer features (peak at L9–L11) outperform exit-layer representations where collapse is pronounced\"\n可改：\"Where exit collapse is pronounced, we recommend using mid-layer features (L9–L11) rather than exit-layer representations for distillation or reward modeling\"\n\n这些改动把 \"we observed X\" 转为 \"we recommend Y because X\"，让论文从\"纯分析\"向\"带 actionable guideline 的分析\"偏移。字数基本持平，不触发页面溢出。\n\n**风险**：prescriptive 语气可能被审稿人攻击为\"overclaimed given no closed-loop validation\"。当前 observational 语气恰好匹配论文的 open-loop 分析 scope。\n\n**建议**：如果要做，只改 \"justifies staged pipelines\" 一句（有 VLA→VLA ΔR² 数据直接支撑），不改其他（缺直接 validation）。净收益约 1pp。\n\n### 4. Abstract — 边际收益 <0.5pp，可做一个微调\n\n**当前写法**：5 句，结构 question → method → finding → implication。关键数字（ΔR²=0.16-0.46, d=0.45-1.52）在位。\n\n**缺失**：\n- 未显式提及\"3 architectures\"的具体身份\n- 未提及 NLP controls\n- 末句 \"disentangling...\" 缺实践后果\n\n**可行微调**（不增字数）：\n\n现在：\"...suggesting this reorganization is specific to action-oriented training.\"\n可改：\"...suggesting this reorganization is specific to action-oriented training rather than a generic fine-tuning artifact (confirmed by three NLP instruction-tuning controls).\"\n\n这 +12 words 把 NLP controls 这个核心证据点提到 abstract 里，强化 specificity claim 的说服力。但需删 12 words 抵消。可从 sentence 2 删\"using layer-wise action probes, attention profiling, and counterfactual instruction perturbations to\"（方法细节在正文有，abstract 不必列举全部工具），替换为更精炼的表述。\n\n**风险**：极低。NLP controls 是论文最强防线之一，abstract 中提及属于合理信息密度。\n\n---\n\n### 综合判断\n\n| 维度 | 当前水平 | 可改进空间 | 边际中稿率提升 | 建议 |\n|------|---------|-----------|-------------|------|\n| Intro motivation | 8/10 | 换实践 hook | ~1pp | ❌ 风险过高 |\n| Contribution | 8/10 | 加强措辞 | <0.5pp | ❌ 开放攻击面 |\n| Discussion | 7/10 | 观察→指南 | ~1pp | ⚠️ 仅改 staged pipeline 一句 |\n| Abstract | 8/10 | 加 NLP controls | ~0.5pp | ✅ 低风险高信息密度 |\n\n**总计边际提升：~1.5-2pp**（从 55% → ~57%），前提是执行无误且不引入新问题。\n\n**诚实评估**：论文写作已接近该 scope 的极限。主要弱点（analysis paper at robotics venue）是结构性的，不可通过 wordsmithing 解决。上述微调是 cosmetic polish，不改变审稿人对 contribution type 的根本判断。如果 Director 决定执行，建议仅做 Abstract 微调（最低风险 + 最高信息密度收益），Discussion 改动酌情。",
  "project": "vla-ssd"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "mcp__agent-ml-research__reviewer_post_to_director",
  "tool_args": {
    "text": "[severity: info] 纯写作层面进攻空间评估——逐项分析\n\n**前置约束**：目视确认 §5 Discussion 已在第 9 页（与 References 同页），主体内容紧贴 8 页上限。任何文本新增都需要等量删除。这是所有建议的硬约束。\n\n---\n\n### 1. Introduction motivation — 边际收益 ~1pp，不建议动\n\n**当前写法**：以科学问题开头（\"which representational changes reflect action training vs inherited?\"），然后引 behavioral studies，然后指出 gap，然后 findings。\n\n**可改进方向**：用实践问题开钩（\"VLA practitioners lack cheap diagnostics to assess fine-tuning quality...\"），然后引出科学问题。这更贴 robotics 审稿人的关注点。\n\n**不建议动的原因**：\n- 当前 framing 在 Abstract → Intro → Method → Experiments → Discussion 全链条上内部一致\n- 改动 opening hook 有级联不一致风险\n- 实践角度已在 Discussion 中体现（ΔR² as screening signal）\n- Intro 已引 Grant (2026) 和 Haon (2025) 两篇 robotics-relevant behavioral studies 建立 relevance\n- **风险 > 收益**：2 天内改 framing 可能引入叙事裂缝\n\n### 2. Contribution statement — 边际收益 <0.5pp，不建议动\n\n**当前写法**：\n1. \"A cross-architecture representational analysis...\"（描述性）\n2. \"Evidence that R² exit collapse is associated with...\"（谨慎 hedge）\n3. \"A decomposition of VLA instruction routing into...\"（描述性）\n\n**可改进方向**：\n- \"The first cross-architecture...\" → 有 \"first\" 风险\n- \"We demonstrate that...\" → 对 N=2 过度声称\n- 加入规模数字（\"107 experiments across a 3×4 matrix\"）→ 字数膨胀\n\n**不建议动的原因**：\n当前 hedging 程度是 N=2 VLM→VLA transitions 下的正确校准。加强措辞开放审稿人攻击面（\"overclaimed given limited sample size\"）。Contribution 2 的 \"Evidence that\" 比 \"We show that\" 更安全——permutation test p=0.008 支撑 \"evidence\"，但 N=2 不支撑 \"demonstrate\"。\n\n### 3. Discussion / Broader Impact — 边际收益 ~1-2pp，**有一个微操作值得考虑**\n\n**当前写法**（14 行，2 段）：\n- Limitations 段：correlational, N=2, LIBERO-only, open-loop, underpowered correlation\n- Practical implications 段：ΔR² screening, staged pipelines, mid-layer features, uniform pruning, appendix 指向\n\n**页面硬约束**：Discussion 在第 9 页顶部，下方紧跟 References。无法加整段。\n\n**唯一可行的微操作**：将现有观察性表述改为设计指南性表述（同字数），例如：\n\n现在：\"The flat VLA-to-VLA ΔR² profile justifies staged pipelines that preserve exit structure\"\n可改：\"Practitioners adapting VLAs to new tasks should prefer staged pipelines (VLM→VLA→task) that preserve exit structure, as the flat VLA-to-VLA ΔR² profile shows this pathway does not reintroduce exit collapse\"\n\n现在：\"mid-layer features (peak at L9–L11) outperform exit-layer representations where collapse is pronounced\"\n可改：\"Where exit collapse is pronounced, we recommend using mid-layer features (L9–L11) rather than exit-layer representations for distillation or reward modeling\"\n\n这些改动把 \"we observed X\" 转为 \"we recommend Y because X\"，让论文从\"纯分析\"向\"带 actionable guideline 的分析\"偏移。字数基本持平，不触发页面溢出。\n\n**风险**：prescriptive 语气可能被审稿人攻击为\"overclaimed given no closed-loop validation\"。当前 observational 语气恰好匹配论文的 open-loop 分析 scope。\n\n**建议**：如果要做，只改 \"justifies staged pipelines\" 一句（有 VLA→VLA ΔR² 数据直接支撑），不改其他（缺直接 validation）。净收益约 1pp。\n\n### 4. Abstract — 边际收益 <0.5pp，可做一个微调\n\n**当前写法**：5 句，结构 question → method → finding → implication。关键数字（ΔR²=0.16-0.46, d=0.45-1.52）在位。\n\n**缺失**：\n- 未显式提及\"3 architectures\"的具体身份\n- 未提及 NLP controls\n- 末句 \"disentangling...\" 缺实践后果\n\n**可行微调**（不增字数）：\n\n现在：\"...suggesting this reorganization is specific to action-oriented training.\"\n可改：\"...suggesting this reorganization is specific to action-oriented training rather than a generic fine-tuning artifact (confirmed by three NLP instruction-tuning controls).\"\n\n这 +12 words 把 NLP controls 这个核心证据点提到 abstract 里，强化 specificity claim 的说服力。但需删 12 words 抵消。可从 sentence 2 删\"using layer-wise action probes, attention profiling, and counterfactual instruction perturbations to\"（方法细节在正文有，abstract 不必列举全部工具），替换为更精炼的表述。\n\n**风险**：极低。NLP controls 是论文最强防线之一，abstract 中提及属于合理信息密度。\n\n---\n\n### 综合判断\n\n| 维度 | 当前水平 | 可改进空间 | 边际中稿率提升 | 建议 |\n|------|---------|-----------|-------------|------|\n| Intro motivation | 8/10 | 换实践 hook | ~1pp | ❌ 风险过高 |\n| Contribution | 8/10 | 加强措辞 | <0.5pp | ❌ 开放攻击面 |\n| Discussion | 7/10 | 观察→指南 | ~1pp | ⚠️ 仅改 staged pipeline 一句 |\n| Abstract | 8/10 | 加 NLP controls | ~0.5pp | ✅ 低风险高信息密度 |\n\n**总计边际提升：~1.5-2pp**（从 55% → ~57%），前提是执行无误且不引入新问题。\n\n**诚实评估**：论文写作已接近该 scope 的极限。主要弱点（analysis paper at robotics venue）是结构性的，不可通过 wordsmithing 解决。上述微调是 cosmetic polish，不改变审稿人对 contribution type 的根本判断。如果 Director 决定执行，建议仅做 Abstract 微调（最低风险 + 最高信息密度收益），Discussion 改动酌情。",
    "project": "vla-ssd"
  }
}
```

</details>

---


### Tool result

_source line 588 · 2026-05-27T08:45:58.227422+00:00_

{"result":"{\"success\": true, \"data\": {\"director_session\": \"feishu:group:oc_a1d032cbe70bdd2058438e67e0d57613:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "mcp__agent-ml-research__reviewer_post_to_director",
  "elapsed_ms": 4090
}
```

</details>

---


### Tool call

_source line 589 · 2026-05-27T08:46:01.447357+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__cleanup_pdf_images",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__cleanup_pdf_images",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 590 · 2026-05-27T08:46:01.499174+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "ToolSearch",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 591 · 2026-05-27T08:46:05.315095+00:00_

called mcp__agent-ml-research__cleanup_pdf_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__cleanup_pdf_images</summary>

```json
{
  "output_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/_pdf_images"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "tool_args": {
    "output_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/_pdf_images"
  }
}
```

</details>

---


### Tool result

_source line 592 · 2026-05-27T08:46:05.315527+00:00_

{"result":"{\"success\": true, \"data\": {\"deleted\": 4, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "elapsed_ms": 0
}
```

</details>

---


### Assistant

_source line 593 · 2026-05-27T08:46:08.154156+00:00_

评估已发送。待机等待 Director 回复。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer"
}
```

</details>

---


## Round 25

## Round 25

2 recorded events


### User

_source line 594 · 2026-05-27T12:13:47.950748+00:00_

[WRITE HANDOFF] 请立即写你的 handoff。

**格式硬约束**:
- 整条回复**只能**是 &lt;handoff>...&lt;/handoff> 标签包裹
- 禁止在标签外写任何寒暄 / 说明 / 确认（"好的"/"我开始写"/"写完了"等）

**必须覆盖以下 5 个 section（缺一不可，无内容写 N/A）**:

### 1. 🔴 硬约束 / 红线
  本项目特定的不可违反约束（GPU 设备号、服务器名、账号、路径限制等）。
  写本项目特定的，不要抄 CLAUDE.md 通用 L1 红线。
  下一个"你"第一眼看到的就是这里，写错了会被 Director CRITICAL。

### 2. 🖥️ 基础设施快照
  - 服务器名 + 工作目录 + Python 路径 + conda env
  - 模型路径 / 数据集路径 / wandb config / HF cache
  - 活跃进程：PID + tmux session + cron 任务 ID
  写一次就稳定，下一个"你"不用再 SSH 探查。

### 3. 📊 当前状态
  - 你刚做完什么 / 正在做什么
  - registry 里 RUNNING/PREPARING 的实验列表 + 一句话摘要
  - 等待中的 Worker 回调 / Cron / Director 决策

### 4. 📋 待办（条件触发式）
  格式 "条件 X 满足 → 动作 Y"。例如:
  - "Falcon-H1R 下载完成 → sed 修 MODEL_PATH → dry-run → 提交"
  - "pilot_011 出 GC4 结果 → ≥2pp 转架构 narrative，<2pp 写 null-result"

### 5. 🎯 战略上下文
  - 项目核心结论 / 决策链（D001..）
  - 下一个"你"最容易判断错的事 / 容易踩的坑

**写作原则**：
- 第 1 节必须是项目特定的（不是通用 L1 红线）
- 第 2 节让下一轮 BOOT 后能立即开工，避免重新 SSH 探查
- 简洁 > 完整：每节 5-10 行足够，长 handoff 不等于好 handoff

示例格式:
&lt;handoff>
### 1. 🔴 硬约束 / 红线
- 本项目只能用 cuda:4 / cuda:5（之前两次违规 cuda:0 被 Director CRITICAL）
- submit_training_job 不支持 shell builtin（source/conda activate 全不行）

### 2. 🖥️ 基础设施快照
- 服务器：westd-8x6000，工作目录 /root/autodl-tmp/hybrid_reasoning_phases
- Python：/root/miniconda3/bin/python（绝对路径，不走 conda activate）
- 模型：/root/autodl-tmp/qwen35_4b_direct
- 活跃：pilot_011 (PID 203221, tmux=pilot_011, cuda:4)

### 3. 📊 当前状态
我刚完成 pilot_010 分析，正在等 pilot_011 (Falcon-H1R) CoT 生成完成（6/50）。
registry: pilot_011 RUNNING；其他全 DONE。

### 4. 📋 待办
- pilot_011 cron 回调 → spawn worker 跑 probe + GC4 计算
- GC4 ≥2pp → 转架构 narrative；<2pp → null-result paper outline 已就绪

### 5. 🎯 战略上下文
Falcon-H1R 是最后一个数据点。已知 4B/9B GC4 都 FAIL。
易错：不要把 GC4-par (Falcon parallel) 和 GC4-seq (Qwen sequential) 直接对比。
&lt;/handoff>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer",
  "source": "system:ralph_loop"
}
```

</details>

---


### Assistant

_source line 595 · 2026-05-27T12:14:35.669112+00:00_

&lt;handoff>
### 1. 🔴 硬约束 / 红线
- GPU: westd-19183 的 2× RTX PRO 6000，`gpu_ids` 需查 constraints.yaml 确认白名单（全部实验已完成，GPU 空闲待释放）
- 论文页面限制：CoRL 2026 = 8 页正文 + references。当前 §5 Discussion 已在第 9 页顶部（与 References 同页），**零空间可用**，任何正文新增必须等量删除
- 不要建议"降级 venue"——venue 决策不在 Reviewer 职责范围内
- 审"未改"类结论前必须双边核对源：论文在本地 workspace `projects/vla-ssd/docs/paper/`，训练代码/数据在远程 `/root/vla-ssd/`

### 2. 🖥️ 基础设施快照
- 服务器：westd-19183，远程代码根 `/root/vla-ssd/`
- 本地 workspace：`/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/`
- 论文源码：`projects/vla-ssd/docs/paper/`（main.tex + 7 个 .tex + figures/）
- 编译 PDF：`docs/paper/main.pdf`（最新 2026-05-27 06:54 UTC，43 页含 appendix）
- Rebuttal：`artifacts/submission_package/anticipated_rebuttal_v2.md`（Q1-Q12）
- 无活跃进程、无 tmux session、无 cron。全部 107 success 实验已完成。GPU 空闲，释放请求已提 Manager 5 次未批。
- W&B 项目存在但本轮未用（核查指标直接读 registry）

### 3. 📊 当前状态
**全部审查完成，论文提交就绪，等待用户操作 OpenReview 提交（DDL 5/29）。**

本轮（Loop #14）完成的审查：
1. Type 3 字体最终验证 → ✅ 零 Type 3（38 CID TrueType + 26 Type 1）
2. Q11 rebuttal 强化确认 → ✅ 已含 "Scientific validation of the metric" 段
3. 布局检查 → ✅ 0 critical, 8 warning（均无害）
4. 进攻性实验评估（Director 触发）→ 结论：107 实验中无值得跑的新实验，核心弱点（venue fit）不可通过实验解决
5. 纯写作层面进攻评估（Director 触发）→ 结论：写作接近该 scope 极限，总边际提升 ~1.5-2pp（55%→57%），仅 Abstract 加 NLP controls 和 Discussion staged pipeline 微调值得考虑

Registry: 0 RUNNING, 0 PREPARING。154 total (107 success / 19 negative / 12 killed / 7 failed)。无等待中的回调。

### 4. 📋 待办
- Director 批准 Abstract/Discussion 微调 → 验证修改后叙事一致性 + 重新确认页面未溢出
- 用户提交论文 → 无需 Reviewer 动作
- 审稿意见返回 → 加载 `rebuttal` skill，对照 `anticipated_rebuttal_v2.md` 逐条评估覆盖率
- Manager 批准 GPU 释放 → 无需 Reviewer 动作
- Director 转发新 framing 提案 → 加载 `negative-framing-review` skill 四维度审

### 5. 🎯 战略上下文
**核心结论**：VLM→VLA fine-tuning 引发 exit collapse（ΔR²=0.156-0.455, 6/6 cells），VLA→VLA 不引发（0/4 cells, ΔR²<0.10），NLP controls 确认 specificity（3/3, ΔR²=0.000）。L1 instruction attention 是 inherited 而非 trained。

**中稿率估计**：53-58%，median 55%。主要风险是 venue fit（analysis paper at robotics venue）。

**关键决策链**：D105（Qwen NLP control 闭合 stated limitation）→ D107（n=9 behavioral correlation 为设计硬约束，终结扩展讨论）→ D108/D110（无可跑实验，GPU 空置）→ D112（关闭 action-head decoding 实验线）

**易错点**：
1. 不要被 19 个 negative 实验吓到——已逐条审查（D110），均为 honest negative，无一值得重试
2. specificity control 只有 8% gap（d=0.65 vs 0.60）——这是 distributed routing 的证据，不是 specificity 失败。论文已正确 frame 为"instruction information woven into general residual stream"
3. NORA-Goal ΔR²=0.455 的 bootstrap CI 不可靠（exit R²≈-0.006 artifact）——论文用 footnote b 标注，核心结论不依赖此 cell（排除后 VLM→VLA range 仍 0.156-0.362）
4. 不要把 Cohen's d（action-space）和 cosine distance（representation-space）跨指标比较——论文 §4.4 已明确标注 incommensurability
&lt;/handoff>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_9e9aef1687e6abd097aa0edaf0551ee3:reviewer"
}
```

</details>

---
