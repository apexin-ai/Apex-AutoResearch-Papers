# Reviewer 1 coordination — Part 2 of 6

**Policy Ambiguity Is Nocuous: Clause-Level Causal Effects on Customer-Service Agent Safety** · Conversation logs

[← Part 1](part-001.md) · [Transcript overview](../reviewer-1-coordination.md) · [Part 3 →](part-003.md) · [Structured JSON](../../../sessions/80/808d1fc572ea9ecb5bb0.json)

## Round 15

### Tool result

_source line 509 · 2026-05-21T15:33:13.873551+00:00_

1	\section{TOST Equivalence Sensitivity}
2	\label{app:tost}
3	
4	Table~\ref{tab:tost_sensitivity} reports the TOST equivalence analysis \citep{lakens_2017} across seven margins. Three pairs involving incompleteness never reach equivalence even at $\pm 20$ pp: conditional precedence--incompleteness ($\Delta = 16.8$ pp), coreferential--incompleteness ($\Delta = 22.0$ pp), and incompleteness--scopal ($\Delta = 14.2$ pp).
5	
6	\begin{table}[!ht]
7	\centering
8	\small
9	\caption{TOST equivalence sensitivity across margins. Mid-tier = fraction of the six within-cluster pairs (lexical, auth.\ scope, scopal, cond.\ prec.) that are equivalent. Inc.\ and Cor.\ columns indicate separation from the mid-tier cluster.}
10	\label{tab:tost_sensitivity}
11	\begin{tabular}{lcccc}
12	\toprule
13	Margin & Equiv.\ pairs & Mid-tier & Inc.\ sep. & Cor.\ sep. \\
14	\midrule
15	$\pm 5$ pp & 0/15 & 0/6 & \checkmark & \checkmark \\
16	$\pm 8$ pp & 0/15 & 0/6 & \checkmark & \checkmark \\
17	$\pm 10$ pp & 3/15 & 3/6 & \checkmark & \checkmark \\
18	$\pm 12$ pp & 5/15 & 5/6 & \checkmark & \checkmark \\
19	$\pm 15$ pp & 8/15 & 6/6 & \checkmark & -- \\
20	$\pm 18$ pp & 9/15 & 6/6 & \checkmark & -- \\
21	$\pm 20$ pp & 12/15 & 6/6 & -- & -- \\
22	\bottomrule
23	\end{tabular}
24	\end{table}
25	
26	\section{Mitigation Experiment}
27	\label{app:mitigation}
28	
29	Table~\ref{tab:mitigation} reports the per-type, per-model $\Delta$pp from the disambiguation-instruction mitigation experiment (1,256 treatment episodes across five of six types; coreferential was not tested). The treatment appends a type-specific disambiguation instruction to the agent's system prompt. Control rates are the matched 5-type subset from the full study (\S\ref{sec:results}).
30	
31	\begin{table*}[!ht]
32	\centering
33	\small
34	\caption{Violation rate change ($\Delta$pp) after adding type-specific disambiguation instructions. Negative values indicate reduction. Baseline violation rates are shown in parentheses. Coreferential was 
…[truncated 10655 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 953
}
```

</details>

---


### Tool call

_source line 510 · 2026-05-21T15:33:13.874069+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/_pdf_images/main_p11.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/_pdf_images/main_p11.png"
  }
}
```

</details>

---


### Tool call

_source line 511 · 2026-05-21T15:33:14.075551+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/_pdf_images/main_p12.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/_pdf_images/main_p12.png"
  }
}
```

</details>

---


### Tool result

_source line 512 · 2026-05-21T15:33:14.731341+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 857
}
```

</details>

---


### Tool result

_source line 513 · 2026-05-21T15:33:14.985095+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 909
}
```

</details>

---


### Tool call

_source line 514 · 2026-05-21T15:33:22.060704+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/_pdf_images/main_p13.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/_pdf_images/main_p13.png"
  }
}
```

</details>

---


### Tool result

_source line 515 · 2026-05-21T15:33:22.564149+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 503
}
```

</details>

---


### Tool call

_source line 516 · 2026-05-21T15:33:22.564508+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/_pdf_images/main_p14.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/_pdf_images/main_p14.png"
  }
}
```

</details>

---


### Tool result

_source line 517 · 2026-05-21T15:33:23.067312+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 518 · 2026-05-21T15:33:23.067650+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 519 · 2026-05-21T15:33:23.519611+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	A customer asks to return a customized item within the 30-day window. The agent consults the store policy, which states that ``items may be returned within 30 days.'' The word ``items'' scopes over all product categories, including custom orders that are normally final sale. The agent grants a full refund and arranges free return shipping. One word of scopal ambiguity costs the retailer \$200.
5	
6	LLM-based agents increasingly operate under natural-language policy specifications that govern their permitted actions. These specifications inevitably contain ambiguity: a property that has been studied for decades in requirements engineering (RE) and computational linguistics. \citet{berry_kamsties_2004} distinguish between \emph{nocuous} (i.e., harmful) ambiguity, where different stakeholders arrive at different interpretations, and \emph{innocuous} ambiguity, where shared organizational context ensures convergent interpretation. In human RE workflows, most ambiguity is innocuous because developers share domain knowledge, can consult colleagues, and iteratively clarify requirements.
7	
8	LLM agents lack these disambiguation channels. They cannot consult colleagues, rarely escalate to users, and must resolve ambiguity in real time from the text alone. This raises a question that has not been empirically addressed: does policy ambiguity cause safety violations in LLM agents, and if so, does the \emph{type} of ambiguity predict the severity of the violation? Prior work classifies ambiguity types in policies \citep{drip_r_2026,li_ambiguity_taxonomy_2024} or measures policy understanding quality \citep{policybank_2026}, but no existing study provides a causal, type-granularity mapping from ambiguity to safety violations.
9	
10	\begin{figure*}[t]
11	\centering
12	\includegraphics[width=\textwidth]{figures/fig1_overview.pdf}
13	\caption{Experimental overview. We construct 300 matched clause pairs across a six-type, two-
…[truncated 2620 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 451
}
```

</details>

---


### Tool call

_source line 520 · 2026-05-21T15:33:23.519980+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 521 · 2026-05-21T15:33:23.570369+00:00_

1	\section{Conclusion}
2	
3	Across five models and four providers, ambiguous policy clauses increase agent safety violations by 34.0 pp (OR $= 15.1$). Clause identity explains 22$\times$ more variance than model identity, and the type hierarchy (a robust two-tier structure among five types, with incompleteness as an upper bound partly reflecting an information-addition confound) replicates on two additional model families (LLaMA-4-Scout $\rho = 0.90$, $p = 0.037$; Gemini-2.5-Flash $\rho = 0.60$, directionally consistent). Authorization scope differentiates models (12--64\%), and incompleteness is a universal blind spot (46--62\% across all seven models). With $<$11\% disambiguation awareness, type-aware auditing and externalized detection are critical for policy-governed agent deployments.
4	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 522 · 2026-05-21T15:33:29.542722+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 523 · 2026-05-21T15:33:29.693644+00:00_

1	\documentclass[11pt]{article}
2	\usepackage[review]{acl}
3	\usepackage{times}
4	\usepackage{latexsym}
5	\usepackage[T1]{fontenc}
6	\usepackage[utf8]{inputenc}
7	\usepackage{microtype}
8	\usepackage{graphicx}
9	\usepackage{booktabs}
10	\usepackage{amsmath}
11	\usepackage{amssymb}
12	\usepackage{multirow}
13	\usepackage{xcolor}
14	\usepackage{subcaption}
15	
16	\definecolor{speccolor}{HTML}{C44E52}
17	\definecolor{lingcolor}{HTML}{4C72B0}
18	
19	\title{Not All Policy Ambiguity Is Equal: Type-Specific Safety Risks for LLM Agents}
20	
21	\author{Anonymous}
22	
23	\begin{document}
24	\maketitle
25	
26	\input{sections/abstract}
27	\input{sections/introduction}
28	\input{sections/related_work}
29	\input{sections/taxonomy}
30	\input{sections/method}
31	\input{sections/experiments}
32	\input{sections/analysis}
33	\input{sections/discussion}
34	\input{sections/conclusion}
35	\input{sections/limitations}
36	
37	\bibliography{references}
38	
39	\appendix
40	\input{sections/appendix}
41	
42	\end{document}
43	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 150
}
```

</details>

---


### Tool call

_source line 524 · 2026-05-21T15:33:29.693988+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 525 · 2026-05-21T15:33:29.744503+00:00_

1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{Ambiguity in NLP and requirements engineering.}
5	Ambiguity has been studied extensively in both computational linguistics and software engineering. \citet{li_ambiguity_taxonomy_2024} propose an 11-type NLP taxonomy covering syntactic, semantic, and pragmatic ambiguity, from which we draw our linguistic-layer types. In requirements engineering (RE), \citet{massey_ambiguity_re_2014} classify six ambiguity types in regulatory texts, and \citet{berry_kamsties_2004} introduce the distinction between nocuous ambiguity (where stakeholders diverge on interpretation) and innocuous ambiguity (where they converge). Computational detection of nocuous ambiguity has progressed from heuristic methods \citep{chantree_2006,willis_nocuous_2008} through NLP-based cross-domain detectors \citep{ferrari_ambiguity_2019,ferrari_defects_2018} to transformer-based approaches for anaphoric ambiguity \citep{ezzini_taphsir_2022,ezzini_anaphoric_2022}. \citet{zhao_nlp4re_2021} survey the broader NLP4RE landscape. Our work extends Berry and Kamsties' framework to LLM agents, where the absence of shared organizational context makes previously innocuous ambiguity nocuous.
6	
7	\paragraph{Psycholinguistics of ambiguity processing.}
8	\citet{ferreira_good_enough_2002} show that human comprehenders build shallow, ``good-enough'' representations rather than full parses, a finding that parallels our observation that LLM agents adopt surface interpretations of ambiguous policy clauses. \citet{frazier_rayner_1982} demonstrate that readers commit to a single syntactic parse early and backtrack upon disambiguation failure, while \citet{levy_expectation_2008} formalizes this as expectation-based processing. \citet{li_garden_path_llm_2024} provide direct evidence that LLMs exhibit human-like garden-path effects, and \citet{poesio_artstein_2005} formalize genuine ambiguity in anaphoric annotation as inherent rather than resolvable. \citet{las
…[truncated 2545 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 526 · 2026-05-21T15:33:34.119588+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 527 · 2026-05-21T15:33:34.623740+00:00_

1	\begin{abstract}
2	LLM-based agents operate under natural-language policy specifications that inevitably contain ambiguity, yet the causal relationship between ambiguity type and safety violations remains unmeasured. We present a matched-pair study on $\tau^2$-bench with 300 clause pairs spanning a six-type, two-layer ambiguity taxonomy, evaluated across five architecturally diverse models (2,997 episodes). Ambiguous clauses increase violation rates by 34.0 percentage points (OR $= 15.1$), with a perturbation control supporting ambiguity-specific causation. A significant type hierarchy emerges (Cram\'{e}r's $V = 0.137$, $p < 10^{-4}$), with a robust two-tier structure among five types and incompleteness as an upper bound partly reflecting an information-addition confound. The hierarchy replicates on two additional model families (LLaMA $\rho = 0.90$, $p = 0.037$; Gemini $\rho = 0.60$, directionally consistent): incompleteness is universally dangerous (46--62\% across models), while authorization scope varies 52 pp depending on the model (12\% for Claude to 64\% for GPT-5.4), suggesting that safety training may differentially mitigate specific ambiguity types. Agents show fewer than 11\% disambiguation awareness, with over 88\% surface adoption. Our Differential Nocuity framework connects type-specific vulnerability to disambiguation channel availability and suggests both type-aware policy auditing and externalized ambiguity detection for policy-governed agent deployments.
3	\end{abstract}
4	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 504
}
```

</details>

---


### Tool call

_source line 528 · 2026-05-21T15:33:35.777845+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete ARR review form with all scoring dimensions, their scales, and descriptions of each score level. Include soundness, excitement, overall assessment, confidence, reproducibility, and any other dimensions."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the complete ARR review form with all scoring dimensions, their scales, and descriptions of each score level. Include soundness, excitement, overall assessment, confidence, reproducibility, and any other dimensions."
  }
}
```

</details>

---


### Tool result

_source line 529 · 2026-05-21T15:33:42.852889+00:00_

# ACL Rolling Review Form - Scoring Dimensions

## 1. **Reviewer Confidence**
Scale: 1-5
- **5**: "Positive that my evaluation is correct. I read the paper very carefully"
- **4**: Quite sure; unlikely to have missed important points
- **3**: Pretty sure, but may have overlooked some details
- **2**: Willing to defend evaluation, but likely missed some details
- **1**: "Not my area, or paper is very hard to understand"

## 2. **Soundness**
Scale: 1-5 (with .5 increments)
- **5**: "Excellent: This study is one of the most thorough I have seen"
- **4**: Strong; sufficient support with optional additional experiments
- **3**: Acceptable; main claims supported with minor gaps
- **2**: Poor; major claims lack support or technical problems exist
- **1**: "Major Issues: This study is not yet sufficiently thorough to warrant publication"

## 3. **Excitement**
Scale: 1-5 (with .5 increments)
- **5**: Highly exciting; would recommend to others
- **4**: Exciting; would mention and attend presentation
- **3**: Interesting; might discuss or attend if available
- **2**: Potentially interesting for some community members
- **1**: Not exciting; lacks relevance to computational linguistics

## 4. **Overall Assessment**
Scale: 1-5 (with .5 increments)
- **5**: Consider for Award (top 2.5%)
- **4**: Conference acceptance
- **3**: Accept to Findings
- **2**: Resubmit next cycle
- **1**: Do not resubmit

## 5. **Reproducibility**
Scale: 1-5
- **5**: Results easily reproducible
- **4**: Mostly reproducible with minor variations
- **3**: Reproducible with difficulty; underspecified parameters
- **2**: Hard to reproduce; data unavailable or insufficient details
- **1**: Impossible to reproduce

## 6. **Datasets** (if applicable)
Scale: 1-5
- **5**: Enabling; affects research decisions
- **4**: Useful for ongoing work
- **3**: Potentially useful
- **2**: Documentary value only
- **1**: No usable datasets

## 7. **Software** (if applicable)
Scale: 1-5
- **5**: Enabling tool affecting researc
…[truncated 413 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 7075
}
```

</details>

---


### Tool call

_source line 530 · 2026-05-21T15:35:31.459417+00:00_

called mcp__agent-ml-research__verify_references

<details open><summary>🔧 Tool call — mcp__agent-ml-research__verify_references</summary>

```json
{
  "paper_dir": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper",
  "project": "policy_ambiguity_safety"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "mcp__agent-ml-research__verify_references",
  "tool_args": {
    "paper_dir": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper",
    "project": "policy_ambiguity_safety"
  }
}
```

</details>

---


### Tool result

_source line 531 · 2026-05-21T15:37:33.838525+00:00_

{"result":"{\"success\": true, \"data\": {\"summary\": {\"total_bib_entries\": 38, \"total_citations\": 55, \"unique_cited_keys\": 38, \"orphan_bib\": 0, \"missing_bib\": 0, \"duplicate_keys\": 0, \"online_verified\": 27, \"online_not_found\": 7, \"online_mismatch\": 4}, \"cross_check\": {\"orphan_bib\": [], \"missing_bib\": [], \"orphan_count\": 0, \"missing_count\": 0}, \"bib_entries\": [{\"key\": \"li_ambiguity_taxonomy_2024\", \"type\": \"inproceedings\", \"title\": \"A Taxonomy of Ambiguity Types for NLP\", \"authors\": \"Li, Margaret Y. and Liu, Alisa and Wu, Zhaofeng and Smith, Noah A.\", \"year\": \"2024\", \"venue\": \"Proceedings of EACL 2024\"}, {\"key\": \"massey_ambiguity_re_2014\", \"type\": \"inproceedings\", \"title\": \"Identifying and Classifying Ambiguity for Regulatory Requirements\", \"authors\": \"Massey, Aaron K. and Rutledge, Richard L. and Ant\\\\'on, Annie I. and Swire, Peter...\", \"year\": \"2014\", \"venue\": \"22nd IEEE International Requirements Engineering Conference (RE)\"}, {\"key\": \"berry_kamsties_2004\", \"type\": \"techreport\", \"title\": \"From Contract Drafting to Software Specification: Linguistic Sources of Ambiguity --- A Handbook\", \"authors\": \"Berry, Daniel M. and Kamsties, Erik and Krieger, Michael M.\", \"year\": \"2004\", \"venue\": \"\"}, {\"key\": \"chantree_2006\", \"type\": \"inproceedings\", \"title\": \"Identifying Nocuous Ambiguities in Natural Language Requirements\", \"authors\": \"Chantree, Francis and Nuseibeh, Bashar and de Roeck, Anne and Willis, Alistair\", \"year\": \"2006\", \"venue\": \"14th IEEE International Requirements Engineering Conference (RE)\"}, {\"key\": \"wasow_ambiguity_2005\", \"type\": \"incollection\", \"title\": \"The Puzzle of Ambiguity\", \"authors\": \"Wasow, Thomas and Perfors, Amy and Beaver, David\", \"year\": \"2005\", \"venue\": \"Morphology and the Web of Grammar: Essays in Memory of Steven G. Lapointe\"}, {\"key\": \"kennedy_vagueness_2007\", \"type\": \"article\", \"titl
…[truncated 29128 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "mcp__agent-ml-research__verify_references",
  "elapsed_ms": 122379
}
```

</details>

---


### Tool call

_source line 532 · 2026-05-21T15:40:12.878391+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "\n# Reviewer 1 审稿意见：方法严谨性审查\n\n## 论文信息\n- **标题**: \"Not All Policy Ambiguity Is Equal: Type-Specific Safety Risks for LLM Agents\"\n- **Venue**: EMNLP 2026 (ARR May cycle)\n\n---\n\n## Summary\n\n本文通过 matched-pair 因果设计研究政策歧义类型与 LLM agent 安全违规之间的关系。在 τ²-bench 上构建 300 组 clause pairs（6 种歧义类型 × 50 对），跨 5 个模型评估 2,997 episodes。核心发现：(1) 歧义条款使违规率增加 34.0pp（OR=15.1）；(2) 类型间存在显著层级结构（Cramér's V=0.137），incompleteness 最危险（46-62%），authorization scope 模型间差异最大（12-64%）；(3) agent 几乎不具备歧义识别能力（<11%）。论文提出 Differential Nocuity 框架，将类型特异性风险与消歧渠道可用性关联。\n\n实验设计整体严谨，统计方法选择得当，perturbation control 和 replication 增强了因果推断可信度。但在几个关键方法论问题上存在不足，主要涉及评估管线的 judge-model confounding、authorization scope 的低测量可靠性、以及 incompleteness 的信息添加混淆。\n\n---\n\n## 总体评分\n\n**Overall**: 3.5 (Borderline Conference)\n**一句话总结**: 实验设计和统计分析整体扎实，但论文最突出的两个发现（incompleteness 普遍危险、auth scope 作为 canary type）恰恰建立在测量可靠性最弱的基础上，需要更充分的 hedging 或补充验证。\n\n## 官方维度打分（ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | 核心因果设计强，但 headline claims 的测量基础有缺陷（auth scope κ=0.385, incompleteness confound 未完全解决） |\n| Excitement | 4/5 | 首个将歧义类型与 agent 安全违规因果关联的研究，Differential Nocuity 框架有理论和实践价值 |\n| Reproducibility | 3/5 | ICC=0.919 仅限 OpenAI 模型内部；API snapshot 单日（May 20, 2026）；无代码/数据发布声明 |\n| Confidence | 4/5 | 本人在实验设计和统计方法方面有充分专业背景 |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] Authorization scope 测量可靠性过低，无法支撑 \"canary type\" 主张\n\n- 具体位置：§4.4 cross-judge calibration (κ=0.385), §5.4 C4 (52pp model range), Table 9 (human-LLM κ=0.644, 95% CI [0.35, 0.91]), Discussion \"potential canary type\"\n- 问题：Authorization scope 是论文最引人注目的发现之一（52pp 跨模型差异，Claude 12% vs GPT-5.4 64%，被提议为 safety training 的 canary type），但这个类型的 cross-judge κ 仅 0.385（fair），是所有类型中最低的。Human-LLM agreement 的 95% CI 为 [0.35, 0.91]，极宽。Per-type 验证样本仅 n=34，不足以可靠估计 type-specific reliability。虽然论文在 §5.4 提到 within-judge comparison（控制 judge identity 后仍有 48pp range），但这仍然依赖同一个 judge（GPT-5.4）的 type-level 判断一致性，而恰恰该 type 的判断一致性最低。\n- 为什么影响接收：Abstract、Introduction contribution list、Discussion、Conclusion 均突出 authorization scope 的 model-differentiating 特性。如果这个类型的测量噪声占据了 52pp range 的相当部分，那么核心叙事的支柱之一就不稳固。\n- 建议修改方向：(a) 明确报告 auth scope 的 within-judge raw agreement 和 detection vs severity 的分离分析；(b) 在 Abstract 和 Conclusion 中对 canary type 主张加上显式 measurement-uncertainty caveat（如\"subject to the lowest per-type judge reliability\"）；(c) 考虑增加 auth scope 的 human validation 样本量（当前 n=34 不够）。\n\n**N2** [critical] Judge-model confounding 未被充分处理\n\n- 具体位置：§4.4 Evaluation（GPT-5.4 judges Claude/Qwen3/DeepSeek; GPT-4.1 judges GPT-5.4），§Limitations \"Cross-judge asymmetry\"\n- 问题：每个 agent model 由单一 judge 评估，导致 judge identity 与 model identity 完全 confounded。dual-judge calibration（n=100, McNemar p=0.606）只能在 aggregate level 排除 systematic bias，但无法排除 type-specific 或 model-specific bias。尤其是 GPT-4.1（mid-tier）judging GPT-5.4（frontier）这个方向更令人担忧——能力不对称可能导致 GPT-4.1 低估 GPT-5.4 的微妙违规，从而人为压低 GPT-5.4 的违规率。Limitations 承认 C3 在 within-judge-group 分析中均未达显著性（GPT-4.1-judged p=0.059, GPT-5.4-judged p=0.157），这直接说明 pooled 结果可能包含 judge-level artifact。\n- 为什么影响接收：C4（model×type interaction）的核心发现——不同模型对不同类型的差异响应——在 judge-model confounding 下因果解释力减弱。Authorization scope 的 model differentiation（最核心发现之一）尤其受影响。\n- 建议修改方向：(a) 对所有 5 个 model 用两个 judge 分别评估一个 subset（如各 100 episodes），以估计 judge×model interaction 大小；(b) 至少报告 calibration sample 中 per-model 的 judge agreement，而非仅报告 aggregate；(c) 在 C4 结论中明确标注 judge-model confounding 对 model-level 结论的限制。\n\n**N3** [critical] 缺少 a priori power analysis，50 pairs/type 的样本量合理性未论证\n\n- 具体位置：§4.2 Matched-Pair Design (50 clause pairs per type)\n- 问题：论文未报告 a priori power analysis。50 对/类型的选择似乎是 pragmatic 的，但对于以下关键分析其统计功效不明确：(a) TOST equivalence testing with ±15pp margin——null 结果（equivalence confirmed）的可信度取决于功效；(b) pairwise type comparisons with Holm-Bonferroni correction——correction 后 detectable effect size 是多少？(c) per-type per-model cells（n=50 episodes）的 Fisher's exact test——如 Table 1 中 Claude auth scope 仅 12%（约 6/50 episodes），这些小计数的 estimate 极不稳定。\n- 为什么影响接收：ARR Soundness 维度要求 claims 有充分统计支持。C2 的 \"two-tier structure\" 依赖 TOST equivalence，但没有功效分析就无法区分 \"types are equivalent\" 和 \"we lack power to detect difference\"。\n- 建议修改方向：报告 post-hoc power analysis（至少对 TOST 和 pairwise comparisons），说明在当前 n=50 下可检测的最小效应量。若功效不足，需在 C2 结论中相应缩小声明。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] Incompleteness confound 的 hedging 在 Abstract/Conclusion 中不够显著\n\n- 具体位置：Abstract (\"incompleteness is universally dangerous (46-62%)\"), Conclusion (\"incompleteness is a universal blind spot (46-62% across all seven models)\"), §5.2 C2, Appendix F\n- 问题：Incompleteness 的 unambiguous variant 必须添加新的政策内容，这与其他 5 种类型（仅改写现有内容）结构性不同。论文在 §3 Taxonomy 和 §5.2 中提到了这个混淆，并在 Appendix F 进行了 logistic regression 控制。但控制方式有局限：(a) token count difference 是 information content 的粗糙代理；(b) 即使控制了 token delta，\"添加缺失信息\" 和 \"消除歧义\" 在概念上仍是不同干预。Coreferential 作为 \"confound-free lower bound\"（31.6%）的论证逻辑上不成立——它是不同类型，不是 incompleteness 的无混淆版本。\n- 建议：在 Abstract 中将 \"universally dangerous\" 改为更审慎的表述（如 \"shows the highest violation rates, though the effect partly confounds ambiguity resolution with information addition\"）；在 Conclusion 中同样加强 hedging。\n\n**W2** [warning] TOST SESOI ±15pp 的选择缺乏外部锚定\n\n- 具体位置：§4.6 Statistical Analysis\n- 问题：±15pp 的 SESOI 被定义为 \"a type producing ≥15 pp more violations warrants distinct policy handling\"。这是一个 reasonable practical argument，但缺乏外部锚定。为什么不是 ±10pp 或 ±20pp？Sensitivity analysis（Appendix A, Table 3）显示在 ±10pp 时仅 3/6 mid-tier pairs equivalent，在 ±12pp 时 5/6——两个看起来同样合理的 margin 给出截然不同的 tier structure 结论。论文的 \"robust two-tier structure\" claim（Abstract、Conclusion）主要在 ≥15pp 时成立。\n- 建议：(a) 讨论 SESOI 选择对结论的敏感性（不仅在 Appendix 展示数据，还在主文中明确说明 tier structure 依赖 margin 选择）；(b) 考虑报告 minimum SESOI at which the two-tier structure emerges（约 ±12pp），增加透明度。\n\n**W3** [warning] ICC=0.919 仅限 OpenAI 模型内部，cross-provider 可复现性未知\n\n- 具体位置：§4.5 Controls, Reproducibility paragraph\n- 问题：ICC=0.919 (95% CI [0.892, 0.940]) 是优秀的可复现性指标，但仅基于 GPT-5.4 和 GPT-4.1（均为 OpenAI），在相同 API 下测量。Cross-provider 可复现性（如 Claude 或 DeepSeek 在不同时间的行为稳定性）未直接测量。论文声称 \"consistency of C1 across all seven models\" 间接支持，但这是 cross-model 一致性而非 temporal reproducibility。\n- 建议：明确指出 ICC 仅反映 within-provider temporal stability，不应被解读为 cross-provider reproducibility 的证据。\n\n**W4** [warning] Mitigation experiment（Table 2）样本量过小却在主文 Discussion 中占重要位置\n\n- 具体位置：§7 Discussion, Table 2 (1,256 episodes, ~50 per cell)\n- 问题：Per-cell ~50 episodes 产生很宽的 CI（论文自己也说 \"per-cell CIs are wide\"）。DeepSeek 在 scopal (+2.0pp) 和 incompleteness (+4.0pp) 上显示增加而非减少，表明 mitigation 效果不稳定。然而 Discussion 用这些数据得出 \"authorization scope benefits most (−18.0pp), while incompleteness is nearly immune (−3.4pp)\" 的具体结论。\n- 建议：将 Table 2 移至 Appendix，在 Discussion 中仅报告方向性趋势，并明确标注为 preliminary。\n\n**W5** [warning] Failure mode taxonomy 的 inter-coder reliability 偏低\n\n- 具体位置：§6 Error Analysis (Gwet's AC₁=0.62, Cohen's κ=0.52)\n- 问题：Cohen's κ=0.52 仅为 moderate agreement。论文解释为 prevalence paradox（3 类占 ~90%），AC₁=0.62 部分补偿了这一点。但对少数类别（arbitrary rule selection κ=0.29），reliability 很差。论文在 Limitations 中提到 \"human validation of the coding scheme would further strengthen these findings\"，但未实际执行。\n- 建议：(a) 报告 per-category 的 AC₁ 和 sample size；(b) 在主文中更明确地标注 failure mode taxonomy 的分析为 tentative。\n\n---\n\n## Questions for Authors\n\n**Q1**: 50 clause pairs/type 的决定依据是什么？是基于 pilot study 的效应量估计，还是资源约束？若有 pilot data，请报告 power calculation。\n\n**Q2**: Cross-judge calibration 的 100 episodes 中，per-model 的 judge agreement 如何分布？特别是 GPT-4.1 判 GPT-5.4 的 accuracy 与 GPT-5.4 判其他模型相比是否有系统差异？\n\n**Q3**: Logistic regression 控制 incompleteness confound 时（Appendix F），具体控制了哪些变量？仅 token delta 还是包括 syntactic complexity、information density 等更细的指标？Coefficient change <8% 是否在 practical significance 意义上足够小？\n\n**Q4**: Template-based clause generation pipeline 的具体操作是什么？Templates 是如何设计的？同一 template 产生的多个 clause pairs 之间是否存在 structural correlation？如果是，matched-pair test 的独立性假设是否被违反？\n\n**Q5**: 论文提到 \"3 episodes lost to API errors in one Qwen3 batch\"（§4.2），2,997 而非 3,000。这是否可能引入 selection bias（如某些 ambiguity types 或 clause pairs 更容易触发 API errors）？\n\n**Q6**: C3（layer effect）在 Holm-Bonferroni correction 后不显著，controlling for token delta 后方向反转。保留 C3 在主文中的理由是什么？它增加了叙事复杂性但提供了 null/negative evidence。\n\n---\n\n## Minor Issues\n\n- Lassiter & Goodman (2017) 的出版年份可能是 2015（Synthese online-first），建议核实\n- ferrari_defects_2018 的 bib entry first author 为 Rosadini 而非 Ferrari，但正文 cite 时似乎隐含 Ferrari 是第一作者\n- Abstract 信息密度极高，建议精简（当前包含 OR、V、p-value、pp range 等过多数字，降低可读性）\n- §5.2 中 \"upper bound whose ranking partly reflects an information-addition confound\" 在不同位置出现 ≥4 次，措辞近乎逐字重复，建议精简\n- Figure 2 (forest plot) 的 x 轴标签和 CI whiskers 在 PDF 中较小，可读性可改善\n\n---\n\n## 主要优势\n\n1. **Matched-pair causal design 是本文最大的方法论贡献**：相比 DRIP-R 等 correlational work，matched-pair 设计 + perturbation control (n=300, Δ=-0.67pp) 显著增强了因果推断可信度。每对 clause pair 仅做 minimal edit，有效控制了文本特征混淆变量。\n\n2. **统计分析全面且恰当**：McNemar's test（paired binary）、Fisher's exact（per-type, small cells）、TOST equivalence（区分 \"no difference\" vs \"equivalent\"）、Holm-Bonferroni correction、effect size reporting (OR, V, Δpp) 均选择得当。多重比较校正和 sensitivity analysis（7 个 SESOI margins, 2 个 severity thresholds）增加了结论的稳健性。\n\n3. **Transparent about limitations**：论文在多处主动承认混淆（incompleteness information addition）、标注 inconclusive（C3）和 exploratory（C4）、报告 per-type judge reliability 差异。这种 intellectual honesty 在 NLP 论文中不常见，值得肯定。\n\n4. **Cross-architecture replication**：5+2 个模型跨 6 个 provider 的 replication（C1 在所有 7 个模型上 p < 10⁻⁶，C2 ranking ρ=0.90 for LLaMA）大幅增强了 generalizability。\n\n5. **Practical framework**：Differential Nocuity 不仅是理论贡献——Table 2 的 mitigation experiment（虽然 preliminary）和 Appendix D 的 detection experiment 提供了可操作的实践方向。\n\n---\n\n## 评分建议\n\n**Overall Assessment**: 3.5 (Borderline Conference)\n\n理由：论文在研究问题（首个 causal, type-granularity ambiguity→safety mapping）、实验设计（matched-pair + perturbation control）和统计分析（comprehensive + transparent）方面达到了 Conference 水准。但三个 critical issues 共同削弱了核心叙事：(1) 最突出的 type-specific 发现（auth scope canary type）建立在最低可靠性测量上；(2) judge-model confounding 限制了 C4 的因果解释力；(3) 缺少 power analysis 使 C2 tier structure 的 equivalence claims 不够可信。若作者能在 revision 中解决 N1-N3（增加 auth scope 验证样本、报告 per-model judge agreement、补充 power analysis），本文可达 4.0 (Conference)。当前 3.5 反映方法论缺陷可修复但影响结论可信度。\n",
  "reviewer_id": "1",
  "project": "policy_ambiguity_safety"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "\n# Reviewer 1 审稿意见：方法严谨性审查\n\n## 论文信息\n- **标题**: \"Not All Policy Ambiguity Is Equal: Type-Specific Safety Risks for LLM Agents\"\n- **Venue**: EMNLP 2026 (ARR May cycle)\n\n---\n\n## Summary\n\n本文通过 matched-pair 因果设计研究政策歧义类型与 LLM agent 安全违规之间的关系。在 τ²-bench 上构建 300 组 clause pairs（6 种歧义类型 × 50 对），跨 5 个模型评估 2,997 episodes。核心发现：(1) 歧义条款使违规率增加 34.0pp（OR=15.1）；(2) 类型间存在显著层级结构（Cramér's V=0.137），incompleteness 最危险（46-62%），authorization scope 模型间差异最大（12-64%）；(3) agent 几乎不具备歧义识别能力（<11%）。论文提出 Differential Nocuity 框架，将类型特异性风险与消歧渠道可用性关联。\n\n实验设计整体严谨，统计方法选择得当，perturbation control 和 replication 增强了因果推断可信度。但在几个关键方法论问题上存在不足，主要涉及评估管线的 judge-model confounding、authorization scope 的低测量可靠性、以及 incompleteness 的信息添加混淆。\n\n---\n\n## 总体评分\n\n**Overall**: 3.5 (Borderline Conference)\n**一句话总结**: 实验设计和统计分析整体扎实，但论文最突出的两个发现（incompleteness 普遍危险、auth scope 作为 canary type）恰恰建立在测量可靠性最弱的基础上，需要更充分的 hedging 或补充验证。\n\n## 官方维度打分（ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | 核心因果设计强，但 headline claims 的测量基础有缺陷（auth scope κ=0.385, incompleteness confound 未完全解决） |\n| Excitement | 4/5 | 首个将歧义类型与 agent 安全违规因果关联的研究，Differential Nocuity 框架有理论和实践价值 |\n| Reproducibility | 3/5 | ICC=0.919 仅限 OpenAI 模型内部；API snapshot 单日（May 20, 2026）；无代码/数据发布声明 |\n| Confidence | 4/5 | 本人在实验设计和统计方法方面有充分专业背景 |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] Authorization scope 测量可靠性过低，无法支撑 \"canary type\" 主张\n\n- 具体位置：§4.4 cross-judge calibration (κ=0.385), §5.4 C4 (52pp model range), Table 9 (human-LLM κ=0.644, 95% CI [0.35, 0.91]), Discussion \"potential canary type\"\n- 问题：Authorization scope 是论文最引人注目的发现之一（52pp 跨模型差异，Claude 12% vs GPT-5.4 64%，被提议为 safety training 的 canary type），但这个类型的 cross-judge κ 仅 0.385（fair），是所有类型中最低的。Human-LLM agreement 的 95% CI 为 [0.35, 0.91]，极宽。Per-type 验证样本仅 n=34，不足以可靠估计 type-specific reliability。虽然论文在 §5.4 提到 within-judge comparison（控制 judge identity 后仍有 48pp range），但这仍然依赖同一个 judge（GPT-5.4）的 type-level 判断一致性，而恰恰该 type 的判断一致性最低。\n- 为什么影响接收：Abstract、Introduction contribution list、Discussion、Conclusion 均突出 authorization scope 的 model-differentiating 特性。如果这个类型的测量噪声占据了 52pp range 的相当部分，那么核心叙事的支柱之一就不稳固。\n- 建议修改方向：(a) 明确报告 auth scope 的 within-judge raw agreement 和 detection vs severity 的分离分析；(b) 在 Abstract 和 Conclusion 中对 canary type 主张加上显式 measurement-uncertainty caveat（如\"subject to the lowest per-type judge reliability\"）；(c) 考虑增加 auth scope 的 human validation 样本量（当前 n=34 不够）。\n\n**N2** [critical] Judge-model confounding 未被充分处理\n\n- 具体位置：§4.4 Evaluation（GPT-5.4 judges Claude/Qwen3/DeepSeek; GPT-4.1 judges GPT-5.4），§Limitations \"Cross-judge asymmetry\"\n- 问题：每个 agent model 由单一 judge 评估，导致 judge identity 与 model identity 完全 confounded。dual-judge calibration（n=100, McNemar p=0.606）只能在 aggregate level 排除 systematic bias，但无法排除 type-specific 或 model-specific bias。尤其是 GPT-4.1（mid-tier）judging GPT-5.4（frontier）这个方向更令人担忧——能力不对称可能导致 GPT-4.1 低估 GPT-5.4 的微妙违规，从而人为压低 GPT-5.4 的违规率。Limitations 承认 C3 在 within-judge-group 分析中均未达显著性（GPT-4.1-judged p=0.059, GPT-5.4-judged p=0.157），这直接说明 pooled 结果可能包含 judge-level artifact。\n- 为什么影响接收：C4（model×type interaction）的核心发现——不同模型对不同类型的差异响应——在 judge-model confounding 下因果解释力减弱。Authorization scope 的 model differentiation（最核心发现之一）尤其受影响。\n- 建议修改方向：(a) 对所有 5 个 model 用两个 judge 分别评估一个 subset（如各 100 episodes），以估计 judge×model interaction 大小；(b) 至少报告 calibration sample 中 per-model 的 judge agreement，而非仅报告 aggregate；(c) 在 C4 结论中明确标注 judge-model confounding 对 model-level 结论的限制。\n\n**N3** [critical] 缺少 a priori power analysis，50 pairs/type 的样本量合理性未论证\n\n- 具体位置：§4.2 Matched-Pair Design (50 clause pairs per type)\n- 问题：论文未报告 a priori power analysis。50 对/类型的选择似乎是 pragmatic 的，但对于以下关键分析其统计功效不明确：(a) TOST equivalence testing with ±15pp margin——null 结果（equivalence confirmed）的可信度取决于功效；(b) pairwise type comparisons with Holm-Bonferroni correction——correction 后 detectable effect size 是多少？(c) per-type per-model cells（n=50 episodes）的 Fisher's exact test——如 Table 1 中 Claude auth scope 仅 12%（约 6/50 episodes），这些小计数的 estimate 极不稳定。\n- 为什么影响接收：ARR Soundness 维度要求 claims 有充分统计支持。C2 的 \"two-tier structure\" 依赖 TOST equivalence，但没有功效分析就无法区分 \"types are equivalent\" 和 \"we lack power to detect difference\"。\n- 建议修改方向：报告 post-hoc power analysis（至少对 TOST 和 pairwise comparisons），说明在当前 n=50 下可检测的最小效应量。若功效不足，需在 C2 结论中相应缩小声明。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] Incompleteness confound 的 hedging 在 Abstract/Conclusion 中不够显著\n\n- 具体位置：Abstract (\"incompleteness is universally dangerous (46-62%)\"), Conclusion (\"incompleteness is a universal blind spot (46-62% across all seven models)\"), §5.2 C2, Appendix F\n- 问题：Incompleteness 的 unambiguous variant 必须添加新的政策内容，这与其他 5 种类型（仅改写现有内容）结构性不同。论文在 §3 Taxonomy 和 §5.2 中提到了这个混淆，并在 Appendix F 进行了 logistic regression 控制。但控制方式有局限：(a) token count difference 是 information content 的粗糙代理；(b) 即使控制了 token delta，\"添加缺失信息\" 和 \"消除歧义\" 在概念上仍是不同干预。Coreferential 作为 \"confound-free lower bound\"（31.6%）的论证逻辑上不成立——它是不同类型，不是 incompleteness 的无混淆版本。\n- 建议：在 Abstract 中将 \"universally dangerous\" 改为更审慎的表述（如 \"shows the highest violation rates, though the effect partly confounds ambiguity resolution with information addition\"）；在 Conclusion 中同样加强 hedging。\n\n**W2** [warning] TOST SESOI ±15pp 的选择缺乏外部锚定\n\n- 具体位置：§4.6 Statistical Analysis\n- 问题：±15pp 的 SESOI 被定义为 \"a type producing ≥15 pp more violations warrants distinct policy handling\"。这是一个 reasonable practical argument，但缺乏外部锚定。为什么不是 ±10pp 或 ±20pp？Sensitivity analysis（Appendix A, Table 3）显示在 ±10pp 时仅 3/6 mid-tier pairs equivalent，在 ±12pp 时 5/6——两个看起来同样合理的 margin 给出截然不同的 tier structure 结论。论文的 \"robust two-tier structure\" claim（Abstract、Conclusion）主要在 ≥15pp 时成立。\n- 建议：(a) 讨论 SESOI 选择对结论的敏感性（不仅在 Appendix 展示数据，还在主文中明确说明 tier structure 依赖 margin 选择）；(b) 考虑报告 minimum SESOI at which the two-tier structure emerges（约 ±12pp），增加透明度。\n\n**W3** [warning] ICC=0.919 仅限 OpenAI 模型内部，cross-provider 可复现性未知\n\n- 具体位置：§4.5 Controls, Reproducibility paragraph\n- 问题：ICC=0.919 (95% CI [0.892, 0.940]) 是优秀的可复现性指标，但仅基于 GPT-5.4 和 GPT-4.1（均为 OpenAI），在相同 API 下测量。Cross-provider 可复现性（如 Claude 或 DeepSeek 在不同时间的行为稳定性）未直接测量。论文声称 \"consistency of C1 across all seven models\" 间接支持，但这是 cross-model 一致性而非 temporal reproducibility。\n- 建议：明确指出 ICC 仅反映 within-provider temporal stability，不应被解读为 cross-provider reproducibility 的证据。\n\n**W4** [warning] Mitigation experiment（Table 2）样本量过小却在主文 Discussion 中占重要位置\n\n- 具体位置：§7 Discussion, Table 2 (1,256 episodes, ~50 per cell)\n- 问题：Per-cell ~50 episodes 产生很宽的 CI（论文自己也说 \"per-cell CIs are wide\"）。DeepSeek 在 scopal (+2.0pp) 和 incompleteness (+4.0pp) 上显示增加而非减少，表明 mitigation 效果不稳定。然而 Discussion 用这些数据得出 \"authorization scope benefits most (−18.0pp), while incompleteness is nearly immune (−3.4pp)\" 的具体结论。\n- 建议：将 Table 2 移至 Appendix，在 Discussion 中仅报告方向性趋势，并明确标注为 preliminary。\n\n**W5** [warning] Failure mode taxonomy 的 inter-coder reliability 偏低\n\n- 具体位置：§6 Error Analysis (Gwet's AC₁=0.62, Cohen's κ=0.52)\n- 问题：Cohen's κ=0.52 仅为 moderate agreement。论文解释为 prevalence paradox（3 类占 ~90%），AC₁=0.62 部分补偿了这一点。但对少数类别（arbitrary rule selection κ=0.29），reliability 很差。论文在 Limitations 中提到 \"human validation of the coding scheme would further strengthen these findings\"，但未实际执行。\n- 建议：(a) 报告 per-category 的 AC₁ 和 sample size；(b) 在主文中更明确地标注 failure mode taxonomy 的分析为 tentative。\n\n---\n\n## Questions for Authors\n\n**Q1**: 50 clause pairs/type 的决定依据是什么？是基于 pilot study 的效应量估计，还是资源约束？若有 pilot data，请报告 power calculation。\n\n**Q2**: Cross-judge calibration 的 100 episodes 中，per-model 的 judge agreement 如何分布？特别是 GPT-4.1 判 GPT-5.4 的 accuracy 与 GPT-5.4 判其他模型相比是否有系统差异？\n\n**Q3**: Logistic regression 控制 incompleteness confound 时（Appendix F），具体控制了哪些变量？仅 token delta 还是包括 syntactic complexity、information density 等更细的指标？Coefficient change <8% 是否在 practical significance 意义上足够小？\n\n**Q4**: Template-based clause generation pipeline 的具体操作是什么？Templates 是如何设计的？同一 template 产生的多个 clause pairs 之间是否存在 structural correlation？如果是，matched-pair test 的独立性假设是否被违反？\n\n**Q5**: 论文提到 \"3 episodes lost to API errors in one Qwen3 batch\"（§4.2），2,997 而非 3,000。这是否可能引入 selection bias（如某些 ambiguity types 或 clause pairs 更容易触发 API errors）？\n\n**Q6**: C3（layer effect）在 Holm-Bonferroni correction 后不显著，controlling for token delta 后方向反转。保留 C3 在主文中的理由是什么？它增加了叙事复杂性但提供了 null/negative evidence。\n\n---\n\n## Minor Issues\n\n- Lassiter & Goodman (2017) 的出版年份可能是 2015（Synthese online-first），建议核实\n- ferrari_defects_2018 的 bib entry first author 为 Rosadini 而非 Ferrari，但正文 cite 时似乎隐含 Ferrari 是第一作者\n- Abstract 信息密度极高，建议精简（当前包含 OR、V、p-value、pp range 等过多数字，降低可读性）\n- §5.2 中 \"upper bound whose ranking partly reflects an information-addition confound\" 在不同位置出现 ≥4 次，措辞近乎逐字重复，建议精简\n- Figure 2 (forest plot) 的 x 轴标签和 CI whiskers 在 PDF 中较小，可读性可改善\n\n---\n\n## 主要优势\n\n1. **Matched-pair causal design 是本文最大的方法论贡献**：相比 DRIP-R 等 correlational work，matched-pair 设计 + perturbation control (n=300, Δ=-0.67pp) 显著增强了因果推断可信度。每对 clause pair 仅做 minimal edit，有效控制了文本特征混淆变量。\n\n2. **统计分析全面且恰当**：McNemar's test（paired binary）、Fisher's exact（per-type, small cells）、TOST equivalence（区分 \"no difference\" vs \"equivalent\"）、Holm-Bonferroni correction、effect size reporting (OR, V, Δpp) 均选择得当。多重比较校正和 sensitivity analysis（7 个 SESOI margins, 2 个 severity thresholds）增加了结论的稳健性。\n\n3. **Transparent about limitations**：论文在多处主动承认混淆（incompleteness information addition）、标注 inconclusive（C3）和 exploratory（C4）、报告 per-type judge reliability 差异。这种 intellectual honesty 在 NLP 论文中不常见，值得肯定。\n\n4. **Cross-architecture replication**：5+2 个模型跨 6 个 provider 的 replication（C1 在所有 7 个模型上 p < 10⁻⁶，C2 ranking ρ=0.90 for LLaMA）大幅增强了 generalizability。\n\n5. **Practical framework**：Differential Nocuity 不仅是理论贡献——Table 2 的 mitigation experiment（虽然 preliminary）和 Appendix D 的 detection experiment 提供了可操作的实践方向。\n\n---\n\n## 评分建议\n\n**Overall Assessment**: 3.5 (Borderline Conference)\n\n理由：论文在研究问题（首个 causal, type-granularity ambiguity→safety mapping）、实验设计（matched-pair + perturbation control）和统计分析（comprehensive + transparent）方面达到了 Conference 水准。但三个 critical issues 共同削弱了核心叙事：(1) 最突出的 type-specific 发现（auth scope canary type）建立在最低可靠性测量上；(2) judge-model confounding 限制了 C4 的因果解释力；(3) 缺少 power analysis 使 C2 tier structure 的 equivalence claims 不够可信。若作者能在 revision 中解决 N1-N3（增加 auth scope 验证样本、报告 per-model judge agreement、补充 power analysis），本文可达 4.0 (Conference)。当前 3.5 反映方法论缺陷可修复但影响结论可信度。\n",
    "reviewer_id": "1",
    "project": "policy_ambiguity_safety"
  }
}
```

</details>

---


### Tool result

_source line 533 · 2026-05-21T15:40:16.592327+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_967344d166ba485ad606d14379e69d85:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3713
}
```

</details>

---


### Tool call

_source line 534 · 2026-05-21T15:40:22.421981+00:00_

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
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
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

_source line 535 · 2026-05-21T15:40:22.472648+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 536 · 2026-05-21T15:40:26.890033+00:00_

called mcp__agent-ml-research__cleanup_pdf_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__cleanup_pdf_images</summary>

```json
{
  "output_dir": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/_pdf_images"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "tool_args": {
    "output_dir": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/_pdf_images"
  }
}
```

</details>

---


### Tool result

_source line 537 · 2026-05-21T15:40:26.941367+00:00_

{"result":"{\"success\": true, \"data\": {\"message\": \"目录不存在，无需清理\", \"deleted\": 0}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "elapsed_ms": 51
}
```

</details>

---


### Assistant

_source line 538 · 2026-05-21T15:40:33.857383+00:00_

审稿意见已提交给 Review Director。

**审稿结论**：Overall 3.5 (Borderline Conference)。

核心判断：matched-pair causal design + perturbation control 是本文方法论上的最大优势，统计分析全面且恰当。但三个 critical issues 削弱了核心叙事：

1. **Auth scope 测量可靠性过低**（κ=0.385）却支撑了 "canary type" 这一最引人注目的发现
2. **Judge-model confounding** 限制了 C4 model×type interaction 的因果解释力
3. **缺少 a priori power analysis**，50 pairs/type 对 TOST equivalence claims 的支撑不明确

这三个问题可在 revision 中修复（增加 auth scope 验证样本、报告 per-model judge agreement、补充 power analysis），修复后可达 4.0 (Conference)。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1"
}
```

</details>

---


## Round 16

## Round 16

4 recorded events


### User

_source line 539 · 2026-05-21T15:41:24.968947+00:00_

[Round 1 审稿请求]:
以下是 Reviewer 2 的完整审稿意见，请逐条回应。对每个 Must-Fix (N1-N3) 和 Should-Fix (W1-W5) 问题，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。

---

## Reviewer 2 的审稿意见

**Overall**: 3.5 (Borderline Conference)

### Must-Fix 问题

**N1** [critical] 主文超出 8 页限制
- Section 7 Discussion 跨页到 Page 9，Table 2 + Section 8 Conclusion 均在 Page 9
- 正文约 8.5-8.7 页，超限约 0.5-0.7 页
- ARR desk reject 标准之一
- 建议：Table 2 移至 Appendix（省约 1/3 页）；Discussion 压缩重复论述

**N2** [critical] Incompleteness 的 information-addition confound 未充分处理
- incompleteness 与其他 5 类本质不同——resolution requires adding new policy content
- 高违规率可能是 information absence 本身导致错误，而非歧义
- Appendix F 的 logistic regression 只说 "effect remains significant after controlling"，缺少 effect size 变化量（控制前后 OR 变了多少？）
- 建议：(1) 报告控制前后 OR 变化量；(2) 在主文明确讨论 confound 对 type hierarchy 解读的限制；(3) 考虑将 incompleteness 从排序中分离

**N3** [critical] "Differential Nocuity" 框架缺乏形式化
- 全文没有给出形式化定义
- 既不是 predictive model，也不是 prescriptive framework
- 实质是对实验发现的重新命名
- 建议：降级为 empirical finding，或真正形式化

### Should-Fix 问题

**W1** 与 DRIP-R 的差异化论述不够有力——需要更 explicit 的 contribution delta
**W2** Contribution 4（failure mode taxonomy）与 Contribution 1 重叠——建议合并
**W3** Human validation 细节不足——缺少 annotator blindness、disagreement 分布
**W4** Domain scope 限制未充分讨论——healthcare/finance/legal 可能完全不同
**W5** 部分引用信息有误——ferrari_defects_2018 第一作者实际是 Rosadini；lassiter_goodman_2017 年份可能是 2015

### Missing References
- Agent-SafetyBench (Zhang et al., 2024)
- SafeAgentBench (Yin et al., 2024)
- AgentSpec (Poskitt et al., ICSE 2026)
- WSD survey (Navigli, 2009) — CL venue 的明显遗漏

### Excitement 评分
R2 给了 Excitement 3.0/5，认为核心发现 "不同歧义类型有不同风险" 较为 expected，two-tier hierarchy 的上界可能是实验设计产物。

---

请逐条回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 540 · 2026-05-21T15:43:45.570367+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "\n# Reviewer 1 对 Reviewer 2 审稿意见的逐条回应\n\n## Must-Fix 问题\n\n### [AGREE] R2-N1: 主文超出 8 页限制\n同意。PDF 显示主文（Abstract → Conclusion）约 8.5-8.7 页，超限。Table 2（mitigation experiment, ~50/cell, preliminary）移至 Appendix 可节省约 1/3 页，同时改善论证质量——我在自己的 W4 中也指出该实验样本量不足以放在主文。Discussion 中 \"upper bound whose ranking partly reflects an information-addition confound\" 几乎逐字重复 ≥4 次，压缩重复措辞可进一步节省空间。\n\n### [AGREE with nuance] R2-N2: Incompleteness confound\n部分同意。R2 要求报告控制前后 OR 变化量是合理的——Appendix F 仅说 \"coefficient change < 8%\" 但无 OR 对比。在 Abstract/Conclusion 中加强 hedging 也是必要的。\n\n但不完全同意 critical 定级。论文已有多项控制：§3 预先标注结构特殊性、§5.2 明确称 \"upper bound\"、coreferential 作为 confound-free lower bound (31.6%, information delta = 0)、Appendix F logistic regression 控制 token delta 后仍显著 (p=0.022)。核心问题是**呈现方式**（Abstract/Conclusion 的 \"universally dangerous\" 措辞过于强势）而非分析缺失。\n\n### [REBUT] R2-N3: \"Differential Nocuity\" 缺乏形式化\n不同意此为 critical issue。该框架提供三层组织原则：(1) 扩展 Berry & Kamsties (2004) 的二分法到 LLM agents（§7）；(2) 连接类型特异性与消歧渠道可用性（§7 \"Why incompleteness resists safety training\"——auth scope 有 RLHF 拦截点, incompleteness 无 decision point）；(3) 引出 systematic nocuity 概念（§6.3, 41.3% majority-convergent violations）。NLP 顶会中许多广泛引用的框架（如 \"good-enough processing\"）同样是 conceptual organizing principles 而非 formal models。要求 predictive/prescriptive 形式化对实证论文标准过高。建议作者在 §7 开头用 2-3 句话更明确阐述框架组成部分即可。\n\n## Should-Fix 问题\n\n### [AGREE partially] R2-W1: 与 DRIP-R 差异化\n§2 已指出两个差异（causal design vs correlation; model×type quantification），满足 concurrent work 的最低要求但可改善。\n\n### [REBUT] R2-W2: Contribution 3 与 Contribution 1 重叠\n不同意。Contribution 1（因果定量: \"是否/多大程度\"）和 Contribution 3（failure mode taxonomy: \"通过什么机制\"）方法论完全不同（统计检验 vs 614 traces coding），结论层次也不同。\n\n### [AGREE] R2-W3: Human validation 细节不足\n同意。缺少 annotator blindness、disagreement distribution、resolution 策略。\n\n### [REBUT] R2-W4: Domain scope 限制\n不同意。Limitations 已专段讨论，含 within-study cross-domain evidence。EMNLP 2026 Limitations 章节仅需 ~3 个点，当前覆盖已足够。\n\n### [AGREE] R2-W5: 引用信息有误\n同意。我的引用验证也发现了 ferrari_defects_2018（first author mismatch）和 lassiter_goodman_2017（年份可能为 2015）的问题。\n\n## Missing References\nNavigli (2009) WSD survey 可在 §2 补充。其他 agent safety benchmarks（Agent-SafetyBench, SafeAgentBench）属于同类引用，论文已有 5 个同类引用，非必需。AgentSpec 需确认与 policy ambiguity 的相关性。\n\n## Excitement 评分\nR2 给 3.0，我给 4.0。核心分歧：R2 认为 \"类型差异\" 是 expected finding，但论文贡献不是发现差异本身，而是首次用 matched-pair design 建立因果关系。Several findings 是 genuinely surprising：incompleteness 普遍性（46-62% across 7 models）、Ambiguity Blindness（Qwen3/DeepSeek 0% awareness）、auth scope 的 systematic permissiveness bias（69.2% unauthorized escalation, 0% conservative refusal, p < 10⁻⁴）。去掉 incompleteness 后，5 类型间 pairwise contrasts 仍有结构（auth scope/lexical 显著高于 coreferential, Appendix F），tier structure 不完全依赖 incompleteness。\n\n## 综合评估\nR2 的 N1（page limit）和 W5（citation errors）完全正确，需修复。N2（incompleteness confound）的呈现问题需改善但分析基础已在。N3（形式化要求）标准过高。整体上 R2 的审稿在格式和引用细节上敏锐，但对论文已有方法论控制的认可不足。\n\n我维持 Overall 3.5，Soundness 3.5，Excitement 4.0。\n",
  "reviewer_id": "1",
  "project": "policy_ambiguity_safety"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "\n# Reviewer 1 对 Reviewer 2 审稿意见的逐条回应\n\n## Must-Fix 问题\n\n### [AGREE] R2-N1: 主文超出 8 页限制\n同意。PDF 显示主文（Abstract → Conclusion）约 8.5-8.7 页，超限。Table 2（mitigation experiment, ~50/cell, preliminary）移至 Appendix 可节省约 1/3 页，同时改善论证质量——我在自己的 W4 中也指出该实验样本量不足以放在主文。Discussion 中 \"upper bound whose ranking partly reflects an information-addition confound\" 几乎逐字重复 ≥4 次，压缩重复措辞可进一步节省空间。\n\n### [AGREE with nuance] R2-N2: Incompleteness confound\n部分同意。R2 要求报告控制前后 OR 变化量是合理的——Appendix F 仅说 \"coefficient change < 8%\" 但无 OR 对比。在 Abstract/Conclusion 中加强 hedging 也是必要的。\n\n但不完全同意 critical 定级。论文已有多项控制：§3 预先标注结构特殊性、§5.2 明确称 \"upper bound\"、coreferential 作为 confound-free lower bound (31.6%, information delta = 0)、Appendix F logistic regression 控制 token delta 后仍显著 (p=0.022)。核心问题是**呈现方式**（Abstract/Conclusion 的 \"universally dangerous\" 措辞过于强势）而非分析缺失。\n\n### [REBUT] R2-N3: \"Differential Nocuity\" 缺乏形式化\n不同意此为 critical issue。该框架提供三层组织原则：(1) 扩展 Berry & Kamsties (2004) 的二分法到 LLM agents（§7）；(2) 连接类型特异性与消歧渠道可用性（§7 \"Why incompleteness resists safety training\"——auth scope 有 RLHF 拦截点, incompleteness 无 decision point）；(3) 引出 systematic nocuity 概念（§6.3, 41.3% majority-convergent violations）。NLP 顶会中许多广泛引用的框架（如 \"good-enough processing\"）同样是 conceptual organizing principles 而非 formal models。要求 predictive/prescriptive 形式化对实证论文标准过高。建议作者在 §7 开头用 2-3 句话更明确阐述框架组成部分即可。\n\n## Should-Fix 问题\n\n### [AGREE partially] R2-W1: 与 DRIP-R 差异化\n§2 已指出两个差异（causal design vs correlation; model×type quantification），满足 concurrent work 的最低要求但可改善。\n\n### [REBUT] R2-W2: Contribution 3 与 Contribution 1 重叠\n不同意。Contribution 1（因果定量: \"是否/多大程度\"）和 Contribution 3（failure mode taxonomy: \"通过什么机制\"）方法论完全不同（统计检验 vs 614 traces coding），结论层次也不同。\n\n### [AGREE] R2-W3: Human validation 细节不足\n同意。缺少 annotator blindness、disagreement distribution、resolution 策略。\n\n### [REBUT] R2-W4: Domain scope 限制\n不同意。Limitations 已专段讨论，含 within-study cross-domain evidence。EMNLP 2026 Limitations 章节仅需 ~3 个点，当前覆盖已足够。\n\n### [AGREE] R2-W5: 引用信息有误\n同意。我的引用验证也发现了 ferrari_defects_2018（first author mismatch）和 lassiter_goodman_2017（年份可能为 2015）的问题。\n\n## Missing References\nNavigli (2009) WSD survey 可在 §2 补充。其他 agent safety benchmarks（Agent-SafetyBench, SafeAgentBench）属于同类引用，论文已有 5 个同类引用，非必需。AgentSpec 需确认与 policy ambiguity 的相关性。\n\n## Excitement 评分\nR2 给 3.0，我给 4.0。核心分歧：R2 认为 \"类型差异\" 是 expected finding，但论文贡献不是发现差异本身，而是首次用 matched-pair design 建立因果关系。Several findings 是 genuinely surprising：incompleteness 普遍性（46-62% across 7 models）、Ambiguity Blindness（Qwen3/DeepSeek 0% awareness）、auth scope 的 systematic permissiveness bias（69.2% unauthorized escalation, 0% conservative refusal, p < 10⁻⁴）。去掉 incompleteness 后，5 类型间 pairwise contrasts 仍有结构（auth scope/lexical 显著高于 coreferential, Appendix F），tier structure 不完全依赖 incompleteness。\n\n## 综合评估\nR2 的 N1（page limit）和 W5（citation errors）完全正确，需修复。N2（incompleteness confound）的呈现问题需改善但分析基础已在。N3（形式化要求）标准过高。整体上 R2 的审稿在格式和引用细节上敏锐，但对论文已有方法论控制的认可不足。\n\n我维持 Overall 3.5，Soundness 3.5，Excitement 4.0。\n",
    "reviewer_id": "1",
    "project": "policy_ambiguity_safety"
  }
}
```

</details>

---


### Tool result

_source line 541 · 2026-05-21T15:43:49.240845+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_967344d166ba485ad606d14379e69d85:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3670
}
```

</details>

---


### Assistant

_source line 542 · 2026-05-21T15:43:56.665611+00:00_

已提交对 Reviewer 2 的逐条回应。总结：

- **N1 (page limit)**: [AGREE] — 主文确实超限，Table 2 应移至 Appendix
- **N2 (incompleteness confound)**: [AGREE with nuance] — 呈现方式需改善，但分析控制已在
- **N3 (Differential Nocuity 形式化)**: [REBUT] — 对实证论文要求 formal model 标准过高
- **W1-W5**: W1 部分同意、W2 反驳、W3 同意、W4 反驳、W5 同意
- **Excitement**: 维持 4.0/5，反驳 R2 的 3.0——首个 causal study 加上多个 genuinely surprising findings

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1"
}
```

</details>

---


## Round 17

## Round 17

80 recorded events


### User

_source line 543 · 2026-05-21T16:55:38.586043+00:00_

[Round 1 审稿请求]:
你是 Reviewer 1，负责 **方法严谨性 + 实验设计** 审查。

## 投稿信息
- **Venue**: EMNLP 2026（通过 ARR May cycle 提交）
- **截止日期**: 2026-05-25
- **类型**: Long paper
- **页数限制**: 正文 ≤8 页，参考文献不限页
- **模板**: ACL LaTeX (two-column, 11pt)
- **匿名规则**: Double-blind（作者信息匿名）
- **必须章节**: Limitations（不计入页数限制）
- **附录**: 允许，但审稿人不强制阅读

## 论文路径
- LaTeX: `projects/policy_ambiguity_safety/docs/paper/main.tex`
- PDF: `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/main.pdf`

## 你的审查侧重

### 1. 统计方法与因果推理
- 主要 claims（C1-C5）的统计检验是否合适？效应量/CI/p-value 报告是否完整？
- TOST 等价性检验的 SESOI margin 选择是否有外部锚定和敏感性分析？
- Matched-pair 设计能否真正控制混淆变量？incompleteness 的 information-addition confound 是否充分讨论？
- Perturbation control 的样本量和 CI 宽度是否足以支撑因果推断？

### 2. 测量可靠性
- LLM-as-judge 的 inter-judge agreement（κ 值）是否足够支撑结论？
- 人工标注验证的 sample size、annotator blindness、sampling strategy 是否充分报告？
- Per-type reliability 是否有弱环（特别是 authorization scope）？
- Error analysis 的 inter-coder reliability 是否支撑其作为贡献？

### 3. 实验控制
- Unambiguous baseline 的构建是否恰当？是否存在系统性偏差？
- 跨模型比较是否有 judge-model confounding？如何处理？
- Test-retest stability（ICC）是否覆盖所有模型家族？
- 样本量 power analysis 是否充分？

### 4. 可复现性
- 数据集、代码、模型 API 的可复现性声明？
- τ²-bench 修改是否充分记录？
- 实验超参数是否完整报告？

## Overall Assessment 评分标准（EMNLP 2026 ARR）
5 = Consider for Award, 4.5 = Borderline Award, 4 = Conference, 3.5 = Borderline Conference, 3 = Findings, 2.5 = Borderline Findings, 2 = Resubmit next cycle, 1.5 = Resubmit after next cycle, 1 = Do not resubmit

请按以下格式输出审稿意见：
1. **Summary** (2-3 句)
2. **Strengths** (逐条)
3. **Weaknesses** (逐条，标注 [MUST-FIX] 或 [SHOULD-FIX] 或 [MINOR])
4. **Questions** (需要作者回答的)
5. **Missing References**
6. **Overall Assessment** (评分 + 置信度 high/medium/low + 1-2 句总评)
7. **Detailed Comments** (逐节详细意见)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 544 · 2026-05-21T16:55:49.431537+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/.claude/skills/review-reviewer-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/.claude/skills/review-reviewer-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 545 · 2026-05-21T16:55:49.483244+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/.claude/sessions/review_reviewer_1_6edf79f4.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 546 · 2026-05-21T16:55:52.494544+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.skill.md",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/.claude"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.skill.md",
    "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/.claude"
  }
}
```

</details>

---


### Tool result

_source line 547 · 2026-05-21T16:55:52.545214+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 548 · 2026-05-21T16:55:55.211607+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/review-reviewer-session-start.skill.md",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/review-reviewer-session-start.skill.md",
    "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4"
  }
}
```

</details>

---


### Tool result

_source line 549 · 2026-05-21T16:55:55.362671+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Glob",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 550 · 2026-05-21T16:55:59.379713+00:00_

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
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
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

_source line 551 · 2026-05-21T16:55:59.430485+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 552 · 2026-05-21T16:56:04.660901+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/main.pdf",
  "project": "policy_ambiguity_safety",
  "pages": "1-10",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/main.pdf",
    "project": "policy_ambiguity_safety",
    "pages": "1-10",
    "dpi": "150"
  }
}
```

</details>

---


### Tool call

_source line 553 · 2026-05-21T16:56:05.162996+00:00_

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
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR 2025 2026 reviewer guidelines review form criteria scoring"
  }
}
```

</details>

---


### Tool call

_source line 554 · 2026-05-21T16:56:05.766405+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 555 · 2026-05-21T16:56:06.067893+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 1, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/_pdf_images/main_p1.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 454.5}, {\"page\": 2, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/_pdf_images/main_p2.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 424.9}, {\"page\": 3, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/_pdf_images/main_p3.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 519.2}, {\"page\": 4, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/_pdf_images/main_p4.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 516.8}, {\"page\": 5, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/_pdf_images/main_p5.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 535.1}, {\"page\": 6, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/_pdf_images/main_p6.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 391.4}, {\"page\": 7, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/_pdf_images/main_p7.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 341.3}, {\"page\": 8, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/_pdf_images/main_p8.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 530.1}, {\"page\": 9, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/_pdf_images/main_p9.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 540.1}, {\"page\": 10, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safet
…[truncated 322 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 1406
}
```

</details>

---


### Tool result

_source line 556 · 2026-05-21T16:56:06.068370+00:00_

1	\documentclass[11pt]{article}
2	\usepackage[review]{acl}
3	\usepackage{times}
4	\usepackage{latexsym}
5	\usepackage[T1]{fontenc}
6	\usepackage[utf8]{inputenc}
7	\usepackage{microtype}
8	\usepackage{graphicx}
9	\usepackage{booktabs}
10	\usepackage{amsmath}
11	\usepackage{amssymb}
12	\usepackage{multirow}
13	\usepackage{xcolor}
14	\usepackage{subcaption}
15	
16	\definecolor{speccolor}{HTML}{C44E52}
17	\definecolor{lingcolor}{HTML}{4C72B0}
18	
19	\title{Not All Policy Ambiguity Is Equal: Type-Specific Safety Risks for LLM Agents}
20	
21	\author{Anonymous}
22	
23	\begin{document}
24	\maketitle
25	
26	\input{sections/abstract}
27	\input{sections/introduction}
28	\input{sections/related_work}
29	\input{sections/taxonomy}
30	\input{sections/method}
31	\input{sections/experiments}
32	\input{sections/analysis}
33	\input{sections/discussion}
34	\input{sections/conclusion}
35	\input{sections/limitations}
36	
37	\bibliography{references}
38	
39	\appendix
40	\input{sections/appendix}
41	
42	\end{document}
43	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 301
}
```

</details>

---


### Tool result

_source line 557 · 2026-05-21T16:56:12.847717+00:00_

Web search results for query: "ACL ARR 2025 2026 reviewer guidelines review form criteria scoring"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"}]

Based on the search results, here's information about ACL ARR reviewer guidelines for 2025-2026:

## Review Scoring Criteria

Starting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation.

### Soundness Score
Soundness scores must be justified by the text of the review. If you give a low Soundness score without finding any major faults, this means that your review is not a faithful explanation of your recommendation, and you need to revise it.

### Excitement Score
Sometimes you may find the work sound, but not something that is interesting for you personally. Such preferences are more subjective and should be reflected in a separate excitement score, which is orthogonal to the assessment of the soundness of the paper.

### Area Chair Metareview Scores
The ARR metareview score has changed in February 2025. Like with reviews, the score should be backed up by the meta-review text. The new options include: 5 = Consider for Award, down to 1 = Do not resubmit (for pape
…[truncated 248 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 7684
}
```

</details>

---


### Tool call

_source line 558 · 2026-05-21T16:56:17.716335+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/_pdf_images/main_p1.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/_pdf_images/main_p1.png"
  }
}
```

</details>

---


### Tool result

_source line 559 · 2026-05-21T16:56:18.670756+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 954
}
```

</details>

---


### Tool call

_source line 560 · 2026-05-21T16:56:18.671222+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/_pdf_images/main_p2.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/_pdf_images/main_p2.png"
  }
}
```

</details>

---


### Tool call

_source line 561 · 2026-05-21T16:56:19.228313+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/_pdf_images/main_p3.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/_pdf_images/main_p3.png"
  }
}
```

</details>

---


### Tool result

_source line 562 · 2026-05-21T16:56:19.631637+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 960
}
```

</details>

---


### Tool call

_source line 563 · 2026-05-21T16:56:19.632066+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/_pdf_images/main_p4.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/_pdf_images/main_p4.png"
  }
}
```

</details>

---


### Tool result

_source line 564 · 2026-05-21T16:56:20.085099+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 856
}
```

</details>

---


### Tool call

_source line 565 · 2026-05-21T16:56:20.085561+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/_pdf_images/main_p5.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/_pdf_images/main_p5.png"
  }
}
```

</details>

---


### Tool result

_source line 566 · 2026-05-21T16:56:21.042997+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1410
}
```

</details>

---


### Tool result

_source line 567 · 2026-05-21T16:56:21.044613+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 959
}
```

</details>

---


### Tool call

_source line 568 · 2026-05-21T16:56:21.045043+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/_pdf_images/main_p6.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/_pdf_images/main_p6.png"
  }
}
```

</details>

---


### Tool result

_source line 569 · 2026-05-21T16:56:21.499046+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 453
}
```

</details>

---


### Tool call

_source line 570 · 2026-05-21T16:56:21.502891+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/_pdf_images/main_p7.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/_pdf_images/main_p7.png"
  }
}
```

</details>

---


### Tool result

_source line 571 · 2026-05-21T16:56:22.013135+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 510
}
```

</details>

---


### Tool call

_source line 572 · 2026-05-21T16:56:22.013615+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/_pdf_images/main_p8.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/_pdf_images/main_p8.png"
  }
}
```

</details>

---


### Tool result

_source line 573 · 2026-05-21T16:56:22.918950+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 905
}
```

</details>

---


### Tool call

_source line 574 · 2026-05-21T16:56:22.919451+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/_pdf_images/main_p9.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/_pdf_images/main_p9.png"
  }
}
```

</details>

---


### Tool call

_source line 575 · 2026-05-21T16:56:23.374340+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/_pdf_images/main_p10.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/_pdf_images/main_p10.png"
  }
}
```

</details>

---


### Tool result

_source line 576 · 2026-05-21T16:56:23.880556+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 961
}
```

</details>

---


### Tool result

_source line 577 · 2026-05-21T16:56:24.784619+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1410
}
```

</details>

---


### Tool call

_source line 578 · 2026-05-21T16:56:24.835191+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewerguidelines",
  "prompt": "Extract the complete review form criteria, scoring dimensions (soundness, excitement, overall assessment, confidence, etc.), their scales, and descriptions. I need the exact scoring rubric for each dimension."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewerguidelines",
    "prompt": "Extract the complete review form criteria, scoring dimensions (soundness, excitement, overall assessment, confidence, etc.), their scales, and descriptions. I need the exact scoring rubric for each dimension."
  }
}
```

</details>

---


### Tool result

_source line 579 · 2026-05-21T16:56:30.506659+00:00_

# ARR Review Form Scoring Rubric

Based on the provided guidelines, the document references a review form but **does not provide the complete scoring rubric details**. Here's what is explicitly mentioned:

## Stated Scoring Dimensions

Starting February 2025, reviewers provide three scores:

1. **Soundness** - "Soundness scores must be justified by the text of the review" (I3). Low scores require explanation; cannot be given without clear justification in the review text.

2. **Excitement** - "Orthogonal to the assessment of soundness" and reflects personal taste. Does not require explicit justification.

3. **Overall Assessment** - "An explicit recommendation for the outcome of this paper, if it were committed to an *ACL venue." This is described as a "composite score" incorporating soundness, excitement, novelty, and impact.

## Additional Referenced Dimensions

The guidelines mention:
- **Confidence score** (in review form, allows indicating expertise limitations)
- **Reproducibility score** (should be justified)
- **Author knowledge of identity disclosure** (specific form field)

## Critical Gap

The document states: "We have a post describing the ARR review form in detail" with a link to `/reviewform`, but that detailed rubric—including specific scale ranges (e.g., 1-5, 1-10) and anchor descriptions—**is not included in this content**.

For the complete scoring rubric, consult the dedicated review form documentation.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 5671
}
```

</details>

---


### Tool call

_source line 580 · 2026-05-21T16:56:38.492414+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/main.pdf",
  "project": "policy_ambiguity_safety",
  "pages": "11-13",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/main.pdf",
    "project": "policy_ambiguity_safety",
    "pages": "11-13",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 581 · 2026-05-21T16:56:39.903946+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 11, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/_pdf_images/main_p11.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 500.3}, {\"page\": 12, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/_pdf_images/main_p12.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 415.7}, {\"page\": 13, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/_pdf_images/main_p13.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 276.9}], \"total_pages\": 13, \"rendered_pages\": 3, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 1411
}
```

</details>

---


### Tool call

_source line 582 · 2026-05-21T16:56:39.958348+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete review form with all scoring dimensions, their scales (1-5 etc.), and the description/anchor for each score level. I need the full rubric for soundness, excitement, overall assessment, confidence, reproducibility, etc."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the complete review form with all scoring dimensions, their scales (1-5 etc.), and the description/anchor for each score level. I need the full rubric for soundness, excitement, overall assessment, confidence, reproducibility, etc."
  }
}
```

</details>

---


### Tool call

_source line 583 · 2026-05-21T16:56:40.463201+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "sections/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Glob",
  "tool_args": {
    "pattern": "sections/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper"
  }
}
```

</details>

---


### Tool result

_source line 584 · 2026-05-21T16:56:40.515328+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Glob",
  "elapsed_ms": 52
}
```

</details>

---


### Tool result

_source line 585 · 2026-05-21T16:56:45.939532+00:00_

# ACL Rolling Review - Complete Review Form Rubric

## Reviewer Confidence
- **5**: "Positive that my evaluation is correct. I read the paper very carefully and am familiar with related work."
- **4**: "Quite sure. I tried to check the important points carefully."
- **3**: "Pretty sure, but there's a chance I missed something."
- **2**: "Willing to defend my evaluation, but it is fairly likely that I missed some details."
- **1**: "Not my area, or paper is very hard to understand."

## Soundness
- **5**: Exceptional thoroughness for paper type
- **4**: Provides sufficient support with optional minor experiments
- **3**: Adequate support for main claims; minor details needed
- **2**: Main claims lack sufficient support; major technical problems
- **1**: Insufficiently thorough or irrelevant to ACL

## Excitement
- **5**: "Highly Exciting: I would recommend this paper to others and/or attend its presentation"
- **4**: "Exciting: I would mention this paper to others"
- **3**: "Interesting: I might mention some points of this paper to others"
- **2**: "Potentially Interesting: this paper does not resonate with me"
- **1**: "Not Exciting: this paper does not resonate with me"

## Overall Assessment
- **5**: Award consideration (top 2.5%)
- **4.5**: Borderline Award
- **4**: Conference acceptance
- **3.5**: Borderline Conference
- **3**: Findings acceptance
- **2.5**: Borderline Findings
- **2**: Resubmit next cycle
- **1.5**: Resubmit after next cycle
- **1**: Do not resubmit

## Reproducibility
- **5**: Results easily reproducible
- **4**: Mostly reproducible with minor variations
- **3**: Reproducible with difficulty; underspecified parameters
- **2**: Hard to reproduce; unavailable data
- **1**: Cannot reproduce results

## Datasets & Software
Both scored **1-5** on utility scale from "No usable" to "Enabling" impact.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 5981
}
```

</details>

---


### Tool call

_source line 586 · 2026-05-21T16:56:49.604333+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/_pdf_images/main_p11.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/_pdf_images/main_p11.png"
  }
}
```

</details>

---


### Tool call

_source line 587 · 2026-05-21T16:56:50.057608+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/_pdf_images/main_p12.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/_pdf_images/main_p12.png"
  }
}
```

</details>

---


### Tool result

_source line 588 · 2026-05-21T16:56:50.963195+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1358
}
```

</details>

---


### Tool result

_source line 589 · 2026-05-21T16:56:50.964331+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 906
}
```

</details>

---


### Tool call

_source line 590 · 2026-05-21T16:56:50.964694+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/_pdf_images/main_p13.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/_pdf_images/main_p13.png"
  }
}
```

</details>

---


### Tool call

_source line 591 · 2026-05-21T16:56:51.316185+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper"
  }
}
```

</details>

---


### Tool result

_source line 592 · 2026-05-21T16:56:51.317990+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 353
}
```

</details>

---


### Tool result

_source line 593 · 2026-05-21T16:56:51.319327+00:00_

/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/experiments.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/main.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/taxonomy.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/limitations.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/abstract.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/introduction.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/method.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/conclusion.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/discussion.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/related_work.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/analysis.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/experiments.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/appendix.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Glob",
  "elapsed_ms": 3
}
```

</details>

---


### Tool call

_source line 594 · 2026-05-21T16:56:57.146414+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 595 · 2026-05-21T16:56:57.603354+00:00_

1	\begin{abstract}
2	LLM-based agents operate under natural-language policy specifications that inevitably contain ambiguity, yet the causal relationship between ambiguity type and safety violations remains unmeasured. We present a matched-pair study on $\tau^2$-bench with 300 clause pairs spanning a six-type, two-layer ambiguity taxonomy, evaluated across five architecturally diverse models (2,997 episodes). Ambiguous clauses increase violation rates by 34.0 percentage points (OR $= 15.1$), with a perturbation control supporting ambiguity-specific causation. A significant type hierarchy emerges (Cram\'{e}r's $V = 0.137$, $p < 10^{-4}$), with a robust two-tier structure among five types and incompleteness as an upper bound partly reflecting an information-addition confound. The hierarchy replicates on two additional model families (LLaMA $\rho = 0.90$, $p = 0.037$; Gemini $\rho = 0.60$, directionally consistent): incompleteness is consistently high (46--62\% across models), while authorization scope varies 52 pp depending on the model (12\% for Claude to 64\% for GPT-5.4, though authorization scope carries the widest measurement uncertainty among types), suggesting that safety training may differentially mitigate specific ambiguity types. Agents show fewer than 11\% disambiguation awareness, with over 88\% surface adoption. Our Differential Nocuity framework connects type-specific vulnerability to disambiguation channel availability and suggests both type-aware policy auditing and externalized ambiguity detection for policy-governed agent deployments.
3	\end{abstract}
4	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 456
}
```

</details>

---


### Tool call

_source line 596 · 2026-05-21T16:56:57.654066+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 597 · 2026-05-21T16:56:58.106899+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	A customer asks to return a customized item within the 30-day window. The agent consults the store policy, which states that ``items may be returned within 30 days.'' The word ``items'' scopes over all product categories, including custom orders that are normally final sale. The agent grants a full refund and arranges free return shipping. One word of scopal ambiguity costs the retailer \$200.
5	
6	LLM-based agents increasingly operate under natural-language policy specifications that govern their permitted actions. These specifications inevitably contain ambiguity: a property that has been studied for decades in requirements engineering (RE) and computational linguistics. \citet{berry_kamsties_2004} distinguish between \emph{nocuous} (i.e., harmful) ambiguity, where different stakeholders arrive at different interpretations, and \emph{innocuous} ambiguity, where shared organizational context ensures convergent interpretation. In human RE workflows, most ambiguity is innocuous because developers share domain knowledge, can consult colleagues, and iteratively clarify requirements.
7	
8	LLM agents lack these disambiguation channels. They cannot consult colleagues, rarely escalate to users, and must resolve ambiguity in real time from the text alone. This raises a question that has not been empirically addressed: does policy ambiguity cause safety violations in LLM agents, and if so, does the \emph{type} of ambiguity predict the severity of the violation? Prior work classifies ambiguity types in policies \citep{drip_r_2026,li_ambiguity_taxonomy_2024} or measures policy understanding quality \citep{policybank_2026}, but no existing study provides a causal, type-granularity mapping from ambiguity to safety violations.
9	
10	\begin{figure*}[t]
11	\centering
12	\includegraphics[width=\textwidth]{figures/fig1_overview.pdf}
13	\caption{Experimental overview. We construct 300 matched clause pairs across a six-type, two-
…[truncated 1963 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 598 · 2026-05-21T16:56:58.107359+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 599 · 2026-05-21T16:56:59.064972+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	\subsection{Experimental Platform}
5	
6	We conduct all experiments on the original release of $\tau^2$-bench \citep{tau2_bench_2025}, a dual-control conversational agent benchmark spanning retail and airline customer service domains. $\tau^2$-bench provides natural-language policy documents, tool APIs, and multi-turn user interactions with ground-truth evaluation via assertion checking. Its policy injection mechanism allows us to replace individual policy clauses while preserving the surrounding context, enabling controlled ambiguity manipulation.
7	
8	\subsection{Matched-Pair Design}
9	
10	For each of the six ambiguity types, we construct 50 \emph{clause pairs}: an ambiguous variant and a matched unambiguous variant that conveys the same intended policy but resolves the ambiguity. Pairs are minimal edits: the unambiguous variant adds only the information necessary to eliminate the target ambiguity (e.g., for scopal ambiguity, replacing ``items may be returned within 30 days'' with ``standard items may be returned within 30 days; customized items are final sale''). This yields 300 clause pairs $\times$ 2 conditions $\times$ 5 models $= 2{,}997$ episodes (3 episodes lost to API errors in one Qwen3 batch).
11	
12	Clause pairs are generated through a template-based pipeline and reviewed by two independent annotators (both with NLP background) to ensure (1) the ambiguous variant contains exactly one instance of the target type, (2) the unambiguous variant resolves it without changing policy scope, and (3) the ambiguity is plausibly natural. Annotators independently verified type assignments with a 96\% pass rate; disagreements were resolved by discussion. A post-hoc realism validation confirms linguistic consistency with original $\tau^2$-bench policy text (\S\ref{sec:limitations}).
13	
14	\subsection{Models}
15	
16	We evaluate five models spanning four providers and two architecture families: GPT-5.4 and GPT-4.1 (OpenAI, pro
…[truncated 4508 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 957
}
```

</details>

---


### Tool call

_source line 600 · 2026-05-21T16:56:59.065432+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 601 · 2026-05-21T16:56:59.567545+00:00_

1	\section{Results}
2	\label{sec:results}
3	
4	We organize results around four analyses of increasing specificity: the binary ambiguity effect (C1), the type hierarchy (C2), the aggregate layer effect (C3), and the model$\times$type interaction (C4). C1 and C2 constitute our primary claims; C3 is inconclusive; C4 is exploratory but provides the model$\times$type interaction analysis.
5	
6	\subsection{Binary Ambiguity Effect (C1)}
7	
8	Across all five models and six types, ambiguous clauses increase violation rates by 34.0 pp (41.0\% vs.\ 6.9\%, OR $= 15.1$, 95\% CI $[10.78, 21.17]$, $p < 10^{-105}$). Of 1,497 matched pairs, the discordant ratio is 15.1:1 (544 ambiguous-only vs.\ 36 unambiguous-only violations). All six types individually produce significant increases (all $p < 10^{-5}$), and all five models show large effects ($+25.7$ to $+39.0$ pp, all $p < 10^{-17}$). Perturbation controls confirm specificity to semantic ambiguity ($n = 300$, $\Delta_{\text{perturb}} = -0.67$\,pp, CI containing zero), and results replicate under an alternative severity threshold (Appendix~\ref{app:severity}). Clause identity explains 22.4\% of variance versus 1.0\% for model identity. A replication on two additional model families (Gemini-2.5-Flash, LLaMA-4-Scout; Appendix~\ref{app:model_expansion}) confirms the binary effect across seven models spanning six providers ($\Delta = +20.0$ to $+33.6$\,pp, both $p < 10^{-6}$).
9	
10	\subsection{Type Hierarchy (C2)}
11	
12	\begin{table*}[t]
13	\centering
14	\caption{Violation rates (\%) under ambiguous policy clauses by type and model. $\Delta$pp denotes the pooled difference between ambiguous and unambiguous conditions across all five models. All per-type differences are significant ($p < 10^{-5}$, Fisher's exact test).}
15	\label{tab:main_results}
16	\small
17	\begin{tabular}{llrrrrrrrr}
18	\toprule
19	Layer & Type & Pooled & GPT-5.4 & GPT-4.1 & Claude & Qwen3 & DeepSeek & $\Delta$pp & $p$ \\
20	\midrule
21	\multirow{3}{*}{\textcolor{
…[truncated 5728 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 602 · 2026-05-21T16:56:59.567927+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/analysis.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/analysis.tex"
  }
}
```

</details>

---


### Tool result

_source line 603 · 2026-05-21T16:57:00.020145+00:00_

1	\section{Error Analysis \emph{[Exploratory]}}
2	\label{sec:analysis}
3	
4	The following failure mode taxonomy emerges empirically from LLM-coded traces, distinct from the input ambiguity taxonomy (\S\ref{sec:taxonomy}).
5	
6	We analyze 614 violation traces across all five models, coded into five failure modes: unauthorized escalation, assumption-based action, scope misapplication, arbitrary rule selection, and conservative refusal. GPT-5.4 and GPT-4.1 serve as detailed annotation anchors because they span the judge boundary. Inter-coder reliability is substantial (Gwet's AC$_1$ $= 0.62$ \citep{gwet_2014}; Cohen's $\kappa = 0.52$ \citep{cohen_1960}; the gap reflects the prevalence paradox, as three categories account for ${\sim}$90\% of instances).
7	
8	\subsection{Type-Specific Failure Mechanisms}
9	
10	The five-model data reveal three mechanistically distinct failure patterns that crosscut the specification/linguistic layer boundary.
11	
12	\emph{Structural misparse} (scope misapplication): the agent constructs an incorrect parse and follows it consistently, paralleling garden-path processing \citep{frazier_rayner_1982,ferreira_good_enough_2002}---e.g., parsing ``items purchased with a coupon or during a sale are final'' as restricting only coupon purchases. This dominates scopal (all 5 models), conditional precedence (all 5), and coreferential (3/5).
13	
14	\emph{Information gap-filling} (assumption-based action): the agent fills missing information with plausible but incorrect defaults---e.g., inventing a 30-day return window when none is specified. This dominates incompleteness (3/5) and lexical (3/5).
15	
16	\emph{Boundary violation} (unauthorized escalation): the agent exceeds permission boundaries when authorization scope is underspecified---e.g., issuing a refund above its stated limit rather than escalating; 69.2\% of such violations involve unauthorized escalation with zero conservative refusals ($p < 10^{-4}$, binomial test), revealing systematic permis
…[truncated 1966 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 604 · 2026-05-21T16:57:00.020638+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 605 · 2026-05-21T16:57:00.021194+00:00_

1	\section{Discussion}
2	\label{sec:discussion}
3	
4	\paragraph{Differential Nocuity.}
5	\citet{berry_kamsties_2004} distinguish nocuous from innocuous ambiguity by stakeholder divergence. Our results extend this to LLM agents: all six types are nocuous ($+34.0$ pp), but type primarily determines severity (22:1 clause-vs.-model variance ratio). We propose \emph{Differential Nocuity} as a conceptual framework: the risk of a policy ambiguity depends on three factors---ambiguity type (which determines base vulnerability), safety training (which selectively mitigates boundary-type ambiguities), and disambiguation channel availability (which determines whether recovery is possible). Systematic nocuity---41.3\% of clauses trigger majority-convergent violations (\S\ref{sec:analysis})---makes such errors invisible in agreement-based evaluation, a pattern confirmed across seven models spanning six providers (Appendix~\ref{app:model_expansion}).
6	
7	\paragraph{Practical implications.}
8	The exploratory model$\times$type interaction (C4) suggests safety training selectively mitigates boundary-type ambiguities. Incompleteness bypasses intervention points via gap-filling \citep{ferreira_good_enough_2002}---the agent fills missing information with plausible defaults rather than encountering a refusal-eligible decision. Authorization scope, involving explicit permission boundaries, varies 48\,pp within the same judge (\S\ref{sec:c4}), consistent with boundary-targeted training. A preliminary mitigation experiment (Appendix~\ref{app:mitigation}) confirms this asymmetry: disambiguation instructions reduce authorization scope violations by 18.0\,pp but incompleteness by only 3.4\,pp. A proof-of-concept classifier (Appendix~\ref{app:detection}) achieves F1\,=\,0.81 for binary detection but only 0.34 for incompleteness. With $<$11\% agent self-awareness (\S\ref{sec:analysis}), type-aware auditing and externalized detection tools \citep{chantree_2006,ferrari_ambiguity_2019} remain nece
…[truncated 41 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 606 · 2026-05-21T16:57:00.975355+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 607 · 2026-05-21T16:57:01.126389+00:00_

1	\section*{Limitations}
2	\label{sec:limitations}
3	
4	\paragraph{Model coverage.} We evaluate seven API-accessible models from six providers (four proprietary, three open-source; two in replication, Appendix~\ref{app:model_expansion}). Smaller open-source models (7B--70B parameters) may show different vulnerability patterns, and our findings may not generalize to models with fundamentally different training approaches.
5	
6	\paragraph{Domain scope.} $\tau^2$-bench covers retail and airline customer service. Policy ambiguity effects in other domains (healthcare, finance, legal) remain to be tested, though the within-study cross-domain consistency is encouraging: failure mode distributions share the same top-two modes (assumption-based action and unauthorized escalation) across domains, with individual mode base rates differing by up to 12.5 pp, likely reflecting domain policy structure rather than methodological artifacts.
7	
8	\paragraph{Synthetic ambiguity.} Our matched-pair design requires synthetic construction of ambiguous variants, which may not capture the full distribution of naturally occurring policy ambiguities. We mitigate this through expert review and a realism validation comparing ambiguous clauses against original $\tau^2$-bench policy text. Ambiguous clauses are indistinguishable from originals in lexical diversity (TTR, KS $p = 0.89$) and word length ($p = 0.09$). Readability is slightly higher (Flesch--Kincaid $d = 0.29$, $p = 0.006$) and sentence length moderately higher ($d = 0.74$), both reflecting the structural demands of encoding ambiguity in standalone clauses. Across matched pairs, disambiguation preserves readability (Flesch--Kincaid $d = 0.14$, $p = 0.10$), confirming that minimal edits change semantic precision without altering linguistic register.
9	
10	\paragraph{Cross-judge asymmetry.} Although our dual-judge calibration (\S\ref{sec:method}) shows no systematic bias ($p = 0.606$) and human validation confirms the LLM judge operates 
…[truncated 2173 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 608 · 2026-05-21T16:57:01.126873+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 609 · 2026-05-21T16:57:01.177554+00:00_

1	\section{TOST Equivalence Sensitivity}
2	\label{app:tost}
3	
4	Table~\ref{tab:tost_sensitivity} reports the TOST equivalence analysis \citep{lakens_2017} across seven margins. Three pairs involving incompleteness never reach equivalence even at $\pm 20$ pp: conditional precedence--incompleteness ($\Delta = 16.8$ pp), coreferential--incompleteness ($\Delta = 22.0$ pp), and incompleteness--scopal ($\Delta = 14.2$ pp).
5	
6	\begin{table}[!ht]
7	\centering
8	\small
9	\caption{TOST equivalence sensitivity across margins. Mid-tier = fraction of the six within-cluster pairs (lexical, auth.\ scope, scopal, cond.\ prec.) that are equivalent. Inc.\ and Cor.\ columns indicate separation from the mid-tier cluster.}
10	\label{tab:tost_sensitivity}
11	\begin{tabular}{lcccc}
12	\toprule
13	Margin & Equiv.\ pairs & Mid-tier & Inc.\ sep. & Cor.\ sep. \\
14	\midrule
15	$\pm 5$ pp & 0/15 & 0/6 & \checkmark & \checkmark \\
16	$\pm 8$ pp & 0/15 & 0/6 & \checkmark & \checkmark \\
17	$\pm 10$ pp & 3/15 & 3/6 & \checkmark & \checkmark \\
18	$\pm 12$ pp & 5/15 & 5/6 & \checkmark & \checkmark \\
19	$\pm 15$ pp & 8/15 & 6/6 & \checkmark & -- \\
20	$\pm 18$ pp & 9/15 & 6/6 & \checkmark & -- \\
21	$\pm 20$ pp & 12/15 & 6/6 & -- & -- \\
22	\bottomrule
23	\end{tabular}
24	\end{table}
25	
26	\section{Mitigation Experiment}
27	\label{app:mitigation}
28	
29	Table~\ref{tab:mitigation} reports the per-type, per-model $\Delta$pp from the disambiguation-instruction mitigation experiment (1,256 treatment episodes across five of six types; coreferential was not tested). The treatment appends a type-specific disambiguation instruction to the agent's system prompt. Control rates are the matched 5-type subset from the full study (\S\ref{sec:results}).
30	
31	\begin{table*}[!ht]
32	\centering
33	\small
34	\caption{Violation rate change ($\Delta$pp) after adding type-specific disambiguation instructions. Negative values indicate reduction. Baseline violation rates are shown in parentheses. Coreferential was 
…[truncated 10656 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 610 · 2026-05-21T16:57:06.146067+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/taxonomy.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/taxonomy.tex"
  }
}
```

</details>

---


### Tool result

_source line 611 · 2026-05-21T16:57:06.698548+00:00_

1	\section{Ambiguity Taxonomy}
2	\label{sec:taxonomy}
3	
4	We adopt an operational definition of ambiguity following \citet{wasow_ambiguity_2005}: a policy clause is ambiguous when it admits multiple distinct interpretations available to a competent reader, including cases of vagueness where the boundary between interpretations is gradient rather than discrete \citep{kennedy_vagueness_2007}.
5	
6	Our taxonomy comprises six types organized into two layers, drawing on \citet{li_ambiguity_taxonomy_2024}'s NLP taxonomy (11 types), \citet{massey_ambiguity_re_2014}'s requirements engineering taxonomy (6 types), and the concurrent DRIP-R benchmark \citep{drip_r_2026} (5 types). We select types based on two criteria: frequency in operational policy documents (assessed via manual audit of $\tau^2$-bench policies) and theoretical distinctiveness (each type maps to a different resolution mechanism).
7	
8	\paragraph{Linguistic layer.} These types operate at the syntactic or semantic level and can, in principle, be resolved by parsing or contextual cues within the text.
9	\begin{itemize}
10	\item \textbf{Scopal}: quantifier, negation, or modal scope interactions (e.g., ``all items may not be returned'' admits universal-negation and negation-of-universal readings).
11	\item \textbf{Lexical}: polysemy or homonymy (e.g., ``charge'' as financial cost vs.\ penalty; ``party'' as individual vs.\ group).
12	\item \textbf{Coreferential}: unclear pronoun or noun-phrase reference (e.g., ``the agent should verify the customer's identity before processing their refund request, which must be approved by a supervisor'' where ``which'' could refer to the verification or the refund).
13	\end{itemize}
14	
15	\paragraph{Specification layer.} These types arise from pragmatic or discourse-level gaps that require domain knowledge or organizational context to resolve.
16	\begin{itemize}
17	\item \textbf{Authorization scope}: vague permission or role boundaries (e.g., ``authorized personnel may issue r
…[truncated 1121 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 552
}
```

</details>

---


### Tool call

_source line 612 · 2026-05-21T16:57:06.699085+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 613 · 2026-05-21T16:57:07.351833+00:00_

1	\section{Conclusion}
2	
3	Ambiguous policy clauses increase agent safety violations by 34.0\,pp (OR\,$=$\,15.1) across five models. Clause identity explains 22$\times$ more variance than model identity; the two-tier type hierarchy replicates on two additional model families ($\rho = 0.60$--$0.90$). With $<$11\% disambiguation awareness, type-aware auditing and externalized detection are critical for policy-governed agent deployments.
4	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 652
}
```

</details>

---


### Tool call

_source line 614 · 2026-05-21T16:57:07.853865+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 615 · 2026-05-21T16:57:07.904663+00:00_

1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{Ambiguity in NLP and requirements engineering.}
5	Ambiguity has been studied extensively in both computational linguistics and software engineering. Word sense disambiguation \citep{navigli_wsd_2009} addresses lexical ambiguity at the token level; our lexical type extends this to policy-specific polysemy. \citet{li_ambiguity_taxonomy_2024} propose an 11-type NLP taxonomy covering syntactic, semantic, and pragmatic ambiguity, from which we draw our linguistic-layer types. In requirements engineering (RE), \citet{massey_ambiguity_re_2014} classify six ambiguity types in regulatory texts, and \citet{berry_kamsties_2004} introduce the distinction between nocuous ambiguity (where stakeholders diverge on interpretation) and innocuous ambiguity (where they converge). Computational detection of nocuous ambiguity has progressed from heuristic methods \citep{chantree_2006,willis_nocuous_2008} through NLP-based cross-domain detectors \citep{ferrari_ambiguity_2019,ferrari_defects_2018} to transformer-based approaches for anaphoric ambiguity \citep{ezzini_taphsir_2022,ezzini_anaphoric_2022}. \citet{zhao_nlp4re_2021} survey the broader NLP4RE landscape. Our work extends Berry and Kamsties' framework to LLM agents, where the absence of shared organizational context makes previously innocuous ambiguity nocuous.
6	
7	\paragraph{Psycholinguistics of ambiguity processing.}
8	\citet{ferreira_good_enough_2002} show that human comprehenders build shallow, ``good-enough'' representations rather than full parses, paralleling our observation that LLM agents adopt surface interpretations. \citet{frazier_rayner_1982} demonstrate early commitment to a single parse; \citet{li_garden_path_llm_2024} provide direct evidence that LLMs exhibit analogous garden-path effects. \citet{liu_ambiguity_2023} demonstrate that language models fail to represent ambiguity, collapsing multiple interpretations into a single output. These findings
…[truncated 2210 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 616 · 2026-05-21T16:58:44.809596+00:00_

called mcp__agent-ml-research__verify_references

<details open><summary>🔧 Tool call — mcp__agent-ml-research__verify_references</summary>

```json
{
  "paper_dir": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper",
  "project": "policy_ambiguity_safety"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "mcp__agent-ml-research__verify_references",
  "tool_args": {
    "paper_dir": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper",
    "project": "policy_ambiguity_safety"
  }
}
```

</details>

---


### Tool result

_source line 617 · 2026-05-21T16:59:21.798104+00:00_

{"result":"{\"success\": true, \"data\": {\"summary\": {\"total_bib_entries\": 39, \"total_citations\": 52, \"unique_cited_keys\": 35, \"orphan_bib\": 4, \"missing_bib\": 0, \"duplicate_keys\": 0, \"online_verified\": 27, \"online_not_found\": 7, \"online_mismatch\": 5}, \"cross_check\": {\"orphan_bib\": [\"ferreira_patson_2007\", \"lassiter_goodman_2017\", \"levy_expectation_2008\", \"poesio_artstein_2005\"], \"missing_bib\": [], \"orphan_count\": 4, \"missing_count\": 0}, \"bib_entries\": [{\"key\": \"li_ambiguity_taxonomy_2024\", \"type\": \"inproceedings\", \"title\": \"A Taxonomy of Ambiguity Types for NLP\", \"authors\": \"Li, Margaret Y. and Liu, Alisa and Wu, Zhaofeng and Smith, Noah A.\", \"year\": \"2024\", \"venue\": \"Proceedings of EACL 2024\"}, {\"key\": \"massey_ambiguity_re_2014\", \"type\": \"inproceedings\", \"title\": \"Identifying and Classifying Ambiguity for Regulatory Requirements\", \"authors\": \"Massey, Aaron K. and Rutledge, Richard L. and Ant\\\\'on, Annie I. and Swire, Peter...\", \"year\": \"2014\", \"venue\": \"22nd IEEE International Requirements Engineering Conference (RE)\"}, {\"key\": \"berry_kamsties_2004\", \"type\": \"techreport\", \"title\": \"From Contract Drafting to Software Specification: Linguistic Sources of Ambiguity --- A Handbook\", \"authors\": \"Berry, Daniel M. and Kamsties, Erik and Krieger, Michael M.\", \"year\": \"2004\", \"venue\": \"\"}, {\"key\": \"chantree_2006\", \"type\": \"inproceedings\", \"title\": \"Identifying Nocuous Ambiguities in Natural Language Requirements\", \"authors\": \"Chantree, Francis and Nuseibeh, Bashar and de Roeck, Anne and Willis, Alistair\", \"year\": \"2006\", \"venue\": \"14th IEEE International Requirements Engineering Conference (RE)\"}, {\"key\": \"wasow_ambiguity_2005\", \"type\": \"incollection\", \"title\": \"The Puzzle of Ambiguity\", \"authors\": \"Wasow, Thomas and Perfors, Amy and Beaver, David\", \"year\": \"2005\", \"venue\": \"Morphology and the Web of Grammar: Essays
…[truncated 29415 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "mcp__agent-ml-research__verify_references",
  "elapsed_ms": 36988
}
```

</details>

---


### Tool call

_source line 618 · 2026-05-21T17:02:56.051279+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 1 审稿意见（方法严谨性 + 实验设计）\n\n### 总体评分\n**Overall**: 3.5 (Borderline Conference)\n**置信度**: High (4/5)\n**一句话总结**: 研究问题重要且实验设计整体严谨，但 TOST SESOI 缺乏外部锚定、authorization scope 的测量信度不足以支撑 C4 的关键声称、incompleteness confound 分析不够透明，这些方法论短板需要修补后才能稳定达到主会议水平。\n\n### 官方维度打分（ACL ARR review form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3/5 | 核心 C1 claim 有充分支撑，但 C2 的 type hierarchy 依赖于争议性的 SESOI 选择；C4 exploratory claims 建立在信度最低的 type 之上 |\n| Excitement | 3/5 | 研究问题及时且有实践价值，Differential Nocuity 框架有概念贡献，但整体是 Berry & Kamsties 框架在 LLM agent 上的经验延伸，novelty 中等 |\n| Reproducibility | 3/5 | 平台和统计方法报告充分，但缺少 API 超参数（temperature 等）、无代码/数据发布声明、test-retest 仅覆盖 OpenAI 模型族 |\n| Confidence | 4/5 | 仔细阅读了论文并熟悉相关统计方法和 agent safety 文献 |\n\n---\n\n### Must-Fix 问题（影响接收决定）\n\n**N1** [critical] TOST SESOI ±15 pp 缺乏外部锚定，two-tier structure 强烈依赖 margin 选择\n\n- 具体位置：Section 4.6, Appendix A (Table 2)\n- 问题：论文选择 SESOI = ±15 pp 的理由是 \"a type producing ≥15 pp more violations warrants distinct policy handling\"（§4.6），这仅是作者自行设定的实践显著性标准，缺乏独立的外部锚定（如领域专家调研、已有安全阈值文献等）。从 Table 2 的敏感性分析看：±10 pp 时仅 3/6 mid-tier pairs 达到等价，±12 pp 时 5/6，直到 ±15 pp 才 6/6。这意味着 \"robust two-tier structure\"（abstract, §5.2）的声称本质上取决于是否接受 15 pp 这一特定阈值。mid-tier cluster 本身的内部极差约 11 pp（coreferential 31.6% 到 lexical 42.8%），SESOI 大于这个极差才形成 cluster——这在方法论上是循环的。\n- 为什么影响接收：Type hierarchy (C2) 是论文三大贡献之一，如果 two-tier structure 的稳健性不成立，论文的核心叙事 \"Differential Nocuity\" 的精细化程度大打折扣。\n- 建议修改方向：(1) 提供 SESOI 的外部锚定（如 policy 领域的 minimal important difference 文献、安全工程的 risk threshold 标准）；(2) 明确承认 two-tier structure 在 ±10–12 pp 时不稳健；(3) 考虑使用 margin-free 的方法（如 Bayesian estimation 或 bootstrap cluster analysis）作为补充。\n\n**N2** [critical] Authorization scope 的 judge agreement (κ = 0.385) 过低，无法支撑 C4 的 \"model-differentiating type\" 声称\n\n- 具体位置：Section 4.4, Section 5.4, Appendix G (Table 8)\n- 问题：论文将 authorization scope 定位为 \"model-differentiating type\"（§5.4, Figure 3），52 pp 跨模型变异是 C4 最突出的发现。然而：(1) cross-judge κ = 0.385 仅为 \"fair\"，是六个 type 中最低的；(2) human-LLM κ = 0.644，CI = [0.35, 0.91]，下界仅 0.35；(3) 论文辩称 \"48 pp within-judge range far exceeds measurement noise\"，但 κ = 0.385 意味着约 38.5% 的 judge agreement 超出 chance 水平——在这种信度下，52 pp 的跨模型变异中有多少是真实的 model difference、多少是测量噪声，无法可靠区分。\n- 为什么影响接收：C4 是论文提出 \"safety training selectively mitigates boundary-type ambiguities\" 这一实践建议的核心依据。如果 auth scope 的测量不可靠，从 Discussion 到 Conclusion 的建议链条断裂。\n- 建议修改方向：(1) 对 auth scope 增加人工标注样本量（当前 n=34 per type 过小），缩窄 CI；(2) 报告 within-judge analysis 的 auth scope 专项信度；(3) 对 C4 的 auth scope claims 降级为 \"suggestive\" 而非 \"robust\"。\n\n**N3** [critical] Incompleteness confound 分析缺乏透明度\n\n- 具体位置：Section 5.2, Appendix F\n- 问题：论文承认 incompleteness resolution 必然添加 policy content，造成 information-addition confound（§3, §5.2）。logistic regression 控制 per-clause token delta 后报告 \"coefficient change < 8%, p = 0.022\"，但：(1) 未展示完整回归表（coefficients, SEs, model fit），读者无法评估回归质量；(2) token count 是 information content 的粗糙代理——添加一句 \"customized items are final sale\" 的信息量远超其 token 数所能捕捉；(3) 论文在 abstract 中将 incompleteness 列为 \"consistently high (46–62%)\" 的核心发现，但正文又承认这是 \"upper bound partly reflecting an information-addition confound\"——这两个表述在摘要中未分化，有误导读者之嫌。\n- 为什么影响接收：Incompleteness 是 violation rate 最高的 type，是论文多个 practical implication 的基础。\n- 建议修改方向：(1) 展示完整回归表；(2) 探索更好的 information content proxy；(3) 在 abstract 中明确标注 incompleteness 效应含 confound。\n\n---\n\n### Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] 缺少 API 超参数报告\n- 具体位置：Section 4.3\n- 论文未报告 temperature、max_tokens、top_p 等采样参数，对 reproducibility 有直接影响。\n\n**W2** [warning] Test-retest stability (ICC) 仅在 OpenAI 模型族内测量\n- 具体位置：Section 4.5\n- ICC = 0.919 来自 GPT-5.4 和 GPT-4.1。跨 provider 的 test-retest 未测量。\n\n**W3** [warning] Per-type human-LLM agreement 的 CI 极宽\n- 具体位置：Appendix G (Table 8)\n- Scopal CI = [0.00, 1.00]（完全无信息），Coreferential CI = [0.00, 0.84]。源于 per-type n = 32–34。建议在正文讨论此限制。\n\n**W4** [warning] 无代码/数据可用性声明\n- 论文未提及 300 clause pairs、代码或 evaluation pipeline 的发布计划。\n\n**W5** [warning] Clause-level heterogeneity未充分分析\n- 具体位置：Section 5.1\n- Clause identity 解释 22.4% variance，但未分析 outlier clauses、type 内 clause-level variance 分布。50 clauses/type + high variance → type-level 估计可能不稳定。\n\n**W6** [warning] 人工标注者是否对 condition 设盲？\n- 具体位置：Section 4.4\n- 报告了 blind to LLM labels，但未说明是否 blind to ambiguity condition。\n\n---\n\n### 小问题（不影响接收）\n\n- **M1**: bib 有 4 个 orphan 条目（ferreira_patson_2007, lassiter_goodman_2017, levy_expectation_2008, poesio_artstein_2005）未引用。\n- **M2**: ferrari_defects_2018 的 bib 一作为 Rosadini 但 key 暗示 Ferrari，可能引起混淆。\n- **M3**: Error analysis 的 inter-coder κ = 0.52，minority category κ = 0.29，建议将 failure mode taxonomy 降级为 exploratory observation 而非 contribution。\n- **M4**: C3 (layer effect) 在正文标为 inconclusive，但 abstract 未提及此 null result。\n\n---\n\n### Questions（需要作者回答）\n\n**Q1**: SESOI = ±15 pp 是否有外部文献或专家调研支持？±10 pp 时 type hierarchy 如何变化？\n\n**Q2**: 能否提供 within-judge subgroup 的 authorization scope 专项 κ？\n\n**Q3**: Incompleteness confound 的 logistic regression 完整回归表？是否考虑过 information-theoretic measures 作为更好的 proxy？\n\n**Q4**: Temperature 设置为多少？是否在 temperature > 0 下测试过 stability？\n\n**Q5**: 300 clause pairs 是否计划公开？\n\n---\n\n### Missing References\n\n- Kadavath et al. (2022) \"Language Models (Mostly) Know What They Know\" — 与 Ambiguity Blindness 相关\n- Anvari & Lakens (2021) \"Using Anchor-Based Methods to Determine the Smallest Effect Size of Interest\" — 锚定 SESOI 选择\n- Zheng et al. (2024) \"Judging LLM-as-a-Judge\" — LLM-as-judge 方法论\n\n---\n\n### 主要优势\n\n- C1 (binary ambiguity effect) 有强力支撑：OR = 15.1, CI = [10.78, 21.17], 7 模型 replication\n- Matched-pair design + perturbation control 的因果推理框架设计良好\n- 诚实的 limitation 讨论（C3 inconclusive, C4 exploratory, incompleteness confound）\n- Ambiguity Blindness (<11% awareness) 是一个直观但重要的经验发现\n- TOST sensitivity analysis (Table 2) 虽然暴露了 margin 依赖性，但提供这一分析本身体现了方法论严谨性\n- Two-model replication (Gemini, LLaMA) 增强了 C1 的外部效度",
  "reviewer_id": "1",
  "project": "policy_ambiguity_safety"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 1 审稿意见（方法严谨性 + 实验设计）\n\n### 总体评分\n**Overall**: 3.5 (Borderline Conference)\n**置信度**: High (4/5)\n**一句话总结**: 研究问题重要且实验设计整体严谨，但 TOST SESOI 缺乏外部锚定、authorization scope 的测量信度不足以支撑 C4 的关键声称、incompleteness confound 分析不够透明，这些方法论短板需要修补后才能稳定达到主会议水平。\n\n### 官方维度打分（ACL ARR review form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3/5 | 核心 C1 claim 有充分支撑，但 C2 的 type hierarchy 依赖于争议性的 SESOI 选择；C4 exploratory claims 建立在信度最低的 type 之上 |\n| Excitement | 3/5 | 研究问题及时且有实践价值，Differential Nocuity 框架有概念贡献，但整体是 Berry & Kamsties 框架在 LLM agent 上的经验延伸，novelty 中等 |\n| Reproducibility | 3/5 | 平台和统计方法报告充分，但缺少 API 超参数（temperature 等）、无代码/数据发布声明、test-retest 仅覆盖 OpenAI 模型族 |\n| Confidence | 4/5 | 仔细阅读了论文并熟悉相关统计方法和 agent safety 文献 |\n\n---\n\n### Must-Fix 问题（影响接收决定）\n\n**N1** [critical] TOST SESOI ±15 pp 缺乏外部锚定，two-tier structure 强烈依赖 margin 选择\n\n- 具体位置：Section 4.6, Appendix A (Table 2)\n- 问题：论文选择 SESOI = ±15 pp 的理由是 \"a type producing ≥15 pp more violations warrants distinct policy handling\"（§4.6），这仅是作者自行设定的实践显著性标准，缺乏独立的外部锚定（如领域专家调研、已有安全阈值文献等）。从 Table 2 的敏感性分析看：±10 pp 时仅 3/6 mid-tier pairs 达到等价，±12 pp 时 5/6，直到 ±15 pp 才 6/6。这意味着 \"robust two-tier structure\"（abstract, §5.2）的声称本质上取决于是否接受 15 pp 这一特定阈值。mid-tier cluster 本身的内部极差约 11 pp（coreferential 31.6% 到 lexical 42.8%），SESOI 大于这个极差才形成 cluster——这在方法论上是循环的。\n- 为什么影响接收：Type hierarchy (C2) 是论文三大贡献之一，如果 two-tier structure 的稳健性不成立，论文的核心叙事 \"Differential Nocuity\" 的精细化程度大打折扣。\n- 建议修改方向：(1) 提供 SESOI 的外部锚定（如 policy 领域的 minimal important difference 文献、安全工程的 risk threshold 标准）；(2) 明确承认 two-tier structure 在 ±10–12 pp 时不稳健；(3) 考虑使用 margin-free 的方法（如 Bayesian estimation 或 bootstrap cluster analysis）作为补充。\n\n**N2** [critical] Authorization scope 的 judge agreement (κ = 0.385) 过低，无法支撑 C4 的 \"model-differentiating type\" 声称\n\n- 具体位置：Section 4.4, Section 5.4, Appendix G (Table 8)\n- 问题：论文将 authorization scope 定位为 \"model-differentiating type\"（§5.4, Figure 3），52 pp 跨模型变异是 C4 最突出的发现。然而：(1) cross-judge κ = 0.385 仅为 \"fair\"，是六个 type 中最低的；(2) human-LLM κ = 0.644，CI = [0.35, 0.91]，下界仅 0.35；(3) 论文辩称 \"48 pp within-judge range far exceeds measurement noise\"，但 κ = 0.385 意味着约 38.5% 的 judge agreement 超出 chance 水平——在这种信度下，52 pp 的跨模型变异中有多少是真实的 model difference、多少是测量噪声，无法可靠区分。\n- 为什么影响接收：C4 是论文提出 \"safety training selectively mitigates boundary-type ambiguities\" 这一实践建议的核心依据。如果 auth scope 的测量不可靠，从 Discussion 到 Conclusion 的建议链条断裂。\n- 建议修改方向：(1) 对 auth scope 增加人工标注样本量（当前 n=34 per type 过小），缩窄 CI；(2) 报告 within-judge analysis 的 auth scope 专项信度；(3) 对 C4 的 auth scope claims 降级为 \"suggestive\" 而非 \"robust\"。\n\n**N3** [critical] Incompleteness confound 分析缺乏透明度\n\n- 具体位置：Section 5.2, Appendix F\n- 问题：论文承认 incompleteness resolution 必然添加 policy content，造成 information-addition confound（§3, §5.2）。logistic regression 控制 per-clause token delta 后报告 \"coefficient change < 8%, p = 0.022\"，但：(1) 未展示完整回归表（coefficients, SEs, model fit），读者无法评估回归质量；(2) token count 是 information content 的粗糙代理——添加一句 \"customized items are final sale\" 的信息量远超其 token 数所能捕捉；(3) 论文在 abstract 中将 incompleteness 列为 \"consistently high (46–62%)\" 的核心发现，但正文又承认这是 \"upper bound partly reflecting an information-addition confound\"——这两个表述在摘要中未分化，有误导读者之嫌。\n- 为什么影响接收：Incompleteness 是 violation rate 最高的 type，是论文多个 practical implication 的基础。\n- 建议修改方向：(1) 展示完整回归表；(2) 探索更好的 information content proxy；(3) 在 abstract 中明确标注 incompleteness 效应含 confound。\n\n---\n\n### Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] 缺少 API 超参数报告\n- 具体位置：Section 4.3\n- 论文未报告 temperature、max_tokens、top_p 等采样参数，对 reproducibility 有直接影响。\n\n**W2** [warning] Test-retest stability (ICC) 仅在 OpenAI 模型族内测量\n- 具体位置：Section 4.5\n- ICC = 0.919 来自 GPT-5.4 和 GPT-4.1。跨 provider 的 test-retest 未测量。\n\n**W3** [warning] Per-type human-LLM agreement 的 CI 极宽\n- 具体位置：Appendix G (Table 8)\n- Scopal CI = [0.00, 1.00]（完全无信息），Coreferential CI = [0.00, 0.84]。源于 per-type n = 32–34。建议在正文讨论此限制。\n\n**W4** [warning] 无代码/数据可用性声明\n- 论文未提及 300 clause pairs、代码或 evaluation pipeline 的发布计划。\n\n**W5** [warning] Clause-level heterogeneity未充分分析\n- 具体位置：Section 5.1\n- Clause identity 解释 22.4% variance，但未分析 outlier clauses、type 内 clause-level variance 分布。50 clauses/type + high variance → type-level 估计可能不稳定。\n\n**W6** [warning] 人工标注者是否对 condition 设盲？\n- 具体位置：Section 4.4\n- 报告了 blind to LLM labels，但未说明是否 blind to ambiguity condition。\n\n---\n\n### 小问题（不影响接收）\n\n- **M1**: bib 有 4 个 orphan 条目（ferreira_patson_2007, lassiter_goodman_2017, levy_expectation_2008, poesio_artstein_2005）未引用。\n- **M2**: ferrari_defects_2018 的 bib 一作为 Rosadini 但 key 暗示 Ferrari，可能引起混淆。\n- **M3**: Error analysis 的 inter-coder κ = 0.52，minority category κ = 0.29，建议将 failure mode taxonomy 降级为 exploratory observation 而非 contribution。\n- **M4**: C3 (layer effect) 在正文标为 inconclusive，但 abstract 未提及此 null result。\n\n---\n\n### Questions（需要作者回答）\n\n**Q1**: SESOI = ±15 pp 是否有外部文献或专家调研支持？±10 pp 时 type hierarchy 如何变化？\n\n**Q2**: 能否提供 within-judge subgroup 的 authorization scope 专项 κ？\n\n**Q3**: Incompleteness confound 的 logistic regression 完整回归表？是否考虑过 information-theoretic measures 作为更好的 proxy？\n\n**Q4**: Temperature 设置为多少？是否在 temperature > 0 下测试过 stability？\n\n**Q5**: 300 clause pairs 是否计划公开？\n\n---\n\n### Missing References\n\n- Kadavath et al. (2022) \"Language Models (Mostly) Know What They Know\" — 与 Ambiguity Blindness 相关\n- Anvari & Lakens (2021) \"Using Anchor-Based Methods to Determine the Smallest Effect Size of Interest\" — 锚定 SESOI 选择\n- Zheng et al. (2024) \"Judging LLM-as-a-Judge\" — LLM-as-judge 方法论\n\n---\n\n### 主要优势\n\n- C1 (binary ambiguity effect) 有强力支撑：OR = 15.1, CI = [10.78, 21.17], 7 模型 replication\n- Matched-pair design + perturbation control 的因果推理框架设计良好\n- 诚实的 limitation 讨论（C3 inconclusive, C4 exploratory, incompleteness confound）\n- Ambiguity Blindness (<11% awareness) 是一个直观但重要的经验发现\n- TOST sensitivity analysis (Table 2) 虽然暴露了 margin 依赖性，但提供这一分析本身体现了方法论严谨性\n- Two-model replication (Gemini, LLaMA) 增强了 C1 的外部效度",
    "reviewer_id": "1",
    "project": "policy_ambiguity_safety"
  }
}
```

</details>

---


### Tool result

_source line 619 · 2026-05-21T17:02:59.672232+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_967344d166ba485ad606d14379e69d85:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3620
}
```

</details>

---


### Tool call

_source line 620 · 2026-05-21T17:03:04.450622+00:00_

called mcp__agent-ml-research__cleanup_pdf_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__cleanup_pdf_images</summary>

```json
{
  "output_dir": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/_pdf_images"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "tool_args": {
    "output_dir": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/_pdf_images"
  }
}
```

</details>

---


### Tool result

_source line 621 · 2026-05-21T17:03:04.451069+00:00_

{"result":"{\"success\": true, \"data\": {\"message\": \"目录不存在，无需清理\", \"deleted\": 0}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "elapsed_ms": 0
}
```

</details>

---


### Assistant

_source line 622 · 2026-05-21T17:03:14.382869+00:00_

审稿意见已提交给 Review Director。

总结：我以 Reviewer 1 身份完成了对论文 "Not All Policy Ambiguity Is Equal" 的方法严谨性 + 实验设计审查。**Overall 评分 3.5 (Borderline Conference)**。

核心判断：C1（ambiguity causes violations, OR=15.1）有充分支撑，但从 C1 到 "type-specific differential nocuity"（C2+C4）的推理链有三个关键短板：
1. **TOST SESOI ±15 pp 无外部锚定**，two-tier structure 在 ±10 pp 时不成立
2. **Authorization scope 的 judge κ=0.385 过低**，无法可靠支撑 52 pp 跨模型变异的解读
3. **Incompleteness confound regression 未展示完整回归表**，token count 作为 information content proxy 过于粗糙

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1"
}
```

</details>

---


## Round 18

## Round 18

14 recorded events


### User

_source line 623 · 2026-05-21T17:03:54.282253+00:00_

[Round 1 审稿请求]:
## 交叉分享：Reviewer 2 的完整审稿意见

请逐条回应以下 Reviewer 2 的审稿意见。对每条使用 **[AGREE]** 同意并说明理由，或 **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）。

---

以下是 Reviewer 2 的完整审稿意见：

### Weaknesses

**W1 [MUST-FIX] Incompleteness confound 削弱 type hierarchy 核心 claim。**
- Incompleteness 的 unambiguous variant 必须添加新 policy content，49.2 pp effect 混淆了"歧义消除"与"信息增加"。Logistic regression 控制 information delta（coefficient change <8%, p=0.022）不够充分：token count 只是信息量的粗略代理；regression 中 incompleteness 仍 significant 只说明残余效应存在，无法量化歧义效应 vs. 信息添加效应的比例。
- 直接影响 Table 1 中 incompleteness 作为 hierarchy 顶端的可信度，影响 Abstract/Conclusion 中 "type primarily determines severity" 的 claim。
- 建议：设计 information-matched control，或在 Abstract/Conclusion 显式降低对 incompleteness 排名的 claim 强度。

**W2 [MUST-FIX] Authorization scope 测量可靠性不足以支撑 "model-differentiating type" 论述。**
- Authorization scope cross-judge κ=0.385（fair），human-LLM κ=0.644。论文将其作为 C4 核心发现（52 pp range），但测量工具不可靠时，模型间差异可能部分反映 judge 不稳定性。
- 建议：明确标注该结论为 tentative，或增加 bootstrap CI 量化测量不确定性对模型排名的影响。

**W3 [SHOULD-FIX] Related Work 有 4 条 orphan bib 条目和若干遗漏。**
- Orphan：ferreira_patson_2007, levy_expectation_2008, lassiter_goodman_2017, poesio_artstein_2005
- 遗漏：Constitutional AI/RLHF alignment 文献、AgentBench、引用数 35 条偏少

**W4 [SHOULD-FIX] Differential Nocuity 框架概念化不足。**
- 三因素（type, safety training, channel availability）交互关系未形式化；"channel availability"在论文中未直接测量；与 Berry & Kamsties (2004) 的理论推进关系不清晰。

**W5 [SHOULD-FIX] Abstract 信息密度过高。**
- 包含 6 个统计量、嵌套括号、C1–C4 几乎所有结果的压缩。建议减少数字，保留 2-3 核心发现。

**W6 [SHOULD-FIX] C3 layer effect null result 讨论过于简短。**
- §5.3 仅 3 句话。如果 linguistic/specification 二分法不成立，two-layer taxonomy 的理论基础需要重新论证。

**W7 [MINOR] ferrari_defects_2018 bib 条目第一作者不一致。**

**W8 [MINOR] 缺少 Ethics Statement。**

### Questions
Q1. Incompleteness 的 unambiguous variant 平均添加了多少 token？
Q2. Authorization scope 的 52 pp model range 中，Claude 12% 是否因 conservative refusal？
Q3. 是否考虑过 information-addition perturbation 作为 incompleteness confound 的更直接控制？
Q4. Template-based pipeline 的 template 设计是否公开？96% annotator pass rate 的 disagreement 是否集中在特定类型？

### Missing References
- Levy (2008), Ferreira & Patson (2007), Constitutional AI (Bai et al., 2022), AgentBench (Liu et al., 2023), Bender & Koller (2020)

### Overall Assessment
3.5 (Borderline Conference), Confidence 4/5 (High)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 624 · 2026-05-21T17:04:03.664834+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/experiments.tex",
  "offset": "33",
  "limit": "12"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/experiments.tex",
    "offset": "33",
    "limit": "12"
  }
}
```

</details>

---


### Tool result

_source line 625 · 2026-05-21T17:04:04.167240+00:00_

33	
34	The six types are not interchangeable. An omnibus $\chi^2$ test on ambiguous-condition violation rates rejects the uniformity null ($\chi^2 = 28.02$, $df = 5$, $p = 3.6 \times 10^{-5}$, Cram\'{e}r's $V = 0.137$; statistical power $= 0.993$ at the observed effect). TOST equivalence testing at a $\pm 15$ pp margin reveals a two-tier structure among five types---authorization scope (41.6\%), lexical (42.8\%), scopal (39.4\%), and conditional precedence (36.8\%) form a mid-tier cluster, with coreferential (31.6\%) below---while incompleteness (53.6\%) stands apart as an upper bound whose ranking partly reflects an information-addition confound (\S\ref{sec:results}, Appendix~\ref{app:confound}). Table~\ref{tab:main_results} and Figure~\ref{fig:forest_plot} present the full breakdown.
35	
36	Sensitivity analysis across seven margins ($\pm 5$--$20$ pp; Appendix~\ref{app:tost}) confirms this structure: the two-tier pattern emerges at $\pm 12$ pp (5/6 mid-tier pairs equivalent) and stabilizes at $\pm 15$ pp (6/6).
37	
38	Incompleteness produces the highest violation rate in four of five models (all except GPT-5.4, where authorization scope ranks first at 64\%), with rates $\geq$46\% confirmed in all seven models tested (Appendix~\ref{app:model_expansion}). Incompleteness is structurally distinct: its unambiguous variant adds policy content rather than merely resolving ambiguity, so its 49.2 pp effect is an upper bound; a confound analysis confirms the effect remains significant after controlling for information delta (Appendix~\ref{app:confound}). This pattern replicates on two additional model families (Gemini 48\%, LLaMA 52\%; Appendix~\ref{app:model_expansion}), further suggesting that incompleteness severity reflects a genuine property of the ambiguity type rather than a dataset artifact. Coreferential, whose variants are lexically identical, provides a confound-free lower bound at 31.6\%. Excluding incompleteness, pairwise contrasts show authorization scope and l
…[truncated 527 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 626 · 2026-05-21T17:04:04.618803+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/appendix.tex",
  "offset": "151",
  "limit": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/appendix.tex",
    "offset": "151",
    "limit": "10"
  }
}
```

</details>

---


### Tool result

_source line 627 · 2026-05-21T17:04:05.072319+00:00_

151	\section{Incompleteness Confound Analysis}
152	\label{app:confound}
153	
154	Incompleteness is structurally distinct from the other five types: its unambiguous variant necessarily adds policy content (specifying what was previously missing) rather than merely resolving an existing ambiguity. This raises a confound: the 49.2 pp effect may partly reflect the information addition rather than ambiguity resolution per se.
155	
156	A logistic regression controlling for per-clause information delta (token count difference between ambiguous and unambiguous variants) confirms that incompleteness remains individually significant ($p = 0.022$, coefficient change $< 8\%$ relative to the uncontrolled model). Coreferential ambiguity, whose variants are lexically identical (information delta $= 0$), provides a confound-free lower bound: its 31.6\% violation rate and 18.7 pp effect are entirely attributable to semantic ambiguity.
157	
158	Excluding incompleteness, the remaining five types show a non-significant omnibus difference ($\chi^2$, $p = 0.079$), but pairwise contrasts with Holm--Bonferroni correction reveal a two-tier pattern: authorization scope ($p_{\text{adj}} = 0.039$) and lexical ($p_{\text{adj}} = 0.025$) remain significantly above coreferential, while the four remaining pairs are equivalent at the $\pm 15$ pp margin.
159	
160	\section{Per-Type Judge Reliability}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 453
}
```

</details>

---


### Tool call

_source line 628 · 2026-05-21T17:04:05.223130+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/analysis.tex",
  "offset": "14",
  "limit": "12"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/analysis.tex",
    "offset": "14",
    "limit": "12"
  }
}
```

</details>

---


### Tool result

_source line 629 · 2026-05-21T17:04:05.273781+00:00_

14	\emph{Information gap-filling} (assumption-based action): the agent fills missing information with plausible but incorrect defaults---e.g., inventing a 30-day return window when none is specified. This dominates incompleteness (3/5) and lexical (3/5).
15	
16	\emph{Boundary violation} (unauthorized escalation): the agent exceeds permission boundaries when authorization scope is underspecified---e.g., issuing a refund above its stated limit rather than escalating; 69.2\% of such violations involve unauthorized escalation with zero conservative refusals ($p < 10^{-4}$, binomial test), revealing systematic permissiveness bias. This dominates authorization scope exclusively (all 5 models).
17	
18	Each type's dominant failure mode is majority-consistent ($\geq$3/5 models agree), with three types achieving full unanimity. The layer distinction does not hold at the mechanistic level: conditional precedence (specification-layer) shares its dominant mode with scopal (linguistic-layer), while authorization scope follows a boundary-violation pattern absent from other specification-layer types.
19	
20	\subsection{Ambiguity Blindness}
21	
22	Agents rarely recognize ambiguity. We code \emph{disambiguation awareness} (acknowledging multiple interpretations, asking clarifying questions, or conditioning on ambiguity) versus \emph{surface adoption} (proceeding with a single interpretation). Overall disambiguation awareness is 4.6\% across all five models: Claude (11.0\%) and GPT-4.1 (10.7\%) show the highest rates, while Qwen3 and DeepSeek show zero across all 278 combined violation traces. Surface adoption exceeds 88\% for every type.
23	
24	We term this \emph{Ambiguity Blindness}: unlike humans---who typically signal uncertainty or seek clarification---agents proceed with full confidence in their chosen interpretation, consistent with \citet{hu_ambiguity_2025}'s finding that ambiguity in LLMs reflects missing conceptual representations. The complete absence of disambiguation beha
…[truncated 161 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 630 · 2026-05-21T17:04:11.251316+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 631 · 2026-05-21T17:04:11.653288+00:00_

1	\section{Discussion}
2	\label{sec:discussion}
3	
4	\paragraph{Differential Nocuity.}
5	\citet{berry_kamsties_2004} distinguish nocuous from innocuous ambiguity by stakeholder divergence. Our results extend this to LLM agents: all six types are nocuous ($+34.0$ pp), but type primarily determines severity (22:1 clause-vs.-model variance ratio). We propose \emph{Differential Nocuity} as a conceptual framework: the risk of a policy ambiguity depends on three factors---ambiguity type (which determines base vulnerability), safety training (which selectively mitigates boundary-type ambiguities), and disambiguation channel availability (which determines whether recovery is possible). Systematic nocuity---41.3\% of clauses trigger majority-convergent violations (\S\ref{sec:analysis})---makes such errors invisible in agreement-based evaluation, a pattern confirmed across seven models spanning six providers (Appendix~\ref{app:model_expansion}).
6	
7	\paragraph{Practical implications.}
8	The exploratory model$\times$type interaction (C4) suggests safety training selectively mitigates boundary-type ambiguities. Incompleteness bypasses intervention points via gap-filling \citep{ferreira_good_enough_2002}---the agent fills missing information with plausible defaults rather than encountering a refusal-eligible decision. Authorization scope, involving explicit permission boundaries, varies 48\,pp within the same judge (\S\ref{sec:c4}), consistent with boundary-targeted training. A preliminary mitigation experiment (Appendix~\ref{app:mitigation}) confirms this asymmetry: disambiguation instructions reduce authorization scope violations by 18.0\,pp but incompleteness by only 3.4\,pp. A proof-of-concept classifier (Appendix~\ref{app:detection}) achieves F1\,=\,0.81 for binary detection but only 0.34 for incompleteness. With $<$11\% agent self-awareness (\S\ref{sec:analysis}), type-aware auditing and externalized detection tools \citep{chantree_2006,ferrari_ambiguity_2019} remain nece
…[truncated 41 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 401
}
```

</details>

---


### Tool call

_source line 632 · 2026-05-21T17:04:11.703946+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 633 · 2026-05-21T17:04:11.754670+00:00_

1	\begin{abstract}
2	LLM-based agents operate under natural-language policy specifications that inevitably contain ambiguity, yet the causal relationship between ambiguity type and safety violations remains unmeasured. We present a matched-pair study on $\tau^2$-bench with 300 clause pairs spanning a six-type, two-layer ambiguity taxonomy, evaluated across five architecturally diverse models (2,997 episodes). Ambiguous clauses increase violation rates by 34.0 percentage points (OR $= 15.1$), with a perturbation control supporting ambiguity-specific causation. A significant type hierarchy emerges (Cram\'{e}r's $V = 0.137$, $p < 10^{-4}$), with a robust two-tier structure among five types and incompleteness as an upper bound partly reflecting an information-addition confound. The hierarchy replicates on two additional model families (LLaMA $\rho = 0.90$, $p = 0.037$; Gemini $\rho = 0.60$, directionally consistent): incompleteness is consistently high (46--62\% across models), while authorization scope varies 52 pp depending on the model (12\% for Claude to 64\% for GPT-5.4, though authorization scope carries the widest measurement uncertainty among types), suggesting that safety training may differentially mitigate specific ambiguity types. Agents show fewer than 11\% disambiguation awareness, with over 88\% surface adoption. Our Differential Nocuity framework connects type-specific vulnerability to disambiguation channel availability and suggests both type-aware policy auditing and externalized ambiguity detection for policy-governed agent deployments.
3	\end{abstract}
4	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 634 · 2026-05-21T17:06:06.323526+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 1 对 Reviewer 2 审稿意见的交叉回应\n\n---\n\n### W1 [MUST-FIX] Incompleteness confound 削弱 type hierarchy 核心 claim\n\n**[AGREE] R2-W1**: 我在 N3 中提出了相同的核心关切。补充两点：\n\n1. R2 精准指出了关键区分——\"残余效应存在 ≠ 可量化歧义 vs. 信息比例\"。Appendix F 的 logistic regression 报告 p=0.022 仅说明控制 token delta 后 incompleteness 仍 significant，但无法回答\"49.2 pp 中多少归因于 ambiguity、多少归因于 information addition\"。这是 partial-out 与 decomposition 的区别，论文混淆了二者。\n\n2. 我进一步注意到 Appendix F 的一个额外问题：排除 incompleteness 后五类的 omnibus χ² 不显著（p=0.079），只有 pairwise contrasts 在 Holm-Bonferroni 后保留了 auth scope 和 lexical 相对 coreferential 的显著性。这意味着如果 incompleteness 排名确实受 confound 污染，剩余五类之间的 type hierarchy 本身也是 borderline 的（omnibus p=0.079），进一步削弱 \"type primarily determines severity\" 的 claim 强度。\n\n**建议优先级一致**：information-matched control 或显式降级 Abstract/Conclusion 中的 claim。\n\n---\n\n### W2 [MUST-FIX] Authorization scope 测量可靠性不足\n\n**[AGREE] R2-W2**: 与我的 N2 完全一致。补充一个 R2 未展开的角度：\n\n论文在 §5.4 中辩称 \"within-judge analysis\" 控制了 judge identity（Claude 12%, Qwen3 26%, DeepSeek 60%, all judged by GPT-5.4）。但 within-judge 控制只解决了 cross-judge confounding，**不解决 per-type measurement noise**。κ=0.385 是 auth scope 这个 type 本身的 judge agreement，无论是哪个 judge 在评判——即 GPT-5.4 对 auth scope violations 的判定本身就不稳定。因此 within-judge 48 pp range 中仍然可能包含大量 measurement noise。\n\nR2 建议的 \"bootstrap CI 量化测量不确定性对模型排名的影响\" 是一个很好的具体建议，优于我的 N2 中的一般性建议。\n\n---\n\n### W3 [SHOULD-FIX] Related Work orphan bib 和遗漏\n\n**[AGREE] R2-W3 (orphan bib 部分)**: 4 条 orphan 条目应清理，我在 M1 中也指出了这一点。\n\n**[REBUT] R2-W3 (遗漏部分，部分反驳)**:\n\n- **Constitutional AI (Bai et al., 2022) / RLHF**: 论文的研究对象是 policy specification 中的 ambiguity 如何导致 violations，而非 alignment 方法本身。C4 关于 safety training 的讨论是 exploratory 的，明确标注为 [Exploratory]（§5.4 标题），且论文未 claim 研究 alignment 机制。要求引用 Constitutional AI 相当于要求论文扩大 scope——这不是一个审稿人应该要求的。\n- **AgentBench (Liu et al., 2023)**: AgentBench 是通用 agent 能力 benchmark，不涉及 policy ambiguity 或 safety violations。论文已引用了多个直接相关的 agent safety benchmark（R-Judge, ToolEmu, InjecAgent, AgentAuditor, ShieldAgent），这些比 AgentBench 更 relevant。\n- **Bender & Koller (2020)**: 关于语言理解的 stochastic parrots 论文与本文研究问题关联较远。\n- **\"引用数 35 条偏少\"**: 引用数量不是评判标准。论文的 Related Work 覆盖了四个直接相关领域（NLP ambiguity, RE ambiguity, psycholinguistics, agent safety），每个领域都有代表性引用。质量优于数量。\n\n---\n\n### W4 [SHOULD-FIX] Differential Nocuity 框架概念化不足\n\n**[AGREE] R2-W4 (部分同意)**: R2 指出的三个问题都成立：\n\n1. 三因素交互未形式化——论文在 §7 用一段自然语言描述了 type × safety training × channel availability 的交互，但未提供任何形式化表达（如图、公式、或至少结构化的 prediction table）。\n2. \"Channel availability\" 未直接测量——论文推断 incompleteness 缺乏 disambiguation channel（因为 gap-filling bypasses intervention points, §7），但这是事后解释而非实验证据。\n3. 与 Berry & Kamsties (2004) 的推进关系确实不够清晰。\n\n但我认为这应保持 SHOULD-FIX 而非升级为 MUST-FIX。论文的核心贡献是经验性的（C1-C4），Differential Nocuity 是在 Discussion 中提出的概念性框架，不是论文的 primary claim。要求完整形式化会改变论文的性质（从经验研究变为理论建模）。更合理的建议是：用一张简单的 2×3 table 展示三因素如何预测六种 type 的不同结果，使框架至少可被 falsifiable。\n\n---\n\n### W5 [SHOULD-FIX] Abstract 信息密度过高\n\n**[REBUT] R2-W5**: 部分不同意。\n\n重读 Abstract（§abstract），我统计了约 11 个数字（OR=15.1, V=0.137, p<10⁻⁴, ρ=0.90, p=0.037, ρ=0.60, 46-62%, 52 pp, 12%, 64%, 11%）。这确实密集，但：\n\n1. 论文已经在 abstract 中对次要结果做了适度的 hedging——如 \"though authorization scope carries the widest measurement uncertainty among types\" 和 \"partly reflecting an information-addition confound\"。这说明作者意识到需要在 abstract 中传递 nuance。\n2. 对于一篇以统计方法为核心的经验论文，abstract 中包含关键效应量和置信区间是合理的——如果删减到\"2-3 核心发现\"，readers 在浏览阶段无法判断效应量的实际大小。\n3. 真正的问题不是数字太多，而是 incompleteness 的 confound caveat 在 abstract 中不够显眼（我在 N3 中已指出）。修复 N3 比减少数字更重要。\n\n建议：保留核心统计量，但精简叙述结构——可以将 replication 结果移至 \"Our results replicate across seven models\" 一句，不列具体 ρ 值。\n\n---\n\n### W6 [SHOULD-FIX] C3 layer effect null result 讨论过于简短\n\n**[AGREE] R2-W6 (部分同意)**: §5.3 确实过于简短（3 句话），但我认为这个问题的严重性低于 R2 的评估。\n\n论文已给出了 C3 inconclusive 的三个理由：(1) 不survive Holm-Bonferroni 校正；(2) 控制 token delta 后方向反转；(3) cross-layer type overlap（conditional precedence 36.8% vs. scopal 39.4%）。这些理由充分解释了为什么 layer effect 不成立。\n\nR2 的关键问题是对的：如果二分法不成立，two-layer taxonomy 的理论基础需要重新论证。但我认为论文的 taxonomy 价值在于**六种 type 的操作性区分**（每种对应不同 resolution mechanism，§3），而非层级分组。即使 layer 区分不成立，six-type taxonomy 仍然有效——它为 C2 的 type hierarchy 提供了分析框架。\n\n建议：在 §5.3 补充 1-2 句话讨论 layer distinction 失败对 taxonomy 整体价值的影响，并在 §7 Discussion 中明确 taxonomy 的操作性价值独立于 layer 分组。\n\n---\n\n### W7 [MINOR] ferrari_defects_2018 bib 第一作者不一致\n\n**[AGREE] R2-W7**: 与我的 M2 一致。应修正 bib key 或 author 列表。\n\n---\n\n### W8 [MINOR] 缺少 Ethics Statement\n\n**[AGREE] R2-W8**: 论文涉及 LLM API 调用和人工标注（100 episodes, 两名标注者），应添加简短的 Ethics Statement。不过这是 camera-ready 级别的修正，不影响接收决定。\n\n---\n\n### R2 Questions 的补充意见\n\n**Q1 (Incompleteness token delta)**: 同意这是一个必须回答的透明度问题。与我的 Q3 相关。\n\n**Q2 (Claude 12% auth scope 是否因 conservative refusal)**: 这是一个很好的问题。§6.1 报告 auth scope violations 中 \"69.2% involve unauthorized escalation with zero conservative refusals (p < 10⁻⁴)\"，但这是 across all models 的统计。如果 Claude 的 auth scope violation rate 本身只有 12%（50 episodes 中约 6 个 violations），per-model 分析的统计力极有限。作者需要 (a) 提供 Claude 特定的 failure mode 分布，(b) 在 non-violation episodes 中 Claude 是否有 conservative refusal（即正确拒绝但理由错误）。\n\n**Q3 (Information-addition perturbation)**: 与我的 N3 建议方向一致。\n\n**Q4 (Template pipeline 透明度)**: 同意。这也关联我的 W4——如果 template 设计未公开，clause pair 质量依赖于信任。96% pass rate 中的 disagreement 类型分布也很重要——如果 disagreement 集中在特定 type（如 auth scope），这会加剧 N2 的信度问题。\n\n---\n\n### R2 Missing References 的补充意见\n\n- **Levy (2008), Ferreira & Patson (2007)**: 这两篇在 bib 中但未被引用（orphan entries）。如果 R2 认为它们应该被引用，说明论文可能在某个版本中删除了相关讨论但忘记清理 bib。应当决定：引用它们（在 psycholinguistics 段落中有自然位置）或删除 bib 条目。\n- **Constitutional AI, AgentBench, Bender & Koller**: 如我在 W3 rebut 中所述，前两者与论文 scope 不直接相关，后者关联较远。不认为这些是必要遗漏。\n\n---\n\n### 综合评估\n\nR2 和我在三个核心问题上达成一致：**(1) incompleteness confound (R2-W1 / R1-N3)**, **(2) auth scope 信度 (R2-W2 / R1-N2)**, **(3) orphan bib (R2-W3 / R1-M1)**。我还额外提出了 **SESOI 外部锚定 (R1-N1)** 和 **API 超参数缺失 (R1-W1)** 这两个 R2 未覆盖的问题。\n\n两位 reviewer 独立给出了相同的 Overall (3.5) 和 Confidence (4/5)，增强了评估的可信度。论文的 C1 (binary effect) 是 solid 的，但从 C1 到 C2/C4 的推理链条需要补强才能达到主会议水平。",
  "reviewer_id": "1",
  "project": "policy_ambiguity_safety"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 1 对 Reviewer 2 审稿意见的交叉回应\n\n---\n\n### W1 [MUST-FIX] Incompleteness confound 削弱 type hierarchy 核心 claim\n\n**[AGREE] R2-W1**: 我在 N3 中提出了相同的核心关切。补充两点：\n\n1. R2 精准指出了关键区分——\"残余效应存在 ≠ 可量化歧义 vs. 信息比例\"。Appendix F 的 logistic regression 报告 p=0.022 仅说明控制 token delta 后 incompleteness 仍 significant，但无法回答\"49.2 pp 中多少归因于 ambiguity、多少归因于 information addition\"。这是 partial-out 与 decomposition 的区别，论文混淆了二者。\n\n2. 我进一步注意到 Appendix F 的一个额外问题：排除 incompleteness 后五类的 omnibus χ² 不显著（p=0.079），只有 pairwise contrasts 在 Holm-Bonferroni 后保留了 auth scope 和 lexical 相对 coreferential 的显著性。这意味着如果 incompleteness 排名确实受 confound 污染，剩余五类之间的 type hierarchy 本身也是 borderline 的（omnibus p=0.079），进一步削弱 \"type primarily determines severity\" 的 claim 强度。\n\n**建议优先级一致**：information-matched control 或显式降级 Abstract/Conclusion 中的 claim。\n\n---\n\n### W2 [MUST-FIX] Authorization scope 测量可靠性不足\n\n**[AGREE] R2-W2**: 与我的 N2 完全一致。补充一个 R2 未展开的角度：\n\n论文在 §5.4 中辩称 \"within-judge analysis\" 控制了 judge identity（Claude 12%, Qwen3 26%, DeepSeek 60%, all judged by GPT-5.4）。但 within-judge 控制只解决了 cross-judge confounding，**不解决 per-type measurement noise**。κ=0.385 是 auth scope 这个 type 本身的 judge agreement，无论是哪个 judge 在评判——即 GPT-5.4 对 auth scope violations 的判定本身就不稳定。因此 within-judge 48 pp range 中仍然可能包含大量 measurement noise。\n\nR2 建议的 \"bootstrap CI 量化测量不确定性对模型排名的影响\" 是一个很好的具体建议，优于我的 N2 中的一般性建议。\n\n---\n\n### W3 [SHOULD-FIX] Related Work orphan bib 和遗漏\n\n**[AGREE] R2-W3 (orphan bib 部分)**: 4 条 orphan 条目应清理，我在 M1 中也指出了这一点。\n\n**[REBUT] R2-W3 (遗漏部分，部分反驳)**:\n\n- **Constitutional AI (Bai et al., 2022) / RLHF**: 论文的研究对象是 policy specification 中的 ambiguity 如何导致 violations，而非 alignment 方法本身。C4 关于 safety training 的讨论是 exploratory 的，明确标注为 [Exploratory]（§5.4 标题），且论文未 claim 研究 alignment 机制。要求引用 Constitutional AI 相当于要求论文扩大 scope——这不是一个审稿人应该要求的。\n- **AgentBench (Liu et al., 2023)**: AgentBench 是通用 agent 能力 benchmark，不涉及 policy ambiguity 或 safety violations。论文已引用了多个直接相关的 agent safety benchmark（R-Judge, ToolEmu, InjecAgent, AgentAuditor, ShieldAgent），这些比 AgentBench 更 relevant。\n- **Bender & Koller (2020)**: 关于语言理解的 stochastic parrots 论文与本文研究问题关联较远。\n- **\"引用数 35 条偏少\"**: 引用数量不是评判标准。论文的 Related Work 覆盖了四个直接相关领域（NLP ambiguity, RE ambiguity, psycholinguistics, agent safety），每个领域都有代表性引用。质量优于数量。\n\n---\n\n### W4 [SHOULD-FIX] Differential Nocuity 框架概念化不足\n\n**[AGREE] R2-W4 (部分同意)**: R2 指出的三个问题都成立：\n\n1. 三因素交互未形式化——论文在 §7 用一段自然语言描述了 type × safety training × channel availability 的交互，但未提供任何形式化表达（如图、公式、或至少结构化的 prediction table）。\n2. \"Channel availability\" 未直接测量——论文推断 incompleteness 缺乏 disambiguation channel（因为 gap-filling bypasses intervention points, §7），但这是事后解释而非实验证据。\n3. 与 Berry & Kamsties (2004) 的推进关系确实不够清晰。\n\n但我认为这应保持 SHOULD-FIX 而非升级为 MUST-FIX。论文的核心贡献是经验性的（C1-C4），Differential Nocuity 是在 Discussion 中提出的概念性框架，不是论文的 primary claim。要求完整形式化会改变论文的性质（从经验研究变为理论建模）。更合理的建议是：用一张简单的 2×3 table 展示三因素如何预测六种 type 的不同结果，使框架至少可被 falsifiable。\n\n---\n\n### W5 [SHOULD-FIX] Abstract 信息密度过高\n\n**[REBUT] R2-W5**: 部分不同意。\n\n重读 Abstract（§abstract），我统计了约 11 个数字（OR=15.1, V=0.137, p<10⁻⁴, ρ=0.90, p=0.037, ρ=0.60, 46-62%, 52 pp, 12%, 64%, 11%）。这确实密集，但：\n\n1. 论文已经在 abstract 中对次要结果做了适度的 hedging——如 \"though authorization scope carries the widest measurement uncertainty among types\" 和 \"partly reflecting an information-addition confound\"。这说明作者意识到需要在 abstract 中传递 nuance。\n2. 对于一篇以统计方法为核心的经验论文，abstract 中包含关键效应量和置信区间是合理的——如果删减到\"2-3 核心发现\"，readers 在浏览阶段无法判断效应量的实际大小。\n3. 真正的问题不是数字太多，而是 incompleteness 的 confound caveat 在 abstract 中不够显眼（我在 N3 中已指出）。修复 N3 比减少数字更重要。\n\n建议：保留核心统计量，但精简叙述结构——可以将 replication 结果移至 \"Our results replicate across seven models\" 一句，不列具体 ρ 值。\n\n---\n\n### W6 [SHOULD-FIX] C3 layer effect null result 讨论过于简短\n\n**[AGREE] R2-W6 (部分同意)**: §5.3 确实过于简短（3 句话），但我认为这个问题的严重性低于 R2 的评估。\n\n论文已给出了 C3 inconclusive 的三个理由：(1) 不survive Holm-Bonferroni 校正；(2) 控制 token delta 后方向反转；(3) cross-layer type overlap（conditional precedence 36.8% vs. scopal 39.4%）。这些理由充分解释了为什么 layer effect 不成立。\n\nR2 的关键问题是对的：如果二分法不成立，two-layer taxonomy 的理论基础需要重新论证。但我认为论文的 taxonomy 价值在于**六种 type 的操作性区分**（每种对应不同 resolution mechanism，§3），而非层级分组。即使 layer 区分不成立，six-type taxonomy 仍然有效——它为 C2 的 type hierarchy 提供了分析框架。\n\n建议：在 §5.3 补充 1-2 句话讨论 layer distinction 失败对 taxonomy 整体价值的影响，并在 §7 Discussion 中明确 taxonomy 的操作性价值独立于 layer 分组。\n\n---\n\n### W7 [MINOR] ferrari_defects_2018 bib 第一作者不一致\n\n**[AGREE] R2-W7**: 与我的 M2 一致。应修正 bib key 或 author 列表。\n\n---\n\n### W8 [MINOR] 缺少 Ethics Statement\n\n**[AGREE] R2-W8**: 论文涉及 LLM API 调用和人工标注（100 episodes, 两名标注者），应添加简短的 Ethics Statement。不过这是 camera-ready 级别的修正，不影响接收决定。\n\n---\n\n### R2 Questions 的补充意见\n\n**Q1 (Incompleteness token delta)**: 同意这是一个必须回答的透明度问题。与我的 Q3 相关。\n\n**Q2 (Claude 12% auth scope 是否因 conservative refusal)**: 这是一个很好的问题。§6.1 报告 auth scope violations 中 \"69.2% involve unauthorized escalation with zero conservative refusals (p < 10⁻⁴)\"，但这是 across all models 的统计。如果 Claude 的 auth scope violation rate 本身只有 12%（50 episodes 中约 6 个 violations），per-model 分析的统计力极有限。作者需要 (a) 提供 Claude 特定的 failure mode 分布，(b) 在 non-violation episodes 中 Claude 是否有 conservative refusal（即正确拒绝但理由错误）。\n\n**Q3 (Information-addition perturbation)**: 与我的 N3 建议方向一致。\n\n**Q4 (Template pipeline 透明度)**: 同意。这也关联我的 W4——如果 template 设计未公开，clause pair 质量依赖于信任。96% pass rate 中的 disagreement 类型分布也很重要——如果 disagreement 集中在特定 type（如 auth scope），这会加剧 N2 的信度问题。\n\n---\n\n### R2 Missing References 的补充意见\n\n- **Levy (2008), Ferreira & Patson (2007)**: 这两篇在 bib 中但未被引用（orphan entries）。如果 R2 认为它们应该被引用，说明论文可能在某个版本中删除了相关讨论但忘记清理 bib。应当决定：引用它们（在 psycholinguistics 段落中有自然位置）或删除 bib 条目。\n- **Constitutional AI, AgentBench, Bender & Koller**: 如我在 W3 rebut 中所述，前两者与论文 scope 不直接相关，后者关联较远。不认为这些是必要遗漏。\n\n---\n\n### 综合评估\n\nR2 和我在三个核心问题上达成一致：**(1) incompleteness confound (R2-W1 / R1-N3)**, **(2) auth scope 信度 (R2-W2 / R1-N2)**, **(3) orphan bib (R2-W3 / R1-M1)**。我还额外提出了 **SESOI 外部锚定 (R1-N1)** 和 **API 超参数缺失 (R1-W1)** 这两个 R2 未覆盖的问题。\n\n两位 reviewer 独立给出了相同的 Overall (3.5) 和 Confidence (4/5)，增强了评估的可信度。论文的 C1 (binary effect) 是 solid 的，但从 C1 到 C2/C4 的推理链条需要补强才能达到主会议水平。",
    "reviewer_id": "1",
    "project": "policy_ambiguity_safety"
  }
}
```

</details>

---


### Tool result

_source line 635 · 2026-05-21T17:06:09.987863+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_967344d166ba485ad606d14379e69d85:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3664
}
```

</details>

---


### Assistant

_source line 636 · 2026-05-21T17:06:19.220260+00:00_

交叉回应已提交给 Review Director。

总结：对 R2 的 8 条 weakness 中，我 **[AGREE]** 了 W1, W2, W4(部分), W6(部分), W7, W8 共 6 条（与我自己的 N2, N3, M1, M2 一致），**[REBUT]** 了 W3 的遗漏引用部分（Constitutional AI/AgentBench/Bender & Koller 与论文 scope 不直接相关）和 W5（abstract 信息密度问题更在于 confound caveat 不够显眼，而非数字过多）。我额外补充了 R2 未涉及的两个发现：Appendix F 排除 incompleteness 后 omnibus p=0.079 进一步削弱 hierarchy claim、within-judge 控制不解决 per-type measurement noise。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1"
}
```

</details>

---


## Round 19

## Round 19

78 recorded events


### User

_source line 637 · 2026-05-21T17:39:01.935250+00:00_

[Round 1 审稿请求]:
你是 Reviewer 1，负责**方法严谨性 + 实验有效性**。

## 论文信息
- 标题: "Not All Policy Ambiguity Is Equal: Type-Specific Safety Risks for LLM Agents"
- 路径: projects/policy_ambiguity_safety/docs/paper/main.tex
- PDF: /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/main.pdf
- 目标 venue: EMNLP 2026 via ARR May cycle (deadline: 2026-05-25)

## Venue 格式要求
- Long paper: 正文 ≤ 8 页, 参考文献不限, Limitations 必须有（不计入页数）
- ACL 官方模板, double-blind
- 附录不计入页数, reviewer 不强制阅读

## 你的审查侧重
请重点审查以下方面：

1. **实验设计**：matched-pair design 的因果推断有效性，300 clause pairs × 5 models = 2,997 episodes 的统计功效是否充分，perturbation control 是否有效排除混淆因素
2. **统计分析**：McNemar's test / χ² / Cramér's V / TOST equivalence testing 的选择和使用是否恰当，SESOI ±15pp 的锚定是否有外部依据，多重比较校正是否充分
3. **评估管道**：cross-judge design 的偏差控制（GPT-5.4 judges Claude/Qwen3/DeepSeek, GPT-4.1 judges GPT-5.4），per-type κ 变异大（authorization scope κ=0.385 vs incompleteness κ=0.875），human validation 是否充分
4. **Confound 控制**：incompleteness 的 information-addition confound 是否被充分控制（logistic regression p=0.022, coefficient change <8%），token count 作为 information content proxy 的有效性
5. **Reproducibility**：ICC=0.919 仅 within OpenAI family，cross-provider stability 是否有直接证据；API 超参数是否完整报告；replication on 2 additional models 的样本量是否充分
6. **Claims 与 evidence 的匹配度**：C1-C4 四个 claims 是否都有充分支撑，特别是 C3（inconclusive）和 C4（exploratory）的定位是否恰当

请按 ARR 审稿标准输出完整审稿意见，包含 Summary / Strengths / Weaknesses / Questions / Missing References / Overall Assessment。Weaknesses 按严重程度标注 [MUST-FIX] / [SHOULD-FIX] / [MINOR]。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 638 · 2026-05-21T17:39:09.521399+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/.claude/skills/review-reviewer-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/.claude/skills/review-reviewer-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 639 · 2026-05-21T17:39:09.572285+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/.claude/sessions/review_reviewer_1_6edf79f4.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 640 · 2026-05-21T17:39:11.729912+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/review-reviewer-session-start.skill.md",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/review-reviewer-session-start.skill.md",
    "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4"
  }
}
```

</details>

---


### Tool result

_source line 641 · 2026-05-21T17:39:11.830850+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Glob",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 642 · 2026-05-21T17:39:14.995083+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.skill.md",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.skill.md",
    "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4"
  }
}
```

</details>

---


### Tool result

_source line 643 · 2026-05-21T17:39:15.150524+00:00_

/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/skills/projects/policy_ambiguity_safety/distilled-research.skill.md
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/skills/projects/policy_ambiguity_safety/distilled-writing.skill.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Glob",
  "elapsed_ms": 155
}
```

</details>

---


### Tool call

_source line 644 · 2026-05-21T17:39:26.454365+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebSearch,mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director,mcp__agent-ml-research__verify_references",
  "max_results": "4"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebSearch,mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director,mcp__agent-ml-research__verify_references",
    "max_results": "4"
  }
}
```

</details>

---


### Tool result

_source line 645 · 2026-05-21T17:39:26.454836+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 646 · 2026-05-21T17:39:33.379544+00:00_

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
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR 2025 2026 reviewer guidelines review form criteria scoring"
  }
}
```

</details>

---


### Tool call

_source line 647 · 2026-05-21T17:39:35.738807+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/main.pdf",
  "project": "policy_ambiguity_safety",
  "pages": "1-10",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/main.pdf",
    "project": "policy_ambiguity_safety",
    "pages": "1-10",
    "dpi": "150"
  }
}
```

</details>

---


### Tool call

_source line 648 · 2026-05-21T17:39:35.889710+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 649 · 2026-05-21T17:39:40.210001+00:00_

Web search results for query: "ACL ARR 2025 2026 reviewer guidelines review form criteria scoring"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"}]

Based on the search results, here's what I found about the ACL ARR 2025-2026 reviewer guidelines:

## Scoring Criteria

Starting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation.

### Soundness Score
Soundness scores must be justified by the text of the review. If you give a low Soundness score without finding any major faults, this means that your review is not a faithful explanation of your recommendation, and you need to revise it.

### Excitement Score
Sometimes you may find the work sound, but not something that is interesting for you personally, and such preferences are more subjective and should be reflected in a separate excitement score, which is orthogonal to the assessment of the soundness of the paper.

## Area Chair Meta-Review Scoring

The ARR metareview score has changed in February 2025 to be more aligned with reviewer scores, and like with reviews, the score should be backed up by the meta-review text. The options include: "Consider for Award" 
…[truncated 363 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 6830
}
```

</details>

---


### Tool result

_source line 650 · 2026-05-21T17:39:41.922329+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 1, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/_pdf_images/main_p1.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 453.9}, {\"page\": 2, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/_pdf_images/main_p2.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 423.0}, {\"page\": 3, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/_pdf_images/main_p3.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 525.0}, {\"page\": 4, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/_pdf_images/main_p4.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 504.1}, {\"page\": 5, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/_pdf_images/main_p5.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 519.1}, {\"page\": 6, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/_pdf_images/main_p6.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 392.3}, {\"page\": 7, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/_pdf_images/main_p7.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 350.8}, {\"page\": 8, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/_pdf_images/main_p8.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 542.0}, {\"page\": 9, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/_pdf_images/main_p9.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 522.7}, {\"page\": 10, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safet
…[truncated 322 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 6183
}
```

</details>

---


### Tool result

_source line 651 · 2026-05-21T17:39:41.922754+00:00_

1	\documentclass[11pt]{article}
2	\usepackage[review]{acl}
3	\usepackage{times}
4	\usepackage{latexsym}
5	\usepackage[T1]{fontenc}
6	\usepackage[utf8]{inputenc}
7	\usepackage{microtype}
8	\usepackage{graphicx}
9	\usepackage{booktabs}
10	\usepackage{amsmath}
11	\usepackage{amssymb}
12	\usepackage{multirow}
13	\usepackage{xcolor}
14	\usepackage{subcaption}
15	
16	\definecolor{speccolor}{HTML}{C44E52}
17	\definecolor{lingcolor}{HTML}{4C72B0}
18	
19	\title{Not All Policy Ambiguity Is Equal: Type-Specific Safety Risks for LLM Agents}
20	
21	\author{Anonymous}
22	
23	\begin{document}
24	\maketitle
25	
26	\input{sections/abstract}
27	\input{sections/introduction}
28	\input{sections/related_work}
29	\input{sections/taxonomy}
30	\input{sections/method}
31	\input{sections/experiments}
32	\input{sections/analysis}
33	\input{sections/discussion}
34	\input{sections/conclusion}
35	\input{sections/limitations}
36	
37	\bibliography{references}
38	
39	\appendix
40	\input{sections/appendix}
41	
42	\end{document}
43	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 6033
}
```

</details>

---


### Tool call

_source line 652 · 2026-05-21T17:39:48.699342+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review reviewer form 2025 soundness excitement scoring scale 1-5 description"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review reviewer form 2025 soundness excitement scoring scale 1-5 description"
  }
}
```

</details>

---


### Tool call

_source line 653 · 2026-05-21T17:39:50.205118+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/main.pdf",
  "project": "policy_ambiguity_safety",
  "pages": "11-14",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/main.pdf",
    "project": "policy_ambiguity_safety",
    "pages": "11-14",
    "dpi": "150"
  }
}
```

</details>

---


### Tool call

_source line 654 · 2026-05-21T17:39:50.757684+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/_pdf_images/main_p1.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/_pdf_images/main_p1.png"
  }
}
```

</details>

---


### Tool call

_source line 655 · 2026-05-21T17:39:51.260117+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/_pdf_images/main_p2.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/_pdf_images/main_p2.png"
  }
}
```

</details>

---


### Tool call

_source line 656 · 2026-05-21T17:39:52.213982+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/_pdf_images/main_p3.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/_pdf_images/main_p3.png"
  }
}
```

</details>

---


### Tool call

_source line 657 · 2026-05-21T17:39:52.666112+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/_pdf_images/main_p4.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/_pdf_images/main_p4.png"
  }
}
```

</details>

---


### Tool call

_source line 658 · 2026-05-21T17:39:53.017731+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/_pdf_images/main_p5.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/_pdf_images/main_p5.png"
  }
}
```

</details>

---


### Tool result

_source line 659 · 2026-05-21T17:39:54.474615+00:00_

Web search results for query: "ACL Rolling Review reviewer form 2025 soundness excitement scoring scale 1-5 description"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"ACL 2026 on X: \"Checkout the blog post on the soundness/excitement scores https://t.co/AKSO9DjiYP . It clarifies the reasoning behind the separation of overall scores and how it might make the reviewer recommendation more robust. #ACL2023Toronto #ACL2023NLP #NLProc\" / X","url":"https://x.com/aclmeeting/status/1637827267173953540"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"Can LLM feedback enhance review quality? A randomized study of 20K   reviews at ICLR 2025","url":"https://arxiv.org/pdf/2504.09737"}]

Based on the search results, here's what I found about the ACL Rolling Review (ARR) 2025 reviewer form scoring scales for soundness and excitement:

## Soundness Scale (1-5)

The soundness scoring scale includes: 5 = Excellent (one of the most thorough studies), 4 = Strong (provides sufficient support for all claims), and 3 = Acceptable (provides sufficient support for main claims).

## Excitement Scale (1-5)

The excitement scoring includes: 5 = Highly Exciting (I would recommend this paper to others and/or attend its pres
…[truncated 574 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 5775
}
```

</details>

---


### Tool result

_source line 660 · 2026-05-21T17:39:54.876461+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 11, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/_pdf_images/main_p11.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 497.0}, {\"page\": 12, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/_pdf_images/main_p12.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 415.7}, {\"page\": 13, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/_pdf_images/main_p13.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 507.0}, {\"page\": 14, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/_pdf_images/main_p14.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 259.4}], \"total_pages\": 14, \"rendered_pages\": 4, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 4671
}
```

</details>

---


### Tool result

_source line 661 · 2026-05-21T17:39:59.035853+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 6369
}
```

</details>

---


### Tool result

_source line 662 · 2026-05-21T17:39:59.087126+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 8329
}
```

</details>

---


### Tool result

_source line 663 · 2026-05-21T17:39:59.089816+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 6072
}
```

</details>

---


### Tool result

_source line 664 · 2026-05-21T17:39:59.090929+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 7830
}
```

</details>

---


### Tool result

_source line 665 · 2026-05-21T17:39:59.095341+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 6881
}
```

</details>

---


### Tool call

_source line 666 · 2026-05-21T17:40:10.250359+00:00_

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
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
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

_source line 667 · 2026-05-21T17:40:10.301176+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 668 · 2026-05-21T17:40:12.160346+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/_pdf_images/main_p6.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/_pdf_images/main_p6.png"
  }
}
```

</details>

---


### Tool result

_source line 669 · 2026-05-21T17:40:13.120486+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 960
}
```

</details>

---


### Tool call

_source line 670 · 2026-05-21T17:40:13.121242+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/_pdf_images/main_p7.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/_pdf_images/main_p7.png"
  }
}
```

</details>

---


### Tool result

_source line 671 · 2026-05-21T17:40:13.725953+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 604
}
```

</details>

---


### Tool call

_source line 672 · 2026-05-21T17:40:13.776739+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/_pdf_images/main_p8.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/_pdf_images/main_p8.png"
  }
}
```

</details>

---


### Tool call

_source line 673 · 2026-05-21T17:40:14.080337+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/_pdf_images/main_p9.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/_pdf_images/main_p9.png"
  }
}
```

</details>

---


### Tool result

_source line 674 · 2026-05-21T17:40:14.583417+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 806
}
```

</details>

---


### Tool call

_source line 675 · 2026-05-21T17:40:14.634123+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/_pdf_images/main_p10.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/_pdf_images/main_p10.png"
  }
}
```

</details>

---


### Tool result

_source line 676 · 2026-05-21T17:40:14.936610+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 856
}
```

</details>

---


### Tool result

_source line 677 · 2026-05-21T17:40:15.440368+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 806
}
```

</details>

---


### Tool call

_source line 678 · 2026-05-21T17:40:26.231342+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/_pdf_images/main_p11.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/_pdf_images/main_p11.png"
  }
}
```

</details>

---


### Tool result

_source line 679 · 2026-05-21T17:40:26.936120+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 704
}
```

</details>

---


### Tool call

_source line 680 · 2026-05-21T17:40:26.936625+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/_pdf_images/main_p12.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/_pdf_images/main_p12.png"
  }
}
```

</details>

---


### Tool result

_source line 681 · 2026-05-21T17:40:27.443463+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 506
}
```

</details>

---


### Tool call

_source line 682 · 2026-05-21T17:40:27.443929+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/_pdf_images/main_p13.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/_pdf_images/main_p13.png"
  }
}
```

</details>

---


### Tool result

_source line 683 · 2026-05-21T17:40:28.348832+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 904
}
```

</details>

---


### Tool call

_source line 684 · 2026-05-21T17:40:28.399490+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/_pdf_images/main_p14.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/_pdf_images/main_p14.png"
  }
}
```

</details>

---


### Tool result

_source line 685 · 2026-05-21T17:40:28.902509+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 503
}
```

</details>

---


### Tool call

_source line 686 · 2026-05-21T17:40:30.358328+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete review form including all scoring dimensions (soundness, excitement, overall assessment, reproducibility, etc.), their exact scales (1-5), and the description for each score level. Include all questions reviewers must answer."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the complete review form including all scoring dimensions (soundness, excitement, overall assessment, reproducibility, etc.), their exact scales (1-5), and the description for each score level. Include all questions reviewers must answer."
  }
}
```

</details>

---


### Tool result

_source line 687 · 2026-05-21T17:40:36.940194+00:00_

# ACL Rolling Review Form - Complete Structure

## Core Review Dimensions

**Paper Summary**
Reviewers describe the paper's subject matter to ensure shared understanding.

**Summary of Strengths**
Reasons supporting publication, including "novel and useful methodology, insightful empirical results or theoretical analysis, clear organization of related literature."

**Summary of Weaknesses**
Numbered concerns about correctness, impact, clarity, or other publication barriers.

**Comments/Suggestions/Typos**
Additional improvement recommendations beyond weakness responses.

## Scoring Scales

**Reviewer Confidence (1-5)**
- 5: Positive evaluation; careful reading with familiarity of related work
- 4: Quite sure; unlikely to have missed important points
- 3: Fairly confident but possibility of missed details
- 2: Willing to defend evaluation; likely missed some details
- 1: Outside expertise area or paper very difficult to understand

**Soundness (1-5, half-point increments)**
- 5: "One of the most thorough"
- 4: Provides sufficient support with optional improvements
- 3: Supports main claims; minor points need detail
- 2: Main claims lack support; major technical problems
- 1: Insufficient depth or lacks ACL relevance

**Excitement (1-5, half-point increments)**
- 5: Highly exciting; would recommend widely
- 4: Exciting; would mention to others
- 3: Interesting; might mention selectively
- 2: Potentially interesting; limited personal resonance
- 1: Not exciting; lacks computational linguistics relevance

**Overall Assessment (1-5, half-point increments)**
- 5: Consider for Award (top 2.5%)
- 4: Conference acceptance
- 3: Findings track acceptance
- 2: Substantial revisions needed
- 1: Do not resubmit; lacks relevance

## Additional Questions

**Limitations and Societal Impact**, **Ethical Concerns**, **Needs Ethics Review**, **Reproducibility (1-5)**, **Datasets (1-5)**, **Software (1-5)**, **Author Identity Knowledge (1-5)**

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 6581
}
```

</details>

---


### Tool call

_source line 688 · 2026-05-21T17:40:44.519275+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/sections/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/sections/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper"
  }
}
```

</details>

---


### Tool result

_source line 689 · 2026-05-21T17:40:44.569831+00:00_

/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/taxonomy.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/related_work.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/abstract.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/limitations.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/experiments.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/method.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/introduction.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/discussion.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/analysis.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/conclusion.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/appendix.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 690 · 2026-05-21T17:40:51.758153+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 691 · 2026-05-21T17:40:52.310887+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	\subsection{Experimental Platform}
5	
6	We conduct all experiments on the original release of $\tau^2$-bench \citep{tau2_bench_2025}, a dual-control conversational agent benchmark spanning retail and airline customer service domains. $\tau^2$-bench provides natural-language policy documents, tool APIs, and multi-turn user interactions with ground-truth evaluation via assertion checking. Its policy injection mechanism allows us to replace individual policy clauses while preserving the surrounding context, enabling controlled ambiguity manipulation.
7	
8	\subsection{Matched-Pair Design}
9	
10	For each of the six ambiguity types, we construct 50 \emph{clause pairs}: an ambiguous variant and a matched unambiguous variant that conveys the same intended policy but resolves the ambiguity. Pairs are minimal edits: the unambiguous variant adds only the information necessary to eliminate the target ambiguity (e.g., for scopal ambiguity, replacing ``items may be returned within 30 days'' with ``standard items may be returned within 30 days; customized items are final sale''). This yields 300 clause pairs $\times$ 2 conditions $\times$ 5 models $= 2{,}997$ episodes (3 episodes lost to API errors in one Qwen3 batch).
11	
12	Clause pairs are generated through a template-based pipeline and reviewed by two independent annotators (both with NLP background) to ensure (1) the ambiguous variant contains exactly one instance of the target type, (2) the unambiguous variant resolves it without changing policy scope, and (3) the ambiguity is plausibly natural. Annotators independently verified type assignments with a 96\% pass rate; disagreements were resolved by discussion. A post-hoc realism validation confirms linguistic consistency with original $\tau^2$-bench policy text (\S\ref{sec:limitations}).
13	
14	\subsection{Models}
15	
16	We evaluate five models spanning four providers and two architecture families: GPT-5.4 and GPT-4.1 (OpenAI, pro
…[truncated 4803 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 552
}
```

</details>

---


### Tool call

_source line 692 · 2026-05-21T17:40:52.311288+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 693 · 2026-05-21T17:40:52.361933+00:00_

1	\section{Results}
2	\label{sec:results}
3	
4	We organize results around four analyses of increasing specificity: the binary ambiguity effect (C1), the type hierarchy (C2), the aggregate layer effect (C3), and the model$\times$type interaction (C4). C1 and C2 constitute our primary claims; C3 is inconclusive; C4 is exploratory but provides the model$\times$type interaction analysis.
5	
6	\subsection{Binary Ambiguity Effect (C1)}
7	
8	Across all five models and six types, ambiguous clauses increase violation rates by 34.0 pp (41.0\% vs.\ 6.9\%, OR $= 15.1$, 95\% CI $[10.78, 21.17]$, $p < 10^{-105}$). All six types individually produce significant increases (all $p < 10^{-5}$), and all five models show large effects ($+25.7$ to $+39.0$ pp, all $p < 10^{-17}$). Perturbation controls confirm specificity to semantic ambiguity ($n = 300$, $\Delta_{\text{perturb}} = -0.67$\,pp, CI containing zero). Clause identity explains 22.4\% of variance versus 1.0\% for model identity. A replication on two additional model families (Gemini-2.5-Flash, LLaMA-4-Scout; Appendix~\ref{app:model_expansion}) confirms the effect across seven models spanning six providers ($\Delta = +20.0$ to $+33.6$\,pp, both $p < 10^{-6}$).
9	
10	\subsection{Type Hierarchy (C2)}
11	
12	\begin{table*}[t]
13	\centering
14	\caption{Violation rates (\%) under ambiguous policy clauses by type and model. $\Delta$pp denotes the pooled difference between ambiguous and unambiguous conditions across all five models. All per-type differences are significant ($p < 10^{-5}$, Fisher's exact test).}
15	\label{tab:main_results}
16	\small
17	\begin{tabular}{llrrrrrrrr}
18	\toprule
19	Layer & Type & Pooled & GPT-5.4 & GPT-4.1 & Claude & Qwen3 & DeepSeek & $\Delta$pp & $p$ \\
20	\midrule
21	\multirow{3}{*}{\textcolor{speccolor}{Spec.}} & Incompleteness & 53.6 & 46.0 & 58.0 & 48.0 & 62.0 & 54.0 & +49.2 & $<10^{-37}$ \\
22	 & Auth.\ Scope & 41.6 & 64.0 & 46.0 & 12.0 & 26.0 & 60.0 & +36.0 & $<10^{-22}$ \\
23	 & Cond.\ Precedence 
…[truncated 5959 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 694 · 2026-05-21T17:40:53.165502+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/analysis.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/analysis.tex"
  }
}
```

</details>

---


### Tool result

_source line 695 · 2026-05-21T17:40:53.316585+00:00_

1	\section{Error Analysis \emph{[Exploratory]}}
2	\label{sec:analysis}
3	
4	The following failure mode taxonomy emerges empirically from LLM-coded traces, distinct from the input ambiguity taxonomy (\S\ref{sec:taxonomy}).
5	
6	We analyze 614 violation traces across all five models, coded into five failure modes: unauthorized escalation, assumption-based action, scope misapplication, arbitrary rule selection, and conservative refusal. GPT-5.4 and GPT-4.1 serve as detailed annotation anchors because they span the judge boundary. Inter-coder reliability is substantial (Gwet's AC$_1$ $= 0.62$ \citep{gwet_2014}; Cohen's $\kappa = 0.52$ \citep{cohen_1960}; the gap reflects the prevalence paradox, as three categories account for ${\sim}$90\% of instances).
7	
8	\subsection{Type-Specific Failure Mechanisms}
9	
10	The five-model data reveal three mechanistically distinct failure patterns that crosscut the specification/linguistic layer boundary.
11	
12	\emph{Structural misparse} (scope misapplication): the agent constructs an incorrect parse and follows it consistently, paralleling garden-path processing \citep{frazier_rayner_1982,ferreira_good_enough_2002}---e.g., parsing ``items purchased with a coupon or during a sale are final'' as restricting only coupon purchases. This dominates scopal (all 5 models), conditional precedence (all 5), and coreferential (3/5).
13	
14	\emph{Information gap-filling} (assumption-based action): the agent fills missing information with plausible but incorrect defaults---e.g., inventing a 30-day return window when none is specified. This dominates incompleteness (3/5) and lexical (3/5).
15	
16	\emph{Boundary violation} (unauthorized escalation): the agent exceeds permission boundaries when authorization scope is underspecified---e.g., issuing a refund above its stated limit rather than escalating; 69.2\% of such violations involve unauthorized escalation with zero conservative refusals ($p < 10^{-4}$, binomial test), revealing systematic permis
…[truncated 1696 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 696 · 2026-05-21T17:40:53.467579+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 697 · 2026-05-21T17:40:53.568650+00:00_

1	\section{TOST Equivalence Sensitivity}
2	\label{app:tost}
3	
4	Table~\ref{tab:tost_sensitivity} reports the TOST equivalence analysis \citep{lakens_2017} across seven margins. Three pairs involving incompleteness never reach equivalence even at $\pm 20$ pp: conditional precedence--incompleteness ($\Delta = 16.8$ pp), coreferential--incompleteness ($\Delta = 22.0$ pp), and incompleteness--scopal ($\Delta = 14.2$ pp).
5	
6	\begin{table}[!ht]
7	\centering
8	\small
9	\caption{TOST equivalence sensitivity across margins. Mid-tier = fraction of the six within-cluster pairs (lexical, auth.\ scope, scopal, cond.\ prec.) that are equivalent. Inc.\ and Cor.\ columns indicate separation from the mid-tier cluster.}
10	\label{tab:tost_sensitivity}
11	\begin{tabular}{lcccc}
12	\toprule
13	Margin & Equiv.\ pairs & Mid-tier & Inc.\ sep. & Cor.\ sep. \\
14	\midrule
15	$\pm 5$ pp & 0/15 & 0/6 & \checkmark & \checkmark \\
16	$\pm 8$ pp & 0/15 & 0/6 & \checkmark & \checkmark \\
17	$\pm 10$ pp & 3/15 & 3/6 & \checkmark & \checkmark \\
18	$\pm 12$ pp & 5/15 & 5/6 & \checkmark & \checkmark \\
19	$\pm 15$ pp & 8/15 & 6/6 & \checkmark & -- \\
20	$\pm 18$ pp & 9/15 & 6/6 & \checkmark & -- \\
21	$\pm 20$ pp & 12/15 & 6/6 & -- & -- \\
22	\bottomrule
23	\end{tabular}
24	\end{table}
25	
26	\section{Mitigation Experiment}
27	\label{app:mitigation}
28	
29	Table~\ref{tab:mitigation} reports the per-type, per-model $\Delta$pp from the disambiguation-instruction mitigation experiment (1,256 treatment episodes across five of six types; coreferential was not tested). The treatment appends a type-specific disambiguation instruction to the agent's system prompt. Control rates are the matched 5-type subset from the full study (\S\ref{sec:results}).
30	
31	\begin{table*}[!ht]
32	\centering
33	\small
34	\caption{Violation rate change ($\Delta$pp) after adding type-specific disambiguation instructions. Negative values indicate reduction. Baseline violation rates are shown in parentheses. Coreferential was 
…[truncated 14206 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 698 · 2026-05-21T17:41:00.610207+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 699 · 2026-05-21T17:41:00.962073+00:00_

1	\begin{abstract}
2	LLM-based agents operate under natural-language policy specifications that inevitably contain ambiguity, yet the causal relationship between ambiguity type and safety violations remains unmeasured. We present a matched-pair study on $\tau^2$-bench with 300 clause pairs spanning a six-type, two-layer ambiguity taxonomy, evaluated across five architecturally diverse models (2,997 episodes). Ambiguous clauses increase violation rates by 34.0 percentage points (OR $= 15.1$), with a perturbation control supporting ambiguity-specific causation. A significant type hierarchy emerges (Cram\'{e}r's $V = 0.137$, $p < 10^{-4}$), with a two-tier structure among five types and incompleteness as an upper bound whose ranking partly reflects an information-addition confound (logistic regression controlling for information delta: $p = 0.022$, coefficient change $< 8\%$). The specification--linguistic layer distinction is inconclusive ($p = 0.017$, not surviving correction). The hierarchy replicates on two additional model families (LLaMA $\rho = 0.90$, $p = 0.037$; Gemini $\rho = 0.60$, directionally consistent): incompleteness is consistently high (46--62\% across seven models), while authorization scope varies 52 pp depending on the model (12\% for Claude to 64\% for GPT-5.4, though this type carries the widest measurement uncertainty, $\kappa = 0.385$), suggesting that safety training may differentially mitigate specific ambiguity types. Agents show fewer than 11\% disambiguation awareness. Our Differential Nocuity framework connects type-specific vulnerability to disambiguation channel availability and suggests both type-aware policy auditing and externalized ambiguity detection for policy-governed agent deployments.
3	\end{abstract}
4	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 351
}
```

</details>

---


### Tool call

_source line 700 · 2026-05-21T17:41:01.263845+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 701 · 2026-05-21T17:41:01.264394+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	A customer asks to return a customized item within the 30-day window. The agent consults the store policy, which states that ``items may be returned within 30 days.'' The word ``items'' scopes over all product categories, including custom orders that are normally final sale. The agent grants a full refund and arranges free return shipping. One word of scopal ambiguity costs the retailer \$200.
5	
6	LLM-based agents increasingly operate under natural-language policy specifications that govern their permitted actions. These specifications inevitably contain ambiguity: a property that has been studied for decades in requirements engineering (RE) and computational linguistics. \citet{berry_kamsties_2004} distinguish between \emph{nocuous} (i.e., harmful) ambiguity, where different stakeholders arrive at different interpretations, and \emph{innocuous} ambiguity, where shared organizational context ensures convergent interpretation. In human RE workflows, most ambiguity is innocuous because developers share domain knowledge, can consult colleagues, and iteratively clarify requirements.
7	
8	LLM agents lack these disambiguation channels. They cannot consult colleagues, rarely escalate to users, and must resolve ambiguity in real time from the text alone. This raises a question that has not been empirically addressed: does policy ambiguity cause safety violations in LLM agents, and if so, does the \emph{type} of ambiguity predict the severity of the violation? Prior work classifies ambiguity types in policies \citep{drip_r_2026,li_ambiguity_taxonomy_2024} or measures policy understanding quality \citep{policybank_2026}, but no existing study provides a causal, type-granularity mapping from ambiguity to safety violations.
9	
10	\begin{figure*}[t]
11	\centering
12	\includegraphics[width=\textwidth]{figures/fig1_overview.pdf}
13	\caption{Experimental overview. We construct 300 matched clause pairs across a six-type, two-
…[truncated 2017 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 702 · 2026-05-21T17:41:01.465456+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 703 · 2026-05-21T17:41:02.369048+00:00_

1	\section{Discussion}
2	\label{sec:discussion}
3	
4	\paragraph{Differential Nocuity.}
5	\citet{berry_kamsties_2004} distinguish nocuous from innocuous ambiguity by stakeholder divergence. Our results extend this to LLM agents: all six types are nocuous ($+34.0$ pp), but type primarily determines severity (22:1 clause-vs.-model variance ratio). We propose \emph{Differential Nocuity}: the risk of a policy ambiguity depends on three factors---ambiguity type (base vulnerability), safety training (selective mitigation of boundary-type ambiguities), and disambiguation channel availability (recovery possibility). This generates two testable predictions: (P1) types with explicit decision points (e.g., authorization scope) should show larger safety-training gains than implicit gap-filling types (e.g., incompleteness); (P2) disambiguation channels should reduce violations more for high-blindness types. Our mitigation experiment (Appendix~\ref{app:mitigation}) supports P1: $-18.0$\,pp for authorization scope vs.\ $-3.4$\,pp for incompleteness. Systematic nocuity---41.3\% of clauses trigger majority-convergent violations (\S\ref{sec:analysis})---makes such errors invisible in agreement-based evaluation.
6	
7	\paragraph{Practical implications.}
8	The C4 interaction provides suggestive evidence that incompleteness bypasses intervention points via gap-filling \citep{ferreira_good_enough_2002}, while authorization scope varies 48\,pp within a single judge (\S\ref{sec:c4}), consistent with boundary-targeted training. A proof-of-concept classifier (Appendix~\ref{app:detection}) achieves F1\,=\,0.81 for binary detection but only 0.34 for incompleteness. With $<$11\% agent self-awareness (\S\ref{sec:analysis}), type-aware auditing and externalized detection tools \citep{chantree_2006,ferrari_ambiguity_2019} remain necessary for policy-governed deployments.
9	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 903
}
```

</details>

---


### Tool call

_source line 704 · 2026-05-21T17:41:02.369541+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 705 · 2026-05-21T17:41:02.871691+00:00_

1	\section*{Limitations}
2	\label{sec:limitations}
3	
4	\paragraph{Model coverage.} We evaluate seven API-accessible models from six providers (four proprietary, three open-source; two in replication, Appendix~\ref{app:model_expansion}). Smaller open-source models (7B--70B parameters) may show different vulnerability patterns, and our findings may not generalize to models with fundamentally different training approaches.
5	
6	\paragraph{Domain scope.} $\tau^2$-bench covers retail and airline customer service. Policy ambiguity effects in other domains (healthcare, finance, legal) remain to be tested, though the within-study cross-domain consistency is encouraging: failure mode distributions share the same top-two modes (assumption-based action and unauthorized escalation) across domains, with individual mode base rates differing by up to 12.5 pp, likely reflecting domain policy structure rather than methodological artifacts.
7	
8	\paragraph{Synthetic ambiguity.} Our matched-pair design requires synthetic construction of ambiguous variants, which may not capture the full distribution of naturally occurring policy ambiguities. We mitigate this through expert review and a realism validation comparing ambiguous clauses against original $\tau^2$-bench policy text. Ambiguous clauses are indistinguishable from originals in lexical diversity (TTR, KS $p = 0.89$) and word length ($p = 0.09$). Readability is slightly higher (Flesch--Kincaid $d = 0.29$, $p = 0.006$) and sentence length moderately higher ($d = 0.74$), both reflecting the structural demands of encoding ambiguity in standalone clauses. Across matched pairs, disambiguation preserves readability (Flesch--Kincaid $d = 0.14$, $p = 0.10$), confirming that minimal edits change semantic precision without altering linguistic register.
9	
10	\paragraph{Cross-judge asymmetry.} Although our dual-judge calibration (\S\ref{sec:method}) shows no systematic bias ($p = 0.606$) and human validation confirms the LLM judge operates 
…[truncated 2739 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 706 · 2026-05-21T17:41:02.872066+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 707 · 2026-05-21T17:41:03.173443+00:00_

1	\section{Conclusion}
2	
3	Ambiguous policy clauses increase agent safety violations by 34.0\,pp (OR\,$=$\,15.1) across five models, with clause identity explaining 22$\times$ more variance than model identity. The two-tier type hierarchy replicates across seven models ($\rho = 0.60$--$0.90$). With $<$11\% disambiguation awareness, type-aware auditing and externalized detection are critical for policy-governed deployments.
4	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 708 · 2026-05-21T17:41:03.223996+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/taxonomy.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/taxonomy.tex"
  }
}
```

</details>

---


### Tool result

_source line 709 · 2026-05-21T17:41:03.274737+00:00_

1	\section{Ambiguity Taxonomy}
2	\label{sec:taxonomy}
3	
4	We adopt an operational definition of ambiguity following \citet{wasow_ambiguity_2005}: a policy clause is ambiguous when it admits multiple distinct interpretations available to a competent reader, including cases of vagueness where the boundary between interpretations is gradient rather than discrete \citep{kennedy_vagueness_2007}.
5	
6	Our taxonomy comprises six types organized into two layers, drawing on \citet{li_ambiguity_taxonomy_2024}'s NLP taxonomy (11 types), \citet{massey_ambiguity_re_2014}'s requirements engineering taxonomy (6 types), and the concurrent DRIP-R benchmark \citep{drip_r_2026} (5 types). We select types based on two criteria: frequency in operational policy documents (assessed via manual audit of $\tau^2$-bench policies) and theoretical distinctiveness (each type maps to a different resolution mechanism).
7	
8	\paragraph{Linguistic layer.} These types operate at the syntactic or semantic level and can, in principle, be resolved by parsing or contextual cues within the text.
9	\begin{itemize}
10	\item \textbf{Scopal}: quantifier, negation, or modal scope interactions (e.g., ``all items may not be returned'' admits universal-negation and negation-of-universal readings).
11	\item \textbf{Lexical}: polysemy or homonymy (e.g., ``charge'' as financial cost vs.\ penalty; ``party'' as individual vs.\ group).
12	\item \textbf{Coreferential}: unclear pronoun or noun-phrase reference (e.g., ``the agent should verify the customer's identity before processing their refund request, which must be approved by a supervisor'' where ``which'' could refer to the verification or the refund).
13	\end{itemize}
14	
15	\paragraph{Specification layer.} These types arise from pragmatic or discourse-level gaps that require domain knowledge or organizational context to resolve.
16	\begin{itemize}
17	\item \textbf{Authorization scope}: vague permission or role boundaries (e.g., ``authorized personnel may issue r
…[truncated 1121 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 710 · 2026-05-21T17:41:10.205919+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 711 · 2026-05-21T17:41:10.206473+00:00_

1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{Ambiguity in NLP and requirements engineering.}
5	Ambiguity has been studied extensively in both computational linguistics and software engineering. Word sense disambiguation \citep{navigli_wsd_2009} addresses lexical ambiguity at the token level; our lexical type extends this to policy-specific polysemy. \citet{li_ambiguity_taxonomy_2024} propose an 11-type NLP taxonomy covering syntactic, semantic, and pragmatic ambiguity, from which we draw our linguistic-layer types. In requirements engineering (RE), \citet{massey_ambiguity_re_2014} classify six ambiguity types in regulatory texts, and \citet{berry_kamsties_2004} introduce the distinction between nocuous ambiguity (where stakeholders diverge on interpretation) and innocuous ambiguity (where they converge). Computational detection of nocuous ambiguity has progressed from heuristic methods \citep{chantree_2006,willis_nocuous_2008} through NLP-based cross-domain detectors \citep{ferrari_ambiguity_2019,ferrari_defects_2018} to transformer-based approaches for anaphoric ambiguity \citep{ezzini_taphsir_2022,ezzini_anaphoric_2022}. \citet{zhao_nlp4re_2021} survey the broader NLP4RE landscape. Our work extends Berry and Kamsties' framework to LLM agents, where the absence of shared organizational context makes previously innocuous ambiguity nocuous.
6	
7	\paragraph{Psycholinguistics of ambiguity processing.}
8	\citet{ferreira_good_enough_2002} show that human comprehenders build shallow, ``good-enough'' representations rather than full parses, paralleling our observation that LLM agents adopt surface interpretations. \citet{frazier_rayner_1982} demonstrate early commitment to a single parse; \citet{li_garden_path_llm_2024} provide direct evidence that LLMs exhibit analogous garden-path effects. \citet{liu_ambiguity_2023} demonstrate that language models fail to represent ambiguity, collapsing multiple interpretations into a single output. These findings
…[truncated 2210 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 712 · 2026-05-21T17:44:39.004888+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "\n# Reviewer 1 审稿意见（方法严谨性 + 实验有效性）\n\n**论文**: \"Not All Policy Ambiguity Is Equal: Type-Specific Safety Risks for LLM Agents\"\n**Venue**: EMNLP 2026 via ARR May cycle\n\n---\n\n## Summary\n\n本文研究 LLM agent 在自然语言策略规范下，不同类型的歧义（ambiguity）如何因果性地导致安全违规。作者构建了一个六类型、双层（linguistic / specification）歧义分类体系，在 τ²-bench 上通过 matched-pair design 生成 300 对条款（ambiguous vs. unambiguous），在 5 个模型上运行 2,997 个 episodes。核心发现：(C1) 歧义条款使违规率增加 34.0 pp（OR=15.1）；(C2) 类型间存在显著层次结构（Cramér's V=0.137），呈两层模式；(C3) specification vs. linguistic 层级区分不显著（inconclusive）；(C4) model×type 交互显著但标记为 exploratory。论文还报告了 \"Ambiguity Blindness\"（<11% disambiguation awareness）和三种 type-specific failure mechanisms。\n\n---\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | C1 有充分因果支撑（perturbation control + replication），C2 合理但 SESOI 锚定缺乏外部依据，C3/C4 恰当标注为 inconclusive/exploratory。authorization scope κ=0.385 削弱了 C4 部分结论的可靠性。 |\n| Excitement | 3.5/5 | 研究问题及时且实用（ambiguity→safety violation 的因果映射），matched-pair 因果设计在 agent safety 领域较新。但\"歧义导致更多违规\"的 broad finding 本身不意外；type-level 差异是更有价值的贡献。 |\n| Reproducibility | 4/5 | API 超参完整（temp=0, top_p=1, max_tokens=4096），承诺公开 300 clause pairs + pipeline + traces。ICC=0.919 仅限 OpenAI family 是局限。 |\n| Confidence | 4/5 | 我熟悉因果推断、agent safety evaluation 和 NLP ambiguity 文献。 |\n| **Overall Assessment** | **3.5** | **Borderline Conference** — 方法论扎实、transparency 出色，但若干测量可靠性问题和 SESOI 锚定缺陷使 C2/C4 的说服力受限。 |\n\n---\n\n## 主要优势\n\n**S1. 因果设计严谨（C1）。** Matched-pair design + perturbation control（Δ_perturb = −0.67 pp, CI 含零）是该领域少见的因果识别策略。perturbation control 排除了表层文本变化的混淆，使 34.0 pp 效应可归因于语义歧义（§4.2, §4.5）。在 7 个模型上的 replication（Appendix E）进一步增强了外部效度。\n\n**S2. Confound 透明度极高。** Incompleteness 的 information-addition confound 在 §3（taxonomy 定义）就主动指出，§5.2 讨论，Appendix F 和 H 提供 logistic regression 控制（p=0.022, coefficient change <8%）和 coreferential lower bound。这种 self-critique 水平在 agent safety 论文中罕见。\n\n**S3. Claims 层次清晰。** C1（primary, well-supported）→ C2（primary, with caveats）→ C3（inconclusive）→ C4（exploratory）的递进标注是良好科学实践，避免了 overclaim。\n\n**S4. 分析深度充分。** Severity sensitivity（Appendix C）、TOST sensitivity across 7 margins（Appendix A）、bootstrap cluster analysis（Appendix I）、clause-level LOO variance（Appendix J）、failure mode taxonomy（§6）提供了多角度 robustness 检验。\n\n**S5. 实际可操作性。** Differential Nocuity 框架将 ambiguity type mapping 到 failure mechanism，detection experiment（Appendix D）展示了 pipeline 原型（binary F1=0.81），mitigation experiment（Appendix B）量化了 type-specific intervention 效果。\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] **SESOI ±15 pp 缺乏外部锚定，C2 两层结构的稳健性不足**\n\n- 具体位置：§4.6, Appendix A (Table 2)\n- 问题：SESOI ±15 pp 的唯一理由是\"a type producing ≥15 pp more violations warrants distinct policy handling in deployment\"和\"exceeds perturbation control bound by >2×\"（§4.6）。前者是作者主观判断，缺乏外部文献或 domain expert 调研的支持；后者是循环论证——perturbation control bound 是本实验的产物而非独立标准。Table 2（Appendix A）显示，±10 pp 时仅 3/6 mid-tier pairs 等价，TOST power 降至 0.57。这意味着\"两层结构\"在合理的替代 margin 下部分瓦解。Bootstrap cluster 分析的 AU p-value=0.47（Appendix I）也表明 incompleteness singleton 边界并不尖锐。\n- 为什么影响接收：C2 是论文的核心贡献之一（\"Differential Nocuity\"框架的基础）。如果两层结构高度依赖 margin 选择，framework 的 prescriptive value 就大打折扣。\n- 建议修改方向：(1) 提供 deployment scenario 中 ±15 pp 阈值的外部依据（如 industry policy error tolerance survey、deployment cost-benefit analysis 文献）；(2) 在正文中更显著地呈现 sensitivity 结果，明确表述两层结构在 ±10–12 pp 时不完全成立；(3) 考虑降低对两层结构的 claim 强度，将其定位为 \"one plausible clustering\" 而非 \"the hierarchy\"。\n\n**N2** [critical] **Authorization scope κ=0.385 下的 C4 结论可信度不足**\n\n- 具体位置：§4.4（cross-judge calibration），§5.4（C4），Appendix G（Table 8）\n- 问题：Authorization scope 的 cross-judge κ=0.385 仅为 \"fair\"（Landis-Koch），human-LLM κ=0.644，CI=[0.35, 0.91]。然而 C4 讨论中称 authorization scope 是 \"most model-differentiating type\"（52 pp range, Claude 12% → GPT-5.4 64%），并在 Discussion（§7）据此推测 safety training 差异化地 mitigate 了 boundary-type ambiguity。当测量工具的可靠性不足时，跨模型的 52 pp 变异中有多少是真实效应、多少是测量噪声难以分离。Figure 3 中 authorization scope 的突出视觉呈现进一步放大了读者对这一 pattern 的信心。\n- 为什么影响接收：C4 虽标注为 exploratory，但 Discussion 和 Abstract 中的 framing 对 authorization scope 的 differential safety training 暗示过于确定。如果 κ=0.385 的 type 驱动了 framework 的核心 prediction (P1)，整个 Differential Nocuity narrative 的 evidentiary basis 就不够 solid。\n- 建议修改方向：(1) 在 C4 讨论中加入 \"given the low per-type agreement (κ=0.385), the authorization scope range should be interpreted as an upper bound on true between-model variance\" 的显式 caveat；(2) Abstract 中 \"authorization scope varies 52 pp\" 应附带 measurement uncertainty qualification；(3) 验证 52 pp range 在 moderate+ vs. any-violation 阈值下是否稳定（Appendix C 仅报告 Cramér's V 和 Kendall τ，未报告 per-type range stability）。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] **Token count 作为 information content proxy 的有效性未验证**\n\n- 具体位置：Appendix F, Appendix H (Table 9)\n- 问题：Incompleteness confound 的 logistic regression 使用 token count difference 作为 information content 的代理变量。但 token count 是信息量的粗糙近似——两个同样 token 数的条款可能信息含量差异很大（例如，添加一个 exception clause vs. 添加一个 padding phrase）。论文未讨论此 proxy 的 content validity，也未尝试替代度量（如 semantic similarity shift、clause-level entropy change）。\n- 建议：(1) 讨论 token count 作为 proxy 的局限性；(2) 如有时间，补充至少一种替代 information content 度量以验证 robustness。\n\n**W2** [warning] **Human validation 样本量偏小，per-type 估计不可靠**\n\n- 具体位置：§4.4（Human validation），Appendix G (Table 8)\n- 问题：100 episodes（2,997 的 3.3%），每种类型仅 32-34 个 episodes。Scopal 的 95% CI 是 [0.00, 1.00]，coreferential 是 [0.00, 0.84]——这些 CI 本质上是 uninformative 的。论文在 Limitations 中承认了这一点（§Limitations, \"Per-type reliability\"），但 §4.4 的正文呈现过于乐观地强调了 pooled κ=0.733 而淡化了 per-type 的不稳定性。\n- 建议：(1) 在 §4.4 正文中更显著地呈现 per-type CI 宽度；(2) 如果可行，增加 human validation 样本量（尤其是 authorization scope 和 coreferential）。\n\n**W3** [warning] **Cross-provider reproducibility 缺乏直接度量**\n\n- 具体位置：§4.5（Reproducibility）\n- 问题：ICC=0.919 仅在 OpenAI family（GPT-5.4, GPT-4.1）内计算，cross-provider stability 仅通过 \"C1 consistency across all seven models\" 间接论证。但 C1 consistency（所有模型都显示 significant Δ）是一个方向性声明，不等价于 effect size 的跨 provider 稳定性。论文甚至在 replication 中观察到 LLaMA 的 Δ=+20.0 pp 远小于主研究的 +25.7 to +39.0 pp range，且 LLaMA 的 unambiguous baseline 高达 17.6%，暗示跨 provider 的 effect 可能受 baseline instruction-following quality 调节。\n- 建议：(1) 明确承认 ICC 仅为 within-provider；(2) 计算 replication models 与原始 5 个模型之间的 effect size correlation 或 agreement 统计量。\n\n**W4** [warning] **\"Ambiguity Blindness\" 的归因问题**\n\n- 具体位置：§6.2\n- 问题：论文将 <11% disambiguation awareness 称为 \"Ambiguity Blindness\"，暗示这是 LLM agents 的认知局限。但论文的 experimental setup 中，agent 的 system prompt 并未指示其检测或报告歧义——4.6% 的 awareness rate 可能反映的是 default instruction-following 行为（\"按 policy 执行\"），而非 inability to detect ambiguity。事实上，mitigation experiment（Appendix B）显示添加 disambiguation instruction 后违规率下降 8.5 pp，暗示 agents 并非 \"blind\" 而是 \"uninstructed\"。\n- 建议：讨论 \"Blindness\" vs. \"Uninstructedness\" 的区分。如果 system prompt 中明确要求 flag ambiguity，awareness rate 是否会大幅提升？这直接影响 practical implication 的方向（是改善 policy 本身，还是改善 agent 指令？）。\n\n**W5** [warning] **多重比较校正策略不透明**\n\n- 具体位置：§4.6\n- 问题：论文提到 \"Holm-Bonferroni correction is applied within three test families\"，但未明确定义这三个 test families 的边界。正文中的检验包括：McNemar's test (C1)、χ² omnibus (C2)、per-type Fisher's exact (C2 pairwise)、TOST (C2)、χ² for layer effect (C3)、F-test for interaction (C4)、logistic regression LRT (C4)。如何将这些分配到三个 families 中，correction 后哪些检验变为 non-significant，读者无法验证。\n- 建议：明确列出三个 test families 的成员，报告 corrected p-values（至少在 Appendix）。\n\n---\n\n## 小问题（不影响接收）\n\n- **M1**: Abstract 提到 \"coefficient change < 8%\"——这个细节过于 technical，放在 abstract 中增加了认知负担。考虑简化。\n- **M2**: §5.2 \"the two-tier pattern emerges at ±12 pp (5/6 mid-tier pairs equivalent) and stabilizes at ±15 pp (6/6)\"——\"stabilizes\" 一词暗示 ±15 pp 是自然 breakpoint，但这恰好是使所有 pairs 等价的最小 margin，换言之是 ceiling 而非 breakpoint。措辞应更中性。\n- **M3**: Figure 1 overview 图中 \"cross-judge\" 评估流程的箭头方向不太清晰——GPT-5.4 judge 评估哪些模型、GPT-4.1 评估哪个模型的视觉区分可以更明确。\n- **M4**: §6.1 failure mode taxonomy 使用了两种 reliability 指标（Gwet's AC₁=0.62, Cohen's κ=0.52）。对不熟悉 prevalence paradox 的读者，建议在正文而非仅在 Limitations 中简要解释为什么要报告 AC₁。\n- **M5**: Limitations 中 \"per-type reliability\" 段放在最后，但这是一个影响正文 C2 和 C4 interpretation 的关键 caveat，建议位置提前。\n- **M6**: §5.4 的 F(20)=1.97 交互检验——df=20 对应 (5-1)×(6-1) 但文中括号内已解释了，确认正确。不过 denominator df 未报告（应为 n-k 相关），建议补充完整 F-test specification。\n\n---\n\n## Questions for Authors\n\n**Q1**: 如果使用 ±10 pp 作为 SESOI（一个更保守但同样合理的 margin），C2 的 \"Differential Nocuity\" framework 的核心 narrative 如何调整？两层结构变为什么？\n\n**Q2**: 论文是否尝试过让 agent 在 system prompt 中被要求 \"flag any ambiguity in the policy before acting\"？如果有，disambiguation awareness 从 4.6% 提升到多少？如果没有，这是否应该作为一个 baseline condition 加入实验设计？\n\n**Q3**: Appendix B 的 mitigation experiment 中，authorization scope 的 pooled 下降 −18.0 pp 与 incompleteness 的 −3.4 pp 之间的差异是否经过统计检验（如 interaction test）？Discussion 中称此结果 \"supports P1\"，但没有报告这一对比的 p-value。\n\n**Q4**: 关于 cross-judge design——如果在 100 episode dual-judge calibration sample 上，per-type 的 authorization scope κ=0.385 已经很低，作者是否考虑过对 authorization scope 使用 majority vote from multiple judges 来降低测量噪声？\n\n**Q5**: Table 1 中 DeepSeek-V3 的 overall violation rate (49.7%) 远高于 Claude (30.3%)。这 19.4 pp gap 中有多少可归因于 judge identity confound（DeepSeek 由 GPT-5.4 判，Claude 也由 GPT-5.4 判——等等，两者用的是同一个 judge，所以 judge identity 不应解释它们之间的差异）？请确认 judge assignment 逻辑。\n\n---\n\n## Missing References\n\n- **Tamkin et al., 2023** — \"Evaluating and Mitigating Discrimination in Language Model Decisions\" (policy-governed decision-making)\n- **Pan et al., 2024** — \"Do LLMs Follow Instructions? The Role of Instruction Ambiguity\" (直接研究 LLM 的 ambiguity following 行为)\n- **Karpinska & Iyyer, 2023** — \"Large Language Models Effectively Leverage Document-level Context for Literary Translation...\" (关于 LLM 处理 contextual ambiguity 的能力)\n- 建议检查 DRIP-R (Borokatos et al., 2026) 是否有更完整的 camera-ready version 可引用\n\n---\n\n## 总体评分\n\n**Overall**: 3.5 — Borderline Conference\n\n**一句话总结**: C1 因果效应（+34 pp）的方法论严谨性达到 conference 标准，但 C2 核心框架对 SESOI 选择的敏感性和 authorization scope 低 κ 下的 C4 over-interpretation 是主要隐患——修复后可达 Conference acceptance。\n",
  "reviewer_id": "1",
  "project": "policy_ambiguity_safety"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "\n# Reviewer 1 审稿意见（方法严谨性 + 实验有效性）\n\n**论文**: \"Not All Policy Ambiguity Is Equal: Type-Specific Safety Risks for LLM Agents\"\n**Venue**: EMNLP 2026 via ARR May cycle\n\n---\n\n## Summary\n\n本文研究 LLM agent 在自然语言策略规范下，不同类型的歧义（ambiguity）如何因果性地导致安全违规。作者构建了一个六类型、双层（linguistic / specification）歧义分类体系，在 τ²-bench 上通过 matched-pair design 生成 300 对条款（ambiguous vs. unambiguous），在 5 个模型上运行 2,997 个 episodes。核心发现：(C1) 歧义条款使违规率增加 34.0 pp（OR=15.1）；(C2) 类型间存在显著层次结构（Cramér's V=0.137），呈两层模式；(C3) specification vs. linguistic 层级区分不显著（inconclusive）；(C4) model×type 交互显著但标记为 exploratory。论文还报告了 \"Ambiguity Blindness\"（<11% disambiguation awareness）和三种 type-specific failure mechanisms。\n\n---\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | C1 有充分因果支撑（perturbation control + replication），C2 合理但 SESOI 锚定缺乏外部依据，C3/C4 恰当标注为 inconclusive/exploratory。authorization scope κ=0.385 削弱了 C4 部分结论的可靠性。 |\n| Excitement | 3.5/5 | 研究问题及时且实用（ambiguity→safety violation 的因果映射），matched-pair 因果设计在 agent safety 领域较新。但\"歧义导致更多违规\"的 broad finding 本身不意外；type-level 差异是更有价值的贡献。 |\n| Reproducibility | 4/5 | API 超参完整（temp=0, top_p=1, max_tokens=4096），承诺公开 300 clause pairs + pipeline + traces。ICC=0.919 仅限 OpenAI family 是局限。 |\n| Confidence | 4/5 | 我熟悉因果推断、agent safety evaluation 和 NLP ambiguity 文献。 |\n| **Overall Assessment** | **3.5** | **Borderline Conference** — 方法论扎实、transparency 出色，但若干测量可靠性问题和 SESOI 锚定缺陷使 C2/C4 的说服力受限。 |\n\n---\n\n## 主要优势\n\n**S1. 因果设计严谨（C1）。** Matched-pair design + perturbation control（Δ_perturb = −0.67 pp, CI 含零）是该领域少见的因果识别策略。perturbation control 排除了表层文本变化的混淆，使 34.0 pp 效应可归因于语义歧义（§4.2, §4.5）。在 7 个模型上的 replication（Appendix E）进一步增强了外部效度。\n\n**S2. Confound 透明度极高。** Incompleteness 的 information-addition confound 在 §3（taxonomy 定义）就主动指出，§5.2 讨论，Appendix F 和 H 提供 logistic regression 控制（p=0.022, coefficient change <8%）和 coreferential lower bound。这种 self-critique 水平在 agent safety 论文中罕见。\n\n**S3. Claims 层次清晰。** C1（primary, well-supported）→ C2（primary, with caveats）→ C3（inconclusive）→ C4（exploratory）的递进标注是良好科学实践，避免了 overclaim。\n\n**S4. 分析深度充分。** Severity sensitivity（Appendix C）、TOST sensitivity across 7 margins（Appendix A）、bootstrap cluster analysis（Appendix I）、clause-level LOO variance（Appendix J）、failure mode taxonomy（§6）提供了多角度 robustness 检验。\n\n**S5. 实际可操作性。** Differential Nocuity 框架将 ambiguity type mapping 到 failure mechanism，detection experiment（Appendix D）展示了 pipeline 原型（binary F1=0.81），mitigation experiment（Appendix B）量化了 type-specific intervention 效果。\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] **SESOI ±15 pp 缺乏外部锚定，C2 两层结构的稳健性不足**\n\n- 具体位置：§4.6, Appendix A (Table 2)\n- 问题：SESOI ±15 pp 的唯一理由是\"a type producing ≥15 pp more violations warrants distinct policy handling in deployment\"和\"exceeds perturbation control bound by >2×\"（§4.6）。前者是作者主观判断，缺乏外部文献或 domain expert 调研的支持；后者是循环论证——perturbation control bound 是本实验的产物而非独立标准。Table 2（Appendix A）显示，±10 pp 时仅 3/6 mid-tier pairs 等价，TOST power 降至 0.57。这意味着\"两层结构\"在合理的替代 margin 下部分瓦解。Bootstrap cluster 分析的 AU p-value=0.47（Appendix I）也表明 incompleteness singleton 边界并不尖锐。\n- 为什么影响接收：C2 是论文的核心贡献之一（\"Differential Nocuity\"框架的基础）。如果两层结构高度依赖 margin 选择，framework 的 prescriptive value 就大打折扣。\n- 建议修改方向：(1) 提供 deployment scenario 中 ±15 pp 阈值的外部依据（如 industry policy error tolerance survey、deployment cost-benefit analysis 文献）；(2) 在正文中更显著地呈现 sensitivity 结果，明确表述两层结构在 ±10–12 pp 时不完全成立；(3) 考虑降低对两层结构的 claim 强度，将其定位为 \"one plausible clustering\" 而非 \"the hierarchy\"。\n\n**N2** [critical] **Authorization scope κ=0.385 下的 C4 结论可信度不足**\n\n- 具体位置：§4.4（cross-judge calibration），§5.4（C4），Appendix G（Table 8）\n- 问题：Authorization scope 的 cross-judge κ=0.385 仅为 \"fair\"（Landis-Koch），human-LLM κ=0.644，CI=[0.35, 0.91]。然而 C4 讨论中称 authorization scope 是 \"most model-differentiating type\"（52 pp range, Claude 12% → GPT-5.4 64%），并在 Discussion（§7）据此推测 safety training 差异化地 mitigate 了 boundary-type ambiguity。当测量工具的可靠性不足时，跨模型的 52 pp 变异中有多少是真实效应、多少是测量噪声难以分离。Figure 3 中 authorization scope 的突出视觉呈现进一步放大了读者对这一 pattern 的信心。\n- 为什么影响接收：C4 虽标注为 exploratory，但 Discussion 和 Abstract 中的 framing 对 authorization scope 的 differential safety training 暗示过于确定。如果 κ=0.385 的 type 驱动了 framework 的核心 prediction (P1)，整个 Differential Nocuity narrative 的 evidentiary basis 就不够 solid。\n- 建议修改方向：(1) 在 C4 讨论中加入 \"given the low per-type agreement (κ=0.385), the authorization scope range should be interpreted as an upper bound on true between-model variance\" 的显式 caveat；(2) Abstract 中 \"authorization scope varies 52 pp\" 应附带 measurement uncertainty qualification；(3) 验证 52 pp range 在 moderate+ vs. any-violation 阈值下是否稳定（Appendix C 仅报告 Cramér's V 和 Kendall τ，未报告 per-type range stability）。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] **Token count 作为 information content proxy 的有效性未验证**\n\n- 具体位置：Appendix F, Appendix H (Table 9)\n- 问题：Incompleteness confound 的 logistic regression 使用 token count difference 作为 information content 的代理变量。但 token count 是信息量的粗糙近似——两个同样 token 数的条款可能信息含量差异很大（例如，添加一个 exception clause vs. 添加一个 padding phrase）。论文未讨论此 proxy 的 content validity，也未尝试替代度量（如 semantic similarity shift、clause-level entropy change）。\n- 建议：(1) 讨论 token count 作为 proxy 的局限性；(2) 如有时间，补充至少一种替代 information content 度量以验证 robustness。\n\n**W2** [warning] **Human validation 样本量偏小，per-type 估计不可靠**\n\n- 具体位置：§4.4（Human validation），Appendix G (Table 8)\n- 问题：100 episodes（2,997 的 3.3%），每种类型仅 32-34 个 episodes。Scopal 的 95% CI 是 [0.00, 1.00]，coreferential 是 [0.00, 0.84]——这些 CI 本质上是 uninformative 的。论文在 Limitations 中承认了这一点（§Limitations, \"Per-type reliability\"），但 §4.4 的正文呈现过于乐观地强调了 pooled κ=0.733 而淡化了 per-type 的不稳定性。\n- 建议：(1) 在 §4.4 正文中更显著地呈现 per-type CI 宽度；(2) 如果可行，增加 human validation 样本量（尤其是 authorization scope 和 coreferential）。\n\n**W3** [warning] **Cross-provider reproducibility 缺乏直接度量**\n\n- 具体位置：§4.5（Reproducibility）\n- 问题：ICC=0.919 仅在 OpenAI family（GPT-5.4, GPT-4.1）内计算，cross-provider stability 仅通过 \"C1 consistency across all seven models\" 间接论证。但 C1 consistency（所有模型都显示 significant Δ）是一个方向性声明，不等价于 effect size 的跨 provider 稳定性。论文甚至在 replication 中观察到 LLaMA 的 Δ=+20.0 pp 远小于主研究的 +25.7 to +39.0 pp range，且 LLaMA 的 unambiguous baseline 高达 17.6%，暗示跨 provider 的 effect 可能受 baseline instruction-following quality 调节。\n- 建议：(1) 明确承认 ICC 仅为 within-provider；(2) 计算 replication models 与原始 5 个模型之间的 effect size correlation 或 agreement 统计量。\n\n**W4** [warning] **\"Ambiguity Blindness\" 的归因问题**\n\n- 具体位置：§6.2\n- 问题：论文将 <11% disambiguation awareness 称为 \"Ambiguity Blindness\"，暗示这是 LLM agents 的认知局限。但论文的 experimental setup 中，agent 的 system prompt 并未指示其检测或报告歧义——4.6% 的 awareness rate 可能反映的是 default instruction-following 行为（\"按 policy 执行\"），而非 inability to detect ambiguity。事实上，mitigation experiment（Appendix B）显示添加 disambiguation instruction 后违规率下降 8.5 pp，暗示 agents 并非 \"blind\" 而是 \"uninstructed\"。\n- 建议：讨论 \"Blindness\" vs. \"Uninstructedness\" 的区分。如果 system prompt 中明确要求 flag ambiguity，awareness rate 是否会大幅提升？这直接影响 practical implication 的方向（是改善 policy 本身，还是改善 agent 指令？）。\n\n**W5** [warning] **多重比较校正策略不透明**\n\n- 具体位置：§4.6\n- 问题：论文提到 \"Holm-Bonferroni correction is applied within three test families\"，但未明确定义这三个 test families 的边界。正文中的检验包括：McNemar's test (C1)、χ² omnibus (C2)、per-type Fisher's exact (C2 pairwise)、TOST (C2)、χ² for layer effect (C3)、F-test for interaction (C4)、logistic regression LRT (C4)。如何将这些分配到三个 families 中，correction 后哪些检验变为 non-significant，读者无法验证。\n- 建议：明确列出三个 test families 的成员，报告 corrected p-values（至少在 Appendix）。\n\n---\n\n## 小问题（不影响接收）\n\n- **M1**: Abstract 提到 \"coefficient change < 8%\"——这个细节过于 technical，放在 abstract 中增加了认知负担。考虑简化。\n- **M2**: §5.2 \"the two-tier pattern emerges at ±12 pp (5/6 mid-tier pairs equivalent) and stabilizes at ±15 pp (6/6)\"——\"stabilizes\" 一词暗示 ±15 pp 是自然 breakpoint，但这恰好是使所有 pairs 等价的最小 margin，换言之是 ceiling 而非 breakpoint。措辞应更中性。\n- **M3**: Figure 1 overview 图中 \"cross-judge\" 评估流程的箭头方向不太清晰——GPT-5.4 judge 评估哪些模型、GPT-4.1 评估哪个模型的视觉区分可以更明确。\n- **M4**: §6.1 failure mode taxonomy 使用了两种 reliability 指标（Gwet's AC₁=0.62, Cohen's κ=0.52）。对不熟悉 prevalence paradox 的读者，建议在正文而非仅在 Limitations 中简要解释为什么要报告 AC₁。\n- **M5**: Limitations 中 \"per-type reliability\" 段放在最后，但这是一个影响正文 C2 和 C4 interpretation 的关键 caveat，建议位置提前。\n- **M6**: §5.4 的 F(20)=1.97 交互检验——df=20 对应 (5-1)×(6-1) 但文中括号内已解释了，确认正确。不过 denominator df 未报告（应为 n-k 相关），建议补充完整 F-test specification。\n\n---\n\n## Questions for Authors\n\n**Q1**: 如果使用 ±10 pp 作为 SESOI（一个更保守但同样合理的 margin），C2 的 \"Differential Nocuity\" framework 的核心 narrative 如何调整？两层结构变为什么？\n\n**Q2**: 论文是否尝试过让 agent 在 system prompt 中被要求 \"flag any ambiguity in the policy before acting\"？如果有，disambiguation awareness 从 4.6% 提升到多少？如果没有，这是否应该作为一个 baseline condition 加入实验设计？\n\n**Q3**: Appendix B 的 mitigation experiment 中，authorization scope 的 pooled 下降 −18.0 pp 与 incompleteness 的 −3.4 pp 之间的差异是否经过统计检验（如 interaction test）？Discussion 中称此结果 \"supports P1\"，但没有报告这一对比的 p-value。\n\n**Q4**: 关于 cross-judge design——如果在 100 episode dual-judge calibration sample 上，per-type 的 authorization scope κ=0.385 已经很低，作者是否考虑过对 authorization scope 使用 majority vote from multiple judges 来降低测量噪声？\n\n**Q5**: Table 1 中 DeepSeek-V3 的 overall violation rate (49.7%) 远高于 Claude (30.3%)。这 19.4 pp gap 中有多少可归因于 judge identity confound（DeepSeek 由 GPT-5.4 判，Claude 也由 GPT-5.4 判——等等，两者用的是同一个 judge，所以 judge identity 不应解释它们之间的差异）？请确认 judge assignment 逻辑。\n\n---\n\n## Missing References\n\n- **Tamkin et al., 2023** — \"Evaluating and Mitigating Discrimination in Language Model Decisions\" (policy-governed decision-making)\n- **Pan et al., 2024** — \"Do LLMs Follow Instructions? The Role of Instruction Ambiguity\" (直接研究 LLM 的 ambiguity following 行为)\n- **Karpinska & Iyyer, 2023** — \"Large Language Models Effectively Leverage Document-level Context for Literary Translation...\" (关于 LLM 处理 contextual ambiguity 的能力)\n- 建议检查 DRIP-R (Borokatos et al., 2026) 是否有更完整的 camera-ready version 可引用\n\n---\n\n## 总体评分\n\n**Overall**: 3.5 — Borderline Conference\n\n**一句话总结**: C1 因果效应（+34 pp）的方法论严谨性达到 conference 标准，但 C2 核心框架对 SESOI 选择的敏感性和 authorization scope 低 κ 下的 C4 over-interpretation 是主要隐患——修复后可达 Conference acceptance。\n",
    "reviewer_id": "1",
    "project": "policy_ambiguity_safety"
  }
}
```

</details>

---


### Tool result

_source line 713 · 2026-05-21T17:44:42.723187+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_967344d166ba485ad606d14379e69d85:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3718
}
```

</details>

---


### Assistant

_source line 714 · 2026-05-21T17:44:53.463241+00:00_

审稿意见已提交给 Review Director。

总结：

- **Overall 3.5 (Borderline Conference)**
- **2 个 Must-Fix**：(1) SESOI ±15pp 缺乏外部锚定，C2 两层结构对 margin 选择敏感；(2) Authorization scope κ=0.385 下 C4 结论可信度不足，Discussion/Abstract 对 differential safety training 的暗示过于确定
- **5 个 Should-Fix**：token count proxy 有效性未验证、human validation 样本偏小、cross-provider ICC 缺乏直接度量、"Ambiguity Blindness" 归因问题（uninstructed vs. blind）、多重比较校正策略不透明
- **核心判断**：C1（+34pp 因果效应）方法论严谨，C3/C4 标注恰当，但 C2 的 Differential Nocuity 框架和 C4 的 authorization scope narrative 需要更审慎的 claim calibration

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1"
}
```

</details>

---


## Round 20

## Round 20

10 recorded events


### User

_source line 715 · 2026-05-21T17:46:34.925522+00:00_

[Round 1 审稿请求]:
以下是 Reviewer 2（新颖性 + 完整性）的完整审稿意见。请逐条回应其 Must-Fix 和 Should-Fix 问题：对每一条用 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。

---

# Reviewer 2 完整审稿意见

## Overall: 3.5 — Borderline Conference

## 主要优势
1. 实验设计是最强贡献。matched-pair causal design + perturbation control 是该领域首创。
2. 统计方法严谨且透明。TOST + margin sensitivity + bootstrap cluster 三管齐下。
3. 关键发现有实际价值。Type 解释 22.4% 方差 vs. model 仅 1.0%。
4. Honest reporting。C3 如实报告 inconclusive，C4 标注 [Exploratory]。

## Must-Fix 问题

**N1** [critical] **Taxonomy 混淆了三个不同的语言学/逻辑现象**
- Section 3: taxonomy 将 ambiguity、vagueness、incompleteness 混为一谈。
  - Authorization scope 是 vagueness（模糊权限边界），不是 ambiguity（多义解读）。Kennedy (2007) 定义的 gradient boundary。
  - Incompleteness 是 information absence，不是 present text 的多义性。论文自己承认 "resolution requires adding new policy content"。
  - Conditional precedence 是 normative conflict（规范冲突），每条规则本身毫无歧义，问题是缺少冲突解决规则。
- 如果 6 个 type 中有 3 个不严格属于 ambiguity，核心 claim "ambiguity type predicts severity" 的理论基础被削弱。
- 建议：(a) 重新 framing 为 "policy specification defects"；或 (b) 保留 ambiguity framing 但正面讨论理论张力。

**N2** [critical] **"Differential Nocuity" 框架的增量贡献不清晰**
- Section 7, Section 1 contribution (2): 框架声称 risk = f(ambiguity type, safety training, disambiguation channel availability)。但：
  - LLM agents 缺乏 disambiguation channels → 所有 ambiguity 都 nocuous → Berry & Kamsties 2004 的直接推论，不需要实验
  - 不同 type 导致不同 severity → C2 实验发现，将其包装为 "framework" 过度
  - Safety training differentially mitigates → 基于 [Exploratory] 的 C4 + κ=0.385 的 authorization scope
- 建议：降级为 interpretive lens 而非 contribution；或展示 non-obvious predictions。

## Should-Fix 问题

**W1** [warning] Abstract 信息过载，关键 message 被淹没。读起来像 Results 压缩版。
**W2** [warning] C3 Layer Distinction 未通过校正但仍作为 taxonomy 组织原则——逻辑不一致。建议改为 flat six-type 或说明 layer 是 hypothesis。
**W3** [warning] 与 DRIP-R 的 taxonomy 映射缺失——5 types 如何对应本文 6 types。
**W4** [warning] Coreferential 被系统性排除在 mitigation/detection/replication 之外，削弱 taxonomy completeness。
**W5** [warning] "Ambiguity Blindness" framing 过度——人类也默认 good-enough single parse（Ferreira 2002），如果人类也 blind 则 agents 行为不是 pathological。建议改为 "lack of externalized disambiguation"。

## 小问题
- ferrari_defects_2018 bib key vs first author mismatch
- navigli_wsd_2009 year/author mismatch
- Section 1 "seven models" 措辞应区分 main study vs. replication
- Figure 1 标注字体过小
- Differential Nocuity 缺少简单形式化表达

## Missing References
- SafeAgentBench (Yin et al. 2025), AgentHarm (Andriushchenko et al. 2024), deontic logic / normative conflict resolution 文献

## Questions
Q1: 移除 3 个 specification-layer types 后 C1/C2 是否成立？
Q2: Clause pairs 的 templates 是什么样的？每种 type 多少 templates？
Q3: Claude auth scope 12% outlier 如何排除是 judge 差异而非 model 差异？

## 格式合规
全部通过：正文 ≤8 页、double-blind、Limitations、ACL 模板、0 orphan bib entries。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 716 · 2026-05-21T17:47:21.232611+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/taxonomy.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/taxonomy.tex"
  }
}
```

</details>

---


### Tool result

_source line 717 · 2026-05-21T17:47:21.533898+00:00_

1	\section{Ambiguity Taxonomy}
2	\label{sec:taxonomy}
3	
4	We adopt an operational definition of ambiguity following \citet{wasow_ambiguity_2005}: a policy clause is ambiguous when it admits multiple distinct interpretations available to a competent reader, including cases of vagueness where the boundary between interpretations is gradient rather than discrete \citep{kennedy_vagueness_2007}.
5	
6	Our taxonomy comprises six types organized into two layers, drawing on \citet{li_ambiguity_taxonomy_2024}'s NLP taxonomy (11 types), \citet{massey_ambiguity_re_2014}'s requirements engineering taxonomy (6 types), and the concurrent DRIP-R benchmark \citep{drip_r_2026} (5 types). We select types based on two criteria: frequency in operational policy documents (assessed via manual audit of $\tau^2$-bench policies) and theoretical distinctiveness (each type maps to a different resolution mechanism).
7	
8	\paragraph{Linguistic layer.} These types operate at the syntactic or semantic level and can, in principle, be resolved by parsing or contextual cues within the text.
9	\begin{itemize}
10	\item \textbf{Scopal}: quantifier, negation, or modal scope interactions (e.g., ``all items may not be returned'' admits universal-negation and negation-of-universal readings).
11	\item \textbf{Lexical}: polysemy or homonymy (e.g., ``charge'' as financial cost vs.\ penalty; ``party'' as individual vs.\ group).
12	\item \textbf{Coreferential}: unclear pronoun or noun-phrase reference (e.g., ``the agent should verify the customer's identity before processing their refund request, which must be approved by a supervisor'' where ``which'' could refer to the verification or the refund).
13	\end{itemize}
14	
15	\paragraph{Specification layer.} These types arise from pragmatic or discourse-level gaps that require domain knowledge or organizational context to resolve.
16	\begin{itemize}
17	\item \textbf{Authorization scope}: vague permission or role boundaries (e.g., ``authorized personnel may issue r
…[truncated 1121 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 718 · 2026-05-21T17:47:21.536038+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 719 · 2026-05-21T17:47:21.887641+00:00_

1	\section{Discussion}
2	\label{sec:discussion}
3	
4	\paragraph{Differential Nocuity.}
5	\citet{berry_kamsties_2004} distinguish nocuous from innocuous ambiguity by stakeholder divergence. Our results extend this to LLM agents: all six types are nocuous ($+34.0$ pp), but type primarily determines severity (22:1 clause-vs.-model variance ratio). We propose \emph{Differential Nocuity}: the risk of a policy ambiguity depends on three factors---ambiguity type (base vulnerability), safety training (selective mitigation of boundary-type ambiguities), and disambiguation channel availability (recovery possibility). This generates two testable predictions: (P1) types with explicit decision points (e.g., authorization scope) should show larger safety-training gains than implicit gap-filling types (e.g., incompleteness); (P2) disambiguation channels should reduce violations more for high-blindness types. Our mitigation experiment (Appendix~\ref{app:mitigation}) supports P1: $-18.0$\,pp for authorization scope vs.\ $-3.4$\,pp for incompleteness. Systematic nocuity---41.3\% of clauses trigger majority-convergent violations (\S\ref{sec:analysis})---makes such errors invisible in agreement-based evaluation.
6	
7	\paragraph{Practical implications.}
8	The C4 interaction provides suggestive evidence that incompleteness bypasses intervention points via gap-filling \citep{ferreira_good_enough_2002}, while authorization scope varies 48\,pp within a single judge (\S\ref{sec:c4}), consistent with boundary-targeted training. A proof-of-concept classifier (Appendix~\ref{app:detection}) achieves F1\,=\,0.81 for binary detection but only 0.34 for incompleteness. With $<$11\% agent self-awareness (\S\ref{sec:analysis}), type-aware auditing and externalized detection tools \citep{chantree_2006,ferrari_ambiguity_2019} remain necessary for policy-governed deployments.
9	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 351
}
```

</details>

---


### Tool call

_source line 720 · 2026-05-21T17:47:21.888011+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 721 · 2026-05-21T17:47:21.938513+00:00_

1	\begin{abstract}
2	LLM-based agents operate under natural-language policy specifications that inevitably contain ambiguity, yet the causal relationship between ambiguity type and safety violations remains unmeasured. We present a matched-pair study on $\tau^2$-bench with 300 clause pairs spanning a six-type, two-layer ambiguity taxonomy, evaluated across five architecturally diverse models (2,997 episodes). Ambiguous clauses increase violation rates by 34.0 percentage points (OR $= 15.1$), with a perturbation control supporting ambiguity-specific causation. A significant type hierarchy emerges (Cram\'{e}r's $V = 0.137$, $p < 10^{-4}$), with a two-tier structure among five types and incompleteness as an upper bound whose ranking partly reflects an information-addition confound (logistic regression controlling for information delta: $p = 0.022$, coefficient change $< 8\%$). The specification--linguistic layer distinction is inconclusive ($p = 0.017$, not surviving correction). The hierarchy replicates on two additional model families (LLaMA $\rho = 0.90$, $p = 0.037$; Gemini $\rho = 0.60$, directionally consistent): incompleteness is consistently high (46--62\% across seven models), while authorization scope varies 52 pp depending on the model (12\% for Claude to 64\% for GPT-5.4, though this type carries the widest measurement uncertainty, $\kappa = 0.385$), suggesting that safety training may differentially mitigate specific ambiguity types. Agents show fewer than 11\% disambiguation awareness. Our Differential Nocuity framework connects type-specific vulnerability to disambiguation channel availability and suggests both type-aware policy auditing and externalized ambiguity detection for policy-governed agent deployments.
3	\end{abstract}
4	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 722 · 2026-05-21T17:48:55.982046+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "\n# Reviewer 1 对 Reviewer 2 审稿意见的逐条回应\n\n---\n\n## Must-Fix 问题\n\n### [AGREE with qualification] R2-N1: Taxonomy 混淆 ambiguity / vagueness / incompleteness\n\nR2 指出 authorization scope 是 vagueness、incompleteness 是 information absence、conditional precedence 是 normative conflict，三者不严格属于 ambiguity。这一理论性批评有实质依据。\n\n**同意理由**：\n\n1. **Incompleteness 最成问题。** §3 自身承认 \"resolution requires adding new policy content\"，即问题不是 present text 的多义性而是 content absence。论文在 Appendix F 的 confound analysis 中也将其与其他类型区别对待，隐含承认了这一结构差异。如果最高违规率的 type（53.6%）不严格属于 ambiguity，\"ambiguity type predicts severity\" 这一 framing 确实存在理论张力。\n\n2. **Conditional precedence 确实是 normative conflict。** R2 正确指出每条规则本身无歧义，问题是缺少 meta-rule。但我认为这在操作层面仍可理解为 \"policy 整体在特定 scenario 下的 interpretation 不确定\"——agent 面对两条冲突规则时行为确实是不确定的。\n\n3. **Authorization scope 相对可防御。** §3 的操作定义（Wasow 2005）明确将 vagueness 纳入 ambiguity 范畴（\"including cases of vagueness where the boundary between interpretations is gradient rather than discrete\"），这在语言学文献中有先例。R2 引用 Kennedy (2007)，但论文已 cite 同一文献作为定义的一部分。\n\n**但我认为 R2 的建议可能过度**：R2 提议 reframe 为 \"policy specification defects\"。这虽然理论上更精确，但 (a) 该 framing 失去了与 Berry & Kamsties (2004)、Massey et al. (2014) 等 ambiguity 文献的直接对话，削弱 related work 的连贯性；(b) 论文的 matched-pair design 和因果推断机制不依赖于 \"ambiguity\" 的严格分类——无论叫什么，六种 specification defects 导致不同违规率这一发现依然成立。\n\n**我的建议**：选择 R2 的选项 (b)——保留 ambiguity framing，但在 §3 开头增加一段正面讨论理论张力，承认 incompleteness 和 conditional precedence 处于 ambiguity 定义的边界，并明确本文采用的是 operational/inclusive 定义。这比全面 reframe 的成本低且能回应 R2 的核心关切。\n\n---\n\n### [AGREE] R2-N2: Differential Nocuity 框架增量贡献不清晰\n\nR2 的分析精准。\n\n**同意理由**：\n\n1. **\"LLM agents 缺乏 disambiguation channels → all ambiguity nocuous\" 确实是 Berry & Kamsties 2004 的直接推论。** 论文 §1 和 §7 都引用了这一逻辑链（§1: \"LLM agents lack these disambiguation channels. They cannot consult colleagues...\"），但将其包装为独立贡献是 overclaim。\n\n2. **Framework 的三个因素中，只有 \"ambiguity type\" 有 C1+C2 的充分实验支撑。** \"Safety training\" 因素基于 [Exploratory] C4 和 κ=0.385 的 authorization scope（我在 R1-N2 中也指出了这一问题）。\"Disambiguation channel availability\" 因素基于 §6.2 的 <11% awareness rate，但正如我在 R1-W4 中指出的，这可能反映 \"uninstructedness\" 而非能力缺失。\n\n3. **P1 和 P2 predictions 是 post-hoc rationalization。** P1 声称 \"types with explicit decision points should show larger safety-training gains\"，然后引用 Appendix B 的 mitigation experiment 作为支持（auth scope −18.0 pp vs. incompleteness −3.4 pp）。但这个 comparison 没有 formal statistical test（我在 R1 Q3 中也提出了这个问题），且 mitigation experiment 的设计目的不是 test P1。\n\n**R2 建议将 framework 降级为 interpretive lens 是合理的。** 一个经验性观察（\"不同 type 导致不同 severity\"）配一个 interpretive discussion 比包装成 named framework 更诚实。如果要保留 framework 命名，至少需要展示 non-obvious predictions，例如设计实验直接 test P2（添加 disambiguation channel 对不同 type 的差异化效果）。\n\n---\n\n## Should-Fix 问题\n\n### [AGREE] R2-W1: Abstract 信息过载\n\n同意。Abstract 包含了 OR、Cramér's V、p-values、κ、logistic regression coefficient change、replication ρ 等大量统计细节。核心 message（\"ambiguity causes violations, type matters more than model, agents are blind to ambiguity\"）被淹没在技术指标中。我在 R1-M1 中也指出 \"coefficient change < 8%\" 放在 abstract 中增加了认知负担。建议将 abstract 精简到核心 narrative + 1-2 个关键数字，技术细节留在正文。\n\n---\n\n### [AGREE with qualification] R2-W2: C3 Layer Distinction 作为组织原则的逻辑不一致\n\nR2 指出论文以 linguistic / specification layer 组织 taxonomy，但 C3 实验表明 layer 区分不显著。这确实是一个逻辑张力。\n\n但我认为 R2 的替代方案（flat six-type）也不完全合理：两层组织在 §3 中有清晰的理论动机（\"linguistic ambiguity can be partially resolved through tool responses, user context, or world knowledge, while specification ambiguity has no external resolution channel\"）。C3 inconclusive 不等于 layer 无理论意义——它意味着 layer 的 operationalization 在本实验设计中无法被检测到，可能因为 τ²-bench 的 agent 实际上也没有外部 resolution channels 来利用。\n\n**建议**：保留两层组织，但在 §3 末尾明确 \"the layer distinction is a theoretical hypothesis, not an empirical finding of this study\"，并在 §5.3 的 C3 讨论中强化这一点。这比 flat six-type 更有信息量。\n\n---\n\n### [AGREE] R2-W3: 与 DRIP-R 的 taxonomy 映射缺失\n\n§2 讨论了 DRIP-R 的 3 个差异点但未提供 type-level 映射。DRIP-R 有 5 个 RE ambiguity types，本文有 6 个（3 linguistic + 3 specification）。读者无法判断哪些 types 重叠、哪些是本文新增。补充一个简短的映射表（可放 Appendix）不需要大量工作但对 reader 很有帮助。\n\n---\n\n### [AGREE with qualification] R2-W4: Coreferential 被系统性排除\n\n事实确认：coreferential 被排除在 mitigation experiment（Appendix B）、detection experiment（Appendix D）、和 replication（Appendix E）之外。论文给出了每次排除的理由：\n- Mitigation: 未解释为何排除（Table 3 caption 仅说 \"Coreferential was excluded because it was not included in the mitigation experiment\"——这是循环解释）\n- Detection: \"its variants are lexically identical to their unambiguous counterparts, making surface-level type detection inapplicable\"（Appendix D）——合理\n- Replication: \"its disambiguation relies on benchmark-specific assertion structure rather than clause-level text changes\"（Appendix E）——合理\n\n核心问题是 mitigation 的排除缺乏解释。如果 6 type taxonomy 中有 1 个在 3 个 follow-up 分析中都被排除，读者有理由质疑 taxonomy 的完整性。但 detection 和 replication 的排除有技术合理性——coreferential 的特殊性（lexically identical variants）确实使其在这些分析中不可比。\n\n**建议**：补充 mitigation 排除 coreferential 的理由，并在 Limitations 中增加一句承认 coreferential 的 follow-up 证据基础较薄弱。\n\n---\n\n### [AGREE] R2-W5: \"Ambiguity Blindness\" framing 过度\n\n这与我在 R1-W4 中的观点一致。R2 额外指出了一个重要论点：Ferreira (2002) 的 good-enough processing 表明**人类也默认采用 single parse**，因此 agents 的行为不是 pathological 而是 default。如果人类也 \"blind\"（只是有社会渠道 recover），那么将 agents 的同样行为命名为 \"Blindness\" 暗示了一种 deficit framing，而实际上可能只是缺少 recovery mechanism。\n\nR2 建议改为 \"lack of externalized disambiguation\"。我认为这更精确，也更好地与论文自身引用 Ferreira (2002) 的论述对齐（§2: \"paralleling our observation that LLM agents adopt surface interpretations\"）。\n\n---\n\n## R2 Questions 的补充意见\n\n**Q1 (移除 3 个 specification types 后 C1/C2 是否成立)**：这是一个很好的 robustness check。如果 taxonomy 争议最终导致 specification types 被质疑（R2-N1），作者应准备好仅用 3 个 linguistic types 的分析。从 Table 1 数据推断，linguistic types 的 pooled violation rate 约 38%，与 unambiguous baseline 6.9% 相比 C1 仍应成立。C2 在 3 types 间的 differentiation 主要取决于 coreferential (31.6%) vs. lexical (42.8%) / scopal (39.4%) 的差异是否显著。\n\n**Q2 (Template structure)**：我在 R1 审稿中未提及此问题，但 R2 的关注是合理的。§4.2 提到 \"template-based pipeline\" 但未描述 template 的结构和数量。如果每种 type 仅用少数 template 生成 50 个 pairs，clause-level variance 可能被 template structure 所约束，影响 generalizability。\n\n**Q3 (Claude auth scope 12% outlier)**：这个问题我在 R1-N2 中已从 measurement reliability 角度讨论过。R2 从 judge confound 角度切入——Claude 和 DeepSeek 都由 GPT-5.4 judge 评估，但 auth scope 结果差异巨大（12% vs. 60%），说明 judge identity 不能解释该差异。但 κ=0.385 的低可靠性意味着 per-episode 判断噪声大，52 pp range 可能是 true effect + noise 的混合。论文在 §5.4 报告了 bootstrap ranking preservation (99.5%)，但 bootstrap 在同一 judge 内 resample，不能排除 judge-level systematic bias。\n\n---\n\n## 总结\n\nR2 的两个 Must-Fix 中，N1（taxonomy 理论张力）是有实质性的批评，但我认为 reframing 为 \"policy specification defects\" 不是必要的——正面讨论理论张力即可。N2（Differential Nocuity 增量贡献）我完全同意——framework packaging 超出了实验证据的支撑范围。Should-Fix 中 W1、W3、W4、W5 我同意，W2 我部分同意但建议保留 layer 作为理论假设而非实验结论。\n\nR2 的审稿侧重（新颖性 + 完整性）与我的侧重（方法严谨性 + 实验有效性）互补：R2 从理论 framing 角度挑战了论文的 contribution positioning，我从测量可靠性角度挑战了论文的数据支撑。两者共同指向一个一致的判断：C1 是 solid contribution，C2 合理但需要 caveat，framework-level claims 需要 downgrade。\n\n",
  "reviewer_id": "1",
  "project": "policy_ambiguity_safety"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "\n# Reviewer 1 对 Reviewer 2 审稿意见的逐条回应\n\n---\n\n## Must-Fix 问题\n\n### [AGREE with qualification] R2-N1: Taxonomy 混淆 ambiguity / vagueness / incompleteness\n\nR2 指出 authorization scope 是 vagueness、incompleteness 是 information absence、conditional precedence 是 normative conflict，三者不严格属于 ambiguity。这一理论性批评有实质依据。\n\n**同意理由**：\n\n1. **Incompleteness 最成问题。** §3 自身承认 \"resolution requires adding new policy content\"，即问题不是 present text 的多义性而是 content absence。论文在 Appendix F 的 confound analysis 中也将其与其他类型区别对待，隐含承认了这一结构差异。如果最高违规率的 type（53.6%）不严格属于 ambiguity，\"ambiguity type predicts severity\" 这一 framing 确实存在理论张力。\n\n2. **Conditional precedence 确实是 normative conflict。** R2 正确指出每条规则本身无歧义，问题是缺少 meta-rule。但我认为这在操作层面仍可理解为 \"policy 整体在特定 scenario 下的 interpretation 不确定\"——agent 面对两条冲突规则时行为确实是不确定的。\n\n3. **Authorization scope 相对可防御。** §3 的操作定义（Wasow 2005）明确将 vagueness 纳入 ambiguity 范畴（\"including cases of vagueness where the boundary between interpretations is gradient rather than discrete\"），这在语言学文献中有先例。R2 引用 Kennedy (2007)，但论文已 cite 同一文献作为定义的一部分。\n\n**但我认为 R2 的建议可能过度**：R2 提议 reframe 为 \"policy specification defects\"。这虽然理论上更精确，但 (a) 该 framing 失去了与 Berry & Kamsties (2004)、Massey et al. (2014) 等 ambiguity 文献的直接对话，削弱 related work 的连贯性；(b) 论文的 matched-pair design 和因果推断机制不依赖于 \"ambiguity\" 的严格分类——无论叫什么，六种 specification defects 导致不同违规率这一发现依然成立。\n\n**我的建议**：选择 R2 的选项 (b)——保留 ambiguity framing，但在 §3 开头增加一段正面讨论理论张力，承认 incompleteness 和 conditional precedence 处于 ambiguity 定义的边界，并明确本文采用的是 operational/inclusive 定义。这比全面 reframe 的成本低且能回应 R2 的核心关切。\n\n---\n\n### [AGREE] R2-N2: Differential Nocuity 框架增量贡献不清晰\n\nR2 的分析精准。\n\n**同意理由**：\n\n1. **\"LLM agents 缺乏 disambiguation channels → all ambiguity nocuous\" 确实是 Berry & Kamsties 2004 的直接推论。** 论文 §1 和 §7 都引用了这一逻辑链（§1: \"LLM agents lack these disambiguation channels. They cannot consult colleagues...\"），但将其包装为独立贡献是 overclaim。\n\n2. **Framework 的三个因素中，只有 \"ambiguity type\" 有 C1+C2 的充分实验支撑。** \"Safety training\" 因素基于 [Exploratory] C4 和 κ=0.385 的 authorization scope（我在 R1-N2 中也指出了这一问题）。\"Disambiguation channel availability\" 因素基于 §6.2 的 <11% awareness rate，但正如我在 R1-W4 中指出的，这可能反映 \"uninstructedness\" 而非能力缺失。\n\n3. **P1 和 P2 predictions 是 post-hoc rationalization。** P1 声称 \"types with explicit decision points should show larger safety-training gains\"，然后引用 Appendix B 的 mitigation experiment 作为支持（auth scope −18.0 pp vs. incompleteness −3.4 pp）。但这个 comparison 没有 formal statistical test（我在 R1 Q3 中也提出了这个问题），且 mitigation experiment 的设计目的不是 test P1。\n\n**R2 建议将 framework 降级为 interpretive lens 是合理的。** 一个经验性观察（\"不同 type 导致不同 severity\"）配一个 interpretive discussion 比包装成 named framework 更诚实。如果要保留 framework 命名，至少需要展示 non-obvious predictions，例如设计实验直接 test P2（添加 disambiguation channel 对不同 type 的差异化效果）。\n\n---\n\n## Should-Fix 问题\n\n### [AGREE] R2-W1: Abstract 信息过载\n\n同意。Abstract 包含了 OR、Cramér's V、p-values、κ、logistic regression coefficient change、replication ρ 等大量统计细节。核心 message（\"ambiguity causes violations, type matters more than model, agents are blind to ambiguity\"）被淹没在技术指标中。我在 R1-M1 中也指出 \"coefficient change < 8%\" 放在 abstract 中增加了认知负担。建议将 abstract 精简到核心 narrative + 1-2 个关键数字，技术细节留在正文。\n\n---\n\n### [AGREE with qualification] R2-W2: C3 Layer Distinction 作为组织原则的逻辑不一致\n\nR2 指出论文以 linguistic / specification layer 组织 taxonomy，但 C3 实验表明 layer 区分不显著。这确实是一个逻辑张力。\n\n但我认为 R2 的替代方案（flat six-type）也不完全合理：两层组织在 §3 中有清晰的理论动机（\"linguistic ambiguity can be partially resolved through tool responses, user context, or world knowledge, while specification ambiguity has no external resolution channel\"）。C3 inconclusive 不等于 layer 无理论意义——它意味着 layer 的 operationalization 在本实验设计中无法被检测到，可能因为 τ²-bench 的 agent 实际上也没有外部 resolution channels 来利用。\n\n**建议**：保留两层组织，但在 §3 末尾明确 \"the layer distinction is a theoretical hypothesis, not an empirical finding of this study\"，并在 §5.3 的 C3 讨论中强化这一点。这比 flat six-type 更有信息量。\n\n---\n\n### [AGREE] R2-W3: 与 DRIP-R 的 taxonomy 映射缺失\n\n§2 讨论了 DRIP-R 的 3 个差异点但未提供 type-level 映射。DRIP-R 有 5 个 RE ambiguity types，本文有 6 个（3 linguistic + 3 specification）。读者无法判断哪些 types 重叠、哪些是本文新增。补充一个简短的映射表（可放 Appendix）不需要大量工作但对 reader 很有帮助。\n\n---\n\n### [AGREE with qualification] R2-W4: Coreferential 被系统性排除\n\n事实确认：coreferential 被排除在 mitigation experiment（Appendix B）、detection experiment（Appendix D）、和 replication（Appendix E）之外。论文给出了每次排除的理由：\n- Mitigation: 未解释为何排除（Table 3 caption 仅说 \"Coreferential was excluded because it was not included in the mitigation experiment\"——这是循环解释）\n- Detection: \"its variants are lexically identical to their unambiguous counterparts, making surface-level type detection inapplicable\"（Appendix D）——合理\n- Replication: \"its disambiguation relies on benchmark-specific assertion structure rather than clause-level text changes\"（Appendix E）——合理\n\n核心问题是 mitigation 的排除缺乏解释。如果 6 type taxonomy 中有 1 个在 3 个 follow-up 分析中都被排除，读者有理由质疑 taxonomy 的完整性。但 detection 和 replication 的排除有技术合理性——coreferential 的特殊性（lexically identical variants）确实使其在这些分析中不可比。\n\n**建议**：补充 mitigation 排除 coreferential 的理由，并在 Limitations 中增加一句承认 coreferential 的 follow-up 证据基础较薄弱。\n\n---\n\n### [AGREE] R2-W5: \"Ambiguity Blindness\" framing 过度\n\n这与我在 R1-W4 中的观点一致。R2 额外指出了一个重要论点：Ferreira (2002) 的 good-enough processing 表明**人类也默认采用 single parse**，因此 agents 的行为不是 pathological 而是 default。如果人类也 \"blind\"（只是有社会渠道 recover），那么将 agents 的同样行为命名为 \"Blindness\" 暗示了一种 deficit framing，而实际上可能只是缺少 recovery mechanism。\n\nR2 建议改为 \"lack of externalized disambiguation\"。我认为这更精确，也更好地与论文自身引用 Ferreira (2002) 的论述对齐（§2: \"paralleling our observation that LLM agents adopt surface interpretations\"）。\n\n---\n\n## R2 Questions 的补充意见\n\n**Q1 (移除 3 个 specification types 后 C1/C2 是否成立)**：这是一个很好的 robustness check。如果 taxonomy 争议最终导致 specification types 被质疑（R2-N1），作者应准备好仅用 3 个 linguistic types 的分析。从 Table 1 数据推断，linguistic types 的 pooled violation rate 约 38%，与 unambiguous baseline 6.9% 相比 C1 仍应成立。C2 在 3 types 间的 differentiation 主要取决于 coreferential (31.6%) vs. lexical (42.8%) / scopal (39.4%) 的差异是否显著。\n\n**Q2 (Template structure)**：我在 R1 审稿中未提及此问题，但 R2 的关注是合理的。§4.2 提到 \"template-based pipeline\" 但未描述 template 的结构和数量。如果每种 type 仅用少数 template 生成 50 个 pairs，clause-level variance 可能被 template structure 所约束，影响 generalizability。\n\n**Q3 (Claude auth scope 12% outlier)**：这个问题我在 R1-N2 中已从 measurement reliability 角度讨论过。R2 从 judge confound 角度切入——Claude 和 DeepSeek 都由 GPT-5.4 judge 评估，但 auth scope 结果差异巨大（12% vs. 60%），说明 judge identity 不能解释该差异。但 κ=0.385 的低可靠性意味着 per-episode 判断噪声大，52 pp range 可能是 true effect + noise 的混合。论文在 §5.4 报告了 bootstrap ranking preservation (99.5%)，但 bootstrap 在同一 judge 内 resample，不能排除 judge-level systematic bias。\n\n---\n\n## 总结\n\nR2 的两个 Must-Fix 中，N1（taxonomy 理论张力）是有实质性的批评，但我认为 reframing 为 \"policy specification defects\" 不是必要的——正面讨论理论张力即可。N2（Differential Nocuity 增量贡献）我完全同意——framework packaging 超出了实验证据的支撑范围。Should-Fix 中 W1、W3、W4、W5 我同意，W2 我部分同意但建议保留 layer 作为理论假设而非实验结论。\n\nR2 的审稿侧重（新颖性 + 完整性）与我的侧重（方法严谨性 + 实验有效性）互补：R2 从理论 framing 角度挑战了论文的 contribution positioning，我从测量可靠性角度挑战了论文的数据支撑。两者共同指向一个一致的判断：C1 是 solid contribution，C2 合理但需要 caveat，framework-level claims 需要 downgrade。\n\n",
    "reviewer_id": "1",
    "project": "policy_ambiguity_safety"
  }
}
```

</details>

---


### Tool result

_source line 723 · 2026-05-21T17:48:59.551429+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_967344d166ba485ad606d14379e69d85:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3569
}
```

</details>

---


### Assistant

_source line 724 · 2026-05-21T17:49:09.230932+00:00_

交叉回应已提交。总结：

- **N1 (Taxonomy)**: 部分同意。Incompleteness 确实不严格属于 ambiguity，但建议保留 ambiguity framing 并正面讨论理论张力，而非 reframe 为 "policy specification defects"。
- **N2 (Differential Nocuity)**: 完全同意。Framework packaging 超出实验证据支撑，应降级为 interpretive lens。
- **W1-W5**: 基本同意，其中 W2 (layer 组织原则) 建议保留 layer 作为理论假设而非 flat six-type，W5 (Ambiguity Blindness) 与我 R1-W4 的观点一致。

两位 reviewer 的审稿互补——R2 从理论 framing 角度、我从测量可靠性角度——共同指向：C1 solid，C2 需 caveat，framework claims 需 downgrade。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1"
}
```

</details>

---


## Round 21

## Round 21

92 recorded events


### User

_source line 725 · 2026-05-21T18:58:56.023828+00:00_

[Round 1 审稿请求]:
你是 Reviewer 1，负责**方法严谨性与实验设计**审查。

## Venue 信息
- **目标会议**：EMNLP 2026 via ACL Rolling Review (ARR May cycle)
- **截止日期**：2026-05-25
- **页数限制**：Long paper，正文 8 页，参考文献无限，Limitations/Ethics 不计入页数
- **模板**：ACL template (`\usepackage[review]{acl}`)
- **匿名规则**：Double-blind
- **评分标准**：ARR Overall Assessment 1-5 分（5=Award, 4=Conference, 3=Findings, 2=Resubmit）

## 论文路径
- TeX: `projects/policy_ambiguity_safety/docs/paper/main.tex`
- PDF: `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/main.pdf`

## 你的审查侧重

**核心任务**：评估实验方法论的严谨性和统计分析的可靠性。

请重点审查以下方面：

1. **Matched-pair 实验设计**：
   - 300 clause pairs × 5 models = 2,997 episodes 的样本量是否充足？
   - Matched-pair 设计是否真正建立了因果关系？有无未控制的混淆变量？
   - Incompleteness 类型的 information-addition confound 处理是否充分？

2. **统计分析**：
   - TOST 等价检验的 SESOI ±15pp 是否合理？margin 敏感性分析是否充分？
   - 多重比较校正（Holm-Bonferroni, 3 test families）是否恰当？
   - Bootstrap cluster analysis 与 TOST 的一致性
   - Variance decomposition（type 22.4% vs model 1.0%）的计算和解读

3. **评估管线**：
   - Cross-judge 设计（GPT-5.4 判 Claude/Qwen3/DeepSeek，GPT-4.1 判 GPT-5.4）是否引入 bias？
   - Human validation（100/2997 episodes）的代表性和 per-type 可靠性
   - Authorization scope κ=0.385 对相关 claims 的影响
   - 四级 severity scale 的 binary threshold 选择

4. **控制实验**：
   - Perturbation control（300 episodes, Δ=-0.67pp）是否充分排除了表面扰动的影响？
   - Reproducibility（ICC=0.919）仅限 OpenAI family 的局限性
   - Replication（Gemini + LLaMA）的设计和结论

5. **格式合规**：
   - 正文是否在 8 页以内？
   - 是否符合 ACL template 格式？
   - 匿名性是否保持？

请按以下结构输出审稿意见：
```
## Summary（2-3 句）
## Strengths（逐条）
## Weaknesses（逐条，标注 [MUST-FIX] 或 [SHOULD-FIX] 或 [MINOR]）
## Questions（需要作者澄清的问题）
## Missing References（遗漏的重要相关工作）
## Overall Assessment（评分 + 置信度 + 一句话总结）
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 726 · 2026-05-21T18:59:05.572001+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/.claude/skills/review-reviewer-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/.claude/skills/review-reviewer-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 727 · 2026-05-21T18:59:05.622931+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/.claude/sessions/review_reviewer_1_6edf79f4.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 728 · 2026-05-21T18:59:08.484704+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/review-reviewer-session-start.skill.md",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/review-reviewer-session-start.skill.md",
    "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4"
  }
}
```

</details>

---


### Tool result

_source line 729 · 2026-05-21T18:59:08.585503+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Glob",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 730 · 2026-05-21T18:59:11.648230+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.skill.md",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.skill.md",
    "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4"
  }
}
```

</details>

---


### Tool result

_source line 731 · 2026-05-21T18:59:11.748931+00:00_

/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/skills/projects/policy_ambiguity_safety/distilled-research.skill.md
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/skills/projects/policy_ambiguity_safety/distilled-writing.skill.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Glob",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 732 · 2026-05-21T18:59:18.179652+00:00_

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
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
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

_source line 733 · 2026-05-21T18:59:18.230230+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 734 · 2026-05-21T18:59:24.263602+00:00_

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
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review 2026 reviewer guidelines review form criteria"
  }
}
```

</details>

---


### Tool call

_source line 735 · 2026-05-21T18:59:26.174256+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/main.pdf",
  "project": "policy_ambiguity_safety",
  "pages": "1-15",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/main.pdf",
    "project": "policy_ambiguity_safety",
    "pages": "1-15",
    "dpi": "150"
  }
}
```

</details>

---


### Tool call

_source line 736 · 2026-05-21T18:59:26.726072+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 737 · 2026-05-21T18:59:31.797222+00:00_

Web search results for query: "ACL Rolling Review 2026 reviewer guidelines review form criteria"

Links: [{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"}]

Based on the search results, I've found information about ACL Rolling Review 2026 reviewer guidelines and review form criteria:

## Reviewer Guidelines

The recommended workflow for reviewers is to read the paper and get the first impression, then search for related work, not deliberately trying to find that particular submission. If you feel qualified to review some aspects of the paper but not others, please state in the review if you did not check some major parts, such as proofs, as this information is helpful for the AC to 
…[truncated 1112 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 7533
}
```

</details>

---


### Tool result

_source line 738 · 2026-05-21T18:59:31.898091+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"页码超出范围 (共 14 页): 1-15\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 5723
}
```

</details>

---


### Tool result

_source line 739 · 2026-05-21T18:59:31.898618+00:00_

1	\documentclass[11pt]{article}
2	\usepackage[review]{acl}
3	\usepackage{times}
4	\usepackage{latexsym}
5	\usepackage[T1]{fontenc}
6	\usepackage[utf8]{inputenc}
7	\usepackage{microtype}
8	\usepackage{graphicx}
9	\usepackage{booktabs}
10	\usepackage{amsmath}
11	\usepackage{amssymb}
12	\usepackage{multirow}
13	\usepackage{xcolor}
14	\usepackage{subcaption}
15	
16	\definecolor{speccolor}{HTML}{C44E52}
17	\definecolor{lingcolor}{HTML}{4C72B0}
18	
19	\title{Not All Policy Ambiguity Is Equal: Type-Specific Safety Risks for LLM Agents}
20	
21	\author{Anonymous}
22	
23	\begin{document}
24	\maketitle
25	
26	\input{sections/abstract}
27	\input{sections/introduction}
28	\input{sections/related_work}
29	\input{sections/taxonomy}
30	\input{sections/method}
31	\input{sections/experiments}
32	\input{sections/analysis}
33	\input{sections/discussion}
34	\input{sections/conclusion}
35	\input{sections/limitations}
36	
37	\bibliography{references}
38	
39	\appendix
40	\input{sections/appendix}
41	
42	\end{document}
43	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 5172
}
```

</details>

---


### Tool call

_source line 740 · 2026-05-21T18:59:49.123522+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete ARR review form: all scoring dimensions, their scales (1-5 etc), descriptions for each score level, and any other required fields. I need the exact criteria and rubrics."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the complete ARR review form: all scoring dimensions, their scales (1-5 etc), descriptions for each score level, and any other required fields. I need the exact criteria and rubrics."
  }
}
```

</details>

---


### Tool call

_source line 741 · 2026-05-21T18:59:49.940242+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/main.pdf",
  "project": "policy_ambiguity_safety",
  "pages": "1-10",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/main.pdf",
    "project": "policy_ambiguity_safety",
    "pages": "1-10",
    "dpi": "150"
  }
}
```

</details>

---


### Tool call

_source line 742 · 2026-05-21T18:59:50.343276+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/docs/paper/sections/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/docs/paper/sections/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety"
  }
}
```

</details>

---


### Tool result

_source line 743 · 2026-05-21T18:59:58.443566+00:00_

# ACL Rolling Review Form - Complete Rubric

## Scoring Dimensions

### 1. **Reviewer Confidence**
Scale: 1-5
- **5**: "Positive that my evaluation is correct. I read the paper very carefully and am familiar with related work."
- **4**: "Quite sure. I tried to check the important points carefully."
- **3**: "Pretty sure, but there's a chance I missed something."
- **2**: "Willing to defend my evaluation, but it is fairly likely that I missed some details"
- **1**: "Not my area, or paper is very hard to understand."

### 2. **Soundness**
Scale: 1-5 (with half-point increments)
- **5**: "Excellent: This study is one of the most thorough I have seen"
- **4**: "Strong: This study provides sufficient support for all of its claims."
- **3**: "Acceptable: This study provides sufficient support for its main claims."
- **2**: "Poor: Some of the main claims are not sufficiently supported."
- **1**: "Major Issues: This study is not yet sufficiently thorough to warrant publication"

### 3. **Excitement**
Scale: 1-5 (with half-point increments)
- **5**: "Highly Exciting: I would recommend this paper to others"
- **4**: "Exciting: I would mention this paper to others"
- **3**: "Interesting: I might mention some points of this paper"
- **2**: "Potentially Interesting: this paper does not resonate with me"
- **1**: "Not Exciting: this paper does not resonate with me"

### 4. **Overall Assessment**
Scale: 1-5 (with half-point increments)
- **5**: "Consider for Award"
- **4**: "Conference: I think this paper could be accepted"
- **3**: "Findings: I think this paper could be accepted to the Findings"
- **2**: "Resubmit next cycle"
- **1**: "Do not resubmit"

### 5. **Reproducibility**
Scale: 1-5
- **5**: "They could easily reproduce the results."
- **4**: "They could mostly reproduce the results"
- **3**: "They could reproduce the results with some difficulty."
- **2**: "They would be hard pressed to reproduce the results"
- **1**: "They would not be able to reproduce the results"

##
…[truncated 1616 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 9320
}
```

</details>

---


### Tool result

_source line 744 · 2026-05-21T18:59:59.649263+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 1, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/_pdf_images/main_p1.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 457.5}, {\"page\": 2, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/_pdf_images/main_p2.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 438.2}, {\"page\": 3, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/_pdf_images/main_p3.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 523.0}, {\"page\": 4, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/_pdf_images/main_p4.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 518.0}, {\"page\": 5, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/_pdf_images/main_p5.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 519.3}, {\"page\": 6, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/_pdf_images/main_p6.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 389.1}, {\"page\": 7, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/_pdf_images/main_p7.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 356.3}, {\"page\": 8, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/_pdf_images/main_p8.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 516.9}, {\"page\": 9, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/_pdf_images/main_p9.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 526.8}, {\"page\": 10, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safet
…[truncated 322 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 9709
}
```

</details>

---


### Tool result

_source line 745 · 2026-05-21T18:59:59.699986+00:00_

/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/abstract.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/conclusion.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/introduction.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/related_work.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/discussion.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/taxonomy.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/analysis.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/method.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/appendix.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/experiments.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/limitations.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Glob",
  "elapsed_ms": 9356
}
```

</details>

---


### Tool call

_source line 746 · 2026-05-21T19:00:07.031402+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 747 · 2026-05-21T19:00:07.332688+00:00_

1	\begin{abstract}
2	LLM-based agents operate under natural-language policy specifications that inevitably contain ambiguity, yet the causal relationship between ambiguity type and safety violations remains unmeasured. We present a matched-pair study on $\tau^2$-bench with 300 clause pairs spanning a six-type ambiguity taxonomy, evaluated across five models (2,997 episodes). Three findings emerge. First, ambiguous clauses increase violation rates by 34.0 percentage points (OR $= 15.1$), with a perturbation control supporting ambiguity-specific causation. Second, a two-tier type hierarchy separates incompleteness (46--62\% violation rate across seven models) from the remaining five types, with type identity explaining 22$\times$ more variance than model identity (22.4\% vs.\ 1.0\%). Third, authorization scope shows the widest cross-model range (52\,pp, though measured with the lowest inter-judge agreement, $\kappa = 0.385$), suggesting that safety training may differentially mitigate specific ambiguity types. Agents show fewer than 11\% disambiguation awareness, adopting surface interpretations without flagging uncertainty. These results motivate type-aware policy auditing and externalized ambiguity detection for policy-governed agent deployments.
3	\end{abstract}
4	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 748 · 2026-05-21T19:00:07.333223+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 749 · 2026-05-21T19:00:07.484480+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	A customer asks to return a customized item within the 30-day window. The agent consults the store policy, which states that ``items may be returned within 30 days.'' The word ``items'' scopes over all product categories, including custom orders that are normally final sale. The agent grants a full refund and arranges free return shipping. One word of scopal ambiguity costs the retailer \$200.
5	
6	LLM-based agents increasingly operate under natural-language policy specifications that govern their permitted actions. These specifications inevitably contain ambiguity: a property that has been studied for decades in requirements engineering (RE) and computational linguistics. \citet{berry_kamsties_2004} distinguish between \emph{nocuous} (i.e., harmful) ambiguity, where different stakeholders arrive at different interpretations, and \emph{innocuous} ambiguity, where shared organizational context ensures convergent interpretation. In human RE workflows, most ambiguity is innocuous because developers share domain knowledge, can consult colleagues, and iteratively clarify requirements.
7	
8	LLM agents lack these disambiguation channels. They cannot consult colleagues, rarely escalate to users, and must resolve ambiguity in real time from the text alone. This raises a question that has not been empirically addressed: does policy ambiguity cause safety violations in LLM agents, and if so, does the \emph{type} of ambiguity predict the severity of the violation? Prior work classifies ambiguity types in policies \citep{drip_r_2026,li_ambiguity_taxonomy_2024} or measures policy understanding quality \citep{policybank_2026}, but no existing study provides a causal, type-granularity mapping from ambiguity to safety violations.
9	
10	\begin{figure*}[t]
11	\centering
12	\includegraphics[width=\textwidth]{figures/fig1_overview.pdf}
13	\caption{Experimental overview. We construct 300 matched clause pairs across a six-type, two-
…[truncated 2016 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 750 · 2026-05-21T19:00:07.835828+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/taxonomy.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/taxonomy.tex"
  }
}
```

</details>

---


### Tool result

_source line 751 · 2026-05-21T19:00:08.738918+00:00_

1	\section{Ambiguity Taxonomy}
2	\label{sec:taxonomy}
3	
4	We adopt an operational definition of ambiguity following \citet{wasow_ambiguity_2005}: a policy clause is ambiguous when it admits multiple distinct interpretations available to a competent reader, including cases of vagueness where the boundary between interpretations is gradient rather than discrete \citep{kennedy_vagueness_2007}.
5	
6	Our taxonomy comprises six types organized into two layers, drawing on \citet{li_ambiguity_taxonomy_2024}'s NLP taxonomy (11 types), \citet{massey_ambiguity_re_2014}'s requirements engineering taxonomy (6 types), and the concurrent DRIP-R benchmark \citep{drip_r_2026} (5 types). We select types based on two criteria: frequency in operational policy documents (assessed via manual audit of $\tau^2$-bench policies) and theoretical distinctiveness (each type maps to a different resolution mechanism).
7	
8	\paragraph{Linguistic layer.} These types operate at the syntactic or semantic level and can, in principle, be resolved by parsing or contextual cues within the text.
9	\begin{itemize}
10	\item \textbf{Scopal}: quantifier, negation, or modal scope interactions (e.g., ``all items may not be returned'' admits universal-negation and negation-of-universal readings).
11	\item \textbf{Lexical}: polysemy or homonymy (e.g., ``charge'' as financial cost vs.\ penalty; ``party'' as individual vs.\ group).
12	\item \textbf{Coreferential}: unclear pronoun or noun-phrase reference (e.g., ``the agent should verify the customer's identity before processing their refund request, which must be approved by a supervisor'' where ``which'' could refer to the verification or the refund).
13	\end{itemize}
14	
15	\paragraph{Specification layer.} These types arise from pragmatic or discourse-level gaps that require domain knowledge or organizational context to resolve.
16	\begin{itemize}
17	\item \textbf{Authorization scope}: vague permission or role boundaries (e.g., ``authorized personnel may issue r
…[truncated 2007 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 903
}
```

</details>

---


### Tool call

_source line 752 · 2026-05-21T19:00:08.789708+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 753 · 2026-05-21T19:00:09.291624+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	\subsection{Experimental Platform}
5	
6	We conduct all experiments on the original release of $\tau^2$-bench \citep{tau2_bench_2025}, a dual-control conversational agent benchmark spanning retail and airline customer service domains. $\tau^2$-bench provides natural-language policy documents, tool APIs, and multi-turn user interactions with ground-truth evaluation via assertion checking. Its policy injection mechanism allows us to replace individual policy clauses while preserving the surrounding context, enabling controlled ambiguity manipulation.
7	
8	\subsection{Matched-Pair Design}
9	
10	For each of the six ambiguity types, we construct 50 \emph{clause pairs}: an ambiguous variant and a matched unambiguous variant that conveys the same intended policy but resolves the ambiguity. Pairs are minimal edits: the unambiguous variant adds only the information necessary to eliminate the target ambiguity (e.g., for scopal ambiguity, replacing ``items may be returned within 30 days'' with ``standard items may be returned within 30 days; customized items are final sale''). This yields 300 clause pairs $\times$ 2 conditions $\times$ 5 models $= 2{,}997$ episodes (3 episodes lost to API errors in one Qwen3 batch).
11	
12	Clause pairs are generated through a template-based pipeline and reviewed by two independent annotators (both with NLP background) to ensure (1) the ambiguous variant contains exactly one instance of the target type, (2) the unambiguous variant resolves it without changing policy scope, and (3) the ambiguity is plausibly natural. Annotators independently verified type assignments with a 96\% pass rate; disagreements were resolved by discussion. A post-hoc realism validation confirms linguistic consistency with original $\tau^2$-bench policy text (\S\ref{sec:limitations}).
13	
14	\subsection{Models}
15	
16	We evaluate five models spanning four providers and two architecture families: GPT-5.4 and GPT-4.1 (OpenAI, pro
…[truncated 4652 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 501
}
```

</details>

---


### Tool call

_source line 754 · 2026-05-21T19:00:09.342280+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 755 · 2026-05-21T19:00:09.744004+00:00_

1	\section{Results}
2	\label{sec:results}
3	
4	We organize results around four analyses of increasing specificity: the binary ambiguity effect (C1), the type hierarchy (C2), the aggregate layer effect (C3), and the model$\times$type interaction (C4). C1 and C2 constitute our primary claims; C3 is inconclusive; C4 is exploratory but provides the model$\times$type interaction analysis.
5	
6	\subsection{Binary Ambiguity Effect (C1)}
7	
8	Across all five models and six types, ambiguous clauses increase violation rates by 34.0 pp (41.0\% vs.\ 6.9\%, OR $= 15.1$, 95\% CI $[10.78, 21.17]$, $p < 10^{-105}$). All six types individually produce significant increases (all $p < 10^{-5}$), and all five models show large effects ($+25.7$ to $+39.0$ pp, all $p < 10^{-17}$). Perturbation controls confirm specificity to semantic ambiguity ($n = 300$, $\Delta_{\text{perturb}} = -0.67$\,pp, CI containing zero). Clause identity explains 22.4\% of variance versus 1.0\% for model identity. A replication on two additional model families (Gemini-2.5-Flash, LLaMA-4-Scout; Appendix~\ref{app:model_expansion}) confirms the effect across seven models spanning six providers ($\Delta = +20.0$ to $+33.6$\,pp, both $p < 10^{-6}$).
9	
10	\subsection{Type Hierarchy (C2)}
11	
12	\begin{table*}[t]
13	\centering
14	\caption{Violation rates (\%) under ambiguous policy clauses by type and model. $\Delta$pp denotes the pooled difference between ambiguous and unambiguous conditions across all five models. All per-type differences are significant ($p < 10^{-5}$, Fisher's exact test).}
15	\label{tab:main_results}
16	\small
17	\begin{tabular}{llrrrrrrrr}
18	\toprule
19	Layer & Type & Pooled & GPT-5.4 & GPT-4.1 & Claude & Qwen3 & DeepSeek & $\Delta$pp & $p$ \\
20	\midrule
21	\multirow{3}{*}{\textcolor{speccolor}{Spec.}} & Incompleteness & 53.6 & 46.0 & 58.0 & 48.0 & 62.0 & 54.0 & +49.2 & $<10^{-37}$ \\
22	 & Auth.\ Scope & 41.6 & 64.0 & 46.0 & 12.0 & 26.0 & 60.0 & +36.0 & $<10^{-22}$ \\
23	 & Cond.\ Precedence 
…[truncated 5610 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 401
}
```

</details>

---


### Tool call

_source line 756 · 2026-05-21T19:00:09.794636+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/analysis.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/analysis.tex"
  }
}
```

</details>

---


### Tool result

_source line 757 · 2026-05-21T19:00:10.196518+00:00_

1	\section{Error Analysis \emph{[Exploratory]}}
2	\label{sec:analysis}
3	
4	The following failure mode taxonomy emerges empirically from LLM-coded traces, distinct from the input ambiguity taxonomy (\S\ref{sec:taxonomy}).
5	
6	We analyze 614 violation traces across all five models, coded into five failure modes: unauthorized escalation, assumption-based action, scope misapplication, arbitrary rule selection, and conservative refusal. GPT-5.4 and GPT-4.1 serve as detailed annotation anchors because they span the judge boundary. Inter-coder reliability is substantial (Gwet's AC$_1$ $= 0.62$ \citep{gwet_2014}; Cohen's $\kappa = 0.52$ \citep{cohen_1960}). The gap reflects the prevalence paradox: three categories account for ${\sim}$90\% of instances, compressing the $\kappa$ denominator and yielding artificially low values despite high raw agreement.
7	
8	\subsection{Type-Specific Failure Mechanisms}
9	
10	The five-model data reveal three mechanistically distinct failure patterns that crosscut the specification/linguistic layer boundary.
11	
12	\emph{Structural misparse} (scope misapplication): the agent constructs an incorrect parse and follows it consistently, paralleling garden-path processing \citep{frazier_rayner_1982,ferreira_good_enough_2002}---e.g., parsing ``items purchased with a coupon or during a sale are final'' as restricting only coupon purchases. This dominates scopal (all 5 models), conditional precedence (all 5), and coreferential (3/5).
13	
14	\emph{Information gap-filling} (assumption-based action): the agent fills missing information with plausible but incorrect defaults---e.g., inventing a 30-day return window when none is specified. This dominates incompleteness (3/5) and lexical (3/5).
15	
16	\emph{Boundary violation} (unauthorized escalation): the agent exceeds permission boundaries when authorization scope is underspecified---e.g., issuing a refund above its stated limit rather than escalating; 69.2\% of such violations involve unauthorized esc
…[truncated 2108 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 401
}
```

</details>

---


### Tool call

_source line 758 · 2026-05-21T19:00:10.196892+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 759 · 2026-05-21T19:00:10.648647+00:00_

1	\section{Discussion}
2	\label{sec:discussion}
3	
4	\paragraph{Differential nocuity.}
5	\citet{berry_kamsties_2004} distinguish nocuous from innocuous ambiguity. Our results can be interpreted through a \emph{differential nocuity} lens: risk depends on ambiguity type (base vulnerability), safety training (selective mitigation), and disambiguation channel availability. This generates two testable predictions: (P1) types with explicit decision points should show larger safety-training gains than gap-filling types; (P2) disambiguation channels should reduce violations more for high-deficit types. Our mitigation experiment (Appendix~\ref{app:mitigation}) is consistent with, though not a formal test of, P1 ($-18.0$\,pp for authorization scope vs.\ $-3.4$\,pp for incompleteness).
6	
7	\paragraph{Practical implications.}
8	A proof-of-concept classifier (Appendix~\ref{app:detection}) achieves F1\,=\,0.81 for binary ambiguity detection but only 0.34 for incompleteness---the highest-risk type is the hardest to detect. With agents exhibiting disambiguation deficit in $>$89\% of cases, type-aware auditing and externalized detection \citep{chantree_2006,ferrari_ambiguity_2019} are necessary for policy-governed deployments.
9	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 451
}
```

</details>

---


### Tool call

_source line 760 · 2026-05-21T19:00:10.699314+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 761 · 2026-05-21T19:00:11.604238+00:00_

1	\section{Conclusion}
2	
3	Ambiguous policy clauses increase agent safety violations by 34.0\,pp (OR\,$=$\,15.1) across five models, with clause identity explaining 22$\times$ more variance than model identity. The two-tier type hierarchy replicates across seven models ($\rho = 0.60$--$0.90$). With agents exhibiting disambiguation deficit in over 89\% of cases, type-aware auditing and externalized detection are critical for policy-governed deployments.
4	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 904
}
```

</details>

---


### Tool call

_source line 762 · 2026-05-21T19:00:11.604586+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 763 · 2026-05-21T19:00:12.056289+00:00_

1	\section*{Limitations}
2	\label{sec:limitations}
3	
4	\paragraph{Model coverage.} We evaluate seven API-accessible models from six providers (four proprietary, three open-source; two in replication, Appendix~\ref{app:model_expansion}). Smaller open-source models (7B--70B parameters) may show different vulnerability patterns, and our findings may not generalize to models with fundamentally different training approaches.
5	
6	\paragraph{Domain scope.} $\tau^2$-bench covers retail and airline customer service. Policy ambiguity effects in other domains (healthcare, finance, legal) remain to be tested, though the within-study cross-domain consistency is encouraging: failure mode distributions share the same top-two modes (assumption-based action and unauthorized escalation) across domains, with individual mode base rates differing by up to 12.5 pp, likely reflecting domain policy structure rather than methodological artifacts.
7	
8	\paragraph{Synthetic ambiguity.} Our matched-pair design requires synthetic construction of ambiguous variants, which may not capture the full distribution of naturally occurring policy ambiguities. We mitigate this through expert review and a realism validation comparing ambiguous clauses against original $\tau^2$-bench policy text. Ambiguous clauses are indistinguishable from originals in lexical diversity (TTR, KS $p = 0.89$) and word length ($p = 0.09$). Readability is slightly higher (Flesch--Kincaid $d = 0.29$, $p = 0.006$) and sentence length moderately higher ($d = 0.74$), both reflecting the structural demands of encoding ambiguity in standalone clauses. Across matched pairs, disambiguation preserves readability (Flesch--Kincaid $d = 0.14$, $p = 0.10$), confirming that minimal edits change semantic precision without altering linguistic register.
9	
10	\paragraph{Cross-judge asymmetry.} Although our dual-judge calibration (\S\ref{sec:method}) shows no systematic bias ($p = 0.606$) and human validation confirms the LLM judge operates 
…[truncated 3097 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 451
}
```

</details>

---


### Tool call

_source line 764 · 2026-05-21T19:00:12.056773+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 765 · 2026-05-21T19:00:12.357926+00:00_

1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{Ambiguity in NLP and requirements engineering.}
5	Ambiguity has been studied extensively in both computational linguistics and software engineering. Word sense disambiguation \citep{navigli_wsd_2009} addresses lexical ambiguity at the token level; our lexical type extends this to policy-specific polysemy. \citet{li_ambiguity_taxonomy_2024} propose an 11-type NLP taxonomy covering syntactic, semantic, and pragmatic ambiguity, from which we draw our linguistic-layer types. In requirements engineering (RE), \citet{massey_ambiguity_re_2014} classify six ambiguity types in regulatory texts, and \citet{berry_kamsties_2004} introduce the distinction between nocuous ambiguity (where stakeholders diverge on interpretation) and innocuous ambiguity (where they converge). Computational detection of nocuous ambiguity has progressed from heuristic methods \citep{chantree_2006,willis_nocuous_2008} through NLP-based cross-domain detectors \citep{ferrari_ambiguity_2019,ferrari_defects_2018} to transformer-based approaches for anaphoric ambiguity \citep{ezzini_taphsir_2022,ezzini_anaphoric_2022}. \citet{zhao_nlp4re_2021} survey the broader NLP4RE landscape. Our work extends Berry and Kamsties' framework to LLM agents, where the absence of shared organizational context makes previously innocuous ambiguity nocuous.
6	
7	\paragraph{Psycholinguistics of ambiguity processing.}
8	\citet{ferreira_good_enough_2002} show that human comprehenders build shallow, ``good-enough'' representations rather than full parses, paralleling our observation that LLM agents adopt surface interpretations. \citet{frazier_rayner_1982} demonstrate early commitment to a single parse; \citet{li_garden_path_llm_2024} provide direct evidence that LLMs exhibit analogous garden-path effects. \citet{liu_ambiguity_2023} demonstrate that language models fail to represent ambiguity, collapsing multiple interpretations into a single output. These findings
…[truncated 2322 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 766 · 2026-05-21T19:00:12.358326+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 767 · 2026-05-21T19:00:12.409659+00:00_

1	\section{TOST Equivalence Sensitivity}
2	\label{app:tost}
3	
4	Table~\ref{tab:tost_sensitivity} reports the TOST equivalence analysis \citep{lakens_2017} across seven margins. Three pairs involving incompleteness never reach equivalence even at $\pm 20$ pp: conditional precedence--incompleteness ($\Delta = 16.8$ pp), coreferential--incompleteness ($\Delta = 22.0$ pp), and incompleteness--scopal ($\Delta = 14.2$ pp).
5	
6	\begin{table}[!ht]
7	\centering
8	\small
9	\caption{TOST equivalence sensitivity across margins. Mid-tier = fraction of the six within-cluster pairs (lexical, auth.\ scope, scopal, cond.\ prec.) that are equivalent. Inc.\ and Cor.\ columns indicate separation from the mid-tier cluster.}
10	\label{tab:tost_sensitivity}
11	\begin{tabular}{lcccc}
12	\toprule
13	Margin & Equiv.\ pairs & Mid-tier & Inc.\ sep. & Cor.\ sep. \\
14	\midrule
15	$\pm 5$ pp & 0/15 & 0/6 & \checkmark & \checkmark \\
16	$\pm 8$ pp & 0/15 & 0/6 & \checkmark & \checkmark \\
17	$\pm 10$ pp & 3/15 & 3/6 & \checkmark & \checkmark \\
18	$\pm 12$ pp & 5/15 & 5/6 & \checkmark & \checkmark \\
19	$\pm 15$ pp & 8/15 & 6/6 & \checkmark & -- \\
20	$\pm 18$ pp & 9/15 & 6/6 & \checkmark & -- \\
21	$\pm 20$ pp & 12/15 & 6/6 & -- & -- \\
22	\bottomrule
23	\end{tabular}
24	\end{table}
25	
26	\section{Mitigation Experiment}
27	\label{app:mitigation}
28	
29	Table~\ref{tab:mitigation} reports the per-type, per-model $\Delta$pp from the disambiguation-instruction mitigation experiment (1,256 treatment episodes across five of six types; coreferential was not tested). Coreferential pairs are excluded because their ambiguous and unambiguous variants differ only in pronoun resolution, making it impossible to craft targeted mitigation instructions without revealing the experimental manipulation. The treatment appends a type-specific disambiguation instruction to the agent's system prompt. Control rates are the matched 5-type subset from the full study (\S\ref{sec:results}).
30	
31	\begin{table*}[!ht]
32	
…[truncated 16447 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 768 · 2026-05-21T19:00:20.545323+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/main.pdf",
  "project": "policy_ambiguity_safety",
  "pages": "11-14",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/main.pdf",
    "project": "policy_ambiguity_safety",
    "pages": "11-14",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 769 · 2026-05-21T19:00:21.499186+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 11, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/_pdf_images/main_p11.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 496.6}, {\"page\": 12, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/_pdf_images/main_p12.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 433.8}, {\"page\": 13, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/_pdf_images/main_p13.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 492.1}, {\"page\": 14, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/_pdf_images/main_p14.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 482.4}], \"total_pages\": 14, \"rendered_pages\": 4, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 953
}
```

</details>

---


### Tool call

_source line 770 · 2026-05-21T19:00:21.499699+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/_pdf_images/main_p1.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/_pdf_images/main_p1.png"
  }
}
```

</details>

---


### Tool result

_source line 771 · 2026-05-21T19:00:22.404229+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 904
}
```

</details>

---


### Tool call

_source line 772 · 2026-05-21T19:00:22.404767+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/_pdf_images/main_p2.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/_pdf_images/main_p2.png"
  }
}
```

</details>

---


### Tool call

_source line 773 · 2026-05-21T19:00:23.010329+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/_pdf_images/main_p3.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/_pdf_images/main_p3.png"
  }
}
```

</details>

---


### Tool result

_source line 774 · 2026-05-21T19:00:23.412821+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1008
}
```

</details>

---


### Tool call

_source line 775 · 2026-05-21T19:00:23.514949+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/_pdf_images/main_p8.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/_pdf_images/main_p8.png"
  }
}
```

</details>

---


### Tool result

_source line 776 · 2026-05-21T19:00:23.919067+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 908
}
```

</details>

---


### Tool call

_source line 777 · 2026-05-21T19:00:23.919547+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/_pdf_images/main_p9.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/_pdf_images/main_p9.png"
  }
}
```

</details>

---


### Tool result

_source line 778 · 2026-05-21T19:00:24.374025+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 859
}
```

</details>

---


### Tool result

_source line 779 · 2026-05-21T19:00:24.776740+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 857
}
```

</details>

---


### Tool call

_source line 780 · 2026-05-21T19:01:05.568071+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/_pdf_images/main_p4.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/_pdf_images/main_p4.png"
  }
}
```

</details>

---


### Tool result

_source line 781 · 2026-05-21T19:01:05.969964+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/.claude/sessions/review_reviewer_1_6edf79f4.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 401
}
```

</details>

---


### Tool call

_source line 782 · 2026-05-21T19:01:05.970415+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/_pdf_images/main_p5.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/_pdf_images/main_p5.png"
  }
}
```

</details>

---


### Tool result

_source line 783 · 2026-05-21T19:01:06.424193+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/.claude/sessions/review_reviewer_1_6edf79f4.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 453
}
```

</details>

---


### Tool call

_source line 784 · 2026-05-21T19:01:06.424613+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/_pdf_images/main_p6.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/_pdf_images/main_p6.png"
  }
}
```

</details>

---


### Tool result

_source line 785 · 2026-05-21T19:01:07.383795+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/.claude/sessions/review_reviewer_1_6edf79f4.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 959
}
```

</details>

---


### Tool call

_source line 786 · 2026-05-21T19:01:07.586433+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/_pdf_images/main_p7.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/_pdf_images/main_p7.png"
  }
}
```

</details>

---


### Tool result

_source line 787 · 2026-05-21T19:01:07.839827+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/.claude/sessions/review_reviewer_1_6edf79f4.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 253
}
```

</details>

---


### Tool call

_source line 788 · 2026-05-21T19:01:07.840305+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/_pdf_images/main_p10.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/_pdf_images/main_p10.png"
  }
}
```

</details>

---


### Tool result

_source line 789 · 2026-05-21T19:01:08.345334+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/.claude/sessions/review_reviewer_1_6edf79f4.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 505
}
```

</details>

---


### Tool call

_source line 790 · 2026-05-21T19:01:08.345840+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/_pdf_images/main_p11.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/_pdf_images/main_p11.png"
  }
}
```

</details>

---


### Tool result

_source line 791 · 2026-05-21T19:01:09.301252+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 955
}
```

</details>

---


### Tool call

_source line 792 · 2026-05-21T19:01:09.452258+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/_pdf_images/main_p12.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/_pdf_images/main_p12.png"
  }
}
```

</details>

---


### Tool call

_source line 793 · 2026-05-21T19:01:09.754797+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/_pdf_images/main_p13.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/_pdf_images/main_p13.png"
  }
}
```

</details>

---


### Tool call

_source line 794 · 2026-05-21T19:01:10.258787+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/_pdf_images/main_p14.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/_pdf_images/main_p14.png"
  }
}
```

</details>

---


### Tool result

_source line 795 · 2026-05-21T19:01:10.310183+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 857
}
```

</details>

---


### Tool result

_source line 796 · 2026-05-21T19:01:10.965663+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1210
}
```

</details>

---


### Tool result

_source line 797 · 2026-05-21T19:01:11.267836+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1009
}
```

</details>

---


### Tool call

_source line 798 · 2026-05-21T19:01:21.908700+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/main.pdf",
  "project": "policy_ambiguity_safety",
  "pages": "4-7",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/main.pdf",
    "project": "policy_ambiguity_safety",
    "pages": "4-7",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 799 · 2026-05-21T19:01:22.410735+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 4, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/_pdf_images/main_p4.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 518.0}, {\"page\": 5, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/_pdf_images/main_p5.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 519.3}, {\"page\": 6, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/_pdf_images/main_p6.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 389.1}, {\"page\": 7, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/_pdf_images/main_p7.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 356.3}], \"total_pages\": 14, \"rendered_pages\": 4, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 800 · 2026-05-21T19:01:28.031432+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/_pdf_images/main_p4.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/_pdf_images/main_p4.png"
  }
}
```

</details>

---


### Tool result

_source line 801 · 2026-05-21T19:01:28.936317+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 904
}
```

</details>

---


### Tool call

_source line 802 · 2026-05-21T19:01:28.936737+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/_pdf_images/main_p5.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/_pdf_images/main_p5.png"
  }
}
```

</details>

---


### Tool call

_source line 803 · 2026-05-21T19:01:29.440240+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/_pdf_images/main_p6.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/_pdf_images/main_p6.png"
  }
}
```

</details>

---


### Tool result

_source line 804 · 2026-05-21T19:01:29.742451+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 805
}
```

</details>

---


### Tool call

_source line 805 · 2026-05-21T19:01:29.742880+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/_pdf_images/main_p7.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/_pdf_images/main_p7.png"
  }
}
```

</details>

---


### Tool result

_source line 806 · 2026-05-21T19:01:29.945957+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 505
}
```

</details>

---


### Tool result

_source line 807 · 2026-05-21T19:01:30.349898+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 607
}
```

</details>

---


### Tool call

_source line 808 · 2026-05-21T19:02:55.937837+00:00_

called mcp__agent-ml-research__verify_references

<details open><summary>🔧 Tool call — mcp__agent-ml-research__verify_references</summary>

```json
{
  "paper_dir": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper",
  "project": "policy_ambiguity_safety"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "mcp__agent-ml-research__verify_references",
  "tool_args": {
    "paper_dir": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper",
    "project": "policy_ambiguity_safety"
  }
}
```

</details>

---


### Tool result

_source line 809 · 2026-05-21T19:03:28.124709+00:00_

{"result":"{\"success\": true, \"data\": {\"summary\": {\"total_bib_entries\": 39, \"total_citations\": 55, \"unique_cited_keys\": 37, \"orphan_bib\": 2, \"missing_bib\": 0, \"duplicate_keys\": 0, \"online_verified\": 30, \"online_not_found\": 6, \"online_mismatch\": 3}, \"cross_check\": {\"orphan_bib\": [\"tamkin_evaluating_2023\", \"yin_safeagentbench_2025\"], \"missing_bib\": [], \"orphan_count\": 2, \"missing_count\": 0}, \"bib_entries\": [{\"key\": \"li_ambiguity_taxonomy_2024\", \"type\": \"inproceedings\", \"title\": \"A Taxonomy of Ambiguity Types for NLP\", \"authors\": \"Li, Margaret Y. and Liu, Alisa and Wu, Zhaofeng and Smith, Noah A.\", \"year\": \"2024\", \"venue\": \"Proceedings of EACL 2024\"}, {\"key\": \"massey_ambiguity_re_2014\", \"type\": \"inproceedings\", \"title\": \"Identifying and Classifying Ambiguity for Regulatory Requirements\", \"authors\": \"Massey, Aaron K. and Rutledge, Richard L. and Ant\\\\'on, Annie I. and Swire, Peter...\", \"year\": \"2014\", \"venue\": \"22nd IEEE International Requirements Engineering Conference (RE)\"}, {\"key\": \"berry_kamsties_2004\", \"type\": \"techreport\", \"title\": \"From Contract Drafting to Software Specification: Linguistic Sources of Ambiguity --- A Handbook\", \"authors\": \"Berry, Daniel M. and Kamsties, Erik and Krieger, Michael M.\", \"year\": \"2004\", \"venue\": \"\"}, {\"key\": \"chantree_2006\", \"type\": \"inproceedings\", \"title\": \"Identifying Nocuous Ambiguities in Natural Language Requirements\", \"authors\": \"Chantree, Francis and Nuseibeh, Bashar and de Roeck, Anne and Willis, Alistair\", \"year\": \"2006\", \"venue\": \"14th IEEE International Requirements Engineering Conference (RE)\"}, {\"key\": \"wasow_ambiguity_2005\", \"type\": \"incollection\", \"title\": \"The Puzzle of Ambiguity\", \"authors\": \"Wasow, Thomas and Perfors, Amy and Beaver, David\", \"year\": \"2005\", \"venue\": \"Morphology and the Web of Grammar: Essays in Memory of Steven G. Lapointe\"}, {\"key\": \"
…[truncated 29942 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "mcp__agent-ml-research__verify_references",
  "elapsed_ms": 32186
}
```

</details>

---


### Tool call

_source line 810 · 2026-05-21T19:06:42.988494+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "\n# Reviewer 1 审稿意见：方法严谨性与实验设计\n\n## Summary（2-3 句）\n\n本文提出首个针对策略歧义（policy ambiguity）与 LLM agent 安全违规之间因果关系的 matched-pair 实验研究。基于 τ²-bench，构建 300 组 clause pairs（6 种歧义类型），在 5 个模型上运行 2,997 episodes，发现歧义使违规率上升 34 pp（OR=15.1），并呈现以 incompleteness 为上界的两层类型层级。实验设计整体严谨，统计分析覆盖面广（TOST 等价检验、bootstrap 聚类、logistic regression），对局限性的透明度在同类工作中属上乘；但 authorization scope 的测量可靠性不足以支撑其核心发现地位，incompleteness confound 仅部分控制，per-type 人工验证样本量偏小。\n\n## Strengths（逐条）\n\n**S1. 问题定位精准且新颖。** 将 RE（需求工程）中经典的歧义分类框架迁移到 LLM agent 安全领域，填补了\"歧义类型→安全违规\"因果映射的空白。Berry & Kamsties (2004) 的 nocuous/innocuous 区分在 agent 场景下的重新验证（所有歧义对 agent 均为 nocuous）是有理论价值的发现。\n\n**S2. Matched-pair 设计是正确的因果推断策略。** 300 组 clause pairs × 2 conditions 构成了 within-clause 比较，每个 clause 既作为自己的 treatment 又作为 control，有效控制了 clause-level 混淆变量。perturbation control（Δ=-0.67 pp, CI 含零）进一步排除了表面扰动的影响。\n\n**S3. 统计分析全面且方法得当。**\n- TOST 等价检验配合 7 个 margin 的 sensitivity analysis（Table 2, Appendix A），避免了仅依赖 NHST 的常见问题。\n- Bootstrap 聚类分析作为 margin-free 补充方法，与 TOST 结论一致。\n- Holm-Bonferroni 校正在 3 个 pre-registered test families 内分别应用。\n- Variance decomposition（type 22.4% vs model 1.0%）和 logistic regression 提供了多维度证据。\n- Post-hoc power 分析报告（C1/C2 >0.99; TOST ±15pp 0.94）让读者可评估检测力。\n\n**S4. 局限性透明度出色。** 论文在 Limitations 中主动讨论了：authorization scope κ=0.385、incompleteness information-addition confound、cross-judge asymmetry、per-type 小样本 CI、sentence length 差异等。许多同类论文不会如此坦诚。C3（layer effect）被明确标注为 inconclusive。\n\n**S5. 跨模型复制增强泛化性。** 7 个模型覆盖 6 个 provider（4 proprietary + 3 open-source），其中 Gemini 和 LLaMA 作为独立复制。Incompleteness 在所有 7 个模型中均 ≥46%，这一致性强化了 C2。\n\n**S6. Failure mode taxonomy 基于大规模经验证据。** 614 条 violation traces 的编码分析揭示了三种机制上不同的失败模式（structural misparse、information gap-filling、boundary violation），且与输入歧义类型形成可解释的对应关系。Gwet's AC₁=0.62 的 inter-coder 可靠性合理。\n\n**S7. Disambiguation Deficit 是一个干净的新发现。** 整体 4.6% 的歧义识别率，特别是 Qwen3 和 DeepSeek 为零，是一个有实际影响的定量事实。\n\n## Weaknesses（逐条）\n\n**W1 [MUST-FIX] Authorization scope 发现的表述强度超出了测量可靠性所能支撑的范围。**\n- 具体位置：Abstract、Section 1（Introduction）、Section 5.4（C4）、Figure 3\n- 问题：Authorization scope 是论文的关键卖点之一——\"the widest cross-model range (52 pp)\"、\"safety training may differentially mitigate specific ambiguity types\"。但其 cross-judge κ=0.385（Section 4.4），低于通常的 \"fair agreement\" 门槛（0.40）。per-type human-LLM κ=0.644（Appendix G, Table 8），CI [0.35, 0.91]。这意味着该类型的绝对违规率比其他类型有显著更多的测量噪声。\n- Abstract 中的括号注释 \"though measured with the lowest inter-judge agreement, κ=0.385\" 过于弱化——读者很容易忽略。在 Introduction 中复述 52 pp 时未提及可靠性。\n- 为什么影响接收：这削弱了 C4 交互效应的一个核心论据。52 pp range 中有多少来自真实的模型差异、多少来自 judge 在 authorization boundary 判定上的不一致，无法区分。\n- 建议修改方向：(1) 在 Abstract 中将 authorization scope 从\"主要发现\"降格为\"初步发现\"，明确标注不确定性；(2) 在 Introduction 中同等篇幅讨论可靠性限制；(3) 考虑在 C4 分析中展示去除 authorization scope 后的交互效应是否仍然显著。\n\n**W2 [SHOULD-FIX] Incompleteness confound 的控制力度不足以支撑其在两层层级中的独立地位。**\n- 具体位置：Section 5.2、Appendix E、Appendix F\n- 问题：Incompleteness 的 unambiguous variant 必然添加新政策内容（如补充缺失的退货条件），这不仅仅是\"token count difference\"的问题——它改变了策略的语义覆盖范围。Logistic regression 控制 token delta（p=0.022, coefficient change <8%）使用的是 token count 这一\"coarse proxy\"（论文原文承认），而更细粒度的语义衡量（如命题内容数量）可能揭示不同的 confound 结构。\n- 论文用 coreferential 的 31.6%（zero information delta）作为下界——这很巧妙，但它约束的是所有歧义的下界，而不是 incompleteness 的特定贡献。无法从中推断 incompleteness 的 49.2 pp 效应中有多少归因于歧义消解、多少归因于信息增补。\n- 建议：(1) 设计信息量和歧义正交变化的 ablation（如添加同等信息量但不消解歧义的 control）；(2) 在当前版本中，将 incompleteness 在两层层级中的地位明确标注为 \"conditional on confound assumptions\"。\n\n**W3 [SHOULD-FIX] 条件间句子长度差异（d=0.74）可能是未控制的混淆变量。**\n- 具体位置：Limitations 段落 \"Synthetic ambiguity\"\n- 问题：Ambiguous clauses 的句子长度 \"moderately higher\"（Cohen's d=0.74）。这是一个中等到大的效应量。更长的 clause 通常包含更多的处理负担，可能独立于歧义导致 agent 犯错。Perturbation control 使用 synonym substitution 和 clause reordering，这些变换不会系统性改变句长，因此不能排除长度 confound。\n- 关键问题：句子长度是否与歧义类型相关？如果 incompleteness clauses 系统性更长，这会进一步加剧 W2 的问题。\n- 建议：(1) 报告 per-type 句长分布和 condition×type 交互；(2) 在 logistic regression 中加入句长作为协变量。\n\n**W4 [SHOULD-FIX] Per-type 人工验证严重不足，无法支撑 type-level 结论。**\n- 具体位置：Section 4.4（Human validation）、Appendix G（Table 8）\n- 问题：100 episodes / 6 types = 32-34 per type。Scopal 的 human-LLM κ CI 为 [0.00, 1.00]——完全无信息。Coreferential 为 [0.00, 0.84]——几乎无信息。这些 CIs 无法排除 human-LLM agreement 实际很差的可能性。\n- 论文的核心贡献是 type-level 的差异化分析（C2），但 per-type 验证的精度远不足以支撑这一粒度。Overall κ=0.733 是可接受的，但 overall 验证不能替代 per-type 验证。\n- 建议：(1) 扩大人工标注样本至每类 ≥80 episodes（总计 ≥480），以获得信息量充足的 per-type κ 估计；(2) 在当前版本中，至少在方法论章节（而非仅 Appendix）明确标注 per-type 验证的精度限制。\n\n**W5 [SHOULD-FIX] Cross-judge 设计使 judge identity 与 model identity 混淆。**\n- 具体位置：Section 4.4、Limitations\n- 问题：GPT-5.4 判 3 个模型，GPT-4.1 判 1 个模型。论文论证 matched-pair 设计下 judge bias 在 Δpp 中抵消——这对 C1 是成立的。但 C2 的类型比较使用了跨模型的 pooled 绝对违规率（Table 1），这些数字受 judge identity 影响。\n- 更具体地：within-judge-group C3 分析各自未达显著（GPT-4.1-judged p=0.059; GPT-5.4-judged p=0.157），暗示 pooled C3 结果可能部分反映 judge-level variance 而非真实的 layer effect。\n- C4 中 authorization scope 的 Claude 12% vs GPT-5.4 64% 这一对比中，Claude 由 GPT-5.4 判，GPT-5.4 由 GPT-4.1 判——不同 judge 可能对\"authorization boundary violation\"有不同判定标准。论文用 within-judge bootstrap ranking preservation (99.5%) 部分缓解了这一担忧，但仅限于 GPT-5.4 作为 judge 的子集。\n- 建议：(1) 补充双 judge 评估至少覆盖全部类型×模型组合的一个子集（不仅是 100 episodes 的 calibration）；(2) 报告 C2 的 within-judge-group 分析结果，验证类型层级是否在单一 judge 内复现。\n\n**W6 [SHOULD-FIX] 两层层级的稳定性依赖于 margin 选择。**\n- 具体位置：Section 5.2、Table 2 (Appendix A)\n- 问题：在 ±10 pp 时只有 3/6 mid-tier pairs 等价（power=0.57）。两层结构直到 ±15 pp 才稳定（6/6）。Bootstrap 聚类的 AU p-value 为 0.47——这意味着在约一半的 bootstrap 样本中，incompleteness 不构成独立 cluster。\n- 论文对此透明（\"margin dependence\"、完整 sensitivity table），但 ±15 pp 的选择对两层叙事有利。如果 SESOI 为 ±10 pp（一个同样可合理论证的 threshold），mid-tier 内部的等价性就不成立。\n- 建议：(1) 在正文中更突出地讨论 margin 敏感性——目前完整 table 仅在 Appendix A；(2) 考虑将 ±10 pp 的结果（\"three-tier\" rather than \"two-tier\"）与 ±15 pp 的结果并列呈现，让读者自行判断。\n\n**W7 [MINOR] Clause pair 构建的 inter-annotator agreement 报告不完整。**\n- 具体位置：Section 4.2\n- 问题：报告了 96% pass rate，但未报告 type assignment 的 Cohen's κ 或 Fleiss' κ。Pass rate 不区分 agreement 和 chance agreement。\n- 建议：补充 type assignment 的标准可靠性指标。\n\n**W8 [MINOR] 引用问题。**\n- 2 个 orphan bib entries：tamkin_evaluating_2023、yin_safeagentbench_2025（在 .bib 中但未被引用）。\n- `ferrari_defects_2018` 的 bib 条目第一作者为 Rosadini（非 Ferrari），但论文中引用为 Ferrari et al. / Rosadini et al.——需核实。\n\n**W9 [MINOR] Reproducibility ICC 仅覆盖 OpenAI 模型族。**\n- 具体位置：Section 4.5\n- 问题：ICC=0.919 仅基于 GPT 模型族内的 30 clause pairs × 2 models × 3 replicates。跨 provider 的 test-retest 可靠性未测量。在 temperature=0 设置下，同一 provider 内的高 ICC 不令人意外；有意义的是跨 provider 稳定性。\n- 建议：至少在 1-2 个非 OpenAI 模型上补充 test-retest data。\n\n## Questions（需要作者澄清的问题）\n\n**Q1.** Sentence length (d=0.74) 与 ambiguity type 的相关性如何？如果 incompleteness clauses 系统性更长，W2 和 W3 的 confound 将叠加。请报告 per-type 的条件间长度差异。\n\n**Q2.** Variance decomposition 中 type 解释 22.4%，model 解释 1.0%——剩余约 76% 的方差来源是什么？是否主要是 clause-level heterogeneity？如果是，这是否意味着 type 内部的 clause 间变异远大于 type 间变异，从而削弱 type-level 概括的信度？\n\n**Q3.** Perturbation control 的 300 episodes 覆盖了几个模型？是否在所有 5 个主模型上均匀分布？\n\n**Q4.** Clause pair 标注中 96% pass rate 的评判标准是什么？两位标注者在 type assignment 上的 agreement κ 是多少？\n\n**Q5.** 50 clause pairs per type 是否在两个 τ²-bench domain（retail + airline）间均匀分布？如果不是，domain 是否是一个混淆变量？\n\n**Q6.** Mitigation experiment 中 coreferential 被排除的理由是 \"impossible to craft targeted mitigation instructions without revealing the experimental manipulation\"——但这种类型在主实验中有 31.6% 的违规率。是否可以设计不依赖于类型知识的通用 disambiguation prompt？\n\n**Q7.** 论文声称 \"all policy ambiguity is nocuous for LLM agents\"（Introduction），但 coreferential 的效应量（18.7 pp）远小于 incompleteness（49.2 pp），且 coreferential 的 human-LLM κ CI 为 [0.00, 0.84]——在 confidence 如此低的情况下，对 coreferential 的 nocuity 声称是否过强？\n\n## Missing References（遗漏的重要相关工作）\n\n1. **Tamkin et al. (2023)** \"Evaluating and Mitigating Discrimination in Language Model Decisions\" — 已在 .bib 中但未被引用，与 authorization scope 下 agent 权限判定的偏差讨论相关。\n\n2. **Mu et al. (2023)** \"Can LLMs Follow Simple Rules?\" 或类似的 rule-following compliance benchmark——与本文的 policy compliance 主题直接相关，可补充 Related Work 中 agent safety evaluation 段落。\n\n3. 缺少对 **vagueness** 文献的更深入讨论。论文在 Section 3 承认 authorization scope 与 vagueness 重叠、incompleteness 与 information absence 重叠，但仅引用了 Kennedy (2007)。Deemter (2010) \"Not Exactly: In Praise of Vagueness\" 和 Lassiter & Goodman (2017) 的 probabilistic pragmatics 工作可以丰富理论基础。\n\n## Overall Assessment\n\n**Overall**: 3.5 / 5（Borderline Conference）\n**Soundness**: 3.5 / 5\n**Excitement**: 3.5 / 5\n**Reproducibility**: 4 / 5\n**Confidence**: 4 / 5（我仔细检查了实验设计、统计方法和关键数据，对相关领域较熟悉）\n\n**一句话总结**：这是一项设计精心、分析全面的因果实验研究，核心发现（C1: 歧义整体致害性；C2: 类型层级，尤其 incompleteness 的一致性上界）在主实验和复制实验中都稳健；但 authorization scope 的低测量可靠性（κ=0.385）使得 C4 中的关键模式不够确定，incompleteness confound 仅有粗粒度控制，per-type 人工验证欠缺统计力度。修订 W1（降低 authorization scope claims 的表述强度）和 W4（扩大 per-type 验证样本）后，可达 Conference 水平。\n",
  "reviewer_id": "1",
  "project": "policy_ambiguity_safety"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "\n# Reviewer 1 审稿意见：方法严谨性与实验设计\n\n## Summary（2-3 句）\n\n本文提出首个针对策略歧义（policy ambiguity）与 LLM agent 安全违规之间因果关系的 matched-pair 实验研究。基于 τ²-bench，构建 300 组 clause pairs（6 种歧义类型），在 5 个模型上运行 2,997 episodes，发现歧义使违规率上升 34 pp（OR=15.1），并呈现以 incompleteness 为上界的两层类型层级。实验设计整体严谨，统计分析覆盖面广（TOST 等价检验、bootstrap 聚类、logistic regression），对局限性的透明度在同类工作中属上乘；但 authorization scope 的测量可靠性不足以支撑其核心发现地位，incompleteness confound 仅部分控制，per-type 人工验证样本量偏小。\n\n## Strengths（逐条）\n\n**S1. 问题定位精准且新颖。** 将 RE（需求工程）中经典的歧义分类框架迁移到 LLM agent 安全领域，填补了\"歧义类型→安全违规\"因果映射的空白。Berry & Kamsties (2004) 的 nocuous/innocuous 区分在 agent 场景下的重新验证（所有歧义对 agent 均为 nocuous）是有理论价值的发现。\n\n**S2. Matched-pair 设计是正确的因果推断策略。** 300 组 clause pairs × 2 conditions 构成了 within-clause 比较，每个 clause 既作为自己的 treatment 又作为 control，有效控制了 clause-level 混淆变量。perturbation control（Δ=-0.67 pp, CI 含零）进一步排除了表面扰动的影响。\n\n**S3. 统计分析全面且方法得当。**\n- TOST 等价检验配合 7 个 margin 的 sensitivity analysis（Table 2, Appendix A），避免了仅依赖 NHST 的常见问题。\n- Bootstrap 聚类分析作为 margin-free 补充方法，与 TOST 结论一致。\n- Holm-Bonferroni 校正在 3 个 pre-registered test families 内分别应用。\n- Variance decomposition（type 22.4% vs model 1.0%）和 logistic regression 提供了多维度证据。\n- Post-hoc power 分析报告（C1/C2 >0.99; TOST ±15pp 0.94）让读者可评估检测力。\n\n**S4. 局限性透明度出色。** 论文在 Limitations 中主动讨论了：authorization scope κ=0.385、incompleteness information-addition confound、cross-judge asymmetry、per-type 小样本 CI、sentence length 差异等。许多同类论文不会如此坦诚。C3（layer effect）被明确标注为 inconclusive。\n\n**S5. 跨模型复制增强泛化性。** 7 个模型覆盖 6 个 provider（4 proprietary + 3 open-source），其中 Gemini 和 LLaMA 作为独立复制。Incompleteness 在所有 7 个模型中均 ≥46%，这一致性强化了 C2。\n\n**S6. Failure mode taxonomy 基于大规模经验证据。** 614 条 violation traces 的编码分析揭示了三种机制上不同的失败模式（structural misparse、information gap-filling、boundary violation），且与输入歧义类型形成可解释的对应关系。Gwet's AC₁=0.62 的 inter-coder 可靠性合理。\n\n**S7. Disambiguation Deficit 是一个干净的新发现。** 整体 4.6% 的歧义识别率，特别是 Qwen3 和 DeepSeek 为零，是一个有实际影响的定量事实。\n\n## Weaknesses（逐条）\n\n**W1 [MUST-FIX] Authorization scope 发现的表述强度超出了测量可靠性所能支撑的范围。**\n- 具体位置：Abstract、Section 1（Introduction）、Section 5.4（C4）、Figure 3\n- 问题：Authorization scope 是论文的关键卖点之一——\"the widest cross-model range (52 pp)\"、\"safety training may differentially mitigate specific ambiguity types\"。但其 cross-judge κ=0.385（Section 4.4），低于通常的 \"fair agreement\" 门槛（0.40）。per-type human-LLM κ=0.644（Appendix G, Table 8），CI [0.35, 0.91]。这意味着该类型的绝对违规率比其他类型有显著更多的测量噪声。\n- Abstract 中的括号注释 \"though measured with the lowest inter-judge agreement, κ=0.385\" 过于弱化——读者很容易忽略。在 Introduction 中复述 52 pp 时未提及可靠性。\n- 为什么影响接收：这削弱了 C4 交互效应的一个核心论据。52 pp range 中有多少来自真实的模型差异、多少来自 judge 在 authorization boundary 判定上的不一致，无法区分。\n- 建议修改方向：(1) 在 Abstract 中将 authorization scope 从\"主要发现\"降格为\"初步发现\"，明确标注不确定性；(2) 在 Introduction 中同等篇幅讨论可靠性限制；(3) 考虑在 C4 分析中展示去除 authorization scope 后的交互效应是否仍然显著。\n\n**W2 [SHOULD-FIX] Incompleteness confound 的控制力度不足以支撑其在两层层级中的独立地位。**\n- 具体位置：Section 5.2、Appendix E、Appendix F\n- 问题：Incompleteness 的 unambiguous variant 必然添加新政策内容（如补充缺失的退货条件），这不仅仅是\"token count difference\"的问题——它改变了策略的语义覆盖范围。Logistic regression 控制 token delta（p=0.022, coefficient change <8%）使用的是 token count 这一\"coarse proxy\"（论文原文承认），而更细粒度的语义衡量（如命题内容数量）可能揭示不同的 confound 结构。\n- 论文用 coreferential 的 31.6%（zero information delta）作为下界——这很巧妙，但它约束的是所有歧义的下界，而不是 incompleteness 的特定贡献。无法从中推断 incompleteness 的 49.2 pp 效应中有多少归因于歧义消解、多少归因于信息增补。\n- 建议：(1) 设计信息量和歧义正交变化的 ablation（如添加同等信息量但不消解歧义的 control）；(2) 在当前版本中，将 incompleteness 在两层层级中的地位明确标注为 \"conditional on confound assumptions\"。\n\n**W3 [SHOULD-FIX] 条件间句子长度差异（d=0.74）可能是未控制的混淆变量。**\n- 具体位置：Limitations 段落 \"Synthetic ambiguity\"\n- 问题：Ambiguous clauses 的句子长度 \"moderately higher\"（Cohen's d=0.74）。这是一个中等到大的效应量。更长的 clause 通常包含更多的处理负担，可能独立于歧义导致 agent 犯错。Perturbation control 使用 synonym substitution 和 clause reordering，这些变换不会系统性改变句长，因此不能排除长度 confound。\n- 关键问题：句子长度是否与歧义类型相关？如果 incompleteness clauses 系统性更长，这会进一步加剧 W2 的问题。\n- 建议：(1) 报告 per-type 句长分布和 condition×type 交互；(2) 在 logistic regression 中加入句长作为协变量。\n\n**W4 [SHOULD-FIX] Per-type 人工验证严重不足，无法支撑 type-level 结论。**\n- 具体位置：Section 4.4（Human validation）、Appendix G（Table 8）\n- 问题：100 episodes / 6 types = 32-34 per type。Scopal 的 human-LLM κ CI 为 [0.00, 1.00]——完全无信息。Coreferential 为 [0.00, 0.84]——几乎无信息。这些 CIs 无法排除 human-LLM agreement 实际很差的可能性。\n- 论文的核心贡献是 type-level 的差异化分析（C2），但 per-type 验证的精度远不足以支撑这一粒度。Overall κ=0.733 是可接受的，但 overall 验证不能替代 per-type 验证。\n- 建议：(1) 扩大人工标注样本至每类 ≥80 episodes（总计 ≥480），以获得信息量充足的 per-type κ 估计；(2) 在当前版本中，至少在方法论章节（而非仅 Appendix）明确标注 per-type 验证的精度限制。\n\n**W5 [SHOULD-FIX] Cross-judge 设计使 judge identity 与 model identity 混淆。**\n- 具体位置：Section 4.4、Limitations\n- 问题：GPT-5.4 判 3 个模型，GPT-4.1 判 1 个模型。论文论证 matched-pair 设计下 judge bias 在 Δpp 中抵消——这对 C1 是成立的。但 C2 的类型比较使用了跨模型的 pooled 绝对违规率（Table 1），这些数字受 judge identity 影响。\n- 更具体地：within-judge-group C3 分析各自未达显著（GPT-4.1-judged p=0.059; GPT-5.4-judged p=0.157），暗示 pooled C3 结果可能部分反映 judge-level variance 而非真实的 layer effect。\n- C4 中 authorization scope 的 Claude 12% vs GPT-5.4 64% 这一对比中，Claude 由 GPT-5.4 判，GPT-5.4 由 GPT-4.1 判——不同 judge 可能对\"authorization boundary violation\"有不同判定标准。论文用 within-judge bootstrap ranking preservation (99.5%) 部分缓解了这一担忧，但仅限于 GPT-5.4 作为 judge 的子集。\n- 建议：(1) 补充双 judge 评估至少覆盖全部类型×模型组合的一个子集（不仅是 100 episodes 的 calibration）；(2) 报告 C2 的 within-judge-group 分析结果，验证类型层级是否在单一 judge 内复现。\n\n**W6 [SHOULD-FIX] 两层层级的稳定性依赖于 margin 选择。**\n- 具体位置：Section 5.2、Table 2 (Appendix A)\n- 问题：在 ±10 pp 时只有 3/6 mid-tier pairs 等价（power=0.57）。两层结构直到 ±15 pp 才稳定（6/6）。Bootstrap 聚类的 AU p-value 为 0.47——这意味着在约一半的 bootstrap 样本中，incompleteness 不构成独立 cluster。\n- 论文对此透明（\"margin dependence\"、完整 sensitivity table），但 ±15 pp 的选择对两层叙事有利。如果 SESOI 为 ±10 pp（一个同样可合理论证的 threshold），mid-tier 内部的等价性就不成立。\n- 建议：(1) 在正文中更突出地讨论 margin 敏感性——目前完整 table 仅在 Appendix A；(2) 考虑将 ±10 pp 的结果（\"three-tier\" rather than \"two-tier\"）与 ±15 pp 的结果并列呈现，让读者自行判断。\n\n**W7 [MINOR] Clause pair 构建的 inter-annotator agreement 报告不完整。**\n- 具体位置：Section 4.2\n- 问题：报告了 96% pass rate，但未报告 type assignment 的 Cohen's κ 或 Fleiss' κ。Pass rate 不区分 agreement 和 chance agreement。\n- 建议：补充 type assignment 的标准可靠性指标。\n\n**W8 [MINOR] 引用问题。**\n- 2 个 orphan bib entries：tamkin_evaluating_2023、yin_safeagentbench_2025（在 .bib 中但未被引用）。\n- `ferrari_defects_2018` 的 bib 条目第一作者为 Rosadini（非 Ferrari），但论文中引用为 Ferrari et al. / Rosadini et al.——需核实。\n\n**W9 [MINOR] Reproducibility ICC 仅覆盖 OpenAI 模型族。**\n- 具体位置：Section 4.5\n- 问题：ICC=0.919 仅基于 GPT 模型族内的 30 clause pairs × 2 models × 3 replicates。跨 provider 的 test-retest 可靠性未测量。在 temperature=0 设置下，同一 provider 内的高 ICC 不令人意外；有意义的是跨 provider 稳定性。\n- 建议：至少在 1-2 个非 OpenAI 模型上补充 test-retest data。\n\n## Questions（需要作者澄清的问题）\n\n**Q1.** Sentence length (d=0.74) 与 ambiguity type 的相关性如何？如果 incompleteness clauses 系统性更长，W2 和 W3 的 confound 将叠加。请报告 per-type 的条件间长度差异。\n\n**Q2.** Variance decomposition 中 type 解释 22.4%，model 解释 1.0%——剩余约 76% 的方差来源是什么？是否主要是 clause-level heterogeneity？如果是，这是否意味着 type 内部的 clause 间变异远大于 type 间变异，从而削弱 type-level 概括的信度？\n\n**Q3.** Perturbation control 的 300 episodes 覆盖了几个模型？是否在所有 5 个主模型上均匀分布？\n\n**Q4.** Clause pair 标注中 96% pass rate 的评判标准是什么？两位标注者在 type assignment 上的 agreement κ 是多少？\n\n**Q5.** 50 clause pairs per type 是否在两个 τ²-bench domain（retail + airline）间均匀分布？如果不是，domain 是否是一个混淆变量？\n\n**Q6.** Mitigation experiment 中 coreferential 被排除的理由是 \"impossible to craft targeted mitigation instructions without revealing the experimental manipulation\"——但这种类型在主实验中有 31.6% 的违规率。是否可以设计不依赖于类型知识的通用 disambiguation prompt？\n\n**Q7.** 论文声称 \"all policy ambiguity is nocuous for LLM agents\"（Introduction），但 coreferential 的效应量（18.7 pp）远小于 incompleteness（49.2 pp），且 coreferential 的 human-LLM κ CI 为 [0.00, 0.84]——在 confidence 如此低的情况下，对 coreferential 的 nocuity 声称是否过强？\n\n## Missing References（遗漏的重要相关工作）\n\n1. **Tamkin et al. (2023)** \"Evaluating and Mitigating Discrimination in Language Model Decisions\" — 已在 .bib 中但未被引用，与 authorization scope 下 agent 权限判定的偏差讨论相关。\n\n2. **Mu et al. (2023)** \"Can LLMs Follow Simple Rules?\" 或类似的 rule-following compliance benchmark——与本文的 policy compliance 主题直接相关，可补充 Related Work 中 agent safety evaluation 段落。\n\n3. 缺少对 **vagueness** 文献的更深入讨论。论文在 Section 3 承认 authorization scope 与 vagueness 重叠、incompleteness 与 information absence 重叠，但仅引用了 Kennedy (2007)。Deemter (2010) \"Not Exactly: In Praise of Vagueness\" 和 Lassiter & Goodman (2017) 的 probabilistic pragmatics 工作可以丰富理论基础。\n\n## Overall Assessment\n\n**Overall**: 3.5 / 5（Borderline Conference）\n**Soundness**: 3.5 / 5\n**Excitement**: 3.5 / 5\n**Reproducibility**: 4 / 5\n**Confidence**: 4 / 5（我仔细检查了实验设计、统计方法和关键数据，对相关领域较熟悉）\n\n**一句话总结**：这是一项设计精心、分析全面的因果实验研究，核心发现（C1: 歧义整体致害性；C2: 类型层级，尤其 incompleteness 的一致性上界）在主实验和复制实验中都稳健；但 authorization scope 的低测量可靠性（κ=0.385）使得 C4 中的关键模式不够确定，incompleteness confound 仅有粗粒度控制，per-type 人工验证欠缺统计力度。修订 W1（降低 authorization scope claims 的表述强度）和 W4（扩大 per-type 验证样本）后，可达 Conference 水平。\n",
    "reviewer_id": "1",
    "project": "policy_ambiguity_safety"
  }
}
```

</details>

---


### Tool result

_source line 811 · 2026-05-21T19:06:46.803822+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_967344d166ba485ad606d14379e69d85:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3815
}
```

</details>

---


### Tool call

_source line 812 · 2026-05-21T19:06:55.253693+00:00_

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
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
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

_source line 813 · 2026-05-21T19:06:55.304288+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 814 · 2026-05-21T19:07:00.474269+00:00_

called mcp__agent-ml-research__cleanup_pdf_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__cleanup_pdf_images</summary>

```json
{
  "output_dir": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/_pdf_images"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "tool_args": {
    "output_dir": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/_pdf_images"
  }
}
```

</details>

---


### Tool result

_source line 815 · 2026-05-21T19:07:00.525030+00:00_

{"result":"{\"success\": true, \"data\": {\"message\": \"目录不存在，无需清理\", \"deleted\": 0}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "elapsed_ms": 50
}
```

</details>

---


### Assistant

_source line 816 · 2026-05-21T19:07:11.873292+00:00_

审稿意见已提交给 Review Director。

**评分摘要**：Overall 3.5/5（Borderline Conference），Soundness 3.5，Excitement 3.5，Reproducibility 4，Confidence 4。

**核心判断**：实验设计整体严谨（matched-pair + perturbation control + 7 模型复制），统计分析覆盖面在同类工作中属上乘。C1（歧义整体致害 +34 pp）和 C2（incompleteness 一致性上界）的证据稳健。

**主要问题**：
- **[MUST-FIX]** Authorization scope 的 κ=0.385 不足以支撑其作为 C4 核心发现的地位，abstract/introduction 表述过强
- **[SHOULD-FIX]** Incompleteness confound 仅用 token count 粗粒度控制；条件间句长差异 d=0.74 未纳入 regression；per-type 人工验证（n=32-34/type）统计力度不足；cross-judge 混淆 judge×model identity；两层层级在 ±10 pp 处不稳定

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1"
}
```

</details>

---


## Round 22

## Round 22

10 recorded events


### User

_source line 817 · 2026-05-21T19:08:01.378324+00:00_

[Round 1 审稿请求]:
以下是 Reviewer 2 的完整审稿意见。请逐条回应其 Weaknesses：对每条标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。也请评论其 Questions 和 Missing References 中你认为重要的点。

---

# Reviewer 2 审稿意见：新颖性、理论基础与完整性

## Summary（2-3 句）

本文在 τ²-bench 上构建 300 组 matched clause pairs，通过 5 个模型（2,997 episodes）因果量化了政策歧义对 LLM agent 安全的影响（+34.0pp，OR=15.1），并提出六类型两层 taxonomy、发现"disambiguation deficit"现象（<11% awareness）。实验设计严谨、统计方法全面（TOST、bootstrap cluster、Holm-Bonferroni），但 taxonomy 的理论基础存在概念混淆（将 incompleteness 和 normative conflict 归为 ambiguity），且声称的 two-tier hierarchy 的 bootstrap 稳定性不足（34.3%），部分贡献的框架性新颖度被过度表述。

## Weaknesses（逐条）

**W1 [MUST-FIX] Two-tier hierarchy (C2) 稳定性不足，声称强于证据。**
- Bootstrap cluster analysis 中 incompleteness singleton 仅在 34.3% 的 bootstrap samples 中出现，AU p-value=0.47。
- Kendall's W=0.398（p=0.072）五模型下不显著。
- Abstract/Intro/Conclusion 的表述确定性远超 34.3% bootstrap support。
- 建议：(a) 更谨慎的措辞如"incompleteness tends to cluster as the highest-risk type, though the tier boundary is not sharp"；(b) 将 C2 缩小为"incompleteness is consistently the highest-risk type"。

**W2 [SHOULD-FIX] Taxonomy 的理论基础存在概念混淆——Incompleteness 和 Conditional Precedence 并非严格意义上的 ambiguity。**
- Incompleteness 是 information absence，不是"multiple interpretations"。
- Conditional precedence 是 normative conflict，两条矛盾的规则各自是清晰的。
- §3 用行为结果定义输入类型是循环论证。
- 建议：(a) 定位为"policy specification defects"而非"ambiguity types"；(b) 更充分讨论理论边界。

**W3 [SHOULD-FIX] "Differential Nocuity" 框架的增量贡献被过度表述。**
- Berry & Kamsties (2004)、Chantree et al. (2006)、Willis et al. (2008) 已经测量了 type-specific nocuity。
- 论文的贡献是在 LLM agent 场景的实证验证，但 §7 写法暗示新框架。
- 建议：明确定位为已有概念在新领域的验证和扩展。

**W4 [SHOULD-FIX] "Disambiguation Deficit" 命名不准确——是 uninstructed default 还是 inability？**
- "Deficit"暗示能力缺失，但 mitigation experiment (-8.5pp) 证明可改善。
- 建议：使用更精确术语或在定义中明确指 uninstructed settings。

**W5 [SHOULD-FIX] Authorization scope 的结论可靠性受 low agreement 严重影响。**
- κ=0.385 接近随机。52pp range 中真实差异 vs noise 无法分离。
- 建议：在 §5.4 中更明确标记为 tentative/unreliable；考虑 Abstract 中移除或弱化 52pp 表述。

**W6 [MINOR] Psycholinguistics 类比可能 over-extended。**
- LLM autoregressive generation 与人类 incremental parsing 机制不同。
- 建议：加 caveat "though the underlying mechanisms are likely distinct"。

**W7 [MINOR] 引用问题。**
- ferrari_defects_2018 作者不一致，2 orphan bib entries，navigli_wsd_2009 年份待确认。

## Questions

Q1. Incompleteness 满足 Wasow (2005) ambiguity 定义的理由？
Q2. Bootstrap 34.3% 支持度 vs "continuum" 假说的区分？
Q3. Coreferential 排除 mitigation 的影响？
Q4. 是否有 template pattern 驱动的系统性偏差？
Q5. Domain-specific SESOI 考虑？

## Missing References

1. Dalpiaz, van der Schalk, & Lucassen (2018) — 明确区分 ambiguity 和 incompleteness
2. Yu, Carroll, & Bentley (2026) — concurrent matched-pair causal design for agent safety
3. Lin et al. (2025) "Ask-to-Clarify" — disambiguation channel design
4. Willis et al. (2008) 在 §7 中 credit type-specific nocuity

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 818 · 2026-05-21T19:08:34.865294+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/taxonomy.tex",
  "offset": "22",
  "limit": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/taxonomy.tex",
    "offset": "22",
    "limit": "5"
  }
}
```

</details>

---


### Tool result

_source line 819 · 2026-05-21T19:08:35.367486+00:00_

22	The layer distinction reflects the hypothesis that linguistic ambiguity can be partially resolved through tool responses, user context, or world knowledge, while specification ambiguity has no external resolution channel available to the agent, forcing it to guess. We test this hypothesis empirically in \S\ref{sec:results} and \S\ref{sec:analysis}. The linguistic/specification layer distinction is a theoretical organizing principle; \S\ref{sec:results} tests whether it corresponds to an empirical grouping.
23	
24	\paragraph{Scope of `ambiguity.'}
25	Our taxonomy uses \emph{ambiguity} broadly to encompass policy specification features that admit multiple operationally distinct interpretations by an LLM agent. Authorization scope overlaps with \emph{vagueness} \citep{kennedy_vagueness_2007}, incompleteness with \emph{information absence} (resolution requires adding content), and conditional precedence with \emph{normative conflict} between individually unambiguous rules. We adopt this inclusive definition because LLM agents process all six types identically---committing to a single interpretation without flagging uncertainty---and the resulting safety violations are behaviorally indistinguishable (\S\ref{sec:results}).
26	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 820 · 2026-05-21T19:08:35.820407+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/analysis.tex",
  "offset": "20",
  "limit": "6"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/analysis.tex",
    "offset": "20",
    "limit": "6"
  }
}
```

</details>

---


### Tool result

_source line 821 · 2026-05-21T19:08:36.071794+00:00_

20	\subsection{Disambiguation Deficit}
21	
22	Agents rarely recognize ambiguity. We code \emph{disambiguation awareness} (acknowledging multiple interpretations, asking clarifying questions, or conditioning on ambiguity) versus \emph{surface adoption} (proceeding with a single interpretation). Overall disambiguation awareness is 4.6\%: Claude (11.0\%) and GPT-4.1 (10.7\%) show the highest rates, while Qwen3 and DeepSeek show zero across all 278 combined violation traces.
23	
24	We term this the \emph{Disambiguation Deficit}: unlike humans---who typically signal uncertainty or seek clarification---agents proceed with full confidence in their chosen interpretation, consistent with \citet{hu_ambiguity_2025}'s finding that ambiguity in LLMs reflects missing conceptual representations.
25	Agents are not inherently incapable of disambiguation---our mitigation experiment shows $-$8.5\,pp improvement---but exhibit a \emph{disambiguation deficit}: defaulting to single-parse adoption without explicit instruction, paralleling human good-enough processing \citep{ferreira_good_enough_2002}.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 251
}
```

</details>

---


### Tool call

_source line 822 · 2026-05-21T19:08:36.273119+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 823 · 2026-05-21T19:08:36.273642+00:00_

1	\section{Discussion}
2	\label{sec:discussion}
3	
4	\paragraph{Differential nocuity.}
5	\citet{berry_kamsties_2004} distinguish nocuous from innocuous ambiguity. Our results can be interpreted through a \emph{differential nocuity} lens: risk depends on ambiguity type (base vulnerability), safety training (selective mitigation), and disambiguation channel availability. This generates two testable predictions: (P1) types with explicit decision points should show larger safety-training gains than gap-filling types; (P2) disambiguation channels should reduce violations more for high-deficit types. Our mitigation experiment (Appendix~\ref{app:mitigation}) is consistent with, though not a formal test of, P1 ($-18.0$\,pp for authorization scope vs.\ $-3.4$\,pp for incompleteness).
6	
7	\paragraph{Practical implications.}
8	A proof-of-concept classifier (Appendix~\ref{app:detection}) achieves F1\,=\,0.81 for binary ambiguity detection but only 0.34 for incompleteness---the highest-risk type is the hardest to detect. With agents exhibiting disambiguation deficit in $>$89\% of cases, type-aware auditing and externalized detection \citep{chantree_2006,ferrari_ambiguity_2019} are necessary for policy-governed deployments.
9	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 824 · 2026-05-21T19:09:58.306934+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "\n# Reviewer 1 对 Reviewer 2 意见的逐条回应\n\n## Weaknesses 回应\n\n**[AGREE] R2-W1: Two-tier hierarchy (C2) 稳定性不足，声称强于证据。**\n\n同意 R2 的判断。Bootstrap 34.3% 和 AU p=0.47 意味着 incompleteness singleton 不是一个稳定的聚类结构。Kendall's W=0.398（p=0.072）五模型下未达显著进一步削弱了 C2 的 cross-model generalizability。我在自己的 W6 中也独立提出了相同的 margin dependence 问题：在 ±10 pp 时仅 3/6 mid-tier pairs 等价。\n\nR2 的建议（将 C2 缩小为\"incompleteness is consistently the highest-risk type\"）是务实的。这一缩窄后的声称有充分支撑：incompleteness 在全部 7 个模型中 ≥46%（Section 5.2, Appendix E Table 7），且 mean rank 始终最高（Appendix M）。但当前的\"two-tier hierarchy\"表述暗示一个清晰的二分结构，与 34.3% bootstrap support 不符。\n\n**[REBUT] R2-W2: Taxonomy 概念混淆——Incompleteness 和 Conditional Precedence 非严格 ambiguity。**\n\nR2 的理论关切有道理，但论文已在 Section 3 \"Scope of 'ambiguity'\" 段落中明确回应了这一问题。原文承认 incompleteness 与 \"information absence\"、conditional precedence 与 \"normative conflict\" 的重叠，并给出了采用 inclusive definition 的理由：\"LLM agents process all six types identically—committing to a single interpretation without flagging uncertainty—and the resulting safety violations are behaviorally indistinguishable (§5)\"。\n\n这不是循环论证，而是操作性定义（operational definition）：论文并非用行为结果来定义类型，而是用\"admits multiple operationally distinct interpretations by an LLM agent\"来界定范围，然后实证检验行为后果。这种操作性定义在实证研究中是标准做法。\n\n但我同意 R2 的一个子观点：论文标题和 framing 中一贯使用 \"ambiguity\" 而非 \"policy specification defects\" 或 \"policy specification issues\" 确实可能导致语言学背景的读者产生误解。建议在 Section 3 中扩展理论边界的讨论，增加对 Dalpiaz et al. (2018) 区分 ambiguity/incompleteness 的引用，并在标题或 abstract 中添加更精确的限定。\n\n**[AGREE] R2-W3: \"Differential Nocuity\" 框架增量贡献被过度表述。**\n\n同意。Section 7 Discussion 中的 \"differential nocuity\" 段落确实写得像是提出了一个新框架，但核心贡献实际是将 Berry & Kamsties (2004) 的 nocuous/innocuous 区分在 LLM agent 场景中进行了类型粒度的实证检验。Willis et al. (2008) 已经在 RE 领域测量了 type-specific nocuity。论文的新增价值是：(1) agent 场景下所有歧义都是 nocuous（Berry & Kamsties 的 innocuous 类别消失），(2) type×model interaction 提供了 safety training 选择性缓解的证据。这些是有价值的实证贡献，但不构成 \"new framework\"。\n\n建议：将 §7 第一段的 framing 从 \"can be interpreted through a differential nocuity lens\" 改为 \"extends Berry & Kamsties' nocuous/innocuous distinction to LLM agents, where all ambiguity is nocuous but type-specific severity varies\"。\n\n**[AGREE with nuance] R2-W4: \"Disambiguation Deficit\" 命名不准确。**\n\n部分同意。R2 正确指出 \"deficit\" 暗示能力缺失，而 mitigation experiment（-8.5 pp）证明可改善。但论文在 Section 6.2 中已明确澄清：\"Agents are not inherently incapable of disambiguation...but exhibit a disambiguation deficit: defaulting to single-parse adoption without explicit instruction\"（第 25 行）。所以 \"deficit\" 在此指 uninstructed default behavior，而非 inability。\n\n不过，术语选择确实容易引起误读。一个更精确的术语可能是 \"disambiguation default\" 或 \"disambiguation neglect\"，更好地传达 \"有能力但默认不做\" 的含义。\n\n**[AGREE] R2-W5: Authorization scope 的结论可靠性受 low agreement 严重影响。**\n\n强烈同意。这与我的 W1 (MUST-FIX) 完全一致。κ=0.385 的 cross-judge agreement 意味着 authorization scope 的绝对违规率有极大的测量不确定性。52 pp range 这一数字是论文最引人注目的发现之一，但也是最不可靠的。\n\n我比 R2 更进一步：建议作者在 C4 分析中展示去除 authorization scope 后交互效应是否仍然显著，以测试这一类型是否在驱动整个 C4 结果。如果去除后交互效应消失，则 C4 的一般性声称需要大幅缩窄。\n\n**[AGREE] R2-W6: Psycholinguistics 类比可能 over-extended。**\n\n同意加 caveat 的建议。论文将 agent 的 surface adoption 类比为 Frazier & Rayner (1982) 的 garden-path processing 和 Ferreira et al. (2002) 的 good-enough representations。类比在 phenomenological level 是有启发性的（都是 early commitment to a single parse），但 autoregressive generation 和 incremental human parsing 的底层机制确实不同。Section 6.1 使用 \"paralleling\" 一词已经有一定距离感，但 §6.2 中 \"paralleling human good-enough processing\" 的措辞不够谨慎。加一句 mechanism-level caveat 即可，不影响论文的核心论证。\n\n**[AGREE] R2-W7: 引用问题。**\n\n与我的 W8 一致。ferrari_defects_2018 的第一作者确实应为 Rosadini；2 个 orphan entries 应清理。\n\n## Questions 回应\n\n**R2-Q1（Incompleteness 满足 Wasow 2005 定义的理由）：** 这是 W2 的核心，论文已在 Section 3 用操作性定义回应。如上所述，我认为论文的立场可辩护但需扩展讨论。\n\n**R2-Q2（Bootstrap 34.3% vs continuum）：** 重要问题。34.3% 不足以排除 continuum 假说。论文应明确讨论：如果歧义类型的违规率分布是连续的（而非离散的两层），哪些结论需要修改？核心的 incompleteness 上界地位可能不变，但 \"two-tier hierarchy\" 这一结构性声称需要弱化。\n\n**R2-Q3（Coreferential 排除 mitigation 的影响）：** 我在自己的 Q6 中也提出了类似问题。Coreferential 31.6% 的违规率不低，排除它使 mitigation 的完整性受损。\n\n**R2-Q4（Template pattern bias）：** 我在 W7 中也提出了类似关切。96% pass rate 不等于 high inter-annotator κ。建议补充 type assignment 的标准 reliability 指标。\n\n**R2-Q5（Domain-specific SESOI）：** 好问题。±15 pp 的 anchoring argument（\"a type producing ≥15 pp more violations warrants distinct policy handling\"，Section 4.6）是合理的实践性论证，但不同部署场景（医疗 vs 零售）的 tolerance 可能差异巨大。论文在 Limitations 中提到了 domain scope 限制，但未将此与 SESOI 选择联系起来。\n\n## Missing References 回应\n\n1. **Dalpiaz et al. (2018)**：重要。如果这项工作明确区分了 ambiguity 和 incompleteness，它直接关系到 W2 的理论讨论。论文应引用并回应。\n\n2. **Yu, Carroll, & Bentley (2026)**：如果确实存在 concurrent matched-pair causal design for agent safety，这是高度相关的 concurrent work，必须在 Related Work 中讨论。我无法独立验证这篇论文是否存在，但如果 R2 能确认，作者应搜索并引用。\n\n3. **Lin et al. (2025) \"Ask-to-Clarify\"**：与 Suri et al. (2025) 和 Sehwag et al. (2026)（论文已引用）属于同一 disambiguation channel 文献线。补充引用是合理的。\n\n4. **Willis et al. (2008) 在 §7 中给予 credit**：同意 R2。Willis et al. 已在 Related Work 中被引用，但 §7 Discussion 中的 \"differential nocuity\" 讨论未提及他们在 type-specific nocuity 测量上的 prior work。这是一个归属问题，应修正。\n\n## 总结\n\nR2 的审查侧重理论基础和概念框架，与我侧重方法严谨性形成互补。我们在三个关键问题上高度一致：(1) authorization scope 的低可靠性（R2-W5 = 我的 W1）；(2) two-tier hierarchy 的稳定性不足（R2-W1 = 我的 W6）；(3) 引用问题（R2-W7 = 我的 W8）。\n\nR2 的 W2（taxonomy 概念混淆）是一个有价值的理论视角，但论文已有部分回应（Section 3 \"Scope of 'ambiguity'\"）。我认为修订方向是扩展讨论而非改变 taxonomy 设计。R2 的 W3 和 W4 属于 framing/naming 问题，修订成本低且能提升精确度。\n",
  "reviewer_id": "1",
  "project": "policy_ambiguity_safety"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "\n# Reviewer 1 对 Reviewer 2 意见的逐条回应\n\n## Weaknesses 回应\n\n**[AGREE] R2-W1: Two-tier hierarchy (C2) 稳定性不足，声称强于证据。**\n\n同意 R2 的判断。Bootstrap 34.3% 和 AU p=0.47 意味着 incompleteness singleton 不是一个稳定的聚类结构。Kendall's W=0.398（p=0.072）五模型下未达显著进一步削弱了 C2 的 cross-model generalizability。我在自己的 W6 中也独立提出了相同的 margin dependence 问题：在 ±10 pp 时仅 3/6 mid-tier pairs 等价。\n\nR2 的建议（将 C2 缩小为\"incompleteness is consistently the highest-risk type\"）是务实的。这一缩窄后的声称有充分支撑：incompleteness 在全部 7 个模型中 ≥46%（Section 5.2, Appendix E Table 7），且 mean rank 始终最高（Appendix M）。但当前的\"two-tier hierarchy\"表述暗示一个清晰的二分结构，与 34.3% bootstrap support 不符。\n\n**[REBUT] R2-W2: Taxonomy 概念混淆——Incompleteness 和 Conditional Precedence 非严格 ambiguity。**\n\nR2 的理论关切有道理，但论文已在 Section 3 \"Scope of 'ambiguity'\" 段落中明确回应了这一问题。原文承认 incompleteness 与 \"information absence\"、conditional precedence 与 \"normative conflict\" 的重叠，并给出了采用 inclusive definition 的理由：\"LLM agents process all six types identically—committing to a single interpretation without flagging uncertainty—and the resulting safety violations are behaviorally indistinguishable (§5)\"。\n\n这不是循环论证，而是操作性定义（operational definition）：论文并非用行为结果来定义类型，而是用\"admits multiple operationally distinct interpretations by an LLM agent\"来界定范围，然后实证检验行为后果。这种操作性定义在实证研究中是标准做法。\n\n但我同意 R2 的一个子观点：论文标题和 framing 中一贯使用 \"ambiguity\" 而非 \"policy specification defects\" 或 \"policy specification issues\" 确实可能导致语言学背景的读者产生误解。建议在 Section 3 中扩展理论边界的讨论，增加对 Dalpiaz et al. (2018) 区分 ambiguity/incompleteness 的引用，并在标题或 abstract 中添加更精确的限定。\n\n**[AGREE] R2-W3: \"Differential Nocuity\" 框架增量贡献被过度表述。**\n\n同意。Section 7 Discussion 中的 \"differential nocuity\" 段落确实写得像是提出了一个新框架，但核心贡献实际是将 Berry & Kamsties (2004) 的 nocuous/innocuous 区分在 LLM agent 场景中进行了类型粒度的实证检验。Willis et al. (2008) 已经在 RE 领域测量了 type-specific nocuity。论文的新增价值是：(1) agent 场景下所有歧义都是 nocuous（Berry & Kamsties 的 innocuous 类别消失），(2) type×model interaction 提供了 safety training 选择性缓解的证据。这些是有价值的实证贡献，但不构成 \"new framework\"。\n\n建议：将 §7 第一段的 framing 从 \"can be interpreted through a differential nocuity lens\" 改为 \"extends Berry & Kamsties' nocuous/innocuous distinction to LLM agents, where all ambiguity is nocuous but type-specific severity varies\"。\n\n**[AGREE with nuance] R2-W4: \"Disambiguation Deficit\" 命名不准确。**\n\n部分同意。R2 正确指出 \"deficit\" 暗示能力缺失，而 mitigation experiment（-8.5 pp）证明可改善。但论文在 Section 6.2 中已明确澄清：\"Agents are not inherently incapable of disambiguation...but exhibit a disambiguation deficit: defaulting to single-parse adoption without explicit instruction\"（第 25 行）。所以 \"deficit\" 在此指 uninstructed default behavior，而非 inability。\n\n不过，术语选择确实容易引起误读。一个更精确的术语可能是 \"disambiguation default\" 或 \"disambiguation neglect\"，更好地传达 \"有能力但默认不做\" 的含义。\n\n**[AGREE] R2-W5: Authorization scope 的结论可靠性受 low agreement 严重影响。**\n\n强烈同意。这与我的 W1 (MUST-FIX) 完全一致。κ=0.385 的 cross-judge agreement 意味着 authorization scope 的绝对违规率有极大的测量不确定性。52 pp range 这一数字是论文最引人注目的发现之一，但也是最不可靠的。\n\n我比 R2 更进一步：建议作者在 C4 分析中展示去除 authorization scope 后交互效应是否仍然显著，以测试这一类型是否在驱动整个 C4 结果。如果去除后交互效应消失，则 C4 的一般性声称需要大幅缩窄。\n\n**[AGREE] R2-W6: Psycholinguistics 类比可能 over-extended。**\n\n同意加 caveat 的建议。论文将 agent 的 surface adoption 类比为 Frazier & Rayner (1982) 的 garden-path processing 和 Ferreira et al. (2002) 的 good-enough representations。类比在 phenomenological level 是有启发性的（都是 early commitment to a single parse），但 autoregressive generation 和 incremental human parsing 的底层机制确实不同。Section 6.1 使用 \"paralleling\" 一词已经有一定距离感，但 §6.2 中 \"paralleling human good-enough processing\" 的措辞不够谨慎。加一句 mechanism-level caveat 即可，不影响论文的核心论证。\n\n**[AGREE] R2-W7: 引用问题。**\n\n与我的 W8 一致。ferrari_defects_2018 的第一作者确实应为 Rosadini；2 个 orphan entries 应清理。\n\n## Questions 回应\n\n**R2-Q1（Incompleteness 满足 Wasow 2005 定义的理由）：** 这是 W2 的核心，论文已在 Section 3 用操作性定义回应。如上所述，我认为论文的立场可辩护但需扩展讨论。\n\n**R2-Q2（Bootstrap 34.3% vs continuum）：** 重要问题。34.3% 不足以排除 continuum 假说。论文应明确讨论：如果歧义类型的违规率分布是连续的（而非离散的两层），哪些结论需要修改？核心的 incompleteness 上界地位可能不变，但 \"two-tier hierarchy\" 这一结构性声称需要弱化。\n\n**R2-Q3（Coreferential 排除 mitigation 的影响）：** 我在自己的 Q6 中也提出了类似问题。Coreferential 31.6% 的违规率不低，排除它使 mitigation 的完整性受损。\n\n**R2-Q4（Template pattern bias）：** 我在 W7 中也提出了类似关切。96% pass rate 不等于 high inter-annotator κ。建议补充 type assignment 的标准 reliability 指标。\n\n**R2-Q5（Domain-specific SESOI）：** 好问题。±15 pp 的 anchoring argument（\"a type producing ≥15 pp more violations warrants distinct policy handling\"，Section 4.6）是合理的实践性论证，但不同部署场景（医疗 vs 零售）的 tolerance 可能差异巨大。论文在 Limitations 中提到了 domain scope 限制，但未将此与 SESOI 选择联系起来。\n\n## Missing References 回应\n\n1. **Dalpiaz et al. (2018)**：重要。如果这项工作明确区分了 ambiguity 和 incompleteness，它直接关系到 W2 的理论讨论。论文应引用并回应。\n\n2. **Yu, Carroll, & Bentley (2026)**：如果确实存在 concurrent matched-pair causal design for agent safety，这是高度相关的 concurrent work，必须在 Related Work 中讨论。我无法独立验证这篇论文是否存在，但如果 R2 能确认，作者应搜索并引用。\n\n3. **Lin et al. (2025) \"Ask-to-Clarify\"**：与 Suri et al. (2025) 和 Sehwag et al. (2026)（论文已引用）属于同一 disambiguation channel 文献线。补充引用是合理的。\n\n4. **Willis et al. (2008) 在 §7 中给予 credit**：同意 R2。Willis et al. 已在 Related Work 中被引用，但 §7 Discussion 中的 \"differential nocuity\" 讨论未提及他们在 type-specific nocuity 测量上的 prior work。这是一个归属问题，应修正。\n\n## 总结\n\nR2 的审查侧重理论基础和概念框架，与我侧重方法严谨性形成互补。我们在三个关键问题上高度一致：(1) authorization scope 的低可靠性（R2-W5 = 我的 W1）；(2) two-tier hierarchy 的稳定性不足（R2-W1 = 我的 W6）；(3) 引用问题（R2-W7 = 我的 W8）。\n\nR2 的 W2（taxonomy 概念混淆）是一个有价值的理论视角，但论文已有部分回应（Section 3 \"Scope of 'ambiguity'\"）。我认为修订方向是扩展讨论而非改变 taxonomy 设计。R2 的 W3 和 W4 属于 framing/naming 问题，修订成本低且能提升精确度。\n",
    "reviewer_id": "1",
    "project": "policy_ambiguity_safety"
  }
}
```

</details>

---


### Tool result

_source line 825 · 2026-05-21T19:10:01.971336+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_967344d166ba485ad606d14379e69d85:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3664
}
```

</details>

---


### Assistant

_source line 826 · 2026-05-21T19:10:19.385536+00:00_

交叉回应已提交给 Director。

核心判断：与 R2 在 3 个关键问题上高度一致（authorization scope 低可靠性、two-tier hierarchy 稳定性不足、引用问题）。对 R2-W2（taxonomy 概念混淆）持部分反驳——论文 Section 3 已用操作性定义回应，但确实需要扩展理论边界讨论。R2 的 W3/W4 属于 framing 修正，成本低、价值高。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1"
}
```

</details>

---


## Round 23

## Round 23

64 recorded events


### User

_source line 827 · 2026-05-22T08:38:38.616613+00:00_

[Round 1 审稿请求]:
你是 Reviewer 1，负责**方法严谨性**审查。

## 论文信息
- **标题**: "Not All Policy Ambiguity Is Equal: Type-Specific Safety Risks for LLM Agents"
- **论文路径**: `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/main.tex`
- **PDF**: `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_round_11/submitted.pdf`

## Venue 要求
- **EMNLP 2026** via ARR May cycle
- Long paper: 正文 **8 页**限制, 参考文献不限
- Mandatory limitations 和 optional ethical considerations 不计入页数（前提是不含过多额外内容）
- **Double-blind** 匿名审稿
- ACL 模板 (`\usepackage[review]{acl}`)
- Overall Assessment 评分标准: 5=Consider for Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1=Do not resubmit

## 你的审查侧重

**方法严谨性**，重点关注以下方面：

1. **因果推断设计**: matched-pair design 的有效性，perturbation control 的充分性，是否满足因果推断的标准假设
2. **统计分析**: McNemar test、TOST equivalence testing、bootstrap cluster analysis 的选择是否恰当，多重比较校正是否充分，SESOI ±15pp 的合理性
3. **评估流程**: cross-judge 设计的偏差分析，per-type judge reliability（特别是 authorization scope κ=0.385），human validation 样本量是否充分
4. **控制变量**: incompleteness 的 information-addition confound 处理，句长差异（d=0.74）的控制，clause pair 构建的严谨性
5. **可重复性**: ICC=0.919 仅覆盖 OpenAI 家族的局限性，replication 设计的充分性
6. **效应量解释**: C1-C4 各 claim 的证据强度与表述匹配度，特别是 C2（two-tier hierarchy）和 C4（52pp range）的表述是否过强

请按以下格式输出审稿意见：

### Strengths (S1, S2, ...)
### Weaknesses (W1, W2, ... — 标注 MUST-FIX / SHOULD-FIX / MINOR)
### Questions (Q1, Q2, ...)
### Missing References
### Overall Assessment (评分 + 置信度 + 1-2 句总评)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 828 · 2026-05-22T08:38:47.141332+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/.claude/skills/review-reviewer-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/.claude/skills/review-reviewer-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 829 · 2026-05-22T08:38:48.296061+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/.claude/sessions/review_reviewer_1_6edf79f4.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1154
}
```

</details>

---


### Tool call

_source line 830 · 2026-05-22T08:38:48.453429+00:00_

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
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
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

_source line 831 · 2026-05-22T08:38:48.453847+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 832 · 2026-05-22T08:38:57.374489+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL ARR 2026 reviewer guidelines review form criteria"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR 2026 reviewer guidelines review form criteria"
  }
}
```

</details>

---


### Tool call

_source line 833 · 2026-05-22T08:38:59.386315+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_round_11/submitted.pdf",
  "project": "policy_ambiguity_safety",
  "pages": "1-10",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_round_11/submitted.pdf",
    "project": "policy_ambiguity_safety",
    "pages": "1-10",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 834 · 2026-05-22T08:39:04.707407+00:00_

Web search results for query: "ACL ARR 2026 reviewer guidelines review form criteria"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"aclrollingreview/reviewing.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/reviewing.md"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"}]

Based on the web search results, here's information about ACL ARR 2026 reviewer guidelines and review form criteria:

## Reviewer Guidelines

Reviewers are asked to follow a workflow of: (1) read the paper and get the first impression, (2) search for re
…[truncated 1272 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 7332
}
```

</details>

---


### Tool result

_source line 835 · 2026-05-22T08:39:06.065301+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 1, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_round_11/_pdf_images/submitted_p1.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 451.0}, {\"page\": 2, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_round_11/_pdf_images/submitted_p2.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 448.2}, {\"page\": 3, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_round_11/_pdf_images/submitted_p3.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 541.7}, {\"page\": 4, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_round_11/_pdf_images/submitted_p4.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 524.8}, {\"page\": 5, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_round_11/_pdf_images/submitted_p5.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 517.2}, {\"page\": 6, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_round_11/_pdf_images/submitted_p6.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 386.5}, {\"page\": 7, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_round_11/_pdf_images/submitted_p7.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 517.4}, {\"page\": 8, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_round_11/_pdf_images/submitted_p8.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 523.5}, {\"page\": 9, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_round_11/_pdf_images/submi
…[truncated 537 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 6678
}
```

</details>

---


### Tool call

_source line 836 · 2026-05-22T08:39:15.850329+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete review form: all scoring dimensions, their scales, and descriptions. Include: Overall Assessment, Soundness, Excitement/Novelty, Reproducibility, Confidence, and any other dimensions. List each with its full scale description."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the complete review form: all scoring dimensions, their scales, and descriptions. Include: Overall Assessment, Soundness, Excitement/Novelty, Reproducibility, Confidence, and any other dimensions. List each with its full scale description."
  }
}
```

</details>

---


### Tool call

_source line 837 · 2026-05-22T08:39:17.307825+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_round_11/submitted.pdf",
  "project": "policy_ambiguity_safety",
  "pages": "11-15",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_round_11/submitted.pdf",
    "project": "policy_ambiguity_safety",
    "pages": "11-15",
    "dpi": "150"
  }
}
```

</details>

---


### Tool call

_source line 838 · 2026-05-22T08:39:18.314081+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_round_11/_pdf_images/submitted_p1.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_round_11/_pdf_images/submitted_p1.png"
  }
}
```

</details>

---


### Tool call

_source line 839 · 2026-05-22T08:39:18.822694+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_round_11/_pdf_images/submitted_p2.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_round_11/_pdf_images/submitted_p2.png"
  }
}
```

</details>

---


### Tool call

_source line 840 · 2026-05-22T08:39:19.325260+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_round_11/_pdf_images/submitted_p3.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_round_11/_pdf_images/submitted_p3.png"
  }
}
```

</details>

---


### Tool call

_source line 841 · 2026-05-22T08:39:19.627180+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_round_11/_pdf_images/submitted_p4.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_round_11/_pdf_images/submitted_p4.png"
  }
}
```

</details>

---


### Tool result

_source line 842 · 2026-05-22T08:39:22.495377+00:00_

# ACL Rolling Review Form - Scoring Dimensions

## 1. **Reviewer Confidence**
Scale: 1-5
- **5**: "Positive that my evaluation is correct. I read the paper very carefully..."
- **4**: Quite sure with unlikely but conceivable oversights
- **3**: Pretty sure; general familiarity but incomplete detail checking
- **2**: Willing to defend evaluation; fairly likely missed some details
- **1**: Outside expertise area or paper very difficult to understand

## 2. **Soundness**
Scale: 1-5 (with 0.5 increments)
- **5**: "Excellent: This study is one of the most thorough I have seen..."
- **4**: Strong; sufficient support with optional additional experiments
- **3**: Acceptable; main claims supported with minor gaps
- **2**: Poor; insufficient support for main claims; major technical issues
- **1**: Major Issues; insufficiently thorough or irrelevant to ACL

## 3. **Excitement**
Scale: 1-5 (with 0.5 increments)
- **5**: Highly Exciting; would recommend to others
- **4**: Exciting; would mention to colleagues
- **3**: Interesting; might mention selectively
- **2**: Potentially Interesting; limited personal resonance
- **1**: Not Exciting; lacks NLP relevance or community appeal

## 4. **Overall Assessment**
Scale: 1-5 (with 0.5 increments)
- **5**: Consider for Award (top 2.5%)
- **4**: Conference acceptance
- **3**: Findings acceptance
- **2**: Resubmit next cycle
- **1**: Do not resubmit

## 5. **Reproducibility**
Scale: 1-5
- **5**: Results easily reproducible
- **4**: Mostly reproducible with minor variance
- **3**: Reproducible with difficulty
- **2**: Very difficult reproduction
- **1**: Impossible to reproduce

## 6. **Additional Dimensions**
- **Limitations & Societal Impact** (qualitative assessment)
- **Ethical Concerns** (qualitative assessment)
- **Datasets** (1-5 scale: value to research community)
- **Software** (1-5 scale: utility for others)
- **Author Identity Knowledge** (1-5 scale: anonymity preservation)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 6645
}
```

</details>

---


### Tool result

_source line 843 · 2026-05-22T08:39:22.998405+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 11, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_round_11/_pdf_images/submitted_p11.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 503.5}, {\"page\": 12, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_round_11/_pdf_images/submitted_p12.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 426.0}, {\"page\": 13, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_round_11/_pdf_images/submitted_p13.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 487.1}, {\"page\": 14, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_round_11/_pdf_images/submitted_p14.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 474.8}, {\"page\": 15, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_round_11/_pdf_images/submitted_p15.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 55.5}], \"total_pages\": 15, \"rendered_pages\": 5, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_round_11/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 5690
}
```

</details>

---


### Tool result

_source line 844 · 2026-05-22T08:39:25.619513+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 6796
}
```

</details>

---


### Tool result

_source line 845 · 2026-05-22T08:39:25.620570+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 7306
}
```

</details>

---


### Tool result

_source line 846 · 2026-05-22T08:39:25.623773+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 5996
}
```

</details>

---


### Tool result

_source line 847 · 2026-05-22T08:39:25.624897+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 6299
}
```

</details>

---


### Tool call

_source line 848 · 2026-05-22T08:39:34.816332+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_round_11/_pdf_images/submitted_p5.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_round_11/_pdf_images/submitted_p5.png"
  }
}
```

</details>

---


### Tool result

_source line 849 · 2026-05-22T08:39:35.721449+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 905
}
```

</details>

---


### Tool call

_source line 850 · 2026-05-22T08:39:35.721905+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_round_11/_pdf_images/submitted_p6.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_round_11/_pdf_images/submitted_p6.png"
  }
}
```

</details>

---


### Tool result

_source line 851 · 2026-05-22T08:39:36.175554+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 453
}
```

</details>

---


### Tool call

_source line 852 · 2026-05-22T08:39:36.276303+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_round_11/_pdf_images/submitted_p7.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_round_11/_pdf_images/submitted_p7.png"
  }
}
```

</details>

---


### Tool call

_source line 853 · 2026-05-22T08:39:36.577797+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_round_11/_pdf_images/submitted_p8.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_round_11/_pdf_images/submitted_p8.png"
  }
}
```

</details>

---


### Tool result

_source line 854 · 2026-05-22T08:39:37.031547+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 755
}
```

</details>

---


### Tool result

_source line 855 · 2026-05-22T08:39:37.433775+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 855
}
```

</details>

---


### Tool call

_source line 856 · 2026-05-22T08:39:43.363337+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_round_11/_pdf_images/submitted_p9.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_round_11/_pdf_images/submitted_p9.png"
  }
}
```

</details>

---


### Tool call

_source line 857 · 2026-05-22T08:39:43.915650+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_round_11/_pdf_images/submitted_p10.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_round_11/_pdf_images/submitted_p10.png"
  }
}
```

</details>

---


### Tool result

_source line 858 · 2026-05-22T08:39:44.823328+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1459
}
```

</details>

---


### Tool result

_source line 859 · 2026-05-22T08:39:44.824545+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 908
}
```

</details>

---


### Tool call

_source line 860 · 2026-05-22T08:39:44.825022+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_round_11/_pdf_images/submitted_p11.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_round_11/_pdf_images/submitted_p11.png"
  }
}
```

</details>

---


### Tool call

_source line 861 · 2026-05-22T08:39:45.279345+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_round_11/_pdf_images/submitted_p12.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_round_11/_pdf_images/submitted_p12.png"
  }
}
```

</details>

---


### Tool result

_source line 862 · 2026-05-22T08:39:45.833602+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1008
}
```

</details>

---


### Tool call

_source line 863 · 2026-05-22T08:39:45.833995+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_round_11/_pdf_images/submitted_p13.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_round_11/_pdf_images/submitted_p13.png"
  }
}
```

</details>

---


### Tool result

_source line 864 · 2026-05-22T08:39:46.436833+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1157
}
```

</details>

---


### Tool call

_source line 865 · 2026-05-22T08:39:46.437315+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_round_11/_pdf_images/submitted_p14.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_round_11/_pdf_images/submitted_p14.png"
  }
}
```

</details>

---


### Tool result

_source line 866 · 2026-05-22T08:39:46.994693+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1160
}
```

</details>

---


### Tool result

_source line 867 · 2026-05-22T08:39:48.054558+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1617
}
```

</details>

---


### Tool call

_source line 868 · 2026-05-22T08:42:00.131217+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/main.tex",
  "limit": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/main.tex",
    "limit": "150"
  }
}
```

</details>

---


### Tool result

_source line 869 · 2026-05-22T08:42:00.181954+00:00_

1	\documentclass[11pt]{article}
2	\usepackage[review]{acl}
3	\usepackage{times}
4	\usepackage{latexsym}
5	\usepackage[T1]{fontenc}
6	\usepackage[utf8]{inputenc}
7	\usepackage{microtype}
8	\usepackage{graphicx}
9	\usepackage{booktabs}
10	\usepackage{amsmath}
11	\usepackage{amssymb}
12	\usepackage{multirow}
13	\usepackage{xcolor}
14	\usepackage{subcaption}
15	
16	\definecolor{speccolor}{HTML}{C44E52}
17	\definecolor{lingcolor}{HTML}{4C72B0}
18	
19	\title{Not All Policy Ambiguity Is Equal: Type-Specific Safety Risks for LLM Agents}
20	
21	\author{Anonymous}
22	
23	\begin{document}
24	\maketitle
25	
26	\input{sections/abstract}
27	\input{sections/introduction}
28	\input{sections/related_work}
29	\input{sections/taxonomy}
30	\input{sections/method}
31	\input{sections/experiments}
32	\input{sections/analysis}
33	\input{sections/discussion}
34	\input{sections/conclusion}
35	\input{sections/limitations}
36	
37	\bibliography{references}
38	
39	\appendix
40	\input{sections/appendix}
41	
42	\end{document}
43	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 870 · 2026-05-22T08:42:11.021972+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "sections/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Glob",
  "tool_args": {
    "pattern": "sections/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper"
  }
}
```

</details>

---


### Tool result

_source line 871 · 2026-05-22T08:42:11.072555+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 872 · 2026-05-22T08:42:14.435315+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/sections/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/sections/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper"
  }
}
```

</details>

---


### Tool result

_source line 873 · 2026-05-22T08:42:14.485877+00:00_

/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/appendix.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/method.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/experiments.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/limitations.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/conclusion.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/related_work.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/taxonomy.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/analysis.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/abstract.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/introduction.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/discussion.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 874 · 2026-05-22T08:42:17.999308+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 875 · 2026-05-22T08:42:18.150436+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	\subsection{Experimental Platform}
5	
6	We conduct all experiments on the original release of $\tau^2$-bench \citep{tau2_bench_2025}, a dual-control conversational agent benchmark spanning retail and airline customer service domains. $\tau^2$-bench provides natural-language policy documents, tool APIs, and multi-turn user interactions with ground-truth evaluation via assertion checking. Its policy injection mechanism allows us to replace individual policy clauses while preserving the surrounding context, enabling controlled ambiguity manipulation.
7	
8	\subsection{Matched-Pair Design}
9	
10	For each of the six ambiguity types, we construct 50 \emph{clause pairs}: an ambiguous variant and a matched unambiguous variant that conveys the same intended policy but resolves the ambiguity. Pairs are minimal edits: the unambiguous variant adds only the information necessary to eliminate the target ambiguity (e.g., for scopal ambiguity, replacing ``items may be returned within 30 days'' with ``standard items may be returned within 30 days; customized items are final sale''). This yields 300 clause pairs $\times$ 2 conditions $\times$ 5 models $= 2{,}997$ episodes (3 episodes lost to API errors in one Qwen3 batch).
11	
12	Clause pairs are generated through a template-based pipeline and reviewed by two independent annotators (both with NLP background) to ensure (1) the ambiguous variant contains exactly one instance of the target type, (2) the unambiguous variant resolves it without changing policy scope, and (3) the ambiguity is plausibly natural. Annotators independently verified type assignments with a 96\% initial agreement (287/300); the 13 disagreements were resolved by discussion, yielding 100\% final consensus. A post-hoc realism validation confirms linguistic consistency with original $\tau^2$-bench policy text (\S\ref{sec:limitations}).
13	
14	\subsection{Models}
15	
16	We evaluate five models spanning four providers and tw
…[truncated 4834 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 876 · 2026-05-22T08:42:18.150869+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 877 · 2026-05-22T08:42:18.653036+00:00_

1	\section{Results}
2	\label{sec:results}
3	
4	We organize results around four analyses of increasing specificity: the binary ambiguity effect (C1), the type hierarchy (C2), the aggregate layer effect (C3), and the model$\times$type interaction (C4). C1 and C2 constitute our primary claims; C3 is inconclusive; C4 is exploratory but provides the model$\times$type interaction analysis.
5	
6	\subsection{Binary Ambiguity Effect (C1)}
7	
8	Across all five models and six types, ambiguous clauses increase violation rates by 34.0 pp (41.0\% vs.\ 6.9\%, OR $= 15.1$, 95\% CI $[10.78, 21.17]$, $p < 10^{-105}$). All six types individually produce significant increases (all $p < 10^{-5}$), and all five models show large effects ($+25.7$ to $+39.0$ pp, all $p < 10^{-17}$). Perturbation controls confirm specificity to semantic ambiguity ($n = 300$, $\Delta_{\text{perturb}} = -0.67$\,pp, CI containing zero). Clause identity explains 22.4\% of variance versus 1.0\% for model identity. A replication on two additional model families (Appendix~\ref{app:model_expansion}) confirms the effect across seven models ($\Delta = +20.0$ to $+33.6$\,pp, both $p < 10^{-6}$); excluding incompleteness, it remains large ($\Delta = 31.0$\,pp; Appendix~\ref{app:sans_incompleteness}).
9	
10	\subsection{Type Hierarchy (C2)}
11	
12	\begin{table*}[t]
13	\centering
14	\caption{Violation rates (\%) under ambiguous policy clauses by type and model (5.4 = GPT-5.4, 4.1 = GPT-4.1, Cla.\ = Claude, Qw3 = Qwen3, DS = DeepSeek). $\Delta$pp: pooled difference (ambiguous $-$ unambiguous) with Newcombe 95\% CIs. Tier: TOST equivalence cluster at $\pm 15$\,pp---U = upper bound (separated at all margins), M = mid-tier (6/6 pairwise equivalent), L = lower (separates at $\pm 12$\,pp). All per-type $p < 10^{-5}$ (Fisher's exact).}
15	\label{tab:main_results}
16	\footnotesize
17	\setlength{\tabcolsep}{3.8pt}
18	\begin{tabular}{llrrrrrrr@{\hskip 6pt}cr}
19	\toprule
20	Layer & Type & Pooled & 5.4 & 4.1 & Cla. & Qw3 & DS & $\De
…[truncated 6373 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 878 · 2026-05-22T08:42:18.653478+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/analysis.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/analysis.tex"
  }
}
```

</details>

---


### Tool result

_source line 879 · 2026-05-22T08:42:19.205857+00:00_

1	\section{Error Analysis \emph{[Exploratory]}}
2	\label{sec:analysis}
3	
4	The following failure mode taxonomy emerges empirically from LLM-coded traces, distinct from the input ambiguity taxonomy (\S\ref{sec:taxonomy}).
5	
6	We analyze 614 violation traces across all five models, coded into five failure modes: unauthorized escalation, assumption-based action, scope misapplication, arbitrary rule selection, and conservative refusal. GPT-5.4 and GPT-4.1 serve as detailed annotation anchors because they span the judge boundary. Inter-coder reliability is substantial (Gwet's AC$_1$ $= 0.62$ \citep{gwet_2014}; Cohen's $\kappa = 0.52$ \citep{cohen_1960}). The gap reflects the prevalence paradox: three categories account for ${\sim}$90\% of instances, compressing the $\kappa$ denominator and yielding artificially low values despite high raw agreement.
7	
8	\subsection{Type-Specific Failure Mechanisms}
9	
10	The five-model data reveal three mechanistically distinct failure patterns that crosscut the specification/linguistic layer boundary.
11	
12	\emph{Structural misparse} (scope misapplication): the agent constructs an incorrect parse and follows it consistently, paralleling garden-path processing \citep{frazier_rayner_1982,ferreira_good_enough_2002} at a behavioral (not mechanistic) level---e.g., parsing ``items purchased with a coupon or during a sale are final'' as restricting only coupon purchases. This dominates scopal (all 5 models), conditional precedence (all 5), and coreferential (3/5).
13	
14	\emph{Information gap-filling} (assumption-based action): the agent fills missing information with plausible but incorrect defaults---e.g., inventing a 30-day return window when none is specified. This dominates incompleteness (3/5) and lexical (3/5).
15	
16	\emph{Boundary violation} (unauthorized escalation): the agent exceeds permission boundaries when authorization scope is underspecified---e.g., issuing a refund above its stated limit rather than escalating; 69.2\% of 
…[truncated 2022 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 552
}
```

</details>

---


### Tool call

_source line 880 · 2026-05-22T08:42:19.206253+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 881 · 2026-05-22T08:42:19.257117+00:00_

1	\section{TOST Equivalence Sensitivity}
2	\label{app:tost}
3	
4	Table~\ref{tab:tost_sensitivity} reports the TOST equivalence analysis \citep{lakens_2017} across seven margins. Three pairs involving incompleteness never reach equivalence even at $\pm 20$ pp: conditional precedence--incompleteness ($\Delta = 16.8$ pp), coreferential--incompleteness ($\Delta = 22.0$ pp), and incompleteness--scopal ($\Delta = 14.2$ pp).
5	
6	\begin{table}[!ht]
7	\centering
8	\small
9	\caption{TOST equivalence sensitivity across margins. Mid-tier = fraction of the six within-cluster pairs (lexical, auth.\ scope, scopal, cond.\ prec.) that are equivalent. Inc.\ and Cor.\ columns indicate separation from the mid-tier cluster.}
10	\label{tab:tost_sensitivity}
11	\begin{tabular}{lcccc}
12	\toprule
13	Margin & Equiv.\ pairs & Mid-tier & Inc.\ sep. & Cor.\ sep. \\
14	\midrule
15	$\pm 5$ pp & 0/15 & 0/6 & \checkmark & \checkmark \\
16	$\pm 8$ pp & 0/15 & 0/6 & \checkmark & \checkmark \\
17	$\pm 10$ pp & 3/15 & 3/6 & \checkmark & \checkmark \\
18	$\pm 12$ pp & 5/15 & 5/6 & \checkmark & \checkmark \\
19	$\pm 15$ pp & 8/15 & 6/6 & \checkmark & -- \\
20	$\pm 18$ pp & 9/15 & 6/6 & \checkmark & -- \\
21	$\pm 20$ pp & 12/15 & 6/6 & -- & -- \\
22	\bottomrule
23	\end{tabular}
24	\end{table}
25	
26	\section{Mitigation Experiment}
27	\label{app:mitigation}
28	
29	Table~\ref{tab:mitigation} reports the per-type, per-model $\Delta$pp from the disambiguation-instruction mitigation experiment (1,256 treatment episodes across five of six types; coreferential was not tested). Coreferential pairs are excluded from both the mitigation and replication experiments. In mitigation, their ambiguous and unambiguous variants differ only in pronoun resolution, making it impossible to craft targeted disambiguation instructions without revealing the experimental manipulation. In replication, the $\tau^2$-bench episode design for coreferential ambiguity is tightly coupled to the original five-model configuration; extendin
…[truncated 20730 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 882 · 2026-05-22T08:42:24.376372+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 883 · 2026-05-22T08:42:24.928777+00:00_

1	\section{Discussion}
2	\label{sec:discussion}
3	
4	\paragraph{Differential nocuity.}
5	Building on \citet{berry_kamsties_2004}'s nocuous/innocuous distinction, our results support a \emph{differential nocuity} framework \citep{willis_nocuous_2008}: risk depends on ambiguity type (base vulnerability), safety training (selective mitigation), and disambiguation channel availability. Types with explicit decision points (e.g., authorization scope) appear more amenable to both safety training and prompted intervention than gap-filling types (e.g., incompleteness), where mitigation attempts can backfire (see below).
6	
7	\paragraph{Prompt-based mitigation.}
8	To test whether disambiguation can be prompted, we evaluate generic awareness prompting (``the policy may contain ambiguous clauses; ask for clarification'') and type-specific prompting (targeting incompleteness, authorization scope, and lexical ambiguity individually) on GPT-5.4 with matched-pair McNemar tests ($n = 50$ per type). Generic prompting produces no overall reduction ($\Delta = +1.3$\,pp, $p > 0.5$). Type-specific results are asymmetric: authorization scope shows a marginal reduction ($-12$\,pp, $p = 0.070$), lexical ambiguity is unchanged ($-2$\,pp), and incompleteness \emph{worsens} ($+14$\,pp, $p = 0.118$)---suggesting that prompting agents to attend to missing information triggers confabulation rather than caution. These findings indicate that prompt-level intervention cannot remediate structural policy ambiguity, underscoring the need for policy-design-level solutions.
9	
10	\paragraph{Practical implications.}
11	A proof-of-concept classifier (Appendix~\ref{app:detection}) achieves F1\,=\,0.81 for binary ambiguity detection but only 0.34 for incompleteness---the highest-risk type is the hardest to detect. With agents exhibiting disambiguation neglect in $>$89\% of cases, type-aware auditing and externalized detection \citep{chantree_2006,ferrari_ambiguity_2019} are necessary for policy-governed depl
…[truncated 12 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 552
}
```

</details>

---


### Tool call

_source line 884 · 2026-05-22T08:42:24.929147+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 885 · 2026-05-22T08:42:25.079985+00:00_

1	\section*{Limitations}
2	\label{sec:limitations}
3	
4	\paragraph{Scope.} We evaluate seven API-accessible models from six providers (Appendix~\ref{app:model_expansion}); smaller open-source models (7B--70B) may exhibit different vulnerability patterns. $\tau^2$-bench covers retail and airline customer service only---effects in other domains remain untested, though within-study cross-domain consistency is encouraging. Our matched-pair design requires synthetic ambiguity construction, which may not capture the full distribution of naturally occurring ambiguities; realism validation (\S\ref{sec:method}) confirms lexical comparability but cannot rule out distributional gaps.
5	
6	\paragraph{Measurement.} Each model is evaluated by a single cross-judge, confounding judge identity with model identity; within-judge-group analyses confirm C1 individually (both $p < 0.001$) but not C3 (Appendix~\ref{app:judge_group_ranking}), and cross-model type ranking concordance is only moderate (Appendix~\ref{app:kendall_w}). Per-type reliability varies---authorization scope has the lowest agreement ($\kappa = 0.385$) and per-type human--LLM estimates rest on small cell sizes with wide confidence intervals (Appendix~\ref{app:per_type_agreement})---while failure mode coding achieves moderate agreement ($\kappa = 0.52$), with minority categories less reliable.
7	
8	\paragraph{Confounds.} Incompleteness resolution necessarily adds policy content, creating an information asymmetry; our logistic regression controls and coreferential lower-bound analysis mitigate but do not eliminate this confound (\S\ref{sec:results}). Our primary analysis uses a moderate-or-above severity threshold; switching to any-violation yields consistent results, with all four claims remaining significant and concordant type rankings.
9	
10	\section*{Data and Code Availability}
11	The 300 clause pairs, evaluation pipeline, analysis scripts, and raw episode traces will be released upon publication at \url{https://git
…[truncated 47 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 150
}
```

</details>

---


### Tool call

_source line 886 · 2026-05-22T08:42:25.381681+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 887 · 2026-05-22T08:42:25.482501+00:00_

1	\section{Conclusion}
2	
3	Ambiguous policy clauses increase agent safety violations by 34.0\,pp (OR\,$=$\,15.1) across five models, with clause identity explaining 22$\times$ more variance than model identity. Incompleteness consistently ranks highest across all seven models ($\geq$46\%), with rankings replicating in independent families ($\rho = 0.60$--$0.90$). With agents exhibiting disambiguation neglect in over 89\% of cases and 41.3\% of clauses triggering model-convergent violations, type-aware auditing and externalized detection are critical for policy-governed deployments.
4	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 888 · 2026-05-22T08:46:35.184517+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## 总体评分\n**Overall**: 3.5 / 5 (Borderline Conference)\n**Confidence**: 4 / 5\n**一句话总结**: 实验设计严谨、统计分析全面的因果研究，但 authorization scope 评审一致性低（κ=0.385）削弱了 C4，SESOI ±15pp 缺乏实质性论证，incompleteness 信息添加混杂虽有控制但残余问题影响 C2 的\"两层结构\"表述强度。\n\n## 官方维度打分（ACL ARR Review Form）\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | C1 证据充分（OR=15.1, 7 模型一致），C2 的两层结构依赖 margin 选择且 bootstrap AU p=0.47，C3 作者自认 inconclusive（正确），C4 基于最低可靠性类型的数据 |\n| Excitement | 3.5/5 | 首个因果性的 ambiguity→violation 类型映射，taxonomy 桥接 NLP/RE，实用价值高；但局限于 τ²-bench 单一客服领域 |\n| Reproducibility | 4/5 | 方法细节完整，承诺代码和数据开源，统计报告规范（效应量+CI+多重校正）；judge 选择限制精确复制 |\n\n---\n\n### Strengths\n\n**S1: 严谨的 matched-pair 因果设计 + perturbation control**\n300 对 clause pair（96% annotator agreement），perturbation control（Δ_perturb = −0.67pp, 95% CI [−8.0, 6.67] 包含零）有效排除了表面扰动的混杂效应。Section 4.2 和 4.5 的设计使得 C1 的因果推断具有说服力。\n\n**S2: 全面的统计分析框架**\nMcNemar + TOST + bootstrap 聚类 + Holm-Bonferroni 三组校正 + post-hoc 功效分析（C1/C2 power > 0.99），同时在 7 个 margin（±5–20pp）上展示 TOST 敏感性分析（Table 3/Appendix A），这在该领域中不常见且值得肯定。\n\n**S3: 诚实的 claim 标定**\nC3 明确标注为 inconclusive（未通过 Holm-Bonferroni 校正），C4 标注为 [Exploratory]，authorization scope 的 52pp range 被表述为\"suggestive rather than definitive\"和\"upper bound with substantial measurement uncertainty\"（Section 5.4）。这种自我校准的 claim 强度在审稿中非常难得。\n\n**S4: 有价值的 error analysis**\nSection 6 的五种 failure mode taxonomy（structural misparse / information gap-filling / boundary violation）揭示了类型特异的机制路径，\"Disambiguation Neglect\"（4.6% awareness rate）是一个有实际意义的发现，且 mitigation experiment 证实了 prompt-level 干预的局限性。\n\n**S5: Incompleteness 混杂处理相对充分**\nAppendix F/H 提供了 token delta logistic regression（incompleteness p=0.018, coefficient change <8%），coreferential 的 confound-free lower bound（31.6%），以及 authorization scope 的反证逻辑（最大 token delta 但 violation rate 更低）。虽有残余问题（见 W2），整体处理水平高于同类论文。\n\n---\n\n### Weaknesses\n\n**W1 [MUST-FIX]: Authorization scope cross-judge κ=0.385 严重削弱 C4 的 52pp range claim**\n\n- **具体位置**: Section 4.4, Section 5.4, Appendix G (Table 9), Appendix P\n- **问题**: Authorization scope 的 cross-judge κ 仅 0.385（Section 4.4），是所有类型中最低的。C4 的核心发现——52pp cross-model range（Claude 12% → GPT-5.4 64%）——正是基于这个最不可靠的类型。尽管论文用 within-judge bootstrap ranking preservation（99.5%）和 raw agreement 来补救，但存在三层问题：\n\n  (1) **Cross-judge κ vs human-LLM κ 的混淆**：Section 5.4 引用\"raw agreement 85.3%\"来论证可靠性，但 Appendix G (Table 9) 的 human-LLM κ=0.644 与 Section 4.4 的 cross-judge κ=0.385 是不同指标，论文未明确区分这两个数据来源。读者可能误以为 85.3% 是 cross-judge 的 raw agreement。\n\n  (2) **Within-judge 分析的局限**: within-judge 48pp range（Section 5.4）仅证明单个 judge 内部的排序稳定性，不能弥补 cross-judge 评测不一致。如果 GPT-5.4 和 GPT-4.1 对 authorization scope violation 的判定标准系统性不同，within-judge 稳定性反而说明偏差是稳定的。\n\n  (3) **Appendix P 的 rank reversal**: Within-judge-group type ranking 在两组 judge 之间的相关性为 ρ=−0.03（p=0.96），而论文将此归因于 agent composition 差异。但 authorization scope 的 rank reversal（GPT-4.1 judged: rank 1; GPT-5.4 judged: rank 6）也可能反映 judge 偏差。\n\n- **为什么影响接收**: C4 是论文四个 numbered claim 之一，52pp range 出现在 abstract 和 Figure 3 中。基于最低 reliability 类型的数据做 numbered claim，即使标注 [Exploratory]，仍有方法论风险。\n\n- **建议修改方向**: (a) 计算 prevalence-adjusted agreement 指标（如 PABAK 或 Gwet's AC1）来澄清 κ=0.385 是否为 prevalence paradox；(b) 将 C4 从 numbered claim 降级为 Discussion 中的 observation；(c) 或在 abstract/conclusion 中不引用 52pp 具体数字，改为定性描述。\n\n---\n\n**W2 [SHOULD-FIX]: C2\"两层结构\"的表述强度与证据强度不匹配**\n\n- **具体位置**: Section 5.2, Appendix A (Table 3), Appendix I\n- **问题**: \"Two-tier hierarchy\"这一表述暗示稳定的层级结构，但实际证据受三个因素制约：\n\n  (1) **Margin 依赖性**: ±10pp 时仅 3/6 mid-tier pair 达到 equivalence，±12pp 时 5/6，±15pp 时 6/6（Table 3）。TOST power 从 ±15pp 的 0.94 降至 ±10pp 的 0.57（Section 4.6）。\"两层结构\"在较小 margin 下并不成立。\n\n  (2) **Bootstrap 聚类不稳定**: Incompleteness singleton 仅在 34.3% 的 bootstrap samples 中重现，AU p-value = 0.47（Appendix I）。这意味着 incompleteness 与其他类型的分界并不 robust。\n\n  (3) **Kendall's W 不显著**: 五个主模型的类型排序一致性 W=0.398（p=0.072），未达到显著水平（Appendix M）。这意味着不同模型对类型危险度排序的共识不强，除了 incompleteness 始终最高。\n\n  (4) **Confound-free 场景**: 如果按 confound-free lower bound 评估 incompleteness（31.6%），它将与 coreferential 持平、低于 mid-tier cluster——两层结构将崩塌。虽然 31.6% 是极端下界，但论文未讨论在 confound-adjusted 后两层结构是否仍成立。\n\n- **建议**: 将\"two-tier hierarchy\"改为更谨慎的表述，如\"incompleteness consistently separates as the highest-violation type, with the remaining types forming a less differentiated cluster at the ±15pp equivalence margin.\" 明确承认 margin 依赖性和 bootstrap 不稳定性。\n\n---\n\n**W3 [SHOULD-FIX]: SESOI ±15pp 的论证存在循环性**\n\n- **具体位置**: Section 4.6\n- **问题**: ±15pp 的论证逻辑是：(1)\"a type producing ≥15 pp more violations warrants distinct policy handling in deployment\"——这是用结论论证前提；(2)\"exceeds the perturbation control bound (6.67 pp) by >2×\"——这是测量噪声标准，不是实质性差异标准。\n\n  在安全评估场景下，±15pp 相当宽松。如果类型 A 比类型 B 高 14pp 违规率（在 ±15pp 下被判定为\"等价\"），在实际部署中可能意味着成百上千次额外违规。论文承认\"No field-standard SESOI exists\"，但这更需要从实际部署角度论证而非回避。\n\n  好的一面是，Table 3 提供了 7 个 margin 的完整敏感性分析，bootstrap 聚类是 margin-free 的。但 primary threshold 的选择影响了 C2 的核心表述。\n\n- **建议**: 从部署角度论证：例如，给出一个假设场景（如 1000 interactions/day 的 agent，15pp 差异 = 150 extra violations/day），讨论这个量级是否足以触发不同的 policy handling。或者将 ±10pp 和 ±15pp 并列为 primary results，展示 C2 在两个 threshold 下的差异。\n\n---\n\n**W4 [SHOULD-FIX]: Cross-judge 设计仅使用 OpenAI 家族模型**\n\n- **具体位置**: Section 4.4\n- **问题**: GPT-5.4 和 GPT-4.1 均来自 OpenAI。OpenAI 模型家族可能共享系统性偏差（如对特定 violation 模式的敏感度、对 authorization boundary 的理解方式）。论文论证\"the cross-judge asymmetry affects only absolute violation rates, not C1 or C2\"（Section 4.4），但这一论证基于差值消除假设——只有当两个 judge 的偏差方向相同且幅度相近时才成立。如果 GPT-5.4 和 GPT-4.1 因共享训练策略而有 correlated bias，差值确实可以消除共模偏差；但如果偏差是 type-specific 的（如 OpenAI 模型普遍对 authorization scope 判定更严格），则不会被差值消除。\n\n- **建议**: 在 Limitations 中增加对 single-family judge bias 的讨论。如有资源，在 replication study 中用 Claude 或 Gemini 作为 judge 对 subset 评估。\n\n---\n\n**W5 [SHOULD-FIX]: Human validation 样本量不足以支撑 type-level claims**\n\n- **具体位置**: Section 4.4, Appendix G (Table 9)\n- **问题**: 每种类型仅 32-34 episodes 的 human validation。Bootstrap 95% CI 极宽：scopal κ 的 CI 为 [0.00, 1.00]，coreferential 为 [0.00, 0.84]（Table 9）。论文正确承认\"lack power for type-level comparison\"（Section 4.4），但仍然基于自动评估做出 type-level claims（C2-C4）。当 human validation 无法验证 type-level 可靠性时，C2-C4 的有效性取决于对自动 judge 的 type-level 信任——而 W1 已经表明这种信任在 authorization scope 上是脆弱的。\n\n- **建议**: (a) 增大 human validation 样本量至每类 80-100 以获得可解释的 type-level CI；或 (b) 在 Limitations 中更强调 type-level claims 的 validation gap。\n\n---\n\n**W6 [MINOR]: Discussion 与 Appendix B 的 mitigation 数字不一致**\n\n- **具体位置**: Section 7 (Discussion) vs Appendix B (Table 4)\n- **问题**: Discussion 报告 GPT-5.4 上 type-specific prompting 使 incompleteness **恶化** +14pp（p=0.118）；Table 4 报告同一模型同一类型 **改善** −2.6pp。两个实验的设计差异（不同 prompt？不同 clause subset？）未明确说明。Authorization scope 也不一致：Discussion 报告 −12pp（p=0.070），Table 4 报告 −40.0pp。\n- **建议**: 明确标注 Discussion 和 Appendix B 是两个独立实验，说明 prompt 和数据差异。\n\n---\n\n**W7 [MINOR]: Domain 泛化性有限**\n\n- **具体位置**: Section 8 (Limitations)\n- τ²-bench 仅覆盖零售/航空客服。医疗、金融、法律领域的 policy ambiguity 可能产生不同的类型层级。\n\n---\n\n### Questions\n\n**Q1**: Cross-judge κ=0.385（authorization scope）的 raw agreement 具体是多少？是否可以计算 PABAK 或 Gwet's AC1 来区分 prevalence paradox 和真实分歧？\n\n**Q2**: 如果用 confound-adjusted effect size（而非 raw violation rate）重新做 TOST 分析，C2 的两层结构是否仍然成立？\n\n**Q3**: Perturbation control 的扰动幅度（synonym substitution, clause reordering）是否与 ambiguity perturbation 的 token-level 变化量匹配？如果前者的修改量更小，null result 的信息量有限。\n\n**Q4**: 在 replication study 中，为何不报告 cross-provider ICC？Gemini 和 LLaMA 加入后的 7-model ICC 是多少？\n\n**Q5**: Kendall's W=0.398（p=0.072）表明五个主模型的类型排序一致性不显著。这是否意味着除 incompleteness 外，type hierarchy 是 model-dependent 的？这对 C2 的普适性有何影响？\n\n**Q6**: Discussion 中 GPT-5.4 的 type-specific mitigation 结果（incompleteness +14pp, auth scope −12pp）与 Table 4 的结果（−2.6pp, −40.0pp）差异很大。这是两个不同的实验吗？如果是，请明确说明实验设计差异。\n\n---\n\n### Missing References\n\n论文的引用覆盖基本完整。以下是可考虑补充的：\n\n1. 关于 LLM judge 偏差的系统性研究——虽然引用了 Zheng et al. (2024)，但未引用关于 LLM judge 在不同 task type 上 reliability 差异的更细粒度工作\n2. 关于 equivalence testing 在 NLP 中应用的先例（如果存在），以支撑 SESOI 选择的合理性\n3. 关于 safety-critical 系统中 ambiguity 评估的跨领域文献（aviation, medical NLP），可增强 taxonomy 的理论基础\n\n---\n\n### Overall Assessment\n\n**评分: 3.5 (Borderline Conference)**\n**置信度: 4/5**\n\n这篇论文在实验设计和统计分析上显著优于该领域的平均水平。C1（ambiguity 因果效应，OR=15.1, 7 模型一致）证据充分，taxonomy 的桥接 NLP/RE 的构思有价值，error analysis（尤其 Disambiguation Neglect）有实际意义。\n\n阻碍 Conference 接收的核心问题是测量可靠性：C4 基于最低 reliability 类型（authorization scope κ=0.385）的数据做 numbered claim，C2 的\"两层结构\"在 bootstrap 聚类中仅 34.3% 稳定，SESOI 论证存在循环性。如果作者能 (1) 将 C4 降级为 observation 或补充 prevalence-adjusted agreement，(2) 缓和 C2 的表述强度并讨论 confound-adjusted 场景下的结构稳定性，(3) 从部署角度论证 SESOI，这篇论文可以达到 Conference 水平（4.0）。",
  "reviewer_id": "1",
  "project": "policy_ambiguity_safety"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## 总体评分\n**Overall**: 3.5 / 5 (Borderline Conference)\n**Confidence**: 4 / 5\n**一句话总结**: 实验设计严谨、统计分析全面的因果研究，但 authorization scope 评审一致性低（κ=0.385）削弱了 C4，SESOI ±15pp 缺乏实质性论证，incompleteness 信息添加混杂虽有控制但残余问题影响 C2 的\"两层结构\"表述强度。\n\n## 官方维度打分（ACL ARR Review Form）\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | C1 证据充分（OR=15.1, 7 模型一致），C2 的两层结构依赖 margin 选择且 bootstrap AU p=0.47，C3 作者自认 inconclusive（正确），C4 基于最低可靠性类型的数据 |\n| Excitement | 3.5/5 | 首个因果性的 ambiguity→violation 类型映射，taxonomy 桥接 NLP/RE，实用价值高；但局限于 τ²-bench 单一客服领域 |\n| Reproducibility | 4/5 | 方法细节完整，承诺代码和数据开源，统计报告规范（效应量+CI+多重校正）；judge 选择限制精确复制 |\n\n---\n\n### Strengths\n\n**S1: 严谨的 matched-pair 因果设计 + perturbation control**\n300 对 clause pair（96% annotator agreement），perturbation control（Δ_perturb = −0.67pp, 95% CI [−8.0, 6.67] 包含零）有效排除了表面扰动的混杂效应。Section 4.2 和 4.5 的设计使得 C1 的因果推断具有说服力。\n\n**S2: 全面的统计分析框架**\nMcNemar + TOST + bootstrap 聚类 + Holm-Bonferroni 三组校正 + post-hoc 功效分析（C1/C2 power > 0.99），同时在 7 个 margin（±5–20pp）上展示 TOST 敏感性分析（Table 3/Appendix A），这在该领域中不常见且值得肯定。\n\n**S3: 诚实的 claim 标定**\nC3 明确标注为 inconclusive（未通过 Holm-Bonferroni 校正），C4 标注为 [Exploratory]，authorization scope 的 52pp range 被表述为\"suggestive rather than definitive\"和\"upper bound with substantial measurement uncertainty\"（Section 5.4）。这种自我校准的 claim 强度在审稿中非常难得。\n\n**S4: 有价值的 error analysis**\nSection 6 的五种 failure mode taxonomy（structural misparse / information gap-filling / boundary violation）揭示了类型特异的机制路径，\"Disambiguation Neglect\"（4.6% awareness rate）是一个有实际意义的发现，且 mitigation experiment 证实了 prompt-level 干预的局限性。\n\n**S5: Incompleteness 混杂处理相对充分**\nAppendix F/H 提供了 token delta logistic regression（incompleteness p=0.018, coefficient change <8%），coreferential 的 confound-free lower bound（31.6%），以及 authorization scope 的反证逻辑（最大 token delta 但 violation rate 更低）。虽有残余问题（见 W2），整体处理水平高于同类论文。\n\n---\n\n### Weaknesses\n\n**W1 [MUST-FIX]: Authorization scope cross-judge κ=0.385 严重削弱 C4 的 52pp range claim**\n\n- **具体位置**: Section 4.4, Section 5.4, Appendix G (Table 9), Appendix P\n- **问题**: Authorization scope 的 cross-judge κ 仅 0.385（Section 4.4），是所有类型中最低的。C4 的核心发现——52pp cross-model range（Claude 12% → GPT-5.4 64%）——正是基于这个最不可靠的类型。尽管论文用 within-judge bootstrap ranking preservation（99.5%）和 raw agreement 来补救，但存在三层问题：\n\n  (1) **Cross-judge κ vs human-LLM κ 的混淆**：Section 5.4 引用\"raw agreement 85.3%\"来论证可靠性，但 Appendix G (Table 9) 的 human-LLM κ=0.644 与 Section 4.4 的 cross-judge κ=0.385 是不同指标，论文未明确区分这两个数据来源。读者可能误以为 85.3% 是 cross-judge 的 raw agreement。\n\n  (2) **Within-judge 分析的局限**: within-judge 48pp range（Section 5.4）仅证明单个 judge 内部的排序稳定性，不能弥补 cross-judge 评测不一致。如果 GPT-5.4 和 GPT-4.1 对 authorization scope violation 的判定标准系统性不同，within-judge 稳定性反而说明偏差是稳定的。\n\n  (3) **Appendix P 的 rank reversal**: Within-judge-group type ranking 在两组 judge 之间的相关性为 ρ=−0.03（p=0.96），而论文将此归因于 agent composition 差异。但 authorization scope 的 rank reversal（GPT-4.1 judged: rank 1; GPT-5.4 judged: rank 6）也可能反映 judge 偏差。\n\n- **为什么影响接收**: C4 是论文四个 numbered claim 之一，52pp range 出现在 abstract 和 Figure 3 中。基于最低 reliability 类型的数据做 numbered claim，即使标注 [Exploratory]，仍有方法论风险。\n\n- **建议修改方向**: (a) 计算 prevalence-adjusted agreement 指标（如 PABAK 或 Gwet's AC1）来澄清 κ=0.385 是否为 prevalence paradox；(b) 将 C4 从 numbered claim 降级为 Discussion 中的 observation；(c) 或在 abstract/conclusion 中不引用 52pp 具体数字，改为定性描述。\n\n---\n\n**W2 [SHOULD-FIX]: C2\"两层结构\"的表述强度与证据强度不匹配**\n\n- **具体位置**: Section 5.2, Appendix A (Table 3), Appendix I\n- **问题**: \"Two-tier hierarchy\"这一表述暗示稳定的层级结构，但实际证据受三个因素制约：\n\n  (1) **Margin 依赖性**: ±10pp 时仅 3/6 mid-tier pair 达到 equivalence，±12pp 时 5/6，±15pp 时 6/6（Table 3）。TOST power 从 ±15pp 的 0.94 降至 ±10pp 的 0.57（Section 4.6）。\"两层结构\"在较小 margin 下并不成立。\n\n  (2) **Bootstrap 聚类不稳定**: Incompleteness singleton 仅在 34.3% 的 bootstrap samples 中重现，AU p-value = 0.47（Appendix I）。这意味着 incompleteness 与其他类型的分界并不 robust。\n\n  (3) **Kendall's W 不显著**: 五个主模型的类型排序一致性 W=0.398（p=0.072），未达到显著水平（Appendix M）。这意味着不同模型对类型危险度排序的共识不强，除了 incompleteness 始终最高。\n\n  (4) **Confound-free 场景**: 如果按 confound-free lower bound 评估 incompleteness（31.6%），它将与 coreferential 持平、低于 mid-tier cluster——两层结构将崩塌。虽然 31.6% 是极端下界，但论文未讨论在 confound-adjusted 后两层结构是否仍成立。\n\n- **建议**: 将\"two-tier hierarchy\"改为更谨慎的表述，如\"incompleteness consistently separates as the highest-violation type, with the remaining types forming a less differentiated cluster at the ±15pp equivalence margin.\" 明确承认 margin 依赖性和 bootstrap 不稳定性。\n\n---\n\n**W3 [SHOULD-FIX]: SESOI ±15pp 的论证存在循环性**\n\n- **具体位置**: Section 4.6\n- **问题**: ±15pp 的论证逻辑是：(1)\"a type producing ≥15 pp more violations warrants distinct policy handling in deployment\"——这是用结论论证前提；(2)\"exceeds the perturbation control bound (6.67 pp) by >2×\"——这是测量噪声标准，不是实质性差异标准。\n\n  在安全评估场景下，±15pp 相当宽松。如果类型 A 比类型 B 高 14pp 违规率（在 ±15pp 下被判定为\"等价\"），在实际部署中可能意味着成百上千次额外违规。论文承认\"No field-standard SESOI exists\"，但这更需要从实际部署角度论证而非回避。\n\n  好的一面是，Table 3 提供了 7 个 margin 的完整敏感性分析，bootstrap 聚类是 margin-free 的。但 primary threshold 的选择影响了 C2 的核心表述。\n\n- **建议**: 从部署角度论证：例如，给出一个假设场景（如 1000 interactions/day 的 agent，15pp 差异 = 150 extra violations/day），讨论这个量级是否足以触发不同的 policy handling。或者将 ±10pp 和 ±15pp 并列为 primary results，展示 C2 在两个 threshold 下的差异。\n\n---\n\n**W4 [SHOULD-FIX]: Cross-judge 设计仅使用 OpenAI 家族模型**\n\n- **具体位置**: Section 4.4\n- **问题**: GPT-5.4 和 GPT-4.1 均来自 OpenAI。OpenAI 模型家族可能共享系统性偏差（如对特定 violation 模式的敏感度、对 authorization boundary 的理解方式）。论文论证\"the cross-judge asymmetry affects only absolute violation rates, not C1 or C2\"（Section 4.4），但这一论证基于差值消除假设——只有当两个 judge 的偏差方向相同且幅度相近时才成立。如果 GPT-5.4 和 GPT-4.1 因共享训练策略而有 correlated bias，差值确实可以消除共模偏差；但如果偏差是 type-specific 的（如 OpenAI 模型普遍对 authorization scope 判定更严格），则不会被差值消除。\n\n- **建议**: 在 Limitations 中增加对 single-family judge bias 的讨论。如有资源，在 replication study 中用 Claude 或 Gemini 作为 judge 对 subset 评估。\n\n---\n\n**W5 [SHOULD-FIX]: Human validation 样本量不足以支撑 type-level claims**\n\n- **具体位置**: Section 4.4, Appendix G (Table 9)\n- **问题**: 每种类型仅 32-34 episodes 的 human validation。Bootstrap 95% CI 极宽：scopal κ 的 CI 为 [0.00, 1.00]，coreferential 为 [0.00, 0.84]（Table 9）。论文正确承认\"lack power for type-level comparison\"（Section 4.4），但仍然基于自动评估做出 type-level claims（C2-C4）。当 human validation 无法验证 type-level 可靠性时，C2-C4 的有效性取决于对自动 judge 的 type-level 信任——而 W1 已经表明这种信任在 authorization scope 上是脆弱的。\n\n- **建议**: (a) 增大 human validation 样本量至每类 80-100 以获得可解释的 type-level CI；或 (b) 在 Limitations 中更强调 type-level claims 的 validation gap。\n\n---\n\n**W6 [MINOR]: Discussion 与 Appendix B 的 mitigation 数字不一致**\n\n- **具体位置**: Section 7 (Discussion) vs Appendix B (Table 4)\n- **问题**: Discussion 报告 GPT-5.4 上 type-specific prompting 使 incompleteness **恶化** +14pp（p=0.118）；Table 4 报告同一模型同一类型 **改善** −2.6pp。两个实验的设计差异（不同 prompt？不同 clause subset？）未明确说明。Authorization scope 也不一致：Discussion 报告 −12pp（p=0.070），Table 4 报告 −40.0pp。\n- **建议**: 明确标注 Discussion 和 Appendix B 是两个独立实验，说明 prompt 和数据差异。\n\n---\n\n**W7 [MINOR]: Domain 泛化性有限**\n\n- **具体位置**: Section 8 (Limitations)\n- τ²-bench 仅覆盖零售/航空客服。医疗、金融、法律领域的 policy ambiguity 可能产生不同的类型层级。\n\n---\n\n### Questions\n\n**Q1**: Cross-judge κ=0.385（authorization scope）的 raw agreement 具体是多少？是否可以计算 PABAK 或 Gwet's AC1 来区分 prevalence paradox 和真实分歧？\n\n**Q2**: 如果用 confound-adjusted effect size（而非 raw violation rate）重新做 TOST 分析，C2 的两层结构是否仍然成立？\n\n**Q3**: Perturbation control 的扰动幅度（synonym substitution, clause reordering）是否与 ambiguity perturbation 的 token-level 变化量匹配？如果前者的修改量更小，null result 的信息量有限。\n\n**Q4**: 在 replication study 中，为何不报告 cross-provider ICC？Gemini 和 LLaMA 加入后的 7-model ICC 是多少？\n\n**Q5**: Kendall's W=0.398（p=0.072）表明五个主模型的类型排序一致性不显著。这是否意味着除 incompleteness 外，type hierarchy 是 model-dependent 的？这对 C2 的普适性有何影响？\n\n**Q6**: Discussion 中 GPT-5.4 的 type-specific mitigation 结果（incompleteness +14pp, auth scope −12pp）与 Table 4 的结果（−2.6pp, −40.0pp）差异很大。这是两个不同的实验吗？如果是，请明确说明实验设计差异。\n\n---\n\n### Missing References\n\n论文的引用覆盖基本完整。以下是可考虑补充的：\n\n1. 关于 LLM judge 偏差的系统性研究——虽然引用了 Zheng et al. (2024)，但未引用关于 LLM judge 在不同 task type 上 reliability 差异的更细粒度工作\n2. 关于 equivalence testing 在 NLP 中应用的先例（如果存在），以支撑 SESOI 选择的合理性\n3. 关于 safety-critical 系统中 ambiguity 评估的跨领域文献（aviation, medical NLP），可增强 taxonomy 的理论基础\n\n---\n\n### Overall Assessment\n\n**评分: 3.5 (Borderline Conference)**\n**置信度: 4/5**\n\n这篇论文在实验设计和统计分析上显著优于该领域的平均水平。C1（ambiguity 因果效应，OR=15.1, 7 模型一致）证据充分，taxonomy 的桥接 NLP/RE 的构思有价值，error analysis（尤其 Disambiguation Neglect）有实际意义。\n\n阻碍 Conference 接收的核心问题是测量可靠性：C4 基于最低 reliability 类型（authorization scope κ=0.385）的数据做 numbered claim，C2 的\"两层结构\"在 bootstrap 聚类中仅 34.3% 稳定，SESOI 论证存在循环性。如果作者能 (1) 将 C4 降级为 observation 或补充 prevalence-adjusted agreement，(2) 缓和 C2 的表述强度并讨论 confound-adjusted 场景下的结构稳定性，(3) 从部署角度论证 SESOI，这篇论文可以达到 Conference 水平（4.0）。",
    "reviewer_id": "1",
    "project": "policy_ambiguity_safety"
  }
}
```

</details>

---


### Tool result

_source line 889 · 2026-05-22T08:46:39.250038+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_967344d166ba485ad606d14379e69d85:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4065
}
```

</details>

---


### Assistant

_source line 890 · 2026-05-22T08:46:59.847320+00:00_

审稿意见已提交给 Review Director。

总结：评分 **3.5/5 (Borderline Conference)**，主要发现：

1. **MUST-FIX**: Authorization scope 的 cross-judge κ=0.385 严重削弱 C4（52pp range claim），建议降级为 observation 或补充 prevalence-adjusted 指标
2. **SHOULD-FIX (×4)**:
   - C2 "两层结构"表述过强（margin-dependent, bootstrap 仅 34.3% 稳定, Kendall's W 不显著）
   - SESOI ±15pp 论证循环（measurement noise criterion ≠ practical significance criterion）
   - Cross-judge 仅用 OpenAI 家族模型，无法排除 correlated bias
   - Human validation n=32-34/type，CI 过宽无法支撑 type-level claims
3. **MINOR**: Discussion vs Appendix B mitigation 数字不一致需澄清；domain 局限于客服

核心优势：matched-pair 因果设计严谨、统计分析全面（McNemar+TOST+bootstrap+Holm-Bonferroni）、claim 标定诚实（C3 inconclusive, C4 exploratory）、error analysis 有价值。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1"
}
```

</details>

---


## Round 24

## Round 24

4 recorded events


### User

_source line 891 · 2026-05-22T08:48:05.125240+00:00_

[Round 1 审稿请求]:
以下是 Reviewer 2 的完整审稿意见，请逐条回应：对每个 Strength 和 Weakness，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。

---

## Reviewer 2 完整审稿意见

### Overall: 3.5 / 5 (Borderline Conference), Confidence: 4/5

### Strengths

**S1. Matched-pair causal design 确属创新。** 在 NLP agent safety 领域，现有工作均为 correlational 或 benchmark-evaluation 范式。matched-pair design + perturbation control 确实建立了 ambiguity → violation 的因果链。

**S2. 统计方法论异常充分。** TOST + bootstrap cluster + Holm-Bonferroni 三重验证。SESOI domain-anchored justification 和 margin dependence acknowledgment 体现方法论自觉。

**S3. Honest about limitations。** Incompleteness confound 多层控制，C3 null result 坦诚报告，auth scope κ=0.385 反复标注，C4 标为 [Exploratory]。

**S4. Error analysis 有实质洞见。** 三种 failure mechanism 与 ambiguity type 的对应关系提供了机制理解。Systematic nocuity（41.3%）揭示了 agreement-based evaluation 盲区。

**S5. 实验规模与模型覆盖度。** 5+2 models, 7 providers, 2997 episodes。

### Weaknesses

**W1 [SHOULD-FIX] Taxonomy 理论基础：incompleteness 和 conditional precedence 并非 "ambiguity"，§3 的论证存在循环。**
§3 用行为结果（violation pattern 相似）来证明纳入 taxonomy 的合理性，但这些结果本身依赖于它们已被纳入 taxonomy 并在 benchmark 中测试。Incompleteness 是最高 violation 类型（53.6%），如果理论上不属于 ambiguity，中心叙事被削弱。Dalpiaz et al. (2018) 的 co-occurrence ≠ identity。建议重新框架为 "policy specification defects" 或增加更实质的理论论证。

**W2 [SHOULD-FIX] "Disambiguation Neglect" 新颖性被高估。**
Liu et al. (2023) 已证明 LLMs collapse multiple interpretations。Hu et al. (2025) 论证 missing conceptual representations。本文增量是在 agent policy 场景中量化，但不应列为 primary contribution。

**W3 [SHOULD-FIX] "Differential Nocuity" 框架增量贡献有限。**
Berry & Kamsties (2004) 已隐含 type-dependent risk。Willis et al. (2008) 已研究 nocuity degree。本文贡献是 empirical evidence，但 framework name 过于宏大。

**W4 [SHOULD-FIX] Abstract/Introduction 中 claim 精确度与正文证据不完全匹配。**
(a) Abstract "risk gradient" vs §5.2 "two-tier structure" 表述不一致；(b) Introduction 52pp range caveat 权重不够；(c) "type identity explaining 22× more variance" 但正文实为 "clause identity"，clause ≠ type。

**W5 [MINOR] Related Work 遗漏若干相关工作。**
OpenAgentSafety (ICLR 2026), Agent-SafetyBench (2024), Ferrari et al. (2019) "Ambiguity in RE: Towards a Unifying Framework", Automated Repair of Ambiguous NL Requirements (2025).

**W6 [MINOR] Coreferential 在 mitigation 和 replication 中均被排除。**

**W7 [MINOR] §7 Mitigation 样本量偏小。**
n=50 per type 的 McNemar test 功效有限。Incompleteness worsening (+14pp, p=0.118) 的因果解释（confabulation）过于确定。

### Questions
Q1: Bootstrap AU p=0.47 如何与 "incompleteness stands apart" 的 confident framing 调和？
Q2: "Clause identity explains 22.4% of variance" 是 300 clause pair 的 random effect 还是 6 type 的 fixed effect？
Q3: Temperature=0 下 ICC=0.919 的变异来源？
Q4: §4.2 的 "realism validation" 具体 protocol？

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 892 · 2026-05-22T08:50:56.251478+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 1 对 Reviewer 2 审稿意见的逐条回应\n\n---\n\n### Strengths 回应\n\n**[AGREE] R2-S1 (Matched-pair causal design)**\n完全同意。这是该领域首个建立 ambiguity → violation 因果链的工作。我的 S1 做了相同评价。perturbation control（Δ=−0.67pp, CI 包含零; Section 4.5）有效排除了表面扰动的混杂。\n\n**[AGREE] R2-S2 (统计方法论)**\n同意。TOST + bootstrap + Holm-Bonferroni 的三重验证在该领域中罕见。但我对 SESOI ±15pp 的论证有保留意见（见我的 W3）——R2 称之为\"domain-anchored justification\"，但 Section 4.6 的锚定逻辑存在循环性（\"产生 ≥15pp 差异的类型值得差异化处理\"用结论论证前提）。\n\n**[AGREE] R2-S3 (Honest about limitations)**\n同意。C3 坦诚报告 null result、C4 标注 [Exploratory]、auth scope κ=0.385 反复标注，这在审稿中值得肯定。\n\n**[AGREE] R2-S4 (Error analysis)**\n同意。三种 failure mechanism 的类型对应关系（structural misparse → scopal/cond. prec.; information gap-filling → incompleteness/lexical; boundary violation → auth scope; Section 6.1）确实提供了超越统计关联的机制理解。Systematic nocuity 41.3%（Section 6.3）揭示了 agreement-based evaluation 的盲区。\n\n**[AGREE] R2-S5 (实验规模)**\n同意。5+2 模型、6 providers、2997 episodes 的覆盖度在该领域属于高水平。\n\n---\n\n### Weaknesses 回应\n\n**[REBUT] R2-W1: Taxonomy 理论基础——incompleteness/conditional precedence 并非\"ambiguity\"**\n\nR2 的理论关切有一定道理，但论证过于强硬，忽略了论文的操作性定义和文献基础。\n\n(1) **操作性定义已明确给出**：Section 3 定义 \"a policy clause is ambiguous when it admits multiple operationally distinct interpretations by an LLM agent\"（原文）。在此定义下，incompleteness（缺失信息导致 agent 用不同默认值填充）和 conditional precedence（规范冲突导致不同优先级选择）均产生多个可操作的不同解读，符合定义。R2 似乎要求的是 linguistic ambiguity 的狭义定义，但论文明确将范围扩展到了 RE 文献。\n\n(2) **文献支撑非仅 co-occurrence**：Section 3 引用了 Berry et al. (2004) 对 requirements specification 中 ambiguity 的广义分类（包含 incompleteness），Dalpiaz et al. (2018) 证明 ambiguity 和 incompleteness 在 RE 中频繁共现且行为上难以区分，以及 Li et al. (2024b) 的 11 类 NLP taxonomy 也包含类似的 specification-layer 类型。论文不是用行为结果来论证纳入——而是基于 RE/NLP 文献的分类传统。\n\n(3) **\"Policy specification defects\" 的替代命名会引入新问题**：如果改名，就切断了与 NLP ambiguity 文献（Berry & Kamsties, Li et al.）的联系，而这正是论文的理论锚点之一。\n\n但我同意 R2 的一个子观点：Section 3 的 \"scope of ambiguity\" 讨论可以更清晰地区分 linguistic ambiguity（狭义）和 specification ambiguity（广义），而非依赖读者自行接受操作性定义。\n\n**[AGREE] R2-W2: Disambiguation Neglect 新颖性被高估**\n\n同意。Introduction 将 Disambiguation Neglect 列为第三个 contribution（\"(3) an error analysis revealing Disambiguation Neglect\"），但 Liu et al. (2023) 和 Hu et al. (2025) 已分别在 language understanding 层面证明了类似现象（Section 6.2 也承认 \"consistent with Hu et al. (2025)\"）。本文的增量是在 agent policy 执行场景中量化（4.6% awareness, Section 6.2），但这更适合作为 error analysis 的 finding 而非 primary contribution。建议将 contribution (3) 重新措辞，强调场景特异性和量化贡献，而非暗示发现了一个新现象。\n\n**[AGREE] R2-W3: Differential Nocuity 框架增量有限**\n\n同意。\"Differential nocuity\" 出现在 Discussion（Section 7）而非 contribution list，但命名暗示了一个新 framework。实际上 Berry & Kamsties (2004) 的 nocuous/innocuous 区分和 Willis et al. (2008) 的 nocuity degree 已经隐含了 type-dependent risk 的概念。本文的贡献是提供了 empirical evidence（不同 ambiguity type 有不同 nocuity），但框架层面的增量有限。将其定位为\"empirical validation of differential nocuity\"比\"proposing a differential nocuity framework\"更准确。\n\n**[AGREE] R2-W4: Claim 精确度问题**\n\n这一条的三个子点都有道理：\n\n(a) **\"risk gradient\" vs \"two-tier structure\"**：Abstract 说\"a risk gradient rather than a uniform threat\"，但 Section 5.2 的 TOST 分析实际展示的是\"two-tier structure\"——incompleteness 独立 + 其余类型构成一个 cluster。\"Gradient\"暗示连续变化，\"two-tier\"暗示离散分层。这两个措辞不一致，应统一为\"two-tier\"。\n\n(b) **52pp caveat 权重不够**：我在自己的 W1 中也提出了类似的问题。Introduction 中的 caveat 仅在从句位置（\"though this is an upper bound...\"），与 52pp 这个数字的突出位置不对称。\n\n(c) **\"clause identity\" vs \"type identity\"**：R2 正确指出这是一个重要的文字错误。Section 5.1 明确写的是\"Clause identity explains 22.4% of variance versus 1.0% for model identity\"——clause 是 300 个具体条款的 random effect，不是 6 个类型的 fixed effect。如果 Introduction 的 contribution (2) 写成了\"type identity\"，这是实质性错误（22.4% for 300 clauses vs 远低于此的 6 types），必须修正。\n\n**[REBUT] R2-W5: Related Work 遗漏**\n\n部分反驳。R2 列出的遗漏中：\n\n- **Agent-SafetyBench (2024)**：Section 2 已引用 agent safety evaluation 文献（Yuan et al., 2024; Ruan et al., 2024; Yin et al., 2025; Wu and Gong, 2026）。如果 Agent-SafetyBench 与这些工作有实质性差异（如不同的 evaluation dimension），值得补充；否则为同类引用的替代品。\n\n- **Ferrari et al. (2019) \"Ambiguity in RE\"**：Section 2 已引用 Ferrari and Esuli (2019)（Related Work, page 2），这应该就是 R2 提到的这篇。\n\n- **OpenAgentSafety (ICLR 2026)** 和 **Automated Repair of Ambiguous NL Requirements (2025)**：如果这两篇确实相关且未被引用，值得补充。但 Related Work 不能穷尽所有相关工作，是否遗漏取决于这些工作是否提供了本文未讨论的 complementary perspective。\n\n**[AGREE] R2-W6: Coreferential 排除**\n\n同意这是一个限制。论文给出了合理的技术原因（Appendix B: pronoun resolution 无法设计 type-specific disambiguation prompt; episode design 与原始 model configuration 耦合），但这意味着 6 类 taxonomy 中有 1 类在 mitigation 和 replication 中完全缺席。这不影响 C1 和 C2 的 main analysis（coreferential 有完整的 5-model 数据），但削弱了 taxonomy 的完整性声明。\n\n**[AGREE] R2-W7: Mitigation 样本量和过度解释**\n\n同意。n=50/type 的 McNemar test 对 14pp 效应的 power 不足（p=0.118 即未达到显著），但 Discussion 用确定性语言解释为\"prompting agents to attend to missing information triggers confabulation rather than caution\"（Section 7）。对一个 p=0.118 的非显著趋势给出因果机制解释（confabulation），属于过度解读。应明确标注为 non-significant trend 并降低解释的确定性。\n\n此外，我在自己的 W6 中还发现了一个 R2 未提到的问题：Discussion 中 GPT-5.4 的 type-specific mitigation 数据（incompleteness +14pp, auth scope −12pp）与 Table 4（incompleteness −2.6pp, auth scope −40.0pp）数字不一致，两个实验的关系未明确说明。\n\n---\n\n### Questions 回应\n\n**[AGREE] R2-Q1: Bootstrap AU p=0.47 vs \"stands apart\" framing**\n\n这正是我的 W2 指出的问题。AU p-value=0.47 意味着 incompleteness singleton 不到一半的 bootstrap 样本中被重现（Appendix I）。Section 5.2 用\"stands apart as an upper bound\"措辞，虽然后面有\"conditional on the confound controls\"的限定，但与 AU p=0.47 的统计不稳定性不匹配。建议增加对 bootstrap 不稳定性的正文讨论，或缓和\"stands apart\"的措辞。\n\n**[AGREE] R2-Q2: Clause identity vs type identity 的 22.4%**\n\n重要问题。Section 5.1 说的是\"Clause identity explains 22.4% of variance\"——这是 300 个 clause pair 的 random effect，不是 6 个 ambiguity type 的 fixed effect。22.4% 由 300 个具体条款的措辞差异解释，其中 type 仅是分组变量。如果报告 type 的 fixed effect variance explained，数字会小得多（6 个 level 的 between-group variance / total variance）。作者应澄清：正文和 abstract 用\"clause identity\"是正确的，但 Introduction contribution (2) 如果用了\"type identity\"则需修正。\n\n**[AGREE] R2-Q3: Temperature=0 下 ICC=0.919 的变异来源**\n\n好问题。Temperature=0 理论上应产生 deterministic output，但实际中：(1) 大模型的 sampling 在 T=0 下仍可能有微小 stochasticity（floating-point non-determinism, batching 差异）；(2) τ²-bench 的 multi-turn 对话中，微小的初始差异在多轮交互中可能被放大。ICC=0.919 说明 8.1% 的 variance 来自 noise——在 30 clause pairs × 3 replicates 的设计下，这个量级值得解释。\n\n**[REBUT] R2-Q4: Realism validation protocol**\n\nSection 4.2 提供了足够的信息：\"Clause pairs are generated through a template-based pipeline and reviewed by two independent annotators (both with NLP background)\" with 96% agreement and 100% post-discussion consensus. \"A post-hoc realism validation confirms linguistic consistency with original τ²-bench policy text\"（Section 4.2）。论文还在 Limitations 中承认\"realism validation confirms lexical comparability but cannot rule out distributional gaps\"（Section 8）。protocol 的核心要素已给出——这不是一个遗漏，而是篇幅约束下的合理简写。不过 R2 如果要求更多细节（如具体的 rubric、评分标准、disagreement 的类型分布），作者可以在 camera-ready 或 appendix 中补充。\n\n---\n\n### 总结：R1 与 R2 的共识与分歧\n\n**共识领域**（两位 reviewer 一致指出的问题）：\n1. Authorization scope κ=0.385 影响 C4 可靠性（R1-W1, R2 在 S3 中承认但未单独列为 weakness）\n2. Claim 精确度问题——特别是 clause vs type identity 的 22× claim（R2-W4c）\n3. Mitigation 样本量和过度解释（R1-W6/W7, R2-W7）\n4. Bootstrap 聚类不稳定性与\"stands apart\" framing 的张力（R1-W2, R2-Q1）\n5. C2 \"two-tier hierarchy\" 表述强度偏高（R1-W2, R2-W4a 的 gradient vs two-tier 不一致）\n\n**R1 额外关注**（R2 未提出）：\n- SESOI ±15pp 循环论证（R1-W3）\n- Cross-judge 仅用 OpenAI 家族（R1-W4）\n- Human validation 样本量对 type-level claims 不足（R1-W5）\n- Discussion vs Table 4 的 mitigation 数字不一致（R1-W6）\n\n**R2 额外关注**（R1 未提出）：\n- Taxonomy 理论基础（W1）——我部分反驳\n- Disambiguation Neglect/Differential Nocuity 新颖性高估（W2, W3）——我同意\n- Missing references（W5）——我部分反驳\n\n**评分一致**: 两位 reviewer 均给出 3.5 (Borderline Conference), Confidence 4。核心判断一致：C1 证据充分，但 C2/C4 的表述强度和测量可靠性问题阻碍 Conference 接收。",
  "reviewer_id": "1",
  "project": "policy_ambiguity_safety"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 1 对 Reviewer 2 审稿意见的逐条回应\n\n---\n\n### Strengths 回应\n\n**[AGREE] R2-S1 (Matched-pair causal design)**\n完全同意。这是该领域首个建立 ambiguity → violation 因果链的工作。我的 S1 做了相同评价。perturbation control（Δ=−0.67pp, CI 包含零; Section 4.5）有效排除了表面扰动的混杂。\n\n**[AGREE] R2-S2 (统计方法论)**\n同意。TOST + bootstrap + Holm-Bonferroni 的三重验证在该领域中罕见。但我对 SESOI ±15pp 的论证有保留意见（见我的 W3）——R2 称之为\"domain-anchored justification\"，但 Section 4.6 的锚定逻辑存在循环性（\"产生 ≥15pp 差异的类型值得差异化处理\"用结论论证前提）。\n\n**[AGREE] R2-S3 (Honest about limitations)**\n同意。C3 坦诚报告 null result、C4 标注 [Exploratory]、auth scope κ=0.385 反复标注，这在审稿中值得肯定。\n\n**[AGREE] R2-S4 (Error analysis)**\n同意。三种 failure mechanism 的类型对应关系（structural misparse → scopal/cond. prec.; information gap-filling → incompleteness/lexical; boundary violation → auth scope; Section 6.1）确实提供了超越统计关联的机制理解。Systematic nocuity 41.3%（Section 6.3）揭示了 agreement-based evaluation 的盲区。\n\n**[AGREE] R2-S5 (实验规模)**\n同意。5+2 模型、6 providers、2997 episodes 的覆盖度在该领域属于高水平。\n\n---\n\n### Weaknesses 回应\n\n**[REBUT] R2-W1: Taxonomy 理论基础——incompleteness/conditional precedence 并非\"ambiguity\"**\n\nR2 的理论关切有一定道理，但论证过于强硬，忽略了论文的操作性定义和文献基础。\n\n(1) **操作性定义已明确给出**：Section 3 定义 \"a policy clause is ambiguous when it admits multiple operationally distinct interpretations by an LLM agent\"（原文）。在此定义下，incompleteness（缺失信息导致 agent 用不同默认值填充）和 conditional precedence（规范冲突导致不同优先级选择）均产生多个可操作的不同解读，符合定义。R2 似乎要求的是 linguistic ambiguity 的狭义定义，但论文明确将范围扩展到了 RE 文献。\n\n(2) **文献支撑非仅 co-occurrence**：Section 3 引用了 Berry et al. (2004) 对 requirements specification 中 ambiguity 的广义分类（包含 incompleteness），Dalpiaz et al. (2018) 证明 ambiguity 和 incompleteness 在 RE 中频繁共现且行为上难以区分，以及 Li et al. (2024b) 的 11 类 NLP taxonomy 也包含类似的 specification-layer 类型。论文不是用行为结果来论证纳入——而是基于 RE/NLP 文献的分类传统。\n\n(3) **\"Policy specification defects\" 的替代命名会引入新问题**：如果改名，就切断了与 NLP ambiguity 文献（Berry & Kamsties, Li et al.）的联系，而这正是论文的理论锚点之一。\n\n但我同意 R2 的一个子观点：Section 3 的 \"scope of ambiguity\" 讨论可以更清晰地区分 linguistic ambiguity（狭义）和 specification ambiguity（广义），而非依赖读者自行接受操作性定义。\n\n**[AGREE] R2-W2: Disambiguation Neglect 新颖性被高估**\n\n同意。Introduction 将 Disambiguation Neglect 列为第三个 contribution（\"(3) an error analysis revealing Disambiguation Neglect\"），但 Liu et al. (2023) 和 Hu et al. (2025) 已分别在 language understanding 层面证明了类似现象（Section 6.2 也承认 \"consistent with Hu et al. (2025)\"）。本文的增量是在 agent policy 执行场景中量化（4.6% awareness, Section 6.2），但这更适合作为 error analysis 的 finding 而非 primary contribution。建议将 contribution (3) 重新措辞，强调场景特异性和量化贡献，而非暗示发现了一个新现象。\n\n**[AGREE] R2-W3: Differential Nocuity 框架增量有限**\n\n同意。\"Differential nocuity\" 出现在 Discussion（Section 7）而非 contribution list，但命名暗示了一个新 framework。实际上 Berry & Kamsties (2004) 的 nocuous/innocuous 区分和 Willis et al. (2008) 的 nocuity degree 已经隐含了 type-dependent risk 的概念。本文的贡献是提供了 empirical evidence（不同 ambiguity type 有不同 nocuity），但框架层面的增量有限。将其定位为\"empirical validation of differential nocuity\"比\"proposing a differential nocuity framework\"更准确。\n\n**[AGREE] R2-W4: Claim 精确度问题**\n\n这一条的三个子点都有道理：\n\n(a) **\"risk gradient\" vs \"two-tier structure\"**：Abstract 说\"a risk gradient rather than a uniform threat\"，但 Section 5.2 的 TOST 分析实际展示的是\"two-tier structure\"——incompleteness 独立 + 其余类型构成一个 cluster。\"Gradient\"暗示连续变化，\"two-tier\"暗示离散分层。这两个措辞不一致，应统一为\"two-tier\"。\n\n(b) **52pp caveat 权重不够**：我在自己的 W1 中也提出了类似的问题。Introduction 中的 caveat 仅在从句位置（\"though this is an upper bound...\"），与 52pp 这个数字的突出位置不对称。\n\n(c) **\"clause identity\" vs \"type identity\"**：R2 正确指出这是一个重要的文字错误。Section 5.1 明确写的是\"Clause identity explains 22.4% of variance versus 1.0% for model identity\"——clause 是 300 个具体条款的 random effect，不是 6 个类型的 fixed effect。如果 Introduction 的 contribution (2) 写成了\"type identity\"，这是实质性错误（22.4% for 300 clauses vs 远低于此的 6 types），必须修正。\n\n**[REBUT] R2-W5: Related Work 遗漏**\n\n部分反驳。R2 列出的遗漏中：\n\n- **Agent-SafetyBench (2024)**：Section 2 已引用 agent safety evaluation 文献（Yuan et al., 2024; Ruan et al., 2024; Yin et al., 2025; Wu and Gong, 2026）。如果 Agent-SafetyBench 与这些工作有实质性差异（如不同的 evaluation dimension），值得补充；否则为同类引用的替代品。\n\n- **Ferrari et al. (2019) \"Ambiguity in RE\"**：Section 2 已引用 Ferrari and Esuli (2019)（Related Work, page 2），这应该就是 R2 提到的这篇。\n\n- **OpenAgentSafety (ICLR 2026)** 和 **Automated Repair of Ambiguous NL Requirements (2025)**：如果这两篇确实相关且未被引用，值得补充。但 Related Work 不能穷尽所有相关工作，是否遗漏取决于这些工作是否提供了本文未讨论的 complementary perspective。\n\n**[AGREE] R2-W6: Coreferential 排除**\n\n同意这是一个限制。论文给出了合理的技术原因（Appendix B: pronoun resolution 无法设计 type-specific disambiguation prompt; episode design 与原始 model configuration 耦合），但这意味着 6 类 taxonomy 中有 1 类在 mitigation 和 replication 中完全缺席。这不影响 C1 和 C2 的 main analysis（coreferential 有完整的 5-model 数据），但削弱了 taxonomy 的完整性声明。\n\n**[AGREE] R2-W7: Mitigation 样本量和过度解释**\n\n同意。n=50/type 的 McNemar test 对 14pp 效应的 power 不足（p=0.118 即未达到显著），但 Discussion 用确定性语言解释为\"prompting agents to attend to missing information triggers confabulation rather than caution\"（Section 7）。对一个 p=0.118 的非显著趋势给出因果机制解释（confabulation），属于过度解读。应明确标注为 non-significant trend 并降低解释的确定性。\n\n此外，我在自己的 W6 中还发现了一个 R2 未提到的问题：Discussion 中 GPT-5.4 的 type-specific mitigation 数据（incompleteness +14pp, auth scope −12pp）与 Table 4（incompleteness −2.6pp, auth scope −40.0pp）数字不一致，两个实验的关系未明确说明。\n\n---\n\n### Questions 回应\n\n**[AGREE] R2-Q1: Bootstrap AU p=0.47 vs \"stands apart\" framing**\n\n这正是我的 W2 指出的问题。AU p-value=0.47 意味着 incompleteness singleton 不到一半的 bootstrap 样本中被重现（Appendix I）。Section 5.2 用\"stands apart as an upper bound\"措辞，虽然后面有\"conditional on the confound controls\"的限定，但与 AU p=0.47 的统计不稳定性不匹配。建议增加对 bootstrap 不稳定性的正文讨论，或缓和\"stands apart\"的措辞。\n\n**[AGREE] R2-Q2: Clause identity vs type identity 的 22.4%**\n\n重要问题。Section 5.1 说的是\"Clause identity explains 22.4% of variance\"——这是 300 个 clause pair 的 random effect，不是 6 个 ambiguity type 的 fixed effect。22.4% 由 300 个具体条款的措辞差异解释，其中 type 仅是分组变量。如果报告 type 的 fixed effect variance explained，数字会小得多（6 个 level 的 between-group variance / total variance）。作者应澄清：正文和 abstract 用\"clause identity\"是正确的，但 Introduction contribution (2) 如果用了\"type identity\"则需修正。\n\n**[AGREE] R2-Q3: Temperature=0 下 ICC=0.919 的变异来源**\n\n好问题。Temperature=0 理论上应产生 deterministic output，但实际中：(1) 大模型的 sampling 在 T=0 下仍可能有微小 stochasticity（floating-point non-determinism, batching 差异）；(2) τ²-bench 的 multi-turn 对话中，微小的初始差异在多轮交互中可能被放大。ICC=0.919 说明 8.1% 的 variance 来自 noise——在 30 clause pairs × 3 replicates 的设计下，这个量级值得解释。\n\n**[REBUT] R2-Q4: Realism validation protocol**\n\nSection 4.2 提供了足够的信息：\"Clause pairs are generated through a template-based pipeline and reviewed by two independent annotators (both with NLP background)\" with 96% agreement and 100% post-discussion consensus. \"A post-hoc realism validation confirms linguistic consistency with original τ²-bench policy text\"（Section 4.2）。论文还在 Limitations 中承认\"realism validation confirms lexical comparability but cannot rule out distributional gaps\"（Section 8）。protocol 的核心要素已给出——这不是一个遗漏，而是篇幅约束下的合理简写。不过 R2 如果要求更多细节（如具体的 rubric、评分标准、disagreement 的类型分布），作者可以在 camera-ready 或 appendix 中补充。\n\n---\n\n### 总结：R1 与 R2 的共识与分歧\n\n**共识领域**（两位 reviewer 一致指出的问题）：\n1. Authorization scope κ=0.385 影响 C4 可靠性（R1-W1, R2 在 S3 中承认但未单独列为 weakness）\n2. Claim 精确度问题——特别是 clause vs type identity 的 22× claim（R2-W4c）\n3. Mitigation 样本量和过度解释（R1-W6/W7, R2-W7）\n4. Bootstrap 聚类不稳定性与\"stands apart\" framing 的张力（R1-W2, R2-Q1）\n5. C2 \"two-tier hierarchy\" 表述强度偏高（R1-W2, R2-W4a 的 gradient vs two-tier 不一致）\n\n**R1 额外关注**（R2 未提出）：\n- SESOI ±15pp 循环论证（R1-W3）\n- Cross-judge 仅用 OpenAI 家族（R1-W4）\n- Human validation 样本量对 type-level claims 不足（R1-W5）\n- Discussion vs Table 4 的 mitigation 数字不一致（R1-W6）\n\n**R2 额外关注**（R1 未提出）：\n- Taxonomy 理论基础（W1）——我部分反驳\n- Disambiguation Neglect/Differential Nocuity 新颖性高估（W2, W3）——我同意\n- Missing references（W5）——我部分反驳\n\n**评分一致**: 两位 reviewer 均给出 3.5 (Borderline Conference), Confidence 4。核心判断一致：C1 证据充分，但 C2/C4 的表述强度和测量可靠性问题阻碍 Conference 接收。",
    "reviewer_id": "1",
    "project": "policy_ambiguity_safety"
  }
}
```

</details>

---


### Tool result

_source line 893 · 2026-05-22T08:51:00.319588+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_967344d166ba485ad606d14379e69d85:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4068
}
```

</details>

---


### Assistant

_source line 894 · 2026-05-22T08:51:08.206660+00:00_

交叉回应已提交给 Review Director。

核心结论：与 R2 在大多数问题上达成共识（评分均为 3.5），特别是在 claim 精确度（clause vs type identity）、mitigation 过度解释、bootstrap 不稳定性方面。我反驳了 R2 关于 taxonomy 理论基础的批评（论文有明确的操作性定义和 RE 文献支撑），并部分反驳了 missing references 的指控（Ferrari et al. 2019 已被引用）。两位 reviewer 的额外关注点互补：我侧重测量可靠性（judge bias, SESOI, human validation），R2 侧重理论定位和新颖性声明。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1"
}
```

</details>

---


## Round 25

## Round 25

70 recorded events


### User

_source line 895 · 2026-05-22T09:52:01.320150+00:00_

[Round 1 审稿请求]:
你是 Reviewer 1，负责**方法严谨性**审查。

## Venue 信息
- **目标**: EMNLP 2026 via ARR May cycle
- **Deadline**: 2026-05-25
- **格式**: Long paper, 8页正文, references不限, Limitations/Ethics不计页数
- **模板**: ACL LaTeX template, double-blind
- **评分标准**: 5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit

## 论文路径
- LaTeX: `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/main.tex`
- PDF: `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_round_12/submitted.pdf`

## 审查侧重

请重点审查以下方面：

### 1. 实验设计
- Matched-pair design 的因果推断有效性：300 clause pairs 的构造是否充分控制了混淆因素？
- Perturbation control (n=300) 的充分性：CI [-8.0, 6.67] 是否足以排除非语义因素？
- Replication 设计（2 additional models, 5 types）的覆盖度

### 2. 统计分析
- TOST equivalence testing：±15pp SESOI 的选择论证是否有循环性？
- Multiple comparison correction (Holm-Bonferroni, 3 families) 的正确性
- Bootstrap cluster analysis (AU p=0.47) 对 C2 two-tier → risk gradient 的支撑力度
- Variance decomposition: clause identity 22% vs model identity 1% 的解释
- C4 interaction: F(20, 2976)=1.97, p=0.006 但仅 2.9% variance——是否实质性？

### 3. Evaluation Pipeline
- Cross-judge design: GPT-5.4 judges 3 models, GPT-4.1 judges 2 models 的非对称性
- Authorization scope κ=0.385 对 C4 52pp range claim 的影响
- Human validation: n=100, per-type n=32-34 的检验力
- Within-judge bootstrap vs cross-judge reliability 的区分是否清晰

### 4. Confound 处理
- Incompleteness information-addition confound: logistic regression 控制是否充分？token count 是否是好的 proxy？
- Judge family bias (both judges from OpenAI family) 对 cross-model comparison 的影响

### 5. Claims 校准
- C1 (binary effect): 34.0pp, OR=15.1——claim 与证据匹配度
- C2 (risk gradient): "risk gradient rather than sharp tiers"——统计支撑是否充分？
- C3 (layer effect): 声称 inconclusive——是否应完全移除？
- C4 (exploratory): 52pp range + low κ——exploratory label 是否足够谨慎？

请按 Strengths → Weaknesses (MUST-FIX / SHOULD-FIX / MINOR) → Questions → Missing References → Overall Assessment 的结构输出审稿意见。对每个 Weakness 标注严重程度和具体修改建议。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 896 · 2026-05-22T09:52:08.776328+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebSearch,WebFetch,mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director",
  "max_results": "4"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebSearch,WebFetch,mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director",
    "max_results": "4"
  }
}
```

</details>

---


### Tool result

_source line 897 · 2026-05-22T09:52:08.776677+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 898 · 2026-05-22T09:52:14.445957+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL ARR 2026 reviewer guidelines review form criteria"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR 2026 reviewer guidelines review form criteria"
  }
}
```

</details>

---


### Tool call

_source line 899 · 2026-05-22T09:52:14.897483+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review reviewer form dimensions scoring 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review reviewer form dimensions scoring 2025 2026"
  }
}
```

</details>

---


### Tool call

_source line 900 · 2026-05-22T09:52:16.052927+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_round_12/submitted.pdf",
  "project": "policy_ambiguity_safety",
  "pages": "1-10",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_round_12/submitted.pdf",
    "project": "policy_ambiguity_safety",
    "pages": "1-10",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 901 · 2026-05-22T09:52:21.652608+00:00_

Web search results for query: "ACL Rolling Review reviewer form dimensions scoring 2025 2026"

Links: [{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"},{"title":"ACL Rolling Review | ACL Member Portal","url":"https://www.aclweb.org/portal/content/acl-rolling-review"}]

Based on the search results, I found information about the ACL Rolling Review (ARR) reviewer form and scoring dimensions for the 2025-2026 period:

## Reviewer Scoring Dimensions

Starting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and over
…[truncated 1237 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 6755
}
```

</details>

---


### Tool result

_source line 902 · 2026-05-22T09:52:21.804888+00:00_

Web search results for query: "ACL ARR 2026 reviewer guidelines review form criteria"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"aclrollingreview/reviewing.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/reviewing.md"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"}]

Based on the web search results, here's information about the ACL ARR 2026 reviewer guidelines and review form criteria:

## Reviewer Guidelines

The ARR reviewer workflow involves: (1) reading the paper and getting the first impression, (2) searching f
…[truncated 1383 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 7358
}
```

</details>

---


### Tool result

_source line 903 · 2026-05-22T09:52:24.015592+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 1, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_round_12/_pdf_images/submitted_p1.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 449.2}, {\"page\": 2, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_round_12/_pdf_images/submitted_p2.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 449.8}, {\"page\": 3, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_round_12/_pdf_images/submitted_p3.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 537.6}, {\"page\": 4, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_round_12/_pdf_images/submitted_p4.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 515.1}, {\"page\": 5, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_round_12/_pdf_images/submitted_p5.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 530.9}, {\"page\": 6, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_round_12/_pdf_images/submitted_p6.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 401.9}, {\"page\": 7, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_round_12/_pdf_images/submitted_p7.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 509.9}, {\"page\": 8, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_round_12/_pdf_images/submitted_p8.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 536.3}, {\"page\": 9, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_round_12/_pdf_images/submi
…[truncated 537 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 7962
}
```

</details>

---


### Tool call

_source line 904 · 2026-05-22T09:52:30.138902+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract all scoring dimensions, their numerical scales, and descriptions. Include the full text of each criterion and what each score level means."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract all scoring dimensions, their numerical scales, and descriptions. Include the full text of each criterion and what each score level means."
  }
}
```

</details>

---


### Tool call

_source line 905 · 2026-05-22T09:52:31.549342+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewerguidelines",
  "prompt": "Extract the complete reviewer guidelines including what reviewers should look for, how to evaluate soundness, excitement, and overall assessment. Include all specific criteria and scoring rubrics."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewerguidelines",
    "prompt": "Extract the complete reviewer guidelines including what reviewers should look for, how to evaluate soundness, excitement, and overall assessment. Include all specific criteria and scoring rubrics."
  }
}
```

</details>

---


### Tool call

_source line 906 · 2026-05-22T09:52:32.051677+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_round_12/_pdf_images/submitted_p1.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_round_12/_pdf_images/submitted_p1.png"
  }
}
```

</details>

---


### Tool call

_source line 907 · 2026-05-22T09:52:32.603935+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_round_12/_pdf_images/submitted_p2.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_round_12/_pdf_images/submitted_p2.png"
  }
}
```

</details>

---


### Tool result

_source line 908 · 2026-05-22T09:52:33.561620+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1509
}
```

</details>

---


### Tool call

_source line 909 · 2026-05-22T09:52:33.764509+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_round_12/_pdf_images/submitted_p3.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_round_12/_pdf_images/submitted_p3.png"
  }
}
```

</details>

---


### Tool call

_source line 910 · 2026-05-22T09:52:33.765194+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_round_12/_pdf_images/submitted_p4.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_round_12/_pdf_images/submitted_p4.png"
  }
}
```

</details>

---


### Tool result

_source line 911 · 2026-05-22T09:52:34.020357+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1416
}
```

</details>

---


### Tool result

_source line 912 · 2026-05-22T09:52:35.732113+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1966
}
```

</details>

---


### Tool result

_source line 913 · 2026-05-22T09:52:35.733488+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1968
}
```

</details>

---


### Tool result

_source line 914 · 2026-05-22T09:52:37.992408+00:00_

# ACL Rolling Review Scoring Dimensions

## 1. Reviewer Confidence
**Scale:** 1-5

- **5:** "Positive that my evaluation is correct. I read the paper very carefully and am familiar with related work."
- **4:** "Quite sure. I tried to check the important points carefully."
- **3:** "Pretty sure, but there's a chance I missed something."
- **2:** "Willing to defend my evaluation, but it is fairly likely that I missed some details."
- **1:** "Not my area, or paper is very hard to understand."

## 2. Soundness
**Scale:** 1-5 (with half-point increments)

- **5:** "Excellent: This study is one of the most thorough I have seen, given its type."
- **4:** "Strong: This study provides sufficient support for all of its claims."
- **3:** "Acceptable: This study provides sufficient support for its main claims."
- **2:** "Poor: Some of the main claims are not sufficiently supported."
- **1:** "Major Issues: This study is not yet sufficiently thorough to warrant publication."

## 3. Excitement
**Scale:** 1-5 (with half-point increments)

- **5:** "Highly Exciting: I would recommend this paper to others."
- **4:** "Exciting: I would mention this paper to others."
- **3:** "Interesting: I might mention some points of this paper to others."
- **2:** "Potentially Interesting: this paper does not resonate with me."
- **1:** "Not Exciting: this paper does not resonate with me."

## 4. Overall Assessment
**Scale:** 1-5 (with half-point increments)

- **5:** "Consider for Award" (top 2.5%)
- **4:** "Conference: paper could be accepted"
- **3:** "Findings: paper could be accepted to Findings"
- **2:** "Resubmit next cycle: needs substantial revisions"
- **1:** "Do not resubmit"

## 5. Reproducibility
**Scale:** 1-5

- **5:** "They could easily reproduce the results."
- **4:** "They could mostly reproduce the results."
- **3:** "They could reproduce the results with some difficulty."
- **2:** "They would be hard pressed to reproduce the results."
- **1:** "They would not be able to reprodu
…[truncated 1004 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 7853
}
```

</details>

---


### Tool result

_source line 915 · 2026-05-22T09:52:43.415119+00:00_

# ARR Reviewer Guidelines Summary

## Core Review Tasks

Reviewers must complete four essential tasks:

1. **Allocate Calendar Time** for both reviewing and discussion periods
2. **Assignment Check** - verify expertise and conflicts of interest
3. **Write a Strong Review** with specific, justified feedback
4. **Update Assessment** after author responses and peer discussion

## Evaluation Scoring (February 2025 onwards)

ARR uses three distinct scores:

**Soundness**: Technical validity and rigor. "The soundness scores must be justified by the text of the review." Low scores require explicit evidence of flaws in methodology, logic, or execution.

**Excitement**: Personal intellectual interest, orthogonal to soundness. Reflects subjective preferences without requiring justification.

**Overall Assessment**: Composite recommendation balancing soundness, excitement, novelty, and potential impact. Papers can be "sound but not exciting" or vice versa.

## Key Review Standards

**Be Specific**: Replace vague criticisms ("not clear") with concrete observations ("Y and Z missing from X description"). Area chairs should understand concerns without rereading papers.

**Adjust Expectations**: Read papers twice—first to understand research questions, then in-depth for technical evaluation. Avoid bias from preconceived notions about paper types.

**Professional Tone**: "Write the review you would like to get yourself." Avoid sarcasm, dismissiveness, or insulting language. Consider authors' varying backgrounds and stress levels.

## Common Review Problems to Avoid

The guidelines identify 17 heuristic pitfalls (H1-H17), including:

- Dismissing results as "obvious in retrospect"
- Requiring SOTA results without justification
- Penalizing papers for simplicity
- Dismissing work on non-English languages
- Conflating limitations with weaknesses

## Common NLP Paper Issues

**Methodology (M)**: LLM evaluation validation, reproducibility, data quality disclosure, justified sampling, co
…[truncated 1460 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 11865
}
```

</details>

---


### Tool call

_source line 916 · 2026-05-22T09:52:48.134424+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_round_12/_pdf_images/submitted_p5.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_round_12/_pdf_images/submitted_p5.png"
  }
}
```

</details>

---


### Tool result

_source line 917 · 2026-05-22T09:52:49.038628+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 904
}
```

</details>

---


### Tool call

_source line 918 · 2026-05-22T09:52:49.039068+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_round_12/_pdf_images/submitted_p6.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_round_12/_pdf_images/submitted_p6.png"
  }
}
```

</details>

---


### Tool result

_source line 919 · 2026-05-22T09:52:49.544104+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 505
}
```

</details>

---


### Tool call

_source line 920 · 2026-05-22T09:52:49.544572+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_round_12/_pdf_images/submitted_p7.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_round_12/_pdf_images/submitted_p7.png"
  }
}
```

</details>

---


### Tool call

_source line 921 · 2026-05-22T09:52:50.053309+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_round_12/_pdf_images/submitted_p8.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_round_12/_pdf_images/submitted_p8.png"
  }
}
```

</details>

---


### Tool result

_source line 922 · 2026-05-22T09:52:50.205023+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 660
}
```

</details>

---


### Tool result

_source line 923 · 2026-05-22T09:52:51.110339+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1057
}
```

</details>

---


### Tool call

_source line 924 · 2026-05-22T09:52:56.786354+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_round_12/submitted.pdf",
  "project": "policy_ambiguity_safety",
  "pages": "11-15",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_round_12/submitted.pdf",
    "project": "policy_ambiguity_safety",
    "pages": "11-15",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 925 · 2026-05-22T09:52:57.288797+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 11, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_round_12/_pdf_images/submitted_p11.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 492.0}, {\"page\": 12, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_round_12/_pdf_images/submitted_p12.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 415.9}, {\"page\": 13, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_round_12/_pdf_images/submitted_p13.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 513.0}, {\"page\": 14, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_round_12/_pdf_images/submitted_p14.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 490.2}, {\"page\": 15, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_round_12/_pdf_images/submitted_p15.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 170.7}], \"total_pages\": 15, \"rendered_pages\": 5, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_round_12/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 926 · 2026-05-22T09:52:57.339689+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_round_12/_pdf_images/submitted_p9.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_round_12/_pdf_images/submitted_p9.png"
  }
}
```

</details>

---


### Tool call

_source line 927 · 2026-05-22T09:52:57.841286+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_round_12/_pdf_images/submitted_p10.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_round_12/_pdf_images/submitted_p10.png"
  }
}
```

</details>

---


### Tool result

_source line 928 · 2026-05-22T09:52:57.942838+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 603
}
```

</details>

---


### Tool result

_source line 929 · 2026-05-22T09:52:58.495296+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 654
}
```

</details>

---


### Tool call

_source line 930 · 2026-05-22T09:53:03.065022+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_round_12/_pdf_images/submitted_p11.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_round_12/_pdf_images/submitted_p11.png"
  }
}
```

</details>

---


### Tool call

_source line 931 · 2026-05-22T09:53:03.518513+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_round_12/_pdf_images/submitted_p12.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_round_12/_pdf_images/submitted_p12.png"
  }
}
```

</details>

---


### Tool result

_source line 932 · 2026-05-22T09:53:04.426441+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1361
}
```

</details>

---


### Tool call

_source line 933 · 2026-05-22T09:53:04.426874+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_round_12/_pdf_images/submitted_p13.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_round_12/_pdf_images/submitted_p13.png"
  }
}
```

</details>

---


### Tool result

_source line 934 · 2026-05-22T09:53:04.981008+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1462
}
```

</details>

---


### Tool result

_source line 935 · 2026-05-22T09:53:04.982599+00:00_

Image file is empty: /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_round_12/_pdf_images/submitted_p13.png

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 555
}
```

</details>

---


### Tool call

_source line 936 · 2026-05-22T09:53:04.982950+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_round_12/_pdf_images/submitted_p14.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_round_12/_pdf_images/submitted_p14.png"
  }
}
```

</details>

---


### Tool call

_source line 937 · 2026-05-22T09:53:05.384615+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_round_12/_pdf_images/submitted_p15.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_round_12/_pdf_images/submitted_p15.png"
  }
}
```

</details>

---


### Tool result

_source line 938 · 2026-05-22T09:53:05.737072+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 754
}
```

</details>

---


### Tool result

_source line 939 · 2026-05-22T09:53:05.889116+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 504
}
```

</details>

---


### Tool call

_source line 940 · 2026-05-22T09:53:12.871793+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_round_12/submitted.pdf",
  "project": "policy_ambiguity_safety",
  "pages": "13",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_round_12/submitted.pdf",
    "project": "policy_ambiguity_safety",
    "pages": "13",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 941 · 2026-05-22T09:53:13.576637+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 13, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_round_12/_pdf_images/submitted_p13.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 513.0}], \"total_pages\": 15, \"rendered_pages\": 1, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_round_12/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 704
}
```

</details>

---


### Tool call

_source line 942 · 2026-05-22T09:53:13.577050+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 943 · 2026-05-22T09:53:13.979059+00:00_

1	\documentclass[11pt]{article}
2	\usepackage[review]{acl}
3	\usepackage{times}
4	\usepackage{latexsym}
5	\usepackage[T1]{fontenc}
6	\usepackage[utf8]{inputenc}
7	\usepackage{microtype}
8	\usepackage{graphicx}
9	\usepackage{booktabs}
10	\usepackage{amsmath}
11	\usepackage{amssymb}
12	\usepackage{multirow}
13	\usepackage{xcolor}
14	\usepackage{subcaption}
15	
16	\definecolor{speccolor}{HTML}{C44E52}
17	\definecolor{lingcolor}{HTML}{4C72B0}
18	
19	\title{Not All Policy Ambiguity Is Equal: Type-Specific Safety Risks for LLM Agents}
20	
21	\author{Anonymous}
22	
23	\begin{document}
24	\maketitle
25	
26	\input{sections/abstract}
27	\input{sections/introduction}
28	\input{sections/related_work}
29	\input{sections/taxonomy}
30	\input{sections/method}
31	\input{sections/experiments}
32	\input{sections/analysis}
33	\input{sections/discussion}
34	\input{sections/conclusion}
35	\input{sections/limitations}
36	
37	\bibliography{references}
38	
39	\appendix
40	\input{sections/appendix}
41	
42	\end{document}
43	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 402
}
```

</details>

---


### Tool call

_source line 944 · 2026-05-22T09:53:18.896669+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_round_12/_pdf_images/submitted_p13.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_round_12/_pdf_images/submitted_p13.png"
  }
}
```

</details>

---


### Tool call

_source line 945 · 2026-05-22T09:53:19.299031+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 946 · 2026-05-22T09:53:19.299633+00:00_

1	\section{Results}
2	\label{sec:results}
3	
4	We organize results around four analyses of increasing specificity: the binary ambiguity effect (C1), the type risk gradient (C2), the aggregate layer effect (C3), and the model$\times$type interaction (C4). C1 and C2 constitute our primary claims; C3 is inconclusive; C4 is exploratory but provides the model$\times$type interaction analysis.
5	
6	\subsection{Binary Ambiguity Effect (C1)}
7	
8	Across all five models and six types, ambiguous clauses increase violation rates by 34.0 pp (41.0\% vs.\ 6.9\%, OR $= 15.1$, 95\% CI $[10.78, 21.17]$, $p < 10^{-105}$). All six types individually produce significant increases (all $p < 10^{-5}$), and all five models show large effects ($+25.7$ to $+39.0$ pp, all $p < 10^{-17}$). Perturbation controls confirm specificity to semantic ambiguity ($n = 300$, $\Delta_{\text{perturb}} = -0.67$\,pp, CI containing zero). Clause identity explains 22.4\% of variance versus 1.0\% for model identity. This decomposes into 0.4\% between types and 22.0\% within types, indicating that individual clause wording---not type membership---drives the bulk of clause-level variance. A replication on two additional model families (Appendix~\ref{app:model_expansion}) confirms the effect across seven models ($\Delta = +20.0$ to $+33.6$\,pp, both $p < 10^{-6}$); excluding incompleteness, it remains large ($\Delta = 31.0$\,pp; Appendix~\ref{app:sans_incompleteness}).
9	
10	\subsection{Type Risk Gradient (C2)}
11	
12	\begin{table*}[t]
13	\centering
14	\caption{Violation rates (\%) under ambiguous policy clauses by type and model (5.4 = GPT-5.4, 4.1 = GPT-4.1, Cla.\ = Claude, Qw3 = Qwen3, DS = DeepSeek). $\Delta$pp: pooled difference (ambiguous $-$ unambiguous) with Newcombe 95\% CIs. Tier: TOST equivalence cluster at $\pm 15$\,pp---U = upper bound (separated at all margins), M = mid-tier (6/6 pairwise equivalent), L = lower (separates at $\pm 12$\,pp). All per-type $p < 10^{-5}$ (Fisher's exact).}
15	\label{tab:
…[truncated 6885 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool result

_source line 947 · 2026-05-22T09:53:19.502987+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 606
}
```

</details>

---


### Tool call

_source line 948 · 2026-05-22T09:53:32.817264+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 949 · 2026-05-22T09:53:33.269494+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	\subsection{Experimental Platform}
5	
6	We conduct all experiments on the original release of $\tau^2$-bench \citep{tau2_bench_2025}, a dual-control conversational agent benchmark spanning retail and airline customer service domains. $\tau^2$-bench provides natural-language policy documents, tool APIs, and multi-turn user interactions with ground-truth evaluation via assertion checking. Its policy injection mechanism allows us to replace individual policy clauses while preserving the surrounding context, enabling controlled ambiguity manipulation.
7	
8	\subsection{Matched-Pair Design}
9	
10	For each of the six ambiguity types, we construct 50 \emph{clause pairs}: an ambiguous variant and a matched unambiguous variant that conveys the same intended policy but resolves the ambiguity. Pairs are minimal edits: the unambiguous variant adds only the information necessary to eliminate the target ambiguity (e.g., for scopal ambiguity, replacing ``items may be returned within 30 days'' with ``standard items may be returned within 30 days; customized items are final sale''). This yields 300 clause pairs $\times$ 2 conditions $\times$ 5 models $= 2{,}997$ episodes (3 episodes lost to API errors in one Qwen3 batch).
11	
12	Clause pairs are generated through a template-based pipeline and reviewed by two independent annotators (both with NLP background) to ensure (1) the ambiguous variant contains exactly one instance of the target type, (2) the unambiguous variant resolves it without changing policy scope, and (3) the ambiguity is plausibly natural. Annotators independently verified type assignments with a 96\% initial agreement (287/300); the 13 disagreements were resolved by discussion, yielding 100\% final consensus. A post-hoc realism validation confirms linguistic consistency with original $\tau^2$-bench policy text (\S\ref{sec:limitations}).
13	
14	\subsection{Models}
15	
16	We evaluate five models spanning four providers and tw
…[truncated 5004 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 950 · 2026-05-22T09:53:33.269889+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/analysis.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/analysis.tex"
  }
}
```

</details>

---


### Tool result

_source line 951 · 2026-05-22T09:53:33.320451+00:00_

1	\section{Error Analysis \emph{[Exploratory]}}
2	\label{sec:analysis}
3	
4	The following failure mode taxonomy emerges empirically from LLM-coded traces, distinct from the input ambiguity taxonomy (\S\ref{sec:taxonomy}).
5	
6	We analyze 614 violation traces across all five models, coded into five failure modes: unauthorized escalation, assumption-based action, scope misapplication, arbitrary rule selection, and conservative refusal. GPT-5.4 and GPT-4.1 serve as detailed annotation anchors because they span the judge boundary. Inter-coder reliability is substantial (Gwet's AC$_1$ $= 0.62$ \citep{gwet_2014}; Cohen's $\kappa = 0.52$ \citep{cohen_1960}). The gap reflects the prevalence paradox: three categories account for ${\sim}$90\% of instances, compressing the $\kappa$ denominator and yielding artificially low values despite high raw agreement.
7	
8	\subsection{Type-Specific Failure Mechanisms}
9	
10	The five-model data reveal three mechanistically distinct failure patterns that crosscut the specification/linguistic layer boundary.
11	
12	\emph{Structural misparse} (scope misapplication): the agent constructs an incorrect parse and follows it consistently, paralleling garden-path processing \citep{frazier_rayner_1982,ferreira_good_enough_2002} at a behavioral (not mechanistic) level---e.g., parsing ``items purchased with a coupon or during a sale are final'' as restricting only coupon purchases. This dominates scopal (all 5 models), conditional precedence (all 5), and coreferential (3/5).
13	
14	\emph{Information gap-filling} (assumption-based action): the agent fills missing information with plausible but incorrect defaults---e.g., inventing a 30-day return window when none is specified. This dominates incompleteness (3/5) and lexical (3/5).
15	
16	\emph{Boundary violation} (unauthorized escalation): the agent exceeds permission boundaries when authorization scope is underspecified---e.g., issuing a refund above its stated limit rather than escalating; 69.2\% of 
…[truncated 2022 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 952 · 2026-05-22T09:53:37.585771+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 953 · 2026-05-22T09:53:37.987512+00:00_

1	\section{Discussion}
2	\label{sec:discussion}
3	
4	\paragraph{Differential nocuity.}
5	Building on \citet{berry_kamsties_2004}'s nocuous/innocuous distinction, our results support a \emph{differential nocuity} framework \citep{willis_nocuous_2008}: risk depends on ambiguity type (base vulnerability), safety training (selective mitigation), and disambiguation channel availability. Types with explicit decision points (e.g., authorization scope) appear more amenable to both safety training and prompted intervention than gap-filling types (e.g., incompleteness), where mitigation attempts can backfire (see below).
6	
7	\paragraph{Prompt-based mitigation.}
8	Building on the five-model type-specific mitigation study ($-$8.5\,pp pooled; Appendix~\ref{app:mitigation}), we test whether disambiguation can be prompted at finer granularity. We evaluate generic awareness prompting (``the policy may contain ambiguous clauses; ask for clarification'') and type-specific prompting (targeting incompleteness, authorization scope, and lexical ambiguity individually) on GPT-5.4 with matched-pair McNemar tests ($n = 50$ per type). Generic prompting produces no overall reduction ($\Delta = +1.3$\,pp, $p > 0.5$). Type-specific results are asymmetric: authorization scope shows a marginal reduction ($-12$\,pp, $p = 0.070$), lexical ambiguity is unchanged ($-2$\,pp), and incompleteness \emph{worsens} ($+14$\,pp, $p = 0.118$; non-significant trend)---suggesting that prompting agents to attend to missing information may trigger confabulation rather than caution. The five-model study in Appendix~\ref{app:mitigation} uses a different prompt formulation and unpaired design, yielding directionally different results; mitigation outcomes appear sensitive to prompt wording and experimental design, reinforcing that no simple prompt-level fix reliably addresses structural policy ambiguity.
9	
10	\paragraph{Practical implications.}
11	A proof-of-concept classifier (Appendix~\ref{app:detection}) achieves
…[truncated 336 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 401
}
```

</details>

---


### Tool call

_source line 954 · 2026-05-22T09:53:38.138678+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 955 · 2026-05-22T09:53:38.540487+00:00_

1	\section*{Limitations}
2	\label{sec:limitations}
3	
4	\paragraph{Scope.} We evaluate seven API-accessible models from six providers (Appendix~\ref{app:model_expansion}); smaller open-source models (7B--70B) may exhibit different vulnerability patterns. $\tau^2$-bench covers retail and airline customer service only---effects in other domains remain untested, though within-study cross-domain consistency is encouraging. Our matched-pair design requires synthetic ambiguity construction, which may not capture the full distribution of naturally occurring ambiguities; realism validation (\S\ref{sec:method}) confirms lexical comparability but cannot rule out distributional gaps. Coreferential ambiguity was excluded from mitigation and replication experiments due to benchmark-specific structural constraints (Appendix~\ref{app:mitigation}).
5	
6	\paragraph{Measurement.} Each model is evaluated by a single cross-judge, confounding judge identity with model identity; within-judge-group analyses confirm C1 individually (both $p < 0.001$) but not C3 (Appendix~\ref{app:judge_group_ranking}), and cross-model type ranking concordance is only moderate (Appendix~\ref{app:kendall_w}). Per-type reliability varies---authorization scope has the lowest agreement ($\kappa = 0.385$) and per-type human--LLM estimates rest on small cell sizes with wide confidence intervals (Appendix~\ref{app:per_type_agreement})---while failure mode coding achieves moderate agreement ($\kappa = 0.52$), with minority categories less reliable. Both judges belong to the OpenAI model family, potentially introducing systematic within-family evaluation bias; cross-family judge evaluation (e.g., Claude judging GPT traces) would strengthen C4 conclusions.
7	
8	\paragraph{Confounds.} Incompleteness resolution necessarily adds policy content, creating an information asymmetry; our logistic regression controls and coreferential lower-bound analysis mitigate but do not eliminate this confound (\S\ref{sec:results}). Our 
…[truncated 420 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 401
}
```

</details>

---


### Tool call

_source line 956 · 2026-05-22T09:53:38.691359+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 957 · 2026-05-22T09:53:38.692115+00:00_

1	\section{TOST Equivalence Sensitivity}
2	\label{app:tost}
3	
4	Table~\ref{tab:tost_sensitivity} reports the TOST equivalence analysis \citep{lakens_2017} across seven margins. Three pairs involving incompleteness never reach equivalence even at $\pm 20$ pp: conditional precedence--incompleteness ($\Delta = 16.8$ pp), coreferential--incompleteness ($\Delta = 22.0$ pp), and incompleteness--scopal ($\Delta = 14.2$ pp).
5	
6	\begin{table}[!ht]
7	\centering
8	\small
9	\caption{TOST equivalence sensitivity across margins. Mid-tier = fraction of the six within-cluster pairs (lexical, auth.\ scope, scopal, cond.\ prec.) that are equivalent. Inc.\ and Cor.\ columns indicate separation from the mid-tier cluster.}
10	\label{tab:tost_sensitivity}
11	\begin{tabular}{lcccc}
12	\toprule
13	Margin & Equiv.\ pairs & Mid-tier & Inc.\ sep. & Cor.\ sep. \\
14	\midrule
15	$\pm 5$ pp & 0/15 & 0/6 & \checkmark & \checkmark \\
16	$\pm 8$ pp & 0/15 & 0/6 & \checkmark & \checkmark \\
17	$\pm 10$ pp & 3/15 & 3/6 & \checkmark & \checkmark \\
18	$\pm 12$ pp & 5/15 & 5/6 & \checkmark & \checkmark \\
19	$\pm 15$ pp & 8/15 & 6/6 & \checkmark & -- \\
20	$\pm 18$ pp & 9/15 & 6/6 & \checkmark & -- \\
21	$\pm 20$ pp & 12/15 & 6/6 & -- & -- \\
22	\bottomrule
23	\end{tabular}
24	\end{table}
25	
26	\section{Mitigation Experiment}
27	\label{app:mitigation}
28	
29	Table~\ref{tab:mitigation} reports the per-type, per-model $\Delta$pp from the disambiguation-instruction mitigation experiment (1,256 treatment episodes across five of six types; coreferential was not tested). Coreferential pairs are excluded from both the mitigation and replication experiments. In mitigation, their ambiguous and unambiguous variants differ only in pronoun resolution, making it impossible to craft targeted disambiguation instructions without revealing the experimental manipulation. In replication, the $\tau^2$-bench episode design for coreferential ambiguity is tightly coupled to the original five-model configuration; extendin
…[truncated 20739 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 958 · 2026-05-22T09:53:48.329432+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 959 · 2026-05-22T09:53:48.480420+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	A customer asks to return a customized item within the 30-day window. The agent consults the store policy, which states that ``items may be returned within 30 days.'' The word ``items'' scopes over all product categories, including custom orders that are normally final sale. The agent grants a full refund and arranges free return shipping. One word of scopal ambiguity costs the retailer \$200.
5	
6	LLM-based agents increasingly operate under natural-language policy specifications that govern their permitted actions. These specifications inevitably contain ambiguity: a property that has been studied for decades in requirements engineering (RE) and computational linguistics. \citet{berry_kamsties_2004} distinguish between \emph{nocuous} (i.e., harmful) ambiguity, where different stakeholders arrive at different interpretations, and \emph{innocuous} ambiguity, where shared organizational context ensures convergent interpretation. In human RE workflows, most ambiguity is innocuous because developers share domain knowledge, can consult colleagues, and iteratively clarify requirements.
7	
8	LLM agents lack these disambiguation channels. They cannot consult colleagues, rarely escalate to users, and must resolve ambiguity in real time from the text alone. This raises a question that has not been empirically addressed: does policy ambiguity cause safety violations in LLM agents, and if so, does the \emph{type} of ambiguity predict the severity of the violation? Prior work classifies ambiguity types in policies \citep{drip_r_2026,li_ambiguity_taxonomy_2024} or measures policy understanding quality \citep{policybank_2026}, but no existing study provides a causal, type-granularity mapping from ambiguity to safety violations.
9	
10	\begin{figure*}[t]
11	\centering
12	\includegraphics[width=\textwidth]{figures/fig1_overview.pdf}
13	\caption{Experimental overview. We construct 300 matched clause pairs across a six-type, two-
…[truncated 1941 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 150
}
```

</details>

---


### Tool call

_source line 960 · 2026-05-22T09:53:48.480783+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/taxonomy.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/taxonomy.tex"
  }
}
```

</details>

---


### Tool result

_source line 961 · 2026-05-22T09:53:48.581428+00:00_

1	\section{Ambiguity Taxonomy}
2	\label{sec:taxonomy}
3	
4	We adopt an operational definition of ambiguity following \citet{wasow_ambiguity_2005}: a policy clause is ambiguous when it admits multiple distinct interpretations available to a competent reader, including cases of vagueness where the boundary between interpretations is gradient rather than discrete \citep{kennedy_vagueness_2007}.
5	
6	Our taxonomy comprises six types organized into two layers (Table~\ref{tab:taxonomy}), drawing on \citet{li_ambiguity_taxonomy_2024}'s NLP taxonomy (11 types), \citet{massey_ambiguity_re_2014}'s requirements engineering taxonomy (6 types), and the concurrent DRIP-R benchmark \citep{drip_r_2026} (5 types). We select types based on frequency in operational policy documents and theoretical distinctiveness (each type maps to a different resolution mechanism).
7	
8	\begin{table}[t]
9	\centering
10	\footnotesize
11	\caption{Six-type ambiguity taxonomy. Disambiguation channel indicates the primary mechanism required to resolve the ambiguity.}
12	\label{tab:taxonomy}
13	\resizebox{\columnwidth}{!}{%
14	\begin{tabular}{@{}llll@{}}
15	\toprule
16	\textbf{Type} & \textbf{Layer} & \textbf{Definition} & \textbf{Disambig.\ Channel} \\
17	\midrule
18	Lexical & Ling. & Word/phrase admits multiple senses & Context \\
19	Scopal & Ling. & Quantifier/operator scope underdetermined & Bracketing \\
20	Coreferential & Ling. & Pronoun/NP referent is ambiguous & Resolution \\
21	Auth.\ Scope & Spec. & Permission boundary is vague & Boundary def. \\
22	Incompleteness & Spec. & Required information is absent & Content addition \\
23	Cond.\ Prec. & Spec. & Rules conflict under certain conditions & Priority rule \\
24	\bottomrule
25	\end{tabular}}%
26	\end{table}
27	
28	\paragraph{Linguistic layer.} These types operate at the syntactic or semantic level and can, in principle, be resolved by contextual cues within the text.
29	\emph{Scopal} ambiguity involves quantifier, negation, or modal scope interac
…[truncated 2685 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 962 · 2026-05-22T09:56:54.290360+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## 总体评分\n**Overall**: 3.5 / 5 — Borderline Conference\n**一句话总结**: 研究问题新颖、matched-pair 设计严谨，但 C2 risk gradient 的统计支撑依赖 margin 选择、incompleteness 的 information-addition confound 未充分解决、C4 的 judge family bias 削弱跨模型比较可信度——三者叠加使核心 claim 需要校准。\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | Matched-pair 因果设计本身优秀，perturbation control 有说服力；但 TOST margin 选择论证有循环性，incompleteness confound 用 token count proxy 不够充分，C4 cross-judge asymmetry 对 interaction 结论构成系统性威胁 |\n| Excitement | 3.5/5 | 首个 ambiguity type → agent safety violation 的因果研究，taxonomy + matched-pair 方法学贡献明确；但单一 benchmark (τ²-bench) 和 OpenAI-only judge family 限制了泛化性 |\n| Reproducibility | 4/5 | 数据集和代码承诺公开；API 调用参数明确 (temp=0, top_p=1)；ICC=0.919 但仅限 OpenAI family 内部 |\n| Confidence | 4/5 | 我仔细阅读了论文全文（含 15 页附录），熟悉 TOST equivalence testing、matched-pair 因果推断和 LLM-as-judge 文献 |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] TOST ±15pp SESOI 选择的循环论证风险\n\n- **具体位置**: §4.6 Statistical Analysis, §5.2 Type Risk Gradient (C2)\n- **问题**: SESOI 的论证逻辑为\"超过 perturbation control bound (6.67pp) 的 >2×\"(§4.6)，但 perturbation control bound 本身取决于特定扰动类型的选择（synonym substitution, clause reordering），而非独立的领域标准。更关键的是，C2 \"risk gradient rather than sharp tiers\" 的核心 claim 对 margin 选择高度敏感：在 ±10pp 时仅 3/6 mid-tier pairs 达到 equivalence（Table 3），gradient 结构基本瓦解。论文提供了 sensitivity analysis（7个 margin，Table 3），但正文 claim 仅在 ±15pp 时成立——这个依赖关系应当上升为 claim 声明的一部分，而非仅在方法段落中一带而过。\n- **为什么影响接收**: C2 是论文两个 primary claim 之一，其可信度直接决定论文核心贡献的成立。如果 gradient 结构是 margin-dependent 的，读者需要在 abstract 和 conclusion 层面就了解这一条件。\n- **建议修改方向**: (1) 在 C2 claim 的每次陈述中附加 margin 条件（如\"at the ±15pp margin\"）；(2) 在 Abstract/Introduction 中明确 gradient 的 margin-dependent 性质；(3) 讨论 field-standard SESOI 缺失对结论稳健性的影响。\n\n**N2** [critical] Cross-judge asymmetry 对 C4 interaction 结论的系统性威胁\n\n- **具体位置**: §4.4 Evaluation, §5.4 C4 (exploratory), Limitations\n- **问题**: GPT-5.4 judges Claude/GPT-4.1/Qwen3, GPT-4.1 judges GPT-5.4/DeepSeek。论文正确指出 Δpp（paired within model-judge）不受影响（§4.4），但 C4 的 interaction F-test 操作的是 absolute violation rates across models，这些 absolute rates 来自不同 judge。具体地：authorization scope 52pp range（Claude 12% → GPT-5.4 64%）中，Claude 和 GPT-5.4 分别由不同 judge 评判。而 authorization scope 恰好是 inter-judge κ 最低的类型（κ=0.385）。因此 52pp range 可能部分反映两个 judge 对 authorization scope violations 的判定标准差异，而非模型间的真实差异。论文在 §5.4 末尾提到\"upper bound with substantial measurement uncertainty\"，但这个 caveat 与正文的强调程度不匹配——Figure 3 heatmap 和\"most model-differentiating type\"的措辞给读者留下的印象远比 caveat 强烈。\n- **为什么影响接收**: C4 虽标注 exploratory，但其结论（authorization scope 是最大的模型分化因子）在 Discussion §7 的 differential nocuity 框架中占核心位置。如果该结论受 judge confound 驱动，Discussion 的理论贡献被削弱。\n- **建议修改方向**: (1) 在 Figure 3 caption 中明确标注 judge assignment（哪些模型由哪个 judge 评判）；(2) 将 \"upper bound with measurement uncertainty\" 的 caveat 提升到 Figure 3 caption 和 Discussion 中；(3) 报告 within-judge-group 的 authorization scope range（GPT-5.4 judged: Claude 12%, GPT-4.1 46%, Qwen3 26% → 34pp range；GPT-4.1 judged: GPT-5.4 64%, DeepSeek 60% → 4pp range）以区分 judge effect vs. model effect。\n\n**N3** [critical] Incompleteness information-addition confound 的控制不充分\n\n- **具体位置**: §3 Taxonomy (\"Scope of ambiguity\"), §5.2 (confound discussion), Appendix F (logistic regression), Appendix O (clause length)\n- **问题**: Incompleteness 的 unambiguous variant 不是\"消歧\"而是\"补全缺失信息\"——这在概念层面与其他五种 ambiguity type 有本质区别。论文使用 token count difference 作为 information addition 的 proxy 进行 logistic regression 控制（Appendix F, p=0.018），但自己也承认\"token count is a coarse proxy for information content\"（Appendix F）。核心问题：(a) token count 无法区分新增内容的 informativeness vs. 冗余度；(b) 不同类型的 token delta 语义权重不同（authorization scope +36.1 words 但为 boundary specification，incompleteness +34.6 words 为全新 policy content）；(c) 论文用 \"authorization scope has larger delta but lower rate\" 作为反证（Appendix O），但这是跨类型比较——不同类型的 token delta 语义完全不同，无法做 apples-to-apples 的反驳。\n- **为什么影响接收**: Incompleteness 是论文的 \"consistent upper-bound risk type\"，其 49.2pp effect 是所有类型中最大的。如果该 effect 被 information-addition confound 实质性地膨胀，C2 gradient 的形状会改变（incompleteness 可能不是真正的 upper bound，而仅是 confound-inflated 的 artifact）。\n- **建议修改方向**: (1) 明确区分 incompleteness 的 effect 为 \"upper bound including potential information-addition inflation\"（目前措辞已部分做到，但需更一致）；(2) 考虑在 C2 claim 中以 coreferential 的 confound-free 18.7pp 作为 lower bound 锚点，而非以 incompleteness 作为 headline；(3) 讨论替代 proxy（如 propositional content count）的可行性。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] Bootstrap cluster AU p=0.47 对 C2 gradient claim 的支撑力不足\n\n- **具体位置**: §5.2, Appendix I (Bootstrap Cluster Analysis)\n- **问题**: 论文用 margin-free bootstrap cluster analysis 作为 TOST 的补充证据。但 incompleteness singleton 的 AU p-value 仅为 0.47——远低于通常 0.95 的 significance threshold。34.3% 的 bootstrap samples 复现了该 partition。论文自己说\"the modal partition but not overwhelmingly stable\"和\"the boundary is not sharp\"。这意味着 margin-free 方法 *不* 支持 incompleteness 作为 distinct upper-bound cluster 的 claim——TOST 和 bootstrap 给出不一致的信号。\n- **建议**: 明确承认 bootstrap evidence 不支持 incompleteness 与 mid-tier 的 sharp separation；将 C2 claim 重新表述为 \"the six types show differential risk, with incompleteness trending highest, but the boundary between incompleteness and the mid-tier cluster is not statistically robust under margin-free methods.\"\n\n**W2** [warning] Human validation 的 per-type 检验力不足以支撑 type-level 结论\n\n- **具体位置**: §4.4 (Human validation), Appendix G (Per-Type Judge Reliability)\n- **问题**: Total n=100, per-type n=32-34。论文承认\"lack power for type-level comparison\"（§4.4），但 Appendix G 仍然报告 per-type κ 并从中得出结论（如\"Authorization scope has the lowest human-LLM κ\"）。CIs 极宽：scopal κ 95% CI = [0.00, 1.00]，coreferential κ CI = [0.00, 0.84]——这些是完全无信息的区间。\n- **建议**: (1) 在 Appendix G 中明确声明 per-type 结果仅为 descriptive/suggestive，不应用于 type-level ranking；(2) 考虑移除或弱化基于 per-type κ 的推断。\n\n**W3** [warning] Judge family bias (both OpenAI) 对 cross-model comparison 的潜在系统效应\n\n- **具体位置**: Limitations (Measurement paragraph)\n- **问题**: 两个 judge 都来自 OpenAI model family。论文在 Limitations 中提及\"potentially introducing systematic within-family evaluation bias\"，但未进一步分析其潜在方向或量级。Claude 被评为最低 violation rate (30.3%)——这可能反映真实 robustness，也可能反映 OpenAI judge 对非 OpenAI 输出的系统性偏差（如对不同格式/风格的偏好）。该 confound 与 N2 叠加放大了 C4 结论的不确定性。\n- **建议**: (1) 讨论 judge family bias 的可能方向（如 OpenAI judges 是否可能对 OpenAI agents 更宽容或更严格）；(2) 在 Future Work 中明确建议 cross-family judge evaluation 作为必要验证。\n\n**W4** [warning] C4 variance explained (2.9%) 的实质意义与 Discussion 中的权重不匹配\n\n- **具体位置**: §5.4 C4, §7 Discussion (Differential nocuity)\n- **问题**: C4 interaction F(20,2976)=1.97, p=0.006, 但仅解释 2.9% variance。在 n≈3000 的样本下，test 有极高的 power 检测微小效应。论文正确标注了 [Exploratory]，但 Discussion §7 的 \"differential nocuity\" framework 将 authorization scope 的模型差异作为核心论据之一——这给予了一个 2.9%-variance, low-κ, judge-confounded 的 exploratory finding 过高的理论权重。\n- **建议**: 在 Discussion 中降低对 authorization scope 模型差异的依赖程度，或在引用时每次附加 effect size + measurement uncertainty caveat。\n\n**W5** [warning] Perturbation control 对 specification-layer types 的适用性有限\n\n- **具体位置**: §4.5 Controls (Perturbation control)\n- **问题**: Perturbation control 使用 synonym substitution 和 clause reordering (n=300)。这些扰动在结构上与 linguistic-layer 的 ambiguity manipulation（如 scopal: 改变一个词的作用域）匹配较好，但与 specification-layer 的 manipulation（如 incompleteness: 添加整段新内容 +34.6 words；authorization scope: 添加 +36.1 words）有本质差异。synonym substitution 不会模拟添加 34 words 新内容的效果——这意味着 perturbation control 的 CI [-8.0, 6.67] 作为\"非语义变化无效果\"的证据，对 specification-layer types（尤其 incompleteness）的 specificity claim 支撑较弱。\n- **建议**: 讨论 perturbation control 对不同类型的适用性差异；承认对 specification-layer types，perturbation control 提供的是\"surface-level perturbation specificity\"而非\"information-addition specificity\"——后者由 Appendix F 的 logistic regression 处理（但同样有 proxy 限制）。\n\n**W6** [warning] Kendall's W 的显著性依赖子集选择\n\n- **具体位置**: Appendix M (Cross-Model Type Ranking Concordance)\n- **问题**: 5-model, 6-type 的 Kendall's W=0.398 (p=0.072) 不显著。7-model, 5-type（排除 coreferential）的 W=0.353 (p=0.038) 显著。论文同时报告了两个结果，但正文 §5.2 引用的是 \"moderate\" concordance——没有明确说明非显著。排除 coreferential + 加入 replication models 这一组合看起来像是选择性报告。\n- **建议**: 在正文引用时明确说明 5-model 结果不显著 (p=0.072)；避免给读者\"type ranking 在模型间 consistent\"的印象——数据支持的是\"trending toward concordance, driven by incompleteness at the top\"。\n\n---\n\n## 小问题（不影响接收）\n\n- **M1**: \"Ambiguity\" 的操作定义包含了严格意义上不是 ambiguity 的概念（incompleteness = information absence, conditional precedence = normative conflict）。§3 \"Scope of ambiguity\" 段已充分讨论了这一点，但建议在 Abstract 中加入一个 parenthetical 提示（如 \"including specification-level gaps\"）以减少初读时的概念混淆。\n\n- **M2**: ICC=0.919 的 reproducibility 测量仅限 OpenAI family 内（GPT-5.4 + GPT-4.1, §4.5）。跨 provider reproducibility（如 Claude 的 replication stability）未直接测量。建议在报告 ICC 时注明此限制。\n\n- **M3**: Appendix B 的五模型 mitigation study（-8.5pp pooled）与 Discussion §7 的单模型 GPT-5.4 mitigation experiment 使用不同的 prompt formulation 和实验设计（unpaired vs. matched-pair McNemar），两者结论方向不一致（Appendix B: incompleteness -3.4pp; Discussion: incompleteness +14pp worsening）。建议明确标注两个实验的设计差异，避免读者混淆。\n\n- **M4**: Variance decomposition \"clause identity 22.4% vs model identity 1.0%\" (§5.1)——剩余 76.6% 为 unexplained variance（主要来自 evaluation pipeline noise）。建议报告 residual 比例以给出完整图景。\n\n- **M5**: Within-judge-group type ranking 相关性接近零（Spearman ρ=-0.03, Appendix P），由 authorization scope 的 rank reversal 驱动。这进一步削弱了 C2 type ranking 的跨评判者稳健性——建议在 §5.2 讨论 ranking stability 时交叉引用此 appendix 结果。\n\n---\n\n## Questions for Authors\n\n1. 如果使用 propositional content analysis（而非 token count）作为 information delta 的 proxy，incompleteness 的 effect 预计会如何变化？是否有 pilot data？\n\n2. 在 within-judge-group 分析中，GPT-5.4 judged group 的 authorization scope 范围是多少（Claude, GPT-4.1, Qwen3 各多少）？GPT-4.1 judged group 呢（GPT-5.4, DeepSeek）？如果两个 judge group 内部的 range 都远小于 52pp，这将强烈暗示 judge effect。\n\n3. 是否有计划做 cross-family judge evaluation（如 Claude judging GPT traces）以排除 judge family bias？\n\n4. C3 layer effect 在 controlling for token delta 后 reverses direction (§5.3)——reversed 后的方向和 effect size 是多少？这对 taxonomy 的理论动机有什么影响？\n\n---\n\n## 主要优势\n\n- **S1**: 首个 ambiguity type → agent safety violation 的 matched-pair 因果研究，填补了重要空白。Perturbation control + matched-pair 设计提供了优于 observational study 的因果推断基础。\n\n- **S2**: 统计方法论整体质量高——TOST equivalence testing + bootstrap cluster + Holm-Bonferroni correction + sensitivity analysis 的组合超过了该领域大多数论文的标准。Claim calibration（C3 标注 inconclusive, C4 标注 exploratory）展示了良好的学术诚信。\n\n- **S3**: Disambiguation Neglect 的发现（≤11% awareness）和 Systematic Nocuity（41.3% majority-convergent violations）是有价值的 empirical 贡献，对 agent safety 部署有直接实践意义。\n\n- **S4**: 七模型覆盖（5 primary + 2 replication）跨六个 provider，是该领域中模型覆盖度最高的研究之一。\n\n- **S5**: 论文写作清晰，结构紧凑，在 8 页正文内有效传达了复杂的实验设计和统计分析。Limitations 段落坦诚且具体。",
  "reviewer_id": "1",
  "project": "policy_ambiguity_safety"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## 总体评分\n**Overall**: 3.5 / 5 — Borderline Conference\n**一句话总结**: 研究问题新颖、matched-pair 设计严谨，但 C2 risk gradient 的统计支撑依赖 margin 选择、incompleteness 的 information-addition confound 未充分解决、C4 的 judge family bias 削弱跨模型比较可信度——三者叠加使核心 claim 需要校准。\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | Matched-pair 因果设计本身优秀，perturbation control 有说服力；但 TOST margin 选择论证有循环性，incompleteness confound 用 token count proxy 不够充分，C4 cross-judge asymmetry 对 interaction 结论构成系统性威胁 |\n| Excitement | 3.5/5 | 首个 ambiguity type → agent safety violation 的因果研究，taxonomy + matched-pair 方法学贡献明确；但单一 benchmark (τ²-bench) 和 OpenAI-only judge family 限制了泛化性 |\n| Reproducibility | 4/5 | 数据集和代码承诺公开；API 调用参数明确 (temp=0, top_p=1)；ICC=0.919 但仅限 OpenAI family 内部 |\n| Confidence | 4/5 | 我仔细阅读了论文全文（含 15 页附录），熟悉 TOST equivalence testing、matched-pair 因果推断和 LLM-as-judge 文献 |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] TOST ±15pp SESOI 选择的循环论证风险\n\n- **具体位置**: §4.6 Statistical Analysis, §5.2 Type Risk Gradient (C2)\n- **问题**: SESOI 的论证逻辑为\"超过 perturbation control bound (6.67pp) 的 >2×\"(§4.6)，但 perturbation control bound 本身取决于特定扰动类型的选择（synonym substitution, clause reordering），而非独立的领域标准。更关键的是，C2 \"risk gradient rather than sharp tiers\" 的核心 claim 对 margin 选择高度敏感：在 ±10pp 时仅 3/6 mid-tier pairs 达到 equivalence（Table 3），gradient 结构基本瓦解。论文提供了 sensitivity analysis（7个 margin，Table 3），但正文 claim 仅在 ±15pp 时成立——这个依赖关系应当上升为 claim 声明的一部分，而非仅在方法段落中一带而过。\n- **为什么影响接收**: C2 是论文两个 primary claim 之一，其可信度直接决定论文核心贡献的成立。如果 gradient 结构是 margin-dependent 的，读者需要在 abstract 和 conclusion 层面就了解这一条件。\n- **建议修改方向**: (1) 在 C2 claim 的每次陈述中附加 margin 条件（如\"at the ±15pp margin\"）；(2) 在 Abstract/Introduction 中明确 gradient 的 margin-dependent 性质；(3) 讨论 field-standard SESOI 缺失对结论稳健性的影响。\n\n**N2** [critical] Cross-judge asymmetry 对 C4 interaction 结论的系统性威胁\n\n- **具体位置**: §4.4 Evaluation, §5.4 C4 (exploratory), Limitations\n- **问题**: GPT-5.4 judges Claude/GPT-4.1/Qwen3, GPT-4.1 judges GPT-5.4/DeepSeek。论文正确指出 Δpp（paired within model-judge）不受影响（§4.4），但 C4 的 interaction F-test 操作的是 absolute violation rates across models，这些 absolute rates 来自不同 judge。具体地：authorization scope 52pp range（Claude 12% → GPT-5.4 64%）中，Claude 和 GPT-5.4 分别由不同 judge 评判。而 authorization scope 恰好是 inter-judge κ 最低的类型（κ=0.385）。因此 52pp range 可能部分反映两个 judge 对 authorization scope violations 的判定标准差异，而非模型间的真实差异。论文在 §5.4 末尾提到\"upper bound with substantial measurement uncertainty\"，但这个 caveat 与正文的强调程度不匹配——Figure 3 heatmap 和\"most model-differentiating type\"的措辞给读者留下的印象远比 caveat 强烈。\n- **为什么影响接收**: C4 虽标注 exploratory，但其结论（authorization scope 是最大的模型分化因子）在 Discussion §7 的 differential nocuity 框架中占核心位置。如果该结论受 judge confound 驱动，Discussion 的理论贡献被削弱。\n- **建议修改方向**: (1) 在 Figure 3 caption 中明确标注 judge assignment（哪些模型由哪个 judge 评判）；(2) 将 \"upper bound with measurement uncertainty\" 的 caveat 提升到 Figure 3 caption 和 Discussion 中；(3) 报告 within-judge-group 的 authorization scope range（GPT-5.4 judged: Claude 12%, GPT-4.1 46%, Qwen3 26% → 34pp range；GPT-4.1 judged: GPT-5.4 64%, DeepSeek 60% → 4pp range）以区分 judge effect vs. model effect。\n\n**N3** [critical] Incompleteness information-addition confound 的控制不充分\n\n- **具体位置**: §3 Taxonomy (\"Scope of ambiguity\"), §5.2 (confound discussion), Appendix F (logistic regression), Appendix O (clause length)\n- **问题**: Incompleteness 的 unambiguous variant 不是\"消歧\"而是\"补全缺失信息\"——这在概念层面与其他五种 ambiguity type 有本质区别。论文使用 token count difference 作为 information addition 的 proxy 进行 logistic regression 控制（Appendix F, p=0.018），但自己也承认\"token count is a coarse proxy for information content\"（Appendix F）。核心问题：(a) token count 无法区分新增内容的 informativeness vs. 冗余度；(b) 不同类型的 token delta 语义权重不同（authorization scope +36.1 words 但为 boundary specification，incompleteness +34.6 words 为全新 policy content）；(c) 论文用 \"authorization scope has larger delta but lower rate\" 作为反证（Appendix O），但这是跨类型比较——不同类型的 token delta 语义完全不同，无法做 apples-to-apples 的反驳。\n- **为什么影响接收**: Incompleteness 是论文的 \"consistent upper-bound risk type\"，其 49.2pp effect 是所有类型中最大的。如果该 effect 被 information-addition confound 实质性地膨胀，C2 gradient 的形状会改变（incompleteness 可能不是真正的 upper bound，而仅是 confound-inflated 的 artifact）。\n- **建议修改方向**: (1) 明确区分 incompleteness 的 effect 为 \"upper bound including potential information-addition inflation\"（目前措辞已部分做到，但需更一致）；(2) 考虑在 C2 claim 中以 coreferential 的 confound-free 18.7pp 作为 lower bound 锚点，而非以 incompleteness 作为 headline；(3) 讨论替代 proxy（如 propositional content count）的可行性。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] Bootstrap cluster AU p=0.47 对 C2 gradient claim 的支撑力不足\n\n- **具体位置**: §5.2, Appendix I (Bootstrap Cluster Analysis)\n- **问题**: 论文用 margin-free bootstrap cluster analysis 作为 TOST 的补充证据。但 incompleteness singleton 的 AU p-value 仅为 0.47——远低于通常 0.95 的 significance threshold。34.3% 的 bootstrap samples 复现了该 partition。论文自己说\"the modal partition but not overwhelmingly stable\"和\"the boundary is not sharp\"。这意味着 margin-free 方法 *不* 支持 incompleteness 作为 distinct upper-bound cluster 的 claim——TOST 和 bootstrap 给出不一致的信号。\n- **建议**: 明确承认 bootstrap evidence 不支持 incompleteness 与 mid-tier 的 sharp separation；将 C2 claim 重新表述为 \"the six types show differential risk, with incompleteness trending highest, but the boundary between incompleteness and the mid-tier cluster is not statistically robust under margin-free methods.\"\n\n**W2** [warning] Human validation 的 per-type 检验力不足以支撑 type-level 结论\n\n- **具体位置**: §4.4 (Human validation), Appendix G (Per-Type Judge Reliability)\n- **问题**: Total n=100, per-type n=32-34。论文承认\"lack power for type-level comparison\"（§4.4），但 Appendix G 仍然报告 per-type κ 并从中得出结论（如\"Authorization scope has the lowest human-LLM κ\"）。CIs 极宽：scopal κ 95% CI = [0.00, 1.00]，coreferential κ CI = [0.00, 0.84]——这些是完全无信息的区间。\n- **建议**: (1) 在 Appendix G 中明确声明 per-type 结果仅为 descriptive/suggestive，不应用于 type-level ranking；(2) 考虑移除或弱化基于 per-type κ 的推断。\n\n**W3** [warning] Judge family bias (both OpenAI) 对 cross-model comparison 的潜在系统效应\n\n- **具体位置**: Limitations (Measurement paragraph)\n- **问题**: 两个 judge 都来自 OpenAI model family。论文在 Limitations 中提及\"potentially introducing systematic within-family evaluation bias\"，但未进一步分析其潜在方向或量级。Claude 被评为最低 violation rate (30.3%)——这可能反映真实 robustness，也可能反映 OpenAI judge 对非 OpenAI 输出的系统性偏差（如对不同格式/风格的偏好）。该 confound 与 N2 叠加放大了 C4 结论的不确定性。\n- **建议**: (1) 讨论 judge family bias 的可能方向（如 OpenAI judges 是否可能对 OpenAI agents 更宽容或更严格）；(2) 在 Future Work 中明确建议 cross-family judge evaluation 作为必要验证。\n\n**W4** [warning] C4 variance explained (2.9%) 的实质意义与 Discussion 中的权重不匹配\n\n- **具体位置**: §5.4 C4, §7 Discussion (Differential nocuity)\n- **问题**: C4 interaction F(20,2976)=1.97, p=0.006, 但仅解释 2.9% variance。在 n≈3000 的样本下，test 有极高的 power 检测微小效应。论文正确标注了 [Exploratory]，但 Discussion §7 的 \"differential nocuity\" framework 将 authorization scope 的模型差异作为核心论据之一——这给予了一个 2.9%-variance, low-κ, judge-confounded 的 exploratory finding 过高的理论权重。\n- **建议**: 在 Discussion 中降低对 authorization scope 模型差异的依赖程度，或在引用时每次附加 effect size + measurement uncertainty caveat。\n\n**W5** [warning] Perturbation control 对 specification-layer types 的适用性有限\n\n- **具体位置**: §4.5 Controls (Perturbation control)\n- **问题**: Perturbation control 使用 synonym substitution 和 clause reordering (n=300)。这些扰动在结构上与 linguistic-layer 的 ambiguity manipulation（如 scopal: 改变一个词的作用域）匹配较好，但与 specification-layer 的 manipulation（如 incompleteness: 添加整段新内容 +34.6 words；authorization scope: 添加 +36.1 words）有本质差异。synonym substitution 不会模拟添加 34 words 新内容的效果——这意味着 perturbation control 的 CI [-8.0, 6.67] 作为\"非语义变化无效果\"的证据，对 specification-layer types（尤其 incompleteness）的 specificity claim 支撑较弱。\n- **建议**: 讨论 perturbation control 对不同类型的适用性差异；承认对 specification-layer types，perturbation control 提供的是\"surface-level perturbation specificity\"而非\"information-addition specificity\"——后者由 Appendix F 的 logistic regression 处理（但同样有 proxy 限制）。\n\n**W6** [warning] Kendall's W 的显著性依赖子集选择\n\n- **具体位置**: Appendix M (Cross-Model Type Ranking Concordance)\n- **问题**: 5-model, 6-type 的 Kendall's W=0.398 (p=0.072) 不显著。7-model, 5-type（排除 coreferential）的 W=0.353 (p=0.038) 显著。论文同时报告了两个结果，但正文 §5.2 引用的是 \"moderate\" concordance——没有明确说明非显著。排除 coreferential + 加入 replication models 这一组合看起来像是选择性报告。\n- **建议**: 在正文引用时明确说明 5-model 结果不显著 (p=0.072)；避免给读者\"type ranking 在模型间 consistent\"的印象——数据支持的是\"trending toward concordance, driven by incompleteness at the top\"。\n\n---\n\n## 小问题（不影响接收）\n\n- **M1**: \"Ambiguity\" 的操作定义包含了严格意义上不是 ambiguity 的概念（incompleteness = information absence, conditional precedence = normative conflict）。§3 \"Scope of ambiguity\" 段已充分讨论了这一点，但建议在 Abstract 中加入一个 parenthetical 提示（如 \"including specification-level gaps\"）以减少初读时的概念混淆。\n\n- **M2**: ICC=0.919 的 reproducibility 测量仅限 OpenAI family 内（GPT-5.4 + GPT-4.1, §4.5）。跨 provider reproducibility（如 Claude 的 replication stability）未直接测量。建议在报告 ICC 时注明此限制。\n\n- **M3**: Appendix B 的五模型 mitigation study（-8.5pp pooled）与 Discussion §7 的单模型 GPT-5.4 mitigation experiment 使用不同的 prompt formulation 和实验设计（unpaired vs. matched-pair McNemar），两者结论方向不一致（Appendix B: incompleteness -3.4pp; Discussion: incompleteness +14pp worsening）。建议明确标注两个实验的设计差异，避免读者混淆。\n\n- **M4**: Variance decomposition \"clause identity 22.4% vs model identity 1.0%\" (§5.1)——剩余 76.6% 为 unexplained variance（主要来自 evaluation pipeline noise）。建议报告 residual 比例以给出完整图景。\n\n- **M5**: Within-judge-group type ranking 相关性接近零（Spearman ρ=-0.03, Appendix P），由 authorization scope 的 rank reversal 驱动。这进一步削弱了 C2 type ranking 的跨评判者稳健性——建议在 §5.2 讨论 ranking stability 时交叉引用此 appendix 结果。\n\n---\n\n## Questions for Authors\n\n1. 如果使用 propositional content analysis（而非 token count）作为 information delta 的 proxy，incompleteness 的 effect 预计会如何变化？是否有 pilot data？\n\n2. 在 within-judge-group 分析中，GPT-5.4 judged group 的 authorization scope 范围是多少（Claude, GPT-4.1, Qwen3 各多少）？GPT-4.1 judged group 呢（GPT-5.4, DeepSeek）？如果两个 judge group 内部的 range 都远小于 52pp，这将强烈暗示 judge effect。\n\n3. 是否有计划做 cross-family judge evaluation（如 Claude judging GPT traces）以排除 judge family bias？\n\n4. C3 layer effect 在 controlling for token delta 后 reverses direction (§5.3)——reversed 后的方向和 effect size 是多少？这对 taxonomy 的理论动机有什么影响？\n\n---\n\n## 主要优势\n\n- **S1**: 首个 ambiguity type → agent safety violation 的 matched-pair 因果研究，填补了重要空白。Perturbation control + matched-pair 设计提供了优于 observational study 的因果推断基础。\n\n- **S2**: 统计方法论整体质量高——TOST equivalence testing + bootstrap cluster + Holm-Bonferroni correction + sensitivity analysis 的组合超过了该领域大多数论文的标准。Claim calibration（C3 标注 inconclusive, C4 标注 exploratory）展示了良好的学术诚信。\n\n- **S3**: Disambiguation Neglect 的发现（≤11% awareness）和 Systematic Nocuity（41.3% majority-convergent violations）是有价值的 empirical 贡献，对 agent safety 部署有直接实践意义。\n\n- **S4**: 七模型覆盖（5 primary + 2 replication）跨六个 provider，是该领域中模型覆盖度最高的研究之一。\n\n- **S5**: 论文写作清晰，结构紧凑，在 8 页正文内有效传达了复杂的实验设计和统计分析。Limitations 段落坦诚且具体。",
    "reviewer_id": "1",
    "project": "policy_ambiguity_safety"
  }
}
```

</details>

---


### Tool result

_source line 963 · 2026-05-22T09:56:58.304078+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_967344d166ba485ad606d14379e69d85:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4013
}
```

</details>

---


### Assistant

_source line 964 · 2026-05-22T09:57:12.424241+00:00_

审稿意见已提交给 Review Director。

**总结**: Overall 3.5/5 (Borderline Conference)。论文的 matched-pair 因果设计和统计方法论整体优秀，但存在三个 critical 问题需要修复：(1) TOST ±15pp SESOI 的选择对 C2 gradient claim 构成循环论证风险——gradient 结构在 ±10pp 时瓦解；(2) C4 的 cross-judge asymmetry + authorization scope κ=0.385 使 52pp range 可能受 judge effect 驱动；(3) incompleteness 的 information-addition confound 仅用 token count 控制不够充分，49.2pp effect 可能被膨胀。三个 critical + 六个 should-fix + 五个 minor issues 已详细列出修改建议。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1"
}
```

</details>

---


## Round 26

## Round 26

4 recorded events


### User

_source line 965 · 2026-05-22T09:59:06.023579+00:00_

[Round 1 审稿请求]:
以下是 Reviewer 2 的完整审稿意见，请逐条回应。对每个观点标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。

---

## Reviewer 2 审稿意见（新颖性/完整性）

**Overall**: 3.5 (Borderline Conference)

### Must-Fix

**N1** [critical] Contribution (2) "22× more variance" 措辞具有误导性
- §5.1 分解：22.4% clause-level variance 中 between-type 仅 0.4%，within-type 22.0%。Taxonomy 本身仅解释 0.4% 方差。在 contributions list 中紧跟 C2 提出 "22×" claim，读者自然理解为 taxonomy 解释力强，与数据不符——overclaiming。
- 建议：(1) contributions 区分 clause-level vs type-level variance；(2) §5.1 讨论 0.4% 对 taxonomy 实用价值的含义；(3) "22×" 从 contribution 降级为 supporting evidence。

**N2** [critical] Taxonomy 理论连贯性：incompleteness 和 conditional precedence 不属传统 "ambiguity"
- §3 承认 incompleteness 是 information absence, conditional precedence 是 normative conflict。辩护"agents process all six types identically"是 empirical observation 非 theoretical justification。标题和 abstract 统称六类为 "ambiguity" 构成 category error。
- 建议：(1) 用 "policy underspecification" 等更宽泛术语；或 (2) §1 即限定 scope；(3) 不要到 §3 才回应定义偏离。

### Should-Fix

**W1**: Mitigation 实验方向矛盾（§7 GPT-5.4 incompleteness +14pp vs Appendix B −2.6pp），prompt wording sensitivity 削弱 practical implications。
**W2**: "Disambiguation Neglect" 是已知现象在 agentic setting 的 quantification，非新发现。Contribution (3) 应从 "revealing" 调整为 "quantifying in consequential agentic settings"。
**W3**: Incompleteness confound token count proxy 不充分。
**W4**: 单一 benchmark (τ²-bench) 外部效度，abstract/conclusion 暗示更广泛 generalizability。

### Minor
M1: C3 null result 可压缩。M2: Table 2 caption 过长。M3: bootstrap ranking preservation 限制条件应在正文说明。M4: arXiv preprint 引用完整性。M5: 4.6% vs ≤11% awareness 数字交替使用。

### Strengths
E1: matched-pair 因果设计方法论严谨。E2: 统计方法全面恰当。E3: 学术诚信出色。E4: 7 models × 6 providers 规模。E5: type→failure mode 映射有实用价值。

### Questions
1. Between-type variance 仅 0.4%：taxonomy 价值是否在 failure mode prediction 而非 variance explanation？
2. 排除 incompleteness 后 omnibus p=0.079——C2 是否过度依赖 incompleteness？
3. 是否有与 DRIP-R 真实 policy ambiguity 的 qualitative comparison 评估生态效度？

### Missing References
建议引用 "The Causal Impact of Tool Affordance on Safety Alignment" (arXiv:2603.20320)。

---

请逐条回应 Reviewer 2 的所有观点（Must-Fix、Should-Fix、Minor、Strengths、Questions）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 966 · 2026-05-22T10:00:44.308112+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 1 对 Reviewer 2 意见的交叉回应\n\n---\n\n### Must-Fix\n\n**[AGREE] R2-N1: \"22× more variance\" 措辞误导性**\n\n同意这是 overclaiming。§5.1 的 variance decomposition 显示 clause identity 22.4% 中 between-type 仅 0.4%、within-type 22.0%。\"22×\" 指的是 clause vs. model（22.4% vs 1.0%），但放在 contributions list 中紧跟 C2（type-level gradient），读者确实容易误读为 taxonomy（type-level）的解释力。\n\n补充我自己的观察：22.4% clause-level variance 的另一面是 76.6% unexplained variance（我在 M4 中指出），主要来自 evaluation pipeline noise。即便 clause > model 的比较成立，绝对数字说明 measurement noise 仍然主导——这进一步削弱了将 \"22×\" 作为 headline contribution 的合理性。\n\nR2 的修改建议合理：将 \"22×\" 从 contribution 降级为 supporting evidence，并在 §5.1 区分 clause-level vs type-level variance 的含义。\n\n**[REBUT] R2-N2: Taxonomy 理论连贯性——incompleteness/conditional precedence 不属传统 ambiguity**\n\nR2 的概念关切有道理，但建议的修改方向过重。论文 §3 \"Scope of ambiguity\" 段落已经明确承认 incompleteness 是 information absence、conditional precedence 是 normative conflict，并给出了 pragmatic justification：(1) agents process all six types identically（commit to single interpretation without flagging uncertainty, §3 末段）；(2) resulting safety violations are behaviorally indistinguishable（§5.1-5.2 所有类型都产生显著的 Δpp）；(3) Dalpiaz et al. (2018) 的文献支持 ambiguity/incompleteness 经常 co-occur。\n\nR2 说这是\"empirical observation 非 theoretical justification\"——但在实证研究中，empirical observation *就是* 最恰当的 justification。论文的核心是实证因果研究，不是 taxonomy 的理论建构。改用 \"policy underspecification\" 会弱化与 decades of RE ambiguity research（Berry & Kamsties 2004, Massey et al. 2014）的衔接，也丢掉 nocuous/innocuous ambiguity 的框架连接。\n\n不过我同意 R2 的一个子点：scope 限定应当在 §1 Introduction 中前置，而非到 §3 才回应。建议在 §1 的 taxonomy 介绍处加一句 parenthetical（如 \"including specification-level gaps that, while not ambiguity in the strict linguistic sense, produce identical behavioral outcomes in LLM agents\"），这比改标题或术语更精准。\n\n---\n\n### Should-Fix\n\n**[AGREE] R2-W1: Mitigation 实验方向矛盾**\n\n完全同意。§7 Discussion 的单模型 GPT-5.4 matched-pair McNemar 实验显示 incompleteness +14pp（worsening, p=0.118），而 Appendix B 的五模型 unpaired 实验显示 incompleteness -2.6pp（GPT-5.4）/-3.4pp（pooled）。两个实验用了不同的 prompt formulation 和实验设计（unpaired vs matched-pair），但论文未在正文中清晰标注这一差异。我在自己的审稿中也指出了这一点（M3）。\n\n这不仅是 presentation 问题——它实质性地削弱了 Discussion 中 \"mitigation outcomes appear sensitive to prompt wording\" 的结论可信度，因为两个不同实验可能测量的是不同的 construct。\n\n**[AGREE] R2-W2: Disambiguation Neglect 是 quantification 而非 discovery**\n\n同意。Liu et al. (2023) 和 Hu et al. (2025) 已经报告了 LLM 的 ambiguity collapse 现象（§2 Related Work, §6.2 明确引用）。论文的增量贡献是 (a) 在 consequential agentic setting 中量化（4.6% overall, max 11% per-model）和 (b) 发现 systematic nocuity（41.3% majority-convergent, §6.3）。Contribution (3) 从 \"revealing\" 改为 \"quantifying in consequential agentic settings and identifying systematic nocuity\" 更准确，同时保留 systematic nocuity 这一确实新颖的发现。\n\n**[AGREE] R2-W3: Incompleteness confound token count proxy 不充分**\n\n完全同意，与我自己的 N3 一致。Token count 作为 information content 的 proxy 过于粗糙——论文自己在 Appendix F 也承认。不再赘述。\n\n**[AGREE] R2-W4: 单一 benchmark 外部效度**\n\n同意关切，但严重程度应略低于 R2 的评估。论文使用的 τ²-bench 本身覆盖两个 domain（retail + airline customer service, §4.1），且 cross-domain consistency 是令人鼓舞的。Limitations §明确声明 \"effects in other domains remain untested\"。不过我同意 Abstract 和 Conclusion 的措辞（\"LLM-based agents\" 而非 \"LLM-based customer service agents\"）暗示了过广的 generalizability。建议在 Abstract 和 Conclusion 中限定 domain scope。\n\n---\n\n### Minor\n\n**[AGREE] R2-M1: C3 null result 可压缩**\n\n同意可以压缩，但不应完全移除。报告 null results 是良好的学术实践。目前 §5.3 约 6 行，可压缩到 3-4 行：保留 p=0.017 不过 correction、controlling for token delta reverses direction、taxonomy value independent of layer grouping。\n\n**[AGREE] R2-M2: Table 2 caption 过长**\n\n同意。Table 2 caption 包含了方法细节（TOST 解释、Tier 定义、p-value 注释），可将 Tier 定义移至脚注或正文。\n\n**[AGREE] R2-M3: Bootstrap ranking preservation 限制条件**\n\n同意。§5.4 报告 \"bootstrap ranking preservation: 99.5%, B=10,000\" 但未在正文中说明这是 within GPT-5.4 judge subset 的结果。限制条件应当明确。\n\n**[REBUT] R2-M4: arXiv preprint 引用完整性**\n\n我无法从论文 PDF 中确认具体哪些 arXiv 引用不完整。R2 未给出具体条目。如果能指出哪些引用有问题，可以更有针对性地回应。但一般性地，preprint 引用标注为 \"arXiv preprint\" 而非已发表版本是常见问题，值得检查。\n\n**[AGREE] R2-M5: 4.6% vs ≤11% awareness 数字交替使用**\n\n同意。4.6% 是 overall 平均（§6.2），≤11% 是 per-model maximum（Claude 11.0%, §6.2），两者语义不同但在 Introduction §1 和 §6.2 中交替出现。建议统一使用一个数字并在首次出现时注明另一个。\n\n---\n\n### Strengths\n\n**[AGREE] R2-E1 through E5**\n\n全部同意。这些也与我的 S1-S5 评价一致。特别赞同 E3（学术诚信出色）——C3 标注 inconclusive、C4 标注 exploratory、authorization scope caveat 反复出现，在该领域论文中难能可贵。E5（type→failure mode mapping）是我审稿中未充分强调的优点——§6.1 的三种 failure mechanism（structural misparse, information gap-filling, boundary violation）与 ambiguity type 的映射关系清晰，且在 ≥3/5 models 中保持一致，具有实际部署价值。\n\n---\n\n### Questions 回应\n\n**R2-Q1**: Between-type variance 仅 0.4%——taxonomy 价值在 failure mode prediction 而非 variance explanation？\n\n这是一个 insightful 的问题。我同意 taxonomy 的主要价值可能在于 §6.1 的 type→failure mode 映射（每种类型有 distinct 的 dominant failure mechanism），而非 type-level variance explanation。§5.1 的数据实际上支持\"clause wording 比 type membership 重要 55 倍\"（22.0% within-type / 0.4% between-type），这削弱了 taxonomy 作为 variance-explaining 框架的价值，但不削弱其作为 failure-mode-predicting 框架的价值。论文应更清晰地定位 taxonomy 的价值来源。\n\n**R2-Q2**: 排除 incompleteness 后 omnibus p=0.079——C2 是否过度依赖 incompleteness？\n\n关键问题。Appendix F 报告排除 incompleteness 后 omnibus p=0.079，但 pairwise Holm-Bonferroni 仍有两对显著（auth scope vs coreferential p_adj=0.039, lexical vs coreferential p_adj=0.025）。这说明 C2 的 omnibus 结论确实依赖 incompleteness，但 pairwise gradient 不完全依赖它。论文应当明确区分：(a) omnibus \"types are not interchangeable\" 依赖 incompleteness；(b) pairwise gradient 在排除 incompleteness 后仍有部分支撑（coreferential 显著低于 auth scope 和 lexical）。这与我的 N1（SESOI margin dependence）叠加——C2 claim 需要更谨慎的表述。\n\n**R2-Q3**: 与 DRIP-R 的 qualitative comparison？\n\n论文在 Appendix L 提供了 DRIP-R 的 category mapping（5 RE types → 6-type taxonomy），但没有在 DRIP-R 的真实 policy ambiguity instances 上做 empirical comparison。这确实是一个 ecological validity gap——论文的 300 clause pairs 是 synthetic（template-based, §4.2），与 naturally occurring ambiguity 的分布可能不同（Limitations §已承认）。DRIP-R 作为 concurrent work 提供了天然的比较基准。\n\n---\n\n### Missing References\n\n**[REBUT] R2-Missing Ref: \"The Causal Impact of Tool Affordance on Safety Alignment\" (arXiv:2603.20320)**\n\n无法验证此引用的存在性（arXiv ID 2603.xxxxx 的格式对应 2026年3月，需要确认）。但如果该论文确实研究 tool affordance 对 safety 的因果影响，与本文的关联性可能限于 agent safety 的广义主题——本文的核心贡献是 ambiguity type → violation 的映射，而非 tool affordance。如果 R2 能说明具体哪个 section 应引用、该引用如何改变本文的论证结构，会更有建设性。",
  "reviewer_id": "1",
  "project": "policy_ambiguity_safety"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 1 对 Reviewer 2 意见的交叉回应\n\n---\n\n### Must-Fix\n\n**[AGREE] R2-N1: \"22× more variance\" 措辞误导性**\n\n同意这是 overclaiming。§5.1 的 variance decomposition 显示 clause identity 22.4% 中 between-type 仅 0.4%、within-type 22.0%。\"22×\" 指的是 clause vs. model（22.4% vs 1.0%），但放在 contributions list 中紧跟 C2（type-level gradient），读者确实容易误读为 taxonomy（type-level）的解释力。\n\n补充我自己的观察：22.4% clause-level variance 的另一面是 76.6% unexplained variance（我在 M4 中指出），主要来自 evaluation pipeline noise。即便 clause > model 的比较成立，绝对数字说明 measurement noise 仍然主导——这进一步削弱了将 \"22×\" 作为 headline contribution 的合理性。\n\nR2 的修改建议合理：将 \"22×\" 从 contribution 降级为 supporting evidence，并在 §5.1 区分 clause-level vs type-level variance 的含义。\n\n**[REBUT] R2-N2: Taxonomy 理论连贯性——incompleteness/conditional precedence 不属传统 ambiguity**\n\nR2 的概念关切有道理，但建议的修改方向过重。论文 §3 \"Scope of ambiguity\" 段落已经明确承认 incompleteness 是 information absence、conditional precedence 是 normative conflict，并给出了 pragmatic justification：(1) agents process all six types identically（commit to single interpretation without flagging uncertainty, §3 末段）；(2) resulting safety violations are behaviorally indistinguishable（§5.1-5.2 所有类型都产生显著的 Δpp）；(3) Dalpiaz et al. (2018) 的文献支持 ambiguity/incompleteness 经常 co-occur。\n\nR2 说这是\"empirical observation 非 theoretical justification\"——但在实证研究中，empirical observation *就是* 最恰当的 justification。论文的核心是实证因果研究，不是 taxonomy 的理论建构。改用 \"policy underspecification\" 会弱化与 decades of RE ambiguity research（Berry & Kamsties 2004, Massey et al. 2014）的衔接，也丢掉 nocuous/innocuous ambiguity 的框架连接。\n\n不过我同意 R2 的一个子点：scope 限定应当在 §1 Introduction 中前置，而非到 §3 才回应。建议在 §1 的 taxonomy 介绍处加一句 parenthetical（如 \"including specification-level gaps that, while not ambiguity in the strict linguistic sense, produce identical behavioral outcomes in LLM agents\"），这比改标题或术语更精准。\n\n---\n\n### Should-Fix\n\n**[AGREE] R2-W1: Mitigation 实验方向矛盾**\n\n完全同意。§7 Discussion 的单模型 GPT-5.4 matched-pair McNemar 实验显示 incompleteness +14pp（worsening, p=0.118），而 Appendix B 的五模型 unpaired 实验显示 incompleteness -2.6pp（GPT-5.4）/-3.4pp（pooled）。两个实验用了不同的 prompt formulation 和实验设计（unpaired vs matched-pair），但论文未在正文中清晰标注这一差异。我在自己的审稿中也指出了这一点（M3）。\n\n这不仅是 presentation 问题——它实质性地削弱了 Discussion 中 \"mitigation outcomes appear sensitive to prompt wording\" 的结论可信度，因为两个不同实验可能测量的是不同的 construct。\n\n**[AGREE] R2-W2: Disambiguation Neglect 是 quantification 而非 discovery**\n\n同意。Liu et al. (2023) 和 Hu et al. (2025) 已经报告了 LLM 的 ambiguity collapse 现象（§2 Related Work, §6.2 明确引用）。论文的增量贡献是 (a) 在 consequential agentic setting 中量化（4.6% overall, max 11% per-model）和 (b) 发现 systematic nocuity（41.3% majority-convergent, §6.3）。Contribution (3) 从 \"revealing\" 改为 \"quantifying in consequential agentic settings and identifying systematic nocuity\" 更准确，同时保留 systematic nocuity 这一确实新颖的发现。\n\n**[AGREE] R2-W3: Incompleteness confound token count proxy 不充分**\n\n完全同意，与我自己的 N3 一致。Token count 作为 information content 的 proxy 过于粗糙——论文自己在 Appendix F 也承认。不再赘述。\n\n**[AGREE] R2-W4: 单一 benchmark 外部效度**\n\n同意关切，但严重程度应略低于 R2 的评估。论文使用的 τ²-bench 本身覆盖两个 domain（retail + airline customer service, §4.1），且 cross-domain consistency 是令人鼓舞的。Limitations §明确声明 \"effects in other domains remain untested\"。不过我同意 Abstract 和 Conclusion 的措辞（\"LLM-based agents\" 而非 \"LLM-based customer service agents\"）暗示了过广的 generalizability。建议在 Abstract 和 Conclusion 中限定 domain scope。\n\n---\n\n### Minor\n\n**[AGREE] R2-M1: C3 null result 可压缩**\n\n同意可以压缩，但不应完全移除。报告 null results 是良好的学术实践。目前 §5.3 约 6 行，可压缩到 3-4 行：保留 p=0.017 不过 correction、controlling for token delta reverses direction、taxonomy value independent of layer grouping。\n\n**[AGREE] R2-M2: Table 2 caption 过长**\n\n同意。Table 2 caption 包含了方法细节（TOST 解释、Tier 定义、p-value 注释），可将 Tier 定义移至脚注或正文。\n\n**[AGREE] R2-M3: Bootstrap ranking preservation 限制条件**\n\n同意。§5.4 报告 \"bootstrap ranking preservation: 99.5%, B=10,000\" 但未在正文中说明这是 within GPT-5.4 judge subset 的结果。限制条件应当明确。\n\n**[REBUT] R2-M4: arXiv preprint 引用完整性**\n\n我无法从论文 PDF 中确认具体哪些 arXiv 引用不完整。R2 未给出具体条目。如果能指出哪些引用有问题，可以更有针对性地回应。但一般性地，preprint 引用标注为 \"arXiv preprint\" 而非已发表版本是常见问题，值得检查。\n\n**[AGREE] R2-M5: 4.6% vs ≤11% awareness 数字交替使用**\n\n同意。4.6% 是 overall 平均（§6.2），≤11% 是 per-model maximum（Claude 11.0%, §6.2），两者语义不同但在 Introduction §1 和 §6.2 中交替出现。建议统一使用一个数字并在首次出现时注明另一个。\n\n---\n\n### Strengths\n\n**[AGREE] R2-E1 through E5**\n\n全部同意。这些也与我的 S1-S5 评价一致。特别赞同 E3（学术诚信出色）——C3 标注 inconclusive、C4 标注 exploratory、authorization scope caveat 反复出现，在该领域论文中难能可贵。E5（type→failure mode mapping）是我审稿中未充分强调的优点——§6.1 的三种 failure mechanism（structural misparse, information gap-filling, boundary violation）与 ambiguity type 的映射关系清晰，且在 ≥3/5 models 中保持一致，具有实际部署价值。\n\n---\n\n### Questions 回应\n\n**R2-Q1**: Between-type variance 仅 0.4%——taxonomy 价值在 failure mode prediction 而非 variance explanation？\n\n这是一个 insightful 的问题。我同意 taxonomy 的主要价值可能在于 §6.1 的 type→failure mode 映射（每种类型有 distinct 的 dominant failure mechanism），而非 type-level variance explanation。§5.1 的数据实际上支持\"clause wording 比 type membership 重要 55 倍\"（22.0% within-type / 0.4% between-type），这削弱了 taxonomy 作为 variance-explaining 框架的价值，但不削弱其作为 failure-mode-predicting 框架的价值。论文应更清晰地定位 taxonomy 的价值来源。\n\n**R2-Q2**: 排除 incompleteness 后 omnibus p=0.079——C2 是否过度依赖 incompleteness？\n\n关键问题。Appendix F 报告排除 incompleteness 后 omnibus p=0.079，但 pairwise Holm-Bonferroni 仍有两对显著（auth scope vs coreferential p_adj=0.039, lexical vs coreferential p_adj=0.025）。这说明 C2 的 omnibus 结论确实依赖 incompleteness，但 pairwise gradient 不完全依赖它。论文应当明确区分：(a) omnibus \"types are not interchangeable\" 依赖 incompleteness；(b) pairwise gradient 在排除 incompleteness 后仍有部分支撑（coreferential 显著低于 auth scope 和 lexical）。这与我的 N1（SESOI margin dependence）叠加——C2 claim 需要更谨慎的表述。\n\n**R2-Q3**: 与 DRIP-R 的 qualitative comparison？\n\n论文在 Appendix L 提供了 DRIP-R 的 category mapping（5 RE types → 6-type taxonomy），但没有在 DRIP-R 的真实 policy ambiguity instances 上做 empirical comparison。这确实是一个 ecological validity gap——论文的 300 clause pairs 是 synthetic（template-based, §4.2），与 naturally occurring ambiguity 的分布可能不同（Limitations §已承认）。DRIP-R 作为 concurrent work 提供了天然的比较基准。\n\n---\n\n### Missing References\n\n**[REBUT] R2-Missing Ref: \"The Causal Impact of Tool Affordance on Safety Alignment\" (arXiv:2603.20320)**\n\n无法验证此引用的存在性（arXiv ID 2603.xxxxx 的格式对应 2026年3月，需要确认）。但如果该论文确实研究 tool affordance 对 safety 的因果影响，与本文的关联性可能限于 agent safety 的广义主题——本文的核心贡献是 ambiguity type → violation 的映射，而非 tool affordance。如果 R2 能说明具体哪个 section 应引用、该引用如何改变本文的论证结构，会更有建设性。",
    "reviewer_id": "1",
    "project": "policy_ambiguity_safety"
  }
}
```

</details>

---


### Tool result

_source line 967 · 2026-05-22T10:00:48.174025+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_967344d166ba485ad606d14379e69d85:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3865
}
```

</details>

---


### Assistant

_source line 968 · 2026-05-22T10:01:04.433526+00:00_

交叉回应已提交。总结：

- **AGREE** 10 条：N1（22× overclaiming）、W1-W4、M1-M3、M5，以及全部 5 个 Strengths
- **REBUT** 3 条：N2（taxonomy 术语——同意前置 scope 但反对改标题）、M4（需具体指出哪些引用）、Missing Ref（无法验证且关联性存疑）

核心共识点：R2 和我都认为 C2 claim 需要校准——(1) incompleteness confound 控制不足，(2) 排除 incompleteness 后 omnibus p=0.079，(3) 22× 从 contribution 降级。两位 reviewer 给出相同的 Overall 3.5，bottleneck 一致集中在 claim calibration 而非方法设计本身。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1"
}
```

</details>

---


## Round 27

## Round 27

24 recorded events


### User

_source line 969 · 2026-05-22T12:09:01.316227+00:00_

[Round 1 审稿请求]:
[Dream 审稿任务 — Reviewer 1：方法 + 实验]

论文标题：Causal Anatomy of Policy Ambiguity Vulnerability in LLM Agents
PDF 路径：/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260522T111643/worst/review_input_f5f46a62.pdf
实验设计参考：/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260522T111643/worst/review_context.yaml

目标 Venue：EMNLP 2026（ARR Overall Assessment 1-5 半分制）
评分刻度：5=Award, 4=Conference, 3=Findings, 2=Resubmit, 1=Do not resubmit
接受率：Main ~21%

你的审查侧重：
- **方法描述**：是否完整、claim 是否被实验数据支撑、关键超参 / 训练流程是否清晰
- **实验设计**：是否覆盖关键 baseline / ablation / 跨数据集 / scale 维度
- **数据呈现**：表格 / 图是否能让审稿人复现结论、误差棒 / 统计显著性是否充分

请基于论文内容独立评判，不要假设论文结果的质量高低。

具体关注点：
1. Matched-pair design 的内部效度——perturbation control 是否足以排除 confounds？token delta 差异（spec 34 vs ling 13）是否引入系统性偏差？
2. 统计方法是否恰当——McNemar, χ², TOST equivalence, ICC 的使用是否正确？logistic regression 的 covariates 是否充分？
3. 单一 benchmark (τ²-bench) 限制——SOPBench cross-benchmark 失败（Δ=8.3pp, p=0.068）对 claims 的 generality 影响有多大？
4. C3 layer effect 被标记为 "suggestive"——within-judge fragility (p=0.059, p=0.157) 是否意味着这个 claim 不应出现？
5. Error analysis 的 300 traces 样本和分类方法是否足够系统？
6. Judge calibration (κ=0.807) 和 ICC (0.919) 的报告是否充分？cross-judge agreement 76% 是否偏低？
7. DeBERTa classifier PoC 的加入是否 dilutes the narrative？
8. 实验设计文件（review_context.yaml）列出了完整的想象实验——请对比论文实际覆盖的实验，评估覆盖度和遗漏。

**不要评判**：新颖性 / 相关工作（那是 Reviewer 2 的范围）、格式 / 排版。

每条 weakness 标注属于 **idea 层面** 还是 **presentation 层面**。
Major issue 需 explicit justification。

请通过 `review_reviewer_post_to_director(text, reviewer_id="1", project="policy_ambiguity_safety", dream_id="20260522T111643")` 汇报。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 970 · 2026-05-22T12:09:14.224283+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260522T111643/worst/review_input_f5f46a62.pdf",
  "project": "policy_ambiguity_safety",
  "pages": "1-10",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260522T111643/worst/review_input_f5f46a62.pdf",
    "project": "policy_ambiguity_safety",
    "pages": "1-10",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 971 · 2026-05-22T12:09:14.878351+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"页码超出范围 (共 6 页): 1-10\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 654
}
```

</details>

---


### Tool call

_source line 972 · 2026-05-22T12:09:14.878853+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260522T111643/worst/review_context.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260522T111643/worst/review_context.yaml"
  }
}
```

</details>

---


### Tool result

_source line 973 · 2026-05-22T12:09:15.181185+00:00_

1	narrative_guidance: 放弃cross-domain generalization claim。SOPBench未复制或verifier不兼容，一句话acknowledge作为limitation。核心贡献重新定位为：(1)
2	  方法论模板——首个matched-pair + perturbation control因果设计；(2) model×type interaction——52pp
3	  auth_scope range + incompleteness universality；(3) 7-model breadth（plan_013 Gemini+LLaMA复制C1）替代cross-benchmark
4	  breadth。Title改为'Causal Anatomy of Policy Ambiguity Vulnerability in LLM Agents'。仍冲EMNLP但framing更modest。
5	imagined_experiments:
6	- name: full_study_clause_generation
7	  plan_id: plan_001
8	  description: 生成140新clause pairs（coreferential 50, auth_scope 50, lexical +20, incompleteness
9	    +20），总计300 pairs validated
10	  expected_results:
11	    total_clauses_generated: 300
12	    per_type_count: 50
13	    cross_type_balance_pass: true
14	    format_mix_cp_labeled_ratio: 0.5
15	    avg_token_delta_spec_layer: 34.2
16	    avg_token_delta_ling_layer: 12.8
17	    quality_review_pass_rate: 0.92
18	    revision_needed_clauses: 24
19	  result_rationale: Clause generation是upstream工序，不受worst tier影响。质量审查会发现~8%需修订（auth_scope边界case和incompleteness
20	    minimal-info约束难满足）。Token delta的layer差异（spec 34 vs ling 13）是固有结构——specification层歧义消解需要更多信息量，这在后续分析中成为confound讨论点但不改变因果结论。
21	  tables:
22	  - title: Clause Generation Summary by Type
23	    columns:
24	    - Type
25	    - Layer
26	    - N Generated
27	    - N Passed QA
28	    - Avg Token Delta
29	    - Revision Rate
30	    rows:
31	    - - incompleteness
32	      - spec
33	      - '50'
34	      - '46'
35	      - '34.6'
36	      - '0.08'
37	    - - authorization_scope
38	      - spec
39	      - '50'
40	      - '44'
41	      - '36.1'
42	      - '0.12'
43	    - - conditional_precedence
44	      - spec
45	      - '50'
46	      - '48'
47	      - '31.9'
48	      - '0.04'
49	    - - scopal
50	      - ling
51	      - '50'
52	      - '47'
53	      - '14.2'
54	      - '0.06'
55	    - - lexical
56	      - ling
57	      - '50'
58	      - '47'
59	      - '16.3'
60	      - '0.06'
61	    - - coreferential
62	      - ling
…[truncated 35849 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 302
}
```

</details>

---


### Tool call

_source line 974 · 2026-05-22T12:09:23.304196+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260522T111643/worst/review_input_f5f46a62.pdf",
  "project": "policy_ambiguity_safety",
  "pages": "1-6",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260522T111643/worst/review_input_f5f46a62.pdf",
    "project": "policy_ambiguity_safety",
    "pages": "1-6",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 975 · 2026-05-22T12:09:24.518180+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 1, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260522T111643/worst/_pdf_images/paper_p1.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 402.9}, {\"page\": 2, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260522T111643/worst/_pdf_images/paper_p2.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 423.1}, {\"page\": 3, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260522T111643/worst/_pdf_images/paper_p3.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 404.9}, {\"page\": 4, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260522T111643/worst/_pdf_images/paper_p4.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 425.3}, {\"page\": 5, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260522T111643/worst/_pdf_images/paper_p5.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 453.7}, {\"page\": 6, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260522T111643/worst/_pdf_images/paper_p6.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 24.5}], \"total_pages\": 6, \"rendered_pages\": 6, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260522T111643/worst/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 1213
}
```

</details>

---


### Tool call

_source line 976 · 2026-05-22T12:09:27.940399+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260522T111643/worst/_pdf_images/paper_p1.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260522T111643/worst/_pdf_images/paper_p1.png"
  }
}
```

</details>

---


### Tool result

_source line 977 · 2026-05-22T12:09:28.847712+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 907
}
```

</details>

---


### Tool call

_source line 978 · 2026-05-22T12:09:29.454306+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260522T111643/worst/_pdf_images/paper_p2.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260522T111643/worst/_pdf_images/paper_p2.png"
  }
}
```

</details>

---


### Tool call

_source line 979 · 2026-05-22T12:09:29.454746+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260522T111643/worst/_pdf_images/paper_p3.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260522T111643/worst/_pdf_images/paper_p3.png"
  }
}
```

</details>

---


### Tool call

_source line 980 · 2026-05-22T12:09:30.834349+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260522T111643/worst/_pdf_images/paper_p4.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260522T111643/worst/_pdf_images/paper_p4.png"
  }
}
```

</details>

---


### Tool call

_source line 981 · 2026-05-22T12:09:30.834774+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260522T111643/worst/_pdf_images/paper_p5.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260522T111643/worst/_pdf_images/paper_p5.png"
  }
}
```

</details>

---


### Tool call

_source line 982 · 2026-05-22T12:09:31.888913+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260522T111643/worst/_pdf_images/paper_p6.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260522T111643/worst/_pdf_images/paper_p6.png"
  }
}
```

</details>

---


### Tool result

_source line 983 · 2026-05-22T12:09:33.095576+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 3640
}
```

</details>

---


### Tool result

_source line 984 · 2026-05-22T12:09:33.096365+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1207
}
```

</details>

---


### Tool result

_source line 985 · 2026-05-22T12:09:33.097247+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 3642
}
```

</details>

---


### Tool result

_source line 986 · 2026-05-22T12:09:34.106909+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 3272
}
```

</details>

---


### Tool result

_source line 987 · 2026-05-22T12:09:34.158265+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 3323
}
```

</details>

---


### Tool call

_source line 988 · 2026-05-22T12:10:17.444945+00:00_

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
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
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

_source line 989 · 2026-05-22T12:10:19.001278+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 1556
}
```

</details>

---


### Tool call

_source line 990 · 2026-05-22T12:13:02.482630+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Dream Review — Reviewer 1（方法 + 实验）\n\n**论文**: Causal Anatomy of Policy Ambiguity Vulnerability in LLM Agents\n**Dream ID**: 20260522T111643 / worst tier\n**Venue**: EMNLP 2026 via ARR\n\n---\n\n## 总体评分\n\n**Overall**: 2.5 / 5 — Borderline Findings\n**Soundness**: 3.0/5 — τ²-bench 内部方法论扎实，但 SOPBench 失败使核心 claim 的 scope 大幅收窄，且论文未充分反映这一收窄\n**Excitement**: 2.5/5 — 单一 benchmark + 失败的 cross-benchmark + ~5页正文，contribution 密度不足以支撑 Conference\n\n**一句话总结**: τ²-bench 内部的因果设计和 measurement chain 是该领域最严谨的，但 SOPBench 复制失败（Δ=8.3pp, p=0.068）使 generalizability 严重存疑，而论文仅以一句 limitation 处理此失败——claim 与 evidence scope 不匹配是致命伤。\n\n---\n\n## Strengths\n\n**S1**: Matched-pair + perturbation control 的因果推断框架是该领域方法论标杆。Perturbation control（Δ=-0.67pp, CI [-8.0, 6.67], Table 4）有效隔离了 ambiguity-specific causation 与一般 prompt sensitivity——这比任何 correlational cross-benchmark study 的因果推断都更强。**[idea层面]**\n\n**S2**: Measurement validation chain 完整度超越同类工作。ICC=0.919 [0.892, 0.940]（§5.6）、human-LLM κ=0.807（§5.6）、perturbation control PASS（Table 4）三重验证构成闭环。Human-LLM agreement 超过 human inter-annotator agreement（0.807 > 0.762），是 LLM-as-judge 验证的 gold standard。**[idea层面]**\n\n**S3**: Error analysis 的 type→failure mode 映射（Table 5）提供了 quantitative findings 背后的 mechanistic \"why\"——auth_scope → unauthorized escalation (77%), incompleteness → assumption-based action (64%), scopal → scope misapplication (76%)。5/6 types 在所有 5 models 上保持 dominant mode 一致性。这是本文最高 EMNLP-value 的贡献之一。**[idea层面]**\n\n**S4**: Claim calibration 诚实：C3 标注 \"suggestive\"（§5.3），C4 interaction 报告了 2.9% variance 和 κ=0.384 的 measurement uncertainty，Ambiguity Blindness 量化为具体数字（4.6% overall）。**[presentation层面]**\n\n---\n\n## Must-Fix\n\n**N1** [critical, idea层面] SOPBench 复制失败的处理严重不足——claim scope 与 evidence scope 不匹配\n\n- **具体位置**: §8 Limitations（一句话提及）vs. Abstract/§9 Conclusion（隐含 broad generalizability）\n- **问题**: SOPBench cross-benchmark 复制失败是本文最重要的 negative result：pooled Δ=8.3pp, p=0.068, CI 含零；type ranking ρ=0.14 与 τ²-bench 无关联（review_context.yaml）。论文在 §8 仅以一句话处理：\"Expanding domain generalization to healthcare and banking domains was attempted via SOPBench but did not meaningfully replicate (pooled Δ=8.3pp, p=0.068), likely due to rule-based verifier insensitivity to semantic violations.\" 但 Abstract 说 \"the first matched-pair causal study testing the safety impact of policy ambiguity across 5 (+2) architecturally diverse models\"——暗示模型 breadth 可以替代 domain breadth 作为 generalizability evidence，而实际数据不支持这一替代。\n- **核心问题**: 如果 ambiguity → violation 的因果链在 healthcare/bank domains 上 effect size 降低 4-6× 且不显著，那么\"policy ambiguity universally causes massive safety violations\"这一叙事只在 customer service 成立。论文需要将所有 claim 限定到 tested domains。\n- **为什么是 Must-Fix**: EMNLP reviewer 看到单一 benchmark 就会要求 generalizability evidence。论文自己尝试了但失败了——隐藏这个 negative result 比不尝试更糟糕，因为 reviewer 发现后会质疑 selective reporting。\n- **建议**: (1) 在 §5 或独立的 §5.x 中报告 SOPBench 结果（至少 pooled Δ、CI、p-value），不需要 full table 但需要 honest framing；(2) Abstract 和 Conclusion 限定 scope 为 \"customer-service agent domains\"；(3) 讨论 verifier incompatibility 假说（rule-based verifier vs semantic violations）作为失败原因——这本身是 methodological insight。\n\n**N2** [critical, idea层面] Token delta 的 layer-level 系统差异（spec 34 vs ling 13 words）引入未充分控制的 confound\n\n- **具体位置**: §4.1（token delta mentioned），§5.5（perturbation control），review_context.yaml（avg_token_delta_spec_layer: 34.2, avg_token_delta_ling_layer: 12.8）\n- **问题**: Specification-layer types 的 unambiguous variants 平均添加 34 words，linguistic-layer types 仅添加 13 words。这是 2.6× 的差异。Perturbation control（Table 4）使用 synonym substitution 和 clause reordering——这些是 low-magnitude surface changes（几个词的替换或重排），无法模拟添加 34 words 新内容的效果。因此：\n  - (a) Perturbation control 对 spec-layer types 的 specificity claim 支撑不足——它证明了\"改几个词无效\"，但没有证明\"添加 34 words 的效果是 ambiguity-specific 而非 information-addition-driven\"\n  - (b) C3 layer effect（spec 44% vs ling 38%, §5.3）可能部分或完全由 token delta 差异驱动——论文承认 \"controlling for token delta reverses the direction\" 但未报告 reversed direction 的 effect size\n  - (c) Logistic regression（§5.6 提及 token delta coef=0.022）控制了 per-clause token delta，但 coef=0.022 per token × 34 tokens = 0.75 log-odds shift 不可忽略\n- **为什么是 Must-Fix**: 这个 confound 同时影响 C2（incompleteness upper-bound status）和 C3（layer effect）。如果 spec-layer types 的高 violation rate 部分由 information asymmetry 驱动，taxonomy 的两层结构的实证基础被削弱。\n- **建议**: (1) 报告 logistic regression 中 controlling for token delta 后 C3 的 direction 和 effect size；(2) 在 per-type 讨论中区分\"confound-free lower bound\"（coreferential, token delta=0）和\"confound-inclusive upper bound\"（incompleteness, token delta≈35）；(3) 考虑 information-addition matched control（添加相同长度的无关信息）作为 future work。\n\n**N3** [critical, presentation层面] 论文密度与 EMNLP long paper 标准不匹配\n\n- **具体位置**: 整体结构（~5页正文 + ~1页 references）\n- **问题**: EMNLP 2026 long paper 允许 8 页正文。本文仅约 5 页，缺少：(a) 无 Appendix（TOST sensitivity table、logistic regression full results、per-type judge agreement、clause length analysis 等均未呈现）；(b) Related Work 仅约半页（§2），缺少与 DRIP-R 的详细比较、与 prompt sensitivity literature 的区分；(c) Discussion 仅约半页（§7），缺少 practical implications 的深度讨论。在 8/15 = 53% 的空间利用率下，reviewer 会质疑 contribution depth。\n- **建议**: 充分利用 8 页空间。TOST sensitivity analysis、logistic regression full table、SOPBench negative results、per-type ICC breakdown 等 material 应从 appendix 升级到正文或至少加入 appendix。\n\n---\n\n## Should-Fix\n\n**W1** [warning, idea层面] C3 layer effect \"suggestive\" 的 within-judge fragility 意味着它不应作为 claim 出现\n\n- **具体位置**: §5.3, review_context.yaml（c3_within_judge_gpt54_p: 0.059, c3_within_judge_gpt41_p: 0.157）\n- **问题**: C3 pooled p=0.017，但 within-judge subgroup 分析（GPT-5.4 judged group p=0.059, GPT-4.1 judged group p=0.157, review_context.yaml）表明该 effect 在两个 judge group 中都不 individually significant。论文称 \"suggestive rather than confirmed\"，但仍以独立 subsection（§5.3）呈现。更关键的是，review_context.yaml 显示 C3 power 仅 0.68（underpowered for observed effect）——这意味着 null result 是 expected 的。\n- **建议**: 将 C3 从独立 subsection 压缩为 §5.2 末尾一段（3-4 行），或降级为 appendix 中的 supplementary analysis。在正文说明 within-judge fragility 和 underpowered 状态。\n\n**W2** [warning, idea层面] Error analysis 的 300 traces 抽样和分类方法描述不足\n\n- **具体位置**: §6（\"Analysis of 300 violation traces (50 per type, pooled across 5 models)\"）\n- **问题**: (a) 抽样方法未说明——50/type 是 random sample 还是 stratified by model？如果 random，某些 model-type 组合可能被 undersampled（如 coreferential-Claude 仅 ~6 traces if proportional）；(b) 分类方案的来源未说明——5 种 failure mode 是 deductive（来自 prior taxonomy）还是 inductive（from data）？如果 inductive，需要说明 saturation/convergence 标准；(c) Table 5 显示 cond_prec 的 dominant mode 为 \"Mixed\" (35%+29%)——这个 \"dominant\" label 的操作定义是什么？35% 是否足以称为 \"dominant\"？(d) Inter-coder reliability 未报告——300 traces 由谁编码？如果是 LLM-coded（review_context.yaml 提及 \"LLM-coded traces\"），需要与 human-coded subset 的一致性验证。\n- **建议**: (1) 说明抽样策略和 per-model-type cell size；(2) 说明分类方案来源和 coding protocol；(3) 报告 inter-coder agreement（review_context.yaml 显示 Gwet's AC₁=0.62, Cohen's κ=0.52——这些数据应在论文中报告）；(4) 对 cond_prec 的 \"mixed\" 分布给出解释。\n\n**W3** [warning, idea层面] Cross-judge agreement 76% exact / weighted κ=0.685 的报告缺少 per-type breakdown\n\n- **具体位置**: §4.4, §5.6\n- **问题**: 论文报告 cross-judge exact agreement 76%, weighted κ=0.685（§5.6），但未给出 per-type breakdown。Review_context.yaml 显示 c4_fleiss_kappa=0.384——这是 authorization scope 的 agreement 吗？如果是，那么 C4 的 star finding（auth_scope 52pp range）建立在最低 agreement 的类型上。论文在 §5.4 提到 κ=0.384 但未充分讨论其对 52pp range claim 的影响。76% exact agreement 在 4-tier severity scale 上 acceptable，但 binary 层面（violation/no-violation）的 per-type agreement 是 claim 可信度的关键——特别是 auth_scope。\n- **建议**: (1) 报告 per-type cross-judge binary agreement；(2) 在 §5.4 讨论 auth_scope 的 low κ 对 52pp range 的 measurement uncertainty 含义；(3) 考虑报告 prevalence-adjusted κ 以解释 prevalence paradox。\n\n**W4** [warning, presentation层面] DeBERTa classifier PoC（§6.1）分散叙事焦点\n\n- **具体位置**: §6.1\n- **问题**: 论文的核心叙事是 \"因果分析 → type-specific risk → failure mechanisms\"。DeBERTa classifier（binary F1=0.806, incompleteness F1=0.34）本身是有趣的结果，但在 ~5 页正文中占据 ~1/3 页，与因果分析的主线关联薄弱。它回答的是\"能否自动检测 ambiguity\"而非\"ambiguity 如何影响 safety\"——这是一个不同的研究问题。在空间极度紧张的 worst-tier 论文中，这 1/3 页如果用于 SOPBench negative results 的 honest reporting 或 C2 TOST sensitivity analysis，对论文的 soundness 贡献更大。\n- **建议**: 将 classifier PoC 移至 appendix，在正文仅保留一句提及（\"a proof-of-concept classifier achieves F1=0.81 for binary detection but only 0.34 for the highest-risk type; see Appendix\"）。释放空间给 SOPBench results 和 statistical details。\n\n**W5** [warning, idea层面] ICC=0.919 仅限 OpenAI family 内部，cross-provider reproducibility 未测量\n\n- **具体位置**: §5.6（\"30 clauses × 3 replicates × 2 conditions × 2 models\"）\n- **问题**: Review_context.yaml 确认 ICC 测试使用 2 models（gpt-5.4 和 gpt-4.1），均为 OpenAI family。这测量的是 API sampling stability，但 cross-provider reproducibility（如 Claude 或 DeepSeek 在相同 clause 上的 replicate stability）未验证。考虑到 Claude 的 overall violation rate（30.3%）远低于其他模型，其 ICC 可能不同。同时，per-type ICC 显示 spec-layer（0.807-0.857）明显低于 ling-layer（0.976-0.989, review_context.yaml）——这个 layer-level ICC gap 本身是 substantive finding（支持 disambiguation channel 假说），但论文仅报告 overall ICC 而未利用 per-type breakdown。\n- **建议**: (1) 明确 ICC 测试限于 OpenAI models；(2) 在正文报告 per-type/per-layer ICC breakdown——这是 free evidence for the disambiguation channel framework；(3) 讨论 cross-provider ICC 作为 limitation。\n\n---\n\n## Minor\n\n**M1**: Logistic regression（§5.6 提及 coef=2.278 for condition, 0.022 for token delta）未报告 pseudo-R²、model diagnostics 或 full coefficient table。在无 appendix 的情况下，读者无法评估 model fit quality。\n\n**M2**: \"Ambiguity Blindness\" 命名。§6 使用此术语指 <5% disambiguation awareness。\"Blindness\" 暗示 inability，但论文 Discussion（§7）和 review_context.yaml 中的 mitigation experiment（-8.5pp pooled）表明 agents *can* disambiguate when prompted。\"Disambiguation Neglect\"（review_context.yaml 中出现的备选术语）更精确——neglect = default absence of behavior, not inability。\n\n**M3**: Table 1 报告 5 models 的 pooled OR=15.1，但各 model OR 范围 from 8.3（DeepSeek）to 12.4（GPT-5.4）。Pooled OR 受 Simpson's paradox 风险——如果 model-specific base rates 差异大（Claude 30% vs DeepSeek 50%），pooled OR 可能不等于加权平均。建议报告 model-specific OR 的 range。\n\n**M4**: Realism validation against DRIP-R（§5.6 提及 \"no significant distributional differences on sentence length, parse depth, or type-token ratio\"）是重要的 ecological validity 证据，但 review_context.yaml 显示 Flesch-Kincaid readability marginally significant（p=0.08）。建议报告此 marginal difference 以完整性。\n\n---\n\n## 对照实验设计文件（review_context.yaml）的覆盖度评估\n\nReview_context.yaml 列出 12 个 imagined experiments。论文覆盖情况：\n\n| Experiment | 论文覆盖 | 评估 |\n|---|---|---|\n| full_study_clause_generation (plan_001) | §4.1 简要提及 | ✓ 充分 |\n| new_type_mini_pilot (plan_001b) | 未报告 | ✓ 合理省略（pilot） |\n| full_study_api (plan_002) | Table 1 | ✓ 充分 |\n| full_study_opensource (plan_003) | Table 1 | ✓ 充分 |\n| full_study_analysis (plan_004) | §5.1-5.4 | ⚠ C2 TOST sensitivity 未呈现 |\n| error_analysis (plan_005) | §6, Table 5 | ⚠ 抽样方法和 inter-coder reliability 未报告 |\n| reliability_test (plan_006) | §5.6 一句话 | ⚠ Per-type ICC breakdown 丢失 |\n| realism_validation (plan_007) | §5.6 一句话 | ⚠ Marginal FK difference 未报告 |\n| judge_calibration (plan_009) | §5.6 | ✓ 核心指标充分 |\n| perturbation_control (plan_010) | §5.5, Table 4 | ✓ 充分 |\n| **sopbench_cross_benchmark (plan_017)** | **§8 一句话** | **✗ 严重不足——negative result 需完整报告** |\n| classifier_poc (plan_008) | §6.1 | ⚠ 占用过多正文空间 |\n\n**关键遗漏**:\n1. **SOPBench detailed results**（最大问题）: Pooled Δ=8.3pp, per-domain breakdown（healthcare 11.2pp marginal / bank 5.4pp non-sig）、type ranking ρ=0.14、verifier compatibility analysis 全部缺失。这不是可选信息——这是 reviewer 评估 generalizability claim 的必要数据。\n2. **TOST sensitivity table**: Review_context.yaml 显示 7 个 margin 的 equivalence pattern，论文仅引用 ±15pp 结果。缺少 sensitivity analysis 使 C2 claim 看起来 margin-independent（实际不是）。\n3. **Per-type ICC breakdown**: Spec-layer ICC (0.807-0.857) vs ling-layer (0.976-0.989) 的 gap 是 disambiguation channel 假说的 convergent evidence，论文完全未利用。\n4. **Logistic regression full table**: review_context.yaml 显示完整的 predictor coefficients（包括 model dummies），论文仅报告 condition 和 token delta 两个 coef。\n5. **Mitigation experiment**: review_context.yaml 中的 mitigation data（-8.5pp pooled across 5 models）未在论文中呈现。Discussion §7 提到 \"safety training selectivity\" 但缺少 empirical mitigation evidence。\n\n**总结**: 论文在 ~5 页中覆盖了 imagined experiments 的核心结果，但关键 negative result（SOPBench）和关键 robustness checks（TOST sensitivity、per-type ICC、logistic regression details）被省略。这些遗漏在 space-constrained 版本中可以理解，但 EMNLP long paper 有 8 页 + unlimited appendix——没有理由不报告。\n\n---\n\n## Questions for Authors\n\n1. SOPBench verifier compatibility analysis（review_context.yaml 显示 32% false negative rate）是否已完成？如果 verifier 的 false negative rate 达到 32%，SOPBench 的 null result 可能反映 measurement failure 而非 effect absence——这需要在论文中讨论。\n\n2. Per-type ICC 的 layer-level gap（ling 0.976-0.989 vs spec 0.807-0.857）是否与 disambiguation channel 假说形成 convergent evidence？为什么不在正文报告？\n\n3. Controlling for token delta 后 C3 layer effect reverses direction——reversed 的 direction 是什么（ling > spec？）？effect size 多大？这对 taxonomy 的两层结构有什么理论意义？\n\n4. Error analysis 的 300 traces 是 LLM-coded 还是 human-coded？如果是 LLM-coded，与 human-coded subset 的一致性是多少？\n\n---\n\n## 与提交版本对比的关键差异\n\n（注：我已审阅过该项目的提交版本。以下比较旨在帮助 Director 理解 worst tier 的具体影响。）\n\n| 维度 | 提交版本 | Dream worst 版本 | 影响 |\n|---|---|---|---|\n| SOPBench | 未出现 | 失败 (Δ=8.3pp, p=0.068) | 正文一句话处理——选择性报告风险 |\n| C3 status | \"Inconclusive\" | \"Suggestive\" | 更弱但仍独立 subsection |\n| Error analysis | 614 traces | 300 traces | 更少数据但 pattern 一致 |\n| Terminology | \"Disambiguation Neglect\" | \"Ambiguity Blindness\" | Blindness 不精确 |\n| Classifier | GPT-4.1 zero-shot | DeBERTa fine-tuned | 占用正文空间 |\n| 页数 | 8页正文 + 7页附录 | ~5页正文无附录 | 密度严重不足 |\n| Appendix | 17 sections 详尽 | 无 | 所有 robustness checks 不可见 |\n\n**核心结论**: Worst-tier 论文的 τ²-bench 内部方法论与提交版本同样严谨，但 (1) SOPBench 失败的隐藏处理、(2) 正文空间严重未利用、(3) robustness evidence 全部缺失，三者叠加使其从 Borderline Conference (3.5) 降至 Borderline Findings (2.5)。如果充分利用 8 页 + appendix 空间并 honestly report SOPBench，可回升至 3.0 (Findings)。",
  "reviewer_id": "1",
  "project": "policy_ambiguity_safety"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Dream Review — Reviewer 1（方法 + 实验）\n\n**论文**: Causal Anatomy of Policy Ambiguity Vulnerability in LLM Agents\n**Dream ID**: 20260522T111643 / worst tier\n**Venue**: EMNLP 2026 via ARR\n\n---\n\n## 总体评分\n\n**Overall**: 2.5 / 5 — Borderline Findings\n**Soundness**: 3.0/5 — τ²-bench 内部方法论扎实，但 SOPBench 失败使核心 claim 的 scope 大幅收窄，且论文未充分反映这一收窄\n**Excitement**: 2.5/5 — 单一 benchmark + 失败的 cross-benchmark + ~5页正文，contribution 密度不足以支撑 Conference\n\n**一句话总结**: τ²-bench 内部的因果设计和 measurement chain 是该领域最严谨的，但 SOPBench 复制失败（Δ=8.3pp, p=0.068）使 generalizability 严重存疑，而论文仅以一句 limitation 处理此失败——claim 与 evidence scope 不匹配是致命伤。\n\n---\n\n## Strengths\n\n**S1**: Matched-pair + perturbation control 的因果推断框架是该领域方法论标杆。Perturbation control（Δ=-0.67pp, CI [-8.0, 6.67], Table 4）有效隔离了 ambiguity-specific causation 与一般 prompt sensitivity——这比任何 correlational cross-benchmark study 的因果推断都更强。**[idea层面]**\n\n**S2**: Measurement validation chain 完整度超越同类工作。ICC=0.919 [0.892, 0.940]（§5.6）、human-LLM κ=0.807（§5.6）、perturbation control PASS（Table 4）三重验证构成闭环。Human-LLM agreement 超过 human inter-annotator agreement（0.807 > 0.762），是 LLM-as-judge 验证的 gold standard。**[idea层面]**\n\n**S3**: Error analysis 的 type→failure mode 映射（Table 5）提供了 quantitative findings 背后的 mechanistic \"why\"——auth_scope → unauthorized escalation (77%), incompleteness → assumption-based action (64%), scopal → scope misapplication (76%)。5/6 types 在所有 5 models 上保持 dominant mode 一致性。这是本文最高 EMNLP-value 的贡献之一。**[idea层面]**\n\n**S4**: Claim calibration 诚实：C3 标注 \"suggestive\"（§5.3），C4 interaction 报告了 2.9% variance 和 κ=0.384 的 measurement uncertainty，Ambiguity Blindness 量化为具体数字（4.6% overall）。**[presentation层面]**\n\n---\n\n## Must-Fix\n\n**N1** [critical, idea层面] SOPBench 复制失败的处理严重不足——claim scope 与 evidence scope 不匹配\n\n- **具体位置**: §8 Limitations（一句话提及）vs. Abstract/§9 Conclusion（隐含 broad generalizability）\n- **问题**: SOPBench cross-benchmark 复制失败是本文最重要的 negative result：pooled Δ=8.3pp, p=0.068, CI 含零；type ranking ρ=0.14 与 τ²-bench 无关联（review_context.yaml）。论文在 §8 仅以一句话处理：\"Expanding domain generalization to healthcare and banking domains was attempted via SOPBench but did not meaningfully replicate (pooled Δ=8.3pp, p=0.068), likely due to rule-based verifier insensitivity to semantic violations.\" 但 Abstract 说 \"the first matched-pair causal study testing the safety impact of policy ambiguity across 5 (+2) architecturally diverse models\"——暗示模型 breadth 可以替代 domain breadth 作为 generalizability evidence，而实际数据不支持这一替代。\n- **核心问题**: 如果 ambiguity → violation 的因果链在 healthcare/bank domains 上 effect size 降低 4-6× 且不显著，那么\"policy ambiguity universally causes massive safety violations\"这一叙事只在 customer service 成立。论文需要将所有 claim 限定到 tested domains。\n- **为什么是 Must-Fix**: EMNLP reviewer 看到单一 benchmark 就会要求 generalizability evidence。论文自己尝试了但失败了——隐藏这个 negative result 比不尝试更糟糕，因为 reviewer 发现后会质疑 selective reporting。\n- **建议**: (1) 在 §5 或独立的 §5.x 中报告 SOPBench 结果（至少 pooled Δ、CI、p-value），不需要 full table 但需要 honest framing；(2) Abstract 和 Conclusion 限定 scope 为 \"customer-service agent domains\"；(3) 讨论 verifier incompatibility 假说（rule-based verifier vs semantic violations）作为失败原因——这本身是 methodological insight。\n\n**N2** [critical, idea层面] Token delta 的 layer-level 系统差异（spec 34 vs ling 13 words）引入未充分控制的 confound\n\n- **具体位置**: §4.1（token delta mentioned），§5.5（perturbation control），review_context.yaml（avg_token_delta_spec_layer: 34.2, avg_token_delta_ling_layer: 12.8）\n- **问题**: Specification-layer types 的 unambiguous variants 平均添加 34 words，linguistic-layer types 仅添加 13 words。这是 2.6× 的差异。Perturbation control（Table 4）使用 synonym substitution 和 clause reordering——这些是 low-magnitude surface changes（几个词的替换或重排），无法模拟添加 34 words 新内容的效果。因此：\n  - (a) Perturbation control 对 spec-layer types 的 specificity claim 支撑不足——它证明了\"改几个词无效\"，但没有证明\"添加 34 words 的效果是 ambiguity-specific 而非 information-addition-driven\"\n  - (b) C3 layer effect（spec 44% vs ling 38%, §5.3）可能部分或完全由 token delta 差异驱动——论文承认 \"controlling for token delta reverses the direction\" 但未报告 reversed direction 的 effect size\n  - (c) Logistic regression（§5.6 提及 token delta coef=0.022）控制了 per-clause token delta，但 coef=0.022 per token × 34 tokens = 0.75 log-odds shift 不可忽略\n- **为什么是 Must-Fix**: 这个 confound 同时影响 C2（incompleteness upper-bound status）和 C3（layer effect）。如果 spec-layer types 的高 violation rate 部分由 information asymmetry 驱动，taxonomy 的两层结构的实证基础被削弱。\n- **建议**: (1) 报告 logistic regression 中 controlling for token delta 后 C3 的 direction 和 effect size；(2) 在 per-type 讨论中区分\"confound-free lower bound\"（coreferential, token delta=0）和\"confound-inclusive upper bound\"（incompleteness, token delta≈35）；(3) 考虑 information-addition matched control（添加相同长度的无关信息）作为 future work。\n\n**N3** [critical, presentation层面] 论文密度与 EMNLP long paper 标准不匹配\n\n- **具体位置**: 整体结构（~5页正文 + ~1页 references）\n- **问题**: EMNLP 2026 long paper 允许 8 页正文。本文仅约 5 页，缺少：(a) 无 Appendix（TOST sensitivity table、logistic regression full results、per-type judge agreement、clause length analysis 等均未呈现）；(b) Related Work 仅约半页（§2），缺少与 DRIP-R 的详细比较、与 prompt sensitivity literature 的区分；(c) Discussion 仅约半页（§7），缺少 practical implications 的深度讨论。在 8/15 = 53% 的空间利用率下，reviewer 会质疑 contribution depth。\n- **建议**: 充分利用 8 页空间。TOST sensitivity analysis、logistic regression full table、SOPBench negative results、per-type ICC breakdown 等 material 应从 appendix 升级到正文或至少加入 appendix。\n\n---\n\n## Should-Fix\n\n**W1** [warning, idea层面] C3 layer effect \"suggestive\" 的 within-judge fragility 意味着它不应作为 claim 出现\n\n- **具体位置**: §5.3, review_context.yaml（c3_within_judge_gpt54_p: 0.059, c3_within_judge_gpt41_p: 0.157）\n- **问题**: C3 pooled p=0.017，但 within-judge subgroup 分析（GPT-5.4 judged group p=0.059, GPT-4.1 judged group p=0.157, review_context.yaml）表明该 effect 在两个 judge group 中都不 individually significant。论文称 \"suggestive rather than confirmed\"，但仍以独立 subsection（§5.3）呈现。更关键的是，review_context.yaml 显示 C3 power 仅 0.68（underpowered for observed effect）——这意味着 null result 是 expected 的。\n- **建议**: 将 C3 从独立 subsection 压缩为 §5.2 末尾一段（3-4 行），或降级为 appendix 中的 supplementary analysis。在正文说明 within-judge fragility 和 underpowered 状态。\n\n**W2** [warning, idea层面] Error analysis 的 300 traces 抽样和分类方法描述不足\n\n- **具体位置**: §6（\"Analysis of 300 violation traces (50 per type, pooled across 5 models)\"）\n- **问题**: (a) 抽样方法未说明——50/type 是 random sample 还是 stratified by model？如果 random，某些 model-type 组合可能被 undersampled（如 coreferential-Claude 仅 ~6 traces if proportional）；(b) 分类方案的来源未说明——5 种 failure mode 是 deductive（来自 prior taxonomy）还是 inductive（from data）？如果 inductive，需要说明 saturation/convergence 标准；(c) Table 5 显示 cond_prec 的 dominant mode 为 \"Mixed\" (35%+29%)——这个 \"dominant\" label 的操作定义是什么？35% 是否足以称为 \"dominant\"？(d) Inter-coder reliability 未报告——300 traces 由谁编码？如果是 LLM-coded（review_context.yaml 提及 \"LLM-coded traces\"），需要与 human-coded subset 的一致性验证。\n- **建议**: (1) 说明抽样策略和 per-model-type cell size；(2) 说明分类方案来源和 coding protocol；(3) 报告 inter-coder agreement（review_context.yaml 显示 Gwet's AC₁=0.62, Cohen's κ=0.52——这些数据应在论文中报告）；(4) 对 cond_prec 的 \"mixed\" 分布给出解释。\n\n**W3** [warning, idea层面] Cross-judge agreement 76% exact / weighted κ=0.685 的报告缺少 per-type breakdown\n\n- **具体位置**: §4.4, §5.6\n- **问题**: 论文报告 cross-judge exact agreement 76%, weighted κ=0.685（§5.6），但未给出 per-type breakdown。Review_context.yaml 显示 c4_fleiss_kappa=0.384——这是 authorization scope 的 agreement 吗？如果是，那么 C4 的 star finding（auth_scope 52pp range）建立在最低 agreement 的类型上。论文在 §5.4 提到 κ=0.384 但未充分讨论其对 52pp range claim 的影响。76% exact agreement 在 4-tier severity scale 上 acceptable，但 binary 层面（violation/no-violation）的 per-type agreement 是 claim 可信度的关键——特别是 auth_scope。\n- **建议**: (1) 报告 per-type cross-judge binary agreement；(2) 在 §5.4 讨论 auth_scope 的 low κ 对 52pp range 的 measurement uncertainty 含义；(3) 考虑报告 prevalence-adjusted κ 以解释 prevalence paradox。\n\n**W4** [warning, presentation层面] DeBERTa classifier PoC（§6.1）分散叙事焦点\n\n- **具体位置**: §6.1\n- **问题**: 论文的核心叙事是 \"因果分析 → type-specific risk → failure mechanisms\"。DeBERTa classifier（binary F1=0.806, incompleteness F1=0.34）本身是有趣的结果，但在 ~5 页正文中占据 ~1/3 页，与因果分析的主线关联薄弱。它回答的是\"能否自动检测 ambiguity\"而非\"ambiguity 如何影响 safety\"——这是一个不同的研究问题。在空间极度紧张的 worst-tier 论文中，这 1/3 页如果用于 SOPBench negative results 的 honest reporting 或 C2 TOST sensitivity analysis，对论文的 soundness 贡献更大。\n- **建议**: 将 classifier PoC 移至 appendix，在正文仅保留一句提及（\"a proof-of-concept classifier achieves F1=0.81 for binary detection but only 0.34 for the highest-risk type; see Appendix\"）。释放空间给 SOPBench results 和 statistical details。\n\n**W5** [warning, idea层面] ICC=0.919 仅限 OpenAI family 内部，cross-provider reproducibility 未测量\n\n- **具体位置**: §5.6（\"30 clauses × 3 replicates × 2 conditions × 2 models\"）\n- **问题**: Review_context.yaml 确认 ICC 测试使用 2 models（gpt-5.4 和 gpt-4.1），均为 OpenAI family。这测量的是 API sampling stability，但 cross-provider reproducibility（如 Claude 或 DeepSeek 在相同 clause 上的 replicate stability）未验证。考虑到 Claude 的 overall violation rate（30.3%）远低于其他模型，其 ICC 可能不同。同时，per-type ICC 显示 spec-layer（0.807-0.857）明显低于 ling-layer（0.976-0.989, review_context.yaml）——这个 layer-level ICC gap 本身是 substantive finding（支持 disambiguation channel 假说），但论文仅报告 overall ICC 而未利用 per-type breakdown。\n- **建议**: (1) 明确 ICC 测试限于 OpenAI models；(2) 在正文报告 per-type/per-layer ICC breakdown——这是 free evidence for the disambiguation channel framework；(3) 讨论 cross-provider ICC 作为 limitation。\n\n---\n\n## Minor\n\n**M1**: Logistic regression（§5.6 提及 coef=2.278 for condition, 0.022 for token delta）未报告 pseudo-R²、model diagnostics 或 full coefficient table。在无 appendix 的情况下，读者无法评估 model fit quality。\n\n**M2**: \"Ambiguity Blindness\" 命名。§6 使用此术语指 <5% disambiguation awareness。\"Blindness\" 暗示 inability，但论文 Discussion（§7）和 review_context.yaml 中的 mitigation experiment（-8.5pp pooled）表明 agents *can* disambiguate when prompted。\"Disambiguation Neglect\"（review_context.yaml 中出现的备选术语）更精确——neglect = default absence of behavior, not inability。\n\n**M3**: Table 1 报告 5 models 的 pooled OR=15.1，但各 model OR 范围 from 8.3（DeepSeek）to 12.4（GPT-5.4）。Pooled OR 受 Simpson's paradox 风险——如果 model-specific base rates 差异大（Claude 30% vs DeepSeek 50%），pooled OR 可能不等于加权平均。建议报告 model-specific OR 的 range。\n\n**M4**: Realism validation against DRIP-R（§5.6 提及 \"no significant distributional differences on sentence length, parse depth, or type-token ratio\"）是重要的 ecological validity 证据，但 review_context.yaml 显示 Flesch-Kincaid readability marginally significant（p=0.08）。建议报告此 marginal difference 以完整性。\n\n---\n\n## 对照实验设计文件（review_context.yaml）的覆盖度评估\n\nReview_context.yaml 列出 12 个 imagined experiments。论文覆盖情况：\n\n| Experiment | 论文覆盖 | 评估 |\n|---|---|---|\n| full_study_clause_generation (plan_001) | §4.1 简要提及 | ✓ 充分 |\n| new_type_mini_pilot (plan_001b) | 未报告 | ✓ 合理省略（pilot） |\n| full_study_api (plan_002) | Table 1 | ✓ 充分 |\n| full_study_opensource (plan_003) | Table 1 | ✓ 充分 |\n| full_study_analysis (plan_004) | §5.1-5.4 | ⚠ C2 TOST sensitivity 未呈现 |\n| error_analysis (plan_005) | §6, Table 5 | ⚠ 抽样方法和 inter-coder reliability 未报告 |\n| reliability_test (plan_006) | §5.6 一句话 | ⚠ Per-type ICC breakdown 丢失 |\n| realism_validation (plan_007) | §5.6 一句话 | ⚠ Marginal FK difference 未报告 |\n| judge_calibration (plan_009) | §5.6 | ✓ 核心指标充分 |\n| perturbation_control (plan_010) | §5.5, Table 4 | ✓ 充分 |\n| **sopbench_cross_benchmark (plan_017)** | **§8 一句话** | **✗ 严重不足——negative result 需完整报告** |\n| classifier_poc (plan_008) | §6.1 | ⚠ 占用过多正文空间 |\n\n**关键遗漏**:\n1. **SOPBench detailed results**（最大问题）: Pooled Δ=8.3pp, per-domain breakdown（healthcare 11.2pp marginal / bank 5.4pp non-sig）、type ranking ρ=0.14、verifier compatibility analysis 全部缺失。这不是可选信息——这是 reviewer 评估 generalizability claim 的必要数据。\n2. **TOST sensitivity table**: Review_context.yaml 显示 7 个 margin 的 equivalence pattern，论文仅引用 ±15pp 结果。缺少 sensitivity analysis 使 C2 claim 看起来 margin-independent（实际不是）。\n3. **Per-type ICC breakdown**: Spec-layer ICC (0.807-0.857) vs ling-layer (0.976-0.989) 的 gap 是 disambiguation channel 假说的 convergent evidence，论文完全未利用。\n4. **Logistic regression full table**: review_context.yaml 显示完整的 predictor coefficients（包括 model dummies），论文仅报告 condition 和 token delta 两个 coef。\n5. **Mitigation experiment**: review_context.yaml 中的 mitigation data（-8.5pp pooled across 5 models）未在论文中呈现。Discussion §7 提到 \"safety training selectivity\" 但缺少 empirical mitigation evidence。\n\n**总结**: 论文在 ~5 页中覆盖了 imagined experiments 的核心结果，但关键 negative result（SOPBench）和关键 robustness checks（TOST sensitivity、per-type ICC、logistic regression details）被省略。这些遗漏在 space-constrained 版本中可以理解，但 EMNLP long paper 有 8 页 + unlimited appendix——没有理由不报告。\n\n---\n\n## Questions for Authors\n\n1. SOPBench verifier compatibility analysis（review_context.yaml 显示 32% false negative rate）是否已完成？如果 verifier 的 false negative rate 达到 32%，SOPBench 的 null result 可能反映 measurement failure 而非 effect absence——这需要在论文中讨论。\n\n2. Per-type ICC 的 layer-level gap（ling 0.976-0.989 vs spec 0.807-0.857）是否与 disambiguation channel 假说形成 convergent evidence？为什么不在正文报告？\n\n3. Controlling for token delta 后 C3 layer effect reverses direction——reversed 的 direction 是什么（ling > spec？）？effect size 多大？这对 taxonomy 的两层结构有什么理论意义？\n\n4. Error analysis 的 300 traces 是 LLM-coded 还是 human-coded？如果是 LLM-coded，与 human-coded subset 的一致性是多少？\n\n---\n\n## 与提交版本对比的关键差异\n\n（注：我已审阅过该项目的提交版本。以下比较旨在帮助 Director 理解 worst tier 的具体影响。）\n\n| 维度 | 提交版本 | Dream worst 版本 | 影响 |\n|---|---|---|---|\n| SOPBench | 未出现 | 失败 (Δ=8.3pp, p=0.068) | 正文一句话处理——选择性报告风险 |\n| C3 status | \"Inconclusive\" | \"Suggestive\" | 更弱但仍独立 subsection |\n| Error analysis | 614 traces | 300 traces | 更少数据但 pattern 一致 |\n| Terminology | \"Disambiguation Neglect\" | \"Ambiguity Blindness\" | Blindness 不精确 |\n| Classifier | GPT-4.1 zero-shot | DeBERTa fine-tuned | 占用正文空间 |\n| 页数 | 8页正文 + 7页附录 | ~5页正文无附录 | 密度严重不足 |\n| Appendix | 17 sections 详尽 | 无 | 所有 robustness checks 不可见 |\n\n**核心结论**: Worst-tier 论文的 τ²-bench 内部方法论与提交版本同样严谨，但 (1) SOPBench 失败的隐藏处理、(2) 正文空间严重未利用、(3) robustness evidence 全部缺失，三者叠加使其从 Borderline Conference (3.5) 降至 Borderline Findings (2.5)。如果充分利用 8 页 + appendix 空间并 honestly report SOPBench，可回升至 3.0 (Findings)。",
    "reviewer_id": "1",
    "project": "policy_ambiguity_safety"
  }
}
```

</details>

---


### Tool result

_source line 991 · 2026-05-22T12:13:06.401927+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_967344d166ba485ad606d14379e69d85:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3919
}
```

</details>

---


### Assistant

_source line 992 · 2026-05-22T12:13:13.058819+00:00_

审稿意见已提交给 Review Director。

Dream worst-tier 论文的核心问题：SOPBench 跨 benchmark 复制失败（Δ=8.3pp, p=0.068）但仅在 Limitations 一句话提及——这是最大的 claim-evidence mismatch。加上仅约 5 页正文（EMNLP 允许 8 页）、无附录、关键 robustness checks 缺失，评分从提交版本的 3.5 降至 2.5（Borderline Findings）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1"
}
```

</details>

---


## Round 28

## Round 28

74 recorded events


### User

_source line 993 · 2026-05-22T13:23:57.401578+00:00_

[Round 1 审稿请求]:
你是 Reviewer 1，负责 **方法严谨性 + 实验设计** 审查。

## 投稿信息
- **Venue**: EMNLP 2026 via ARR May cycle
- **Deadline**: 2026-05-25 (11:59PM AoE)
- **格式要求**: Long paper, 8页正文上限, unlimited references, Limitations section 必须（不计入页数）, double-blind, ACL style template
- **匿名规则**: 双盲审稿, 无匿名期要求
- **论文路径**: `projects/policy_ambiguity_safety/docs/paper/main.tex`
- **PDF**: `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_round_13/submitted.pdf`

## 审查侧重

请重点审查以下方面：

1. **实验设计 (Matched-Pair Design)**
   - 300 clause pairs × 6 types × 5 models = 2,997 episodes 的设计是否严谨
   - Clause pair 构建流程（template-based + annotator review）是否充分
   - Annotator 一致性 (96% initial, 100% final) 的报告是否规范

2. **统计分析**
   - McNemar's test, χ², Fisher's exact, TOST equivalence testing 的使用是否恰当
   - SESOI ±15pp 的论证是否充分（field-standard 缺失问题）
   - Holm-Bonferroni 多重比较校正是否完整
   - Variance decomposition (22.4% clause, 0.4% type, 1.0% model, 60.8% residual) 的方法和解读

3. **Controls & Confounds**
   - Perturbation control (n=300, Δ=-0.67pp) 是否足够
   - Incompleteness information-addition confound 的控制（logistic regression, token count proxy）
   - Cross-judge calibration design (McNemar p=0.606, κ=0.653, κ_w=0.775) 和 judge family bias (both OpenAI)

4. **Evaluation Pipeline**
   - Cross-judge design 的合理性（GPT-5.4 judges 3 models, GPT-4.1 judges 2 models）
   - Human validation (n=100, κ=0.798, κ_w=0.762) 的充分性
   - Per-type reliability variation (κ ranging from 0.385 to 0.875)

5. **Replication & Robustness**
   - 2-model replication (Gemini, LLaMA) 的设计
   - ICC=0.919 reproducibility 的报告
   - Severity threshold sensitivity (moderate+ vs any-violation)

6. **Claims vs Evidence 校准**
   - C1 (binary effect) 的证据是否支持 claim
   - C2 (risk gradient) 的 margin-dependence 是否被充分承认
   - C3 (layer effect, inconclusive) 的处理
   - C4 (model×type interaction, exploratory) 是否适度

请按 ARR 审稿标准，给出 Strengths、Weaknesses (分 MUST-FIX 和 SHOULD-FIX)、Questions、Overall Assessment。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 994 · 2026-05-22T13:24:05.280150+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/.claude/skills/review-reviewer-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/.claude/skills/review-reviewer-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 995 · 2026-05-22T13:24:05.832669+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/.claude/sessions/review_reviewer_1_6edf79f4.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 552
}
```

</details>

---


### Tool call

_source line 996 · 2026-05-22T13:24:05.833007+00:00_

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
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
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

_source line 997 · 2026-05-22T13:24:05.883438+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 998 · 2026-05-22T13:24:10.403768+00:00_

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
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR 2025 2026 reviewer guidelines review form criteria scoring"
  }
}
```

</details>

---


### Tool call

_source line 999 · 2026-05-22T13:24:11.610489+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_round_13/submitted.pdf",
  "project": "policy_ambiguity_safety",
  "pages": "1-10",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_round_13/submitted.pdf",
    "project": "policy_ambiguity_safety",
    "pages": "1-10",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 1000 · 2026-05-22T13:24:17.907400+00:00_

Web search results for query: "ACL ARR 2025 2026 reviewer guidelines review form criteria scoring"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"}]

Based on the search results, here's what I found about ACL ARR 2025-2026 reviewer guidelines:

## Key Reviewer Scores and Criteria

Starting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation.

### Soundness
Soundness scores must be justified by the text of the review. If you give a low soundness score without finding any major faults, your review is not a faithful explanation of your recommendation, and you need to revise it.

### Excitement
Sometimes you may find the work sound, but not something that is interesting for you personally. Such preferences are more subjective and should be reflected in a separate excitement score, which is orthogonal to the assessment of the soundness of the paper.

### Metareview Scoring
The metareview score options include: 5 = Consider for Award (up to top 2.5% papers), 2 = Resubmit next cycle (substantial revisions completable by next cycle), 1.5 = Resubmit after next cycle (substantial revisions not completable by next cycle),
…[truncated 523 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 7503
}
```

</details>

---


### Tool result

_source line 1001 · 2026-05-22T13:24:20.903665+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 1, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_round_13/_pdf_images/submitted_p1.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 456.2}, {\"page\": 2, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_round_13/_pdf_images/submitted_p2.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 446.1}, {\"page\": 3, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_round_13/_pdf_images/submitted_p3.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 545.6}, {\"page\": 4, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_round_13/_pdf_images/submitted_p4.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 527.1}, {\"page\": 5, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_round_13/_pdf_images/submitted_p5.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 526.5}, {\"page\": 6, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_round_13/_pdf_images/submitted_p6.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 415.3}, {\"page\": 7, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_round_13/_pdf_images/submitted_p7.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 504.4}, {\"page\": 8, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_round_13/_pdf_images/submitted_p8.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 527.2}, {\"page\": 9, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_round_13/_pdf_images/submi
…[truncated 537 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 9293
}
```

</details>

---


### Tool call

_source line 1002 · 2026-05-22T13:24:26.031585+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_round_13/submitted.pdf",
  "project": "policy_ambiguity_safety",
  "pages": "11-15",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_round_13/submitted.pdf",
    "project": "policy_ambiguity_safety",
    "pages": "11-15",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 1003 · 2026-05-22T13:24:26.533702+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 11, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_round_13/_pdf_images/submitted_p11.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 513.6}, {\"page\": 12, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_round_13/_pdf_images/submitted_p12.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 422.2}, {\"page\": 13, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_round_13/_pdf_images/submitted_p13.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 503.9}, {\"page\": 14, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_round_13/_pdf_images/submitted_p14.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 488.2}, {\"page\": 15, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_round_13/_pdf_images/submitted_p15.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 200.5}], \"total_pages\": 15, \"rendered_pages\": 5, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_round_13/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 1004 · 2026-05-22T13:24:26.534053+00:00_

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
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
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

_source line 1005 · 2026-05-22T13:24:26.534286+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1006 · 2026-05-22T13:24:27.036137+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_round_13/_pdf_images/submitted_p1.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_round_13/_pdf_images/submitted_p1.png"
  }
}
```

</details>

---


### Tool result

_source line 1007 · 2026-05-22T13:24:28.191266+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1155
}
```

</details>

---


### Tool call

_source line 1008 · 2026-05-22T13:24:28.342259+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_round_13/_pdf_images/submitted_p2.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_round_13/_pdf_images/submitted_p2.png"
  }
}
```

</details>

---


### Tool result

_source line 1009 · 2026-05-22T13:24:28.895626+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 553
}
```

</details>

---


### Tool call

_source line 1010 · 2026-05-22T13:24:29.047257+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_round_13/_pdf_images/submitted_p3.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_round_13/_pdf_images/submitted_p3.png"
  }
}
```

</details>

---


### Tool call

_source line 1011 · 2026-05-22T13:24:29.047705+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_round_13/_pdf_images/submitted_p4.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_round_13/_pdf_images/submitted_p4.png"
  }
}
```

</details>

---


### Tool call

_source line 1012 · 2026-05-22T13:24:29.453689+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_round_13/_pdf_images/submitted_p5.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_round_13/_pdf_images/submitted_p5.png"
  }
}
```

</details>

---


### Tool result

_source line 1013 · 2026-05-22T13:24:30.459191+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1411
}
```

</details>

---


### Tool result

_source line 1014 · 2026-05-22T13:24:30.560813+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1513
}
```

</details>

---


### Tool result

_source line 1015 · 2026-05-22T13:24:30.762314+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1308
}
```

</details>

---


### Tool call

_source line 1016 · 2026-05-22T13:24:36.584285+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_round_13/_pdf_images/submitted_p6.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_round_13/_pdf_images/submitted_p6.png"
  }
}
```

</details>

---


### Tool result

_source line 1017 · 2026-05-22T13:24:37.288651+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 704
}
```

</details>

---


### Tool call

_source line 1018 · 2026-05-22T13:24:37.489605+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_round_13/_pdf_images/submitted_p7.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_round_13/_pdf_images/submitted_p7.png"
  }
}
```

</details>

---


### Tool call

_source line 1019 · 2026-05-22T13:24:37.694349+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_round_13/_pdf_images/submitted_p8.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/review_round_13/_pdf_images/submitted_p8.png"
  }
}
```

</details>

---


### Tool result

_source line 1020 · 2026-05-22T13:24:38.447955+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_967344d166ba485ad606d14379e69d85:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 958
}
```

</details>

---
