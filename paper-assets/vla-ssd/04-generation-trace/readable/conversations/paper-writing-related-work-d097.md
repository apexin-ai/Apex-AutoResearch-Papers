# paper writing related work d097

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 21
- **Recorded user turns:** 0
- **Tool calls:** 10
- **Original source:** `logs/chats/worker_paper_writing_related_work_d097_20260522T060541.jsonl`
- **Structured JSON:** [`2a31f6981cd4fd992f7d.json`](../../sessions/2a/2a31f6981cd4fd992f7d.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

21 recorded events

### Tool call

_source line 1 · 2026-05-22T06:08:57.194029+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/agent-ml-research/skills/global/paper-writing-norms.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_related_work_d097_20260522T060541",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/paper-writing-norms.skill.md"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-22T06:08:57.194637+00:00_

1	---
2	name: paper-writing-norms
3	description: 顶会级别论文写作风格规范——章节写法（Abstract/Intro/Related Work）、去 AI 风格、视觉密度、叙事哲学。Paper Agent 和 Worker 写论文章节时必须加载。
4	allowed-tools: [Read, Write, Edit, Glob, Grep]
5	scope: global
6	version: 2
7	priority: 9
8	tags:
9	  - writing
10	  - paper
11	  - style
12	  - norms
13	roles:
14	  - agent
15	  - worker
16	  - paper_agent
17	---
18	
19	# 论文写作风格规范
20	
21	> 核心哲学：**论文是一个有说服力的故事，不是实验报告。** 审稿人在几十秒内判断论文价值——如果 Abstract 和 Introduction 读起来像实验日志，论文就已经失败了。
22	
23	---
24	
25	## 一、总体写作哲学
26	
27	### 1.1 故事驱动，不是数据堆砌
28	
29	- 论文必须以"故事线"为核心展开：问题 → 洞察 → 方法 → 验证
30	- 禁止大量实验数据堆砌——每个数字出现必须服务于叙事推进
31	- 附录内容必须在正文中有明确引用且融入叙事，禁止简单堆砌
32	- 如果附录数据对核心叙事有重大影响，根据附录数据调整论文 framing
33	
34	### 1.2 主线统一性
35	
36	- 当 idea 在研究过程中发生变化后，**必须重审全文逻辑**
37	- 常见问题：Introduction 讲的故事 A，Method 做的是故事 B，Results 又在讲故事 C
38	- 修复方式：从最终实验结论反推，重写 Introduction 的问题定义和动机
39	- 每次 idea 调整后检查：Abstract → Introduction → Method → Results → Discussion → Conclusion 是否形成一条连贯主线
40	
41	### 1.3 专有名词必须有定义
42	
43	- 首次出现的专有名词/缩写必须给出完整定义和解释
44	- Abstract 中使用的缩写也必须在 Abstract 内定义（如 LLM = Large Language Model）
45	- 不能假设读者知道你自己定义的术语——论文从来没解释过的概念不能直接使用
46	- 通用规则：如果一个非标准术语第一次出现时没有括号定义，就是写作 bug
47	
48	### 1.4 写作前必读同类优秀论文
49	
50	- 每个章节动笔前，找 **2-3 篇目标会议近 1-2 年的高分论文**作为风格参考——同类问题或同类方法皆可
51	- 重点学：
52	  - Abstract 怎么用最少篇幅讲完故事
53	  - Introduction 怎么从大问题切入到具体贡献
54	  - Related Work 怎么 positioning 自己（不是 survey）
55	  - Table/Figure 怎么压缩信息密度
56	- **不是抄袭**，是学习同行的故事节奏和审美——不同子领域叙事节奏差异很大
57	- 实操：Paper Agent 可以从 `literature_map.yaml` 中挑 `role=foundation` 或 `role=direct-competitor` 的论文，把 `{title, venue, year, abstract}` 附在 Worker 的 task_prompt 中作为概念参考；如需学习写作风格本身，让 Worker 通过 WebSearch 取得论文链接并 fetch 全文
58	
59	---
60	
61	## 二、Abstract 写作规范
62	
63	### 2.1 四个必答问题（150-250 words）
64	
65	Abstract 必须在很短的篇幅内清楚回答：
66	1. **研究什么问题** — 1-2 句话交代背景和痛点
67	2. **为什么重要** — 现有方法的不足（不用写太多）
68	3. **本文提出什么** — 核心贡献的关键机制（简要，不堆砌细节）
69	4. **结果说明什么** — 用具体实验结论支撑贡献
70	
71	### 2.2 禁忌
72	
73	- **禁止堆砌数据**：Abstract 不是 Results 的缩写。最多引用 2-3 个关键数字，要服务于 claim
74	- **
…[truncated 5709 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_related_work_d097_20260522T060541",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-22T06:08:57.194843+00:00_

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
  "session": "worker_paper_writing_related_work_d097_20260522T060541",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/related_work.tex"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-22T06:08:57.195089+00:00_

1	\section{Related Work}\label{sec:related_work}
2	
3	\paragraph{Vision-language-action models.}
4	VLAs fine-tune large language models on robot demonstrations to produce action tokens conditioned on visual observations and language instructions~\cite{brohan2023_rt2,kim2024_openvla,karamcheti2024,black2024_pi0}; recent work conditions action generation on dynamic visual reweighting~\cite{xiao2025ava}.
5	A central assumption is that fine-tuning injects action-relevant knowledge into pretrained representations; unlike NLP instruction tuning, which targets behavioral compliance~\cite{wei2022finetuned,ouyang2022training}, we test this at the representational level through per-layer, per-token-type decomposition.
6	Fine-tuning operates in a low intrinsic dimension~\cite{aghajanyan2021intrinsic} and can distort pretrained features~\cite{kumar2022finetuning}; our per-layer analysis reveals where restructuring concentrates and finds VLA training primarily redistributes rather than distorts, with image geometry largely preserved ($\Delta \leq 1.7\%$).
7	
8	\paragraph{Mechanistic interpretability in transformers.}
9	Mechanistic analyses have identified residual stream communication~\cite{elhage2021}, induction heads for in-context learning~\cite{olsson2022}, complete circuits for specific tasks~\cite{wang2023_ioi,conmy2023}, causal tracing for factual recall~\cite{meng2022_rome}, and the tuned lens for per-layer prediction~\cite{belrose2023_tunedlens}, while feature-level methods have scaled to dictionary learning over millions of features~\cite{bills2023language,templeton2024scaling}.
10	Attention probing reveals that individual heads encode syntactic relations~\cite{clark2019}, capture depth-dependent patterns~\cite{vig2019}, and that a small subset accounts for most performance~\cite{voita2019}; Michel et al.~\cite{michel2019sixteen} showed most heads can be pruned without loss.
11	Our L1 analysis extends this to VLAs: we use functional ablation to study attention redistri
…[truncated 2555 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_related_work_d097_20260522T060541",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-22T06:08:57.195265+00:00_

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
  "session": "worker_paper_writing_related_work_d097_20260522T060541",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/introduction.tex"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-22T06:08:57.195439+00:00_

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
…[truncated 5597 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_related_work_d097_20260522T060541",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-22T06:08:57.195633+00:00_

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
  "session": "worker_paper_writing_related_work_d097_20260522T060541",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/experiments.tex"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-22T06:08:57.195897+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Experimental Setup}
5	\label{sec:setup}
6	
7	We analyze three VLA architectures across four LIBERO~\cite{liu2023_libero} task suites (Goal, Spatial, Object, Long-Horizon) in a $3 \times 4$ cross-architecture matrix (Table~\ref{tab:cross_arch_matrix}).
8	The architectures span distinct backbone families: OpenVLA~\cite{kim2024_openvla,karamcheti2024} (Llama-2-7B~\cite{touvron2023_llama2}, 32 layers, 32 MHA heads), TracVLA~\cite{zheng2024tracevla} (Phi-3-mini~\cite{abdin2024phi3}, 32 layers, 32 heads), and NORA~\cite{TODO_nora} (Qwen2.5-VL-3B, 36 layers, GQA with 16 query heads and 2 KV heads).
9	Of the 12 matrix cells, 10 are filled; NORA Object and Long-Horizon lack available checkpoints.
10	Each architecture is compared in trained and untrained conditions, with a critical asymmetry between untrained baselines: OpenVLA's untrained checkpoint is the OXE-pretrained~\cite{padalkar2023_oxe} VLA (already fine-tuned for action prediction on 970K episodes), while TracVLA and NORA untrained checkpoints are pure vision-language models (Phi-3-Vision and Qwen2.5-VL) with no action training.
11	Three analyses are applied to each cell (\S\ref{sec:method}): $R^2$ action probes at all layers, L1 attention head profiling for instruction dominance, and counterfactual instruction perturbation.
12	For OpenVLA LIBERO-Goal, $N = 63{,}228$ observations; other cells are at comparable scale.
13	For trained models that produce action outputs, counterfactual sensitivity is measured via Cohen's $d$ on action MSE.
14	For untrained VLMs (Phi-3-Vision, Qwen2.5-VL) that do not produce actions, sensitivity is measured via cosine distance on hidden representations; these metrics operate on different scales and are not directly comparable (\S\ref{sec:cf_sensitivity}).
15	OpenVLA's OXE-pretrained checkpoint produces actions, permitting same-metric (Cohen's $d$) comparison in that condition.
16	Bonferroni correction details appear in Ap
…[truncated 22247 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_related_work_d097_20260522T060541",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-22T06:08:57.196180+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/related_work.tex",
  "content": "\\section{Related Work}\\label{sec:related_work}\n\n\\paragraph{Vision-language-action models.}\nVLAs fine-tune large language models on robot demonstrations to produce action tokens conditioned on visual observations and language instructions~\\cite{brohan2023_rt2,kim2024_openvla,karamcheti2024,black2024_pi0,zheng2024tracevla,TODO_nora}; recent work conditions action generation on dynamic visual reweighting~\\cite{xiao2025ava}.\nA central assumption is that fine-tuning injects action-relevant knowledge into pretrained representations; unlike NLP instruction tuning, which targets behavioral compliance~\\cite{wei2022finetuned,ouyang2022training}, we test this at the representational level through per-layer, per-token-type decomposition.\nFine-tuning operates in a low intrinsic dimension~\\cite{aghajanyan2021intrinsic} and can distort pretrained features~\\cite{kumar2022finetuning}; however, existing representational analyses target a single architecture and cannot distinguish training dynamics from backbone-specific artifacts.\nUnlike these prior analyses, we test representational changes across three backbone families (Llama-2, Phi-3, Qwen2.5-VL) and find that VLA training creates exit collapse and counterfactual sensitivity while L1 attention structure reflects inherited base-model priors.\n\n\\paragraph{Mechanistic interpretability in transformers.}\nMechanistic analyses have identified residual stream communication~\\cite{elhage2021}, induction heads for in-context learning~\\cite{olsson2022}, complete circuits for specific tasks~\\cite{wang2023_ioi,conmy2023}, causal tracing for factual recall~\\cite{meng2022_rome}, and the tuned lens for per-layer prediction~\\cite{belrose2023_tunedlens}, while feature-level methods have scaled to dictionary learning over millions of features~\\cite{bills2023language,templeton2024scaling}.\nAttention probing reveals that individual heads encode syntactic relations~\\cite{clark2019}, capture depth-dependent patterns~\\cite{vig2019}, and that a small subset accounts for most performance~\\cite{voita2019}; Michel et al.~\\cite{michel2019sixteen} showed most heads can be pruned without loss.\nOur L1 analysis extends this to VLAs: OpenVLA shows 24/32 instruction-dominant heads after training, but cross-architecture comparison reveals this count reflects base-model priors rather than fine-tuning (Phi-3-Vision allocates 32/32 instruction-dominant heads before any action training).\nProgressive ablation of instruction-dominant heads yields monotonic rather than threshold-like degradation.\n\n\\paragraph{Behavioral and mechanistic analysis of VLAs.}\nBehavioral evaluations reveal that current VLAs rely disproportionately on visual input~\\cite{grant2026,hou2026,fei2025}.\nMechanistic studies have identified sparse semantic directions linked to action selection~\\cite{haon2025}, interpretable features and memorized sequences~\\cite{swann2026,buurmeijer2026}, symbolic state representations~\\cite{lu2025,molinari2025}, and fine-tuning erosion of VLM reasoning~\\cite{fang2025}.\nThe closest works, Grant et al.~\\cite{grant2026} (visual dominance) and H\\\"aon et al.~\\cite{haon2025} (sparse directions), address \\emph{what} information VLAs encode; our analysis is complementary, addressing \\emph{where} instruction information is redistributed across layers and token positions, with trained-vs-untrained controls that isolate fine-tuning effects.\nPrior work in this area targets single architectures; our cross-architecture matrix (3 architectures $\\times$ 4 task suites) tests whether identified mechanisms replicate across backbone families, and distinguishes training-induced effects (exit collapse, counterfactual sensitivity) from inherited structure (L1 attention).\n\n\\paragraph{Token-level functional specialization in transformers.}\nIn Vision Transformers, the CLS token aggregates global information~\\cite{dosovitskiy2021} and certain patch positions serve as registers~\\cite{darcet2024}; in language models, feed-forward layers store factual associations in position-specific patterns~\\cite{geva2021}, probing reveals increasingly abstract features across depth~\\cite{tenney2019}, the logit lens~\\cite{nostalgebraist2020} tracks prediction evolution, and Neo et al.~\\cite{neo2025} identified task-specific neurons in multi-task LLMs.\nIn VLMs, recent work has characterized visual token sparsity and redundancy~\\cite{fan2026visual}, progressive visual-textual alignment across layers~\\cite{neo2025interpreting,long2026understanding}, and phase-structured feed-forward dynamics~\\cite{wei2024phase}.\nWe extend this to VLAs: image tokens remain instruction-blind while the readout token serves as the primary multimodal hub.\nBoth properties hold across all three architectures as structural consequences of the causal attention mask.\n\n\\paragraph{Representation similarity and probing methodology.}\nRSA~\\cite{kriegeskorte2008}, SVCCA~\\cite{raghu2017}, CCA~\\cite{morcos2018}, and Centered Kernel Alignment (CKA)~\\cite{kornblith2019} compare geometric structure between representation spaces; Raghu et al.~\\cite{raghu2021} applied these tools to compare ViT and CNN representations.\nLinear probes~\\cite{alain2017,hewitt2019,hewitt2019control,belinkov2022} complement geometric methods with functional evaluation.\nWe adopt RSA and MLP probes, with CKA in the appendix; RSA and CKA can produce divergent orderings on the same data (Appendix~\\ref{sec:cka_appendix}), and Cohen's $d$ and cosine distance are not comparable across trained and untrained conditions.\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_related_work_d097_20260522T060541",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/related_work.tex",
    "content": "\\section{Related Work}\\label{sec:related_work}\n\n\\paragraph{Vision-language-action models.}\nVLAs fine-tune large language models on robot demonstrations to produce action tokens conditioned on visual observations and language instructions~\\cite{brohan2023_rt2,kim2024_openvla,karamcheti2024,black2024_pi0,zheng2024tracevla,TODO_nora}; recent work conditions action generation on dynamic visual reweighting~\\cite{xiao2025ava}.\nA central assumption is that fine-tuning injects action-relevant knowledge into pretrained representations; unlike NLP instruction tuning, which targets behavioral compliance~\\cite{wei2022finetuned,ouyang2022training}, we test this at the representational level through per-layer, per-token-type decomposition.\nFine-tuning operates in a low intrinsic dimension~\\cite{aghajanyan2021intrinsic} and can distort pretrained features~\\cite{kumar2022finetuning}; however, existing representational analyses target a single architecture and cannot distinguish training dynamics from backbone-specific artifacts.\nUnlike these prior analyses, we test representational changes across three backbone families (Llama-2, Phi-3, Qwen2.5-VL) and find that VLA training creates exit collapse and counterfactual sensitivity while L1 attention structure reflects inherited base-model priors.\n\n\\paragraph{Mechanistic interpretability in transformers.}\nMechanistic analyses have identified residual stream communication~\\cite{elhage2021}, induction heads for in-context learning~\\cite{olsson2022}, complete circuits for specific tasks~\\cite{wang2023_ioi,conmy2023}, causal tracing for factual recall~\\cite{meng2022_rome}, and the tuned lens for per-layer prediction~\\cite{belrose2023_tunedlens}, while feature-level methods have scaled to dictionary learning over millions of features~\\cite{bills2023language,templeton2024scaling}.\nAttention probing reveals that individual heads encode syntactic relations~\\cite{clark2019}, capture depth-dependent patterns~\\cite{vig2019}, and that a small subset accounts for most performance~\\cite{voita2019}; Michel et al.~\\cite{michel2019sixteen} showed most heads can be pruned without loss.\nOur L1 analysis extends this to VLAs: OpenVLA shows 24/32 instruction-dominant heads after training, but cross-architecture comparison reveals this count reflects base-model priors rather than fine-tuning (Phi-3-Vision allocates 32/32 instruction-dominant heads before any action training).\nProgressive ablation of instruction-dominant heads yields monotonic rather than threshold-like degradation.\n\n\\paragraph{Behavioral and mechanistic analysis of VLAs.}\nBehavioral evaluations reveal that current VLAs rely disproportionately on visual input~\\cite{grant2026,hou2026,fei2025}.\nMechanistic studies have identified sparse semantic directions linked to action selection~\\cite{haon2025}, interpretable features and memorized sequences~\\cite{swann2026,buurmeijer2026}, symbolic state representations~\\cite{lu2025,molinari2025}, and fine-tuning erosion of VLM reasoning~\\cite{fang2025}.\nThe closest works, Grant et al.~\\cite{grant2026} (visual dominance) and H\\\"aon et al.~\\cite{haon2025} (sparse directions), address \\emph{what} information VLAs encode; our analysis is complementary, addressing \\emph{where} instruction information is redistributed across layers and token positions, with trained-vs-untrained controls that isolate fine-tuning effects.\nPrior work in this area targets single architectures; our cross-architecture matrix (3 architectures $\\times$ 4 task suites) tests whether identified mechanisms replicate across backbone families, and distinguishes training-induced effects (exit collapse, counterfactual sensitivity) from inherited structure (L1 attention).\n\n\\paragraph{Token-level functional specialization in transformers.}\nIn Vision Transformers, the CLS token aggregates global information~\\cite{dosovitskiy2021} and certain patch positions serve as registers~\\cite{darcet2024}; in language models, feed-forward layers store factual associations in position-specific patterns~\\cite{geva2021}, probing reveals increasingly abstract features across depth~\\cite{tenney2019}, the logit lens~\\cite{nostalgebraist2020} tracks prediction evolution, and Neo et al.~\\cite{neo2025} identified task-specific neurons in multi-task LLMs.\nIn VLMs, recent work has characterized visual token sparsity and redundancy~\\cite{fan2026visual}, progressive visual-textual alignment across layers~\\cite{neo2025interpreting,long2026understanding}, and phase-structured feed-forward dynamics~\\cite{wei2024phase}.\nWe extend this to VLAs: image tokens remain instruction-blind while the readout token serves as the primary multimodal hub.\nBoth properties hold across all three architectures as structural consequences of the causal attention mask.\n\n\\paragraph{Representation similarity and probing methodology.}\nRSA~\\cite{kriegeskorte2008}, SVCCA~\\cite{raghu2017}, CCA~\\cite{morcos2018}, and Centered Kernel Alignment (CKA)~\\cite{kornblith2019} compare geometric structure between representation spaces; Raghu et al.~\\cite{raghu2021} applied these tools to compare ViT and CNN representations.\nLinear probes~\\cite{alain2017,hewitt2019,hewitt2019control,belinkov2022} complement geometric methods with functional evaluation.\nWe adopt RSA and MLP probes, with CKA in the appendix; RSA and CKA can produce divergent orderings on the same data (Appendix~\\ref{sec:cka_appendix}), and Cohen's $d$ and cosine distance are not comparable across trained and untrained conditions.\n"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-22T06:08:57.196367+00:00_

&lt;tool_use_error>File has been modified since read, either by the user or by a linter. Read it again before attempting to write it.&lt;/tool_use_error>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_related_work_d097_20260522T060541",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-22T06:08:57.196494+00:00_

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
  "session": "worker_paper_writing_related_work_d097_20260522T060541",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/related_work.tex"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-22T06:08:57.196650+00:00_

1	\section{Related Work}\label{sec:related_work}
2	
3	\paragraph{Vision-language-action models.}
4	VLAs fine-tune large language models on robot demonstrations to produce action tokens conditioned on visual observations and language instructions~\cite{brohan2023_rt2,kim2024_openvla,karamcheti2024,black2024_pi0,zheng2024tracevla,TODO_nora}; recent work conditions action generation on dynamic visual reweighting~\cite{xiao2025ava}.
5	A central assumption is that fine-tuning injects action-relevant knowledge into pretrained representations; unlike NLP instruction tuning, which targets behavioral compliance~\cite{wei2022finetuned,ouyang2022training}, we test this at the representational level through per-layer, per-token-type decomposition across three distinct backbone families.
6	Fine-tuning operates in a low intrinsic dimension~\cite{aghajanyan2021intrinsic} and can distort pretrained features~\cite{kumar2022finetuning}; our cross-architecture analysis reveals that VLA training creates exit-layer reorganization and instruction sensitivity while preserving inherited early-layer attention structure and image geometry ($\Delta \leq 1.7\%$ on OpenVLA).
7	
8	\paragraph{Mechanistic interpretability in transformers.}
9	Mechanistic analyses have identified residual stream communication~\cite{elhage2021}, induction heads for in-context learning~\cite{olsson2022}, complete circuits for specific tasks~\cite{wang2023_ioi,conmy2023}, causal tracing for factual recall~\cite{meng2022_rome}, and the tuned lens for per-layer prediction~\cite{belrose2023_tunedlens}, while feature-level methods have scaled to dictionary learning over millions of features~\cite{bills2023language,templeton2024scaling}.
10	Attention probing reveals that individual heads encode syntactic relations~\cite{clark2019}, capture depth-dependent patterns~\cite{vig2019}, and that a small subset accounts for most performance~\cite{voita2019}; Michel et al.~\cite{michel2019sixteen} showed most heads can be pruned wit
…[truncated 3191 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_related_work_d097_20260522T060541",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-22T06:08:57.196852+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/related_work.tex",
  "old_string": "our cross-architecture analysis reveals that VLA training creates exit-layer reorganization and instruction sensitivity while preserving inherited early-layer attention structure and image geometry ($\\Delta \\leq 1.7\\%$ on OpenVLA).",
  "new_string": "however, existing representational analyses target a single architecture and cannot distinguish training dynamics from backbone-specific artifacts.\nUnlike these prior analyses, we test representational changes across three backbone families (Llama-2, Phi-3, Qwen2.5-VL) and find that VLA training creates exit collapse and counterfactual sensitivity while L1 attention structure reflects inherited base-model priors."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_related_work_d097_20260522T060541",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/related_work.tex",
    "old_string": "our cross-architecture analysis reveals that VLA training creates exit-layer reorganization and instruction sensitivity while preserving inherited early-layer attention structure and image geometry ($\\Delta \\leq 1.7\\%$ on OpenVLA).",
    "new_string": "however, existing representational analyses target a single architecture and cannot distinguish training dynamics from backbone-specific artifacts.\nUnlike these prior analyses, we test representational changes across three backbone families (Llama-2, Phi-3, Qwen2.5-VL) and find that VLA training creates exit collapse and counterfactual sensitivity while L1 attention structure reflects inherited base-model priors."
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-22T06:08:57.197047+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/related_work.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_related_work_d097_20260522T060541",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-22T06:08:57.197179+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/related_work.tex",
  "old_string": "tests whether identified mechanisms replicate across backbone families and distinguishes training-induced effects from inherited base-model priors.",
  "new_string": "tests whether identified mechanisms replicate across backbone families, and distinguishes training-induced effects (exit collapse, counterfactual sensitivity) from inherited structure (L1 attention)."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_related_work_d097_20260522T060541",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/related_work.tex",
    "old_string": "tests whether identified mechanisms replicate across backbone families and distinguishes training-induced effects from inherited base-model priors.",
    "new_string": "tests whether identified mechanisms replicate across backbone families, and distinguishes training-induced effects (exit collapse, counterfactual sensitivity) from inherited structure (L1 attention)."
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-22T06:08:57.197332+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/related_work.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_related_work_d097_20260522T060541",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-22T06:08:57.197456+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/related_work.tex",
  "old_string": "We adopt RSA and MLP probes, with CKA in the appendix; the divergence between RSA and CKA on our data (\\S\\ref{sec:routing_synthesis}) illustrates metric sensitivity in representational analysis.",
  "new_string": "We adopt RSA and MLP probes, with CKA in the appendix; RSA and CKA can produce divergent orderings on the same data (Appendix~\\ref{sec:cka_appendix}), and Cohen's $d$ and cosine distance are not comparable across trained and untrained conditions (\\S\\ref{sec:cf_sensitivity})."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_related_work_d097_20260522T060541",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/related_work.tex",
    "old_string": "We adopt RSA and MLP probes, with CKA in the appendix; the divergence between RSA and CKA on our data (\\S\\ref{sec:routing_synthesis}) illustrates metric sensitivity in representational analysis.",
    "new_string": "We adopt RSA and MLP probes, with CKA in the appendix; RSA and CKA can produce divergent orderings on the same data (Appendix~\\ref{sec:cka_appendix}), and Cohen's $d$ and cosine distance are not comparable across trained and untrained conditions (\\S\\ref{sec:cf_sensitivity})."
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-22T06:08:57.197610+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/related_work.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_related_work_d097_20260522T060541",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-22T06:08:57.197742+00:00_

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
  "session": "worker_paper_writing_related_work_d097_20260522T060541",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/related_work.tex"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-22T06:08:57.197890+00:00_

1	\section{Related Work}\label{sec:related_work}
2	
3	\paragraph{Vision-language-action models.}
4	VLAs fine-tune large language models on robot demonstrations to produce action tokens conditioned on visual observations and language instructions~\cite{brohan2023_rt2,kim2024_openvla,karamcheti2024,black2024_pi0,zheng2024tracevla,TODO_nora}; recent work conditions action generation on dynamic visual reweighting~\cite{xiao2025ava}.
5	A central assumption is that fine-tuning injects action-relevant knowledge into pretrained representations; unlike NLP instruction tuning, which targets behavioral compliance~\cite{wei2022finetuned,ouyang2022training}, we test this at the representational level through per-layer, per-token-type decomposition across three distinct backbone families.
6	Fine-tuning operates in a low intrinsic dimension~\cite{aghajanyan2021intrinsic} and can distort pretrained features~\cite{kumar2022finetuning}; however, existing representational analyses target a single architecture and cannot distinguish training dynamics from backbone-specific artifacts.
7	Unlike these prior analyses, we test representational changes across three backbone families (Llama-2, Phi-3, Qwen2.5-VL) and find that VLA training creates exit collapse and counterfactual sensitivity while L1 attention structure reflects inherited base-model priors.
8	
9	\paragraph{Mechanistic interpretability in transformers.}
10	Mechanistic analyses have identified residual stream communication~\cite{elhage2021}, induction heads for in-context learning~\cite{olsson2022}, complete circuits for specific tasks~\cite{wang2023_ioi,conmy2023}, causal tracing for factual recall~\cite{meng2022_rome}, and the tuned lens for per-layer prediction~\cite{belrose2023_tunedlens}, while feature-level methods have scaled to dictionary learning over millions of features~\cite{bills2023language,templeton2024scaling}.
11	Attention probing reveals that individual heads encode syntactic relations~\cite{clark2019}, capture
…[truncated 3512 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_related_work_d097_20260522T060541",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 21 · 2026-05-22T06:08:57.198104+00:00_

D097 compliance check:
- "architecture-independent": absent
- "7-10×": absent
- L1 attention = base-model prior (line 12: "reflects base-model language priors rather than VLA training, since Phi-3-Vision saturates at 32/32 before any action training")
- "significantly" without stats: absent
- NORA `\cite{TODO_nora}`, TracVLA `\cite{zheng2024tracevla}`: correct (line 4)
- No em-dashes: confirmed
- No -ing phrase endings: confirmed

All 5 paragraphs updated:
1. **VLA models**: added TracVLA/NORA, cross-architecture positioning, replaced "redistributes rather than distorts" with "exit collapse and counterfactual sensitivity while L1 attention reflects inherited base-model priors"
2. **Mechanistic interp**: D097-corrected L1 claim (24/32 is base-model prior, not training effect)
3. **Behavioral/mechanistic VLA**: cross-architecture matrix positioning, explicit training-induced vs inherited decomposition
4. **Token-level**: cross-architecture confirmation of instruction-blindness and readout integration
5. **RSA/probing**: added metric limitations (RSA/CKA divergence + Cohen's d/cosine incomparability)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_paper_writing_related_work_d097_20260522T060541"
}
```

</details>

---
