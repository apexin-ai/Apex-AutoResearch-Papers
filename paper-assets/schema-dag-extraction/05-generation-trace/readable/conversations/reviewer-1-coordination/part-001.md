# Reviewer 1 coordination — Part 1 of 5

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Conversation logs

[Transcript overview](../reviewer-1-coordination.md) · [Part 2 →](part-002.md) · [Structured JSON](../../../sessions/d1/d148805112ce41231b9b.json)

## Round 1

## Round 1

28 recorded events


### User

_source line 1 · 2026-05-16T00:53:34.104070+00:00_

[Round 1 审稿请求]:
## Round 1 审稿任务 — Reviewer 1（方法严谨性）

**论文：** "Does Type Confusability Drive Schema-Induced Degradation in Training-Free LLM Information Extraction?"
**Venue：** EMNLP 2026 Main Conference（ARR May 25 cycle）
**格式要求：** 长文 8 页 + 无限参考文献，ACL 模板，double-blind，mandatory Limitations section，Responsible NLP Research Checklist
**论文路径：** `projects/schema-dag-extraction/docs/paper/main.tex`（各章节在同目录下：abstract.tex, introduction.tex, related_work.tex, experimental_setup.tex, results.tex, sdgd_negative.tex, discussion.tex；Limitations 在 main.tex 内）

### 你的审查侧重

**1. 实验设计与统计方法**
- 两个实验范式（count curves + BCS-controlled）的设计是否合理？是否真正隔离了 count 和 confusability？
- BCS-controlled 实验中 low-BCS vs high-BCS batch 的构造是否有偏？样本量（5 batches/count level, 27 total）是否足够？
- Bootstrap CI 的使用是否恰当？是否有应报而未报的统计检验？
- 16-rel 到 80-rel 的 3.4× amplification 是两点比较，统计可靠性如何？
- Pairwise correlation r=0.112 (r²=1.3%) 的效应量是否被过度解读？

**2. 评估指标**
- 三个任务使用不同评估指标（text-match F1, accuracy, relaxed F1）是否合理？跨任务可比性如何？
- NER 的 text-match 而非 exact span match 评估是否引入偏差？
- MAVEN relaxed F1 的定义是否足够严格？

**3. 可复现性**
- 实验细节是否充分？（模型配置、prompt 模板、decoding 参数、随机种子）
- v1/v2 prompt 切换的处理是否透明？
- Cross-model validation (Llama-3.1-8B) 的覆盖范围是否充分？

**4. SDGD 负面结果**
- Merge amplification 的分析是否充分？是否遗漏了可能的 merge 策略？
- 负面结果的呈现是否公平客观？

请按以下格式输出审稿报告：
- Summary (2-3 句)
- Strengths (逐条)
- Weaknesses (逐条，标注 [Must-Fix] 或 [Should-Fix] 或 [Minor])
- Questions (需要作者澄清的)
- Overall Assessment (strong reject / weak reject / borderline / weak accept / strong accept + 简要理由)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 2 · 2026-05-16T00:53:42.833452+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebSearch,mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebSearch,mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director",
    "max_results": "3"
  }
}
```

</details>

---


### Tool result

_source line 3 · 2026-05-16T00:53:42.884102+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 4 · 2026-05-16T00:53:47.373354+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL ARR review form criteria 2025 2026 reviewer guidelines scoring"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR review form criteria 2025 2026 reviewer guidelines scoring"
  }
}
```

</details>

---


### Tool call

_source line 5 · 2026-05-16T00:53:49.281861+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 6 · 2026-05-16T00:53:50.137966+00:00_

1	\documentclass[11pt]{article}
2	
3	\usepackage[review]{acl}
4	
5	\usepackage{times}
6	\usepackage{latexsym}
7	\usepackage[T1]{fontenc}
8	\usepackage[utf8]{inputenc}
9	\usepackage{microtype}
10	\usepackage{graphicx}
11	\usepackage{booktabs}
12	\usepackage{amsmath}
13	\usepackage{enumitem}
14	
15	\title{Does Type Confusability Drive Schema-Induced Degradation\\in Training-Free LLM Information Extraction?}
16	
17	\author{Anonymous}
18	
19	\begin{document}
20	\maketitle
21	
22	\input{abstract}
23	
24	\input{introduction}
25	
26	\input{related_work}
27	
28	\input{experimental_setup}
29	
30	\input{results}
31	
32	\input{sdgd_negative}
33	
34	\input{discussion}
35	
36	\section*{Limitations}
37	The primary experiments use Qwen3-32B. Channel~1 (count effect) has been validated on Meta-Llama-3.1-8B-Instruct (recall decline $-$43\,pp, per-batch $r = 0.725$ with Qwen3-32B). Channel~2 was validated cross-model on FewRel RE: Llama-3.1-8B-Instruct shows $\Delta = -27.1$\,pp at count 8 and $-23.9$\,pp at count 16, comparable to Qwen3-32B's $-31.2$\,pp. High-BCS accuracy is model-invariant ($\approx$0.51), with cross-model divergence confined to the low-BCS regime. On Few-NERD NER, the effect was not robustly detectable, likely due to floor effects at 8B scale and the noisier text-match metric. The pairwise confusability signal explains roughly 1.3--1.7\% of the variance in type confusion---entity frequency, prompt position effects, and type definition quality likely contribute to the remaining variance. Our decomposition experiments test only union-based merge strategies; calibration-aware or joint-decoding alternatives remain unexplored. We conducted a within-dataset $2\!\times\!2$ factorial analysis (count $\times$ BCS) on Few-NERD; the interaction term was directionally consistent but not statistically significant ($z = -0.67$, $p = 0.50$), possibly due to BCS range compression in high-count schemas. The primary evidence for count--confusability interaction remains the $3.4\ti
…[truncated 3802 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 856
}
```

</details>

---


### Tool call

_source line 7 · 2026-05-16T00:53:50.389521+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 8 · 2026-05-16T00:53:50.390021+00:00_

1	\begin{abstract}
2	Training-free LLM information extraction---prompting models with target schemas without fine-tuning---degrades sharply as schema complexity grows: NER recall drops from 0.72 to 0.42 with 64 candidate types, and RE accuracy falls from 85.7\% to 50.4\% with 80 relations. Prior work conflates type count with type confusability, leaving the mechanisms unclear. We conduct the first controlled empirical study isolating these factors across three IE tasks and three datasets, introducing the Schema Confusability Score (SCS) and two experimental paradigms: count curves that vary schema size while randomizing confusability, and BCS-controlled experiments that fix size while varying confusability. Our experiments reveal two degradation channels: a count channel that suppresses recall as candidate types increase, and a confusability channel where semantically similar types trigger intra-batch substitution errors---cleanly separable in RE but interacting in NER. Confusability effects amplify $3.4\times$ as schema size grows from 16 to 80 types, with accuracy gaps widening from 9.1 to 31.2 percentage points. Both channels replicate on Llama-3.1-8B (count $r = 0.725$; confusability $\Delta = -27$\,pp), with high-BCS accuracy converging to a model-invariant floor. Our confusability-aware decomposition yields an informative negative result: merge amplification destroys precision across all strategies, identifying a structural bottleneck for decompose-then-merge pipelines in zero-shot IE.
3	\end{abstract}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 9 · 2026-05-16T00:53:50.491160+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 10 · 2026-05-16T00:53:50.541977+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	Training-free LLM information extraction---prompting a large language model with a target schema and asking it to extract structured information without any task-specific fine-tuning---enables rapid deployment across new domains and ontologies. This zero-shot paradigm eliminates the need for labeled data, making it attractive for applications where annotation is expensive or schemas evolve frequently \cite{llm4ie-survey-2024}. Yet the paradigm carries a critical limitation: performance degrades sharply as the number of candidate types in the prompt schema grows. On named entity recognition, recall drops from 0.72 with a single candidate type to 0.42 with 64 types, a 42\% relative decline. On relation extraction, accuracy falls from 85.7\% with one relation to 50.4\% with 80 relations---near halving. This degradation is not academic: real-world ontologies routinely define 50--200+ types, placing them squarely in the regime where training-free extraction becomes unreliable.
5	
6	What causes this schema-induced degradation? Prior work has proposed decomposition strategies that implicitly assume different answers. \citet{uniner-2024} extract each type independently, assuming types can be treated as separable. \citet{llm-pee-2025} partition large event schemas by type embedding similarity before extraction, assuming that semantic overlap between co-presented types drives errors. \citet{parse-2025} rewrite and optimize schema definitions, assuming that description quality is the bottleneck. Each approach improves extraction under certain conditions, but none isolates \emph{why} schemas degrade performance in the first place. The closest work, LLM-PEE \cite{llm-pee-2025}, reduces both the number of co-presented types and their inter-type similarity simultaneously, making it impossible to determine which factor---or what combination---accounts for the observed gains. More broadly, all prior approaches conflate two dis
…[truncated 3551 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 11 · 2026-05-16T00:53:54.661156+00:00_

Web search results for query: "ACL ARR review form criteria 2025 2026 reviewer guidelines scoring"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"aclrollingreview/reviewerguidelines.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/reviewerguidelines.md"},{"title":"ACLRollingReview (@ReviewAcl) / X","url":"https://x.com/reviewacl"}]

Based on the search results, here's the key information about ACL ARR review form criteria, reviewer guidelines, and scoring for 2025-2026:

## Reviewer Scoring System

Starting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation. The soundness scores 
…[truncated 1366 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 7287
}
```

</details>

---


### Tool call

_source line 12 · 2026-05-16T00:54:00.034620+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 13 · 2026-05-16T00:54:00.490985+00:00_

1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\subsection{Training-Free LLM Information Extraction}
5	\label{sec:rw_training_free}
6	
7	Recent surveys categorize LLM-based IE along instruction-tuning and code-generation axes \cite{llm4ie-survey-2024}. Approaches span instruction tuning for unified IE \cite{instructuie-2023}, code-style schema encoding \cite{knowcoder-2024,codeie-2023}, annotation-guided zero-shot extraction \cite{gollie-2024,adelie-2024}, and schema-driven decoding \cite{slot-2025,oneke-2025}. For NER, methods include zero-shot decomposition by entity type \cite{xie-zeroshot-ner-2023,promptner-2023}, ChatGPT distillation \cite{uniner-2024}, bidirectional transformers \cite{gliner-2024,gliner2-2025}, self-improvement \cite{self-improve-ner-2024}, type descriptions \cite{zeroner-2025}, and guided synthesis \cite{guidex-2025,nuner-2024}. Relation extraction benefits from self-prompting \cite{self-prompting-re-2024} and retrieval-augmented code generation \cite{code4uie-2024}. \citet{familiarity-2025} highlight evaluation pitfalls by quantifying label shifts in zero-shot NER. Separately, constrained decoding via JSON schema enforcement \cite{json-schema-bench-2025} guarantees structurally valid outputs; all our experiments use vLLM's constrained JSON decoding (\S\ref{sec:model}).
8	
9	These methods perform well with moderate schemas (4--20 types) but none investigates how performance degrades as schema complexity scales, nor proposes quantitative metrics for inter-type confusability. Our work fills both gaps.
10	
11	\subsection{Schema Complexity in IE}
12	\label{sec:rw_schema}
13	
14	The most directly related work is LLM-PEE \cite{llm-pee-2025}, which addresses event extraction with massive type inventories by partitioning schemas based on type embedding similarity. LLM-PEE clusters event types and assigns each cluster to a separate extraction prompt, demonstrating improved performance on schemas with hundreds of types. Our work is complement
…[truncated 2472 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 455
}
```

</details>

---


### Tool call

_source line 14 · 2026-05-16T00:54:00.542961+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/experimental_setup.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/experimental_setup.tex"
  }
}
```

</details>

---


### Tool result

_source line 15 · 2026-05-16T00:54:00.947702+00:00_

1	\section{Experimental Setup}
2	\label{sec:experimental_setup}
3	
4	We evaluate how prompt schema size and inter-type confusability affect zero-shot LLM extraction across three information extraction tasks: named entity recognition (NER), relation extraction (RE), and event detection (ED).
5	
6	\subsection{Tasks and Datasets}
7	\label{sec:datasets}
8	
9	\paragraph{Few-NERD (NER).}
10	Few-NERD \cite{fewnerd-2021} provides 66 fine-grained entity types organized into 8 coarse categories (person, location, organization, building, art, product, event, other). The dataset spans diverse domains, making it suitable for cross-domain evaluation. We sample 1{,}000 test instances and evaluate with token-level text matching.
11	
12	\paragraph{FewRel (RE).}
13	FewRel \cite{fewrel-2018} contains 80 relation types sourced from Wikidata. Since the validation split covers only 16 relations, we combine the training and validation splits to obtain the full 80-relation pool required for schema-scale experiments, and sample 1{,}000 balanced instances. Each instance provides a sentence with marked head and tail entities; the task is to classify the relation.
14	
15	\paragraph{MAVEN (ED).}
16	MAVEN \cite{maven-2020} defines 168 event types derived from the FrameNet ontology, making it a same-domain schema. We use the validation set (8{,}042 sentences containing 18{,}904 event mentions) for evaluation, as test set labels are not publicly available. The task requires both trigger identification and event type classification.
17	
18	Table~\ref{tab:datasets} summarizes the dataset statistics, including the Schema Confusability Score (SCS) ranges defined in \S\ref{sec:scs}.
19	
20	\begin{table}[t]
21	\centering
22	\small
23	\resizebox{\columnwidth}{!}{%
24	\begin{tabular}{llrrlll}
25	\toprule
26	\textbf{Dataset} & \textbf{Task} & \textbf{\# Types} & \textbf{\# Eval Units} & \textbf{Domain} & \textbf{BCS Range} & \textbf{Embedding} \\
27	\midrule
28	Few-NERD & NER & 66 & 1{,}000 & Cross & 0.77-
…[truncated 6755 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 404
}
```

</details>

---


### Tool call

_source line 16 · 2026-05-16T00:54:01.098780+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex"
  }
}
```

</details>

---


### Tool result

_source line 17 · 2026-05-16T00:54:01.450987+00:00_

1	\section{Results}
2	\label{sec:results}
3	
4	\subsection{Count-Degradation Curves}
5	\label{sec:count_curves}
6	
7	We first examine how extraction performance changes as the number of types in the prompt schema increases (Experiment~1; see Figure~\ref{fig:count_curves} in the Appendix for visualizations).
8	
9	\paragraph{NER (Few-NERD).}
10	Recall generally declines from 0.72 at count${}\,=\,1$ to 0.42 at count${}\,=\,64$, a 42\% relative drop, with minor non-monotonicity at intermediate counts (e.g., 0.527 at count${}\,=\,22$ to 0.551 at count${}\,=\,44$). Precision moves in the opposite direction, rising from 0.11 to 0.52, reflecting a shift from over-prediction to under-prediction as more candidate types compete in the prompt. F1 exhibits an inverted-U shape, peaking at intermediate counts where the precision--recall trade-off is most balanced.
11	
12	\paragraph{RE (FewRel).}
13	Accuracy drops monotonically from 85.7\% at count${}\,=\,1$ through 58.8\% at count${}\,=\,40$ to 50.4\% at count${}\,=\,80$, a near-halving when the model must discriminate among all 80 relation types simultaneously. (The count${}\,=\,40$ evaluation uses 40-relation subsets sampled from the 80-relation pool, not an independent schema.)
14	
15	\paragraph{ED (MAVEN).}
16	In contrast to NER and RE, MAVEN relaxed F1 \emph{increases} from 0.106 at count${}\,=\,1$ to 0.247 at count${}\,=\,44$. This reversal arises from three properties of the MAVEN setup: (i)~trigger-level relaxed matching, which requires only token overlap rather than exact span match; (ii)~MAVEN's 168 event types derive from the FrameNet ontology, forming a same-domain hierarchy where co-presented types provide disambiguating context; and (iii)~extreme class imbalance---rare event types benefit from being presented alongside related types that prime the model toward the correct semantic region. We investigate this reversal further in \S\ref{sec:centrality_confound}.
17	
18	\paragraph{Cross-model replication.}
19	Channel~1 
…[truncated 12248 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 352
}
```

</details>

---


### Tool call

_source line 18 · 2026-05-16T00:54:01.451392+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/sdgd_negative.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/sdgd_negative.tex"
  }
}
```

</details>

---


### Tool result

_source line 19 · 2026-05-16T00:54:02.456423+00:00_

1	\section{Why Naive Decomposition Fails}
2	\label{sec:sdgd}
3	
4	The multi-channel degradation model (\S\ref{sec:results}) raises an interventional question: if confusability drives type confusion, can we decompose the schema so that confusable types never co-occur in the same prompt?  We test this idea with \textbf{Schema-DAG-Guided Decomposition} (SDGD), a method that uses the pairwise SCS matrix to partition types into low-confusability batches, runs extraction independently on each batch, and merges the results.
5	
6	\paragraph{Decomposition protocol.}
7	We construct a thresholded confusability graph $G = (V, E)$ where each type is a vertex and an edge connects types $t_i, t_j$ whenever $\text{SCS}(t_i, t_j) > \tau$. Greedy graph coloring (\textsc{largest\_first}) assigns each type to a color such that no two adjacent---i.e., highly confusable---types share a color. Each color class forms one extraction batch, and predictions are merged via set union. We compare four modes: (i)~\textbf{single\_pass}, the undecomposed baseline; (ii)~\textbf{sdgd\_zero}, SCS-guided partitioning; (iii)~\textbf{random\_batch}, random partitioning with matched batch sizes; and (iv)~\textbf{per\_type}, the extreme case where each type is extracted in isolation, following the strategy of \citet{uniner-2024}. Table~\ref{tab:sdgd_results} summarizes the results on Few-NERD.
8	
9	\paragraph{All decomposition modes degrade F1.}
10	Table~\ref{tab:sdgd_results} reports the outcome.  Single-pass extraction achieves F1\,=\,0.445 (P\,=\,0.563, R\,=\,0.368).  SDGD obtains F1\,=\,0.251 (P\,=\,0.210, R\,=\,0.314), a 44\% relative drop.  Random batching reaches F1\,=\,0.320 (P\,=\,0.249, R\,=\,0.446), and per-type extraction yields F1\,=\,0.292 (P\,=\,0.194, R\,=\,0.586).  Every decomposition mode falls below the single-pass baseline.
11	
12	\begin{table}[t]
13	\centering
14	\small
15	\resizebox{\columnwidth}{!}{%
16	\begin{tabular}{lrccc}
17	\toprule
18	\textbf{Mode} & \textbf{\# Batches} & \text
…[truncated 3015 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1005
}
```

</details>

---


### Tool call

_source line 20 · 2026-05-16T00:54:02.457031+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 21 · 2026-05-16T00:54:02.909523+00:00_

1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	We isolated schema-induced degradation into count-driven recall decline and confusability-driven type confusion, showed these channels are separable in RE but interact in NER, and confirmed that both channels replicate across model families on RE (Meta-Llama-3.1-8B-Instruct: count $r = 0.725$, confusability $\Delta = -27$\,pp), with high-BCS accuracy converging to a model-invariant floor. We further identified a centrality confound on same-domain schemas and demonstrated that merge amplification is the bottleneck for decompose-then-merge pipelines. Cross-batch calibration or joint decoding is the key next step.
5	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 22 · 2026-05-16T00:54:02.910012+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebFetch",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebFetch",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 23 · 2026-05-16T00:54:02.960648+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 24 · 2026-05-16T00:54:08.435527+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete review form criteria, scoring scales, and all dimensions that reviewers must evaluate. Include the exact scale descriptions for soundness, excitement, overall recommendation, and any other scored dimensions."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the complete review form criteria, scoring scales, and all dimensions that reviewers must evaluate. Include the exact scale descriptions for soundness, excitement, overall recommendation, and any other scored dimensions."
  }
}
```

</details>

---


### Tool result

_source line 25 · 2026-05-16T00:54:14.711966+00:00_

# ACL Rolling Review Form - Complete Evaluation Criteria

## Primary Scored Dimensions

### Reviewer Confidence
Scale 1-5, where:
- **5**: "Positive that my evaluation is correct. I read the paper very carefully and am familiar with related work."
- **4**: "Quite sure. I tried to check the important points carefully."
- **3**: "Pretty sure, but there's a chance I missed something."
- **2**: "Willing to defend my evaluation, but it is fairly likely that I missed some details."
- **1**: "Not my area, or paper is very hard to understand."

### Soundness
Scale 1-5 (with .5 increments):
- **5**: "This study is one of the most thorough I have seen, given its type."
- **4**: "This study provides sufficient support for all of its claims."
- **3**: "This study provides sufficient support for its main claims."
- **2**: "Some of the main claims are not sufficiently supported."
- **1**: "This study is not yet sufficiently thorough to warrant publication."

### Excitement
Scale 1-5 (with .5 increments):
- **5**: "I would recommend this paper to others and/or attend its presentation."
- **4**: "I would mention this paper to others and/or make an effort to attend."
- **3**: "I might mention some points of this paper to others."
- **2**: "Does not resonate with me, but it might with others."
- **1**: "Does not resonate with me, and I don't think it would with others."

### Overall Assessment
Scale 1-5 (with .5 increments):
- **5**: Consider for Award (top 2.5%)
- **4**: Conference acceptance
- **3**: Findings acceptance
- **2**: Resubmit next cycle
- **1**: Do not resubmit

## Additional Evaluation Sections

**Reproducibility** (1-5 scale), **Datasets** (1-5 scale), **Software** (1-5 scale), **Author Identity Knowledge** (1-5 scale), plus qualitative sections addressing limitations, ethical concerns, and ethics review necessity.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 6276
}
```

</details>

---


### Tool call

_source line 26 · 2026-05-16T00:57:22.252502+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 1 — Round 1 审稿报告（方法严谨性）\n\n### Summary\n\n本文首次对 training-free LLM 信息抽取中的 schema-induced degradation 进行了受控实验分析，将性能退化分解为 count channel（类型数量→recall 下降）和 confusability channel（语义相似性→类型替换错误），并提出 SCS/BCS 指标量化 schema 混淆度。实验涵盖 NER/RE/ED 三个任务，辅以跨模型验证，最后通过 SDGD 实验给出 decompose-then-merge 失败的负面结果。研究问题有价值、实验设计新颖，但若干方法论问题削弱了核心 claim 的可靠性。\n\n---\n\n### Strengths\n\n**S1.** 研究问题定义清晰且有实际意义。将 count 和 confusability 拆分为独立 channel 的思路是该领域的空白，实验设计（count curves + BCS-controlled）逻辑上互补，从 correlational 到 interventional 层层递进。\n\n**S2.** Error taxonomy 分析（§5.4, Table 4）质量高。IntraSub 随 BCS 单调递增（RE: ρ=0.954）、RE 中 100% confusion 为 intra-batch 的发现清晰有力，为 Channel 2 提供了机制层面的证据。NER 与 RE 在 missed-entity pattern 上的分歧也被如实报告。\n\n**S3.** Centrality confound 分析（§5.5）是对 BCS 指标局限性的坦诚自省，与 representation degeneration 文献的连接恰当。\n\n**S4.** 跨模型验证设计合理：不同家族（Qwen vs. Llama）、不同规模（32B vs. 8B）。High-BCS accuracy 在两个模型上收敛到 ≈51% 的 model-invariant floor 是一个有趣的发现。\n\n**S5.** Limitations section 异常详尽，主动披露了 factorial 检验不显著（z=−0.67, p=0.50）、3.4× 为两点比较等问题。\n\n---\n\n### Weaknesses\n\n**W1 [Must-Fix] 3.4× amplification 的统计基础薄弱**\n\n3.4× amplification（31.2pp / 9.1pp）是论文最突出的定量 claim（出现在 abstract、introduction、contributions、results），但存在两个严重问题：\n\n(a) 基线无 CI。16-rel 条件下 low-BCS 和 high-BCS 各只有 1 个 batch（Table 3 注释确认）。9.1pp 基线是单次观测，无法评估不确定性。论文只对 80-rel CI 做了传播（1.9–4.7×），但分母方差被完全忽略。\n\n(b) 跨 pool 比较引入混淆。16-rel 来自 validation split，80-rel 来自 train+val 合并的 80 relations。type pool 组成完全不同，amplification 可能部分归因于 pool 差异而非 scale 效应。\n\n建议：在 80-rel pool 内构造 16-type 子集的 BCS-controlled 实验（多个 low/high batch），获取可比 baseline 并附 CI。当前 3.4× 应降格为描述性观察。\n\n**W2 [Must-Fix] Pairwise SCS 效应量极小，framing 过度**\n\nr=0.112, r²=1.3%（Table 2）。论文将其定位为 \"the first factor empirically isolated\"，掩盖了 embedding similarity 仅解释 1.3% confusion 方差的事实。§5.2 中 nonzero-confusion 子集分析（ρ=0.27–0.31）存在 conditioning on the outcome 问题——剔除 confusion=0 的 pair 人为抬高相关性。\n\n建议：明确承认解释力有限；删除或重新框定 nonzero-confusion 分析并讨论 conditioning bias。\n\n**W3 [Must-Fix] NER 上 count×confusability 交互的证据不足**\n\n§5.4 声称 NER 中两个 channel \"interact\"，但 Limitations 中的 2×2 factorial 检验不显著（z=−0.67, p=0.50）。这是 Contribution 1 的核心组成部分，缺乏统计支撑。\n\n建议：提供更有力的交互证据，或降级为 \"suggestive but not statistically confirmed\"。\n\n**W4 [Should-Fix] SDGD 负面结果仅覆盖两种 merge 策略，overclaim \"structural bottleneck\"**\n\n§6 仅测试 union merge 和 confidence-gated merge 就声称 \"structural bottleneck\"。未测试 span-level NMS、majority voting、calibration-based reranking 等替代方案。且仅在 Few-NERD 上测试，单数据集 + 两种策略不足以支撑 \"structural\" 修饰语。\n\n建议：测试更多 merge 策略，在 FewRel 上复现，或弱化表述。\n\n**W5 [Should-Fix] v1/v2 prompt 切换引入实验内混淆**\n\nv1（fabricate offset 96.5%）用于 count curves 和 BCS-controlled NER；v2 用于后续实验和跨模型比较。绝对数值跨实验不直接可比。\n\n建议：统一用 v2 重跑核心实验，或提供 v1/v2 对照消融。\n\n**W6 [Should-Fix] Embedding 模型不一致**\n\nFew-NERD 用 Qwen3-32B embeddings，FewRel/MAVEN 用 MiniLM。不同 embedding 空间的 BCS 不可直接比较，削弱跨任务一致性。\n\n**W7 [Should-Fix] FewRel 数据集构造可能引入偏差**\n\n合并 train+val splits 且未说明 1,000 balanced instances 的抽样方式。\n\n**W8 [Minor] 完整 prompt 模板未在 appendix 中提供，影响可复现性。\n\n**W9 [Minor] MAVEN 结果实质上反驳 count channel 的普遍性（F1 随 count 上升），abstract/introduction 表述应更谨慎。\n\n**W10 [Minor] 缺少与 supervised IE baseline 的参照。\n\n---\n\n### Questions\n\nQ1. 如果在 80-rel pool 内抽 16-type 子集做 BCS-controlled，amplification 估计值是否变化？\nQ2. 是否探索过多变量模型（加入 type frequency、prompt position 等）提升解释力？\nQ3. SDGD 的 single_pass baseline 用的是 v1 还是 v2 prompt？\nQ4. NER cross-model 效应 \"not robustly detectable\"，如何排除 confusability channel 为 Qwen3 特有？\nQ5. High-BCS ≈51% floor 的来源？是否接近随机猜测？\n\n---\n\n### Overall Assessment\n\n**Soundness**: 3/5\n**Excitement**: 3.5/5\n**Overall**: 3/5 (Findings acceptance)\n**Confidence**: 4/5\n\n论文研究问题好、实验设计有新意、写作透明度高，但 W1–W3 三个 Must-Fix 问题需要实质性修正才能达到 Main Conference 接收标准。建议修改后以 Findings 投稿，或补充实验后提升至 Main Conference 水平。",
  "reviewer_id": "1",
  "project": "schema-dag-extraction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 1 — Round 1 审稿报告（方法严谨性）\n\n### Summary\n\n本文首次对 training-free LLM 信息抽取中的 schema-induced degradation 进行了受控实验分析，将性能退化分解为 count channel（类型数量→recall 下降）和 confusability channel（语义相似性→类型替换错误），并提出 SCS/BCS 指标量化 schema 混淆度。实验涵盖 NER/RE/ED 三个任务，辅以跨模型验证，最后通过 SDGD 实验给出 decompose-then-merge 失败的负面结果。研究问题有价值、实验设计新颖，但若干方法论问题削弱了核心 claim 的可靠性。\n\n---\n\n### Strengths\n\n**S1.** 研究问题定义清晰且有实际意义。将 count 和 confusability 拆分为独立 channel 的思路是该领域的空白，实验设计（count curves + BCS-controlled）逻辑上互补，从 correlational 到 interventional 层层递进。\n\n**S2.** Error taxonomy 分析（§5.4, Table 4）质量高。IntraSub 随 BCS 单调递增（RE: ρ=0.954）、RE 中 100% confusion 为 intra-batch 的发现清晰有力，为 Channel 2 提供了机制层面的证据。NER 与 RE 在 missed-entity pattern 上的分歧也被如实报告。\n\n**S3.** Centrality confound 分析（§5.5）是对 BCS 指标局限性的坦诚自省，与 representation degeneration 文献的连接恰当。\n\n**S4.** 跨模型验证设计合理：不同家族（Qwen vs. Llama）、不同规模（32B vs. 8B）。High-BCS accuracy 在两个模型上收敛到 ≈51% 的 model-invariant floor 是一个有趣的发现。\n\n**S5.** Limitations section 异常详尽，主动披露了 factorial 检验不显著（z=−0.67, p=0.50）、3.4× 为两点比较等问题。\n\n---\n\n### Weaknesses\n\n**W1 [Must-Fix] 3.4× amplification 的统计基础薄弱**\n\n3.4× amplification（31.2pp / 9.1pp）是论文最突出的定量 claim（出现在 abstract、introduction、contributions、results），但存在两个严重问题：\n\n(a) 基线无 CI。16-rel 条件下 low-BCS 和 high-BCS 各只有 1 个 batch（Table 3 注释确认）。9.1pp 基线是单次观测，无法评估不确定性。论文只对 80-rel CI 做了传播（1.9–4.7×），但分母方差被完全忽略。\n\n(b) 跨 pool 比较引入混淆。16-rel 来自 validation split，80-rel 来自 train+val 合并的 80 relations。type pool 组成完全不同，amplification 可能部分归因于 pool 差异而非 scale 效应。\n\n建议：在 80-rel pool 内构造 16-type 子集的 BCS-controlled 实验（多个 low/high batch），获取可比 baseline 并附 CI。当前 3.4× 应降格为描述性观察。\n\n**W2 [Must-Fix] Pairwise SCS 效应量极小，framing 过度**\n\nr=0.112, r²=1.3%（Table 2）。论文将其定位为 \"the first factor empirically isolated\"，掩盖了 embedding similarity 仅解释 1.3% confusion 方差的事实。§5.2 中 nonzero-confusion 子集分析（ρ=0.27–0.31）存在 conditioning on the outcome 问题——剔除 confusion=0 的 pair 人为抬高相关性。\n\n建议：明确承认解释力有限；删除或重新框定 nonzero-confusion 分析并讨论 conditioning bias。\n\n**W3 [Must-Fix] NER 上 count×confusability 交互的证据不足**\n\n§5.4 声称 NER 中两个 channel \"interact\"，但 Limitations 中的 2×2 factorial 检验不显著（z=−0.67, p=0.50）。这是 Contribution 1 的核心组成部分，缺乏统计支撑。\n\n建议：提供更有力的交互证据，或降级为 \"suggestive but not statistically confirmed\"。\n\n**W4 [Should-Fix] SDGD 负面结果仅覆盖两种 merge 策略，overclaim \"structural bottleneck\"**\n\n§6 仅测试 union merge 和 confidence-gated merge 就声称 \"structural bottleneck\"。未测试 span-level NMS、majority voting、calibration-based reranking 等替代方案。且仅在 Few-NERD 上测试，单数据集 + 两种策略不足以支撑 \"structural\" 修饰语。\n\n建议：测试更多 merge 策略，在 FewRel 上复现，或弱化表述。\n\n**W5 [Should-Fix] v1/v2 prompt 切换引入实验内混淆**\n\nv1（fabricate offset 96.5%）用于 count curves 和 BCS-controlled NER；v2 用于后续实验和跨模型比较。绝对数值跨实验不直接可比。\n\n建议：统一用 v2 重跑核心实验，或提供 v1/v2 对照消融。\n\n**W6 [Should-Fix] Embedding 模型不一致**\n\nFew-NERD 用 Qwen3-32B embeddings，FewRel/MAVEN 用 MiniLM。不同 embedding 空间的 BCS 不可直接比较，削弱跨任务一致性。\n\n**W7 [Should-Fix] FewRel 数据集构造可能引入偏差**\n\n合并 train+val splits 且未说明 1,000 balanced instances 的抽样方式。\n\n**W8 [Minor] 完整 prompt 模板未在 appendix 中提供，影响可复现性。\n\n**W9 [Minor] MAVEN 结果实质上反驳 count channel 的普遍性（F1 随 count 上升），abstract/introduction 表述应更谨慎。\n\n**W10 [Minor] 缺少与 supervised IE baseline 的参照。\n\n---\n\n### Questions\n\nQ1. 如果在 80-rel pool 内抽 16-type 子集做 BCS-controlled，amplification 估计值是否变化？\nQ2. 是否探索过多变量模型（加入 type frequency、prompt position 等）提升解释力？\nQ3. SDGD 的 single_pass baseline 用的是 v1 还是 v2 prompt？\nQ4. NER cross-model 效应 \"not robustly detectable\"，如何排除 confusability channel 为 Qwen3 特有？\nQ5. High-BCS ≈51% floor 的来源？是否接近随机猜测？\n\n---\n\n### Overall Assessment\n\n**Soundness**: 3/5\n**Excitement**: 3.5/5\n**Overall**: 3/5 (Findings acceptance)\n**Confidence**: 4/5\n\n论文研究问题好、实验设计有新意、写作透明度高，但 W1–W3 三个 Must-Fix 问题需要实质性修正才能达到 Main Conference 接收标准。建议修改后以 Findings 投稿，或补充实验后提升至 Main Conference 水平。",
    "reviewer_id": "1",
    "project": "schema-dag-extraction"
  }
}
```

</details>

---


### Tool result

_source line 27 · 2026-05-16T00:57:26.017932+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3765
}
```

</details>

---


### Assistant

_source line 28 · 2026-05-16T00:57:34.457744+00:00_

审稿报告已提交给 Review Director。

总结：给出 **Overall 3/5 (Findings acceptance)**，识别了 3 个 Must-Fix 问题：

1. **3.4× amplification 统计基础薄弱**——16-rel baseline 仅 1 个 batch 无 CI，且跨 pool 比较引入混淆
2. **Pairwise SCS r²=1.3% 效应量极小但 framing 偏强**——nonzero-confusion 子集分析存在 conditioning on the outcome 偏差
3. **NER count×confusability 交互缺乏统计支撑**——factorial 检验 p=0.50 不显著，但论文仍将其作为核心 contribution

另有 4 个 Should-Fix（SDGD overclaim、v1/v2 prompt 混淆、embedding 不一致、FewRel 数据构造）和 3 个 Minor 问题。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1"
}
```

</details>

---


## Round 2

## Round 2

104 recorded events


### User

_source line 29 · 2026-05-16T01:00:40.796602+00:00_

[Round 1 审稿请求]:
## 交叉分享 — 请逐条回应 Reviewer 2 的审稿意见

以下是 Reviewer 2（新颖性与完整性方向）的完整审稿原文。请逐条回应每个 Weakness 和 Question：
- **[AGREE]** 同意并说明理由
- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）

特别关注与你的发现是否一致或矛盾的地方。

---

## Reviewer 2 完整审稿原文

**Paper:** "Does Type Confusability Drive Schema-Induced Degradation in Training-Free LLM Information Extraction?"

### Summary

本文研究 training-free LLM 信息抽取中，prompt schema 的 type count 和 type confusability 如何独立影响抽取性能。作者引入 Schema Confusability Score (SCS/BCS)，设计 count curve 和 BCS-controlled 两套实验范式，在 NER/RE/ED 三个任务上隔离出 count-driven recall decline（Channel 1）和 confusability-driven type confusion（Channel 2）两条退化通道，并证明 confusability-aware decomposition 因 merge amplification 而失败。实验设计严谨，研究问题明确，但核心发现的 effect size 偏弱（pairwise r² < 2%），关键 amplification claim 依赖两点比较，且论文在呈现上存在明显缺陷（正文无 figure、无 Discussion section）。

### 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| **Soundness** | 3.5/5 | 实验设计出色（count curve + BCS-controlled），bootstrap CI 规范。但 pairwise SCS 解释力极弱（r² < 2%），3.4× amplification 基于两点比较，中间点非独立。MAVEN 结果反向，削弱统一叙事 |
| **Excitement** | 3/5 | 研究问题重要且先前未被系统研究，controlled experiment 思路值得推广。但结论以描述性发现为主，缺乏可操作的方法论贡献（SDGD 失败、未提出替代方案） |
| **Overall** | 3/5 | Findings track 可接收水平。实验设计强于结论强度，呈现问题可修复但需实质工作 |
| **Confidence** | 4/5 | 熟悉 LLM-based IE 和 zero-shot extraction 文献 |
| **Reproducibility** | 4/5 | 固定 seed、报告 CI、详细描述实验配置，但代码/数据未提供 |

### Strengths

**S1.** 实验设计精良，因果推断层次清晰。Count curve 提供 correlational evidence，BCS-controlled 提供 interventional evidence，逐步升级。这在 LLM IE 文献中属于首次。

**S2.** Centrality confound 的发现极有价值。§4.5 揭示 same-domain schema 中 mean BCS 与 error rate 正相关的反直觉现象，追溯到 representation degeneration 文献，对后续 metric 设计有直接指导。

**S3.** Cross-model validation 设计合理。不同模型家族上复现两条 channel，特别是 high-BCS accuracy 收敛到 ~51% 的 model-invariant floor。

**S4.** Negative result（SDGD）报告诚实且有信息量。系统测试四种 decomposition mode，明确定位 merge amplification 为瓶颈。

**S5.** 相关工作覆盖广泛，与 LLM-PEE 的三点区分清晰有力。

### Weaknesses

**W1 [Must-Fix] 正文零 figure，关键结果缺乏视觉呈现。** Count curves、BCS scaling、error taxonomy 三张核心 figure 全在 Appendix。Reviewer 评估正文 8 页时无法看到最核心的 evidence。建议将 Fig 1 和 Fig 2 移入正文。

**W2 [Must-Fix] Pairwise SCS 解释力极弱（r² = 1.3–1.7%），framing 有 overclaiming 嫌疑。** Contribution 2 声称"robust predictor"，但 r² < 2%。Conditioning on nonzero confusion pairs（ρ = 0.27–0.31）有 selection bias 风险。建议改为"statistically significant but weak predictor"，详细讨论剩余 98% variance 来源。

**W3 [Must-Fix] 3.4× amplification 核心 claim 基于两点比较，统计支撑不足。** 16-rel 条件仅一个 extreme batch（无 CI），中间 40-rel 来自 80-rel pool 子集（非独立）。建议增加 16-rel 多 batch + 独立中间规模验证。

**W4 [Should-Fix] 无 Discussion section，Conclusion 仅 1 段 5 行。** 对于呈现复杂、矛盾结果的论文，缺乏对 theoretical implications、practical guidelines、替代方案的讨论。

**W5 [Should-Fix] MAVEN 结果与主 narrative 矛盾，SCS/BCS 适用范围被限制在 cross-domain schema，generalizability 大幅缩小。**

**W6 [Should-Fix] v1 vs v2 prompt 不一致，NER count curves 使用 known-flawed v1 prompt（96.5% offset fabrication），影响可比性。**

**W7 [Should-Fix] Limitations section 单段 ~20 行，结构差，难以评估各 limitation 严重程度。**

**W8 [Should-Fix] `minilm-2019` 引用指向 Sentence-BERT，但实际使用 all-MiniLM-L6-v2（应引 MiniLM 原始论文）。**

**W9 [Minor] 缺少 Responsible NLP Research Checklist。**

**W10 [Minor] FewRel 合并 train+val split 为非标准设置，讨论不够显著。**

**W11 [Minor] "Multi-channel degradation model"用"model"描述经验分类，建议改为"framework"。**

### Questions for Authors

Q1. 16-rel 条件为何仅一个 extreme batch？增加 batch 获 CI 的技术障碍是什么？
Q2. 是否尝试过 residualized BCS（去除 centrality component）？
Q3. v1 prompt 的 offset fabrication 是否影响 type discrimination behavior？
Q4. SDGD 为何仅在 NER 上测试？RE 上 merge amplification 是否同样严重？
Q5. 是否探索过 non-zero temperature 对 type confusion 的影响？

### Missing References

1. "Reflect then Learn: Active Prompting for IE Guided by Introspective Confusion" (AAAI 2026)
2. MiniLM 原始论文 (Wang et al., 2020, NeurIPS)
3. Prompt sensitivity 文献（如 Sclar et al., 2024, TACL）

### Overall Assessment

**Borderline (3/5)** — 推荐 Findings track 接收，主会议需实质修改。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 30 · 2026-05-16T01:00:52.309936+00:00_

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
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
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

_source line 31 · 2026-05-16T01:00:52.411901+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 32 · 2026-05-16T01:00:57.636743+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/paper/*.pdf",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/paper/*.pdf",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction"
  }
}
```

</details>

---


### Tool result

_source line 33 · 2026-05-16T01:00:58.089868+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/figures/paper/fig_count_curves.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/figures/paper/fig_error_taxonomy.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/figures/paper/fig_bcs_scaling.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/figures/paper/fig_sdgd_comparison.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.pdf

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Glob",
  "elapsed_ms": 453
}
```

</details>

---


### Tool call

_source line 34 · 2026-05-16T01:00:58.191587+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/paper/main.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/paper/main.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction"
  }
}
```

</details>

---


### Tool result

_source line 35 · 2026-05-16T01:00:58.243005+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Glob",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 36 · 2026-05-16T01:01:01.833794+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.pdf",
  "pages": "1-8",
  "dpi": "180"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.pdf",
    "pages": "1-8",
    "dpi": "180"
  }
}
```

</details>

---


### Tool result

_source line 37 · 2026-05-16T01:01:06.500646+00:00_

Error: result (6,544,075 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-18-projects-schema-dag-extraction--claude-sessions-review-reviewer-1-b5f154cf/65fb597d-af39-4276-9043-33e3b748196b/tool-results/mcp-agent-ml-research-pdf_to_images-1778893266019.txt.
Format: JSON with schema: {result: string}
- For targeted queries (find a value, filter by field): use jq on the file directly.
- For analysis or summarization that requires reading the full content: first probe the structure (e.g., jq 'type, length, keys?' /home/ubuntu/.claude-account-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-18-projects-schema-dag-extraction--claude-sessions-review-reviewer-1-b5f154cf/65fb597d-af39-4276-9043-33e3b748196b/tool-results/mcp-agent-ml-research-pdf_to_images-1778893266019.txt), then extract slices with jq or python — Read's line-based offset/limit will not chunk this file.
- If the Agent tool is available, do this inside a subagent so the full output stays out of your main context. Give it the instruction above verbatim, and be explicit about what it must return — e.g. "/home/ubuntu/.claude-account-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-18-projects-schema-dag-extraction--claude-sessions-review-reviewer-1-b5f154cf/65fb597d-af39-4276-9043-33e3b748196b/tool-results/mcp-agent-ml-research-pdf_to_images-1778893266019.txt is JSON with schema: {result: string}; probe the structure with jq (type/length/keys), then extract and read the content in full with jq or python, then summarize and quote any key findings verbatim." A vague "summarize this" may lose detail.


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 4666
}
```

</details>

---


### Tool call

_source line 38 · 2026-05-16T01:01:10.824114+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.pdf",
  "pages": "1-2",
  "dpi": "170"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.pdf",
    "pages": "1-2",
    "dpi": "170"
  }
}
```

</details>

---


### Tool result

_source line 39 · 2026-05-16T01:01:11.879591+00:00_

Error: result (1,492,259 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-18-projects-schema-dag-extraction--claude-sessions-review-reviewer-1-b5f154cf/65fb597d-af39-4276-9043-33e3b748196b/tool-results/mcp-agent-ml-research-pdf_to_images-1778893271784.txt.
Format: JSON with schema: {result: string}
- For targeted queries (find a value, filter by field): use jq on the file directly.
- For analysis or summarization that requires reading the full content: first probe the structure (e.g., jq 'type, length, keys?' /home/ubuntu/.claude-account-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-18-projects-schema-dag-extraction--claude-sessions-review-reviewer-1-b5f154cf/65fb597d-af39-4276-9043-33e3b748196b/tool-results/mcp-agent-ml-research-pdf_to_images-1778893271784.txt), then extract slices with jq or python — Read's line-based offset/limit will not chunk this file.
- If the Agent tool is available, do this inside a subagent so the full output stays out of your main context. Give it the instruction above verbatim, and be explicit about what it must return — e.g. "/home/ubuntu/.claude-account-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-18-projects-schema-dag-extraction--claude-sessions-review-reviewer-1-b5f154cf/65fb597d-af39-4276-9043-33e3b748196b/tool-results/mcp-agent-ml-research-pdf_to_images-1778893271784.txt is JSON with schema: {result: string}; probe the structure with jq (type/length/keys), then extract and read the content in full with jq or python, then summarize and quote any key findings verbatim." A vague "summarize this" may lose detail.


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 1055
}
```

</details>

---


### Tool call

_source line 40 · 2026-05-16T01:01:17.906799+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.pdf",
  "pages": "1",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.pdf",
    "pages": "1",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 41 · 2026-05-16T01:01:18.618767+00:00_

Error: result (615,977 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-18-projects-schema-dag-extraction--claude-sessions-review-reviewer-1-b5f154cf/65fb597d-af39-4276-9043-33e3b748196b/tool-results/mcp-agent-ml-research-pdf_to_images-1778893278599.txt.
Format: JSON with schema: {result: string}
- For targeted queries (find a value, filter by field): use jq on the file directly.
- For analysis or summarization that requires reading the full content: first probe the structure (e.g., jq 'type, length, keys?' /home/ubuntu/.claude-account-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-18-projects-schema-dag-extraction--claude-sessions-review-reviewer-1-b5f154cf/65fb597d-af39-4276-9043-33e3b748196b/tool-results/mcp-agent-ml-research-pdf_to_images-1778893278599.txt), then extract slices with jq or python — Read's line-based offset/limit will not chunk this file.
- If the Agent tool is available, do this inside a subagent so the full output stays out of your main context. Give it the instruction above verbatim, and be explicit about what it must return — e.g. "/home/ubuntu/.claude-account-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-18-projects-schema-dag-extraction--claude-sessions-review-reviewer-1-b5f154cf/65fb597d-af39-4276-9043-33e3b748196b/tool-results/mcp-agent-ml-research-pdf_to_images-1778893278599.txt is JSON with schema: {result: string}; probe the structure with jq (type/length/keys), then extract and read the content in full with jq or python, then summarize and quote any key findings verbatim." A vague "summarize this" may lose detail.


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 711
}
```

</details>

---


### Tool call

_source line 42 · 2026-05-16T01:01:30.589141+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

````json
{
  "description": "Read paper pages 1-4",
  "prompt": "I need you to read a research paper PDF and provide a detailed summary of its content. The PDF has been converted to images.\n\nFirst, check what image files exist in the output directory:\n```\nls /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/_pdf_images/\n```\n\nThen read pages 1-4 of the paper (the image files should be named something like page_1.png, page_2.png, etc.) using the Read tool on each image file.\n\nFor each page, provide a DETAILED transcription/summary of ALL content — every section heading, every claim, every number, every table entry, every equation. I need the full content, not a high-level summary. This is for a peer review and I need to see every detail.\n\nThe paper is titled \"Does Type Confusability Drive Schema-Induced Degradation in Training-Free LLM Information Extraction?\"\n\nReport back ALL content from pages 1-4 in full detail.",
  "subagent_type": "general-purpose"
}
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Agent",
  "tool_args": {
    "description": "Read paper pages 1-4",
    "prompt": "I need you to read a research paper PDF and provide a detailed summary of its content. The PDF has been converted to images.\n\nFirst, check what image files exist in the output directory:\n```\nls /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/_pdf_images/\n```\n\nThen read pages 1-4 of the paper (the image files should be named something like page_1.png, page_2.png, etc.) using the Read tool on each image file.\n\nFor each page, provide a DETAILED transcription/summary of ALL content — every section heading, every claim, every number, every table entry, every equation. I need the full content, not a high-level summary. This is for a peer review and I need to see every detail.\n\nThe paper is titled \"Does Type Confusability Drive Schema-Induced Degradation in Training-Free LLM Information Extraction?\"\n\nReport back ALL content from pages 1-4 in full detail.",
    "subagent_type": "general-purpose"
  }
}
````

</details>

---


### Tool call

_source line 43 · 2026-05-16T01:01:32.949821+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

````json
{
  "description": "Read paper pages 5-8",
  "prompt": "I need you to read a research paper PDF and provide a detailed summary of its content. The PDF has been converted to images.\n\nFirst, check what image files exist in the output directory:\n```\nls /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/_pdf_images/\n```\n\nThen read pages 5-8 of the paper (the image files should be named something like page_5.png, page_6.png, etc.) using the Read tool on each image file.\n\nFor each page, provide a DETAILED transcription/summary of ALL content — every section heading, every claim, every number, every table entry, every equation. I need the full content, not a high-level summary. This is for a peer review and I need to see every detail.\n\nThe paper is titled \"Does Type Confusability Drive Schema-Induced Degradation in Training-Free LLM Information Extraction?\"\n\nReport back ALL content from pages 5-8 in full detail.",
  "subagent_type": "general-purpose"
}
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Agent",
  "tool_args": {
    "description": "Read paper pages 5-8",
    "prompt": "I need you to read a research paper PDF and provide a detailed summary of its content. The PDF has been converted to images.\n\nFirst, check what image files exist in the output directory:\n```\nls /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/_pdf_images/\n```\n\nThen read pages 5-8 of the paper (the image files should be named something like page_5.png, page_6.png, etc.) using the Read tool on each image file.\n\nFor each page, provide a DETAILED transcription/summary of ALL content — every section heading, every claim, every number, every table entry, every equation. I need the full content, not a high-level summary. This is for a peer review and I need to see every detail.\n\nThe paper is titled \"Does Type Confusability Drive Schema-Induced Degradation in Training-Free LLM Information Extraction?\"\n\nReport back ALL content from pages 5-8 in full detail.",
    "subagent_type": "general-purpose"
  }
}
````

</details>

---


### Tool call

_source line 44 · 2026-05-16T01:01:35.228329+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/_pdf_images/",
  "description": "List PDF image files in the output directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/_pdf_images/",
    "description": "List PDF image files in the output directory"
  }
}
```

</details>

---


### Tool result

_source line 45 · 2026-05-16T01:01:35.228728+00:00_

main_p1.png
main_p10.png
main_p11.png
main_p12.png
main_p2.png
main_p3.png
main_p4.png
main_p5.png
main_p6.png
main_p7.png
main_p8.png
main_p9.png

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 46 · 2026-05-16T01:01:35.480263+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

````json
{
  "description": "Read paper pages 9-end",
  "prompt": "I need you to read a research paper PDF and provide a detailed summary of its content. The PDF has been converted to images.\n\nFirst, check what image files exist in the output directory:\n```\nls /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/_pdf_images/\n```\n\nThen read ALL pages from page 9 onwards (these are likely appendix/supplementary pages) using the Read tool on each image file.\n\nFor each page, provide a DETAILED transcription/summary of ALL content — every section heading, every claim, every number, every table entry, every figure description, every equation. I need the full content, not a high-level summary. This is for a peer review and I need to see every detail.\n\nThe paper is titled \"Does Type Confusability Drive Schema-Induced Degradation in Training-Free LLM Information Extraction?\"\n\nReport back ALL content from pages 9 onwards in full detail.",
  "subagent_type": "general-purpose"
}
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Agent",
  "tool_args": {
    "description": "Read paper pages 9-end",
    "prompt": "I need you to read a research paper PDF and provide a detailed summary of its content. The PDF has been converted to images.\n\nFirst, check what image files exist in the output directory:\n```\nls /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/_pdf_images/\n```\n\nThen read ALL pages from page 9 onwards (these are likely appendix/supplementary pages) using the Read tool on each image file.\n\nFor each page, provide a DETAILED transcription/summary of ALL content — every section heading, every claim, every number, every table entry, every figure description, every equation. I need the full content, not a high-level summary. This is for a peer review and I need to see every detail.\n\nThe paper is titled \"Does Type Confusability Drive Schema-Induced Degradation in Training-Free LLM Information Extraction?\"\n\nReport back ALL content from pages 9 onwards in full detail.",
    "subagent_type": "general-purpose"
  }
}
````

</details>

---


### Tool call

_source line 47 · 2026-05-16T01:01:35.986084+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/_pdf_images/",
  "description": "List PDF image files in output directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/_pdf_images/",
    "description": "List PDF image files in output directory"
  }
}
```

</details>

---


### Tool result

_source line 48 · 2026-05-16T01:01:36.036711+00:00_

main_p1.png
main_p10.png
main_p11.png
main_p12.png
main_p2.png
main_p3.png
main_p4.png
main_p5.png
main_p6.png
main_p7.png
main_p8.png
main_p9.png

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 49 · 2026-05-16T01:01:37.752361+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/_pdf_images/main_p1.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/_pdf_images/main_p1.png"
  }
}
```

</details>

---


### Tool call

_source line 50 · 2026-05-16T01:01:38.206180+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/_pdf_images/main_p2.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/_pdf_images/main_p2.png"
  }
}
```

</details>

---


### Tool call

_source line 51 · 2026-05-16T01:01:39.162174+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/_pdf_images/",
  "description": "List PDF image files in the output directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/_pdf_images/",
    "description": "List PDF image files in the output directory"
  }
}
```

</details>

---


### Tool call

_source line 52 · 2026-05-16T01:01:39.162599+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/_pdf_images/main_p3.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/_pdf_images/main_p3.png"
  }
}
```

</details>

---


### Tool call

_source line 53 · 2026-05-16T01:01:39.315053+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/_pdf_images/main_p4.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/_pdf_images/main_p4.png"
  }
}
```

</details>

---


### Tool result

_source line 54 · 2026-05-16T01:01:39.667507+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1915
}
```

</details>

---


### Tool call

_source line 55 · 2026-05-16T01:01:39.720402+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/_pdf_images/main_p5.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/_pdf_images/main_p5.png"
  }
}
```

</details>

---


### Tool call

_source line 56 · 2026-05-16T01:01:39.720820+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/_pdf_images/main_p6.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/_pdf_images/main_p6.png"
  }
}
```

</details>

---


### Tool call

_source line 57 · 2026-05-16T01:01:41.034008+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/_pdf_images/main_p7.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/_pdf_images/main_p7.png"
  }
}
```

</details>

---


### Tool call

_source line 58 · 2026-05-16T01:01:41.034523+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/_pdf_images/main_p8.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/_pdf_images/main_p8.png"
  }
}
```

</details>

---


### Tool result

_source line 59 · 2026-05-16T01:01:43.426197+00:00_

main_p1.png
main_p10.png
main_p11.png
main_p12.png
main_p2.png
main_p3.png
main_p4.png
main_p5.png
main_p6.png
main_p7.png
main_p8.png
main_p9.png

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Bash",
  "elapsed_ms": 4264
}
```

</details>

---


### Tool result

_source line 60 · 2026-05-16T01:01:44.332360+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 6126
}
```

</details>

---


### Tool call

_source line 61 · 2026-05-16T01:01:48.462219+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/_pdf_images/main_p9.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/_pdf_images/main_p9.png"
  }
}
```

</details>

---


### Tool call

_source line 62 · 2026-05-16T01:01:48.462743+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/_pdf_images/main_p10.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/_pdf_images/main_p10.png"
  }
}
```

</details>

---


### Tool call

_source line 63 · 2026-05-16T01:01:48.463104+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/_pdf_images/main_p11.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/_pdf_images/main_p11.png"
  }
}
```

</details>

---


### Tool call

_source line 64 · 2026-05-16T01:01:48.514201+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/_pdf_images/main_p12.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/_pdf_images/main_p12.png"
  }
}
```

</details>

---


### Tool result

_source line 65 · 2026-05-16T01:01:49.832282+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 10669
}
```

</details>

---


### Tool result

_source line 66 · 2026-05-16T01:01:50.341154+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 11026
}
```

</details>

---


### Tool result

_source line 67 · 2026-05-16T01:01:51.302257+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 11581
}
```

</details>

---


### Tool result

_source line 68 · 2026-05-16T01:01:51.303055+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 11582
}
```

</details>

---


### Tool result

_source line 69 · 2026-05-16T01:01:53.429146+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 12394
}
```

</details>

---


### Tool result

_source line 70 · 2026-05-16T01:01:53.480334+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 12446
}
```

</details>

---


### Tool result

_source line 71 · 2026-05-16T01:01:54.593324+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 6079
}
```

</details>

---


### Tool result

_source line 72 · 2026-05-16T01:01:55.615398+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 7152
}
```

</details>

---


### Tool result

_source line 73 · 2026-05-16T01:01:55.616184+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 7153
}
```

</details>

---


### Tool result

_source line 74 · 2026-05-16T01:01:55.667159+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 7204
}
```

</details>

---


### Tool call

_source line 75 · 2026-05-16T01:02:00.695833+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/_pdf_images/main_p1.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/_pdf_images/main_p1.png"
  }
}
```

</details>

---


### Tool call

_source line 76 · 2026-05-16T01:02:00.696473+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/_pdf_images/main_p8.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/_pdf_images/main_p8.png"
  }
}
```

</details>

---


### Tool result

_source line 77 · 2026-05-16T01:02:03.061159+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 2365
}
```

</details>

---


### Tool result

_source line 78 · 2026-05-16T01:02:03.513519+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 2817
}
```

</details>

---


### Tool call

_source line 79 · 2026-05-16T01:02:07.638777+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/_pdf_images/main_p2.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/_pdf_images/main_p2.png"
  }
}
```

</details>

---


### Tool call

_source line 80 · 2026-05-16T01:02:07.991112+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/_pdf_images/main_p3.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/_pdf_images/main_p3.png"
  }
}
```

</details>

---


### Tool call

_source line 81 · 2026-05-16T01:02:08.497139+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/_pdf_images/main_p4.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/_pdf_images/main_p4.png"
  }
}
```

</details>

---


### Tool call

_source line 82 · 2026-05-16T01:02:09.407165+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/_pdf_images/main_p5.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/_pdf_images/main_p5.png"
  }
}
```

</details>

---


### Tool call

_source line 83 · 2026-05-16T01:02:10.416147+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/_pdf_images/main_p6.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/_pdf_images/main_p6.png"
  }
}
```

</details>

---


### Tool call

_source line 84 · 2026-05-16T01:02:10.568984+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/_pdf_images/main_p7.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/_pdf_images/main_p7.png"
  }
}
```

</details>

---


### Tool result

_source line 85 · 2026-05-16T01:02:12.648970+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 5010
}
```

</details>

---


### Tool result

_source line 86 · 2026-05-16T01:02:13.510495+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 5519
}
```

</details>

---


### Tool result

_source line 87 · 2026-05-16T01:02:14.822421+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 6325
}
```

</details>

---


### Tool result

_source line 88 · 2026-05-16T01:02:15.234676+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 5827
}
```

</details>

---


### Tool result

_source line 89 · 2026-05-16T01:02:15.790633+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 5374
}
```

</details>

---


### Tool result

_source line 90 · 2026-05-16T01:02:15.791466+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 5222
}
```

</details>

---


### Tool result

_source line 91 · 2026-05-16T01:04:04.105529+00:00_

Here is the detailed content of pages 1 through 4.

---

## PAGE 1

### Title
**Does Type Confusability Drive Schema-Induced Degradation in Training-Free LLM Information Extraction?**

**Anonymous ACL submission**

### Abstract
Training-free LLM information extraction -- prompting models with target schemas without fine-tuning -- degrades sharply as schema complexity grows. NER recall drops from 0.72 to 0.42 with 64 candidate types, and RE accuracy falls from 85.7% to 50.4% with 80 relations. Prior work conflates type count with type confusability, leaving the mechanisms behind this degradation unclear. We conduct the first controlled empirical study that isolates type confusability from type count across three IE tasks (NER, RE, event detection) and three datasets. We introduce the Schema Confusability Score (SCS) to quantify pairwise semantic overlap between types and design two complementary experimental paradigms: count curves that vary schema size while randomizing confusability, and BCS-controlled experiments that fix size while varying confusability. Our experiments reveal two degradation channels: a count channel that suppresses recall in NER and RE as candidate types increase, and a confusability channel where semantically similar type triggers intra-batch substitution errors. In RE, these channels are clearly separable: in NER, confusable type sets additionally impair entity detection, revealing task-dependent error mechanisms. Pairwise SCS predicts type confusion across tasks (Pearson r = 0.112-0.129, p = 0.013-0.017) -- modest in magnitude but the first factor empirically isolated in controlled zero-shot IE experiments. Confusability effects amplify 3.1x as schema size grows from 16 to 80 types, with accuracy gaps widening from 0.1 to 31.2 percentage points. Both channels replicate on Llama-3.1-8B; the count channel (perhaps r = 0.173) and the confusability channel on RE (delta = -27 pp), with high-BCS accuracy converging to the same floor across models.
…[truncated 19411 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Agent",
  "elapsed_ms": 153516
}
```

</details>

---


### Tool result

_source line 92 · 2026-05-16T01:04:23.686470+00:00_

Now I have all pages. Here is the detailed transcription of pages 9 through 12:

---

## PAGE 9 (top half: end of Section 5, Limitations; bottom half: beginning of References)

### Section 5 continuation (from page 8) — "Why Naive Decomposition Fails"

The page begins mid-sentence, continuing the discussion of the Schema-DAG-Guided Decomposition (SDGD) method. The content visible at the very top discusses:

- **Decomposition protocol**: They construct a **confusability graph** G = (V, E) where each vertex is a type and an edge connects types t_i, t_j whenever SCS(t_i, t_j) > τ. Greedy graph coloring (LARGEST_FIRST) assigns each type to a color such that no two adjacent (i.e., highly confusable) types share a color. Each color class forms one extraction batch, and predictions are merged via set union.
- **Four modes compared**: (i) **single_pass**, the undecomposed baseline; (ii) **ndgl_zero**, SCS-guided partitioning; (iii) **random_batch**, random partitioning with matched batch sizes; and (iv) **per_type**, the extreme case where each type is extracted in isolation, following the strategy of Zhou et al. (2024).
- **Table 5** summarizes the results on Few-NERD.

**"All decomposition modes degrade F1."** Table 5 reports the outcomes. Single-pass extraction achieves F1 = 0.445 (P = 0.363, R = 0.568). SDGD obtains F1 = 0.251 (P = 0.210, R = 0.314), a 44% relative drop. Random batching reaches F1 = 0.320 (P = 0.249, R = 0.446), and per-type extraction yields F1 = 0.024 (P = 0.194, R = 0.586). **Every decomposition mode falls below the single-pass baseline.**

**"Merge amplification."** The pattern across modes is consistent: decomposition boosts recall (per-type recall reaches 0.586 versus single-pass 0.368) but devastates precision (0.194 versus 0.563). The mechanism is straightforward: when the same text is presented to the model k times with different type subsets, each pass independently generates entity predictions. Because LLM outputs are not calibrated across pa
…[truncated 15375 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Agent",
  "elapsed_ms": 168206
}
```

</details>

---


### Tool result

_source line 93 · 2026-05-16T01:04:24.591891+00:00_

Here is the detailed transcription of pages 5 through 8.

---

## PAGE 5

### Section 3.3 (continued): Experiment designs

**Experiment 1: Count Curves.** The authors vary the number of types presented in the prompt schema to measure performance as a function of schema size. For each count level, they sample 5 random type batches and evaluate the same 1,000 test samples across all batches. At count = 1, every type is evaluated individually as a solo baseline. The count levels follow natural partition points in each schema's type hierarchy rather than uniform spacing: {1, 2, 6, 12, 22, 44, 64} for Few-NERD, {1, 4, 8, 16, 32, 64, 80} for FewRel, and {1, 6, 12, 22, 44, 64} for MAVEN.

**Experiment 2: BCS-Controlled.** They fix the type count and vary the Batch Confusability Score to isolate the effect of inter-type similarity from schema size. For each count level, they construct one low-BCS batch (types with the lowest pairwise similarities), one high-BCS batch (types with the highest pairwise similarities), and 25 random batches (27 total per count level). They run this paradigm on Few-NERD at count {6, 12} and on FewRel at count {6, 16}, the latter evaluated on both a 16-relation pool and the full 80-relation pool. For MAVEN, they conduct analogous BCS-controlled experiments at count = {6, 12} with 27 batches per level; however, the same-domain nature of MAVEN's FrameNet-derived types introduces a confounding confounder that complicates BCS interpretation. They report these results separately in Section 4.5.

### Section 3.4: Evaluation Metrics

They use task-appropriate metrics that reflect the distinct nature of each extraction problem.

**NER (Few-NERD): Text-match F1.** A predicted entity is a true positive if the predicted text string exactly matches (case-insensitive) a gold entity text and the predicted type matches the gold type. This text-match evaluation operates at the entity level rather than the token level. They report Precision, Recall, and F1.

**RE 
…[truncated 18336 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Agent",
  "elapsed_ms": 171642
}
```

</details>

---


### Tool call

_source line 94 · 2026-05-16T01:05:29.964023+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\nimport subprocess\nresult = subprocess.run(['python3', '-c', '''\ntry:\n    import fitz\n    doc = fitz.open('/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.pdf')\n    print(f'Total pages: {doc.page_count}')\n    doc.close()\nexcept ImportError:\n    print('no pymupdf')\n'''], capture_output=True, text=True)\nprint(result.stdout)\nprint(result.stderr)\n\"",
  "description": "Check PDF total page count"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"\nimport subprocess\nresult = subprocess.run(['python3', '-c', '''\ntry:\n    import fitz\n    doc = fitz.open('/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.pdf')\n    print(f'Total pages: {doc.page_count}')\n    doc.close()\nexcept ImportError:\n    print('no pymupdf')\n'''], capture_output=True, text=True)\nprint(result.stdout)\nprint(result.stderr)\n\"",
    "description": "Check PDF total page count"
  }
}
```

</details>

---


### Tool result

_source line 95 · 2026-05-16T01:05:30.824028+00:00_

Total pages: 12

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Bash",
  "elapsed_ms": 860
}
```

</details>

---


### Tool call

_source line 96 · 2026-05-16T01:05:30.876041+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/paper/appendix*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/paper/appendix*",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction"
  }
}
```

</details>

---


### Tool result

_source line 97 · 2026-05-16T01:05:31.177829+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Glob",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 98 · 2026-05-16T01:05:31.229239+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/paper/*appendix*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/paper/*appendix*",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction"
  }
}
```

</details>

---


### Tool result

_source line 99 · 2026-05-16T01:05:31.280025+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 100 · 2026-05-16T01:05:36.206011+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "appendix|\\\\\\\\appendix|Appendix",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Grep",
  "tool_args": {
    "pattern": "appendix|\\\\\\\\appendix|Appendix",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
    "output_mode": "content"
  }
}
```

</details>

---


### Tool result

_source line 101 · 2026-05-16T01:05:36.658043+00:00_

41:\appendix
44:\label{sec:appendix_figures}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Grep",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 102 · 2026-05-16T01:05:37.417279+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "\\\\\\\\includegraphics|\\\\\\\\begin\\{figure\\}",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Grep",
  "tool_args": {
    "pattern": "\\\\\\\\includegraphics|\\\\\\\\begin\\{figure\\}",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
    "output_mode": "content"
  }
}
```

</details>

---


### Tool result

_source line 103 · 2026-05-16T01:05:37.518015+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Grep",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 104 · 2026-05-16T01:05:40.231004+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
  "offset": "30",
  "limit": "30"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
    "offset": "30",
    "limit": "30"
  }
}
```

</details>

---


### Tool result

_source line 105 · 2026-05-16T01:05:40.281657+00:00_

30	\input{results}
31	
32	\input{sdgd_negative}
33	
34	\input{discussion}
35	
36	\section*{Limitations}
37	The primary experiments use Qwen3-32B. Channel~1 (count effect) has been validated on Meta-Llama-3.1-8B-Instruct (recall decline $-$43\,pp, per-batch $r = 0.725$ with Qwen3-32B). Channel~2 was validated cross-model on FewRel RE: Llama-3.1-8B-Instruct shows $\Delta = -27.1$\,pp at count 8 and $-23.9$\,pp at count 16, comparable to Qwen3-32B's $-31.2$\,pp. High-BCS accuracy is model-invariant ($\approx$0.51), with cross-model divergence confined to the low-BCS regime. On Few-NERD NER, the effect was not robustly detectable, likely due to floor effects at 8B scale and the noisier text-match metric. The pairwise confusability signal explains roughly 1.3--1.7\% of the variance in type confusion---entity frequency, prompt position effects, and type definition quality likely contribute to the remaining variance. Our decomposition experiments test only union-based merge strategies; calibration-aware or joint-decoding alternatives remain unexplored. We conducted a within-dataset $2\!\times\!2$ factorial analysis (count $\times$ BCS) on Few-NERD; the interaction term was directionally consistent but not statistically significant ($z = -0.67$, $p = 0.50$), possibly due to BCS range compression in high-count schemas. The primary evidence for count--confusability interaction remains the $3.4\times$ amplification observed across FewRel schema scales (\S\ref{sec:bcs_controlled}). An intermediate evaluation at 40-relation subsets sampled from the 80-relation pool (accuracy 0.588, BCS $\Delta = -33.3$\,pp at count 8) confirms monotonic decline, but this is not an independent schema---all 40-relation subsets draw from the same 80-type pool, so the 16-to-80 amplification ($3.4\times$) remains a two-point comparison. The $3.4\times$ amplification is a point estimate; propagating the 80-rel CI ([17.7, 42.7]\,pp) against the 9.1\,pp baseline yields a range of $1.9\text{--}4.7\times$
…[truncated 1029 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 106 · 2026-05-16T01:05:43.208770+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
  "offset": "59",
  "limit": "50"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
    "offset": "59",
    "limit": "50"
  }
}
```

</details>

---


### Tool result

_source line 107 · 2026-05-16T01:05:43.209305+00:00_

59	\caption{Cross-model count-curve replication on Few-NERD (text-match recall). Both models show a general declining trend in recall with schema size. Per-batch correlation $r = 0.725$. Qwen3-32B values use the v2 prompt (\S\ref{sec:model}) for fair cross-model comparison; the count-curve results in \S\ref{sec:count_curves} use the v1 prompt, yielding higher absolute recall (0.72 vs.\ 0.64 at count${}\,=\,1$) due to over-prediction under v1.}
60	\label{tab:cross_model}
61	\end{table}
62	
63	\begin{table}[h]
64	\centering
65	\small
66	\resizebox{\columnwidth}{!}{%
67	\begin{tabular}{crrrrrr}
68	\toprule
69	& \multicolumn{3}{c}{\textbf{Llama-3.1-8B}} & \multicolumn{3}{c}{\textbf{Qwen3-32B}} \\
70	\cmidrule(lr){2-4} \cmidrule(lr){5-7}
71	\textbf{Count} & \textbf{Low} & \textbf{High} & \textbf{$\Delta$} & \textbf{Low} & \textbf{High} & \textbf{$\Delta$} \\
72	\midrule
73	8 & 78.1\% & 51.0\% & $-$27.1 & 82.3\% & 51.0\% & $-$31.2 \\
74	16 & 75.5\% & 51.6\% & $-$23.9 & 82.8\% & 51.6\% & $-$31.2 \\
75	\bottomrule
76	\end{tabular}}
77	\caption{Cross-model BCS-controlled FewRel accuracy.  High-BCS accuracy converges to $\approx$51\% regardless of model, while low-BCS accuracy reflects model capacity differences.  The confusability gap ($\Delta$, in pp) is 77--87\% as large on Llama-3.1-8B as on Qwen3-32B.}
78	\label{tab:cross_model_bcs}
79	\end{table}
80	
81	\begin{figure}[h]
82	\centering
83	\includegraphics[width=\columnwidth]{../../figures/paper/fig_count_curves.pdf}
84	\caption{Count-degradation curves across three IE tasks. NER recall generally declines and RE accuracy declines monotonically with schema size; MAVEN relaxed F1 increases, reflecting same-domain disambiguation benefits (\S\ref{sec:centrality_confound}).}
85	\label{fig:count_curves}
86	\end{figure}
87	
88	\begin{figure}[h]
89	\centering
90	\includegraphics[width=\columnwidth]{../../figures/paper/fig_bcs_scaling.pdf}
91	\caption{BCS-controlled FewRel accuracy. The confusability gap between low-BCS and high-B
…[truncated 629 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 108 · 2026-05-16T01:06:03.024556+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/paper/discussion*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/paper/discussion*",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction"
  }
}
```

</details>

---


### Tool result

_source line 109 · 2026-05-16T01:06:03.025263+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/discussion.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 110 · 2026-05-16T01:06:06.289566+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 111 · 2026-05-16T01:06:06.289957+00:00_

1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	We isolated schema-induced degradation into count-driven recall decline and confusability-driven type confusion, showed these channels are separable in RE but interact in NER, and confirmed that both channels replicate across model families on RE (Meta-Llama-3.1-8B-Instruct: count $r = 0.725$, confusability $\Delta = -27$\,pp), with high-BCS accuracy converging to a model-invariant floor. We further identified a centrality confound on same-domain schemas and demonstrated that merge amplification is the bottleneck for decompose-then-merge pipelines. Cross-batch calibration or joint decoding is the key next step.
5	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 112 · 2026-05-16T01:06:13.326381+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
  "offset": "0",
  "limit": "30"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
    "offset": "0",
    "limit": "30"
  }
}
```

</details>

---


### Tool result

_source line 113 · 2026-05-16T01:06:13.326809+00:00_

0	\documentclass[11pt]{article}
1	
2	\usepackage[review]{acl}
3	
4	\usepackage{times}
5	\usepackage{latexsym}
6	\usepackage[T1]{fontenc}
7	\usepackage[utf8]{inputenc}
8	\usepackage{microtype}
9	\usepackage{graphicx}
10	\usepackage{booktabs}
11	\usepackage{amsmath}
12	\usepackage{enumitem}
13	
14	\title{Does Type Confusability Drive Schema-Induced Degradation\\in Training-Free LLM Information Extraction?}
15	
16	\author{Anonymous}
17	
18	\begin{document}
19	\maketitle
20	
21	\input{abstract}
22	
23	\input{introduction}
24	
25	\input{related_work}
26	
27	\input{experimental_setup}
28	
29	\input{results}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 114 · 2026-05-16T01:06:18.951774+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

```json
{
  "description": "Read results and setup tex",
  "prompt": "Read the following LaTeX files in full and provide their complete content:\n\n1. /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex\n2. /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/sdgd_negative.tex\n3. /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/experimental_setup.tex\n\nFor each file, provide the COMPLETE LaTeX source text — every line, every table, every number. Do not summarize. This is for a peer review where every detail matters.",
  "subagent_type": "general-purpose"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Agent",
  "tool_args": {
    "description": "Read results and setup tex",
    "prompt": "Read the following LaTeX files in full and provide their complete content:\n\n1. /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex\n2. /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/sdgd_negative.tex\n3. /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/experimental_setup.tex\n\nFor each file, provide the COMPLETE LaTeX source text — every line, every table, every number. Do not summarize. This is for a peer review where every detail matters.",
    "subagent_type": "general-purpose"
  }
}
```

</details>

---


### Tool call

_source line 115 · 2026-05-16T01:06:22.265937+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex"
  }
}
```

</details>

---


### Tool result

_source line 116 · 2026-05-16T01:06:22.618001+00:00_

1	\section{Results}
2	\label{sec:results}
3	
4	\subsection{Count-Degradation Curves}
5	\label{sec:count_curves}
6	
7	We first examine how extraction performance changes as the number of types in the prompt schema increases (Experiment~1; see Figure~\ref{fig:count_curves} in the Appendix for visualizations).
8	
9	\paragraph{NER (Few-NERD).}
10	Recall generally declines from 0.72 at count${}\,=\,1$ to 0.42 at count${}\,=\,64$, a 42\% relative drop, with minor non-monotonicity at intermediate counts (e.g., 0.527 at count${}\,=\,22$ to 0.551 at count${}\,=\,44$). Precision moves in the opposite direction, rising from 0.11 to 0.52, reflecting a shift from over-prediction to under-prediction as more candidate types compete in the prompt. F1 exhibits an inverted-U shape, peaking at intermediate counts where the precision--recall trade-off is most balanced.
11	
12	\paragraph{RE (FewRel).}
13	Accuracy drops monotonically from 85.7\% at count${}\,=\,1$ through 58.8\% at count${}\,=\,40$ to 50.4\% at count${}\,=\,80$, a near-halving when the model must discriminate among all 80 relation types simultaneously. (The count${}\,=\,40$ evaluation uses 40-relation subsets sampled from the 80-relation pool, not an independent schema.)
14	
15	\paragraph{ED (MAVEN).}
16	In contrast to NER and RE, MAVEN relaxed F1 \emph{increases} from 0.106 at count${}\,=\,1$ to 0.247 at count${}\,=\,44$. This reversal arises from three properties of the MAVEN setup: (i)~trigger-level relaxed matching, which requires only token overlap rather than exact span match; (ii)~MAVEN's 168 event types derive from the FrameNet ontology, forming a same-domain hierarchy where co-presented types provide disambiguating context; and (iii)~extreme class imbalance---rare event types benefit from being presented alongside related types that prime the model toward the correct semantic region. We investigate this reversal further in \S\ref{sec:centrality_confound}.
17	
18	\paragraph{Cross-model replication.}
19	Channel~1 
…[truncated 12248 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 352
}
```

</details>

---


### Tool call

_source line 117 · 2026-05-16T01:06:22.618585+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/sdgd_negative.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/sdgd_negative.tex"
  }
}
```

</details>

---


### Tool result

_source line 118 · 2026-05-16T01:06:22.869917+00:00_

1	\section{Why Naive Decomposition Fails}
2	\label{sec:sdgd}
3	
4	The multi-channel degradation model (\S\ref{sec:results}) raises an interventional question: if confusability drives type confusion, can we decompose the schema so that confusable types never co-occur in the same prompt?  We test this idea with \textbf{Schema-DAG-Guided Decomposition} (SDGD), a method that uses the pairwise SCS matrix to partition types into low-confusability batches, runs extraction independently on each batch, and merges the results.
5	
6	\paragraph{Decomposition protocol.}
7	We construct a thresholded confusability graph $G = (V, E)$ where each type is a vertex and an edge connects types $t_i, t_j$ whenever $\text{SCS}(t_i, t_j) > \tau$. Greedy graph coloring (\textsc{largest\_first}) assigns each type to a color such that no two adjacent---i.e., highly confusable---types share a color. Each color class forms one extraction batch, and predictions are merged via set union. We compare four modes: (i)~\textbf{single\_pass}, the undecomposed baseline; (ii)~\textbf{sdgd\_zero}, SCS-guided partitioning; (iii)~\textbf{random\_batch}, random partitioning with matched batch sizes; and (iv)~\textbf{per\_type}, the extreme case where each type is extracted in isolation, following the strategy of \citet{uniner-2024}. Table~\ref{tab:sdgd_results} summarizes the results on Few-NERD.
8	
9	\paragraph{All decomposition modes degrade F1.}
10	Table~\ref{tab:sdgd_results} reports the outcome.  Single-pass extraction achieves F1\,=\,0.445 (P\,=\,0.563, R\,=\,0.368).  SDGD obtains F1\,=\,0.251 (P\,=\,0.210, R\,=\,0.314), a 44\% relative drop.  Random batching reaches F1\,=\,0.320 (P\,=\,0.249, R\,=\,0.446), and per-type extraction yields F1\,=\,0.292 (P\,=\,0.194, R\,=\,0.586).  Every decomposition mode falls below the single-pass baseline.
11	
12	\begin{table}[t]
13	\centering
14	\small
15	\resizebox{\columnwidth}{!}{%
16	\begin{tabular}{lrccc}
17	\toprule
18	\textbf{Mode} & \textbf{\# Batches} & \text
…[truncated 3015 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 251
}
```

</details>

---


### Tool call

_source line 119 · 2026-05-16T01:06:22.920709+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/experimental_setup.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/experimental_setup.tex"
  }
}
```

</details>

---


### Tool result

_source line 120 · 2026-05-16T01:06:22.971649+00:00_

1	\section{Experimental Setup}
2	\label{sec:experimental_setup}
3	
4	We evaluate how prompt schema size and inter-type confusability affect zero-shot LLM extraction across three information extraction tasks: named entity recognition (NER), relation extraction (RE), and event detection (ED).
5	
6	\subsection{Tasks and Datasets}
7	\label{sec:datasets}
8	
9	\paragraph{Few-NERD (NER).}
10	Few-NERD \cite{fewnerd-2021} provides 66 fine-grained entity types organized into 8 coarse categories (person, location, organization, building, art, product, event, other). The dataset spans diverse domains, making it suitable for cross-domain evaluation. We sample 1{,}000 test instances and evaluate with token-level text matching.
11	
12	\paragraph{FewRel (RE).}
13	FewRel \cite{fewrel-2018} contains 80 relation types sourced from Wikidata. Since the validation split covers only 16 relations, we combine the training and validation splits to obtain the full 80-relation pool required for schema-scale experiments, and sample 1{,}000 balanced instances. Each instance provides a sentence with marked head and tail entities; the task is to classify the relation.
14	
15	\paragraph{MAVEN (ED).}
16	MAVEN \cite{maven-2020} defines 168 event types derived from the FrameNet ontology, making it a same-domain schema. We use the validation set (8{,}042 sentences containing 18{,}904 event mentions) for evaluation, as test set labels are not publicly available. The task requires both trigger identification and event type classification.
17	
18	Table~\ref{tab:datasets} summarizes the dataset statistics, including the Schema Confusability Score (SCS) ranges defined in \S\ref{sec:scs}.
19	
20	\begin{table}[t]
21	\centering
22	\small
23	\resizebox{\columnwidth}{!}{%
24	\begin{tabular}{llrrlll}
25	\toprule
26	\textbf{Dataset} & \textbf{Task} & \textbf{\# Types} & \textbf{\# Eval Units} & \textbf{Domain} & \textbf{BCS Range} & \textbf{Embedding} \\
27	\midrule
28	Few-NERD & NER & 66 & 1{,}000 & Cross & 0.77-
…[truncated 6755 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 121 · 2026-05-16T01:09:28.332405+00:00_

Here are the complete contents of all three files.

---

## File 1: `/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex`

```latex
\section{Results}
\label{sec:results}

\subsection{Count-Degradation Curves}
\label{sec:count_curves}

We first examine how extraction performance changes as the number of types in the prompt schema increases (Experiment~1; see Figure~\ref{fig:count_curves} in the Appendix for visualizations).

\paragraph{NER (Few-NERD).}
Recall generally declines from 0.72 at count${}\,=\,1$ to 0.42 at count${}\,=\,64$, a 42\% relative drop, with minor non-monotonicity at intermediate counts (e.g., 0.527 at count${}\,=\,22$ to 0.551 at count${}\,=\,44$). Precision moves in the opposite direction, rising from 0.11 to 0.52, reflecting a shift from over-prediction to under-prediction as more candidate types compete in the prompt. F1 exhibits an inverted-U shape, peaking at intermediate counts where the precision--recall trade-off is most balanced.

\paragraph{RE (FewRel).}
Accuracy drops monotonically from 85.7\% at count${}\,=\,1$ through 58.8\% at count${}\,=\,40$ to 50.4\% at count${}\,=\,80$, a near-halving when the model must discriminate among all 80 relation types simultaneously. (The count${}\,=\,40$ evaluation uses 40-relation subsets sampled from the 80-relation pool, not an independent schema.)

\paragraph{ED (MAVEN).}
In contrast to NER and RE, MAVEN relaxed F1 \emph{increases} from 0.106 at count${}\,=\,1$ to 0.247 at count${}\,=\,44$. This reversal arises from three properties of the MAVEN setup: (i)~trigger-level relaxed matching, which requires only token overlap rather than exact span match; (ii)~MAVEN's 168 event types derive from the FrameNet ontology, forming a same-domain hierarchy where co-presented types provide disambiguating context; and (iii)~extreme class imbalance---rare event types benefit from being presented alongside related types that prime the model toward the correct sem
…[truncated 25994 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Agent",
  "elapsed_ms": 189380
}
```

</details>

---


### Tool call

_source line 122 · 2026-05-16T01:10:16.565993+00:00_

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
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
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

_source line 123 · 2026-05-16T01:10:16.616728+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 124 · 2026-05-16T01:10:19.831537+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL ARR 2026 reviewer guidelines review form criteria scoring"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR 2026 reviewer guidelines review form criteria scoring"
  }
}
```

</details>

---


### Tool result

_source line 125 · 2026-05-16T01:10:28.617903+00:00_

Web search results for query: "ACL ARR 2026 reviewer guidelines review form criteria scoring"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"aclrollingreview/reviewing.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/reviewing.md"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"}]

Based on the search results, here's information about ACL ARR 2026 reviewer guidelines, review form criteria, and scoring:

## Reviewer Scores

Starting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, 
…[truncated 1737 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 8786
}
```

</details>

---


### Tool call

_source line 126 · 2026-05-16T01:10:31.479182+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review review form soundness excitement overall score scale 1-5 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review review form soundness excitement overall score scale 1-5 2025 2026"
  }
}
```

</details>

---


### Tool result

_source line 127 · 2026-05-16T01:10:38.458439+00:00_

Web search results for query: "ACL Rolling Review review form soundness excitement overall score scale 1-5 2025 2026"

Links: [{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ACL 2023 Acceptance Recommendations - ACL 2023","url":"https://2023.aclweb.org/blog/overall-recommendation/"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"Program Chairs’ Report on Peer Review at ACL 2023 Anna Rogers}","url":"https://aclanthology.org/2023.acl-long.report.pdf"},{"title":"aclrollingreview/reviewform.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/reviewform.md"},{"title":"ACL 2026 on X: \"Checkout the blog post on the soundness/excitement scores https://t.co/AKSO9DjiYP . It clarifies the reasoning behind the separation of overall scores and how it might make the reviewer recommendation more robust. #ACL2023Toronto #ACL2023NLP #NLProc\" / X","url":"https://x.com/aclmeeting/status/1637827267173953540"},{"title":"ACL’23 Peer Review Form - ACL 2023","url":"https://2023.aclweb.org/blog/review-form/"},{"title":"aclrollingreview/reviewerguidelines.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/reviewerguidelines.md"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"}]

Based on the search results, here is information about the ACL Rolling Review (ARR) review form, specifically regarding the soundness, excitemen
…[truncated 1552 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 6979
}
```

</details>

---


### Tool call

_source line 128 · 2026-05-16T01:10:42.828187+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__review_reviewer_post_to_director",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__review_reviewer_post_to_director",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 129 · 2026-05-16T01:10:42.878776+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 130 · 2026-05-16T01:14:16.181488+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 1 交叉回应 — 逐条回应 Reviewer 2 审稿意见\n\n已通读论文全文（正文 + 附录 + LaTeX 源码），以下逐条回应 R2 的 Weakness 和 Question。\n\n---\n\n### Weaknesses 逐条回应\n\n**[AGREE] R2-W1: 正文零 figure，关键结果缺乏视觉呈现**\n\n完全同意，这是严重的呈现缺陷。我确认所有 `\\includegraphics` 命令仅出现在 `\\appendix` 之后（main.tex L81–100）。Fig 1（count curves）、Fig 2（BCS scaling）、Fig 3（error taxonomy）全部放在附录。12 页 PDF 中，前 8 页为正文，9–10 页为 references，附录的 2 张表 + 3 张图被挤到最后 1–2 页。Reviewer 评估正文时完全看不到最核心的 empirical evidence。对于一篇以实证发现为核心贡献的论文，这不可接受。\n\n---\n\n**[PARTIALLY AGREE] R2-W2: Pairwise SCS r² < 2%，\"robust predictor\" overclaiming**\n\n部分同意。r² = 0.013–0.017 的解释力确实极弱，Contribution 2 用 \"robust predictor\" 容易产生误解。但有两点 nuance：\n\n(1) **\"Robust\" 的语义**：Contribution 2 原文是 \"Pairwise confusability as a robust predictor. We demonstrate that pairwise SCS predicts type confusion across tasks and embedding models\"。结合正文 §4.2 明确说 \"modest in magnitude\" 和 \"one factor among several\"，\"robust\" 更可能指 \"可复现性强\"（跨任务、跨 embedding、survive bootstrap），而非 \"效应量大\"。问题在于 contribution list 的简短表述有误导性，正文措辞是审慎的。\n\n(2) **Selection bias 的严重程度**：R2 担心 conditioning on nonzero pairs (ρ = 0.27–0.31) 有 selection bias。但论文将此作为补充分析，主结论基于全样本 r = 0.112–0.129。Zero-inflation 来自结构性稀疏——大多数 type pair 从未同时出现在同一 batch，confusion rate 自然为 0——这不等于 SCS 无效。但我同意应改为 \"statistically significant but modest predictor\" 并详细讨论剩余 98% variance 的来源。\n\n---\n\n**[PARTIALLY AGREE] R2-W3: 3.4× amplification 基于两点比较，统计支撑不足**\n\n部分同意，但论文比 R2 描述的更透明。\n\nTable 3 caption 明确说：\"The 16-relation condition used a single extreme batch per BCS level; bootstrap CIs require multiple batches\"。Limitations section 进一步承认：\"the 16-to-80 amplification (3.4×) remains a two-point comparison\" 并给出 CI-propagated range 1.9–4.7×。论文还说明 40-rel 中间点 \"is not an independent schema—all 40-relation subsets draw from the same 80-type pool\"（§4.1 和 Limitations）。所以 R2 指出的非独立性和两点比较问题，论文已经 disclosed。\n\n但 R2 的核心问题仍然成立：**16-rel 基线的 Δ = -9.1 pp 无 CI，使得 3.4× 是一个无法量化不确定性的 ratio**。从 16-relation pool 中选 8 个有 C(16,8)=12,870 种组合，理论上可以构造多个 extreme batches。如果 BCS 分布在 16-rel pool 中过于集中导致只有一个有意义的 extreme batch，这本身就值得报告。建议作者补充 16-rel 多 batch 实验或解释技术障碍。\n\n此外，80-rel 条件本身的证据是稳固的：count=8 和 count=16 两个水平均给出 Δ ≈ 31.2 pp 且 CI 不含 0（[17.7, 42.7] 和 [22.9, 39.6]），cross-model validation 也确认了类似幅度（Llama: Δ = -27.1 pp 和 -23.9 pp）。**核心问题不在于 confusability effect 是否存在，而在于 amplification ratio 的精确估计。**\n\n---\n\n**[AGREE] R2-W4: 无 Discussion section**\n\n完全同意。我确认 discussion.tex 仅包含一个 4 行 Conclusion（main.tex L34 `\\input{discussion}` → discussion.tex 仅 `\\section{Conclusion}` 加 4 句话）。\n\n对于一篇发现复杂且部分矛盾的结果（MAVEN 反转、centrality confound、SDGD 失败、NER 两通道交互）的论文，缺少 Discussion 是严重缺陷。需要至少讨论：(1) 两通道模型的理论边界条件；(2) SCS/BCS 在 same-domain vs cross-domain schema 下的差异化使用指南；(3) merge amplification 的可能解决方向（论文已尝试 confidence-gated merge 但未在 Discussion 中展开）；(4) 对实际 schema 设计的操作性建议。\n\n---\n\n**[PARTIALLY AGREE] R2-W5: MAVEN 矛盾限制 generalizability**\n\n部分同意，但 R2 低估了论文对此的处理深度。\n\n§4.5 对 MAVEN 反转提供了完整的因果解释：same-domain schema 导致 embeddings collapse into single cluster（引用 Cai et al. 2021），centrality signal 压过 confusability signal，翻转聚合层相关性。关键是 pairwise SCS–confusion correlation 在 MAVEN 上仍然完好（r = 0.129, CI [0.104, 0.156], p < 10⁻¹⁰），问题仅出在 mean BCS 聚合步骤。论文还给出实践指导：\"mean BCS is a reliable predictor of schema difficulty only for cross-domain schemas\"。\n\n但我同意 generalizability 的确被缩小了。论文的两个核心应用层面——per-type error 预测和 count curve 趋势——在 MAVEN 上都失效或反转。这意味着主要发现仅在 cross-domain schema（Few-NERD + FewRel）上完整成立。考虑到实际应用中 same-domain schema 很常见（如医疗 NER、法律 RE），这是一个实质性的适用范围限制，值得在 Discussion（如果有的话）中充分讨论。\n\n---\n\n**[AGREE] R2-W6: v1 vs v2 prompt 不一致**\n\n同意。NER count curves（§4.1）和 BCS-controlled NER 实验使用 v1 prompt（96.5% offset fabrication），后续实验全部使用 v2。虽然 text matching 评估不受 offset fabrication 直接影响，但 v1 要求 offsets 可能改变模型的 capacity allocation（同时执行定位 + 分类 vs 纯分类）。\n\n附录 Table 6 提供了关键证据：v1 recall at count=1 为 0.72，v2 为 0.64，差异 8 pp。这说明 prompt 版本确实改变了提取行为（v1 的 over-prediction 趋势）。这使得 §4.1 NER count curves 与 §4.4 error taxonomy 分析之间的对比不够干净——前者基于 v1 行为，后者基于 v2。\n\n---\n\n**[AGREE] R2-W7: Limitations section 结构差**\n\n同意。main.tex L36–37 是一个约 20 行的密集段落，涵盖模型限制、variance 解释、merge 策略、interaction term 不显著、amplification 两点比较、BCS metric 局限等多个议题，但全部挤在一个段落中。结构化为分点列表并标注严重程度会大幅改善可读性和可评估性。\n\n---\n\n**[AGREE] R2-W8: MiniLM 引用错误**\n\n同意。LaTeX 源码 `\\cite{minilm-2019}` 指向 Reimers and Gurevych 2019 (Sentence-BERT)，references 中有脚注 \"All-MiniLM-L6-v2 is a distilled variant\"。但 all-MiniLM-L6-v2 基于 MiniLM 架构，应引用 Wang et al. 2020 (NeurIPS) 的 MiniLM 原始论文。当前引用不准确。\n\n---\n\n**[AGREE] R2-W9: 缺少 Responsible NLP Research Checklist**\n\n同意。ACL ARR 提交要求附带此 checklist。\n\n---\n\n**[AGREE] R2-W10: FewRel 合并 train+val split**\n\n同意，但问题不严重。§3.1 解释了原因（val split 仅 16 relations，不足以支持 schema-scale 实验）。建议更显著地讨论潜在影响——train split 的 relation 分布可能不同，合并后的 1,000 balanced instances 是否仍然 representative。\n\n---\n\n**[AGREE] R2-W11: \"model\" vs \"framework\"**\n\n同意。\"Multi-channel degradation model\" 描述的是经验性分类体系（count channel + confusability channel），不是可参数化/可 fit 的统计模型。\"Framework\" 或 \"taxonomy\" 更准确，避免混淆。\n\n---\n\n### Questions 回应\n\n**Q1** (16-rel 为何仅一个 extreme batch？)\n我也认为这需要解释。C(16,8)=12,870 种可能的 8-type batch，应足以构造多个 extreme batches。可能的 barrier：16-rel pool 的 BCS 分布很窄（Table 1 的 BCS Range 0.42–0.97 是全 80-rel pool，16-rel 子集的范围会更小），导致 \"extreme\" 选择空间有限。但这应被明确报告。\n\n**Q2** (Residualized BCS？)\n优秀建议，我强烈支持。对 MAVEN 的 mean BCS 进行 centrality 残差化（regress out 与 cluster centroid 的 distance）可能恢复预期方向的相关性，同时为 centrality confound 解释提供因果性检验。\n\n**Q3** (v1 offset fabrication 对 type discrimination 的影响？)\n重要问题。v1 要求 offsets 迫使模型同时执行定位 + 分类，可能改变 capacity allocation。Table 6 已显示 v1 vs v2 行为不同（recall 0.72 vs 0.64）。建议补充 v1 vs v2 的 per-type confusion matrix 对比，或至少在 v2 上重跑 NER count curves 以确认趋势一致。\n\n**Q4** (SDGD 仅在 NER 上测试？)\n同意应扩展。RE 是更干净的测试场（Channel 2 与 Channel 1 可分离，§4.4）。且 RE 每个 instance 只有一个 gold relation，merge 冲突的性质与 NER（多 entity spans 重叠）不同，merge amplification 的表现可能有差异。补充说明：Table 5 显示作者还测试了 confidence-gated merge (v2 mode)，虽然 F1 仍低于 baseline，但说明作者已探索了 alternatives——R2 审查未提及这一点。\n\n**Q5** (Non-zero temperature？)\n次要问题。Temperature=0 是 zero-shot IE 的标准设置，论文使用 greedy decoding 确保确定性和可复现性。Non-zero temperature 可能增加输出噪声，掩盖 confusability signal。学术上有意义但不影响当前贡献。\n\n---\n\n### Missing References 回应\n\n1. **\"Reflect then Learn\" (AAAI 2026)**——如涉及 confusion-aware prompting for IE，高度相关，应引用。\n2. **MiniLM 原始论文 (Wang et al., 2020, NeurIPS)**——必须引用，与 W8 一致。\n3. **Sclar et al. 2024 (TACL) prompt sensitivity**——与 v1/v2 差异讨论直接相关，应引用。\n\n---\n\n### 与我审查发现的一致/补充\n\nR2 的审查与我的关注高度一致。我补充以下 R2 未覆盖的发现：\n\n1. **FewRel 未进行 pairwise SCS 分析**：§4.2 解释原因（RE 是 per-instance classification，confusion matrix 不可比），但这意味着 Contribution 2 \"pairwise SCS predicts type confusion across tasks\" 的跨任务泛化性只有 NER + ED 两个数据点，FewRel 的 confusability 证据完全来自 BCS-controlled 实验（interventional 而非 correlational）。应明确承认这一 asymmetry。\n\n2. **Confidence-gated merge**：Table 5 包含 v2 结果（sdgd_zero v2: F1=0.241, random_batch v2: F1=0.301），虽然 F1 仍低于 baseline (0.445)，但 precision 有改善（sdgd: 0.210→0.324）。论文引用 LLM calibration 文献（Geng et al., 2024）解释失败。R2 的审查完全未提及这些 v2 结果——这是作者对 merge problem 的积极探索，体现了研究的 thoroughness。\n\n3. **NER 两通道交互未量化**：§4.4 指出 NER missed rates 与 BCS non-monotonic，暗示 Channel 1 和 Channel 2 交互。Limitations 提到 2×2 factorial 的 interaction term 不显著（z=-0.67, p=0.50）。但论文仍在 abstract 和 introduction 中说 \"confusable type sets additionally impair entity detection\"，这一 claim 的统计支撑不足。\n\n---\n\n### 总体判断\n\nR2 审查质量很高，11 个 Weakness 中我完全同意 8 个，部分同意 3 个（W2、W3、W5）。分歧主要在 severity 而非 direction：论文在正文和 Limitations 中对 W3 和 W5 的处理比 R2 给的 credit 更充分；W2 的 \"robust\" 有语义歧义但确实应修改。\n\n**我同意 R2 的 Borderline (3/5) 评分和 Findings track 推荐。** 实验设计是论文最大的优势，但 effect size 弱、呈现问题（零 figure、无 Discussion）和 generalizability 限制（MAVEN 失效）需要实质修改。",
  "reviewer_id": "1",
  "project": "schema-dag-extraction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 1 交叉回应 — 逐条回应 Reviewer 2 审稿意见\n\n已通读论文全文（正文 + 附录 + LaTeX 源码），以下逐条回应 R2 的 Weakness 和 Question。\n\n---\n\n### Weaknesses 逐条回应\n\n**[AGREE] R2-W1: 正文零 figure，关键结果缺乏视觉呈现**\n\n完全同意，这是严重的呈现缺陷。我确认所有 `\\includegraphics` 命令仅出现在 `\\appendix` 之后（main.tex L81–100）。Fig 1（count curves）、Fig 2（BCS scaling）、Fig 3（error taxonomy）全部放在附录。12 页 PDF 中，前 8 页为正文，9–10 页为 references，附录的 2 张表 + 3 张图被挤到最后 1–2 页。Reviewer 评估正文时完全看不到最核心的 empirical evidence。对于一篇以实证发现为核心贡献的论文，这不可接受。\n\n---\n\n**[PARTIALLY AGREE] R2-W2: Pairwise SCS r² < 2%，\"robust predictor\" overclaiming**\n\n部分同意。r² = 0.013–0.017 的解释力确实极弱，Contribution 2 用 \"robust predictor\" 容易产生误解。但有两点 nuance：\n\n(1) **\"Robust\" 的语义**：Contribution 2 原文是 \"Pairwise confusability as a robust predictor. We demonstrate that pairwise SCS predicts type confusion across tasks and embedding models\"。结合正文 §4.2 明确说 \"modest in magnitude\" 和 \"one factor among several\"，\"robust\" 更可能指 \"可复现性强\"（跨任务、跨 embedding、survive bootstrap），而非 \"效应量大\"。问题在于 contribution list 的简短表述有误导性，正文措辞是审慎的。\n\n(2) **Selection bias 的严重程度**：R2 担心 conditioning on nonzero pairs (ρ = 0.27–0.31) 有 selection bias。但论文将此作为补充分析，主结论基于全样本 r = 0.112–0.129。Zero-inflation 来自结构性稀疏——大多数 type pair 从未同时出现在同一 batch，confusion rate 自然为 0——这不等于 SCS 无效。但我同意应改为 \"statistically significant but modest predictor\" 并详细讨论剩余 98% variance 的来源。\n\n---\n\n**[PARTIALLY AGREE] R2-W3: 3.4× amplification 基于两点比较，统计支撑不足**\n\n部分同意，但论文比 R2 描述的更透明。\n\nTable 3 caption 明确说：\"The 16-relation condition used a single extreme batch per BCS level; bootstrap CIs require multiple batches\"。Limitations section 进一步承认：\"the 16-to-80 amplification (3.4×) remains a two-point comparison\" 并给出 CI-propagated range 1.9–4.7×。论文还说明 40-rel 中间点 \"is not an independent schema—all 40-relation subsets draw from the same 80-type pool\"（§4.1 和 Limitations）。所以 R2 指出的非独立性和两点比较问题，论文已经 disclosed。\n\n但 R2 的核心问题仍然成立：**16-rel 基线的 Δ = -9.1 pp 无 CI，使得 3.4× 是一个无法量化不确定性的 ratio**。从 16-relation pool 中选 8 个有 C(16,8)=12,870 种组合，理论上可以构造多个 extreme batches。如果 BCS 分布在 16-rel pool 中过于集中导致只有一个有意义的 extreme batch，这本身就值得报告。建议作者补充 16-rel 多 batch 实验或解释技术障碍。\n\n此外，80-rel 条件本身的证据是稳固的：count=8 和 count=16 两个水平均给出 Δ ≈ 31.2 pp 且 CI 不含 0（[17.7, 42.7] 和 [22.9, 39.6]），cross-model validation 也确认了类似幅度（Llama: Δ = -27.1 pp 和 -23.9 pp）。**核心问题不在于 confusability effect 是否存在，而在于 amplification ratio 的精确估计。**\n\n---\n\n**[AGREE] R2-W4: 无 Discussion section**\n\n完全同意。我确认 discussion.tex 仅包含一个 4 行 Conclusion（main.tex L34 `\\input{discussion}` → discussion.tex 仅 `\\section{Conclusion}` 加 4 句话）。\n\n对于一篇发现复杂且部分矛盾的结果（MAVEN 反转、centrality confound、SDGD 失败、NER 两通道交互）的论文，缺少 Discussion 是严重缺陷。需要至少讨论：(1) 两通道模型的理论边界条件；(2) SCS/BCS 在 same-domain vs cross-domain schema 下的差异化使用指南；(3) merge amplification 的可能解决方向（论文已尝试 confidence-gated merge 但未在 Discussion 中展开）；(4) 对实际 schema 设计的操作性建议。\n\n---\n\n**[PARTIALLY AGREE] R2-W5: MAVEN 矛盾限制 generalizability**\n\n部分同意，但 R2 低估了论文对此的处理深度。\n\n§4.5 对 MAVEN 反转提供了完整的因果解释：same-domain schema 导致 embeddings collapse into single cluster（引用 Cai et al. 2021），centrality signal 压过 confusability signal，翻转聚合层相关性。关键是 pairwise SCS–confusion correlation 在 MAVEN 上仍然完好（r = 0.129, CI [0.104, 0.156], p < 10⁻¹⁰），问题仅出在 mean BCS 聚合步骤。论文还给出实践指导：\"mean BCS is a reliable predictor of schema difficulty only for cross-domain schemas\"。\n\n但我同意 generalizability 的确被缩小了。论文的两个核心应用层面——per-type error 预测和 count curve 趋势——在 MAVEN 上都失效或反转。这意味着主要发现仅在 cross-domain schema（Few-NERD + FewRel）上完整成立。考虑到实际应用中 same-domain schema 很常见（如医疗 NER、法律 RE），这是一个实质性的适用范围限制，值得在 Discussion（如果有的话）中充分讨论。\n\n---\n\n**[AGREE] R2-W6: v1 vs v2 prompt 不一致**\n\n同意。NER count curves（§4.1）和 BCS-controlled NER 实验使用 v1 prompt（96.5% offset fabrication），后续实验全部使用 v2。虽然 text matching 评估不受 offset fabrication 直接影响，但 v1 要求 offsets 可能改变模型的 capacity allocation（同时执行定位 + 分类 vs 纯分类）。\n\n附录 Table 6 提供了关键证据：v1 recall at count=1 为 0.72，v2 为 0.64，差异 8 pp。这说明 prompt 版本确实改变了提取行为（v1 的 over-prediction 趋势）。这使得 §4.1 NER count curves 与 §4.4 error taxonomy 分析之间的对比不够干净——前者基于 v1 行为，后者基于 v2。\n\n---\n\n**[AGREE] R2-W7: Limitations section 结构差**\n\n同意。main.tex L36–37 是一个约 20 行的密集段落，涵盖模型限制、variance 解释、merge 策略、interaction term 不显著、amplification 两点比较、BCS metric 局限等多个议题，但全部挤在一个段落中。结构化为分点列表并标注严重程度会大幅改善可读性和可评估性。\n\n---\n\n**[AGREE] R2-W8: MiniLM 引用错误**\n\n同意。LaTeX 源码 `\\cite{minilm-2019}` 指向 Reimers and Gurevych 2019 (Sentence-BERT)，references 中有脚注 \"All-MiniLM-L6-v2 is a distilled variant\"。但 all-MiniLM-L6-v2 基于 MiniLM 架构，应引用 Wang et al. 2020 (NeurIPS) 的 MiniLM 原始论文。当前引用不准确。\n\n---\n\n**[AGREE] R2-W9: 缺少 Responsible NLP Research Checklist**\n\n同意。ACL ARR 提交要求附带此 checklist。\n\n---\n\n**[AGREE] R2-W10: FewRel 合并 train+val split**\n\n同意，但问题不严重。§3.1 解释了原因（val split 仅 16 relations，不足以支持 schema-scale 实验）。建议更显著地讨论潜在影响——train split 的 relation 分布可能不同，合并后的 1,000 balanced instances 是否仍然 representative。\n\n---\n\n**[AGREE] R2-W11: \"model\" vs \"framework\"**\n\n同意。\"Multi-channel degradation model\" 描述的是经验性分类体系（count channel + confusability channel），不是可参数化/可 fit 的统计模型。\"Framework\" 或 \"taxonomy\" 更准确，避免混淆。\n\n---\n\n### Questions 回应\n\n**Q1** (16-rel 为何仅一个 extreme batch？)\n我也认为这需要解释。C(16,8)=12,870 种可能的 8-type batch，应足以构造多个 extreme batches。可能的 barrier：16-rel pool 的 BCS 分布很窄（Table 1 的 BCS Range 0.42–0.97 是全 80-rel pool，16-rel 子集的范围会更小），导致 \"extreme\" 选择空间有限。但这应被明确报告。\n\n**Q2** (Residualized BCS？)\n优秀建议，我强烈支持。对 MAVEN 的 mean BCS 进行 centrality 残差化（regress out 与 cluster centroid 的 distance）可能恢复预期方向的相关性，同时为 centrality confound 解释提供因果性检验。\n\n**Q3** (v1 offset fabrication 对 type discrimination 的影响？)\n重要问题。v1 要求 offsets 迫使模型同时执行定位 + 分类，可能改变 capacity allocation。Table 6 已显示 v1 vs v2 行为不同（recall 0.72 vs 0.64）。建议补充 v1 vs v2 的 per-type confusion matrix 对比，或至少在 v2 上重跑 NER count curves 以确认趋势一致。\n\n**Q4** (SDGD 仅在 NER 上测试？)\n同意应扩展。RE 是更干净的测试场（Channel 2 与 Channel 1 可分离，§4.4）。且 RE 每个 instance 只有一个 gold relation，merge 冲突的性质与 NER（多 entity spans 重叠）不同，merge amplification 的表现可能有差异。补充说明：Table 5 显示作者还测试了 confidence-gated merge (v2 mode)，虽然 F1 仍低于 baseline，但说明作者已探索了 alternatives——R2 审查未提及这一点。\n\n**Q5** (Non-zero temperature？)\n次要问题。Temperature=0 是 zero-shot IE 的标准设置，论文使用 greedy decoding 确保确定性和可复现性。Non-zero temperature 可能增加输出噪声，掩盖 confusability signal。学术上有意义但不影响当前贡献。\n\n---\n\n### Missing References 回应\n\n1. **\"Reflect then Learn\" (AAAI 2026)**——如涉及 confusion-aware prompting for IE，高度相关，应引用。\n2. **MiniLM 原始论文 (Wang et al., 2020, NeurIPS)**——必须引用，与 W8 一致。\n3. **Sclar et al. 2024 (TACL) prompt sensitivity**——与 v1/v2 差异讨论直接相关，应引用。\n\n---\n\n### 与我审查发现的一致/补充\n\nR2 的审查与我的关注高度一致。我补充以下 R2 未覆盖的发现：\n\n1. **FewRel 未进行 pairwise SCS 分析**：§4.2 解释原因（RE 是 per-instance classification，confusion matrix 不可比），但这意味着 Contribution 2 \"pairwise SCS predicts type confusion across tasks\" 的跨任务泛化性只有 NER + ED 两个数据点，FewRel 的 confusability 证据完全来自 BCS-controlled 实验（interventional 而非 correlational）。应明确承认这一 asymmetry。\n\n2. **Confidence-gated merge**：Table 5 包含 v2 结果（sdgd_zero v2: F1=0.241, random_batch v2: F1=0.301），虽然 F1 仍低于 baseline (0.445)，但 precision 有改善（sdgd: 0.210→0.324）。论文引用 LLM calibration 文献（Geng et al., 2024）解释失败。R2 的审查完全未提及这些 v2 结果——这是作者对 merge problem 的积极探索，体现了研究的 thoroughness。\n\n3. **NER 两通道交互未量化**：§4.4 指出 NER missed rates 与 BCS non-monotonic，暗示 Channel 1 和 Channel 2 交互。Limitations 提到 2×2 factorial 的 interaction term 不显著（z=-0.67, p=0.50）。但论文仍在 abstract 和 introduction 中说 \"confusable type sets additionally impair entity detection\"，这一 claim 的统计支撑不足。\n\n---\n\n### 总体判断\n\nR2 审查质量很高，11 个 Weakness 中我完全同意 8 个，部分同意 3 个（W2、W3、W5）。分歧主要在 severity 而非 direction：论文在正文和 Limitations 中对 W3 和 W5 的处理比 R2 给的 credit 更充分；W2 的 \"robust\" 有语义歧义但确实应修改。\n\n**我同意 R2 的 Borderline (3/5) 评分和 Findings track 推荐。** 实验设计是论文最大的优势，但 effect size 弱、呈现问题（零 figure、无 Discussion）和 generalizability 限制（MAVEN 失效）需要实质修改。",
    "reviewer_id": "1",
    "project": "schema-dag-extraction"
  }
}
```

</details>

---


### Tool result

_source line 131 · 2026-05-16T01:14:20.048459+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3866
}
```

</details>

---


### Assistant

_source line 132 · 2026-05-16T01:14:28.925564+00:00_

交叉回应已提交给 Review Director。

逐条回应了 R2 的 11 个 Weakness 和 5 个 Question：
- **完全同意 8 个**：W1（零 figure）、W4（无 Discussion）、W7（Limitations 结构）、W8（MiniLM 引用）、W9（checklist）、W10（FewRel split）、W11（"model"术语）、W6（v1/v2 不一致）
- **部分同意 3 个**：W2（"robust" 有语义歧义，正文措辞比 contribution list 审慎）、W3（论文已 disclose 两点比较局限，但 16-rel 无 CI 仍是问题）、W5（论文对 MAVEN 反转的分析比 R2 给的 credit 更充分，但 generalizability 确实被缩小）

额外补充了 R2 未覆盖的 3 个发现：FewRel 缺失 pairwise 分析的 asymmetry、Table 5 confidence-gated merge (v2) 结果被 R2 忽略、NER 两通道交互 claim 统计支撑不足。

总体同意 R2 的 Borderline 3/5 评分和 Findings track 推荐。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1"
}
```

</details>

---


## Round 3

## Round 3

44 recorded events


### User

_source line 133 · 2026-05-16T02:48:07.373015+00:00_

[Round 1 审稿请求]:
## Round 1 审稿任务 — Reviewer 1

### 你的审查侧重：方法严谨性 + 实验设计 + 统计分析

### Venue 信息
- **目标**: EMNLP 2026 Main Conference (via ARR May 2026 cycle)
- **截止日期**: 2026-05-25
- **页数限制**: 8 页正文 + 无限参考文献 + Limitations（不计页数）
- **模板**: ACL style (`\usepackage[review]{acl}`)
- **匿名规则**: Double-blind

### 论文文件
- 主文件: `projects/schema-dag-extraction/docs/paper/main.tex`
- 各节: `abstract.tex`, `introduction.tex`, `related_work.tex`, `experimental_setup.tex`, `results.tex`, `sdgd_negative.tex`, `discussion.tex`
- 参考文献: `references.bib`

### 审查要求

请以 EMNLP 最严格审稿人的标准评审此论文，重点关注：

1. **实验设计严谨性**
   - Count curves 和 BCS-controlled 实验的设计是否充分控制了混淆变量？
   - 样本量（n=25/27 batches, 1000 test instances）是否足够？bootstrap CI 的使用是否恰当？
   - 三个数据集（Few-NERD/FewRel/MAVEN）的选择是否合理？评估指标是否恰当？

2. **统计分析**
   - Pairwise SCS r²=1.3-1.7% 的效应量是否足以支撑论文声称？framing 是否诚实？
   - Within-pool permutation test (p=0.436) 的解读是否正确？
   - BCS-controlled 实验中 16-rel 单 batch vs 80-rel 多 batch 的统计功效差异是否被充分讨论？
   - MAVEN centrality confound 的 partial correlation 分析是否方法论正确？

3. **Claims vs Evidence 对齐**
   - 四个 contribution 是否都有充分实验支撑？
   - "Multi-channel degradation framework" 是否过度声称？（是 framework 还是 empirical observation？）
   - SDGD 负面结果的讨论是否充分？是否过度泛化？
   - 跨模型验证（Llama-3.1-8B）的范围和深度是否足够支持泛化声称？

4. **可复现性**
   - 实验细节是否足以复现？prompt 模板是否公开？
   - v1/v2 prompt 切换是否引入跨实验混淆？
   - 随机种子、bootstrap 参数是否完整报告？

### Round 1 遗留关键问题（供参考验证是否已修复）
- MW1: 3.4× amplification 统计基础（需 CI + within-pool 控制）
- MW2: r²=1.3% "robust predictor" framing
- MW3: NER factorial p=0.505 但正文称 "interact"
- SW3: v1/v2 prompt 切换混淆
- Q1: 16-rel 为何仅一个 extreme batch

请输出完整审稿意见，格式：Summary → Strengths → Weaknesses（逐条编号 W1/W2/...，标注严重程度 [Critical/Major/Minor]）→ Questions → Missing References → Overall Assessment（评分 + 置信度）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 134 · 2026-05-16T02:48:22.008624+00:00_

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
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
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

_source line 135 · 2026-05-16T02:48:22.009083+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 136 · 2026-05-16T02:48:33.272234+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL ARR 2026 reviewer guidelines review form criteria scoring"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR 2026 reviewer guidelines review form criteria scoring"
  }
}
```

</details>

---


### Tool call

_source line 137 · 2026-05-16T02:48:33.826032+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 reviewer guidelines review form"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 reviewer guidelines review form"
  }
}
```

</details>

---


### Tool call

_source line 138 · 2026-05-16T02:48:33.977203+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "projects/schema-dag-extraction/docs/paper/*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Glob",
  "tool_args": {
    "pattern": "projects/schema-dag-extraction/docs/paper/*.tex"
  }
}
```

</details>

---


### Tool result

_source line 139 · 2026-05-16T02:48:34.027751+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 140 · 2026-05-16T02:48:34.028114+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "projects/schema-dag-extraction/docs/paper/*.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Glob",
  "tool_args": {
    "pattern": "projects/schema-dag-extraction/docs/paper/*.bib"
  }
}
```

</details>

---


### Tool result

_source line 141 · 2026-05-16T02:48:34.078480+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 142 · 2026-05-16T02:48:40.729144+00:00_

Web search results for query: "EMNLP 2026 reviewer guidelines review form"

Links: [{"title":"FAQ - EMNLP 2026","url":"https://2026.emnlp.org/faq/"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"EMNLP 2026 | OpenReview","url":"https://openreview.net/group?id=EMNLP%2F2026"},{"title":"EMNLP | OpenReview","url":"https://openreview.net/group?id=EMNLP"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"ARR Reviewer Guidelines","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"Changes to reviewer volunteering requirement and incentives in May 2025 cycle (EMNLP 2025)","url":"http://aclrollingreview.org/incentives2025"},{"title":"EMNLP 2025 (@emnlpmeeting) · X","url":"https://twitter.com/emnlpmeeting"},{"title":"EMNLP 2026 (@emnlpmeeting) / Posts / X","url":"https://x.com/emnlpmeeting"}]

Based on the search results, I found information about EMNLP 2026's review process. Here's what I discovered:

## EMNLP 2026 Review Process Overview

EMNLP 2026 will use ACL Rolling Review (ARR) as a reviewing system, but final decisions will be made by the conference.

Both submissions and commitment of reviewed articles will be performed via the Open Review platform, where authors submit articles to ARR for reviews and meta-reviews from ARR reviewers and action editors, then commit their reviewed articles to EMNLP 2026, where Senior Area Chairs and Program Chairs make acceptance decisions.

## Key Reviewer Requirements and Deadlines

If you receive assignments, your reviews must be completed by July 6, or your meta-reviews by July 29.

All authors are expected to sign up to review; wheth
…[truncated 689 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 6903
}
```

</details>

---


### Tool result

_source line 143 · 2026-05-16T02:48:41.586772+00:00_

Web search results for query: "ACL ARR 2026 reviewer guidelines review form criteria scoring"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"aclrollingreview/reviewing.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/reviewing.md"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"}]

Based on the search results, here's information about ACL ARR 2026 reviewer guidelines, review form criteria, and scoring:

## Reviewer Guidelines & Scoring

Starting with February 2025, ARR reviewers are asked to provide three scores: soundness
…[truncated 1660 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 8314
}
```

</details>

---


### Tool call

_source line 144 · 2026-05-16T02:48:55.625146+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete ACL ARR review form including all scoring dimensions, their scales, and descriptions. I need the exact scoring criteria for: soundness, excitement, overall assessment, confidence, reproducibility, and any other dimensions."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the complete ACL ARR review form including all scoring dimensions, their scales, and descriptions. I need the exact scoring criteria for: soundness, excitement, overall assessment, confidence, reproducibility, and any other dimensions."
  }
}
```

</details>

---


### Tool call

_source line 145 · 2026-05-16T02:48:56.428329+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/docs/paper/main.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/docs/paper/main.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18"
  }
}
```

</details>

---


### Tool result

_source line 146 · 2026-05-16T02:48:57.285056+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Glob",
  "elapsed_ms": 856
}
```

</details>

---


### Tool call

_source line 147 · 2026-05-16T02:48:57.285480+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper -name \"*.tex\" -o -name \"*.bib\" 2>/dev/null | head -30",
  "description": "Find paper tex and bib files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper -name \"*.tex\" -o -name \"*.bib\" 2>/dev/null | head -30",
    "description": "Find paper tex and bib files"
  }
}
```

</details>

---


### Tool result

_source line 148 · 2026-05-16T02:48:57.436895+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/sdgd_negative.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/references.bib
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/experimental_setup.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/discussion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/related_work.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Bash",
  "elapsed_ms": 151
}
```

</details>

---


### Tool result

_source line 149 · 2026-05-16T02:49:07.429183+00:00_

# ACL ARR Review Form Scoring Dimensions

## Reviewer Confidence
Scale: 1-5
- **5**: "Positive that my evaluation is correct. I read the paper very carefully and am familiar with related work."
- **4**: Quite sure; unlikely but conceivable to miss important details
- **3**: Pretty sure; good general familiarity but didn't check all details carefully
- **2**: Can defend evaluation but fairly likely to have missed details or novelty assessment
- **1**: Outside expertise area or paper very difficult to understand

## Soundness
Scale: 1-5 (with .5 increments)
- **5**: "Excellent: This study is one of the most thorough I have seen, given its type."
- **4**: Strong; sufficient support with optional additional experiments
- **3**: Acceptable; main claims supported with minor details needing work
- **2**: Poor; main claims lack sufficient support with major technical problems
- **1**: "Major Issues: This study is not yet sufficiently thorough to warrant publication"

## Excitement
Scale: 1-5 (with .5 increments)
- **5**: "Highly Exciting: I would recommend this paper to others and/or attend its presentation"
- **4**: Would mention to others or make effort to attend presentation
- **3**: Might mention points or attend if time permits
- **2**: Doesn't resonate personally but might interest others
- **1**: "Not Exciting: this paper does not resonate with me, and I don't think it would with others"

## Overall Assessment
Scale: 1-5 (with .5 increments)
- **5**: Consider for Award (top 2.5%)
- **4**: Conference acceptance
- **3**: Findings acceptance
- **2**: Resubmit next cycle
- **1**: Do not resubmit

## Reproducibility
Scale: 1-5
- **5**: Results easily reproducible
- **4**: Mostly reproducible with minor variation possible
- **3**: Reproducible with difficulty; underspecified parameters
- **2**: Hard to reproduce; unavailable data or insufficient details
- **1**: Cannot reproduce results

## Datasets & Software
Both scale 1-5:
- **5**: Enabling impact on research choices
- 
…[truncated 122 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 11804
}
```

</details>

---


### Tool call

_source line 150 · 2026-05-16T02:49:18.532199+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 151 · 2026-05-16T02:49:18.884385+00:00_

1	\documentclass[11pt]{article}
2	
3	\usepackage[review]{acl}
4	
5	\usepackage{times}
6	\usepackage{latexsym}
7	\usepackage[T1]{fontenc}
8	\usepackage[utf8]{inputenc}
9	\usepackage{microtype}
10	\usepackage{graphicx}
11	\usepackage{booktabs}
12	\usepackage{amsmath}
13	\usepackage{enumitem}
14	
15	\title{Does Type Confusability Drive Schema-Induced Degradation\\in Training-Free LLM Information Extraction?}
16	
17	\author{Anonymous}
18	
19	\begin{document}
20	\maketitle
21	
22	\input{abstract}
23	
24	\input{introduction}
25	
26	\input{related_work}
27	
28	\input{experimental_setup}
29	
30	\input{results}
31	
32	\input{sdgd_negative}
33	
34	\input{discussion}
35	
36	\section*{Limitations}
37	\begin{enumerate}[leftmargin=*,itemsep=2pt]
38	\item \textbf{Single primary model.} The primary experiments use Qwen3-32B. Channel~1 has been validated on Llama-3.1-8B-Instruct (recall decline $-$43\,pp, $r = 0.725$). Channel~2 was validated on FewRel RE ($\Delta = -27.1$\,pp at count 8, $-23.9$\,pp at count 16), with high-BCS accuracy converging to a model-invariant floor ($\approx$0.51). On Few-NERD NER, Channel~2 was not robustly detectable at 8B scale, likely due to floor effects and the noisier text-match metric.
39	
40	\item \textbf{Modest pairwise effect size.} Pairwise SCS explains 1.3--1.7\% of the variance in type confusion. Entity frequency, prompt position effects, mention ambiguity, context complexity, and type definition quality likely account for the remaining variance.
41	
42	\item \textbf{Cross-pool slope consistency.} The BCS--accuracy slopes are statistically indistinguishable across pools (permutation $p = 0.436$), indicating consistent per-unit sensitivity. The larger absolute gap at 80 relations (31.2\,pp vs.\ 9.1\,pp) reflects the wider BCS range available in that pool, not a stronger underlying effect. A within-pool comparison (Table~\ref{tab:within_pool}) confirms this interpretation: slope $-$0.401, CI excludes zero.
43	
44	\item \textbf{Non-significant fa
…[truncated 11809 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 352
}
```

</details>

---


### Tool call

_source line 152 · 2026-05-16T02:49:18.884997+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 153 · 2026-05-16T02:49:19.337152+00:00_

1	\begin{abstract}
2	Training-free LLM information extraction---prompting models with target schemas without fine-tuning---degrades sharply as schema complexity grows: NER recall drops from 0.72 to 0.42 with 64 candidate types, and RE accuracy falls from 85.7\% to 50.4\% with 80 relations. Prior work conflates type count with type confusability, leaving the mechanisms unclear. We conduct the first controlled empirical study isolating these factors across three IE tasks and three datasets, introducing the Schema Confusability Score (SCS) and two experimental paradigms: count curves that vary schema size while randomizing confusability, and BCS-controlled experiments that fix size while varying confusability. Our experiments reveal two degradation channels: a count channel that generally suppresses recall as candidate types increase, and a confusability channel where semantically similar types trigger intra-batch substitution errors---cleanly separable in RE; in NER, confusability additionally impairs entity detection (same-domain schemas are subject to a centrality confound). The BCS--accuracy relationship is robust across schema sizes: the regression slope is consistent between independent 16-type and within-pool 80-type evaluations (permutation $p = 0.44$), while the wider BCS range at 80 types produces larger absolute accuracy gaps (31.2 vs.\ 9.1\,pp). Both channels replicate on Llama-3.1-8B (count $r = 0.725$; confusability $\Delta = -27$\,pp), with high-BCS accuracy converging to a model-invariant floor. Our confusability-aware decomposition yields an informative negative result: merge amplification destroys precision across all strategies, identifying a structural challenge for union-based merge pipelines in zero-shot IE.
3	\end{abstract}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 154 · 2026-05-16T02:49:19.337517+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 155 · 2026-05-16T02:49:20.253096+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	Training-free LLM information extraction---prompting a large language model with a target schema and asking it to extract structured information without any task-specific fine-tuning---enables rapid deployment across new domains and ontologies. This zero-shot paradigm eliminates the need for labeled data, making it attractive for applications where annotation is expensive or schemas evolve frequently \cite{llm4ie-survey-2024}. Yet the paradigm carries a critical limitation: performance degrades sharply as the number of candidate types in the prompt schema grows. On named entity recognition, recall drops from 0.72 with a single candidate type to 0.42 with 64 types, a 42\% relative decline. On relation extraction, accuracy falls from 85.7\% with one relation to 50.4\% with 80 relations---near halving. This degradation is not academic: real-world ontologies routinely define 50--200+ types, placing them squarely in the regime where training-free extraction becomes unreliable.
5	
6	What causes this schema-induced degradation? Prior work has proposed decomposition strategies that implicitly assume different answers. \citet{uniner-2024} extract each type independently, assuming types can be treated as separable. \citet{llm-pee-2025} partition large event schemas by type embedding similarity before extraction, assuming that semantic overlap between co-presented types drives errors. \citet{parse-2025} rewrite and optimize schema definitions, assuming that description quality is the bottleneck. Each approach improves extraction under certain conditions, but none isolates \emph{why} schemas degrade performance in the first place. The closest work, LLM-PEE \cite{llm-pee-2025}, reduces both the number of co-presented types and their inter-type similarity simultaneously, making it impossible to determine which factor---or what combination---accounts for the observed gains. More broadly, all prior approaches conflate two dis
…[truncated 3768 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 915
}
```

</details>

---


### Tool call

_source line 156 · 2026-05-16T02:49:20.303746+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 157 · 2026-05-16T02:49:20.755685+00:00_

1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\subsection{Training-Free LLM Information Extraction}
5	\label{sec:rw_training_free}
6	
7	Training-free LLM IE spans instruction tuning \cite{instructuie-2023}, code-style schema encoding \cite{knowcoder-2024,codeie-2023}, annotation-guided extraction \cite{gollie-2024,adelie-2024}, schema-driven decoding \cite{slot-2025,oneke-2025}, and constrained JSON decoding \cite{json-schema-bench-2025}. For NER, approaches include zero-shot decomposition \cite{xie-zeroshot-ner-2023,promptner-2023}, distillation \cite{uniner-2024}, bidirectional encoders \cite{gliner-2024,gliner2-2025}, and guided synthesis \cite{guidex-2025,nuner-2024}; \citet{familiarity-2025} quantify label shifts in zero-shot NER evaluation. These methods perform well with moderate schemas (4--20 types) but none investigates how performance degrades as schema complexity scales, nor proposes quantitative metrics for inter-type confusability.
8	
9	\subsection{Schema Complexity in IE}
10	\label{sec:rw_schema}
11	
12	The most directly related work is LLM-PEE \cite{llm-pee-2025}, which addresses event extraction with massive type inventories by partitioning schemas based on type embedding similarity. LLM-PEE clusters event types and assigns each cluster to a separate extraction prompt, demonstrating improved performance on schemas with hundreds of types. Our work is complementary in three respects. First, whereas LLM-PEE develops an engineering solution---partition to improve extraction---we conduct controlled empirical analysis to understand \emph{why} extraction degrades. Second, LLM-PEE does not disentangle the effects of type count from type confusability; their partitioning simultaneously reduces both. Our BCS-controlled experiments (\S\ref{sec:bcs_controlled}) isolate these as independent degradation channels. Third, our pairwise SCS analysis provides a theoretical explanation for why their similarity-based partitioning works: it reduces Batch Confu
…[truncated 1969 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 451
}
```

</details>

---


### Tool call

_source line 158 · 2026-05-16T02:49:20.756160+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/experimental_setup.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/experimental_setup.tex"
  }
}
```

</details>

---


### Tool result

_source line 159 · 2026-05-16T02:49:21.208147+00:00_

1	\section{Experimental Setup}
2	\label{sec:experimental_setup}
3	
4	We evaluate how prompt schema size and inter-type confusability affect zero-shot LLM extraction across three information extraction tasks: named entity recognition (NER), relation extraction (RE), and event detection (ED).
5	
6	\subsection{Tasks and Datasets}
7	\label{sec:datasets}
8	
9	\paragraph{Few-NERD (NER).}
10	Few-NERD \cite{fewnerd-2021} provides 66 fine-grained entity types organized into 8 coarse categories (person, location, organization, building, art, product, event, other). The dataset spans diverse domains, making it suitable for cross-domain evaluation. We sample 1{,}000 test instances and evaluate with token-level text matching.
11	
12	\paragraph{FewRel (RE).}
13	FewRel \cite{fewrel-2018} contains 80 relation types sourced from Wikidata. Since the validation split covers only 16 relations, we combine the training and validation splits to obtain the full 80-relation pool required for schema-scale experiments, and sample 1{,}000 balanced instances (12--13 per relation type, stratified to ensure equal representation). Each instance provides a sentence with marked head and tail entities; the task is to classify the relation.
14	
15	\paragraph{MAVEN (ED).}
16	MAVEN \cite{maven-2020} defines 168 event types derived from the FrameNet ontology, making it a same-domain schema. We use the validation set (8{,}042 sentences containing 18{,}904 event mentions) for evaluation, as test set labels are not publicly available. The task requires both trigger identification and event type classification.
17	
18	Table~\ref{tab:datasets} summarizes the dataset statistics, including the Schema Confusability Score (SCS) ranges defined in \S\ref{sec:scs}.
19	
20	\begin{table}[t]
21	\centering
22	\small
23	\resizebox{\columnwidth}{!}{%
24	\begin{tabular}{llrrlll}
25	\toprule
26	\textbf{Dataset} & \textbf{Task} & \textbf{\# Types} & \textbf{\# Eval Units} & \textbf{Domain} & \textbf{BCS Range} & \textbf{Embe
…[truncated 7260 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 451
}
```

</details>

---


### Tool call

_source line 160 · 2026-05-16T02:49:21.208676+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex"
  }
}
```

</details>

---


### Tool result

_source line 161 · 2026-05-16T02:49:21.361457+00:00_

1	\section{Results}
2	\label{sec:results}
3	
4	\subsection{Count-Degradation Curves}
5	\label{sec:count_curves}
6	
7	\begin{figure}[t]
8	\centering
9	\begin{minipage}[t]{0.48\columnwidth}
10	\centering
11	\includegraphics[width=\linewidth]{../../figures/paper/fig_count_curves.pdf}
12	\end{minipage}
13	\hfill
14	\begin{minipage}[t]{0.48\columnwidth}
15	\centering
16	\includegraphics[width=\linewidth]{../../figures/paper/fig_bcs_scaling.pdf}
17	\end{minipage}
18	\caption{\textbf{(a)} Count-degradation curves across three IE tasks. NER recall generally declines and RE accuracy declines monotonically with schema size; MAVEN relaxed F1 increases (\S\ref{sec:centrality_confound}). \textbf{(b)} BCS-controlled FewRel accuracy. The BCS--accuracy slope is consistent across the independent 16-relation pool and within-pool 16-relation subsets (permutation $p = 0.44$); the wider BCS range available at 80 relations produces larger absolute gaps.}
19	\label{fig:main_results}
20	\end{figure}
21	
22	We first examine how extraction performance changes as the number of types in the prompt schema increases (Experiment~1; Figure~\ref{fig:main_results}a).
23	
24	\paragraph{NER (Few-NERD).}
25	Recall generally declines from 0.72 at count${}\,=\,1$ to 0.42 at count${}\,=\,64$, a 42\% relative drop, with minor non-monotonicity at intermediate counts (e.g., 0.527 at count${}\,=\,22$ to 0.551 at count${}\,=\,44$). Precision moves in the opposite direction, rising from 0.11 to 0.52, reflecting a shift from over-prediction to under-prediction as more candidate types compete in the prompt. F1 exhibits an inverted-U shape, peaking at intermediate counts where the precision--recall trade-off is most balanced.
26	
27	\paragraph{RE (FewRel).}
28	Accuracy drops monotonically from 85.7\% at count${}\,=\,1$ through 58.8\% at count${}\,=\,40$ to 50.4\% at count${}\,=\,80$, a near-halving when the model must discriminate among all 80 relation types simultaneously. (The count${}\,=\,40$ evaluation uses 40
…[truncated 15036 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 152
}
```

</details>

---


### Tool call

_source line 162 · 2026-05-16T02:49:21.713105+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/sdgd_negative.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/sdgd_negative.tex"
  }
}
```

</details>

---


### Tool result

_source line 163 · 2026-05-16T02:49:22.165270+00:00_

1	\section{Why Naive Decomposition Fails}
2	\label{sec:sdgd}
3	
4	Given that confusability drives type confusion, a natural intervention is to partition the schema so confusable types never co-occur. We test this with \textbf{Schema-DAG-Guided Decomposition} (SDGD), which constructs a thresholded confusability graph from the pairwise SCS matrix, applies greedy graph coloring to assign types to low-confusability batches, and merges per-batch predictions via set union (full protocol and per-mode results in Appendix~\ref{sec:appendix_sdgd}).
5	
6	Every decomposition mode produces lower F1 than single-pass extraction on Few-NERD: SDGD achieves F1 = 0.241, random batching 0.320, and per-type extraction 0.292, versus the single-pass baseline of 0.445 (Table~\ref{tab:sdgd_results}). The bottleneck is \emph{merge amplification}: processing the same text across multiple passes with different type subsets accumulates contradictory predictions at the union step, destroying precision. Confidence-gated merge does not resolve this, as poorly calibrated LLM scores \cite{llm-calibration-survey-2024} discard correct predictions as aggressively as false positives. This is a structural challenge for union-based merge pipelines, independent of decomposition quality, with direct implications for the partitioning approach of \citet{llm-pee-2025}. Future work must address cross-batch calibration before decomposition can translate confusability signals into extraction gains.
7	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 164 · 2026-05-16T02:49:22.316405+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 165 · 2026-05-16T02:49:22.718291+00:00_

1	\section{Discussion}
2	\label{sec:discussion}
3	
4	\paragraph{Boundary conditions.}
5	The two-channel framework applies most cleanly to cross-domain schemas where types span multiple semantic clusters. For same-domain schemas (e.g., MAVEN's FrameNet-derived types), the centrality confound (\S\ref{sec:centrality_confound}) complicates BCS-level analysis, though the pairwise SCS signal remains intact. Practitioners should use BCS as a schema difficulty predictor for cross-domain ontologies, and pairwise SCS directly---or with centrality factored out---for same-domain schemas.
6	
7	\paragraph{The 51\% floor.}
8	High-BCS accuracy converges to $\approx$51\% on FewRel regardless of model size (8B vs.\ 32B), well above random guessing (12.5\% for 8-way classification). This suggests that under high confusability, models can still resolve a ``confusion subgroup'' of easily distinguishable relations but fail on the tightly clustered remainder. The floor's model-invariance indicates a task-inherent difficulty ceiling that scaling alone cannot overcome.
9	
10	\paragraph{Merge amplification and future directions.}
11	Our SDGD experiments show that naive decompose-then-merge pipelines fail because union merge accumulates contradictory predictions across passes. Three directions may address this: (1)~calibration-aware merge, where cross-batch confidence scores are normalized before aggregation; (2)~joint decoding, where the model sees all types but decodes with confusability-aware constraints; and (3)~hierarchical extraction, processing coarse-grained types first and refining within clusters.
12	
13	\paragraph{Schema design implications.}
14	Our results suggest concrete guidelines: monitor BCS when assembling extraction schemas---high-BCS batches are unreliable regardless of model; for large ontologies, prefer cross-domain type groupings that minimize intra-batch similarity; when decomposition is necessary, invest in cross-batch calibration rather than decomposition quality, si
…[truncated 802 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 401
}
```

</details>

---


### Tool call

_source line 166 · 2026-05-16T02:49:22.718693+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 167 · 2026-05-16T02:49:23.121056+00:00_

1	% DEPRECATED — this file is no longer included in main.tex.
2	% The active conclusion is in discussion.tex (\input{discussion}).
3	% Kept for reference only; safe to delete.
4	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 402
}
```

</details>

---


### Tool call

_source line 168 · 2026-05-16T02:49:23.121583+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/references.bib"
  }
}
```

</details>

---


### Tool result

_source line 169 · 2026-05-16T02:49:23.172465+00:00_

1	% References for Schema-DAG-Extraction
2	% Generated: 2026-05-15
3	% Sources: literature_map.yaml + references_survey.md
4	
5	% =============================================================================
6	% DIRECT COMPETITORS
7	% =============================================================================
8	
9	@inproceedings{llm-pee-2025,
10	    title     = {Towards Event Extraction with Massive Types: {LLM}-based Collaborative Annotation and Partitioning Extraction},
11	    author    = {Liu, Wenxuan and Li, Zixuan and Bai, Long and Zuo, Yuxin and Xu, Daozhu and Jin, Xiaolong and Guo, Jiafeng and Cheng, Xueqi},
12	    booktitle = {Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing},
13	    year      = {2025},
14	    url       = {https://aclanthology.org/2025.emnlp-main.1743/},
15	}
16	
17	@article{parse-2025,
18	    title   = {{PARSE}: {LLM} Driven Schema Optimization for Reliable Entity Extraction},
19	    author  = {Shrimal, Anubhav and Jain, Aryan and Chowdhury, Soumyajit and Yenigalla, Promod},
20	    journal = {arXiv preprint arXiv:2510.08623},
21	    year    = {2025},
22	    url     = {https://arxiv.org/abs/2510.08623},
23	}
24	
25	@inproceedings{dee-2024,
26	    title     = {Decompose, Enrich, and Extract! Schema-aware Event Extraction using {LLM}s},
27	    author    = {Shiri, Fatemeh and Nguyen, Van and Moghimifar, Farhad and Yoo, John and Haffari, Gholamreza and Li, Yuan-Fang},
28	    booktitle = {Proceedings of the IEEE International Conference on Tools with Artificial Intelligence},
29	    year      = {2024},
30	    url       = {https://arxiv.org/abs/2406.01045},
31	}
32	
33	@inproceedings{crossagentie-2025,
34	    title     = {{CROSSAGENTIE}: Cross-Type and Cross-Task Multi-Agent {LLM} Collaboration for Zero-Shot Information Extraction},
35	    author    = {Lu, Meng and Xie, Yuzhang and Bi, Zhenyu and Cao, Shuxiang and Wang, Xuan},
36	    booktitle = {Findings of the Association for Computational Linguistics: ACL
…[truncated 18250 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 170 · 2026-05-16T02:49:30.653171+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewerguidelines",
  "prompt": "Extract the full reviewer guidelines including: what reviewers should focus on, how to assess soundness, excitement, and overall scores, any specific guidance on evaluating empirical papers, negative results, statistical rigor, and reproducibility. Also extract any guidance on review structure and what makes a good review."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewerguidelines",
    "prompt": "Extract the full reviewer guidelines including: what reviewers should focus on, how to assess soundness, excitement, and overall scores, any specific guidance on evaluating empirical papers, negative results, statistical rigor, and reproducibility. Also extract any guidance on review structure and what makes a good review."
  }
}
```

</details>

---


### Tool call

_source line 171 · 2026-05-16T02:49:32.209973+00:00_

called mcp__agent-ml-research__verify_references

<details open><summary>🔧 Tool call — mcp__agent-ml-research__verify_references</summary>

```json
{
  "paper_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper",
  "project": "schema-dag-extraction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "mcp__agent-ml-research__verify_references",
  "tool_args": {
    "paper_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper",
    "project": "schema-dag-extraction"
  }
}
```

</details>

---


### Tool result

_source line 172 · 2026-05-16T02:49:38.587227+00:00_

# ARR Reviewer Guidelines: Key Focus Areas

## Core Review Components

Reviewers must provide three scores:
- **Soundness**: "must be justified by the text of the review" (I3)
- **Excitement**: reflects personal interest, separate from technical quality
- **Overall Assessment**: composite recommendation considering soundness, novelty, and impact

## What Reviewers Should Prioritize

**Initial Reading Strategy**
Begin with two-pass reading. First, skim to understand the research question without examining results, avoiding hindsight bias. Then conduct in-depth technical evaluation.

**Specificity Requirements**
Vague critiques like "not clear" should become concrete: "Y and Z are missing from X's description." This enables area chairs to understand issues without reading the full paper.

## Evaluating Empirical Papers

**Reproducibility (M2)**
Assess whether sufficient implementation details, hyperparameter choices, and code/data availability information exist. You're not obligated to run code, but should determine if reproducibility is feasible.

**Statistical Rigor (R5)**
"Main experimental results should be accompanied by appropriate information about their statistical significance (error bars, confidence intervals, statistical significance tests)."

**Analysis Quality (R1)**
Watch for p-hacking, presenting best results from unknown trial counts, and under-tuned baselines. This includes prompt engineering comparisons.

## Handling Negative Results

The guidelines emphasize that negative findings addressing expected outcomes deserve publication. The field benefits from knowing "what systematically does not work" rather than only positive results.

## Common Review Pitfalls to Avoid

**Problematic Heuristics** (H1-H17) include:
- Dismissing results as "obvious in retrospect"
- Criticizing simplicity as insufficient
- Demanding SOTA performance when not claimed
- Requesting experiments beyond what claims require
- Treating acknowledged limitations as rejection reason
…[truncated 510 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 7934
}
```

</details>

---


### Tool result

_source line 173 · 2026-05-16T02:50:07.680177+00:00_

{"result":"{\"success\": true, \"data\": {\"summary\": {\"total_bib_entries\": 40, \"total_citations\": 50, \"unique_cited_keys\": 40, \"orphan_bib\": 0, \"missing_bib\": 0, \"duplicate_keys\": 0, \"online_verified\": 30, \"online_not_found\": 4, \"online_mismatch\": 6}, \"cross_check\": {\"orphan_bib\": [], \"missing_bib\": [], \"orphan_count\": 0, \"missing_count\": 0}, \"bib_entries\": [{\"key\": \"llm-pee-2025\", \"type\": \"inproceedings\", \"title\": \"Towards Event Extraction with Massive Types: LLM-based Collaborative Annotation and Partitioning Extraction\", \"authors\": \"Liu, Wenxuan and Li, Zixuan and Bai, Long and Zuo, Yuxin and Xu, Daozhu and Jin,...\", \"year\": \"2025\", \"venue\": \"Proceedings of the 2025 Conference on Empirical Methods in Natural Language Proc...\"}, {\"key\": \"parse-2025\", \"type\": \"article\", \"title\": \"PARSE: LLM Driven Schema Optimization for Reliable Entity Extraction\", \"authors\": \"Shrimal, Anubhav and Jain, Aryan and Chowdhury, Soumyajit and Yenigalla, Promod\", \"year\": \"2025\", \"venue\": \"arXiv preprint arXiv:2510.08623\"}, {\"key\": \"dee-2024\", \"type\": \"inproceedings\", \"title\": \"Decompose, Enrich, and Extract! Schema-aware Event Extraction using LLMs\", \"authors\": \"Shiri, Fatemeh and Nguyen, Van and Moghimifar, Farhad and Yoo, John and Haffari,...\", \"year\": \"2024\", \"venue\": \"Proceedings of the IEEE International Conference on Tools with Artificial Intell...\"}, {\"key\": \"crossagentie-2025\", \"type\": \"inproceedings\", \"title\": \"CROSSAGENTIE: Cross-Type and Cross-Task Multi-Agent LLM Collaboration for Zero-Shot Information Extraction\", \"authors\": \"Lu, Meng and Xie, Yuzhang and Bi, Zhenyu and Cao, Shuxiang and Wang, Xuan\", \"year\": \"2025\", \"venue\": \"Findings of the Association for Computational Linguistics: ACL 2025\"}, {\"key\": \"dlisc-2025\", \"type\": \"article\", \"title\": \"Effective and Efficient Schema-aware Information Extraction Using On-Device LLMs\", \"authors
…[truncated 31336 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "mcp__agent-ml-research__verify_references",
  "elapsed_ms": 35470
}
```

</details>

---


### Tool call

_source line 174 · 2026-05-16T02:53:47.086179+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 1 — Round 1 完整审稿意见\n\n### 审查侧重：方法严谨性 + 实验设计 + 统计分析\n\n---\n\n## 总体评分\n**Overall**: 3.0/5 (Findings acceptance)\n**一句话总结**: 一篇实验设计用心、负面结果诚实的经验性研究，但核心统计证据不足以支撑\"multi-channel degradation framework\"的声称——该框架仅在 RE 一个任务上 cleanly work，NER 有耦合，ED 有反转，且关键条件存在统计功效不足和 prompt 混淆问题。\n\n## 官方维度打分（来自 ACL ARR review form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 2.5/5 | 核心 claims 有多处统计支撑不足：16-rel 无 CI 的单 batch 比较、80-rel 条件整体回归不显著、非独立 bootstrap、v1/v2 prompt 混淆 |\n| Excitement | 3.0/5 | 问题提得好——首次系统性隔离 count vs confusability，centrality confound 分析有新意，SDGD 负面结果有价值 |\n| Reproducibility | 3.5/5 | 固定种子、greedy decoding、bootstrap 参数均有报告，但 prompt 模板未公开，v1/v2 切换标准不明确 |\n| Overall | 3.0/5 | 贡献真实但被过度包装——\"framework\" 的叙事超出了证据支持的范围，建议重新定位为更谦虚的经验性发现 |\n| Confidence | 4/5 | 仔细阅读了全部实验设计和统计分析，熟悉零样本 IE 和统计方法论 |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [Critical] v1/v2 prompt 切换引入系统性混淆\n- 具体位置：§3.5 (experimental_setup.tex L85)、Appendix Table 1 caption (main.tex L71)、Appendix Table 5 caption (main.tex L146)\n- 问题：v1 prompt（含 offset 要求）用于 count curves 和 BCS-controlled NER 实验；v2 prompt（去 offset + 加 role instruction）用于\"all subsequent experiments\"。v1 的 offset 错误率 96.5%，说明 v1 从根本上改变了模型的输出行为。跨模型表（Table A1）用 v2 评估 Qwen3，但 §5.1 的 count curve 用 v1，Qwen3 在 count=1 时 recall 差 0.08（0.72 v1 vs 0.64 v2）——这不是 minor difference，是 11% 的相对差异。SDGD 实验用 v1 prompt（Table 5 caption），但 SDGD 与 single-pass 的对比基准也是 v1，这部分内部一致——然而读者无法判断 SDGD 在 v2 prompt 下是否有不同结论。论文承认了 prompt sensitivity（引用 Sclar et al.），但没有系统性地报告 v1 vs v2 在所有实验上的 paired comparison。\n- 为什么影响接收：当论文跨实验比较结果时（如 count curve 数字 vs cross-model 数字），prompt 版本不同使得这些比较无效。核心 framework 的两个 channel 分别建立在不同 prompt 版本上。\n- 建议修改方向：(1) 所有主实验统一用一个 prompt 版本运行；或 (2) 对关键实验同时报告两版 prompt 的结果，展示结论对 prompt 选择的鲁棒性。\n\n**N2** [Critical] 16-rel BCS gap (9.1 pp) 基于单个 batch 对比，无统计可靠性\n- 具体位置：Table 3 (results.tex L79)、Table 3 caption\n- 问题：Table 3 明确标注\"The 16-relation condition used a single extreme batch per BCS level; bootstrap CIs require multiple batches\"——即 9.1 pp 这个数字是一个 low-BCS batch vs 一个 high-BCS batch 的比较，无任何 CI。然而论文随后将 9.1 pp 与 31.2 pp (80-rel) 进行对比来论证\"wider BCS range produces larger absolute gaps\"（Abstract, §5.3），这个比较的一端没有统计基础。\n- 为什么影响接收：9.1 vs 31.2 的对比是论文核心叙事（BCS range 解释 absolute gap 差异）的关键证据支柱。若 9.1 pp 不可靠，slope consistency 论证受损。\n- 建议修改方向：对 16-rel 条件补充多 batch 实验，提供 CI。\n\n**N3** [Critical] 80-rel 整体 BCS-accuracy 回归不显著，但论文用 80-rel extreme batches 做 headline result\n- 具体位置：Table 4 (results.tex L108)、Table 3\n- 问题：Table 4 第三行：Full 80-rel (n=25) slope = −0.151, CI [−0.930, +0.657], r = −0.082, p = 0.698。论文承认\"underpowered for both metrics\"。但 Table 3 的 headline result 31.2 pp gap 正是从 80-rel pool 的 extreme batches 得来。在 80-rel pool 中，BCS 与 accuracy 的整体线性关系不显著，但 extreme batches 的差异被呈现为核心发现——这本质上是 cherry-picked endpoints。\n- 为什么影响接收：31.2 pp 出现在 Abstract、Introduction、Discussion、Conclusion 中，是论文最醒目的数字，但来自一个 BCS-accuracy 关系整体不显著的 pool。\n- 建议修改方向：(1) 增加 80-rel batch 数量；(2) 呈现 31.2 pp 时必须紧跟提及整体回归不显著；(3) 考虑以 within-pool 16-sub（slope 显著，p=0.027）作为核心证据。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [Major] \"Multi-channel degradation framework\" 过度声称\n- 具体位置：Introduction Contribution 1、Abstract\n- 问题：框架仅在 RE 上 cleanly work；NER 有 channel 耦合 + non-monotonic count curve + 不显著 factorial test (p=0.50)；ED 完全反转。称之为\"framework\"暗示通用性，但实际证据只支持\"empirical observation primarily demonstrated on RE\"。\n\n**W2** [Major] 非独立观测的 bootstrap CI\n- 具体位置：Table 2 (results.tex L48-57)\n- 问题：Pairwise SCS-confusion 的 1,953/11,026 pairs 不独立（同一 type 出现在多个 pairs），bootstrap percentile CI 会低估真实不确定性，p < 10^{-10} 可能被高估。建议使用 cluster-robust bootstrap（以 type 为 cluster）。\n\n**W3** [Major] NER count curve non-monotonicity 未充分解释\n- 具体位置：§5.1 (results.tex L25)\n- 问题：count=22 (0.527) → count=44 (0.551) 的 recall 上升被称为\"minor non-monotonicity\"，但未报告这两点的 bootstrap CI。若这在 CI 外则说明 count channel 在 NER 上非单调。\n\n**W4** [Major] SDGD 仅在 Few-NERD 上测试\n- 具体位置：§6 (sdgd_negative.tex)\n- 问题：负面结果仅在 NER 上报告。RE 是 channels 最 cleanly separable 的任务，若 SDGD 在 RE 上也失败则大大增强 merge amplification 论点；若在 RE 上成功则改变结论。只在一个任务上就得出\"structural challenge for union-based merge pipelines\"的一般性结论，证据不够。\n\n**W5** [Major] r²=1.3-1.7% 的 practical significance 论证跳跃\n- 具体位置：§5.2 (results.tex L62-64)\n- 问题：从 r²=1.3-1.7% 跳到\"compounds into 31.2 pp\"缺乏形式化。within-pool quartile Δ 仅 −3.92 pp（CI 穿越零）。建议用 typical BCS range × slope 计算 realistic practical effect。\n\n**W6** [Minor] \"model-invariant floor\" 基于仅两个同架构模型\n- 具体位置：§5.3、Discussion\n- 问题：\"model-invariant\" 和 \"scaling alone cannot overcome\" 基于 8B 和 32B 两个 decoder-only 模型，不足以支持这种泛化 claim。\n\n**W7** [Minor] reflect-learn-2026 作者为 \"[To be verified]\"\n**W8** [Minor] FewRel 合并 train/val splits 的 distribution 影响未讨论\n\n---\n\n## 小问题\n- Table 1 BCS Range 用不同 embedding 计算但并列呈现\n- FP8 量化对 extraction 质量的影响未讨论\n- FewRel 理论上可做 2×2 factorial (count=8/16 × BCS high/low)，但论文称\"not conducted\"\n\n---\n\n## 主要优势\n1. 研究问题重要且清晰——首次系统性隔离 count vs confusability\n2. 诚实报告 modest effect sizes 和负面结果\n3. Centrality confound 分析有独立方法论价值\n4. 实验细节充足（种子、decoding、bootstrap 参数）\n5. Within-pool controlled comparison 是精心设计的控制实验\n\n---\n\n## Questions for Authors\n- Q1: 能否提供 v1/v2 prompt 完整文本？\n- Q2: 16-rel 为何仅一个 extreme batch？是 pool 限制还是 budget？\n- Q3: NER count=22→44 的 recall 上升是否在 bootstrap CI 内？\n- Q4: Pairwise bootstrap 是否 accounted for type-level clustering？\n- Q5: 为什么 SDGD 没有在 FewRel 上测试？\n\n---\n\n## Missing References\n- reflect-learn-2026 作者缺失\n- 可考虑补充 schema-guided generation 相关 recent work\n\n---\n\n**评分**: Overall 3.0/5 | Soundness 2.5/5 | Excitement 3.0/5 | Confidence 4/5",
  "reviewer_id": "1",
  "project": "schema-dag-extraction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 1 — Round 1 完整审稿意见\n\n### 审查侧重：方法严谨性 + 实验设计 + 统计分析\n\n---\n\n## 总体评分\n**Overall**: 3.0/5 (Findings acceptance)\n**一句话总结**: 一篇实验设计用心、负面结果诚实的经验性研究，但核心统计证据不足以支撑\"multi-channel degradation framework\"的声称——该框架仅在 RE 一个任务上 cleanly work，NER 有耦合，ED 有反转，且关键条件存在统计功效不足和 prompt 混淆问题。\n\n## 官方维度打分（来自 ACL ARR review form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 2.5/5 | 核心 claims 有多处统计支撑不足：16-rel 无 CI 的单 batch 比较、80-rel 条件整体回归不显著、非独立 bootstrap、v1/v2 prompt 混淆 |\n| Excitement | 3.0/5 | 问题提得好——首次系统性隔离 count vs confusability，centrality confound 分析有新意，SDGD 负面结果有价值 |\n| Reproducibility | 3.5/5 | 固定种子、greedy decoding、bootstrap 参数均有报告，但 prompt 模板未公开，v1/v2 切换标准不明确 |\n| Overall | 3.0/5 | 贡献真实但被过度包装——\"framework\" 的叙事超出了证据支持的范围，建议重新定位为更谦虚的经验性发现 |\n| Confidence | 4/5 | 仔细阅读了全部实验设计和统计分析，熟悉零样本 IE 和统计方法论 |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [Critical] v1/v2 prompt 切换引入系统性混淆\n- 具体位置：§3.5 (experimental_setup.tex L85)、Appendix Table 1 caption (main.tex L71)、Appendix Table 5 caption (main.tex L146)\n- 问题：v1 prompt（含 offset 要求）用于 count curves 和 BCS-controlled NER 实验；v2 prompt（去 offset + 加 role instruction）用于\"all subsequent experiments\"。v1 的 offset 错误率 96.5%，说明 v1 从根本上改变了模型的输出行为。跨模型表（Table A1）用 v2 评估 Qwen3，但 §5.1 的 count curve 用 v1，Qwen3 在 count=1 时 recall 差 0.08（0.72 v1 vs 0.64 v2）——这不是 minor difference，是 11% 的相对差异。SDGD 实验用 v1 prompt（Table 5 caption），但 SDGD 与 single-pass 的对比基准也是 v1，这部分内部一致——然而读者无法判断 SDGD 在 v2 prompt 下是否有不同结论。论文承认了 prompt sensitivity（引用 Sclar et al.），但没有系统性地报告 v1 vs v2 在所有实验上的 paired comparison。\n- 为什么影响接收：当论文跨实验比较结果时（如 count curve 数字 vs cross-model 数字），prompt 版本不同使得这些比较无效。核心 framework 的两个 channel 分别建立在不同 prompt 版本上。\n- 建议修改方向：(1) 所有主实验统一用一个 prompt 版本运行；或 (2) 对关键实验同时报告两版 prompt 的结果，展示结论对 prompt 选择的鲁棒性。\n\n**N2** [Critical] 16-rel BCS gap (9.1 pp) 基于单个 batch 对比，无统计可靠性\n- 具体位置：Table 3 (results.tex L79)、Table 3 caption\n- 问题：Table 3 明确标注\"The 16-relation condition used a single extreme batch per BCS level; bootstrap CIs require multiple batches\"——即 9.1 pp 这个数字是一个 low-BCS batch vs 一个 high-BCS batch 的比较，无任何 CI。然而论文随后将 9.1 pp 与 31.2 pp (80-rel) 进行对比来论证\"wider BCS range produces larger absolute gaps\"（Abstract, §5.3），这个比较的一端没有统计基础。\n- 为什么影响接收：9.1 vs 31.2 的对比是论文核心叙事（BCS range 解释 absolute gap 差异）的关键证据支柱。若 9.1 pp 不可靠，slope consistency 论证受损。\n- 建议修改方向：对 16-rel 条件补充多 batch 实验，提供 CI。\n\n**N3** [Critical] 80-rel 整体 BCS-accuracy 回归不显著，但论文用 80-rel extreme batches 做 headline result\n- 具体位置：Table 4 (results.tex L108)、Table 3\n- 问题：Table 4 第三行：Full 80-rel (n=25) slope = −0.151, CI [−0.930, +0.657], r = −0.082, p = 0.698。论文承认\"underpowered for both metrics\"。但 Table 3 的 headline result 31.2 pp gap 正是从 80-rel pool 的 extreme batches 得来。在 80-rel pool 中，BCS 与 accuracy 的整体线性关系不显著，但 extreme batches 的差异被呈现为核心发现——这本质上是 cherry-picked endpoints。\n- 为什么影响接收：31.2 pp 出现在 Abstract、Introduction、Discussion、Conclusion 中，是论文最醒目的数字，但来自一个 BCS-accuracy 关系整体不显著的 pool。\n- 建议修改方向：(1) 增加 80-rel batch 数量；(2) 呈现 31.2 pp 时必须紧跟提及整体回归不显著；(3) 考虑以 within-pool 16-sub（slope 显著，p=0.027）作为核心证据。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [Major] \"Multi-channel degradation framework\" 过度声称\n- 具体位置：Introduction Contribution 1、Abstract\n- 问题：框架仅在 RE 上 cleanly work；NER 有 channel 耦合 + non-monotonic count curve + 不显著 factorial test (p=0.50)；ED 完全反转。称之为\"framework\"暗示通用性，但实际证据只支持\"empirical observation primarily demonstrated on RE\"。\n\n**W2** [Major] 非独立观测的 bootstrap CI\n- 具体位置：Table 2 (results.tex L48-57)\n- 问题：Pairwise SCS-confusion 的 1,953/11,026 pairs 不独立（同一 type 出现在多个 pairs），bootstrap percentile CI 会低估真实不确定性，p < 10^{-10} 可能被高估。建议使用 cluster-robust bootstrap（以 type 为 cluster）。\n\n**W3** [Major] NER count curve non-monotonicity 未充分解释\n- 具体位置：§5.1 (results.tex L25)\n- 问题：count=22 (0.527) → count=44 (0.551) 的 recall 上升被称为\"minor non-monotonicity\"，但未报告这两点的 bootstrap CI。若这在 CI 外则说明 count channel 在 NER 上非单调。\n\n**W4** [Major] SDGD 仅在 Few-NERD 上测试\n- 具体位置：§6 (sdgd_negative.tex)\n- 问题：负面结果仅在 NER 上报告。RE 是 channels 最 cleanly separable 的任务，若 SDGD 在 RE 上也失败则大大增强 merge amplification 论点；若在 RE 上成功则改变结论。只在一个任务上就得出\"structural challenge for union-based merge pipelines\"的一般性结论，证据不够。\n\n**W5** [Major] r²=1.3-1.7% 的 practical significance 论证跳跃\n- 具体位置：§5.2 (results.tex L62-64)\n- 问题：从 r²=1.3-1.7% 跳到\"compounds into 31.2 pp\"缺乏形式化。within-pool quartile Δ 仅 −3.92 pp（CI 穿越零）。建议用 typical BCS range × slope 计算 realistic practical effect。\n\n**W6** [Minor] \"model-invariant floor\" 基于仅两个同架构模型\n- 具体位置：§5.3、Discussion\n- 问题：\"model-invariant\" 和 \"scaling alone cannot overcome\" 基于 8B 和 32B 两个 decoder-only 模型，不足以支持这种泛化 claim。\n\n**W7** [Minor] reflect-learn-2026 作者为 \"[To be verified]\"\n**W8** [Minor] FewRel 合并 train/val splits 的 distribution 影响未讨论\n\n---\n\n## 小问题\n- Table 1 BCS Range 用不同 embedding 计算但并列呈现\n- FP8 量化对 extraction 质量的影响未讨论\n- FewRel 理论上可做 2×2 factorial (count=8/16 × BCS high/low)，但论文称\"not conducted\"\n\n---\n\n## 主要优势\n1. 研究问题重要且清晰——首次系统性隔离 count vs confusability\n2. 诚实报告 modest effect sizes 和负面结果\n3. Centrality confound 分析有独立方法论价值\n4. 实验细节充足（种子、decoding、bootstrap 参数）\n5. Within-pool controlled comparison 是精心设计的控制实验\n\n---\n\n## Questions for Authors\n- Q1: 能否提供 v1/v2 prompt 完整文本？\n- Q2: 16-rel 为何仅一个 extreme batch？是 pool 限制还是 budget？\n- Q3: NER count=22→44 的 recall 上升是否在 bootstrap CI 内？\n- Q4: Pairwise bootstrap 是否 accounted for type-level clustering？\n- Q5: 为什么 SDGD 没有在 FewRel 上测试？\n\n---\n\n## Missing References\n- reflect-learn-2026 作者缺失\n- 可考虑补充 schema-guided generation 相关 recent work\n\n---\n\n**评分**: Overall 3.0/5 | Soundness 2.5/5 | Excitement 3.0/5 | Confidence 4/5",
    "reviewer_id": "1",
    "project": "schema-dag-extraction"
  }
}
```

</details>

---


### Tool result

_source line 175 · 2026-05-16T02:53:51.323997+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4237
}
```

</details>

---


### Assistant

_source line 176 · 2026-05-16T02:53:56.334580+00:00_

审稿意见已提交给 Review Director。

总结：Overall 3.0/5，三个 Critical 问题——(1) v1/v2 prompt 混淆使跨实验比较失效；(2) 16-rel 的 9.1 pp gap 基于单 batch 无 CI；(3) 80-rel 整体回归不显著却用 extreme batches 做 headline result。四个 Major 问题涉及 "framework" 过度声称、非独立 bootstrap、NER non-monotonicity、SDGD 仅测试一个任务。论文核心贡献有价值但 framing 超出了证据支持的范围，修订后有望达到 Findings 水平。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1"
}
```

</details>

---


## Round 4

## Round 4

4 recorded events


### User

_source line 177 · 2026-05-16T02:54:27.912131+00:00_

[Round 1 审稿请求]:
## 交叉分享 — 请逐条回应 Reviewer 2 的审稿意见

以下是 Reviewer 2 的完整审稿意见。请对每个 Must-Fix 和 Should-Fix 逐条回应：
- **[AGREE]** 同意并说明理由
- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）

---

## Reviewer 2 完整审稿意见

### 审查侧重：新颖性 + 论文完整性 + 写作质量 + 格式合规

**Overall**: 3.0/5 | Soundness 3.5/5 | Excitement 2.5/5 | Reproducibility 2.5/5 | Confidence 4/5

### Must-Fix

**N1** [critical] `reflect-learn-2026` 引用条目不完整
- 位置：references.bib line 329–334；Related Work §2.2
- 问题：作者字段为 `[To be verified]`，无 URL、DOI 或页码。提交带占位符的 bib 条目不可接受。

**N2** [critical] 缺少 Responsible NLP Research Checklist
- 位置：main.tex——Limitations 后直接是 \bibliography，无 checklist
- 问题：ACL ARR 要求所有投稿附带 Responsible NLP Research Checklist。当前版本完全缺失，可能导致 desk reject。

**N3** [critical] 核心效应量过小但 framing 过强
- 位置：Abstract（"first controlled empirical study"）；Introduction Contribution 2；Table 2（r² = 0.013–0.017）
- 问题：pairwise SCS 仅解释 1.3–1.7% 的 type confusion variance。虽然 p < 10^{-10}，但 r² 极小意味着 SCS 几乎不具有个体预测力。BCS-level 实验（31.2 pp gap）显示批次级效应显著，但 pairwise→batch-level 的信号放大机制没有清楚解释。

**N4** [major] 正文仅一幅 Figure
- 位置：Figure 1（§5.1）是正文唯一的 figure。Error taxonomy（Table 7/Figure 2）均在 Appendix。

### Should-Fix

**W1** [major] Prompt template 未公开
**W2** [major] MAVEN 反转对普适性的限制未充分反映在 Abstract
**W3** [major] FewRel 数据构造的外部效度——合并 train+val、closed-set classification vs extraction
**W4** [warning] `json-schema-bench-2025` 引用不完整——author 为 "Li, Saibo and others"
**W5** [warning] MiniLM 引用仍不精确——应额外引用 Reimers & Gurevych (2019) Sentence-BERT
**W6** [warning] 51% floor 的 "confusion subgroup" 解释是推测性的，无实证支撑
**W7** [warning] §6 SDGD 正文仅半页总结，核心数据全在 Appendix

### Questions
Q1: Pairwise r²=1.5% 但 BCS gap=31.2 pp，请解释信号放大机制。
Q2: v1→v2 prompt 导致 precision 翻倍，如何排除 prompt artifact？
Q3: SDGD 为什么不在 FewRel 上测试？
Q4: 加入 type description 计算 SCS 是否提升预测力？
Q5: 是否考虑过 closed-source 模型验证？

### Missing References
1. Reimers & Gurevych (EMNLP 2019) Sentence-BERT
2. Li et al. (2023) "Evaluating ChatGPT's Information Extraction Capabilities"
3. Wadhwa et al. (2023) "Revisiting Relation Extraction in the era of Large Language Models"
4. Hierarchical classification / label confusion 文献（如 AFET, Ren et al. 2016）

---

请逐条回应上述所有 Must-Fix (N1-N4)、Should-Fix (W1-W7)、Questions (Q1-Q5) 和 Missing References。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 178 · 2026-05-16T02:56:27.106361+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 1 交叉回应 Reviewer 2 审稿意见\n\n---\n\n### Must-Fix 逐条回应\n\n**[AGREE] R2-N1: `reflect-learn-2026` 引用不完整**\n同意，我在自己的审稿中也标记了此问题（我的 W7）。作者字段 `[To be verified]` 在 double-blind 提交中不可接受。无论该论文是否真实存在，以此状态提交属于审稿材料质量问题。但我认为这是一个 5 分钟可修复的格式问题，不应上升到影响接收决定的 critical 级别——降为 Should-Fix 更合适。\n\n**[AGREE] R2-N2: 缺少 Responsible NLP Research Checklist**\n同意。ACL ARR 要求所有提交附带 checklist，我在自己的审稿中遗漏了这一点。若确实缺失，这是 desk reject 风险。但需确认：有些提交通过 OpenReview 单独上传 checklist 而非嵌入 main.tex。如果论文确实在任何渠道都没有提交 checklist，则确实是 critical。\n\n**[REBUT] R2-N3: 核心效应量过小但 framing 过强**\n部分不同意 R2 的定性。我在自己的审稿（W5）中也质疑了 r²=1.3-1.7% 到 31.2 pp gap 的跳跃缺乏形式化论证。但 R2 将此列为 critical 且同时给 Soundness 3.5/5，存在内部矛盾——如果效应量问题是 critical 级别，Soundness 不应高于 3.0。\n\n更重要的是，论文在 §5.2 (results.tex L62-64) 中的 framing 实际上相当诚实：明确说 \"modest in magnitude\"，列出了其他可能的 variance sources（frequency、position effects、mention ambiguity 等），并将 SCS 定位为 \"one specific, actionable mechanism\" 而非全部解释。Contribution 2 标题也是 \"statistically significant but modest predictor\"。R2 说 \"framing 过强\" 可能更多是对 Abstract 中 \"first controlled empirical study\" 的措辞反应——但这个措辞描述的是实验设计的原创性，不是效应量大小。\n\n**我与 R2 的实质分歧在于**：真正的问题不是 r² 小本身（小效应量在大样本中统计显著是正常的），而是 pairwise→batch 的信号放大缺乏形式化（我的 W5），以及 31.2 pp 来自整体回归不显著的 80-rel pool 的 extreme batches（我的 N3）。这些是统计方法论问题，不是\"效应量太小\"的问题。\n\n**[REBUT] R2-N4: 正文仅一幅 Figure**\n不同意 critical 级别。正文 Figure 1 包含两个 panel（count curves + BCS scaling），信息密度合理。Error taxonomy 的详细可视化放在 Appendix 是合理的空间分配——8 页正文限制下不可能把所有图都放正文。这更多是呈现偏好问题，不影响技术正确性或接收决定。\n\n我同意增加 1-2 幅正文 figure（如将 error taxonomy 的关键 panel 提入正文、或加一个 MAVEN centrality confound 的 scatter plot）会改善可读性，但这是 Should-Fix (warning) 级别，不是 Must-Fix。\n\n---\n\n### Should-Fix 逐条回应\n\n**[AGREE] R2-W1: Prompt template 未公开**\n强烈同意。我在 Q1 中也提出了同样的问题。v1/v2 prompt 的完整文本对 reproducibility 至关重要——这也是我将 v1/v2 混淆列为 N1 (Critical) 的原因之一。没有 prompt 文本，读者无法判断 v1→v2 的变化是 minor formatting tweak 还是根本性的 task framing 改变。\n\n**[AGREE] R2-W2: MAVEN 反转未在 Abstract 充分体现**\n强烈同意，与我的 W1 一致。Abstract 说 \"two degradation channels...across three IE tasks\" 但实际上 MAVEN/ED 完全不符合这个叙事。Abstract 应当明确指出 ED 的反转趋势和 centrality confound，而非给读者一种\"三个任务都支持 framework\"的印象。\n\n**[AGREE] R2-W3: FewRel 数据构造的外部效度**\n同意，且我想补充一个 R2 隐含但未充分展开的重要观点：FewRel 的 RE 任务是 **closed-set classification**（给定 head/tail entities，选择 relation label），而非 **open extraction**（从文本中同时识别 entities 和 relations）。论文声称 \"channels are cleanly separable in RE\"（§5.5, results.tex L131）——但这个 \"clean separation\" 可能是 **任务形式的产物而非降解机制的真实属性**。Classification 任务中不存在 \"entity detection\" 环节，所以 Channel 2 自然不会影响 detection（missed rate flat at 10-16%）。将此解读为 \"RE 上 channels cleanly separate\" 是循环论证——classification 本身就消除了 detection 维度。\n\n这一点削弱了论文最强的 claim 之一。如果 \"clean separation\" 只是因为 RE 没有 detection component，那它不能作为 framework 普适性的证据。\n\n**[AGREE] R2-W4: `json-schema-bench-2025` 引用不完整**\n同意但 severity 低。`and others` 在 bib 中不规范，应列出至少前三位作者。\n\n**[AGREE] R2-W5: MiniLM 引用应补充 Sentence-BERT**\n同意。论文使用的 `all-MiniLM-L6-v2` 是 Sentence-Transformers 框架下的模型，其训练方法论来自 Reimers & Gurevych (2019)。仅引用 MiniLM 原始论文（关于 knowledge distillation）不足以准确归因。\n\n**[AGREE] R2-W6: 51% floor 的 \"confusion subgroup\" 解释是推测**\n同意，与我的 W6 一致。论文在 Discussion (discussion.tex L8) 中提出 \"models can still resolve a confusion subgroup of easily distinguishable relations\"，但未提供任何实证支持（如：哪些 relations 被正确分类？是否存在可识别的 easy cluster？）。这是 post-hoc speculation，应标注为 hypothesis 而非 finding。\n\n**[AGREE] R2-W7: §6 SDGD 正文过短**\n部分同意。SDGD 被列为四个 contributions 之一（Introduction Contribution 4），但正文仅半页（sdgd_negative.tex 共 6 行文字），核心数据（Table 5, 完整 protocol）全在 Appendix。对于 claimed contribution，这不够。但我认为更根本的问题不是篇幅而是 **scope**——SDGD 仅在 Few-NERD 一个任务上测试（我的 W4），这比篇幅短更影响 claim 的可信度。\n\n---\n\n### Questions 逐条回应\n\n**[AGREE] R2-Q1: Pairwise r²=1.5% 但 BCS gap=31.2 pp 的信号放大机制**\n与我的 W5 完全一致。这是论文需要回答的核心问题。我补充：即使放大机制存在，31.2 pp 来自 extreme batches——within-pool 的 quartile Δ 仅 −3.92 pp（CI 穿越零，Table 4）。论文需要区分 \"theoretical maximum amplification\"（extreme batches）和 \"typical amplification\"（representative batches），并只用后者做 practical significance 论证。\n\n**[AGREE] R2-Q2: v1→v2 prompt artifact**\n与我的 N1 完全一致。v1→v2 使 precision 翻倍（SDGD 表格中 single_pass v1 P=0.563 vs v2 experiments showing much higher precision patterns），这说明 prompt 设计对提取行为有巨大影响。论文必须展示核心结论（两通道分离、BCS-accuracy 关系）在两个 prompt 版本下都成立，否则无法排除 prompt artifact。\n\n**[AGREE] R2-Q3: SDGD 不在 FewRel 上测试**\n与我的 W4 完全一致。RE 是 channels 最 cleanly separable 的任务——如果 confusability-aware decomposition 在最有利的条件下都不 work，这才是 \"structural challenge\" 的强证据。仅在 NER（channels 耦合的任务）上测试，无法区分 merge amplification 本身的问题和 NER-specific 的 detection coupling 问题。\n\n**[REBUT] R2-Q4: 加入 type description 计算 SCS 是否提升预测力**\n这是一个合理的 future work 建议，但我不认为它是当前论文的弱点。论文在 §3.2 (experimental_setup.tex L52) 明确说明 \"Both use type name strings only, without definitions or descriptions, to reflect the information available to the model at inference time\"——在 zero-shot 设置下，prompt 中只有 type names（至少在本文的实验设计中如此）。使用 name-only embedding 与实验设置一致。当然，如果未来工作的 prompt 包含 type definitions，SCS 应相应扩展。但要求当前论文测试一个超出其实验设置的 metric variant 不太公平。\n\n**[REBUT] R2-Q5: Closed-source 模型验证**\n合理建议但不是必要的。论文已在两个开源模型（Qwen3-32B, Llama-3.1-8B）上验证，涵盖不同模型家族和规模。Closed-source 模型（GPT-4, Claude）的 API 不支持 hidden-state extraction（用于 Qwen3 embedding 的 SCS），且 API 行为可能受 system prompt、safety filters 等影响，引入额外混淆。开源模型的 reproducibility 优势在本文的经验性研究中更重要。\n\n---\n\n### Missing References 回应\n\n1. **Reimers & Gurevych (2019) Sentence-BERT** — [AGREE] 应补充，理由见 W5。\n2. **Li et al. (2023) \"Evaluating ChatGPT's IE Capabilities\"** — [AGREE] 相关性较高，属于 zero-shot IE evaluation 文献，应至少在 §2.1 提及。\n3. **Wadhwa et al. (2023) RE in era of LLMs** — [AGREE] 与论文的 RE 实验直接相关。\n4. **AFET / hierarchical label confusion 文献** — [REBUT] 相关性有限。AFET (Ren et al., 2016) 关注的是 hierarchical fine-grained typing with noise，其 label confusion 概念与本文的 embedding-based confusability 在技术层面差异较大。可以在 related work 中一句话提及，但不是 missing 到影响论文完整性的程度。\n\n---\n\n### 总结：与 R2 的主要分歧\n\n1. **R2 给 Soundness 3.5，我给 2.5** — 我认为 R2 低估了统计方法论问题的严重性（16-rel 无 CI、80-rel 回归不显著、非独立 bootstrap），这些直接影响核心 claims 的可信度。\n2. **R2 将 N4 (仅一幅图) 列为 critical** — 我认为这是 presentation preference，不是 soundness 或 acceptance 决定问题。\n3. **R2-W3 的 FewRel 外部效度** — 我提出了一个 R2 没有明确说的更深层问题：RE-as-classification 本身消除了 detection 维度，使 \"clean channel separation\" 成为任务设计的 artifact 而非 framework 的验证。\n4. **R2-Q4 和 Q5** — 我认为这些是合理的 future work 方向但不是当前论文的缺陷。",
  "reviewer_id": "1",
  "project": "schema-dag-extraction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 1 交叉回应 Reviewer 2 审稿意见\n\n---\n\n### Must-Fix 逐条回应\n\n**[AGREE] R2-N1: `reflect-learn-2026` 引用不完整**\n同意，我在自己的审稿中也标记了此问题（我的 W7）。作者字段 `[To be verified]` 在 double-blind 提交中不可接受。无论该论文是否真实存在，以此状态提交属于审稿材料质量问题。但我认为这是一个 5 分钟可修复的格式问题，不应上升到影响接收决定的 critical 级别——降为 Should-Fix 更合适。\n\n**[AGREE] R2-N2: 缺少 Responsible NLP Research Checklist**\n同意。ACL ARR 要求所有提交附带 checklist，我在自己的审稿中遗漏了这一点。若确实缺失，这是 desk reject 风险。但需确认：有些提交通过 OpenReview 单独上传 checklist 而非嵌入 main.tex。如果论文确实在任何渠道都没有提交 checklist，则确实是 critical。\n\n**[REBUT] R2-N3: 核心效应量过小但 framing 过强**\n部分不同意 R2 的定性。我在自己的审稿（W5）中也质疑了 r²=1.3-1.7% 到 31.2 pp gap 的跳跃缺乏形式化论证。但 R2 将此列为 critical 且同时给 Soundness 3.5/5，存在内部矛盾——如果效应量问题是 critical 级别，Soundness 不应高于 3.0。\n\n更重要的是，论文在 §5.2 (results.tex L62-64) 中的 framing 实际上相当诚实：明确说 \"modest in magnitude\"，列出了其他可能的 variance sources（frequency、position effects、mention ambiguity 等），并将 SCS 定位为 \"one specific, actionable mechanism\" 而非全部解释。Contribution 2 标题也是 \"statistically significant but modest predictor\"。R2 说 \"framing 过强\" 可能更多是对 Abstract 中 \"first controlled empirical study\" 的措辞反应——但这个措辞描述的是实验设计的原创性，不是效应量大小。\n\n**我与 R2 的实质分歧在于**：真正的问题不是 r² 小本身（小效应量在大样本中统计显著是正常的），而是 pairwise→batch 的信号放大缺乏形式化（我的 W5），以及 31.2 pp 来自整体回归不显著的 80-rel pool 的 extreme batches（我的 N3）。这些是统计方法论问题，不是\"效应量太小\"的问题。\n\n**[REBUT] R2-N4: 正文仅一幅 Figure**\n不同意 critical 级别。正文 Figure 1 包含两个 panel（count curves + BCS scaling），信息密度合理。Error taxonomy 的详细可视化放在 Appendix 是合理的空间分配——8 页正文限制下不可能把所有图都放正文。这更多是呈现偏好问题，不影响技术正确性或接收决定。\n\n我同意增加 1-2 幅正文 figure（如将 error taxonomy 的关键 panel 提入正文、或加一个 MAVEN centrality confound 的 scatter plot）会改善可读性，但这是 Should-Fix (warning) 级别，不是 Must-Fix。\n\n---\n\n### Should-Fix 逐条回应\n\n**[AGREE] R2-W1: Prompt template 未公开**\n强烈同意。我在 Q1 中也提出了同样的问题。v1/v2 prompt 的完整文本对 reproducibility 至关重要——这也是我将 v1/v2 混淆列为 N1 (Critical) 的原因之一。没有 prompt 文本，读者无法判断 v1→v2 的变化是 minor formatting tweak 还是根本性的 task framing 改变。\n\n**[AGREE] R2-W2: MAVEN 反转未在 Abstract 充分体现**\n强烈同意，与我的 W1 一致。Abstract 说 \"two degradation channels...across three IE tasks\" 但实际上 MAVEN/ED 完全不符合这个叙事。Abstract 应当明确指出 ED 的反转趋势和 centrality confound，而非给读者一种\"三个任务都支持 framework\"的印象。\n\n**[AGREE] R2-W3: FewRel 数据构造的外部效度**\n同意，且我想补充一个 R2 隐含但未充分展开的重要观点：FewRel 的 RE 任务是 **closed-set classification**（给定 head/tail entities，选择 relation label），而非 **open extraction**（从文本中同时识别 entities 和 relations）。论文声称 \"channels are cleanly separable in RE\"（§5.5, results.tex L131）——但这个 \"clean separation\" 可能是 **任务形式的产物而非降解机制的真实属性**。Classification 任务中不存在 \"entity detection\" 环节，所以 Channel 2 自然不会影响 detection（missed rate flat at 10-16%）。将此解读为 \"RE 上 channels cleanly separate\" 是循环论证——classification 本身就消除了 detection 维度。\n\n这一点削弱了论文最强的 claim 之一。如果 \"clean separation\" 只是因为 RE 没有 detection component，那它不能作为 framework 普适性的证据。\n\n**[AGREE] R2-W4: `json-schema-bench-2025` 引用不完整**\n同意但 severity 低。`and others` 在 bib 中不规范，应列出至少前三位作者。\n\n**[AGREE] R2-W5: MiniLM 引用应补充 Sentence-BERT**\n同意。论文使用的 `all-MiniLM-L6-v2` 是 Sentence-Transformers 框架下的模型，其训练方法论来自 Reimers & Gurevych (2019)。仅引用 MiniLM 原始论文（关于 knowledge distillation）不足以准确归因。\n\n**[AGREE] R2-W6: 51% floor 的 \"confusion subgroup\" 解释是推测**\n同意，与我的 W6 一致。论文在 Discussion (discussion.tex L8) 中提出 \"models can still resolve a confusion subgroup of easily distinguishable relations\"，但未提供任何实证支持（如：哪些 relations 被正确分类？是否存在可识别的 easy cluster？）。这是 post-hoc speculation，应标注为 hypothesis 而非 finding。\n\n**[AGREE] R2-W7: §6 SDGD 正文过短**\n部分同意。SDGD 被列为四个 contributions 之一（Introduction Contribution 4），但正文仅半页（sdgd_negative.tex 共 6 行文字），核心数据（Table 5, 完整 protocol）全在 Appendix。对于 claimed contribution，这不够。但我认为更根本的问题不是篇幅而是 **scope**——SDGD 仅在 Few-NERD 一个任务上测试（我的 W4），这比篇幅短更影响 claim 的可信度。\n\n---\n\n### Questions 逐条回应\n\n**[AGREE] R2-Q1: Pairwise r²=1.5% 但 BCS gap=31.2 pp 的信号放大机制**\n与我的 W5 完全一致。这是论文需要回答的核心问题。我补充：即使放大机制存在，31.2 pp 来自 extreme batches——within-pool 的 quartile Δ 仅 −3.92 pp（CI 穿越零，Table 4）。论文需要区分 \"theoretical maximum amplification\"（extreme batches）和 \"typical amplification\"（representative batches），并只用后者做 practical significance 论证。\n\n**[AGREE] R2-Q2: v1→v2 prompt artifact**\n与我的 N1 完全一致。v1→v2 使 precision 翻倍（SDGD 表格中 single_pass v1 P=0.563 vs v2 experiments showing much higher precision patterns），这说明 prompt 设计对提取行为有巨大影响。论文必须展示核心结论（两通道分离、BCS-accuracy 关系）在两个 prompt 版本下都成立，否则无法排除 prompt artifact。\n\n**[AGREE] R2-Q3: SDGD 不在 FewRel 上测试**\n与我的 W4 完全一致。RE 是 channels 最 cleanly separable 的任务——如果 confusability-aware decomposition 在最有利的条件下都不 work，这才是 \"structural challenge\" 的强证据。仅在 NER（channels 耦合的任务）上测试，无法区分 merge amplification 本身的问题和 NER-specific 的 detection coupling 问题。\n\n**[REBUT] R2-Q4: 加入 type description 计算 SCS 是否提升预测力**\n这是一个合理的 future work 建议，但我不认为它是当前论文的弱点。论文在 §3.2 (experimental_setup.tex L52) 明确说明 \"Both use type name strings only, without definitions or descriptions, to reflect the information available to the model at inference time\"——在 zero-shot 设置下，prompt 中只有 type names（至少在本文的实验设计中如此）。使用 name-only embedding 与实验设置一致。当然，如果未来工作的 prompt 包含 type definitions，SCS 应相应扩展。但要求当前论文测试一个超出其实验设置的 metric variant 不太公平。\n\n**[REBUT] R2-Q5: Closed-source 模型验证**\n合理建议但不是必要的。论文已在两个开源模型（Qwen3-32B, Llama-3.1-8B）上验证，涵盖不同模型家族和规模。Closed-source 模型（GPT-4, Claude）的 API 不支持 hidden-state extraction（用于 Qwen3 embedding 的 SCS），且 API 行为可能受 system prompt、safety filters 等影响，引入额外混淆。开源模型的 reproducibility 优势在本文的经验性研究中更重要。\n\n---\n\n### Missing References 回应\n\n1. **Reimers & Gurevych (2019) Sentence-BERT** — [AGREE] 应补充，理由见 W5。\n2. **Li et al. (2023) \"Evaluating ChatGPT's IE Capabilities\"** — [AGREE] 相关性较高，属于 zero-shot IE evaluation 文献，应至少在 §2.1 提及。\n3. **Wadhwa et al. (2023) RE in era of LLMs** — [AGREE] 与论文的 RE 实验直接相关。\n4. **AFET / hierarchical label confusion 文献** — [REBUT] 相关性有限。AFET (Ren et al., 2016) 关注的是 hierarchical fine-grained typing with noise，其 label confusion 概念与本文的 embedding-based confusability 在技术层面差异较大。可以在 related work 中一句话提及，但不是 missing 到影响论文完整性的程度。\n\n---\n\n### 总结：与 R2 的主要分歧\n\n1. **R2 给 Soundness 3.5，我给 2.5** — 我认为 R2 低估了统计方法论问题的严重性（16-rel 无 CI、80-rel 回归不显著、非独立 bootstrap），这些直接影响核心 claims 的可信度。\n2. **R2 将 N4 (仅一幅图) 列为 critical** — 我认为这是 presentation preference，不是 soundness 或 acceptance 决定问题。\n3. **R2-W3 的 FewRel 外部效度** — 我提出了一个 R2 没有明确说的更深层问题：RE-as-classification 本身消除了 detection 维度，使 \"clean channel separation\" 成为任务设计的 artifact 而非 framework 的验证。\n4. **R2-Q4 和 Q5** — 我认为这些是合理的 future work 方向但不是当前论文的缺陷。",
    "reviewer_id": "1",
    "project": "schema-dag-extraction"
  }
}
```

</details>

---


### Tool result

_source line 179 · 2026-05-16T02:56:32.129048+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 5022
}
```

</details>

---


### Assistant

_source line 180 · 2026-05-16T02:56:39.221188+00:00_

交叉回应已提交给 Review Director。

主要立场：
- 与 R2 在 7/11 个 Should-Fix + Must-Fix 上 AGREE，但对 N3 的 severity 定性和 N4 的 critical 级别持异议
- 对 R2-W3 (FewRel) 补充了更深层的论点：RE-as-classification 本身消除了 detection 维度，使 "clean channel separation" 可能是任务设计的 artifact
- 与 R2 最大的分歧在 Soundness 评分（我 2.5 vs R2 3.5）——我认为统计方法论问题（无 CI 的单 batch、不显著的 80-rel 回归、非独立 bootstrap）比 R2 认为的更严重

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1"
}
```

</details>

---


## Round 5

## Round 5

42 recorded events


### User

_source line 181 · 2026-05-16T04:35:40.108037+00:00_

[Round 3 审稿请求]:
## Round 3 审稿任务 — Reviewer 1

**侧重**: 方法严谨性 + 实验设计 + 统计分析

### Venue 信息
- **目标**: EMNLP 2026 Main Conference (ARR May 2026 cycle)
- **Deadline**: 2026-05-25
- **格式**: ACL template `[review]`, Long paper 8页正文 + unlimited references + appendix
- **匿名**: Double-blind
- **必须项**: Limitations section + Responsible NLP Research Checklist

### 论文路径
`projects/schema-dag-extraction/docs/paper/main.tex`
（含多个 \input 文件：abstract.tex, introduction.tex, related_work.tex, experimental_setup.tex, results.tex, sdgd_negative.tex, discussion.tex, checklist.tex, prompt_appendix.tex）

### 你的审查重点

1. **统计方法论**：
   - 所有 bootstrap CI 是否使用了正确的 resampling 单元（特别是 pairwise SCS 的 type-level cluster bootstrap）
   - 16-rel BCS gap 是否已降级为 illustrative 或补充了多 batch CI
   - 80-rel BCS-accuracy 回归不显著问题是否在引用 31.2pp 时有适当注明
   - NER count=22→44 recall 上升是否报了 CI
   - r²=1.3-1.7% → batch-level 31.2pp 的信号放大是否有形式化论证（§practical_magnitude）

2. **实验设计**：
   - v1/v2 prompt 问题是否已解决（Round 2 要求：公开 prompt template + 报告 v2 实验结果）
   - 检查 prompt_appendix.tex 是否包含完整 prompt template
   - Cross-model validation 是否充分
   - SDGD 仅在 NER 测试的局限性是否在 Limitations 中明确标注

3. **因果推断**：
   - "Type confusability drives degradation" 的因果语言是否与 observational 证据匹配
   - RE clean channel separation 是否讨论了 classification artifact 可能

### Round 2 未解决问题（需验证）

**Open issues:**
- `R2-W4-sdgd-scope` (warning): SDGD 仅在 Few-NERD (NER) 测试 → Limitations 是否已限定
- `MW4` (warning, in_progress): 正文仅一幅 Figure → 是否有改善

**Round 2 Critical issues 标记为 resolved，请验证修复质量:**
- `MW1`: Abstract 中 9.1pp 是否替换为 bootstrapped Δ=-7.42pp CI[-9.40,-5.54]；Table 3 caption 是否标注为 illustrative
- `MW2`: §practical_magnitude 是否充分论证了 realistic effect size
- `SW3`: v1/v2 prompt 混淆是否解决——prompt_appendix.tex 是否存在且完整；每个实验的 prompt 版本是否在正文标注
- `R2-N3-80rel`: 31.2pp 出现时是否注明 full 80-rel 条件不显著
- `m3`: Responsible NLP Checklist (checklist.tex) 是否完整且格式正确
- `REF1`: reflect-learn-2026 引用是否已修正为真实作者

### 输出格式

请按以下结构输出审稿意见：
1. Summary (2-3句)
2. Strengths (逐条 S1, S2, ...)
3. Weaknesses (逐条 W1, W2, ... 标注 severity: critical/major/minor)
4. Questions for Authors (逐条 Q1, Q2, ...)
5. Missing References
6. Round 2 Issue Resolution Verification (逐条确认每个 resolved issue 的修复质量: PASS/PARTIAL/FAIL)
7. Overall Score (1-5) 和 Confidence (1-5)
8. Soundness Score (1-5)
9. Excitement Score (1-5)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 182 · 2026-05-16T04:35:50.295000+00:00_

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
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
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

_source line 183 · 2026-05-16T04:35:50.346041+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 184 · 2026-05-16T04:35:54.242041+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL ARR 2026 reviewer guidelines review form criteria scoring"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR 2026 reviewer guidelines review form criteria scoring"
  }
}
```

</details>

---


### Tool call

_source line 185 · 2026-05-16T04:35:54.747015+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "projects/schema-dag-extraction/docs/paper/*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Glob",
  "tool_args": {
    "pattern": "projects/schema-dag-extraction/docs/paper/*.tex"
  }
}
```

</details>

---


### Tool call

_source line 186 · 2026-05-16T04:35:54.797674+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "projects/schema-dag-extraction/docs/paper/*.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Glob",
  "tool_args": {
    "pattern": "projects/schema-dag-extraction/docs/paper/*.bib"
  }
}
```

</details>

---


### Tool result

_source line 187 · 2026-05-16T04:35:54.849986+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Glob",
  "elapsed_ms": 102
}
```

</details>

---


### Tool result

_source line 188 · 2026-05-16T04:35:54.850366+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Glob",
  "elapsed_ms": 52
}
```

</details>

---


### Tool result

_source line 189 · 2026-05-16T04:36:02.775159+00:00_

Web search results for query: "ACL ARR 2026 reviewer guidelines review form criteria scoring"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"aclrollingreview/reviewing.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/reviewing.md"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"}]

Based on the search results, here's comprehensive information about ACL ARR 2026 reviewer guidelines, review form criteria, and scoring:

## Reviewer Scoring System

Starting with February 2025, ARR reviewers are asked to provide three scores: s
…[truncated 1729 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 8533
}
```

</details>

---


### Tool call

_source line 190 · 2026-05-16T04:36:07.854887+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete ARR review form: all scoring dimensions, their scales (1-5 descriptions for each level), and all free-text fields. I need the exact scoring rubric for soundness, excitement, and overall recommendation."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the complete ARR review form: all scoring dimensions, their scales (1-5 descriptions for each level), and all free-text fields. I need the exact scoring rubric for soundness, excitement, and overall recommendation."
  }
}
```

</details>

---


### Tool call

_source line 191 · 2026-05-16T04:36:09.010235+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/main.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/main.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction"
  }
}
```

</details>

---


### Tool result

_source line 192 · 2026-05-16T04:36:09.061039+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 193 · 2026-05-16T04:36:16.453445+00:00_

# ACL Rolling Review Form - Complete Scoring Rubric

## Scoring Dimensions

### 1. Reviewer Confidence
Scale: 1-5
- **5**: "Positive that my evaluation is correct. I read the paper very carefully and am familiar with related work."
- **4**: "Quite sure. I tried to check the important points carefully."
- **3**: "Pretty sure, but there's a chance I missed something."
- **2**: "Willing to defend my evaluation, but it is fairly likely that I missed some details."
- **1**: "Not my area, or paper is very hard to understand."

### 2. Soundness
Scale: 1-5 (with half-point options)
- **5**: "Excellent: This study is one of the most thorough I have seen, given its type."
- **4**: "Strong: This study provides sufficient support for all of its claims."
- **3**: "Acceptable: This study provides sufficient support for its main claims."
- **2**: "Poor: Some of the main claims are not sufficiently supported."
- **1**: "Major Issues: This study is not yet sufficiently thorough to warrant publication."

### 3. Excitement
Scale: 1-5 (with half-point options)
- **5**: "Highly Exciting: I would recommend this paper to others and/or attend its presentation."
- **4**: "Exciting: I would mention this paper to others and/or make an effort to attend."
- **3**: "Interesting: I might mention some points of this paper to others."
- **2**: "Potentially Interesting: this paper does not resonate with me, but it might with others."
- **1**: "Not Exciting: this paper does not resonate with me, and I don't think it would with others."

### 4. Overall Assessment
Scale: 1-5 (with half-point options)
- **5**: "Consider for Award: Could be considered for an outstanding paper award (top 2.5%)."
- **4.5**: "Borderline Award"
- **4**: "Conference: Could be accepted to an *ACL conference."
- **3.5**: "Borderline Conference"
- **3**: "Findings: Could be accepted to the Findings of the ACL."
- **2.5**: "Borderline Findings"
- **2**: "Resubmit next cycle: Needs substantial revisions completable by next ARR cyc
…[truncated 668 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 8598
}
```

</details>

---


### Tool call

_source line 194 · 2026-05-16T04:36:20.174559+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 195 · 2026-05-16T04:36:20.225530+00:00_

1	\documentclass[11pt]{article}
2	
3	\usepackage[review]{acl}
4	
5	\usepackage{times}
6	\usepackage{latexsym}
7	\usepackage[T1]{fontenc}
8	\usepackage[utf8]{inputenc}
9	\usepackage{microtype}
10	\usepackage{graphicx}
11	\usepackage{booktabs}
12	\usepackage{amsmath}
13	\usepackage{enumitem}
14	\usepackage[normalem]{ulem}
15	
16	\title{Does Type Confusability Drive Schema-Induced Degradation\\in Training-Free LLM Information Extraction?}
17	
18	\author{Anonymous}
19	
20	\begin{document}
21	\maketitle
22	
23	\input{abstract}
24	
25	\input{introduction}
26	
27	\input{related_work}
28	
29	\input{experimental_setup}
30	
31	\input{results}
32	
33	\input{sdgd_negative}
34	
35	\input{discussion}
36	
37	\section*{Limitations}
38	\begin{enumerate}[leftmargin=*,itemsep=2pt]
39	\item \textbf{Single primary model.} The primary experiments use Qwen3-32B. Channel~1 has been validated on Llama-3.1-8B-Instruct (recall decline $-$43\,pp, $r = 0.725$). Channel~2 was validated on FewRel RE ($\Delta = -27.1$\,pp at count 8, $-23.9$\,pp at count 16), with high-BCS accuracy converging to a floor consistent across both tested models ($\approx$0.51). On Few-NERD NER, Channel~2 was not robustly detectable at 8B scale, likely due to floor effects and the noisier text-match metric.
40	
41	\item \textbf{Modest pairwise effect size.} Pairwise SCS explains 1.3--1.7\% of the variance in type confusion. Entity frequency, prompt position effects, mention ambiguity, context complexity, and type definition quality likely account for the remaining variance.
42	
43	\item \textbf{Cross-pool slope consistency.} The BCS--accuracy slopes are statistically indistinguishable across pools (permutation $p = 0.436$), indicating consistent per-unit sensitivity. The 80-relation extreme-batch gap (31.2\,pp) reflects the wider BCS range in that pool, not a stronger underlying effect; the independent 16-relation pool yields a bootstrapped quartile $\Delta$ of $-$7.4\,pp (95\% CI: [$-$9.4, $-$5.5]). A within-pool compa
…[truncated 15655 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 196 · 2026-05-16T04:36:24.817636+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 197 · 2026-05-16T04:36:25.319254+00:00_

1	\begin{abstract}
2	Training-free LLM information extraction---prompting models with target schemas without fine-tuning---degrades sharply as schema complexity grows: NER recall drops from 0.72 to 0.42 with 64 candidate types, and RE accuracy falls from 85.7\% to 50.4\% with 80 relations. Prior work conflates type count with type confusability, leaving the mechanisms unclear. We conduct the first controlled empirical study isolating these factors across three IE tasks and three datasets, introducing the Schema Confusability Score (SCS) and two experimental paradigms: count curves that vary schema size while randomizing confusability, and BCS-controlled experiments that fix size while varying confusability. Our experiments reveal two degradation channels: a count channel that generally suppresses recall as candidate types increase, and a confusability channel where semantically similar types trigger intra-batch substitution errors---cleanly separable in RE; in NER, confusability additionally impairs entity detection. The BCS--accuracy relationship is robust across schema sizes: the regression slope is consistent between independent 16-type and within-pool 80-type evaluations (permutation $p = 0.44$), with the quartile gap reaching $-$7.4\,pp (95\% CI: [$-$9.4, $-$5.5]) on the independent 16-relation pool. On MAVEN's same-domain schema (168 event types), per-type confusability reverses direction due to a centrality confound, though pairwise confusability remains significant. Both channels replicate on Llama-3.1-8B (count $r = 0.725$; confusability $\Delta = -27$\,pp), with high-BCS accuracy converging to a floor consistent across both tested models. Our confusability-aware decomposition yields an informative negative result: merge amplification destroys precision across all strategies, identifying a structural challenge for union-based merge pipelines in zero-shot IE.
3	\end{abstract}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 501
}
```

</details>

---


### Tool call

_source line 198 · 2026-05-16T04:36:25.319717+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 199 · 2026-05-16T04:36:25.772079+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	Training-free LLM information extraction---prompting a large language model with a target schema and asking it to extract structured information without any task-specific fine-tuning---enables rapid deployment across new domains and ontologies. This zero-shot paradigm eliminates the need for labeled data, making it attractive for applications where annotation is expensive or schemas evolve frequently \cite{llm4ie-survey-2024}. Yet the paradigm carries a critical limitation: performance degrades sharply as the number of candidate types in the prompt schema grows. On named entity recognition, recall drops from 0.72 with a single candidate type to 0.42 with 64 types, a 42\% relative decline. On relation extraction, accuracy falls from 85.7\% with one relation to 50.4\% with 80 relations---near halving. This degradation is not academic: real-world ontologies routinely define 50--200+ types, placing them squarely in the regime where training-free extraction becomes unreliable.
5	
6	What causes this schema-induced degradation? Prior work has proposed decomposition strategies that implicitly assume different answers. \citet{uniner-2024} extract each type independently, assuming types can be treated as separable. \citet{llm-pee-2025} partition large event schemas by type embedding similarity before extraction, assuming that semantic overlap between co-presented types drives errors. \citet{parse-2025} rewrite and optimize schema definitions, assuming that description quality is the bottleneck. Each approach improves extraction under certain conditions, but none isolates \emph{why} schemas degrade performance in the first place. The closest work, LLM-PEE \cite{llm-pee-2025}, reduces both the number of co-presented types and their inter-type similarity simultaneously, making it impossible to determine which factor---or what combination---accounts for the observed gains. More broadly, all prior approaches conflate two dis
…[truncated 3728 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 200 · 2026-05-16T04:36:25.772556+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 201 · 2026-05-16T04:36:26.224431+00:00_

1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\subsection{Training-Free LLM Information Extraction}
5	\label{sec:rw_training_free}
6	
7	Training-free LLM IE spans instruction tuning \cite{instructuie-2023}, code-style schema encoding \cite{knowcoder-2024,codeie-2023}, annotation-guided extraction \cite{gollie-2024,adelie-2024}, schema-driven decoding \cite{slot-2025,oneke-2025}, and constrained JSON decoding \cite{json-schema-bench-2025}. Early evaluations of ChatGPT's extraction capabilities \cite{chatgpt-ie-eval-2023} and relation extraction under LLMs \cite{wadhwa-re-llm-2023} establish baselines for training-free IE. For NER, approaches include zero-shot decomposition \cite{xie-zeroshot-ner-2023,promptner-2023}, distillation \cite{uniner-2024}, bidirectional encoders \cite{gliner-2024,gliner2-2025}, and guided synthesis \cite{guidex-2025,nuner-2024}; \citet{familiarity-2025} quantify label shifts in zero-shot NER evaluation. These methods perform well with moderate schemas (4--20 types) but none investigates how performance degrades as schema complexity scales, nor proposes quantitative metrics for inter-type confusability.
8	
9	\subsection{Schema Complexity in IE}
10	\label{sec:rw_schema}
11	
12	The most directly related work is LLM-PEE \cite{llm-pee-2025}, which addresses event extraction with massive type inventories by partitioning schemas based on type embedding similarity. LLM-PEE clusters event types and assigns each cluster to a separate extraction prompt, demonstrating improved performance on schemas with hundreds of types. Our work is complementary in three respects. First, whereas LLM-PEE develops an engineering solution---partition to improve extraction---we conduct controlled empirical analysis to understand \emph{why} extraction degrades. Second, LLM-PEE does not disentangle the effects of type count from type confusability; their partitioning simultaneously reduces both. Our BCS-controlled experiments (\S\ref{sec:bcs_controlled}) isolat
…[truncated 1797 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 451
}
```

</details>

---


### Tool call

_source line 202 · 2026-05-16T04:36:26.275144+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/experimental_setup.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/experimental_setup.tex"
  }
}
```

</details>

---


### Tool result

_source line 203 · 2026-05-16T04:36:26.727242+00:00_

1	\section{Experimental Setup}
2	\label{sec:experimental_setup}
3	
4	We evaluate how prompt schema size and inter-type confusability affect zero-shot LLM extraction across three information extraction tasks: named entity recognition (NER), relation extraction (RE), and event detection (ED).
5	
6	\subsection{Tasks and Datasets}
7	\label{sec:datasets}
8	
9	\paragraph{Few-NERD (NER).}
10	Few-NERD \cite{fewnerd-2021} provides 66 fine-grained entity types organized into 8 coarse categories (person, location, organization, building, art, product, event, other). The dataset spans diverse domains, making it suitable for cross-domain evaluation. We sample 1{,}000 test instances and evaluate with token-level text matching.
11	
12	\paragraph{FewRel (RE).}
13	FewRel \cite{fewrel-2018} contains 80 relation types sourced from Wikidata. Since the validation split covers only 16 relations, we combine the training and validation splits to obtain the full 80-relation pool required for schema-scale experiments, and sample 1{,}000 balanced instances (12--13 per relation type, stratified to ensure equal representation). Each instance provides a sentence with marked head and tail entities; the task is to classify the relation.
14	
15	\paragraph{MAVEN (ED).}
16	MAVEN \cite{maven-2020} defines 168 event types derived from the FrameNet ontology, making it a same-domain schema. We use the validation set (8{,}042 sentences containing 18{,}904 event mentions) for evaluation, as test set labels are not publicly available. The task requires both trigger identification and event type classification.
17	
18	Table~\ref{tab:datasets} summarizes the dataset statistics, including the Schema Confusability Score (SCS) ranges defined in \S\ref{sec:scs}.
19	
20	\begin{table}[t]
21	\centering
22	\small
23	\resizebox{\columnwidth}{!}{%
24	\begin{tabular}{llrrlll}
25	\toprule
26	\textbf{Dataset} & \textbf{Task} & \textbf{\# Types} & \textbf{\# Eval Units} & \textbf{Domain} & \textbf{BCS Range} & \textbf{Embe
…[truncated 6272 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 204 · 2026-05-16T04:36:26.727708+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex"
  }
}
```

</details>

---


### Tool result

_source line 205 · 2026-05-16T04:36:27.684361+00:00_

1	\section{Results}
2	\label{sec:results}
3	
4	Unless otherwise noted, all experiments in this section use the v1 prompt (\S\ref{sec:model}; full templates in Appendix~\ref{sec:appendix_prompts}).
5	
6	\subsection{Count-Degradation Curves}
7	\label{sec:count_curves}
8	
9	\begin{figure}[t]
10	\centering
11	\begin{minipage}[t]{0.48\columnwidth}
12	\centering
13	\includegraphics[width=\linewidth]{../../figures/paper/fig_count_curves.pdf}
14	\end{minipage}
15	\hfill
16	\begin{minipage}[t]{0.48\columnwidth}
17	\centering
18	\includegraphics[width=\linewidth]{../../figures/paper/fig_bcs_scaling.pdf}
19	\end{minipage}
20	\caption{\textbf{(a)} Count-degradation curves across three IE tasks. NER recall generally declines and RE accuracy declines monotonically with schema size; MAVEN relaxed F1 increases (\S\ref{sec:centrality_confound}). \textbf{(b)} BCS-controlled FewRel accuracy. The BCS--accuracy slope is consistent across the independent 16-relation pool and within-pool 16-relation subsets (permutation $p = 0.44$); the wider BCS range available at 80 relations produces larger absolute gaps.}
21	\label{fig:main_results}
22	\end{figure}
23	
24	We first examine how extraction performance changes as the number of types in the prompt schema increases (Experiment~1; Figure~\ref{fig:main_results}a).
25	
26	\paragraph{NER (Few-NERD).}
27	Recall generally declines from 0.72 at count${}\,=\,1$ to 0.42 at count${}\,=\,64$, a 42\% relative drop, with minor non-monotonicity at intermediate counts (e.g., 0.527 at count${}\,=\,22$ to 0.551 at count${}\,=\,44$; bootstrap 95\% CIs overlap: [0.484, 0.569] vs.\ [0.525, 0.570], indicating this reversal is within sampling variability). Precision moves in the opposite direction, rising from 0.11 to 0.52, reflecting a shift from over-prediction to under-prediction as more candidate types compete in the prompt. F1 exhibits an inverted-U shape, peaking at intermediate counts where the precision--recall trade-off is most balanced.
28	
29	\paragra
…[truncated 14911 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 956
}
```

</details>

---


### Tool call

_source line 206 · 2026-05-16T04:36:27.684814+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/sdgd_negative.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/sdgd_negative.tex"
  }
}
```

</details>

---


### Tool result

_source line 207 · 2026-05-16T04:36:28.138557+00:00_

1	\section{Why Naive Decomposition Fails}
2	\label{sec:sdgd}
3	
4	A natural intervention is to partition the schema so confusable types never co-occur. We test this with \textbf{Schema-DAG-Guided Decomposition} (SDGD), which uses greedy graph coloring on the pairwise SCS graph to assign types to low-confusability batches, merging predictions via set union. Every decomposition mode---SDGD (F1\,=\,0.241), random batching (0.320), per-type (0.292)---falls below the single-pass baseline (0.445) on Few-NERD (Table~\ref{tab:sdgd_results}). The bottleneck is \emph{merge amplification}: multiple passes accumulate contradictory predictions at union, destroying precision faster than decomposition helps recall. Confidence-gated merge does not resolve this, as poorly calibrated LLM scores \cite{llm-calibration-survey-2024} discard correct predictions as aggressively as false positives---a structural challenge with direct implications for \citet{llm-pee-2025}. Full experimental details including v1/v2 comparisons are in Appendix~\ref{sec:appendix_sdgd}.
5	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 453
}
```

</details>

---


### Tool call

_source line 208 · 2026-05-16T04:36:28.139007+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 209 · 2026-05-16T04:36:28.139325+00:00_

1	\section{Discussion}
2	\label{sec:discussion}
3	
4	\paragraph{Boundary conditions and schema design.}
5	The two-channel decomposition applies most cleanly to cross-domain schemas; for same-domain schemas, pairwise SCS should be used directly or with centrality factored out (\S\ref{sec:centrality_confound}). High-BCS accuracy converges to $\approx$51\% on both tested models; one possible explanation is a task-inherent difficulty ceiling that scaling alone cannot overcome, though broader model coverage is needed to confirm this hypothesis. RE's clean channel separation may partly reflect its closed-set classification format, which eliminates the entity detection dimension; whether the pattern holds for open extraction remains to be tested. Practitioners should monitor BCS when assembling schemas and prefer cross-domain type groupings that minimize intra-batch similarity. Prompt design also modulates the confusability effect: switching from v1 to v2 prompts reduces the RE BCS gap from 31.2\,pp to 7.9\,pp (Appendix~\ref{sec:appendix_prompt_sensitivity}), suggesting that format constraints can partially mitigate type confusion.
6	
7	\paragraph{Future directions.}
8	Naive decompose-then-merge pipelines fail due to merge amplification (\S\ref{sec:sdgd}). Three directions may address this: (1)~calibration-aware merge with cross-batch confidence normalization; (2)~confusability-aware joint decoding; and (3)~hierarchical coarse-to-fine extraction.
9	
10	\section{Conclusion}
11	\label{sec:conclusion}
12	
13	We isolated schema-induced degradation into count-driven recall decline and confusability-driven type confusion, showed these channels are separable in RE, with Channel~2 additionally impairing entity detection in NER, and confirmed that both channels replicate across model families on RE (Meta-Llama-3.1-8B-Instruct: count $r = 0.725$, confusability $\Delta = -27$\,pp), with high-BCS accuracy converging to a floor consistent across both tested models. We further identifie
…[truncated 215 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 210 · 2026-05-16T04:36:28.592337+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/checklist.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/checklist.tex"
  }
}
```

</details>

---


### Tool result

_source line 211 · 2026-05-16T04:36:28.643173+00:00_

1	\section*{Responsible NLP Research Checklist}
2	
3	For each question, the answer is \textbf{Yes}, \textbf{No}, or \textbf{N/A}. If Yes, the relevant section is indicated. If No, a justification is provided.
4	
5	\subsection*{A \quad For Every Submission}
6	
7	\begin{enumerate}[label=\textbf{A\arabic*.},leftmargin=*,itemsep=4pt]
8	
9	\item \textbf{Did you describe the limitations of your work?}
10	
11	Yes. The Limitations section (after \S\ref{sec:conclusion}) discusses single-model reliance, modest pairwise effect sizes, cross-pool slope consistency, non-significant factorial results, decomposition scope, and metric scope.
12	
13	\item \textbf{Did you discuss any potential risks of your work?}
14	
15	N/A. This is a purely analytical study of schema-induced degradation in existing LLM IE systems. It does not introduce new models, datasets, or deployment-facing artifacts. The findings characterize failure modes and are intended to inform safer schema design.
16	
17	\item \textbf{Do the abstract and introduction summarize the paper's main claims?}
18	
19	Yes. The abstract and \S\ref{sec:introduction} state the two-channel degradation pattern (count and confusability), the cross-model replication, and the negative SDGD result.
20	
21	\item \textbf{Did you use AI assistants (e.g., ChatGPT, Copilot) when working on this paper?}
22	
23	Yes. An AI coding assistant was used for experiment scripting and LaTeX formatting. All scientific claims, experimental design, and analysis were conducted by the authors.
24	
25	\end{enumerate}
26	
27	\subsection*{B \quad Scientific Artifacts}
28	
29	\begin{enumerate}[label=\textbf{B\arabic*.},leftmargin=*,itemsep=4pt]
30	
31	\item \textbf{Did you cite the creators of artifacts you used?}
32	
33	Yes. Few-NERD \cite{fewnerd-2021}, FewRel \cite{fewrel-2018}, MAVEN \cite{maven-2020}, Qwen3-32B \cite{qwen3-2025}, Meta-Llama-3.1-8B-Instruct, vLLM \cite{vllm-2023}, and all-MiniLM-L6-v2 \cite{minilm-2020} are cited in \S\ref{sec:datasets} and \S
…[truncated 4358 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 212 · 2026-05-16T04:36:29.095629+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/prompt_appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/prompt_appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 213 · 2026-05-16T04:36:29.497076+00:00_

1	\section{Prompt Templates}
2	\label{sec:appendix_prompts}
3	
4	This appendix reproduces the complete prompt templates used for all three extraction tasks.
5	All prompts are injected into a single \texttt{user} message (no system prompt); the model's chat template adds the system/assistant framing.
6	Both versions provide a JSON-formatted type schema to the vLLM constrained-decoding engine; the schema is \emph{not} included in the natural-language prompt itself.
7	We use greedy decoding (\texttt{temperature=0}, \texttt{seed=42}) throughout.
8	
9	\medskip\noindent
10	\textbf{Notation.}
11	Placeholders are shown in \texttt{\{braces\}}.
12	Text \textbf{added in v2} (relative to v1) is marked with $\triangleright$.
13	Text \textbf{removed in v2} is marked with \sout{strikethrough}.
14	
15	\subsection{Named Entity Recognition (Few-NERD)}
16	
17	\paragraph{v1 prompt (with character offsets).}
18	
19	\begin{small}
20	\begin{verbatim}
21	Extract all named entities from the following text.
22	Only extract entities of the following types:
23	- {type_1}: {definition_1}
24	- {type_2}: {definition_2}
25	  ...
26	
27	Text: {input_text}
28	
29	Output as JSON: [{"text": "...", "type": "...",
30	                  "start": ..., "end": ...}]
31	\end{verbatim}
32	\end{small}
33	
34	\noindent
35	\textbf{v1 constrained-decoding schema:}
36	\begin{small}
37	\begin{verbatim}
38	{"type": "array",
39	 "items": {"type": "object",
40	   "properties": {
41	     "text":  {"type": "string"},
42	     "type":  {"type": "string",
43	               "enum": [&lt;sorted_types>]},
44	     "start": {"type": "integer"},
45	     "end":   {"type": "integer"}},
46	   "required": ["text","type","start","end"]}}
47	\end{verbatim}
48	\end{small}
49	
50	\paragraph{v2 prompt (text+type only).}
51	
52	\begin{small}
53	\begin{verbatim}
54	Extract all named entities from the following text.
55	Only extract entities of the following types:
56	- {type_1}: {definition_1}
57	- {type_2}: {definition_2}
58	  ...
59	
60	Text
…[truncated 5004 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 401
}
```

</details>

---


### Tool call

_source line 214 · 2026-05-16T04:36:29.497567+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/references.bib"
  }
}
```

</details>

---


### Tool result

_source line 215 · 2026-05-16T04:36:29.550372+00:00_

1	% References for Schema-DAG-Extraction
2	% Generated: 2026-05-15
3	% Sources: literature_map.yaml + references_survey.md
4	
5	% =============================================================================
6	% DIRECT COMPETITORS
7	% =============================================================================
8	
9	@inproceedings{llm-pee-2025,
10	    title     = {Towards Event Extraction with Massive Types: {LLM}-based Collaborative Annotation and Partitioning Extraction},
11	    author    = {Liu, Wenxuan and Li, Zixuan and Bai, Long and Zuo, Yuxin and Xu, Daozhu and Jin, Xiaolong and Guo, Jiafeng and Cheng, Xueqi},
12	    booktitle = {Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing},
13	    year      = {2025},
14	    url       = {https://aclanthology.org/2025.emnlp-main.1743/},
15	}
16	
17	@article{parse-2025,
18	    title   = {{PARSE}: {LLM} Driven Schema Optimization for Reliable Entity Extraction},
19	    author  = {Shrimal, Anubhav and Jain, Aryan and Chowdhury, Soumyajit and Yenigalla, Promod},
20	    journal = {arXiv preprint arXiv:2510.08623},
21	    year    = {2025},
22	    url     = {https://arxiv.org/abs/2510.08623},
23	}
24	
25	@inproceedings{dee-2024,
26	    title     = {Decompose, Enrich, and Extract! Schema-aware Event Extraction using {LLM}s},
27	    author    = {Shiri, Fatemeh and Nguyen, Van and Moghimifar, Farhad and Yoo, John and Haffari, Gholamreza and Li, Yuan-Fang},
28	    booktitle = {Proceedings of the IEEE International Conference on Tools with Artificial Intelligence},
29	    year      = {2024},
30	    url       = {https://arxiv.org/abs/2406.01045},
31	}
32	
33	@inproceedings{crossagentie-2025,
34	    title     = {{CROSSAGENTIE}: Cross-Type and Cross-Task Multi-Agent {LLM} Collaboration for Zero-Shot Information Extraction},
35	    author    = {Lu, Meng and Xie, Yuzhang and Bi, Zhenyu and Cao, Shuxiang and Wang, Xuan},
36	    booktitle = {Findings of the Association for Computational Linguistics: ACL
…[truncated 19987 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 52
}
```

</details>

---


### Tool call

_source line 216 · 2026-05-16T04:37:59.169025+00:00_

called mcp__agent-ml-research__verify_references

<details open><summary>🔧 Tool call — mcp__agent-ml-research__verify_references</summary>

```json
{
  "paper_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper",
  "project": "schema-dag-extraction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "mcp__agent-ml-research__verify_references",
  "tool_args": {
    "paper_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper",
    "project": "schema-dag-extraction"
  }
}
```

</details>

---


### Tool call

_source line 217 · 2026-05-16T04:37:59.370643+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Reflect then Learn Active Prompting Information Extraction Introspective Confusion Zhao Dong AAAI 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Reflect then Learn Active Prompting Information Extraction Introspective Confusion Zhao Dong AAAI 2026"
  }
}
```

</details>

---


### Tool result

_source line 218 · 2026-05-16T04:38:36.953336+00:00_

{"result":"{\"success\": true, \"data\": {\"summary\": {\"total_bib_entries\": 43, \"total_citations\": 62, \"unique_cited_keys\": 43, \"orphan_bib\": 0, \"missing_bib\": 0, \"duplicate_keys\": 0, \"online_verified\": 32, \"online_not_found\": 5, \"online_mismatch\": 6}, \"cross_check\": {\"orphan_bib\": [], \"missing_bib\": [], \"orphan_count\": 0, \"missing_count\": 0}, \"bib_entries\": [{\"key\": \"llm-pee-2025\", \"type\": \"inproceedings\", \"title\": \"Towards Event Extraction with Massive Types: LLM-based Collaborative Annotation and Partitioning Extraction\", \"authors\": \"Liu, Wenxuan and Li, Zixuan and Bai, Long and Zuo, Yuxin and Xu, Daozhu and Jin,...\", \"year\": \"2025\", \"venue\": \"Proceedings of the 2025 Conference on Empirical Methods in Natural Language Proc...\"}, {\"key\": \"parse-2025\", \"type\": \"article\", \"title\": \"PARSE: LLM Driven Schema Optimization for Reliable Entity Extraction\", \"authors\": \"Shrimal, Anubhav and Jain, Aryan and Chowdhury, Soumyajit and Yenigalla, Promod\", \"year\": \"2025\", \"venue\": \"arXiv preprint arXiv:2510.08623\"}, {\"key\": \"dee-2024\", \"type\": \"inproceedings\", \"title\": \"Decompose, Enrich, and Extract! Schema-aware Event Extraction using LLMs\", \"authors\": \"Shiri, Fatemeh and Nguyen, Van and Moghimifar, Farhad and Yoo, John and Haffari,...\", \"year\": \"2024\", \"venue\": \"Proceedings of the IEEE International Conference on Tools with Artificial Intell...\"}, {\"key\": \"crossagentie-2025\", \"type\": \"inproceedings\", \"title\": \"CROSSAGENTIE: Cross-Type and Cross-Task Multi-Agent LLM Collaboration for Zero-Shot Information Extraction\", \"authors\": \"Lu, Meng and Xie, Yuzhang and Bi, Zhenyu and Cao, Shuxiang and Wang, Xuan\", \"year\": \"2025\", \"venue\": \"Findings of the Association for Computational Linguistics: ACL 2025\"}, {\"key\": \"dlisc-2025\", \"type\": \"article\", \"title\": \"Effective and Efficient Schema-aware Information Extraction Using On-Device LLMs\", \"authors
…[truncated 34770 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "mcp__agent-ml-research__verify_references",
  "elapsed_ms": 37784
}
```

</details>

---


### Tool result

_source line 219 · 2026-05-16T04:38:42.882539+00:00_

Web search results for query: "Reflect then Learn Active Prompting Information Extraction Introspective Confusion Zhao Dong AAAI 2026"

Links: [{"title":"[2508.10036] Reflect then Learn: Active Prompting for Information Extraction Guided by Introspective Confusion","url":"https://arxiv.org/abs/2508.10036"},{"title":"Reflect then Learn: Active Prompting for Information Extraction Guided by Introspective Confusion","url":"https://arxiv.org/html/2508.10036v1"},{"title":"SAIL: Sample-Centric In-Context Learning for Document Information Extraction | Request PDF","url":"https://www.researchgate.net/publication/390720994_SAIL_Sample-Centric_In-Context_Learning_for_Document_Information_Extraction"},{"title":"Information Retrieval","url":"https://arxiv.org/list/cs.IR/recent?skip=12&show=100"},{"title":"Computer Science","url":"https://www.arxiv.org/list/cs/recent?skip=1168&show=1000"},{"title":"Proceedings of the AAAI Conference on Artificial Intelligence","url":"https://ojs.aaai.org/index.php/AAAI/index"},{"title":"Mitigating pervasive modality absence through multimodal ...","url":"https://dl.acm.org/doi/abs/10.1609/aaai.v39i25.34883"},{"title":"Computer Science Aug 2025","url":"https://arxiv.org/list/cs/2025-08?skip=4500&show=2000"},{"title":"AAAI 2026 | OpenReview","url":"https://openreview.net/group?id=AAAI.org%2F2026"},{"title":"The 40th Annual AAAI Conference on Artificial Intelligence","url":"https://aaai.org/conference/aaai/aaai-26/"}]

Based on the search results, here's what I found about the paper you're looking for:

## Paper Summary

"Reflect then Learn: Active Prompting for Information Extraction Guided by Introspective Confusion" is a research paper by Dong Zhao, Yadong Wang, and other authors.

**Key Contribution:**
The authors introduce Active Prompting for Information Extraction (APIE), a novel active prompting framework guided by a principle they term introspective confusion.

**Problem Addressed:**
Large Language Models (LLMs) show remarkable potential f
…[truncated 848 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 43511
}
```

</details>

---


### Tool call

_source line 220 · 2026-05-16T04:40:49.383300+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Round 3 Review — Reviewer 1 (方法严谨性 + 实验设计 + 统计分析)\n\n### 1. Summary\n\n本文通过控制实验设计首次隔离了 training-free LLM IE 中 schema 退化的两个独立通道（type count 和 type confusability），在 NER/RE/ED 三个任务上验证了 pairwise SCS 对 type confusion 的预测力，并报告了 confusability-aware decomposition 的信息性负结果。相比 Round 2，论文在统计注解、prompt 透明度和 limitations 覆盖方面有显著改善。主要遗留问题集中在 prompt 敏感性对主要 claim 的影响未在正文充分展现，以及 BCS-controlled 实验的因果推断语言略微超出证据支持范围。\n\n---\n\n### 2. Strengths\n\n**S1: 实验设计精良，变量隔离到位。** Count curves（固定 confusability 随机化，变 count）和 BCS-controlled experiments（固定 count，变 confusability）互补设计合理，within-pool 控制（从 80-rel pool 抽 16-rel 子集）有效排除了 pool composition 混淆因素。这在该领域是首次系统性的因素隔离。(§3.3, Table 5)\n\n**S2: 统计方法论全面、透明。** Bootstrap CI（B=10,000）、type-level cluster bootstrap（考虑 pair 非独立性）、permutation test（slope comparison p=0.436）、Spearman + Pearson 双验证等。特别是对 pairwise CI 和 cluster bootstrap CI 的差异做了诚实解释——pair-level tighter because treating pairs as independent, cluster bootstrap wider but still significant（Few-NERD: [0.069, 0.219]; MAVEN: [0.081, 0.185]）。(§4.2, Table 2)\n\n**S3: 诚实报告负面结果和 limitations。** SDGD 全面失败（best F1=0.32 vs single-pass 0.45）、factorial test 不显著（z=-0.67, p=0.50）、MAVEN centrality confound、80-rel full condition underpowered 等均明确报告且 framing 恰当。Limitations section 涵盖 8 项，比多数投稿更全面。(§5, Limitations, Appendix C)\n\n**S4: Cross-model validation 设计合理。** Llama-3.1-8B 在 NER count channel（r=0.725）和 RE confusability channel（Δ=-27.1pp）上复现了主要发现。High-BCS accuracy 跨模型收敛到 ~51% floor 是一个有趣且有启发性的发现。(§4.3, Appendix Tables 6-7)\n\n**S5: Prompt 完整性大幅改善。** Appendix D 包含三个任务的完整 prompt template（v1/v2 对比，包括 JSON schema），v1→v2 差异明确标注（offset removal + format constraints），RE 单版本明确说明。(Appendix §D)\n\n**S6: Centrality confound 分析是一项独立贡献。** 识别 per-type BCS 在 same-domain schema 上因 embedding collapse 而反转（MAVEN: ρ=+0.184），并通过 residualized analysis 证实 confound（控制 log freq + degree centrality 后 p>0.2），同时保持 pairwise SCS 有效（r=0.129, p<10⁻¹⁰）。(§4.5, Appendix E)\n\n---\n\n### 3. Weaknesses\n\n**W1 [major] Prompt 敏感性严重削弱核心 claim，但正文未充分展现。**\n- 具体位置：§4.3 main text vs. Appendix F (§prompt_sensitivity)\n- 问题：v2 prompt 将 RE BCS gap 从 31.2pp 缩减至 7.9pp（CI: [-5.2, +21.5] 包含零，n=5）。这意味着论文的标志性数字 31.2pp 有相当部分来自 prompt-induced noise 而非 genuine type confusion。论文在 Appendix F 坦诚讨论了这一点（\"the v1 extreme-batch gap reflects both genuine type confusion and prompt-induced noise\"），Discussion 也提及（\"switching from v1 to v2 reduces the RE BCS gap from 31.2pp to 7.9pp\"），但正文核心 narrative 仍以 v1 结果为主锚点。Abstract 虽已用 quartile Δ=-7.4pp 替换，但 Introduction finding (2) 仍引用 \"accuracy gaps reaching 31.2pp under extreme-batch comparison\"。\n- 影响：读者可能高估 confusability 的 practical magnitude。v2 gap 7.9pp 与 CI 包含零意味着在 reasonable prompt design 下，confusability channel 在 RE 上可能不显著——这与论文的主题 \"type confusability drives degradation\" 存在张力。\n- 建议：正文 §4.3 应增加一段明确讨论 v2 attenuation 的文字（不仅放在 Appendix），且 Introduction 引用 31.2pp 时应同时注明 v2 结果。\n\n**W2 [major] \"Interventional\" 因果语言超出实验设计所支持的推断。**\n- 具体位置：§4.3 第一句 \"To move from correlational to interventional evidence\"；§4.4 \"confusability drives substitution errors\"\n- 问题：BCS-controlled experiments 通过构造 batch（选择高/低 BCS 的 type 组合）来操纵 BCS，但这不是真正的 intervention——batch composition（哪些具体 types 被选入）与 BCS 完全共变。高 BCS batch 里的 types 可能在 inherent difficulty、frequency、definition quality 等维度上系统性地不同于低 BCS types。Within-pool analysis 部分缓解了 pool composition confound，但未控制 type-level properties（如 type frequency in evaluation corpus）。论文在 §4.2 讨论了 entity frequency 等 confounding factors，但在 §4.3 的因果 framing 中未回溯这些 caveats。\n- 影响：Reviewer 和读者可能将 BCS-controlled 结果误读为 causal identification，实际上是 quasi-experimental。\n- 建议：将 \"interventional\" 改为 \"quasi-experimental\" 或 \"controlled comparison\"；在 §4.3 开头明确 acknowledge 残余 confounds（type frequency, definition quality 等可能与 BCS 共变）。\n\n**W3 [minor] Pairwise r²=1.3-1.7% 到 batch-level gap 的信号放大缺乏形式化论证。**\n- 具体位置：§4.2 最后一段，§practical_magnitude\n- 问题：论文声称 \"pairwise $r^2$ is modest, the signal compounds at the batch level into accuracy gaps reaching 31.2pp\"。§practical_magnitude 提供了经验数据（IQR=0.054 → 2.2pp expected gap），但缺乏从 pair-level variance explained 到 batch-level effect magnitude 的数学推导。Compounding mechanism 不清楚：为什么 1.3% pair-level variance 能在 batch aggregation 下产生 2-31pp batch-level gaps？是线性叠加、还是非线性放大？\n- 建议：增加一个简短的形式化说明（即使放在 Appendix），解释 pair-level r² 如何通过 BCS aggregation 转化为 batch-level accuracy variation。或者承认这是一个 empirical observation 而非 theoretically derived relationship。\n\n**W4 [minor] 正文视觉支持不足。**\n- 具体位置：全文仅 Figure 1（双 panel）\n- 问题：对于一篇包含 count curves、BCS-controlled experiments、error taxonomy、cross-model validation、centrality confound、SDGD 六大实验模块的论文，仅一张主图不足以引导读者。Error taxonomy visualization（Appendix Figure 2）、within-pool BCS regression scatter、MAVEN centrality confound 等都值得在正文呈现。\n- 建议：至少增加 error taxonomy 图或 within-pool regression scatter 到正文。8 页限制内有空间（当前 Discussion 和 Conclusion 较短）。\n\n**W5 [minor] FewRel evaluation 的 classification vs extraction gap 讨论不足。**\n- 具体位置：Limitations item 7, item 8\n- 问题：FewRel 是 closed-set classification（给定 entity pair 预测 relation），不是 open extraction。论文的最清晰 channel separation 恰恰在 RE 上获得——但这可能正是因为 classification format 消除了 entity detection 维度（Limitations item 8 已承认）。这意味着 \"confusability drives substitution errors while detection remains stable\"（§4.4）的 clean separation 可能是 task format artifact 而非 confusability 的本质特征。\n- 影响：论文最强的 evidence（RE BCS gap）的 external validity 受限。\n- 建议：在 Discussion 中更 prominently 讨论这一 threat to validity，而非仅在 Limitations 末尾一句。\n\n---\n\n### 4. Questions for Authors\n\n**Q1:** v2 prompt 下 RE BCS gap 的 CI 包含零（[-5.2, +21.5]）。如果增加 batch 数量（从 n=5 到例如 n=25），是否有初步迹象表明 gap 会达到统计显著？或者 7.9pp 本身可能只是 noise？\n\n**Q2:** Within-pool analysis（80-pool → 16-sub）的 quartile Δ CI 也包含零（[-8.17, +0.38]）。这是否意味着在控制 pool composition 后，BCS 效应在 80-rel pool 内的 typical batches 中实际上不显著？\n\n**Q3:** High-BCS accuracy 跨模型收敛到 ~51%。这个 floor 是否可能只是 random guessing among confusable types 的 expected accuracy？对于包含 8 个 relations 的高 BCS batch，如果模型在高相似 types 间均匀猜测，expected accuracy 约为多少？\n\n**Q4:** NER 的 pairwise SCS-confusion correlation 使用了 Qwen3 embedding（r=0.112），而 RE 使用 MiniLM 的 BCS。embedding 选择是否影响效应方向或大小？Few-NERD 用 MiniLM 做 SCS 结果如何？\n\n**Q5:** SDGD 实验全部使用 v1 prompt（Table 8 caption 确认）。v2 prompt 的 higher precision 是否可能改善 merge amplification 问题？是否考虑过 v2 prompt + SDGD 的组合？\n\n---\n\n### 5. Missing References\n\n- **Chia et al. (2022)** \"RELATIONPROMPT: Leveraging Prompts to Generate Synthetic Data for Zero-Shot Relation Triplet Extraction\" — zero-shot RE 的 prompt-based approach，与 FewRel 实验设计相关\n- **Li et al. (2023)** \"Evaluating ChatGPT's Information Extraction Capabilities\" 的 arXiv 版本在 OpenAlex 上未找到（not_found），建议补充 DOI 或确认出版状态\n\n---\n\n### 6. Round 2 Issue Resolution Verification\n\n| Issue ID | Description | Status | Evidence |\n|----------|-------------|--------|----------|\n| `MW1` | Abstract 9.1pp → bootstrapped Δ; Table 3 caption illustrative | **PASS** | Abstract: \"quartile gap reaching −7.4pp (95% CI: [−9.4, −5.5])\"; Table 3 caption: \"The 16-relation condition used a single extreme batch per BCS level\" |\n| `MW2` | §practical_magnitude 论证 realistic effect size | **PASS** | IQR=0.054 → 2.2pp (CI: [0.4, 4.0])，直接 quartile comparison 3.9pp，10th-90th 4.2pp。Clear and well-calibrated. |\n| `SW3` | v1/v2 prompt 混淆 → prompt_appendix.tex 完整 | **PASS** | Appendix D 包含 NER v1/v2、ED v1/v2、RE 完整 template + JSON schema + v1→v2 diff 说明。§4 开头标注 \"all experiments use v1 unless noted\"。 |\n| `R2-N3-80rel` | 31.2pp 引用时注明 80-rel 不显著 | **PASS** | 所有 31.2pp 出现处均标注 \"extreme-batch comparison\" + 引导读者到 §practical_magnitude 或 Table 5。Appendix C 明确 \"do not draw inferential conclusions from [full 80-rel]\"。 |\n| `m3` | Responsible NLP Checklist 完整 | **PASS** | checklist.tex 覆盖 A1-A4, B1-B6, C1-C4, D1-D5, E1，格式正确，引用具体 section。 |\n| `REF1` | reflect-learn-2026 引用真实性 | **PASS** | Web search 确认 arXiv:2508.10036 存在，作者 Zhao, Dong et al.，AAAI 2026 发表。OpenAlex 匹配 title + year。 |\n| `R2-W4-sdgd-scope` | SDGD 仅在 NER 测试 → Limitations 标注 | **PASS** | Limitations item 5: \"Our SDGD experiments test only span-level NER (Few-NERD)...whether decomposition helps or hurts RE or ED remains untested\" |\n| `MW4` | 正文仅一幅 Figure | **PARTIAL** | 仍然只有 Figure 1（双 panel）。Error taxonomy 图、cross-model 表、residualized BCS 表等均在 Appendix。正文可容纳更多视觉内容。 |\n\n---\n\n### 7. Overall Score: **3.5** (Borderline Conference)\n\n**Confidence: 4** (Quite sure. I tried to check the important points carefully.)\n\n**一句话总结：** 实验设计精良、统计方法透明的 controlled empirical study，但 prompt 敏感性严重削弱了核心 claim 的 robustness（v2 gap CI 包含零），且因果语言超出 quasi-experimental 设计所能支撑的推断水平。\n\n### 8. Soundness: **3.5**\n\n统计方法（bootstrap CI、cluster bootstrap、permutation test）执行规范且透明。主要扣分点：(1) BCS-controlled 实验的 \"interventional\" 定位不当——未控制 type frequency/definition quality 等与 BCS 共变的 confounders；(2) v2 prompt 下 RE 核心效应的 CI 包含零但未在正文充分讨论；(3) pair-level r² 到 batch-level gap 的放大机制缺乏形式化。如果将因果语言降级为 \"controlled observational\" 并在正文突出 v2 attenuation，soundness 可上升到 4。\n\n### 9. Excitement: **3.0**\n\n研究问题有实际意义（schema complexity 是 training-free IE 的真实痛点），controlled experimental design 是该领域的方法论进步。但 excitement 受限于：(1) 核心 predictor (SCS) 的 variance explained 仅 1.3-1.7%；(2) 论文的 actionable takeaway 偏有限——SDGD 失败意味着没有提出可行的 engineering solution；(3) 主要的 clean evidence 来自 RE classification task，external validity 待验证。如果能增加一个 open extraction RE 实验或展示 SCS-based schema optimization 的实际收益，excitement 可显著提升。",
  "reviewer_id": "1",
  "project": "schema-dag-extraction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Round 3 Review — Reviewer 1 (方法严谨性 + 实验设计 + 统计分析)\n\n### 1. Summary\n\n本文通过控制实验设计首次隔离了 training-free LLM IE 中 schema 退化的两个独立通道（type count 和 type confusability），在 NER/RE/ED 三个任务上验证了 pairwise SCS 对 type confusion 的预测力，并报告了 confusability-aware decomposition 的信息性负结果。相比 Round 2，论文在统计注解、prompt 透明度和 limitations 覆盖方面有显著改善。主要遗留问题集中在 prompt 敏感性对主要 claim 的影响未在正文充分展现，以及 BCS-controlled 实验的因果推断语言略微超出证据支持范围。\n\n---\n\n### 2. Strengths\n\n**S1: 实验设计精良，变量隔离到位。** Count curves（固定 confusability 随机化，变 count）和 BCS-controlled experiments（固定 count，变 confusability）互补设计合理，within-pool 控制（从 80-rel pool 抽 16-rel 子集）有效排除了 pool composition 混淆因素。这在该领域是首次系统性的因素隔离。(§3.3, Table 5)\n\n**S2: 统计方法论全面、透明。** Bootstrap CI（B=10,000）、type-level cluster bootstrap（考虑 pair 非独立性）、permutation test（slope comparison p=0.436）、Spearman + Pearson 双验证等。特别是对 pairwise CI 和 cluster bootstrap CI 的差异做了诚实解释——pair-level tighter because treating pairs as independent, cluster bootstrap wider but still significant（Few-NERD: [0.069, 0.219]; MAVEN: [0.081, 0.185]）。(§4.2, Table 2)\n\n**S3: 诚实报告负面结果和 limitations。** SDGD 全面失败（best F1=0.32 vs single-pass 0.45）、factorial test 不显著（z=-0.67, p=0.50）、MAVEN centrality confound、80-rel full condition underpowered 等均明确报告且 framing 恰当。Limitations section 涵盖 8 项，比多数投稿更全面。(§5, Limitations, Appendix C)\n\n**S4: Cross-model validation 设计合理。** Llama-3.1-8B 在 NER count channel（r=0.725）和 RE confusability channel（Δ=-27.1pp）上复现了主要发现。High-BCS accuracy 跨模型收敛到 ~51% floor 是一个有趣且有启发性的发现。(§4.3, Appendix Tables 6-7)\n\n**S5: Prompt 完整性大幅改善。** Appendix D 包含三个任务的完整 prompt template（v1/v2 对比，包括 JSON schema），v1→v2 差异明确标注（offset removal + format constraints），RE 单版本明确说明。(Appendix §D)\n\n**S6: Centrality confound 分析是一项独立贡献。** 识别 per-type BCS 在 same-domain schema 上因 embedding collapse 而反转（MAVEN: ρ=+0.184），并通过 residualized analysis 证实 confound（控制 log freq + degree centrality 后 p>0.2），同时保持 pairwise SCS 有效（r=0.129, p<10⁻¹⁰）。(§4.5, Appendix E)\n\n---\n\n### 3. Weaknesses\n\n**W1 [major] Prompt 敏感性严重削弱核心 claim，但正文未充分展现。**\n- 具体位置：§4.3 main text vs. Appendix F (§prompt_sensitivity)\n- 问题：v2 prompt 将 RE BCS gap 从 31.2pp 缩减至 7.9pp（CI: [-5.2, +21.5] 包含零，n=5）。这意味着论文的标志性数字 31.2pp 有相当部分来自 prompt-induced noise 而非 genuine type confusion。论文在 Appendix F 坦诚讨论了这一点（\"the v1 extreme-batch gap reflects both genuine type confusion and prompt-induced noise\"），Discussion 也提及（\"switching from v1 to v2 reduces the RE BCS gap from 31.2pp to 7.9pp\"），但正文核心 narrative 仍以 v1 结果为主锚点。Abstract 虽已用 quartile Δ=-7.4pp 替换，但 Introduction finding (2) 仍引用 \"accuracy gaps reaching 31.2pp under extreme-batch comparison\"。\n- 影响：读者可能高估 confusability 的 practical magnitude。v2 gap 7.9pp 与 CI 包含零意味着在 reasonable prompt design 下，confusability channel 在 RE 上可能不显著——这与论文的主题 \"type confusability drives degradation\" 存在张力。\n- 建议：正文 §4.3 应增加一段明确讨论 v2 attenuation 的文字（不仅放在 Appendix），且 Introduction 引用 31.2pp 时应同时注明 v2 结果。\n\n**W2 [major] \"Interventional\" 因果语言超出实验设计所支持的推断。**\n- 具体位置：§4.3 第一句 \"To move from correlational to interventional evidence\"；§4.4 \"confusability drives substitution errors\"\n- 问题：BCS-controlled experiments 通过构造 batch（选择高/低 BCS 的 type 组合）来操纵 BCS，但这不是真正的 intervention——batch composition（哪些具体 types 被选入）与 BCS 完全共变。高 BCS batch 里的 types 可能在 inherent difficulty、frequency、definition quality 等维度上系统性地不同于低 BCS types。Within-pool analysis 部分缓解了 pool composition confound，但未控制 type-level properties（如 type frequency in evaluation corpus）。论文在 §4.2 讨论了 entity frequency 等 confounding factors，但在 §4.3 的因果 framing 中未回溯这些 caveats。\n- 影响：Reviewer 和读者可能将 BCS-controlled 结果误读为 causal identification，实际上是 quasi-experimental。\n- 建议：将 \"interventional\" 改为 \"quasi-experimental\" 或 \"controlled comparison\"；在 §4.3 开头明确 acknowledge 残余 confounds（type frequency, definition quality 等可能与 BCS 共变）。\n\n**W3 [minor] Pairwise r²=1.3-1.7% 到 batch-level gap 的信号放大缺乏形式化论证。**\n- 具体位置：§4.2 最后一段，§practical_magnitude\n- 问题：论文声称 \"pairwise $r^2$ is modest, the signal compounds at the batch level into accuracy gaps reaching 31.2pp\"。§practical_magnitude 提供了经验数据（IQR=0.054 → 2.2pp expected gap），但缺乏从 pair-level variance explained 到 batch-level effect magnitude 的数学推导。Compounding mechanism 不清楚：为什么 1.3% pair-level variance 能在 batch aggregation 下产生 2-31pp batch-level gaps？是线性叠加、还是非线性放大？\n- 建议：增加一个简短的形式化说明（即使放在 Appendix），解释 pair-level r² 如何通过 BCS aggregation 转化为 batch-level accuracy variation。或者承认这是一个 empirical observation 而非 theoretically derived relationship。\n\n**W4 [minor] 正文视觉支持不足。**\n- 具体位置：全文仅 Figure 1（双 panel）\n- 问题：对于一篇包含 count curves、BCS-controlled experiments、error taxonomy、cross-model validation、centrality confound、SDGD 六大实验模块的论文，仅一张主图不足以引导读者。Error taxonomy visualization（Appendix Figure 2）、within-pool BCS regression scatter、MAVEN centrality confound 等都值得在正文呈现。\n- 建议：至少增加 error taxonomy 图或 within-pool regression scatter 到正文。8 页限制内有空间（当前 Discussion 和 Conclusion 较短）。\n\n**W5 [minor] FewRel evaluation 的 classification vs extraction gap 讨论不足。**\n- 具体位置：Limitations item 7, item 8\n- 问题：FewRel 是 closed-set classification（给定 entity pair 预测 relation），不是 open extraction。论文的最清晰 channel separation 恰恰在 RE 上获得——但这可能正是因为 classification format 消除了 entity detection 维度（Limitations item 8 已承认）。这意味着 \"confusability drives substitution errors while detection remains stable\"（§4.4）的 clean separation 可能是 task format artifact 而非 confusability 的本质特征。\n- 影响：论文最强的 evidence（RE BCS gap）的 external validity 受限。\n- 建议：在 Discussion 中更 prominently 讨论这一 threat to validity，而非仅在 Limitations 末尾一句。\n\n---\n\n### 4. Questions for Authors\n\n**Q1:** v2 prompt 下 RE BCS gap 的 CI 包含零（[-5.2, +21.5]）。如果增加 batch 数量（从 n=5 到例如 n=25），是否有初步迹象表明 gap 会达到统计显著？或者 7.9pp 本身可能只是 noise？\n\n**Q2:** Within-pool analysis（80-pool → 16-sub）的 quartile Δ CI 也包含零（[-8.17, +0.38]）。这是否意味着在控制 pool composition 后，BCS 效应在 80-rel pool 内的 typical batches 中实际上不显著？\n\n**Q3:** High-BCS accuracy 跨模型收敛到 ~51%。这个 floor 是否可能只是 random guessing among confusable types 的 expected accuracy？对于包含 8 个 relations 的高 BCS batch，如果模型在高相似 types 间均匀猜测，expected accuracy 约为多少？\n\n**Q4:** NER 的 pairwise SCS-confusion correlation 使用了 Qwen3 embedding（r=0.112），而 RE 使用 MiniLM 的 BCS。embedding 选择是否影响效应方向或大小？Few-NERD 用 MiniLM 做 SCS 结果如何？\n\n**Q5:** SDGD 实验全部使用 v1 prompt（Table 8 caption 确认）。v2 prompt 的 higher precision 是否可能改善 merge amplification 问题？是否考虑过 v2 prompt + SDGD 的组合？\n\n---\n\n### 5. Missing References\n\n- **Chia et al. (2022)** \"RELATIONPROMPT: Leveraging Prompts to Generate Synthetic Data for Zero-Shot Relation Triplet Extraction\" — zero-shot RE 的 prompt-based approach，与 FewRel 实验设计相关\n- **Li et al. (2023)** \"Evaluating ChatGPT's Information Extraction Capabilities\" 的 arXiv 版本在 OpenAlex 上未找到（not_found），建议补充 DOI 或确认出版状态\n\n---\n\n### 6. Round 2 Issue Resolution Verification\n\n| Issue ID | Description | Status | Evidence |\n|----------|-------------|--------|----------|\n| `MW1` | Abstract 9.1pp → bootstrapped Δ; Table 3 caption illustrative | **PASS** | Abstract: \"quartile gap reaching −7.4pp (95% CI: [−9.4, −5.5])\"; Table 3 caption: \"The 16-relation condition used a single extreme batch per BCS level\" |\n| `MW2` | §practical_magnitude 论证 realistic effect size | **PASS** | IQR=0.054 → 2.2pp (CI: [0.4, 4.0])，直接 quartile comparison 3.9pp，10th-90th 4.2pp。Clear and well-calibrated. |\n| `SW3` | v1/v2 prompt 混淆 → prompt_appendix.tex 完整 | **PASS** | Appendix D 包含 NER v1/v2、ED v1/v2、RE 完整 template + JSON schema + v1→v2 diff 说明。§4 开头标注 \"all experiments use v1 unless noted\"。 |\n| `R2-N3-80rel` | 31.2pp 引用时注明 80-rel 不显著 | **PASS** | 所有 31.2pp 出现处均标注 \"extreme-batch comparison\" + 引导读者到 §practical_magnitude 或 Table 5。Appendix C 明确 \"do not draw inferential conclusions from [full 80-rel]\"。 |\n| `m3` | Responsible NLP Checklist 完整 | **PASS** | checklist.tex 覆盖 A1-A4, B1-B6, C1-C4, D1-D5, E1，格式正确，引用具体 section。 |\n| `REF1` | reflect-learn-2026 引用真实性 | **PASS** | Web search 确认 arXiv:2508.10036 存在，作者 Zhao, Dong et al.，AAAI 2026 发表。OpenAlex 匹配 title + year。 |\n| `R2-W4-sdgd-scope` | SDGD 仅在 NER 测试 → Limitations 标注 | **PASS** | Limitations item 5: \"Our SDGD experiments test only span-level NER (Few-NERD)...whether decomposition helps or hurts RE or ED remains untested\" |\n| `MW4` | 正文仅一幅 Figure | **PARTIAL** | 仍然只有 Figure 1（双 panel）。Error taxonomy 图、cross-model 表、residualized BCS 表等均在 Appendix。正文可容纳更多视觉内容。 |\n\n---\n\n### 7. Overall Score: **3.5** (Borderline Conference)\n\n**Confidence: 4** (Quite sure. I tried to check the important points carefully.)\n\n**一句话总结：** 实验设计精良、统计方法透明的 controlled empirical study，但 prompt 敏感性严重削弱了核心 claim 的 robustness（v2 gap CI 包含零），且因果语言超出 quasi-experimental 设计所能支撑的推断水平。\n\n### 8. Soundness: **3.5**\n\n统计方法（bootstrap CI、cluster bootstrap、permutation test）执行规范且透明。主要扣分点：(1) BCS-controlled 实验的 \"interventional\" 定位不当——未控制 type frequency/definition quality 等与 BCS 共变的 confounders；(2) v2 prompt 下 RE 核心效应的 CI 包含零但未在正文充分讨论；(3) pair-level r² 到 batch-level gap 的放大机制缺乏形式化。如果将因果语言降级为 \"controlled observational\" 并在正文突出 v2 attenuation，soundness 可上升到 4。\n\n### 9. Excitement: **3.0**\n\n研究问题有实际意义（schema complexity 是 training-free IE 的真实痛点），controlled experimental design 是该领域的方法论进步。但 excitement 受限于：(1) 核心 predictor (SCS) 的 variance explained 仅 1.3-1.7%；(2) 论文的 actionable takeaway 偏有限——SDGD 失败意味着没有提出可行的 engineering solution；(3) 主要的 clean evidence 来自 RE classification task，external validity 待验证。如果能增加一个 open extraction RE 实验或展示 SCS-based schema optimization 的实际收益，excitement 可显著提升。",
    "reviewer_id": "1",
    "project": "schema-dag-extraction"
  }
}
```

</details>

---


### Tool result

_source line 221 · 2026-05-16T04:40:56.216173+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 6832
}
```

</details>

---


### Assistant

_source line 222 · 2026-05-16T04:41:03.913151+00:00_

审稿意见已提交给 Review Director。

总结：

- **Overall 3.5（Borderline Conference）**，Soundness 3.5，Excitement 3.0，Confidence 4
- **主要优势**：实验设计精良（count/confusability 隔离）、统计方法全面透明（cluster bootstrap, permutation test）、负面结果诚实报告、prompt 模板完整
- **两个 major issues**：(1) v2 prompt 将 RE BCS gap 从 31.2pp 缩至 7.9pp（CI 含零），核心 claim robustness 存疑但正文未充分讨论；(2) "interventional" 因果语言超出 quasi-experimental 设计支撑范围
- **Round 2 修复验证**：7 项 PASS、1 项 PARTIAL（正文仍仅 1 幅图）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1"
}
```

</details>

---


## Round 6

## Round 6

2 recorded events


### User

_source line 223 · 2026-05-16T04:46:01.417874+00:00_

[Round 3 审稿请求]:
## 交叉分享 — 请逐条回应 Reviewer 2 的审稿意见

以下是 Reviewer 2 的完整审稿意见。请对每一条 Weakness 和 Question 逐条回应：
- **[AGREE]** 同意并说明理由
- **[REBUT]** 反驳并提供具体证据（cite Section/Table/Figure）

---

### Reviewer 2 评分
- Overall: 3.5/5, Novelty: 3.5/5, Excitement: 3/5, Confidence: 4/5

### Reviewer 2 Strengths (S1-S6)
- S1: 控制实验设计是核心亮点——count curves + BCS-controlled 构成相关性→干预性证据链，within-pool 排除 composition confound
- S2: Centrality confound 分析具独立方法论价值（partial correlation 控制 log freq + degree centrality）
- S3: Cross-model 51% floor convergence 是有趣发现，已恰当标注为 hypothesis
- S4: 统计报告优秀：bootstrap CI、cluster bootstrap、selection bias 警告
- S5: Negative SDGD result 准确定位 merge amplification 瓶颈
- S6: Limitations 极详尽（8 条）

### Reviewer 2 Weaknesses
- **W1 [major]**: 核心效应量极小（r²=1.3-1.7%，typical-batch gap 仅 2.2 pp），abstract/intro 侧重报道 extreme-batch gap (31.2 pp) 可能误导读者。建议更显著报告 typical-batch magnitude。
- **W2 [major]**: 正文仅 1 Figure + 4 Tables，error taxonomy 和 cross-model 结果全在 appendix。建议将核心证据移入正文。
- **W3 [minor]**: §5 SDGD 仍仅 ~100 词/4 句，与其 contribution 地位不匹配
- **W4 [minor]**: Abstract 中 MAVEN count-curve 反转仅隐式处理（"generally"），未独立陈述
- **W5 [minor]**: RE clean channel separation 可能是 closed-set classification format 的产物，abstract/intro 未附加 caveat
- **W6 [minor]**: 不同 dataset 使用不同 embedding（Qwen3 vs MiniLM），缺少 cross-embedding sensitivity ablation

### Reviewer 2 Key Questions
- Q1: SCS/BCS 在什么阈值以上才值得干预？（2.2 pp typical gap 是否有 actionable 决策边界？）
- Q2: Pairwise r² → batch-level gap 的放大机制？（additive vs nonlinear？）
- Q3: MAVEN count-curve 反转的三个归因中哪个贡献最大？
- Q4: 51% floor 是否接近 random-chance baseline？

### Reviewer 2 Round 2 Issue Verification
9/11 PASS，2 PARTIAL：
- PARTIAL: SW4 (MAVEN count-curve reversal 在 abstract 中仍仅隐式); R2-m-sdgd-short (§5 仍 ~4 句)

### Reviewer 2 格式合规
页数、匿名、Checklist、ACL [review]、引用均合规。

---

请逐条回应上述 Weaknesses (W1-W6) 和 Questions (Q1-Q4)，对每条标注 [AGREE] 或 [REBUT]。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 224 · 2026-05-16T04:47:53.364042+00:00_

以下是我对 Reviewer 2 各条意见的逐条回应。

---

## Weaknesses 逐条回应

### W1 [major] — Effect size 小，abstract/intro 侧重 extreme-batch gap

**[REBUT]**

R2 的关切有道理但程度被夸大了。当前版本 abstract 的主数字已经是 independent 16-rel pool 的 quartile gap **−7.4 pp (95% CI: [−9.4, −5.5])**，不是 31.2 pp。31.2 pp 在 abstract 中完全没有出现。Introduction §1 第12行提到 "accuracy gaps reaching 31.2 pp under extreme-batch comparison" 时**同句**附带了 "(typical-batch gap ≈2–4 pp, §practical_magnitude)" 的 caveat。§practical_magnitude（results.tex）进一步报告 IQR 产生的预期 gap 仅 2.2 pp (CI: [0.4, 4.0])，直接量化了 typical experience。Table 5 caption 也注明了 extreme vs. typical 的区分。

不过，pairwise r²=1.3–1.7% 确实值得在 abstract 中更显式量化，目前 abstract 只说了 "modest in magnitude"，可以加入具体数字让读者在第一时间校准期望。这方面 R2 有道理。

---

### W2 [major] — 正文仅 1 Figure + 4 Tables

**[AGREE]**

完全同意。对于一篇以实证为核心的 8 页论文，error taxonomy（Table in Appendix §A）和 cross-model BCS 表（Appendix Table）是支撑 Contribution 1（multi-channel pattern）和 cross-model validation 的关键证据，却全部放在 appendix。特别是 error taxonomy 的 IntraSub ρ=1.0 是 Channel 2 机制论证的核心数据点，正文 §4.4 仅用文字引用了这些数字。Figure 1 承载了两个 panel（count curves + BCS scaling），信息密度很高但覆盖面不够。

建议至少将 error taxonomy table 或 fig\_error\_taxonomy.pdf 移入正文，并考虑将 cross-model BCS table 合并为正文 Table 3 的扩展列。这对 8 页 long paper 是可行的（目前 §5 和 §6 加起来不到 1 页，有空间）。

---

### W3 [minor] — §5 SDGD 篇幅过短

**[AGREE]**

同意。§5（sdgd\_negative.tex）正文仅约 100 词 / 4 句，而 SDGD 是 Introduction 列出的第四条 contribution（"informative negative result"）。Appendix §B 有完整的 protocol 和 v1/v2 对比，但正文没有给出足够的 merge amplification 机制分析。读者需要翻到 appendix 才能理解为什么 precision 从 0.563 暴跌到 0.210。建议正文至少增加一段，简要展示 precision-recall tradeoff 的定量分解（multi-pass → union → FP accumulation 的逻辑链）。

---

### W4 [minor] — Abstract 中 MAVEN 反转仅隐式处理

**[AGREE]**

同意。Abstract 用 "a count channel that **generally** suppresses recall" 处理了 MAVEN 例外，但 "generally" 这个词承载了太多信息——读者很容易误读为 "在所有三个数据集上都 suppress recall"。MAVEN 的反转（F1 从 0.106 上升到 0.247）是一个重要的 boundary condition，值得在 abstract 中用半句话显式陈述，例如 "...while same-domain schemas (MAVEN) exhibit the opposite trend due to contextual disambiguation"。这也有助于与 §4.5 centrality confound 形成呼应。

---

### W5 [minor] — RE clean channel separation 可能是 classification artifact

**[REBUT]**（部分同意）

R2 指出 abstract/intro 未附 caveat 是对的。Abstract 说 "cleanly separable in RE" 但没有提及 closed-set classification format 的可能影响。Limitations item 8 和 Discussion §6 都讨论了这一点（"RE's clean channel separation may partly reflect its closed-set classification format, which eliminates the entity detection dimension"），但这些 caveats 来得太晚。

不过，我认为 R2 将此标注为 minor 是合理的，不需要升级为 major。RE 的 clean separation 不仅仅是 format artifact——Table in Appendix 的 error taxonomy 显示 RE missed rates 保持 flat (10–16%) 是一个跨 BCS bin 的系统性 pattern（ρ=0.954 for IntraSub, flat for Missed），而 NER 的 missed rates 是 43–65% 且 non-monotonic。这种 task-level 对比即使考虑 format 差异也是有信息量的。建议在 abstract 中加入 "possibly reflecting its closed-set format" 即可。

---

### W6 [minor] — 不同 dataset 用不同 embedding，缺 cross-embedding ablation

**[AGREE]**

同意这是一个有效关切。Table 1 显示 Few-NERD 用 Qwen3 embedding，FewRel 和 MAVEN 用 MiniLM，但论文没有系统解释选择依据，也没有跨 embedding 的 sensitivity 分析。

唯一的 cross-embedding 数据出现在 Appendix §C（residualized BCS, Table），其中 MAVEN 在 MiniLM 和 Qwen3 两种 embedding 下都做了 partial correlation，结果方向一致（raw positive → controlled non-significant）。但 Few-NERD 的 pairwise 分析（Table 2）只报了 Qwen3，FewRel 的 BCS-controlled 实验只用了 MiniLM。至少应补充 Few-NERD+MiniLM 和 FewRel+Qwen3 的 sensitivity check，或在 Limitations 中明确说明为何没做。

---

## Questions 逐条回应

### Q1 — SCS/BCS actionable threshold?

**[AGREE]**

这是一个实际且重要的缺口。§practical\_magnitude 报告了 typical gap 的 empirical 分布（IQR=0.054 → 2.2pp），但没有给出 practitioners 可操作的 BCS 阈值。论文定位 SCS/BCS 为 "actionable for schema design"，但如果不能说 "BCS 超过 X 时应该考虑 schema 分拆"，这个 actionability claim 就是空的。建议在 Discussion 中基于 regression slope 给出一个参考阈值区间（例如：BCS > 0.7 时 expected accuracy loss > 5pp）。

---

### Q2 — Pairwise r² → batch-level gap 的放大机制?

**[AGREE]**

论文提供了 empirical 证据（§practical\_magnitude: pairwise r²=1.3–1.7%, batch quartile Δ=7.4pp, extreme Δ=31.2pp）但没有 formal 的数学推导。直觉上，batch BCS 是 O(k²) 个 pairwise SCS 的均值，高 BCS batch 意味着**所有**共现 type pair 都 confusable，而非单个 pair——这是 additive accumulation 而非 nonlinear 放大。但论文没有形式化这一点。

一个简单的 sanity check：如果 batch 内每个 confusable pair 独立贡献一个 substitution error，则总 confusion 应与 batch 内高-SCS pair 数量成正比——即 additive。Table (Appendix) 的 IntraSub rates 随 BCS bin 单调上升但未加速（0% → 1.6% → 10.6% → 49.4% for NER），看起来更像 super-linear（可能因为高 BCS bin 内 pair-level SCS 也更高，不仅仅是 pair 数量多）。这个问题值得在 Discussion 中用 1–2 句形式化。

---

### Q3 — MAVEN count-curve 反转的主因?

**[AGREE]**

§4.1 给出了三个归因（relaxed matching / same-domain context / class imbalance），§4.5 提供了 centrality confound 分析，但没有量化各因素的相对贡献。例如，可以通过将 relaxed matching 切换为 exact matching 来隔离因素 (i)，或通过 frequency-stratified 分析隔离因素 (iii)。当前的归因是 post-hoc 的、未分解的，与论文在 NER/RE 上追求的 controlled analysis 标准不一致。这是一个合理的弱点，虽然 MAVEN 不是论文的核心 focus。

---

### Q4 — 51% floor vs random-chance baseline?

**[REBUT]**

这个问题的答案可以从论文中推导。BCS-controlled 实验在 count=8 的 batch 上评估（Table 3: "80-rel, count 8"），random-chance baseline 是 1/8 = 12.5%。51% 远高于 random chance（4.1×），所以这不是 "model 在 guess"。

更有趣的解读是：高 BCS batch 中最 confusable 的 type pair 可能将 8-way classification 有效退化为若干 binary confusions。如果 top-2 confusable types 各占约一半的错误，51% 可以理解为 "除了最 confusable pair 之外的 types 基本正确，但最 confusable pair 上接近 coin-flip"。论文在 Discussion 中已经将此标注为 "task-inherent difficulty floor" 且 "broader model coverage is needed to confirm this hypothesis"（discussion.tex §6）。

建议论文在 Table 3 caption 或 §4.3 正文中明确报告 random-chance baseline 数字以消除读者疑虑，但这不构成 methodology 问题。

---

## 总结

| 条目 | 判断 | 核心理由 |
|------|------|----------|
| W1 | REBUT（部分同意） | Abstract 已改用 −7.4pp 为主数字，但 pairwise r² 可更显式 |
| W2 | AGREE | 核心证据不应全在 appendix |
| W3 | AGREE | §5 篇幅与 contribution 地位不匹配 |
| W4 | AGREE | "generally" 承载过多，MAVEN 反转应显式 |
| W5 | REBUT（部分同意） | Error taxonomy 提供了超越 format artifact 的证据，但 abstract 确需 caveat |
| W6 | AGREE | 缺 cross-embedding sensitivity check |
| Q1 | AGREE | 缺 actionable threshold |
| Q2 | AGREE | 缺 formal amplification mechanism |
| Q3 | AGREE | MAVEN 归因未量化分解 |
| Q4 | REBUT | 51% >> random chance (12.5%)，可从论文推导 |

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1"
}
```

</details>

---


## Round 7

## Round 7

38 recorded events


### User

_source line 225 · 2026-05-16T09:05:42.027483+00:00_

[Round 1 审稿请求]:
你是 Reviewer 1，负责审查 **方法严谨性 + 实验设计 + 统计分析**。

## 投稿信息
- **Venue**: EMNLP 2026 Main Conference (ACL Rolling Review, May cycle)
- **Deadline**: 2026-05-25
- **页数限制**: 正文 8 页（不含参考文献和附录）
- **模板**: ACL style files (`\usepackage[review]{acl}`)
- **匿名规则**: Double-blind（无匿名期要求，但论文中不得出现作者身份信息）
- **论文路径**: `projects/schema-dag-extraction/docs/paper/main.tex`（含 `\input` 的所有子文件）

## 你的审查侧重

1. **SCS/BCS 度量的合理性**：embedding cosine similarity 作为 confusability proxy 的理论依据是否充分？Qwen3 vs MiniLM 两种 embedding 的选择是否引入系统偏差？BCS 的 mean 聚合是否优于 max（Appendix E 有对比）？

2. **因果推断逻辑**：
   - BCS-controlled 实验声称是 "quasi-experimental"，但未控制 type frequency、definition quality 等 confounders——这是否削弱了因果声称？
   - 论文中是否存在超出实验设计支撑的因果语言（如 "drives"、"interventional"）？
   - Within-pool 分析（Table 5）是否充分控制了 pool composition confound？

3. **统计检验充分性**：
   - Pairwise r²=1.3-1.7% → batch-level 31.2pp 的放大是否有数学解释（不仅仅是 empirical observation）？
   - 80-rel 全量回归不显著（Table 5 第三行 p=0.762）但 extreme batches 做 headline result——是否有 cherry-picking 风险？
   - Bootstrap CI 方法是否恰当？非独立观测（pairwise data）的处理是否正确？
   - v2 prompt 下 RE BCS gap 从 31.2pp 缩至多少？Appendix F 提到 7.9pp (n=5) 和 25.5pp (n=25)——哪个更可信？

4. **跨数据集/跨模型泛化性**：
   - 仅 Qwen3-32B + Llama-3.1-8B 两个模型是否足够？
   - MAVEN 反转的解释（centrality confound）是否充分？
   - DocRED 的 R²=0.53 vs FewRel R²=0.218——差异原因是否解释清楚？

5. **SDGD 负面结果**：
   - Merge amplification 的分析是否足够深入？
   - RE batch composition +1.4pp (p≈0.19) 是否有实际意义？
   - §5 篇幅是否足够（当前约 200 词正文 + Appendix B）？

请按 EMNLP 标准给出完整审稿意见：Summary → Strengths → Weaknesses → Questions → Missing References → Overall Assessment（strong reject / weak reject / borderline / weak accept / strong accept + 置信度 1-5）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 226 · 2026-05-16T09:05:51.847032+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebSearch,mcp__agent-ml-research__pdf_to_images",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebSearch,mcp__agent-ml-research__pdf_to_images",
    "max_results": "2"
  }
}
```

</details>

---


### Tool result

_source line 227 · 2026-05-16T09:05:51.847498+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 228 · 2026-05-16T09:05:55.064026+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review 2026 reviewer guidelines review form criteria"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review 2026 reviewer guidelines review form criteria"
  }
}
```

</details>

---


### Tool call

_source line 229 · 2026-05-16T09:05:56.270223+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/docs/paper/**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/docs/paper/**/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction"
  }
}
```

</details>

---


### Tool result

_source line 230 · 2026-05-16T09:05:56.320867+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/prompt_appendix.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/checklist.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/discussion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/experimental_setup.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/sdgd_negative.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 231 · 2026-05-16T09:06:03.868629+00:00_

Web search results for query: "ACL Rolling Review 2026 reviewer guidelines review form criteria"

Links: [{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"ACL Rolling Review | ACL Member Portal","url":"https://www.aclweb.org/portal/content/acl-rolling-review"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"}]

I've successfully retrieved information about ACL Rolling Review 2026 reviewer guidelines, review form criteria, and more. Here's a summary of the key information found:

## Reviewer Guidelines

The reviewing workflow involves reading the paper and getting the first impression,
…[truncated 1902 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 8804
}
```

</details>

---


### Tool call

_source line 232 · 2026-05-16T09:06:11.757188+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebFetch",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebFetch",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 233 · 2026-05-16T09:06:11.757619+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 234 · 2026-05-16T09:06:12.159497+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 235 · 2026-05-16T09:06:12.210498+00:00_

1	\documentclass[11pt]{article}
2	
3	\usepackage[review]{acl}
4	
5	\usepackage{times}
6	\usepackage{latexsym}
7	\usepackage[T1]{fontenc}
8	\usepackage[utf8]{inputenc}
9	\usepackage{microtype}
10	\usepackage{graphicx}
11	\usepackage{booktabs}
12	\usepackage{amsmath}
13	\usepackage{enumitem}
14	\usepackage[normalem]{ulem}
15	
16	\title{Does Type Confusability Drive Schema-Induced Degradation\\in Training-Free LLM Information Extraction?}
17	
18	\author{Anonymous}
19	
20	\begin{document}
21	\maketitle
22	
23	\input{abstract}
24	
25	\input{introduction}
26	
27	\input{related_work}
28	
29	\input{experimental_setup}
30	
31	\input{results}
32	
33	\input{sdgd_negative}
34	
35	\input{discussion}
36	
37	\section*{Limitations}
38	\begin{enumerate}[leftmargin=*,itemsep=2pt]
39	\item \textbf{Model coverage.} Primary experiments use Qwen3-32B with cross-model validation on Llama-3.1-8B-Instruct. Whether patterns hold for proprietary models (GPT-4, Gemini) remains unverified. Channel~2 was not robustly detectable on NER at 8B scale, likely due to floor effects.
40	
41	\item \textbf{Modest pairwise effect size.} Pairwise SCS explains 1.3--1.7\% of type confusion variance; entity frequency, prompt position, mention ambiguity, and type definition quality likely account for the remainder.
42	
43	\item \textbf{Non-significant factorial test.} Within-dataset count $\times$ BCS interaction on Few-NERD did not reach significance (Appendix~\ref{sec:appendix_factorial}); cross-pool slope consistency suggests confusability sensitivity is stable rather than amplifying.
44	
45	\item \textbf{Decomposition and metric scope.} RE batch composition is tested on FewRel only; NER merge alternatives remain unexplored. SCS relies on embedding cosine similarity; label entropy or ontological depth may capture complementary dimensions.
46	
47	\item \textbf{RE format specificity.} RE's clean channel separation may reflect its closed-set classification format. FewRel combines training and validation splits 
…[truncated 18346 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 236 · 2026-05-16T09:06:24.546884+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "http://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete review form with all scoring dimensions, their scales (numeric ranges), and descriptions. I need the exact criteria names, score ranges, and what each score level means."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "http://aclrollingreview.org/reviewform",
    "prompt": "Extract the complete review form with all scoring dimensions, their scales (numeric ranges), and descriptions. I need the exact criteria names, score ranges, and what each score level means."
  }
}
```

</details>

---


### Tool call

_source line 237 · 2026-05-16T09:06:26.354638+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 238 · 2026-05-16T09:06:26.806942+00:00_

1	\begin{abstract}
2	Training-free LLM information extraction---prompting models with target schemas without fine-tuning---degrades sharply as schema complexity grows: NER recall drops from 0.72 to 0.42 with 64 candidate types, and RE accuracy falls from 85.7\% to 50.4\% with 80 relations (sentence-level) and from 88.0\% to 38.7\% with 96 relations (document-level). Prior work conflates type count with type confusability, leaving the mechanisms unclear. We conduct the first controlled empirical study isolating these factors across three IE tasks and four datasets, introducing the Schema Confusability Score (SCS) and two experimental paradigms: count curves that vary schema size while randomizing confusability, and BCS-controlled experiments that fix size while varying confusability. Our experiments reveal two degradation channels: a count channel that suppresses recall in NER and RE, but reverses direction in MAVEN (168 event types) due to centrality confounds in same-domain schemas as candidate types increase, and a confusability channel where semantically similar types trigger intra-batch substitution errors---cleanly separable in RE (a closed-set classification task); in NER, confusability additionally impairs entity detection. The BCS--accuracy relationship is robust across schema sizes and prompt designs: the regression slope is consistent between independent 16-type and within-pool 80-type evaluations (permutation $p = 0.60$), with the quartile gap reaching $-$5.3\,pp (95\% CI: [$-$7.4, $-$3.2]), though pairwise effect sizes are modest ($r^2 = 1.3\text{--}1.7\%$) on the independent 16-relation pool. On MAVEN's same-domain schema (168 event types), per-type confusability reverses direction due to a centrality confound, though pairwise confusability remains significant. Both channels replicate on Llama-3.1-8B (count $r = 0.725$; confusability $\Delta = -27$\,pp), with high-BCS accuracy converging to a floor consistent across both tested models. Our confusability
…[truncated 344 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 239 · 2026-05-16T09:06:26.807473+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 240 · 2026-05-16T09:06:27.058751+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	Training-free LLM information extraction---prompting a large language model with a target schema and asking it to extract structured information without any task-specific fine-tuning---enables rapid deployment across new domains and ontologies. This zero-shot paradigm eliminates the need for labeled data, making it attractive for applications where annotation is expensive or schemas evolve frequently \cite{llm4ie-survey-2024}. Yet the paradigm carries a critical limitation: performance degrades sharply as the number of candidate types in the prompt schema grows. On named entity recognition, recall drops from 0.72 with a single candidate type to 0.42 with 64 types, a 42\% relative decline. On relation extraction, accuracy falls from 85.7\% with one relation to 50.4\% with 80 relations (sentence-level) and from 88.0\% to 38.7\% with 96 relations (document-level)---near or exceeding halving. This degradation is not academic: real-world ontologies routinely define 50--200+ types, placing them squarely in the regime where training-free extraction becomes unreliable.
5	
6	What causes this degradation? Prior decomposition strategies implicitly assume different answers: \citet{uniner-2024} extract each type independently; \citet{llm-pee-2025} partition schemas by type embedding similarity; \citet{parse-2025} optimize schema definitions. None isolates \emph{why} schemas degrade performance. The closest work, LLM-PEE, reduces both the number of co-presented types and their inter-type similarity simultaneously, making it impossible to determine which factor accounts for the gains. All prior approaches conflate two mechanisms: having more types to discriminate among (count) and having semantically similar types to confuse (confusability). Without disentangling these, decomposition strategies optimize a black-box objective without understanding its components.
7	
8	We ask three questions. \textbf{RQ1}: Does type confusabil
…[truncated 2602 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 251
}
```

</details>

---


### Tool call

_source line 241 · 2026-05-16T09:06:27.109493+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/experimental_setup.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/experimental_setup.tex"
  }
}
```

</details>

---


### Tool result

_source line 242 · 2026-05-16T09:06:27.160193+00:00_

1	\section{Experimental Setup}
2	\label{sec:experimental_setup}
3	
4	We evaluate how prompt schema size and inter-type confusability affect zero-shot LLM extraction across three information extraction tasks and four datasets: named entity recognition (NER), sentence-level relation extraction (RE), document-level RE, and event detection (ED).
5	
6	\subsection{Tasks and Datasets}
7	\label{sec:datasets}
8	
9	\paragraph{Few-NERD (NER).}
10	Few-NERD \cite{fewnerd-2021} provides 66 fine-grained entity types organized into 8 coarse categories (person, location, organization, building, art, product, event, other). The dataset spans diverse domains, making it suitable for cross-domain evaluation. We sample 1{,}000 test instances and evaluate with token-level text matching.
11	
12	\paragraph{FewRel (RE).}
13	FewRel \cite{fewrel-2018} contains 80 relation types sourced from Wikidata. Since the validation split covers only 16 relations, we combine the training and validation splits to obtain the full 80-relation pool required for schema-scale experiments, and sample 1{,}000 balanced instances (12--13 per relation type, stratified to ensure equal representation). Each instance provides a sentence with marked head and tail entities; the task is to classify the relation.
14	
15	\paragraph{DocRED (Document-level RE).}
16	DocRED \cite{docred-2019} contains 96 relation types sourced from Wikidata, evaluated at the document level where entity pairs may span multiple sentences. We sample balanced instances and formulate the task identically to FewRel: given a document with marked head and tail entities, classify the relation. DocRED extends the RE evaluation to a larger schema (96 vs.\ 80 types) and document-level context, testing whether confusability effects persist under longer input contexts and cross-sentence reasoning.
17	
18	\paragraph{MAVEN (ED).}
19	MAVEN \cite{maven-2020} defines 168 event types derived from the FrameNet ontology, making it a same-domain schema. We use the va
…[truncated 4995 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 243 · 2026-05-16T09:06:32.386605+00:00_

# ACL Rolling Review Form - Scoring Dimensions

## 1. Reviewer Confidence
**Scale:** 1-5
- **5:** "Positive that my evaluation is correct. I read the paper very carefully"
- **4:** "Quite sure. I tried to check the important points carefully"
- **3:** "Pretty sure, but there's a chance I missed something"
- **2:** "Willing to defend my evaluation, but it is fairly likely that I missed some details"
- **1:** "Not my area, or paper is very hard to understand"

## 2. Soundness
**Scale:** 1-5 (with .5 increments)
- **5:** "Excellent: This study is one of the most thorough I have seen"
- **4:** "Strong: This study provides sufficient support for all its claims"
- **3:** "Acceptable: This study provides sufficient support for main claims"
- **2:** "Poor: Some of the main claims are not sufficiently supported"
- **1:** "Major Issues: This study is not yet sufficiently thorough to warrant publication"

## 3. Excitement
**Scale:** 1-5 (with .5 increments)
- **5:** "Highly Exciting: I would recommend this paper to others"
- **4:** "Exciting: I would mention this paper to others"
- **3:** "Interesting: I might mention some points of this paper"
- **2:** "Potentially Interesting: this paper does not resonate with me"
- **1:** "Not Exciting: does not resonate with me, and I don't think it would with others"

## 4. Overall Assessment
**Scale:** 1-5 (with .5 increments)
- **5:** "Consider for Award: up to top 2.5% papers"
- **4:** "Conference: could be accepted"
- **3:** "Findings: could be accepted to the Findings of the ACL"
- **2:** "Resubmit next cycle: needs substantial revisions"
- **1:** "Do not resubmit: fully redone or not relevant"

## 5. Reproducibility
**Scale:** 1-5
- **5:** "They could easily reproduce the results"
- **4:** "They could mostly reproduce the results"
- **3:** "They could reproduce with some difficulty"
- **2:** "They would be hard pressed to reproduce"
- **1:** "They would not be able to reproduce"

## 6. Datasets & Software Value
**Scale:** 1-5 (ident
…[truncated 597 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 7839
}
```

</details>

---


### Tool call

_source line 244 · 2026-05-16T09:06:36.805137+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex"
  }
}
```

</details>

---


### Tool result

_source line 245 · 2026-05-16T09:06:37.258085+00:00_

1	\section{Results}
2	\label{sec:results}
3	
4	Unless otherwise noted, all experiments in this section use the v1 prompt (\S\ref{sec:model}; full templates in Appendix~\ref{sec:appendix_prompts}).
5	
6	\subsection{Count-Degradation Curves}
7	\label{sec:count_curves}
8	
9	\begin{figure}[t]
10	\centering
11	\begin{minipage}[t]{0.48\columnwidth}
12	\centering
13	\includegraphics[width=\linewidth]{../../figures/paper/fig_count_curves.pdf}
14	\end{minipage}
15	\hfill
16	\begin{minipage}[t]{0.48\columnwidth}
17	\centering
18	\includegraphics[width=\linewidth]{../../figures/paper/fig_bcs_scaling.pdf}
19	\end{minipage}
20	\caption{\textbf{(a)} Count-degradation curves across four datasets. NER recall generally declines and RE accuracy (both FewRel and DocRED) declines monotonically with schema size; MAVEN relaxed F1 increases (\S\ref{sec:centrality_confound}). \textbf{(b)} BCS-controlled FewRel accuracy. The BCS--accuracy slope is consistent across the independent 16-relation pool and within-pool 16-relation subsets (permutation $p = 0.60$); the wider BCS range available at 80 relations produces larger absolute gaps.}
21	\label{fig:main_results}
22	\end{figure}
23	
24	We first examine how extraction performance changes as the number of types in the prompt schema increases (Experiment~1; Figure~\ref{fig:main_results}a).
25	
26	\paragraph{NER (Few-NERD).}
27	Recall declines from 0.72 at count${}\,=\,1$ to 0.42 at count${}\,=\,64$ ($-$42\% relative), with minor non-monotonicity within sampling variability (bootstrap CIs overlap). Precision rises inversely (0.11 $\to$ 0.52), reflecting a shift from over-prediction to under-prediction as candidate types increase.
28	
29	\paragraph{RE (FewRel).}
30	Accuracy drops monotonically from 85.7\% at count${}\,=\,1$ through 58.8\% at count${}\,=\,40$ to 50.4\% at count${}\,=\,80$, a near-halving when the model must discriminate among all 80 relation types simultaneously. (The count${}\,=\,40$ evaluation uses 40-relation subsets sampled fr
…[truncated 12428 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 246 · 2026-05-16T09:06:37.258466+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/sdgd_negative.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/sdgd_negative.tex"
  }
}
```

</details>

---


### Tool result

_source line 247 · 2026-05-16T09:06:37.761246+00:00_

1	\section{Schema Decomposition: Failure, Diagnosis, and Mitigation}
2	\label{sec:sdgd}
3	
4	A natural intervention is to partition the schema so confusable types never co-occur. We test this with \textbf{Schema-DAG-Guided Decomposition} (SDGD), which uses greedy graph coloring on the pairwise SCS graph to assign types to low-confusability batches, merging predictions via set union. Every decomposition mode---SDGD (F1\,=\,0.241), random batching (0.320), per-type (0.292)---falls below the single-pass baseline (0.445) on Few-NERD NER (Table~\ref{tab:sdgd_results}).
5	
6	\paragraph{Merge amplification as the bottleneck.}
7	The failure is \emph{merge amplification}: presenting the same text $k$ times causes each pass to independently generate predictions. Single-pass precision (0.563) collapses to 0.210--0.249 after union merge with 8 batches, while recall gains are modest (0.368 $\to$ 0.314--0.446). Confidence gating improves precision but with disproportionate recall loss (Appendix~\ref{sec:appendix_sdgd}). The fundamental issue is that LLM predictions are not calibrated across passes \cite{llm-calibration-survey-2024}.
8	
9	\paragraph{Why NER fails but RE does not.}
10	Merge amplification is specific to span-level tasks: each NER pass independently proposes entity spans, and union merge must resolve conflicting boundaries and type assignments, degrading systematically with pass count. RE operates on fixed (head, tail) pairs with no span reconciliation---each pair receives an independent classification, eliminating the mechanism that caused SDGD to fail.
11	
12	\paragraph{Confusability-aware batch composition for RE.}
13	Since RE avoids merge amplification, we test whether confusability-aware batching improves accuracy. All decomposition conditions use oracle routing (each instance is routed to the batch containing its gold type). Single-type batches versus the 80-relation single-pass yields +29.8\,pp (0.802 vs.\ 0.504), confirming that decomposition is effective whe
…[truncated 415 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 248 · 2026-05-16T09:06:37.761736+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 249 · 2026-05-16T09:06:37.812341+00:00_

1	\section{Discussion}
2	\label{sec:discussion}
3	
4	\paragraph{Boundary conditions.}
5	The two-channel model applies cleanly to cross-domain schemas; same-domain schemas require pairwise SCS or centrality adjustment (\S\ref{sec:centrality_confound}). High-BCS accuracy converges to $\approx$51\% across tested models, suggesting a task-inherent difficulty ceiling. RE's clean channel separation may partly reflect its closed-set format; the effect generalizes to document-level RE (DocRED slope $-$0.71). Practitioners should monitor BCS and prefer cross-domain type groupings. Prompt design modulates but does not eliminate the effect (v2 gap: $-$25.5\,pp vs.\ v1: $-$31.2\,pp; Appendix~\ref{sec:appendix_prompt_sensitivity}).
6	
7	\paragraph{Future directions.}
8	For NER, merge amplification blocks naive decomposition (\S\ref{sec:sdgd}); calibration-aware merge, joint decoding, or coarse-to-fine extraction may address this. For RE, extending confusability-aware batching to broader benchmarks is a natural next step.
9	
10	\section{Conclusion}
11	\label{sec:conclusion}
12	
13	We isolated schema-induced degradation into count-driven recall decline and confusability-driven type confusion, showed these channels are separable in RE, with Channel~2 additionally impairing entity detection in NER, and confirmed that both channels replicate across model families on RE (Meta-Llama-3.1-8B-Instruct: count $r = 0.725$, confusability $\Delta = -27$\,pp) and across extraction granularities (DocRED document-level RE: count decline $-$49\,pp; BCS slope $= -0.71$, $R^2 = 0.53$), with high-BCS accuracy converging to a floor consistent across both tested models. We further identified a centrality confound on same-domain schemas, demonstrated that merge amplification is a structural challenge for NER decomposition, and showed that confusability-aware batch composition recovers +1.4\,pp on RE where span reconciliation is unnecessary. Cross-batch calibration or joint decoding for NER, and broader
…[truncated 64 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 250 · 2026-05-16T09:06:42.636743+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 251 · 2026-05-16T09:06:42.888144+00:00_

1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{Training-free LLM IE.}
5	Training-free LLM IE spans instruction tuning \cite{instructuie-2023}, code-style schema encoding \cite{knowcoder-2024,codeie-2023}, annotation-guided extraction \cite{gollie-2024,adelie-2024}, schema-driven decoding \cite{slot-2025,oneke-2025}, and constrained JSON decoding \cite{json-schema-bench-2025}. For NER, methods include zero-shot decomposition \cite{xie-zeroshot-ner-2023,promptner-2023}, distillation \cite{uniner-2024}, and bidirectional encoders \cite{gliner-2024,gliner2-2025}. These methods perform well with moderate schemas (4--20 types) but none investigates how performance degrades as schema complexity scales, nor proposes quantitative metrics for inter-type confusability.
6	
7	\paragraph{Schema complexity in IE.}
8	The most directly related work is LLM-PEE \cite{llm-pee-2025}, which partitions large event schemas by type embedding similarity. Our work differs in three ways: (1)~we conduct controlled analysis to understand \emph{why} extraction degrades rather than developing an engineering solution; (2)~our BCS-controlled experiments isolate count from confusability, which LLM-PEE conflates; (3)~our SDGD experiments reveal that merge amplification---not partitioning quality---is the bottleneck in decompose-then-merge pipelines. Other approaches address schema complexity via hard negative mining \cite{iepile-2024}, schema definition optimization \cite{parse-2025}, multi-agent debate \cite{crossagentie-2025,cmas-ner-2025}, and active prompting \cite{reflect-learn-2026}; all treat it as an engineering problem rather than isolating the underlying degradation mechanisms.
9	
10	\paragraph{Embedding anisotropy.}
11	Our centrality confound (\S\ref{sec:centrality_confound}) connects to representation degeneration: embeddings collapse into narrow cones \cite{gao-repr-degen-2019,ethayarajh-contextual-2019}, but local clusters can be isotropic \cite{cai-isotropy-clusters
…[truncated 101 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 251
}
```

</details>

---


### Tool call

_source line 252 · 2026-05-16T09:06:42.888629+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/checklist.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/checklist.tex"
  }
}
```

</details>

---


### Tool result

_source line 253 · 2026-05-16T09:06:42.939234+00:00_

1	\section*{Responsible NLP Research Checklist}
2	
3	For each question, the answer is \textbf{Yes}, \textbf{No}, or \textbf{N/A}. If Yes, the relevant section is indicated. If No, a justification is provided.
4	
5	\subsection*{A \quad For Every Submission}
6	
7	\begin{enumerate}[label=\textbf{A\arabic*.},leftmargin=*,itemsep=4pt]
8	
9	\item \textbf{Did you describe the limitations of your work?}
10	
11	Yes. The Limitations section (after \S\ref{sec:conclusion}) discusses single-model reliance, modest pairwise effect sizes, cross-pool slope consistency, non-significant factorial results, decomposition scope, and metric scope.
12	
13	\item \textbf{Did you discuss any potential risks of your work?}
14	
15	N/A. This is a purely analytical study of schema-induced degradation in existing LLM IE systems. It does not introduce new models, datasets, or deployment-facing artifacts. The findings characterize failure modes and are intended to inform safer schema design.
16	
17	\item \textbf{Do the abstract and introduction summarize the paper's main claims?}
18	
19	Yes. The abstract and \S\ref{sec:introduction} state the two-channel degradation pattern (count and confusability), the cross-model replication, and the negative SDGD result.
20	
21	\item \textbf{Did you use AI assistants (e.g., ChatGPT, Copilot) when working on this paper?}
22	
23	Yes. An AI coding assistant was used for experiment scripting and LaTeX formatting. All scientific claims, experimental design, and analysis were conducted by the authors.
24	
25	\end{enumerate}
26	
27	\subsection*{B \quad Scientific Artifacts}
28	
29	\begin{enumerate}[label=\textbf{B\arabic*.},leftmargin=*,itemsep=4pt]
30	
31	\item \textbf{Did you cite the creators of artifacts you used?}
32	
33	Yes. Few-NERD \cite{fewnerd-2021}, FewRel \cite{fewrel-2018}, MAVEN \cite{maven-2020}, Qwen3-32B \cite{qwen3-2025}, Meta-Llama-3.1-8B-Instruct, vLLM \cite{vllm-2023}, and all-MiniLM-L6-v2 \cite{minilm-2020} are cited in \S\ref{sec:datasets} and \S
…[truncated 4366 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 254 · 2026-05-16T09:06:45.987657+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/prompt_appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/prompt_appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 255 · 2026-05-16T09:06:46.038596+00:00_

1	\section{Prompt Templates}
2	\label{sec:appendix_prompts}
3	
4	This appendix reproduces the complete prompt templates used for all three extraction tasks.
5	All prompts are injected into a single \texttt{user} message (no system prompt); the model's chat template adds the system/assistant framing.
6	Both versions provide a JSON-formatted type schema to the vLLM constrained-decoding engine; the schema is \emph{not} included in the natural-language prompt itself.
7	We use greedy decoding (\texttt{temperature=0}, \texttt{seed=42}) throughout.
8	
9	\medskip\noindent
10	\textbf{Notation.}
11	Placeholders are shown in \texttt{\{braces\}}.
12	Text \textbf{added in v2} (relative to v1) is marked with $\triangleright$.
13	Text \textbf{removed in v2} is marked with \sout{strikethrough}.
14	
15	\subsection{Named Entity Recognition (Few-NERD)}
16	
17	\paragraph{v1 prompt (with character offsets).}
18	
19	\begin{small}
20	\begin{verbatim}
21	Extract all named entities from the following text.
22	Only extract entities of the following types:
23	- {type_1}: {definition_1}
24	- {type_2}: {definition_2}
25	  ...
26	
27	Text: {input_text}
28	
29	Output as JSON: [{"text": "...", "type": "...",
30	                  "start": ..., "end": ...}]
31	\end{verbatim}
32	\end{small}
33	
34	\noindent
35	\textbf{v1 constrained-decoding schema:}
36	\begin{small}
37	\begin{verbatim}
38	{"type": "array",
39	 "items": {"type": "object",
40	   "properties": {
41	     "text":  {"type": "string"},
42	     "type":  {"type": "string",
43	               "enum": [&lt;sorted_types>]},
44	     "start": {"type": "integer"},
45	     "end":   {"type": "integer"}},
46	   "required": ["text","type","start","end"]}}
47	\end{verbatim}
48	\end{small}
49	
50	\paragraph{v2 prompt (text+type only).}
51	
52	\begin{small}
53	\begin{verbatim}
54	Extract all named entities from the following text.
55	Only extract entities of the following types:
56	- {type_1}: {definition_1}
57	- {type_2}: {definition_2}
58	  ...
59	
60	Text
…[truncated 5004 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 256 · 2026-05-16T09:07:37.553172+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "http://aclrollingreview.org/reviewform",
  "prompt": "Extract the exact scoring scales, descriptions for each level, and all review form fields. Include the soundness scale, excitement scale, overall assessment scale, and reproducibility scale with all level descriptions verbatim."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "http://aclrollingreview.org/reviewform",
    "prompt": "Extract the exact scoring scales, descriptions for each level, and all review form fields. Include the soundness scale, excitement scale, overall assessment scale, and reproducibility scale with all level descriptions verbatim."
  }
}
```

</details>

---


### Tool result

_source line 257 · 2026-05-16T09:07:42.427610+00:00_

# ACL Rolling Review Form: Scoring Scales & Fields

## Review Form Fields

The form contains these main sections:
- Paper Summary
- Summary of Strengths
- Summary of Weaknesses
- Comments/Suggestions/Typos
- Reviewer Confidence
- Soundness
- Excitement
- Overall Assessment
- Best Paper Justification
- Limitations and Societal Impact
- Ethical Concerns
- Needs Ethics Review
- Reproducibility
- Datasets
- Software
- Knowledge of Author Identity

## Reviewer Confidence Scale

"5 = Positive that my evaluation is correct" through "1 = Not my area, or paper is very hard to understand."

## Soundness Scale

- **5**: "Excellent: This study is one of the most thorough I have seen"
- **4**: "Strong: This study provides sufficient support for all claims"
- **3**: "Acceptable: This study provides sufficient support for main claims"
- **2**: "Poor: Some main claims not sufficiently supported"
- **1**: "Major Issues: not sufficiently thorough to warrant publication"

## Excitement Scale

- **5**: "Highly Exciting: I would recommend this paper to others"
- **4**: "Exciting: I would mention this paper to others"
- **3**: "Interesting: I might mention some points"
- **2**: "Potentially Interesting: does not resonate with me"
- **1**: "Not Exciting: does not resonate with me"

## Overall Assessment Scale

- **5**: Consider for Award
- **4**: Conference acceptance
- **3**: Findings acceptance
- **2**: Resubmit next cycle
- **1**: Do not resubmit

## Reproducibility Scale

Ranges from "5 = They could easily reproduce" to "1 = They would not be able to reproduce."

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 4874
}
```

</details>

---


### Tool call

_source line 258 · 2026-05-16T09:09:26.168138+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__review_reviewer_post_to_director",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__review_reviewer_post_to_director",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 259 · 2026-05-16T09:09:26.218910+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 260 · 2026-05-16T09:10:21.992772+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 1 — Round 1 审稿意见（方法严谨性 + 实验设计 + 统计分析）\n\n### 总体评分\n**Overall**: 3.0 / 5 (Findings)\n**Confidence**: 4/5\n**一句话总结**: 研究问题有价值、实验设计有创意，但核心效应量极小（pairwise r²<2%），因果声称超出证据支撑，统计呈现存在 cherry-picking 风险——目前更适合作为 Findings 论文。\n\n### 官方维度打分（ACL Rolling Review form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 2.5/5 | 核心因果声称（\"drive\"）缺乏充分支撑；headline 数字（31.2pp）来自极端构造而非典型场景；多处非显著结果被以\"directionally consistent\"解读 |\n| Excitement | 3.5/5 | 首次系统隔离 count vs confusability 两通道，BCS-controlled 设计有方法论贡献，centrality confound 发现有启发性 |\n| Reproducibility | 4/5 | 提供了详细 prompt 模板、decoding 参数、数据集描述、bootstrap 参数；code upon acceptance |\n\n---\n\n### Must-Fix 问题（影响接收决定）\n\n**N1** [critical] **因果语言超出证据支撑**\n- 具体位置：Title (\"Does Type Confusability **Drive** Schema-Induced Degradation\")、§1 RQ1、§4.3 (\"quasi-experimental evidence\")\n- 问题：BCS-controlled 实验声称是 \"quasi-experimental\"，但未控制关键 confounders：(a) type frequency in pretraining corpus（高 BCS 的相似 types 可能本身就是低频/罕见 types）；(b) type definition quality/length（相似 types 的 definitions 本身可能更相似，导致 LLM 混淆来自 prompt 信息不足而非 embedding space overlap）；(c) prompt position effects。Without controlling these, the study establishes **correlation** not **causation**。\n- 为什么影响接收：Title 和 RQ framing 暗示因果关系，但证据链只到相关性。如果真正的 driver 是 definition quality 或 type frequency 而非 embedding similarity 本身，整个 \"confusability\" narrative 的解释力被严重削弱。\n- 建议：(1) 将 title 改为描述性表述；(2) 明确声明 BCS-controlled 实验控制了什么、没控制什么；(3) 至少对 type frequency 进行 partial correlation 控制。\n\n**N2** [critical] **Pairwise → batch-level 效应放大缺乏数学解释**\n- 具体位置：§4.2 Table 2 (r²=1.3-1.7%) → §4.3 Table 3 (31.2pp gap)\n- 问题：Pairwise SCS 解释 type confusion variance 仅 1.3-1.7%，但论文声称这 \"compounds\" 到 batch level 产生 31.2pp gap。这一放大没有形式化的数学解释——是线性叠加（120 pairs × small effect）、还是非线性交互？更重要的是，§4.3 \"Practical magnitude\" 承认 typical batch gap 仅 2.2pp (CI: [0.4, 4.0])，即 IQR 范围内的真实效应不到 headline 的 7%。\n- 为什么影响接收：无法解释为什么 1.7% variance → 31.2pp gap（且典型场景仅 2.2pp），读者无法判断 BCS 是否有实际工程价值。31.2pp 放在 abstract 和 Table 3 作为 headline result 有误导性。\n- 建议：(1) 提供从 pairwise r² 到 batch-level gap 的数学推导；(2) 在 abstract/Results 突出 typical-batch gap（2-4pp）而非 extreme-batch gap；(3) 明确 31.2pp 是 BCS range maximized 的构造结果。\n\n**N3** [critical] **Full 80-rel 回归不显著但极端 batch 作为 headline——cherry-picking 风险**\n- 具体位置：Table 5 第三行 (full 80-rel, n=25, slope=+0.221, p=0.762)\n- 问题：使用 full 80-rel pool 的 25 个 random batches 做回归时，BCS-accuracy 关系**完全不显著**（p=0.762，slope 甚至为正）。论文注释 \"BCS range insufficient\" 作为解释，但这等于承认：在自然采样条件下，BCS 对 accuracy 没有可检测的预测力。然而 Table 3 的 31.2pp 极端 batch 比较仍是论文的核心 evidence。\n- 为什么影响接收：呈现方式 (burying the null in a footnote while headlining the extreme result) 削弱 credibility。一个 reviewer 的直觉读法：\"在 natural conditions 下找不到效应，于是构造了极端条件来展示效应\"。\n- 建议：(1) Table 5 的 80-rel null result 应与 extreme-batch result 并列讨论；(2) 论述 \"effect detectable only with sufficient BCS range\" 不等于 \"effect practically important\"。\n\n---\n\n### Should-Fix 问题\n\n**W1** [warning] **Bootstrap CI 对非独立观测可能 anti-conservative**\n- 具体位置：§4.2 Table 2 (pair-level percentile bootstrap)\n- 问题：Pairwise confusion rates 不独立——共享 type 的 pairs 在统计上相关。论文提到 \"type-level cluster bootstrap yields wider CIs\" 但仅 parenthetical 一笔带过，primary CIs 仍是 pair-level。\n- 建议：将 cluster bootstrap 作为 primary CI 报告。\n\n**W2** [warning] **Embedding 选择不一致且缺乏理论驱动**\n- 具体位置：§3.2, Table 1 (Qwen3 for Few-NERD, MiniLM for FewRel/DocRED/MAVEN)\n- 问题：如果 SCS 理论基础是 \"LLM representation space 中的 overlap 导致 confusion\"，应统一用 LLM 自身 embedding。用 MiniLM 计算 RE confusability 缺乏 first-principles justification，且未解释为何不同 task 用不同 embedding。\n- 建议：在所有 dataset 上报告两种 embedding 的 SCS-confusion 对比。\n\n**W3** [warning] **RE batch composition +1.4pp (p≈0.19) 不具统计/实际意义**\n- 具体位置：§5, Appendix D Table 7\n- 问题：n=1 graph-coloring vs random, p≈0.19, BCS margin 仅 0.006。论文 framing \"directionally consistent application\" 过于积极。Abstract 中 \"succeeds for RE\" 的表述误导。\n- 建议：坦率承认是 null result；将 framing 从 \"succeeds\" 改为 \"provides suggestive but inconclusive evidence\"。\n\n**W4** [warning] **仅两个模型（32B+8B）的跨模型泛化过于薄弱**\n- 具体位置：Appendix A, §4.3 cross-model paragraph\n- 问题：规模差异大，architecture 不同，Channel 2 在 8B NER 上未复制。两模型不足以声称 \"cross-model replication\"。\n- 建议：下调泛化声称强度。\n\n**W5** [warning] **DocRED R²=0.53 vs FewRel R²=0.218 差异解释自相矛盾**\n- 具体位置：§4.3 Document-level RE paragraph\n- 问题：论文归因 \"wider confusability range\"，但 Table 1 显示 DocRED BCS range (0.53-0.73) 实际比 FewRel (0.42-0.97) 更窄。解释与数据矛盾。\n- 建议：检查并修正此说法。\n\n---\n\n### 小问题\n\n- SCS 仅基于 type name 计算，但 prompt 中提供了 definitions——如果 LLM 主要依据 definition 判断，SCS 可能 misrepresent 真实 confusability\n- Abstract 过长（~350 words），EMNLP 建议 150-250 words\n- Table 3 的 16-rel condition 无 CI，与其他条目不一致\n- §4.4 \"100% of confusion errors are intra-batch\" 是 RE classification format 的 tautology，非 evidence for confusability\n- Limitations #6 承认 \"correlational evidence\" 与正文 \"quasi-experimental\" framing 矛盾\n\n---\n\n### 主要优势\n\n- 首次系统隔离 schema degradation 的 count 和 confusability 维度，填补 training-free IE 文献 gap\n- BCS-controlled 设计（fix count, vary confusability）比 prior work 提供更强的控制\n- Centrality confound 诊断有方法论贡献，提醒社区 per-type aggregation 在 homogeneous schemas 上的陷阱\n- Honest about negative results（SDGD failure, RE batch composition non-significance）\n- Reproducibility 良好：prompt 模板完整、参数详尽\n\n---\n\n### Questions to Authors\n\n1. 能否提供从 pairwise r²≈1.5% 到 extreme-batch 31.2pp gap 的数学推导（即使是 order-of-magnitude estimation）？\n2. 为什么 FewRel 用 MiniLM 而 Few-NERD 用 Qwen3 embedding？有没有在 FewRel 上也用 Qwen3 的结果？\n3. Table 5 full 80-rel 回归 p=0.762——如果用 top/bottom 10 batches 单独回归，是否显著？\n4. BCS-controlled 实验中，high-BCS vs low-BCS batches 的平均 type frequency 是否有系统差异？\n\n---\n\n### Missing References\n\n- Li et al. (2023) \"Evaluating ChatGPT's Information Extraction Capabilities\"\n- Wadhwa et al. (2023) \"Revisiting Relation Extraction in the era of Large Language Models\"",
  "reviewer_id": "1",
  "project": "schema-dag-extraction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 1 — Round 1 审稿意见（方法严谨性 + 实验设计 + 统计分析）\n\n### 总体评分\n**Overall**: 3.0 / 5 (Findings)\n**Confidence**: 4/5\n**一句话总结**: 研究问题有价值、实验设计有创意，但核心效应量极小（pairwise r²<2%），因果声称超出证据支撑，统计呈现存在 cherry-picking 风险——目前更适合作为 Findings 论文。\n\n### 官方维度打分（ACL Rolling Review form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 2.5/5 | 核心因果声称（\"drive\"）缺乏充分支撑；headline 数字（31.2pp）来自极端构造而非典型场景；多处非显著结果被以\"directionally consistent\"解读 |\n| Excitement | 3.5/5 | 首次系统隔离 count vs confusability 两通道，BCS-controlled 设计有方法论贡献，centrality confound 发现有启发性 |\n| Reproducibility | 4/5 | 提供了详细 prompt 模板、decoding 参数、数据集描述、bootstrap 参数；code upon acceptance |\n\n---\n\n### Must-Fix 问题（影响接收决定）\n\n**N1** [critical] **因果语言超出证据支撑**\n- 具体位置：Title (\"Does Type Confusability **Drive** Schema-Induced Degradation\")、§1 RQ1、§4.3 (\"quasi-experimental evidence\")\n- 问题：BCS-controlled 实验声称是 \"quasi-experimental\"，但未控制关键 confounders：(a) type frequency in pretraining corpus（高 BCS 的相似 types 可能本身就是低频/罕见 types）；(b) type definition quality/length（相似 types 的 definitions 本身可能更相似，导致 LLM 混淆来自 prompt 信息不足而非 embedding space overlap）；(c) prompt position effects。Without controlling these, the study establishes **correlation** not **causation**。\n- 为什么影响接收：Title 和 RQ framing 暗示因果关系，但证据链只到相关性。如果真正的 driver 是 definition quality 或 type frequency 而非 embedding similarity 本身，整个 \"confusability\" narrative 的解释力被严重削弱。\n- 建议：(1) 将 title 改为描述性表述；(2) 明确声明 BCS-controlled 实验控制了什么、没控制什么；(3) 至少对 type frequency 进行 partial correlation 控制。\n\n**N2** [critical] **Pairwise → batch-level 效应放大缺乏数学解释**\n- 具体位置：§4.2 Table 2 (r²=1.3-1.7%) → §4.3 Table 3 (31.2pp gap)\n- 问题：Pairwise SCS 解释 type confusion variance 仅 1.3-1.7%，但论文声称这 \"compounds\" 到 batch level 产生 31.2pp gap。这一放大没有形式化的数学解释——是线性叠加（120 pairs × small effect）、还是非线性交互？更重要的是，§4.3 \"Practical magnitude\" 承认 typical batch gap 仅 2.2pp (CI: [0.4, 4.0])，即 IQR 范围内的真实效应不到 headline 的 7%。\n- 为什么影响接收：无法解释为什么 1.7% variance → 31.2pp gap（且典型场景仅 2.2pp），读者无法判断 BCS 是否有实际工程价值。31.2pp 放在 abstract 和 Table 3 作为 headline result 有误导性。\n- 建议：(1) 提供从 pairwise r² 到 batch-level gap 的数学推导；(2) 在 abstract/Results 突出 typical-batch gap（2-4pp）而非 extreme-batch gap；(3) 明确 31.2pp 是 BCS range maximized 的构造结果。\n\n**N3** [critical] **Full 80-rel 回归不显著但极端 batch 作为 headline——cherry-picking 风险**\n- 具体位置：Table 5 第三行 (full 80-rel, n=25, slope=+0.221, p=0.762)\n- 问题：使用 full 80-rel pool 的 25 个 random batches 做回归时，BCS-accuracy 关系**完全不显著**（p=0.762，slope 甚至为正）。论文注释 \"BCS range insufficient\" 作为解释，但这等于承认：在自然采样条件下，BCS 对 accuracy 没有可检测的预测力。然而 Table 3 的 31.2pp 极端 batch 比较仍是论文的核心 evidence。\n- 为什么影响接收：呈现方式 (burying the null in a footnote while headlining the extreme result) 削弱 credibility。一个 reviewer 的直觉读法：\"在 natural conditions 下找不到效应，于是构造了极端条件来展示效应\"。\n- 建议：(1) Table 5 的 80-rel null result 应与 extreme-batch result 并列讨论；(2) 论述 \"effect detectable only with sufficient BCS range\" 不等于 \"effect practically important\"。\n\n---\n\n### Should-Fix 问题\n\n**W1** [warning] **Bootstrap CI 对非独立观测可能 anti-conservative**\n- 具体位置：§4.2 Table 2 (pair-level percentile bootstrap)\n- 问题：Pairwise confusion rates 不独立——共享 type 的 pairs 在统计上相关。论文提到 \"type-level cluster bootstrap yields wider CIs\" 但仅 parenthetical 一笔带过，primary CIs 仍是 pair-level。\n- 建议：将 cluster bootstrap 作为 primary CI 报告。\n\n**W2** [warning] **Embedding 选择不一致且缺乏理论驱动**\n- 具体位置：§3.2, Table 1 (Qwen3 for Few-NERD, MiniLM for FewRel/DocRED/MAVEN)\n- 问题：如果 SCS 理论基础是 \"LLM representation space 中的 overlap 导致 confusion\"，应统一用 LLM 自身 embedding。用 MiniLM 计算 RE confusability 缺乏 first-principles justification，且未解释为何不同 task 用不同 embedding。\n- 建议：在所有 dataset 上报告两种 embedding 的 SCS-confusion 对比。\n\n**W3** [warning] **RE batch composition +1.4pp (p≈0.19) 不具统计/实际意义**\n- 具体位置：§5, Appendix D Table 7\n- 问题：n=1 graph-coloring vs random, p≈0.19, BCS margin 仅 0.006。论文 framing \"directionally consistent application\" 过于积极。Abstract 中 \"succeeds for RE\" 的表述误导。\n- 建议：坦率承认是 null result；将 framing 从 \"succeeds\" 改为 \"provides suggestive but inconclusive evidence\"。\n\n**W4** [warning] **仅两个模型（32B+8B）的跨模型泛化过于薄弱**\n- 具体位置：Appendix A, §4.3 cross-model paragraph\n- 问题：规模差异大，architecture 不同，Channel 2 在 8B NER 上未复制。两模型不足以声称 \"cross-model replication\"。\n- 建议：下调泛化声称强度。\n\n**W5** [warning] **DocRED R²=0.53 vs FewRel R²=0.218 差异解释自相矛盾**\n- 具体位置：§4.3 Document-level RE paragraph\n- 问题：论文归因 \"wider confusability range\"，但 Table 1 显示 DocRED BCS range (0.53-0.73) 实际比 FewRel (0.42-0.97) 更窄。解释与数据矛盾。\n- 建议：检查并修正此说法。\n\n---\n\n### 小问题\n\n- SCS 仅基于 type name 计算，但 prompt 中提供了 definitions——如果 LLM 主要依据 definition 判断，SCS 可能 misrepresent 真实 confusability\n- Abstract 过长（~350 words），EMNLP 建议 150-250 words\n- Table 3 的 16-rel condition 无 CI，与其他条目不一致\n- §4.4 \"100% of confusion errors are intra-batch\" 是 RE classification format 的 tautology，非 evidence for confusability\n- Limitations #6 承认 \"correlational evidence\" 与正文 \"quasi-experimental\" framing 矛盾\n\n---\n\n### 主要优势\n\n- 首次系统隔离 schema degradation 的 count 和 confusability 维度，填补 training-free IE 文献 gap\n- BCS-controlled 设计（fix count, vary confusability）比 prior work 提供更强的控制\n- Centrality confound 诊断有方法论贡献，提醒社区 per-type aggregation 在 homogeneous schemas 上的陷阱\n- Honest about negative results（SDGD failure, RE batch composition non-significance）\n- Reproducibility 良好：prompt 模板完整、参数详尽\n\n---\n\n### Questions to Authors\n\n1. 能否提供从 pairwise r²≈1.5% 到 extreme-batch 31.2pp gap 的数学推导（即使是 order-of-magnitude estimation）？\n2. 为什么 FewRel 用 MiniLM 而 Few-NERD 用 Qwen3 embedding？有没有在 FewRel 上也用 Qwen3 的结果？\n3. Table 5 full 80-rel 回归 p=0.762——如果用 top/bottom 10 batches 单独回归，是否显著？\n4. BCS-controlled 实验中，high-BCS vs low-BCS batches 的平均 type frequency 是否有系统差异？\n\n---\n\n### Missing References\n\n- Li et al. (2023) \"Evaluating ChatGPT's Information Extraction Capabilities\"\n- Wadhwa et al. (2023) \"Revisiting Relation Extraction in the era of Large Language Models\"",
    "reviewer_id": "1",
    "project": "schema-dag-extraction"
  }
}
```

</details>

---


### Tool result

_source line 261 · 2026-05-16T09:10:26.157158+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4164
}
```

</details>

---


### Assistant

_source line 262 · 2026-05-16T09:10:32.231029+00:00_

审稿意见已提交给 Review Director。

总结：给出 **3.0/5 (Findings)** 评分，主要问题集中在三个 critical issues：(1) 因果语言超出 correlational evidence 支撑，(2) pairwise r²<2% 到 31.2pp headline gap 的放大缺乏数学解释且 typical effect 仅 2pp，(3) full 80-rel 自然条件下回归不显著（p=0.762）但极端构造结果作为 headline 有 cherry-picking 风险。论文的真正贡献在方法论层面（BCS-controlled 设计、centrality confound 诊断），建议 reframe narrative 强度。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1"
}
```

</details>

---


## Round 8

## Round 8

4 recorded events


### User

_source line 263 · 2026-05-16T09:12:55.781274+00:00_

[Round 1 审稿请求]:
以下是 Reviewer 2 的完整 Round 1 审稿意见。请逐条回应：对每个 Must-Fix、Should-Fix 和小问题，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。

---

# Reviewer 2 审稿意见 — Round 1

**Overall**: 3/5 (Findings acceptance recommendation)
**Confidence**: 4/5

## Must-Fix 问题

**N1** [critical] 非显著结果被呈现为正面贡献——RE batch composition +1.4pp
- §5 第3段、Abstract 最后一句、Introduction contributions #4、Appendix Table 8
- +1.4pp gain 不显著（p≈0.19），在 15 个随机种子中排第 13 名。BCS 边际差异仅 0.006。Abstract 将其呈现为 "demonstrating a directionally consistent application"，contributions 列表将其作为第四条贡献。对于 EMNLP Main Conference 论文，将统计不显著的结果写入 contributions list 属于 overclaim。
- 建议：(1) 从 contributions list 中移除或改为明确的 negative/inconclusive result；(2) Abstract 中直接说 "does not yield statistically significant gains"。

**N2** [critical] Pairwise effect size 极低，削弱中心 claim 的实际意义
- Table 2（r²=1.3-1.7%）、§4.2 全节、§4.3 Practical magnitude 段
- SCS 仅解释 1.3-1.7% 的类型混淆方差。Typical-batch gap 仅 2.2pp（95% CI: [0.4, 4.0]），约为 extreme gap 的 7%。标题问 "Does Type Confusability Drive Schema-Induced Degradation?"——但 r²≈1.5% 的答案更接近 "type confusability is a statistically detectable but practically minor factor"。
- 建议：Abstract 和 Introduction 需要突出 typical-batch magnitude（2.2pp）；标题可能需要调整。

**N3** [critical] MAVEN 反转严重限制 two-channel 模型的普适性
- §4.1 ED (MAVEN) 段、§4.5、Abstract、Appendix §C
- 4 个数据集中，MAVEN（168 types）的 count channel 完全反转，per-type BCS-F1 correlation 在控制 centrality 后也消失（p>0.2）。Two-channel degradation model 是 contribution #1，但它在最大 schema 上部分失效。
- 建议：在 abstract/intro 中明确标注适用范围；Discussion 需更多篇幅讨论 same-domain vs cross-domain。

## Should-Fix 问题

**W1** [warning] Abstract 过长过密——约 280 words，堆积大量数字和 qualification
- 建议精简到 200 words 以内

**W2** [warning] §5（SDGD）在正文中过短（约 0.5 页），关键负面结果未充分展开
- 建议将 SDGD failure analysis 移入正文

**W3** [warning] 正文仅一幅 Figure——对 data-heavy empirical paper 不够
- 建议将 Appendix Figure 2 (error taxonomy) 移入正文

**W4** [warning] Discussion（§6）和 Conclusion（§7）过短（合计约 0.5 页）
- 建议扩展 Discussion 至至少 1 页

**W5** [warning] Related Work 覆盖度缺口
- RelationPrompt (Chia et al., 2022) 在 bib 中但未被引用
- 缺少 dialogue state tracking 和 non-LLM type confusion 相关工作
- LLM-PEE 对比可更详细

**W6** [warning] "robust across prompt designs" claim 被 v2 初始结果（n=5, -7.9pp, CI 穿零）削弱
- 建议改为 "directionally consistent across prompt designs, with attenuated magnitude"

## 小问题
1. 11 个 orphan .bib 条目
2. vLLM 版本号 v0.20.2 需核实
3. p-value 格式不一致
4. DocRED 采样细节不足
5. FewRel 合并 train+val splits 的影响需说明

## Questions to Authors
1. Typical-batch BCS gap 仅 2.2pp 是否意味着实际影响可忽略？
2. Same-domain schema 的 two-channel model 适用性限制？
3. 剩余 98% 方差的来源中哪个是主导因素？
4. Merge amplification 是否本质上使所有 decompose-then-merge 对 span-level tasks 无效？
5. 为什么不同 dataset 用不同 embedding model？

---

请逐条回应以上所有问题。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 264 · 2026-05-16T09:14:44.242037+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 1 — 对 Reviewer 2 Round 1 意见的逐条回应\n\n### Must-Fix\n\n**[AGREE] R2-N1: RE batch composition +1.4pp overclaim**\n完全同意。与我的 W3 一致。p≈0.19、n=1 treatment、BCS margin 0.006——统计和实际意义上都是 null result。Abstract \"demonstrating a directionally consistent application\" 和 contributions #4 均构成 overclaim。\n\n**[AGREE] R2-N2: Pairwise effect size 极低**\n完全同意。与我的 N2 高度重合。r²=1.3-1.7% 意味着论文 headline claim 应从 \"identifies the driver\" reframe 为 \"empirically isolates one specific, modest factor\"。核心问题是 framing hierarchy：typical gap (2.2pp) 被埋在 §4.3 中段，而 extreme gap (31.2pp) 出现在 Abstract/Table 3/Conclusion。\n\n**[REBUT] R2-N3: MAVEN 反转严重限制 two-channel 普适性**\n部分不同意，建议降为 warning：\n1. Pairwise SCS-confusion 在 MAVEN 仍高度显著（r=0.129, p<10^{-42}, Table 2）——失效的是 per-type aggregation，不是 underlying relationship\n2. Count channel 反转有明确 task-structure 解释（relaxed matching + same-domain hierarchy + class imbalance, §4.1）\n3. Appendix C 花 ~1 page 正确诊断了 centrality confound 并给出 partial correlation 验证\n4. 但同意 Abstract/Intro 需明确标注 \"cross-domain schemas\" 作为适用条件——这是 scope qualification (warning)，非 fundamental validity threat (critical)\n\n### Should-Fix\n\n**[AGREE] R2-W1**: Abstract 过长，同意精简。\n**[AGREE] R2-W2**: §5 SDGD 正文过短，merge amplification 分析应移入正文。\n**[AGREE] R2-W3**: 正文 Figure 不够，error taxonomy 图应入正文。\n**[AGREE] R2-W4**: Discussion+Conclusion 过短，缺 synthesis 和 actionable guidelines。\n\n**[REBUT] R2-W5**: Related Work 缺口——部分同意（orphan bib 应清理，LLM-PEE 可扩展），但 dialogue state tracking 与 IE scope 较远，不认为是必要补充。\n\n**[REBUT] R2-W6**: \"robust\" 被 n=5 削弱——不同意严重程度。n=25 结果 definitive（p<0.0001, r=-0.919），n=5 是 underpowered 的正确诊断（Appendix F Interpretation 段已论证）。但同意措辞可改为 \"robust in direction and significance, with modest magnitude attenuation\"。\n\n### 小问题\n5 条全部 [AGREE]。vLLM v0.20.2 可能是笔误（当前版本应在 0.4-0.6 范围）。\n\n### 与 R2 的核心分歧\n1. N3 严重程度：R2=critical, 我=warning（pairwise signal 仍显著，问题在 aggregation 方法非 fundamental relationship）\n2. W6 prompt robustness：R2 认为被 n=5 削弱，我认为 n=25 已 definitive\n\n### 共识点\n- Effect size 极小是最大 soundness 问题\n- RE +1.4pp 是 null result 不应作为 contribution\n- 因果 framing 超出 correlational evidence（我的 N1 + R2 的 N2 指向同一核心问题）\n- 论文更适合 Findings track",
  "reviewer_id": "1",
  "project": "schema-dag-extraction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 1 — 对 Reviewer 2 Round 1 意见的逐条回应\n\n### Must-Fix\n\n**[AGREE] R2-N1: RE batch composition +1.4pp overclaim**\n完全同意。与我的 W3 一致。p≈0.19、n=1 treatment、BCS margin 0.006——统计和实际意义上都是 null result。Abstract \"demonstrating a directionally consistent application\" 和 contributions #4 均构成 overclaim。\n\n**[AGREE] R2-N2: Pairwise effect size 极低**\n完全同意。与我的 N2 高度重合。r²=1.3-1.7% 意味着论文 headline claim 应从 \"identifies the driver\" reframe 为 \"empirically isolates one specific, modest factor\"。核心问题是 framing hierarchy：typical gap (2.2pp) 被埋在 §4.3 中段，而 extreme gap (31.2pp) 出现在 Abstract/Table 3/Conclusion。\n\n**[REBUT] R2-N3: MAVEN 反转严重限制 two-channel 普适性**\n部分不同意，建议降为 warning：\n1. Pairwise SCS-confusion 在 MAVEN 仍高度显著（r=0.129, p<10^{-42}, Table 2）——失效的是 per-type aggregation，不是 underlying relationship\n2. Count channel 反转有明确 task-structure 解释（relaxed matching + same-domain hierarchy + class imbalance, §4.1）\n3. Appendix C 花 ~1 page 正确诊断了 centrality confound 并给出 partial correlation 验证\n4. 但同意 Abstract/Intro 需明确标注 \"cross-domain schemas\" 作为适用条件——这是 scope qualification (warning)，非 fundamental validity threat (critical)\n\n### Should-Fix\n\n**[AGREE] R2-W1**: Abstract 过长，同意精简。\n**[AGREE] R2-W2**: §5 SDGD 正文过短，merge amplification 分析应移入正文。\n**[AGREE] R2-W3**: 正文 Figure 不够，error taxonomy 图应入正文。\n**[AGREE] R2-W4**: Discussion+Conclusion 过短，缺 synthesis 和 actionable guidelines。\n\n**[REBUT] R2-W5**: Related Work 缺口——部分同意（orphan bib 应清理，LLM-PEE 可扩展），但 dialogue state tracking 与 IE scope 较远，不认为是必要补充。\n\n**[REBUT] R2-W6**: \"robust\" 被 n=5 削弱——不同意严重程度。n=25 结果 definitive（p<0.0001, r=-0.919），n=5 是 underpowered 的正确诊断（Appendix F Interpretation 段已论证）。但同意措辞可改为 \"robust in direction and significance, with modest magnitude attenuation\"。\n\n### 小问题\n5 条全部 [AGREE]。vLLM v0.20.2 可能是笔误（当前版本应在 0.4-0.6 范围）。\n\n### 与 R2 的核心分歧\n1. N3 严重程度：R2=critical, 我=warning（pairwise signal 仍显著，问题在 aggregation 方法非 fundamental relationship）\n2. W6 prompt robustness：R2 认为被 n=5 削弱，我认为 n=25 已 definitive\n\n### 共识点\n- Effect size 极小是最大 soundness 问题\n- RE +1.4pp 是 null result 不应作为 contribution\n- 因果 framing 超出 correlational evidence（我的 N1 + R2 的 N2 指向同一核心问题）\n- 论文更适合 Findings track",
    "reviewer_id": "1",
    "project": "schema-dag-extraction"
  }
}
```

</details>

---


### Tool result

_source line 265 · 2026-05-16T09:14:48.211178+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3969
}
```

</details>

---


### Assistant

_source line 266 · 2026-05-16T09:14:53.553420+00:00_

已完成对 Reviewer 2 意见的逐条回应并提交给 Director。

核心结论：与 R2 在大部分问题上达成共识（effect size 过小、RE +1.4pp overclaim、因果语言过强），主要分歧在 MAVEN 反转的严重程度（我认为是 scope qualification 而非 fundamental failure，因为 pairwise signal 仍显著）和 prompt robustness（n=25 结果 definitive）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1"
}
```

</details>

---


## Round 9

## Round 9

30 recorded events


### User

_source line 267 · 2026-05-16T11:17:29.087902+00:00_

[Round 1 审稿请求]:
## Round 1 审稿任务 — Reviewer 1（方法严谨性 + 实验设计 + 统计分析）

### Venue 信息
- **Venue**: ACL ARR May 2025 (Main Conference, Long Paper)
- **Deadline**: 2025-05-25
- **页数限制**: 正文 8 页（Limitations/Ethics/References 不计）
- **模板**: ACL style (`\usepackage[review]{acl}`)
- **匿名**: Double-blind
- **Checklist**: Responsible NLP Research Checklist 必需

### 论文路径
`projects/schema-dag-extraction/docs/paper/main.tex`
（含子文件：abstract.tex, introduction.tex, related_work.tex, experimental_setup.tex, results.tex, sdgd_negative.tex, discussion.tex, checklist.tex, prompt_appendix.tex）

### 你的审查侧重

**聚焦方法严谨性和实验设计**，具体关注：

1. **SCS/BCS 指标定义**：embedding cosine similarity 作为 type confusability proxy 的合理性；type name-only SCS 是否充分反映推理时信息（prompt 实际包含 definitions）
2. **实验控制变量**：count curve 和 BCS-controlled 两种实验范式能否真正分离 count 与 confusability；是否存在未控制的 confounders（type frequency, definition quality, prompt position）
3. **统计分析严谨性**：
   - Pairwise r²=1.3-1.7% 到 batch-level gap 31.2pp 的放大是否有充分论证
   - Bootstrap CIs 的构造（非独立观测问题）
   - Within-pool analysis 的 power 和 CI 覆盖零的问题
   - 80-rel full condition p=0.762 与 extreme-batch headline 31.2pp 的关系
   - Permutation test 的适用性
4. **Cross-model validation**：仅两个模型是否足够支撑 "cross-model replication" claim；8B NER Channel 2 floor effects 的处理
5. **SDGD 实验**：merge amplification 诊断的充分性；RE batch composition +1.4pp (p≈0.19) 的结论准确性
6. **Prompt sensitivity**：v1/v2 切换对结果的影响；v2 下 effect attenuation 的定量评估

请对上述方面逐一给出评价（strength 或 weakness），并按 ACL 审稿标准给出：
- **Strengths**（逐条）
- **Weaknesses**（逐条，标注 severity: critical/warning/minor）
- **Questions**（需要作者回答的）
- **Overall Assessment**（soundness 1-5 分）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 268 · 2026-05-16T11:17:39.682429+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebSearch,mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebSearch,mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director",
    "max_results": "3"
  }
}
```

</details>

---


### Tool result

_source line 269 · 2026-05-16T11:17:39.732988+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 270 · 2026-05-16T11:17:44.060682+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL ARR 2025 reviewer guidelines review form criteria scoring"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR 2025 reviewer guidelines review form criteria scoring"
  }
}
```

</details>

---


### Tool call

_source line 271 · 2026-05-16T11:17:44.766576+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 272 · 2026-05-16T11:17:44.817533+00:00_

1	\documentclass[11pt]{article}
2	
3	\usepackage[review]{acl}
4	
5	\usepackage{times}
6	\usepackage{latexsym}
7	\usepackage[T1]{fontenc}
8	\usepackage[utf8]{inputenc}
9	\usepackage{microtype}
10	\usepackage{graphicx}
11	\usepackage{booktabs}
12	\usepackage{amsmath}
13	\usepackage{enumitem}
14	\usepackage[normalem]{ulem}
15	\usepackage{listings}
16	
17	\title{Does Type Confusability Shape Schema-Induced Degradation\\in Training-Free LLM Information Extraction?}
18	
19	\author{Anonymous}
20	
21	\begin{document}
22	\maketitle
23	
24	\input{abstract}
25	
26	\input{introduction}
27	
28	\input{related_work}
29	
30	\input{experimental_setup}
31	
32	\input{results}
33	
34	\input{sdgd_negative}
35	
36	\input{discussion}
37	
38	\section*{Limitations}
39	\begin{enumerate}[leftmargin=*,itemsep=2pt]
40	\item \textbf{Model coverage.} Primary experiments use Qwen3-32B with cross-model validation on Llama-3.1-8B-Instruct. Whether patterns hold for proprietary models (GPT-4, Gemini) remains unverified. Channel~2 was not robustly detectable on NER at 8B scale, likely due to floor effects.
41	
42	\item \textbf{Modest pairwise effect size.} Pairwise SCS explains 1.3--1.7\% of type confusion variance; entity frequency, prompt position, mention ambiguity, and type definition quality likely account for the remainder.
43	
44	\item \textbf{Non-significant factorial test.} Within-dataset count $\times$ BCS interaction on Few-NERD did not reach significance (Appendix~\ref{sec:appendix_factorial}); cross-pool slope consistency suggests confusability sensitivity is stable rather than amplifying.
45	
46	\item \textbf{Decomposition and metric scope.} RE batch composition is tested on FewRel only; NER merge alternatives remain unexplored. SCS relies on embedding cosine similarity; label entropy or ontological depth may capture complementary dimensions.
47	
48	\item \textbf{RE format specificity.} RE's clean channel separation may reflect its closed-set classification format. FewRel combines traini
…[truncated 18047 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 273 · 2026-05-16T11:17:52.571072+00:00_

Web search results for query: "ACL ARR 2025 reviewer guidelines review form criteria scoring"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"aclrollingreview/reviewerguidelines.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/reviewerguidelines.md"},{"title":"ACLRollingReview (@ReviewAcl) / X","url":"https://x.com/reviewacl"},{"title":"aclrollingreview/reviewing.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/reviewing.md"}]

Based on the search results, here's what I found about ACL ARR 2025 reviewer guidelines, review form criteria, and scoring:

## Three Scoring Dimensions

Starting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation.

## Soundness Score

The soundness scores must be justified 
…[truncated 1567 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 8510
}
```

</details>

---


### Tool call

_source line 274 · 2026-05-16T11:17:56.640253+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL ARR review form 2025 soundness excitement scoring scale 1-5 detailed criteria"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR review form 2025 soundness excitement scoring scale 1-5 detailed criteria"
  }
}
```

</details>

---


### Tool call

_source line 275 · 2026-05-16T11:17:58.507028+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 276 · 2026-05-16T11:17:59.165041+00:00_

1	\begin{abstract}
2	Training-free LLM information extraction degrades as schema complexity grows. We conduct the first controlled study isolating type confusability from type count across NER, RE (a closed-set classification task), and event detection on four datasets, introducing the Schema Confusability Score (SCS) and two paradigms: count curves varying schema size while randomizing confusability, and BCS-controlled experiments fixing size while varying confusability.
3	
4	We identify two degradation channels: count-driven recall decline and confusability-driven type substitution. For RE, the quartile BCS gap is $-$5.3\,pp (95\% CI: [$-$7.4, $-$3.2]); typical random batches differ by ${\approx}\,2.2$\,pp. Under extreme-batch construction maximizing BCS contrast, the gap reaches 31.2\,pp. Batch-level BCS explains $R^2 = 0.22\text{--}0.53$ of accuracy variance as an aggregated signal, while pairwise effect sizes remain modest ($r^2 = 1.3\text{--}1.7\%$). The effect is directionally consistent across prompt designs, with attenuated magnitude under improved prompts. Channel~1 replicates fully on Llama-3.1-8B; Channel~2 replicates on RE but shows floor effects on 8B NER. Count increases generally suppress extraction on cross-domain schemas; MAVEN's same-domain schema exhibits centrality confounding that reverses this trend. Schema decomposition via oracle routing recovers count-based degradation for RE (+29.8\,pp over single-pass), but confusability-aware grouping yields no significant additional gain (+1.4\,pp, $p\approx 0.19$).
5	\end{abstract}
6	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 658
}
```

</details>

---


### Tool call

_source line 277 · 2026-05-16T11:17:59.215721+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 278 · 2026-05-16T11:17:59.671257+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	Training-free LLM information extraction---prompting a large language model with a target schema and asking it to extract structured information without any task-specific fine-tuning---enables rapid deployment across new domains and ontologies. This zero-shot paradigm eliminates the need for labeled data, making it attractive for applications where annotation is expensive or schemas evolve frequently \cite{llm4ie-survey-2024}. Yet the paradigm carries a critical limitation: performance degrades sharply as the number of candidate types in the prompt schema grows. On named entity recognition, recall drops from 0.72 with a single candidate type to 0.42 with 64 types, a 42\% relative decline. On relation extraction, accuracy falls from 85.7\% with one relation to 50.4\% with 80 relations (sentence-level) and from 88.0\% to 38.7\% with 96 relations (document-level)---near or exceeding halving. This degradation is not academic: real-world ontologies routinely define 50--200+ types, placing them squarely in the regime where training-free extraction becomes unreliable.
5	
6	What causes this degradation? Prior decomposition strategies implicitly assume different answers: \citet{uniner-2024} extract each type independently; \citet{llm-pee-2025} partition schemas by type embedding similarity; \citet{parse-2025} optimize schema definitions. None isolates \emph{why} schemas degrade performance. The closest work, LLM-PEE, reduces both the number of co-presented types and their inter-type similarity simultaneously, making it impossible to determine which factor accounts for the gains. All prior approaches conflate two mechanisms: having more types to discriminate among (count) and having semantically similar types to confuse (confusability). Without disentangling these, decomposition strategies optimize a black-box objective without understanding its components.
7	
8	We ask three questions. \textbf{RQ1}: Does type confusabil
…[truncated 2905 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 455
}
```

</details>

---


### Tool call

_source line 279 · 2026-05-16T11:17:59.671701+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/experimental_setup.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/experimental_setup.tex"
  }
}
```

</details>

---


### Tool result

_source line 280 · 2026-05-16T11:17:59.723139+00:00_

1	\section{Experimental Setup}
2	\label{sec:experimental_setup}
3	
4	We evaluate how prompt schema size and inter-type confusability affect zero-shot LLM extraction across three information extraction tasks and four datasets: named entity recognition (NER), sentence-level relation extraction (RE), document-level RE, and event detection (ED).
5	
6	\subsection{Tasks and Datasets}
7	\label{sec:datasets}
8	
9	\paragraph{Few-NERD (NER).}
10	Few-NERD \cite{fewnerd-2021} provides 66 fine-grained entity types organized into 8 coarse categories (person, location, organization, building, art, product, event, other). The dataset spans diverse domains, making it suitable for cross-domain evaluation. We sample 1{,}000 test instances and evaluate with token-level text matching.
11	
12	\paragraph{FewRel (RE).}
13	FewRel \cite{fewrel-2018} contains 80 relation types sourced from Wikidata. Since the validation split covers only 16 relations, we combine the training and validation splits to obtain the full 80-relation pool required for schema-scale experiments, and sample 1{,}000 balanced instances (12--13 per relation type, stratified to ensure equal representation). Each instance provides a sentence with marked head and tail entities; the task is to classify the relation.
14	
15	\paragraph{DocRED (Document-level RE).}
16	DocRED \cite{docred-2019} contains 96 relation types sourced from Wikidata, evaluated at the document level where entity pairs may span multiple sentences. We sample balanced instances and formulate the task identically to FewRel: given a document with marked head and tail entities, classify the relation. DocRED extends the RE evaluation to a larger schema (96 vs.\ 80 types) and document-level context, testing whether confusability effects persist under longer input contexts and cross-sentence reasoning.
17	
18	\paragraph{MAVEN (ED).}
19	MAVEN \cite{maven-2020} defines 168 event types derived from the FrameNet ontology, making it a same-domain schema. We use the va
…[truncated 6235 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool result

_source line 281 · 2026-05-16T11:18:05.872169+00:00_

Web search results for query: "ACL ARR review form 2025 soundness excitement scoring scale 1-5 detailed criteria"

Links: [{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"aclrollingreview/reviewerguidelines.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/reviewerguidelines.md"},{"title":"ACL 2025 Statistics - Paper Copilot","url":"https://papercopilot.com/statistics/acl-statistics/acl-2025-statistics/"},{"title":"ACL 2023 Acceptance Recommendations - ACL 2023","url":"https://2023.aclweb.org/blog/overall-recommendation/"},{"title":"🎪 ACL 2025 Reviews Are Out: To Rebut or Flee? The Harsh Reality of NLP’s \"Publish or Perish\" Circus | CSPaper Forum","url":"https://forum.cspaper.org/topic/27/acl-2025-reviews-are-out-to-rebut-or-flee-the-harsh-reality-of-nlp-s-publish-or-perish-circus"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"ACL 2026 on X: \"Checkout the blog post on the soundness/excitement scores https://t.co/AKSO9DjiYP . It clarifies the reasoning behind the separation of overall scores and how it might make the reviewer recommendation more robust. #ACL2023Toronto #ACL2023NLP #NLProc\" / X","url":"https://x.com/aclmeeting/status/1637827267173953540"},{"title":"Conference Decisions · GitHub","url":"https://gist.github.com/antonisa/2158dee79179c7c49304ef353887bfa0"}]

Based on the search r
…[truncated 2451 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 9231
}
```

</details>

---


### Tool call

_source line 282 · 2026-05-16T11:18:10.996171+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex"
  }
}
```

</details>

---


### Tool result

_source line 283 · 2026-05-16T11:18:11.499259+00:00_

1	\section{Results}
2	\label{sec:results}
3	
4	Unless otherwise noted, all experiments in this section use the v1 prompt (\S\ref{sec:model}; full templates in Appendix~\ref{sec:appendix_prompts}).
5	
6	\subsection{Count-Degradation Curves}
7	\label{sec:count_curves}
8	
9	\begin{figure}[t]
10	\centering
11	\begin{minipage}[t]{0.48\columnwidth}
12	\centering
13	\includegraphics[width=\linewidth]{../../figures/paper/fig_count_curves.pdf}
14	\end{minipage}
15	\hfill
16	\begin{minipage}[t]{0.48\columnwidth}
17	\centering
18	\includegraphics[width=\linewidth]{../../figures/paper/fig_bcs_scaling.pdf}
19	\end{minipage}
20	\caption{\textbf{(a)} Count-degradation curves across four datasets. NER recall generally declines and RE accuracy (both FewRel and DocRED) declines monotonically with schema size; MAVEN relaxed F1 increases (\S\ref{sec:centrality_confound}). \textbf{(b)} BCS-controlled FewRel accuracy. The BCS--accuracy slope is consistent across the independent 16-relation pool and within-pool 16-relation subsets (permutation $p = 0.60$); the wider BCS range available at 80 relations produces larger absolute gaps.}
21	\label{fig:main_results}
22	\end{figure}
23	
24	We first examine how extraction performance changes as the number of types in the prompt schema increases (Experiment~1; Figure~\ref{fig:main_results}a).
25	
26	\paragraph{NER (Few-NERD).}
27	Recall declines from 0.72 at count${}\,=\,1$ to 0.42 at count${}\,=\,64$ ($-$42\% relative), with minor non-monotonicity within sampling variability (bootstrap CIs overlap). Precision rises inversely (0.11 $\to$ 0.52), reflecting a shift from over-prediction to under-prediction as candidate types increase.
28	
29	\paragraph{RE (FewRel).}
30	Accuracy drops monotonically from 85.7\% at count${}\,=\,1$ through 58.8\% at count${}\,=\,40$ to 50.4\% at count${}\,=\,80$, a near-halving when the model must discriminate among all 80 relation types simultaneously. (The count${}\,=\,40$ evaluation uses 40-relation subsets sampled fr
…[truncated 14298 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 503
}
```

</details>

---


### Tool call

_source line 284 · 2026-05-16T11:18:11.499610+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/sdgd_negative.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/sdgd_negative.tex"
  }
}
```

</details>

---


### Tool result

_source line 285 · 2026-05-16T11:18:11.801323+00:00_

1	\section{Schema Decomposition: Failure, Diagnosis, and Mitigation}
2	\label{sec:sdgd}
3	
4	A natural intervention is to partition the schema so confusable types never co-occur. We test this with \textbf{Schema-DAG-Guided Decomposition} (SDGD), which uses greedy graph coloring on the pairwise SCS graph to assign types to low-confusability batches, merging predictions via set union. Every decomposition mode---SDGD (F1\,=\,0.241), random batching (0.320), per-type (0.292)---falls below the single-pass baseline (0.445) on Few-NERD NER (Table~\ref{tab:sdgd_results}).
5	
6	\paragraph{Merge amplification as the bottleneck.}
7	The failure is \emph{merge amplification}: presenting the same text $k$ times causes each pass to independently generate predictions. Single-pass precision (0.563) collapses to 0.210--0.249 after union merge with 8 batches, while recall gains are modest (0.368 $\to$ 0.314--0.446). Confidence gating improves precision but with disproportionate recall loss (Appendix~\ref{sec:appendix_sdgd}). The fundamental issue is that LLM predictions are not calibrated across passes \cite{llm-calibration-survey-2024}.
8	
9	In our NER experiments, multi-pass decomposition produces $k$ independent tagging outputs per sentence. Entities may receive conflicting labels across separate decomposition passes, or hallucinated entities may appear in passes where the correct type is absent. Union merge amplifies these false positives: precision collapses from 0.563 (single-pass) to 0.210--0.249 (8 batches), faster than the modest recall gains.
10	
11	\paragraph{Why NER fails but RE does not.}
12	Merge amplification is specific to span-level tasks: each NER pass independently proposes entity spans, and union merge must resolve conflicting boundaries and type assignments, degrading systematically with pass count. Under oracle routing, RE requires no span reconciliation---each pair receives a single classification from the batch containing its gold type, eliminating the mechanis
…[truncated 913 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 286 · 2026-05-16T11:18:11.801687+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 287 · 2026-05-16T11:18:11.852150+00:00_

1	\section{Discussion}
2	\label{sec:discussion}
3	
4	\paragraph{Boundary conditions.}
5	The two-channel model applies to cross-domain schemas; same-domain schemas (e.g., MAVEN's FrameNet-derived event types) exhibit centrality confounding that obscures per-type aggregated signals, requiring pairwise SCS or centrality adjustment (\S\ref{sec:centrality_confound}). High-BCS accuracy converges to $\approx$51\% across tested models, suggesting a task-inherent difficulty ceiling. RE's clean channel separation may partly reflect its closed-set format; the effect generalizes to document-level RE (DocRED slope $-$0.71). Prompt design modulates but does not eliminate the effect (v2 gap: $-$25.5\,pp vs.\ v1: $-$31.2\,pp; Appendix~\ref{sec:appendix_prompt_sensitivity}).
6	
7	\paragraph{Practitioner guidance.}
8	Our results suggest that type pairs with high SCS tend to produce disproportionately more substitution errors (\S4.3). Practitioners designing extraction schemas may benefit from pre-computing pairwise SCS and restructuring or merging types that exceed this threshold.
9	
10	\paragraph{Future directions.}
11	Three directions merit investigation: (i)~non-oracle routing strategies (e.g., embedding-based instance-to-batch assignment) that would make decomposition deployable without gold labels; (ii)~broader model coverage, particularly proprietary APIs; and (iii)~definition-inclusive SCS that incorporates type descriptions rather than names alone. For NER, merge amplification blocks naive decomposition (\S\ref{sec:sdgd}); calibration-aware merge, joint decoding, or coarse-to-fine extraction may address this.
12	
13	\section{Conclusion}
14	\label{sec:conclusion}
15	
16	We isolated schema-induced degradation into count-driven recall decline and confusability-driven type confusion, showed these channels are separable in RE, with Channel~2 additionally impairing entity detection in NER, and confirmed that both channels replicate across model families on RE (Meta-Llama-3.1-8B-Ins
…[truncated 688 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 288 · 2026-05-16T11:18:16.980734+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 289 · 2026-05-16T11:18:17.031516+00:00_

1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{Training-free LLM IE.}
5	Training-free LLM IE spans instruction tuning \cite{instructuie-2023}, code-style schema encoding \cite{knowcoder-2024,codeie-2023}, annotation-guided extraction \cite{gollie-2024,adelie-2024}, schema-driven decoding \cite{slot-2025,oneke-2025}, and constrained JSON decoding \cite{json-schema-bench-2025}. For NER, methods include zero-shot decomposition \cite{xie-zeroshot-ner-2023,promptner-2023}, distillation \cite{uniner-2024}, and bidirectional encoders \cite{gliner-2024,gliner2-2025}. For RE, recent work examines zero-shot relation triplet extraction via prompting \cite{relationprompt-2022} and revisits relation extraction in the LLM era \cite{wadhwa-re-llm-2023}. These methods perform well with moderate schemas (4--20 types) but none investigates how performance degrades as schema complexity scales, nor proposes quantitative metrics for inter-type confusability.
6	
7	\paragraph{Schema complexity in IE.}
8	The most directly related work is LLM-PEE \cite{llm-pee-2025}, which partitions large event schemas by type embedding similarity. Our work differs in three ways: (1)~we conduct controlled analysis to understand \emph{why} extraction degrades rather than developing an engineering solution; (2)~our BCS-controlled experiments isolate count from confusability, which LLM-PEE conflates; (3)~our SDGD experiments reveal that merge amplification---not partitioning quality---is the bottleneck in decompose-then-merge pipelines. Other approaches address schema complexity via hard negative mining \cite{iepile-2024}, schema definition optimization \cite{parse-2025}, multi-agent debate \cite{crossagentie-2025,cmas-ner-2025}, schema-aware decomposition for event extraction \cite{dee-2024}, and active prompting \cite{reflect-learn-2026}; all treat it as an engineering problem rather than isolating the underlying degradation mechanisms.
9	
10	\paragraph{Embedding anisotropy.}
11	Our cen
…[truncated 349 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 290 · 2026-05-16T11:18:17.083364+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/checklist.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/checklist.tex"
  }
}
```

</details>

---


### Tool result

_source line 291 · 2026-05-16T11:18:17.083804+00:00_

1	\section*{Responsible NLP Research Checklist}
2	
3	For each question, the answer is \textbf{Yes}, \textbf{No}, or \textbf{N/A}. If Yes, the relevant section is indicated. If No, a justification is provided.
4	
5	\subsection*{A \quad For Every Submission}
6	
7	\begin{enumerate}[label=\textbf{A\arabic*.},leftmargin=*,itemsep=4pt]
8	
9	\item \textbf{Did you describe the limitations of your work?}
10	
11	Yes. The Limitations section (after \S\ref{sec:conclusion}) discusses single-model reliance, modest pairwise effect sizes, cross-pool slope consistency, non-significant factorial results, decomposition scope, and metric scope.
12	
13	\item \textbf{Did you discuss any potential risks of your work?}
14	
15	N/A. This is a purely analytical study of schema-induced degradation in existing LLM IE systems. It does not introduce new models, datasets, or deployment-facing artifacts. The findings characterize failure modes and are intended to inform safer schema design.
16	
17	\item \textbf{Do the abstract and introduction summarize the paper's main claims?}
18	
19	Yes. The abstract and \S\ref{sec:introduction} state the two-channel degradation pattern (count and confusability), the cross-model replication, and the negative SDGD result.
20	
21	\item \textbf{Did you use AI assistants (e.g., ChatGPT, Copilot) when working on this paper?}
22	
23	Yes. An AI coding assistant was used for experiment scripting and LaTeX formatting. All scientific claims, experimental design, and analysis were conducted by the authors.
24	
25	\end{enumerate}
26	
27	\subsection*{B \quad Scientific Artifacts}
28	
29	\begin{enumerate}[label=\textbf{B\arabic*.},leftmargin=*,itemsep=4pt]
30	
31	\item \textbf{Did you cite the creators of artifacts you used?}
32	
33	Yes. Few-NERD \cite{fewnerd-2021}, FewRel \cite{fewrel-2018}, MAVEN \cite{maven-2020}, Qwen3-32B \cite{qwen3-2025}, Meta-Llama-3.1-8B-Instruct, vLLM \cite{vllm-2023}, and all-MiniLM-L6-v2 \cite{minilm-2020} are cited in \S\ref{sec:datasets} and \S
…[truncated 4366 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 292 · 2026-05-16T11:18:20.800059+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/prompt_appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/prompt_appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 293 · 2026-05-16T11:18:20.852181+00:00_

1	\lstset{
2	  basicstyle=\ttfamily\small,
3	  breaklines=true,
4	  breakatwhitespace=true,
5	  columns=fullflexible
6	}
7	
8	\section{Prompt Templates}
9	\label{sec:appendix_prompts}
10	
11	This appendix reproduces the complete prompt templates used for all three extraction tasks.
12	All prompts are injected into a single \texttt{user} message (no system prompt); the model's chat template adds the system/assistant framing.
13	Both versions provide a JSON-formatted type schema to the vLLM constrained-decoding engine; the schema is \emph{not} included in the natural-language prompt itself.
14	We use greedy decoding (\texttt{temperature=0}, \texttt{seed=42}) throughout.
15	
16	\medskip\noindent
17	\textbf{Notation.}
18	Placeholders are shown in \texttt{\{braces\}}.
19	Text \textbf{added in v2} (relative to v1) is marked with $\triangleright$.
20	Text \textbf{removed in v2} is marked with \sout{strikethrough}.
21	
22	\subsection{Named Entity Recognition (Few-NERD)}
23	
24	\paragraph{v1 prompt (with character offsets).}
25	
26	\begin{small}
27	\begin{lstlisting}
28	Extract all named entities from the following text.
29	Only extract entities of the following types:
30	- {type_1}: {definition_1}
31	- {type_2}: {definition_2}
32	  ...
33	
34	Text: {input_text}
35	
36	Output as JSON: [{"text": "...", "type": "...",
37	                  "start": ..., "end": ...}]
38	\end{lstlisting}
39	\end{small}
40	
41	\noindent
42	\textbf{v1 constrained-decoding schema:}
43	\begin{small}
44	\begin{lstlisting}
45	{"type": "array",
46	 "items": {"type": "object",
47	   "properties": {
48	     "text":  {"type": "string"},
49	     "type":  {"type": "string",
50	               "enum": [&lt;sorted_types>]},
51	     "start": {"type": "integer"},
52	     "end":   {"type": "integer"}},
53	   "required": ["text","type","start","end"]}}
54	\end{lstlisting}
55	\end{small}
56	
57	\paragraph{v2 prompt (text+type only).}
58	
59	\begin{small}
60	\begin{lstlisting}
61	Extract all named entities from the foll
…[truncated 5190 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 52
}
```

</details>

---


### Tool call

_source line 294 · 2026-05-16T11:20:56.009211+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## 总体评分\n**Overall**: 3.5 / 5（介于 Resubmit next cycle 和 Accept 之间，偏向 Accept with revisions）\n**一句话总结**: 研究问题有价值、实验设计有创意，但 SCS 指标存在构造缺陷（name-only vs. prompt 实际包含 definitions），核心统计叙事在 headline 数字（31.2pp）和 practical magnitude（2.2pp）之间存在张力，两模型验证不足以支撑 \"cross-model replication\" 的 claim。\n\n## 官方维度打分（来自 ACL ARR Review Form, Feb 2025+）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3/5 | 核心指标 SCS 的构造前提与实验设置矛盾（详见 N1）；统计推断从 r²=1.5% 到 31.2pp 的放大逻辑需更严格论证；多项关键条件未达显著性 |\n| Excitement | 4/5 | 首次系统分离 count vs. confusability 两条退化通道，研究问题对零样本 IE 社区有直接实用价值 |\n| Overall | 3.5/5 | 选题好、设计巧，但方法论缺陷若不修复会影响结论可信度 |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] SCS 指标构造与实验设置之间的逻辑矛盾\n\n- 具体位置：§3.2 第56行 \"Both use type name strings only, without definitions or descriptions, **to reflect the information available to the model at inference time**\"（强调为原文）；Appendix §F (prompt_appendix.tex) 第28-32行明确显示 prompt 格式为 `- {type_1}: {definition_1}`\n- 问题：论文以 \"反映推理时模型可用信息\" 为理由仅用 type name 计算 SCS。但 prompt 模板明确表明模型推理时看到的是 **name + definition**，而非仅 name。因此 SCS 实际测量的是 type name 的 embedding 相似度，而非模型决策时面对的完整信息的相似度。两个 type name 相近但 definition 能有效区分的类型对（如 \"person-artist\" vs. \"person-athlete\"，定义差异大）可能被 SCS 标记为高混淆，但模型实际并不混淆。反之，name 不同但 definition 相似的类型对会被漏标。\n- 为什么影响接收：SCS 是全文两大范式（count curve 的 BCS 聚合、BCS-controlled experiment 的分组依据）的核心度量。如果 proxy 的构造前提本身有误，所有基于 BCS 分层的实验结论的效度存疑。\n- 建议修改方向：(1) 用 \"name + definition\" 拼接后的 embedding 重新计算 SCS，对比 name-only 结果；(2) 如保留 name-only，需修改理由——改为 \"name-only SCS 是 lightweight pre-hoc proxy，虽不完全匹配推理时信息，但实证验证表明与观测混淆率相关\"（论文已有部分此类语言，但需去除 §3.2 的错误理由）。\n\n**N2** [critical] Headline 数字 31.2pp 与 practical magnitude 2.2pp 之间的叙事失衡\n\n- 具体位置：Abstract 第4行 \"the gap reaches 31.2 pp\"；§4.3 Practical magnitude 段 \"the typical BCS span (IQR = 0.054) yields an expected accuracy gap of 2.2 pp\"\n- 问题：Abstract/Introduction 突出 31.2pp 作为核心结果，但这是 **extreme-batch construction**（刻意选取 BCS 分布两端极端值）的产物。对 practitioner 而言，随机 schema 下的预期影响仅 2.2pp（Table 5 quartile Δ = 3.9pp）。论文在 §4.3 有诚实讨论，但 framing 仍可能误导读者高估效应实用规模。\n- 为什么影响接收：ACL ARR soundness 标准要求 claim 与证据匹配。如果 abstract 传达的印象是 \"confusability 导致 31.2pp 退化\"，而实际 typical 影响仅 ~2pp，这构成 overclaim。\n- 建议修改方向：Abstract 中应同时报告 extreme-batch gap 和 typical-batch gap，例如 \"quartile gap of −5.3 pp under typical batching (reaching −31.2 pp under extreme BCS contrast)\"。\n\n**N3** [critical] r²=1.3–1.7% → batch-level R²=22–53% 的 \"amplification\" 论证不严格\n\n- 具体位置：§4.3 Practical magnitude 最后一句 \"Pair-level r²=1.5% aggregates to batch-level R²=22–53% across datasets, a 14–35× amplification consistent with averaging over ~C(k,2) correlated pair effects per batch\"\n- 问题：这一放大并非简单的统计聚合效应。Pair-level r² 描述的是单一 type pair 的 SCS 对该 pair 混淆率的解释力；batch-level R² 描述的是 batch 的 mean BCS 对该 batch 整体准确率的解释力。两者度量的对象不同（pair confusion rate vs. batch accuracy）且受不同混杂因素影响。论文用 \"consistent with averaging over ~C(k,2) correlated pair effects\" 一带而过，但没有给出：(1) 在什么相关结构下这种放大成立的数学推导或模拟验证；(2) 排除 batch-level R² 来自其他 batch-level confounders（如 batch 内 type frequency 分布、type definition 长度等）的可能性。\n- 为什么影响接收：这个 amplification 叙事是论文 \"modest pairwise effect 仍有实用意义\" 的核心支柱。如果聚合效应的归因不正确，整条推理链断裂。\n- 建议修改方向：(1) 用 simulation 验证：给定 pairwise r=0.12 和观测到的 pair-pair 相关矩阵，模拟 batch-level R² 的期望分布；(2) 明确区分 pair-level 和 batch-level 分析的 claim 范围，不要将二者用单一 \"amplification\" 叙事串联。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] \"Cross-model replication\" claim 仅基于两个模型\n\n- 具体位置：§4.1 \"Cross-model replication\"段；§4.3 \"Cross-model validation\"段；Table 1/2\n- 问题：Qwen3-32B 和 Llama-3.1-8B-Instruct 在模型规模（32B vs 8B）和架构上同时不同。Channel 2 在 8B NER 上出现 floor effects 无法检测。两个模型不足以支撑 \"cross-model replication\" 这一术语的通常含义（暗示现象在模型间广泛成立）。\n- 建议：改为 \"cross-model consistency check\" 或 \"preliminary cross-model evidence\"，并在 Limitations 中明确说明不能排除 model-specific artifacts。\n\n**W2** [warning] Bootstrap CIs 的非独立观测问题未充分处理\n\n- 具体位置：§4.2 Table 2 \"CIs are pair-level percentile bootstrap (B=1,000)\"；同段提到 \"Type-level cluster bootstrap yields wider but still significant CIs\"\n- 问题：Pairwise SCS 的 bootstrap 单位应为 type（每个 type 参与多个 pair），而非 pair。论文确实提到了 cluster bootstrap 并报告了更宽的 CI，但 (1) 主表（Table 2）仍报告的是 pair-level bootstrap CI，cluster bootstrap 仅在正文中一笔带过；(2) 没有说明 cluster bootstrap 的聚类变量是什么（按单一 type？按 type pair 共享的某一 type？）。\n- 建议：主表应报告 cluster-robust CI（或至少双报），并明确 cluster 定义。\n\n**W3** [warning] Within-pool quartile Δ 的 CI 跨零 + full 80-rel condition p=0.762\n\n- 具体位置：Table 5 — 80-pool→16-sub quartile Δ CI = [−8.17, +0.38]；full 80-rel slope p=0.762\n- 问题：论文的 within-pool control 是关键设计——用于排除 pool composition confound。但该条件的 quartile Δ CI 跨零，regression 虽显著 (p=0.027) 但 borderline。Full 80-rel condition 完全不显著。论文将后者归因于 BCS range 不足，但另一种解释是：当 type pool 固定（不能自由选择 extreme types）时，confusability 效应消失或极小。这与 extreme-batch 结果的可推广性直接相关。\n- 建议：(1) 增加 80-pool 内的 BCS variation 方法（如更大的 subsample n 或不同的 subset size）来提升 power；(2) 如不可补实验，需在正文（不仅 appendix）明确讨论 generalizability 的限制。\n\n**W4** [warning] FewRel 使用 training + validation split 合并数据\n\n- 具体位置：§3.1 FewRel 段 \"we combine the training and validation splits to obtain the full 80-relation pool\"\n- 问题：FewRel 的 training split 有 64,000 instances across 64 relations（每 relation 700 instances），validation 有 16,000 instances across 16 relations。合并后从 training split 采样的实例可能与模型预训练数据重叠（Qwen3/Llama 的训练数据未公开）。论文未讨论数据泄露风险。\n- 建议：(1) 讨论 contamination 风险并进行简单检验（如对比 train-split 和 val-split 来源的 relation 在 accuracy 上的差异）；(2) 说明为何不使用仅 validation split 的 16-relation 子集进行核心分析。\n\n**W5** [warning] SDGD 的 RE batch composition 结论过于弱化为 \"contribution\"\n\n- 具体位置：§5 最后段 \"+1.4 pp that is directionally consistent but not statistically significant (p ≈ 0.19)\"；Introduction Contribution (4) 将此列为贡献\n- 问题：n=1（单一 graph coloring 配置）、BCS margin 仅 0.006、p=0.19——这本质上是 null result。论文诚实报告了这一点，但仍将其框架为 \"贡献\" 之一，措辞 \"directionally consistent\" 暗示支持假说。统计学上，p=0.19 下的方向一致性没有信息量。\n- 建议：将 Contribution (4) 重新框架为 \"negative/inconclusive finding on confusability-aware grouping\"，不要使用 \"directionally consistent\" 这样的措辞。或者增加 n（多种 graph-coloring 方案/阈值），使结论具有统计基础。\n\n**W6** [warning] v1 vs v2 的选择性报告\n\n- 具体位置：§4 开头 \"Unless otherwise noted, all experiments in this section use the v1 prompt\"；§3.4 描述 v1 有 96.5% hallucinated offsets\n- 问题：v1 prompt 导致 96.5% 的 offset 幻觉，表明模型在 v1 下输出质量有问题。论文主要基于 v1 结果，理由是 v1 是初始版本。但如果 v2 是更合理的 prompt 设计（减少幻觉、提升精度），那么核心结论应该基于 v2 验证。当前做法相当于基于已知有缺陷的实验设置建立结论，再用改进设置做 sensitivity check。\n- 建议：说明为什么选择 v1 作为 primary（如果是因为 v1 effect size 更大则需承认这一点），或者将 v2 结果提升为同等地位。\n\n---\n\n## 小问题（不影响接收）\n\n- §3.2：\"to reflect the information available to the model at inference time\" 这一表述即使修改 SCS 构造理由后仍需删除，因为与事实不符。\n- Table 1 (BCS-controlled)：16-rel condition 无 CI（仅一个 extreme batch per level），应在表内注明 n=1 限制。已有脚注但容易忽略。\n- §4.1 MAVEN：relaxed F1 increases 的解释涉及三个因素（relaxed matching、same-domain hierarchy、class imbalance），未区分各因素贡献，分析偏定性。\n- Limitations 第5条 \"FewRel combines training and validation splits for 80 types and characterizes classification accuracy rather than end-to-end extraction\" 似在为 FewRel 非端到端性质辩解，但更重要的 limitation 是 data contamination 风险（W4）。\n- Checklist B2：\"FewRel, DocRED, and MAVEN are publicly released for research use\" 但未给出具体 license，不如 Few-NERD 明确。\n\n---\n\n## Questions（需作者回答）\n\n1. **SCS with definitions**: 是否尝试过用 \"type name: definition\" 全文计算 SCS？如果有，结果如何？如果没有，这是有意的设计选择还是遗漏？\n2. **Amplification mechanism**: 能否提供 simulation evidence 证明 pairwise r²=1.5% 在给定 batch size 和 pair correlation structure 下确实期望产生 R²=22%+ 的 batch-level 效应？\n3. **Within-pool power**: 80-pool 16-sub 的 quartile Δ CI [−8.17, +0.38] 跨零。如果增加 random subsets 从 100 到 500 或 1000，是否预期 CI 会收窄到不跨零？\n4. **FewRel contamination**: 从 training split 采样的 relation 的准确率是否系统性高于 validation split 的 relation？\n5. **Prompt v2 attenuation**: v2 gap 从 31.2pp 降至 25.5pp（−5.7pp）。这 −5.7pp 中有多少归因于 BCS range 缩窄（v2 sampling: 0.36–0.80 vs v1: 0.47–0.97），多少归因于 prompt 本身的改进？能否用相同 BCS range 对比两个 prompt？\n\n---\n\n## 主要优势\n\n1. **研究问题有清晰的实用价值**：首次系统分离 count 和 confusability 两条退化通道，对实际的 schema 设计有直接指导意义。\n2. **BCS-controlled 实验设计优雅**：固定 count 变 BCS 的范式有效控制了最主要的混淆因素，within-pool design 进一步排除 pool composition confound。\n3. **负面结果的诚实报告**：SDGD 的失败、merge amplification 的诊断、p=0.19 的 batch composition 结果均如实报告，未选择性隐藏不利证据。\n4. **多数据集多任务覆盖**：跨 NER/RE (sentence + document)/ED 四任务四数据集，结论的覆盖面较广。\n5. **Centrality confound 的识别与处理**：§4.5 对 MAVEN 的 centrality confound 分析深入，partial correlation 控制做得仔细，对未来研究有方法论参考价值。\n6. **统计报告规范**：CIs、permutation tests、effect sizes 均有报告，优于大多数 NLP 论文。",
  "reviewer_id": "1",
  "project": "schema-dag-extraction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## 总体评分\n**Overall**: 3.5 / 5（介于 Resubmit next cycle 和 Accept 之间，偏向 Accept with revisions）\n**一句话总结**: 研究问题有价值、实验设计有创意，但 SCS 指标存在构造缺陷（name-only vs. prompt 实际包含 definitions），核心统计叙事在 headline 数字（31.2pp）和 practical magnitude（2.2pp）之间存在张力，两模型验证不足以支撑 \"cross-model replication\" 的 claim。\n\n## 官方维度打分（来自 ACL ARR Review Form, Feb 2025+）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3/5 | 核心指标 SCS 的构造前提与实验设置矛盾（详见 N1）；统计推断从 r²=1.5% 到 31.2pp 的放大逻辑需更严格论证；多项关键条件未达显著性 |\n| Excitement | 4/5 | 首次系统分离 count vs. confusability 两条退化通道，研究问题对零样本 IE 社区有直接实用价值 |\n| Overall | 3.5/5 | 选题好、设计巧，但方法论缺陷若不修复会影响结论可信度 |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] SCS 指标构造与实验设置之间的逻辑矛盾\n\n- 具体位置：§3.2 第56行 \"Both use type name strings only, without definitions or descriptions, **to reflect the information available to the model at inference time**\"（强调为原文）；Appendix §F (prompt_appendix.tex) 第28-32行明确显示 prompt 格式为 `- {type_1}: {definition_1}`\n- 问题：论文以 \"反映推理时模型可用信息\" 为理由仅用 type name 计算 SCS。但 prompt 模板明确表明模型推理时看到的是 **name + definition**，而非仅 name。因此 SCS 实际测量的是 type name 的 embedding 相似度，而非模型决策时面对的完整信息的相似度。两个 type name 相近但 definition 能有效区分的类型对（如 \"person-artist\" vs. \"person-athlete\"，定义差异大）可能被 SCS 标记为高混淆，但模型实际并不混淆。反之，name 不同但 definition 相似的类型对会被漏标。\n- 为什么影响接收：SCS 是全文两大范式（count curve 的 BCS 聚合、BCS-controlled experiment 的分组依据）的核心度量。如果 proxy 的构造前提本身有误，所有基于 BCS 分层的实验结论的效度存疑。\n- 建议修改方向：(1) 用 \"name + definition\" 拼接后的 embedding 重新计算 SCS，对比 name-only 结果；(2) 如保留 name-only，需修改理由——改为 \"name-only SCS 是 lightweight pre-hoc proxy，虽不完全匹配推理时信息，但实证验证表明与观测混淆率相关\"（论文已有部分此类语言，但需去除 §3.2 的错误理由）。\n\n**N2** [critical] Headline 数字 31.2pp 与 practical magnitude 2.2pp 之间的叙事失衡\n\n- 具体位置：Abstract 第4行 \"the gap reaches 31.2 pp\"；§4.3 Practical magnitude 段 \"the typical BCS span (IQR = 0.054) yields an expected accuracy gap of 2.2 pp\"\n- 问题：Abstract/Introduction 突出 31.2pp 作为核心结果，但这是 **extreme-batch construction**（刻意选取 BCS 分布两端极端值）的产物。对 practitioner 而言，随机 schema 下的预期影响仅 2.2pp（Table 5 quartile Δ = 3.9pp）。论文在 §4.3 有诚实讨论，但 framing 仍可能误导读者高估效应实用规模。\n- 为什么影响接收：ACL ARR soundness 标准要求 claim 与证据匹配。如果 abstract 传达的印象是 \"confusability 导致 31.2pp 退化\"，而实际 typical 影响仅 ~2pp，这构成 overclaim。\n- 建议修改方向：Abstract 中应同时报告 extreme-batch gap 和 typical-batch gap，例如 \"quartile gap of −5.3 pp under typical batching (reaching −31.2 pp under extreme BCS contrast)\"。\n\n**N3** [critical] r²=1.3–1.7% → batch-level R²=22–53% 的 \"amplification\" 论证不严格\n\n- 具体位置：§4.3 Practical magnitude 最后一句 \"Pair-level r²=1.5% aggregates to batch-level R²=22–53% across datasets, a 14–35× amplification consistent with averaging over ~C(k,2) correlated pair effects per batch\"\n- 问题：这一放大并非简单的统计聚合效应。Pair-level r² 描述的是单一 type pair 的 SCS 对该 pair 混淆率的解释力；batch-level R² 描述的是 batch 的 mean BCS 对该 batch 整体准确率的解释力。两者度量的对象不同（pair confusion rate vs. batch accuracy）且受不同混杂因素影响。论文用 \"consistent with averaging over ~C(k,2) correlated pair effects\" 一带而过，但没有给出：(1) 在什么相关结构下这种放大成立的数学推导或模拟验证；(2) 排除 batch-level R² 来自其他 batch-level confounders（如 batch 内 type frequency 分布、type definition 长度等）的可能性。\n- 为什么影响接收：这个 amplification 叙事是论文 \"modest pairwise effect 仍有实用意义\" 的核心支柱。如果聚合效应的归因不正确，整条推理链断裂。\n- 建议修改方向：(1) 用 simulation 验证：给定 pairwise r=0.12 和观测到的 pair-pair 相关矩阵，模拟 batch-level R² 的期望分布；(2) 明确区分 pair-level 和 batch-level 分析的 claim 范围，不要将二者用单一 \"amplification\" 叙事串联。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] \"Cross-model replication\" claim 仅基于两个模型\n\n- 具体位置：§4.1 \"Cross-model replication\"段；§4.3 \"Cross-model validation\"段；Table 1/2\n- 问题：Qwen3-32B 和 Llama-3.1-8B-Instruct 在模型规模（32B vs 8B）和架构上同时不同。Channel 2 在 8B NER 上出现 floor effects 无法检测。两个模型不足以支撑 \"cross-model replication\" 这一术语的通常含义（暗示现象在模型间广泛成立）。\n- 建议：改为 \"cross-model consistency check\" 或 \"preliminary cross-model evidence\"，并在 Limitations 中明确说明不能排除 model-specific artifacts。\n\n**W2** [warning] Bootstrap CIs 的非独立观测问题未充分处理\n\n- 具体位置：§4.2 Table 2 \"CIs are pair-level percentile bootstrap (B=1,000)\"；同段提到 \"Type-level cluster bootstrap yields wider but still significant CIs\"\n- 问题：Pairwise SCS 的 bootstrap 单位应为 type（每个 type 参与多个 pair），而非 pair。论文确实提到了 cluster bootstrap 并报告了更宽的 CI，但 (1) 主表（Table 2）仍报告的是 pair-level bootstrap CI，cluster bootstrap 仅在正文中一笔带过；(2) 没有说明 cluster bootstrap 的聚类变量是什么（按单一 type？按 type pair 共享的某一 type？）。\n- 建议：主表应报告 cluster-robust CI（或至少双报），并明确 cluster 定义。\n\n**W3** [warning] Within-pool quartile Δ 的 CI 跨零 + full 80-rel condition p=0.762\n\n- 具体位置：Table 5 — 80-pool→16-sub quartile Δ CI = [−8.17, +0.38]；full 80-rel slope p=0.762\n- 问题：论文的 within-pool control 是关键设计——用于排除 pool composition confound。但该条件的 quartile Δ CI 跨零，regression 虽显著 (p=0.027) 但 borderline。Full 80-rel condition 完全不显著。论文将后者归因于 BCS range 不足，但另一种解释是：当 type pool 固定（不能自由选择 extreme types）时，confusability 效应消失或极小。这与 extreme-batch 结果的可推广性直接相关。\n- 建议：(1) 增加 80-pool 内的 BCS variation 方法（如更大的 subsample n 或不同的 subset size）来提升 power；(2) 如不可补实验，需在正文（不仅 appendix）明确讨论 generalizability 的限制。\n\n**W4** [warning] FewRel 使用 training + validation split 合并数据\n\n- 具体位置：§3.1 FewRel 段 \"we combine the training and validation splits to obtain the full 80-relation pool\"\n- 问题：FewRel 的 training split 有 64,000 instances across 64 relations（每 relation 700 instances），validation 有 16,000 instances across 16 relations。合并后从 training split 采样的实例可能与模型预训练数据重叠（Qwen3/Llama 的训练数据未公开）。论文未讨论数据泄露风险。\n- 建议：(1) 讨论 contamination 风险并进行简单检验（如对比 train-split 和 val-split 来源的 relation 在 accuracy 上的差异）；(2) 说明为何不使用仅 validation split 的 16-relation 子集进行核心分析。\n\n**W5** [warning] SDGD 的 RE batch composition 结论过于弱化为 \"contribution\"\n\n- 具体位置：§5 最后段 \"+1.4 pp that is directionally consistent but not statistically significant (p ≈ 0.19)\"；Introduction Contribution (4) 将此列为贡献\n- 问题：n=1（单一 graph coloring 配置）、BCS margin 仅 0.006、p=0.19——这本质上是 null result。论文诚实报告了这一点，但仍将其框架为 \"贡献\" 之一，措辞 \"directionally consistent\" 暗示支持假说。统计学上，p=0.19 下的方向一致性没有信息量。\n- 建议：将 Contribution (4) 重新框架为 \"negative/inconclusive finding on confusability-aware grouping\"，不要使用 \"directionally consistent\" 这样的措辞。或者增加 n（多种 graph-coloring 方案/阈值），使结论具有统计基础。\n\n**W6** [warning] v1 vs v2 的选择性报告\n\n- 具体位置：§4 开头 \"Unless otherwise noted, all experiments in this section use the v1 prompt\"；§3.4 描述 v1 有 96.5% hallucinated offsets\n- 问题：v1 prompt 导致 96.5% 的 offset 幻觉，表明模型在 v1 下输出质量有问题。论文主要基于 v1 结果，理由是 v1 是初始版本。但如果 v2 是更合理的 prompt 设计（减少幻觉、提升精度），那么核心结论应该基于 v2 验证。当前做法相当于基于已知有缺陷的实验设置建立结论，再用改进设置做 sensitivity check。\n- 建议：说明为什么选择 v1 作为 primary（如果是因为 v1 effect size 更大则需承认这一点），或者将 v2 结果提升为同等地位。\n\n---\n\n## 小问题（不影响接收）\n\n- §3.2：\"to reflect the information available to the model at inference time\" 这一表述即使修改 SCS 构造理由后仍需删除，因为与事实不符。\n- Table 1 (BCS-controlled)：16-rel condition 无 CI（仅一个 extreme batch per level），应在表内注明 n=1 限制。已有脚注但容易忽略。\n- §4.1 MAVEN：relaxed F1 increases 的解释涉及三个因素（relaxed matching、same-domain hierarchy、class imbalance），未区分各因素贡献，分析偏定性。\n- Limitations 第5条 \"FewRel combines training and validation splits for 80 types and characterizes classification accuracy rather than end-to-end extraction\" 似在为 FewRel 非端到端性质辩解，但更重要的 limitation 是 data contamination 风险（W4）。\n- Checklist B2：\"FewRel, DocRED, and MAVEN are publicly released for research use\" 但未给出具体 license，不如 Few-NERD 明确。\n\n---\n\n## Questions（需作者回答）\n\n1. **SCS with definitions**: 是否尝试过用 \"type name: definition\" 全文计算 SCS？如果有，结果如何？如果没有，这是有意的设计选择还是遗漏？\n2. **Amplification mechanism**: 能否提供 simulation evidence 证明 pairwise r²=1.5% 在给定 batch size 和 pair correlation structure 下确实期望产生 R²=22%+ 的 batch-level 效应？\n3. **Within-pool power**: 80-pool 16-sub 的 quartile Δ CI [−8.17, +0.38] 跨零。如果增加 random subsets 从 100 到 500 或 1000，是否预期 CI 会收窄到不跨零？\n4. **FewRel contamination**: 从 training split 采样的 relation 的准确率是否系统性高于 validation split 的 relation？\n5. **Prompt v2 attenuation**: v2 gap 从 31.2pp 降至 25.5pp（−5.7pp）。这 −5.7pp 中有多少归因于 BCS range 缩窄（v2 sampling: 0.36–0.80 vs v1: 0.47–0.97），多少归因于 prompt 本身的改进？能否用相同 BCS range 对比两个 prompt？\n\n---\n\n## 主要优势\n\n1. **研究问题有清晰的实用价值**：首次系统分离 count 和 confusability 两条退化通道，对实际的 schema 设计有直接指导意义。\n2. **BCS-controlled 实验设计优雅**：固定 count 变 BCS 的范式有效控制了最主要的混淆因素，within-pool design 进一步排除 pool composition confound。\n3. **负面结果的诚实报告**：SDGD 的失败、merge amplification 的诊断、p=0.19 的 batch composition 结果均如实报告，未选择性隐藏不利证据。\n4. **多数据集多任务覆盖**：跨 NER/RE (sentence + document)/ED 四任务四数据集，结论的覆盖面较广。\n5. **Centrality confound 的识别与处理**：§4.5 对 MAVEN 的 centrality confound 分析深入，partial correlation 控制做得仔细，对未来研究有方法论参考价值。\n6. **统计报告规范**：CIs、permutation tests、effect sizes 均有报告，优于大多数 NLP 论文。",
    "reviewer_id": "1",
    "project": "schema-dag-extraction"
  }
}
```

</details>

---


### Tool result

_source line 295 · 2026-05-16T11:20:59.977400+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3968
}
```

</details>

---


### Assistant

_source line 296 · 2026-05-16T11:21:07.308236+00:00_

Round 1 审稿完成，已提交至 Review Director。

核心发现：论文研究问题有价值（首次分离 count vs. confusability 两条退化通道），实验设计有创意（BCS-controlled paradigm），但存在三个 critical 问题：(1) SCS 仅用 type name 计算与 prompt 实际包含 definitions 矛盾；(2) 31.2pp headline 数字 vs. 2.2pp typical effect 的叙事失衡；(3) pairwise r²→batch R² 的 amplification 缺乏严格论证。建议 3.5/5，偏向 accept with revisions。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1"
}
```

</details>

---


## Round 10

## Round 10

4 recorded events


### User

_source line 297 · 2026-05-16T11:23:57.612694+00:00_

[Round 1 审稿请求]:
## 交叉分享 — 请逐条回应 Reviewer 2 和 Reviewer 3 的审稿意见

请对以下两位 Reviewer 的每个 Must-Fix 和 Should-Fix 问题逐条回应：
- **[AGREE]**：同意该问题存在，说明理由
- **[REBUT]**：不同意或认为问题程度被高估，提供证据（cite 具体 Section/Table/Figure）

---

## Reviewer 2 完整审稿意见（新颖性 + Related Work + Framing）

### Overall: 3.5/5

### Must-Fix

**R2-N1** [critical] SCS 新颖性声称过强——与 LLM-PEE embedding similarity 的区分不够本质
- SCS 定义为 cos(embed(name_i), embed(name_j))（§4.2 Eq.1），与 LLM-PEE 使用 type embedding similarity 进行 schema partitioning 技术上同构。Introduction "introducing the Schema Confusability Score (SCS)" 暗示 novel metric，实际是 cosine similarity 重命名 + batch-level 聚合。

**R2-N2** [critical] 因果语言超出实验设计
- 全文 "degradation operates through two separable channels"；"Channel 1 (count → recall decline) and Channel 2 (confusability → type confusion)"；Contribution #1 "independently degrade"。箭头和 "channel" 暗示因果，但 Limitations #6 自认 correlational evidence。BCS-controlled 未控制 type frequency / definition quality / prompt position。

**R2-N3** [critical] Contribution #1 声称 "across NER, RE, and ED" 但 MAVEN (ED) 是反例
- MAVEN count curve 增长（F1 0.106→0.247），§5.1 和 §5.4 解释了反转，但 Contribution #1 仍声称 "degrade...across...ED"。

### Should-Fix

**R2-W1** [warning] RE batch composition +1.4pp (p≈0.19) 被列为 Contribution #4
- p=0.19、n=1、rank 13/15 seeds，本质是 null result，不应列为贡献。

**R2-W2** [warning] Title 疑问句式与论文结论匹配度
- 实际答案是 "partially, under specific conditions"，疑问句暗示明确 yes。

**R2-W3** [warning] "Both channels replicate on Llama-3.1-8B" 表述误导
- Limitations #1 说 Channel 2 在 8B NER 上 floor effects。"both channels replicate" 仅限 RE。

**R2-W4** [warning] Related Work 遗漏 SGD (Rastogi 2020) 和 DST schema scaling 文献

**R2-W5** [warning] Pairwise r²=1.3-1.7% 的 framing 不够坦诚
- Abstract/Intro 中 "the first factor empirically isolated" 让人误以为效应量实质性，r² 未在 abstract 报告。

**R2-W6** [warning] 31.2pp extreme-batch gap 的 prominence 与 typical-batch 2.2pp 不成比例
- 31.2pp 出现至少 7 次，2.2pp 仅 3 次。

### Missing References
1. Rastogi et al. 2020 (SGD, AAAI)
2. Lee et al. 2022 (SGD-X, AAAI)
3. Li et al. 2023 (ChatGPT IE evaluation)
4. Volkanovska et al. 2024 (LLM NER error taxonomy)

---

## Reviewer 3 完整审稿意见（写作质量 + 格式 + Reproducibility）

### Overall: 3/5

### Must-Fix

**R3-N1** [critical] 参考文献时间线不一致——多条引用在提交日期后才存在
- reflect-learn-2026 (arXiv 2025-08), gliner2-2025 (arXiv 2025-07), llm-pee-2025, crossagentie-2025, slot-2025 均在 ACL ARR May 2025 截止日之后。

**R3-N2** [critical] DocRED 采样数量正文未明确说明
- FewRel 写了 "1,000 balanced instances (12-13 per type)"，DocRED 仅 "sample balanced instances"。

### Should-Fix

**R3-W1** [warning] §5 SDGD 篇幅严重不足——核心 RQ3 仅约半页
- Table 8 和 confidence gating 全在 Appendix，正文仅概述。

**R3-W2** [warning] 正文仅 2 个 figure
- figures 目录有 fig_sdgd_comparison.pdf 未使用。

**R3-W3** [warning] Abstract 数字密度过高

**R3-W4** [warning] Discussion + Conclusion 过于单薄

**R3-W5** [warning] vLLM 版本号 v0.20.2 存疑

**R3-W6** [warning] p-value 格式不统一

### Minor Issues
- M1: CI 标注不统一
- M2: Figure 引用路径问题
- M3: Checklist A4 AI assistant 声明模糊
- M4: FewRel train+val 合并 justification 不足
- M5: Table 4 脚注 null result 不够显著
- M6: DocRED prompt template 缺失
- M7: "SDGD" 中 "DAG" 与实际无向图不一致
- M8: "floor effects" 未解释

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 298 · 2026-05-16T11:26:05.271241+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## 交叉回应：Reviewer 2 审稿意见\n\n---\n\n### Must-Fix\n\n**[AGREE] R2-N1: SCS 新颖性声称过强**\n\n同意。SCS 在技术实现层面确实是 cosine similarity 的命名包装，与 LLM-PEE 的 type embedding partitioning 使用相同的底层计算。论文的真正贡献不在 metric 本身，而在 **controlled experimental paradigm**（固定 count 变 BCS、within-pool control）。但 Introduction 第10行 \"introducing the Schema Confusability Score (SCS)\" 的措辞确实暗示 metric 本身是 novel contribution。\n\n建议作者将 \"introducing SCS\" 改为 \"operationalizing type confusability via SCS\" 并在 §2 Related Work 中明确承认与 LLM-PEE 在度量层面的技术等价性，强调区分在于 **分析性使用（controlled isolation）** vs. **工程性使用（schema partitioning）**。\n\n补充我自己的发现：SCS 还有更本质的问题——它仅用 type name 计算 embedding similarity，但 prompt 实际包含 definitions（见我的 N1）。这比 novelty framing 问题更严重。\n\n---\n\n**[AGREE] R2-N2: 因果语言超出实验设计**\n\n同意，但认为 severity 介于 critical 和 warning 之间。\n\n证据：\n- §4.4 \"These results establish two channels: Channel 1 (count → recall decline) and Channel 2 (confusability → type confusion)\" 使用箭头暗示因果\n- Contribution #1 \"independently degrade\" 隐含因果独立性\n- Limitations #6 自认 \"correlational evidence with controlled stratification\"\n\nBCS-controlled 实验确实比纯相关分析更强——它固定 count 变 BCS，属于 **stratified controlled comparison**，高于 observational correlation 但低于 intervention/do-calculus 意义上的因果推断。具体而言：\n- FewRel 的 balanced design（每 type 700 instances）控制了 type frequency\n- Within-pool design 控制了 pool composition\n- 但 **definition quality**（高 BCS type pairs 可能有更相似/更难区分的 definitions）和 **prompt position effects** 未控制\n\n建议：将 \"channels\" 改为 \"degradation patterns/components\"，将 \"→\" 改为 \"associated with\"，将 \"independently degrade\" 改为 \"separately predict degradation\"。保留 stratified design 相对于纯 observational 的优势论述。\n\n---\n\n**[REBUT] R2-N3: MAVEN 作为反例使 \"across NER, RE, and ED\" 失实**\n\n部分不同意 severity 为 critical。\n\n论文在 §4.5 明确识别了 MAVEN 的 centrality confound 并做了详尽分析（Appendix D, Table 6 partial correlation）。关键区分：\n- **Count curve（Channel 1）**: MAVEN 确实是反例——F1 随 count 增加。Contribution #1 声称 \"count...degrade...across...ED\" 不准确。\n- **Pairwise confusability（Channel 2）**: MAVEN 的 pairwise SCS-confusion correlation **仍然显著** ($r = 0.129$, $p < 10^{-10}$; Table 2)。问题出在 per-type aggregation（mean BCS）而非底层关系。\n\n因此我认为：\n- R2 对 Contribution #1 措辞的批评 **成立**——应改为 \"degrade NER and RE; ED exhibits a centrality confound that reverses count-curve trends but preserves pairwise confusability signals\"\n- 但 severity 不应为 critical，因为论文并未隐瞒此结果，而是专门用一整个 subsection (§4.5) + appendix 进行分析\n- 修改 contribution 措辞即可解决，不涉及核心实验有效性\n\n---\n\n### Should-Fix\n\n**[AGREE] R2-W1: RE batch composition +1.4pp 不应列为 Contribution**\n\n完全同意。我在自己的审稿中也指出了同一问题（我的 W5）。p=0.19, n=1, rank 13/15 seeds——这是 null result。将其框架为 \"contribution\" 不合适。应改为 \"negative/inconclusive finding\" 或从 contribution list 中删除，合并到 §5 的 failure analysis 中。\n\n---\n\n**[REBUT] R2-W2: Title 疑问句式与结论不匹配**\n\n不同意。疑问句式 title 在 NLP/ML 论文中常见（\"Does X do Y?\"），其功能是 framing research question 而非暗示答案为 yes。论文的答案 \"partially, under specific conditions\" 是典型的 nuanced empirical finding，与疑问句 title 完全兼容。参见 ACL 近年高引论文如 \"Are Sixteen Heads Really Better than One?\" (Voita et al. 2019)——答案也是 \"partially\"。此问题不影响论文质量。\n\n---\n\n**[AGREE] R2-W3: \"Both channels replicate on Llama-3.1-8B\" 表述误导**\n\n同意。§4.1 Summary 段 \"Both channels replicate on Llama-3.1-8B\" 与 Limitations #1 \"Channel 2 was not robustly detectable on NER at 8B scale\" 直接矛盾。准确表述应为 \"Channel 1 replicates fully; Channel 2 replicates on RE but shows floor effects on 8B NER\"。Conclusion 中也有类似问题（\"both channels replicate across model families on RE\" 这个限定词 \"on RE\" 在括号中太隐蔽）。\n\n---\n\n**[AGREE] R2-W4: Related Work 遗漏 SGD 相关文献**\n\n部分同意。SGD (Rastogi et al. 2020) 研究 dialogue state tracking 中的 schema scaling，虽非 IE 任务但涉及 LLM 在大 schema 下的退化，与本文主题相关。SGD-X (Lee et al. 2022) 更直接——它研究 schema 变体对 DST 的影响，本质上也是 \"confusability\" 的一种形式。建议在 §2 \"Schema complexity in IE\" 段末加一句 bridge：\"Schema scaling challenges extend beyond IE to dialogue systems (SGD; Lee et al. 2022), though controlled isolation of confusability from count has not been attempted in prior work.\"\n\nLi et al. 2023 (ChatGPT IE evaluation) 和 Volkanovska et al. 2024 不确定是否必要引用——前者是 evaluation survey，后者是 error taxonomy。如果 Volkanovska 的 error taxonomy 与本文的 IntraSub/Missed 分类高度相关则应引用。\n\n---\n\n**[AGREE] R2-W5: r²=1.3-1.7% framing 不够坦诚**\n\n同意，且与我的 N2 和 N3 互补。Abstract 中 \"the first factor empirically isolated\" 让读者预期有实质效应量，但 pairwise r² 仅 1.3-1.7%。Abstract 报告了 batch-level R² (0.22–0.53) 但未报告 pairwise r²，这构成选择性呈现。建议 abstract 中至少加入 \"pairwise effect sizes remain modest (r²=1.3–1.7%)\" 以平衡读者预期。\n\n---\n\n**[AGREE] R2-W6: 31.2pp prominence 与 typical 2.2pp 不成比例**\n\n完全同意。这与我的 N2 高度重叠。31.2pp 在 abstract、introduction、§4.3、conclusion 中反复出现，而 practical magnitude 2.2pp 仅在 §4.3 一个段落中报告。建议 abstract 和 conclusion 中始终将 extreme-batch gap 与 typical-batch gap 并列报告。\n\n---\n\n## 交叉回应：Reviewer 3 审稿意见\n\n---\n\n### Must-Fix\n\n**[AGREE] R3-N1: 引用时间线不一致**\n\n同意这是一个问题，但 severity 取决于具体 arXiv 上线日期。\n\n- ACL ARR May 2025 deadline: 2025-05-25\n- 如果 reflect-learn-2026 确实是 2025-08 才上线的 arXiv，则投稿时不可能引用\n- 类似地，如果 gliner2-2025 是 2025-07 上线，也不可能\n\n但需注意：\n1. 部分 \"2025\" 引用可能是 2024 年底已上 arXiv 的 preprint，bibtex year 字段设为 venue 的 publication year\n2. \"reflect-learn-2026\" 如果 year 字段确实是 2026 则明显不可能在 2025-05 前引用\n\n这种问题要么说明：(a) 投稿日期不是 May 2025（修订后重投？），或 (b) 引用存在伪造/预引用。无论哪种情况都需要作者解释。我同意这是 critical issue（如果确认引用在投稿时不存在）。\n\n---\n\n**[AGREE] R3-N2: DocRED 采样数量未明确**\n\n同意。§3.1 FewRel 段明确写 \"1,000 balanced instances (12–13 per relation type, stratified)\"，但 DocRED 段仅 \"We sample balanced instances\"。这不符合 reproducibility 要求。读者无法判断是 1,000 还是其他数量、每 type 多少、document-level 采样策略（按 document 还是按 entity pair）。Table 1 的 \"# Eval Units\" 列也没有给 DocRED 具体数字（需要回查——实际上 Table 1 确实写了 \"1,000\"，但正文描述缺失是问题）。\n\n建议：正文中补充 \"(1,000 balanced instances, ~10 per relation type)\" 或类似表述，并说明是 entity-pair level 还是 document level sampling。\n\n---\n\n### Should-Fix\n\n**[REBUT] R3-W1: §5 SDGD 篇幅不足**\n\n部分不同意。§5 的简洁是有意的设计选择：SDGD 是 **negative result**（所有 decomposition 均低于 single-pass baseline），核心信息是诊断性的（merge amplification）。将 Table 8、confidence gating 细节全放正文会挤占 positive results 的空间。Appendix B (SDGD Full Protocol) 提供了完整细节。\n\n但我同意 §5 可以再多 2-3 句话来更好地连接 RQ3 和具体实验结果。当前从 \"We test this\" 直接跳到数字，缺少对 reader 的 signposting。\n\n---\n\n**[AGREE] R3-W2: 正文仅 2 个 figure**\n\n同意这对一篇实验密集的论文来说偏少。特别是 error taxonomy (Table 3/Figure 2) 和 BCS-controlled results 用 figure 展示比 table 更直观。如果确实有 fig_sdgd_comparison.pdf 未使用，应考虑纳入正文（如果页数允许）。\n\n---\n\n**[REBUT] R3-W3: Abstract 数字密度过高**\n\n部分不同意。对于 empirical paper，abstract 提供具体数字是 ACL 社区的常见做法（cf. 大多数 empirical NLP paper 的 abstract 都包含 baseline vs. proposed 的具体数字）。本文的问题不在于数字多，而在于数字的 **选择性**（如 R2-W5/W6 指出的 31.2pp vs 2.2pp framing 问题）。如果修改 framing 使关键数字更均衡，数字密度本身不是问题。\n\n---\n\n**[AGREE] R3-W4: Discussion + Conclusion 单薄**\n\n同意。Discussion 仅三段（boundary conditions、practitioner guidance、future directions），缺少：\n- 与 in-context learning scaling laws 的联系\n- 对 \"为什么 cosine similarity 能预测 confusion\" 的 mechanistic intuition\n- Broader impact on schema design tools 的讨论\n\nConclusion 也基本是 results summary 的压缩版。建议扩展 Discussion 1-2 段。\n\n---\n\n**[AGREE] R3-W5: vLLM v0.20.2 存疑**\n\n同意。截至 2025 年 5 月，公开发布的 vLLM 版本号为 0.4.x–0.6.x 范围。v0.20.2 格式上看起来像一个不存在的版本号。可能的解释：(1) 作者混淆了版本号（可能是 v0.2.2 或 v0.5.2）；(2) internal fork with different versioning。无论如何，这需要核实——如果版本号错误，影响 reproducibility。\n\n---\n\n**[AGREE] R3-W6: p-value 格式不统一**\n\n同意。论文中混合使用了：\n- $p < 10^{-6}$（科学记数法）\n- $p < 0.001$\n- $p = 0.027$\n- $p \\approx 0.19$\n\n建议统一为：精确值报 $p = X.XXX$（3位小数），极小值报 $p < 10^{-k}$ 或 $p < 0.001$，约等于避免使用。\n\n---\n\n### Minor Issues 选择性回应\n\n**[AGREE] R3-M7: \"SDGD\" 中 \"DAG\" 与实际无向图不一致**\n\n这是一个有意义的命名问题。§B (Appendix) 描述 \"thresholded confusability graph G = (V, E)\" 使用 greedy graph coloring——这是 **无向图** 操作。\"DAG\" (Directed Acyclic Graph) 暗示有向无环结构，与实际实现不符。应改为 \"Schema-Graph-Guided Decomposition (SGGD)\" 或直接删除 \"DAG\" 改为 \"Schema-Guided Decomposition (SGD)\"。\n\n**[AGREE] R3-M4: FewRel train+val 合并 justification 不足**\n\n同意，且与我的 W4 重叠。论文需要讨论 contamination 风险。\n\n**[REBUT] R3-M8: \"floor effects\" 未解释**\n\n\"Floor effects\" 是心理学/统计学的标准术语，指测量值接近量表下限导致无法检测差异。对 NLP 审稿人可能不熟悉，但在 ACL 近年论文中已有使用。加一个简短括号解释即可 \"(i.e., baseline performance too low to detect further degradation)\"，不需要改术语。",
  "reviewer_id": "1",
  "project": "schema-dag-extraction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## 交叉回应：Reviewer 2 审稿意见\n\n---\n\n### Must-Fix\n\n**[AGREE] R2-N1: SCS 新颖性声称过强**\n\n同意。SCS 在技术实现层面确实是 cosine similarity 的命名包装，与 LLM-PEE 的 type embedding partitioning 使用相同的底层计算。论文的真正贡献不在 metric 本身，而在 **controlled experimental paradigm**（固定 count 变 BCS、within-pool control）。但 Introduction 第10行 \"introducing the Schema Confusability Score (SCS)\" 的措辞确实暗示 metric 本身是 novel contribution。\n\n建议作者将 \"introducing SCS\" 改为 \"operationalizing type confusability via SCS\" 并在 §2 Related Work 中明确承认与 LLM-PEE 在度量层面的技术等价性，强调区分在于 **分析性使用（controlled isolation）** vs. **工程性使用（schema partitioning）**。\n\n补充我自己的发现：SCS 还有更本质的问题——它仅用 type name 计算 embedding similarity，但 prompt 实际包含 definitions（见我的 N1）。这比 novelty framing 问题更严重。\n\n---\n\n**[AGREE] R2-N2: 因果语言超出实验设计**\n\n同意，但认为 severity 介于 critical 和 warning 之间。\n\n证据：\n- §4.4 \"These results establish two channels: Channel 1 (count → recall decline) and Channel 2 (confusability → type confusion)\" 使用箭头暗示因果\n- Contribution #1 \"independently degrade\" 隐含因果独立性\n- Limitations #6 自认 \"correlational evidence with controlled stratification\"\n\nBCS-controlled 实验确实比纯相关分析更强——它固定 count 变 BCS，属于 **stratified controlled comparison**，高于 observational correlation 但低于 intervention/do-calculus 意义上的因果推断。具体而言：\n- FewRel 的 balanced design（每 type 700 instances）控制了 type frequency\n- Within-pool design 控制了 pool composition\n- 但 **definition quality**（高 BCS type pairs 可能有更相似/更难区分的 definitions）和 **prompt position effects** 未控制\n\n建议：将 \"channels\" 改为 \"degradation patterns/components\"，将 \"→\" 改为 \"associated with\"，将 \"independently degrade\" 改为 \"separately predict degradation\"。保留 stratified design 相对于纯 observational 的优势论述。\n\n---\n\n**[REBUT] R2-N3: MAVEN 作为反例使 \"across NER, RE, and ED\" 失实**\n\n部分不同意 severity 为 critical。\n\n论文在 §4.5 明确识别了 MAVEN 的 centrality confound 并做了详尽分析（Appendix D, Table 6 partial correlation）。关键区分：\n- **Count curve（Channel 1）**: MAVEN 确实是反例——F1 随 count 增加。Contribution #1 声称 \"count...degrade...across...ED\" 不准确。\n- **Pairwise confusability（Channel 2）**: MAVEN 的 pairwise SCS-confusion correlation **仍然显著** ($r = 0.129$, $p < 10^{-10}$; Table 2)。问题出在 per-type aggregation（mean BCS）而非底层关系。\n\n因此我认为：\n- R2 对 Contribution #1 措辞的批评 **成立**——应改为 \"degrade NER and RE; ED exhibits a centrality confound that reverses count-curve trends but preserves pairwise confusability signals\"\n- 但 severity 不应为 critical，因为论文并未隐瞒此结果，而是专门用一整个 subsection (§4.5) + appendix 进行分析\n- 修改 contribution 措辞即可解决，不涉及核心实验有效性\n\n---\n\n### Should-Fix\n\n**[AGREE] R2-W1: RE batch composition +1.4pp 不应列为 Contribution**\n\n完全同意。我在自己的审稿中也指出了同一问题（我的 W5）。p=0.19, n=1, rank 13/15 seeds——这是 null result。将其框架为 \"contribution\" 不合适。应改为 \"negative/inconclusive finding\" 或从 contribution list 中删除，合并到 §5 的 failure analysis 中。\n\n---\n\n**[REBUT] R2-W2: Title 疑问句式与结论不匹配**\n\n不同意。疑问句式 title 在 NLP/ML 论文中常见（\"Does X do Y?\"），其功能是 framing research question 而非暗示答案为 yes。论文的答案 \"partially, under specific conditions\" 是典型的 nuanced empirical finding，与疑问句 title 完全兼容。参见 ACL 近年高引论文如 \"Are Sixteen Heads Really Better than One?\" (Voita et al. 2019)——答案也是 \"partially\"。此问题不影响论文质量。\n\n---\n\n**[AGREE] R2-W3: \"Both channels replicate on Llama-3.1-8B\" 表述误导**\n\n同意。§4.1 Summary 段 \"Both channels replicate on Llama-3.1-8B\" 与 Limitations #1 \"Channel 2 was not robustly detectable on NER at 8B scale\" 直接矛盾。准确表述应为 \"Channel 1 replicates fully; Channel 2 replicates on RE but shows floor effects on 8B NER\"。Conclusion 中也有类似问题（\"both channels replicate across model families on RE\" 这个限定词 \"on RE\" 在括号中太隐蔽）。\n\n---\n\n**[AGREE] R2-W4: Related Work 遗漏 SGD 相关文献**\n\n部分同意。SGD (Rastogi et al. 2020) 研究 dialogue state tracking 中的 schema scaling，虽非 IE 任务但涉及 LLM 在大 schema 下的退化，与本文主题相关。SGD-X (Lee et al. 2022) 更直接——它研究 schema 变体对 DST 的影响，本质上也是 \"confusability\" 的一种形式。建议在 §2 \"Schema complexity in IE\" 段末加一句 bridge：\"Schema scaling challenges extend beyond IE to dialogue systems (SGD; Lee et al. 2022), though controlled isolation of confusability from count has not been attempted in prior work.\"\n\nLi et al. 2023 (ChatGPT IE evaluation) 和 Volkanovska et al. 2024 不确定是否必要引用——前者是 evaluation survey，后者是 error taxonomy。如果 Volkanovska 的 error taxonomy 与本文的 IntraSub/Missed 分类高度相关则应引用。\n\n---\n\n**[AGREE] R2-W5: r²=1.3-1.7% framing 不够坦诚**\n\n同意，且与我的 N2 和 N3 互补。Abstract 中 \"the first factor empirically isolated\" 让读者预期有实质效应量，但 pairwise r² 仅 1.3-1.7%。Abstract 报告了 batch-level R² (0.22–0.53) 但未报告 pairwise r²，这构成选择性呈现。建议 abstract 中至少加入 \"pairwise effect sizes remain modest (r²=1.3–1.7%)\" 以平衡读者预期。\n\n---\n\n**[AGREE] R2-W6: 31.2pp prominence 与 typical 2.2pp 不成比例**\n\n完全同意。这与我的 N2 高度重叠。31.2pp 在 abstract、introduction、§4.3、conclusion 中反复出现，而 practical magnitude 2.2pp 仅在 §4.3 一个段落中报告。建议 abstract 和 conclusion 中始终将 extreme-batch gap 与 typical-batch gap 并列报告。\n\n---\n\n## 交叉回应：Reviewer 3 审稿意见\n\n---\n\n### Must-Fix\n\n**[AGREE] R3-N1: 引用时间线不一致**\n\n同意这是一个问题，但 severity 取决于具体 arXiv 上线日期。\n\n- ACL ARR May 2025 deadline: 2025-05-25\n- 如果 reflect-learn-2026 确实是 2025-08 才上线的 arXiv，则投稿时不可能引用\n- 类似地，如果 gliner2-2025 是 2025-07 上线，也不可能\n\n但需注意：\n1. 部分 \"2025\" 引用可能是 2024 年底已上 arXiv 的 preprint，bibtex year 字段设为 venue 的 publication year\n2. \"reflect-learn-2026\" 如果 year 字段确实是 2026 则明显不可能在 2025-05 前引用\n\n这种问题要么说明：(a) 投稿日期不是 May 2025（修订后重投？），或 (b) 引用存在伪造/预引用。无论哪种情况都需要作者解释。我同意这是 critical issue（如果确认引用在投稿时不存在）。\n\n---\n\n**[AGREE] R3-N2: DocRED 采样数量未明确**\n\n同意。§3.1 FewRel 段明确写 \"1,000 balanced instances (12–13 per relation type, stratified)\"，但 DocRED 段仅 \"We sample balanced instances\"。这不符合 reproducibility 要求。读者无法判断是 1,000 还是其他数量、每 type 多少、document-level 采样策略（按 document 还是按 entity pair）。Table 1 的 \"# Eval Units\" 列也没有给 DocRED 具体数字（需要回查——实际上 Table 1 确实写了 \"1,000\"，但正文描述缺失是问题）。\n\n建议：正文中补充 \"(1,000 balanced instances, ~10 per relation type)\" 或类似表述，并说明是 entity-pair level 还是 document level sampling。\n\n---\n\n### Should-Fix\n\n**[REBUT] R3-W1: §5 SDGD 篇幅不足**\n\n部分不同意。§5 的简洁是有意的设计选择：SDGD 是 **negative result**（所有 decomposition 均低于 single-pass baseline），核心信息是诊断性的（merge amplification）。将 Table 8、confidence gating 细节全放正文会挤占 positive results 的空间。Appendix B (SDGD Full Protocol) 提供了完整细节。\n\n但我同意 §5 可以再多 2-3 句话来更好地连接 RQ3 和具体实验结果。当前从 \"We test this\" 直接跳到数字，缺少对 reader 的 signposting。\n\n---\n\n**[AGREE] R3-W2: 正文仅 2 个 figure**\n\n同意这对一篇实验密集的论文来说偏少。特别是 error taxonomy (Table 3/Figure 2) 和 BCS-controlled results 用 figure 展示比 table 更直观。如果确实有 fig_sdgd_comparison.pdf 未使用，应考虑纳入正文（如果页数允许）。\n\n---\n\n**[REBUT] R3-W3: Abstract 数字密度过高**\n\n部分不同意。对于 empirical paper，abstract 提供具体数字是 ACL 社区的常见做法（cf. 大多数 empirical NLP paper 的 abstract 都包含 baseline vs. proposed 的具体数字）。本文的问题不在于数字多，而在于数字的 **选择性**（如 R2-W5/W6 指出的 31.2pp vs 2.2pp framing 问题）。如果修改 framing 使关键数字更均衡，数字密度本身不是问题。\n\n---\n\n**[AGREE] R3-W4: Discussion + Conclusion 单薄**\n\n同意。Discussion 仅三段（boundary conditions、practitioner guidance、future directions），缺少：\n- 与 in-context learning scaling laws 的联系\n- 对 \"为什么 cosine similarity 能预测 confusion\" 的 mechanistic intuition\n- Broader impact on schema design tools 的讨论\n\nConclusion 也基本是 results summary 的压缩版。建议扩展 Discussion 1-2 段。\n\n---\n\n**[AGREE] R3-W5: vLLM v0.20.2 存疑**\n\n同意。截至 2025 年 5 月，公开发布的 vLLM 版本号为 0.4.x–0.6.x 范围。v0.20.2 格式上看起来像一个不存在的版本号。可能的解释：(1) 作者混淆了版本号（可能是 v0.2.2 或 v0.5.2）；(2) internal fork with different versioning。无论如何，这需要核实——如果版本号错误，影响 reproducibility。\n\n---\n\n**[AGREE] R3-W6: p-value 格式不统一**\n\n同意。论文中混合使用了：\n- $p < 10^{-6}$（科学记数法）\n- $p < 0.001$\n- $p = 0.027$\n- $p \\approx 0.19$\n\n建议统一为：精确值报 $p = X.XXX$（3位小数），极小值报 $p < 10^{-k}$ 或 $p < 0.001$，约等于避免使用。\n\n---\n\n### Minor Issues 选择性回应\n\n**[AGREE] R3-M7: \"SDGD\" 中 \"DAG\" 与实际无向图不一致**\n\n这是一个有意义的命名问题。§B (Appendix) 描述 \"thresholded confusability graph G = (V, E)\" 使用 greedy graph coloring——这是 **无向图** 操作。\"DAG\" (Directed Acyclic Graph) 暗示有向无环结构，与实际实现不符。应改为 \"Schema-Graph-Guided Decomposition (SGGD)\" 或直接删除 \"DAG\" 改为 \"Schema-Guided Decomposition (SGD)\"。\n\n**[AGREE] R3-M4: FewRel train+val 合并 justification 不足**\n\n同意，且与我的 W4 重叠。论文需要讨论 contamination 风险。\n\n**[REBUT] R3-M8: \"floor effects\" 未解释**\n\n\"Floor effects\" 是心理学/统计学的标准术语，指测量值接近量表下限导致无法检测差异。对 NLP 审稿人可能不熟悉，但在 ACL 近年论文中已有使用。加一个简短括号解释即可 \"(i.e., baseline performance too low to detect further degradation)\"，不需要改术语。",
    "reviewer_id": "1",
    "project": "schema-dag-extraction"
  }
}
```

</details>

---


### Tool result

_source line 299 · 2026-05-16T11:26:09.339967+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4068
}
```

</details>

---


### Assistant

_source line 300 · 2026-05-16T11:26:17.117669+00:00_

已提交交叉回应。总结：

- **R2 的 3 个 Must-Fix**：同意 N1（SCS novelty overclaim）和 N2（causal language），部分反驳 N3（MAVEN 反例的 severity 应降级为 warning，因论文已充分讨论）
- **R2 的 6 个 Should-Fix**：同意 W1/W3/W4/W5/W6，反驳 W2（疑问句 title 是常规做法）
- **R3 的 2 个 Must-Fix**：同意 N1（引用时间线）和 N2（DocRED 采样未明确）
- **R3 的 6 个 Should-Fix**：同意 W2/W4/W5/W6，部分反驳 W1（SDGD 篇幅短是因为 negative result）和 W3（abstract 数字密度本身不是问题，选择性才是）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1"
}
```

</details>

---


## Round 11

## Round 11

34 recorded events


### User

_source line 301 · 2026-05-16T13:48:52.128201+00:00_

[Round 1 审稿请求]:
## Round 1 审稿任务 — Reviewer 1

**你的审查侧重：方法论 + 实验严谨性 + 统计分析**

### Venue 信息
- **目标**: ACL ARR May 2025, Main Conference Long Paper
- **页数限制**: ≤ 8 页正文（Limitations/References/Appendix 不计入）
- **匿名规则**: Double-blind
- **模板**: ACL style template `[review]` 模式

### 论文路径
`projects/schema-dag-extraction/docs/paper/main.tex`
（含 abstract.tex, introduction.tex, related_work.tex, experimental_setup.tex, results.tex, sdgd_negative.tex, discussion.tex, checklist.tex, prompt_appendix.tex 等子文件）

### 论文概要
本文研究 training-free LLM IE 中 schema 复杂度导致的性能下降，提出 Schema Confusability Score (SCS) 和 Batch Confusability Score (BCS)，在 NER/RE/ED 三个任务四个数据集上进行 controlled study，声称分离出两个降级通道（count-driven recall decline 和 confusability-driven type substitution）。

### 你需要重点审查的方面

1. **SCS/BCS 定义的合理性**：
   - 用 type name embedding cosine similarity 作为 confusability proxy 是否充分？
   - BCS 用 mean 聚合 vs max 的选择是否合理？
   - SCS 验证实验（name-only vs name+def）是否充分？

2. **实验设计的严谨性**：
   - Count Curves 和 BCS-Controlled 两个实验范式能否真正分离 count 和 confusability？
   - 每个 count level 仅 5 个 random batches 是否足够？
   - BCS-controlled 中 "extreme batch" 构造方式是否引入偏差？
   - Within-pool 分析是否充分控制了 pool composition confound？

3. **统计分析的正确性**：
   - Bootstrap CI 的使用是否恰当（percentile method, B=1000）？
   - Permutation test for slope equivalence 是否合适？
   - Partial correlation 控制 centrality confound 是否充分？
   - Effect size 报告是否完整（r, r², CI, p-value）？
   - 多重比较问题是否存在？

4. **因果推断的力度**：
   - 论文声称 "separable degradation channels" — 证据是否支持因果而非仅相关？
   - "two-channel model" 这个框架是否有过强的因果暗示？

5. **Cross-model validation 的充分性**：
   - 仅 2 个模型（Qwen3-32B + Llama-3.1-8B）是否足够？
   - 缺少闭源模型验证的影响？

6. **SDGD 负结果的分析**：
   - Merge amplification 的诊断是否令人信服？
   - Oracle routing 作为 "performance ceiling" 的论证是否严密？

请产出结构化审稿意见：Summary → Strengths → Weaknesses → Questions → Minor Issues。每个 Weakness 标注严重程度（Critical / Major / Minor）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 302 · 2026-05-16T13:49:01.316924+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebSearch,mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebSearch,mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director",
    "max_results": "3"
  }
}
```

</details>

---


### Tool result

_source line 303 · 2026-05-16T13:49:01.367450+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 304 · 2026-05-16T13:49:04.832281+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL ARR 2025 reviewer guidelines review form criteria scoring"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR 2025 reviewer guidelines review form criteria scoring"
  }
}
```

</details>

---


### Tool call

_source line 305 · 2026-05-16T13:49:05.735712+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 306 · 2026-05-16T13:49:06.038014+00:00_

1	\documentclass[11pt]{article}
2	
3	\usepackage[review]{acl}
4	
5	\usepackage{times}
6	\usepackage{latexsym}
7	\usepackage[T1]{fontenc}
8	\usepackage[utf8]{inputenc}
9	\usepackage{microtype}
10	\usepackage{graphicx}
11	\usepackage{booktabs}
12	\usepackage{amsmath}
13	\usepackage{enumitem}
14	\usepackage[normalem]{ulem}
15	\usepackage{listings}
16	
17	\title{Does Type Confusability Shape Schema-Induced Degradation\\in Training-Free LLM Information Extraction?}
18	
19	\author{Anonymous}
20	
21	\begin{document}
22	\maketitle
23	
24	\input{abstract}
25	
26	\input{introduction}
27	
28	\input{related_work}
29	
30	\input{experimental_setup}
31	
32	\input{results}
33	
34	\input{sdgd_negative}
35	
36	\input{discussion}
37	
38	\section*{Limitations}
39	\begin{enumerate}[leftmargin=*,itemsep=2pt]
40	\item \textbf{Model coverage.} Primary experiments use Qwen3-32B with cross-model validation on Llama-3.1-8B-Instruct. Whether patterns hold for proprietary models (GPT-4, Gemini) remains unverified. Channel~2 was not robustly detectable on NER at 8B scale, likely due to floor effects.
41	
42	\item \textbf{Modest pairwise effect size.} Pairwise SCS explains 1.3--1.7\% of type confusion variance; entity frequency, prompt position, mention ambiguity, and type definition quality likely account for the remainder.
43	
44	\item \textbf{Non-significant factorial test.} Within-dataset count $\times$ BCS interaction on Few-NERD did not reach significance (Appendix~\ref{sec:appendix_factorial}); cross-pool slope consistency suggests confusability sensitivity is stable rather than amplifying.
45	
46	\item \textbf{Decomposition and metric scope.} RE batch composition is tested on FewRel only; NER merge alternatives remain unexplored. SCS relies on embedding cosine similarity; label entropy or ontological depth may capture complementary dimensions.
47	
48	\item \textbf{RE format specificity.} RE's clean channel separation may reflect its closed-set classification format. FewRel combines traini
…[truncated 24429 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 302
}
```

</details>

---


### Tool result

_source line 307 · 2026-05-16T13:49:12.592115+00:00_

Web search results for query: "ACL ARR 2025 reviewer guidelines review form criteria scoring"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"aclrollingreview/reviewerguidelines.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/reviewerguidelines.md"},{"title":"ACLRollingReview (@ReviewAcl) / X","url":"https://x.com/reviewacl"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"aclrollingreview/reviewing.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/reviewing.md"}]

Based on the search results, here's information about ACL ARR 2025 reviewer guidelines, review form criteria, and scoring:

## Scoring System

Starting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation. The soundness scores must be justified by the text of the review.

## K
…[truncated 1285 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 7759
}
```

</details>

---


### Tool call

_source line 308 · 2026-05-16T13:49:18.368966+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review review form 2025 soundness excitement scoring scale 1-5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review review form 2025 soundness excitement scoring scale 1-5"
  }
}
```

</details>

---


### Tool call

_source line 309 · 2026-05-16T13:49:20.278003+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 310 · 2026-05-16T13:49:20.629446+00:00_

1	\begin{abstract}
2	Training-free LLM information extraction degrades as schema complexity grows. We conduct the first controlled study isolating type confusability from type count across NER, RE (a closed-set classification task), and event detection on four datasets, introducing the Schema Confusability Score (SCS) and two paradigms: count curves varying schema size while randomizing confusability, and BCS-controlled experiments fixing size while varying confusability.
3	
4	We identify two empirically separable degradation channels: count-driven recall decline and confusability-driven type substitution. For RE, the quartile BCS gap is $-$5.3\,pp (95\% CI: [$-$7.4, $-$3.2]); typical random batches differ by ${\approx}\,2.2$\,pp. Under extreme-batch construction (a methodological upper-bound), the gap reaches 31.2\,pp. Batch-level BCS explains $R^2 = 0.22\text{--}0.53$ of accuracy variance as an aggregated signal, while pairwise effect sizes remain modest ($r^2 = 1.3\text{--}1.7\%$). The effect is directionally consistent across prompt designs, with attenuated magnitude under improved prompts. Channel~1 replicates fully on Llama-3.1-8B; Channel~2 replicates on RE but shows floor effects on 8B NER. Count increases generally suppress extraction on cross-domain schemas; MAVEN's same-domain schema exhibits centrality confounding that reverses this trend. Schema decomposition via oracle routing recovers count-based degradation for RE (+29.8\,pp over single-pass), but confusability-aware grouping yields no significant additional gain (+1.4\,pp, $p\approx 0.19$).
5	\end{abstract}
6	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 351
}
```

</details>

---


### Tool call

_source line 311 · 2026-05-16T13:49:20.629822+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 312 · 2026-05-16T13:49:21.181748+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	Training-free LLM information extraction---prompting a large language model with a target schema and asking it to extract structured information without any task-specific fine-tuning---enables rapid deployment across new domains and ontologies. This zero-shot paradigm eliminates the need for labeled data, making it attractive for applications where annotation is expensive or schemas evolve frequently \cite{llm4ie-survey-2024}. Yet the paradigm carries a critical limitation: performance degrades sharply as the number of candidate types in the prompt schema grows. On named entity recognition, recall drops from 0.72 with a single candidate type to 0.42 with 64 types, a 42\% relative decline. On relation extraction, accuracy falls from 85.7\% with one relation to 50.4\% with 80 relations (sentence-level) and from 88.0\% to 38.7\% with 96 relations (document-level)---near or exceeding halving. This degradation is not academic: real-world ontologies routinely define 50--200+ types, placing them squarely in the regime where training-free extraction becomes unreliable.
5	
6	What causes this degradation? Prior decomposition strategies \cite{uniner-2024,llm-pee-2025,parse-2025} conflate two mechanisms: having more types to discriminate among (count) and having semantically similar types to confuse (confusability). None isolates which factor predicts the gains (\S\ref{sec:related_work}).
7	
8	We ask three questions. \textbf{RQ1}: Does type confusability independently predict extraction degradation beyond the effect of type count? \textbf{RQ2}: Through what mechanisms do count and confusability each degrade performance? \textbf{RQ3}: Can confusability-aware schema decomposition improve extraction quality?
9	
10	We conduct the first controlled study isolating type confusability from type count across NER, RE, and event detection (ED). We operationalize confusability via the \emph{Schema Confusability Score} (SCS)---pairwis
…[truncated 2442 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 551
}
```

</details>

---


### Tool call

_source line 313 · 2026-05-16T13:49:21.232375+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 314 · 2026-05-16T13:49:21.433680+00:00_

1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{Training-free LLM IE.}
5	Training-free LLM IE spans instruction tuning \cite{instructuie-2023}, code-style schema encoding \cite{knowcoder-2024,codeie-2023}, annotation-guided extraction \cite{gollie-2024,adelie-2024}, schema-driven decoding \cite{slot-2025,oneke-2025}, and constrained JSON decoding \cite{json-schema-bench-2025}. For NER, methods include zero-shot decomposition \cite{xie-zeroshot-ner-2023,promptner-2023}, distillation \cite{uniner-2024}, and bidirectional encoders \cite{gliner-2024,gliner2-2025}. For RE, recent work examines zero-shot relation triplet extraction via prompting \cite{relationprompt-2022} and revisits relation extraction in the LLM era \cite{wadhwa-re-llm-2023}. These methods perform well with moderate schemas (4--20 types) but none investigates how performance degrades as schema complexity scales, nor proposes quantitative metrics for inter-type confusability.
6	
7	\paragraph{Schema complexity in IE.}
8	The most directly related work is LLM-PEE \cite{llm-pee-2025}, which partitions large event schemas by type embedding similarity. Our work differs in three ways: (1)~we conduct controlled analysis to understand \emph{why} extraction degrades rather than developing an engineering solution; (2)~our BCS-controlled experiments isolate count from confusability, which LLM-PEE conflates; (3)~our SDGD experiments reveal that merge amplification---not partitioning quality---is the bottleneck in decompose-then-merge pipelines. Other approaches address schema complexity via hard negative mining \cite{iepile-2024}, schema definition optimization \cite{parse-2025}, multi-agent debate \cite{crossagentie-2025,cmas-ner-2025}, schema-aware decomposition for event extraction \cite{dee-2024}, and active prompting \cite{reflect-learn-2026}; all treat it as an engineering problem rather than isolating the underlying degradation mechanisms.
9	
10	\paragraph{Schema complexity in dialogue and
…[truncated 1156 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 201
}
```

</details>

---


### Tool result

_source line 315 · 2026-05-16T13:49:26.125136+00:00_

Web search results for query: "ACL Rolling Review review form 2025 soundness excitement scoring scale 1-5"

Links: [{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"aclrollingreview/reviewerguidelines.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/reviewerguidelines.md"},{"title":"aclrollingreview/acguidelines.md at main · yoshitomo-matsubara/aclrollingreview","url":"https://github.com/yoshitomo-matsubara/aclrollingreview/blob/main/acguidelines.md"},{"title":"ACL 2023 Acceptance Recommendations - ACL 2023","url":"https://2023.aclweb.org/blog/overall-recommendation/"},{"title":"ACL 2026 on X: \"Checkout the blog post on the soundness/excitement scores https://t.co/AKSO9DjiYP . It clarifies the reasoning behind the separation of overall scores and how it might make the reviewer recommendation more robust. #ACL2023Toronto #ACL2023NLP #NLProc\" / X","url":"https://x.com/aclmeeting/status/1637827267173953540"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"Conference Decisions · GitHub","url":"https://gist.github.com/antonisa/2158dee79179c7c49304ef353887bfa0"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"}]

Based on the search results, here's what I found about the ACL Rolling Review (ARR) review form fo
…[truncated 1624 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 7756
}
```

</details>

---


### Tool call

_source line 316 · 2026-05-16T13:49:30.493149+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/experimental_setup.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/experimental_setup.tex"
  }
}
```

</details>

---


### Tool result

_source line 317 · 2026-05-16T13:49:30.794959+00:00_

1	\section{Experimental Setup}
2	\label{sec:experimental_setup}
3	
4	We evaluate how prompt schema size and inter-type confusability affect zero-shot LLM extraction across three information extraction tasks and four datasets: named entity recognition (NER), sentence-level relation extraction (RE), document-level RE, and event detection (ED).
5	
6	\subsection{Tasks and Datasets}
7	\label{sec:datasets}
8	
9	\paragraph{Few-NERD (NER).}
10	Few-NERD \cite{fewnerd-2021} provides 66 fine-grained entity types organized into 8 coarse categories (person, location, organization, building, art, product, event, other). The dataset spans diverse domains, making it suitable for cross-domain evaluation. We sample 1{,}000 test instances and evaluate with token-level text matching.
11	
12	\paragraph{FewRel (RE).}
13	FewRel \cite{fewrel-2018} contains 80 relation types sourced from Wikidata. Since the validation split covers only 16 relations, we combine the training and validation splits to obtain the full 80-relation pool required for schema-scale experiments, and sample 1{,}000 balanced instances (12--13 per relation type, stratified to ensure equal representation). Each instance provides a sentence with marked head and tail entities; the task is to classify the relation.
14	
15	\paragraph{DocRED (Document-level RE).}
16	DocRED \cite{docred-2019} contains 96 relation types sourced from Wikidata, evaluated at the document level where entity pairs may span multiple sentences. We sample 1{,}000 instances balanced across 96 relation types ($\sim$10 per type) from the DocRED development set and formulate the task identically to FewRel: given a document with marked head and tail entities, classify the relation. DocRED extends the RE evaluation to a larger schema (96 vs.\ 80 types) and document-level context, testing whether confusability effects persist under longer input contexts and cross-sentence reasoning.
17	
18	\paragraph{MAVEN (ED).}
19	MAVEN \cite{maven-2020} defines 168 event ty
…[truncated 6514 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 318 · 2026-05-16T13:49:30.795411+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex"
  }
}
```

</details>

---


### Tool result

_source line 319 · 2026-05-16T13:49:30.996625+00:00_

1	\section{Results}
2	\label{sec:results}
3	
4	Unless otherwise noted, all experiments in this section use the v1 prompt (\S\ref{sec:model}; full templates in Appendix~\ref{sec:appendix_prompts}).
5	
6	\subsection{Count-Degradation Curves}
7	\label{sec:count_curves}
8	
9	\begin{figure}[t]
10	\centering
11	\begin{minipage}[t]{0.48\columnwidth}
12	\centering
13	\includegraphics[width=\linewidth]{../../figures/paper/fig_count_curves.pdf}
14	\end{minipage}
15	\hfill
16	\begin{minipage}[t]{0.48\columnwidth}
17	\centering
18	\includegraphics[width=\linewidth]{../../figures/paper/fig_bcs_scaling.pdf}
19	\end{minipage}
20	\caption{\textbf{(a)} Count-degradation curves across four datasets. NER recall generally declines and RE accuracy (both FewRel and DocRED) declines monotonically with schema size; MAVEN relaxed F1 increases (\S\ref{sec:centrality_confound}). \textbf{(b)} BCS-controlled FewRel accuracy. The BCS--accuracy slope is consistent across the independent 16-relation pool and within-pool 16-relation subsets (permutation $p = 0.60$); the wider BCS range available at 80 relations produces larger absolute gaps.}
21	\label{fig:main_results}
22	\end{figure}
23	
24	Figure~\ref{fig:main_results}a shows extraction quality degrades monotonically with schema size across three datasets: Few-NERD recall drops from 0.72 to 0.42 ($-$42\%), FewRel accuracy from 85.7\% to 50.4\% ($-$35.3\,pp), and DocRED from 88.0\% to 38.7\% ($-$56\%). MAVEN exhibits a reversed trend attributable to centrality confounding (\S\ref{sec:centrality_confound}). The effect replicates on Llama-3.1-8B-Instruct ($-$43\,pp on Few-NERD; per-batch $r = 0.725$; Table~\ref{tab:cross_model}), indicating schema configuration rather than model-specific factors predicts difficulty.
25	
26	\subsection{Pairwise Confusability and Type Confusion}
27	\label{sec:pairwise}
28	
29	We test whether pairwise SCS predicts type-level confusion rates. For each type pair $(t_i, t_j)$, we compute the confusion rate---the fraction
…[truncated 8556 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 320 · 2026-05-16T13:49:30.997126+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/sdgd_negative.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/sdgd_negative.tex"
  }
}
```

</details>

---


### Tool result

_source line 321 · 2026-05-16T13:49:31.047700+00:00_

1	\section{Schema Decomposition: Failure, Diagnosis, and Mitigation}
2	\label{sec:sdgd}
3	
4	A natural intervention against confusability-driven degradation is to partition the schema so that confusable types never co-occur in the same prompt. We test this idea with \textbf{Schema-DAG-Guided Decomposition} (SDGD\footnote{SDGD (Schema Decomposition and Grouping for Degradation mitigation) is an internal project designation; the graph structure is undirected.}), which uses greedy graph coloring on the pairwise SCS graph to assign types to low-confusability batches.
5	
6	We construct a thresholded confusability graph $G = (V, E)$ where each type is a vertex and an edge connects types $t_i, t_j$ whenever $\text{SCS}(t_i, t_j) > \tau$. Greedy graph coloring (\textsc{largest\_first}) assigns each type to a color such that no two adjacent---i.e., highly confusable---types share a batch. Each color class forms one extraction batch. For NER, predictions from all batches are merged via set union; for RE, each instance is routed to the batch containing its gold type (oracle routing). We test four NER modes: (i)~\textbf{single\_pass}, the undecomposed baseline; (ii)~\textbf{sdgd\_zero}, SCS-guided partitioning; (iii)~\textbf{random\_batch}, random partitioning with matched batch sizes; and (iv)~\textbf{per\_type}, each type extracted in isolation. Every mode falls below the single-pass NER baseline: SDGD obtains F1\,=\,0.251, random batching 0.320, per-type 0.292, versus 0.445 for single-pass (Table~\ref{tab:sdgd_results}, Appendix~\ref{sec:appendix_sdgd}).
7	
8	\paragraph{Merge amplification in NER.}
9	The core failure mechanism is \emph{merge amplification}: presenting the same text to the model $k$ times with different type subsets causes each pass to independently generate entity predictions, and union merge accumulates all of them into a single output. Each pass produces an independent set of span predictions; because LLM outputs are not calibrated across passes \cite{llm-
…[truncated 4314 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 322 · 2026-05-16T13:49:36.367585+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 323 · 2026-05-16T13:49:36.819671+00:00_

1	\section{Discussion}
2	\label{sec:discussion}
3	
4	\paragraph{Boundary conditions.}
5	The two-channel model applies to cross-domain schemas; same-domain schemas (e.g., MAVEN's FrameNet-derived event types) exhibit centrality confounding that obscures per-type aggregated signals, requiring pairwise SCS or centrality adjustment (\S\ref{sec:centrality_confound}). High-BCS accuracy converges to $\approx$51\% across tested models, suggesting a task-inherent difficulty ceiling. RE's clean channel separation may partly reflect its closed-set format; the effect generalizes to document-level RE (DocRED slope $-$0.71). Prompt design modulates but does not eliminate the effect (v2 gap: $-$25.5\,pp vs.\ v1: $-$31.2\,pp; Appendix~\ref{sec:appendix_prompt_sensitivity}).
6	
7	\paragraph{Why does embedding similarity predict LLM confusion?}
8	Type name embeddings capture semantic proximity in the same representational space that LLMs use for in-context type resolution. When two type names are close in embedding space, we hypothesize that the model's attention mechanism may produce overlapping key--query representations for those types, increasing the probability of substitution errors. This mechanistic link explains why a simple cosine similarity metric predicts extraction failures: high SCS directly indexes the degree of representational overlap that causes confusion during decoding. Critically, the pair-level effect is modest ($R^2 \approx 7\%$ over non-zero confusion pairs) because individual substitution events are stochastic and influenced by many factors beyond type similarity. However, pairs sharing a common type exhibit correlated SCS values ($\rho = 0.35$), so when multiple high-SCS pairs co-occur in a batch, their effects aggregate constructively: noise averages out while the confusability signal is preserved. Monte Carlo simulation confirms that this inter-pair correlation produces an effective amplification of ${\sim}3\times$, yielding batch-level $R^2 \approx 22\%$ f
…[truncated 3252 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 324 · 2026-05-16T13:49:36.870425+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/checklist.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/checklist.tex"
  }
}
```

</details>

---


### Tool result

_source line 325 · 2026-05-16T13:49:36.921268+00:00_

1	\section*{Responsible NLP Research Checklist}
2	
3	For each question, the answer is \textbf{Yes}, \textbf{No}, or \textbf{N/A}. If Yes, the relevant section is indicated. If No, a justification is provided.
4	
5	\subsection*{A \quad For Every Submission}
6	
7	\begin{enumerate}[label=\textbf{A\arabic*.},leftmargin=*,itemsep=4pt]
8	
9	\item \textbf{Did you describe the limitations of your work?}
10	
11	Yes. The Limitations section (after \S\ref{sec:conclusion}) discusses single-model reliance, modest pairwise effect sizes, cross-pool slope consistency, non-significant factorial results, decomposition scope, and metric scope.
12	
13	\item \textbf{Did you discuss any potential risks of your work?}
14	
15	N/A. This is a purely analytical study of schema-induced degradation in existing LLM IE systems. It does not introduce new models, datasets, or deployment-facing artifacts. The findings characterize failure modes and are intended to inform safer schema design.
16	
17	\item \textbf{Do the abstract and introduction summarize the paper's main claims?}
18	
19	Yes. The abstract and \S\ref{sec:introduction} state the two-channel degradation pattern (count and confusability), the cross-model consistency check, and the negative SDGD result.
20	
21	\item \textbf{Did you use AI assistants (e.g., ChatGPT, Copilot) when working on this paper?}
22	
23	Yes. An AI coding assistant was used for experiment scripting and LaTeX formatting. All scientific claims, experimental design, and analysis were conducted by the authors.
24	
25	\end{enumerate}
26	
27	\subsection*{B \quad Scientific Artifacts}
28	
29	\begin{enumerate}[label=\textbf{B\arabic*.},leftmargin=*,itemsep=4pt]
30	
31	\item \textbf{Did you cite the creators of artifacts you used?}
32	
33	Yes. Few-NERD \cite{fewnerd-2021}, FewRel \cite{fewrel-2018}, MAVEN \cite{maven-2020}, Qwen3-32B \cite{qwen3-2025}, Meta-Llama-3.1-8B-Instruct, vLLM \cite{vllm-2023}, and all-MiniLM-L6-v2 \cite{minilm-2020} are cited in \S\ref{sec:datasets} 
…[truncated 4372 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 326 · 2026-05-16T13:49:41.239023+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebFetch",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebFetch",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 327 · 2026-05-16T13:49:41.239376+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 328 · 2026-05-16T13:49:41.590956+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/prompt_appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/prompt_appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 329 · 2026-05-16T13:49:41.641745+00:00_

1	\lstset{
2	  basicstyle=\ttfamily\small,
3	  breaklines=true,
4	  breakatwhitespace=true,
5	  columns=fullflexible
6	}
7	
8	\section{Prompt Templates}
9	\label{sec:appendix_prompts}
10	
11	This appendix reproduces the complete prompt templates used for all three extraction tasks.
12	All prompts are injected into a single \texttt{user} message (no system prompt); the model's chat template adds the system/assistant framing.
13	Both versions provide a JSON-formatted type schema to the vLLM constrained-decoding engine; the schema is \emph{not} included in the natural-language prompt itself.
14	We use greedy decoding (\texttt{temperature=0}, \texttt{seed=42}) throughout.
15	
16	\medskip\noindent
17	\textbf{Notation.}
18	Placeholders are shown in \texttt{\{braces\}}.
19	Text \textbf{added in v2} (relative to v1) is marked with $\triangleright$.
20	Text \textbf{removed in v2} is marked with \sout{strikethrough}.
21	
22	\subsection{Named Entity Recognition (Few-NERD)}
23	
24	\paragraph{v1 prompt (with character offsets).}
25	
26	\begin{small}
27	\begin{lstlisting}
28	Extract all named entities from the following text.
29	Only extract entities of the following types:
30	- {type_1}: {definition_1}
31	- {type_2}: {definition_2}
32	  ...
33	
34	Text: {input_text}
35	
36	Output as JSON: [{"text": "...", "type": "...",
37	                  "start": ..., "end": ...}]
38	\end{lstlisting}
39	\end{small}
40	
41	\noindent
42	\textbf{v1 constrained-decoding schema:}
43	\begin{small}
44	\begin{lstlisting}
45	{"type": "array",
46	 "items": {"type": "object",
47	   "properties": {
48	     "text":  {"type": "string"},
49	     "type":  {"type": "string",
50	               "enum": [&lt;sorted_types>]},
51	     "start": {"type": "integer"},
52	     "end":   {"type": "integer"}},
53	   "required": ["text","type","start","end"]}}
54	\end{lstlisting}
55	\end{small}
56	
57	\paragraph{v2 prompt (text+type only).}
58	
59	\begin{small}
60	\begin{lstlisting}
61	Extract all named entities from the foll
…[truncated 5190 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 330 · 2026-05-16T13:49:46.629175+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete review form structure: all scoring dimensions, their scales (1-5), descriptions for each score level, and any other required fields (confidence, best paper recommendation, etc.). List everything in detail."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the complete review form structure: all scoring dimensions, their scales (1-5), descriptions for each score level, and any other required fields (confidence, best paper recommendation, etc.). List everything in detail."
  }
}
```

</details>

---


### Tool result

_source line 331 · 2026-05-16T13:49:52.458750+00:00_

# ACL Rolling Review Form Structure

## Core Scoring Dimensions

**1. Soundness** (1-5 scale)
- 5: "Excellent: This study is one of the most thorough I have seen"
- 4: Strong with sufficient support; minor experiments optional
- 3: Acceptable with main claims supported; minor details needed
- 2: Poor; main claims lack sufficient support
- 1: "Major Issues: This study is not yet sufficiently thorough to warrant publication"

**2. Excitement** (1-5 scale)
- 5: "Highly Exciting: I would recommend this paper to others"
- 4: Exciting; would mention to colleagues
- 3: Interesting; might attend presentation
- 2: Potentially interesting to some community members
- 1: "Not Exciting: this paper does not resonate with me"

**3. Overall Assessment** (1-5 scale)
- 5: Consider for Award (top 2.5%)
- 4: Conference acceptance
- 3: Findings acceptance
- 2: Resubmit next cycle
- 1: Do not resubmit

## Required Text Fields

- Paper Summary
- Summary of Strengths
- Summary of Weaknesses (numbered)
- Comments/Suggestions/Typos
- Best Paper Justification (conditional)

## Supporting Metrics

**Reviewer Confidence** (1-5)
**Reproducibility** (1-5)
**Datasets Value** (1-5, if applicable)
**Software Value** (1-5, if applicable)
**Author Identity Knowledge** (1-5)

## Additional Required Sections

- Limitations and Societal Impact assessment
- Ethical Concerns review
- Ethics Review necessity determination

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 5829
}
```

</details>

---


### Tool call

_source line 332 · 2026-05-16T13:52:36.083944+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 1 — Round 1 审稿意见\n\n**论文**: \"Does Type Confusability Shape Schema-Induced Degradation in Training-Free LLM Information Extraction?\"\n**侧重**: 方法论 + 实验严谨性 + 统计分析\n\n---\n\n## 总体评分\n\n**Overall**: 3 (Findings acceptance)\n**一句话总结**: 实验设计精细、统计报告透明，但核心 claim（\"separable channels\"）缺乏形式统计支撑，且实际效应量之小（typical batch gap 仅 2.2pp）削弱了研究的实践意义。\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3/5 | 核心 factorial test 不显著(p=0.50)、Channel 2 在 8B NER 上不可复现、pairwise R²仅1.3-1.7%。但 controlled stratification 设计合理，统计报告诚实。 |\n| Excitement | 3/5 | 研究问题有实践价值，centrality confound 分析是新颖贡献，但 negative SDGD 结果和微弱 effect size 限制了对社区的直接帮助。 |\n| Reproducibility | 4/5 | 实验细节充分（prompt template、decoding params、seed），承诺 release 代码，但代码尚未提供。 |\n| Confidence | 4/5 | 本人熟悉 zero-shot IE、LLM evaluation 方法学和统计检验。 |\n\n---\n\n## Summary\n\n本文研究 training-free LLM IE 中 schema 规模增大导致的性能下降，提出 SCS（pairwise cosine similarity）和 BCS（batch-level mean SCS）量化 type confusability，通过 count curves 和 BCS-controlled 两种实验范式在 4 个数据集上分析，声称分离出 count-driven recall decline 和 confusability-driven type substitution 两个降级通道。同时报告了 SDGD（schema decomposition）的 negative result，诊断 merge amplification 为 NER 分解失败的原因。\n\n---\n\n## 主要优势\n\n1. **精良的 controlled design**: 固定 count 变 BCS、固定 BCS 变 count 的范式在 zero-shot IE 文献中属首次，within-pool analysis 额外控制 pool composition confound，实验逻辑链完整。\n\n2. **统计报告的透明度**: 非显著结果（factorial $p=0.50$, SDGD +1.4pp $p≈0.19$, within-pool quartile CI 过零）、modest effect sizes（$r^2=1.3$–$1.7\\%$）、floor effects 均如实报告，未做 cherry-picking。\n\n3. **Centrality confound 分析（§5.5 + Appendix D）**: 识别 MAVEN 上 per-type BCS 正相关为 spurious signal，通过 partial correlation 控制 log-frequency 和 degree centrality 后信号消失，同时保留 pairwise signal——这是对社区有方法论价值的贡献。\n\n4. **Pair-to-batch aggregation simulation（Appendix F）**: 用 Monte Carlo 验证 pair-level $R^2=7\\%$ 如何经 inter-pair correlation ($\\rho=0.35$) 聚合到 batch-level $R^2≈22\\%$，定量解释了微弱个体信号如何产生可检测的批次效应。\n\n5. **Negative result 的价值**: SDGD 失败的诊断（merge amplification: precision 0.563→0.210）机制清晰、有实践警示价值。\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [Critical] **Factorial test 不显著与 \"separable channels\" 声称矛盾**\n\n- 具体位置：Appendix C（§A.3），Limitations item 3，Abstract/Introduction \"two empirically separable degradation channels\"\n- 问题：论文核心 claim 是 count 和 confusability 构成 \"empirically separable\" 的两个降级通道。但唯一的形式 separability 检验——Few-NERD 上的 2×2 factorial interaction——不显著（$z=-0.67$, $p=0.50$）。FewRel 上甚至没有做 factorial test（\"BCS-controlled design varies confusability within fixed count levels rather than crossing both factors\"——但这正是 controlled study 应该做的 factorial crossing）。在没有显著交互效应（或显著缺乏交互效应、即加性模型的 equivalence test）的情况下，\"separable\" 的声称缺乏统计基础。\n- 为什么影响接收：这是论文标题和主要贡献的核心 framing。如果 separability 无法形式验证，title/abstract/contributions 需要显著弱化。\n- 建议修改方向：(1) 在 FewRel 上做 count×BCS crossed factorial；(2) 使用 equivalence test (TOST) 检验交互项是否在 practical equivalence margin 内；(3) 如果无法完成，将 \"separable channels\" 改为 \"partially distinguishable dimensions\" 并在 framing 中降调。\n\n**N2** [Critical] **Extreme-batch gap 与 typical-batch gap 的呈现失衡，构成 misleading framing**\n\n- 具体位置：Abstract (\"up to 31.2 pp\")、Introduction (contribution 1, 3)、§5.3 \"Practical magnitude\" (typical gap 2.2pp 首次出现)\n- 问题：Abstract 和 Introduction 反复引用 31.2pp 作为 confusability effect 的标志性数字，但 §5.3 揭示 typical random batch 间的 BCS 差异仅产生 ~2.2pp 的准确率差距（95% CI: [0.4, 4.0]）。31.2pp 来自 deliberately constructed extreme batches（最高 vs 最低 BCS），代表 upper bound 而非 representative magnitude。Quartile gap 也仅 3.9-5.3pp。将 methodological upper-bound 呈现为 headline finding 误导读者对实际效应大小的判断。\n- 为什么影响接收：ARR soundness 标准要求 claims 与 evidence 对齐。当 typical magnitude 是 2.2pp 时，以 31.2pp 为 headline 不符合比例。\n- 建议修改方向：Abstract/Intro 中首先报告 typical-batch magnitude (2.2pp quartile gap 3.9-5.3pp)，将 31.2pp 明确标注为 \"methodological upper-bound under extreme construction\"。让读者能从 abstract 正确估计实践影响。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [Major] **Pairwise SCS 解释力极低（$r^2 = 1.3$–$1.7\\%$），proxy validity 存疑**\n\n- 具体位置：Table 2（§5.2）, §4.2 \"SCS as a lightweight proxy\"\n- 问题：SCS 解释 type confusion 方差的 1.3-1.7%。即便 aggregation 到 batch-level 达到 22%，仍有 78% 未解释。论文将 SCS 定位为 \"informative proxy\" 但未充分讨论：(a) 为何不使用更强的 proxy（如 task-grounded confusion matrix from pilot study、LLM perplexity-based similarity、few-shot confusion rate）; (b) 1.3% $r^2$ 是否足以称为 \"predicts type confusion\"（Table 2 caption 用此措辞）。\n- 建议：增加一个 paragraph 讨论 SCS 作为 pre-hoc metric 的 cost-performance tradeoff——为何不先跑少量实验获得 empirical confusion matrix，用 confusion-based score 替代 embedding similarity。或者 reframe：SCS 不是 \"predicts confusion\" 而是 \"weakly correlated with confusion\"。\n\n**W2** [Major] **Cross-model validation 覆盖不足**\n\n- 具体位置：Limitations item 1, Table 5-6 (Appendix A), §5.3 cross-model\n- 问题：仅 2 个模型（Qwen3-32B, Llama-3.1-8B），规模差 4×，架构相近（均 decoder-only）。Channel 2 在 8B NER 上未能复现（floor effect）。缺少：(a) 类似规模的不同架构（如 Mistral, Gemma）; (b) 闭源模型（GPT-4o, Gemini）; (c) encoder-decoder 架构。两个模型的一致性可能仅反映 decoder-only transformer 的共性而非通用规律。\n- 建议：至少增加一个同规模不同架构的开源模型验证（如 Mistral-7B 或 Gemma-2-27B）。如果资源有限，需要在 Discussion 中明确标注 generalizability boundary。\n\n**W3** [Major] **FewRel 实验设计的生态效度问题**\n\n- 具体位置：§4.1 FewRel description, §4.3 Experiment 2\n- 问题：FewRel 的 BCS-controlled experiment 使用 oracle routing（将 instance 路由到包含其 gold type 的 batch），这在实际部署中不可用。论文明确承认这一点（§6 \"oracle routing requires gold labels\"），但 FewRel 上所有 BCS-controlled 结果（Table 4, 7-9, within-pool analysis）都依赖 oracle routing。真正的 confusability effect 需要在无 oracle 的 full-schema single-pass 设定下测量——而 Table 8 的 full 80-rel condition 恰恰不显著（$p=0.76$）。\n- 为什么这很重要：读者可能误读为 \"在实际 80-type 抽取中，BCS 高的 batch 性能差 31pp\"，但实际上这是 oracle-routed 到 8-type batches 的结果。\n- 建议：在正文中更早、更显著地说明 BCS-controlled experiments 的 oracle routing 前提，并讨论在 non-oracle (full single-pass) 设定下 BCS 信号为何消失（BCS range collapse at 80 types）。\n\n**W4** [Major] **Count curves 每个 level 仅 5 batches**\n\n- 具体位置：§4.3 \"For each count level, we sample 5 random type batches\"\n- 问题：5 个 random batches 导致 count-curve estimates 的方差可能很大。Figure 1a 的 CI bands 有多宽？论文未报告 count-curve 的 per-level CIs。仅在 BCS-controlled experiments 用 25 batches。如果 5 个 batch 中碰巧包含 extreme BCS 组合，count effect 的估计会被 confusability 污染——这恰恰是论文试图分离的 confound。\n- 建议：(1) 报告 count-curve 每个 level 的 inter-batch SD 或 CI; (2) 讨论 5 batches 是否足以使 BCS 期望值收敛到 population mean; (3) 或增加 bootstrap resampling 证明 count-curve 结论对 batch selection 稳健。\n\n**W5** [Minor→Major] **多重比较未校正**\n\n- 具体位置：全文\n- 问题：论文在 4 个数据集 × 2 embeddings × 多个 count levels × 2 prompt versions 上报告大量 correlation/regression $p$-values。虽然核心结论的 $p < 0.001$ 不受影响，但边界显著的结果（MAVEN per-type $p=0.025$, within-pool regression $p=0.027$, Few-NERD per-type $\\rho=-0.293$ $p=0.02$）在 Bonferroni 或 FDR 校正后可能不再显著。\n- 建议：添加一个 paragraph 说明多重比较策略。如果不做 formal correction，至少讨论哪些 $p$-values 在校正后仍然 robust。\n\n---\n\n## Questions to Authors\n\n**Q1**: §5.3 Practical magnitude 指出 typical BCS span (IQR=0.054) 仅产生 2.2pp gap。在实际应用中，用户无法控制 schema 中 type 的语义分布——那么这 2.2pp 的 expected gap 是否真的值得用额外的 pre-hoc SCS computation + schema redesign 来解决？能否提供一个 cost-benefit 分析？\n\n**Q2**: 为什么选择 MiniLM 而非更强的 embedding model（如 E5-large, BGE, GTE）？是否有实验表明 MiniLM 是最优选择，还是仅因为方便？更强的 embedding 是否会显著提高 pairwise $r^2$？\n\n**Q3**: Oracle routing 在 RE 上恢复 +29.8pp，但 confusability-aware grouping 仅 +1.4pp（n.s.）。这是否说明 count effect（从 80-type 降到 8-type batches）远大于 confusability effect？如果是，论文的 framing 是否应将 count channel 作为更重要的发现？\n\n**Q4**: FewRel 合并 train+val splits 产生 80 types。contamination argument（train-origin accuracy < val-origin）基于多少 instances？$p=0.06$ 在单侧检验中是否接近显著？\n\n**Q5**: MAVEN 上 count-curve 呈上升趋势（与其他 3 个数据集相反），论文归因于 centrality confound。但 centrality confound 解释的是 per-type BCS-F1 correlation——它如何解释 count-curve 的方向反转？这两个现象的联系需要更 explicit 的论证。\n\n---\n\n## 小问题（不影响接收）\n\n- §4.1 FewRel: \"12-13 per relation type, stratified to ensure equal representation\" — 为什么不精确到每 type 恰好 12.5 instances（即 1000/80）？\n- Table 3 (error taxonomy): NER 的 \"V.High\" BCS bin 标 \"---\"，应说明为什么 NER 仅有 4 个 bin 而 RE 有 5 个。\n- §5.1: \"effect replicates on Llama-3.1-8B-Instruct ($-$43pp on Few-NERD; per-batch $r = 0.725$)\" — per-batch $r$ 指的是什么和什么之间的相关？应 clarify。\n- Appendix H \"Pair-to-Batch Aggregation Simulation\": 将 \"effective degrees of freedom ≈ 3.4\" 的推导写清楚——是 $28 / (1 + 27 \\times \\rho)$ 还是其他公式？\n- §6 Discussion \"Why does embedding similarity predict LLM confusion?\" — 这段以 hypothesis 形式讨论 attention mechanism overlap，但没有任何验证。建议标注为 speculative/hypothesis 而非 explanation。\n\n---\n\n## 总结\n\n论文在 zero-shot IE 领域提出了一个有意义的分析框架（SCS/BCS + controlled stratification），实验设计和统计报告的透明度值得肯定。主要问题是：(1) \"separable channels\" 的形式统计支撑缺失（factorial $p=0.50$）; (2) typical effect size 很小（2.2pp）但 abstract/intro 以 extreme-batch gap（31.2pp）为 headline; (3) 模型覆盖不足。如果 framing 调整为 \"partially distinguishable, modest-magnitude dimensions of schema-induced degradation\" 并诚实前置 typical magnitude，论文作为 controlled empirical study 仍有贡献价值，推荐 Findings track。",
  "reviewer_id": "1",
  "project": "schema-dag-extraction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 1 — Round 1 审稿意见\n\n**论文**: \"Does Type Confusability Shape Schema-Induced Degradation in Training-Free LLM Information Extraction?\"\n**侧重**: 方法论 + 实验严谨性 + 统计分析\n\n---\n\n## 总体评分\n\n**Overall**: 3 (Findings acceptance)\n**一句话总结**: 实验设计精细、统计报告透明，但核心 claim（\"separable channels\"）缺乏形式统计支撑，且实际效应量之小（typical batch gap 仅 2.2pp）削弱了研究的实践意义。\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3/5 | 核心 factorial test 不显著(p=0.50)、Channel 2 在 8B NER 上不可复现、pairwise R²仅1.3-1.7%。但 controlled stratification 设计合理，统计报告诚实。 |\n| Excitement | 3/5 | 研究问题有实践价值，centrality confound 分析是新颖贡献，但 negative SDGD 结果和微弱 effect size 限制了对社区的直接帮助。 |\n| Reproducibility | 4/5 | 实验细节充分（prompt template、decoding params、seed），承诺 release 代码，但代码尚未提供。 |\n| Confidence | 4/5 | 本人熟悉 zero-shot IE、LLM evaluation 方法学和统计检验。 |\n\n---\n\n## Summary\n\n本文研究 training-free LLM IE 中 schema 规模增大导致的性能下降，提出 SCS（pairwise cosine similarity）和 BCS（batch-level mean SCS）量化 type confusability，通过 count curves 和 BCS-controlled 两种实验范式在 4 个数据集上分析，声称分离出 count-driven recall decline 和 confusability-driven type substitution 两个降级通道。同时报告了 SDGD（schema decomposition）的 negative result，诊断 merge amplification 为 NER 分解失败的原因。\n\n---\n\n## 主要优势\n\n1. **精良的 controlled design**: 固定 count 变 BCS、固定 BCS 变 count 的范式在 zero-shot IE 文献中属首次，within-pool analysis 额外控制 pool composition confound，实验逻辑链完整。\n\n2. **统计报告的透明度**: 非显著结果（factorial $p=0.50$, SDGD +1.4pp $p≈0.19$, within-pool quartile CI 过零）、modest effect sizes（$r^2=1.3$–$1.7\\%$）、floor effects 均如实报告，未做 cherry-picking。\n\n3. **Centrality confound 分析（§5.5 + Appendix D）**: 识别 MAVEN 上 per-type BCS 正相关为 spurious signal，通过 partial correlation 控制 log-frequency 和 degree centrality 后信号消失，同时保留 pairwise signal——这是对社区有方法论价值的贡献。\n\n4. **Pair-to-batch aggregation simulation（Appendix F）**: 用 Monte Carlo 验证 pair-level $R^2=7\\%$ 如何经 inter-pair correlation ($\\rho=0.35$) 聚合到 batch-level $R^2≈22\\%$，定量解释了微弱个体信号如何产生可检测的批次效应。\n\n5. **Negative result 的价值**: SDGD 失败的诊断（merge amplification: precision 0.563→0.210）机制清晰、有实践警示价值。\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [Critical] **Factorial test 不显著与 \"separable channels\" 声称矛盾**\n\n- 具体位置：Appendix C（§A.3），Limitations item 3，Abstract/Introduction \"two empirically separable degradation channels\"\n- 问题：论文核心 claim 是 count 和 confusability 构成 \"empirically separable\" 的两个降级通道。但唯一的形式 separability 检验——Few-NERD 上的 2×2 factorial interaction——不显著（$z=-0.67$, $p=0.50$）。FewRel 上甚至没有做 factorial test（\"BCS-controlled design varies confusability within fixed count levels rather than crossing both factors\"——但这正是 controlled study 应该做的 factorial crossing）。在没有显著交互效应（或显著缺乏交互效应、即加性模型的 equivalence test）的情况下，\"separable\" 的声称缺乏统计基础。\n- 为什么影响接收：这是论文标题和主要贡献的核心 framing。如果 separability 无法形式验证，title/abstract/contributions 需要显著弱化。\n- 建议修改方向：(1) 在 FewRel 上做 count×BCS crossed factorial；(2) 使用 equivalence test (TOST) 检验交互项是否在 practical equivalence margin 内；(3) 如果无法完成，将 \"separable channels\" 改为 \"partially distinguishable dimensions\" 并在 framing 中降调。\n\n**N2** [Critical] **Extreme-batch gap 与 typical-batch gap 的呈现失衡，构成 misleading framing**\n\n- 具体位置：Abstract (\"up to 31.2 pp\")、Introduction (contribution 1, 3)、§5.3 \"Practical magnitude\" (typical gap 2.2pp 首次出现)\n- 问题：Abstract 和 Introduction 反复引用 31.2pp 作为 confusability effect 的标志性数字，但 §5.3 揭示 typical random batch 间的 BCS 差异仅产生 ~2.2pp 的准确率差距（95% CI: [0.4, 4.0]）。31.2pp 来自 deliberately constructed extreme batches（最高 vs 最低 BCS），代表 upper bound 而非 representative magnitude。Quartile gap 也仅 3.9-5.3pp。将 methodological upper-bound 呈现为 headline finding 误导读者对实际效应大小的判断。\n- 为什么影响接收：ARR soundness 标准要求 claims 与 evidence 对齐。当 typical magnitude 是 2.2pp 时，以 31.2pp 为 headline 不符合比例。\n- 建议修改方向：Abstract/Intro 中首先报告 typical-batch magnitude (2.2pp quartile gap 3.9-5.3pp)，将 31.2pp 明确标注为 \"methodological upper-bound under extreme construction\"。让读者能从 abstract 正确估计实践影响。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [Major] **Pairwise SCS 解释力极低（$r^2 = 1.3$–$1.7\\%$），proxy validity 存疑**\n\n- 具体位置：Table 2（§5.2）, §4.2 \"SCS as a lightweight proxy\"\n- 问题：SCS 解释 type confusion 方差的 1.3-1.7%。即便 aggregation 到 batch-level 达到 22%，仍有 78% 未解释。论文将 SCS 定位为 \"informative proxy\" 但未充分讨论：(a) 为何不使用更强的 proxy（如 task-grounded confusion matrix from pilot study、LLM perplexity-based similarity、few-shot confusion rate）; (b) 1.3% $r^2$ 是否足以称为 \"predicts type confusion\"（Table 2 caption 用此措辞）。\n- 建议：增加一个 paragraph 讨论 SCS 作为 pre-hoc metric 的 cost-performance tradeoff——为何不先跑少量实验获得 empirical confusion matrix，用 confusion-based score 替代 embedding similarity。或者 reframe：SCS 不是 \"predicts confusion\" 而是 \"weakly correlated with confusion\"。\n\n**W2** [Major] **Cross-model validation 覆盖不足**\n\n- 具体位置：Limitations item 1, Table 5-6 (Appendix A), §5.3 cross-model\n- 问题：仅 2 个模型（Qwen3-32B, Llama-3.1-8B），规模差 4×，架构相近（均 decoder-only）。Channel 2 在 8B NER 上未能复现（floor effect）。缺少：(a) 类似规模的不同架构（如 Mistral, Gemma）; (b) 闭源模型（GPT-4o, Gemini）; (c) encoder-decoder 架构。两个模型的一致性可能仅反映 decoder-only transformer 的共性而非通用规律。\n- 建议：至少增加一个同规模不同架构的开源模型验证（如 Mistral-7B 或 Gemma-2-27B）。如果资源有限，需要在 Discussion 中明确标注 generalizability boundary。\n\n**W3** [Major] **FewRel 实验设计的生态效度问题**\n\n- 具体位置：§4.1 FewRel description, §4.3 Experiment 2\n- 问题：FewRel 的 BCS-controlled experiment 使用 oracle routing（将 instance 路由到包含其 gold type 的 batch），这在实际部署中不可用。论文明确承认这一点（§6 \"oracle routing requires gold labels\"），但 FewRel 上所有 BCS-controlled 结果（Table 4, 7-9, within-pool analysis）都依赖 oracle routing。真正的 confusability effect 需要在无 oracle 的 full-schema single-pass 设定下测量——而 Table 8 的 full 80-rel condition 恰恰不显著（$p=0.76$）。\n- 为什么这很重要：读者可能误读为 \"在实际 80-type 抽取中，BCS 高的 batch 性能差 31pp\"，但实际上这是 oracle-routed 到 8-type batches 的结果。\n- 建议：在正文中更早、更显著地说明 BCS-controlled experiments 的 oracle routing 前提，并讨论在 non-oracle (full single-pass) 设定下 BCS 信号为何消失（BCS range collapse at 80 types）。\n\n**W4** [Major] **Count curves 每个 level 仅 5 batches**\n\n- 具体位置：§4.3 \"For each count level, we sample 5 random type batches\"\n- 问题：5 个 random batches 导致 count-curve estimates 的方差可能很大。Figure 1a 的 CI bands 有多宽？论文未报告 count-curve 的 per-level CIs。仅在 BCS-controlled experiments 用 25 batches。如果 5 个 batch 中碰巧包含 extreme BCS 组合，count effect 的估计会被 confusability 污染——这恰恰是论文试图分离的 confound。\n- 建议：(1) 报告 count-curve 每个 level 的 inter-batch SD 或 CI; (2) 讨论 5 batches 是否足以使 BCS 期望值收敛到 population mean; (3) 或增加 bootstrap resampling 证明 count-curve 结论对 batch selection 稳健。\n\n**W5** [Minor→Major] **多重比较未校正**\n\n- 具体位置：全文\n- 问题：论文在 4 个数据集 × 2 embeddings × 多个 count levels × 2 prompt versions 上报告大量 correlation/regression $p$-values。虽然核心结论的 $p < 0.001$ 不受影响，但边界显著的结果（MAVEN per-type $p=0.025$, within-pool regression $p=0.027$, Few-NERD per-type $\\rho=-0.293$ $p=0.02$）在 Bonferroni 或 FDR 校正后可能不再显著。\n- 建议：添加一个 paragraph 说明多重比较策略。如果不做 formal correction，至少讨论哪些 $p$-values 在校正后仍然 robust。\n\n---\n\n## Questions to Authors\n\n**Q1**: §5.3 Practical magnitude 指出 typical BCS span (IQR=0.054) 仅产生 2.2pp gap。在实际应用中，用户无法控制 schema 中 type 的语义分布——那么这 2.2pp 的 expected gap 是否真的值得用额外的 pre-hoc SCS computation + schema redesign 来解决？能否提供一个 cost-benefit 分析？\n\n**Q2**: 为什么选择 MiniLM 而非更强的 embedding model（如 E5-large, BGE, GTE）？是否有实验表明 MiniLM 是最优选择，还是仅因为方便？更强的 embedding 是否会显著提高 pairwise $r^2$？\n\n**Q3**: Oracle routing 在 RE 上恢复 +29.8pp，但 confusability-aware grouping 仅 +1.4pp（n.s.）。这是否说明 count effect（从 80-type 降到 8-type batches）远大于 confusability effect？如果是，论文的 framing 是否应将 count channel 作为更重要的发现？\n\n**Q4**: FewRel 合并 train+val splits 产生 80 types。contamination argument（train-origin accuracy < val-origin）基于多少 instances？$p=0.06$ 在单侧检验中是否接近显著？\n\n**Q5**: MAVEN 上 count-curve 呈上升趋势（与其他 3 个数据集相反），论文归因于 centrality confound。但 centrality confound 解释的是 per-type BCS-F1 correlation——它如何解释 count-curve 的方向反转？这两个现象的联系需要更 explicit 的论证。\n\n---\n\n## 小问题（不影响接收）\n\n- §4.1 FewRel: \"12-13 per relation type, stratified to ensure equal representation\" — 为什么不精确到每 type 恰好 12.5 instances（即 1000/80）？\n- Table 3 (error taxonomy): NER 的 \"V.High\" BCS bin 标 \"---\"，应说明为什么 NER 仅有 4 个 bin 而 RE 有 5 个。\n- §5.1: \"effect replicates on Llama-3.1-8B-Instruct ($-$43pp on Few-NERD; per-batch $r = 0.725$)\" — per-batch $r$ 指的是什么和什么之间的相关？应 clarify。\n- Appendix H \"Pair-to-Batch Aggregation Simulation\": 将 \"effective degrees of freedom ≈ 3.4\" 的推导写清楚——是 $28 / (1 + 27 \\times \\rho)$ 还是其他公式？\n- §6 Discussion \"Why does embedding similarity predict LLM confusion?\" — 这段以 hypothesis 形式讨论 attention mechanism overlap，但没有任何验证。建议标注为 speculative/hypothesis 而非 explanation。\n\n---\n\n## 总结\n\n论文在 zero-shot IE 领域提出了一个有意义的分析框架（SCS/BCS + controlled stratification），实验设计和统计报告的透明度值得肯定。主要问题是：(1) \"separable channels\" 的形式统计支撑缺失（factorial $p=0.50$）; (2) typical effect size 很小（2.2pp）但 abstract/intro 以 extreme-batch gap（31.2pp）为 headline; (3) 模型覆盖不足。如果 framing 调整为 \"partially distinguishable, modest-magnitude dimensions of schema-induced degradation\" 并诚实前置 typical magnitude，论文作为 controlled empirical study 仍有贡献价值，推荐 Findings track。",
    "reviewer_id": "1",
    "project": "schema-dag-extraction"
  }
}
```

</details>

---


### Tool result

_source line 333 · 2026-05-16T13:52:39.950042+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3866
}
```

</details>

---


### Assistant

_source line 334 · 2026-05-16T13:52:45.223090+00:00_

审稿意见已提交给 Review Director。

核心判断：论文实验设计精良、统计透明，但三个关键问题影响接收——(1) "separable channels" 的 factorial 检验不显著(p=0.50)与核心 claim 矛盾；(2) typical batch gap 仅 2.2pp，abstract/intro 以 extreme 31.2pp 为 headline 构成 framing 失衡；(3) 仅 2 个模型覆盖不足。建议 Findings track（Overall 3/5）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1"
}
```

</details>

---


## Round 12

## Round 12

4 recorded events


### User

_source line 335 · 2026-05-16T13:54:01.363415+00:00_

[Round 1 审稿请求]:
## 交叉分享 — 请逐条回应 Reviewer 2 和 Reviewer 3 的审稿意见

请仔细阅读以下两位 Reviewer 的完整审稿意见，对每个 Must-Fix 和 Should-Fix 问题逐条回应：
- **[AGREE]** 同意并说明理由
- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）

---

## Reviewer 2 的审稿意见（新颖性 + Related Work + 论证逻辑）

**Overall**: 3.0/5

### Must-Fix 问题

**R2-N1** [Critical] Abstract/Introduction 的 framing 存在系统性过度强调
- Abstract/Intro 反复突出 31.2pp 和 5.3pp，而 typical random batch 效应仅为 2.2pp（§5.3）。31.2pp 来自人工构造的 extreme batch，不代表真实使用场景。

**R2-N2** [Critical] "首次 controlled study" 声称需更严格限定
- LLM-PEE 的 type-partitioning 策略隐含了对 count vs. confusability 的区分；"Reflect then Learn" 通过 introspective confusion 间接量化 type confusion；"From Haystack to Needle: Label Space Reduction" 明确研究 label set size 对 zero-shot classification 的影响。

**R2-N3** [Critical] Two-channel model 的概念深度不足以作为独立贡献
- "更多 types → recall 下降"已是常识 + "相似 types → type confusion" LLM-PEE 已 operationalize。贡献不在于 model 本身而在于 controlled experiments。

### Should-Fix 问题

**R2-W1** [Major] Pairwise r²=1.3-1.7% 的 practical significance 论证不充分
- Typical-batch 2.2pp gap 可能在工程实践中 within noise margin。

**R2-W2** [Major] Related Work 遗漏：Label Space Reduction / Label Confusion 文献

**R2-W3** [Major] RE 实验使用 oracle routing，限制了 RQ3 的回答质量
- +1.4pp 在 oracle 条件下缺乏实用价值；RQ3 的实际答案是 "目前不 work"。

**R2-W4** [Minor-to-Major] SCS 与 LLM-PEE 的差异讨论缺乏深度

---

## Reviewer 3 的审稿意见（格式合规 + 可复现性 + 写作质量）

**Overall**: 3.5/5

### Must-Fix 问题

**R3-N1** [Critical] 正文页数可能超过 8 页限制
- 估计正文约 8.5-9 页，ACL ARR Long Paper 正文限制 ≤ 8 页。

**R3-N2** [Critical] Few-NERD 采样策略未明确描述
- FewRel/DocRED 说明了分层抽样，但 Few-NERD 仅说 "We sample 1,000 test instances"，未说明是否按 66 个类型分层。

### Should-Fix 问题

**R3-W1** [Major] Count-curve 批次构造的随机种子未报告
**R3-W2** [Major] Checklist B1 遗漏 DocRED 引用且 Llama 缺少 \cite
**R3-W3** [Major] Bootstrap 重采样次数不一致（B=1,000 vs B=10,000）
**R3-W4** [Minor-to-Major] 代码与数据未公开，仅承诺 "upon acceptance"
**R3-W5** [Minor] NER evaluation metric "text-match" 定义不够精确

### 小问题
- SDGD 脚注 "internal project designation" 可能引起匿名性疑虑
- vLLM v0.20.2 版本号似乎偏高，需确认准确性
- Channel 1/2 标签首次出现位置不统一

---

请逐条给出你的 [AGREE] 或 [REBUT] 回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 336 · 2026-05-16T13:56:23.517176+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 1 — 交叉回应（Reviewer 2 & Reviewer 3）\n\n---\n\n# 回应 Reviewer 2\n\n## Must-Fix\n\n**[AGREE] R2-N1: Abstract/Intro framing 过度强调 31.2pp**\n\n同意。这与我的 N2 完全一致。Abstract 第一段引用 \"up to 31.2 pp under extreme-batch construction\" 而 typical-batch gap 2.2pp 被藏在 §5.3 第四段。Introduction 的 contribution (1) 也以 \"up to −49pp\" 和 extreme gap 作为 headline。论文 §5.3 \"Practical magnitude\" 确实做了诚实披露，但读者在 abstract/intro 阶段已形成了 \"效应很大\" 的预期，到 §5.3 才被修正——这是 framing bias。Typical batch experience 应该在 abstract 中前置。\n\n**[REBUT] R2-N2: \"首次 controlled study\" 声称**\n\n部分反驳。R2 提到三个先前工作：\n\n1. **LLM-PEE**: §2 Related Work 明确讨论了这一区别——\"LLM-PEE partitions large event schemas by type embedding similarity. Our work differs in three ways: (1) we conduct controlled analysis... (2) our BCS-controlled experiments isolate count from confusability, which LLM-PEE conflates.\" LLM-PEE 用 similarity 做工程方案，没有 fixing count while varying BCS 的对照实验——这是 controlled study 的核心含义。\n\n2. **\"Reflect then Learn\"**: 该工作通过 introspective confusion 进行 schema refinement，是 engineering intervention，未做 count-controlled stratification。它观察到 confusion 但没有量化 count vs. confusability 的独立贡献。\n\n3. **\"From Haystack to Needle\"**: 研究 label set size reduction 对 zero-shot classification 的影响——这恰恰是 count effect only，没有在固定 count 下操纵 confusability。\n\n**然而**，R2 的批评有部分道理：\"首次\" 的 scope 应更精确。建议改为 \"the first study that formally isolates confusability from count via stratified experimental design\"——而非宽泛的 \"first controlled study\"。这是一个 framing 精确性问题，非 factual error。\n\n**[AGREE] R2-N3: Two-channel model 概念深度不足以作为独立贡献**\n\n同意，但需 nuance。\"Count → recall decline\" 确实是 well-established observation（Li et al. 2023 已有）；\"Similar types → confusion\" 的方向被 LLM-PEE 隐式利用。论文的真正贡献不是 \"two-channel model\" 这个 conceptual framework（它确实接近 trivial decomposition），而是：(a) controlled experimental evidence showing these are partially separable（尽管 factorial test 不显著——见我的 N1）; (b) effect size quantification; (c) centrality confound identification; (d) merge amplification diagnosis。\n\n建议：将 Contribution 1 从 \"Two-channel degradation model\" 改为 \"Controlled empirical evidence for partial separability of count and confusability effects\"——强调 evidence 而非 model。\n\n## Should-Fix\n\n**[AGREE] R2-W1: 2.2pp practical significance 不充分**\n\n完全同意。与我的 N2 互补。2.2pp 在 LLM IE 的 typical variance 中可能 within noise——特别是 prompt wording 变化本身就引入 5-6pp 变化（v1 vs v2 gap = 5.7pp; Appendix §A.7）。如果 prompt choice 的影响大于 BCS 的影响，那么 confusability-aware schema design 的 ROI 存疑。\n\n**[AGREE] R2-W2: Related work 遗漏 label space reduction / label confusion 文献**\n\n同意。论文 §2 未引用 label confusion / noisy label learning 方向的经典工作（如 label smoothing 动机下的 inter-class similarity analysis），也未引用 zero-shot classification 中 label set size 研究。补充这些文献能更好地定位 SCS 的 novelty boundary。\n\n**[AGREE] R2-W3: Oracle routing 限制 RQ3 回答**\n\n同意。与我的 W3 一致。RQ3 问 \"Can confusability-aware schema decomposition improve extraction quality?\" 实际答案是：NER 不行（merge amplification），RE 在 oracle 条件下仅 +1.4pp（n.s.）。去掉 oracle 后目前没有 positive evidence。论文应将 RQ3 的回答明确为 negative result + theoretical ceiling analysis，而非暗示 decomposition 是 viable direction。\n\n**[REBUT] R2-W4: SCS vs LLM-PEE 差异讨论不足**\n\n部分反驳。§2 \"SCS novelty\" paragraph 已明确承认：\"SCS shares its formal definition—pairwise cosine similarity of type name embeddings—with the partitioning criterion used in LLM-PEE. Our contribution is not the metric itself but the controlled experimental framework.\"——这一声明足够 honest。R2 要求 \"更深入讨论差异\" 可能预设 SCS 本身应是 novelty，但论文已明确放弃了这个 claim。作为 methodology paper，novelty 在于实验设计，不在于 metric。但同意可增加 1-2 句讨论 LLM-PEE 的 similarity threshold 选择与本文 BCS 连续量化的方法论差异。\n\n---\n\n# 回应 Reviewer 3\n\n## Must-Fix\n\n**[AGREE] R3-N1: 正文可能超 8 页**\n\n同意这是需要验证的问题。从内容量估算：Introduction (~1.5p) + Related Work (~1p) + Experimental Setup (~1.5p with Table 1) + Results (~2.5p with Figure 1, Tables 2-3) + SDGD (~1.5p with Table 4) + Discussion + Conclusion (~1.5p) = ~10p raw text。加上 figures 和 tables 的 float space，正文超 8 页的可能性很高。这是 hard violation——ACL ARR 在 desk reject criteria 中明确包含 page limit。但我无法 compile LaTeX 验证，故不确定是否已通过压缩排版解决。如果确实超限，这是 must-fix 且 trivial 的修改（移内容到 appendix）。\n\n**[AGREE] R3-N2: Few-NERD 采样策略不明确**\n\n同意。§4.1 对比明显：FewRel \"1,000 balanced instances (12-13 per relation type, stratified)\"、DocRED \"1,000 instances balanced across 96 relation types (~10 per type)\"——但 Few-NERD 仅说 \"We sample 1,000 test instances\"。66 types 在 Few-NERD 中频率分布极不均匀（长尾分布），非分层抽样会导致稀有 type 的 confusion rate 估计不可靠，直接影响 Table 2 pairwise SCS-confusion correlation 的统计质量。这不是格式问题而是方法论问题。\n\n## Should-Fix\n\n**[AGREE] R3-W1: Count-curve batch 构造的随机种子未报告**\n\n同意。§4.4 报告了 decoding seed (42) 但 batch sampling 的随机种子未提及。对 5 batches × 7 count levels × 4 datasets = 140 个 batch selection 的可复现性至关重要。此外，如果 batch selection seed 固定但仅 1 个 seed，则 5 个 batch 可能存在 sampling bias。需报告 seed 或 batch selection algorithm details。\n\n**[AGREE] R3-W2: Checklist B1 遗漏 DocRED + Llama 无 \\cite**\n\n同意。Checklist 原文列出 \"Few-NERD \\cite{...}, FewRel \\cite{...}, MAVEN \\cite{...}, Qwen3-32B \\cite{...}, Meta-Llama-3.1-8B-Instruct, vLLM \\cite{...}, and all-MiniLM-L6-v2 \\cite{...}\"——DocRED \\cite{docred-2019} 在正文有引用但 checklist 遗漏；Llama 无 \\cite 命令。这是 mechanical 问题但反映 proof-reading 不足。\n\n**[REBUT] R3-W3: Bootstrap B 不一致（1,000 vs 10,000）**\n\n部分反驳。不同分析使用不同 B 值是 methodologically defensible：\n- §4.4 standard percentile bootstrap: B=1,000 is adequate for CI coverage (Efron & Tibshirani 1993 recommend ≥1,000 for percentile CIs)\n- Table 2 cluster bootstrap: B=10,000 is appropriate because cluster resampling has higher variance, requiring more resamples for CI stability\n- Appendix G (within-pool slopes): B=10,000 for OLS bootstrap with small $n$\n\n**然而**，论文应明确说明这是 deliberate methodological choice 而非 inconsistency。目前 §4.4 笼统说 \"B=1,000\" 但实际某些分析用了 10,000——这造成 apparent inconsistency。建议在 §4.4 添加一句：\"Cluster bootstrap and regression-based CIs use $B=10{,}000$ for stability; standard percentile CIs use $B=1{,}000$.\"\n\n**[AGREE] R3-W4: 代码未公开**\n\n同意但认为 severity 偏低。\"Code release upon acceptance\" 是 ACL ARR 的常见做法且被 reviewer guidelines 允许。ARR review form 的 reproducibility scoring 区分 \"code available\" 和 \"code promised\"。论文提供了充分的实验细节（prompts、decoding params、seeds、dataset splits）使 independent replication theoretically possible。降为 Minor 更合理。\n\n**[AGREE] R3-W5: NER text-match 定义不够精确**\n\n同意。§4.3 定义 \"a prediction is correct if the text string matches (case-insensitive) a gold entity and the type matches\"——但未说明：(a) partial overlap 如何处理（\"New York\" vs \"New York City\"）; (b) 同一 entity 出现多次是否要求所有 mentions 匹配; (c) duplicate predictions 的计分方式（是否做 bipartite matching）。对于 text-match 这种非标准 metric（vs. standard span-based micro-F1），精确定义尤为重要。\n\n## 小问题\n\n**[AGREE]** SDGD 脚注 \"internal project designation\" 确实引起匿名性疑虑。建议删除该脚注或改为 \"a mnemonic label for the decomposition approach\"。\n\n**[REBUT]** vLLM v0.20.2 版本号：论文目标 ACL ARR May 2025，投稿日可能在 2026。vLLM 发展极快（2024 年内从 v0.2 到 v0.6），到 2026 年 v0.20+ 并非不可能（如果 versioning scheme 改变或 rapid releases）。不能仅凭版本号判断为 error。但 R3 的 concern 合理——如果是 typo 则需修正。\n\n**[AGREE]** Channel 1/2 标签首次出现在 §5.4 但 abstract/intro 中已暗示 two channels 的存在。建议在 §1 Introduction 首次提到 \"two channels\" 时就给出 Channel 1/2 的简短定义，避免读者在 5 pages 后才知道标签含义。\n\n---\n\n## 综合评估\n\n三位 Reviewer 的主要关切有高度重叠：\n\n| 共识问题 | R1 | R2 | R3 |\n|----------|----|----|-----|\n| 31.2pp framing 过度 | N2 | N1 | — |\n| Factorial/separability 证据不足 | N1 | N3 (隐含) | — |\n| Cross-model 覆盖不足 | W2 | — | — |\n| Typical effect size 实践意义 | W1(部分) | W1 | — |\n| 页数超限 | — | — | N1 |\n| Few-NERD sampling 不明 | — | — | N2 |\n\n**我的判断**：R2-N1 和我的 N2 是同一个核心问题（framing 失衡），这是最容易修的——调整 abstract/intro 措辞即可。R2-N2/N3 的 novelty 挑战更深层，但论文如果将 contribution 从 \"model\" 重心转向 \"controlled evidence + methodology\"（centrality confound、aggregation simulation、merge amplification diagnosis），novelty 仍可 defend。R3-N1 页数问题若属实则是 hard constraint 需立即解决。\n\nOverall 维持 **3/5 (Findings)**——如果 framing 修正且 factorial evidence 得到补充（或 claim 弱化），可升至 3.5。",
  "reviewer_id": "1",
  "project": "schema-dag-extraction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 1 — 交叉回应（Reviewer 2 & Reviewer 3）\n\n---\n\n# 回应 Reviewer 2\n\n## Must-Fix\n\n**[AGREE] R2-N1: Abstract/Intro framing 过度强调 31.2pp**\n\n同意。这与我的 N2 完全一致。Abstract 第一段引用 \"up to 31.2 pp under extreme-batch construction\" 而 typical-batch gap 2.2pp 被藏在 §5.3 第四段。Introduction 的 contribution (1) 也以 \"up to −49pp\" 和 extreme gap 作为 headline。论文 §5.3 \"Practical magnitude\" 确实做了诚实披露，但读者在 abstract/intro 阶段已形成了 \"效应很大\" 的预期，到 §5.3 才被修正——这是 framing bias。Typical batch experience 应该在 abstract 中前置。\n\n**[REBUT] R2-N2: \"首次 controlled study\" 声称**\n\n部分反驳。R2 提到三个先前工作：\n\n1. **LLM-PEE**: §2 Related Work 明确讨论了这一区别——\"LLM-PEE partitions large event schemas by type embedding similarity. Our work differs in three ways: (1) we conduct controlled analysis... (2) our BCS-controlled experiments isolate count from confusability, which LLM-PEE conflates.\" LLM-PEE 用 similarity 做工程方案，没有 fixing count while varying BCS 的对照实验——这是 controlled study 的核心含义。\n\n2. **\"Reflect then Learn\"**: 该工作通过 introspective confusion 进行 schema refinement，是 engineering intervention，未做 count-controlled stratification。它观察到 confusion 但没有量化 count vs. confusability 的独立贡献。\n\n3. **\"From Haystack to Needle\"**: 研究 label set size reduction 对 zero-shot classification 的影响——这恰恰是 count effect only，没有在固定 count 下操纵 confusability。\n\n**然而**，R2 的批评有部分道理：\"首次\" 的 scope 应更精确。建议改为 \"the first study that formally isolates confusability from count via stratified experimental design\"——而非宽泛的 \"first controlled study\"。这是一个 framing 精确性问题，非 factual error。\n\n**[AGREE] R2-N3: Two-channel model 概念深度不足以作为独立贡献**\n\n同意，但需 nuance。\"Count → recall decline\" 确实是 well-established observation（Li et al. 2023 已有）；\"Similar types → confusion\" 的方向被 LLM-PEE 隐式利用。论文的真正贡献不是 \"two-channel model\" 这个 conceptual framework（它确实接近 trivial decomposition），而是：(a) controlled experimental evidence showing these are partially separable（尽管 factorial test 不显著——见我的 N1）; (b) effect size quantification; (c) centrality confound identification; (d) merge amplification diagnosis。\n\n建议：将 Contribution 1 从 \"Two-channel degradation model\" 改为 \"Controlled empirical evidence for partial separability of count and confusability effects\"——强调 evidence 而非 model。\n\n## Should-Fix\n\n**[AGREE] R2-W1: 2.2pp practical significance 不充分**\n\n完全同意。与我的 N2 互补。2.2pp 在 LLM IE 的 typical variance 中可能 within noise——特别是 prompt wording 变化本身就引入 5-6pp 变化（v1 vs v2 gap = 5.7pp; Appendix §A.7）。如果 prompt choice 的影响大于 BCS 的影响，那么 confusability-aware schema design 的 ROI 存疑。\n\n**[AGREE] R2-W2: Related work 遗漏 label space reduction / label confusion 文献**\n\n同意。论文 §2 未引用 label confusion / noisy label learning 方向的经典工作（如 label smoothing 动机下的 inter-class similarity analysis），也未引用 zero-shot classification 中 label set size 研究。补充这些文献能更好地定位 SCS 的 novelty boundary。\n\n**[AGREE] R2-W3: Oracle routing 限制 RQ3 回答**\n\n同意。与我的 W3 一致。RQ3 问 \"Can confusability-aware schema decomposition improve extraction quality?\" 实际答案是：NER 不行（merge amplification），RE 在 oracle 条件下仅 +1.4pp（n.s.）。去掉 oracle 后目前没有 positive evidence。论文应将 RQ3 的回答明确为 negative result + theoretical ceiling analysis，而非暗示 decomposition 是 viable direction。\n\n**[REBUT] R2-W4: SCS vs LLM-PEE 差异讨论不足**\n\n部分反驳。§2 \"SCS novelty\" paragraph 已明确承认：\"SCS shares its formal definition—pairwise cosine similarity of type name embeddings—with the partitioning criterion used in LLM-PEE. Our contribution is not the metric itself but the controlled experimental framework.\"——这一声明足够 honest。R2 要求 \"更深入讨论差异\" 可能预设 SCS 本身应是 novelty，但论文已明确放弃了这个 claim。作为 methodology paper，novelty 在于实验设计，不在于 metric。但同意可增加 1-2 句讨论 LLM-PEE 的 similarity threshold 选择与本文 BCS 连续量化的方法论差异。\n\n---\n\n# 回应 Reviewer 3\n\n## Must-Fix\n\n**[AGREE] R3-N1: 正文可能超 8 页**\n\n同意这是需要验证的问题。从内容量估算：Introduction (~1.5p) + Related Work (~1p) + Experimental Setup (~1.5p with Table 1) + Results (~2.5p with Figure 1, Tables 2-3) + SDGD (~1.5p with Table 4) + Discussion + Conclusion (~1.5p) = ~10p raw text。加上 figures 和 tables 的 float space，正文超 8 页的可能性很高。这是 hard violation——ACL ARR 在 desk reject criteria 中明确包含 page limit。但我无法 compile LaTeX 验证，故不确定是否已通过压缩排版解决。如果确实超限，这是 must-fix 且 trivial 的修改（移内容到 appendix）。\n\n**[AGREE] R3-N2: Few-NERD 采样策略不明确**\n\n同意。§4.1 对比明显：FewRel \"1,000 balanced instances (12-13 per relation type, stratified)\"、DocRED \"1,000 instances balanced across 96 relation types (~10 per type)\"——但 Few-NERD 仅说 \"We sample 1,000 test instances\"。66 types 在 Few-NERD 中频率分布极不均匀（长尾分布），非分层抽样会导致稀有 type 的 confusion rate 估计不可靠，直接影响 Table 2 pairwise SCS-confusion correlation 的统计质量。这不是格式问题而是方法论问题。\n\n## Should-Fix\n\n**[AGREE] R3-W1: Count-curve batch 构造的随机种子未报告**\n\n同意。§4.4 报告了 decoding seed (42) 但 batch sampling 的随机种子未提及。对 5 batches × 7 count levels × 4 datasets = 140 个 batch selection 的可复现性至关重要。此外，如果 batch selection seed 固定但仅 1 个 seed，则 5 个 batch 可能存在 sampling bias。需报告 seed 或 batch selection algorithm details。\n\n**[AGREE] R3-W2: Checklist B1 遗漏 DocRED + Llama 无 \\cite**\n\n同意。Checklist 原文列出 \"Few-NERD \\cite{...}, FewRel \\cite{...}, MAVEN \\cite{...}, Qwen3-32B \\cite{...}, Meta-Llama-3.1-8B-Instruct, vLLM \\cite{...}, and all-MiniLM-L6-v2 \\cite{...}\"——DocRED \\cite{docred-2019} 在正文有引用但 checklist 遗漏；Llama 无 \\cite 命令。这是 mechanical 问题但反映 proof-reading 不足。\n\n**[REBUT] R3-W3: Bootstrap B 不一致（1,000 vs 10,000）**\n\n部分反驳。不同分析使用不同 B 值是 methodologically defensible：\n- §4.4 standard percentile bootstrap: B=1,000 is adequate for CI coverage (Efron & Tibshirani 1993 recommend ≥1,000 for percentile CIs)\n- Table 2 cluster bootstrap: B=10,000 is appropriate because cluster resampling has higher variance, requiring more resamples for CI stability\n- Appendix G (within-pool slopes): B=10,000 for OLS bootstrap with small $n$\n\n**然而**，论文应明确说明这是 deliberate methodological choice 而非 inconsistency。目前 §4.4 笼统说 \"B=1,000\" 但实际某些分析用了 10,000——这造成 apparent inconsistency。建议在 §4.4 添加一句：\"Cluster bootstrap and regression-based CIs use $B=10{,}000$ for stability; standard percentile CIs use $B=1{,}000$.\"\n\n**[AGREE] R3-W4: 代码未公开**\n\n同意但认为 severity 偏低。\"Code release upon acceptance\" 是 ACL ARR 的常见做法且被 reviewer guidelines 允许。ARR review form 的 reproducibility scoring 区分 \"code available\" 和 \"code promised\"。论文提供了充分的实验细节（prompts、decoding params、seeds、dataset splits）使 independent replication theoretically possible。降为 Minor 更合理。\n\n**[AGREE] R3-W5: NER text-match 定义不够精确**\n\n同意。§4.3 定义 \"a prediction is correct if the text string matches (case-insensitive) a gold entity and the type matches\"——但未说明：(a) partial overlap 如何处理（\"New York\" vs \"New York City\"）; (b) 同一 entity 出现多次是否要求所有 mentions 匹配; (c) duplicate predictions 的计分方式（是否做 bipartite matching）。对于 text-match 这种非标准 metric（vs. standard span-based micro-F1），精确定义尤为重要。\n\n## 小问题\n\n**[AGREE]** SDGD 脚注 \"internal project designation\" 确实引起匿名性疑虑。建议删除该脚注或改为 \"a mnemonic label for the decomposition approach\"。\n\n**[REBUT]** vLLM v0.20.2 版本号：论文目标 ACL ARR May 2025，投稿日可能在 2026。vLLM 发展极快（2024 年内从 v0.2 到 v0.6），到 2026 年 v0.20+ 并非不可能（如果 versioning scheme 改变或 rapid releases）。不能仅凭版本号判断为 error。但 R3 的 concern 合理——如果是 typo 则需修正。\n\n**[AGREE]** Channel 1/2 标签首次出现在 §5.4 但 abstract/intro 中已暗示 two channels 的存在。建议在 §1 Introduction 首次提到 \"two channels\" 时就给出 Channel 1/2 的简短定义，避免读者在 5 pages 后才知道标签含义。\n\n---\n\n## 综合评估\n\n三位 Reviewer 的主要关切有高度重叠：\n\n| 共识问题 | R1 | R2 | R3 |\n|----------|----|----|-----|\n| 31.2pp framing 过度 | N2 | N1 | — |\n| Factorial/separability 证据不足 | N1 | N3 (隐含) | — |\n| Cross-model 覆盖不足 | W2 | — | — |\n| Typical effect size 实践意义 | W1(部分) | W1 | — |\n| 页数超限 | — | — | N1 |\n| Few-NERD sampling 不明 | — | — | N2 |\n\n**我的判断**：R2-N1 和我的 N2 是同一个核心问题（framing 失衡），这是最容易修的——调整 abstract/intro 措辞即可。R2-N2/N3 的 novelty 挑战更深层，但论文如果将 contribution 从 \"model\" 重心转向 \"controlled evidence + methodology\"（centrality confound、aggregation simulation、merge amplification diagnosis），novelty 仍可 defend。R3-N1 页数问题若属实则是 hard constraint 需立即解决。\n\nOverall 维持 **3/5 (Findings)**——如果 framing 修正且 factorial evidence 得到补充（或 claim 弱化），可升至 3.5。",
    "reviewer_id": "1",
    "project": "schema-dag-extraction"
  }
}
```

</details>

---


### Tool result

_source line 337 · 2026-05-16T13:56:27.538140+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4020
}
```

</details>

---


### Assistant

_source line 338 · 2026-05-16T13:56:34.209200+00:00_

交叉回应已提交给 Review Director。总结：

- 与 R2 在 framing 过度（N1）、practical significance（W1）、oracle routing 限制（W3）上一致
- 对 R2-N2（"首次"声称）部分反驳——论文的 controlled stratification 确实区别于 prior work 的工程方案，但措辞应更精确
- 对 R2-N3 同意 two-channel model 本身不构成独立贡献，novelty 在于 controlled evidence
- 与 R3 在页数（N1）、Few-NERD 采样（N2）、seed 报告（W1）上一致
- 对 R3-W3（Bootstrap B 不一致）部分反驳——不同 B 值有方法论依据，但需明确说明

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1"
}
```

</details>

---


## Round 13

## Round 13

40 recorded events


### User

_source line 339 · 2026-05-16T15:08:35.091663+00:00_

[Round 1 审稿请求]:
你是 Reviewer 1，负责**方法严谨性、实验设计、统计有效性**审查。

## Venue 信息
- **EMNLP 2026 Main Conference**（ARR May 25, 2026 cycle）
- 长文 8 页限制（不含 references、limitations、appendix）
- ACL 模板，double-blind
- 必须包含 Limitations section

## 论文路径
`projects/schema-dag-extraction/docs/paper/main.tex`（含 \input 的子文件：abstract.tex, introduction.tex, related_work.tex, experimental_setup.tex, results.tex, sdgd_negative.tex, discussion.tex, checklist.tex, prompt_appendix.tex）

## 审查侧重

### 1. 实验设计
- Count curve 每个 level 仅 5 个 random batches，方差估计是否充分？种子是否公开？
- BCS-controlled 实验的 batch 构造方法是否有 confound（如 batch 构造算法本身引入的偏差）
- Few-NERD 66 types 长尾分布下的采样策略是否 bias 了 confusion rate 估计
- FewRel train+val 合并使用的 data contamination 风险
- 单种子 (seed=42) 评估的可靠性

### 2. 统计方法
- Pairwise r²=1.3-1.7% 是否有实际意义（vs statistical significance）
- 多重比较问题：MAVEN p=0.025, within-pool p=0.027 等边界显著结果在 Bonferroni/FDR 校正后是否存活
- Factorial interaction test: Few-NERD p=0.50 不显著 + FewRel TOST p=0.003 显著 → "empirically separable" 的统计支撑是否充分
- Bootstrap CI 方法：pair-level B=10000 vs batch-level B=1000 的不一致性，cluster bootstrap 的适用性
- 31.2pp extreme-batch gap vs 2.2pp typical gap 的 framing 是否误导

### 3. 方法论
- SCS 基于 type name cosine similarity — 作为 confusability proxy 的 construct validity
- name-only vs name+definition ablation 是否充分验证了 SCS 的选择
- 不同 dataset 用不同 embedding (Qwen3 vs MiniLM) 的理由和影响
- SDGD 负面结果的归因分析（merge amplification vs 其他因素）

### 4. 格式合规
- 正文是否超 8 页（需编译确认）
- vLLM 版本号 v0.20.2 是否真实
- p-value 格式是否一致

请按以下结构输出审稿意见：
1. Summary (2-3 句)
2. Strengths (逐条)
3. Weaknesses (逐条，每条标注 severity: critical/warning/info)
4. Questions (需要作者澄清)
5. Missing References
6. Overall Assessment (strong reject / weak reject / borderline / weak accept / strong accept + 置信度)
7. Detailed Comments (逐节)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 340 · 2026-05-16T15:09:02.390804+00:00_

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
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
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

_source line 341 · 2026-05-16T15:09:02.391274+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 342 · 2026-05-16T15:09:02.993455+00:00_

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
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
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

_source line 343 · 2026-05-16T15:09:03.044505+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 344 · 2026-05-16T15:09:06.215982+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL ARR 2025 2026 reviewer guidelines review form criteria scoring"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR 2025 2026 reviewer guidelines review form criteria scoring"
  }
}
```

</details>

---


### Tool call

_source line 345 · 2026-05-16T15:09:07.269606+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 346 · 2026-05-16T15:09:07.521207+00:00_

1	\documentclass[11pt]{article}
2	
3	\usepackage[review]{acl}
4	
5	\usepackage{times}
6	\usepackage{latexsym}
7	\usepackage[T1]{fontenc}
8	\usepackage[utf8]{inputenc}
9	\usepackage{microtype}
10	\usepackage{graphicx}
11	\usepackage{booktabs}
12	\usepackage{amsmath}
13	\usepackage{enumitem}
14	\usepackage[normalem]{ulem}
15	\usepackage{listings}
16	
17	\title{Does Type Confusability Shape Schema-Induced Degradation\\in Training-Free LLM Information Extraction?}
18	
19	\author{Anonymous}
20	
21	\begin{document}
22	\maketitle
23	
24	\input{abstract}
25	
26	\input{introduction}
27	
28	\input{related_work}
29	
30	\input{experimental_setup}
31	
32	\input{results}
33	
34	\input{sdgd_negative}
35	
36	\input{discussion}
37	
38	\section*{Limitations}
39	\begin{enumerate}[leftmargin=*,itemsep=2pt]
40	\item \textbf{Model coverage.} Primary experiments use Qwen3-32B with cross-model validation on Llama-3.1-8B-Instruct. Whether patterns hold for proprietary models (GPT-4, Gemini) remains unverified. Channel~2 was not robustly detectable on NER at 8B scale, likely due to floor effects.
41	
42	\item \textbf{Modest pairwise effect size.} Pairwise SCS explains 1.3--1.7\% of type confusion variance; entity frequency, prompt position, mention ambiguity, and type definition quality likely account for the remainder.
43	
44	\item \textbf{Factorial interaction tests.} Within-dataset count $\times$ BCS interaction on Few-NERD did not reach significance ($p = 0.50$; Appendix~\ref{sec:appendix_factorial}). However, a FewRel factorial with TOST equivalence testing confirms additive separability ($p_{\text{TOST}} = .003$, interaction = 0.47\,pp; Appendix~\ref{sec:appendix_factorial}), and cross-pool slope consistency ($p = 0.60$) corroborates stable rather than amplifying sensitivity.
45	
46	\item \textbf{Decomposition and metric scope.} RE batch composition is tested on FewRel only; NER merge alternatives remain unexplored. SCS relies on embedding cosine similarity; label entropy or ontologica
…[truncated 25124 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 251
}
```

</details>

---


### Tool result

_source line 347 · 2026-05-16T15:09:13.849767+00:00_

Web search results for query: "ACL ARR 2025 2026 reviewer guidelines review form criteria scoring"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"ACLRollingReview (@ReviewAcl) / X","url":"https://x.com/reviewacl"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"aclrollingreview/reviewing.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/reviewing.md"}]

Based on the search results, here's information about ACL ARR 2025-2026 reviewer guidelines, review form criteria, and scoring:

## Reviewer Scoring System

Starting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation. The soundness scores must be justified by the text 
…[truncated 1318 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 7633
}
```

</details>

---


### Tool call

_source line 348 · 2026-05-16T15:09:19.854313+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 349 · 2026-05-16T15:09:20.206085+00:00_

1	\begin{abstract}
2	Training-free LLM information extraction degrades as schema complexity grows. We present the first study to formally isolate type confusability from type count via stratified controlled design in zero-shot LLM IE, spanning NER, RE (a closed-set classification task), and event detection across four datasets, introducing the Schema Confusability Score (SCS) and two paradigms: count curves varying schema size while randomizing confusability, and BCS-controlled experiments fixing size while varying confusability.
3	
4	We identify two empirically separable degradation channels: count-driven recall decline and confusability-driven type substitution. For RE, the quartile BCS gap is $-$5.3\,pp (95\% CI: [$-$7.4, $-$3.2]); typical random batches differ by ${\approx}\,2.2$\,pp. Under extreme-batch construction, the gap widens substantially (Table~\ref{tab:bcs_controlled}). Batch-level BCS explains $R^2 = 0.22\text{--}0.53$ of accuracy variance as an aggregated signal, while pairwise effect sizes remain modest ($r^2 = 1.3\text{--}1.7\%$). The effect is directionally consistent across prompt designs, with attenuated magnitude under improved prompts. Channel~1 replicates fully on Llama-3.1-8B; Channel~2 replicates on RE but shows floor effects on 8B NER. Count increases generally suppress extraction on cross-domain schemas; MAVEN's same-domain schema exhibits centrality confounding that reverses this trend. Schema decomposition via oracle routing recovers count-based degradation for RE (+29.8\,pp over single-pass), but confusability-aware grouping yields no significant additional gain (+1.4\,pp, $p\approx 0.19$).
5	\end{abstract}
6	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 351
}
```

</details>

---


### Tool call

_source line 350 · 2026-05-16T15:09:20.256754+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 351 · 2026-05-16T15:09:20.811144+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	Training-free\footnote{We use ``training-free'' and ``zero-shot'' interchangeably to denote prompting without parameter updates.} LLM information extraction---prompting a large language model with a target schema and asking it to extract structured information without any task-specific fine-tuning---enables rapid deployment across new domains and ontologies. This zero-shot paradigm eliminates the need for labeled data, making it attractive for applications where annotation is expensive or schemas evolve frequently \cite{llm4ie-survey-2024}. Yet the paradigm carries a critical limitation: performance degrades sharply as the number of candidate types in the prompt schema grows. On named entity recognition, recall drops from 0.72 with a single candidate type to 0.42 with 64 types, a 42\% relative decline. On relation extraction, accuracy falls from 85.7\% with one relation to 50.4\% with 80 relations (sentence-level) and from 88.0\% to 38.7\% with 96 relations (document-level)---near or exceeding halving. This degradation is not academic: real-world ontologies routinely define 50--200+ types, placing them squarely in the regime where training-free extraction becomes unreliable.
5	
6	What explains this degradation? Prior decomposition strategies \cite{uniner-2024,llm-pee-2025,parse-2025} conflate two mechanisms: having more types to discriminate among (count) and having semantically similar types to confuse (confusability) (hereafter Channel~1 and Channel~2). None isolates which factor predicts the gains (\S\ref{sec:related_work}).
7	
8	We ask three questions. \textbf{RQ1}: Does type confusability independently predict extraction degradation beyond the effect of type count? \textbf{RQ2}: Through what mechanisms do count and confusability each degrade performance? \textbf{RQ3}: Can confusability-aware schema decomposition improve extraction quality?
9	
10	We present the first study to formally isolate type confusab
…[truncated 2585 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 554
}
```

</details>

---


### Tool call

_source line 352 · 2026-05-16T15:09:20.811669+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 353 · 2026-05-16T15:09:21.767981+00:00_

1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{Training-free LLM IE.}
5	Training-free LLM IE spans instruction tuning \cite{instructuie-2023}, code-style schema encoding \cite{knowcoder-2024,codeie-2023}, annotation-guided extraction \cite{gollie-2024,adelie-2024}, schema-driven decoding \cite{slot-2025,oneke-2025}, and constrained JSON decoding \cite{json-schema-bench-2025}. For NER, methods include zero-shot decomposition \cite{xie-zeroshot-ner-2023,promptner-2023}, distillation \cite{uniner-2024}, and bidirectional encoders \cite{gliner-2024,gliner2-2025}. For RE, recent work examines zero-shot relation triplet extraction via prompting \cite{relationprompt-2022} and revisits relation extraction in the LLM era \cite{wadhwa-re-llm-2023}. These methods perform well with moderate schemas (4--20 types) but none investigates how performance degrades as schema complexity scales, nor proposes quantitative metrics for inter-type confusability.
6	
7	\paragraph{Schema complexity in IE.}
8	The most directly related work is LLM-PEE \cite{llm-pee-2025}, which partitions large event schemas by type embedding similarity. Our work differs in three ways: (1)~we conduct controlled analysis to understand \emph{why} extraction degrades rather than developing an engineering solution; (2)~our BCS-controlled experiments isolate count from confusability, which LLM-PEE conflates; (3)~our SDGD experiments reveal that merge amplification---not partitioning quality---is the bottleneck in decompose-then-merge pipelines. Other approaches address schema complexity via hard negative mining \cite{iepile-2024}, schema definition optimization \cite{parse-2025}, multi-agent debate \cite{crossagentie-2025,cmas-ner-2025}, schema-aware decomposition for event extraction \cite{dee-2024}, and active prompting \cite{reflect-learn-2026}; all treat it as an engineering problem rather than isolating the underlying degradation mechanisms.
9	
10	\paragraph{Schema complexity in dialogue and
…[truncated 1156 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 956
}
```

</details>

---


### Tool call

_source line 354 · 2026-05-16T15:09:21.818759+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/experimental_setup.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/experimental_setup.tex"
  }
}
```

</details>

---


### Tool result

_source line 355 · 2026-05-16T15:09:22.271441+00:00_

1	\section{Experimental Setup}
2	\label{sec:experimental_setup}
3	
4	We evaluate how prompt schema size and inter-type confusability affect zero-shot LLM extraction across three information extraction tasks and four datasets: named entity recognition (NER), sentence-level relation extraction (RE), document-level RE, and event detection (ED).
5	
6	\subsection{Tasks and Datasets}
7	\label{sec:datasets}
8	
9	\paragraph{Few-NERD (NER).}
10	Few-NERD \cite{fewnerd-2021} provides 66 fine-grained entity types organized into 8 coarse categories (person, location, organization, building, art, product, event, other). The dataset spans diverse domains, making it suitable for cross-domain evaluation. We sample 1{,}000 test instances uniformly across test instances; type frequency follows the natural long-tail distribution of Few-NERD. Evaluation uses token-level text matching. Pairwise analysis covers 1{,}953 type pairs with non-zero co-occurrence out of $\binom{66}{2}=2{,}145$ possible pairs.
11	
12	\paragraph{FewRel (RE).}
13	FewRel \cite{fewrel-2018} contains 80 relation types sourced from Wikidata. Since the validation split covers only 16 relations, we combine the training and validation splits to obtain the full 80-relation pool required for schema-scale experiments, and sample 1{,}000 balanced instances (12--13 per relation type, stratified to ensure equal representation). Each instance provides a sentence with marked head and tail entities; the task is to classify the relation.
14	
15	\paragraph{DocRED (Document-level RE).}
16	DocRED \cite{docred-2019} contains 96 relation types sourced from Wikidata, evaluated at the document level where entity pairs may span multiple sentences. We sample 1{,}000 instances balanced across 96 relation types ($\sim$10 per type) from the DocRED development set and formulate the task identically to FewRel: given a document with marked head and tail entities, classify the relation. DocRED extends the RE evaluation to a larger schema (96 vs.\
…[truncated 6947 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 356 · 2026-05-16T15:09:22.272145+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebFetch",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebFetch",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 357 · 2026-05-16T15:09:22.322543+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 358 · 2026-05-16T15:09:28.104709+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex"
  }
}
```

</details>

---


### Tool result

_source line 359 · 2026-05-16T15:09:28.507956+00:00_

1	\section{Results}
2	\label{sec:results}
3	
4	Unless otherwise noted, all experiments in this section use the v1 prompt (\S\ref{sec:model}; full templates in Appendix~\ref{sec:appendix_prompts}).
5	
6	\subsection{Count-Degradation Curves}
7	\label{sec:count_curves}
8	
9	\begin{figure}[t]
10	\centering
11	\begin{minipage}[t]{0.48\columnwidth}
12	\centering
13	\includegraphics[width=\linewidth]{../../figures/paper/fig_count_curves.pdf}
14	\end{minipage}
15	\hfill
16	\begin{minipage}[t]{0.48\columnwidth}
17	\centering
18	\includegraphics[width=\linewidth]{../../figures/paper/fig_bcs_scaling.pdf}
19	\end{minipage}
20	\caption{\textbf{(a)} Count-degradation curves across four datasets. NER recall generally declines and RE accuracy (both FewRel and DocRED) declines monotonically with schema size; MAVEN relaxed F1 increases (\S\ref{sec:centrality_confound}). \textbf{(b)} BCS-controlled FewRel accuracy. The BCS--accuracy slope is consistent across the independent 16-relation pool and within-pool 16-relation subsets (permutation $p = 0.60$); the wider BCS range available at 80 relations produces larger absolute gaps.}
21	\label{fig:main_results}
22	\end{figure}
23	
24	Figure~\ref{fig:main_results}a shows extraction quality degrades monotonically with schema size across three datasets: Few-NERD recall drops from 0.72 to 0.42 ($-$42\%), FewRel accuracy from 85.7\% to 50.4\% ($-$35.3\,pp), and DocRED from 88.0\% to 38.7\% ($-$56\%). MAVEN exhibits a reversed trend attributable to centrality confounding (\S\ref{sec:centrality_confound}). The effect replicates on Llama-3.1-8B-Instruct ($-$43\,pp on Few-NERD; per-batch $r = 0.725$; Table~\ref{tab:cross_model}), indicating schema configuration rather than model-specific factors predicts difficulty.
25	
26	\subsection{Pairwise Confusability and Type Confusion}
27	\label{sec:pairwise}
28	
29	We test whether pairwise SCS predicts type-level confusion rates. For each type pair $(t_i, t_j)$, we compute the confusion rate---the fraction
…[truncated 8700 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 403
}
```

</details>

---


### Tool call

_source line 360 · 2026-05-16T15:09:28.558627+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/sdgd_negative.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/sdgd_negative.tex"
  }
}
```

</details>

---


### Tool result

_source line 361 · 2026-05-16T15:09:29.612393+00:00_

1	\section{Schema Decomposition: Failure, Diagnosis, and Mitigation}
2	\label{sec:sdgd}
3	
4	A natural intervention against confusability-driven degradation is to partition the schema so that confusable types never co-occur in the same prompt. We test this idea with \textbf{Schema-DAG-Guided Decomposition} (SDGD\footnote{SDGD (Schema Decomposition and Grouping for Degradation mitigation) is an adopted abbreviation for schema decomposition and grouping; the graph structure is undirected.}), which uses greedy graph coloring on the pairwise SCS graph to assign types to low-confusability batches.
5	
6	We construct a thresholded confusability graph $G = (V, E)$ where each type is a vertex and an edge connects types $t_i, t_j$ whenever $\text{SCS}(t_i, t_j) > \tau$. Greedy graph coloring (\textsc{largest\_first}) assigns each type to a color such that no two adjacent---i.e., highly confusable---types share a batch. Each color class forms one extraction batch. For NER, predictions from all batches are merged via set union; for RE, each instance is routed to the batch containing its gold type (oracle routing). We test four NER modes: (i)~\textbf{single\_pass}, the undecomposed baseline; (ii)~\textbf{sdgd\_zero}, SCS-guided partitioning; (iii)~\textbf{random\_batch}, random partitioning with matched batch sizes; and (iv)~\textbf{per\_type}, each type extracted in isolation. Every mode falls below the single-pass NER baseline: SDGD obtains F1\,=\,0.251, random batching 0.320, per-type 0.292, versus 0.445 for single-pass (Table~\ref{tab:sdgd_results}, Appendix~\ref{sec:appendix_sdgd}).
7	
8	\paragraph{Merge amplification in NER.}
9	The core failure mechanism is \emph{merge amplification}: presenting the same text to the model $k$ times with different type subsets causes each pass to independently generate entity predictions, and union merge accumulates all of them into a single output. Each pass produces an independent set of span predictions; because LLM outputs are not calib
…[truncated 4344 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1053
}
```

</details>

---


### Tool call

_source line 362 · 2026-05-16T15:09:29.662999+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 363 · 2026-05-16T15:09:30.165667+00:00_

1	\section{Discussion}
2	\label{sec:discussion}
3	
4	\paragraph{Boundary conditions.}
5	The two-channel decomposition applies to cross-domain schemas; same-domain schemas (e.g., MAVEN's FrameNet-derived event types) exhibit centrality confounding that obscures per-type aggregated signals, requiring pairwise SCS or centrality adjustment (\S\ref{sec:centrality_confound}). High-BCS accuracy converges to $\approx$51\% across tested models, suggesting a task-inherent difficulty ceiling. RE's clean channel separation may partly reflect its closed-set format; the effect generalizes to document-level RE (DocRED slope $-$0.71). Prompt design modulates but does not eliminate the effect (v2 gap: $-$25.5\,pp vs.\ v1 extreme-batch gap; Appendix~\ref{sec:appendix_prompt_sensitivity}).
6	
7	\paragraph{Why does embedding similarity predict LLM confusion?}
8	Type name embeddings capture semantic proximity in the same representational space that LLMs use for in-context type resolution. When two type names are close in embedding space, we hypothesize that the model's attention mechanism may produce overlapping key--query representations for those types, increasing the probability of substitution errors. This mechanistic link explains why a simple cosine similarity metric predicts extraction failures: high SCS directly indexes the degree of representational overlap that causes confusion during decoding. Critically, the pair-level effect is modest ($R^2 \approx 7\%$ over non-zero confusion pairs) because individual substitution events are stochastic and influenced by many factors beyond type similarity. However, pairs sharing a common type exhibit correlated SCS values ($\rho = 0.35$), so when multiple high-SCS pairs co-occur in a batch, their effects aggregate constructively: noise averages out while the confusability signal is preserved. Monte Carlo simulation confirms that this inter-pair correlation produces an effective amplification of ${\sim}3\times$, yielding batch-level $R^2 \a
…[truncated 3766 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 364 · 2026-05-16T15:09:31.270817+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete review form criteria, scoring scales (soundness, excitement, overall assessment), and all rating options with their descriptions. I need the exact scoring scales and what each score means."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the complete review form criteria, scoring scales (soundness, excitement, overall assessment), and all rating options with their descriptions. I need the exact scoring scales and what each score means."
  }
}
```

</details>

---


### Tool result

_source line 365 · 2026-05-16T15:09:37.094779+00:00_

# ACL Rolling Review Form - Scoring Criteria

## Reviewer Confidence Scale
- **5**: "Positive that my evaluation is correct. I read the paper very carefully and am familiar with related work."
- **4**: "Quite sure. I tried to check the important points carefully."
- **3**: "Pretty sure, but there's a chance I missed something."
- **2**: "Willing to defend my evaluation, but it is fairly likely that I missed some details."
- **1**: "Not my area, or paper is very hard to understand."

## Soundness Scale
- **5**: "Excellent: This study is one of the most thorough I have seen, given its type."
- **4**: "Strong: This study provides sufficient support for all of its claims."
- **3**: "Acceptable: This study provides sufficient support for its main claims."
- **2**: "Poor: Some of the main claims are not sufficiently supported."
- **1**: "Major Issues: This study is not yet sufficiently thorough to warrant publication."

## Excitement Scale
- **5**: "Highly Exciting: I would recommend this paper to others and/or attend its presentation."
- **4**: "Exciting: I would mention this paper to others and/or make an effort to attend."
- **3**: "Interesting: I might mention some points of this paper to others."
- **2**: "Potentially Interesting: this paper does not resonate with me, but it might with others."
- **1**: "Not Exciting: this paper does not resonate with me."

## Overall Assessment Scale
- **5**: Consider for Award (top 2.5% papers)
- **4**: Conference acceptance
- **3**: Findings acceptance
- **2**: Resubmit next cycle
- **1**: Do not resubmit

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 5823
}
```

</details>

---


### Tool call

_source line 366 · 2026-05-16T15:09:43.377196+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/checklist.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/checklist.tex"
  }
}
```

</details>

---


### Tool result

_source line 367 · 2026-05-16T15:09:43.377632+00:00_

1	\section*{Responsible NLP Research Checklist}
2	
3	For each question, the answer is \textbf{Yes}, \textbf{No}, or \textbf{N/A}. If Yes, the relevant section is indicated. If No, a justification is provided.
4	
5	\subsection*{A \quad For Every Submission}
6	
7	\begin{enumerate}[label=\textbf{A\arabic*.},leftmargin=*,itemsep=4pt]
8	
9	\item \textbf{Did you describe the limitations of your work?}
10	
11	Yes. The Limitations section (after \S\ref{sec:conclusion}) discusses single-model reliance, modest pairwise effect sizes, cross-pool slope consistency, factorial interaction tests with TOST equivalence, decomposition scope, and metric scope.
12	
13	\item \textbf{Did you discuss any potential risks of your work?}
14	
15	N/A. This is a purely analytical study of schema-induced degradation in existing LLM IE systems. It does not introduce new models, datasets, or deployment-facing artifacts. The findings characterize failure modes and are intended to inform safer schema design.
16	
17	\item \textbf{Do the abstract and introduction summarize the paper's main claims?}
18	
19	Yes. The abstract and \S\ref{sec:introduction} state the two-channel degradation pattern (count and confusability), the cross-model consistency check, and the negative SDGD result.
20	
21	\item \textbf{Did you use AI assistants (e.g., ChatGPT, Copilot) when working on this paper?}
22	
23	Yes. An AI coding assistant was used for experiment scripting and LaTeX formatting. All scientific claims, experimental design, and analysis were conducted by the authors.
24	
25	\end{enumerate}
26	
27	\subsection*{B \quad Scientific Artifacts}
28	
29	\begin{enumerate}[label=\textbf{B\arabic*.},leftmargin=*,itemsep=4pt]
30	
31	\item \textbf{Did you cite the creators of artifacts you used?}
32	
33	Yes. Few-NERD \cite{fewnerd-2021}, FewRel \cite{fewrel-2018}, DocRED \cite{docred-2019}, MAVEN \cite{maven-2020}, Qwen3-32B \cite{qwen3-2025}, Meta-Llama-3.1-8B-Instruct \cite{llama3-2024}, vLLM \cite{vllm-2023}, and all-Mini
…[truncated 4435 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 368 · 2026-05-16T15:09:44.232090+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/prompt_appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/prompt_appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 369 · 2026-05-16T15:09:44.784831+00:00_

1	\lstset{
2	  basicstyle=\ttfamily\small,
3	  breaklines=true,
4	  breakatwhitespace=true,
5	  columns=fullflexible
6	}
7	
8	\section{Prompt Templates}
9	\label{sec:appendix_prompts}
10	
11	This appendix reproduces the complete prompt templates used for all three extraction tasks.
12	All prompts are injected into a single \texttt{user} message (no system prompt); the model's chat template adds the system/assistant framing.
13	Both versions provide a JSON-formatted type schema to the vLLM constrained-decoding engine; the schema is \emph{not} included in the natural-language prompt itself.
14	We use greedy decoding (\texttt{temperature=0}, \texttt{seed=42}) throughout.
15	
16	\medskip\noindent
17	\textbf{Notation.}
18	Placeholders are shown in \texttt{\{braces\}}.
19	Text \textbf{added in v2} (relative to v1) is marked with $\triangleright$.
20	Text \textbf{removed in v2} is marked with \sout{strikethrough}.
21	
22	\subsection{Named Entity Recognition (Few-NERD)}
23	
24	\paragraph{v1 prompt (with character offsets).}
25	
26	\begin{small}
27	\begin{lstlisting}
28	Extract all named entities from the following text.
29	Only extract entities of the following types:
30	- {type_1}: {definition_1}
31	- {type_2}: {definition_2}
32	  ...
33	
34	Text: {input_text}
35	
36	Output as JSON: [{"text": "...", "type": "...",
37	                  "start": ..., "end": ...}]
38	\end{lstlisting}
39	\end{small}
40	
41	\noindent
42	\textbf{v1 constrained-decoding schema:}
43	\begin{small}
44	\begin{lstlisting}
45	{"type": "array",
46	 "items": {"type": "object",
47	   "properties": {
48	     "text":  {"type": "string"},
49	     "type":  {"type": "string",
50	               "enum": [&lt;sorted_types>]},
51	     "start": {"type": "integer"},
52	     "end":   {"type": "integer"}},
53	   "required": ["text","type","start","end"]}}
54	\end{lstlisting}
55	\end{small}
56	
57	\paragraph{v2 prompt (text+type only).}
58	
59	\begin{small}
60	\begin{lstlisting}
61	Extract all named entities from the foll
…[truncated 5190 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 552
}
```

</details>

---


### Tool call

_source line 370 · 2026-05-16T15:09:44.785351+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "vLLM v0.20.2 release 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "vLLM v0.20.2 release 2025 2026"
  }
}
```

</details>

---


### Tool result

_source line 371 · 2026-05-16T15:09:51.039383+00:00_

Web search results for query: "vLLM v0.20.2 release 2025 2026"

Links: [{"title":"Releases · vllm-project/vllm","url":"https://github.com/vllm-project/vllm/releases"},{"title":"vLLM Release Notes - NVIDIA Docs","url":"https://docs.nvidia.com/deeplearning/frameworks/vllm-release-notes/index.html"},{"title":"vLLM on X: \"vLLM v0.20.0 is here! 752 commits from 320 contributors (123 new). 🎉 Highlights: DeepSeek V4, Hunyuan v3 preview support, CUDA 13 / PyTorch 2.11 / Transformers v5 baseline, FA4 as default MLA prefill, TurboQuant 2-bit KV (4× capacity), vLLM IR foundation. Thread 👇 https://t.co/ZMpMWgGTHM\" / X","url":"https://x.com/vllm_project/status/2048918629144805619"},{"title":"vllm · PyPI","url":"https://pypi.org/project/vllm/"},{"title":"Releases · vllm-project/vllm-omni","url":"https://github.com/vllm-project/vllm-omni/releases"},{"title":"vllm-project/vllm v0.20.0 on GitHub","url":"https://newreleases.io/project/github/vllm-project/vllm/release/v0.20.0"},{"title":"v0.20.0 - vLLM","url":"https://docs.vllm.ai/en/v0.20.0/"},{"title":"GPU - vLLM-Omni","url":"https://docs.vllm.ai/projects/vllm-omni/en/latest/getting_started/installation/gpu/"},{"title":"Release Notes — vllm-ascend","url":"https://docs.vllm.ai/projects/ascend/en/latest/user_guide/release_notes.html"},{"title":"Previous vLLM Releases | vLLM","url":"https://vllm.ai/releases"}]

Based on the search results, I found information about vLLM v0.20.2. This is a patch release on top of v0.20.0 primarily focused on DeepSeek V4 stabilization and performance improvements, along with several important bug fixes.

The release includes several key improvements:

**Performance Optimizations:**
- Multi-stream pre-attention GEMM, configurable pre-attn GEMM knob, and tuned default VLLM_MULTI_STREAM_GEMM_TOKEN_THRESHOLD
- BF16 and MXFP8 all-to-all support for FlashInfer one-sided communication
- PTX cvt instruction for faster FP32->FP4 conversion and integrated tile kernels for optimized head computation

**Bug Fixes:
…[truncated 452 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 6254
}
```

</details>

---


### Tool call

_source line 372 · 2026-05-16T15:11:22.776629+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Qwen3-32B model release 2025 Alibaba"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Qwen3-32B model release 2025 Alibaba"
  }
}
```

</details>

---


### Tool result

_source line 373 · 2026-05-16T15:11:29.507695+00:00_

Web search results for query: "Qwen3-32B model release 2025 Alibaba"

Links: [{"title":"Supported Models and Capabilities Overview - Model Studio - Alibaba Cloud - Alibaba Cloud Model Studio - Alibaba Cloud Documentation Center","url":"https://www.alibabacloud.com/help/en/model-studio/models"},{"title":"GitHub - QwenLM/Qwen3: Qwen3 is the large language model series developed by Qwen team, Alibaba Cloud. · GitHub","url":"https://github.com/QwenLM/Qwen3"},{"title":"Qwen - Wikipedia","url":"https://en.wikipedia.org/wiki/Qwen"},{"title":"Alibaba Introduces Qwen3, Setting New Benchmark in Open-Source AI with Hybrid Reasoning - Alibaba Cloud Community","url":"https://www.alibabacloud.com/blog/alibaba-introduces-qwen3-setting-new-benchmark-in-open-source-ai-with-hybrid-reasoning_602192"},{"title":"GitHub - QwenLM/Qwen3.6: Qwen3.6 is the large language model series developed by Qwen team, Alibaba Group. · GitHub","url":"https://github.com/QwenLM/Qwen3.6"},{"title":"Alibaba unveils Qwen3, a family of 'hybrid' AI reasoning models | TechCrunch","url":"https://techcrunch.com/2025/04/28/alibaba-unveils-qwen-3-a-family-of-hybrid-ai-reasoning-models/"},{"title":"GitHub - QwenLM/Qwen3-VL: Qwen3-VL is the multimodal large language model series developed by Qwen team, Alibaba Cloud. · GitHub","url":"https://github.com/QwenLM/Qwen3-VL"},{"title":"Qwen3 32B pricing & specs — Alibaba | CloudPrice","url":"https://cloudprice.net/models/alibaba-qwen3-32b"},{"title":"Qwen Models: The Complete Guide to Alibaba’s Open-Source LLMs (With a Deep Dive into Qwen 3) | Data Science Dojo","url":"https://datasciencedojo.com/blog/the-evolution-of-qwen-models/"},{"title":"Alibaba releases next-generation Qwen3 model as AI rivalry intensifies | South China Morning Post","url":"https://www.scmp.com/tech/big-tech/article/3325272/alibaba-releases-next-generation-qwen3-model-ai-rivalry-intensifies"}]

Based on the web search results, here's what I found about the Qwen3-32B model release in 2025 by Alibaba:

…[truncated 1076 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 6731
}
```

</details>

---


### Tool call

_source line 374 · 2026-05-16T15:11:45.985050+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__review_reviewer_post_to_director",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__review_reviewer_post_to_director",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 375 · 2026-05-16T15:11:46.035680+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 376 · 2026-05-16T15:14:14.387756+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "\n# Reviewer 1 审稿意见：方法严谨性、实验设计、统计有效性\n\n## 1. Summary\n\n本文首次通过分层控制实验设计，在零样本 LLM 信息抽取中将 schema 规模（count）与类型间语义混淆度（confusability）解耦，提出 Schema Confusability Score (SCS) 作为量化指标，在 NER/RE/ED 四个数据集上验证了\"两通道退化\"假说。实验设计严谨、统计报告透明，但核心效应在实际场景中偏小（典型 batch 仅 2.2pp 差异），且\"两通道可分离\"的统计支撑在 NER 上不足。\n\n## 2. Strengths\n\n**S1. 精心设计的控制实验框架。** BCS-controlled 实验固定 count 变 confusability，within-pool 分析排除 pool composition 混淆，permutation test 验证跨 pool 斜率一致性（p=0.60）。这是该领域少见的因果推断尝试。\n\n**S2. 统计透明度高。** 所有核心结论附 bootstrap CI、p 值、效应量。主动报告 r²=1.3-1.7% 的微小效应，practical magnitude 一节明确区分极端 batch（31.2pp）与典型 batch（2.2pp）。Limitations 逐条列出已知缺陷。这是负责任的科学报告。\n\n**S3. 诚实的负面结果。** SDGD 分解全面失败（NER F1: 0.445→0.251），论文不回避而是深入诊断 merge amplification 机制。Oracle routing 实验巧妙地证明了性能天花板存在但实际不可达。\n\n**S4. 多数据集、跨模型验证。** 四个数据集覆盖 NER/RE/ED，跨 Qwen3-32B 和 Llama-3.1-8B 验证，DocRED 扩展到文档级 RE。MAVEN 异常（正相关）的处理（centrality confound 识别+partial correlation 控制）方法学上成熟。\n\n**S5. 聚合效应的理论解释。** Pair-to-batch amplification 的 Monte Carlo 模拟（Appendix）给出了从 pair-level r²=7% 到 batch-level R²=22% 的定量解释，不是 hand-waving。\n\n## 3. Weaknesses\n\n**W1 [critical] \"两通道可分离\"的统计证据不对称且不充分。**\n- 具体位置：§5.4, Appendix §Factorial Analysis\n- 问题：FewRel factorial TOST p=0.003 支持可分离性，但 Few-NERD p=0.50 完全无法区分\"无交互\"和\"检验力不足\"。论文承认 Few-NERD\"did not reach significance\"但仍在 abstract 和 contribution 中声称\"two empirically separable degradation channels\"覆盖 NER 和 RE。更重要的是，§5.4 自己说 NER 中 count 和 confusability \"coupled\"（\"cleanly separable in RE but coupled in NER\"），这与\"两通道可分离\"的总体 claim 矛盾。\n- 为什么影响接收：核心 contribution 之一的证据支撑不足。如果可分离性仅在 RE（closed-set classification）上成立，而 NER（span-level extraction）上无法证明，那么 generality 有限。\n- 建议：(a) 将\"empirically separable\"限定为 RE-specific finding；(b) NER 侧改为\"two channels identified, separability not confirmed\"；(c) 考虑增加 NER 的 power analysis 说明需要多少样本才能检测到交互效应。\n\n**W2 [critical] Count curve 每个 level 仅 5 个 random batch，方差估计不可靠。**\n- 具体位置：§3.3 Experiment 1\n- 问题：每个 count level 仅 5 个 batch，batch 间方差可高达 31.2pp（极端情况）。5 个 batch 的 mean 和 SE 估计不稳定——特别是在中间 count（如 16-32）处，不同 batch 的 BCS 可能差异很大，5 个采样无法代表真实分布。\n- 论文未报告 count curve 的 batch 间方差或 CI。Figure 1a 是否有 error bar？如果没有，读者无法判断单调下降是否 robust。\n- 为什么影响接收：Count curve 是 Channel 1 的核心证据，如果 5 个 batch 的估计不稳定，Channel 1 的 claim 基础动摇。\n- 建议：(a) 报告每个 count level 的 batch 间 SD 或 95% CI；(b) 解释为什么 5 个 batch 足够（例如 batch 间方差多大？单调性是否在每个 seed 下成立？）；(c) 或者增加 batch 数。\n\n**W3 [warning] Pairwise r²=1.3-1.7% 的实际意义问题。**\n- 具体位置：Table 2, §5.2\n- 问题：r²=1.3% 意味着 SCS 仅解释了 type confusion 方差的 1.3%。虽然统计显著（n=1953），但效应极小。论文试图通过聚合解释（pair→batch amplification）来 justify 这个数字，但聚合后的 R²=22% 在 FewRel 上也仅是一个数据集的结果。\n- 更关键的是：conditioning on non-zero confusion pairs 将 r² 提升到 7%（论文自承\"conditioning on the dependent variable may inflate this\"），但后续讨论中多次使用 7% 作为\"真实效应大小\"进行 aggregation simulation。这引入了选择偏差。\n- 为什么影响评分：SCS 作为论文的核心贡献指标，其预测能力如此有限，需要更明确地讨论 what SCS does NOT capture，以及为什么不寻找更好的 proxy。\n- 建议：增加一段讨论 alternative confusability metrics（如 type definition overlap、ontological distance）可能提供更强的预测。\n\n**W4 [warning] 不同数据集使用不同 embedding 的合理性不足。**\n- 具体位置：Table 1, §3.2\n- 问题：Few-NERD 用 Qwen3-32B hidden states 计算 SCS，而 FewRel/DocRED/MAVEN 用 MiniLM。§3.2 声称\"We use MiniLM as the primary embedding\"，但 Table 2 中 Few-NERD 的 pairwise 分析用 Qwen3。这导致：\n  (a) 跨数据集的 r 值不可直接比较（不同 embedding space 有不同的各向异性特征）；\n  (b) Few-NERD 用模型自身的 embedding（construct validity 更强但有循环论证风险——模型的 representation 相似性当然预测模型的混淆）；\n  (c) 论文未解释为什么 Few-NERD 不用 MiniLM。\n- 建议：(a) 明确说明 Few-NERD 选择 Qwen3 embedding 的理由；(b) 补充 Few-NERD 使用 MiniLM 的对比结果（即使只在 appendix 中）；(c) 或者统一使用 MiniLM 以保证方法一致性。\n\n**W5 [warning] FewRel train+val 合并的 data contamination 风险未充分排除。**\n- 具体位置：§3.1, Limitations item 7\n- 问题：FewRel 2018 是一个广泛使用的数据集，很可能出现在 Qwen3 的预训练语料中。论文的 defense（train-origin accuracy 低于 val-origin，−8.8pp, p=0.06）是 borderline non-significant 且方向性证据不等于排除。\n  关键点：contamination 可能不是 uniform 的——模型可能对某些 relation types 记住了 pattern 而非 instances。在 BCS-controlled 实验中，如果 high-BCS batch 恰好包含更多\"记住\"的 types，效应可能被放大或缩小。\n- 为什么影响评分：RE 是论文最强的证据来源（\"cleanly separable\"），如果 FewRel contamination 存在，Channel 2 的 RE 证据受质疑。\n- 建议：(a) 将 contamination 分析细化到 BCS 条件——high-BCS 和 low-BCS batch 中 train-origin/val-origin type 的比例和表现是否不同？(b) 考虑使用 DocRED（2019，contamination 风险稍低）作为 primary RE 证据。\n\n**W6 [warning] 31.2pp extreme-batch gap 的 framing 存在误导风险。**\n- 具体位置：Abstract, §1, §5.3, Table in Appendix\n- 问题：Abstract 第一次出现数字时写\"quartile BCS gap is −5.3 pp\"然后\"Table ref\"指向 31.2pp 的极端 batch 结果。Introduction 写\"up to 31.2 pp under extreme-batch construction\"。虽然 §5.3 明确说明\"reflects maximum BCS contrast, not the typical batch experience\"，但 abstract/intro 给读者的第一印象是 confusability 有 31.2pp 的实际影响。\n  实际上：(a) typical gap = 2.2pp；(b) quartile gap = 5.3pp；(c) extreme = 31.2pp。论文的 honest reporting 值得肯定，但 presentation order 的选择仍有误导倾向。\n- 建议：在 abstract 中先报 typical/quartile magnitude，再以\"under extreme construction\"引出上界，明确标注这是 adversarial construction 而非自然场景。\n\n**W7 [info] 单种子评估（seed=42）的可靠性。**\n- 具体位置：§3.4\n- 问题：所有实验使用 greedy decoding + seed=42，variance across seeds not quantified。虽然 greedy decoding 理论上是 deterministic 的（给定相同 input），但 vLLM 的 FP8 quantization 和 GPU kernel scheduling 可能引入微小变异。\n- 论文明确声明这一限制但未量化影响。\n- 建议：选取一个关键实验（如 BCS-controlled FewRel count=16），用 3-5 个 seed 运行确认结果稳定。\n\n**W8 [info] Bootstrap 参数不一致（B=10,000 vs B=1,000）。**\n- 具体位置：§3.4\n- 问题：pair-level 用 B=10,000 而 batch-level 用 B=1,000。虽然 B=1,000 通常足够（Efron & Tibshirani 推荐 CIs 至少 1,000），但同一论文内应统一标准或 justify 差异。\n- 影响极小，属格式问题。\n\n## 4. Questions to Authors\n\n**Q1.** Few-NERD count curve 的 Figure 1a 中是否有 error bar / confidence band？如果没有，5 个 batch 的 batch-间方差有多大？特别是在 count=22 和 count=44 这些中间值处。\n\n**Q2.** Few-NERD pairwise 分析为什么选 Qwen3 而非 MiniLM？是否有 MiniLM-on-Few-NERD 的结果？如果有，r 值是否更高/更低？\n\n**Q3.** Aggregation simulation 中使用 inter-pair SCS correlation ρ=0.35 来估算 batch-level amplification。这个 0.35 是从哪个数据集估得的？是否对结果敏感（例如 ρ=0.2 或 ρ=0.5 时 simulated batch R² 变化多少）？\n\n**Q4.** BCS-controlled 极端 batch（31.2pp）中，high-BCS batch 的具体 relation types 是什么？是否存在某些 types 在 high-BCS 条件下被系统性地选入（例如语义相近的 Wikidata properties 子集），从而引入 domain confound？\n\n**Q5.** SDGD 的 merge amplification 分析中，per-type extraction 的 recall=0.586 显著高于 single-pass 的 0.368。这是否意味着 single-pass 本身存在 recall ceiling 问题（可能由 prompt length 导致）？如果是，count curve 中的 recall 下降可能不完全是\"count-driven\"而是 prompt length driven。\n\n**Q6.** TOST equivalence margin ±3pp 的选择依据是什么？如果 margin 设为 ±2pp 或 ±5pp，FewRel 的 equivalence test 结论是否改变？\n\n## 5. Missing References\n\n- **Banerjee et al. (2025)** \"Benchmarking LLM-based Schema Extraction\" — 如果存在的话，应讨论是否有其他人做了类似的 controlled study。\n- **Effect size reporting 方法论**：建议引用 Cohen (1988) 或 Lakens (2013) 关于 small effect size 的实际意义讨论，为 r²=1.3% 的 framing 提供方法论背景。\n- **Multiple testing correction 方法论**：如果声称各数据集是\"independent replication\"而不做 FDR 校正，应引用 Bonferroni vs independent replication 的方法论讨论（如 Perneger 1998 或 Rothman 1990）。\n\n## 6. Overall Assessment\n\n**Overall**: 3 (Findings acceptance)\n**Confidence**: 4 (Quite sure. I tried to check the important points carefully.)\n\n**一句话总结**: 实验设计严谨、统计报告透明的分析型论文，但核心效应在实践中很小（2.2pp typical），且\"两通道可分离\"的核心 claim 在 NER 上缺乏统计支撑。\n\n**Rationale**: 论文的主要贡献在于方法论——提出第一个控制实验框架来解耦 count 和 confusability。这有价值。但两个问题制约了 acceptance：(1) 实际效应小到对 practitioners 意义有限（typical 2.2pp），论文的 practical implications 更多是\"awareness\"而非 actionable guidance；(2) \"两通道可分离\"作为核心 claim，仅在 RE 上有 TOST 支持，NER 上无法证明。如果论文将自身定位为\"RE-specific finding with suggestive NER evidence\"会更准确，但这也削弱了 contribution 的 scope。\n\n建议：作为 Findings paper 接收。如要升级为 main conference，需 (a) 增加 NER 的 factorial power 或放弃全面可分离性 claim；(b) 统一 embedding 选择或充分 justify；(c) count curve 补充方差信息。\n\n## 7. Detailed Comments（逐节）\n\n### Abstract\n- \"first study to formally isolate type confusability from type count\"——technically correct for zero-shot LLM IE，但 LLM-PEE (2025) 已用 type embedding similarity 做分组（虽未做 controlled isolation），建议加 qualifier。\n- \"two empirically separable degradation channels\"——如 W1 所述，NER 上未证明 separability，建议改为\"two identified channels, separable under RE closed-set classification\"。\n\n### §3.2 SCS\n- \"SCS uses name-only embeddings as a practical simplification\"——name+definition 的 ablation（Appendix）显示 Few-NERD 上 name-only 更好（-0.023），MAVEN/FewRel 上 definition 更好。论文结论是\"no systematic benefit\"——但这可能是因为 definition quality 参差不齐，而非 name-only 真的已经 sufficient。\n\n### §3.4 Model and Inference\n- \"vLLM v0.20.2\"——已验证存在（2026 年 release）。✓\n- \"96 GB GPU\"——Checklist 中指明 RTX PRO 6000 Blackwell，合理。✓\n- p-value 格式：大部分一致（\"p = 0.025\"），但 Appendix 中有\"p = .003\"（无前导零），建议统一。\n\n### §5.2 Pairwise\n- \"Spearman correlations corroborate: ρ = 0.144–0.227 across all pairs, strengthening to ρ = 0.27–0.31 among pairs with nonzero confusion\"——后半句有选择偏差风险，论文自知但仍在正文报告，建议移至 appendix 或更明确地 discount。\n\n### §5.3 BCS-Controlled\n- \"BCS explains 44–53% of cross-batch variance (R²=0.525 at count 16)\"——这是 DocRED 的结果，显著高于 FewRel (R²=0.218)。论文推测\"wider confusability range\"但也可能是 DocRED 的 96 types 中有特定 highly-confusable clusters。需要更多分析来排除 DocRED-specific artifacts。\n\n### §6 SDGD\n- \"Random batching outperforms confusability-aware SDGD on NER (0.320 vs. 0.251)\"——这个结果很有趣但解释可能不完整。SDGD 产生的 batch 数更少（8→4 in v2），是否 batch 大小差异也是因素？论文应控制 batch 数完全相同的条件。\n- Table 4 中 graph coloring 的 mean BCS (0.552) vs random (0.559) 差异仅 0.006——这本身就说明 graph coloring 在 80-type、5-batch 粒度下几乎无法实现有意义的 BCS 降低。论文需要讨论这一 ceiling effect。\n\n### Limitations\n- 写得全面且诚实。\"Multiple comparisons\"段落的 rationale 合理但应引用方法论文献支持。\n- Item 3 提到 TOST on Few-NERD factorial \"did not reach significance (p = 0.50)\"——这是指 INTERACTION 的 p 值还是 TOST 的 p 值？如果是 TOST equivalence p=0.50 则无法 reject non-equivalence，这与 abstract 的\"separable\"claim 直接矛盾。请澄清。\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3/5 | 方法论和统计整体合格，但核心 claim（两通道可分离）在 NER 上缺乏足够支撑；pairwise 效应极小 |\n| Excitement | 3/5 | 首次在 zero-shot IE 中做 controlled confusability isolation，有方法论贡献；但实际效应小（2.2pp typical）限制了 impact |\n| Reproducibility | 4/5 | 数据集公开、prompt 完整、统计方法详述；唯一缺失是代码（承诺 acceptance 后释放）和 multi-seed 验证 |\n| Overall | 3/5 | Findings 级别接收 |\n| Confidence | 4/5 | 仔细检查了实验设计和统计方法 |\n",
  "reviewer_id": "1",
  "project": "schema-dag-extraction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "\n# Reviewer 1 审稿意见：方法严谨性、实验设计、统计有效性\n\n## 1. Summary\n\n本文首次通过分层控制实验设计，在零样本 LLM 信息抽取中将 schema 规模（count）与类型间语义混淆度（confusability）解耦，提出 Schema Confusability Score (SCS) 作为量化指标，在 NER/RE/ED 四个数据集上验证了\"两通道退化\"假说。实验设计严谨、统计报告透明，但核心效应在实际场景中偏小（典型 batch 仅 2.2pp 差异），且\"两通道可分离\"的统计支撑在 NER 上不足。\n\n## 2. Strengths\n\n**S1. 精心设计的控制实验框架。** BCS-controlled 实验固定 count 变 confusability，within-pool 分析排除 pool composition 混淆，permutation test 验证跨 pool 斜率一致性（p=0.60）。这是该领域少见的因果推断尝试。\n\n**S2. 统计透明度高。** 所有核心结论附 bootstrap CI、p 值、效应量。主动报告 r²=1.3-1.7% 的微小效应，practical magnitude 一节明确区分极端 batch（31.2pp）与典型 batch（2.2pp）。Limitations 逐条列出已知缺陷。这是负责任的科学报告。\n\n**S3. 诚实的负面结果。** SDGD 分解全面失败（NER F1: 0.445→0.251），论文不回避而是深入诊断 merge amplification 机制。Oracle routing 实验巧妙地证明了性能天花板存在但实际不可达。\n\n**S4. 多数据集、跨模型验证。** 四个数据集覆盖 NER/RE/ED，跨 Qwen3-32B 和 Llama-3.1-8B 验证，DocRED 扩展到文档级 RE。MAVEN 异常（正相关）的处理（centrality confound 识别+partial correlation 控制）方法学上成熟。\n\n**S5. 聚合效应的理论解释。** Pair-to-batch amplification 的 Monte Carlo 模拟（Appendix）给出了从 pair-level r²=7% 到 batch-level R²=22% 的定量解释，不是 hand-waving。\n\n## 3. Weaknesses\n\n**W1 [critical] \"两通道可分离\"的统计证据不对称且不充分。**\n- 具体位置：§5.4, Appendix §Factorial Analysis\n- 问题：FewRel factorial TOST p=0.003 支持可分离性，但 Few-NERD p=0.50 完全无法区分\"无交互\"和\"检验力不足\"。论文承认 Few-NERD\"did not reach significance\"但仍在 abstract 和 contribution 中声称\"two empirically separable degradation channels\"覆盖 NER 和 RE。更重要的是，§5.4 自己说 NER 中 count 和 confusability \"coupled\"（\"cleanly separable in RE but coupled in NER\"），这与\"两通道可分离\"的总体 claim 矛盾。\n- 为什么影响接收：核心 contribution 之一的证据支撑不足。如果可分离性仅在 RE（closed-set classification）上成立，而 NER（span-level extraction）上无法证明，那么 generality 有限。\n- 建议：(a) 将\"empirically separable\"限定为 RE-specific finding；(b) NER 侧改为\"two channels identified, separability not confirmed\"；(c) 考虑增加 NER 的 power analysis 说明需要多少样本才能检测到交互效应。\n\n**W2 [critical] Count curve 每个 level 仅 5 个 random batch，方差估计不可靠。**\n- 具体位置：§3.3 Experiment 1\n- 问题：每个 count level 仅 5 个 batch，batch 间方差可高达 31.2pp（极端情况）。5 个 batch 的 mean 和 SE 估计不稳定——特别是在中间 count（如 16-32）处，不同 batch 的 BCS 可能差异很大，5 个采样无法代表真实分布。\n- 论文未报告 count curve 的 batch 间方差或 CI。Figure 1a 是否有 error bar？如果没有，读者无法判断单调下降是否 robust。\n- 为什么影响接收：Count curve 是 Channel 1 的核心证据，如果 5 个 batch 的估计不稳定，Channel 1 的 claim 基础动摇。\n- 建议：(a) 报告每个 count level 的 batch 间 SD 或 95% CI；(b) 解释为什么 5 个 batch 足够（例如 batch 间方差多大？单调性是否在每个 seed 下成立？）；(c) 或者增加 batch 数。\n\n**W3 [warning] Pairwise r²=1.3-1.7% 的实际意义问题。**\n- 具体位置：Table 2, §5.2\n- 问题：r²=1.3% 意味着 SCS 仅解释了 type confusion 方差的 1.3%。虽然统计显著（n=1953），但效应极小。论文试图通过聚合解释（pair→batch amplification）来 justify 这个数字，但聚合后的 R²=22% 在 FewRel 上也仅是一个数据集的结果。\n- 更关键的是：conditioning on non-zero confusion pairs 将 r² 提升到 7%（论文自承\"conditioning on the dependent variable may inflate this\"），但后续讨论中多次使用 7% 作为\"真实效应大小\"进行 aggregation simulation。这引入了选择偏差。\n- 为什么影响评分：SCS 作为论文的核心贡献指标，其预测能力如此有限，需要更明确地讨论 what SCS does NOT capture，以及为什么不寻找更好的 proxy。\n- 建议：增加一段讨论 alternative confusability metrics（如 type definition overlap、ontological distance）可能提供更强的预测。\n\n**W4 [warning] 不同数据集使用不同 embedding 的合理性不足。**\n- 具体位置：Table 1, §3.2\n- 问题：Few-NERD 用 Qwen3-32B hidden states 计算 SCS，而 FewRel/DocRED/MAVEN 用 MiniLM。§3.2 声称\"We use MiniLM as the primary embedding\"，但 Table 2 中 Few-NERD 的 pairwise 分析用 Qwen3。这导致：\n  (a) 跨数据集的 r 值不可直接比较（不同 embedding space 有不同的各向异性特征）；\n  (b) Few-NERD 用模型自身的 embedding（construct validity 更强但有循环论证风险——模型的 representation 相似性当然预测模型的混淆）；\n  (c) 论文未解释为什么 Few-NERD 不用 MiniLM。\n- 建议：(a) 明确说明 Few-NERD 选择 Qwen3 embedding 的理由；(b) 补充 Few-NERD 使用 MiniLM 的对比结果（即使只在 appendix 中）；(c) 或者统一使用 MiniLM 以保证方法一致性。\n\n**W5 [warning] FewRel train+val 合并的 data contamination 风险未充分排除。**\n- 具体位置：§3.1, Limitations item 7\n- 问题：FewRel 2018 是一个广泛使用的数据集，很可能出现在 Qwen3 的预训练语料中。论文的 defense（train-origin accuracy 低于 val-origin，−8.8pp, p=0.06）是 borderline non-significant 且方向性证据不等于排除。\n  关键点：contamination 可能不是 uniform 的——模型可能对某些 relation types 记住了 pattern 而非 instances。在 BCS-controlled 实验中，如果 high-BCS batch 恰好包含更多\"记住\"的 types，效应可能被放大或缩小。\n- 为什么影响评分：RE 是论文最强的证据来源（\"cleanly separable\"），如果 FewRel contamination 存在，Channel 2 的 RE 证据受质疑。\n- 建议：(a) 将 contamination 分析细化到 BCS 条件——high-BCS 和 low-BCS batch 中 train-origin/val-origin type 的比例和表现是否不同？(b) 考虑使用 DocRED（2019，contamination 风险稍低）作为 primary RE 证据。\n\n**W6 [warning] 31.2pp extreme-batch gap 的 framing 存在误导风险。**\n- 具体位置：Abstract, §1, §5.3, Table in Appendix\n- 问题：Abstract 第一次出现数字时写\"quartile BCS gap is −5.3 pp\"然后\"Table ref\"指向 31.2pp 的极端 batch 结果。Introduction 写\"up to 31.2 pp under extreme-batch construction\"。虽然 §5.3 明确说明\"reflects maximum BCS contrast, not the typical batch experience\"，但 abstract/intro 给读者的第一印象是 confusability 有 31.2pp 的实际影响。\n  实际上：(a) typical gap = 2.2pp；(b) quartile gap = 5.3pp；(c) extreme = 31.2pp。论文的 honest reporting 值得肯定，但 presentation order 的选择仍有误导倾向。\n- 建议：在 abstract 中先报 typical/quartile magnitude，再以\"under extreme construction\"引出上界，明确标注这是 adversarial construction 而非自然场景。\n\n**W7 [info] 单种子评估（seed=42）的可靠性。**\n- 具体位置：§3.4\n- 问题：所有实验使用 greedy decoding + seed=42，variance across seeds not quantified。虽然 greedy decoding 理论上是 deterministic 的（给定相同 input），但 vLLM 的 FP8 quantization 和 GPU kernel scheduling 可能引入微小变异。\n- 论文明确声明这一限制但未量化影响。\n- 建议：选取一个关键实验（如 BCS-controlled FewRel count=16），用 3-5 个 seed 运行确认结果稳定。\n\n**W8 [info] Bootstrap 参数不一致（B=10,000 vs B=1,000）。**\n- 具体位置：§3.4\n- 问题：pair-level 用 B=10,000 而 batch-level 用 B=1,000。虽然 B=1,000 通常足够（Efron & Tibshirani 推荐 CIs 至少 1,000），但同一论文内应统一标准或 justify 差异。\n- 影响极小，属格式问题。\n\n## 4. Questions to Authors\n\n**Q1.** Few-NERD count curve 的 Figure 1a 中是否有 error bar / confidence band？如果没有，5 个 batch 的 batch-间方差有多大？特别是在 count=22 和 count=44 这些中间值处。\n\n**Q2.** Few-NERD pairwise 分析为什么选 Qwen3 而非 MiniLM？是否有 MiniLM-on-Few-NERD 的结果？如果有，r 值是否更高/更低？\n\n**Q3.** Aggregation simulation 中使用 inter-pair SCS correlation ρ=0.35 来估算 batch-level amplification。这个 0.35 是从哪个数据集估得的？是否对结果敏感（例如 ρ=0.2 或 ρ=0.5 时 simulated batch R² 变化多少）？\n\n**Q4.** BCS-controlled 极端 batch（31.2pp）中，high-BCS batch 的具体 relation types 是什么？是否存在某些 types 在 high-BCS 条件下被系统性地选入（例如语义相近的 Wikidata properties 子集），从而引入 domain confound？\n\n**Q5.** SDGD 的 merge amplification 分析中，per-type extraction 的 recall=0.586 显著高于 single-pass 的 0.368。这是否意味着 single-pass 本身存在 recall ceiling 问题（可能由 prompt length 导致）？如果是，count curve 中的 recall 下降可能不完全是\"count-driven\"而是 prompt length driven。\n\n**Q6.** TOST equivalence margin ±3pp 的选择依据是什么？如果 margin 设为 ±2pp 或 ±5pp，FewRel 的 equivalence test 结论是否改变？\n\n## 5. Missing References\n\n- **Banerjee et al. (2025)** \"Benchmarking LLM-based Schema Extraction\" — 如果存在的话，应讨论是否有其他人做了类似的 controlled study。\n- **Effect size reporting 方法论**：建议引用 Cohen (1988) 或 Lakens (2013) 关于 small effect size 的实际意义讨论，为 r²=1.3% 的 framing 提供方法论背景。\n- **Multiple testing correction 方法论**：如果声称各数据集是\"independent replication\"而不做 FDR 校正，应引用 Bonferroni vs independent replication 的方法论讨论（如 Perneger 1998 或 Rothman 1990）。\n\n## 6. Overall Assessment\n\n**Overall**: 3 (Findings acceptance)\n**Confidence**: 4 (Quite sure. I tried to check the important points carefully.)\n\n**一句话总结**: 实验设计严谨、统计报告透明的分析型论文，但核心效应在实践中很小（2.2pp typical），且\"两通道可分离\"的核心 claim 在 NER 上缺乏统计支撑。\n\n**Rationale**: 论文的主要贡献在于方法论——提出第一个控制实验框架来解耦 count 和 confusability。这有价值。但两个问题制约了 acceptance：(1) 实际效应小到对 practitioners 意义有限（typical 2.2pp），论文的 practical implications 更多是\"awareness\"而非 actionable guidance；(2) \"两通道可分离\"作为核心 claim，仅在 RE 上有 TOST 支持，NER 上无法证明。如果论文将自身定位为\"RE-specific finding with suggestive NER evidence\"会更准确，但这也削弱了 contribution 的 scope。\n\n建议：作为 Findings paper 接收。如要升级为 main conference，需 (a) 增加 NER 的 factorial power 或放弃全面可分离性 claim；(b) 统一 embedding 选择或充分 justify；(c) count curve 补充方差信息。\n\n## 7. Detailed Comments（逐节）\n\n### Abstract\n- \"first study to formally isolate type confusability from type count\"——technically correct for zero-shot LLM IE，但 LLM-PEE (2025) 已用 type embedding similarity 做分组（虽未做 controlled isolation），建议加 qualifier。\n- \"two empirically separable degradation channels\"——如 W1 所述，NER 上未证明 separability，建议改为\"two identified channels, separable under RE closed-set classification\"。\n\n### §3.2 SCS\n- \"SCS uses name-only embeddings as a practical simplification\"——name+definition 的 ablation（Appendix）显示 Few-NERD 上 name-only 更好（-0.023），MAVEN/FewRel 上 definition 更好。论文结论是\"no systematic benefit\"——但这可能是因为 definition quality 参差不齐，而非 name-only 真的已经 sufficient。\n\n### §3.4 Model and Inference\n- \"vLLM v0.20.2\"——已验证存在（2026 年 release）。✓\n- \"96 GB GPU\"——Checklist 中指明 RTX PRO 6000 Blackwell，合理。✓\n- p-value 格式：大部分一致（\"p = 0.025\"），但 Appendix 中有\"p = .003\"（无前导零），建议统一。\n\n### §5.2 Pairwise\n- \"Spearman correlations corroborate: ρ = 0.144–0.227 across all pairs, strengthening to ρ = 0.27–0.31 among pairs with nonzero confusion\"——后半句有选择偏差风险，论文自知但仍在正文报告，建议移至 appendix 或更明确地 discount。\n\n### §5.3 BCS-Controlled\n- \"BCS explains 44–53% of cross-batch variance (R²=0.525 at count 16)\"——这是 DocRED 的结果，显著高于 FewRel (R²=0.218)。论文推测\"wider confusability range\"但也可能是 DocRED 的 96 types 中有特定 highly-confusable clusters。需要更多分析来排除 DocRED-specific artifacts。\n\n### §6 SDGD\n- \"Random batching outperforms confusability-aware SDGD on NER (0.320 vs. 0.251)\"——这个结果很有趣但解释可能不完整。SDGD 产生的 batch 数更少（8→4 in v2），是否 batch 大小差异也是因素？论文应控制 batch 数完全相同的条件。\n- Table 4 中 graph coloring 的 mean BCS (0.552) vs random (0.559) 差异仅 0.006——这本身就说明 graph coloring 在 80-type、5-batch 粒度下几乎无法实现有意义的 BCS 降低。论文需要讨论这一 ceiling effect。\n\n### Limitations\n- 写得全面且诚实。\"Multiple comparisons\"段落的 rationale 合理但应引用方法论文献支持。\n- Item 3 提到 TOST on Few-NERD factorial \"did not reach significance (p = 0.50)\"——这是指 INTERACTION 的 p 值还是 TOST 的 p 值？如果是 TOST equivalence p=0.50 则无法 reject non-equivalence，这与 abstract 的\"separable\"claim 直接矛盾。请澄清。\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3/5 | 方法论和统计整体合格，但核心 claim（两通道可分离）在 NER 上缺乏足够支撑；pairwise 效应极小 |\n| Excitement | 3/5 | 首次在 zero-shot IE 中做 controlled confusability isolation，有方法论贡献；但实际效应小（2.2pp typical）限制了 impact |\n| Reproducibility | 4/5 | 数据集公开、prompt 完整、统计方法详述；唯一缺失是代码（承诺 acceptance 后释放）和 multi-seed 验证 |\n| Overall | 3/5 | Findings 级别接收 |\n| Confidence | 4/5 | 仔细检查了实验设计和统计方法 |\n",
    "reviewer_id": "1",
    "project": "schema-dag-extraction"
  }
}
```

</details>

---


### Tool result

_source line 377 · 2026-05-16T15:14:18.713575+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4325
}
```

</details>

---


### Assistant

_source line 378 · 2026-05-16T15:14:26.153765+00:00_

审稿意见已提交给 Review Director。

核心判断：**Findings 级别接收（Overall 3/5）**。论文实验设计严谨、统计报告透明，但两个核心问题制约主会议接收：(1) 实际效应很小（typical batch 仅 2.2pp 差异）；(2) "两通道可分离"的 claim 仅在 RE 上有 TOST 支持，NER factorial p=0.50 无法区分"无交互"和"检验力不足"。标注了 2 个 critical issues、6 个 warnings、6 个 questions to authors。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1"
}
```

</details>

---


## Round 14

## Round 14

4 recorded events


### User

_source line 379 · 2026-05-16T15:15:24.598647+00:00_

[Round 1 审稿请求]:
以下是 Reviewer 2 的完整审稿意见。请逐条回应：对每条 Weakness 标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。也请对 Strengths、Questions、Missing References 中你有不同看法的部分发表意见。

---

# Reviewer 2 — Round 1 审稿意见

**审查侧重**: 新颖性、Framing、Related Work、完整性

## 2. Strengths

- **S1**: 实验设计严谨——BCS-controlled experiments 有效隔离了 count 和 confusability 变量，within-pool analysis 控制了 pool composition confound，permutation test 验证了跨池 slope 一致性
- **S2**: 负面结果的诚实报告——SDGD 在 NER 上的失败及原因分析（merge amplification）对社区有实际指导价值
- **S3**: 统计方法全面——bootstrap CIs、TOST equivalence testing、cluster bootstrap、Monte Carlo simulation 验证 pair-to-batch aggregation，方法论素养高于平均水平
- **S4**: MAVEN centrality confound 的识别和解决（§4.5 + Appendix D）展示了对 embedding space 结构问题的深入理解
- **S5**: Limitations section 覆盖 7 项关键弱点 + multiple comparisons 讨论，自我批评充分
- **S6**: 跨模型验证（Qwen3-32B + Llama-3.1-8B）和跨 prompt 验证（v1/v2）增强了结论鲁棒性

## 3. Weaknesses

### **W1** [critical] 核心 novelty 有限：two-channel decomposition 近似 trivial
"更多类型导致 recall 下降"已被 Li et al. (2023) 和 LLM-PEE (2025) 观察到；"语义相似的类型容易混淆"是 NLP 分类任务的常识性直觉。本文的贡献在于用 controlled design 量化这一直觉，但 decomposition 本身的概念 novelty 有限。
**证据**: §2 Related Work 已承认 "SCS shares its formal definition...with the partitioning criterion used in LLM-PEE"。Contribution #1 称之为 "controlled evidence for two degradation channels"——这更像是 empirical confirmation 而非 conceptual advancement。
**为什么影响接收**: EMNLP 要求 excitement/novelty 达到一定阈值。如果核心贡献是 "用受控实验证实了一个广泛预期的直觉"，excitement 打分将偏低。

### **W2** [critical] Framing 过度强调 extreme-batch 结果，弱化 typical-batch 现实
Abstract 第一个具体数据点是 "quartile BCS gap is −5.3pp"，而 "typical random batches differ by ≈2.2pp" 被放在后面。极端批次 31.2pp 出现在 Table ref 引用中。Introduction 的 finding (1) 以 "up to 31.2pp under extreme-batch construction" 结尾。
**问题**: 对于实践者来说，真实工作负载中遇到的效应量是 ~2.2pp（约 7% of extreme-batch gap）。这个 magnitude 在许多应用场景中可能不具备实际意义。论文未讨论这 2.2pp 是否超过了 practitioners 的 noise tolerance。

### **W3** [critical] 非显著结果被不恰当地 frame 为正面贡献
Contribution #4: "RE batch composition yields a directional +1.4pp gain (p≈0.19)"。Abstract 也提到此结果。Conclusion 重复。
**问题**: p=0.19 远未达到任何常规显著性阈值。将非显著结果列为 contribution 违反了学术写作规范。"directional" 这个修饰词不能将 n.s. 结果升格为 contribution。此外，graph coloring 方案在 15 个 random seeds 中仅排第 13——比大多数随机方案更差。

### **W4** [warning] "Empirically separable channels" 的证据不均衡
- FewRel factorial TOST: p=0.003，支持 additive separability ✓
- Few-NERD factorial: p=0.50，不支持 ✗
- Few-NERD within-dataset 2×2: p_TOST=0.56，不支持 ✗
三项检验中两项失败。

### **W5** [warning] Cross-model claim 省略 NER Channel 2 失败
Abstract 表述相对准确，但 Conclusion "replicate across model families" 暗示全任务复现。

### **W6** [warning] SCS 作为 metric 的增量贡献存疑
SCS = cosine similarity of type name embeddings，与 LLM-PEE partitioning criterion 形式相同。Pairwise R² = 1.3-1.7%。

### **W7** [warning] FewRel train+val 合并的 data contamination 风险
p=0.06 defense 是 borderline non-significant。

### **W8** [warning] Abstract 数字密度过高
至少 12 个数字/区间，严重超出 abstract 信息承载力。

## 4. Questions

Q1: Typical-batch 2.2pp 差异是否超过下游应用 noise tolerance？
Q2: 为什么不将 entity frequency, prompt position 等纳入 multivariate model？
Q3: Oracle routing 对实践者的指导价值是什么？
Q4: Few-NERD factorial p=0.50 的 power analysis？
Q5: 为什么 NER 用 Qwen3 embedding 而 RE/ED 用 MiniLM？

## 5. Missing References

M1: "From Haystack to Needle: Label Space Reduction for Zero-shot Classification" (2025)
M2: "Many-Shot In-Context Learning" (NeurIPS 2024)
M3: Label confusion / class similarity 在传统 ML 中的文献
M4: SGD/SGD-X 讨论深度不足

## 6. Overall Assessment
**Borderline reject (2.5/5)**，置信度 4/5
**核心问题**: novelty 有限 + framing 偏差 + 非显著结果作为 contribution

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 380 · 2026-05-16T15:17:25.569849+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "\n# Reviewer 1 对 Reviewer 2 意见的逐条回应\n\n## 对 Strengths 的意见\n\nR2 的 S1-S6 与我的评估高度一致，无异议。特别是 S2（负面结果诚实报告）和 S3（统计方法全面）是本文的显著优势。\n\n---\n\n## 对 Weaknesses 的逐条回应\n\n### [REBUT] R2-W1: \"Two-channel decomposition 近似 trivial\"\n\nR2 的批评有道理但过于严厉。几点反驳：\n\n1. **\"直觉上显然\"≠\"实验上已证\"。** \"更多类型→recall 下降\"确实被 Li et al. (2023) 观察过，但他们未控制 confusability；LLM-PEE (2025) 用 similarity 做分组但未做 controlled isolation。本文的贡献在于**方法论层面**——提出第一个能将 count 和 confusability 效应正交分离的实验范式。这类似于医学中 RCT 相对于观察性研究的价值。\n\n2. **但我承认 novelty 确实有限。** controlled confirmation 的价值取决于结果是否 surprising。如果结果完美符合预期（两通道可分离、confusability 有强效应），那 confirmation 的增量信息很少。而本文的结果实际上有 nuance：(a) NER 上两通道 NOT cleanly separable；(b) 实际效应仅 2.2pp；(c) SDGD 失败。这些 nuances 是 non-trivial findings，不是简单 confirmation。\n\n3. **SCS 作为 metric 的 novelty**：R2 正确指出 SCS 与 LLM-PEE 形式相同（§2 原文承认）。但 SCS 在本文中不是 contribution 本身，而是实验工具。类似于用 t-test 做对照实验——t-test 不新但实验是新的。\n\n**结论**：R2 的 novelty concern 有效，但程度上我认为是 borderline 而非 deal-breaker。Controlled methodology + negative findings (SDGD) + centrality confound 识别 = 足够的 intellectual contribution for Findings-level publication。不够 exciting for main conference。\n\n---\n\n### [AGREE] R2-W2: Framing 过度强调 extreme-batch 结果\n\n完全同意。我在自己的 W6 中提出了同一问题。Abstract 和 Introduction 的 presentation order 使读者首先接触到大数字（31.2pp），而实践中典型效应仅 2.2pp。论文 §5.3 的 honest qualification 来得太晚——多数读者（包括 AC/meta-reviewer）可能只仔细读 abstract+intro。\n\n补充一点 R2 未提到的：Introduction 的 opening paragraph 报告了 count curve 的 overall degradation（\"recall drops from 0.72 to 0.42\"）——这些是 Channel 1 (count) 的数字，不是 Channel 2 (confusability) 的。但论文标题问的是 \"Does Type Confusability Shape...\"——如果 confusability 的 typical effect 只有 2.2pp 而 count 的 effect 是 35+pp，那 confusability 作为 degradation 的\"shaping\"因素其重要性需要被 contextualized。\n\n---\n\n### [REBUT] R2-W3: 非显著结果被不恰当 frame 为正面 contribution\n\nR2 的批评方向正确但解读有偏差。让我重新看 Contribution #4 原文（§1）：\n\n> \"Schema decomposition proves structurally infeasible for NER (merge amplification collapses precision from 0.56 to 0.21) **and yields no statistically significant improvement for RE** (graph-coloring: +1.4pp, p≈0.19). Oracle routing (+29.8pp) confirms the performance ceiling exists but highlights the gap between theoretical and achievable gains.\"\n\n这里 +1.4pp (p≈0.19) 是被引用为**负面证据**——\"no statistically significant improvement\"。Contribution #4 的实质是**诊断性发现**：(a) NER 失败因 merge amplification；(b) RE 的 confusability-aware grouping 无显著增益；(c) 但 oracle routing 证明 ceiling 存在。整个 contribution 是一个 negative/diagnostic finding，不是在 claim +1.4pp 是正面成果。\n\n**但我部分同意**：Abstract 中的 \"RE batch composition yields a directional +1.4pp gain\" 措辞确实可被误读为正面 claim。\"directional\" 这个词暗示了方向性收益。建议改为 \"confusability-aware grouping yields no significant improvement (+1.4pp, p≈0.19, n.s.)\"。\n\n此外，R2 指出 graph coloring \"排第 13/15 个 random seeds\"——这确实是一个 damning detail，论文应在正文而非仅在 Table caption 中讨论。如果 confusability-aware 方案比大多数 random 方案差，那 SCS 指导的分组在这个粒度下甚至是 counterproductive 的。\n\n---\n\n### [AGREE] R2-W4: \"Empirically separable\" 证据不均衡\n\n完全同意，与我的 W1 (critical) 一致。补充：\n\nR2 列出三项检验中两项失败。但论文的 defense 是 Few-NERD factorial \"underpowered\"（Appendix）。问题是：**如果你承认检验力不足，就不能将 n.s. 结果同时用来 claim separability（在 abstract/contributions 中）和 dismiss 为 underpowered（在 appendix 中）。**\n\n论文 §5.4 自己写道 \"cleanly separable in RE but coupled in NER\"——这是准确的。但 abstract 的 \"two empirically separable degradation channels\" 没有这个 qualifier。这是一个 overclaim。\n\n---\n\n### [AGREE] R2-W5: Cross-model claim 省略 NER Channel 2 失败\n\n同意。Conclusion 的 \"replicate across model families\" 后面列举的证据 \"(Llama-3.1-8B: count r = 0.725, confusability Δ = −27pp)\" 确实只包含 RE 数据。Limitations item 1 承认 \"Channel 2 was not robustly detectable on NER at 8B scale\"，但这个 caveat 在 conclusion 中消失了。\n\n不过，这个问题的 severity 我认为是 warning 而非 critical——因为 Limitations 确实讨论了，只是 conclusion 的 wording 不够精确。\n\n---\n\n### [REBUT] R2-W6: SCS 作为 metric 的增量贡献存疑\n\nR2 的批评逻辑是：SCS = cosine similarity（与 LLM-PEE 相同），且 r² 很低，所以 SCS 无贡献。\n\n反驳：\n1. 论文 §2 已明确声明 \"Our contribution is not the metric itself but the controlled experimental framework that isolates confusability's predictive relationship with extraction degradation\"。R2 在 W1 和 W6 中重复了同一个批评（novelty limited），但 SCS 不是 claimed as a novel metric。\n\n2. r²=1.3-1.7% 低不代表 metric 无价值——它代表**在所有 pair 上（包括大量零混淆 pair）**的 variance explained。Among non-zero confusion pairs, R²=7%（虽然有选择偏差）。而 batch-level R²=22-53% 是 actionable 的。\n\n3. 真正的问题不是 SCS 是否\"新\"，而是是否有 better alternatives 被忽略了。论文未尝试 ontological distance、type definition overlap、token-level overlap 等替代 metrics。这是一个遗漏但不影响论文现有结论的 validity。\n\n---\n\n### [AGREE] R2-W7: FewRel data contamination 风险\n\n同意，与我的 W5 一致。补充：论文的 defense（train-origin accuracy 更低）方向正确但 p=0.06 不够 conclusive。如果 contamination 是 relation-type-specific 而非 uniform，BCS-controlled 实验中 high-BCS/low-BCS batch 的 contaminated type 比例差异可能是一个未控制的 confound。\n\n---\n\n### [REBUT] R2-W8: Abstract 数字密度过高\n\n这是一个 style preference。我实际上认为数字密度高是这篇分析型论文的**优点**——审稿人可以从 abstract 直接判断效应大小和统计支撑。相比于那些 abstract 中充斥 vague claims（\"significantly outperforms...\"）而不给具体数字的论文，这种 precision 是 preferable 的。\n\n当然，可读性确实受影响。但这是一个写作 polish 问题，不影响 acceptance 决策。Severity 应为 info，不是 warning。\n\n---\n\n## 对 Questions 的意见\n\n**Q1 (2.2pp noise tolerance)**: 好问题。我在 W3 中也隐含了这一点。2.2pp 在 RE accuracy 上可能低于 practitioners 的 noise margin。论文应讨论。\n\n**Q2 (Multivariate model)**: 非常好的建议。如果把 entity frequency、prompt position、mention ambiguity 纳入 regression model，SCS 是否仍然 significant？这能更 convincingly 证明 SCS 的 unique contribution。但我不确定这是否 feasible——prompt position 是 random（论文用 alphabetical order），mention ambiguity 难以操作化。\n\n**Q3 (Oracle routing 指导价值)**: 论文已清楚说明 oracle routing 是 ceiling analysis，不是可部署方案。这个问题的答案在 §6 已经给出了——价值在于证明 \"performance gap exists and is recoverable in principle\"。我认为这不需要额外回答。\n\n**Q4 (NER power analysis)**: 与我的 Q in W1 一致。需要作者回答。\n\n**Q5 (不同 embedding)**: 与我的 W4 一致。需要作者回答。\n\n---\n\n## 对 Missing References 的意见\n\n**M1 \"From Haystack to Needle\" (2025)**: 如果这是关于 label space reduction in zero-shot classification，确实相关——属于 count reduction 策略。应引用。[AGREE]\n\n**M2 \"Many-Shot In-Context Learning\" (NeurIPS 2024)**: [REBUT] 这篇是关于 scaling in-context examples 数量，而非 schema type 数量。两者方向不同——增加 ICL examples 是增加 training signal，而增加 schema types 是增加 discrimination difficulty。关联性较弱。\n\n**M3 Label confusion in 传统 ML**: [AGREE] 论文确实缺少对 class similarity / label confusion 经典文献的引用。例如 hierarchical classification 中 sibling class confusion 的研究（Cesa-Bianchi et al., 2006; Deng et al., 2010 ImageNet hierarchy）可以提供 theoretical grounding。\n\n**M4 SGD/SGD-X 讨论深度**: [REBUT] 论文 §2 已引用 SGD/SGD-X，且 Appendix §Cross-Domain Connections 专门讨论了这一联系。R2 未指明具体缺少什么内容。\n\n---\n\n## Overall Assessment 对比\n\nR2 给 borderline reject (2.5/5)，我给 3/5 (Findings acceptance)。\n\n**差异的原因**：R2 更重视 novelty/excitement，认为 \"confirming an intuition with controlled design\" 不够新。我更重视 methodological rigor 和 honest reporting，认为 controlled framework + negative findings + centrality confound analysis 对该领域有 lasting reference value。\n\n**共识点**：(a) typical effect 太小（2.2pp）; (b) separability claim overclaimed; (c) framing 有偏差。\n\n**我的建议不变**：Findings-level accept，条件是修改 overclaims（separability 限定为 RE、abstract 数字重排序、+1.4pp 明确标为 n.s.）。\n",
  "reviewer_id": "1",
  "project": "schema-dag-extraction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "\n# Reviewer 1 对 Reviewer 2 意见的逐条回应\n\n## 对 Strengths 的意见\n\nR2 的 S1-S6 与我的评估高度一致，无异议。特别是 S2（负面结果诚实报告）和 S3（统计方法全面）是本文的显著优势。\n\n---\n\n## 对 Weaknesses 的逐条回应\n\n### [REBUT] R2-W1: \"Two-channel decomposition 近似 trivial\"\n\nR2 的批评有道理但过于严厉。几点反驳：\n\n1. **\"直觉上显然\"≠\"实验上已证\"。** \"更多类型→recall 下降\"确实被 Li et al. (2023) 观察过，但他们未控制 confusability；LLM-PEE (2025) 用 similarity 做分组但未做 controlled isolation。本文的贡献在于**方法论层面**——提出第一个能将 count 和 confusability 效应正交分离的实验范式。这类似于医学中 RCT 相对于观察性研究的价值。\n\n2. **但我承认 novelty 确实有限。** controlled confirmation 的价值取决于结果是否 surprising。如果结果完美符合预期（两通道可分离、confusability 有强效应），那 confirmation 的增量信息很少。而本文的结果实际上有 nuance：(a) NER 上两通道 NOT cleanly separable；(b) 实际效应仅 2.2pp；(c) SDGD 失败。这些 nuances 是 non-trivial findings，不是简单 confirmation。\n\n3. **SCS 作为 metric 的 novelty**：R2 正确指出 SCS 与 LLM-PEE 形式相同（§2 原文承认）。但 SCS 在本文中不是 contribution 本身，而是实验工具。类似于用 t-test 做对照实验——t-test 不新但实验是新的。\n\n**结论**：R2 的 novelty concern 有效，但程度上我认为是 borderline 而非 deal-breaker。Controlled methodology + negative findings (SDGD) + centrality confound 识别 = 足够的 intellectual contribution for Findings-level publication。不够 exciting for main conference。\n\n---\n\n### [AGREE] R2-W2: Framing 过度强调 extreme-batch 结果\n\n完全同意。我在自己的 W6 中提出了同一问题。Abstract 和 Introduction 的 presentation order 使读者首先接触到大数字（31.2pp），而实践中典型效应仅 2.2pp。论文 §5.3 的 honest qualification 来得太晚——多数读者（包括 AC/meta-reviewer）可能只仔细读 abstract+intro。\n\n补充一点 R2 未提到的：Introduction 的 opening paragraph 报告了 count curve 的 overall degradation（\"recall drops from 0.72 to 0.42\"）——这些是 Channel 1 (count) 的数字，不是 Channel 2 (confusability) 的。但论文标题问的是 \"Does Type Confusability Shape...\"——如果 confusability 的 typical effect 只有 2.2pp 而 count 的 effect 是 35+pp，那 confusability 作为 degradation 的\"shaping\"因素其重要性需要被 contextualized。\n\n---\n\n### [REBUT] R2-W3: 非显著结果被不恰当 frame 为正面 contribution\n\nR2 的批评方向正确但解读有偏差。让我重新看 Contribution #4 原文（§1）：\n\n> \"Schema decomposition proves structurally infeasible for NER (merge amplification collapses precision from 0.56 to 0.21) **and yields no statistically significant improvement for RE** (graph-coloring: +1.4pp, p≈0.19). Oracle routing (+29.8pp) confirms the performance ceiling exists but highlights the gap between theoretical and achievable gains.\"\n\n这里 +1.4pp (p≈0.19) 是被引用为**负面证据**——\"no statistically significant improvement\"。Contribution #4 的实质是**诊断性发现**：(a) NER 失败因 merge amplification；(b) RE 的 confusability-aware grouping 无显著增益；(c) 但 oracle routing 证明 ceiling 存在。整个 contribution 是一个 negative/diagnostic finding，不是在 claim +1.4pp 是正面成果。\n\n**但我部分同意**：Abstract 中的 \"RE batch composition yields a directional +1.4pp gain\" 措辞确实可被误读为正面 claim。\"directional\" 这个词暗示了方向性收益。建议改为 \"confusability-aware grouping yields no significant improvement (+1.4pp, p≈0.19, n.s.)\"。\n\n此外，R2 指出 graph coloring \"排第 13/15 个 random seeds\"——这确实是一个 damning detail，论文应在正文而非仅在 Table caption 中讨论。如果 confusability-aware 方案比大多数 random 方案差，那 SCS 指导的分组在这个粒度下甚至是 counterproductive 的。\n\n---\n\n### [AGREE] R2-W4: \"Empirically separable\" 证据不均衡\n\n完全同意，与我的 W1 (critical) 一致。补充：\n\nR2 列出三项检验中两项失败。但论文的 defense 是 Few-NERD factorial \"underpowered\"（Appendix）。问题是：**如果你承认检验力不足，就不能将 n.s. 结果同时用来 claim separability（在 abstract/contributions 中）和 dismiss 为 underpowered（在 appendix 中）。**\n\n论文 §5.4 自己写道 \"cleanly separable in RE but coupled in NER\"——这是准确的。但 abstract 的 \"two empirically separable degradation channels\" 没有这个 qualifier。这是一个 overclaim。\n\n---\n\n### [AGREE] R2-W5: Cross-model claim 省略 NER Channel 2 失败\n\n同意。Conclusion 的 \"replicate across model families\" 后面列举的证据 \"(Llama-3.1-8B: count r = 0.725, confusability Δ = −27pp)\" 确实只包含 RE 数据。Limitations item 1 承认 \"Channel 2 was not robustly detectable on NER at 8B scale\"，但这个 caveat 在 conclusion 中消失了。\n\n不过，这个问题的 severity 我认为是 warning 而非 critical——因为 Limitations 确实讨论了，只是 conclusion 的 wording 不够精确。\n\n---\n\n### [REBUT] R2-W6: SCS 作为 metric 的增量贡献存疑\n\nR2 的批评逻辑是：SCS = cosine similarity（与 LLM-PEE 相同），且 r² 很低，所以 SCS 无贡献。\n\n反驳：\n1. 论文 §2 已明确声明 \"Our contribution is not the metric itself but the controlled experimental framework that isolates confusability's predictive relationship with extraction degradation\"。R2 在 W1 和 W6 中重复了同一个批评（novelty limited），但 SCS 不是 claimed as a novel metric。\n\n2. r²=1.3-1.7% 低不代表 metric 无价值——它代表**在所有 pair 上（包括大量零混淆 pair）**的 variance explained。Among non-zero confusion pairs, R²=7%（虽然有选择偏差）。而 batch-level R²=22-53% 是 actionable 的。\n\n3. 真正的问题不是 SCS 是否\"新\"，而是是否有 better alternatives 被忽略了。论文未尝试 ontological distance、type definition overlap、token-level overlap 等替代 metrics。这是一个遗漏但不影响论文现有结论的 validity。\n\n---\n\n### [AGREE] R2-W7: FewRel data contamination 风险\n\n同意，与我的 W5 一致。补充：论文的 defense（train-origin accuracy 更低）方向正确但 p=0.06 不够 conclusive。如果 contamination 是 relation-type-specific 而非 uniform，BCS-controlled 实验中 high-BCS/low-BCS batch 的 contaminated type 比例差异可能是一个未控制的 confound。\n\n---\n\n### [REBUT] R2-W8: Abstract 数字密度过高\n\n这是一个 style preference。我实际上认为数字密度高是这篇分析型论文的**优点**——审稿人可以从 abstract 直接判断效应大小和统计支撑。相比于那些 abstract 中充斥 vague claims（\"significantly outperforms...\"）而不给具体数字的论文，这种 precision 是 preferable 的。\n\n当然，可读性确实受影响。但这是一个写作 polish 问题，不影响 acceptance 决策。Severity 应为 info，不是 warning。\n\n---\n\n## 对 Questions 的意见\n\n**Q1 (2.2pp noise tolerance)**: 好问题。我在 W3 中也隐含了这一点。2.2pp 在 RE accuracy 上可能低于 practitioners 的 noise margin。论文应讨论。\n\n**Q2 (Multivariate model)**: 非常好的建议。如果把 entity frequency、prompt position、mention ambiguity 纳入 regression model，SCS 是否仍然 significant？这能更 convincingly 证明 SCS 的 unique contribution。但我不确定这是否 feasible——prompt position 是 random（论文用 alphabetical order），mention ambiguity 难以操作化。\n\n**Q3 (Oracle routing 指导价值)**: 论文已清楚说明 oracle routing 是 ceiling analysis，不是可部署方案。这个问题的答案在 §6 已经给出了——价值在于证明 \"performance gap exists and is recoverable in principle\"。我认为这不需要额外回答。\n\n**Q4 (NER power analysis)**: 与我的 Q in W1 一致。需要作者回答。\n\n**Q5 (不同 embedding)**: 与我的 W4 一致。需要作者回答。\n\n---\n\n## 对 Missing References 的意见\n\n**M1 \"From Haystack to Needle\" (2025)**: 如果这是关于 label space reduction in zero-shot classification，确实相关——属于 count reduction 策略。应引用。[AGREE]\n\n**M2 \"Many-Shot In-Context Learning\" (NeurIPS 2024)**: [REBUT] 这篇是关于 scaling in-context examples 数量，而非 schema type 数量。两者方向不同——增加 ICL examples 是增加 training signal，而增加 schema types 是增加 discrimination difficulty。关联性较弱。\n\n**M3 Label confusion in 传统 ML**: [AGREE] 论文确实缺少对 class similarity / label confusion 经典文献的引用。例如 hierarchical classification 中 sibling class confusion 的研究（Cesa-Bianchi et al., 2006; Deng et al., 2010 ImageNet hierarchy）可以提供 theoretical grounding。\n\n**M4 SGD/SGD-X 讨论深度**: [REBUT] 论文 §2 已引用 SGD/SGD-X，且 Appendix §Cross-Domain Connections 专门讨论了这一联系。R2 未指明具体缺少什么内容。\n\n---\n\n## Overall Assessment 对比\n\nR2 给 borderline reject (2.5/5)，我给 3/5 (Findings acceptance)。\n\n**差异的原因**：R2 更重视 novelty/excitement，认为 \"confirming an intuition with controlled design\" 不够新。我更重视 methodological rigor 和 honest reporting，认为 controlled framework + negative findings + centrality confound analysis 对该领域有 lasting reference value。\n\n**共识点**：(a) typical effect 太小（2.2pp）; (b) separability claim overclaimed; (c) framing 有偏差。\n\n**我的建议不变**：Findings-level accept，条件是修改 overclaims（separability 限定为 RE、abstract 数字重排序、+1.4pp 明确标为 n.s.）。\n",
    "reviewer_id": "1",
    "project": "schema-dag-extraction"
  }
}
```

</details>

---


### Tool result

_source line 381 · 2026-05-16T15:17:29.436279+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3866
}
```

</details>

---


### Assistant

_source line 382 · 2026-05-16T15:17:37.191178+00:00_

已提交对 Reviewer 2 意见的逐条回应。

核心立场：与 R2 在 framing 偏差（W2）、separability overclaim（W4）、contamination（W7）上达成共识；在 novelty（W1 部分反驳——controlled methodology 有方法论贡献）、非显著结果 framing（W3 部分反驳——实际是作为负面证据引用）、SCS 贡献（W6 反驳——metric 不是 claimed novelty）、abstract 数字密度（W8 反驳——分析型论文的精确性是优点）上有分歧。

最终评分维持 3/5（Findings acceptance），与 R2 的 2.5/5 差异主要源于对 methodological contribution 价值的权重不同。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1"
}
```

</details>

---


## Round 15

## Round 15

32 recorded events


### User

_source line 383 · 2026-05-16T16:34:50.872245+00:00_

[Round 1 审稿请求]:
你是 Reviewer 1，负责**方法论严谨性 + 统计推断 + 实验设计**。

## Venue 信息
- **目标**: EMNLP 2026 Main Conference (via ACL Rolling Review May 2026 cycle)
- **截止日期**: 2026-05-25
- **格式**: ACL 2-column template, 8 页正文 + 无限参考文献/附录, double-blind
- **匿名规则**: 严格 double-blind

## 论文路径
`projects/schema-dag-extraction/docs/paper/main.tex`（含 \input 的子文件）

## 审查侧重

请从以下角度严格评审：

1. **统计推断的有效性**：
   - 效应量（pairwise r²=1.3–1.7%）是否足以支撑核心 claims？
   - TOST 等价性检验的 margin 选择是否合理？
   - Bootstrap CI 的使用是否正确？样本量是否充足？
   - Conditioning on non-zero pairs (7% vs 1.3%) 是否引入选择偏差？

2. **实验设计的内部效度**：
   - Count curves 每 level 5 batches 是否足够稳定？
   - BCS-controlled 实验是否完全控制了混淆变量（type frequency, prompt position, etc.）？
   - Factorial design 两项中两项不显著（NER p=0.50, FewRel 2×2 p_TOST=0.56），唯一通过的是 full regression — 是否 cherry-picking？
   - 跨数据集使用不同 embedding（Qwen3 vs MiniLM）对可比性的影响

3. **可复现性**：
   - 种子策略、采样方法、超参数是否充分报告？
   - Single-seed evaluation 的局限性

4. **格式合规**：
   - 页数是否符合 8 页限制？
   - 匿名性是否被破坏？

请按 Strengths / Weaknesses (Must-Fix / Should-Fix / Minor) / Questions / Missing References 结构输出审稿意见。Weaknesses 请按严重程度排序，每条给出具体 evidence 和建议修改方案。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 384 · 2026-05-16T16:35:04.252916+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebSearch,mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebSearch,mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director",
    "max_results": "3"
  }
}
```

</details>

---


### Tool result

_source line 385 · 2026-05-16T16:35:04.303557+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 386 · 2026-05-16T16:35:07.167179+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review 2026 reviewer guidelines review form criteria"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review 2026 reviewer guidelines review form criteria"
  }
}
```

</details>

---


### Tool call

_source line 387 · 2026-05-16T16:35:08.574049+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 388 · 2026-05-16T16:35:08.877938+00:00_

1	\documentclass[11pt]{article}
2	
3	\usepackage[review]{acl}
4	
5	\usepackage{times}
6	\usepackage{latexsym}
7	\usepackage[T1]{fontenc}
8	\usepackage[utf8]{inputenc}
9	\usepackage{microtype}
10	\usepackage{graphicx}
11	\usepackage{booktabs}
12	\usepackage{amsmath}
13	\usepackage{enumitem}
14	\usepackage[normalem]{ulem}
15	\usepackage{listings}
16	
17	\title{Does Type Confusability Shape Schema-Induced Degradation\\in Training-Free LLM Information Extraction?}
18	
19	\author{Anonymous}
20	
21	\begin{document}
22	\maketitle
23	
24	\input{abstract}
25	
26	\input{introduction}
27	
28	\input{related_work}
29	
30	\input{experimental_setup}
31	
32	\input{results}
33	
34	\input{sdgd_negative}
35	
36	\input{discussion}
37	
38	\section*{Limitations}
39	\begin{enumerate}[leftmargin=*,itemsep=2pt]
40	\item \textbf{Model coverage.} Primary experiments use Qwen3-32B with cross-model validation on Llama-3.1-8B-Instruct. Whether patterns hold for proprietary models (GPT-4, Gemini) remains unverified. Channel~2 was not robustly detectable on NER at 8B scale, likely due to floor effects.
41	
42	\item \textbf{Modest pairwise effect size.} Pairwise SCS explains 1.3--1.7\% of type confusion variance; entity frequency, prompt position, mention ambiguity, and type definition quality likely account for the remainder.
43	
44	\item \textbf{Factorial interaction tests.} Within-dataset count $\times$ BCS interaction on Few-NERD did not reach significance ($p = 0.50$; Appendix~\ref{sec:appendix_factorial}). However, a FewRel factorial with TOST equivalence testing confirms additive separability ($p_{\text{TOST}} = 0.003$, interaction = 0.47\,pp; Appendix~\ref{sec:appendix_factorial}), and cross-pool slope consistency ($p = 0.60$) corroborates stable rather than amplifying sensitivity.
45	
46	\item \textbf{Decomposition and metric scope.} RE batch composition is tested on FewRel only; NER merge alternatives remain unexplored. SCS relies on embedding cosine similarity; label entropy or ontologic
…[truncated 26937 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 303
}
```

</details>

---


### Tool result

_source line 389 · 2026-05-16T16:35:15.957990+00:00_

Web search results for query: "ACL Rolling Review 2026 reviewer guidelines review form criteria"

Links: [{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"ACL Rolling Review | ACL Member Portal","url":"https://www.aclweb.org/portal/content/acl-rolling-review"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"}]

Based on the search results, here's information about the ACL Rolling Review 2026 reviewer guidelines, review form, and criteria:

## Reviewer Guidelines

Reviewers are asked to read the paper and get a first impression, then search for related work without deliberately trying 
…[truncated 1908 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 8790
}
```

</details>

---


### Tool call

_source line 390 · 2026-05-16T16:35:22.300206+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review review form scoring criteria soundness excitement novelty 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review review form scoring criteria soundness excitement novelty 2025 2026"
  }
}
```

</details>

---


### Tool call

_source line 391 · 2026-05-16T16:35:24.057433+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 392 · 2026-05-16T16:35:24.158286+00:00_

1	\begin{abstract}
2	Training-free LLM information extraction degrades as schema complexity grows. We present the first controlled study isolating type confusability from type count in zero-shot LLM IE, spanning NER, RE, and event detection across four datasets. We introduce the Schema Confusability Score (SCS) and two experimental paradigms: count curves (varying schema size while randomizing confusability) and BCS-controlled experiments (fixing size while varying confusability).
3	
4	We identify two degradation channels: count-driven recall decline and confusability-driven type substitution. In typical random batches, confusability accounts for ${\approx}\,2.2$\,pp accuracy difference; under quartile contrast the gap reaches $-5.3$\,pp, and batch-level BCS explains up to 53\% of cross-batch variance. The channels are cleanly separable in RE (TOST equivalence test, $p = 0.003$) but coupled in NER where boundary and type ambiguity interact. Effects are directionally consistent across prompt designs and model scales, though Channel~2 attenuates on smaller models. Schema decomposition via oracle routing recovers +29.8\,pp for RE, but confusability-aware grouping yields no significant improvement over random grouping (+1.4\,pp, $p \approx 0.19$, n.s.).
5	\end{abstract}
6	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 393 · 2026-05-16T16:35:24.309182+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 394 · 2026-05-16T16:35:24.360078+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	Training-free\footnote{We use ``training-free'' and ``zero-shot'' interchangeably to denote prompting without parameter updates.} LLM information extraction---prompting a large language model with a target schema and asking it to extract structured information without any task-specific fine-tuning---enables rapid deployment across new domains and ontologies. This zero-shot paradigm eliminates the need for labeled data, making it attractive for applications where annotation is expensive or schemas evolve frequently \cite{llm4ie-survey-2024}. Yet the paradigm carries a critical limitation: performance degrades sharply as the number of candidate types in the prompt schema grows. On named entity recognition, recall drops from 0.72 with a single candidate type to 0.42 with 64 types, a 42\% relative decline. On relation extraction, accuracy falls from 85.7\% with one relation to 50.4\% with 80 relations (sentence-level) and from 88.0\% to 38.7\% with 96 relations (document-level)---near or exceeding halving. This degradation is not academic: real-world ontologies routinely define 50--200+ types, placing them squarely in the regime where training-free extraction becomes unreliable.
5	
6	What explains this degradation? Prior decomposition strategies \cite{uniner-2024,llm-pee-2025,parse-2025} conflate two mechanisms: having more types to discriminate among (count) and having semantically similar types to confuse (confusability) (hereafter Channel~1 and Channel~2). None isolates which factor predicts the gains (\S\ref{sec:related_work}).
7	
8	We ask three questions. \textbf{RQ1}: Does type confusability independently predict extraction degradation beyond the effect of type count? \textbf{RQ2}: Through what mechanisms do count and confusability each degrade performance? \textbf{RQ3}: Can confusability-aware schema decomposition improve extraction quality?
9	
10	We present the first controlled study isolating type confusa
…[truncated 2686 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 395 · 2026-05-16T16:35:30.236670+00:00_

Web search results for query: "ACL Rolling Review review form scoring criteria soundness excitement novelty 2025 2026"

Links: [{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"aclrollingreview/reviewerguidelines.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/reviewerguidelines.md"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"ARR Changelog – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/changelog"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"ACL 2023 Acceptance Recommendations - ACL 2023","url":"https://2023.aclweb.org/blog/overall-recommendation/"}]

Based on the search results, here's information about the ACL Rolling Review (ARR) review form scoring criteria for 2025-2026:

## Three-Part Scoring System

Starting with February 2025, ARR reviewers are asked to provide 
…[truncated 1518 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 7936
}
```

</details>

---


### Tool call

_source line 396 · 2026-05-16T16:35:33.706327+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/experimental_setup.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/experimental_setup.tex"
  }
}
```

</details>

---


### Tool result

_source line 397 · 2026-05-16T16:35:33.857443+00:00_

1	\section{Experimental Setup}
2	\label{sec:experimental_setup}
3	
4	We evaluate how prompt schema size and inter-type confusability affect zero-shot LLM extraction across three information extraction tasks and four datasets: named entity recognition (NER), sentence-level relation extraction (RE), document-level RE, and event detection (ED).
5	
6	\subsection{Tasks and Datasets}
7	\label{sec:datasets}
8	
9	\paragraph{Few-NERD (NER).}
10	Few-NERD \cite{fewnerd-2021} provides 66 fine-grained entity types organized into 8 coarse categories (person, location, organization, building, art, product, event, other). The dataset spans diverse domains, making it suitable for cross-domain evaluation. We sample 1{,}000 test instances uniformly across test instances; type frequency follows the natural long-tail distribution of Few-NERD. Evaluation uses token-level text matching. Pairwise analysis covers 1{,}953 type pairs with non-zero co-occurrence out of $\binom{66}{2}=2{,}145$ possible pairs.
11	
12	\paragraph{FewRel (RE).}
13	FewRel \cite{fewrel-2018} contains 80 relation types sourced from Wikidata. Since the validation split covers only 16 relations, we combine the training and validation splits to obtain the full 80-relation pool required for schema-scale experiments, and sample 1{,}000 balanced instances (12--13 per relation type, stratified to ensure equal representation). Each instance provides a sentence with marked head and tail entities; the task is to classify the relation.
14	
15	\paragraph{DocRED (Document-level RE).}
16	DocRED \cite{docred-2019} contains 96 relation types sourced from Wikidata, evaluated at the document level where entity pairs may span multiple sentences. We sample 1{,}000 instances balanced across 96 relation types ($\sim$10 per type) from the DocRED development set and formulate the task identically to FewRel: given a document with marked head and tail entities, classify the relation. DocRED extends the RE evaluation to a larger schema (96 vs.\
…[truncated 7281 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 398 · 2026-05-16T16:35:33.857937+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex"
  }
}
```

</details>

---


### Tool result

_source line 399 · 2026-05-16T16:35:33.908573+00:00_

1	\section{Results}
2	\label{sec:results}
3	
4	Unless otherwise noted, all experiments in this section use the v1 prompt (\S\ref{sec:model}; full templates in Appendix~\ref{sec:appendix_prompts}).
5	
6	\subsection{Count-Degradation Curves}
7	\label{sec:count_curves}
8	
9	\begin{figure}[t]
10	\centering
11	\begin{minipage}[t]{0.48\columnwidth}
12	\centering
13	\includegraphics[width=\linewidth]{../../figures/paper/fig_count_curves.pdf}
14	\end{minipage}
15	\hfill
16	\begin{minipage}[t]{0.48\columnwidth}
17	\centering
18	\includegraphics[width=\linewidth]{../../figures/paper/fig_bcs_scaling.pdf}
19	\end{minipage}
20	\caption{\textbf{(a)} Count-degradation curves across three tasks. Error bars show $\pm 1$\,SD across 5 random type batches per count level (omitted at count${}\,=\,1$ where each type is evaluated individually). NER recall and RE accuracy decline monotonically with schema size; MAVEN relaxed F1 increases (\S\ref{sec:centrality_confound}). \textbf{(b)} BCS-controlled FewRel accuracy. The BCS--accuracy slope is consistent across the independent 16-relation pool and within-pool 16-relation subsets (permutation $p = 0.60$); the wider BCS range available at 80 relations produces larger absolute gaps.}
21	\label{fig:main_results}
22	\end{figure}
23	
24	Figure~\ref{fig:main_results}a shows extraction quality degrades monotonically with schema size across three datasets: Few-NERD recall drops from 0.72 to 0.42 ($-$42\%), FewRel accuracy from 85.7\% to 50.4\% ($-$35.3\,pp), and DocRED from 88.0\% to 38.7\% ($-$56\%). MAVEN exhibits a reversed trend attributable to centrality confounding (\S\ref{sec:centrality_confound}). The effect replicates on Llama-3.1-8B-Instruct ($-$43\,pp on Few-NERD; per-batch $r = 0.725$; Table~\ref{tab:cross_model}), indicating schema configuration rather than model-specific factors predicts difficulty.
25	
26	\subsection{Pairwise Confusability and Type Confusion}
27	\label{sec:pairwise}
28	
29	We test whether pairwise SCS predicts type-le
…[truncated 8919 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 400 · 2026-05-16T16:35:38.027094+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/sdgd_negative.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/sdgd_negative.tex"
  }
}
```

</details>

---


### Tool result

_source line 401 · 2026-05-16T16:35:38.479689+00:00_

1	\section{Schema Decomposition: Failure, Diagnosis, and Mitigation}
2	\label{sec:sdgd}
3	
4	A natural intervention against confusability-driven degradation is to partition the schema so that confusable types never co-occur in the same prompt. We test this idea with \textbf{Schema-DAG-Guided Decomposition} (SDGD\footnote{SDGD (Schema Decomposition and Grouping for Degradation mitigation) is an adopted abbreviation for schema decomposition and grouping; the graph structure is undirected.}), which uses greedy graph coloring on the pairwise SCS graph to assign types to low-confusability batches.
5	
6	We construct a thresholded confusability graph $G = (V, E)$ where each type is a vertex and an edge connects types $t_i, t_j$ whenever $\text{SCS}(t_i, t_j) > \tau$. Greedy graph coloring (\textsc{largest\_first}) assigns each type to a color such that no two adjacent---i.e., highly confusable---types share a batch. Each color class forms one extraction batch. For NER, predictions from all batches are merged via set union; for RE, each instance is routed to the batch containing its gold type (oracle routing). We test four NER modes: (i)~\textbf{single\_pass}, the undecomposed baseline; (ii)~\textbf{sdgd\_zero}, SCS-guided partitioning; (iii)~\textbf{random\_batch}, random partitioning with matched batch sizes; and (iv)~\textbf{per\_type}, each type extracted in isolation. Every mode falls below the single-pass NER baseline: SDGD obtains F1\,=\,0.251, random batching 0.320, per-type 0.292, versus 0.445 for single-pass (Table~\ref{tab:sdgd_results}, Appendix~\ref{sec:appendix_sdgd}).
7	
8	\paragraph{Merge amplification in NER.}
9	The core failure mechanism is \emph{merge amplification}: presenting the same text to the model $k$ times with different type subsets causes each pass to independently generate entity predictions, and union merge accumulates all of them into a single output. Each pass produces an independent set of span predictions; because LLM outputs are not calib
…[truncated 4344 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 402 · 2026-05-16T16:35:38.580871+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 403 · 2026-05-16T16:35:38.583407+00:00_

1	\section{Discussion}
2	\label{sec:discussion}
3	
4	\paragraph{Boundary conditions.}
5	The two-channel decomposition applies to cross-domain schemas; same-domain schemas (e.g., MAVEN's FrameNet-derived event types) exhibit centrality confounding that obscures per-type aggregated signals, requiring pairwise SCS or centrality adjustment (\S\ref{sec:centrality_confound}). High-BCS accuracy converges to $\approx$51\% across tested models, suggesting a task-inherent difficulty ceiling. RE's clean channel separation may partly reflect its closed-set format; the effect generalizes to document-level RE (DocRED slope $-$0.71). Prompt design modulates but does not eliminate the effect (v2 gap: $-$25.5\,pp vs.\ v1 extreme-batch gap; Appendix~\ref{sec:appendix_prompt_sensitivity}). Preliminary cross-scale evidence (32B vs.\ 8B) shows Channel~2 attenuates on smaller models due to floor effects, while Channel~1 replicates fully (Tables~\ref{tab:cross_model}--\ref{tab:cross_model_bcs}).
6	
7	\paragraph{Prompt length as mechanism.}
8	Count-driven degradation (Channel~1) may partly reflect prompt length increase: adding types mechanically lengthens the prompt, and per-type recall (0.586) substantially exceeds single-pass recall (0.368), consistent with lost-in-middle effects \cite{lost-in-middle-2024}. Disentangling count from prompt length would require fixed-count variable-length experiments, which we leave to future work.
9	
10	\paragraph{Why does embedding similarity predict LLM confusion?}
11	Type name embeddings capture semantic proximity in the same representational space LLMs use for in-context type resolution; high SCS indexes representational overlap that causes substitution errors during decoding. The pair-level effect is modest (conditional $R^2 \approx 7\%$ among non-zero confusion pairs; unconditional $r^2 = 1.3$--$1.7\%$) but amplifies ${\sim}3\times$ at the batch level through inter-pair correlation (Appendix~\ref{app:aggregation-sim}), yielding batch-level $R^2$ of
…[truncated 1454 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 2
}
```

</details>

---


### Tool call

_source line 404 · 2026-05-16T16:35:48.925616+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 405 · 2026-05-16T16:35:49.077385+00:00_

1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{Training-free LLM IE.}
5	Training-free LLM IE spans instruction tuning \cite{instructuie-2023}, code-style schema encoding \cite{knowcoder-2024,codeie-2023}, annotation-guided extraction \cite{gollie-2024,adelie-2024}, schema-driven decoding \cite{slot-2025,oneke-2025}, and constrained JSON decoding \cite{json-schema-bench-2025}. For NER, methods include zero-shot decomposition \cite{xie-zeroshot-ner-2023,promptner-2023}, distillation \cite{uniner-2024}, and bidirectional encoders \cite{gliner-2024,gliner2-2025}. For RE, recent work examines zero-shot relation triplet extraction via prompting \cite{relationprompt-2022} and revisits relation extraction in the LLM era \cite{wadhwa-re-llm-2023}. These methods perform well with moderate schemas (4--20 types) but none investigates how performance degrades as schema complexity scales, nor proposes quantitative metrics for inter-type confusability.
6	
7	\paragraph{Schema complexity in IE.}
8	The most directly related work is LLM-PEE \cite{llm-pee-2025}, which partitions large event schemas by type embedding similarity. Our work differs in three ways: (1)~we conduct controlled analysis to understand \emph{why} extraction degrades rather than developing an engineering solution; (2)~our BCS-controlled experiments isolate count from confusability, which LLM-PEE conflates; (3)~our SDGD experiments reveal that merge amplification---not partitioning quality---is the bottleneck in decompose-then-merge pipelines. Other approaches address schema complexity via hard negative mining \cite{iepile-2024}, schema definition optimization \cite{parse-2025}, multi-agent debate \cite{crossagentie-2025,cmas-ner-2025}, schema-aware decomposition for event extraction \cite{dee-2024}, and active prompting \cite{reflect-learn-2026}; all treat it as an engineering problem rather than isolating the underlying degradation mechanisms. Concurrently, \citet{haystack-to-needle-2025} redu
…[truncated 1932 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 406 · 2026-05-16T16:35:49.077743+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebFetch",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebFetch",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 407 · 2026-05-16T16:35:49.130033+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 52
}
```

</details>

---


### Tool call

_source line 408 · 2026-05-16T16:35:53.951025+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete review form with all scoring dimensions, their scale (1-5), and descriptions of each score level. Include soundness, excitement, overall recommendation, and any other scored dimensions."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the complete review form with all scoring dimensions, their scale (1-5), and descriptions of each score level. Include soundness, excitement, overall recommendation, and any other scored dimensions."
  }
}
```

</details>

---


### Tool call

_source line 409 · 2026-05-16T16:35:54.102035+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/checklist.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/checklist.tex"
  }
}
```

</details>

---


### Tool result

_source line 410 · 2026-05-16T16:35:54.152823+00:00_

1	\section*{Responsible NLP Research Checklist}
2	
3	For each question, the answer is \textbf{Yes}, \textbf{No}, or \textbf{N/A}. If Yes, the relevant section is indicated. If No, a justification is provided.
4	
5	\subsection*{A \quad For Every Submission}
6	
7	\begin{enumerate}[label=\textbf{A\arabic*.},leftmargin=*,itemsep=4pt]
8	
9	\item \textbf{Did you describe the limitations of your work?}
10	
11	Yes. The Limitations section (after \S\ref{sec:conclusion}) discusses single-model reliance, modest pairwise effect sizes, cross-pool slope consistency, factorial interaction tests with TOST equivalence, decomposition scope, and metric scope.
12	
13	\item \textbf{Did you discuss any potential risks of your work?}
14	
15	N/A. This is a purely analytical study of schema-induced degradation in existing LLM IE systems. It does not introduce new models, datasets, or deployment-facing artifacts. The findings characterize failure modes and are intended to inform safer schema design.
16	
17	\item \textbf{Do the abstract and introduction summarize the paper's main claims?}
18	
19	Yes. The abstract and \S\ref{sec:introduction} state the two-channel degradation pattern (count and confusability), the cross-model consistency check, and the negative SDGD result.
20	
21	\item \textbf{Did you use AI assistants (e.g., ChatGPT, Copilot) when working on this paper?}
22	
23	Yes. An AI coding assistant was used for experiment scripting and LaTeX formatting. All scientific claims, experimental design, and analysis were conducted by the authors.
24	
25	\end{enumerate}
26	
27	\subsection*{B \quad Scientific Artifacts}
28	
29	\begin{enumerate}[label=\textbf{B\arabic*.},leftmargin=*,itemsep=4pt]
30	
31	\item \textbf{Did you cite the creators of artifacts you used?}
32	
33	Yes. Few-NERD \cite{fewnerd-2021}, FewRel \cite{fewrel-2018}, DocRED \cite{docred-2019}, MAVEN \cite{maven-2020}, Qwen3-32B \cite{qwen3-2025}, Meta-Llama-3.1-8B-Instruct \cite{llama3-2024}, vLLM \cite{vllm-2023}, and all-Mini
…[truncated 4435 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 411 · 2026-05-16T16:35:58.938650+00:00_

# ACL Rolling Review Form – Scoring Dimensions

## 1. **Reviewer Confidence** (1-5 scale)
- **5**: "Positive that my evaluation is correct"
- **4**: "Quite sure" with unlikely but possible oversights
- **3**: "Pretty sure" but may have missed details
- **2**: "Willing to defend" but likely missed some details
- **1**: "Not my area" or paper is very hard to understand

## 2. **Soundness** (1-5 scale with half-points)
- **5**: "Excellent: This study is one of the most thorough"
- **4**: "Strong: sufficient support for all claims"
- **3**: "Acceptable: sufficient support for main claims"
- **2**: "Poor: main claims not sufficiently supported"
- **1**: "Major Issues: not sufficiently thorough to warrant publication"

## 3. **Excitement** (1-5 scale with half-points)
- **5**: "Highly Exciting: I would recommend this paper to others"
- **4**: "Exciting: I would mention this paper to others"
- **3**: "Interesting: I might mention some points"
- **2**: "Potentially Interesting: does not resonate with me"
- **1**: "Not Exciting: does not resonate with me"

## 4. **Overall Assessment** (1-5 scale with half-points)
- **5**: "Consider for Award" (top 2.5%)
- **4**: "Conference acceptance"
- **3**: "Findings acceptance"
- **2**: "Resubmit next cycle"
- **1**: "Do not resubmit"

## 5. **Reproducibility** (1-5 scale)
- **5**: "Could easily reproduce the results"
- **4**: "Could mostly reproduce" with minor variations
- **3**: "Could reproduce with some difficulty"
- **2**: "Would be hard pressed to reproduce"
- **1**: "Would not be able to reproduce"

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 4987
}
```

</details>

---


### Tool call

_source line 412 · 2026-05-16T16:38:15.993812+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## 总体评分\n**Overall**: 3.5/5 (介于 Findings acceptance 和 Conference acceptance 之间)\n**一句话总结**: 一篇诚实且方法论透明的分析性论文，但核心效应量过小（pairwise r²=1.3-1.7%）、多项关键统计检验未通过（3/4 factorial tests 失败）、且唯一通过的检验依赖于测试选择，削弱了\"两通道可分离\"的核心 claim。\n\n## 官方维度打分（来自 ACL ARR review form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3/5 | 主要 claims 有证据支撑但力度不足：effect size 极小，factorial 显著性依赖测试方法选择，多处条件分析未过显著性门槛 |\n| Excitement | 3.5/5 | 问题设定有价值（isolate count vs confusability），方法论框架（SCS/BCS + controlled design）可复用，但负面结果（SDGD 失败）限制了实用影响力 |\n| Reproducibility | 3.5/5 | 报告了模型、种子、bootstrap 参数；但 single-seed evaluation、未量化跨种子方差、代码未公开是主要缺陷 |\n| Reviewer Confidence | 4/5 | 统计方法论和实验设计是我的专长领域 |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] Factorial separability claim 建立在选择性测试上\n\n- 具体位置：§4.4 (Multi-Channel Degradation) + Appendix §Factorial Analysis\n- 问题：论文声称 count 和 confusability \"cleanly separable in RE (TOST p=0.003)\"，但这一结论依赖于选择最有利的检验：\n  - Few-NERD 2×2 factorial: p=0.50（不显著）\n  - FewRel 2×2 factorial (n=54): p_TOST=0.56（不显著）\n  - FewRel full regression (n=69, 5 count levels): p_TOST=0.003（显著）\n\n  三项检验中只有一项通过。论文声称 \"regression approach provides the stronger test by leveraging the full count range\"——但这是 post-hoc 对测试选择的辩护。如果研究者在设计阶段就确定 full regression 是 primary test，应在方法部分预注册/声明；当前呈现方式是先展示失败的检验、再解释为何另一个更好，这是典型的 garden of forking paths 问题。\n- 为什么影响接收：additivity/separability 是论文五个核心发现之一（Finding 1: \"cleanly separable in RE\"），也是 abstract 和 conclusion 的关键措辞。如果 separability 只在特定测试下成立，结论需要大幅软化。\n- 建议修改方向：(1) 在 §3.3 明确预先指定 primary test（如果确实是 regression，需解释为什么）；(2) 将 abstract/conclusion 中的 \"cleanly separable\" 改为 \"consistent with additive separability under the full-range regression (TOST p=0.003), though lower-powered 2×2 designs did not reach equivalence\"；(3) 或执行 pre-registered replication 用独立数据验证。\n\n**N2** [critical] 典型效应量（2.2pp）是否足以支撑核心论点？\n\n- 具体位置：§4.3 Practical magnitude; Table 2 (pairwise r²=1.3-1.7%)\n- 问题：论文报告的 \"typical\" confusability gap 仅为 2.2pp（95% CI: [0.4, 4.0]），pairwise r²=1.3-1.7%。这意味着：\n  - 在自然随机 batching 条件下，confusability 对 accuracy 的实际贡献约 2pp\n  - 高达 98.3-98.7% 的 type confusion variance 由其他因素解释\n  - CI 下界为 0.4pp——接近于零实际意义\n\n  论文通过两种方式放大感知效应量：(a) 引用 extreme-batch gap (-31.2pp)；(b) conditioning on non-zero pairs 将 r² 从 1.3% 提升到 7%——但后者是 selection on dependent variable，论文虽承认 \"conditioning inflates this\" 但仍将 7% 作为 aggregation simulation 的输入。Abstract 中 \"batch-level BCS explains up to 53% of cross-batch variance\" 来自 DocRED 的极端条件，不代表一般性结论。\n- 为什么影响接收：如果 confusability 的 typical impact 仅为 2pp，其作为 \"degradation channel\" 的实用价值和理论意义均可质疑。Reviewer 需要判断这是否是一个 \"real but trivially small\" 的效应。\n- 建议修改方向：(1) Abstract 应前置 typical 效应量（2.2pp），而非先报告 extreme/conditional 数字；(2) 明确讨论 practical significance vs statistical significance 的区别；(3) 考虑是否应将论文重新定位为 \"confusability is detectable but not the primary driver\"，这仍然是有价值的发现但需要不同的 framing。\n\n**N3** [critical] Conditioning on non-zero pairs 引入选择偏差，且作为后续分析的基础\n\n- 具体位置：§4.3 Practical magnitude; Appendix §Pair-to-Batch Aggregation Simulation\n- 问题：\n  - 全部 type pairs 中只有约 30-40% 实际产生非零 confusion（Few-NERD: 1,953/2,145 有 non-zero co-occurrence，但多少有 non-zero confusion 未报告）\n  - 论文将 unconditional r²=1.3% 和 conditional r²=7%（non-zero pairs only）并列报告\n  - Appendix 的 Monte Carlo aggregation simulation 使用 conditional R²=0.074 作为输入参数，模拟得到 batch-level R²=0.219\n  - 但如果用 unconditional r²=0.013 作为输入，模拟结果会大幅缩水\n  \n  这构成了一个逻辑链问题：conditional estimate → simulation → \"explains\" batch-level R²，但 conditioning step 本身是有偏的。\n- 为什么影响接收：aggregation simulation 是论文解释 \"为什么 pairwise 效应小但 batch 效应大\" 的关键桥梁。如果这个桥梁的输入有偏，batch-level 的解释力就缺乏坚实基础。\n- 建议修改方向：(1) 用 unconditional r² 重新运行 simulation，报告两种输入下的结果；(2) 如果 unconditional 版本不能 reproduce batch-level R²，需要承认 conditioning 不仅 inflates 而且 distorts 解释；(3) 或提供 formal justification for why conditioning is the correct analytical frame。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] Single-seed evaluation 无法量化推断不确定性\n\n- 具体位置：§3.5 (Model and Inference): \"All experiments use single-seed evaluation; variance across seeds is not quantified.\"\n- 问题：Greedy decoding (temp=0) 理论上确定性，但 vLLM 的 FP8 量化和 batch scheduling 可能引入非确定性。更关键的是，5 random type batches per count level 的 sampling variability 未被 replicated across seeds。如果换不同的 5 batches，count curve 形状是否稳定？\n- 建议：至少对 core claims（count curve slope, BCS-accuracy correlation）报告 3 seeds × 5 batches 的 variance decomposition。\n\n**W2** [warning] 跨数据集 embedding 不一致削弱可比性\n\n- 具体位置：Table 1: Few-NERD 用 Qwen3-32B, 其余用 MiniLM\n- 问题：SCS 的数值含义在不同 embedding 空间中完全不同。Few-NERD BCS range [0.77, 0.93] 与 FewRel [0.42, 0.97] 不在同一尺度上。论文声称 \"cross-embedding check confirms directional consistency\" (§3.2)，但 r=0.172 (MiniLM) vs r=0.138 (Qwen3) 方向相同但量级有差异。这使得跨任务比较（如 \"RE 的 channel separation 比 NER 更 clean\"）可能部分归因于 embedding 选择而非任务特性。\n- 建议：对 Few-NERD 补充完整的 MiniLM 分析（不仅是 pairwise correlation check），或明确声明跨任务比较不是论文目标。\n\n**W3** [warning] Count curve 每 level 仅 5 batches，稳定性存疑\n\n- 具体位置：§3.3: \"For each count level, we sample 5 random type batches\"\n- 问题：5 batches 的 SD 估计自由度仅为 4，Figure 1a 的 error bars (±1 SD) 本身的 CI 很宽。在 count=64 时，66 types 中取 64 只有极少数可能的 batch 组合，5 个样本可能接近穷举；但在 count=8-16 时，组合空间巨大，5 个 batch 远不足以代表 population。\n- 建议：增加至 25+ batches 或报告 bootstrap CI on the mean（而非 SD bars）。\n\n**W4** [warning] FewRel 合并 train+val splits 的方法论风险\n\n- 具体位置：§3.1: \"we combine the training and validation splits to obtain the full 80-relation pool\"\n- 问题：FewRel 的 train/val splits 可能被设计为具有不同特征（如 val 中的 relations 可能更难/更容易）。论文在 Limitations 中提到 \"train-origin relations show numerically lower accuracy than val-origin (−8.8pp, p=0.06, n.s.)\"——这本身就暗示存在 split-level confound。虽然 p=0.06 不显著，但 8.8pp 的差异不可忽视。\n- 建议：在 BCS-controlled 分析中加入 split-origin 作为 covariate，或报告 results stratified by origin。\n\n**W5** [warning] TOST equivalence margin (±3pp) 的 justification 非标准\n\n- 具体位置：Appendix §Factorial: \"motivated by two considerations: (1) prompt design variation induces accuracy shifts of ≈25pp, so a 3pp interaction would represent only 12% of prompt-induced noise\"\n- 问题：TOST margin 应基于 smallest effect size of interest (SESOI)，即 \"多大的 interaction 会改变实践决策\"，而非相对于 noise 的比例。用 noise 作为 reference 是非标准做法——noise 大不意味着 3pp 的 interaction 不重要。如果 practitioner 关心的是 \"我的 schema 设计是否需要考虑 count×BCS interaction\"，3pp 可能已经有实际意义。\n- 建议：(1) 从 practitioner decision boundary 角度重新论证 margin（如 \"在我们的应用场景中，<3pp 的 accuracy 变化不会改变 schema 选择\"）；(2) 或增加 ±1pp 和 ±2pp 的 sensitivity 已做到（Table in appendix），但应在正文中讨论 ±1pp inconclusive 的含义。\n\n---\n\n## 小问题（不影响接收）\n\n- §1 Introduction: \"recall drops from 0.72 with a single candidate type to 0.42 with 64 types, a 42% relative decline\" — 实际相对下降是 (0.72-0.42)/0.72 = 41.7%，约等于 42%，OK。\n- Table 2: FewRel r=0.187 被省略因 \"RE's per-instance format precludes direct cross-task comparison\" — 但 r² 数字在 SCS validation (§3.2) 中已报告为 evidence，逻辑上应统一处理。\n- Limitations 段落的 \"Multiple comparisons\" 引用 Rothman (1990) 辩护不做 family-wise correction — 这一论点在 NLP 社区有争议，应至少 acknowledge 对立观点。\n- Abstract 文字较密，建议结构化为 problem → method → key findings → implication 以提高可读性。\n\n---\n\n## 主要优势\n\n1. **问题设定精准且有价值**：isolate count vs confusability 是 LLM IE 领域一个重要且未被正式研究的问题。BCS-controlled design 是一个优雅的实验范式。\n\n2. **高度诚实的负面结果报告**：SDGD 完全失败、MAVEN 正向 confound、multiple factorial tests 未通过——全部如实报告并深入分析。这在 NLP 论文中罕见且值得赞赏。\n\n3. **分析深度出色**：within-pool control、centrality confound 识别与处理、aggregation simulation、TOST sensitivity analysis、cross-model validation——每个潜在 confound 都被识别并 addressed。\n\n4. **Limitations 质量极高**：7 条具体、可操作的 limitation，涵盖 effect size、factorial failure、causal mechanism 等，优于绝大多数提交论文。\n\n5. **跨任务一致性**：核心效应方向在 NER/RE/ED 三个任务、4 个数据集、2 个模型上方向一致，增强了结论可信度。\n\n---\n\n## Questions to Authors\n\nQ1: 如果用 unconditional r²=0.013 替代 conditional R²=0.074 作为 aggregation simulation 的输入，模拟的 batch-level R² 是多少？这是否仍能解释观察到的 0.218？\n\nQ2: 5 random batches per count level 中，你们观察到的 batch-to-batch variance 有多大？是否有 batch 组合使 count curve 非单调？\n\nQ3: 论文将 \"cleanly separable\" 作为 RE 的核心特征——但如果只有 full regression 通过 TOST 而两个 factorial designs 都失败，你们如何向读者保证这不是 cherry-picking the test that works？\n\nQ4: NER 的 positive batch-level BCS-F1 correlation (r=+0.50/+0.58) 被归因于 type-frequency confound。但如果 BCS 和 frequency 相关，那么在 BCS-controlled design 中，controlling BCS 是否也间接 controlled frequency，从而使 Channel 2 效应被 attenuate？\n\n---\n\n## Missing References\n\n- Lakens (2017) \"Equivalence Tests: A Practical Primer\" — 更完整地介绍 TOST 方法学，尤其是 margin justification 的最佳实践\n- Simmons et al. (2011) \"False-Positive Psychology\" — 关于 researcher degrees of freedom 和 garden of forking paths\n- 建议引用 Stefan et al. (2019) on SESOI determination methods for TOST",
  "reviewer_id": "1",
  "project": "schema-dag-extraction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## 总体评分\n**Overall**: 3.5/5 (介于 Findings acceptance 和 Conference acceptance 之间)\n**一句话总结**: 一篇诚实且方法论透明的分析性论文，但核心效应量过小（pairwise r²=1.3-1.7%）、多项关键统计检验未通过（3/4 factorial tests 失败）、且唯一通过的检验依赖于测试选择，削弱了\"两通道可分离\"的核心 claim。\n\n## 官方维度打分（来自 ACL ARR review form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3/5 | 主要 claims 有证据支撑但力度不足：effect size 极小，factorial 显著性依赖测试方法选择，多处条件分析未过显著性门槛 |\n| Excitement | 3.5/5 | 问题设定有价值（isolate count vs confusability），方法论框架（SCS/BCS + controlled design）可复用，但负面结果（SDGD 失败）限制了实用影响力 |\n| Reproducibility | 3.5/5 | 报告了模型、种子、bootstrap 参数；但 single-seed evaluation、未量化跨种子方差、代码未公开是主要缺陷 |\n| Reviewer Confidence | 4/5 | 统计方法论和实验设计是我的专长领域 |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] Factorial separability claim 建立在选择性测试上\n\n- 具体位置：§4.4 (Multi-Channel Degradation) + Appendix §Factorial Analysis\n- 问题：论文声称 count 和 confusability \"cleanly separable in RE (TOST p=0.003)\"，但这一结论依赖于选择最有利的检验：\n  - Few-NERD 2×2 factorial: p=0.50（不显著）\n  - FewRel 2×2 factorial (n=54): p_TOST=0.56（不显著）\n  - FewRel full regression (n=69, 5 count levels): p_TOST=0.003（显著）\n\n  三项检验中只有一项通过。论文声称 \"regression approach provides the stronger test by leveraging the full count range\"——但这是 post-hoc 对测试选择的辩护。如果研究者在设计阶段就确定 full regression 是 primary test，应在方法部分预注册/声明；当前呈现方式是先展示失败的检验、再解释为何另一个更好，这是典型的 garden of forking paths 问题。\n- 为什么影响接收：additivity/separability 是论文五个核心发现之一（Finding 1: \"cleanly separable in RE\"），也是 abstract 和 conclusion 的关键措辞。如果 separability 只在特定测试下成立，结论需要大幅软化。\n- 建议修改方向：(1) 在 §3.3 明确预先指定 primary test（如果确实是 regression，需解释为什么）；(2) 将 abstract/conclusion 中的 \"cleanly separable\" 改为 \"consistent with additive separability under the full-range regression (TOST p=0.003), though lower-powered 2×2 designs did not reach equivalence\"；(3) 或执行 pre-registered replication 用独立数据验证。\n\n**N2** [critical] 典型效应量（2.2pp）是否足以支撑核心论点？\n\n- 具体位置：§4.3 Practical magnitude; Table 2 (pairwise r²=1.3-1.7%)\n- 问题：论文报告的 \"typical\" confusability gap 仅为 2.2pp（95% CI: [0.4, 4.0]），pairwise r²=1.3-1.7%。这意味着：\n  - 在自然随机 batching 条件下，confusability 对 accuracy 的实际贡献约 2pp\n  - 高达 98.3-98.7% 的 type confusion variance 由其他因素解释\n  - CI 下界为 0.4pp——接近于零实际意义\n\n  论文通过两种方式放大感知效应量：(a) 引用 extreme-batch gap (-31.2pp)；(b) conditioning on non-zero pairs 将 r² 从 1.3% 提升到 7%——但后者是 selection on dependent variable，论文虽承认 \"conditioning inflates this\" 但仍将 7% 作为 aggregation simulation 的输入。Abstract 中 \"batch-level BCS explains up to 53% of cross-batch variance\" 来自 DocRED 的极端条件，不代表一般性结论。\n- 为什么影响接收：如果 confusability 的 typical impact 仅为 2pp，其作为 \"degradation channel\" 的实用价值和理论意义均可质疑。Reviewer 需要判断这是否是一个 \"real but trivially small\" 的效应。\n- 建议修改方向：(1) Abstract 应前置 typical 效应量（2.2pp），而非先报告 extreme/conditional 数字；(2) 明确讨论 practical significance vs statistical significance 的区别；(3) 考虑是否应将论文重新定位为 \"confusability is detectable but not the primary driver\"，这仍然是有价值的发现但需要不同的 framing。\n\n**N3** [critical] Conditioning on non-zero pairs 引入选择偏差，且作为后续分析的基础\n\n- 具体位置：§4.3 Practical magnitude; Appendix §Pair-to-Batch Aggregation Simulation\n- 问题：\n  - 全部 type pairs 中只有约 30-40% 实际产生非零 confusion（Few-NERD: 1,953/2,145 有 non-zero co-occurrence，但多少有 non-zero confusion 未报告）\n  - 论文将 unconditional r²=1.3% 和 conditional r²=7%（non-zero pairs only）并列报告\n  - Appendix 的 Monte Carlo aggregation simulation 使用 conditional R²=0.074 作为输入参数，模拟得到 batch-level R²=0.219\n  - 但如果用 unconditional r²=0.013 作为输入，模拟结果会大幅缩水\n  \n  这构成了一个逻辑链问题：conditional estimate → simulation → \"explains\" batch-level R²，但 conditioning step 本身是有偏的。\n- 为什么影响接收：aggregation simulation 是论文解释 \"为什么 pairwise 效应小但 batch 效应大\" 的关键桥梁。如果这个桥梁的输入有偏，batch-level 的解释力就缺乏坚实基础。\n- 建议修改方向：(1) 用 unconditional r² 重新运行 simulation，报告两种输入下的结果；(2) 如果 unconditional 版本不能 reproduce batch-level R²，需要承认 conditioning 不仅 inflates 而且 distorts 解释；(3) 或提供 formal justification for why conditioning is the correct analytical frame。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] Single-seed evaluation 无法量化推断不确定性\n\n- 具体位置：§3.5 (Model and Inference): \"All experiments use single-seed evaluation; variance across seeds is not quantified.\"\n- 问题：Greedy decoding (temp=0) 理论上确定性，但 vLLM 的 FP8 量化和 batch scheduling 可能引入非确定性。更关键的是，5 random type batches per count level 的 sampling variability 未被 replicated across seeds。如果换不同的 5 batches，count curve 形状是否稳定？\n- 建议：至少对 core claims（count curve slope, BCS-accuracy correlation）报告 3 seeds × 5 batches 的 variance decomposition。\n\n**W2** [warning] 跨数据集 embedding 不一致削弱可比性\n\n- 具体位置：Table 1: Few-NERD 用 Qwen3-32B, 其余用 MiniLM\n- 问题：SCS 的数值含义在不同 embedding 空间中完全不同。Few-NERD BCS range [0.77, 0.93] 与 FewRel [0.42, 0.97] 不在同一尺度上。论文声称 \"cross-embedding check confirms directional consistency\" (§3.2)，但 r=0.172 (MiniLM) vs r=0.138 (Qwen3) 方向相同但量级有差异。这使得跨任务比较（如 \"RE 的 channel separation 比 NER 更 clean\"）可能部分归因于 embedding 选择而非任务特性。\n- 建议：对 Few-NERD 补充完整的 MiniLM 分析（不仅是 pairwise correlation check），或明确声明跨任务比较不是论文目标。\n\n**W3** [warning] Count curve 每 level 仅 5 batches，稳定性存疑\n\n- 具体位置：§3.3: \"For each count level, we sample 5 random type batches\"\n- 问题：5 batches 的 SD 估计自由度仅为 4，Figure 1a 的 error bars (±1 SD) 本身的 CI 很宽。在 count=64 时，66 types 中取 64 只有极少数可能的 batch 组合，5 个样本可能接近穷举；但在 count=8-16 时，组合空间巨大，5 个 batch 远不足以代表 population。\n- 建议：增加至 25+ batches 或报告 bootstrap CI on the mean（而非 SD bars）。\n\n**W4** [warning] FewRel 合并 train+val splits 的方法论风险\n\n- 具体位置：§3.1: \"we combine the training and validation splits to obtain the full 80-relation pool\"\n- 问题：FewRel 的 train/val splits 可能被设计为具有不同特征（如 val 中的 relations 可能更难/更容易）。论文在 Limitations 中提到 \"train-origin relations show numerically lower accuracy than val-origin (−8.8pp, p=0.06, n.s.)\"——这本身就暗示存在 split-level confound。虽然 p=0.06 不显著，但 8.8pp 的差异不可忽视。\n- 建议：在 BCS-controlled 分析中加入 split-origin 作为 covariate，或报告 results stratified by origin。\n\n**W5** [warning] TOST equivalence margin (±3pp) 的 justification 非标准\n\n- 具体位置：Appendix §Factorial: \"motivated by two considerations: (1) prompt design variation induces accuracy shifts of ≈25pp, so a 3pp interaction would represent only 12% of prompt-induced noise\"\n- 问题：TOST margin 应基于 smallest effect size of interest (SESOI)，即 \"多大的 interaction 会改变实践决策\"，而非相对于 noise 的比例。用 noise 作为 reference 是非标准做法——noise 大不意味着 3pp 的 interaction 不重要。如果 practitioner 关心的是 \"我的 schema 设计是否需要考虑 count×BCS interaction\"，3pp 可能已经有实际意义。\n- 建议：(1) 从 practitioner decision boundary 角度重新论证 margin（如 \"在我们的应用场景中，<3pp 的 accuracy 变化不会改变 schema 选择\"）；(2) 或增加 ±1pp 和 ±2pp 的 sensitivity 已做到（Table in appendix），但应在正文中讨论 ±1pp inconclusive 的含义。\n\n---\n\n## 小问题（不影响接收）\n\n- §1 Introduction: \"recall drops from 0.72 with a single candidate type to 0.42 with 64 types, a 42% relative decline\" — 实际相对下降是 (0.72-0.42)/0.72 = 41.7%，约等于 42%，OK。\n- Table 2: FewRel r=0.187 被省略因 \"RE's per-instance format precludes direct cross-task comparison\" — 但 r² 数字在 SCS validation (§3.2) 中已报告为 evidence，逻辑上应统一处理。\n- Limitations 段落的 \"Multiple comparisons\" 引用 Rothman (1990) 辩护不做 family-wise correction — 这一论点在 NLP 社区有争议，应至少 acknowledge 对立观点。\n- Abstract 文字较密，建议结构化为 problem → method → key findings → implication 以提高可读性。\n\n---\n\n## 主要优势\n\n1. **问题设定精准且有价值**：isolate count vs confusability 是 LLM IE 领域一个重要且未被正式研究的问题。BCS-controlled design 是一个优雅的实验范式。\n\n2. **高度诚实的负面结果报告**：SDGD 完全失败、MAVEN 正向 confound、multiple factorial tests 未通过——全部如实报告并深入分析。这在 NLP 论文中罕见且值得赞赏。\n\n3. **分析深度出色**：within-pool control、centrality confound 识别与处理、aggregation simulation、TOST sensitivity analysis、cross-model validation——每个潜在 confound 都被识别并 addressed。\n\n4. **Limitations 质量极高**：7 条具体、可操作的 limitation，涵盖 effect size、factorial failure、causal mechanism 等，优于绝大多数提交论文。\n\n5. **跨任务一致性**：核心效应方向在 NER/RE/ED 三个任务、4 个数据集、2 个模型上方向一致，增强了结论可信度。\n\n---\n\n## Questions to Authors\n\nQ1: 如果用 unconditional r²=0.013 替代 conditional R²=0.074 作为 aggregation simulation 的输入，模拟的 batch-level R² 是多少？这是否仍能解释观察到的 0.218？\n\nQ2: 5 random batches per count level 中，你们观察到的 batch-to-batch variance 有多大？是否有 batch 组合使 count curve 非单调？\n\nQ3: 论文将 \"cleanly separable\" 作为 RE 的核心特征——但如果只有 full regression 通过 TOST 而两个 factorial designs 都失败，你们如何向读者保证这不是 cherry-picking the test that works？\n\nQ4: NER 的 positive batch-level BCS-F1 correlation (r=+0.50/+0.58) 被归因于 type-frequency confound。但如果 BCS 和 frequency 相关，那么在 BCS-controlled design 中，controlling BCS 是否也间接 controlled frequency，从而使 Channel 2 效应被 attenuate？\n\n---\n\n## Missing References\n\n- Lakens (2017) \"Equivalence Tests: A Practical Primer\" — 更完整地介绍 TOST 方法学，尤其是 margin justification 的最佳实践\n- Simmons et al. (2011) \"False-Positive Psychology\" — 关于 researcher degrees of freedom 和 garden of forking paths\n- 建议引用 Stefan et al. (2019) on SESOI determination methods for TOST",
    "reviewer_id": "1",
    "project": "schema-dag-extraction"
  }
}
```

</details>

---


### Tool result

_source line 413 · 2026-05-16T16:38:20.088558+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4094
}
```

</details>

---


### Assistant

_source line 414 · 2026-05-16T16:38:27.176429+00:00_

审稿意见已提交给 Review Director。

核心判断：论文问题设定有价值、分析深度出色、负面结果报告诚实，但三个 critical issues 削弱了核心 claims——(1) separability claim 依赖选择性测试（3/4 factorial 失败），(2) typical 效应量仅 2.2pp 的实用意义可疑，(3) aggregation simulation 的输入基于有偏的 conditional estimate。建议评分 Overall 3.5/5，介于 Findings 和 Main Conference 之间。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1"
}
```

</details>

---


## Round 16

## Round 16

4 recorded events


### User

_source line 415 · 2026-05-16T16:42:22.058745+00:00_

[Round 1 审稿请求]:
以下是 Reviewer 2 的完整审稿意见，请逐条回应：对每个 Must-Fix / Should-Fix / Minor 问题标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。也请对 R2 的 Strengths 和缺失引用给出你的看法。

---

## Reviewer 2 完整审稿意见

**Overall**: 3.0/5

**官方维度打分**:
| 维度 | 分数 |
|------|------|
| Soundness | 3.5/5 |
| Excitement | 2.5/5 |
| Reproducibility | 4.0/5 |
| Reviewer Confidence | 4/5 |

### Must-Fix

**N1** [critical] 核心发现 novelty 不足
- SCS = LLM-PEE 的 partitioning criterion（论文自己承认）
- "similar labels cause confusion" 是 common sense
- pairwise r²=1.3-1.7% 意味 SCS 只解释极小部分 variance
- "Controlled factorial design" 是标准方法论，不构成创新
- 建议：挖掘剩余 98.3% variance 由什么解释，或提出更好 predictor

**N2** [critical] Contribution #4 "Diagnosis to mitigation" framing 误导
- NER SDGD: F1 0.445→0.251；RE graph-coloring: +1.4pp n.s.
- "Mitigation" 暗示成功，但 RQ3 答案是 negative
- 建议：改为 "Schema decomposition reveals structural barriers"

**N3** [critical] Hierarchical classification / label confusion 文献覆盖严重不足
- 遗漏：Zhou et al. NAACL 2025, Guo et al. AAAI 2021, Novack et al. ICML 2023 (CHiLS), ZERONER ACL Findings 2025
- 只引了 Deng et al. (2010) ImageNet
- 削弱 "first controlled study" 声称

### Should-Fix

**W1** Abstract/Introduction headline 数字 cherry-picking（"up to 53%" 是极端条件）
**W2** "First controlled study" 声称需 qualify
**W3** Single-seed 评估削弱 claim 稳健性
**W4** LLM-PEE 对比不够公平和深入
**W5** RE 实验的 ecological validity

### Strengths
1. 实验设计精巧
2. 负结果的诚实报告
3. Centrality confound 分析
4. 统计方法规范
5. 四数据集三任务覆盖 + cross-model

### Missing References
- Zhou et al., NAACL 2025 — Semantic Similarity through Classification Confusion
- Guo et al., AAAI 2021 — Label Confusion Learning
- Novack et al., ICML 2023 — CHiLS
- ZERONER, ACL Findings 2025

---

请逐条回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---
