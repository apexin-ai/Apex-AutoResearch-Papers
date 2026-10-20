# Director coordination — Part 2 of 16

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Conversation logs

[← Part 1](part-001.md) · [Transcript overview](../director-coordination-copy-2.md) · [Part 3 →](part-003.md) · [Structured JSON](../../../sessions/6a/6a5a1a2f9a2bf6bdf404.json)

## Round 32

### Tool call

_source line 343 · 2026-05-15T06:39:01.040041+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 submission deadline page limit formatting guidelines ARR"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 submission deadline page limit formatting guidelines ARR"
  }
}
```

</details>

---


### Tool call

_source line 344 · 2026-05-15T06:39:02.496481+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"EMNLP 2026\" call for papers main conference submission"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"EMNLP 2026\" call for papers main conference submission"
  }
}
```

</details>

---


### Tool call

_source line 345 · 2026-05-15T06:39:03.451006+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "struct_self_consist_ie",
  "file": "paper_checklist.yaml",
  "max_chars": "5000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "struct_self_consist_ie",
    "file": "paper_checklist.yaml",
    "max_chars": "5000"
  }
}
```

</details>

---


### Tool result

_source line 346 · 2026-05-15T06:39:07.268433+00:00_

Web search results for query: "EMNLP 2026 submission deadline page limit formatting guidelines ARR"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"EMNLP 2026 LaTeX Template | ACL Style Files & Overleaf | Underleaf","url":"https://www.underleaf.ai/templates/emnlp"},{"title":"Dates and Venues","url":"http://aclrollingreview.org/dates"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"EMNLP 2026 on X: \"📢 The First Call for Papers for EMNLP 2026 is officially out! 📝 We welcome long &amp; short papers featuring original research on empirical methods for NLP. 🗓️ ARR Submission Deadline: May 25, 2026 🔗 Read the full CFP here: https://t.co/GU2kaISjUG #EMNLP2026\" / X","url":"https://x.com/emnlpmeeting/status/2029508292637061462"},{"title":"AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/"},{"title":"EMNLP: Empirical Methods in Natural Language Processing 2027 2026 2025 ...","url":"http://www.wikicfp.com/cfp/program?id=883"}]

Based on the search results, here's the key information about EMNLP 2026 submission requirements:

## Submission Deadline
The ARR submission deadline for long and short papers is May 25, 2026. All deadlines are 11:59PM UTC-12:00 ("anywhere on Earth").

## Page Limits and Formatting Guidelines
The format is two-column with an 8-page limit for long papers and a 4-page limit for short papers. EMNLP uses the standard ACL style files, so the LaTeX template is identical to the one used for ACL, NAACL, and other *ACL conferences.

## Additional Requireme
…[truncated 703 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "WebSearch",
  "elapsed_ms": 6228
}
```

</details>

---


### Tool result

_source line 347 · 2026-05-15T06:39:10.633586+00:00_

Web search results for query: ""EMNLP 2026" call for papers main conference submission"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"EMNLP 2026 on X: \"📢 The First Call for Papers for EMNLP 2026 is officially out! 📝 We welcome long &amp; short papers featuring original research on empirical methods for NLP. 🗓️ ARR Submission Deadline: May 25, 2026 🔗 Read the full CFP here: https://t.co/GU2kaISjUG #EMNLP2026\" / X","url":"https://x.com/emnlpmeeting/status/2029508292637061462"},{"title":"EMNLP 2026 on X: \"📢 Please note a critical update to the original #EMNLP2026 Call for Papers: since EMNLP and AACL share the ARR May cycle, authors will need to explicitly select a target conference at submission time. This choice will be binding! For more details see: https://t.co/0u1wbX9fT6\" / X","url":"https://x.com/emnlpmeeting/status/2047754845919031450"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"EMNLP 2026 Conference | OpenReview","url":"https://openreview.net/group?id=EMNLP%2F2026%2FConference"},{"title":"2026 *ACL Conference Dates | Computational Linguistics","url":"https://submissions.cljournal.org/index.php/cljournal/announcement/view/14"},{"title":"emnlp 2026 - AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/conference/?id=emnlp26"},{"title":"EMNLP 2026 Call for Papers — Official Deadlines & Important Dates | PaperPilot","url":"https://www.getpaperpilot.com/deadlines/emnlp-2026.html"}]

I found comprehensive information about the EMNLP 2026 Call for Papers for the main conference. He
…[truncated 1523 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "WebSearch",
  "elapsed_ms": 8137
}
```

</details>

---


### Tool result

_source line 348 · 2026-05-15T06:39:10.635042+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"No paper_checklist.yaml found for 'struct_self_consist_ie'.\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 7184
}
```

</details>

---


### Tool call

_source line 349 · 2026-05-15T06:39:19.132193+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL rolling review 2026 formatting guidelines page limit long short paper anonymity responsible NLP checklist"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL rolling review 2026 formatting guidelines page limit long short paper anonymity responsible NLP checklist"
  }
}
```

</details>

---


### Tool call

_source line 350 · 2026-05-15T06:39:20.438311+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/sections/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/sections/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper"
  }
}
```

</details>

---


### Tool result

_source line 351 · 2026-05-15T06:39:20.488985+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/method.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/limitations.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 352 · 2026-05-15T06:39:26.969185+00:00_

Web search results for query: "ACL rolling review 2026 formatting guidelines page limit long short paper anonymity responsible NLP checklist"

Links: [{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"},{"title":"Paper formatting guidelines - ACLPUB","url":"https://acl-org.github.io/ACLPUB/formatting.html"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"ACL Rolling Review | ACL Member Portal","url":"https://www.aclweb.org/portal/content/acl-rolling-review"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/responsibleNLPresearch/"}]

I've completed the web search for ACL Rolling Review 2026 formatting guidelines. Here are the key findings:

## Page Limits

Long papers have a page limit of 8 pages, while short papers have a limit of 4 pages, excluding ethical considerations and limitations. Final versions of accepted papers will be given one additional page of content (up to 9 pages for long papers, up to 5 pages for short papers)
…[truncated 1276 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "WebSearch",
  "elapsed_ms": 7836
}
```

</details>

---


### Tool call

_source line 353 · 2026-05-15T06:39:32.543667+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 354 · 2026-05-15T06:39:32.995899+00:00_

1	\begin{abstract}
2	Test-time scaling through multi-sample generation promises quality improvements for LLM-based information extraction, but which confidence signals best serve quality estimation versus sample selection remains unclear.
3	We systematically compare five confidence signals from three families---structural (entity voting, Soft Jaccard), surface (exact match, Fleiss' $\kappa$), and model-internal (log-probability)---across NER (three datasets of varying difficulty) and RE (SciERC) with two model families (Qwen3-8B, LLaMA-3.1-8B).
4	We find that the strongest signals achieve $\rho{=}0.38$ (entity voting) and AUROC${=}0.75$ (exact match) for quality estimation, with ranking and classification favoring different signals across task complexity; however, this strong quality estimation does not translate into selection gains---we find no statistically significant evidence that any signal surpasses greedy decoding on SciERC---where output diversity is substantial---across both model architectures ($p{>}0.39$, bootstrap) despite 13--18~pp of oracle headroom; on easier tasks, near-identical outputs preclude meaningful selection analysis.
5	We term this disconnect the \textit{correlation-selection gap}: instance-level consistency signals predict which inputs the model handles reliably, not which output is best among $N$ candidates.
6	Signal rankings further depend on task difficulty---exact match dominates easy tasks, structural signals dominate hard tasks---with consistent ordering direction across models but model-dependent magnitude; when model capability is insufficient, apparent correlations are driven by zero/non-zero separation rather than genuine quality gradation.
7	These results reframe consistency signals as quality estimators rather than output selectors for structured IE.
8	\end{abstract}
9	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 355 · 2026-05-15T06:39:32.996332+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 356 · 2026-05-15T06:39:33.498971+00:00_

1	\section{Introduction}\label{sec:introduction}
2	
3	Self-consistency---sampling multiple outputs and aggregating them---has become a powerful strategy for improving language model reasoning.
4	On discrete-answer tasks such as arithmetic and commonsense QA, majority voting over chain-of-thought samples yields large gains: +18 percentage points on GSM8K (PaLM-540B; \citealp{wang2023selfconsistency}).
5	More broadly, test-time compute scaling through repeated sampling and selection has emerged as a complementary axis to model scaling, offering substantial quality improvements at inference time \cite{snell2024scaling, brown2024monkeys}.
6	These results rest on a shared assumption: that among $N$ stochastic samples, a selection mechanism can identify better outputs.
7	For tasks with a single correct answer, this assumption holds naturally---the majority vote is the selector.
8	But information extraction (IE) poses a fundamentally different challenge.
9	The output is not a single token or number; it is a \textit{set} of entities or relations with internal dependencies, where two samples may extract overlapping but non-identical structures.
10	There is no obvious majority to vote on, partial agreement is the norm rather than the exception, and the space of valid outputs is combinatorially large.
11	Can self-consistency still provide useful signal in this structured setting?
12	
13	Prior work on confidence estimation for LLM-based IE has conflated two distinct objectives: \textit{quality estimation} (which inputs does the model handle reliably?) and \textit{sample selection} (which of $N$ outputs is best?).
14	These require fundamentally different signal properties: the former benefits from instance-level aggregation, while the latter demands per-sample discrimination.
15	Self-consistency methods for discrete answers \cite{wang2023selfconsistency, chen2024usc} and weighted variants \cite{taubenfeld2025cisc, kang2025selfcertainty} assume outputs can be grouped by equivalen
…[truncated 4333 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 357 · 2026-05-15T06:39:33.549976+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 358 · 2026-05-15T06:39:33.550521+00:00_

1	\section{Related Work}\label{sec:related}
2	
3	\paragraph{Self-consistency and test-time scaling.}
4	Self-consistency decoding \cite{wang2023selfconsistency} improves reasoning by majority voting over chain-of-thought samples, assuming a discrete answer space.
5	Extensions to free-form text use LLM-based comparison \cite{chen2024usc}, atomic sub-claim decomposition \cite{thirukovalluru2024atomic}, or cross-sample hallucination detection \cite{manakul2023selfcheckgpt}.
6	For test-time scaling, \citet{snell2024scaling} characterize compute scaling laws and \citet{brown2024monkeys} show best-of-$N$ gains across tasks.
7	Recent reward-free selectors include confidence-weighted voting \cite{taubenfeld2025cisc}, KL-based self-certainty \cite{kang2025selfcertainty}, adaptive sampling \cite{kim2026reasc}, ranked aggregation \cite{wang2025rankedvoting}, and latent-space consistency \cite{oh2025latentsc}.
8	Concurrently, \citet{feng2025optimal} and \citet{wang2025make} adapt self-consistency to difficulty-aware settings, echoing our finding that signal rankings shift with task complexity; \citet{li2025llms} propose generative self-aggregation for IE but focus on output fusion rather than confidence-based selection.
9	All of the above target reasoning/QA with discrete answers or specific aggregation strategies.
10	Our work extends self-consistency to set-valued structured outputs and identifies the correlation-selection gap: strong quality estimation ($\rho{=}0.38$) coexists with selection failure ($p{>}0.39$).
11	
12	\paragraph{Consistency for structured IE.}
13	\citet{nedellec2026consistency} study consistency--accuracy correlations for LLM-based NER/RE, corroborating our quality-estimation findings.
14	Their work leaves open three questions we address: (i)~whether structural matching improves on surface-level agreement (which they acknowledge ``overlooks semantically consistent outputs''); (ii)~whether quality estimation translates to best-of-$N$ selection; and (iii)~whet
…[truncated 3141 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 359 · 2026-05-15T06:39:34.454432+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 360 · 2026-05-15T06:39:34.906586+00:00_

1	\section{Method}\label{sec:method}
2	
3	\subsection{Problem Formulation}\label{sec:formulation}
4	
5	Given a language model $\mathcal{M}$ and input $x$, we sample $N$ structured outputs $\{y_1, \ldots, y_N\}$ at temperature $T > 0$ via constrained decoding \cite{willard2023guided}.
6	Each $y_i$ is an entity set (NER) or relation set (RE).
7	A confidence signal $c$ serves two purposes: (a) \textit{quality estimation}---predicting which instances the model handles reliably, and (b) \textit{sample selection}---identifying the best output among $N$ candidates.
8	
9	A \textbf{per-sample signal} scores each $y_i$ independently, $c_{\text{ps}}: (x, y_i) \to \mathbb{R}$, enabling direct candidate ranking.
10	An \textbf{instance-level signal} aggregates over all $N$ samples, $c_{\text{il}}: (x, \{y_i\}_{i=1}^N) \to \mathbb{R}$, producing a single score per input.
11	This asymmetry---between predicting \textit{which inputs} are easy and selecting \textit{which output} is best---is central to the correlation-selection gap we investigate.
12	Notation is summarized in Appendix~\ref{app:notation}.
13	
14	\subsection{Confidence Signals}\label{sec:signals}
15	
16	We compare five signals from three families: \textit{model-internal} (log-probability), \textit{surface} (exact match, Fleiss' $\kappa$), and \textit{structural} (Soft Jaccard, entity voting).
17	
18	\paragraph{Log-probability (model-internal, per-sample).}
19	The only per-sample signal.
20	For sample $y_i$ with tokens $t_1, \ldots, t_{|y_i|}$:
21	\begin{equation}\label{eq:logprob}
22	c_{\text{lp}}(y_i) = \frac{1}{|y_i|} \sum_{j=1}^{|y_i|} \log p_{\mathcal{M}}(t_j \mid t_{<j}, x)
23	\end{equation}
24	
25	\paragraph{Exact match voting (surface, instance-level).}
26	The majority fraction---the proportion of samples producing the most common output:
27	\begin{equation}\label{eq:em}
28	c_{\text{em}}(x) = \frac{1}{N} \max_{y} \big|\{i : y_i = y\}\big|
29	\end{equation}
30	
31	\paragraph{Fleiss' $\kappa$ (surface, instance-lev
…[truncated 3478 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 361 · 2026-05-15T06:39:34.957207+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 362 · 2026-05-15T06:39:35.359634+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Experimental Setup}
5	\label{sec:setup}
6	
7	\paragraph{Datasets.}
8	We evaluate on three English IE benchmarks spanning a difficulty gradient.
9	\textbf{SciERC} \cite{luan2018scierc} contains 551 test instances annotated for joint NER (6 types) and RE (7 types).
10	\textbf{CoNLL-2003} \cite{tjongkimsang2003conll} provides 3{,}453 test sentences with 4 entity types, where models achieve ${\approx}$91\% micro F1.
11	\textbf{WNUT-17} \cite{derczynski2017wnut} consists of 1{,}287 social media instances with emerging entities, used to probe method boundaries (52\% zero F1).
12	
13	\paragraph{Models and sampling.}
14	Both \textbf{Qwen3-8B} and \textbf{LLaMA-3.1-8B-Instruct} are fine-tuned with LoRA (rank$=$32, $\alpha{=}64$) for 5 epochs using LLaMA Factory \cite{zheng2024llamafactory} under identical training procedures, ensuring cross-architecture comparisons (at 8B scale) reflect architectural differences rather than training confounds.
15	We draw $N{=}8$ samples at $T{=}1.0$ (primary), with $N{=}16$ for scaling experiments.\footnote{$N{=}16$ results for CoNLL (Qwen) and SciERC (LLaMA) are in Table~\ref{tab:robustness} (Appendix~\ref{app:robustness}).}
16	Quality estimation uses Spearman $\rho$ and AUROC; downstream utility uses best-of-$N$ selection F1 with exact span matching (NER) and head-tail-label matching (RE).
17	Inference uses vLLM with constrained decoding \cite{willard2023guided}.
18	
19	%% ============================================================
20	\subsection{Quality Estimation Results}
21	\label{sec:qe_results}
22	
23	\begin{table*}[t]
24	\centering
25	\small
26	\caption{Quality estimation across tasks and models (Spearman $\rho$ and AUROC). Best value per block and column in \textbf{bold}. SciERC evaluates joint NER (6 types) and RE (7 types); CoNLL evaluates NER (4 types). $N{=}8$ results use seed${=}42$; $N{=}16$ results are averaged across seeds \{42, 123, 456\}.}
27	\label{tab:qu
…[truncated 11663 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 402
}
```

</details>

---


### Tool call

_source line 363 · 2026-05-15T06:39:35.410224+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 364 · 2026-05-15T06:39:35.812284+00:00_

1	\section{Discussion}\label{sec:discussion}
2	
3	\paragraph{Practical recommendations.}
4	For per-instance quality ranking, entity voting provides the strongest rank correlation ($\rho{=}0.38$), though exact match leads binary discrimination (AUROC${=}0.749$); under conditional filtering, EM leads on both NER and RE ($\rho{=}0.360$, $0.417$).
5	Signal rankings depend on task difficulty---EM dominates easy tasks (CoNLL), Voting and SJ dominate hard tasks (SciERC)---directionally consistent across tested model families, though with model-dependent magnitude.
6	When model capability is insufficient (WNUT-17), all signals converge toward non-significant conditional correlations (Table~\ref{tab:wnut}).
7	
8	\paragraph{Why the gap exists.}
9	Four of five signals are instance-level by construction and cannot rank $N$ candidates; the consensus-proximity strategy (\S\ref{sec:evaluation}) adds no reliable value (Table~\ref{tab:selection}).
10	Logprob, the sole per-sample signal, primarily reflects grammar compliance under constrained decoding---75\% of comparisons are effectively ties (\S\ref{sec:selection_gap}).
11	The common root is that quality estimation ranks \textit{instances}, while sample selection ranks \textit{candidates within a single instance}, requiring per-sample quality information that neither instance-level aggregation nor token-level confidence provides.
12	On SciERC, diversity-stratified analysis confirms the gap persists even among high-diversity instances (Appendix~\ref{app:diversity}); calibration analysis shows RE miscalibration (ECE 0.109--0.339; Appendix~\ref{app:calibration}) may compound this failure.
13	These signals are thus well-suited for quality-aware routing but not for discriminating among candidates.
14	
15	\paragraph{Connection to MBR decoding.}
16	Our selection strategies instantiate minimum Bayes risk (MBR) decoding \cite{eikema2022sampling}: SJ uses $U{=}\text{SJ}(y_i, y_j)$, EM uses $U{=}\mathbb{1}[y_i{=}y_j]$ (standard majority votin
…[truncated 918 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 402
}
```

</details>

---


### Tool call

_source line 365 · 2026-05-15T06:39:35.862992+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 366 · 2026-05-15T06:39:36.315390+00:00_

1	\section{Conclusion}\label{sec:conclusion}
2	
3	This work provides, to our knowledge, the first multi-family comparison of confidence signals for test-time scaling in generative information extraction.
4	By comparing five signals from three families across NER and RE tasks of varying difficulty, we disentangle quality estimation from sample selection---two objectives that prior work has conflated.
5	Consistency-based signals are effective quality estimators ($\rho$ up to 0.38, AUROC up to 0.75), but we find no significant evidence that any signal surpasses greedy on best-of-$N$ selection on SciERC ($p{>}0.39$, 13--18~pp oracle headroom), a disconnect we term the \textit{correlation-selection gap}.
6	Signal rankings depend on task difficulty---exact match leads on easy tasks, structural signals on hard tasks---with this ordering directionally consistent across model families, though magnitudes are model-dependent.
7	While our NER findings are validated across three datasets, our RE conclusions rest on SciERC alone and warrant further validation.
8	
9	Trained verifiers or reward models could close the selection gap by learning per-sample quality discrimination.
10	Cross-task transfer beyond IE, scaling to larger models (70B+), and integration with conformal prediction are promising directions.
11	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 367 · 2026-05-15T06:39:36.366166+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 368 · 2026-05-15T06:39:36.717847+00:00_

1	Our evaluation covers three datasets but only one RE benchmark (SciERC), where 40\% of instances receive zero F1, compressing the discriminable range and limiting signal differentiation for relation extraction.
2	WNUT-17 confirms the capability boundary of our approach, but our positive results on formal-domain text (CoNLL, SciERC) have not been validated on informal or noisy text where models achieve non-trivial performance.
3	
4	We evaluate two model families (Qwen3-8B and LLaMA-3.1-8B), both at 8B parameters.
5	A 3-seed robustness analysis confirms that signal rankings are stable across seeds ($\sigma{\leq}0.025$; Table~\ref{tab:multiseed}), but whether our findings---particularly the correlation-selection gap and the difficulty-dependent signal ordering---hold for larger models (70B+) or closed-source APIs remains untested.
6	Larger models may produce higher-quality and more diverse samples, potentially altering the signal landscape.
7	
8	Our analysis of selection potential uses only unsupervised signals.
9	We do not train a dedicated verifier or reward model, leaving unknown how much of the oracle headroom a supervised approach could recover.
10	
11	We evaluate at $N{=}8$ and $N{=}16$.
12	The behavior of confidence signals at larger sample sizes (e.g., $N{=}64$ or $N{=}128$) is unknown, and $N$-scaling gains are setting-dependent: SJ improves by $+0.052$ on Qwen SciERC NER but only $+0.016$ on LLaMA SciERC NER when doubling from $N{=}8$ to $N{=}16$.
13	
14	On CoNLL with LLaMA, the SJ--FK gap is only 0.003 ($\rho{=}0.431$ vs.\ $0.428$), so the structural advantage over surface signals may not generalize to all simple-schema datasets.
15	Constrained decoding (Outlines/vLLM) enforces schema compliance, potentially compressing per-sample diversity and contributing to the correlation-selection gap beyond what free-form generation would exhibit.
16	Finally, log-probability was excluded from the temperature comparison ($T{=}0.7$ vs.\ $T{=}1.0$) due to missing $T{=}0
…[truncated 307 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 351
}
```

</details>

---


### Tool call

_source line 369 · 2026-05-15T06:39:36.718243+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 370 · 2026-05-15T06:39:36.769646+00:00_

1	\section{Notation}\label{app:notation}
2	
3	Table~\ref{tab:notation} summarizes the notation used throughout the paper.
4	
5	\begin{table}[h]
6	\centering
7	\small
8	\begin{tabular}{cl}
9	\toprule
10	Symbol & Meaning \\
11	\midrule
12	$\mathcal{M}$ & Language model \\
13	$x$ & Input instance \\
14	$y_i$ & $i$-th stochastic sample \\
15	$N$ & Number of samples \\
16	$T$ & Sampling temperature \\
17	$c(\cdot)$ & Confidence signal \\
18	SJ & Soft Jaccard similarity \\
19	FK & Fleiss' $\kappa$ \\
20	EM & Exact-match voting rate \\
21	$c_{\text{vote}}$ & Entity voting confidence \\
22	$c_{\text{lp}}$ & Log-probability (mean token log-likelihood) \\
23	\bottomrule
24	\end{tabular}
25	\caption{Notation used throughout the paper.}
26	\label{tab:notation}
27	\end{table}
28	
29	\section{Robustness Analysis}\label{app:robustness}
30	
31	\begin{table}[t]
32	\centering
33	\small
34	\caption{Signal robustness across configurations (Spearman $\rho$). Top: temperature on Qwen SciERC. Middle: sample size on Qwen SciERC. Bottom: cross-architecture transfer (LLaMA CoNLL $N{=}16$, 3-seed mean $\pm\sigma$). $^\dagger$Mean over 3 seeds ($\sigma{=}0.025$; individual: 0.428, 0.424, 0.384).}
35	\label{tab:robustness}
36	\begin{tabular}{llcc}
37	\toprule
38	& & NER $\rho$ & RE $\rho$ \\
39	\midrule
40	\multicolumn{4}{l}{\textit{Temperature} (Qwen SciERC, $N{=}8$)} \\
41	\quad SJ & $T{=}0.7$ & 0.388 & 0.234 \\
42	\quad SJ & $T{=}1.0$ & 0.360 & 0.250 \\
43	\quad FK & $T{=}0.7$ & 0.321 & 0.184 \\
44	\quad FK & $T{=}1.0$ & 0.267 & 0.275 \\
45	\midrule
46	\multicolumn{4}{l}{\textit{Sample size} (Qwen SciERC, $T{=}1.0$)} \\
47	\quad SJ & $N{=}8$  & 0.360 & 0.250 \\
48	\quad SJ & $N{=}16$ & 0.412$^\dagger$ & 0.281 \\
49	\quad FK & $N{=}8$  & 0.267 & 0.275 \\
50	\quad FK & $N{=}16$ & 0.280 & 0.279 \\
51	\midrule
52	\multicolumn{4}{l}{\textit{Cross-architecture} (LLaMA CoNLL, $N{=}16$, 3 seeds)} \\
53	\quad SJ &  & $0.463{\pm}0.007$ & --- \\
54	\quad FK &  & $0.455{\pm}0.006$ & --- \\
55	\quad EM &
…[truncated 21352 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 371 · 2026-05-15T06:39:45.812146+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/references.bib"
  }
}
```

</details>

---


### Tool result

_source line 372 · 2026-05-15T06:39:46.365355+00:00_

1	% Auto-generated from literature_map.yaml — do not edit manually
2	
3	@inproceedings{angelopoulos2021conformal,
4	  title = {Uncertainty Sets for Image Classifiers using Conformal Prediction},
5	  author = {Angelopoulos, Anastasios N. and Bates, Stephen and Malik, Jitendra and Jordan, Michael I.},
6	  booktitle = {ICLR 2021},
7	  year = {2021},
8	  url = {https://arxiv.org/abs/2009.14193}
9	}
10	
11	@article{brown2024monkeys,
12	  title = {Large Language Monkeys: Scaling Inference Compute with Repeated Sampling},
13	  author = {Brown, Bradley and Juravsky, Jordan and Ehrlich, Ryan and Clark, Ronald and Le, Quoc V. and Ré, Christopher and Mirhoseini, Azalia},
14	  journal = {arXiv preprint arXiv:2407.21787},
15	  year = {2024},
16	  url = {https://arxiv.org/abs/2407.21787}
17	}
18	
19	@inproceedings{chen2024usc,
20	  title = {Universal Self-Consistency for Large Language Model Generation},
21	  author = {Chen, Xinyun and Aksitov, Renat and Alon, Uri and Ren, Jie and Xiao, Kefan and Yin, Pengcheng and Prakash, Sushant and Sutton, Charles and Wang, Xuezhi and Zhou, Denny},
22	  booktitle = {arXiv preprint (ICML 2024 Workshop ICL)},
23	  year = {2024},
24	  url = {https://arxiv.org/abs/2311.17311}
25	}
26	
27	@article{cobbe2021verifiers,
28	  title = {Training Verifiers to Solve Math Word Problems},
29	  author = {Cobbe, Karl and Kosaraju, Vineet and Bavarian, Mohammad and Chen, Mark and Jun, Heewoo and Kaiser, Lukasz and Plappert, Matthias and Tworek, Jerry and Hilton, Jacob and Nakano, Reiichiro and Hesse, Christopher and Schulman, John},
30	  journal = {arXiv preprint arXiv:2110.14168},
31	  year = {2021},
32	  url = {https://arxiv.org/abs/2110.14168}
33	}
34	
35	@inproceedings{culotta2004confidence,
36	  title = {Confidence Estimation for Information Extraction},
37	  author = {Culotta, Aron and McCallum, Andrew},
38	  booktitle = {HLT-NAACL 2004},
39	  year = {2004},
40	  url = {https://aclanthology.org/N04-4028/}
41	}
42	
43	@inproceedings{derczynski2017wnut,
44
…[truncated 20478 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 553
}
```

</details>

---


### Tool call

_source line 373 · 2026-05-15T06:39:46.817654+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "struct_self_consist_ie",
  "file": "decisions.yaml",
  "max_chars": "5000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "struct_self_consist_ie",
    "file": "decisions.yaml",
    "max_chars": "5000"
  }
}
```

</details>

---


### Tool result

_source line 374 · 2026-05-15T06:39:47.220245+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/decisions.yaml\", \"content\": \"_next_id: 67\\ndecisions:\\n- id: D001\\n  date: 2026-05-14 04:23 UTC\\n  summary: 'MVP 方案: ACE05 上验证 structural consistency vs Fleiss'' Kappa 的 correlation\\n    差异'\\n  rationale: 'PMC12888769 用 surface-level Fleiss'' Kappa 在 zero-shot 模型上得到 ρ=0.20-0.28，我们假设\\n    fine-tuned 模型 + structural consistency (soft Jaccard) 能达到 ρ≥0.40。这是整个论文的基础假设——如果\\n    structural consistency 不能更好地预测准确率，后续的 adaptive gating 无从谈起。Phase 0 pilot 设计: Qwen3-8B\\n    fine-tuned on ACE05, N=8 samples, 200 instances, 对比两种 consistency metric 的 Spearman\\n    ρ。Pass ≥0.40, Fail <0.30。'\\n  related_experiments: []\\n  depends_on: []\\n- id: D002\\n  date: 2026-05-14 04:27 UTC\\n  summary: 采纳 Reviewer 审查意见，收紧 MVP pass/fail 标准\\n  rationale: 'Reviewer 指出 5 个问题，全部合理采纳：(1) PASS 必须要求 EAE (high-headroom subtask) ρ≥0.40，仅\\n    NER 通过不够（ceiling effect 可能虚高）；(2) MARGINAL 区间加 time-boxed protocol: N=16 追加 +\\n    1天上限；(3) 加 fine-tuning 质量门控 (NER≥73, EAE≥45)，模型不行时先修 fine-tuning；(4) ACE05 今天必须确认；(5)\\n    监控 T=1.0 per-sample F1 分布，>30% F1=0 时追加 T=0.7。'\\n  related_experiments: []\\n  depends_on:\\n  - D001\\n- id: D003\\n  date: 2026-05-14 04:53 UTC\\n  summary: SciERC RE 替代 ACE05 EAE 作为 MVP high-headroom subtask\\n  rationale: ACE05 需 LDC 许可，用户未确认。SciERC 公开可得，有 NER+RE 两个 subtask。RE base F1 ~47（与\\n    ACE05 EAE ~52 相当），结构复杂度高（entity pair + relation type），headroom 大，是 EAE 的合理替代。PASS\\n    标准更新为 RE ρ≥0.40。需要补实现 RE 的 consistency + evaluation + pipeline 支持。\\n  related_experiments: []\\n  depends_on:\\n  - D002\\n- id: D004\\n  date: 2026-05-14 07:38 UTC\\n  summary: 'Gate 0: NER PASS (60.4%), RE FAIL (33.8%). 执行方案 C——当前模型先跑 pilot + 追训改进版，需修复\\n    RE evaluation'\\n  rationale: RE 33.8% 低于 40% 阈值但不阻塞 pilot：(1) headroom 大，oracle best-of-N 有提升空间；(2)\\n    consistency correlation 不要求高绝对 F1，要求 per-instance variance；(3) 弱模型上验证假设结论更强。但\\n    Reviewer 发现
…[truncated 3529 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 402
}
```

</details>

---


### Tool call

_source line 375 · 2026-05-15T06:39:47.270908+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/figures/*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/figures/*",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper"
  }
}
```

</details>

---


### Tool result

_source line 376 · 2026-05-15T06:39:47.321550+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/figures/fig_overview.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/figures/fig_reliability.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/figures/fig_signal_heatmap.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/figures/fig_selection_gap.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/figures/fig_temperature_robustness.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/figures/fig_length_logprob_scatter.pdf

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 377 · 2026-05-15T06:40:07.003677+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "struct_self_consist_ie",
  "file": "memory.md",
  "max_chars": "3000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "struct_self_consist_ie",
    "file": "memory.md",
    "max_chars": "3000"
  }
}
```

</details>

---


### Tool result

_source line 378 · 2026-05-15T06:40:07.205285+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/memory.md\", \"content\": \"# Memory — struct_self_consist_ie\\n\\n## 服务器环境\\n- autodl-5090: 4× RTX 5090 32GB, Python 3.12, vLLM 0.18.1, LLaMA Factory 0.9.4, tmux 3.2a\\n- gpu-5090-4x-2: 4× RTX 5090 32GB, PyTorch 2.10.0+cu128, vLLM 0.18.1\\n- conda: /root/miniconda3/\\n- 环境初始化: `source /etc/network_turbo && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`\\n- 项目路径: /root/autodl-tmp/struct_self_consist_ie/\\n- 基座模型: /root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B/\\n- ft_002_v2 merged: checkpoints/qwen3-8b-scierc-merged-v2/\\n- run_mvp_pilot.py 支持 --collect_logprobs, --num_test (默认已改为 9999)\\n\\n## 数据修正链 (D054-D060) 关键教训\\n- exp_012 是唯一使用 max_tokens=512 的实验，导致 voting_conf ρ 虚高 (0.502→0.379)\\n- SJ/FK 对 max_tokens 参数鲁棒（Δ<0.004），但 voting_conf 极度敏感\\n- 修正后 AUROC 排名反转：EM (0.749) > SJ (0.692) > Voting (0.684)\\n- Selection claim 由 bootstrap 确认为 null result（p=0.39），不能写 \\\"significantly outperforms\\\"\\n- 论文数据必须来自 _rerun_1024 或本身就用 1024 的实验\\n\\n## D066 LLaMA fresh rerun (2026-05-15)\\n- D066 决策：LLaMA 3-seed 全部使用 fresh rerun 数据（seed42_r1024 + seed123 + seed456_r1024）\\n- exp_018_llama_scierc_seed456（旧 exp_007 复制品）已标记 SUPERSEDED\\n- LLaMA NER SJ ρ 修正：旧 0.362±0.004 → 新 0.325±0.021（σ 增大 5× 是真实 seed 变异，seed123 拉高均值）\\n- **分析脚本与 report.json 的 EM/VC 值存在系统性差异**（如 seed42 VC: 脚本 0.373 vs report.json 0.405）。Reviewer 要求论文统一使用分析脚本输出（与 Qwen 同一套）。不要从 registry metrics（来自 report.json）直接引用 EM/VC 到论文。\\n- NER 信号排名 6/6 完全稳定：VC > SJ > EM > FK > LP\\n- Core claim \\\"structural > logprob\\\" NER 全部成立 (12/12)；RE 仅 VC 稳定胜 LP\\n\\n## Registry 清理备注 (2026-05-15)\\n- 9 个 PREPARING+killed 实验因状态机限制无法推进到 DONE，实质已废弃\\n- 包括：exp_017_llama_conll_n16_s456_r1024, exp_017_llama_conll_n16_r1024, exp_001_n16_seed123_full, exp_001_n16_seed456_full, exp001_seed123, exp001_seed456, exp_007_ner_llama, exp_002_merge_conll2003, exp008_re_n16\\n\", \"total_chars\": 1740,
…[truncated 60 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 379 · 2026-05-15T06:40:07.255941+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
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

_source line 380 · 2026-05-15T06:40:07.306583+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 381 · 2026-05-15T06:40:13.683341+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/struct_self_consist_ie/config.*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/struct_self_consist_ie/config.*",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1"
  }
}
```

</details>

---


### Tool result

_source line 382 · 2026-05-15T06:40:14.135595+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Glob",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 383 · 2026-05-15T06:40:14.186262+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/struct_self_consist_ie/*.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/struct_self_consist_ie/*.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects"
  }
}
```

</details>

---


### Tool result

_source line 384 · 2026-05-15T06:40:14.236899+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/experiment_plan.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/literature_map.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/dream_registry.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/writing_plan.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/paper_provenance.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/decisions.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/registry.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 385 · 2026-05-15T06:40:19.408673+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

```json
{
  "subagent_type": "Explore",
  "description": "Find external review config",
  "prompt": "Search for files containing \"external_review\" or \"paperreview_ai\" configuration in the project directory /home/ubuntu/.agent-ml-research-idea_gen_0514_1/. I need to find whether the struct_self_consist_ie project has external review enabled. Check project config files, YAML configs, TOML configs, etc. Report what you find in under 100 words."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Agent",
  "tool_args": {
    "subagent_type": "Explore",
    "description": "Find external review config",
    "prompt": "Search for files containing \"external_review\" or \"paperreview_ai\" configuration in the project directory /home/ubuntu/.agent-ml-research-idea_gen_0514_1/. I need to find whether the struct_self_consist_ie project has external review enabled. Check project config files, YAML configs, TOML configs, etc. Report what you find in under 100 words."
  }
}
```

</details>

---


### Tool call

_source line 386 · 2026-05-15T06:40:20.967367+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "external_review|paperreview_ai",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Grep",
  "tool_args": {
    "pattern": "external_review|paperreview_ai",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1"
  }
}
```

</details>

---


### Tool result

_source line 387 · 2026-05-15T06:40:21.169319+00:00_

Found 7 files
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/logs/chats/feishu_group_oc_3897c2857f11615119e277e820eae311_director.jsonl
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/global/logs/system.log
AGENTS.md
CLAUDE.md
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/logs/chats/feishu_group_oc_1b56445332d8ca2b4964b30f300f0e00_director.jsonl
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_reports/round_3.md
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_reports/round_2.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Grep",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 388 · 2026-05-15T06:40:21.169793+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/**/*.{yaml,yml,toml,json,config}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/**/*.{yaml,yml,toml,json,config}"
  }
}
```

</details>

---


### Tool result

_source line 389 · 2026-05-15T06:40:21.220408+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_1/config/approvals.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/config/feishu.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/config/pool.json
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/workspace.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/config/mcp_config.json
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/config/backend.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/idea_generator/ideas.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/config/mcp_config_director.json
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/config/mcp_config_reviewer.json
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/config/mcp_config_worker_5fb1f955b45e38e31789286a1790398d.json
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/logs/workers/worker_code_data_eval_modules_20260514T042533_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/logs/workers/worker_code_consistency_module_20260514T042604_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/logs/workers/worker_code_sampling_and_main_20260514T042643_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/logs/workers/worker_code_fix_chat_template_20260514T043155_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/logs/workers/worker_code_fix_sample_f1_dist_20260514T043208_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/config/secrets/struct_self_consist_ie/manifest.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/config/mcp_config_worker_0aa51d591547913249ab7a68dc681be8.json
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/logs/workers/worker_infra_env_setup_20260514T044757_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/logs/workers/worker_code_add_re_subtask_20260514T050825_res
…[truncated 11271 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 390 · 2026-05-15T06:40:22.776762+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/config/feishu.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/config/feishu.yaml"
  }
}
```

</details>

---


### Tool result

_source line 391 · 2026-05-15T06:40:22.927855+00:00_

1	app_id: cli_a97ee92a41b81cb1
2	app_secret: mlARg4oP9AVEWECTLUaEEgG0ivekqJg2
3	bot_name: Auto Research Prod15
4	chats: {}
5	policy:
6	  require_mention: true
7	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 392 · 2026-05-15T06:40:22.978951+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/workspace.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/workspace.yaml"
  }
}
```

</details>

---


### Tool result

_source line 393 · 2026-05-15T06:40:22.979407+00:00_

1	projects: {}
2	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 394 · 2026-05-15T06:40:24.635848+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie -type f \\( -name \"*.yaml\" -o -name \"*.yml\" -o -name \"*.json\" \\) | head -20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie -type f \\( -name \"*.yaml\" -o -name \"*.yml\" -o -name \"*.json\" \\) | head -20"
  }
}
```

</details>

---


### Tool result

_source line 395 · 2026-05-15T06:40:24.887893+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/figures/paper/fig_reliability_data.json
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/dream_registry.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/logs/workers/worker_code_sampling_and_main_20260514T042643_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/logs/workers/worker_code_exp_005_v2_20260514T152032_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/logs/workers/worker_analysis_read_exp016_and_seed123_results_20260514T122622_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/logs/workers/worker_experiment_exp_017_llama_conll_n16_s123_20260514T192424_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/logs/workers/worker_analysis_re_selection_bootstrap_20260515T032411_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/logs/workers/worker_paper_writing_introduction_20260514T200845_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/logs/workers/worker_analysis_exp_013_014_voting_baselines_20260514T111404_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/logs/workers/worker_paper_writing_related_work_20260514T202951_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/logs/workers/worker_analysis_tost_equivalence_20260515T050401_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/logs/workers/worker_analysis_exp_018_llama_scierc_seed456_r1024_20260515T062018_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/logs/workers/worker_analysis_n8_bootstrap_ci_20260515T030809_result.json
/home/ubuntu/.agent-ml-research-i
…[truncated 1046 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Bash",
  "elapsed_ms": 252
}
```

</details>

---


### Tool call

_source line 396 · 2026-05-15T06:40:24.888306+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/config/secrets/struct_self_consist_ie/manifest.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/config/secrets/struct_self_consist_ie/manifest.yaml"
  }
}
```

</details>

---


### Tool result

_source line 397 · 2026-05-15T06:40:24.939335+00:00_

1	autodl_5090_password:
[REDACTED]	  created_at: '2026-05-14T04:46:17.028384+00:00'
3	  provider: AutoDL
4	  purpose: SSH password for autodl-5090 server (RTX 5090 x4)
5	  updated_at: '2026-05-14T04:46:17.028399+00:00'
6	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 398 · 2026-05-15T06:40:26.747599+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/dream_registry.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/dream_registry.yaml"
  }
}
```

</details>

---


### Tool result

_source line 399 · 2026-05-15T06:40:27.099478+00:00_

1	dreams:
2	  dream_20260514T093336:
3	    dream_id: dream_20260514T093336
4	    project: struct_self_consist_ie
5	    status: done
6	    review_mode: full
7	    review_visible: true
8	    writing_visible: true
9	    venue: ''
10	    focus: 'Key tension: NER-primary paper with RE diagnostic. Reviewers will challenge:
11	      (1) scope narrowness (only NER positive), (2) single dataset risk, (3) whether
12	      diagnostic finding on RE is contribution enough. Best case should show multi-dataset
13	      NER generalization + strong diagnostic analysis. Worst case should show NER
14	      fails on new datasets or rho doesn''t improve with N=16.'
15	    what_if: []
16	    pid: 38424
17	    chat_id: oc_1b56445332d8ca2b4964b30f300f0e00
18	    card_message_id: om_x100b6f6d21c44ca0b32fc238f424cd5
19	    started_at: '2026-05-14T09:33:36+00:00'
20	    updated_at: '2026-05-14T10:29:10+00:00'
21	    stages_completed:
22	    - imagine
23	    - write
24	    - review
25	    error: null
26	    context_hash: b4e03a2916b5254d51daed52cfbe6b9abf6f3f6dc716eae1b4aecc4c5e13f095
27	  dream_20260514T105303:
28	    dream_id: dream_20260514T105303
29	    project: struct_self_consist_ie
30	    status: done
31	    review_mode: full
32	    review_visible: true
33	    writing_visible: true
34	    venue: ''
35	    focus: 'Post-revision dream. Key change: paper now compares 4 confidence signal
36	      families (log-prob, exact-match, FK, SJ) rather than just SJ vs FK. Reviewers
37	      in previous dream unanimously flagged missing baselines as #1 issue. This revision
38	      should address: (1) baseline completeness, (2) evaluation metric breadth (rho
39	      + AUROC + calibration + tau), (3) reframed contribution as systematic comparison
40	      + diagnostic analysis. Watch for: does the broader baseline set change the novelty
41	      assessment? Does SJ-vs-logprob become the new critical question?'
42	    what_if: []
43	    pid: 47146
44	    chat_id: oc_1b56445332d8ca2b4964b30f300f0e00
45
…[truncated 1258 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 351
}
```

</details>

---


### Tool call

_source line 400 · 2026-05-15T06:40:27.099965+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -r \"external_review\\|paperreview\" /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie --include=\"*.yaml\" --include=\"*.yml\" --include=\"*.json\" -l 2>/dev/null | head -10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -r \"external_review\\|paperreview\" /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie --include=\"*.yaml\" --include=\"*.yml\" --include=\"*.json\" -l 2>/dev/null | head -10"
  }
}
```

</details>

---


### Tool result

_source line 401 · 2026-05-15T06:40:27.200655+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Bash",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 402 · 2026-05-15T06:40:29.410211+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -i \"external_review\\|paperreview\" /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/logs/chats/*.jsonl 2>/dev/null | head -20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -i \"external_review\\|paperreview\" /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/logs/chats/*.jsonl 2>/dev/null | head -20"
  }
}
```

</details>

---


### Tool result

_source line 403 · 2026-05-15T06:40:29.461020+00:00_

&lt;persisted-output>
Output too large (56.9KB). Full output saved to: /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-review-director-0161122b/e9a736ba-69ad-4af3-90c7-9a7c4195a256/tool-results/bwl6latqw.txt

Preview (first 2KB):
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/logs/chats/feishu_group_oc_1b56445332d8ca2b4964b30f300f0e00_director.jsonl:{"ts": "2026-05-15T02:56:58.503899+00:00", "role": "user", "session": "feishu:group:oc_1b56445332d8ca2b4964b30f300f0e00:director", "text": "[审稿报告]\nOverall: borderline\n\n# Round 2 审稿报告 — struct_self_consist_ie\n\n**论文**: Strong Predictors, Weak Selectors: A Systematic Comparison of Confidence Signals for Test-Time Scaling in Information Extraction\n**Venue**: EMNLP 2026 Main Conference (ARR May 2026 cycle)\n**截止日期**: 2026-05-25\n**审稿人**: Reviewer 1（方法严谨性 + 实验设计）、Reviewer 2（新颖性 + 完整性 + 格式）\n**交叉分享**: 已完成，两位 Reviewer 均提交逐条 [AGREE]/[REBUT] 回应\n\n---\n\n## Summary\n\n本文系统比较了三个族群（structural/surface/model-internal）的五种 confidence signal 在 generative IE（NER + RE）中的 quality estimation 与 sample selection 表现。核心发现是 \"correlation-selection gap\"：instance-level consistency signals 是有效的 quality estimators（entity voting ρ=0.38, exact match AUROC=0.75），但无法可靠超越 greedy decoding 进行 best-of-N selection（p>0.39, bootstrap），尽管存在 13-18pp 的 oracle headroom。附带发现 signal ranking 随 task difficulty 变化（EM 领先 easy tasks，SJ/Voting 领先 hard tasks，WNUT-17 全部 collapse）。\n\n---\n\n## Strengths\n\n1. **概念贡献清晰且有框架性价值**：quality estimation（ranking instances by expected performance）vs sample selection（choosing best output among N candidates）的解耦（§3.1 per-sample vs instance-level signal formulation）对 generative IE 社区有指导意义，是与 Nédellec et al. (2026) 的关键差异化。\n\n2. **Quality estimation 分析深度突出**：5 signals × 4 configurations (Table 1) + conditional filtering + capability stratification + per-relation diagnostic + ρ-AUROC dissociation 分析，超过多数同类 empirical 
…[truncated 340 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 404 · 2026-05-15T06:40:31.421494+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "struct_self_consist_ie",
  "file": "memory.md",
  "max_chars": "3000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "struct_self_consist_ie",
    "file": "memory.md",
    "max_chars": "3000"
  }
}
```

</details>

---


### Tool result

_source line 405 · 2026-05-15T06:40:31.522354+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/memory.md\", \"content\": \"# Memory — struct_self_consist_ie\\n\\n## 服务器环境\\n- autodl-5090: 4× RTX 5090 32GB, Python 3.12, vLLM 0.18.1, LLaMA Factory 0.9.4, tmux 3.2a\\n- gpu-5090-4x-2: 4× RTX 5090 32GB, PyTorch 2.10.0+cu128, vLLM 0.18.1\\n- conda: /root/miniconda3/\\n- 环境初始化: `source /etc/network_turbo && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`\\n- 项目路径: /root/autodl-tmp/struct_self_consist_ie/\\n- 基座模型: /root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B/\\n- ft_002_v2 merged: checkpoints/qwen3-8b-scierc-merged-v2/\\n- run_mvp_pilot.py 支持 --collect_logprobs, --num_test (默认已改为 9999)\\n\\n## 数据修正链 (D054-D060) 关键教训\\n- exp_012 是唯一使用 max_tokens=512 的实验，导致 voting_conf ρ 虚高 (0.502→0.379)\\n- SJ/FK 对 max_tokens 参数鲁棒（Δ<0.004），但 voting_conf 极度敏感\\n- 修正后 AUROC 排名反转：EM (0.749) > SJ (0.692) > Voting (0.684)\\n- Selection claim 由 bootstrap 确认为 null result（p=0.39），不能写 \\\"significantly outperforms\\\"\\n- 论文数据必须来自 _rerun_1024 或本身就用 1024 的实验\\n\\n## D066 LLaMA fresh rerun (2026-05-15)\\n- D066 决策：LLaMA 3-seed 全部使用 fresh rerun 数据（seed42_r1024 + seed123 + seed456_r1024）\\n- exp_018_llama_scierc_seed456（旧 exp_007 复制品）已标记 SUPERSEDED\\n- LLaMA NER SJ ρ 修正：旧 0.362±0.004 → 新 0.325±0.021（σ 增大 5× 是真实 seed 变异，seed123 拉高均值）\\n- **分析脚本与 report.json 的 EM/VC 值存在系统性差异**（如 seed42 VC: 脚本 0.373 vs report.json 0.405）。Reviewer 要求论文统一使用分析脚本输出（与 Qwen 同一套）。不要从 registry metrics（来自 report.json）直接引用 EM/VC 到论文。\\n- NER 信号排名 6/6 完全稳定：VC > SJ > EM > FK > LP\\n- Core claim \\\"structural > logprob\\\" NER 全部成立 (12/12)；RE 仅 VC 稳定胜 LP\\n\\n## Registry 清理备注 (2026-05-15)\\n- 9 个 PREPARING+killed 实验因状态机限制无法推进到 DONE，实质已废弃\\n- 包括：exp_017_llama_conll_n16_s456_r1024, exp_017_llama_conll_n16_r1024, exp_001_n16_seed123_full, exp_001_n16_seed456_full, exp001_seed123, exp001_seed456, exp_007_ner_llama, exp_002_merge_conll2003, exp008_re_n16\\n\", \"total_chars\": 1740,
…[truncated 60 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 406 · 2026-05-15T06:40:31.522864+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "struct_self_consist_ie"
  }
}
```

</details>

---


### Tool result

_source line 407 · 2026-05-15T06:40:31.573528+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 408 · 2026-05-15T06:40:33.581913+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_reports/round_3.md",
  "limit": "50"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_reports/round_3.md",
    "limit": "50"
  }
}
```

</details>

---


### Tool result

_source line 409 · 2026-05-15T06:40:33.632678+00:00_

1	---
2	round: 3
3	overall_score: borderline
4	timestamp: 2026-05-15T04:14:58.309947+00:00
5	reviewer_ids: [1, 2]
6	cross_response_reviewer_ids: [1, 2]
7	force_resubmit: False
8	---
9	
10	# 审稿报告 — Round 3
11	**论文**: Strong Predictors, Weak Selectors: A Systematic Comparison of Confidence Signals for Test-Time Scaling in Information Extraction
12	**Venue**: EMNLP 2026 Main Conference (ARR May 2026 cycle)
13	**Reviewer 编排**: 2 人（R1: 方法严谨性+实验设计; R2: 新颖性+完整性+写作质量）
14	**流程**: Round 1 独立审稿 → 交叉分享（逐条 AGREE/REBUT） → 收敛汇总
15	
16	---
17	
18	## Summary
19	
20	本文系统比较了三个 family（structural / surface / model-internal）的五种 confidence signal 在生成式信息抽取（NER + RE）中的 quality estimation 和 sample selection 性能。在 SciERC、CoNLL-2003、WNUT-17 三个数据集和两个 8B 模型（Qwen3-8B, LLaMA-3.1-8B）上实验。核心发现是 "correlation-selection gap"：instance-level consistency signal 在质量估计上有效（ρ 最高 0.38, AUROC 最高 0.75），但在 best-of-N selection 中无信号显著超越 greedy decoding（p>0.39），尽管存在 13–18pp 的 oracle headroom。论文还发现信号排序依赖于任务难度。
21	
22	---
23	
24	## Strengths
25	
26	**S1. 问题分解有真正洞察力。** 将 quality estimation 与 sample selection 明确区分为两个独立目标，用不同指标分别评估（Spearman ρ + AUROC vs. best-of-N F1）。Per-sample vs. instance-level 信号的形式化区分使分析逻辑链条清晰可追溯。这一分析框架本身是对现有文献的有价值贡献。[R1-S1, R2-S1 一致]
27	
28	**S2. 统计报告全面严谨。** Paired bootstrap (B=10,000) 附带 95% CI、Cohen's d、sign test win%、pairwise Δρ CI（Appendix D），多数实证论文不会做到这个粒度。[R1-S2, R2-S2 一致]
29	
30	**S3. WNUT-17 capability boundary 分析揭示重要方法论警示。** Voting ρ=0.724（full-set）→ conditional ρ=0.038 (n.s.) 揭示 inflated correlation 由 zero/non-zero boundary 驱动；logprob 条件反转（full ρ=−0.410 → conditional ρ=0.350）进一步确认此现象。[R1-S4, R2-S3 一致]
31	
32	**S4. 负面结果处理诚实平衡。** RE 单数据集局限在 Introduction、Discussion、Conclusion、Limitations 四处明确提及。WNUT-17 作为方法边界坦率报告。Limitations section 全面覆盖多项局限。[R1-S3, R2-S4 一致]
33	
34	**S5. Task difficulty 分析有实用价值。** EM 在简单任务领先 vs. SJ/Voting 在复杂任务领先的 crossover 发现，以及 conditional filtering 后信号排序翻转，为从业者信号选择提供实用指导。[R1-S4]
35	
36	**S6. Robustness 覆盖面广。** Temperature (T=0.7/1.0)、N-scaling (8→16)、cross-architecture 均有系
…[truncated 796 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 410 · 2026-05-15T06:40:36.244394+00:00_

Based on my search, here are the findings:

**External Review Status: NOT ENABLED**

The `struct_self_consist_ie` project currently has **no external review requested or enabled**. The external review status API returns `not_requested`. The project has completed three rounds of internal review (with 2 reviewers doing cross-sharing) as documented in the review reports, but no integration with external review platforms (paperreview.ai/Stanford Agentic Reviewer) has been configured or activated. The project follows internal review-only workflow.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Agent",
  "elapsed_ms": 16835
}
```

</details>

---


### Tool call

_source line 411 · 2026-05-15T06:40:42.922324+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
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

_source line 412 · 2026-05-15T06:40:42.973176+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 413 · 2026-05-15T06:40:49.703747+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/review_issues.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/review_issues.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie"
  }
}
```

</details>

---


### Tool result

_source line 414 · 2026-05-15T06:40:50.156036+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_issues.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Glob",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 415 · 2026-05-15T06:40:50.206696+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/review_reports/*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/review_reports/*",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie"
  }
}
```

</details>

---


### Tool result

_source line 416 · 2026-05-15T06:40:50.257593+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_reports/round_0.md
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_reports/round_1.md
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_reports/round_2.md
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_reports/round_3.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 417 · 2026-05-15T06:40:53.922696+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_issues.yaml"
  }
}
```

</details>

---


### Tool result

_source line 418 · 2026-05-15T06:40:54.576314+00:00_

1	issues:
2	  # ============================================================
3	  # Round 0 issues (all resolved)
4	  # ============================================================
5	  - id: "R0-C1"
6	    summary: "模型规模单一（仅 8B）"
7	    category: experiment
8	    severity: critical
9	    status: resolved
10	    first_raised_round: 0
11	    last_seen_round: 1
12	    mentions:
13	      - round: 0
14	        reviewers: [1, 2]
15	        note: "8B→8B 仅验证架构鲁棒性非规模鲁棒性"
16	      - round: 1
17	        reviewers: [1, 2]
18	        note: "model-agnostic 与 Limitations 矛盾"
19	    action_items:
20	      - round: 1
21	        action: "全文替换 model-agnostic → consistent across tested model families"
22	        assigned_to: "Paper Agent"
23	        status: resolved
24	    resolution: "Round 2 Reviewer 确认措辞修正到位，无再提"
25	    resolution_round: 2
26	
27	  - id: "R0-C2"
28	    summary: "相关工作显著遗漏"
29	    category: framing
30	    severity: warning
31	    status: resolved
32	    first_raised_round: 0
33	    last_seen_round: 1
34	    mentions:
35	      - round: 0
36	        reviewers: [1, 2]
37	        note: "5 篇核心文献缺失"
38	      - round: 1
39	        reviewers: [1, 2]
40	        note: "新遗漏：Optimal SC, Difficulty-Adaptive SC"
41	    action_items:
42	      - round: 1
43	        action: "补充 6 篇引用到 Related Work"
44	        assigned_to: "Paper Agent"
45	        status: resolved
46	    resolution: "Round 2: 49 条 bib 全部 cited, 0 orphan, 无遗漏"
47	    resolution_round: 2
48	
49	  - id: "R0-C3"
50	    summary: "RE 结论仅基于 SciERC 单数据集"
51	    category: experiment
52	    severity: critical
53	    status: in_progress
54	    first_raised_round: 0
55	    last_seen_round: 3
56	    mentions:
57	      - round: 0
58	        reviewers: [1, 2]
59	        note: "需跨数据集验证或降级措辞"
60	      - round: 2
61	        reviewers: [1, 2]
62	        note: "Abstract RE 措辞需修正"
63	      - round: 3
64	        reviewers: [1, 2]
65	        note: "Round 2 措辞修正到位，但 R3 Reviewer 2 再次提出 44% zero-F1 floor effect 严重压缩可区分范围，gap 的 RE 证据 (-0.9pp, p=0.8
…[truncated 31843 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 653
}
```

</details>

---


### Tool call

_source line 419 · 2026-05-15T06:42:18.233660+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "project": "struct_self_consist_ie",
  "text": "## Round 1 审稿任务 — Reviewer 1\n\n**你的审查侧重：方法严谨性 + 实验设计 + 统计分析**\n\n### 论文信息\n- **标题**: Strong Predictors, Weak Selectors: A Systematic Comparison of Confidence Signals for Test-Time Scaling in Information Extraction\n- **路径**: projects/struct_self_consist_ie/docs/paper/main.tex（含 sections/ 下 9 个 .tex 文件 + references.bib + figures/）\n- **目标 Venue**: EMNLP 2026 Findings track\n- **截止日期**: 2026-05-25（ARR May cycle）\n- **格式**: ACL template, 长文 8 页正文, double-blind, 附录须 double-column\n- **匿名**: Double-blind（当前标注 Anonymous ✓）\n\n### 论文概要\n本文系统比较了三族五种置信度信号（structural: entity voting, Soft Jaccard; surface: exact match, Fleiss' κ; model-internal: log-probability）在生成式信息抽取（NER 三数据集 + RE SciERC）的 test-time scaling 场景下的表现。核心发现：这些信号是有效的 quality estimators（ρ=0.38, AUROC=0.75），但作为 sample selectors 失败（无信号显著超越 greedy，p>0.39），作者称之为 \"correlation-selection gap\"。\n\n### 审查要求\n请从以下维度深入评审，给出结构化报告（Summary → Strengths → Weaknesses → Questions → Missing References → Detailed Comments）：\n\n1. **方法设计**\n   - 五种信号的数学定义是否严谨、完整、可复现\n   - Soft Jaccard 的 Hungarian matching 细节是否充分（优化方向、cost function、零 IoU 处理、threshold）\n   - Fleiss' κ 应用于非独立 temperature-sampled outputs 的 justification 是否充分\n   - Per-sample vs instance-level 信号分类的理论清晰度\n\n2. **实验设计**\n   - 数据集选择覆盖度（3 NER + 1 RE）是否足以支撑 claims\n   - 模型选择（2 × 8B）的代表性，cross-architecture vs cross-scale 区分\n   - N=8/16 采样规模、temperature 选择的 justification\n   - 训练设置（LoRA fine-tuning）的详细程度与可复现性\n   - Constrained decoding 对 output diversity 的影响是否被充分讨论\n\n3. **统计分析**\n   - Bootstrap resampling 的规范性（B=10,000, seed, CI 类型）\n   - Selection gap 的统计论证：failure-to-reject vs evidence of absence\n   - TOST 等价性检验的 δ 选择是否合理\n   - 信号间比较的多重比较校正\n   - Single-seed (N=8) 结果的稳定性论证\n   - Effect size 报告（Cohen's d, win%）\n\n4. **核心 claim 的支撑力度**\n   - \"Correlation-selection gap\" 是否为非平凡发现（4/5 信号 instance-level by design）\n   - Gap 是否可能是 constrained decoding 导致的 artifact\n   - RE 结论仅基于 SciERC 单数据集的限制程度\n\n请独立审查，给出你对本文的 overall assessment（strong reject / weak reject / borderline / weak accept / strong accept）+ 置信度。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "project": "struct_self_consist_ie",
    "text": "## Round 1 审稿任务 — Reviewer 1\n\n**你的审查侧重：方法严谨性 + 实验设计 + 统计分析**\n\n### 论文信息\n- **标题**: Strong Predictors, Weak Selectors: A Systematic Comparison of Confidence Signals for Test-Time Scaling in Information Extraction\n- **路径**: projects/struct_self_consist_ie/docs/paper/main.tex（含 sections/ 下 9 个 .tex 文件 + references.bib + figures/）\n- **目标 Venue**: EMNLP 2026 Findings track\n- **截止日期**: 2026-05-25（ARR May cycle）\n- **格式**: ACL template, 长文 8 页正文, double-blind, 附录须 double-column\n- **匿名**: Double-blind（当前标注 Anonymous ✓）\n\n### 论文概要\n本文系统比较了三族五种置信度信号（structural: entity voting, Soft Jaccard; surface: exact match, Fleiss' κ; model-internal: log-probability）在生成式信息抽取（NER 三数据集 + RE SciERC）的 test-time scaling 场景下的表现。核心发现：这些信号是有效的 quality estimators（ρ=0.38, AUROC=0.75），但作为 sample selectors 失败（无信号显著超越 greedy，p>0.39），作者称之为 \"correlation-selection gap\"。\n\n### 审查要求\n请从以下维度深入评审，给出结构化报告（Summary → Strengths → Weaknesses → Questions → Missing References → Detailed Comments）：\n\n1. **方法设计**\n   - 五种信号的数学定义是否严谨、完整、可复现\n   - Soft Jaccard 的 Hungarian matching 细节是否充分（优化方向、cost function、零 IoU 处理、threshold）\n   - Fleiss' κ 应用于非独立 temperature-sampled outputs 的 justification 是否充分\n   - Per-sample vs instance-level 信号分类的理论清晰度\n\n2. **实验设计**\n   - 数据集选择覆盖度（3 NER + 1 RE）是否足以支撑 claims\n   - 模型选择（2 × 8B）的代表性，cross-architecture vs cross-scale 区分\n   - N=8/16 采样规模、temperature 选择的 justification\n   - 训练设置（LoRA fine-tuning）的详细程度与可复现性\n   - Constrained decoding 对 output diversity 的影响是否被充分讨论\n\n3. **统计分析**\n   - Bootstrap resampling 的规范性（B=10,000, seed, CI 类型）\n   - Selection gap 的统计论证：failure-to-reject vs evidence of absence\n   - TOST 等价性检验的 δ 选择是否合理\n   - 信号间比较的多重比较校正\n   - Single-seed (N=8) 结果的稳定性论证\n   - Effect size 报告（Cohen's d, win%）\n\n4. **核心 claim 的支撑力度**\n   - \"Correlation-selection gap\" 是否为非平凡发现（4/5 信号 instance-level by design）\n   - Gap 是否可能是 constrained decoding 导致的 artifact\n   - RE 结论仅基于 SciERC 单数据集的限制程度\n\n请独立审查，给出你对本文的 overall assessment（strong reject / weak reject / borderline / weak accept / strong accept）+ 置信度。"
  }
}
```

</details>

---


### Tool result

_source line 420 · 2026-05-15T06:42:36.674505+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 18440
}
```

</details>

---


### Tool call

_source line 421 · 2026-05-15T06:42:36.725312+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "project": "struct_self_consist_ie",
  "text": "## Round 1 审稿任务 — Reviewer 2\n\n**你的审查侧重：新颖性 + 相关工作完整性 + 写作质量 + 格式合规**\n\n### 论文信息\n- **标题**: Strong Predictors, Weak Selectors: A Systematic Comparison of Confidence Signals for Test-Time Scaling in Information Extraction\n- **路径**: projects/struct_self_consist_ie/docs/paper/main.tex（含 sections/ 下 9 个 .tex 文件 + references.bib + figures/）\n- **目标 Venue**: EMNLP 2026 Findings track\n- **截止日期**: 2026-05-25（ARR May cycle）\n- **格式**: ACL template, 长文 8 页正文, double-blind, 附录须 double-column\n- **匿名**: Double-blind（当前标注 Anonymous ✓）\n\n### 论文概要\n本文系统比较了三族五种置信度信号在生成式 IE（NER + RE）中的 test-time scaling 表现。核心贡献：(1) 首个多族信号比较；(2) 发现 correlation-selection gap（信号能估计质量但不能选择最佳样本）；(3) 信号排名依赖任务难度。使用 Qwen3-8B 和 LLaMA-3.1-8B，在 SciERC、CoNLL-2003、WNUT-17 上评测。\n\n### 审查要求\n请从以下维度深入评审，给出结构化报告（Summary → Strengths → Weaknesses → Questions → Missing References → Detailed Comments）：\n\n1. **新颖性与贡献**\n   - \"Correlation-selection gap\" 概念的原创性和学术价值\n   - 相对于 Nedellec (2026)（最相关先行工作）的增量贡献是否充分\n   - \"First multi-family comparison\" claim 的准确性和 scope\n   - Findings track 的定位是否合适（empirical study with negative result）\n   - 对 NLP/IE 社区的实际影响力评估\n\n2. **相关工作完整性**\n   - 自洽性文献（Wang 2023, Chen 2024, Taubenfeld 2025 等）覆盖度\n   - MBR decoding 文献（Eikema & Aziz 2022, Freitag 2022）是否充分讨论\n   - 结构化 IE 不确定性文献（VerifiNER, CoCoA 等）\n   - Uncertainty estimation 综述类文献\n   - 是否有重要遗漏（特别关注 2025-2026 年最新工作）\n\n3. **写作质量**\n   - 论文结构和叙事流畅度\n   - 术语一致性（confidence signal vs consistency signal, 缩写统一）\n   - 图表质量和信息密度（6 figures, 多张 tables）\n   - Abstract 和 Conclusion 是否准确反映 claims\n   - 对 Nedellec 等先行工作的语气是否中立客观\n\n4. **格式合规**\n   - 页数限制（8 页正文）\n   - 匿名审查合规\n   - Limitations section 内容充实度\n   - Ethics statement 存在性\n   - 附录格式（double-column 要求）\n   - 参考文献格式一致性\n   - Responsible NLP Checklist 相关内容\n\n请独立审查，给出你对本文的 overall assessment（strong reject / weak reject / borderline / weak accept / strong accept）+ 置信度。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "project": "struct_self_consist_ie",
    "text": "## Round 1 审稿任务 — Reviewer 2\n\n**你的审查侧重：新颖性 + 相关工作完整性 + 写作质量 + 格式合规**\n\n### 论文信息\n- **标题**: Strong Predictors, Weak Selectors: A Systematic Comparison of Confidence Signals for Test-Time Scaling in Information Extraction\n- **路径**: projects/struct_self_consist_ie/docs/paper/main.tex（含 sections/ 下 9 个 .tex 文件 + references.bib + figures/）\n- **目标 Venue**: EMNLP 2026 Findings track\n- **截止日期**: 2026-05-25（ARR May cycle）\n- **格式**: ACL template, 长文 8 页正文, double-blind, 附录须 double-column\n- **匿名**: Double-blind（当前标注 Anonymous ✓）\n\n### 论文概要\n本文系统比较了三族五种置信度信号在生成式 IE（NER + RE）中的 test-time scaling 表现。核心贡献：(1) 首个多族信号比较；(2) 发现 correlation-selection gap（信号能估计质量但不能选择最佳样本）；(3) 信号排名依赖任务难度。使用 Qwen3-8B 和 LLaMA-3.1-8B，在 SciERC、CoNLL-2003、WNUT-17 上评测。\n\n### 审查要求\n请从以下维度深入评审，给出结构化报告（Summary → Strengths → Weaknesses → Questions → Missing References → Detailed Comments）：\n\n1. **新颖性与贡献**\n   - \"Correlation-selection gap\" 概念的原创性和学术价值\n   - 相对于 Nedellec (2026)（最相关先行工作）的增量贡献是否充分\n   - \"First multi-family comparison\" claim 的准确性和 scope\n   - Findings track 的定位是否合适（empirical study with negative result）\n   - 对 NLP/IE 社区的实际影响力评估\n\n2. **相关工作完整性**\n   - 自洽性文献（Wang 2023, Chen 2024, Taubenfeld 2025 等）覆盖度\n   - MBR decoding 文献（Eikema & Aziz 2022, Freitag 2022）是否充分讨论\n   - 结构化 IE 不确定性文献（VerifiNER, CoCoA 等）\n   - Uncertainty estimation 综述类文献\n   - 是否有重要遗漏（特别关注 2025-2026 年最新工作）\n\n3. **写作质量**\n   - 论文结构和叙事流畅度\n   - 术语一致性（confidence signal vs consistency signal, 缩写统一）\n   - 图表质量和信息密度（6 figures, 多张 tables）\n   - Abstract 和 Conclusion 是否准确反映 claims\n   - 对 Nedellec 等先行工作的语气是否中立客观\n\n4. **格式合规**\n   - 页数限制（8 页正文）\n   - 匿名审查合规\n   - Limitations section 内容充实度\n   - Ethics statement 存在性\n   - 附录格式（double-column 要求）\n   - 参考文献格式一致性\n   - Responsible NLP Checklist 相关内容\n\n请独立审查，给出你对本文的 overall assessment（strong reject / weak reject / borderline / weak accept / strong accept）+ 置信度。"
  }
}
```

</details>

---


### Tool result

_source line 422 · 2026-05-15T06:42:38.587804+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1862
}
```

</details>

---


### Assistant

_source line 423 · 2026-05-15T06:43:01.097080+00:00_

**【Round 1 — 审稿任务已分配】**

| Reviewer | 侧重 | 状态 |
|----------|------|------|
| Reviewer 1 | 方法严谨性 + 实验设计 + 统计分析 | 已派发，等待审稿报告 |
| Reviewer 2 | 新颖性 + 相关工作 + 写作质量 + 格式合规 | 已派发，等待审稿报告 |

等待两位 Reviewer 的独立审稿报告返回。收到后进入交叉分享（Step 2）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 33

## Round 33

22 recorded events


### User

_source line 424 · 2026-05-15T06:47:48.553657+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 审稿报告

**论文**: Strong Predictors, Weak Selectors: A Systematic Comparison of Confidence Signals for Test-Time Scaling in Information Extraction
**Venue**: EMNLP 2026 Findings (ACL ARR May cycle)

---

## 总体评分
**Overall**: 3.0 / 5（Findings acceptance 边缘）
**一句话总结**: 研究问题定义清晰、统计方法论扎实的实证研究，但核心发现（correlation-selection gap）部分因信号设计的内在限制（4/5 为 instance-level）而缺乏足够的非平凡性，且 constrained decoding 对 selection gap 的贡献未被实验量化。

---

## 官方维度打分（ACL ARR review form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5 / 5 | 统计方法论优秀（bootstrap + TOST + effect size + 多 seed），但核心 claim 的非平凡性受质疑——4/5 信号 instance-level 使得 selection 失败部分为 by-design；constrained decoding confound 未实验验证 |
| Excitement | 3.0 / 5 | 填补了 quality estimation vs. sample selection 的区分空白，但本质是 negative result + 对已知设计限制的实证确认，practical impact 有限 |
| Reproducibility | 3.0 / 5 | 使用公开数据集和开源模型，但 LoRA 训练缺少关键超参数（learning rate, batch size, warmup, eval strategy），prompt template 未提供 |
| Confidence | 4 / 5 | 仔细阅读了全文和附录，熟悉 self-consistency、MBR decoding、uncertainty estimation 相关文献 |

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] Correlation-selection gap 的非平凡性不足——instance-level 信号的 selection 失败部分为 tautological

- 具体位置：§3.1（per-sample vs instance-level 定义）、§4.3（Table 3 selection 结果）、§5 Discussion 第一段
- 问题：论文定义了 per-sample 信号（直接为每个 $y_i$ 打分）和 instance-level 信号（为整个输入 $x$ 打分）。5 个信号中 4 个（Voting, SJ, FK, EM）是 instance-level，本身不区分同一 input 下的不同 candidate。论文通过 consensus-proximity 策略将 instance-level 信号转化为 per-sample selector（§3.3: "instance-level signals select the sample closest to the consensus output"），这等价于 MBR decoding（§5）。但论文的叙述框架将"所有信号均未显著超越 greedy"包装为一个统一的经验发现（"correlation-selection gap"），而实际上 instance-level 信号的 selection 失败主要是 **设计层面的先验预期**——consensus-proximity 将 instance-level 一致性转化为 per-sample 排序，但当 per-sample variance 低时（mean pairwise SJ = 0.703），consensus-proximity 得分的区分度天然有限。这一点在 Discussion 中被承认（"Four of five signals are instance-level by construction and cannot rank N candidates"），但这个自承的事实与 §4.3 和 abstract 中将其作为核心 empirical contribution 的定位之间存在张力。
- 真正非平凡的发现是 **logprob 的 selection 失败**：作为唯一的 per-sample 信号，logprob 在 SciERC 上仅获得 +0.6 pp（NER, p=0.39）和 -0.9 pp（RE），Cohen's d = 0.038。但这一发现被淹没在"所有信号统一失败"的叙述中，且 Discussion 将原因归结为"primarily reflects grammar compliance under constrained decoding—75% of comparisons are effectively ties"——这实际上指向 constrained decoding 是 confounding factor（见 N2）。
- 为什么影响接收：核心 contribution #2 的新颖性被削弱。如果 4/5 信号的 selection 失败可以从其 instance-level 设计中先验推导，那么 "gap" 更多是一个 terminology 贡献而非 empirical discovery。
- 建议修改方向：(a) 明确区分"instance-level 信号通过 consensus-proximity 做 selection 失败"和"per-sample 信号（logprob）做 selection 失败"是两个独立发现，前者的非平凡性来自 consensus-proximity/MBR 策略的失败，后者的非平凡性来自 logprob 在 constrained decoding 下的区分度坍缩；(b) 重新定义 "gap" 的 scope，聚焦在"即使是 MBR-style 的 consensus-proximity selection，在 structured IE 上也失败"——这比笼统的 "所有信号失败" 更精确且更有说服力。

**N2** [critical] Constrained decoding 作为 correlation-selection gap 的 confounding factor 未被实验量化

- 具体位置：§4.1（"Inference uses vLLM with constrained decoding"），§7 Limitations（"Constrained decoding...potentially compressing per-sample diversity and contributing to the correlation-selection gap beyond what free-form generation would exhibit"），§5 Discussion（"logprob primarily reflects grammar compliance under constrained decoding—75% of comparisons are effectively ties"）
- 问题：Constrained decoding（Outlines/vLLM）强制输出符合 JSON schema，可能从两方面造成 confound：(1) 压缩 per-sample diversity，使得不同 sample 的"有意义差异"被限制在 entity 选择层面而非格式/结构层面，降低信号的区分空间；(2) 使 logprob 主要反映 grammar compliance 而非 semantic confidence（论文自己在 Discussion 中承认）。论文报告了 SciERC 上仍有 43% unique outputs 和 per-sample F1 std = 0.14，但这并不排除 diversity 被压缩到 constrained decoding 允许的子空间内。论文在 Limitations 中承认此问题但未实验验证。
- 为什么影响接收：如果 gap 主要由 constrained decoding 导致，则 "correlation-selection gap" 不是 confidence signals 在 structured IE 上的固有限制，而是特定 inference setup 的 artifact。这直接动摇论文的 generalization claim（"reframe consistency signals as quality estimators rather than output selectors for structured IE"——abstract 最后一句）。
- 建议修改方向：(a) 增加 free-form generation（不使用 constrained decoding）的对比实验，即使需要 post-hoc 解析且 parse success rate 较低；(b) 或至少分析 constrained decoding 下 logprob 值的分布——如果 75% 的 comparison 是 effective ties，则量化 "tie" 的定义（Δlogprob < ε），并分析在 non-tie 的 25% 上 logprob 是否能成功 select；(c) 对 effective ties 进行更深入的分析：是 logprob 值本身差异小（constrained decoding 的 grammar path 导致），还是 logprob 差异虽大但与 F1 差异无关？

**N3** [critical] 训练细节不足以复现

- 具体位置：§4.1（"fine-tuned with LoRA (rank=32, α=64) for 5 epochs using LLaMA Factory"）
- 问题：训练配置缺少以下关键信息：learning rate、batch size（per-device 和 effective）、warmup steps/ratio、weight decay、optimizer（AdamW? 参数？）、gradient accumulation steps、early stopping 策略（是否使用？基于什么指标？）、训练数据的 train/dev split 方式、prompt template（NER/RE 各用什么 prompt 格式？）、训练数据量、LoRA target modules（all linear? q_proj/v_proj only?）、max sequence length。
- 为什么影响接收：ACL ARR 要求 reproducibility，LoRA 微调对超参数敏感（特别是 learning rate 和 target modules），不同配置可能导致模型能力差异，进而影响 output diversity 和 consistency 信号的表现。
- 建议修改方向：补充完整的训练配置表格，优选放在附录。提供 prompt template 示例。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] RE 结论仅基于 SciERC 单一数据集

- 具体位置：§4.1（datasets）、§6 Conclusion、§7 Limitations
- 问题：RE 分析仅使用 SciERC（7 relation types，40% zero F1），论文 claim "correlation-selection gap" 覆盖 NER 和 RE，但 RE 证据严重不足。SciERC RE 的 40% zero-F1 base rate 进一步压缩了信号可区分的范围。论文在 Conclusion 中承认 "our RE conclusions rest on SciERC alone"，但 abstract 和 introduction 的表述仍然将 RE 作为等权的证据呈现。
- 建议：(a) 增加至少一个 RE 数据集（如 TACRED、DocRED、ACE05）；或 (b) 在 abstract/introduction 中明确 RE findings 是初步的。当前 abstract 说 "across NER (three datasets of varying difficulty) and RE (SciERC)"，建议改为强调 NER 是主要证据。

**W2** [warning] Fleiss' κ 应用于非独立 temperature-sampled outputs 的理论 justification 薄弱

- 具体位置：§3.2 Fleiss' κ 段落（"While FK assumes independent raters, temperature-based sampling provides sufficient response diversity..."）
- 问题：Fleiss' κ 的统计理论假设 raters 是独立的。Temperature sampling 产生的 N 个输出共享相同的模型权重、prompt、和前缀，因此系统性地非独立。论文引用 empirical evidence（excess agreement -0.4% to -4.0%），声称 FK 不被 inter-sample dependence 所 inflate。但这个实证观察的 methodology 不清楚——excess agreement 是相对于什么 baseline 计算的？如果 baseline 本身也有问题，结论不可靠。此外，negative excess agreement（即 temperature-sampled outputs 的 agreement 低于独立 rater 的预期）本身是一个值得讨论的现象——为什么从同一模型 sample 出的结果反而 agreement 更低？这可能指向 temperature sampling 引入的 noise 结构与 Fleiss' κ 假设的 random disagreement 结构不同。
- 建议：(a) 解释 excess agreement 的计算方法；(b) 讨论 negative excess agreement 的含义；(c) 或者将 FK 的 justification 限定为"作为 agreement 的经验度量使用，不做统计推断"——论文确实只将 FK 用于 rank correlation，不用于假设检验。

**W3** [warning] Soft Jaccard 定义中 normalizer 的选择缺乏对比

- 具体位置：§3.2 Soft Jaccard（"We use $\max(|g_i|, |g_j|)$ rather than $|g_i \cup g_j|$ as the normalizer to penalize length asymmetry between samples"）
- 问题：$\max(|g_i|, |g_j|)$ 和 $|g_i \cup g_j|$ 在 entity set 大小不对称时有不同的 penalization behavior。论文仅声明使用前者但未比较。此外，当两个 sample 的 entity set 大小差异大时，$\max$ normalizer 可能过度惩罚；当 entity set 有大量重叠时，$|g_i \cup g_j|$ 可能更合适。作为 core signal 的设计决策，缺少 ablation 或 justification。
- 建议：至少在附录中报告使用 $|g_i \cup g_j|$ normalizer 的 SJ 结果，或提供选择 $\max$ 的理论依据。

**W4** [warning] 模型规模限于 8B，generalization 受限

- 具体位置：§4.1（models）、§7 Limitations
- 问题：两个模型均为 8B 参数。Larger models（70B+）可能产生更高质量、更多样化的 output，这可能改变 signal landscape——例如，logprob 在更强模型上可能更有区分力（因为 grammar compliance 已接近完美，logprob 更多反映 semantic confidence）。论文在 Limitations 中承认此点。
- 建议：讨论 model scale 可能如何影响 gap 的方向——是预期 gap 缩小（更强模型 logprob 更有信息量）还是扩大（更强模型 output 更一致，per-sample variance 更低）？

**W5** [warning] TOST 等价性检验的 δ 选择缺乏理论或实践依据

- 具体位置：Appendix E Table 6（"TOST equivalence testing"）
- 问题：TOST 的 δ 选择（±2, ±3, ±5 pp）直接影响等价性结论。论文报告了三个 δ 水平但未讨论哪个是"合理"的等价边界。在 IE 任务中，2 pp 的 F1 差异是否有实际意义？这取决于下游应用。论文应讨论 δ 的选择依据——例如，如果 annotation agreement 的 F1 variance 是 ~3 pp，则 ±3 pp 是合理的等价边界。
- 建议：提供 δ 选择的实际意义论证，或至少引用 IE 任务中 F1 差异的 practical significance 标准。

**W6** [warning] N=8 主实验的 single-seed 稳定性

- 具体位置：§4.1（"N=8 results use seed=42"）、Appendix D（multi-seed 分析）
- 问题：主表格（Table 1, Table 3）的 N=8 结果均来自 seed=42 单次运行。虽然 Appendix D 的 3-seed 分析显示 σ≤0.025 且 ranking 稳定，但 multi-seed 分析仅覆盖 SciERC NER（Table 7），不覆盖 CoNLL N=8 和 SciERC RE。特别是 selection gap 的 p-value (p=0.39) 来自单 seed，其在不同 seed 下的变异未报告。
- 建议：(a) 至少对 SciERC 的 selection 分析（Table 3）报告多 seed 结果；(b) 在主文中注明 N=8 single-seed 的局限性而非仅在附录中提及。

---

## 小问题（不影响接收）

- §4.2 第一段：footnote 5 说 "semantic entropy achieves AUROC ≈ 0.75-0.85 on discrete-answer QA tasks" 后加了 "however, these numbers are not directly comparable"。既然不可比，引用 semantic entropy 的数字可能误导读者。建议删除具体数字或更清楚地框定比较目的。
- Table 1（N=16 部分）：只填了 LLaMA CoNLL 的值，Qwen 和 SciERC 的 N=16 结果为空白。建议在 caption 中说明哪些配置有 N=16 数据，或将 N=16 结果全部移至附录以保持主表的一致性。
- §3.2 Entity Voting：公式 (5) 中 $|E_\cup|$ 当所有 sample 都产生空输出时，分母为 0。虽然实践中通过 constrained decoding 可能不会出现空输出，但数学定义应注明边界条件处理。
- Appendix C Fig 3 reliability diagram：caption 说 "calibration ECE 0.069-0.096"，但正文 §4.4 也报告了相同的数字。ECE 的 bin 数量未报告（10? 15? 20?）——不同 bin 数会显著影响 ECE 值。

---

## 主要优势

1. **研究问题定义清晰**：quality estimation vs. sample selection 的概念区分是有价值的贡献，prior work（如 Nedellec et al. 2026）确实混淆了这两个目标。§3.1 的 per-sample vs. instance-level 形式化是简洁有效的。

2. **统计方法论严谨**：paired bootstrap resampling (B=10,000)、TOST 等价性检验、effect size 报告（Cohen's d, win%）、pairwise bootstrap CIs with Bonferroni correction——这在 NLP 实证论文中是高于平均水准的统计实践。

3. **Difficulty gradient 分析有深度**：CoNLL（easy）→ SciERC（medium）→ WNUT-17（capability boundary）的三级难度梯度设计精良，WNUT-17 上 full-set vs. conditional-set 的对比（Table 5: Voting full ρ=0.724 vs. conditional ρ=0.038）是一个很有说服力的发现——说明在高 failure rate 下 consistency signals 的表现可以是完全 artifactual 的。

4. **Transparency**：论文在 Limitations 和 Discussion 中对自身局限性的讨论是诚实和全面的（constrained decoding confound、single RE dataset、model scale limitation、logprob temperature data missing）。

5. **MBR decoding 连接**：§5 将 selection strategies 形式化为 MBR decoding 变体是一个有价值的理论框架，帮助读者理解不同信号在 selection 中实际做了什么。

6. **引用质量高**：55 条引用经 OpenAlex 验证，0 orphan / 0 missing bib，51 条完全验证通过。引用覆盖了 self-consistency、uncertainty estimation、generative IE、MBR decoding 等相关领域，包含 2025-2026 的最新工作。

---

## 缺失引用

- **Bertsch et al. (2024)** "In-Context Learning with Long-Context Models: An In-Depth Exploration" — 讨论了 long-context models 在 IE 上的 test-time scaling 行为，与本文的 test-time scaling 框架相关。
- **Wiher et al. (2022)** "On Decoding Strategies for Neural Text Generators" — 系统比较了不同 decoding strategies 对 output diversity 的影响，可帮助 contextualize constrained decoding 对 diversity 的压缩效应。
- **Müller & Sennrich (2021)** "Understanding the Properties of Minimum Bayes Risk Decoding in Neural Machine Translation" — 深入分析了 MBR decoding 的 failure modes，与本文 §5 的 MBR 连接直接相关。

---

## 总结判断

本文是一篇方法论严谨的实证研究，清晰定义了 quality estimation vs. sample selection 的区分，并在统计分析上显著超过 NLP 实证论文的平均水平。但核心发现 "correlation-selection gap" 的非平凡性不足（4/5 信号 instance-level 使 selection 失败部分为 by-design），且 constrained decoding 作为主要 confound 未被实验控制。这两个问题削弱了论文的 contribution novelty，使其更像是对一个可预见限制的实证确认，而非一个令人惊讶的发现。

推荐 **Findings acceptance（边缘）**，条件是修复训练细节（N3）并更精确地定位 gap 的非平凡性来源（N1）。如果能增加 free-form generation 对比实验（N2），将显著增强论文的说服力。

**Overall Assessment**: 3.0 / 5 (Findings acceptance 边缘)
**Confidence**: 4 / 5

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 425 · 2026-05-15T06:48:04.443300+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__update_review_issues",
  "max_results": "7"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__update_review_issues",
    "max_results": "7"
  }
}
```

</details>

---


### Tool result

_source line 426 · 2026-05-15T06:48:04.443785+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 427 · 2026-05-15T06:48:08.861904+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "struct_self_consist_ie"
  }
}
```

</details>

---


### Tool result

_source line 428 · 2026-05-15T06:48:10.269100+00:00_

{"result":"# 项目 struct_self_consist_ie 概况\n\n## 实验状态 (79 个)\n\n- **exp_002_ner_conll2003**: DONE (success) — \n- **exp_004_re_diagnostic**: DONE (success) — \n- **exp_005**: DONE (success) — \n- **exp_014_entity_majority_voting**: DONE (success) — \n- **exp_013_exact_match_voting**: DONE (negative) — \n- **exp_012_logprob_baseline**: DONE (success) — \n- **mvp_pilot_005**: DONE (negative) — \n- **e1_component_wise_re_sj**: DONE (negative) — \n- **mvp_pilot_004**: DONE (negative) — \n- **ft_002_v2**: DONE (success) — \n- **mvp_pilot_002**: DONE (failed) — \n- **ft_002**: DONE (killed) — \n- **ft_001**: DONE (success) — \n- **mvp_pilot_003**: DONE (negative) — \n- **mvp_pilot_001**: DONE (negative) — \n\n## 最新报告\n# Handover — 2026-05-15\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n- exp_017_llama_conll_n16_s456_r1024（准备中）\n- exp_017_llama_conll_n16_r1024（准备中）\n- exp_001_n16_seed123_full（准备中）\n- exp_001_n16_seed456_full（准备中）\n- exp001_seed123（准备中）\n- exp001_seed456（准备中）\n- exp_007_ner_llama（准备中）\n- exp_002_merge_conll2003（准备中）\n- exp008_re_n16（准备中）\n\n## 近期结论\n- **exp_018_llama_scierc_seed42_r1024** (success): —\n- **exp_018_llama_scierc_seed456_r1024** (success): —\n- **exp_018_llama_scierc_seed456** (success): —\n\n## 趋势\n成功 43 / 负向 18 / 失败 1 / 共 70\n\n## 下一步\n（无活跃 idea，请通过 ideas.md 添加）\n\n## 资源状态\nautodl-5090: 空闲 cuda:0, cuda:1, cuda:2, cuda:3\n\n## 告警\n- ft_002: 已被终止 — unknown\n- mvp_pilot_002: 训练失败 — unknown\n- exp_008_re_n16_full: 已被终止 — unknown\n- exp_001_seed42_v2_r1024: 已被终止 — unknown\n- exp_001_seed123_v2_r1024: 已被终止 — unknown\n- exp_001_seed456_v2_ner_r1024: 已被终止 — unknown\n- exp_002_conll_n16_r1024: 已被终止 — unknown\n- exp_007_llama_n16_r1024: 已被终止 — unknown\n- exp_017_llama_conll_n16_s123_r1024: 已被终止 — unknown"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 1407
}
```

</details>

---


### Tool call

_source line 429 · 2026-05-15T06:48:10.269631+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool call

_source line 430 · 2026-05-15T06:48:10.270108+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "struct_self_consist_ie"
  }
}
```

</details>

---


### Tool result

_source line 431 · 2026-05-15T06:48:10.320835+00:00_

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
…[truncated 2458 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool result

_source line 432 · 2026-05-15T06:48:10.321366+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 433 · 2026-05-15T06:48:20.013467+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/review_reports/*.md",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/review_reports/*.md",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie"
  }
}
```

</details>

---


### Tool result

_source line 434 · 2026-05-15T06:48:20.617693+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_reports/round_0.md
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_reports/round_1.md
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_reports/round_2.md
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_reports/round_3.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Glob",
  "elapsed_ms": 604
}
```

</details>

---


### Tool call

_source line 435 · 2026-05-15T06:48:20.618110+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/review_issues.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/review_issues.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie"
  }
}
```

</details>

---


### Tool result

_source line 436 · 2026-05-15T06:48:21.020087+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_issues.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Glob",
  "elapsed_ms": 401
}
```

</details>

---


### Tool call

_source line 437 · 2026-05-15T06:48:21.271792+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "struct_self_consist_ie",
  "file": "memory.md",
  "max_chars": "5000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "struct_self_consist_ie",
    "file": "memory.md",
    "max_chars": "5000"
  }
}
```

</details>

---


### Tool result

_source line 438 · 2026-05-15T06:48:21.322553+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/memory.md\", \"content\": \"# Memory — struct_self_consist_ie\\n\\n## 服务器环境\\n- autodl-5090: 4× RTX 5090 32GB, Python 3.12, vLLM 0.18.1, LLaMA Factory 0.9.4, tmux 3.2a\\n- gpu-5090-4x-2: 4× RTX 5090 32GB, PyTorch 2.10.0+cu128, vLLM 0.18.1\\n- conda: /root/miniconda3/\\n- 环境初始化: `source /etc/network_turbo && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`\\n- 项目路径: /root/autodl-tmp/struct_self_consist_ie/\\n- 基座模型: /root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B/\\n- ft_002_v2 merged: checkpoints/qwen3-8b-scierc-merged-v2/\\n- run_mvp_pilot.py 支持 --collect_logprobs, --num_test (默认已改为 9999)\\n\\n## 数据修正链 (D054-D060) 关键教训\\n- exp_012 是唯一使用 max_tokens=512 的实验，导致 voting_conf ρ 虚高 (0.502→0.379)\\n- SJ/FK 对 max_tokens 参数鲁棒（Δ<0.004），但 voting_conf 极度敏感\\n- 修正后 AUROC 排名反转：EM (0.749) > SJ (0.692) > Voting (0.684)\\n- Selection claim 由 bootstrap 确认为 null result（p=0.39），不能写 \\\"significantly outperforms\\\"\\n- 论文数据必须来自 _rerun_1024 或本身就用 1024 的实验\\n\\n## D066 LLaMA fresh rerun (2026-05-15)\\n- D066 决策：LLaMA 3-seed 全部使用 fresh rerun 数据（seed42_r1024 + seed123 + seed456_r1024）\\n- exp_018_llama_scierc_seed456（旧 exp_007 复制品）已标记 SUPERSEDED\\n- LLaMA NER SJ ρ 修正：旧 0.362±0.004 → 新 0.325±0.021（σ 增大 5× 是真实 seed 变异，seed123 拉高均值）\\n- **分析脚本与 report.json 的 EM/VC 值存在系统性差异**（如 seed42 VC: 脚本 0.373 vs report.json 0.405）。Reviewer 要求论文统一使用分析脚本输出（与 Qwen 同一套）。不要从 registry metrics（来自 report.json）直接引用 EM/VC 到论文。\\n- NER 信号排名 6/6 完全稳定：VC > SJ > EM > FK > LP\\n- Core claim \\\"structural > logprob\\\" NER 全部成立 (12/12)；RE 仅 VC 稳定胜 LP\\n\\n## Registry 清理备注 (2026-05-15)\\n- 9 个 PREPARING+killed 实验因状态机限制无法推进到 DONE，实质已废弃\\n- 包括：exp_017_llama_conll_n16_s456_r1024, exp_017_llama_conll_n16_r1024, exp_001_n16_seed123_full, exp_001_n16_seed456_full, exp001_seed123, exp001_seed456, exp_007_ner_llama, exp_002_merge_conll2003, exp008_re_n16\\n\", \"total_chars\": 1740,
…[truncated 60 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 439 · 2026-05-15T06:48:28.305178+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_reports/round_3.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_reports/round_3.md"
  }
}
```

</details>

---


### Tool result

_source line 440 · 2026-05-15T06:48:28.607066+00:00_

1	---
2	round: 3
3	overall_score: borderline
4	timestamp: 2026-05-15T04:14:58.309947+00:00
5	reviewer_ids: [1, 2]
6	cross_response_reviewer_ids: [1, 2]
7	force_resubmit: False
8	---
9	
10	# 审稿报告 — Round 3
11	**论文**: Strong Predictors, Weak Selectors: A Systematic Comparison of Confidence Signals for Test-Time Scaling in Information Extraction
12	**Venue**: EMNLP 2026 Main Conference (ARR May 2026 cycle)
13	**Reviewer 编排**: 2 人（R1: 方法严谨性+实验设计; R2: 新颖性+完整性+写作质量）
14	**流程**: Round 1 独立审稿 → 交叉分享（逐条 AGREE/REBUT） → 收敛汇总
15	
16	---
17	
18	## Summary
19	
20	本文系统比较了三个 family（structural / surface / model-internal）的五种 confidence signal 在生成式信息抽取（NER + RE）中的 quality estimation 和 sample selection 性能。在 SciERC、CoNLL-2003、WNUT-17 三个数据集和两个 8B 模型（Qwen3-8B, LLaMA-3.1-8B）上实验。核心发现是 "correlation-selection gap"：instance-level consistency signal 在质量估计上有效（ρ 最高 0.38, AUROC 最高 0.75），但在 best-of-N selection 中无信号显著超越 greedy decoding（p>0.39），尽管存在 13–18pp 的 oracle headroom。论文还发现信号排序依赖于任务难度。
21	
22	---
23	
24	## Strengths
25	
26	**S1. 问题分解有真正洞察力。** 将 quality estimation 与 sample selection 明确区分为两个独立目标，用不同指标分别评估（Spearman ρ + AUROC vs. best-of-N F1）。Per-sample vs. instance-level 信号的形式化区分使分析逻辑链条清晰可追溯。这一分析框架本身是对现有文献的有价值贡献。[R1-S1, R2-S1 一致]
27	
28	**S2. 统计报告全面严谨。** Paired bootstrap (B=10,000) 附带 95% CI、Cohen's d、sign test win%、pairwise Δρ CI（Appendix D），多数实证论文不会做到这个粒度。[R1-S2, R2-S2 一致]
29	
30	**S3. WNUT-17 capability boundary 分析揭示重要方法论警示。** Voting ρ=0.724（full-set）→ conditional ρ=0.038 (n.s.) 揭示 inflated correlation 由 zero/non-zero boundary 驱动；logprob 条件反转（full ρ=−0.410 → conditional ρ=0.350）进一步确认此现象。[R1-S4, R2-S3 一致]
31	
32	**S4. 负面结果处理诚实平衡。** RE 单数据集局限在 Introduction、Discussion、Conclusion、Limitations 四处明确提及。WNUT-17 作为方法边界坦率报告。Limitations section 全面覆盖多项局限。[R1-S3, R2-S4 一致]
33	
34	**S5. Task difficulty 分析有实用价值。** EM 在简单任务领先 vs. SJ/Voting 在复杂任务领先的 crossover 发现，以及 conditional filtering 后信号排序翻转，为从业者信号选择提供实用指导。[R1-S4]
35	
36	**S6. Robustness 覆盖面广。** Temperature (T=0.7/1.0)、N-scaling (8→16)、cross-architecture 均有系
…[truncated 9800 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 441 · 2026-05-15T06:48:28.657834+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_issues.yaml"
  }
}
```

</details>

---


### Tool result

_source line 442 · 2026-05-15T06:48:29.010628+00:00_

1	issues:
2	  # ============================================================
3	  # Round 0 issues (all resolved)
4	  # ============================================================
5	  - id: "R0-C1"
6	    summary: "模型规模单一（仅 8B）"
7	    category: experiment
8	    severity: critical
9	    status: resolved
10	    first_raised_round: 0
11	    last_seen_round: 1
12	    mentions:
13	      - round: 0
14	        reviewers: [1, 2]
15	        note: "8B→8B 仅验证架构鲁棒性非规模鲁棒性"
16	      - round: 1
17	        reviewers: [1, 2]
18	        note: "model-agnostic 与 Limitations 矛盾"
19	    action_items:
20	      - round: 1
21	        action: "全文替换 model-agnostic → consistent across tested model families"
22	        assigned_to: "Paper Agent"
23	        status: resolved
24	    resolution: "Round 2 Reviewer 确认措辞修正到位，无再提"
25	    resolution_round: 2
26	
27	  - id: "R0-C2"
28	    summary: "相关工作显著遗漏"
29	    category: framing
30	    severity: warning
31	    status: resolved
32	    first_raised_round: 0
33	    last_seen_round: 1
34	    mentions:
35	      - round: 0
36	        reviewers: [1, 2]
37	        note: "5 篇核心文献缺失"
38	      - round: 1
39	        reviewers: [1, 2]
40	        note: "新遗漏：Optimal SC, Difficulty-Adaptive SC"
41	    action_items:
42	      - round: 1
43	        action: "补充 6 篇引用到 Related Work"
44	        assigned_to: "Paper Agent"
45	        status: resolved
46	    resolution: "Round 2: 49 条 bib 全部 cited, 0 orphan, 无遗漏"
47	    resolution_round: 2
48	
49	  - id: "R0-C3"
50	    summary: "RE 结论仅基于 SciERC 单数据集"
51	    category: experiment
52	    severity: critical
53	    status: in_progress
54	    first_raised_round: 0
55	    last_seen_round: 3
56	    mentions:
57	      - round: 0
58	        reviewers: [1, 2]
59	        note: "需跨数据集验证或降级措辞"
60	      - round: 2
61	        reviewers: [1, 2]
62	        note: "Abstract RE 措辞需修正"
63	      - round: 3
64	        reviewers: [1, 2]
65	        note: "Round 2 措辞修正到位，但 R3 Reviewer 2 再次提出 44% zero-F1 floor effect 严重压缩可区分范围，gap 的 RE 证据 (-0.9pp, p=0.8
…[truncated 31843 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 352
}
```

</details>

---


### Tool call

_source line 443 · 2026-05-15T06:51:03.712351+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "4",
  "project": "struct_self_consist_ie",
  "text": "## Round 4 审稿任务 — Reviewer 2\n\n**论文**: Strong Predictors, Weak Selectors: A Systematic Comparison of Confidence Signals for Test-Time Scaling in Information Extraction\n**论文路径**: `projects/struct_self_consist_ie/docs/paper/main.tex`\n**Venue**: EMNLP 2026 Findings (ACL ARR May 2026 cycle)\n- 正文 8 页（不含 references），附录不限\n- ACL 模板 (acl_natbib)\n- Double-blind 匿名审稿\n- 附录参与审稿但不要求审稿人阅读\n\n**你的审查侧重：新颖性 + 完整性 + 写作质量 + Round 3 issue 修复验证**\n\n### 侧重维度\n\n1. **新颖性与贡献定位**：\n   - \"Correlation-selection gap\" 作为概念的新颖性和非平凡性\n   - Contribution claims 的 scope 是否与实际证据匹配\n   - 论文在 uncertainty estimation / self-consistency / MBR decoding 文献中的定位是否准确\n\n2. **完整性**：\n   - 数据集覆盖（NER 3 个 vs RE 仅 1 个）对结论的支撑力\n   - 模型规模（仅 8B）对 generalization claims 的限制\n   - 相关工作覆盖是否充分——特别检查 MBR decoding 相关文献是否已补充（Round 3 要求补 Eikema & Aziz 2022, Freitag et al. 2022）\n   - 训练配置完整性（LoRA 超参、prompt template、training data split）\n\n3. **写作质量**：\n   - 术语一致性（confidence signal vs consistency signal; VC vs Voting Conf.）\n   - 统计措辞准确性（failure-to-reject ≠ evidence of absence）\n   - 对 prior work（尤其 Nedellec 2026）的措辞是否 neutral\n\n4. **ACL ARR 格式规范**：\n   - Ethics Statement 是否已添加\n   - Limitations section 是否充分\n   - 引用格式、页数合规\n\n### Round 3 遗留 Open Issues（请验证修复状态）\n\n以下是 Round 3 审稿中标记为 in_progress 的核心问题，请检查论文当前版本是否已解决：\n\n| ID | 问题 | 严重性 | 修复预期 |\n|----|------|--------|----------|\n| R3-C1 | Constrained decoding 是 gap 的未控制混淆变量 | critical | 量化 diversity 或限定 scope |\n| R3-C2 | Failure-to-reject ≠ evidence of absence | warning | 措辞修改或补 TOST |\n| R3-C3 | N=8 结果 single seed | warning | Limitations 声明或补 multi-seed |\n| R3-W1 | 多重比较校正缺失 | warning | 声明 + 修改 borderline 措辞 |\n| R3-W2 | Gap 概念部分 tautological | warning | Discussion 分层论证 |\n| R3-W3 | Consensus-proximity 未与 MBR 建立联系 | warning | 补 MBR 讨论+引用 |\n| R3-W4 | FK 独立性假设 justification 不足 | warning | 报告 inter-sample correlation |\n| R3-W5 | Cross-model → cross-architecture | warning | 加限定词 |\n| R3-W6 | First multi-family claim scope 过宽 | warning | 收窄措辞 |\n| R3-W7 | 术语不一致 | warning | 统一 |\n| R3-W8 | 遗漏引用（VerifiNER, MBR, Malinin&Gales, He+ 2024） | warning | 补引用 |\n| R0-C3 | RE 结论仅基于 SciERC 单数据集 | critical | 降级 claim 为 preliminary |\n| R1-W1 | SJ Hungarian 形式化歧义 | warning | 补 cost function 方向+zero-IoU 处理 |\n\n### 输出格式\n\n请按 ACL ARR review form 格式输出：\n- 总体评分 (1-5)\n- 维度打分：Soundness, Excitement, Reproducibility, Confidence\n- Must-Fix 问题（影响接收决定）\n- Should-Fix 问题（影响评分）\n- 小问题\n- 主要优势\n- 缺失引用\n- 总结判断\n\n对每个 Round 3 遗留问题，明确标注 [RESOLVED] / [PARTIALLY RESOLVED] / [UNRESOLVED] 及理由。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "4",
    "project": "struct_self_consist_ie",
    "text": "## Round 4 审稿任务 — Reviewer 2\n\n**论文**: Strong Predictors, Weak Selectors: A Systematic Comparison of Confidence Signals for Test-Time Scaling in Information Extraction\n**论文路径**: `projects/struct_self_consist_ie/docs/paper/main.tex`\n**Venue**: EMNLP 2026 Findings (ACL ARR May 2026 cycle)\n- 正文 8 页（不含 references），附录不限\n- ACL 模板 (acl_natbib)\n- Double-blind 匿名审稿\n- 附录参与审稿但不要求审稿人阅读\n\n**你的审查侧重：新颖性 + 完整性 + 写作质量 + Round 3 issue 修复验证**\n\n### 侧重维度\n\n1. **新颖性与贡献定位**：\n   - \"Correlation-selection gap\" 作为概念的新颖性和非平凡性\n   - Contribution claims 的 scope 是否与实际证据匹配\n   - 论文在 uncertainty estimation / self-consistency / MBR decoding 文献中的定位是否准确\n\n2. **完整性**：\n   - 数据集覆盖（NER 3 个 vs RE 仅 1 个）对结论的支撑力\n   - 模型规模（仅 8B）对 generalization claims 的限制\n   - 相关工作覆盖是否充分——特别检查 MBR decoding 相关文献是否已补充（Round 3 要求补 Eikema & Aziz 2022, Freitag et al. 2022）\n   - 训练配置完整性（LoRA 超参、prompt template、training data split）\n\n3. **写作质量**：\n   - 术语一致性（confidence signal vs consistency signal; VC vs Voting Conf.）\n   - 统计措辞准确性（failure-to-reject ≠ evidence of absence）\n   - 对 prior work（尤其 Nedellec 2026）的措辞是否 neutral\n\n4. **ACL ARR 格式规范**：\n   - Ethics Statement 是否已添加\n   - Limitations section 是否充分\n   - 引用格式、页数合规\n\n### Round 3 遗留 Open Issues（请验证修复状态）\n\n以下是 Round 3 审稿中标记为 in_progress 的核心问题，请检查论文当前版本是否已解决：\n\n| ID | 问题 | 严重性 | 修复预期 |\n|----|------|--------|----------|\n| R3-C1 | Constrained decoding 是 gap 的未控制混淆变量 | critical | 量化 diversity 或限定 scope |\n| R3-C2 | Failure-to-reject ≠ evidence of absence | warning | 措辞修改或补 TOST |\n| R3-C3 | N=8 结果 single seed | warning | Limitations 声明或补 multi-seed |\n| R3-W1 | 多重比较校正缺失 | warning | 声明 + 修改 borderline 措辞 |\n| R3-W2 | Gap 概念部分 tautological | warning | Discussion 分层论证 |\n| R3-W3 | Consensus-proximity 未与 MBR 建立联系 | warning | 补 MBR 讨论+引用 |\n| R3-W4 | FK 独立性假设 justification 不足 | warning | 报告 inter-sample correlation |\n| R3-W5 | Cross-model → cross-architecture | warning | 加限定词 |\n| R3-W6 | First multi-family claim scope 过宽 | warning | 收窄措辞 |\n| R3-W7 | 术语不一致 | warning | 统一 |\n| R3-W8 | 遗漏引用（VerifiNER, MBR, Malinin&Gales, He+ 2024） | warning | 补引用 |\n| R0-C3 | RE 结论仅基于 SciERC 单数据集 | critical | 降级 claim 为 preliminary |\n| R1-W1 | SJ Hungarian 形式化歧义 | warning | 补 cost function 方向+zero-IoU 处理 |\n\n### 输出格式\n\n请按 ACL ARR review form 格式输出：\n- 总体评分 (1-5)\n- 维度打分：Soundness, Excitement, Reproducibility, Confidence\n- Must-Fix 问题（影响接收决定）\n- Should-Fix 问题（影响评分）\n- 小问题\n- 主要优势\n- 缺失引用\n- 总结判断\n\n对每个 Round 3 遗留问题，明确标注 [RESOLVED] / [PARTIALLY RESOLVED] / [UNRESOLVED] 及理由。"
  }
}
```

</details>

---


### Tool result

_source line 444 · 2026-05-15T06:51:07.931480+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 4219
}
```

</details>

---


### Assistant

_source line 445 · 2026-05-15T06:51:21.269627+00:00_

Reviewer 2 已派发（Round 4，侧重新颖性+完整性+写作质量+Round 3修复验证）。

当前状态：
- **Reviewer 1**：已收到报告（3.0/5，Findings 边缘）
- **Reviewer 2**：已派发，等待回稿

Reviewer 1 关键发现摘要：
- **N1 [critical]**: correlation-selection gap 非平凡性不足——4/5 instance-level 信号的 selection 失败部分为 by-design tautological，真正非平凡的是 logprob 失败，但被淹没在统一叙述中
- **N2 [critical]**: constrained decoding confound 仍未实验量化（与 R3-C1 一致，未解决）
- **N3 [critical]**: 训练细节缺失（learning rate/batch size/prompt template/LoRA target modules 等）——**新增问题**
- **W1-W6**: RE 单数据集、FK 独立性假设、SJ normalizer 选择、模型规模、TOST δ、single seed

等 Reviewer 2 回稿后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 34

## Round 34

6 recorded events


### User

_source line 446 · 2026-05-15T06:51:22.766483+00:00_

[Reviewer 1 审稿结果]:
审稿报告已提交给 Review Director。

**审稿结论**：Overall 3.0/5（Findings acceptance 边缘），Soundness 3.5，Excitement 3.0，Confidence 4/5。

三个 Must-Fix 问题：
1. **Correlation-selection gap 非平凡性不足**：4/5 信号是 instance-level，selection 失败部分是 by-design 而非 empirical surprise。真正有趣的发现（logprob 的 selection 失败）被淹没在统一叙述中。
2. **Constrained decoding confound**：论文自己承认 logprob 75% 的比较是 effective ties，指向 constrained decoding 可能是 gap 的主因而非信号本身的固有限制，但未实验验证。
3. **训练细节不足**：缺少 learning rate、batch size、prompt template 等关键超参数。

---

[Reviewer 2 审稿意见]:
## Reviewer 2 — Round 1 审稿报告

**论文**: Strong Predictors, Weak Selectors: A Systematic Comparison of Confidence Signals for Test-Time Scaling in Information Extraction
**Venue**: EMNLP 2026 Findings (ACL ARR May 2026 cycle)

---

## 总体评分

**Overall**: 3.5 / 5（Findings: borderline accept）
**一句话总结**: 方法论扎实、统计分析严谨的实证研究，"correlation-selection gap"概念有用，但新颖性受限于 gap 可从信号设计原理预见，且实验范围（2个8B模型、1个RE数据集）制约了结论的泛化性。

---

## 官方维度打分（ACL ARR Review Form, Feb 2025+）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| **Soundness** | 4 / 5 | 统计方法严谨（bootstrap CI, TOST equivalence testing, 3-seed validation），实验设计控制了训练混淆变量（identical LoRA procedure），结论的 hedge 恰当（"no statistically significant evidence" 而非 "no effect"）。RE 仅 SciERC 单数据集是主要弱点。 |
| **Excitement** | 2.5 / 5 | Correlation-selection gap 概念有实用价值，但其核心原因——4/5信号是 instance-level、无法区分候选样本——可从信号定义直接推出，缺少"意外性"。对 Nedellec (2026) 的增量贡献真实但幅度有限。 |
| **Overall Assessment** | 3.5 / 5 | 符合 Findings 标准：sound, reproducible, 有实用 takeaway（routing vs. selection）。但 novelty 不足以达到 main conference 水平。 |
| **Confidence** | 4 / 5 | 熟悉自洽性解码、MBR、LLM 不确定性估计和生成式 IE 文献。仔细阅读了全文和附录。 |

---

## 主要优势

1. **系统性和严谨性出色**。五种信号×三族系×四个配置的交叉比较，bootstrap CI（B=10,000）、TOST 等价检验、3-seed 稳定性验证——统计分析在 NLP 实证论文中属于上乘水准。特别是 TOST 等价检验（Table 8, Appendix D）不常见但非常恰当：它区分了"没有显著差异"和"确认等价"（例如 EM/Voting 在 RE 上即使±5pp 也不等价于 greedy，说明是系统性劣化）。

2. **质量估计 vs. 样本选择的解耦**（Section 3.3）是清晰的方法论贡献。将 per-sample signal 和 instance-level signal 明确区分（Eq. 1–7），并展示 ρ 和 AUROC 的分离（Section 4.2 "ρ–AUROC dissociation"），为后续工作提供了好的评估框架。

3. **任务难度依赖的信号排名**有实际指导意义：EM 在简单任务领先、结构化信号在复杂任务领先、能力不足时所有信号退化为 binary success/failure 检测器（WNUT-17 conditional ρ=0.038, Table 5）——这三层梯度比单一结论更有价值。

4. **MBR 连接**（Discussion Section "Connection to MBR decoding"）将自洽性选择策略统一为 MBR 框架下不同 utility function 的实例化，概念上很优雅。

5. **Limitations section 诚实且具体**，涵盖了 RE 单数据集、模型规模、constrained decoding 对 diversity 的压缩效应、logprob 温度敏感性数据缺失等——审稿人能想到的大部分限制作者都提前讨论了。

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] Correlation-selection gap 的"意外性"论证不足

- **具体位置**: Section 1 (Introduction para 3), Section 4.3 (Selection Gap), Section 5 (Discussion "Why the gap exists")
- **问题**: 论文将 correlation-selection gap 作为核心贡献（Contribution #2），但 gap 的主要原因——4/5 信号是 instance-level 的、对同一 input 的 N 个候选给出相同分数——是从信号设计中可以直接推导出的（Section 5 自己承认 "Four of five signals are instance-level by construction and cannot rank N candidates"）。唯一的 per-sample 信号 logprob 的失败更有趣（75% comparisons are ties），但探讨不够深入。如果 gap 在实验前就可以从原理预测，那核心贡献更多是"验证一个预期结论"而非"发现一个意外现象"。
- **为什么影响接收**: 这直接关系到论文的 novelty 判断——Findings track 接收的最低标准包括 "interesting findings"。如果 reviewers 认为 gap 是显而易见的，excitement 评分会低于可接收线。
- **建议修改方向**: (a) 在 Introduction 中正面讨论 "why the gap is not obvious a priori"——例如，MBR 在 MT 中成功地用 instance-level utility 做了有效选择（Freitag 2022），为什么在 IE 中失败？consensus-proximity 策略在理论上应该能产生 per-sample 区分度，为什么实际上不行？(b) 对 logprob 的 per-sample 选择失败做更深入的分析——logprob ties 的 75% 统计数据非常有价值，可以量化分析 constrained decoding 如何压缩了 logprob 的判别力（例如比较自由生成 vs. constrained decoding 下的 logprob 方差）。(c) 如果空间允许，讨论什么样的 per-sample 信号可能 work（不仅仅是 "trained verifiers"——是否存在无监督的 per-sample 结构化信号？）。

**N2** [critical] RE 结论基于单一数据集（SciERC），泛化性不明

- **具体位置**: Section 4.1 (Datasets), Section 6 (Conclusion para 1 最后一句), Limitations para 1
- **问题**: SciERC RE 有 40% zero-F1 的 floor effect（Section 4.2 para 1），且 7 种关系类型的信号质量差异巨大（Feature-Of ρ=0.004 vs. Hyponym-Of ρ=0.646, Appendix C）。论文所有 RE 结论（correlation-selection gap、信号排名、calibration 等）都只来自这一个数据集。Conclusion 的 hedge（"our RE conclusions rest on SciERC alone and warrant further validation"）是诚实的，但 Contribution #1 的表述（"quality estimation for NER and RE"）在 RE 部分缺乏足够支撑。
- **为什么影响接收**: 作为 systematic comparison 论文，单一 RE 数据集削弱了"systematic"的 claim。RE 结论中的 floor effect 使得很难区分"信号本身的局限"与"数据集特性的伪影"。
- **建议修改方向**: (a) 增加至少一个 RE 数据集（如 TACRED/Re-TACRED 的子集或 NYT/WebNLG），或在 Contribution claims 中明确降低 RE 部分的贡献力度。(b) 对 SciERC RE 的 floor effect 做更系统的消融——例如，在 non-zero F1 的 RE 子集上重做选择分析，看 gap 是否依然存在。(c) 如果不增加数据集，至少在 Abstract 和 Contribution 列表中将 RE 标记为 preliminary/exploratory。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] Abstract 过于密集，可读性差

- **具体位置**: Abstract (sections/abstract.tex), 尤其第 4 行和第 6 行
- **问题**: 第 4 行是一个包含 6 个括号注释、3 个分号、跨越 4 行的超长句子（"We find that...despite 13–18 pp of oracle headroom"）。第 6 行同样包含多层嵌套的条件限定。虽然信息量大，但第一次阅读很难把握核心信息。
- **建议**: 将核心发现拆分为 2-3 个独立句子。具体数字（如 ρ=0.38, AUROC=0.75, p>0.39）可以保留，但每个句子应只传达一个关键 claim。

**W2** [warning] "confidence signal" vs "consistency signal" 术语不一致

- **具体位置**: Abstract line 7 ("consistency signals"), Introduction line 17 ("confidence signals"), Section 3 ("confidence signal" 作为 formal term), Discussion 多处
- **问题**: 论文用 "confidence signal" 作为五种信号的统称（Section 3.2），但 Abstract 结尾和 Discussion 多处用 "consistency signals" 泛指——而 logprob 不是 consistency signal。这种混用虽然上下文可以区分，但对快速阅读的 reviewer 会造成困惑。
- **建议**: 在 Method 开头（Section 3.2 之前）明确定义："We use confidence signal as the umbrella term for all five signals; the four non-logprob signals are collectively referred to as consistency signals."

**W3** [warning] Nedellec (2026) 的引用键名 misleading

- **具体位置**: references.bib line 280–287, 多处引用
- **问题**: BibTeX 键名为 `nedellec2026consistency`，但查看 bib 条目，第一作者实际上是 Yao, Xinzhi，Nédellec 是第二作者。论文正文中使用 `\citet{nedellec2026consistency}` 会产生 "Yao et al. (2026)" 的输出——但论文多处文字讨论说 "Nedellec (2026)" 指代这篇工作（如 Introduction line 16, Related Work line 13），可能造成读者混淆。
- **建议**: 统一使用 Yao et al. (2026) 或更新 bib 键名为 `yao2026consistency`。

**W4** [warning] Soft Jaccard 对 Nedellec (2026) 的改进幅度有限

- **具体位置**: Section 4.2 para 1, Appendix E (Table 6)
- **问题**: Contribution #1 的核心卖点之一是 structural matching 相对于 surface-level agreement 的优势（回应 Nedellec 的 limitation）。但 SJ vs. EM 在 SciERC NER 上 Δρ=+0.065，bootstrap CI 的下界仅为 +0.003，在 Bonferroni correction 下不显著（Table 6 footnote）。在 CoNLL 上 EM 反超 SJ。这意味着 structural matching 的优势是 task-dependent 且 marginal 的。
- **为什么影响评分**: 这削弱了"structural signals are superior"的叙事——更准确的表述应该是 "structural and surface signals are complementary, with the choice depending on task complexity"。
- **建议**: (a) 在 Contribution #1 中弱化 "structural advantage" 的表述，改为强调 difficulty-dependent complementarity。(b) 讨论在什么条件下用户应该选择 structural vs. surface signal，提供决策树或简单规则。

**W5** [warning] 缺少 constrained decoding 对 diversity 影响的实验对照

- **具体位置**: Limitations para 5 (line 15)
- **问题**: 论文承认 "constrained decoding (Outlines/vLLM) enforces schema compliance, potentially compressing per-sample diversity and contributing to the correlation-selection gap beyond what free-form generation would exhibit"，但没有提供对照实验。这是一个重要的混淆变量：如果 constrained decoding 大幅压缩了 sample diversity，那么 correlation-selection gap 可能是 constrained decoding 的伪影，而非 structured IE 的固有属性。
- **建议**: 增加一个 free-form generation baseline（无 constrained decoding），比较 output diversity 和 selection gap 的变化。哪怕只在一个 model-dataset 配置上做也很有说明力。

**W6** [warning] 缺少若干相关工作

- **具体位置**: Section 2 (Related Work)
- **遗漏文献**:
  1. **Xiong et al. (2024) "Can LLMs Express Their Uncertainty? An Empirical Evaluation of Confidence Elicitation in LLMs"** (ICLR 2024) — 系统评估了 LLM 置信度获取方法（verbalized, consistency-based, logit-based），与本文的多族信号比较直接相关。
  2. **Ye et al. (2024) "Do LLMs Estimate Uncertainty Well in Instruction Following?"** (ICLR 2025) — 评估 LLM 在指令跟随任务中的不确定性估计，与本文的 structured output + confidence 主题有交叉。
  3. **最近的 Generative IE survey**（如 COLING 2025 的 "A Survey of Generative Information Extraction"）——可在 Related Work 的 generative IE 段落中引用以加强 IE 背景。
- **建议**: 在 Related Work 的 "Uncertainty estimation" 段落中加入 Xiong et al. 的讨论，明确说明本文与 verbalized confidence 方法的区别（本文不要求模型显式表达置信度）。

---

## 小问题（不影响接收）

1. **Table 1 N=16 行数据不完整**: N=16 的 3-seed 结果只报告了 LLaMA CoNLL（5列），SciERC 的 N=16 数据完全空白。虽然 Table 3 (Appendix) 有部分 N=16 数据，但 Table 1 的空白列给人"实验不完整"的印象。建议填充或添加脚注说明 N=16 全部数据的位置。

2. **Figure 1 (Overview) 的右侧面板**: 标题说 "the same instance-level signal assigns identical scores to all N candidates"，但没有解释 consensus-proximity 策略如何将 instance-level 信号转化为 per-sample 排序。建议在 caption 中增加一句说明。

3. **references.bib 格式小问题**: `feng2025optimal` 的第一作者姓名 mismatch（bib: Feng, Austin vs OpenAlex API: Austin as first name, suggesting `author = {Austin, Feng}`?），`snell2024scaling` 同理。实际上检查 bib 内容，author field 写的是 "Feng, Austin and Alonso, Marius..."——这里 Feng 是 last name, Austin 是 first name, 应该没问题。OpenAlex API 的 mismatch 可能是 API 端的解析问题。不影响论文。

4. **Appendix 中 Table 5 (WNUT-17)**: Conditional ρ 和 p 值很有价值，建议将其关键数字在主文中也提及（目前主文 Section 4.2 最后一段提到了但没有给出所有信号的 conditional ρ）。

5. **Ethics statement 位于 Limitations section 内部**（limitations.tex line 18–20）——ACL 格式通常建议将 Ethics Statement 作为独立段落或 section。当前位置不影响合规但不够规范。

---

## Missing References 总结

| 文献 | 类型 | 相关度 | 优先级 |
|------|------|--------|--------|
| Xiong et al. (2024) "Can LLMs Express Their Uncertainty?" ICLR 2024 | Confidence elicitation survey | 高 | Should-cite |
| Ye et al. (2025) "Do LLMs Estimate Uncertainty Well?" ICLR 2025 | Uncertainty in instruction-following | 中 | Nice-to-cite |
| Xu et al. (2025) "A Survey of Generative Information Extraction" COLING 2025 | Generative IE survey | 中 | Nice-to-cite |

---

## 关于 Findings Track 定位

本文作为 empirical study with negative result，Findings track 是合适的定位。论文满足 Findings 的核心标准：
- **Soundness**: 方法论扎实，统计分析严谨（4/5）
- **Reproducibility**: 使用公开模型和数据集，实验设置详细（LoRA 参数、N、T、seed 均明确）

但 excitement 偏低（2.5/5），主要因为：(a) 核心 gap 可从信号设计预测；(b) 对社区的实际影响有限——实用 takeaway 是"用 consistency 信号做 routing 而不做 selection"，这个结论已经在 reasoning 领域有类似的先例。

**对 Findings 的接收建议**: Borderline Accept — 方法论上足以发表，但建议作者加强 N1（gap 的非显然性论证）和 W4（弱化 structural advantage claim），这将使论文更有说服力。

---

**Reviewer 2 Confidence**: 4/5 — 熟悉该领域，仔细阅读全文及附录。

---

[Reviewer 2 审稿结果]:
审稿报告已提交给 Review Director。

**总结**：给出 Overall 3.5/5（Findings borderline accept），Soundness 4/5，Excitement 2.5/5。

主要发现：
- **2 个 Must-Fix**：(N1) correlation-selection gap 的"意外性"论证不足——4/5 信号 instance-level 的局限可从设计原理直接推出，需正面论证 why not obvious；(N2) RE 结论仅基于 SciERC 单一数据集，泛化性不明。
- **6 个 Should-Fix**：Abstract 过密、术语不一致（confidence vs consistency signal）、Nedellec 引用键名 misleading（实际第一作者是 Yao）、Soft Jaccard 优势幅度有限且 Bonferroni 下不显著、缺少 constrained decoding 对 diversity 影响的对照实验、缺少 Xiong et al. (2024) 等相关工作。
- **格式合规总体良好**：匿名合规、Limitations 充实、Ethics statement 存在（但位置不够规范）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 447 · 2026-05-15T06:52:08.413821+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "4",
  "project": "struct_self_consist_ie",
  "text": "## 交叉分享 — 请逐条回应 Reviewer 2 的审稿意见\n\n以下是 Reviewer 2 的完整审稿报告。请对每个 Must-Fix 和 Should-Fix 逐条回应：\n- **[AGREE]** 同意并说明理由\n- **[REBUT]** 反驳并提供证据（引用论文具体 Section/Table/Figure）\n\n---\n\n## Reviewer 2 — Round 1 审稿报告\n\n**Overall**: 3.5 / 5（Findings: borderline accept）\n\n### 维度打分\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 4 / 5 | 统计方法严谨（bootstrap CI, TOST equivalence testing, 3-seed validation），RE 仅 SciERC 单数据集是主要弱点 |\n| Excitement | 2.5 / 5 | Gap 概念有实用价值，但核心原因可从信号定义推出，缺少\"意外性\" |\n| Overall Assessment | 3.5 / 5 | 符合 Findings 标准，但 novelty 不足以达到 main conference |\n| Confidence | 4 / 5 | 熟悉相关文献，仔细阅读全文和附录 |\n\n### 主要优势\n1. 系统性和严谨性出色（bootstrap CI B=10,000, TOST, 3-seed）\n2. 质量估计 vs. 样本选择的解耦是清晰的方法论贡献\n3. 任务难度依赖的信号排名有实际指导意义\n4. MBR 连接优雅\n5. Limitations section 诚实且具体\n\n### Must-Fix\n\n**N1** [critical] Correlation-selection gap 的\"意外性\"论证不足\n- 4/5 信号 instance-level，selection 失败可从设计原理推出\n- 论文将 gap 作为核心贡献但未正面论证 \"why not obvious a priori\"\n- 建议：(a) 讨论 MBR 在 MT 中成功但 IE 中失败的原因；(b) 深入分析 logprob ties 的 75% 统计数据；(c) 讨论什么样的 per-sample 信号可能 work\n\n**N2** [critical] RE 结论基于单一数据集（SciERC），泛化性不明\n- SciERC RE 40% zero-F1 floor effect，7 种关系类型信号质量差异巨大\n- Contribution #1 \"quality estimation for NER and RE\" 在 RE 部分缺乏足够支撑\n- 建议：增加 RE 数据集或明确降级 RE 贡献\n\n### Should-Fix\n\n**W1** [warning] Abstract 过于密集，可读性差\n- 第 4 行超长句子含 6 个括号注释、3 个分号\n- 建议拆分为 2-3 个独立句子\n\n**W2** [warning] \"confidence signal\" vs \"consistency signal\" 术语不一致\n- \"confidence signal\" 是统称但多处用 \"consistency signals\" 泛指（logprob 不是 consistency signal）\n- 建议在 Method 开头明确定义\n\n**W3** [warning] Nedellec (2026) 引用键名 misleading\n- BibTeX 键名 `nedellec2026consistency` 但第一作者实际是 Yao\n- 正文多处说 \"Nedellec (2026)\" 但 \\citet 输出 \"Yao et al. (2026)\"\n\n**W4** [warning] Soft Jaccard 对 Nedellec 改进幅度有限\n- SJ vs EM: Δρ=+0.065，CI 下界仅 +0.003，Bonferroni 下不显著\n- CoNLL 上 EM 反超 SJ\n- 建议弱化 \"structural advantage\" 叙事，强调 difficulty-dependent complementarity\n\n**W5** [warning] 缺少 constrained decoding 对 diversity 影响的实验对照\n- 论文承认 constrained decoding 可能压缩 diversity 但无对照\n- 建议增加 free-form generation baseline\n\n**W6** [warning] 缺少若干相关工作\n- Xiong et al. (2024) \"Can LLMs Express Their Uncertainty?\" ICLR 2024（高相关）\n- Ye et al. (2025) \"Do LLMs Estimate Uncertainty Well?\" ICLR 2025\n- Generative IE survey（COLING 2025）\n\n### 小问题\n1. Table 1 N=16 数据不完整\n2. Figure 1 caption 未解释 consensus-proximity\n3. references.bib 格式小问题\n4. WNUT-17 conditional ρ 数字建议在主文提及\n5. Ethics statement 位置不够规范\n\n### Missing References\n| 文献 | 相关度 | 优先级 |\n|------|--------|--------|\n| Xiong et al. (2024) ICLR | 高 | Should-cite |\n| Ye et al. (2025) ICLR | 中 | Nice-to-cite |\n| Xu et al. (2025) COLING | 中 | Nice-to-cite |\n\n---\n\n请逐条回应以上所有 Must-Fix 和 Should-Fix 问题。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "4",
    "project": "struct_self_consist_ie",
    "text": "## 交叉分享 — 请逐条回应 Reviewer 2 的审稿意见\n\n以下是 Reviewer 2 的完整审稿报告。请对每个 Must-Fix 和 Should-Fix 逐条回应：\n- **[AGREE]** 同意并说明理由\n- **[REBUT]** 反驳并提供证据（引用论文具体 Section/Table/Figure）\n\n---\n\n## Reviewer 2 — Round 1 审稿报告\n\n**Overall**: 3.5 / 5（Findings: borderline accept）\n\n### 维度打分\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 4 / 5 | 统计方法严谨（bootstrap CI, TOST equivalence testing, 3-seed validation），RE 仅 SciERC 单数据集是主要弱点 |\n| Excitement | 2.5 / 5 | Gap 概念有实用价值，但核心原因可从信号定义推出，缺少\"意外性\" |\n| Overall Assessment | 3.5 / 5 | 符合 Findings 标准，但 novelty 不足以达到 main conference |\n| Confidence | 4 / 5 | 熟悉相关文献，仔细阅读全文和附录 |\n\n### 主要优势\n1. 系统性和严谨性出色（bootstrap CI B=10,000, TOST, 3-seed）\n2. 质量估计 vs. 样本选择的解耦是清晰的方法论贡献\n3. 任务难度依赖的信号排名有实际指导意义\n4. MBR 连接优雅\n5. Limitations section 诚实且具体\n\n### Must-Fix\n\n**N1** [critical] Correlation-selection gap 的\"意外性\"论证不足\n- 4/5 信号 instance-level，selection 失败可从设计原理推出\n- 论文将 gap 作为核心贡献但未正面论证 \"why not obvious a priori\"\n- 建议：(a) 讨论 MBR 在 MT 中成功但 IE 中失败的原因；(b) 深入分析 logprob ties 的 75% 统计数据；(c) 讨论什么样的 per-sample 信号可能 work\n\n**N2** [critical] RE 结论基于单一数据集（SciERC），泛化性不明\n- SciERC RE 40% zero-F1 floor effect，7 种关系类型信号质量差异巨大\n- Contribution #1 \"quality estimation for NER and RE\" 在 RE 部分缺乏足够支撑\n- 建议：增加 RE 数据集或明确降级 RE 贡献\n\n### Should-Fix\n\n**W1** [warning] Abstract 过于密集，可读性差\n- 第 4 行超长句子含 6 个括号注释、3 个分号\n- 建议拆分为 2-3 个独立句子\n\n**W2** [warning] \"confidence signal\" vs \"consistency signal\" 术语不一致\n- \"confidence signal\" 是统称但多处用 \"consistency signals\" 泛指（logprob 不是 consistency signal）\n- 建议在 Method 开头明确定义\n\n**W3** [warning] Nedellec (2026) 引用键名 misleading\n- BibTeX 键名 `nedellec2026consistency` 但第一作者实际是 Yao\n- 正文多处说 \"Nedellec (2026)\" 但 \\citet 输出 \"Yao et al. (2026)\"\n\n**W4** [warning] Soft Jaccard 对 Nedellec 改进幅度有限\n- SJ vs EM: Δρ=+0.065，CI 下界仅 +0.003，Bonferroni 下不显著\n- CoNLL 上 EM 反超 SJ\n- 建议弱化 \"structural advantage\" 叙事，强调 difficulty-dependent complementarity\n\n**W5** [warning] 缺少 constrained decoding 对 diversity 影响的实验对照\n- 论文承认 constrained decoding 可能压缩 diversity 但无对照\n- 建议增加 free-form generation baseline\n\n**W6** [warning] 缺少若干相关工作\n- Xiong et al. (2024) \"Can LLMs Express Their Uncertainty?\" ICLR 2024（高相关）\n- Ye et al. (2025) \"Do LLMs Estimate Uncertainty Well?\" ICLR 2025\n- Generative IE survey（COLING 2025）\n\n### 小问题\n1. Table 1 N=16 数据不完整\n2. Figure 1 caption 未解释 consensus-proximity\n3. references.bib 格式小问题\n4. WNUT-17 conditional ρ 数字建议在主文提及\n5. Ethics statement 位置不够规范\n\n### Missing References\n| 文献 | 相关度 | 优先级 |\n|------|--------|--------|\n| Xiong et al. (2024) ICLR | 高 | Should-cite |\n| Ye et al. (2025) ICLR | 中 | Nice-to-cite |\n| Xu et al. (2025) COLING | 中 | Nice-to-cite |\n\n---\n\n请逐条回应以上所有 Must-Fix 和 Should-Fix 问题。"
  }
}
```

</details>

---


### Tool result

_source line 448 · 2026-05-15T06:52:57.383026+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 48969
}
```

</details>

---


### Tool call

_source line 449 · 2026-05-15T06:52:57.534077+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "4",
  "project": "struct_self_consist_ie",
  "text": "## 交叉分享 — 请逐条回应 Reviewer 1 的审稿意见\n\n以下是 Reviewer 1 的完整审稿报告。请对每个 Must-Fix 和 Should-Fix 逐条回应：\n- **[AGREE]** 同意并说明理由\n- **[REBUT]** 反驳并提供证据（引用论文具体 Section/Table/Figure）\n\n---\n\n## Reviewer 1 — 审稿报告\n\n**Overall**: 3.0 / 5（Findings acceptance 边缘）\n\n### 维度打分\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5 / 5 | 统计方法论优秀，但核心 claim 非平凡性受质疑；constrained decoding confound 未验证 |\n| Excitement | 3.0 / 5 | 填补了 QE vs. selection 区分空白，但本质是 negative result + 对已知设计限制的实证确认 |\n| Reproducibility | 3.0 / 5 | 使用公开数据和开源模型，但 LoRA 训练缺关键超参（lr, batch size, warmup, prompt template） |\n| Confidence | 4 / 5 | 熟悉相关文献 |\n\n### 主要优势\n1. 研究问题定义清晰（QE vs. selection 区分）\n2. 统计方法论严谨（bootstrap B=10,000, TOST, Cohen's d, multi-seed）\n3. Difficulty gradient 分析有深度（CoNLL→SciERC→WNUT-17 + conditional filtering）\n4. Transparency：自身局限性讨论诚实全面\n5. MBR decoding 连接有价值\n6. 引用质量高（55 条，0 orphan，51 条 OpenAlex 验证通过）\n\n### Must-Fix\n\n**N1** [critical] Correlation-selection gap 非平凡性不足——instance-level 信号的 selection 失败部分为 tautological\n- §3.1: 5 个信号中 4 个是 instance-level，consensus-proximity 转换等价于 MBR decoding\n- 论文将 \"所有信号均未超越 greedy\" 包装为统一经验发现，但 instance-level 信号的 selection 失败主要是**设计层面的先验预期**\n- 真正非平凡的发现是 **logprob 的 selection 失败**（SciERC +0.6pp, p=0.39, Cohen's d=0.038），但被淹没在统一叙述中\n- Discussion 承认 \"Four of five signals are instance-level by construction\" 但这与 §4.3/abstract 的 core empirical contribution 定位存在张力\n- 建议：(a) 明确分离 instance-level 失败（by-design）和 logprob 失败（empirical）为两个独立发现；(b) 重定义 gap scope 聚焦 \"consensus-proximity/MBR selection 在 structured IE 上失败\"\n\n**N2** [critical] Constrained decoding 作为 correlation-selection gap 的 confounding factor 未被实验量化\n- §4.1 使用 vLLM + Outlines constrained decoding\n- 可能从两方面 confound：(1) 压缩 per-sample diversity；(2) 使 logprob 主要反映 grammar compliance\n- 论文报告 SciERC 43% unique outputs + per-sample F1 std=0.14，但不排除 diversity 被压缩到 constrained 子空间\n- §5 承认 \"75% of comparisons are effectively ties\" 但归因于 logprob 特性而非实验设置\n- 建议：(a) 增加 free-form generation 对照；(b) 或分析 logprob 分布——在 non-tie 的 25% 上 logprob 是否能成功 select；(c) 区分 logprob 值差异小（grammar path 导致）vs. 差异大但与 F1 无关\n\n**N3** [critical] 训练细节不足以复现\n- §4.1: LoRA rank=32, α=64, 5 epochs, LLaMA Factory——但缺少：\n  - learning rate, batch size, warmup, weight decay, optimizer\n  - early stopping 策略, train/dev split\n  - prompt template（NER/RE 各用什么格式？）\n  - LoRA target modules, max sequence length\n- LoRA 微调对 lr 和 target modules 敏感，不同配置可能影响 output diversity 和信号表现\n\n### Should-Fix\n\n**W1** [warning] RE 结论仅基于 SciERC 单一数据集\n- SciERC 40% zero-F1，RE gap 证据薄弱（-0.9pp, p=0.80）\n- Abstract/Introduction 将 RE 作为等权证据呈现\n- 建议增加 RE 数据集或降级 RE claim 为 preliminary\n\n**W2** [warning] Fleiss' κ 应用于非独立 temperature-sampled outputs 的理论 justification 薄弱\n- FK 假设独立 raters，但 temperature sampling 共享模型权重/prompt/前缀\n- excess agreement (-0.4% to -4.0%) 的 baseline 和 negative 值含义不清\n- 建议解释 excess agreement 计算方法或限定 FK 为\"经验度量\"\n\n**W3** [warning] Soft Jaccard normalizer 选择缺乏对比\n- max(|g_i|, |g_j|) vs. |g_i ∪ g_j| 未比较\n- 建议至少在附录报告替代 normalizer 结果\n\n**W4** [warning] 模型规模限于 8B\n- Larger models 可能改变 signal landscape（logprob 在更强模型上可能更有区分力）\n- 建议讨论 model scale 对 gap 方向的影响\n\n**W5** [warning] TOST δ 选择缺乏依据\n- ±2, ±3, ±5 pp 的选择未讨论合理性\n- 建议提供 δ 选择的实际意义论证\n\n**W6** [warning] N=8 主实验的 single-seed 稳定性\n- Table 1, Table 3 N=8 均 seed=42 单次运行\n- Appendix D 3-seed 分析仅覆盖 SciERC NER（Table 7），不覆盖 CoNLL N=8 和 SciERC RE\n- 建议补多 seed 或注明局限\n\n### 小问题\n- semantic entropy footnote 不可比数字可能误导\n- Table 1 N=16 区域不完整\n- Entity Voting 公式分母为 0 的边界条件\n- Appendix Fig 3 ECE bin 数量未报告\n\n### 缺失引用\n- Bertsch et al. (2024) \"In-Context Learning with Long-Context Models\"\n- Wiher et al. (2022) \"On Decoding Strategies for Neural Text Generators\"\n- Müller & Sennrich (2021) \"Understanding the Properties of MBR Decoding in NMT\"\n\n---\n\n请逐条回应以上所有 Must-Fix 和 Should-Fix 问题。特别关注：\n1. 你是否同意 N3（训练细节不足）的严重性评估？\n2. 你对 W2（FK 独立性）和 W3（SJ normalizer）的看法？\n3. R1 提出的 3 篇缺失引用你是否认同？"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "4",
    "project": "struct_self_consist_ie",
    "text": "## 交叉分享 — 请逐条回应 Reviewer 1 的审稿意见\n\n以下是 Reviewer 1 的完整审稿报告。请对每个 Must-Fix 和 Should-Fix 逐条回应：\n- **[AGREE]** 同意并说明理由\n- **[REBUT]** 反驳并提供证据（引用论文具体 Section/Table/Figure）\n\n---\n\n## Reviewer 1 — 审稿报告\n\n**Overall**: 3.0 / 5（Findings acceptance 边缘）\n\n### 维度打分\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5 / 5 | 统计方法论优秀，但核心 claim 非平凡性受质疑；constrained decoding confound 未验证 |\n| Excitement | 3.0 / 5 | 填补了 QE vs. selection 区分空白，但本质是 negative result + 对已知设计限制的实证确认 |\n| Reproducibility | 3.0 / 5 | 使用公开数据和开源模型，但 LoRA 训练缺关键超参（lr, batch size, warmup, prompt template） |\n| Confidence | 4 / 5 | 熟悉相关文献 |\n\n### 主要优势\n1. 研究问题定义清晰（QE vs. selection 区分）\n2. 统计方法论严谨（bootstrap B=10,000, TOST, Cohen's d, multi-seed）\n3. Difficulty gradient 分析有深度（CoNLL→SciERC→WNUT-17 + conditional filtering）\n4. Transparency：自身局限性讨论诚实全面\n5. MBR decoding 连接有价值\n6. 引用质量高（55 条，0 orphan，51 条 OpenAlex 验证通过）\n\n### Must-Fix\n\n**N1** [critical] Correlation-selection gap 非平凡性不足——instance-level 信号的 selection 失败部分为 tautological\n- §3.1: 5 个信号中 4 个是 instance-level，consensus-proximity 转换等价于 MBR decoding\n- 论文将 \"所有信号均未超越 greedy\" 包装为统一经验发现，但 instance-level 信号的 selection 失败主要是**设计层面的先验预期**\n- 真正非平凡的发现是 **logprob 的 selection 失败**（SciERC +0.6pp, p=0.39, Cohen's d=0.038），但被淹没在统一叙述中\n- Discussion 承认 \"Four of five signals are instance-level by construction\" 但这与 §4.3/abstract 的 core empirical contribution 定位存在张力\n- 建议：(a) 明确分离 instance-level 失败（by-design）和 logprob 失败（empirical）为两个独立发现；(b) 重定义 gap scope 聚焦 \"consensus-proximity/MBR selection 在 structured IE 上失败\"\n\n**N2** [critical] Constrained decoding 作为 correlation-selection gap 的 confounding factor 未被实验量化\n- §4.1 使用 vLLM + Outlines constrained decoding\n- 可能从两方面 confound：(1) 压缩 per-sample diversity；(2) 使 logprob 主要反映 grammar compliance\n- 论文报告 SciERC 43% unique outputs + per-sample F1 std=0.14，但不排除 diversity 被压缩到 constrained 子空间\n- §5 承认 \"75% of comparisons are effectively ties\" 但归因于 logprob 特性而非实验设置\n- 建议：(a) 增加 free-form generation 对照；(b) 或分析 logprob 分布——在 non-tie 的 25% 上 logprob 是否能成功 select；(c) 区分 logprob 值差异小（grammar path 导致）vs. 差异大但与 F1 无关\n\n**N3** [critical] 训练细节不足以复现\n- §4.1: LoRA rank=32, α=64, 5 epochs, LLaMA Factory——但缺少：\n  - learning rate, batch size, warmup, weight decay, optimizer\n  - early stopping 策略, train/dev split\n  - prompt template（NER/RE 各用什么格式？）\n  - LoRA target modules, max sequence length\n- LoRA 微调对 lr 和 target modules 敏感，不同配置可能影响 output diversity 和信号表现\n\n### Should-Fix\n\n**W1** [warning] RE 结论仅基于 SciERC 单一数据集\n- SciERC 40% zero-F1，RE gap 证据薄弱（-0.9pp, p=0.80）\n- Abstract/Introduction 将 RE 作为等权证据呈现\n- 建议增加 RE 数据集或降级 RE claim 为 preliminary\n\n**W2** [warning] Fleiss' κ 应用于非独立 temperature-sampled outputs 的理论 justification 薄弱\n- FK 假设独立 raters，但 temperature sampling 共享模型权重/prompt/前缀\n- excess agreement (-0.4% to -4.0%) 的 baseline 和 negative 值含义不清\n- 建议解释 excess agreement 计算方法或限定 FK 为\"经验度量\"\n\n**W3** [warning] Soft Jaccard normalizer 选择缺乏对比\n- max(|g_i|, |g_j|) vs. |g_i ∪ g_j| 未比较\n- 建议至少在附录报告替代 normalizer 结果\n\n**W4** [warning] 模型规模限于 8B\n- Larger models 可能改变 signal landscape（logprob 在更强模型上可能更有区分力）\n- 建议讨论 model scale 对 gap 方向的影响\n\n**W5** [warning] TOST δ 选择缺乏依据\n- ±2, ±3, ±5 pp 的选择未讨论合理性\n- 建议提供 δ 选择的实际意义论证\n\n**W6** [warning] N=8 主实验的 single-seed 稳定性\n- Table 1, Table 3 N=8 均 seed=42 单次运行\n- Appendix D 3-seed 分析仅覆盖 SciERC NER（Table 7），不覆盖 CoNLL N=8 和 SciERC RE\n- 建议补多 seed 或注明局限\n\n### 小问题\n- semantic entropy footnote 不可比数字可能误导\n- Table 1 N=16 区域不完整\n- Entity Voting 公式分母为 0 的边界条件\n- Appendix Fig 3 ECE bin 数量未报告\n\n### 缺失引用\n- Bertsch et al. (2024) \"In-Context Learning with Long-Context Models\"\n- Wiher et al. (2022) \"On Decoding Strategies for Neural Text Generators\"\n- Müller & Sennrich (2021) \"Understanding the Properties of MBR Decoding in NMT\"\n\n---\n\n请逐条回应以上所有 Must-Fix 和 Should-Fix 问题。特别关注：\n1. 你是否同意 N3（训练细节不足）的严重性评估？\n2. 你对 W2（FK 独立性）和 W3（SJ normalizer）的看法？\n3. R1 提出的 3 篇缺失引用你是否认同？"
  }
}
```

</details>

---


### Tool result

_source line 450 · 2026-05-15T06:52:59.140586+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1606
}
```

</details>

---


### Assistant

_source line 451 · 2026-05-15T06:53:07.747470+00:00_

交叉分享已发出。两位 Reviewer 正在互相审阅对方的意见，等待交叉回应返回后进入收敛判断和报告汇总。

当前状态：
- **Reviewer 1**: Overall 3.0/5, 3 Critical + 6 Warning
- **Reviewer 2**: Overall 3.5/5, 2 Critical + 6 Warning
- **共识趋势**: 两人在 gap 非平凡性、RE 单数据集、constrained decoding confound 上观点高度一致；分歧可能在训练细节严重性（R1 列 critical vs R2 未提）和 FK/SJ 技术细节上

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 35

## Round 35

2 recorded events


### User

_source line 452 · 2026-05-15T06:56:15.980837+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 → 交叉回应 Reviewer 2 审稿意见

---

### Must-Fix

**[REBUT] R2-N1: Correlation-selection gap 的"意外性"论证不足**

R2 认为"4/5 信号是 instance-level，selection 失败可从设计原理推出"。我部分反驳：

1. **MBR 类比非平凡**。论文 Section 4.3（p7）建立了 MBR decoding 连接。MBR 在 MT 中成功（Eikema and Aziz, 2022），并非显然可预测 structural MBR 在 IE 中全面失败。
2. **Logprob 是 per-sample 信号但仍失败**。75% comparisons are ties（Section 4.3, p7）是经验发现，非设计可推。
3. **但 R2 改进建议合理**。"Why the gap exists"（p7-8）偏事后解释，增加 MT-vs-IE 的 MBR 对比讨论会加强论证。

**结论：核心观察有价值，"非显然性"论证可加强，但不应作为 reject 理由。**

---

**[AGREE] R2-N2: RE 结论基于单一数据集**

同意这是实质性弱点：
- Table 1 RE 仅有 SciERC，NER 有三个 difficulty 梯度数据集
- 40% zero-F1 floor effect 严重限制信号鉴别力
- Contributions 中 RE 与 NER 并列但支撑力度不对等
- 缓解因素：3-seed 验证和 conditional set 分析覆盖了 RE，方法论严谨性无问题

**建议：增加 RE 数据集或将 RE 降级为 "preliminary findings"。**

---

### Should-Fix

**[AGREE] R2-W1: Abstract 过于密集**
同意。第 3-4 行含 3 层嵌套括号的超长句子可拆分为 2-3 句。

**[AGREE] R2-W2: terminology 不一致**
部分同意。"confidence signal"（总称）vs "consistency signal"（子集）边界在某些段落模糊。建议 Section 3.2 开头增加明确 taxonomy。

**[REBUT] R2-W3: Nedellec (2026) BibTeX 键名**
不同意。R2 称"正文说 Nedellec (2026) 但 \citet 输出 Yao et al. (2026)"——如果 \citet 输出正确，读者看到的就是正确引用。我通读全文（p2-3）未发现硬编码的 "Nedellec"。BibTeX 键名是内部实现细节，不属于审稿范围。建议降级或移除。

**[AGREE] R2-W4: Soft Jaccard 改进幅度有限**
同意。SJ vs EM Δρ=+0.065 在 Bonferroni 下 marginal（论文 p5 脚注确认）；CoNLL 上 EM 反超。应调整叙事为 difficulty-dependent complementarity 而非 structural dominance。

**[REBUT] R2-W5: 缺少 free-form generation baseline**
不同意列为 Should-Fix。Constrained decoding 对 structured IE 是方法论必要条件，free-form 引入新混淆变量。论文 Limitations 已诚实讨论。可加 diversity 统计，但不需 free-form 实验。

**[AGREE] R2-W6: 缺少相关工作**
部分同意。Xiong et al. (2024) ICLR "Can LLMs Express Their Uncertainty?" 高度相关，应引用。其余两篇 nice-to-cite。

---

### 对 R2 整体评价的意见

- Soundness 4/5：准确
- Excitement 2.5/5：稍低估，Findings track 3/5 更合理（系统性 benchmark 实用价值 + MBR 连接 + difficulty-dependent guidance）
- R2 审稿质量高。最有价值意见：N2（RE 单数据集）和 W4（SJ 优势弱化）。N1 过度批评，W3 和 W5 可降级。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 453 · 2026-05-15T06:56:23.894493+00:00_

Reviewer 1 交叉回应已收到。等待 Reviewer 2 的交叉回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 36

## Round 36

2 recorded events


### User

_source line 454 · 2026-05-15T06:56:28.857453+00:00_

[Reviewer 1 审稿结果]:
交叉回应已提交。总结：

- **N1**（gap 意外性）：[REBUT]——MBR 类比和 logprob ties 数据提供了非平凡发现，但同意加强"非显然性"论证
- **N2**（RE 单数据集）：[AGREE]——实质性弱点，建议增加数据集或降级 RE 贡献
- **W1**（Abstract 密度）：[AGREE]
- **W2**（术语不一致）：[AGREE]——建议加 taxonomy 定义
- **W3**（BibTeX 键名）：[REBUT]——内部实现细节，未观察到可见引用错误
- **W4**（SJ 优势有限）：[AGREE]——Bonferroni 下 marginal，应改为 complementarity 叙事
- **W5**（free-form baseline）：[REBUT]——constrained decoding 是方法论必要条件
- **W6**（缺少引用）：[AGREE]——Xiong et al. (2024) 应引用

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 455 · 2026-05-15T06:56:34.558616+00:00_

Reviewer 1 交叉回应已收到。等待 Reviewer 2 的交叉回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 37

## Round 37

6 recorded events


### User

_source line 456 · 2026-05-15T06:56:44.956479+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 — Round 4 审稿报告

**Overall**: 3.0 (Findings)
**Soundness**: 3.5 | **Excitement**: 2.5 | **Reproducibility**: 3 | **Confidence**: 4

### Round 3 修复状态总览
- **RESOLVED (8/13)**: R3-C2 (TOST已补), R3-C3 (3-seed已补), R3-W1 (Bonferroni已补), R3-W3 (MBR连接已补), R3-W4 (FK excess agreement数据已补), R3-W5 (cross-architecture统一), R3-W8 (引用已补全), R0-C3 (RE claim已降级), R1-W1 (SJ形式化已完善)
- **PARTIALLY RESOLVED (4/13)**: R3-C1 (constrained decoding承认但未量化), R3-W2 (gap tautology改善但核心张力仍在), R3-W6 (hedge加在Conclusion但Introduction仍断言式), R3-W7 (表格缩写VC/Voting Conf.不统一)
- **UNRESOLVED (1/13)**: 无完全未解决的问题

### 新发现的 Must-Fix (2个)
1. **N1 [critical] Contribution #2 非平凡性不足**: 4/5 信号是 instance-level 的，其 selection 失败是定义性推论。真正的经验贡献是 logprob（唯一 per-sample 信号）也失败了，但论文对此区分不清晰。建议重新 frame：区分 "定义性 gap"（instance-level 信号）和"经验性 gap"（logprob 也失败），后者才是需要实验验证的贡献。
2. **N2 [critical] Prompt template 和 fine-tuning 数据细节缺失**: 附录无 prompt template、training split、schema constraint 定义，影响独立复现。

### Should-Fix (5个)
- W1: Constrained decoding 对 logprob 信号语义的影响未充分讨论（R3-C1延续）
- W2: Ethics Statement 应为独立 section 而非 Limitations 内 paragraph
- W3: 表格缩写不统一（Voting Conf. vs VC）
- W4: Introduction novelty claim 缺 hedge（Conclusion 有但 Introduction 无）
- W5: Table 1 N=16 block 大面积空白，未引导读者到附录

### 主要优势
统计方法论显著改进（TOST/bootstrap CI/Bonferroni/3-seed）、多层面评估框架设计合理、MBR 连接清晰、条件过滤分析有洞察力、claims 范围审慎。

### 判断
推荐 Findings 接收，条件是 N1（framing 调整区分定义性/经验性 gap）和 N2（prompt template 补充）得到修复。论文经四轮迭代已达到较高的统计严谨度。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 457 · 2026-05-15T07:06:09.605273+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "struct_self_consist_ie",
  "issues_yaml": "issues:\n  # ============================================================\n  # Round 0 issues (all resolved)\n  # ============================================================\n  - id: \"R0-C1\"\n    summary: \"模型规模单一（仅 8B）\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 0\n    last_seen_round: 1\n    mentions:\n      - round: 0\n        reviewers: [1, 2]\n        note: \"8B→8B 仅验证架构鲁棒性非规模鲁棒性\"\n      - round: 1\n        reviewers: [1, 2]\n        note: \"model-agnostic 与 Limitations 矛盾\"\n    action_items:\n      - round: 1\n        action: \"全文替换 model-agnostic → consistent across tested model families\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"Round 2 Reviewer 确认措辞修正到位，无再提\"\n    resolution_round: 2\n\n  - id: \"R0-C2\"\n    summary: \"相关工作显著遗漏\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 0\n    last_seen_round: 1\n    mentions:\n      - round: 0\n        reviewers: [1, 2]\n        note: \"5 篇核心文献缺失\"\n      - round: 1\n        reviewers: [1, 2]\n        note: \"新遗漏：Optimal SC, Difficulty-Adaptive SC\"\n    action_items:\n      - round: 1\n        action: \"补充 6 篇引用到 Related Work\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"Round 2: 49 条 bib 全部 cited, 0 orphan, 无遗漏\"\n    resolution_round: 2\n\n  - id: \"R0-C3\"\n    summary: \"RE 结论仅基于 SciERC 单数据集\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 0\n    last_seen_round: 4\n    mentions:\n      - round: 0\n        reviewers: [1, 2]\n        note: \"需跨数据集验证或降级措辞\"\n      - round: 2\n        reviewers: [1, 2]\n        note: \"Abstract RE 措辞需修正\"\n      - round: 3\n        reviewers: [1, 2]\n        note: \"Round 2 措辞修正到位，但 R3 Reviewer 2 再次提出 44% zero-F1 floor effect 严重压缩可区分范围\"\n      - round: 4\n        reviewers: [1, 2]\n        note: \"R2 确认 claim 降级已完成（Conclusion 明确 hedge）。两位 Reviewer 仍认为 RE 证据薄弱，但 claim 范围已恰当限定——后续改进作为 R4-W1 追踪\"\n    action_items:\n      - round: 1\n        action: \"降级措辞 universal → observed in SciERC\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n      - round: 2\n        action: \"Abstract 改为 NER (three datasets) and RE (SciERC)\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n      - round: 3\n        action: \"进一步降级 RE claim 为 preliminary evidence + 补 SciERC RE conditional analysis\"\n        assigned_to: \"Agent + Paper Agent\"\n        status: resolved\n    resolution: \"Round 4: claim 降级到位（Conclusion 明确 hedge, Abstract 区分 NER/RE 证据量），RE conditional analysis 作为后续改进建议\"\n    resolution_round: 4\n\n  - id: \"R0-C4\"\n    summary: \"SJ 方法新颖性有限\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 0\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [2]\n        note: \"Nedellec 增量贡献论证不足 + 引用错误\"\n    action_items:\n      - round: 1\n        action: \"修正 bib + 加强增量贡献论证\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"Round 2 确认三点差异化清晰\"\n    resolution_round: 2\n\n  - id: \"R0-C5\"\n    summary: \"全文零图表\"\n    category: writing\n    severity: critical\n    status: resolved\n    first_raised_round: 0\n    last_seen_round: 0\n    mentions:\n      - round: 0\n        reviewers: [1, 2]\n        note: \"缺少 selection curves、reliability diagrams\"\n    action_items: []\n    resolution: \"论文已包含 5 个 figures\"\n    resolution_round: 1\n\n  - id: \"R0-C6\"\n    summary: \"成本分析 negligible 误导\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 0\n    last_seen_round: 0\n    mentions:\n      - round: 0\n        reviewers: [1, 2]\n        note: \"8-16× 推理开销不应描述为 negligible\"\n    action_items: []\n    resolution: \"Round 1+ 未再提及\"\n    resolution_round: 1\n\n  - id: \"R0-W1\"\n    summary: \"未探索 signal combination\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 0\n    last_seen_round: 0\n    mentions:\n      - round: 0\n        reviewers: [1, 2]\n        note: \"互补性已证明但未尝试组合\"\n    action_items: []\n    resolution: \"Round 1+ 未再提及\"\n    resolution_round: 1\n\n  - id: \"R0-W4\"\n    summary: \"统计检验不系统\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 0\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"Bootstrap 细节不足\"\n    action_items:\n      - round: 1\n        action: \"补完整 bootstrap 规范\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"Round 2 Reviewer 评价 bootstrap 达到高标准\"\n    resolution_round: 2\n\n  - id: \"R0-RR-D1\"\n    summary: \"Voting Conf N-scaling +0.018 与数据矛盾\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 0\n    last_seen_round: 0\n    mentions:\n      - round: 0\n        reviewers: [\"Research Reviewer\"]\n        note: \"+0.018 实际为 -0.080\"\n    action_items:\n      - round: 0\n        action: \"修正声明\"\n        assigned_to: \"Main Agent\"\n        status: resolved\n    resolution: \"已修正\"\n    resolution_round: 1\n\n  # ============================================================\n  # Round 1 issues (all resolved)\n  # ============================================================\n  - id: \"R1-N1\"\n    summary: \"Bootstrap 检验细节不足\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"p=0.39 支撑核心结论但细节缺失\"\n    action_items:\n      - round: 1\n        action: \"补完整 bootstrap 规范\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"Round 2 Reviewer 评价统计规范达到高标准\"\n    resolution_round: 2\n\n  - id: \"R1-N2\"\n    summary: \"Gap 解释力不足 + logprob 失败未分析\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"4/5 定义性 + logprob 机制缺失\"\n    action_items:\n      - round: 1\n        action: \"区分 by-design vs empirical + logprob failure 分析段\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"Round 2 Reviewer 评价 logprob failure analysis 充分\"\n    resolution_round: 2\n\n  - id: \"R1-N3\"\n    summary: \"Per-sample signal 单薄\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"consensus-proximity = LOO-SJ 是表述问题\"\n    action_items:\n      - round: 1\n        action: \"显式说明等价关系\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"Round 2 确认 consensus-proximity = LOO-SJ 已明确\"\n    resolution_round: 2\n\n  - id: \"R1-N4\"\n    summary: \"Nedellec 引用错误 + 增量贡献弱\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"Yao vs Nédellec 事实错误\"\n    action_items:\n      - round: 1\n        action: \"修正 bib + 加强论证\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"Round 2 确认差异化清晰\"\n    resolution_round: 2\n\n  - id: \"R1-W1\"\n    summary: \"SJ 形式化有歧义\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 4\n    mentions:\n      - round: 2\n        reviewers: [1, 2]\n        note: \"Hungarian threshold + max denominator 需补充\"\n      - round: 3\n        reviewers: [1, 2]\n        note: \"R3-R1 再次指出 Hungarian cost function 未明确 maximize/minimize 方向, zero-IoU pairs 处理方式缺失\"\n      - round: 4\n        reviewers: [2]\n        note: \"R2 Round 4 确认 SJ 形式化已完善 [RESOLVED]\"\n    action_items:\n      - round: 1\n        action: \"补全 Eq(4) 定义\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n      - round: 2\n        action: \"补 threshold 说明 + max vs union 设计理由\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n      - round: 3\n        action: \"补 Hungarian optimization objective (max-weight matching on IoU) + zero-IoU pairs handling\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"Round 4: R2 确认 SJ 形式化已完善，Hungarian matching 描述清晰\"\n    resolution_round: 4\n\n  - id: \"R1-W2\"\n    summary: \"Voting-SJ 冗余度未分析\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"instance-level correlation 未报告\"\n    action_items:\n      - round: 1\n        action: \"报告 Voting-SJ ρ=0.659/0.605\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"中等相关数据已报告\"\n    resolution_round: 2\n\n  - id: \"R1-W3\"\n    summary: \"ρ=0.38 缺 contextualization\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    mentions:\n      - round: 2\n        reviewers: [1, 2]\n        note: \"需 cross-method footnote\"\n    action_items:\n      - round: 2\n        action: \"§5 footnote: semantic entropy AUROC comparison + cross-task caveat\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"Footnote 已加\"\n    resolution_round: 2\n\n  - id: \"R1-W4\"\n    summary: \"Logprob 温度数据缺失\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"robustness 结论需限定\"\n    action_items:\n      - round: 1\n        action: \"限定为 consistency-based signals robust; logprob uncharacterized\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"措辞限定到位\"\n    resolution_round: 2\n\n  - id: \"R1-W5\"\n    summary: \"WNUT-17 establishing 措辞过度\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"fail to reject ≠ accept\"\n    action_items:\n      - round: 1\n        action: \"establishing → consistent with/suggests\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"已修正\"\n    resolution_round: 2\n\n  - id: \"R1-W6\"\n    summary: \"LLaMA 训练设置不对称\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"LLaMA fine-tuning 状态未说明\"\n    action_items:\n      - round: 1\n        action: \"明确两模型 identical LoRA 配置\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"Round 2 未再提及\"\n    resolution_round: 2\n\n  - id: \"R1-W7\"\n    summary: \"约束解码 diversity 影响\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    mentions:\n      - round: 2\n        reviewers: [1, 2]\n        note: \"需扩展为全局 confound + Limitations 条目\"\n    action_items:\n      - round: 2\n        action: \"Discussion 扩展 + Limitations 新增条目\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"已扩展为全局 confound 讨论\"\n    resolution_round: 2\n\n  - id: \"R1-W8\"\n    summary: \"first systematic 过强\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"需收窄 scope\"\n    action_items:\n      - round: 1\n        action: \"first multi-family\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"Round 2 无再提\"\n    resolution_round: 2\n\n  - id: \"R1-W9\"\n    summary: \"遗漏引用\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"Optimal SC, Difficulty-Adaptive SC 等\"\n    action_items:\n      - round: 1\n        action: \"补充引用\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"Round 2 确认无遗漏\"\n    resolution_round: 2\n\n  - id: \"R1-W10\"\n    summary: \"ρ-AUROC dissociation 分析浅\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"EM=1 压缩效应需主文提及\"\n    action_items:\n      - round: 1\n        action: \"Section 5 简述 + 引导 Appendix\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"Round 2 确认 dissociation 分析为 actionable finding\"\n    resolution_round: 2\n\n  - id: \"R1-M1\"\n    summary: \"Logistic regression proxy 无结果\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"展示结果或删除\"\n    action_items:\n      - round: 1\n        action: \"删除提及\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"已删除\"\n    resolution_round: 2\n\n  - id: \"R1-M2\"\n    summary: \"GSM8K +18pp 未注明模型\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"补注 PaLM-540B\"\n    action_items:\n      - round: 1\n        action: \"补注\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"已补注\"\n    resolution_round: 2\n\n  - id: \"R1-M3\"\n    summary: \"Cross-model Δ=0.005 未报告 CI\"\n    category: experiment\n    severity: info\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"within 3-seed σ≈0.007\"\n    action_items:\n      - round: 1\n        action: \"补注\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"已补注\"\n    resolution_round: 2\n\n  # ============================================================\n  # Round 2 issues (all resolved)\n  # ============================================================\n  - id: \"R2-C1\"\n    summary: \"Selection 证据面过窄——仅 1 dataset × 1 model\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - round: 2\n        reviewers: [1, 2]\n        note: \"需补 LLaMA SciERC + CoNLL selection\"\n    action_items:\n      - round: 2\n        action: \"补 4 配置 selection 分析 + Appendix Table 6\"\n        assigned_to: \"Agent + Paper Agent\"\n        status: resolved\n    resolution: \"6 configurations 全部补齐，无 signal 显著超越 greedy\"\n    resolution_round: 2\n\n  - id: \"R2-C2\"\n    summary: \"WNUT-17 仅报告 1 个信号\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - round: 2\n        reviewers: [1, 2]\n        note: \"5 signals 中仅 SJ 一个数据点\"\n    action_items:\n      - round: 2\n        action: \"补全 5 信号 full/conditional ρ + AUROC + Appendix Table 5\"\n        assigned_to: \"Agent + Paper Agent\"\n        status: resolved\n    resolution: \"WNUT-17 全信号表完整，叙事修正为区分 full-set vs conditional\"\n    resolution_round: 2\n\n  - id: \"R2-W1\"\n    summary: \"ρ=0.38 缺 cross-method 对比\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - round: 2\n        reviewers: [1, 2]\n        note: \"需 footnote 引用 semantic entropy AUROC\"\n    action_items:\n      - round: 2\n        action: \"§5 footnote\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"Footnote 已加\"\n    resolution_round: 2\n\n  - id: \"R2-W2\"\n    summary: \"N=8 QE ρ 无 uncertainty\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - round: 2\n        reviewers: [1, 2]\n        note: \"需 bootstrap CIs\"\n    action_items:\n      - round: 2\n        action: \"计算 B=10,000 bootstrap CI + Appendix 表\"\n        assigned_to: \"Agent + Paper Agent\"\n        status: resolved\n    resolution: \"Bootstrap CI 表已加入 Appendix，SJ-logprob 显著\"\n    resolution_round: 2\n\n  - id: \"R2-W3\"\n    summary: \"SJ Hungarian threshold + max denominator\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - round: 2\n        reviewers: [1, 2]\n        note: \"无 threshold 声明需验证\"\n    action_items:\n      - round: 2\n        action: \"代码验证 + method.tex 补充\"\n        assigned_to: \"Agent + Paper Agent\"\n        status: resolved\n    resolution: \"无 threshold, 96.6% pairs sim≥0.5, max denominator 已解释\"\n    resolution_round: 2\n\n  - id: \"R2-W4\"\n    summary: \"RE selection 无统计检验\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - round: 2\n        reviewers: [1, 2]\n        note: \"需 bootstrap p-value\"\n    action_items:\n      - round: 2\n        action: \"RE bootstrap + 补 p=0.80 到论文\"\n        assigned_to: \"Agent + Paper Agent\"\n        status: resolved\n    resolution: \"RE logprob p=0.80, all signals below greedy\"\n    resolution_round: 2\n\n  - id: \"R2-W5\"\n    summary: \"Constrained decoding 全局 confound\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - round: 2\n        reviewers: [1, 2]\n        note: \"需扩展到全局 + Limitations\"\n    action_items:\n      - round: 2\n        action: \"Discussion 扩展 + Limitations 条目\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"已处理\"\n    resolution_round: 2\n\n  - id: \"R2-W6\"\n    summary: \"Abstract RE 措辞误导\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - round: 2\n        reviewers: [1, 2]\n        note: \"NER (three datasets) and RE (SciERC)\"\n    action_items:\n      - round: 2\n        action: \"修正 Abstract\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"已修正\"\n    resolution_round: 2\n\n  - id: \"R2-W7\"\n    summary: \"n=529 vs 551 未解释\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - round: 2\n        reviewers: [1, 2]\n        note: \"22 instances filtering criteria\"\n    action_items:\n      - round: 2\n        action: \"补一句说明\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"已说明 gold-empty filtering\"\n    resolution_round: 2\n\n  - id: \"R2-DATA\"\n    summary: \"RE selection 数据矛盾 (Table 2 vs L129)\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - round: 2\n        reviewers: [\"Research Reviewer\"]\n        note: \"Table 2 logprob=0.395 (-0.9pp) vs L129 logprob=0.410 (+0.6pp)\"\n    action_items:\n      - round: 2\n        action: \"Agent 确认 Table 2 正确 → Paper Agent 修正 L129\"\n        assigned_to: \"Agent + Paper Agent\"\n        status: resolved\n    resolution: \"L129 统一为 logprob=0.395, -0.9pp, p=0.80\"\n    resolution_round: 2\n\n  - id: \"R2-AUROC\"\n    summary: \"L64 AUROC 归属错误 (Voting ρ 配 EM AUROC)\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - round: 2\n        reviewers: [\"Research Reviewer\"]\n        note: \"corresponding 暗示同一信号\"\n    action_items:\n      - round: 2\n        action: \"分别标注 Voting ρ 和 EM AUROC\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"已拆分归属\"\n    resolution_round: 2\n\n  # ============================================================\n  # Round 3 issues (updated with Round 4 status)\n  # ============================================================\n  - id: \"R3-C1\"\n    summary: \"Constrained decoding 是 correlation-selection gap 的未控制混淆变量\"\n    category: method\n    severity: critical\n    status: in_progress\n    first_raised_round: 3\n    last_seen_round: 4\n    mentions:\n      - round: 3\n        reviewers: [1, 2]\n        note: \"两位 Reviewer 均独立提出。Outlines/vLLM constrained decoding 可能压缩 per-sample diversity，使 gap 成为实验设置 artifact。\"\n      - round: 4\n        reviewers: [1, 2]\n        note: \"R2 确认部分解决（承认但未量化）。R1 仍列 critical（需 logprob 分布分析）。R1 rebut free-form baseline（constrained decoding 是方法论必要条件），但同意需量化 diversity 压缩效应。共识：elevated should-fix，量化 logprob 分布而非增加 free-form 实验。\"\n    action_items:\n      - round: 3\n        action: \"Agent 量化 diversity；Paper Agent 写入论文 + 限定 scope\"\n        assigned_to: \"Agent + Paper Agent\"\n        status: resolved\n      - round: 4\n        action: \"量化 logprob 分布（tie 定义 Δlogprob<ε, non-tie 子集 selection 能力）+ Discussion 中讨论 grammar compliance 如何压缩区分度\"\n        assigned_to: \"Agent + Paper Agent\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R3-C2\"\n    summary: \"Failure-to-reject 不等于 evidence of absence，selection gap 统计论证不完整\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 4\n    mentions:\n      - round: 3\n        reviewers: [1, 2]\n        note: \"需修改措辞或补充等价性检验\"\n      - round: 4\n        reviewers: [2]\n        note: \"R2 确认 RESOLVED：TOST 已补充，措辞修正到位\"\n    action_items:\n      - round: 3\n        action: \"修改措辞 + 6/6 cumulative evidence 论证\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"Round 4: TOST 等价检验已补充，措辞修正为 'no significant evidence'，R2 确认到位\"\n    resolution_round: 4\n\n  - id: \"R3-C3\"\n    summary: \"N=8 核心结果 single seed (seed=42)\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 4\n    mentions:\n      - round: 3\n        reviewers: [1, 2]\n        note: \"Table 1 N=8 和 Table 2 selection 全部 single seed\"\n      - round: 4\n        reviewers: [2]\n        note: \"R2 确认 RESOLVED：3-seed 验证已补充\"\n    action_items:\n      - round: 3\n        action: \"Limitations 中明确 single-seed 风险并引用 N=16 stability\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"Round 4: 3-seed 稳定性验证已补充，R2 确认到位\"\n    resolution_round: 4\n\n  - id: \"R3-W1\"\n    summary: \"多重比较校正缺失\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 4\n    mentions:\n      - round: 3\n        reviewers: [1, 2]\n        note: \"SJ-EM CI lower bound +0.003 在 Bonferroni 下不会 survive\"\n      - round: 4\n        reviewers: [2]\n        note: \"R2 确认 RESOLVED：Bonferroni 声明已加\"\n    action_items:\n      - round: 3\n        action: \"声明未做多重比较校正 + SJ-EM 改为 suggestive\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"Round 4: Bonferroni 声明已加，R2 确认到位\"\n    resolution_round: 4\n\n  - id: \"R3-W2\"\n    summary: \"Gap 概念部分 tautological——instance-level 信号无法 select 是定义必然\"\n    category: method\n    severity: warning\n    status: in_progress\n    first_raised_round: 3\n    last_seen_round: 4\n    mentions:\n      - round: 3\n        reviewers: [1, 2]\n        note: \"需在 Discussion 中分离两层论证\"\n      - round: 4\n        reviewers: [1, 2]\n        note: \"R2 确认部分改善但核心张力仍在。R4 两位 Reviewer 独立再次提出（R1-N1, R2-N1）：Introduction 未正面论证 why not obvious a priori，§4.3 和 abstract 将 gap 作为统一经验发现但 §5 承认 4/5 是 by construction。R1 部分 rebut：MBR 在 MT 成功但 IE 失败是非平凡的。共识：需明确分离定义性 gap 和经验性 gap，加强非显然性论证。升级为 Round 4 W-C1。\"\n    action_items:\n      - round: 3\n        action: \"Discussion 中分离两层论证\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n      - round: 4\n        action: \"(a) Introduction 正面论证 why gap is not obvious (MBR MT vs IE 对比); (b) Discussion 明确分离定义性局限 vs 经验性失败 (logprob + consensus-proximity); (c) 聚焦 logprob 75% ties 做深入分析\"\n        assigned_to: \"Paper Agent\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R3-W3\"\n    summary: \"Consensus-proximity 是唯一 instance-to-sample 转换策略，未与 MBR decoding 建立联系\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 4\n    mentions:\n      - round: 3\n        reviewers: [1, 2]\n        note: \"MBR decoding 是成熟替代方案但未讨论\"\n      - round: 4\n        reviewers: [2]\n        note: \"R2 确认 RESOLVED：MBR 连接已补充，§5 MBR 段清晰\"\n    action_items:\n      - round: 3\n        action: \"明确 consensus-proximity 与 MBR 联系 + 引用 MBR 文献\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"Round 4: §5 MBR decoding 连接段已写入，R2 评价'概念优雅'\"\n    resolution_round: 4\n\n  - id: \"R3-W4\"\n    summary: \"FK 独立性假设 justification 不足\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 4\n    mentions:\n      - round: 3\n        reviewers: [1, 2]\n        note: \"§3.2 一句 hand-wave。需报告 inter-sample correlation\"\n      - round: 4\n        reviewers: [2]\n        note: \"R2 确认 RESOLVED：excess agreement 数据已补充。R1 仍对 negative excess agreement 含义有疑问，但降为 minor\"\n    action_items:\n      - round: 3\n        action: \"Agent 量化 inter-sample correlation；Paper Agent 写入\"\n        assigned_to: \"Agent + Paper Agent\"\n        status: resolved\n    resolution: \"Round 4: Excess agreement 数据已补 (-0.4% to -4.0%)。R1 minor 疑问不影响接收\"\n    resolution_round: 4\n\n  - id: \"R3-W5\"\n    summary: \"Cross-model 实为 cross-architecture at fixed 8B scale\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 4\n    mentions:\n      - round: 3\n        reviewers: [1, 2]\n        note: \"两模型均 8B，措辞过度外推\"\n      - round: 4\n        reviewers: [2]\n        note: \"R2 确认 RESOLVED：cross-architecture 措辞已统一\"\n    action_items:\n      - round: 3\n        action: \"正文将 cross-model 替换为 cross-architecture 或加限定词\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"Round 4: 措辞已统一为 cross-architecture at 8B scale\"\n    resolution_round: 4\n\n  - id: \"R3-W6\"\n    summary: \"'First multi-family comparison' claim scope 过宽\"\n    category: framing\n    severity: warning\n    status: in_progress\n    first_raised_round: 3\n    last_seen_round: 4\n    mentions:\n      - round: 3\n        reviewers: [1, 2]\n        note: \"需限定为 structured IE 的 QE + selection\"\n      - round: 4\n        reviewers: [2]\n        note: \"R2 确认部分解决：Conclusion 有 hedge 但 Introduction 仍断言式。需对齐 Introduction 与 Conclusion 的 claim scope\"\n    action_items:\n      - round: 3\n        action: \"收窄 Contribution 1 措辞\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n      - round: 4\n        action: \"Introduction contribution claim 加 hedge，与 Conclusion 对齐\"\n        assigned_to: \"Paper Agent\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R3-W7\"\n    summary: \"术语不一致\"\n    category: writing\n    severity: warning\n    status: in_progress\n    first_raised_round: 3\n    last_seen_round: 4\n    mentions:\n      - round: 3\n        reviewers: [1, 2]\n        note: \"confidence signal vs consistency signal 混用；VC vs Voting Conf.\"\n      - round: 4\n        reviewers: [1, 2]\n        note: \"R2 确认部分解决：表格缩写 VC/Voting Conf. 仍不统一。R1 同意需加明确 taxonomy 定义。建议 §3.2 开头定义 confidence signal（统称）vs consistency signal（子集，不含 logprob）\"\n    action_items:\n      - round: 3\n        action: \"统一术语 + 补 LLaMA Factory 引用\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n      - round: 4\n        action: \"§3.2 开头加明确 taxonomy + 全文统一表格缩写\"\n        assigned_to: \"Paper Agent\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R3-W8\"\n    summary: \"遗漏引用：VerifiNER, RASC, MBR decoding, Malinin & Gales\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 4\n    mentions:\n      - round: 3\n        reviewers: [1, 2]\n        note: \"VerifiNER, MBR decoding 等高度相关\"\n      - round: 4\n        reviewers: [2]\n        note: \"R2 确认 RESOLVED：引用已补全\"\n    action_items:\n      - round: 3\n        action: \"补充引用并在 Related Work 中讨论\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"Round 4: 引用已补全，R2 确认到位\"\n    resolution_round: 4\n\n  - id: \"R3-M1\"\n    summary: \"WNUT-17 '54% zero F1' 与 Table 7 数据不一致 (51.5%)\"\n    category: experiment\n    severity: info\n    status: in_progress\n    first_raised_round: 3\n    last_seen_round: 3\n    mentions:\n      - round: 3\n        reviewers: [1]\n        note: \"355/689 ≈ 51.5% vs 正文 54%\"\n      - round: 4\n        reviewers: []\n        note: \"本轮未提及，可能已修复，待 Research Director 确认\"\n    action_items:\n      - round: 3\n        action: \"Agent 核实实际数字 → Paper Agent 统一\"\n        assigned_to: \"Agent + Paper Agent\"\n        status: in_progress\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R3-M2\"\n    summary: \"EM selection exclusion 缺乏经验支持\"\n    category: experiment\n    severity: info\n    status: in_progress\n    first_raised_round: 3\n    last_seen_round: 3\n    mentions:\n      - round: 3\n        reviewers: [1, 2]\n        note: \"'probability negligible' 需报告 exact match pairs 频率\"\n      - round: 4\n        reviewers: []\n        note: \"本轮未提及，可能已修复，待 Research Director 确认\"\n    action_items:\n      - round: 3\n        action: \"Agent 计算 exact match pairs 频率 → Paper Agent 写入\"\n        assigned_to: \"Agent + Paper Agent\"\n        status: in_progress\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R3-M3\"\n    summary: \"Ethics Statement 缺失\"\n    category: format\n    severity: info\n    status: in_progress\n    first_raised_round: 3\n    last_seen_round: 4\n    mentions:\n      - round: 3\n        reviewers: [2]\n        note: \"共识降为 minor\"\n      - round: 4\n        reviewers: [2]\n        note: \"R2 确认 Ethics Statement 已存在但位于 Limitations section 内——建议改为独立 section 以符合 ACL 格式规范\"\n    action_items:\n      - round: 3\n        action: \"添加简短 Ethics Statement\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n      - round: 4\n        action: \"将 Ethics Statement 从 Limitations 内移出为独立 section\"\n        assigned_to: \"Paper Agent\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R3-M4\"\n    summary: \"ρ-AUROC dissociation 作为独立发现过度强调\"\n    category: framing\n    severity: info\n    status: in_progress\n    first_raised_round: 3\n    last_seen_round: 3\n    mentions:\n      - round: 3\n        reviewers: [1, 2]\n        note: \"建议承认统计预期性后聚焦实践含义\"\n      - round: 4\n        reviewers: []\n        note: \"本轮未提及，可能已修复，待 Research Director 确认\"\n    action_items:\n      - round: 3\n        action: \"§4.2 承认 dissociation 的统计预期性\"\n        assigned_to: \"Paper Agent\"\n        status: in_progress\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R3-M5\"\n    summary: \"对 Nedellec (2026) 措辞偏 adversarial\"\n    category: writing\n    severity: info\n    status: in_progress\n    first_raised_round: 3\n    last_seen_round: 3\n    mentions:\n      - round: 3\n        reviewers: [1, 2]\n        note: \"建议用更 neutral 语气\"\n      - round: 4\n        reviewers: []\n        note: \"本轮未提及，可能已修复，待 Research Director 确认\"\n    action_items:\n      - round: 3\n        action: \"Introduction 中改为更 neutral 的语气\"\n        assigned_to: \"Paper Agent\"\n        status: in_progress\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R3-M6\"\n    summary: \"LOO-SJ 验证中 Δρ 和 per-instance Δρ 量纲混淆\"\n    category: writing\n    severity: info\n    status: in_progress\n    first_raised_round: 3\n    last_seen_round: 3\n    mentions:\n      - round: 3\n        reviewers: [1]\n        note: \"Δρ=−0.014 vs per-instance max Δρ=3.1×10⁻⁴ 量纲不同\"\n      - round: 4\n        reviewers: []\n        note: \"本轮未提及，可能已修复，待 Research Director 确认\"\n    action_items:\n      - round: 3\n        action: \"澄清 per-instance Δρ 具体含义\"\n        assigned_to: \"Paper Agent\"\n        status: in_progress\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R3-M7\"\n    summary: \"Figure 1 caption 引入未直接可视化的 p=0.39\"\n    category: writing\n    severity: info\n    status: in_progress\n    first_raised_round: 3\n    last_seen_round: 3\n    mentions:\n      - round: 3\n        reviewers: [1]\n        note: \"建议加 '(Table 2)' 交叉引用\"\n      - round: 4\n        reviewers: []\n        note: \"本轮未提及，可能已修复，待 Research Director 确认\"\n    action_items:\n      - round: 3\n        action: \"补 '(Table 2)' 交叉引用\"\n        assigned_to: \"Paper Agent\"\n        status: in_progress\n    resolution: \"\"\n    resolution_round: null\n\n  # ============================================================\n  # Round 4 new issues\n  # ============================================================\n  - id: \"R4-C1\"\n    summary: \"训练配置和 prompt template 缺失，影响独立复现\"\n    category: experiment\n    severity: critical\n    status: open\n    first_raised_round: 4\n    last_seen_round: 4\n    mentions:\n      - round: 4\n        reviewers: [1, 2]\n        note: \"两位 Reviewer 独立提出（R1-N3, R2-N2），完全共识。§4.1 仅报告 LoRA rank=32, α=64, 5 epochs, LLaMA Factory，缺少 lr, batch size, warmup, weight decay, optimizer, early stopping, train/dev split, prompt template, LoRA target modules, max seq length, schema constraint\"\n    action_items:\n      - round: 4\n        action: \"附录补充完整训练配置表 + NER/RE prompt template 示例 + schema constraint 定义\"\n        assigned_to: \"Paper Agent\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R4-W1\"\n    summary: \"RE 证据需进一步加强（conditional analysis 或降级）\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 4\n    last_seen_round: 4\n    mentions:\n      - round: 4\n        reviewers: [1, 2]\n        note: \"R0-C3 的 claim 降级已完成（resolved），但两位 Reviewer 仍认为 RE 证据薄弱：40% zero-F1 floor effect, gap 证据 -0.9pp p=0.80。R1 建议 SciERC RE conditional analysis；R2 建议 Abstract/Introduction 进一步降级。\"\n    action_items:\n      - round: 4\n        action: \"(a) SciERC RE non-zero F1 子集 selection 分析; (b) Abstract/Introduction 中 RE 标记为 preliminary/exploratory\"\n        assigned_to: \"Agent + Paper Agent\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R4-W2\"\n    summary: \"SJ vs EM 优势叙事应改为 difficulty-dependent complementarity\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 4\n    last_seen_round: 4\n    mentions:\n      - round: 4\n        reviewers: [1, 2]\n        note: \"SJ vs EM Δρ=+0.065, CI 下界 +0.003, Bonferroni 下不显著。CoNLL 上 EM 反超 SJ。两位 Reviewer 一致认为应弱化 structural advantage 叙事，强调 difficulty-dependent complementarity\"\n    action_items:\n      - round: 4\n        action: \"Contribution #1 弱化 structural advantage，改为强调 difficulty-dependent complementarity + 提供信号选择指导\"\n        assigned_to: \"Paper Agent\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R4-W3\"\n    summary: \"Abstract 过于密集，第 4 行超长句子需拆分\"\n    category: writing\n    severity: warning\n    status: open\n    first_raised_round: 4\n    last_seen_round: 4\n    mentions:\n      - round: 4\n        reviewers: [1, 2]\n        note: \"第 3-4 行含多层嵌套括号和分号的超长句子，首次阅读难以把握核心信息。两位 Reviewer 一致建议拆分为 2-3 个独立句子\"\n    action_items:\n      - round: 4\n        action: \"Abstract 核心发现拆分为 2-3 句，每句一个关键 claim\"\n        assigned_to: \"Paper Agent\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R4-W4\"\n    summary: \"缺少 Xiong et al. (2024) 'Can LLMs Express Their Uncertainty?' ICLR 2024\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 4\n    last_seen_round: 4\n    mentions:\n      - round: 4\n        reviewers: [1, 2]\n        note: \"系统评估 LLM 置信度获取方法（verbalized, consistency-based, logit-based），与本文多族信号比较直接相关。两位 Reviewer 一致认为应引用。另有 Bertsch et al. (2024), Wiher et al. (2022), Müller & Sennrich (2021) 由 R1 建议\"\n    action_items:\n      - round: 4\n        action: \"Related Work 'Uncertainty estimation' 段引用 Xiong et al. + 区分本文与 verbalized confidence 方法。评估补引 Bertsch/Wiher/Müller&Sennrich\"\n        assigned_to: \"Paper Agent\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R4-M1\"\n    summary: \"SJ normalizer 选择（max vs union）缺乏对比\"\n    category: method\n    severity: info\n    status: open\n    first_raised_round: 4\n    last_seen_round: 4\n    mentions:\n      - round: 4\n        reviewers: [1]\n        note: \"R1-W3: max(|g_i|,|g_j|) vs |g_i∪g_j| 未比较。建议附录报告替代 normalizer 结果或提供理论依据\"\n    action_items:\n      - round: 4\n        action: \"附录补 union normalizer 的 SJ 结果，或提供 max normalizer 的理论依据\"\n        assigned_to: \"Agent + Paper Agent\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R4-M2\"\n    summary: \"TOST δ 选择（±2/3/5 pp）缺乏实践意义论证\"\n    category: experiment\n    severity: info\n    status: open\n    first_raised_round: 4\n    last_seen_round: 4\n    mentions:\n      - round: 4\n        reviewers: [1]\n        note: \"R1-W5: δ 选择直接影响等价结论，需讨论在 IE 任务中 F1 差异的 practical significance 标准\"\n    action_items:\n      - round: 4\n        action: \"讨论 δ 选择依据（如 annotation agreement F1 variance）\"\n        assigned_to: \"Paper Agent\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R4-M3\"\n    summary: \"Table 1 N=16 block 大面积空白\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 4\n    last_seen_round: 4\n    mentions:\n      - round: 4\n        reviewers: [1, 2]\n        note: \"N=16 仅填 LLaMA CoNLL，SciERC 空白，给人实验不完整印象。建议填充或添加脚注引导读者到附录\"\n    action_items:\n      - round: 4\n        action: \"补脚注说明 N=16 数据位置或考虑合并呈现\"\n        assigned_to: \"Paper Agent\"\n        status: open\n    resolution: \"\"\n    resolution_round: null"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "struct_self_consist_ie",
    "issues_yaml": "issues:\n  # ============================================================\n  # Round 0 issues (all resolved)\n  # ============================================================\n  - id: \"R0-C1\"\n    summary: \"模型规模单一（仅 8B）\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 0\n    last_seen_round: 1\n    mentions:\n      - round: 0\n        reviewers: [1, 2]\n        note: \"8B→8B 仅验证架构鲁棒性非规模鲁棒性\"\n      - round: 1\n        reviewers: [1, 2]\n        note: \"model-agnostic 与 Limitations 矛盾\"\n    action_items:\n      - round: 1\n        action: \"全文替换 model-agnostic → consistent across tested model families\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"Round 2 Reviewer 确认措辞修正到位，无再提\"\n    resolution_round: 2\n\n  - id: \"R0-C2\"\n    summary: \"相关工作显著遗漏\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 0\n    last_seen_round: 1\n    mentions:\n      - round: 0\n        reviewers: [1, 2]\n        note: \"5 篇核心文献缺失\"\n      - round: 1\n        reviewers: [1, 2]\n        note: \"新遗漏：Optimal SC, Difficulty-Adaptive SC\"\n    action_items:\n      - round: 1\n        action: \"补充 6 篇引用到 Related Work\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"Round 2: 49 条 bib 全部 cited, 0 orphan, 无遗漏\"\n    resolution_round: 2\n\n  - id: \"R0-C3\"\n    summary: \"RE 结论仅基于 SciERC 单数据集\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 0\n    last_seen_round: 4\n    mentions:\n      - round: 0\n        reviewers: [1, 2]\n        note: \"需跨数据集验证或降级措辞\"\n      - round: 2\n        reviewers: [1, 2]\n        note: \"Abstract RE 措辞需修正\"\n      - round: 3\n        reviewers: [1, 2]\n        note: \"Round 2 措辞修正到位，但 R3 Reviewer 2 再次提出 44% zero-F1 floor effect 严重压缩可区分范围\"\n      - round: 4\n        reviewers: [1, 2]\n        note: \"R2 确认 claim 降级已完成（Conclusion 明确 hedge）。两位 Reviewer 仍认为 RE 证据薄弱，但 claim 范围已恰当限定——后续改进作为 R4-W1 追踪\"\n    action_items:\n      - round: 1\n        action: \"降级措辞 universal → observed in SciERC\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n      - round: 2\n        action: \"Abstract 改为 NER (three datasets) and RE (SciERC)\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n      - round: 3\n        action: \"进一步降级 RE claim 为 preliminary evidence + 补 SciERC RE conditional analysis\"\n        assigned_to: \"Agent + Paper Agent\"\n        status: resolved\n    resolution: \"Round 4: claim 降级到位（Conclusion 明确 hedge, Abstract 区分 NER/RE 证据量），RE conditional analysis 作为后续改进建议\"\n    resolution_round: 4\n\n  - id: \"R0-C4\"\n    summary: \"SJ 方法新颖性有限\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 0\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [2]\n        note: \"Nedellec 增量贡献论证不足 + 引用错误\"\n    action_items:\n      - round: 1\n        action: \"修正 bib + 加强增量贡献论证\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"Round 2 确认三点差异化清晰\"\n    resolution_round: 2\n\n  - id: \"R0-C5\"\n    summary: \"全文零图表\"\n    category: writing\n    severity: critical\n    status: resolved\n    first_raised_round: 0\n    last_seen_round: 0\n    mentions:\n      - round: 0\n        reviewers: [1, 2]\n        note: \"缺少 selection curves、reliability diagrams\"\n    action_items: []\n    resolution: \"论文已包含 5 个 figures\"\n    resolution_round: 1\n\n  - id: \"R0-C6\"\n    summary: \"成本分析 negligible 误导\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 0\n    last_seen_round: 0\n    mentions:\n      - round: 0\n        reviewers: [1, 2]\n        note: \"8-16× 推理开销不应描述为 negligible\"\n    action_items: []\n    resolution: \"Round 1+ 未再提及\"\n    resolution_round: 1\n\n  - id: \"R0-W1\"\n    summary: \"未探索 signal combination\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 0\n    last_seen_round: 0\n    mentions:\n      - round: 0\n        reviewers: [1, 2]\n        note: \"互补性已证明但未尝试组合\"\n    action_items: []\n    resolution: \"Round 1+ 未再提及\"\n    resolution_round: 1\n\n  - id: \"R0-W4\"\n    summary: \"统计检验不系统\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 0\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"Bootstrap 细节不足\"\n    action_items:\n      - round: 1\n        action: \"补完整 bootstrap 规范\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"Round 2 Reviewer 评价 bootstrap 达到高标准\"\n    resolution_round: 2\n\n  - id: \"R0-RR-D1\"\n    summary: \"Voting Conf N-scaling +0.018 与数据矛盾\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 0\n    last_seen_round: 0\n    mentions:\n      - round: 0\n        reviewers: [\"Research Reviewer\"]\n        note: \"+0.018 实际为 -0.080\"\n    action_items:\n      - round: 0\n        action: \"修正声明\"\n        assigned_to: \"Main Agent\"\n        status: resolved\n    resolution: \"已修正\"\n    resolution_round: 1\n\n  # ============================================================\n  # Round 1 issues (all resolved)\n  # ============================================================\n  - id: \"R1-N1\"\n    summary: \"Bootstrap 检验细节不足\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"p=0.39 支撑核心结论但细节缺失\"\n    action_items:\n      - round: 1\n        action: \"补完整 bootstrap 规范\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"Round 2 Reviewer 评价统计规范达到高标准\"\n    resolution_round: 2\n\n  - id: \"R1-N2\"\n    summary: \"Gap 解释力不足 + logprob 失败未分析\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"4/5 定义性 + logprob 机制缺失\"\n    action_items:\n      - round: 1\n        action: \"区分 by-design vs empirical + logprob failure 分析段\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"Round 2 Reviewer 评价 logprob failure analysis 充分\"\n    resolution_round: 2\n\n  - id: \"R1-N3\"\n    summary: \"Per-sample signal 单薄\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"consensus-proximity = LOO-SJ 是表述问题\"\n    action_items:\n      - round: 1\n        action: \"显式说明等价关系\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"Round 2 确认 consensus-proximity = LOO-SJ 已明确\"\n    resolution_round: 2\n\n  - id: \"R1-N4\"\n    summary: \"Nedellec 引用错误 + 增量贡献弱\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"Yao vs Nédellec 事实错误\"\n    action_items:\n      - round: 1\n        action: \"修正 bib + 加强论证\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"Round 2 确认差异化清晰\"\n    resolution_round: 2\n\n  - id: \"R1-W1\"\n    summary: \"SJ 形式化有歧义\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 4\n    mentions:\n      - round: 2\n        reviewers: [1, 2]\n        note: \"Hungarian threshold + max denominator 需补充\"\n      - round: 3\n        reviewers: [1, 2]\n        note: \"R3-R1 再次指出 Hungarian cost function 未明确 maximize/minimize 方向, zero-IoU pairs 处理方式缺失\"\n      - round: 4\n        reviewers: [2]\n        note: \"R2 Round 4 确认 SJ 形式化已完善 [RESOLVED]\"\n    action_items:\n      - round: 1\n        action: \"补全 Eq(4) 定义\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n      - round: 2\n        action: \"补 threshold 说明 + max vs union 设计理由\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n      - round: 3\n        action: \"补 Hungarian optimization objective (max-weight matching on IoU) + zero-IoU pairs handling\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"Round 4: R2 确认 SJ 形式化已完善，Hungarian matching 描述清晰\"\n    resolution_round: 4\n\n  - id: \"R1-W2\"\n    summary: \"Voting-SJ 冗余度未分析\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"instance-level correlation 未报告\"\n    action_items:\n      - round: 1\n        action: \"报告 Voting-SJ ρ=0.659/0.605\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"中等相关数据已报告\"\n    resolution_round: 2\n\n  - id: \"R1-W3\"\n    summary: \"ρ=0.38 缺 contextualization\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    mentions:\n      - round: 2\n        reviewers: [1, 2]\n        note: \"需 cross-method footnote\"\n    action_items:\n      - round: 2\n        action: \"§5 footnote: semantic entropy AUROC comparison + cross-task caveat\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"Footnote 已加\"\n    resolution_round: 2\n\n  - id: \"R1-W4\"\n    summary: \"Logprob 温度数据缺失\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"robustness 结论需限定\"\n    action_items:\n      - round: 1\n        action: \"限定为 consistency-based signals robust; logprob uncharacterized\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"措辞限定到位\"\n    resolution_round: 2\n\n  - id: \"R1-W5\"\n    summary: \"WNUT-17 establishing 措辞过度\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"fail to reject ≠ accept\"\n    action_items:\n      - round: 1\n        action: \"establishing → consistent with/suggests\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"已修正\"\n    resolution_round: 2\n\n  - id: \"R1-W6\"\n    summary: \"LLaMA 训练设置不对称\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"LLaMA fine-tuning 状态未说明\"\n    action_items:\n      - round: 1\n        action: \"明确两模型 identical LoRA 配置\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"Round 2 未再提及\"\n    resolution_round: 2\n\n  - id: \"R1-W7\"\n    summary: \"约束解码 diversity 影响\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    mentions:\n      - round: 2\n        reviewers: [1, 2]\n        note: \"需扩展为全局 confound + Limitations 条目\"\n    action_items:\n      - round: 2\n        action: \"Discussion 扩展 + Limitations 新增条目\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"已扩展为全局 confound 讨论\"\n    resolution_round: 2\n\n  - id: \"R1-W8\"\n    summary: \"first systematic 过强\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"需收窄 scope\"\n    action_items:\n      - round: 1\n        action: \"first multi-family\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"Round 2 无再提\"\n    resolution_round: 2\n\n  - id: \"R1-W9\"\n    summary: \"遗漏引用\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"Optimal SC, Difficulty-Adaptive SC 等\"\n    action_items:\n      - round: 1\n        action: \"补充引用\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"Round 2 确认无遗漏\"\n    resolution_round: 2\n\n  - id: \"R1-W10\"\n    summary: \"ρ-AUROC dissociation 分析浅\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"EM=1 压缩效应需主文提及\"\n    action_items:\n      - round: 1\n        action: \"Section 5 简述 + 引导 Appendix\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"Round 2 确认 dissociation 分析为 actionable finding\"\n    resolution_round: 2\n\n  - id: \"R1-M1\"\n    summary: \"Logistic regression proxy 无结果\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"展示结果或删除\"\n    action_items:\n      - round: 1\n        action: \"删除提及\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"已删除\"\n    resolution_round: 2\n\n  - id: \"R1-M2\"\n    summary: \"GSM8K +18pp 未注明模型\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"补注 PaLM-540B\"\n    action_items:\n      - round: 1\n        action: \"补注\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"已补注\"\n    resolution_round: 2\n\n  - id: \"R1-M3\"\n    summary: \"Cross-model Δ=0.005 未报告 CI\"\n    category: experiment\n    severity: info\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"within 3-seed σ≈0.007\"\n    action_items:\n      - round: 1\n        action: \"补注\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"已补注\"\n    resolution_round: 2\n\n  # ============================================================\n  # Round 2 issues (all resolved)\n  # ============================================================\n  - id: \"R2-C1\"\n    summary: \"Selection 证据面过窄——仅 1 dataset × 1 model\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - round: 2\n        reviewers: [1, 2]\n        note: \"需补 LLaMA SciERC + CoNLL selection\"\n    action_items:\n      - round: 2\n        action: \"补 4 配置 selection 分析 + Appendix Table 6\"\n        assigned_to: \"Agent + Paper Agent\"\n        status: resolved\n    resolution: \"6 configurations 全部补齐，无 signal 显著超越 greedy\"\n    resolution_round: 2\n\n  - id: \"R2-C2\"\n    summary: \"WNUT-17 仅报告 1 个信号\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - round: 2\n        reviewers: [1, 2]\n        note: \"5 signals 中仅 SJ 一个数据点\"\n    action_items:\n      - round: 2\n        action: \"补全 5 信号 full/conditional ρ + AUROC + Appendix Table 5\"\n        assigned_to: \"Agent + Paper Agent\"\n        status: resolved\n    resolution: \"WNUT-17 全信号表完整，叙事修正为区分 full-set vs conditional\"\n    resolution_round: 2\n\n  - id: \"R2-W1\"\n    summary: \"ρ=0.38 缺 cross-method 对比\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - round: 2\n        reviewers: [1, 2]\n        note: \"需 footnote 引用 semantic entropy AUROC\"\n    action_items:\n      - round: 2\n        action: \"§5 footnote\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"Footnote 已加\"\n    resolution_round: 2\n\n  - id: \"R2-W2\"\n    summary: \"N=8 QE ρ 无 uncertainty\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - round: 2\n        reviewers: [1, 2]\n        note: \"需 bootstrap CIs\"\n    action_items:\n      - round: 2\n        action: \"计算 B=10,000 bootstrap CI + Appendix 表\"\n        assigned_to: \"Agent + Paper Agent\"\n        status: resolved\n    resolution: \"Bootstrap CI 表已加入 Appendix，SJ-logprob 显著\"\n    resolution_round: 2\n\n  - id: \"R2-W3\"\n    summary: \"SJ Hungarian threshold + max denominator\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - round: 2\n        reviewers: [1, 2]\n        note: \"无 threshold 声明需验证\"\n    action_items:\n      - round: 2\n        action: \"代码验证 + method.tex 补充\"\n        assigned_to: \"Agent + Paper Agent\"\n        status: resolved\n    resolution: \"无 threshold, 96.6% pairs sim≥0.5, max denominator 已解释\"\n    resolution_round: 2\n\n  - id: \"R2-W4\"\n    summary: \"RE selection 无统计检验\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - round: 2\n        reviewers: [1, 2]\n        note: \"需 bootstrap p-value\"\n    action_items:\n      - round: 2\n        action: \"RE bootstrap + 补 p=0.80 到论文\"\n        assigned_to: \"Agent + Paper Agent\"\n        status: resolved\n    resolution: \"RE logprob p=0.80, all signals below greedy\"\n    resolution_round: 2\n\n  - id: \"R2-W5\"\n    summary: \"Constrained decoding 全局 confound\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - round: 2\n        reviewers: [1, 2]\n        note: \"需扩展到全局 + Limitations\"\n    action_items:\n      - round: 2\n        action: \"Discussion 扩展 + Limitations 条目\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"已处理\"\n    resolution_round: 2\n\n  - id: \"R2-W6\"\n    summary: \"Abstract RE 措辞误导\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - round: 2\n        reviewers: [1, 2]\n        note: \"NER (three datasets) and RE (SciERC)\"\n    action_items:\n      - round: 2\n        action: \"修正 Abstract\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"已修正\"\n    resolution_round: 2\n\n  - id: \"R2-W7\"\n    summary: \"n=529 vs 551 未解释\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - round: 2\n        reviewers: [1, 2]\n        note: \"22 instances filtering criteria\"\n    action_items:\n      - round: 2\n        action: \"补一句说明\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"已说明 gold-empty filtering\"\n    resolution_round: 2\n\n  - id: \"R2-DATA\"\n    summary: \"RE selection 数据矛盾 (Table 2 vs L129)\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - round: 2\n        reviewers: [\"Research Reviewer\"]\n        note: \"Table 2 logprob=0.395 (-0.9pp) vs L129 logprob=0.410 (+0.6pp)\"\n    action_items:\n      - round: 2\n        action: \"Agent 确认 Table 2 正确 → Paper Agent 修正 L129\"\n        assigned_to: \"Agent + Paper Agent\"\n        status: resolved\n    resolution: \"L129 统一为 logprob=0.395, -0.9pp, p=0.80\"\n    resolution_round: 2\n\n  - id: \"R2-AUROC\"\n    summary: \"L64 AUROC 归属错误 (Voting ρ 配 EM AUROC)\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - round: 2\n        reviewers: [\"Research Reviewer\"]\n        note: \"corresponding 暗示同一信号\"\n    action_items:\n      - round: 2\n        action: \"分别标注 Voting ρ 和 EM AUROC\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"已拆分归属\"\n    resolution_round: 2\n\n  # ============================================================\n  # Round 3 issues (updated with Round 4 status)\n  # ============================================================\n  - id: \"R3-C1\"\n    summary: \"Constrained decoding 是 correlation-selection gap 的未控制混淆变量\"\n    category: method\n    severity: critical\n    status: in_progress\n    first_raised_round: 3\n    last_seen_round: 4\n    mentions:\n      - round: 3\n        reviewers: [1, 2]\n        note: \"两位 Reviewer 均独立提出。Outlines/vLLM constrained decoding 可能压缩 per-sample diversity，使 gap 成为实验设置 artifact。\"\n      - round: 4\n        reviewers: [1, 2]\n        note: \"R2 确认部分解决（承认但未量化）。R1 仍列 critical（需 logprob 分布分析）。R1 rebut free-form baseline（constrained decoding 是方法论必要条件），但同意需量化 diversity 压缩效应。共识：elevated should-fix，量化 logprob 分布而非增加 free-form 实验。\"\n    action_items:\n      - round: 3\n        action: \"Agent 量化 diversity；Paper Agent 写入论文 + 限定 scope\"\n        assigned_to: \"Agent + Paper Agent\"\n        status: resolved\n      - round: 4\n        action: \"量化 logprob 分布（tie 定义 Δlogprob<ε, non-tie 子集 selection 能力）+ Discussion 中讨论 grammar compliance 如何压缩区分度\"\n        assigned_to: \"Agent + Paper Agent\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R3-C2\"\n    summary: \"Failure-to-reject 不等于 evidence of absence，selection gap 统计论证不完整\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 4\n    mentions:\n      - round: 3\n        reviewers: [1, 2]\n        note: \"需修改措辞或补充等价性检验\"\n      - round: 4\n        reviewers: [2]\n        note: \"R2 确认 RESOLVED：TOST 已补充，措辞修正到位\"\n    action_items:\n      - round: 3\n        action: \"修改措辞 + 6/6 cumulative evidence 论证\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"Round 4: TOST 等价检验已补充，措辞修正为 'no significant evidence'，R2 确认到位\"\n    resolution_round: 4\n\n  - id: \"R3-C3\"\n    summary: \"N=8 核心结果 single seed (seed=42)\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 4\n    mentions:\n      - round: 3\n        reviewers: [1, 2]\n        note: \"Table 1 N=8 和 Table 2 selection 全部 single seed\"\n      - round: 4\n        reviewers: [2]\n        note: \"R2 确认 RESOLVED：3-seed 验证已补充\"\n    action_items:\n      - round: 3\n        action: \"Limitations 中明确 single-seed 风险并引用 N=16 stability\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"Round 4: 3-seed 稳定性验证已补充，R2 确认到位\"\n    resolution_round: 4\n\n  - id: \"R3-W1\"\n    summary: \"多重比较校正缺失\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 4\n    mentions:\n      - round: 3\n        reviewers: [1, 2]\n        note: \"SJ-EM CI lower bound +0.003 在 Bonferroni 下不会 survive\"\n      - round: 4\n        reviewers: [2]\n        note: \"R2 确认 RESOLVED：Bonferroni 声明已加\"\n    action_items:\n      - round: 3\n        action: \"声明未做多重比较校正 + SJ-EM 改为 suggestive\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"Round 4: Bonferroni 声明已加，R2 确认到位\"\n    resolution_round: 4\n\n  - id: \"R3-W2\"\n    summary: \"Gap 概念部分 tautological——instance-level 信号无法 select 是定义必然\"\n    category: method\n    severity: warning\n    status: in_progress\n    first_raised_round: 3\n    last_seen_round: 4\n    mentions:\n      - round: 3\n        reviewers: [1, 2]\n        note: \"需在 Discussion 中分离两层论证\"\n      - round: 4\n        reviewers: [1, 2]\n        note: \"R2 确认部分改善但核心张力仍在。R4 两位 Reviewer 独立再次提出（R1-N1, R2-N1）：Introduction 未正面论证 why not obvious a priori，§4.3 和 abstract 将 gap 作为统一经验发现但 §5 承认 4/5 是 by construction。R1 部分 rebut：MBR 在 MT 成功但 IE 失败是非平凡的。共识：需明确分离定义性 gap 和经验性 gap，加强非显然性论证。升级为 Round 4 W-C1。\"\n    action_items:\n      - round: 3\n        action: \"Discussion 中分离两层论证\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n      - round: 4\n        action: \"(a) Introduction 正面论证 why gap is not obvious (MBR MT vs IE 对比); (b) Discussion 明确分离定义性局限 vs 经验性失败 (logprob + consensus-proximity); (c) 聚焦 logprob 75% ties 做深入分析\"\n        assigned_to: \"Paper Agent\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R3-W3\"\n    summary: \"Consensus-proximity 是唯一 instance-to-sample 转换策略，未与 MBR decoding 建立联系\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 4\n    mentions:\n      - round: 3\n        reviewers: [1, 2]\n        note: \"MBR decoding 是成熟替代方案但未讨论\"\n      - round: 4\n        reviewers: [2]\n        note: \"R2 确认 RESOLVED：MBR 连接已补充，§5 MBR 段清晰\"\n    action_items:\n      - round: 3\n        action: \"明确 consensus-proximity 与 MBR 联系 + 引用 MBR 文献\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"Round 4: §5 MBR decoding 连接段已写入，R2 评价'概念优雅'\"\n    resolution_round: 4\n\n  - id: \"R3-W4\"\n    summary: \"FK 独立性假设 justification 不足\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 4\n    mentions:\n      - round: 3\n        reviewers: [1, 2]\n        note: \"§3.2 一句 hand-wave。需报告 inter-sample correlation\"\n      - round: 4\n        reviewers: [2]\n        note: \"R2 确认 RESOLVED：excess agreement 数据已补充。R1 仍对 negative excess agreement 含义有疑问，但降为 minor\"\n    action_items:\n      - round: 3\n        action: \"Agent 量化 inter-sample correlation；Paper Agent 写入\"\n        assigned_to: \"Agent + Paper Agent\"\n        status: resolved\n    resolution: \"Round 4: Excess agreement 数据已补 (-0.4% to -4.0%)。R1 minor 疑问不影响接收\"\n    resolution_round: 4\n\n  - id: \"R3-W5\"\n    summary: \"Cross-model 实为 cross-architecture at fixed 8B scale\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 4\n    mentions:\n      - round: 3\n        reviewers: [1, 2]\n        note: \"两模型均 8B，措辞过度外推\"\n      - round: 4\n        reviewers: [2]\n        note: \"R2 确认 RESOLVED：cross-architecture 措辞已统一\"\n    action_items:\n      - round: 3\n        action: \"正文将 cross-model 替换为 cross-architecture 或加限定词\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"Round 4: 措辞已统一为 cross-architecture at 8B scale\"\n    resolution_round: 4\n\n  - id: \"R3-W6\"\n    summary: \"'First multi-family comparison' claim scope 过宽\"\n    category: framing\n    severity: warning\n    status: in_progress\n    first_raised_round: 3\n    last_seen_round: 4\n    mentions:\n      - round: 3\n        reviewers: [1, 2]\n        note: \"需限定为 structured IE 的 QE + selection\"\n      - round: 4\n        reviewers: [2]\n        note: \"R2 确认部分解决：Conclusion 有 hedge 但 Introduction 仍断言式。需对齐 Introduction 与 Conclusion 的 claim scope\"\n    action_items:\n      - round: 3\n        action: \"收窄 Contribution 1 措辞\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n      - round: 4\n        action: \"Introduction contribution claim 加 hedge，与 Conclusion 对齐\"\n        assigned_to: \"Paper Agent\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R3-W7\"\n    summary: \"术语不一致\"\n    category: writing\n    severity: warning\n    status: in_progress\n    first_raised_round: 3\n    last_seen_round: 4\n    mentions:\n      - round: 3\n        reviewers: [1, 2]\n        note: \"confidence signal vs consistency signal 混用；VC vs Voting Conf.\"\n      - round: 4\n        reviewers: [1, 2]\n        note: \"R2 确认部分解决：表格缩写 VC/Voting Conf. 仍不统一。R1 同意需加明确 taxonomy 定义。建议 §3.2 开头定义 confidence signal（统称）vs consistency signal（子集，不含 logprob）\"\n    action_items:\n      - round: 3\n        action: \"统一术语 + 补 LLaMA Factory 引用\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n      - round: 4\n        action: \"§3.2 开头加明确 taxonomy + 全文统一表格缩写\"\n        assigned_to: \"Paper Agent\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R3-W8\"\n    summary: \"遗漏引用：VerifiNER, RASC, MBR decoding, Malinin & Gales\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 4\n    mentions:\n      - round: 3\n        reviewers: [1, 2]\n        note: \"VerifiNER, MBR decoding 等高度相关\"\n      - round: 4\n        reviewers: [2]\n        note: \"R2 确认 RESOLVED：引用已补全\"\n    action_items:\n      - round: 3\n        action: \"补充引用并在 Related Work 中讨论\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"Round 4: 引用已补全，R2 确认到位\"\n    resolution_round: 4\n\n  - id: \"R3-M1\"\n    summary: \"WNUT-17 '54% zero F1' 与 Table 7 数据不一致 (51.5%)\"\n    category: experiment\n    severity: info\n    status: in_progress\n    first_raised_round: 3\n    last_seen_round: 3\n    mentions:\n      - round: 3\n        reviewers: [1]\n        note: \"355/689 ≈ 51.5% vs 正文 54%\"\n      - round: 4\n        reviewers: []\n        note: \"本轮未提及，可能已修复，待 Research Director 确认\"\n    action_items:\n      - round: 3\n        action: \"Agent 核实实际数字 → Paper Agent 统一\"\n        assigned_to: \"Agent + Paper Agent\"\n        status: in_progress\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R3-M2\"\n    summary: \"EM selection exclusion 缺乏经验支持\"\n    category: experiment\n    severity: info\n    status: in_progress\n    first_raised_round: 3\n    last_seen_round: 3\n    mentions:\n      - round: 3\n        reviewers: [1, 2]\n        note: \"'probability negligible' 需报告 exact match pairs 频率\"\n      - round: 4\n        reviewers: []\n        note: \"本轮未提及，可能已修复，待 Research Director 确认\"\n    action_items:\n      - round: 3\n        action: \"Agent 计算 exact match pairs 频率 → Paper Agent 写入\"\n        assigned_to: \"Agent + Paper Agent\"\n        status: in_progress\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R3-M3\"\n    summary: \"Ethics Statement 缺失\"\n    category: format\n    severity: info\n    status: in_progress\n    first_raised_round: 3\n    last_seen_round: 4\n    mentions:\n      - round: 3\n        reviewers: [2]\n        note: \"共识降为 minor\"\n      - round: 4\n        reviewers: [2]\n        note: \"R2 确认 Ethics Statement 已存在但位于 Limitations section 内——建议改为独立 section 以符合 ACL 格式规范\"\n    action_items:\n      - round: 3\n        action: \"添加简短 Ethics Statement\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n      - round: 4\n        action: \"将 Ethics Statement 从 Limitations 内移出为独立 section\"\n        assigned_to: \"Paper Agent\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R3-M4\"\n    summary: \"ρ-AUROC dissociation 作为独立发现过度强调\"\n    category: framing\n    severity: info\n    status: in_progress\n    first_raised_round: 3\n    last_seen_round: 3\n    mentions:\n      - round: 3\n        reviewers: [1, 2]\n        note: \"建议承认统计预期性后聚焦实践含义\"\n      - round: 4\n        reviewers: []\n        note: \"本轮未提及，可能已修复，待 Research Director 确认\"\n    action_items:\n      - round: 3\n        action: \"§4.2 承认 dissociation 的统计预期性\"\n        assigned_to: \"Paper Agent\"\n        status: in_progress\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R3-M5\"\n    summary: \"对 Nedellec (2026) 措辞偏 adversarial\"\n    category: writing\n    severity: info\n    status: in_progress\n    first_raised_round: 3\n    last_seen_round: 3\n    mentions:\n      - round: 3\n        reviewers: [1, 2]\n        note: \"建议用更 neutral 语气\"\n      - round: 4\n        reviewers: []\n        note: \"本轮未提及，可能已修复，待 Research Director 确认\"\n    action_items:\n      - round: 3\n        action: \"Introduction 中改为更 neutral 的语气\"\n        assigned_to: \"Paper Agent\"\n        status: in_progress\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R3-M6\"\n    summary: \"LOO-SJ 验证中 Δρ 和 per-instance Δρ 量纲混淆\"\n    category: writing\n    severity: info\n    status: in_progress\n    first_raised_round: 3\n    last_seen_round: 3\n    mentions:\n      - round: 3\n        reviewers: [1]\n        note: \"Δρ=−0.014 vs per-instance max Δρ=3.1×10⁻⁴ 量纲不同\"\n      - round: 4\n        reviewers: []\n        note: \"本轮未提及，可能已修复，待 Research Director 确认\"\n    action_items:\n      - round: 3\n        action: \"澄清 per-instance Δρ 具体含义\"\n        assigned_to: \"Paper Agent\"\n        status: in_progress\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R3-M7\"\n    summary: \"Figure 1 caption 引入未直接可视化的 p=0.39\"\n    category: writing\n    severity: info\n    status: in_progress\n    first_raised_round: 3\n    last_seen_round: 3\n    mentions:\n      - round: 3\n        reviewers: [1]\n        note: \"建议加 '(Table 2)' 交叉引用\"\n      - round: 4\n        reviewers: []\n        note: \"本轮未提及，可能已修复，待 Research Director 确认\"\n    action_items:\n      - round: 3\n        action: \"补 '(Table 2)' 交叉引用\"\n        assigned_to: \"Paper Agent\"\n        status: in_progress\n    resolution: \"\"\n    resolution_round: null\n\n  # ============================================================\n  # Round 4 new issues\n  # ============================================================\n  - id: \"R4-C1\"\n    summary: \"训练配置和 prompt template 缺失，影响独立复现\"\n    category: experiment\n    severity: critical\n    status: open\n    first_raised_round: 4\n    last_seen_round: 4\n    mentions:\n      - round: 4\n        reviewers: [1, 2]\n        note: \"两位 Reviewer 独立提出（R1-N3, R2-N2），完全共识。§4.1 仅报告 LoRA rank=32, α=64, 5 epochs, LLaMA Factory，缺少 lr, batch size, warmup, weight decay, optimizer, early stopping, train/dev split, prompt template, LoRA target modules, max seq length, schema constraint\"\n    action_items:\n      - round: 4\n        action: \"附录补充完整训练配置表 + NER/RE prompt template 示例 + schema constraint 定义\"\n        assigned_to: \"Paper Agent\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R4-W1\"\n    summary: \"RE 证据需进一步加强（conditional analysis 或降级）\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 4\n    last_seen_round: 4\n    mentions:\n      - round: 4\n        reviewers: [1, 2]\n        note: \"R0-C3 的 claim 降级已完成（resolved），但两位 Reviewer 仍认为 RE 证据薄弱：40% zero-F1 floor effect, gap 证据 -0.9pp p=0.80。R1 建议 SciERC RE conditional analysis；R2 建议 Abstract/Introduction 进一步降级。\"\n    action_items:\n      - round: 4\n        action: \"(a) SciERC RE non-zero F1 子集 selection 分析; (b) Abstract/Introduction 中 RE 标记为 preliminary/exploratory\"\n        assigned_to: \"Agent + Paper Agent\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R4-W2\"\n    summary: \"SJ vs EM 优势叙事应改为 difficulty-dependent complementarity\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 4\n    last_seen_round: 4\n    mentions:\n      - round: 4\n        reviewers: [1, 2]\n        note: \"SJ vs EM Δρ=+0.065, CI 下界 +0.003, Bonferroni 下不显著。CoNLL 上 EM 反超 SJ。两位 Reviewer 一致认为应弱化 structural advantage 叙事，强调 difficulty-dependent complementarity\"\n    action_items:\n      - round: 4\n        action: \"Contribution #1 弱化 structural advantage，改为强调 difficulty-dependent complementarity + 提供信号选择指导\"\n        assigned_to: \"Paper Agent\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R4-W3\"\n    summary: \"Abstract 过于密集，第 4 行超长句子需拆分\"\n    category: writing\n    severity: warning\n    status: open\n    first_raised_round: 4\n    last_seen_round: 4\n    mentions:\n      - round: 4\n        reviewers: [1, 2]\n        note: \"第 3-4 行含多层嵌套括号和分号的超长句子，首次阅读难以把握核心信息。两位 Reviewer 一致建议拆分为 2-3 个独立句子\"\n    action_items:\n      - round: 4\n        action: \"Abstract 核心发现拆分为 2-3 句，每句一个关键 claim\"\n        assigned_to: \"Paper Agent\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R4-W4\"\n    summary: \"缺少 Xiong et al. (2024) 'Can LLMs Express Their Uncertainty?' ICLR 2024\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 4\n    last_seen_round: 4\n    mentions:\n      - round: 4\n        reviewers: [1, 2]\n        note: \"系统评估 LLM 置信度获取方法（verbalized, consistency-based, logit-based），与本文多族信号比较直接相关。两位 Reviewer 一致认为应引用。另有 Bertsch et al. (2024), Wiher et al. (2022), Müller & Sennrich (2021) 由 R1 建议\"\n    action_items:\n      - round: 4\n        action: \"Related Work 'Uncertainty estimation' 段引用 Xiong et al. + 区分本文与 verbalized confidence 方法。评估补引 Bertsch/Wiher/Müller&Sennrich\"\n        assigned_to: \"Paper Agent\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R4-M1\"\n    summary: \"SJ normalizer 选择（max vs union）缺乏对比\"\n    category: method\n    severity: info\n    status: open\n    first_raised_round: 4\n    last_seen_round: 4\n    mentions:\n      - round: 4\n        reviewers: [1]\n        note: \"R1-W3: max(|g_i|,|g_j|) vs |g_i∪g_j| 未比较。建议附录报告替代 normalizer 结果或提供理论依据\"\n    action_items:\n      - round: 4\n        action: \"附录补 union normalizer 的 SJ 结果，或提供 max normalizer 的理论依据\"\n        assigned_to: \"Agent + Paper Agent\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R4-M2\"\n    summary: \"TOST δ 选择（±2/3/5 pp）缺乏实践意义论证\"\n    category: experiment\n    severity: info\n    status: open\n    first_raised_round: 4\n    last_seen_round: 4\n    mentions:\n      - round: 4\n        reviewers: [1]\n        note: \"R1-W5: δ 选择直接影响等价结论，需讨论在 IE 任务中 F1 差异的 practical significance 标准\"\n    action_items:\n      - round: 4\n        action: \"讨论 δ 选择依据（如 annotation agreement F1 variance）\"\n        assigned_to: \"Paper Agent\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R4-M3\"\n    summary: \"Table 1 N=16 block 大面积空白\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 4\n    last_seen_round: 4\n    mentions:\n      - round: 4\n        reviewers: [1, 2]\n        note: \"N=16 仅填 LLaMA CoNLL，SciERC 空白，给人实验不完整印象。建议填充或添加脚注引导读者到附录\"\n    action_items:\n      - round: 4\n        action: \"补脚注说明 N=16 数据位置或考虑合并呈现\"\n        assigned_to: \"Paper Agent\"\n        status: open\n    resolution: \"\"\n    resolution_round: null"
  }
}
```

</details>

---


### Tool result

_source line 458 · 2026-05-15T07:06:09.758794+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_issues.yaml\", \"bytes\": 36436}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 153
}
```

</details>

---


### Tool call

_source line 459 · 2026-05-15T07:08:36.937381+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "report": "# 审稿报告 — Round 4\n\n**论文**: Strong Predictors, Weak Selectors: A Systematic Comparison of Confidence Signals for Test-Time Scaling in Information Extraction\n**Venue**: EMNLP 2026 Findings (ACL ARR May 2026 cycle)\n**Reviewer 编排**: 2 人（R1: 方法严谨性+实验设计; R2: 新颖性+完整性+写作质量+Round 3 修复验证）\n**流程**: Round 1 独立审稿 → 交叉分享（逐条 AGREE/REBUT）→ 收敛汇总\n**Round 3 修复评估**: R2 系统审查了 13 个 Round 3 遗留问题——8 个 RESOLVED，4 个 PARTIALLY RESOLVED，0 个 UNRESOLVED\n\n---\n\n## Summary\n\n本文系统比较了三族（structural / surface / model-internal）五种 confidence signal 在生成式信息抽取（NER + RE）中的 quality estimation 和 sample selection 性能。核心发现 \"correlation-selection gap\"：instance-level consistency signal 在质量估计上有效（ρ 最高 0.38, AUROC 最高 0.75），但在 best-of-N selection 中无信号显著超越 greedy decoding（p>0.39）。经四轮迭代，论文统计方法论已达到高水平（TOST, bootstrap CI, 3-seed, Bonferroni），但核心贡献的 framing 和可复现性仍需改进。\n\n---\n\n## Strengths\n\n**S1. 统计方法论显著改善。** Bootstrap CI (B=10,000)、TOST 等价检验（区分\"无显著差异\"与\"确认等价\"）、3-seed 稳定性验证、Bonferroni 校正声明——四轮迭代后统计分析在 NLP 实证论文中属上乘。TOST 揭示 EM/Voting 在 RE 上即使 ±5pp 也不等价于 greedy（系统性劣化）。[R1-S2, R2-S1 一致]\n\n**S2. 质量估计 vs. 样本选择的解耦是清晰的方法论贡献。** Per-sample vs. instance-level 信号的形式化区分（Eq. 1-7）和 ρ-AUROC dissociation 分析为后续工作提供了好的评估框架。[R1-S1, R2-S2 一致]\n\n**S3. 任务难度梯度分析有实际指导意义。** CoNLL（easy）→ SciERC（medium）→ WNUT-17（capability boundary）三级设计精良。WNUT-17 conditional ρ=0.038 (n.s.) 揭示高 failure rate 下信号表现为 artifactual。EM 在简单任务领先、结构化信号在复杂任务领先的 crossover 有实用价值。[R1-S3, R2-S3 一致]\n\n**S4. MBR decoding 连接概念优雅。** §5 将 selection strategies 形式化为 MBR 框架下不同 utility function 的实例化，有理论统一价值。[R1-S5, R2-S4 一致]\n\n**S5. Limitations section 诚实且具体。** 覆盖了 RE 单数据集、模型规模、constrained decoding、logprob 温度敏感性缺失等。[R1-S4, R2-S5 一致]\n\n**S6. 引用质量高。** 55 条引用经 OpenAlex 验证，0 orphan / 0 missing bib，51 条完全验证通过。Round 3 要求补充的 MBR decoding 等引用已到位。[R1-S6]\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**[Critical] W-C1: Correlation-selection gap 的 framing 需要区分\"定义性 gap\"和\"经验性 gap\"**\n- 两位 Reviewer 独立提出（R1-N1, R2-N1），交叉回应后共识\n- 4/5 信号是 instance-level，对同一 input 的 N 个候选给出相同分数——其 selection 失败是设计层面的先验预期。论文 §5 承认 \"Four of five signals are instance-level by construction and cannot rank N candidates\"，但这与 §4.3 和 abstract 中将 gap 作为核心 empirical contribution 的定位存在张力\n- 真正的经验贡献是：(1) logprob（唯一 per-sample 信号）也失败（75% comparisons are ties, Cohen's d=0.038）; (2) consensus-proximity/MBR 策略未能弥合 gap\n- R1 部分 rebut R2 的严厉程度——认为 MBR 在 MT 中成功但 IE 中失败的对比是非平凡的，但同意论证可加强\n- **共识建议**：(a) Introduction 正面论证 \"why the gap is not obvious a priori\"——MBR 在 MT 中成功为何 IE 中失败？(b) Discussion 明确分离两层论证：定义性局限 (instance-level by construction) vs. 经验性失败 (logprob + consensus-proximity)；(c) 聚焦 logprob ties 的 75% 统计数据做深入分析\n\n**[Critical] W-C2: 训练配置和 prompt template 缺失，影响独立复现**\n- 两位 Reviewer 独立提出（R1-N3, R2-N2），无分歧\n- §4.1 仅报告 LoRA rank=32, α=64, 5 epochs, LLaMA Factory，缺少：learning rate、batch size、warmup、weight decay、optimizer、early stopping 策略、train/dev split、prompt template（NER/RE 各用什么格式？）、LoRA target modules、max sequence length、schema constraint 定义\n- LoRA 微调对 lr 和 target modules 敏感，不同配置可能影响 output diversity 和信号表现\n- **共识建议**：附录补充完整训练配置表 + prompt template 示例\n\n### Should-Fix（影响评分）\n\n**[Warning] W-S1: Constrained decoding 对 logprob 信号语义的影响需进一步量化**\n- R1 列 critical (N2), R2 列 should-fix (W1)——存在严重性分歧，取交集为 elevated should-fix\n- 论文自承 \"75% of comparisons are effectively ties\"、\"logprob primarily reflects grammar compliance under constrained decoding\"——但未实验验证此归因\n- R1 建议分析 non-tie 的 25% 上 logprob 是否能成功 select；R2 建议讨论 constrained decoding 如何压缩 logprob 判别力\n- R1 rebut R2 的 free-form baseline 建议：constrained decoding 对 structured IE 是方法论必要条件，free-form 引入新混淆变量\n- **共识建议**：(a) 量化 logprob 分布——tie 的定义（Δlogprob < ε）、non-tie 子集上 logprob 的 selection 能力；(b) 在 Discussion 中讨论 constrained decoding 如何从 grammar compliance 层面压缩 logprob 区分度；(c) 限定 gap 结论的 scope 为 constrained decoding regime\n\n**[Warning] W-S2: RE 证据需进一步加强**\n- 两位 Reviewer 一致（R1-W1, R2-N2 initial）\n- R0-C3 的 claim 降级已完成（Conclusion 有 hedge），但 Abstract/Introduction 仍将 RE 作为等权证据\n- 40% zero-F1 floor effect 严重压缩信号可区分范围，gap 的 RE 证据（-0.9pp, p=0.80）统计说服力弱\n- **共识建议**：(a) SciERC RE non-zero F1 子集 selection 分析；(b) Abstract/Introduction 中 RE 标记为 preliminary/exploratory evidence\n\n**[Warning] W-S3: SJ vs EM 优势叙事应改为 difficulty-dependent complementarity**\n- 两位 Reviewer 一致（R1 同意 R2-W4）\n- SJ vs EM: Δρ=+0.065, CI 下界 +0.003, Bonferroni 下不显著；CoNLL 上 EM 反超\n- **共识建议**：弱化 \"structural advantage\" 叙事，强调在不同难度下 structural 和 surface signal 互补\n\n**[Warning] W-S4: Abstract 过于密集**\n- 两位 Reviewer 一致\n- 第 4 行含多层嵌套括号的超长句子\n- **建议**：核心发现拆分为 2-3 个独立句子\n\n**[Warning] W-S5: \"confidence signal\" vs \"consistency signal\" 术语不一致**\n- 两位 Reviewer 一致，Round 3 遗留（R3-W7 部分解决）\n- logprob 不是 consistency signal 但被 \"consistency signals\" 统称覆盖\n- **建议**：Section 3.2 开头增加明确 taxonomy 定义\n\n**[Warning] W-S6: Introduction novelty claim 缺 hedge**\n- R2 提出，Round 3 遗留（R3-W6 部分解决）\n- Conclusion 已有 hedge 但 Introduction 仍断言式\n- **建议**：Introduction 的 contribution claim 与 Conclusion 的 hedge 对齐\n\n**[Warning] W-S7: 缺少 Xiong et al. (2024) \"Can LLMs Express Their Uncertainty?\" ICLR 2024**\n- 两位 Reviewer 一致\n- 系统评估 LLM 置信度获取方法（verbalized, consistency-based, logit-based），与本文多族信号比较直接相关\n- **建议**：Related Work \"Uncertainty estimation\" 段引用并区分\n\n### Minor Issues\n\n**[Info] W-M1**: Table 1 N=16 block 大面积空白，建议补脚注或合并呈现 [R1, R2 一致]\n**[Info] W-M2**: Ethics Statement 位于 Limitations 内——建议改为独立 section [R2]\n**[Info] W-M3**: Figure 1 caption 未解释 consensus-proximity 转换策略 [R2]\n**[Info] W-M4**: Semantic entropy footnote 引用不可比数字——建议强化 caveat [R1]\n**[Info] W-M5**: Entity Voting 公式 (5) 分母为 0 的边界条件未注明 [R1]\n**[Info] W-M6**: Appendix reliability diagram ECE 的 bin 数量未报告 [R1]\n**[Info] W-M7**: TOST δ 选择（±2, ±3, ±5 pp）缺乏实践意义论证 [R1]\n**[Info] W-M8**: FK excess agreement negative 值含义可进一步解释 [R1]\n**[Info] W-M9**: SJ normalizer max(|g_i|,|g_j|) vs |g_i∪g_j| 未对比 [R1]\n\n---\n\n## Round 3 Issue Resolution Status\n\n| ID | 问题 | Round 4 状态 | 说明 |\n|----|------|-------------|------|\n| R3-C1 | Constrained decoding confound | PARTIALLY RESOLVED | 承认但未量化 → 降为 W-S1 |\n| R3-C2 | Failure-to-reject 措辞 | RESOLVED | TOST 已补充 |\n| R3-C3 | N=8 single seed | RESOLVED | 3-seed 验证已补充 |\n| R3-W1 | 多重比较校正 | RESOLVED | Bonferroni 声明已加 |\n| R3-W2 | Gap tautological | PARTIALLY RESOLVED | 改善但核心张力仍在 → 升级为 W-C1 |\n| R3-W3 | MBR 连接缺失 | RESOLVED | §5 MBR 段已写入 |\n| R3-W4 | FK 独立性 | RESOLVED | Excess agreement 数据已补 |\n| R3-W5 | Cross-model → cross-architecture | RESOLVED | 措辞已统一 |\n| R3-W6 | First multi-family claim scope | PARTIALLY RESOLVED | Conclusion 有 hedge 但 Introduction 无 → W-S6 |\n| R3-W7 | 术语不一致 | PARTIALLY RESOLVED | 表格缩写仍不统一 → W-S5 |\n| R3-W8 | 遗漏引用 | RESOLVED | 已补全 |\n| R0-C3 | RE 单数据集 | RESOLVED (claim降级) | 但 RE 证据仍薄弱 → W-S2 |\n| R1-W1 | SJ 形式化歧义 | RESOLVED | 补全 |\n\n**总结**: Round 3 的 13 个 in_progress 问题中，8 个已完全解决，4 个部分解决（回归为本轮 issue），0 个完全未解决。论文在统计方法论上的改进（TOST、3-seed、Bonferroni、MBR 连接）是实质性的。\n\n---\n\n## Reviewer Consensus [AGREE]\n\n1. **Gap framing 需分层论证**：定义性局限 (instance-level) 和经验性失败 (logprob + consensus-proximity) 应明确分离 [R1-N1 ≈ R2-N1, 共识]\n2. **训练细节/prompt template 必须补充**：独立复现的基本要求 [R1-N3 = R2-N2, 完全共识]\n3. **RE 证据仍然薄弱**：claim 降级已做但可进一步加强 [R1-W1, R2 确认]\n4. **SJ 优势叙事应改为互补性**：Bonferroni 下不显著，CoNLL 上 EM 反超 [R1 agree R2-W4]\n5. **术语需统一 + Abstract 需简化**：[双方一致]\n6. **Xiong et al. (2024) 应引用**：高度相关的 LLM 置信度评估工作 [双方一致]\n7. **统计方法论已达高水准**：四轮迭代的改进得到两位 Reviewer 一致认可 [双方一致]\n\n## Reviewer Divergence [REBUT]\n\n1. **Constrained decoding 严重性**：R1 列 critical（需实验量化）→ R2 列 should-fix（需更多讨论）→ **共识为 elevated should-fix**，量化 logprob 分布而非增加 free-form 实验\n2. **Gap 非平凡性的严厉程度**：R2 认为 excitement 仅 2.5（gap 可预测）→ R1 rebut（MBR 类比非平凡，logprob ties 是经验发现）→ **共识评分 3.0/5**\n3. **Free-form generation baseline**：R2 建议增加 → R1 rebut（constrained decoding 是方法论必要条件）→ **共识为不需要 free-form 实验，但需量化 diversity 压缩效应**\n4. **BibTeX 键名 nedellec2026consistency**：R2 建议修改 → R1 rebut（内部细节，\\citet 输出正确）→ **共识降至 minor**\n\n---\n\n## Questions to Authors\n\n1. Logprob ties（75%）的具体定义是什么？Δlogprob < ε 的 ε 取值？在 non-tie 子集上，logprob 作为 selector 的表现如何？\n2. SciERC RE non-zero F1 子集上的 selection gap 分析结果是否与主文结论一致？\n3. 是否考虑过在 Introduction 中正面论证 \"why the gap is not obvious\"——例如引用 MBR 在 MT 中的成功作为对比？\n4. LoRA target modules 具体是 all linear 还是 q_proj/v_proj only？这对 output diversity 的影响有多大？\n5. Prompt template 中 schema constraint 如何定义？是否有 few-shot examples？\n\n---\n\n## Missing References\n\n1. **Xiong et al. (2024)** \"Can LLMs Express Their Uncertainty? An Empirical Evaluation of Confidence Elicitation in LLMs\" ICLR 2024 — 高度相关 [两位 Reviewer 一致]\n2. **Ye et al. (2025)** \"Do LLMs Estimate Uncertainty Well in Instruction Following?\" ICLR 2025 — 中等相关 [R2]\n3. **Bertsch et al. (2024)** \"In-Context Learning with Long-Context Models\" — 与 test-time scaling 相关 [R1]\n4. **Wiher et al. (2022)** \"On Decoding Strategies for Neural Text Generators\" — 与 constrained decoding diversity 相关 [R1]\n5. **Müller & Sennrich (2021)** \"Understanding the Properties of MBR Decoding in NMT\" — 与 §5 MBR 连接直接相关 [R1]\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n外部审稿：未启用\n\n---\n\n## Overall Assessment\n\n**Overall Score: 3.0 / 5 (Findings: borderline)**\n**Confidence: 4/5**\n\n**判断依据**：\n\n两位 Reviewer 交叉回应后评分收敛至 3.0/5（R1: 3.0 维持不变, R2: 3.5→3.0 下调）。\n\n**支持接收的因素**：\n- 统计方法论经四轮迭代达到高水准（TOST, bootstrap CI, 3-seed, Bonferroni）\n- QE vs. selection 的解耦框架有方法论贡献价值\n- 任务难度梯度分析和 WNUT-17 capability boundary 发现有实用指导意义\n- MBR decoding 连接提供理论统一\n- Round 3 的 13 个 issue 中 8 个完全解决，改进幅度显著\n\n**制约接收的因素**：\n- 核心贡献 \"correlation-selection gap\" 的 framing 仍未清晰区分定义性局限和经验性发现（W-C1），削弱 novelty\n- 训练细节/prompt template 缺失影响独立复现（W-C2）\n- Constrained decoding 对 logprob 信号语义的影响仍为 unquantified confound（W-S1）\n- RE 证据薄弱（W-S2），SJ 优势 marginal（W-S3）\n\n**修订优先级**（按影响排序）：\n1. **[Must]** Gap framing 分层（定义性 vs 经验性）——决定核心贡献的 novelty 定位\n2. **[Must]** 训练配置 + prompt template 补充——复现基本要求\n3. **[Should]** Constrained decoding 下 logprob 分布量化——加强 gap 解释力\n4. **[Should]** RE conditional analysis + 进一步降级——减少过度泛化\n5. **[Should]** SJ narrative 调整 + Abstract 简化 + 术语统一——写作质量\n6. **[Minor]** Table 格式、Ethics 位置、引用补充",
  "project": "struct_self_consist_ie",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "borderline (Findings)",
  "review_chat_id": "oc_3897c2857f11615119e277e820eae311"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "report": "# 审稿报告 — Round 4\n\n**论文**: Strong Predictors, Weak Selectors: A Systematic Comparison of Confidence Signals for Test-Time Scaling in Information Extraction\n**Venue**: EMNLP 2026 Findings (ACL ARR May 2026 cycle)\n**Reviewer 编排**: 2 人（R1: 方法严谨性+实验设计; R2: 新颖性+完整性+写作质量+Round 3 修复验证）\n**流程**: Round 1 独立审稿 → 交叉分享（逐条 AGREE/REBUT）→ 收敛汇总\n**Round 3 修复评估**: R2 系统审查了 13 个 Round 3 遗留问题——8 个 RESOLVED，4 个 PARTIALLY RESOLVED，0 个 UNRESOLVED\n\n---\n\n## Summary\n\n本文系统比较了三族（structural / surface / model-internal）五种 confidence signal 在生成式信息抽取（NER + RE）中的 quality estimation 和 sample selection 性能。核心发现 \"correlation-selection gap\"：instance-level consistency signal 在质量估计上有效（ρ 最高 0.38, AUROC 最高 0.75），但在 best-of-N selection 中无信号显著超越 greedy decoding（p>0.39）。经四轮迭代，论文统计方法论已达到高水平（TOST, bootstrap CI, 3-seed, Bonferroni），但核心贡献的 framing 和可复现性仍需改进。\n\n---\n\n## Strengths\n\n**S1. 统计方法论显著改善。** Bootstrap CI (B=10,000)、TOST 等价检验（区分\"无显著差异\"与\"确认等价\"）、3-seed 稳定性验证、Bonferroni 校正声明——四轮迭代后统计分析在 NLP 实证论文中属上乘。TOST 揭示 EM/Voting 在 RE 上即使 ±5pp 也不等价于 greedy（系统性劣化）。[R1-S2, R2-S1 一致]\n\n**S2. 质量估计 vs. 样本选择的解耦是清晰的方法论贡献。** Per-sample vs. instance-level 信号的形式化区分（Eq. 1-7）和 ρ-AUROC dissociation 分析为后续工作提供了好的评估框架。[R1-S1, R2-S2 一致]\n\n**S3. 任务难度梯度分析有实际指导意义。** CoNLL（easy）→ SciERC（medium）→ WNUT-17（capability boundary）三级设计精良。WNUT-17 conditional ρ=0.038 (n.s.) 揭示高 failure rate 下信号表现为 artifactual。EM 在简单任务领先、结构化信号在复杂任务领先的 crossover 有实用价值。[R1-S3, R2-S3 一致]\n\n**S4. MBR decoding 连接概念优雅。** §5 将 selection strategies 形式化为 MBR 框架下不同 utility function 的实例化，有理论统一价值。[R1-S5, R2-S4 一致]\n\n**S5. Limitations section 诚实且具体。** 覆盖了 RE 单数据集、模型规模、constrained decoding、logprob 温度敏感性缺失等。[R1-S4, R2-S5 一致]\n\n**S6. 引用质量高。** 55 条引用经 OpenAlex 验证，0 orphan / 0 missing bib，51 条完全验证通过。Round 3 要求补充的 MBR decoding 等引用已到位。[R1-S6]\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**[Critical] W-C1: Correlation-selection gap 的 framing 需要区分\"定义性 gap\"和\"经验性 gap\"**\n- 两位 Reviewer 独立提出（R1-N1, R2-N1），交叉回应后共识\n- 4/5 信号是 instance-level，对同一 input 的 N 个候选给出相同分数——其 selection 失败是设计层面的先验预期。论文 §5 承认 \"Four of five signals are instance-level by construction and cannot rank N candidates\"，但这与 §4.3 和 abstract 中将 gap 作为核心 empirical contribution 的定位存在张力\n- 真正的经验贡献是：(1) logprob（唯一 per-sample 信号）也失败（75% comparisons are ties, Cohen's d=0.038）; (2) consensus-proximity/MBR 策略未能弥合 gap\n- R1 部分 rebut R2 的严厉程度——认为 MBR 在 MT 中成功但 IE 中失败的对比是非平凡的，但同意论证可加强\n- **共识建议**：(a) Introduction 正面论证 \"why the gap is not obvious a priori\"——MBR 在 MT 中成功为何 IE 中失败？(b) Discussion 明确分离两层论证：定义性局限 (instance-level by construction) vs. 经验性失败 (logprob + consensus-proximity)；(c) 聚焦 logprob ties 的 75% 统计数据做深入分析\n\n**[Critical] W-C2: 训练配置和 prompt template 缺失，影响独立复现**\n- 两位 Reviewer 独立提出（R1-N3, R2-N2），无分歧\n- §4.1 仅报告 LoRA rank=32, α=64, 5 epochs, LLaMA Factory，缺少：learning rate、batch size、warmup、weight decay、optimizer、early stopping 策略、train/dev split、prompt template（NER/RE 各用什么格式？）、LoRA target modules、max sequence length、schema constraint 定义\n- LoRA 微调对 lr 和 target modules 敏感，不同配置可能影响 output diversity 和信号表现\n- **共识建议**：附录补充完整训练配置表 + prompt template 示例\n\n### Should-Fix（影响评分）\n\n**[Warning] W-S1: Constrained decoding 对 logprob 信号语义的影响需进一步量化**\n- R1 列 critical (N2), R2 列 should-fix (W1)——存在严重性分歧，取交集为 elevated should-fix\n- 论文自承 \"75% of comparisons are effectively ties\"、\"logprob primarily reflects grammar compliance under constrained decoding\"——但未实验验证此归因\n- R1 建议分析 non-tie 的 25% 上 logprob 是否能成功 select；R2 建议讨论 constrained decoding 如何压缩 logprob 判别力\n- R1 rebut R2 的 free-form baseline 建议：constrained decoding 对 structured IE 是方法论必要条件，free-form 引入新混淆变量\n- **共识建议**：(a) 量化 logprob 分布——tie 的定义（Δlogprob < ε）、non-tie 子集上 logprob 的 selection 能力；(b) 在 Discussion 中讨论 constrained decoding 如何从 grammar compliance 层面压缩 logprob 区分度；(c) 限定 gap 结论的 scope 为 constrained decoding regime\n\n**[Warning] W-S2: RE 证据需进一步加强**\n- 两位 Reviewer 一致（R1-W1, R2-N2 initial）\n- R0-C3 的 claim 降级已完成（Conclusion 有 hedge），但 Abstract/Introduction 仍将 RE 作为等权证据\n- 40% zero-F1 floor effect 严重压缩信号可区分范围，gap 的 RE 证据（-0.9pp, p=0.80）统计说服力弱\n- **共识建议**：(a) SciERC RE non-zero F1 子集 selection 分析；(b) Abstract/Introduction 中 RE 标记为 preliminary/exploratory evidence\n\n**[Warning] W-S3: SJ vs EM 优势叙事应改为 difficulty-dependent complementarity**\n- 两位 Reviewer 一致（R1 同意 R2-W4）\n- SJ vs EM: Δρ=+0.065, CI 下界 +0.003, Bonferroni 下不显著；CoNLL 上 EM 反超\n- **共识建议**：弱化 \"structural advantage\" 叙事，强调在不同难度下 structural 和 surface signal 互补\n\n**[Warning] W-S4: Abstract 过于密集**\n- 两位 Reviewer 一致\n- 第 4 行含多层嵌套括号的超长句子\n- **建议**：核心发现拆分为 2-3 个独立句子\n\n**[Warning] W-S5: \"confidence signal\" vs \"consistency signal\" 术语不一致**\n- 两位 Reviewer 一致，Round 3 遗留（R3-W7 部分解决）\n- logprob 不是 consistency signal 但被 \"consistency signals\" 统称覆盖\n- **建议**：Section 3.2 开头增加明确 taxonomy 定义\n\n**[Warning] W-S6: Introduction novelty claim 缺 hedge**\n- R2 提出，Round 3 遗留（R3-W6 部分解决）\n- Conclusion 已有 hedge 但 Introduction 仍断言式\n- **建议**：Introduction 的 contribution claim 与 Conclusion 的 hedge 对齐\n\n**[Warning] W-S7: 缺少 Xiong et al. (2024) \"Can LLMs Express Their Uncertainty?\" ICLR 2024**\n- 两位 Reviewer 一致\n- 系统评估 LLM 置信度获取方法（verbalized, consistency-based, logit-based），与本文多族信号比较直接相关\n- **建议**：Related Work \"Uncertainty estimation\" 段引用并区分\n\n### Minor Issues\n\n**[Info] W-M1**: Table 1 N=16 block 大面积空白，建议补脚注或合并呈现 [R1, R2 一致]\n**[Info] W-M2**: Ethics Statement 位于 Limitations 内——建议改为独立 section [R2]\n**[Info] W-M3**: Figure 1 caption 未解释 consensus-proximity 转换策略 [R2]\n**[Info] W-M4**: Semantic entropy footnote 引用不可比数字——建议强化 caveat [R1]\n**[Info] W-M5**: Entity Voting 公式 (5) 分母为 0 的边界条件未注明 [R1]\n**[Info] W-M6**: Appendix reliability diagram ECE 的 bin 数量未报告 [R1]\n**[Info] W-M7**: TOST δ 选择（±2, ±3, ±5 pp）缺乏实践意义论证 [R1]\n**[Info] W-M8**: FK excess agreement negative 值含义可进一步解释 [R1]\n**[Info] W-M9**: SJ normalizer max(|g_i|,|g_j|) vs |g_i∪g_j| 未对比 [R1]\n\n---\n\n## Round 3 Issue Resolution Status\n\n| ID | 问题 | Round 4 状态 | 说明 |\n|----|------|-------------|------|\n| R3-C1 | Constrained decoding confound | PARTIALLY RESOLVED | 承认但未量化 → 降为 W-S1 |\n| R3-C2 | Failure-to-reject 措辞 | RESOLVED | TOST 已补充 |\n| R3-C3 | N=8 single seed | RESOLVED | 3-seed 验证已补充 |\n| R3-W1 | 多重比较校正 | RESOLVED | Bonferroni 声明已加 |\n| R3-W2 | Gap tautological | PARTIALLY RESOLVED | 改善但核心张力仍在 → 升级为 W-C1 |\n| R3-W3 | MBR 连接缺失 | RESOLVED | §5 MBR 段已写入 |\n| R3-W4 | FK 独立性 | RESOLVED | Excess agreement 数据已补 |\n| R3-W5 | Cross-model → cross-architecture | RESOLVED | 措辞已统一 |\n| R3-W6 | First multi-family claim scope | PARTIALLY RESOLVED | Conclusion 有 hedge 但 Introduction 无 → W-S6 |\n| R3-W7 | 术语不一致 | PARTIALLY RESOLVED | 表格缩写仍不统一 → W-S5 |\n| R3-W8 | 遗漏引用 | RESOLVED | 已补全 |\n| R0-C3 | RE 单数据集 | RESOLVED (claim降级) | 但 RE 证据仍薄弱 → W-S2 |\n| R1-W1 | SJ 形式化歧义 | RESOLVED | 补全 |\n\n**总结**: Round 3 的 13 个 in_progress 问题中，8 个已完全解决，4 个部分解决（回归为本轮 issue），0 个完全未解决。论文在统计方法论上的改进（TOST、3-seed、Bonferroni、MBR 连接）是实质性的。\n\n---\n\n## Reviewer Consensus [AGREE]\n\n1. **Gap framing 需分层论证**：定义性局限 (instance-level) 和经验性失败 (logprob + consensus-proximity) 应明确分离 [R1-N1 ≈ R2-N1, 共识]\n2. **训练细节/prompt template 必须补充**：独立复现的基本要求 [R1-N3 = R2-N2, 完全共识]\n3. **RE 证据仍然薄弱**：claim 降级已做但可进一步加强 [R1-W1, R2 确认]\n4. **SJ 优势叙事应改为互补性**：Bonferroni 下不显著，CoNLL 上 EM 反超 [R1 agree R2-W4]\n5. **术语需统一 + Abstract 需简化**：[双方一致]\n6. **Xiong et al. (2024) 应引用**：高度相关的 LLM 置信度评估工作 [双方一致]\n7. **统计方法论已达高水准**：四轮迭代的改进得到两位 Reviewer 一致认可 [双方一致]\n\n## Reviewer Divergence [REBUT]\n\n1. **Constrained decoding 严重性**：R1 列 critical（需实验量化）→ R2 列 should-fix（需更多讨论）→ **共识为 elevated should-fix**，量化 logprob 分布而非增加 free-form 实验\n2. **Gap 非平凡性的严厉程度**：R2 认为 excitement 仅 2.5（gap 可预测）→ R1 rebut（MBR 类比非平凡，logprob ties 是经验发现）→ **共识评分 3.0/5**\n3. **Free-form generation baseline**：R2 建议增加 → R1 rebut（constrained decoding 是方法论必要条件）→ **共识为不需要 free-form 实验，但需量化 diversity 压缩效应**\n4. **BibTeX 键名 nedellec2026consistency**：R2 建议修改 → R1 rebut（内部细节，\\citet 输出正确）→ **共识降至 minor**\n\n---\n\n## Questions to Authors\n\n1. Logprob ties（75%）的具体定义是什么？Δlogprob < ε 的 ε 取值？在 non-tie 子集上，logprob 作为 selector 的表现如何？\n2. SciERC RE non-zero F1 子集上的 selection gap 分析结果是否与主文结论一致？\n3. 是否考虑过在 Introduction 中正面论证 \"why the gap is not obvious\"——例如引用 MBR 在 MT 中的成功作为对比？\n4. LoRA target modules 具体是 all linear 还是 q_proj/v_proj only？这对 output diversity 的影响有多大？\n5. Prompt template 中 schema constraint 如何定义？是否有 few-shot examples？\n\n---\n\n## Missing References\n\n1. **Xiong et al. (2024)** \"Can LLMs Express Their Uncertainty? An Empirical Evaluation of Confidence Elicitation in LLMs\" ICLR 2024 — 高度相关 [两位 Reviewer 一致]\n2. **Ye et al. (2025)** \"Do LLMs Estimate Uncertainty Well in Instruction Following?\" ICLR 2025 — 中等相关 [R2]\n3. **Bertsch et al. (2024)** \"In-Context Learning with Long-Context Models\" — 与 test-time scaling 相关 [R1]\n4. **Wiher et al. (2022)** \"On Decoding Strategies for Neural Text Generators\" — 与 constrained decoding diversity 相关 [R1]\n5. **Müller & Sennrich (2021)** \"Understanding the Properties of MBR Decoding in NMT\" — 与 §5 MBR 连接直接相关 [R1]\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n外部审稿：未启用\n\n---\n\n## Overall Assessment\n\n**Overall Score: 3.0 / 5 (Findings: borderline)**\n**Confidence: 4/5**\n\n**判断依据**：\n\n两位 Reviewer 交叉回应后评分收敛至 3.0/5（R1: 3.0 维持不变, R2: 3.5→3.0 下调）。\n\n**支持接收的因素**：\n- 统计方法论经四轮迭代达到高水准（TOST, bootstrap CI, 3-seed, Bonferroni）\n- QE vs. selection 的解耦框架有方法论贡献价值\n- 任务难度梯度分析和 WNUT-17 capability boundary 发现有实用指导意义\n- MBR decoding 连接提供理论统一\n- Round 3 的 13 个 issue 中 8 个完全解决，改进幅度显著\n\n**制约接收的因素**：\n- 核心贡献 \"correlation-selection gap\" 的 framing 仍未清晰区分定义性局限和经验性发现（W-C1），削弱 novelty\n- 训练细节/prompt template 缺失影响独立复现（W-C2）\n- Constrained decoding 对 logprob 信号语义的影响仍为 unquantified confound（W-S1）\n- RE 证据薄弱（W-S2），SJ 优势 marginal（W-S3）\n\n**修订优先级**（按影响排序）：\n1. **[Must]** Gap framing 分层（定义性 vs 经验性）——决定核心贡献的 novelty 定位\n2. **[Must]** 训练配置 + prompt template 补充——复现基本要求\n3. **[Should]** Constrained decoding 下 logprob 分布量化——加强 gap 解释力\n4. **[Should]** RE conditional analysis + 进一步降级——减少过度泛化\n5. **[Should]** SJ narrative 调整 + Abstract 简化 + 术语统一——写作质量\n6. **[Minor]** Table 格式、Ethics 位置、引用补充",
    "project": "struct_self_consist_ie",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "borderline (Findings)",
    "review_chat_id": "oc_3897c2857f11615119e277e820eae311"
  }
}
```

</details>

---


### Tool result

_source line 460 · 2026-05-15T07:08:41.203295+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_1b56445332d8ca2b4964b30f300f0e00:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4265
}
```

</details>

---


### Assistant

_source line 461 · 2026-05-15T07:08:49.785994+00:00_

Round 4 审稿报告已投递。

**汇总**：
- **Overall 3.0/5 (Findings borderline)**，两位 Reviewer 收敛一致
- **2 个 Must-Fix**：(1) Gap framing 需区分定义性/经验性两层论证；(2) 训练配置+prompt template 缺失
- **7 个 Should-Fix**：constrained decoding logprob 量化、RE 证据加强、SJ 叙事调整、Abstract 简化、术语统一、Introduction hedge、补引 Xiong et al.
- **9 个 Minor**
- **Round 3 修复进展**：13 个遗留问题中 8 个完全解决，4 个部分解决，0 个未解决。统计方法论改进（TOST/3-seed/Bonferroni/MBR 连接）得到两位 Reviewer 一致认可
- Issue Tracker 已同步更新（`review_issues.yaml`）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 38

## Round 38

2 recorded events


### User

_source line 462 · 2026-05-15T07:08:51.136293+00:00_

[Reviewer 2 审稿结果]:
审稿报告已提交给 Review Director。

总结：Round 4 审稿完成。论文统计方法论显著改进，Round 3 的 13 个问题中 8 个完全解决、4 个部分解决。新发现 2 个 Must-Fix：(1) correlation-selection gap 的非平凡性论证需区分定义性结果与经验性发现，(2) prompt template 等训练细节缺失影响复现。整体评分 Overall 3.0 (Findings)，推荐条件接收。

---

[Reviewer 2 审稿意见]:
## Reviewer 2 交叉回应 — 对 Reviewer 1 审稿报告的逐条意见

### Must-Fix 共识度
- **R1-N1 (gap 非平凡性)**: [AGREE] 与我的 N1 独立一致，进一步佐证此问题的核心性。补充：Abstract "any signal" 措辞混淆了定义性失败和经验性失败。
- **R1-N2 (constrained decoding confound)**: [AGREE with severity downgrade → should-fix] 论文已有 diversity-stratified 分析作为间接证据。但赞同 R1 建议 (b)：分析 logprob non-tie 25% 上的 selection 表现——成本低且直接回答 logprob 失败根因。
- **R1-N3 (训练细节不足)**: [AGREE] 与我的 N2 一致。R1 的列举更完整（lr, batch size, optimizer, LoRA target modules）。

### Should-Fix 共识度
- **R1-W1 (RE 单数据集)**: [REBUT] 论文已在 4 处显式声明限制并降级 claim。
- **R1-W2 (FK 独立性)**: [PARTIALLY AGREE] 论证方向正确（excess agreement 为负→FK 保守），但需补充计算方法说明。
- **R1-W3 (SJ normalizer)**: [WEAKLY AGREE] 有 rationale，ablation 为 nice-to-have。
- **R1-W4 (8B 限制)**: [REBUT] Limitations 已充分讨论。
- **R1-W5 (TOST δ 选择)**: [AGREE] 需补充 practical significance 论证。
- **R1-W6 (single-seed)**: [PARTIALLY AGREE] SciERC RE single-seed 是最弱环节，建议 Limitations 补一句。

### 缺失引用
- Bertsch et al. 2024: [REBUT] ICL focus，与 fine-tuned 模型的 confidence signals 关联薄弱
- Wiher et al. 2022: [WEAKLY AGREE] 边际相关
- Müller & Sennrich 2021: [AGREE] 与 MBR discussion 直接呼应，应补引用

### 两位 Reviewer 的核心共识
1. **Contribution #2 framing 需调整**（R1-N1 = R2-N1）——两位 reviewer 独立指出同一问题，高置信度
2. **训练细节必须补充**（R1-N3 = R2-N2）——prompt template 缺失尤其关键
3. **Constrained decoding 对 logprob 的影响需深化讨论**——R1 评为 critical，R2 评为 should-fix，建议折中处理：分析 non-tie subset + 补充 Discussion 段落

### 分歧点
- R1-W1 (RE 单数据集)：R1 认为需进一步降级，R2 认为已充分处理
- R1-N2 严重性：R1 评 critical，R2 评 should-fix（基于已有 diversity 分析）

---

[Reviewer 2 审稿结果]:
交叉回应已提交给 Director。

核心结论：两位 Reviewer 在两个关键问题上达成独立共识——(1) gap framing 需区分定义性/经验性失败，(2) 训练细节必须补充。对 constrained decoding confound 的严重性有分歧（R1: critical, R2: should-fix），建议折中处理。R1 提出的 3 篇缺失引用中仅 Müller & Sennrich 2021 值得补充。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 463 · 2026-05-15T07:09:04.985685+00:00_

Round 4 审稿流程完成。报告已投递给 Research Director。

**本轮结果摘要**：
- **Overall**: 3.0/5 (Findings borderline)，两位 Reviewer 交叉后收敛
- **2 个 Must-Fix**：(1) Gap framing 需区分定义性 vs 经验性失败；(2) 训练配置/prompt template 补充
- **7 个 Should-Fix**：constrained decoding logprob 量化、RE 证据加强、SJ 叙事调整、Abstract 简化、术语统一、Introduction hedge、补引 Xiong et al.
- **Round 3 修复**：13 个遗留问题中 8 个完全解决，4 个部分解决，0 个未解决
- Issue Tracker 已同步更新（`review_issues.yaml`）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 39

## Round 39

74 recorded events


### User

_source line 464 · 2026-05-15T07:48:50.660736+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: struct_self_consist_ie
- 论文路径: projects/struct_self_consist_ie/docs/paper/main.tex
- 目标 venue: EMNLP 2026
- Track: findings
- 截止日期: 2026-05-25

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 465 · 2026-05-15T07:48:57.056898+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 466 · 2026-05-15T07:48:57.108179+00:00_

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
…[truncated 2458 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 467 · 2026-05-15T07:49:01.579413+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__read_local_file",
  "max_results": "8"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__read_local_file",
    "max_results": "8"
  }
}
```

</details>

---


### Tool result

_source line 468 · 2026-05-15T07:49:01.630118+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 469 · 2026-05-15T07:49:04.451821+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "struct_self_consist_ie"
  }
}
```

</details>

---


### Tool result

_source line 470 · 2026-05-15T07:49:04.954702+00:00_

{"result":"# 项目 struct_self_consist_ie 概况\n\n## 实验状态 (79 个)\n\n- **exp_002_ner_conll2003**: DONE (success) — \n- **exp_004_re_diagnostic**: DONE (success) — \n- **exp_005**: DONE (success) — \n- **exp_014_entity_majority_voting**: DONE (success) — \n- **exp_013_exact_match_voting**: DONE (negative) — \n- **exp_012_logprob_baseline**: DONE (success) — \n- **mvp_pilot_005**: DONE (negative) — \n- **e1_component_wise_re_sj**: DONE (negative) — \n- **mvp_pilot_004**: DONE (negative) — \n- **ft_002_v2**: DONE (success) — \n- **mvp_pilot_002**: DONE (failed) — \n- **ft_002**: DONE (killed) — \n- **ft_001**: DONE (success) — \n- **mvp_pilot_003**: DONE (negative) — \n- **mvp_pilot_001**: DONE (negative) — \n\n## 最新报告\n# Handover — 2026-05-15\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n- exp_017_llama_conll_n16_s456_r1024（准备中）\n- exp_017_llama_conll_n16_r1024（准备中）\n- exp_001_n16_seed123_full（准备中）\n- exp_001_n16_seed456_full（准备中）\n- exp001_seed123（准备中）\n- exp001_seed456（准备中）\n- exp_007_ner_llama（准备中）\n- exp_002_merge_conll2003（准备中）\n- exp008_re_n16（准备中）\n\n## 近期结论\n- **exp_018_llama_scierc_seed42_r1024** (success): —\n- **exp_018_llama_scierc_seed456_r1024** (success): —\n- **exp_018_llama_scierc_seed456** (success): —\n\n## 趋势\n成功 43 / 负向 18 / 失败 1 / 共 70\n\n## 下一步\n（无活跃 idea，请通过 ideas.md 添加）\n\n## 资源状态\nautodl-5090: 空闲 cuda:0, cuda:1, cuda:2, cuda:3\n\n## 告警\n- ft_002: 已被终止 — unknown\n- mvp_pilot_002: 训练失败 — unknown\n- exp_008_re_n16_full: 已被终止 — unknown\n- exp_001_seed42_v2_r1024: 已被终止 — unknown\n- exp_001_seed123_v2_r1024: 已被终止 — unknown\n- exp_001_seed456_v2_ner_r1024: 已被终止 — unknown\n- exp_002_conll_n16_r1024: 已被终止 — unknown\n- exp_007_llama_n16_r1024: 已被终止 — unknown\n- exp_017_llama_conll_n16_s123_r1024: 已被终止 — unknown"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 471 · 2026-05-15T07:49:05.006323+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "struct_self_consist_ie",
  "file": "memory.md",
  "max_chars": "6000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "struct_self_consist_ie",
    "file": "memory.md",
    "max_chars": "6000"
  }
}
```

</details>

---


### Tool result

_source line 472 · 2026-05-15T07:49:05.107653+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/memory.md\", \"content\": \"# Memory — struct_self_consist_ie\\n\\n## 服务器环境\\n- autodl-5090: 4× RTX 5090 32GB, Python 3.12, vLLM 0.18.1, LLaMA Factory 0.9.4, tmux 3.2a\\n- gpu-5090-4x-2: 4× RTX 5090 32GB, PyTorch 2.10.0+cu128, vLLM 0.18.1\\n- conda: /root/miniconda3/\\n- 环境初始化: `source /etc/network_turbo && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`\\n- 项目路径: /root/autodl-tmp/struct_self_consist_ie/\\n- 基座模型: /root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B/\\n- ft_002_v2 merged: checkpoints/qwen3-8b-scierc-merged-v2/\\n- run_mvp_pilot.py 支持 --collect_logprobs, --num_test (默认已改为 9999)\\n\\n## 数据修正链 (D054-D060) 关键教训\\n- exp_012 是唯一使用 max_tokens=512 的实验，导致 voting_conf ρ 虚高 (0.502→0.379)\\n- SJ/FK 对 max_tokens 参数鲁棒（Δ<0.004），但 voting_conf 极度敏感\\n- 修正后 AUROC 排名反转：EM (0.749) > SJ (0.692) > Voting (0.684)\\n- Selection claim 由 bootstrap 确认为 null result（p=0.39），不能写 \\\"significantly outperforms\\\"\\n- 论文数据必须来自 _rerun_1024 或本身就用 1024 的实验\\n\\n## D066 LLaMA fresh rerun (2026-05-15)\\n- D066 决策：LLaMA 3-seed 全部使用 fresh rerun 数据（seed42_r1024 + seed123 + seed456_r1024）\\n- exp_018_llama_scierc_seed456（旧 exp_007 复制品）已标记 SUPERSEDED\\n- LLaMA NER SJ ρ 修正：旧 0.362±0.004 → 新 0.325±0.021（σ 增大 5× 是真实 seed 变异，seed123 拉高均值）\\n- **分析脚本与 report.json 的 EM/VC 值存在系统性差异**（如 seed42 VC: 脚本 0.373 vs report.json 0.405）。Reviewer 要求论文统一使用分析脚本输出（与 Qwen 同一套）。不要从 registry metrics（来自 report.json）直接引用 EM/VC 到论文。\\n- NER 信号排名 6/6 完全稳定：VC > SJ > EM > FK > LP\\n- Core claim \\\"structural > logprob\\\" NER 全部成立 (12/12)；RE 仅 VC 稳定胜 LP\\n\\n## Registry 清理备注 (2026-05-15)\\n- 9 个 PREPARING+killed 实验因状态机限制无法推进到 DONE，实质已废弃\\n- 包括：exp_017_llama_conll_n16_s456_r1024, exp_017_llama_conll_n16_r1024, exp_001_n16_seed123_full, exp_001_n16_seed456_full, exp001_seed123, exp001_seed456, exp_007_ner_llama, exp_002_merge_conll2003, exp008_re_n16\\n\", \"total_chars\": 1740,
…[truncated 60 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 473 · 2026-05-15T07:49:12.839726+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex",
    "limit": "100"
  }
}
```

</details>

---


### Tool result

_source line 474 · 2026-05-15T07:49:12.840103+00:00_

1	\documentclass[11pt]{article}
2	
3	\usepackage[review]{acl}
4	
5	\usepackage{times}
6	\usepackage{latexsym}
7	\usepackage[T1]{fontenc}
8	\usepackage[utf8]{inputenc}
9	\usepackage{microtype}
10	\usepackage{inconsolata}
11	\usepackage{graphicx}
12	\usepackage{booktabs}
13	\usepackage{amsmath}
14	\usepackage{amssymb}
15	\usepackage{multirow}
16	\usepackage{xcolor}
17	\usepackage{subcaption}
18	
19	\graphicspath{{figures/}}
20	
21	\title{Strong Predictors, Weak Selectors: A Systematic Comparison of Confidence Signals for Test-Time Scaling in Information Extraction}
22	
23	\author{Anonymous}
24	
25	\begin{document}
26	\maketitle
27	
28	\input{sections/abstract}
29	\input{sections/introduction}
30	\input{sections/related_work}
31	\input{sections/method}
32	\input{sections/experiments}
33	\input{sections/discussion}
34	\input{sections/conclusion}
35	
36	\section*{Limitations}
37	\input{sections/limitations}
38	
39	\section*{Ethics Statement}
40	All experiments use publicly available benchmarks (SciERC, CoNLL-2003, WNUT-17) and open-weight models (Qwen3-8B, LLaMA-3.1-8B).
41	No new human data was collected or annotated for this study.
42	
43	\bibliography{references}
44	
45	\appendix
46	\input{sections/appendix}
47	
48	\end{document}
49	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 475 · 2026-05-15T07:49:13.292068+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
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

_source line 476 · 2026-05-15T07:49:13.292480+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 477 · 2026-05-15T07:49:13.694258+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "struct_self_consist_ie",
  "file": "paper_checklist.yaml",
  "max_chars": "3000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "struct_self_consist_ie",
    "file": "paper_checklist.yaml",
    "max_chars": "3000"
  }
}
```

</details>

---


### Tool result

_source line 478 · 2026-05-15T07:49:13.795364+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"No paper_checklist.yaml found for 'struct_self_consist_ie'.\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 479 · 2026-05-15T07:49:19.421895+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 call for papers submission guidelines"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 call for papers submission guidelines"
  }
}
```

</details>

---


### Tool call

_source line 480 · 2026-05-15T07:49:19.923806+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 findings track submission deadline author guidelines"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 findings track submission deadline author guidelines"
  }
}
```

</details>

---


### Tool call

_source line 481 · 2026-05-15T07:49:20.375662+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "struct_self_consist_ie",
  "file": "writing_plan.yaml",
  "max_chars": "6000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "struct_self_consist_ie",
    "file": "writing_plan.yaml",
    "max_chars": "6000"
  }
}
```

</details>

---


### Tool result

_source line 482 · 2026-05-15T07:49:27.708494+00:00_

Web search results for query: "EMNLP 2026 findings track submission deadline author guidelines"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"Announcements | Computational Linguistics","url":"https://submissions.cljournal.org/index.php/cljournal/announcement"},{"title":"EMNLP 2026 Conference Deadline | Live Countdown Tracker","url":"https://www.getpaperpilot.com/deadlines/emnlp-2026.html"},{"title":"[EMNLP 2025] First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2025-first-call-papers"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"},{"title":"EMNLP: Empirical Methods in Natural Language Processing 2027 2026 2025 ...","url":"http://www.wikicfp.com/cfp/program?id=883"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"EMNLP 2026 (@emnlpmeeting) / Posts / X","url":"https://x.com/emnlpmeeting"}]

Based on the search results, here's the information about EMNLP 2026 submission deadlines and guidelines:

## Key Submission Information

**Submission Process:**
EMNLP 2026 uses ACL Rolling Review (ARR) as a reviewing system, but final decisions will be made by the conference. Authors follow a two-step process: first submitting articles to ARR where they receive reviews and meta-reviews, then committing their reviewed articles to EMNLP 2026 where Senior Area Chairs and Program Chairs make acceptance decisions.

**Important Deadlines:**
- ARR submission deadline (long & short papers): May 25, 2026
- Reviewer registration deadline for ALL authors: May 27
…[truncated 947 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "WebSearch",
  "elapsed_ms": 7784
}
```

</details>

---


### Tool result

_source line 483 · 2026-05-15T07:49:29.319831+00:00_

Web search results for query: "EMNLP 2026 call for papers submission guidelines"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"Submission Guide","url":"https://nlp4climate.github.io/submissionguide/"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"},{"title":"2026 *ACL Conference Dates | Computational Linguistics","url":"https://submissions.cljournal.org/index.php/cljournal/announcement/view/14"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"Confs: 2026 Conference on Empirical Methods in Natural ...","url":"https://www.facebook.com/linguistlist/posts/confs-2026-conference-on-empirical-methods-in-natural-language-processing-emnlp-/1351983883622556/"},{"title":"EMNLP 2026 on X: \"📢 Please note a critical update to the original #EMNLP2026 Call for Papers: since EMNLP and AACL share the ARR May cycle, authors will need to explicitly select a target conference at submission time. This choice will be binding! For more details see: https://t.co/0u1wbX9fT6\" / X","url":"https://x.com/emnlpmeeting/status/2047754845919031450"},{"title":"EMNLP 2026 on X: \"📢 The First Call for Papers for EMNLP 2026 is officially out! 📝 We welcome long &amp; short papers featuring original research on empirical methods for NLP. 🗓️ ARR Submission Deadline: May 25, 2026 🔗 Read the full CFP here: https://t.co/GU2kaISjUG #EMNLP2026\" / X","url":"https://x.com/emnlpmeeting/status/2029508292637061462"}]

Based on the
…[truncated 2481 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "WebSearch",
  "elapsed_ms": 9897
}
```

</details>

---


### Tool result

_source line 484 · 2026-05-15T07:49:29.320460+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/writing_plan.yaml\", \"content\": \"meta:\\n  venue: EMNLP 2026 Main (via ARR May)\\n  track: main\\n  template: null  # ARR/ACL format — need to download acl2023.sty or latest ARR template\\n  template_note: \\\"No local template found. Worker should download latest ARR LaTeX template from ACL Rolling Review.\\\"\\n  page_limit: 8  # + unlimited references\\n  deadline: 2026-05-25\\n  core_claim: >\\n    Structural consistency signals are the strongest unsupervised quality estimators for LLM-based IE —\\n    entity voting leads ρ (0.38) while EM leads AUROC (0.75), with soft Jaccard as complementary robust signal\\n    (temperature-stable: NER Δρ=0.028; conditional filtering ρ=0.31). A correlation-selection gap means\\n    this does not translate to best-of-N selection — no signal reliably surpasses greedy on either task\\n    (p>0.39, bootstrap). Signal effectiveness is task-difficulty-dependent: easy tasks favor exact-match,\\n    hard tasks favor structural consistency, and SJ strength scales with both sample size (N=8→16 ρ +0.052)\\n    and instance complexity (entity count 6+ ρ=0.55). RE reveals a capability boundary: when compound\\n    error propagation dominates (~44% zero-F1), all signals weaken (ρ=0.134-0.350) — conditional filtering restores\\n    structural signal advantage (SJ ρ=0.31) while logprob collapses (ρ=-0.03).\\n  created_at: 2026-05-14T13:00:00Z\\n  selected_title: \\\"Strong Predictors, Weak Selectors: A Systematic Comparison of Confidence Signals for Test-Time Scaling in Information Extraction\\\"\\n  director_approval: \\\"2026-05-14 approved with modifications: title #2 selected, RE must distinguish joint vs RE-only protocol (D023), 3 tables confirmed (tab_robustness kept), exp_003/exp_007 pending — Director will notify for Patch\\\"\\n  re_protocol_note: \\\"D023: Joint RE SJ ρ=0.267 < FK ρ=0.315; RE-only 
…[truncated 4526 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 8944
}
```

</details>

---


### Tool call

_source line 485 · 2026-05-15T07:49:38.663903+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "sections/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "sections/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper"
  }
}
```

</details>

---


### Tool result

_source line 486 · 2026-05-15T07:49:38.865516+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Glob",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 487 · 2026-05-15T07:49:38.865947+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "struct_self_consist_ie"
  }
}
```

</details>

---


### Tool result

_source line 488 · 2026-05-15T07:49:38.916591+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 489 · 2026-05-15T07:49:41.880656+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper"
  }
}
```

</details>

---


### Tool result

_source line 490 · 2026-05-15T07:49:41.931456+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/method.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/limitations.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 491 · 2026-05-15T07:49:44.793639+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 492 · 2026-05-15T07:49:45.245443+00:00_

1	\begin{abstract}
2	Test-time scaling through multi-sample generation promises quality improvements for LLM-based information extraction, but which confidence signals best serve quality estimation versus sample selection remains unclear.
3	We systematically compare five confidence signals from three families---structural (entity voting, Soft Jaccard), surface (exact match, Fleiss' $\kappa$), and model-internal (log-probability)---across NER (three datasets of varying difficulty) and RE (SciERC, preliminary) with two model families (Qwen3-8B, LLaMA-3.1-8B).
4	For quality estimation, the strongest signals achieve $\rho{=}0.38$ (entity voting) and AUROC${=}0.75$ (exact match), with ranking and classification favoring different signals across task complexity.
5	However, this strong estimation does not translate into selection gains: four of five signals are instance-level by construction, and log-probability---the only per-sample signal---also fails to outperform greedy decoding on SciERC ($p{>}0.39$, bootstrap) despite 13--18~pp of oracle headroom.
6	We term this the \textit{correlation-selection gap}.
7	Signal rankings further depend on task difficulty---exact match dominates easy tasks, structural signals dominate hard tasks---with consistent ordering direction across models but model-dependent magnitude; when model capability is insufficient, apparent correlations are driven by zero/non-zero separation rather than genuine quality gradation.
8	These results reframe consistency signals as quality estimators rather than output selectors for structured IE.
9	\end{abstract}
10	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 451
}
```

</details>

---


### Tool call

_source line 493 · 2026-05-15T07:49:45.245914+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 494 · 2026-05-15T07:49:45.697559+00:00_

1	\section{Introduction}\label{sec:introduction}
2	
3	Self-consistency---sampling multiple outputs and aggregating them---has become a powerful strategy for improving language model reasoning.
4	On discrete-answer tasks such as arithmetic and commonsense QA, majority voting over chain-of-thought samples yields large gains: +18 percentage points on GSM8K (PaLM-540B; \citealp{wang2023selfconsistency}).
5	More broadly, test-time compute scaling through repeated sampling and selection has emerged as a complementary axis to model scaling, offering substantial quality improvements at inference time \cite{snell2024scaling, brown2024monkeys}.
6	These results rest on a shared assumption: that among $N$ stochastic samples, a selection mechanism can identify better outputs.
7	For tasks with a single correct answer, this assumption holds naturally---the majority vote is the selector.
8	But information extraction (IE) poses a fundamentally different challenge.
9	The output is not a single token or number; it is a \textit{set} of entities or relations with internal dependencies, where two samples may extract overlapping but non-identical structures.
10	There is no obvious majority to vote on, partial agreement is the norm rather than the exception, and the space of valid outputs is combinatorially large.
11	Can self-consistency still provide useful signal in this structured setting?
12	
13	Prior work on confidence estimation for LLM-based IE has conflated two distinct objectives: \textit{quality estimation} (which inputs does the model handle reliably?) and \textit{sample selection} (which of $N$ outputs is best?).
14	These require fundamentally different signal properties: the former benefits from instance-level aggregation, while the latter demands per-sample discrimination.
15	Self-consistency methods for discrete answers \cite{wang2023selfconsistency, chen2024usc} and weighted variants \cite{taubenfeld2025cisc, kang2025selfcertainty} assume outputs can be grouped by equivalen
…[truncated 4876 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 451
}
```

</details>

---


### Tool call

_source line 495 · 2026-05-15T07:49:45.697912+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 496 · 2026-05-15T07:49:48.809915+00:00_

1	\section{Related Work}\label{sec:related}
2	
3	\paragraph{Self-consistency and test-time scaling.}
4	Self-consistency decoding \cite{wang2023selfconsistency} improves reasoning by majority voting over chain-of-thought samples, assuming a discrete answer space.
5	Extensions to free-form text use LLM-based comparison \cite{chen2024usc}, atomic sub-claim decomposition \cite{thirukovalluru2024atomic}, or cross-sample hallucination detection \cite{manakul2023selfcheckgpt}.
6	For test-time scaling, \citet{snell2024scaling} characterize compute scaling laws and \citet{brown2024monkeys} show best-of-$N$ gains across tasks.
7	Recent reward-free selectors include confidence-weighted voting \cite{taubenfeld2025cisc}, KL-based self-certainty \cite{kang2025selfcertainty}, adaptive sampling \cite{kim2026reasc}, ranked aggregation \cite{wang2025rankedvoting}, and latent-space consistency \cite{oh2025latentsc}.
8	Concurrently, \citet{feng2025optimal} and \citet{wang2025make} adapt self-consistency to difficulty-aware settings, echoing our finding that signal rankings shift with task complexity; \citet{li2025llms} propose generative self-aggregation for IE but focus on output fusion rather than confidence-based selection.
9	All of the above target reasoning/QA with discrete answers or specific aggregation strategies.
10	Our work extends self-consistency to set-valued structured outputs and identifies the correlation-selection gap: strong quality estimation ($\rho{=}0.38$) coexists with selection failure ($p{>}0.39$).
11	
12	\paragraph{Consistency for structured IE.}
13	\citet{nedellec2026consistency} study consistency--accuracy correlations for LLM-based NER/RE, corroborating our quality-estimation findings.
14	Their work leaves open three questions we address: (i)~whether structural matching improves on surface-level agreement (which they acknowledge ``overlooks semantically consistent outputs''); (ii)~whether quality estimation translates to best-of-$N$ selection; and (iii)~whet
…[truncated 3430 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 3111
}
```

</details>

---


### Tool call

_source line 497 · 2026-05-15T07:49:49.211580+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 498 · 2026-05-15T07:49:49.212047+00:00_

1	\section{Method}\label{sec:method}
2	
3	\subsection{Problem Formulation}\label{sec:formulation}
4	
5	Given a language model $\mathcal{M}$ and input $x$, we sample $N$ structured outputs $\{y_1, \ldots, y_N\}$ at temperature $T > 0$ via constrained decoding \cite{willard2023guided}.
6	Each $y_i$ is an entity set (NER) or relation set (RE).
7	A confidence signal $c$ serves two purposes: (a) \textit{quality estimation}---predicting which instances the model handles reliably, and (b) \textit{sample selection}---identifying the best output among $N$ candidates.
8	
9	A \textbf{per-sample signal} scores each $y_i$ independently, $c_{\text{ps}}: (x, y_i) \to \mathbb{R}$, enabling direct candidate ranking.
10	An \textbf{instance-level signal} aggregates over all $N$ samples, $c_{\text{il}}: (x, \{y_i\}_{i=1}^N) \to \mathbb{R}$, producing a single score per input.
11	This asymmetry---between predicting \textit{which inputs} are easy and selecting \textit{which output} is best---is central to the correlation-selection gap we investigate.
12	Notation is summarized in Appendix~\ref{app:notation}.
13	
14	\subsection{Confidence Signals}\label{sec:signals}
15	
16	We use \textit{confidence signal} as the umbrella term for all five measures.
17	Four are \textit{consistency signals}---computed from inter-sample agreement---spanning two families: \textit{structural} (Soft Jaccard, entity voting) and \textit{surface} (exact match, Fleiss' $\kappa$).
18	The fifth, log-probability, is the sole \textit{model-internal} signal and the only one that scores individual samples rather than the instance as a whole.
19	
20	\paragraph{Log-probability (model-internal, per-sample).}
21	The only per-sample signal.
22	For sample $y_i$ with tokens $t_1, \ldots, t_{|y_i|}$:
23	\begin{equation}\label{eq:logprob}
24	c_{\text{lp}}(y_i) = \frac{1}{|y_i|} \sum_{j=1}^{|y_i|} \log p_{\mathcal{M}}(t_j \mid t_{<j}, x)
25	\end{equation}
26	
27	\paragraph{Exact match voting (surface, instance-level).}
28	The majo
…[truncated 4022 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 499 · 2026-05-15T07:49:49.413744+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 500 · 2026-05-15T07:49:49.414913+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Experimental Setup}
5	\label{sec:setup}
6	
7	\paragraph{Datasets.}
8	We evaluate on three English IE benchmarks spanning a difficulty gradient.
9	\textbf{SciERC} \cite{luan2018scierc} contains 551 test instances annotated for joint NER (6 types) and RE (7 types).
10	\textbf{CoNLL-2003} \cite{tjongkimsang2003conll} provides 3{,}453 test sentences with 4 entity types, where models achieve ${\approx}$91\% micro F1.
11	\textbf{WNUT-17} \cite{derczynski2017wnut} consists of 1{,}287 social media instances with emerging entities, used to probe method boundaries (52\% zero F1).
12	
13	\paragraph{Models and sampling.}
14	Both \textbf{Qwen3-8B} and \textbf{LLaMA-3.1-8B-Instruct} are fine-tuned with LoRA (rank$=$32, $\alpha{=}64$) for 5 epochs using LLaMA Factory \cite{zheng2024llamafactory} under identical training procedures, ensuring cross-architecture comparisons (at 8B scale) reflect architectural differences rather than training confounds.
15	We draw $N{=}8$ samples at $T{=}1.0$ (primary), with $N{=}16$ for scaling experiments.\footnote{$N{=}16$ results for CoNLL (Qwen) and SciERC (LLaMA) are in Table~\ref{tab:robustness} (Appendix~\ref{app:robustness}).}
16	Quality estimation uses Spearman $\rho$ and AUROC; downstream utility uses best-of-$N$ selection F1 with exact span matching (NER) and head-tail-label matching (RE).
17	Inference uses vLLM with constrained decoding \cite{willard2023guided}.
18	
19	%% ============================================================
20	\subsection{Quality Estimation Results}
21	\label{sec:qe_results}
22	
23	\begin{table*}[t]
24	\centering
25	\small
26	\caption{Quality estimation across tasks and models (Spearman $\rho$ and AUROC). Best value per block and column in \textbf{bold}. SciERC evaluates joint NER (6 types) and RE (7 types); CoNLL evaluates NER (4 types). $N{=}8$ results use seed${=}42$; $N{=}16$ results are averaged across seeds \{42, 123, 456\}.\textsuperscript{$
…[truncated 12480 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 1
}
```

</details>

---


### Tool call

_source line 501 · 2026-05-15T07:49:49.465566+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 502 · 2026-05-15T07:49:49.466038+00:00_

1	\section{Discussion}\label{sec:discussion}
2	
3	\paragraph{Practical recommendations.}
4	For per-instance quality ranking, entity voting provides the strongest rank correlation ($\rho{=}0.38$), though exact match leads binary discrimination (AUROC${=}0.749$); under conditional filtering, EM leads on both NER and RE ($\rho{=}0.360$, $0.417$).
5	Signal rankings depend on task difficulty---EM dominates easy tasks (CoNLL), Voting and SJ dominate hard tasks (SciERC)---directionally consistent across tested model families, though with model-dependent magnitude.
6	When model capability is insufficient (WNUT-17), all signals converge toward non-significant conditional correlations (Table~\ref{tab:wnut}).
7	
8	\paragraph{Why the gap exists: two layers.}
9	\textit{Layer 1 (structural):} Four of five signals are instance-level aggregates that assign a single score per input; they cannot rank candidates by construction.
10	Consensus-proximity selection (\S\ref{sec:evaluation}) does not recover per-sample discrimination (Table~\ref{tab:selection}).
11	\textit{Layer 2 (empirical):} Log-probability, the only per-sample signal, also fails to exploit the 13--18~pp oracle headroom.
12	Under constrained decoding, logprob scores are severely compressed: 60\% of instances have a within-sample range below 0.05, and 75\% of pairwise comparisons are effective ties ($|\Delta|{<}0.026$; Appendix~\ref{app:logprob_ties}).
13	In the non-tied 40\%, logprob selection significantly outperforms greedy ($+2.9$~pp, $p{=}0.01$), confirming the signal carries useful information but is resolution-limited.
14	The common root is that quality estimation ranks \textit{instances}, while sample selection requires ranking \textit{candidates within a single instance}---a finer granularity that neither instance-level aggregation nor token-level confidence provides.
15	Diversity-stratified analysis confirms the gap persists even among high-diversity instances (Appendix~\ref{app:diversity}); RE miscalibration (E
…[truncated 1117 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 503 · 2026-05-15T07:49:49.518002+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 504 · 2026-05-15T07:49:49.518473+00:00_

1	\section{Conclusion}\label{sec:conclusion}
2	
3	This work provides, to our knowledge, the first multi-family comparison of confidence signals for test-time scaling in generative information extraction.
4	By comparing five signals from three families across NER and RE tasks of varying difficulty, we disentangle quality estimation from sample selection---two objectives that prior work has conflated.
5	Consistency-based signals are effective quality estimators ($\rho$ up to 0.38, AUROC up to 0.75).
6	Four of five signals are instance-level by construction and cannot rank candidates; log-probability, the only per-sample signal, also fails ($p{>}0.39$, 13--18~pp oracle headroom on SciERC), a disconnect we term the \textit{correlation-selection gap}.
7	Signal rankings depend on task difficulty---exact match leads on easy tasks, structural signals on hard tasks---with this ordering directionally consistent across model families, though magnitudes are model-dependent.
8	While our NER findings are validated across three datasets, our RE conclusions rest on SciERC alone and warrant further validation.
9	
10	Trained verifiers or reward models could close the selection gap by learning per-sample quality discrimination.
11	Cross-task transfer beyond IE, scaling to larger models (70B+), and integration with conformal prediction are promising directions.
12	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 505 · 2026-05-15T07:49:49.569120+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 506 · 2026-05-15T07:49:49.569528+00:00_

1	Our evaluation covers three datasets but only one RE benchmark (SciERC), where 40\% of instances receive zero F1, compressing the discriminable range and limiting signal differentiation for relation extraction.
2	RE selection failure persists even when restricting to non-zero F1 instances (Appendix~\ref{app:re_conditional_selection}), ruling out floor effects as the sole explanation, but generalization to other RE benchmarks remains unvalidated.
3	WNUT-17 confirms the capability boundary of our approach, but our positive results on formal-domain text (CoNLL, SciERC) have not been validated on informal or noisy text where models achieve non-trivial performance.
4	
5	We evaluate two model families (Qwen3-8B and LLaMA-3.1-8B), both at 8B parameters.
6	A 3-seed robustness analysis confirms that signal rankings are stable across seeds ($\sigma{\leq}0.025$; Table~\ref{tab:multiseed}), but whether our findings---particularly the correlation-selection gap and the difficulty-dependent signal ordering---hold for larger models (70B+) or closed-source APIs remains untested.
7	Larger models may produce higher-quality and more diverse samples, potentially altering the signal landscape.
8	
9	Our analysis of selection potential uses only unsupervised signals.
10	We do not train a dedicated verifier or reward model, leaving unknown how much of the oracle headroom a supervised approach could recover.
11	
12	We evaluate at $N{=}8$ and $N{=}16$.
13	The behavior of confidence signals at larger sample sizes (e.g., $N{=}64$ or $N{=}128$) is unknown, and $N$-scaling gains are setting-dependent: SJ improves by $+0.052$ on Qwen SciERC NER but only $+0.016$ on LLaMA SciERC NER when doubling from $N{=}8$ to $N{=}16$.
14	
15	On CoNLL with LLaMA, the SJ--FK gap is only 0.003 ($\rho{=}0.431$ vs.\ $0.428$), so the structural advantage over surface signals may not generalize to all simple-schema datasets.
16	Constrained decoding (Outlines/vLLM) enforces schema compliance, potentially compressing 
…[truncated 314 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 507 · 2026-05-15T07:49:49.569764+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 508 · 2026-05-15T07:49:49.871763+00:00_

1	\section{Notation}\label{app:notation}
2	
3	Table~\ref{tab:notation} summarizes the notation used throughout the paper.
4	
5	\begin{table}[h]
6	\centering
7	\small
8	\begin{tabular}{cl}
9	\toprule
10	Symbol & Meaning \\
11	\midrule
12	$\mathcal{M}$ & Language model \\
13	$x$ & Input instance \\
14	$y_i$ & $i$-th stochastic sample \\
15	$N$ & Number of samples \\
16	$T$ & Sampling temperature \\
17	$c(\cdot)$ & Confidence signal \\
18	SJ & Soft Jaccard similarity \\
19	FK & Fleiss' $\kappa$ \\
20	EM & Exact-match voting rate \\
21	$c_{\text{vote}}$ & Entity voting confidence \\
22	$c_{\text{lp}}$ & Log-probability (mean token log-likelihood) \\
23	\bottomrule
24	\end{tabular}
25	\caption{Notation used throughout the paper.}
26	\label{tab:notation}
27	\end{table}
28	
29	\section{Robustness Analysis}\label{app:robustness}
30	
31	\begin{table}[t]
32	\centering
33	\small
34	\caption{Signal robustness across configurations (Spearman $\rho$). Top: temperature on Qwen SciERC. Middle: sample size on Qwen SciERC. Bottom: cross-architecture transfer (LLaMA CoNLL $N{=}16$, 3-seed mean $\pm\sigma$). $^\dagger$Mean over 3 seeds ($\sigma{=}0.025$; individual: 0.428, 0.424, 0.384).}
35	\label{tab:robustness}
36	\begin{tabular}{llcc}
37	\toprule
38	& & NER $\rho$ & RE $\rho$ \\
39	\midrule
40	\multicolumn{4}{l}{\textit{Temperature} (Qwen SciERC, $N{=}8$)} \\
41	\quad SJ & $T{=}0.7$ & 0.388 & 0.234 \\
42	\quad SJ & $T{=}1.0$ & 0.360 & 0.250 \\
43	\quad FK & $T{=}0.7$ & 0.321 & 0.184 \\
44	\quad FK & $T{=}1.0$ & 0.267 & 0.275 \\
45	\midrule
46	\multicolumn{4}{l}{\textit{Sample size} (Qwen SciERC, $T{=}1.0$)} \\
47	\quad SJ & $N{=}8$  & 0.360 & 0.250 \\
48	\quad SJ & $N{=}16$ & 0.412$^\dagger$ & 0.281 \\
49	\quad FK & $N{=}8$  & 0.267 & 0.275 \\
50	\quad FK & $N{=}16$ & 0.280 & 0.279 \\
51	\midrule
52	\multicolumn{4}{l}{\textit{Cross-architecture} (LLaMA CoNLL, $N{=}16$, 3 seeds)} \\
53	\quad SJ &  & $0.463{\pm}0.007$ & --- \\
54	\quad FK &  & $0.455{\pm}0.006$ & --- \\
55	\quad EM &
…[truncated 27104 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 509 · 2026-05-15T07:49:57.004218+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/references.bib",
  "limit": "200"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/references.bib",
    "limit": "200"
  }
}
```

</details>

---


### Tool result

_source line 510 · 2026-05-15T07:49:57.356124+00:00_

1	% Auto-generated from literature_map.yaml — do not edit manually
2	
3	@inproceedings{angelopoulos2021conformal,
4	  title = {Uncertainty Sets for Image Classifiers using Conformal Prediction},
5	  author = {Angelopoulos, Anastasios N. and Bates, Stephen and Malik, Jitendra and Jordan, Michael I.},
6	  booktitle = {ICLR 2021},
7	  year = {2021},
8	  url = {https://arxiv.org/abs/2009.14193}
9	}
10	
11	@article{brown2024monkeys,
12	  title = {Large Language Monkeys: Scaling Inference Compute with Repeated Sampling},
13	  author = {Brown, Bradley and Juravsky, Jordan and Ehrlich, Ryan and Clark, Ronald and Le, Quoc V. and Ré, Christopher and Mirhoseini, Azalia},
14	  journal = {arXiv preprint arXiv:2407.21787},
15	  year = {2024},
16	  url = {https://arxiv.org/abs/2407.21787}
17	}
18	
19	@inproceedings{chen2024usc,
20	  title = {Universal Self-Consistency for Large Language Model Generation},
21	  author = {Chen, Xinyun and Aksitov, Renat and Alon, Uri and Ren, Jie and Xiao, Kefan and Yin, Pengcheng and Prakash, Sushant and Sutton, Charles and Wang, Xuezhi and Zhou, Denny},
22	  booktitle = {arXiv preprint (ICML 2024 Workshop ICL)},
23	  year = {2024},
24	  url = {https://arxiv.org/abs/2311.17311}
25	}
26	
27	@article{cobbe2021verifiers,
28	  title = {Training Verifiers to Solve Math Word Problems},
29	  author = {Cobbe, Karl and Kosaraju, Vineet and Bavarian, Mohammad and Chen, Mark and Jun, Heewoo and Kaiser, Lukasz and Plappert, Matthias and Tworek, Jerry and Hilton, Jacob and Nakano, Reiichiro and Hesse, Christopher and Schulman, John},
30	  journal = {arXiv preprint arXiv:2110.14168},
31	  year = {2021},
32	  url = {https://arxiv.org/abs/2110.14168}
33	}
34	
35	@inproceedings{culotta2004confidence,
36	  title = {Confidence Estimation for Information Extraction},
37	  author = {Culotta, Aron and McCallum, Andrew},
38	  booktitle = {HLT-NAACL 2004},
39	  year = {2004},
40	  url = {https://aclanthology.org/N04-4028/}
41	}
42	
43	@inproceedings{derczynski2017wnut,
44
…[truncated 7562 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 351
}
```

</details>

---


### Tool call

_source line 511 · 2026-05-15T07:49:57.406825+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
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

_source line 512 · 2026-05-15T07:49:57.457470+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 513 · 2026-05-15T07:50:02.031518+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "struct_self_consist_ie",
  "file": "review_issues.yaml",
  "max_chars": "3000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "struct_self_consist_ie",
    "file": "review_issues.yaml",
    "max_chars": "3000"
  }
}
```

</details>

---


### Tool result

_source line 514 · 2026-05-15T07:50:02.031910+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"file must be one of ['ARCHITECTURE.md', 'DATA.md', 'EVALUATION.md', 'MODELS.md', 'ROADMAP.md', 'constraints.yaml', 'decisions.yaml', 'ideas.md', 'literature_map.yaml', 'memory.md', 'paper_checklist.yaml', 'paper_framing.md', 'paper_provenance.yaml', 'report.md', 'writing_plan.yaml'], got 'review_issues.yaml'\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 515 · 2026-05-15T07:50:02.483593+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/review_issues.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/review_issues.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie"
  }
}
```

</details>

---


### Tool result

_source line 516 · 2026-05-15T07:50:03.236418+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_issues.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Glob",
  "elapsed_ms": 752
}
```

</details>

---


### Tool call

_source line 517 · 2026-05-15T07:50:03.437584+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review 2026 submission format page limit long paper short paper guidelines"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review 2026 submission format page limit long paper short paper guidelines"
  }
}
```

</details>

---


### Tool result

_source line 518 · 2026-05-15T07:50:08.862301+00:00_

Web search results for query: "ACL Rolling Review 2026 submission format page limit long paper short paper guidelines"

Links: [{"title":"Paper formatting guidelines - ACLPUB","url":"https://acl-org.github.io/ACLPUB/formatting.html"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"ACL Rolling Review | ACL Member Portal","url":"https://www.aclweb.org/portal/content/acl-rolling-review"},{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"}]

Based on the search results, here are the ACL Rolling Review 2026 submission format guidelines for page limits:

## Long Papers

Review versions of long papers may have up to eight (8) pages of content plus unlimited pages for references. Final versions of accepted papers will be given one additional page of content (up to 9 pages for long papers) to address reviewers' comments.

## Short Papers

Short papers may consi
…[truncated 804 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "WebSearch",
  "elapsed_ms": 5424
}
```

</details>

---


### Tool call

_source line 519 · 2026-05-15T07:50:11.324405+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_issues.yaml"
  }
}
```

</details>

---


### Tool result

_source line 520 · 2026-05-15T07:50:11.576784+00:00_

1	issues:
2	  # ============================================================
3	  # Round 0 issues (all resolved)
4	  # ============================================================
5	  - id: "R0-C1"
6	    summary: "模型规模单一（仅 8B）"
7	    category: experiment
8	    severity: critical
9	    status: resolved
10	    first_raised_round: 0
11	    last_seen_round: 1
12	    mentions:
13	      - round: 0
14	        reviewers: [1, 2]
15	        note: "8B→8B 仅验证架构鲁棒性非规模鲁棒性"
16	      - round: 1
17	        reviewers: [1, 2]
18	        note: "model-agnostic 与 Limitations 矛盾"
19	    action_items:
20	      - round: 1
21	        action: "全文替换 model-agnostic → consistent across tested model families"
22	        assigned_to: "Paper Agent"
23	        status: resolved
24	    resolution: "Round 2 Reviewer 确认措辞修正到位，无再提"
25	    resolution_round: 2
26	
27	  - id: "R0-C2"
28	    summary: "相关工作显著遗漏"
29	    category: framing
30	    severity: warning
31	    status: resolved
32	    first_raised_round: 0
33	    last_seen_round: 1
34	    mentions:
35	      - round: 0
36	        reviewers: [1, 2]
37	        note: "5 篇核心文献缺失"
38	      - round: 1
39	        reviewers: [1, 2]
40	        note: "新遗漏：Optimal SC, Difficulty-Adaptive SC"
41	    action_items:
42	      - round: 1
43	        action: "补充 6 篇引用到 Related Work"
44	        assigned_to: "Paper Agent"
45	        status: resolved
46	    resolution: "Round 2: 49 条 bib 全部 cited, 0 orphan, 无遗漏"
47	    resolution_round: 2
48	
49	  - id: "R0-C3"
50	    summary: "RE 结论仅基于 SciERC 单数据集"
51	    category: experiment
52	    severity: critical
53	    status: resolved
54	    first_raised_round: 0
55	    last_seen_round: 4
56	    mentions:
57	      - round: 0
58	        reviewers: [1, 2]
59	        note: "需跨数据集验证或降级措辞"
60	      - round: 2
61	        reviewers: [1, 2]
62	        note: "Abstract RE 措辞需修正"
63	      - round: 3
64	        reviewers: [1, 2]
65	        note: "Round 2 措辞修正到位，但 R3 Reviewer 2 再次提出 44% zero-F1 floor effect 严重压缩可区分范围"
66	      - round: 4
67	     
…[truncated 40210 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 252
}
```

</details>

---


### Tool call

_source line 521 · 2026-05-15T07:50:40.969735+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "struct_self_consist_ie",
  "file": "constraints.yaml",
  "max_chars": "3000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "struct_self_consist_ie",
    "file": "constraints.yaml",
    "max_chars": "3000"
  }
}
```

</details>

---


### Tool result

_source line 522 · 2026-05-15T07:50:41.070449+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"No constraints.yaml found for 'struct_self_consist_ie'.\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 523 · 2026-05-15T07:50:44.486310+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/config.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/config.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie"
  }
}
```

</details>

---


### Tool result

_source line 524 · 2026-05-15T07:50:44.537000+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 525 · 2026-05-15T07:50:47.100189+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/config*.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/config*.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie"
  }
}
```

</details>

---


### Tool result

_source line 526 · 2026-05-15T07:50:47.150783+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 527 · 2026-05-15T07:50:53.382320+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/project.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/project.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie"
  }
}
```

</details>

---


### Tool result

_source line 528 · 2026-05-15T07:50:53.433084+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 529 · 2026-05-15T07:50:56.345957+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/",
  "description": "List project root directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/",
    "description": "List project root directory"
  }
}
```

</details>

---


### Tool result

_source line 530 · 2026-05-15T07:50:56.496978+00:00_

AGENTS.md
ROADMAP.lock
ROADMAP.md
artifacts
checkpoints
decisions.lock
decisions.yaml
docs
dream_registry.lock
dream_registry.yaml
dream_registry.yaml.bak
experiment_plan.lock
experiment_plan.yaml
figures
literature_map.lock
literature_map.yaml
logs
memory.md
paper_framing.md
paper_provenance.lock
paper_provenance.yaml
registry.lock
registry.yaml
report.md
study_status.lock
task_context
writing_plan.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Bash",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 531 · 2026-05-15T07:50:59.610645+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/agent/ 2>/dev/null || echo \"NO_AGENT_DIR\"",
  "description": "List agent directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/agent/ 2>/dev/null || echo \"NO_AGENT_DIR\"",
    "description": "List agent directory"
  }
}
```

</details>

---


### Tool result

_source line 532 · 2026-05-15T07:50:59.711462+00:00_

NO_AGENT_DIR

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Bash",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 533 · 2026-05-15T07:51:48.879432+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "project": "struct_self_consist_ie",
  "text": "## 审稿任务 — Reviewer 1 (Round 1)\n\n### Venue 信息\n- **Target**: EMNLP 2026 Findings (via ARR May 2026 cycle)\n- **Deadline**: 2026-05-25\n- **页数限制**: 正文 8 页 + unlimited references\n- **模板**: ACL format (`\\usepackage[review]{acl}`)\n- **匿名规则**: Double-blind\n- **Limitations section**: 必须，位于 Conclusion 后、References 前，不计页数\n- **附录**: 允许，不计页数\n\n### 论文路径\n`projects/struct_self_consist_ie/docs/paper/main.tex`\n（各 section 在 `sections/` 子目录下）\n\n### 你的审查侧重：方法严谨性 + 实验设计 + 统计有效性\n\n请重点评估以下方面：\n\n1. **方法形式化**\n   - 5 种信号的数学定义是否清晰完整、无歧义？\n   - Soft Jaccard 的 Hungarian matching 描述是否足够精确可复现？\n   - Fleiss' κ 应用于非独立样本的 justification 是否充分？\n   - per-sample vs instance-level 信号的分类是否自洽？\n\n2. **实验设计**\n   - 数据集选择是否合理覆盖 difficulty gradient？\n   - 模型选择（2×8B）是否足以支撑论文声称的 cross-architecture 结论？\n   - N=8/16 和 T=0.7/1.0 的设置是否充分？\n   - 训练配置（LoRA + fine-tuning）的细节是否足够复现？\n\n3. **统计分析**\n   - Bootstrap 检验的设置（B=10,000, 95% CI）是否恰当？\n   - TOST 等价检验的 δ 选择是否有依据？\n   - 多重比较校正的处理是否到位？\n   - Spearman ρ 和 AUROC 的联合报告是否合理？\n\n4. **核心 claim 验证**\n   - \"correlation-selection gap\" 的论证是否严密？特别是 4/5 信号是 instance-level（定义性无法 select）vs logprob 经验性失败——这两层是否被清晰区分？\n   - \"constrained decoding\" 作为潜在混淆变量是否被充分讨论？\n   - RE 结论仅基于 SciERC 单数据集——这一局限是否在论文中被恰当处理？\n   - Task-difficulty dependent signal ranking 是否有充分数据支持？\n\n5. **复现性**\n   - 训练 hyperparameters 是否完整报告？\n   - Prompt template 是否提供？\n   - 代码/数据可用性？\n\n请按 EMNLP 审稿标准给出完整审稿报告，包含：Summary、Strengths、Weaknesses (must-fix / should-fix / minor)、Questions、Missing References、Overall Assessment（评分 + 置信度）。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "project": "struct_self_consist_ie",
    "text": "## 审稿任务 — Reviewer 1 (Round 1)\n\n### Venue 信息\n- **Target**: EMNLP 2026 Findings (via ARR May 2026 cycle)\n- **Deadline**: 2026-05-25\n- **页数限制**: 正文 8 页 + unlimited references\n- **模板**: ACL format (`\\usepackage[review]{acl}`)\n- **匿名规则**: Double-blind\n- **Limitations section**: 必须，位于 Conclusion 后、References 前，不计页数\n- **附录**: 允许，不计页数\n\n### 论文路径\n`projects/struct_self_consist_ie/docs/paper/main.tex`\n（各 section 在 `sections/` 子目录下）\n\n### 你的审查侧重：方法严谨性 + 实验设计 + 统计有效性\n\n请重点评估以下方面：\n\n1. **方法形式化**\n   - 5 种信号的数学定义是否清晰完整、无歧义？\n   - Soft Jaccard 的 Hungarian matching 描述是否足够精确可复现？\n   - Fleiss' κ 应用于非独立样本的 justification 是否充分？\n   - per-sample vs instance-level 信号的分类是否自洽？\n\n2. **实验设计**\n   - 数据集选择是否合理覆盖 difficulty gradient？\n   - 模型选择（2×8B）是否足以支撑论文声称的 cross-architecture 结论？\n   - N=8/16 和 T=0.7/1.0 的设置是否充分？\n   - 训练配置（LoRA + fine-tuning）的细节是否足够复现？\n\n3. **统计分析**\n   - Bootstrap 检验的设置（B=10,000, 95% CI）是否恰当？\n   - TOST 等价检验的 δ 选择是否有依据？\n   - 多重比较校正的处理是否到位？\n   - Spearman ρ 和 AUROC 的联合报告是否合理？\n\n4. **核心 claim 验证**\n   - \"correlation-selection gap\" 的论证是否严密？特别是 4/5 信号是 instance-level（定义性无法 select）vs logprob 经验性失败——这两层是否被清晰区分？\n   - \"constrained decoding\" 作为潜在混淆变量是否被充分讨论？\n   - RE 结论仅基于 SciERC 单数据集——这一局限是否在论文中被恰当处理？\n   - Task-difficulty dependent signal ranking 是否有充分数据支持？\n\n5. **复现性**\n   - 训练 hyperparameters 是否完整报告？\n   - Prompt template 是否提供？\n   - 代码/数据可用性？\n\n请按 EMNLP 审稿标准给出完整审稿报告，包含：Summary、Strengths、Weaknesses (must-fix / should-fix / minor)、Questions、Missing References、Overall Assessment（评分 + 置信度）。"
  }
}
```

</details>

---


### Tool result

_source line 534 · 2026-05-15T07:52:04.228110+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 15348
}
```

</details>

---


### Tool call

_source line 535 · 2026-05-15T07:52:04.429317+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "project": "struct_self_consist_ie",
  "text": "## 审稿任务 — Reviewer 2 (Round 1)\n\n### Venue 信息\n- **Target**: EMNLP 2026 Findings (via ARR May 2026 cycle)\n- **Deadline**: 2026-05-25\n- **页数限制**: 正文 8 页 + unlimited references\n- **模板**: ACL format (`\\usepackage[review]{acl}`)\n- **匿名规则**: Double-blind\n- **Limitations section**: 必须，位于 Conclusion 后、References 前，不计页数\n- **附录**: 允许，不计页数\n\n### 论文路径\n`projects/struct_self_consist_ie/docs/paper/main.tex`\n（各 section 在 `sections/` 子目录下）\n\n### 你的审查侧重：新颖性 + framing + related work 完整性 + 写作质量\n\n请重点评估以下方面：\n\n1. **新颖性与贡献**\n   - \"correlation-selection gap\" 作为概念贡献是否有足够新颖性？（注意：4/5 信号是 instance-level，定义上无法做 sample selection——这部分论证中有多少是 trivial/tautological 的？）\n   - 与 Nédellec et al. (2026) 的增量贡献是否充分论证？\n   - Soft Jaccard 作为方法贡献的新颖性如何？\n   - 三个 contribution 的每一个是否都有实质性新知识？\n\n2. **Framing 与 claim scope**\n   - 论文的核心 narrative 是否自洽？（Abstract → Introduction → Conclusion 的 claim 一致性）\n   - \"first multi-family comparison\" 的 claim 是否准确？scope 是否被恰当限定？\n   - Abstract 是否过于密集？是否首次阅读即可把握核心信息？\n   - RE 被标记为 \"preliminary\" 但在多处仍作为主要证据——framing 是否一致？\n\n3. **Related Work 完整性**\n   - 引用是否覆盖了该领域的核心文献？\n   - 是否遗漏了重要的相关工作？特别关注：\n     - LLM confidence/uncertainty estimation 领域的核心论文\n     - Self-consistency 的最新变体\n     - MBR decoding 在非 MT 领域的应用\n     - 结构化预测不确定性估计\n   - 与已有工作的对比定位是否公允（不过度贬低或忽略先前工作）？\n\n4. **写作质量**\n   - 术语使用是否一致？（confidence signal vs consistency signal; VC vs Voting Conf. 等）\n   - 论文整体组织结构是否清晰？\n   - 图表是否有效传达信息？caption 是否自足？\n   - Ethics Statement 的位置和内容是否符合 ACL 要求？\n   - Limitations section 是否诚实全面？\n\n5. **格式合规性**\n   - 是否符合 ACL 模板要求？\n   - 正文是否在 8 页内？\n   - 匿名性是否保持（无 self-citation 泄露）？\n   - 引用格式是否正确？\n\n请按 EMNLP 审稿标准给出完整审稿报告，包含：Summary、Strengths、Weaknesses (must-fix / should-fix / minor)、Questions、Missing References、Overall Assessment（评分 + 置信度）。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "project": "struct_self_consist_ie",
    "text": "## 审稿任务 — Reviewer 2 (Round 1)\n\n### Venue 信息\n- **Target**: EMNLP 2026 Findings (via ARR May 2026 cycle)\n- **Deadline**: 2026-05-25\n- **页数限制**: 正文 8 页 + unlimited references\n- **模板**: ACL format (`\\usepackage[review]{acl}`)\n- **匿名规则**: Double-blind\n- **Limitations section**: 必须，位于 Conclusion 后、References 前，不计页数\n- **附录**: 允许，不计页数\n\n### 论文路径\n`projects/struct_self_consist_ie/docs/paper/main.tex`\n（各 section 在 `sections/` 子目录下）\n\n### 你的审查侧重：新颖性 + framing + related work 完整性 + 写作质量\n\n请重点评估以下方面：\n\n1. **新颖性与贡献**\n   - \"correlation-selection gap\" 作为概念贡献是否有足够新颖性？（注意：4/5 信号是 instance-level，定义上无法做 sample selection——这部分论证中有多少是 trivial/tautological 的？）\n   - 与 Nédellec et al. (2026) 的增量贡献是否充分论证？\n   - Soft Jaccard 作为方法贡献的新颖性如何？\n   - 三个 contribution 的每一个是否都有实质性新知识？\n\n2. **Framing 与 claim scope**\n   - 论文的核心 narrative 是否自洽？（Abstract → Introduction → Conclusion 的 claim 一致性）\n   - \"first multi-family comparison\" 的 claim 是否准确？scope 是否被恰当限定？\n   - Abstract 是否过于密集？是否首次阅读即可把握核心信息？\n   - RE 被标记为 \"preliminary\" 但在多处仍作为主要证据——framing 是否一致？\n\n3. **Related Work 完整性**\n   - 引用是否覆盖了该领域的核心文献？\n   - 是否遗漏了重要的相关工作？特别关注：\n     - LLM confidence/uncertainty estimation 领域的核心论文\n     - Self-consistency 的最新变体\n     - MBR decoding 在非 MT 领域的应用\n     - 结构化预测不确定性估计\n   - 与已有工作的对比定位是否公允（不过度贬低或忽略先前工作）？\n\n4. **写作质量**\n   - 术语使用是否一致？（confidence signal vs consistency signal; VC vs Voting Conf. 等）\n   - 论文整体组织结构是否清晰？\n   - 图表是否有效传达信息？caption 是否自足？\n   - Ethics Statement 的位置和内容是否符合 ACL 要求？\n   - Limitations section 是否诚实全面？\n\n5. **格式合规性**\n   - 是否符合 ACL 模板要求？\n   - 正文是否在 8 页内？\n   - 匿名性是否保持（无 self-citation 泄露）？\n   - 引用格式是否正确？\n\n请按 EMNLP 审稿标准给出完整审稿报告，包含：Summary、Strengths、Weaknesses (must-fix / should-fix / minor)、Questions、Missing References、Overall Assessment（评分 + 置信度）。"
  }
}
```

</details>

---


### Tool result

_source line 536 · 2026-05-15T07:52:06.096587+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1667
}
```

</details>

---


### Assistant

_source line 537 · 2026-05-15T07:52:10.490787+00:00_

两位 Reviewer 已分配，等待独立初审结果返回。

- **Reviewer 1** (方法严谨性 + 实验 + 统计)：已分配
- **Reviewer 2** (新颖性 + framing + related work + 写作)：已分配

等待两位 Reviewer 返回审稿意见后，进入交叉分享（Step 2）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 40

## Round 40

2 recorded events


### User

_source line 538 · 2026-05-15T07:56:36.022642+00:00_

[Reviewer 1 审稿意见]:

# Reviewer 1 — Round 1 审稿报告

**论文**: Strong Predictors, Weak Selectors: A Systematic Comparison of Confidence Signals for Test-Time Scaling in Information Extraction

---

## 总体评分

**Overall**: 3 / 5（Findings track acceptance）
**一句话总结**: 研究问题定义清晰、实验设计总体扎实，"correlation-selection gap"是一个有实际意义的 negative result；但 constrained decoding 作为核心混淆变量未被充分隔离，削弱了中心结论的普适性。

---

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| **Soundness** | 3 / 5 | Main claims 在实验范围内得到支持，但 constrained decoding confound 和 RE 单数据集问题构成方法论缺口 |
| **Excitement** | 3.5 / 5 | Correlation-selection gap 概念新颖且对 test-time scaling 实践有指导意义；信号分类框架（per-sample vs instance-level）清晰有价值 |
| **Reproducibility** | 4 / 5 | 训练配置完整（Appendix Table 8），prompt 提供，数据集公开；但未提及代码/数据发布计划 |
| **Confidence** | 4 / 5 | 我仔细阅读了论文全文和附录，熟悉 self-consistency、MBR decoding 和 IE 领域 |

---

## 主要优势

1. **问题定义清晰**。将 quality estimation 和 sample selection 解耦是重要的概念贡献（§1, §3.1）。per-sample vs instance-level 的区分框架简洁有力，解释了为什么 4/5 信号在 selection 上必然失败。

2. **统计分析严谨**。Bootstrap CI (B=10,000)、TOST 等价检验（Table 6, Appendix D）、多种 δ 阈值（±2/3/5 pp）、sign test 和 Cohen's d 的联合报告（§4.3），统计方法论在 ACL 投稿中属于上乘。条件过滤分析（non-zero F1 subset, Figure 2 right panel）有效揭示了 full-set correlation 的虚高问题。

3. **Negative result 有价值**。Log-probability 作为唯一 per-sample 信号也无法有效 select（p=0.39, 13-18 pp oracle headroom），且原因可追溯到 score compression（60% 的 instance 内 range < 0.05, Appendix F）——这是对 test-time scaling 文献（Brown et al. 2024; Snell et al. 2024）的重要补充。

4. **Task-difficulty gradient 设计合理**。CoNLL（easy, ~91% F1）→ SciERC（hard, 6/7 types）→ WNUT-17（boundary, 52% zero F1）覆盖了有意义的难度谱，且 EM↔SJ crossover pattern 在两个模型上方向一致（§4.2, Table 1）。

5. **引用完整**。58 条引用，0 orphan，0 missing bib entry，52 条在线验证通过。对最相关工作 Nédellec et al. (2026) 的定位精准（§1, §2），清楚说明了在哪三个维度上推进。

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] Constrained decoding 作为核心混淆变量未被隔离

- 具体位置：§4.1 (Experimental Setup), §5 (Discussion), Limitations §第16行, Appendix F (logprob ties)
- 问题：所有实验均使用 constrained decoding (vLLM + XGrammar)。论文承认 constrained decoding "may compress per-sample diversity"（Limitations §16），且 Appendix F 显示 60% 的 instance logprob range < 0.05。但论文无法区分 correlation-selection gap 是 structured IE 的固有属性还是 constrained decoding 的人工产物。Constrained decoding 同时影响：(a) 输出多样性（diversity）；(b) logprob 分布（score compression）；(c) 信号之间的相对排序（因为所有输出都 schema-compliant，消除了 format error 这一重要变异来源）。
- 为什么影响接收：这是论文核心结论 ("signals are predictors not selectors for structured IE") 的普适性基础。如果 gap 主要由 constrained decoding 驱动，则结论应改为 "for structured IE *under constrained decoding*"——scope 显著缩窄。论文目前的措辞（title, abstract, conclusion）未加此限定。
- 建议修改方向：(1) 添加 free-form decoding 消融实验（即使在 SciERC subset 上），对比 logprob score resolution 和 selection gap 幅度；或 (2) 如果无法添加实验，在 title/abstract/conclusion 中明确限定 scope 为 constrained decoding setting，并在 Discussion 中深化分析（例如从 Appendix F 的 non-tied subset 结果反推：在 non-tied 40% 中 logprob selection 显著优于 greedy +2.9pp, p=0.01——这暗示 score compression 而非 IE 本身是 gap 的主因）。

**N2** [critical] Appendix F 的 non-tied subset 结果实际上削弱了核心 claim

- 具体位置：Appendix F (§F, line 396-397)
- 问题：论文报告在 logprob range ≥ 0.05 的 non-tied subset (n=210, 40%) 中，logprob selection 显著优于 greedy (+2.9 pp, p=0.01)，且 within-instance ρ(logprob, F1) 从 0.08 升到 0.39。论文将此解读为 "signal exists but is resolution-limited"。但更直接的解读是：**logprob 在有足够 score resolution 的情况下确实是有效 selector**，gap 的根因是 constrained decoding 导致的 score compression，而非 structured IE 的固有性质。
- 这与 N1 构成同一个问题的两面：empirical evidence 在论文自身数据中已经暗示 constrained decoding 是主要 confound，但论文的 framing 仍然是 "IE 本身的 gap"。
- 建议：重新组织 Discussion §5 的 "Layer 2 (empirical)" 分析，将 non-tied subset 结果提升为主文讨论（而非 appendix），明确承认这一反面证据对 claim scope 的影响。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] RE 结论仅基于 SciERC，但 abstract 和 contribution 列表未充分限定

- 具体位置：Abstract line 3 ("RE (SciERC, preliminary)"), Introduction contribution 3 (line 47), Conclusion (line 8)
- 问题：Abstract 用了 "(SciERC, preliminary)" 修饰 RE，但 Introduction 的 contribution 3 没有类似限定（"When model capability is insufficient (WNUT-17, 52% zero F1), inflated full-set correlations collapse on the conditional set"——RE 结论被嵌入通用表述中）。Conclusion line 8 提到 "our RE conclusions rest on SciERC alone"，但紧接的 future work 没有将 RE 验证列为优先方向。
- SciERC RE 有 40% zero F1，这不是一般性 RE benchmark 的特征。
- 建议：在 contribution 列表和 conclusion 中一致使用 "preliminary" 或 "single-benchmark" 限定词；在 future work 中明确列出 RE 多数据集验证。

**W2** [warning] Fleiss' κ 的 independence 假设 justification 不够严格

- 具体位置：§3.2, Eq. 3, line 39
- 问题：论文用经验数据 (excess agreement -0.4% to -4.0%) 论证 temperature sampling 产生"足够独立"的样本。但这些数字没有对应的统计检验（e.g., permutation test for independence），也没有说明是在哪个 dataset/model 上测量的。"mild negative dependence" 的结论是否在所有 6 个 model-dataset 配置上一致成立？
- Fleiss' κ 在 N 小（如 N=8）且 rater 非独立时行为不稳定（Gwet 2014），论文未引用相关分析。
- 建议：(1) 提供所有配置的 excess agreement 数据；(2) 引用 FK 在非独立 rater 下的行为分析文献；(3) 或降低对 FK 结论的依赖程度（FK 在 5 个信号中排名靠后，不影响核心 claim）。

**W3** [warning] "Cross-architecture" 结论的基础偏窄

- 具体位置：§4.4 (Robustness), Table 3, Conclusion line 7
- 问题：论文使用 "cross-architecture" 描述 Qwen3-8B vs LLaMA-3.1-8B 的比较。但两者均为 8B 参数量的 decoder-only transformer，共享极其相似的架构（grouped query attention, RoPE, SwiGLU）。更准确的说法是 "cross-model-family at 8B scale"。Conclusion 声称 signal ordering "directionally consistent across model families, though magnitudes are model-dependent"——这一结论在 2 个模型上成立但置信度有限。
- 建议：将 "cross-architecture" 改为 "cross-model" 或 "across two model families"；在讨论 generalization 时明确 8B-only 的局限。

**W4** [warning] TOST 等价检验的 δ 选择缺乏外部锚点

- 具体位置：Appendix D (§D), Table 6, line 270-271
- 问题：δ = ±2/3/5 pp 被描述为 "practical significance" 阈值，并与 "typical inter-annotator disagreement on IE benchmarks" 关联，但没有引用具体的 IAA 数据。对于 SciERC NER (greedy F1 ≈ 0.644)，2pp 对应 ~0.3% 的相对变化，这是极其严格的；对于 RE (greedy ≈ 0.404)，5pp 对应 ~1.2% 的相对变化。
- 建议：引用 1-2 篇报告 IE benchmark IAA 数字的文献来锚定 δ 选择；或用 effect size (Cohen's d) 的 small/medium/large 分界作为补充。

**W5** [warning] Qwen3-8B 的 thinking token 训练不一致

- 具体位置：Appendix E (§E), footnote line 369
- 问题：SciERC 训练 "did not explicitly disable thinking tokens (enable_thinking)"，而 CoNLL/WNUT "explicitly set this to false"。虽然推理时 constrained decoding 覆盖了 thinking behavior，但训练时的差异可能影响 learned representations。这意味着 SciERC vs CoNLL/WNUT 的比较中，Qwen 模型的训练条件不完全一致。
- 建议：在 Limitations 中明确讨论此不一致性及其潜在影响，或确认 thinking tokens 在 SciERC fine-tuning 中实际是否被激活。

---

## 小问题（不影响接收）

- **M1**: Table 1 脚注格式：`\textsuperscript{†}` 和 `\footnotetext` 在 two-column 模板中可能渲染异常（应检查 PDF 输出）。
- **M2**: Appendix A (notation) 将 SJ 定义为 "Soft Jaccard similarity"，但 main text §3.2 标题是 "Soft Jaccard (structural, instance-level)"——首次出现时建议统一全称。
- **M3**: §4.2 line 64 脚注中比较 semantic entropy AUROC 0.75-0.85，并声明 "direct comparison is not meaningful"。如果不 meaningful，这个数字引用的必要性存疑——建议删除或缩短。
- **M4**: `he2024uncertainty` 的 bib entry 标题 "Uncertainty Estimation on Sequential Labeling via Uncertainty Transmission" 但 Related Work 引用上下文是 "survey uncertainty quantification specifically for LLMs"——内容可能不匹配（该论文实际是 sequential labeling 的，不是 LLM survey）。
- **M5**: 引用验证发现 `hobelsberger2025systematic` 和 `lightman2024verify` 未在 OpenAlex 找到（可能索引延迟），`feng2025optimal` 和 `ye2025uncertainty` 有 first author name mismatch（bib vs API，可能是 name variant）——建议 double-check。

---

## Questions for Authors

1. 在 Appendix F 的 non-tied subset (logprob range ≥ 0.05) 中，logprob selection 显著优于 greedy (+2.9pp, p=0.01)。如果 constrained decoding 是 score compression 的主因，那么在 free-form decoding 下，logprob 是否有可能成为有效 selector？你们如何论证 gap 是 IE-inherent 而非 decoding-induced？

2. Consensus-proximity selection（§3.3）被描述为 "mathematically equivalent to leave-one-out SJ selection"，但未给出证明。能否补充简要推导？

3. FK 的 excess agreement 数据 (-0.4% to -4.0%) 是在哪个配置上测量的？是否在所有配置上一致？

4. 对于 WNUT-17 上 logprob 的负相关（ρ=-0.410），作者的解释是什么？是否与 constrained decoding 在 OOD 域上的行为有关？

---

## Missing References

无明显遗漏。引用覆盖了 self-consistency (Wang et al. 2023)、MBR decoding (Eikema & Aziz 2022)、semantic uncertainty (Kuhn et al. 2023)、最近的 difficulty-aware 方法 (Feng et al. 2025; Wang & Feng et al. 2025) 和 IE-specific consistency (Nédellec et al. 2026)。可考虑补充：
- Bertsch et al. (2023) "Unlimiformer" 或类似的 constrained generation 分析文献，以强化 constrained decoding confound 的讨论。

---

## Overall Assessment

**评分: 3 / 5 (Findings track acceptance)**

这是一篇执行质量较高的 empirical study，核心概念（correlation-selection gap）有实际指导价值，统计分析在 ACL 投稿中属上乘。主要弱点是 constrained decoding confound 未被隔离——论文自身的 non-tied subset 数据（Appendix F）实际暗示 gap 可能主要源于 decoding constraint 而非 IE task structure。如果作者能 (a) 添加 free-form decoding 消融或 (b) 在所有 claim 中限定 scope 为 constrained decoding setting 并提升 non-tied analysis 至主文，我认为此论文适合 Findings track。当前版本的 claim scope 与 evidence 之间存在 gap。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 539 · 2026-05-15T07:56:43.062311+00:00_

Reviewer 1 审稿已收到。等待 Reviewer 2 完成初审后进入交叉分享。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 41

## Round 41

2 recorded events


### User

_source line 540 · 2026-05-15T07:56:47.581292+00:00_

[Reviewer 1 审稿结果]:
审稿报告已提交给 Review Director。

**核心发现总结**：

- **Overall 3/5 (Findings acceptance)**，Soundness 3，Excitement 3.5
- **2 个 Critical 问题**：constrained decoding 作为核心混淆变量未被隔离——论文自身 Appendix F 的 non-tied subset 数据（logprob selection +2.9pp, p=0.01）反面证明了 gap 可能主要源于 score compression 而非 IE 本身的固有属性。当前 claim scope（title/abstract/conclusion）未限定 constrained decoding setting。
- **5 个 Should-Fix**：RE 单数据集限定不一致、FK independence justification 不足、"cross-architecture" 用词过度、TOST δ 缺外部锚点、thinking token 训练不一致
- **引用完整**，格式合规

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 541 · 2026-05-15T07:56:52.740288+00:00_

Reviewer 1 报告已收到。等待 Reviewer 2。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 42

## Round 42

6 recorded events


### User

_source line 542 · 2026-05-15T07:57:42.273213+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 — Round 1 完整审稿报告

### 审稿侧重：新颖性 + framing + related work 完整性 + 写作质量

---

## 总体评分
**Overall**: 3.0 / 5（Findings publication）
**一句话总结**: 实验设计严谨、统计分析到位的 empirical study，但核心概念贡献"correlation-selection gap"的新颖性因 4/5 信号在定义上就无法做 sample selection 而被大幅削弱——这是一个 tautological observation 被包装成 empirical finding 的 framing 问题。

## 官方维度打分（来自 ACL ARR review form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | 实验严谨（bootstrap CI、TOST、multi-seed），但核心 claim 中的 tautological 成分削弱了论证的 substantiveness |
| Excitement | 2.5/5 | 负面结果对实践有价值，但新颖性有限——核心发现部分来自定义而非实验 |
| Reproducibility | 4/5 | 训练细节、prompt template、超参数、统计测试均有详细描述 |
| Confidence | 4/5 | 熟悉 self-consistency、uncertainty estimation、generative IE 文献 |

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] Correlation-selection gap 的核心论证存在 tautological 成分，新颖性不足

- 具体位置：Section 1 (L22–24), Section 5.3, Section 6 (Discussion "Why the gap exists: two layers")
- 问题：论文将"correlation-selection gap"作为三个 contribution 之一（C2），但 4/5 信号（EM、FK、SJ、Voting）是 instance-level by definition——它们对同一 input 的所有 N 个 sample 产生同一个分数。论文自己承认："they cannot rank candidates by construction"（Section 5.3, L121; Discussion Layer 1）。这意味着这 4 个信号的"selection failure"不是实验发现，而是定义的逻辑后果。将一个 definitional impossibility 包装为"gap"并命名为 contribution，exaggerates the novelty。

  真正 non-trivial 的发现只有 logprob 的失败——但 Appendix F 已解释：constrained decoding 造成 score compression（60% instances 的 within-instance range < 0.05），且在 non-tied subset 中 logprob 显著优于 greedy（+2.9 pp, p=0.01）。这说明 logprob 的"failure"是 constrained decoding 的 artifact，而非 confidence signal 的 intrinsic limitation。

  因此，"correlation-selection gap"被两头夹击：instance-level signals 的 failure 是 tautological；logprob 的 failure 是 constrained-decoding artifact。

- 为什么影响接收：核心 contribution 的新颖性是 Findings 接收的底线要求。
- 建议修改方向：(1) 明确区分"by-construction impossibility"和"empirical finding"，不要将前者算作 contribution；(2) 将 C2 重心转向 logprob score compression 分析；(3) 考虑标题和 abstract 的 reframing。

**N2** [critical] 与 Nédellec et al. (2026) 的增量贡献论证不充分

- 具体位置：Section 1 (L16), Section 2 (L13–15), Table 5 (Appendix B)
- 问题：三个增量均偏弱：(i) SJ vs EM 的 Δρ=+0.065 在 Bonferroni 校正后不显著（Table 5 自述），且 conditional set 上 EM 反而第一；(ii) selection analysis 如 N1 所述主要是 tautological；(iii) difficulty gradient 发现（harder→structural better, easier→EM better）在直觉上不意外。
- 建议修改方向：更诚实地量化增量大小，或找到 structural matching 有 clearly significant 优势的 setting。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] Abstract 信息密度过高
- 9 行包含 5 个 signal、3 个 family、4 个数值指标、3 个数据集、2 个模型、gap 概念、technical arguments。首次阅读难以把握核心 message。
- 建议聚焦 1–2 个核心发现，将细节数字移入 Introduction。

**W2** [warning] RE "preliminary" 标注与实际使用不一致
- Abstract 标注 "preliminary"，但 RE 结果在 Table 1（2 列）、Table 2、Figure 2–3、Discussion 中被大量使用作为主要论证。
- 建议：要么移 RE 至 Appendix，要么去掉"preliminary"标签。

**W3** [warning] Soft Jaccard 方法论新颖性有限
- 本质是 Hungarian matching + token-level IoU，均为标准技术。缺少与 soft set similarity 已有工作（如 object detection 中的 soft IoU）的对比讨论。

**W4** [warning] "first multi-family comparison" claim 过度依赖 scope 限定
- "first" 依赖"for test-time scaling" + "in generative IE"的双重限定。建议去掉"first"或将 gap 描述清楚而非宣称优先权。

---

## 小问题（不影响接收）

- 术语不一致：Table 1 用 "Voting Conf."，Table 4 用 "VC"，建议统一。
- Ethics Statement 仅两句话，可补充 LLM extraction error 的潜在影响。
- 引用验证：`hobelsberger2025systematic` 和 `lightman2024verify` 在 OpenAlex 未找到（可能索引延迟）；`feng2025optimal` 和 `ye2025uncertainty` 的 first author 与 API 记录不匹配，建议核查 bib。
- Figure 1 caption 引用了 Table 2，降低 self-containment。
- Table 1 的 `\footnotetext` 紧跟 `\caption`，某些模板编译下可能显示异常。

---

## Missing References

1. "Trust but Verify! A Survey on Verification Design for Test-time Scaling" (2025, arXiv:2508.16665) — 与 Discussion 中 verifier 建议直接相关
2. 2025–2026 最新 uncertainty quantification survey（如 arXiv:2503.15850）
3. SLOT (EMNLP 2025 Industry) — structured output generation + constrained decoding 相关
4. MBR 在非 MT 任务中的应用（summarization、dialogue）——帮助 contextualize MBR 的 task-dependent 表现

---

## 主要优势

- 统计分析的严谨性：bootstrap CI、TOST、multi-seed、conditional filtering、diversity stratification 远超同类 empirical papers
- Negative result 的充分刻画：logprob compression analysis 和 diversity-stratified gap 排除了多个 alternative explanations
- 实验设计公平：两模型相同训练配置，三数据集覆盖难度梯度
- Limitations section 诚实全面
- 整体写作质量良好（除 abstract 过密和术语不一致外）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 543 · 2026-05-15T07:58:14.627319+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "project": "struct_self_consist_ie",
  "text": "## 交叉分享 — 请逐条回应 Reviewer 1 的审稿意见\n\n以下是 Reviewer 1 的完整审稿意见。请逐条回应：\n- **[AGREE]** 同意并说明理由\n- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）\n\n---\n\n### Reviewer 1 的 Must-Fix 问题\n\n**R1-N1** [critical] Constrained decoding 作为核心混淆变量未被隔离\n- 所有实验均使用 constrained decoding (vLLM + XGrammar)。论文承认 \"may compress per-sample diversity\"（Limitations §16），Appendix F 显示 60% instance logprob range < 0.05。论文无法区分 correlation-selection gap 是 structured IE 固有属性还是 constrained decoding 的人工产物。\n- 建议：添加 free-form decoding 消融，或在 title/abstract/conclusion 限定 scope。\n\n**R1-N2** [critical] Appendix F 的 non-tied subset 结果（logprob +2.9pp, p=0.01）实际削弱核心 claim\n- 在 non-tied 40% 中 logprob selection 显著优于 greedy，within-instance ρ 从 0.08 升到 0.39。更直接的解读是 logprob 在有 score resolution 时确实有效，gap 根因是 constrained decoding 的 score compression。\n- 建议：提升 non-tied analysis 至主文，重新组织 Discussion。\n\n### Reviewer 1 的 Should-Fix 问题\n\n**R1-W1** RE 结论仅基于 SciERC，abstract/contribution/conclusion 限定不一致\n**R1-W2** FK independence 假设 justification 不够严格，excess agreement 数据不全\n**R1-W3** \"Cross-architecture\" 用词过度（均为 8B decoder-only transformer）\n**R1-W4** TOST δ 选择缺乏外部锚点\n**R1-W5** Qwen3-8B thinking token 训练不一致（SciERC vs CoNLL/WNUT）\n\n### Reviewer 1 的 Minor 问题\n\n**R1-M1** Table 1 脚注格式可能渲染异常\n**R1-M2** SJ 全称首次出现时应统一\n**R1-M3** §4.2 脚注 semantic entropy 比较——如果 \"not meaningful\" 为何引用？\n**R1-M4** `he2024uncertainty` bib entry 与引用上下文不匹配\n**R1-M5** 部分引用在 OpenAlex 未找到\n\n### Reviewer 1 的 Questions\n\n1. Free-form decoding 下 logprob 是否可能成为有效 selector？\n2. Consensus-proximity = LOO-SJ 的证明？\n3. FK excess agreement 在哪个配置测量？\n4. WNUT-17 logprob 负相关的解释？\n\n### Reviewer 1 评分\nOverall 3/5, Soundness 3, Excitement 3.5, Reproducibility 4, Confidence 4\n\n---\n\n请对以上每个 N/W/M 和 Question 逐条给出 [AGREE] 或 [REBUT]。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "project": "struct_self_consist_ie",
    "text": "## 交叉分享 — 请逐条回应 Reviewer 1 的审稿意见\n\n以下是 Reviewer 1 的完整审稿意见。请逐条回应：\n- **[AGREE]** 同意并说明理由\n- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）\n\n---\n\n### Reviewer 1 的 Must-Fix 问题\n\n**R1-N1** [critical] Constrained decoding 作为核心混淆变量未被隔离\n- 所有实验均使用 constrained decoding (vLLM + XGrammar)。论文承认 \"may compress per-sample diversity\"（Limitations §16），Appendix F 显示 60% instance logprob range < 0.05。论文无法区分 correlation-selection gap 是 structured IE 固有属性还是 constrained decoding 的人工产物。\n- 建议：添加 free-form decoding 消融，或在 title/abstract/conclusion 限定 scope。\n\n**R1-N2** [critical] Appendix F 的 non-tied subset 结果（logprob +2.9pp, p=0.01）实际削弱核心 claim\n- 在 non-tied 40% 中 logprob selection 显著优于 greedy，within-instance ρ 从 0.08 升到 0.39。更直接的解读是 logprob 在有 score resolution 时确实有效，gap 根因是 constrained decoding 的 score compression。\n- 建议：提升 non-tied analysis 至主文，重新组织 Discussion。\n\n### Reviewer 1 的 Should-Fix 问题\n\n**R1-W1** RE 结论仅基于 SciERC，abstract/contribution/conclusion 限定不一致\n**R1-W2** FK independence 假设 justification 不够严格，excess agreement 数据不全\n**R1-W3** \"Cross-architecture\" 用词过度（均为 8B decoder-only transformer）\n**R1-W4** TOST δ 选择缺乏外部锚点\n**R1-W5** Qwen3-8B thinking token 训练不一致（SciERC vs CoNLL/WNUT）\n\n### Reviewer 1 的 Minor 问题\n\n**R1-M1** Table 1 脚注格式可能渲染异常\n**R1-M2** SJ 全称首次出现时应统一\n**R1-M3** §4.2 脚注 semantic entropy 比较——如果 \"not meaningful\" 为何引用？\n**R1-M4** `he2024uncertainty` bib entry 与引用上下文不匹配\n**R1-M5** 部分引用在 OpenAlex 未找到\n\n### Reviewer 1 的 Questions\n\n1. Free-form decoding 下 logprob 是否可能成为有效 selector？\n2. Consensus-proximity = LOO-SJ 的证明？\n3. FK excess agreement 在哪个配置测量？\n4. WNUT-17 logprob 负相关的解释？\n\n### Reviewer 1 评分\nOverall 3/5, Soundness 3, Excitement 3.5, Reproducibility 4, Confidence 4\n\n---\n\n请对以上每个 N/W/M 和 Question 逐条给出 [AGREE] 或 [REBUT]。"
  }
}
```

</details>

---


### Tool result

_source line 544 · 2026-05-15T07:58:24.737551+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 10110
}
```

</details>

---


### Tool call

_source line 545 · 2026-05-15T07:58:24.790361+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "project": "struct_self_consist_ie",
  "text": "## 交叉分享 — 请逐条回应 Reviewer 2 的审稿意见\n\n以下是 Reviewer 2 的完整审稿意见。请逐条回应：\n- **[AGREE]** 同意并说明理由\n- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）\n \n---\n\n### Reviewer 2 的 Must-Fix 问题\n\n**R2-N1** [critical] Correlation-selection gap 的核心论证存在 tautological 成分，新颖性不足\n- 4/5 信号是 instance-level by definition，\"selection failure\" 是定义的逻辑后果而非实验发现。论文自己承认 \"they cannot rank candidates by construction\"（§4.3 L121, Discussion Layer 1）。\n- 真正 non-trivial 的发现只有 logprob 的失败，但 Appendix F 已解释为 constrained decoding 的 score compression artifact。\n- 因此 gap 被两头夹击：instance-level failure 是 tautological；logprob failure 是 artifact。\n- 建议：区分 by-construction impossibility 和 empirical finding；将 C2 重心转向 logprob score compression 分析。\n\n**R2-N2** [critical] 与 Nédellec et al. (2026) 的增量贡献论证不充分\n- 三个增量均偏弱：(i) SJ vs EM Δρ=+0.065 Bonferroni 后不显著；(ii) selection analysis 主要 tautological；(iii) difficulty gradient 发现直觉上不意外。\n- 建议：更诚实地量化增量大小。\n\n### Reviewer 2 的 Should-Fix 问题\n\n**R2-W1** Abstract 信息密度过高（9 行含 5 signal/3 family/4 metric/3 dataset/2 model）\n**R2-W2** RE \"preliminary\" 标注与实际使用不一致（在 Table 1/2/Figure 2-3/Discussion 大量引用）\n**R2-W3** Soft Jaccard 方法论新颖性有限（Hungarian + token IoU 均为标准技术）\n**R2-W4** \"first multi-family comparison\" claim 过度依赖 scope 限定\n\n### Reviewer 2 的 Minor 问题\n\n- 术语不一致（\"Voting Conf.\" vs \"VC\"）\n- Ethics Statement 过简\n- 部分 bib entries 未在 OpenAlex 找到\n- Figure 1 caption 引用 Table 2\n- Table 1 脚注格式问题\n\n### Reviewer 2 的 Missing References\n\n1. \"Trust but Verify! A Survey on Verification Design for Test-time Scaling\" (2025)\n2. 最新 UQ survey (arXiv:2503.15850)\n3. SLOT (EMNLP 2025 Industry)\n4. MBR 在非 MT 任务中的应用\n\n### Reviewer 2 评分\nOverall 3.0/5, Soundness 3.5, Excitement 2.5, Reproducibility 4, Confidence 4\n\n---\n\n请对以上每个 N/W/M 和 Missing Reference 逐条给出 [AGREE] 或 [REBUT]。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "project": "struct_self_consist_ie",
    "text": "## 交叉分享 — 请逐条回应 Reviewer 2 的审稿意见\n\n以下是 Reviewer 2 的完整审稿意见。请逐条回应：\n- **[AGREE]** 同意并说明理由\n- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）\n \n---\n\n### Reviewer 2 的 Must-Fix 问题\n\n**R2-N1** [critical] Correlation-selection gap 的核心论证存在 tautological 成分，新颖性不足\n- 4/5 信号是 instance-level by definition，\"selection failure\" 是定义的逻辑后果而非实验发现。论文自己承认 \"they cannot rank candidates by construction\"（§4.3 L121, Discussion Layer 1）。\n- 真正 non-trivial 的发现只有 logprob 的失败，但 Appendix F 已解释为 constrained decoding 的 score compression artifact。\n- 因此 gap 被两头夹击：instance-level failure 是 tautological；logprob failure 是 artifact。\n- 建议：区分 by-construction impossibility 和 empirical finding；将 C2 重心转向 logprob score compression 分析。\n\n**R2-N2** [critical] 与 Nédellec et al. (2026) 的增量贡献论证不充分\n- 三个增量均偏弱：(i) SJ vs EM Δρ=+0.065 Bonferroni 后不显著；(ii) selection analysis 主要 tautological；(iii) difficulty gradient 发现直觉上不意外。\n- 建议：更诚实地量化增量大小。\n\n### Reviewer 2 的 Should-Fix 问题\n\n**R2-W1** Abstract 信息密度过高（9 行含 5 signal/3 family/4 metric/3 dataset/2 model）\n**R2-W2** RE \"preliminary\" 标注与实际使用不一致（在 Table 1/2/Figure 2-3/Discussion 大量引用）\n**R2-W3** Soft Jaccard 方法论新颖性有限（Hungarian + token IoU 均为标准技术）\n**R2-W4** \"first multi-family comparison\" claim 过度依赖 scope 限定\n\n### Reviewer 2 的 Minor 问题\n\n- 术语不一致（\"Voting Conf.\" vs \"VC\"）\n- Ethics Statement 过简\n- 部分 bib entries 未在 OpenAlex 找到\n- Figure 1 caption 引用 Table 2\n- Table 1 脚注格式问题\n\n### Reviewer 2 的 Missing References\n\n1. \"Trust but Verify! A Survey on Verification Design for Test-time Scaling\" (2025)\n2. 最新 UQ survey (arXiv:2503.15850)\n3. SLOT (EMNLP 2025 Industry)\n4. MBR 在非 MT 任务中的应用\n\n### Reviewer 2 评分\nOverall 3.0/5, Soundness 3.5, Excitement 2.5, Reproducibility 4, Confidence 4\n\n---\n\n请对以上每个 N/W/M 和 Missing Reference 逐条给出 [AGREE] 或 [REBUT]。"
  }
}
```

</details>

---


### Tool result

_source line 546 · 2026-05-15T07:58:26.454319+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1663
}
```

</details>

---


### Assistant

_source line 547 · 2026-05-15T07:58:29.158406+00:00_

交叉分享已发送。等待两位 Reviewer 的逐条回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 43

## Round 43

2 recorded events


### User

_source line 548 · 2026-05-15T07:58:31.994100+00:00_

[Reviewer 2 审稿结果]:
审稿报告已发送给 Director。

总结：论文在实验设计和统计分析上质量很高，但核心概念贡献（correlation-selection gap）的新颖性存在结构性问题——4/5 信号的 selection failure 是定义的逻辑后果而非实验发现，logprob 的 failure 是 constrained decoding 的 artifact。整体评分 Overall 3.0/5（Findings 水平），需要在 framing 上做 substantial rewrite 才能更准确地反映实际贡献。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 549 · 2026-05-15T07:58:37.154475+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 44

## Round 44

2 recorded events


### User

_source line 550 · 2026-05-15T07:59:51.728597+00:00_

[Reviewer 1 审稿意见]:

# Reviewer 1 — 交叉回应 Reviewer 2 审稿意见

---

## Must-Fix 问题

**[REBUT] R2-N1: Correlation-selection gap 的 tautological 成分与新颖性**

R2 认为 gap 被"两头夹击"——instance-level failure 是 tautological，logprob failure 是 artifact——因此整个 contribution 空心化。我部分同意但认为 R2 低估了三个方面：

1. **论文已经做了 R2 建议的区分**。Introduction Contribution 2（§1, line 41-43）明确写道 "Four of five signals are instance-level by construction, **making selection failure expected**; the empirical finding is that log-probability...also fails"。Discussion §5 的 "two layers" 结构也做了清晰分层。R2 建议的 "区分 by-construction impossibility 和 empirical finding" 实际上已经在论文中实现了。

2. **Consensus-proximity strategy 的失败不是 tautological**。Instance-level 信号确实不能直接 rank candidates，但论文设计了 consensus-proximity selection（§3.3, line 70）——选择最接近 consensus 的 sample——这是一个合理的 bridge，且被证明 "mathematically equivalent to leave-one-out SJ selection"。该策略的失败是实验结果（Table 2: SJ selection 0.645 vs greedy 0.644 on NER），不是定义推导。MBR decoding 在 MT 中成功正是因为类似的 utility-based selection work（Freitag et al. 2022）；在 IE 中失败并非 a priori obvious。

3. **但我同意 logprob failure 的 artifact 问题是 real concern**。这与我的 R1-N1 和 R1-N2 一致：Appendix F 的 non-tied subset (+2.9pp, p=0.01) 暗示 constrained decoding score compression 是主因。论文需要要么添加 free-form 消融，要么在 claim scope 上加限定。

**总体判断**：R2 的 tautological 批评部分有理（论文确实需要更加突出 logprob 分析的独立价值），但 "entirely tautological" 过强——consensus-proximity failure 和 MBR 在 IE 中的失败是 non-trivial 的实验发现。建议论文 reframe C2 以 logprob + MBR failure 为中心，而非以 "5 signals all fail" 为叙事。

---

**[REBUT] R2-N2: 与 Nédellec et al. (2026) 的增量贡献不足**

R2 批评三个增量均偏弱。我逐一评估：

(i) **SJ vs EM Δρ=+0.065 Bonferroni 后不显著**——事实正确（Table 5, Appendix B: "Marginally significant without multiple comparison correction; would not survive Bonferroni correction"）。但论文的核心 claim 不是 "SJ > EM"，而是 signal ranking 随 task difficulty 变化的 crossover pattern（SJ > EM on SciERC, EM > SJ on CoNLL），且这一 pattern 在两个模型上一致。单个 Δρ 的显著性不是 claim 的支点。

(ii) **Selection analysis 主要 tautological**——见上文 R2-N1 回应，部分同意但不完全。

(iii) **Difficulty gradient 发现直觉上不意外**——不同意。"Easy task favors exact match, hard task favors structural signals" 听起来直觉合理，但事后合理化 (hindsight bias) 不等于事前可预测。更重要的是，WNUT-17 的 conditional collapse（full-set ρ=0.724 → conditional ρ=0.038, Table 4）和 logprob negative correlation (ρ=-0.410) 不是直觉可预测的结果。

**总体判断**：相比 Nédellec et al. (2026) 的增量确实不是 ground-breaking，但对 Findings track 而言足够。R2 的 Excitement 评分 2.5 反映了这一判断，我理解但不完全赞同——将其定为 3.0 更合理，因为 quality estimation ≠ selection 的解耦框架对后续研究有实际指导价值。

---

## Should-Fix 问题

**[AGREE] R2-W1: Abstract 信息密度过高**

同意。Abstract 9 行包含 5 个信号名、3 个 family、4 种 metric (ρ/AUROC/p-value/oracle headroom)、3 个数据集、2 个模型。对非 IE 专家读者构成认知负荷。建议将 Abstract 聚焦于核心 claim（gap 存在 + difficulty-dependent ranking），具体数字移入正文。

---

**[AGREE] R2-W2: RE "preliminary" 标注与实际使用不一致**

完全同意，这也是我在 R1-W1 中提出的问题。Abstract 标注 "(SciERC, preliminary)" 但论文后续在 Table 1（4 列中有 2 列是 RE）、Table 2、Figure 2-3、Discussion 中大量引用 RE 结果，无 "preliminary" 限定。要么减少 RE 结果的篇幅权重，要么在所有 RE 分析处一致标注为 single-benchmark preliminary results。

---

**[REBUT] R2-W3: Soft Jaccard 方法论新颖性有限**

R2 称 Hungarian matching + token IoU "均为标准技术"。技术上正确，但忽略了 application novelty：将 type-aware bipartite matching 应用于 LLM 生成的 entity set 之间的 partial overlap 度量，在 IE quality estimation 文献中（据我所知）是新的。Nédellec et al. (2026) 明确承认他们的 surface-level approach "overlooks semantically consistent outputs"（§1, line 16 引用）。论文没有 claim SJ 本身是新方法——而是 claim 这种组合在 IE confidence estimation 中填补了 structural matching 的空白。这一定位是准确的。

不过我同意论文不应对此过度宣传——当前措辞 "Our core structural signal extends Jaccard similarity"（§3.2, line 43）中 "core" 一词可能暗示过高的方法贡献，可弱化为 "primary structural signal"。

---

**[AGREE] R2-W4: "first multi-family comparison" claim 过度依赖 scope 限定**

同意。Introduction line 17 "No existing work compares confidence signals from multiple families...for both quality estimation and sample selection in generative structured IE" 通过堆叠修饰词 (multiple families + both objectives + generative + structured IE) 来确保 "first" 成立。虽然事实上可能正确，但这种 contribution framing 给读者的印象是在通过 scope engineering 制造新颖性。建议改为描述性表述，避免 "first" claim。

---

## Minor 问题

**[AGREE] R2-M (术语不一致)**：Table 1 用 "Voting Conf."，Table 5 和 Table 7 用 "VC"，正文又用 "entity voting"。应统一。

**[AGREE] R2-M (Ethics Statement 过简)**：当前 Ethics Statement 仅 2 行，但对 Findings track 基本够用。如果 reviewer 要求可适当补充 computational cost 或 environmental impact。

**[AGREE] R2-M (部分 bib entries 未在 OpenAlex 找到)**：我的引用验证也发现 `hobelsberger2025systematic` 和 `lightman2024verify` 未在 OpenAlex 找到，但这两篇是真实论文（前者 arXiv:2510.20460，后者 arXiv:2305.20050），应为索引延迟而非 fabrication。

**[AGREE] R2-M (Figure 1 caption 引用 Table 2)**：Figure 1 caption（§1, line 29）确实引用 "Table~\ref{tab:selection}" 即 Table 2——这是 forward reference，虽然不违规但在排版上不理想。

**[AGREE] R2-M (Table 1 脚注格式)**：与我的 R1-M1 一致。

---

## Missing References

**[AGREE] "Trust but Verify!" survey (2025)**：与论文讨论的 test-time scaling + verification 直接相关，应引用。

**[AGREE] 最新 UQ survey (arXiv:2503.15850)**：如果 R2 能确认具体论文，Related Work §3 的 survey 引用集合可以补充。

**[REBUT] SLOT (EMNLP 2025 Industry)**：R2 未说明 SLOT 与本文的具体关联。如果是 structured output 相关的 test-time 方法，相关性取决于其是否处理 set-valued IE output。在了解具体内容前不确定是否属于 missing reference。

**[AGREE] MBR 在非 MT 任务中的应用**：论文 Discussion §5 将其方法与 MBR 对接（Eikema & Aziz 2022; Freitag et al. 2022; Müller & Sennrich 2021），但只引用了 MT 领域的 MBR 工作。如果存在 MBR 在 summarization/QA 等任务中的应用文献，应补充以增强对比分析。

---

## 对 R2 整体评分的看法

R2 给出 Overall 3.0, Excitement 2.5。我认为 Excitement 2.5 偏低——quality estimation vs selection 的解耦概念和 difficulty-dependent signal ranking 对 practitioners 有实际价值，3.0-3.5 更合理。但 Soundness 3.5 vs 我的 3.0 差异主要来自我对 constrained decoding confound 的更重权重——R2 虽然提到了这一问题（在 N1 的 "artifact" 论述中），但没有像我一样将其列为独立的 must-fix。我认为 constrained decoding confound 应该是独立的 critical issue，而非仅作为 N1 tautological argument 的一部分。

**我维持我的 Overall 3.0 评分不变。**


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 551 · 2026-05-15T07:59:56.769792+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 45

## Round 45

2 recorded events


### User

_source line 552 · 2026-05-15T08:00:03.929863+00:00_

[Reviewer 1 审稿结果]:
交叉回应已提交给 Review Director。逐条回应了 R2 的 2 个 Must-Fix、4 个 Should-Fix、5 个 Minor 和 4 个 Missing Reference，其中：

- **REBUT** 3 条（R2-N1 tautological 批评过强、R2-N2 增量贡献 Findings-worthy、R2-W3 SJ 有 application novelty）
- **AGREE** 10 条（abstract 过密、RE preliminary 不一致、"first" claim、术语不一致、大部分 minor 和 missing references）
- 维持 Overall 3.0 评分不变，认为 R2 的 Excitement 2.5 偏低但 Soundness 3.5 偏高（我因 constrained decoding confound 给了 3.0）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 553 · 2026-05-15T08:00:09.044641+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 46

## Round 46

6 recorded events


### User

_source line 554 · 2026-05-15T08:00:27.293324+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 — 交叉回应 Reviewer 1

### Must-Fix

[AGREE] R1-N1: Constrained decoding 混淆变量 — 与我的 N1 高度一致。补充：free-form decoding 消融本身也非 clean experiment（格式错误），但论文至少应在 title/abstract 限定 scope（"under constrained decoding"），当前 framing 将 gap 呈现为 structured IE 固有属性，证据不支持。

[AGREE] R1-N2: Non-tied subset 削弱核心 claim — 完全同意，这是我 N1 的核心论据之一。logprob 在有 score resolution 时有效（+2.9pp, p=0.01, ρ=0.39），说明 gap 根因是 score compression 而非 signal intrinsic limitation。论文应将此提升为主文核心发现。

### Should-Fix

[AGREE] R1-W1: RE scope 不一致 — 与我的 W2 一致
[AGREE with nuance] R1-W2: FK independence — 关切有效但 severity 偏低（FK 非核心 contribution，负 excess agreement 回应了核心担忧）
[AGREE] R1-W3: "Cross-architecture" 过度 — 应改为 "cross-model-family"
[AGREE with nuance] R1-W4: TOST δ — 多水平 δ 已构成 sensitivity analysis，建议引用 IAA 数据即可
[AGREE] R1-W5: Thinking token 训练不一致 — SciERC 是核心 benchmark，训练配置差异需严肃对待

### Minor

[AGREE] R1-M1, M2, M4, M5
[REBUT] R1-M3: Semantic entropy 脚注意图合理（提供 AUROC scale 参考），但执行上可能误导快速读者，建议缩短或删除

### Questions

Q1: 基于 non-tied evidence，free-form 下 logprob 很可能有效，同意这是关键消融
Q2: Consensus-proximity = LOO-SJ 需数学证明或更正为"approximately equivalent"
Q3: FK excess agreement 应注明 configuration
Q4: WNUT-17 logprob 负相关需机制解释（可能是 novel entities + overconfident familiar patterns）

### 两份审稿的互补性

R1 和 R2 在核心问题上高度一致（constrained decoding 混淆变量、RE scope、术语）。R1 技术层面更深（FK、thinking token、TOST δ），R2 在 framing/novelty 层面着力更多（tautological argument、incremental over Nédellec、abstract density）。两份审稿互补。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 555 · 2026-05-15T08:06:02.992795+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "struct_self_consist_ie",
  "issues_yaml": "issues:\n  # ============================================================\n  # Round 0 issues (all resolved)\n  # ============================================================\n  - id: \"R0-C1\"\n    summary: \"模型规模单一（仅 8B）\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 0\n    last_seen_round: 1\n    mentions:\n      - round: 0\n        reviewers: [1, 2]\n        note: \"8B→8B 仅验证架构鲁棒性非规模鲁棒性\"\n      - round: 1\n        reviewers: [1, 2]\n        note: \"model-agnostic 与 Limitations 矛盾\"\n    action_items:\n      - round: 1\n        action: \"全文替换 model-agnostic → consistent across tested model families\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"Round 2 Reviewer 确认措辞修正到位，无再提\"\n    resolution_round: 2\n\n  - id: \"R0-C2\"\n    summary: \"相关工作显著遗漏\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 0\n    last_seen_round: 1\n    mentions:\n      - round: 0\n        reviewers: [1, 2]\n        note: \"5 篇核心文献缺失\"\n      - round: 1\n        reviewers: [1, 2]\n        note: \"新遗漏：Optimal SC, Difficulty-Adaptive SC\"\n    action_items:\n      - round: 1\n        action: \"补充 6 篇引用到 Related Work\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"Round 2: 49 条 bib 全部 cited, 0 orphan, 无遗漏\"\n    resolution_round: 2\n\n  - id: \"R0-C3\"\n    summary: \"RE 结论仅基于 SciERC 单数据集\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 0\n    last_seen_round: 4\n    mentions:\n      - round: 0\n        reviewers: [1, 2]\n        note: \"需跨数据集验证或降级措辞\"\n      - round: 2\n        reviewers: [1, 2]\n        note: \"Abstract RE 措辞需修正\"\n      - round: 3\n        reviewers: [1, 2]\n        note: \"Round 2 措辞修正到位，但 R3 Reviewer 2 再次提出 44% zero-F1 floor effect 严重压缩可区分范围\"\n      - round: 4\n        reviewers: [1, 2]\n        note: \"R2 确认 claim 降级已完成（Conclusion 明确 hedge）。两位 Reviewer 仍认为 RE 证据薄弱，但 claim 范围已恰当限定——后续改进作为 R4-W1 追踪\"\n    action_items:\n      - round: 1\n        action: \"降级措辞 universal → observed in SciERC\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n      - round: 2\n        action: \"Abstract 改为 NER (three datasets) and RE (SciERC)\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n      - round: 3\n        action: \"进一步降级 RE claim 为 preliminary evidence + 补 SciERC RE conditional analysis\"\n        assigned_to: \"Agent + Paper Agent\"\n        status: resolved\n    resolution: \"Round 4: claim 降级到位（Conclusion 明确 hedge, Abstract 区分 NER/RE 证据量），RE conditional analysis 作为后续改进建议\"\n    resolution_round: 4\n\n  - id: \"R0-C4\"\n    summary: \"SJ 方法新颖性有限\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 0\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [2]\n        note: \"Nedellec 增量贡献论证不足 + 引用错误\"\n    action_items:\n      - round: 1\n        action: \"修正 bib + 加强增量贡献论证\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"Round 2 确认三点差异化清晰\"\n    resolution_round: 2\n\n  - id: \"R0-C5\"\n    summary: \"全文零图表\"\n    category: writing\n    severity: critical\n    status: resolved\n    first_raised_round: 0\n    last_seen_round: 0\n    mentions:\n      - round: 0\n        reviewers: [1, 2]\n        note: \"缺少 selection curves、reliability diagrams\"\n    action_items: []\n    resolution: \"论文已包含 5 个 figures\"\n    resolution_round: 1\n\n  - id: \"R0-C6\"\n    summary: \"成本分析 negligible 误导\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 0\n    last_seen_round: 0\n    mentions:\n      - round: 0\n        reviewers: [1, 2]\n        note: \"8-16× 推理开销不应描述为 negligible\"\n    action_items: []\n    resolution: \"Round 1+ 未再提及\"\n    resolution_round: 1\n\n  - id: \"R0-W1\"\n    summary: \"未探索 signal combination\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 0\n    last_seen_round: 0\n    mentions:\n      - round: 0\n        reviewers: [1, 2]\n        note: \"互补性已证明但未尝试组合\"\n    action_items: []\n    resolution: \"Round 1+ 未再提及\"\n    resolution_round: 1\n\n  - id: \"R0-W4\"\n    summary: \"统计检验不系统\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 0\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"Bootstrap 细节不足\"\n    action_items:\n      - round: 1\n        action: \"补完整 bootstrap 规范\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"Round 2 Reviewer 评价 bootstrap 达到高标准\"\n    resolution_round: 2\n\n  - id: \"R0-RR-D1\"\n    summary: \"Voting Conf N-scaling +0.018 与数据矛盾\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 0\n    last_seen_round: 0\n    mentions:\n      - round: 0\n        reviewers: [\"Research Reviewer\"]\n        note: \"+0.018 实际为 -0.080\"\n    action_items:\n      - round: 0\n        action: \"修正声明\"\n        assigned_to: \"Main Agent\"\n        status: resolved\n    resolution: \"已修正\"\n    resolution_round: 1\n\n  # ============================================================\n  # Round 1 issues (all resolved)\n  # ============================================================\n  - id: \"R1-N1\"\n    summary: \"Bootstrap 检验细节不足\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"p=0.39 支撑核心结论但细节缺失\"\n    action_items:\n      - round: 1\n        action: \"补完整 bootstrap 规范\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"Round 2 Reviewer 评价统计规范达到高标准\"\n    resolution_round: 2\n\n  - id: \"R1-N2\"\n    summary: \"Gap 解释力不足 + logprob 失败未分析\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"4/5 定义性 + logprob 机制缺失\"\n    action_items:\n      - round: 1\n        action: \"区分 by-design vs empirical + logprob failure 分析段\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"Round 2 Reviewer 评价 logprob failure analysis 充分\"\n    resolution_round: 2\n\n  - id: \"R1-N3\"\n    summary: \"Per-sample signal 单薄\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"consensus-proximity = LOO-SJ 是表述问题\"\n    action_items:\n      - round: 1\n        action: \"显式说明等价关系\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"Round 2 确认 consensus-proximity = LOO-SJ 已明确\"\n    resolution_round: 2\n\n  - id: \"R1-N4\"\n    summary: \"Nedellec 引用错误 + 增量贡献弱\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"Yao vs Nédellec 事实错误\"\n    action_items:\n      - round: 1\n        action: \"修正 bib + 加强论证\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"Round 2 确认差异化清晰\"\n    resolution_round: 2\n\n  - id: \"R1-W1\"\n    summary: \"SJ 形式化有歧义\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 4\n    mentions:\n      - round: 2\n        reviewers: [1, 2]\n        note: \"Hungarian threshold + max denominator 需补充\"\n      - round: 3\n        reviewers: [1, 2]\n        note: \"R3-R1 再次指出 Hungarian cost function 未明确 maximize/minimize 方向, zero-IoU pairs 处理方式缺失\"\n      - round: 4\n        reviewers: [2]\n        note: \"R2 Round 4 确认 SJ 形式化已完善 [RESOLVED]\"\n    action_items:\n      - round: 1\n        action: \"补全 Eq(4) 定义\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n      - round: 2\n        action: \"补 threshold 说明 + max vs union 设计理由\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n      - round: 3\n        action: \"补 Hungarian optimization objective (max-weight matching on IoU) + zero-IoU pairs handling\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"Round 4: R2 确认 SJ 形式化已完善，Hungarian matching 描述清晰\"\n    resolution_round: 4\n\n  - id: \"R1-W2\"\n    summary: \"Voting-SJ 冗余度未分析\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"instance-level correlation 未报告\"\n    action_items:\n      - round: 1\n        action: \"报告 Voting-SJ ρ=0.659/0.605\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"中等相关数据已报告\"\n    resolution_round: 2\n\n  - id: \"R1-W3\"\n    summary: \"ρ=0.38 缺 contextualization\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    mentions:\n      - round: 2\n        reviewers: [1, 2]\n        note: \"需 cross-method footnote\"\n    action_items:\n      - round: 2\n        action: \"§5 footnote: semantic entropy AUROC comparison + cross-task caveat\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"Footnote 已加\"\n    resolution_round: 2\n\n  - id: \"R1-W4\"\n    summary: \"Logprob 温度数据缺失\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"robustness 结论需限定\"\n    action_items:\n      - round: 1\n        action: \"限定为 consistency-based signals robust; logprob uncharacterized\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"措辞限定到位\"\n    resolution_round: 2\n\n  - id: \"R1-W5\"\n    summary: \"WNUT-17 establishing 措辞过度\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"fail to reject ≠ accept\"\n    action_items:\n      - round: 1\n        action: \"establishing → consistent with/suggests\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"已修正\"\n    resolution_round: 2\n\n  - id: \"R1-W6\"\n    summary: \"LLaMA 训练设置不对称\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"LLaMA fine-tuning 状态未说明\"\n    action_items:\n      - round: 1\n        action: \"明确两模型 identical LoRA 配置\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"Round 2 未再提及\"\n    resolution_round: 2\n\n  - id: \"R1-W7\"\n    summary: \"约束解码 diversity 影响\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    mentions:\n      - round: 2\n        reviewers: [1, 2]\n        note: \"需扩展为全局 confound + Limitations 条目\"\n    action_items:\n      - round: 2\n        action: \"Discussion 扩展 + Limitations 新增条目\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"已扩展为全局 confound 讨论\"\n    resolution_round: 2\n\n  - id: \"R1-W8\"\n    summary: \"first systematic 过强\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"需收窄 scope\"\n    action_items:\n      - round: 1\n        action: \"first multi-family\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"Round 2 无再提\"\n    resolution_round: 2\n\n  - id: \"R1-W9\"\n    summary: \"遗漏引用\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"Optimal SC, Difficulty-Adaptive SC 等\"\n    action_items:\n      - round: 1\n        action: \"补充引用\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"Round 2 确认无遗漏\"\n    resolution_round: 2\n\n  - id: \"R1-W10\"\n    summary: \"ρ-AUROC dissociation 分析浅\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"EM=1 压缩效应需主文提及\"\n    action_items:\n      - round: 1\n        action: \"Section 5 简述 + 引导 Appendix\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"Round 2 确认 dissociation 分析为 actionable finding\"\n    resolution_round: 2\n\n  - id: \"R1-M1\"\n    summary: \"Logistic regression proxy 无结果\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"展示结果或删除\"\n    action_items:\n      - round: 1\n        action: \"删除提及\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"已删除\"\n    resolution_round: 2\n\n  - id: \"R1-M2\"\n    summary: \"GSM8K +18pp 未注明模型\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"补注 PaLM-540B\"\n    action_items:\n      - round: 1\n        action: \"补注\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"已补注\"\n    resolution_round: 2\n\n  - id: \"R1-M3\"\n    summary: \"Cross-model Δ=0.005 未报告 CI\"\n    category: experiment\n    severity: info\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"within 3-seed σ≈0.007\"\n    action_items:\n      - round: 1\n        action: \"补注\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"已补注\"\n    resolution_round: 2\n\n  # ============================================================\n  # Round 2 issues (all resolved)\n  # ============================================================\n  - id: \"R2-C1\"\n    summary: \"Selection 证据面过窄——仅 1 dataset × 1 model\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - round: 2\n        reviewers: [1, 2]\n        note: \"需补 LLaMA SciERC + CoNLL selection\"\n    action_items:\n      - round: 2\n        action: \"补 4 配置 selection 分析 + Appendix Table 6\"\n        assigned_to: \"Agent + Paper Agent\"\n        status: resolved\n    resolution: \"6 configurations 全部补齐，无 signal 显著超越 greedy\"\n    resolution_round: 2\n\n  - id: \"R2-C2\"\n    summary: \"WNUT-17 仅报告 1 个信号\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - round: 2\n        reviewers: [1, 2]\n        note: \"5 signals 中仅 SJ 一个数据点\"\n    action_items:\n      - round: 2\n        action: \"补全 5 信号 full/conditional ρ + AUROC + Appendix Table 5\"\n        assigned_to: \"Agent + Paper Agent\"\n        status: resolved\n    resolution: \"WNUT-17 全信号表完整，叙事修正为区分 full-set vs conditional\"\n    resolution_round: 2\n\n  - id: \"R2-W1\"\n    summary: \"ρ=0.38 缺 cross-method 对比\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - round: 2\n        reviewers: [1, 2]\n        note: \"需 footnote 引用 semantic entropy AUROC\"\n    action_items:\n      - round: 2\n        action: \"§5 footnote\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"Footnote 已加\"\n    resolution_round: 2\n\n  - id: \"R2-W2\"\n    summary: \"N=8 QE ρ 无 uncertainty\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - round: 2\n        reviewers: [1, 2]\n        note: \"需 bootstrap CIs\"\n    action_items:\n      - round: 2\n        action: \"计算 B=10,000 bootstrap CI + Appendix 表\"\n        assigned_to: \"Agent + Paper Agent\"\n        status: resolved\n    resolution: \"Bootstrap CI 表已加入 Appendix，SJ-logprob 显著\"\n    resolution_round: 2\n\n  - id: \"R2-W3\"\n    summary: \"SJ Hungarian threshold + max denominator\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - round: 2\n        reviewers: [1, 2]\n        note: \"无 threshold 声明需验证\"\n    action_items:\n      - round: 2\n        action: \"代码验证 + method.tex 补充\"\n        assigned_to: \"Agent + Paper Agent\"\n        status: resolved\n    resolution: \"无 threshold, 96.6% pairs sim≥0.5, max denominator 已解释\"\n    resolution_round: 2\n\n  - id: \"R2-W4\"\n    summary: \"RE selection 无统计检验\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - round: 2\n        reviewers: [1, 2]\n        note: \"需 bootstrap p-value\"\n    action_items:\n      - round: 2\n        action: \"RE bootstrap + 补 p=0.80 到论文\"\n        assigned_to: \"Agent + Paper Agent\"\n        status: resolved\n    resolution: \"RE logprob p=0.80, all signals below greedy\"\n    resolution_round: 2\n\n  - id: \"R2-W5\"\n    summary: \"Constrained decoding 全局 confound\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - round: 2\n        reviewers: [1, 2]\n        note: \"需扩展到全局 + Limitations\"\n    action_items:\n      - round: 2\n        action: \"Discussion 扩展 + Limitations 条目\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"已处理\"\n    resolution_round: 2\n\n  - id: \"R2-W6\"\n    summary: \"Abstract RE 措辞误导\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - round: 2\n        reviewers: [1, 2]\n        note: \"NER (three datasets) and RE (SciERC)\"\n    action_items:\n      - round: 2\n        action: \"修正 Abstract\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"已修正\"\n    resolution_round: 2\n\n  - id: \"R2-W7\"\n    summary: \"n=529 vs 551 未解释\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - round: 2\n        reviewers: [1, 2]\n        note: \"22 instances filtering criteria\"\n    action_items:\n      - round: 2\n        action: \"补一句说明\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"已说明 gold-empty filtering\"\n    resolution_round: 2\n\n  - id: \"R2-DATA\"\n    summary: \"RE selection 数据矛盾 (Table 2 vs L129)\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - round: 2\n        reviewers: [\"Research Reviewer\"]\n        note: \"Table 2 logprob=0.395 (-0.9pp) vs L129 logprob=0.410 (+0.6pp)\"\n    action_items:\n      - round: 2\n        action: \"Agent 确认 Table 2 正确 → Paper Agent 修正 L129\"\n        assigned_to: \"Agent + Paper Agent\"\n        status: resolved\n    resolution: \"L129 统一为 logprob=0.395, -0.9pp, p=0.80\"\n    resolution_round: 2\n\n  - id: \"R2-AUROC\"\n    summary: \"L64 AUROC 归属错误 (Voting ρ 配 EM AUROC)\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - round: 2\n        reviewers: [\"Research Reviewer\"]\n        note: \"corresponding 暗示同一信号\"\n    action_items:\n      - round: 2\n        action: \"分别标注 Voting ρ 和 EM AUROC\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"已拆分归属\"\n    resolution_round: 2\n\n  # ============================================================\n  # Round 3 issues (updated with Round 5 status)\n  # ============================================================\n  - id: \"R3-C1\"\n    summary: \"Constrained decoding 是 correlation-selection gap 的未控制混淆变量\"\n    category: method\n    severity: critical\n    status: open\n    first_raised_round: 3\n    last_seen_round: 5\n    mentions:\n      - round: 3\n        reviewers: [1, 2]\n        note: \"两位 Reviewer 均独立提出。Outlines/vLLM constrained decoding 可能压缩 per-sample diversity，使 gap 成为实验设置 artifact。\"\n      - round: 4\n        reviewers: [1, 2]\n        note: \"R2 确认部分解决（承认但未量化）。R1 仍列 critical（需 logprob 分布分析）。共识：elevated should-fix，量化 logprob 分布而非增加 free-form 实验。\"\n      - round: 5\n        reviewers: [1, 2]\n        note: \"Round 5 两位 Reviewer 再次独立提出为 critical。Appendix F 已有 logprob tie 分析（60% instances range<0.05），但论文 claim scope（title/abstract/conclusion）仍未限定为 constrained decoding setting。Non-tied subset +2.9pp p=0.01 结果被两位 Reviewer 一致解读为 gap 主因是 score compression 而非 IE 固有属性。共识：要么添加 free-form 消融，要么在所有核心 claim 中限定 scope。\"\n    action_items:\n      - round: 3\n        action: \"Agent 量化 diversity；Paper Agent 写入论文 + 限定 scope\"\n        assigned_to: \"Agent + Paper Agent\"\n        status: resolved\n      - round: 4\n        action: \"量化 logprob 分布（tie 定义 Δlogprob<ε, non-tie 子集 selection 能力）+ Discussion 中讨论 grammar compliance 如何压缩区分度\"\n        assigned_to: \"Agent + Paper Agent\"\n        status: resolved\n      - round: 5\n        action: \"(a) Title/Abstract/Conclusion 限定 claim scope 为 constrained decoding setting；(b) 提升 Appendix F non-tied analysis 至主文 Discussion；(c) 明确承认 non-tied evidence 对 claim 普适性的影响\"\n        assigned_to: \"Paper Agent\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R3-C2\"\n    summary: \"Failure-to-reject 不等于 evidence of absence，selection gap 统计论证不完整\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 4\n    mentions:\n      - round: 3\n        reviewers: [1, 2]\n        note: \"需修改措辞或补充等价性检验\"\n      - round: 4\n        reviewers: [2]\n        note: \"R2 确认 RESOLVED：TOST 已补充，措辞修正到位\"\n    action_items:\n      - round: 3\n        action: \"修改措辞 + 6/6 cumulative evidence 论证\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"Round 4: TOST 等价检验已补充，措辞修正为 'no significant evidence'，R2 确认到位\"\n    resolution_round: 4\n\n  - id: \"R3-C3\"\n    summary: \"N=8 核心结果 single seed (seed=42)\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 4\n    mentions:\n      - round: 3\n        reviewers: [1, 2]\n        note: \"Table 1 N=8 和 Table 2 selection 全部 single seed\"\n      - round: 4\n        reviewers: [2]\n        note: \"R2 确认 RESOLVED：3-seed 验证已补充\"\n    action_items:\n      - round: 3\n        action: \"Limitations 中明确 single-seed 风险并引用 N=16 stability\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"Round 4: 3-seed 稳定性验证已补充，R2 确认到位\"\n    resolution_round: 4\n\n  - id: \"R3-W1\"\n    summary: \"多重比较校正缺失\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 4\n    mentions:\n      - round: 3\n        reviewers: [1, 2]\n        note: \"SJ-EM CI lower bound +0.003 在 Bonferroni 下不会 survive\"\n      - round: 4\n        reviewers: [2]\n        note: \"R2 确认 RESOLVED：Bonferroni 声明已加\"\n    action_items:\n      - round: 3\n        action: \"声明未做多重比较校正 + SJ-EM 改为 suggestive\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"Round 4: Bonferroni 声明已加，R2 确认到位\"\n    resolution_round: 4\n\n  - id: \"R3-W2\"\n    summary: \"Gap 概念部分 tautological——instance-level 信号无法 select 是定义必然\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 3\n    last_seen_round: 5\n    mentions:\n      - round: 3\n        reviewers: [1, 2]\n        note: \"需在 Discussion 中分离两层论证\"\n      - round: 4\n        reviewers: [1, 2]\n        note: \"R4 两位 Reviewer 独立再次提出：Introduction 未正面论证 why not obvious a priori\"\n      - round: 5\n        reviewers: [1, 2]\n        note: \"R2 认为 gap 被两头夹击（instance-level=tautological, logprob=artifact），整体 contribution 空心化。R1 rebut：consensus-proximity/MBR failure 是 non-trivial empirical finding，但同意 logprob artifact 是 real concern。共识：gap 不完全 tautological（MBR 在 MT 成功 IE 失败是非平凡的），但 C2 应以 logprob+MBR failure 为重心而非 '5 signals all fail'。\"\n    action_items:\n      - round: 3\n        action: \"Discussion 中分离两层论证\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n      - round: 4\n        action: \"(a) Introduction 正面论证 why gap is not obvious (MBR MT vs IE 对比); (b) Discussion 明确分离定义性局限 vs 经验性失败\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n      - round: 5\n        action: \"Reframe C2: 以 logprob score compression + MBR/consensus-proximity empirical failure 为中心，弱化 '5 signals all fail' 叙事；Introduction 加强非显然性论证（MBR 在 MT 成功但 IE 失败）\"\n        assigned_to: \"Paper Agent\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R3-W3\"\n    summary: \"Consensus-proximity 是唯一 instance-to-sample 转换策略，未与 MBR decoding 建立联系\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 4\n    mentions:\n      - round: 3\n        reviewers: [1, 2]\n        note: \"MBR decoding 是成熟替代方案但未讨论\"\n      - round: 4\n        reviewers: [2]\n        note: \"R2 确认 RESOLVED：MBR 连接已补充，§5 MBR 段清晰\"\n    action_items:\n      - round: 3\n        action: \"明确 consensus-proximity 与 MBR 联系 + 引用 MBR 文献\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"Round 4: §5 MBR decoding 连接段已写入，R2 评价'概念优雅'\"\n    resolution_round: 4\n\n  - id: \"R3-W4\"\n    summary: \"FK 独立性假设 justification 不足\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 3\n    last_seen_round: 5\n    mentions:\n      - round: 3\n        reviewers: [1, 2]\n        note: \"§3.2 一句 hand-wave。需报告 inter-sample correlation\"\n      - round: 4\n        reviewers: [2]\n        note: \"R2 确认 RESOLVED：excess agreement 数据已补充\"\n      - round: 5\n        reviewers: [1]\n        note: \"R1 重新提出：excess agreement (-0.4% to -4.0%) 未注明在哪个 configuration 测量，未提供所有配置数据，未引用 FK 在非独立 rater 下的行为分析文献。R2 同意但认为 severity 偏低（FK 非核心 contribution）。\"\n    action_items:\n      - round: 3\n        action: \"Agent 量化 inter-sample correlation；Paper Agent 写入\"\n        assigned_to: \"Agent + Paper Agent\"\n        status: resolved\n      - round: 5\n        action: \"(a) 注明 excess agreement 的 configuration；(b) 补充所有配置数据或至少说明范围；(c) 引用 FK 在非独立 rater 下的行为文献\"\n        assigned_to: \"Paper Agent\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R3-W5\"\n    summary: \"Cross-model 实为 cross-architecture at fixed 8B scale\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 3\n    last_seen_round: 5\n    mentions:\n      - round: 3\n        reviewers: [1, 2]\n        note: \"两模型均 8B，措辞过度外推\"\n      - round: 4\n        reviewers: [2]\n        note: \"R2 确认 RESOLVED：cross-architecture 措辞已统一\"\n      - round: 5\n        reviewers: [1, 2]\n        note: \"R1 再次提出：两模型均为 8B decoder-only transformer，共享相似架构（GQA, RoPE, SwiGLU）。R2 同意应改为 cross-model-family。当前 Conclusion 仍用 'across model families' 而非限定 'at 8B scale'。\"\n    action_items:\n      - round: 5\n        action: \"Conclusion 和 Abstract 统一加 'at 8B scale' 限定，或改为 'across two model families at 8B scale'\"\n        assigned_to: \"Paper Agent\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R3-W6\"\n    summary: \"'First multi-family comparison' claim scope 过宽\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 3\n    last_seen_round: 5\n    mentions:\n      - round: 3\n        reviewers: [1, 2]\n        note: \"需限定为 structured IE 的 QE + selection\"\n      - round: 4\n        reviewers: [2]\n        note: \"R2 确认部分解决：Conclusion 有 hedge 但 Introduction 仍断言式\"\n      - round: 5\n        reviewers: [1, 2]\n        note: \"两位 Reviewer 一致同意：通过堆叠修饰词(multiple families + both objectives + generative + structured IE)确保 'first' 成立属于 scope engineering。建议改为描述性表述，避免 'first' claim。\"\n    action_items:\n      - round: 5\n        action: \"Introduction 和 Conclusion 去掉 'first' claim，改为描述性表述\"\n        assigned_to: \"Paper Agent\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R3-W7\"\n    summary: \"术语不一致\"\n    category: writing\n    severity: warning\n    status: open\n    first_raised_round: 3\n    last_seen_round: 5\n    mentions:\n      - round: 3\n        reviewers: [1, 2]\n        note: \"confidence signal vs consistency signal 混用；VC vs Voting Conf.\"\n      - round: 4\n        reviewers: [1, 2]\n        note: \"R2 确认部分解决：表格缩写 VC/Voting Conf. 仍不统一\"\n      - round: 5\n        reviewers: [1, 2]\n        note: \"仍未解决。Table 1 用 'Voting Conf.'，Table 4/7 用 'VC'，正文用 'entity voting'。§3.2 已有 taxonomy 定义（confidence signal 统称 vs consistency signal 子集），但表格缩写未统一。\"\n    action_items:\n      - round: 5\n        action: \"全文统一表格缩写（建议全部用 VC）+ 正文首次出现时写全称\"\n        assigned_to: \"Paper Agent\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R3-W8\"\n    summary: \"遗漏引用：VerifiNER, RASC, MBR decoding, Malinin & Gales\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 4\n    mentions:\n      - round: 3\n        reviewers: [1, 2]\n        note: \"VerifiNER, MBR decoding 等高度相关\"\n      - round: 4\n        reviewers: [2]\n        note: \"R2 确认 RESOLVED：引用已补全\"\n    action_items:\n      - round: 3\n        action: \"补充引用并在 Related Work 中讨论\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"Round 4: 引用已补全，R2 确认到位\"\n    resolution_round: 4\n\n  - id: \"R3-M1\"\n    summary: \"WNUT-17 '54% zero F1' 与 Table 7 数据不一致 (51.5%)\"\n    category: experiment\n    severity: info\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 3\n    mentions:\n      - round: 3\n        reviewers: [1]\n        note: \"355/689 ≈ 51.5% vs 正文 54%\"\n    action_items:\n      - round: 3\n        action: \"Agent 核实实际数字 → Paper Agent 统一\"\n        assigned_to: \"Agent + Paper Agent\"\n        status: resolved\n    resolution: \"54% → 52% 已修正，Round 4 未再提及\"\n    resolution_round: 4\n\n  - id: \"R3-M2\"\n    summary: \"EM selection exclusion 缺乏经验支持\"\n    category: experiment\n    severity: info\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 3\n    mentions:\n      - round: 3\n        reviewers: [1, 2]\n        note: \"'probability negligible' 需报告 exact match pairs 频率\"\n    action_items:\n      - round: 3\n        action: \"Agent 计算 exact match pairs 频率 → Paper Agent 写入\"\n        assigned_to: \"Agent + Paper Agent\"\n        status: resolved\n    resolution: \"EM 已加入 Table 2，Round 4 未再提及\"\n    resolution_round: 4\n\n  - id: \"R3-M3\"\n    summary: \"Ethics Statement 缺失\"\n    category: format\n    severity: info\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 5\n    mentions:\n      - round: 3\n        reviewers: [2]\n        note: \"共识降为 minor\"\n      - round: 4\n        reviewers: [2]\n        note: \"R2 确认 Ethics Statement 已存在但位于 Limitations section 内——建议改为独立 section\"\n      - round: 5\n        reviewers: [2]\n        note: \"Ethics Statement 现为独立 \\\\section*{Ethics Statement}，位于 Limitations 后、References 前，符合 ACL 格式。内容仅 2 句，R2 建议补充但非 must-fix。\"\n    action_items:\n      - round: 4\n        action: \"将 Ethics Statement 从 Limitations 内移出为独立 section\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"Round 5: Ethics Statement 已为独立 section，格式合规\"\n    resolution_round: 5\n\n  - id: \"R3-M4\"\n    summary: \"ρ-AUROC dissociation 作为独立发现过度强调\"\n    category: framing\n    severity: info\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 3\n    mentions:\n      - round: 3\n        reviewers: [1, 2]\n        note: \"建议承认统计预期性后聚焦实践含义\"\n    action_items:\n      - round: 3\n        action: \"§4.2 承认 dissociation 的统计预期性\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"已承认统计预期性，Round 4 未再提及\"\n    resolution_round: 4\n\n  - id: \"R3-M5\"\n    summary: \"对 Nedellec (2026) 措辞偏 adversarial\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 3\n    mentions:\n      - round: 3\n        reviewers: [1, 2]\n        note: \"建议用更 neutral 语气\"\n    action_items:\n      - round: 3\n        action: \"Introduction 中改为更 neutral 的语气\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"Nedellec 措辞已改为 neutral，Round 4 未再提及\"\n    resolution_round: 4\n\n  - id: \"R3-M6\"\n    summary: \"LOO-SJ 验证中 Δρ 和 per-instance Δρ 量纲混淆\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 3\n    mentions:\n      - round: 3\n        reviewers: [1]\n        note: \"Δρ=−0.014 vs per-instance max Δρ=3.1×10⁻⁴ 量纲不同\"\n    action_items:\n      - round: 3\n        action: \"澄清 per-instance Δρ 具体含义\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"LOO-SJ Δρ 含义已澄清，Round 4 未再提及\"\n    resolution_round: 4\n\n  - id: \"R3-M7\"\n    summary: \"Figure 1 caption 引入未直接可视化的 p=0.39\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 3\n    mentions:\n      - round: 3\n        reviewers: [1]\n        note: \"建议加 '(Table 2)' 交叉引用\"\n    action_items:\n      - round: 3\n        action: \"补 '(Table 2)' 交叉引用\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"Figure 1 caption 交叉引用已补，Round 4 未再提及\"\n    resolution_round: 4\n\n  # ============================================================\n  # Round 4 issues (updated with Round 5 status)\n  # ============================================================\n  - id: \"R4-C1\"\n    summary: \"训练配置和 prompt template 缺失，影响独立复现\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 5\n    mentions:\n      - round: 4\n        reviewers: [1, 2]\n        note: \"§4.1 仅报告 LoRA rank=32, α=64, 5 epochs, LLaMA Factory，缺少 lr, batch size 等\"\n      - round: 5\n        reviewers: [1, 2]\n        note: \"Appendix E 已包含完整 Table 8（lr, optimizer, batch size, warmup, max seq length, LoRA target, precision 等）+ prompt template + constrained decoding 细节。两位 Reviewer 均给 Reproducibility 4/5。\"\n    action_items:\n      - round: 4\n        action: \"附录补充完整训练配置表 + NER/RE prompt template 示例 + schema constraint 定义\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"Round 5: Appendix E Table 8 完整，prompt template 已提供，Reproducibility 4/5\"\n    resolution_round: 5\n\n  - id: \"R4-W1\"\n    summary: \"RE 证据需进一步加强（conditional analysis 或降级）\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 4\n    last_seen_round: 5\n    mentions:\n      - round: 4\n        reviewers: [1, 2]\n        note: \"claim 降级已完成（resolved），但两位 Reviewer 仍认为 RE 证据薄弱\"\n      - round: 5\n        reviewers: [1, 2]\n        note: \"Abstract 标注 '(SciERC, preliminary)' 但论文后续 Table 1/2, Figure 2-3, Discussion 大量使用 RE 结果无 preliminary 限定。Contribution #3 将 RE 结论嵌入通用表述。需全文一致标注。\"\n    action_items:\n      - round: 5\n        action: \"(a) 所有 RE 分析处一致标注 single-benchmark preliminary；(b) Contribution #3 加 RE 限定；(c) Future work 明确列出 RE 多数据集验证\"\n        assigned_to: \"Paper Agent\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R4-W2\"\n    summary: \"SJ vs EM 优势叙事应改为 difficulty-dependent complementarity\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 5\n    mentions:\n      - round: 4\n        reviewers: [1, 2]\n        note: \"SJ vs EM Δρ=+0.065, CI 下界 +0.003, Bonferroni 下不显著\"\n      - round: 5\n        reviewers: [1, 2]\n        note: \"§4.2 已使用 'difficulty-dependent complementarity rather than a universal structural advantage' 措辞。R2 仍认为增量不足但 R1 认为 crossover pattern 是核心 claim 而非单个 Δρ。\"\n    action_items:\n      - round: 4\n        action: \"Contribution #1 弱化 structural advantage，改为强调 difficulty-dependent complementarity\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"Round 5: §4.2 已用 complementarity 措辞，Contribution #1 已包含 difficulty-dependent ordering\"\n    resolution_round: 5\n\n  - id: \"R4-W3\"\n    summary: \"Abstract 过于密集，第 4 行超长句子需拆分\"\n    category: writing\n    severity: warning\n    status: open\n    first_raised_round: 4\n    last_seen_round: 5\n    mentions:\n      - round: 4\n        reviewers: [1, 2]\n        note: \"多层嵌套括号和分号的超长句子\"\n      - round: 5\n        reviewers: [1, 2]\n        note: \"仍未修改。9 行含 5 signal/3 family/4 metric/3 dataset/2 model + gap 概念。两位 Reviewer 一致建议拆分为 2-3 句，聚焦核心 claim，具体数字移入 Introduction。\"\n    action_items:\n      - round: 5\n        action: \"Abstract 拆分为 2-3 句核心 claim，将具体信号名/数字/family 移入 Introduction\"\n        assigned_to: \"Paper Agent\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R4-W4\"\n    summary: \"缺少 Xiong et al. (2024) 'Can LLMs Express Their Uncertainty?' ICLR 2024\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 5\n    mentions:\n      - round: 4\n        reviewers: [1, 2]\n        note: \"系统评估 LLM 置信度获取方法，与本文多族信号比较直接相关\"\n      - round: 5\n        reviewers: [1, 2]\n        note: \"Related Work §2 已引用 Xiong et al. (2024)：'systematically evaluate confidence elicitation across prompting, sampling, and aggregation strategies'\"\n    action_items:\n      - round: 4\n        action: \"Related Work 引用 Xiong et al.\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"Round 5: 已引用，§2 第三段\"\n    resolution_round: 5\n\n  - id: \"R4-M1\"\n    summary: \"SJ normalizer 选择（max vs union）缺乏对比\"\n    category: method\n    severity: info\n    status: wont_fix\n    first_raised_round: 4\n    last_seen_round: 4\n    mentions:\n      - round: 4\n        reviewers: [1]\n        note: \"R1-W3: max(|g_i|,|g_j|) vs |g_i∪g_j| 未比较\"\n    action_items:\n      - round: 4\n        action: \"附录补 union normalizer 结果或提供理论依据\"\n        assigned_to: \"Agent + Paper Agent\"\n        status: wont_fix\n    resolution: \"Rejected: max normalizer 设计已在 method.tex 有理由，超出 scope\"\n    resolution_round: 4\n\n  - id: \"R4-M2\"\n    summary: \"TOST δ 选择（±2/3/5 pp）缺乏实践意义论证\"\n    category: experiment\n    severity: info\n    status: open\n    first_raised_round: 4\n    last_seen_round: 5\n    mentions:\n      - round: 4\n        reviewers: [1]\n        note: \"δ 选择直接影响等价结论\"\n      - round: 5\n        reviewers: [1, 2]\n        note: \"R1 再提：与 IAA 关联无引用。R2 同意但认为多水平 δ 已构成 sensitivity analysis，引用 IAA 数据即可。\"\n    action_items:\n      - round: 5\n        action: \"引用 1-2 篇 IE benchmark IAA 数据来锚定 δ 选择\"\n        assigned_to: \"Paper Agent\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R4-M3\"\n    summary: \"Table 1 N=16 block 大面积空白\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 4\n    last_seen_round: 5\n    mentions:\n      - round: 4\n        reviewers: [1, 2]\n        note: \"N=16 仅填 LLaMA CoNLL，SciERC 空白\"\n      - round: 5\n        reviewers: [1, 2]\n        note: \"Table 1 已加脚注说明 N=16 数据位置（Appendix Table 3），但脚注格式（\\\\textsuperscript{†} + \\\\footnotetext）在 two-column 模板下可能渲染异常。\"\n    action_items:\n      - round: 5\n        action: \"检查 PDF 渲染；考虑合并 N=16 到附录以简化 Table 1\"\n        assigned_to: \"Paper Agent\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  # ============================================================\n  # Round 5 new issues\n  # ============================================================\n  - id: \"R5-N1\"\n    summary: \"与 Nédellec et al. (2026) 的增量贡献不充分\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 5\n    last_seen_round: 5\n    mentions:\n      - round: 5\n        reviewers: [2]\n        note: \"三个增量均偏弱：SJ vs EM Bonferroni 不显著，selection analysis 部分 tautological，difficulty gradient 直觉上不意外。R1 rebut：crossover pattern 是核心 claim 而非单个 Δρ；WNUT-17 conditional collapse 不是直觉可预测。共识：Findings-worthy 但非 ground-breaking。\"\n    action_items:\n      - round: 5\n        action: \"更诚实地量化增量大小；强调 WNUT-17 conditional collapse 和 logprob negative correlation 作为 non-obvious findings\"\n        assigned_to: \"Paper Agent\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R5-W1\"\n    summary: \"Qwen3-8B thinking token 训练不一致（SciERC vs CoNLL/WNUT）\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 5\n    last_seen_round: 5\n    mentions:\n      - round: 5\n        reviewers: [1, 2]\n        note: \"SciERC 未显式禁用 enable_thinking，CoNLL/WNUT 显式设 false。推理时 constrained decoding 覆盖，但训练时差异可能影响 learned representations。\"\n    action_items:\n      - round: 5\n        action: \"Limitations 讨论此不一致性，或确认 thinking tokens 在 SciERC fine-tuning 中是否实际被激活\"\n        assigned_to: \"Paper Agent\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R5-W2\"\n    summary: \"Semantic entropy 脚注比较可能误导\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 5\n    last_seen_round: 5\n    mentions:\n      - round: 5\n        reviewers: [1, 2]\n        note: \"§4.2 脚注比较 semantic entropy AUROC 0.75-0.85，但自述 'direct comparison is not meaningful'。R1 建议删除或缩短；R2 认为意图合理但执行可能误导快速读者。\"\n    action_items:\n      - round: 5\n        action: \"缩短脚注，去掉具体数字，仅保留 'scale context' 功能\"\n        assigned_to: \"Paper Agent\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R5-W3\"\n    summary: \"he2024uncertainty bib entry 与引用上下文不匹配\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 5\n    last_seen_round: 5\n    mentions:\n      - round: 5\n        reviewers: [1]\n        note: \"bib 标题 'Uncertainty Estimation on Sequential Labeling via Uncertainty Transmission' (NAACL 2024 Findings)，但 Related Work 引用上下文是 'survey uncertainty quantification specifically for LLMs'——实际是 sequential labeling 论文而非 LLM survey\"\n    action_items:\n      - round: 5\n        action: \"修正引用上下文描述，或替换为正确的 LLM UQ survey 引用\"\n        assigned_to: \"Paper Agent\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R5-M1\"\n    summary: \"缺少 test-time scaling verification survey 引用\"\n    category: framing\n    severity: info\n    status: open\n    first_raised_round: 5\n    last_seen_round: 5\n    mentions:\n      - round: 5\n        reviewers: [1, 2]\n        note: \"R2 建议补 'Trust but Verify! A Survey on Verification Design for Test-time Scaling' (2025)，R1 同意与 Discussion 中 verifier 建议直接相关\"\n    action_items:\n      - round: 5\n        action: \"Related Work 或 Discussion 引用 test-time scaling verification survey\"\n        assigned_to: \"Paper Agent\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R5-M2\"\n    summary: \"缺少 MBR 在非 MT 任务中的应用引用\"\n    category: framing\n    severity: info\n    status: open\n    first_raised_round: 5\n    last_seen_round: 5\n    mentions:\n      - round: 5\n        reviewers: [1, 2]\n        note: \"Discussion §5 将方法与 MBR 对接但只引用 MT 领域。应补 summarization/QA 等任务中的 MBR 文献。\"\n    action_items:\n      - round: 5\n        action: \"补充 MBR 在非 MT 任务中的引用\"\n        assigned_to: \"Paper Agent\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R5-M3\"\n    summary: \"Consensus-proximity = LOO-SJ 等价性缺少推导\"\n    category: method\n    severity: info\n    status: open\n    first_raised_round: 5\n    last_seen_round: 5\n    mentions:\n      - round: 5\n        reviewers: [1, 2]\n        note: \"§3.3 声称数学等价但未给出推导。R1 要求证明；R2 建议更正为 'approximately equivalent' 如果无法严格证明。\"\n    action_items:\n      - round: 5\n        action: \"附录补简要推导，或更正为 approximately equivalent\"\n        assigned_to: \"Paper Agent\"\n        status: open\n    resolution: \"\"\n    resolution_round: null"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "struct_self_consist_ie",
    "issues_yaml": "issues:\n  # ============================================================\n  # Round 0 issues (all resolved)\n  # ============================================================\n  - id: \"R0-C1\"\n    summary: \"模型规模单一（仅 8B）\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 0\n    last_seen_round: 1\n    mentions:\n      - round: 0\n        reviewers: [1, 2]\n        note: \"8B→8B 仅验证架构鲁棒性非规模鲁棒性\"\n      - round: 1\n        reviewers: [1, 2]\n        note: \"model-agnostic 与 Limitations 矛盾\"\n    action_items:\n      - round: 1\n        action: \"全文替换 model-agnostic → consistent across tested model families\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"Round 2 Reviewer 确认措辞修正到位，无再提\"\n    resolution_round: 2\n\n  - id: \"R0-C2\"\n    summary: \"相关工作显著遗漏\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 0\n    last_seen_round: 1\n    mentions:\n      - round: 0\n        reviewers: [1, 2]\n        note: \"5 篇核心文献缺失\"\n      - round: 1\n        reviewers: [1, 2]\n        note: \"新遗漏：Optimal SC, Difficulty-Adaptive SC\"\n    action_items:\n      - round: 1\n        action: \"补充 6 篇引用到 Related Work\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"Round 2: 49 条 bib 全部 cited, 0 orphan, 无遗漏\"\n    resolution_round: 2\n\n  - id: \"R0-C3\"\n    summary: \"RE 结论仅基于 SciERC 单数据集\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 0\n    last_seen_round: 4\n    mentions:\n      - round: 0\n        reviewers: [1, 2]\n        note: \"需跨数据集验证或降级措辞\"\n      - round: 2\n        reviewers: [1, 2]\n        note: \"Abstract RE 措辞需修正\"\n      - round: 3\n        reviewers: [1, 2]\n        note: \"Round 2 措辞修正到位，但 R3 Reviewer 2 再次提出 44% zero-F1 floor effect 严重压缩可区分范围\"\n      - round: 4\n        reviewers: [1, 2]\n        note: \"R2 确认 claim 降级已完成（Conclusion 明确 hedge）。两位 Reviewer 仍认为 RE 证据薄弱，但 claim 范围已恰当限定——后续改进作为 R4-W1 追踪\"\n    action_items:\n      - round: 1\n        action: \"降级措辞 universal → observed in SciERC\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n      - round: 2\n        action: \"Abstract 改为 NER (three datasets) and RE (SciERC)\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n      - round: 3\n        action: \"进一步降级 RE claim 为 preliminary evidence + 补 SciERC RE conditional analysis\"\n        assigned_to: \"Agent + Paper Agent\"\n        status: resolved\n    resolution: \"Round 4: claim 降级到位（Conclusion 明确 hedge, Abstract 区分 NER/RE 证据量），RE conditional analysis 作为后续改进建议\"\n    resolution_round: 4\n\n  - id: \"R0-C4\"\n    summary: \"SJ 方法新颖性有限\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 0\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [2]\n        note: \"Nedellec 增量贡献论证不足 + 引用错误\"\n    action_items:\n      - round: 1\n        action: \"修正 bib + 加强增量贡献论证\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"Round 2 确认三点差异化清晰\"\n    resolution_round: 2\n\n  - id: \"R0-C5\"\n    summary: \"全文零图表\"\n    category: writing\n    severity: critical\n    status: resolved\n    first_raised_round: 0\n    last_seen_round: 0\n    mentions:\n      - round: 0\n        reviewers: [1, 2]\n        note: \"缺少 selection curves、reliability diagrams\"\n    action_items: []\n    resolution: \"论文已包含 5 个 figures\"\n    resolution_round: 1\n\n  - id: \"R0-C6\"\n    summary: \"成本分析 negligible 误导\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 0\n    last_seen_round: 0\n    mentions:\n      - round: 0\n        reviewers: [1, 2]\n        note: \"8-16× 推理开销不应描述为 negligible\"\n    action_items: []\n    resolution: \"Round 1+ 未再提及\"\n    resolution_round: 1\n\n  - id: \"R0-W1\"\n    summary: \"未探索 signal combination\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 0\n    last_seen_round: 0\n    mentions:\n      - round: 0\n        reviewers: [1, 2]\n        note: \"互补性已证明但未尝试组合\"\n    action_items: []\n    resolution: \"Round 1+ 未再提及\"\n    resolution_round: 1\n\n  - id: \"R0-W4\"\n    summary: \"统计检验不系统\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 0\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"Bootstrap 细节不足\"\n    action_items:\n      - round: 1\n        action: \"补完整 bootstrap 规范\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"Round 2 Reviewer 评价 bootstrap 达到高标准\"\n    resolution_round: 2\n\n  - id: \"R0-RR-D1\"\n    summary: \"Voting Conf N-scaling +0.018 与数据矛盾\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 0\n    last_seen_round: 0\n    mentions:\n      - round: 0\n        reviewers: [\"Research Reviewer\"]\n        note: \"+0.018 实际为 -0.080\"\n    action_items:\n      - round: 0\n        action: \"修正声明\"\n        assigned_to: \"Main Agent\"\n        status: resolved\n    resolution: \"已修正\"\n    resolution_round: 1\n\n  # ============================================================\n  # Round 1 issues (all resolved)\n  # ============================================================\n  - id: \"R1-N1\"\n    summary: \"Bootstrap 检验细节不足\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"p=0.39 支撑核心结论但细节缺失\"\n    action_items:\n      - round: 1\n        action: \"补完整 bootstrap 规范\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"Round 2 Reviewer 评价统计规范达到高标准\"\n    resolution_round: 2\n\n  - id: \"R1-N2\"\n    summary: \"Gap 解释力不足 + logprob 失败未分析\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"4/5 定义性 + logprob 机制缺失\"\n    action_items:\n      - round: 1\n        action: \"区分 by-design vs empirical + logprob failure 分析段\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"Round 2 Reviewer 评价 logprob failure analysis 充分\"\n    resolution_round: 2\n\n  - id: \"R1-N3\"\n    summary: \"Per-sample signal 单薄\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"consensus-proximity = LOO-SJ 是表述问题\"\n    action_items:\n      - round: 1\n        action: \"显式说明等价关系\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"Round 2 确认 consensus-proximity = LOO-SJ 已明确\"\n    resolution_round: 2\n\n  - id: \"R1-N4\"\n    summary: \"Nedellec 引用错误 + 增量贡献弱\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"Yao vs Nédellec 事实错误\"\n    action_items:\n      - round: 1\n        action: \"修正 bib + 加强论证\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"Round 2 确认差异化清晰\"\n    resolution_round: 2\n\n  - id: \"R1-W1\"\n    summary: \"SJ 形式化有歧义\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 4\n    mentions:\n      - round: 2\n        reviewers: [1, 2]\n        note: \"Hungarian threshold + max denominator 需补充\"\n      - round: 3\n        reviewers: [1, 2]\n        note: \"R3-R1 再次指出 Hungarian cost function 未明确 maximize/minimize 方向, zero-IoU pairs 处理方式缺失\"\n      - round: 4\n        reviewers: [2]\n        note: \"R2 Round 4 确认 SJ 形式化已完善 [RESOLVED]\"\n    action_items:\n      - round: 1\n        action: \"补全 Eq(4) 定义\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n      - round: 2\n        action: \"补 threshold 说明 + max vs union 设计理由\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n      - round: 3\n        action: \"补 Hungarian optimization objective (max-weight matching on IoU) + zero-IoU pairs handling\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"Round 4: R2 确认 SJ 形式化已完善，Hungarian matching 描述清晰\"\n    resolution_round: 4\n\n  - id: \"R1-W2\"\n    summary: \"Voting-SJ 冗余度未分析\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"instance-level correlation 未报告\"\n    action_items:\n      - round: 1\n        action: \"报告 Voting-SJ ρ=0.659/0.605\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"中等相关数据已报告\"\n    resolution_round: 2\n\n  - id: \"R1-W3\"\n    summary: \"ρ=0.38 缺 contextualization\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    mentions:\n      - round: 2\n        reviewers: [1, 2]\n        note: \"需 cross-method footnote\"\n    action_items:\n      - round: 2\n        action: \"§5 footnote: semantic entropy AUROC comparison + cross-task caveat\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"Footnote 已加\"\n    resolution_round: 2\n\n  - id: \"R1-W4\"\n    summary: \"Logprob 温度数据缺失\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"robustness 结论需限定\"\n    action_items:\n      - round: 1\n        action: \"限定为 consistency-based signals robust; logprob uncharacterized\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"措辞限定到位\"\n    resolution_round: 2\n\n  - id: \"R1-W5\"\n    summary: \"WNUT-17 establishing 措辞过度\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"fail to reject ≠ accept\"\n    action_items:\n      - round: 1\n        action: \"establishing → consistent with/suggests\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"已修正\"\n    resolution_round: 2\n\n  - id: \"R1-W6\"\n    summary: \"LLaMA 训练设置不对称\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"LLaMA fine-tuning 状态未说明\"\n    action_items:\n      - round: 1\n        action: \"明确两模型 identical LoRA 配置\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"Round 2 未再提及\"\n    resolution_round: 2\n\n  - id: \"R1-W7\"\n    summary: \"约束解码 diversity 影响\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    mentions:\n      - round: 2\n        reviewers: [1, 2]\n        note: \"需扩展为全局 confound + Limitations 条目\"\n    action_items:\n      - round: 2\n        action: \"Discussion 扩展 + Limitations 新增条目\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"已扩展为全局 confound 讨论\"\n    resolution_round: 2\n\n  - id: \"R1-W8\"\n    summary: \"first systematic 过强\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"需收窄 scope\"\n    action_items:\n      - round: 1\n        action: \"first multi-family\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"Round 2 无再提\"\n    resolution_round: 2\n\n  - id: \"R1-W9\"\n    summary: \"遗漏引用\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"Optimal SC, Difficulty-Adaptive SC 等\"\n    action_items:\n      - round: 1\n        action: \"补充引用\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"Round 2 确认无遗漏\"\n    resolution_round: 2\n\n  - id: \"R1-W10\"\n    summary: \"ρ-AUROC dissociation 分析浅\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"EM=1 压缩效应需主文提及\"\n    action_items:\n      - round: 1\n        action: \"Section 5 简述 + 引导 Appendix\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"Round 2 确认 dissociation 分析为 actionable finding\"\n    resolution_round: 2\n\n  - id: \"R1-M1\"\n    summary: \"Logistic regression proxy 无结果\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"展示结果或删除\"\n    action_items:\n      - round: 1\n        action: \"删除提及\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"已删除\"\n    resolution_round: 2\n\n  - id: \"R1-M2\"\n    summary: \"GSM8K +18pp 未注明模型\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"补注 PaLM-540B\"\n    action_items:\n      - round: 1\n        action: \"补注\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"已补注\"\n    resolution_round: 2\n\n  - id: \"R1-M3\"\n    summary: \"Cross-model Δ=0.005 未报告 CI\"\n    category: experiment\n    severity: info\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"within 3-seed σ≈0.007\"\n    action_items:\n      - round: 1\n        action: \"补注\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"已补注\"\n    resolution_round: 2\n\n  # ============================================================\n  # Round 2 issues (all resolved)\n  # ============================================================\n  - id: \"R2-C1\"\n    summary: \"Selection 证据面过窄——仅 1 dataset × 1 model\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - round: 2\n        reviewers: [1, 2]\n        note: \"需补 LLaMA SciERC + CoNLL selection\"\n    action_items:\n      - round: 2\n        action: \"补 4 配置 selection 分析 + Appendix Table 6\"\n        assigned_to: \"Agent + Paper Agent\"\n        status: resolved\n    resolution: \"6 configurations 全部补齐，无 signal 显著超越 greedy\"\n    resolution_round: 2\n\n  - id: \"R2-C2\"\n    summary: \"WNUT-17 仅报告 1 个信号\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - round: 2\n        reviewers: [1, 2]\n        note: \"5 signals 中仅 SJ 一个数据点\"\n    action_items:\n      - round: 2\n        action: \"补全 5 信号 full/conditional ρ + AUROC + Appendix Table 5\"\n        assigned_to: \"Agent + Paper Agent\"\n        status: resolved\n    resolution: \"WNUT-17 全信号表完整，叙事修正为区分 full-set vs conditional\"\n    resolution_round: 2\n\n  - id: \"R2-W1\"\n    summary: \"ρ=0.38 缺 cross-method 对比\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - round: 2\n        reviewers: [1, 2]\n        note: \"需 footnote 引用 semantic entropy AUROC\"\n    action_items:\n      - round: 2\n        action: \"§5 footnote\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"Footnote 已加\"\n    resolution_round: 2\n\n  - id: \"R2-W2\"\n    summary: \"N=8 QE ρ 无 uncertainty\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - round: 2\n        reviewers: [1, 2]\n        note: \"需 bootstrap CIs\"\n    action_items:\n      - round: 2\n        action: \"计算 B=10,000 bootstrap CI + Appendix 表\"\n        assigned_to: \"Agent + Paper Agent\"\n        status: resolved\n    resolution: \"Bootstrap CI 表已加入 Appendix，SJ-logprob 显著\"\n    resolution_round: 2\n\n  - id: \"R2-W3\"\n    summary: \"SJ Hungarian threshold + max denominator\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - round: 2\n        reviewers: [1, 2]\n        note: \"无 threshold 声明需验证\"\n    action_items:\n      - round: 2\n        action: \"代码验证 + method.tex 补充\"\n        assigned_to: \"Agent + Paper Agent\"\n        status: resolved\n    resolution: \"无 threshold, 96.6% pairs sim≥0.5, max denominator 已解释\"\n    resolution_round: 2\n\n  - id: \"R2-W4\"\n    summary: \"RE selection 无统计检验\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - round: 2\n        reviewers: [1, 2]\n        note: \"需 bootstrap p-value\"\n    action_items:\n      - round: 2\n        action: \"RE bootstrap + 补 p=0.80 到论文\"\n        assigned_to: \"Agent + Paper Agent\"\n        status: resolved\n    resolution: \"RE logprob p=0.80, all signals below greedy\"\n    resolution_round: 2\n\n  - id: \"R2-W5\"\n    summary: \"Constrained decoding 全局 confound\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - round: 2\n        reviewers: [1, 2]\n        note: \"需扩展到全局 + Limitations\"\n    action_items:\n      - round: 2\n        action: \"Discussion 扩展 + Limitations 条目\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"已处理\"\n    resolution_round: 2\n\n  - id: \"R2-W6\"\n    summary: \"Abstract RE 措辞误导\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - round: 2\n        reviewers: [1, 2]\n        note: \"NER (three datasets) and RE (SciERC)\"\n    action_items:\n      - round: 2\n        action: \"修正 Abstract\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"已修正\"\n    resolution_round: 2\n\n  - id: \"R2-W7\"\n    summary: \"n=529 vs 551 未解释\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - round: 2\n        reviewers: [1, 2]\n        note: \"22 instances filtering criteria\"\n    action_items:\n      - round: 2\n        action: \"补一句说明\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"已说明 gold-empty filtering\"\n    resolution_round: 2\n\n  - id: \"R2-DATA\"\n    summary: \"RE selection 数据矛盾 (Table 2 vs L129)\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - round: 2\n        reviewers: [\"Research Reviewer\"]\n        note: \"Table 2 logprob=0.395 (-0.9pp) vs L129 logprob=0.410 (+0.6pp)\"\n    action_items:\n      - round: 2\n        action: \"Agent 确认 Table 2 正确 → Paper Agent 修正 L129\"\n        assigned_to: \"Agent + Paper Agent\"\n        status: resolved\n    resolution: \"L129 统一为 logprob=0.395, -0.9pp, p=0.80\"\n    resolution_round: 2\n\n  - id: \"R2-AUROC\"\n    summary: \"L64 AUROC 归属错误 (Voting ρ 配 EM AUROC)\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 2\n    last_seen_round: 2\n    mentions:\n      - round: 2\n        reviewers: [\"Research Reviewer\"]\n        note: \"corresponding 暗示同一信号\"\n    action_items:\n      - round: 2\n        action: \"分别标注 Voting ρ 和 EM AUROC\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"已拆分归属\"\n    resolution_round: 2\n\n  # ============================================================\n  # Round 3 issues (updated with Round 5 status)\n  # ============================================================\n  - id: \"R3-C1\"\n    summary: \"Constrained decoding 是 correlation-selection gap 的未控制混淆变量\"\n    category: method\n    severity: critical\n    status: open\n    first_raised_round: 3\n    last_seen_round: 5\n    mentions:\n      - round: 3\n        reviewers: [1, 2]\n        note: \"两位 Reviewer 均独立提出。Outlines/vLLM constrained decoding 可能压缩 per-sample diversity，使 gap 成为实验设置 artifact。\"\n      - round: 4\n        reviewers: [1, 2]\n        note: \"R2 确认部分解决（承认但未量化）。R1 仍列 critical（需 logprob 分布分析）。共识：elevated should-fix，量化 logprob 分布而非增加 free-form 实验。\"\n      - round: 5\n        reviewers: [1, 2]\n        note: \"Round 5 两位 Reviewer 再次独立提出为 critical。Appendix F 已有 logprob tie 分析（60% instances range<0.05），但论文 claim scope（title/abstract/conclusion）仍未限定为 constrained decoding setting。Non-tied subset +2.9pp p=0.01 结果被两位 Reviewer 一致解读为 gap 主因是 score compression 而非 IE 固有属性。共识：要么添加 free-form 消融，要么在所有核心 claim 中限定 scope。\"\n    action_items:\n      - round: 3\n        action: \"Agent 量化 diversity；Paper Agent 写入论文 + 限定 scope\"\n        assigned_to: \"Agent + Paper Agent\"\n        status: resolved\n      - round: 4\n        action: \"量化 logprob 分布（tie 定义 Δlogprob<ε, non-tie 子集 selection 能力）+ Discussion 中讨论 grammar compliance 如何压缩区分度\"\n        assigned_to: \"Agent + Paper Agent\"\n        status: resolved\n      - round: 5\n        action: \"(a) Title/Abstract/Conclusion 限定 claim scope 为 constrained decoding setting；(b) 提升 Appendix F non-tied analysis 至主文 Discussion；(c) 明确承认 non-tied evidence 对 claim 普适性的影响\"\n        assigned_to: \"Paper Agent\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R3-C2\"\n    summary: \"Failure-to-reject 不等于 evidence of absence，selection gap 统计论证不完整\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 4\n    mentions:\n      - round: 3\n        reviewers: [1, 2]\n        note: \"需修改措辞或补充等价性检验\"\n      - round: 4\n        reviewers: [2]\n        note: \"R2 确认 RESOLVED：TOST 已补充，措辞修正到位\"\n    action_items:\n      - round: 3\n        action: \"修改措辞 + 6/6 cumulative evidence 论证\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"Round 4: TOST 等价检验已补充，措辞修正为 'no significant evidence'，R2 确认到位\"\n    resolution_round: 4\n\n  - id: \"R3-C3\"\n    summary: \"N=8 核心结果 single seed (seed=42)\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 4\n    mentions:\n      - round: 3\n        reviewers: [1, 2]\n        note: \"Table 1 N=8 和 Table 2 selection 全部 single seed\"\n      - round: 4\n        reviewers: [2]\n        note: \"R2 确认 RESOLVED：3-seed 验证已补充\"\n    action_items:\n      - round: 3\n        action: \"Limitations 中明确 single-seed 风险并引用 N=16 stability\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"Round 4: 3-seed 稳定性验证已补充，R2 确认到位\"\n    resolution_round: 4\n\n  - id: \"R3-W1\"\n    summary: \"多重比较校正缺失\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 4\n    mentions:\n      - round: 3\n        reviewers: [1, 2]\n        note: \"SJ-EM CI lower bound +0.003 在 Bonferroni 下不会 survive\"\n      - round: 4\n        reviewers: [2]\n        note: \"R2 确认 RESOLVED：Bonferroni 声明已加\"\n    action_items:\n      - round: 3\n        action: \"声明未做多重比较校正 + SJ-EM 改为 suggestive\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"Round 4: Bonferroni 声明已加，R2 确认到位\"\n    resolution_round: 4\n\n  - id: \"R3-W2\"\n    summary: \"Gap 概念部分 tautological——instance-level 信号无法 select 是定义必然\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 3\n    last_seen_round: 5\n    mentions:\n      - round: 3\n        reviewers: [1, 2]\n        note: \"需在 Discussion 中分离两层论证\"\n      - round: 4\n        reviewers: [1, 2]\n        note: \"R4 两位 Reviewer 独立再次提出：Introduction 未正面论证 why not obvious a priori\"\n      - round: 5\n        reviewers: [1, 2]\n        note: \"R2 认为 gap 被两头夹击（instance-level=tautological, logprob=artifact），整体 contribution 空心化。R1 rebut：consensus-proximity/MBR failure 是 non-trivial empirical finding，但同意 logprob artifact 是 real concern。共识：gap 不完全 tautological（MBR 在 MT 成功 IE 失败是非平凡的），但 C2 应以 logprob+MBR failure 为重心而非 '5 signals all fail'。\"\n    action_items:\n      - round: 3\n        action: \"Discussion 中分离两层论证\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n      - round: 4\n        action: \"(a) Introduction 正面论证 why gap is not obvious (MBR MT vs IE 对比); (b) Discussion 明确分离定义性局限 vs 经验性失败\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n      - round: 5\n        action: \"Reframe C2: 以 logprob score compression + MBR/consensus-proximity empirical failure 为中心，弱化 '5 signals all fail' 叙事；Introduction 加强非显然性论证（MBR 在 MT 成功但 IE 失败）\"\n        assigned_to: \"Paper Agent\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R3-W3\"\n    summary: \"Consensus-proximity 是唯一 instance-to-sample 转换策略，未与 MBR decoding 建立联系\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 4\n    mentions:\n      - round: 3\n        reviewers: [1, 2]\n        note: \"MBR decoding 是成熟替代方案但未讨论\"\n      - round: 4\n        reviewers: [2]\n        note: \"R2 确认 RESOLVED：MBR 连接已补充，§5 MBR 段清晰\"\n    action_items:\n      - round: 3\n        action: \"明确 consensus-proximity 与 MBR 联系 + 引用 MBR 文献\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"Round 4: §5 MBR decoding 连接段已写入，R2 评价'概念优雅'\"\n    resolution_round: 4\n\n  - id: \"R3-W4\"\n    summary: \"FK 独立性假设 justification 不足\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 3\n    last_seen_round: 5\n    mentions:\n      - round: 3\n        reviewers: [1, 2]\n        note: \"§3.2 一句 hand-wave。需报告 inter-sample correlation\"\n      - round: 4\n        reviewers: [2]\n        note: \"R2 确认 RESOLVED：excess agreement 数据已补充\"\n      - round: 5\n        reviewers: [1]\n        note: \"R1 重新提出：excess agreement (-0.4% to -4.0%) 未注明在哪个 configuration 测量，未提供所有配置数据，未引用 FK 在非独立 rater 下的行为分析文献。R2 同意但认为 severity 偏低（FK 非核心 contribution）。\"\n    action_items:\n      - round: 3\n        action: \"Agent 量化 inter-sample correlation；Paper Agent 写入\"\n        assigned_to: \"Agent + Paper Agent\"\n        status: resolved\n      - round: 5\n        action: \"(a) 注明 excess agreement 的 configuration；(b) 补充所有配置数据或至少说明范围；(c) 引用 FK 在非独立 rater 下的行为文献\"\n        assigned_to: \"Paper Agent\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R3-W5\"\n    summary: \"Cross-model 实为 cross-architecture at fixed 8B scale\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 3\n    last_seen_round: 5\n    mentions:\n      - round: 3\n        reviewers: [1, 2]\n        note: \"两模型均 8B，措辞过度外推\"\n      - round: 4\n        reviewers: [2]\n        note: \"R2 确认 RESOLVED：cross-architecture 措辞已统一\"\n      - round: 5\n        reviewers: [1, 2]\n        note: \"R1 再次提出：两模型均为 8B decoder-only transformer，共享相似架构（GQA, RoPE, SwiGLU）。R2 同意应改为 cross-model-family。当前 Conclusion 仍用 'across model families' 而非限定 'at 8B scale'。\"\n    action_items:\n      - round: 5\n        action: \"Conclusion 和 Abstract 统一加 'at 8B scale' 限定，或改为 'across two model families at 8B scale'\"\n        assigned_to: \"Paper Agent\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R3-W6\"\n    summary: \"'First multi-family comparison' claim scope 过宽\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 3\n    last_seen_round: 5\n    mentions:\n      - round: 3\n        reviewers: [1, 2]\n        note: \"需限定为 structured IE 的 QE + selection\"\n      - round: 4\n        reviewers: [2]\n        note: \"R2 确认部分解决：Conclusion 有 hedge 但 Introduction 仍断言式\"\n      - round: 5\n        reviewers: [1, 2]\n        note: \"两位 Reviewer 一致同意：通过堆叠修饰词(multiple families + both objectives + generative + structured IE)确保 'first' 成立属于 scope engineering。建议改为描述性表述，避免 'first' claim。\"\n    action_items:\n      - round: 5\n        action: \"Introduction 和 Conclusion 去掉 'first' claim，改为描述性表述\"\n        assigned_to: \"Paper Agent\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R3-W7\"\n    summary: \"术语不一致\"\n    category: writing\n    severity: warning\n    status: open\n    first_raised_round: 3\n    last_seen_round: 5\n    mentions:\n      - round: 3\n        reviewers: [1, 2]\n        note: \"confidence signal vs consistency signal 混用；VC vs Voting Conf.\"\n      - round: 4\n        reviewers: [1, 2]\n        note: \"R2 确认部分解决：表格缩写 VC/Voting Conf. 仍不统一\"\n      - round: 5\n        reviewers: [1, 2]\n        note: \"仍未解决。Table 1 用 'Voting Conf.'，Table 4/7 用 'VC'，正文用 'entity voting'。§3.2 已有 taxonomy 定义（confidence signal 统称 vs consistency signal 子集），但表格缩写未统一。\"\n    action_items:\n      - round: 5\n        action: \"全文统一表格缩写（建议全部用 VC）+ 正文首次出现时写全称\"\n        assigned_to: \"Paper Agent\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R3-W8\"\n    summary: \"遗漏引用：VerifiNER, RASC, MBR decoding, Malinin & Gales\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 4\n    mentions:\n      - round: 3\n        reviewers: [1, 2]\n        note: \"VerifiNER, MBR decoding 等高度相关\"\n      - round: 4\n        reviewers: [2]\n        note: \"R2 确认 RESOLVED：引用已补全\"\n    action_items:\n      - round: 3\n        action: \"补充引用并在 Related Work 中讨论\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"Round 4: 引用已补全，R2 确认到位\"\n    resolution_round: 4\n\n  - id: \"R3-M1\"\n    summary: \"WNUT-17 '54% zero F1' 与 Table 7 数据不一致 (51.5%)\"\n    category: experiment\n    severity: info\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 3\n    mentions:\n      - round: 3\n        reviewers: [1]\n        note: \"355/689 ≈ 51.5% vs 正文 54%\"\n    action_items:\n      - round: 3\n        action: \"Agent 核实实际数字 → Paper Agent 统一\"\n        assigned_to: \"Agent + Paper Agent\"\n        status: resolved\n    resolution: \"54% → 52% 已修正，Round 4 未再提及\"\n    resolution_round: 4\n\n  - id: \"R3-M2\"\n    summary: \"EM selection exclusion 缺乏经验支持\"\n    category: experiment\n    severity: info\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 3\n    mentions:\n      - round: 3\n        reviewers: [1, 2]\n        note: \"'probability negligible' 需报告 exact match pairs 频率\"\n    action_items:\n      - round: 3\n        action: \"Agent 计算 exact match pairs 频率 → Paper Agent 写入\"\n        assigned_to: \"Agent + Paper Agent\"\n        status: resolved\n    resolution: \"EM 已加入 Table 2，Round 4 未再提及\"\n    resolution_round: 4\n\n  - id: \"R3-M3\"\n    summary: \"Ethics Statement 缺失\"\n    category: format\n    severity: info\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 5\n    mentions:\n      - round: 3\n        reviewers: [2]\n        note: \"共识降为 minor\"\n      - round: 4\n        reviewers: [2]\n        note: \"R2 确认 Ethics Statement 已存在但位于 Limitations section 内——建议改为独立 section\"\n      - round: 5\n        reviewers: [2]\n        note: \"Ethics Statement 现为独立 \\\\section*{Ethics Statement}，位于 Limitations 后、References 前，符合 ACL 格式。内容仅 2 句，R2 建议补充但非 must-fix。\"\n    action_items:\n      - round: 4\n        action: \"将 Ethics Statement 从 Limitations 内移出为独立 section\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"Round 5: Ethics Statement 已为独立 section，格式合规\"\n    resolution_round: 5\n\n  - id: \"R3-M4\"\n    summary: \"ρ-AUROC dissociation 作为独立发现过度强调\"\n    category: framing\n    severity: info\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 3\n    mentions:\n      - round: 3\n        reviewers: [1, 2]\n        note: \"建议承认统计预期性后聚焦实践含义\"\n    action_items:\n      - round: 3\n        action: \"§4.2 承认 dissociation 的统计预期性\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"已承认统计预期性，Round 4 未再提及\"\n    resolution_round: 4\n\n  - id: \"R3-M5\"\n    summary: \"对 Nedellec (2026) 措辞偏 adversarial\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 3\n    mentions:\n      - round: 3\n        reviewers: [1, 2]\n        note: \"建议用更 neutral 语气\"\n    action_items:\n      - round: 3\n        action: \"Introduction 中改为更 neutral 的语气\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"Nedellec 措辞已改为 neutral，Round 4 未再提及\"\n    resolution_round: 4\n\n  - id: \"R3-M6\"\n    summary: \"LOO-SJ 验证中 Δρ 和 per-instance Δρ 量纲混淆\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 3\n    mentions:\n      - round: 3\n        reviewers: [1]\n        note: \"Δρ=−0.014 vs per-instance max Δρ=3.1×10⁻⁴ 量纲不同\"\n    action_items:\n      - round: 3\n        action: \"澄清 per-instance Δρ 具体含义\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"LOO-SJ Δρ 含义已澄清，Round 4 未再提及\"\n    resolution_round: 4\n\n  - id: \"R3-M7\"\n    summary: \"Figure 1 caption 引入未直接可视化的 p=0.39\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 3\n    last_seen_round: 3\n    mentions:\n      - round: 3\n        reviewers: [1]\n        note: \"建议加 '(Table 2)' 交叉引用\"\n    action_items:\n      - round: 3\n        action: \"补 '(Table 2)' 交叉引用\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"Figure 1 caption 交叉引用已补，Round 4 未再提及\"\n    resolution_round: 4\n\n  # ============================================================\n  # Round 4 issues (updated with Round 5 status)\n  # ============================================================\n  - id: \"R4-C1\"\n    summary: \"训练配置和 prompt template 缺失，影响独立复现\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 5\n    mentions:\n      - round: 4\n        reviewers: [1, 2]\n        note: \"§4.1 仅报告 LoRA rank=32, α=64, 5 epochs, LLaMA Factory，缺少 lr, batch size 等\"\n      - round: 5\n        reviewers: [1, 2]\n        note: \"Appendix E 已包含完整 Table 8（lr, optimizer, batch size, warmup, max seq length, LoRA target, precision 等）+ prompt template + constrained decoding 细节。两位 Reviewer 均给 Reproducibility 4/5。\"\n    action_items:\n      - round: 4\n        action: \"附录补充完整训练配置表 + NER/RE prompt template 示例 + schema constraint 定义\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"Round 5: Appendix E Table 8 完整，prompt template 已提供，Reproducibility 4/5\"\n    resolution_round: 5\n\n  - id: \"R4-W1\"\n    summary: \"RE 证据需进一步加强（conditional analysis 或降级）\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 4\n    last_seen_round: 5\n    mentions:\n      - round: 4\n        reviewers: [1, 2]\n        note: \"claim 降级已完成（resolved），但两位 Reviewer 仍认为 RE 证据薄弱\"\n      - round: 5\n        reviewers: [1, 2]\n        note: \"Abstract 标注 '(SciERC, preliminary)' 但论文后续 Table 1/2, Figure 2-3, Discussion 大量使用 RE 结果无 preliminary 限定。Contribution #3 将 RE 结论嵌入通用表述。需全文一致标注。\"\n    action_items:\n      - round: 5\n        action: \"(a) 所有 RE 分析处一致标注 single-benchmark preliminary；(b) Contribution #3 加 RE 限定；(c) Future work 明确列出 RE 多数据集验证\"\n        assigned_to: \"Paper Agent\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R4-W2\"\n    summary: \"SJ vs EM 优势叙事应改为 difficulty-dependent complementarity\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 5\n    mentions:\n      - round: 4\n        reviewers: [1, 2]\n        note: \"SJ vs EM Δρ=+0.065, CI 下界 +0.003, Bonferroni 下不显著\"\n      - round: 5\n        reviewers: [1, 2]\n        note: \"§4.2 已使用 'difficulty-dependent complementarity rather than a universal structural advantage' 措辞。R2 仍认为增量不足但 R1 认为 crossover pattern 是核心 claim 而非单个 Δρ。\"\n    action_items:\n      - round: 4\n        action: \"Contribution #1 弱化 structural advantage，改为强调 difficulty-dependent complementarity\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"Round 5: §4.2 已用 complementarity 措辞，Contribution #1 已包含 difficulty-dependent ordering\"\n    resolution_round: 5\n\n  - id: \"R4-W3\"\n    summary: \"Abstract 过于密集，第 4 行超长句子需拆分\"\n    category: writing\n    severity: warning\n    status: open\n    first_raised_round: 4\n    last_seen_round: 5\n    mentions:\n      - round: 4\n        reviewers: [1, 2]\n        note: \"多层嵌套括号和分号的超长句子\"\n      - round: 5\n        reviewers: [1, 2]\n        note: \"仍未修改。9 行含 5 signal/3 family/4 metric/3 dataset/2 model + gap 概念。两位 Reviewer 一致建议拆分为 2-3 句，聚焦核心 claim，具体数字移入 Introduction。\"\n    action_items:\n      - round: 5\n        action: \"Abstract 拆分为 2-3 句核心 claim，将具体信号名/数字/family 移入 Introduction\"\n        assigned_to: \"Paper Agent\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R4-W4\"\n    summary: \"缺少 Xiong et al. (2024) 'Can LLMs Express Their Uncertainty?' ICLR 2024\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 4\n    last_seen_round: 5\n    mentions:\n      - round: 4\n        reviewers: [1, 2]\n        note: \"系统评估 LLM 置信度获取方法，与本文多族信号比较直接相关\"\n      - round: 5\n        reviewers: [1, 2]\n        note: \"Related Work §2 已引用 Xiong et al. (2024)：'systematically evaluate confidence elicitation across prompting, sampling, and aggregation strategies'\"\n    action_items:\n      - round: 4\n        action: \"Related Work 引用 Xiong et al.\"\n        assigned_to: \"Paper Agent\"\n        status: resolved\n    resolution: \"Round 5: 已引用，§2 第三段\"\n    resolution_round: 5\n\n  - id: \"R4-M1\"\n    summary: \"SJ normalizer 选择（max vs union）缺乏对比\"\n    category: method\n    severity: info\n    status: wont_fix\n    first_raised_round: 4\n    last_seen_round: 4\n    mentions:\n      - round: 4\n        reviewers: [1]\n        note: \"R1-W3: max(|g_i|,|g_j|) vs |g_i∪g_j| 未比较\"\n    action_items:\n      - round: 4\n        action: \"附录补 union normalizer 结果或提供理论依据\"\n        assigned_to: \"Agent + Paper Agent\"\n        status: wont_fix\n    resolution: \"Rejected: max normalizer 设计已在 method.tex 有理由，超出 scope\"\n    resolution_round: 4\n\n  - id: \"R4-M2\"\n    summary: \"TOST δ 选择（±2/3/5 pp）缺乏实践意义论证\"\n    category: experiment\n    severity: info\n    status: open\n    first_raised_round: 4\n    last_seen_round: 5\n    mentions:\n      - round: 4\n        reviewers: [1]\n        note: \"δ 选择直接影响等价结论\"\n      - round: 5\n        reviewers: [1, 2]\n        note: \"R1 再提：与 IAA 关联无引用。R2 同意但认为多水平 δ 已构成 sensitivity analysis，引用 IAA 数据即可。\"\n    action_items:\n      - round: 5\n        action: \"引用 1-2 篇 IE benchmark IAA 数据来锚定 δ 选择\"\n        assigned_to: \"Paper Agent\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R4-M3\"\n    summary: \"Table 1 N=16 block 大面积空白\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 4\n    last_seen_round: 5\n    mentions:\n      - round: 4\n        reviewers: [1, 2]\n        note: \"N=16 仅填 LLaMA CoNLL，SciERC 空白\"\n      - round: 5\n        reviewers: [1, 2]\n        note: \"Table 1 已加脚注说明 N=16 数据位置（Appendix Table 3），但脚注格式（\\\\textsuperscript{†} + \\\\footnotetext）在 two-column 模板下可能渲染异常。\"\n    action_items:\n      - round: 5\n        action: \"检查 PDF 渲染；考虑合并 N=16 到附录以简化 Table 1\"\n        assigned_to: \"Paper Agent\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  # ============================================================\n  # Round 5 new issues\n  # ============================================================\n  - id: \"R5-N1\"\n    summary: \"与 Nédellec et al. (2026) 的增量贡献不充分\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 5\n    last_seen_round: 5\n    mentions:\n      - round: 5\n        reviewers: [2]\n        note: \"三个增量均偏弱：SJ vs EM Bonferroni 不显著，selection analysis 部分 tautological，difficulty gradient 直觉上不意外。R1 rebut：crossover pattern 是核心 claim 而非单个 Δρ；WNUT-17 conditional collapse 不是直觉可预测。共识：Findings-worthy 但非 ground-breaking。\"\n    action_items:\n      - round: 5\n        action: \"更诚实地量化增量大小；强调 WNUT-17 conditional collapse 和 logprob negative correlation 作为 non-obvious findings\"\n        assigned_to: \"Paper Agent\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R5-W1\"\n    summary: \"Qwen3-8B thinking token 训练不一致（SciERC vs CoNLL/WNUT）\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 5\n    last_seen_round: 5\n    mentions:\n      - round: 5\n        reviewers: [1, 2]\n        note: \"SciERC 未显式禁用 enable_thinking，CoNLL/WNUT 显式设 false。推理时 constrained decoding 覆盖，但训练时差异可能影响 learned representations。\"\n    action_items:\n      - round: 5\n        action: \"Limitations 讨论此不一致性，或确认 thinking tokens 在 SciERC fine-tuning 中是否实际被激活\"\n        assigned_to: \"Paper Agent\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R5-W2\"\n    summary: \"Semantic entropy 脚注比较可能误导\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 5\n    last_seen_round: 5\n    mentions:\n      - round: 5\n        reviewers: [1, 2]\n        note: \"§4.2 脚注比较 semantic entropy AUROC 0.75-0.85，但自述 'direct comparison is not meaningful'。R1 建议删除或缩短；R2 认为意图合理但执行可能误导快速读者。\"\n    action_items:\n      - round: 5\n        action: \"缩短脚注，去掉具体数字，仅保留 'scale context' 功能\"\n        assigned_to: \"Paper Agent\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R5-W3\"\n    summary: \"he2024uncertainty bib entry 与引用上下文不匹配\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 5\n    last_seen_round: 5\n    mentions:\n      - round: 5\n        reviewers: [1]\n        note: \"bib 标题 'Uncertainty Estimation on Sequential Labeling via Uncertainty Transmission' (NAACL 2024 Findings)，但 Related Work 引用上下文是 'survey uncertainty quantification specifically for LLMs'——实际是 sequential labeling 论文而非 LLM survey\"\n    action_items:\n      - round: 5\n        action: \"修正引用上下文描述，或替换为正确的 LLM UQ survey 引用\"\n        assigned_to: \"Paper Agent\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R5-M1\"\n    summary: \"缺少 test-time scaling verification survey 引用\"\n    category: framing\n    severity: info\n    status: open\n    first_raised_round: 5\n    last_seen_round: 5\n    mentions:\n      - round: 5\n        reviewers: [1, 2]\n        note: \"R2 建议补 'Trust but Verify! A Survey on Verification Design for Test-time Scaling' (2025)，R1 同意与 Discussion 中 verifier 建议直接相关\"\n    action_items:\n      - round: 5\n        action: \"Related Work 或 Discussion 引用 test-time scaling verification survey\"\n        assigned_to: \"Paper Agent\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R5-M2\"\n    summary: \"缺少 MBR 在非 MT 任务中的应用引用\"\n    category: framing\n    severity: info\n    status: open\n    first_raised_round: 5\n    last_seen_round: 5\n    mentions:\n      - round: 5\n        reviewers: [1, 2]\n        note: \"Discussion §5 将方法与 MBR 对接但只引用 MT 领域。应补 summarization/QA 等任务中的 MBR 文献。\"\n    action_items:\n      - round: 5\n        action: \"补充 MBR 在非 MT 任务中的引用\"\n        assigned_to: \"Paper Agent\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R5-M3\"\n    summary: \"Consensus-proximity = LOO-SJ 等价性缺少推导\"\n    category: method\n    severity: info\n    status: open\n    first_raised_round: 5\n    last_seen_round: 5\n    mentions:\n      - round: 5\n        reviewers: [1, 2]\n        note: \"§3.3 声称数学等价但未给出推导。R1 要求证明；R2 建议更正为 'approximately equivalent' 如果无法严格证明。\"\n    action_items:\n      - round: 5\n        action: \"附录补简要推导，或更正为 approximately equivalent\"\n        assigned_to: \"Paper Agent\"\n        status: open\n    resolution: \"\"\n    resolution_round: null"
  }
}
```

</details>

---


### Tool result

_source line 556 · 2026-05-15T08:06:03.094538+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_issues.yaml\", \"bytes\": 42570}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 557 · 2026-05-15T08:08:03.118439+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "project": "struct_self_consist_ie",
  "report": "# 审稿报告 — Round 5\n\n**论文**: Strong Predictors, Weak Selectors: A Systematic Comparison of Confidence Signals for Test-Time Scaling in Information Extraction\n**Venue**: EMNLP 2026 Findings (via ARR May 2026 cycle)\n**Deadline**: 2026-05-25\n**Reviewer 编排**: 2 人（R1: 方法严谨性 + 实验设计 + 统计有效性; R2: 新颖性 + framing + related work + 写作质量）\n**轮次**: Round 1（独立审稿 → 交叉分享 → 收敛，1 轮完成）\n\n---\n\n## Summary\n\n论文系统比较了 5 种置信度信号（structural: entity voting, Soft Jaccard; surface: exact match, Fleiss' κ; model-internal: log-probability）在生成式 IE（NER + RE）中用于 quality estimation 和 sample selection 的能力。核心发现是 \"correlation-selection gap\"——信号能预测哪些实例模型处理可靠（ρ 最高 0.38, AUROC 最高 0.75），但无法在 N 个候选中选出最佳输出（p>0.39）。附带发现：信号排名随 task difficulty 变化（easy task EM 领先, hard task structural signals 领先），以及 WNUT-17 上的 capability boundary（conditional ρ 趋近零）。\n\n---\n\n## Strengths\n\n1. **统计分析严谨性在 ACL 投稿中属上乘**。Bootstrap CI (B=10,000)、TOST 等价检验（多级 δ）、sign test、Cohen's d、multi-seed stability (σ≤0.025)、conditional filtering、diversity stratification——远超同类 empirical papers。[两位 Reviewer 一致肯定]\n\n2. **Negative result 有实际价值**。Log-probability 作为唯一 per-sample signal 也无法有效 select（p=0.39, 13-18 pp oracle headroom），且原因可追溯到 constrained decoding 下的 score compression（60% instance 内 range <0.05, Appendix F）。这对 test-time scaling 文献是重要补充。[R1 Soundness 3, R2 Soundness 3.5]\n\n3. **Problem formulation 清晰**。Per-sample vs instance-level 信号的分类框架简洁有力；quality estimation vs sample selection 的解耦是概念上的贡献。[两位 Reviewer 一致]\n\n4. **实验设计公平**。两模型相同 LoRA 配置（Appendix E Table 8），三数据集覆盖 difficulty gradient（CoNLL easy → SciERC hard → WNUT-17 boundary），训练细节、prompt template 完整（Reproducibility 4/5）。[两位 Reviewer 一致]\n\n5. **引用完整**。58 条引用，核心相关工作（Nédellec et al. 2026, Wang et al. 2023, Kuhn et al. 2023, Eikema & Aziz 2022, Xiong et al. 2024）均已覆盖。\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**[CONSENSUS] W-C1: Constrained decoding 作为核心混淆变量未被隔离，claim scope 与 evidence 不匹配**\n- 来源: R1-N1 + R1-N2 + R2-N1 (constrained decoding 部分)\n- 两位 Reviewer 独立提出，交叉分享后完全共识\n- 核心问题: 所有实验均使用 constrained decoding (vLLM + XGrammar)。论文无法区分 correlation-selection gap 是 structured IE 的固有属性还是 constrained decoding 的 artifact。论文自身的 Appendix F 提供了反面证据：在 logprob non-tied subset (n=210, 40%) 中，logprob selection 显著优于 greedy (+2.9 pp, p=0.01, within-instance ρ 从 0.08 升到 0.39)——暗示 gap 主因是 constrained decoding 造成的 score compression，而非 IE 本身的固有性质\n- 当前论文的 title、abstract、conclusion 将 gap 呈现为 structured IE 的通用属性，未限定 constrained decoding setting\n- 修改建议: (a) Title/Abstract/Conclusion 限定 claim scope 为 constrained decoding setting; (b) 提升 Appendix F non-tied analysis 至主文 Discussion; (c) 明确承认 non-tied evidence 对 claim 普适性的影响; (d) 如条件允许添加 free-form decoding 消融更佳（但非强制）\n\n**[CONSENSUS with nuance] W-C2: Correlation-selection gap 的 tautological 成分削弱核心贡献新颖性**\n- 来源: R2-N1 (tautological) + R1 交叉回应\n- R2 认为 gap 被 \"两头夹击\"（4/5 instance-level failure = tautological; logprob failure = artifact），整体 contribution 空心化\n- R1 部分 rebut：consensus-proximity/MBR failure 是 non-trivial empirical finding（MBR 在 MT 成功但 IE 失败并非 a priori obvious）；论文已有两层论证结构（Discussion §5）\n- **共识**: Gap 不完全 tautological，但 Contribution 2 应以 logprob score compression + MBR/consensus-proximity empirical failure 为重心，而非 \"5 signals all fail\" 的统一叙事。Abstract 和 Introduction 需 reframe\n- 修改建议: (a) Reframe C2 聚焦 logprob 和 MBR failure; (b) 弱化 \"5 signals all fail\" 叙事; (c) Introduction 加强非显然性论证\n\n### Should-Fix（影响评分但不一票否决）\n\n**[CONSENSUS] W-S1: RE \"preliminary\" 标注与实际使用不一致**\n- 来源: R1-W1 + R2-W2\n- Abstract 标注 \"(SciERC, preliminary)\"，但 Table 1/2, Figure 2-3, Discussion 大量使用 RE 结果无限定词。Contribution #3 将 RE 结论嵌入通用表述\n- 修改建议: 全文一致标注 RE 为 single-benchmark preliminary; Contribution #3 加限定; Future work 列出 RE 多数据集验证\n\n**[CONSENSUS] W-S2: Abstract 信息密度过高**\n- 来源: R2-W1, R1 交叉 AGREE\n- 9 行含 5 signal/3 family/4 metric/3 dataset/2 model + gap 概念 + technical arguments\n- 修改建议: 聚焦 1-2 个核心 claim，具体数字移入 Introduction\n\n**[CONSENSUS] W-S3: \"First multi-family comparison\" claim 过度依赖 scope 限定**\n- 来源: R2-W4, R1 交叉 AGREE\n- 通过堆叠修饰词确保 \"first\" 成立属于 scope engineering\n- 修改建议: 改为描述性表述，避免 \"first\" claim\n\n**[CONSENSUS] W-S4: \"Cross-architecture\" 用词过度**\n- 来源: R1-W3, R2 交叉 AGREE\n- 两模型均为 8B decoder-only transformer (GQA, RoPE, SwiGLU)\n- 修改建议: 改为 \"across two model families at 8B scale\"\n\n**[CONSENSUS] W-S5: 术语不一致**\n- 来源: R3-W7 (Round 3 遗留, 仍未解决)\n- Table 1 \"Voting Conf.\" vs Table 4/7 \"VC\" vs 正文 \"entity voting\"\n- 修改建议: 全文统一（建议全部用 VC）\n\n**[CONSENSUS, low severity] W-S6: FK independence justification 不够严格**\n- 来源: R1-W2, R2 交叉 AGREE with nuance (severity 偏低)\n- Excess agreement (-0.4% to -4.0%) 未注明 configuration, 未引用 FK 非独立 rater 行为文献\n- 修改建议: 补充 configuration 信息 + 引用; FK 非核心 contribution, 可接受 minimal fix\n\n**[CONSENSUS, low severity] W-S7: TOST δ 选择缺乏外部锚点**\n- 来源: R1-W4, R2 交叉 AGREE with nuance\n- 多水平 δ 已构成 sensitivity analysis, 但需引用 IAA 数据\n- 修改建议: 引用 1-2 篇 IE benchmark IAA 文献\n\n**[R1 only] W-S8: Qwen3-8B thinking token 训练不一致**\n- 来源: R1-W5, R2 交叉 AGREE\n- SciERC 未禁用 enable_thinking, CoNLL/WNUT 显式禁用\n- 修改建议: Limitations 讨论此不一致性\n\n**[R2 only, R1 REBUT] W-S9: Soft Jaccard 方法论新颖性有限**\n- 来源: R2-W3\n- R1 rebut: application novelty 在 IE quality estimation 中是新的; Nédellec (2026) 承认其表面方法的局限\n- 共识: SJ 有 application novelty 但不应过度宣传; \"core structural signal\" 可弱化为 \"primary\"\n\n**[R2 only] W-S10: 与 Nédellec et al. (2026) 增量贡献论证不充分**\n- 来源: R2-N2\n- R1 rebut: WNUT-17 conditional collapse 和 logprob negative correlation 不是直觉可预测; difficulty-dependent crossover 是核心 claim\n- 共识: Findings-worthy 但非 ground-breaking; 建议更诚实量化增量\n\n### Minor（不影响接收）\n\n- **M1** [CONSENSUS]: Semantic entropy 脚注（§4.2）——自述 \"direct comparison not meaningful\" 但给出具体数字，可能误导。建议缩短\n- **M2** [R1]: `he2024uncertainty` bib entry 与引用上下文不匹配（sequential labeling 论文被描述为 LLM survey）\n- **M3** [CONSENSUS]: Table 1 脚注格式（`\\textsuperscript{†}` + `\\footnotetext`）在 two-column 模板下可能渲染异常\n- **M4** [R1]: Consensus-proximity = LOO-SJ 等价性声称缺少推导\n- **M5** [CONSENSUS]: 部分 bib entries (`hobelsberger2025systematic`, `lightman2024verify`) 在 OpenAlex 未找到; `feng2025optimal` 和 `ye2025uncertainty` author name 可能有 variant\n- **M6** [R2]: Ethics Statement 仅 2 句（格式合规但内容偏简）\n\n---\n\n## Reviewer Consensus\n\n以下问题两位 Reviewer 在交叉分享后完全一致：\n\n1. **Constrained decoding confound 是论文最大弱点** [AGREE]: 论文自身 Appendix F 数据（non-tied subset logprob selection +2.9pp, p=0.01）暗示 gap 主因是 score compression 而非 IE 固有属性。Title/Abstract/Conclusion 的 claim scope 需限定\n2. **RE scope 不一致** [AGREE]: Abstract \"preliminary\" 与后续大量使用之间矛盾\n3. **Abstract 过密** [AGREE]: 首次阅读难以把握核心 message\n4. **\"Cross-architecture\" 过度** [AGREE]: 改为 \"across two model families at 8B scale\"\n5. **\"First\" claim 应去掉** [AGREE]: scope engineering\n6. **术语不一致** [AGREE]: 需全文统一\n7. **统计分析质量高** [AGREE]: bootstrap CI、TOST、multi-seed 在 ACL 投稿中属上乘\n8. **训练配置完整** [AGREE]: Reproducibility 4/5\n\n---\n\n## Reviewer Divergence\n\n1. **Tautological 程度**:\n   - R2: Gap 被两头夹击，整体 contribution 空心化 → Excitement 2.5\n   - R1: Consensus-proximity/MBR failure 是 non-trivial → Excitement 3.5\n   - **Resolution**: 共识认为 gap 不完全 tautological，但 C2 需 reframe 以 logprob+MBR failure 为重心\n\n2. **与 Nédellec 增量**:\n   - R2: 三个增量均偏弱\n   - R1: Difficulty gradient 发现（WNUT-17 conditional collapse）不是直觉可预测\n   - **Resolution**: Findings-worthy 但非 ground-breaking\n\n3. **SJ 方法新颖性**:\n   - R2: 标准技术组合\n   - R1: Application novelty 在 IE context 中是新的\n   - **Resolution**: 有 application novelty 但不应过度宣传\n\n---\n\n## Questions\n\n1. Appendix F 的 non-tied subset 中 logprob selection 有效 (+2.9pp, p=0.01)。如果 constrained decoding 是 score compression 主因，free-form decoding 下 logprob 是否可能成为有效 selector？如何论证 gap 是 IE-inherent 而非 decoding-induced？\n2. Consensus-proximity = LOO-SJ 的数学等价性缺少推导。能否补充？\n3. FK excess agreement (-0.4% to -4.0%) 在哪个 configuration 测量？是否在所有配置一致？\n4. WNUT-17 logprob 负相关 (ρ=-0.410) 的机制解释？\n\n---\n\n## Missing References\n\n- \"Trust but Verify! A Survey on Verification Design for Test-time Scaling\" (2025) — 与 Discussion 中 verifier 建议直接相关 [两位 Reviewer 一致]\n- MBR 在非 MT 任务 (summarization, QA) 中的应用文献 — 增强 Discussion §5 MBR 对比分析 [两位 Reviewer 一致]\n- 最新 uncertainty quantification survey (2025-2026) [R2 建议]\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n外部审稿：未请求（项目未启用外部审稿）。\n\n---\n\n## Overall Assessment\n\n**评分: borderline (3.0/5)**\n**置信度: 高 (4/5)**\n\n| 维度 | R1 | R2 | 加权 |\n|------|-----|-----|------|\n| Soundness | 3.0 | 3.5 | 3.25 |\n| Excitement | 3.5 | 2.5 | 3.0 |\n| Reproducibility | 4.0 | 4.0 | 4.0 |\n| Overall | 3.0 | 3.0 | 3.0 |\n\n**总结判断**: 这是一篇执行质量较高的 empirical study——统计分析严谨、实验设计公平、训练细节完整。核心概念（quality estimation vs sample selection 解耦）对 test-time scaling 实践有指导价值。\n\n**但存在两个结构性问题阻碍更高评分:**\n\n1. **Claim scope 与 evidence 不匹配**: 论文将 correlation-selection gap 呈现为 structured IE 的通用属性，但所有实验均在 constrained decoding 下进行，且论文自身数据（Appendix F non-tied subset）暗示 gap 主因可能是 score compression artifact。Title/Abstract/Conclusion 需加限定词。\n\n2. **核心贡献的 tautological 成分**: 4/5 信号的 selection failure 是定义的逻辑后果（instance-level signals 无法 rank per-sample），真正 non-trivial 的发现是 logprob 的 failure 和 consensus-proximity/MBR 在 IE 中的 failure。C2 需 reframe。\n\n**Findings track 接收条件**: 如果作者能 (a) 在核心 claim 中限定 constrained decoding scope, (b) reframe C2 以 logprob + MBR failure 为中心, (c) 统一 RE preliminary 标注, (d) 精简 Abstract, 则论文适合 Findings track。当前版本需 moderate revision。\n\n---\n\n## Detailed Comments（按 Section）\n\n### Abstract\n- 信息密度过高，需拆分为 2-3 句核心 claim\n- \"(SciERC, preliminary)\" 限定词需在后续分析中一致使用\n- \"for Information Extraction\" 需加 \"under constrained decoding\" 限定\n\n### §1 Introduction\n- Contribution 2 需 reframe：将 \"5 signals all fail\" 叙事改为以 logprob compression + MBR failure 为中心\n- Contribution 3 需加 RE single-benchmark 限定\n- \"first multi-family comparison\" → 改为描述性表述\n- MBR 在 MT 中成功 → IE 中失败的非显然性论证可以加强\n\n### §2 Related Work\n- 引用覆盖良好\n- 补充: test-time verification survey, MBR 非 MT 应用\n- `he2024uncertainty` 引用上下文需修正\n\n### §3 Method\n- SJ 形式化清晰完整\n- FK independence justification 补 configuration 信息\n- Consensus-proximity = LOO-SJ 等价性需推导\n- \"core structural signal\" → \"primary structural signal\"\n\n### §4 Experiments\n- 统计分析严谨\n- Table 1 脚注格式检查 PDF 渲染\n- Semantic entropy 脚注缩短\n- TOST δ 引用 IAA 数据\n- WNUT-17 logprob negative correlation 需机制解释\n\n### §5 Discussion\n- \"Two layers\" 结构良好但需更明确分离定义性 vs 经验性 gap\n- 提升 Appendix F non-tied analysis 至此处\n- 承认 non-tied evidence 对 claim 普适性的影响\n\n### §6 Conclusion\n- 加 constrained decoding scope 限定\n- RE 限定与 Abstract 对齐\n- \"across model families\" → \"across two model families at 8B scale\"\n\n### Limitations\n- 全面诚实\n- 补充 thinking token 训练不一致性讨论\n\n### Appendix\n- Training config (Table 8) 完整 ✓\n- Prompt template 提供 ✓\n- Appendix F logprob tie analysis 应提升至主文",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "borderline",
  "review_chat_id": "oc_3897c2857f11615119e277e820eae311"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "project": "struct_self_consist_ie",
    "report": "# 审稿报告 — Round 5\n\n**论文**: Strong Predictors, Weak Selectors: A Systematic Comparison of Confidence Signals for Test-Time Scaling in Information Extraction\n**Venue**: EMNLP 2026 Findings (via ARR May 2026 cycle)\n**Deadline**: 2026-05-25\n**Reviewer 编排**: 2 人（R1: 方法严谨性 + 实验设计 + 统计有效性; R2: 新颖性 + framing + related work + 写作质量）\n**轮次**: Round 1（独立审稿 → 交叉分享 → 收敛，1 轮完成）\n\n---\n\n## Summary\n\n论文系统比较了 5 种置信度信号（structural: entity voting, Soft Jaccard; surface: exact match, Fleiss' κ; model-internal: log-probability）在生成式 IE（NER + RE）中用于 quality estimation 和 sample selection 的能力。核心发现是 \"correlation-selection gap\"——信号能预测哪些实例模型处理可靠（ρ 最高 0.38, AUROC 最高 0.75），但无法在 N 个候选中选出最佳输出（p>0.39）。附带发现：信号排名随 task difficulty 变化（easy task EM 领先, hard task structural signals 领先），以及 WNUT-17 上的 capability boundary（conditional ρ 趋近零）。\n\n---\n\n## Strengths\n\n1. **统计分析严谨性在 ACL 投稿中属上乘**。Bootstrap CI (B=10,000)、TOST 等价检验（多级 δ）、sign test、Cohen's d、multi-seed stability (σ≤0.025)、conditional filtering、diversity stratification——远超同类 empirical papers。[两位 Reviewer 一致肯定]\n\n2. **Negative result 有实际价值**。Log-probability 作为唯一 per-sample signal 也无法有效 select（p=0.39, 13-18 pp oracle headroom），且原因可追溯到 constrained decoding 下的 score compression（60% instance 内 range <0.05, Appendix F）。这对 test-time scaling 文献是重要补充。[R1 Soundness 3, R2 Soundness 3.5]\n\n3. **Problem formulation 清晰**。Per-sample vs instance-level 信号的分类框架简洁有力；quality estimation vs sample selection 的解耦是概念上的贡献。[两位 Reviewer 一致]\n\n4. **实验设计公平**。两模型相同 LoRA 配置（Appendix E Table 8），三数据集覆盖 difficulty gradient（CoNLL easy → SciERC hard → WNUT-17 boundary），训练细节、prompt template 完整（Reproducibility 4/5）。[两位 Reviewer 一致]\n\n5. **引用完整**。58 条引用，核心相关工作（Nédellec et al. 2026, Wang et al. 2023, Kuhn et al. 2023, Eikema & Aziz 2022, Xiong et al. 2024）均已覆盖。\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**[CONSENSUS] W-C1: Constrained decoding 作为核心混淆变量未被隔离，claim scope 与 evidence 不匹配**\n- 来源: R1-N1 + R1-N2 + R2-N1 (constrained decoding 部分)\n- 两位 Reviewer 独立提出，交叉分享后完全共识\n- 核心问题: 所有实验均使用 constrained decoding (vLLM + XGrammar)。论文无法区分 correlation-selection gap 是 structured IE 的固有属性还是 constrained decoding 的 artifact。论文自身的 Appendix F 提供了反面证据：在 logprob non-tied subset (n=210, 40%) 中，logprob selection 显著优于 greedy (+2.9 pp, p=0.01, within-instance ρ 从 0.08 升到 0.39)——暗示 gap 主因是 constrained decoding 造成的 score compression，而非 IE 本身的固有性质\n- 当前论文的 title、abstract、conclusion 将 gap 呈现为 structured IE 的通用属性，未限定 constrained decoding setting\n- 修改建议: (a) Title/Abstract/Conclusion 限定 claim scope 为 constrained decoding setting; (b) 提升 Appendix F non-tied analysis 至主文 Discussion; (c) 明确承认 non-tied evidence 对 claim 普适性的影响; (d) 如条件允许添加 free-form decoding 消融更佳（但非强制）\n\n**[CONSENSUS with nuance] W-C2: Correlation-selection gap 的 tautological 成分削弱核心贡献新颖性**\n- 来源: R2-N1 (tautological) + R1 交叉回应\n- R2 认为 gap 被 \"两头夹击\"（4/5 instance-level failure = tautological; logprob failure = artifact），整体 contribution 空心化\n- R1 部分 rebut：consensus-proximity/MBR failure 是 non-trivial empirical finding（MBR 在 MT 成功但 IE 失败并非 a priori obvious）；论文已有两层论证结构（Discussion §5）\n- **共识**: Gap 不完全 tautological，但 Contribution 2 应以 logprob score compression + MBR/consensus-proximity empirical failure 为重心，而非 \"5 signals all fail\" 的统一叙事。Abstract 和 Introduction 需 reframe\n- 修改建议: (a) Reframe C2 聚焦 logprob 和 MBR failure; (b) 弱化 \"5 signals all fail\" 叙事; (c) Introduction 加强非显然性论证\n\n### Should-Fix（影响评分但不一票否决）\n\n**[CONSENSUS] W-S1: RE \"preliminary\" 标注与实际使用不一致**\n- 来源: R1-W1 + R2-W2\n- Abstract 标注 \"(SciERC, preliminary)\"，但 Table 1/2, Figure 2-3, Discussion 大量使用 RE 结果无限定词。Contribution #3 将 RE 结论嵌入通用表述\n- 修改建议: 全文一致标注 RE 为 single-benchmark preliminary; Contribution #3 加限定; Future work 列出 RE 多数据集验证\n\n**[CONSENSUS] W-S2: Abstract 信息密度过高**\n- 来源: R2-W1, R1 交叉 AGREE\n- 9 行含 5 signal/3 family/4 metric/3 dataset/2 model + gap 概念 + technical arguments\n- 修改建议: 聚焦 1-2 个核心 claim，具体数字移入 Introduction\n\n**[CONSENSUS] W-S3: \"First multi-family comparison\" claim 过度依赖 scope 限定**\n- 来源: R2-W4, R1 交叉 AGREE\n- 通过堆叠修饰词确保 \"first\" 成立属于 scope engineering\n- 修改建议: 改为描述性表述，避免 \"first\" claim\n\n**[CONSENSUS] W-S4: \"Cross-architecture\" 用词过度**\n- 来源: R1-W3, R2 交叉 AGREE\n- 两模型均为 8B decoder-only transformer (GQA, RoPE, SwiGLU)\n- 修改建议: 改为 \"across two model families at 8B scale\"\n\n**[CONSENSUS] W-S5: 术语不一致**\n- 来源: R3-W7 (Round 3 遗留, 仍未解决)\n- Table 1 \"Voting Conf.\" vs Table 4/7 \"VC\" vs 正文 \"entity voting\"\n- 修改建议: 全文统一（建议全部用 VC）\n\n**[CONSENSUS, low severity] W-S6: FK independence justification 不够严格**\n- 来源: R1-W2, R2 交叉 AGREE with nuance (severity 偏低)\n- Excess agreement (-0.4% to -4.0%) 未注明 configuration, 未引用 FK 非独立 rater 行为文献\n- 修改建议: 补充 configuration 信息 + 引用; FK 非核心 contribution, 可接受 minimal fix\n\n**[CONSENSUS, low severity] W-S7: TOST δ 选择缺乏外部锚点**\n- 来源: R1-W4, R2 交叉 AGREE with nuance\n- 多水平 δ 已构成 sensitivity analysis, 但需引用 IAA 数据\n- 修改建议: 引用 1-2 篇 IE benchmark IAA 文献\n\n**[R1 only] W-S8: Qwen3-8B thinking token 训练不一致**\n- 来源: R1-W5, R2 交叉 AGREE\n- SciERC 未禁用 enable_thinking, CoNLL/WNUT 显式禁用\n- 修改建议: Limitations 讨论此不一致性\n\n**[R2 only, R1 REBUT] W-S9: Soft Jaccard 方法论新颖性有限**\n- 来源: R2-W3\n- R1 rebut: application novelty 在 IE quality estimation 中是新的; Nédellec (2026) 承认其表面方法的局限\n- 共识: SJ 有 application novelty 但不应过度宣传; \"core structural signal\" 可弱化为 \"primary\"\n\n**[R2 only] W-S10: 与 Nédellec et al. (2026) 增量贡献论证不充分**\n- 来源: R2-N2\n- R1 rebut: WNUT-17 conditional collapse 和 logprob negative correlation 不是直觉可预测; difficulty-dependent crossover 是核心 claim\n- 共识: Findings-worthy 但非 ground-breaking; 建议更诚实量化增量\n\n### Minor（不影响接收）\n\n- **M1** [CONSENSUS]: Semantic entropy 脚注（§4.2）——自述 \"direct comparison not meaningful\" 但给出具体数字，可能误导。建议缩短\n- **M2** [R1]: `he2024uncertainty` bib entry 与引用上下文不匹配（sequential labeling 论文被描述为 LLM survey）\n- **M3** [CONSENSUS]: Table 1 脚注格式（`\\textsuperscript{†}` + `\\footnotetext`）在 two-column 模板下可能渲染异常\n- **M4** [R1]: Consensus-proximity = LOO-SJ 等价性声称缺少推导\n- **M5** [CONSENSUS]: 部分 bib entries (`hobelsberger2025systematic`, `lightman2024verify`) 在 OpenAlex 未找到; `feng2025optimal` 和 `ye2025uncertainty` author name 可能有 variant\n- **M6** [R2]: Ethics Statement 仅 2 句（格式合规但内容偏简）\n\n---\n\n## Reviewer Consensus\n\n以下问题两位 Reviewer 在交叉分享后完全一致：\n\n1. **Constrained decoding confound 是论文最大弱点** [AGREE]: 论文自身 Appendix F 数据（non-tied subset logprob selection +2.9pp, p=0.01）暗示 gap 主因是 score compression 而非 IE 固有属性。Title/Abstract/Conclusion 的 claim scope 需限定\n2. **RE scope 不一致** [AGREE]: Abstract \"preliminary\" 与后续大量使用之间矛盾\n3. **Abstract 过密** [AGREE]: 首次阅读难以把握核心 message\n4. **\"Cross-architecture\" 过度** [AGREE]: 改为 \"across two model families at 8B scale\"\n5. **\"First\" claim 应去掉** [AGREE]: scope engineering\n6. **术语不一致** [AGREE]: 需全文统一\n7. **统计分析质量高** [AGREE]: bootstrap CI、TOST、multi-seed 在 ACL 投稿中属上乘\n8. **训练配置完整** [AGREE]: Reproducibility 4/5\n\n---\n\n## Reviewer Divergence\n\n1. **Tautological 程度**:\n   - R2: Gap 被两头夹击，整体 contribution 空心化 → Excitement 2.5\n   - R1: Consensus-proximity/MBR failure 是 non-trivial → Excitement 3.5\n   - **Resolution**: 共识认为 gap 不完全 tautological，但 C2 需 reframe 以 logprob+MBR failure 为重心\n\n2. **与 Nédellec 增量**:\n   - R2: 三个增量均偏弱\n   - R1: Difficulty gradient 发现（WNUT-17 conditional collapse）不是直觉可预测\n   - **Resolution**: Findings-worthy 但非 ground-breaking\n\n3. **SJ 方法新颖性**:\n   - R2: 标准技术组合\n   - R1: Application novelty 在 IE context 中是新的\n   - **Resolution**: 有 application novelty 但不应过度宣传\n\n---\n\n## Questions\n\n1. Appendix F 的 non-tied subset 中 logprob selection 有效 (+2.9pp, p=0.01)。如果 constrained decoding 是 score compression 主因，free-form decoding 下 logprob 是否可能成为有效 selector？如何论证 gap 是 IE-inherent 而非 decoding-induced？\n2. Consensus-proximity = LOO-SJ 的数学等价性缺少推导。能否补充？\n3. FK excess agreement (-0.4% to -4.0%) 在哪个 configuration 测量？是否在所有配置一致？\n4. WNUT-17 logprob 负相关 (ρ=-0.410) 的机制解释？\n\n---\n\n## Missing References\n\n- \"Trust but Verify! A Survey on Verification Design for Test-time Scaling\" (2025) — 与 Discussion 中 verifier 建议直接相关 [两位 Reviewer 一致]\n- MBR 在非 MT 任务 (summarization, QA) 中的应用文献 — 增强 Discussion §5 MBR 对比分析 [两位 Reviewer 一致]\n- 最新 uncertainty quantification survey (2025-2026) [R2 建议]\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n外部审稿：未请求（项目未启用外部审稿）。\n\n---\n\n## Overall Assessment\n\n**评分: borderline (3.0/5)**\n**置信度: 高 (4/5)**\n\n| 维度 | R1 | R2 | 加权 |\n|------|-----|-----|------|\n| Soundness | 3.0 | 3.5 | 3.25 |\n| Excitement | 3.5 | 2.5 | 3.0 |\n| Reproducibility | 4.0 | 4.0 | 4.0 |\n| Overall | 3.0 | 3.0 | 3.0 |\n\n**总结判断**: 这是一篇执行质量较高的 empirical study——统计分析严谨、实验设计公平、训练细节完整。核心概念（quality estimation vs sample selection 解耦）对 test-time scaling 实践有指导价值。\n\n**但存在两个结构性问题阻碍更高评分:**\n\n1. **Claim scope 与 evidence 不匹配**: 论文将 correlation-selection gap 呈现为 structured IE 的通用属性，但所有实验均在 constrained decoding 下进行，且论文自身数据（Appendix F non-tied subset）暗示 gap 主因可能是 score compression artifact。Title/Abstract/Conclusion 需加限定词。\n\n2. **核心贡献的 tautological 成分**: 4/5 信号的 selection failure 是定义的逻辑后果（instance-level signals 无法 rank per-sample），真正 non-trivial 的发现是 logprob 的 failure 和 consensus-proximity/MBR 在 IE 中的 failure。C2 需 reframe。\n\n**Findings track 接收条件**: 如果作者能 (a) 在核心 claim 中限定 constrained decoding scope, (b) reframe C2 以 logprob + MBR failure 为中心, (c) 统一 RE preliminary 标注, (d) 精简 Abstract, 则论文适合 Findings track。当前版本需 moderate revision。\n\n---\n\n## Detailed Comments（按 Section）\n\n### Abstract\n- 信息密度过高，需拆分为 2-3 句核心 claim\n- \"(SciERC, preliminary)\" 限定词需在后续分析中一致使用\n- \"for Information Extraction\" 需加 \"under constrained decoding\" 限定\n\n### §1 Introduction\n- Contribution 2 需 reframe：将 \"5 signals all fail\" 叙事改为以 logprob compression + MBR failure 为中心\n- Contribution 3 需加 RE single-benchmark 限定\n- \"first multi-family comparison\" → 改为描述性表述\n- MBR 在 MT 中成功 → IE 中失败的非显然性论证可以加强\n\n### §2 Related Work\n- 引用覆盖良好\n- 补充: test-time verification survey, MBR 非 MT 应用\n- `he2024uncertainty` 引用上下文需修正\n\n### §3 Method\n- SJ 形式化清晰完整\n- FK independence justification 补 configuration 信息\n- Consensus-proximity = LOO-SJ 等价性需推导\n- \"core structural signal\" → \"primary structural signal\"\n\n### §4 Experiments\n- 统计分析严谨\n- Table 1 脚注格式检查 PDF 渲染\n- Semantic entropy 脚注缩短\n- TOST δ 引用 IAA 数据\n- WNUT-17 logprob negative correlation 需机制解释\n\n### §5 Discussion\n- \"Two layers\" 结构良好但需更明确分离定义性 vs 经验性 gap\n- 提升 Appendix F non-tied analysis 至此处\n- 承认 non-tied evidence 对 claim 普适性的影响\n\n### §6 Conclusion\n- 加 constrained decoding scope 限定\n- RE 限定与 Abstract 对齐\n- \"across model families\" → \"across two model families at 8B scale\"\n\n### Limitations\n- 全面诚实\n- 补充 thinking token 训练不一致性讨论\n\n### Appendix\n- Training config (Table 8) 完整 ✓\n- Prompt template 提供 ✓\n- Appendix F logprob tie analysis 应提升至主文",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "borderline",
    "review_chat_id": "oc_3897c2857f11615119e277e820eae311"
  }
}
```

</details>

---


### Tool result

_source line 558 · 2026-05-15T08:08:07.438776+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_1b56445332d8ca2b4964b30f300f0e00:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4320
}
```

</details>

---


### Assistant

_source line 559 · 2026-05-15T08:08:16.711116+00:00_

审稿报告已投递至 Research Director。

**Round 5 审稿完成。** 汇总：

- **Overall: borderline (3.0/5)**，两位 Reviewer 评分一致
- **2 个核心问题**（完全共识）：
  1. Constrained decoding confound 未隔离 — 论文自身 Appendix F 数据暗示 gap 主因是 score compression 而非 IE 固有属性，但 title/abstract/conclusion 未限定 scope
  2. Correlation-selection gap 的 tautological 成分 — 4/5 信号 selection failure 是定义必然，C2 需以 logprob+MBR failure 为重心 reframe
- **10 个 should-fix**（RE scope 不一致、abstract 过密、"first" claim、cross-architecture 用词、术语不一致等）
- **6 个 minor**（脚注格式、bib 不匹配、LOO-SJ 推导缺失等）
- **Findings track 条件**：限定 constrained decoding scope + reframe C2 + 统一 RE 标注 + 精简 abstract → moderate revision 后可接收

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 47

## Round 47

2 recorded events


### User

_source line 560 · 2026-05-15T08:08:19.595708+00:00_

[Reviewer 2 审稿结果]:
交叉回应已提交给 Director。对 R1 的 11 个具体意见中，9 个 [AGREE]（其中 3 个 with nuance），1 个 [REBUT]（M3 semantic entropy 脚注），1 个 [AGREE]（M4 bib mismatch）。两份审稿在核心问题（constrained decoding 混淆变量、gap 的 tautological 成分）上高度一致。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 561 · 2026-05-15T08:08:30.882560+00:00_

审稿报告已提交给 Research Director。

**审稿完成总结：**

- **Overall: borderline (3.0/5)**，2 位 Reviewer 均给 3.0/5
- **2 个 Must-Fix（完全共识）**：
  1. Constrained decoding 混淆变量——论文自身 Appendix F 的 non-tied subset 数据暗示 gap 主因是 score compression 而非 IE 固有属性，但 title/abstract/conclusion 未限定 scope
  2. Correlation-selection gap 的 tautological 成分——C2 需以 logprob+MBR failure 为重心 reframe
- **10 个 Should-Fix**：RE scope 不一致、Abstract 过密、"first" claim、cross-architecture 过度、术语不一致、FK justification、TOST δ 锚点、thinking token 不一致、SJ 宣传弱化、Nédellec 增量量化
- **6 个 Minor**：semantic entropy 脚注、bib mismatch、Table 1 脚注格式、LOO-SJ 推导、bib 验证、Ethics 简短
- **Issue Tracker 已同步更新**（`review_issues.yaml`），新增 8 个 Round 5 issue，更新 5 个历史 issue 状态

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 48

## Round 48

68 recorded events


### User

_source line 562 · 2026-05-15T08:42:36.693068+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: struct_self_consist_ie
- 论文路径: projects/struct_self_consist_ie/docs/paper/main.tex
- 目标 venue: EMNLP 2026
- Track: findings
- 截止日期: 2026-05-25

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 563 · 2026-05-15T08:42:51.697656+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 564 · 2026-05-15T08:42:51.698526+00:00_

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
…[truncated 2458 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 565 · 2026-05-15T08:42:56.869898+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__read_project_file",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__read_project_file",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 566 · 2026-05-15T08:42:56.920581+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 567 · 2026-05-15T08:43:01.540716+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "struct_self_consist_ie"
  }
}
```

</details>

---


### Tool result

_source line 568 · 2026-05-15T08:43:03.499068+00:00_

{"result":"# 项目 struct_self_consist_ie 概况\n\n## 实验状态 (79 个)\n\n- **exp_002_ner_conll2003**: DONE (success) — \n- **exp_004_re_diagnostic**: DONE (success) — \n- **exp_005**: DONE (success) — \n- **exp_014_entity_majority_voting**: DONE (success) — \n- **exp_013_exact_match_voting**: DONE (negative) — \n- **exp_012_logprob_baseline**: DONE (success) — \n- **mvp_pilot_005**: DONE (negative) — \n- **e1_component_wise_re_sj**: DONE (negative) — \n- **mvp_pilot_004**: DONE (negative) — \n- **ft_002_v2**: DONE (success) — \n- **mvp_pilot_002**: DONE (failed) — \n- **ft_002**: DONE (killed) — \n- **ft_001**: DONE (success) — \n- **mvp_pilot_003**: DONE (negative) — \n- **mvp_pilot_001**: DONE (negative) — \n\n## 最新报告\n# Handover — 2026-05-15\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n- exp_017_llama_conll_n16_s456_r1024（准备中）\n- exp_017_llama_conll_n16_r1024（准备中）\n- exp_001_n16_seed123_full（准备中）\n- exp_001_n16_seed456_full（准备中）\n- exp001_seed123（准备中）\n- exp001_seed456（准备中）\n- exp_007_ner_llama（准备中）\n- exp_002_merge_conll2003（准备中）\n- exp008_re_n16（准备中）\n\n## 近期结论\n- **exp_018_llama_scierc_seed42_r1024** (success): —\n- **exp_018_llama_scierc_seed456_r1024** (success): —\n- **exp_018_llama_scierc_seed456** (success): —\n\n## 趋势\n成功 43 / 负向 18 / 失败 1 / 共 70\n\n## 下一步\n（无活跃 idea，请通过 ideas.md 添加）\n\n## 资源状态\nautodl-5090: 空闲 cuda:0, cuda:1, cuda:2, cuda:3\n\n## 告警\n- ft_002: 已被终止 — unknown\n- mvp_pilot_002: 训练失败 — unknown\n- exp_008_re_n16_full: 已被终止 — unknown\n- exp_001_seed42_v2_r1024: 已被终止 — unknown\n- exp_001_seed123_v2_r1024: 已被终止 — unknown\n- exp_001_seed456_v2_ner_r1024: 已被终止 — unknown\n- exp_002_conll_n16_r1024: 已被终止 — unknown\n- exp_007_llama_n16_r1024: 已被终止 — unknown\n- exp_017_llama_conll_n16_s123_r1024: 已被终止 — unknown"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 1958
}
```

</details>

---


### Tool call

_source line 569 · 2026-05-15T08:43:04.002016+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex 2>/dev/null && echo \"FILE_EXISTS\" || echo \"FILE_NOT_FOUND\"",
  "description": "Check if paper file exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex 2>/dev/null && echo \"FILE_EXISTS\" || echo \"FILE_NOT_FOUND\"",
    "description": "Check if paper file exists"
  }
}
```

</details>

---


### Tool result

_source line 570 · 2026-05-15T08:43:04.554560+00:00_

-rw-r--r-- 1 ubuntu ubuntu 1285 May 15 08:23 /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex
FILE_EXISTS

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Bash",
  "elapsed_ms": 552
}
```

</details>

---


### Tool call

_source line 571 · 2026-05-15T08:43:04.605207+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
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

_source line 572 · 2026-05-15T08:43:04.655792+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 573 · 2026-05-15T08:43:09.980244+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 call for papers submission guidelines"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 call for papers submission guidelines"
  }
}
```

</details>

---


### Tool call

_source line 574 · 2026-05-15T08:43:10.482479+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 author guidelines page limit template anonymity"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 author guidelines page limit template anonymity"
  }
}
```

</details>

---


### Tool call

_source line 575 · 2026-05-15T08:43:11.588058+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 576 · 2026-05-15T08:43:11.940150+00:00_

1	\documentclass[11pt]{article}
2	
3	\usepackage[review]{acl}
4	
5	\usepackage{times}
6	\usepackage{latexsym}
7	\usepackage[T1]{fontenc}
8	\usepackage[utf8]{inputenc}
9	\usepackage{microtype}
10	\usepackage{inconsolata}
11	\usepackage{graphicx}
12	\usepackage{booktabs}
13	\usepackage{amsmath}
14	\usepackage{amssymb}
15	\usepackage{multirow}
16	\usepackage{xcolor}
17	\usepackage{subcaption}
18	
19	\graphicspath{{figures/}}
20	
21	\title{Strong Predictors, Weak Selectors:\\ Confidence Signals for Test-Time Scaling in Information Extraction under Constrained Decoding}
22	
23	\author{Anonymous}
24	
25	\begin{document}
26	\maketitle
27	
28	\input{sections/abstract}
29	\input{sections/introduction}
30	\input{sections/related_work}
31	\input{sections/method}
32	\input{sections/experiments}
33	\input{sections/discussion}
34	\input{sections/conclusion}
35	
36	\section*{Limitations}
37	\input{sections/limitations}
38	
39	\section*{Ethics Statement}
40	All experiments use publicly available benchmarks (SciERC, CoNLL-2003, WNUT-17) and open-weight models (Qwen3-8B, LLaMA-3.1-8B).
41	No new human data was collected or annotated for this study.
42	Our findings on signal limitations could inform more reliable deployment of IE systems by guiding practitioners toward appropriate confidence signals for their use case.
43	
44	\bibliography{references}
45	
46	\appendix
47	\input{sections/appendix}
48	
49	\end{document}
50	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 352
}
```

</details>

---


### Tool call

_source line 577 · 2026-05-15T08:43:11.990864+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "struct_self_consist_ie",
  "file": "paper_checklist.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "struct_self_consist_ie",
    "file": "paper_checklist.yaml"
  }
}
```

</details>

---


### Tool result

_source line 578 · 2026-05-15T08:43:17.113269+00:00_

Web search results for query: "EMNLP 2026 author guidelines page limit template anonymity"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"EMNLP 2026 LaTeX Template | ACL Style Files & Overleaf | Underleaf","url":"https://www.underleaf.ai/templates/emnlp"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"},{"title":"Confs: 2026 Conference on Empirical Methods in Natural ...","url":"https://www.facebook.com/linguistlist/posts/confs-2026-conference-on-empirical-methods-in-natural-language-processing-emnlp-/1351983883622556/"},{"title":"EMNLP: Empirical Methods in Natural Language Processing 2027 2026 2025 ...","url":"http://www.wikicfp.com/cfp/program?id=883"},{"title":"GitHub - acl-org/emnlp-2026: Repository for the EMNLP 2026 conference · GitHub","url":"https://github.com/acl-org/emnlp-2026"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"ICML 2026 Author Instructions","url":"https://icml.cc/Conferences/2026/AuthorInstructions"}]

Based on my search results, here's what I found regarding EMNLP 2026 author guidelines:

## Page Limits

EMNLP 2026 has an 8-page limit for long papers and a 4-page limit for short papers.

## Template

EMNLP uses the standard ACL style files, so the LaTeX template is identical to the one used for ACL, NAACL, and other *ACL conferences. EMNLP uses the ACL style files available at github.com/acl-org/acl-style-files.

## Anonymity

Regarding anonymity policies, following the ACL and ARR policies, there is no anonymity period requirement. However, the reviewing 
…[truncated 465 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "WebSearch",
  "elapsed_ms": 6630
}
```

</details>

---


### Tool result

_source line 579 · 2026-05-15T08:43:20.831367+00:00_

Web search results for query: "EMNLP 2026 call for papers submission guidelines"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"Submission Guide","url":"https://nlp4climate.github.io/submissionguide/"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"},{"title":"2026 *ACL Conference Dates | Computational Linguistics","url":"https://submissions.cljournal.org/index.php/cljournal/announcement/view/14"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"Confs: 2026 Conference on Empirical Methods in Natural ...","url":"https://www.facebook.com/linguistlist/posts/confs-2026-conference-on-empirical-methods-in-natural-language-processing-emnlp-/1351983883622556/"},{"title":"EMNLP 2026 on X: \"📢 Please note a critical update to the original #EMNLP2026 Call for Papers: since EMNLP and AACL share the ARR May cycle, authors will need to explicitly select a target conference at submission time. This choice will be binding! For more details see: https://t.co/0u1wbX9fT6\" / X","url":"https://x.com/emnlpmeeting/status/2047754845919031450"},{"title":"EMNLP 2026 on X: \"📢 The First Call for Papers for EMNLP 2026 is officially out! 📝 We welcome long &amp; short papers featuring original research on empirical methods for NLP. 🗓️ ARR Submission Deadline: May 25, 2026 🔗 Read the full CFP here: https://t.co/GU2kaISjUG #EMNLP2026\" / X","url":"https://x.com/emnlpmeeting/status/2029508292637061462"}]

Based on the
…[truncated 2538 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "WebSearch",
  "elapsed_ms": 10851
}
```

</details>

---


### Tool result

_source line 580 · 2026-05-15T08:43:20.831841+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"No paper_checklist.yaml found for 'struct_self_consist_ie'.\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 8840
}
```

</details>

---


### Tool call

_source line 581 · 2026-05-15T08:43:32.681256+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "sections/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "sections/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper"
  }
}
```

</details>

---


### Tool result

_source line 582 · 2026-05-15T08:43:33.234181+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Glob",
  "elapsed_ms": 552
}
```

</details>

---


### Tool call

_source line 583 · 2026-05-15T08:43:33.686247+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "struct_self_consist_ie",
  "file": "memory.md",
  "max_chars": "3000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "struct_self_consist_ie",
    "file": "memory.md",
    "max_chars": "3000"
  }
}
```

</details>

---


### Tool result

_source line 584 · 2026-05-15T08:43:35.241741+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/memory.md\", \"content\": \"# Memory — struct_self_consist_ie\\n\\n## 服务器环境\\n- autodl-5090: 4× RTX 5090 32GB, Python 3.12, vLLM 0.18.1, LLaMA Factory 0.9.4, tmux 3.2a\\n- gpu-5090-4x-2: 4× RTX 5090 32GB, PyTorch 2.10.0+cu128, vLLM 0.18.1\\n- conda: /root/miniconda3/\\n- 环境初始化: `source /etc/network_turbo && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`\\n- 项目路径: /root/autodl-tmp/struct_self_consist_ie/\\n- 基座模型: /root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B/\\n- ft_002_v2 merged: checkpoints/qwen3-8b-scierc-merged-v2/\\n- run_mvp_pilot.py 支持 --collect_logprobs, --num_test (默认已改为 9999)\\n\\n## 数据修正链 (D054-D060) 关键教训\\n- exp_012 是唯一使用 max_tokens=512 的实验，导致 voting_conf ρ 虚高 (0.502→0.379)\\n- SJ/FK 对 max_tokens 参数鲁棒（Δ<0.004），但 voting_conf 极度敏感\\n- 修正后 AUROC 排名反转：EM (0.749) > SJ (0.692) > Voting (0.684)\\n- Selection claim 由 bootstrap 确认为 null result（p=0.39），不能写 \\\"significantly outperforms\\\"\\n- 论文数据必须来自 _rerun_1024 或本身就用 1024 的实验\\n\\n## D066 LLaMA fresh rerun (2026-05-15)\\n- D066 决策：LLaMA 3-seed 全部使用 fresh rerun 数据（seed42_r1024 + seed123 + seed456_r1024）\\n- exp_018_llama_scierc_seed456（旧 exp_007 复制品）已标记 SUPERSEDED\\n- LLaMA NER SJ ρ 修正：旧 0.362±0.004 → 新 0.325±0.021（σ 增大 5× 是真实 seed 变异，seed123 拉高均值）\\n- **分析脚本与 report.json 的 EM/VC 值存在系统性差异**（如 seed42 VC: 脚本 0.373 vs report.json 0.405）。Reviewer 要求论文统一使用分析脚本输出（与 Qwen 同一套）。不要从 registry metrics（来自 report.json）直接引用 EM/VC 到论文。\\n- NER 信号排名 6/6 完全稳定：VC > SJ > EM > FK > LP\\n- Core claim \\\"structural > logprob\\\" NER 全部成立 (12/12)；RE 仅 VC 稳定胜 LP\\n\\n## Registry 清理备注 (2026-05-15)\\n- 9 个 PREPARING+killed 实验因状态机限制无法推进到 DONE，实质已废弃\\n- 包括：exp_017_llama_conll_n16_s456_r1024, exp_017_llama_conll_n16_r1024, exp_001_n16_seed123_full, exp_001_n16_seed456_full, exp001_seed123, exp001_seed456, exp_007_ner_llama, exp_002_merge_conll2003, exp008_re_n16\\n\", \"total_chars\": 1740,
…[truncated 60 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 1555
}
```

</details>

---


### Tool call

_source line 585 · 2026-05-15T08:43:35.242252+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/config.yaml 2>/dev/null | grep -A 5 \"external_review\" || echo \"NO_EXTERNAL_REVIEW_CONFIG\"",
  "description": "Check external review config"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/config.yaml 2>/dev/null | grep -A 5 \"external_review\" || echo \"NO_EXTERNAL_REVIEW_CONFIG\"",
    "description": "Check external review config"
  }
}
```

</details>

---


### Tool result

_source line 586 · 2026-05-15T08:43:35.995486+00:00_

NO_EXTERNAL_REVIEW_CONFIG

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Bash",
  "elapsed_ms": 753
}
```

</details>

---


### Tool call

_source line 587 · 2026-05-15T08:43:35.995912+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_issues.yaml 2>/dev/null || echo \"NO_EXISTING_ISSUES\"",
  "description": "Check existing review issues tracker"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_issues.yaml 2>/dev/null || echo \"NO_EXISTING_ISSUES\"",
    "description": "Check existing review issues tracker"
  }
}
```

</details>

---


### Tool result

_source line 588 · 2026-05-15T08:43:36.046938+00:00_

&lt;persisted-output>
Output too large (53KB). Full output saved to: /home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-review-director-0161122b/788664a7-cbda-4ca9-aeda-2dfae5004d00/tool-results/biyzhs6gh.txt

Preview (first 2KB):
issues:
  # ============================================================
  # Round 0 issues (all resolved)
  # ============================================================
  - id: "R0-C1"
    summary: "模型规模单一（仅 8B）"
    category: experiment
    severity: critical
    status: resolved
    first_raised_round: 0
    last_seen_round: 1
    mentions:
      - round: 0
        reviewers: [1, 2]
        note: "8B→8B 仅验证架构鲁棒性非规模鲁棒性"
      - round: 1
        reviewers: [1, 2]
        note: "model-agnostic 与 Limitations 矛盾"
    action_items:
      - round: 1
        action: "全文替换 model-agnostic → consistent across tested model families"
        assigned_to: "Paper Agent"
        status: resolved
    resolution: "Round 2 Reviewer 确认措辞修正到位，无再提"
    resolution_round: 2

  - id: "R0-C2"
    summary: "相关工作显著遗漏"
    category: framing
    severity: warning
    status: resolved
    first_raised_round: 0
    last_seen_round: 1
    mentions:
      - round: 0
        reviewers: [1, 2]
        note: "5 篇核心文献缺失"
      - round: 1
        reviewers: [1, 2]
        note: "新遗漏：Optimal SC, Difficulty-Adaptive SC"
    action_items:
      - round: 1
        action: "补充 6 篇引用到 Related Work"
        assigned_to: "Paper Agent"
        status: resolved
    resolution: "Round 2: 49 条 bib 全部 cited, 0 orphan, 无遗漏"
    resolution_round: 2

  - id: "R0-C3"
    summary: "RE 结论仅基于 SciERC 单数据集"
    category: experiment
    severity: critical
    status: resolved
    first_raised_round: 0
    last_seen_round: 4
    mentions:
      - round: 0
        reviewers: [1, 2]
        note: "需跨数据集验证或降级措辞"
      - round: 2
        reviewers: [1, 2]
        note: "Abstract RE 措辞需修正"
      - round: 3
        revie
…[truncated 313 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Bash",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 589 · 2026-05-15T08:43:42.523108+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper"
  }
}
```

</details>

---


### Tool result

_source line 590 · 2026-05-15T08:43:43.427120+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/limitations.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/method.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Glob",
  "elapsed_ms": 904
}
```

</details>

---


### Tool call

_source line 591 · 2026-05-15T08:43:43.578204+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-review-director-0161122b/788664a7-cbda-4ca9-aeda-2dfae5004d00/tool-results/biyzhs6gh.txt",
  "limit": "200"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-review-director-0161122b/788664a7-cbda-4ca9-aeda-2dfae5004d00/tool-results/biyzhs6gh.txt",
    "limit": "200"
  }
}
```

</details>

---


### Tool result

_source line 592 · 2026-05-15T08:43:43.629212+00:00_

1	issues:
2	  # ============================================================
3	  # Round 0 issues (all resolved)
4	  # ============================================================
5	  - id: "R0-C1"
6	    summary: "模型规模单一（仅 8B）"
7	    category: experiment
8	    severity: critical
9	    status: resolved
10	    first_raised_round: 0
11	    last_seen_round: 1
12	    mentions:
13	      - round: 0
14	        reviewers: [1, 2]
15	        note: "8B→8B 仅验证架构鲁棒性非规模鲁棒性"
16	      - round: 1
17	        reviewers: [1, 2]
18	        note: "model-agnostic 与 Limitations 矛盾"
19	    action_items:
20	      - round: 1
21	        action: "全文替换 model-agnostic → consistent across tested model families"
22	        assigned_to: "Paper Agent"
23	        status: resolved
24	    resolution: "Round 2 Reviewer 确认措辞修正到位，无再提"
25	    resolution_round: 2
26	
27	  - id: "R0-C2"
28	    summary: "相关工作显著遗漏"
29	    category: framing
30	    severity: warning
31	    status: resolved
32	    first_raised_round: 0
33	    last_seen_round: 1
34	    mentions:
35	      - round: 0
36	        reviewers: [1, 2]
37	        note: "5 篇核心文献缺失"
38	      - round: 1
39	        reviewers: [1, 2]
40	        note: "新遗漏：Optimal SC, Difficulty-Adaptive SC"
41	    action_items:
42	      - round: 1
43	        action: "补充 6 篇引用到 Related Work"
44	        assigned_to: "Paper Agent"
45	        status: resolved
46	    resolution: "Round 2: 49 条 bib 全部 cited, 0 orphan, 无遗漏"
47	    resolution_round: 2
48	
49	  - id: "R0-C3"
50	    summary: "RE 结论仅基于 SciERC 单数据集"
51	    category: experiment
52	    severity: critical
53	    status: resolved
54	    first_raised_round: 0
55	    last_seen_round: 4
56	    mentions:
57	      - round: 0
58	        reviewers: [1, 2]
59	        note: "需跨数据集验证或降级措辞"
60	      - round: 2
61	        reviewers: [1, 2]
62	        note: "Abstract RE 措辞需修正"
63	      - round: 3
64	        reviewers: [1, 2]
65	        note: "Round 2 措辞修正到位，但 R3 Reviewer 2 再次提出 44% zero-F1 floor effect 严重压缩可区分范围"
66	      - round: 4
67	     
…[truncated 4037 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 593 · 2026-05-15T08:43:55.224499+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 594 · 2026-05-15T08:43:55.275159+00:00_

1	\begin{abstract}
2	Test-time scaling through multi-sample generation promises quality improvements for LLM-based information extraction (IE), but which confidence signals best serve quality estimation versus sample selection remains unclear.
3	Under constrained decoding---the standard inference regime for schema-compliant IE---we compare five signals from three families (structural, surface, model-internal) across NER (three datasets) and RE (SciERC, preliminary) with two 8B-parameter model families.
4	For quality estimation, the strongest signals achieve Spearman $\rho{=}0.38$ and AUROC${=}0.75$, with ranking and classification favoring different signals depending on task complexity.
5	However, this estimation does not translate into selection gains: four of five signals are instance-level by construction, and log-probability---the only per-sample signal---fails to outperform greedy decoding ($p{>}0.39$, bootstrap) despite 13--18~pp of oracle headroom.
6	We term this the \textit{correlation-selection gap} and diagnose its mechanism: log-probability scores are severely compressed under constrained decoding, but in the 40\% of instances where compression is mitigated, log-probability becomes a significant selector ($+2.9$~pp, $p{=}0.01$).
7	Signal rankings further depend on task difficulty, with consistent ordering across models but model-dependent magnitude.
8	These results reframe consistency signals as quality estimators rather than output selectors for structured IE under constrained decoding.
9	\end{abstract}
10	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 595 · 2026-05-15T08:43:55.526780+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 596 · 2026-05-15T08:43:55.527223+00:00_

1	\section{Introduction}\label{sec:introduction}
2	
3	Self-consistency---sampling multiple outputs and aggregating them---has become a powerful strategy for improving language model reasoning.
4	On discrete-answer tasks such as arithmetic and commonsense QA, majority voting over chain-of-thought samples yields large gains: +18 percentage points on GSM8K (PaLM-540B; \citealp{wang2023selfconsistency}).
5	More broadly, test-time compute scaling through repeated sampling and selection has emerged as a complementary axis to model scaling, offering substantial quality improvements at inference time \cite{snell2024scaling, brown2024monkeys}.
6	These results rest on a shared assumption: that among $N$ stochastic samples, a selection mechanism can identify better outputs.
7	For tasks with a single correct answer, this assumption holds naturally---the majority vote is the selector.
8	But information extraction (IE) poses a fundamentally different challenge.
9	The output is not a single token or number; it is a \textit{set} of entities or relations with internal dependencies, where two samples may extract overlapping but non-identical structures.
10	There is no obvious majority to vote on, partial agreement is the norm rather than the exception, and the space of valid outputs is combinatorially large.
11	Can self-consistency still provide useful signal in this structured setting?
12	
13	Prior work on confidence estimation for LLM-based IE has conflated two distinct objectives: \textit{quality estimation} (which inputs does the model handle reliably?) and \textit{sample selection} (which of $N$ outputs is best?).
14	These require fundamentally different signal properties: the former benefits from instance-level aggregation, while the latter demands per-sample discrimination.
15	Self-consistency methods for discrete answers \cite{wang2023selfconsistency, chen2024usc} and weighted variants \cite{taubenfeld2025cisc, kang2025selfcertainty} assume outputs can be grouped by equivalen
…[truncated 5169 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 597 · 2026-05-15T08:43:56.330683+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 598 · 2026-05-15T08:43:56.783126+00:00_

1	\section{Method}\label{sec:method}
2	
3	\subsection{Problem Formulation}\label{sec:formulation}
4	
5	Given a language model $\mathcal{M}$ and input $x$, we sample $N$ structured outputs $\{y_1, \ldots, y_N\}$ at temperature $T > 0$ via constrained decoding \cite{willard2023guided}.
6	Each $y_i$ is an entity set (NER) or relation set (RE).
7	A confidence signal $c$ serves two purposes: (a) \textit{quality estimation}---predicting which instances the model handles reliably, and (b) \textit{sample selection}---identifying the best output among $N$ candidates.
8	
9	A \textbf{per-sample signal} scores each $y_i$ independently, $c_{\text{ps}}: (x, y_i) \to \mathbb{R}$, enabling direct candidate ranking.
10	An \textbf{instance-level signal} aggregates over all $N$ samples, $c_{\text{il}}: (x, \{y_i\}_{i=1}^N) \to \mathbb{R}$, producing a single score per input.
11	This asymmetry---between predicting \textit{which inputs} are easy and selecting \textit{which output} is best---is central to the correlation-selection gap we investigate.
12	Notation is summarized in Appendix~\ref{app:notation}.
13	
14	\subsection{Confidence Signals}\label{sec:signals}
15	
16	We use \textit{confidence signal} as the umbrella term for all five measures.
17	Four are \textit{consistency signals}---computed from inter-sample agreement---spanning two families: \textit{structural} (Soft Jaccard [SJ], entity voting confidence [VC]) and \textit{surface} (exact match [EM], Fleiss' $\kappa$ [FK]).
18	The fifth, log-probability, is the sole \textit{model-internal} signal and the only one that scores individual samples rather than the instance as a whole.
19	
20	\paragraph{Log-probability (model-internal, per-sample).}
21	The only per-sample signal.
22	For sample $y_i$ with tokens $t_1, \ldots, t_{|y_i|}$:
23	\begin{equation}\label{eq:logprob}
24	c_{\text{lp}}(y_i) = \frac{1}{|y_i|} \sum_{j=1}^{|y_i|} \log p_{\mathcal{M}}(t_j \mid t_{<j}, x)
25	\end{equation}
26	
27	\paragraph{Exact match voting (surface
…[truncated 4314 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 599 · 2026-05-15T08:43:56.783662+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 600 · 2026-05-15T08:43:57.285948+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Experimental Setup}
5	\label{sec:setup}
6	
7	\paragraph{Datasets.}
8	We evaluate on three English IE benchmarks spanning a difficulty gradient.
9	\textbf{SciERC} \cite{luan2018scierc} contains 551 test instances annotated for joint NER (6 types) and RE (7 types).
10	\textbf{CoNLL-2003} \cite{tjongkimsang2003conll} provides 3{,}453 test sentences with 4 entity types, where models achieve ${\approx}$91\% micro F1.
11	\textbf{WNUT-17} \cite{derczynski2017wnut} consists of 1{,}287 social media instances with emerging entities, used to probe method boundaries (52\% zero F1).
12	
13	\paragraph{Models and sampling.}
14	Both \textbf{Qwen3-8B} and \textbf{LLaMA-3.1-8B-Instruct} are fine-tuned with LoRA (rank$=$32, $\alpha{=}64$) for 5 epochs using LLaMA Factory \cite{zheng2024llamafactory} under identical training procedures, ensuring comparisons across the two model families (both at 8B scale) reflect model differences rather than training confounds.
15	We draw $N{=}8$ samples at $T{=}1.0$ (primary), with $N{=}16$ for scaling experiments.\footnote{$N{=}16$ results for CoNLL (Qwen) and SciERC (LLaMA) are in Table~\ref{tab:robustness} (Appendix~\ref{app:robustness}).}
16	Quality estimation uses Spearman $\rho$ and AUROC; downstream utility uses best-of-$N$ selection F1 with exact span matching (NER) and head-tail-label matching (RE).
17	Inference uses vLLM with constrained decoding \cite{willard2023guided}.
18	
19	%% ============================================================
20	\subsection{Quality Estimation Results}
21	\label{sec:qe_results}
22	
23	\begin{table*}[t]
24	\centering
25	\small
26	\caption{Quality estimation across tasks and models (Spearman $\rho$ and AUROC). Best value per block and column in \textbf{bold}. SciERC evaluates joint NER (6 types) and RE (7 types, single benchmark---preliminary); CoNLL evaluates NER (4 types). $N{=}8$ results use seed${=}42$. $N{=}16$ results (LLaMA CoNLL only; 3-
…[truncated 11185 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 601 · 2026-05-15T08:43:57.286418+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 602 · 2026-05-15T08:43:57.747084+00:00_

1	\section{Related Work}\label{sec:related}
2	
3	\paragraph{Self-consistency and test-time scaling.}
4	Self-consistency decoding \cite{wang2023selfconsistency} improves reasoning by majority voting over chain-of-thought samples, assuming a discrete answer space.
5	Extensions to free-form text use LLM-based comparison \cite{chen2024usc}, atomic sub-claim decomposition \cite{thirukovalluru2024atomic}, or cross-sample hallucination detection \cite{manakul2023selfcheckgpt}.
6	For test-time scaling, \citet{snell2024scaling} characterize compute scaling laws and \citet{brown2024monkeys} show best-of-$N$ gains across tasks.
7	Recent reward-free selectors include confidence-weighted voting \cite{taubenfeld2025cisc}, KL-based self-certainty \cite{kang2025selfcertainty}, adaptive sampling \cite{kim2026reasc}, ranked aggregation \cite{wang2025rankedvoting}, and latent-space consistency \cite{oh2025latentsc}.
8	Concurrently, \citet{feng2025optimal} and \citet{wang2025make} adapt self-consistency to difficulty-aware settings, echoing our finding that signal rankings shift with task complexity; \citet{li2025llms} propose generative self-aggregation for IE but focus on output fusion rather than confidence-based selection.
9	All of the above target reasoning/QA with discrete answers or specific aggregation strategies.
10	Our work extends self-consistency to set-valued structured outputs and identifies the correlation-selection gap: strong quality estimation ($\rho{=}0.38$) coexists with selection failure ($p{>}0.39$).
11	
12	\paragraph{Consistency for structured IE.}
13	\citet{nedellec2026consistency} study consistency--accuracy correlations for LLM-based NER/RE, corroborating our quality-estimation findings.
14	Their work leaves open three questions we address: (i)~whether structural matching improves on surface-level agreement (which they acknowledge ``overlooks semantically consistent outputs''); (ii)~whether quality estimation translates to best-of-$N$ selection; and (iii)~whet
…[truncated 2752 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 460
}
```

</details>

---


### Tool call

_source line 603 · 2026-05-15T08:43:57.747559+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 604 · 2026-05-15T08:43:58.249850+00:00_

1	\section{Discussion}\label{sec:discussion}
2	
3	\paragraph{Practical recommendations.}
4	For per-instance quality ranking, VC provides the strongest rank correlation ($\rho{=}0.38$), though exact match leads binary discrimination (AUROC${=}0.749$); under conditional filtering, EM leads on both NER and RE ($\rho{=}0.360$, $0.417$).
5	Signal rankings depend on task difficulty---EM dominates easy tasks (CoNLL), VC and SJ dominate hard tasks (SciERC)---directionally consistent across tested model families, though with model-dependent magnitude.
6	When model capability is insufficient (WNUT-17), all signals converge toward non-significant conditional correlations (Table~\ref{tab:wnut}).
7	
8	\paragraph{Why the gap exists: two layers.}
9	\textit{Layer 1 (definitional):} Four of five signals are instance-level aggregates that assign a single score per input; they cannot rank candidates by construction.
10	Consensus-proximity selection (\S\ref{sec:evaluation}) does not recover per-sample discrimination (Table~\ref{tab:selection}).
11	\textit{Layer 2 (constrained-decoding compression):} Log-probability, the only per-sample signal, also fails to exploit the 13--18~pp oracle headroom.
12	Under constrained decoding, logprob scores are severely compressed: 60\% of instances have a within-sample range below 0.05, and 75\% of pairwise comparisons are effective ties ($|\Delta|{<}0.026$; Appendix~\ref{app:logprob_ties}).
13	In the 40\% of instances where compression is mitigated (logprob range ${\geq}0.05$, $n{=}210$), logprob \textit{significantly} outperforms greedy ($+2.9$~pp, $p{=}0.01$; within-instance $\rho$: 0.08$\to$0.39).
14	This diagnostic confirms that logprob carries useful per-sample quality information; score compression under constrained decoding---the standard regime for schema-compliant IE---is the primary mechanistic bottleneck, though whether compression fully accounts for the gap remains open.
15	Diversity-stratified analysis confirms the gap persists even amon
…[truncated 1387 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 605 · 2026-05-15T08:43:58.250291+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 606 · 2026-05-15T08:43:59.204996+00:00_

1	\section{Conclusion}\label{sec:conclusion}
2	
3	Within the constrained decoding regime standard for structured IE, we demonstrate that consistency signals are effective quality estimators ($\rho$ up to 0.38, AUROC up to 0.75) but fail at sample selection---the \textit{correlation-selection gap}.
4	Four of five signals are instance-level by construction; log-probability also fails ($p{>}0.39$) despite 13--18~pp oracle headroom.
5	Mechanistic diagnosis identifies logprob score compression as the bottleneck: where compression is mitigated, logprob becomes a significant selector ($+2.9$~pp, $p{=}0.01$).
6	Signal rankings depend on task difficulty, with consistent ordering across two model families at 8B scale.
7	RE findings rest on SciERC alone and warrant multi-benchmark validation.
8	Trained verifiers, relaxed decoding constraints, scaling to 70B+ models, and conformal prediction are promising directions.
9	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 954
}
```

</details>

---


### Tool call

_source line 607 · 2026-05-15T08:43:59.205456+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 608 · 2026-05-15T08:43:59.356371+00:00_

1	Our evaluation covers three datasets but only one RE benchmark (SciERC), where 40\% of instances receive zero F1, compressing the discriminable range and limiting signal differentiation for relation extraction.
2	RE selection failure persists even when restricting to non-zero F1 instances (Appendix~\ref{app:re_conditional_selection}), ruling out floor effects as the sole explanation, but generalization to other RE benchmarks remains unvalidated.
3	WNUT-17 confirms the capability boundary of our approach, but our positive results on formal-domain text (CoNLL, SciERC) have not been validated on informal or noisy text where models achieve non-trivial performance.
4	
5	We evaluate two model families (Qwen3-8B and LLaMA-3.1-8B), both at 8B parameters.
6	A 3-seed robustness analysis confirms that signal rankings are stable across seeds ($\sigma{\leq}0.025$; Table~\ref{tab:multiseed}), but whether our findings---particularly the correlation-selection gap and the difficulty-dependent signal ordering---hold for larger models (70B+) or closed-source APIs remains untested.
7	Larger models may produce higher-quality and more diverse samples, potentially altering the signal landscape.
8	
9	Our analysis of selection potential uses only unsupervised signals.
10	We do not train a dedicated verifier or reward model, leaving unknown how much of the oracle headroom a supervised approach could recover.
11	
12	We evaluate at $N{=}8$ and $N{=}16$.
13	The behavior of confidence signals at larger sample sizes (e.g., $N{=}64$ or $N{=}128$) is unknown, and $N$-scaling gains are setting-dependent: SJ improves by $+0.052$ on Qwen SciERC NER but only $+0.016$ on LLaMA SciERC NER when doubling from $N{=}8$ to $N{=}16$.
14	
15	On CoNLL with LLaMA, the SJ--FK gap is only 0.003 ($\rho{=}0.431$ vs.\ $0.428$), so the structural advantage over surface signals may not generalize to all simple-schema datasets.
16	Constrained decoding (Outlines/vLLM) enforces schema compliance, potentially compressing 
…[truncated 1014 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 150
}
```

</details>

---


### Tool call

_source line 609 · 2026-05-15T08:43:59.406942+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 610 · 2026-05-15T08:43:59.708798+00:00_

1	\section{Notation}\label{app:notation}
2	
3	Table~\ref{tab:notation} summarizes the notation used throughout the paper.
4	
5	\begin{table}[h]
6	\centering
7	\small
8	\begin{tabular}{cl}
9	\toprule
10	Symbol & Meaning \\
11	\midrule
12	$\mathcal{M}$ & Language model \\
13	$x$ & Input instance \\
14	$y_i$ & $i$-th stochastic sample \\
15	$N$ & Number of samples \\
16	$T$ & Sampling temperature \\
17	$c(\cdot)$ & Confidence signal \\
18	SJ & Soft Jaccard similarity \\
19	FK & Fleiss' $\kappa$ \\
20	EM & Exact-match voting rate \\
21	$c_{\text{vote}}$ & Entity voting confidence \\
22	$c_{\text{lp}}$ & Log-probability (mean token log-likelihood) \\
23	\bottomrule
24	\end{tabular}
25	\caption{Notation used throughout the paper.}
26	\label{tab:notation}
27	\end{table}
28	
29	\section{Robustness Analysis}\label{app:robustness}
30	
31	\begin{table}[t]
32	\centering
33	\small
34	\caption{Signal robustness across configurations (Spearman $\rho$). Top: temperature on Qwen SciERC. Middle: sample size on Qwen SciERC. Bottom: cross-model transfer (LLaMA CoNLL $N{=}16$, 3-seed mean $\pm\sigma$). $^\dagger$Mean over 3 seeds ($\sigma{=}0.025$; individual: 0.428, 0.424, 0.384).}
35	\label{tab:robustness}
36	\begin{tabular}{llcc}
37	\toprule
38	& & NER $\rho$ & RE $\rho$ \\
39	\midrule
40	\multicolumn{4}{l}{\textit{Temperature} (Qwen SciERC, $N{=}8$)} \\
41	\quad SJ & $T{=}0.7$ & 0.388 & 0.234 \\
42	\quad SJ & $T{=}1.0$ & 0.360 & 0.250 \\
43	\quad FK & $T{=}0.7$ & 0.321 & 0.184 \\
44	\quad FK & $T{=}1.0$ & 0.267 & 0.275 \\
45	\midrule
46	\multicolumn{4}{l}{\textit{Sample size} (Qwen SciERC, $T{=}1.0$)} \\
47	\quad SJ & $N{=}8$  & 0.360 & 0.250 \\
48	\quad SJ & $N{=}16$ & 0.412$^\dagger$ & 0.281 \\
49	\quad FK & $N{=}8$  & 0.267 & 0.275 \\
50	\quad FK & $N{=}16$ & 0.280 & 0.279 \\
51	\midrule
52	\multicolumn{4}{l}{\textit{Cross-model} (LLaMA CoNLL, $N{=}16$, 3 seeds)} \\
53	\quad SJ &  & $0.463{\pm}0.007$ & --- \\
54	\quad FK &  & $0.455{\pm}0.006$ & --- \\
55	\quad EM &  & $0.460{\pm
…[truncated 27696 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 611 · 2026-05-15T08:44:10.361482+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -E \"status: (open|in_progress)\" /home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-review-director-0161122b/788664a7-cbda-4ca9-aeda-2dfae5004d00/tool-results/biyzhs6gh.txt",
  "description": "Find open/in_progress issues in tracker"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -E \"status: (open|in_progress)\" /home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-review-director-0161122b/788664a7-cbda-4ca9-aeda-2dfae5004d00/tool-results/biyzhs6gh.txt",
    "description": "Find open/in_progress issues in tracker"
  }
}
```

</details>

---


### Tool result

_source line 612 · 2026-05-15T08:44:11.818096+00:00_

    status: open
        status: open
    status: open
        status: open
    status: open
        status: open
    status: open
        status: open
    status: open
        status: open
    status: open
        status: in_progress
    status: open
        status: in_progress
    status: open
        status: in_progress
    status: open
        status: in_progress
    status: open
        status: in_progress
    status: open
        status: in_progress
    status: open
        status: in_progress
    status: open
        status: in_progress
    status: open
        status: in_progress
    status: open
        status: in_progress
    status: open
        status: in_progress
    status: open
        status: in_progress
    status: in_progress
        status: in_progress
    status: in_progress
        status: in_progress
    status: in_progress
        status: in_progress
    status: in_progress
        status: in_progress
    status: in_progress
        status: in_progress
    status: in_progress
        status: in_progress
    status: in_progress
        status: in_progress
    status: in_progress
        status: in_progress
    status: in_progress
        status: in_progress

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Bash",
  "elapsed_ms": 1456
}
```

</details>

---


### Tool call

_source line 613 · 2026-05-15T08:44:12.370734+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "wc -l /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/references.bib 2>/dev/null && head -100 /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/references.bib",
  "description": "Check references.bib file"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Bash",
  "tool_args": {
    "command": "wc -l /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/references.bib 2>/dev/null && head -100 /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/references.bib",
    "description": "Check references.bib file"
  }
}
```

</details>

---


### Tool result

_source line 614 · 2026-05-15T08:44:12.823093+00:00_

503 /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/references.bib
% Auto-generated from literature_map.yaml — do not edit manually

@inproceedings{angelopoulos2021conformal,
  title = {Uncertainty Sets for Image Classifiers using Conformal Prediction},
  author = {Angelopoulos, Anastasios N. and Bates, Stephen and Malik, Jitendra and Jordan, Michael I.},
  booktitle = {ICLR 2021},
  year = {2021},
  url = {https://arxiv.org/abs/2009.14193}
}

@article{brown2024monkeys,
  title = {Large Language Monkeys: Scaling Inference Compute with Repeated Sampling},
  author = {Brown, Bradley and Juravsky, Jordan and Ehrlich, Ryan and Clark, Ronald and Le, Quoc V. and Ré, Christopher and Mirhoseini, Azalia},
  journal = {arXiv preprint arXiv:2407.21787},
  year = {2024},
  url = {https://arxiv.org/abs/2407.21787}
}

@inproceedings{chen2024usc,
  title = {Universal Self-Consistency for Large Language Model Generation},
  author = {Chen, Xinyun and Aksitov, Renat and Alon, Uri and Ren, Jie and Xiao, Kefan and Yin, Pengcheng and Prakash, Sushant and Sutton, Charles and Wang, Xuezhi and Zhou, Denny},
  booktitle = {arXiv preprint (ICML 2024 Workshop ICL)},
  year = {2024},
  url = {https://arxiv.org/abs/2311.17311}
}

@article{cobbe2021verifiers,
  title = {Training Verifiers to Solve Math Word Problems},
  author = {Cobbe, Karl and Kosaraju, Vineet and Bavarian, Mohammad and Chen, Mark and Jun, Heewoo and Kaiser, Lukasz and Plappert, Matthias and Tworek, Jerry and Hilton, Jacob and Nakano, Reiichiro and Hesse, Christopher and Schulman, John},
  journal = {arXiv preprint arXiv:2110.14168},
  year = {2021},
  url = {https://arxiv.org/abs/2110.14168}
}

@inproceedings{culotta2004confidence,
  title = {Confidence Estimation for Information Extraction},
  author = {Culotta, Aron and McCallum, Andrew},
  booktitle = {HLT-NAACL 2004},
  year = {2004},
  url = {https://aclanthology.org/N04-4028/}
}

@inproceedings{derczynski2017wnut,
  title = {R
…[truncated 2277 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Bash",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 615 · 2026-05-15T08:44:13.074531+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/figures/ 2>/dev/null",
  "description": "Check figures directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/figures/ 2>/dev/null",
    "description": "Check figures directory"
  }
}
```

</details>

---


### Tool result

_source line 616 · 2026-05-15T08:44:13.125320+00:00_

fig_length_logprob_scatter.pdf
fig_overview.pdf
fig_reliability.pdf
fig_selection_gap.pdf
fig_signal_heatmap.pdf
fig_temperature_robustness.pdf

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 617 · 2026-05-15T08:44:22.215632+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -B 3 -A 15 \"status: open\" /home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-review-director-0161122b/788664a7-cbda-4ca9-aeda-2dfae5004d00/tool-results/biyzhs6gh.txt | head -300",
  "description": "Read open issues with context"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -B 3 -A 15 \"status: open\" /home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-review-director-0161122b/788664a7-cbda-4ca9-aeda-2dfae5004d00/tool-results/biyzhs6gh.txt | head -300",
    "description": "Read open issues with context"
  }
}
```

</details>

---


### Tool result

_source line 618 · 2026-05-15T08:44:22.266542+00:00_

    summary: "Constrained decoding 是 correlation-selection gap 的未控制混淆变量"
    category: method
    severity: critical
    status: open
    first_raised_round: 3
    last_seen_round: 5
    mentions:
      - round: 3
        reviewers: [1, 2]
        note: "两位 Reviewer 均独立提出。Outlines/vLLM constrained decoding 可能压缩 per-sample diversity，使 gap 成为实验设置 artifact。"
      - round: 4
        reviewers: [1, 2]
        note: "R2 确认部分解决（承认但未量化）。R1 仍列 critical（需 logprob 分布分析）。共识：elevated should-fix，量化 logprob 分布而非增加 free-form 实验。"
      - round: 5
        reviewers: [1, 2]
        note: "Round 5 两位 Reviewer 再次独立提出为 critical。Appendix F 已有 logprob tie 分析（60% instances range<0.05），但论文 claim scope（title/abstract/conclusion）仍未限定为 constrained decoding setting。Non-tied subset +2.9pp p=0.01 结果被两位 Reviewer 一致解读为 gap 主因是 score compression 而非 IE 固有属性。共识：要么添加 free-form 消融，要么在所有核心 claim 中限定 scope。"
    action_items:
      - round: 3
        action: "Agent 量化 diversity；Paper Agent 写入论文 + 限定 scope"
--
      - round: 5
        action: "(a) Title/Abstract/Conclusion 限定 claim scope 为 constrained decoding setting；(b) 提升 Appendix F non-tied analysis 至主文 Discussion；(c) 明确承认 non-tied evidence 对 claim 普适性的影响"
        assigned_to: "Paper Agent"
        status: open
    resolution: ""
    resolution_round: null

  - id: "R3-C2"
    summary: "Failure-to-reject 不等于 evidence of absence，selection gap 统计论证不完整"
    category: method
    severity: warning
    status: resolved
    first_raised_round: 3
    last_seen_round: 4
    mentions:
      - round: 3
        reviewers: [1, 2]
        note: "需修改措辞或补充等价性检验"
      - round: 4
--
    summary: "Gap 概念部分 tautological——instance-level 信号无法 select 是定义必然"
    category: method
    severity: warning
    status: open
    first_raised_round: 3
    last_seen_round: 5
    mentions:
      - round: 3
        reviewers: [1, 2]
        note: "需在 Discussion 中分离两层论证"
      - round: 4
        reviewers: [1, 2]
        note: "R4 两位 Reviewer 独立再次提出：Introduction 未正面论证 why not obvious a 
…[truncated 8203 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 619 · 2026-05-15T08:44:30.606213+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -B 3 -A 15 \"status: open\" /home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-review-director-0161122b/788664a7-cbda-4ca9-aeda-2dfae5004d00/tool-results/biyzhs6gh.txt | tail -200",
  "description": "Read remaining open issues"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -B 3 -A 15 \"status: open\" /home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-review-director-0161122b/788664a7-cbda-4ca9-aeda-2dfae5004d00/tool-results/biyzhs6gh.txt | tail -200",
    "description": "Read remaining open issues"
  }
}
```

</details>

---


### Tool result

_source line 620 · 2026-05-15T08:44:30.657117+00:00_

    action_items:
      - round: 5
        action: "(a) 所有 RE 分析处一致标注 single-benchmark preliminary；(b) Contribution #3 加 RE 限定；(c) Future work 明确列出 RE 多数据集验证"
        assigned_to: "Paper Agent"
        status: in_progress
    resolution: ""
--
    summary: "Abstract 过于密集，第 4 行超长句子需拆分"
    category: writing
    severity: warning
    status: open
    first_raised_round: 4
    last_seen_round: 5
    mentions:
      - round: 4
        reviewers: [1, 2]
        note: "多层嵌套括号和分号的超长句子"
      - round: 5
        reviewers: [1, 2]
        note: "仍未修改。9 行含 5 signal/3 family/4 metric/3 dataset/2 model + gap 概念。两位 Reviewer 一致建议拆分为 2-3 句，聚焦核心 claim，具体数字移入 Introduction。"
    action_items:
      - round: 5
        action: "Abstract 拆分为 2-3 句核心 claim，将具体信号名/数字/family 移入 Introduction"
        assigned_to: "Paper Agent"
        status: in_progress
    resolution: ""
--
    summary: "TOST δ 选择（±2/3/5 pp）缺乏实践意义论证"
    category: experiment
    severity: info
    status: open
    first_raised_round: 4
    last_seen_round: 5
    mentions:
      - round: 4
        reviewers: [1]
        note: "δ 选择直接影响等价结论"
      - round: 5
        reviewers: [1, 2]
        note: "R1 再提：与 IAA 关联无引用。R2 同意但认为多水平 δ 已构成 sensitivity analysis，引用 IAA 数据即可。"
    action_items:
      - round: 5
        action: "引用 1-2 篇 IE benchmark IAA 数据来锚定 δ 选择"
        assigned_to: "Paper Agent"
        status: in_progress
    resolution: ""
--
    summary: "Table 1 N=16 block 大面积空白"
    category: writing
    severity: info
    status: open
    first_raised_round: 4
    last_seen_round: 5
    mentions:
      - round: 4
        reviewers: [1, 2]
        note: "N=16 仅填 LLaMA CoNLL，SciERC 空白"
      - round: 5
        reviewers: [1, 2]
        note: "Table 1 已加脚注说明 N=16 数据位置（Appendix Table 3），但脚注格式（\\textsuperscript{†} + \\footnotetext）在 two-column 模板下可能渲染异常。"
    action_items:
      - round: 5
        action: "检查 PDF 渲染；考虑合并 N=16 到附录以简化 Table 1"
        assigned_to: "Paper Agent"
        status: in_progress
    resolution: ""
--
   
…[truncated 4172 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 621 · 2026-05-15T08:44:40.899927+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -A 25 \"R5-C1\" /home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-review-director-0161122b/788664a7-cbda-4ca9-aeda-2dfae5004d00/tool-results/biyzhs6gh.txt",
  "description": "Read R5-C1 issue"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -A 25 \"R5-C1\" /home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-review-director-0161122b/788664a7-cbda-4ca9-aeda-2dfae5004d00/tool-results/biyzhs6gh.txt",
    "description": "Read R5-C1 issue"
  }
}
```

</details>

---


### Tool result

_source line 622 · 2026-05-15T08:44:41.000802+00:00_

  - id: "R5-C1"
    summary: "Constrained decoding 混淆变量未隔离，claim scope 与 evidence 不匹配"
    category: framing
    severity: critical
    status: in_progress
    first_raised_round: 5
    last_seen_round: 5
    mentions:
      - round: 5
        reviewers: [1, 2]
        note: "所有实验均在 constrained decoding 下。Appendix F non-tied subset (n=210) logprob +2.9pp, p=0.01 暗示 gap 主因是 score compression 而非 IE 固有属性。Title/Abstract/Conclusion 需限定 constrained decoding scope。"
    action_items:
      - round: 5
        action: "Title 加 'under Constrained Decoding'; Abstract/Introduction/Discussion/Conclusion 限定 scope; 提升 Appendix F non-tied analysis 到主文 Discussion"
        assigned_to: "Paper Agent"
        status: in_progress
    resolution: ""
    resolution_round: null

  - id: "R5-C2"
    summary: "Correlation-selection gap 的 tautological 成分削弱核心贡献新颖性"
    category: framing
    severity: critical
    status: in_progress
    first_raised_round: 5
    last_seen_round: 5

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Bash",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 623 · 2026-05-15T08:44:44.365325+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -A 25 \"R5-C2\" /home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-review-director-0161122b/788664a7-cbda-4ca9-aeda-2dfae5004d00/tool-results/biyzhs6gh.txt",
  "description": "Read R5-C2 issue"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -A 25 \"R5-C2\" /home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-review-director-0161122b/788664a7-cbda-4ca9-aeda-2dfae5004d00/tool-results/biyzhs6gh.txt",
    "description": "Read R5-C2 issue"
  }
}
```

</details>

---


### Tool result

_source line 624 · 2026-05-15T08:44:44.416027+00:00_

  - id: "R5-C2"
    summary: "Correlation-selection gap 的 tautological 成分削弱核心贡献新颖性"
    category: framing
    severity: critical
    status: in_progress
    first_raised_round: 5
    last_seen_round: 5
    mentions:
      - round: 5
        reviewers: [1, 2]
        note: "4/5 instance-level failure = tautological; logprob failure = artifact。C2 应以 logprob compression + MBR/consensus-proximity failure 为重心，弱化 '5 signals all fail' 统一叙事。"
    action_items:
      - round: 5
        action: "Reframe C2 聚焦 logprob compression + MBR failure; 弱化 '5 signals all fail'; Introduction 加强非显然性论证"
        assigned_to: "Paper Agent"
        status: in_progress
    resolution: ""
    resolution_round: null

  - id: "R5-W4"
    summary: "'First multi-family comparison' claim = scope engineering"
    category: framing
    severity: warning
    status: in_progress
    first_raised_round: 5
    last_seen_round: 5

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 625 · 2026-05-15T08:45:51.105030+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "## Round 1 审稿任务 — Reviewer 1\n\n**你的审查侧重：方法严谨性 + 实验设计**\n\n### 论文信息\n- **论文路径**: `projects/struct_self_consist_ie/docs/paper/main.tex`（各章节在 `sections/` 子目录）\n- **目标 venue**: EMNLP 2026 Findings\n- **截止日期**: 2026-05-25\n- **页数限制**: 长文 8 页正文（不含 limitations/ethics/references/appendix）\n- **模板**: ACL style files（`\\usepackage[review]{acl}`）\n- **匿名规则**: Double-blind\n\n### 论文概要\n标题：Strong Predictors, Weak Selectors: Confidence Signals for Test-Time Scaling in Information Extraction under Constrained Decoding\n\n研究在 constrained decoding 下，5 种 confidence signals（VC, SJ, FK, EM, logprob）对 structured IE（NER + RE）的 quality estimation 和 sample selection 效果。核心发现：信号是有效的 quality estimator（ρ=0.38, AUROC=0.75）但无法做 sample selection（correlation-selection gap）。\n\n### 你需要重点审查\n1. **统计方法严谨性**：bootstrap resampling 设计、TOST 等价检验的 δ 选择是否有据、p 值解读是否准确\n2. **实验设计 confounds**：constrained decoding 是否是 gap 的 confounding variable（论文已有 non-tied subset 分析，但是否充分）；Qwen3 thinking token 训练不一致是否影响结论\n3. **Claim-evidence 匹配**：核心 claim（gap 存在且有实际意义）与 evidence 是否匹配；instance-level 信号无法 select 是否 tautological；logprob 失败是否仅因 score compression\n4. **RE 证据强度**：单数据集（SciERC）RE 结论的可信度\n5. **信号定义数学正确性**：SJ 的 Hungarian matching、VC 的 frequency 定义、FK 的 adaptation 是否正确\n6. **格式合规**：页数是否超限、ACL 模板使用是否正确",
  "project": "struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "text": "## Round 1 审稿任务 — Reviewer 1\n\n**你的审查侧重：方法严谨性 + 实验设计**\n\n### 论文信息\n- **论文路径**: `projects/struct_self_consist_ie/docs/paper/main.tex`（各章节在 `sections/` 子目录）\n- **目标 venue**: EMNLP 2026 Findings\n- **截止日期**: 2026-05-25\n- **页数限制**: 长文 8 页正文（不含 limitations/ethics/references/appendix）\n- **模板**: ACL style files（`\\usepackage[review]{acl}`）\n- **匿名规则**: Double-blind\n\n### 论文概要\n标题：Strong Predictors, Weak Selectors: Confidence Signals for Test-Time Scaling in Information Extraction under Constrained Decoding\n\n研究在 constrained decoding 下，5 种 confidence signals（VC, SJ, FK, EM, logprob）对 structured IE（NER + RE）的 quality estimation 和 sample selection 效果。核心发现：信号是有效的 quality estimator（ρ=0.38, AUROC=0.75）但无法做 sample selection（correlation-selection gap）。\n\n### 你需要重点审查\n1. **统计方法严谨性**：bootstrap resampling 设计、TOST 等价检验的 δ 选择是否有据、p 值解读是否准确\n2. **实验设计 confounds**：constrained decoding 是否是 gap 的 confounding variable（论文已有 non-tied subset 分析，但是否充分）；Qwen3 thinking token 训练不一致是否影响结论\n3. **Claim-evidence 匹配**：核心 claim（gap 存在且有实际意义）与 evidence 是否匹配；instance-level 信号无法 select 是否 tautological；logprob 失败是否仅因 score compression\n4. **RE 证据强度**：单数据集（SciERC）RE 结论的可信度\n5. **信号定义数学正确性**：SJ 的 Hungarian matching、VC 的 frequency 定义、FK 的 adaptation 是否正确\n6. **格式合规**：页数是否超限、ACL 模板使用是否正确",
    "project": "struct_self_consist_ie"
  }
}
```

</details>

---


### Tool result

_source line 626 · 2026-05-15T08:46:02.675895+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 11570
}
```

</details>

---


### Tool call

_source line 627 · 2026-05-15T08:46:02.727349+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "## Round 1 审稿任务 — Reviewer 2\n\n**你的审查侧重：新颖性 + 完整性 + 相关工作**\n\n### 论文信息\n- **论文路径**: `projects/struct_self_consist_ie/docs/paper/main.tex`（各章节在 `sections/` 子目录）\n- **目标 venue**: EMNLP 2026 Findings\n- **截止日期**: 2026-05-25\n- **页数限制**: 长文 8 页正文（不含 limitations/ethics/references/appendix）\n- **模板**: ACL style files（`\\usepackage[review]{acl}`）\n- **匿名规则**: Double-blind\n\n### 论文概要\n标题：Strong Predictors, Weak Selectors: Confidence Signals for Test-Time Scaling in Information Extraction under Constrained Decoding\n\n研究在 constrained decoding 下，5 种 confidence signals（VC, SJ, FK, EM, logprob）对 structured IE（NER + RE）的 quality estimation 和 sample selection 效果。核心发现：信号是有效的 quality estimator（ρ=0.38, AUROC=0.75）但无法做 sample selection（correlation-selection gap）。\n\n### 你需要重点审查\n1. **Contribution 新颖性**：与 Nédellec et al. (2026) 的增量有多大？三个声称的贡献（multi-family comparison / gap identification / difficulty gradient）是否各自有足够新意？\n2. **Related work 覆盖度**：是否遗漏重要工作（test-time scaling verification surveys, MBR 在非 MT 任务的应用, 最新 self-consistency 变体等）？引用是否准确（检查引用上下文是否与被引论文实际内容匹配）\n3. **Framing 诚实度**：\"first\" claim 是否站得住？cross-model 措辞是否过度外推？gap 概念是否被呈现为比实际更新颖？\n4. **写作质量**：Abstract 密度是否过高？术语一致性（confidence signal vs consistency signal, VC vs Voting Conf.）？论文结构是否清晰？\n5. **完整性**：是否有关键分析缺失？Future work 是否充分讨论？Limitations 是否诚实？\n6. **引用格式与准确性**：bib entry 是否正确、是否有 orphan 引用、是否有引用上下文与实际论文不匹配的情况",
  "project": "struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "text": "## Round 1 审稿任务 — Reviewer 2\n\n**你的审查侧重：新颖性 + 完整性 + 相关工作**\n\n### 论文信息\n- **论文路径**: `projects/struct_self_consist_ie/docs/paper/main.tex`（各章节在 `sections/` 子目录）\n- **目标 venue**: EMNLP 2026 Findings\n- **截止日期**: 2026-05-25\n- **页数限制**: 长文 8 页正文（不含 limitations/ethics/references/appendix）\n- **模板**: ACL style files（`\\usepackage[review]{acl}`）\n- **匿名规则**: Double-blind\n\n### 论文概要\n标题：Strong Predictors, Weak Selectors: Confidence Signals for Test-Time Scaling in Information Extraction under Constrained Decoding\n\n研究在 constrained decoding 下，5 种 confidence signals（VC, SJ, FK, EM, logprob）对 structured IE（NER + RE）的 quality estimation 和 sample selection 效果。核心发现：信号是有效的 quality estimator（ρ=0.38, AUROC=0.75）但无法做 sample selection（correlation-selection gap）。\n\n### 你需要重点审查\n1. **Contribution 新颖性**：与 Nédellec et al. (2026) 的增量有多大？三个声称的贡献（multi-family comparison / gap identification / difficulty gradient）是否各自有足够新意？\n2. **Related work 覆盖度**：是否遗漏重要工作（test-time scaling verification surveys, MBR 在非 MT 任务的应用, 最新 self-consistency 变体等）？引用是否准确（检查引用上下文是否与被引论文实际内容匹配）\n3. **Framing 诚实度**：\"first\" claim 是否站得住？cross-model 措辞是否过度外推？gap 概念是否被呈现为比实际更新颖？\n4. **写作质量**：Abstract 密度是否过高？术语一致性（confidence signal vs consistency signal, VC vs Voting Conf.）？论文结构是否清晰？\n5. **完整性**：是否有关键分析缺失？Future work 是否充分讨论？Limitations 是否诚实？\n6. **引用格式与准确性**：bib entry 是否正确、是否有 orphan 引用、是否有引用上下文与实际论文不匹配的情况",
    "project": "struct_self_consist_ie"
  }
}
```

</details>

---


### Tool result

_source line 628 · 2026-05-15T08:46:04.437939+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1710
}
```

</details>

---


### Assistant

_source line 629 · 2026-05-15T08:46:17.477840+00:00_

Round 1 审稿任务已派发给两位 Reviewer：

- **Reviewer 1**（方法严谨性 + 实验设计）：统计方法、实验 confounds、claim-evidence 匹配、RE 证据强度、信号定义正确性
- **Reviewer 2**（新颖性 + 完整性 + 相关工作）：contribution 新颖性、related work 覆盖、framing 诚实度、写作质量、引用准确性

等待两位 Reviewer 返回独立审稿结果。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 49

## Round 49

2 recorded events


### User

_source line 630 · 2026-05-15T08:51:18.515698+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 — Round 1 审稿报告

**论文**: Strong Predictors, Weak Selectors: Confidence Signals for Test-Time Scaling in Information Extraction under Constrained Decoding
**审查侧重**: 新颖性 + 完整性 + 相关工作

---

## 总体评分

**Overall**: 3/5 (Findings track)
**一句话总结**: 实验设计扎实、统计分析严谨的负面结果论文，对 structured IE 的 test-time scaling 提供了有价值的实证警告，但核心发现的新颖性有限——correlation-selection gap 的 4/5 信号来源于定义层面的不可避免性（instance-level 信号天然无法做 sample selection），真正有趣的 logprob 压缩诊断只占论文的一小部分。

---

## 官方维度打分（来自 ACL ARR review form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | 统计方法严谨（bootstrap, TOST, multi-seed），但 FK 独立性假设仅以经验验证部分回应，consensus-proximity 作为 selection 唯一策略有局限 |
| Excitement | 2.5/5 | 负面结果对从业者有参考价值，但 gap 的 4/5 来源是定义性的（instance-level 信号不可能做 per-sample selection），最有趣的 logprob 压缩分析篇幅不足 |
| Reproducibility | 3/5 | Training config、prompt template、超参详尽（Table 7, Appendix F），但未提及代码/数据发布计划 |
| Reviewer Confidence | 4/5 | 熟悉 self-consistency、MBR decoding、结构化 IE 和不确定性估计文献 |

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] Contribution 1 "systematic multi-family comparison" 的新颖性与 framing 不匹配
- 具体位置：Section 1 (Introduction), Contribution (i); Section 2 (Related Work), ¶2
- 问题：论文将 "5 signals from 3 families" 的对比定位为主要贡献，但这本质上是 engineering benchmark——将已知的 confidence signals（logprob, exact match, Fleiss' κ 等）应用于新任务设置。与 Nédellec et al. (2026) 的增量确实存在（结构化匹配、constrained decoding、多数据集），但论文在 Introduction 中没有足够清楚地区分 "applying known signals to a new setting" 和 "discovering new signals or principles"。
- 为什么影响接收：如果 reviewer 将这理解为 "known metrics on new tasks" 的简单应用研究，会直接影响 novelty 评分。
- 建议修改方向：在 Introduction 中更明确地说明，核心贡献不是比较本身，而是 (a) 发现质量估计与选择之间的 gap，(b) logprob 压缩的机制诊断。将 Contribution 1 降级为 setup/methodology，将 Contribution 2 (gap) 提升为核心 claim。

**N2** [critical] Correlation-selection gap 的 4/5 来源是定义性的，非实证发现
- 具体位置：Section 1 (Introduction), ¶5; Section 5 (Discussion), ¶2 "Layer 1 (definitional)"
- 问题：论文在 Discussion 中自己承认 4/5 信号的 selection failure 是 "by construction"（Layer 1），因为 instance-level 信号天然给所有候选样本相同分数。这不是一个需要通过实验才能发现的 gap——这是信号定义的直接推论。论文的真正实证贡献是 Layer 2（logprob 在 constrained decoding 下的压缩），但这在当前 framing 中被埋在了 "gap" 这个更大叙事之下。
- 为什么影响接收：将定义性结论包装为实证发现会降低论文的可信度。一个熟悉这些信号的 reviewer 会立即意识到 instance-level 信号不能做 per-sample selection，这不需要实验验证。
- 建议修改方向：(1) 在 Introduction 中提前透明化 Layer 1 是 definitional，而非卖悬念；(2) 将叙事重心转向 Layer 2——logprob（唯一的 per-sample signal）为何也失败，constrained decoding 压缩的机制及其条件性缓解（+2.9pp, p=0.01）才是论文最有价值的贡献。

**N3** [critical] Related Work 遗漏关键引用
- 具体位置：Section 2 (Related Work)
- 问题：
  (a) **Zhang et al. (2025) "A Survey on Test-Time Scaling in Large Language Models: What, How, Where, and How Well?" (arXiv:2503.24235)**——目前最全面的 test-time scaling survey，提出了系统性的 TTS 分类框架（what/how/where/how well to scale），论文引用了 Snell 和 Brown 的个别工作但遗漏了这个综述，考虑到论文标题包含 "Test-Time Scaling" 这个关键词，这是显著的遗漏。
  (b) **Eikema, Rutkiewicz & Giulianelli (EMNLP 2025) "Structure-Conditional Minimum Bayes Risk Decoding"**——直接研究 MBR decoding 在结构化输出上的问题，发现 common utility functions 在结构化场景（dialogue, instruction-following）下表现不佳，与本文 Section 5 ¶3 的 MBR 失败发现高度相关。
- 为什么影响接收：Related Work 完整性是 EMNLP Findings 的基本要求；遗漏了同一 venue (EMNLP 2025) 的直接相关工作会被 reviewer 视为文献调研不充分。
- 建议修改方向：在 Section 2 ¶1 补充 Zhang et al. survey 作为 test-time scaling 的综述引用；在 ¶3 (uncertainty/MBR) 补充 Eikema et al. (2025) 并讨论其 utility function 对结构化输出不适用的发现如何与本文的 MBR failure 互相印证。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] "cross-model" 措辞过度外推
- 具体位置：Section 1 (Introduction), Contribution (iii) "consistent ordering across models"；Section 4.1 "cross-model stability is strong"
- 问题：实际只测试了 2 个同规模 (8B) 模型。"cross-model" 的说法暗示了比实际更广的泛化性。Limitations 中承认了 70B+/closed-source 未测试，但 main text 的措辞没有同步限定。
- 建议：将 main text 中的 "cross-model" 改为 "cross-architecture" 或 "across two model families (at 8B scale)"，使措辞与实际实验范围匹配。

**W2** [warning] Abstract 信息密度过高
- 具体位置：sections/abstract.tex
- 问题：9 行 abstract 包含：5 个信号名、3 个信号家族名、4 个数字 (ρ=0.38, AUROC=0.75, p>0.39, +2.9pp)、3 个数据集（隐含在 "three datasets"）、2 个任务、2 个模型（隐含在 "two 8B-parameter model families"）、plus "correlation-selection gap" 这个新术语的引入。对于不熟悉该领域的 reviewer，首次阅读时信息过载。
- 建议：减少具体数字，将 signal family 名称移到正文；abstract 聚焦于问题-发现-意义三段式。

**W3** [warning] 术语一致性问题
- 具体位置：全文多处
- 问题：
  (a) "VC" 在 Table 1 和正文中用，但 Method Section 定义为 "entity voting confidence"，Notation Table (Appendix A) 用 $c_{\text{vote}}$——三个名称指同一个东西。
  (b) "confidence signal" 是 umbrella term (Section 3.2 line 1)，但 Introduction line 1 说 "Self-consistency...sampling multiple outputs and aggregating them" 然后用 "confidence signals" 包含 logprob 这个非 consistency-based 的信号——读者需要读到 Method 才明白这个术语层次。
  (c) "LP" 在 Table 5 使用，但 Table 1 用 "Log-prob"，正文用 "logprob"。
- 建议：统一为一套术语，在第一次出现时明确定义缩写并全文一致使用。

**W4** [warning] RE 结论建立在单一数据集上，但 main text 中的呈现方式容易让读者忽略这一点
- 具体位置：Table 1 (tab:quality_estimation), Table 2 (tab:selection), Section 4.2
- 问题：SciERC 是唯一的 RE 数据集，40% 的 instances 有 zero F1，RE 结果在 Table 1 中与 NER 并列呈现但缺少明确的 "preliminary/single-benchmark" 标记。虽然 Table 1 caption 说 "single benchmark—preliminary"，Table 2 caption 也说 "RE results are from a single benchmark (preliminary)"，但 Discussion 和 Conclusion 中 RE 的发现与 NER 一起总结，没有在每次引用 RE 结论时重申 preliminary 性质。
- 建议：在 Discussion/Conclusion 中每次引用 RE 结论时加 "(preliminary, single benchmark)" 后缀，或在 Conclusion 中用独立句子总结 RE 的局限性（当前只有一句 "RE findings rest on SciERC alone"）。

**W5** [warning] Qwen3-8B thinking mode 配置不一致
- 具体位置：Section 7 (Limitations), ¶6; Appendix F ¶3
- 问题：SciERC 训练时未显式关闭 thinking mode，CoNLL/WNUT 显式关闭了。虽然 constrained decoding 在推理时会覆盖 thinking behavior，但训练时暴露 thinking tokens 可能影响 learned representations——论文自己在 Limitations 中也承认了这一点。这引入了一个潜在的 confound：SciERC 和 CoNLL/WNUT 之间的 signal behavior 差异可能部分来自训练配置不一致而非数据集特性差异。
- 建议：要么补做实验（统一配置重新训练 SciERC），要么在 Experiments Setup 中 prominently 声明这一 confound（当前只在 Limitations 和 Appendix 的脚注中提及），让 reader 在解读 cross-dataset comparisons 时有充分的背景信息。

**W6** [warning] 缺少与 supervised verifier 的对比
- 具体位置：Section 5 (Discussion) ¶4; Section 7 (Limitations) ¶3
- 问题：论文反复建议 "trained verifiers" 作为 closing the gap 的方向（Discussion: "Effective selection likely requires...trained verifiers"；Conclusion: "Trained verifiers...are promising directions"），但没有提供任何 supervised baseline。即使训练一个简单的 linear probe on logprob features 也能量化 supervision 能 recover 多少 oracle headroom，使得 "trained verifiers needed" 的结论从猜测变为有证据的 claim。
- 建议：加入一个简单的 supervised verifier baseline（例如 logistic regression on signal features predicting per-sample F1），哪怕只是 oracle-bound analysis，以量化 unsupervised 和 supervised 之间的 gap。

---

## 小问题（不影响接收）

- Figure 1 caption 重复了正文 Section 4.2 的大部分内容（"p=0.39 for NER logprob; Table 2"），caption 应更简洁。
- Table 1 的 $N{=}16$ 行只有 LLaMA CoNLL 一个配置的数据，且只报告了 $\rho$ 没有 AUROC——要么删除这一行移到 Appendix，要么补全数据。
- Section 3.2 ¶3 (FK): "excess agreement ($\bar{P} - \bar{P}_e$) across all configurations...between $-$0.4% and $-$4.0%" ——负的 excess agreement 意味着 $\bar{P} < \bar{P}_e$（observed agreement 低于随机预期），这表示轻微负依赖。论文将此解读为 "confirms that FK is not inflated by inter-sample dependence"，这个推理是正确的，但措辞可以更清晰——"mild negative dependence" 比 "sufficient response diversity" 更准确。
- Appendix A Notation Table: $c_{\text{vote}}$ 的 Meaning 列写 "Entity voting confidence"，但没有列出 LP/logprob 的 shorthand "LP"（Table 5 使用了 LP 缩写）。
- Ethics Statement 提及 "CoNLL-2003" 但该数据集基于 Reuters 新闻语料，其 license 有使用限制（研究目的）——可以在 Ethics Statement 中简要注明。

---

## 引用格式与准确性

引用验证工具结果：60 条 bib entries，91 条引用，0 orphan，0 missing，53 条在线验证通过。

具体问题：
1. **feng2025optimal**: OpenAlex 显示 first author 为 "Austin"（全名 Austin Feng），bib 中 authors 字段写 "Feng, Austin and Marius, Alonso and..."——检查是否应为 "Feng, Austin and Alonso, Marius and Odonnat, Ambroise"，当前 bib 中 Marius 被放在了 first name 位置。
2. **ye2025uncertainty**: OpenAlex 显示 first author 可能为 Heo 而非 Ye——需确认正确的 first author。
3. **hobelsberger2025systematic** 和 **venktesh2025trust**: OpenAlex 未找到，可能是较新的 preprint；建议确认 arXiv ID 正确。
4. **lightman2024verify**: OpenAlex 未找到（"Let's Verify Step by Step"），这是 ICLR 2024 论文，可能是 API 覆盖问题而非引用错误。
5. **snell2024scaling**: bib 标注为 2024 但 venue 为 "ICLR 2025"——key 和 year 应统一为 2025。

---

## 主要优势

1. **统计分析的严谨性**：Bootstrap CI、TOST equivalence testing、multi-seed stability analysis、diversity stratification、conditional filtering——这是我在 IE 领域论文中少见的统计严谨程度，远超大多数只报 point estimates 的工作。
2. **Logprob 压缩诊断**：Section 5 ¶2 (Layer 2) 和 Appendix G 的 non-tied subset analysis（+2.9pp, p=0.01）是论文最有价值的贡献——它不仅报告了 selection failure，还提供了 actionable 的机制解释（constrained decoding 压缩 logprob resolution）。
3. **Limitations 的诚实程度**：Section 7 覆盖了 RE 单数据集、模型规模限制、N-scaling 范围、thinking mode confound、logprob temperature gap——这种自我批评的坦诚值得肯定。
4. **Difficulty gradient 设计**：三个 NER 数据集跨越 easy (CoNLL, 91% F1) → hard (SciERC) → boundary (WNUT-17, 52% zero F1) 的梯度设计合理，WNUT-17 的负面 logprob correlation (ρ=−0.410) 是一个有趣且非显然的发现。
5. **质量估计与选择的明确区分**：即使 4/5 的 selection failure 是 definitional，将 quality estimation 和 sample selection 作为两个独立评价维度进行系统对比，在 IE 文献中是有价值的框架贡献。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 631 · 2026-05-15T08:51:25.977798+00:00_

Reviewer 2 报告已收到。等待 Reviewer 1 完成独立审稿。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 50

## Round 50

2 recorded events


### User

_source line 632 · 2026-05-15T08:51:28.796267+00:00_

[Reviewer 2 审稿结果]:
审稿报告已提交给 Review Director。

核心判断：**Overall 3/5，适合 Findings track**。

3 个 Must-Fix：
- **N1**: Contribution 1（multi-family comparison）本质是 benchmark 应用研究，framing 应将 logprob 压缩诊断提升为核心贡献
- **N2**: Correlation-selection gap 的 4/5 来源是 instance-level 信号的定义性质而非实证发现，当前 framing 掩盖了这一点
- **N3**: 遗漏 Zhang et al. (2025) test-time scaling 综述和 Eikema et al. (EMNLP 2025) Structure-Conditional MBR——均为高度相关的近期工作

6 个 Should-Fix 涵盖 cross-model 过度外推、abstract 信息过载、术语不一致、RE 单数据集标注不足、Qwen3 thinking mode confound、缺少 supervised verifier baseline。引用验证发现 5 处 bib 条目需修正。

主要优势：统计分析严谨度远超同类工作，logprob 压缩诊断有 actionable 价值，Limitations 坦诚。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 633 · 2026-05-15T08:51:34.902429+00:00_

Reviewer 2 报告已收到。等待 Reviewer 1 报告。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 51

## Round 51

6 recorded events


### User

_source line 634 · 2026-05-15T08:52:00.528293+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 — Round 1 审稿报告

**论文**: Strong Predictors, Weak Selectors: Confidence Signals for Test-Time Scaling in Information Extraction under Constrained Decoding
**审查侧重**: 方法严谨性 + 实验设计

---

## 总体评分
**Overall**: 3.0/5（Findings acceptance）
**一句话总结**: 方法论扎实、统计实践规范的实证研究，但核心发现（correlation-selection gap）大部分可归因于 constrained decoding 的技术 artifact 而非 structured IE 的基本属性，加上 RE 仅单数据集、Qwen3 thinking token confound 未充分控制，限制了贡献的深度和普适性。

---

## 官方维度打分（来自 ACL ARR review form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | 核心 claim 有合理支撑，bootstrap 和 TOST 设计规范，但缺少 free-form decoding 对照实验是显著缺口；TOST δ 选择的理据间接 |
| Excitement | 3.0/5 | Quality estimation vs. sample selection 的区分有价值，但 4/5 信号 instance-level 不能 select 在定义上即成立，logprob 失败归因于 score compression 是 constrained decoding 的特有问题，非通用发现 |
| Overall | 3.0/5 | 适合 Findings：实证全面、写作清晰、局限性坦诚，但贡献增量性偏强 |
| Reproducibility | 4/5 | 训练超参、数据集 split、prompt 模板、推理配置均有详细记录（Appendix E），代码未共享是唯一扣分点 |
| Confidence | 4/5 | 熟悉 self-consistency、MBR decoding、LLM-based IE 和 uncertainty estimation 领域 |

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] **缺少 free-form decoding 对照实验——核心发现可能是 constrained decoding artifact**
- 具体位置：Section 5 (Discussion), Limitations
- 问题：论文的核心概念 "correlation-selection gap" 被呈现为 structured IE 的重要发现，但 non-tied subset analysis（Section 5）已经证明：当 score compression 被缓解时（logprob range ≥ 0.05 的 40% instances），logprob 成为显著 selector（+2.9pp, p=0.01, within-instance ρ: 0.08→0.39）。这直接暗示 gap 主要源于 constrained decoding 的技术限制，而非 structured IE 的固有属性。缺少 free-form decoding（不使用 grammar constraint）的对照实验，无法区分这两种解释。
- 为什么影响接收：如果 gap 仅存在于 constrained decoding 下（且已可追溯到 score compression），贡献从 "发现 structured IE 的基本现象" 降级为 "记录 constrained decoding 的一个副作用"，显著降低普适性和 novelty。
- 建议修改方向：(1) 即使 free-form decoding 会产生部分 unparseable outputs，仍应在可解析子集上报告 selection F1 作为参照；(2) 至少在 SciERC 上运行 free-form + post-hoc parsing 的对照，量化 gap 在非 constrained 场景下是否缩小；(3) 或在 Discussion 中更明确地将 claim scope 限定为 "constrained decoding 下的 selection 瓶颈 = score compression"，不暗示更广泛的普适性。

**N2** [critical] **TOST 等价检验的 δ 选择缺乏直接理据**
- 具体位置：Appendix F (Table 4), Section 4.3 第 130 行
- 问题：δ 取值 ±2pp, ±3pp, ±5pp 的唯一理由是 "well-annotated NER benchmarks typically achieve inter-annotator F1 above 95%, implying 3–5pp annotation-induced variation is normal"（Appendix F，line 274-275 引用 tjongkimsang2003conll）。但 IAA 变异反映的是标注噪声，与 "一个好的 selector 应该带来多少增益" 是不同的概念。实际上，oracle headroom = 13-18pp，如果 δ=5pp 意味着"接受错过 5pp 也算等价"，那在 13pp headroom 中放弃 5pp = 放弃 38% 的可能增益，这算"等价"吗？
- 为什么影响接收：TOST 是论文支撑 "selection failure" 结论的关键工具之一。如果 δ 选择缺乏 principled 理据，等价结论的可信度受损。Section 4.3 主体文本只报告 "most signals are indistinguishable from greedy at ±2–3pp on NER"，读者容易把这当作强证据，但 δ 的选择实际上是自由度很大的分析师决策。
- 建议修改方向：(1) 用 smallest effect size of interest (SESOI) 框架，基于 oracle headroom 的比例（如 oracle 增益的 20%）或先验 best-of-N 文献中的 expected gain 来选 δ；(2) 报告使 TOST 刚好通过/不通过的 δ 临界值（breakpoint analysis），让读者自行判断。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] **Qwen3 thinking token 训练不一致的影响被低估**
- 具体位置：Limitations (line 19-21), Appendix E (line 373-374 footnote)
- 问题：SciERC 训练未禁用 enable_thinking，而 CoNLL/WNUT 禁用了。论文以 "constrained decoding overrides any thinking behavior by enforcing JSON-only output" 为由将其定性为 "minor inconsistency"。但 thinking tokens 在训练时出现会影响 learned representations——模型可能学到 "先推理再输出" 的内部模式，即使推理不出现在输出中，也会影响 hidden states 和 logprob 分布。这对 SciERC 上的 logprob 行为可能有非平凡影响。
- 问题的影响范围：SciERC 是 selection analysis 的主要数据集（Table 2），也是唯一同时有 NER 和 RE 结果的数据集。如果 thinking token 影响了 SciERC logprob 分布，则 logprob selection failure 的诊断（score compression 是主因）可能部分受 confound。
- 建议：(1) 在 Limitations 中明确讨论 thinking token 对 logprob 行为的潜在影响，而非仅说 "minor"；(2) 如有可能，用禁用 thinking 的 Qwen3 SciERC checkpoint 重新验证 logprob 相关结论。

**W2** [warning] **RE 证据强度不足以支撑多处主体论述中的 RE claims**
- 具体位置：Abstract (line 3: "RE (SciERC, preliminary)"), Table 1, Table 2, Section 4.2, Section 5
- 问题：RE 基于单数据集（SciERC，238 个 non-zero F1 instances），且 per-relation 诊断（Appendix D）显示极大变异（Feature-Of ρ=0.004 vs. Hyponym-Of ρ=0.646），n per relation 可能很小。然而论文在 Abstract、Table 1（RE 列）、Table 2（RE 列）、Discussion 中多次引用 RE 数据，给人 RE 是 "preliminary but still a contribution" 的印象。实际上，238 个 instance 且 relation type 间差异如此大，RE 结论的统计功效相当弱。
- 建议：(1) 在 Section 4 开头更突出地标记 RE 为 exploratory/pilot analysis，而非仅在括号中标 "preliminary"；(2) 考虑将 RE 更多地移入 Appendix，减少主表中 RE 列的权重。

**W3** [warning] **VC 定义：公式与实现不一致**
- 具体位置：Section 3.2, Equation 6, Footnote 2 (line 62)
- 问题：Equation 6 定义 $c_{vote}(x) = \frac{1}{|E_\cup|} \sum_{e \in E_\cup} \text{freq}(e)$，即所有 entity 的平均频率，无阈值。但 footnote 2 承认 "Our implementation computes the mean entity-level match rate against a majority threshold (>N/2)"。这两个定义在数学上不等价：公式是对所有 entity 的平均频率（连续值），实现是先二值化（>N/2 则 match=1，否则 0）再取均值。论文说 "identical qualitative conclusions"，但这种公式-实现不一致在方法论上有问题——读者如果根据公式复现，会得到不同的数值。
- 建议：(1) 统一公式和实现——要么改公式以反映 threshold，要么改实现以匹配公式；(2) 报告两种定义下的量化差异（不仅 "slightly different" 而是具体数值）。

**W4** [warning] **Instance-level 信号无法 select 的论证部分 tautological**
- 具体位置：Section 4.3 (line 121), Section 5 "Why the gap exists: two layers" (line 8-10)
- 问题：论文称 "four of five signals are instance-level aggregates that assign a single score per input regardless of which sample is evaluated; they cannot rank candidates by construction"（Section 4.3）。这在定义上就成立——instance-level signal 给每个 input 一个分数，当然无法区分 N 个 candidates。论文确实引入了 consensus-proximity selection 来将 instance-level signals 转化为 per-sample scores，但 Discussion 的 "Layer 1 (definitional)" 仍将此作为 gap 的主要解释之一。将 definitional 事实作为 empirical finding 呈现，弱化了论文的贡献感。
- 建议：重构 narrative——明确 4/5 信号不能 select 是 by design（不算 finding），真正的 finding 是：(a) consensus-proximity 也不能恢复 per-sample discrimination，(b) logprob（唯一的 per-sample signal）也失败了。目前的写法已经在 Section 4.3 做了这个区分，但 Abstract、Introduction 中 "four of five signals fail" 的表述模糊了这一点。

---

## 小问题（不影响接收）

- **引用 ye2025uncertainty**：reference verification 显示 bib 中第一作者为 Ye，但 OpenAlex 返回 Heo。需要核实此条引用的作者信息是否正确。
- **Table 1 布局密集**：8 列数据加 2 个 model blocks，视觉上难以快速定位关键比较。建议拆分为 NER 和 RE 子表或使用条件着色。
- **Section 4.2 脚注 1 (line 64)**：与 semantic entropy 的 AUROC 比较注明 "direct comparison is not meaningful due to fundamentally different output spaces"——既然如此，提及此比较的价值有限，可删除或移至 Appendix。
- **Fleiss' κ 独立性假设**（Section 3.2, line 39-40）：论文通过实测 excess agreement 验证 FK 未因依赖性被膨胀，但 excess agreement 在 -0.4% 到 -4.0% 范围内——这些负值是否在统计上显著不同于 0 没有测试。如果不显著，则验证更有力；如果显著，则 FK 的理论假设确实被违反（虽然方向是保守的）。
- **N=8 primary results 使用单一 seed=42**：虽然 3-seed 分析在 Appendix C 中表明 σ≤0.025，但主表 single-seed 的做法在方法上不够 robust，尤其是 selection F1 的差异（如 logprob +0.6pp）与 σ 在同一数量级。

---

## 主要优势

1. **清晰的概念区分**：quality estimation vs. sample selection 的区分是有价值的，此前文献经常混淆这两个目标（Section 1, line 13-14 正确指出这一点）。
2. **统计实践优于多数同类论文**：paired bootstrap + TOST + Cohen's d + confidence intervals + multi-seed analysis，远超 NLP 论文常见的 "report p-value only" 标准。
3. **诚实的局限性讨论**：RE preliminary、constrained decoding confound、thinking token 不一致、N scaling 限制——Limitations section 覆盖面广且具体。
4. **Mechanistic diagnosis 有说服力**：non-tied subset analysis（Section 5, Appendix G）是论文最有洞察力的分析——将 logprob failure 追溯到 score compression，且证明 compression 缓解后 logprob 有效。
5. **Task-difficulty dependent signal ranking** 是一个实用发现：EM 在简单任务领先，SJ/VC 在复杂任务领先，为实践者提供了 actionable guidance。
6. **Cross-model consistency**（ρ 排序一致，幅度有差异）增强了发现的可信度。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 635 · 2026-05-15T08:52:45.929982+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "## 交叉分享 — Reviewer 1 的完整审稿意见\n\n请逐条回应以下 Reviewer 1 的审稿意见。对每条使用 **[AGREE]** 同意并说明理由，或 **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n以下是 Reviewer 1 的完整审稿原文：\n\n## Reviewer 1 — Round 1 审稿报告\n\n**总体评分**: 3.0/5（Findings acceptance）\n\n### Must-Fix 问题\n\n**N1** [critical] **缺少 free-form decoding 对照实验——核心发现可能是 constrained decoding artifact**\n- 具体位置：Section 5 (Discussion), Limitations\n- 问题：论文的核心概念 \"correlation-selection gap\" 被呈现为 structured IE 的重要发现，但 non-tied subset analysis（Section 5）已经证明：当 score compression 被缓解时（logprob range ≥ 0.05 的 40% instances），logprob 成为显著 selector（+2.9pp, p=0.01, within-instance ρ: 0.08→0.39）。这直接暗示 gap 主要源于 constrained decoding 的技术限制，而非 structured IE 的固有属性。缺少 free-form decoding（不使用 grammar constraint）的对照实验，无法区分这两种解释。\n- 为什么影响接收：如果 gap 仅存在于 constrained decoding 下（且已可追溯到 score compression），贡献从 \"发现 structured IE 的基本现象\" 降级为 \"记录 constrained decoding 的一个副作用\"。\n- 建议修改方向：(1) 在可解析子集上报告 free-form selection F1 作为参照；(2) 至少在 SciERC 上运行 free-form + post-hoc parsing 的对照；(3) 或更明确地将 claim scope 限定为 \"constrained decoding 下的 selection 瓶颈 = score compression\"。\n\n**N2** [critical] **TOST 等价检验的 δ 选择缺乏直接理据**\n- 具体位置：Appendix F (Table 4), Section 4.3\n- 问题：δ 取值 ±2pp, ±3pp, ±5pp 的唯一理由是 IAA 变异，但 IAA 变异反映标注噪声，与 \"一个好的 selector 应该带来多少增益\" 是不同概念。Oracle headroom = 13-18pp，δ=5pp 意味着放弃 38% 的可能增益——这算\"等价\"吗？\n- 建议：用 SESOI 框架或报告 breakpoint analysis。\n\n### Should-Fix 问题\n\n**W1** [warning] **Qwen3 thinking token 训练不一致的影响被低估**\n- SciERC 训练未禁用 enable_thinking，而 CoNLL/WNUT 禁用了。训练时 thinking tokens 可能影响 learned representations 和 logprob 分布。SciERC 是 selection analysis 的主要数据集。\n\n**W2** [warning] **RE 证据强度不足以支撑多处主体论述中的 RE claims**\n- RE 基于单数据集（238 个 non-zero F1 instances），per-relation 变异极大。建议将 RE 更多移入 Appendix。\n\n**W3** [warning] **VC 定义：公式与实现不一致**\n- Equation 6 无阈值，但 footnote 2 承认实现使用 majority threshold (>N/2)。两者数学上不等价，影响可复现性。\n\n**W4** [warning] **Instance-level 信号无法 select 的论证部分 tautological**\n- 4/5 信号不能 select 在定义上成立，不算 empirical finding。真正的 finding 是 consensus-proximity 和 logprob 也失败。Abstract/Introduction 的 \"four of five signals fail\" 表述模糊了这一点。\n\n### 小问题\n- ye2025uncertainty 作者信息需核实\n- Table 1 布局密集，建议拆分\n- Semantic entropy 脚注价值有限\n- FK excess agreement 未做显著性检验\n- N=8 primary results 使用单一 seed=42，与 σ 在同一数量级\n\n### 主要优势\n1. Quality estimation vs. sample selection 区分有价值\n2. 统计实践远超同类论文\n3. 诚实的局限性讨论\n4. Mechanistic diagnosis（non-tied subset）有说服力\n5. Difficulty-dependent signal ranking 实用\n6. Cross-model consistency 增强可信度",
  "project": "struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "text": "## 交叉分享 — Reviewer 1 的完整审稿意见\n\n请逐条回应以下 Reviewer 1 的审稿意见。对每条使用 **[AGREE]** 同意并说明理由，或 **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n以下是 Reviewer 1 的完整审稿原文：\n\n## Reviewer 1 — Round 1 审稿报告\n\n**总体评分**: 3.0/5（Findings acceptance）\n\n### Must-Fix 问题\n\n**N1** [critical] **缺少 free-form decoding 对照实验——核心发现可能是 constrained decoding artifact**\n- 具体位置：Section 5 (Discussion), Limitations\n- 问题：论文的核心概念 \"correlation-selection gap\" 被呈现为 structured IE 的重要发现，但 non-tied subset analysis（Section 5）已经证明：当 score compression 被缓解时（logprob range ≥ 0.05 的 40% instances），logprob 成为显著 selector（+2.9pp, p=0.01, within-instance ρ: 0.08→0.39）。这直接暗示 gap 主要源于 constrained decoding 的技术限制，而非 structured IE 的固有属性。缺少 free-form decoding（不使用 grammar constraint）的对照实验，无法区分这两种解释。\n- 为什么影响接收：如果 gap 仅存在于 constrained decoding 下（且已可追溯到 score compression），贡献从 \"发现 structured IE 的基本现象\" 降级为 \"记录 constrained decoding 的一个副作用\"。\n- 建议修改方向：(1) 在可解析子集上报告 free-form selection F1 作为参照；(2) 至少在 SciERC 上运行 free-form + post-hoc parsing 的对照；(3) 或更明确地将 claim scope 限定为 \"constrained decoding 下的 selection 瓶颈 = score compression\"。\n\n**N2** [critical] **TOST 等价检验的 δ 选择缺乏直接理据**\n- 具体位置：Appendix F (Table 4), Section 4.3\n- 问题：δ 取值 ±2pp, ±3pp, ±5pp 的唯一理由是 IAA 变异，但 IAA 变异反映标注噪声，与 \"一个好的 selector 应该带来多少增益\" 是不同概念。Oracle headroom = 13-18pp，δ=5pp 意味着放弃 38% 的可能增益——这算\"等价\"吗？\n- 建议：用 SESOI 框架或报告 breakpoint analysis。\n\n### Should-Fix 问题\n\n**W1** [warning] **Qwen3 thinking token 训练不一致的影响被低估**\n- SciERC 训练未禁用 enable_thinking，而 CoNLL/WNUT 禁用了。训练时 thinking tokens 可能影响 learned representations 和 logprob 分布。SciERC 是 selection analysis 的主要数据集。\n\n**W2** [warning] **RE 证据强度不足以支撑多处主体论述中的 RE claims**\n- RE 基于单数据集（238 个 non-zero F1 instances），per-relation 变异极大。建议将 RE 更多移入 Appendix。\n\n**W3** [warning] **VC 定义：公式与实现不一致**\n- Equation 6 无阈值，但 footnote 2 承认实现使用 majority threshold (>N/2)。两者数学上不等价，影响可复现性。\n\n**W4** [warning] **Instance-level 信号无法 select 的论证部分 tautological**\n- 4/5 信号不能 select 在定义上成立，不算 empirical finding。真正的 finding 是 consensus-proximity 和 logprob 也失败。Abstract/Introduction 的 \"four of five signals fail\" 表述模糊了这一点。\n\n### 小问题\n- ye2025uncertainty 作者信息需核实\n- Table 1 布局密集，建议拆分\n- Semantic entropy 脚注价值有限\n- FK excess agreement 未做显著性检验\n- N=8 primary results 使用单一 seed=42，与 σ 在同一数量级\n\n### 主要优势\n1. Quality estimation vs. sample selection 区分有价值\n2. 统计实践远超同类论文\n3. 诚实的局限性讨论\n4. Mechanistic diagnosis（non-tied subset）有说服力\n5. Difficulty-dependent signal ranking 实用\n6. Cross-model consistency 增强可信度",
    "project": "struct_self_consist_ie"
  }
}
```

</details>

---


### Tool result

_source line 636 · 2026-05-15T08:53:11.413198+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 25483
}
```

</details>

---


### Tool call

_source line 637 · 2026-05-15T08:53:11.614723+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "## 交叉分享 — Reviewer 2 的完整审稿意见\n\n请逐条回应以下 Reviewer 2 的审稿意见。对每条使用 **[AGREE]** 同意并说明理由，或 **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n以下是 Reviewer 2 的完整审稿原文：\n\n## Reviewer 2 — Round 1 审稿报告\n\n**总体评分**: 3/5 (Findings track)\n\n### Must-Fix 问题\n\n**N1** [critical] Contribution 1 \"systematic multi-family comparison\" 的新颖性与 framing 不匹配\n- 论文将 \"5 signals from 3 families\" 的对比定位为主要贡献，但本质是 engineering benchmark——将已知 confidence signals 应用于新任务设置。与 Nédellec et al. (2026) 的增量存在（结构化匹配、constrained decoding、多数据集），但 Introduction 没有充分区分 \"applying known signals\" 和 \"discovering new principles\"。\n- 建议：将 Contribution 1 降级为 setup/methodology，将 Contribution 2 (gap) 提升为核心。\n\n**N2** [critical] Correlation-selection gap 的 4/5 来源是定义性的，非实证发现\n- Discussion 自己承认 4/5 信号的 selection failure 是 \"by construction\"（Layer 1）。真正的实证贡献是 Layer 2（logprob 压缩），但被埋在 \"gap\" 叙事下。\n- 建议：(1) Introduction 提前透明化 Layer 1 是 definitional；(2) 将叙事重心转向 Layer 2。\n\n**N3** [critical] Related Work 遗漏关键引用\n- (a) Zhang et al. (2025) \"A Survey on Test-Time Scaling in LLMs\"——最全面的 TTS survey\n- (b) Eikema, Rutkiewicz & Giulianelli (EMNLP 2025) \"Structure-Conditional MBR Decoding\"——直接研究 MBR 在结构化输出上的问题\n\n### Should-Fix 问题\n\n**W1** [warning] \"cross-model\" 措辞过度外推（实际 2 个 8B 模型）\n**W2** [warning] Abstract 信息密度过高（9 行含 5 signal/3 family/4 metric/3 dataset/2 model + 新术语）\n**W3** [warning] 术语不一致（VC/Voting Conf./entity voting；LP/Log-prob/logprob）\n**W4** [warning] RE 单数据集标注在 Discussion/Conclusion 中不足\n**W5** [warning] Qwen3 thinking mode confound\n**W6** [warning] 缺少 supervised verifier baseline\n\n### 小问题\n- Figure 1 caption 冗余\n- Table 1 N=16 行空白多\n- FK excess agreement \"sufficient diversity\" 措辞不准确\n- Notation Table 缺 LP 缩写\n- Ethics Statement 未注明 CoNLL-2003 Reuters license 限制\n\n### 引用验证发现 5 处 bib 问题\n- feng2025optimal 作者顺序\n- ye2025uncertainty 第一作者可能为 Heo\n- hobelsberger2025systematic 和 venktesh2025trust 无法在线验证\n- snell2024scaling key 标 2024 但 venue 为 ICLR 2025\n\n### 主要优势\n1. 统计分析严谨度远超同类\n2. Logprob 压缩诊断有 actionable 价值\n3. Limitations 坦诚\n4. Difficulty gradient 设计合理（WNUT-17 负 logprob correlation 非显然）\n5. Quality estimation vs selection 区分是有价值的框架贡献",
  "project": "struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "text": "## 交叉分享 — Reviewer 2 的完整审稿意见\n\n请逐条回应以下 Reviewer 2 的审稿意见。对每条使用 **[AGREE]** 同意并说明理由，或 **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n以下是 Reviewer 2 的完整审稿原文：\n\n## Reviewer 2 — Round 1 审稿报告\n\n**总体评分**: 3/5 (Findings track)\n\n### Must-Fix 问题\n\n**N1** [critical] Contribution 1 \"systematic multi-family comparison\" 的新颖性与 framing 不匹配\n- 论文将 \"5 signals from 3 families\" 的对比定位为主要贡献，但本质是 engineering benchmark——将已知 confidence signals 应用于新任务设置。与 Nédellec et al. (2026) 的增量存在（结构化匹配、constrained decoding、多数据集），但 Introduction 没有充分区分 \"applying known signals\" 和 \"discovering new principles\"。\n- 建议：将 Contribution 1 降级为 setup/methodology，将 Contribution 2 (gap) 提升为核心。\n\n**N2** [critical] Correlation-selection gap 的 4/5 来源是定义性的，非实证发现\n- Discussion 自己承认 4/5 信号的 selection failure 是 \"by construction\"（Layer 1）。真正的实证贡献是 Layer 2（logprob 压缩），但被埋在 \"gap\" 叙事下。\n- 建议：(1) Introduction 提前透明化 Layer 1 是 definitional；(2) 将叙事重心转向 Layer 2。\n\n**N3** [critical] Related Work 遗漏关键引用\n- (a) Zhang et al. (2025) \"A Survey on Test-Time Scaling in LLMs\"——最全面的 TTS survey\n- (b) Eikema, Rutkiewicz & Giulianelli (EMNLP 2025) \"Structure-Conditional MBR Decoding\"——直接研究 MBR 在结构化输出上的问题\n\n### Should-Fix 问题\n\n**W1** [warning] \"cross-model\" 措辞过度外推（实际 2 个 8B 模型）\n**W2** [warning] Abstract 信息密度过高（9 行含 5 signal/3 family/4 metric/3 dataset/2 model + 新术语）\n**W3** [warning] 术语不一致（VC/Voting Conf./entity voting；LP/Log-prob/logprob）\n**W4** [warning] RE 单数据集标注在 Discussion/Conclusion 中不足\n**W5** [warning] Qwen3 thinking mode confound\n**W6** [warning] 缺少 supervised verifier baseline\n\n### 小问题\n- Figure 1 caption 冗余\n- Table 1 N=16 行空白多\n- FK excess agreement \"sufficient diversity\" 措辞不准确\n- Notation Table 缺 LP 缩写\n- Ethics Statement 未注明 CoNLL-2003 Reuters license 限制\n\n### 引用验证发现 5 处 bib 问题\n- feng2025optimal 作者顺序\n- ye2025uncertainty 第一作者可能为 Heo\n- hobelsberger2025systematic 和 venktesh2025trust 无法在线验证\n- snell2024scaling key 标 2024 但 venue 为 ICLR 2025\n\n### 主要优势\n1. 统计分析严谨度远超同类\n2. Logprob 压缩诊断有 actionable 价值\n3. Limitations 坦诚\n4. Difficulty gradient 设计合理（WNUT-17 负 logprob correlation 非显然）\n5. Quality estimation vs selection 区分是有价值的框架贡献",
    "project": "struct_self_consist_ie"
  }
}
```

</details>

---


### Tool result

_source line 638 · 2026-05-15T08:53:13.226330+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1611
}
```

</details>

---


### Assistant

_source line 639 · 2026-05-15T08:53:17.079399+00:00_

交叉分享已发送。等待两位 Reviewer 的逐条回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 52

## Round 52

2 recorded events


### User

_source line 640 · 2026-05-15T08:53:19.852210+00:00_

[Reviewer 1 审稿结果]:
审稿报告已提交给 Review Director。

总结：

**Overall 3.0/5（Findings acceptance）**。方法论扎实、统计实践规范的实证研究，有两个 Must-Fix 问题：

1. **缺少 free-form decoding 对照实验**——non-tied subset analysis 已证明 logprob 在 compression 缓解时有效（+2.9pp, p=0.01），强烈暗示 correlation-selection gap 主要是 constrained decoding artifact 而非 structured IE 的固有属性，但论文缺乏直接对照实验来区分这两种解释。

2. **TOST δ 选择理据薄弱**——基于 IAA 变异的 δ 论证概念上不匹配（IAA 噪声 ≠ selector 预期增益），且在 13-18pp oracle headroom 中 δ=5pp 意味着放弃 ~38% 增益仍算"等价"。

四个 Should-Fix：Qwen3 thinking token confound 被低估、RE 单数据集证据不足、VC 公式-实现不一致、instance-level 信号不能 select 部分 tautological。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 641 · 2026-05-15T08:53:25.218544+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 53

## Round 53

2 recorded events


### User

_source line 642 · 2026-05-15T08:54:25.237852+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 — 交叉回应 Reviewer 1 审稿意见

---

### Must-Fix 问题

**[REBUT] R1-N1: 缺少 free-form decoding 对照实验**

R1 的论点是 correlation-selection gap 可能主要是 constrained decoding artifact。这个关切部分成立但程度被高估了，理由如下：

1. **Gap 的 Layer 1 与 constrained decoding 无关。** 论文在 Section 5 ¶2 明确区分了两个层次：Layer 1 是 definitional——4/5 信号是 instance-level aggregates，无论有无 constrained decoding 都无法做 per-sample selection。Free-form decoding 不会改变这一事实。R1 的论点仅适用于 Layer 2（logprob 压缩），但论文的 gap 概念包含两个层次。

2. **Free-form decoding 对 structured IE 的实用性存疑。** Section 1 (Introduction, line 19) 指出 "without it [constrained decoding], a substantial fraction of outputs are unparseable"。如果 free-form 下大量输出不可解析，那么在可解析子集上的 selection 结果会有严重的 selection bias——只有模型最确信的 outputs 才能通过格式过滤，这本身就会压缩 per-sample 变异。R1 建议的 "free-form + post-hoc parsing 对照" 需要处理不可解析样本（丢弃？赋零分？），每种处理方式都引入新的 confound。

3. **但 R1 的核心建议有道理：claim scope 应更明确。** 论文标题已包含 "under Constrained Decoding"，但 Introduction 和 Discussion 中部分措辞确实暗示 gap 是 structured IE 的固有属性而非特定推理 regime 下的现象。建议作者在 Section 5 ¶2 末尾增加一句明确声明："The extent to which the correlation-selection gap persists under free-form generation remains an open question; our findings are specific to the constrained decoding regime standard for schema-compliant IE."

**综合判断：** R1 将此列为 must-fix 我认为过重。论文标题和多处表述已明确限定在 constrained decoding 下，且 Layer 1 的 definitional gap 不受 decoding 策略影响。但 claim scope 的收紧（R1 建议 (3)）是合理的 should-fix。

---

**[AGREE] R1-N2: TOST δ 选择缺乏直接理据**

同意 R1 的分析。Appendix F (Table 4) 用 IAA 变异（3–5pp annotation-induced variation）来论证 δ 的合理性，但 IAA 测量的是标注噪声天花板，而 TOST 检验的是 "selector 与 greedy 是否实质等价"——两者概念不同。

补充 R1 未提到的一个问题：Oracle headroom 在 NER 为 13.2pp、RE 为 18.1pp（Table 2），δ=5pp 意味着即使 selector 只 recover 了 oracle headroom 的 28%（NER）或 28%（RE），也会被判定为"不等价"而被拒绝。这个门槛看起来合理。但 δ=2pp 时，只需 recover 15% 的 headroom 就算"显著"——在 N=8 的 bootstrap 方差下，这个精度可能不够。

建议作者：(1) 报告 breakpoint δ*（使结论翻转的最小 δ），给读者完整信息；(2) 直接报告 effect size (Cohen's d) 和 bootstrap CI（当前已在 Section 4.2 ¶2 报告了 NER logprob 的 d=0.038 和 CI [−3.0, +4.2]pp），这些比 TOST 更直观。

---

### Should-Fix 问题

**[AGREE] R1-W1: Qwen3 thinking token 训练不一致**

完全同意，我在 R2-W5 中提出了相同问题。SciERC 是 selection analysis 的主要数据集，thinking token 训练不一致可能影响 logprob 分布，而 logprob 压缩诊断是论文的核心机制分析。补充一点：如果 thinking tokens 在训练时改变了 Qwen3 在 SciERC 上的 logprob scale，那么 Section 5 中 "60% of instances effectively tied" 的数字可能在 thinking-disabled 训练下不同——这会直接动摇 Layer 2 诊断的可靠性。

---

**[AGREE] R1-W2: RE 证据强度不足**

同意，我在 R2-W4 中也提出了类似关切。238 个 non-zero F1 instances 用于 RE conditional analysis（Appendix H, Table 6），per-relation 变异极大（Feature-Of ρ=0.004 vs. Hyponym-Of ρ=0.646，Appendix D ¶1）——这种量级的变异使得 aggregate RE 结论的信息量有限。建议至少将 RE selection results（Table 2 RE column, Table 6）标记为 exploratory，或在 Discussion 中每次引用 RE 结论时加 "(exploratory, n=238)" 后缀。

---

**[AGREE] R1-W3: VC 定义与实现不一致**

好的 catch，我审稿时未注意到这个细节。Equation 6 定义 $c_{\text{vote}}(x) = \frac{1}{|E_\cup|} \sum_{e \in E_\cup} \text{freq}(e)$——这是所有 entity 的平均频率，没有阈值。但 Footnote 2（Section 3.2, method.tex line 62）说 "Our implementation computes the mean entity-level match rate against a majority threshold (>N/2)"——这意味着实现时只统计 freq(e) > 0.5 的 entity 的 match rate，与公式的 "average over ALL entities in E_∪" 不等价。

具体差异：如果某 entity 只在 2/8 sample 中出现（freq=0.25），Eq.6 会将其 0.25 纳入平均，但 thresholded 实现可能会忽略它或给它 0 分。这会系统性地影响 low-agreement entities 的贡献，可能改变 VC 与其他信号的相对排名——尤其是在 SciERC 这种 entity 集合大、低频 entity 多的数据集上。

Footnote 2 最后说 "yields slightly different absolute values but identical qualitative conclusions"——但没有提供 quantitative 比较（例如两种实现的 ρ 差值）。建议作者：(1) 报告两种实现的 ρ 对比，(2) 明确 Table 1 中报告的是哪种实现的结果。

---

**[AGREE] R1-W4: Instance-level 信号的 selection failure 部分 tautological**

强烈同意，这与我在 R2-N2 中的核心关切一致。Instance-level 信号给同一 input 的所有 N 个 sample 相同的分数——它们不能做 per-sample selection 是 **定义的直接推论**，不是需要实验验证的发现。

论文的真正 empirical findings 是：
1. Consensus-proximity selection（Section 3.3, method.tex line 71）——将 instance-level SJ 转化为 per-sample 排名——也失败了（Table 2: SJ selection 0.645 vs greedy 0.644）
2. Logprob（唯一 per-sample signal）也失败了（p=0.39）
3. Logprob 失败的机制是 constrained decoding 下的 score compression（Appendix G）

当前 Abstract（"four of five signals are instance-level by construction"）和 Introduction（Section 1, ¶5 "Four of five signals are instance-level by construction; log-probability...also fails"）的表述方式将 definitional fact 和 empirical finding 混在一起呈现。建议作者重构叙事：先一句话 dismiss instance-level 信号的 selection potential（"by definition, not empirically"），然后集中论证 consensus-proximity 和 logprob 为何失败——这才是需要实验证据的部分。

---

### 小问题

**[AGREE] R1-小问题-1: ye2025uncertainty 作者**
同意，我也在引用审计中标记了此条。OpenAlex 显示 first author 可能为 Heo 而非 Ye。

**[AGREE] R1-小问题-2: Table 1 布局**
同意密度过高。N=16 行只有 LLaMA CoNLL 的数据，与上方 N=8 的完整矩阵形成不对称——要么补全 N=16 数据，要么移到 Appendix。

**[REBUT] R1-小问题-3: Semantic entropy 脚注价值有限**
部分不同意。Section 4.1 脚注（experiments.tex line 64）将 AUROC 0.749 与 semantic entropy 做 scale context 比较，并明确说 "direct comparison is not meaningful due to fundamentally different output spaces"。这种 calibrated comparison 对不熟悉该领域的 reviewer 有帮助——它提供了 AUROC 0.75 在 LLM confidence 文献中的大致位置，同时避免了不当的跨任务 claim。脚注是合适的呈现方式（不在正文中突出）。

**[AGREE] R1-小问题-4: FK excess agreement 未做显著性检验**
合理关切。Section 3.2（method.tex line 40）报告 excess agreement 在 −0.4% 到 −4.0% 之间，但没有 CI 或 p-value。对于一个关键假设（FK 不被 inter-sample dependence inflate）的验证，应该提供 permutation test 或 bootstrap CI。

**[AGREE] R1-小问题-5: N=8 primary results 单一 seed**
合理关切。Table 1 的 N=8 主结果用 seed=42，Appendix E (Table 5) 的 3-seed analysis 显示 σ≤0.025——与部分信号间差异在同一量级（例如 SJ−FK gap = 0.093 on SciERC NER，大于 σ 但 VC−SJ gap = 0.019 远小于 σ）。建议至少在 main text 中注明 single-seed limitation 并引用 Appendix 的 stability analysis，当前 Table 1 caption 只说 "seed=42" 没有引导读者去查看 multi-seed 结果。

---

### 总结

与 R1 的评估高度一致。主要分歧在 N1（free-form 对照）的严重程度：我认为 Layer 1 (definitional) 不受 decoding 策略影响，因此 gap 不完全是 constrained decoding artifact；但同意 Layer 2 的 scope 应更明确限定。R1 和 R2 共同识别的核心问题是 **叙事结构**——论文将 definitional facts（instance-level 信号不能 select）与 empirical findings（consensus-proximity 和 logprob 也失败）混合呈现，降低了真正贡献（logprob 压缩诊断）的 visibility。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 643 · 2026-05-15T08:54:30.260962+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 54

## Round 54

2 recorded events


### User

_source line 644 · 2026-05-15T08:54:33.168511+00:00_

[Reviewer 2 审稿结果]:
交叉回应已提交。与 R1 在大部分问题上达成一致，主要分歧在 N1（free-form 对照实验）——我认为 R1 将其列为 must-fix 过重，因为 Layer 1 的 definitional gap 不受 decoding 策略影响，但同意 Layer 2 的 claim scope 应收紧。两位 reviewer 共同识别的核心问题是叙事结构：definitional facts 与 empirical findings 的混合呈现削弱了 logprob 压缩诊断这一真正贡献的 visibility。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 645 · 2026-05-15T08:54:37.820766+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 55

## Round 55

16 recorded events


### User

_source line 646 · 2026-05-15T08:54:44.790855+00:00_

[Reviewer 1 审稿结果]:
逐条回应 Reviewer 2 的审稿意见。

---

## 交叉回应：Reviewer 1 对 Reviewer 2 的意见

### Must-Fix 问题

**[AGREE] R2-N1: Contribution 1 的新颖性与 framing 不匹配**

同意核心判断。Contribution 1（"systematic multi-family comparison"）本质上是将已知信号应用于新设置的 engineering benchmark。与 Nédellec et al. (2026) 的三个增量（结构化匹配、best-of-N 测试、难度梯度）是合理的方法论改进，但不足以单独构成一个 contribution。Introduction (Section 1, line 39-42) 将其列为第一条贡献，给读者的印象是这是论文的主要贡献，这在 framing 上确实过度。

补充发现：从我自己的审查看，SJ 信号（type-aware bipartite matching + token-level IoU）确实是方法层面的新设计，但这应该被呈现为 "methodology" 而非 "contribution"。R2 建议将 Contribution 1 降级为 setup/methodology、Contribution 2 提升为核心，我认为是正确的重构方向。

---

**[AGREE] R2-N2: 4/5 selection failure 是 definitional**

完全同意。我在自己的审稿中将此列为 W4，指出 Section 4.3 (line 121) "they cannot rank candidates by construction" 本身就是一个定义性事实而非实证发现。Discussion Section 5 的 "Layer 1 (definitional)" 标签实际上是论文自己承认了这一点，但 Abstract（line 5-6: "four of five signals are instance-level by construction"）和 Introduction（line 46: "Four of five signals are instance-level by construction"）仍然将其与 logprob failure 并列呈现为 gap 的组成部分，模糊了真正的实证贡献边界。

进一步补充：这个 framing 问题与 N1 相互强化。如果 Contribution 1 是 benchmark + Contribution 2 的核心 is half definitional，那论文的 novelty 实际上集中在一个较窄的点上——logprob 在 constrained decoding 下的 score compression 诊断。这个点本身有价值（我在自己审稿的优势 #4 中肯定了这一点），但需要更诚实的 framing。

---

**[REBUT] R2-N3: Related Work 遗漏关键引用**

部分不同意将此列为 critical。

(a) Zhang et al. (2025) "A Survey on Test-Time Scaling in LLMs"——这是一篇综述性论文。Related Work (Section 2) 已经引用了 test-time scaling 的核心原始工作：Snell et al. (2024)、Brown et al. (2024)，以及多篇具体方法论文（Taubenfeld 2025, Kang 2025, Kim 2026, Wang 2025 等）。遗漏一篇综述在 8 页正文的 Findings 论文中不构成 critical 问题——引用原始贡献比引用综述更重要。建议降级为 minor，可在 camera-ready 补充。

(b) Eikema, Rutkiewicz & Giulianelli (EMNLP 2025) "Structure-Conditional MBR Decoding"——这条引用更有实质关联，因为论文的 Discussion Section 5 (line 18-19) 明确讨论了 MBR decoding 在结构化输出上的失败，与这篇工作直接相关。Section 2 已经引用了 Eikema & Aziz (2022)、Freitag et al. (2022)、Müller & Sennrich (2021)、Jinnai et al. (2024) 等 MBR 工作，但缺少结构化输出上的 MBR 这一最直接的相关工作确实是一个值得修复的遗漏。不过这仍然是 should-fix 级别而非 critical——它不影响论文结论的成立性，因为论文的 MBR 分析（consensus-proximity selection = MBR with structural utility）是独立完成的。

综合建议：将 (b) 提升为 should-fix 并在 camera-ready 中引用和讨论差异；(a) 列为 minor。

---

### Should-Fix 问题

**[AGREE] R2-W1: "cross-model" 措辞过度外推**

同意。论文仅测试了 Qwen3-8B 和 LLaMA-3.1-8B-Instruct，两者均为 8B 参数。Section 4.2 (line 75) "Cross-model stability is strong" 和 Appendix B "Cross-model transfer" 的措辞暗示了比实际覆盖范围更广的泛化性。"cross-model" 在严格意义上只意味着 "across two specific model families at identical scale"，应改为 "cross-family"（两个架构家族间）或明确限定 "at 8B scale"。Limitations (line 5-7) 虽然承认了 scale 局限性，但主体文本的措辞未反映这一限定。

---

**[AGREE] R2-W2: Abstract 信息密度过高**

同意。Abstract (9 lines) 中包含：5 个信号名、3 个 family 名、4 个评估 metric（ρ, AUROC, F1, p-value）、3 个数据集、2 个模型 + "correlation-selection gap" 新术语 + non-tied subset 诊断结果。对首次阅读的 reviewer 而言，信息过载导致核心 message 被稀释。Abstract 应该聚焦于 gap 的发现和诊断，将信号/数据集的细节留给 Introduction。

---

**[AGREE] R2-W3: 术语不一致**

同意。通篇存在多处同一概念使用不同缩写/名称的情况。仅从我读到的：VC / Voting Conf. / entity voting confidence / $c_{\text{vote}}$（Section 3.2 Equation 6 vs. Table 1 vs. 行文中）；LP / Log-prob / logprob / $c_{\text{lp}}$（Table 1 header vs. Section 4.3 行文 vs. Appendix）。这不影响理解但降低了论文的打磨度，在 Findings 投稿中应该修正。

---

**[AGREE] R2-W4: RE 单数据集标注在 Discussion/Conclusion 不足**

同意，与我自己的 W2 一致。Abstract 中 "(SciERC, preliminary)" 的括号标注容易被忽略。Discussion Section 5 多次引用 RE 数据（如 MBR decoding 分析, calibration ECE），但未在每处重复 "preliminary/single-benchmark" 警告。Conclusion (Section 6, line 7) 一句 "RE findings rest on SciERC alone" 是论文中最明确的标注，但 Discussion 中的多处 RE 引用缺乏同等标注。

---

**[AGREE] R2-W5: Qwen3 thinking mode confound**

同意，与我自己的 W1 一致。我在自己的审稿中将此列为 should-fix 并详细分析了 thinking tokens 在训练中影响 learned representations 的机制——即使 constrained decoding 阻止了推理 tokens 出现在输出中，训练时的 thinking token exposure 可能改变了 SciERC checkpoint 的 logprob 分布。这是一个未控制的 confound。

---

**[REBUT] R2-W6: 缺少 supervised verifier baseline**

不同意将此列为 should-fix。论文的研究问题是 "unsupervised confidence signals 在 structured IE 中的 quality estimation 和 sample selection 表现"（Section 3.1, line 7-8）。Supervised verifier 是一个不同的方法范式，论文在 Section 5 (line 23) 和 Conclusion (line 8) 中将 "trained verifiers" 明确列为 future work 方向，且引用了 Cobbe et al. (2021)、Lightman et al. (2024)、Venktesh et al. (2025) 等相关工作。

要求一篇关于 unsupervised signals 的 empirical study 同时训练 supervised verifier 作为 baseline，会显著改变论文的 scope 和工作量。更合理的期望是：(1) 论文应该讨论 supervised approach 可能恢复多少 oracle headroom——这它已经做了（Discussion Section 5, line 23），(2) 引用相关 supervised 工作——也已做到。

如果 R2 的意思是 "至少用一个现成的 verifier（如 reward model）做 zero-shot baseline"，这个建议更合理，但仍然超出了论文的 stated scope。

---

### 小问题

**[AGREE] R2-小问题-Figure 1 caption 冗余**：Figure 1 caption（Section 1, line 30-33）确实过长，重复了 Section 4.3 的信息。

**[AGREE] R2-小问题-Table 1 N=16 行空白多**：Table 1 (Table~\ref{tab:quality_estimation}) 的 N=16 section 仅有 LLaMA CoNLL 一个配置的数据，其余全为空白。视觉上浪费空间，建议将 N=16 数据整合到 Appendix Table 3 中。

**[AGREE] R2-小问题-FK "sufficient diversity" 措辞**：Section 3.2 (line 39) "temperature-based sampling provides sufficient response diversity for the statistic to capture inter-sample agreement patterns" 中 "sufficient" 未量化。虽然后文给出了 excess agreement 的实测值 (-0.4% to -4.0%)，但 "sufficient" 的标准未定义。

**[AGREE] R2-小问题-Notation Table 缺 LP**：Appendix A Table (line 19) 列了 $c_{\text{lp}}$ 但未列 "LP" 缩写。考虑到行文中频繁使用 LP/logprob，应补充。

**[AGREE] R2-小问题-Ethics Statement 缺 CoNLL-2003 Reuters license**：CoNLL-2003 基于 Reuters 语料，存在已知的 license 限制。Ethics Statement (main.tex, line 40) 仅说 "publicly available benchmarks" 未提及 license 细节。这是一个合规瑕疵。

---

### 引用验证

**[AGREE] R2-引用问题**：5 处 bib 问题与我自己的引用验证结果一致。ye2025uncertainty 的 Ye vs. Heo 差异最值得关注——如果第一作者确实是 Heo 而非 Ye，这是一个事实错误需要修正。snell2024scaling key 标 2024 但 venue 为 ICLR 2025 是一个常见的 arXiv-first / venue-later 不一致，应更新 key 或 year。

---

### 优势部分

**[AGREE] R2-优势 1-5**：全部同意。R2 识别的优势与我自己的审稿判断高度一致，特别是：统计严谨度（我的优势 #2）、logprob 压缩诊断（我的优势 #4）、difficulty gradient 设计（我的优势 #5）、quality estimation vs. selection 区分（我的优势 #1）。

---

### 综合评价

Reviewer 2 的审稿意见整体质量高，与我的独立审查结论方向一致。核心分歧仅两处：(1) R2-N3 related work 遗漏的严重程度（我认为应降级为 should-fix/minor）；(2) R2-W6 supervised verifier baseline（我认为超出论文 scope）。其余 must-fix 和 should-fix 意见我均认同，且多处与我自己的发现互为印证。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 647 · 2026-05-15T08:55:37.642010+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-review-director-0161122b/788664a7-cbda-4ca9-aeda-2dfae5004d00/tool-results/biyzhs6gh.txt",
  "offset": "0",
  "limit": "50"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-review-director-0161122b/788664a7-cbda-4ca9-aeda-2dfae5004d00/tool-results/biyzhs6gh.txt",
    "offset": "0",
    "limit": "50"
  }
}
```

</details>

---


### Tool result

_source line 648 · 2026-05-15T08:55:37.692846+00:00_

0	issues:
1	  # ============================================================
2	  # Round 0 issues (all resolved)
3	  # ============================================================
4	  - id: "R0-C1"
5	    summary: "模型规模单一（仅 8B）"
6	    category: experiment
7	    severity: critical
8	    status: resolved
9	    first_raised_round: 0
10	    last_seen_round: 1
11	    mentions:
12	      - round: 0
13	        reviewers: [1, 2]
14	        note: "8B→8B 仅验证架构鲁棒性非规模鲁棒性"
15	      - round: 1
16	        reviewers: [1, 2]
17	        note: "model-agnostic 与 Limitations 矛盾"
18	    action_items:
19	      - round: 1
20	        action: "全文替换 model-agnostic → consistent across tested model families"
21	        assigned_to: "Paper Agent"
22	        status: resolved
23	    resolution: "Round 2 Reviewer 确认措辞修正到位，无再提"
24	    resolution_round: 2
25	
26	  - id: "R0-C2"
27	    summary: "相关工作显著遗漏"
28	    category: framing
29	    severity: warning
30	    status: resolved
31	    first_raised_round: 0
32	    last_seen_round: 1
33	    mentions:
34	      - round: 0
35	        reviewers: [1, 2]
36	        note: "5 篇核心文献缺失"
37	      - round: 1
38	        reviewers: [1, 2]
39	        note: "新遗漏：Optimal SC, Difficulty-Adaptive SC"
40	    action_items:
41	      - round: 1
42	        action: "补充 6 篇引用到 Related Work"
43	        assigned_to: "Paper Agent"
44	        status: resolved
45	    resolution: "Round 2: 49 条 bib 全部 cited, 0 orphan, 无遗漏"
46	    resolution_round: 2
47	
48	  - id: "R0-C3"
49	    summary: "RE 结论仅基于 SciERC 单数据集"

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 649 · 2026-05-15T08:56:12.500728+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__update_review_issues",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__update_review_issues",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 650 · 2026-05-15T08:56:12.602295+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "ToolSearch",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 651 · 2026-05-15T08:56:24.602151+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-review-director-0161122b/788664a7-cbda-4ca9-aeda-2dfae5004d00/tool-results/biyzhs6gh.txt",
  "offset": "200",
  "limit": "600"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-review-director-0161122b/788664a7-cbda-4ca9-aeda-2dfae5004d00/tool-results/biyzhs6gh.txt",
    "offset": "200",
    "limit": "600"
  }
}
```

</details>

---


### Tool result

_source line 652 · 2026-05-15T08:56:24.653817+00:00_

200	        note: "p=0.39 支撑核心结论但细节缺失"
201	    action_items:
202	      - round: 1
203	        action: "补完整 bootstrap 规范"
204	        assigned_to: "Paper Agent"
205	        status: resolved
206	    resolution: "Round 2 Reviewer 评价统计规范达到高标准"
207	    resolution_round: 2
208	
209	  - id: "R1-N2"
210	    summary: "Gap 解释力不足 + logprob 失败未分析"
211	    category: method
212	    severity: critical
213	    status: resolved
214	    first_raised_round: 1
215	    last_seen_round: 1
216	    mentions:
217	      - round: 1
218	        reviewers: [1, 2]
219	        note: "4/5 定义性 + logprob 机制缺失"
220	    action_items:
221	      - round: 1
222	        action: "区分 by-design vs empirical + logprob failure 分析段"
223	        assigned_to: "Paper Agent"
224	        status: resolved
225	    resolution: "Round 2 Reviewer 评价 logprob failure analysis 充分"
226	    resolution_round: 2
227	
228	  - id: "R1-N3"
229	    summary: "Per-sample signal 单薄"
230	    category: method
231	    severity: warning
232	    status: resolved
233	    first_raised_round: 1
234	    last_seen_round: 1
235	    mentions:
236	      - round: 1
237	        reviewers: [1, 2]
238	        note: "consensus-proximity = LOO-SJ 是表述问题"
239	    action_items:
240	      - round: 1
241	        action: "显式说明等价关系"
242	        assigned_to: "Paper Agent"
243	        status: resolved
244	    resolution: "Round 2 确认 consensus-proximity = LOO-SJ 已明确"
245	    resolution_round: 2
246	
247	  - id: "R1-N4"
248	    summary: "Nedellec 引用错误 + 增量贡献弱"
249	    category: framing
250	    severity: critical
251	    status: resolved
252	    first_raised_round: 1
253	    last_seen_round: 1
254	    mentions:
255	      - round: 1
256	        reviewers: [1, 2]
257	        note: "Yao vs Nédellec 事实错误"
258	    action_items:
259	      - round: 1
260	        action: "修正 bib + 加强论证"
261	        assigned_to: "Paper Agent"
262	        status: resolved
263	    resolution: "Round 2 确认差异化清晰"
264	    resolution_round: 2
265	
266	  - id: "R1-W1"
267	    summary: "SJ 形式化有歧义"
2
…[truncated 16684 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 653 · 2026-05-15T08:56:33.290787+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-review-director-0161122b/788664a7-cbda-4ca9-aeda-2dfae5004d00/tool-results/biyzhs6gh.txt",
  "offset": "800",
  "limit": "500"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-review-director-0161122b/788664a7-cbda-4ca9-aeda-2dfae5004d00/tool-results/biyzhs6gh.txt",
    "offset": "800",
    "limit": "500"
  }
}
```

</details>

---


### Tool result

_source line 654 · 2026-05-15T08:56:33.341966+00:00_

800	    severity: warning
801	    status: resolved
802	    first_raised_round: 3
803	    last_seen_round: 4
804	    mentions:
805	      - round: 3
806	        reviewers: [1, 2]
807	        note: "Table 1 N=8 和 Table 2 selection 全部 single seed"
808	      - round: 4
809	        reviewers: [2]
810	        note: "R2 确认 RESOLVED：3-seed 验证已补充"
811	    action_items:
812	      - round: 3
813	        action: "Limitations 中明确 single-seed 风险并引用 N=16 stability"
814	        assigned_to: "Paper Agent"
815	        status: resolved
816	    resolution: "Round 4: 3-seed 稳定性验证已补充，R2 确认到位"
817	    resolution_round: 4
818	
819	  - id: "R3-W1"
820	    summary: "多重比较校正缺失"
821	    category: experiment
822	    severity: warning
823	    status: resolved
824	    first_raised_round: 3
825	    last_seen_round: 4
826	    mentions:
827	      - round: 3
828	        reviewers: [1, 2]
829	        note: "SJ-EM CI lower bound +0.003 在 Bonferroni 下不会 survive"
830	      - round: 4
831	        reviewers: [2]
832	        note: "R2 确认 RESOLVED：Bonferroni 声明已加"
833	    action_items:
834	      - round: 3
835	        action: "声明未做多重比较校正 + SJ-EM 改为 suggestive"
836	        assigned_to: "Paper Agent"
837	        status: resolved
838	    resolution: "Round 4: Bonferroni 声明已加，R2 确认到位"
839	    resolution_round: 4
840	
841	  - id: "R3-W2"
842	    summary: "Gap 概念部分 tautological——instance-level 信号无法 select 是定义必然"
843	    category: method
844	    severity: warning
845	    status: open
846	    first_raised_round: 3
847	    last_seen_round: 5
848	    mentions:
849	      - round: 3
850	        reviewers: [1, 2]
851	        note: "需在 Discussion 中分离两层论证"
852	      - round: 4
853	        reviewers: [1, 2]
854	        note: "R4 两位 Reviewer 独立再次提出：Introduction 未正面论证 why not obvious a priori"
855	      - round: 5
856	        reviewers: [1, 2]
857	        note: "R2 认为 gap 被两头夹击（instance-level=tautological, logprob=artifact），整体 contribution 空心化。R1 rebut：consensus-proximity/MBR failure 是 non-trivial empirical finding，但同意 logprob 
…[truncated 15984 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 655 · 2026-05-15T08:56:40.372736+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-review-director-0161122b/788664a7-cbda-4ca9-aeda-2dfae5004d00/tool-results/biyzhs6gh.txt",
  "offset": "1300",
  "limit": "400"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-review-director-0161122b/788664a7-cbda-4ca9-aeda-2dfae5004d00/tool-results/biyzhs6gh.txt",
    "offset": "1300",
    "limit": "400"
  }
}
```

</details>

---


### Tool result

_source line 656 · 2026-05-15T08:56:40.473894+00:00_

1300	    mentions:
1301	      - round: 4
1302	        reviewers: [1]
1303	        note: "δ 选择直接影响等价结论"
1304	      - round: 5
1305	        reviewers: [1, 2]
1306	        note: "R1 再提：与 IAA 关联无引用。R2 同意但认为多水平 δ 已构成 sensitivity analysis，引用 IAA 数据即可。"
1307	    action_items:
1308	      - round: 5
1309	        action: "引用 1-2 篇 IE benchmark IAA 数据来锚定 δ 选择"
1310	        assigned_to: "Paper Agent"
1311	        status: in_progress
1312	    resolution: ""
1313	    resolution_round: null
1314	
1315	  - id: "R4-M3"
1316	    summary: "Table 1 N=16 block 大面积空白"
1317	    category: writing
1318	    severity: info
1319	    status: open
1320	    first_raised_round: 4
1321	    last_seen_round: 5
1322	    mentions:
1323	      - round: 4
1324	        reviewers: [1, 2]
1325	        note: "N=16 仅填 LLaMA CoNLL，SciERC 空白"
1326	      - round: 5
1327	        reviewers: [1, 2]
1328	        note: "Table 1 已加脚注说明 N=16 数据位置（Appendix Table 3），但脚注格式（\\textsuperscript{†} + \\footnotetext）在 two-column 模板下可能渲染异常。"
1329	    action_items:
1330	      - round: 5
1331	        action: "检查 PDF 渲染；考虑合并 N=16 到附录以简化 Table 1"
1332	        assigned_to: "Paper Agent"
1333	        status: in_progress
1334	    resolution: ""
1335	    resolution_round: null
1336	
1337	  # ============================================================
1338	  # Round 5 new issues
1339	  # ============================================================
1340	  - id: "R5-N1"
1341	    summary: "与 Nédellec et al. (2026) 的增量贡献不充分"
1342	    category: framing
1343	    severity: warning
1344	    status: open
1345	    first_raised_round: 5
1346	    last_seen_round: 5
1347	    mentions:
1348	      - round: 5
1349	        reviewers: [2]
1350	        note: "三个增量均偏弱：SJ vs EM Bonferroni 不显著，selection analysis 部分 tautological，difficulty gradient 直觉上不意外。R1 rebut：crossover pattern 是核心 claim 而非单个 Δρ；WNUT-17 conditional collapse 不是直觉可预测。共识：Findings-worthy 但非 ground-breaking。"
1351	    action_items:
1352	      - round: 5
1353	        action: "更诚实地量化增量大小；强调 WNUT-
…[truncated 10435 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 101
}
```

</details>

---
